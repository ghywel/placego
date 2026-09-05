# The animation shaders: a class for cel content

The owner's idea from the project's first week (`ROADMAP.md`, "A shader
class specific to animation"), built on 2026-09-05 on other people's
results, credited in `ANI-PRIOR-ART.md`. Everything here is a variant of
`bidirectional-interpolation-animation.glsl`, made from it by a builder
script, each builder taking the previous variant as its input:

| file | builder | what it adds |
|---|---|---|
| `-plate.glsl` | `build_plate.py` | a persistent storage image of what each texel showed when it was last still, confidence-counted, cleared on cuts; a warp candidate whose source texel is background is replaced by the plate at the output texel, and where the two candidates still disagree the plate arbitrates |
| `-coherent.glsl` | `build_coherent.py` | one motion per moving thing as a trimmed mean of the dense flow over the character texels the plate identifies (a first attempt; superseded by the template) |
| `-snap.glsl` | (hand edit of the coherent warp) | a coherent character texel shows the nearer drawing, no blend |
| `-lineart.glsl` | `build_lineart.py` | the line art of each frame at half res, a distance transform of it by jump flooding (eleven passes per frame), the matcher's pyramid fed luma and distance together, and a warp that morphs the two fields under the flow and paints ink at the level set, only where something moves and only where the ink is dark |
| `-template.glsl` | `build_template.py` | on the line-art shader: an exhaustive template match of a character-sized window at 1/8 res, one rigid shift per moving thing by construction, used by the warp for character texels |

**Use `-lineart.glsl`.** It is the version to carry. The instruments are
`tests/cel_scenes.py` (synthetic cel scenes with an exact in-between at
every instant), `tests/bandmetric.py` (the error split into the moving band
and the rest) and `tests/chamfer.py` (the chamfer line distance, the
animation literature's measure in place of PSNR).

## Measured on the synthetic scenes

Decimate-and-reconstruct at 640x360, 6 px/frame, two 72-frame segments,
the shipped animation shader against the variants. Whole-frame PSNR / SSIM,
PSNR inside the moving band, and the chamfer line distance in pixels:

| scene | shipped | plate | line-art | template |
|---|---|---|---|---|
| rigid character, detailed backdrop | 31.23 / 0.9806, band 14.96, chamfer 0.82 | 31.22 / 0.9810, 14.95, 0.91 | **34.53 / 0.9894, 18.35, 0.38** | 33.59 / 0.9888, 17.42, 0.37 |
| swinging legs, detailed backdrop | 32.32 / 0.9826, band 16.08, chamfer 0.74 | 32.30 / 0.9833, 16.05, 0.80 | **33.77 / 0.9884, 17.52, 0.42** | 33.30 / 0.9877, 17.11, 0.41 |
| swinging legs, flat sky | 33.14 / 0.9863, band 16.98, chamfer 0.78 | 33.19 / 0.9877, 17.03, 0.86 | **34.95 / 0.9931, 18.77, 0.27** | 34.05 / 0.9915, 17.90, 0.31 |

The line-art shader gains 1.5 to 3.3 dB whole-frame and halves the chamfer
distance or better on every scene; the moving band gains 1.4 to 3.4 dB; on
the detailed backdrop the region outside the band also improves (48.3 to
50.4 dB on the rigid scene), which is the plate's background rule removing
the halo of smeared backdrop a character's flow drags in. The plate alone is
neutral: its effect is inside the line-art chain. The template match is
consistently a little below the line-art shader here, where the character
is large enough for the matcher.

## Measured on cel footage, and why that is the eye's job

On a 360p excerpt of a cel-animated show (720p puts its walk at the
tracker's reach after decimation), four 72-frame segments: shipped 27.80 dB
/ 0.9550, line-art 27.30 / 0.9541, template 27.01 / 0.9504; chamfer within
a few hundredths of a pixel either way. The true in-between of a walk cycle
is a third drawing that exists in neither source frame, so a crossfade and a
morph both miss it and the metrics reward the hedge (Chen and Zwicker,
ECCV 2022, say the same). In the frames the small walking characters are
single, readable poses on the line-art and template shaders where the
shipped shader shows two blended. The four-way half-speed videos are in the
owner's renders folder; the ATD-12K benchmark (12,000 triplets with the
middle frame as truth) is the external measure and needs a browser download
from the AnimeInterp repository's Google Drive link.

## What is left

- The small-character limit: a figure sixty pixels tall with limbs redrawn
  every frame gives the dense matcher nothing its size at the coarse levels
  and redraws at the fine ones; the template match is the answer in
  principle and needs a per-character window, which needs a segmentation
  (connected components of the moving region, one vote per component).
- The distance transform runs at half res in 2 x 11 passes; a 4K source
  would want it at quarter res, and the jump-flood stride list is sized for
  a 2K source.
- ATD-12K, with LPIPS beside the chamfer distance, once downloaded.
