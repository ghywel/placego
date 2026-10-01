#!/usr/bin/env python3
"""THE FAST PRINT RE-SCORED ON ITS LATTICE: a switch for gen_variational.py (2026-10-01, ENERGY-TRANSFER.md lead 4, the
offline mechanism of steps 1j / 1k2 / 1n / 1o in tests/probes/weave/rescore1.py; NFRAME-LIMITS.md "The weave").

PRINT_LATTICE=1 -- at the 1/8 grid, after the carry's pick (and OUTLINE_ADOPT's passes when they are there), before the
variational iterations: a fine periodic print moving FAST, whose interior the pyramid locked one period away (the weave
at 11-19 px/frame: 98 percent of a box's core wrong), is re-scored at FULL resolution among the aliases its own lattice
predicts. Offline (rescore1.py, RESCORE_STEP=1k2 RESCORE_LATTICE=rival3 RESCORE_MENU=small RESCORE_SELF=sparse) the
fast weave's core goes from 98 to 13-23 percent wrong; noise and exact rotating prints are kept.
Seven passes per direction since 2026-10-01 (the same arithmetic split across threads, for the time; identical output):
  1. THE LATTICE (1/8 grid): where a cell moves (over 0.5 px), the 1/8 level's best-minus-rival offsets of the 5 x 5
     cells around it whose margin is under 0.3 (ALIAS_E's own basins and margins), 8 px a texel, sign-folded and
     de-duplicated within 4 px. Each is refined by the self-match of the source frame's own 32 x 32 neighbourhood (8 x 8
     samples at 4 px; +-4 px on a 2-px grid, then +-1 px) and kept under 0.3 of the samples' mean absolute deviation,
     and only as an ISOLATED minimum (8 neighbours at +-2 px cost at least max(2 c, c + 0.15 MAD): a stripe has none).
     The kept vectors are COMPLETED (a/2, a/3; (a +- b)/2, (a +- b)/3, a +- b, each reduced to its shortest coset
     representative, refined +-1 px, up to three rounds), and the basis is the shortest valid vector and the shortest
     valid one not collinear with it.
  2. THE RE-SCORE (1/8 grid): the menu is the 3 x 3 cells' DISTINCT flows (within 1 px) plus the nearest lattice steps
     (n, m in -1..1, within 45 px). Each candidate is ranked by the best 16 x 16 full-resolution SAD within +-0.5 px; the
     best, and the best more than 2 px from it, are refined +-1 px in half-pixel steps, and so is the cell's own flow.
     The pick replaces the flow only if it beats the flow AND the best of a different basin by 1/255 (an exact print's
     aliases tie, and the cell keeps its flow: the lossless fallback). Cached per source pair.
  3. APPLY (quarter level): the cell's 2 x 2 quarter texels take the picked vector.
Needs ALIAS_CARRY=1 (the 1/8-level basins pass that writes ALIAS_E_AB_ST, ALIAS_E_BA_ST and ALIAS_E_M_ST).
    print_lattice.add_print_lattice(t)
"""

PL_MOVING = 0.5           # px: a cell is moving
PL_MARGIN = 0.3           # the 1/8 level's rival-basin margin under which a cell's offset is a lattice candidate
PL_KEEP = 0.3             # a self-match under this fraction of the samples' MAD is a lattice vector
PL_PICK = 0.004           # 1/255: the pick's margin over the flow and over a different basin
PL_REACH = 45.0           # px: the menu's lattice points
PL_MAXO = 8               # offsets kept
PL_MAXV = 24              # lattice vectors kept
PL_MAXP = 96              # completion probes (all rounds; offline has no cap)
PL_MAXA = 48              # menu candidates
PL_EXT = 5                # (C4) a cell opens only if at least this many of its 5 x 5 cells have a low margin
PL_FUSE = True            # one pass per stage for both directions (the apply excepted): half the dispatches
PL_BUDGET = 4000.0        # the cost cap: opened cells per direction before only a stride grid runs (about 1/8 of 1080p)


def _once(t, a, what):
    n = t.count(a)
    assert n == 1, f"print lattice: {what}: anchor found {n} times"


