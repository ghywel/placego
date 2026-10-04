#!/usr/bin/env python3
"""Generate a MULTI-LEVEL variational build: iterate at every pyramid level.

    ./gen_variational.py [S,E,Q,H iterations] [alpha] [sigma] [out.glsl] [sigma_flow] [S,E,Q,H medians] [base.glsl]

Milestone 1 put warped Horn-Schunck refinement only at the finest (half-res)
level, as a post-process. That validated the mechanism -- +5 to +7 dB on the
rotation ladder -- but did not transfer to real footage, for a reason already
measured twice in this project: REACH.

Where the image is flat, Ix = Iy = 0, so the HS update degenerates to
f_new = favg -- pure neighbourhood averaging. Flat-shaded animation is mostly
flat, so a half-res-only stage collapses into short-range diffusion, which is
exactly the configuration measured as ineffective (+0.02 dB at 120px). One
iteration propagates information one texel; at half resolution that is 2px,
so even 24 iterations reach ~48px. At 1/16 resolution one texel is 16px, so
the same iteration count reaches ~380px.

So: run the iterations at EVERY level, inside the coarse-to-fine cascade,
which is how variational optical flow is actually formulated. Coarse levels
supply reach, fine levels supply detail, and each level's result seeds the
next through the existing refine passes.

Cost works out FAVOURABLY versus milestone 1, because coarse levels are
nearly free. In full-resolution pass-equivalents, per direction:
    S: n/256    E: n/64    Q: n/16    H: n/4
So 16/12/8/6 iterations at S/E/Q/H costs ~2.3 equivalents per direction,
against 24 half-res iterations costing 6.0 -- less than half, with roughly
eight times the reach.

Iterations are uncached deliberately (they re-run every output frame). The
coarse levels are too cheap for that to matter; the half-res ones are not, and
caching them is the obvious optimisation once the approach earns its place.
"""
import os
import pathlib
import re
import sys
import tempfile

import add_human_reading as READING

# Resolved from this file's own location, not hardcoded. The previous absolute
# path was both machine-specific and WSL-only (/mnt/c/...), so the generator
# ran on exactly one host -- which the cross-platform smoke test caught the
# moment it was run under MSYS2.
HERE = pathlib.Path(__file__).resolve().parent
SHADERS = HERE.parent / "shaders"


def shader_arg(s):
    """A bare file name means a shader in shaders/; a path with a directory is used as given."""
    p = pathlib.Path(s)
    return p if p.parent != pathlib.Path(".") else SHADERS / p


SRC = str(SHADERS / "bidirectional-interpolation.glsl")

# level key -> (flow suffix, luma A, luma B, WIDTH/HEIGHT divisor, anchor)
LEVELS = [
    ("S", "FLOW_S", "LUMA_A_S", "LUMA_B_S", 16,
     "//!HOOK FRAME_MIX\n//!BIND HOOKED\n//!SAVE LUMA_A_E\n"),
    ("E", "FLOW_E", "LUMA_A_E", "LUMA_B_E", 8,
     "//!HOOK FRAME_MIX\n//!BIND HOOKED\n//!SAVE LUMA_A_Q\n"),
    ("Q", "FLOW_Q", "LUMA_A_Q", "LUMA_B_Q", 4,
     "//!HOOK FRAME_MIX\n//!BIND HOOKED\n//!SAVE LUMA_A_H\n"),
    ("H", "FLOW_H", "LUMA_A_H", "LUMA_B_H", 2,
     "// ---------------------------------------------------------------------\n"
     "// Vector median filter on both flow fields: rejects outlier vectors that\n"),
]

HEADER = """// ---------------------------------------------------------------------
// VARIATIONAL REFINEMENT at {lvl} ({div}x downsampled), {n} iterations per
// direction. Warped Horn-Schunck with edge-aware smoothness.
//
// Coherence enters the OBJECTIVE here rather than being imposed afterwards:
// each iteration jointly minimises brightness-constancy residual and
// deviation from the neighbourhood, so neighbouring texels constrain each
// other instead of each deciding alone. Linearising around the current flow
// (i.e. warping first) is what lets this handle motion larger than a pixel.
//
//   It    = B(x + f0) - A(x)
//   Ix,Iy = gradient of B at x + f0
//   favg  = edge-aware weighted mean of neighbouring flow
//   g     = favg - f0
//   rho   = Ix*g.x + Iy*g.y + It
//   f_new = favg - (Ix,Iy) * rho / (alpha^2 + Ix^2 + Iy^2)
//
// One texel of propagation per iteration means {reach}px of reach at this
// level, which is the whole reason the iterations are spread across the
// pyramid rather than concentrated at the finest level.
// ---------------------------------------------------------------------
"""

PASS = """//!HOOK FRAME_MIX
//!BIND {FLOW}
//!BIND {LREF}
//!BIND {LTGT}
//!SAVE {FLOW}
//!WIDTH HOOKED.w {DIV} /
//!HEIGHT HOOKED.h {DIV} /
//!COMPONENTS 2
//!DESC [high] variational {LVL} {DIR} (iter {I})
const float VAR_ALPHA = {ALPHA};
const float VAR_SIGMA_LUMA = {SIGMA};{SIGMAFLOWDECL}
vec4 hook() {{
    vec2 uv = {FLOW}_pos;
    vec2 f0 = {FLOW}_tex(uv).xy;
    vec2 pt = {LREF}_pt;

    float cl = {LREF}_tex(uv).r;
    vec2 acc = vec2(0.0);
    float wsum = 0.0;
    for (int y = -1; y <= 1; y++) {{
        for (int x = -1; x <= 1; x++) {{
            if (x == 0 && y == 0) continue;
            vec2 o = vec2(float(x), float(y)) * pt;
            float dl = {LREF}_tex(uv + o).r - cl;
            float ws = (x == 0 || y == 0) ? 1.0 : 0.70710678;
            float w = ws * exp(-(dl * dl) / (2.0 * VAR_SIGMA_LUMA * VAR_SIGMA_LUMA));
            vec2 nf = {FLOW}_tex(uv + o).xy;
{FLOWTERM}            acc += nf * w;
            wsum += w;
        }}
    }}
    vec2 favg = wsum > 0.0001 ? acc / wsum : f0;

    vec2 wuv = uv + f0 * pt;
    float It = {LTGT}_tex(wuv).r - {LREF}_tex(uv).r;
    float Ix = ({LTGT}_tex(wuv + vec2(pt.x, 0.0)).r - {LTGT}_tex(wuv - vec2(pt.x, 0.0)).r) * 0.5;
    float Iy = ({LTGT}_tex(wuv + vec2(0.0, pt.y)).r - {LTGT}_tex(wuv - vec2(0.0, pt.y)).r) * 0.5;

    vec2 g = favg - f0;
    float rho = Ix * g.x + Iy * g.y + It;
    float denom = VAR_ALPHA * VAR_ALPHA + Ix * Ix + Iy * Iy;
    return vec4(favg - vec2(Ix, Iy) * (rho / denom), 0.0, 0.0);
}}
"""

