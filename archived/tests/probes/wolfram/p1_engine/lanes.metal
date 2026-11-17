// P1, the exact lane engine for Q01 death times (GPU-METAL-JOBS.md §J.1, revision 2; Local, 2026-10-24).
//
// The kit's zero-boundary half line: depth coordinates, the wall at depth 0 held white,
//   (Fx)_k = x_{k+1} xor (x_k or x_{k-1})  for k >= 1,   (Fx)_0 = 0.
// d(L) = the least EVEN ordinary time t at which depth 1 is white; a lane alive at the cutoff T is censored (d > T).
//
// Lanes: one lane is one free-bit index n; bit i of n is the odd trace bit a(2i+1) (the value of depth 1 at time
// 2i+1); the even trace bits are 1. LW lanes per word (32 with uint, 64 with ulong, chosen by the LANE64 macro).
// A lane-group is one word's worth of lanes; group g has a base index base[g] (a multiple of LW) and a valid mask.
// Row layout, depth-major and interleaved by group for coalescing: row k of group g is rows[k * G + g].
//
// The finite-row contract (§J.1 revision 2, GC1776): indices 0..L-1 with L = Wsup + T + 2; row[0] = 0 (the wall);
// at time t, row[k] = 0 for every k > Wsup + t (the support bound Wsup + t is inclusive); the step computes
// new[k] for 1 <= k <= Wsup + t + 1 (so the new edge cell is computed from row[Wsup+t+2] = row[Wsup+t+1] = 0);
// the halo above stays zero and is never read uninitialised; the run stops at t = T without stepping again.
// Implementation note: the step runs IN PLACE over one buffer with the old value of row[k-1] carried in a register
// (new[k] needs old[k+1], old[k], old[k-1]; old[k+1] is read before it is overwritten at the next k); the semantics
// equal the two-buffer contract cell for cell, which the trace control checks against the scalar engine.

#include <metal_stdlib>
using namespace metal;

#ifdef LANE64
typedef ulong lane_t;
constant uint LW = 64;
constant uint LOG2LW = 6;
#else
typedef uint lane_t;
constant uint LW = 32;
constant uint LOG2LW = 5;
#endif

struct Params {
    uint W;           // class width for build_start (free bits floor(W/2)); the start is truncated to depths <= W
    uint T;           // cutoff
    uint Wsup;        // support bound of the initial rows (W for built starts; given for uploaded rows)
    uint L;           // row length, Wsup + T + 2
    uint G;           // lane-groups in this batch
    uint traceSteps;  // > 0: group 0's rows are copied out for t = 0..traceSteps
};

// The lane pattern for index bit i < LOG2LW: bit l of the word is bit i of l.
static inline lane_t lane_pattern(uint i) {
    lane_t w = 0;
    for (uint l = 0; l < LW; l++) {
        if ((l >> i) & 1u) w |= ((lane_t)1) << l;
    }
    return w;
}

// The depth-1 trace word at time t for a group whose base index is b (b a multiple of LW).
static inline lane_t trace_word(ulong b, uint t) {
    if ((t & 1u) == 0u) return ~((lane_t)0);
    uint i = (t - 1u) >> 1;
    if (i < LOG2LW) return lane_pattern(i);
    return ((b >> i) & 1ul) ? ~((lane_t)0) : (lane_t)0;
}

// Build the start of every lane from its trace: column k holds cell(t, k) for t = 0..W-k, column 0 = 0 (the wall),
// column 1 = the trace; col[k+1][t] = col[k][t+1] xor (col[k][t] or col[k-1][t]); the start's depth k is col[k][0].
// Workspace: two columns of W+1 words per group (A = column k-1, overwritten in place by column k+1; B = column k).
kernel void build_start(device lane_t* rows          [[buffer(0)]],
                        device const ulong* base      [[buffer(1)]],
                        device lane_t* ws             [[buffer(2)]],
                        constant Params& P            [[buffer(3)]],
                        uint g [[thread_position_in_grid]])
{
    if (g >= P.G) return;
    const uint W = P.W, G = P.G, L = P.L;
    const ulong b = base[g];
    device lane_t* A = ws + g;
    device lane_t* B = ws + (ulong)(W + 1) * G + g;
    for (uint t = 0; t < W; t++) { A[(ulong)t * G] = 0; B[(ulong)t * G] = trace_word(b, t); }
    rows[g] = 0;                                  // the wall
    if (W >= 1) rows[(ulong)1 * G + g] = B[0];
    for (uint k = 1; k + 1 <= W; k++) {
        // column k+1 at t = 0..W-k-1, written over column k-1 (A); column k is B
        for (uint t = 0; t + k + 1 <= W; t++) {
            A[(ulong)t * G] = B[(ulong)(t + 1) * G] ^ (B[(ulong)t * G] | A[(ulong)t * G]);
        }
        rows[(ulong)(k + 1) * G + g] = A[0];
        device lane_t* tmp = A; A = B; B = tmp;  // now B = column k+1, A = column k
    }
    for (uint k = W + 1; k < L; k++) rows[(ulong)k * G + g] = 0;   // truncation to width W, and the halo
}

