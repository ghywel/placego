#!/usr/bin/env python3
"""THE HALF-PERIOD ALIAS, IN THE SHADER: two switches for gen_variational.py (2026-09-28; PRIOR-ART.md's periodic-interior
survey, NFRAME-LIMITS.md "The carry, offline" and "Which of the cage's switches holds V3").

ALIAS_PRIOR=1 (needs GLOBAL_SEED=1) -- the frame's shift may break a LOCAL tie only if it is one of the tied answers.
    A new 1/8-level pass reads each cell's cost curve over +-3 texels (5 x 5 SAD, a tiny magnitude prior) and keeps
    its best shift, its RIVAL -- the best shift at least 2 texels away behind a RIDGE (a cost above both ends by a
    quarter of the curve's typical rise S = mean - best) -- and the margin (rival - best) / S (tests/probes/limb/
    ambiguity.py, offline: V3's interior flagged at 100%, its ends at 0%, real footage 0.1-2.6%). Where the margin is
    under ALIAS_TAU, the 1/8 refine measures its small-motion prior from ZERO unless the frame's shift lies within a
    texel of one of the two basins. On V3 the frame's shift is the patch's own motion and keeps its vote; on B1 it is a
    Moire artefact of the background, (+24, +24) px, and was deciding every tie toward "down".

ALIAS_CARRY=1 -- carry each pattern's END into its tied interior, every frame (tests/probes/limb/carry.py, offline:
    V3 8% -> 100% at every start, B1 24% -> 95%, the period family unharmed). At the quarter level, where 12 px is
    3 texels:
    1. hypotheses: each cell keeps its OWN two basins -- the 1/8 level's best and rival, both refined here -- with
       data costs in units of the curve's rise -- 0 for the better, the margin for the worse, and
       EXACTLY 0 for both when the margin is under ALIAS_TAU (a faint preference inside is what lets a boundary lose
       its grip: Imry-Ma). A cell with no rival has one hypothesis; a flat cell breaks the paths.
    2. four scans of semi-global matching's min-sum (Hirschmuller): along the rows in one pass and the columns in
       another, four invocations per line (forward and back, A->B and B->A), each into its own storage: L(p, v) = D(p, v) + min_u [L(p - r, u) + pen(v, u)] - min_u L(p - r, u),
       pen 0 / ALIAS_P1 for a one-texel step / ALIAS_P2 beyond;
    3. the four summed, each TIED cell whose own flow lies in one of its basins takes the cheaper one: the carry only
       switches aliases, and only where the cell cannot tell them apart; everywhere else the level's flow stands.
    Both directions (A->B, B->A), cached per source pair like every level above it.
    Build 5 (the aperture, ALIAS_APERTURE=1 by default; 0 behaves as build 4): the penalty and the pick ignore the
    component of a step along the cell's stripes (the structure tensor's minor axis over 5 x 5, weighted by
    coherence), and a switched flow keeps the level's own component along them. Inside stripes that component is
    unmeasurable, and at a pattern's ends the background had pulled the RIGHT alias's to junk while the wrong alias
    kept zero: B1 moving up 21.8 -> 23.7, down 25.3 -> 27.0 (tests/probes/limb/ownerdump.py, apcarry.py).

    alias_carry.add_alias_e(t)      the 1/8-level basins pass (either switch adds it, once)
    alias_carry.add_alias_prior(t)  the gate in the two 1/8 refine passes
    alias_carry.add_alias_carry(t)  the five quarter-level passes"""
import os

TAU = 0.05
# the CARRY's own tie threshold (stage 0c, 2026-09-30): an override that moves the carry alone; the prior's gate keeps TAU
TAU_CARRY = float(os.environ.get("ALIAS_TAU_CARRY", TAU))
LAMBDA = 0.001
M_MAX = 1.0
P1, P2 = 0.1, 1.0
BIG = 1.0e6


def _once(t, a, what):
    n = t.count(a)
    assert n == 1, f"alias ({what}): anchor found {n} times: {a[:80]!r}"


