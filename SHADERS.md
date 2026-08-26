# Example shaders

Six `.hook`-format GLSL shaders built on
[frame-mix-hook.patch](frame-mix-hook.patch)'s `PL_HOOK_FRAME_MIX` stage
-- see [README.md](README.md) for what that patch adds and why. Five are
the interpolation shader family (one does real motion-compensated frame
interpolation, three are diagnostic builds of that same algorithm, one
is an unrelated smoke test for the patch's N-frame generalization);
`motion-edges-dual.glsl` is the first entry toward what ROADMAP.md calls
for as ongoing work: a *range* of simpler examples alongside the one
complex flagship, not just the flagship itself. Expect more entries here
over time, weighted toward the simple end.

## Files

- `bidirectional-interpolation.glsl` -- the production interpolator
  (outlined below).
- `interpolate-debug-grid.glsl` -- diagnostic build (below): the same
  algorithm as a shrunk-down 3x2 grid of intermediate results.
- `interpolate-debug-overlay.glsl` -- a second diagnostic build (below):
  the actual full-resolution output, with the flow field and edge masks
  tinted on top of it in place, for inspecting a specific, localized
  defect that a shrunk-down grid cell can't show clearly enough.
- `interpolate-debug-warp-stages.glsl` -- a third diagnostic build
  (below): outputs exactly one stage of the final warp/blend pipeline at
  a time (single-direction warp, cross-blended, or fully composited),
  selected by editing one constant, for isolating which specific stage
  introduces a subtle warp defect. Both this and the overlay diagnostic
  above were originally built during a 2026-08-26 real-hardware
  investigation into a specific such defect -- see ROADMAP.md for what
  was found and why that particular investigation is currently parked --
  but the techniques themselves are general-purpose and kept in lockstep
  with whichever pyramid the production shader currently runs, not tied
  to that investigation.
- `nframe-smoketest.glsl` -- unrelated smoke test for the
  N-frame generalization described in README.md, not a companion to the
  flow debug shader above. Binds 4 frames at once (`FRAME0`..`FRAME3`)
  and renders them as a 2x2 grid with per-cell diagnostics (a distinct
  color tag per index, each frame's `rts_mix[]` value as a small bar, a
  `num_mix` readout, and the same red/green `pair_changed` indicator the
  flow debug shader uses) -- see its own header comment for the full
  layout. Not a production shader and not meant to demonstrate a useful
  N-frame algorithm, just to make the plumbing directly checkable by eye
  the same way the flow debug shader did for caching.
- `motion-edges-dual.glsl` -- the first non-interpolation example
  (outlined below): a plain 2-frame difference-and-threshold motion edge
  outline, no motion estimation at all, with HOOKED's and NEXT's
  contribution to the outline shown separately in contrasting colors.

Each file is self-contained and uses the mpv/libplacebo custom shader
hook DSL (`//!HOOK`, `//!BIND`, `//!SAVE`, `//!WIDTH`/`//!HEIGHT`),
targeting the `FRAME_MIX` stage. Read the header comment in each file for
the specific tuning knobs.

## Interpolation shader: working outline

`bidirectional-interpolation.glsl` synthesizes each output frame from the
two source frames the `PL_HOOK_FRAME_MIX` hook hands it (`HOOKED` =
earlier, `NEXT` = later), in five stages. It's written against exactly 2
frames and needed *no changes* for the N-frame generalization -- `HOOKED`
and `NEXT` still mean exactly frame index 0 and 1, same as always; this
shader is simply the N=2 case of the now-more-general mechanism:

1. **Downsample.** Both frames' luma is downsampled to four pyramid
   levels (1/16, 1/8, 1/4, 1/2 resolution) for coarse-to-fine motion
   search.
2. **Bidirectional block-matching search**, at each pyramid level, in
   both directions independently (A->B and B->A, not one derived from
   the other by sign-flipping) -- a per-block SAD search refined level by
   level, with a magnitude-regularization term biasing ambiguous/flat
   regions toward small motion rather than spurious large jumps. Only the
   coarsest level does this full iterative search from scratch (5
   halving steps, currently capped at ~23px full-res reach -- confirmed
   on real footage this avoids locking onto a spuriously-matching distant
   candidate in repetitive texture like blurred bokeh); every finer level
   nudges that result within a local +-2-texel neighborhood, biased
   (distance-scaled, the same shape as the coarse level's own
   regularization) toward staying at the seed unless a neighbor scores
   clearly lower, rather than chasing a marginal, possibly
   window-contamination-driven improvement. Reading each level's seed
   from the one below it snaps to that coarser texture's exact texel
   center rather than bilinear-sampling it -- an ordinary bilinear read
   there would smooth a real per-texel value across many finer texels
   when handing it down, independent of how correct that value is
   (found and fixed on real hardware: it was smoothing away, not fixing,
   an underlying defect). The coarsest level also gates on local contrast
   before searching at all, to reject dark/noisy regions with no real
   signal to match against -- the finer levels do not gate on contrast
   (removing that gate at the finer levels, tested on real hardware, had
   no effect: they were already finding nothing better to search for in
   genuinely low-texture areas -- see ROADMAP.md's account of the
   2026-08-26 investigation for what that turned out to mean).
3. **Vector median filtering**, run twice per direction, to smooth out
   individually-plausible-but-locally-inconsistent motion vectors (the
   classic aperture-problem failure mode along straight edges).
4. **Occlusion detection**, via a forward/backward consistency check: if
   warping A->B and B->A round-trips back close to the starting point,
   the flow is trusted; if not, that region falls back to the nearer
   *unwarped* source frame instead of a warped sample that's more likely
   wrong.
5. **Warp and blend.** Each source frame is sampled at its
   motion-compensated position and blended by `mix_t`. The sample itself
   is a blend of texel-snapped (nearest-neighbor-equivalent, to avoid the
   extra blur linear filtering would add at a fractional offset) and
   plain linear filtering. Pure snapping alone is a *discontinuous*
   function of the warp position -- even a clean, low-noise flow field
   has enough sub-texel imprecision that adjacent output pixels can land
   on opposite sides of a texel boundary purely by chance, which is
   invisible on ordinary content but fragments thin, high-contrast
   linework into a dashed-looking line (confirmed on real footage: a
   cartoon's black outlines breaking up against the background, despite a
   clean flow field in the debug visualization -- a sampling artifact
   downstream of the flow, not a flow quality problem).

   Rather than blend a fixed amount of linear filtering back in
   everywhere (softening the whole frame to fix a problem that only
   shows up in specific spots), the blend strength is decided per pixel
   by an independent edge-consistency check. Two extra full-resolution
   passes (`EDGE_A`/`EDGE_B`) compute a motion-gated spatial edge mask
   for each source frame -- reusing the exact technique
   `motion-edges-dual.glsl` already validates on real hardware: a pixel
   only counts as an edge if it's both a genuine spatial edge within its
   own frame and part of a temporally-moving region, so the vast
   majority of any frame (its static edges) never registers at all. At
   warp time, that mask is read twice: once at the true (unsnapped) warp
   position -- smooth/bilinear, so a continuous "is a moving edge
   expected here" signal -- and once at the snapped position, which
   degenerates to the exact value of whichever single texel the snap
   landed on. Where the two agree (both confidently edge, or both
   confidently not) the snap is corroborated and gets trusted fully;
   where they disagree, that's precisely the coin-flip case that
   fragments a line, so that specific sample falls back toward linear
   filtering instead. `SNAP_STRENGTH` is an overall damping multiplier on
   top of that per-pixel signal rather than the sole knob it used to be.

   **Currently set to 0.0** (fully disabled -- pure bilinear at the
   warped position, `EDGE_A`/`EDGE_B` still computed but unused by the
   warp itself). Real-hardware isolation during the 2026-08-26
   investigation (see ROADMAP.md) traced the actual reported defect
   ("parts of the warp left behind" on real footage, most visible on
   faces/skin in natural motion) to the flow field's own resolvable
   precision in low-texture regions, not to this mechanism -- setting
   this to 0.0 as a control confirmed the defect persisted identically
   either way, and the investigation's eventual fix for that (an
   edge-aware flow diffusion mechanism) was itself set aside as scope
   creep beyond this project's current priorities, not carried forward
   here. This mechanism's own original target (thin-outline
   fragmentation on cartoon content) is a real, separate problem it was
   never disproven for; re-enabling and re-verifying it is open,
   unstarted follow-up work, not a decision made yet.

