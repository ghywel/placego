#!/usr/bin/env python3
"""Rescale a shader of this family for a larger frame: the RESOLUTION half of the scale-aware generator.

    ./scale_shader.py <in.glsl> <out.glsl> <factors>
        <factors> is one power of two for every level, or four of them for S,E,Q,H:
          2         every level doubled: the shader's exact behaviour as a fraction of the screen (use this)
          2,2,2,1   the three coarse levels doubled, the finest kept -- measured no better on the textured
                    cases and a little worse on reach (SHADERS.md, "the 4K shader"); kept for the record

WHY. Every rule in the tracker is in pixels and frames: the coarse level is 1/16 of the frame, the search
reaches about 23 px per frame, the block matcher's windows are 5x5 texels of their level, and the
thresholds were tuned on a 1280x720 ladder and 1080p footage. Feed the same scene at twice the pixel
count and every motion is twice as many pixels while the reach, the windows and the thresholds stay
where they were: the reach halves as a fraction of the screen, the coarse level sees half the context,
and the picture comes out differently (NFRAME-LIMITS.md section 9; WHAT-WE-BUILT.md, the scaling
paragraph). The 4K rendering of the rotating disc is where this was seen.

WHAT IT DOES. Multiplies each pyramid level's divisor by its factor -- `//!WIDTH HOOKED.w 16 /` becomes
`32 /` for a factor of 2 -- so that level of a larger frame has the texel count the shader was tuned on.
Everything expressed in a level's own texels is then unchanged by construction: the search radius, the
matching windows, the regularisation, the cost margins, the propagation reach, the medians. What changes
is every ratio between two things whose factors differ:
  - the hand-off from one level to the next, `FLOW_<coarser>_... * 2.0 * LUMA_x_<finer>_pt`, becomes 2.0
    times the ratio of the two factors (texture reads and the fused caches' image loads alike);
  - the hand-off from the half-resolution level to the full-resolution flow level of the field shaders,
    `* 2.0 * LUMA_x_F_pt`, becomes 2.0 times the half-resolution factor (the full-resolution level is
    the frame and does not scale);
  - the conversion of half-resolution flow to the frame's pixels, `* 2.0 * HOOKED_pt` (the warp, and
    the reading tail's own copy of the final pass), likewise;
  - every constant in the frame's pixels -- the acceleration and jerk caps, the diagnostic and
    machine-read full scales -- is multiplied by the frame's factor, so the shader's judgement is the
    same fraction of the screen and a painted field is comparable with the original's; a machine reader
    decodes a scaled shader's field at the scaled full scale, and the field is in the frame's own pixels.
The full-resolution flow level's reads (`FLOW_F_... * HOOKED_pt`, one texel per pixel) are correct as
they are and are left alone; so are the two full-resolution edge masks' one-pixel neighbourhoods (an edge
is an edge at any size). A ratio of four at one hand-off is safe where the coarser level carries a
sub-texel fit (Q -> H) and NOT at E -> Q (the E flow is integer texels, and half an E texel is the whole
Q search radius), so factors may only differ between Q and H. The tool counts every hand-off in the file
against what it classified and refuses a shader with a pixel use it does not know.

The storage caches are declared at literal sizes (README.md, "Costs and limitations") chosen for 4K at
the original divisors, so a scaled shader at 4K still fits them. The output is a generated file:
regenerate it after the source shader changes (`tests/smoke.sh` step 3b does, for the variational).
"""
import datetime
import pathlib
import re
import sys

src = pathlib.Path(sys.argv[1])
dst = pathlib.Path(sys.argv[2])
spec = sys.argv[3]
LEVELS = ("S", "E", "Q", "H")
DIV = {16: "S", 8: "E", 4: "Q", 2: "H"}
fs = [int(x) for x in spec.split(",")]
if len(fs) == 1:
    fs = fs * 4
assert len(fs) == 4, "one factor, or four for S,E,Q,H"
for f in fs:
    assert f >= 1 and (f & (f - 1)) == 0, "factors must be powers of two"
F = dict(zip(LEVELS, fs))
F["F"] = 1                      # the full-resolution flow level is the frame
assert F["S"] == F["E"] == F["Q"], "S, E and Q must share a factor (the E -> Q hand-off cannot widen)"
assert F["Q"] >= F["H"], "the finest level's factor cannot exceed the others'"
assert any(f > 1 for f in fs), "nothing to scale"
FRAME = F["S"]                  # how much larger the frame is than the one the shader was tuned on
t = src.read_text(encoding="utf-8")
report = []

