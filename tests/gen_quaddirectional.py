#!/usr/bin/env python3
"""Generate the QUADDIRECTIONAL interpolation shader from the bidirectional base.

    ./gen_quaddirectional.py [output.glsl [base.glsl]]    (default: ../shaders/quaddirectional-interpolation.glsl)

THE HYPOTHESIS THIS BUILDS -- and, unusually, what it is pre-registered NOT to
do. Three frames determine a quadratic: velocity and acceleration, with
acceleration forced constant across the window. Four frames determine a cubic
-- velocity, acceleration AND jerk -- or, spent differently, an overdetermined
quadratic whose residual is a per-texel measurement of its own trustworthiness.
Both arms exist in the record (PRIOR-ART.md: the exact cubic in All-at-Once,
ECCV 2020; the least-squares quadratic in EQVI, ECCV-W 2020) and this shader
builds both, switched by QUAD_MODE, because the fork is the experiment.

The pre-registration, from the stencil algebra (PLAN.md T3.1): at a symmetric
window the centred pair's acceleration is jerk-immune -- the cubic solve
returns the IDENTICAL anchor acceleration the tridirectional shader already
measures. So this shader is NOT expected to improve the N:N field's accuracy
on smooth content. Its gains are pre-registered elsewhere:

  1. the JERK FIELD itself -- the first thing in this project no 3-frame
     shader can measure at all, calibratable against the O-series' analytic
     jerk;
  2. the LSQ RESIDUAL as a per-texel measured confidence signal (QUAD_MODE 1)
     -- replacing heuristic trust with an actual consistency measurement;
  3. cubic PLACEMENT at 24->60, where the output sits off the window's centre
     of symmetry and jerk does not cancel out of the trajectory.

WHY GENERATED, NOT FORKED: same reasoning as gen_tridirectional.py, from which
this generator imports its machinery. The pipeline is the proven bidirectional
base plus two more luma pyramids, two more adjacent-pair flow chains, two more
cut statistics, and a final pass that fits one degree higher.

SLOT-KEYED, LIKE TRI -- the architecture that the role-keyed failure taught.
Slots 0..3 in ascending time; every cached field is a pure function of the
window (adjacent-pair flows F01,F10,F12,F21,F23,F32); only the final pass
knows about roles.

THE 4-FRAME WINDOW. Binding FRAME3 declares frame_mix_count = 4. From the
patch's selection logic the window is always a CONTIGUOUS run of four source
frames: {k-1, k, k+1, k+2} for an interior 24->60 output (straddle = slots
1,2 -- two frames each side, every phase), and {k-2, k-1, k, k+1} at exact
N:N (output ON slot 2). Unlike tri, the window does not re-centre as the
output crosses mid-interval, so the anchor is a per-output ROLE: the
straddling frame nearer the output, always slot 1 or slot 2 -- both interior,
both with a full flow set.

ADJACENT FLOWS ONLY, COMPOSED FOR REACH. The anchor needs displacements to
three other frames, one of which is two intervals away. That flow is NOT
searched directly -- a 2-interval search doubles the displacement and exits
the coarse search's ~23 px/frame reach exactly on the content that matters.
It is COMPOSED from the two adjacent links: F13(x) = F12(x) + F23(x + F12(x)),
the trajectory-linking construction (dense-trajectory literature, and the
same reason PIV links interrogation windows frame to frame). Each link is a
measured adjacent flow inside its own reach, each link is round-trip checked,
and the worst link gates the composition.

THE ALGEBRA. Anchor at time 0; taus of the other three frames in straddle-
interval units; displacement model

    d(tau) = v*tau + (a/2)*tau^2 + (j/6)*tau^3

Three flows, three unknowns: an exact 3x3 solve (QUAD_MODE 0). At uniform
spacing the acceleration row reduces to a = d(+1) + d(-1) -- tri's formula,
untouched by jerk, which is the pre-registration above. QUAD_MODE 1 instead
fits the quadratic by least squares over all three flows (EQVI's RQFP) and
reads the residual out as confidence.

Placement: the deviation of the cubic trajectory from the straddle chord.
With s in [0,1] across the straddle and the anchor at one end,

    corr = s*(1-s) * ( a/2 + (j/6)*(anchor==A ? (1+s) : -(2-s)) )

which reduces to tri's s*(1-s)*a/2 at j = 0 and to the bidirectional warp at
a = j = 0 -- the null-hypothesis ladder ctrl tests ride on.
"""
import pathlib
import re
import sys

