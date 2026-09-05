#!/usr/bin/env python3
"""Generate the six-frame (sextdirectional) shader from a two-frame base.

    ./gen_sextdirectional.py [output.glsl [base.glsl]]    (default: ../shaders/sextdirectional-interpolation.glsl)

Everything the five-frame generator does, plus one slot -- luma pyramids and the cut statistic for slot
5, the slot 4 <-> 5 flow chains at every level, their full-res refines, one more half-res pack, one more
full-res pack, the cut statistics in a 2x1 texture (five do not fit one texel) -- and a different FIELD
estimator. The quint's is the exact quartic through the anchor's four displacements over a symmetric
window; that window exists only at the odd frame count's centre. Six frames have no centre: at the exact
N:N phase the output sits at the end of the straddle interval, on slot 3, with three links behind it and
two ahead, and at any other phase the anchor is slot 2 or 3 with the links split 2+3 or 3+2. So the
estimator here is a WEIGHTED LEAST-SQUARES quartic through however many of the six possible
displacements (taus -3..+3, the far ones composed from adjacent links, each round-trip checked) are
trusted, each weighted by its round trip; with four it is the quint's exact quartic, with five it is
overdetermined by one and the leftover -- the residual -- is a per-texel measurement of the fit's own
consistency, which the quad had at four frames (its mode 1) and the quint gave up. Mode 6 reports it.
The PICTURE keeps the quad's cubic placement on the four slots around the output, as the quint does, so
the interpolation ladder must equal the quad's.

The final pass is the quint's, transformed by asserted substitutions (the slot list, the packs, the roles,
the estimator block), so the two cannot drift apart silently. Slot letters are data (SLOTS below).
"""
import pathlib
import re
import sys

import gen_tridirectional as T3
import gen_quaddirectional as T4
import gen_quintdirectional as T5
import add_human_reading as READING

HERE = pathlib.Path(__file__).resolve().parent
SHADERS = HERE.parent / "shaders"


def shader_arg(s):
    p = pathlib.Path(s)
    return p if p.parent != pathlib.Path(".") else SHADERS / p


SRC = shader_arg(sys.argv[2]) if len(sys.argv) > 2 else SHADERS / "bidirectional-interpolation.glsl"
DST = shader_arg(sys.argv[1]) if len(sys.argv) > 1 else SHADERS / "sextdirectional-interpolation.glsl"

SLOTS = ["A", "B", "C", "D", "E", "F"]                    # slot 0..5
FRAMES = ["HOOKED", "FRAME1", "FRAME2", "FRAME3", "FRAME4", "FRAME5"]
SIX_BINDS = "\n".join(f"//!BIND {f}" for f in FRAMES)
PAIRS = [("A", "B", "AB", "BA", 0), ("B", "C", "BC", "CB", 1), ("C", "D", "CD", "DC", 2),
         ("D", "E", "DE", "ED", 3), ("E", "F", "EF", "FE", 4)]
T4.BANNER_PAIRS.update({"DE": (3, 4), "ED": (3, 4), "EF": (4, 5), "FE": (4, 5)})

BANNER_EF = T5.BANNER_DE.replace("SLOT 3 -> SLOT 4", "SLOT 4 -> SLOT 5").replace("[quint]", "[sext]")
BANNER_FE = T5.BANNER_ED.replace("SLOT 4 -> SLOT 3", "SLOT 5 -> SLOT 4").replace("[quint]", "[sext]")
assert BANNER_EF != T5.BANNER_DE and BANNER_FE != T5.BANNER_ED, "the quint's DE/ED banners changed shape"


def luma_block(letter, slot_index, frame_tex, lvl):
    return T5.luma_block(letter, slot_index, frame_tex, lvl).replace(T5.FIVE_BINDS, SIX_BINDS).replace("[quint]", "[sext]")


def cut_block(la, lb, save, pair):
    return T5.cut_block(la, lb, save, pair).replace("[quint]", "[sext]")


# ---- packing: five cut statistics need two texels; five half-res flows need three packs ----
def sub(t, old, new, n=1, what=""):
    assert t.count(old) == n, f"{what}: expected {n} of {old[:50]!r}, found {t.count(old)}"
    return t.replace(old, new)


