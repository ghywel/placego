#!/usr/bin/env python3
"""THE OUTLINE ADOPTED BY A LOCKED PRINT: a switch for gen_variational.py (2026-09-30, ENERGY-TRANSFER.md "The shared
stage", stage v2 in GLSL; NFRAME-LIMITS.md "The weave").

OUTLINE_ADOPT=1 -- at the quarter level, after the carry's pick and before the variational iterations, a fine periodic
print whose interior the pyramid locked one period away (the weave: 89% of a slow box's interior wrong at 5 px/frame)
adopts its OUTLINE's motion. The outline is where the print meets something else, and there the quarter level reads
the truth. Offline this is stage v2 (tests/probes/weave/unwrap.py UNWRAP_FORM=6 UNWRAP_WIDE=30 UNWRAP_CENTRE=cell):
the slow weave's core 72 -> 2.2 / 90 -> 9 percent, noise untouched, an independent patch inside the print untouched.
Six passes per direction (the wide sum separable, 2026-09-30 after A5's timing):
  1. ANCHORS (quarter res): a moving texel (over 0.5 px) with a still texel within 16 px -- a moving region's boundary.
  2. HISTOGRAMS (a 32-px coarse grid x 65 one-pixel bins): each coarse cell's anchors' flow components, counted.
  3. THE REFERENCE (the coarse grid): each coarse cell's histograms summed over +-8 coarse cells (+-256 px) and the
     median read off the cumulative counts, per component; with the anchors' count.
  4. ADOPT (quarter res): only where the 1/8 level's cost curve holds a RIVAL basin within margin 0.3 (ALIAS_E's own
     margins, grown by one cell: the print's signature; noise and a plain moving object have none), and only for a
     moving texel: the coarse cell's reference, refined +-1 px in half-pixel steps by a 5 x 5 quarter-level SAD,
     replaces the texel's flow only where it differs by more than 2 px AND matches the frames no worse.
Needs ALIAS_PRIOR=1 or ALIAS_CARRY=1 (the 1/8-level basins pass that writes ALIAS_E_M_ST).
    outline_adopt.add_outline_adopt(t)
"""

ADOPT_MOVING = 0.5        # px: a texel is moving
ADOPT_STILL_R = 4         # quarter texels (16 px): a still texel this near makes a moving one an anchor
ADOPT_BINS = 65           # one-pixel bins over -32..+32 px
ADOPT_WIDE = 8            # coarse cells (32 px): the reference's reach, +-256 px
ADOPT_MARGIN = 0.3        # the 1/8 level's rival-basin margin under which a texel is a print's
ADOPT_MIN_ANCHORS = 8.0   # fewer anchors within reach: no reference, no adoption
ADOPT_DIFF = 2.0          # px: the reference must differ by more than this to replace


def _once(t, a, what):
    n = t.count(a)
    assert n == 1, f"outline adopt: {what}: anchor found {n} times"


