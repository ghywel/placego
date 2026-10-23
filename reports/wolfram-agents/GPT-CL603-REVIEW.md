# CL603: width-14 channel carrying review

GPT, 2026-10-23. Requested source: commit `fe63c39b`,
`submissions/channel-14/Rule30Submission.lean` relative to this directory.
SHA256: `7559970244b025c1733a9fc98f1f16a2583366ff8d70edb5cfda50bd71f42fd7`.

**Verdict: PASS for the formal carrying steps and the exact width-14 headline.**
The implementation supplies the previously missing explicit-data soundness interface.
No gap found in section 7, range assembly, or its connection to the physical bound.
This is an independent source/statement review, not a fresh Lean build or kernel replay.
Cloud's committed receipt reports pass for 3,961 replayed constants and eight headlines,
with no new axioms. The README's source digest matches the actual file; the JSON itself
does not embed a source digest. Cloud's measured times and memory are attributed to Cloud.

Before submission, correct the essay's leftover `218` to `300`. This is an explanatory
constant error, not an error in the formal theorem or abstract. Two further documentation
qualifications appear below. Frozen submitted-source files were not edited by GPT.

## What the theorem actually says

For every natural number n there is ONE finite set S of Boolean words such that every
full-space configuration x with center clock `evol x t 0 = decide (t % 2 = 1)` for all t
has `visFrom x 0 n` in S, and

`S.card * 1000000000 ^ n <= 300 * 1184655442 ^ n`.

The quantifier order is important: S is shared by all those configurations. The words
are column 1 at even times, not all columns or the single seed's center sequence. The
rate is asymptotic, with the finite correction `log2(300)/n`. This does not exclude a
clocked configuration, prove Q01, or solve a full prize question. The headline does not
claim that the supplied state sets are exact reachable sets, minimal, or unique.

## Carrying steps checked

1. **Four images, section 7 lines 923–968.** `imgs4In` includes all four combinations
   of the exterior bit at the two successive times. `imgs4In_spec` converts
   `((tgt >> t) & 1) == 1` to `tgt.testBit t = true`, using quotient/remainder at
   `2^t`. Then `u,v <= 1` exhausts 00, 01, 10, 11, and `nxtT_eq` identifies the
   shifted exterior input with `step2`. The proved direction is soundness (passing
   implies every required membership), which is exactly what the bound needs.

2. **Fuel is sufficient, lines 978–1021.** The superficially dangerous zero-fuel
   branch returns true, but `wordOK_spec` requires `w < 2^fuel`. At fuel zero this
   forces the word empty. For a nonzero word, `pos64_spec` selects its highest set
   bit p; `p <= fuel - 1`. Clearing that bit gives a word below `2^p`, hence below
   `2^(fuel-1)`. Other set bits are preserved by `testBit_clear_of_ne`. Thus fuel
   cannot run out while an unchecked member remains. The separate `w < 2^64`
   premise justifies the six-comparison top-bit routine. Routing uses the low bit
   of the GLOBAL row `base + j`, not the bit position within the word alone.

3. **All words are covered, lines 1030–1063.** `stateCheck_spec` splits a row s at
   `64*k`: lower rows use the induction hypothesis; the upper word uses
   `j = s - 64*k`, with `j < 64`. `word_testBit` and `word_lt` establish the exact
   extraction and both fuel premises. Empty-word and failed-word branches are
   handled explicitly. The conclusion covers every `s < 64*nwords`, including
   word-boundary positions; it does not claim coverage beyond that range.

4. **Coverage and liveness, lines 1065–1104.** `StateOK` fixes the scan count to
   `(2^M) >> 6`; it is not an unchecked certificate field. For `M >= 6`, divisibility
   by 64 gives `64*nwords = 2^M`, so every physical window row is covered.
   `explicit_sound` uses the actual row's parity to select the same graph edge
   used by `st`. `bset` is zero at EVERY index at or above the graph length, not
   only at the chosen DEAD sentinel. If an actual member tried to use such an
   edge, even its 00 image would have to be a set bit of zero, a contradiction.
   A label with no source members may legitimately have a dead edge: `EdgeOK`
   requires liveness only when that label is used by a member.

5. **Assembly and root.** `range_one` proves precisely the half-open singleton
   interval, and `range_split` partitions at mid by `i < mid` or `mid <= i`.
   Source binding checks account for all 919 single-state theorems and all 918
   splits up to `[0,919)`, with matching endpoints and child references.
   `all14` ties 919 to the SAME successor list's length. `root14` independently
   checks the full initial bitset. A malformed lookup tree is not an extra trust
   assumption: whatever function it defines must satisfy these same root and
   closure proofs. Aliases or extra high bits do not invalidate an upper bound.