PACKING = T5.PACKING
PACKING = sub(PACKING, "//!BIND SCENE_DIFF_DE\n//!SAVE CUTS\n//!WIDTH 1\n//!HEIGHT 1\n",
              "//!BIND SCENE_DIFF_DE\n//!BIND SCENE_DIFF_EF\n//!SAVE CUTS\n//!WIDTH 2\n//!HEIGHT 1\n", what="CUTS header")
PACKING = sub(PACKING, "//!DESC [quint] pack the four cut statistics into one texel (r: 0-1, g: 1-2, b: 2-3, a: 3-4)\nvec4 hook() {\n"
              "    return vec4(SCENE_DIFF_tex(vec2(0.5)).r, SCENE_DIFF_BC_tex(vec2(0.5)).r,\n"
              "                SCENE_DIFF_CD_tex(vec2(0.5)).r, SCENE_DIFF_DE_tex(vec2(0.5)).r);\n}",
              "//!DESC [sext] pack the five cut statistics into two texels (texel 0: 0-1, 1-2, 2-3, 3-4; texel 1: 4-5)\nvec4 hook() {\n"
              "    if (gl_FragCoord.x < 1.0)\n"
              "        return vec4(SCENE_DIFF_tex(vec2(0.5)).r, SCENE_DIFF_BC_tex(vec2(0.5)).r,\n"
              "                    SCENE_DIFF_CD_tex(vec2(0.5)).r, SCENE_DIFF_DE_tex(vec2(0.5)).r);\n"
              "    return vec4(SCENE_DIFF_EF_tex(vec2(0.5)).r, 0.0, 0.0, 0.0);\n}", what="CUTS body")
PACKING += """
//!HOOK FRAME_MIX
//!BIND FLOW_H_EF
//!SAVE FLOW_HP2
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!DESC [sext] pack the half-res straddle flow 4->5 (rg; ba unused)
vec4 hook() {
    return vec4(FLOW_H_EF_tex(FLOW_H_EF_pos).xy, 0.0, 0.0);
}
"""
PACKING = PACKING.replace("[quint]", "[sext]")


def pack_f(k, fwd, bwd):
    return T5.pack_f(k, fwd, bwd).replace("[quint]", "[sext]")


# ---- the final pass: the quint's, with the sixth slot, the extra packs, the wider roles, and the
# ---- least-squares estimator in place of the symmetric quartic
FINAL_PASS = T5.FINAL_PASS
FINAL_PASS = sub(FINAL_PASS, "//!BIND FRAME4\n", "//!BIND FRAME4\n//!BIND FRAME5\n", what="frame binds")
FINAL_PASS = sub(FINAL_PASS, "//!BIND FLOW_HP1\n", "//!BIND FLOW_HP1\n//!BIND FLOW_HP2\n", what="HP binds")
FINAL_PASS = sub(FINAL_PASS, "//!BIND FLOW_FP3\n", "//!BIND FLOW_FP3\n//!BIND FLOW_FP4\n", what="FP binds")
FINAL_PASS = sub(FINAL_PASS, "    if (i == 3) return FRAME3_tex(uv);\n    return FRAME4_tex(uv);\n}",
                 "    if (i == 3) return FRAME3_tex(uv);\n    if (i == 4) return FRAME4_tex(uv);\n    return FRAME5_tex(uv);\n}", what="slot_tex")
FINAL_PASS = sub(FINAL_PASS, "    vec4 t = (k < 2) ? FLOW_HP0_tex(uv) : FLOW_HP1_tex(uv);",
                 "    vec4 t = (k < 2) ? FLOW_HP0_tex(uv) : (k < 4) ? FLOW_HP1_tex(uv) : FLOW_HP2_tex(uv);", what="flow_h")
FINAL_PASS = sub(FINAL_PASS, "(k == 2) ? FLOW_FP2_tex(uv) : FLOW_FP3_tex(uv);",
                 "(k == 2) ? FLOW_FP2_tex(uv) : (k == 3) ? FLOW_FP3_tex(uv) : FLOW_FP4_tex(uv);", what="flow_f")