PASSES = """
//!HOOK FRAME_MIX
//!BIND FLOW_Q_{D}
//!SAVE ADOPT_ANCH_{D}
//!WIDTH HOOKED.w 4 /
//!HEIGHT HOOKED.h 4 /
//!COMPONENTS 1
//!DESC [adopt] anchors ({D}): a moving quarter texel with a still one within 16 px
vec4 hook() {{
    if (!pair_changed) return vec4(0.0);                  // unused: the adopt pass reuses its cached result
    vec2 uv = FLOW_Q_{D}_pos;
    float m = length(FLOW_Q_{D}_tex(uv).xy * 4.0);
    if (m <= {MOVING}) return vec4(0.0);
    for (int y = -{STILL_R}; y <= {STILL_R}; y++)
        for (int x = -{STILL_R}; x <= {STILL_R}; x++) {{
            vec2 p = uv + vec2(float(x), float(y)) * FLOW_Q_{D}_pt;
            if (length(FLOW_Q_{D}_tex(p).xy * 4.0) <= {MOVING}) return vec4(1.0);
        }}
    return vec4(0.0);
}}

//!HOOK FRAME_MIX
//!BIND FLOW_Q_{D}
//!BIND ADOPT_ANCH_{D}
//!SAVE ADOPT_HIST_{D}
//!WIDTH HOOKED.w 31 + 32 / {BINS} *
//!HEIGHT HOOKED.h 31 + 32 /
//!COMPONENTS 2
//!DESC [adopt] histograms ({D}): each 32-px cell's anchors' flow components in one-pixel bins
vec4 hook() {{
    if (!pair_changed) return vec4(0.0);
    ivec2 t = ivec2(gl_FragCoord.xy);                        // this pass's own texel (its output has no _pos)
    int cx = t.x / {BINS}, b = t.x - cx * {BINS};
    float cntx = 0.0, cnty = 0.0;
    for (int y = 0; y < 8; y++)
        for (int x = 0; x < 8; x++) {{
            vec2 p = (vec2(float(cx * 8 + x), float(t.y * 8 + y)) + 0.5) * FLOW_Q_{D}_pt;
            if (p.x >= 1.0 || p.y >= 1.0 || ADOPT_ANCH_{D}_tex(p).r < 0.5) continue;
            vec2 f = clamp(round(FLOW_Q_{D}_tex(p).xy * 4.0), -32.0, 32.0) + 32.0;
            if (int(f.x) == b) cntx += 1.0;
            if (int(f.y) == b) cnty += 1.0;
        }}
    return vec4(cntx, cnty, 0.0, 0.0);
}}

//!HOOK FRAME_MIX
//!BIND ADOPT_HIST_{D}
//!SAVE ADOPT_HSUM_{D}
//!WIDTH HOOKED.w 31 + 32 / {BINS} *
//!HEIGHT HOOKED.h 31 + 32 /
//!COMPONENTS 2
//!DESC [adopt] the wide sum along the rows ({D}): each bin over +-{WIDE} coarse cells (separable: the same sums)
vec4 hook() {{
    if (!pair_changed) return vec4(0.0);
    ivec2 t = ivec2(gl_FragCoord.xy);
    ivec2 n = ivec2(ADOPT_HIST_{D}_size) / ivec2({BINS}, 1);
    int cx = t.x / {BINS}, b = t.x - cx * {BINS};
    vec2 s = vec2(0.0);
    for (int i = max(cx - {WIDE}, 0); i <= min(cx + {WIDE}, n.x - 1); i++)
        s += ADOPT_HIST_{D}_tex((vec2(float(i * {BINS} + b), float(t.y)) + 0.5) * ADOPT_HIST_{D}_pt).xy;
    return vec4(s, 0.0, 0.0);
}}

//!HOOK FRAME_MIX
//!BIND ADOPT_HSUM_{D}
//!SAVE ADOPT_VSUM_{D}
//!WIDTH HOOKED.w 31 + 32 / {BINS} *
//!HEIGHT HOOKED.h 31 + 32 /
//!COMPONENTS 2
//!DESC [adopt] the wide sum along the columns ({D})
vec4 hook() {{
    if (!pair_changed) return vec4(0.0);
    ivec2 t = ivec2(gl_FragCoord.xy);
    ivec2 n = ivec2(ADOPT_HSUM_{D}_size) / ivec2({BINS}, 1);
    vec2 s = vec2(0.0);
    for (int j = max(t.y - {WIDE}, 0); j <= min(t.y + {WIDE}, n.y - 1); j++)
        s += ADOPT_HSUM_{D}_tex((vec2(float(t.x), float(j)) + 0.5) * ADOPT_HSUM_{D}_pt).xy;
    return vec4(s, 0.0, 0.0);
}}

//!HOOK FRAME_MIX
//!BIND ADOPT_VSUM_{D}
//!SAVE ADOPT_REF_{D}
//!WIDTH HOOKED.w 31 + 32 /
//!HEIGHT HOOKED.h 31 + 32 /
//!COMPONENTS 4
//!DESC [adopt] the reference ({D}): the anchors' median within +-256 px of each 32-px cell
vec4 hook() {{
    if (!pair_changed) return vec4(0.0);
    ivec2 c = ivec2(gl_FragCoord.xy);                        // this pass's own coarse cell
    float hx[{BINS}], hy[{BINS}];
    float tot = 0.0;
    for (int b = 0; b < {BINS}; b++) {{                       // the window's sums, already summed by the two passes above
        vec2 h = ADOPT_VSUM_{D}_tex((vec2(float(c.x * {BINS} + b), float(c.y)) + 0.5) * ADOPT_VSUM_{D}_pt).xy;
        hx[b] = h.x; hy[b] = h.y;
    }}
    for (int b = 0; b < {BINS}; b++) tot += hx[b];
    if (tot < {MIN_ANCHORS}) return vec4(0.0, 0.0, tot, 0.0);
    float mx = 0.0, my = 0.0, sx = 0.0, sy = 0.0;
    bool dx = false, dy = false;
    for (int b = 0; b < {BINS}; b++) {{
        sx += hx[b]; sy += hy[b];
        if (!dx && sx >= 0.5 * tot) {{ mx = float(b) - 32.0; dx = true; }}
        if (!dy && sy >= 0.5 * tot) {{ my = float(b) - 32.0; dy = true; }}
    }}
    return vec4(mx, my, tot, 1.0);
}}

//!TEXTURE ADOPT_OUT_{D}_ST
//!SIZE 960 540
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND FLOW_Q_{D}
//!BIND ADOPT_REF_{D}
//!BIND ALIAS_E_M_ST
//!BIND ADOPT_OUT_{D}_ST
//!BIND LUMA_A_Q
//!BIND LUMA_B_Q
//!SAVE FLOW_Q_{D}
//!WIDTH HOOKED.w 4 /
//!HEIGHT HOOKED.h 4 /
//!COMPONENTS 2
//!DESC [adopt] a locked print adopts its outline's motion ({D})
float adopt_sad(vec2 uv, vec2 d) {{
    float s = 0.0;
    for (int y = -2; y <= 2; y++)
        for (int x = -2; x <= 2; x++) {{
            vec2 o = vec2(float(x), float(y)) * LUMA_A_Q_pt;
            s += abs({FROM}_tex(uv + o).r - {TO}_tex(uv + o + d * LUMA_A_Q_pt).r);
        }}
    return s;
}}
vec4 hook() {{
    ivec2 coord = ivec2(LUMA_A_Q_pos * LUMA_A_Q_size);
    if (!pair_changed)
        return imageLoad(ADOPT_OUT_{D}_ST, coord);
    vec2 uv = LUMA_A_Q_pos;
    vec2 h = FLOW_Q_{D}_tex(uv).xy;                          // quarter texels
    vec4 result = vec4(h, 0.0, 0.0);
    // THE GATE: a rival basin within margin at the 1/8 level, in this cell or a neighbour (the print's signature)
    bool gate = false;
    ivec2 ec = coord / 2, en = ivec2(LUMA_A_Q_size) / 2;       // the 1/8 grid actually in use (the storage is 4K-sized)
    for (int y = -1; y <= 1; y++)
        for (int x = -1; x <= 1; x++) {{
            ivec2 e = clamp(ec + ivec2(x, y), ivec2(0), en - 1);
            if (imageLoad(ALIAS_E_M_ST, e).{M} < {MARGIN}) gate = true;
        }}
    if (gate && length(h * 4.0) > {MOVING}) {{
        vec4 ref = ADOPT_REF_{D}_tex((vec2(coord / 8) + 0.5) * ADOPT_REF_{D}_pt);   // this texel's 32-px cell, exactly
        if (ref.w > 0.5) {{
            vec2 best = ref.xy * 0.25;                          // px -> quarter texels
            float bc = adopt_sad(uv, best);
            for (int j = -2; j <= 2; j++)
                for (int i = -2; i <= 2; i++) {{
                    vec2 d = ref.xy * 0.25 + vec2(float(i), float(j)) * 0.125;   // +-1 px in half-pixel steps
                    float c = adopt_sad(uv, d);
                    if (c < bc) {{ bc = c; best = d; }}
                }}
            if (length((best - h) * 4.0) > {DIFF} && bc <= adopt_sad(uv, h))
                result = vec4(best, 0.0, 0.0);
        }}
    }}
    imageStore(ADOPT_OUT_{D}_ST, coord, result);
    return result;
}}
"""


