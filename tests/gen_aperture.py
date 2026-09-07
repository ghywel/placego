#!/usr/bin/env python3
"""Aperture-aware propagation: a variant of the propagated base whose first propagation pass votes by the
STRUCTURE TENSOR instead of scalar contrast.

    ./gen_aperture.py [output.glsl [base.glsl]]     (default: ../shaders/bidirectional-interpolation-propagated-aperture.glsl)

THE PROBLEM IT ADDRESSES (NFRAME-LIMITS.md, 2026-09-07, "the stairs' lensing"). On the film's stairs under a
horizontal pan the steps are horizontal lines, which cannot see horizontal motion; the propagated base's
contrast-weighted propagation lets every high-contrast cell vote for BOTH components of its flow, so the
steps vote their unconstrained horizontal component, borrowed from whatever the matcher's descent settled
on, and the picture warps blob by blob. The variational cascade's smoothness diffuses the constrained
components across, but only as far as 80 passes reach.

WHAT THIS DOES. After the 1/8 luma downsamples, one pass per frame computes each cell's structure tensor
over a 5x5 window (central-difference gradients, J = sum g g^T, normalised by its largest eigenvalue, so an
isotropic cell is the identity and a line is e e^T) beside the
existing contrast (TENS_A_E, TENS_B_E: Jxx, Jxy, Jyy, conf). The first propagation pass then solves, per
cell, the tensor-weighted least squares over a window of radius PROP_TENSOR_R:

    W = sum_i w_i J_i + w_own J_own + eps I,   b = sum_i w_i J_i f_i + w_own J_own f_own + eps f_own,   f = W^-1 b

so a neighbour on an edge contributes only the component of its flow across that edge, a textured neighbour
both, and a cell's own unconstrained component is filled from the nearest cells that constrain it, within
the window; eps keeps the own flow where nothing in the window constrains a component. Passes 2 and 3 and
the three-way data check are unchanged except that the check's disagreement test, which sends a flow its
neighbourhood contradicts to zero, measures the disagreement through the cell's own tensor, so a step's
borrowed horizontal component cannot veto its own fill. Everything is behind PROP_TENSOR (1 here, 0 = the
base's arithmetic, byte-identical in output). Cost: the tensor passes (cheap) and the wider first pass
((2R+1)^2 taps of two textures against the base's 24 x 25 luma reads).

The human-reading tail is re-applied last, as every generator does.

VERDICT (2026-09-07, the same afternoon): REFUTED, ships no shader. The 41-case gate on the first form
(trace-normalised tensors, the base's own weight) read -0.70 dB mean with 17 cases down (A5 -6.1, R3 -4.5,
L1 -3.5): trace normalisation halves an isotropic cell's projected disagreement and defeats the alias
rejection, and a radius-8 window swamps the own vote. The second form (largest-eigenvalue normalisation,
own weight scaled to the window; the code below) repairs those (A5 +0.9, M2/O6 flat) but still costs a
plain translation 1.9 dB and gains NOTHING on the aperture cases, because the base already fills the
aperture wherever a resolvable texture constrains it (P2 60 dB). Kept as the record of the design point;
NFRAME-LIMITS.md "The aperture series" has the tables.
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import add_human_reading as HR  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent / "shaders" / "bidirectional-interpolation-propagated-aperture.glsl"
BASE = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else HERE.parent / "shaders" / "bidirectional-interpolation-propagated.glsl"

import os
PROP_TENSOR = os.environ.get("PROP_TENSOR", "1")
PROP_TENSOR_R = os.environ.get("PROP_TENSOR_R", "8")
PROP_TENSOR_EPS = os.environ.get("PROP_TENSOR_EPS", "0.05")

text = HR.strip_tail(BASE.read_text(encoding="utf-8"))


def must_sub(pattern, repl, s, count, flags=0):
    s2, n = re.subn(pattern, repl, s, count=count, flags=flags)
    assert n == count, f"{pattern!r}: {n} substitutions, expected {count}"
    return s2


def must_replace(old, new, s, count=1):
    assert s.count(old) == count, f"{old[:60]!r}: found {s.count(old)}, expected {count}"
    return s.replace(old, new)


# 1. the tensor passes, after the 1/8 luma downsample of frame B
desc_b = "//!DESC [high] downsample frame B to 1/8 res (luma)"
i = text.index(desc_b)
j = text.index("\n}\n", i) + 3
tensor_pass = """
//!HOOK FRAME_MIX
//!BIND LUMA_{F}_E
//!SAVE TENS_{F}_E
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!DESC [aperture] structure tensor of the 1/8 luma of frame {F} over 5x5 (Jxx, Jxy, Jyy, largest eigenvalue 1) and the propagation's contrast

const float PROP_CONF_FULL_T = 0.08;