FINAL_PASS = sub(FINAL_PASS, "    vec4 c = CUTS_tex(vec2(0.5));\n    return (k == 0) ? c.r : (k == 1) ? c.g : (k == 2) ? c.b : c.a;",
                 "    vec4 c = CUTS_tex(vec2((k < 4) ? 0.25 : 0.75, 0.5));\n    return (k == 0) ? c.r : (k == 1) ? c.g : (k == 2) ? c.b : (k == 3) ? c.a : c.r;", what="cut")
FINAL_PASS = sub(FINAL_PASS, "    if (rts_mix[3] <= 0.0) p = 3;\n", "    if (rts_mix[3] <= 0.0) p = 3;\n    if (rts_mix[4] <= 0.0) p = 4;\n", what="roles")
FINAL_PASS = sub(FINAL_PASS, "int anchor = clamp(s <= 0.5 ? p : p + 1, 1, 3);", "int anchor = clamp(s <= 0.5 ? p : p + 1, 1, 4);", what="anchor clamp")
FINAL_PASS = sub(FINAL_PASS, "if (TRI_DIAG != 0 && DIAG_HOLD_ANCHOR == 1) anchor = 2;", "if (TRI_DIAG != 0 && DIAG_HOLD_ANCHOR == 1) anchor = 3;", what="held anchor")
FINAL_PASS = sub(FINAL_PASS, "    bool has_far_n = (anchor + 2 <= 4);", "    bool has_far_n = (anchor + 2 <= 5);", what="far link")
FINAL_PASS = sub(FINAL_PASS, "//!DESC [quint] motion-compensated warp (cubic placement) and the symmetric-window field",
                 "//!DESC [sext] motion-compensated warp (cubic placement) and the least-squares field", what="DESC")
FINAL_PASS = sub(FINAL_PASS, "//   6 = (unused here; 0)       7 = velocity, the straddle flow",
                 "//   6 = the fit's residual (px)  7 = velocity, the straddle flow", what="mode list")
FINAL_PASS = sub(FINAL_PASS, "        if (TRI_DIAG == 6)\n            return vec4(vec3(0.0), 1.0);",
                 "        if (TRI_DIAG == 6)\n            return vec4(vec3(clamp(resid_px / RESID_DIAG_FS, 0.0, 1.0)), 1.0);", what="mode 6")

