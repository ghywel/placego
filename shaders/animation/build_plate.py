"""The background-plate variant of the animation shader (the owner's 2026-08 idea, ROADMAP.md
'A shader class specific to animation', second half).

    build_plate.py <out.glsl> <base.glsl> [STATIC_TAU=0.03] [DISAGREE_TAU=0.12] [MIN_CONF=2]

A persistent storage image PLATE (rgb = the background this texel showed when it was last still, a =
how many windows have confirmed it) is updated once per source pair: a texel whose colour does not change
between A and B is still, and a still texel is background unless a character is standing on it; it
confirms the plate if it agrees, replaces it with confidence 1 if it does not. A moving texel leaves the
plate alone, which is the whole point: while a character crosses a texel the plate keeps the background
it held before. A scene cut clears the plate.

The warp is changed in one place. Where its two candidates -- the texel warped from A and from B --
disagree by more than DISAGREE_TAU, the current shader blends them (the ghost). Now, if the plate is
confident there, the candidate closer to the plate wins outright IF it is within DISAGREE_TAU of the
plate, else the blend stands. The plate arbitrates; it never invents. A texel a character uncovers has one
candidate that is the character (warped from the frame that still had it there) and one that is the
background; the plate picks the background. The same rule at a character's leading edge picks the
background too, which is the known cost this experiment measures.
"""
import pathlib
import re
import sys

OUT, BASE = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
STATIC_TAU = sys.argv[3] if len(sys.argv) > 3 else "0.03"
DISAGREE_TAU = sys.argv[4] if len(sys.argv) > 4 else "0.12"
MIN_CONF = sys.argv[5] if len(sys.argv) > 5 else "2.0"
t = BASE.read_text(encoding="utf-8")

PLATE = """
//!TEXTURE PLATE
//!SIZE 1920 1080
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND NEXT
//!BIND SCENE_DIFF
//!BIND PLATE
//!SAVE PLATE_TEX
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!DESC [plate] background plate: what this texel showed when it was last still, and how many windows confirm it
const float PLATE_STATIC_TAU = %s;      // a texel whose A/B colour differs less than this is still
const float PLATE_AGREE_TAU = 0.06;     // agreement with the plate's stored colour
const float PLATE_CONF_MAX = 16.0;
const float PLATE_CUT_DIFF = 0.125;     // the warp's SCENE_CUT_DIFF
vec4 hook() {
    ivec2 c = ivec2(gl_FragCoord.xy);
    vec4 p = imageLoad(PLATE, c);
    if (SCENE_DIFF_tex(vec2(0.5)).r > PLATE_CUT_DIFF)
        p = vec4(0.0);
    if (pair_changed) {
        vec3 a = HOOKED_tex(HOOKED_pos).rgb;
        vec3 b = NEXT_tex(NEXT_pos).rgb;
        bool still = length(a - b) < PLATE_STATIC_TAU;
        if (still) {
            if (p.a > 0.0 && length(a - p.rgb) < PLATE_AGREE_TAU)
                p = vec4(mix(p.rgb, a, 0.25), min(p.a + 1.0, PLATE_CONF_MAX));
            else
                p = vec4(a, 1.0);
        }
        imageStore(PLATE, c, p);
    }
    return p;
}
"""

# 1. the plate pass goes in front of the warp pass
marker = "//!HOOK FRAME_MIX\n//!BIND HOOKED\n//!BIND NEXT\n//!BIND FLOW_H_AB\n"
i = t.index("//!DESC [high] motion-compensated warp")
j = t.rfind("//!HOOK FRAME_MIX", 0, i)
assert j > 0, "no warp pass"
t = t[:j] + (PLATE % STATIC_TAU).lstrip("\n") + "\n" + t[j:]

# 2. the warp binds the plate texture and arbitrates
warp_hdr_i = t.index("//!HOOK FRAME_MIX", t.index("//!DESC [plate]"))
hdr_end = t.index("//!DESC [high] motion-compensated warp", warp_hdr_i)
hdr = t[warp_hdr_i:hdr_end]
assert hdr.count("//!BIND HOOKED\n") == 1, hdr
hdr2 = hdr.replace("//!BIND HOOKED\n", "//!BIND HOOKED\n//!BIND PLATE_TEX\n", 1)
t = t[:warp_hdr_i] + hdr2 + t[hdr_end:]
old = "    return mix(warped_a, warped_b, mix_t);\n}"
assert t.count(old) == 1, t.count(old)
new = """    // THE PLATE ARBITRATES (scratch experiment, see build_plate.py). Where the two candidates disagree,
    // the shipped shader blends them into a ghost; if the plate is confident here, the candidate closer to
    // the plate wins outright when it is within reach of it. The plate chooses, it never invents.
    const float PLATE_DISAGREE_TAU = %s;
    const float PLATE_MIN_CONF = %s;
    vec4 plate = PLATE_TEX_tex(HOOKED_pos);
    // A candidate whose SOURCE texel is background (it agrees with the plate there) is background, and the
    // true background at THIS texel is the plate here -- not the other cell of a patterned backdrop that a
    // character's flow dragged in. Measured without this: a halo of smeared background around every
    // moving character on a detailed backdrop.
    if (plate.a >= PLATE_MIN_CONF) {
        vec4 pa = PLATE_TEX_tex(HOOKED_pos - flow_ab * mix_t);
        if (pa.a >= PLATE_MIN_CONF && length(warped_a.rgb - pa.rgb) < 0.06) warped_a = vec4(plate.rgb, warped_a.a);
        vec4 pb = PLATE_TEX_tex(NEXT_pos + flow_ab * (1.0 - mix_t));
        if (pb.a >= PLATE_MIN_CONF && length(warped_b.rgb - pb.rgb) < 0.06) warped_b = vec4(plate.rgb, warped_b.a);
    }
    if (plate.a >= PLATE_MIN_CONF && length(warped_a.rgb - warped_b.rgb) > PLATE_DISAGREE_TAU) {
        float da = length(warped_a.rgb - plate.rgb), db = length(warped_b.rgb - plate.rgb);
        if (min(da, db) < PLATE_DISAGREE_TAU)
            return (da < db) ? warped_a : warped_b;
    }
    return mix(warped_a, warped_b, mix_t);
}""" % (DISAGREE_TAU, MIN_CONF)
t = t.replace(old, new)
assert t.count("[plate]") == 1 and t.count("PLATE_TEX_tex(") == 3, t.count("PLATE_TEX_tex(")
OUT.write_text(t, encoding="utf-8", newline="\n")
print("%s: plate pass + arbitrating warp (STATIC_TAU %s, DISAGREE_TAU %s, MIN_CONF %s), %d passes" % (OUT.name, STATIC_TAU, DISAGREE_TAU, MIN_CONF, t.count("//!HOOK")))
