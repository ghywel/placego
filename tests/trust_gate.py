#!/usr/bin/env python3
"""THE PER-LEVEL TRUST GATE: a switch for gen_variational.py (2026-10-01, ENERGY-TRANSFER.md "The per-level trust gate,
returned to"; NFRAME-LIMITS.md section 8's lead, first built here).

TRUST_GATE=1 -- at the quarter level, after the carry's pick and before the outline adoption and the lattice: where the
1/8 level is AMBIGUOUS (at least 5 of the 5 x 5 cells around have a rival basin within a margin of 0.3: the print's
signature, the lattice's own gate), the 1/16 and 1/8 levels' seeds are not trusted. On a fine print they are a moire
moving at its own speed, or the print one period away (T0: every 1/16 seed wrong at every speed on the weave box). The
quarter level, the first that sees a 10-16 px print unaliased (T1), is searched WIDE instead, and full resolution
decides. Offline (tests/probes/trust/wide.py, RANK=full): the truth on 98-100 percent of the weave box's core at every
speed from 3 to 19 px/frame; noise 99.9-100.
Two passes per direction:
  1. THE OFFER AND THE DECISION (1/8 grid, one thread per cell): every whole quarter texel within +-6 (+-24 px), the
     5 x 5 window's mean absolute difference at the cell's quarter texel plus TG_LAMBDA per px (a light small-motion
     prior: 0.002 drags noise, T2); its three best DISTINCT local minima (at least 2 texels apart) are offered, with
     the cell's own flow, to the 16 x 16 block centred on the cell at full resolution, each over +-0.5 px in half-pixel
     steps. The best replaces the flow only if it beats the flow's own score by TG_PICK (1/255 a pixel): the flow is
     kept on a tie, the lossless fallback. Cached per source pair.
  2. APPLY (quarter level): the cell's 2 x 2 quarter texels take the decided vector where the gate opened.
Needs ALIAS_CARRY=1 (the 1/8-level basins' margins, ALIAS_E_M_ST).
    trust_gate.add_trust_gate(t)
"""

TG_EXT = 5                # cells of the 5 x 5 whose 1/8-level rival-basin margin is under TG_MARGIN
TG_MARGIN = 0.3
TG_R = 6                  # quarter texels: the offer's reach (+-24 px)
TG_LAMBDA = 0.0005        # the offer's small-motion prior, per px, on the window's mean absolute difference
TG_PICK = 0.004           # 1/255: the decision's margin over the flow, a pixel's mean absolute difference
# TRUST_DECIDE=two (a cost cut, 2026-10-01): the decision scores every candidate at its own position first, and only the
# best and the cell's own flow are refined over +-0.5 px (5,120 samples a cell against 9,216). Default: full.
import os
TG_DECIDE = os.environ.get("TRUST_DECIDE", "full")
# TRUST_OFFER=parab (2026-10-01, after trust2's K1 miss): each offered minimum carries its parabola's sub-texel position in x
# and y (from its two neighbours' costs, clipped to half a texel), as the offline emulation's offer did. Default: whole.
TG_OFFER = os.environ.get("TRUST_OFFER", "whole")
# TRUST_UNIQUE=1 (2026-10-01, after trust1's ladder: V3 -11.0, R3 -8.9 on EXACT prints): lead 4's step 1d, which trust1
# left out -- the winner must also beat the best candidate of a DIFFERENT basin (more than 2 px from it) by TG_PICK, so on
# an exact print, whose aliases tie, the cell keeps its flow. Default: off (trust1's form).
TG_UNIQUE = os.environ.get("TRUST_UNIQUE", "0") == "1"
# TRUST_ALIAS=<tau> (2026-10-01, after R3: ambiguity alone opens the gate on exact prints the 1/8 level sees honestly): the
# gate opens only where the 1/8 level is also ALIASED around the cell -- over its 5 x 5 window, the range of the
# box-filtered values (each texel's 8 x 8 footprint averaged; one pass per frame) under tau of the range of the point
# samples the level actually uses (T1's flag A; tau 0.7: the weave 100 percent, a period-40 print and the stairs 0, film a
# median 14). The parked design's own flag. Default: off.
TG_ALIAS = float(os.environ["TRUST_ALIAS"]) if os.environ.get("TRUST_ALIAS") else None