MEDIAN_HEADER = """// ---------------------------------------------------------------------
// VECTOR MEDIAN at {lvl} ({div}x downsampled), {n} pass(es) per direction.
//
// The base shader already medians the flow, but only at H and only 3x3 (twice,
// so about 5x5 of reach). That is enough for a stray texel and useless against
// what actually goes wrong on flat-shaded animation: small high-contrast
// features -- an eye, a mouth -- that get REDRAWN between source frames rather
// than moved. Block matching then finds a confident match to the wrong shape,
// and the result is a compact ISLAND of flow pointing somewhere the entire
// surrounding face disagrees with. Measured on blueydefect.mp4: islands up to
// 20px of deviation against a head moving 3-5px, several hundred pixels per
// frame, sitting exactly where the visible artifact is.
//
// A 22px island is 11 texels at H, so it out-votes a 5x5 kernel everywhere
// inside itself -- the median cannot fix at H what is already that large. The
// same island is 5.5 texels at Q, 2.8 at E, 1.4 at S, where a 3x3 kernel
// removes it outright. This is the reach principle this project keeps
// re-deriving: do the work at the level where the kernel is large relative to
// the defect, which is also where it is cheapest.
//
// Why a median and not a blur: a genuine motion boundary is a CONTIGUOUS
// region, so most of its neighbours share its value and it survives the vote.
// A false match is a local minority and does not. A blur cannot tell them
// apart and would smear the boundary instead.
//
// Rejected vectors are replaced by the neighbourhood consensus, which for a
// redrawn feature means it travels with the surface it sits on -- the face --
// and the shape change resolves as a cross-fade in the right place. That is
// the correct answer for content that has no correspondence to find.
// ---------------------------------------------------------------------
"""

MEDIAN = """//!HOOK FRAME_MIX
//!BIND {FLOW}
//!SAVE {FLOW}
//!WIDTH HOOKED.w {DIV} /
//!HEIGHT HOOKED.h {DIV} /
//!COMPONENTS 2
//!DESC [high] vector median {LVL} {DIR} (pass {I})
vec4 hook() {{
    vec2 v[9];
    int n = 0;
    for (int y = -1; y <= 1; y++) {{
        for (int x = -1; x <= 1; x++) {{
            vec2 o = vec2(float(x), float(y)) * {FLOW}_pt;
            v[n++] = {FLOW}_tex({FLOW}_pos + o).xy;
        }}
    }}

    // The vector median is the candidate minimising total distance to all the
    // others -- a joint choice over (x,y), not two independent scalar medians,
    // which could otherwise invent a vector no neighbour actually voted for.
    //
    // TIE_MARGIN: deterministic tie-breaking, the same mechanism and the same
    // reasoning as the block match's -- see the base shader's coarse A->B
    // search. It matters here too: where several of the nine candidates agree,
    // their totals are near-tied, so without a margin a rounding difference
    // decides between two equal-sized clusters that disagree. The incumbent is
    // the first candidate in a fixed scan order.
    const float TIE_MARGIN = 1.0e-4;
    float best_cost = 1e30;
    vec2 best = v[4];
    for (int i = 0; i < 9; i++) {{
        float cost = 0.0;
        for (int j = 0; j < 9; j++)
            cost += length(v[i] - v[j]);
        if (cost < best_cost * (1.0 - TIE_MARGIN)) {{
            best_cost = cost;
            best = v[i];
        }}
    }}

    return vec4(best, 0.0, 0.0);
}}
"""



# ---------------------------------------------------------------------------
# THE GLOBAL-MOTION SEED (2026-09-20; NFRAME-LIMITS.md "The fast pan over fine texture" and its sequel).
# A tracking shot's wall crossing the frame at 30-40 px per source frame collapsed to the linear blend,
# because at the coarse level (1/16) a shift of 2.3 texels and a shift of 0.3 are the same to texture
# whose grain is a two-texel period there, and the per-texel search takes the nearer; the whole frame
# can tell them apart (its coarser structure breaks the tie), and a phase correlation off the same images
# read the film's pan exactly. So: two small passes find the frame's dominant shift at the coarse level
# (every candidate shift's SAD on a sparse grid, in parallel, then one argmin), the coarse search
# descends from it as a FOURTH seed (kept in the second cache's .zw), the 1/8 level refines it as a
# FIFTH candidate scored like the others -- and the 1/8 level's small-motion prior is measured from the
# frame's own shift instead of from zero, which was the term that mattered: at 4.6 texels of true motion
# the prior toward zero outweighed the match, and the seed alone moved nothing past 36 px. With the
# frame's shift at zero (no global motion) every scored term is exactly what it was. GLOBAL_SEED=1 in
# the environment emits it; without the variable the output is byte-identical to the form before.
# Ranges: +-4 x +-2 coarse texels (64 x 32 px at 1080p) in half-texel steps, 17 x 9 candidates.
# ---------------------------------------------------------------------------
GLOBAL_SEED = os.environ.get("GLOBAL_SEED", "0") == "1"

# ---------------------------------------------------------------------------
# THE QUARTER LEVEL'S ZERO DESCENT UNDER MOIRE (2026-09-21; NFRAME-LIMITS.md "The cage"). A fine periodic print
# -- the film's railing, bars nine pixels apart -- is a Moire to the 1/8 level (eight-pixel sampling), and the
# flow read there is the Moire's; the quarter level then refines from a flow that is a period out and the bars
# bend. Where the 1/8 level's picture of a texel is a Moire (point contrast at 1/8 far above the same footprint
# box-averaged from 1/4), the quarter level runs a second descent from ZERO, and the two compete: the zero
# descent wins only as the smaller of two GOOD matches with a RIDGE between them (the match half way between
# two minima of a periodic print is at its worst; a flat interior matches everywhere and has no ridge, and
# there the seed stands -- L1 lost six decibels before that test). +3 dB on the synthetic cage, +0.8 on the
# film's railing, the ladder within its noise either way (2026-09-21). QZERO_MOIRE=1 emits it.
# ---------------------------------------------------------------------------
QZERO_MOIRE = os.environ.get("QZERO_MOIRE", "0") == "1"

