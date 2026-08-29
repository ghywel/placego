// bidirectional-interpolation.glsl
//
// Real motion-compensated frame interpolation for libplacebo's custom
// shader hook system, targeting the PL_HOOK_FRAME_MIX stage.
//
// REQUIRES a libplacebo build patched with frame-mix-hook.patch (see
// README.md) -- stock libplacebo has no PL_HOOK_FRAME_MIX stage, and this
// version additionally requires the `pair_changed` field added to
// `pl_hook_params` (same patch, later revision -- if you built this
// project before the "storage-based flow caching" work, re-apply the
// updated patch).
//
// Algorithm: 4-level coarse-to-fine block-matching pyramid (sixteenth res
// -> eighth -> quarter -> half), 5x5 SAD windows, genuine BIDIRECTIONAL
// flow (A->B and B->A computed independently through the same pyramid,
// not just a sign-flipped approximation), and a forward/backward
// consistency check used for real occlusion detection: where the two flow
// fields disagree (indicating a pixel that's only visible in one of the
// two source frames), the final blend favors the non-occluded source
// instead of ghosting the two together. Targets modern GPUs with headroom
// to spare -- this is roughly 2x the search cost of the medium tier due to
// computing both flow directions.
//
// Storage-based flow caching: all 8 flow-search passes (both directions,
// all 4 pyramid levels) plus both directions' *second* vector-median-
// filter pass (10 persistent storage-image textures total) are gated on
// `pair_changed`. At a 24->60fps (2.5x) ratio, 2-3 consecutive output
// frames share the same source pair and only differ in `mix_t` -- the
// flow field itself is provably identical across them (it never depends
// on `mix_t`), so recomputing it on every single output frame is wasted
// GPU work. When `pair_changed` is false, each cached pass just reads
// back its stored result instead of redoing the work. Confirmed working
// (red/green cache-hit indicator in interpolate-debug-grid.glsl, plus
// measured ~20-30% faster end-to-end than the same algorithm with
// caching removed) before the median filter was added to the cache; the
// median filter was the single largest *uncached* cost remaining (a 9x9
// pairwise-distance comparison at half resolution, comparable to or
// larger than the entire search it was sitting next to), so caching it
// too should meaningfully close the gap between measured and
// theoretical speedup -- re-verify the red/green pattern and fps after
// this change, same as after the original caching work. Each median
// filter's *first* pass has no cache of its own (its output only feeds
// the second pass within the same dispatch) -- it returns a cheap dummy
// on a cache hit instead. Luma downsampling remains deliberately
// uncached (cheap enough that caching it isn't worth the complexity).
//
// Caveat: the TEXTURE/STORAGE size declaration only accepts literal
// integers (no `HOOKED.w`-style expressions like the WIDTH/HEIGHT
// declarations on hook passes support), so each cache texture is sized
// to a fixed ceiling (full-res 3840x2160 / 4K, scaled per pyramid level)
// rather than the actual video resolution, and the shader only ever
// touches the sub-rectangle matching the real resolution. Source video
// larger than 4K will read/write outside the allocated cache texture --
// undefined behavior, not just wasted memory. Bump the SIZE values (and
// this comment) if you need to support larger sources.
//
// The `pair_changed` signal only tracks whether *this renderer's* source
// pair changed; if you ever see stale-looking flow after a seek or
// stream discontinuity, that's the first place to look (the cache has no
// explicit invalidation on discontinuities beyond the natural signature
// change when decode resumes with different frames) -- not yet stress-
// tested against seeking.
//
// Bound automatically by the FRAME_MIX hook stage:
//   HOOKED  = source frame immediately before the output timestamp
//   NEXT    = source frame immediately after the output timestamp
//   mix_t   = 0.0 (at HOOKED) .. 1.0 (at NEXT) position of the output frame
//   pair_changed = true if HOOKED/NEXT differ from the previous call on
//                  this renderer (see "Storage-based flow caching" above)

