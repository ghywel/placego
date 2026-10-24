// P1 host driver (GPU-METAL-JOBS.md §J.1 revision 2; Local, 2026-10-24).
// usage: p1engine JOB.json OUT.json
// Reads a job, compiles lanes.metal at run time (LANE64 for 64-lane words), runs batches of lane-groups on the GPU,
// reduces on the CPU with exact 64-bit counts, and writes one JSON result. Nothing is claimed by the driver: the
// Python harness (p1_lane_engine.py) checks every result against independent scalar code.
//
// Modes: "census" lanes n in [lo, hi) (decimal strings, 64-bit); "list" the given indices; "rows" uploaded starts
// (hex, depth j+1 = bit j) with an explicit support bound Wsup, no reconstruction (edge-case controls).

import Foundation
import Metal

struct Params { var W: UInt32; var T: UInt32; var Wsup: UInt32; var L: UInt32; var G: UInt32; var traceSteps: UInt32 }

func fail(_ msg: String, _ out: String?) -> Never {
    if let out = out {
        let obj: [String: Any] = ["status": "error", "error": msg]
        if let d = try? JSONSerialization.data(withJSONObject: obj, options: [.prettyPrinted, .sortedKeys]) { try? d.write(to: URL(fileURLWithPath: out)) }
    }
    FileHandle.standardError.write(("p1engine error: " + msg + "\n").data(using: .utf8)!)
    exit(2)
}

let args = CommandLine.arguments
guard args.count == 3 else { fail("usage: p1engine JOB.json OUT.json", nil) }
let outPath = args[2]
guard let jobData = FileManager.default.contents(atPath: args[1]),
      let job = (try? JSONSerialization.jsonObject(with: jobData)) as? [String: Any] else { fail("cannot read job", outPath) }

func int(_ k: String, _ dflt: Int? = nil) -> Int {
    if let v = job[k] as? NSNumber { return v.intValue }
    if let v = job[k] as? String, let i = Int(v) { return i }
    if let d = dflt { return d }
    fail("missing integer field \(k)", outPath)
}
func u64(_ s: Any?) -> UInt64? {
    if let v = s as? String { return UInt64(v) }
    if let v = s as? NSNumber { return v.uint64Value }
    return nil
}

let laneBits = int("lane_bits", 32)
guard laneBits == 32 || laneBits == 64 else { fail("lane_bits must be 32 or 64", outPath) }
let LW = laneBits
let mode = (job["mode"] as? String) ?? ""
let W = int("W", 0), T = int("T")
guard T >= 0 && T <= 65534 else { fail("T out of range (death times are 16-bit, 0xFFFF = censored)", outPath) }
let Gmax = int("G_max", 1 << 16)
let tgReq = int("tg", 0)
let budget = int("gpu_budget_bytes", 2 << 30)
let traceSteps = int("trace_steps", 0)
let samplePerBatch = int("sample_per_batch", 64)
let sampleSeed = UInt64(int("sample_seed", 1))
guard let metalPath = job["metal"] as? String, let src = try? String(contentsOfFile: metalPath, encoding: .utf8) else { fail("cannot read metal source", outPath) }

guard let device = MTLCreateSystemDefaultDevice() else { fail("no Metal device", outPath) }
let opts = MTLCompileOptions()
var macros: [String: NSObject] = [:]
if LW == 64 { macros["LANE64"] = NSNumber(value: 1) }
let mutant = (job["mutant"] as? String) ?? ""
if mutant == "drop_edge" { macros["MUTANT_DROP_EDGE"] = NSNumber(value: 1) } else if !mutant.isEmpty { fail("unknown mutant \(mutant)", outPath) }
opts.preprocessorMacros = macros
let library: MTLLibrary
do { library = try device.makeLibrary(source: src, options: opts) } catch { fail("metal compile: \(error)", outPath) }
guard let fBuild = library.makeFunction(name: "build_start"), let fSim = library.makeFunction(name: "simulate"),
      let pBuild = try? device.makeComputePipelineState(function: fBuild),
      let pSim = try? device.makeComputePipelineState(function: fSim),
      let queue = device.makeCommandQueue() else { fail("pipeline creation failed", outPath) }