def _once(t, a, what):
    n = t.count(a)
    assert n == 1, f"trust gate: {what}: anchor found {n} times"


PASSES = """
//!TEXTURE TG_{D}_ST
//!SIZE 480 270
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND {FROMF}
//!BIND {TOF}
//!BIND FLOW_Q_{D}
//!BIND {LA}
//!BIND {LB}
//!BIND LUMA_A_E
//!BIND ALIAS_E_M_ST
//!BIND TG_{D}_ST
//!SAVE TG_{D}
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 4
//!DESC [trust] the first honest level ({D}): where the 1/8 level is ambiguous, the quarter level offers its three best minima within +-24 px and full resolution decides
float tg_lum_a(vec2 p) {{ return dot({FROMF}_tex((p + 0.5) * {FROMF}_pt).rgb, vec3(0.299, 0.587, 0.114)); }}
float tg_lum_b(vec2 p) {{ return dot({TOF}_tex((p + 0.5) * {TOF}_pt).rgb, vec3(0.299, 0.587, 0.114)); }}
{OFFER}
vec4 hook() {{
    ivec2 cell = ivec2(gl_FragCoord.xy);
    if (!pair_changed) return imageLoad(TG_{D}_ST, cell);
    vec4 result = vec4(0.0);                               // .z = 0: the gate is shut and the flow stands
    // THE GATE: the 1/8 level ambiguous here (the print's signature)
    int nlow = 0;
    ivec2 en = ivec2(LUMA_A_E_size);
    for (int y = -2; y <= 2; y++)
        for (int x = -2; x <= 2; x++) {{
            ivec2 e = cell + ivec2(x, y);
            if (e.x < 0 || e.y < 0 || e.x >= en.x || e.y >= en.y) continue;
            if (imageLoad(ALIAS_E_M_ST, e).{M} < {MARGIN}) nlow++;
        }}
    if (nlow < {EXT}) {{ imageStore(TG_{D}_ST, cell, result); return result; }}
{ALIASGATE}    // THE OFFER: every whole quarter texel within +-{R}, at the cell's first quarter texel
    vec2 qc = (vec2(cell * 2) + 0.5) * {LA}_pt;
    float a25[25];
    for (int k = 0; k < 25; k++) a25[k] = {LA}_tex(qc + vec2(float(k % 5 - 2), float(k / 5 - 2)) * {LA}_pt).r;
    float c[{N}];
    for (int j = 0; j < {N}; j++) {{
        vec2 d = vec2(float(j % {S} - {R}), float(j / {S} - {R}));
        float s = 0.0;
        for (int k = 0; k < 25; k++)
            s += abs(a25[k] - {LB}_tex(qc + (vec2(float(k % 5 - 2), float(k / 5 - 2)) + d) * {LA}_pt).r);
        c[j] = s / 25.0 + {LAMBDA} * 4.0 * length(d);
    }}
    int pk[3];
    pk[0] = -1; pk[1] = -1; pk[2] = -1;
    for (int n = 0; n < 3; n++) {{
        float bc = 1.0e30;
        int bi = -1;
        for (int j = 0; j < {N}; j++) {{
            if (c[j] >= bc) continue;
            ivec2 p = ivec2(j % {S}, j / {S});
            bool lm = true;                                // a local minimum of the 3 x 3 inside the grid
            for (int dy = -1; dy <= 1; dy++)
                for (int dx = -1; dx <= 1; dx++) {{
                    ivec2 q = p + ivec2(dx, dy);
                    if ((dx == 0 && dy == 0) || q.x < 0 || q.y < 0 || q.x >= {S} || q.y >= {S}) continue;
                    if (c[q.y * {S} + q.x] < c[j]) lm = false;
                }}
            if (!lm) continue;
            bool far = true;                               // distinct from those already offered
            for (int m = 0; m < 3; m++)
                if (m < n && pk[m] >= 0 && max(abs(pk[m] % {S} - p.x), abs(pk[m] / {S} - p.y)) < 2) far = false;
            if (!far) continue;
            bc = c[j]; bi = j;
        }}
        pk[n] = bi;
    }}
    // THE DECISION: the 16 x 16 block centred on the cell at full resolution, the offered minima and the cell's own flow
    vec2 h = FLOW_Q_{D}_tex(qc).xy * 4.0;                  // px
    vec2 b0 = vec2(cell * 8 - 4);
    float blk[256];
    for (int k = 0; k < 256; k++) blk[k] = tg_lum_a(b0 + vec2(float(k % 16), float(k / 16)));
{DECIDE}    if ({ACCEPT}) result = vec4(bv * 0.25, 1.0, 0.0);   // quarter texels; the gate opened and decided
    imageStore(TG_{D}_ST, cell, result);
    return result;
}}

//!HOOK FRAME_MIX
//!BIND FLOW_Q_{D}
//!BIND TG_{D}
//!BIND LUMA_A_Q
//!SAVE FLOW_Q_{D}
//!WIDTH HOOKED.w 4 /
//!HEIGHT HOOKED.h 4 /
//!COMPONENTS 2
//!DESC [trust] apply ({D}): each cell's two by two quarter texels take its decided vector
vec4 hook() {{
    ivec2 q = ivec2(LUMA_A_Q_pos * LUMA_A_Q_size);
    vec4 t = TG_{D}_tex((vec2(q / 2) + 0.5) * TG_{D}_pt);
    return vec4(t.z > 0.5 ? t.xy : FLOW_Q_{D}_tex(LUMA_A_Q_pos).xy, 0.0, 0.0);
}}
"""


