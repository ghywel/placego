// The native Metal host for the quaddirectional shader — P2 of METALPORT.md.
//
// This is the engine without the UI: it loads the generated pass graph
// (gen.sh -> generated/), reimplements the patch's window semantics
// natively (rts_mix in source-frame units relative to the output
// timestamp, negative/zero at-or-before; pair_changed on window advance;
// hook fires only with exactly 4 frames, hold otherwise), renders a
// synthetic constant-velocity scene, and checks the output against
// analytic truth. CLI:
//
//   QuadDemo [--frames N] [--src-fps F] [--out-fps F] [--size WxH]
//
// The correctness gate proper is P3 (export + the existing ladder /
// accelcheck tools); the PSNR-vs-analytic-truth here is first light.
import Metal
import Foundation

// ---------------------------------------------------------------- graph
struct GBind: Codable { let name: String; let kind: String; let slot: Int }
struct GPass: Codable {
    let index: Int; let save: String; let desc: String
    let width_rpn: [String]; let height_rpn: [String]
    let components: Int; let binds: [GBind]
    let out_texture_slot: Int; let params_buffer: Int; let entry: String
}
struct GTex: Codable {
    let name: String; let w: Int?; let h: Int?
    let format: String?; let storage: Bool
}
struct Graph: Codable { let source: String; let textures: [GTex]; let passes: [GPass] }

func evalRPN(_ rpn: [String], w: Int, h: Int) -> Int {
    var st: [Double] = []
    for tok in rpn {
        switch tok {
        case "HOOKED.w": st.append(Double(w))
        case "HOOKED.h": st.append(Double(h))
        case "/": let b = st.removeLast(); let a = st.removeLast(); st.append(a / b)
        case "*": let b = st.removeLast(); let a = st.removeLast(); st.append(a * b)
        case "+": let b = st.removeLast(); let a = st.removeLast(); st.append(a + b)
        case "-": let b = st.removeLast(); let a = st.removeLast(); st.append(a - b)
        default: st.append(Double(tok)!)
        }
    }
    // libplacebo rounds hook output sizes to nearest
    return max(1, Int((st.last ?? 1).rounded()))
}

// ------------------------------------------------------------ arguments
var frames = 24, srcFps = 24.0, outFps = 60.0, W = 1280, H = 720
var inputPath: String? = nil, exportPath: String? = nil, graphDir: String? = nil
var args = Array(CommandLine.arguments.dropFirst())
while !args.isEmpty {
    let a = args.removeFirst()
    switch a {
    case "--frames":  frames = Int(args.removeFirst())!
    case "--src-fps": srcFps = Double(args.removeFirst())!
    case "--out-fps": outFps = Double(args.removeFirst())!
    case "--input":   inputPath = args.removeFirst()   // rgb48le raw frames
    case "--export":  exportPath = args.removeFirst()  // rgb48le raw frames
    case "--graph":   graphDir = args.removeFirst()    // generated/ override
    case "--size":
        let p = args.removeFirst().split(separator: "x")
        W = Int(p[0])!; H = Int(p[1])!
    default: fatalError("unknown arg \(a)")
    }
}
// rgb48le raw input: 6 bytes per pixel, frame count from the file size.
var inputData: Data? = nil
if let ip = inputPath {
    inputData = try Data(contentsOf: URL(fileURLWithPath: ip))
    frames = inputData!.count / (W * H * 6)
}

// -------------------------------------------------------------- engine
let here = URL(fileURLWithPath: CommandLine.arguments[0])
    .deletingLastPathComponent()
// generated/ sits next to Package.swift; find it relative to cwd or the
// package root (swift run executes from the package directory).
var genDir = URL(fileURLWithPath: graphDir ?? "generated")
if graphDir == nil && !FileManager.default.fileExists(atPath: genDir.path) {
    genDir = here.deletingLastPathComponent().deletingLastPathComponent()
        .deletingLastPathComponent().appendingPathComponent("generated")
}
let graph = try JSONDecoder().decode(
    Graph.self, from: Data(contentsOf: genDir.appendingPathComponent("graph.json")))