var families: [Int] = []
for raw in [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 2002, 3001, 3002, 3003, 5001, 5002, 5003] {
    if let f = MTLGPUFamily(rawValue: raw), device.supportsFamily(f) { families.append(raw) }
}
let deviceInfo: [String: Any] = [
    "name": device.name, "families_supported_raw": families, "has_unified_memory": device.hasUnifiedMemory,
    "max_threadgroup_memory_length": device.maxThreadgroupMemoryLength, "max_buffer_length": device.maxBufferLength,
    "recommended_max_working_set_size": device.recommendedMaxWorkingSetSize,
    "max_threads_per_threadgroup": [device.maxThreadsPerThreadgroup.width, device.maxThreadsPerThreadgroup.height, device.maxThreadsPerThreadgroup.depth],
]
let pipelineInfo: [String: Any] = [
    "build_thread_execution_width": pBuild.threadExecutionWidth, "build_max_total_threads_per_threadgroup": pBuild.maxTotalThreadsPerThreadgroup,
    "sim_thread_execution_width": pSim.threadExecutionWidth, "sim_max_total_threads_per_threadgroup": pSim.maxTotalThreadsPerThreadgroup,
    "build_static_threadgroup_memory_length": pBuild.staticThreadgroupMemoryLength, "sim_static_threadgroup_memory_length": pSim.staticThreadgroupMemoryLength,
]

// ---- the lane-groups to run: (base index, valid mask) per group, plus the uploaded starts in rows mode -------------
let laneBytes = LW / 8
var groupBase: [UInt64] = []
var groupValid: [UInt64] = []          // low LW bits used
var listIndices: [UInt64] = []
var rowStarts: [[UInt64]] = []          // rows mode: per lane, the start's words of 64 depths (depth j+1 = bit j)
var Wsup = W
var lo: UInt64 = 0, hi: UInt64 = 0
let fullMask: UInt64 = LW == 64 ? UInt64.max : (UInt64(1) << UInt64(LW)) - 1

switch mode {
case "census":
    guard let l = u64(job["lo"]), let h = u64(job["hi"]), h > l else { fail("census needs lo < hi", outPath) }
    let nb = W / 2
    if nb < 64 { guard h <= (UInt64(1) << UInt64(nb)) else { fail("hi exceeds 2^floor(W/2)", outPath) } }
    lo = l; hi = h
    var b = (l / UInt64(LW)) * UInt64(LW)
    while b < h {
        var m: UInt64 = 0
        for i in 0..<LW { let n = b + UInt64(i); if n >= l && n < h { m |= UInt64(1) << UInt64(i) } }
        groupBase.append(b); groupValid.append(m); b += UInt64(LW)
    }
case "list":
    guard let arr = job["indices"] as? [Any], !arr.isEmpty else { fail("list needs indices", outPath) }
    listIndices = arr.compactMap { u64($0) }
    guard listIndices.count == arr.count else { fail("bad index", outPath) }
    let nb = W / 2
    if nb < 64 { for n in listIndices { guard n < (UInt64(1) << UInt64(nb)) else { fail("index exceeds 2^floor(W/2)", outPath) } } }
    var byBase: [UInt64: UInt64] = [:]
    for n in listIndices { let b = (n / UInt64(LW)) * UInt64(LW); byBase[b, default: 0] |= UInt64(1) << (n - b) }
    for b in byBase.keys.sorted() { groupBase.append(b); groupValid.append(byBase[b]!) }
case "rows":
    guard let arr = job["starts"] as? [String], !arr.isEmpty else { fail("rows needs starts", outPath) }
    Wsup = int("Wsup")
    for s in arr {
        var hex = s.lowercased(); if hex.hasPrefix("0x") { hex.removeFirst(2) }
        var words = [UInt64](repeating: 0, count: (Wsup + 63) / 64 + 1)
        var bit = 0
        for ch in hex.reversed() {
            guard let v = ch.hexDigitValue else { fail("bad hex start \(s)", outPath) }
            for j in 0..<4 where (v >> j) & 1 == 1 {
                let p = bit + j
                guard p < Wsup else { fail("start \(s) has a black cell beyond Wsup", outPath) }
                words[p / 64] |= UInt64(1) << UInt64(p % 64)
            }
            bit += 4
        }
        rowStarts.append(words)
    }
    let ng = (rowStarts.count + LW - 1) / LW
    for g in 0..<ng {
        var m: UInt64 = 0
        for i in 0..<LW where g * LW + i < rowStarts.count { m |= UInt64(1) << UInt64(i) }
        groupBase.append(UInt64(g * LW)); groupValid.append(m)
    }
default:
    fail("mode must be census, list or rows", outPath)
}