ALIAS_E = """
//!TEXTURE ALIAS_E_AB_ST
//!SIZE 480 270
//!FORMAT rgba32f
//!STORAGE

//!TEXTURE ALIAS_E_BA_ST
//!SIZE 480 270
//!FORMAT rgba32f
//!STORAGE

//!TEXTURE ALIAS_E_M_ST
//!SIZE 480 270
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND LUMA_A_E
//!BIND LUMA_B_E
//!BIND ALIAS_E_AB_ST
//!BIND ALIAS_E_BA_ST
//!BIND ALIAS_E_M_ST
//!SAVE ALIAS_E_AB
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 4
//!DESC [alias] the 1/8 level's two basins per cell, A->B and B->A: the best shift, the best rival behind a ridge, the margin
// (tests/alias_carry.py; offline: tests/probes/limb/ambiguity.py). .xy the best shift, .zw the rival, in this level's
// texels; the margins (rival - best, in units of the curve's typical rise) in ALIAS_E_M_ST.xy; no rival: the best twice
// and a margin of 1e6. B->A's basins in ALIAS_E_BA_ST.
const float ALIAS_LAMBDA = {LAMBDA};
float alias_sad(vec2 uv, vec2 d, bool ba) {{
    float s = 0.0;
    for (int y = -2; y <= 2; y++)
        for (int x = -2; x <= 2; x++) {{
            vec2 o = vec2(float(x), float(y)) * LUMA_A_E_pt;
            vec2 w = uv + o + d * LUMA_A_E_pt;
            s += ba ? abs(LUMA_B_E_tex(uv + o).r - LUMA_A_E_tex(w).r) : abs(LUMA_A_E_tex(uv + o).r - LUMA_B_E_tex(w).r);
        }}
    return s + ALIAS_LAMBDA * (abs(d.x) + abs(d.y));
}}
float alias_range(vec2 uv, bool ba) {{
    float lo = 1.0, hi = 0.0;
    for (int y = -2; y <= 2; y++)
        for (int x = -2; x <= 2; x++) {{
            vec2 o = vec2(float(x), float(y)) * LUMA_A_E_pt;
            float l = ba ? LUMA_B_E_tex(uv + o).r : LUMA_A_E_tex(uv + o).r;
            lo = min(lo, l); hi = max(hi, l);
        }}
    return hi - lo;
}}
vec4 alias_basins(vec2 uv, bool ba, out float margin) {{
    margin = {BIG};
    if (alias_range(uv, ba) < 0.02) return vec4(0.0);
    float c[49];
    float cmin = 1.0e30, csum = 0.0;
    int i1 = 24;
    for (int j = 0; j < 49; j++) {{
        float s = alias_sad(uv, vec2(float(j % 7 - 3), float(j / 7 - 3)), ba);
        c[j] = s; csum += s;
        if (s < cmin) {{ cmin = s; i1 = j; }}
    }}
    float S = max(csum / 49.0 - cmin, 1.0e-4);
    ivec2 a = ivec2(i1 % 7 - 3, i1 / 7 - 3);
    int i2 = i1;
    for (int j = 0; j < 49; j++) {{
        ivec2 b = ivec2(j % 7 - 3, j / 7 - 3);
        int n = max(abs(b.x - a.x), abs(b.y - a.y));
        if (n < 2) continue;
        float ridge = 0.0;
        for (int k = 1; k < n; k++) {{
            ivec2 p = ivec2(floor(vec2(a) + vec2(b - a) * float(k) / float(n) + 0.5));
            ridge = max(ridge, c[(p.y + 3) * 7 + p.x + 3]);
        }}
        if (ridge - max(cmin, c[j]) < 0.25 * S) continue;
        float m = (c[j] - cmin) / S;
        if (m < margin) {{ margin = m; i2 = j; }}
    }}
    return vec4(vec2(a), vec2(float(i2 % 7 - 3), float(i2 / 7 - 3)));
}}
vec4 hook() {{
    ivec2 coord = ivec2(LUMA_A_E_pos * LUMA_A_E_size);
    if (!pair_changed)
        return imageLoad(ALIAS_E_AB_ST, coord);
    float m_ab, m_ba;
    vec4 ab = alias_basins(LUMA_A_E_pos, false, m_ab);
    vec4 ba = alias_basins(LUMA_A_E_pos, true, m_ba);
    imageStore(ALIAS_E_AB_ST, coord, ab);
    imageStore(ALIAS_E_BA_ST, coord, ba);
    imageStore(ALIAS_E_M_ST, coord, vec4(m_ab, m_ba, 0.0, 0.0));
    return ab;
}}
""".format(LAMBDA=LAMBDA, BIG=f"{BIG:.1f}")


