#!/usr/bin/env python3
"""The texture-energy channel, second form: SMOOTHED energy, at the coarse level and the 1/8 level (a prototype
patched onto a generated file; energyvariant.py was the first form).

The first form took each coarse texel's energy over its own 16 x 16 box. It gave the limb reach, and it cost the
period family 2-7 dB, as its pre-registered risk said: a 24-px print's gradient energy, averaged over a 16-px box,
ripples with the print's phase, and that ripple aliases at 16-px texels just as the luma did. Here the energy is a
GAUSSIAN-weighted mean of the 2-px gradient magnitude (sigma SIGMA px, a 9 x 9 grid of taps at sigma / 2, out to 2
sigma). At sigma 12 a 24-px period's ripple is attenuated to exp(-2 pi^2 sigma^2 / P^2) < 1%, so a print reads as a
flat energy field and the term is silent inside it, while a 48-px textured limb stays a blob that moves.
The same channel is added at the 1/8 level too, where the limb's 5-px grain aliases at 8-px texels in the same way.

    energyvariant2.py <in.glsl> <out.glsl> [W_S] [W_E] [SIGMA] [STEP]      (defaults 8, 4, 12, 2)"""
import sys

src, dst = sys.argv[1], sys.argv[2]
ws = float(sys.argv[3]) if len(sys.argv) > 3 else 8.0
we = float(sys.argv[4]) if len(sys.argv) > 4 else 4.0
sigma = float(sys.argv[5]) if len(sys.argv) > 5 else 12.0
t = open(src, encoding="utf-8").read()


def must(old, new, count=1):
    global t
    n = t.count(old)
    assert n == count, f"{n} x (want {count}): {old[:90]!r}"
    t = t.replace(old, new)


STEP = float(sys.argv[6]) if len(sys.argv) > 6 else 2.0          # tap spacing, px
R = int(round(2 * sigma / STEP))


def luma_pass(frame, tex, level, div, weight):
    if weight == 0:
        return
    must(f"""//!SAVE LUMA_{frame}_{level}
//!WIDTH HOOKED.w {div} /
//!HEIGHT HOOKED.h {div} /
//!COMPONENTS 1
//!DESC [high] downsample frame {frame} to 1/{div} res (luma)
vec4 hook() {{
    return vec4(dot({tex}_tex({tex}_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}}""", f"""//!SAVE LUMA_{frame}_{level}
//!WIDTH HOOKED.w {div} /
//!HEIGHT HOOKED.h {div} /
//!COMPONENTS 2
//!DESC [high] downsample frame {frame} to 1/{div} res (luma; .g the smoothed texture energy)
float lum_{frame}{level}(vec2 p) {{ return dot({tex}_tex(p).rgb, vec3(0.299, 0.587, 0.114)); }}
vec4 hook() {{
    float l = lum_{frame}{level}({tex}_pos);
    // texture energy: a Gaussian-weighted (sigma {sigma:g} px) mean of the 2-px gradient magnitude on a DENSE grid
    // of taps every {STEP:g} px out to 2 sigma -- a statistic of the grain, smoothed past a print's period. The taps must
    // be dense: at sigma / 2 apart they sampled a 24-px print's 12-px |gradient| at one phase, and the estimate
    // aliased (the first smoothed form's period-family collapse)
    float e = 0.0, ws = 0.0;
    for (int j = -{R}; j <= {R}; j++) {{
        for (int i = -{R}; i <= {R}; i++) {{
            vec2 d = vec2(float(i), float(j)) * {STEP:.4f};
            float w = exp(-dot(d, d) / {2 * sigma * sigma:.4f});
            vec2 p = {tex}_pos + d * {tex}_pt;
            float c = lum_{frame}{level}(p);
            e += w * (abs(lum_{frame}{level}(p + vec2(2.0, 0.0) * {tex}_pt) - c) + abs(lum_{frame}{level}(p + vec2(0.0, 2.0) * {tex}_pt) - c));
            ws += w;
        }}
    }}
    return vec4(l, e / ws, 0, 0);
}}""")