**Where the patch's functionality actually earns its keep** (using just
2 of the up-to-8 frames it can supply): every one of the five stages
above needs *both* source frames and the true timing relationship
between them -- none of it is expressible against the single composited
texture a stock libplacebo custom shader would normally see.
Blending by the real `mix_t` (rather than a fixed step) is also what
makes this correct for non-integer fps ratios like 24->60 out of the box.

And because a 2.5x ratio means several consecutive output frames share
the same source pair (only `mix_t` moves between them), stages 1-3 are
wrapped in `//!TEXTURE ... //!STORAGE` caches gated on `pair_changed`: on
a cache hit, the shader `imageLoad`s a stored motion field instead of
re-running the search, cutting genuinely repeated GPU work rather than
just repeated output. See [README.md](README.md) for the fixed
cache-texture-size ceiling this implies. Measured effect below.

## Debug shader: embedding diagnostics in the output itself

`interpolate-debug-grid.glsl` is the same algorithm, kept in lockstep
pass-for-pass with the production shader, with one difference: instead
of returning the final warped/blended picture, its last pass renders a
3x2 diagnostic grid.

```
+------------+------------+------------+
|  source A  |  source B  | flow color |
|  (HOOKED)  |  (NEXT)    | wheel [C][F]
+------------+------------+------------+
| flow magni-| occlusion  |  actual    |
| tude heat- | (FB-error) |  warped    |
| map (AB)   |  mask      |  result    |
+------------+------------+------------+
```

