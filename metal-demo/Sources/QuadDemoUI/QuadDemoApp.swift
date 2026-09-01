// QuadDemoUI — P4 of METALPORT.md: the demonstration the shader template
// deserves. SwiftUI chrome around QuadEngine: synthetic scenes with known
// motion laws, live 24->60 interpolation, an A/B wipe against zero-order
// hold, and the field overlays -- acceleration and jerk read out of the
// same passes -- because the field is the product, and the demo should
// show the measurement, not just smooth pixels.
//
//   swift run -c release QuadDemoUI     (run ./gen.sh first)
import SwiftUI
import MetalKit
import UniformTypeIdentifiers
import QuadEngine

// ------------------------------------------------------------ controller
enum GraphKind: String, CaseIterable, Identifiable {
    case production = "Picture"
    case velocity = "Velocity field"
    case accel = "Acceleration field"
    case jerk = "Jerk field"
    var id: String { rawValue }
    var dir: String {
        switch self {
        case .production: return "generated"
        case .velocity: return "generated-vel"
        case .accel: return "generated-accel"
        case .jerk: return "generated-jerk"
        }
    }
    // The diag encoding's full scale, px per interval^n (gen.sh bakes it).
    var fieldFS: Float {
        switch self {
        case .production: return 0
        case .velocity: return 32
        case .accel: return 4
        case .jerk: return 8
        }
    }
    // Reading-style gates in px: (vis lo, vis hi, full saturation).
    // Accel/jerk sit just above the pooled peak-locking floor (bg p95
    // 0.10); velocity's signal is 30x larger, and the higher floor also
    // trims the pooling halo to a crisp edge and lets the oscillate
    // square fade honestly at its turnarounds.
    var readingGates: (Float, Float, Float) {
        self == .velocity ? (1.0, 2.0, 3.0) : (0.12, 0.22, 0.30)
    }
}

enum SceneKind: String, CaseIterable, Identifiable {
    case translate = "Translate (constant v)"
    case accelerate = "Accelerate (constant a)"
    case oscillate = "Oscillate (accel + jerk)"
    var id: String { rawValue }
    // Every scene traverses the full frame width (see SyntheticScene's
    // header for the spec and the measured speed envelope). The laws
    // derive from the frame geometry: travel = W − 300, oscillation
    // amplitude = W/2 − 150 (edges kiss the walls); loop lengths are
    // chosen so peak speed stays inside the envelope (~14-15 px/frame
    // at 360p, ~21-23 at 720p, both PSNR-verified).
    func motion(scale s: Int) -> SyntheticScene.Motion {
        let W = Double(640 * s)
        let n = Double(frameCount(scale: s))
        switch self {
        case .translate: return .translate(vx: (W - 300) / n)
        case .accelerate: return .accelerate(a: 8 * (W - 300) / (n * n), period: n)
        case .oscillate: return .oscillate(amp: W / 2 - 150,
                                           period: n / Double(s == 1 ? 2 : 1))
        }
    }
    func frameCount(scale s: Int) -> Int {
        switch self {
        case .translate: return 48 * s     // v: 7.1 / 10.2 px per frame
        case .accelerate: return s == 1 ? 96 : 168   // peak v: 14.2 / 23.3
        case .oscillate: return 144        // peak v: 14.8 / 21.4
        }
    }
    // Whether the motion law closes the loop exactly, so the engine may
    // wrap its window across the restart. Accelerate is built to: with
    // a = -2*v0/N, x(N) = x(0) and v(N) = -v(0) — the restart IS the
    // right-wall bounce. Oscillate spans ten whole periods. Translate
    // exits the frame and jump-cuts, so its seam stays a hold.
    var seamless: Bool { self != .translate }
}

enum ViewMode: String, CaseIterable, Identifiable {
    case interpolated = "Interpolated"
    case hold = "Hold (24p)"
    case wipe = "A/B wipe"
    var id: String { rawValue }
}

// How a field overlay is presented. Raw is the instrument's own signed
// per-channel encoding, noise floor and all; Reading decodes it into the
// optical-flow colour convention (hue = direction, brightness = signal
// above the measured noise floor, pooled over ±16 px) composited on the
// dimmed picture — the "solid colour where something coherent happens"
// view. Both read the same graph; the toggle is display-only.
enum FieldStyle: String, CaseIterable, Identifiable {
    case reading = "Reading"
    case raw = "Raw"
    var id: String { rawValue }
}

