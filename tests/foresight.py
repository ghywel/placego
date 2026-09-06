"""The FORESIGHT SEED: the temporal seed mirrored in time (2026-09-06; NFRAME-LIMITS.md, "The foresight seed").

In the seeded family a pair's coarse search starts one of its descents from the PREVIOUS window's flow for
that pair -- the past-adjacent pair's motion at this texel -- and its 1/8 arbitration adds a prior toward it
where that flow round-trips. Nothing looked the other way, although the next pair's flow is computed in the
same window. This transform gives a generated pair that has a later neighbour (BC from CD in the quad; CD from
DE and BC from CD in the quint) a fourth coarse descent from the neighbour's arbitrated 1/8 flow at the same
texel (kept in the spare half of the temporal cache), a fifth 1/8 candidate refined from it, and a prior toward
it under the same round-trip trust the temporal prior uses: SEED_FUT_LAMBDA, the mirror of SEED_TEMP_LAMBDA.
Forward flows take the neighbour's forward flow, backward flows its backward flow. For the neighbour's caches
to hold this window's values the generators emit the later pair first; that reorder alone is bit-identical.

Measured (the quad, RX 6600, 2026-09-06): the 32-case ladder is a trade, mean +0.02 dB -- every textured case
whose motion changes inside the window gains (A5 +1.23, A7 +0.98, R3 +0.79, O1/F2 +0.36) and four fast
flat-edge cases lose (L2 -2.28, L3 -0.74, L6 -0.46, A3 -0.31); real footage is up on every segment (+0.13 dB,
+0.0005 SSIM over five); time +0.6% on the quad, +2.2% on the quint. The field at N:N does not see it in the
quad (the machine read is the last pair's forward flow, which has no future in the window) and moves a little
the wrong way in the quint. Seeding the base pair from its future as well (deferring the base's own chain)
changes nothing measurable and costs +3-5%; not shipped, recorded.

The PRIOR (SEED_FUT_LAMBDA 0.5, the mirror of SEED_TEMP_LAMBDA) bought a tenth on live action and cost
2.3 dB on a 16-px flat box, so the shipped form is the candidate alone (SEED_FUT_LAMBDA 0). The loss was
then located, the same day, in the one to three columns of the box's LEADING edge, rendered a fraction of
a pixel further along: the prior was breaking sub-texel ties between refinements of the same basin in
favour of the one nearest the next pair's flow, not choosing a wrong basin (a contrast-gated trust,
FUT_TRUST_CONTRAST, changed nothing and is kept off as the record of that). A half-texel deadband on the
prior (FUT_PRIOR_DEADBAND 0.5) repairs it: the box back to the shipped number, the live-action tenth kept,
a few tenths given back on the rotating texture -- a trade, so the deadband prior is the owner's knob pair,
off by default (NFRAME-LIMITS.md, "The prior's loss, located and repaired").

Every substitution is asserted to match exactly once (the column-aligned constants trap: a silent no-op
patch yields a full table of confident numbers). The transform applies only to a base that carries the
temporal seed; a base without SEED_TEMP_LAMBDA takes the generators' unchanged path.
"""
import re

import gen_tridirectional as T3

SEED_FUT_LAMBDA = "0.0"   # the foresight prior per 1/8 texel, toward the next pair's flow; "0.0" = candidate only
# Experimental (off = the shipped files, byte for byte): trust the next pair's flow at a texel only where
# the next pair's FIRST frame has texture there (its 5x5 contrast at 1/8 res at or above MIN_CONTRAST).
# The round trip that gates the prior closes anywhere on a flat interior, which is how the prior at 0.5
# cost 2.3 dB on a flat 16-px translation; this asks the flow it trusts to have been matched on something.
FUT_TRUST_CONTRAST = False
# Experimental (off = the shipped files): the prior pulls only beyond a deadband, in 1/8 texels, so it can
# break a BASIN tie (aliases sit two or more texels apart) but never a sub-texel tie between refinements
# of the same basin. Found 2026-09-06: with the prior at 0.5 the whole 2.3 dB loss on the 16-px flat box
# is the leading edge rendered a fraction of a pixel further along, i.e. the prior choosing the sub-texel
# refinement nearest the next pair's flow over the SAD minimum.
FUT_PRIOR_DEADBAND = "0.0"


