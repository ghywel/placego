#!/usr/bin/env python3
"""Generate the five-frame (quintdirectional) shader from a two-frame base.

    ./gen_quintdirectional.py [output.glsl [base.glsl]]    (default: ../shaders/quintdirectional-interpolation.glsl)

Everything the four-frame generator does, plus one slot: luma pyramids and
the cut statistic for slot 4, the slot 3 <-> 4 flow chains at every level
(cached, round-trip checkable), their full-res refines, three packing passes
that bring the final pass from 21 binds to 12 (libplacebo allows 16), and a
final pass that at the exact N:N phase reads FOUR displacements of the
anchor -- d(-1), d(+1) direct, d(-2), d(+2) composed from adjacent links --
and solves the exact quartic through them for acceleration and jerk, with
graded degrade to the quad's cubic and the tri's quadratic when a link is
untrusted or a cut severs it. The PICTURE keeps the quad's cubic placement
on the four slots around the output: the fifth frame is for the field, and
the interpolation ladder must equal the quad's. Design, costs and the
pre-registered targets: QUINTDIRECTIONAL.md.

Slot letters are data (SLOTS below); a sixth frame is a list change plus
the packing arithmetic, not a rewrite.
"""
import pathlib
import re
import sys

import gen_tridirectional as T3
import gen_quaddirectional as T4
import add_human_reading as READING

HERE = pathlib.Path(__file__).resolve().parent
SHADERS = HERE.parent / "shaders"


def shader_arg(s):
    p = pathlib.Path(s)
    return p if p.parent != pathlib.Path(".") else SHADERS / p


SRC = shader_arg(sys.argv[2]) if len(sys.argv) > 2 else SHADERS / "bidirectional-interpolation.glsl"
DST = shader_arg(sys.argv[1]) if len(sys.argv) > 1 else SHADERS / "quintdirectional-interpolation.glsl"

LEVELS = T3.LEVELS
SLOTS = ["A", "B", "C", "D", "E"]                      # slot 0..4
FRAMES = ["HOOKED", "FRAME1", "FRAME2", "FRAME3", "FRAME4"]
FIVE_BINDS = "\n".join(f"//!BIND {f}" for f in FRAMES)
PAIRS = [("A", "B", "AB", "BA", 0), ("B", "C", "BC", "CB", 1), ("C", "D", "CD", "DC", 2), ("D", "E", "DE", "ED", 3)]

# the quad's chain builder looks pairs up in its own module dict; teach it the new pair
T4.BANNER_PAIRS.update({"DE": (3, 4), "ED": (3, 4)})
BANNER_DE = """\
// =====================================================================
// SLOT 3 -> SLOT 4 flow chain ([quint], generated). The pair the fifth
// frame adds: the second link of the composed +2 displacement
// F24(x) = F23(x) + F34(x + F23(x)), the mirror of the quad's far flow.
// ====================================================================="""
BANNER_ED = """\
// =====================================================================
// SLOT 4 -> SLOT 3 flow chain ([quint], generated). Reverse of the above,
// closing the round trip on the +2 displacement's second link.
// ====================================================================="""


def luma_block(letter, slot_index, frame_tex, lvl):
    div = dict(S=16, E=8, Q=4, H=2)[lvl]
    return f"""
//!HOOK FRAME_MIX
{FIVE_BINDS}
//!SAVE LUMA_{letter}_{lvl}
//!WIDTH HOOKED.w {div} /
//!HEIGHT HOOKED.h {div} /
//!COMPONENTS 1
//!DESC [quint] downsample slot {slot_index} to 1/{div} res (luma)
vec4 hook() {{
    return vec4(dot({frame_tex}_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}}"""


def cut_block(la, lb, save, pair):
    return T4.cut_block(la, lb, save, pair).replace("[quad]", "[quint]")