# 1. the pyramid divisors (the reading tail's 1/8-res passes are sized the same way and scale the same way)
n_div = {}
def div(m):
    n = int(m.group(2)); lv = DIV[n]
    n_div[lv] = n_div.get(lv, 0) + 1
    return "%s%d /" % (m.group(1), n * F[lv])
t = re.sub(r"^(//!(?:WIDTH|HEIGHT) HOOKED\.[wh] )(16|8|4|2) /$", div, t, flags=re.M)
assert set(n_div) == set(LEVELS), "levels found: %s" % sorted(n_div)
report.append("divisors " + " ".join("%s:%d" % (lv, n_div[lv]) for lv in LEVELS))
# ... and the outline adoption's coarse grid (OUTLINE_ADOPT, tests/outline_adopt.py): a cell is 8 quarter texels, sized
# `HOOKED.w 31 + 32 /` (a ceiling), so it takes Q's factor; left alone it would be correct but four times too large
n_grid = [0]
def grid(m):
    n_grid[0] += 1; c = 32 * F["Q"]
    return "%s%d + %d /" % (m.group(1), c - 1, c)
t = re.sub(r"^(//!(?:WIDTH|HEIGHT) HOOKED\.[wh] )31 \+ 32 /", grid, t, flags=re.M)
if n_grid[0]:
    report.append("adopt grid %d -> %d px" % (n_grid[0], 32 * F["Q"]))
# ... and PRINT_LATTICE's 1/8-level grids (tests/print_lattice.py): a fused pass is two halves of N cells' slots each,
# `HOOKED.w 8 / N * 2 *`, so its divisor takes E's factor like the level itself
n_pgrid = [0]
def pgrid(m):
    n_pgrid[0] += 1
    return "%s%d /%s" % (m.group(1), 8 * F["E"], m.group(2))
t = re.sub(r"^(//!WIDTH HOOKED\.w )8 /((?: \d+ \*)? 2 \*)$", pgrid, t, flags=re.M)
if n_pgrid[0]:
    report.append("print grids %d" % n_pgrid[0])

# 2. the hand-offs between levels: counted before rewriting, since a hand-off whose two factors are
#    equal still reads 2.0 afterwards
n_total = len(re.findall(r"\* 2\.0 \* LUMA_[A-E]_[EQHF]_pt", t))
n_hand = {}
for coarse, fine in (("S", "E"), ("E", "Q"), ("Q", "H"), ("H", "F")):
    ratio = 2.0 * F[coarse] / F[fine]
    # a hand-off reads the coarser flow on the same line, or -- the seeded lineage's 1/8 refine -- from
    # the `seeds` it loaded from the coarse level on the line before
    src_forms = r"FLOW_%s_[A-E]{2}\w*(?:_tex\(|, )[^;]*?" % coarse
    if coarse == "S":
        for b in t.split("//!HOOK FRAME_MIX"):
            if "seeds.xy * 2.0 * LUMA_" in b:
                assert re.search(r"vec4 seeds = (?:imageLoad\()?FLOW_S_", b), "a pass converts `seeds` it did not load from the coarse level"
        # the global-motion seed (2026-09-20): the frame's shift, found at the coarse level, handed to the
        # 1/8 level's prior -- a coarse-to-1/8 hand-off like any other
        src_forms = r"(?:%s|seeds\.(?:xy|zw)|GLOBAL_SHIFT_tex\(vec2\(0\.5\)\)\.xy)" % src_forms
    pat = re.compile(r"(%s) \* 2\.0 \* (LUMA_[A-E]_%s_pt)" % (src_forms, fine))
    t, n = pat.subn(lambda m: "%s * %.1f * %s" % (m.group(1), ratio, m.group(2)), t)
    n_hand[coarse + fine] = n
    if fine != "F":
        assert n >= 2, "hand-off %s -> %s: found %d (expected one per direction at least)" % (coarse, fine, n)
assert sum(n_hand.values()) == n_total, ("hand-offs in the file: %d, classified: %d" % (n_total, sum(n_hand.values())))
report.append("hand-offs " + " ".join("%s:%d" % kv for kv in n_hand.items() if kv[1]))