enum SizePreset: String, CaseIterable, Identifiable {
    case p360 = "640×360"
    case p720 = "1280×720"
    var id: String { rawValue }
    var wh: (Int, Int) { self == .p360 ? (640, 360) : (1280, 720) }
}

final class RenderController: ObservableObject {
    @Published var sceneKind: SceneKind = .oscillate {
        didSet { videoURL = nil; rebuild() }
    }
    @Published var videoURL: URL? = nil
    var videoSource: VideoSource?
    @Published var graphKind: GraphKind = .production {
        didSet {
            // Hold shows the untouched source; a field overlay changes the
            // ENGINE output — flip the view so the choice is visible.
            if graphKind != .production && viewMode == .hold {
                viewMode = .interpolated
            }
            // Same scene, same timeline — a Show switch stays on the
            // frame the viewer is looking at.
            rebuild(keepPosition: true)
        }
    }
    @Published var status: String? = nil
    @Published var sizePreset: SizePreset = .p360 { didSet { rebuild() } }
    @Published var viewMode: ViewMode = .interpolated
    @Published var fieldStyle: FieldStyle = .reading
    // Field overlay opacity: 1 = the field replaces the content,
    // 0 = content only. Presentation-side, so it costs no rebuild.
    @Published var fieldOpacity = 1.0
    @Published var wipePos: Double = 0.5
    @Published var playing = true
    @Published var compiling = true
    @Published var achievedFps: Double = 0
    @Published var frameIndex = 0

    let device = MTLCreateSystemDefaultDevice()!
    var engine: Engine?
    var lastOut: Engine.Output?
    private var fpsEMA = 0.0
    private let buildQueue = DispatchQueue(label: "engine-build")
    private var buildGeneration = 0

    init() { rebuild() }

    private func graphURL(_ kind: GraphKind) -> URL {
        // Resolution order: package directory (swift run), then the .app
        // bundle's Resources (make-app.sh copies the graphs there), then
        // beside whatever contains the executable.
        let cwd = URL(fileURLWithPath: kind.dir)
        if FileManager.default.fileExists(atPath: cwd.path) { return cwd }
        if let res = Bundle.main.resourceURL?.appendingPathComponent(kind.dir),
           FileManager.default.fileExists(atPath: res.path) { return res }
        return Bundle.main.bundleURL.deletingLastPathComponent()
            .appendingPathComponent(kind.dir)
    }

    func rebuild(keepPosition: Bool = false) {
        compiling = true
        lastOut = nil
        let gen = buildGeneration + 1
        buildGeneration = gen
        let (w, h) = sizePreset.wh
        let kind = graphKind, scene = sceneKind, dev = device
        let vurl = videoURL
        let paused = !playing
        let shown = max(frameIndex - 1, 0)   // the frame currently on screen
        buildQueue.async { [weak self] in
            guard let self else { return }
            do {
                let e: Engine
                var vsrc: VideoSource? = nil
                var vfail: String? = nil
                var vopen: VideoSource? = nil
                if let u = vurl {
                    vopen = VideoSource(url: u, device: dev)
                    if vopen == nil {
                        vfail = "\(u.lastPathComponent): \(VideoSource.lastFailure ?? "unknown failure")"
                    }
                }
                if let v = vopen {
                    // Zero-copy: decoded CVPixelBuffers become engine
                    // sources via CVMetalTextureCache -- unified memory's
                    // party trick, and the path ffmpeg structurally lacks.
                    vsrc = v
                    e = try Engine(graphDir: self.graphURL(kind),
                                   width: v.width, height: v.height,
                                   srcFps: v.fps, outFps: 60,
                                   frameCount: v.frameCount, device: dev)
                    e.provideFrame = { v.texture(for: $0) }
                } else {
                    let s = max(1, h / 360)   // size factor vs the baseline
                    e = try Engine(graphDir: self.graphURL(kind),
                                   width: w, height: h,
                                   srcFps: 24, outFps: 60,
                                   frameCount: scene.frameCount(scale: s), device: dev)
                    e.loops = scene.seamless
                    let synth = SyntheticScene(motion: scene.motion(scale: s),
                                               width: w, height: h)
                    e.fillFrame = { tex, idx in synth.fill(tex, frame: idx) }
                }
                let target = min(keepPosition ? shown : 0, e.outCount - 1)
                // A kept mid-video position with a FRESH VideoSource must
                // seek, not decode forward from zero — the first render
                // otherwise pays the whole preroll on the main thread
                // (the reported beachball: mid-file + Show switch).
                if let v = vsrc, target > 0 {
                    let tSrc = Double(target) * e.srcFps / e.outFps
                    v.seek(toFrame: max(Int(tSrc.rounded(.down)) - 1, 0))
                }
                // A paused view has no step() tick to pull a frame through
                // the new engine — it would keep showing the old graph's
                // image forever. Render the target frame here, off-main,
                // before publishing.
                let preOut = paused ? e.render(outputIndex: target) : nil
                DispatchQueue.main.async {
                    guard self.buildGeneration == gen else { return }
                    self.engine = e
                    self.videoSource = vsrc
                    if let po = preOut {
                        self.lastOut = po
                        self.frameIndex = target + 1   // Step advances from here
                    } else {
                        self.frameIndex = target
                    }
                    self.compiling = false
                    self.status = vfail
                    if vfail != nil { self.videoURL = nil }   // honest fallback
                }
            } catch {
                DispatchQueue.main.async {
                    self.compiling = false
                    NSLog("engine build failed: \(error)")
                }
            }
        }
    }

