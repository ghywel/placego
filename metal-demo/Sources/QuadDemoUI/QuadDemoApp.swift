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
    case accel = "Acceleration field"
    case jerk = "Jerk field"
    var id: String { rawValue }
    var dir: String {
        switch self {
        case .production: return "generated"
        case .accel: return "generated-accel"
        case .jerk: return "generated-jerk"
        }
    }
}

enum SceneKind: String, CaseIterable, Identifiable {
    case translate = "Translate (constant v)"
    case accelerate = "Accelerate (constant a)"
    case oscillate = "Oscillate (accel + jerk)"
    var id: String { rawValue }
    var motion: SyntheticScene.Motion {
        switch self {
        // Laws chosen from the ladder's own envelopes: velocity inside the
        // ~23 px search reach, accel readable at FS=4, jerk at FS=8.
        case .translate: return .translate(vx: 6)
        case .accelerate: return .accelerate(a: 1.333, v0: -16)
        case .oscillate: return .oscillate(amp: 20, period: 9.6)
        }
    }
    var frameCount: Int {
        switch self {
        case .translate: return 96
        case .accelerate: return 24
        case .oscillate: return 96
        }
    }
}

enum ViewMode: String, CaseIterable, Identifiable {
    case interpolated = "Interpolated"
    case hold = "Hold (24p)"
    case wipe = "A/B wipe"
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
            rebuild()
        }
    }
    @Published var status: String? = nil
    @Published var sizePreset: SizePreset = .p360 { didSet { rebuild() } }
    @Published var viewMode: ViewMode = .interpolated
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

    func rebuild() {
        compiling = true
        lastOut = nil
        let gen = buildGeneration + 1
        buildGeneration = gen
        let (w, h) = sizePreset.wh
        let kind = graphKind, scene = sceneKind, dev = device
        let vurl = videoURL
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
                    e = try Engine(graphDir: self.graphURL(kind),
                                   width: w, height: h,
                                   srcFps: 24, outFps: 60,
                                   frameCount: scene.frameCount, device: dev)
                    let synth = SyntheticScene(motion: scene.motion, width: w, height: h)
                    e.fillFrame = { tex, idx in synth.fill(tex, frame: idx) }
                }
                DispatchQueue.main.async {
                    guard self.buildGeneration == gen else { return }
                    self.engine = e
                    self.videoSource = vsrc
                    self.frameIndex = 0
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

    /// Advance one output frame (called from the view's draw tick).
    func step() {
        guard let e = engine, !compiling else { return }
        let t0 = DispatchTime.now()
        if frameIndex >= e.outCount {
            frameIndex = 0; e.reset(); videoSource?.reset()
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
struct MetalPresentView: NSViewRepresentable {
    @ObservedObject var controller: RenderController

    func makeCoordinator() -> Coordinator { Coordinator(controller) }
    func makeNSView(context: Context) -> MTKView {
        let v = MTKView(frame: .zero, device: controller.device)
        v.framebufferOnly = false            // the present kernel writes it
        v.colorPixelFormat = .bgra8Unorm
        v.preferredFramesPerSecond = 60
        v.delegate = context.coordinator
        return v
    }
    func updateNSView(_ view: MTKView, context: Context) {}

    final class Coordinator: NSObject, MTKViewDelegate {
        let c: RenderController
        let queue: MTLCommandQueue
        let pso: MTLComputePipelineState
        let sampler: MTLSamplerState

        // The present kernel: wipe compositing + scaling. Host-side MSL,
        // not part of the shader template (it is chrome, not method).
        static let msl = """
        #include <metal_stdlib>
        using namespace metal;
        kernel void present(texture2d<float, access::sample> holdT [[texture(0)]],
                            texture2d<float, access::sample> outT  [[texture(1)]],
                            texture2d<float, access::write> dst    [[texture(2)]],
                            sampler smp [[sampler(0)]],
                            constant float2 &p [[buffer(0)]],
                            uint2 gid [[thread_position_in_grid]]) {
            if (gid.x >= dst.get_width() || gid.y >= dst.get_height()) return;
            float2 uv = (float2(gid) + 0.5) /
                        float2(dst.get_width(), dst.get_height());
            float4 c;
            int mode = int(p.y);
            if (mode == 1) c = holdT.sample(smp, uv);
            else if (mode == 2) {
                c = uv.x < p.x ? holdT.sample(smp, uv) : outT.sample(smp, uv);
                if (fabs(uv.x - p.x) * float(dst.get_width()) < 1.5)
                    c = float4(1.0, 1.0, 1.0, 1.0);
            } else c = outT.sample(smp, uv);
            dst.write(float4(c.rgb, 1.0), gid);
        }
        """

        init(_ c: RenderController) {
            self.c = c
            queue = c.device.makeCommandQueue()!
            let lib = try! c.device.makeLibrary(source: Self.msl, options: nil)
            pso = try! c.device.makeComputePipelineState(function: lib.makeFunction(name: "present")!)
            let sd = MTLSamplerDescriptor()
            sd.minFilter = .linear; sd.magFilter = .linear
            sd.sAddressMode = .clampToEdge; sd.tAddressMode = .clampToEdge
            sd.normalizedCoordinates = true
            sampler = c.device.makeSamplerState(descriptor: sd)!
        }

        func mtkView(_ view: MTKView, drawableSizeWillChange size: CGSize) {}

        func draw(in view: MTKView) {
            if c.playing { c.step() }
            guard let out = c.lastOut,
                  let drawable = view.currentDrawable else { return }
            let mode: Float
            switch c.viewMode {
            case .interpolated: mode = 0
            case .hold: mode = 1
            case .wipe: mode = 2
            }
            var p: [Float] = [Float(c.wipePos), mode]
            let cb = queue.makeCommandBuffer()!
            let enc = cb.makeComputeCommandEncoder()!
            enc.setComputePipelineState(pso)
            enc.setTexture(out.hold, index: 0)
            enc.setTexture(out.image, index: 1)
            enc.setTexture(drawable.texture, index: 2)
            enc.setSamplerState(sampler, index: 0)
            enc.setBytes(&p, length: 8, index: 0)
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
                Picker("Scene", selection: $controller.sceneKind) {
                    ForEach(SceneKind.allCases) { Text($0.rawValue).tag($0) }
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
                if controller.viewMode == .wipe {
                    Slider(value: $controller.wipePos, in: 0...1) {
                        Text("Wipe")
                    }.frame(maxWidth: 220)
                }
                Spacer()
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