# 3. half-resolution flow to the frame's pixels, wherever it is read that way (the warp; the reading
#    tail's copy of the final pass): every such line must be reading a half-resolution flow
conv = "* %.1f * HOOKED_pt" % (2.0 * F["H"])
n_warp = 0
lines = t.split("\n")
for i, l in enumerate(lines):
    if "* 2.0 * HOOKED_pt" in l and not l.strip().startswith("//"):
        assert "FLOW_H_" in l, "a '* 2.0 * HOOKED_pt' that is not a half-resolution flow read: " + l.strip()[:100]
        lines[i] = l.replace("* 2.0 * HOOKED_pt", conv); n_warp += l.count("* 2.0 * HOOKED_pt")
t = "\n".join(lines)
assert n_warp >= 1, "no half-resolution-to-frame conversion found"
report.append("H->frame %d -> %.1f" % (n_warp, 2.0 * F["H"]))

# 4. constants in the frame's pixels
n_px = []
def px(m):
    v = float(m.group(2)) * FRAME
    n_px.append("%s %s->%g" % (m.group(1), m.group(2), v))
    return "const float %s = %s;" % (m.group(1), ("%.1f" % v) if v == int(v) else repr(v))
t = re.sub(r"const float (\w+(?:_PX|_DIAG_FS|_MACHINE_FS_\w+)) = ([0-9.]+);", px, t)
report.append("px constants x%d: %s" % (FRAME, ", ".join(sorted(set(n_px))) or "none"))
# ... and regions measured in the frame's pixels (`24.0 * HOOKED_pt.x`: a corner swatch), likewise
n_reg = []
def reg(m):
    v = float(m.group(1)) * FRAME
    n_reg.append("%s->%g" % (m.group(1), v))
    return "%.1f * HOOKED_pt.%s" % (v, m.group(2))
t = re.sub(r"\b(\d+\.\d+) \* HOOKED_pt\.([xy])\b", reg, t)
if n_reg:
    report.append("px regions x%d: %s" % (FRAME, ", ".join(sorted(set(n_reg)))))
# ... and the texture-energy passes (COARSE_ENERGY, tests/coarse_energy.py), one per frame: each block's four taps sit
# 1 px from its centre and its gradient steps 2 px, both in the frame's pixels, so both scale with the frame (the pass
# itself is a 1/4-resolution level and took Q's factor in step 1). The second frame's pass reads NEXT_pt, which no
# other pass of the family uses -- step 5 checks it too, or a scaled A beside an unscaled B would bias every score.
n_en = 0
for fr in ("HOOKED", "NEXT"):
    tap = "(vec2(float(i), float(j)) * 2.0 - 1.0) * %s_pt;" % fr
    grad = "abs(lum_q(p + vec2(2.0, 0.0) * %s_pt) - c) + abs(lum_q(p + vec2(0.0, 2.0) * %s_pt) - c)" % (fr, fr)
    lum = "float lum_q(vec2 p) { return dot(%s_tex(p).rgb" % fr
    assert t.count(tap) == t.count(grad) == t.count(lum) <= 1, "an energy pass for %s not in its known form" % fr
    if t.count(tap):
        t = t.replace(tap, "(vec2(float(i), float(j)) * 2.0 - 1.0) * ENERGY_FRAME_PX * %s_pt;" % fr)
        t = t.replace(grad, "abs(lum_q(p + vec2(2.0, 0.0) * ENERGY_FRAME_PX * %s_pt) - c) + "
                            "abs(lum_q(p + vec2(0.0, 2.0) * ENERGY_FRAME_PX * %s_pt) - c)" % (fr, fr))
        t = t.replace(lum, "const float ENERGY_FRAME_PX = %.1f;   // (scale_shader) the frame's pixels per original pixel\n%s"
                      % (FRAME, lum))
        n_en += 1
assert n_en in (0, 2), "one frame's energy pass without the other's"
if n_en:
    report.append("energy taps x%d (both frames)" % FRAME)