    /// Playback position 0..1 of the frame on screen (video scrubber).
    /// While a scrub is pending, the knob follows the finger.
    var progress: Double {
        if let p = pendingSeek { return p }
        guard let e = engine, e.outCount > 1 else { return 0 }
        return Double(min(max(frameIndex - 1, 0), e.outCount - 1)) / Double(e.outCount - 1)
    }

    /// True while the user holds the scrubber; playback freezes and the
    /// draw tick shows sought frames instead of advancing.
    @Published var scrubbing = false
    private var pendingSeek: Double? = nil

    /// Event-path half of scrubbing: record the wanted position and
    /// return. The Slider fires this per drag event — doing reader
    /// rebuilds and full-window renders here serially beachballs the
    /// main thread (it did).
    func requestSeek(_ pos: Double) {
        guard videoSource != nil else { return }
        pendingSeek = pos
    }

    /// Draw-tick half: perform at most ONE coalesced seek per frame —
    /// the sequential reader is rebuilt at the target's window start (a
    /// timeRange seek, not a decode from zero), the engine's window
    /// state resets (its cache contract expects that after any seek),
    /// and the target frame renders immediately as the scrub preview.
    func serviceSeek() {
        guard let pos = pendingSeek else { return }
        guard let e = engine, let v = videoSource, !compiling else {
            if videoSource == nil { pendingSeek = nil }
            return
        }
        pendingSeek = nil
        let target = min(max(Int(pos * Double(e.outCount - 1)), 0), e.outCount - 1)
        guard target != max(frameIndex - 1, 0) else { return }
        let tSrc = Double(target) * e.srcFps / e.outFps
        v.seek(toFrame: max(Int(tSrc.rounded(.down)) - 1, 0))
        e.reset()
        lastOut = e.render(outputIndex: target)
        frameIndex = target + 1
    }

    /// Advance one output frame (called from the view's draw tick).
    func step() {
        guard let e = engine, !compiling else { return }
        let t0 = DispatchTime.now()
        if frameIndex >= e.outCount {
            frameIndex = 0
            // A wrapping engine slides its window straight across the
            // seam — resetting would only throw away warm caches.
            if !e.loops { e.reset(); videoSource?.reset() }
        }
        lastOut = e.render(outputIndex: frameIndex)
        frameIndex += 1
        let dt = Double(DispatchTime.now().uptimeNanoseconds - t0.uptimeNanoseconds) / 1e9
        // EMA over TIME, inverted -- never over instantaneous rates. Frame
        // costs alternate hugely here (window-advance frames rebuild the
        // flow caches; in-between frames are served from them), and a mean
        // of rates lets the cheap cache-hit frames shout over the real
        // throughput: measured 75 "fps" shown against ~5 delivered.
        fpsEMA = fpsEMA == 0 ? dt : fpsEMA * 0.9 + dt * 0.1
        achievedFps = 1.0 / fpsEMA
    }
}

// ------------------------------------------------------------ metal view