PASSES = """
//!HOOK FRAME_MIX
//!BIND FLOW_Q_{D}
//!BIND LUMA_A_E
//!BIND ALIAS_E_{D}_ST
//!BIND ALIAS_E_M_ST
//!SAVE PLAT_G_{D}
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 1
//!DESC [print] the gate ({D}): the cells the print gate opens, flagged for the cost cap's count
vec2 pl_fold(vec2 q) {{ return (q.x < 0.0 || (q.x == 0.0 && q.y < 0.0)) ? -q : q; }}
vec4 hook() {{
    if (!pair_changed) return vec4(0.0);
    ivec2 cell = ivec2(gl_FragCoord.xy);
    vec2 w = FLOW_Q_{D}_tex((vec2(cell) + 0.5) / LUMA_A_E_size).xy * 4.0;
    if (length(w) <= {MOVING}) return vec4(0.0);
    // the offsets: 8 x (rival - best) of the 5 x 5 cells whose margin is under PL_MARGIN
    vec2 offs[{MAXO}];
    int no = 0, nlow = 0;
    ivec2 en = ivec2(LUMA_A_E_size);
    for (int y = -2; y <= 2; y++)
        for (int x = -2; x <= 2; x++) {{
            ivec2 e = cell + ivec2(x, y);
            if (e.x < 0 || e.y < 0 || e.x >= en.x || e.y >= en.y) continue;
            if (imageLoad(ALIAS_E_M_ST, e).{M} >= {MARGIN}) continue;
            nlow++;
            vec4 bas = imageLoad(ALIAS_E_{D}_ST, e);
            vec2 o = pl_fold(8.0 * (bas.zw - bas.xy));
            if (dot(o, o) == 0.0) continue;
            bool dup = false;
            for (int k = 0; k < no; k++) if (length(o - offs[k]) < 4.0) dup = true;
            if (!dup && no < {MAXO}) {{ offs[no] = o; no++; }}
        }}
    return vec4((no > 0 && nlow >= {EXT}) ? 1.0 : 0.0, 0.0, 0.0, 0.0);
}}

//!HOOK FRAME_MIX
//!BIND LUMA_A_E
//!BIND PLAT_G_{D}
//!SAVE PLAT_SR_{D}
//!WIDTH 1
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 1
//!DESC [print] the count ({D}), per row of cells
vec4 hook() {{
    if (!pair_changed) return vec4(0.0);
    ivec2 t = ivec2(gl_FragCoord.xy);
    float s = 0.0;
    for (int i = 0; i < int(LUMA_A_E_size.x); i++) s += PLAT_G_{D}_tex((vec2(float(i), float(t.y)) + 0.5) / LUMA_A_E_size).x;
    return vec4(s, 0.0, 0.0, 0.0);
}}

//!HOOK FRAME_MIX
//!BIND LUMA_A_E
//!BIND PLAT_SR_{D}
//!SAVE PLAT_SN_{D}
//!WIDTH 1
//!HEIGHT 1
//!COMPONENTS 1
//!DESC [print] the count ({D}), the frame's: over the budget, only a stride grid of cells runs the lattice
vec4 hook() {{
    if (!pair_changed) return vec4(0.0);
    float s = 0.0;
    for (int j = 0; j < int(LUMA_A_E_size.y); j++) s += PLAT_SR_{D}_tex(vec2(0.5, (float(j) + 0.5) / LUMA_A_E_size.y)).x;
    return vec4(s, 0.0, 0.0, 0.0);
}}

//!HOOK FRAME_MIX
//!BIND {FROMF}
//!BIND FLOW_Q_{D}
//!BIND LUMA_A_E
//!BIND ALIAS_E_{D}_ST
//!BIND ALIAS_E_M_ST
//!BIND PLAT_SN_{D}
//!SAVE PLAT_O_{D}
//!WIDTH HOOKED.w 8 / {MAXO} *
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 4
//!DESC [print] the lattice's offsets ({D}): one thread per offset, refined by a self-match
float pl_lum(vec2 p) {{ return dot({FROMF}_tex((p + 0.5) * {FROMF}_pt).rgb, vec3(0.299, 0.587, 0.114)); }}
vec2 pl_fold(vec2 q) {{ return (q.x < 0.0 || (q.x == 0.0 && q.y < 0.0)) ? -q : q; }}
// a lattice vector is an ISOLATED minimum of the self-match (step 1r): its 8 neighbours at +-2 px all cost at least
// max(2 c, c + 0.15 MAD) -- along a stripe the cost does not rise, so a one-dimensional print yields no such vector
bool pl_isolated(float c, vec2 v, float smp[64], vec2 b0, float mad) {{
    float nb = 1.0e30;
    for (int dy = -2; dy <= 2; dy += 2)
        for (int dx = -2; dx <= 2; dx += 2) {{
            if (dx == 0 && dy == 0) continue;
            float s = 0.0;
            for (int q = 0; q < 64; q++) s += abs(smp[q] - pl_lum(b0 + 4.0 * vec2(float(q % 8), float(q / 8)) + v + vec2(float(dx), float(dy))));
            nb = min(nb, s);
        }}
    return nb / 64.0 >= max(2.0 * c / 64.0, c / 64.0 + 0.15 * mad);
}}
vec4 hook() {{
    if (!pair_changed) return vec4(0.0);                  // unused: the re-score reuses its cached result
    ivec2 t = ivec2(gl_FragCoord.xy);                        // this pass's own texel: (cell, slot)
    ivec2 tc = ivec2(t.x / {MAXO}, t.y);                     // the COMPACT cell index (the cost cap's stride grid, packed)
    int slot = t.x - tc.x * {MAXO};
    int stride = int(ceil(sqrt(max(PLAT_SN_{D}_tex(vec2(0.5)).x / {BUDGET}, 1.0))));   // 1 under the budget
    ivec2 cell = tc * stride;                                 // the cell itself: over the budget only the grid's cells run,
    if (cell.x >= int(LUMA_A_E_size.x) || cell.y >= int(LUMA_A_E_size.y)) return vec4(0.0);   // packed, so the GPU's lanes stay full
    vec2 w = FLOW_Q_{D}_tex((vec2(cell) + 0.5) / LUMA_A_E_size).xy * 4.0;
    if (length(w) <= {MOVING}) return vec4(0.0);
    // the offsets: 8 x (rival - best) of the 5 x 5 cells whose margin is under PL_MARGIN
    vec2 offs[{MAXO}];
    int no = 0, nlow = 0;
    ivec2 en = ivec2(LUMA_A_E_size);
    for (int y = -2; y <= 2; y++)
        for (int x = -2; x <= 2; x++) {{
            ivec2 e = cell + ivec2(x, y);
            if (e.x < 0 || e.y < 0 || e.x >= en.x || e.y >= en.y) continue;
            if (imageLoad(ALIAS_E_M_ST, e).{M} >= {MARGIN}) continue;
            nlow++;
            vec4 bas = imageLoad(ALIAS_E_{D}_ST, e);
            vec2 o = pl_fold(8.0 * (bas.zw - bas.xy));
            if (dot(o, o) == 0.0) continue;
            bool dup = false;
            for (int k = 0; k < no; k++) if (length(o - offs[k]) < 4.0) dup = true;
            if (!dup && no < {MAXO}) {{ offs[no] = o; no++; }}
        }}
    if (slot >= no || nlow < {EXT}) return vec4(0.0);      // (C4) a print is extended: at least EXT of the 25 cells low
    int slot0 = slot;
    // the self-match: 8 x 8 samples at 4 px over the cell's 32 x 32 neighbourhood (the cell's centre is pixel corner 8 cell + 4)
    vec2 b0 = vec2(cell * 8 - 12);
    float smp[64];
    float mean = 0.0;
    for (int k = 0; k < 64; k++) {{ smp[k] = pl_lum(b0 + 4.0 * vec2(float(k % 8), float(k / 8))); mean += smp[k]; }}
    mean /= 64.0;
    float mad = 0.0;
    for (int k = 0; k < 64; k++) mad += abs(smp[k] - mean);
    mad /= 64.0;
    if (mad < 1.0e-3) return vec4(0.0);
    // +-4 px on a 2-px grid on 4 x 4 samples at 8 px (C5), then +-1 px on the 8 x 8
    vec2 best = vec2(0.0); float bc4 = 1.0e30;
    for (int sy = -4; sy <= 4; sy += 2)
        for (int sx = -4; sx <= 4; sx += 2) {{
            vec2 s = floor(offs[slot0] + 0.5) + vec2(float(sx), float(sy));
            if (dot(s, s) == 0.0) continue;
            float c = 0.0;
            for (int q = 0; q < 16; q++) {{
                int qq = (q / 4) * 16 + (q % 4) * 2;             // the 8 x 8's (2 qx, 2 qy): 8-px spacing
                c += abs(smp[qq] - pl_lum(b0 + 4.0 * vec2(float(qq % 8), float(qq / 8)) + s));
            }}
            if (c < bc4) {{ bc4 = c; best = s; }}
        }}
    float bc = 1.0e30;
    vec2 c0 = best;
    for (int sy = -1; sy <= 1; sy++)
        for (int sx = -1; sx <= 1; sx++) {{
            vec2 s = c0 + vec2(float(sx), float(sy));
            if (dot(s, s) == 0.0) continue;
            float c = 0.0;
            for (int q = 0; q < 64; q++) c += abs(smp[q] - pl_lum(b0 + 4.0 * vec2(float(q % 8), float(q / 8)) + s));
            if (c < bc) {{ bc = c; best = s; }}
        }}
    if (bc / 64.0 < {KEEP} * mad && pl_isolated(bc, best, smp, b0, mad)) return vec4(pl_fold(best), 1.0, 0.0);
    return vec4(0.0);
}}

//!HOOK FRAME_MIX
//!BIND {FROMF}
//!BIND LUMA_A_E
//!BIND PLAT_O_{D}
//!BIND PLAT_SN_{D}
//!SAVE PLAT_L_{D}
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 4
//!DESC [print] the lattice ({D}): the refined offsets gathered, completed, reduced to a basis
float pl_lum(vec2 p) {{ return dot({FROMF}_tex((p + 0.5) * {FROMF}_pt).rgb, vec3(0.299, 0.587, 0.114)); }}
vec2 pl_fold(vec2 q) {{ return (q.x < 0.0 || (q.x == 0.0 && q.y < 0.0)) ? -q : q; }}
// a lattice vector is an ISOLATED minimum of the self-match (step 1r): its 8 neighbours at +-2 px all cost at least
// max(2 c, c + 0.15 MAD) -- along a stripe the cost does not rise, so a one-dimensional print yields no such vector
bool pl_isolated(float c, vec2 v, float smp[64], vec2 b0, float mad) {{
    float nb = 1.0e30;
    for (int dy = -2; dy <= 2; dy += 2)
        for (int dx = -2; dx <= 2; dx += 2) {{
            if (dx == 0 && dy == 0) continue;
            float s = 0.0;
            for (int q = 0; q < 64; q++) s += abs(smp[q] - pl_lum(b0 + 4.0 * vec2(float(q % 8), float(q / 8)) + v + vec2(float(dx), float(dy))));
            nb = min(nb, s);
        }}
    return nb / 64.0 >= max(2.0 * c / 64.0, c / 64.0 + 0.15 * mad);
}}
vec4 hook() {{
    if (!pair_changed) return vec4(0.0);
    ivec2 tc = ivec2(gl_FragCoord.xy);                        // compact (see the offsets pass)
    int stride = int(ceil(sqrt(max(PLAT_SN_{D}_tex(vec2(0.5)).x / {BUDGET}, 1.0))));
    ivec2 cell = tc * stride;
    if (cell.x >= int(LUMA_A_E_size.x) || cell.y >= int(LUMA_A_E_size.y)) return vec4(0.0);
    vec2 vec[{MAXV}];
    int nv = 0;
    for (int s = 0; s < {MAXO}; s++) {{                       // in slot order: the serial form's order, so the same list
        vec4 r = PLAT_O_{D}_tex((vec2(float(tc.x * {MAXO} + s), float(tc.y)) + 0.5) * PLAT_O_{D}_pt);
        if (r.z < 0.5 || nv >= {MAXV}) continue;
        bool dup = false;
        for (int j = 0; j < nv; j++) if (length(r.xy - vec[j]) < 0.5) dup = true;
        if (!dup) {{ vec[nv] = r.xy; nv++; }}
    }}
    if (nv == 0) return vec4(0.0);
    // the self-match: 8 x 8 samples at 4 px over the cell's 32 x 32 neighbourhood (the cell's centre is pixel corner 8 cell + 4)
    vec2 b0 = vec2(cell * 8 - 12);
    float smp[64];
    float mean = 0.0;
    for (int k = 0; k < 64; k++) {{ smp[k] = pl_lum(b0 + 4.0 * vec2(float(k % 8), float(k / 8))); mean += smp[k]; }}
    mean /= 64.0;
    float mad = 0.0;
    for (int k = 0; k < 64; k++) mad += abs(smp[k] - mean);
    mad /= 64.0;
    if (mad < 1.0e-3) return vec4(0.0);
    // COMPLETION: the short representatives of a/2, a/3 and, for each non-collinear pair, (a +- b)/2, (a +- b)/3, a +- b
    vec2 probed[{MAXP}];
    int np = 0;
    for (int round = 0; round < 3; round++) {{
        vec2 cand[{MAXP}];
        int nc = 0;
        for (int a = 0; a < nv && nc < {MAXP}; a++) {{
            cand[nc] = vec[a] / 2.0; nc++;
            if (nc < {MAXP}) {{ cand[nc] = vec[a] / 3.0; nc++; }}
        }}
        for (int a = 0; a < nv; a++)
            for (int b = a + 1; b < nv; b++) {{
                vec2 A = vec[a], B = vec[b];
                if (abs(A.x * B.y - A.y * B.x) < 1.0e-6) continue;
                for (int f = 0; f < 6 && nc < {MAXP}; f++) {{
                    vec2 c = f == 0 ? (A + B) / 2.0 : f == 1 ? (A - B) / 2.0 : f == 2 ? (A + B) / 3.0
                           : f == 3 ? (A - B) / 3.0 : f == 4 ? A - B : A + B;
                    vec2 r = c; float rl = length(c);
                    for (int n = -1; n <= 1; n++)
                        for (int m = -1; m <= 1; m++) {{
                            vec2 z = c + float(n) * A + float(m) * B;
                            if (length(z) < rl) {{ rl = length(z); r = z; }}
                        }}
                    cand[nc] = r; nc++;
                }}
            }}
        int added = 0;
        for (int k = 0; k < nc; k++) {{
            vec2 q = pl_fold(floor(cand[k] + 0.5));
            float ql = length(q);
            if (ql < 8.0 || ql > 40.0) continue;
            bool seen = false;
            for (int j = 0; j < nv; j++) if (length(q - vec[j]) < 2.0) seen = true;
            for (int j = 0; j < np; j++) if (length(q - probed[j]) < 2.0) seen = true;
            if (seen || np >= {MAXP}) continue;
            probed[np] = q; np++;
            vec2 best = q; float bc = 1.0e30;
            for (int sy = -1; sy <= 1; sy++)
                for (int sx = -1; sx <= 1; sx++) {{
                    vec2 s = q + vec2(float(sx), float(sy));
                    float c = 0.0;
                    for (int t = 0; t < 64; t++) c += abs(smp[t] - pl_lum(b0 + 4.0 * vec2(float(t % 8), float(t / 8)) + s));
                    if (c < bc) {{ bc = c; best = s; }}
                }}
            if (bc / 64.0 < {KEEP} * mad && nv < {MAXV} && pl_isolated(bc, best, smp, b0, mad)) {{ vec[nv] = pl_fold(best); nv++; added++; }}
        }}
        if (added == 0) break;
    }}
    // the basis: the shortest valid vector, and the shortest valid one not collinear with it
    int i1 = 0;
    for (int k = 1; k < nv; k++) if (length(vec[k]) < length(vec[i1])) i1 = k;
    vec2 p1 = vec[i1], p2 = vec2(0.0);
    float l2 = 1.0e30;
    for (int k = 0; k < nv; k++) {{
        if (abs(p1.x * vec[k].y - p1.y * vec[k].x) <= 1.0e-6) continue;
        if (length(vec[k]) < l2) {{ l2 = length(vec[k]); p2 = vec[k]; }}
    }}
    return vec4(p1, p2);
}}

//!TEXTURE PLAT_T_{D}_ST
//!SIZE 1920 270
//!FORMAT rgba32f
//!STORAGE

//!TEXTURE PLAT_K_{D}_ST
//!SIZE 1920 270
//!FORMAT rgba32f
//!STORAGE

//!TEXTURE PLAT_F_{D}_ST
//!SIZE 7200 270
//!FORMAT rgba32f
//!STORAGE

//!TEXTURE PLAT_R_{D}_ST
//!SIZE 480 270
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND {FROMF}
//!BIND {TOF}
//!BIND FLOW_Q_{D}
//!BIND LUMA_A_E
//!BIND PLAT_L_{D}
//!BIND PLAT_SN_{D}
//!BIND PLAT_T_{D}_ST
//!SAVE PLAT_M_{D}
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 4
//!DESC [print] the menu ({D}): the 3 x 3 cells' distinct flows plus the nearest lattice steps, its best four by a cheap SAD
float pr_lum_a(vec2 p) {{ return dot({FROMF}_tex((p + 0.5) * {FROMF}_pt).rgb, vec3(0.299, 0.587, 0.114)); }}
float pr_lum_b(vec2 p) {{ return dot({TOF}_tex((p + 0.5) * {TOF}_pt).rgb, vec3(0.299, 0.587, 0.114)); }}
vec4 hook() {{
    if (!pair_changed) return vec4(0.0);                  // unused: the decision reuses its cached result
    ivec2 tc = ivec2(gl_FragCoord.xy);                        // compact (see the offsets pass)
    int stride = int(ceil(sqrt(max(PLAT_SN_{D}_tex(vec2(0.5)).x / {BUDGET}, 1.0))));
    ivec2 cell = tc * stride;
    if (cell.x >= int(LUMA_A_E_size.x) || cell.y >= int(LUMA_A_E_size.y)) return vec4(0.0);
    vec2 w = FLOW_Q_{D}_tex((vec2(cell) + 0.5) / LUMA_A_E_size).xy * 4.0;
    vec4 lat = PLAT_L_{D}_tex((vec2(tc) + 0.5) / LUMA_A_E_size);
    if (!(length(w) > {MOVING} && dot(lat.xy, lat.xy) > 0.0)) return vec4(0.0);   // inactive: no slot is read
    for (int s = 0; s < 4; s++) imageStore(PLAT_T_{D}_ST, ivec2(tc.x * 4 + s, tc.y), vec4(0.0, 0.0, -1.0, 0.0));
    vec2 b0 = vec2(cell * 8 - 4);                            // the 16 x 16 block around the cell's centre (pixel corner 8 cell + 4)
    float blk16[16];                                          // (C1) its 4 x 4 samples at 4 px
    for (int k = 0; k < 16; k++) {{
        int kk = (k / 4) * 64 + (k % 4) * 4;
        blk16[k] = pr_lum_a(b0 + vec2(float(kk % 16), float(kk / 16)));
    }}
        // the menu: the 3 x 3 cells' distinct moving flows, plus the nearest lattice steps
        vec2 seeds[9];
        int ns = 0;
        ivec2 en = ivec2(LUMA_A_E_size);
        for (int y = -1; y <= 1; y++)
            for (int x = -1; x <= 1; x++) {{
                ivec2 e = cell + ivec2(x, y);
                if (e.x < 0 || e.y < 0 || e.x >= en.x || e.y >= en.y) continue;
                vec2 s = FLOW_Q_{D}_tex((vec2(e) + 0.5) / LUMA_A_E_size).xy * 4.0;
                if (length(s) <= {MOVING}) continue;
                bool dup = false;
                for (int k = 0; k < ns; k++) if (length(s - seeds[k]) < 1.0) dup = true;
                if (!dup) {{ seeds[ns] = s; ns++; }}
            }}
        vec2 alts[{MAXA}];
        int na = 0;
        for (int k = 0; k < ns; k++)
            for (int n = -1; n <= 1; n++)
                for (int m = -1; m <= 1; m++) {{
                    vec2 q = float(n) * lat.xy + float(m) * lat.zw;
                    if (length(q) > {REACH}) continue;
                    vec2 c = seeds[k] + q;
                    if (length(c - w) <= 1.5) continue;
                    bool dup = false;
                    for (int j = 0; j < na; j++) if (length(c - alts[j]) < 1.0) dup = true;
                    if (!dup && na < {MAXA}) {{ alts[na] = c; na++; }}
                }}
        // (C1) the cheap first stage over the whole menu, +-0.5 px; the best four, in rank order, to the next pass
        int top[4];
        float topc[4];
        for (int s = 0; s < 4; s++) {{ top[s] = -1; topc[s] = 1.0e30; }}
        for (int j = 0; j < na; j++) {{
            float bc = 1.0e30;
            for (int dy = -1; dy <= 1; dy++)
                for (int dx = -1; dx <= 1; dx++) {{
                    vec2 d = alts[j] + 0.5 * vec2(float(dx), float(dy));
                    float c = 0.0;
                    for (int k = 0; k < 16; k++) {{
                        int kk = (k / 4) * 64 + (k % 4) * 4;
                        c += abs(blk16[k] - pr_lum_b(b0 + vec2(float(kk % 16), float(kk / 16)) + d));
                    }}
                    bc = min(bc, c);
                }}
            for (int s = 0; s < 4; s++)
                if (bc < topc[s]) {{
                    for (int u = 3; u > s; u--) {{ top[u] = top[u - 1]; topc[u] = topc[u - 1]; }}
                    top[s] = j; topc[s] = bc;
                    break;
                }}
        }}
        for (int s = 0; s < 4; s++)
            if (top[s] >= 0) imageStore(PLAT_T_{D}_ST, ivec2(tc.x * 4 + s, tc.y), vec4(alts[top[s]], float(top[s]), 1.0));
    return vec4(w, 1.0, 0.0);
}}

//!HOOK FRAME_MIX
//!BIND {FROMF}
//!BIND {TOF}
//!BIND LUMA_A_E
//!BIND PLAT_M_{D}
//!BIND PLAT_SN_{D}
//!BIND PLAT_T_{D}_ST
//!BIND PLAT_K_{D}_ST
//!SAVE PLAT_KD_{D}
//!WIDTH HOOKED.w 8 / 4 *
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 1
//!DESC [print] the rank ({D}): one thread per offered candidate, the best full SAD within +-0.5 px
float pr_lum_a(vec2 p) {{ return dot({FROMF}_tex((p + 0.5) * {FROMF}_pt).rgb, vec3(0.299, 0.587, 0.114)); }}
float pr_lum_b(vec2 p) {{ return dot({TOF}_tex((p + 0.5) * {TOF}_pt).rgb, vec3(0.299, 0.587, 0.114)); }}
vec4 hook() {{
    if (!pair_changed) return vec4(0.0);
    ivec2 t = ivec2(gl_FragCoord.xy);
    if (t.x / 4 >= int(LUMA_A_E_size.x)) return vec4(0.0);
    if (PLAT_M_{D}_tex((vec2(float(t.x / 4), float(t.y)) + 0.5) / LUMA_A_E_size).z < 0.5) return vec4(0.0);   // inactive
    vec4 cd = imageLoad(PLAT_T_{D}_ST, t);
    if (cd.w < 0.5) {{ imageStore(PLAT_K_{D}_ST, t, vec4(0.0, 0.0, 1.0e30, -1.0)); return vec4(0.0); }}
    ivec2 cell = ivec2(t.x / 4, t.y) * int(ceil(sqrt(max(PLAT_SN_{D}_tex(vec2(0.5)).x / {BUDGET}, 1.0))));   // the cell itself (the thread is compact)
    vec2 b0 = vec2(cell * 8 - 4);
    float blk[256];
    for (int k = 0; k < 256; k++) blk[k] = pr_lum_a(b0 + vec2(float(k % 16), float(k / 16)));
    float bc = 1.0e30;
    for (int dy = -1; dy <= 1; dy++)
        for (int dx = -1; dx <= 1; dx++) {{
            vec2 d = cd.xy + 0.5 * vec2(float(dx), float(dy));
            float c = 0.0;
            for (int k = 0; k < 256; k++) c += abs(blk[k] - pr_lum_b(b0 + vec2(float(k % 16), float(k / 16)) + d));
            bc = min(bc, c);
        }}
    imageStore(PLAT_K_{D}_ST, t, vec4(cd.xy, bc, cd.z));
    return vec4(0.0);
}}

//!HOOK FRAME_MIX
//!BIND {FROMF}
//!BIND {TOF}
//!BIND LUMA_A_E
//!BIND PLAT_M_{D}
//!BIND PLAT_KD_{D}
//!BIND PLAT_SN_{D}
//!BIND PLAT_K_{D}_ST
//!BIND PLAT_F_{D}_ST
//!SAVE PLAT_FD_{D}
//!WIDTH HOOKED.w 8 / 15 *
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 1
//!DESC [print] the refine ({D}): one thread per (candidate, row), +-1 px in half-pixel steps
float pr_lum_a(vec2 p) {{ return dot({FROMF}_tex((p + 0.5) * {FROMF}_pt).rgb, vec3(0.299, 0.587, 0.114)); }}
float pr_lum_b(vec2 p) {{ return dot({TOF}_tex((p + 0.5) * {TOF}_pt).rgb, vec3(0.299, 0.587, 0.114)); }}
vec4 hook() {{
    if (!pair_changed) return vec4(0.0);
    ivec2 t = ivec2(gl_FragCoord.xy);
    ivec2 cell = ivec2(t.x / 15, t.y);                        // compact here: the decision's pass reads it by this index
    if (cell.x >= int(LUMA_A_E_size.x)) return vec4(0.0);
    int r = t.x - cell.x * 15, which = r / 5, dy = r - which * 5 - 2;
    ivec2 real = cell * int(ceil(sqrt(max(PLAT_SN_{D}_tex(vec2(0.5)).x / {BUDGET}, 1.0))));   // the cell itself, for the frame's samples
    // the two offered, as the serial form chose them: the best rank (rank order breaks ties), and the best of a
    // different basin (menu order breaks ties)
    vec4 m = PLAT_M_{D}_tex((vec2(cell) + 0.5) / LUMA_A_E_size);
    float r1 = 1.0e30; int s1 = -1; vec4 k1 = vec4(0.0);
    if (m.z > 0.5)
        for (int s = 0; s < 4; s++) {{
            vec4 k = imageLoad(PLAT_K_{D}_ST, ivec2(cell.x * 4 + s, cell.y));
            if (k.w < 0.0) continue;
            if (k.z < r1) {{ r1 = k.z; s1 = s; k1 = k; }}
        }}
    float r2 = 1.0e30, j2 = 1.0e30; int s2 = -1; vec4 k2 = vec4(0.0);
    if (s1 >= 0)
        for (int s = 0; s < 4; s++) {{
            if (s == s1) continue;
            vec4 k = imageLoad(PLAT_K_{D}_ST, ivec2(cell.x * 4 + s, cell.y));
            if (k.w < 0.0 || length(k.xy - k1.xy) <= 2.0) continue;
            if (k.z < r2 || (k.z == r2 && k.w < j2)) {{ r2 = k.z; j2 = k.w; s2 = s; k2 = k; }}
        }}
    vec4 n = vec4(m.xy, s1 >= 0 ? 1.0 : 0.0, s2 >= 0 ? 1.0 : 0.0);
    vec4 a = vec4(k1.xy, k2.xy);
    if (n.z < 0.5 || (which == 2 && n.w < 0.5)) return vec4(0.0);   // inactive, or no second candidate: never read
    vec2 d0 = which == 0 ? n.xy : which == 1 ? a.xy : a.zw;
    vec2 b0 = vec2(real * 8 - 4);
    float blk[256];
    for (int k = 0; k < 256; k++) blk[k] = pr_lum_a(b0 + vec2(float(k % 16), float(k / 16)));
    vec2 best = d0; float bc = 1.0e30;
    for (int dx = -2; dx <= 2; dx++) {{
        vec2 d = d0 + 0.5 * vec2(float(dx), float(dy));
        float c = 0.0;
        for (int k = 0; k < 256; k++) c += abs(blk[k] - pr_lum_b(b0 + vec2(float(k % 16), float(k / 16)) + d));
        if (c < bc) {{ bc = c; best = d; }}
    }}
    imageStore(PLAT_F_{D}_ST, t, vec4(best, bc, 1.0));
    return vec4(0.0);
}}

//!HOOK FRAME_MIX
//!BIND LUMA_A_E
//!BIND PLAT_M_{D}
//!BIND PLAT_K_{D}_ST
//!BIND PLAT_FD_{D}
//!BIND PLAT_F_{D}_ST
//!BIND PLAT_R_{D}_ST
//!SAVE PLAT_R_{D}
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 4
//!DESC [print] the decision ({D}): the pick only if it beats the flow and the best of a different basin by 1/255
vec4 hook() {{
    ivec2 cell = ivec2(gl_FragCoord.xy);
    if (!pair_changed) return imageLoad(PLAT_R_{D}_ST, cell);
    vec4 result = vec4(0.0);
    // the two offered, as the serial form chose them: the best rank (rank order breaks ties), and the best of a
    // different basin (menu order breaks ties)
    vec4 m = PLAT_M_{D}_tex((vec2(cell) + 0.5) / LUMA_A_E_size);
    float r1 = 1.0e30; int s1 = -1; vec4 k1 = vec4(0.0);
    if (m.z > 0.5)
        for (int s = 0; s < 4; s++) {{
            vec4 k = imageLoad(PLAT_K_{D}_ST, ivec2(cell.x * 4 + s, cell.y));
            if (k.w < 0.0) continue;
            if (k.z < r1) {{ r1 = k.z; s1 = s; k1 = k; }}
        }}
    float r2 = 1.0e30, j2 = 1.0e30; int s2 = -1; vec4 k2 = vec4(0.0);
    if (s1 >= 0)
        for (int s = 0; s < 4; s++) {{
            if (s == s1) continue;
            vec4 k = imageLoad(PLAT_K_{D}_ST, ivec2(cell.x * 4 + s, cell.y));
            if (k.w < 0.0 || length(k.xy - k1.xy) <= 2.0) continue;
            if (k.z < r2 || (k.z == r2 && k.w < j2)) {{ r2 = k.z; j2 = k.w; s2 = s; k2 = k; }}
        }}
    vec4 n = vec4(m.xy, s1 >= 0 ? 1.0 : 0.0, s2 >= 0 ? 1.0 : 0.0);
    vec4 a = vec4(k1.xy, k2.xy);
    if (n.z > 0.5) {{
        vec2 sc_v[3];
        float sc_c[3];
        int nsc = 0;
        for (int which = 0; which < 3; which++) {{
            if (which == 2 && n.w < 0.5) continue;
            vec2 best = vec2(0.0); float bc = 1.0e30;
            for (int r = 0; r < 5; r++) {{                      // the rows in order: the serial form's first minimum
                vec4 f = imageLoad(PLAT_F_{D}_ST, ivec2(cell.x * 15 + which * 5 + r, cell.y));
                if (f.z < bc) {{ bc = f.z; best = f.xy; }}
            }}
            sc_v[nsc] = best; sc_c[nsc] = bc / 256.0; nsc++;
        }}
        int ib = 0;
        for (int k = 1; k < nsc; k++) if (sc_c[k] < sc_c[ib]) ib = k;
        bool ok = sc_c[ib] <= sc_c[0] - {PICK};
        float rival = 1.0e30;
        for (int k = 0; k < nsc; k++)
            if (k != ib && length(sc_v[k] - sc_v[ib]) > 2.0) rival = min(rival, sc_c[k]);
        ok = ok && sc_c[ib] <= rival - {PICK};
        if (ok) result = vec4(sc_v[ib], 1.0, 0.0);
    }}
    imageStore(PLAT_R_{D}_ST, cell, result);
    return result;
}}

//!TEXTURE PLAT_P_{D}_ST
//!SIZE 480 270
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND {FROMF}
//!BIND {TOF}
//!BIND FLOW_Q_{D}
//!BIND LUMA_A_E
//!BIND PLAT_G_{D}
//!BIND PLAT_SN_{D}
//!BIND PLAT_R_{D}
//!BIND PLAT_P_{D}_ST
//!SAVE PLAT_P_{D}
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!COMPONENTS 4
//!DESC [print] the borrowing ({D}): over the budget, an opened cell off the grid tries its grid neighbours' lattice steps
float pp_lum_a(vec2 p) {{ return dot({FROMF}_tex((p + 0.5) * {FROMF}_pt).rgb, vec3(0.299, 0.587, 0.114)); }}
float pp_lum_b(vec2 p) {{ return dot({TOF}_tex((p + 0.5) * {TOF}_pt).rgb, vec3(0.299, 0.587, 0.114)); }}
vec4 hook() {{
    ivec2 cell = ivec2(gl_FragCoord.xy);
    if (!pair_changed) return imageLoad(PLAT_P_{D}_ST, cell);
    vec2 uv = (vec2(cell) + 0.5) / LUMA_A_E_size;
    int stride = int(ceil(sqrt(max(PLAT_SN_{D}_tex(vec2(0.5)).x / {BUDGET}, 1.0))));
    bool ongrid = cell.x % stride == 0 && cell.y % stride == 0;
    vec4 result = ongrid ? PLAT_R_{D}_tex((vec2(cell / stride) + 0.5) / LUMA_A_E_size) : vec4(0.0);   // compact index
    if (stride > 1 && (cell.x % stride != 0 || cell.y % stride != 0) && PLAT_G_{D}_tex(uv).x > 0.5) {{
        vec2 w = FLOW_Q_{D}_tex(uv).xy * 4.0;
        vec2 b0 = vec2(cell * 8 - 4);
        float blk[256];
        for (int k = 0; k < 256; k++) blk[k] = pp_lum_a(b0 + vec2(float(k % 16), float(k / 16)));
        // the candidates: w plus the lattice step of each corner of this cell's stride block that made a pick
        ivec2 a0 = (cell / stride) * stride;
        ivec2 en = ivec2(LUMA_A_E_size);
        vec2 cand[4];
        float cheap[4];
        int nc = 0;
        for (int q = 0; q < 4; q++) {{
            ivec2 a = a0 + stride * ivec2(q % 2, q / 2);
            if (a.x >= en.x || a.y >= en.y) continue;
            vec2 ua = (vec2(a) + 0.5) / LUMA_A_E_size;
            vec4 ra = PLAT_R_{D}_tex((vec2(a / stride) + 0.5) / LUMA_A_E_size);   // its decision, by compact index
            if (ra.z < 0.5) continue;
            vec2 c = w + (ra.xy - FLOW_Q_{D}_tex(ua).xy * 4.0);
            if (length(c - w) <= 1.5) continue;
            bool dup = false;
            for (int j = 0; j < nc; j++) if (length(c - cand[j]) < 1.0) dup = true;
            if (dup) continue;
            float cc = 0.0;                                   // ranked cheaply: 4 x 4 samples, at the candidate itself
            for (int k = 0; k < 16; k++) {{
                int kk = (k / 4) * 64 + (k % 4) * 4;
                cc += abs(blk[kk] - pp_lum_b(b0 + vec2(float(kk % 16), float(kk / 16)) + c));
            }}
            cand[nc] = c; cheap[nc] = cc; nc++;
        }}
        if (nc > 0) {{
            int i1 = 0;
            for (int j = 1; j < nc; j++) if (cheap[j] < cheap[i1]) i1 = j;
            int i2 = -1;
            for (int j = 0; j < nc; j++) if (j != i1 && length(cand[j] - cand[i1]) > 2.0 && (i2 < 0 || cheap[j] < cheap[i2])) i2 = j;
            // the full SAD within +-0.5 px for the flow, the best borrowed step and a different basin's best
            vec2 bv[3]; float bcst[3];
            for (int which = 0; which < 3; which++) {{
                if (which == 2 && i2 < 0) {{ bcst[2] = 1.0e30; bv[2] = w; continue; }}
                vec2 d0 = which == 0 ? w : which == 1 ? cand[i1] : cand[i2];
                float bc = 1.0e30; vec2 best = d0;
                for (int dy = -1; dy <= 1; dy++)
                    for (int dx = -1; dx <= 1; dx++) {{
                        vec2 d = d0 + 0.5 * vec2(float(dx), float(dy));
                        float c = 0.0;
                        for (int k = 0; k < 256; k++) c += abs(blk[k] - pp_lum_b(b0 + vec2(float(k % 16), float(k / 16)) + d));
                        if (c < bc) {{ bc = c; best = d; }}
                    }}
                bv[which] = best; bcst[which] = bc / 256.0;
            }}
            if (bcst[1] <= bcst[0] - {PICK} && bcst[1] <= bcst[2] - {PICK}) result = vec4(bv[1], 1.0, 0.0);
        }}
    }}
    imageStore(PLAT_P_{D}_ST, cell, result);
    return result;
}}

//!HOOK FRAME_MIX
//!BIND FLOW_Q_{D}
//!BIND LUMA_A_E
//!BIND PLAT_P_{D}
//!SAVE FLOW_Q_{D}
//!WIDTH HOOKED.w 4 /
//!HEIGHT HOOKED.h 4 /
//!COMPONENTS 2
//!DESC [print] apply ({D}): each cell's two by two quarter texels take its re-scored vector
vec4 hook() {{
    vec2 h = FLOW_Q_{D}_tex(FLOW_Q_{D}_pos).xy;
    ivec2 cell = ivec2(gl_FragCoord.xy) / 2;
    vec4 r = PLAT_P_{D}_tex((vec2(cell) + 0.5) / LUMA_A_E_size);
    return vec4(r.z > 0.5 ? r.xy * 0.25 : h, 0.0, 0.0);
}}
"""


