#!/usr/bin/env python3
"""Turn the tridirectional shader into an acceleration visualiser.

    ./trivis.py <tridirectional.glsl> <out.glsl>

Replaces only the FINAL hook(), the same way flowvis.py does, so what it
renders is exactly the fields the given shader computed -- not a
reimplementation that could drift from it.

THE DESIGN PROBLEM. A flow field is 2D and the colour wheel encodes exactly
2D: hue for direction, saturation for magnitude. Acceleration is a SECOND 2D
field, and the wheel has no third and fourth dimension to extend into.
Overloading it -- brightness for |a|, say -- collides with saturation and
makes both unreadable, and the one thing you most need to see is precisely
where the two fields DISAGREE.

So: do not extend the wheel. Show four separable panels, each honest about
one quantity, on a shared layout so a texel keeps its position across all
four. A 2x2 grid at half resolution each:
    +----------------------+----------------------+
    | VELOCITY             | ACCELERATION         |
    | wheel, +-10 px/int   | wheel, +-10 px/int^2 |
    | (matches flowvis.py) | same encoding, so    |
    |                      | the two are directly |
    |                      | comparable by eye    |
    +----------------------+----------------------+
    | CORRECTION           | TRUST                |
    | |a|/8 px heat map:   | the confidence gate: |
    | how far a 2-frame    | green where accel is |
    | shader misplaces     | believed, red where  |
    | this texel           | it was discarded     |
    +----------------------+----------------------+

The bottom-left panel is the one that matters most and is the reason this
tool exists rather than just two flowvis renders. Acceleration in px/int^2
is not directly meaningful to a viewer; what is meaningful is the resulting
PLACEMENT ERROR, |a|/8 px at mid-interval, which is exactly what the
tridirectional model exists to remove. Reading it as "how wrong is the
bidirectional shader here" makes the whole hypothesis visible at a glance:
if that panel is black everywhere on your content, there is nothing for a
3-frame shader to win.

The bottom-right panel is the honesty check. Acceleration is a small
residual of two large near-cancelling flows, so it is meaningless wherever
those flows do not cancel -- occlusion boundaries above all. Without seeing
where the gate fired you cannot tell a real acceleration field from noise
that happened to survive.
"""
import pathlib
import sys

if len(sys.argv) < 3:
    sys.exit("usage: trivis.py <tridirectional.glsl> <out.glsl>")

src, dst = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
text = src.read_text()
i = text.rfind("vec4 hook() {")
if i < 0:
    sys.exit(f"no final hook() in {src}")
if "FLOW_H_AT" not in text:
    sys.exit(f"{src} has no anchor->outer flow -- is that a tridirectional build?")

BODY = """vec4 hook() {
    vec2 cell  = floor(HOOKED_pos * 2.0);
    vec2 local = fract(HOOKED_pos * 2.0);
    int panel  = int(cell.y) * 2 + int(cell.x);

    // Same timing and solve as the real final pass, so what is drawn is what
    // the shader actually used. Kept textually parallel to it on purpose.
    bool outer_future = rts_mix[1] > 0.0;
    float tA = outer_future ? rts_mix[0] : rts_mix[1];
    float tB = outer_future ? rts_mix[1] : rts_mix[2];
    float tT = outer_future ? rts_mix[2] : rts_mix[0];
    float L  = tB - tA;

    vec2 flow_ab = FLOW_H_AB_tex(local).xy * 2.0 * HOOKED_pt;
    vec2 f_str = (outer_future ? FLOW_H_BA_tex(local).xy
                               : FLOW_H_AB_tex(local).xy) * 2.0 * HOOKED_pt;
    vec2 f_out = FLOW_H_AT_tex(local).xy * 2.0 * HOOKED_pt;

    float t_anch  = outer_future ? tB : tA;
    float tau_str = ((outer_future ? tA : tB) - t_anch) / L;
    float tau_out = (tT - t_anch) / L;

    vec2 accel_raw = 2.0 * (f_out * tau_str - f_str * tau_out)
                   / (tau_out * tau_str * (tau_out - tau_str));

    float amag_px = length(accel_raw) / length(HOOKED_pt);
    vec2 fab = FLOW_H_AB_tex(local).xy * 2.0 * HOOKED_pt;
    vec2 fba = FLOW_H_BA_tex(local + fab).xy * 2.0 * HOOKED_pt;
    float rt_px = length(fab + fba) / length(HOOKED_pt);
    float trust = 1.0 - smoothstep(ACCEL_TRUST_LO, ACCEL_TRUST_HI, rt_px);
    vec2 accel = accel_raw * trust;
    vec2 amax = ACCEL_MAX_PX * HOOKED_pt;
    accel = clamp(accel, -amax, amax);

    // Panel 0: velocity. flowvis.py's exact encoding and gain, so a
    // tridirectional render can be laid beside a bidirectional one.
    if (panel == 0) {
        vec2 v = flow_ab / HOOKED_pt;
        return vec4(0.5 + v.x * 0.05, 0.5 + v.y * 0.05, 0.5, 1.0);
    }

    // Panel 1: acceleration, SAME encoding and gain as panel 0. Identical
    // scaling is the point: it makes "is the acceleration comparable to the
    // velocity here?" a direct visual comparison, and a texel where it is
    // means the quadratic model is being asked to explain something large.
    if (panel == 1) {
        vec2 a = accel / HOOKED_pt;
        return vec4(0.5 + a.x * 0.05, 0.5 + a.y * 0.05, 0.5, 1.0);
    }

    // Panel 2: the placement error a 2-frame shader commits, |a|/8 px at
    // mid-interval. Blue -> cyan -> yellow -> red across 0 .. 2px, which
    // spans the whole physically reachable range (O3, the strongest case
    // the search can still track, peaks near 1.65px).
    if (panel == 2) {
        float err = length(accel / HOOKED_pt) / 8.0;
        float u = clamp(err / 2.0, 0.0, 1.0);
        vec3 c = u < 0.5 ? mix(vec3(0.0, 0.0, 0.3), vec3(0.0, 0.9, 0.9), u * 2.0)
                         : mix(vec3(0.0, 0.9, 0.9), vec3(1.0, 0.1, 0.0), (u - 0.5) * 2.0);
        return vec4(c, 1.0);
    }

    // Panel 3: the confidence gate. Green = accepted, red = discarded,
    // dimmed by how much acceleration was on offer -- so a red region that
    // had nothing to discard stays dark and does not read as a problem.
    float mag = clamp(amag_px / 8.0, 0.0, 1.0);
    return vec4(mix(vec3(0.06), vec3(1.0, 0.15, 0.0), (1.0 - trust) * mag)
              + vec3(0.0, 0.55, 0.0) * trust * mag, 1.0);
}
"""

dst.write_text(text[:i] + BODY, newline="\n")
print(f"  {dst.name}: velocity | acceleration / correction | trust")
