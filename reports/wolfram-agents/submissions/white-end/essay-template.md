---
Template: ComputationalEssay
Name: The white end: no column of rule 30 settles into 1 0^q, for any q ≥ 10
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-22
Description: A partial result for Problem 1 of the Rule 30 Prize, proved in Lean against the official statements: the center column is never eventually the repeating word 1 0^q for any q ≥ 10, and the same holds for every column of every configuration with a leftmost black cell
Abstract: Problem 1 asks whether the center column of rule 30 is ever eventually periodic. The kit's catalog excludes the words 1 0^10, 1 0^11 and 1 0^12 by three separate certificates. This essay excludes the whole family 1 0^q, uniformly in q ≥ 10, as the headline theorem Rule30Submission.not_eventuallyWord_white_end, together with the same statement for every column of every configuration with a leftmost black cell (Rule30Submission.white_end). The argument is Jen's: the eight cells right of the column form a finite relaxation on which, after three periods, the next column is forced to read 1 0 0 1^(q-2); two adjacent periodic columns contradict the moving left edge. What is new is the uniformity: a periodicity of the relaxation's white step (W^26 = W^22 on the sets that occur) makes sixteen kernel checks cover every q. The verifier's replay accepts the module with the three standard axioms only. Nothing is claimed for q ≤ 9, and this is not a solution of Problem 1.
Keywords: [rule 30, Rule 30 Prize, Problem 1, eventually periodic, Jen's theorem, strip relaxation, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record, PROOFS.md entry 40](https://github.com/ghywel/placego/blob/main/PROOFS.md)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[wolframcollatzmahler.com](https://www.wolframcollatzmahler.com)"]
---

## The question

Rule 30 updates every cell from itself and its two neighbors: the new color is *left* XOR (*center* OR *right*). From a single black cell it grows a pattern whose center column looks random. Problem 1 of the Rule 30 Prize asks whether that column is ever eventually periodic: whether, from some time on, it repeats a word forever.

The first 60 steps, with the center column in red:

```wl
pattern = CellularAutomaton[30, {{1}, 0}, 60];
ArrayPlot[ReplacePart[pattern, {t_, 61} :> 2 pattern[[t, 61]]], ColorRules -> {0 -> White, 1 -> GrayLevel[0.15], 2 -> StandardRed}, ImageSize -> 520]
```

A proof of Problem 1 has to rule out every word, from every starting time. This essay rules out one infinite family of words: `1 0^q`, one black cell followed by `q` white cells, repeated, for every `q ≥ 10`. It proves it for the center column of the single seed, in the kit's own vocabulary, and for every column of every configuration that has a leftmost black cell.

## The center column, and the words it does and does not settle into

The first 10,000 cells of the center column, and the first 20 of them:

```wl
center = CellularAutomaton[30, {{1}, 0}, {10^4 - 1, {{0}}}];
Take[center, 20]
```

The block `1 0^q` does occur in the column as a finite block; what the theorem excludes is the column *settling into* it. How often each block occurs in the first 10,000 cells, and the longest run of white cells there:

```wl
{Table[{q, SequenceCount[center, Prepend[ConstantArray[0, q], 1]]}, {q, {8, 9, 10, 11, 12, 15, 20}}], Max[Length /@ Select[Split[center], First[#] == 0 &]]}
```

So `1 0^10` occurs six times, `1 0^12` twice, and no white run is longer than 12. None of this proves anything about the infinite column; it shows that the excluded words are not exotic. The kit's catalog already excludes `1 0^10`, `1 0^11` and `1 0^12`, each by its own strip certificate (`Rule30StripCertificateTable`), and the mirror-image family `1^r 0` for large `r` (`Rule30BlackRunBlocks`). The family `1 0^q` as a whole, for every `q`, is what is added here.

## The idea: the eight cells to the right are a finite machine

Suppose column `c` reads `1 0^q` from some time on. Watch the eight cells immediately to its right, `c + 1, …, c + 8`. Their next values depend on column `c` (known: the word), on themselves, and on one unknown cell `c + 9`. Allow that unknown cell both values at every step. The eight cells then move through a finite nondeterministic system with 256 states, and every actual history of rule 30 is one path of it.

The system, with a state as a number below 256 (bit `j` is cell `c + 1 + j`), the column's bit `w` and the outside bit `u`:

```wl
stp[w_, s_, u_] := BitAnd[BitXor[BitAnd[BitOr[BitShiftLeft[s, 1], w], 255], BitOr[s, BitShiftRight[s, 1], BitShiftLeft[u, 7]]], 255];
img[w_, S_] := Union[Flatten[Table[{stp[w, s, 0], stp[w, s, 1]}, {s, S}]]];
mac[q_, S_] := Nest[img[0, #] &, img[1, S], q];
reach[q_, n_] := Nest[mac[q, #] &, Range[0, 255], n];
```

`img` is the image of a set of states under one step, over both values of the outside bit; `mac[q, S]` applies one period of `1 0^q` (a black step, then `q` white steps); `reach[q, n]` is the set of states reachable after `n` periods from every start.

The sets shrink and stop. After three periods they are fixed, and on the fixed set the first cell of the strip, column `c + 1`, takes a single value at every tick of the period. The number of states after 1, 2, 3, 4 periods, whether one more period maps the third set into itself, and column `c + 1` over one period read off the fixed set (`?` marks a tick where both values occur):

```wl
tick[S_, i_] := If[i == 0, S, Nest[img[0, #] &, img[1, S], i - 1]];
word[q_] := StringJoin[Table[Union[BitAnd[#, 1] & /@ tick[reach[q, 3], i]] /. {{0} -> "0", {1} -> "1", {0, 1} -> "?"}, {i, 0, q}]];
Grid[Prepend[Table[{q, Length /@ Table[reach[q, n], {n, 1, 4}], mac[q, reach[q, 3]] === reach[q, 3], word[q]}, {q, {9, 10, 11, 12, 15, 20, 25}}], {"q", "states after 1, 2, 3, 4 periods", "fixed after 3", "column c+1 over one period"}], Frame -> All, Alignment -> Left]
```

For every `q ≥ 10` shown, column `c + 1` is forced: it reads `1 0 0 1^(q-2)`, so it is periodic with the same period `q + 1`. At `q = 9` the third set is not yet fixed and one tick is undetermined; the method says nothing there, and the proof below does not claim it.

**Every `q`, from finitely many checks.** The white step `W = img[0, ·]` repeats on the sets that occur: `W^26 = W^22` on each set `img[1, reach[q, n]]`, `n = 0, …, 3`, for `q = 22, …, 25`. So the behaviour of `q ≥ 26` is that of `22 + (q − 22) mod 4`, and sixteen checks, `q = 10, …, 25`, cover every `q ≥ 10`:

```wl
Table[{q, And @@ Table[Nest[img[0, #] &, img[1, reach[q, n]], 26] === Nest[img[0, #] &, img[1, reach[q, n]], 22], {n, 0, 3}]}, {q, 22, 25}]
```

**The contradiction: Jen's theorem with a clock.** Columns `c` and `c + 1` are now both periodic, with period `q + 1`, from some time `a` on. Rule 30 is left-permutive: the cell at `c − 1` at time `t` is determined by the cells at `c` at times `t` and `t + 1` and at `c + 1` at time `t`. So periodicity of two adjacent columns on a time window propagates to the column on their left, on a window one step shorter, and by induction `L` columns to the left on a window `L` shorter. Meanwhile the leftmost black cell of the configuration moves one cell left per step: at time `t` it is at `e − t`, with everything left of it white. Take the column `c − j` with `j = a + P + L`, where `L` is the distance from column `c` to the leftmost black cell at time 0. At time `a` that column is left of the edge, so white; at time `a + P` the edge is exactly there, so black; yet the two times differ by one period, so periodicity (which reaches that column on a window long enough to contain both times, once the window `[a, b]` is taken long enough) makes them equal. That is Theorem A below: `b ≤ 2a + L + 2P − 1`, which fails for `b` large. If the leftmost black cell starts to the right of column `c`, the clock is re-based after it has passed.

Everything in this section is a computation or a sketch. The proof is the next section.

## The formal proof

The module, as the verifier rebuilds and checks it. Its definitions and lemmas follow the sketch: `stp`, `img`, `Wp`, `mac`, `reach` are the finite machine; `checkQ` and `repOK` are the kernel-decided facts; `win` encodes the actual eight cells and `win_step` proves that the encoding follows rule 30 exactly; `edge`, `left`, `theorem_A` and `no_two_periodic` are Jen's theorem with a clock on the kit's `evol`; `core` and `white_end` assemble the contradiction; the bridge lemmas turn the kit's `EventuallyWord` into the module's `Reads` through the kit's `evol_seed`.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["@@LEAN_SOURCE@@", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The headline theorem, as Lean prints it. For every `q ≥ 10`, the center column is not eventually the word `1 0^q`:

```wl
thm = rule30Submission["Rule30Submission.not_eventuallyWord_white_end"];
thm["TypeForm", "Open" -> {"Ruliology.CellularAutomata.Rule30StripCertificates", "Rule30Submission"}]
```

Its axioms are the three standard ones and nothing else:

```wl
thm["Axioms"]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs:

```wl
thm["KernelCheck"]
```

The general statement, for every column of every configuration with a leftmost black cell. `Reads x0 c q a` says that column `c` of the evolution of `x0` reads `1 0^q` from time `a`, the `1` first:

```wl
rule30Submission["Rule30Submission.white_end"]["TypeForm", "Open" -> {"Ruliology.CellularAutomata.Rule30Realization", "Rule30Submission"}]
```

The same for finite nonzero configurations (a left bound and one black cell; the right side may be infinite), and for every column of the single seed:

```wl
{rule30Submission["Rule30Submission.white_end_finite"]["TypeForm", "Open" -> {"Ruliology.CellularAutomata.Rule30Realization", "Rule30Submission"}], rule30Submission["Rule30Submission.white_end_seed"]["TypeForm", "Open" -> {"Ruliology.CellularAutomata.Rule30Realization", "Rule30Submission"}]}
```

Jen's theorem with a clock, the lemma that finishes the argument:

```wl
rule30Submission["Rule30Submission.theorem_A"]["TypeForm", "Open" -> {"Ruliology.CellularAutomata.Rule30Realization", "Rule30Submission"}]
```

The control: the finite check fails at `q = 9`, so the checks are not vacuous:

```wl
rule30Submission["Rule30Submission.control_q9"]["TypeForm", "Open" -> {"Rule30Submission"}]
```

The proof's structure, one level down from the headline:

```wl
thm["CallGraph", "Depth" -> 1]
```

## What is not proved

- Nothing for `q ≤ 9`. The method does not determine column `c + 1` there (the control above), and `q = 1` is the word `10`, the period-2 case of Problem 1, which stays open.
- Nothing about any other word. The same route excludes further specific words by the same finite checks; that is a separate matter.
- This is a partial result, one infinite family of words removed from Problem 1. It does not touch Problems 2 and 3.

## Provenance

The result is entry 40 of the Wolfram · Collatz · Mahler record, an open research record kept on GitHub by Gareth Herbert with Claude and GPT. Local (Claude) found the route and machine-checked it in Lean on 2026-10-09; Cloud (Claude) and GPT read and replayed it independently with separate implementations; Cloud restated it on the kit's definitions and added the bridge to `EventuallyWord` on 2026-10-22. The finite computations above were reproduced in Python before this essay was written. The mechanism is Jen's, as the kit's strip certificates use it; the kit's `window_jen` is the same clocked form of Jen's theorem, stated with the or-column.

## References

[1] E. Jen, *Global properties of cellular automata*, Journal of Statistical Physics 43 (1986) 219–242.

[2] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[3] Wolfram Institute, [*Rule30PrizeKit*](https://github.com/WolframInstitute/Rule30PrizeKit), the reference Lean environment, commit cc1e0e0, 2026.

[4] The Wolfram · Collatz · Mahler record, [github.com/ghywel/placego](https://github.com/ghywel/placego): PROOFS.md entry 40 and `tests/probes/lean/WhiteEnd.lean`, 2026.
