#!/usr/bin/env python3
"""Generate a "human-reading" view of any interpolation shader.

    gen_human_reading.py <base.glsl> <out.glsl> <velocity|acceleration|jerk>

The base is left untouched: its final pass is kept verbatim (renamed to
save READ_PICTURE), and three passes are appended that port the Metal
demo's Reading decode (QuadDemoApp.swift, constants measured 2026-09-01):

  READ_FIELD  the chosen field in px at 1/8 resolution. For the tri/quad
              family this is a clone of the base's own final pass with its
              TRI_DIAG mode switched on, so the field is exactly what the
              shader under test computes. For the bi family it is the
              half-res flow the warp uses (velocity only).
  READ_POOL   13x13 box at 8 px spacing (+/-48 px) then an EMA across
              frames in a STORAGE accumulator (alpha 0.12).
  FRAME_MIX   hue = direction, visibility/saturation = magnitude above the
              pooled floor, painted over the dimmed picture. Gates are per
              field: velocity 1.0/2.0/3.0 px, acceleration and jerk
              0.12/0.22/0.30 px (the demo's measured values).

Because the tail is generated from whichever base you pass, the view
attunes to the variant under test (-seeded, -variational, ...) instead of
mirroring the stock base by hand.
"""
import pathlib
import re
import sys

FIELDS = {
    "velocity":     dict(mode=7, gates=(1.0, 2.0, 3.0), unit="px/interval"),
    "acceleration": dict(mode=2, gates=(0.12, 0.22, 0.30), unit="px/interval^2"),
    "jerk":         dict(mode=5, gates=(0.12, 0.22, 0.30), unit="px/interval^3"),
}

if len(sys.argv) not in (4, 5) or sys.argv[3] not in FIELDS or (len(sys.argv) == 5 and sys.argv[4] != "relative"):
    sys.exit(__doc__ + "\nOptional 4th argument `relative`: read motion relative to the frame's dominant motion.\n")
HERE = pathlib.Path(__file__).resolve().parent
SHADERS = HERE.parent / "shaders"


def shader_arg(s):
    """A bare file name means a shader in shaders/; a path with a directory is used as given."""
    p = pathlib.Path(s)
    return p if p.parent != pathlib.Path(".") else SHADERS / p


SRC, DST, FIELD = shader_arg(sys.argv[1]), shader_arg(sys.argv[2]), sys.argv[3]
relative = 1 if len(sys.argv) == 5 else 0
spec = FIELDS[FIELD]
text = SRC.read_text(encoding="utf-8")


def must_sub(pattern, repl, s, count, flags=0):
    new, n = re.subn(pattern, repl, s, flags=flags)
    assert n == count, f"{pattern!r}: expected {count} substitutions, made {n}"
    return new


# ---- split off the final pass (the one that saves FRAME_MIX) ----
hooks = [m.start() for m in re.finditer(r"^//!HOOK FRAME_MIX\n", text, re.M)]
assert hooks, "no FRAME_MIX hook in base"
final_start = None
for h in reversed(hooks):
    chunk = text[h:]
    directives = chunk.split("\n\n", 1)[0]
    if "//!SAVE FRAME_MIX" in directives:
        final_start = h
        break
assert final_start is not None, "no pass saves FRAME_MIX"
head, final = text[:final_start], text[final_start:]
assert final.count("//!SAVE FRAME_MIX") == 1

is_tri = "const int TRI_DIAG" in final

# ---- pass 1: the base's real output, kept verbatim, saved as READ_PICTURE ----
picture = must_sub(r"^//!SAVE FRAME_MIX$", "//!SAVE READ_PICTURE", final, 1, re.M)

# ---- pass 2: the field in px at 1/8 resolution ----
if is_tri:
    field = final
    field = must_sub(r"^//!SAVE FRAME_MIX$", "//!SAVE READ_FIELD", field, 1, re.M)
    field = must_sub(r"^//!WIDTH HOOKED\.w$", "//!WIDTH HOOKED.w 8 /", field, 1, re.M)
    field = must_sub(r"^//!HEIGHT HOOKED\.h$", "//!HEIGHT HOOKED.h 8 /", field, 1, re.M)
    field = must_sub(r"^//!DESC .*$",
                     f"//!DESC [reading] {FIELD} field ({spec['unit']}) at 1/8 -- the base's own final pass in diag mode",
                     field, 1, re.M)
    field = must_sub(r"^const int TRI_DIAG = 0;", f"const int TRI_DIAG = {spec['mode']};", field, 1, re.M)
    field = must_sub(r"^const int DIAG_HOLD_ANCHOR = 0;", "const int DIAG_HOLD_ANCHOR = 1;", field, 1, re.M)
    # no 24-px marker corner: the whole texture is field
    field = must_sub(r"\n[ \t]*if \(HOOKED_pos\.x < 24\.0 \* HOOKED_pt\.x && HOOKED_pos\.y < 24\.0 \* HOOKED_pt\.y\)\n[ \t]*return tri_diag_marker\(\);",
                     "", field, 1)
    # raw px instead of the 0.5-offset full-scale encoding (float FBO, same as the flow textures)
    field = must_sub(r"return vec4\(0\.5 \+ \((\w+) / HOOKED_pt\) \* \(0\.5 / \w+_DIAG_FS\), 0\.5, 1\.0\);",
                     r"return vec4(\1 / HOOKED_pt, 0.0, 1.0);", field, 4)