/// The wipe's division bar IS the slider: in wipe mode a click lands the
/// bar at the cursor and a drag carries it, with a resize cursor over the
/// bar itself — no separate control. The view fills its 16:9 fit exactly,
/// so x/width maps straight to the wipe uv.
final class WipeDragView: MTKView {
    weak var controller: RenderController?
    private var lastBarX: CGFloat = -1

    private func setWipe(with event: NSEvent) {
        guard let c = controller, c.viewMode == .wipe else { return }
        let x = convert(event.locationInWindow, from: nil).x
        c.wipePos = min(max(Double(x / max(bounds.width, 1)), 0), 1)
    }
    override func mouseDown(with event: NSEvent) { setWipe(with: event) }
    override func mouseDragged(with event: NSEvent) { setWipe(with: event) }

    override func resetCursorRects() {
        guard let c = controller, c.viewMode == .wipe else { return }
        let x = CGFloat(c.wipePos) * bounds.width
        addCursorRect(NSRect(x: x - 12, y: 0, width: 24, height: bounds.height)
                          .intersection(bounds), cursor: .resizeLeftRight)
    }
    /// Draw-tick hook: keep the cursor band glued to the moving bar.
    func refreshCursor() {
        let x = controller?.viewMode == .wipe
            ? CGFloat(controller!.wipePos) * bounds.width : -1
        if x != lastBarX { lastBarX = x; window?.invalidateCursorRects(for: self) }
    }
}

struct MetalPresentView: NSViewRepresentable {
    @ObservedObject var controller: RenderController

    func makeCoordinator() -> Coordinator { Coordinator(controller) }
    func makeNSView(context: Context) -> MTKView {
        let v = WipeDragView(frame: .zero, device: controller.device)
        v.framebufferOnly = false            // the present kernel writes it
        v.colorPixelFormat = .bgra8Unorm
        v.preferredFramesPerSecond = 60
        v.delegate = context.coordinator
        v.controller = controller
        return v
    }
    func updateNSView(_ view: MTKView, context: Context) {}

    final class Coordinator: NSObject, MTKViewDelegate {
        let c: RenderController
        let queue: MTLCommandQueue
        let pso: MTLComputePipelineState
        let poolPso: MTLComputePipelineState
        let sampler: MTLSamplerState
        // Reading-style accumulator (pooled+EMA'd field, px units),
        // ping-ponged; reseeded whenever the style was off or size changed.
        var accum: [MTLTexture] = []
        var accumFront = 0
        var accumFresh = true

