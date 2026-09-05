#!/usr/bin/env python3
"""The line-art shader: distance transforms under the matcher and a level-set morph in the warp.

    ./build_lineart.py <out.glsl> <plate-variant.glsl> [LINE_TAU=0.10] [DT_SCALE=24] [DT_MIX=0.5] [LINE_W=0.7]

Prior art and credit: ANI-PRIOR-ART.md in this folder (Narita/Hirakawa/Aizawa 2019 for the distance
transform under the flow; Rong/Tan 2006 for jump flooding; Cohen-Or/Solomovici/Levin 1998 for the
level-set morph; Chen/Zwicker 2022 for the distance transform in the synthesis).

What it adds to the plate variant of the animation shader, in file order (pass order):
  1. [lineart] LINE_A / LINE_B at half res: the line art of each frame -- where the luma gradient across a
     texel exceeds LINE_TAU. Ink lines and the boundaries between flat fills are both curves.
  2. [lineart] jump flooding: JF_A / JF_B carry, per texel, the half-res texel coordinate of the nearest
     line texel; the seed pass then log2(width) passes with halving strides. The last pass writes the
     distance (in half-res texels) into DT_A / DT_B.
  3. The luma pyramid's coarsest source passes (LUMA_A_S, LUMA_B_S and the S-level lumas) are fed
     mix(luma, dt / DT_SCALE, DT_MIX) instead of luma alone, so flat fills carry a gradient the block
     matcher can follow (Narita); the finer levels are derived from the same source in the base already.
  4. The warp morphs the two distance fields under the flow -- D_t = (1 - t) D_A(x - f t) + t D_B(x + f (1 - t))
     -- and paints ink where D_t is within LINE_W of zero: ONE in-between line where the shipped warp
     blends two. The fill is the plate-arbitrated blend the plate variant already produces.
"""
import pathlib
import re
import sys

OUT, BASE = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
LINE_TAU = sys.argv[3] if len(sys.argv) > 3 else "0.10"
DT_SCALE = sys.argv[4] if len(sys.argv) > 4 else "24.0"
DT_MIX = sys.argv[5] if len(sys.argv) > 5 else "0.5"
LINE_W = sys.argv[6] if len(sys.argv) > 6 else "0.7"
t = BASE.read_text(encoding="utf-8")
assert "[plate]" in t, "input must be the plate variant (build_plate.py)"


def sub(text, old, new, n=1, what=""):
    assert text.count(old) == n, "%s: expected %d of %r, found %d" % (what, n, old[:60], text.count(old))
    return text.replace(old, new)


def line_pass(letter, frame):
    return """//!HOOK FRAME_MIX
//!BIND %s
//!SAVE LINE_%s
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!COMPONENTS 1
//!DESC [lineart] the line art of frame %s at half res: where the luma gradient exceeds LINE_TAU
const float LINE_TAU = %s;
float lum(vec2 p) { return dot(%s_tex(p).rgb, vec3(0.299, 0.587, 0.114)); }
vec4 hook() {
    vec2 p = %s_pos; vec2 d = %s_pt;
    float gx = lum(p + vec2(d.x, 0.0)) - lum(p - vec2(d.x, 0.0));
    float gy = lum(p + vec2(0.0, d.y)) - lum(p - vec2(0.0, d.y));
    return vec4(length(vec2(gx, gy)) > LINE_TAU ? 1.0 : 0.0, 0.0, 0.0, 0.0);
}
""" % (frame, letter, letter, LINE_TAU, frame, frame, frame)


def jfa_passes(letter):
    """Seed pass, then strides 512..1 (enough for a half-res width up to 1024, i.e. 2K sources; larger
    strides are harmless on smaller frames), the last also writing the distance."""
    out = ["""//!HOOK FRAME_MIX
//!BIND LINE_%s
//!SAVE JF_%s
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!DESC [lineart] jump flooding seed for frame %s: a line texel is its own nearest seed
vec4 hook() {
    vec2 tex = floor(LINE_%s_pos * LINE_%s_size);
    bool line = LINE_%s_tex(LINE_%s_pos).r > 0.5;
    return line ? vec4(tex, 1.0, 0.0) : vec4(-1.0, -1.0, 0.0, 0.0);
}
""" % (letter, letter, letter, letter, letter, letter, letter)]
    strides = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    for k, s in enumerate(strides):
        last = (k == len(strides) - 1)
        out.append("""//!HOOK FRAME_MIX
//!BIND JF_%s
//!SAVE %s
//!WIDTH HOOKED.w 2 /
//!HEIGHT HOOKED.h 2 /
//!DESC [lineart] jump flooding for frame %s, stride %d%s
vec4 hook() {
    vec2 size = JF_%s_size; vec2 tex = floor(JF_%s_pos * size);
    vec4 best = JF_%s_tex(JF_%s_pos);
    float bd = best.z > 0.5 ? length(best.xy - tex) : 1.0e9;
    for (int j = -1; j <= 1; j++) {
        for (int i = -1; i <= 1; i++) {
            if (i == 0 && j == 0) continue;
            vec2 q = tex + vec2(float(i), float(j)) * %d.0;
            if (q.x < 0.0 || q.y < 0.0 || q.x >= size.x || q.y >= size.y) continue;
            vec4 c = JF_%s_tex((q + 0.5) / size);
            if (c.z < 0.5) continue;
            float d = length(c.xy - tex);
            if (d < bd) { bd = d; best = c; }
        }
    }
    %s
}
""" % (letter, ("DT_" + letter) if last else ("JF_" + letter), letter, s, " (and the distance)" if last else "",
       letter, letter, letter, letter, s, letter,
       ("return vec4(min(bd, 1.0e4), best.xy, best.z);" if last else "return best;")))
    return "\n".join(out)