import gen_tridirectional as T3
import add_human_reading as READING   # the human-reading tail every shipped shader carries (off by default)

HERE = pathlib.Path(__file__).resolve().parent
# The base to generate from. Default is the shipped bidirectional shader;
# a second positional argument names a VARIANT base (e.g. a two-descent
# bidirectional-interpolation-<variant>.glsl), so tri/quad variants can be
# generated beside the stock files without overwriting them.
SHADERS = HERE.parent / "shaders"


def shader_arg(s):
    """A bare file name means a shader in shaders/; a path with a directory is used as given."""
    p = pathlib.Path(s)
    return p if p.parent != pathlib.Path(".") else SHADERS / p


SRC = shader_arg(sys.argv[2]) if len(sys.argv) > 2 else \
    SHADERS / "bidirectional-interpolation.glsl"
DST = shader_arg(sys.argv[1]) if len(sys.argv) > 1 else \
    SHADERS / "quaddirectional-interpolation.glsl"

LEVELS = T3.LEVELS

FOUR_BINDS = ("//!BIND HOOKED\n//!BIND FRAME1\n"
              "//!BIND FRAME2\n//!BIND FRAME3")


def luma_block(slot_letter, slot_index, frame_tex, lvl):
    div = dict(S=16, E=8, Q=4, H=2)[lvl]
    return f"""

//!HOOK FRAME_MIX
{FOUR_BINDS}
//!SAVE LUMA_{slot_letter}_{lvl}
//!WIDTH HOOKED.w {div} /
//!HEIGHT HOOKED.h {div} /
//!COMPONENTS 1
//!DESC [quad] downsample slot {slot_index} to 1/{div} res (luma)
vec4 hook() {{
    return vec4(dot({frame_tex}_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}}"""


def cut_block(la, lb, save, pair):
    return f"""

//!HOOK FRAME_MIX
//!BIND LUMA_{la}_S
//!BIND LUMA_{lb}_S
//!SAVE {save}
//!WIDTH 1
//!HEIGHT 1
//!COMPONENTS 1
//!DESC [quad] scene-cut statistic, slots {pair}
vec4 hook() {{
    const int N = 24;
    float acc = 0.0;
    for (int y = 0; y < N; y++) {{
        for (int x = 0; x < N; x++) {{
            vec2 uv = (vec2(float(x), float(y)) + 0.5) / float(N);
            acc += abs(LUMA_{la}_S_tex(uv).r - LUMA_{lb}_S_tex(uv).r);
        }}
    }}
    return vec4(acc / float(N * N), 0.0, 0.0, 0.0);
}}"""