        // Host-side MSL: the present kernel (wipe compositing + scaling)
        // and the field "Reading" style. Chrome, not method.
        //
        // Reading style, two passes, constants all MEASURED 2026-09-01:
        // poolacc decodes the diag encoding (rg = 0.5 + field_px*0.5/FS)
        // to px, pools 13x13 taps at 8 px spacing (+/-48 px — spanning
        // the texture wavelengths the peak-locking floor is structured
        // at: static bg p95 falls 0.52 -> 0.10 px) and EMAs across
        // frames (the mover's noise re-rolls every window advance while
        // true field persists: mid-flight coherence 0.74 -> 0.92).
        // present then paints hue = direction, visibility/saturation =
        // magnitude above the pooled floor (gate 0.12->0.22, full colour
        // by 0.30) over the dimmed grayscale picture.
        static let msl = """
        #include <metal_stdlib>
        using namespace metal;
        static float3 hsv2rgb(float h, float s, float v) {
            float3 k = fmod(float3(5.0, 3.0, 1.0) + h * 6.0, 6.0);
            return v - v * s * clamp(min(k, 4.0 - k), 0.0, 1.0);
        }
        kernel void poolacc(texture2d<float, access::sample> outT   [[texture(0)]],
                            texture2d<float, access::sample> accumIn [[texture(1)]],
                            texture2d<float, access::write> accumOut [[texture(2)]],
                            sampler smp [[sampler(0)]],
                            constant float2 &q [[buffer(0)]],   // (alpha, FS)
                            uint2 gid [[thread_position_in_grid]]) {
            if (gid.x >= accumOut.get_width() || gid.y >= accumOut.get_height()) return;
            float2 ts = float2(outT.get_width(), outT.get_height());
            float2 uv = (float2(gid) + 0.5) / ts;
            float2 fpx = float2(0.0);
            for (int j = -6; j <= 6; j++)
                for (int i = -6; i <= 6; i++)
                    fpx += (outT.sample(smp, uv + float2(i, j) * 8.0 / ts).rg - 0.5) * 2.0 * q.y;
            fpx /= 169.0;
            // the 24 px diag marker corner plus the pooling reach is not field
            if (gid.x < 74 && gid.y < 74) fpx = float2(0.0);
            float2 prev = accumIn.sample(smp, uv).rg;
            accumOut.write(float4(mix(prev, fpx, q.x), 0.0, 1.0), gid);
        }
        static float4 reading(texture2d<float, access::sample> accumT,
                              texture2d<float, access::sample> holdT,
                              sampler smp, float2 uv, float3 gate) {
            float2 ts = float2(accumT.get_width(), accumT.get_height());
            // 4-tap soften: the pooled field keeps a faint per-pixel
            // checker from the raw diag output that dithers the gate.
            float2 fpx = float2(0.0);
            fpx += accumT.sample(smp, uv + float2( 2.0,  2.0) / ts).rg;
            fpx += accumT.sample(smp, uv + float2(-2.0,  2.0) / ts).rg;
            fpx += accumT.sample(smp, uv + float2( 2.0, -2.0) / ts).rg;
            fpx += accumT.sample(smp, uv + float2(-2.0, -2.0) / ts).rg;
            fpx *= 0.25;
            float mag = length(fpx);
            float vis = smoothstep(gate.x, gate.y, mag) * 0.9;
            // borders: the pool clamps onto frame-edge flow garbage
            float2 bpx = min(uv, 1.0 - uv) * ts;
            vis *= smoothstep(4.0, 28.0, min(bpx.x, bpx.y));
            float sat = 0.95 * smoothstep(gate.x, gate.z, mag);
            float hue = fract(atan2(fpx.y, fpx.x) / (2.0 * M_PI_F) + 1.0);
            float lum = dot(holdT.sample(smp, uv).rgb, float3(0.299, 0.587, 0.114));
            return float4(mix(float3(lum * 0.35), hsv2rgb(hue, sat, 1.0), vis), 1.0);
        }
        // p[0] = (wipePos, viewMode, style, FS) with style 0 = production
        // passthrough, 1 = Reading, 2 = Raw field; p[1] = (visLo, visHi,
        // satFull, overlayOpacity). Any field style blends over the
        // source picture by the opacity — 1 replaces the content, 0 is
        // content only — and the wipe's B-side inherits it.
        kernel void present(texture2d<float, access::sample> holdT [[texture(0)]],
                            texture2d<float, access::sample> outT  [[texture(1)]],
                            texture2d<float, access::write> dst    [[texture(2)]],
                            texture2d<float, access::sample> accumT [[texture(3)]],
                            sampler smp [[sampler(0)]],
                            constant float4 *p [[buffer(0)]],
                            uint2 gid [[thread_position_in_grid]]) {
            if (gid.x >= dst.get_width() || gid.y >= dst.get_height()) return;
            float2 uv = (float2(gid) + 0.5) /
                        float2(dst.get_width(), dst.get_height());
            int style = int(p[0].z);
            float4 outC = style == 1 ? reading(accumT, holdT, smp, uv, p[1].xyz)
                                     : outT.sample(smp, uv);
            if (style != 0)
                outC = float4(mix(holdT.sample(smp, uv).rgb, outC.rgb, p[1].w), 1.0);
            float4 c;
            int mode = int(p[0].y);
            if (mode == 1) c = holdT.sample(smp, uv);
            else if (mode == 2) {
                c = uv.x < p[0].x ? holdT.sample(smp, uv) : outC;
                if (fabs(uv.x - p[0].x) * float(dst.get_width()) < 1.5)
                    c = float4(1.0, 1.0, 1.0, 1.0);
            } else c = outC;
            dst.write(float4(c.rgb, 1.0), gid);
        }
        """

        init(_ c: RenderController) {
            self.c = c
            queue = c.device.makeCommandQueue()!
            let lib = try! c.device.makeLibrary(source: Self.msl, options: nil)
            pso = try! c.device.makeComputePipelineState(function: lib.makeFunction(name: "present")!)
            poolPso = try! c.device.makeComputePipelineState(function: lib.makeFunction(name: "poolacc")!)
            let sd = MTLSamplerDescriptor()
            sd.minFilter = .linear; sd.magFilter = .linear
            sd.sAddressMode = .clampToEdge; sd.tAddressMode = .clampToEdge
            sd.normalizedCoordinates = true
            sampler = c.device.makeSamplerState(descriptor: sd)!
        }