def add_outline_adopt(t):
    """after the carry's two picks (the last passes that save FLOW_Q_AB / FLOW_Q_BA before the variational stage)"""
    for anchor in ("//!DESC [alias] each quarter-level cell takes its cheaper hypothesis over the four scans (AB)\n",
                   "//!DESC [alias] each quarter-level cell takes its cheaper hypothesis over the four scans (BA)\n"):
        _once(t, anchor, "the carry's pick (needs ALIAS_CARRY=1)")
    _once(t, "//!TEXTURE ALIAS_E_M_ST\n", "the 1/8-level basins' margins")
    i = t.index("//!DESC [alias] each quarter-level cell takes its cheaper hypothesis over the four scans (BA)\n")
    j = t.index("\n//!HOOK FRAME_MIX", i) + 1                      # the start of the pass after the BA pick
    body = ""
    for d, m, fr, to in (("AB", "x", "LUMA_A_Q", "LUMA_B_Q"), ("BA", "y", "LUMA_B_Q", "LUMA_A_Q")):
        body += PASSES.format(D=d, M=m, FROM=fr, TO=to, MOVING=f"{ADOPT_MOVING:.2f}", STILL_R=ADOPT_STILL_R, BINS=ADOPT_BINS,
                              WIDE=ADOPT_WIDE, MARGIN=f"{ADOPT_MARGIN:.2f}", MIN_ANCHORS=f"{ADOPT_MIN_ANCHORS:.1f}",
                              DIFF=f"{ADOPT_DIFF:.1f}")
    return t[:j] + body + t[j:]