def _sub1(nb, old, new, what):
    n = nb.count(old)
    assert n == 1, f"foresight {what}: expected 1 match, found {n}"
    return nb.replace(old, new)


def _desc(nb, note):
    m = re.search(r"^//!DESC (.+)$", nb, re.M)
    assert m, "foresight: no DESC line"
    return nb[:m.start()] + "//!DESC " + m.group(1) + " " + note + nb[m.end():]


def applies(base_text):
    """A base carries the temporal seed, so the foresight seed has something to mirror."""
    return "SEED_TEMP_LAMBDA" in base_text


def foresight(nb, own_fwd, own_bwd, fut_fwd, fut_bwd):
    """Patch one shifted block of pair (own_fwd/own_bwd) to read pair (fut_fwd/fut_bwd); other blocks pass through."""
    save, desc = T3.block_id(nb)
    if save == f"FLOW_S_{own_fwd}" and "[fused" in (desc or ""):
        return _coarse(nb, own_fwd, own_bwd, fut_fwd, fut_bwd)
    # The 1/8 seed arbitration is keyed on its own line, not on the pass name: the propagated base saves
    # it as FLOW_E_*_RAW (a check pass saves FLOW_E_* after propagation), the seeded base as FLOW_E_*
    # directly. Matching the name alone left the seeded quad with a fourth descent nothing read.
    arbitrates = "    float tl = trusted ? SEED_TEMP_LAMBDA : 0.0;\n" in nb
    if arbitrates and save in (f"FLOW_E_{own_fwd}_RAW", f"FLOW_E_{own_fwd}"):
        return _refine(nb, own_fwd, fut_fwd, fut_bwd, "uv_a")
    if arbitrates and save in (f"FLOW_E_{own_bwd}_RAW", f"FLOW_E_{own_bwd}"):
        return _refine(nb, own_bwd, fut_bwd, fut_fwd, "uv_b")
    return nb


def _coarse(nb, own_fwd, own_bwd, fut_fwd, fut_bwd):
    # the backward twin (coarse_ba): descend_s2 / uv_b / the backward caches
    nb = _sub1(nb,
               f"    vec2 prev_s = imageLoad(FLOW_S_{own_bwd}_CACHE, coord).xy * LUMA_A_S_pt;\n",
               f"    vec2 prev_s = imageLoad(FLOW_S_{own_bwd}_CACHE, coord).xy * LUMA_A_S_pt;\n"
               f"    vec2 fut_s = imageLoad(FLOW_E_{fut_bwd}_CACHE, coord * 2).xy * 0.5 * LUMA_A_S_pt;\n",
               "coarse bwd prev_s")
    nb = _sub1(nb,
               f"    vec2 off_c = descend_s2(uv_b, prev_s, cost_c);\n"
               f"    imageStore(FLOW_S_{own_bwd}_CACHE2, coord, vec4(off_c / LUMA_A_S_pt, 0.0, 0.0));\n",
               f"    vec2 off_c = descend_s2(uv_b, prev_s, cost_c);\n"
               f"    float cost_f;\n"
               f"    vec2 off_f = descend_s2(uv_b, fut_s, cost_f);\n"
               f"    imageStore(FLOW_S_{own_bwd}_CACHE2, coord, vec4(off_c / LUMA_A_S_pt, off_f / LUMA_A_S_pt));\n",
               "coarse bwd descent")
    # the forward direction (hook): descend_s / uv_a / the forward caches
    nb = _sub1(nb,
               f"    vec2 prev_s = imageLoad(FLOW_S_{own_fwd}_CACHE, coord).xy * LUMA_A_S_pt;\n",
               f"    vec2 prev_s = imageLoad(FLOW_S_{own_fwd}_CACHE, coord).xy * LUMA_A_S_pt;\n"
               f"    vec2 fut_s = imageLoad(FLOW_E_{fut_fwd}_CACHE, coord * 2).xy * 0.5 * LUMA_A_S_pt;\n",
               "coarse fwd prev_s")
    nb = _sub1(nb,
               f"    vec2 off_c = descend_s(uv_a, prev_s, cost_c);\n"
               f"    imageStore(FLOW_S_{own_fwd}_CACHE2, coord, vec4(off_c / LUMA_A_S_pt, 0.0, 0.0));\n",
               f"    vec2 off_c = descend_s(uv_a, prev_s, cost_c);\n"
               f"    float cost_f;\n"
               f"    vec2 off_f = descend_s(uv_a, fut_s, cost_f);\n"
               f"    imageStore(FLOW_S_{own_fwd}_CACHE2, coord, vec4(off_c / LUMA_A_S_pt, off_f / LUMA_A_S_pt));\n",
               "coarse fwd descent")
    nb = T3.add_binds(nb, [f"FLOW_E_{fut_fwd}_CACHE", f"FLOW_E_{fut_bwd}_CACHE"])
    return _desc(nb, f"[foresight: fourth descent from the {fut_fwd}/{fut_bwd} 1/8 flow]")


