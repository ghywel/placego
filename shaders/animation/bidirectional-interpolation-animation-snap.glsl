// bidirectional-interpolation-animation.glsl
//
// A VARIANT of bidirectional-interpolation-propagated.glsl tuned for
// ANIMATION: hand-drawn or cel-shaded content, where fills are flat, the
// information is in the line art, and there is no natural depth -- the
// camera may pan or push over a painted world, but shading defaults to
// flat. Same passes as the propagated shader, same cost (about +13% over
// the stock shader); one constant differs. Kept as its own file because
// the setting that is best on flat-shaded line art gives up a little on
// plain rotation and on fast textured translations, which is the wrong
// trade for live action and the right one here. The three- and four-frame
// shaders built on this base are generated with the base argument:
//
//   ./tests/gen_tridirectional.py  tridirectional-interpolation-animation.glsl  bidirectional-interpolation-animation.glsl
//   ./tests/gen_quaddirectional.py quaddirectional-interpolation-animation.glsl bidirectional-interpolation-animation.glsl
//
// WHAT DIFFERS. The propagated shader's check pass blends -- takes zero flow
// instead of the refine's -- wherever a textured texel's propagated
// consensus contradicts the refine's flow by more than PROP_DISAGREE texels
// or PROP_DISAGREE_REL times the flow's own length: a flow its own
// neighbourhood disagrees with is an alias suspect, and an alias scores the
// same SAD as the truth. The general file sets PROP_DISAGREE to 1.5 texels
// of the 1/8 level; this one sets 0.75. On line art the tracker's wrong
// flows are small and scattered (the aperture problem along an edge, not a
// lattice alias texels away), so the finer threshold catches them; the
// relative term keeps a pan from being mistaken for one.
//
// WHAT WAS MEASURED, same harness, same day as the propagated shader.
// Flat-shaded anime, decimate-and-reconstruct: 42.50 dB against the
// propagated shader's 40.98, the seeded base's 36.89 and the 115-pass
// variational build's 42.48 -- the fast tier matches the recommended
// viewing shader on this content at a third of the passes. The other anime
// segment 47.22 (propagated 47.21, variational 46.83). Live action is a
// wash: 35.25 / 46.62 / 33.31 / 33.33 dB against the propagated shader's
// 35.28 / 46.58 / 33.39 / 33.30. Ladder against the seeded base: +2.14 dB
// mean, the same as the propagated shader, with R3 +1.0 and A5 +0.2 more
// and R1 -0.6, L7 -0.4, L4 -0.3 less; the three cases below the seeded
// base are L7 -1.8, L4 -1.3, L1 -0.2. A finer threshold still (0.5) changes
// nothing measurable; the fixed 0.75 without the relative term reaches
// 43.1 dB on the anime but loses 2 dB on plain translations and 0.8 on
// live action, so it is not shipped. NFRAME-LIMITS.md section 8 has the
// whole account.
//
// The propagated shader's header follows, then the seeded variant's;
// everything they say applies unchanged here.
//
// ---- bidirectional-interpolation-propagated.glsl's header, kept verbatim ----
//
// A VARIANT of bidirectional-interpolation-seeded.glsl, which is itself a
// variant of bidirectional-interpolation.glsl: the seeded base, byte for
// byte, plus eight passes at the 1/8-resolution level. Kept as its own file
// because it costs render time: measured +1-4% over the seeded base and
// about +13% over the stock shader (O5 at 24->60, 60 output frames,
// ffmpeg's benchmark clock, median of three; NFRAME-LIMITS.md section 8).
// If that is inside your budget it is above the seeded base on every real
// segment measured and on 21 of 32 ladder cases; if it is not, the seeded
// base is the fast tier. The three- and four-frame shaders built on this
// base are generated with the base argument the generators take (which
// carry a base's extra passes into every pair's chain):
//
//   ./tests/gen_tridirectional.py  tridirectional-interpolation-propagated.glsl  bidirectional-interpolation-propagated.glsl
//   ./tests/gen_quaddirectional.py quaddirectional-interpolation-propagated.glsl bidirectional-interpolation-propagated.glsl
//
// WHAT IT IS FOR. On flat-shaded line art -- anime -- the fast tier's loss
// against the variational build sits on the EDGES, not in the flat fills:
// split by local texture, every build including plain blending scores
// 46-47 dB on the flattest quartile of a real anime frame, and the whole
// gap is in the most textured quartile (base 29.6, variational 36.0 dB).
// An edge constrains one component of motion (the aperture problem), the
// block matcher's descent wanders along it, and only coherence from the
// corners and junctions along the edge fixes it -- which the variational
// cascade buys with 80 Horn-Schunck passes. And on lattice-like textures
// the coarse search returns an alias of the motion (NFRAME-LIMITS.md
// section 3); where the neighbourhood disagrees with such a flow, a plain
// blend beats warping on it.
//
// WHAT CHANGED. After the 1/8-level refine, three Jacobi passes per
// direction: each texel takes the contrast-weighted mean of its 5x5
// neighbours' flow (a neighbour votes in proportion to its own 5x5 luma
// range, capped at PROP_CONF_FULL), mixed with its own flow in proportion to
// PROP_SELF_WEIGHT times its contrast squared. A textured texel keeps its
// flow; a flat one inherits its confident neighbours'. Reach: 16 px per
// pass. Then one check pass per direction scores three candidates on the
// 1/8-level luma over a 5x5 window -- the propagated flow, the refine's
// own, and zero. For a textured texel: the propagated flow if it strictly
// beats the others by PROP_CHECK_MARGIN; else ZERO (a blend) if the
// consensus disagrees with the refine's flow by more than PROP_DISAGREE
// texels or PROP_DISAGREE_REL times the flow's own length, whichever is
// larger, because a flow its own neighbourhood contradicts is an alias
// suspect and an alias scores the same SAD as the truth (the relative
// term keeps a fast translation, whose consensus is diluted by background
// votes near its edges, from being mistaken for one); else the propagated
// flow if within the margin of the best, else the refine's own or zero.
// For a flat texel: the propagated flow only if it strictly beats both
// (the only evidence is an edge inside the window), else zero, which is
// invisible in the warp and is the base's own prior. Without the check a
// static flat background beside a moving object inherits the object's
// flow and the ladder's clean translations lose 8-22 dB; with it they hold.
//
// WHAT WAS MEASURED, against the seeded base, same harness, same night.
// Ladder, 32 cases: +2.14 dB mean, 21 cases up by more than 0.1, three
// down: L7 -1.4, L4 -1.0 (a 40 px/frame translation; still 2.5 dB above
// blending), L1 -0.2. Largest gains, the lattice-textured cases: O6 +11.8,
// A5 +11.1, A6 +9.8, O5 +7.0, A7 +6.8, A4 +4.6, R3 +4.1; then F2 +2.7,
// R2 +2.5, R1 +2.4, F1 +2.3, L3 +1.8. Real footage,
// decimate-and-reconstruct, PSNR of the synthesised frames: the avengers
// clip's five segments 34.74 -> 35.28 dB (SSIM 0.9663 -> 0.9696; the stock
// base 34.29); five library segments, all up -- anime 46.67 -> 47.21
// (above the variational's 46.83 there) and 36.89 -> 40.98 (the
// variational: 42.48), film 45.66 -> 46.58 and 32.58 -> 33.39, a 30 fps
// show 32.12 -> 33.30. SSIM up on all six.
//
// WHAT IT DOES NOT DO. The unchecked propagation reaches 41.6 dB on the
// flat-shaded anime; a version that blends wherever a flow cannot prove
// itself against zero beats the variational on both anime segments and
// lifts the lattice cases further, but collapses every smooth case; a
// fixed disagreement threshold of 0.75 texels reaches 43.1 dB on that
// anime (above the variational) at the cost of 2 dB on the plain
// translations and 0.6 on live action; a fixed 1.5 gives 0.1-0.4 dB more
// on four lattice cases and 0.8 less on L4, 0.2-0.3 less on live action.
// Those are the knobs; NFRAME-LIMITS.md section 8 has the whole account.
//
// The seeded variant's own header follows; everything it says about the
// three coarse seeds and the round-trip gate applies unchanged here.
//
// ---- bidirectional-interpolation-seeded.glsl's header, kept verbatim ----
//
// A VARIANT of bidirectional-interpolation.glsl. Same pyramid, same passes,
// same everything from the quarter-resolution level down; the difference is
// how the two coarsest levels choose the motion they hand to the finer ones.
// Kept as its own file, and the stock shader left byte-identical, because it
// costs render time: measured +10% on the bidirectional shader and +10% on
// the four-frame shader generated from it (O5 at 24->60, 60 output frames,
// ffmpeg's benchmark clock, median of three runs; NFRAME-LIMITS.md section 8).
// If that is inside your budget it is a strict improvement on the synthetic
// ladder and a small, consistent one on real footage; if it is not, the stock
// file is a fifth of the variational build's passes and still the fast tier.
// The three- and four-frame shaders built on this base are generated with the
// base argument the generators take:
//
//   ./tests/gen_tridirectional.py  tridirectional-interpolation-seeded.glsl  bidirectional-interpolation-seeded.glsl
//   ./tests/gen_quaddirectional.py quaddirectional-interpolation-seeded.glsl bidirectional-interpolation-seeded.glsl
//
// This file replaced the `-twoseed` variant of the same day (two descents, no
// temporal seed); that one is in the git history, and its numbers stay in
// NFRAME-LIMITS.md section 8 as the record of how this one was arrived at.
//
// WHAT CHANGED. The stock coarse search is not a window search: it is a
// five-iteration 3x3 descent from zero offset, on a luma pyramid that is
// point-sampled. On any texture with a repeat, that descent lands on the
// nearest integer-texel minimum of the aliased pattern, the next level's
// +/-2-texel refine then reaches the texture's own symmetry vector, and no
// finer level can reject that alias by SAD because its SAD is identically
// zero. Measured on the ladder's A7 (a sine-product texture, period 40 px):
// 39-75% of the velocity field wrong on mid-speed frames, the readings
// sitting exactly at d + (20, -20) and d + (40, 0). The full account is
// NFRAME-LIMITS.md section 8 and THREEDIMENSIONAL.md section 9.7.
//
// So each coarse pass now runs THREE descents and stores three seeds:
//   A  from zero                       -- the stock path, unchanged;
//   B  from the best point of the +/-1-texel ring that lies at least 0.75
//      texel from A, so it cannot fall into A's basin;
//   C  from the previous window's coarse flow at this texel, read from the
//      storage cache before this pass overwrites it.
// A and B ride in the existing rgba32f cache (.xy and .zw; the stock shader
// used only .xy); C lives in a second storage cache per coarse pass. Each
// 1/8-resolution pass refines all three with its unchanged 5x5 search and
// keeps the one with the lowest
//     SAD + SEED_MAG_LAMBDA * |offset| + SEED_TEMP_LAMBDA * |offset - previous flow|
// in that level's texels.
//
// The temporal seed is GATED. An ungated version of C re-seeded its own
// mistakes: a wrong flow, once cached, was found again next window, and the
// accelerating-texture case A5 fell 2.9 dB below stock with a field that
// lagged the motion (hysteresis). So C and its prior are used only where
// the cached forward flow and the reverse flow at its landing point close a
// round trip within SEED_RT_MAX (1.0 texel at the 1/8 level); elsewhere C
// scores as infinitely bad and SEED_TEMP_LAMBDA is zero, and the pass is
// exactly the two-seed variant. With the gate, A5 reads frame by frame like
// stock and scores above it. The two priors' weights are measured, not
// chosen: the magnitude prior has a knee at 0.3 (0.06 loses 1-2.6 dB on every
// lattice case, 1.0 starts costing the fine-texture cases, 3.0 reverts to
// stock to the hundredth); the temporal seed is what turns the lattice cases
// from losses into gains, and the ring seed is what finds the better
// sub-texel basin the stock descent misses on edges. Neither alone does
// both; that is why there are three.
//
// WHAT WAS MEASURED, against the stock shader, same harness, same day.
// Ladder, 32 cases: +2.90 dB mean, 25 cases up by more than 0.1, none down
// by more than 0.1 (L4 -0.07 is the worst). Cases the seeds were built for
// (dB): A6 +3.3, A7 +3.1, L1 +13.8, L2 +20.6, L3 +2.1, L6 +9.9, M2 +6.2,
// O5 +1.6, O6 +2.4; the accelerating textures A4/A5 +1.9/+1.0. A7's velocity
// field on its mid-speed frames: 37.5% of texels gross against 45.6% stock,
// and the acceleration field's coverage there 67% against 36%. Real footage
// (decimate-and-reconstruct on five segments of a live-action clip, PSNR /
// SSIM of the synthesised frames): 34.74 / 0.9663 against the stock base's
// 34.29 / 0.9647, and 34.67 / 0.9651 for the four-frame shader against its
// stock's 34.22 / 0.9635 -- every segment up. The variational build
// (bidirectional-interpolation-variational.glsl) is still ahead on footage
// (36.27 / 0.9741) and remains the recommended interpolator for viewing.
// The speed comb -- fine aperiodic texture at non-integer coarse speeds --
// barely moves under any seeding, because no correct basin exists at the
// coarse level there; that failure is unchanged and documented.
//
// This variant's first customer is the FIELD -- the three- and four-frame
// shaders' acceleration and jerk readings at N:N, which inherit the coarse
// seeds -- and the fast interpolation tier second.
//
// The comment blocks on the tie-breaking margin and the starting step below
// are the stock shader's, verbatim; they apply unchanged inside descend_s().
//
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

