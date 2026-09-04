// =====================================================================
// GENERATED FILE -- DO NOT EDIT BY HAND.
//
// Produced by scripts/tests/gen_tridirectional.py from
// bidirectional-interpolation.glsl. Edit the base (shared machinery) or
// the generator (everything [tri]-tagged) and regenerate:
//
//   ./tests/gen_tridirectional.py
//
// TRIDIRECTIONAL INTERPOLATION -- the experiment this file exists for.
// A 2-frame shader can only encode constant velocity, so it places an
// inserted frame's content at the constant-velocity midpoint -- wrong by
// a/8 px under acceleration a. This shader binds THREE frames (the
// straddling pair plus the temporally nearest outer frame), estimates a
// third flow field from the anchor to that outer frame, solves per-texel
// acceleration from the anchor's two outgoing flows, and places content
// on the quadratic trajectory instead of the straight line. With zero
// estimated acceleration it degenerates exactly to the bidirectional
// shader. Hypothesis, algebra, calibration and results: TRIDIRECTIONAL.md.
// Everything below this banner up to the [tri]-tagged passes is the
// bidirectional base, transformed only in how it reads its source frames.
// =====================================================================

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!SAVE LUMA_A_S
//!WIDTH HOOKED.w 16 /
//!HEIGHT HOOKED.h 16 /
//!COMPONENTS 1
//!DESC [tri] downsample slot 0 to 1/16 res (luma)
vec4 hook() {
    return vec4(dot(HOOKED_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!SAVE LUMA_B_S
//!WIDTH HOOKED.w 16 /
//!HEIGHT HOOKED.h 16 /
//!COMPONENTS 1
//!DESC [tri] downsample slot 1 to 1/16 res (luma)
vec4 hook() {
    return vec4(dot(FRAME1_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!SAVE LUMA_C_S
//!WIDTH HOOKED.w 16 /
//!HEIGHT HOOKED.h 16 /
//!COMPONENTS 1
//!DESC [tri] downsample slot 2 to 1/16 res (luma)
vec4 hook() {
    return vec4(dot(FRAME2_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}


// ---------------------------------------------------------------------
// SCENE-CUT GATE: mean |A - B| over the whole frame, as a single number.
//
// WHAT IT IS FOR. Across a hard cut the two source frames are unrelated
// images. There is no correspondence to find and no motion to compensate, so
// interpolating between them superimposes two different shots -- a ghosted
// double exposure lasting two or three output frames. Found on real footage:
// a cut from a wide two-shot to a close-up rendered both at once, with the
// close-up's detail bleeding through the wide shot.
//
// Stock libplacebo's builtin mixers do this too, visibly worse. Gating it
// here makes this shader strictly better than the builtin blend rather than
// merely different.
//
// WHY A HARD SWITCH IS RIGHT HERE, when it was wrong for occlusion. The
// occlusion fallback was removed because at an occlusion boundary
// correspondence DOES exist for most of the frame, so substituting an
// unwarped frame threw away good information and produced a doubled contour.
// At a cut nothing corresponds, and the original edit was itself a hard
// switch: reproducing it is the correct output, not an approximation to it.
//
// WHAT THE STATISTIC ACTUALLY MEASURES, stated honestly: not "is there a
// cut", but "are these two frames too different to blend". Those are not the
// same thing and the difference matters. Measured across three very different
// clips (13081 frame pairs: a dark night scene, bright fast action, and flat
// animation), cuts between visually SIMILAR shots score no higher than
// ordinary fast motion -- and interpolating across those does no visible
// harm, which is why a 60-second clip containing eleven such cuts was viewed
// as defect-free. The gate fires on the cases that look wrong, which is the
// useful behaviour even though it is not cut detection.
//
// Two other statistics were tried and measured worse. The FRACTION of the
// frame that changed beyond a per-pixel threshold is diluted by grain in dark
// material. The ratio of post-warp residual to raw difference sounds better
// -- it asks how much of the change motion explains -- but the coarse flow
// explains too little at 1/16 resolution for the ratio to separate anything;
// non-cut pairs sat at 0.77 against cuts at 0.85.
//
// Sampled on a sparse fixed grid rather than every texel: this is a global
// statistic, so a few hundred samples is ample, and the sample count is the
// whole cost of a pass that runs as a single invocation.
// ---------------------------------------------------------------------
//!HOOK FRAME_MIX
//!BIND LUMA_A_S
//!BIND LUMA_B_S
//!SAVE SCENE_DIFF
//!WIDTH 1
//!HEIGHT 1
//!COMPONENTS 1
//!DESC [tri] scene-cut statistic, slots 0-1
vec4 hook() {
    const int N = 24;
    float acc = 0.0;
    for (int y = 0; y < N; y++) {
        for (int x = 0; x < N; x++) {
            vec2 uv = (vec2(float(x), float(y)) + 0.5) / float(N);
            acc += abs(LUMA_A_S_tex(uv).r - LUMA_B_S_tex(uv).r);
        }
    }
    return vec4(acc / float(N * N), 0.0, 0.0, 0.0);
}

//!HOOK FRAME_MIX
//!BIND LUMA_B_S
//!BIND LUMA_C_S
//!SAVE SCENE_DIFF_BC
//!WIDTH 1
//!HEIGHT 1
//!COMPONENTS 1
//!DESC [tri] scene-cut statistic, slots 1-2
vec4 hook() {
    const int N = 24;
    float acc = 0.0;
    for (int y = 0; y < N; y++) {
        for (int x = 0; x < N; x++) {
            vec2 uv = (vec2(float(x), float(y)) + 0.5) / float(N);
            acc += abs(LUMA_B_S_tex(uv).r - LUMA_C_S_tex(uv).r);
        }
    }
    return vec4(acc / float(N * N), 0.0, 0.0, 0.0);
}

// ---------------------------------------------------------------------
// Sixteenth-res coarse search, both directions: 5-step, 5x5 SAD window.
// Cached across repeated output frames sharing the same source pair --
// see the "Storage-based flow caching" note at the top of this file.
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
//!DESC [high] coarse flow search A->B (1/16 res)

// Matching-window radius for the coarse SAD cost below, independent of
// local_contrast_5x5_s()'s own fixed window further down (that one only
// checks whether there's enough texture here to trust a match at all,
// not how wide a match window to use). RE-TESTING at 1 (3x3, 48px
// footprint, down from the original 5x5/80px). First tried before the
// coarse-to-fine seed-snapping fix existed (see snap_texel() in the
// refine passes below) and came back pixel-identical -- but real-
// hardware testing after that fix confirmed the previously-smooth
// "nebulous cloud" is actually a sharp-edged grid of ~16px blocks,
// exactly this level's own native texel size (1/16 res), now visible
// because the seed-snapping fix stopped smoothing it away. That means
// the earlier null result may have been confounded by the very
// smoothing this level's output was passing through at the time, not a
// clean test of window size on its own. Re-testing now that the signal
// is no longer masked -- not yet confirmed either way.
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

// Local contrast (max-min luma) of the reference block, sampled over its
// own fixed 5x5 window -- independent of sad5x5_s's own (now
// COARSE_WINDOW_RADIUS-controlled) matching window above; this checks
// whether there's real texture here at all, not how wide a match window
// to use. Below MIN_CONTRAST, this block has
// essentially no real texture to match against -- dark/shadow sensor
// noise, or a genuinely flat surface -- so whatever offset the search
// below finds is closer to a random noise correlation than a real motion
// estimate. This is a different problem than REG_LAMBDA below already
// handles: REG_LAMBDA breaks near-ties toward zero when the cost surface
// is flat, but pure noise produces a *jagged*, not flat, cost surface --
// individual candidate offsets can score genuinely (if spuriously) lower
// than the true zero-motion cost purely by chance, which a small
// tie-breaking bias can't reliably outweigh. Confirmed on real dark-scene
// footage: without this gate, low-signal background regions mis-fire as
// incoherent, high-magnitude "motion" -- large patches of unrelated
// colors in the flow visualization, not the isolated one-off jitter
// REG_LAMBDA alone is meant to damp. Only applied at this coarsest level,
// since every finer level just nudges this level's result by +-1px with
// no search freedom of its own (see the refinement levels' comment
// below) -- a correct zero here propagates cleanly downstream.
//
// If real low-contrast motion is being missed, lower this; if dark-noise
// mis-firing persists, raise it -- and if raising it stops helping, the
// noise likely has enough local contrast (e.g. from shadow-lifting in
// the source grade) that this needs to also factor in absolute darkness
// (mean luma), not just contrast, as the next thing to try.
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

// Small-magnitude bias: breaks near-ties in flat/low-texture regions
// toward small/zero motion instead of letting the search wander onto an
// arbitrary large offset (which produces coherent local "fisheye" bulges
// rather than noise). Small enough that any genuinely stronger match wins.
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
    // full-res -- comfortably past MAX_PX (30px, see the debug shader's
    // magenta convention), meaning the search could reach and lock onto a
    // spurious match well beyond what any real per-frame motion in typical
    // content would need, given enough repetitive-looking texture to fool
    // it (confirmed on real footage: a backlit hair/shoulder edge against
    // blurred bokeh, which is exactly this kind of ambiguous, semi-
    // repetitive content). 0.75 caps full-res reach at ~23px -- if
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
//!DESC [high] coarse flow search B->A (1/16 res)

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

// See local_contrast_5x5_s()/MIN_CONTRAST in the A->B pass above for why
// this exists -- same gate, mirrored for the B->A direction.
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
// Macro-generated refinement levels: eighth, quarter, half res.
// Each level downsamples luma, then refines both AB and BA flow fields
// from the previous (coarser) level with a 3x3, one-pixel-step search.
// ---------------------------------------------------------------------

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!SAVE LUMA_A_E
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 1
//!DESC [tri] downsample slot 0 to 1/8 res (luma)
vec4 hook() {
    return vec4(dot(HOOKED_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!SAVE LUMA_B_E
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 1
//!DESC [tri] downsample slot 1 to 1/8 res (luma)
vec4 hook() {
    return vec4(dot(FRAME1_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!SAVE LUMA_C_E
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 1
//!DESC [tri] downsample slot 2 to 1/8 res (luma)
vec4 hook() {
    return vec4(dot(FRAME2_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
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
//!DESC [high] refine flow A->B (1/8 res)

// Snaps to the exact center of whichever FLOW_S_AB texel this position
// falls in, before reading it as this level's search seed just below.
// An ordinary bilinear read here (as this used to be) blends between
// neighboring coarse-level vectors whenever the sample position isn't
// exactly on a coarse texel center -- which is most positions, since
// this level is 2x finer. At a real motion boundary, where one coarse
// texel holds the object's true motion and its neighbor holds ~zero,
// that blend produces a smooth gradient of in-between seed vectors
// spanning roughly one full FLOW_S_AB texel width in every direction --
// 16 full-res pixels each way at this handoff specifically -- entirely
// independent of how correct the underlying FLOW_S_AB values are.
// Real-hardware testing already ruled out the coarse search's own
// matching-window size as the (sole) cause of the "nebulous cloud" seen
// bleeding from real motion boundaries into neighboring static content
// in interpolate-debug-overlay.glsl (see COARSE_WINDOW_RADIUS in the
// coarse search pass) -- this is a different, independent mechanism:
// not what value gets computed at each coarse texel, but how that value
// gets smeared across many fine-level texels when read as a seed.
// Applied at all three coarse-to-fine handoffs (S->E, E->Q, Q->H) at
// once rather than just this one, since a partial fix at a single
// handoff could produce an effect too small to read as a clear result
// on its own -- not yet confirmed on real hardware.
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

// Same window-straddling-boundary mechanism as COARSE_WINDOW_RADIUS at
// the S level (confirmed on real hardware: narrowing it there measurably
// shrank and reshaped the "nebulous cloud" visible via
// interpolate-debug-overlay.glsl, once the coarse-to-fine seed-snapping
// fix stopped masking the effect) -- applied here to this level's own
// matching window, at its own 1/8-res scale (footprint 40px at the
// original 5x5, 24px at this narrowed 3x3). Not yet confirmed whether
// this level's window contributes independently, or whether S's fix
// already accounts for what's left.
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
// reasoning), re-checked at this level's own resolution. This level's
// local search has no regularization of its own (a single +-1px step
// either wins on raw SAD or it doesn't) -- without also gating here, a
// correctly-zeroed coarse seed could still drift away from zero on pure
// noise at this level, then again at the next, compounding across all
// three refine levels regardless of what the coarse level decided.
// TESTING at 0.0 (was 0.02), disabling this level's early-exit entirely.
// This value was tuned against one specific failure mode (dark, noisy
// footage mis-firing as motion) and never checked against how much of a
// normal, smoothly-shaded frame it disables refinement for. Real-
// hardware evidence: widening REFINE_SEARCH_RADIUS had zero effect on
// the flow visualization's ~16px block granularity, which is consistent
// with this gate firing broadly enough that the search loop below never
// runs at all for most content -- no radius, however wide, matters if
// the code path it's in never executes. At 0.0, `< MIN_CONTRAST` can
// never be true, so this level's search always runs. Not yet confirmed.
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

    // How far this level's own local search can stray from the inherited
    // seed, in this level's own texels. TESTING at 2 (was effectively 1,
    // i.e. a single-step nudge). Real-hardware evidence pointed here: the
    // reported defect persisted through every fix to how cleanly each
    // level hands off to the next, and each refine level's total possible
    // contribution was only +-1 texel -- +-8px/+-4px/+-2px at E/Q/H,
    // +-14px combined -- meaning if the coarse S level's own decision
    // needs more correction than that to reach the true motion, nothing
    // downstream had the budget to supply it, no matter how clean the
    // hand-off was. Doubling the radius doubles that combined budget to
    // +-28px. This is a genuine architecture question, not a bug fix:
    // coarse-to-fine is still the right search order (a coarse level
    // covers a huge real-pixel area cheaply, which is what lets large
    // motion get found at all), but the refine levels exist specifically
    // to add detail on top of that coarse answer, and a 1-texel nudge may
    // simply not be enough room for them to do that job.
    const int REFINE_SEARCH_RADIUS = 2;

    // Bias against moving away from the inherited seed at all, unless a
    // neighbor's raw SAD cost is clearly lower. Without this, the loop
    // below has no preference for staying at an already-reasonable seed
    // over any of its neighbors -- unlike the coarse S level, whose
    // REG_LAMBDA discourages drifting from zero, every refine level's
    // local search would otherwise pick whichever candidate scores
    // marginally lowest on raw SAD alone, with nothing to reject a "win"
    // that's actually just window-contamination noise near a boundary
    // (see COARSE_WINDOW_RADIUS above -- even a narrowed window still has
    // *some* footprint, so this ambiguity shrinks rather than
    // disappears). Now that REFINE_SEARCH_RADIUS is wider than 1, the
    // candidates are no longer all the same distance from the seed (the
    // nearest are 1 texel away, the far corners ~2.8), so the bias is
    // scaled by that distance -- the same shape as the coarse level's own
    // REG_LAMBDA -- rather than the flat bias a single-ring search used.
    // Untested on real hardware -- a reasoned starting value, not a
    // verified one.
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
//!DESC [high] refine flow B->A (1/8 res)

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
//!BIND FRAME1
//!BIND FRAME2
//!SAVE LUMA_A_Q
//!WIDTH HOOKED.w 4 /
//!HEIGHT HOOKED.h 4 /
//!COMPONENTS 1
//!DESC [tri] downsample slot 0 to 1/4 res (luma)
vec4 hook() {
    return vec4(dot(HOOKED_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!SAVE LUMA_B_Q
//!WIDTH HOOKED.w 4 /
//!HEIGHT HOOKED.h 4 /
//!COMPONENTS 1
//!DESC [tri] downsample slot 1 to 1/4 res (luma)
vec4 hook() {
    return vec4(dot(FRAME1_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!SAVE LUMA_C_Q
//!WIDTH HOOKED.w 4 /
//!HEIGHT HOOKED.h 4 /
//!COMPONENTS 1
//!DESC [tri] downsample slot 2 to 1/4 res (luma)
vec4 hook() {
    return vec4(dot(FRAME2_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
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
//!DESC [high] refine flow A->B (1/4 res)

// Same seed-snapping fix as the S->E handoff above (see that pass for
// the full reasoning) -- here for the E->Q handoff: FLOW_E_AB's own
// texel is 8 full-res px, so an unsnapped bilinear read would smear a
// real boundary across ~8px in every direction (~16px total) when
// seeding this level, on top of whatever the S->E handoff already did.
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

// Same window-straddling-boundary mechanism as COARSE_WINDOW_RADIUS at
// the S and E levels above -- applied here at this level's own 1/4-res
// scale (footprint 20px at the original 5x5, 12px at this narrowed 3x3).
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
//!DESC [high] refine flow B->A (1/4 res)

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
//!BIND FRAME1
//!BIND FRAME2
//!SAVE LUMA_A_H
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 1
//!DESC [tri] downsample slot 0 to half res (luma)
vec4 hook() {
    return vec4(dot(HOOKED_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!SAVE LUMA_B_H
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 1
//!DESC [tri] downsample slot 1 to half res (luma)
vec4 hook() {
    return vec4(dot(FRAME1_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!SAVE LUMA_C_H
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 1
//!DESC [tri] downsample slot 2 to 1/2 res (luma)
vec4 hook() {
    return vec4(dot(FRAME2_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
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
//!DESC [high] refine flow A->B (half res)

// Same seed-snapping fix as the two coarser handoffs above -- here for
// the Q->H handoff: FLOW_Q_AB's own texel is 4 full-res px, so an
// unsnapped bilinear read would smear a real boundary across ~4px in
// every direction (~8px total) when seeding this level.
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

    // SUB-PIXEL REFINEMENT. Every search in this pipeline -- coarse and all
    // three refine levels -- steps WHOLE texels of its own level, so without
    // this the finest flow the estimator can express is one half-res texel,
    // i.e. 2 full-res px per interval. Nothing finer in the sampled field is
    // measured: it is bilinear interpolation of a half-res texture, which
    // looks smooth and carries no extra information.
    //
    // That floor is invisible to the interpolator on fast motion and decisive
    // for the acceleration field, which is a small residual of two such flows
    // and inherits the floor twice. Below |a| ~ 0.5 px/interval^2 the readings
    // pin to the resampling lattice instead of tracking the truth (A4 in
    // tests/scenes.sh errs 69-125% there).
    //
    // A parabola through the SAD minimum and its two neighbours per axis
    // recovers the sub-texel position of the true minimum -- standard block
    // matching, four extra SAD evaluations against the 25 the search already
    // does. The denominator is the valley's curvature: at or below zero the
    // neighbourhood is flat or non-convex, the fit is meaningless, and the
    // integer result is kept. Displacement is clamped to half a texel because
    // a parabola fit cannot legitimately move the minimum outside the bracket
    // it was fitted to.
    //
    // Deliberately at the HALF-RES level only. The coarser levels are each
    // re-searched by the level below, so sub-texel precision there is
    // discarded before it can be used.
    //
    // OFF in this shader, ON in the generated tridirectional one, and the
    // asymmetry is measured rather than arbitrary. Fractional flow forces the
    // warp to resample bilinearly where an integer half-res flow landed on
    // pixel centres, and that costs real dB on a pure interpolator: measured
    // -0.48 on L1_trans_8px, -0.66 on L2, -0.16 on O4_osc_flat300, with
    // nothing to show for it here because this shader has no acceleration
    // field to sharpen. The tridirectional shader pays the same cost and gets
    // a 5x better field for it (60.6% -> 11.2% error at |a| = 2.2), so there
    // the trade is worth taking. See tests/gen_tridirectional.py, which flips
    // this, and PLAN.md T1.1.
    const int SUBPEL_REFINE = 1;

    // SUBPEL_FIT 1 (equiangular) is the DEFAULT, from a measured A/B on the
    // acceleration calibration -- 15 of 18 paired samples improved, the low
    // band most (A5 f12 32.0% -> 3.9%, A4 f6 25.4% -> 4.3%, A6 f12
    // 15.3% -> 3.3%), the three losses all <= 0.7 points, and the quad
    // shader's jerk NULLS fell ~3.7x (A6 f12 -0.263 -> -0.070
    // px/interval^3). Exactly the peak-locking prediction from the stereo/
    // PIV literature (PRIOR-ART.md): the V fit matches the SAD valley's
    // piecewise-linear shape, the parabola does not. The interpolation-side
    // cost is small and confined to the sharpest content (tri ladder:
    // L1 -0.37, O2 -0.18, O4 -0.08, O5 -0.02 dB) -- more honest fractional
    // flow means marginally more resampling. Inert here while SUBPEL_REFINE
    // is 0; the field shaders inherit it live.
    const int SUBPEL_FIT = 1;
    if (SUBPEL_REFINE != 0) {
        float c0  = sad3x3_h(uv_a, uv_a + best_off);
        vec2  ex  = vec2(LUMA_A_H_pt.x, 0.0);
        vec2  ey  = vec2(0.0, LUMA_A_H_pt.y);
        float cxm = sad3x3_h(uv_a, uv_a + best_off - ex);
        float cxp = sad3x3_h(uv_a, uv_a + best_off + ex);
        float cym = sad3x3_h(uv_a, uv_a + best_off - ey);
        float cyp = sad3x3_h(uv_a, uv_a + best_off + ey);
        // TWO FITS, matched to two valley shapes -- and the choice is a
        // measured one, not a style preference. A parabola is the matched
        // estimator for an SSD valley (quadratic near its minimum); an SAD
        // valley of a well-matched shifted pattern is PIECEWISE LINEAR, for
        // which the matched estimator is the equiangular fit: two lines of
        // equal slope meeting at the vertex (Shimizu & Okutomi; standard in
        // stereo and PIV, where the parabola's mismatch is called PEAK
        // LOCKING -- a bias toward integer positions, worst at small
        // fractional displacements). Both share the same numerator; only
        // the denominator differs:
        //
        //   parabola:    x0 = (c_m - c_p) / (2*(c_m - 2*c_0 + c_p))
        //   equiangular: x0 = (c_m - c_p) / (2*(max(c_m, c_p) - c_0))
        //
        // A non-positive denominator means the neighbourhood is flat or
        // non-convex, the fit is meaningless, and the integer result is
        // kept. SUBPEL_FIT: 0 = parabola, 1 = equiangular.
        float dx = SUBPEL_FIT != 0 ? max(cxm, cxp) - c0 : cxm - 2.0 * c0 + cxp;
        float dy = SUBPEL_FIT != 0 ? max(cym, cyp) - c0 : cym - 2.0 * c0 + cyp;
        vec2  sub = vec2(dx > 1.0e-6 ? clamp(0.5 * (cxm - cxp) / dx, -0.5, 0.5) : 0.0,
                         dy > 1.0e-6 ? clamp(0.5 * (cym - cyp) / dy, -0.5, 0.5) : 0.0);
        best_off += sub * LUMA_A_H_pt;
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
//!DESC [high] refine flow B->A (half res)

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

    // SUB-PIXEL REFINEMENT. Every search in this pipeline -- coarse and all
    // three refine levels -- steps WHOLE texels of its own level, so without
    // this the finest flow the estimator can express is one half-res texel,
    // i.e. 2 full-res px per interval. Nothing finer in the sampled field is
    // measured: it is bilinear interpolation of a half-res texture, which
    // looks smooth and carries no extra information.
    //
    // That floor is invisible to the interpolator on fast motion and decisive
    // for the acceleration field, which is a small residual of two such flows
    // and inherits the floor twice. Below |a| ~ 0.5 px/interval^2 the readings
    // pin to the resampling lattice instead of tracking the truth (A4 in
    // tests/scenes.sh errs 69-125% there).
    //
    // A parabola through the SAD minimum and its two neighbours per axis
    // recovers the sub-texel position of the true minimum -- standard block
    // matching, four extra SAD evaluations against the 25 the search already
    // does. The denominator is the valley's curvature: at or below zero the
    // neighbourhood is flat or non-convex, the fit is meaningless, and the
    // integer result is kept. Displacement is clamped to half a texel because
    // a parabola fit cannot legitimately move the minimum outside the bracket
    // it was fitted to.
    //
    // Deliberately at the HALF-RES level only. The coarser levels are each
    // re-searched by the level below, so sub-texel precision there is
    // discarded before it can be used.
    //
    // OFF in this shader, ON in the generated tridirectional one, and the
    // asymmetry is measured rather than arbitrary. Fractional flow forces the
    // warp to resample bilinearly where an integer half-res flow landed on
    // pixel centres, and that costs real dB on a pure interpolator: measured
    // -0.48 on L1_trans_8px, -0.66 on L2, -0.16 on O4_osc_flat300, with
    // nothing to show for it here because this shader has no acceleration
    // field to sharpen. The tridirectional shader pays the same cost and gets
    // a 5x better field for it (60.6% -> 11.2% error at |a| = 2.2), so there
    // the trade is worth taking. See tests/gen_tridirectional.py, which flips
    // this, and PLAN.md T1.1.
    const int SUBPEL_REFINE = 1;

    // SUBPEL_FIT 1 (equiangular) is the DEFAULT, from a measured A/B on the
    // acceleration calibration -- 15 of 18 paired samples improved, the low
    // band most (A5 f12 32.0% -> 3.9%, A4 f6 25.4% -> 4.3%, A6 f12
    // 15.3% -> 3.3%), the three losses all <= 0.7 points, and the quad
    // shader's jerk NULLS fell ~3.7x (A6 f12 -0.263 -> -0.070
    // px/interval^3). Exactly the peak-locking prediction from the stereo/
    // PIV literature (PRIOR-ART.md): the V fit matches the SAD valley's
    // piecewise-linear shape, the parabola does not. The interpolation-side
    // cost is small and confined to the sharpest content (tri ladder:
    // L1 -0.37, O2 -0.18, O4 -0.08, O5 -0.02 dB) -- more honest fractional
    // flow means marginally more resampling. Inert here while SUBPEL_REFINE
    // is 0; the field shaders inherit it live.
    const int SUBPEL_FIT = 1;
    if (SUBPEL_REFINE != 0) {
        float c0  = sad3x3_h2(uv_b, uv_b + best_off);
        vec2  ex  = vec2(LUMA_A_H_pt.x, 0.0);
        vec2  ey  = vec2(0.0, LUMA_A_H_pt.y);
        float cxm = sad3x3_h2(uv_b, uv_b + best_off - ex);
        float cxp = sad3x3_h2(uv_b, uv_b + best_off + ex);
        float cym = sad3x3_h2(uv_b, uv_b + best_off - ey);
        float cyp = sad3x3_h2(uv_b, uv_b + best_off + ey);
        // TWO FITS, matched to two valley shapes -- and the choice is a
        // measured one, not a style preference. A parabola is the matched
        // estimator for an SSD valley (quadratic near its minimum); an SAD
        // valley of a well-matched shifted pattern is PIECEWISE LINEAR, for
        // which the matched estimator is the equiangular fit: two lines of
        // equal slope meeting at the vertex (Shimizu & Okutomi; standard in
        // stereo and PIV, where the parabola's mismatch is called PEAK
        // LOCKING -- a bias toward integer positions, worst at small
        // fractional displacements). Both share the same numerator; only
        // the denominator differs:
        //
        //   parabola:    x0 = (c_m - c_p) / (2*(c_m - 2*c_0 + c_p))
        //   equiangular: x0 = (c_m - c_p) / (2*(max(c_m, c_p) - c_0))
        //
        // A non-positive denominator means the neighbourhood is flat or
        // non-convex, the fit is meaningless, and the integer result is
        // kept. SUBPEL_FIT: 0 = parabola, 1 = equiangular.
        float dx = SUBPEL_FIT != 0 ? max(cxm, cxp) - c0 : cxm - 2.0 * c0 + cxp;
        float dy = SUBPEL_FIT != 0 ? max(cym, cyp) - c0 : cym - 2.0 * c0 + cyp;
        vec2  sub = vec2(dx > 1.0e-6 ? clamp(0.5 * (cxm - cxp) / dx, -0.5, 0.5) : 0.0,
                         dy > 1.0e-6 ? clamp(0.5 * (cym - cyp) / dy, -0.5, 0.5) : 0.0);
        best_off += sub * LUMA_A_H_pt;
    }
    vec4 result = vec4(best_off / LUMA_A_H_pt, 0.0, 0.0);
    imageStore(FLOW_H_BA_CACHE, coord, result);
    return result;
}

// ---------------------------------------------------------------------
// Vector median filter on both flow fields: rejects outlier vectors that
// disagree with their neighborhood (typical of ambiguous/textured content
// like smoke or particle effects), while preserving genuine motion
// boundaries -- unlike a blur, which would smear across them instead.
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
//!DESC [high] vector median filter on flow A->B (pass 1)
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

// Second pass: a single 3x3 vector median can be out-voted by a small cluster of neighboring cells that all agree with each other on the same wrong (but locally self-consistent) vector; running it twice extends its effective reach.
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
//!DESC [high] vector median filter on flow A->B (pass 2)
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
//!DESC [high] vector median filter on flow B->A (pass 1)
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

// Second pass: a single 3x3 vector median can be out-voted by a small cluster of neighboring cells that all agree with each other on the same wrong (but locally self-consistent) vector; running it twice extends its effective reach.
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
//!DESC [high] vector median filter on flow B->A (pass 2)
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
// =====================================================================
// SLOT 1 -> SLOT 2 flow chain ([tri], generated). The base's slot-0 -> slot-1
// chain with the luma pair shifted along by one; identical in every other
// respect. Together with the base's chains this gives all four adjacent-slot
// flows, from which the final pass reads whichever ones play the straddling
// and anchor roles for a given output frame.
// =====================================================================


// ---------------------------------------------------------------------
// Sixteenth-res coarse search, both directions: 5-step, 5x5 SAD window.
// Cached across repeated output frames sharing the same source pair --
// see the "Storage-based flow caching" note at the top of this file.
// ---------------------------------------------------------------------
//!TEXTURE FLOW_S_BC_CACHE
//!SIZE 240 135
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_S_BC_CACHE
//!BIND LUMA_A_S
//!BIND LUMA_B_S
//!BIND LUMA_C_S
//!SAVE FLOW_S_BC
//!WIDTH HOOKED.w 16 /
//!HEIGHT HOOKED.h 16 /
//!COMPONENTS 2
//!DESC [tri] coarse flow search slot1->slot2 (1/16 res)

// Matching-window radius for the coarse SAD cost below, independent of
// local_contrast_5x5_s()'s own fixed window further down (that one only
// checks whether there's enough texture here to trust a match at all,
// not how wide a match window to use). RE-TESTING at 1 (3x3, 48px
// footprint, down from the original 5x5/80px). First tried before the
// coarse-to-fine seed-snapping fix existed (see snap_texel() in the
// refine passes below) and came back pixel-identical -- but real-
// hardware testing after that fix confirmed the previously-smooth
// "nebulous cloud" is actually a sharp-edged grid of ~16px blocks,
// exactly this level's own native texel size (1/16 res), now visible
// because the seed-snapping fix stopped smoothing it away. That means
// the earlier null result may have been confounded by the very
// smoothing this level's output was passing through at the time, not a
// clean test of window size on its own. Re-testing now that the signal
// is no longer masked -- not yet confirmed either way.
const int COARSE_WINDOW_RADIUS = 1;

float sad5x5_s(vec2 uv_a, vec2 uv_b) {
    float s = 0.0;
    for (int y = -COARSE_WINDOW_RADIUS; y <= COARSE_WINDOW_RADIUS; y++) {
        for (int x = -COARSE_WINDOW_RADIUS; x <= COARSE_WINDOW_RADIUS; x++) {
            vec2 o = vec2(float(x), float(y)) * LUMA_A_S_pt;
            s += abs(LUMA_B_S_tex(uv_a + o).r - LUMA_C_S_tex(uv_b + o).r);
        }
    }
    return s;
}

// Local contrast (max-min luma) of the reference block, sampled over its
// own fixed 5x5 window -- independent of sad5x5_s's own (now
// COARSE_WINDOW_RADIUS-controlled) matching window above; this checks
// whether there's real texture here at all, not how wide a match window
// to use. Below MIN_CONTRAST, this block has
// essentially no real texture to match against -- dark/shadow sensor
// noise, or a genuinely flat surface -- so whatever offset the search
// below finds is closer to a random noise correlation than a real motion
// estimate. This is a different problem than REG_LAMBDA below already
// handles: REG_LAMBDA breaks near-ties toward zero when the cost surface
// is flat, but pure noise produces a *jagged*, not flat, cost surface --
// individual candidate offsets can score genuinely (if spuriously) lower
// than the true zero-motion cost purely by chance, which a small
// tie-breaking bias can't reliably outweigh. Confirmed on real dark-scene
// footage: without this gate, low-signal background regions mis-fire as
// incoherent, high-magnitude "motion" -- large patches of unrelated
// colors in the flow visualization, not the isolated one-off jitter
// REG_LAMBDA alone is meant to damp. Only applied at this coarsest level,
// since every finer level just nudges this level's result by +-1px with
// no search freedom of its own (see the refinement levels' comment
// below) -- a correct zero here propagates cleanly downstream.
//
// If real low-contrast motion is being missed, lower this; if dark-noise
// mis-firing persists, raise it -- and if raising it stops helping, the
// noise likely has enough local contrast (e.g. from shadow-lifting in
// the source grade) that this needs to also factor in absolute darkness
// (mean luma), not just contrast, as the next thing to try.
const float MIN_CONTRAST = 0.02;

float local_contrast_5x5_s(vec2 uv_a) {
    float lo = 1.0, hi = 0.0;
    for (int y = -2; y <= 2; y++) {
        for (int x = -2; x <= 2; x++) {
            float v = LUMA_B_S_tex(uv_a + vec2(float(x), float(y)) * LUMA_A_S_pt).r;
            lo = min(lo, v);
            hi = max(hi, v);
        }
    }
    return hi - lo;
}

// Small-magnitude bias: breaks near-ties in flat/low-texture regions
// toward small/zero motion instead of letting the search wander onto an
// arbitrary large offset (which produces coherent local "fisheye" bulges
// rather than noise). Small enough that any genuinely stronger match wins.
const float REG_LAMBDA = 0.06;

vec4 hook() {
    ivec2 coord = ivec2(LUMA_A_S_pos * LUMA_A_S_size);
    if (!pair_changed)
        return imageLoad(FLOW_S_BC_CACHE, coord);

    vec2 uv_a = LUMA_A_S_pos;

    if (local_contrast_5x5_s(uv_a) < MIN_CONTRAST) {
        vec4 result = vec4(0.0);
        imageStore(FLOW_S_BC_CACHE, coord, result);
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
    // full-res -- comfortably past MAX_PX (30px, see the debug shader's
    // magenta convention), meaning the search could reach and lock onto a
    // spurious match well beyond what any real per-frame motion in typical
    // content would need, given enough repetitive-looking texture to fool
    // it (confirmed on real footage: a backlit hair/shoulder edge against
    // blurred bokeh, which is exactly this kind of ambiguous, semi-
    // repetitive content). 0.75 caps full-res reach at ~23px -- if
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
    imageStore(FLOW_S_BC_CACHE, coord, result);
    return result;
}


//!TEXTURE FLOW_E_BC_CACHE
//!SIZE 480 270
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_E_BC_CACHE
//!BIND LUMA_A_E
//!BIND LUMA_B_E
//!BIND LUMA_C_E
//!BIND FLOW_S_BC
//!SAVE FLOW_E_BC
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 2
//!DESC [tri] refine flow slot1->slot2 (1/8 res)

// Snaps to the exact center of whichever FLOW_S_BC texel this position
// falls in, before reading it as this level's search seed just below.
// An ordinary bilinear read here (as this used to be) blends between
// neighboring coarse-level vectors whenever the sample position isn't
// exactly on a coarse texel center -- which is most positions, since
// this level is 2x finer. At a real motion boundary, where one coarse
// texel holds the object's true motion and its neighbor holds ~zero,
// that blend produces a smooth gradient of in-between seed vectors
// spanning roughly one full FLOW_S_BC texel width in every direction --
// 16 full-res pixels each way at this handoff specifically -- entirely
// independent of how correct the underlying FLOW_S_BC values are.
// Real-hardware testing already ruled out the coarse search's own
// matching-window size as the (sole) cause of the "nebulous cloud" seen
// bleeding from real motion boundaries into neighboring static content
// in interpolate-debug-overlay.glsl (see COARSE_WINDOW_RADIUS in the
// coarse search pass) -- this is a different, independent mechanism:
// not what value gets computed at each coarse texel, but how that value
// gets smeared across many fine-level texels when read as a seed.
// Applied at all three coarse-to-fine handoffs (S->E, E->Q, Q->H) at
// once rather than just this one, since a partial fix at a single
// handoff could produce an effect too small to read as a clear result
// on its own -- not yet confirmed on real hardware.
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

// Same window-straddling-boundary mechanism as COARSE_WINDOW_RADIUS at
// the S level (confirmed on real hardware: narrowing it there measurably
// shrank and reshaped the "nebulous cloud" visible via
// interpolate-debug-overlay.glsl, once the coarse-to-fine seed-snapping
// fix stopped masking the effect) -- applied here to this level's own
// matching window, at its own 1/8-res scale (footprint 40px at the
// original 5x5, 24px at this narrowed 3x3). Not yet confirmed whether
// this level's window contributes independently, or whether S's fix
// already accounts for what's left.
const int COARSE_WINDOW_RADIUS = 1;

float sad5x5_e(vec2 uv_a, vec2 uv_b) {
    float s = 0.0;
    for (int y = -COARSE_WINDOW_RADIUS; y <= COARSE_WINDOW_RADIUS; y++) {
        for (int x = -COARSE_WINDOW_RADIUS; x <= COARSE_WINDOW_RADIUS; x++) {
            vec2 o = vec2(float(x), float(y)) * LUMA_A_E_pt;
            s += abs(LUMA_B_E_tex(uv_a + o).r - LUMA_C_E_tex(uv_b + o).r);
        }
    }
    return s;
}

// Same low-signal gate as the coarse search (see that pass for the full
// reasoning), re-checked at this level's own resolution. This level's
// local search has no regularization of its own (a single +-1px step
// either wins on raw SAD or it doesn't) -- without also gating here, a
// correctly-zeroed coarse seed could still drift away from zero on pure
// noise at this level, then again at the next, compounding across all
// three refine levels regardless of what the coarse level decided.
// TESTING at 0.0 (was 0.02), disabling this level's early-exit entirely.
// This value was tuned against one specific failure mode (dark, noisy
// footage mis-firing as motion) and never checked against how much of a
// normal, smoothly-shaded frame it disables refinement for. Real-
// hardware evidence: widening REFINE_SEARCH_RADIUS had zero effect on
// the flow visualization's ~16px block granularity, which is consistent
// with this gate firing broadly enough that the search loop below never
// runs at all for most content -- no radius, however wide, matters if
// the code path it's in never executes. At 0.0, `< MIN_CONTRAST` can
// never be true, so this level's search always runs. Not yet confirmed.
const float MIN_CONTRAST = 0.0;

float local_contrast_5x5_e(vec2 uv_a) {
    float lo = 1.0, hi = 0.0;
    for (int y = -2; y <= 2; y++) {
        for (int x = -2; x <= 2; x++) {
            float v = LUMA_B_E_tex(uv_a + vec2(float(x), float(y)) * LUMA_A_E_pt).r;
            lo = min(lo, v);
            hi = max(hi, v);
        }
    }
    return hi - lo;
}

vec4 hook() {
    ivec2 coord = ivec2(LUMA_A_E_pos * LUMA_A_E_size);
    if (!pair_changed)
        return imageLoad(FLOW_E_BC_CACHE, coord);

    vec2 uv_a = LUMA_A_E_pos;
    vec2 base_off = FLOW_S_BC_tex(snap_texel(uv_a, FLOW_S_BC_size)).xy * 2.0 * LUMA_A_E_pt;

    if (local_contrast_5x5_e(uv_a) < MIN_CONTRAST) {
        vec4 result = vec4(base_off / LUMA_A_E_pt, 0.0, 0.0);
        imageStore(FLOW_E_BC_CACHE, coord, result);
        return result;
    }

    // How far this level's own local search can stray from the inherited
    // seed, in this level's own texels. TESTING at 2 (was effectively 1,
    // i.e. a single-step nudge). Real-hardware evidence pointed here: the
    // reported defect persisted through every fix to how cleanly each
    // level hands off to the next, and each refine level's total possible
    // contribution was only +-1 texel -- +-8px/+-4px/+-2px at E/Q/H,
    // +-14px combined -- meaning if the coarse S level's own decision
    // needs more correction than that to reach the true motion, nothing
    // downstream had the budget to supply it, no matter how clean the
    // hand-off was. Doubling the radius doubles that combined budget to
    // +-28px. This is a genuine architecture question, not a bug fix:
    // coarse-to-fine is still the right search order (a coarse level
    // covers a huge real-pixel area cheaply, which is what lets large
    // motion get found at all), but the refine levels exist specifically
    // to add detail on top of that coarse answer, and a 1-texel nudge may
    // simply not be enough room for them to do that job.
    const int REFINE_SEARCH_RADIUS = 2;

    // Bias against moving away from the inherited seed at all, unless a
    // neighbor's raw SAD cost is clearly lower. Without this, the loop
    // below has no preference for staying at an already-reasonable seed
    // over any of its neighbors -- unlike the coarse S level, whose
    // REG_LAMBDA discourages drifting from zero, every refine level's
    // local search would otherwise pick whichever candidate scores
    // marginally lowest on raw SAD alone, with nothing to reject a "win"
    // that's actually just window-contamination noise near a boundary
    // (see COARSE_WINDOW_RADIUS above -- even a narrowed window still has
    // *some* footprint, so this ambiguity shrinks rather than
    // disappears). Now that REFINE_SEARCH_RADIUS is wider than 1, the
    // candidates are no longer all the same distance from the seed (the
    // nearest are 1 texel away, the far corners ~2.8), so the bias is
    // scaled by that distance -- the same shape as the coarse level's own
    // REG_LAMBDA -- rather than the flat bias a single-ring search used.
    // Untested on real hardware -- a reasoned starting value, not a
    // verified one.
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
    imageStore(FLOW_E_BC_CACHE, coord, result);
    return result;
}


//!TEXTURE FLOW_Q_BC_CACHE
//!SIZE 960 540
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_Q_BC_CACHE
//!BIND LUMA_A_Q
//!BIND LUMA_B_Q
//!BIND LUMA_C_Q
//!BIND FLOW_E_BC
//!SAVE FLOW_Q_BC
//!WIDTH HOOKED.w 4 /
//!HEIGHT HOOKED.h 4 /
//!COMPONENTS 2
//!DESC [tri] refine flow slot1->slot2 (1/4 res)

// Same seed-snapping fix as the S->E handoff above (see that pass for
// the full reasoning) -- here for the E->Q handoff: FLOW_E_BC's own
// texel is 8 full-res px, so an unsnapped bilinear read would smear a
// real boundary across ~8px in every direction (~16px total) when
// seeding this level, on top of whatever the S->E handoff already did.
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

// Same window-straddling-boundary mechanism as COARSE_WINDOW_RADIUS at
// the S and E levels above -- applied here at this level's own 1/4-res
// scale (footprint 20px at the original 5x5, 12px at this narrowed 3x3).
const int COARSE_WINDOW_RADIUS = 1;

float sad5x5_q(vec2 uv_a, vec2 uv_b) {
    float s = 0.0;
    for (int y = -COARSE_WINDOW_RADIUS; y <= COARSE_WINDOW_RADIUS; y++) {
        for (int x = -COARSE_WINDOW_RADIUS; x <= COARSE_WINDOW_RADIUS; x++) {
            vec2 o = vec2(float(x), float(y)) * LUMA_A_Q_pt;
            s += abs(LUMA_B_Q_tex(uv_a + o).r - LUMA_C_Q_tex(uv_b + o).r);
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
            float v = LUMA_B_Q_tex(uv_a + vec2(float(x), float(y)) * LUMA_A_Q_pt).r;
            lo = min(lo, v);
            hi = max(hi, v);
        }
    }
    return hi - lo;
}

vec4 hook() {
    ivec2 coord = ivec2(LUMA_A_Q_pos * LUMA_A_Q_size);
    if (!pair_changed)
        return imageLoad(FLOW_Q_BC_CACHE, coord);

    vec2 uv_a = LUMA_A_Q_pos;
    vec2 base_off = FLOW_E_BC_tex(snap_texel(uv_a, FLOW_E_BC_size)).xy * 2.0 * LUMA_A_Q_pt;

    if (local_contrast_5x5_q(uv_a) < MIN_CONTRAST) {
        vec4 result = vec4(base_off / LUMA_A_Q_pt, 0.0, 0.0);
        imageStore(FLOW_Q_BC_CACHE, coord, result);
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
    imageStore(FLOW_Q_BC_CACHE, coord, result);
    return result;
}


//!TEXTURE FLOW_H_BC_CACHE
//!SIZE 1920 1080
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_H_BC_CACHE
//!BIND LUMA_A_H
//!BIND LUMA_B_H
//!BIND LUMA_C_H
//!BIND FLOW_Q_BC
//!SAVE FLOW_H_BC
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 2
//!DESC [tri] refine flow slot1->slot2 (half res)

// Same seed-snapping fix as the two coarser handoffs above -- here for
// the Q->H handoff: FLOW_Q_BC's own texel is 4 full-res px, so an
// unsnapped bilinear read would smear a real boundary across ~4px in
// every direction (~8px total) when seeding this level.
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

float sad3x3_h(vec2 uv_a, vec2 uv_b) {
    float s = 0.0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 o = vec2(float(x), float(y)) * LUMA_A_H_pt;
            s += abs(LUMA_B_H_tex(uv_a + o).r - LUMA_C_H_tex(uv_b + o).r);
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
            float v = LUMA_B_H_tex(uv_a + vec2(float(x), float(y)) * LUMA_A_H_pt).r;
            lo = min(lo, v);
            hi = max(hi, v);
        }
    }
    return hi - lo;
}

vec4 hook() {
    ivec2 coord = ivec2(LUMA_A_H_pos * LUMA_A_H_size);
    if (!pair_changed)
        return imageLoad(FLOW_H_BC_CACHE, coord);

    vec2 uv_a = LUMA_A_H_pos;
    vec2 base_off = FLOW_Q_BC_tex(snap_texel(uv_a, FLOW_Q_BC_size)).xy * 2.0 * LUMA_A_H_pt;

    if (local_contrast_3x3_h(uv_a) < MIN_CONTRAST) {
        vec4 result = vec4(base_off / LUMA_A_H_pt, 0.0, 0.0);
        imageStore(FLOW_H_BC_CACHE, coord, result);
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

    // SUB-PIXEL REFINEMENT. Every search in this pipeline -- coarse and all
    // three refine levels -- steps WHOLE texels of its own level, so without
    // this the finest flow the estimator can express is one half-res texel,
    // i.e. 2 full-res px per interval. Nothing finer in the sampled field is
    // measured: it is bilinear interpolation of a half-res texture, which
    // looks smooth and carries no extra information.
    //
    // That floor is invisible to the interpolator on fast motion and decisive
    // for the acceleration field, which is a small residual of two such flows
    // and inherits the floor twice. Below |a| ~ 0.5 px/interval^2 the readings
    // pin to the resampling lattice instead of tracking the truth (A4 in
    // tests/scenes.sh errs 69-125% there).
    //
    // A parabola through the SAD minimum and its two neighbours per axis
    // recovers the sub-texel position of the true minimum -- standard block
    // matching, four extra SAD evaluations against the 25 the search already
    // does. The denominator is the valley's curvature: at or below zero the
    // neighbourhood is flat or non-convex, the fit is meaningless, and the
    // integer result is kept. Displacement is clamped to half a texel because
    // a parabola fit cannot legitimately move the minimum outside the bracket
    // it was fitted to.
    //
    // Deliberately at the HALF-RES level only. The coarser levels are each
    // re-searched by the level below, so sub-texel precision there is
    // discarded before it can be used.
    //
    // OFF in this shader, ON in the generated tridirectional one, and the
    // asymmetry is measured rather than arbitrary. Fractional flow forces the
    // warp to resample bilinearly where an integer half-res flow landed on
    // pixel centres, and that costs real dB on a pure interpolator: measured
    // -0.48 on L1_trans_8px, -0.66 on L2, -0.16 on O4_osc_flat300, with
    // nothing to show for it here because this shader has no acceleration
    // field to sharpen. The tridirectional shader pays the same cost and gets
    // a 5x better field for it (60.6% -> 11.2% error at |a| = 2.2), so there
    // the trade is worth taking. See tests/gen_tridirectional.py, which flips
    // this, and PLAN.md T1.1.
    const int SUBPEL_REFINE = 1;

    // SUBPEL_FIT 1 (equiangular) is the DEFAULT, from a measured A/B on the
    // acceleration calibration -- 15 of 18 paired samples improved, the low
    // band most (A5 f12 32.0% -> 3.9%, A4 f6 25.4% -> 4.3%, A6 f12
    // 15.3% -> 3.3%), the three losses all <= 0.7 points, and the quad
    // shader's jerk NULLS fell ~3.7x (A6 f12 -0.263 -> -0.070
    // px/interval^3). Exactly the peak-locking prediction from the stereo/
    // PIV literature (PRIOR-ART.md): the V fit matches the SAD valley's
    // piecewise-linear shape, the parabola does not. The interpolation-side
    // cost is small and confined to the sharpest content (tri ladder:
    // L1 -0.37, O2 -0.18, O4 -0.08, O5 -0.02 dB) -- more honest fractional
    // flow means marginally more resampling. Inert here while SUBPEL_REFINE
    // is 0; the field shaders inherit it live.
    const int SUBPEL_FIT = 1;
    if (SUBPEL_REFINE != 0) {
        float c0  = sad3x3_h(uv_a, uv_a + best_off);
        vec2  ex  = vec2(LUMA_A_H_pt.x, 0.0);
        vec2  ey  = vec2(0.0, LUMA_A_H_pt.y);
        float cxm = sad3x3_h(uv_a, uv_a + best_off - ex);
        float cxp = sad3x3_h(uv_a, uv_a + best_off + ex);
        float cym = sad3x3_h(uv_a, uv_a + best_off - ey);
        float cyp = sad3x3_h(uv_a, uv_a + best_off + ey);
        // TWO FITS, matched to two valley shapes -- and the choice is a
        // measured one, not a style preference. A parabola is the matched
        // estimator for an SSD valley (quadratic near its minimum); an SAD
        // valley of a well-matched shifted pattern is PIECEWISE LINEAR, for
        // which the matched estimator is the equiangular fit: two lines of
        // equal slope meeting at the vertex (Shimizu & Okutomi; standard in
        // stereo and PIV, where the parabola's mismatch is called PEAK
        // LOCKING -- a bias toward integer positions, worst at small
        // fractional displacements). Both share the same numerator; only
        // the denominator differs:
        //
        //   parabola:    x0 = (c_m - c_p) / (2*(c_m - 2*c_0 + c_p))
        //   equiangular: x0 = (c_m - c_p) / (2*(max(c_m, c_p) - c_0))
        //
        // A non-positive denominator means the neighbourhood is flat or
        // non-convex, the fit is meaningless, and the integer result is
        // kept. SUBPEL_FIT: 0 = parabola, 1 = equiangular.
        float dx = SUBPEL_FIT != 0 ? max(cxm, cxp) - c0 : cxm - 2.0 * c0 + cxp;
        float dy = SUBPEL_FIT != 0 ? max(cym, cyp) - c0 : cym - 2.0 * c0 + cyp;
        vec2  sub = vec2(dx > 1.0e-6 ? clamp(0.5 * (cxm - cxp) / dx, -0.5, 0.5) : 0.0,
                         dy > 1.0e-6 ? clamp(0.5 * (cym - cyp) / dy, -0.5, 0.5) : 0.0);
        best_off += sub * LUMA_A_H_pt;
    }
    vec4 result = vec4(best_off / LUMA_A_H_pt, 0.0, 0.0);
    imageStore(FLOW_H_BC_CACHE, coord, result);
    return result;
}


// ---------------------------------------------------------------------
// Vector median filter on both flow fields: rejects outlier vectors that
// disagree with their neighborhood (typical of ambiguous/textured content
// like smoke or particle effects), while preserving genuine motion
// boundaries -- unlike a blur, which would smear across them instead.
// ---------------------------------------------------------------------
// Pass 1's result only ever feeds pass 2 within this same dispatch, so it
// has no cache of its own -- on a cache hit it returns a cheap dummy that
// pass 2 will never look at, skipping the real 9x9-comparison cost.
//!HOOK FRAME_MIX
//!BIND FLOW_H_BC
//!SAVE FLOW_H_BC
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 2
//!DESC [tri] vector median filter on flow slot1->slot2 (pass 1)
vec4 hook() {
    if (!pair_changed)
        return vec4(0.0);

    vec2 v[9];
    int n = 0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 o = vec2(float(x), float(y)) * FLOW_H_BC_pt;
            v[n++] = FLOW_H_BC_tex(FLOW_H_BC_pos + o).xy;
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


// Second pass: a single 3x3 vector median can be out-voted by a small cluster of neighboring cells that all agree with each other on the same wrong (but locally self-consistent) vector; running it twice extends its effective reach.
// This one's result is what the final warp actually reads, so it gets a
// real persistent cache (unlike pass 1 above).
//!TEXTURE FLOW_H_BC_MEDIAN_CACHE
//!SIZE 1920 1080
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_H_BC_MEDIAN_CACHE
//!BIND FLOW_H_BC
//!SAVE FLOW_H_BC
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 2
//!DESC [tri] vector median filter on flow slot1->slot2 (pass 2)
vec4 hook() {
    ivec2 coord = ivec2(FLOW_H_BC_pos * FLOW_H_BC_size);
    if (!pair_changed)
        return imageLoad(FLOW_H_BC_MEDIAN_CACHE, coord);

    vec2 v[9];
    int n = 0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 o = vec2(float(x), float(y)) * FLOW_H_BC_pt;
            v[n++] = FLOW_H_BC_tex(FLOW_H_BC_pos + o).xy;
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
    imageStore(FLOW_H_BC_MEDIAN_CACHE, coord, result);
    return result;
}
// =====================================================================
// SLOT 2 -> SLOT 1 flow chain ([tri], generated). The reverse of the chain
// above, and it exists so the final pass can close a round trip on the
// anchor's forward flow. Without it that flow is the one field in the shader
// nothing checks, and an unchecked flow is indistinguishable from real
// acceleration -- which is how constant-velocity content was being warped.
// =====================================================================


//!TEXTURE FLOW_S_CB_CACHE
//!SIZE 240 135
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_S_CB_CACHE
//!BIND LUMA_A_S
//!BIND LUMA_B_S
//!BIND LUMA_C_S
//!SAVE FLOW_S_CB
//!WIDTH HOOKED.w 16 /
//!HEIGHT HOOKED.h 16 /
//!COMPONENTS 2
//!DESC [tri] coarse flow search slot2->slot1 (1/16 res)

// See COARSE_WINDOW_RADIUS in the A->B pass above.
const int COARSE_WINDOW_RADIUS = 1;

float sad5x5_s2(vec2 uv_b, vec2 uv_a) {
    float s = 0.0;
    for (int y = -COARSE_WINDOW_RADIUS; y <= COARSE_WINDOW_RADIUS; y++) {
        for (int x = -COARSE_WINDOW_RADIUS; x <= COARSE_WINDOW_RADIUS; x++) {
            vec2 o = vec2(float(x), float(y)) * LUMA_A_S_pt;
            s += abs(LUMA_C_S_tex(uv_b + o).r - LUMA_B_S_tex(uv_a + o).r);
        }
    }
    return s;
}

// See local_contrast_5x5_s()/MIN_CONTRAST in the A->B pass above for why
// this exists -- same gate, mirrored for the B->A direction.
const float MIN_CONTRAST = 0.02;

float local_contrast_5x5_s2(vec2 uv_b) {
    float lo = 1.0, hi = 0.0;
    for (int y = -2; y <= 2; y++) {
        for (int x = -2; x <= 2; x++) {
            float v = LUMA_C_S_tex(uv_b + vec2(float(x), float(y)) * LUMA_A_S_pt).r;
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
        return imageLoad(FLOW_S_CB_CACHE, coord);

    vec2 uv_b = LUMA_B_S_pos;

    if (local_contrast_5x5_s2(uv_b) < MIN_CONTRAST) {
        vec4 result = vec4(0.0);
        imageStore(FLOW_S_CB_CACHE, coord, result);
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
    imageStore(FLOW_S_CB_CACHE, coord, result);
    return result;
}


//!TEXTURE FLOW_E_CB_CACHE
//!SIZE 480 270
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_E_CB_CACHE
//!BIND LUMA_A_E
//!BIND LUMA_B_E
//!BIND LUMA_C_E
//!BIND FLOW_S_CB
//!SAVE FLOW_E_CB
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 2
//!DESC [tri] refine flow slot2->slot1 (1/8 res)

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
            s += abs(LUMA_C_E_tex(uv_b + o).r - LUMA_B_E_tex(uv_a + o).r);
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
            float v = LUMA_C_E_tex(uv_b + vec2(float(x), float(y)) * LUMA_A_E_pt).r;
            lo = min(lo, v);
            hi = max(hi, v);
        }
    }
    return hi - lo;
}

vec4 hook() {
    ivec2 coord = ivec2(LUMA_B_E_pos * LUMA_B_E_size);
    if (!pair_changed)
        return imageLoad(FLOW_E_CB_CACHE, coord);

    vec2 uv_b = LUMA_B_E_pos;
    vec2 base_off = FLOW_S_CB_tex(snap_texel(uv_b, FLOW_S_CB_size)).xy * 2.0 * LUMA_A_E_pt;

    if (local_contrast_5x5_e2(uv_b) < MIN_CONTRAST) {
        vec4 result = vec4(base_off / LUMA_A_E_pt, 0.0, 0.0);
        imageStore(FLOW_E_CB_CACHE, coord, result);
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
    imageStore(FLOW_E_CB_CACHE, coord, result);
    return result;
}


//!TEXTURE FLOW_Q_CB_CACHE
//!SIZE 960 540
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_Q_CB_CACHE
//!BIND LUMA_A_Q
//!BIND LUMA_B_Q
//!BIND LUMA_C_Q
//!BIND FLOW_E_CB
//!SAVE FLOW_Q_CB
//!WIDTH HOOKED.w 4 /
//!HEIGHT HOOKED.h 4 /
//!COMPONENTS 2
//!DESC [tri] refine flow slot2->slot1 (1/4 res)

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
            s += abs(LUMA_C_Q_tex(uv_b + o).r - LUMA_B_Q_tex(uv_a + o).r);
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
            float v = LUMA_C_Q_tex(uv_b + vec2(float(x), float(y)) * LUMA_A_Q_pt).r;
            lo = min(lo, v);
            hi = max(hi, v);
        }
    }
    return hi - lo;
}

vec4 hook() {
    ivec2 coord = ivec2(LUMA_B_Q_pos * LUMA_B_Q_size);
    if (!pair_changed)
        return imageLoad(FLOW_Q_CB_CACHE, coord);

    vec2 uv_b = LUMA_B_Q_pos;
    vec2 base_off = FLOW_E_CB_tex(snap_texel(uv_b, FLOW_E_CB_size)).xy * 2.0 * LUMA_A_Q_pt;

    if (local_contrast_5x5_q2(uv_b) < MIN_CONTRAST) {
        vec4 result = vec4(base_off / LUMA_A_Q_pt, 0.0, 0.0);
        imageStore(FLOW_Q_CB_CACHE, coord, result);
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
    imageStore(FLOW_Q_CB_CACHE, coord, result);
    return result;
}


//!TEXTURE FLOW_H_CB_CACHE
//!SIZE 1920 1080
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_H_CB_CACHE
//!BIND LUMA_A_H
//!BIND LUMA_B_H
//!BIND LUMA_C_H
//!BIND FLOW_Q_CB
//!SAVE FLOW_H_CB
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 2
//!DESC [tri] refine flow slot2->slot1 (half res)

// See snap_texel() in the A->B pass above.
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

float sad3x3_h2(vec2 uv_b, vec2 uv_a) {
    float s = 0.0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 o = vec2(float(x), float(y)) * LUMA_A_H_pt;
            s += abs(LUMA_C_H_tex(uv_b + o).r - LUMA_B_H_tex(uv_a + o).r);
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
            float v = LUMA_C_H_tex(uv_b + vec2(float(x), float(y)) * LUMA_A_H_pt).r;
            lo = min(lo, v);
            hi = max(hi, v);
        }
    }
    return hi - lo;
}

vec4 hook() {
    ivec2 coord = ivec2(LUMA_B_H_pos * LUMA_B_H_size);
    if (!pair_changed)
        return imageLoad(FLOW_H_CB_CACHE, coord);

    vec2 uv_b = LUMA_B_H_pos;
    vec2 base_off = FLOW_Q_CB_tex(snap_texel(uv_b, FLOW_Q_CB_size)).xy * 2.0 * LUMA_A_H_pt;

    if (local_contrast_3x3_h2(uv_b) < MIN_CONTRAST) {
        vec4 result = vec4(base_off / LUMA_A_H_pt, 0.0, 0.0);
        imageStore(FLOW_H_CB_CACHE, coord, result);
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

    // SUB-PIXEL REFINEMENT. Every search in this pipeline -- coarse and all
    // three refine levels -- steps WHOLE texels of its own level, so without
    // this the finest flow the estimator can express is one half-res texel,
    // i.e. 2 full-res px per interval. Nothing finer in the sampled field is
    // measured: it is bilinear interpolation of a half-res texture, which
    // looks smooth and carries no extra information.
    //
    // That floor is invisible to the interpolator on fast motion and decisive
    // for the acceleration field, which is a small residual of two such flows
    // and inherits the floor twice. Below |a| ~ 0.5 px/interval^2 the readings
    // pin to the resampling lattice instead of tracking the truth (A4 in
    // tests/scenes.sh errs 69-125% there).
    //
    // A parabola through the SAD minimum and its two neighbours per axis
    // recovers the sub-texel position of the true minimum -- standard block
    // matching, four extra SAD evaluations against the 25 the search already
    // does. The denominator is the valley's curvature: at or below zero the
    // neighbourhood is flat or non-convex, the fit is meaningless, and the
    // integer result is kept. Displacement is clamped to half a texel because
    // a parabola fit cannot legitimately move the minimum outside the bracket
    // it was fitted to.
    //
    // Deliberately at the HALF-RES level only. The coarser levels are each
    // re-searched by the level below, so sub-texel precision there is
    // discarded before it can be used.
    //
    // OFF in this shader, ON in the generated tridirectional one, and the
    // asymmetry is measured rather than arbitrary. Fractional flow forces the
    // warp to resample bilinearly where an integer half-res flow landed on
    // pixel centres, and that costs real dB on a pure interpolator: measured
    // -0.48 on L1_trans_8px, -0.66 on L2, -0.16 on O4_osc_flat300, with
    // nothing to show for it here because this shader has no acceleration
    // field to sharpen. The tridirectional shader pays the same cost and gets
    // a 5x better field for it (60.6% -> 11.2% error at |a| = 2.2), so there
    // the trade is worth taking. See tests/gen_tridirectional.py, which flips
    // this, and PLAN.md T1.1.
    const int SUBPEL_REFINE = 1;

    // SUBPEL_FIT 1 (equiangular) is the DEFAULT, from a measured A/B on the
    // acceleration calibration -- 15 of 18 paired samples improved, the low
    // band most (A5 f12 32.0% -> 3.9%, A4 f6 25.4% -> 4.3%, A6 f12
    // 15.3% -> 3.3%), the three losses all <= 0.7 points, and the quad
    // shader's jerk NULLS fell ~3.7x (A6 f12 -0.263 -> -0.070
    // px/interval^3). Exactly the peak-locking prediction from the stereo/
    // PIV literature (PRIOR-ART.md): the V fit matches the SAD valley's
    // piecewise-linear shape, the parabola does not. The interpolation-side
    // cost is small and confined to the sharpest content (tri ladder:
    // L1 -0.37, O2 -0.18, O4 -0.08, O5 -0.02 dB) -- more honest fractional
    // flow means marginally more resampling. Inert here while SUBPEL_REFINE
    // is 0; the field shaders inherit it live.
    const int SUBPEL_FIT = 1;
    if (SUBPEL_REFINE != 0) {
        float c0  = sad3x3_h2(uv_b, uv_b + best_off);
        vec2  ex  = vec2(LUMA_A_H_pt.x, 0.0);
        vec2  ey  = vec2(0.0, LUMA_A_H_pt.y);
        float cxm = sad3x3_h2(uv_b, uv_b + best_off - ex);
        float cxp = sad3x3_h2(uv_b, uv_b + best_off + ex);
        float cym = sad3x3_h2(uv_b, uv_b + best_off - ey);
        float cyp = sad3x3_h2(uv_b, uv_b + best_off + ey);
        // TWO FITS, matched to two valley shapes -- and the choice is a
        // measured one, not a style preference. A parabola is the matched
        // estimator for an SSD valley (quadratic near its minimum); an SAD
        // valley of a well-matched shifted pattern is PIECEWISE LINEAR, for
        // which the matched estimator is the equiangular fit: two lines of
        // equal slope meeting at the vertex (Shimizu & Okutomi; standard in
        // stereo and PIV, where the parabola's mismatch is called PEAK
        // LOCKING -- a bias toward integer positions, worst at small
        // fractional displacements). Both share the same numerator; only
        // the denominator differs:
        //
        //   parabola:    x0 = (c_m - c_p) / (2*(c_m - 2*c_0 + c_p))
        //   equiangular: x0 = (c_m - c_p) / (2*(max(c_m, c_p) - c_0))
        //
        // A non-positive denominator means the neighbourhood is flat or
        // non-convex, the fit is meaningless, and the integer result is
        // kept. SUBPEL_FIT: 0 = parabola, 1 = equiangular.
        float dx = SUBPEL_FIT != 0 ? max(cxm, cxp) - c0 : cxm - 2.0 * c0 + cxp;
        float dy = SUBPEL_FIT != 0 ? max(cym, cyp) - c0 : cym - 2.0 * c0 + cyp;
        vec2  sub = vec2(dx > 1.0e-6 ? clamp(0.5 * (cxm - cxp) / dx, -0.5, 0.5) : 0.0,
                         dy > 1.0e-6 ? clamp(0.5 * (cym - cyp) / dy, -0.5, 0.5) : 0.0);
        best_off += sub * LUMA_A_H_pt;
    }
    vec4 result = vec4(best_off / LUMA_A_H_pt, 0.0, 0.0);
    imageStore(FLOW_H_CB_CACHE, coord, result);
    return result;
}


//!HOOK FRAME_MIX
//!BIND FLOW_H_CB
//!SAVE FLOW_H_CB
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 2
//!DESC [tri] vector median filter on flow slot2->slot1 (pass 1)
vec4 hook() {
    if (!pair_changed)
        return vec4(0.0);

    vec2 v[9];
    int n = 0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 o = vec2(float(x), float(y)) * FLOW_H_CB_pt;
            v[n++] = FLOW_H_CB_tex(FLOW_H_CB_pos + o).xy;
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


// Second pass: a single 3x3 vector median can be out-voted by a small cluster of neighboring cells that all agree with each other on the same wrong (but locally self-consistent) vector; running it twice extends its effective reach.
// This one's result is what the final warp actually reads, so it gets a
// real persistent cache (unlike pass 1 above).
//!TEXTURE FLOW_H_CB_MEDIAN_CACHE
//!SIZE 1920 1080
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_H_CB_MEDIAN_CACHE
//!BIND FLOW_H_CB
//!SAVE FLOW_H_CB
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 2
//!DESC [tri] vector median filter on flow slot2->slot1 (pass 2)
vec4 hook() {
    ivec2 coord = ivec2(FLOW_H_CB_pos * FLOW_H_CB_size);
    if (!pair_changed)
        return imageLoad(FLOW_H_CB_MEDIAN_CACHE, coord);

    vec2 v[9];
    int n = 0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 o = vec2(float(x), float(y)) * FLOW_H_CB_pt;
            v[n++] = FLOW_H_CB_tex(FLOW_H_CB_pos + o).xy;
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
    imageStore(FLOW_H_CB_MEDIAN_CACHE, coord, result);
    return result;
}
//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!SAVE LUMA_A_F
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!COMPONENTS 1
//!DESC [tri] slot 0 luma at full res
vec4 hook() {
    return vec4(dot(HOOKED_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}
//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!SAVE LUMA_B_F
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!COMPONENTS 1
//!DESC [tri] slot 1 luma at full res
vec4 hook() {
    return vec4(dot(FRAME1_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}
//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!SAVE LUMA_C_F
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!COMPONENTS 1
//!DESC [tri] slot 2 luma at full res
vec4 hook() {
    return vec4(dot(FRAME2_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!TEXTURE FLOW_F_AB_CACHE
//!SIZE 1920 1080
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_F_AB_CACHE
//!BIND LUMA_A_F
//!BIND LUMA_B_F
//!BIND FLOW_H_AB
//!SAVE FLOW_F_AB
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!COMPONENTS 2
//!DESC [tri] refine flow A->B (full res)

// Same seed-snapping fix as the two coarser handoffs above -- here for
// the H->F handoff: FLOW_H_AB's own texel is 2 full-res px, so an
// unsnapped bilinear read would smear a real boundary across ~2px in
// every direction (~4px total) when seeding this level.
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

float sad5x5_f(vec2 uv_a, vec2 uv_b) {
    float s = 0.0;
    for (int y = -2; y <= 2; y++) {
        for (int x = -2; x <= 2; x++) {
            vec2 o = vec2(float(x), float(y)) * LUMA_A_F_pt;
            s += abs(LUMA_A_F_tex(uv_a + o).r - LUMA_B_F_tex(uv_b + o).r);
        }
    }
    return s * (9.0 / 25.0);
}

// See local_contrast_5x5_e()/MIN_CONTRAST in the 1/8-res A->B pass --
// same reasoning, over the 3x3 window this level's own SAD uses.
// See the E-level A->B pass for the full reasoning.
const float MIN_CONTRAST = 0.0;

float local_contrast_3x3_f(vec2 uv_a) {
    float lo = 1.0, hi = 0.0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            float v = LUMA_A_F_tex(uv_a + vec2(float(x), float(y)) * LUMA_A_F_pt).r;
            lo = min(lo, v);
            hi = max(hi, v);
        }
    }
    return hi - lo;
}

vec4 hook() {
    ivec2 coord = ivec2(LUMA_A_F_pos * LUMA_A_F_size);
    if (!pair_changed)
        return imageLoad(FLOW_F_AB_CACHE, coord);

    vec2 uv_a = LUMA_A_F_pos;
    vec2 base_off = FLOW_H_AB_tex(snap_texel(uv_a, FLOW_H_AB_size)).xy * 2.0 * LUMA_A_F_pt;

    if (local_contrast_3x3_f(uv_a) < MIN_CONTRAST) {
        vec4 result = vec4(base_off / LUMA_A_F_pt, 0.0, 0.0);
        imageStore(FLOW_F_AB_CACHE, coord, result);
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
    float best_cost = sad5x5_f(uv_a, uv_a + base_off);

    for (int y = -REFINE_SEARCH_RADIUS; y <= REFINE_SEARCH_RADIUS; y++) {
        for (int x = -REFINE_SEARCH_RADIUS; x <= REFINE_SEARCH_RADIUS; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 off = base_off + vec2(float(x), float(y)) * LUMA_A_F_pt;
            float cost = sad5x5_f(uv_a, uv_a + off)
                       + REFINE_REG_LAMBDA * length(vec2(float(x), float(y)));
            if (cost < best_cost * (1.0 - TIE_MARGIN)) {
                best_cost = cost;
                best_off = off;
            }
        }
    }

    // SUB-PIXEL REFINEMENT. Every search in this pipeline -- coarse and all
    // three refine levels -- steps WHOLE texels of its own level, so without
    // this the finest flow the estimator can express is one half-res texel,
    // i.e. 2 full-res px per interval. Nothing finer in the sampled field is
    // measured: it is bilinear interpolation of a half-res texture, which
    // looks smooth and carries no extra information.
    //
    // That floor is invisible to the interpolator on fast motion and decisive
    // for the acceleration field, which is a small residual of two such flows
    // and inherits the floor twice. Below |a| ~ 0.5 px/interval^2 the readings
    // pin to the resampling lattice instead of tracking the truth (A4 in
    // tests/scenes.sh errs 69-125% there).
    //
    // A parabola through the SAD minimum and its two neighbours per axis
    // recovers the sub-texel position of the true minimum -- standard block
    // matching, four extra SAD evaluations against the 25 the search already
    // does. The denominator is the valley's curvature: at or below zero the
    // neighbourhood is flat or non-convex, the fit is meaningless, and the
    // integer result is kept. Displacement is clamped to half a texel because
    // a parabola fit cannot legitimately move the minimum outside the bracket
    // it was fitted to.
    //
    // Deliberately at the HALF-RES level only. The coarser levels are each
    // re-searched by the level below, so sub-texel precision there is
    // discarded before it can be used.
    //
    // OFF in this shader, ON in the generated tridirectional one, and the
    // asymmetry is measured rather than arbitrary. Fractional flow forces the
    // warp to resample bilinearly where an integer half-res flow landed on
    // pixel centres, and that costs real dB on a pure interpolator: measured
    // -0.48 on L1_trans_8px, -0.66 on L2, -0.16 on O4_osc_flat300, with
    // nothing to show for it here because this shader has no acceleration
    // field to sharpen. The tridirectional shader pays the same cost and gets
    // a 5x better field for it (60.6% -> 11.2% error at |a| = 2.2), so there
    // the trade is worth taking. See tests/gen_tridirectional.py, which flips
    // this, and PLAN.md T1.1.
    const int SUBPEL_REFINE = 1;

    // SUBPEL_FIT 1 (equiangular) is the DEFAULT, from a measured A/B on the
    // acceleration calibration -- 15 of 18 paired samples improved, the low
    // band most (A5 f12 32.0% -> 3.9%, A4 f6 25.4% -> 4.3%, A6 f12
    // 15.3% -> 3.3%), the three losses all <= 0.7 points, and the quad
    // shader's jerk NULLS fell ~3.7x (A6 f12 -0.263 -> -0.070
    // px/interval^3). Exactly the peak-locking prediction from the stereo/
    // PIV literature (PRIOR-ART.md): the V fit matches the SAD valley's
    // piecewise-linear shape, the parabola does not. The interpolation-side
    // cost is small and confined to the sharpest content (tri ladder:
    // L1 -0.37, O2 -0.18, O4 -0.08, O5 -0.02 dB) -- more honest fractional
    // flow means marginally more resampling. Inert here while SUBPEL_REFINE
    // is 0; the field shaders inherit it live.
    const int SUBPEL_FIT = 1;
    if (SUBPEL_REFINE != 0) {
        float c0  = sad5x5_f(uv_a, uv_a + best_off);
        vec2  ex  = vec2(LUMA_A_F_pt.x, 0.0);
        vec2  ey  = vec2(0.0, LUMA_A_F_pt.y);
        float cxm = sad5x5_f(uv_a, uv_a + best_off - ex);
        float cxp = sad5x5_f(uv_a, uv_a + best_off + ex);
        float cym = sad5x5_f(uv_a, uv_a + best_off - ey);
        float cyp = sad5x5_f(uv_a, uv_a + best_off + ey);
        // TWO FITS, matched to two valley shapes -- and the choice is a
        // measured one, not a style preference. A parabola is the matched
        // estimator for an SSD valley (quadratic near its minimum); an SAD
        // valley of a well-matched shifted pattern is PIECEWISE LINEAR, for
        // which the matched estimator is the equiangular fit: two lines of
        // equal slope meeting at the vertex (Shimizu & Okutomi; standard in
        // stereo and PIV, where the parabola's mismatch is called PEAK
        // LOCKING -- a bias toward integer positions, worst at small
        // fractional displacements). Both share the same numerator; only
        // the denominator differs:
        //
        //   parabola:    x0 = (c_m - c_p) / (2*(c_m - 2*c_0 + c_p))
        //   equiangular: x0 = (c_m - c_p) / (2*(max(c_m, c_p) - c_0))
        //
        // A non-positive denominator means the neighbourhood is flat or
        // non-convex, the fit is meaningless, and the integer result is
        // kept. SUBPEL_FIT: 0 = parabola, 1 = equiangular.
        float dx = SUBPEL_FIT != 0 ? max(cxm, cxp) - c0 : cxm - 2.0 * c0 + cxp;
        float dy = SUBPEL_FIT != 0 ? max(cym, cyp) - c0 : cym - 2.0 * c0 + cyp;
        vec2  sub = vec2(dx > 1.0e-6 ? clamp(0.5 * (cxm - cxp) / dx, -0.5, 0.5) : 0.0,
                         dy > 1.0e-6 ? clamp(0.5 * (cym - cyp) / dy, -0.5, 0.5) : 0.0);
        best_off += sub * LUMA_A_F_pt;
    }
    vec4 result = vec4(best_off / LUMA_A_F_pt, 0.0, 0.0);
    imageStore(FLOW_F_AB_CACHE, coord, result);
    return result;
}

//!TEXTURE FLOW_F_BA_CACHE
//!SIZE 1920 1080
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_F_BA_CACHE
//!BIND LUMA_A_F
//!BIND LUMA_B_F
//!BIND FLOW_H_BA
//!SAVE FLOW_F_BA
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!COMPONENTS 2
//!DESC [tri] refine flow B->A (full res)

// See snap_texel() in the A->B pass above.
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

float sad5x5_f2(vec2 uv_b, vec2 uv_a) {
    float s = 0.0;
    for (int y = -2; y <= 2; y++) {
        for (int x = -2; x <= 2; x++) {
            vec2 o = vec2(float(x), float(y)) * LUMA_A_F_pt;
            s += abs(LUMA_B_F_tex(uv_b + o).r - LUMA_A_F_tex(uv_a + o).r);
        }
    }
    return s * (9.0 / 25.0);
}

// See local_contrast_5x5_e()/MIN_CONTRAST in the 1/8-res A->B pass.
// See the E-level A->B pass for the full reasoning.
const float MIN_CONTRAST = 0.0;

float local_contrast_3x3_f2(vec2 uv_b) {
    float lo = 1.0, hi = 0.0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            float v = LUMA_B_F_tex(uv_b + vec2(float(x), float(y)) * LUMA_A_F_pt).r;
            lo = min(lo, v);
            hi = max(hi, v);
        }
    }
    return hi - lo;
}

vec4 hook() {
    ivec2 coord = ivec2(LUMA_B_F_pos * LUMA_B_F_size);
    if (!pair_changed)
        return imageLoad(FLOW_F_BA_CACHE, coord);

    vec2 uv_b = LUMA_B_F_pos;
    vec2 base_off = FLOW_H_BA_tex(snap_texel(uv_b, FLOW_H_BA_size)).xy * 2.0 * LUMA_A_F_pt;

    if (local_contrast_3x3_f2(uv_b) < MIN_CONTRAST) {
        vec4 result = vec4(base_off / LUMA_A_F_pt, 0.0, 0.0);
        imageStore(FLOW_F_BA_CACHE, coord, result);
        return result;
    }

    // See REFINE_SEARCH_RADIUS/REFINE_REG_LAMBDA in the A->B pass above.
    const int REFINE_SEARCH_RADIUS = 2;
    const float REFINE_REG_LAMBDA = 0.05;

    vec2 best_off = base_off;
    // See TIE_MARGIN in the coarse A->B search above.
    const float TIE_MARGIN = 1.0e-4;
    float best_cost = sad5x5_f2(uv_b, uv_b + base_off);

    for (int y = -REFINE_SEARCH_RADIUS; y <= REFINE_SEARCH_RADIUS; y++) {
        for (int x = -REFINE_SEARCH_RADIUS; x <= REFINE_SEARCH_RADIUS; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 off = base_off + vec2(float(x), float(y)) * LUMA_A_F_pt;
            float cost = sad5x5_f2(uv_b, uv_b + off)
                       + REFINE_REG_LAMBDA * length(vec2(float(x), float(y)));
            if (cost < best_cost * (1.0 - TIE_MARGIN)) {
                best_cost = cost;
                best_off = off;
            }
        }
    }

    // SUB-PIXEL REFINEMENT. Every search in this pipeline -- coarse and all
    // three refine levels -- steps WHOLE texels of its own level, so without
    // this the finest flow the estimator can express is one half-res texel,
    // i.e. 2 full-res px per interval. Nothing finer in the sampled field is
    // measured: it is bilinear interpolation of a half-res texture, which
    // looks smooth and carries no extra information.
    //
    // That floor is invisible to the interpolator on fast motion and decisive
    // for the acceleration field, which is a small residual of two such flows
    // and inherits the floor twice. Below |a| ~ 0.5 px/interval^2 the readings
    // pin to the resampling lattice instead of tracking the truth (A4 in
    // tests/scenes.sh errs 69-125% there).
    //
    // A parabola through the SAD minimum and its two neighbours per axis
    // recovers the sub-texel position of the true minimum -- standard block
    // matching, four extra SAD evaluations against the 25 the search already
    // does. The denominator is the valley's curvature: at or below zero the
    // neighbourhood is flat or non-convex, the fit is meaningless, and the
    // integer result is kept. Displacement is clamped to half a texel because
    // a parabola fit cannot legitimately move the minimum outside the bracket
    // it was fitted to.
    //
    // Deliberately at the HALF-RES level only. The coarser levels are each
    // re-searched by the level below, so sub-texel precision there is
    // discarded before it can be used.
    //
    // OFF in this shader, ON in the generated tridirectional one, and the
    // asymmetry is measured rather than arbitrary. Fractional flow forces the
    // warp to resample bilinearly where an integer half-res flow landed on
    // pixel centres, and that costs real dB on a pure interpolator: measured
    // -0.48 on L1_trans_8px, -0.66 on L2, -0.16 on O4_osc_flat300, with
    // nothing to show for it here because this shader has no acceleration
    // field to sharpen. The tridirectional shader pays the same cost and gets
    // a 5x better field for it (60.6% -> 11.2% error at |a| = 2.2), so there
    // the trade is worth taking. See tests/gen_tridirectional.py, which flips
    // this, and PLAN.md T1.1.
    const int SUBPEL_REFINE = 1;

    // SUBPEL_FIT 1 (equiangular) is the DEFAULT, from a measured A/B on the
    // acceleration calibration -- 15 of 18 paired samples improved, the low
    // band most (A5 f12 32.0% -> 3.9%, A4 f6 25.4% -> 4.3%, A6 f12
    // 15.3% -> 3.3%), the three losses all <= 0.7 points, and the quad
    // shader's jerk NULLS fell ~3.7x (A6 f12 -0.263 -> -0.070
    // px/interval^3). Exactly the peak-locking prediction from the stereo/
    // PIV literature (PRIOR-ART.md): the V fit matches the SAD valley's
    // piecewise-linear shape, the parabola does not. The interpolation-side
    // cost is small and confined to the sharpest content (tri ladder:
    // L1 -0.37, O2 -0.18, O4 -0.08, O5 -0.02 dB) -- more honest fractional
    // flow means marginally more resampling. Inert here while SUBPEL_REFINE
    // is 0; the field shaders inherit it live.
    const int SUBPEL_FIT = 1;
    if (SUBPEL_REFINE != 0) {
        float c0  = sad5x5_f2(uv_b, uv_b + best_off);
        vec2  ex  = vec2(LUMA_A_F_pt.x, 0.0);
        vec2  ey  = vec2(0.0, LUMA_A_F_pt.y);
        float cxm = sad5x5_f2(uv_b, uv_b + best_off - ex);
        float cxp = sad5x5_f2(uv_b, uv_b + best_off + ex);
        float cym = sad5x5_f2(uv_b, uv_b + best_off - ey);
        float cyp = sad5x5_f2(uv_b, uv_b + best_off + ey);
        // TWO FITS, matched to two valley shapes -- and the choice is a
        // measured one, not a style preference. A parabola is the matched
        // estimator for an SSD valley (quadratic near its minimum); an SAD
        // valley of a well-matched shifted pattern is PIECEWISE LINEAR, for
        // which the matched estimator is the equiangular fit: two lines of
        // equal slope meeting at the vertex (Shimizu & Okutomi; standard in
        // stereo and PIV, where the parabola's mismatch is called PEAK
        // LOCKING -- a bias toward integer positions, worst at small
        // fractional displacements). Both share the same numerator; only
        // the denominator differs:
        //
        //   parabola:    x0 = (c_m - c_p) / (2*(c_m - 2*c_0 + c_p))
        //   equiangular: x0 = (c_m - c_p) / (2*(max(c_m, c_p) - c_0))
        //
        // A non-positive denominator means the neighbourhood is flat or
        // non-convex, the fit is meaningless, and the integer result is
        // kept. SUBPEL_FIT: 0 = parabola, 1 = equiangular.
        float dx = SUBPEL_FIT != 0 ? max(cxm, cxp) - c0 : cxm - 2.0 * c0 + cxp;
        float dy = SUBPEL_FIT != 0 ? max(cym, cyp) - c0 : cym - 2.0 * c0 + cyp;
        vec2  sub = vec2(dx > 1.0e-6 ? clamp(0.5 * (cxm - cxp) / dx, -0.5, 0.5) : 0.0,
                         dy > 1.0e-6 ? clamp(0.5 * (cym - cyp) / dy, -0.5, 0.5) : 0.0);
        best_off += sub * LUMA_A_F_pt;
    }
    vec4 result = vec4(best_off / LUMA_A_F_pt, 0.0, 0.0);
    imageStore(FLOW_F_BA_CACHE, coord, result);
    return result;
}

//!TEXTURE FLOW_F_BC_CACHE
//!SIZE 1920 1080
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_F_BC_CACHE
//!BIND LUMA_A_F
//!BIND LUMA_B_F
//!BIND LUMA_C_F
//!BIND FLOW_H_BC
//!SAVE FLOW_F_BC
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!COMPONENTS 2
//!DESC [tri] refine flow slot1->slot2 (full res)

// Same seed-snapping fix as the two coarser handoffs above -- here for
// the H->F handoff: FLOW_H_BC's own texel is 2 full-res px, so an
// unsnapped bilinear read would smear a real boundary across ~2px in
// every direction (~4px total) when seeding this level.
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

float sad5x5_f(vec2 uv_a, vec2 uv_b) {
    float s = 0.0;
    for (int y = -2; y <= 2; y++) {
        for (int x = -2; x <= 2; x++) {
            vec2 o = vec2(float(x), float(y)) * LUMA_A_F_pt;
            s += abs(LUMA_B_F_tex(uv_a + o).r - LUMA_C_F_tex(uv_b + o).r);
        }
    }
    return s * (9.0 / 25.0);
}

// See local_contrast_5x5_e()/MIN_CONTRAST in the 1/8-res A->B pass --
// same reasoning, over the 3x3 window this level's own SAD uses.
// See the E-level A->B pass for the full reasoning.
const float MIN_CONTRAST = 0.0;

float local_contrast_3x3_f(vec2 uv_a) {
    float lo = 1.0, hi = 0.0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            float v = LUMA_B_F_tex(uv_a + vec2(float(x), float(y)) * LUMA_A_F_pt).r;
            lo = min(lo, v);
            hi = max(hi, v);
        }
    }
    return hi - lo;
}

vec4 hook() {
    ivec2 coord = ivec2(LUMA_A_F_pos * LUMA_A_F_size);
    if (!pair_changed)
        return imageLoad(FLOW_F_BC_CACHE, coord);

    vec2 uv_a = LUMA_A_F_pos;
    vec2 base_off = FLOW_H_BC_tex(snap_texel(uv_a, FLOW_H_BC_size)).xy * 2.0 * LUMA_A_F_pt;

    if (local_contrast_3x3_f(uv_a) < MIN_CONTRAST) {
        vec4 result = vec4(base_off / LUMA_A_F_pt, 0.0, 0.0);
        imageStore(FLOW_F_BC_CACHE, coord, result);
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
    float best_cost = sad5x5_f(uv_a, uv_a + base_off);

    for (int y = -REFINE_SEARCH_RADIUS; y <= REFINE_SEARCH_RADIUS; y++) {
        for (int x = -REFINE_SEARCH_RADIUS; x <= REFINE_SEARCH_RADIUS; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 off = base_off + vec2(float(x), float(y)) * LUMA_A_F_pt;
            float cost = sad5x5_f(uv_a, uv_a + off)
                       + REFINE_REG_LAMBDA * length(vec2(float(x), float(y)));
            if (cost < best_cost * (1.0 - TIE_MARGIN)) {
                best_cost = cost;
                best_off = off;
            }
        }
    }

    // SUB-PIXEL REFINEMENT. Every search in this pipeline -- coarse and all
    // three refine levels -- steps WHOLE texels of its own level, so without
    // this the finest flow the estimator can express is one half-res texel,
    // i.e. 2 full-res px per interval. Nothing finer in the sampled field is
    // measured: it is bilinear interpolation of a half-res texture, which
    // looks smooth and carries no extra information.
    //
    // That floor is invisible to the interpolator on fast motion and decisive
    // for the acceleration field, which is a small residual of two such flows
    // and inherits the floor twice. Below |a| ~ 0.5 px/interval^2 the readings
    // pin to the resampling lattice instead of tracking the truth (A4 in
    // tests/scenes.sh errs 69-125% there).
    //
    // A parabola through the SAD minimum and its two neighbours per axis
    // recovers the sub-texel position of the true minimum -- standard block
    // matching, four extra SAD evaluations against the 25 the search already
    // does. The denominator is the valley's curvature: at or below zero the
    // neighbourhood is flat or non-convex, the fit is meaningless, and the
    // integer result is kept. Displacement is clamped to half a texel because
    // a parabola fit cannot legitimately move the minimum outside the bracket
    // it was fitted to.
    //
    // Deliberately at the HALF-RES level only. The coarser levels are each
    // re-searched by the level below, so sub-texel precision there is
    // discarded before it can be used.
    //
    // OFF in this shader, ON in the generated tridirectional one, and the
    // asymmetry is measured rather than arbitrary. Fractional flow forces the
    // warp to resample bilinearly where an integer half-res flow landed on
    // pixel centres, and that costs real dB on a pure interpolator: measured
    // -0.48 on L1_trans_8px, -0.66 on L2, -0.16 on O4_osc_flat300, with
    // nothing to show for it here because this shader has no acceleration
    // field to sharpen. The tridirectional shader pays the same cost and gets
    // a 5x better field for it (60.6% -> 11.2% error at |a| = 2.2), so there
    // the trade is worth taking. See tests/gen_tridirectional.py, which flips
    // this, and PLAN.md T1.1.
    const int SUBPEL_REFINE = 1;

    // SUBPEL_FIT 1 (equiangular) is the DEFAULT, from a measured A/B on the
    // acceleration calibration -- 15 of 18 paired samples improved, the low
    // band most (A5 f12 32.0% -> 3.9%, A4 f6 25.4% -> 4.3%, A6 f12
    // 15.3% -> 3.3%), the three losses all <= 0.7 points, and the quad
    // shader's jerk NULLS fell ~3.7x (A6 f12 -0.263 -> -0.070
    // px/interval^3). Exactly the peak-locking prediction from the stereo/
    // PIV literature (PRIOR-ART.md): the V fit matches the SAD valley's
    // piecewise-linear shape, the parabola does not. The interpolation-side
    // cost is small and confined to the sharpest content (tri ladder:
    // L1 -0.37, O2 -0.18, O4 -0.08, O5 -0.02 dB) -- more honest fractional
    // flow means marginally more resampling. Inert here while SUBPEL_REFINE
    // is 0; the field shaders inherit it live.
    const int SUBPEL_FIT = 1;
    if (SUBPEL_REFINE != 0) {
        float c0  = sad5x5_f(uv_a, uv_a + best_off);
        vec2  ex  = vec2(LUMA_A_F_pt.x, 0.0);
        vec2  ey  = vec2(0.0, LUMA_A_F_pt.y);
        float cxm = sad5x5_f(uv_a, uv_a + best_off - ex);
        float cxp = sad5x5_f(uv_a, uv_a + best_off + ex);
        float cym = sad5x5_f(uv_a, uv_a + best_off - ey);
        float cyp = sad5x5_f(uv_a, uv_a + best_off + ey);
        // TWO FITS, matched to two valley shapes -- and the choice is a
        // measured one, not a style preference. A parabola is the matched
        // estimator for an SSD valley (quadratic near its minimum); an SAD
        // valley of a well-matched shifted pattern is PIECEWISE LINEAR, for
        // which the matched estimator is the equiangular fit: two lines of
        // equal slope meeting at the vertex (Shimizu & Okutomi; standard in
        // stereo and PIV, where the parabola's mismatch is called PEAK
        // LOCKING -- a bias toward integer positions, worst at small
        // fractional displacements). Both share the same numerator; only
        // the denominator differs:
        //
        //   parabola:    x0 = (c_m - c_p) / (2*(c_m - 2*c_0 + c_p))
        //   equiangular: x0 = (c_m - c_p) / (2*(max(c_m, c_p) - c_0))
        //
        // A non-positive denominator means the neighbourhood is flat or
        // non-convex, the fit is meaningless, and the integer result is
        // kept. SUBPEL_FIT: 0 = parabola, 1 = equiangular.
        float dx = SUBPEL_FIT != 0 ? max(cxm, cxp) - c0 : cxm - 2.0 * c0 + cxp;
        float dy = SUBPEL_FIT != 0 ? max(cym, cyp) - c0 : cym - 2.0 * c0 + cyp;
        vec2  sub = vec2(dx > 1.0e-6 ? clamp(0.5 * (cxm - cxp) / dx, -0.5, 0.5) : 0.0,
                         dy > 1.0e-6 ? clamp(0.5 * (cym - cyp) / dy, -0.5, 0.5) : 0.0);
        best_off += sub * LUMA_A_F_pt;
    }
    vec4 result = vec4(best_off / LUMA_A_F_pt, 0.0, 0.0);
    imageStore(FLOW_F_BC_CACHE, coord, result);
    return result;
}

//!TEXTURE FLOW_F_CB_CACHE
//!SIZE 1920 1080
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_F_CB_CACHE
//!BIND LUMA_A_F
//!BIND LUMA_B_F
//!BIND LUMA_C_F
//!BIND FLOW_H_CB
//!SAVE FLOW_F_CB
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!COMPONENTS 2
//!DESC [tri] refine flow slot2->slot1 (full res)

// See snap_texel() in the A->B pass above.
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

float sad5x5_f2(vec2 uv_b, vec2 uv_a) {
    float s = 0.0;
    for (int y = -2; y <= 2; y++) {
        for (int x = -2; x <= 2; x++) {
            vec2 o = vec2(float(x), float(y)) * LUMA_A_F_pt;
            s += abs(LUMA_C_F_tex(uv_b + o).r - LUMA_B_F_tex(uv_a + o).r);
        }
    }
    return s * (9.0 / 25.0);
}

// See local_contrast_5x5_e()/MIN_CONTRAST in the 1/8-res A->B pass.
// See the E-level A->B pass for the full reasoning.
const float MIN_CONTRAST = 0.0;

float local_contrast_3x3_f2(vec2 uv_b) {
    float lo = 1.0, hi = 0.0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            float v = LUMA_C_F_tex(uv_b + vec2(float(x), float(y)) * LUMA_A_F_pt).r;
            lo = min(lo, v);
            hi = max(hi, v);
        }
    }
    return hi - lo;
}

vec4 hook() {
    ivec2 coord = ivec2(LUMA_B_F_pos * LUMA_B_F_size);
    if (!pair_changed)
        return imageLoad(FLOW_F_CB_CACHE, coord);

    vec2 uv_b = LUMA_B_F_pos;
    vec2 base_off = FLOW_H_CB_tex(snap_texel(uv_b, FLOW_H_CB_size)).xy * 2.0 * LUMA_A_F_pt;

    if (local_contrast_3x3_f2(uv_b) < MIN_CONTRAST) {
        vec4 result = vec4(base_off / LUMA_A_F_pt, 0.0, 0.0);
        imageStore(FLOW_F_CB_CACHE, coord, result);
        return result;
    }

    // See REFINE_SEARCH_RADIUS/REFINE_REG_LAMBDA in the A->B pass above.
    const int REFINE_SEARCH_RADIUS = 2;
    const float REFINE_REG_LAMBDA = 0.05;

    vec2 best_off = base_off;
    // See TIE_MARGIN in the coarse A->B search above.
    const float TIE_MARGIN = 1.0e-4;
    float best_cost = sad5x5_f2(uv_b, uv_b + base_off);

    for (int y = -REFINE_SEARCH_RADIUS; y <= REFINE_SEARCH_RADIUS; y++) {
        for (int x = -REFINE_SEARCH_RADIUS; x <= REFINE_SEARCH_RADIUS; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 off = base_off + vec2(float(x), float(y)) * LUMA_A_F_pt;
            float cost = sad5x5_f2(uv_b, uv_b + off)
                       + REFINE_REG_LAMBDA * length(vec2(float(x), float(y)));
            if (cost < best_cost * (1.0 - TIE_MARGIN)) {
                best_cost = cost;
                best_off = off;
            }
        }
    }

    // SUB-PIXEL REFINEMENT. Every search in this pipeline -- coarse and all
    // three refine levels -- steps WHOLE texels of its own level, so without
    // this the finest flow the estimator can express is one half-res texel,
    // i.e. 2 full-res px per interval. Nothing finer in the sampled field is
    // measured: it is bilinear interpolation of a half-res texture, which
    // looks smooth and carries no extra information.
    //
    // That floor is invisible to the interpolator on fast motion and decisive
    // for the acceleration field, which is a small residual of two such flows
    // and inherits the floor twice. Below |a| ~ 0.5 px/interval^2 the readings
    // pin to the resampling lattice instead of tracking the truth (A4 in
    // tests/scenes.sh errs 69-125% there).
    //
    // A parabola through the SAD minimum and its two neighbours per axis
    // recovers the sub-texel position of the true minimum -- standard block
    // matching, four extra SAD evaluations against the 25 the search already
    // does. The denominator is the valley's curvature: at or below zero the
    // neighbourhood is flat or non-convex, the fit is meaningless, and the
    // integer result is kept. Displacement is clamped to half a texel because
    // a parabola fit cannot legitimately move the minimum outside the bracket
    // it was fitted to.
    //
    // Deliberately at the HALF-RES level only. The coarser levels are each
    // re-searched by the level below, so sub-texel precision there is
    // discarded before it can be used.
    //
    // OFF in this shader, ON in the generated tridirectional one, and the
    // asymmetry is measured rather than arbitrary. Fractional flow forces the
    // warp to resample bilinearly where an integer half-res flow landed on
    // pixel centres, and that costs real dB on a pure interpolator: measured
    // -0.48 on L1_trans_8px, -0.66 on L2, -0.16 on O4_osc_flat300, with
    // nothing to show for it here because this shader has no acceleration
    // field to sharpen. The tridirectional shader pays the same cost and gets
    // a 5x better field for it (60.6% -> 11.2% error at |a| = 2.2), so there
    // the trade is worth taking. See tests/gen_tridirectional.py, which flips
    // this, and PLAN.md T1.1.
    const int SUBPEL_REFINE = 1;

    // SUBPEL_FIT 1 (equiangular) is the DEFAULT, from a measured A/B on the
    // acceleration calibration -- 15 of 18 paired samples improved, the low
    // band most (A5 f12 32.0% -> 3.9%, A4 f6 25.4% -> 4.3%, A6 f12
    // 15.3% -> 3.3%), the three losses all <= 0.7 points, and the quad
    // shader's jerk NULLS fell ~3.7x (A6 f12 -0.263 -> -0.070
    // px/interval^3). Exactly the peak-locking prediction from the stereo/
    // PIV literature (PRIOR-ART.md): the V fit matches the SAD valley's
    // piecewise-linear shape, the parabola does not. The interpolation-side
    // cost is small and confined to the sharpest content (tri ladder:
    // L1 -0.37, O2 -0.18, O4 -0.08, O5 -0.02 dB) -- more honest fractional
    // flow means marginally more resampling. Inert here while SUBPEL_REFINE
    // is 0; the field shaders inherit it live.
    const int SUBPEL_FIT = 1;
    if (SUBPEL_REFINE != 0) {
        float c0  = sad5x5_f2(uv_b, uv_b + best_off);
        vec2  ex  = vec2(LUMA_A_F_pt.x, 0.0);
        vec2  ey  = vec2(0.0, LUMA_A_F_pt.y);
        float cxm = sad5x5_f2(uv_b, uv_b + best_off - ex);
        float cxp = sad5x5_f2(uv_b, uv_b + best_off + ex);
        float cym = sad5x5_f2(uv_b, uv_b + best_off - ey);
        float cyp = sad5x5_f2(uv_b, uv_b + best_off + ey);
        // TWO FITS, matched to two valley shapes -- and the choice is a
        // measured one, not a style preference. A parabola is the matched
        // estimator for an SSD valley (quadratic near its minimum); an SAD
        // valley of a well-matched shifted pattern is PIECEWISE LINEAR, for
        // which the matched estimator is the equiangular fit: two lines of
        // equal slope meeting at the vertex (Shimizu & Okutomi; standard in
        // stereo and PIV, where the parabola's mismatch is called PEAK
        // LOCKING -- a bias toward integer positions, worst at small
        // fractional displacements). Both share the same numerator; only
        // the denominator differs:
        //
        //   parabola:    x0 = (c_m - c_p) / (2*(c_m - 2*c_0 + c_p))
        //   equiangular: x0 = (c_m - c_p) / (2*(max(c_m, c_p) - c_0))
        //
        // A non-positive denominator means the neighbourhood is flat or
        // non-convex, the fit is meaningless, and the integer result is
        // kept. SUBPEL_FIT: 0 = parabola, 1 = equiangular.
        float dx = SUBPEL_FIT != 0 ? max(cxm, cxp) - c0 : cxm - 2.0 * c0 + cxp;
        float dy = SUBPEL_FIT != 0 ? max(cym, cyp) - c0 : cym - 2.0 * c0 + cyp;
        vec2  sub = vec2(dx > 1.0e-6 ? clamp(0.5 * (cxm - cxp) / dx, -0.5, 0.5) : 0.0,
                         dy > 1.0e-6 ? clamp(0.5 * (cym - cyp) / dy, -0.5, 0.5) : 0.0);
        best_off += sub * LUMA_A_F_pt;
    }
    vec4 result = vec4(best_off / LUMA_A_F_pt, 0.0, 0.0);
    imageStore(FLOW_F_CB_CACHE, coord, result);
    return result;
}

// ---------------------------------------------------------------------
// Edge-consistency reference (see the final warp pass below for how this
// gets used): per-frame motion-gated spatial edge masks, full
// resolution, one per source frame. Reuses the exact technique
// motion-edges-dual.glsl already validated on real hardware -- a pixel
// counts as "edge" only if it's both a genuine spatial edge within its
// own frame AND part of a temporally-moving region, so static scene
// edges (the vast majority of any frame) never register at all.
// Deliberately uncached: this is a new, unverified mechanism, so it
// starts as simply as possible. If real-hardware testing shows the
// extra full-res compute actually matters, caching this the same way
// the flow search is cached is the natural next step -- deferred rather
// than pre-optimized, since there's compute headroom to spare on the
// target hardware for now.
// ---------------------------------------------------------------------
//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!SAVE EDGE_A
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!COMPONENTS 1
//!DESC [high] motion-gated spatial edge mask (frame A)

const float MOTION_THRESHOLD = 0.08;
const float SPATIAL_EDGE_THRESHOLD = 0.1;

float luma(vec4 c) {
    return dot(c.rgb, vec3(0.299, 0.587, 0.114));
}

bool moving(vec2 pos) {
    return abs(luma(HOOKED_tex(pos)) - luma(FRAME1_tex(pos))) > MOTION_THRESHOLD;
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
//!BIND FRAME1
//!BIND FRAME2
//!SAVE EDGE_B
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!COMPONENTS 1
//!DESC [high] motion-gated spatial edge mask (frame B)

const float MOTION_THRESHOLD = 0.08;
const float SPATIAL_EDGE_THRESHOLD = 0.1;

float luma(vec4 c) {
    return dot(c.rgb, vec3(0.299, 0.587, 0.114));
}

bool moving(vec2 pos) {
    return abs(luma(HOOKED_tex(pos)) - luma(FRAME1_tex(pos))) > MOTION_THRESHOLD;
}

bool spatial_edge_b(vec2 pos) {
    float center = luma(FRAME1_tex(pos));
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 o = vec2(float(x), float(y)) * HOOKED_pt;
            if (abs(luma(FRAME1_tex(pos + o)) - center) > SPATIAL_EDGE_THRESHOLD)
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
// Final pass: TRIDIRECTIONAL warp -- quadratic (constant-acceleration)
// placement, full resolution.
//
// The bidirectional warp assumes constant velocity across the straddling
// interval: content moves f*s by output time s. Three frames determine a
// quadratic, and the constant-acceleration trajectory through them puts
// the straddling frames' content at
//
//     d(s) = f*s - (a/2)*s*(1-s)
//
// -- the linear warp plus a correction that vanishes at both endpoints
// and peaks at a/8 mid-interval. Both warp directions get the same
// +(a/2)*s*(1-s) term on their sample position (it is one trajectory
// bowing, seen from either end). At a = 0 this pass IS the bidirectional
// final pass, exactly -- that is both the safety property and the null
// hypothesis the benchmarks test.
//
// EVERYTHING READ HERE IS SLOT-KEYED. The four flows are between fixed
// adjacent slots, so they are pure functions of the window and the base's
// caching is valid for them unmodified. This pass is the only place that
// knows about ROLES, and it derives them per output frame from rts_mix
// without recomputing anything.
//
// WARP ON H, MEASURE ON F -- the two use cases split a third time (after
// the deadband and the sub-pixel default). The full-res flows are the
// finest measurement and feed the ESTIMATOR; the WARP keeps the mediated
// half-res flows, because the first full-res build fed them to both and
// the picture paid 2.95 dB on L1 -- the unfiltered final level moves
// pixels on scatter the medians used to remove, while the field's
// consumers never wanted the medians' smoothing in the first place.
// ---------------------------------------------------------------------
//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!BIND SCENE_DIFF
//!BIND SCENE_DIFF_BC
//!BIND FLOW_H_AB
//!BIND FLOW_H_BC
//!BIND FLOW_F_AB
//!BIND FLOW_F_BA
//!BIND FLOW_F_BC
//!BIND FLOW_F_CB
//!BIND EDGE_A
//!BIND EDGE_B
//!SAVE FRAME_MIX
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!DESC [tri] motion-compensated warp (quadratic placement)

// Texel snap and its edge-consistency gate: carried over from the base
// final pass unchanged (SNAP_STRENGTH is 0.0 there and stays 0.0 here, so
// both warps currently degenerate to plain bilinear -- kept for lockstep,
// see the base shader for the full history of this mechanism).
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

float edge_consistency(float expected, float snapped) {
    return 1.0 - abs(expected - snapped);
}

const float SNAP_STRENGTH = 0.0;

// Same value and reasoning as the base shader's gate (see its final pass).
const float SCENE_CUT_DIFF = 0.125;

// Acceleration clamp, in full-res px per straddle-interval^2. A physical
// bound, not a tuning knob: sustained acceleration beyond a few px/frame^2
// exits the search's ~23px/frame reach within a handful of frames (see the
// O-series calibration in tests/scenes.sh), and the oscillation ladder tops
// out at ~13. Anything much past that is estimation noise, so it is clamped
// and the shader degrades toward bidirectional behaviour instead of warping
// on noise. A reasoned starting value, not yet a measured optimum.
const float ACCEL_MAX_PX = 16.0;

// Acceleration is a SMALL RESIDUAL of two large, near-cancelling flows: under
// smooth motion the anchor's two outgoing flows point opposite ways and
// mostly cancel, and what survives is the acceleration. A gate is not
// optional -- ungated, this shader lost 13.7 dB on L1_trans_8px, a pure
// constant-velocity case where the true acceleration is exactly zero and it
// should have been a no-op.
//
// The first gate tried rejected by MAGNITUDE -- large |a| relative to the
// flows means they failed to cancel, so distrust it. That cannot work, and
// why is the central difficulty here. Two completely different things stop
// the flows cancelling:
//
//   OCCLUSION: one flow matched unrelated content. The residual is junk.
//   REVERSAL:  the object genuinely turned around. Both flows are good
//              matches pointing the same way, and the residual is the
//              largest, most REAL acceleration in the scene.
//
// A magnitude ratio drives toward 1 in both, so it discarded the signal
// exactly where it was strongest -- the fingerprint being that the gain FELL
// as acceleration rose, when the model should help more. Round-trip
// consistency separates them cleanly, because a reversal round-trips
// perfectly and an occlusion cannot. Judge the answer's provenance, not its
// size. Worth up to +4.4 dB. Thresholds in px of round-trip error; swept.
const float ACCEL_TRUST_LO = 2.0;
const float ACCEL_TRUST_HI = 5.0;

// DEADBAND on the acceleration used for the WARP -- deliberately not on the
// field the diagnostics report, because the two use cases want different
// things from the same number. A sensing consumer wants what was measured; an
// interpolator wants only what is safe to move pixels with.
//
// Why it is needed at all: sub-pixel refinement lifted the flow off the
// integer lattice, which is what made the field usable at low |a| -- but on
// content whose true acceleration is exactly zero the field still carries a
// heavy tail (measured on L7, constant velocity: median 0.000, p90 0.277,
// p99 3.914 px/interval^2). The correction acts on that tail and warps on
// noise. With sub-pixel enabled and no deadband it cost 0.82 dB on
// L1_trans_8px beyond the warp's own resampling cost.
//
// Expressed in px/interval^2 so it can be read against the calibration
// directly. Zero disables it.
//
// SWEPT, and 0.5/1.5 is the knee. On L1_trans_8px, where the true
// acceleration is exactly zero and the shader must be a no-op:
//
//   deadband      L1      O1      O2      O4      O5
//   off        56.16   49.65   46.17   47.35   34.03
//   0.25/0.75  58.21   49.62   46.17   47.35   34.03
//   0.5 /1.5   60.77   49.44   46.19   47.36   34.03
//   1.0 /2.5   61.35   49.06   46.16   47.33     --
//
// L1 climbs 5.2 dB across the sweep while the oscillation cases -- where the
// acceleration is real and the correction is earning its place -- move by
// hundredths until the widest setting finally costs O1 0.6 dB. 0.5/1.5 takes
// nearly all of the recovery for 0.21 dB of it.
//
// Against the pre-sub-pixel shader this is +3.31 dB on L1, which closes the
// -3.80 dB L1 regression that stood as the tridirectional shader's only
// losing case. Suppressing corrections below ~1 px/interval^2 costs at most
// a/8 ~ 0.12 px of placement error, which is not a visible amount.
const float ACCEL_DEADBAND_LO = 0.5;
const float ACCEL_DEADBAND_HI = 1.5;

// TRI_DIAG -- in-shader diagnostic output, for reading the estimator's
// internal fields without building a separate visualiser (tests/trivis.py is
// the full four-panel instrument).
//
//   0 = normal interpolated output
//   1 = the quadratic CORRECTION, i.e. how far this texel is being moved off
//       the constant-velocity straight line, in px
//   2 = the ACCELERATION field, in px per interval^2
//   3 = acceleration MAGNITUDE as a heat map, auto-scaled to ACCEL_DIAG_FS
//   4 = acceleration magnitude as LINEAR LUMA -- a measurement mode, so a
//       whole-frame average is proportional to mean |a|. No marker.
//
// Modes 1 and 2 encode a 2D vector the way tests/flowvis.py does: R and G
// carry the x and y components around a mid-grey zero, so mid-grey means
// "nothing here" and the hue tells you the direction. Mode 3 discards
// direction and shows only magnitude, which is easier to read when the
// question is "is there any acceleration in this shot at all".
//
// A MODE MARKER is burned into the top-left corner whenever TRI_DIAG is
// non-zero: a solid colour block, one colour per mode. It exists because the
// honest failure mode of these diagnostics is a screen of near-uniform
// mid-grey that looks identical to "the switch did nothing" -- and on real
// footage that is the COMMON case, since ordinary camera motion carries far
// less acceleration than the synthetic ladder does. With the marker, "mode is
// active but the field is near zero" and "my edit did not take effect" stop
// looking the same.
const int TRI_DIAG = 0;

// Full-scale values for the diagnostic encodings, in real units, so a reader
// can convert a pixel back to a number rather than guess.
//
// These are deliberately far more sensitive than the synthetic ladder needs.
// The ladder reaches 13 px/interval^2; ordinary camera motion is one to two
// orders of magnitude below that, and the first version of these constants
// was calibrated on the ladder and rendered real footage invisible -- mode 1
// deviated by ONE level out of 255. Set for the content you are looking at:
// raise for synthetic tests, lower to see subtle real motion.
const float ACCEL_DIAG_FS = 2.0;   // px/interval^2 at full scale (modes 2, 3)
const float CORR_DIAG_FS  = 0.25;  // px of correction at full scale (mode 1)

// Mode marker: a solid block in the top-left corner, 24px square.
vec4 tri_diag_marker() {
    if (TRI_DIAG == 1) return vec4(1.0, 0.2, 0.2, 1.0);   // red   -- correction
    if (TRI_DIAG == 2) return vec4(0.2, 0.6, 1.0, 1.0);   // blue  -- acceleration
    return vec4(0.2, 1.0, 0.3, 1.0);                      // green -- magnitude
}

vec4 hook() {
    // ---- roles, derived per output frame from slot-keyed fields ----
    // rts_mix[1] > 0 means slot 1 is still in the future, so the output sits
    // in the FIRST interval (slots 0-1). Otherwise it sits in the second.
    bool first_half = rts_mix[1] > 0.0;

    float tA = first_half ? rts_mix[0] : rts_mix[1];
    float tB = first_half ? rts_mix[1] : rts_mix[2];
    float L  = tB - tA;                       // straddle interval, > 0
    float s  = clamp((0.0 - tA) / L, 0.0, 1.0);

    // Straddling flow: slots 0-1 or slots 1-2.
    vec2 f_fwd = (first_half ? FLOW_H_AB_tex(HOOKED_pos).xy
                             : FLOW_H_BC_tex(HOOKED_pos).xy) * 2.0 * HOOKED_pt;

    // Cut inside the straddling pair: reproduce the cut (base behaviour).
    float cut_straddle = first_half ? SCENE_DIFF_tex(vec2(0.5)).r
                                    : SCENE_DIFF_BC_tex(vec2(0.5)).r;
    if (cut_straddle > SCENE_CUT_DIFF) {
        if (first_half)
            return s < 0.5 ? HOOKED_tex(HOOKED_pos) : FRAME1_tex(HOOKED_pos);
        return s < 0.5 ? FRAME1_tex(HOOKED_pos) : FRAME2_tex(HOOKED_pos);
    }

    // ---- acceleration: the anchor is ALWAYS slot 1 ----
    // Whichever half the output sits in, slot 1 is the frame with two
    // outgoing flows inside the window, so the solve has no phase
    // dependence at all. f10 and f12 are its flows toward slots 0 and 2.
    vec2 f10 = FLOW_F_BA_tex(HOOKED_pos).xy * HOOKED_pt;
    vec2 f12 = FLOW_F_BC_tex(HOOKED_pos).xy * HOOKED_pt;

    // Quadratic through slot 1's three sampled positions, in units of the
    // straddle interval. For uniform spacing tau0 = -1 and tau2 = +1, and
    // this reduces to a = f10 + f12: the two flows cancel under constant
    // velocity and whatever survives IS the acceleration. Written out in
    // full so non-uniform (VFR) spacing is exact rather than assumed away.
    float tau0 = (rts_mix[0] - rts_mix[1]) / L;
    float tau2 = (rts_mix[2] - rts_mix[1]) / L;
    vec2 accel = 2.0 * (f12 * tau0 - f10 * tau2)
               / (tau2 * tau0 * (tau2 - tau0));

    // A cut between slot 1 and the far slot does not stop the straddling
    // pair being blendable -- it only makes the acceleration meaningless. So
    // zero it and degrade exactly to bidirectional, rather than cutting.
    float cut_far = first_half ? SCENE_DIFF_BC_tex(vec2(0.5)).r
                               : SCENE_DIFF_tex(vec2(0.5)).r;
    if (cut_far > SCENE_CUT_DIFF)
        accel = vec2(0.0);

    // ---- confidence: round-trip BOTH of the anchor's flows ----
    // Follow each flow out and back. Content visible in both frames lands
    // where it started; occluded content does not. Both are checked at slot
    // 1's own grid, and the worse of the two decides -- a texel has to
    // survive both to be believed, because the acceleration is built from
    // both and either being wrong is enough to ruin it.
    vec2 r10 = FLOW_F_AB_tex(HOOKED_pos + f10).xy * HOOKED_pt;
    float rt10 = length(f10 + r10) / length(HOOKED_pt);

    vec2 r12 = FLOW_F_CB_tex(HOOKED_pos + f12).xy * HOOKED_pt;
    float rt12 = length(f12 + r12) / length(HOOKED_pt);

    accel *= 1.0 - smoothstep(ACCEL_TRUST_LO, ACCEL_TRUST_HI, max(rt10, rt12));

    // NO SPANNING slot-0 -> slot-2 TEST, and this is a proof rather than an
    // omission. It was built (6 passes) and measured, on the reasoning that
    // the triangle identity d01 + d12 == d02 checks the measurements against
    // each other. Count the degrees of freedom: three frames give TWO unknown
    // displacements and THREE measurements, so exactly ONE redundancy -- and
    // the identity spends it constraining the SUM. Acceleration is the
    // DIFFERENCE. Orthogonal, so the constraint cannot touch it. A
    // common-mode error, which is what a moving edge produces, is invisible
    // to it by construction. Measured: weighting that residual 20x recovered
    // 0.09 dB on L1 while costing 2.59 dB on O2 -- anti-correlated with its
    // purpose. Validating acceleration needs a FOURTH frame; see
    // TRIDIRECTIONAL.md.

    vec2 amax = ACCEL_MAX_PX * HOOKED_pt;
    accel = clamp(accel, -amax, amax);

    // ---- quadratic placement: linear warp plus the s(1-s) correction ----
    // The warp's copy of the acceleration, deadbanded; `accel` itself is left
    // alone so TRI_DIAG still reports the measurement rather than the gate.
    vec2 accel_w = accel;
    if (ACCEL_DEADBAND_HI > 0.0)
        accel_w *= smoothstep(ACCEL_DEADBAND_LO, ACCEL_DEADBAND_HI,
                              length(accel / HOOKED_pt));

    vec2 corr = 0.5 * accel_w * s * (1.0 - s);

    if (TRI_DIAG != 0) {
        // Mode 4 is a MEASUREMENT mode, not an eyeball mode: |a| as linear
        // luma, so a whole-frame average is directly proportional to the mean
        // acceleration in the frame and the field can be reduced to one
        // number per frame by signalstats. No marker, deliberately -- a
        // 24x24 patch would bias that average, and nothing downstream is
        // looking at it by eye.
        if (TRI_DIAG == 4)
            return vec4(vec3(clamp(length(accel / HOOKED_pt) / ACCEL_DIAG_FS,
                                   0.0, 1.0)), 1.0);

        // Mode marker first, so an active-but-empty diagnostic is never
        // mistaken for an edit that did not take effect.
        if (HOOKED_pos.x < 24.0 * HOOKED_pt.x && HOOKED_pos.y < 24.0 * HOOKED_pt.y)
            return tri_diag_marker();

        if (TRI_DIAG == 1)
            return vec4(0.5 + (corr / HOOKED_pt) * (0.5 / CORR_DIAG_FS), 0.5, 1.0);
        if (TRI_DIAG == 2)
            return vec4(0.5 + (accel / HOOKED_pt) * (0.5 / ACCEL_DIAG_FS), 0.5, 1.0);

        // Mode 3: magnitude only, blue -> cyan -> red across 0..ACCEL_DIAG_FS.
        float m = clamp(length(accel / HOOKED_pt) / ACCEL_DIAG_FS, 0.0, 1.0);
        vec3 c = m < 0.5 ? mix(vec3(0.0, 0.0, 0.25), vec3(0.0, 0.9, 0.9), m * 2.0)
                         : mix(vec3(0.0, 0.9, 0.9), vec3(1.0, 0.1, 0.0), (m - 0.5) * 2.0);
        return vec4(c, 1.0);
    }

    vec2 uv_a = HOOKED_pos - f_fwd * s + corr;
    vec2 uv_b = HOOKED_pos + f_fwd * (1.0 - s) + corr;

    vec4 sa = first_half ? HOOKED_tex(uv_a) : FRAME1_tex(uv_a);
    vec4 sb = first_half ? FRAME1_tex(uv_b) : FRAME2_tex(uv_b);

    // Snap gate, inert at SNAP_STRENGTH 0.0 but kept in lockstep with the
    // base. EDGE_A/EDGE_B are pinned to slots 0-1 (see their passes).
    vec2 sa_uv = snap_texel(uv_a, HOOKED_size);
    vec2 sb_uv = snap_texel(uv_b, HOOKED_size);
    float ea = edge_consistency(EDGE_A_tex(uv_a).r, EDGE_A_tex(sa_uv).r);
    float eb = edge_consistency(EDGE_B_tex(uv_b).r, EDGE_B_tex(sb_uv).r);
    sa = mix(sa, first_half ? HOOKED_tex(sa_uv) : FRAME1_tex(sa_uv),
             SNAP_STRENGTH * ea);
    sb = mix(sb, first_half ? FRAME1_tex(sb_uv) : FRAME2_tex(sb_uv),
             SNAP_STRENGTH * eb);

    return mix(sa, sb, s);
}

// ==== human-reading tail (generated by tests/add_human_reading.py; do not edit) ====
//!PARAM read_view
//!DESC 0 = normal output; 1/2/3 = velocity/acceleration/jerk painted for a human; 4/5/6 = the same fields raw, for a machine
//!TYPE int
//!MINIMUM 0
//!MAXIMUM 6
0

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!BIND SCENE_DIFF
//!BIND SCENE_DIFF_BC
//!BIND FLOW_H_AB
//!BIND FLOW_H_BC
//!BIND FLOW_F_AB
//!BIND FLOW_F_BA
//!BIND FLOW_F_BC
//!BIND FLOW_F_CB
//!BIND EDGE_A
//!BIND EDGE_B
//!SAVE READ_FIELD
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!WHEN read_view 0 >
//!DESC [reading] the chosen field in px at 1/8 res: this shader's own final pass in its diagnostic mode

// Texel snap and its edge-consistency gate: carried over from the base
// final pass unchanged (SNAP_STRENGTH is 0.0 there and stays 0.0 here, so
// both warps currently degenerate to plain bilinear -- kept for lockstep,
// see the base shader for the full history of this mechanism).
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

float edge_consistency(float expected, float snapped) {
    return 1.0 - abs(expected - snapped);
}

const float SNAP_STRENGTH = 0.0;

// Same value and reasoning as the base shader's gate (see its final pass).
const float SCENE_CUT_DIFF = 0.125;

// Acceleration clamp, in full-res px per straddle-interval^2. A physical
// bound, not a tuning knob: sustained acceleration beyond a few px/frame^2
// exits the search's ~23px/frame reach within a handful of frames (see the
// O-series calibration in tests/scenes.sh), and the oscillation ladder tops
// out at ~13. Anything much past that is estimation noise, so it is clamped
// and the shader degrades toward bidirectional behaviour instead of warping
// on noise. A reasoned starting value, not yet a measured optimum.
const float ACCEL_MAX_PX = 16.0;

// Acceleration is a SMALL RESIDUAL of two large, near-cancelling flows: under
// smooth motion the anchor's two outgoing flows point opposite ways and
// mostly cancel, and what survives is the acceleration. A gate is not
// optional -- ungated, this shader lost 13.7 dB on L1_trans_8px, a pure
// constant-velocity case where the true acceleration is exactly zero and it
// should have been a no-op.
//
// The first gate tried rejected by MAGNITUDE -- large |a| relative to the
// flows means they failed to cancel, so distrust it. That cannot work, and
// why is the central difficulty here. Two completely different things stop
// the flows cancelling:
//
//   OCCLUSION: one flow matched unrelated content. The residual is junk.
//   REVERSAL:  the object genuinely turned around. Both flows are good
//              matches pointing the same way, and the residual is the
//              largest, most REAL acceleration in the scene.
//
// A magnitude ratio drives toward 1 in both, so it discarded the signal
// exactly where it was strongest -- the fingerprint being that the gain FELL
// as acceleration rose, when the model should help more. Round-trip
// consistency separates them cleanly, because a reversal round-trips
// perfectly and an occlusion cannot. Judge the answer's provenance, not its
// size. Worth up to +4.4 dB. Thresholds in px of round-trip error; swept.
const float ACCEL_TRUST_LO = 2.0;
const float ACCEL_TRUST_HI = 5.0;

// DEADBAND on the acceleration used for the WARP -- deliberately not on the
// field the diagnostics report, because the two use cases want different
// things from the same number. A sensing consumer wants what was measured; an
// interpolator wants only what is safe to move pixels with.
//
// Why it is needed at all: sub-pixel refinement lifted the flow off the
// integer lattice, which is what made the field usable at low |a| -- but on
// content whose true acceleration is exactly zero the field still carries a
// heavy tail (measured on L7, constant velocity: median 0.000, p90 0.277,
// p99 3.914 px/interval^2). The correction acts on that tail and warps on
// noise. With sub-pixel enabled and no deadband it cost 0.82 dB on
// L1_trans_8px beyond the warp's own resampling cost.
//
// Expressed in px/interval^2 so it can be read against the calibration
// directly. Zero disables it.
//
// SWEPT, and 0.5/1.5 is the knee. On L1_trans_8px, where the true
// acceleration is exactly zero and the shader must be a no-op:
//
//   deadband      L1      O1      O2      O4      O5
//   off        56.16   49.65   46.17   47.35   34.03
//   0.25/0.75  58.21   49.62   46.17   47.35   34.03
//   0.5 /1.5   60.77   49.44   46.19   47.36   34.03
//   1.0 /2.5   61.35   49.06   46.16   47.33     --
//
// L1 climbs 5.2 dB across the sweep while the oscillation cases -- where the
// acceleration is real and the correction is earning its place -- move by
// hundredths until the widest setting finally costs O1 0.6 dB. 0.5/1.5 takes
// nearly all of the recovery for 0.21 dB of it.
//
// Against the pre-sub-pixel shader this is +3.31 dB on L1, which closes the
// -3.80 dB L1 regression that stood as the tridirectional shader's only
// losing case. Suppressing corrections below ~1 px/interval^2 costs at most
// a/8 ~ 0.12 px of placement error, which is not a visible amount.
const float ACCEL_DEADBAND_LO = 0.5;
const float ACCEL_DEADBAND_HI = 1.5;

// TRI_DIAG -- in-shader diagnostic output, for reading the estimator's
// internal fields without building a separate visualiser (tests/trivis.py is
// the full four-panel instrument).
//
//   0 = normal interpolated output
//   1 = the quadratic CORRECTION, i.e. how far this texel is being moved off
//       the constant-velocity straight line, in px
//   2 = the ACCELERATION field, in px per interval^2
//   3 = acceleration MAGNITUDE as a heat map, auto-scaled to ACCEL_DIAG_FS
//   4 = acceleration magnitude as LINEAR LUMA -- a measurement mode, so a
//       whole-frame average is proportional to mean |a|. No marker.
//
// Modes 1 and 2 encode a 2D vector the way tests/flowvis.py does: R and G
// carry the x and y components around a mid-grey zero, so mid-grey means
// "nothing here" and the hue tells you the direction. Mode 3 discards
// direction and shows only magnitude, which is easier to read when the
// question is "is there any acceleration in this shot at all".
//
// A MODE MARKER is burned into the top-left corner whenever TRI_DIAG is
// non-zero: a solid colour block, one colour per mode. It exists because the
// honest failure mode of these diagnostics is a screen of near-uniform
// mid-grey that looks identical to "the switch did nothing" -- and on real
// footage that is the COMMON case, since ordinary camera motion carries far
// less acceleration than the synthetic ladder does. With the marker, "mode is
// active but the field is near zero" and "my edit did not take effect" stop
// looking the same.
int TRI_DIAG = (read_view == 1 || read_view == 4) ? 7 : (read_view == 2 || read_view == 5) ? 2 : 2;

// Full-scale values for the diagnostic encodings, in real units, so a reader
// can convert a pixel back to a number rather than guess.
//
// These are deliberately far more sensitive than the synthetic ladder needs.
// The ladder reaches 13 px/interval^2; ordinary camera motion is one to two
// orders of magnitude below that, and the first version of these constants
// was calibrated on the ladder and rendered real footage invisible -- mode 1
// deviated by ONE level out of 255. Set for the content you are looking at:
// raise for synthetic tests, lower to see subtle real motion.
const float ACCEL_DIAG_FS = 2.0;   // px/interval^2 at full scale (modes 2, 3)
const float CORR_DIAG_FS  = 0.25;  // px of correction at full scale (mode 1)

// Mode marker: a solid block in the top-left corner, 24px square.
vec4 tri_diag_marker() {
    if (TRI_DIAG == 1) return vec4(1.0, 0.2, 0.2, 1.0);   // red   -- correction
    if (TRI_DIAG == 2) return vec4(0.2, 0.6, 1.0, 1.0);   // blue  -- acceleration
    return vec4(0.2, 1.0, 0.3, 1.0);                      // green -- magnitude
}

vec4 hook() {
    // ---- roles, derived per output frame from slot-keyed fields ----
    // rts_mix[1] > 0 means slot 1 is still in the future, so the output sits
    // in the FIRST interval (slots 0-1). Otherwise it sits in the second.
    bool first_half = rts_mix[1] > 0.0;

    float tA = first_half ? rts_mix[0] : rts_mix[1];
    float tB = first_half ? rts_mix[1] : rts_mix[2];
    float L  = tB - tA;                       // straddle interval, > 0
    float s  = clamp((0.0 - tA) / L, 0.0, 1.0);

    // Straddling flow: slots 0-1 or slots 1-2.
    vec2 f_fwd = (first_half ? FLOW_H_AB_tex(HOOKED_pos).xy
                             : FLOW_H_BC_tex(HOOKED_pos).xy) * 2.0 * HOOKED_pt;

    // Cut inside the straddling pair: reproduce the cut (base behaviour).
    float cut_straddle = first_half ? SCENE_DIFF_tex(vec2(0.5)).r
                                    : SCENE_DIFF_BC_tex(vec2(0.5)).r;
    if (cut_straddle > SCENE_CUT_DIFF) {
        if (first_half)
            return s < 0.5 ? HOOKED_tex(HOOKED_pos) : FRAME1_tex(HOOKED_pos);
        return s < 0.5 ? FRAME1_tex(HOOKED_pos) : FRAME2_tex(HOOKED_pos);
    }

    // ---- acceleration: the anchor is ALWAYS slot 1 ----
    // Whichever half the output sits in, slot 1 is the frame with two
    // outgoing flows inside the window, so the solve has no phase
    // dependence at all. f10 and f12 are its flows toward slots 0 and 2.
    vec2 f10 = FLOW_F_BA_tex(HOOKED_pos).xy * HOOKED_pt;
    vec2 f12 = FLOW_F_BC_tex(HOOKED_pos).xy * HOOKED_pt;

    // Quadratic through slot 1's three sampled positions, in units of the
    // straddle interval. For uniform spacing tau0 = -1 and tau2 = +1, and
    // this reduces to a = f10 + f12: the two flows cancel under constant
    // velocity and whatever survives IS the acceleration. Written out in
    // full so non-uniform (VFR) spacing is exact rather than assumed away.
    float tau0 = (rts_mix[0] - rts_mix[1]) / L;
    float tau2 = (rts_mix[2] - rts_mix[1]) / L;
    vec2 accel = 2.0 * (f12 * tau0 - f10 * tau2)
               / (tau2 * tau0 * (tau2 - tau0));

    // A cut between slot 1 and the far slot does not stop the straddling
    // pair being blendable -- it only makes the acceleration meaningless. So
    // zero it and degrade exactly to bidirectional, rather than cutting.
    float cut_far = first_half ? SCENE_DIFF_BC_tex(vec2(0.5)).r
                               : SCENE_DIFF_tex(vec2(0.5)).r;
    if (cut_far > SCENE_CUT_DIFF)
        accel = vec2(0.0);

    // ---- confidence: round-trip BOTH of the anchor's flows ----
    // Follow each flow out and back. Content visible in both frames lands
    // where it started; occluded content does not. Both are checked at slot
    // 1's own grid, and the worse of the two decides -- a texel has to
    // survive both to be believed, because the acceleration is built from
    // both and either being wrong is enough to ruin it.
    vec2 r10 = FLOW_F_AB_tex(HOOKED_pos + f10).xy * HOOKED_pt;
    float rt10 = length(f10 + r10) / length(HOOKED_pt);

    vec2 r12 = FLOW_F_CB_tex(HOOKED_pos + f12).xy * HOOKED_pt;
    float rt12 = length(f12 + r12) / length(HOOKED_pt);

    accel *= 1.0 - smoothstep(ACCEL_TRUST_LO, ACCEL_TRUST_HI, max(rt10, rt12));

    // NO SPANNING slot-0 -> slot-2 TEST, and this is a proof rather than an
    // omission. It was built (6 passes) and measured, on the reasoning that
    // the triangle identity d01 + d12 == d02 checks the measurements against
    // each other. Count the degrees of freedom: three frames give TWO unknown
    // displacements and THREE measurements, so exactly ONE redundancy -- and
    // the identity spends it constraining the SUM. Acceleration is the
    // DIFFERENCE. Orthogonal, so the constraint cannot touch it. A
    // common-mode error, which is what a moving edge produces, is invisible
    // to it by construction. Measured: weighting that residual 20x recovered
    // 0.09 dB on L1 while costing 2.59 dB on O2 -- anti-correlated with its
    // purpose. Validating acceleration needs a FOURTH frame; see
    // TRIDIRECTIONAL.md.

    vec2 amax = ACCEL_MAX_PX * HOOKED_pt;
    accel = clamp(accel, -amax, amax);

    // ---- quadratic placement: linear warp plus the s(1-s) correction ----
    // The warp's copy of the acceleration, deadbanded; `accel` itself is left
    // alone so TRI_DIAG still reports the measurement rather than the gate.
    vec2 accel_w = accel;
    if (ACCEL_DEADBAND_HI > 0.0)
        accel_w *= smoothstep(ACCEL_DEADBAND_LO, ACCEL_DEADBAND_HI,
                              length(accel / HOOKED_pt));

    vec2 corr = 0.5 * accel_w * s * (1.0 - s);

    if (TRI_DIAG != 0) {
        // Mode 4 is a MEASUREMENT mode, not an eyeball mode: |a| as linear
        // luma, so a whole-frame average is directly proportional to the mean
        // acceleration in the frame and the field can be reduced to one
        // number per frame by signalstats. No marker, deliberately -- a
        // 24x24 patch would bias that average, and nothing downstream is
        // looking at it by eye.
        if (TRI_DIAG == 4)
            return vec4(vec3(clamp(length(accel / HOOKED_pt) / ACCEL_DIAG_FS,
                                   0.0, 1.0)), 1.0);

        // Mode marker first, so an active-but-empty diagnostic is never
        // mistaken for an edit that did not take effect.

        if (TRI_DIAG == 1)
            return vec4(corr / HOOKED_pt, 0.0, 1.0);
        if (TRI_DIAG == 7)
            return vec4(f_fwd / HOOKED_pt, 0.0, 1.0);
        if (TRI_DIAG == 2)
            return vec4(accel / HOOKED_pt, 0.0, 1.0);

        // Mode 3: magnitude only, blue -> cyan -> red across 0..ACCEL_DIAG_FS.
        float m = clamp(length(accel / HOOKED_pt) / ACCEL_DIAG_FS, 0.0, 1.0);
        vec3 c = m < 0.5 ? mix(vec3(0.0, 0.0, 0.25), vec3(0.0, 0.9, 0.9), m * 2.0)
                         : mix(vec3(0.0, 0.9, 0.9), vec3(1.0, 0.1, 0.0), (m - 0.5) * 2.0);
        return vec4(c, 1.0);
    }

    vec2 uv_a = HOOKED_pos - f_fwd * s + corr;
    vec2 uv_b = HOOKED_pos + f_fwd * (1.0 - s) + corr;

    vec4 sa = first_half ? HOOKED_tex(uv_a) : FRAME1_tex(uv_a);
    vec4 sb = first_half ? FRAME1_tex(uv_b) : FRAME2_tex(uv_b);

    // Snap gate, inert at SNAP_STRENGTH 0.0 but kept in lockstep with the
    // base. EDGE_A/EDGE_B are pinned to slots 0-1 (see their passes).
    vec2 sa_uv = snap_texel(uv_a, HOOKED_size);
    vec2 sb_uv = snap_texel(uv_b, HOOKED_size);
    float ea = edge_consistency(EDGE_A_tex(uv_a).r, EDGE_A_tex(sa_uv).r);
    float eb = edge_consistency(EDGE_B_tex(uv_b).r, EDGE_B_tex(sb_uv).r);
    sa = mix(sa, first_half ? HOOKED_tex(sa_uv) : FRAME1_tex(sa_uv),
             SNAP_STRENGTH * ea);
    sb = mix(sb, first_half ? FRAME1_tex(sb_uv) : FRAME2_tex(sb_uv),
             SNAP_STRENGTH * eb);

    return mix(sa, sb, s);
}

//!TEXTURE READ_ACC
//!SIZE 480 270
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND READ_FIELD
//!BIND READ_ACC
//!SAVE READ_POOL
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!WHEN read_view 0 >
//!DESC [reading] 13x13 pool at 8 px spacing, then an exponential memory across frames

// Measured on the Metal demo (2026-09-01): pooling +/-48 px drops the
// static-background p95 from 0.52 to 0.10 px; the memory lifts a mover's
// direction coherence from 0.74 to 0.92. READ_EMA_ALPHA is per OUTPUT
// frame; 1.0 = no memory (frame-by-frame reading: fast oscillators average
// toward zero under any memory).
const float READ_EMA_ALPHA = 0.12;
const int   READ_POOL_R    = 6;

vec4 hook() {
    ivec2 coord = ivec2(READ_FIELD_pos * READ_FIELD_size);
    vec2 fpx = vec2(0.0);
    for (int j = -READ_POOL_R; j <= READ_POOL_R; j++)
        for (int i = -READ_POOL_R; i <= READ_POOL_R; i++)
            fpx += READ_FIELD_tex(READ_FIELD_pos + vec2(float(i), float(j)) * READ_FIELD_pt).xy;
    fpx /= float((2 * READ_POOL_R + 1) * (2 * READ_POOL_R + 1));
    vec2 prev = imageLoad(READ_ACC, coord).xy;
    vec2 acc = mix(prev, fpx, READ_EMA_ALPHA);
    imageStore(READ_ACC, coord, vec4(acc, 0.0, 1.0));
    return vec4(acc, 0.0, 1.0);
}

//!HOOK FRAME_MIX
//!BIND FRAME_MIX
//!BIND READ_FIELD
//!BIND READ_POOL
//!SAVE FRAME_MIX
//!WIDTH FRAME_MIX.w
//!HEIGHT FRAME_MIX.h
//!WHEN read_view 0 >
//!DESC [reading] paint the field over the picture (modes 1-3) or emit it raw for a machine (modes 4-6)

// three-frame family: velocity (the straddle flow) and acceleration from this shader's own stencil; it has no jerk, so modes 3 and 6 read acceleration
// Gates in px per interval (velocity) or px per interval^2 / ^3
// (acceleration, jerk): below _LO nothing is drawn, full colour at _SAT.
// The demo's measured values at 1280 wide; at 1920 the acceleration and
// jerk gates admit some speckle in foliage (doubling them clears most).
const float READ_VEL_LO  = 1.0,  READ_VEL_HI  = 2.0,  READ_VEL_SAT  = 3.0;
const float READ_ACC_LO  = 0.12, READ_ACC_HI  = 0.22, READ_ACC_SAT  = 0.30;
// READ_GATE 1: visibility needs the UNPOOLED field to move within READ_GATE_R
// texels of 1/8 res (2 = 16 px, the tracker's own reach), so the pool cannot
// paint further than the tracker itself moved. Measured on a 100 px square:
// painted area 4.05x the object without it, 2.86x with it, 94% covered.
const int   READ_GATE     = 1;
const int   READ_GATE_R   = 2;
const float READ_PICTURE_LUMA = 0.35;
// machine modes: 0.5 + px / (2 * FS), one full scale per field
const float READ_MACHINE_FS_VEL = 32.0;
const float READ_MACHINE_FS_ACC = 2.0;
const float READ_MACHINE_FS_JERK = 2.0;

vec3 read_hsv2rgb(vec3 c) {
    vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
    return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
}

vec4 hook() {
    bool vel = (read_view == 1 || read_view == 4);
    if (read_view >= 4) {
        float fs = (read_view == 4) ? READ_MACHINE_FS_VEL : (read_view == 5) ? READ_MACHINE_FS_ACC : READ_MACHINE_FS_JERK;
        vec2 f = READ_FIELD_tex(FRAME_MIX_pos).xy;
        return vec4(0.5 + f * (0.5 / fs), 0.5, 1.0);
    }
    float lo  = vel ? READ_VEL_LO  : READ_ACC_LO;
    float hi  = vel ? READ_VEL_HI  : READ_ACC_HI;
    float sat_full = vel ? READ_VEL_SAT : READ_ACC_SAT;
    vec2 uv = FRAME_MIX_pos;
    // 4-tap soften: the pooled field keeps a faint per-texel checker that would dither the gate
    vec2 fpx = vec2(0.0);
    fpx += READ_POOL_tex(uv + vec2( 2.0,  2.0) * FRAME_MIX_pt).xy;
    fpx += READ_POOL_tex(uv + vec2(-2.0,  2.0) * FRAME_MIX_pt).xy;
    fpx += READ_POOL_tex(uv + vec2( 2.0, -2.0) * FRAME_MIX_pt).xy;
    fpx += READ_POOL_tex(uv + vec2(-2.0, -2.0) * FRAME_MIX_pt).xy;
    fpx *= 0.25;
    float mag = length(fpx);
    float vis = smoothstep(lo, hi, mag) * 0.9;
    if (READ_GATE == 1) {
        float rawmag = 0.0;
        for (int j = -READ_GATE_R; j <= READ_GATE_R; j++)
            for (int i = -READ_GATE_R; i <= READ_GATE_R; i++)
                rawmag = max(rawmag, length(READ_FIELD_tex(uv + vec2(float(i), float(j)) * READ_FIELD_pt).xy));
        vis *= smoothstep(0.5 * lo, lo, rawmag);
    }
    vec2 bpx = min(uv, 1.0 - uv) * FRAME_MIX_size;
    vis *= smoothstep(4.0, 28.0, min(bpx.x, bpx.y));
    float sat = 0.95 * smoothstep(lo, sat_full, mag);
    // screen space, +y down: red = moving right, cyan = left, purple/blue = down, yellow-green = up
    float hue = fract(atan(fpx.y, fpx.x) / (2.0 * 3.14159265) + 1.0);
    vec4 pic = FRAME_MIX_tex(FRAME_MIX_pos);
    float lum = dot(pic.rgb, vec3(0.2126, 0.7152, 0.0722));
    vec3 reading = mix(vec3(lum * READ_PICTURE_LUMA), read_hsv2rgb(vec3(hue, sat, 1.0)), vis);
    return vec4(reading, pic.a);
}