else:
    assert FIELD == "velocity", "the bi family exposes velocity only (its warp uses one flow)"
    assert "//!BIND FLOW_H_AB" in final, "bi final pass does not bind FLOW_H_AB"
    field = """//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FLOW_H_AB
//!SAVE READ_FIELD
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!DESC [reading] velocity field (px/interval) at 1/8 -- the half-res flow the warp uses

vec4 hook() {
    // FLOW_H is stored in half-resolution texels; x2 gives full-res px.
    return vec4(FLOW_H_AB_tex(HOOKED_pos).xy * 2.0, 0.0, 1.0);
}
"""

lo, hi, sat_full = spec["gates"]

# ---- pass 3: pool + EMA (STORAGE accumulator persists across frames) ----
pool = """//!TEXTURE READ_ACC
//!SIZE 480 270
//!FORMAT rgba32f
//!STORAGE

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND READ_FIELD
//!BIND READ_ACC
//!SAVE READ_POOL
//!WIDTH HOOKED.w 8 /
//!HEIGHT HOOKED.h 8 /
//!DESC [reading] 13x13 pool at 8 px spacing, then EMA across frames

// Measured on the Metal demo (2026-09-01): pooling +/-48 px drops the
// static-background p95 from 0.52 to 0.10 px; the EMA lifts a mover's
// direction coherence from 0.74 to 0.92. Alpha is per OUTPUT frame, as
// in the demo's 60 Hz present. Set READ_EMA_ALPHA to 1.0 for a
// frame-by-frame reading (no memory) -- e.g. fast oscillators, whose
// velocity averages toward zero under any EMA.
const float READ_EMA_ALPHA = 0.12;
const int   READ_POOL_R    = 6;      // 13x13 taps

vec4 hook() {
    ivec2 coord = ivec2(READ_FIELD_pos * READ_FIELD_size);
    vec2 fpx = vec2(0.0);
    for (int j = -READ_POOL_R; j <= READ_POOL_R; j++)
        for (int i = -READ_POOL_R; i <= READ_POOL_R; i++)
            fpx += READ_FIELD_tex(READ_FIELD_pos + vec2(float(i), float(j)) * READ_FIELD_pt).xy;
    fpx /= float((2 * READ_POOL_R + 1) * (2 * READ_POOL_R + 1));
    vec2 prev = imageLoad(READ_ACC, coord).xy;
    vec2 acc = mix(prev, fpx, READ_EMA_ALPHA);
    imageStore(READ_ACC, coord, vec4(acc, 0.0, 1.0));
    return vec4(acc, 0.0, 1.0);
}
"""

# ---- optional: the frame's dominant motion, once per frame, 1x1 ----
dom = """//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND READ_POOL
//!SAVE READ_DOM
//!WIDTH HOOKED.w 128 /
//!HEIGHT HOOKED.h 128 /
//!DESC [reading] dominant (camera) motion: the mode of the pooled field on a 16x9 grid (tiny pass; every texel computes the same value)

// A mode, not a mean: mean-shift from the border ring's mean (the frame
// edge is nearly always camera, not subject), READ_DOM_ITERS steps of
// "mean of the samples within READ_DOM_TRIM px of the current estimate".
// A subject filling a third of the frame does not move a mode; it moves
// a mean a long way. (An all-pairs search was tried first: 144x144 per
// texel made the pass take minutes per frame on the RX 6600.)
const float READ_DOM_TRIM  = 2.0;
const int   READ_DOM_ITERS = 4;

vec2 read_grid(int i, int j) {
    return READ_POOL_tex((vec2(float(i), float(j)) + 0.5) / vec2(16.0, 9.0)).xy;
}

// Mean-shift from one start finds the mode nearest that start, which is
// not always the biggest one (the frame edge often reads as zero motion
// where the estimator has nothing to match). So: six starts -- the whole
// grid's mean, the border ring's mean, the four quadrant means -- each
// shifted READ_DOM_ITERS times, and the converged mode with the most
// support wins.
vec2 region_mean(int i0, int i1, int j0, int j1, bool ring) {
    vec2 acc = vec2(0.0);
    float n = 0.0;
    for (int j = j0; j < j1; j++)
        for (int i = i0; i < i1; i++)
            if (!ring || i == 0 || i == 15 || j == 0 || j == 8) { acc += read_grid(i, j); n += 1.0; }
    return acc / max(n, 1.0);
}

vec3 shifted(vec2 start) {
    vec2 dom = start;
    float n = 0.0;
    for (int it = 0; it < READ_DOM_ITERS; it++) {
        vec2 acc = vec2(0.0);
        n = 0.0;
        for (int j = 0; j < 9; j++)
            for (int i = 0; i < 16; i++) {
                vec2 v = read_grid(i, j);
                if (length(v - dom) < READ_DOM_TRIM) { acc += v; n += 1.0; }
            }
        if (n > 0.0) dom = acc / n;
    }
    return vec3(dom, n);
}

vec4 hook() {
    vec3 best = shifted(region_mean(0, 16, 0, 9, false));
    vec3 c;
    c = shifted(region_mean(0, 16, 0, 9, true)); if (c.z > best.z) best = c;
    c = shifted(region_mean(0, 8, 0, 5, false)); if (c.z > best.z) best = c;
    c = shifted(region_mean(8, 16, 0, 5, false)); if (c.z > best.z) best = c;
    c = shifted(region_mean(0, 8, 5, 9, false)); if (c.z > best.z) best = c;
    c = shifted(region_mean(8, 16, 5, 9, false)); if (c.z > best.z) best = c;
    return vec4(best.xy, best.z / 144.0, 1.0);   // .z = share of the grid that agrees with the camera
}
"""