let dev = MTLCreateSystemDefaultDevice()!
let queue = dev.makeCommandQueue()!
FileHandle.standardError.write("# \(dev.name), \(graph.passes.count) passes\n".data(using: .utf8)!)

// Pipelines, compiled concurrently (68 sequential runtime compiles drag).
var psos = [MTLComputePipelineState?](repeating: nil, count: graph.passes.count)
let psoLock = NSLock()
DispatchQueue.concurrentPerform(iterations: graph.passes.count) { i in
    let p = graph.passes[i]
    let stem = String(format: "%02d_%@", p.index, p.save)
    do {
        let src = try String(contentsOf: genDir.appendingPathComponent("\(stem).metal"),
                             encoding: .utf8)
        let lib = try dev.makeLibrary(source: src, options: nil)
        let pso = try dev.makeComputePipelineState(function: lib.makeFunction(name: p.entry)!)
        psoLock.lock(); psos[i] = pso; psoLock.unlock()
    } catch { fatalError("pipeline \(stem): \(error)") }
}

func makeTex(_ w: Int, _ h: Int, _ fmt: MTLPixelFormat,
             usage: MTLTextureUsage, shared: Bool = false) -> MTLTexture {
    let d = MTLTextureDescriptor.texture2DDescriptor(
        pixelFormat: fmt, width: w, height: h, mipmapped: false)
    d.usage = usage; d.storageMode = shared ? .shared : .private
    return dev.makeTexture(descriptor: d)!
}

// Storage textures (the persistent flow caches) — fixed sizes, rgba32f.
var storageTex: [String: MTLTexture] = [:]
for t in graph.textures where t.storage {
    storageTex[t.name] = makeTex(t.w!, t.h!, .rgba32Float,
                                 usage: [.shaderRead, .shaderWrite])
}
// SAVE intermediates — sized by RPN, DOUBLE-BUFFERED: refinement passes
// bind and save the same name (ping-pong), which libplacebo handles by
// double-buffering internally; a single texture would read-write race.
// front(name) = latest written, back(name) = next write target.
let dumpMode = ProcessInfo.processInfo.environment["DUMP"] != nil
var passPair: [String: [MTLTexture]] = [:]
var passFront: [String: Int] = [:]
for p in graph.passes where passPair[p.save] == nil {
    let pw = evalRPN(p.width_rpn, w: W, h: H)
    let ph = evalRPN(p.height_rpn, w: W, h: H)
    let shared = p.save == "FRAME_MIX" || dumpMode
    // rgba16Float, production-faithful. rgba32Float was tried against the
    // jerk deviation and REFUTED (18.0% vs 17.9% -- no change) at 3x the
    // bandwidth cost (5 fps vs 15), so precision of intermediates is not
    // a factor at the measured scales. FRAME_MIX readback stride below
    // must match this choice.
    passPair[p.save] = [
        makeTex(pw, ph, .rgba16Float, usage: [.shaderRead, .shaderWrite], shared: shared),
        makeTex(pw, ph, .rgba16Float, usage: [.shaderRead, .shaderWrite], shared: shared),
    ]
    passFront[p.save] = 0
}
func front(_ name: String) -> MTLTexture { passPair[name]![passFront[name]!] }
func back(_ name: String) -> MTLTexture { passPair[name]![1 - passFront[name]!] }
// The 4-frame window ring. UNORM16, not float16: production libplacebo
// samples the original 16-bit video planes, and float16 at mid-gray has
// only ~1/16 of unorm16's resolution -- measured as an 11-17 dB deficit
// on low-contrast ladder cases (L5, M4) and a quantisation floor at the
// near-ceiling ones (L0, L1) before this was fixed.
let frameTex = (0..<4).map { _ in
    makeTex(W, H, .rgba16Unorm, usage: [.shaderRead], shared: true)
}

let sd = MTLSamplerDescriptor()
sd.minFilter = .linear; sd.magFilter = .linear
sd.sAddressMode = .clampToEdge; sd.tAddressMode = .clampToEdge
sd.normalizedCoordinates = true
let sampler = dev.makeSamplerState(descriptor: sd)!

