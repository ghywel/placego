// Native Metal twin of vkbench.c. Same kernels (MSL translations, line for
// line), same grids, same per-batch dispatch counts, same barrier policy
// (explicit texture-scope barrier between dispatches), same wall-clock
// timing around one committed command buffer per batch.
// Usage: metalbench <alu|sad|tiny> [batches]
import Metal
import Foundation

let msl = """
#include <metal_stdlib>
using namespace metal;

kernel void initk(texture2d<float, access::write> A [[texture(0)]],
                  texture2d<float, access::write> B [[texture(1)]],
                  texture2d<float, access::write> O [[texture(2)]],
                  uint2 gid [[thread_position_in_grid]]) {
    float2 fp = float2(gid);
    float a = fract(sin(dot(fp, float2(12.9898, 78.233))) * 43758.5453);
    float b = fract(sin(dot(fp + float2(3.7, 1.3), float2(12.9898, 78.233))) * 43758.5453);
    A.write(float4(a), gid);
    B.write(float4(b), gid);
    O.write(float4(0.0), gid);
}

kernel void aluk(texture2d<float, access::read> A [[texture(0)]],
                 texture2d<float, access::read> B [[texture(1)]],
                 texture2d<float, access::write> O [[texture(2)]],
                 uint2 gid [[thread_position_in_grid]]) {
    float m = 0.999999 + A.read(gid).r * 1e-9;
    float c = B.read(gid).r * 1e-9;
    float a0 = float(gid.x) * 1e-3 + 0.1, a1 = a0 + 0.11, a2 = a0 + 0.22, a3 = a0 + 0.33;
    float a4 = float(gid.y) * 1e-3 + 0.5, a5 = a4 + 0.11, a6 = a4 + 0.22, a7 = a4 + 0.33;
    for (int i = 0; i < 2048; i++) {
        a0 = fma(a0, m, c); a1 = fma(a1, m, c);
        a2 = fma(a2, m, c); a3 = fma(a3, m, c);
        a4 = fma(a4, m, c); a5 = fma(a5, m, c);
        a6 = fma(a6, m, c); a7 = fma(a7, m, c);
    }
    O.write(float4(a0 + a1 + a2 + a3 + a4 + a5 + a6 + a7), gid);
}

kernel void sadk(texture2d<float, access::read> A [[texture(0)]],
                 texture2d<float, access::read> B [[texture(1)]],
                 texture2d<float, access::write> O [[texture(2)]],
                 uint2 gid [[thread_position_in_grid]]) {
    uint2 p0 = gid + uint2(64, 64);
    float best = 1e30;
    int bestIdx = 0;
    for (int dy = -2; dy <= 2; dy++)
    for (int dx = -2; dx <= 2; dx++) {
        float s = 0.0;
        for (int j = 0; j < 8; j++)
        for (int i = 0; i < 8; i++) {
            float av = A.read(p0 + uint2(i, j)).r;
            float bv = B.read(uint2(int2(p0) + int2(dx + i, dy + j))).r;
            s += abs(av - bv);
        }
        if (s < best * (1.0 - 1.0e-4)) { best = s; bestIdx = (dy + 2) * 5 + (dx + 2); }
    }
    O.write(float4(best + float(bestIdx) * 1e-3), gid);
}

kernel void tinyk(texture2d<float, access::read> A [[texture(0)]],
                  texture2d<float, access::read> B [[texture(1)]],
                  texture2d<float, access::read_write> O [[texture(2)]],
                  uint2 gid [[thread_position_in_grid]]) {
    float v = O.read(gid).r;
    O.write(float4(fma(v, 0.5, A.read(gid).r)), gid);
}
"""

let args = CommandLine.arguments
guard args.count >= 2 else { fputs("usage: metalbench <alu|sad|tiny> [batches]\n", stderr); exit(1) }
let mode = args[1]
let batches = args.count > 2 ? Int(args[2]) ?? 3 : 3

let ndisp: Int, gw: Int, gh: Int, kname: String
switch mode {
case "alu":  ndisp = 20;   gw = 1024; gh = 1024; kname = "aluk"
case "sad":  ndisp = 20;   gw = 1280; gh = 720;  kname = "sadk"
case "tiny": ndisp = 2000; gw = 16;   gh = 16;   kname = "tinyk"
default: fputs("unknown mode \(mode)\n", stderr); exit(1)
}

let dev = MTLCreateSystemDefaultDevice()!
FileHandle.standardError.write("# device: \(dev.name)\n".data(using: .utf8)!)
let lib = try dev.makeLibrary(source: msl, options: nil)
let initPSO = try dev.makeComputePipelineState(function: lib.makeFunction(name: "initk")!)
let benchPSO = try dev.makeComputePipelineState(function: lib.makeFunction(name: kname)!)
let queue = dev.makeCommandQueue()!

let td = MTLTextureDescriptor.texture2DDescriptor(
    pixelFormat: .r32Float, width: 2048, height: 1024, mipmapped: false)
td.usage = [.shaderRead, .shaderWrite]
td.storageMode = .private
let texA = dev.makeTexture(descriptor: td)!
let texB = dev.makeTexture(descriptor: td)!
let texO = dev.makeTexture(descriptor: td)!

let tg = MTLSize(width: 16, height: 16, depth: 1)

// Setup: init once.
do {
    let cb = queue.makeCommandBuffer()!
    let enc = cb.makeComputeCommandEncoder()!
    enc.setComputePipelineState(initPSO)
    enc.setTexture(texA, index: 0); enc.setTexture(texB, index: 1); enc.setTexture(texO, index: 2)
    enc.dispatchThreads(MTLSize(width: 2048, height: 1024, depth: 1), threadsPerThreadgroup: tg)
    enc.endEncoding()
    cb.commit(); cb.waitUntilCompleted()
}

// One batch = ndisp dispatches with an explicit texture barrier between,
// one command buffer, wall-clocked around commit+wait. Batch 0 warms up.
for b in 0...batches {
    let cb = queue.makeCommandBuffer()!
    let enc = cb.makeComputeCommandEncoder()!
    enc.setComputePipelineState(benchPSO)
    enc.setTexture(texA, index: 0); enc.setTexture(texB, index: 1); enc.setTexture(texO, index: 2)
    let grid = MTLSize(width: gw, height: gh, depth: 1)
    for _ in 0..<ndisp {
        enc.dispatchThreads(grid, threadsPerThreadgroup: tg)
        enc.memoryBarrier(scope: .textures)
    }
    enc.endEncoding()
    let t0 = DispatchTime.now()
    cb.commit(); cb.waitUntilCompleted()
    let t1 = DispatchTime.now()
    let ms = Double(t1.uptimeNanoseconds - t0.uptimeNanoseconds) / 1e6
    if b > 0 {
        print("\(mode),metal,\(String(format: "%.3f", ms)),\(String(format: "%.4f", ms / Double(ndisp)))")
    }
}