# 4b. PRINT_LATTICE's luma samplers (tests/print_lattice.py): the passes work in TUNED pixels (8 per 1/8 cell, 4 per quarter
#     texel, which the factors keep), so only the reading of the frame scales: a tuned pixel p is the frame's
#     (p + 0.5) * FRAME, the corner of its FRAME x FRAME block, where bilinear averages the block
n_ps = len(re.findall(r"_tex\(\(p \+ 0\.5\) \* (?:HOOKED|NEXT)_pt\)", t))
assert n_ps in (0, 16, 20), "PRINT_LATTICE's samplers not in their known form: %d" % n_ps   # 20 with the cost cap's borrowing
t = re.sub(r"_tex\(\(p \+ 0\.5\) \* (HOOKED|NEXT)_pt\)", lambda m: "_tex(((p + 0.5) * %.1f) * %s_pt)" % (FRAME, m.group(1)), t)
if n_ps:
    report.append("print samplers %d x%d" % (n_ps, FRAME))
# ... and its cost cap's budget (opened cells per direction): the grid keeps its cell count, but a cell's samples lie
# FRAME times further apart and cost about FRAME times as much (cache locality; measured 2026-10-01 on the M5: the
# full-frame print pan at 4K runs in 19.7 ms with half the budget, 24.8 with the same), so the budget divides by FRAME
n_bud = [0]
def bud(m):
    n_bud[0] += 1
    return "/ %.1f, 1.0)" % (float(m.group(1)) / FRAME)
t = re.sub(r"/ (\d+\.\d), 1\.0\)", bud, t)
if n_bud[0]:
    report.append("print budget %d sites /%d" % (n_bud[0], FRAME))

# 5. nothing else may carry the frame's own scale. Every remaining HOOKED_pt use must be one the tool
#    knows to be right as it stands.
KNOWN = (
    re.compile(r"vec2 o = vec2\(float\(x\), float\(y\)\) \* HOOKED_pt;"),   # the edge masks' 1-px neighbourhood
    re.compile(r"FLOW_F_[A-E]{2}\w*_tex\([^;]*\)\.xy \* HOOKED_pt"),        # full-res flow, one texel per pixel
    re.compile(r"/ (?:length\()?HOOKED_pt\)?"),                              # pixels out of a full-res quantity
    re.compile(r"\w+_PX \* (?:HOOKED|NEXT)_pt"),                            # a scaled cap or tap in pixels
    re.compile(r"\d+\.\d+ \* HOOKED_pt\.[xy]\b"),                            # a scaled region in pixels
    re.compile(re.escape(conv)),
    re.compile(r"_tex\(\(\(p \+ 0\.5\) \* \d+\.\d\) \* (?:HOOKED|NEXT)_pt\)"),   # a scaled print sampler
)
other = [l.strip() for l in t.split("\n")
         if ("HOOKED_pt" in l or "NEXT_pt" in l) and not l.strip().startswith("//") and not any(k.search(l) for k in KNOWN)]
assert not other, ("unexpected HOOKED_pt / NEXT_pt use, decide how it scales: " + str(other[:3]))

# 6. the header
levels = ", ".join("%s x%d" % (lv, F[lv]) for lv in LEVELS)
head = """// =====================================================================
// GENERATED FILE -- DO NOT EDIT BY HAND.
//
// Produced by scripts/tests/scale_shader.py from %s
// with factors %s (%s), %s. It is that shader with each
// pyramid level's divisor multiplied by its factor, so that level of a
// frame %d times larger has the texel count the shader was tuned on;
// everything expressed in a level's own texels (the search reach, the
// matching windows, the thresholds, the propagation reach, the medians)
// is unchanged by construction. Hand-offs between levels whose factors
// differ carry the ratio, half-resolution flow converts to the frame
// with %.1f instead of 2.0, and every constant in the frame's pixels is
// %d times the original's -- so the field is in this frame's own pixels
// and a painted or machine-read field is comparable with the original's
// at %d times its full scale. Storage caches were sized for 4K at the
// original divisors, so this file is safe to %d times 4K. The comments
// below describe the pyramid in the original shader's terms ("1/16
// resolution" is 1/%d of this frame, and so on).
//
//   ./scale_shader.py %s %s %s
// =====================================================================

""" % (src.name, spec, levels, datetime.date.today().isoformat(), FRAME, 2.0 * F["H"], FRAME, FRAME,
       F["H"], 16 * F["S"], src.name, dst.name, spec)
dst.write_text(head + t, encoding="utf-8", newline="\n")
print("%s: %s; %d passes" % (dst.name, "; ".join(report), t.count("//!HOOK")))