def _refine(nb, own, fut, fut_rev, uv):
    nb = _sub1(nb,
               "const float SEED_RT_MAX = 1.0;   // E-texels; the previous flow must round-trip within this to be trusted\n",
               "const float SEED_RT_MAX = 1.0;   // E-texels; the previous flow must round-trip within this to be trusted\n"
               f"const float SEED_FUT_LAMBDA = {SEED_FUT_LAMBDA};   // the foresight prior, toward the NEXT pair's flow: SEED_TEMP_LAMBDA mirrored in time\n",
               "SEED_FUT_LAMBDA")
    nb = _sub1(nb,
               "    float tl = trusted ? SEED_TEMP_LAMBDA : 0.0;\n",
               "    float tl = trusted ? SEED_TEMP_LAMBDA : 0.0;\n"
               f"    // ---- the foresight seed: the next pair's flow at this texel, trusted where IT round-trips ----\n"
               f"    vec2 fut_e = imageLoad(FLOW_E_{fut}_CACHE, coord).xy * LUMA_A_E_pt;\n"
               f"    ivec2 fcoord = clamp(ivec2(({uv} + fut_e) * LUMA_A_E_size), ivec2(0), ivec2(LUMA_A_E_size) - 1);\n"
               f"    vec2 fut_rev = imageLoad(FLOW_E_{fut_rev}_CACHE, fcoord).xy * LUMA_A_E_pt;\n"
               f"    float rt_f = length((fut_e + fut_rev) / LUMA_A_E_pt);\n"
               f"    bool trusted_f = rt_f < SEED_RT_MAX && length(fut_e) > 0.0;\n"
               f"    float fl = trusted_f ? SEED_FUT_LAMBDA : 0.0;\n",
               "tl line")
    nb = _sub1(nb,
               f"    vec2 base_off3 = imageLoad(FLOW_S_{own}_CACHE2, scoord).xy * 2.0 * LUMA_A_E_pt;\n"
               f"    float sad_a, sad_b, sad_c;\n",
               f"    vec2 base_off3 = imageLoad(FLOW_S_{own}_CACHE2, scoord).xy * 2.0 * LUMA_A_E_pt;\n"
               f"    vec2 base_off4 = imageLoad(FLOW_S_{own}_CACHE2, scoord).zw * 2.0 * LUMA_A_E_pt;\n"
               f"    float sad_a, sad_b, sad_c, sad_f;\n",
               "base_off3")
    nb = _sub1(nb,
               f"    vec2 ref_c = refine_e({uv}, base_off3, sad_c);\n",
               f"    vec2 ref_c = refine_e({uv}, base_off3, sad_c);\n"
               f"    vec2 ref_f = refine_e({uv}, base_off4, sad_f);\n",
               "ref_c")
    for s in ("a", "b"):
        nb = _sub1(nb,
                   f" + tl * length((ref_{s} - prev_e) / LUMA_A_E_pt);\n",
                   f" + tl * length((ref_{s} - prev_e) / LUMA_A_E_pt) + fl * length((ref_{s} - fut_e) / LUMA_A_E_pt);\n",
                   f"score_{s}")
    nb = _sub1(nb,
               " + tl * length((ref_c - prev_e) / LUMA_A_E_pt) : 1.0e30;\n",
               " + tl * length((ref_c - prev_e) / LUMA_A_E_pt) + fl * length((ref_c - fut_e) / LUMA_A_E_pt) : 1.0e30;\n"
               "    float score_f = trusted_f ? sad_f + SEED_MAG_LAMBDA * length(ref_f / LUMA_A_E_pt) + tl * length((ref_f - prev_e) / LUMA_A_E_pt) + fl * length((ref_f - fut_e) / LUMA_A_E_pt) : 1.0e30;\n",
               "score_c")
    nb = _sub1(nb,
               " + tl * length((ref_d - prev_e) / LUMA_A_E_pt);\n",
               " + tl * length((ref_d - prev_e) / LUMA_A_E_pt) + fl * length((ref_d - fut_e) / LUMA_A_E_pt);\n",
               "score_d")
    nb = _sub1(nb,
               "    if (score_c < best_score * (1.0 - TIE_MARGIN)) { best_off = ref_c; best_score = score_c; }\n",
               "    if (score_c < best_score * (1.0 - TIE_MARGIN)) { best_off = ref_c; best_score = score_c; }\n"
               "    if (score_f < best_score * (1.0 - TIE_MARGIN)) { best_off = ref_f; best_score = score_f; }\n",
               "arbitration")
    nb = _sub1(nb,
               "(best_off == ref_b) ? sad_b : sad_c;\n",
               "(best_off == ref_b) ? sad_b : (best_off == ref_c) ? sad_c : sad_f;\n",
               "best_sad")
    nb = T3.add_binds(nb, [f"FLOW_E_{fut}_CACHE", f"FLOW_E_{fut_rev}_CACHE"])
    note = f"[foresight: fifth candidate and prior from the {fut} 1/8 flow]"
    if FUT_PRIOR_DEADBAND != "0.0":
        n_terms = nb.count(" - fut_e) / LUMA_A_E_pt)")
        assert n_terms == 5, f"expected 5 prior terms (a, b, c, d, f), found {n_terms}"
        for s in ("a", "b", "c", "d", "f"):
            nb = _sub1(nb,
                       f"fl * length((ref_{s} - fut_e) / LUMA_A_E_pt)",
                       f"fl * max(0.0, length((ref_{s} - fut_e) / LUMA_A_E_pt) - {FUT_PRIOR_DEADBAND})",
                       f"deadband {s}")
        note = note[:-1] + f", deadband {FUT_PRIOR_DEADBAND} texel]"
    if FUT_TRUST_CONTRAST:
        first = fut[0]   # the next pair's first frame: the frame its flow at this texel was matched FROM
        nb = _sub1(nb,
                   "const float SEED_MAG_LAMBDA = 0.3;\n",
                   "// The next pair's first frame's own 5x5 contrast at this texel (FUT_TRUST_CONTRAST): a flow read\n"
                   "// where that frame is flat was matched on nothing and closes a round trip by accident.\n"
                   "float local_contrast_5x5_fut(vec2 uv) {\n"
                   "    float lo = 1.0, hi = 0.0;\n"
                   "    for (int y = -2; y <= 2; y++) {\n"
                   "        for (int x = -2; x <= 2; x++) {\n"
                   f"            float v = LUMA_{first}_E_tex(uv + vec2(float(x), float(y)) * LUMA_A_E_pt).r;\n"
                   "            lo = min(lo, v);\n"
                   "            hi = max(hi, v);\n"
                   "        }\n"
                   "    }\n"
                   "    return hi - lo;\n"
                   "}\n"
                   "const float SEED_MAG_LAMBDA = 0.3;\n",
                   "contrast function")
        nb = _sub1(nb,
                   "    bool trusted_f = rt_f < SEED_RT_MAX && length(fut_e) > 0.0;\n",
                   f"    bool trusted_f = rt_f < SEED_RT_MAX && length(fut_e) > 0.0 && local_contrast_5x5_fut({uv}) >= MIN_CONTRAST;\n",
                   "contrast trust")
        nb = T3.add_binds(nb, [f"LUMA_{first}_E"])
        note = f"[foresight: fifth candidate and prior from the {fut} 1/8 flow, trusted where frame {first} has texture at the texel]"
    return _desc(nb, note)
