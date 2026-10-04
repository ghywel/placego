#!/usr/bin/env python3
"""l4_variant.py <out.glsl> [base.glsl]: REPAIRS.md lead L4's experiment (2026-10-04), as a variant, never in place.

Where the 1/8 level takes the coarse result as its seed, round it to whole half-resolution texels (multiples of 1/8
coarse texel = 2 full-resolution px), so the whole-texel refinement can land on an even speed exactly. The base's coarse
search lands on m = 21 or 22 (15.75 or 16.5 px) for a 16 px/frame motion (l4_coarse_fraction.py), and its finest flow
stays 15.75 px on 94% of M2's moving texels. PREDICTION (REPAIRS.md, written before the run): no change where the
coarse search already lands on m = 0 (mod 8); a gain on the textured even-speed translations (L7, M1-M3); a loss on
speeds that are not a whole even number of px; the ladder mean within +-0.10 dB. REFUTED by: no gain on L7 and M1-M3,
or a fall of the mean by more than 0.10 dB.
"""
import pathlib, sys
src = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else
                   pathlib.Path(__file__).resolve().parents[3] / "shaders" / "bidirectional-interpolation.glsl")
t = src.read_text(encoding="utf-8")
old = "FLOW_S_AB_tex(snap_texel(uv_a, FLOW_S_AB_size)).xy * 2.0 * LUMA_A_E_pt"
assert t.count(old) == 1, t.count(old)
t = t.replace(old, "(round(FLOW_S_AB_tex(snap_texel(uv_a, FLOW_S_AB_size)).xy * 8.0) / 8.0) * 2.0 * LUMA_A_E_pt")
pathlib.Path(sys.argv[1]).write_text(t, encoding="utf-8", newline="\n")
print(f"wrote {sys.argv[1]}: the seed rounded to 1/8 coarse texel at the 1/8 level")