def add_alias_e(t):
    """the 1/8-level basins pass, right after the pass that saves LUMA_B_E (both lumas exist from there on)"""
    if "//!SAVE ALIAS_E_AB\n" in t:
        return t
    _once(t, "//!SAVE LUMA_B_E\n", "the 1/8 luma")
    i = t.index("//!SAVE LUMA_B_E\n")
    j = t.index("\n}\n", i) + 3
    return t[:j] + ALIAS_E + t[j:]


GATE = """    // ALIAS_PRIOR (tests/alias_carry.py): where this cell's two basins tie, the frame's shift breaks the tie only if it
    // IS one of them -- a frame shift that is neither (a background's Moire, B1) would decide every tie its own way.
    {{
        ivec2 ac = ivec2({UV} * LUMA_A_E_size);
        vec4 bas = imageLoad({BAS}, ac);
        float am = imageLoad(ALIAS_E_M_ST, ac).{M};
        vec2 gt = {SIGN}g_e / LUMA_A_E_pt;
        vec2 e1 = abs(gt - bas.xy), e2 = abs(gt - bas.zw);
        if (am < {TAU} && min(max(e1.x, e1.y), max(e2.x, e2.y)) > 1.0) g_e = vec2(0.0);
    }}
"""


def add_alias_prior(t):
    t = add_alias_e(t)
    for save, uv, bas, m, sign in (("FLOW_E_AB_RAW", "uv_a", "ALIAS_E_AB_ST", "x", ""),
                                   ("FLOW_E_BA_RAW", "uv_b", "ALIAS_E_BA_ST", "y", "-")):
        a = f"//!BIND GLOBAL_SHIFT\n//!SAVE {save}\n"
        _once(t, a, f"prior binds {save}")
        t = t.replace(a, f"//!BIND GLOBAL_SHIFT\n//!BIND {bas}\n//!BIND ALIAS_E_M_ST\n//!SAVE {save}\n")
        i = t.index(f"//!SAVE {save}\n")
        j = t.index("    vec2 g_e = GLOBAL_SHIFT_tex(vec2(0.5)).xy * 2.0 * LUMA_A_E_pt;", i)
        k = t.index("\n", j) + 1
        assert t.index("//!HOOK FRAME_MIX", i) > j, f"prior: g_e not in the {save} pass"
        t = t[:k] + GATE.format(UV=uv, BAS=bas, M=m, SIGN=sign, TAU=TAU) + t[k:]
    assert t.count("// ALIAS_PRIOR (tests/alias_carry.py)") == 2
    return t