def add_qzero_moire(t, moire_min=0.25, good=0.30, ridge=1.5):
    def once(a):
        n = t.count(a)
        assert n == 1, f"qzero: anchor found {n} times: {a[:70]!r}"
    a = "//!BIND LUMA_A_Q\n//!BIND LUMA_B_Q\n//!BIND FLOW_E_AB\n//!SAVE FLOW_Q_AB\n"
    once(a)
    t = t.replace(a, "//!BIND LUMA_A_Q\n//!BIND LUMA_B_Q\n//!BIND LUMA_A_E\n//!BIND FLOW_E_AB\n//!SAVE FLOW_Q_AB\n")
    a = "//!BIND LUMA_A_Q\n//!BIND LUMA_B_Q\n//!BIND FLOW_E_BA_ST\n//!BIND FLOW_E_AB\n//!SAVE FLOW_Q_BA\n"
    once(a)
    t = t.replace(a, "//!BIND LUMA_A_Q\n//!BIND LUMA_B_Q\n//!BIND LUMA_B_E\n//!BIND FLOW_E_BA_ST\n//!BIND FLOW_E_AB\n//!SAVE FLOW_Q_BA\n")
    MOIRE = """
// MOIRE EVIDENCE for the 1/8 level at this texel, as moire_s() reads it for the coarse level: point contrast
// at 1/8 against the same footprint box-averaged from this level's texels. Structure between this level's
// Nyquist and the 1/8 level's survives there as a Moire whose motion is its own (bars nine pixels apart
// under eight-pixel sampling: the film's cage, 2026-09-21), and a flow read from it is not the frame's.
float moire_e_{S}(vec2 uv) {{
    float plo = 1.0, phi = 0.0, blo = 1.0, bhi = 0.0;
    for (int j = -1; j <= 1; j++) {{
        for (int i = -1; i <= 1; i++) {{
            vec2 c = uv + vec2(float(i), float(j)) * LUMA_{S}_E_pt;
            float p = LUMA_{S}_E_tex(c).r;
            float b = 0.25 * (LUMA_{S}_Q_tex(c + vec2(-0.25, -0.25) * LUMA_{S}_E_pt).r + LUMA_{S}_Q_tex(c + vec2(0.25, -0.25) * LUMA_{S}_E_pt).r
                            + LUMA_{S}_Q_tex(c + vec2(-0.25, 0.25) * LUMA_{S}_E_pt).r + LUMA_{S}_Q_tex(c + vec2(0.25, 0.25) * LUMA_{S}_E_pt).r);
            plo = min(plo, p); phi = max(phi, p); blo = min(blo, b); bhi = max(bhi, b);
        }}
    }}
    float cp = phi - plo, cb = bhi - blo;
    return cp > 0.02 ? clamp(1.0 - cb / cp, 0.0, 1.0) : 0.0;
}}
const float MOIRE_E_MIN = {MM};
"""
    ZERO = """    if (moire_here) {
        // The 1/8 level's picture here was a Moire, so its flow may be the Moire's: a second descent from ZERO,
        // and the two compete. The zero descent wins only when BOTH matches are good, a RIDGE lies between
        // them (half way between two minima of a periodic print the match is at its worst; a flat interior
        // matches everywhere and has no ridge, and there the seed stands) and it is the smaller motion -- only
        // the prior knows which of two good matches is the frame's (2026-09-21).
        vec2 z_off = vec2(0.0);
        float z_cost = SAD(UV, UV);
        for (int y = -REFINE_SEARCH_RADIUS; y <= REFINE_SEARCH_RADIUS; y++) {
            for (int x = -REFINE_SEARCH_RADIUS; x <= REFINE_SEARCH_RADIUS; x++) {
                if (x == 0 && y == 0) continue;
                vec2 off = vec2(float(x), float(y)) * LUMA_A_Q_pt;
                float cost = SAD(UV, UV + off) + REFINE_REG_LAMBDA * length(vec2(float(x), float(y)));
                if (cost < z_cost * (1.0 - TIE_MARGIN)) { z_cost = cost; z_off = off; }
            }
        }
        float good = GOOD * 9.0 * max(CONTRAST(UV), 0.02);
        float z_mag = length(z_off / LUMA_A_Q_pt), b_mag = length(best_off / LUMA_A_Q_pt);
        float ridge = SAD(UV, UV + 0.5 * (z_off + best_off));
        if (z_cost <= good && best_cost <= good && ridge > RIDGE * good && z_mag < b_mag - 0.5) {
            best_off = z_off; best_cost = z_cost;
        }
    }
"""
    for S, uv, save, fn, lc, seed in (("A", "uv_a", "FLOW_Q_AB", "sad5x5_q", "local_contrast_5x5_q",
                                       "    vec2 base_off = FLOW_E_AB_tex(snap_texel(uv_a, FLOW_E_AB_size)).xy * 2.0 * LUMA_A_Q_pt;\n"),
                                      ("B", "uv_b", "FLOW_Q_BA", "sad5x5_q2", "local_contrast_5x5_q2",
                                       "    vec2 base_off = imageLoad(FLOW_E_BA_ST, ivec2(floor((FLOW_E_AB_size) * (snap_texel(uv_b, FLOW_E_AB_size))))).xy * 2.0 * LUMA_A_Q_pt;\n")):
        i = t.index(f"//!SAVE {save}\n"); j = t.index("vec4 hook() {", i)
        t = t[:j] + MOIRE.format(S=S, MM=moire_min) + t[j:]
        once(seed)
        t = t.replace(seed, seed + f"    bool moire_here = moire_e_{S}({uv}) > MOIRE_E_MIN;\n")
        i = t.index(f"//!SAVE {save}\n"); j = t.index("    vec4 result = vec4(best_off / LUMA_A_Q_pt, 0.0, 0.0);\n", i)
        body = (ZERO.replace("UV", uv).replace("SAD(", fn + "(").replace("CONTRAST(", lc + "(")
                .replace("GOOD", f"{good:.2f}").replace("RIDGE", f"{ridge:.1f}"))
        t = t[:j] + body + t[j:]
    return t


# ---------------------------------------------------------------------------
# THE COHERENCE GATE (2026-09-21; NFRAME-LIMITS.md "The field's coherence"). On a fine periodic print under a
# sub-pixel drift every warp of the family, even one with the TRUE flow forced, scores six decibels below the
# plain blend of the two frames: the target there is not a better flow but knowing when not to warp. Three
# things together say so, none alone: the field disagrees with itself (SUPPORT: the share of a texel's 9x9
# neighbours within 0.75 px of its own flow, under a half -- a print matched a period out gives patches of
# wrong flow; a moving texture's right flows agree, and a moving object's edge has half its window on each
# side), the two frames nearly agree UNMOVED (a 5x5 mean of |A - B| under 0.4 of the local contrast; an edge
# that moved eight pixels disagrees by the whole contrast), and zero matches as well as the flow does
# (RELATIVE: |A - B| at zero against |A - B(uv + flow)|; a random texture in motion agrees at zero to a third
# of its contrast and at its flow to nothing, which the absolute test alone could not tell from a drift --
# M1 -5). One pass at the half level, and the final pass blends the frames unwarped by the product of the
# three fades. Measured: the synthetic cage +8.4 (C1) / +5.3 (C2), the film's railing +2.3, the ladder within
# its noise (M1 -2.3, F1 -1.6, H1 -1.4 / P1 +7.4, L1 +2.2, M2 +1.3), +2.8% time. COHERENCE_GATE=1 emits it;
# it stacks with QZERO_MOIRE=1 (the cage +10.9 stacked).
# ---------------------------------------------------------------------------
COHERENCE_GATE = os.environ.get("COHERENCE_GATE", "0") == "1"