6. **Weights and physical interface.** `bound_of` is the previously reviewed body
   of `Cert.bound` after obtaining root and closure. `st_inv` keeps the actual
   physical row in the state set, `visFrom_mem` embeds the entire visible word,
   and `weight_bound` bounds accepted words on the same graph and state indices.
   The formal headline uses checked positivity, list lengths, root weight and
   `wcheck14` with D = 1000000000, R = 1184655442, minimum weight 653189453 and
   prefactor 300. Cancelling the minimum weight uses its strict positivity.
   No reconstructed `Cert.Valid.hcheck` or final monolithic decision is smuggled in.

The executable proof bodies before section 7 are unchanged from the reviewed width-12
module; only the introductory documentation differs. The pilot and width-14 generic
proof bodies through section 7 are identical. All eight receipt headlines agree with
these reviewed steps; no `sorry`, new axiom, native decision, or replacement evolution
definition is introduced in the new interface.

## Pilot controls and the unexpected coverage check

`neg_dead`, `neg_swap`, and `neg_drop` are genuine rejections. The tiny independent
literal-cell audit finds the following witnesses `(source row, u, v, image)`:

| Control | Witness | What it detects |
|---|---|---|
| false dead edge | `(1, 0, 0, 4)` | odd source member needs a nonempty successor |
| swapped targets | `(0, 0, 0, 1)` | label 0 is routed to the wrong set |
| removed image | `(0, 0, 0, 1)` | bit 1 was deleted from target state 3 |

The literal cellular update and a separate packed update agree on all 263 evaluated
transitions, including the complete positive root check. This is small diagnostic
support, not an independent width-14 closure certificate or Lean replay.

**`neg_missing_root` is not a negative control.** Its proposition asserts the correct
root transition succeeds, with the original full root and correct targets. Keep it
as a positive control under an accurate name; do not count it as root-corruption or
missing-interval rejection. The three advertised negative controls remain valid.

Unexpected adversarial check by hand: `stateCheck ... 0 B` returns true for any B,
and an empty source can satisfy local closure vacuously. These are real weaknesses of
an unqualified local check, but not of this theorem: the fixed scan-count identity
and `root14` separately rule out the two abuses. A future shortened-chunk interface
would need its own explicit interval coverage. This implementation uses whole states,
so CL602's missing-interval pilot is not present as an executable negative; its
obligation is discharged here by the formal coverage proof, not by that mislabeled test.

## Presentation corrections and provenance

- `essay-template.md:68` says `w_0 <= 218 * wmin`. The actual numbers give
  `w_0 = 195955063994` and `wmin = 653189453`; the proved prefactor is **300**.
  The abstract, headline, and formal `w0_14` already use 300. Correct the template
  and reassemble the essay; this requires no change to the Lean module.
- The provenance paragraph at line 136 says the graph and growth rate are recomputed
  in the essay. The essay rebuilds the graphs at widths **6 and 8**; at width **14**
  it embeds the graph and weights, checks the weight inequalities, and computes
  growth/prefix diagnostics from that supplied graph. State that distinction.
  Kernel-checked closure still establishes the theorem without trusting BFS exactness.
- The pilot's introductory docstring is inherited width-12 text. It is not the new
  submitted module's description. Rename or annotate `neg_missing_root` as above
  when doing documentation cleanup; this is not a formal-proof blocker.
- The committed JSON and timings are Cloud's receipt. Local still owns notebook
  execution, import readback, size/API behavior, and submission. The four-minute
  verifier limit is not a theorem about performance; no automatic pass is promised.

## Audit receipt and disposition

`tests/probes/channel14_source_review.py` was frozen with predictions, stop conditions,
independent literal/packed controls and caps before its sole run. It passed source
and exact essay bindings, range references, receipt schema and the tiny controls.
No width-14 automaton regeneration, full closure replay, Lean build, Wolfram execution,
or width-16 attempt was made. The script preserves the result in its outcome header.
The two standing startup checks also completed ALL CHECKS PASS, retaining their old
refuted predictions. Initial invocations at the wrong probe directory failed before
execution; the correct existing `lexicon/` paths were then used, not modified.

Formal carrying gate cleared in the stated scope. Cloud should make the two essay
corrections, then Local can apply its existing build/readback/submission gates. There
is no new research or duplicate independent-review request from GPT. Q01 remains open;
the owner-requested heartbeat remains paused.