def shift_pair(b, lvl, la, lb, tag, desc_pair):
    """Rewrite a base slot0<->slot1 flow pass onto the luma pair (la, lb).

    Generalises gen_tridirectional.shift_slot: (B, C) reproduces the tri
    chains exactly; (C, D) produces the slot2<->slot3 chains. LUMA_B must be
    rewritten before LUMA_A or the first substitution's output is eaten by
    the second. LUMA_A's bind always STAYS -- the pass body uses its _pt/_pos
    geometry identifiers, and removing the bind is the silent-fallback trap
    the tri generator documents.
    """
    nb = b
    nb = re.sub(rf"\bLUMA_B_{lvl}_tex\(", "__LB__(", nb)
    nb = re.sub(rf"\bLUMA_A_{lvl}_tex\(", "__LA__(", nb)
    nb = nb.replace("__LB__(", f"LUMA_{lb}_{lvl}_tex(")
    nb = nb.replace("__LA__(", f"LUMA_{la}_{lvl}_tex(")
    extra = "".join(f"\n//!BIND LUMA_{x}_{lvl}" for x in (la, lb)
                    if x not in ("A", "B"))
    nb = nb.replace(f"//!BIND LUMA_B_{lvl}", f"//!BIND LUMA_B_{lvl}{extra}")
    # Same-direction flow references take the pair tag; a CROSS-direction
    # reference (the reverse flow, used for a round-trip check) takes the
    # reversed tag. The block's own direction is read from its //!SAVE line.
    own = "BA" if re.search(r"^//!SAVE FLOW_[SEQH]_BA", nb, re.M) else "AB"
    other = "BA" if own == "AB" else "AB"
    nb = re.sub(rf"FLOW_([SEQH])_{other}", rf"FLOW_\1_{tag[::-1]}", nb)
    nb = re.sub(rf"FLOW_([SEQH])_{own}", rf"FLOW_\1_{tag}", nb)
    a, b_ = desc_pair
    nb = nb.replace("flow search A->B", f"flow search slot{a}->slot{b_}")
    nb = nb.replace("flow search B->A", f"flow search slot{b_}->slot{a}")
    nb = nb.replace("flow A->B", f"flow slot{a}->slot{b_}")
    nb = nb.replace("flow B->A", f"flow slot{b_}->slot{a}")
    nb = nb.replace("[high]", "[quad]")
    nb = nb.replace("[tri]", "[quad]")
    return nb


def chain(find, la, lb, tag, rev, banner):
    """One full flow chain (coarse + 3 refines + 2 medians) for a slot pair."""
    parts = [banner]
    src = "BA" if rev else "AB"
    for lvl, _ in LEVELS:
        if lvl == "H":
            lvl_blocks = [find(f"FLOW_H_{src}", "refine")]
        else:
            lvl_blocks = find.all(f"FLOW_{lvl}_{src}")
        for b in lvl_blocks:
            parts.append(shift_pair(b, lvl, la, lb, tag,
                                    desc_pair=BANNER_PAIRS[tag]))
    for pn in ("pass 1", "pass 2"):
        b = find(f"FLOW_H_{src}", pn)
        parts.append(shift_pair(b, "H", la, lb, tag,
                                desc_pair=BANNER_PAIRS[tag]))
    return "\n\n".join(parts)


BANNER_PAIRS = {"BC": (1, 2), "CB": (1, 2), "CD": (2, 3), "DC": (2, 3)}

BANNERS = {
    "BC": """\
// =====================================================================
// SLOT 1 -> SLOT 2 flow chain ([quad], generated). The base's slot-0 ->
// slot-1 chain with the luma pair shifted along by one -- identical to the
// tridirectional shader's chain, because it IS the same field.
// =====================================================================""",
    "CB": """\
// =====================================================================
// SLOT 2 -> SLOT 1 flow chain ([quad], generated). Reverse of the above,
// for round-trip validation of the slot-1 anchor's forward flow and of
// slot 2's backward flow.
// =====================================================================""",
    "CD": """\
// =====================================================================
// SLOT 2 -> SLOT 3 flow chain ([quad], generated). The pair the fourth
// frame adds. Also the second LINK of the composed two-interval flow
// F13(x) = F12(x) + F23(x + F12(x)) -- composition keeps every search
// inside its own one-interval reach, which a direct two-interval search
// would exit exactly on fast content.
// =====================================================================""",
    "DC": """\
// =====================================================================
// SLOT 3 -> SLOT 2 flow chain ([quad], generated). Reverse of the above,
// closing the round trip on the composed flow's second link. An unchecked
// link is indistinguishable from real jerk, which is the same lesson the
// tri shader learned about unchecked flows and acceleration.
// =====================================================================""",
}