vec4 hook() {
    vec2 uv = LUMA_{F}_E_pos; vec2 pt = LUMA_{F}_E_pt;
    float jxx = 0.0, jxy = 0.0, jyy = 0.0, lo = 1.0, hi = 0.0;
    for (int y = -2; y <= 2; y++)
        for (int x = -2; x <= 2; x++) {
            vec2 o = vec2(float(x), float(y)) * pt;
            float l = LUMA_{F}_E_tex(uv + o).r;
            lo = min(lo, l); hi = max(hi, l);
            float gx = 0.5 * (LUMA_{F}_E_tex(uv + o + vec2(pt.x, 0.0)).r - LUMA_{F}_E_tex(uv + o - vec2(pt.x, 0.0)).r);
            float gy = 0.5 * (LUMA_{F}_E_tex(uv + o + vec2(0.0, pt.y)).r - LUMA_{F}_E_tex(uv + o - vec2(0.0, pt.y)).r);
            jxx += gx * gx; jxy += gx * gy; jyy += gy * gy;
        }
    // normalised by the LARGEST eigenvalue, not the trace: an isotropic cell is then the identity (it votes
    // both components in full and a disagreement projects through it whole), a line is e e^T
    float l1 = max(0.5 * (jxx + jyy + sqrt((jxx - jyy) * (jxx - jyy) + 4.0 * jxy * jxy)), 1.0e-8);
    return vec4(jxx / l1, jxy / l1, jyy / l1, clamp((hi - lo) / PROP_CONF_FULL_T, 0.0, 1.0));
}
"""
text = text[:j] + tensor_pass.replace("{F}", "A") + tensor_pass.replace("{F}", "B") + text[j:]

# 2. the first propagation pass: bind the tensors, add the tensor solve behind the switch
head1 = """//!BIND FLOW_E_BA_RAW
//!BIND FLOW_E_BA_PROP_ST1
//!SAVE FLOW_E_AB_PROP
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 2
//!DESC [prop12] contrast-weighted flow propagation AB (pass 1 of 3) [fused with its B->A twin: one dispatch]

const float PROP_SELF_WEIGHT = 8.0;
const float PROP_CONF_FULL   = 0.08;
"""
text = must_replace(head1, """//!BIND FLOW_E_BA_RAW
//!BIND FLOW_E_BA_PROP_ST1
//!BIND TENS_A_E
//!BIND TENS_B_E
//!SAVE FLOW_E_AB_PROP
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 2
//!DESC [prop12] contrast-weighted flow propagation AB (pass 1 of 3) [fused with its B->A twin: one dispatch] [aperture: the tensor solve when PROP_TENSOR is 1]

const float PROP_SELF_WEIGHT = 8.0;
const float PROP_CONF_FULL   = 0.08;
// The aperture-aware form (gen_aperture.py): each neighbour votes through its structure tensor, so an
// edge contributes only the component across itself; a cell's unconstrained component is filled from
// the cells within PROP_TENSOR_R that constrain it, and eps keeps its own flow where none does.
const int   PROP_TENSOR     = %s;
const int   PROP_TENSOR_R   = %s;
const float PROP_TENSOR_EPS = %s;

