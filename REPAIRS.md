# Repairs

One dated section per round of repairs: what was found, how it was fixed, and how the fix was checked. A finding
that needs a measurement before anything changes is listed under its round as an open lead. It comes with a
prediction written before the run, and what would refute it.

---

## 2026-10-04: wrong comments across the family, one stale generated file, one generator anchor

**How it was found.** Writing [shaders/bidirectional-interpolation.glsl](shaders/bidirectional-interpolation.glsl)
out as equations ([BIDIRECTIONAL-AS-MATHEMATICS.md](BIDIRECTIONAL-AS-MATHEMATICS.md)) turned up comments that the
code contradicts. Most of the family copies the base's text, so the same wrong comments sit in up to 39 of the 43
shader files.

**Where the work ran.** In a cloud session with no GPU. Only repairs that change no code were made. The full ladder,
`smoke.sh`'s render steps and render timing need the local machine, so everything that would change behaviour or
cost is listed under [Open leads](#open-leads-for-the-local-ladder) instead.

### What was found, and the repair

| # | Found | Where | Repair |
|---|---|---|---|
| 1 | The file header says "5x5 SAD windows" and describes "a forward/backward consistency check used for real occlusion detection ... the final blend favors the non-occluded source". The windows are 3x3 (`COARSE_WINDOW_RADIUS = 1`). The fallback was removed earlier, as the shader's own NO OCCLUSION FALLBACK note records. The header also compared the cost with a "medium tier" that no longer exists. | 27 files: the base, `-seeded`, `-propagated`, `-animation`, the six `shaders/animation/` files, and the variational line generated from them with its 4K twins (the N-frame shaders have their own header) | Header rewritten: 3x3 windows, and a dated note that the fallback described there was removed. The two diffusion forks still run the check, so their header is true and was left alone. |
| 2 | The banner above the final pass, "bidirectional warp with forward/backward consistency-based occlusion detection", is wrong for the same reason. | the same 27 files | Banner rewritten: "motion-compensated warp and blend", pointing to NO OCCLUSION FALLBACK. |
| 3 | The sub-pixel note says "Every search in this pipeline -- coarse and all three refine levels -- steps WHOLE texels", so "the finest flow the estimator can express is one half-res texel". The coarse search steps 0.75, 0.375, 0.1875, 0.09375 and 0.046875 of its own texels, so its result is generally fractional. The refine levels add whole texels to it, so that fraction passes down unchanged. In the base the flow therefore lies on a quarter-pixel grid, with its fraction decided at 1/16 resolution ([BIDIRECTIONAL-AS-MATHEMATICS.md](BIDIRECTIONAL-AS-MATHEMATICS.md), section 12.4). | 194 copies in 39 files | Note rewritten to say which searches step whole texels and which do not, with the date of the correction. |
| 4 | The next paragraph of the same note says sub-texel precision at the coarser levels "is discarded before it can be used". For the same reason it is not discarded; it is carried down uncorrected. | the same 194 places | Sentence rewritten, with the date of the correction. |
| 5 | `sextdirectional-interpolation-propagated.glsl` no longer matched its generator. Ten comment lines said "ZERO_SEED is OFF in this two-frame shader" while its code has `const int ZERO_SEED = 1`. Its base's comment had been corrected but the six-frame file was never regenerated. | 1 file | Regenerated with `tests/gen_sextdirectional.py`. Code unchanged. |
| 6 | `tests/gen_variational.py` finds where to insert the coherence gate by matching the text of the banner in repair 2. After that repair the anchor matched nothing, and the generator stopped with its own assertion (`anchor found 0 times`) instead of writing a wrong file. | 1 generator, 5 recipes (`-global-cage` and the four built on it) | Anchor updated to the new banner. The generator copies the anchor into its output, so its output carries the corrected banner; the code it emits is unchanged. |

The rules followed: never edit a generated or 4K file by hand, rebuild it ([generated-pass-traps](WORKFLOW-SAVED-MEMORY.md#generated-pass-traps));
assert every replacement took ([assert-every-patch](WORKFLOW-SAVED-MEMORY.md#assert-every-patch)).

### How it was done

1. **Hand-maintained files edited by exact text replacement**, with the count asserted per file. There are 14 such
   files: the base, `-seeded`, `-propagated`, `-animation`, the two diffusion forks, the two small examples and the
   six files in `shaders/animation/`. Ten of them carry the text, and each received repairs 1 to 4 (repairs 3 and 4
   twice). `human-reading-quad.glsl` was edited the same way (12 copies of repairs 3 and 4) before it was recognised
   as generated. Its body was then shown to be byte-identical to its two-step recipe, both before the repair and
   after it, so the result is the same as a rebuild.
2. **The other 28 generated files rebuilt by their own generators**: `gen_variational.py` with the recipes in
   `smoke.sh` (sections 3-3e) and [SHADERS.md](SHADERS.md); `gen_tridirectional.py` and `gen_quaddirectional.py` on
   each of their four bases (`CADENCE=1` for the cadence file); `gen_quintdirectional.py` and
   `gen_sextdirectional.py` on the propagated base; and `scale_shader.py ... 2` for every `-4k` twin, from its rebuilt
   unscaled file. The eight `-4k` headers now carry the regeneration date, as `scale_shader.py` writes it.
3. **SHADERS.md** gained a table, "How each file is made", saying which files are generated and from what. A fix to
   the base reaches the stock variational, tri and quad builds on regeneration. It does not reach the forks or what is
   generated from them.

### How it was checked

| Check | Before the repair | After |
|---|---|---|
| Generated files that their generator rebuilds byte-identical (the body after the header, as `smoke.sh` compares) | 28 of 29: the six-frame file was stale (repair 5) | 29 of 29, in an independent rebuild into a fresh directory |
| Shader files whose **code** is identical to commit `87f43f3` (comments and blank lines ignored; `//!` directives count as code) | 43 of 43 | 43 of 43 |
| Copies of the old text left | — | repairs 3 and 4: none; repairs 1 and 2: only the two diffusion forks, where the text is true |
| Copies of the new sub-pixel note | — | 194 in 39 files |

The code comparison was calibrated before it was trusted, on a scratch copy of the base. A comment-only edit had to
read as identical, and it did. `REG_LAMBDA` 0.06 → 0.07 had to read as different, and it did. `//!WIDTH HOOKED.w 16 /`
→ `8 /` had to read as different, and it did.

**The step off the plan** ([random-chaos](WORKFLOW-SAVED-MEMORY.md#random-chaos)): the rebuild harness was first run
on the untouched tree as a calibration, for every generated file rather than only the five `smoke.sh` covers. That
run found repair 5. A second unplanned check, for passes whose output no later pass reads, found lead L1.

**Not checked here, and why.** There is no GPU in this session, so no shader was compiled or run. The code is
unchanged, so this prediction is recorded before any run (pre-registered, 2026-10-04): *on a deterministic host,
`smoke.sh` passes every step, and a render through any changed shader is byte-identical to the same render at
`87f43f3`. Any differing frame refutes it.*

**Knock-on for the Metal port.** `tests/gen_metal.py` records the SHA-256 of the whole GLSL file
(`source_sha256`), comments included. Every translated graph whose source shader changed here now carries a stale
hash. Regenerate them with `gen_metal.py` on the local machine; it needs `glslc`.

### Open leads for the local ladder

None of these were changed: each changes behaviour or cost, and needs the ladder, timing from a file and `smoke.sh`
([regression-gate](WORKFLOW-SAVED-MEMORY.md#regression-gate), [variants-not-overwrites](WORKFLOW-SAVED-MEMORY.md#variants-not-overwrites)).
One assumption sits under the cost leads and has not been checked: that libplacebo runs every pass of a hook, even
one whose saved texture no later pass binds. If it skips such passes, L1 and L2 cost nothing and fall away.

**L1. Edge-mask passes that nothing reads (8 files).** In the four-, five- and six-frame shaders
(`quaddirectional-*`, `quintdirectional-*`, `sextdirectional-*`, `human-reading-quad.glsl`), `EDGE_A` and `EDGE_B`
are computed at full resolution on every output frame, and no pass binds them. `gen_quaddirectional.py` (line 577)
deliberately leaves the snap gate out of the four-frame warp, but it still emits, and rewrites, the two passes that
fed it. The six-frame shader also computes `LUMA_F_F`, a full-resolution luma that nothing reads. *Proposal:* the
generators stop emitting these passes. *Prediction:* every render is byte-identical, and render time from a file
falls by more than the noise of three interleaved runs. *Refuted by:* any differing frame, or no fall in time. Note
that the pass counts in SHADERS.md would change.

**L2. Work whose result is multiplied by zero, or never reaches the output.** In every file that defines it (33),
`SNAP_STRENGTH = 0.0`, so the edge masks and the snapped texture reads in the warp cannot change the output. The
source marks this "TESTING ... Not yet confirmed either way". In the base, the B→A chain (four searches and two
median passes) is computed and nothing downstream reads it. The generators clone these passes for the N-frame
shaders, so they cannot simply be deleted from the base. *This is a decision, not a measurement:* keep the snap
experiment open, or retire it ([fit-for-purpose](WORKFLOW-SAVED-MEMORY.md#fit-for-purpose)). If it is retired, the
prediction is the same as L1's.

**L3. Contrast gates that can never fire (41 files).** At the 1/8, 1/4 and 1/2 levels `MIN_CONTRAST = 0.0`. The
range it tests is never negative, and the test is a strict `<`, so the gate is dead code. It still reads 25 texels
per texel at the 1/8 and 1/4 levels and 9 at the 1/2 level. The source marks it "TESTING at 0.0 ... Not yet
confirmed". *Decision for the human:* retire the gate, or restore a threshold and measure it.

**L4. The coarse search sets the flow's fraction, and nothing corrects it (the base).** Writing the base out shows
that its half-resolution flow is $0.75\,m + 2n$ full-resolution pixels. Here $m$ is the coarse search's result in
units of $\tfrac{3}{64}$ coarse texel, and $n$ is a whole number. A motion of exactly $16$ px per interval is
therefore represented exactly only if the coarse search returns $m \in \lbrace 0, \pm 8, \pm 16, \pm 24 \rbrace$.
Its natural nearest answers, $m = 21$ or $22$, put the total at $15.75$ or $16.5$ plus an even number, never
$16$. *A cheap step first* ([steps-before-leaps](WORKFLOW-SAVED-MEMORY.md#steps-before-leaps)): read `FLOW_S_AB`
raw on the ladder's 16 px/frame cases (L7, M1, M2, M3) and count how often $m \equiv 0 \pmod 8$. *Then the
experiment, as a variant:* round the coarse result to whole half-resolution texels (multiples of $\tfrac18$ coarse
texel) at the S→E handoff. *Prediction:* no change where the coarse search already lands on $m \equiv 0 \pmod 8$,
a gain on the textured even-speed translations, a loss on speeds that are not a whole even number of pixels, and
the ladder mean within $\pm 0.10$ dB. *Refuted by:* no gain on L7 and M1-M3, or a fall of the mean by more than
0.10 dB. The lead concerns the base and its two-frame forks. The field shaders run the sub-pixel fit, which can
move the flow by up to half a texel. The variational cascade refines the flow continuously and may not share the
property; that has not been checked.

**L5. The cel-animation class still has `ZERO_SEED = 0`.** The six files in `shaders/animation/` were built on
2026-09-05 and set `ZERO_SEED = 0`. Their parent, `bidirectional-interpolation-animation.glsl`, switched it on on
2026-09-06 for a measured rise from 19 to 50 dB on periodic structure below the coarse Nyquist. Their comments say
OFF and are accurate, so nothing was repaired. Whether the experimental class should follow its parent is a decision
with a ladder behind it ([ANIMATION.md](shaders/animation/ANIMATION.md)).

**L6. A value computed and never used in every reading tail.** `lum` in the paint pass (line 2184 of the base) comes
from `tests/add_human_reading.py`. The compiler removes it, so it costs nothing. It can be dropped the next time the
tails are regenerated.
