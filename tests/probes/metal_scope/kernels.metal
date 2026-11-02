#include <metal_stdlib>
using namespace metal;
struct Params { uint n; uint steps; };
kernel void trajectories(const device uint *input [[buffer(0)]],
                         device uint *output [[buffer(1)]],
                         constant Params &p [[buffer(2)]],
                         uint i [[thread_position_in_grid]]) {
    if (i >= p.n) return;
    uint x = input[i];
    for (uint t=0; t<p.steps; ++t)
        x ^= ((x << 1) | (x >> 31)) | ((x << 2) | (x >> 30));
    output[i] = x;
}
kernel void graph_min(const device uint *dst [[buffer(0)]],
                      const device int *weight [[buffer(1)]],
                      const device int *oldv [[buffer(2)]],
                      device int *newv [[buffer(3)]],
                      constant Params &p [[buffer(4)]],
                      uint i [[thread_position_in_grid]]) {
    if (i >= p.n) return;
    int best = 1000000000;
    for (uint e=4*i; e<4*i+4; ++e) {
        int value = oldv[dst[e]];
        if (value < 1000000000) best = min(best, weight[e]+value);
    }
    newv[i] = best;
}