HYP = """
//!TEXTURE ALIAS_Q_AB_ST
//!SIZE 960 540
//!FORMAT rgba32f
//!STORAGE

//!TEXTURE ALIAS_Q_BA_ST
//!SIZE 960 540
//!FORMAT rgba32f
//!STORAGE

//!TEXTURE ALIAS_Q1_AB_ST
//!SIZE 960 540
//!FORMAT rgba32f
//!STORAGE

//!TEXTURE ALIAS_Q1_BA_ST
//!SIZE 960 540
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND LUMA_A_Q
//!BIND LUMA_B_Q
//!BIND LUMA_A_E
//!BIND LUMA_B_E
//!BIND ALIAS_E_AB
//!BIND ALIAS_E_AB_ST
//!BIND ALIAS_E_BA_ST
//!BIND ALIAS_E_M_ST
//!BIND ALIAS_Q_AB_ST
//!BIND ALIAS_Q_BA_ST
//!BIND ALIAS_Q1_AB_ST
//!BIND ALIAS_Q1_BA_ST
//!SAVE ALIAS_Q_AB
//!WIDTH HOOKED.w 4 /
//!HEIGHT HOOKED.h 4 /
//!COMPONENTS 4
//!DESC [alias] each quarter-level cell's two hypotheses, A->B and B->A: the two basins the 1/8 level found, refined here, and their data costs
// The cell's OWN basins, not the level's flow: b1 (the 1/8 curve's best) in ALIAS_Q1_*_ST.xy; b2 (its rival) in
// ALIAS_Q_*_ST.xy with the data costs in .zw, in units of the cost curve's rise: 0 for the better, the margin for
// the worse, both EXACTLY 0 on a tie; .w = 1e6 where there is one basin; .z = -1 on a flat cell (it breaks the scans).
// (The first build carried the level's own flow as the first hypothesis. Where that flow was junk -- at a pattern's
// sides and ends, the very cells that hold the evidence -- the carry either anchored on the junk or, told to ignore
// such cells, lost the end's evidence: V3 moving UP stayed at 21 on the recommendation and 26 on the cage.)
const float ALIAS_LAMBDA = {LAMBDA};
float qsad(vec2 uv, vec2 d, bool ba) {{
    float s = 0.0;
    for (int y = -2; y <= 2; y++)
        for (int x = -2; x <= 2; x++) {{
            vec2 o = vec2(float(x), float(y)) * LUMA_A_Q_pt;
            vec2 w = uv + o + d * LUMA_A_Q_pt;
            s += ba ? abs(LUMA_B_Q_tex(uv + o).r - LUMA_A_Q_tex(w).r) : abs(LUMA_A_Q_tex(uv + o).r - LUMA_B_Q_tex(w).r);
        }}
    return s + ALIAS_LAMBDA * (abs(d.x) + abs(d.y));
}}
float qrange(vec2 uv, bool ba) {{
    float lo = 1.0, hi = 0.0;
    for (int y = -2; y <= 2; y++)
        for (int x = -2; x <= 2; x++) {{
            vec2 o = vec2(float(x), float(y)) * LUMA_A_Q_pt;
            float l = ba ? LUMA_B_Q_tex(uv + o).r : LUMA_A_Q_tex(uv + o).r;
            lo = min(lo, l); hi = max(hi, l);
        }}
    return hi - lo;
}}
float cheb(vec2 v) {{ return max(abs(v.x), abs(v.y)); }}
// THE APERTURE (builds 5 and 6): the cell's stripe direction -- the structure tensor's minor eigenvector -- times
// sqrt(smoothstep(0.5, 0.9, coherence)); zero on isotropic texture. The scans and the pick ignore the component of a
// step along it: inside horizontal stripes x is unmeasurable, and at a pattern's end the background in the window
// pulls the RIGHT alias's x to junk while the wrong alias (the background mapped onto x-free bars) keeps x = 0 --
// compared as whole vectors, the right chain paid P2 at every junk step (tests/probes/limb/ownerdump.py, apcarry.py:
// B1 moving up 83% -> 99% offline). Build 6 reads the tensor over the 1/8 level's 5 x 5 window (40 px), not this
// level's (20 px): on a 2-D print of period 40 (the ladder's M2 texture, sin x sin y) half a period reads as stripes
// near its zero lines, and build 5 threw away a component those cells could measure (A6 -0.5, O5 -0.8 on the gate;
// tests/probes/limb/cases.sh). A 40-px window spans that period and still sees V3's and B1's bars as stripes.
vec2 aperture_w(vec2 uv, bool ba) {{
    float l[49];
    for (int j = 0; j < 49; j++) {{
        vec2 o = vec2(float(j % 7 - 3), float(j / 7 - 3)) * LUMA_A_E_pt;
        l[j] = ba ? LUMA_B_E_tex(uv + o).r : LUMA_A_E_tex(uv + o).r;
    }}
    float jxx = 0.0, jyy = 0.0, jxy = 0.0;
    for (int y = 1; y <= 5; y++)
        for (int x = 1; x <= 5; x++) {{
            float gx = 0.5 * (l[y * 7 + x + 1] - l[y * 7 + x - 1]);
            float gy = 0.5 * (l[(y + 1) * 7 + x] - l[(y - 1) * 7 + x]);
            jxx += gx * gx; jyy += gy * gy; jxy += gx * gy;
        }}
    float tr = jxx + jyy;
    if (tr < 1.0e-8) return vec2(0.0);
    float coh = sqrt((jxx - jyy) * (jxx - jyy) + 4.0 * jxy * jxy) / tr;
    float th = 0.5 * atan(2.0 * jxy, jxx - jyy);
    return vec2(-sin(th), cos(th)) * sqrt(smoothstep(0.5, 0.9, coh)) * {APERTURE};
}}
// the best lattice shift within +-2 of a 1/8-level basin doubled to this level's texels
vec2 refine(vec2 uv, vec2 s, bool ba, out float cbest) {{
    vec2 best = s;
    cbest = 1.0e30;
    for (int y = -2; y <= 2; y++)
        for (int x = -2; x <= 2; x++) {{
            vec2 d = s + vec2(float(x), float(y));
            float c = qsad(uv, d, ba);
            if (c < cbest) {{ cbest = c; best = d; }}
        }}
    return best;
}}
// returns (b2, D1, D2); b1 out
vec4 hypotheses(vec2 uv, vec4 bas, float me, bool ba, out vec2 b1) {{
    b1 = 2.0 * bas.xy;
    if (qrange(uv, ba) < 0.02) return vec4(b1, -1.0, {BIG});
    float c1, c2;
    b1 = refine(uv, 2.0 * bas.xy, ba, c1);
    if (me >= {M_MAX}) return vec4(b1, 0.0, {BIG});
    vec2 b2 = refine(uv, 2.0 * bas.zw, ba, c2);
    if (cheb(b2 - b1) < 1.5) return vec4(b1, 0.0, {BIG});
    float rise = 0.0;
    for (int k = 0; k < 8; k++) {{
        vec2 o = vec2(k == 0 || k == 4 || k == 5 ? 2.0 : k == 1 || k == 6 || k == 7 ? -2.0 : 0.0,
                      k == 2 || k == 4 || k == 6 ? 2.0 : k == 3 || k == 5 || k == 7 ? -2.0 : 0.0);
        rise += qsad(uv, (c1 <= c2 ? b1 : b2) + o, ba);
    }}
    float cm = min(c1, c2);
    float S = max(rise / 8.0 - cm, 1.0e-4);
    float ridge = max(qsad(uv, mix(b1, b2, 0.5), ba), max(qsad(uv, mix(b1, b2, 0.25), ba), qsad(uv, mix(b1, b2, 0.75), ba)));
    if (ridge - max(c1, c2) < 0.25 * S) return vec4(c1 <= c2 ? b1 : b2, 0.0, {BIG});
    float d1 = (c1 - cm) / S, d2 = (c2 - cm) / S;
    if (abs(c1 - c2) / S < {TAU}) {{ d1 = 0.0; d2 = 0.0; }}
    return vec4(b2, d1, d2);
}}
vec4 hook() {{
    ivec2 coord = ivec2(LUMA_A_Q_pos * LUMA_A_Q_size);
    if (!pair_changed)
        return imageLoad(ALIAS_Q_AB_ST, coord);
    vec2 uv = LUMA_A_Q_pos;
    ivec2 ec = ivec2(uv * ALIAS_E_AB_size);
    vec2 me = imageLoad(ALIAS_E_M_ST, ec).xy;
    vec2 b1ab, b1ba;
    vec4 ab = hypotheses(uv, imageLoad(ALIAS_E_AB_ST, ec), me.x, false, b1ab);
    vec4 ba = hypotheses(uv, imageLoad(ALIAS_E_BA_ST, ec), me.y, true, b1ba);
    // one basin: b1 is the anchor (a "no ridge" pair keeps the better of the two, in .xy)
    if (ab.w >= {HALF}) b1ab = ab.xy;
    if (ba.w >= {HALF}) b1ba = ba.xy;
    imageStore(ALIAS_Q_AB_ST, coord, ab);
    imageStore(ALIAS_Q_BA_ST, coord, ba);
    imageStore(ALIAS_Q1_AB_ST, coord, vec4(b1ab, aperture_w(uv, false)));
    imageStore(ALIAS_Q1_BA_ST, coord, vec4(b1ba, aperture_w(uv, true)));
    return ab;
}}
"""