def add_coherence_gate(t, lo=0.50, hi=0.70, radius=4, tol_px=0.75, agree=0.40, rel=0.5, rel_floor=0.10):
    def once(a):
        n = t.count(a)
        assert n == 1, f"coherence gate: anchor found {n} times: {a[:70]!r}"
    n_taps = float((2 * radius + 1) ** 2)
    PASS = f"""// ---------------------------------------------------------------------
// The field's coherence (2026-09-21): the share of each texel's {2*radius+1}x{2*radius+1}
// neighbours (half-res texels) whose final flow agrees with its own within
// {tol_px} px. A periodic print matched a period out gives patches of wrong
// flow whose neighbours disagree; a moving texture's right flows agree.
// ---------------------------------------------------------------------
//!HOOK FRAME_MIX
//!BIND FLOW_H_AB
//!BIND LUMA_A_H
//!BIND LUMA_B_H
//!SAVE SUPPORT
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 3
//!DESC [high] the field's support, and the frames' agreement unmoved (absolute, and relative to the flow's own match)
vec4 hook() {{
    vec2 uv = FLOW_H_AB_pos;
    vec2 f0 = FLOW_H_AB_tex(uv).xy;
    const float tol = {tol_px:.3f} * 0.5;          // px -> half-res texels
    float n = 0.0;
    for (int y = -{radius}; y <= {radius}; y++) {{
        for (int x = -{radius}; x <= {radius}; x++) {{
            vec2 f = FLOW_H_AB_tex(uv + vec2(float(x), float(y)) * FLOW_H_AB_pt).xy;
            n += (length(f - f0) < tol) ? 1.0 : 0.0;
        }}
    }}
    // and the frames' agreement at ZERO offset, as a share of the local contrast: a fine print under a
    // sub-pixel drift agrees with itself unmoved (a tenth to a quarter); an object edge that moved eight pixels
    // does not (the whole contrast across the band). The blend is only right where they agree.
    // RELATIVE to the flow's own match: a periodic print a period out matches at zero as well as at its
    // flow (the two are the same match); a random texture in motion matches at zero to a third of its
    // contrast and at its flow to nothing -- the absolute test could not tell the two apart (M1 -5).
    float sad0 = 0.0, sadf = 0.0, lo = 1.0, hi = 0.0;
    vec2 fuv = f0 * LUMA_A_H_pt;
    for (int y = -2; y <= 2; y++) {{
        for (int x = -2; x <= 2; x++) {{
            vec2 o = vec2(float(x), float(y)) * LUMA_A_H_pt;
            float a = LUMA_A_H_tex(uv + o).r;
            sad0 += abs(a - LUMA_B_H_tex(uv + o).r);
            sadf += abs(a - LUMA_B_H_tex(uv + fuv + o).r);
            lo = min(lo, a); hi = max(hi, a);
        }}
    }}
    float c25 = 25.0 * max(hi - lo, 0.02);
    float ratio = sad0 / c25;                                   // the absolute agreement, a share of the contrast
    float rel = sad0 / (sadf + {rel_floor:.2f} * c25);           // and the relative one: under 1, zero matches as well as the flow
    return vec4(n / {n_taps:.1f}, ratio, rel, 0.0);
}}

"""
    a = """// ---------------------------------------------------------------------
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
"""
    once(a)
    t = t.replace(a, PASS + a.replace("//!BIND EDGE_B\n", "//!BIND EDGE_B\n//!BIND SUPPORT\n"))
    a = """    vec4 warped_a = warp_sample_a(HOOKED_pos - flow_ab * mix_t);
    vec4 warped_b = warp_sample_b(NEXT_pos + flow_ab * (1.0 - mix_t));

    return mix(warped_a, warped_b, mix_t);
}
"""
    once(a)
    t = t.replace(a, f"""    vec4 warped_a = warp_sample_a(HOOKED_pos - flow_ab * mix_t);
    vec4 warped_b = warp_sample_b(NEXT_pos + flow_ab * (1.0 - mix_t));

    // The coherence gate: where the flow's own neighbours disagree with it (SUPPORT low), the two frames
    // blended unwarped -- a periodic print matched a period out is put back where it was, unmoved, rather
    // than a bar's width away (2026-09-21).
    vec3 sup = SUPPORT_tex(HOOKED_pos).rgb;
    float unwarped = (1.0 - smoothstep({lo:.2f}, {hi:.2f}, sup.x)) * (1.0 - smoothstep({agree:.2f}, {agree:.2f} + 0.15, sup.y))
                   * (1.0 - smoothstep({rel:.2f}, {rel:.2f} + 0.5, sup.z));
    vec4 warped = mix(warped_a, warped_b, mix_t);
    if (unwarped <= 0.0) return warped;
    return mix(warped, mix(HOOKED_tex(HOOKED_pos), NEXT_tex(NEXT_pos), mix_t), unwarped);
}}
""")
    return t


# ---------------------------------------------------------------------------
# THE 1/8 PROPAGATION MADE MOTION-EDGE AWARE (2026-09-27; NFRAME-LIMITS.md "The field on real bodies", the limb).
# The base's three propagation passes replace each 1/8 texel's flow with a CONTRAST-weighted mean of its own
# (weight 8 c^2) and its 5 x 5 neighbours' (their contrast / distance). A textured still background is all
# high-contrast zeros, so a small moving object's flow is averaged toward zero. On K1 (a limb sweeping a still
# textured wall) the fresh 1/8 search reads the limb at 0.67 at 18-24 px/frame and propagation leaves 0.29; on
# K3 (the same limb brighter) 0.62 -> 0.29 at 36-42. A flat background's zeros carry no weight, which is why the
# dark wall never showed it. EDGE_PROP=1 multiplies each neighbour's weight by its flow's AGREEMENT with the
# texel's own, 1 / (1 + (|f_n - f_own| / TAU)^2), blended in by the texel's own confidence (a flat texel's own
# flow means nothing, so it still fills from its neighbours exactly as before: the aperture fill the propagation
# is for). TAU in 1/8 texels (EDGE_PROP_TAU, default 1.0 = 8 px). Without the variable the output is
# byte-identical to the form before.
# VERDICT (2026-09-27, the same evening): REFUTED, ships no shader. The full ladder, best-of-3 on the Mac: capped
# mean -0.36 dB, 21 of 42 cases down -- the period family collapses (H1 and V1 -11.6, H2 and V2 -5.8, R3 -4.6,
# A5 -4.0). There a texel's own raw match is CONFIDENTLY WRONG (an alias) and the contrast-weighted mean across
# disagreeing neighbours is exactly what carries the right basin over it ("propagation carries the basin"): the
# weight protects confident texels that disagree with their neighbours, which is right at a limb's edge and fatal
# at an alias, and disagreement alone cannot tell the two apart. On the limb it had given +1.07 dB at 18-24 px/frame.
# Kept as the record of the design point (tests/probes/limb/PREDICTION.md has the table).
# ---------------------------------------------------------------------------
EDGE_PROP = os.environ.get("EDGE_PROP", "0") == "1"
EDGE_PROP_TAU = float(os.environ.get("EDGE_PROP_TAU", "1.0"))


def add_edge_prop(t, tau=EDGE_PROP_TAU):
    # the neighbour sums take two forms: a sampled texture, FLOW_E_*_tex(uv + o).xy, and (the fused B->A twins of
    # passes 2 and 3) a storage image, imageLoad(FLOW_E_BA_PROP_STn, ...(uv + o)...).xy -- both captured whole
    pat = re.compile(r"(?P<ind>[ \t]+)acc \+= w \* (?P<expr>(?:FLOW_E_\w+_tex|imageLoad)\(.*?\)\.xy);\n")
    n = [0]

    def sub(m):
        n[0] += 1
        ind, expr = m.group("ind"), m.group("expr")
        assert "uv + o" in expr, expr
        return (f"{ind}vec2 fn = {expr};\n"
                f"{ind}float dfl = length(fn - own) / PROP_TAU;\n"
                f"{ind}w *= mix(1.0, 1.0 / (1.0 + dfl * dfl), c_own);\n"
                f"{ind}acc += w * fn;\n")
    out = pat.sub(sub, t)
    decl = "const float PROP_SELF_WEIGHT = 8.0;\n"
    k = out.count(decl)
    assert n[0] == 6 and k == 3, f"edge prop: {n[0]} neighbour sums (want 6), {k} propagation passes (want 3)"
    out = out.replace(decl, decl + f"const float PROP_TAU = {tau};   // EDGE_PROP: flow agreement, 1/8 texels\n")
    assert out.count("float dfl = length(fn - own) / PROP_TAU;") == 6
    return out


