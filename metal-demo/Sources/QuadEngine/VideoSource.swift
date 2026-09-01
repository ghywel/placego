// Zero-copy video input: AVAssetReader -> CVPixelBuffer ->
// CVMetalTextureCache -> MTLTexture, the path unified memory makes nearly
// free and the ffmpeg pipeline structurally cannot take (the
// videotoolbox<->vulkan derive is ENOSYS; BUILDANDUSAGE.md). Decoded
// frames become engine source textures without a single CPU copy.
//
// The engine requests source indices monotonically (the window slides
// forward), so a sequential reader plus a small keep-alive dictionary of
// the last few CVMetalTextures is the whole design. reset() rebuilds the
// reader for loop restarts.
//
// TRAP, found the hard way: AVFoundation refuses HEVC in mp4 carrying the
// `hev1` sample entry -- which is what ffmpeg writes by DEFAULT -- with
// "Cannot Decode / decoder required for this media cannot be found"
// (-11833/-12906), even though the codec itself hardware-decodes fine.
// The fix is a copy remux, seconds, no transcode:
//     ffmpeg -i in.mp4 -c copy -tag:v hvc1 out.mp4
// Matroska is not AVFoundation-decodable at all; mp4/mov only.
import AVFoundation
import Metal
import CoreVideo

public final class VideoSource {
    /// Why the most recent init returned nil — the UI surfaces this
    /// instead of silently falling back (a failure that does not announce
    /// itself is this project's cardinal sin).
    public private(set) static var lastFailure: String?
    public let url: URL
    public let width: Int, height: Int
    public let fps: Double
    public let frameCount: Int

    private let device: MTLDevice
    private let asset: AVURLAsset      // retained: track.asset is weak, and
                                       // startReader needs the asset alive
    private var reader: AVAssetReader!
    private var output: AVAssetReaderTrackOutput!
    private let track: AVAssetTrack
    private var texCache: CVMetalTextureCache!
    private var live: [Int: (CVMetalTexture, MTLTexture)] = [:]
    private var nextIndex = 0

    public init?(url: URL, device: MTLDevice) {
        self.url = url
        self.device = device
        asset = AVURLAsset(url: url)
        // Synchronous accessors return nothing until values are loaded on
        // current macOS -- block here (init already runs off-main).
        let sem = DispatchSemaphore(value: 0)
        asset.loadValuesAsynchronously(forKeys: ["tracks", "duration"]) { sem.signal() }
        sem.wait()
        guard let t = asset.tracks(withMediaType: .video).first else {
            Self.lastFailure = "no video track (Matroska/.mkv is not AVFoundation-readable)"
            return nil
        }
        track = t
        let size = t.naturalSize.applying(t.preferredTransform)
        width = Int(abs(size.width)); height = Int(abs(size.height))
        fps = Double(t.nominalFrameRate)
        frameCount = Int((asset.duration.seconds * fps).rounded())
        guard frameCount > 4, width > 0 else {
            Self.lastFailure = "bad geometry \(width)×\(height), \(frameCount) frames"
            return nil
        }
        guard CVMetalTextureCacheCreate(nil, nil, device, nil, &texCache) == kCVReturnSuccess else {
            Self.lastFailure = "CVMetalTextureCache creation failed"
            return nil
        }
        guard startReader() else { return nil }   // startReader sets lastFailure
        Self.lastFailure = nil
    }

    private func startReader() -> Bool {
        guard let r = try? AVAssetReader(asset: asset) else { return false }
        let settings: [String: Any] = [
            kCVPixelBufferPixelFormatTypeKey as String: kCVPixelFormatType_32BGRA,
            kCVPixelBufferMetalCompatibilityKey as String: true,
        ]
        let o = AVAssetReaderTrackOutput(track: track, outputSettings: settings)
        o.alwaysCopiesSampleData = false
        guard r.canAdd(o) else {
            FileHandle.standardError.write("VideoSource: canAdd=false\n".data(using: .utf8)!)
            return false
        }
        r.add(o)
        guard r.startReading() else {
            let code = (r.error as NSError?)?.code ?? 0
            Self.lastFailure = code == -11833
                ? "decoder refused — ffmpeg's default hev1 HEVC tag; remux: ffmpeg -i in.mp4 -c copy -tag:v hvc1 out.mp4"
                : "reader failed: \(r.error?.localizedDescription ?? "unknown")"
            return false
        }
        reader = r; output = o
        return true
    }

    public func reset() {
        live.removeAll()
        nextIndex = 0
        reader.cancelReading()
        _ = startReader()
    }

    /// Texture for source frame `idx`. Sequential-forward contract: the
    /// engine's window never moves backward except via reset().
    public func texture(for idx: Int) -> MTLTexture {
        while nextIndex <= idx {
            guard let sample = output.copyNextSampleBuffer(),
                  let pb = CMSampleBufferGetImageBuffer(sample) else {
                // ran off the end (variable-rate tail): reuse the last frame
                if let last = live[nextIndex - 1] { live[nextIndex] = last; nextIndex += 1; continue }
                fatalError("video decode ran dry at frame \(nextIndex)")
            }
            var cvTex: CVMetalTexture?
            let w = CVPixelBufferGetWidth(pb), h = CVPixelBufferGetHeight(pb)
            guard CVMetalTextureCacheCreateTextureFromImage(
                    nil, texCache, pb, nil, .bgra8Unorm, w, h, 0, &cvTex) == kCVReturnSuccess,
                  let cv = cvTex, let mtl = CVMetalTextureGetTexture(cv) else {
                fatalError("CVMetalTexture creation failed at frame \(nextIndex)")
            }
            live[nextIndex] = (cv, mtl)     // the CVMetalTexture ref keeps the IOSurface alive
            live[nextIndex - 6] = nil       // window is 4 wide; keep a small margin
            nextIndex += 1
        }
        return live[idx]!.1
    }
}
