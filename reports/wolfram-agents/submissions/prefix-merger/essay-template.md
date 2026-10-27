---
Template: ComputationalEssay
Name: A seven-cell rewrite beside the white wall that merges in two steps, for every tail and every finite cut
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-27
Description: A partial result on the Rule 30 Prize kit's zero-boundary left half, proved in Lean: the starts 1100011 and 1010101 beside the white wall, followed by the same arbitrary tail, have equal rows from time 2 on, and so do their truncations at every common depth of at least 7; inside the kit's reconstruction Theta, the corresponding free-bit change is confined to depths 1 to 6.
Abstract: ABSTRACT_PLACEHOLDER
Keywords: [rule 30, Rule 30 Prize, Q01, zero boundary, Theta, reconstruction, merger, finite support, truncation, Lean 4, LeanLink]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[Rule30ZeroBoundary in the kit](https://github.com/WolframInstitute/Rule30PrizeKit/blob/main/lean/Ruliology/CellularAutomata/Rule30ZeroBoundary.lean)"]
---

## The question

The kit's open statement `Q01` concerns the left half of rule 30 beside a white wall (`Rule30ZeroBoundary.zrow`): can a finitely supported start keep the cell beside the wall black at every even time? The kit rebuilds every such start from its free bits by `Theta`. Two different free-bit sequences give different starts, but their histories can *merge*: once two rows are equal, they stay equal. When a merger happens, which cells were really different? And does the merger survive when both starts are cut to a common finite width, as every finitely supported start must be? This essay gives an exact answer for one such merger: a rewrite of the seven cells nearest the wall.

## Two starts that merge, whatever follows them

One step of the zero-boundary left half, on depths `1, 2, …` (the wall at depth `0` is white):

```wl
zstep[w_] := With[{p = Join[{0}, w, {0, 0}]}, Table[BitXor[p[[k + 2]], BitOr[p[[k + 1]], p[[k]]]], {k, 1, Length[w] + 1}]];
startA[tail_] := Join[{1, 1, 0, 0, 0, 1, 1}, tail]; startB[tail_] := Join[{1, 0, 1, 0, 1, 0, 1}, tail];
tails = {{}, {1}, {0, 1, 1, 0, 1}, {1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1}};
Table[{Nest[zstep, startA[tl], 1] === Nest[zstep, startB[tl], 1], Nest[zstep, startA[tl], 2] === Nest[zstep, startB[tl], 2]}, {tl, tails}]
```

For each tail the rows differ at time `1` and agree at time `2`. Dropping the black cell at depth `7`, with nothing after it, they no longer agree:

```wl
{Nest[zstep, {1, 1, 0, 0, 0, 1}, 2], Nest[zstep, {1, 0, 1, 0, 1, 0}, 2]}
```

## The theorems

- **The rewrite** (`mergePrefix_two`, `mergePrefix_future`). For every tail `τ : ℕ → Bool`, the starts `mergePrefix false τ` (depths `1 .. 7` read `1 1 0 0 0 1 1`) and `mergePrefix true τ` (`1 0 1 0 1 0 1`), with `τ` from depth `8` on, have equal rows at time `2`, and therefore at every time `2 + t`.
- **Finite cuts** (`mergePrefix_truncate`, `mergePrefix_truncate_fin`). For every `W ≥ 7`, the truncations of the two starts at depth `W` are finitely supported and have equal rows at time `2`.
- **The depth-7 cell is needed** (`mergePrefix_needs_seven`). With depth `7` white and a white tail, the truncations at depth `6` differ at time `2`.
- **Inside `Theta`** (`theta_prefix`, `theta_first_edit_local`, `theta_truncate_merge`). Take free-bit sequences `f` and `g` that agree from index `1` on, with `f 1 = f 2 = true`. Then `Theta f` reads the prefix with `a = f 0` at depths `1 .. 7`, and `Theta f` and `Theta g` agree at every depth `k ≥ 7`. Their truncations at every common depth `W ≥ 7` have equal rows at time `2`.
- **Reading a merger** (`trace_tail_iff_row`, `merge_preserves_last_black`, `odd_edits_iff_guarded_merge`). Rows equal at time `T` are the same as equal column `1` from `T` on. Merged starts have their last black cell at the same depth. Agreement at every even time and every time from `T` on is the same as a merger at `T` together with the earlier even observations.

## The idea of the proof

1. **Locality.** A cell at depth `k` and time `2` reads the start at depths `k - 2 .. k + 2`. From depth `10` on the two starts read only the common tail, so their rows agree there (`step_local`). Depths `0 .. 9` read the start up to depth `11`: the prefix and the first four tail cells. A Boolean case split on those four cells settles them.
2. **Cuts.** For `W ≥ 7` the truncation of `mergePrefix a τ` is `mergePrefix a` with the cut tail, at every depth `k ≥ 1` (`truncate_mergePrefix`). The supplied initial value at depth `0` is ignored; that boundary is held white (`zrow_congr_pos`). So the cut starts are again an instance of step 1.
3. **Inside `Theta`.** `Theta f` is the kit's reconstruction `recon (alt f) · 0`, and `alt f` differs from `alt g` only at time `1`. From time `2` on the reconstructions agree at every depth (`recon_local`). At times `0` and `1` the depths `7` and `8` read `alt` only up to time `8`, where the window is fixed by `f 0` and `f 3`, and a finite check shows they do not depend on `f 0`. The kit's recursion `recon_two` then carries agreement at two consecutive depths outward to every depth.
4. **Reading.** `trace_tail_iff_row` is the kit's `zrow_det` and `zrow_shift`. `merge_preserves_last_black` compares the two edges given by the kit's `zrow_edge`.

## The formal proof

The module, built against the kit at the verifier's commit:

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["LEAN_PLACEHOLDER", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The headlines, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30ZeroBoundary"};
thm = rule30Submission["Rule30Submission.theta_truncate_merge"];
Table[rule30Submission["Rule30Submission." <> n]["TypeForm", "Open" -> opens], {n, {"mergePrefix_two", "mergePrefix_truncate", "mergePrefix_needs_seven", "theta_first_edit_local", "theta_truncate_merge", "merge_preserves_last_black", "odd_edits_iff_guarded_merge"}}]
```

The axioms of the headline `theta_truncate_merge` are standard ones only (the checker verifies all eleven headlines and replays the whole module):

```wl
thm["Axioms"]
```

The proof's structure, one level down from the headline:

```wl
thm["CallGraph", "Depth" -> 1]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
thm["KernelCheck"]
```

## What is not proved

- Nothing decides `Q01`, bounds a death time, or concerns the center column. `FinSupp (Theta f)` is the open hypothesis of `Q01`; nothing here instantiates it.
- The untruncated merger of `Theta f` and `Theta g` is the kit's `two_step_shift`. Equal last black depth is a short application of `zrow_det` and `zrow_edge`. What this module adds is the explicit seven-cell rewrite, its survival under every common cut `W ≥ 7`, and its localization inside `Theta`.
- `W` is a cut bound; the actually occupied width of a truncated start may be smaller.
- The depth-7 countercontrol shows only that this rewrite needs depth `7`; it says nothing about other six-cell rewrites.
- The exact rewrite was not found in the kit's catalog or the submissions list as we read them, which is a statement about our search, not a global novelty determination.
- The Wolfram Language computations above are illustrations; the theorems do not depend on them.

## Provenance

The merger turned up in a census of sideways rows on the Apple M5. GPT (OpenAI) proved the two-step merger of this seven-cell pair by hand (GC1930), and Claude (Anthropic) read it independently (L996). GPT then wrote the statement chain for this module, separating the general reconstruction facts from the finite-cut rewrite (GC1965). Claude formalized it. The record is at github.com/ghywel/placego, reports/wolfram-agents/GPT-S3-FINITE-EDITS-STATEMENT-CHAIN.md and reports/wolfram-agents/submissions/prefix-merger.

## References

[1] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[2] Wolfram Institute, [*The Rule 30 Prize kit*](https://github.com/WolframInstitute/Rule30PrizeKit), 2026: `Rule30ZeroBoundary.zrow`, `truncate`, `Theta`, `recon`, `recon_local`, `recon_two`, `zrow_det`, `zrow_shift`, `zrow_edge`, `two_step_shift`.
