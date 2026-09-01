// QuadEngine — the native Metal host for the generated pass graph, as a
// library. Extracted from the P2 CLI so the demo UI (P4) and the CLI share
// one engine. Semantics are the verified P3 set: the patch's rts_mix
// units, pair_changed on window advance, slot-keyed persistent storage
// caches, double-buffered SAVE targets with encode-time flip, unorm16
// frame ring, fp16 intermediates (rgba32Float refuted, see METALPORT.md).
import Metal
import Foundation

public struct GBind: Codable { public let name: String; public let kind: String; public let slot: Int }
public struct GPass: Codable {
    public let index: Int; public let save: String; public let desc: String
    public let width_rpn: [String]; public let height_rpn: [String]
    public let components: Int; public let binds: [GBind]
    public let out_texture_slot: Int; public let params_buffer: Int; public let entry: String
}
public struct GTex: Codable {
    public let name: String; public let w: Int?; public let h: Int?
    public let format: String?; public let storage: Bool
}
public struct Graph: Codable {
    public let source: String; public let textures: [GTex]; public let passes: [GPass]
}

public func evalRPN(_ rpn: [String], w: Int, h: Int) -> Int {
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
    return max(1, Int((st.last ?? 1).rounded()))   // libplacebo rounds to nearest
}

public final class Engine {
    public let device: MTLDevice
    public let graph: Graph
    public let width: Int, height: Int
    public var srcFps: Double, outFps: Double
    public var frameCount: Int

    /// CPU source: fill this rgba16Unorm texture with source frame `idx`.
    public var fillFrame: ((MTLTexture, Int) -> Void)?
    /// Zero-copy source: return a ready texture for source frame `idx`
    /// (any unorm format; caller keeps the 4 window textures alive).
    /// Takes precedence over fillFrame when set.
    public var provideFrame: ((Int) -> MTLTexture)?
    /// Treat the source as a seamless loop: window indices wrap modulo
    /// frameCount instead of collapsing to hold at the sequence ends.
    /// Only correct when the content is seam-periodic — the synthetic
    /// scenes built to close their loops — never for real video.
    public var loops = false

    private let queue: MTLCommandQueue
    private var psos: [MTLComputePipelineState] = []
    private var storageTex: [String: MTLTexture] = [:]
    private var passPair: [String: [MTLTexture]] = [:]
    private var passFront: [String: Int] = [:]
    private var frameTex: [MTLTexture] = []
    private let sampler: MTLSamplerState
    private var paramsBufs: [MTLBuffer] = []
    private var prevWindow: [Int] = []
    private var frameCache: [Int: Int] = [:]
    private var ringNext = 0

    public var outCount: Int { Int((Double(frameCount) * outFps / srcFps).rounded()) }

    public init(graphDir: URL, width: Int, height: Int,
                srcFps: Double = 24, outFps: Double = 60, frameCount: Int = 24,
                device: MTLDevice? = nil, sharedIntermediates: Bool = false) throws {
        self.device = device ?? MTLCreateSystemDefaultDevice()!
        self.width = width; self.height = height
        self.srcFps = srcFps; self.outFps = outFps; self.frameCount = frameCount
        self.queue = self.device.makeCommandQueue()!
        self.graph = try JSONDecoder().decode(
            Graph.self, from: Data(contentsOf: graphDir.appendingPathComponent("graph.json")))

        // Pipelines, compiled concurrently (68 sequential compiles drag).
        var built = [MTLComputePipelineState?](repeating: nil, count: graph.passes.count)
        var firstError: Error? = nil
        let lock = NSLock()
        let dev = self.device, passes = graph.passes
        DispatchQueue.concurrentPerform(iterations: passes.count) { i in
            let p = passes[i]
            let stem = String(format: "%02d_%@", p.index, p.save)
            do {
                let src = try String(contentsOf: graphDir.appendingPathComponent("\(stem).metal"),
                                     encoding: .utf8)
                let lib = try dev.makeLibrary(source: src, options: nil)
                let pso = try dev.makeComputePipelineState(function: lib.makeFunction(name: p.entry)!)
                lock.lock(); built[i] = pso; lock.unlock()
            } catch { lock.lock(); firstError = firstError ?? error; lock.unlock() }
        }
        if let e = firstError { throw e }
        psos = built.map { $0! }

        func makeTex(_ w: Int, _ h: Int, _ fmt: MTLPixelFormat,
                     usage: MTLTextureUsage, shared: Bool = false) -> MTLTexture {
            let d = MTLTextureDescriptor.texture2DDescriptor(
                pixelFormat: fmt, width: w, height: h, mipmapped: false)
            d.usage = usage; d.storageMode = shared ? .shared : .private
            return dev.makeTexture(descriptor: d)!
        }
        for t in graph.textures where t.storage {
            storageTex[t.name] = makeTex(t.w!, t.h!, .rgba32Float,
                                         usage: [.shaderRead, .shaderWrite])
        }
        for p in graph.passes where passPair[p.save] == nil {
            let pw = evalRPN(p.width_rpn, w: width, h: height)
            let ph = evalRPN(p.height_rpn, w: width, h: height)
            let shared = p.save == "FRAME_MIX" || sharedIntermediates
            passPair[p.save] = [
                makeTex(pw, ph, .rgba16Float, usage: [.shaderRead, .shaderWrite], shared: shared),
                makeTex(pw, ph, .rgba16Float, usage: [.shaderRead, .shaderWrite], shared: shared),
            ]
            passFront[p.save] = 0
        }
        frameTex = (0..<4).map { _ in
            makeTex(width, height, .rgba16Unorm, usage: [.shaderRead], shared: true)
        }
        let sd = MTLSamplerDescriptor()
        sd.minFilter = .linear; sd.magFilter = .linear
        sd.sAddressMode = .clampToEdge; sd.tAddressMode = .clampToEdge
        sd.normalizedCoordinates = true
        sampler = dev.makeSamplerState(descriptor: sd)!

        paramsBufs = graph.passes.map { p in
            let n = p.binds.filter { $0.kind != "storage" }.count
            return dev.makeBuffer(length: Engine.layout(sampledCount: n).size,
                                  options: .storageModeShared)!
        }
    }