vec2 tensor_fill(vec2 uv, vec2 own, vec4 t_own, bool ba) {
    mat2 J0 = mat2(t_own.x, t_own.y, t_own.y, t_own.z);
    // the own vote keeps the base's share of the window: its 5x5 had 24 neighbours, this one (2R+1)^2 - 1
    float w_own = PROP_SELF_WEIGHT * t_own.w * t_own.w * float((2 * PROP_TENSOR_R + 1) * (2 * PROP_TENSOR_R + 1) - 1) / 24.0;
    mat2 W = w_own * J0 + mat2(PROP_TENSOR_EPS, 0.0, 0.0, PROP_TENSOR_EPS);
    vec2 b = w_own * (J0 * own) + PROP_TENSOR_EPS * own;
    for (int y = -PROP_TENSOR_R; y <= PROP_TENSOR_R; y++)
        for (int x = -PROP_TENSOR_R; x <= PROP_TENSOR_R; x++) {
            if (x == 0 && y == 0) continue;
            vec2 o = vec2(float(x), float(y)) * FLOW_E_AB_RAW_pt;
            vec4 t = ba ? TENS_B_E_tex(uv + o) : TENS_A_E_tex(uv + o);
            float w = t.w / (1.0 + 0.5 * float(abs(x) + abs(y)));
            if (w <= 0.0) continue;
            mat2 J = mat2(t.x, t.y, t.y, t.z);
            vec2 f = ba ? FLOW_E_BA_RAW_tex(uv + o).xy : FLOW_E_AB_RAW_tex(uv + o).xy;
            W += w * J;
            b += w * (J * f);
        }
    return inverse(W) * b;
}
""" % (PROP_TENSOR, PROP_TENSOR_R, PROP_TENSOR_EPS), text)

# the BA half of pass 1
old_ba = """void hook_ba() {
    vec2 uv = FLOW_E_BA_RAW_pos;
    vec2 own = FLOW_E_BA_RAW_tex(uv).xy;
    float c_own = prop_conf(uv);
    vec2 acc = vec2(0.0);
"""
new_ba = """void hook_ba() {
    vec2 uv = FLOW_E_BA_RAW_pos;
    vec2 own = FLOW_E_BA_RAW_tex(uv).xy;
    if (PROP_TENSOR == 1)
        { imageStore(FLOW_E_BA_PROP_ST1, ivec2(gl_FragCoord.xy), vec4(tensor_fill(uv, own, TENS_B_E_tex(uv), true), 0.0, 0.0)); return; }
    float c_own = prop_conf(uv);
    vec2 acc = vec2(0.0);
"""
text = must_replace(old_ba, new_ba, text)
# the AB half of pass 1 (the hook right after hook_ba in the same pass)
old_ab = """vec4 hook() {
    hook_ba();
    vec2 uv = FLOW_E_AB_RAW_pos;
    vec2 own = FLOW_E_AB_RAW_tex(uv).xy;
    float c_own = prop_conf(uv);
"""
new_ab = """vec4 hook() {
    hook_ba();
    vec2 uv = FLOW_E_AB_RAW_pos;
    vec2 own = FLOW_E_AB_RAW_tex(uv).xy;
    if (PROP_TENSOR == 1)
        return vec4(tensor_fill(uv, own, TENS_A_E_tex(uv), false), 0.0, 0.0);
    float c_own = prop_conf(uv);
"""
text = must_replace(old_ab, new_ab, text)

# 3. the data check: the disagreement through the cell's own tensor
head_chk = """//!BIND FLOW_E_BA_PROP_ST3
//!BIND FLOW_E_BA_ST
//!SAVE FLOW_E_AB
"""
text = must_replace(head_chk, """//!BIND FLOW_E_BA_PROP_ST3
//!BIND FLOW_E_BA_ST
//!BIND TENS_A_E
//!BIND TENS_B_E
//!SAVE FLOW_E_AB
""", text)
old_c = "const float PROP_CONF_FULL    = 0.08;\n\nfloat prop_conf(vec2 uv) {"
text = must_replace(old_c, """const float PROP_CONF_FULL    = 0.08;
const int   PROP_TENSOR       = %s;   // gen_aperture.py: the disagreement measured through the cell's tensor

vec2 tensor_proj(vec4 t, vec2 d) { return mat2(t.x, t.y, t.y, t.z) * d; }

float prop_conf(vec2 uv) {""" % PROP_TENSOR, text)
old_dis_ba = """        if (length(prop - raw) > max(PROP_DISAGREE, PROP_DISAGREE_REL * length(raw)))
            { imageStore(FLOW_E_BA_ST, ivec2(gl_FragCoord.xy), vec4(0.0)); return; }
"""
new_dis_ba = """        vec2 dis_ba = (PROP_TENSOR == 1) ? tensor_proj(TENS_B_E_tex(uv), prop - raw) : (prop - raw);
        if (length(dis_ba) > max(PROP_DISAGREE, PROP_DISAGREE_REL * length(raw)))
            { imageStore(FLOW_E_BA_ST, ivec2(gl_FragCoord.xy), vec4(0.0)); return; }
"""
text = must_replace(old_dis_ba, new_dis_ba, text)
old_dis_ab = """        if (length(prop - raw) > max(PROP_DISAGREE, PROP_DISAGREE_REL * length(raw)))
            return vec4(0.0);
"""
new_dis_ab = """        vec2 dis_ab = (PROP_TENSOR == 1) ? tensor_proj(TENS_A_E_tex(uv), prop - raw) : (prop - raw);
        if (length(dis_ab) > max(PROP_DISAGREE, PROP_DISAGREE_REL * length(raw)))
            return vec4(0.0);
"""
text = must_replace(old_dis_ab, new_dis_ab, text)

# 4. the header
banner = """// bidirectional-interpolation-propagated-aperture.glsl
// GENERATED by tests/gen_aperture.py from bidirectional-interpolation-propagated.glsl -- do not edit.
// The propagated base with an APERTURE-AWARE first propagation pass: neighbours vote through their
// structure tensors, so an edge supplies only the component across itself and a cell's unconstrained
// component is filled from the nearest cells that constrain it (PROP_TENSOR %s, radius %s, eps %s).
// See the generator's docstring and NFRAME-LIMITS.md ("the stairs' lensing", 2026-09-07).
//
""" % (PROP_TENSOR, PROP_TENSOR_R, PROP_TENSOR_EPS)
text = banner + text

out = HR.add_tail(text, 0)
OUT.write_text(out, encoding="utf-8", newline="\n")
print(f"{OUT.name}: {out.count('//!HOOK')} passes; PROP_TENSOR {PROP_TENSOR}, R {PROP_TENSOR_R}, eps {PROP_TENSOR_EPS}")
