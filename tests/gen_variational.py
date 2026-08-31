#!/usr/bin/env python3
"""Generate a MULTI-LEVEL variational build: iterate at every pyramid level.

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
import pathlib
import sys
import tempfile

# Resolved from this file's own location, not hardcoded. The previous absolute
# path was both machine-specific and WSL-only (/mnt/c/...), so the generator
# ran on exactly one host -- which the cross-platform smoke test caught the
# moment it was run under MSYS2.
HERE = pathlib.Path(__file__).resolve().parent
SRC = str(HERE.parent / "bidirectional-interpolation.glsl")

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


BANNER = """// =====================================================================
// GENERATED FILE -- DO NOT EDIT BY HAND.
//
// Produced by scripts/tests/gen_variational.py from
// bidirectional-interpolation.glsl. To change the variational stage, edit the
// generator and regenerate. Hand edits will be lost, and the ~100
// near-identical iteration passes are not maintainable by hand anyway.
//
//   ./gen_variational.py "{spec}" {alpha} {sigma} <output.glsl> {sigma_flow_doc} "{medspec_doc}"
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
    t = open(SRC).read()
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
    out = sys.argv[4] if len(sys.argv) > 4 else str(
        pathlib.Path(tempfile.gettempdir()) / "casc.glsl")
    sigma_flow = sys.argv[5] if len(sys.argv) > 5 else "0"
    medspec = sys.argv[6] if len(sys.argv) > 6 else "2,2,2,0"
    s, e, q, h = (int(x) for x in spec.split(","))
    ms, me, mq, mh = (int(x) for x in medspec.split(","))
    text = build({"S": s, "E": e, "Q": q, "H": h}, alpha, sigma, sigma_flow,
                 {"S": ms, "E": me, "Q": mq, "H": mh})
    cost = 2 * (s / 256 + e / 64 + q / 16 + h / 4)
    text = BANNER.format(spec=spec, alpha=alpha, sigma=sigma,
                         s=s, e=e, q=q, h=h, cost=cost,
                         ms=ms, me=me, mq=mq, mh=mh,
                         sigma_flow_doc=sigma_flow, medspec_doc=medspec) + text
    open(out, "w", newline="\n").write(text)
    ok = text.count("{") == text.count("}") and text.count("(") == text.count(")")
    print(f"{out}: S={s} E={e} Q={q} H={h} med={medspec}  "
          f"HOOK={text.count('//!HOOK')} "
          f"lines={text.count(chr(10))} braces {text.count('{')}/{text.count('}')} "
          f"parens {text.count('(')}/{text.count(')')} "
          f"~{cost:.1f} full-res pass-equiv  {'OK' if ok else 'UNBALANCED'}")
