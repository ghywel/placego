# Prior art for the animation shaders: whose footsteps these are

The shaders in this folder are built on other people's results, and this file
says whose, in the same spirit as `../../PRIOR-ART.md`: what was taken, what
was independently re-derived, and what is ours. Surveyed 2026-09-05, when the
owner's idea from the project's first week (`ROADMAP.md`, "A shader class
specific to animation") was picked up again.

## The idea's origin, and what the record already knew

The owner's note of 2026-08 made two observations: `motion-edges-dual.glsl`
draws a strikingly accurate outline of a character's before and after
positions, so a character could be moved as a template rather than as a field
of independent texels; and animated backgrounds are mostly static, so a
background plate kept in persistent storage could fill what a character
uncovers instead of inventing it. Both turn out to be old footsteps, walked by
people who went further, and the survey below is what made the idea workable.

## Taken directly

**The distance transform under the flow estimator.** Rei Narita, Keigo
Hirakawa and Kiyoharu Aizawa, *Optical Flow Based Line Drawing Frame
Interpolation Using Distance Transform to Support Inbetweenings*, ICIP 2019.
Optical flow fails on line drawings because flat regions carry no gradient;
replacing each pixel by its distance to the nearest line pixel gives the
drawing a texture the estimator can match. That is exactly the failure we
watched on a flat-shaded character, and their remedy is the one used here:
the pyramid the block matcher works on is fed the distance field of the line
art beside the luma.

**The distance transform in the synthesis, and the right metrics.** Shuhong
Chen and Matthias Zwicker, *Improving the Perceptual Quality of 2D Animation
Interpolation*, ECCV 2022 ("EISAI"). A forward-warping architecture with a
distance-transform module that uses line proximity to correct solid-colour
regions; and, the part this project needed most, the demonstration that PSNR
and SSIM are the wrong measures for animation interpolation, replaced by the
LPIPS perceptual metric and the chamfer line distance. The band-PSNR floor we
hit on a walk cycle -- the true in-between is a third drawing that exists in
neither source -- is their finding, arrived at from the other side.
`tests/chamfer.py` implements the chamfer line distance on their reasoning.

**The benchmark.** Li Siyao, Shiyu Zhao, Weijiang Yu, Wenxiu Sun, Dimitris
Metaxas, Chen Change Loy and Ziwei Liu, *Deep Animation Video Interpolation in
the Wild*, CVPR 2021 ("AnimeInterp"), and its dataset ATD-12K: 12,000 frame
triplets from 30 animated films, the middle frame as ground truth, the test
set in three difficulty tiers by motion and occlusion. It is the external
ground truth for the picture on cel content, and the numbers of every method
above are on it.

**The distance transform itself.** Guodong Rong and Tiow-Seng Tan, *Jump
Flooding in GPU with Applications to Voronoi Diagram and Distance Transform*,
I3D 2006. The jump-flooding algorithm computes a distance transform in
log2(N) parallel passes, each texel asking its neighbours at a halving stride
who their nearest seed is. It is the only way a distance transform fits a
pipeline of fragment passes, and the `[lineart]` passes here are it verbatim.

**Morphing curves as level sets of distance fields.** The principle that a
blend of two distance fields, taken at a level set, gives one in-between
curve rather than two superimposed ones is the distance-field metamorphosis of
Daniel Cohen-Or, Amira Solomovici and David Levin, *Three-dimensional
distance field metamorphosis*, ACM Transactions on Graphics 1998, applied
here in two dimensions and under a flow. It is the vector principle -- a line
has an identity as a curve, not as a row of pixels -- without vectorising
anything.

## Consulted, and why we did not go that way

**Stroke-based inbetweening.** Brian Whited, Gioacchino Noris, Maryann
Simmons, Robert Sumner, Markus Gross and Jarek Rossignac, *BetweenIT: An
Interactive Tool for Tight Inbetweening*, Eurographics 2010 (Disney
Research): vectorised keyframes segmented into strokes, matched, and
interpolated, with the artist in the loop. CACANi (Nanyang Technological
University; cacani.sg) is the commercial descendant of that line: automatic
feature points at stroke ends and corners, inbetweens generated and coloured,
from clean vector strokes the artist supplies. The research that starts from
raster keyframes -- *Joint Stroke Tracing and Correspondence for 2D
Animation* (ACM Transactions on Graphics 2024), *LayerInbetween:
Occlusion-Aware Stroke Correspondence and Inbetweening with Automatic
Layering* (ACM Transactions on Graphics 2025), *Stroke Correspondence by
Labeling Closed Areas* (2021) -- is neural and offline. The lesson taken:
stroke correspondence is the crux in every formulation, and no tool gets it
free from raster; the level-set route sidesteps explicit strokes.

**Ground-truth flow for animation.** *LinkTo-Anime: A 2D Animation Optical
Flow Dataset from 3D Model Rendering* (2025) renders animation-style frames
from 3D models with the true flow. It is the external benchmark for the field
shaders on cel content, listed on the front line with the PIV datasets.

## Ours, as far as the record shows

The delivery: all of it inside a real-time, deterministic user shader in a
production video pipeline, with the distance transform, the matcher and the
morph as passes of one hook. The background plate as a persistent storage
image that arbitrates between the warp's two candidates rather than inventing
anything. One motion per moving thing as a robust vote over the dense field,
gated by the plate. And the instrument work around it: the moving-band split
of the error, and the decimate-and-reconstruct bench on cel footage at a size
that keeps the motion inside reach.

## Sources

- Narita, Hirakawa, Aizawa, ICIP 2019: https://ieeexplore.ieee.org/document/8803506/
- Chen, Zwicker, ECCV 2022 (EISAI): https://arxiv.org/abs/2111.12792
- Siyao et al., CVPR 2021 (AnimeInterp, ATD-12K): https://openaccess.thecvf.com/content/CVPR2021/papers/Siyao_Deep_Animation_Video_Interpolation_in_the_Wild_CVPR_2021_paper.pdf and https://github.com/lisiyao21/AnimeInterp/
- Rong, Tan, I3D 2006 (jump flooding): https://www.comp.nus.edu.sg/~tants/jfa.html
- Cohen-Or, Solomovici, Levin, TOG 1998 (distance field metamorphosis): https://dl.acm.org/doi/10.1145/274363.274366
- Whited et al., Eurographics 2010 (BetweenIT): https://studios.disneyresearch.com/wp-content/uploads/2019/03/BetweenIT-An-Interactive-Tool-for-Tight-Inbetweening-Paper.pdf
- Joint Stroke Tracing and Correspondence for 2D Animation, TOG 2024: https://dl.acm.org/doi/10.1145/3649890
- LayerInbetween, TOG 2025: https://dl.acm.org/doi/10.1145/3811364
- Stroke Correspondence by Labeling Closed Areas, 2021: https://arxiv.org/pdf/2108.04393
- CACANi: https://cacani.sg/
- LinkTo-Anime, 2025: https://arxiv.org/html/2506.02733v2

## Surveyed 2026-09-05, at the owner's suggestion: the Anime4K line shaders

bloc97, *Anime4K* (github.com/bloc97/Anime4K), MIT licence, copyright 2019-2021 bloc97. A family of
mpv GLSL hook shaders for anime, spatial only (no frame mixing): CNN restore and upscale, deblur,
denoise, and two line effects in `glsl/Experimental-Effects` that bear on this folder's line-art shader:

- **Darken (difference of Gaussians).** Luma, then a Gaussian blur sized to the frame, then
  `min(luma - blur, 0)` isolates the dark lines and nothing else, smoothed again and added back with a
  strength. That is a line DETECTOR that answers only to ink: this folder's line pass thresholds the
  luma gradient and so fires on every boundary between two fills as well. The DoG is the candidate
  replacement for the line pass wherever the ink is darker than its surroundings, which on cel it is.
- **Thin (advection along the gradient).** Luma, Sobel gradient with a 0.7 power curve, Gaussian
  smoothing, the smoothed gradient's derivatives, and a warp that moves each texel along the gradient
  by `strength * iterations`, so lines contract toward their centres. A candidate post-pass for the
  morphed in-between line, which comes out of the level-set morph slightly wider than either drawing's.

Nothing of theirs is in the shaders yet. If either idea goes in, the pass carries this credit and the
licence notice, and this entry says which and where.

## Surveyed 2026-09-19, at the owner's question: SVP and the cadence

The owner: *"I know apps like SVP can do it. So it must be possible and we must be missing something - or our
shaders are alien to their closed-source methodology."* Four research angles were run the same day (SVP and
SVPflow; the learned route; the television MEMC lineage; the free-player ecosystem), each sourced, then audited
against this repository and adversarially checked. What follows is the documented part; the measurement it led
to is `NFRAME-LIMITS.md`, "Content drawn on twos" (2026-09-19). D = documented at the source, I = inferred.