SCAN = """
//!TEXTURE ALIAS_{AX}F_AB_ST
//!SIZE 960 540
//!FORMAT rgba32f
//!STORAGE

//!TEXTURE ALIAS_{AX}B_AB_ST
//!SIZE 960 540
//!FORMAT rgba32f
//!STORAGE

//!TEXTURE ALIAS_{AX}F_BA_ST
//!SIZE 960 540
//!FORMAT rgba32f
//!STORAGE

//!TEXTURE ALIAS_{AX}B_BA_ST
//!SIZE 960 540
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND ALIAS_Q1_AB_ST
//!BIND ALIAS_Q1_BA_ST
//!BIND ALIAS_Q_AB_ST
//!BIND ALIAS_Q_BA_ST
//!BIND ALIAS_{AX}F_AB_ST
//!BIND ALIAS_{AX}B_AB_ST
//!BIND ALIAS_{AX}F_BA_ST
//!BIND ALIAS_{AX}B_BA_ST
//!BIND LUMA_A_Q
//!SAVE ALIAS_{AX}_DONE
//!WIDTH {W}
//!HEIGHT {H}
//!COMPONENTS 1
//!DESC [alias] semi-global min-sum over each cell's hypotheses, {WHAT}: four invocations per {LINE} (forward and back, A->B and B->A)
// L(p, v) = D(p, v) + min_u [L(p - r, u) + pen(v, u)] - min_u L(p - r, u), in .xy for h1 and h2; each scan writes its
// own storage once and reads only the hypotheses, so no invocation reads what it wrote. A flat cell (.z = -1 in the
// hypotheses) passes nothing on. The penalty ignores a step's component along the stripes of the more coherent of
// the two cells (the aperture, build 5: ALIAS_Q1_*_ST.zw).
float pen(vec2 v, vec2 u, vec2 w) {{
    vec2 m = v - u;
    m -= dot(m, w) * w;
    float d = max(abs(m.x), abs(m.y));
    return d < 0.75 ? 0.0 : d < 1.75 ? {P1} : {P2};
}}
void scan(bool ba, int line, int n, bool back) {{
    vec2 Lp = vec2(0.0), hp1 = vec2(0.0), hp2 = vec2(0.0), wp = vec2(0.0);
    bool ok = false;
    for (int s = 0; s < n; s++) {{
        int i = back ? n - 1 - s : s;
        ivec2 c = {CELL};
        vec4 q1 = ba ? imageLoad(ALIAS_Q1_BA_ST, c) : imageLoad(ALIAS_Q1_AB_ST, c);
        vec2 h1 = q1.xy, wc = q1.zw, w = dot(wc, wc) >= dot(wp, wp) ? wc : wp;
        vec4 hy = ba ? imageLoad(ALIAS_Q_BA_ST, c) : imageLoad(ALIAS_Q_AB_ST, c);
        vec2 L;
        if (hy.z < 0.0) {{
            L = vec2(0.0, {BIG});
            ok = false;
        }} else {{
            L = hy.zw;
            if (ok) {{
                float mp = min(Lp.x, Lp.y);
                L.x += min(Lp.x + pen(h1, hp1, w), Lp.y + pen(h1, hp2, w)) - mp;
                L.y += min(Lp.x + pen(hy.xy, hp1, w), Lp.y + pen(hy.xy, hp2, w)) - mp;
            }}
            ok = true;
        }}
        L = min(L, vec2({BIG}));
        vec4 outv = vec4(L, 0.0, 0.0);
        if (ba) {{ if (back) imageStore(ALIAS_{AX}B_BA_ST, c, outv); else imageStore(ALIAS_{AX}F_BA_ST, c, outv); }}
        else    {{ if (back) imageStore(ALIAS_{AX}B_AB_ST, c, outv); else imageStore(ALIAS_{AX}F_AB_ST, c, outv); }}
        Lp = L; hp1 = h1; hp2 = hy.xy; wp = wc;
    }}
}}
vec4 hook() {{
    if (!pair_changed)
        return vec4(0.0);
    int line = int(gl_FragCoord.{LC});
    int which = int(gl_FragCoord.{WC});
    scan(which >= 2, line, int(LUMA_A_Q_size.{NC}), (which & 1) == 1);
    return vec4(0.0);
}}
"""