# ---------------------------------------------------------------------------
# THE COARSE TEXTURE-ENERGY CHANNEL (2026-09-27; NFRAME-LIMITS.md "The field on real bodies", the limb and after).
# The coarse (1/16) and 1/8 lumas are POINT-SAMPLED: one tap per footprint. A fine grain moving by anything but a
# multiple of the texel is tapped at different grain cells in A and B, so a small textured mover's coarse picture
# scrambles while a still background's taps match at zero (the party's children against a still room; K1).
# COARSE_ENERGY=1 adds, per frame, a smoothed TEXTURE ENERGY:
#   - each 4 x 4 block's 2-px gradient magnitude on dense taps, at quarter resolution, blurred separably
#     (sigma 12 px);
#   - carried in the coarse and 1/8 lumas' .g, and scored beside the luma: SAD + W |dE|, W_S at 1/16, W_E at 1/8;
#   - the 1/8 level's post-propagation data check scores the same way.
# A statistic of the grain, not a sample of it, so it does not scramble as the grain moves. It is NOT section 8's
# prefilter, which replaced the taps and lost their contrast.
# VERDICT: A TRADE (the full ladder best-of-3 on the Mac, COARSE_ENERGY_WS 8 / WE 1, the best of four weightings):
#   - 23 of 42 cases up: L1 +6.2, L2 +4.7, L8 +3.4, L3 +2.8, F1 +2.4, R3 +2.3, L4 +2.1, M1 +1.9;
#   - the limb +3 to +5 dB at 18-36 px/frame; real footage level to +0.66; cost +7%;
#   - against: V3 -7.9 (the half-period alias, which the base rescues at the 1/8 level and any coarse energy
#     term unseats) and the sine bars -1.5 / -1.8.
# A switch, off by default: the owner's call. Without the variable the output is byte-identical.
# ---------------------------------------------------------------------------
COARSE_ENERGY = os.environ.get("COARSE_ENERGY", "0") == "1"
COARSE_ENERGY_WS = float(os.environ.get("COARSE_ENERGY_WS", "8"))
COARSE_ENERGY_WE = float(os.environ.get("COARSE_ENERGY_WE", "1"))


# ---------------------------------------------------------------------------
# THE HALF-PERIOD ALIAS (2026-09-28; tests/alias_carry.py, which holds the passes and their reasoning; NFRAME-LIMITS.md
# "The carry, offline" and "Which of the cage's switches holds V3"; PRIOR-ART.md, the periodic-interior survey).
# ALIAS_PRIOR=1 (with GLOBAL_SEED=1): where a 1/8-level cell's two cost basins tie, the frame's shift breaks the tie
# only if it IS one of them. ALIAS_CARRY=1: at the quarter level, each cell keeps its flow and the other basin, and a
# semi-global min-sum over the two carries a pattern's ends into its tied interior, every frame. Without the
# variables the output is byte-identical to the form before.
# ---------------------------------------------------------------------------
ALIAS_PRIOR = os.environ.get("ALIAS_PRIOR", "0") == "1"
ALIAS_CARRY = os.environ.get("ALIAS_CARRY", "0") == "1"
# OUTLINE_ADOPT=1 (2026-09-30; tests/outline_adopt.py, ENERGY-TRANSFER.md "The shared stage"): a locked print adopts its
# outline's motion at the quarter level, after the carry's pick. Needs ALIAS_CARRY=1.
OUTLINE_ADOPT = os.environ.get("OUTLINE_ADOPT", "0") == "1"
# PRINT_LATTICE=1 (2026-10-01; tests/print_lattice.py, ENERGY-TRANSFER.md lead 4): a fast periodic print re-scored at full
# resolution among the aliases of its own lattice, after the carry's pick (and the adoption). Needs ALIAS_CARRY=1.
PRINT_LATTICE = os.environ.get("PRINT_LATTICE", "0") == "1"
# TRUST_GATE=1 (2026-10-01; tests/trust_gate.py, ENERGY-TRANSFER.md "The per-level trust gate, returned to"): where the 1/8
# level is ambiguous, the quarter level offers its best minima within +-24 px and full resolution decides, after the
# carry's pick and before the adoption. Needs ALIAS_CARRY=1.
TRUST_GATE = os.environ.get("TRUST_GATE", "0") == "1"
# CUT_MOTION=1 (2026-10-01; tests/cut_motion.py, ENERGY-TRANSFER.md C1 and C2): the warp's cut gate holds a frame only if the
# frames' difference is over its threshold AND the final flow leaves more than CUT_EXPLAINED of it unexplained.
CUT_MOTION = os.environ.get("CUT_MOTION", "0") == "1"
ALIAS_APERTURE = os.environ.get("ALIAS_APERTURE", "1") == "1"    # the carry's aperture rule (build 5); 0 = build 4


def add_coarse_energy(t, ws=COARSE_ENERGY_WS, we=COARSE_ENERGY_WE):
    import coarse_energy                     # tests/coarse_energy.py: the transform, shared with the limb probe
    return coarse_energy.add(t, ws, we)