- **Flow color wheel** -- hue = direction, brightness = magnitude of the
  A->B motion vector at each point (the same visualization convention
  the Middlebury/KITTI optical-flow benchmarks use). A rigid object
  should read as one consistent color; a patchwork of colors across what
  should be one object is a direct visual signal of a bad match.
- **[C] cache indicator** (top-left corner) -- red when this output frame
  recomputed the flow field, green when it was served from the
  `pair_changed` storage cache. Confirms the caching described above is
  actually engaging, frame by frame, without separate instrumentation.
- **[F] fallback indicator** (top-right corner) -- black-to-yellow-to-red
  based on how much of this frame is falling back to an unwarped source
  frame (via the occlusion check) rather than being genuinely
  motion-compensated -- a frame-level summary of the same decision the
  occlusion mask below shows per-pixel.
- **Magnitude heatmap** -- motion magnitude, clamped, with anything over
  the clamp shown in magenta as a likely-runaway-vector signal rather
  than just an under-tuned search.
- **Occlusion mask** -- white where the forward/backward consistency
  check distrusts the flow (and the final result falls back
  accordingly); a direct predictor of where warping artifacts are most
  likely to appear.
- **Actual warped result** -- exactly what the production shader would
  output for this frame.

**Why this matters:** normally, debugging a GPU motion-compensation
shader means either reasoning blind from the final picture (is that
blur a flow error, an occlusion fallback, or something else entirely?)
or bolting on separate tooling to extract intermediate GPU state. Since
this is just a shader, neither is necessary -- the diagnostic data is
written directly into the same render pipeline and viewed as an ordinary
video frame, or a single exported still. One screenshot shows the source
frames, the computed flow, where it's trusted vs. not, and the actual
result, all at once, on real hardware, without touching a debugger --
which is how essentially every bug in the production shader (sign
errors, bad coarse matches, aperture-problem edge artifacts, occlusion
ghosting) actually got found during development.

## Two further diagnostics: full-resolution overlay and warp-stage isolation

The 3x2 grid above has a real limit: shrinking the whole frame into a
cell to fit six of them side by side loses exactly the fine spatial
detail a subtle, localized defect needs to be judged properly. Two
further diagnostic builds address that, kept in the same lockstep as
the grid above -- both were originally built during a 2026-08-26
real-hardware investigation into a specific warp defect (see ROADMAP.md
for what was found and why that particular investigation is currently
parked), but the techniques are general-purpose and independent of it.

`interpolate-debug-overlay.glsl` outputs the real warped/blended result
at full resolution -- bit-identical to bidirectional-interpolation.glsl's
own final pass -- with the flow-color wheel and both `EDGE_A`/`EDGE_B`
edge masks (red/cyan, `motion-edges-dual.glsl`'s convention) composited
additively on top in place. Additive, not alpha blend, because every
diagnostic signal is exactly zero where it isn't firing -- black flow
color, zero edge mask -- so a pixel with no measured motion and no
detected edge passes through completely unaffected, still the real
algorithm's actual output. Both overlays sample RAW/unwarped (at each
output pixel's own position, not motion-compensated to the interpolated
timestamp), independent of whether the flow field or warp mechanism
under inspection is itself correct -- an independent reference to
compare the visible result against.