def sad(level, fn_ab, fn_ba, weight):
    if weight == 0:
        return
    L = level
    must(f"""            s += abs(LUMA_A_{L}_tex(uv_a + o).r - LUMA_B_{L}_tex(uv_b + o).r);""",
         f"""            vec2 la = LUMA_A_{L}_tex(uv_a + o).rg, lb = LUMA_B_{L}_tex(uv_b + o).rg;
            s += abs(la.r - lb.r) + ENERGY_W_{L} * abs(la.g - lb.g);""")
    must(f"""            s += abs(LUMA_B_{L}_tex(uv_b + o).r - LUMA_A_{L}_tex(uv_a + o).r);""",
         f"""            vec2 lb2 = LUMA_B_{L}_tex(uv_b + o).rg, la2 = LUMA_A_{L}_tex(uv_a + o).rg;
            s += abs(lb2.r - la2.r) + ENERGY_W_{L} * abs(lb2.g - la2.g);""")
    # one declaration per PASS: the coarse search is fused (both directions in one pass), the 1/8 fresh search is two
    ia = t.index(f"float {fn_ab}(vec2 uv_a, vec2 uv_b) {{\n")
    ib = t.index(f"float {fn_ba}(vec2 uv_b, vec2 uv_a) {{\n")
    same_pass = "//!HOOK" not in t[min(ia, ib):max(ia, ib)]
    decl = f"const float ENERGY_W_{L} = {weight:g};   // PROTOTYPE: the texture-energy term's weight\n"
    fns = ((fn_ab, "vec2 uv_a, vec2 uv_b"),) if same_pass else ((fn_ab, "vec2 uv_a, vec2 uv_b"), (fn_ba, "vec2 uv_b, vec2 uv_a"))
    for fn, args in fns:
        if same_pass and ib < ia:
            fn, args = fn_ba, "vec2 uv_b, vec2 uv_a"
        must(f"float {fn}({args}) {{\n", decl + f"float {fn}({args}) {{\n")
    print(f"  {L}: {fn_ab}/{fn_ba} {'one pass' if same_pass else 'two passes'}")


def check_pass(weight):
    """The 1/8 level's three-way data check (after propagation) re-scores the raw and the propagated vector; it must
    score them as the search did, or it rejects the energy-chosen vector by luma alone (found: K2's final field fell
    from 0.9 to 0.2 while its raw 1/8 search read 0.95)."""
    if weight == 0:
        return
    must("""            s += abs(LUMA_A_E_tex(uv + o).r - LUMA_B_E_tex(uv + o + flow_uv).r);""",
         """            vec2 ca = LUMA_A_E_tex(uv + o).rg, cb = LUMA_B_E_tex(uv + o + flow_uv).rg;
            s += abs(ca.r - cb.r) + ENERGY_W_E * abs(ca.g - cb.g);""")
    must("""            s += abs(LUMA_B_E_tex(uv + o).r - LUMA_A_E_tex(uv + o + flow_uv).r);""",
         """            vec2 cb2 = LUMA_B_E_tex(uv + o).rg, ca2 = LUMA_A_E_tex(uv + o + flow_uv).rg;
            s += abs(cb2.r - ca2.r) + ENERGY_W_E * abs(cb2.g - ca2.g);""")
    ia, ib = t.index("float sad5(vec2 uv, vec2 flow_uv) {\n"), t.index("float sad5_ba(vec2 uv, vec2 flow_uv) {\n")
    decl = f"const float ENERGY_W_E = {weight:g};   // PROTOTYPE: the check scores as the search does\n"
    if "//!HOOK" not in t[min(ia, ib):max(ia, ib)]:
        first = "float sad5(vec2 uv, vec2 flow_uv) {\n" if ia < ib else "float sad5_ba(vec2 uv, vec2 flow_uv) {\n"
        must(first, decl + first)
    else:
        must("float sad5(vec2 uv, vec2 flow_uv) {\n", decl + "float sad5(vec2 uv, vec2 flow_uv) {\n")
        must("float sad5_ba(vec2 uv, vec2 flow_uv) {\n", decl + "float sad5_ba(vec2 uv, vec2 flow_uv) {\n")


for frame, tex in (("A", "HOOKED"), ("B", "NEXT")):
    luma_pass(frame, tex, "S", 16, ws)
    luma_pass(frame, tex, "E", 8, we)
sad("S", "sad5x5_s", "sad5x5_s2", ws)
sad("E", "sad5x5_e", "sad5x5_e2", we)
check_pass(we)
open(dst, "w", encoding="utf-8").write(t)
print(f"wrote {dst} (W_S {ws:g}, W_E {we:g}, sigma {sigma:g})")
