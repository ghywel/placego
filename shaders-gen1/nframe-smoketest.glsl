// nframe-smoketest.glsl
//
// DIAGNOSTIC / SMOKE TEST -- not for production use, and not a companion
// to interpolate-debug-grid.glsl's flow visualization. This shader exists
// for exactly one purpose: to verify, on real hardware, that the N-frame
// generalization of PL_HOOK_FRAME_MIX actually works end to end -- that
// binding more than 2 frames resolves to genuinely distinct textures, that
// `rts_mix[]` holds sane per-frame timestamps, that `num_mix` reads back
// correctly, and that `pair_changed` correctly tracks a 4-frame window
// instead of just a pair. It doesn't attempt any real algorithm. See
// README.md's "What's new" for what the generalization actually is, and
// note that bidirectional-interpolation.glsl needed *zero* changes for it --
// HOOKED/NEXT still mean exactly what they always did (frame index 0/1),
// so the 2-frame production shader is unaffected either way.
//
// Binds FRAME0(HOOKED)..FRAME3, a concrete N=4 test -- comfortably below
// the PL_FRAME_MIX_MAX=8 ceiling, and enough to prove the mechanism
// generalizes past 2 without needing to exhaustively test every value.
//
// Layout: a 2x2 grid, each cell showing one bound frame's full picture
// (scaled down), in index order:
//   +------------+------------+
//   |  FRAME0    |   FRAME1   |
//   |  [P][N] ...|.........[1]|
//   +------------+------------+
//   |  FRAME2    |   FRAME3   |
//   |.........[2]|.........[3]|
//   +------------+------------+
//
// [P] pair_changed indicator (top-left corner, cell 0 only): red when
// this output frame's 4-frame window changed since the previous call,
// green when served from the same window as last time (only relative
// position within it moved). Same red/green convention as
// interpolate-debug-grid.glsl's cache indicator -- expect it to flash
// red/green following the same pattern the flow shader's cache indicator
// does, since both are driven by the same underlying pair_changed signal
// generalized to more frames.
//
// [N] num_mix readout (top-right corner, cell 0 only): a row of up to 8
// (== PL_FRAME_MIX_MAX) ticks, lit white for the first `num_mix` of them
// and dim gray for the rest. This shader always declares exactly 4 binds,
// so a correctly working build should show exactly 4 lit ticks on every
// frame the grid renders at all -- anything else (0, a number that
// flickers, etc.) means the frame_mix_count plumbing is wrong.
//
// [0]-[3] small corner tag (bottom-right of each cell): a fixed color per
// index (red/orange/yellow/green), purely so it's obvious at a glance
// which cell is which index. If two cells ever show visually identical
// content, that's the actual bug this shader exists to catch -- two
// different indices resolving to the same underlying texture instead of
// genuinely distinct ones.
//
// Thin bar along each cell's bottom edge: visualizes rts_mix[i] directly.
// A center tick marks the output timestamp (0); the bar extends left
// (blue) for a negative relative timestamp or right (orange) for a
// positive one, length proportional to |rts_mix[i]| (clamped at
// BAR_MAX_RTS nominal source-frame durations for display purposes). The
// two middle cells (FRAME1 via HOOKED/NEXT-style "nearest before/after"
// selection, i.e. cells 0 and 1 in a well-behaved 4-frame window) should
// show the shortest bars, growing outward from there -- if that ordering
// looks scrambled, the frame-selection logic picked a non-sensible window.
//
// Bound automatically by the FRAME_MIX hook stage:
//   HOOKED/FRAME0..FRAME3 = the 4 frames making up this hook's declared
//                           window, in ascending timestamp order
//   rts_mix[0..3]         = each frame's relative timestamp (see above)
//   num_mix                = how many of the above are valid (always 4
//                            for this shader specifically)
//   pair_changed            = whether the whole window changed since the
//                            previous output frame

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!BIND FRAME3
//!DESC [debug] N-frame smoke test (4-frame grid)

const float BAR_MAX_RTS = 3.0; // rts magnitude that maxes out the bar

vec3 index_color(int i) {
    if (i == 0) return vec3(1.0, 0.2, 0.2); // red
    if (i == 1) return vec3(1.0, 0.6, 0.1); // orange
    if (i == 2) return vec3(0.9, 0.9, 0.1); // yellow
    return vec3(0.2, 0.9, 0.3);             // green
}

vec4 frame_tex(int i, vec2 pos) {
    if (i == 0) return HOOKED_tex(pos);
    if (i == 1) return FRAME1_tex(pos);
    if (i == 2) return FRAME2_tex(pos);
    return FRAME3_tex(pos);
}

vec4 hook() {
    vec2 uv = HOOKED_pos;
    vec2 cell = floor(uv * 2.0);   // cell.x/y in {0, 1}
    vec2 local = fract(uv * 2.0);  // 0..1 within the selected cell

    int idx = int(cell.y) * 2 + int(cell.x); // 0=TL, 1=TR, 2=BL, 3=BR
    float rts = rts_mix[idx];

    // pair_changed indicator: top-left corner of cell 0 only.
    if (idx == 0 && local.x < 0.06 && local.y < 0.06)
        return pair_changed ? vec4(1.0, 0.0, 0.0, 1.0) : vec4(0.0, 1.0, 0.0, 1.0);

    // num_mix readout: a row of ticks in the top-right corner of cell 0.
    if (idx == 0 && local.y < 0.06 && local.x > 0.6) {
        const int MAX_TICKS = 8; // == PL_FRAME_MIX_MAX
        float slot = (local.x - 0.6) / 0.4 * float(MAX_TICKS);
        int tick = int(slot);
        bool gap = fract(slot) < 0.15; // thin gaps between ticks
        if (!gap) {
            return tick < num_mix ? vec4(1.0, 1.0, 1.0, 1.0)
                                   : vec4(0.15, 0.15, 0.15, 1.0);
        }
    }

    // Per-cell index tag: bottom-right corner.
    if (local.x > 0.94 && local.y > 0.94)
        return vec4(index_color(idx), 1.0);

    // Per-cell rts_mix[] bar: thin strip along the bottom edge.
    if (local.y > 0.9 && local.y < 0.94) {
        if (abs(local.x - 0.5) < 0.003)
            return vec4(1.0); // center tick at the output timestamp

        float mag = clamp(abs(rts) / BAR_MAX_RTS, 0.0, 1.0);
        float half_len = 0.45 * mag;
        if (rts < 0.0 && local.x > 0.5 - half_len && local.x < 0.5)
            return vec4(0.2, 0.5, 1.0, 1.0); // blue: before the output time
        if (rts >= 0.0 && local.x > 0.5 && local.x < 0.5 + half_len)
            return vec4(1.0, 0.6, 0.2, 1.0); // orange: after the output time
    }

    return frame_tex(idx, local);
}
