#!/usr/bin/env python3
"""THE CUT GATE ASKS WHETHER MOTION EXPLAINS THE DIFFERENCE: a switch for gen_variational.py (2026-10-01, ENERGY-TRANSFER.md
"The per-level trust gate, returned to", C1 and C2).

The warp's scene-cut gate is a hard switch to the nearer source frame whenever the mean |A - B| on a sparse grid of the
1/16 level exceeds 0.125 (TESTING.md, "Scene cuts"). It measures how DIFFERENT two frames are, not whether motion
explains the difference, and a high-contrast print panning by about half its period reads 0.15-0.17: the warp holds a
frame although the field is right (C1: the cut gate out of reach lifts the frame-filling weave pan by 6.6 and 10.9 dB).

add_scene_res(t) -- one pass, one invocation, right before the warp (after the final flow): on the same 24 x 24 sparse
grid, the mean |A(x) - B(x + f(x))| with f the final half-level flow (what motion leaves unexplained) and the mean
|A(x) - B(x)| (the frames' difference, unmoved), both at full resolution, single taps: SCENE_RES.rg. On its own it
changes no output (the probe tests/probes/trust/cutstat.py reads it).
CUT_MOTION=1 at generation -- add_cut_motion(t): SCENE_RES, and the warp holds a frame only if the cut statistic is over
its threshold AND the final flow leaves more than CUT_EXPLAINED of the difference unexplained.
"""

CUT_EXPLAINED = 0.3        # the share of the frames' difference the flow must leave for a cut: every real cut read 0.37 or more, the weave pans 0.26 or less (C2a)


def _once(t, a, what):
    n = t.count(a)
    assert n == 1, f"cut motion: {what}: anchor found {n} times"


PASS = """//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND NEXT
//!BIND FLOW_H_AB
//!SAVE SCENE_RES
//!WIDTH 1
//!HEIGHT 1
//!COMPONENTS 2
//!DESC [cut] the scene-cut statistic, motion-compensated: what the final flow leaves of the frames' difference (.r), and the difference unmoved (.g)
vec4 hook() {
    const int N = 24;
    float r = 0.0, d0 = 0.0;
    for (int y = 0; y < N; y++) {
        for (int x = 0; x < N; x++) {
            vec2 uv = (vec2(float(x), float(y)) + 0.5) / float(N);
            float a = dot(HOOKED_tex(uv).rgb, vec3(0.299, 0.587, 0.114));
            vec2 f = FLOW_H_AB_tex(uv).xy * 2.0 * HOOKED_pt;          // half-level texels -> px -> uv
            r += abs(a - dot(NEXT_tex(uv + f).rgb, vec3(0.299, 0.587, 0.114)));
            d0 += abs(a - dot(NEXT_tex(uv).rgb, vec3(0.299, 0.587, 0.114)));
        }
    }
    return vec4(r / float(N * N), d0 / float(N * N), 0.0, 0.0);
}

"""


def add_scene_res(t):
    a = "//!DESC [high] motion-compensated warp\n"
    _once(t, a, "the warp")
    i = t.rindex("//!HOOK FRAME_MIX\n", 0, t.index(a))                 # the warp's own header
    return t[:i] + PASS + t[i:]


def add_cut_motion(t, explained=CUT_EXPLAINED):
    t = add_scene_res(t)
    a = "//!BIND HOOKED\n//!BIND SCENE_DIFF\n//!BIND NEXT\n"
    _once(t, a, "the warp's binds")
    t = t.replace(a, "//!BIND HOOKED\n//!BIND SCENE_DIFF\n//!BIND SCENE_RES\n//!BIND NEXT\n")
    a = "    if (SCENE_DIFF_tex(vec2(0.5)).r > SCENE_CUT_DIFF)\n"
    _once(t, a, "the cut gate's condition")
    t = t.replace(a, "    vec2 cut_res = SCENE_RES_tex(vec2(0.5)).rg;     // a cut: different AND not explained by the motion (CUT_MOTION)\n"
                     f"    if (SCENE_DIFF_tex(vec2(0.5)).r > SCENE_CUT_DIFF && cut_res.r > {explained:.3f} * cut_res.g)\n")
    return t
