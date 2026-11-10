# S-11: carry the flush edge exclusion, not the centre-column barrier

GPT GC2803, 10 November. **First worker read: in progress until the finite replay below returns.**
Local retains module/build/notebook/post ownership. This read concerns HX-2.1 only; HX-2.2's ranking
claims, HX-2.3's past census and asymptotic interpretations are excluded.

## Sources and exact additional content

Read the full HX-2 report, its first claim, the complete SKM-HX-2-1 report/verdict and its relevant
three scripts/outputs from `cited/local/sw02-all-20261106.tar.gz`, SHA256
`c231157f6daeb1433d2c8aaf2e0190f78b5c4723009fdcc32ee8842a5c11d94c`.
The skeptic's flush correction is essential. Current kit commit
`03a19bf6240b63c6d15894c5f7552f3a6091d937`: read `Rule30FrozenRuler` through its depth/frozen-ruler
proofs, `Rule30RightPeriods`' period definitions and statements, and the exact `c7`, `c7cut`,
edge and translation lemmas in `Rule30ZeroBoundaryBarriers`. Also read closed kit PR42's full
body, conversation and review summaries (head `ee2f42152cc62b862af2c6e21c00a8e1b5887ed7`):
the general frozen-ruler theorem is already proved and credited; it is not an S-11 discovery.

Record searched: record_find `c7cut` + `seed`; current known_find `ether`/`c7cut` + `seed`,
including lean/equivalents/catalogues, portal and current open PR source. The last complete refresh is
GC2802, 10:54:14Z, kit03a19bf6/portal10:53:59Z/20PRs. No exact specialization appeared in those
matches; that is not a priority claim. `seed_rows_return_iff` is in the Mathlib equivalents, not
the core FrozenRuler module. We can avoid this dependency entirely.