//!TEXTURE FLOW_S_AB_CACHE2
//!SIZE 240 135
//!FORMAT rgba32f
//!STORAGE

//!TEXTURE FLOW_S_BA_CACHE
//!SIZE 240 135
//!FORMAT rgba32f
//!STORAGE

//!TEXTURE FLOW_S_BA_CACHE2
//!SIZE 240 135
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_S_AB_CACHE
//!BIND FLOW_S_AB_CACHE2
//!BIND FLOW_S_BA_CACHE
//!BIND FLOW_S_BA_CACHE2
//!BIND LUMA_A_S
//!BIND LUMA_B_S
//!SAVE FLOW_S_AB
//!WIDTH HOOKED.w 16 /
//!HEIGHT HOOKED.h 16 /
//!COMPONENTS 4
//!DESC [high] coarse flow search A->B and B->A (1/16 res) [fused: one dispatch]

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
vec2 descend_s2(vec2 uv, vec2 start, out float best_cost) {
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
void coarse_ba() {
    ivec2 coord = ivec2(LUMA_A_S_pos * LUMA_A_S_size);
    if (!pair_changed)
        return;

    vec2 uv_b = LUMA_A_S_pos;
    vec2 prev_s = imageLoad(FLOW_S_BA_CACHE, coord).xy * LUMA_A_S_pt;

    if (local_contrast_5x5_s2(uv_b) < MIN_CONTRAST) {
        vec4 result = vec4(0.0);
        imageStore(FLOW_S_BA_CACHE, coord, result);
        imageStore(FLOW_S_BA_CACHE2, coord, result);
        return;
    }

    // ---- three descents (scratch: twoseed4.py) ----
    float cost_a, cost_b, cost_c;
    vec2 off_a = descend_s2(uv_b, vec2(0.0), cost_a);
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
    vec2 off_b = descend_s2(uv_b, start_b, cost_b);
    vec2 off_c = descend_s2(uv_b, prev_s, cost_c);
    imageStore(FLOW_S_BA_CACHE2, coord, vec4(off_c / LUMA_A_S_pt, 0.0, 0.0));
    vec4 result = vec4(off_a / LUMA_A_S_pt, off_b / LUMA_A_S_pt);
    imageStore(FLOW_S_BA_CACHE, coord, result);
}
vec4 hook() {
    ivec2 coord = ivec2(LUMA_A_S_pos * LUMA_A_S_size);
    if (!pair_changed)
        return imageLoad(FLOW_S_AB_CACHE, coord);
    coarse_ba();

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
//!BIND FLOW_S_AB_CACHE2
//!BIND LUMA_A_S
//!BIND FLOW_E_BA_CACHE
//!BIND LUMA_B_S
//!SAVE FLOW_E_AB_RAW
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
// MOIRE EVIDENCE for the coarse level at this texel. The coarse (1/16) level is point-sampled, so
// texture above its Nyquist survives there as a Moire at full contrast; the same footprint averaged
// from this level's texels (a 2x2 box) keeps only what the coarse grid can represent. Point contrast
// far above box contrast means the coarse seeds here were matched on a Moire (NFRAME-LIMITS.md
// section 9: the diagonal speed ladder). Flat edges score near zero; textured diagonals high.
// INTER-FRAME EVIDENCE for the coarse level at this texel: how much the two frames differ over the
// footprint the coarse search matched on, as the largest absolute difference of the two 1/16 lumas
// across the 3x3. The Moire evidence beside it asks whether the coarse grid could represent this
// texture at all; this asks whether there was motion here to get wrong. Both lumas are read, so both
// are bound, and the generators shift both to each slot pair (NFRAME-LIMITS.md section 9, the Moire
// gate). Used only when FRAME_DIFF_GATE is on, below.
float frame_diff_s(vec2 uv) {
    float d = 0.0;
    for (int j = -1; j <= 1; j++) {
        for (int i = -1; i <= 1; i++) {
            vec2 c = uv + vec2(float(i), float(j)) * LUMA_A_S_pt;
            d = max(d, abs(LUMA_A_S_tex(c).r - LUMA_B_S_tex(c).r));
        }
    }
    return d;
}


float moire_s(vec2 uv) {
    float plo = 1.0, phi = 0.0, blo = 1.0, bhi = 0.0;
    for (int j = -1; j <= 1; j++) {
        for (int i = -1; i <= 1; i++) {
            vec2 c = uv + vec2(float(i), float(j)) * LUMA_A_S_pt;
            float p = LUMA_A_S_tex(c).r;
            float b = 0.25 * (LUMA_A_E_tex(c + vec2(-0.25, -0.25) * LUMA_A_S_pt).r + LUMA_A_E_tex(c + vec2(0.25, -0.25) * LUMA_A_S_pt).r
                            + LUMA_A_E_tex(c + vec2(-0.25, 0.25) * LUMA_A_S_pt).r + LUMA_A_E_tex(c + vec2(0.25, 0.25) * LUMA_A_S_pt).r);
            plo = min(plo, p); phi = max(phi, p); blo = min(blo, b); bhi = max(bhi, b);
        }
    }
    float cp = phi - plo, cb = bhi - blo;
    return cp > 0.02 ? clamp(1.0 - cb / cp, 0.0, 1.0) : 0.0;
}
// APERTURE TEST for a candidate offset: the 3x3 structure tensor of the reference block at this level.
// An edge-like block (smaller eigenvalue far below the larger) constrains motion only across the edge;
// a candidate whose offset lies mostly along the edge was matched on nothing. Returns true when the
// offset is trustworthy: the block is two-dimensional, or the offset is mostly across the edge.
const float EDGE_RATIO = 0.1;
bool aperture_ok(vec2 uv, vec2 off) {
    float jxx = 0.0, jyy = 0.0, jxy = 0.0;
    for (int j = -1; j <= 1; j++) {
        for (int i = -1; i <= 1; i++) {
            vec2 c = uv + vec2(float(i), float(j)) * LUMA_A_E_pt;
            float gx = LUMA_A_E_tex(c + vec2(LUMA_A_E_pt.x, 0.0)).r - LUMA_A_E_tex(c - vec2(LUMA_A_E_pt.x, 0.0)).r;
            float gy = LUMA_A_E_tex(c + vec2(0.0, LUMA_A_E_pt.y)).r - LUMA_A_E_tex(c - vec2(0.0, LUMA_A_E_pt.y)).r;
            jxx += gx * gx; jyy += gy * gy; jxy += gx * gy;
        }
    }
    float tr = jxx + jyy, det = jxx * jyy - jxy * jxy;
    float disc = sqrt(max(0.25 * tr * tr - det, 0.0));
    float lmax = 0.5 * tr + disc, lmin = 0.5 * tr - disc;
    if (lmax <= 1.0e-8) return false;                       // flat: nothing to match on
    if (lmin > EDGE_RATIO * lmax) return true;               // two-dimensional structure
    // the edge's along direction is the eigenvector of lmin; measure the offset's share along it
    vec2 e_across = normalize(abs(jxy) > 1.0e-8 ? vec2(lmax - jyy, jxy) : (jxx >= jyy ? vec2(1.0, 0.0) : vec2(0.0, 1.0)));
    float len = length(off);
    if (len <= 1.0e-8) return true;
    float across = abs(dot(off / len, e_across));
    return across > 0.5;                                     // mostly across the edge: constrained
}
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
    // ZERO SEED (NFRAME-LIMITS.md section 9). The coarse level is point-sampled: on texture above its
    // own Nyquist it matches a Moire that is right only at integer coarse-texel shifts (the diagonal
    // speed ladder: (16,16) px/frame exact, (8,8) 61% locked to a texture-period copy, (4,4) 98%). This
    // level resolves that texture and reaches +/-2 of its texels from any seed, so a fourth seed at
    // ZERO finds the true match wherever the coarse seeds are Moire and the motion is within reach.
    // Three guards, each measured: where the Moire evidence is high it competes like the other seeds
    // (prior included); elsewhere it replaces the best coarse seed only when its SAD is
    // ZERO_SEED_MARGIN lower, because with the prior in play a converged zero seed on an EDGE beat
    // correct large motions (L3 -4.2 dB, real footage -0.4); a zero seed that ends on its own search
    // boundary did not converge and is discounted; and one that slid along an edge-like block's edge
    // (aperture_ok) was matched on nothing. Through the four-frame shader: (8,8) diagonal 21 px / 61%
    // gross -> 0.03 px / 0%; the rotating textured disc's inner band 25% gross -> 14%; the 32-case
    // ladder +0.23 dB mean (R3 +2.4, O6 +1.3, A5 +1.0; worst F1 -0.9); real footage unchanged.
    // What it cannot do: a fractional shift of a perfectly periodic texture at this level, whose
    // exact integer copy inside the search window is a better match than any integer neighbour of
    // the truth (period locking, section 3).
    // ZERO_SEED is OFF in this two-frame shader -- it costs +4% and the picture tier keeps its
    // published numbers and time -- and ON in every generated tri/quad/quint, where the field is
    // the product.
    const int ZERO_SEED = 0;
    const float ZERO_SEED_MARGIN = 0.1;
    const float MOIRE_MIN = 0.25;
    // FRAME_DIFF_GATE (2026-09-04, off): also let the zero seed COMPETE where the two frames differ by
    // more than DIFF_MIN over the coarse footprint. Found by accident -- the generated shaders' cloned
    // pairs were comparing Moire evidence across two frames until de2b61a, which measured exactly this,
    // and fixing it cost up to 0.8 dB on fast textured motion. Put back on purpose, on the quad's
    // 32-case ladder: +0.18 dB mean, every oscillation case up (O1 +1.17, O4 +0.83), R3_rot_tex +1.07,
    // L1 +0.47, F1 +0.71; worst F2 and L3 -0.36. Real footage: -0.10 dB PSNR and -0.0004 SSIM on every
    // one of five segments. No time cost. That trade is the owner's to make; the switch ships off so
    // the shipped numbers stand, and a field-only reading of it belongs with ZERO_SEED in the
    // generators. Costs 18 taps per texel of this pass when on.
    const int FRAME_DIFF_GATE = 0;
    const float DIFF_MIN = 0.10;
    float sad_d = 1.0e30, moire = 0.0, fdiff = 0.0;
    vec2 ref_d = vec2(0.0);
    bool d_ok = false;
    if (ZERO_SEED != 0) {
        ref_d = refine_e(uv_a, vec2(0.0), sad_d);
        vec2 ref_d_t = abs(ref_d / LUMA_A_E_pt);
        d_ok = max(ref_d_t.x, ref_d_t.y) < float(REFINE_SEARCH_RADIUS) - 0.5;
        moire = moire_s(uv_a);
        if (FRAME_DIFF_GATE != 0) fdiff = frame_diff_s(uv_a);
        d_ok = d_ok && aperture_ok(uv_a, ref_d);
    }
    float score_a = sad_a + SEED_MAG_LAMBDA * length(ref_a / LUMA_A_E_pt) + tl * length((ref_a - prev_e) / LUMA_A_E_pt);
    float score_b = sad_b + SEED_MAG_LAMBDA * length(ref_b / LUMA_A_E_pt) + tl * length((ref_b - prev_e) / LUMA_A_E_pt);
    float score_c = trusted ? sad_c + SEED_MAG_LAMBDA * length(ref_c / LUMA_A_E_pt) + tl * length((ref_c - prev_e) / LUMA_A_E_pt) : 1.0e30;
    const float TIE_MARGIN = 1.0e-4;
    vec2 best_off = ref_a;
    float best_score = score_a;
    if (score_b < best_score * (1.0 - TIE_MARGIN)) { best_off = ref_b; best_score = score_b; }
    if (score_c < best_score * (1.0 - TIE_MARGIN)) { best_off = ref_c; best_score = score_c; }
    float best_sad = (best_off == ref_a) ? sad_a : (best_off == ref_b) ? sad_b : sad_c;
    if (d_ok) {
        if (moire > MOIRE_MIN || fdiff > DIFF_MIN) {
            float score_d = sad_d + SEED_MAG_LAMBDA * length(ref_d / LUMA_A_E_pt) + tl * length((ref_d - prev_e) / LUMA_A_E_pt);
            if (score_d < best_score * (1.0 - TIE_MARGIN)) best_off = ref_d;
        } else if (sad_d < best_sad * (1.0 - ZERO_SEED_MARGIN)) {
            best_off = ref_d;
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
//!BIND FLOW_S_BA_CACHE
//!BIND FLOW_S_BA_CACHE2
//!BIND LUMA_B_S
//!BIND FLOW_E_AB_CACHE
//!BIND LUMA_A_S
//!SAVE FLOW_E_BA_RAW
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
// MOIRE EVIDENCE for the coarse level at this texel. The coarse (1/16) level is point-sampled, so
// texture above its Nyquist survives there as a Moire at full contrast; the same footprint averaged
// from this level's texels (a 2x2 box) keeps only what the coarse grid can represent. Point contrast
// far above box contrast means the coarse seeds here were matched on a Moire (NFRAME-LIMITS.md
// section 9: the diagonal speed ladder). Flat edges score near zero; textured diagonals high.
// INTER-FRAME EVIDENCE for the coarse level at this texel: how much the two frames differ over the
// footprint the coarse search matched on, as the largest absolute difference of the two 1/16 lumas
// across the 3x3. The Moire evidence beside it asks whether the coarse grid could represent this
// texture at all; this asks whether there was motion here to get wrong. Both lumas are read, so both
// are bound, and the generators shift both to each slot pair (NFRAME-LIMITS.md section 9, the Moire
// gate). Used only when FRAME_DIFF_GATE is on, below.
float frame_diff_s(vec2 uv) {
    float d = 0.0;
    for (int j = -1; j <= 1; j++) {
        for (int i = -1; i <= 1; i++) {
            vec2 c = uv + vec2(float(i), float(j)) * LUMA_A_S_pt;
            d = max(d, abs(LUMA_A_S_tex(c).r - LUMA_B_S_tex(c).r));
        }
    }
    return d;
}


float moire_s(vec2 uv) {
    float plo = 1.0, phi = 0.0, blo = 1.0, bhi = 0.0;
    for (int j = -1; j <= 1; j++) {
        for (int i = -1; i <= 1; i++) {
            vec2 c = uv + vec2(float(i), float(j)) * LUMA_B_S_pt;
            float p = LUMA_B_S_tex(c).r;
            float b = 0.25 * (LUMA_B_E_tex(c + vec2(-0.25, -0.25) * LUMA_B_S_pt).r + LUMA_B_E_tex(c + vec2(0.25, -0.25) * LUMA_B_S_pt).r
                            + LUMA_B_E_tex(c + vec2(-0.25, 0.25) * LUMA_B_S_pt).r + LUMA_B_E_tex(c + vec2(0.25, 0.25) * LUMA_B_S_pt).r);
            plo = min(plo, p); phi = max(phi, p); blo = min(blo, b); bhi = max(bhi, b);
        }
    }
    float cp = phi - plo, cb = bhi - blo;
    return cp > 0.02 ? clamp(1.0 - cb / cp, 0.0, 1.0) : 0.0;
}
// APERTURE TEST for a candidate offset: the 3x3 structure tensor of the reference block at this level.
// An edge-like block (smaller eigenvalue far below the larger) constrains motion only across the edge;
// a candidate whose offset lies mostly along the edge was matched on nothing. Returns true when the
// offset is trustworthy: the block is two-dimensional, or the offset is mostly across the edge.
const float EDGE_RATIO = 0.1;
bool aperture_ok(vec2 uv, vec2 off) {
    float jxx = 0.0, jyy = 0.0, jxy = 0.0;
    for (int j = -1; j <= 1; j++) {
        for (int i = -1; i <= 1; i++) {
            vec2 c = uv + vec2(float(i), float(j)) * LUMA_A_E_pt;
            float gx = LUMA_B_E_tex(c + vec2(LUMA_A_E_pt.x, 0.0)).r - LUMA_B_E_tex(c - vec2(LUMA_A_E_pt.x, 0.0)).r;
            float gy = LUMA_B_E_tex(c + vec2(0.0, LUMA_A_E_pt.y)).r - LUMA_B_E_tex(c - vec2(0.0, LUMA_A_E_pt.y)).r;
            jxx += gx * gx; jyy += gy * gy; jxy += gx * gy;
        }
    }
    float tr = jxx + jyy, det = jxx * jyy - jxy * jxy;
    float disc = sqrt(max(0.25 * tr * tr - det, 0.0));
    float lmax = 0.5 * tr + disc, lmin = 0.5 * tr - disc;
    if (lmax <= 1.0e-8) return false;                       // flat: nothing to match on
    if (lmin > EDGE_RATIO * lmax) return true;               // two-dimensional structure
    // the edge's along direction is the eigenvector of lmin; measure the offset's share along it
    vec2 e_across = normalize(abs(jxy) > 1.0e-8 ? vec2(lmax - jyy, jxy) : (jxx >= jyy ? vec2(1.0, 0.0) : vec2(0.0, 1.0)));
    float len = length(off);
    if (len <= 1.0e-8) return true;
    float across = abs(dot(off / len, e_across));
    return across > 0.5;                                     // mostly across the edge: constrained
}
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
    vec4 seeds = imageLoad(FLOW_S_BA_CACHE, ivec2(snap_texel(uv_b, LUMA_B_S_size) * LUMA_B_S_size));
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
    ivec2 scoord = ivec2(snap_texel(uv_b, LUMA_B_S_size) * LUMA_B_S_size);
    vec2 base_off3 = imageLoad(FLOW_S_BA_CACHE2, scoord).xy * 2.0 * LUMA_A_E_pt;
    float sad_a, sad_b, sad_c;
    vec2 ref_a = refine_e(uv_b, base_off, sad_a);
    vec2 ref_b = refine_e(uv_b, base_off2, sad_b);
    vec2 ref_c = refine_e(uv_b, base_off3, sad_c);
    // ZERO SEED (NFRAME-LIMITS.md section 9). The coarse level is point-sampled: on texture above its
    // own Nyquist it matches a Moire that is right only at integer coarse-texel shifts (the diagonal
    // speed ladder: (16,16) px/frame exact, (8,8) 61% locked to a texture-period copy, (4,4) 98%). This
    // level resolves that texture and reaches +/-2 of its texels from any seed, so a fourth seed at
    // ZERO finds the true match wherever the coarse seeds are Moire and the motion is within reach.
    // Three guards, each measured: where the Moire evidence is high it competes like the other seeds
    // (prior included); elsewhere it replaces the best coarse seed only when its SAD is
    // ZERO_SEED_MARGIN lower, because with the prior in play a converged zero seed on an EDGE beat
    // correct large motions (L3 -4.2 dB, real footage -0.4); a zero seed that ends on its own search
    // boundary did not converge and is discounted; and one that slid along an edge-like block's edge
    // (aperture_ok) was matched on nothing. Through the four-frame shader: (8,8) diagonal 21 px / 61%
    // gross -> 0.03 px / 0%; the rotating textured disc's inner band 25% gross -> 14%; the 32-case
    // ladder +0.23 dB mean (R3 +2.4, O6 +1.3, A5 +1.0; worst F1 -0.9); real footage unchanged.
    // What it cannot do: a fractional shift of a perfectly periodic texture at this level, whose
    // exact integer copy inside the search window is a better match than any integer neighbour of
    // the truth (period locking, section 3).
    // ZERO_SEED is OFF in this two-frame shader -- it costs +4% and the picture tier keeps its
    // published numbers and time -- and ON in every generated tri/quad/quint, where the field is
    // the product.
    const int ZERO_SEED = 0;
    const float ZERO_SEED_MARGIN = 0.1;
    const float MOIRE_MIN = 0.25;
    // FRAME_DIFF_GATE (2026-09-04, off): also let the zero seed COMPETE where the two frames differ by
    // more than DIFF_MIN over the coarse footprint. Found by accident -- the generated shaders' cloned
    // pairs were comparing Moire evidence across two frames until de2b61a, which measured exactly this,
    // and fixing it cost up to 0.8 dB on fast textured motion. Put back on purpose, on the quad's
    // 32-case ladder: +0.18 dB mean, every oscillation case up (O1 +1.17, O4 +0.83), R3_rot_tex +1.07,
    // L1 +0.47, F1 +0.71; worst F2 and L3 -0.36. Real footage: -0.10 dB PSNR and -0.0004 SSIM on every
    // one of five segments. No time cost. That trade is the owner's to make; the switch ships off so
    // the shipped numbers stand, and a field-only reading of it belongs with ZERO_SEED in the
    // generators. Costs 18 taps per texel of this pass when on.
    const int FRAME_DIFF_GATE = 0;
    const float DIFF_MIN = 0.10;
    float sad_d = 1.0e30, moire = 0.0, fdiff = 0.0;
    vec2 ref_d = vec2(0.0);
    bool d_ok = false;
    if (ZERO_SEED != 0) {
        ref_d = refine_e(uv_b, vec2(0.0), sad_d);
        vec2 ref_d_t = abs(ref_d / LUMA_A_E_pt);
        d_ok = max(ref_d_t.x, ref_d_t.y) < float(REFINE_SEARCH_RADIUS) - 0.5;
        moire = moire_s(uv_b);
        if (FRAME_DIFF_GATE != 0) fdiff = frame_diff_s(uv_b);
        d_ok = d_ok && aperture_ok(uv_b, ref_d);
    }
    float score_a = sad_a + SEED_MAG_LAMBDA * length(ref_a / LUMA_A_E_pt) + tl * length((ref_a - prev_e) / LUMA_A_E_pt);
    float score_b = sad_b + SEED_MAG_LAMBDA * length(ref_b / LUMA_A_E_pt) + tl * length((ref_b - prev_e) / LUMA_A_E_pt);
    float score_c = trusted ? sad_c + SEED_MAG_LAMBDA * length(ref_c / LUMA_A_E_pt) + tl * length((ref_c - prev_e) / LUMA_A_E_pt) : 1.0e30;
    const float TIE_MARGIN = 1.0e-4;
    vec2 best_off = ref_a;
    float best_score = score_a;
    if (score_b < best_score * (1.0 - TIE_MARGIN)) { best_off = ref_b; best_score = score_b; }
    if (score_c < best_score * (1.0 - TIE_MARGIN)) { best_off = ref_c; best_score = score_c; }
    float best_sad = (best_off == ref_a) ? sad_a : (best_off == ref_b) ? sad_b : sad_c;
    if (d_ok) {
        if (moire > MOIRE_MIN || fdiff > DIFF_MIN) {
            float score_d = sad_d + SEED_MAG_LAMBDA * length(ref_d / LUMA_A_E_pt) + tl * length((ref_d - prev_e) / LUMA_A_E_pt);
            if (score_d < best_score * (1.0 - TIE_MARGIN)) best_off = ref_d;
        } else if (sad_d < best_sad * (1.0 - ZERO_SEED_MARGIN)) {
            best_off = ref_d;
        }
    }
    vec4 result = vec4(best_off / LUMA_A_E_pt, 0.0, 0.0);
    imageStore(FLOW_E_BA_CACHE, coord, result);
    return result;
}

//!TEXTURE FLOW_E_BA_PROP_ST1
//!SIZE 480 270
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_E_AB_RAW
//!BIND LUMA_A_E
//!BIND LUMA_B_E
//!BIND FLOW_E_BA_RAW
//!BIND FLOW_E_BA_PROP_ST1
//!SAVE FLOW_E_AB_PROP
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 2
//!DESC [prop13] contrast-weighted flow propagation AB (pass 1 of 3) [fused with its B->A twin: one dispatch]

const float PROP_SELF_WEIGHT = 8.0;
const float PROP_CONF_FULL   = 0.08;

float prop_conf(vec2 uv) {
    float lo = 1.0, hi = 0.0;
    for (int y = -2; y <= 2; y++)
        for (int x = -2; x <= 2; x++) {
            float l = LUMA_A_E_tex(uv + vec2(float(x), float(y)) * LUMA_A_E_pt).r;
            lo = min(lo, l); hi = max(hi, l);
        }
    return clamp((hi - lo) / PROP_CONF_FULL, 0.0, 1.0);
}

void hook_ba() {
    vec2 uv = FLOW_E_BA_RAW_pos;
    vec2 own = FLOW_E_BA_RAW_tex(uv).xy;
    float c_own = prop_conf(uv);
    vec2 acc = vec2(0.0);
    float wsum = 0.0;
    for (int y = -2; y <= 2; y++)
        for (int x = -2; x <= 2; x++) {
            if (x == 0 && y == 0) continue;
            vec2 o = vec2(float(x), float(y)) * FLOW_E_BA_RAW_pt;
            float w = prop_conf(uv + o) / (1.0 + 0.5 * float(abs(x) + abs(y)));
            acc += w * FLOW_E_BA_RAW_tex(uv + o).xy;
            wsum += w;
        }
    float w_own = PROP_SELF_WEIGHT * c_own * c_own;
    if (wsum + w_own <= 0.0)
        { imageStore(FLOW_E_BA_PROP_ST1, ivec2(gl_FragCoord.xy), vec4(own, 0.0, 0.0)); return; }
    { imageStore(FLOW_E_BA_PROP_ST1, ivec2(gl_FragCoord.xy), vec4((w_own * own + acc) / (w_own + wsum), 0.0, 0.0)); return; }
}
vec4 hook() {
    hook_ba();
    vec2 uv = FLOW_E_AB_RAW_pos;
    vec2 own = FLOW_E_AB_RAW_tex(uv).xy;
    float c_own = prop_conf(uv);
    vec2 acc = vec2(0.0);
    float wsum = 0.0;
    for (int y = -2; y <= 2; y++)
        for (int x = -2; x <= 2; x++) {
            if (x == 0 && y == 0) continue;
            vec2 o = vec2(float(x), float(y)) * FLOW_E_AB_RAW_pt;
            float w = prop_conf(uv + o) / (1.0 + 0.5 * float(abs(x) + abs(y)));
            acc += w * FLOW_E_AB_RAW_tex(uv + o).xy;
            wsum += w;
        }
    float w_own = PROP_SELF_WEIGHT * c_own * c_own;
    if (wsum + w_own <= 0.0)
        return vec4(own, 0.0, 0.0);
    return vec4((w_own * own + acc) / (w_own + wsum), 0.0, 0.0);
}

//!TEXTURE FLOW_E_BA_PROP_ST2
//!SIZE 480 270
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_E_AB_PROP
//!BIND LUMA_A_E
//!BIND LUMA_B_E
//!BIND FLOW_E_BA_PROP_ST1
//!BIND FLOW_E_BA_PROP_ST2
//!SAVE FLOW_E_AB_PROP
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 2
//!DESC [prop13] contrast-weighted flow propagation AB (pass 2 of 3) [fused with its B->A twin: one dispatch]

const float PROP_SELF_WEIGHT = 8.0;
const float PROP_CONF_FULL   = 0.08;

float prop_conf(vec2 uv) {
    float lo = 1.0, hi = 0.0;
    for (int y = -2; y <= 2; y++)
        for (int x = -2; x <= 2; x++) {
            float l = LUMA_A_E_tex(uv + vec2(float(x), float(y)) * LUMA_A_E_pt).r;
            lo = min(lo, l); hi = max(hi, l);
        }
    return clamp((hi - lo) / PROP_CONF_FULL, 0.0, 1.0);
}

void hook_ba() {
    vec2 uv = FLOW_E_AB_PROP_pos;
    vec2 own = imageLoad(FLOW_E_BA_PROP_ST1, ivec2(floor((FLOW_E_AB_PROP_size) * (uv)))).xy;
    float c_own = prop_conf(uv);
    vec2 acc = vec2(0.0);
    float wsum = 0.0;
    for (int y = -2; y <= 2; y++)
        for (int x = -2; x <= 2; x++) {
            if (x == 0 && y == 0) continue;
            vec2 o = vec2(float(x), float(y)) * FLOW_E_AB_PROP_pt;
            float w = prop_conf(uv + o) / (1.0 + 0.5 * float(abs(x) + abs(y)));
            acc += w * imageLoad(FLOW_E_BA_PROP_ST1, ivec2(floor((FLOW_E_AB_PROP_size) * (uv + o)))).xy;
            wsum += w;
        }
    float w_own = PROP_SELF_WEIGHT * c_own * c_own;
    if (wsum + w_own <= 0.0)
        { imageStore(FLOW_E_BA_PROP_ST2, ivec2(gl_FragCoord.xy), vec4(own, 0.0, 0.0)); return; }
    { imageStore(FLOW_E_BA_PROP_ST2, ivec2(gl_FragCoord.xy), vec4((w_own * own + acc) / (w_own + wsum), 0.0, 0.0)); return; }
}
vec4 hook() {
    hook_ba();
    vec2 uv = FLOW_E_AB_PROP_pos;
    vec2 own = FLOW_E_AB_PROP_tex(uv).xy;
    float c_own = prop_conf(uv);
    vec2 acc = vec2(0.0);
    float wsum = 0.0;
    for (int y = -2; y <= 2; y++)
        for (int x = -2; x <= 2; x++) {
            if (x == 0 && y == 0) continue;
            vec2 o = vec2(float(x), float(y)) * FLOW_E_AB_PROP_pt;
            float w = prop_conf(uv + o) / (1.0 + 0.5 * float(abs(x) + abs(y)));
            acc += w * FLOW_E_AB_PROP_tex(uv + o).xy;
            wsum += w;
        }
    float w_own = PROP_SELF_WEIGHT * c_own * c_own;
    if (wsum + w_own <= 0.0)
        return vec4(own, 0.0, 0.0);
    return vec4((w_own * own + acc) / (w_own + wsum), 0.0, 0.0);
}

//!TEXTURE FLOW_E_BA_PROP_ST3
//!SIZE 480 270
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_E_AB_PROP
//!BIND LUMA_A_E
//!BIND LUMA_B_E
//!BIND FLOW_E_BA_PROP_ST2
//!BIND FLOW_E_BA_PROP_ST3
//!SAVE FLOW_E_AB_PROP
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 2
//!DESC [prop13] contrast-weighted flow propagation AB (pass 3 of 3) [fused with its B->A twin: one dispatch]

const float PROP_SELF_WEIGHT = 8.0;
const float PROP_CONF_FULL   = 0.08;

float prop_conf(vec2 uv) {
    float lo = 1.0, hi = 0.0;
    for (int y = -2; y <= 2; y++)
        for (int x = -2; x <= 2; x++) {
            float l = LUMA_A_E_tex(uv + vec2(float(x), float(y)) * LUMA_A_E_pt).r;
            lo = min(lo, l); hi = max(hi, l);
        }
    return clamp((hi - lo) / PROP_CONF_FULL, 0.0, 1.0);
}

void hook_ba() {
    vec2 uv = FLOW_E_AB_PROP_pos;
    vec2 own = imageLoad(FLOW_E_BA_PROP_ST2, ivec2(floor((FLOW_E_AB_PROP_size) * (uv)))).xy;
    float c_own = prop_conf(uv);
    vec2 acc = vec2(0.0);
    float wsum = 0.0;
    for (int y = -2; y <= 2; y++)
        for (int x = -2; x <= 2; x++) {
            if (x == 0 && y == 0) continue;
            vec2 o = vec2(float(x), float(y)) * FLOW_E_AB_PROP_pt;
            float w = prop_conf(uv + o) / (1.0 + 0.5 * float(abs(x) + abs(y)));
            acc += w * imageLoad(FLOW_E_BA_PROP_ST2, ivec2(floor((FLOW_E_AB_PROP_size) * (uv + o)))).xy;
            wsum += w;
        }
    float w_own = PROP_SELF_WEIGHT * c_own * c_own;
    if (wsum + w_own <= 0.0)
        { imageStore(FLOW_E_BA_PROP_ST3, ivec2(gl_FragCoord.xy), vec4(own, 0.0, 0.0)); return; }
    { imageStore(FLOW_E_BA_PROP_ST3, ivec2(gl_FragCoord.xy), vec4((w_own * own + acc) / (w_own + wsum), 0.0, 0.0)); return; }
}
vec4 hook() {
    hook_ba();
    vec2 uv = FLOW_E_AB_PROP_pos;
    vec2 own = FLOW_E_AB_PROP_tex(uv).xy;
    float c_own = prop_conf(uv);
    vec2 acc = vec2(0.0);
    float wsum = 0.0;
    for (int y = -2; y <= 2; y++)
        for (int x = -2; x <= 2; x++) {
            if (x == 0 && y == 0) continue;
            vec2 o = vec2(float(x), float(y)) * FLOW_E_AB_PROP_pt;
            float w = prop_conf(uv + o) / (1.0 + 0.5 * float(abs(x) + abs(y)));
            acc += w * FLOW_E_AB_PROP_tex(uv + o).xy;
            wsum += w;
        }
    float w_own = PROP_SELF_WEIGHT * c_own * c_own;
    if (wsum + w_own <= 0.0)
        return vec4(own, 0.0, 0.0);
    return vec4((w_own * own + acc) / (w_own + wsum), 0.0, 0.0);
}

//!TEXTURE FLOW_E_BA_ST
//!SIZE 480 270
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_E_AB_RAW
//!BIND FLOW_E_AB_PROP
//!BIND LUMA_A_E
//!BIND LUMA_B_E
//!BIND FLOW_E_BA_RAW
//!BIND FLOW_E_BA_PROP_ST3
//!BIND FLOW_E_BA_ST
//!SAVE FLOW_E_AB
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 2
//!DESC [prop13] three-way data check AB: propagated vs raw vs zero, ties to consensus on texture only [fused with its B->A twin: one dispatch]

const float PROP_CHECK_MARGIN = 0.1;
const float PROP_FLAT_CONF    = 0.25;
const float PROP_DISAGREE     = 0.75;
const float PROP_DISAGREE_REL = 0.5;   // 1/8-level texels (6 px)
const float PROP_CONF_FULL    = 0.08;

float prop_conf(vec2 uv) {
    float lo = 1.0, hi = 0.0;
    for (int y = -2; y <= 2; y++)
        for (int x = -2; x <= 2; x++) {
            float l = LUMA_A_E_tex(uv + vec2(float(x), float(y)) * LUMA_A_E_pt).r;
            lo = min(lo, l); hi = max(hi, l);
        }
    return clamp((hi - lo) / PROP_CONF_FULL, 0.0, 1.0);
}

float sad5(vec2 uv, vec2 flow_uv) {
    float s = 0.0;
    for (int y = -2; y <= 2; y++)
        for (int x = -2; x <= 2; x++) {
            vec2 o = vec2(float(x), float(y)) * LUMA_A_E_pt;
            s += abs(LUMA_A_E_tex(uv + o).r - LUMA_B_E_tex(uv + o + flow_uv).r);
        }
    return s;
}

float prop_conf_ba(vec2 uv) {
    float lo = 1.0, hi = 0.0;
    for (int y = -2; y <= 2; y++)
        for (int x = -2; x <= 2; x++) {
            float l = LUMA_B_E_tex(uv + vec2(float(x), float(y)) * LUMA_B_E_pt).r;
            lo = min(lo, l); hi = max(hi, l);
        }
    return clamp((hi - lo) / PROP_CONF_FULL, 0.0, 1.0);
}

float sad5_ba(vec2 uv, vec2 flow_uv) {
    float s = 0.0;
    for (int y = -2; y <= 2; y++)
        for (int x = -2; x <= 2; x++) {
            vec2 o = vec2(float(x), float(y)) * LUMA_B_E_pt;
            s += abs(LUMA_B_E_tex(uv + o).r - LUMA_A_E_tex(uv + o + flow_uv).r);
        }
    return s;
}

void hook_ba() {
    vec2 uv = FLOW_E_AB_PROP_pos;
    vec2 raw = FLOW_E_BA_RAW_tex(uv).xy;
    vec2 prop = imageLoad(FLOW_E_BA_PROP_ST3, ivec2(floor((FLOW_E_AB_PROP_size) * (uv)))).xy;
    if (prop == raw)
        { imageStore(FLOW_E_BA_ST, ivec2(gl_FragCoord.xy), vec4(raw, 0.0, 0.0)); return; }
    float s_prop = sad5_ba(uv, prop * LUMA_B_E_pt);
    float s_raw  = sad5_ba(uv, raw * LUMA_B_E_pt);
    float s_zero = sad5_ba(uv, vec2(0.0));
    float best = min(s_raw, s_zero);
    bool textured = prop_conf_ba(uv) >= PROP_FLAT_CONF;
    if (textured) {
        // prop9: a proven consensus wins outright; where the neighbourhood
        // DISAGREES with the raw flow and neither is proven, the raw flow is
        // an alias suspect and a blend (zero) beats trusting it; otherwise
        // the three-way rule as before.
        if (s_prop < best * (1.0 - PROP_CHECK_MARGIN) - 1e-4)
            { imageStore(FLOW_E_BA_ST, ivec2(gl_FragCoord.xy), vec4(prop, 0.0, 0.0)); return; }
        // prop12: the disagreement threshold scales with the flow, so a fast
        // translation whose consensus is diluted by background votes near its
        // edges is not mistaken for an alias (aliases sit texels apart at
        // speeds of a texel or two).
        if (length(prop - raw) > max(PROP_DISAGREE, PROP_DISAGREE_REL * length(raw)))
            { imageStore(FLOW_E_BA_ST, ivec2(gl_FragCoord.xy), vec4(0.0)); return; }
        if (s_prop <= best * (1.0 + PROP_CHECK_MARGIN) + 1e-4)
            { imageStore(FLOW_E_BA_ST, ivec2(gl_FragCoord.xy), vec4(prop, 0.0, 0.0)); return; }
        { imageStore(FLOW_E_BA_ST, ivec2(gl_FragCoord.xy), s_raw <= s_zero ? vec4(raw, 0.0, 0.0) : vec4(0.0)); return; }
    }
    // flat: evidence required
    if (s_prop < best * (1.0 - PROP_CHECK_MARGIN) - 1e-4)
        { imageStore(FLOW_E_BA_ST, ivec2(gl_FragCoord.xy), vec4(prop, 0.0, 0.0)); return; }
    { imageStore(FLOW_E_BA_ST, ivec2(gl_FragCoord.xy), vec4(0.0)); return; }
}
vec4 hook() {
    hook_ba();
    vec2 uv = FLOW_E_AB_PROP_pos;
    vec2 raw = FLOW_E_AB_RAW_tex(uv).xy;
    vec2 prop = FLOW_E_AB_PROP_tex(uv).xy;
    if (prop == raw)
        return vec4(raw, 0.0, 0.0);
    float s_prop = sad5(uv, prop * LUMA_A_E_pt);
    float s_raw  = sad5(uv, raw * LUMA_A_E_pt);
    float s_zero = sad5(uv, vec2(0.0));
    float best = min(s_raw, s_zero);
    bool textured = prop_conf(uv) >= PROP_FLAT_CONF;
    if (textured) {
        // prop9: a proven consensus wins outright; where the neighbourhood
        // DISAGREES with the raw flow and neither is proven, the raw flow is
        // an alias suspect and a blend (zero) beats trusting it; otherwise
        // the three-way rule as before.
        if (s_prop < best * (1.0 - PROP_CHECK_MARGIN) - 1e-4)
            return vec4(prop, 0.0, 0.0);
        // prop12: the disagreement threshold scales with the flow, so a fast
        // translation whose consensus is diluted by background votes near its
        // edges is not mistaken for an alias (aliases sit texels apart at
        // speeds of a texel or two).
        if (length(prop - raw) > max(PROP_DISAGREE, PROP_DISAGREE_REL * length(raw)))
            return vec4(0.0);
        if (s_prop <= best * (1.0 + PROP_CHECK_MARGIN) + 1e-4)
            return vec4(prop, 0.0, 0.0);
        return s_raw <= s_zero ? vec4(raw, 0.0, 0.0) : vec4(0.0);
    }
    // flat: evidence required
    if (s_prop < best * (1.0 - PROP_CHECK_MARGIN) - 1e-4)
        return vec4(prop, 0.0, 0.0);
    return vec4(0.0);
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
//!BIND FLOW_E_BA_ST
//!BIND FLOW_E_AB
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
    vec2 base_off = imageLoad(FLOW_E_BA_ST, ivec2(floor((FLOW_E_AB_size) * (snap_texel(uv_b, FLOW_E_AB_size))))).xy * 2.0 * LUMA_A_Q_pt;

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
    const int SUBPEL_REFINE = 0;

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
    const int SUBPEL_SELFREF = 0;
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
    const int SUBPEL_REFINE = 0;

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
    const int SUBPEL_SELFREF = 0;
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
//!TEXTURE FLOW_H_BA_M1_ST
//!SIZE 1920 1080
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_H_AB
//!BIND FLOW_H_BA
//!BIND FLOW_H_BA_M1_ST
//!SAVE FLOW_H_AB
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 2
//!DESC [high] vector median filter on flow A->B (pass 1) [fused with its B->A twin: one dispatch]
void hook_ba() {
    if (!pair_changed)
        { imageStore(FLOW_H_BA_M1_ST, ivec2(gl_FragCoord.xy), vec4(0.0)); return; }

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

    { imageStore(FLOW_H_BA_M1_ST, ivec2(gl_FragCoord.xy), vec4(best, 0.0, 0.0)); return; }
}

// Second pass: a single 3x3 vector median can be out-voted by a small cluster of neighboring cells that all agree with each other on the same wrong (but locally self-consistent) vector; running it twice extends its effective reach.
// This one's result is what the final warp actually reads, so it gets a
// real persistent cache (unlike pass 1 above).
vec4 hook() {
    hook_ba();
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

//!TEXTURE FLOW_H_BA_MEDIAN_CACHE
//!SIZE 1920 1080
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_H_BA_MEDIAN_CACHE
//!BIND FLOW_H_BA_M1_ST
//!BIND FLOW_H_AB
//!SAVE FLOW_H_BA
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 2
//!DESC [high] vector median filter on flow B->A (pass 2)
vec4 hook() {
    ivec2 coord = ivec2(FLOW_H_AB_pos * FLOW_H_AB_size);
    if (!pair_changed)
        return imageLoad(FLOW_H_BA_MEDIAN_CACHE, coord);

    vec2 v[9];
    int n = 0;
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            vec2 o = vec2(float(x), float(y)) * FLOW_H_AB_pt;
            v[n++] = imageLoad(FLOW_H_BA_M1_ST, ivec2(floor((FLOW_H_AB_size) * (FLOW_H_AB_pos + o)))).xy;
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
//!TEXTURE PLATE
//!SIZE 1920 1080
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND NEXT
//!BIND SCENE_DIFF
//!BIND PLATE
//!SAVE PLATE_TEX
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!DESC [plate] background plate: what this texel showed when it was last still, and how many windows confirm it
const float PLATE_STATIC_TAU = 0.03;      // a texel whose A/B colour differs less than this is still
const float PLATE_AGREE_TAU = 0.06;     // agreement with the plate's stored colour
const float PLATE_CONF_MAX = 16.0;
const float PLATE_CUT_DIFF = 0.125;     // the warp's SCENE_CUT_DIFF
vec4 hook() {
    ivec2 c = ivec2(gl_FragCoord.xy);
    vec4 p = imageLoad(PLATE, c);
    if (SCENE_DIFF_tex(vec2(0.5)).r > PLATE_CUT_DIFF)
        p = vec4(0.0);
    if (pair_changed) {
        vec3 a = HOOKED_tex(HOOKED_pos).rgb;
        vec3 b = NEXT_tex(NEXT_pos).rgb;
        bool still = length(a - b) < PLATE_STATIC_TAU;
        if (still) {
            if (p.a > 0.0 && length(a - p.rgb) < PLATE_AGREE_TAU)
                p = vec4(mix(p.rgb, a, 0.25), min(p.a + 1.0, PLATE_CONF_MAX));
            else
                p = vec4(a, 1.0);
        }
        imageStore(PLATE, c, p);
    }
    return p;
}

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND NEXT
//!BIND LUMA_A_H
//!BIND LUMA_B_H
//!BIND FLOW_H_AB
//!BIND PLATE_TEX
//!SAVE FLOW_C
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!DESC [coherent] one motion per moving thing: the trimmed mean of the dense flow over the character texels around this one
const int COH_R = 32;                 // half-res texels: the vote's radius (a character-sized window)
const float COH_MOVING_TAU = 0.08;      // A/B luma difference that marks the moving region
const float COH_CHAR_TAU = 0.03;        // a texel further than this from a confident plate is character
const float COH_MINFLOW = 0.5;         // half-res texels; a texel whose dense flow is smaller found nothing and does not vote
bool is_char(vec2 p, vec3 c) {
    vec4 pl = PLATE_TEX_tex(p);
    return pl.a < 2.0 || length(c - pl.rgb) > COH_CHAR_TAU;
}
vec4 hook() {
    vec2 uv = FLOW_H_AB_pos;
    vec2 f0 = FLOW_H_AB_tex(uv).xy;
    bool moving = abs(LUMA_A_H_tex(uv).r - LUMA_B_H_tex(uv).r) > COH_MOVING_TAU;
    bool char_a = is_char(uv, HOOKED_tex(uv).rgb);
    bool char_b = is_char(uv, NEXT_tex(uv).rgb);
    if (!moving || !(char_a || char_b))
        return vec4(f0, 0.0, 0.0);
    vec2 sum = vec2(0.0); float n = 0.0;
    for (int j = -COH_R; j <= COH_R; j += 4) {
        for (int i = -COH_R; i <= COH_R; i += 4) {
            vec2 p = uv + vec2(float(i), float(j)) * FLOW_H_AB_pt;
            if (abs(LUMA_A_H_tex(p).r - LUMA_B_H_tex(p).r) <= COH_MOVING_TAU) continue;
            if (!is_char(p, HOOKED_tex(p).rgb)) continue;              // only a texel that is character IN A carries the A->B motion
            vec2 f = FLOW_H_AB_tex(p).xy;
            if (length(f) < COH_MINFLOW) continue;
            sum += f; n += 1.0;
        }
    }
    if (n < 6.0) return vec4(f0, 0.0, 0.0);
    vec2 m = sum / n;
    sum = vec2(0.0); n = 0.0;
    for (int j = -COH_R; j <= COH_R; j += 4) {
        for (int i = -COH_R; i <= COH_R; i += 4) {
            vec2 p = uv + vec2(float(i), float(j)) * FLOW_H_AB_pt;
            if (abs(LUMA_A_H_tex(p).r - LUMA_B_H_tex(p).r) <= COH_MOVING_TAU) continue;
            if (!is_char(p, HOOKED_tex(p).rgb)) continue;
            vec2 f = FLOW_H_AB_tex(p).xy;
            if (length(f) < COH_MINFLOW || length(f - m) > 2.0) continue;
            sum += f; n += 1.0;
        }
    }
    if (n < 6.0) return vec4(f0, 0.0, 0.0);
    return vec4(sum / n, 1.0, 0.0);
}

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND PLATE_TEX
//!BIND SCENE_DIFF
//!BIND NEXT
//!BIND FLOW_H_AB
//!BIND FLOW_C
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
    vec2 flow_ab = FLOW_C_tex(HOOKED_pos).xy * 2.0 * HOOKED_pt;     // [coherent] one motion per moving thing

    vec4 warped_a = warp_sample_a(HOOKED_pos - flow_ab * mix_t);
    vec4 warped_b = warp_sample_b(NEXT_pos + flow_ab * (1.0 - mix_t));

    // THE PLATE ARBITRATES (scratch experiment, see build_plate.py). Where the two candidates disagree,
    // the shipped shader blends them into a ghost; if the plate is confident here, the candidate closer to
    // the plate wins outright when it is within reach of it. The plate chooses, it never invents.
    const float PLATE_DISAGREE_TAU = 0.12;
    const float PLATE_MIN_CONF = 2.0;
    vec4 plate = PLATE_TEX_tex(HOOKED_pos);
    // A candidate whose SOURCE texel is background (it agrees with the plate there) is background, and the
    // true background at THIS texel is the plate here -- not the other cell of a patterned backdrop that a
    // character's flow dragged in. Measured without this: a halo of smeared background around every
    // moving character on a detailed backdrop.
    if (plate.a >= PLATE_MIN_CONF) {
        vec4 pa = PLATE_TEX_tex(HOOKED_pos - flow_ab * mix_t);
        if (pa.a >= PLATE_MIN_CONF && length(warped_a.rgb - pa.rgb) < 0.06) warped_a = vec4(plate.rgb, warped_a.a);
        vec4 pb = PLATE_TEX_tex(NEXT_pos + flow_ab * (1.0 - mix_t));
        if (pb.a >= PLATE_MIN_CONF && length(warped_b.rgb - pb.rgb) < 0.06) warped_b = vec4(plate.rgb, warped_b.a);
    }
    if (plate.a >= PLATE_MIN_CONF && length(warped_a.rgb - warped_b.rgb) > PLATE_DISAGREE_TAU) {
        float da = length(warped_a.rgb - plate.rgb), db = length(warped_b.rgb - plate.rgb);
        if (min(da, db) < PLATE_DISAGREE_TAU)
            return (da < db) ? warped_a : warped_b;
    }
    // SNAP (scratch): a coherent character texel shows the NEARER drawing, shifted rigidly to where the
    // character is at this instant, never a blend of two drawings -- a cel character has no in-between.
    if (FLOW_C_tex(HOOKED_pos).z > 0.5)
        return mix_t < 0.5 ? warped_a : warped_b;
    return mix(warped_a, warped_b, mix_t);
}

// ==== human-reading tail (generated by tests/add_human_reading.py; do not edit) ====
//!PARAM read_view
//!DESC 0 = normal output; 1/2/3 = velocity/acceleration/jerk painted for a human; 4/5/6 = the same fields raw, for a machine; 7 = the pooled reading raw; 8 = the per-cell mode memory raw; 9 = divergence, curl, shear raw
//!TYPE int
//!MINIMUM 0
//!MAXIMUM 9
0

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FLOW_H_AB
//!SAVE READ_FIELD
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!WHEN read_view 0 >
//!DESC [reading] velocity field in px at 1/8 res: the half-res flow this shader warps with

vec4 hook() {
    // FLOW_H is stored in half-resolution texels; x2 gives full-res px. The
    // two-frame family has one flow, so every mode reads velocity.
    return vec4(FLOW_H_AB_tex(HOOKED_pos).xy * 2.0, 0.0, 1.0);
}

//!TEXTURE MODE_MEM
//!SIZE 1440 270
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND READ_FIELD
//!BIND MODE_MEM
//!SAVE READ_MODE
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!WHEN read_view 0 >
//!DESC [reading] the per-cell mode memory: K candidate readings across frames, the heaviest reported with its support

// Lead G (NFRAME-LIMITS.md, 2026-09-05): on a field the tracker aliases, a mean of its readings across
// frames shrinks toward zero and the mode of them does not (the torus loop: 8.6 px against 1.7). Each
// cell keeps MODE_K candidates (mean vx, vy, weight): the frame's raw reading joins the nearest within
// MODE_R px (mean <- mix(mean, r, MODE_ALPHA), weight += 1) or replaces the weakest; weights decay by
// MODE_DECAY per frame, so the horizon is about 1 / (1 - MODE_DECAY) frames -- 33 at 0.97, which the
// steady field needs (0.90 reads 3.1 px, 0.80 5.1) and which holds stale zeros on transient motion.
// The storage holds 480 x MODE_K cells wide: a 4K frame's cells at MODE_K = 3.
// MODE_MISS / MODE_FAST: the ADAPTIVE horizon. A cell counts consecutive frames whose reading joined no
// candidate; past MODE_MISS of them every weight also decays by MODE_FAST, so what the cell learned while
// still fades within a few frames of new motion, while a cell whose readings keep agreeing keeps the long
// horizon. Measured: on the noisy torus loop the fixed horizon reads 1.7 px, MISS 3 / FAST 0.7 2.2, MISS 2 /
// FAST 0.5 2.4-3.8, MISS 1 / FAST 0.3 4-5 (the shipped mean 8.6); on live action only MISS 2 / FAST 0.5 and
// below paint a walking figure. Off (MISS huge) by default: the fixed horizon is the steady-field setting.
const int   MODE_K = 3;
const float MODE_R = 1.5, MODE_DECAY = 0.97, MODE_ALPHA = 0.3;
const float MODE_MISS = 1.0e9, MODE_FAST = 0.5;

vec4 hook() {
    ivec2 coord = ivec2(READ_FIELD_pos * READ_FIELD_size);
    vec2 r = READ_FIELD_tex(READ_FIELD_pos).xy;
    vec4 cand[3];
    int best = 0, weakest = 0, hit = -1; float dbest = 1.0e9;
    for (int k = 0; k < MODE_K; k++) {
        cand[k] = imageLoad(MODE_MEM, ivec2(coord.x * MODE_K + k, coord.y));
        cand[k].z *= MODE_DECAY;
        float d = length(cand[k].xy - r);
        if (cand[k].z > 0.0 && d < MODE_R && d < dbest) { dbest = d; hit = k; }
        if (cand[k].z < cand[weakest].z) weakest = k;
    }
    float miss = (hit >= 0) ? 0.0 : cand[0].w + 1.0;        // consecutive misses, kept in candidate 0's spare component
    if (miss > MODE_MISS) for (int k = 0; k < MODE_K; k++) cand[k].z *= MODE_FAST;
    if (hit >= 0) { cand[hit].xy = mix(cand[hit].xy, r, MODE_ALPHA); cand[hit].z += 1.0; }
    else { cand[weakest] = vec4(r, 1.0, 0.0); }
    cand[0].w = miss;
    for (int k = 0; k < MODE_K; k++) {
        imageStore(MODE_MEM, ivec2(coord.x * MODE_K + k, coord.y), cand[k]);
        if (cand[k].z > cand[best].z) best = k;
    }
    return vec4(cand[best].xy, cand[best].z, 1.0);
}

//!TEXTURE READ_ACC
//!SIZE 480 270
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND READ_FIELD
//!BIND READ_ACC
//!BIND READ_MODE
//!SAVE READ_POOL
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!WHEN read_view 0 >
//!DESC [reading] the reading's memory: 13x13 pool then an exponential mean (READ_MEMORY 0), or the per-cell mode with a support-weighted pool (1)

// Measured on the Metal demo (2026-09-01): pooling +/-48 px drops the
// static-background p95 from 0.52 to 0.10 px; the memory lifts a mover's
// direction coherence from 0.74 to 0.92. READ_EMA_ALPHA is per OUTPUT
// frame; 1.0 = no memory (frame-by-frame reading: fast oscillators average
// toward zero under any memory).
const float READ_EMA_ALPHA = 0.12;
const int   READ_POOL_R    = 6;
// READ_MEMORY 1: the per-cell mode (the pass above) pooled over MODE_POOL_R cells, each weighted by its
// support, and no exponential mean (the mode is the memory). Measured on the noisy torus loop
// (tests/loop.sh bg=tex noise=3): radius 0 reads 1.70 px and a backdrop speckle p95 of 0.029, radius 1
// 1.70 and 0.021, radius 6 5.5 px (the pool's mean over aliasing cells shrinks like the mean over frames).
const int   READ_MEMORY    = 0;
const int   MODE_POOL_R    = 1;

vec4 hook() {
    ivec2 coord = ivec2(READ_FIELD_pos * READ_FIELD_size);
    if (READ_MEMORY == 1) {
        vec2 fpx = vec2(0.0); float wsum = 0.0;
        for (int j = -MODE_POOL_R; j <= MODE_POOL_R; j++)
            for (int i = -MODE_POOL_R; i <= MODE_POOL_R; i++) {
                vec3 c = READ_MODE_tex(READ_FIELD_pos + vec2(float(i), float(j)) * READ_FIELD_pt).xyz;
                fpx += c.xy * c.z; wsum += c.z;
            }
        return vec4(fpx / max(wsum, 1.0e-6), 0.0, 1.0);
    }
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
//!BIND HOOKED
//!BIND READ_FIELD
//!SAVE READ_DERIV
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!WHEN read_view 0 >
//!DESC [reading] the velocity gradient tensor by central differences over neighbouring cells: divergence, curl, the two shears (1/frame)

// Lead E, the half that needs no new match (NFRAME-LIMITS.md, 2026-09-05): the field's own spatial
// derivatives. Cells are 8 px apart, so a central difference spans 16 px; units are 1/frame. Read the
// RAW field, not the pooled one: on the disc the pool's window damps the curl (0.26 -> 0.13 at 0.5 R).
vec4 hook() {
    vec2 uv = READ_FIELD_pos; vec2 pt = READ_FIELD_pt;
    vec2 dfdx = (READ_FIELD_tex(uv + vec2(pt.x, 0.0)).xy - READ_FIELD_tex(uv - vec2(pt.x, 0.0)).xy) / 16.0;
    vec2 dfdy = (READ_FIELD_tex(uv + vec2(0.0, pt.y)).xy - READ_FIELD_tex(uv - vec2(0.0, pt.y)).xy) / 16.0;
    return vec4(dfdx.x + dfdy.y, dfdx.y - dfdy.x, dfdx.x - dfdy.y, dfdy.x + dfdx.y);
}

//!HOOK FRAME_MIX
//!BIND FRAME_MIX
//!BIND READ_FIELD
//!BIND READ_POOL
//!BIND READ_MODE
//!BIND READ_DERIV
//!SAVE FRAME_MIX
//!WIDTH FRAME_MIX.w
//!HEIGHT FRAME_MIX.h
//!WHEN read_view 0 >
//!DESC [reading] paint the field over the picture (modes 1-3) or emit it raw for a machine (modes 4-9)

// two-frame family: one flow, so every mode reads velocity
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
const float READ_MACHINE_FS_DERIV = 0.5;    // 1/frame: divergence, curl, shear

vec3 read_hsv2rgb(vec3 c) {
    vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
    return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
}

vec4 hook() {
    bool vel = (read_view == 1 || read_view == 4 || read_view >= 7);
    if (read_view == 7)      // the pooled reading, raw: what the painting shows, whichever memory
        return vec4(0.5 + READ_POOL_tex(FRAME_MIX_pos).xy * (0.5 / READ_MACHINE_FS_VEL), 0.5, 1.0);
    if (read_view == 9)      // the velocity gradient tensor, raw: divergence (R), curl (G), the first shear (B)
        return vec4(0.5 + READ_DERIV_tex(FRAME_MIX_pos).xyz * (0.5 / READ_MACHINE_FS_DERIV), 1.0);
    if (read_view == 8)      // the per-cell mode memory, raw
        return vec4(0.5 + READ_MODE_tex(FRAME_MIX_pos).xy * (0.5 / READ_MACHINE_FS_VEL), 0.5, 1.0);
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