**SVPflow is not alien (D).** SVP 3.1 and 4 are built on SVPflow: svpflow1, the motion search, is "a deeply
refactored and modified version of MVTools2", the same hierarchical block matcher with SAD, penalties and
overlapping blocks as this family; svpflow2, the renderer, is closed. https://www.svp-team.com/wiki/Manual:SVPflow
The pipeline is a "super" pyramid, a block search with penalties (lambda, pnew, pzero, pglobal, pnbour),
per-level refinement, and a frame renderer with cover/uncover masks, a bad-area mask from block SAD, and a
scene-change module. Nothing in its parameter set or manual identifies, tracks or transforms objects.

**What SVP does for anime is policy, not estimation (D).** The manual's own caveat: "Greater smoothness always
results in more noticeable artifacts ... There is no perfect set of options that gives maximum smoothness
without artifacts." https://www.svp-team.com/wiki/Manual:FRC The Animation preset is "optimized for hand-drawn
animations (cartoons), which are characterized by sharp contrasting borders of objects and a static
background" (same page). The developer-prescribed anime settings (MAG79, 2012): the "Sharp" shader, which
"makes interpolated frames from only one source frame ... to avoid blended frames and double contours"; a
32-pixel block with 8-pixel overlap, "sensitive enough to detect global pan and zoom and not detect little
motions"; the smallest search radius, "best choice to detect global motions only"; two-pixel precision, which
"disable[s] search at finest level". https://www.svp-team.com/forum/viewtopic.php?id=2173 So SVP's anime
recipe deliberately coarsens the estimator until only global motion survives and renders each output from
one source frame, and it retreats to original frames per frame when the vector field is judged bad
("Adaptive ... In the scenes which are difficult to analyze, the smoothness will decrease") and overlays
original pixels where block SAD is high ("Artifacts masking ... The stronger the masking is, the blurrier
image and the worse smoothness"). Its developers say the anime "wave" artefact on thin contrast lines cannot
be repaired, only hidden (https://www.svp-team.com/wiki/SVP3:Watching_anime). This repository's `-snap.glsl`
is the single-source warp; the retreat and the SAD overlay have no shipped equivalent here (the occlusion
fallback was removed for doubling contours; see the scene-cut gate's comment in the recommendation).

**SVP and content on twos (D).** The only handling is a toggle, "Duplicate frames removal -> Remove every other
frame", implemented as an unconditional `SelectEvery(2,0)` with the rate doubled
(https://www.svp-team.com/wiki/SVP:Technical_insights; https://www.svp-team.com/forum/viewtopic.php?id=7310).
The developer, 2022: "this is only for the simplest case now, when every other frame is a duplicate"
(https://www.svp-team.com/forum/viewtopic.php?id=6598); a 2020 request for TDecimate-style detection of
triple and partial duplicates went unanswered (https://www.svp-team.com/forum/viewtopic.php?id=5793). No
cadence detection exists in SVP; its RIFE path likewise interpolates between two adjacent frames and does
nothing across duplicates (https://www.svp-team.com/wiki/RIFE_AI_interpolation).

**The rest of the ecosystem dedupes first (D).** Flowframes: "Frame De-Duplication: This is meant for 2D
animation. Removing duplicates makes a smooth interpolation possible ... These have to be removed before
interpolation to avoid choppy outputs", with `mpdecimate` as one of its two detectors, and the documented
failure mode of a threshold set too high ("very choppy, especially in dark (or low-contrast) scenes")
(https://github.com/n00mkrad/flowframes). DAIN-App's modes 2-4 remove duplicates with `mpdecimate`, mode 3
"record timestamps then remove duplicate frames (won't alter animation speed)". The television lineage
(Philips Natural Motion, de Haan's 3-D recursive search) detects the source cadence from the alternation of
frame differences or the estimator's own vector statistics and interpolates across the true frame period
(Philips AN97058, https://tvsat.com.pl/PDF/S/saa4991_ph.pdf; the per-region cadence of US6937655B2 and
US8004607B2, where a panning background on ones and a character on twos take different phases).

**The learned route (D).** RIFE and its anime-tuned models are what SVP now recommends for anime; their
documented margin on ATD-12K over the classical engines is one to two decibels, they do nothing across
duplicates either, and their prior over drawings is the one thing no deterministic method has. Not testable
here; ATD-12K remains the number that would place this family against that line.

**The answer to the question, as far as it is measurable here (I from the D above).** SVP's methodology is
not alien: it is this family's lineage with a policy of hiding failure -- retreat, mask, single-source warp,
global-only search -- and, for content on twos, an unconditional decimation in front. The measurement of the
same day (`NFRAME-LIMITS.md`) put the cadence step at 16 to 25 dB on the exact ladder, larger than every
estimator mechanism in this record, and found that nothing solves the redraw: the limit stated at the top of
`ANIMATION.md` stands.