BOX = """
//!HOOK FRAME_MIX
//!BIND {F}
//!SAVE TG_BOX_{X}
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 1
//!DESC [trust] frame {X}'s 1/8 level box-filtered: each texel's 8 x 8 footprint averaged (the aliasing flag's reference)
vec4 hook() {{
    vec2 base = floor(gl_FragCoord.xy) * 8.0;
    float s = 0.0;
    for (int j = 0; j < 4; j++)
        for (int i = 0; i < 4; i++)                        // a pixel corner: the bilinear tap is the 2 x 2 pixels' mean
            s += dot({F}_tex((base + vec2(2.0 * float(i) + 1.0, 2.0 * float(j) + 1.0)) * {F}_pt).rgb, vec3(0.299, 0.587, 0.114));
    return vec4(s / 16.0, 0.0, 0.0, 0.0);
}}
"""
ALIASGATE = """    // THE FLAG: the 1/8 level ALIASED here (its box-filtered range under {TAU} of its point-sampled range, 5 x 5 cells)
    {{
        float plo = 1.0, phi = 0.0, blo = 1.0, bhi = 0.0;
        for (int y = -2; y <= 2; y++)
            for (int x = -2; x <= 2; x++) {{
                ivec2 e = clamp(cell + ivec2(x, y), ivec2(0), en - 1);
                vec2 uv = (vec2(e) + 0.5) / vec2(en);
                float pv = {LE}_tex(uv).r, bv0 = TG_BOX_{X}_tex(uv).r;
                plo = min(plo, pv); phi = max(phi, pv); blo = min(blo, bv0); bhi = max(bhi, bv0);
            }}
        if (phi - plo < 0.02 || bhi - blo >= {TAU} * (phi - plo)) {{ imageStore(TG_{D}_ST, cell, result); return result; }}
    }}
"""
DECIDE_UNIQUE = """    float hs = 1.0e30, bs = 1.0e30;
    vec2 bv = h;
    float cs[4];
    vec2 cp[4];
    int ncand = 0;
    for (int n = -1; n < 3; n++) {{
        vec2 cv;
        if (n < 0) cv = h;
        else {{
            if (pk[n] < 0) continue;
            cv = {CAND};
        }}
        float cb = 1.0e30;
        vec2 cbv = cv;
        for (int dy = -1; dy <= 1; dy++)
            for (int dx = -1; dx <= 1; dx++) {{
                vec2 d = cv + 0.5 * vec2(float(dx), float(dy));
                float s = 0.0;
                for (int k = 0; k < 256; k++) s += abs(blk[k] - tg_lum_b(b0 + vec2(float(k % 16), float(k / 16)) + d));
                s /= 256.0;
                if (s < cb) {{ cb = s; cbv = d; }}
            }}
        if (n < 0) hs = cb;
        cs[ncand] = cb; cp[ncand] = cbv; ncand++;
        if (cb < bs) {{ bs = cb; bv = cbv; }}
    }}
    // the uniqueness test (lead 4's step 1d): the best of a DIFFERENT basin, more than 2 px from the winner
    float ru = 1.0e30;
    for (int m = 0; m < 4; m++) {{
        if (m >= ncand) break;
        vec2 e = abs(cp[m] - bv);
        if (max(e.x, e.y) > 2.0) ru = min(ru, cs[m]);
    }}
"""
OFFER_PARAB = """// an offered minimum, in px: its quarter texel plus the parabola through its neighbours' costs in x and in y (a
// neighbour outside the grid: that axis stays whole), clipped to half a texel
vec2 tg_offer(float c[{N}], int j) {{
    ivec2 p = ivec2(j % {S}, j / {S});
    vec2 sub = vec2(0.0);
    if (p.x > 0 && p.x < {S} - 1) {{
        float lo = c[j - 1], hi = c[j + 1], den = lo - 2.0 * c[j] + hi;
        if (den > 1.0e-9) sub.x = clamp(0.5 * (lo - hi) / den, -0.5, 0.5);
    }}
    if (p.y > 0 && p.y < {S} - 1) {{
        float lo = c[j - {S}], hi = c[j + {S}], den = lo - 2.0 * c[j] + hi;
        if (den > 1.0e-9) sub.y = clamp(0.5 * (lo - hi) / den, -0.5, 0.5);
    }}
    return 4.0 * (vec2(p - ivec2({R})) + sub);
}}"""
DECIDE_FULL = """    float hs = 1.0e30, bs = 1.0e30;
    vec2 bv = h;
    for (int n = -1; n < 3; n++) {{
        vec2 cv;
        if (n < 0) cv = h;
        else {{
            if (pk[n] < 0) continue;
            cv = {CAND};
        }}
        for (int dy = -1; dy <= 1; dy++)
            for (int dx = -1; dx <= 1; dx++) {{
                vec2 d = cv + 0.5 * vec2(float(dx), float(dy));
                float s = 0.0;
                for (int k = 0; k < 256; k++) s += abs(blk[k] - tg_lum_b(b0 + vec2(float(k % 16), float(k / 16)) + d));
                s /= 256.0;
                if (n < 0) hs = min(hs, s);
                if (s < bs) {{ bs = s; bv = d; }}
            }}
    }}
"""
DECIDE_TWO = """    // two stages: every candidate at its own position, then the best and the flow over +-0.5 px
    vec2 cvs[4];
    cvs[0] = h;
    int nc = 1;
    for (int n = 0; n < 3; n++)
        if (pk[n] >= 0) {{ cvs[nc] = {CAND}; nc++; }}
    float b1 = 1.0e30;
    int bi = 0;
    for (int n = 0; n < 4; n++) {{
        if (n >= nc) break;
        float s = 0.0;
        for (int k = 0; k < 256; k++) s += abs(blk[k] - tg_lum_b(b0 + vec2(float(k % 16), float(k / 16)) + cvs[n]));
        if (s < b1) {{ b1 = s; bi = n; }}
    }}
    float hs = 1.0e30, bs = 1.0e30;
    vec2 bv = h;
    for (int m = 0; m < 2; m++) {{
        if (m == 1 && bi == 0) break;
        vec2 cv = m == 0 ? h : cvs[bi];
        for (int dy = -1; dy <= 1; dy++)
            for (int dx = -1; dx <= 1; dx++) {{
                vec2 d = cv + 0.5 * vec2(float(dx), float(dy));
                float s = 0.0;
                for (int k = 0; k < 256; k++) s += abs(blk[k] - tg_lum_b(b0 + vec2(float(k % 16), float(k / 16)) + d));
                s /= 256.0;
                if (m == 0) hs = min(hs, s);
                if (s < bs) {{ bs = s; bv = d; }}
            }}
    }}
"""