        func mtkView(_ view: MTKView, drawableSizeWillChange size: CGSize) {}

        func draw(in view: MTKView) {
            (view as? WipeDragView)?.refreshCursor()
            c.serviceSeek()
            if c.playing && !c.scrubbing { c.step() }
            guard let out = c.lastOut,
                  let drawable = view.currentDrawable else { return }
            let mode: Float
            switch c.viewMode {
            case .interpolated: mode = 0
            case .hold: mode = 1
            case .wipe: mode = 2
            }
            // Hold-fallback frames carry the raw picture, not a field
            // encoding — never decode them as one.
            let fieldOn = c.graphKind != .production && !out.wasHold
            let readingOn = fieldOn && c.fieldStyle == .reading
            let fs = c.graphKind.fieldFS
            let cb = queue.makeCommandBuffer()!
            if readingOn {
                let (fw, fh) = (out.image.width, out.image.height)
                if accum.first?.width != fw || accum.first?.height != fh {
                    let d = MTLTextureDescriptor.texture2DDescriptor(
                        pixelFormat: .rg16Float, width: fw, height: fh, mipmapped: false)
                    d.usage = [.shaderRead, .shaderWrite]; d.storageMode = .private
                    accum = [c.device.makeTexture(descriptor: d)!,
                             c.device.makeTexture(descriptor: d)!]
                    accumFresh = true
                }
                var q: [Float] = [accumFresh ? 1 : 0.12, fs]
                accumFresh = false
                let pe = cb.makeComputeCommandEncoder()!
                pe.setComputePipelineState(poolPso)
                pe.setTexture(out.image, index: 0)
                pe.setTexture(accum[accumFront], index: 1)
                pe.setTexture(accum[1 - accumFront], index: 2)
                pe.setSamplerState(sampler, index: 0)
                pe.setBytes(&q, length: 8, index: 0)
                pe.dispatchThreads(MTLSize(width: fw, height: fh, depth: 1),
                                   threadsPerThreadgroup: MTLSize(width: 16, height: 16, depth: 1))
                pe.endEncoding()
                accumFront = 1 - accumFront
            } else {
                accumFresh = true
            }
            let g = c.graphKind.readingGates
            let style: Float = !fieldOn ? 0 : (readingOn ? 1 : 2)
            var p: [Float] = [Float(c.wipePos), mode, style, fs,
                              g.0, g.1, g.2, Float(c.fieldOpacity)]
            let enc = cb.makeComputeCommandEncoder()!
            enc.setComputePipelineState(pso)
            enc.setTexture(out.hold, index: 0)
            enc.setTexture(out.image, index: 1)
            enc.setTexture(drawable.texture, index: 2)
            enc.setTexture(accum.isEmpty ? out.image : accum[accumFront], index: 3)
            enc.setSamplerState(sampler, index: 0)
            enc.setBytes(&p, length: 32, index: 0)
            enc.dispatchThreads(MTLSize(width: drawable.texture.width,
                                        height: drawable.texture.height, depth: 1),
                                threadsPerThreadgroup: MTLSize(width: 16, height: 16, depth: 1))
            enc.endEncoding()
            cb.present(drawable)
            cb.commit()
        }
    }
}

// -------------------------------------------------------------- the view

// Scene picker selection: the synthetic scenes, or the open video. The
// video entry only exists while one is open; picking any scene closes it.
private enum SceneSel: Hashable {
    case video
    case scene(SceneKind)
}

struct ContentView: View {
    @StateObject var controller = RenderController()