PICK = """
//!TEXTURE ALIAS_OUT_{D}_ST
//!SIZE 960 540
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_Q_{D}
//!BIND ALIAS_Q_{D}_ST
//!BIND ALIAS_Q1_{D}_ST
//!BIND ALIAS_HF_{D}_ST
//!BIND ALIAS_HB_{D}_ST
//!BIND ALIAS_VF_{D}_ST
//!BIND ALIAS_VB_{D}_ST
//!BIND ALIAS_H_DONE
//!BIND ALIAS_V_DONE
//!BIND ALIAS_OUT_{D}_ST
//!BIND LUMA_A_Q
//!SAVE FLOW_Q_{D}
//!WIDTH HOOKED.w 4 /
//!HEIGHT HOOKED.h 4 /
//!COMPONENTS 2
//!DESC [alias] each quarter-level cell takes its cheaper hypothesis over the four scans ({D})
vec4 hook() {{
    ivec2 coord = ivec2(LUMA_A_Q_pos * LUMA_A_Q_size);
    if (!pair_changed)
        return imageLoad(ALIAS_OUT_{D}_ST, coord);
    vec2 h = FLOW_Q_{D}_tex(LUMA_A_Q_pos).xy;
    vec4 hy = imageLoad(ALIAS_Q_{D}_ST, coord);
    vec4 q1 = imageLoad(ALIAS_Q1_{D}_ST, coord);
    vec2 b1 = q1.xy, w = q1.zw;
    vec4 result = vec4(h, 0.0, 0.0);
    if (hy.z >= 0.0 && hy.w < {HALF}) {{
        vec2 tot = imageLoad(ALIAS_HF_{D}_ST, coord).xy + imageLoad(ALIAS_HB_{D}_ST, coord).xy
                 + imageLoad(ALIAS_VF_{D}_ST, coord).xy + imageLoad(ALIAS_VB_{D}_ST, coord).xy - 3.0 * hy.zw;
        // The carry only SWITCHES ALIASES: in a TIED cell (both data costs exactly 0) whose own flow lies in one of its
        // two basins, it may move the flow to the other. Build 3 also replaced a flow that lay in neither basin, and an
        // untied cell's flow when the scans outvoted its margin: near a pattern's ends a cell's 1/8-level basins can
        // both be wrong, and the level's right flow was overwritten -- V1 and H1 fell from 55 to 34 dB, R3 -7.6.
        // Build 5, the aperture: membership and the switch are measured across the cell's stripes only, and a switched
        // flow keeps the level's own component along them (w = 0 on isotropic texture: build 4 exactly).
        vec2 pick = tot.y < tot.x - 1.0e-4 ? hy.xy : b1;
        vec2 e1 = b1 - h, e2 = hy.xy - h, mv = pick - h;
        e1 -= dot(e1, w) * w; e2 -= dot(e2, w) * w; mv -= dot(mv, w) * w;
        float in1 = max(abs(e1.x), abs(e1.y)), in2 = max(abs(e2.x), abs(e2.y));
        bool tied = hy.z == 0.0 && hy.w == 0.0;
        if (tied && min(in1, in2) < 1.5 && max(abs(mv.x), abs(mv.y)) >= 1.5) result = vec4(pick + dot(h - pick, w) * w, 0.0, 0.0);
    }}
    imageStore(ALIAS_OUT_{D}_ST, coord, result);
    return result;
}}
"""