def add_global_seed(t, rx=4.0, ry=2.0):
    nx = int(2 * rx / 0.5) + 1; ny = int(2 * ry / 0.5) + 1
    def once(a):
        n = t.count(a)
        assert n == 1, f"global seed: anchor found {n} times: {a[:70]!r}"
    # The 1/8 lumas are made after the coarse search in the base's order; the frame-wide Moire evidence the
    # global shift is gated on needs them, so their two passes move ahead of it (they read the frames alone).
    lumas = ""
    for name, src in (("LUMA_A_E", "HOOKED"), ("LUMA_B_E", "NEXT")):
        blk = (f"//!HOOK FRAME_MIX\n//!BIND {src}\n//!SAVE {name}\n//!WIDTH HOOKED.w 8 /\n//!HEIGHT HOOKED.h 8 /\n//!COMPONENTS 1\n"
               f"//!DESC [high] downsample frame {'A' if src == 'HOOKED' else 'B'} to 1/8 res (luma)\nvec4 hook() {{\n"
               f"    return vec4(dot({src}_tex({src}_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);\n}}\n\n")
        once(blk)
        t = t.replace(blk, "")
        lumas += blk
    a = "// ---------------------------------------------------------------------\n// Sixteenth-res coarse search, both directions: 5-step, 5x5 SAD window.\n"
    once(a)
    t = t.replace(a, lumas + f"""// ---------------------------------------------------------------------
// The global-motion seed (GLOBAL_SEED=1 at generation): the frame's dominant
// shift at the coarse level, A -> B, in half-texel steps over +-{rx:.0f} x +-{ry:.0f}
// texels. One texel of GLOBAL_COST per candidate shift, each the SAD of A
// against B shifted, on a 16 x 16 sparse grid of the central frame; then
// GLOBAL_SHIFT, one texel, the argmin. A per-texel search cannot resolve a
// shift that aliases the texture's own period at this level; the frame as
// a whole can, because the coarser structure breaks the tie.
// ---------------------------------------------------------------------
//!HOOK FRAME_MIX
//!BIND LUMA_A_S
//!BIND LUMA_B_S
//!BIND LUMA_A_E
//!SAVE GLOBAL_COST
//!WIDTH {nx}
//!HEIGHT {ny}
//!COMPONENTS 2
//!DESC [global] the cost of every candidate frame shift; at the zero shift, the frame's Moire evidence too
vec4 hook() {{
    ivec2 c = ivec2(LUMA_A_S_pos * vec2({nx}.0, {ny}.0));
    vec2 shift = (vec2(c) * 0.5 - vec2({rx:.1f}, {ry:.1f})) * LUMA_A_S_pt;
    const int N = 16;
    float acc = 0.0, moire = 0.0;
    bool zero = (c == ivec2({nx} / 2, {ny} / 2));
    for (int y = 0; y < N; y++) {{
        for (int x = 0; x < N; x++) {{
            vec2 uv = vec2(0.2, 0.2) + (vec2(float(x), float(y)) + 0.5) / float(N) * 0.6;
            acc += abs(LUMA_A_S_tex(uv).r - LUMA_B_S_tex(uv + shift).r);
            if (zero) {{
                // the coarse level's Moire evidence here, as moire_s() reads it per texel: point contrast at
                // 1/16 against the same footprint box-averaged from 1/8; texture above the coarse level's
                // Nyquist survives point sampling at full contrast and the box takes it out
                float plo = 1.0, phi = 0.0, blo = 1.0, bhi = 0.0;
                for (int j = -1; j <= 1; j++) for (int i = -1; i <= 1; i++) {{
                    vec2 q = uv + vec2(float(i), float(j)) * LUMA_A_S_pt;
                    float pv = LUMA_A_S_tex(q).r;
                    float bv = 0.25 * (LUMA_A_E_tex(q + vec2(-0.25, -0.25) * LUMA_A_S_pt).r + LUMA_A_E_tex(q + vec2(0.25, -0.25) * LUMA_A_S_pt).r
                                     + LUMA_A_E_tex(q + vec2(-0.25, 0.25) * LUMA_A_S_pt).r + LUMA_A_E_tex(q + vec2(0.25, 0.25) * LUMA_A_S_pt).r);
                    plo = min(plo, pv); phi = max(phi, pv); blo = min(blo, bv); bhi = max(bhi, bv);
                }}
                float cp = phi - plo, cb = bhi - blo;
                moire += cp > 0.02 ? clamp(1.0 - cb / cp, 0.0, 1.0) : 0.0;
            }}
        }}
    }}
    return vec4(acc / float(N * N), moire / float(N * N), 0.0, 0.0);
}}

//!TEXTURE GLOBAL_PREV
//!SIZE 1 1
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND GLOBAL_COST
//!BIND GLOBAL_PREV
//!SAVE GLOBAL_SHIFT
//!WIDTH 1
//!HEIGHT 1
//!COMPONENTS 2
//!DESC [global] the frame's dominant shift, in coarse texels
vec4 hook() {{
    float best = 1.0e30; vec2 bestShift = vec2(0.0);
    for (int y = 0; y < {ny}; y++) {{
        for (int x = 0; x < {nx}; x++) {{
            float cst = GLOBAL_COST_tex((vec2(float(x), float(y)) + 0.5) / GLOBAL_COST_size).r;
            // a small pull toward zero: a flat cost surface (a blank frame) must not pick a large shift
            vec2 s = vec2(float(x), float(y)) * 0.5 - vec2({rx:.1f}, {ry:.1f});
            cst += 0.002 * length(s);
            if (cst < best) {{ best = cst; bestShift = s; }}
        }}
    }}
    // (A margin test against the runner-up more than a texel away was tried first and dropped: on the
    // periodic ladder cases the aliased coarse level gave the wrong pick a wide margin anyway, and on a
    // tracking shot -- the film -- the still subject makes every frame's surface two-valued, so the test
    // refused the pan on every other frame and the prior flickered, which is worse than either state.
    // The three gates below are what hold.)
    // And the frame must AGREE WITH THE LAST PAIR: a pan persists, so a shift that jumps by more than a
    // texel from the pair before is not a pan but the cost surface's noise -- on the ladder's stairs the
    // aliased coarse level hands a different minimum every pair (+0.4, -1.0, +1.7 texels on H2, whose
    // motion is 0.375), and each one taken would drag the field to it. The pair's raw best is remembered
    // (once per pair, not per output frame) so a pan that starts is accepted from its second pair.
    vec2 prev = imageLoad(GLOBAL_PREV, ivec2(0)).xy;
    vec2 raw = bestShift;
    // And the coarse level must be able to SEE the frame: where its texture lies above the level's
    // Nyquist (the ladder's stairs, a fine periodic print), what moves at 1/16 is a Moire that moves at
    // its own speed, and the shift found there is the Moire's, not the frame's (H2 read +1.8 texels for
    // a motion of 0.375). The frame's mean Moire evidence, as moire_s() reads it per texel, refuses it.
    const float GLOBAL_MOIRE_MAX = 0.25;
    if (GLOBAL_COST_tex((vec2({nx} / 2, {ny} / 2) + 0.5) / GLOBAL_COST_size).g > GLOBAL_MOIRE_MAX) bestShift = vec2(0.0);
    if (max(abs(raw.x - prev.x), abs(raw.y - prev.y)) > 1.0) bestShift = vec2(0.0);
    if (pair_changed) imageStore(GLOBAL_PREV, ivec2(0), vec4(raw, 0.0, 0.0));
    // And only for a FAST pan. Within a texel and a half (24 px at 1080p) the per-texel search reaches the
    // motion on its own and the seed has nothing to add but its mistakes: the ladder's small periodic
    // motions (the stairs at 4-6 px) read a wrong shift of about a texel with every gate above passed,
    // since consecutive wrong picks can agree. Faded in between one and two texels, so nothing switches.
    bestShift *= smoothstep(1.0, 2.0, length(raw));
    return vec4(bestShift, 0.0, 0.0);
}}

""" + a)
    a = "//!BIND LUMA_A_S\n//!BIND LUMA_B_S\n//!SAVE FLOW_S_AB\n"
    once(a)
    t = t.replace(a, "//!BIND LUMA_A_S\n//!BIND LUMA_B_S\n//!BIND GLOBAL_SHIFT\n//!SAVE FLOW_S_AB\n")
    a = ("    vec2 off_b = descend_s2(uv_b, start_b, cost_b);\n    vec2 off_c = descend_s2(uv_b, prev_s, cost_c);\n"
         "    imageStore(FLOW_S_BA_CACHE2, coord, vec4(off_c / LUMA_A_S_pt, 0.0, 0.0));\n")
    once(a)
    t = t.replace(a, ("    vec2 off_b = descend_s2(uv_b, start_b, cost_b);\n    vec2 off_c = descend_s2(uv_b, prev_s, cost_c);\n"
                      "    float cost_g;\n    vec2 off_g = descend_s2(uv_b, -GLOBAL_SHIFT_tex(vec2(0.5)).xy * LUMA_A_S_pt, cost_g);\n"
                      "    imageStore(FLOW_S_BA_CACHE2, coord, vec4(off_c / LUMA_A_S_pt, off_g / LUMA_A_S_pt));\n"))
    a = ("    vec2 off_b = descend_s(uv_a, start_b, cost_b);\n    vec2 off_c = descend_s(uv_a, prev_s, cost_c);\n"
         "    imageStore(FLOW_S_AB_CACHE2, coord, vec4(off_c / LUMA_A_S_pt, 0.0, 0.0));\n")
    once(a)
    t = t.replace(a, ("    vec2 off_b = descend_s(uv_a, start_b, cost_b);\n    vec2 off_c = descend_s(uv_a, prev_s, cost_c);\n"
                      "    float cost_g;\n    vec2 off_g = descend_s(uv_a, GLOBAL_SHIFT_tex(vec2(0.5)).xy * LUMA_A_S_pt, cost_g);\n"
                      "    imageStore(FLOW_S_AB_CACHE2, coord, vec4(off_c / LUMA_A_S_pt, off_g / LUMA_A_S_pt));\n"))
    for cache in ("FLOW_S_AB_CACHE2", "FLOW_S_BA_CACHE2"):
        a = f"    vec2 base_off3 = imageLoad({cache}, scoord).xy * 2.0 * LUMA_A_E_pt;\n"
        once(a)
        t = t.replace(a, a + f"    vec2 base_off4 = imageLoad({cache}, scoord).zw * 2.0 * LUMA_A_E_pt;\n")
    def add_g(m):
        fn, uv = m.group(1), m.group(2)
        return (m.group(0) + f"    float sad_g;\n    vec2 ref_g = {fn}({uv}, base_off4, sad_g);\n"
                "    float score_g = sad_g + SEED_MAG_LAMBDA * length(ref_g / LUMA_A_E_pt) + tl * length((ref_g - prev_e) / LUMA_A_E_pt);\n")
    t, k = re.subn(r"    vec2 ref_c = (refine_\w+)\((uv_\w+), base_off3, sad_c\);\n(?:.*\n)*?    float score_c = trusted \? sad_c .*\n", add_g, t)
    assert k == 2, f"global seed: the 1/8 level's temporal candidate appears {k} times, expected 2"
    a = ("    if (score_c < best_score * (1.0 - TIE_MARGIN)) { best_off = ref_c; best_score = score_c; }\n"
         "    float best_sad = (best_off == ref_a) ? sad_a : (best_off == ref_b) ? sad_b : sad_c;\n")
    assert t.count(a) == 2, "global seed: the 1/8 level's choice"
    t = t.replace(a, ("    if (score_c < best_score * (1.0 - TIE_MARGIN)) { best_off = ref_c; best_score = score_c; }\n"
                      "    if (score_g < best_score * (1.0 - TIE_MARGIN)) { best_off = ref_g; best_score = score_g; }\n"
                      "    float best_sad = (best_off == ref_a) ? sad_a : (best_off == ref_b) ? sad_b : (best_off == ref_c) ? sad_c : sad_g;\n"))
    # the 1/8 level's prior, measured from the frame's own shift
    for save in ("FLOW_E_AB_RAW", "FLOW_E_BA_RAW"):
        a = f"//!SAVE {save}\n"
        once(a)
        t = t.replace(a, f"//!BIND GLOBAL_SHIFT\n{a}")
    i = t.index("//!SAVE FLOW_E_AB_RAW"); j = t.index("//!SAVE FLOW_E_BA_RAW"); k2 = t.index("//!SAVE FLOW_E_AB\n", j)
    ab, ba = t[i:j], t[j:k2]
    assert ab.count("SEED_MAG_LAMBDA * length(ref_") == 5 and ba.count("SEED_MAG_LAMBDA * length(ref_") == 5, "global seed: the prior terms"
    ab = re.sub(r"SEED_MAG_LAMBDA \* length\(ref_(\w) / LUMA_A_E_pt\)", r"SEED_MAG_LAMBDA * length((ref_\1 - g_e) / LUMA_A_E_pt)", ab)
    ba = re.sub(r"SEED_MAG_LAMBDA \* length\(ref_(\w) / LUMA_A_E_pt\)", r"SEED_MAG_LAMBDA * length((ref_\1 + g_e) / LUMA_A_E_pt)", ba)
    a = "    vec2 base_off = seeds.xy * 2.0 * LUMA_A_E_pt;\n"
    assert ab.count(a) == 1 and ba.count(a) == 1, "global seed: the seeds line"
    ab = ab.replace(a, a + "    vec2 g_e = GLOBAL_SHIFT_tex(vec2(0.5)).xy * 2.0 * LUMA_A_E_pt;   // the frame's own shift: the small-motion prior is measured from it, not from zero\n")
    ba = ba.replace(a, a + "    vec2 g_e = GLOBAL_SHIFT_tex(vec2(0.5)).xy * 2.0 * LUMA_A_E_pt;\n")
    return t[:i] + ab + ba + t[k2:]