present = f"""//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND READ_PICTURE
//!BIND READ_POOL
{"//!BIND READ_DOM" if relative else "//!DESC (no dominant-motion pass)"}
//!SAVE FRAME_MIX
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!DESC [reading] {FIELD} painted over the picture: hue = direction, colour = magnitude above the floor

// Gates in {spec['unit']}: below READ_VIS_LO nothing is drawn, colour
// reaches full saturation at READ_SAT_FULL. The demo's measured values
// for this field.
const float READ_VIS_LO   = {lo};
const float READ_VIS_HI   = {hi};
const float READ_SAT_FULL = {sat_full};
// 1.0 = the full reading (dimmed picture + colour), 0.0 = plain picture.
const float READ_OPACITY  = 1.0;
const float READ_PICTURE_LUMA = 0.35;
// READ_RELATIVE 1 = motion relative to the frame's dominant motion (a
// camera pan otherwise colours the whole frame); a generation-time choice
// because it adds a pass. Informational here.
const int   READ_RELATIVE = {relative};

vec3 read_hsv2rgb(vec3 c) {{
    vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
    return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
}}

vec4 hook() {{
    // 4-tap soften: the pooled field keeps a faint per-texel checker
    // from the raw field that would dither the gate.
    vec2 fpx = vec2(0.0);
    fpx += READ_POOL_tex(HOOKED_pos + vec2( 2.0,  2.0) * HOOKED_pt).xy;
    fpx += READ_POOL_tex(HOOKED_pos + vec2(-2.0,  2.0) * HOOKED_pt).xy;
    fpx += READ_POOL_tex(HOOKED_pos + vec2( 2.0, -2.0) * HOOKED_pt).xy;
    fpx += READ_POOL_tex(HOOKED_pos + vec2(-2.0, -2.0) * HOOKED_pt).xy;
    fpx *= 0.25;
{"    fpx -= READ_DOM_tex(vec2(0.5)).xy;   // the camera's motion, found once per frame by the pass above" if relative else "    // (not relative to the camera: generate with the `relative` argument for that)"}
    float mag = length(fpx);
    float vis = smoothstep(READ_VIS_LO, READ_VIS_HI, mag) * 0.9;
    // borders: the pool clamps onto frame-edge flow garbage
    vec2 bpx = min(HOOKED_pos, 1.0 - HOOKED_pos) * HOOKED_size;
    vis *= smoothstep(4.0, 28.0, min(bpx.x, bpx.y));
    float sat = 0.95 * smoothstep(READ_VIS_LO, READ_SAT_FULL, mag);
    // screen space, +y down: red = moving right, cyan = left,
    // purple/blue = down, yellow-green = up (the demo's convention)
    float hue = fract(atan(fpx.y, fpx.x) / (2.0 * 3.14159265) + 1.0);
    vec4 pic = READ_PICTURE_tex(HOOKED_pos);
    float lum = dot(pic.rgb, vec3(0.2126, 0.7152, 0.0722));
    vec3 reading = mix(vec3(lum * READ_PICTURE_LUMA), read_hsv2rgb(vec3(hue, sat, 1.0)), vis);
    return vec4(mix(pic.rgb, reading, READ_OPACITY), pic.a);
}}
"""

header = f"""// {DST.name}
//
// HUMAN-READING VIEW -- not for production use. Generated from
// {SRC.name} by
//   tests/gen_human_reading.py {SRC.name} {DST.name} {FIELD}
// The base is byte-for-byte intact up to and including its final pass,
// which is kept as the picture; the appended passes draw the {FIELD}
// field the way the Metal demo's "Reading" display does. Regenerate
// rather than edit: the point is that this view can never drift from
// the shader it is reading.
//
"""

out = header + head + picture + "\n" + field + "\n" + pool + "\n" + (dom + "\n" if relative else "") + present
assert out.count("//!SAVE FRAME_MIX") == 1
DST.write_text(out, encoding="utf-8", newline="\n")
print(f"{DST.name}: {out.count(chr(10))} lines, family={'tri/quad' if is_tri else 'bi'}, field={FIELD}, "
      f"passes={out.count('//!SAVE ')}")