let L = Wsup + T + 2
let Gtotal = groupBase.count
let Gbatch = min(Gmax, Gtotal)
let liveBytes = Gbatch * (L * laneBytes + 8 + laneBytes + 2 * (W + 1) * laneBytes + LW * 2) + (traceSteps + 1) * L * laneBytes
guard liveBytes <= budget else { fail("live allocation \(liveBytes) bytes exceeds the GPU budget \(budget)", outPath) }
guard L * Gbatch * laneBytes <= device.maxBufferLength else { fail("row buffer exceeds maxBufferLength", outPath) }

guard let bRows = device.makeBuffer(length: max(L * Gbatch * laneBytes, 16), options: .storageModeShared),
      let bBase = device.makeBuffer(length: max(Gbatch * 8, 16), options: .storageModeShared),
      let bValid = device.makeBuffer(length: max(Gbatch * laneBytes, 16), options: .storageModeShared),
      let bWs = device.makeBuffer(length: max(2 * (W + 1) * Gbatch * laneBytes, 16), options: .storageModeShared),
      let bDeath = device.makeBuffer(length: max(Gbatch * LW * 2, 16), options: .storageModeShared),
      let bTrace = device.makeBuffer(length: max((traceSteps + 1) * L * laneBytes, 16), options: .storageModeShared)
else { fail("buffer allocation failed", outPath) }

func tgSize(_ p: MTLComputePipelineState, _ n: Int) -> Int {
    var t = tgReq > 0 ? tgReq : min(256, p.maxTotalThreadsPerThreadgroup)
    t = min(t, p.maxTotalThreadsPerThreadgroup); return max(1, min(t, n))
}

func runKernel(_ p: MTLComputePipelineState, _ bufs: [(Int, MTLBuffer)], _ params: inout Params, paramIndex: Int, n: Int) -> (Double, Double) {
    let cb = queue.makeCommandBuffer()!
    let enc = cb.makeComputeCommandEncoder()!
    enc.setComputePipelineState(p)
    for (i, b) in bufs { enc.setBuffer(b, offset: 0, index: i) }
    enc.setBytes(&params, length: MemoryLayout<Params>.stride, index: paramIndex)
    enc.dispatchThreads(MTLSize(width: n, height: 1, depth: 1), threadsPerThreadgroup: MTLSize(width: tgSize(p, n), height: 1, depth: 1))
    enc.endEncoding()
    let w0 = Date()
    cb.commit(); cb.waitUntilCompleted()
    let wall = Date().timeIntervalSince(w0)
    if let e = cb.error { fail("command buffer error: \(e)", outPath) }
    return (cb.gpuEndTime - cb.gpuStartTime, wall)
}

// ---- batches --------------------------------------------------------------------------------------------------------
var histogram: [Int: UInt64] = [:]
var censored: UInt64 = 0, lanesTotal: UInt64 = 0
var maxDeath = -1, maxCount: UInt64 = 0
var maximizers: [String] = []
var batches: [[String: Any]] = []
var listDeaths: [[String: Any]] = []
var rowDeaths: [Int] = []
var traceDump: [[String]] = []
var deathsHandle: FileHandle? = nil
if mode == "census", let p = job["deaths_out"] as? String {
    FileManager.default.createFile(atPath: p, contents: nil); deathsHandle = FileHandle(forWritingAtPath: p)
}
var lcg = sampleSeed &* 6364136223846793005 &+ 1442695040888963407
func rnd() -> UInt64 { lcg = lcg &* 6364136223846793005 &+ 1442695040888963407; return lcg >> 11 }