BANNER = """// =====================================================================
// GENERATED FILE -- DO NOT EDIT BY HAND.
//
// Produced by scripts/tests/gen_variational.py from
// bidirectional-interpolation.glsl. To change the variational stage, edit the
// generator and regenerate. Hand edits will be lost, and the ~100
// near-identical iteration passes are not maintainable by hand anyway.
//
//   {env}./gen_variational.py "{spec}" {alpha} {sigma} <output.glsl> {sigma_flow_doc} "{medspec_doc}"
//
// Variational iterations per pyramid level: S={s} E={e} Q={q} H={h}
// (S = 1/16 resolution, E = 1/8, Q = 1/4, H = 1/2). Roughly {cost:.1f}
// full-resolution pass-equivalents of added work.
//
// Vector-median passes per level: S={ms} E={me} Q={mq} H={mh}, on top of the
// two the base shader already runs at H. A median texel costs far more than a
// variational one (81 length() calls against a fixed handful), so judge these
// by measured render time, not by the pass-equivalent figure above.
// =====================================================================

"""


# --- occlusion fallback: intentionally absent -----------------------------
# The base shader has no occlusion fallback. Three versions of one were built
# and each measured worse than none: a hard mix_t switch (8.75x periodic jump),
# a continuous blend of two unwarped frames (translucent doubled contour at
# every moving edge), and directional per-side weighting (better, still worse
# than removing it). Confirmed by direct viewing on a clip cut around the
# artifact. See the base shader's warp pass for the full account.
#
# Nothing to patch here as a result. This guard exists so that if a fallback
# is ever reintroduced upstream, generated builds fail loudly rather than
# silently inheriting a gate that was never measured for them.
FALLBACK_MARKER = "float occluded ="


def check_no_fallback(text):
    if FALLBACK_MARKER in text:
        raise SystemExit(
            "base shader has an occlusion fallback again -- generated builds "
            "need their own gate measured, not inherited. See TESTING.md.")
    return text


def build(iters, alpha, sigma, sigma_flow=0.0, medians=None):
    """iters:   dict level-key -> variational iteration count
       medians: dict level-key -> vector-median passes at that level"""
    medians = medians or {}
    t = READING.strip_tail(open(SRC).read())   # the base's own tail is not carried; this shader gets its own
    for lvl, flow, la, lb, div, anchor in LEVELS:
        n = iters.get(lvl, 0)
        m = medians.get(lvl, 0)
        if n == 0 and m == 0:
            continue
        if anchor not in t:
            sys.exit(f"anchor for level {lvl} not found")
        blocks = []
        if n:
            blocks.append(HEADER.format(lvl=lvl, div=div, n=n, reach=n * div))
        for direction, f, ref, tgt in ((("A->B", flow + "_AB", la, lb),
                                        ("B->A", flow + "_BA", lb, la))
                                       if n else ()):
            for i in range(n):
                blocks.append(PASS.format(
                    FLOW=f, LREF=ref, LTGT=tgt, DIV=div, LVL=lvl,
                    DIR=direction, I=i + 1, ALPHA=alpha, SIGMA=sigma,
                    SIGMAFLOWDECL=(
                        "\n// Robust term: a neighbour whose flow already disagrees"
                        "\n// strongly contributes little, so a fast object is not"
                        "\n// dragged toward slower surroundings. In this level's"
                        "\n// texels, so it scales with the pyramid.\n"
                        f"const float VAR_SIGMA_FLOW = {sigma_flow};"
                        if float(sigma_flow) > 0 else ""),
                    FLOWTERM=(
                        "            vec2 dfv = nf - f0;\n"
                        "            w *= exp(-dot(dfv, dfv) /"
                        " (2.0 * VAR_SIGMA_FLOW * VAR_SIGMA_FLOW));\n"
                        if float(sigma_flow) > 0 else "")))
        if m:
            blocks.append(MEDIAN_HEADER.format(lvl=lvl, div=div, n=m))
            for direction, f in (("A->B", flow + "_AB"),
                                 ("B->A", flow + "_BA")):
                for i in range(m):
                    blocks.append(MEDIAN.format(
                        FLOW=f, DIV=div, LVL=lvl, DIR=direction, I=i + 1))
        t = t.replace(anchor, "".join(blocks) + "\n" + anchor, 1)
    return check_no_fallback(t)