def add_trust_gate(t):
    """at the pass right after the carry's BA pick: before the outline adoption's passes when they are there"""
    _once(t, "//!TEXTURE ALIAS_E_M_ST\n", "the 1/8-level basins' margins (needs ALIAS_CARRY=1)")
    anchor = "//!DESC [alias] each quarter-level cell takes its cheaper hypothesis over the four scans (BA)\n"
    _once(t, anchor, "the carry's BA pick")
    i = t.index(anchor)
    j = t.index("\n//!HOOK FRAME_MIX", i) + 1
    k = t.find("\n//!TEXTURE", i)
    if 0 <= k < j: j = k + 1                               # before any textures the next passes declare
    S = 2 * TG_R + 1
    body = ""
    for d, m, fr, to, la, lb in (("AB", "x", "HOOKED", "NEXT", "LUMA_A_Q", "LUMA_B_Q"),
                                 ("BA", "y", "NEXT", "HOOKED", "LUMA_B_Q", "LUMA_A_Q")):
        assert not (TG_UNIQUE and TG_DECIDE == "two"), "TRUST_UNIQUE is built on the full decision"
        p = PASSES.replace("{DECIDE}", DECIDE_UNIQUE if TG_UNIQUE else DECIDE_TWO if TG_DECIDE == "two" else DECIDE_FULL)
        p = p.replace("{ACCEPT}", "bs < hs - {PICK} && bs < ru - {PICK}" if TG_UNIQUE else "bs < hs - {PICK}")
        if TG_ALIAS is not None:
            x, le = ("A", "LUMA_A_E") if d == "AB" else ("B", "LUMA_B_E")
            p = p.replace("{ALIASGATE}", ALIASGATE.replace("{X}", x).replace("{LE}", le).replace("{TAU}", f"{TG_ALIAS:.2f}"))
            extra = (f"//!BIND {le}\n" if le != "LUMA_A_E" else "") + f"//!BIND TG_BOX_{x}\n"   # LUMA_A_E is bound already
            assert p.count("//!BIND ALIAS_E_M_ST\n//!BIND TG_{D}_ST\n") == 1
            p = p.replace("//!BIND ALIAS_E_M_ST\n//!BIND TG_{D}_ST\n", "//!BIND ALIAS_E_M_ST\n//!BIND TG_{D}_ST\n" + extra)
        else:
            p = p.replace("{ALIASGATE}", "")
        if TG_OFFER == "parab":
            p = p.replace("{OFFER}\n", OFFER_PARAB + "\n").replace("{CAND}", "tg_offer(c, pk[n])")
        else:                                              # the whole texel, inline (the form trust1 was gated as)
            p = p.replace("{OFFER}\n", "").replace("{CAND}", "4.0 * vec2(float(pk[n] % {S} - {R}), float(pk[n] / {S} - {R}))")
        body += p.format(D=d, M=m, FROMF=fr, TOF=to, LA=la, LB=lb, MARGIN=f"{TG_MARGIN:.2f}", EXT=TG_EXT, R=TG_R,
                         S=S, N=S * S, LAMBDA=f"{TG_LAMBDA:.6f}", PICK=f"{TG_PICK:.4f}")
    if TG_ALIAS is not None:
        body = BOX.format(F="HOOKED", X="A") + BOX.format(F="NEXT", X="B") + body
    return t[:j] + body + t[j:]