PACKING = """\
// ---------------------------------------------------------------------
// PACKING for the bind ceiling ([quint], generated). libplacebo binds at
// most sixteen textures per pass and the quad's final pass used all
// sixteen; a fifth slot adds five. Three kinds of copy pass bring the
// final pass to twelve: the four 1x1 cut statistics into one RGBA texel,
// the four half-res straddle flows into two RGBA textures (two flows
// each), the eight full-res stencil flows into four. Copies only; nothing
// the field reads changes.
// ---------------------------------------------------------------------
//!HOOK FRAME_MIX
//!BIND SCENE_DIFF
//!BIND SCENE_DIFF_BC
//!BIND SCENE_DIFF_CD
//!BIND SCENE_DIFF_DE
//!SAVE CUTS
//!WIDTH 1
//!HEIGHT 1
//!DESC [quint] pack the four cut statistics into one texel (r: 0-1, g: 1-2, b: 2-3, a: 3-4)
vec4 hook() {
    return vec4(SCENE_DIFF_tex(vec2(0.5)).r, SCENE_DIFF_BC_tex(vec2(0.5)).r,
                SCENE_DIFF_CD_tex(vec2(0.5)).r, SCENE_DIFF_DE_tex(vec2(0.5)).r);
}

//!HOOK FRAME_MIX
//!BIND FLOW_H_AB
//!BIND FLOW_H_BC
//!SAVE FLOW_HP0
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!DESC [quint] pack the half-res straddle flows 0->1 (rg) and 1->2 (ba)
vec4 hook() {
    return vec4(FLOW_H_AB_tex(FLOW_H_AB_pos).xy, FLOW_H_BC_tex(FLOW_H_BC_pos).xy);
}

//!HOOK FRAME_MIX
//!BIND FLOW_H_CD
//!BIND FLOW_H_DE
//!SAVE FLOW_HP1
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!DESC [quint] pack the half-res straddle flows 2->3 (rg) and 3->4 (ba)
vec4 hook() {
    return vec4(FLOW_H_CD_tex(FLOW_H_CD_pos).xy, FLOW_H_DE_tex(FLOW_H_DE_pos).xy);
}
"""


def pack_f(k, fwd, bwd):
    return f"""
//!HOOK FRAME_MIX
//!BIND FLOW_F_{fwd}
//!BIND FLOW_F_{bwd}
//!SAVE FLOW_FP{k}
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!DESC [quint] pack the full-res flows slot{k}->slot{k + 1} (rg) and slot{k + 1}->slot{k} (ba)
vec4 hook() {{
    return vec4(FLOW_F_{fwd}_tex(FLOW_F_{fwd}_pos).xy, FLOW_F_{bwd}_tex(FLOW_F_{bwd}_pos).xy);
}}"""