if __name__ == "__main__":
    spec = sys.argv[1] if len(sys.argv) > 1 else "16,12,8,6"
    alpha = sys.argv[2] if len(sys.argv) > 2 else "0.3"
    sigma = sys.argv[3] if len(sys.argv) > 3 else "0.08"
    # Defaults to a scratch file rather than the shipped shader: regenerating
    # production should be a deliberate act with the path spelled out.
    out = str(shader_arg(sys.argv[4])) if len(sys.argv) > 4 else str(
        pathlib.Path(tempfile.gettempdir()) / "casc.glsl")
    sigma_flow = sys.argv[5] if len(sys.argv) > 5 else "0"
    medspec = sys.argv[6] if len(sys.argv) > 6 else "2,2,2,0"
    # A seventh argument names the base (2026-09-06): the cascade rebuilt on the propagated base is a
    # variant of its own. A FUSED base saves its reverse coarse flow only in a storage image and its
    # reverse 1/8 flow only in the check pass twin, so on such a base iterate and take medians only from
    # the levels where both directions are saved textures: "0,0,8,4" with medians "0,0,2,0" on the
    # propagated base ("0,12,8,4" / "0,2,2,0" on the seeded one); check_binds finds a later-save bind
    # otherwise.
    if len(sys.argv) > 7:
        SRC = str(shader_arg(sys.argv[7]))
    # ZERO_SEED=1 in the environment switches the base's zero seed on in the output (both sites, asserted):
    # the variant on the propagated base ships with it on, its gate being a trade the base itself does not
    # take in place (NFRAME-LIMITS.md, "The owner's eyes", the gate).
    zero_seed = os.environ.get("ZERO_SEED", "0") == "1"
    s, e, q, h = (int(x) for x in spec.split(","))
    ms, me, mq, mh = (int(x) for x in medspec.split(","))
    text = build({"S": s, "E": e, "Q": q, "H": h}, alpha, sigma, sigma_flow,
                 {"S": ms, "E": me, "Q": mq, "H": mh})
    if zero_seed:
        n0 = text.count("const int ZERO_SEED = 0;"); n1 = text.count("const int ZERO_SEED = 1;")
        assert (n0, n1) in ((2, 0), (0, 2)), f"ZERO_SEED=1 asked but the base has {n0} sites off and {n1} on (a base without the seed code cannot take it)"
        text = text.replace("const int ZERO_SEED = 0;", "const int ZERO_SEED = 1;")
    if GLOBAL_SEED:
        text = add_global_seed(text)
    if QZERO_MOIRE:
        # QZERO_MOIRE_MIN (stage 0e, 2026-09-30): the Moire score that opens the zero descent; 0.25 unless overridden
        text = add_qzero_moire(text, moire_min=float(os.environ.get("QZERO_MOIRE_MIN", "0.25")))
    if COHERENCE_GATE:
        text = add_coherence_gate(text)
    if EDGE_PROP:
        text = add_edge_prop(text)
    if COARSE_ENERGY:
        text = add_coarse_energy(text)
    if ALIAS_PRIOR or ALIAS_CARRY:
        import alias_carry
        if ALIAS_PRIOR:
            assert GLOBAL_SEED, "ALIAS_PRIOR gates the global seed's prior: it needs GLOBAL_SEED=1"
            text = alias_carry.add_alias_prior(text)
        if ALIAS_CARRY:
            text = alias_carry.add_alias_carry(text, aperture=ALIAS_APERTURE)
    if OUTLINE_ADOPT:
        assert ALIAS_CARRY, "OUTLINE_ADOPT sits after the carry's pick: it needs ALIAS_CARRY=1"
        import outline_adopt
        text = outline_adopt.add_outline_adopt(text)
    if PRINT_LATTICE:
        assert ALIAS_CARRY, "PRINT_LATTICE reads the 1/8 basins and sits after the carry's pick: it needs ALIAS_CARRY=1"
        import print_lattice
        text = print_lattice.add_print_lattice(text)
    if TRUST_GATE:
        assert ALIAS_CARRY, "TRUST_GATE reads the 1/8 basins' margins and sits after the carry's pick: it needs ALIAS_CARRY=1"
        import trust_gate
        text = trust_gate.add_trust_gate(text)
    if CUT_MOTION:
        import cut_motion
        text = cut_motion.add_cut_motion(text, float(os.environ.get("CUT_EXPLAINED", cut_motion.CUT_EXPLAINED)))
    cost = 2 * (s / 256 + e / 64 + q / 16 + h / 4)
    env = ("GLOBAL_SEED=1 " if GLOBAL_SEED else "") + ("QZERO_MOIRE=1 " if QZERO_MOIRE else "") + ("COHERENCE_GATE=1 " if COHERENCE_GATE else "") \
        + (f"EDGE_PROP=1 EDGE_PROP_TAU={EDGE_PROP_TAU:g} " if EDGE_PROP else "") \
        + (f"COARSE_ENERGY=1 COARSE_ENERGY_WS={COARSE_ENERGY_WS:g} COARSE_ENERGY_WE={COARSE_ENERGY_WE:g} " if COARSE_ENERGY else "") \
        + ("ALIAS_PRIOR=1 " if ALIAS_PRIOR else "") + ("ALIAS_CARRY=1 " if ALIAS_CARRY else "") \
        + ("OUTLINE_ADOPT=1 " if OUTLINE_ADOPT else "") \
        + ("PRINT_LATTICE=1 " if PRINT_LATTICE else "") \
        + ("TRUST_GATE=1 " if TRUST_GATE else "") \
        + ("CUT_MOTION=1 " if CUT_MOTION else "") \
        + ("ALIAS_APERTURE=0 " if ALIAS_CARRY and not ALIAS_APERTURE else "")     # the zero seed is the recommendation's standing state and the line never named it
    text = BANNER.format(env=env, spec=spec, alpha=alpha, sigma=sigma,
                         s=s, e=e, q=q, h=h, cost=cost,
                         ms=ms, me=me, mq=mq, mh=mh,
                         sigma_flow_doc=sigma_flow, medspec_doc=medspec) + text
    ok = text.count("{") == text.count("}") and text.count("(") == text.count(")")
    text = READING.add_tail(text)   # the human-reading tail every shipped shader carries (off by default)
    open(out, "w", newline="\n").write(text)
    print(f"{out}: S={s} E={e} Q={q} H={h} med={medspec}  "
          f"HOOK={text.count('//!HOOK')} "
          f"lines={text.count(chr(10))} braces {text.count('{')}/{text.count('}')} "
          f"parens {text.count('(')}/{text.count(')')} "
          f"~{cost:.1f} full-res pass-equiv  {'OK' if ok else 'UNBALANCED'}")