    struct ParamsLayout { let rtsOffset: Int; let pcOffset: Int; let size: Int }
    static func layout(sampledCount n: Int) -> ParamsLayout {
        let afterSizes = 8 + 8 * n
        let rts = (afterSizes + 15) / 16 * 16
        return ParamsLayout(rtsOffset: rts, pcOffset: rts + 32,
                            size: (rts + 36 + 15) / 16 * 16)
    }

    public func front(_ name: String) -> MTLTexture { passPair[name]![passFront[name]!] }
    private func back(_ name: String) -> MTLTexture { passPair[name]![1 - passFront[name]!] }

    /// Forget window/ring state (e.g. after a seek or loop restart). The
    /// storage caches go stale but the next window is new, so pair_changed
    /// fires and the shader recomputes them — the cache contract holds.
    public func reset() {
        prevWindow = []; frameCache = [:]; ringNext = 0
    }

    public struct Output {
        public let image: MTLTexture     // FRAME_MIX front, or the hold frame
        public let hold: MTLTexture      // nearest source frame (wipe A-side)
        public let wasHold: Bool         // true when the window couldn't form
    }

    private func sourceTexture(_ idx: Int) -> MTLTexture {
        if let provide = provideFrame { return provide(idx) }
        if frameCache[idx] == nil {
            let slot = ringNext; ringNext = (ringNext + 1) % 4
            frameCache = frameCache.filter { $0.value != slot }
            fillFrame?(frameTex[slot], idx)
            frameCache[idx] = slot
        }
        return frameTex[frameCache[idx]!]
    }

    public func render(outputIndex k: Int) -> Output {
        let tSrc = Double(k) * srcFps / outFps
        let i = Int(tSrc.rounded(.down))
        let window = [i - 1, i, i + 1, i + 2]
        // rts and pair_changed stay in UNWRAPPED indices (relative times
        // must keep their spacing); only the texture fetch wraps.
        let looping = loops && frameCount >= 4
        func wrap(_ n: Int) -> Int { ((n % frameCount) + frameCount) % frameCount }
        let nearest = looping ? wrap(Int(tSrc.rounded()))
                              : min(max(Int(tSrc.rounded()), 0), frameCount - 1)
        if !looping {
            guard window[0] >= 0, window[3] < frameCount else {
                let h = sourceTexture(nearest)
                return Output(image: h, hold: h, wasHold: true)
            }
        }
        let slotTex = window.map { sourceTexture(looping ? wrap($0) : $0) }
        let pairChanged: Int32 = window == prevWindow ? 0 : 1
        prevWindow = window
        let rts = window.map { Float(Double($0) - tSrc) }

        let cb = queue.makeCommandBuffer()!
        let enc = cb.makeComputeCommandEncoder()!
        for (pi, p) in graph.passes.enumerated() {
            let pw = passPair[p.save]![0].width, ph = passPair[p.save]![0].height
            let sampled = p.binds.filter { $0.kind != "storage" }
            let lay = Engine.layout(sampledCount: sampled.count)
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

            enc.setComputePipelineState(psos[pi])
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
            passFront[p.save] = 1 - passFront[p.save]!
        }
        enc.endEncoding()
        cb.commit(); cb.waitUntilCompleted()
        if let e = cb.error { fatalError("frame \(k): \(e)") }
        return Output(image: front("FRAME_MIX"), hold: sourceTexture(nearest), wasHold: false)
    }
}