`interpolate-debug-warp-stages.glsl` isolates exactly ONE stage of the
final warp/blend pipeline at a time, full resolution, with no tinting
at all -- selected by editing `DEBUG_STAGE`: `0`/`1` output
`warp_sample_a`/`warp_sample_b` alone (no cross-blend, no occlusion
fallback), `2` is the two cross-blended by `mix_t` with no occlusion
fallback yet, `3` is the actual production output. Comparing adjacent
stages pairwise localizes a defect by exclusion: present already in `0`
or `1` individually points at the per-direction warp sampling itself;
absent there but present in `2` points at the two directions not
agreeing on position; absent through `2` but present in `3` points at
the occlusion/fallback blend triggering too broadly. No diagnostic
tinting on any of the four views, on purpose -- comparing images against
each other stage-by-stage is a fundamentally easier comparison than
describing one complex, fully-composited image in words.

## motion-edges-dual.glsl: a simple, non-interpolation example

Where `bidirectional-interpolation.glsl` sits at the complex end of what
`PL_HOOK_FRAME_MIX` enables, `motion-edges-dual.glsl` sits at the simple
end, deliberately: a plain per-pixel frame difference and a threshold,
no motion estimation, no warping, no pyramid, no caching. It outputs
`HOOKED` (the current frame) with a colored trace drawn wherever
something changed noticeably between `HOOKED` and `NEXT`. (Two other
variants -- a single merged white outline, and a version showing only the
edge that matches the displayed frame -- were tried and dropped after
real-hardware comparison found this one clearly the most visually useful
of the three; the name is a holdover from when it had siblings to be
"dual" relative to, not a claim about the technique itself.)

The algorithm has two parts, both operating directly on full-resolution
luma with no downsampling:

1. **Threshold a temporal frame difference**, to decide which pixels are
   part of a moving region at all. `abs(luma(HOOKED) - luma(NEXT))` past
   `MOTION_THRESHOLD` (0.08 by default) counts as "moving"; below it,
   "static" -- ordinary sensor noise and static content routinely differ
   by a few percent between two real frames even with zero actual
   motion, so this threshold is what makes "static objects / small
   motions / noise are irrelevant" true rather than aspirational.
2. **Detect genuine spatial edges within HOOKED and within NEXT
   independently** (`SPATIAL_EDGE_THRESHOLD` -- does a pixel's luma
   differ from an immediate neighbor's, in the same frame; the
   single-image analogue of the temporal threshold above), then keep
   only the spatial edges that also fall inside the temporally-moving
   region from step 1 -- filtering out the far more numerous static edges
   elsewhere in the scene. A moving object's silhouette is a real
   spatial edge in whichever frame you look at it in, so this cleanly
   separates "HOOKED's edge" from "NEXT's edge" rather than merging them
   into one undifferentiated trace.