def main():
    text = READING.strip_tail(SRC.read_text())
    assert "TIE_MARGIN" in text, "base shader lacks TIE_MARGIN -- wrong vintage?"
    first = text.index("//!")
    text = text[first:]
    n_sub = text.count("const int SUBPEL_REFINE = 0;")
    assert n_sub == 2, f"expected 2 SUBPEL_REFINE sites in base, found {n_sub}"
    text = text.replace("const int SUBPEL_REFINE = 0;", "const int SUBPEL_REFINE = 1;")
    # the self-referenced fit rides with the refinement: on in every field shader, off in the picture bases
    n_self = text.count("const int SUBPEL_SELFREF = 0;")
    assert n_self == 2, f"expected 2 SUBPEL_SELFREF sites in base, found {n_self}"
    text = text.replace("const int SUBPEL_SELFREF = 0;", "const int SUBPEL_SELFREF = 1;")
    # the zero seed rides with the field shaders too: on here, off in the picture bases (+4% time)
    n_zs = text.count("const int ZERO_SEED = 0;")
    assert n_zs in (0, 2), f"expected 0 or 2 ZERO_SEED sites in base, found {n_zs}"
    text = text.replace("const int ZERO_SEED = 0;", "const int ZERO_SEED = 1;")
    blocks = T3.chunk(text)
    hook_blocks = [b for b in blocks if "//!HOOK" in b]
    extra = len(hook_blocks) - 24
    assert extra >= 0 and extra % 2 == 0, f"expected 24 base passes (+ an even number of extras), found {len(hook_blocks)}"

    def find(save, desc_frag=None):
        cands = [b for b in blocks if T3.block_id(b)[0] == save and
                 (desc_frag is None or desc_frag in (T3.block_id(b)[1] or ""))]
        assert len(cands) == 1, f"lookup {save}/{desc_frag}: {len(cands)} matches"
        return cands[0]

    def find_all(save):
        cands = [b for b in blocks if T3.block_id(b)[0] == save or
                 (T3.block_id(b)[0] or "").startswith(save + "_")]
        assert cands, f"lookup {save}*: no matches"
        return cands
    find.all = find_all

    out = []
    for b in blocks:
        save, desc = T3.block_id(b)
        nb = b
        if save and re.fullmatch(r"LUMA_A_[SEQH]", save):
            nb = nb.replace("//!BIND HOOKED", FIVE_BINDS)
            nb = nb.replace("[high] downsample frame A", "[quint] downsample slot 0")
        elif save and re.fullmatch(r"LUMA_B_[SEQH]", save):
            lvl = save[-1]
            nb = nb.replace("//!BIND NEXT", FIVE_BINDS)
            nb = nb.replace("NEXT_tex(NEXT_pos)", "FRAME1_tex(HOOKED_pos)")
            nb = nb.replace("[high] downsample frame B", "[quint] downsample slot 1")
            nb += luma_block("C", 2, "FRAME2", lvl)
            nb += luma_block("D", 3, "FRAME3", lvl)
            nb += luma_block("E", 4, "FRAME4", lvl)
        elif save == "SCENE_DIFF":
            nb = nb.replace("[high] scene-cut statistic (whole-frame luma difference)",
                            "[quint] scene-cut statistic, slots 0-1")
            nb += cut_block("B", "C", "SCENE_DIFF_BC", "1-2")
            nb += cut_block("C", "D", "SCENE_DIFF_CD", "2-3")
            nb += cut_block("D", "E", "SCENE_DIFF_DE", "3-4")
        elif save in ("EDGE_A", "EDGE_B"):
            nb = nb.replace("//!BIND HOOKED\n//!BIND NEXT", FIVE_BINDS)
            nb = re.sub(r"\bNEXT_tex\(", "FRAME1_tex(", nb)
            nb = nb.replace("NEXT_pos", "HOOKED_pos")
        elif save == "FRAME_MIX":
            nb = FINAL_PASS
        out.append(nb)
        if save == "FLOW_H_BA" and desc and "pass 2" in desc:
            out.append(T4.chain(find, "B", "C", "BC", rev=False, banner=T4.BANNERS["BC"]).replace("[quad]", "[quint]"))
            out.append(T4.chain(find, "B", "C", "CB", rev=True, banner=T4.BANNERS["CB"]).replace("[quad]", "[quint]"))
            out.append(T4.chain(find, "C", "D", "CD", rev=False, banner=T4.BANNERS["CD"]).replace("[quad]", "[quint]"))
            out.append(T4.chain(find, "C", "D", "DC", rev=True, banner=T4.BANNERS["DC"]).replace("[quad]", "[quint]"))
            out.append(T4.chain(find, "D", "E", "DE", rev=False, banner=BANNER_DE).replace("[quad]", "[quint]"))
            out.append(T4.chain(find, "D", "E", "ED", rev=True, banner=BANNER_ED).replace("[quad]", "[quint]"))
            for letter, idx, frame in zip(SLOTS, range(5), FRAMES):
                out.append(T3.fullres_luma(letter, idx, frame, FIVE_BINDS, "quint"))
            h_ab = find("FLOW_H_AB", "refine")
            h_ba = find("FLOW_H_BA", "refine")
            out.append(T3.to_fullres(h_ab, "AB", "quint"))
            out.append(T3.to_fullres(h_ba, "BA", "quint"))
            for la, lb, fwd, bwd, k in PAIRS[1:]:
                out.append(T3.to_fullres(T4.shift_pair(h_ab, "H", la, lb, fwd, T4.BANNER_PAIRS[fwd]), fwd, "quint"))
                out.append(T3.to_fullres(T4.shift_pair(h_ba, "H", la, lb, bwd, T4.BANNER_PAIRS[bwd]), bwd, "quint"))
            out.append(PACKING)
            for la, lb, fwd, bwd, k in PAIRS:
                out.append(pack_f(k, fwd, bwd))
    result = "\n".join(out)
    result = result.replace("[quad]", "[quint]")
    code = "\n".join(l for l in result.split("\n") if not l.lstrip().startswith("//"))
    for bad in ("BIND NEXT", "NEXT_tex(", "NEXT_pos", "NEXT_size", "NEXT_pt"):
        assert bad not in code, f"residual 2-frame reference in code: {bad}"
    assert not re.search(r"\bmix_t\b", code), "mix_t survived in code"
    hooks = result.count("//!HOOK")
    braces = result.count("{") - result.count("}")
    parens = result.count("(") - result.count(")")
    expected = 95 + 4 * extra
    assert hooks == expected, f"expected {expected} passes, got {hooks}"
    assert braces == 0 and parens == 0, f"unbalanced: braces {braces}, parens {parens}"
    # the final pass must sit under the bind ceiling
    fp = result[result.index("//!DESC [quint] motion-compensated warp"):]
    fp_binds = result[:result.index("//!DESC [quint] motion-compensated warp")].rsplit("//!HOOK FRAME_MIX", 1)[1].count("//!BIND")
    assert fp_binds <= 16, f"final pass binds {fp_binds} textures, the ceiling is 16"
    header = HEADER
    if SRC.name != "bidirectional-interpolation.glsl":
        header = header.replace("bidirectional-interpolation.glsl", SRC.name)
        header = header.replace("//   ./tests/gen_quintdirectional.py\n",
                                f"//   ./tests/gen_quintdirectional.py {DST.name} {SRC.name}\n")
    DST.write_text(READING.add_tail(header + result), newline="\n")
    print(f"  {DST.name}: {hooks} passes ({24 + extra} base + 12 slot-2/3/4 lumas + 3 cut stats + "
          f"{36 + 3 * extra} pair flow + 5 full-res lumas + 8 full-res refines + 7 packing), "
          f"final pass binds {fp_binds}, braces/parens balanced  OK")