// ---------------------------------------------------------------------
// Sixteenth-res luma (coarsest search level)
// ---------------------------------------------------------------------
//!HOOK FRAME_MIX
//!BIND HOOKED
//!SAVE LUMA_A_S
//!WIDTH HOOKED.w 16 /
//!HEIGHT HOOKED.h 16 /
//!COMPONENTS 1
//!DESC [high] downsample frame A to 1/16 res (luma)
vec4 hook() {
    return vec4(dot(HOOKED_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!HOOK FRAME_MIX
//!BIND NEXT
//!SAVE LUMA_B_S
//!WIDTH HOOKED.w 16 /
//!HEIGHT HOOKED.h 16 /
//!COMPONENTS 1
//!DESC [high] downsample frame B to 1/16 res (luma)
vec4 hook() {
    return vec4(dot(NEXT_tex(NEXT_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
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
//!DESC [high] scene-cut statistic (whole-frame luma difference)
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
                if (cost < best_cost) {
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
                if (cost < best_cost) {
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
//!SAVE LUMA_A_E
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 1
//!DESC [high] downsample frame A to 1/8 res (luma)
vec4 hook() {
    return vec4(dot(HOOKED_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!HOOK FRAME_MIX
//!BIND NEXT
//!SAVE LUMA_B_E
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 1
//!DESC [high] downsample frame B to 1/8 res (luma)
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
    float best_cost = sad5x5_e(uv_a, uv_a + base_off);

    for (int y = -REFINE_SEARCH_RADIUS; y <= REFINE_SEARCH_RADIUS; y++) {
        for (int x = -REFINE_SEARCH_RADIUS; x <= REFINE_SEARCH_RADIUS; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 off = base_off + vec2(float(x), float(y)) * LUMA_A_E_pt;
            float cost = sad5x5_e(uv_a, uv_a + off)
                       + REFINE_REG_LAMBDA * length(vec2(float(x), float(y)));
            if (cost < best_cost) {
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
    float best_cost = sad5x5_e2(uv_b, uv_b + base_off);

    for (int y = -REFINE_SEARCH_RADIUS; y <= REFINE_SEARCH_RADIUS; y++) {
        for (int x = -REFINE_SEARCH_RADIUS; x <= REFINE_SEARCH_RADIUS; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 off = base_off + vec2(float(x), float(y)) * LUMA_A_E_pt;
            float cost = sad5x5_e2(uv_b, uv_b + off)
                       + REFINE_REG_LAMBDA * length(vec2(float(x), float(y)));
            if (cost < best_cost) {
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
//!DESC [high] downsample frame A to 1/4 res (luma)
vec4 hook() {
    return vec4(dot(HOOKED_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!HOOK FRAME_MIX
//!BIND NEXT
//!SAVE LUMA_B_Q
//!WIDTH HOOKED.w 4 /
//!HEIGHT HOOKED.h 4 /
//!COMPONENTS 1
//!DESC [high] downsample frame B to 1/4 res (luma)
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
    float best_cost = sad5x5_q(uv_a, uv_a + base_off);

    for (int y = -REFINE_SEARCH_RADIUS; y <= REFINE_SEARCH_RADIUS; y++) {
        for (int x = -REFINE_SEARCH_RADIUS; x <= REFINE_SEARCH_RADIUS; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 off = base_off + vec2(float(x), float(y)) * LUMA_A_Q_pt;
            float cost = sad5x5_q(uv_a, uv_a + off)
                       + REFINE_REG_LAMBDA * length(vec2(float(x), float(y)));
            if (cost < best_cost) {
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
    float best_cost = sad5x5_q2(uv_b, uv_b + base_off);

    for (int y = -REFINE_SEARCH_RADIUS; y <= REFINE_SEARCH_RADIUS; y++) {
        for (int x = -REFINE_SEARCH_RADIUS; x <= REFINE_SEARCH_RADIUS; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 off = base_off + vec2(float(x), float(y)) * LUMA_A_Q_pt;
            float cost = sad5x5_q2(uv_b, uv_b + off)
                       + REFINE_REG_LAMBDA * length(vec2(float(x), float(y)));
            if (cost < best_cost) {
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
//!DESC [high] downsample frame A to half res (luma)
vec4 hook() {
    return vec4(dot(HOOKED_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}

//!HOOK FRAME_MIX
//!BIND NEXT
//!SAVE LUMA_B_H
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 1
//!DESC [high] downsample frame B to half res (luma)
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
    float best_cost = sad3x3_h(uv_a, uv_a + base_off);

    for (int y = -REFINE_SEARCH_RADIUS; y <= REFINE_SEARCH_RADIUS; y++) {
        for (int x = -REFINE_SEARCH_RADIUS; x <= REFINE_SEARCH_RADIUS; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 off = base_off + vec2(float(x), float(y)) * LUMA_A_H_pt;
            float cost = sad3x3_h(uv_a, uv_a + off)
                       + REFINE_REG_LAMBDA * length(vec2(float(x), float(y)));
            if (cost < best_cost) {
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
    float best_cost = sad3x3_h2(uv_b, uv_b + base_off);

    for (int y = -REFINE_SEARCH_RADIUS; y <= REFINE_SEARCH_RADIUS; y++) {
        for (int x = -REFINE_SEARCH_RADIUS; x <= REFINE_SEARCH_RADIUS; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 off = base_off + vec2(float(x), float(y)) * LUMA_A_H_pt;
            float cost = sad3x3_h2(uv_b, uv_b + off)
                       + REFINE_REG_LAMBDA * length(vec2(float(x), float(y)));
            if (cost < best_cost) {
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

    float best_cost = 1e30;
    vec2 best = v[4];
    for (int i = 0; i < 9; i++) {
        float cost = 0.0;
        for (int j = 0; j < 9; j++)
            cost += length(v[i] - v[j]);
        if (cost < best_cost) {
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

    float best_cost = 1e30;
    vec2 best = v[4];
    for (int i = 0; i < 9; i++) {
        float cost = 0.0;
        for (int j = 0; j < 9; j++)
            cost += length(v[i] - v[j]);
        if (cost < best_cost) {
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

    float best_cost = 1e30;
    vec2 best = v[4];
    for (int i = 0; i < 9; i++) {
        float cost = 0.0;
        for (int j = 0; j < 9; j++)
            cost += length(v[i] - v[j]);
        if (cost < best_cost) {
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

    float best_cost = 1e30;
    vec2 best = v[4];
    for (int i = 0; i < 9; i++) {
        float cost = 0.0;
        for (int j = 0; j < 9; j++)
            cost += length(v[i] - v[j]);
        if (cost < best_cost) {
            best_cost = cost;
            best = v[i];
        }
    }

    vec4 result = vec4(best, 0.0, 0.0);
    imageStore(FLOW_H_BA_MEDIAN_CACHE, coord, result);
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
//!BIND NEXT
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
//!DESC [high] motion-gated spatial edge mask (frame B)

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
// Final pass: bidirectional warp with forward/backward consistency-based
// occlusion detection, full resolution
// ---------------------------------------------------------------------
//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND SCENE_DIFF
//!BIND NEXT
//!BIND FLOW_H_AB
//!BIND EDGE_A
//!BIND EDGE_B
//!SAVE FRAME_MIX
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!DESC [high] motion-compensated warp

// Sampling the source textures at a fractional pixel position always
// blends between the 4 nearest texels (linear filtering), which is what
// a soft/blurred edge actually is -- not a flow error. Snapping the UV to
// the exact center of the nearest source texel first makes that same
// linear sample degenerate to picking a single texel, i.e. effectively
// nearest-neighbor sampling, without needing a different sampler.
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

// snap_texel() is a *discontinuous* function of the warp position: it
// jumps to a different source texel the instant the true (unsnapped)
// position crosses a texel boundary. flow_ab itself varies smoothly
// across output pixels (it's a bilinear read of a half-res flow field),
// but any real flow estimate still carries some sub-texel imprecision on
// top of that smooth variation -- invisible on ordinary content, since
// neighboring texels usually look similar anyway, but for a source
// texture with thin, high-contrast linework (e.g. a cartoon's black
// outlines), that sub-texel noise is enough to make adjacent output
// pixels land on opposite sides of a boundary purely by chance: one
// hits the outline texel, its neighbor misses onto the background one
// instead, producing a crisp but *fragmented*, dashed-looking line
// (confirmed on real footage: Bluey's ear outlines breaking up against
// the background, despite a clean, low-noise flow field in the debug
// visualization -- this is a sampling artifact downstream of the flow,
// not a flow quality problem).
//
// Rather than a single global blend toward bilinear (which softens this
// everywhere to fix a problem that only happens in specific spots), use
// EDGE_A/EDGE_B (above) as an independent check on whether the snap
// actually landed where an edge was expected. EDGE_A_tex(uv) at the
// *unsnapped* position is a smooth (bilinearly filtered, so continuous,
// unlike the snap itself) "is a moving edge expected here" signal;
// EDGE_A_tex(snapped_uv) is the exact value of whichever single texel
// the snap landed on (sampling a stored texture exactly at a texel
// center degenerates to reading that texel, the same trick snap_texel
// itself relies on). Where they agree -- both near 0 (no edge expected
// or found) or both near 1 (an edge was expected and the snap found
// one) -- the snap is confirmed correct and gets trusted fully. Where
// they disagree -- an edge was confidently expected but the snap missed
// onto background, or vice versa -- that is precisely the coin-flip case
// that fragments a line, so fall back toward bilinear only for that
// specific sample.
float edge_consistency(float expected, float snapped) {
    return 1.0 - abs(expected - snapped);
}

// TESTING at 0.0 (was 1.0). Real-hardware isolation via
// interpolate-debug-warp-stages.glsl found the reported "smudge tool,
// parts left behind" defect already present -- exaggerated, even -- in
// warp_sample_a/b's own output alone, before any cross-direction blend
// or occlusion fallback runs at all. That points at this mechanism: the
// per-pixel edge_consistency() check above reads as "confirmed correct,
// trust the snap fully" whenever `expected` and `snapped_edge` AGREE --
// but they agree just as strongly when both correctly read "no edge
// here" (true for most of any real frame -- flat regions, smooth
// gradients, anything that never crosses SPATIAL_EDGE_THRESHOLD) as when
// both correctly confirm a genuine edge, which is the only case this
// mechanism was actually designed to trust. With SNAP_STRENGTH at 1.0,
// that means ordinary non-edge content gets snapped to nearest-neighbor
// too, not just genuine hard edges -- and nearest-neighbor sampling
// through a smooth gradient during motion produces a stepped, quantized
// look rather than a smooth pull, plausibly exactly the reported defect.
// At 0.0 this reduces to pure bilinear at the warped position (the
// mechanism fully disabled) -- if the defect clears up, that confirms
// this is the cause; if it's completely unchanged even at 0.0, that
// rules this whole mechanism out and points back at the flow field's
// actual values (not just its visual smoothness) or the base warp
// position math instead. Not yet confirmed either way.
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

// NO OCCLUSION FALLBACK -- and that is a deliberate, tested decision.
//
// This pass used to detect unreliable flow via forward/backward consistency
// and substitute a non-warped frame there. Three successive versions of that
// idea were built and each was worse than having none at all:
//
//   1. `mix_t < 0.5 ? unwarped_A : unwarped_B`, gated at (4,7) px of
//      round-trip error. The hard switch jumped by the full inter-frame
//      displacement as mix_t crossed the midpoint, once per source pair --
//      an 8.75x periodic spike in frame-to-frame change on real footage
//      against 1.43x for a plain blend. It reads as a wobble that snaps.
//   2. The same, made continuous (`mix(A, B, mix_t)`) and the gate raised to
//      (20,30). This removed the snap (8.75x -> 1.24x) but replaced it with a
//      translucent DOUBLED CONTOUR along any moving edge -- inevitable, since
//      it blends two unwarped frames in which the edge is in different
//      places.
//   3. Directional handling: judge each side's reliability at its own sample
//      position and weight toward the self-consistent one, using the WARPED
//      sample so no ghost is possible. Better than (2), still worse than
//      removing the fallback.
//
// Confirmed by direct viewing of all three against no fallback at all, on a
// clip cut specifically around the artifact (a head translocating faster than
// its surroundings): no-fallback was cleanest in every comparison. Whole-frame
// SSIM disagrees, marginally (about 0.002), but that metric is demonstrably
// blind to this defect -- it rates the segment *containing* the artifact as
// the best of three. Where a metric cannot see the thing being judged, it does
// not get the casting vote.
//
// Why removing it works: mc_result already degrades gracefully on its own.
// Both samples use the same flow, so where that flow is wrong they are wrong
// *together and in the same direction*, which stays spatially coherent; and
// as mix_t approaches 0 or 1 the blend converges on the unwarped nearest
// frame anyway, continuously. Substituting an unwarped frame mid-interval
// buys nothing and costs an edge.
//
// The forward/backward consistency computation is gone with it (it fed
// nothing else), which also saves a full-resolution texture fetch per pixel.
// `interpolate-debug-grid.glsl` still VISUALISES that consistency error, which
// remains diagnostically useful even though nothing acts on it now.
// Chosen from measurement, and the number is a compromise rather than a
// solution. Scored against 134 cuts across 12986 non-cut pairs on three clips
// (dark night, bright action, flat animation):
//
//     0.120   100/134 caught (75%)   21 false -- but 9 of those on the
//                                    bright-action clip, where a wrong fire
//                                    snaps a frame that should be blended
//     0.125    96/134 caught (72%)   12 false, NONE on bright action
//     0.150    88/134 caught (66%)    9 false
//
// The bright-action clip binds it: its highest non-cut reading is 0.1224, so
// anything below 0.125 starts snapping correctly-interpolable frames on
// material that is otherwise clean. 0.125 sits just above that and buys eight
// more cuts for three more false positives in thirteen thousand.
//
// Recall is 72%, not 100%. A first calibration used only the ten strongest
// cuts as ground truth and appeared to catch all of them; scoring against a
// fuller list showed that was an artefact of the ground truth, not a property
// of the gate. Cuts between visually similar shots are missed, and one such
// was confirmed by eye at 27.9s. Those are also the ones that do least visible
// harm when blended, which is why this remains worth shipping -- but it is a
// partial fix and should not be described otherwise.
const float SCENE_CUT_DIFF = 0.125;

vec4 hook() {
    // Too different to blend: reproduce the cut instead of averaging across
    // it. See the SCENE-CUT GATE note above for why a hard switch is correct
    // here and was not for occlusion.
    if (SCENE_DIFF_tex(vec2(0.5)).r > SCENE_CUT_DIFF)
        return mix_t < 0.5 ? HOOKED_tex(HOOKED_pos) : NEXT_tex(NEXT_pos);

    // flow_ab = displacement from A's position to the matching position in B,
    // i.e. A(x) ~= B(x + flow_ab(x)). For output pixel p at time t, the
    // source position in A is p - flow_ab*t; in B it's p + flow_ab*(1-t).
    vec2 flow_ab = FLOW_H_AB_tex(HOOKED_pos).xy * 2.0 * HOOKED_pt;

    vec4 warped_a = warp_sample_a(HOOKED_pos - flow_ab * mix_t);
    vec4 warped_b = warp_sample_b(NEXT_pos + flow_ab * (1.0 - mix_t));

    return mix(warped_a, warped_b, mix_t);
}