def add_alias_carry(t, aperture=True):
    """aperture=False (ALIAS_APERTURE=0) stores a zero stripe direction: build 4's behaviour"""
    t = add_alias_e(t)
    # after the quarter level's B->A refine (the last pass that saves FLOW_Q_BA before the variational stage)
    _once(t, "//!DESC [high] refine flow B->A (1/4 res)\n", "the quarter B->A refine")
    i = t.index("//!DESC [high] refine flow B->A (1/4 res)\n")
    j = t.index("\n}\n", t.index("vec4 hook() {", i)) + 3
    k = t.index("//!HOOK FRAME_MIX", i)
    assert k >= j - 3, "alias carry: the B->A refine's hook() is not the pass's last function"
    body = HYP.format(LAMBDA=LAMBDA, BIG=f"{BIG:.1f}", M_MAX=f"{M_MAX:.2f}", TAU=f"{TAU_CARRY:.2f}", HALF=f"{BIG / 2:.1f}",
                      APERTURE="1.0" if aperture else "0.0")
    body += SCAN.format(AX="H", W="4", H="HOOKED.h 4 /", WHAT="along the rows", LINE="row",
                        CELL="ivec2(i, line)", LC="y", WC="x", NC="x", P1=P1, P2=P2, BIG=f"{BIG:.1f}")
    body += SCAN.format(AX="V", W="HOOKED.w 4 /", H="4", WHAT="along the columns", LINE="column",
                        CELL="ivec2(line, i)", LC="x", WC="y", NC="y", P1=P1, P2=P2, BIG=f"{BIG:.1f}")
    for d in ("AB", "BA"):
        body += PICK.format(D=d, HALF=f"{BIG / 2:.1f}")
    return t[:j] + body + t[j:]