let t0 = Date()
var g0 = 0
var batchNo = 0
while g0 < Gtotal {
    let G = min(Gbatch, Gtotal - g0)
    let tp0 = Date()
    let pBase = bBase.contents().bindMemory(to: UInt64.self, capacity: G)
    for i in 0..<G { pBase[i] = groupBase[g0 + i] }
    if LW == 64 { let pv = bValid.contents().bindMemory(to: UInt64.self, capacity: G); for i in 0..<G { pv[i] = groupValid[g0 + i] } }
    else { let pv = bValid.contents().bindMemory(to: UInt32.self, capacity: G); for i in 0..<G { pv[i] = UInt32(truncatingIfNeeded: groupValid[g0 + i]) } }
    var params = Params(W: UInt32(W), T: UInt32(T), Wsup: UInt32(Wsup), L: UInt32(L), G: UInt32(G), traceSteps: UInt32(traceSteps))
    var tBuildGpu = 0.0, tBuildWall = 0.0
    if mode == "rows" {
        // upload the rows: row k of group g, bit l = depth k of start (g*LW + l); the wall and the halo zero
        memset(bRows.contents(), 0, L * G * laneBytes)
        for gi in 0..<G {
            for l in 0..<LW {
                let s = (g0 + gi) * LW + l; if s >= rowStarts.count { break }
                for k in 1...Wsup where (rowStarts[s][(k - 1) / 64] >> UInt64((k - 1) % 64)) & 1 == 1 {
                    let idx = k * G + gi
                    if LW == 64 { bRows.contents().bindMemory(to: UInt64.self, capacity: L * G)[idx] |= UInt64(1) << UInt64(l) }
                    else { bRows.contents().bindMemory(to: UInt32.self, capacity: L * G)[idx] |= UInt32(1) << UInt32(l) }
                }
            }
        }
    }
    let tPrep = Date().timeIntervalSince(tp0)
    if mode != "rows" {
        (tBuildGpu, tBuildWall) = runKernel(pBuild, [(0, bRows), (1, bBase), (2, bWs)], &params, paramIndex: 3, n: G)
    }
    let (tSimGpu, tSimWall) = runKernel(pSim, [(0, bRows), (1, bValid), (2, bDeath), (4, bTrace)], &params, paramIndex: 3, n: G)
    let tr0 = Date()
    let pd = bDeath.contents().bindMemory(to: UInt16.self, capacity: G * LW)
    var bMax = -1, bMaxCount: UInt64 = 0, bCens: UInt64 = 0, bLanes: UInt64 = 0
    var samples: [[String]] = []
    var firstValid: (UInt64, Int)? = nil, lastValid: (UInt64, Int)? = nil
    for gi in 0..<G {
        let m = groupValid[g0 + gi]; if m == 0 { continue }
        let b = groupBase[g0 + gi]
        for l in 0..<LW where (m >> UInt64(l)) & 1 == 1 {
            let d = Int(pd[gi * LW + l]); let n = b + UInt64(l)
            bLanes += 1
            if firstValid == nil { firstValid = (n, d) }
            lastValid = (n, d)
            if d == 0xFFFF { bCens += 1 } else {
                histogram[d, default: 0] += 1
                if d > bMax { bMax = d; bMaxCount = 1 } else if d == bMax { bMaxCount += 1 }
                if d > maxDeath { maxDeath = d; maxCount = 1; maximizers = [String(n)] }
                else if d == maxDeath { maxCount += 1; if maximizers.count < 4096 { maximizers.append(String(n)) } }
            }
            if mode == "list" { listDeaths.append(["index": String(n), "death": d == 0xFFFF ? -1 : d]) }
            if mode == "rows" { rowDeaths.append(d == 0xFFFF ? -1 : d) }
        }
    }
    // deterministic sample: first and last valid lanes, the lanes either side of the first group boundary, then seeded picks
    if samplePerBatch > 0 && mode == "census" {
        var picks: [UInt64] = []
        if let f = firstValid { picks.append(f.0) }
        if let l = lastValid { picks.append(l.0) }
        if G >= 2 { picks.append(groupBase[g0] + UInt64(LW - 1)); picks.append(groupBase[g0 + 1]) }
        var tries = 0
        while picks.count < samplePerBatch && tries < samplePerBatch * 8 {
            tries += 1
            let gi = Int(rnd() % UInt64(G)); let l = Int(rnd() % UInt64(LW))
            if (groupValid[g0 + gi] >> UInt64(l)) & 1 == 1 { picks.append(groupBase[g0 + gi] + UInt64(l)) }
        }
        var seen = Set<UInt64>()
        for n in picks where !seen.contains(n) {
            seen.insert(n)
            let gi = Int((n - groupBase[g0]) / UInt64(LW)); let l = Int(n % UInt64(LW))
            guard gi < G, (groupValid[g0 + gi] >> UInt64(l)) & 1 == 1 else { continue }
            let d = Int(pd[gi * LW + l]); samples.append([String(n), String(d == 0xFFFF ? -1 : d)])
        }
    }
    if let h = deathsHandle {
        // range order: lanes lo..hi-1 of this batch, contiguous
        var out = Data(capacity: Int(bLanes) * 2)
        for gi in 0..<G {
            let m = groupValid[g0 + gi]
            for l in 0..<LW where (m >> UInt64(l)) & 1 == 1 { var v = pd[gi * LW + l]; withUnsafeBytes(of: &v) { out.append(contentsOf: $0) } }
        }
        h.write(out)
    }
    let tReduce = Date().timeIntervalSince(tr0)
    censored += bCens; lanesTotal += bLanes
    batches.append(["batch": batchNo, "first_group_base": String(groupBase[g0]), "groups": G, "lanes": bLanes, "t_prep_s": tPrep,
                    "t_build_gpu_s": tBuildGpu, "t_build_wall_s": tBuildWall, "t_sim_gpu_s": tSimGpu, "t_sim_wall_s": tSimWall,
                    "t_reduce_s": tReduce, "max": bMax, "max_count": bMaxCount, "censored": bCens, "samples": samples])
    g0 += G; batchNo += 1
}
try? deathsHandle?.close()