Outside primary source: [rule30-open SeedPastPeriods](https://github.com/lhallee/rule30-open/blob/1ddcd41186e245d6a001604e15b584981990591a/Rule30Open/Frames/SeedPastPeriods.lean),
current HEAD `1ddcd41186e245d6a001604e15b584981990591a`; read its `phiF_topAt`,
`phiIter_topAt`, `phiIter_white`, `exists_top` and full `rho_not_evZero` proof, plus its note.
The nonfinite past is known there. Do not sell “no finite cut is a past row” as additional.
The meaningful S-11 content is the exact finite depth/phase and the sharp **flush** ether-word
exclusion, as specializations of the existing edge dynamics.

## Mathematical carrying step

Write `r_N = code (c7cut N) (7N+6)`, using actual rightmost black cells, and let `C_k` be the
cycle of the one-bit code under the map `T`, restricted to its first k bits.

1. **Finite-prefix dynamics.** The first k output bits of `T` depend only on the first k input
   bits. The induced map is a permutation: bit0 is retained, and after recovering bits below i,
   bit i is recovered by XOR with the known lower-bit term. This holds on all bit strings and
   on the odd ones. Thus a cycle and its complement are invariant in both directions. This is
   the known triangular-map argument, not a new odometer theorem.
2. **The seed cycle.** Start with1, iterate the finite map, check a return to1 and distinctness
   before it. Induction on time then proves that these are *all* seed residues, with no appeal
   to a sampled horizon. The required finite facts are: C9 has32states,129 is absent, while
   phase16 has residue385 modulo512, hence129 modulo256; C13 has64states.
3. **Uniform cut prefix.** For every N, `r_N` has prefix129 modulo512: bits0 and7 are black,
   bits1..6 and8 white. For N=0, bit8 lies outside the cut and is white; for N>0, it is inside
   but its residue is not black. That endpoint case must be included in the Lean proof.
   Consequently `HasDepth r_N 8 16`. The general `depth_shift`/`frozen_ruler` already gives,
   at every physical tick t, agreement below8 and disagreement at8 with seed phase16+t.
   Complement invariance additionally excludes agreement below9 with *any* seed phase after
   any t, not only the aligned phase. This last sentence does not follow from the aligned
   `depth_shift` sentence alone; use injectivity of the finite map or a checked cycle-complement
   invariant. Equality with a seed row, including translated seed rows, is then impossible.
4. **Flush ether words.** The kit's ether has4 temporal phases and7 spatial positions. Retain
   only positions whose endpoint is black:13 words. Their prefixes of length13 avoid C13.
   Therefore at every seed time, cells at distances0..12 from its rightmost black cell cannot
   equal any such word. The other15 phase/position words begin white and are excluded by the
   black edge itself. The depth13 bound is sharp if the deepest word's12-prefix occurs at55.
   Kit `evol_c7_four`/`evol_c7_shift` cover all phases/positions, and `seed_code` connects the
   finite cycle to actual whole-line seed rows.

This carries the universal reduction **conditional on the stated finite checks**. The module
should check those finite facts in Lean, not assume the Python result as an axiom. No Lean
compilation or kernel proof of these new specializations is claimed here yet.

## Scope repair and useful controls

The words **flush with the rightmost black cell** are part of the theorem. “No thirteen ether
cells behind the edge” without that condition is false: seed row204 has a black-ended13-cell
ether word at distances7..19; row80 has a white-ended14-cell word at distances3..16. These
are negative controls, not exceptions to the flush statement.

The bare whole-row non-equality for the unmodified c7cut family has a much cheaper span-parity
proof: width14N+8 stays even under evolution, whereas seed rows have odd width. A submission
should lead with the depth and flush-word statements. Unexpected control, predicted before
replay: remove the rightmost black pulse of c7cut1. The resulting cut has odd span15 but the
same forbidden9-prefix129. This shows why the local edge statement says more than span parity;
it does not establish a general exclusion for arbitrary caps or shifted windows.

Do not infer that excluding the kit's witness family removes the all-finite ranking barrier,
that every finite code off the seed orbit has this depth, or that the seed has no long ether
intervals at positive offsets. There is no centre-column/prize consequence. The separate
short-cut classification and predecessor-period census need their own checks if ever included.

## Frozen independent finite replay

[Checker](../tests/probes/swarm/sw02/block10/s11_read_check.py), SHA256
`b32d5c75d5d1e8277e5550277d80433aef66246171e68ea6e9a6aeabe6460b02`.
No swarm producer is imported. Literal eight-entry cell table on whole-line rows, tuple edge
map and packed expression cross-check one another. Fixed rows0..204, C9/C13 only; four
c7cut controls through32ticks; no census, width enlargement, randomness or new Lean/Wolfram run.

Prediction: C9=32/excludes129/low8phase16, C13=64, all13exits
`9;9,6,3;9,9,3;3,9,9,6,13,3`;12-prefix sharp at55; offset and odd-span controls pass.
Counterfactual: any mismatch stops the carrying verdict; diagnose it before a module is built.

One Intel scalar stage, one worker/nice10, no GPU. Under run_capped.py tree tracking and the
existing all-thread aggregate controller `tests/probes/metal_scope/stage.py`: stage5 aggregate
CPU seconds (including outer monitor),45wall; individual job3CPU/15wall; outer15CPU/60wall;
tree768MiB RSS, max6processes, launchfree4096/runningfloor1024MiB, swapgrowth4096MiB,
4MiB/file/16MiBstage. Pressure, thermal or monitor failure stops the stage, preserves evidence,
and redirects to hand reasoning; no retry or enlargement is authorized by this freeze.
Private executable plan SHA256 `f171059ae32d18c84ae4c61ae181364c61bf3bc115aeb322266b9159ed8b3c4d`.

## Next executable handoff

After the finite replay, give Local the carried small-module scope: `c7cut_depth`8/16,
its frozen-ruler corollary, no seed flush13-ether prefix, and the sharp12witness. A finite
prefix invariant may supply the stronger all-phase nonagreement; keep it explicit. Existing
kit general results should be cited/imported, with new calculations checked through ordinary
kernel reduction/certificates. Do not formalize HX2.2 or past-period claims in S-11. Local
continues S-13/S-12 first; this is a passive statement handoff, not a competing build request.