LSQ = """    // ---- the FIELD: a weighted least-squares quartic through every trusted link, up to six ----
    // d(tau) = v tau + a/2 tau^2 + j/6 tau^3 + s/24 tau^4. Six frames have no centre: the anchor has
    // three links on one side and two on the other, so there is no symmetric stencil to solve exactly;
    // instead every displacement the window offers (taus -3..+3, the far ones composed from adjacent
    // links) enters a least-squares fit weighted by its own round trip. With four trusted links this is
    // the quint's exact quartic; with five it is overdetermined by one, and the leftover is the fit's
    // residual -- a per-texel measurement of how well ONE smooth trajectory explains all the links, the
    // confidence the quad's mode 1 had at four frames. Fewer than four trusted links: the quad's cubic.
    vec2 accel = accel_c, jerk = jerk_c;
    float resid_px = 0.0;
    {
        const float SNAP_MAX_PX = 8.0;
        bool has_f3n = has_far_n && (anchor + 3 <= 5);
        bool has_f3p = has_far_p && (anchor - 3 >= 0);
        vec2 f_f3n = vec2(0.0), f_f3p = vec2(0.0);
        float rt_f3n = 1.0e9, rt_f3p = 1.0e9, tau_f3n = 0.0, tau_f3p = 0.0, cut_f3n = 1.0, cut_f3p = 1.0;
        if (has_f3n) {
            vec2 link = flow_f(anchor + 2, true, HOOKED_pos + f_far_n);
            f_f3n = f_far_n + link;
            rt_f3n = max(rt_far_n, round_trip(link, flow_f(anchor + 2, false, HOOKED_pos + f_f3n)));
            tau_f3n = (rts_mix[anchor + 3] - rts_mix[anchor]) / L;
            cut_f3n = max(cut_far_n, cut(anchor + 2));
        }
        if (has_f3p) {
            vec2 link = flow_f(anchor - 3, false, HOOKED_pos + f_far_p);
            f_f3p = f_far_p + link;
            rt_f3p = max(rt_far_p, round_trip(link, flow_f(anchor - 3, true, HOOKED_pos + f_f3p)));
            tau_f3p = (rts_mix[anchor - 3] - rts_mix[anchor]) / L;
            cut_f3p = max(cut_far_p, cut(anchor - 3));
        }
        float tau[6]; vec2 d[6]; float w[6];
        tau[0] = tau_f3p; d[0] = f_f3p; w[0] = (has_f3p && cut_f3p <= SCENE_CUT_DIFF) ? 1.0 - smoothstep(ACCEL_TRUST_LO, ACCEL_TRUST_HI, rt_f3p) : 0.0;
        tau[1] = tau_fp;  d[1] = f_far_p; w[1] = (has_far_p && cut_far_p <= SCENE_CUT_DIFF) ? 1.0 - smoothstep(ACCEL_TRUST_LO, ACCEL_TRUST_HI, rt_far_p) : 0.0;
        tau[2] = tau_p;   d[2] = f_prev;  w[2] = 1.0 - smoothstep(ACCEL_TRUST_LO, ACCEL_TRUST_HI, rt_prev);
        tau[3] = tau_n;   d[3] = f_next;  w[3] = 1.0 - smoothstep(ACCEL_TRUST_LO, ACCEL_TRUST_HI, rt_next);
        tau[4] = tau_fn;  d[4] = f_far_n; w[4] = (has_far_n && cut_far_n <= SCENE_CUT_DIFF) ? 1.0 - smoothstep(ACCEL_TRUST_LO, ACCEL_TRUST_HI, rt_far_n) : 0.0;
        tau[5] = tau_f3n; d[5] = f_f3n;   w[5] = (has_f3n && cut_f3n <= SCENE_CUT_DIFF) ? 1.0 - smoothstep(ACCEL_TRUST_LO, ACCEL_TRUST_HI, rt_f3n) : 0.0;
        int nlinks = 0;
        for (int k = 0; k < 6; k++) if (w[k] > 0.05) nlinks++;
        // SEXT_CENTRED = 1: the anchor itself joins the fit as a seventh point (tau 0, displacement 0)
        // and the trajectory is fitted about the weighted centre of the points in use, with a free
        // constant. Measured 2026-09-05 on O9: fitted at the anchor, the lopsided stencil (three links
        // behind, two ahead at N:N) leaves an odd-order truncation bias of 0.2 px/interval^2 at every
        // zero crossing of the acceleration and an RMS three times the quint's; a fit about the centre
        // of a symmetric point set cancels the odd orders. The price is definitional: acceleration and
        // jerk are then reported at the CENTRE instant (half an interval before the anchor at N:N),
        // not at the anchor. SEXT_CENTRED = 0 fits at the anchor as the quint does.
        const int SEXT_CENTRED = 1;
        if (cut_adj <= SCENE_CUT_DIFF && nlinks >= 4) {
            // seven points: the six links and the anchor; five unknowns: c0, v, a/2, j/6, s/24 about tc
            float tau7[7]; vec2 d7[7]; float w7[7];
            for (int k = 0; k < 6; k++) { tau7[k] = tau[k]; d7[k] = d[k]; w7[k] = w[k]; }
            tau7[6] = 0.0; d7[6] = vec2(0.0); w7[6] = (SEXT_CENTRED == 1) ? 1.0 : 0.0;
            float tc = 0.0;
            if (SEXT_CENTRED == 1) {
                float sw = 0.0;
                for (int k = 0; k < 7; k++) { tc += w7[k] * tau7[k]; sw += w7[k]; }
                tc /= max(sw, 1.0e-6);
            }
            // normal equations, 5x5, solved by Gaussian elimination with partial pivoting
            float A[25]; float bx[5]; float by[5];
            for (int i = 0; i < 25; i++) A[i] = 0.0;
            for (int i = 0; i < 5; i++) { bx[i] = 0.0; by[i] = 0.0; }
            for (int k = 0; k < 7; k++) {
                if (w7[k] <= 0.05) continue;
                float u = tau7[k] - tc;
                float bb[5]; bb[0] = (SEXT_CENTRED == 1) ? 1.0 : 0.0; bb[1] = u; bb[2] = u * u * 0.5; bb[3] = u * u * u / 6.0; bb[4] = u * u * u * u / 24.0;
                for (int i = 0; i < 5; i++) {
                    for (int j = 0; j < 5; j++) A[i * 5 + j] += w7[k] * bb[i] * bb[j];
                    bx[i] += w7[k] * bb[i] * d7[k].x; by[i] += w7[k] * bb[i] * d7[k].y;
                }
            }
            if (SEXT_CENTRED == 0) { A[0] = 1.0; }    // the constant is pinned to zero at the anchor
            bool ok = true;
            for (int c = 0; c < 5; c++) {
                int piv = c;
                for (int r = c + 1; r < 5; r++) if (abs(A[r * 5 + c]) > abs(A[piv * 5 + c])) piv = r;
                if (abs(A[piv * 5 + c]) < 1.0e-9) { ok = false; break; }
                if (piv != c) {
                    for (int j = 0; j < 5; j++) { float t0 = A[c * 5 + j]; A[c * 5 + j] = A[piv * 5 + j]; A[piv * 5 + j] = t0; }
                    float t0 = bx[c]; bx[c] = bx[piv]; bx[piv] = t0; t0 = by[c]; by[c] = by[piv]; by[piv] = t0;
                }
                for (int r = 0; r < 5; r++) {
                    if (r == c) continue;
                    float f = A[r * 5 + c] / A[c * 5 + c];
                    if (f == 0.0) continue;
                    for (int j = c; j < 5; j++) A[r * 5 + j] -= f * A[c * 5 + j];
                    bx[r] -= f * bx[c]; by[r] -= f * by[c];
                }
            }
            if (ok) {
                float sx[5]; float sy[5];
                for (int i = 0; i < 5; i++) { sx[i] = bx[i] / A[i * 5 + i]; sy[i] = by[i] / A[i * 5 + i]; }
                // the snap row as the alarm, as in the quint: a lattice-sized value means a composed
                // far link jumped to a texture-period copy, and the estimate stays the quad's cubic
                float snap_px = length(vec2(sx[4], sy[4]) / HOOKED_pt);
                if (snap_px <= SNAP_MAX_PX) {
                    accel = clamp(vec2(sx[2], sy[2]), -amax, amax);
                    jerk  = clamp(vec2(sx[3], sy[3]), -jmax, jmax);
                    float num = 0.0, den = 0.0;
                    for (int k = 0; k < 7; k++) {
                        if (w7[k] <= 0.05) continue;
                        float u = tau7[k] - tc;
                        float c0 = (SEXT_CENTRED == 1) ? sx[0] : 0.0, c0y = (SEXT_CENTRED == 1) ? sy[0] : 0.0;
                        vec2 m = vec2(c0 + sx[1] * u + sx[2] * u * u * 0.5 + sx[3] * u * u * u / 6.0 + sx[4] * u * u * u * u / 24.0,
                                      c0y + sy[1] * u + sy[2] * u * u * 0.5 + sy[3] * u * u * u / 6.0 + sy[4] * u * u * u * u / 24.0);
                        vec2 r = d7[k] - m;
                        num += w7[k] * dot(r, r);
                        den += w7[k];
                    }
                    resid_px = sqrt(num / max(den, 1.0e-6)) / length(HOOKED_pt);
                }
            }
        }
    }
"""
i = FINAL_PASS.index("    // ---- the symmetric quartic (the field's estimator) where all four links hold ----")
j = FINAL_PASS.index("    // ---- cubic placement: the quad's warp, unchanged ----")
FINAL_PASS = FINAL_PASS[:i] + LSQ + FINAL_PASS[j:]
FINAL_PASS = FINAL_PASS.replace("[quint]", "[sext]")
assert "resid_px" in FINAL_PASS and "FLOW_FP4" in FINAL_PASS and "FRAME5" in FINAL_PASS

