// CLI host for QuadEngine — the P2/P3 acceptance surface.
//
//   QuadDemo [--frames N] [--src-fps F] [--out-fps F] [--size WxH]
//            [--input raw.rgb48le] [--export out.rgb48le] [--graph dir]
//
// Behaviour is the verified P3 set; the engine itself lives in
// Sources/QuadEngine (shared with the demo UI). The synthetic full-field
// scene here is deliberately unchanged from P2 so the first-light PSNR
// numbers stay comparable across refactors.
import Metal
import Foundation
import QuadEngine

var frames = 24, srcFps = 24.0, outFps = 60.0, W = 1280, H = 720
var inputPath: String? = nil, exportPath: String? = nil, graphDir: String? = nil
var videoPath: String? = nil, bench = false
var args = Array(CommandLine.arguments.dropFirst())
while !args.isEmpty {
    let a = args.removeFirst()
    switch a {
    case "--frames":  frames = Int(args.removeFirst())!
    case "--src-fps": srcFps = Double(args.removeFirst())!
    case "--out-fps": outFps = Double(args.removeFirst())!
    case "--input":   inputPath = args.removeFirst()
    case "--export":  exportPath = args.removeFirst()
    case "--graph":   graphDir = args.removeFirst()
    case "--video":   videoPath = args.removeFirst()  // zero-copy AVFoundation source
    case "--bench":   bench = true                    // render-only, report fps
    case "--size":
        let p = args.removeFirst().split(separator: "x")
        W = Int(p[0])!; H = Int(p[1])!
    default: fatalError("unknown arg \(a)")
    }
}
var inputData: Data? = nil
if let ip = inputPath {
    inputData = try Data(contentsOf: URL(fileURLWithPath: ip))
    frames = inputData!.count / (W * H * 6)
}

let here = URL(fileURLWithPath: CommandLine.arguments[0]).deletingLastPathComponent()
var genDir = URL(fileURLWithPath: graphDir ?? "generated")
if graphDir == nil && !FileManager.default.fileExists(atPath: genDir.path) {
    genDir = here.deletingLastPathComponent().deletingLastPathComponent()
        .deletingLastPathComponent().appendingPathComponent("generated")
}

let dumpMode = ProcessInfo.processInfo.environment["DUMP"] != nil
var video: VideoSource? = nil
if let vp = videoPath {
    guard let v = VideoSource(url: URL(fileURLWithPath: vp),
                              device: MTLCreateSystemDefaultDevice()!) else {
        fatalError("cannot open video \(vp)")
    }
    video = v
    W = v.width; H = v.height; srcFps = v.fps; frames = v.frameCount
}
let engine = try Engine(graphDir: genDir, width: W, height: H,
                        srcFps: srcFps, outFps: outFps, frameCount: frames,
                        sharedIntermediates: dumpMode)
if let v = video { engine.provideFrame = { v.texture(for: $0) } }
FileHandle.standardError.write("# \(engine.device.name), \(engine.graph.passes.count) passes\n"
    .data(using: .utf8)!)

// P2's full-field multi-scale scene (see METALPORT.md for the aliasing
// lesson its wavelengths encode). Kept verbatim for PSNR continuity.
let VX = 6.0
func scene(_ x: Double, _ y: Double, _ t: Double) -> Float {
    let u = x - VX * t
    let a = 0.5 + 0.16 * sin(2 * .pi * u / 173.0) + 0.13 * sin(2 * .pi * u / 89.0 + 0.7)
    let b = 0.09 * sin(2 * .pi * (u + 0.6 * y) / 127.0) + 0.07 * sin(2 * .pi * y / 97.0)
    let c = 0.05 * sin(2 * .pi * u / 47.0 + 2.1) + 0.02 * sin(2 * .pi * (u - y) / 19.0)
    return Float(min(max(a + b + c, 0.0), 1.0))
}

engine.fillFrame = { tex, idx in
    var row = [UInt16](repeating: 0, count: W * 4)
    if let data = inputData {
        let base = idx * W * H * 6
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
            let v = UInt16((min(max(scene(Double(x) + 0.5, Double(y) + 0.5, Double(idx)), 0), 1) * 65535).rounded())
            row[x * 4] = v; row[x * 4 + 1] = v; row[x * 4 + 2] = v; row[x * 4 + 3] = 65535
        }
        row.withUnsafeBytes {
            tex.replace(region: MTLRegionMake2D(0, y, W, 1), mipmapLevel: 0,
                        withBytes: $0.baseAddress!, bytesPerRow: W * 8)
        }
    }
}

// rgb48le export — matches ffmpeg's -pix_fmt rgb48le rawvideo, so the
// existing tools (accept.sh's PSNR, accelcheck.py) read it unchanged.
let exportHandle: FileHandle? = exportPath.map {
    FileManager.default.createFile(atPath: $0, contents: nil)
    return FileHandle(forWritingAtPath: $0)!
}
var exportRow = [UInt16](repeating: 0, count: W * H * 3)
var outPix = [Float16](repeating: 0, count: W * H * 4)
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

// P5 bench: the end-user measurement -- hardware decode, zero-copy
// upload, full graph, no readback (the UMA rows measured readback as
// ~free on this machine, so the number is comparable to the ffmpeg
// pipeline's downloaded rows either way).
if bench {
    let tb = DispatchTime.now()
    var rendered = 0
    for k in 0..<engine.outCount {
        let o = engine.render(outputIndex: k)
        if !o.wasHold { rendered += 1 }
    }
    let dtb = Double(DispatchTime.now().uptimeNanoseconds - tb.uptimeNanoseconds) / 1e9
    print(String(format: "bench: %d output frames (%dx%d, %.3f -> %.0f fps) in %.1fs = %.1f fps",
                 engine.outCount, W, H, srcFps, outFps, dtb,
                 Double(engine.outCount) / dtb))
    _ = rendered
    exit(0)
}
var interpPSNR: [Double] = []
var passthroughPSNR: [Double] = []
let t0 = DispatchTime.now()
for k in 0..<engine.outCount {
    let tSrc = Double(k) * srcFps / outFps
    let out = engine.render(outputIndex: k)
    if out.wasHold {
        if exportHandle != nil {
            exportSourceFrame(min(max(Int(tSrc.rounded()), 0), frames - 1))
        }
        continue
    }
    if dumpMode && k == 3 {
        for p in engine.graph.passes {
            let t = engine.front(p.save)
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
    out.image.getBytes(&outPix, bytesPerRow: W * 8,
                       from: MTLRegionMake2D(0, 0, W, H), mipmapLevel: 0)
    if exportHandle != nil { exportPixels(outPix) }
    if inputData != nil { continue }
    var se = 0.0
    for y in stride(from: 8, to: H - 8, by: 3) {
        for x in stride(from: 8, to: W - 8, by: 3) {
            let d = Double(outPix[(y * W + x) * 4]) - Double(scene(Double(x) + 0.5, Double(y) + 0.5, tSrc))
            se += d * d
        }
    }
    let n = Double(((H - 16 + 2) / 3) * ((W - 16 + 2) / 3))
    let psnr = 10 * log10(1.0 / (se / n + 1e-12))
    let i = Int(tSrc.rounded(.down))
    if abs(tSrc - Double(i)) < 1e-6 { passthroughPSNR.append(psnr) } else { interpPSNR.append(psnr) }
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