HOOKED's edge draws **red** (where it was), NEXT's edge draws **cyan**
(where it's going) -- directly showing both where an edge currently is
and roughly where it's heading, which is what made this variant more
useful in practice than either single-color alternative. Where both
fire at the same pixel (little relative motion at that specific point
along the boundary), red and cyan add to white.

Built for **N:N frame rate** (e.g. 24fps -> 24fps, no frame insertion --
see ROADMAP.md's testing notes on this case): it never reads `mix_t` at
all, since it isn't synthesizing an in-between frame -- every output
frame is just "the current frame, with motion edges drawn on it," the
natural shape for a `PL_HOOK_FRAME_MIX` use case where the hook fires
and synthesizes every output frame but no actual rate conversion is
happening.

**Confirmed on real hardware** -- the most visually convincing of the
three variants that were compared, which is why it's the one that
remains. Not yet specifically tested against dark or noisy content -- if
such a region flickers a trace where nothing is really moving, that's
the same underlying failure mode `bidirectional-interpolation.glsl`'s
`MIN_CONTRAST` gate was built for -- frame-to-frame noise in low-signal
regions can itself exceed a magnitude threshold by chance. Try raising
`MOTION_THRESHOLD` or `SPATIAL_EDGE_THRESHOLD` first; if that stops
helping without also suppressing real motion/edges, a local-contrast
pre-check like that gate is the next thing to add.

## N-frame smoke test

`nframe-smoketest.glsl` applies the same "embed the diagnostic
data directly in the output" idea to a different question: not whether
the interpolation algorithm is correct, but whether the underlying patch
mechanism generalizes past 2 frames at all. It binds 4 frames at once
(`FRAME0`..`FRAME3`) and renders a 2x2 grid, one cell per frame:

```
+------------+------------+
|  FRAME0    |   FRAME1   |
|  [P][N] ...|.........[1]|
+------------+------------+
|  FRAME2    |   FRAME3   |
|.........[2]|.........[3]|
+------------+------------+
```

- **[P] pair_changed indicator** (top-left corner, cell 0) -- same
  red/green convention as the flow debug shader's cache indicator, now
  tracking a 4-frame window instead of a pair.
- **[N] num_mix readout** (top-right corner, cell 0) -- a row of lit
  ticks, one per valid frame. This shader always declares exactly 4
  binds, so a correct build always shows exactly 4 lit ticks; anything
  else means the `frame_mix_count` plumbing is broken.
- **Per-cell corner tag** (`[0]`-`[3]`, bottom-right of each cell) -- a
  fixed color per index, so it's obvious at a glance which cell is which.
  Two cells ever looking identical is the actual failure mode this
  shader exists to catch: two different indices silently resolving to
  the same texture instead of genuinely distinct ones.
- **Per-cell timestamp bar** (thin strip along each cell's bottom edge)
  -- visualizes that frame's `rts_mix[i]` directly: a center tick at the
  output timestamp, the bar extending left (blue, before) or right
  (orange, after), length proportional to magnitude. The two frames
  nearest the center tick should have the shortest bars; a scrambled
  ordering means frame selection picked a non-sensible window.

Unlike the flow debug shader, this one isn't validating an algorithm --
there's no "correct" picture to compare against, just internal
consistency (distinct textures, sane timestamps, a correct count) that's
otherwise invisible from C code alone. It exists because the alternative
-- trusting the N-frame plumbing without ever actually binding more than
2 frames from a real GPU dispatch -- isn't good enough for a change this
structural; see README.md's "Verifying the N-frame case" section for the
rest of that reasoning.

**Confirmed on real hardware:** 4 visually distinct frames, sane
timestamp bars, a correct 4-tick `num_mix` readout, ~212fps, and no
unexpected fallbacks across a full 60-second clip once past the startup
window -- i.e. the 4-frame window found exactly 4 frames on every
steady-state dispatch, reliably, for the whole clip. The startup window
itself behaved as expected too: a black first output frame (nothing
decoded yet), then the single-decoded-frame zero-order-hold from
libplacebo's own builtin behavior for a few frames, before the grid
takes over once 4 real frames exist. See README.md's "Costs and
limitations" for why that startup hold is worth watching (a small
possible A/V offset), and "Testing status" for what this test does and
doesn't cover (one fps ratio, no source above 1080p).

## Performance

**End-to-end, real encode pipeline** (`hevc_vaapi -global_quality 20`,
full command as in README.md's Usage section): confirmed on real
hardware, a low-end discrete GPU renders 1080p through
`bidirectional-interpolation.glsl` at ~138fps, comfortably inside
real-time-streaming tolerance.

**Isolated render cost, caching impact specifically** (output discarded
via `-f null -` to remove encoding from the measurement, 1080p source):

| | Low-end discrete GPU | Weaker iGPU |
|---|---|---|
| No caching (baseline) | 144 fps | 33 fps |
| + flow-search caching | 174 fps | 44 fps |
| + median-filter caching | 184 fps | 48 fps |

(Measured against a since-removed uncached variant of the shader --
the numbers themselves remain valid as a baseline for what caching
buys; the variant was dropped as an unneeded second file to maintain,
not because the comparison stopped mattering.)

Smaller than a naive per-pass-cost estimate would predict, most likely
because of fixed per-dispatch overhead (the shader issues ~23 dispatches
every output frame regardless of cache state) and possible
`PL_MEMORY_COHERENT` synchronization cost on every storage access --
neither of which caching can remove.

All the numbers above predate the `EDGE_A`/`EDGE_B` edge-consistency
passes (see "Warp and blend" above) -- two extra full-resolution,
uncached dispatches added since this table was last measured (21 -> 23
above is the one part of this already re-counted; the fps figures
themselves are not yet re-measured). Expect some reduction until they're
checked again on real hardware; per the project's working assumption
there's headroom to spare on the target hardware, but that's an
assumption, not a re-measurement.

4K is untested; if it struggles, the coarse search levels (run at 1/16
and 1/8 resolution, the most expensive part) are the first place to
look -- e.g. dropping a pyramid level or reducing the SAD window at the
coarsest level.
