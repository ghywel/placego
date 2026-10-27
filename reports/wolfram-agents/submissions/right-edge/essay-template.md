---
Template: ComputationalEssay
Name: Every finite row's right edge is the single cell's ruler, cut off at one depth
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-27
Description: A partial structural result on Rule 30, proved in Lean against the kit: the right edge of every finite nonzero starting row emits exactly the single black cell's white triangles, shifted in time, except that every triangle of width k - 1 or more is cut to exactly k - 1, where k is the depth to which the row's edge code agrees with the single cell's orbit; the cut width lies in a gap of the single cell's ruler.
Abstract: ABSTRACT_PLACEHOLDER
Keywords: [rule 30, Rule 30 Prize, right edge, edge code, 2-adic, ruler, finite configurations, universality, Lean 4, LeanLink]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[Rule30RightPeriods in the kit](https://github.com/WolframInstitute/Rule30PrizeKit/blob/main/lean/Ruliology/CellularAutomata/Rule30RightPeriods.lean)"]
---

## The question

Started from one black cell, rule 30 has a famously regular right edge. Read the row from its rightmost black cell leftward: just behind that cell there is a run of white cells, and its length, step by step, is a *ruler*: 0, 2, 0, 3, 0, 2, 0, 5, 0, 2, 0, 3, 0, 2, 0, 6, … The kit's `Rule30RightPeriods` describes the single cell's right diagonals, whose periods produce this ruler. What does the right edge of an *arbitrary* finite starting row look like? This essay proves that it is always the same ruler, shifted in time and cut off at one depth that the row itself determines.

## The ruler, and two rows that copy it

One step of rule 30, on a finite row (white beyond both ends), and the length of the white run just behind the rightmost black cell:

```wl
step[w_] := With[{p = Join[{0, 0}, w, {0, 0}]}, Table[BitXor[p[[i - 1]], BitOr[p[[i]], p[[i + 1]]]], {i, 2, Length[p] - 1}]];
width[w_] := With[{r = Reverse[w]}, LengthWhile[Drop[r, First[FirstPosition[r, 1]]], # == 0 &]];
widths[init_, n_] := width /@ Rest[NestList[step, init, n]];
single = widths[{1}, 40];
Take[single, 32]
```

The single cell gives `0, 2, 0, 3, 0, 2, 0, 5, 0, 2, 0, 3, 0, 2, 0, 6, …, 0, 8`: a zero at every other step (the black run at the edge alternates between one cell and more), and between them the widths of the white triangles the edge emits.

The row of four black cells copies the ruler from time `3` on, except that every width of `4` or more becomes exactly `4`:

```wl
four = widths[{1, 1, 1, 1}, 32];
{Take[four, 16], Take[four, 29] === Table[Min[single[[t + 3]], 4], {t, 1, 29}]}
```

The row `1 0 1 1 1` does the same with phase `5`, and the row `1 1`, a *rain edge*, emits only lone white cells, the ruler cut at width `1`:

```wl
{widths[{1, 0, 1, 1, 1}, 29] === Table[Min[single[[t + 5]], 4], {t, 1, 29}], Take[widths[{1, 1}, 12], 12]}
```

The cut widths `1` and `4` never occur in the single cell's own ruler. The theorem says why, and that this is the only thing a finite row can do.

## The theorem

Read a finite nonzero row `x` from its rightmost black cell `e`: bit `k` of its **edge code** is the cell at distance `k` from `e` (`code x e k = x (e - k)`). The single cell's code is `one` (bit `0` only), and `orbit s` is its code at time `s`.

- **The edge map** (`edge_evol`). The rightmost black cell of `evol x t` is `e + t`, and its code is `T^[t] (code x e)`, where `T c 0 = c 0`, `T c 1 = c 1 xor c 0` and `T c (k + 2) = c (k + 2) xor (c (k + 1) || c k)`. This is the 2-adic right-edge map of Coven, Pivato and Yassawi.
- **Depth** (`HasDepth`, `depth_dichotomy`). A code has depth `k` with phase `s₀` if it agrees with `orbit s₀` on bits `0 .. k - 1`, while no code of the single cell's orbit agrees with it on bits `0 .. k`. Every finite nonzero row has a depth `k ≥ 2`, or agrees with the single cell's orbit at every depth.
- **The frozen ruler** (`frozen_ruler`). If the code of `x` has depth `k ≥ 2` with phase `s₀`, then for every time `t`, the code of `evol x t` agrees with the single cell's code at time `s₀ + t` below bit `k` and differs from it at bit `k`. Its white run behind the edge cell is the single cell's whenever that run is shorter than `k - 1`, exactly `k - 1` whenever the single cell's run is at least `k - 1`, and never longer.
- **The cut is in a gap** (`no_width_at_depth`). The single cell's code never has a white run of exactly `k - 1` behind its edge, when some code has depth `k`.
- **The first level for every row** (`edge_run_alternates`). The cell behind the edge cell flips at every step.

## The idea of the proof

1. **The edge map.** The rightmost black cell `e` always gains a black right neighbour (`rule 1 0 0 = 1`) and nothing beyond it, so the edge moves one cell per step. Read from the edge, the new bit `k` is the rule applied to the old bits `k`, `k - 1` and `k - 2`, with white beyond the edge: that is `T`.
2. **Triangularity.** Bit `k` of `T c` reads only bits `k - 2 .. k` of `c`, and passes bit `k` through an exclusive or. So two codes that agree below `k` and differ at bit `k` keep doing so for ever (`iter_agree`, `iter_diff`). A row of depth `k` and the single cell, shifted by `s₀`, are such a pair.
3. **Widths.** A white run shorter than `k - 1` is read below bit `k`, where the two agree. If the single cell's bits `1 .. k - 1` are white, its bit `k` must be white too, by step 4, so the row's bit `k` is black: its run is exactly `k - 1`. A longer run for the row would force the single cell's bits `1 .. k - 1` white and bit `k` black, which step 4 excludes.
4. **The gap.** Suppose the single cell's code at some time `u` has bits `1 .. k - 1` white and bit `k` black. It then agrees with `one` below `k` and differs at `k`, so by step 2 the codes at times `u + s₀` and `s₀` differ exactly at bit `k`. The row's code differs from the code at `s₀` exactly at bit `k` too, so it agrees with the code at `u + s₀` on bits `0 .. k`, contradicting its depth. No counting of periods is needed.
5. **Every row has a depth.** Bit `0` is always black, and the single cell's codes at times `0` and `1` cover both values of bit `1`. So every code agrees with the orbit below `2`, and the least depth where agreement fails, if there is one, is at least `3`.

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
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30Realization", "Ruliology.CellularAutomata.Rule30Jen"};
thm = rule30Submission["Rule30Submission.frozen_ruler"];
Table[rule30Submission["Rule30Submission." <> n]["TypeForm", "Open" -> opens], {n, {"frozen_ruler", "no_width_at_depth", "depth_dichotomy", "edge_evol", "edge_run_alternates"}}]
```

The axioms of the headline `frozen_ruler` are the three standard ones and nothing else (the checker verifies all five headlines and replays the whole module):

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

- Nothing about the center column, or any of the Prize problems. The center sits ever deeper behind the edge, and this result says nothing there.
- The infinite-depth case is stated only as agreement with the single cell's orbit at every finite depth, with a phase that may depend on the depth. Whether every finite row of infinite depth is one of the single cell's own rows, shifted in time, is open. Our record proves it for every row whose edge code is below `2^24`, by a finite computation that is not part of this module.
- The edge map is not new; it is the right-edge map of Coven, Pivato and Yassawi (2007). The truncation theorem for every finite row is new to the kit's catalog and the submissions list as we read them, which is a statement about our search, not a global novelty determination.
- The Wolfram Language computations above are illustrations; the theorems do not depend on them.

## Provenance

The owner of the project noticed the ruler on the single cell's right edge. Claude (Anthropic), on the Apple M5, found that every finite row keeps it up to one depth (the record's L1000 and L1001), and proved the theorem by hand. GPT (OpenAI) read the proof, replaced its period-counting step with a direct argument (GC1935), and qualified the infinite-depth case. Claude wrote this module, using an argument that needs no period counting at all. The record is at github.com/ghywel/placego, reports/rule30-universal-ruler.md and reports/wolfram-agents/submissions/right-edge.

## References

[1] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[2] E. M. Coven, M. Pivato and R. Yassawi, *Prevalence of odometers in cellular automata*, Proceedings of the American Mathematical Society 135 (2007).

[3] Wolfram Institute, [*The Rule 30 Prize kit*](https://github.com/WolframInstitute/Rule30PrizeKit), 2026: `Rule30RightPeriods`, `Rule30Realization.evol`, `Rule30Realization.evol_seed`.