HEADER = """\
// =====================================================================
// GENERATED FILE -- DO NOT EDIT BY HAND.
//
// Produced by scripts/tests/gen_sextdirectional.py from
// bidirectional-interpolation.glsl. Edit the base (shared machinery) or
// the generator (everything [sext]-tagged) and regenerate:
//
//   ./tests/gen_sextdirectional.py
//
// SEXTDIRECTIONAL -- the six-frame experiment, for the FIELD. Binds the
// contiguous six-frame window around each output, computes all ten
// adjacent-slot flows, and fits a WEIGHTED LEAST-SQUARES quartic through
// every trusted displacement of the anchor (taus -3..+3, the far ones
// composed from adjacent links, each round-trip checked and weighted by
// it). Six frames have no centre, so there is no symmetric stencil: with
// four trusted links the fit is the quint's exact quartic, with five it
// is overdetermined and its residual (mode 6) is a per-texel measurement
// of how well one smooth trajectory explains all the links. The PICTURE
// is the quad's cubic on the four slots around the output, so the
// interpolation ladder must equal the quad's. Built on the night of
// 2026-09-05 at the owner's request; its calibration is owed.
// =====================================================================
"""


def main():
    text = READING.strip_tail(SRC.read_text())
    assert "TIE_MARGIN" in text, "base shader lacks TIE_MARGIN -- wrong vintage?"
    text = text[text.index("//!"):]
    for name in ("SUBPEL_REFINE", "SUBPEL_SELFREF"):
        n = text.count(f"const int {name} = 0;")
        assert n == 2, f"expected 2 {name} sites in base, found {n}"
        text = text.replace(f"const int {name} = 0;", f"const int {name} = 1;")
    n_zs = text.count("const int ZERO_SEED = 0;")
    assert n_zs in (0, 2), f"expected 0 or 2 ZERO_SEED sites in base, found {n_zs}"
    text = text.replace("const int ZERO_SEED = 0;", "const int ZERO_SEED = 1;")
    blocks = T3.chunk(text)
    hook_blocks = [b for b in blocks if "//!HOOK" in b]
    extra = len(hook_blocks) - 24
    fused = any("[fused" in b for b in hook_blocks)
    assert fused or (extra >= 0 and extra % 2 == 0), f"expected 24 base passes (+ an even number of extras), found {len(hook_blocks)}"

    def find(save, desc_frag=None):
        cands = [b for b in blocks if T3.block_id(b)[0] == save and
                 (desc_frag is None or desc_frag in (T3.block_id(b)[1] or ""))]
        assert len(cands) == 1, f"lookup {save}/{desc_frag}: {len(cands)} matches"
        return cands[0]

    def find_all(save):
        cands = [b for b in blocks if T3.block_id(b)[0] == save or (T3.block_id(b)[0] or "").startswith(save + "_")]
        assert cands, f"lookup {save}*: no matches"
        return cands
    find.all = find_all

    out = []
    for b in blocks:
        save, desc = T3.block_id(b)
        nb = b
        if save and re.fullmatch(r"LUMA_A_[SEQH]", save):
            nb = nb.replace("//!BIND HOOKED", SIX_BINDS)
            nb = nb.replace("[high] downsample frame A", "[sext] downsample slot 0")
        elif save and re.fullmatch(r"LUMA_B_[SEQH]", save):
            lvl = save[-1]
            nb = nb.replace("//!BIND NEXT", SIX_BINDS)
            nb = nb.replace("NEXT_tex(NEXT_pos)", "FRAME1_tex(HOOKED_pos)")
            nb = nb.replace("[high] downsample frame B", "[sext] downsample slot 1")
            for letter, idx, frame in zip(SLOTS[2:], range(2, 6), FRAMES[2:]):
                nb += luma_block(letter, idx, frame, lvl)
        elif save == "SCENE_DIFF":
            nb = nb.replace("[high] scene-cut statistic (whole-frame luma difference)", "[sext] scene-cut statistic, slots 0-1")
            nb += cut_block("B", "C", "SCENE_DIFF_BC", "1-2")
            nb += cut_block("C", "D", "SCENE_DIFF_CD", "2-3")
            nb += cut_block("D", "E", "SCENE_DIFF_DE", "3-4")
            nb += cut_block("E", "F", "SCENE_DIFF_EF", "4-5")
        elif save in ("EDGE_A", "EDGE_B"):
            nb = nb.replace("//!BIND HOOKED\n//!BIND NEXT", SIX_BINDS)
            nb = re.sub(r"\bNEXT_tex\(", "FRAME1_tex(", nb)
            nb = nb.replace("NEXT_pos", "HOOKED_pos")
        elif save == "FRAME_MIX":
            nb = FINAL_PASS
        out.append(nb)
        if save == "FLOW_H_BA" and desc and "pass 2" in desc:
            banners = {"BC": T4.BANNERS["BC"], "CB": T4.BANNERS["CB"], "CD": T4.BANNERS["CD"], "DC": T4.BANNERS["DC"],
                       "DE": T5.BANNER_DE, "ED": T5.BANNER_ED, "EF": BANNER_EF, "FE": BANNER_FE}
            for la, lb, fwd, bwd, k in PAIRS[1:]:
                if fused:
                    out.append(T4.pair_chain(blocks, la, lb, fwd, bwd, banners[fwd], banners[bwd]).replace("[quad]", "[sext]").replace("[quint]", "[sext]"))
                else:
                    out.append(T4.chain(find, la, lb, fwd, rev=False, banner=banners[fwd]).replace("[quad]", "[sext]").replace("[quint]", "[sext]"))
                    out.append(T4.chain(find, la, lb, bwd, rev=True, banner=banners[bwd]).replace("[quad]", "[sext]").replace("[quint]", "[sext]"))
            for letter, idx, frame in zip(SLOTS, range(6), FRAMES):
                out.append(T3.fullres_luma(letter, idx, frame, SIX_BINDS, "sext"))
            h_ab = find("FLOW_H_AB", "refine")
            h_ba = find("FLOW_H_BA", "refine")
            out.append(T3.to_fullres(h_ab, "AB", "sext"))
            out.append(T3.to_fullres(h_ba, "BA", "sext"))
            for la, lb, fwd, bwd, k in PAIRS[1:]:
                out.append(T3.to_fullres(T4.shift_pair(h_ab, "H", la, lb, fwd, T4.BANNER_PAIRS[fwd]), fwd, "sext"))
                out.append(T3.to_fullres(T4.shift_pair(h_ba, "H", la, lb, bwd, T4.BANNER_PAIRS[bwd]), bwd, "sext"))
            out.append(PACKING)
            for la, lb, fwd, bwd, k in PAIRS:
                out.append(pack_f(k, fwd, bwd))
    result = "\n".join(out).replace("[quad]", "[sext]").replace("[quint]", "[sext]")
    code = "\n".join(l for l in result.split("\n") if not l.lstrip().startswith("//"))
    for bad in ("BIND NEXT", "NEXT_tex(", "NEXT_pos", "NEXT_size", "NEXT_pt"):
        assert bad not in code, f"residual 2-frame reference in code: {bad}"
    assert not re.search(r"\bmix_t\b", code), "mix_t survived in code"
    hooks = result.count("//!HOOK")
    braces = result.count("{") - result.count("}")
    parens = result.count("(") - result.count(")")
    # 24 base + 16 lumas (4 slots x 4 levels) + 4 cuts + 48 pair flow (4 pairs x 12) + 6 full-res lumas
    # + 10 full-res refines + 9 packing (CUTS, 3 HP, 5 FP) = 117, plus the base's extras once per pair
    expected = 117 + 5 * extra
    assert hooks == expected, f"expected {expected} passes, got {hooks}"
    assert braces == 0 and parens == 0, f"unbalanced: braces {braces}, parens {parens}"
    marker = "//!DESC [sext] motion-compensated warp"
    fp_binds = result[:result.index(marker)].rsplit("//!HOOK FRAME_MIX", 1)[1].count("//!BIND")
    assert fp_binds <= 16, f"final pass binds {fp_binds} textures, the ceiling is 16"
    header = HEADER
    if SRC.name != "bidirectional-interpolation.glsl":
        header = header.replace("bidirectional-interpolation.glsl", SRC.name)
        header = header.replace("//   ./tests/gen_sextdirectional.py\n", f"//   ./tests/gen_sextdirectional.py {DST.name} {SRC.name}\n")
    DST.write_text(READING.add_tail(header + result), newline="\n")
    print(f"  {DST.name}: {hooks} passes ({24 + extra} base + 16 slot-2..5 lumas + 4 cut stats + "
          f"{48 + 4 * extra} pair flow + 6 full-res lumas + 10 full-res refines + 9 packing), "
          f"final pass binds {fp_binds}, braces/parens balanced  OK")


if __name__ == "__main__":
    main()