PRE = line_pass("A", "HOOKED") + "\n" + line_pass("B", "NEXT") + "\n" + jfa_passes("A") + "\n" + jfa_passes("B") + "\n"

# 1. the new passes go in front of the first pass of the base (the luma pyramid's coarsest level)
first = t.index("//!HOOK FRAME_MIX")
t = t[:first] + PRE + t[first:]

# 2. the coarsest luma source: the S-level luma passes sample the frame; feed them luma + distance.
#    The base's S-level passes are `LUMA_A_S` (from HOOKED) and `LUMA_B_S` (from NEXT); find their hooks.
def feed(text, save, frame, letter):
    i = text.index("//!SAVE %s\n" % save)
    hs = text.rfind("//!HOOK FRAME_MIX", 0, i)
    he = text.index("vec4 hook() {", i)
    hdr = text[hs:he]
    assert "//!BIND %s\n" % frame in hdr, (save, hdr[:200])
    hdr2 = hdr.replace("//!BIND %s\n" % frame, "//!BIND %s\n//!BIND DT_%s\n" % (frame, letter), 1)
    body_end = text.index("\n}\n", he) + 3
    body = text[he:body_end]
    m = re.search(r"dot\(%s_tex\(([^)]*)\)\.rgb, vec3\(0\.299, 0\.587, 0\.114\)\)" % frame, body)
    assert m, (save, body[:300])
    pos = m.group(1)
    body2 = body.replace(m.group(0), "mix(%s, clamp(DT_%s_tex(%s).r / %s, 0.0, 1.0), %s)" % (m.group(0), letter, pos, DT_SCALE, DT_MIX), 1)
    return text[:hs] + hdr2 + body2 + text[body_end:]


# every level of the pyramid samples the frame directly in this base, so every level gets the same source
for lvl in ("S", "E", "Q", "H"):
    for frame, letter in (("HOOKED", "A"), ("NEXT", "B")):
        t = feed(t, "LUMA_%s_%s" % (letter, lvl), frame, letter)

# 3. the warp: bind the distance fields and paint the morphed line
i = t.index("//!DESC [high] motion-compensated warp")
hs = t.rfind("//!HOOK FRAME_MIX", 0, i)
hdr = t[hs:i]
assert hdr.count("//!BIND HOOKED\n") == 1
t = t[:hs] + hdr.replace("//!BIND HOOKED\n", "//!BIND HOOKED\n//!BIND DT_A\n//!BIND DT_B\n", 1) + t[i:]
old = "    return mix(warped_a, warped_b, mix_t);\n}"
t = sub(t, old, """    vec4 fill = mix(warped_a, warped_b, mix_t);
    // THE LEVEL-SET MORPH ([lineart]): the two distance fields, each read where the warp reads its frame,
    // blended by time; the in-between line is where the blend is within LINE_W of zero. One curve between
    // two drawings, never two superimposed. Ink is the darker of the two warped samples.
    const float LINE_W = %s;
    // Only where something moves: a still texel's two candidates agree and its fill is already exact;
    // morphing there would paint every edge of a detailed static background as a line (measured: -6.5 dB
    // outside the moving band on a checkered backdrop). And only ink that is ink: the darker candidate
    // must actually be dark, or the level set of a fill boundary would be inked.
    bool moving = length(flow_ab) > 0.25 * HOOKED_pt.x
               || abs(dot(HOOKED_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)) - dot(NEXT_tex(NEXT_pos).rgb, vec3(0.299, 0.587, 0.114))) > 0.08;
    if (!moving) return fill;
    float da = DT_A_tex(HOOKED_pos - flow_ab * mix_t).r;
    float db = DT_B_tex(NEXT_pos + flow_ab * (1.0 - mix_t)).r;
    float dt = mix(da, db, mix_t);
    vec4 ink = min(warped_a, warped_b);
    float dark = 1.0 - smoothstep(0.25, 0.45, dot(ink.rgb, vec3(0.299, 0.587, 0.114)));
    float line = (1.0 - smoothstep(LINE_W - 0.4, LINE_W + 0.6, dt)) * dark;
    return mix(fill, ink, line);
}""" % LINE_W, what="warp return")
# the plate's arbitration returns before the blend; it must also paint the line -- route it through the same tail
t = sub(t, "        if (min(da, db) < PLATE_DISAGREE_TAU)\n            return (da < db) ? warped_a : warped_b;\n",
        "        if (min(da, db) < PLATE_DISAGREE_TAU) {\n            vec4 pick = (da < db) ? warped_a : warped_b;\n"
        "            warped_a = pick; warped_b = pick;\n        }\n", what="plate arbitration")
OUT.write_text(t, encoding="utf-8", newline="\n")
n = t.count("//!HOOK")
print("%s: line passes 2, jump flooding 2 x 11, matcher fed luma+dt (scale %s, mix %s), level-set warp (LINE_W %s); %d passes" % (OUT.name, DT_SCALE, DT_MIX, LINE_W, n))
