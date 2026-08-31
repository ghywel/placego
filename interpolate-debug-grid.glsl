// interpolate-debug-grid.glsl
//
// DIAGNOSTIC BUILD -- not for production use. Identical flow pyramid to
// bidirectional-interpolation.glsl (same 4-level bidirectional search, same
// REG_LAMBDA, same double vector-median filter, same forward/backward
// consistency check, same STORAGE-backed flow caching gated on
// `pair_changed` -- see bidirectional-interpolation.glsl's header for why),
// but the final pass replaces the actual warp/blend output with a 3x2
// diagnostic grid so a single exported still frame shows the flow field
// directly instead of just its (possibly misleading) end result. Keeping
// this in lockstep with the high tier's actual pyramid matters -- a debug
// view built on a simplified stand-in pyramid wouldn't necessarily
// reflect what the production shader is really doing.
//
// Layout of the output frame (each cell shows the full frame, scaled down):
//   +------------+------------+------------+
//   |  source A  |  source B  | flow color |
//   |  (HOOKED)  |  (NEXT)    | wheel (AB) |
//   |            |            | [C]    [F] |
//   +------------+------------+------------+
//   | flow magni-| occlusion  |  actual    |
//   | tude heat- | (FB-error) |  warped    |
//   | map (AB)   |  mask      |  result    |
//   +------------+------------+------------+
//
// Color wheel (top-right): hue = direction of the A->B flow vector,
// brightness = magnitude (black = zero motion). Standard optical-flow
// visualization convention (same one Middlebury/KITTI benchmarks use).
// Rough hue key: red = motion to the right, cyan = motion to the left,
// yellow-green = motion up, purple/blue = motion down (screen space, +y
// down). Exact hue isn't important -- what matters is whether regions
// that should be a single rigid object show a SINGLE consistent color
// (correct) or a patchwork of different colors/brightnesses (wrong).
//
// [C] Cache indicator, top-LEFT corner of the flow-color cell: RED when
// this output frame recomputed the flow field, GREEN when it was served
// from the storage cache. This is the direct way to verify the caching
// is working at all -- on a working cache at e.g. a 2.5x fps ratio,
// expect it to flash red roughly 2 frames out of every 5 and green the
// rest. Solid red on every frame means the cache isn't engaging (check
// that your build actually has the `pair_changed` field -- see
// bidirectional-interpolation.glsl's header for the patch-version note).
//
// [F] Fallback indicator, top-RIGHT corner of the flow-color cell: shows
// how much of THIS output frame is being faded toward an unwarped source
// frame rather than shown as a genuine motion-compensated interpolation
// (the same occluded/fallback decision the bottom-middle mask visualizes
// per-pixel, reduced here to a single frame-level color so it's legible
// at a glance during playback, the same way the cache box is). It probes
// a coarse 5x5 grid of points across the frame, averages their occlusion
// value, and colors black->yellow->red as that average rises -- black
// means this frame is (almost) entirely trusting the motion-compensated
// warp, red means a large enough fraction of it is falling back to a
// plain unwarped frame that it's effectively not being interpolated.
// Since real occluded regions are usually a minority of the frame area,
// the average is amplified (see FALLBACK_INDICATOR_GAIN below) so it
// still lights up meaningfully rather than staying near-black whenever
// only a small object is occluded.
//
// Magnitude heatmap (bottom-left): black = zero px motion, white = at the
// clamp ceiling (30px by default, see MAX_PX below), MAGENTA = motion
// *larger* than the ceiling -- magenta pixels are the most likely sites
// of a genuine bug (runaway/outlier vectors), not just an under-tuned
// search.
//
// Occlusion mask (bottom-middle): white = the forward/backward
// consistency check considers the flow unreliable here, and the final
// result blends toward the nearest *unwarped* source frame instead of
// trusting the motion-compensated warp; black = fully trusting the warp.
// White regions predict where warping artifacts are most likely, since
// warped_a/warped_b were both sampled using the same (unreliable)
// flow_ab -- useful both for checking whether the heuristic is firing
// where it should (real occlusion/motion boundaries) and as a direct
// predictor of visible warp artifacts.
//
// Bound automatically by the FRAME_MIX hook stage:
//   HOOKED  = source frame immediately before the output timestamp
//   NEXT    = source frame immediately after the output timestamp
//   mix_t   = 0.0 (at HOOKED) .. 1.0 (at NEXT) position of the output frame