FINAL_PASS = """\
// ---------------------------------------------------------------------
// Final pass: QUINTDIRECTIONAL -- the picture is the quad's cubic
// placement on the four slots around the output; the FIELD, at the exact
// N:N phase, is the exact quartic through the anchor's four displacements
// over a symmetric window (taus -2, -1, +1, +2). See QUINTDIRECTIONAL.md.
//
// EVERYTHING READ HERE IS SLOT-KEYED, through the packed textures: CUTS
// holds the four cut statistics, FLOW_HP0/1 the four half-res straddle
// flows, FLOW_FP0..3 the eight full-res flows (forward in rg, backward in
// ba). Composed two-interval displacements are built from adjacent links,
// never searched directly.
// ---------------------------------------------------------------------
//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!BIND FRAME3
//!BIND FRAME4
//!BIND CUTS
//!BIND FLOW_HP0
//!BIND FLOW_HP1
//!BIND FLOW_FP0
//!BIND FLOW_FP1
//!BIND FLOW_FP2
//!BIND FLOW_FP3
//!SAVE FRAME_MIX
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!DESC [quint] motion-compensated warp (cubic placement) and the symmetric-window field
// Same values and reasoning as the quad's final pass (see it for the sweeps).
const float SCENE_CUT_DIFF = 0.125;
const float ACCEL_MAX_PX = 16.0;
const float ACCEL_TRUST_LO = 2.0;
const float ACCEL_TRUST_HI = 5.0;
const float JERK_MAX_PX = 8.0;
const float ACCEL_DEADBAND_LO = 0.5;
const float ACCEL_DEADBAND_HI = 1.5;
const float JERK_DEADBAND_LO = 3.0;
const float JERK_DEADBAND_HI = 6.0;
// TRI_DIAG -- the quad's modes, unchanged in meaning, plus two for the
// per-regime comparison the design calls for:
//
//   0 = normal output          1 = correction (px)   2 = acceleration
//   3 = |a| heat map           4 = |a| linear luma   5 = jerk
//   6 = (unused here; 0)       7 = velocity, the straddle flow
//   8 = the QUAD's cubic acceleration from the same anchor (the compact
//       stencil), so the wider window's gain or loss is measured, not
//       assumed;   9 = the quad's cubic jerk likewise.
//
// Modes 2 and 5 report the symmetric quartic wherever all four links are
// trusted and unsevered, and degrade to the cubic (three links), the
// quadratic (two) or zero as links fall away. The WARP always uses the
// cubic, so the picture equals the quad's.
const int TRI_DIAG = 0;
const float ACCEL_DIAG_FS = 2.0;
const float CORR_DIAG_FS  = 0.25;
const float JERK_DIAG_FS  = 2.0;
const float RESID_DIAG_FS = 2.0;
const float VEL_DIAG_FS   = 2.0;
// DIAG_HOLD_ANCHOR = 1 pins the diag modes' anchor to slot 2 (the window's
// centre, the only slot with two links on each side), so a displayed field
// updates once per window advance; see the quad for the strobe it avoids.
const int DIAG_HOLD_ANCHOR = 0;
vec4 tri_diag_marker() {
    if (TRI_DIAG == 1) return vec4(1.0, 0.2, 0.2, 1.0);
    if (TRI_DIAG == 2 || TRI_DIAG == 8) return vec4(0.2, 0.6, 1.0, 1.0);
    if (TRI_DIAG == 5 || TRI_DIAG == 9) return vec4(1.0, 0.2, 1.0, 1.0);
    if (TRI_DIAG == 7) return vec4(1.0, 0.6, 0.1, 1.0);
    return vec4(0.2, 1.0, 0.3, 1.0);
}
vec4 slot_tex(int i, vec2 uv) {
    if (i == 0) return HOOKED_tex(uv);
    if (i == 1) return FRAME1_tex(uv);
    if (i == 2) return FRAME2_tex(uv);
    if (i == 3) return FRAME3_tex(uv);
    return FRAME4_tex(uv);
}
// half-res straddle flow of pair k (slot k -> k+1), in uv
vec2 flow_h(int k, vec2 uv) {
    vec4 t = (k < 2) ? FLOW_HP0_tex(uv) : FLOW_HP1_tex(uv);
    return ((k % 2 == 0) ? t.xy : t.zw) * 2.0 * HOOKED_pt;
}
// full-res flow slot k -> k+1 (fwd) or k+1 -> k (bwd), in uv
vec2 flow_f(int k, bool fwd, vec2 uv) {
    vec4 t = (k == 0) ? FLOW_FP0_tex(uv) : (k == 1) ? FLOW_FP1_tex(uv) : (k == 2) ? FLOW_FP2_tex(uv) : FLOW_FP3_tex(uv);
    return (fwd ? t.xy : t.zw) * HOOKED_pt;
}
float cut(int k) {
    vec4 c = CUTS_tex(vec2(0.5));
    return (k == 0) ? c.r : (k == 1) ? c.g : (k == 2) ? c.b : c.a;
}
float round_trip(vec2 d, vec2 back) { return length(d + back) / length(HOOKED_pt); }
vec4 hook() {
    // ---- roles: straddle pair (p, p+1) is the last slot at or before the output ----
    int p = 0;
    if (rts_mix[1] <= 0.0) p = 1;
    if (rts_mix[2] <= 0.0) p = 2;
    if (rts_mix[3] <= 0.0) p = 3;
    float tA = rts_mix[p];
    float tB = rts_mix[p + 1];
    float L  = tB - tA;
    float s  = clamp((0.0 - tA) / L, 0.0, 1.0);
    vec2 f_fwd = flow_h(p, HOOKED_pos);
    if (cut(p) > SCENE_CUT_DIFF)
        return s < 0.5 ? slot_tex(p, HOOKED_pos) : slot_tex(p + 1, HOOKED_pos);
    // ---- anchor: the straddling frame nearer the output, clamped to the interior slots {1, 2, 3} ----
    int anchor = clamp(s <= 0.5 ? p : p + 1, 1, 3);
    if (TRI_DIAG != 0 && DIAG_HOLD_ANCHOR == 1) anchor = 2;
    bool anchor_is_A = (anchor == p);
    // adjacent displacements of the anchor and their round trips
    vec2 f_prev = flow_f(anchor - 1, false, HOOKED_pos);              // anchor -> anchor-1
    vec2 f_next = flow_f(anchor, true, HOOKED_pos);                   // anchor -> anchor+1
    float rt_prev = round_trip(f_prev, flow_f(anchor - 1, true, HOOKED_pos + f_prev));
    float rt_next = round_trip(f_next, flow_f(anchor, false, HOOKED_pos + f_next));
    float tau_p = (rts_mix[anchor - 1] - rts_mix[anchor]) / L;
    float tau_n = (rts_mix[anchor + 1] - rts_mix[anchor]) / L;
    float cut_adj = max(cut(anchor - 1), cut(anchor));
    // composed +2 / -2 displacements where the window has the links
    bool has_far_n = (anchor + 2 <= 4);
    bool has_far_p = (anchor - 2 >= 0);
    vec2 f_far_n = vec2(0.0), f_far_p = vec2(0.0);
    float rt_far_n = 1.0e9, rt_far_p = 1.0e9;
    float tau_fn = 0.0, tau_fp = 0.0;
    float cut_far_n = 1.0, cut_far_p = 1.0;
    if (has_far_n) {
        vec2 link = flow_f(anchor + 1, true, HOOKED_pos + f_next);    // anchor+1 -> anchor+2 at the landing point
        f_far_n = f_next + link;
        rt_far_n = max(rt_next, round_trip(link, flow_f(anchor + 1, false, HOOKED_pos + f_far_n)));
        tau_fn = (rts_mix[anchor + 2] - rts_mix[anchor]) / L;
        cut_far_n = cut(anchor + 1);
    }
    if (has_far_p) {
        vec2 link = flow_f(anchor - 2, false, HOOKED_pos + f_prev);   // anchor-1 -> anchor-2 at the landing point
        f_far_p = f_prev + link;
        rt_far_p = max(rt_prev, round_trip(link, flow_f(anchor - 2, true, HOOKED_pos + f_far_p)));
        tau_fp = (rts_mix[anchor - 2] - rts_mix[anchor]) / L;
        cut_far_p = cut(anchor - 2);
    }
    // ---- the quad's cubic (the picture's estimator): three displacements, the far one THROUGH the straddle interval ----
    // The quad's rule, kept exactly: the earlier straddler (anchor == p) composes its far flow forward
    // (anchor -> anchor+1 -> anchor+2), the later one backward. Only when that side has no second link
    // (an outer anchor) does the other side serve.
    bool far_is_next = anchor_is_A ? has_far_n : !has_far_p;
    vec2 f_far = far_is_next ? f_far_n : f_far_p;
    float rt_far = far_is_next ? rt_far_n : rt_far_p;
    float tau_f = far_is_next ? tau_fn : tau_fp;
    float cut_link = far_is_next ? cut_far_n : cut_far_p;
    vec2 accel_c = vec2(0.0), jerk_c = vec2(0.0);
    {
        mat3 M = mat3(vec3(tau_p, tau_n, tau_f),
                      vec3(tau_p * tau_p, tau_n * tau_n, tau_f * tau_f) * 0.5,
                      vec3(tau_p * tau_p * tau_p, tau_n * tau_n * tau_n, tau_f * tau_f * tau_f) / 6.0);
        if (abs(determinant(M)) > 1.0e-4) {
            mat3 Mi = inverse(M);
            vec3 sx = Mi * vec3(f_prev.x, f_next.x, f_far.x);
            vec3 sy = Mi * vec3(f_prev.y, f_next.y, f_far.y);
            accel_c = vec2(sx.y, sy.y);
            jerk_c  = vec2(sx.z, sy.z);
        }
    }
    float g2 = 1.0 - smoothstep(ACCEL_TRUST_LO, ACCEL_TRUST_HI, max(rt_prev, rt_next));
    float g3 = 1.0 - smoothstep(ACCEL_TRUST_LO, ACCEL_TRUST_HI, max(max(rt_prev, rt_next), rt_far));
    accel_c *= g2;
    jerk_c  *= g3;
    if (cut_adj > SCENE_CUT_DIFF) { accel_c = vec2(0.0); jerk_c = vec2(0.0); }
    else if (cut_link > SCENE_CUT_DIFF) { jerk_c = vec2(0.0); }
    vec2 amax = ACCEL_MAX_PX * HOOKED_pt;
    vec2 jmax = JERK_MAX_PX * HOOKED_pt;
    accel_c = clamp(accel_c, -amax, amax);
    jerk_c  = clamp(jerk_c, -jmax, jmax);
    // ---- the symmetric quartic (the field's estimator) where all four links hold ----
    vec2 accel = accel_c, jerk = jerk_c;
    bool four = has_far_n && has_far_p
             && max(rt_far_n, rt_far_p) < ACCEL_TRUST_HI
             && cut_adj <= SCENE_CUT_DIFF && cut_far_n <= SCENE_CUT_DIFF && cut_far_p <= SCENE_CUT_DIFF;
    if (four) {
        // d(tau) = v tau + a/2 tau^2 + j/6 tau^3 + s/24 tau^4 through the four displacements;
        // a and j are read, the snap row is solved and ignored.
        mat4 M = mat4(vec4(tau_fp, tau_p, tau_n, tau_fn),
                      vec4(tau_fp * tau_fp, tau_p * tau_p, tau_n * tau_n, tau_fn * tau_fn) * 0.5,
                      vec4(tau_fp * tau_fp * tau_fp, tau_p * tau_p * tau_p, tau_n * tau_n * tau_n, tau_fn * tau_fn * tau_fn) / 6.0,
                      vec4(tau_fp * tau_fp * tau_fp * tau_fp, tau_p * tau_p * tau_p * tau_p,
                           tau_n * tau_n * tau_n * tau_n, tau_fn * tau_fn * tau_fn * tau_fn) / 24.0);
        if (abs(determinant(M)) > 1.0e-6) {
            mat4 Mi = inverse(M);
            vec4 sx = Mi * vec4(f_far_p.x, f_prev.x, f_next.x, f_far_n.x);
            vec4 sy = Mi * vec4(f_far_p.y, f_prev.y, f_next.y, f_far_n.y);
            // The snap row is the fourth difference of the five positions: a few px at most on any
            // motion the window can represent, lattice-sized when a composed far link has jumped to a
            // texture-period copy. Ignored as a signal, kept as the alarm: past SNAP_MAX_PX the far
            // links are not believed and the estimate stays the quad's cubic (mode 8).
            const float SNAP_MAX_PX = 8.0;
            float snap_px = length(vec2(sx.w, sy.w) / HOOKED_pt);
            // Trust per coefficient by the links that carry it. The near links' trust is already in the
            // cubic (g2, g3); the far links' round trips decide only how far the estimate moves from the
            // cubic toward the quartic -- never toward zero. Where the far links are not believed the
            // field is the quad's, which is the degrade the design promised.
            float g4 = 1.0 - smoothstep(ACCEL_TRUST_LO, ACCEL_TRUST_HI, max(rt_far_n, rt_far_p));
            if (snap_px > SNAP_MAX_PX) g4 = 0.0;
            accel = mix(accel_c, clamp(vec2(sx.y, sy.y) * g2, -amax, amax), g4);
            jerk  = mix(jerk_c,  clamp(vec2(sx.z, sy.z) * g2, -jmax, jmax), g4);
        }
    }
    // ---- cubic placement: the quad's warp, unchanged ----
    vec2 accel_w = accel_c;
    if (ACCEL_DEADBAND_HI > 0.0)
        accel_w *= smoothstep(ACCEL_DEADBAND_LO, ACCEL_DEADBAND_HI, length(accel_c / HOOKED_pt));
    vec2 jerk_w = jerk_c;
    if (JERK_DEADBAND_HI > 0.0)
        jerk_w *= smoothstep(JERK_DEADBAND_LO, JERK_DEADBAND_HI, length(jerk_c / HOOKED_pt));
    float jgeom = anchor_is_A ? (1.0 + s) : -(2.0 - s);
    vec2 corr = s * (1.0 - s) * (0.5 * accel_w + jerk_w * (jgeom / 6.0));
    if (TRI_DIAG != 0) {
        if (TRI_DIAG == 4)
            return vec4(vec3(clamp(length(accel / HOOKED_pt) / ACCEL_DIAG_FS, 0.0, 1.0)), 1.0);
        if (TRI_DIAG == 6)
            return vec4(vec3(0.0), 1.0);
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
        if (TRI_DIAG == 8)
            return vec4(0.5 + (accel_c / HOOKED_pt) * (0.5 / ACCEL_DIAG_FS), 0.5, 1.0);
        if (TRI_DIAG == 9)
            return vec4(0.5 + (jerk_c / HOOKED_pt) * (0.5 / JERK_DIAG_FS), 0.5, 1.0);
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
// Produced by scripts/tests/gen_quintdirectional.py from
// bidirectional-interpolation.glsl. Edit the base (shared machinery) or
// the generator (everything [quint]-tagged) and regenerate:
//
//   ./tests/gen_quintdirectional.py
//
// QUINTDIRECTIONAL -- the five-frame experiment, for the FIELD. Binds the
// contiguous five-frame window around each output, computes all eight
// adjacent-slot flows, and at the exact N:N phase fits the exact quartic
// through the anchor's four displacements over a symmetric window (taus
// -2, -1, +1, +2; the far two composed from adjacent links, each round-
// trip checked), reading acceleration and jerk and ignoring the snap row.
// Pre-registered to cut the acceleration error on fast oscillation 3-6x
// (the four-frame second difference's truncation) and the jerk noise on
// slow motion ~2.8x (the symmetric stencil's coefficients), and to change
// the PICTURE not at all: the warp is the quad's cubic on the four slots
// around the output, so the interpolation ladder must equal the quad's.
// Diagnostic modes 8 and 9 report the quad's cubic from the same anchor so
// the per-regime choice is measured. Design, costs, pre-registrations and
// results: QUINTDIRECTIONAL.md.
// =====================================================================
"""

if __name__ == "__main__":
    main()