// trace dump (rows mode): group 0 of the last batch wrote its rows for t = 0..traceSteps (a single-batch job is required)
if traceSteps > 0 && mode == "rows" {
    guard batchNo == 1 else { fail("trace_steps needs a single batch", outPath) }
    for t in 0...traceSteps {
        var rowHex: [String] = []
        for k in 0..<L {
            let v: UInt64 = LW == 64 ? bTrace.contents().bindMemory(to: UInt64.self, capacity: (traceSteps + 1) * L)[t * L + k]
                                     : UInt64(bTrace.contents().bindMemory(to: UInt32.self, capacity: (traceSteps + 1) * L)[t * L + k])
            rowHex.append(String(v, radix: 16))
        }
        traceDump.append(rowHex)
    }
}

var hist: [String: UInt64] = [:]
for (k, v) in histogram { hist[String(k)] = v }
var result: [String: Any] = [
    "status": "ok", "mode": mode, "lane_bits": LW, "mutant": mutant, "W": W, "T": T, "Wsup": Wsup, "L": L,
    "groups_total": Gtotal, "G_batch": Gbatch, "live_bytes": liveBytes, "gpu_budget_bytes": budget,
    "threadgroup_build": tgSize(pBuild, Gbatch), "threadgroup_sim": tgSize(pSim, Gbatch),
    "device": deviceInfo, "pipeline": pipelineInfo, "batches": batches,
    "lanes_total": lanesTotal, "histogram": hist, "max": maxDeath, "max_count": maxCount, "censored": censored,
    "maximizers": maximizers, "maximizers_truncated": maxCount > UInt64(maximizers.count), "wall_total_s": Date().timeIntervalSince(t0),
]
if mode == "census" { result["lo"] = String(lo); result["hi"] = String(hi) }
if mode == "list" { result["deaths"] = listDeaths }
if mode == "rows" { result["deaths"] = rowDeaths; if traceSteps > 0 { result["trace"] = traceDump } }
guard let outData = try? JSONSerialization.data(withJSONObject: result, options: [.prettyPrinted, .sortedKeys]) else { fail("json encode", outPath) }
do { try outData.write(to: URL(fileURLWithPath: outPath)) } catch { fail("write output: \(error)", nil) }
