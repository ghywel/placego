// =====================================================================
// GENERATED FILE -- DO NOT EDIT BY HAND.
//
// Produced by scripts/tests/gen_quaddirectional.py from
// bidirectional-interpolation-seeded.glsl. Edit the base (shared machinery) or
// the generator (everything [quad]-tagged) and regenerate:
//
//   ./tests/gen_quaddirectional.py quaddirectional-interpolation-seeded.glsl bidirectional-interpolation-seeded.glsl
//
// QUADDIRECTIONAL INTERPOLATION -- the four-frame experiment. Binds the
// contiguous four-frame window around each output, computes all six
// adjacent-slot flows, composes the two-interval flow from its links,
// and fits one degree higher than the tridirectional shader: an exact
// cubic (QUAD_MODE 0 -- velocity, acceleration AND JERK) or an
// overdetermined quadratic whose least-squares residual is a per-texel
// measured confidence (QUAD_MODE 1). Pre-registered NOT to change the
// N:N acceleration field on smooth content -- the centred pair is
// jerk-immune -- and to add instead the jerk field, the confidence
// field, and cubic placement at 24->60. With zero acceleration and jerk
// it degenerates exactly to the bidirectional shader. Hypothesis,
// algebra, pre-registrations and results: QUADDIRECTIONAL.md.
// =====================================================================

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!BIND FRAME3
//!SAVE LUMA_A_S
//!WIDTH HOOKED.w 16 /
//!HEIGHT HOOKED.h 16 /
//!COMPONENTS 1
//!DESC [quad] downsample slot 0 to 1/16 res (luma)
vec4 hook() {
    return vec4(dot(HOOKED_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!BIND FRAME3
//!SAVE LUMA_B_S
//!WIDTH HOOKED.w 16 /
//!HEIGHT HOOKED.h 16 /
//!COMPONENTS 1
//!DESC [quad] downsample slot 1 to 1/16 res (luma)
vec4 hook() {
    return vec4(dot(FRAME1_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!BIND FRAME3
//!SAVE LUMA_C_S
//!WIDTH HOOKED.w 16 /
//!HEIGHT HOOKED.h 16 /
//!COMPONENTS 1
//!DESC [quad] downsample slot 2 to 1/16 res (luma)
vec4 hook() {
    return vec4(dot(FRAME2_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!BIND FRAME3
//!SAVE LUMA_D_S
//!WIDTH HOOKED.w 16 /
//!HEIGHT HOOKED.h 16 /
//!COMPONENTS 1
//!DESC [quad] downsample slot 3 to 1/16 res (luma)
vec4 hook() {
    return vec4(dot(FRAME3_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
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
//!DESC [quad] scene-cut statistic, slots 0-1
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
//!DESC [quad] scene-cut statistic, slots 1-2
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

//!HOOK FRAME_MIX
//!BIND LUMA_C_S
//!BIND LUMA_D_S
//!SAVE SCENE_DIFF_CD
//!WIDTH 1
//!HEIGHT 1
//!COMPONENTS 1
//!DESC [quad] scene-cut statistic, slots 2-3
vec4 hook() {
    const int N = 24;
    float acc = 0.0;
    for (int y = 0; y < N; y++) {
        for (int x = 0; x < N; x++) {
            vec2 uv = (vec2(float(x), float(y)) + 0.5) / float(N);
            acc += abs(LUMA_C_S_tex(uv).r - LUMA_D_S_tex(uv).r);
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

//!TEXTURE FLOW_S_AB_CACHE2
//!SIZE 240 135
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_S_AB_CACHE
//!BIND FLOW_S_AB_CACHE2
//!BIND LUMA_A_S
//!BIND LUMA_B_S
//!SAVE FLOW_S_AB
//!WIDTH HOOKED.w 16 /
//!HEIGHT HOOKED.h 16 /
//!COMPONENTS 4
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

vec2 descend_s(vec2 uv, vec2 start, out float best_cost) {
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
    vec2 best_off = start;
    best_cost = sad5x5_s(uv, uv + start) + REG_LAMBDA * length(start / LUMA_A_S_pt);
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
                float cost = sad5x5_s(uv, uv + off)
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
    return best_off;
}
vec4 hook() {
    ivec2 coord = ivec2(LUMA_A_S_pos * LUMA_A_S_size);
    if (!pair_changed)
        return imageLoad(FLOW_S_AB_CACHE, coord);

    vec2 uv_a = LUMA_A_S_pos;
    vec2 prev_s = imageLoad(FLOW_S_AB_CACHE, coord).xy * LUMA_A_S_pt;

    if (local_contrast_5x5_s(uv_a) < MIN_CONTRAST) {
        vec4 result = vec4(0.0);
        imageStore(FLOW_S_AB_CACHE, coord, result);
        imageStore(FLOW_S_AB_CACHE2, coord, result);
        return result;
    }

    // ---- three descents (scratch: twoseed4.py) ----
    float cost_a, cost_b, cost_c;
    vec2 off_a = descend_s(uv_a, vec2(0.0), cost_a);
    vec2 start_b = vec2(0.0);
    float best_ring = 1.0e30;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 o = vec2(float(x), float(y)) * LUMA_A_S_pt;
            if (length((o - off_a) / LUMA_A_S_pt) < 0.75)
                continue;
            float c = sad5x5_s(uv_a, uv_a + o) + REG_LAMBDA * length(o / LUMA_A_S_pt);
            if (c < best_ring) {
                best_ring = c;
                start_b = o;
            }
        }
    }
    vec2 off_b = descend_s(uv_a, start_b, cost_b);
    vec2 off_c = descend_s(uv_a, prev_s, cost_c);
    imageStore(FLOW_S_AB_CACHE2, coord, vec4(off_c / LUMA_A_S_pt, 0.0, 0.0));
    vec4 result = vec4(off_a / LUMA_A_S_pt, off_b / LUMA_A_S_pt);
    imageStore(FLOW_S_AB_CACHE, coord, result);
    return result;
}

//!TEXTURE FLOW_S_BA_CACHE
//!SIZE 240 135
//!FORMAT rgba32f
//!STORAGE

//!TEXTURE FLOW_S_BA_CACHE2
//!SIZE 240 135
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_S_BA_CACHE
//!BIND FLOW_S_BA_CACHE2
//!BIND LUMA_A_S
//!BIND LUMA_B_S
//!SAVE FLOW_S_BA
//!WIDTH HOOKED.w 16 /
//!HEIGHT HOOKED.h 16 /
//!COMPONENTS 4
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

vec2 descend_s(vec2 uv, vec2 start, out float best_cost) {
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
    vec2 best_off = start;
    best_cost = sad5x5_s2(uv, uv + start) + REG_LAMBDA * length(start / LUMA_A_S_pt);
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
                float cost = sad5x5_s2(uv, uv + off)
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
    return best_off;
}
vec4 hook() {
    ivec2 coord = ivec2(LUMA_B_S_pos * LUMA_B_S_size);
    if (!pair_changed)
        return imageLoad(FLOW_S_BA_CACHE, coord);

    vec2 uv_b = LUMA_B_S_pos;
    vec2 prev_s = imageLoad(FLOW_S_BA_CACHE, coord).xy * LUMA_A_S_pt;

    if (local_contrast_5x5_s2(uv_b) < MIN_CONTRAST) {
        vec4 result = vec4(0.0);
        imageStore(FLOW_S_BA_CACHE, coord, result);
        imageStore(FLOW_S_BA_CACHE2, coord, result);
        return result;
    }

    // ---- three descents (scratch: twoseed4.py) ----
    float cost_a, cost_b, cost_c;
    vec2 off_a = descend_s(uv_b, vec2(0.0), cost_a);
    vec2 start_b = vec2(0.0);
    float best_ring = 1.0e30;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 o = vec2(float(x), float(y)) * LUMA_A_S_pt;
            if (length((o - off_a) / LUMA_A_S_pt) < 0.75)
                continue;
            float c = sad5x5_s2(uv_b, uv_b + o) + REG_LAMBDA * length(o / LUMA_A_S_pt);
            if (c < best_ring) {
                best_ring = c;
                start_b = o;
            }
        }
    }
    vec2 off_b = descend_s(uv_b, start_b, cost_b);
    vec2 off_c = descend_s(uv_b, prev_s, cost_c);
    imageStore(FLOW_S_BA_CACHE2, coord, vec4(off_c / LUMA_A_S_pt, 0.0, 0.0));
    vec4 result = vec4(off_a / LUMA_A_S_pt, off_b / LUMA_A_S_pt);
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
//!BIND FRAME3
//!SAVE LUMA_A_E
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 1
//!DESC [quad] downsample slot 0 to 1/8 res (luma)
vec4 hook() {
    return vec4(dot(HOOKED_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!BIND FRAME3
//!SAVE LUMA_B_E
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 1
//!DESC [quad] downsample slot 1 to 1/8 res (luma)
vec4 hook() {
    return vec4(dot(FRAME1_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!BIND FRAME3
//!SAVE LUMA_C_E
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 1
//!DESC [quad] downsample slot 2 to 1/8 res (luma)
vec4 hook() {
    return vec4(dot(FRAME2_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!BIND FRAME3
//!SAVE LUMA_D_E
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 1
//!DESC [quad] downsample slot 3 to 1/8 res (luma)
vec4 hook() {
    return vec4(dot(FRAME3_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
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
//!BIND FLOW_S_AB_CACHE2
//!BIND FLOW_E_BA_CACHE
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

const int REFINE_SEARCH_RADIUS = 2;
const float REFINE_REG_LAMBDA = 0.05;
vec2 refine_e(vec2 uv, vec2 seed, out float sad_out) {
    const float TIE_MARGIN = 1.0e-4;
    vec2 best_off = seed;
    float best_cost = sad5x5_e(uv, uv + seed);
    for (int y = -REFINE_SEARCH_RADIUS; y <= REFINE_SEARCH_RADIUS; y++) {
        for (int x = -REFINE_SEARCH_RADIUS; x <= REFINE_SEARCH_RADIUS; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 off = seed + vec2(float(x), float(y)) * LUMA_A_E_pt;
            float cost = sad5x5_e(uv, uv + off)
                       + REFINE_REG_LAMBDA * length(vec2(float(x), float(y)));
            if (cost < best_cost * (1.0 - TIE_MARGIN)) {
                best_cost = cost;
                best_off = off;
            }
        }
    }
    sad_out = sad5x5_e(uv, uv + best_off);
    return best_off;
}
const float SEED_MAG_LAMBDA = 0.3;
const float SEED_TEMP_LAMBDA = 0.5;
const float SEED_RT_MAX = 1.0;   // E-texels; the previous flow must round-trip within this to be trusted
vec4 hook() {
    ivec2 coord = ivec2(LUMA_A_E_pos * LUMA_A_E_size);
    if (!pair_changed)
        return imageLoad(FLOW_E_AB_CACHE, coord);

    vec2 uv_a = LUMA_A_E_pos;
    vec4 seeds = FLOW_S_AB_tex(snap_texel(uv_a, FLOW_S_AB_size));
    vec2 base_off = seeds.xy * 2.0 * LUMA_A_E_pt;
    vec2 base_off2 = seeds.zw * 2.0 * LUMA_A_E_pt;

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
    // ---- refine three seeds; the temporal seed and prior only where the previous flow round-trips ----
    vec2 prev_e = imageLoad(FLOW_E_AB_CACHE, coord).xy * LUMA_A_E_pt;
    ivec2 rcoord = clamp(ivec2((uv_a + prev_e) * LUMA_A_E_size), ivec2(0), ivec2(LUMA_A_E_size) - 1);
    vec2 prev_rev = imageLoad(FLOW_E_BA_CACHE, rcoord).xy * LUMA_A_E_pt;
    float rt = length((prev_e + prev_rev) / LUMA_A_E_pt);
    bool trusted = rt < SEED_RT_MAX && length(prev_e) > 0.0;
    float tl = trusted ? SEED_TEMP_LAMBDA : 0.0;
    ivec2 scoord = ivec2(snap_texel(uv_a, FLOW_S_AB_size) * FLOW_S_AB_size);
    vec2 base_off3 = imageLoad(FLOW_S_AB_CACHE2, scoord).xy * 2.0 * LUMA_A_E_pt;
    float sad_a, sad_b, sad_c;
    vec2 ref_a = refine_e(uv_a, base_off, sad_a);
    vec2 ref_b = refine_e(uv_a, base_off2, sad_b);
    vec2 ref_c = refine_e(uv_a, base_off3, sad_c);
    float score_a = sad_a + SEED_MAG_LAMBDA * length(ref_a / LUMA_A_E_pt) + tl * length((ref_a - prev_e) / LUMA_A_E_pt);
    float score_b = sad_b + SEED_MAG_LAMBDA * length(ref_b / LUMA_A_E_pt) + tl * length((ref_b - prev_e) / LUMA_A_E_pt);
    float score_c = trusted ? sad_c + SEED_MAG_LAMBDA * length(ref_c / LUMA_A_E_pt) + tl * length((ref_c - prev_e) / LUMA_A_E_pt) : 1.0e30;
    const float TIE_MARGIN = 1.0e-4;
    vec2 best_off = ref_a;
    float best_score = score_a;
    if (score_b < best_score * (1.0 - TIE_MARGIN)) { best_off = ref_b; best_score = score_b; }
    if (score_c < best_score * (1.0 - TIE_MARGIN)) { best_off = ref_c; best_score = score_c; }
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
//!BIND FLOW_S_BA_CACHE2
//!BIND FLOW_E_AB_CACHE
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

const int REFINE_SEARCH_RADIUS = 2;
const float REFINE_REG_LAMBDA = 0.05;
vec2 refine_e(vec2 uv, vec2 seed, out float sad_out) {
    const float TIE_MARGIN = 1.0e-4;
    vec2 best_off = seed;
    float best_cost = sad5x5_e2(uv, uv + seed);
    for (int y = -REFINE_SEARCH_RADIUS; y <= REFINE_SEARCH_RADIUS; y++) {
        for (int x = -REFINE_SEARCH_RADIUS; x <= REFINE_SEARCH_RADIUS; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 off = seed + vec2(float(x), float(y)) * LUMA_A_E_pt;
            float cost = sad5x5_e2(uv, uv + off)
                       + REFINE_REG_LAMBDA * length(vec2(float(x), float(y)));
            if (cost < best_cost * (1.0 - TIE_MARGIN)) {
                best_cost = cost;
                best_off = off;
            }
        }
    }
    sad_out = sad5x5_e2(uv, uv + best_off);
    return best_off;
}
const float SEED_MAG_LAMBDA = 0.3;
const float SEED_TEMP_LAMBDA = 0.5;
const float SEED_RT_MAX = 1.0;   // E-texels; the previous flow must round-trip within this to be trusted
vec4 hook() {
    ivec2 coord = ivec2(LUMA_B_E_pos * LUMA_B_E_size);
    if (!pair_changed)
        return imageLoad(FLOW_E_BA_CACHE, coord);

    vec2 uv_b = LUMA_B_E_pos;
    vec4 seeds = FLOW_S_BA_tex(snap_texel(uv_b, FLOW_S_BA_size));
    vec2 base_off = seeds.xy * 2.0 * LUMA_A_E_pt;
    vec2 base_off2 = seeds.zw * 2.0 * LUMA_A_E_pt;

    if (local_contrast_5x5_e2(uv_b) < MIN_CONTRAST) {
        vec4 result = vec4(base_off / LUMA_A_E_pt, 0.0, 0.0);
        imageStore(FLOW_E_BA_CACHE, coord, result);
        return result;
    }

    // See REFINE_SEARCH_RADIUS/REFINE_REG_LAMBDA in the A->B pass above.
    // ---- refine three seeds; the temporal seed and prior only where the previous flow round-trips ----
    vec2 prev_e = imageLoad(FLOW_E_BA_CACHE, coord).xy * LUMA_A_E_pt;
    ivec2 rcoord = clamp(ivec2((uv_b + prev_e) * LUMA_A_E_size), ivec2(0), ivec2(LUMA_A_E_size) - 1);
    vec2 prev_rev = imageLoad(FLOW_E_AB_CACHE, rcoord).xy * LUMA_A_E_pt;
    float rt = length((prev_e + prev_rev) / LUMA_A_E_pt);
    bool trusted = rt < SEED_RT_MAX && length(prev_e) > 0.0;
    float tl = trusted ? SEED_TEMP_LAMBDA : 0.0;
    ivec2 scoord = ivec2(snap_texel(uv_b, FLOW_S_BA_size) * FLOW_S_BA_size);
    vec2 base_off3 = imageLoad(FLOW_S_BA_CACHE2, scoord).xy * 2.0 * LUMA_A_E_pt;
    float sad_a, sad_b, sad_c;
    vec2 ref_a = refine_e(uv_b, base_off, sad_a);
    vec2 ref_b = refine_e(uv_b, base_off2, sad_b);
    vec2 ref_c = refine_e(uv_b, base_off3, sad_c);
    float score_a = sad_a + SEED_MAG_LAMBDA * length(ref_a / LUMA_A_E_pt) + tl * length((ref_a - prev_e) / LUMA_A_E_pt);
    float score_b = sad_b + SEED_MAG_LAMBDA * length(ref_b / LUMA_A_E_pt) + tl * length((ref_b - prev_e) / LUMA_A_E_pt);
    float score_c = trusted ? sad_c + SEED_MAG_LAMBDA * length(ref_c / LUMA_A_E_pt) + tl * length((ref_c - prev_e) / LUMA_A_E_pt) : 1.0e30;
    const float TIE_MARGIN = 1.0e-4;
    vec2 best_off = ref_a;
    float best_score = score_a;
    if (score_b < best_score * (1.0 - TIE_MARGIN)) { best_off = ref_b; best_score = score_b; }
    if (score_c < best_score * (1.0 - TIE_MARGIN)) { best_off = ref_c; best_score = score_c; }
    vec4 result = vec4(best_off / LUMA_A_E_pt, 0.0, 0.0);
    imageStore(FLOW_E_BA_CACHE, coord, result);
    return result;
}

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!BIND FRAME3
//!SAVE LUMA_A_Q
//!WIDTH HOOKED.w 4 /
//!HEIGHT HOOKED.h 4 /
//!COMPONENTS 1
//!DESC [quad] downsample slot 0 to 1/4 res (luma)
vec4 hook() {
    return vec4(dot(HOOKED_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!BIND FRAME3
//!SAVE LUMA_B_Q
//!WIDTH HOOKED.w 4 /
//!HEIGHT HOOKED.h 4 /
//!COMPONENTS 1
//!DESC [quad] downsample slot 1 to 1/4 res (luma)
vec4 hook() {
    return vec4(dot(FRAME1_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!BIND FRAME3
//!SAVE LUMA_C_Q
//!WIDTH HOOKED.w 4 /
//!HEIGHT HOOKED.h 4 /
//!COMPONENTS 1
//!DESC [quad] downsample slot 2 to 1/4 res (luma)
vec4 hook() {
    return vec4(dot(FRAME2_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!BIND FRAME3
//!SAVE LUMA_D_Q
//!WIDTH HOOKED.w 4 /
//!HEIGHT HOOKED.h 4 /
//!COMPONENTS 1
//!DESC [quad] downsample slot 3 to 1/4 res (luma)
vec4 hook() {
    return vec4(dot(FRAME3_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
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
//!BIND FRAME3
//!SAVE LUMA_A_H
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 1
//!DESC [quad] downsample slot 0 to half res (luma)
vec4 hook() {
    return vec4(dot(HOOKED_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!BIND FRAME3
//!SAVE LUMA_B_H
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 1
//!DESC [quad] downsample slot 1 to half res (luma)
vec4 hook() {
    return vec4(dot(FRAME1_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!BIND FRAME3
//!SAVE LUMA_C_H
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 1
//!DESC [quad] downsample slot 2 to 1/2 res (luma)
vec4 hook() {
    return vec4(dot(FRAME2_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!BIND FRAME3
//!SAVE LUMA_D_H
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 1
//!DESC [quad] downsample slot 3 to 1/2 res (luma)
vec4 hook() {
    return vec4(dot(FRAME3_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
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

float sad3x3_h_self(vec2 uv, vec2 o) {
    float s = 0.0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 d = vec2(float(x), float(y)) * LUMA_A_H_pt;
            s += abs(LUMA_A_H_tex(uv + d).r - LUMA_A_H_tex(uv + o + d).r);
        }
    }
    return s;
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

    // SUBPEL_SELFREF: subtract the fit's own bias. For a PERFECT integer match the fit's vertex is
    // not zero: the 3x3 costs at -1 and +1 texel differ whenever the block spans a fraction of a
    // texture period, and the vertex moves with the block's phase -- a quarter-pixel floor locked
    // to the texture, the same at every speed, integer or fractional (NFRAME-LIMITS.md section 9).
    // That vertex is the fit of the reference block against ITSELF shifted, computable from one
    // frame; subtracting it makes the fit exact at integer shifts. Measured through the four-frame
    // shader: integer translation 0.33 -> 0.001 px median per-texel error, fractional 0.37 -> 0.13,
    // aperiodic texture unchanged, A4's per-texel acceleration spread 2.3x tighter, ladder +0.54 dB
    // mean over 32 cases with one loss (L1, the near-ceiling flat square, -4.7 dB at 74 dB), +2.4%
    // time. OFF here like SUBPEL_REFINE, for the same reason: this shader has no field to sharpen.
    // The generated field shaders turn both on.
    const int SUBPEL_SELFREF = 1;
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
        if (SUBPEL_SELFREF != 0) {
            float sxm = sad3x3_h_self(uv_a, -ex), sxp = sad3x3_h_self(uv_a, ex);
            float sym = sad3x3_h_self(uv_a, -ey), syp = sad3x3_h_self(uv_a, ey);
            float ddx = SUBPEL_FIT != 0 ? max(sxm, sxp) : sxm + sxp;
            float ddy = SUBPEL_FIT != 0 ? max(sym, syp) : sym + syp;
            vec2  bias0 = vec2(ddx > 1.0e-6 ? 0.5 * (sxm - sxp) / ddx : 0.0,
                               ddy > 1.0e-6 ? 0.5 * (sym - syp) / ddy : 0.0);
            sub = clamp(sub - bias0, -0.5, 0.5);
        }
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

float sad3x3_h2_self(vec2 uv, vec2 o) {
    float s = 0.0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 d = vec2(float(x), float(y)) * LUMA_A_H_pt;
            s += abs(LUMA_B_H_tex(uv + d).r - LUMA_B_H_tex(uv + o + d).r);
        }
    }
    return s;
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

    // SUBPEL_SELFREF: subtract the fit's own bias. For a PERFECT integer match the fit's vertex is
    // not zero: the 3x3 costs at -1 and +1 texel differ whenever the block spans a fraction of a
    // texture period, and the vertex moves with the block's phase -- a quarter-pixel floor locked
    // to the texture, the same at every speed, integer or fractional (NFRAME-LIMITS.md section 9).
    // That vertex is the fit of the reference block against ITSELF shifted, computable from one
    // frame; subtracting it makes the fit exact at integer shifts. Measured through the four-frame
    // shader: integer translation 0.33 -> 0.001 px median per-texel error, fractional 0.37 -> 0.13,
    // aperiodic texture unchanged, A4's per-texel acceleration spread 2.3x tighter, ladder +0.54 dB
    // mean over 32 cases with one loss (L1, the near-ceiling flat square, -4.7 dB at 74 dB), +2.4%
    // time. OFF here like SUBPEL_REFINE, for the same reason: this shader has no field to sharpen.
    // The generated field shaders turn both on.
    const int SUBPEL_SELFREF = 1;
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
        if (SUBPEL_SELFREF != 0) {
            float sxm = sad3x3_h2_self(uv_b, -ex), sxp = sad3x3_h2_self(uv_b, ex);
            float sym = sad3x3_h2_self(uv_b, -ey), syp = sad3x3_h2_self(uv_b, ey);
            float ddx = SUBPEL_FIT != 0 ? max(sxm, sxp) : sxm + sxp;
            float ddy = SUBPEL_FIT != 0 ? max(sym, syp) : sym + syp;
            vec2  bias0 = vec2(ddx > 1.0e-6 ? 0.5 * (sxm - sxp) / ddx : 0.0,
                               ddy > 1.0e-6 ? 0.5 * (sym - syp) / ddy : 0.0);
            sub = clamp(sub - bias0, -0.5, 0.5);
        }
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
// SLOT 1 -> SLOT 2 flow chain ([quad], generated). The base's slot-0 ->
// slot-1 chain with the luma pair shifted along by one -- identical to the
// tridirectional shader's chain, because it IS the same field.
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

//!TEXTURE FLOW_S_BC_CACHE2
//!SIZE 240 135
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_S_BC_CACHE
//!BIND FLOW_S_BC_CACHE2
//!BIND LUMA_A_S
//!BIND LUMA_B_S
//!BIND LUMA_C_S
//!SAVE FLOW_S_BC
//!WIDTH HOOKED.w 16 /
//!HEIGHT HOOKED.h 16 /
//!COMPONENTS 4
//!DESC [quad] coarse flow search slot1->slot2 (1/16 res)

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

vec2 descend_s(vec2 uv, vec2 start, out float best_cost) {
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
    vec2 best_off = start;
    best_cost = sad5x5_s(uv, uv + start) + REG_LAMBDA * length(start / LUMA_A_S_pt);
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
                float cost = sad5x5_s(uv, uv + off)
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
    return best_off;
}
vec4 hook() {
    ivec2 coord = ivec2(LUMA_A_S_pos * LUMA_A_S_size);
    if (!pair_changed)
        return imageLoad(FLOW_S_BC_CACHE, coord);

    vec2 uv_a = LUMA_A_S_pos;
    vec2 prev_s = imageLoad(FLOW_S_BC_CACHE, coord).xy * LUMA_A_S_pt;

    if (local_contrast_5x5_s(uv_a) < MIN_CONTRAST) {
        vec4 result = vec4(0.0);
        imageStore(FLOW_S_BC_CACHE, coord, result);
        imageStore(FLOW_S_BC_CACHE2, coord, result);
        return result;
    }

    // ---- three descents (scratch: twoseed4.py) ----
    float cost_a, cost_b, cost_c;
    vec2 off_a = descend_s(uv_a, vec2(0.0), cost_a);
    vec2 start_b = vec2(0.0);
    float best_ring = 1.0e30;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 o = vec2(float(x), float(y)) * LUMA_A_S_pt;
            if (length((o - off_a) / LUMA_A_S_pt) < 0.75)
                continue;
            float c = sad5x5_s(uv_a, uv_a + o) + REG_LAMBDA * length(o / LUMA_A_S_pt);
            if (c < best_ring) {
                best_ring = c;
                start_b = o;
            }
        }
    }
    vec2 off_b = descend_s(uv_a, start_b, cost_b);
    vec2 off_c = descend_s(uv_a, prev_s, cost_c);
    imageStore(FLOW_S_BC_CACHE2, coord, vec4(off_c / LUMA_A_S_pt, 0.0, 0.0));
    vec4 result = vec4(off_a / LUMA_A_S_pt, off_b / LUMA_A_S_pt);
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
//!BIND FLOW_S_BC_CACHE2
//!BIND FLOW_E_CB_CACHE
//!SAVE FLOW_E_BC
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 2
//!DESC [quad] refine flow slot1->slot2 (1/8 res)

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

const int REFINE_SEARCH_RADIUS = 2;
const float REFINE_REG_LAMBDA = 0.05;
vec2 refine_e(vec2 uv, vec2 seed, out float sad_out) {
    const float TIE_MARGIN = 1.0e-4;
    vec2 best_off = seed;
    float best_cost = sad5x5_e(uv, uv + seed);
    for (int y = -REFINE_SEARCH_RADIUS; y <= REFINE_SEARCH_RADIUS; y++) {
        for (int x = -REFINE_SEARCH_RADIUS; x <= REFINE_SEARCH_RADIUS; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 off = seed + vec2(float(x), float(y)) * LUMA_A_E_pt;
            float cost = sad5x5_e(uv, uv + off)
                       + REFINE_REG_LAMBDA * length(vec2(float(x), float(y)));
            if (cost < best_cost * (1.0 - TIE_MARGIN)) {
                best_cost = cost;
                best_off = off;
            }
        }
    }
    sad_out = sad5x5_e(uv, uv + best_off);
    return best_off;
}
const float SEED_MAG_LAMBDA = 0.3;
const float SEED_TEMP_LAMBDA = 0.5;
const float SEED_RT_MAX = 1.0;   // E-texels; the previous flow must round-trip within this to be trusted
vec4 hook() {
    ivec2 coord = ivec2(LUMA_A_E_pos * LUMA_A_E_size);
    if (!pair_changed)
        return imageLoad(FLOW_E_BC_CACHE, coord);

    vec2 uv_a = LUMA_A_E_pos;
    vec4 seeds = FLOW_S_BC_tex(snap_texel(uv_a, FLOW_S_BC_size));
    vec2 base_off = seeds.xy * 2.0 * LUMA_A_E_pt;
    vec2 base_off2 = seeds.zw * 2.0 * LUMA_A_E_pt;

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
    // ---- refine three seeds; the temporal seed and prior only where the previous flow round-trips ----
    vec2 prev_e = imageLoad(FLOW_E_BC_CACHE, coord).xy * LUMA_A_E_pt;
    ivec2 rcoord = clamp(ivec2((uv_a + prev_e) * LUMA_A_E_size), ivec2(0), ivec2(LUMA_A_E_size) - 1);
    vec2 prev_rev = imageLoad(FLOW_E_CB_CACHE, rcoord).xy * LUMA_A_E_pt;
    float rt = length((prev_e + prev_rev) / LUMA_A_E_pt);
    bool trusted = rt < SEED_RT_MAX && length(prev_e) > 0.0;
    float tl = trusted ? SEED_TEMP_LAMBDA : 0.0;
    ivec2 scoord = ivec2(snap_texel(uv_a, FLOW_S_BC_size) * FLOW_S_BC_size);
    vec2 base_off3 = imageLoad(FLOW_S_BC_CACHE2, scoord).xy * 2.0 * LUMA_A_E_pt;
    float sad_a, sad_b, sad_c;
    vec2 ref_a = refine_e(uv_a, base_off, sad_a);
    vec2 ref_b = refine_e(uv_a, base_off2, sad_b);
    vec2 ref_c = refine_e(uv_a, base_off3, sad_c);
    float score_a = sad_a + SEED_MAG_LAMBDA * length(ref_a / LUMA_A_E_pt) + tl * length((ref_a - prev_e) / LUMA_A_E_pt);
    float score_b = sad_b + SEED_MAG_LAMBDA * length(ref_b / LUMA_A_E_pt) + tl * length((ref_b - prev_e) / LUMA_A_E_pt);
    float score_c = trusted ? sad_c + SEED_MAG_LAMBDA * length(ref_c / LUMA_A_E_pt) + tl * length((ref_c - prev_e) / LUMA_A_E_pt) : 1.0e30;
    const float TIE_MARGIN = 1.0e-4;
    vec2 best_off = ref_a;
    float best_score = score_a;
    if (score_b < best_score * (1.0 - TIE_MARGIN)) { best_off = ref_b; best_score = score_b; }
    if (score_c < best_score * (1.0 - TIE_MARGIN)) { best_off = ref_c; best_score = score_c; }
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
//!DESC [quad] refine flow slot1->slot2 (1/4 res)

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
//!DESC [quad] refine flow slot1->slot2 (half res)

// Same seed-snapping fix as the two coarser handoffs above -- here for
// the Q->H handoff: FLOW_Q_BC's own texel is 4 full-res px, so an
// unsnapped bilinear read would smear a real boundary across ~4px in
// every direction (~8px total) when seeding this level.
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

float sad3x3_h_self(vec2 uv, vec2 o) {
    float s = 0.0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 d = vec2(float(x), float(y)) * LUMA_A_H_pt;
            s += abs(LUMA_B_H_tex(uv + d).r - LUMA_B_H_tex(uv + o + d).r);
        }
    }
    return s;
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

    // SUBPEL_SELFREF: subtract the fit's own bias. For a PERFECT integer match the fit's vertex is
    // not zero: the 3x3 costs at -1 and +1 texel differ whenever the block spans a fraction of a
    // texture period, and the vertex moves with the block's phase -- a quarter-pixel floor locked
    // to the texture, the same at every speed, integer or fractional (NFRAME-LIMITS.md section 9).
    // That vertex is the fit of the reference block against ITSELF shifted, computable from one
    // frame; subtracting it makes the fit exact at integer shifts. Measured through the four-frame
    // shader: integer translation 0.33 -> 0.001 px median per-texel error, fractional 0.37 -> 0.13,
    // aperiodic texture unchanged, A4's per-texel acceleration spread 2.3x tighter, ladder +0.54 dB
    // mean over 32 cases with one loss (L1, the near-ceiling flat square, -4.7 dB at 74 dB), +2.4%
    // time. OFF here like SUBPEL_REFINE, for the same reason: this shader has no field to sharpen.
    // The generated field shaders turn both on.
    const int SUBPEL_SELFREF = 1;
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
        if (SUBPEL_SELFREF != 0) {
            float sxm = sad3x3_h_self(uv_a, -ex), sxp = sad3x3_h_self(uv_a, ex);
            float sym = sad3x3_h_self(uv_a, -ey), syp = sad3x3_h_self(uv_a, ey);
            float ddx = SUBPEL_FIT != 0 ? max(sxm, sxp) : sxm + sxp;
            float ddy = SUBPEL_FIT != 0 ? max(sym, syp) : sym + syp;
            vec2  bias0 = vec2(ddx > 1.0e-6 ? 0.5 * (sxm - sxp) / ddx : 0.0,
                               ddy > 1.0e-6 ? 0.5 * (sym - syp) / ddy : 0.0);
            sub = clamp(sub - bias0, -0.5, 0.5);
        }
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
//!DESC [quad] vector median filter on flow slot1->slot2 (pass 1)
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
//!DESC [quad] vector median filter on flow slot1->slot2 (pass 2)
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
// SLOT 2 -> SLOT 1 flow chain ([quad], generated). Reverse of the above,
// for round-trip validation of the slot-1 anchor's forward flow and of
// slot 2's backward flow.
// =====================================================================


//!TEXTURE FLOW_S_CB_CACHE
//!SIZE 240 135
//!FORMAT rgba32f
//!STORAGE

//!TEXTURE FLOW_S_CB_CACHE2
//!SIZE 240 135
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_S_CB_CACHE
//!BIND FLOW_S_CB_CACHE2
//!BIND LUMA_A_S
//!BIND LUMA_B_S
//!BIND LUMA_C_S
//!SAVE FLOW_S_CB
//!WIDTH HOOKED.w 16 /
//!HEIGHT HOOKED.h 16 /
//!COMPONENTS 4
//!DESC [quad] coarse flow search slot2->slot1 (1/16 res)

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

vec2 descend_s(vec2 uv, vec2 start, out float best_cost) {
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
    vec2 best_off = start;
    best_cost = sad5x5_s2(uv, uv + start) + REG_LAMBDA * length(start / LUMA_A_S_pt);
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
                float cost = sad5x5_s2(uv, uv + off)
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
    return best_off;
}
vec4 hook() {
    ivec2 coord = ivec2(LUMA_B_S_pos * LUMA_B_S_size);
    if (!pair_changed)
        return imageLoad(FLOW_S_CB_CACHE, coord);

    vec2 uv_b = LUMA_B_S_pos;
    vec2 prev_s = imageLoad(FLOW_S_CB_CACHE, coord).xy * LUMA_A_S_pt;

    if (local_contrast_5x5_s2(uv_b) < MIN_CONTRAST) {
        vec4 result = vec4(0.0);
        imageStore(FLOW_S_CB_CACHE, coord, result);
        imageStore(FLOW_S_CB_CACHE2, coord, result);
        return result;
    }

    // ---- three descents (scratch: twoseed4.py) ----
    float cost_a, cost_b, cost_c;
    vec2 off_a = descend_s(uv_b, vec2(0.0), cost_a);
    vec2 start_b = vec2(0.0);
    float best_ring = 1.0e30;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 o = vec2(float(x), float(y)) * LUMA_A_S_pt;
            if (length((o - off_a) / LUMA_A_S_pt) < 0.75)
                continue;
            float c = sad5x5_s2(uv_b, uv_b + o) + REG_LAMBDA * length(o / LUMA_A_S_pt);
            if (c < best_ring) {
                best_ring = c;
                start_b = o;
            }
        }
    }
    vec2 off_b = descend_s(uv_b, start_b, cost_b);
    vec2 off_c = descend_s(uv_b, prev_s, cost_c);
    imageStore(FLOW_S_CB_CACHE2, coord, vec4(off_c / LUMA_A_S_pt, 0.0, 0.0));
    vec4 result = vec4(off_a / LUMA_A_S_pt, off_b / LUMA_A_S_pt);
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
//!BIND FLOW_S_CB_CACHE2
//!BIND FLOW_E_BC_CACHE
//!SAVE FLOW_E_CB
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 2
//!DESC [quad] refine flow slot2->slot1 (1/8 res)

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

const int REFINE_SEARCH_RADIUS = 2;
const float REFINE_REG_LAMBDA = 0.05;
vec2 refine_e(vec2 uv, vec2 seed, out float sad_out) {
    const float TIE_MARGIN = 1.0e-4;
    vec2 best_off = seed;
    float best_cost = sad5x5_e2(uv, uv + seed);
    for (int y = -REFINE_SEARCH_RADIUS; y <= REFINE_SEARCH_RADIUS; y++) {
        for (int x = -REFINE_SEARCH_RADIUS; x <= REFINE_SEARCH_RADIUS; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 off = seed + vec2(float(x), float(y)) * LUMA_A_E_pt;
            float cost = sad5x5_e2(uv, uv + off)
                       + REFINE_REG_LAMBDA * length(vec2(float(x), float(y)));
            if (cost < best_cost * (1.0 - TIE_MARGIN)) {
                best_cost = cost;
                best_off = off;
            }
        }
    }
    sad_out = sad5x5_e2(uv, uv + best_off);
    return best_off;
}
const float SEED_MAG_LAMBDA = 0.3;
const float SEED_TEMP_LAMBDA = 0.5;
const float SEED_RT_MAX = 1.0;   // E-texels; the previous flow must round-trip within this to be trusted
vec4 hook() {
    ivec2 coord = ivec2(LUMA_B_E_pos * LUMA_B_E_size);
    if (!pair_changed)
        return imageLoad(FLOW_E_CB_CACHE, coord);

    vec2 uv_b = LUMA_B_E_pos;
    vec4 seeds = FLOW_S_CB_tex(snap_texel(uv_b, FLOW_S_CB_size));
    vec2 base_off = seeds.xy * 2.0 * LUMA_A_E_pt;
    vec2 base_off2 = seeds.zw * 2.0 * LUMA_A_E_pt;

    if (local_contrast_5x5_e2(uv_b) < MIN_CONTRAST) {
        vec4 result = vec4(base_off / LUMA_A_E_pt, 0.0, 0.0);
        imageStore(FLOW_E_CB_CACHE, coord, result);
        return result;
    }

    // See REFINE_SEARCH_RADIUS/REFINE_REG_LAMBDA in the A->B pass above.
    // ---- refine three seeds; the temporal seed and prior only where the previous flow round-trips ----
    vec2 prev_e = imageLoad(FLOW_E_CB_CACHE, coord).xy * LUMA_A_E_pt;
    ivec2 rcoord = clamp(ivec2((uv_b + prev_e) * LUMA_A_E_size), ivec2(0), ivec2(LUMA_A_E_size) - 1);
    vec2 prev_rev = imageLoad(FLOW_E_BC_CACHE, rcoord).xy * LUMA_A_E_pt;
    float rt = length((prev_e + prev_rev) / LUMA_A_E_pt);
    bool trusted = rt < SEED_RT_MAX && length(prev_e) > 0.0;
    float tl = trusted ? SEED_TEMP_LAMBDA : 0.0;
    ivec2 scoord = ivec2(snap_texel(uv_b, FLOW_S_CB_size) * FLOW_S_CB_size);
    vec2 base_off3 = imageLoad(FLOW_S_CB_CACHE2, scoord).xy * 2.0 * LUMA_A_E_pt;
    float sad_a, sad_b, sad_c;
    vec2 ref_a = refine_e(uv_b, base_off, sad_a);
    vec2 ref_b = refine_e(uv_b, base_off2, sad_b);
    vec2 ref_c = refine_e(uv_b, base_off3, sad_c);
    float score_a = sad_a + SEED_MAG_LAMBDA * length(ref_a / LUMA_A_E_pt) + tl * length((ref_a - prev_e) / LUMA_A_E_pt);
    float score_b = sad_b + SEED_MAG_LAMBDA * length(ref_b / LUMA_A_E_pt) + tl * length((ref_b - prev_e) / LUMA_A_E_pt);
    float score_c = trusted ? sad_c + SEED_MAG_LAMBDA * length(ref_c / LUMA_A_E_pt) + tl * length((ref_c - prev_e) / LUMA_A_E_pt) : 1.0e30;
    const float TIE_MARGIN = 1.0e-4;
    vec2 best_off = ref_a;
    float best_score = score_a;
    if (score_b < best_score * (1.0 - TIE_MARGIN)) { best_off = ref_b; best_score = score_b; }
    if (score_c < best_score * (1.0 - TIE_MARGIN)) { best_off = ref_c; best_score = score_c; }
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
//!DESC [quad] refine flow slot2->slot1 (1/4 res)

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
//!DESC [quad] refine flow slot2->slot1 (half res)

// See snap_texel() in the A->B pass above.
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

float sad3x3_h2_self(vec2 uv, vec2 o) {
    float s = 0.0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 d = vec2(float(x), float(y)) * LUMA_A_H_pt;
            s += abs(LUMA_C_H_tex(uv + d).r - LUMA_C_H_tex(uv + o + d).r);
        }
    }
    return s;
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

    // SUBPEL_SELFREF: subtract the fit's own bias. For a PERFECT integer match the fit's vertex is
    // not zero: the 3x3 costs at -1 and +1 texel differ whenever the block spans a fraction of a
    // texture period, and the vertex moves with the block's phase -- a quarter-pixel floor locked
    // to the texture, the same at every speed, integer or fractional (NFRAME-LIMITS.md section 9).
    // That vertex is the fit of the reference block against ITSELF shifted, computable from one
    // frame; subtracting it makes the fit exact at integer shifts. Measured through the four-frame
    // shader: integer translation 0.33 -> 0.001 px median per-texel error, fractional 0.37 -> 0.13,
    // aperiodic texture unchanged, A4's per-texel acceleration spread 2.3x tighter, ladder +0.54 dB
    // mean over 32 cases with one loss (L1, the near-ceiling flat square, -4.7 dB at 74 dB), +2.4%
    // time. OFF here like SUBPEL_REFINE, for the same reason: this shader has no field to sharpen.
    // The generated field shaders turn both on.
    const int SUBPEL_SELFREF = 1;
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
        if (SUBPEL_SELFREF != 0) {
            float sxm = sad3x3_h2_self(uv_b, -ex), sxp = sad3x3_h2_self(uv_b, ex);
            float sym = sad3x3_h2_self(uv_b, -ey), syp = sad3x3_h2_self(uv_b, ey);
            float ddx = SUBPEL_FIT != 0 ? max(sxm, sxp) : sxm + sxp;
            float ddy = SUBPEL_FIT != 0 ? max(sym, syp) : sym + syp;
            vec2  bias0 = vec2(ddx > 1.0e-6 ? 0.5 * (sxm - sxp) / ddx : 0.0,
                               ddy > 1.0e-6 ? 0.5 * (sym - syp) / ddy : 0.0);
            sub = clamp(sub - bias0, -0.5, 0.5);
        }
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
//!DESC [quad] vector median filter on flow slot2->slot1 (pass 1)
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
//!DESC [quad] vector median filter on flow slot2->slot1 (pass 2)
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
// =====================================================================
// SLOT 2 -> SLOT 3 flow chain ([quad], generated). The pair the fourth
// frame adds. Also the second LINK of the composed two-interval flow
// F13(x) = F12(x) + F23(x + F12(x)) -- composition keeps every search
// inside its own one-interval reach, which a direct two-interval search
// would exit exactly on fast content.
// =====================================================================


// ---------------------------------------------------------------------
// Sixteenth-res coarse search, both directions: 5-step, 5x5 SAD window.
// Cached across repeated output frames sharing the same source pair --
// see the "Storage-based flow caching" note at the top of this file.
// ---------------------------------------------------------------------
//!TEXTURE FLOW_S_CD_CACHE
//!SIZE 240 135
//!FORMAT rgba32f
//!STORAGE

//!TEXTURE FLOW_S_CD_CACHE2
//!SIZE 240 135
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_S_CD_CACHE
//!BIND FLOW_S_CD_CACHE2
//!BIND LUMA_A_S
//!BIND LUMA_B_S
//!BIND LUMA_C_S
//!BIND LUMA_D_S
//!SAVE FLOW_S_CD
//!WIDTH HOOKED.w 16 /
//!HEIGHT HOOKED.h 16 /
//!COMPONENTS 4
//!DESC [quad] coarse flow search slot2->slot3 (1/16 res)

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
            s += abs(LUMA_C_S_tex(uv_a + o).r - LUMA_D_S_tex(uv_b + o).r);
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
            float v = LUMA_C_S_tex(uv_a + vec2(float(x), float(y)) * LUMA_A_S_pt).r;
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

vec2 descend_s(vec2 uv, vec2 start, out float best_cost) {
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
    vec2 best_off = start;
    best_cost = sad5x5_s(uv, uv + start) + REG_LAMBDA * length(start / LUMA_A_S_pt);
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
                float cost = sad5x5_s(uv, uv + off)
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
    return best_off;
}
vec4 hook() {
    ivec2 coord = ivec2(LUMA_A_S_pos * LUMA_A_S_size);
    if (!pair_changed)
        return imageLoad(FLOW_S_CD_CACHE, coord);

    vec2 uv_a = LUMA_A_S_pos;
    vec2 prev_s = imageLoad(FLOW_S_CD_CACHE, coord).xy * LUMA_A_S_pt;

    if (local_contrast_5x5_s(uv_a) < MIN_CONTRAST) {
        vec4 result = vec4(0.0);
        imageStore(FLOW_S_CD_CACHE, coord, result);
        imageStore(FLOW_S_CD_CACHE2, coord, result);
        return result;
    }

    // ---- three descents (scratch: twoseed4.py) ----
    float cost_a, cost_b, cost_c;
    vec2 off_a = descend_s(uv_a, vec2(0.0), cost_a);
    vec2 start_b = vec2(0.0);
    float best_ring = 1.0e30;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 o = vec2(float(x), float(y)) * LUMA_A_S_pt;
            if (length((o - off_a) / LUMA_A_S_pt) < 0.75)
                continue;
            float c = sad5x5_s(uv_a, uv_a + o) + REG_LAMBDA * length(o / LUMA_A_S_pt);
            if (c < best_ring) {
                best_ring = c;
                start_b = o;
            }
        }
    }
    vec2 off_b = descend_s(uv_a, start_b, cost_b);
    vec2 off_c = descend_s(uv_a, prev_s, cost_c);
    imageStore(FLOW_S_CD_CACHE2, coord, vec4(off_c / LUMA_A_S_pt, 0.0, 0.0));
    vec4 result = vec4(off_a / LUMA_A_S_pt, off_b / LUMA_A_S_pt);
    imageStore(FLOW_S_CD_CACHE, coord, result);
    return result;
}


//!TEXTURE FLOW_E_CD_CACHE
//!SIZE 480 270
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_E_CD_CACHE
//!BIND LUMA_A_E
//!BIND LUMA_B_E
//!BIND LUMA_C_E
//!BIND LUMA_D_E
//!BIND FLOW_S_CD
//!BIND FLOW_S_CD_CACHE2
//!BIND FLOW_E_DC_CACHE
//!SAVE FLOW_E_CD
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 2
//!DESC [quad] refine flow slot2->slot3 (1/8 res)

// Snaps to the exact center of whichever FLOW_S_CD texel this position
// falls in, before reading it as this level's search seed just below.
// An ordinary bilinear read here (as this used to be) blends between
// neighboring coarse-level vectors whenever the sample position isn't
// exactly on a coarse texel center -- which is most positions, since
// this level is 2x finer. At a real motion boundary, where one coarse
// texel holds the object's true motion and its neighbor holds ~zero,
// that blend produces a smooth gradient of in-between seed vectors
// spanning roughly one full FLOW_S_CD texel width in every direction --
// 16 full-res pixels each way at this handoff specifically -- entirely
// independent of how correct the underlying FLOW_S_CD values are.
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
            s += abs(LUMA_C_E_tex(uv_a + o).r - LUMA_D_E_tex(uv_b + o).r);
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
            float v = LUMA_C_E_tex(uv_a + vec2(float(x), float(y)) * LUMA_A_E_pt).r;
            lo = min(lo, v);
            hi = max(hi, v);
        }
    }
    return hi - lo;
}

const int REFINE_SEARCH_RADIUS = 2;
const float REFINE_REG_LAMBDA = 0.05;
vec2 refine_e(vec2 uv, vec2 seed, out float sad_out) {
    const float TIE_MARGIN = 1.0e-4;
    vec2 best_off = seed;
    float best_cost = sad5x5_e(uv, uv + seed);
    for (int y = -REFINE_SEARCH_RADIUS; y <= REFINE_SEARCH_RADIUS; y++) {
        for (int x = -REFINE_SEARCH_RADIUS; x <= REFINE_SEARCH_RADIUS; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 off = seed + vec2(float(x), float(y)) * LUMA_A_E_pt;
            float cost = sad5x5_e(uv, uv + off)
                       + REFINE_REG_LAMBDA * length(vec2(float(x), float(y)));
            if (cost < best_cost * (1.0 - TIE_MARGIN)) {
                best_cost = cost;
                best_off = off;
            }
        }
    }
    sad_out = sad5x5_e(uv, uv + best_off);
    return best_off;
}
const float SEED_MAG_LAMBDA = 0.3;
const float SEED_TEMP_LAMBDA = 0.5;
const float SEED_RT_MAX = 1.0;   // E-texels; the previous flow must round-trip within this to be trusted
vec4 hook() {
    ivec2 coord = ivec2(LUMA_A_E_pos * LUMA_A_E_size);
    if (!pair_changed)
        return imageLoad(FLOW_E_CD_CACHE, coord);

    vec2 uv_a = LUMA_A_E_pos;
    vec4 seeds = FLOW_S_CD_tex(snap_texel(uv_a, FLOW_S_CD_size));
    vec2 base_off = seeds.xy * 2.0 * LUMA_A_E_pt;
    vec2 base_off2 = seeds.zw * 2.0 * LUMA_A_E_pt;

    if (local_contrast_5x5_e(uv_a) < MIN_CONTRAST) {
        vec4 result = vec4(base_off / LUMA_A_E_pt, 0.0, 0.0);
        imageStore(FLOW_E_CD_CACHE, coord, result);
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
    // ---- refine three seeds; the temporal seed and prior only where the previous flow round-trips ----
    vec2 prev_e = imageLoad(FLOW_E_CD_CACHE, coord).xy * LUMA_A_E_pt;
    ivec2 rcoord = clamp(ivec2((uv_a + prev_e) * LUMA_A_E_size), ivec2(0), ivec2(LUMA_A_E_size) - 1);
    vec2 prev_rev = imageLoad(FLOW_E_DC_CACHE, rcoord).xy * LUMA_A_E_pt;
    float rt = length((prev_e + prev_rev) / LUMA_A_E_pt);
    bool trusted = rt < SEED_RT_MAX && length(prev_e) > 0.0;
    float tl = trusted ? SEED_TEMP_LAMBDA : 0.0;
    ivec2 scoord = ivec2(snap_texel(uv_a, FLOW_S_CD_size) * FLOW_S_CD_size);
    vec2 base_off3 = imageLoad(FLOW_S_CD_CACHE2, scoord).xy * 2.0 * LUMA_A_E_pt;
    float sad_a, sad_b, sad_c;
    vec2 ref_a = refine_e(uv_a, base_off, sad_a);
    vec2 ref_b = refine_e(uv_a, base_off2, sad_b);
    vec2 ref_c = refine_e(uv_a, base_off3, sad_c);
    float score_a = sad_a + SEED_MAG_LAMBDA * length(ref_a / LUMA_A_E_pt) + tl * length((ref_a - prev_e) / LUMA_A_E_pt);
    float score_b = sad_b + SEED_MAG_LAMBDA * length(ref_b / LUMA_A_E_pt) + tl * length((ref_b - prev_e) / LUMA_A_E_pt);
    float score_c = trusted ? sad_c + SEED_MAG_LAMBDA * length(ref_c / LUMA_A_E_pt) + tl * length((ref_c - prev_e) / LUMA_A_E_pt) : 1.0e30;
    const float TIE_MARGIN = 1.0e-4;
    vec2 best_off = ref_a;
    float best_score = score_a;
    if (score_b < best_score * (1.0 - TIE_MARGIN)) { best_off = ref_b; best_score = score_b; }
    if (score_c < best_score * (1.0 - TIE_MARGIN)) { best_off = ref_c; best_score = score_c; }
    vec4 result = vec4(best_off / LUMA_A_E_pt, 0.0, 0.0);
    imageStore(FLOW_E_CD_CACHE, coord, result);
    return result;
}


//!TEXTURE FLOW_Q_CD_CACHE
//!SIZE 960 540
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_Q_CD_CACHE
//!BIND LUMA_A_Q
//!BIND LUMA_B_Q
//!BIND LUMA_C_Q
//!BIND LUMA_D_Q
//!BIND FLOW_E_CD
//!SAVE FLOW_Q_CD
//!WIDTH HOOKED.w 4 /
//!HEIGHT HOOKED.h 4 /
//!COMPONENTS 2
//!DESC [quad] refine flow slot2->slot3 (1/4 res)

// Same seed-snapping fix as the S->E handoff above (see that pass for
// the full reasoning) -- here for the E->Q handoff: FLOW_E_CD's own
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
            s += abs(LUMA_C_Q_tex(uv_a + o).r - LUMA_D_Q_tex(uv_b + o).r);
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
            float v = LUMA_C_Q_tex(uv_a + vec2(float(x), float(y)) * LUMA_A_Q_pt).r;
            lo = min(lo, v);
            hi = max(hi, v);
        }
    }
    return hi - lo;
}

vec4 hook() {
    ivec2 coord = ivec2(LUMA_A_Q_pos * LUMA_A_Q_size);
    if (!pair_changed)
        return imageLoad(FLOW_Q_CD_CACHE, coord);

    vec2 uv_a = LUMA_A_Q_pos;
    vec2 base_off = FLOW_E_CD_tex(snap_texel(uv_a, FLOW_E_CD_size)).xy * 2.0 * LUMA_A_Q_pt;

    if (local_contrast_5x5_q(uv_a) < MIN_CONTRAST) {
        vec4 result = vec4(base_off / LUMA_A_Q_pt, 0.0, 0.0);
        imageStore(FLOW_Q_CD_CACHE, coord, result);
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
    imageStore(FLOW_Q_CD_CACHE, coord, result);
    return result;
}


//!TEXTURE FLOW_H_CD_CACHE
//!SIZE 1920 1080
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_H_CD_CACHE
//!BIND LUMA_A_H
//!BIND LUMA_B_H
//!BIND LUMA_C_H
//!BIND LUMA_D_H
//!BIND FLOW_Q_CD
//!SAVE FLOW_H_CD
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 2
//!DESC [quad] refine flow slot2->slot3 (half res)

// Same seed-snapping fix as the two coarser handoffs above -- here for
// the Q->H handoff: FLOW_Q_CD's own texel is 4 full-res px, so an
// unsnapped bilinear read would smear a real boundary across ~4px in
// every direction (~8px total) when seeding this level.
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

float sad3x3_h_self(vec2 uv, vec2 o) {
    float s = 0.0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 d = vec2(float(x), float(y)) * LUMA_A_H_pt;
            s += abs(LUMA_C_H_tex(uv + d).r - LUMA_C_H_tex(uv + o + d).r);
        }
    }
    return s;
}
float sad3x3_h(vec2 uv_a, vec2 uv_b) {
    float s = 0.0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 o = vec2(float(x), float(y)) * LUMA_A_H_pt;
            s += abs(LUMA_C_H_tex(uv_a + o).r - LUMA_D_H_tex(uv_b + o).r);
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
            float v = LUMA_C_H_tex(uv_a + vec2(float(x), float(y)) * LUMA_A_H_pt).r;
            lo = min(lo, v);
            hi = max(hi, v);
        }
    }
    return hi - lo;
}

vec4 hook() {
    ivec2 coord = ivec2(LUMA_A_H_pos * LUMA_A_H_size);
    if (!pair_changed)
        return imageLoad(FLOW_H_CD_CACHE, coord);

    vec2 uv_a = LUMA_A_H_pos;
    vec2 base_off = FLOW_Q_CD_tex(snap_texel(uv_a, FLOW_Q_CD_size)).xy * 2.0 * LUMA_A_H_pt;

    if (local_contrast_3x3_h(uv_a) < MIN_CONTRAST) {
        vec4 result = vec4(base_off / LUMA_A_H_pt, 0.0, 0.0);
        imageStore(FLOW_H_CD_CACHE, coord, result);
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

    // SUBPEL_SELFREF: subtract the fit's own bias. For a PERFECT integer match the fit's vertex is
    // not zero: the 3x3 costs at -1 and +1 texel differ whenever the block spans a fraction of a
    // texture period, and the vertex moves with the block's phase -- a quarter-pixel floor locked
    // to the texture, the same at every speed, integer or fractional (NFRAME-LIMITS.md section 9).
    // That vertex is the fit of the reference block against ITSELF shifted, computable from one
    // frame; subtracting it makes the fit exact at integer shifts. Measured through the four-frame
    // shader: integer translation 0.33 -> 0.001 px median per-texel error, fractional 0.37 -> 0.13,
    // aperiodic texture unchanged, A4's per-texel acceleration spread 2.3x tighter, ladder +0.54 dB
    // mean over 32 cases with one loss (L1, the near-ceiling flat square, -4.7 dB at 74 dB), +2.4%
    // time. OFF here like SUBPEL_REFINE, for the same reason: this shader has no field to sharpen.
    // The generated field shaders turn both on.
    const int SUBPEL_SELFREF = 1;
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
        if (SUBPEL_SELFREF != 0) {
            float sxm = sad3x3_h_self(uv_a, -ex), sxp = sad3x3_h_self(uv_a, ex);
            float sym = sad3x3_h_self(uv_a, -ey), syp = sad3x3_h_self(uv_a, ey);
            float ddx = SUBPEL_FIT != 0 ? max(sxm, sxp) : sxm + sxp;
            float ddy = SUBPEL_FIT != 0 ? max(sym, syp) : sym + syp;
            vec2  bias0 = vec2(ddx > 1.0e-6 ? 0.5 * (sxm - sxp) / ddx : 0.0,
                               ddy > 1.0e-6 ? 0.5 * (sym - syp) / ddy : 0.0);
            sub = clamp(sub - bias0, -0.5, 0.5);
        }
        best_off += sub * LUMA_A_H_pt;
    }
    vec4 result = vec4(best_off / LUMA_A_H_pt, 0.0, 0.0);
    imageStore(FLOW_H_CD_CACHE, coord, result);
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
//!BIND FLOW_H_CD
//!SAVE FLOW_H_CD
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 2
//!DESC [quad] vector median filter on flow slot2->slot3 (pass 1)
vec4 hook() {
    if (!pair_changed)
        return vec4(0.0);

    vec2 v[9];
    int n = 0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 o = vec2(float(x), float(y)) * FLOW_H_CD_pt;
            v[n++] = FLOW_H_CD_tex(FLOW_H_CD_pos + o).xy;
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
//!TEXTURE FLOW_H_CD_MEDIAN_CACHE
//!SIZE 1920 1080
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_H_CD_MEDIAN_CACHE
//!BIND FLOW_H_CD
//!SAVE FLOW_H_CD
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 2
//!DESC [quad] vector median filter on flow slot2->slot3 (pass 2)
vec4 hook() {
    ivec2 coord = ivec2(FLOW_H_CD_pos * FLOW_H_CD_size);
    if (!pair_changed)
        return imageLoad(FLOW_H_CD_MEDIAN_CACHE, coord);

    vec2 v[9];
    int n = 0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 o = vec2(float(x), float(y)) * FLOW_H_CD_pt;
            v[n++] = FLOW_H_CD_tex(FLOW_H_CD_pos + o).xy;
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
    imageStore(FLOW_H_CD_MEDIAN_CACHE, coord, result);
    return result;
}
// =====================================================================
// SLOT 3 -> SLOT 2 flow chain ([quad], generated). Reverse of the above,
// closing the round trip on the composed flow's second link. An unchecked
// link is indistinguishable from real jerk, which is the same lesson the
// tri shader learned about unchecked flows and acceleration.
// =====================================================================


//!TEXTURE FLOW_S_DC_CACHE
//!SIZE 240 135
//!FORMAT rgba32f
//!STORAGE

//!TEXTURE FLOW_S_DC_CACHE2
//!SIZE 240 135
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_S_DC_CACHE
//!BIND FLOW_S_DC_CACHE2
//!BIND LUMA_A_S
//!BIND LUMA_B_S
//!BIND LUMA_C_S
//!BIND LUMA_D_S
//!SAVE FLOW_S_DC
//!WIDTH HOOKED.w 16 /
//!HEIGHT HOOKED.h 16 /
//!COMPONENTS 4
//!DESC [quad] coarse flow search slot3->slot2 (1/16 res)

// See COARSE_WINDOW_RADIUS in the A->B pass above.
const int COARSE_WINDOW_RADIUS = 1;

float sad5x5_s2(vec2 uv_b, vec2 uv_a) {
    float s = 0.0;
    for (int y = -COARSE_WINDOW_RADIUS; y <= COARSE_WINDOW_RADIUS; y++) {
        for (int x = -COARSE_WINDOW_RADIUS; x <= COARSE_WINDOW_RADIUS; x++) {
            vec2 o = vec2(float(x), float(y)) * LUMA_A_S_pt;
            s += abs(LUMA_D_S_tex(uv_b + o).r - LUMA_C_S_tex(uv_a + o).r);
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
            float v = LUMA_D_S_tex(uv_b + vec2(float(x), float(y)) * LUMA_A_S_pt).r;
            lo = min(lo, v);
            hi = max(hi, v);
        }
    }
    return hi - lo;
}

const float REG_LAMBDA = 0.06;

vec2 descend_s(vec2 uv, vec2 start, out float best_cost) {
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
    vec2 best_off = start;
    best_cost = sad5x5_s2(uv, uv + start) + REG_LAMBDA * length(start / LUMA_A_S_pt);
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
                float cost = sad5x5_s2(uv, uv + off)
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
    return best_off;
}
vec4 hook() {
    ivec2 coord = ivec2(LUMA_B_S_pos * LUMA_B_S_size);
    if (!pair_changed)
        return imageLoad(FLOW_S_DC_CACHE, coord);

    vec2 uv_b = LUMA_B_S_pos;
    vec2 prev_s = imageLoad(FLOW_S_DC_CACHE, coord).xy * LUMA_A_S_pt;

    if (local_contrast_5x5_s2(uv_b) < MIN_CONTRAST) {
        vec4 result = vec4(0.0);
        imageStore(FLOW_S_DC_CACHE, coord, result);
        imageStore(FLOW_S_DC_CACHE2, coord, result);
        return result;
    }

    // ---- three descents (scratch: twoseed4.py) ----
    float cost_a, cost_b, cost_c;
    vec2 off_a = descend_s(uv_b, vec2(0.0), cost_a);
    vec2 start_b = vec2(0.0);
    float best_ring = 1.0e30;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 o = vec2(float(x), float(y)) * LUMA_A_S_pt;
            if (length((o - off_a) / LUMA_A_S_pt) < 0.75)
                continue;
            float c = sad5x5_s2(uv_b, uv_b + o) + REG_LAMBDA * length(o / LUMA_A_S_pt);
            if (c < best_ring) {
                best_ring = c;
                start_b = o;
            }
        }
    }
    vec2 off_b = descend_s(uv_b, start_b, cost_b);
    vec2 off_c = descend_s(uv_b, prev_s, cost_c);
    imageStore(FLOW_S_DC_CACHE2, coord, vec4(off_c / LUMA_A_S_pt, 0.0, 0.0));
    vec4 result = vec4(off_a / LUMA_A_S_pt, off_b / LUMA_A_S_pt);
    imageStore(FLOW_S_DC_CACHE, coord, result);
    return result;
}


//!TEXTURE FLOW_E_DC_CACHE
//!SIZE 480 270
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_E_DC_CACHE
//!BIND LUMA_A_E
//!BIND LUMA_B_E
//!BIND LUMA_C_E
//!BIND LUMA_D_E
//!BIND FLOW_S_DC
//!BIND FLOW_S_DC_CACHE2
//!BIND FLOW_E_CD_CACHE
//!SAVE FLOW_E_DC
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 2
//!DESC [quad] refine flow slot3->slot2 (1/8 res)

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
            s += abs(LUMA_D_E_tex(uv_b + o).r - LUMA_C_E_tex(uv_a + o).r);
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
            float v = LUMA_D_E_tex(uv_b + vec2(float(x), float(y)) * LUMA_A_E_pt).r;
            lo = min(lo, v);
            hi = max(hi, v);
        }
    }
    return hi - lo;
}

const int REFINE_SEARCH_RADIUS = 2;
const float REFINE_REG_LAMBDA = 0.05;
vec2 refine_e(vec2 uv, vec2 seed, out float sad_out) {
    const float TIE_MARGIN = 1.0e-4;
    vec2 best_off = seed;
    float best_cost = sad5x5_e2(uv, uv + seed);
    for (int y = -REFINE_SEARCH_RADIUS; y <= REFINE_SEARCH_RADIUS; y++) {
        for (int x = -REFINE_SEARCH_RADIUS; x <= REFINE_SEARCH_RADIUS; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 off = seed + vec2(float(x), float(y)) * LUMA_A_E_pt;
            float cost = sad5x5_e2(uv, uv + off)
                       + REFINE_REG_LAMBDA * length(vec2(float(x), float(y)));
            if (cost < best_cost * (1.0 - TIE_MARGIN)) {
                best_cost = cost;
                best_off = off;
            }
        }
    }
    sad_out = sad5x5_e2(uv, uv + best_off);
    return best_off;
}
const float SEED_MAG_LAMBDA = 0.3;
const float SEED_TEMP_LAMBDA = 0.5;
const float SEED_RT_MAX = 1.0;   // E-texels; the previous flow must round-trip within this to be trusted
vec4 hook() {
    ivec2 coord = ivec2(LUMA_B_E_pos * LUMA_B_E_size);
    if (!pair_changed)
        return imageLoad(FLOW_E_DC_CACHE, coord);

    vec2 uv_b = LUMA_B_E_pos;
    vec4 seeds = FLOW_S_DC_tex(snap_texel(uv_b, FLOW_S_DC_size));
    vec2 base_off = seeds.xy * 2.0 * LUMA_A_E_pt;
    vec2 base_off2 = seeds.zw * 2.0 * LUMA_A_E_pt;

    if (local_contrast_5x5_e2(uv_b) < MIN_CONTRAST) {
        vec4 result = vec4(base_off / LUMA_A_E_pt, 0.0, 0.0);
        imageStore(FLOW_E_DC_CACHE, coord, result);
        return result;
    }

    // See REFINE_SEARCH_RADIUS/REFINE_REG_LAMBDA in the A->B pass above.
    // ---- refine three seeds; the temporal seed and prior only where the previous flow round-trips ----
    vec2 prev_e = imageLoad(FLOW_E_DC_CACHE, coord).xy * LUMA_A_E_pt;
    ivec2 rcoord = clamp(ivec2((uv_b + prev_e) * LUMA_A_E_size), ivec2(0), ivec2(LUMA_A_E_size) - 1);
    vec2 prev_rev = imageLoad(FLOW_E_CD_CACHE, rcoord).xy * LUMA_A_E_pt;
    float rt = length((prev_e + prev_rev) / LUMA_A_E_pt);
    bool trusted = rt < SEED_RT_MAX && length(prev_e) > 0.0;
    float tl = trusted ? SEED_TEMP_LAMBDA : 0.0;
    ivec2 scoord = ivec2(snap_texel(uv_b, FLOW_S_DC_size) * FLOW_S_DC_size);
    vec2 base_off3 = imageLoad(FLOW_S_DC_CACHE2, scoord).xy * 2.0 * LUMA_A_E_pt;
    float sad_a, sad_b, sad_c;
    vec2 ref_a = refine_e(uv_b, base_off, sad_a);
    vec2 ref_b = refine_e(uv_b, base_off2, sad_b);
    vec2 ref_c = refine_e(uv_b, base_off3, sad_c);
    float score_a = sad_a + SEED_MAG_LAMBDA * length(ref_a / LUMA_A_E_pt) + tl * length((ref_a - prev_e) / LUMA_A_E_pt);
    float score_b = sad_b + SEED_MAG_LAMBDA * length(ref_b / LUMA_A_E_pt) + tl * length((ref_b - prev_e) / LUMA_A_E_pt);
    float score_c = trusted ? sad_c + SEED_MAG_LAMBDA * length(ref_c / LUMA_A_E_pt) + tl * length((ref_c - prev_e) / LUMA_A_E_pt) : 1.0e30;
    const float TIE_MARGIN = 1.0e-4;
    vec2 best_off = ref_a;
    float best_score = score_a;
    if (score_b < best_score * (1.0 - TIE_MARGIN)) { best_off = ref_b; best_score = score_b; }
    if (score_c < best_score * (1.0 - TIE_MARGIN)) { best_off = ref_c; best_score = score_c; }
    vec4 result = vec4(best_off / LUMA_A_E_pt, 0.0, 0.0);
    imageStore(FLOW_E_DC_CACHE, coord, result);
    return result;
}


//!TEXTURE FLOW_Q_DC_CACHE
//!SIZE 960 540
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_Q_DC_CACHE
//!BIND LUMA_A_Q
//!BIND LUMA_B_Q
//!BIND LUMA_C_Q
//!BIND LUMA_D_Q
//!BIND FLOW_E_DC
//!SAVE FLOW_Q_DC
//!WIDTH HOOKED.w 4 /
//!HEIGHT HOOKED.h 4 /
//!COMPONENTS 2
//!DESC [quad] refine flow slot3->slot2 (1/4 res)

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
            s += abs(LUMA_D_Q_tex(uv_b + o).r - LUMA_C_Q_tex(uv_a + o).r);
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
            float v = LUMA_D_Q_tex(uv_b + vec2(float(x), float(y)) * LUMA_A_Q_pt).r;
            lo = min(lo, v);
            hi = max(hi, v);
        }
    }
    return hi - lo;
}

vec4 hook() {
    ivec2 coord = ivec2(LUMA_B_Q_pos * LUMA_B_Q_size);
    if (!pair_changed)
        return imageLoad(FLOW_Q_DC_CACHE, coord);

    vec2 uv_b = LUMA_B_Q_pos;
    vec2 base_off = FLOW_E_DC_tex(snap_texel(uv_b, FLOW_E_DC_size)).xy * 2.0 * LUMA_A_Q_pt;

    if (local_contrast_5x5_q2(uv_b) < MIN_CONTRAST) {
        vec4 result = vec4(base_off / LUMA_A_Q_pt, 0.0, 0.0);
        imageStore(FLOW_Q_DC_CACHE, coord, result);
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
    imageStore(FLOW_Q_DC_CACHE, coord, result);
    return result;
}


//!TEXTURE FLOW_H_DC_CACHE
//!SIZE 1920 1080
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_H_DC_CACHE
//!BIND LUMA_A_H
//!BIND LUMA_B_H
//!BIND LUMA_C_H
//!BIND LUMA_D_H
//!BIND FLOW_Q_DC
//!SAVE FLOW_H_DC
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 2
//!DESC [quad] refine flow slot3->slot2 (half res)

// See snap_texel() in the A->B pass above.
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

float sad3x3_h2_self(vec2 uv, vec2 o) {
    float s = 0.0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 d = vec2(float(x), float(y)) * LUMA_A_H_pt;
            s += abs(LUMA_D_H_tex(uv + d).r - LUMA_D_H_tex(uv + o + d).r);
        }
    }
    return s;
}
float sad3x3_h2(vec2 uv_b, vec2 uv_a) {
    float s = 0.0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 o = vec2(float(x), float(y)) * LUMA_A_H_pt;
            s += abs(LUMA_D_H_tex(uv_b + o).r - LUMA_C_H_tex(uv_a + o).r);
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
            float v = LUMA_D_H_tex(uv_b + vec2(float(x), float(y)) * LUMA_A_H_pt).r;
            lo = min(lo, v);
            hi = max(hi, v);
        }
    }
    return hi - lo;
}

vec4 hook() {
    ivec2 coord = ivec2(LUMA_B_H_pos * LUMA_B_H_size);
    if (!pair_changed)
        return imageLoad(FLOW_H_DC_CACHE, coord);

    vec2 uv_b = LUMA_B_H_pos;
    vec2 base_off = FLOW_Q_DC_tex(snap_texel(uv_b, FLOW_Q_DC_size)).xy * 2.0 * LUMA_A_H_pt;

    if (local_contrast_3x3_h2(uv_b) < MIN_CONTRAST) {
        vec4 result = vec4(base_off / LUMA_A_H_pt, 0.0, 0.0);
        imageStore(FLOW_H_DC_CACHE, coord, result);
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

    // SUBPEL_SELFREF: subtract the fit's own bias. For a PERFECT integer match the fit's vertex is
    // not zero: the 3x3 costs at -1 and +1 texel differ whenever the block spans a fraction of a
    // texture period, and the vertex moves with the block's phase -- a quarter-pixel floor locked
    // to the texture, the same at every speed, integer or fractional (NFRAME-LIMITS.md section 9).
    // That vertex is the fit of the reference block against ITSELF shifted, computable from one
    // frame; subtracting it makes the fit exact at integer shifts. Measured through the four-frame
    // shader: integer translation 0.33 -> 0.001 px median per-texel error, fractional 0.37 -> 0.13,
    // aperiodic texture unchanged, A4's per-texel acceleration spread 2.3x tighter, ladder +0.54 dB
    // mean over 32 cases with one loss (L1, the near-ceiling flat square, -4.7 dB at 74 dB), +2.4%
    // time. OFF here like SUBPEL_REFINE, for the same reason: this shader has no field to sharpen.
    // The generated field shaders turn both on.
    const int SUBPEL_SELFREF = 1;
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
        if (SUBPEL_SELFREF != 0) {
            float sxm = sad3x3_h2_self(uv_b, -ex), sxp = sad3x3_h2_self(uv_b, ex);
            float sym = sad3x3_h2_self(uv_b, -ey), syp = sad3x3_h2_self(uv_b, ey);
            float ddx = SUBPEL_FIT != 0 ? max(sxm, sxp) : sxm + sxp;
            float ddy = SUBPEL_FIT != 0 ? max(sym, syp) : sym + syp;
            vec2  bias0 = vec2(ddx > 1.0e-6 ? 0.5 * (sxm - sxp) / ddx : 0.0,
                               ddy > 1.0e-6 ? 0.5 * (sym - syp) / ddy : 0.0);
            sub = clamp(sub - bias0, -0.5, 0.5);
        }
        best_off += sub * LUMA_A_H_pt;
    }
    vec4 result = vec4(best_off / LUMA_A_H_pt, 0.0, 0.0);
    imageStore(FLOW_H_DC_CACHE, coord, result);
    return result;
}


//!HOOK FRAME_MIX
//!BIND FLOW_H_DC
//!SAVE FLOW_H_DC
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 2
//!DESC [quad] vector median filter on flow slot3->slot2 (pass 1)
vec4 hook() {
    if (!pair_changed)
        return vec4(0.0);

    vec2 v[9];
    int n = 0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 o = vec2(float(x), float(y)) * FLOW_H_DC_pt;
            v[n++] = FLOW_H_DC_tex(FLOW_H_DC_pos + o).xy;
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
//!TEXTURE FLOW_H_DC_MEDIAN_CACHE
//!SIZE 1920 1080
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_H_DC_MEDIAN_CACHE
//!BIND FLOW_H_DC
//!SAVE FLOW_H_DC
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 2
//!DESC [quad] vector median filter on flow slot3->slot2 (pass 2)
vec4 hook() {
    ivec2 coord = ivec2(FLOW_H_DC_pos * FLOW_H_DC_size);
    if (!pair_changed)
        return imageLoad(FLOW_H_DC_MEDIAN_CACHE, coord);

    vec2 v[9];
    int n = 0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 o = vec2(float(x), float(y)) * FLOW_H_DC_pt;
            v[n++] = FLOW_H_DC_tex(FLOW_H_DC_pos + o).xy;
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
    imageStore(FLOW_H_DC_MEDIAN_CACHE, coord, result);
    return result;
}
//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!BIND FRAME3
//!SAVE LUMA_A_F
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!COMPONENTS 1
//!DESC [quad] slot 0 luma at full res
vec4 hook() {
    return vec4(dot(HOOKED_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}
//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!BIND FRAME3
//!SAVE LUMA_B_F
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!COMPONENTS 1
//!DESC [quad] slot 1 luma at full res
vec4 hook() {
    return vec4(dot(FRAME1_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}
//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!BIND FRAME3
//!SAVE LUMA_C_F
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!COMPONENTS 1
//!DESC [quad] slot 2 luma at full res
vec4 hook() {
    return vec4(dot(FRAME2_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}
//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!BIND FRAME3
//!SAVE LUMA_D_F
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!COMPONENTS 1
//!DESC [quad] slot 3 luma at full res
vec4 hook() {
    return vec4(dot(FRAME3_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
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
//!DESC [quad] refine flow A->B (full res)

// Same seed-snapping fix as the two coarser handoffs above -- here for
// the H->F handoff: FLOW_H_AB's own texel is 2 full-res px, so an
// unsnapped bilinear read would smear a real boundary across ~2px in
// every direction (~4px total) when seeding this level.
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

float sad5x5_f_self(vec2 uv, vec2 o) {
    float s = 0.0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 d = vec2(float(x), float(y)) * LUMA_A_F_pt;
            s += abs(LUMA_A_F_tex(uv + d).r - LUMA_A_F_tex(uv + o + d).r);
        }
    }
    return s;
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

    // SUBPEL_SELFREF: subtract the fit's own bias. For a PERFECT integer match the fit's vertex is
    // not zero: the 3x3 costs at -1 and +1 texel differ whenever the block spans a fraction of a
    // texture period, and the vertex moves with the block's phase -- a quarter-pixel floor locked
    // to the texture, the same at every speed, integer or fractional (NFRAME-LIMITS.md section 9).
    // That vertex is the fit of the reference block against ITSELF shifted, computable from one
    // frame; subtracting it makes the fit exact at integer shifts. Measured through the four-frame
    // shader: integer translation 0.33 -> 0.001 px median per-texel error, fractional 0.37 -> 0.13,
    // aperiodic texture unchanged, A4's per-texel acceleration spread 2.3x tighter, ladder +0.54 dB
    // mean over 32 cases with one loss (L1, the near-ceiling flat square, -4.7 dB at 74 dB), +2.4%
    // time. OFF here like SUBPEL_REFINE, for the same reason: this shader has no field to sharpen.
    // The generated field shaders turn both on.
    const int SUBPEL_SELFREF = 1;
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
        if (SUBPEL_SELFREF != 0) {
            float sxm = sad5x5_f_self(uv_a, -ex), sxp = sad5x5_f_self(uv_a, ex);
            float sym = sad5x5_f_self(uv_a, -ey), syp = sad5x5_f_self(uv_a, ey);
            float ddx = SUBPEL_FIT != 0 ? max(sxm, sxp) : sxm + sxp;
            float ddy = SUBPEL_FIT != 0 ? max(sym, syp) : sym + syp;
            vec2  bias0 = vec2(ddx > 1.0e-6 ? 0.5 * (sxm - sxp) / ddx : 0.0,
                               ddy > 1.0e-6 ? 0.5 * (sym - syp) / ddy : 0.0);
            sub = clamp(sub - bias0, -0.5, 0.5);
        }
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
//!DESC [quad] refine flow B->A (full res)

// See snap_texel() in the A->B pass above.
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

float sad5x5_f2_self(vec2 uv, vec2 o) {
    float s = 0.0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 d = vec2(float(x), float(y)) * LUMA_A_F_pt;
            s += abs(LUMA_B_F_tex(uv + d).r - LUMA_B_F_tex(uv + o + d).r);
        }
    }
    return s;
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

    // SUBPEL_SELFREF: subtract the fit's own bias. For a PERFECT integer match the fit's vertex is
    // not zero: the 3x3 costs at -1 and +1 texel differ whenever the block spans a fraction of a
    // texture period, and the vertex moves with the block's phase -- a quarter-pixel floor locked
    // to the texture, the same at every speed, integer or fractional (NFRAME-LIMITS.md section 9).
    // That vertex is the fit of the reference block against ITSELF shifted, computable from one
    // frame; subtracting it makes the fit exact at integer shifts. Measured through the four-frame
    // shader: integer translation 0.33 -> 0.001 px median per-texel error, fractional 0.37 -> 0.13,
    // aperiodic texture unchanged, A4's per-texel acceleration spread 2.3x tighter, ladder +0.54 dB
    // mean over 32 cases with one loss (L1, the near-ceiling flat square, -4.7 dB at 74 dB), +2.4%
    // time. OFF here like SUBPEL_REFINE, for the same reason: this shader has no field to sharpen.
    // The generated field shaders turn both on.
    const int SUBPEL_SELFREF = 1;
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
        if (SUBPEL_SELFREF != 0) {
            float sxm = sad5x5_f2_self(uv_b, -ex), sxp = sad5x5_f2_self(uv_b, ex);
            float sym = sad5x5_f2_self(uv_b, -ey), syp = sad5x5_f2_self(uv_b, ey);
            float ddx = SUBPEL_FIT != 0 ? max(sxm, sxp) : sxm + sxp;
            float ddy = SUBPEL_FIT != 0 ? max(sym, syp) : sym + syp;
            vec2  bias0 = vec2(ddx > 1.0e-6 ? 0.5 * (sxm - sxp) / ddx : 0.0,
                               ddy > 1.0e-6 ? 0.5 * (sym - syp) / ddy : 0.0);
            sub = clamp(sub - bias0, -0.5, 0.5);
        }
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
//!DESC [quad] refine flow slot1->slot2 (full res)

// Same seed-snapping fix as the two coarser handoffs above -- here for
// the H->F handoff: FLOW_H_BC's own texel is 2 full-res px, so an
// unsnapped bilinear read would smear a real boundary across ~2px in
// every direction (~4px total) when seeding this level.
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

float sad5x5_f_self(vec2 uv, vec2 o) {
    float s = 0.0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 d = vec2(float(x), float(y)) * LUMA_A_F_pt;
            s += abs(LUMA_B_F_tex(uv + d).r - LUMA_B_F_tex(uv + o + d).r);
        }
    }
    return s;
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

    // SUBPEL_SELFREF: subtract the fit's own bias. For a PERFECT integer match the fit's vertex is
    // not zero: the 3x3 costs at -1 and +1 texel differ whenever the block spans a fraction of a
    // texture period, and the vertex moves with the block's phase -- a quarter-pixel floor locked
    // to the texture, the same at every speed, integer or fractional (NFRAME-LIMITS.md section 9).
    // That vertex is the fit of the reference block against ITSELF shifted, computable from one
    // frame; subtracting it makes the fit exact at integer shifts. Measured through the four-frame
    // shader: integer translation 0.33 -> 0.001 px median per-texel error, fractional 0.37 -> 0.13,
    // aperiodic texture unchanged, A4's per-texel acceleration spread 2.3x tighter, ladder +0.54 dB
    // mean over 32 cases with one loss (L1, the near-ceiling flat square, -4.7 dB at 74 dB), +2.4%
    // time. OFF here like SUBPEL_REFINE, for the same reason: this shader has no field to sharpen.
    // The generated field shaders turn both on.
    const int SUBPEL_SELFREF = 1;
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
        if (SUBPEL_SELFREF != 0) {
            float sxm = sad5x5_f_self(uv_a, -ex), sxp = sad5x5_f_self(uv_a, ex);
            float sym = sad5x5_f_self(uv_a, -ey), syp = sad5x5_f_self(uv_a, ey);
            float ddx = SUBPEL_FIT != 0 ? max(sxm, sxp) : sxm + sxp;
            float ddy = SUBPEL_FIT != 0 ? max(sym, syp) : sym + syp;
            vec2  bias0 = vec2(ddx > 1.0e-6 ? 0.5 * (sxm - sxp) / ddx : 0.0,
                               ddy > 1.0e-6 ? 0.5 * (sym - syp) / ddy : 0.0);
            sub = clamp(sub - bias0, -0.5, 0.5);
        }
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
//!DESC [quad] refine flow slot2->slot1 (full res)

// See snap_texel() in the A->B pass above.
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

float sad5x5_f2_self(vec2 uv, vec2 o) {
    float s = 0.0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 d = vec2(float(x), float(y)) * LUMA_A_F_pt;
            s += abs(LUMA_C_F_tex(uv + d).r - LUMA_C_F_tex(uv + o + d).r);
        }
    }
    return s;
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

    // SUBPEL_SELFREF: subtract the fit's own bias. For a PERFECT integer match the fit's vertex is
    // not zero: the 3x3 costs at -1 and +1 texel differ whenever the block spans a fraction of a
    // texture period, and the vertex moves with the block's phase -- a quarter-pixel floor locked
    // to the texture, the same at every speed, integer or fractional (NFRAME-LIMITS.md section 9).
    // That vertex is the fit of the reference block against ITSELF shifted, computable from one
    // frame; subtracting it makes the fit exact at integer shifts. Measured through the four-frame
    // shader: integer translation 0.33 -> 0.001 px median per-texel error, fractional 0.37 -> 0.13,
    // aperiodic texture unchanged, A4's per-texel acceleration spread 2.3x tighter, ladder +0.54 dB
    // mean over 32 cases with one loss (L1, the near-ceiling flat square, -4.7 dB at 74 dB), +2.4%
    // time. OFF here like SUBPEL_REFINE, for the same reason: this shader has no field to sharpen.
    // The generated field shaders turn both on.
    const int SUBPEL_SELFREF = 1;
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
        if (SUBPEL_SELFREF != 0) {
            float sxm = sad5x5_f2_self(uv_b, -ex), sxp = sad5x5_f2_self(uv_b, ex);
            float sym = sad5x5_f2_self(uv_b, -ey), syp = sad5x5_f2_self(uv_b, ey);
            float ddx = SUBPEL_FIT != 0 ? max(sxm, sxp) : sxm + sxp;
            float ddy = SUBPEL_FIT != 0 ? max(sym, syp) : sym + syp;
            vec2  bias0 = vec2(ddx > 1.0e-6 ? 0.5 * (sxm - sxp) / ddx : 0.0,
                               ddy > 1.0e-6 ? 0.5 * (sym - syp) / ddy : 0.0);
            sub = clamp(sub - bias0, -0.5, 0.5);
        }
        best_off += sub * LUMA_A_F_pt;
    }
    vec4 result = vec4(best_off / LUMA_A_F_pt, 0.0, 0.0);
    imageStore(FLOW_F_CB_CACHE, coord, result);
    return result;
}

//!TEXTURE FLOW_F_CD_CACHE
//!SIZE 1920 1080
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_F_CD_CACHE
//!BIND LUMA_A_F
//!BIND LUMA_B_F
//!BIND LUMA_C_F
//!BIND LUMA_D_F
//!BIND FLOW_H_CD
//!SAVE FLOW_F_CD
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!COMPONENTS 2
//!DESC [quad] refine flow slot2->slot3 (full res)

// Same seed-snapping fix as the two coarser handoffs above -- here for
// the H->F handoff: FLOW_H_CD's own texel is 2 full-res px, so an
// unsnapped bilinear read would smear a real boundary across ~2px in
// every direction (~4px total) when seeding this level.
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

float sad5x5_f_self(vec2 uv, vec2 o) {
    float s = 0.0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 d = vec2(float(x), float(y)) * LUMA_A_F_pt;
            s += abs(LUMA_C_F_tex(uv + d).r - LUMA_C_F_tex(uv + o + d).r);
        }
    }
    return s;
}
float sad5x5_f(vec2 uv_a, vec2 uv_b) {
    float s = 0.0;
    for (int y = -2; y <= 2; y++) {
        for (int x = -2; x <= 2; x++) {
            vec2 o = vec2(float(x), float(y)) * LUMA_A_F_pt;
            s += abs(LUMA_C_F_tex(uv_a + o).r - LUMA_D_F_tex(uv_b + o).r);
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
            float v = LUMA_C_F_tex(uv_a + vec2(float(x), float(y)) * LUMA_A_F_pt).r;
            lo = min(lo, v);
            hi = max(hi, v);
        }
    }
    return hi - lo;
}

vec4 hook() {
    ivec2 coord = ivec2(LUMA_A_F_pos * LUMA_A_F_size);
    if (!pair_changed)
        return imageLoad(FLOW_F_CD_CACHE, coord);

    vec2 uv_a = LUMA_A_F_pos;
    vec2 base_off = FLOW_H_CD_tex(snap_texel(uv_a, FLOW_H_CD_size)).xy * 2.0 * LUMA_A_F_pt;

    if (local_contrast_3x3_f(uv_a) < MIN_CONTRAST) {
        vec4 result = vec4(base_off / LUMA_A_F_pt, 0.0, 0.0);
        imageStore(FLOW_F_CD_CACHE, coord, result);
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

    // SUBPEL_SELFREF: subtract the fit's own bias. For a PERFECT integer match the fit's vertex is
    // not zero: the 3x3 costs at -1 and +1 texel differ whenever the block spans a fraction of a
    // texture period, and the vertex moves with the block's phase -- a quarter-pixel floor locked
    // to the texture, the same at every speed, integer or fractional (NFRAME-LIMITS.md section 9).
    // That vertex is the fit of the reference block against ITSELF shifted, computable from one
    // frame; subtracting it makes the fit exact at integer shifts. Measured through the four-frame
    // shader: integer translation 0.33 -> 0.001 px median per-texel error, fractional 0.37 -> 0.13,
    // aperiodic texture unchanged, A4's per-texel acceleration spread 2.3x tighter, ladder +0.54 dB
    // mean over 32 cases with one loss (L1, the near-ceiling flat square, -4.7 dB at 74 dB), +2.4%
    // time. OFF here like SUBPEL_REFINE, for the same reason: this shader has no field to sharpen.
    // The generated field shaders turn both on.
    const int SUBPEL_SELFREF = 1;
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
        if (SUBPEL_SELFREF != 0) {
            float sxm = sad5x5_f_self(uv_a, -ex), sxp = sad5x5_f_self(uv_a, ex);
            float sym = sad5x5_f_self(uv_a, -ey), syp = sad5x5_f_self(uv_a, ey);
            float ddx = SUBPEL_FIT != 0 ? max(sxm, sxp) : sxm + sxp;
            float ddy = SUBPEL_FIT != 0 ? max(sym, syp) : sym + syp;
            vec2  bias0 = vec2(ddx > 1.0e-6 ? 0.5 * (sxm - sxp) / ddx : 0.0,
                               ddy > 1.0e-6 ? 0.5 * (sym - syp) / ddy : 0.0);
            sub = clamp(sub - bias0, -0.5, 0.5);
        }
        best_off += sub * LUMA_A_F_pt;
    }
    vec4 result = vec4(best_off / LUMA_A_F_pt, 0.0, 0.0);
    imageStore(FLOW_F_CD_CACHE, coord, result);
    return result;
}

//!TEXTURE FLOW_F_DC_CACHE
//!SIZE 1920 1080
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_F_DC_CACHE
//!BIND LUMA_A_F
//!BIND LUMA_B_F
//!BIND LUMA_C_F
//!BIND LUMA_D_F
//!BIND FLOW_H_DC
//!SAVE FLOW_F_DC
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!COMPONENTS 2
//!DESC [quad] refine flow slot3->slot2 (full res)

// See snap_texel() in the A->B pass above.
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

float sad5x5_f2_self(vec2 uv, vec2 o) {
    float s = 0.0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 d = vec2(float(x), float(y)) * LUMA_A_F_pt;
            s += abs(LUMA_D_F_tex(uv + d).r - LUMA_D_F_tex(uv + o + d).r);
        }
    }
    return s;
}
float sad5x5_f2(vec2 uv_b, vec2 uv_a) {
    float s = 0.0;
    for (int y = -2; y <= 2; y++) {
        for (int x = -2; x <= 2; x++) {
            vec2 o = vec2(float(x), float(y)) * LUMA_A_F_pt;
            s += abs(LUMA_D_F_tex(uv_b + o).r - LUMA_C_F_tex(uv_a + o).r);
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
            float v = LUMA_D_F_tex(uv_b + vec2(float(x), float(y)) * LUMA_A_F_pt).r;
            lo = min(lo, v);
            hi = max(hi, v);
        }
    }
    return hi - lo;
}

vec4 hook() {
    ivec2 coord = ivec2(LUMA_B_F_pos * LUMA_B_F_size);
    if (!pair_changed)
        return imageLoad(FLOW_F_DC_CACHE, coord);

    vec2 uv_b = LUMA_B_F_pos;
    vec2 base_off = FLOW_H_DC_tex(snap_texel(uv_b, FLOW_H_DC_size)).xy * 2.0 * LUMA_A_F_pt;

    if (local_contrast_3x3_f2(uv_b) < MIN_CONTRAST) {
        vec4 result = vec4(base_off / LUMA_A_F_pt, 0.0, 0.0);
        imageStore(FLOW_F_DC_CACHE, coord, result);
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

    // SUBPEL_SELFREF: subtract the fit's own bias. For a PERFECT integer match the fit's vertex is
    // not zero: the 3x3 costs at -1 and +1 texel differ whenever the block spans a fraction of a
    // texture period, and the vertex moves with the block's phase -- a quarter-pixel floor locked
    // to the texture, the same at every speed, integer or fractional (NFRAME-LIMITS.md section 9).
    // That vertex is the fit of the reference block against ITSELF shifted, computable from one
    // frame; subtracting it makes the fit exact at integer shifts. Measured through the four-frame
    // shader: integer translation 0.33 -> 0.001 px median per-texel error, fractional 0.37 -> 0.13,
    // aperiodic texture unchanged, A4's per-texel acceleration spread 2.3x tighter, ladder +0.54 dB
    // mean over 32 cases with one loss (L1, the near-ceiling flat square, -4.7 dB at 74 dB), +2.4%
    // time. OFF here like SUBPEL_REFINE, for the same reason: this shader has no field to sharpen.
    // The generated field shaders turn both on.
    const int SUBPEL_SELFREF = 1;
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
        if (SUBPEL_SELFREF != 0) {
            float sxm = sad5x5_f2_self(uv_b, -ex), sxp = sad5x5_f2_self(uv_b, ex);
            float sym = sad5x5_f2_self(uv_b, -ey), syp = sad5x5_f2_self(uv_b, ey);
            float ddx = SUBPEL_FIT != 0 ? max(sxm, sxp) : sxm + sxp;
            float ddy = SUBPEL_FIT != 0 ? max(sym, syp) : sym + syp;
            vec2  bias0 = vec2(ddx > 1.0e-6 ? 0.5 * (sxm - sxp) / ddx : 0.0,
                               ddy > 1.0e-6 ? 0.5 * (sym - syp) / ddy : 0.0);
            sub = clamp(sub - bias0, -0.5, 0.5);
        }
        best_off += sub * LUMA_A_F_pt;
    }
    vec4 result = vec4(best_off / LUMA_A_F_pt, 0.0, 0.0);
    imageStore(FLOW_F_DC_CACHE, coord, result);
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
//!BIND FRAME3
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
//!BIND FRAME3
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
// Final pass: QUADDIRECTIONAL warp -- cubic (constant-jerk) placement,
// full resolution, plus the jerk and confidence fields no 3-frame shader
// can produce.
//
// Four frames determine a cubic. QUAD_MODE picks how the fourth frame's
// information is spent -- both arms are in the record (PRIOR-ART.md) and
// the fork is the experiment:
//
//   QUAD_MODE 0 (cubic, exact): d(tau) = v*tau + a/2 tau^2 + j/6 tau^3
//     through the anchor's three measured displacements. At uniform
//     spacing the acceleration row reduces to a = d(+1) + d(-1) -- the
//     tridirectional formula EXACTLY, untouched by jerk (odd orders
//     cancel at the centred pair). Pre-registered: the N:N field's
//     accuracy does not change; what is new is j, and cubic placement
//     at 24->60 where the output sits off the centre of symmetry.
//
//   QUAD_MODE 1 (least-squares quadratic, EQVI's RQFP): the same
//     quadratic tri fits, but overdetermined by all three flows, with
//     the residual read out as a per-texel MEASURED confidence -- the
//     arm nobody in the record took further than fitting.
//
// EVERYTHING READ HERE IS SLOT-KEYED. Six adjacent-pair flows between
// fixed slots, all pure functions of the window, all cached. This pass
// alone derives roles (straddle pair, anchor) from rts_mix per output
// frame. The two-interval flow is COMPOSED from adjacent links, never
// searched directly -- see the generator banner for why.
// ---------------------------------------------------------------------
//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!BIND FRAME3
//!BIND SCENE_DIFF
//!BIND SCENE_DIFF_BC
//!BIND SCENE_DIFF_CD
//!BIND FLOW_H_AB
//!BIND FLOW_H_BC
//!BIND FLOW_H_CD
//!BIND FLOW_F_AB
//!BIND FLOW_F_BA
//!BIND FLOW_F_BC
//!BIND FLOW_F_CB
//!BIND FLOW_F_CD
//!BIND FLOW_F_DC
//!SAVE FRAME_MIX
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!DESC [quad] motion-compensated warp (cubic placement)

// WARP ON H, MEASURE ON F: the estimator reads the full-res flows, the
// warp keeps the mediated half-res ones -- the first full-res build fed
// unfiltered F flows to the warp and L1 paid 2.95 dB for scatter the
// medians used to remove. Same split as the deadband and the sub-pixel
// default: the field reports the measurement, the picture moves only on
// what is safe.
//
// The base's texel-snap gate is NOT carried here: its EDGE_A/EDGE_B binds
// no longer fit under libplacebo's 16-bind ceiling once both flow levels
// are bound, and SNAP_STRENGTH has been 0.0 for the gate's entire life.
// If the snap experiment is ever revived, it must earn a bind budget.

// Same value and reasoning as the base shader's gate.
const float SCENE_CUT_DIFF = 0.125;

// 0 = exact cubic (jerk modelled), 1 = least-squares quadratic (residual
// read as confidence). See the pass banner; both are the experiment.
const int QUAD_MODE = 0;

// Acceleration clamp and trust gate: identical values and identical
// reasoning to the tridirectional shader (round-trip provenance, not
// magnitude -- see TRIDIRECTIONAL.md, "the gate that made it work").
const float ACCEL_MAX_PX = 16.0;
const float ACCEL_TRUST_LO = 2.0;
const float ACCEL_TRUST_HI = 5.0;

// Jerk clamp, px per straddle-interval^3. Same physical argument as
// ACCEL_MAX_PX one order up: sustained jerk beyond a few px/interval^3
// exits the search's reach within a couple of frames. The O-series peaks
// at 5.6 (O5) and 0.72 (O6). A reasoned start, not a measured optimum.
const float JERK_MAX_PX = 8.0;

// Deadbands on the WARP's copies of the fields -- never on what the
// diagnostics report. Same trade as tri's accel deadband, ONE ORDER UP --
// and the jerk band had to be measured, not inherited: the uniform jerk
// stencil's coefficients (1,-3,-1)/(1,3,-1) amplify flow noise by
// sqrt(11)/sqrt(2) ~ 2.3x the accel stencil's, and inheriting accel's
// 0.5/1.5 cost 4.9 dB on L1_trans_8px (zero-jerk content). Swept:
//
//   jerk deadband    L1      A2      O3      O4
//   0.5/1.5       55.61   42.70   46.27   47.80
//   1.0/3.0       55.10   42.76   46.27   47.69
//   2.0/4.0       57.22   42.81   46.28   47.58
//   3.0/6.0       60.20   42.81   46.28   47.50
//   jerk OFF      60.55   42.81   45.17   47.24
//
// O3 -- the hardest oscillation, jerk peak ~13.8 px/interval^3 -- keeps its
// FULL +1.1 dB at every setting: its useful jerk lives far above the band.
// L1's noise cost falls monotonically as the band widens. 3.0/6.0 keeps
// all of O3, most of O4's +0.26, costs L1 0.35 dB against jerk-off, and
// returns A2 (true jerk zero) to its jerk-off score exactly.
const float ACCEL_DEADBAND_LO = 0.5;
const float ACCEL_DEADBAND_HI = 1.5;
const float JERK_DEADBAND_LO = 3.0;
const float JERK_DEADBAND_HI = 6.0;

// TRI_DIAG -- keeps the tridirectional shader's name and modes 0-4 so
// every existing instrument (accelcheck.py, accelprospect.sh, trivis.py,
// calsweep drivers) reads this shader unchanged. Two quad-only modes:
//
//   0 = normal output          1 = correction (px)   2 = acceleration
//   3 = |a| heat map           4 = |a| linear luma (measurement, no marker)
//   5 = JERK field, px/interval^3, encoded like mode 2  (marker: magenta)
//   6 = LSQ residual (QUAD_MODE 1) as linear luma -- measurement mode,
//       no marker, in px against RESID_DIAG_FS. The confidence field.
//   7 = VELOCITY field: the straddle-pair flow f_fwd, px/interval,
//       encoded like mode 2 against VEL_DIAG_FS (marker: orange). The
//       zeroth derivative the demo's display was missing -- "moving
//       right" as a solid colour.
const int TRI_DIAG = 0;

const float ACCEL_DIAG_FS = 2.0;   // px/interval^2 full scale (modes 2, 3)
const float CORR_DIAG_FS  = 0.25;  // px full scale (mode 1)
const float JERK_DIAG_FS  = 2.0;   // px/interval^3 full scale (mode 5)
const float RESID_DIAG_FS = 2.0;   // px full scale (mode 6)
const float VEL_DIAG_FS   = 2.0;   // px/interval full scale (mode 7)

// DIAG_HOLD_ANCHOR = 1 pins the diag modes' anchor to slot 1, so a
// displayed field updates once per window advance (source cadence)
// instead of re-anchoring as the output phase s crosses 0.5. The two
// anchors' stencils sample different flow textures whose sub-pixel
// noise is independent, so per-phase re-anchoring STROBES a live
// display between two decorrelated noise fields (~36 Hz at 24->60,
// measured 1.5 px rms background / 3-4 px mover on the jerk field).
// Default 0 keeps the established instrument semantics -- accelcheck's
// calibrations read the phase-dependent anchor -- and the warp path
// never uses this either way. The demo's field graphs set 1 (gen.sh).
const int DIAG_HOLD_ANCHOR = 0;

vec4 tri_diag_marker() {
    if (TRI_DIAG == 1) return vec4(1.0, 0.2, 0.2, 1.0);   // red     -- correction
    if (TRI_DIAG == 2) return vec4(0.2, 0.6, 1.0, 1.0);   // blue    -- acceleration
    if (TRI_DIAG == 5) return vec4(1.0, 0.2, 1.0, 1.0);   // magenta -- jerk
    if (TRI_DIAG == 7) return vec4(1.0, 0.6, 0.1, 1.0);   // orange  -- velocity
    return vec4(0.2, 1.0, 0.3, 1.0);                      // green   -- magnitude
}

vec4 slot_tex(int i, vec2 uv) {
    if (i == 0) return HOOKED_tex(uv);
    if (i == 1) return FRAME1_tex(uv);
    if (i == 2) return FRAME2_tex(uv);
    return FRAME3_tex(uv);
}

vec4 hook() {
    // ---- roles, derived per output frame from slot-keyed fields ----
    // Straddle pair (p, p+1): p is the last slot at or before the output.
    // Interior 24->60 gives p = 1 every phase; exact N:N gives p = 2 with
    // the output ON slot p (s = 0). All-past windows at a stream's end
    // clamp s to 1 and show the newest frame -- same graceful degrade as
    // the tri shader.
    int p = 0;
    if (rts_mix[1] <= 0.0) p = 1;
    if (rts_mix[2] <= 0.0) p = 2;

    float tA = rts_mix[p];
    float tB = rts_mix[p + 1];
    float L  = tB - tA;                       // straddle interval, > 0
    float s  = clamp((0.0 - tA) / L, 0.0, 1.0);

    vec2 f_fwd = (p == 0 ? FLOW_H_AB_tex(HOOKED_pos).xy
                : p == 1 ? FLOW_H_BC_tex(HOOKED_pos).xy
                         : FLOW_H_CD_tex(HOOKED_pos).xy) * 2.0 * HOOKED_pt;

    // Cut inside the straddling pair: reproduce the cut (base behaviour).
    float cut01 = SCENE_DIFF_tex(vec2(0.5)).r;
    float cut12 = SCENE_DIFF_BC_tex(vec2(0.5)).r;
    float cut23 = SCENE_DIFF_CD_tex(vec2(0.5)).r;
    float cut_straddle = p == 0 ? cut01 : p == 1 ? cut12 : cut23;
    if (cut_straddle > SCENE_CUT_DIFF)
        return s < 0.5 ? slot_tex(p, HOOKED_pos) : slot_tex(p + 1, HOOKED_pos);

    // ---- anchor: the straddling frame nearer the output ----
    // Clamped to the interior slots {1, 2}: both have adjacent flows on
    // both sides, so the cubic needs at most ONE composed link. (p = 0
    // or an s > 0.5 at p = 2 would name an outer slot; the interior
    // neighbour serves instead, still a straddler.)
    int anchor = clamp(s <= 0.5 ? p : p + 1, 1, 2);
    if (TRI_DIAG != 0 && DIAG_HOLD_ANCHOR == 1) anchor = 1;
    bool anchor_is_A = (anchor == p);

    // Anchor's three displacements, their taus (interval units), their
    // round trips, and the cuts that sever them.
    vec2 f_prev, f_next, f_far;
    float rt_prev, rt_next, rt_far;
    float tau_p, tau_n, tau_f;
    float cut_adj, cut_link;

    if (anchor == 1) {
        f_prev = FLOW_F_BA_tex(HOOKED_pos).xy * HOOKED_pt;
        f_next = FLOW_F_BC_tex(HOOKED_pos).xy * HOOKED_pt;
        // Composed two-interval flow: slot1 -> slot2 -> slot3.
        vec2 link = FLOW_F_CD_tex(HOOKED_pos + f_next).xy * HOOKED_pt;
        f_far  = f_next + link;

        vec2 rp = FLOW_F_AB_tex(HOOKED_pos + f_prev).xy * HOOKED_pt;
        rt_prev = length(f_prev + rp) / length(HOOKED_pt);
        vec2 rn = FLOW_F_CB_tex(HOOKED_pos + f_next).xy * HOOKED_pt;
        rt_next = length(f_next + rn) / length(HOOKED_pt);
        vec2 rf = FLOW_F_DC_tex(HOOKED_pos + f_far).xy * HOOKED_pt;
        rt_far  = max(rt_next, length(link + rf) / length(HOOKED_pt));

        tau_p = (rts_mix[0] - rts_mix[1]) / L;
        tau_n = (rts_mix[2] - rts_mix[1]) / L;
        tau_f = (rts_mix[3] - rts_mix[1]) / L;
        cut_adj  = max(cut01, cut12);
        cut_link = cut23;
    } else {
        f_prev = FLOW_F_CB_tex(HOOKED_pos).xy * HOOKED_pt;
        f_next = FLOW_F_CD_tex(HOOKED_pos).xy * HOOKED_pt;
        // Composed two-interval flow: slot2 -> slot1 -> slot0.
        vec2 link = FLOW_F_BA_tex(HOOKED_pos + f_prev).xy * HOOKED_pt;
        f_far  = f_prev + link;

        vec2 rp = FLOW_F_BC_tex(HOOKED_pos + f_prev).xy * HOOKED_pt;
        rt_prev = length(f_prev + rp) / length(HOOKED_pt);
        vec2 rn = FLOW_F_DC_tex(HOOKED_pos + f_next).xy * HOOKED_pt;
        rt_next = length(f_next + rn) / length(HOOKED_pt);
        vec2 rf = FLOW_F_AB_tex(HOOKED_pos + f_far).xy * HOOKED_pt;
        rt_far  = max(rt_prev, length(link + rf) / length(HOOKED_pt));

        tau_p = (rts_mix[1] - rts_mix[2]) / L;
        tau_n = (rts_mix[3] - rts_mix[2]) / L;
        tau_f = (rts_mix[0] - rts_mix[2]) / L;
        cut_adj  = max(cut12, cut23);
        cut_link = cut01;
    }

    // ---- the solve ----
    vec2 accel = vec2(0.0);
    vec2 jerk  = vec2(0.0);
    float resid = 0.0;

    if (QUAD_MODE == 0) {
        // Exact cubic through the three displacements. Written as the
        // general Vandermonde solve so non-uniform (VFR) spacing is exact;
        // at uniform spacing the acceleration row reduces to
        // a = f_next + f_prev, i.e. the tridirectional estimate.
        mat3 M = mat3(
            vec3(tau_p, tau_n, tau_f),
            vec3(tau_p * tau_p, tau_n * tau_n, tau_f * tau_f) * 0.5,
            vec3(tau_p * tau_p * tau_p, tau_n * tau_n * tau_n,
                 tau_f * tau_f * tau_f) / 6.0);
        if (abs(determinant(M)) > 1.0e-4) {
            mat3 Mi = inverse(M);
            vec3 sx = Mi * vec3(f_prev.x, f_next.x, f_far.x);
            vec3 sy = Mi * vec3(f_prev.y, f_next.y, f_far.y);
            accel = vec2(sx.y, sy.y);
            jerk  = vec2(sx.z, sy.z);
        }
    } else {
        // Least-squares quadratic over all three flows (EQVI's RQFP),
        // residual read out as the confidence field.
        float S2 = tau_p * tau_p + tau_n * tau_n + tau_f * tau_f;
        float S3 = tau_p * tau_p * tau_p + tau_n * tau_n * tau_n
                 + tau_f * tau_f * tau_f;
        float S4 = tau_p * tau_p * tau_p * tau_p
                 + tau_n * tau_n * tau_n * tau_n
                 + tau_f * tau_f * tau_f * tau_f;
        float det = S2 * (S4 * 0.25) - (S3 * 0.5) * (S3 * 0.5);
        if (abs(det) > 1.0e-4) {
            vec2 b1 = tau_p * f_prev + tau_n * f_next + tau_f * f_far;
            vec2 b2 = (tau_p * tau_p * f_prev + tau_n * tau_n * f_next
                     + tau_f * tau_f * f_far) * 0.5;
            vec2 v = ((S4 * 0.25) * b1 - (S3 * 0.5) * b2) / det;
            accel  = (S2 * b2 - (S3 * 0.5) * b1) / det;
            vec2 rp2 = v * tau_p + 0.5 * accel * tau_p * tau_p - f_prev;
            vec2 rn2 = v * tau_n + 0.5 * accel * tau_n * tau_n - f_next;
            vec2 rf2 = v * tau_f + 0.5 * accel * tau_f * tau_f - f_far;
            resid = max(length(rp2), max(length(rn2), length(rf2)))
                  / length(HOOKED_pt);
        }
    }

    // ---- trust: round-trip provenance, per order ----
    // The acceleration row of the cubic is (at uniform spacing) built from
    // f_prev and f_next alone, so it takes the tri shader's two-flow gate
    // unchanged. Jerk -- and the LSQ fit, which mixes all three flows into
    // everything -- answers additionally for the composed link.
    float g2 = 1.0 - smoothstep(ACCEL_TRUST_LO, ACCEL_TRUST_HI,
                                max(rt_prev, rt_next));
    float g3 = 1.0 - smoothstep(ACCEL_TRUST_LO, ACCEL_TRUST_HI,
                                max(max(rt_prev, rt_next), rt_far));
    if (QUAD_MODE == 0) {
        accel *= g2;
        jerk  *= g3;
    } else {
        accel *= g3;
    }

    // Cuts degrade in order: a cut severing an anchor-adjacent pair kills
    // the whole estimate (bidirectional behaviour); one severing only the
    // composed link's far pair kills jerk (tridirectional behaviour).
    if (cut_adj > SCENE_CUT_DIFF) {
        accel = vec2(0.0);
        jerk  = vec2(0.0);
    } else if (cut_link > SCENE_CUT_DIFF) {
        jerk = vec2(0.0);
    }

    vec2 amax = ACCEL_MAX_PX * HOOKED_pt;
    accel = clamp(accel, -amax, amax);
    vec2 jmax = JERK_MAX_PX * HOOKED_pt;
    jerk = clamp(jerk, -jmax, jmax);

    // ---- cubic placement ----
    // Deviation of the constant-jerk trajectory from the straddle chord,
    // with the anchor at one end of the chord:
    //
    //   corr = s(1-s) * ( a/2 + (j/6) * (anchor==A ? (1+s) : -(2-s)) )
    //
    // j = 0 reduces it to tri's s(1-s)*a/2; a = j = 0 to the bidirectional
    // warp. Warp copies are deadbanded; the reported fields are not.
    vec2 accel_w = accel;
    if (ACCEL_DEADBAND_HI > 0.0)
        accel_w *= smoothstep(ACCEL_DEADBAND_LO, ACCEL_DEADBAND_HI,
                              length(accel / HOOKED_pt));
    vec2 jerk_w = jerk;
    if (JERK_DEADBAND_HI > 0.0)
        jerk_w *= smoothstep(JERK_DEADBAND_LO, JERK_DEADBAND_HI,
                             length(jerk / HOOKED_pt));

    float jgeom = anchor_is_A ? (1.0 + s) : -(2.0 - s);
    vec2 corr = s * (1.0 - s) * (0.5 * accel_w + jerk_w * (jgeom / 6.0));

    if (TRI_DIAG != 0) {
        // Measurement modes first (no marker; whole-frame statistics feed
        // signalstats directly -- see the tri shader's mode 4 note).
        if (TRI_DIAG == 4)
            return vec4(vec3(clamp(length(accel / HOOKED_pt) / ACCEL_DIAG_FS,
                                   0.0, 1.0)), 1.0);
        if (TRI_DIAG == 6)
            return vec4(vec3(clamp(resid / RESID_DIAG_FS, 0.0, 1.0)), 1.0);

        if (HOOKED_pos.x < 24.0 * HOOKED_pt.x && HOOKED_pos.y < 24.0 * HOOKED_pt.y)
            return tri_diag_marker();

        if (TRI_DIAG == 1)
            return vec4(0.5 + (corr / HOOKED_pt) * (0.5 / CORR_DIAG_FS), 0.5, 1.0);
        if (TRI_DIAG == 2)
            return vec4(0.5 + (accel / HOOKED_pt) * (0.5 / ACCEL_DIAG_FS), 0.5, 1.0);
        if (TRI_DIAG == 5)
            return vec4(0.5 + (jerk / HOOKED_pt) * (0.5 / JERK_DIAG_FS), 0.5, 1.0);
        if (TRI_DIAG == 7)
            return vec4(0.5 + (f_fwd / HOOKED_pt) * (0.5 / VEL_DIAG_FS), 0.5, 1.0);

        float m = clamp(length(accel / HOOKED_pt) / ACCEL_DIAG_FS, 0.0, 1.0);
        vec3 c = m < 0.5 ? mix(vec3(0.0, 0.0, 0.25), vec3(0.0, 0.9, 0.9), m * 2.0)
                         : mix(vec3(0.0, 0.9, 0.9), vec3(1.0, 0.1, 0.0), (m - 0.5) * 2.0);
        return vec4(c, 1.0);
    }

    vec2 uv_a = HOOKED_pos - f_fwd * s + corr;
    vec2 uv_b = HOOKED_pos + f_fwd * (1.0 - s) + corr;

    vec4 sa = slot_tex(p, uv_a);
    vec4 sb = slot_tex(p + 1, uv_b);

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
//!BIND FRAME3
//!BIND SCENE_DIFF
//!BIND SCENE_DIFF_BC
//!BIND SCENE_DIFF_CD
//!BIND FLOW_H_AB
//!BIND FLOW_H_BC
//!BIND FLOW_H_CD
//!BIND FLOW_F_AB
//!BIND FLOW_F_BA
//!BIND FLOW_F_BC
//!BIND FLOW_F_CB
//!BIND FLOW_F_CD
//!BIND FLOW_F_DC
//!SAVE READ_FIELD
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!WHEN read_view 0 >
//!DESC [reading] the chosen field in px at 1/8 res: this shader's own final pass in its diagnostic mode

// WARP ON H, MEASURE ON F: the estimator reads the full-res flows, the
// warp keeps the mediated half-res ones -- the first full-res build fed
// unfiltered F flows to the warp and L1 paid 2.95 dB for scatter the
// medians used to remove. Same split as the deadband and the sub-pixel
// default: the field reports the measurement, the picture moves only on
// what is safe.
//
// The base's texel-snap gate is NOT carried here: its EDGE_A/EDGE_B binds
// no longer fit under libplacebo's 16-bind ceiling once both flow levels
// are bound, and SNAP_STRENGTH has been 0.0 for the gate's entire life.
// If the snap experiment is ever revived, it must earn a bind budget.

// Same value and reasoning as the base shader's gate.
const float SCENE_CUT_DIFF = 0.125;

// 0 = exact cubic (jerk modelled), 1 = least-squares quadratic (residual
// read as confidence). See the pass banner; both are the experiment.
const int QUAD_MODE = 0;

// Acceleration clamp and trust gate: identical values and identical
// reasoning to the tridirectional shader (round-trip provenance, not
// magnitude -- see TRIDIRECTIONAL.md, "the gate that made it work").
const float ACCEL_MAX_PX = 16.0;
const float ACCEL_TRUST_LO = 2.0;
const float ACCEL_TRUST_HI = 5.0;

// Jerk clamp, px per straddle-interval^3. Same physical argument as
// ACCEL_MAX_PX one order up: sustained jerk beyond a few px/interval^3
// exits the search's reach within a couple of frames. The O-series peaks
// at 5.6 (O5) and 0.72 (O6). A reasoned start, not a measured optimum.
const float JERK_MAX_PX = 8.0;

// Deadbands on the WARP's copies of the fields -- never on what the
// diagnostics report. Same trade as tri's accel deadband, ONE ORDER UP --
// and the jerk band had to be measured, not inherited: the uniform jerk
// stencil's coefficients (1,-3,-1)/(1,3,-1) amplify flow noise by
// sqrt(11)/sqrt(2) ~ 2.3x the accel stencil's, and inheriting accel's
// 0.5/1.5 cost 4.9 dB on L1_trans_8px (zero-jerk content). Swept:
//
//   jerk deadband    L1      A2      O3      O4
//   0.5/1.5       55.61   42.70   46.27   47.80
//   1.0/3.0       55.10   42.76   46.27   47.69
//   2.0/4.0       57.22   42.81   46.28   47.58
//   3.0/6.0       60.20   42.81   46.28   47.50
//   jerk OFF      60.55   42.81   45.17   47.24
//
// O3 -- the hardest oscillation, jerk peak ~13.8 px/interval^3 -- keeps its
// FULL +1.1 dB at every setting: its useful jerk lives far above the band.
// L1's noise cost falls monotonically as the band widens. 3.0/6.0 keeps
// all of O3, most of O4's +0.26, costs L1 0.35 dB against jerk-off, and
// returns A2 (true jerk zero) to its jerk-off score exactly.
const float ACCEL_DEADBAND_LO = 0.5;
const float ACCEL_DEADBAND_HI = 1.5;
const float JERK_DEADBAND_LO = 3.0;
const float JERK_DEADBAND_HI = 6.0;

// TRI_DIAG -- keeps the tridirectional shader's name and modes 0-4 so
// every existing instrument (accelcheck.py, accelprospect.sh, trivis.py,
// calsweep drivers) reads this shader unchanged. Two quad-only modes:
//
//   0 = normal output          1 = correction (px)   2 = acceleration
//   3 = |a| heat map           4 = |a| linear luma (measurement, no marker)
//   5 = JERK field, px/interval^3, encoded like mode 2  (marker: magenta)
//   6 = LSQ residual (QUAD_MODE 1) as linear luma -- measurement mode,
//       no marker, in px against RESID_DIAG_FS. The confidence field.
//   7 = VELOCITY field: the straddle-pair flow f_fwd, px/interval,
//       encoded like mode 2 against VEL_DIAG_FS (marker: orange). The
//       zeroth derivative the demo's display was missing -- "moving
//       right" as a solid colour.
int TRI_DIAG = (read_view == 1 || read_view == 4) ? 7 : (read_view == 2 || read_view == 5) ? 2 : 5;

const float ACCEL_DIAG_FS = 2.0;   // px/interval^2 full scale (modes 2, 3)
const float CORR_DIAG_FS  = 0.25;  // px full scale (mode 1)
const float JERK_DIAG_FS  = 2.0;   // px/interval^3 full scale (mode 5)
const float RESID_DIAG_FS = 2.0;   // px full scale (mode 6)
const float VEL_DIAG_FS   = 2.0;   // px/interval full scale (mode 7)

// DIAG_HOLD_ANCHOR = 1 pins the diag modes' anchor to slot 1, so a
// displayed field updates once per window advance (source cadence)
// instead of re-anchoring as the output phase s crosses 0.5. The two
// anchors' stencils sample different flow textures whose sub-pixel
// noise is independent, so per-phase re-anchoring STROBES a live
// display between two decorrelated noise fields (~36 Hz at 24->60,
// measured 1.5 px rms background / 3-4 px mover on the jerk field).
// Default 0 keeps the established instrument semantics -- accelcheck's
// calibrations read the phase-dependent anchor -- and the warp path
// never uses this either way. The demo's field graphs set 1 (gen.sh).
const int DIAG_HOLD_ANCHOR = 1;

vec4 tri_diag_marker() {
    if (TRI_DIAG == 1) return vec4(1.0, 0.2, 0.2, 1.0);   // red     -- correction
    if (TRI_DIAG == 2) return vec4(0.2, 0.6, 1.0, 1.0);   // blue    -- acceleration
    if (TRI_DIAG == 5) return vec4(1.0, 0.2, 1.0, 1.0);   // magenta -- jerk
    if (TRI_DIAG == 7) return vec4(1.0, 0.6, 0.1, 1.0);   // orange  -- velocity
    return vec4(0.2, 1.0, 0.3, 1.0);                      // green   -- magnitude
}

vec4 slot_tex(int i, vec2 uv) {
    if (i == 0) return HOOKED_tex(uv);
    if (i == 1) return FRAME1_tex(uv);
    if (i == 2) return FRAME2_tex(uv);
    return FRAME3_tex(uv);
}

vec4 hook() {
    // ---- roles, derived per output frame from slot-keyed fields ----
    // Straddle pair (p, p+1): p is the last slot at or before the output.
    // Interior 24->60 gives p = 1 every phase; exact N:N gives p = 2 with
    // the output ON slot p (s = 0). All-past windows at a stream's end
    // clamp s to 1 and show the newest frame -- same graceful degrade as
    // the tri shader.
    int p = 0;
    if (rts_mix[1] <= 0.0) p = 1;
    if (rts_mix[2] <= 0.0) p = 2;

    float tA = rts_mix[p];
    float tB = rts_mix[p + 1];
    float L  = tB - tA;                       // straddle interval, > 0
    float s  = clamp((0.0 - tA) / L, 0.0, 1.0);

    vec2 f_fwd = (p == 0 ? FLOW_H_AB_tex(HOOKED_pos).xy
                : p == 1 ? FLOW_H_BC_tex(HOOKED_pos).xy
                         : FLOW_H_CD_tex(HOOKED_pos).xy) * 2.0 * HOOKED_pt;

    // Cut inside the straddling pair: reproduce the cut (base behaviour).
    float cut01 = SCENE_DIFF_tex(vec2(0.5)).r;
    float cut12 = SCENE_DIFF_BC_tex(vec2(0.5)).r;
    float cut23 = SCENE_DIFF_CD_tex(vec2(0.5)).r;
    float cut_straddle = p == 0 ? cut01 : p == 1 ? cut12 : cut23;
    if (cut_straddle > SCENE_CUT_DIFF)
        return s < 0.5 ? slot_tex(p, HOOKED_pos) : slot_tex(p + 1, HOOKED_pos);

    // ---- anchor: the straddling frame nearer the output ----
    // Clamped to the interior slots {1, 2}: both have adjacent flows on
    // both sides, so the cubic needs at most ONE composed link. (p = 0
    // or an s > 0.5 at p = 2 would name an outer slot; the interior
    // neighbour serves instead, still a straddler.)
    int anchor = clamp(s <= 0.5 ? p : p + 1, 1, 2);
    if (TRI_DIAG != 0 && DIAG_HOLD_ANCHOR == 1) anchor = 1;
    bool anchor_is_A = (anchor == p);

    // Anchor's three displacements, their taus (interval units), their
    // round trips, and the cuts that sever them.
    vec2 f_prev, f_next, f_far;
    float rt_prev, rt_next, rt_far;
    float tau_p, tau_n, tau_f;
    float cut_adj, cut_link;

    if (anchor == 1) {
        f_prev = FLOW_F_BA_tex(HOOKED_pos).xy * HOOKED_pt;
        f_next = FLOW_F_BC_tex(HOOKED_pos).xy * HOOKED_pt;
        // Composed two-interval flow: slot1 -> slot2 -> slot3.
        vec2 link = FLOW_F_CD_tex(HOOKED_pos + f_next).xy * HOOKED_pt;
        f_far  = f_next + link;

        vec2 rp = FLOW_F_AB_tex(HOOKED_pos + f_prev).xy * HOOKED_pt;
        rt_prev = length(f_prev + rp) / length(HOOKED_pt);
        vec2 rn = FLOW_F_CB_tex(HOOKED_pos + f_next).xy * HOOKED_pt;
        rt_next = length(f_next + rn) / length(HOOKED_pt);
        vec2 rf = FLOW_F_DC_tex(HOOKED_pos + f_far).xy * HOOKED_pt;
        rt_far  = max(rt_next, length(link + rf) / length(HOOKED_pt));

        tau_p = (rts_mix[0] - rts_mix[1]) / L;
        tau_n = (rts_mix[2] - rts_mix[1]) / L;
        tau_f = (rts_mix[3] - rts_mix[1]) / L;
        cut_adj  = max(cut01, cut12);
        cut_link = cut23;
    } else {
        f_prev = FLOW_F_CB_tex(HOOKED_pos).xy * HOOKED_pt;
        f_next = FLOW_F_CD_tex(HOOKED_pos).xy * HOOKED_pt;
        // Composed two-interval flow: slot2 -> slot1 -> slot0.
        vec2 link = FLOW_F_BA_tex(HOOKED_pos + f_prev).xy * HOOKED_pt;
        f_far  = f_prev + link;

        vec2 rp = FLOW_F_BC_tex(HOOKED_pos + f_prev).xy * HOOKED_pt;
        rt_prev = length(f_prev + rp) / length(HOOKED_pt);
        vec2 rn = FLOW_F_DC_tex(HOOKED_pos + f_next).xy * HOOKED_pt;
        rt_next = length(f_next + rn) / length(HOOKED_pt);
        vec2 rf = FLOW_F_AB_tex(HOOKED_pos + f_far).xy * HOOKED_pt;
        rt_far  = max(rt_prev, length(link + rf) / length(HOOKED_pt));

        tau_p = (rts_mix[1] - rts_mix[2]) / L;
        tau_n = (rts_mix[3] - rts_mix[2]) / L;
        tau_f = (rts_mix[0] - rts_mix[2]) / L;
        cut_adj  = max(cut12, cut23);
        cut_link = cut01;
    }

    // ---- the solve ----
    vec2 accel = vec2(0.0);
    vec2 jerk  = vec2(0.0);
    float resid = 0.0;

    if (QUAD_MODE == 0) {
        // Exact cubic through the three displacements. Written as the
        // general Vandermonde solve so non-uniform (VFR) spacing is exact;
        // at uniform spacing the acceleration row reduces to
        // a = f_next + f_prev, i.e. the tridirectional estimate.
        mat3 M = mat3(
            vec3(tau_p, tau_n, tau_f),
            vec3(tau_p * tau_p, tau_n * tau_n, tau_f * tau_f) * 0.5,
            vec3(tau_p * tau_p * tau_p, tau_n * tau_n * tau_n,
                 tau_f * tau_f * tau_f) / 6.0);
        if (abs(determinant(M)) > 1.0e-4) {
            mat3 Mi = inverse(M);
            vec3 sx = Mi * vec3(f_prev.x, f_next.x, f_far.x);
            vec3 sy = Mi * vec3(f_prev.y, f_next.y, f_far.y);
            accel = vec2(sx.y, sy.y);
            jerk  = vec2(sx.z, sy.z);
        }
    } else {
        // Least-squares quadratic over all three flows (EQVI's RQFP),
        // residual read out as the confidence field.
        float S2 = tau_p * tau_p + tau_n * tau_n + tau_f * tau_f;
        float S3 = tau_p * tau_p * tau_p + tau_n * tau_n * tau_n
                 + tau_f * tau_f * tau_f;
        float S4 = tau_p * tau_p * tau_p * tau_p
                 + tau_n * tau_n * tau_n * tau_n
                 + tau_f * tau_f * tau_f * tau_f;
        float det = S2 * (S4 * 0.25) - (S3 * 0.5) * (S3 * 0.5);
        if (abs(det) > 1.0e-4) {
            vec2 b1 = tau_p * f_prev + tau_n * f_next + tau_f * f_far;
            vec2 b2 = (tau_p * tau_p * f_prev + tau_n * tau_n * f_next
                     + tau_f * tau_f * f_far) * 0.5;
            vec2 v = ((S4 * 0.25) * b1 - (S3 * 0.5) * b2) / det;
            accel  = (S2 * b2 - (S3 * 0.5) * b1) / det;
            vec2 rp2 = v * tau_p + 0.5 * accel * tau_p * tau_p - f_prev;
            vec2 rn2 = v * tau_n + 0.5 * accel * tau_n * tau_n - f_next;
            vec2 rf2 = v * tau_f + 0.5 * accel * tau_f * tau_f - f_far;
            resid = max(length(rp2), max(length(rn2), length(rf2)))
                  / length(HOOKED_pt);
        }
    }

    // ---- trust: round-trip provenance, per order ----
    // The acceleration row of the cubic is (at uniform spacing) built from
    // f_prev and f_next alone, so it takes the tri shader's two-flow gate
    // unchanged. Jerk -- and the LSQ fit, which mixes all three flows into
    // everything -- answers additionally for the composed link.
    float g2 = 1.0 - smoothstep(ACCEL_TRUST_LO, ACCEL_TRUST_HI,
                                max(rt_prev, rt_next));
    float g3 = 1.0 - smoothstep(ACCEL_TRUST_LO, ACCEL_TRUST_HI,
                                max(max(rt_prev, rt_next), rt_far));
    if (QUAD_MODE == 0) {
        accel *= g2;
        jerk  *= g3;
    } else {
        accel *= g3;
    }

    // Cuts degrade in order: a cut severing an anchor-adjacent pair kills
    // the whole estimate (bidirectional behaviour); one severing only the
    // composed link's far pair kills jerk (tridirectional behaviour).
    if (cut_adj > SCENE_CUT_DIFF) {
        accel = vec2(0.0);
        jerk  = vec2(0.0);
    } else if (cut_link > SCENE_CUT_DIFF) {
        jerk = vec2(0.0);
    }

    vec2 amax = ACCEL_MAX_PX * HOOKED_pt;
    accel = clamp(accel, -amax, amax);
    vec2 jmax = JERK_MAX_PX * HOOKED_pt;
    jerk = clamp(jerk, -jmax, jmax);

    // ---- cubic placement ----
    // Deviation of the constant-jerk trajectory from the straddle chord,
    // with the anchor at one end of the chord:
    //
    //   corr = s(1-s) * ( a/2 + (j/6) * (anchor==A ? (1+s) : -(2-s)) )
    //
    // j = 0 reduces it to tri's s(1-s)*a/2; a = j = 0 to the bidirectional
    // warp. Warp copies are deadbanded; the reported fields are not.
    vec2 accel_w = accel;
    if (ACCEL_DEADBAND_HI > 0.0)
        accel_w *= smoothstep(ACCEL_DEADBAND_LO, ACCEL_DEADBAND_HI,
                              length(accel / HOOKED_pt));
    vec2 jerk_w = jerk;
    if (JERK_DEADBAND_HI > 0.0)
        jerk_w *= smoothstep(JERK_DEADBAND_LO, JERK_DEADBAND_HI,
                             length(jerk / HOOKED_pt));

    float jgeom = anchor_is_A ? (1.0 + s) : -(2.0 - s);
    vec2 corr = s * (1.0 - s) * (0.5 * accel_w + jerk_w * (jgeom / 6.0));

    if (TRI_DIAG != 0) {
        // Measurement modes first (no marker; whole-frame statistics feed
        // signalstats directly -- see the tri shader's mode 4 note).
        if (TRI_DIAG == 4)
            return vec4(vec3(clamp(length(accel / HOOKED_pt) / ACCEL_DIAG_FS,
                                   0.0, 1.0)), 1.0);
        if (TRI_DIAG == 6)
            return vec4(vec3(clamp(resid / RESID_DIAG_FS, 0.0, 1.0)), 1.0);


        if (TRI_DIAG == 1)
            return vec4(corr / HOOKED_pt, 0.0, 1.0);
        if (TRI_DIAG == 2)
            return vec4(accel / HOOKED_pt, 0.0, 1.0);
        if (TRI_DIAG == 5)
            return vec4(jerk / HOOKED_pt, 0.0, 1.0);
        if (TRI_DIAG == 7)
            return vec4(f_fwd / HOOKED_pt, 0.0, 1.0);

        float m = clamp(length(accel / HOOKED_pt) / ACCEL_DIAG_FS, 0.0, 1.0);
        vec3 c = m < 0.5 ? mix(vec3(0.0, 0.0, 0.25), vec3(0.0, 0.9, 0.9), m * 2.0)
                         : mix(vec3(0.0, 0.9, 0.9), vec3(1.0, 0.1, 0.0), (m - 0.5) * 2.0);
        return vec4(c, 1.0);
    }

    vec2 uv_a = HOOKED_pos - f_fwd * s + corr;
    vec2 uv_b = HOOKED_pos + f_fwd * (1.0 - s) + corr;

    vec4 sa = slot_tex(p, uv_a);
    vec4 sb = slot_tex(p + 1, uv_b);

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

// three- and four-frame family: velocity, acceleration and jerk from this shader's own stencil
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