// Params buffers, one per pass (layout depends on the sampled-bind count).
// std140: out_size at 0; one vec2 per sampled bind; vec4 rts_pack[2]
// 16-aligned; int pair_changed. See gen_metal.py's shim contract.
struct ParamsLayout { let rtsOffset: Int; let pcOffset: Int; let size: Int }
func layout(sampledCount n: Int) -> ParamsLayout {
    let afterSizes = 8 + 8 * n
    let rts = (afterSizes + 15) / 16 * 16
    return ParamsLayout(rtsOffset: rts, pcOffset: rts + 32,
                        size: (rts + 36 + 15) / 16 * 16)
}
var paramsBufs: [MTLBuffer] = graph.passes.map { p in
    let n = p.binds.filter { $0.kind != "storage" }.count
    return dev.makeBuffer(length: layout(sampledCount: n).size,
                          options: .storageModeShared)!
}

// ------------------------------------------------------ synthetic scene
// Smooth textured pattern moving at constant velocity: the design
// envelope (wavelengths 14-40 px, strong 5x5 contrast) and truth known
// analytically at any t. Velocity 6 px/frame — inside the ~23 px reach.
let VX = 6.0
func scene(_ x: Double, _ y: Double, _ t: Double) -> Float {
    // Multi-scale: long wavelengths dominate so the 1/16-res one-tap luma
    // downsample (same as the production pipeline's) stays under Nyquist;
    // moderate mid-scale for the refine levels; a whisper of fine detail.
    // A near-pure 14-31 px tone field aliases at the coarse level and can
    // even reverse apparent motion -- measured here first-hand at -8.7 px
    // for a +6 px truth. Same lesson as P0, opposite direction.
    let u = x - VX * t
    let a = 0.5 + 0.16 * sin(2 * .pi * u / 173.0) + 0.13 * sin(2 * .pi * u / 89.0 + 0.7)
    let b = 0.09 * sin(2 * .pi * (u + 0.6 * y) / 127.0) + 0.07 * sin(2 * .pi * y / 97.0)
    let c = 0.05 * sin(2 * .pi * u / 47.0 + 2.1) + 0.02 * sin(2 * .pi * (u - y) / 19.0)
    return Float(min(max(a + b + c, 0.0), 1.0))
}
func fillFrame(_ tex: MTLTexture, t: Double) {
    var row = [UInt16](repeating: 0, count: W * 4)
    if let data = inputData {
        // rgb48le raw source frame at index t (integer by construction) --
        // a straight 16-bit copy into the unorm texture, no quantisation.
        let base = Int(t.rounded()) * W * H * 6
        data.withUnsafeBytes { (raw: UnsafeRawBufferPointer) in
            let u16 = raw.baseAddress!.advanced(by: base)
                .assumingMemoryBound(to: UInt16.self)
            for y in 0..<H {
                for x in 0..<W {
                    let p = (y * W + x) * 3
                    row[x * 4]     = UInt16(littleEndian: u16[p])
                    row[x * 4 + 1] = UInt16(littleEndian: u16[p + 1])
                    row[x * 4 + 2] = UInt16(littleEndian: u16[p + 2])
                    row[x * 4 + 3] = 65535
                }
                row.withUnsafeBytes {
                    tex.replace(region: MTLRegionMake2D(0, y, W, 1), mipmapLevel: 0,
                                withBytes: $0.baseAddress!, bytesPerRow: W * 8)
                }
            }
        }
        return
    }
    for y in 0..<H {
        for x in 0..<W {
            let v = UInt16((min(max(scene(Double(x) + 0.5, Double(y) + 0.5, t), 0), 1) * 65535).rounded())
            row[x * 4] = v; row[x * 4 + 1] = v; row[x * 4 + 2] = v; row[x * 4 + 3] = 65535
        }
        row.withUnsafeBytes {
            tex.replace(region: MTLRegionMake2D(0, y, W, 1), mipmapLevel: 0,
                        withBytes: $0.baseAddress!, bytesPerRow: W * 8)
        }
    }
}
// rgb48le export: matches ffmpeg's -pix_fmt rgb48le rawvideo, so the
// existing tools (analyze-style PSNR, accelcheck.py) read it unchanged.
let exportHandle: FileHandle? = exportPath.map {
    FileManager.default.createFile(atPath: $0, contents: nil)
    return FileHandle(forWritingAtPath: $0)!
}
var exportRow = [UInt16](repeating: 0, count: W * H * 3)
func exportPixels(_ px: [Float16]) {
    for i in 0..<(W * H) {
        for c in 0..<3 {
            let v = max(0.0, min(1.0, Float(px[i * 4 + c])))
            exportRow[i * 3 + c] = UInt16((v * 65535.0).rounded()).littleEndian
        }
    }
    exportRow.withUnsafeBytes { exportHandle!.write(Data($0)) }
}
func exportSourceFrame(_ idx: Int) {
    // Edge hold: emit the nearest source frame verbatim, as the ffmpeg
    // pipeline's zero-order-hold fallback does when the window can't form.
    if let data = inputData {
        let base = idx * W * H * 6
        exportHandle!.write(data.subdata(in: base..<(base + W * H * 6)))
    } else {
        var px = [Float16](repeating: 0, count: W * H * 4)
        for y in 0..<H { for x in 0..<W {
            let v = Float16(scene(Double(x) + 0.5, Double(y) + 0.5, Double(idx)))
            px[(y * W + x) * 4] = v; px[(y * W + x) * 4 + 1] = v; px[(y * W + x) * 4 + 2] = v
        } }
        exportPixels(px)
    }
}