def main():
    text = READING.strip_tail(SRC.read_text())   # the base's own tail is not carried; this shader gets its own
    assert "TIE_MARGIN" in text, "base shader lacks TIE_MARGIN -- wrong vintage?"

    first = text.index("//!")
    text = text[first:]

    # Sub-pixel refinement on: this is a field shader (see gen_tridirectional).
    n_sub = text.count("const int SUBPEL_REFINE = 0;")
    assert n_sub == 2, f"expected 2 SUBPEL_REFINE sites in base, found {n_sub}"
    text = text.replace("const int SUBPEL_REFINE = 0;",
                        "const int SUBPEL_REFINE = 1;")
    # the self-referenced fit rides with the refinement: on in every field shader, off in the picture bases
    n_self = text.count("const int SUBPEL_SELFREF = 0;")
    assert n_self == 2, f"expected 2 SUBPEL_SELFREF sites in base, found {n_self}"
    text = text.replace("const int SUBPEL_SELFREF = 0;", "const int SUBPEL_SELFREF = 1;")

    blocks = T3.chunk(text)
    hook_blocks = [b for b in blocks if "//!HOOK" in b]
    # A variant base may carry EXTRA passes inside a level's flow chain (see
    # gen_tridirectional.py); they are carried into every pair's chain.
    extra = len(hook_blocks) - 24
    assert extra >= 0 and extra % 2 == 0, f"expected 24 base passes (+ an even number of extras), found {len(hook_blocks)}"

    def find(save, desc_frag=None):
        cands = [b for b in blocks if T3.block_id(b)[0] == save and
                 (desc_frag is None or desc_frag in (T3.block_id(b)[1] or ""))]
        assert len(cands) == 1, f"lookup {save}/{desc_frag}: {len(cands)} matches"
        return cands[0]

    def find_all(save):
        """Every block of a level's flow chain, in file order: the pass saving
        `save` itself plus any saving `save_<suffix>` (a variant's extra passes)."""
        cands = [b for b in blocks if T3.block_id(b)[0] == save or
                 (T3.block_id(b)[0] or "").startswith(save + "_")]
        assert cands, f"lookup {save}*: no matches"
        return cands
    find.all = find_all   # carried alongside find so chain() needs no new argument

    out = []
    for b in blocks:
        save, desc = T3.block_id(b)
        nb = b

        if save and re.fullmatch(r"LUMA_A_[SEQH]", save):
            nb = nb.replace("//!BIND HOOKED", FOUR_BINDS)
            nb = nb.replace("[high] downsample frame A", "[quad] downsample slot 0")

        elif save and re.fullmatch(r"LUMA_B_[SEQH]", save):
            lvl = save[-1]
            nb = nb.replace("//!BIND NEXT", FOUR_BINDS)
            nb = nb.replace("NEXT_tex(NEXT_pos)", "FRAME1_tex(HOOKED_pos)")
            nb = nb.replace("[high] downsample frame B", "[quad] downsample slot 1")
            nb += luma_block("C", 2, "FRAME2", lvl)
            nb += luma_block("D", 3, "FRAME3", lvl)

        elif save == "SCENE_DIFF":
            nb = nb.replace("[high] scene-cut statistic (whole-frame luma difference)",
                            "[quad] scene-cut statistic, slots 0-1")
            nb += cut_block("B", "C", "SCENE_DIFF_BC", "1-2")
            nb += cut_block("C", "D", "SCENE_DIFF_CD", "2-3")

        elif save in ("EDGE_A", "EDGE_B"):
            nb = nb.replace("//!BIND HOOKED\n//!BIND NEXT", FOUR_BINDS)
            nb = re.sub(r"\bNEXT_tex\(", "FRAME1_tex(", nb)
            nb = nb.replace("NEXT_pos", "HOOKED_pos")

        elif save == "FRAME_MIX":
            nb = FINAL_PASS

        out.append(nb)

        if save == "FLOW_H_BA" and desc and "pass 2" in desc:
            out.append(chain(find, "B", "C", "BC", rev=False, banner=BANNERS["BC"]))
            out.append(chain(find, "B", "C", "CB", rev=True, banner=BANNERS["CB"]))
            out.append(chain(find, "C", "D", "CD", rev=False, banner=BANNERS["CD"]))
            out.append(chain(find, "C", "D", "DC", rev=True, banner=BANNERS["DC"]))
            # Full-res level (see gen_tridirectional.to_fullres): lumas for
            # all four slots, then one F pass per pair per direction, each
            # seeded from that pair's post-median H flow emitted above.
            out.append(T3.fullres_luma("A", 0, "HOOKED", FOUR_BINDS, "quad"))
            out.append(T3.fullres_luma("B", 1, "FRAME1", FOUR_BINDS, "quad"))
            out.append(T3.fullres_luma("C", 2, "FRAME2", FOUR_BINDS, "quad"))
            out.append(T3.fullres_luma("D", 3, "FRAME3", FOUR_BINDS, "quad"))
            h_ab = find("FLOW_H_AB", "refine")
            h_ba = find("FLOW_H_BA", "refine")
            out.append(T3.to_fullres(h_ab, "AB", "quad"))
            out.append(T3.to_fullres(h_ba, "BA", "quad"))
            out.append(T3.to_fullres(
                shift_pair(h_ab, "H", "B", "C", "BC", BANNER_PAIRS["BC"]), "BC", "quad"))
            out.append(T3.to_fullres(
                shift_pair(h_ba, "H", "B", "C", "CB", BANNER_PAIRS["CB"]), "CB", "quad"))
            out.append(T3.to_fullres(
                shift_pair(h_ab, "H", "C", "D", "CD", BANNER_PAIRS["CD"]), "CD", "quad"))
            out.append(T3.to_fullres(
                shift_pair(h_ba, "H", "C", "D", "DC", BANNER_PAIRS["DC"]), "DC", "quad"))

    result = "\n".join(out)

    code = "\n".join(l for l in result.split("\n")
                     if not l.lstrip().startswith("//"))
    for bad in ("BIND NEXT", "NEXT_tex(", "NEXT_pos", "NEXT_size", "NEXT_pt"):
        assert bad not in code, f"residual 2-frame reference in code: {bad}"
    assert not re.search(r"\bmix_t\b", code), \
        "mix_t survived in code -- it is only valid for num_mix == 2"
    hooks = result.count("//!HOOK")
    braces = result.count("{") - result.count("}")
    parens = result.count("(") - result.count(")")
    assert hooks == 68 + 3 * extra, f"expected {68 + 3 * extra} passes, got {hooks}"
    assert braces == 0 and parens == 0, f"unbalanced: braces {braces}, parens {parens}"
    header = HEADER
    if SRC.name != "bidirectional-interpolation.glsl":
        header = header.replace("bidirectional-interpolation.glsl", SRC.name)
        header = header.replace("//   ./tests/gen_quaddirectional.py\n",
                                f"//   ./tests/gen_quaddirectional.py {DST.name} {SRC.name}\n")
    DST.write_text(READING.add_tail(header + result), newline="\n")
    print(f"  {DST.name}: {hooks} passes "
          f"({24 + extra} base + 8 slot-2/3 lumas + 2 cut stats + {24 + 2 * extra} pair flow "
          f"+ 4 full-res lumas + 6 full-res refines), braces/parens balanced  OK")


# ---------------------------------------------------------------------------
FINAL_PASS = """\
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
}"""

HEADER = """\
// =====================================================================
// GENERATED FILE -- DO NOT EDIT BY HAND.
//
// Produced by scripts/tests/gen_quaddirectional.py from
// bidirectional-interpolation.glsl. Edit the base (shared machinery) or
// the generator (everything [quad]-tagged) and regenerate:
//
//   ./tests/gen_quaddirectional.py
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

"""


if __name__ == "__main__":
    main()
