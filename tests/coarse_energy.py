"""The coarse texture-energy channel, as a text transform on a generated shader: gen_variational.py's COARSE_ENERGY=1
(its block says what it is and gives the verdict); tests/probes/limb/energyvariant3.py wraps it for probes.

Per frame (A = HOOKED, B = NEXT), three passes at quarter resolution put a smoothed texture energy in ENERGY_x:
each 4 x 4 block's 2-px gradient magnitude on dense 2 x 2 taps, then a separable Gaussian (sigma 3 quarter-res texels
= 12 px). The 1/16 and 1/8 lumas carry one sample of it in .g; their SADs add W |dE| (W_S at 1/16, W_E at 1/8), and
the 1/8 level's post-propagation data check scores the same way.

    add(t, ws, we) -> t        every anchor asserted exactly once"""

LUMA = "vec3(0.299, 0.587, 0.114)"


def _energy_passes(frame, tex):
    return f"""//!HOOK FRAME_MIX
//!BIND {tex}
//!SAVE ENERGY_{frame}_Q0
//!WIDTH HOOKED.w 4 /
//!HEIGHT HOOKED.h 4 /
//!COMPONENTS 1
//!DESC [energy] frame {frame}: each 4x4 block's 2-px gradient magnitude, dense 2x2 taps (1/4 res)
float lum_q(vec2 p) {{ return dot({tex}_tex(p).rgb, {LUMA}); }}
vec4 hook() {{
    float e = 0.0;
    for (int j = 0; j < 2; j++) {{
        for (int i = 0; i < 2; i++) {{
            vec2 p = {tex}_pos + (vec2(float(i), float(j)) * 2.0 - 1.0) * {tex}_pt;
            float c = lum_q(p);
            e += abs(lum_q(p + vec2(2.0, 0.0) * {tex}_pt) - c) + abs(lum_q(p + vec2(0.0, 2.0) * {tex}_pt) - c);
        }}
    }}
    return vec4(e / 4.0, 0, 0, 0);
}}

//!HOOK FRAME_MIX
//!BIND ENERGY_{frame}_Q0
//!SAVE ENERGY_{frame}_Q1
//!WIDTH HOOKED.w 4 /
//!HEIGHT HOOKED.h 4 /
//!COMPONENTS 1
//!DESC [energy] frame {frame}: horizontal Gaussian, sigma 12 px
vec4 hook() {{
    float e = 0.0, w = 0.0;
    for (int i = -6; i <= 6; i++) {{
        float g = exp(-float(i * i) / 18.0);
        e += g * ENERGY_{frame}_Q0_tex(ENERGY_{frame}_Q0_pos + vec2(float(i), 0.0) * ENERGY_{frame}_Q0_pt).r;
        w += g;
    }}
    return vec4(e / w, 0, 0, 0);
}}

//!HOOK FRAME_MIX
//!BIND ENERGY_{frame}_Q1
//!SAVE ENERGY_{frame}
//!WIDTH HOOKED.w 4 /
//!HEIGHT HOOKED.h 4 /
//!COMPONENTS 1
//!DESC [energy] frame {frame}: vertical Gaussian, sigma 12 px -> the smoothed texture energy
vec4 hook() {{
    float e = 0.0, w = 0.0;
    for (int i = -6; i <= 6; i++) {{
        float g = exp(-float(i * i) / 18.0);
        e += g * ENERGY_{frame}_Q1_tex(ENERGY_{frame}_Q1_pos + vec2(0.0, float(i)) * ENERGY_{frame}_Q1_pt).r;
        w += g;
    }}
    return vec4(e / w, 0, 0, 0);
}}

"""


ANCHOR = """// ---------------------------------------------------------------------
// Sixteenth-res luma (coarsest search level)
// ---------------------------------------------------------------------
"""