// ---------------------------------------------------------------------
// Sixteenth-res luma (coarsest search level)
// ---------------------------------------------------------------------
//!HOOK FRAME_MIX
//!BIND HOOKED
//!SAVE LUMA_A_S
//!WIDTH HOOKED.w 16 /
//!HEIGHT HOOKED.h 16 /
//!COMPONENTS 1
//!DESC [debug] downsample frame A to 1/16 res (luma)
vec4 hook() {
    return vec4(dot(HOOKED_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!HOOK FRAME_MIX
//!BIND NEXT
//!SAVE LUMA_B_S
//!WIDTH HOOKED.w 16 /
//!HEIGHT HOOKED.h 16 /
//!COMPONENTS 1
//!DESC [debug] downsample frame B to 1/16 res (luma)
vec4 hook() {
    return vec4(dot(NEXT_tex(NEXT_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

// ---------------------------------------------------------------------
// Sixteenth-res coarse search, both directions: 5-step, 5x5 SAD window
// ---------------------------------------------------------------------
//!TEXTURE FLOW_S_AB_CACHE
//!SIZE 240 135
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_S_AB_CACHE
//!BIND LUMA_A_S
//!BIND LUMA_B_S
//!SAVE FLOW_S_AB
//!WIDTH HOOKED.w 16 /
//!HEIGHT HOOKED.h 16 /
//!COMPONENTS 2
//!DESC [debug] coarse flow search A->B (1/16 res)

// Matching-window radius for the coarse SAD cost below. RE-TESTING at 1
// (3x3), now that the coarse-to-fine seed-snapping fix (see snap_texel()
// in the refine passes below) revealed this level's own ~16px-block
// granularity instead of smoothing it away -- the first test of this
// constant predates that fix and may have been confounded by it. Mirrors
// bidirectional-interpolation.glsl's identical constant exactly -- see
// that file's coarse search pass for the full reasoning.
const int COARSE_WINDOW_RADIUS = 1;

float sad5x5_s(vec2 uv_a, vec2 uv_b) {
    float s = 0.0;
    for (int y = -COARSE_WINDOW_RADIUS; y <= COARSE_WINDOW_RADIUS; y++) {
        for (int x = -COARSE_WINDOW_RADIUS; x <= COARSE_WINDOW_RADIUS; x++) {
            vec2 o = vec2(float(x), float(y)) * LUMA_A_S_pt;
            s += abs(LUMA_A_S_tex(uv_a + o).r - LUMA_B_S_tex(uv_b + o).r);
        }
    }
    return s;
}

// Local contrast (max-min luma) of the reference block. Below
// MIN_CONTRAST, this block has essentially no real texture to match
// against -- dark/shadow sensor noise, or a genuinely flat surface -- so
// whatever offset the search below finds is closer to a random noise
// correlation than a real motion estimate. Mirrors
// bidirectional-interpolation.glsl's identical gate exactly -- see that
// file's coarse search pass for the full reasoning. This is the gate
// that shows up as the flow-color-wheel cell going from an incoherent
// multicolor patchwork to solid black in low-signal regions once it's
// working correctly.
const float MIN_CONTRAST = 0.02;

float local_contrast_5x5_s(vec2 uv_a) {
    float lo = 1.0, hi = 0.0;
    for (int y = -2; y <= 2; y++) {
        for (int x = -2; x <= 2; x++) {
            float v = LUMA_A_S_tex(uv_a + vec2(float(x), float(y)) * LUMA_A_S_pt).r;
            lo = min(lo, v);
            hi = max(hi, v);
        }
    }
    return hi - lo;
}

const float REG_LAMBDA = 0.06;

vec4 hook() {
    ivec2 coord = ivec2(LUMA_A_S_pos * LUMA_A_S_size);
    if (!pair_changed)
        return imageLoad(FLOW_S_AB_CACHE, coord);

    vec2 uv_a = LUMA_A_S_pos;

    if (local_contrast_5x5_s(uv_a) < MIN_CONTRAST) {
        vec4 result = vec4(0.0);
        imageStore(FLOW_S_AB_CACHE, coord, result);
        return result;
    }

    vec2 best_off = vec2(0.0);
    // Deterministic tie-breaking. The search below is an argmin over
    // candidate offsets, and a strict `<` against a fixed scan order already
    // resolves an EXACT tie deterministically -- the incumbent wins. That is
    // not the problem. The problem is the NEAR-tie: where the cost surface is
    // flat, two candidates differ by less than the arithmetic noise between
    // one evaluation and another, and which of them compares smaller stops
    // being a property of the image at all. The chosen motion vector then
    // flips on a rounding difference, and the whole warp for this source pair
    // is built on it.
    //
    // Linux and Windows hide this completely by being bit-reproducible run to
    // run -- the fragility is real, but nothing there ever perturbs it. macOS,
    // whose MoltenVK path is not reproducible, amplified one wrong LSB into
    // 9-14 ruined frames in 60. See BUILDANDUSAGE.md for those measurements.
    //
    // The fix is a MARGIN, not a tie rule. A rule for exact ties would have
    // been a no-op, since those were already decided by scan order; what needs
    // deciding is the near-tie. Requiring a candidate to beat the incumbent by
    // a relative TIE_MARGIN moves the decision threshold off the plateau where
    // the ambiguity lives: a flat cost surface sits at a cost ratio of ~1.0,
    // nowhere near the threshold, so the outcome stops depending on the last
    // bits. The margin is relative because floating-point error is relative --
    // it then holds the same ratio to the noise whether the block matches well
    // or badly.
    //
    // Preferring the incumbent is also the right bias on the merits, not just
    // a convenient way to be deterministic. Here the incumbent is the previous
    // iteration's estimate, seeded at zero motion; at the refine levels it is
    // the coarse level's result. Both are the conservative answer REG_LAMBDA
    // already argues for, so a genuine tie now resolves toward less motion
    // rather than toward whichever candidate the loop happened to visit first.
    //
    // The value is measured, not assumed. tests/tieprobe.sh perturbs every cost
    // by a relative epsilon and counts the output frames that then disagree.
    // Without a margin, 56 of 240 frames flip at ANY perturbation large enough
    // to survive float32 at all -- 1e-7 and 1e-5 do equal damage, which is what
    // "no defence" looks like. At 1e-7, one ULP, the scale a differing
    // summation order actually produces, this margin takes that to 0, and it
    // costs at most 0.02 dB anywhere on the ground-truth ladder.
    //
    // Bigger is not better. A larger margin buys headroom against coarser
    // perturbation but starts refusing genuine improvements where the cost
    // surface is legitimately shallow: 1e-2 costs 0.12 dB at L3/L4 and 0.07 at
    // M3 -- the velocity ceiling and the period-16 ambiguity trap, exactly the
    // cases that are hardest already. Full sweep in tests/TESTING.md.
    const float TIE_MARGIN = 1.0e-4;
    float best_cost = sad5x5_s(uv_a, uv_a);

    // Starting step, halved each of the 5 iterations below: total reach is
    // step_px * 1.9375 coarse-level pixels, i.e. * 16 again for full-res
    // pixels (this level is 1/16 resolution). At the old 1.5 that's ~46px
    // full-res -- comfortably past MAX_PX (30px, see the color-wheel
    // magenta convention below), meaning the search could reach and lock
    // onto a spurious match well beyond what any real per-frame motion in
    // typical content would need, given enough repetitive-looking texture
    // to fool it (confirmed on real footage: a backlit hair/shoulder edge
    // against blurred bokeh, which is exactly this kind of ambiguous,
    // semi-repetitive content). 0.75 caps full-res reach at ~23px -- if
    // genuinely fast motion is now being under-tracked, raise this back up
    // gradually; if long-reach false matches persist, lower it further or
    // strengthen REG_LAMBDA above instead (which biases against distant
    // candidates without hard-capping reach the way this does).
    float step_px = 0.75;
    for (int iter = 0; iter < 5; iter++) {
        vec2 cand_best = best_off;
        for (int y = -1; y <= 1; y++) {
            for (int x = -1; x <= 1; x++) {
                if (x == 0 && y == 0)
                    continue;
                vec2 off = best_off + vec2(float(x), float(y)) * step_px * LUMA_A_S_pt;
                float cost = sad5x5_s(uv_a, uv_a + off)
                           + REG_LAMBDA * length(off / LUMA_A_S_pt);
                if (cost < best_cost * (1.0 - TIE_MARGIN)) {
                    best_cost = cost;
                    cand_best = off;
                }
            }
        }
        best_off = cand_best;
        step_px *= 0.5;
    }

    vec4 result = vec4(best_off / LUMA_A_S_pt, 0.0, 0.0);
    imageStore(FLOW_S_AB_CACHE, coord, result);
    return result;
}

//!TEXTURE FLOW_S_BA_CACHE
//!SIZE 240 135
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_S_BA_CACHE
//!BIND LUMA_A_S
//!BIND LUMA_B_S
//!SAVE FLOW_S_BA
//!WIDTH HOOKED.w 16 /
//!HEIGHT HOOKED.h 16 /
//!COMPONENTS 2
//!DESC [debug] coarse flow search B->A (1/16 res)

// See COARSE_WINDOW_RADIUS in the A->B pass above.
const int COARSE_WINDOW_RADIUS = 1;

float sad5x5_s2(vec2 uv_b, vec2 uv_a) {
    float s = 0.0;
    for (int y = -COARSE_WINDOW_RADIUS; y <= COARSE_WINDOW_RADIUS; y++) {
        for (int x = -COARSE_WINDOW_RADIUS; x <= COARSE_WINDOW_RADIUS; x++) {
            vec2 o = vec2(float(x), float(y)) * LUMA_A_S_pt;
            s += abs(LUMA_B_S_tex(uv_b + o).r - LUMA_A_S_tex(uv_a + o).r);
        }
    }
    return s;
}

// See local_contrast_5x5_s()/MIN_CONTRAST in the A->B pass above.
const float MIN_CONTRAST = 0.02;

float local_contrast_5x5_s2(vec2 uv_b) {
    float lo = 1.0, hi = 0.0;
    for (int y = -2; y <= 2; y++) {
        for (int x = -2; x <= 2; x++) {
            float v = LUMA_B_S_tex(uv_b + vec2(float(x), float(y)) * LUMA_A_S_pt).r;
            lo = min(lo, v);
            hi = max(hi, v);
        }
    }
    return hi - lo;
}

const float REG_LAMBDA = 0.06;

vec4 hook() {
    ivec2 coord = ivec2(LUMA_B_S_pos * LUMA_B_S_size);
    if (!pair_changed)
        return imageLoad(FLOW_S_BA_CACHE, coord);

    vec2 uv_b = LUMA_B_S_pos;

    if (local_contrast_5x5_s2(uv_b) < MIN_CONTRAST) {
        vec4 result = vec4(0.0);
        imageStore(FLOW_S_BA_CACHE, coord, result);
        return result;
    }

    vec2 best_off = vec2(0.0);
    // See TIE_MARGIN in the coarse A->B search above.
    const float TIE_MARGIN = 1.0e-4;
    float best_cost = sad5x5_s2(uv_b, uv_b);

    // See the A->B pass above for the reach/reasoning behind this value.
    float step_px = 0.75;
    for (int iter = 0; iter < 5; iter++) {
        vec2 cand_best = best_off;
        for (int y = -1; y <= 1; y++) {
            for (int x = -1; x <= 1; x++) {
                if (x == 0 && y == 0)
                    continue;
                vec2 off = best_off + vec2(float(x), float(y)) * step_px * LUMA_A_S_pt;
                float cost = sad5x5_s2(uv_b, uv_b + off)
                           + REG_LAMBDA * length(off / LUMA_A_S_pt);
                if (cost < best_cost * (1.0 - TIE_MARGIN)) {
                    best_cost = cost;
                    cand_best = off;
                }
            }
        }
        best_off = cand_best;
        step_px *= 0.5;
    }

    vec4 result = vec4(best_off / LUMA_A_S_pt, 0.0, 0.0);
    imageStore(FLOW_S_BA_CACHE, coord, result);
    return result;
}

// ---------------------------------------------------------------------
// Refinement levels: eighth, quarter, half res. Each level downsamples
// luma, then refines both AB and BA flow fields from the previous
// (coarser) level with a 3x3, one-pixel-step search.
// ---------------------------------------------------------------------

//!HOOK FRAME_MIX
//!BIND HOOKED
//!SAVE LUMA_A_E
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 1
//!DESC [debug] downsample frame A to 1/8 res (luma)
vec4 hook() {
    return vec4(dot(HOOKED_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!HOOK FRAME_MIX
//!BIND NEXT
//!SAVE LUMA_B_E
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 1
//!DESC [debug] downsample frame B to 1/8 res (luma)
vec4 hook() {
    return vec4(dot(NEXT_tex(NEXT_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!TEXTURE FLOW_E_AB_CACHE
//!SIZE 480 270
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_E_AB_CACHE
//!BIND LUMA_A_E
//!BIND LUMA_B_E
//!BIND FLOW_S_AB
//!SAVE FLOW_E_AB
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 2
//!DESC [debug] refine flow A->B (1/8 res)

// Snaps the coarse-level seed read to its exact texel center before
// sampling -- see bidirectional-interpolation.glsl's identical fix (same
// three handoffs, S->E/E->Q/Q->H) for the full reasoning.
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

// Same window-narrowing fix as the S level's COARSE_WINDOW_RADIUS --
// see bidirectional-interpolation.glsl for the full reasoning.
const int COARSE_WINDOW_RADIUS = 1;

float sad5x5_e(vec2 uv_a, vec2 uv_b) {
    float s = 0.0;
    for (int y = -COARSE_WINDOW_RADIUS; y <= COARSE_WINDOW_RADIUS; y++) {
        for (int x = -COARSE_WINDOW_RADIUS; x <= COARSE_WINDOW_RADIUS; x++) {
            vec2 o = vec2(float(x), float(y)) * LUMA_A_E_pt;
            s += abs(LUMA_A_E_tex(uv_a + o).r - LUMA_B_E_tex(uv_b + o).r);
        }
    }
    return s;
}

// Same low-signal gate as the coarse search (see that pass for the full
// reasoning), re-checked at this level's own resolution -- this level's
// local search has no regularization of its own, so a correctly-zeroed
// coarse seed could still drift on pure noise here, then again at the
// next level, compounding across all three refine levels.
// TESTING at 0.0 (was 0.02), disabling this level's early-exit entirely
// -- see bidirectional-interpolation.glsl's E-level A->B pass for the full
// reasoning.
const float MIN_CONTRAST = 0.0;

float local_contrast_5x5_e(vec2 uv_a) {
    float lo = 1.0, hi = 0.0;
    for (int y = -2; y <= 2; y++) {
        for (int x = -2; x <= 2; x++) {
            float v = LUMA_A_E_tex(uv_a + vec2(float(x), float(y)) * LUMA_A_E_pt).r;
            lo = min(lo, v);
            hi = max(hi, v);
        }
    }
    return hi - lo;
}

vec4 hook() {
    ivec2 coord = ivec2(LUMA_A_E_pos * LUMA_A_E_size);
    if (!pair_changed)
        return imageLoad(FLOW_E_AB_CACHE, coord);

    vec2 uv_a = LUMA_A_E_pos;
    vec2 base_off = FLOW_S_AB_tex(snap_texel(uv_a, FLOW_S_AB_size)).xy * 2.0 * LUMA_A_E_pt;

    if (local_contrast_5x5_e(uv_a) < MIN_CONTRAST) {
        vec4 result = vec4(base_off / LUMA_A_E_pt, 0.0, 0.0);
        imageStore(FLOW_E_AB_CACHE, coord, result);
        return result;
    }

    // Search radius and bias against moving away from the inherited seed
    // -- see bidirectional-interpolation.glsl's E-level A->B pass for the
    // full reasoning.
    const int REFINE_SEARCH_RADIUS = 2;
    const float REFINE_REG_LAMBDA = 0.05;

    vec2 best_off = base_off;
    // See TIE_MARGIN in the coarse A->B search above.
    const float TIE_MARGIN = 1.0e-4;
    float best_cost = sad5x5_e(uv_a, uv_a + base_off);

    for (int y = -REFINE_SEARCH_RADIUS; y <= REFINE_SEARCH_RADIUS; y++) {
        for (int x = -REFINE_SEARCH_RADIUS; x <= REFINE_SEARCH_RADIUS; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 off = base_off + vec2(float(x), float(y)) * LUMA_A_E_pt;
            float cost = sad5x5_e(uv_a, uv_a + off)
                       + REFINE_REG_LAMBDA * length(vec2(float(x), float(y)));
            if (cost < best_cost * (1.0 - TIE_MARGIN)) {
                best_cost = cost;
                best_off = off;
            }
        }
    }
    vec4 result = vec4(best_off / LUMA_A_E_pt, 0.0, 0.0);
    imageStore(FLOW_E_AB_CACHE, coord, result);
    return result;
}

//!TEXTURE FLOW_E_BA_CACHE
//!SIZE 480 270
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_E_BA_CACHE
//!BIND LUMA_A_E
//!BIND LUMA_B_E
//!BIND FLOW_S_BA
//!SAVE FLOW_E_BA
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 2
//!DESC [debug] refine flow B->A (1/8 res)

// See snap_texel() in the A->B pass above.
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

// See COARSE_WINDOW_RADIUS in the A->B pass above.
const int COARSE_WINDOW_RADIUS = 1;

float sad5x5_e2(vec2 uv_b, vec2 uv_a) {
    float s = 0.0;
    for (int y = -COARSE_WINDOW_RADIUS; y <= COARSE_WINDOW_RADIUS; y++) {
        for (int x = -COARSE_WINDOW_RADIUS; x <= COARSE_WINDOW_RADIUS; x++) {
            vec2 o = vec2(float(x), float(y)) * LUMA_A_E_pt;
            s += abs(LUMA_B_E_tex(uv_b + o).r - LUMA_A_E_tex(uv_a + o).r);
        }
    }
    return s;
}

// See local_contrast_5x5_e()/MIN_CONTRAST in the A->B pass above.
// See the A->B pass above.
const float MIN_CONTRAST = 0.0;

float local_contrast_5x5_e2(vec2 uv_b) {
    float lo = 1.0, hi = 0.0;
    for (int y = -2; y <= 2; y++) {
        for (int x = -2; x <= 2; x++) {
            float v = LUMA_B_E_tex(uv_b + vec2(float(x), float(y)) * LUMA_A_E_pt).r;
            lo = min(lo, v);
            hi = max(hi, v);
        }
    }
    return hi - lo;
}

vec4 hook() {
    ivec2 coord = ivec2(LUMA_B_E_pos * LUMA_B_E_size);
    if (!pair_changed)
        return imageLoad(FLOW_E_BA_CACHE, coord);

    vec2 uv_b = LUMA_B_E_pos;
    vec2 base_off = FLOW_S_BA_tex(snap_texel(uv_b, FLOW_S_BA_size)).xy * 2.0 * LUMA_A_E_pt;

    if (local_contrast_5x5_e2(uv_b) < MIN_CONTRAST) {
        vec4 result = vec4(base_off / LUMA_A_E_pt, 0.0, 0.0);
        imageStore(FLOW_E_BA_CACHE, coord, result);
        return result;
    }

    // See REFINE_SEARCH_RADIUS/REFINE_REG_LAMBDA in the A->B pass above.
    const int REFINE_SEARCH_RADIUS = 2;
    const float REFINE_REG_LAMBDA = 0.05;

    vec2 best_off = base_off;
    // See TIE_MARGIN in the coarse A->B search above.
    const float TIE_MARGIN = 1.0e-4;
    float best_cost = sad5x5_e2(uv_b, uv_b + base_off);

    for (int y = -REFINE_SEARCH_RADIUS; y <= REFINE_SEARCH_RADIUS; y++) {
        for (int x = -REFINE_SEARCH_RADIUS; x <= REFINE_SEARCH_RADIUS; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 off = base_off + vec2(float(x), float(y)) * LUMA_A_E_pt;
            float cost = sad5x5_e2(uv_b, uv_b + off)
                       + REFINE_REG_LAMBDA * length(vec2(float(x), float(y)));
            if (cost < best_cost * (1.0 - TIE_MARGIN)) {
                best_cost = cost;
                best_off = off;
            }
        }
    }
    vec4 result = vec4(best_off / LUMA_A_E_pt, 0.0, 0.0);
    imageStore(FLOW_E_BA_CACHE, coord, result);
    return result;
}

//!HOOK FRAME_MIX
//!BIND HOOKED
//!SAVE LUMA_A_Q
//!WIDTH HOOKED.w 4 /
//!HEIGHT HOOKED.h 4 /
//!COMPONENTS 1
//!DESC [debug] downsample frame A to 1/4 res (luma)
vec4 hook() {
    return vec4(dot(HOOKED_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!HOOK FRAME_MIX
//!BIND NEXT
//!SAVE LUMA_B_Q
//!WIDTH HOOKED.w 4 /
//!HEIGHT HOOKED.h 4 /
//!COMPONENTS 1
//!DESC [debug] downsample frame B to 1/4 res (luma)
vec4 hook() {
    return vec4(dot(NEXT_tex(NEXT_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!TEXTURE FLOW_Q_AB_CACHE
//!SIZE 960 540
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_Q_AB_CACHE
//!BIND LUMA_A_Q
//!BIND LUMA_B_Q
//!BIND FLOW_E_AB
//!SAVE FLOW_Q_AB
//!WIDTH HOOKED.w 4 /
//!HEIGHT HOOKED.h 4 /
//!COMPONENTS 2
//!DESC [debug] refine flow A->B (1/4 res)

// Same seed-snapping fix, E->Q handoff -- see
// bidirectional-interpolation.glsl for the full reasoning.
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

// Same window-narrowing fix as the S/E levels' COARSE_WINDOW_RADIUS --
// see bidirectional-interpolation.glsl for the full reasoning.
const int COARSE_WINDOW_RADIUS = 1;

float sad5x5_q(vec2 uv_a, vec2 uv_b) {
    float s = 0.0;
    for (int y = -COARSE_WINDOW_RADIUS; y <= COARSE_WINDOW_RADIUS; y++) {
        for (int x = -COARSE_WINDOW_RADIUS; x <= COARSE_WINDOW_RADIUS; x++) {
            vec2 o = vec2(float(x), float(y)) * LUMA_A_Q_pt;
            s += abs(LUMA_A_Q_tex(uv_a + o).r - LUMA_B_Q_tex(uv_b + o).r);
        }
    }
    return s;
}

// See local_contrast_5x5_e()/MIN_CONTRAST in the 1/8-res A->B pass.
// See the E-level A->B pass for the full reasoning.
const float MIN_CONTRAST = 0.0;

float local_contrast_5x5_q(vec2 uv_a) {
    float lo = 1.0, hi = 0.0;
    for (int y = -2; y <= 2; y++) {
        for (int x = -2; x <= 2; x++) {
            float v = LUMA_A_Q_tex(uv_a + vec2(float(x), float(y)) * LUMA_A_Q_pt).r;
            lo = min(lo, v);
            hi = max(hi, v);
        }
    }
    return hi - lo;
}

vec4 hook() {
    ivec2 coord = ivec2(LUMA_A_Q_pos * LUMA_A_Q_size);
    if (!pair_changed)
        return imageLoad(FLOW_Q_AB_CACHE, coord);

    vec2 uv_a = LUMA_A_Q_pos;
    vec2 base_off = FLOW_E_AB_tex(snap_texel(uv_a, FLOW_E_AB_size)).xy * 2.0 * LUMA_A_Q_pt;

    if (local_contrast_5x5_q(uv_a) < MIN_CONTRAST) {
        vec4 result = vec4(base_off / LUMA_A_Q_pt, 0.0, 0.0);
        imageStore(FLOW_Q_AB_CACHE, coord, result);
        return result;
    }

    // Same refine-level search radius and regularization as the E level
    // above -- see bidirectional-interpolation.glsl's E-level A->B pass for
    // the full reasoning.
    const int REFINE_SEARCH_RADIUS = 2;
    const float REFINE_REG_LAMBDA = 0.05;

    vec2 best_off = base_off;
    // See TIE_MARGIN in the coarse A->B search above.
    const float TIE_MARGIN = 1.0e-4;
    float best_cost = sad5x5_q(uv_a, uv_a + base_off);

    for (int y = -REFINE_SEARCH_RADIUS; y <= REFINE_SEARCH_RADIUS; y++) {
        for (int x = -REFINE_SEARCH_RADIUS; x <= REFINE_SEARCH_RADIUS; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 off = base_off + vec2(float(x), float(y)) * LUMA_A_Q_pt;
            float cost = sad5x5_q(uv_a, uv_a + off)
                       + REFINE_REG_LAMBDA * length(vec2(float(x), float(y)));
            if (cost < best_cost * (1.0 - TIE_MARGIN)) {
                best_cost = cost;
                best_off = off;
            }
        }
    }
    vec4 result = vec4(best_off / LUMA_A_Q_pt, 0.0, 0.0);
    imageStore(FLOW_Q_AB_CACHE, coord, result);
    return result;
}

//!TEXTURE FLOW_Q_BA_CACHE
//!SIZE 960 540
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_Q_BA_CACHE
//!BIND LUMA_A_Q
//!BIND LUMA_B_Q
//!BIND FLOW_E_BA
//!SAVE FLOW_Q_BA
//!WIDTH HOOKED.w 4 /
//!HEIGHT HOOKED.h 4 /
//!COMPONENTS 2
//!DESC [debug] refine flow B->A (1/4 res)

// See snap_texel() in the A->B pass above.
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

// See COARSE_WINDOW_RADIUS in the A->B pass above.
const int COARSE_WINDOW_RADIUS = 1;

float sad5x5_q2(vec2 uv_b, vec2 uv_a) {
    float s = 0.0;
    for (int y = -COARSE_WINDOW_RADIUS; y <= COARSE_WINDOW_RADIUS; y++) {
        for (int x = -COARSE_WINDOW_RADIUS; x <= COARSE_WINDOW_RADIUS; x++) {
            vec2 o = vec2(float(x), float(y)) * LUMA_A_Q_pt;
            s += abs(LUMA_B_Q_tex(uv_b + o).r - LUMA_A_Q_tex(uv_a + o).r);
        }
    }
    return s;
}

// See local_contrast_5x5_e()/MIN_CONTRAST in the 1/8-res A->B pass.
// See the E-level A->B pass for the full reasoning.
const float MIN_CONTRAST = 0.0;

float local_contrast_5x5_q2(vec2 uv_b) {
    float lo = 1.0, hi = 0.0;
    for (int y = -2; y <= 2; y++) {
        for (int x = -2; x <= 2; x++) {
            float v = LUMA_B_Q_tex(uv_b + vec2(float(x), float(y)) * LUMA_A_Q_pt).r;
            lo = min(lo, v);
            hi = max(hi, v);
        }
    }
    return hi - lo;
}

vec4 hook() {
    ivec2 coord = ivec2(LUMA_B_Q_pos * LUMA_B_Q_size);
    if (!pair_changed)
        return imageLoad(FLOW_Q_BA_CACHE, coord);

    vec2 uv_b = LUMA_B_Q_pos;
    vec2 base_off = FLOW_E_BA_tex(snap_texel(uv_b, FLOW_E_BA_size)).xy * 2.0 * LUMA_A_Q_pt;

    if (local_contrast_5x5_q2(uv_b) < MIN_CONTRAST) {
        vec4 result = vec4(base_off / LUMA_A_Q_pt, 0.0, 0.0);
        imageStore(FLOW_Q_BA_CACHE, coord, result);
        return result;
    }

    // See REFINE_SEARCH_RADIUS/REFINE_REG_LAMBDA in the A->B pass above.
    const int REFINE_SEARCH_RADIUS = 2;
    const float REFINE_REG_LAMBDA = 0.05;

    vec2 best_off = base_off;
    // See TIE_MARGIN in the coarse A->B search above.
    const float TIE_MARGIN = 1.0e-4;
    float best_cost = sad5x5_q2(uv_b, uv_b + base_off);

    for (int y = -REFINE_SEARCH_RADIUS; y <= REFINE_SEARCH_RADIUS; y++) {
        for (int x = -REFINE_SEARCH_RADIUS; x <= REFINE_SEARCH_RADIUS; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 off = base_off + vec2(float(x), float(y)) * LUMA_A_Q_pt;
            float cost = sad5x5_q2(uv_b, uv_b + off)
                       + REFINE_REG_LAMBDA * length(vec2(float(x), float(y)));
            if (cost < best_cost * (1.0 - TIE_MARGIN)) {
                best_cost = cost;
                best_off = off;
            }
        }
    }
    vec4 result = vec4(best_off / LUMA_A_Q_pt, 0.0, 0.0);
    imageStore(FLOW_Q_BA_CACHE, coord, result);
    return result;
}

//!HOOK FRAME_MIX
//!BIND HOOKED
//!SAVE LUMA_A_H
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 1
//!DESC [debug] downsample frame A to half res (luma)
vec4 hook() {
    return vec4(dot(HOOKED_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!HOOK FRAME_MIX
//!BIND NEXT
//!SAVE LUMA_B_H
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 1
//!DESC [debug] downsample frame B to half res (luma)
vec4 hook() {
    return vec4(dot(NEXT_tex(NEXT_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!TEXTURE FLOW_H_AB_CACHE
//!SIZE 1920 1080
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_H_AB_CACHE
//!BIND LUMA_A_H
//!BIND LUMA_B_H
//!BIND FLOW_Q_AB
//!SAVE FLOW_H_AB
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 2
//!DESC [debug] refine flow A->B (half res)

// Same seed-snapping fix, Q->H handoff -- see
// bidirectional-interpolation.glsl for the full reasoning.
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

float sad3x3_h(vec2 uv_a, vec2 uv_b) {
    float s = 0.0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 o = vec2(float(x), float(y)) * LUMA_A_H_pt;
            s += abs(LUMA_A_H_tex(uv_a + o).r - LUMA_B_H_tex(uv_b + o).r);
        }
    }
    return s;
}

// See local_contrast_5x5_e()/MIN_CONTRAST in the 1/8-res A->B pass --
// same reasoning, over the 3x3 window this level's own SAD uses.
// See the E-level A->B pass for the full reasoning.
const float MIN_CONTRAST = 0.0;

float local_contrast_3x3_h(vec2 uv_a) {
    float lo = 1.0, hi = 0.0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            float v = LUMA_A_H_tex(uv_a + vec2(float(x), float(y)) * LUMA_A_H_pt).r;
            lo = min(lo, v);
            hi = max(hi, v);
        }
    }
    return hi - lo;
}

vec4 hook() {
    ivec2 coord = ivec2(LUMA_A_H_pos * LUMA_A_H_size);
    if (!pair_changed)
        return imageLoad(FLOW_H_AB_CACHE, coord);

    vec2 uv_a = LUMA_A_H_pos;
    vec2 base_off = FLOW_Q_AB_tex(snap_texel(uv_a, FLOW_Q_AB_size)).xy * 2.0 * LUMA_A_H_pt;

    if (local_contrast_3x3_h(uv_a) < MIN_CONTRAST) {
        vec4 result = vec4(base_off / LUMA_A_H_pt, 0.0, 0.0);
        imageStore(FLOW_H_AB_CACHE, coord, result);
        return result;
    }

    // Same refine-level search radius and regularization as the E/Q
    // levels above -- see bidirectional-interpolation.glsl's E-level A->B
    // pass for the full reasoning.
    const int REFINE_SEARCH_RADIUS = 2;
    const float REFINE_REG_LAMBDA = 0.05;

    vec2 best_off = base_off;
    // See TIE_MARGIN in the coarse A->B search above.
    const float TIE_MARGIN = 1.0e-4;
    float best_cost = sad3x3_h(uv_a, uv_a + base_off);

    for (int y = -REFINE_SEARCH_RADIUS; y <= REFINE_SEARCH_RADIUS; y++) {
        for (int x = -REFINE_SEARCH_RADIUS; x <= REFINE_SEARCH_RADIUS; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 off = base_off + vec2(float(x), float(y)) * LUMA_A_H_pt;
            float cost = sad3x3_h(uv_a, uv_a + off)
                       + REFINE_REG_LAMBDA * length(vec2(float(x), float(y)));
            if (cost < best_cost * (1.0 - TIE_MARGIN)) {
                best_cost = cost;
                best_off = off;
            }
        }
    }
    vec4 result = vec4(best_off / LUMA_A_H_pt, 0.0, 0.0);
    imageStore(FLOW_H_AB_CACHE, coord, result);
    return result;
}

//!TEXTURE FLOW_H_BA_CACHE
//!SIZE 1920 1080
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_H_BA_CACHE
//!BIND LUMA_A_H
//!BIND LUMA_B_H
//!BIND FLOW_Q_BA
//!SAVE FLOW_H_BA
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 2
//!DESC [debug] refine flow B->A (half res)

// See snap_texel() in the A->B pass above.
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

float sad3x3_h2(vec2 uv_b, vec2 uv_a) {
    float s = 0.0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 o = vec2(float(x), float(y)) * LUMA_A_H_pt;
            s += abs(LUMA_B_H_tex(uv_b + o).r - LUMA_A_H_tex(uv_a + o).r);
        }
    }
    return s;
}

// See local_contrast_5x5_e()/MIN_CONTRAST in the 1/8-res A->B pass.
// See the E-level A->B pass for the full reasoning.
const float MIN_CONTRAST = 0.0;

float local_contrast_3x3_h2(vec2 uv_b) {
    float lo = 1.0, hi = 0.0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            float v = LUMA_B_H_tex(uv_b + vec2(float(x), float(y)) * LUMA_A_H_pt).r;
            lo = min(lo, v);
            hi = max(hi, v);
        }
    }
    return hi - lo;
}

vec4 hook() {
    ivec2 coord = ivec2(LUMA_B_H_pos * LUMA_B_H_size);
    if (!pair_changed)
        return imageLoad(FLOW_H_BA_CACHE, coord);

    vec2 uv_b = LUMA_B_H_pos;
    vec2 base_off = FLOW_Q_BA_tex(snap_texel(uv_b, FLOW_Q_BA_size)).xy * 2.0 * LUMA_A_H_pt;

    if (local_contrast_3x3_h2(uv_b) < MIN_CONTRAST) {
        vec4 result = vec4(base_off / LUMA_A_H_pt, 0.0, 0.0);
        imageStore(FLOW_H_BA_CACHE, coord, result);
        return result;
    }

    // See REFINE_SEARCH_RADIUS/REFINE_REG_LAMBDA in the A->B pass above.
    const int REFINE_SEARCH_RADIUS = 2;
    const float REFINE_REG_LAMBDA = 0.05;

    vec2 best_off = base_off;
    // See TIE_MARGIN in the coarse A->B search above.
    const float TIE_MARGIN = 1.0e-4;
    float best_cost = sad3x3_h2(uv_b, uv_b + base_off);

    for (int y = -REFINE_SEARCH_RADIUS; y <= REFINE_SEARCH_RADIUS; y++) {
        for (int x = -REFINE_SEARCH_RADIUS; x <= REFINE_SEARCH_RADIUS; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 off = base_off + vec2(float(x), float(y)) * LUMA_A_H_pt;
            float cost = sad3x3_h2(uv_b, uv_b + off)
                       + REFINE_REG_LAMBDA * length(vec2(float(x), float(y)));
            if (cost < best_cost * (1.0 - TIE_MARGIN)) {
                best_cost = cost;
                best_off = off;
            }
        }
    }
    vec4 result = vec4(best_off / LUMA_A_H_pt, 0.0, 0.0);
    imageStore(FLOW_H_BA_CACHE, coord, result);
    return result;
}

// ---------------------------------------------------------------------
// Vector median filter on both flow fields (x2 passes each -- see
// bidirectional-interpolation.glsl for why two passes)
// ---------------------------------------------------------------------
// Pass 1's result only ever feeds pass 2 within this same dispatch, so it
// has no cache of its own -- on a cache hit it returns a cheap dummy that
// pass 2 will never look at, skipping the real 9x9-comparison cost.
//!HOOK FRAME_MIX
//!BIND FLOW_H_AB
//!SAVE FLOW_H_AB
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 2
//!DESC [debug] vector median filter on flow A->B (pass 1)
vec4 hook() {
    if (!pair_changed)
        return vec4(0.0);

    vec2 v[9];
    int n = 0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 o = vec2(float(x), float(y)) * FLOW_H_AB_pt;
            v[n++] = FLOW_H_AB_tex(FLOW_H_AB_pos + o).xy;
        }
    }

    // Deterministic tie-breaking, same mechanism and same reasoning as the
    // block match's TIE_MARGIN -- see the coarse A->B search above. It matters
    // here for the same reason: nine candidate vectors, and where several of
    // them agree the totals are near-tied, so without a margin the median's
    // choice between two disagreeing clusters of equal size can be decided by
    // rounding. The incumbent is the first candidate in a fixed scan order.
    const float TIE_MARGIN = 1.0e-4;
    float best_cost = 1e30;
    vec2 best = v[4];
    for (int i = 0; i < 9; i++) {
        float cost = 0.0;
        for (int j = 0; j < 9; j++)
            cost += length(v[i] - v[j]);
        if (cost < best_cost * (1.0 - TIE_MARGIN)) {
            best_cost = cost;
            best = v[i];
        }
    }

    return vec4(best, 0.0, 0.0);
}

// This one's result is what the final warp actually reads, so it gets a
// real persistent cache (unlike pass 1 above).
//!TEXTURE FLOW_H_AB_MEDIAN_CACHE
//!SIZE 1920 1080
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_H_AB_MEDIAN_CACHE
//!BIND FLOW_H_AB
//!SAVE FLOW_H_AB
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 2
//!DESC [debug] vector median filter on flow A->B (pass 2)
vec4 hook() {
    ivec2 coord = ivec2(FLOW_H_AB_pos * FLOW_H_AB_size);
    if (!pair_changed)
        return imageLoad(FLOW_H_AB_MEDIAN_CACHE, coord);

    vec2 v[9];
    int n = 0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 o = vec2(float(x), float(y)) * FLOW_H_AB_pt;
            v[n++] = FLOW_H_AB_tex(FLOW_H_AB_pos + o).xy;
        }
    }

    // See TIE_MARGIN in the coarse A->B search above.
    const float TIE_MARGIN = 1.0e-4;
    float best_cost = 1e30;
    vec2 best = v[4];
    for (int i = 0; i < 9; i++) {
        float cost = 0.0;
        for (int j = 0; j < 9; j++)
            cost += length(v[i] - v[j]);
        if (cost < best_cost * (1.0 - TIE_MARGIN)) {
            best_cost = cost;
            best = v[i];
        }
    }

    vec4 result = vec4(best, 0.0, 0.0);
    imageStore(FLOW_H_AB_MEDIAN_CACHE, coord, result);
    return result;
}

//!HOOK FRAME_MIX
//!BIND FLOW_H_BA
//!SAVE FLOW_H_BA
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 2
//!DESC [debug] vector median filter on flow B->A (pass 1)
vec4 hook() {
    if (!pair_changed)
        return vec4(0.0);

    vec2 v[9];
    int n = 0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 o = vec2(float(x), float(y)) * FLOW_H_BA_pt;
            v[n++] = FLOW_H_BA_tex(FLOW_H_BA_pos + o).xy;
        }
    }

    // See TIE_MARGIN in the coarse A->B search above.
    const float TIE_MARGIN = 1.0e-4;
    float best_cost = 1e30;
    vec2 best = v[4];
    for (int i = 0; i < 9; i++) {
        float cost = 0.0;
        for (int j = 0; j < 9; j++)
            cost += length(v[i] - v[j]);
        if (cost < best_cost * (1.0 - TIE_MARGIN)) {
            best_cost = cost;
            best = v[i];
        }
    }

    return vec4(best, 0.0, 0.0);
}

// This one's result is what the final warp actually reads, so it gets a
// real persistent cache (unlike pass 1 above).
//!TEXTURE FLOW_H_BA_MEDIAN_CACHE
//!SIZE 1920 1080
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_H_BA_MEDIAN_CACHE
//!BIND FLOW_H_BA
//!SAVE FLOW_H_BA
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 2
//!DESC [debug] vector median filter on flow B->A (pass 2)
vec4 hook() {
    ivec2 coord = ivec2(FLOW_H_BA_pos * FLOW_H_BA_size);
    if (!pair_changed)
        return imageLoad(FLOW_H_BA_MEDIAN_CACHE, coord);

    vec2 v[9];
    int n = 0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 o = vec2(float(x), float(y)) * FLOW_H_BA_pt;
            v[n++] = FLOW_H_BA_tex(FLOW_H_BA_pos + o).xy;
        }
    }

    // See TIE_MARGIN in the coarse A->B search above.
    const float TIE_MARGIN = 1.0e-4;
    float best_cost = 1e30;
    vec2 best = v[4];
    for (int i = 0; i < 9; i++) {
        float cost = 0.0;
        for (int j = 0; j < 9; j++)
            cost += length(v[i] - v[j]);
        if (cost < best_cost * (1.0 - TIE_MARGIN)) {
            best_cost = cost;
            best = v[i];
        }
    }

    vec4 result = vec4(best, 0.0, 0.0);
    imageStore(FLOW_H_BA_MEDIAN_CACHE, coord, result);
    return result;
}

// ---------------------------------------------------------------------
// Edge-consistency reference (see warp_sample_a/b below for how this gets
// used): per-frame motion-gated spatial edge masks, full resolution, one
// per source frame. Identical to bidirectional-interpolation.glsl's EDGE_A/
// EDGE_B passes -- kept in lockstep for the same reason the rest of this
// file's pyramid is.
// ---------------------------------------------------------------------
//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND NEXT
//!SAVE EDGE_A
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!COMPONENTS 1
//!DESC [debug] motion-gated spatial edge mask (frame A)

const float MOTION_THRESHOLD = 0.08;
const float SPATIAL_EDGE_THRESHOLD = 0.1;

float luma(vec4 c) {
    return dot(c.rgb, vec3(0.299, 0.587, 0.114));
}

bool moving(vec2 pos) {
    return abs(luma(HOOKED_tex(pos)) - luma(NEXT_tex(pos))) > MOTION_THRESHOLD;
}

bool spatial_edge_a(vec2 pos) {
    float center = luma(HOOKED_tex(pos));
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 o = vec2(float(x), float(y)) * HOOKED_pt;
            if (abs(luma(HOOKED_tex(pos + o)) - center) > SPATIAL_EDGE_THRESHOLD)
                return true;
        }
    }
    return false;
}

vec4 hook() {
    bool edge = moving(HOOKED_pos) && spatial_edge_a(HOOKED_pos);
    return vec4(edge ? 1.0 : 0.0, 0.0, 0.0, 0.0);
}

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND NEXT
//!SAVE EDGE_B
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!COMPONENTS 1
//!DESC [debug] motion-gated spatial edge mask (frame B)

const float MOTION_THRESHOLD = 0.08;
const float SPATIAL_EDGE_THRESHOLD = 0.1;

float luma(vec4 c) {
    return dot(c.rgb, vec3(0.299, 0.587, 0.114));
}

bool moving(vec2 pos) {
    return abs(luma(HOOKED_tex(pos)) - luma(NEXT_tex(pos))) > MOTION_THRESHOLD;
}

bool spatial_edge_b(vec2 pos) {
    float center = luma(NEXT_tex(pos));
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 o = vec2(float(x), float(y)) * HOOKED_pt;
            if (abs(luma(NEXT_tex(pos + o)) - center) > SPATIAL_EDGE_THRESHOLD)
                return true;
        }
    }
    return false;
}

vec4 hook() {
    bool edge = moving(HOOKED_pos) && spatial_edge_b(HOOKED_pos);
    return vec4(edge ? 1.0 : 0.0, 0.0, 0.0, 0.0);
}

// ---------------------------------------------------------------------
// Final pass: 3x2 diagnostic grid instead of the real warp/blend output
// ---------------------------------------------------------------------
//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND NEXT
//!BIND FLOW_H_AB
//!BIND FLOW_H_BA
//!BIND EDGE_A
//!BIND EDGE_B
//!SAVE FRAME_MIX
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!DESC [debug] 3x2 diagnostic grid (A / B / flow color / magnitude / occlusion / warp)

vec3 hsv2rgb(vec3 c) {
    vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
    return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
}

const float MAX_PX = 30.0; // clamp/normalization ceiling, in full-res pixels

vec3 flow_to_color(vec2 flow_px) {
    float mag = length(flow_px);
    if (mag > MAX_PX)
        return vec3(1.0, 0.0, 1.0); // magenta = off-scale, likely a real bug
    float angle = atan(flow_px.y, flow_px.x); // -pi..pi
    float hue = angle / (2.0 * 3.14159265) + 0.5;
    float val = clamp(mag / MAX_PX, 0.0, 1.0);
    return hsv2rgb(vec3(hue, 1.0, val));
}

vec3 magnitude_to_color(vec2 flow_px) {
    float mag = length(flow_px);
    if (mag > MAX_PX)
        return vec3(1.0, 0.0, 1.0);
    return vec3(mag / MAX_PX);
}

// Same forward/backward consistency check as the bottom-middle occlusion
// cell and the production shader's fallback decision, but as a standalone
// probe usable from anywhere (the fallback indicator samples it at a grid
// of points across the whole frame, not just the current output pixel).
float sample_occlusion(vec2 local) {
    vec2 flow_ab = FLOW_H_AB_tex(local).xy * 2.0 * HOOKED_pt;
    vec2 fb_at_b = FLOW_H_BA_tex(local + flow_ab).xy * 2.0 * HOOKED_pt;
    vec2 round_trip = flow_ab + fb_at_b;
    float fb_error_px = length(round_trip) / HOOKED_pt.x;
    return smoothstep(20.0, 30.0, fb_error_px);
}

// Amplifies the frame-average occlusion before colorizing the fallback
// indicator: a genuinely occluded region (e.g. a moving character) is
// usually a small fraction of total frame area, so the raw average stays
// near-black even when that region is fully faded. Tune this up if the
// indicator feels too dim on content you know is falling back, or down
// if it's flashing red on frames that only have trivial edge occlusion.
const float FALLBACK_INDICATOR_GAIN = 4.0;

vec3 fallback_indicator_color(float avg_occluded) {
    float t = clamp(avg_occluded * FALLBACK_INDICATOR_GAIN, 0.0, 1.0);
    vec3 low = vec3(0.0, 0.0, 0.0);  // black: this frame trusts the warp
    vec3 mid = vec3(1.0, 1.0, 0.0);  // yellow: partial fallback
    vec3 high = vec3(1.0, 0.0, 0.0); // red: mostly faded, not interpolated
    return t < 0.5 ? mix(low, mid, t * 2.0) : mix(mid, high, (t - 0.5) * 2.0);
}

// See bidirectional-interpolation.glsl for why: snapping to the nearest
// source texel center before sampling makes linear filtering degenerate
// to nearest-neighbor, avoiding the blur a fractional-position sample
// would otherwise introduce.
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

// See bidirectional-interpolation.glsl's identical constant/helpers for the
// full reasoning: snap_texel() is a discontinuous function of the warp
// position, and even a clean, low-noise flow field has enough sub-texel
// imprecision to fragment thin, high-contrast linework (confirmed on
// real footage: cartoon outlines breaking up against the background).
// EDGE_A/EDGE_B (above) give a per-pixel check on whether the snap
// actually landed where a moving edge was expected -- agreement trusts
// the snap fully, disagreement (the coin-flip case that fragments a
// line) falls back toward bilinear just for that sample. Kept identical
// to the production shader's mechanism so this diagnostic's "actual
// warped result" cell stays representative of what that shader really
// produces.
float edge_consistency(float expected, float snapped) {
    return 1.0 - abs(expected - snapped);
}

// TESTING at 0.0 (was 1.0), disabling the snap mechanism entirely --
// see bidirectional-interpolation.glsl for the full reasoning: real-
// hardware isolation found the reported defect already present in
// warp_sample_a/b's own output alone, implicating edge_consistency()
// trusting the snap fully in ordinary non-edge content too, not just
// genuine hard edges. Not yet confirmed either way.
const float SNAP_STRENGTH = 0.0;

vec4 warp_sample_a(vec2 uv) {
    vec2 snapped_uv = snap_texel(uv, HOOKED_size);
    float expected = EDGE_A_tex(uv).r;
    float snapped_edge = EDGE_A_tex(snapped_uv).r;
    float strength = SNAP_STRENGTH * edge_consistency(expected, snapped_edge);
    return mix(HOOKED_tex(uv), HOOKED_tex(snapped_uv), strength);
}

vec4 warp_sample_b(vec2 uv) {
    vec2 snapped_uv = snap_texel(uv, NEXT_size);
    float expected = EDGE_B_tex(uv).r;
    float snapped_edge = EDGE_B_tex(snapped_uv).r;
    float strength = SNAP_STRENGTH * edge_consistency(expected, snapped_edge);
    return mix(NEXT_tex(uv), NEXT_tex(snapped_uv), strength);
}

// Layout (3 columns x 2 rows -- each cell shows the full frame, scaled down):
//   +------------+------------+------------+
//   |  source A  |  source B  | flow color |
//   +------------+------------+------------+
//   | flow magni-| occlusion  |  actual    |
//   | tude heat- | mask       |  warped    |
//   | map        |            |  result    |
//   +------------+------------+------------+
vec4 hook() {
    vec2 uv = HOOKED_pos;                          // 0..1 over the full output frame
    vec2 cell = floor(uv * vec2(3.0, 2.0));        // cell.x in {0,1,2}, cell.y in {0,1}
    vec2 local = fract(uv * vec2(3.0, 2.0));       // 0..1 within the selected cell

    vec2 flow_ab_px = FLOW_H_AB_tex(local).xy * 2.0;

    if (cell.y < 0.5) {
        // Top row
        if (cell.x < 0.5)
            return HOOKED_tex(local);                  // source A, unmodified
        if (cell.x < 1.5)
            return NEXT_tex(local);                    // source B, unmodified

        // Cache-hit indicator: a small corner square on the flow-color
        // cell, RED when this frame recomputed the flow (pair_changed),
        // GREEN when it was served from the storage cache instead. On
        // a working cache with e.g. a 2.5x fps ratio, this should flash
        // red roughly 2 frames out of every 5 and green the rest -- solid
        // red every frame means the cache isn't engaging at all.
        if (local.x < 0.06 && local.y < 0.06)
            return pair_changed ? vec4(1.0, 0.0, 0.0, 1.0) : vec4(0.0, 1.0, 0.0, 1.0);

        // Fallback indicator: mirrors the cache box above but in the
        // opposite corner, showing how much of THIS frame is fading to
        // an unwarped source frame instead of being genuinely motion-
        // compensated -- see the [F] note in the header for the color
        // scale. Only evaluated for the handful of output pixels that
        // land inside this small corner square.
        if (local.x > 0.94 && local.y < 0.06) {
            const int N = 5;
            float total = 0.0;
            for (int gy = 0; gy < N; gy++) {
                for (int gx = 0; gx < N; gx++) {
                    vec2 sample_uv = (vec2(gx, gy) + 0.5) / float(N);
                    total += sample_occlusion(sample_uv);
                }
            }
            float avg_occluded = total / float(N * N);
            return vec4(fallback_indicator_color(avg_occluded), 1.0);
        }

        return vec4(flow_to_color(flow_ab_px), 1.0);   // flow color wheel (A->B)
    }

    // Bottom row
    if (cell.x < 0.5)
        return vec4(magnitude_to_color(flow_ab_px), 1.0); // flow magnitude heatmap (A->B)

    vec2 flow_ab = flow_ab_px * HOOKED_pt;

    // Forward/backward consistency: same check as the production shader.
    vec2 fb_at_b = FLOW_H_BA_tex(local + flow_ab).xy * 2.0 * HOOKED_pt;
    vec2 round_trip = flow_ab + fb_at_b;
    float fb_error_px = length(round_trip) / HOOKED_pt.x;
    float occluded = smoothstep(20.0, 30.0, fb_error_px);

    vec4 warped_a = warp_sample_a(local - flow_ab * mix_t);
    vec4 warped_b = warp_sample_b(local + flow_ab * (1.0 - mix_t));
    vec4 mc_result = mix(warped_a, warped_b, mix_t);

    if (cell.x < 1.5)
        return vec4(vec3(occluded), 1.0); // forward/backward inconsistency:
                                          // white = the two flow fields
                                          // disagree here, usually genuine
                                          // occlusion. PURELY INFORMATIONAL
                                          // now -- see below.

    // Actual result from the normal algorithm. Nothing acts on the mask
    // above any more: bidirectional-interpolation.glsl's occlusion fallback
    // was removed after three versions of it each measured worse than none
    // (a hard mix_t switch produced an 8.75x periodic jump; a continuous
    // blend of two unwarped frames produced a translucent doubled contour at
    // every moving edge; directional per-side weighting was better but still
    // worse than removing it), confirmed by direct viewing. The mask is kept
    // because seeing WHERE consistency fails remains diagnostically useful.
    return mc_result;
}
