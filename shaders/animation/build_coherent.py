"""The template warp, expressed in the dense machinery -- ONE MOTION PER MOVING THING.

    build_coherent.py <out.glsl> <plate-variant.glsl> [RADIUS_H=32] [MOVING_TAU=0.08] [CHAR_TAU=0.06] [MINFLOW_H=0.5]

The owner's first cel-animation idea (ROADMAP.md, 'Feature-template warping'): a cel character is redrawn
between frames, so a dense per-texel flow tears it into pieces that warp to different places; but the
character has an identity and one motion. Here: a pass at the half-res flow level takes, for every texel
that is CHARACTER in either frame (not the confident plate's colour there), a trimmed mean of the dense
flow over the character texels within RADIUS_H texels, and hands that one vector to the warp. Both warp
candidates then agree about where the character is at every intermediate time: a texel is character at t
iff it lies in A's character shifted by v t, iff it lies in B's character shifted back by v (1 - t), so
character blends with character and background with background, and a redrawn feature crossfades in
place instead of tearing. Texels that are background in both frames keep their dense flow. Needs the
plate variant as its input (the plate is how a texel is known to be character or background).
"""
import pathlib
import sys

OUT, BASE = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
R = sys.argv[3] if len(sys.argv) > 3 else "32"
MOVING_TAU = sys.argv[4] if len(sys.argv) > 4 else "0.08"
CHAR_TAU = sys.argv[5] if len(sys.argv) > 5 else "0.06"
MINFLOW = sys.argv[6] if len(sys.argv) > 6 else "0.5"
t = BASE.read_text(encoding="utf-8")
assert "[plate]" in t, "input must be the plate variant"

COH = """
//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND NEXT
//!BIND LUMA_A_H
//!BIND LUMA_B_H
//!BIND FLOW_H_AB
//!BIND PLATE_TEX
//!SAVE FLOW_C
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!DESC [coherent] one motion per moving thing: the trimmed mean of the dense flow over the character texels around this one
const int COH_R = %s;                 // half-res texels: the vote's radius (a character-sized window)
const float COH_MOVING_TAU = %s;      // A/B luma difference that marks the moving region
const float COH_CHAR_TAU = %s;        // a texel further than this from a confident plate is character
const float COH_MINFLOW = %s;         // half-res texels; a texel whose dense flow is smaller found nothing and does not vote
bool is_char(vec2 p, vec3 c) {
    vec4 pl = PLATE_TEX_tex(p);
    return pl.a < 2.0 || length(c - pl.rgb) > COH_CHAR_TAU;
}
vec4 hook() {
    vec2 uv = FLOW_H_AB_pos;
    vec2 f0 = FLOW_H_AB_tex(uv).xy;
    bool moving = abs(LUMA_A_H_tex(uv).r - LUMA_B_H_tex(uv).r) > COH_MOVING_TAU;
    bool char_a = is_char(uv, HOOKED_tex(uv).rgb);
    bool char_b = is_char(uv, NEXT_tex(uv).rgb);
    if (!moving || !(char_a || char_b))
        return vec4(f0, 0.0, 0.0);
    vec2 sum = vec2(0.0); float n = 0.0;
    for (int j = -COH_R; j <= COH_R; j += 4) {
        for (int i = -COH_R; i <= COH_R; i += 4) {
            vec2 p = uv + vec2(float(i), float(j)) * FLOW_H_AB_pt;
            if (abs(LUMA_A_H_tex(p).r - LUMA_B_H_tex(p).r) <= COH_MOVING_TAU) continue;
            if (!is_char(p, HOOKED_tex(p).rgb)) continue;              // only a texel that is character IN A carries the A->B motion
            vec2 f = FLOW_H_AB_tex(p).xy;
            if (length(f) < COH_MINFLOW) continue;
            sum += f; n += 1.0;
        }
    }
    if (n < 6.0) return vec4(f0, 0.0, 0.0);
    vec2 m = sum / n;
    sum = vec2(0.0); n = 0.0;
    for (int j = -COH_R; j <= COH_R; j += 4) {
        for (int i = -COH_R; i <= COH_R; i += 4) {
            vec2 p = uv + vec2(float(i), float(j)) * FLOW_H_AB_pt;
            if (abs(LUMA_A_H_tex(p).r - LUMA_B_H_tex(p).r) <= COH_MOVING_TAU) continue;
            if (!is_char(p, HOOKED_tex(p).rgb)) continue;
            vec2 f = FLOW_H_AB_tex(p).xy;
            if (length(f) < COH_MINFLOW || length(f - m) > 2.0) continue;
            sum += f; n += 1.0;
        }
    }
    if (n < 6.0) return vec4(f0, 0.0, 0.0);
    return vec4(sum / n, 1.0, 0.0);
}
""" % (R, MOVING_TAU, CHAR_TAU, MINFLOW)

i = t.index("//!DESC [high] motion-compensated warp")
j = t.rfind("//!HOOK FRAME_MIX", 0, i)
t = t[:j] + COH.lstrip("\n") + "\n" + t[j:]
# the warp binds FLOW_C and reads it in place of the dense flow
wi = t.index("//!HOOK FRAME_MIX", t.index("//!DESC [coherent]"))
we = t.index("//!DESC [high] motion-compensated warp", wi)
hdr = t[wi:we]
assert hdr.count("//!BIND FLOW_H_AB\n") == 1, hdr
t = t[:wi] + hdr.replace("//!BIND FLOW_H_AB\n", "//!BIND FLOW_H_AB\n//!BIND FLOW_C\n", 1) + t[we:]
old = "    vec2 flow_ab = FLOW_H_AB_tex(HOOKED_pos).xy * 2.0 * HOOKED_pt;\n"
assert t.count(old) == 1, t.count(old)
t = t.replace(old, "    vec2 flow_ab = FLOW_C_tex(HOOKED_pos).xy * 2.0 * HOOKED_pt;     // [coherent] one motion per moving thing\n")
OUT.write_text(t, encoding="utf-8", newline="\n")
print("%s: coherent pass (R %s, moving %s, char %s, minflow %s) + warp on FLOW_C, %d passes" % (OUT.name, R, MOVING_TAU, CHAR_TAU, MINFLOW, t.count("//!HOOK")))