// The synthetic scenes: rect-on-background in the ladder's style, with
// motion laws that make the field overlays worth looking at. Multi-scale
// texture keeps the coarse pyramid under Nyquist (the P2 aliasing lesson).
//
// Motion laws are in REAL pixels and REAL frames, and every scene
// traverses the FULL frame width at every size (the demo's spec,
// 2026-09-01): translate crosses from the left edge to the right wall;
// accelerate rests at the left edge, accelerates rightward under
// constant a, bounces elastically mid-loop when its right edge meets
// the right wall (the impulse in full view), and returns — the loop
// seam is the apex, where v = 0, so it closes smoothly; oscillate
// swings about the centre until both edges kiss the walls. Peak speeds
// are capped at the MEASURED envelope (PSNR vs analytic truth,
// 2026-09-01: 40+ dB through 24 px/frame at 720p, through 16 at 360p;
// 35 dB at 32) and the range is bought with loop length instead. The
// trades that implies: constant-a field brightness falls as 8E/N², and
// oscillate's peak jerk (v³/amp²) collapses at wall-to-wall amplitude
// — the jerk overlay reads near-black there, a display-scale (FS)
// matter, not the law's.
public struct SyntheticScene {
    public enum Motion {
        case translate(vx: Double)                 // constant v: accel field dark
        case accelerate(a: Double, period: Double) // bouncing fall onto the right wall
        case oscillate(amp: Double, period: Double)// sweeps accel (jerk dims with amp)
    }
    public let motion: Motion
    public let width: Int, height: Int

    public init(motion: Motion, width: Int, height: Int) {
        self.motion = motion; self.width = width; self.height = height
    }

    /// Rect left edge in REAL pixels; `t` in real (output-rate) frames.
    public func rectX(at t: Double) -> Double {
        switch motion {
        case .translate(let vx):
            return vx * t
        case .accelerate(let a, let period):
            // Constant a toward the right wall, apex (v = 0) at the seam,
            // elastic bounce at t = period/2: x = a/2 · min(t, period−t)²,
            // excursion a·period²/8.
            let tp = t.truncatingRemainder(dividingBy: period)
            let tm = min(tp, period - tp)
            return a / 2 * tm * tm
        case .oscillate(let amp, let period):
            return (Double(width) - 300) / 2 + amp * sin(2 * .pi * t / period)
        }
    }

    static func tex(_ x: Double, _ y: Double) -> Double {
        0.5 + 0.16 * sin(2 * .pi * x / 173.0) + 0.13 * sin(2 * .pi * x / 89.0 + 0.7)
            + 0.09 * sin(2 * .pi * (x + 0.6 * y) / 127.0) + 0.07 * sin(2 * .pi * y / 97.0)
            + 0.05 * sin(2 * .pi * x / 47.0 + 2.1)
    }

    /// `x`,`y` in real pixels, `t` in real (output-rate source) frames.
    /// The mover keeps its 300 px at every size; only trajectories grow.
    public func value(_ x: Double, _ y: Double, t: Double) -> Double {
        let rx = rectX(at: t), ry = Double(height) / 2 - 150
        if x >= rx && x < rx + 300 && y >= ry && y < ry + 300 {
            // the mover carries its own texture (rides the body frame)
            return min(max(Self.tex(x - rx, y - ry) * 0.9 + 0.05, 0), 1)
        }
        // static background, dimmer so the mover reads at a glance
        return min(max(Self.tex(x, y) * 0.35 + 0.1, 0), 1)
    }

    public func fill(_ tex: MTLTexture, frame idx: Int) {
        let tf = Double(idx)   // motion laws are in frames for readability
        let W = tex.width, H = tex.height
        var row = [UInt16](repeating: 0, count: W * 4)
        for y in 0..<H {
            for x in 0..<W {
                let v = UInt16((value(Double(x) + 0.5, Double(y) + 0.5, t: tf) * 65535).rounded())
                row[x * 4] = v; row[x * 4 + 1] = v; row[x * 4 + 2] = v; row[x * 4 + 3] = 65535
            }
            row.withUnsafeBytes {
                tex.replace(region: MTLRegionMake2D(0, y, W, 1), mipmapLevel: 0,
                            withBytes: $0.baseAddress!, bytesPerRow: W * 8)
            }
        }
    }
}