def add(t, ws=8.0, we=1.0):
    def must(old, new, count=1):
        nonlocal t
        n = t.count(old)
        assert n == count, f"coarse energy: {n} x (want {count}): {old[:90]!r}"
        t = t.replace(old, new)

    def declare(fn_a, sig_a, fn_b, sig_b, decl):
        """one declaration per PASS: before the first of two functions if one pass holds both, else before each"""
        ia, ib = t.index(f"float {fn_a}({sig_a}) {{\n"), t.index(f"float {fn_b}({sig_b}) {{\n")
        if "//!HOOK" not in t[min(ia, ib):max(ia, ib)]:
            first = f"float {fn_a}({sig_a}) {{\n" if ia < ib else f"float {fn_b}({sig_b}) {{\n"
            must(first, decl + first)
        else:
            must(f"float {fn_a}({sig_a}) {{\n", decl + f"float {fn_a}({sig_a}) {{\n")
            must(f"float {fn_b}({sig_b}) {{\n", decl + f"float {fn_b}({sig_b}) {{\n")

    must(ANCHOR, ANCHOR + _energy_passes("A", "HOOKED") + _energy_passes("B", "NEXT"))
    for frame, tex in (("A", "HOOKED"), ("B", "NEXT")):
        for level, div, w in (("S", 16, ws), ("E", 8, we)):
            if w == 0:
                continue
            must(f"""//!BIND {tex}
//!SAVE LUMA_{frame}_{level}
//!WIDTH HOOKED.w {div} /
//!HEIGHT HOOKED.h {div} /
//!COMPONENTS 1
//!DESC [high] downsample frame {frame} to 1/{div} res (luma)
vec4 hook() {{
    return vec4(dot({tex}_tex({tex}_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}}""", f"""//!BIND {tex}
//!BIND ENERGY_{frame}
//!SAVE LUMA_{frame}_{level}
//!WIDTH HOOKED.w {div} /
//!HEIGHT HOOKED.h {div} /
//!COMPONENTS 2
//!DESC [high] downsample frame {frame} to 1/{div} res (luma; .g the smoothed texture energy, one sample)
vec4 hook() {{
    return vec4(dot({tex}_tex({tex}_pos).rgb, vec3(0.299, 0.587, 0.114)), ENERGY_{frame}_tex({tex}_pos).r, 0, 0);
}}""")
    for L, fn_ab, fn_ba, w in (("S", "sad5x5_s", "sad5x5_s2", ws), ("E", "sad5x5_e", "sad5x5_e2", we)):
        if w == 0:
            continue
        must(f"""            s += abs(LUMA_A_{L}_tex(uv_a + o).r - LUMA_B_{L}_tex(uv_b + o).r);""",
             f"""            vec2 la = LUMA_A_{L}_tex(uv_a + o).rg, lb = LUMA_B_{L}_tex(uv_b + o).rg;
            s += abs(la.r - lb.r) + ENERGY_W_{L} * abs(la.g - lb.g);""")
        must(f"""            s += abs(LUMA_B_{L}_tex(uv_b + o).r - LUMA_A_{L}_tex(uv_a + o).r);""",
             f"""            vec2 lb2 = LUMA_B_{L}_tex(uv_b + o).rg, la2 = LUMA_A_{L}_tex(uv_a + o).rg;
            s += abs(lb2.r - la2.r) + ENERGY_W_{L} * abs(lb2.g - la2.g);""")
        declare(fn_ab, "vec2 uv_a, vec2 uv_b", fn_ba, "vec2 uv_b, vec2 uv_a",
                f"const float ENERGY_W_{L} = {w:g};   // the texture-energy term's weight (COARSE_ENERGY)\n")
    if we:
        # the 1/8 level's post-propagation data check scores as the search does, or it rejects the energy-chosen
        # vector by luma alone (found: the dark-wall limb's raw 1/8 read 0.95 and its final field 0.2)
        must("""            s += abs(LUMA_A_E_tex(uv + o).r - LUMA_B_E_tex(uv + o + flow_uv).r);""",
             """            vec2 ca = LUMA_A_E_tex(uv + o).rg, cb = LUMA_B_E_tex(uv + o + flow_uv).rg;
            s += abs(ca.r - cb.r) + ENERGY_W_E * abs(ca.g - cb.g);""")
        must("""            s += abs(LUMA_B_E_tex(uv + o).r - LUMA_A_E_tex(uv + o + flow_uv).r);""",
             """            vec2 cb2 = LUMA_B_E_tex(uv + o).rg, ca2 = LUMA_A_E_tex(uv + o + flow_uv).rg;
            s += abs(cb2.r - ca2.r) + ENERGY_W_E * abs(cb2.g - ca2.g);""")
        declare("sad5", "vec2 uv, vec2 flow_uv", "sad5_ba", "vec2 uv, vec2 flow_uv",
                f"const float ENERGY_W_E = {we:g};   // the check scores as the search does (COARSE_ENERGY)\n")
    assert t.count("//!SAVE ENERGY_A\n") == 1 and t.count("//!SAVE ENERGY_B\n") == 1
    return t
