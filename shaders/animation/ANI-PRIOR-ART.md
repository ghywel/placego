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