FUSED = ("PLAT_G", "PLAT_SR", "PLAT_SN", "PLAT_O", "PLAT_L", "PLAT_M", "PLAT_KD", "PLAT_FD", "PLAT_R", "PLAT_P")
# each fused pass's per-direction width (the first half's), as GLSL
FACTOR = {"PLAT_G": "int(LUMA_A_E_size.x)", "PLAT_SR": "1", "PLAT_SN": "1", "PLAT_O": f"int(LUMA_A_E_size.x) * {PL_MAXO}",
          "PLAT_L": "int(LUMA_A_E_size.x)", "PLAT_M": "int(LUMA_A_E_size.x)", "PLAT_KD": "int(LUMA_A_E_size.x) * 4",
          "PLAT_FD": "int(LUMA_A_E_size.x) * 15", "PLAT_R": "int(LUMA_A_E_size.x)", "PLAT_P": "int(LUMA_A_E_size.x)"}


def _passes(t):
    """split a pass list into [(header lines, body)] at each //!HOOK"""
    out = []
    for chunk in t.split("//!HOOK FRAME_MIX\n")[1:]:
        lines = chunk.split("\n")
        n = 0
        while n < len(lines) and lines[n].startswith("//!"): n += 1
        out.append((lines[:n], "\n".join(lines[n:])))
    return out


