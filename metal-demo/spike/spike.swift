// P0 spike harness: compile the spirv-cross MSL of the real coarse-flow
// pass, run it on a known translation (B = A shifted by +2,+1 texels of
// random texture), and check the argmin recovers that motion. Passing
// means the whole GLSL -> SPIR-V -> MSL -> Metal road preserves the
// pass's semantics, not merely its syntax.
import Metal
import Foundation

let W = 240, H = 135
let dev = MTLCreateSystemDefaultDevice()!
let src = try String(contentsOfFile: "spike_pass.metal", encoding: .utf8)
let lib = try dev.makeLibrary(source: src, options: nil)
let pso = try dev.makeComputePipelineState(function: lib.makeFunction(name: "main0")!)
let q = dev.makeCommandQueue()!

func makeTex(_ fmt: MTLPixelFormat, usage: MTLTextureUsage, shared: Bool) -> MTLTexture {
    let d = MTLTextureDescriptor.texture2DDescriptor(pixelFormat: fmt, width: W, height: H, mipmapped: false)
    d.usage = usage
    d.storageMode = shared ? .shared : .private
    return dev.makeTexture(descriptor: d)!
}

// Textured pattern; B is A translated by (+2,+1) with wrap.
func pattern(_ x: Int, _ y: Int) -> Float {
    // Smooth periodic texture inside the search's design envelope: integer
    // cycle counts so the shift wraps cleanly; 5x5 contrast well over the
    // MIN_CONTRAST gate; SAD surface smooth at sub-texel offsets.
    let fx = 2.0 * Double.pi * Double(x) * 22.0 / Double(W)
    let fy = 2.0 * Double.pi * Double(y) * 13.0 / Double(H)
    return Float(0.5 + 0.22 * sin(fx) + 0.22 * sin(fy) + 0.06 * sin(fx * 3.1 + fy * 2.3))
}
let lumaA = makeTex(.r16Float, usage: [.shaderRead], shared: true)
let lumaB = makeTex(.r16Float, usage: [.shaderRead], shared: true)
var rowA = [Float16](repeating: 0, count: W)
var rowB = [Float16](repeating: 0, count: W)
for y in 0..<H {
    for x in 0..<W {
        rowA[x] = Float16(pattern(x, y))
        rowB[x] = Float16(pattern((x - 1 + W) % W, y))  // shift +1 texel in x, within reach
    }
    rowA.withUnsafeBytes { lumaA.replace(region: MTLRegionMake2D(0, y, W, 1), mipmapLevel: 0, withBytes: $0.baseAddress!, bytesPerRow: W * 2) }
    rowB.withUnsafeBytes { lumaB.replace(region: MTLRegionMake2D(0, y, W, 1), mipmapLevel: 0, withBytes: $0.baseAddress!, bytesPerRow: W * 2) }
}
let cache = makeTex(.rgba32Float, usage: [.shaderRead, .shaderWrite], shared: false)
let out   = makeTex(.rgba32Float, usage: [.shaderWrite, .shaderRead], shared: true)

let sd = MTLSamplerDescriptor()
sd.minFilter = .linear; sd.magFilter = .linear
sd.sAddressMode = .clampToEdge; sd.tAddressMode = .clampToEdge
sd.normalizedCoordinates = true
let smplr = dev.makeSamplerState(descriptor: sd)!

// Params (std140): vec2 out_size; vec2 luma_size; int pair_changed
var params = [Float](repeating: 0, count: 8)
params[0] = Float(W); params[1] = Float(H)
params[2] = Float(W); params[3] = Float(H)
let pbuf = dev.makeBuffer(length: 32, options: .storageModeShared)!
memcpy(pbuf.contents(), params, 16)
var pc: Int32 = 1
memcpy(pbuf.contents() + 16, &pc, 4)

let cb = q.makeCommandBuffer()!
let enc = cb.makeComputeCommandEncoder()!
enc.setComputePipelineState(pso)
enc.setBuffer(pbuf, offset: 0, index: 0)
enc.setTexture(lumaA, index: 0); enc.setTexture(lumaB, index: 1)
enc.setTexture(cache, index: 2); enc.setTexture(out, index: 3)
enc.setSamplerState(smplr, index: 0); enc.setSamplerState(smplr, index: 1)
enc.dispatchThreads(MTLSize(width: W, height: H, depth: 1),
                    threadsPerThreadgroup: MTLSize(width: 16, height: 16, depth: 1))
enc.endEncoding()
cb.commit(); cb.waitUntilCompleted()
if let err = cb.error { print("GPU error: \(err)"); exit(1) }

// Read back: histogram the flow vectors (out.xy).
var px = [Float](repeating: 0, count: W * H * 4)
out.getBytes(&px, bytesPerRow: W * 16, from: MTLRegionMake2D(0, 0, W, H), mipmapLevel: 0)
var hist: [String: Int] = [:]
for i in 0..<(W * H) {
    let fx = px[i * 4], fy = px[i * 4 + 1]
    hist["(\(Int(fx.rounded())),\(Int(fy.rounded())))", default: 0] += 1
}
let top = hist.sorted { $0.value > $1.value }.prefix(4)
print("flow vector histogram (expect (1,0)):")
for (k, v) in top { print("  \(k)  \(v) texels (\(String(format: "%.1f", 100.0 * Double(v) / Double(W * H)))%)") }
