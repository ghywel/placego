#!/usr/bin/env python3
"""The template match: one rigid shift per moving thing, found as a template, not as a vote.

    ./build_template.py <out.glsl> <lineart-variant.glsl> [RADIUS_E=3] [WINDOW_E=6] [MOVING_TAU=0.08] [CHAR_TAU=0.03]

Why (ANI-PRIOR-ART.md; the owner's 'feature-template warping'): on a cel character sixty pixels tall
whose limbs are redrawn every frame, the dense flow is a rainbow -- every direction at once -- and a
trimmed mean of it is noise. The coarse levels have nothing that size to match and the fine levels chase
the redraws. A character does have one motion, and the way to find it is to match the character as a
whole: for every texel in the moving region, an exhaustive search over rigid shifts of +-RADIUS_E texels
at the 1/8 level for the one that best matches a (2 WINDOW_E + 1)^2-texel window of the distance-field-fed
luma the line-art variant already computes. Every texel of one character sees nearly the same window, so
every texel of it lands on the same shift by construction. A three-point parabolic fit along each axis
gives a sub-texel answer. The warp moves character texels (those the plate does not vouch for as
background, in either frame) by that shift and nothing else -- no refinement afterwards to re-chase the
limbs -- and the level-set morph draws the lines on the way.
"""
import pathlib
import sys

OUT, BASE = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
R = sys.argv[3] if len(sys.argv) > 3 else "3"
W = sys.argv[4] if len(sys.argv) > 4 else "6"
MOVING_TAU = sys.argv[5] if len(sys.argv) > 5 else "0.08"
CHAR_TAU = sys.argv[6] if len(sys.argv) > 6 else "0.03"
t = BASE.read_text(encoding="utf-8")
assert "[lineart]" in t and "[plate]" in t, "input must be the line-art variant (which contains the plate)"

TEMPLATE = """
//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND NEXT
//!BIND LUMA_A_E
//!BIND LUMA_B_E
//!BIND PLATE_TEX
//!SAVE FLOW_T
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!DESC [template] one rigid shift per moving thing: the exhaustive template match of a character-sized window at 1/8 res
const int TPL_R = %s;                 // search radius, 1/8-res texels (8 px each at the source's size)
const int TPL_W = %s;                 // window half-size, 1/8-res texels: (2W+1)^2 texels, a character-sized template
const float TPL_MOVING_TAU = %s;
const float TPL_CHAR_TAU = %s;
bool moving_near(vec2 uv) {
    for (int j = -2; j <= 2; j++)
        for (int i = -2; i <= 2; i++) {
            vec2 p = uv + vec2(float(i), float(j)) * LUMA_A_E_pt;
            if (abs(LUMA_A_E_tex(p).r - LUMA_B_E_tex(p).r) > TPL_MOVING_TAU) return true;
        }
    return false;
}
float sad(vec2 uv, vec2 d) {
    float s = 0.0;
    for (int j = -TPL_W; j <= TPL_W; j++)
        for (int i = -TPL_W; i <= TPL_W; i++) {
            vec2 p = uv + vec2(float(i), float(j)) * LUMA_A_E_pt;
            s += abs(LUMA_A_E_tex(p).r - LUMA_B_E_tex(p + d * LUMA_A_E_pt).r);
        }
    return s;
}
vec4 hook() {
    vec2 uv = LUMA_A_E_pos;
    if (!moving_near(uv)) return vec4(0.0);
    vec4 pl = PLATE_TEX_tex(uv);
    bool char_a = pl.a < 2.0 || length(HOOKED_tex(uv).rgb - pl.rgb) > TPL_CHAR_TAU;
    bool char_b = pl.a < 2.0 || length(NEXT_tex(uv).rgb - pl.rgb) > TPL_CHAR_TAU;
    if (!(char_a || char_b)) return vec4(0.0);
    float best = 1.0e9; ivec2 bd = ivec2(0);
    for (int y = -TPL_R; y <= TPL_R; y++)
        for (int x = -TPL_R; x <= TPL_R; x++) {
            float s = sad(uv, vec2(float(x), float(y)));
            if (s < best) { best = s; bd = ivec2(x, y); }
        }
    // sub-texel: a parabola through the three costs along each axis
    vec2 sub = vec2(0.0);
    if (abs(bd.x) < TPL_R) {
        float l = sad(uv, vec2(float(bd.x - 1), float(bd.y))), r = sad(uv, vec2(float(bd.x + 1), float(bd.y)));
        float den = l - 2.0 * best + r; if (den > 1.0e-6) sub.x = clamp(0.5 * (l - r) / den, -0.5, 0.5);
    }
    if (abs(bd.y) < TPL_R) {
        float u = sad(uv, vec2(float(bd.x), float(bd.y - 1))), d = sad(uv, vec2(float(bd.x), float(bd.y + 1)));
        float den = u - 2.0 * best + d; if (den > 1.0e-6) sub.y = clamp(0.5 * (u - d) / den, -0.5, 0.5);
    }
    return vec4(vec2(bd) + sub, 1.0, best);
}
""" % (R, W, MOVING_TAU, CHAR_TAU)

i = t.index("//!DESC [high] motion-compensated warp")
j = t.rfind("//!HOOK FRAME_MIX", 0, i)
t = t[:j] + TEMPLATE.lstrip("\n") + "\n" + t[j:]
wi = t.index("//!HOOK FRAME_MIX", t.index("//!DESC [template]"))
we = t.index("//!DESC [high] motion-compensated warp", wi)
hdr = t[wi:we]
assert hdr.count("//!BIND HOOKED\n") == 1
t = t[:wi] + hdr.replace("//!BIND HOOKED\n", "//!BIND HOOKED\n//!BIND FLOW_T\n", 1) + t[we:]
old = "    vec2 flow_ab = FLOW_H_AB_tex(HOOKED_pos).xy * 2.0 * HOOKED_pt;\n"
assert t.count(old) == 1, t.count(old)
t = t.replace(old, old + "    vec4 tpl = FLOW_T_tex(HOOKED_pos);                       // [template] the character's own rigid shift\n"
                         "    if (tpl.z > 0.5) flow_ab = tpl.xy * 8.0 * HOOKED_pt;\n")
OUT.write_text(t, encoding="utf-8", newline="\n")
print("%s: template pass (radius %s, window %s, moving %s, char %s) + warp on FLOW_T for character texels; %d passes" % (OUT.name, R, W, MOVING_TAU, CHAR_TAU, t.count("//!HOOK")))