def _fuse(ab, ba):
    """ONE pass for both directions (2026-10-01, for the time: the passes run on every output frame, so their count is the
    floor on real footage). The texel's half of the output picks the direction; the two bodies are the per-direction
    passes' own text, their functions suffixed, gl_FragCoord replaced by the half's own coordinate; a fused texture is
    read through plat_*_ab / plat_*_ba (its two halves side by side, each the per-direction texture's width)."""
    import re
    pre = ("TEXTURE", "SIZE", "FORMAT", "STORAGE")
    texs, hooks = "", []
    TEX = re.compile(r"//!TEXTURE \w+\n//!SIZE \d+ \d+\n//!FORMAT \w+\n//!STORAGE\n\n?")
    for src in (ab, ba):
        texs += "".join(m.group(0).rstrip("\n") + "\n\n" for m in TEX.finditer(src))   # the storage, declared up front
        hooks.append(_passes(TEX.sub("", src)))
    out = ""
    for i in range(len(hooks[0])):
        (ha, ba_), (hb, bb) = hooks[0][i], hooks[1][i]
        save = [l for l in ha if l.startswith("//!SAVE ")][0].split()[1]
        if save.startswith("FLOW_Q_"):                      # the apply passes stay one per direction (two SAVE targets)
            for hh, bd, d in ((ha, ba_, "AB"), (hb, bb, "BA")):
                binds, helper, body = [], "", bd
                for l in hh:
                    if not l.startswith("//!BIND "): continue
                    b = l.split()[1]
                    f = next((f for f in FUSED if b == f + "_" + d), None)
                    if f:
                        binds.append("//!BIND " + f)
                        body = body.replace(f"{f}_{d}_tex(", f"{f.lower()}_{d.lower()}(")
                        helper += (f"vec4 {f.lower()}_{d.lower()}(vec2 uv) {{ return {f}_tex(vec2(uv.x * 0.5"
                                   f"{' + 0.5' if d == 'BA' else ''}, uv.y)); }}\n")
                    else:
                        binds.append(l)
                rest = [l for l in hh if not l.startswith("//!BIND ")]
                out += "//!HOOK FRAME_MIX\n" + "\n".join(binds + rest) + "\n" + helper + body
            continue
        base = save[:-3]
        assert base in FUSED, base
        binds = []
        for l in ha + hb:
            if l.startswith("//!BIND "):
                b = l.split()[1]
                for f in FUSED:
                    if b in (f + "_AB", f + "_BA"): b = f
                if "//!BIND " + b not in binds: binds.append("//!BIND " + b)
        w = [l for l in ha if l.startswith("//!WIDTH ")][0] + " 2 *"
        h = [l for l in ha if l.startswith("//!HEIGHT ")][0]
        c = [l for l in ha if l.startswith("//!COMPONENTS ")][0]
        desc = [l for l in ha if l.startswith("//!DESC ")][0].replace("(AB)", "(AB and BA, fused)")
        bodies = []
        for bd, d in ((ba_, "ab"), (bb, "ba")):
            names = sorted(set(re.findall(r"\b(?:float|vec2|vec4|bool)\s+(\w+)\s*\(", bd)))
            for nme in names: bd = re.sub(r"\b%s\b" % nme, nme + "_" + d, bd)
            bd = bd.replace("gl_FragCoord.xy", "pl_frag")
            for f in FUSED:
                D = d.upper()
                bd = bd.replace(f"{f}_{D}_tex(", f"{f.lower()}_{d}(")
                bd = bd.replace(f"{f}_{D}_pt", f"({f}_pt * vec2(2.0, 1.0))")
            bodies.append(bd)
        helpers = ""
        for b in binds:
            nm = b.split()[1]
            if nm in FUSED:
                helpers += (f"vec4 {nm.lower()}_ab(vec2 uv) {{ return {nm}_tex(vec2(uv.x * 0.5, uv.y)); }}\n"
                            f"vec4 {nm.lower()}_ba(vec2 uv) {{ return {nm}_tex(vec2(uv.x * 0.5 + 0.5, uv.y)); }}\n")
        disp = ("vec4 hook() {\n"
                f"    int w1 = {FACTOR[base]};\n"
                "    if (gl_FragCoord.x < float(w1)) { pl_frag = gl_FragCoord.xy; return hook_ab(); }\n"
                "    pl_frag = gl_FragCoord.xy - vec2(float(w1), 0.0);\n"
                "    return hook_ba();\n"
                "}\n")
        if "//!BIND LUMA_A_E" not in binds: binds.append("//!BIND LUMA_A_E")
        out += ("//!HOOK FRAME_MIX\n" + "\n".join(binds) + f"\n//!SAVE {base}\n{w}\n{h}\n{c}\n{desc}\n"
                + "vec2 pl_frag;                                              // this direction's own texel (the half's coordinate)\n"
                + helpers
                + bodies[0].rstrip("\n") + "\n" + bodies[1].rstrip("\n") + "\n" + disp + "\n")
    return texs + out