// The GPU-side reduction (revision 2): a histogram of death times in bins t/2 (deaths happen at even t only), the
// censored lanes in the last bin, accumulated per threadgroup in threadgroup memory with ONE atomic add per death event
// (all lanes of a group that die at the same t are added as one popcount), then flushed to the device histogram with
// one atomic add per non-zero bin per threadgroup; and the per-group maximum death (0xFFFF if any lane is censored,
// 0 for a group with no valid lane), from which the host finds the maximizers without scanning every lane.
constant uint HB = 2048;            // bins; requires T <= 2 * (HB - 2); the host checks

// Simulate to the cutoff, recording each lane's first even white time at depth 1 (0xFFFF = censored, d > T).
kernel void simulate(device lane_t* rows             [[buffer(0)]],
                     device const lane_t* valid      [[buffer(1)]],
                     device ushort* death            [[buffer(2)]],
                     constant Params& P              [[buffer(3)]],
                     device lane_t* traceOut         [[buffer(4)]],
                     device atomic_uint* hist        [[buffer(5)]],
                     device ushort* gmax             [[buffer(6)]],
                     uint g [[thread_position_in_grid]],
                     uint tid [[thread_index_in_threadgroup]],
                     uint tpg [[threads_per_threadgroup]])
{
    threadgroup atomic_uint th[HB];
    for (uint i = tid; i < HB; i += tpg) atomic_store_explicit(&th[i], 0u, memory_order_relaxed);
    threadgroup_barrier(mem_flags::mem_threadgroup);
    if (g < P.G) {
    const uint G = P.G, T = P.T, Wsup = P.Wsup, L = P.L;
    const lane_t vm = valid[g];
    lane_t dead = 0;
    ushort gm = 0;
    for (uint l = 0; l < LW; l++) death[(ulong)g * LW + l] = 0xFFFF;
    for (uint t = 0; ; t++) {
        if (P.traceSteps > 0 && g == 0 && t <= P.traceSteps) {
            for (uint k = 0; k < L; k++) traceOut[(ulong)t * L + k] = rows[(ulong)k * G];
        }
        if ((t & 1u) == 0u) {
            lane_t newly = ~rows[(ulong)1 * G + g] & ~dead & vm;
            dead |= newly;
            if (newly != 0) { atomic_fetch_add_explicit(&th[t >> 1], (uint)popcount(newly), memory_order_relaxed); gm = (ushort)t; }
            while (newly != 0) {
                uint l = ctz(newly);
                death[(ulong)g * LW + l] = (ushort)t;
                newly &= newly - (lane_t)1;
            }
            if ((dead & vm) == vm) break;
        }
        if (t == T) break;
#ifdef MUTANT_DROP_EDGE
        const uint kmax = min(Wsup + t, L - 2u);         // NEGATIVE CONTROL ONLY: the first draft's bug (the new edge cell is not computed)
#else
        const uint kmax = min(Wsup + t + 1u, L - 2u);
#endif
        lane_t prev = 0;                           // old row[0], the wall
        lane_t cur = rows[(ulong)1 * G + g];       // old row[1]
        for (uint k = 1; k <= kmax; k++) {
            const lane_t nxt = rows[(ulong)(k + 1) * G + g];
            rows[(ulong)k * G + g] = nxt ^ (cur | prev);
            prev = cur; cur = nxt;
        }
    }
    const lane_t alive = vm & ~dead;
    if (alive != 0) { atomic_fetch_add_explicit(&th[HB - 1], (uint)popcount(alive), memory_order_relaxed); gm = 0xFFFF; }
    gmax[g] = gm;
    }
    threadgroup_barrier(mem_flags::mem_threadgroup);
    for (uint i = tid; i < HB; i += tpg) {
        const uint v = atomic_load_explicit(&th[i], memory_order_relaxed);
        if (v != 0u) atomic_fetch_add_explicit(&hist[i], v, memory_order_relaxed);
    }
}