// ------------------------------------------------------------- render
var prevWindow: [Int] = []
var outPix = [Float16](repeating: 0, count: W * H * 4)
var interpPSNR: [Double] = []
var passthroughPSNR: [Double] = []
var frameCache: [Int: Int] = [:]   // source index -> ring slot
var ringNext = 0

// ffmpeg emits ceil(duration * out_fps) frames for a duration-long clip;
// match it so exported timelines align frame-for-frame with the truth.
let outCount = Int((Double(frames) * outFps / srcFps).rounded())
let t0 = DispatchTime.now()
for k in 0..<outCount {
    let tSrc = Double(k) * srcFps / outFps      // output time in source-frame units
    let i = Int(tSrc.rounded(.down))
    let window = [i - 1, i, i + 1, i + 2]
    guard window[0] >= 0, window[3] < frames else {
        if exportHandle != nil { exportSourceFrame(min(max(Int(tSrc.rounded()), 0), frames - 1)) }
        continue  // hold at edges, as the ffmpeg pipeline does
    }

    // Load any window frames not already resident (4-slot ring, ascending).
    var slotTex: [MTLTexture] = []
    for idx in window {
        if frameCache[idx] == nil {
            let slot = ringNext; ringNext = (ringNext + 1) % 4
            frameCache = frameCache.filter { $0.value != slot }
            fillFrame(frameTex[slot], t: Double(idx))
            frameCache[idx] = slot
        }
        slotTex.append(frameTex[frameCache[idx]!])
    }
    let pairChanged: Int32 = window == prevWindow ? 0 : 1
    prevWindow = window
    let rts = window.map { Float(Double($0) - tSrc) }

    let cb = queue.makeCommandBuffer()!
    let enc = cb.makeComputeCommandEncoder()!
    for (pi, p) in graph.passes.enumerated() {
        let pw = passPair[p.save]![0].width, ph = passPair[p.save]![0].height
        let sampled = p.binds.filter { $0.kind != "storage" }
        let lay = layout(sampledCount: sampled.count)
        let buf = paramsBufs[pi].contents()
        var f2: [Float] = [Float(pw), Float(ph)]
        memcpy(buf, &f2, 8)
        for (j, bnd) in sampled.enumerated() {
            let t: MTLTexture = bnd.kind == "frame"
                ? slotTex[bnd.name == "HOOKED" ? 0 : Int(bnd.name.dropFirst(5))!]
                : front(bnd.name)
            var s: [Float] = [Float(t.width), Float(t.height)]
            memcpy(buf + 8 + 8 * j, &s, 8)
        }
        var rtsPack = [Float](repeating: 0, count: 8)
        for (j, r) in rts.enumerated() { rtsPack[j] = r }
        memcpy(buf + lay.rtsOffset, &rtsPack, 32)
        var pc = pairChanged
        memcpy(buf + lay.pcOffset, &pc, 4)

        enc.setComputePipelineState(psos[pi]!)
        enc.setBuffer(paramsBufs[pi], offset: 0, index: p.params_buffer)
        var texSlot = 0
        for bnd in p.binds {
            let t: MTLTexture
            switch bnd.kind {
            case "frame": t = slotTex[bnd.name == "HOOKED" ? 0 : Int(bnd.name.dropFirst(5))!]
            case "pass": t = front(bnd.name)
            default: t = storageTex[bnd.name]!
            }
            enc.setTexture(t, index: texSlot)
            if bnd.kind != "storage" { enc.setSamplerState(sampler, index: texSlot) }
            texSlot += 1
        }
        enc.setTexture(back(p.save), index: p.out_texture_slot)
        enc.dispatchThreads(MTLSize(width: pw, height: ph, depth: 1),
                            threadsPerThreadgroup: MTLSize(width: 16, height: 16, depth: 1))
        enc.memoryBarrier(scope: .textures)
        passFront[p.save] = 1 - passFront[p.save]!   // encode-time flip
    }
    enc.endEncoding()
    cb.commit(); cb.waitUntilCompleted()
    if let e = cb.error { fatalError("frame \(k): \(e)") }

    if ProcessInfo.processInfo.environment["DUMP"] != nil && k == 3 {
        for p in graph.passes {
            let t = front(p.save)
            var px = [Float16](repeating: 0, count: t.width * t.height * 4)
            t.getBytes(&px, bytesPerRow: t.width * 8,
                       from: MTLRegionMake2D(0, 0, t.width, t.height), mipmapLevel: 0)
            var mean = 0.0; var nz = 0
            for i in 0..<(t.width * t.height) {
                let v = Double(px[i * 4]); mean += v; if v != 0 { nz += 1 }
            }
            mean /= Double(t.width * t.height)
            let name = p.save.padding(toLength: 24, withPad: " ", startingAt: 0)
            print("pass \(String(format: "%02d", p.index)) \(name) "
                  + "\(t.width)x\(t.height)\t"
                  + String(format: "meanR=%+.4f nonzero=%d%%", mean,
                           nz * 100 / (t.width * t.height)))
        }
        exit(0)
    }
    // Readback: export and/or first-light metric.
    let out = front("FRAME_MIX")
    out.getBytes(&outPix, bytesPerRow: W * 8,
                 from: MTLRegionMake2D(0, 0, W, H), mipmapLevel: 0)
    if exportHandle != nil { exportPixels(outPix) }
    if inputData != nil { continue }  // no analytic truth for file input
    var se = 0.0
    for y in stride(from: 8, to: H - 8, by: 3) {       // skip edges, sample rows
        for x in stride(from: 8, to: W - 8, by: 3) {
            let d = Double(outPix[(y * W + x) * 4]) - Double(scene(Double(x) + 0.5, Double(y) + 0.5, tSrc))
            se += d * d
        }
    }
    let n = Double(((H - 16 + 2) / 3) * ((W - 16 + 2) / 3))
    let psnr = 10 * log10(1.0 / (se / n + 1e-12))
    let s = tSrc - Double(i)
    if abs(s) < 1e-6 { passthroughPSNR.append(psnr) } else { interpPSNR.append(psnr) }
}
let dt = Double(DispatchTime.now().uptimeNanoseconds - t0.uptimeNanoseconds) / 1e9

func stats(_ v: [Double]) -> String {
    guard !v.isEmpty else { return "none" }
    let s = v.sorted()
    return String(format: "n=%d min=%.2f median=%.2f mean=%.2f",
                  v.count, s.first!, s[v.count / 2], v.reduce(0, +) / Double(v.count))
}
print("rendered \(interpPSNR.count + passthroughPSNR.count) frames in \(String(format: "%.1f", dt))s "
      + "(\(String(format: "%.1f", Double(interpPSNR.count + passthroughPSNR.count) / dt)) fps)")
print("passthrough PSNR vs truth: \(stats(passthroughPSNR))")
print("interpolated PSNR vs truth: \(stats(interpPSNR))")