def add_print_lattice(t):
    """after the outline adoption's passes when present, else after the carry's BA pick (the last passes that save
    FLOW_Q_AB / FLOW_Q_BA before the variational stage)"""
    _once(t, "//!TEXTURE ALIAS_E_M_ST\n", "the 1/8-level basins' margins (needs ALIAS_CARRY=1)")
    anchor = "//!DESC [adopt] a locked print adopts its outline's motion (BA)\n"
    if anchor not in t:
        anchor = "//!DESC [alias] each quarter-level cell takes its cheaper hypothesis over the four scans (BA)\n"
    _once(t, anchor, "the last quarter-level pass before the variational")
    i = t.index(anchor)
    j = t.index("\n//!HOOK FRAME_MIX", i) + 1
    per = []
    for d, m, fr, to in (("AB", "x", "HOOKED", "NEXT"), ("BA", "y", "NEXT", "HOOKED")):
        per.append(PASSES.format(D=d, M=m, FROMF=fr, TOF=to, MOVING=f"{PL_MOVING:.2f}", MARGIN=f"{PL_MARGIN:.2f}",
                                 KEEP=f"{PL_KEEP:.2f}", PICK=f"{PL_PICK:.4f}", REACH=f"{PL_REACH:.1f}", MAXO=PL_MAXO,
                                 MAXV=PL_MAXV, MAXP=PL_MAXP, MAXA=PL_MAXA, EXT=PL_EXT,
                                 BUDGET=f"{PL_BUDGET:.1f}"))
    body = _fuse(per[0], per[1]) if PL_FUSE else per[0] + per[1]
    return t[:j] + body + t[j:]
