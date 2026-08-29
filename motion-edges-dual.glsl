// motion-edges-dual.glsl
//
// A deliberately SIMPLE example shader for PL_HOOK_FRAME_MIX -- see
// README.md for what that patch stage is. Unlike
// bidirectional-interpolation.glsl (a full hierarchical motion-estimation
// pipeline), this does no motion estimation, no warping, no pyramid, no
// caching -- just a per-pixel frame difference, a threshold, and a
// per-frame spatial edge check. It exists to demonstrate that the
// multi-frame access this patch adds is useful for things much smaller
// than a full interpolator.
//
// What it does: outputs the current (HOOKED) frame with a colored trace
// drawn wherever something changed noticeably between HOOKED and NEXT.
// Small motion, static content, and ordinary sensor noise are
// deliberately ignored (see MOTION_THRESHOLD below) -- only regions with
// a real, sustained brightness change register at all, and only their
// *edge* is drawn, not the whole region. Two colors, not one: HOOKED's
// contribution to the edge draws red (where it was), NEXT's draws cyan
// (where it's going) -- an earlier version merged both into a single
// white trace, which was still useful (it showed both at once) but
// didn't distinguish which was which; comparing on real hardware, the
// two-color version was clearly more visually useful, so that's the one
// that remains. (The "-dual" in the filename is a holdover from that
// comparison, not a claim about the technique needing two frames more
// than any other shader here does.)
//
// Algorithm: for each pixel, gate on a temporal moving/static test
// (MOTION_THRESHOLD -- does HOOKED's luma differ from NEXT's here at
// all), then separately check whether the pixel is a genuine spatial
// edge *within* HOOKED alone, and *within* NEXT alone
// (SPATIAL_EDGE_THRESHOLD -- a plain "does this pixel's luma differ from
// an immediate neighbor's, in the same frame" test, the single-image
// analogue of the temporal test). A moving object's silhouette is a real
// spatial edge in whichever frame you look at it in -- gating each
// frame's own spatial edges by "and this location is also part of the
// moving region" keeps only the edges that belong to something actually
// moving, discarding the (usually far more numerous) static edges
// elsewhere in the scene.
//
// Where only HOOKED has a spatial edge at a pixel (the object was there,
// isn't anymore): red. Where only NEXT does (the object wasn't there,
// now is): cyan. Where both do (little relative motion at that specific
// point along the boundary): red+cyan add to white.
//
// REQUIRES a libplacebo build patched with frame-mix-hook.patch (see
// README.md) -- stock libplacebo has no PL_HOOK_FRAME_MIX stage. Unlike
// the N-frame interpolation shaders, this one only ever needs 2 frames,
// so no FRAME2+/rts_mix/num_mix machinery is used here at all.
//
// Designed for N:N frame rate (e.g. 24fps -> 24fps, no frame insertion --
// see ROADMAP.md's "N:N scaling" note under current-focus testing). This
// shader has no interpolation semantics whatsoever and never reads
// `mix_t` -- every output frame is just "the current frame, with motion
// edges drawn on it," which is exactly the shape of filter an N:N,
// no-rate-conversion use of PL_HOOK_FRAME_MIX needs: the hook still
// fires and synthesizes every output frame, but there's no "in-between"
// frame being created at all.

//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND NEXT
//!SAVE FRAME_MIX
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!DESC motion edge outline, A/B shown separately (2-frame, no motion estimation)

// Below this per-pixel HOOKED/NEXT luma difference, a pixel is not
// considered part of any moving region at all, regardless of what either
// frame's own spatial-edge test below says about it. Ordinary sensor
// noise and static content routinely differ by a few percent between two
// real frames even with zero actual motion, so this threshold is what
// makes "static objects / small motions / noise are irrelevant" true
// rather than aspirational. If real but low-contrast motion isn't being
// picked up, lower this; if static or noisy regions are still
// flickering a trace, raise it.
const float MOTION_THRESHOLD = 0.08;

// How much a pixel's luma has to differ from an immediate neighbor's,
// within a single frame, to count as a real spatial edge in that frame.
// Genuine object-silhouette boundaries are usually high-contrast (well
// above this); flat regions vary far less between adjacent texels than
// they do at a real edge. If real object edges are being missed, lower
// this; if it's picking up fine background texture as if it were an
// edge, raise it. Independent from MOTION_THRESHOLD on purpose -- one
// measures change over time, the other change over space, and there's
// no reason to expect the same numeric value is right for both.
const float SPATIAL_EDGE_THRESHOLD = 0.1;

float luma(vec4 c) {
    return dot(c.rgb, vec3(0.299, 0.587, 0.114));
}

bool moving(vec2 pos) {
    return abs(luma(HOOKED_tex(pos)) - luma(NEXT_tex(pos))) > MOTION_THRESHOLD;
}

// Spatial edge within HOOKED alone -- does this pixel's luma differ from
// any of its 8 immediate HOOKED neighbors? NEXT is never sampled here.
bool spatial_edge_a(vec2 pos) {
    float center = luma(HOOKED_tex(pos));
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 o = vec2(float(x), float(y)) * HOOKED_pt;
            if (abs(luma(HOOKED_tex(pos + o)) - center) > SPATIAL_EDGE_THRESHOLD)
                return true;
        }
    }
    return false;
}

// Same as spatial_edge_a(), but entirely within NEXT instead.
bool spatial_edge_b(vec2 pos) {
    float center = luma(NEXT_tex(pos));
    for (int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            if (x == 0 && y == 0)
                continue;
            vec2 o = vec2(float(x), float(y)) * HOOKED_pt;
            if (abs(luma(NEXT_tex(pos + o)) - center) > SPATIAL_EDGE_THRESHOLD)
                return true;
        }
    }
    return false;
}

vec4 hook() {
    vec2 pos = HOOKED_pos;

    if (!moving(pos))
        return HOOKED_tex(pos);

    bool a = spatial_edge_a(pos);
    bool b = spatial_edge_b(pos);
    if (!a && !b)
        return HOOKED_tex(pos);

    vec3 color = vec3(0.0);
    if (a) color += vec3(1.0, 0.0, 0.0); // red: HOOKED's edge -- where it was
    if (b) color += vec3(0.0, 1.0, 1.0); // cyan: NEXT's edge -- where it's going
    return vec4(clamp(color, 0.0, 1.0), 1.0);
}
