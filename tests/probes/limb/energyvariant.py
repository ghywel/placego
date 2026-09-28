#!/usr/bin/env python3
"""A PROTOTYPE, patched onto a generated file: a TEXTURE-ENERGY channel beside the coarse search's point-sampled
luma (the limb, mechanism 1; NFRAME-LIMITS.md "The field on real bodies" and section 8).

The 1/16 luma is ONE bilinear sample per 16 x 16 footprint. On a finely textured object that moves by anything but
a multiple of 16 px, each coarse texel samples a different grain cell in A and in B, so the object's coarse picture
is scrambled between the frames and matches nothing, while a still textured background's samples are identical and
win at zero motion (K1: the coarse search reads the limb at 0.26 at 18-24 px/frame; K3, the same limb brighter, so
it stands out whatever the grain does: 0.87). Section 8 refuted REPLACING the samples with a box average (11% of the
contrast survives; the aliased detail is load-bearing at integer speeds). This ADDS a second channel instead: the
footprint's texture energy -- the mean 2-px gradient magnitude on a 4 x 4 grid of taps -- which does not depend on
where the grain's cells fall, so a textured object stays a high-energy blob that moves. The coarse SAD becomes
|dL| + ENERGY_W |dE| over the same 3 x 3 window; nothing else reads the new channel.

    energyvariant.py <in.glsl> <out.glsl> [ENERGY_W]"""
import sys

src, dst = sys.argv[1], sys.argv[2]
ew = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
t = open(src, encoding="utf-8").read()


def must(old, new, count=1):
    global t
    n = t.count(old)
    assert n == count, f"{n} x (want {count}): {old[:80]!r}"
    t = t.replace(old, new)


for frame, tex in (("A", "HOOKED"), ("B", "NEXT")):
    must(f"""//!SAVE LUMA_{frame}_S
//!WIDTH HOOKED.w 16 /
//!HEIGHT HOOKED.h 16 /
//!COMPONENTS 1
//!DESC [high] downsample frame {frame} to 1/16 res (luma)
vec4 hook() {{
    return vec4(dot({tex}_tex({tex}_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}}""", f"""//!SAVE LUMA_{frame}_S
//!WIDTH HOOKED.w 16 /
//!HEIGHT HOOKED.h 16 /
//!COMPONENTS 2
//!DESC [high] downsample frame {frame} to 1/16 res (luma; .g the footprint's texture energy)
float lum_{frame}(vec2 p) {{ return dot({tex}_tex(p).rgb, vec3(0.299, 0.587, 0.114)); }}
vec4 hook() {{
    float l = lum_{frame}({tex}_pos);
    // texture energy: the mean 2-px gradient magnitude on a 4 x 4 grid of taps spread over this texel's
    // 16 x 16 footprint -- a statistic of the grain, not a sample of it, so it does not scramble as the grain moves
    float e = 0.0;
    for (int j = 0; j < 4; j++) {{
        for (int i = 0; i < 4; i++) {{
            vec2 p = {tex}_pos + (vec2(float(i), float(j)) * 4.0 - 6.0) * {tex}_pt;
            float c = lum_{frame}(p);
            e += abs(lum_{frame}(p + vec2(2.0, 0.0) * {tex}_pt) - c) + abs(lum_{frame}(p + vec2(0.0, 2.0) * {tex}_pt) - c);
        }}
    }}
    return vec4(l, e / 32.0, 0, 0);
}}""")
# both directions of the fused coarse search (A->B in sad5x5_s, B->A in sad5x5_s2), in the one pass
must("""            s += abs(LUMA_A_S_tex(uv_a + o).r - LUMA_B_S_tex(uv_b + o).r);""",
     """            vec2 la = LUMA_A_S_tex(uv_a + o).rg, lb = LUMA_B_S_tex(uv_b + o).rg;
            s += abs(la.r - lb.r) + COARSE_ENERGY_W * abs(la.g - lb.g);""")
must("""            s += abs(LUMA_B_S_tex(uv_b + o).r - LUMA_A_S_tex(uv_a + o).r);""",
     """            vec2 lb2 = LUMA_B_S_tex(uv_b + o).rg, la2 = LUMA_A_S_tex(uv_a + o).rg;
            s += abs(lb2.r - la2.r) + COARSE_ENERGY_W * abs(lb2.g - la2.g);""")
must("float sad5x5_s(vec2 uv_a, vec2 uv_b) {\n",
     f"const float COARSE_ENERGY_W = {ew};   // PROTOTYPE: the texture-energy term's weight\nfloat sad5x5_s(vec2 uv_a, vec2 uv_b) {{\n")
open(dst, "w", encoding="utf-8").write(t)
print(f"wrote {dst} (ENERGY_W {ew})")