    var body: some View {
        VStack(spacing: 0) {
            ZStack {
                MetalPresentView(controller: controller)
                    .aspectRatio(16.0 / 9.0, contentMode: .fit)
                if controller.compiling {
                    VStack(spacing: 8) {
                        ProgressView()
                        Text("Compiling 68 passes…").font(.caption)
                    }
                    .padding(20)
                    .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 12))
                }
                VStack {
                    HStack {
                        hud
                        Spacer()
                    }
                    Spacer()
                }.padding(10)
            }
            controls
        }
        .onAppear {
            NSApp.setActivationPolicy(.regular)
            NSApp.activate(ignoringOtherApps: true)
        }
        .frame(minWidth: 900, minHeight: 620)
    }

    var hud: some View {
        VStack(alignment: .leading, spacing: 2) {
            Text("\(controller.device.name) — \(controller.engine?.graph.passes.count ?? 0) passes native Metal")
            if let u = controller.videoURL {
                Text("\(u.lastPathComponent) \(controller.engine?.width ?? 0)×\(controller.engine?.height ?? 0) (zero-copy decode)")
            }
            Text(String(format: "%.1f fps render (target 60)", controller.achievedFps))
            Text("frame \(controller.frameIndex)")
            if let s = controller.status {
                Text(s).foregroundStyle(.orange)
                    .frame(maxWidth: 560, alignment: .leading)
            }
        }
        .font(.system(size: 11, design: .monospaced))
        .padding(8)
        .background(.black.opacity(0.55), in: RoundedRectangle(cornerRadius: 8))
        .foregroundStyle(.green)
    }

    var controls: some View {
        VStack(spacing: 10) {
            HStack(spacing: 16) {
                Picker("Scene", selection: Binding<SceneSel>(
                    get: {
                        controller.videoURL != nil ? .video : .scene(controller.sceneKind)
                    },
                    set: { sel in
                        // didSet on sceneKind fires even for the same value,
                        // clearing the video and rebuilding.
                        if case .scene(let s) = sel { controller.sceneKind = s }
                    })) {
                    if controller.videoURL != nil {
                        Text("Video").tag(SceneSel.video)
                    }
                    ForEach(SceneKind.allCases) { Text($0.rawValue).tag(SceneSel.scene($0)) }
                }.frame(maxWidth: 300)
                Picker("Show", selection: $controller.graphKind) {
                    ForEach(GraphKind.allCases) { Text($0.rawValue).tag($0) }
                }.frame(maxWidth: 320)
                Picker("Size", selection: $controller.sizePreset) {
                    ForEach(SizePreset.allCases) { Text($0.rawValue).tag($0) }
                }.frame(maxWidth: 220)
                 .disabled(controller.videoURL != nil)
                Button("Open Video…") {
                    let p = NSOpenPanel()
                    p.allowedContentTypes = [.movie, .mpeg4Movie, .quickTimeMovie]
                    if p.runModal() == .OK, let u = p.url {
                        controller.videoURL = u
                        controller.rebuild()
                    }
                }
            }
            HStack(spacing: 16) {
                Button(controller.playing ? "Pause" : "Play") {
                    controller.playing.toggle()
                }.keyboardShortcut(.space, modifiers: [])
                Button("Step") {
                    controller.playing = false
                    controller.step()
                }
                Picker("View", selection: $controller.viewMode) {
                    ForEach(ViewMode.allCases) { Text($0.rawValue).tag($0) }
                }.pickerStyle(.segmented).frame(maxWidth: 340)
                if controller.graphKind != .production {
                    Picker("Field", selection: $controller.fieldStyle) {
                        ForEach(FieldStyle.allCases) { Text($0.rawValue).tag($0) }
                    }.pickerStyle(.segmented).frame(maxWidth: 180)
                    Slider(value: $controller.fieldOpacity, in: 0...1) {
                        Text("Overlay")
                    }
                    .frame(maxWidth: 150)
                    .help("Field overlay opacity: right replaces the content, left shows content only")
                    if controller.fieldStyle == .reading {
                        Text("hue = direction · brightness = strength")
                            .font(.caption).foregroundStyle(.secondary)
                    }
                }
                if controller.viewMode == .wipe {
                    Text("drag the bar in the picture")
                        .font(.caption).foregroundStyle(.secondary)
                }
                Spacer()
            }
            if controller.videoURL != nil {
                // The video timeline: left is the start, right is the end.
                // The binding only RECORDS the wanted position; the draw
                // tick services one coalesced seek per frame.
                Slider(value: Binding(
                    get: { controller.progress },
                    set: { controller.requestSeek($0) }
                ), in: 0...1, onEditingChanged: { controller.scrubbing = $0 })
            }
        }
        .padding(12)
    }
}

@main
struct QuadDemoApp: App {
    var body: some SwiftUI.Scene {
        WindowGroup("Quaddirectional — native Metal") {
            ContentView()
        }
    }
}
