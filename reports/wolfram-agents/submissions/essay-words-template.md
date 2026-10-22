---
Template: ComputationalEssay
Name: @@TITLE@@
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-23
Description: A partial result for Problem 1 of the Rule 30 Prize, proved in Lean against the official statements: @@COUNT@@ repeating words of length @@LENGTHS@@, none in the kit's certificate table, are excluded as eventual words of the center column, and of every column of every configuration with a leftmost black cell
Abstract: Problem 1 asks whether the center column of rule 30 is ever eventually periodic. The kit's catalog excludes 30 repeating words of length 8 to 13 by strip certificates. This essay excludes @@COUNT@@ further words, of length @@LENGTHS@@, none of them in that table, as the headline theorem Rule30Submission.not_eventuallyWord_words, together with the same statement for every column of every configuration with a leftmost black cell (Rule30Submission.words_general). The argument is Jen's, word by word: the K cells right of the column (K = 8, or 10 for a few words) form a finite relaxation; after a few periods of the word, one more period maps its reachable set into itself while the next column is forced to a single value at every tick, so two adjacent columns are periodic and the moving left edge forbids it. Each word's finite fact is decided by the Lean kernel. The verifier's replay accepts the module with the three standard axioms only. Nothing is claimed for any word not listed, and this is not a solution of Problem 1.
Keywords: [rule 30, Rule 30 Prize, Problem 1, eventually periodic, Jen's theorem, strip certificate, excluded words, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record, PROOFS.md entry 41](https://github.com/ghywel/placego/blob/main/PROOFS.md)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[wolframcollatzmahler.com](https://www.wolframcollatzmahler.com)", "[Submission R30-20261022-c27323, the white end](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261022-c27323)"]
---

## The question

Rule 30 updates every cell from itself and its two neighbors: the new color is *left* XOR (*center* OR *right*). From a single black cell it grows a pattern whose center column looks random. Problem 1 of the Rule 30 Prize asks whether that column is ever eventually periodic: whether, from some time on, it repeats a word forever.

The first 60 steps, with the center column in red:

```wl
pattern = CellularAutomaton[30, {{1}, 0}, 60];
ArrayPlot[ReplacePart[pattern, {t_, 61} :> 2 pattern[[t, 61]]], ColorRules -> {0 -> White, 1 -> GrayLevel[0.15], 2 -> StandardRed}, ImageSize -> 520]
```

A proof of Problem 1 has to rule out every word, from every starting time. The kit's catalog rules out 30 words of length 8 to 13 (`Rule30StripCertificateTable`), the family `0^r 1 1` for `r ≥ 8` (`Rule30WhiteRunEight`), and `1^r u` for eight short blocks `u` and large `r` (`Rule30BlackRunBlocks`). Our previous submission, [R30-20261022-c27323](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261022-c27323), rules out the family `1 0^q` for every `q ≥ 10`. This essay rules out **@@COUNT@@ further words, of length @@LENGTHS@@**, none of them in the kit's table, each by its own kernel-checked certificate on the same mechanism.

## The words

The words, as least rotations (any rotation is the same column word), with the strip width that certifies each:

```wl
words = @@WORDS@@;
Length[words]
```

By length, and by width:

```wl
{Counts[StringLength /@ words[[All, 1]]], Counts[words[[All, 2]]]}
```

Every one has a run of at least six equal cells; the kit's table and these lists overlap in eleven words of length 10 to 13, which are left out here. Nothing is claimed for any word not listed.

## The mechanism: a finite machine to the right of the column

Suppose column `c` reads the word `w` repeatedly from some time on. Watch the `K` cells immediately to its right. Their next values depend on column `c` (known: the word), on themselves, and on one unknown cell beyond them, which is allowed both values at every step. The `K` cells then move through a finite nondeterministic system with `2^K` states, and every actual history of rule 30 is one path of it.

The system, with a state as a number below `2^K` (bit `j` is cell `c + 1 + j`), the column's bit `b` and the outside bit `u`:

```wl
stp[K_, b_, s_, u_] := BitAnd[BitXor[BitAnd[BitOr[BitShiftLeft[s, 1], b], 2^K - 1], BitOr[s, BitShiftRight[s, 1], BitShiftLeft[u, K - 1]]], 2^K - 1];
img[K_, b_, S_] := Union[Flatten[Table[{stp[K, b, s, 0], stp[K, b, s, 1]}, {s, S}]]];
period[K_, w_, S_] := Fold[img[K, #2, #1] &, S, w];
reach[K_, w_, n_] := Nest[period[K, w, #] &, Range[0, 2^K - 1], n];
```

`img` is the image of a set of states under one step, over both values of the outside bit; `period` applies one period of the word; `reach[K, w, n]` is the set of states reachable after `n` periods from every start.

**The certificate for a word.** After `n0` periods, one more period keeps the first cell of the strip, column `c + 1`, constant at every tick and maps the reachable set into itself. Column `c + 1` is then periodic with the word's period: the actual strip lies in the reachable set at every period, the set never grows again, and on it the first cell is forced. The number of states after each period, the warm-up `n0` the certificate uses, and the forced column over one period from the set reached after `n0`, for two of the words (`?` would mark a tick where both values occur; none does):

```wl
forced[K_, w_, S_] := Module[{X = S, out = {}}, Do[AppendTo[out, Union[BitAnd[#, 1] & /@ X] /. {{0} -> "0", {1} -> "1", {0, 1} -> "?"}]; X = img[K, b, X], {b, w}]; StringJoin[out]];
Grid[Prepend[Table[With[{K = e[[2]], n0 = e[[3]], w = ToExpression /@ Characters[e[[1]]]}, {e[[1]], K, n0, Length /@ Table[reach[K, w, n], {n, 1, 4}], forced[K, w, reach[K, w, n0]], SubsetQ[reach[K, w, n0], period[K, w, reach[K, w, n0]]]}], {e, @@EXAMPLES@@}], {"word", "K", "warm-up periods n0", "states after 1..4 periods", "column c+1 over one period, from the set after n0", "maps into itself"}], Frame -> All, Alignment -> Left]
```

**The contradiction: Jen's theorem with a clock.** Columns `c` and `c + 1` are now both periodic with the same period from some time on. Rule 30 is left-permutive, so periodicity of two adjacent columns on a time window propagates to the columns on their left, one step shorter per column; and the leftmost black cell of the configuration moves one cell left per step, with everything left of it white. Far enough to the left, a column is white at one time and black one period later, yet periodicity makes those two values equal. That is `theorem_A` below. If the leftmost black cell starts right of column `c`, the clock is re-based after it has passed.

Everything in this section is a computation or a sketch. The proof is the next section.

## The formal proof

The module, as the verifier rebuilds and checks it. `stp`, `img`, `run`, `reach` are the finite machine for any width `K`; `walk` is one period that returns the final set only if column `c + 1` was constant at every tick; `check K w n0` is the certificate, decided by the kernel for each word; `win` encodes the actual `K` cells and `win_step` proves that the encoding follows rule 30 (`StpOK 8` and `StpOK 10`, decided); `img_mono` and `reach_sub` prove that a set mapped into itself keeps every later set; `theorem_A` and `no_two_periodic` are Jen's theorem with a clock on the kit's `evol`; `core` and `no_word` assemble the contradiction for one word, `words_general` for every listed word, and the bridge lemmas turn the kit's `EventuallyWord` into the module's `ReadsW` through the kit's own `evol_seed`.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["@@LEAN_SOURCE@@", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The headline theorem, as Lean prints it. For every listed word, the center column is not eventually that word:

```wl
opens = {"Ruliology.CellularAutomata.Rule30StripCertificates", "Ruliology.CellularAutomata.Rule30Realization", "Rule30Submission"};
thm = rule30Submission["Rule30Submission.not_eventuallyWord_words"];
thm["TypeForm", "Open" -> opens]
```

Its axioms are the three standard ones and nothing else:

```wl
thm["Axioms"]
```

The listed words are the module's `words`, the same list as above, which the kernel has evaluated:

```wl
LeanEvaluate["(Rule30Submission.words.map fun w => w.map fun b => if b then 1 else 0)", "ProjectDir" -> $Rule30PrizeKit, "Imports" -> {"Rule30Submission"}] === Map[ToExpression /@ Characters[#] &, words[[All, 1]]]
```

The general statement, for every column of every configuration with a leftmost black cell. `ReadsW x0 c ws a` says that column `c` of the evolution of `x0` reads the word `ws` periodically from time `a`:

```wl
rule30Submission["Rule30Submission.words_general"]["TypeForm", "Open" -> opens]
```

The certificate's soundness, in two of its lemmas: from a set that one period maps into itself, every later set stays inside it; and Jen's theorem with a clock:

```wl
{rule30Submission["Rule30Submission.reach_sub"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.theorem_A"]["TypeForm", "Open" -> opens]}
```

The proof's structure, one level down from the headline:

```wl
thm["CallGraph", "Depth" -> 1]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state, after which every fresh display costs a minute:

```wl
thm["KernelCheck"]
```

## What is not proved

- Nothing about any word not listed. In particular no word of period 7 to 9 is determined at width 8 or 10, and the prize's own period-2 word `10` is untouched.
- The listed words are a small share of all words of these lengths: those with a long run, which the strip determines. The method's reach is limited by the strip width; wider strips cost exponentially more kernel time.
- This is a partial result, @@COUNT@@ words removed from Problem 1. It does not touch Problems 2 and 3.

## Provenance

The words are entry 41 of the Wolfram · Collatz · Mahler record, an open research record kept on GitHub by Gareth Herbert with Claude and GPT. Local (Claude) found them by a census on 2026-10-09 and machine-checked them in Lean on 2026-10-10; Cloud (Claude) replayed the census with separate code; Cloud restated the proof on the kit's definitions, replaced the fixed-point test by the subset test with the monotonicity lemma, took each word's minimal warm-up, and added the bridge to `EventuallyWord` on 2026-10-23. The mechanism is Jen's, as the kit's strip certificates use it; the kit's `window_jen` is the same clocked form of Jen's theorem. The previous submission, the white end, used the same module structure for the infinite family `1 0^q`.

## References

[1] E. Jen, *Global properties of cellular automata*, Journal of Statistical Physics 43 (1986) 219–242.

[2] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[3] Wolfram Institute, [*Rule30PrizeKit*](https://github.com/WolframInstitute/Rule30PrizeKit), the reference Lean environment, commit cc1e0e0, 2026.

[4] The Wolfram · Collatz · Mahler record, [github.com/ghywel/placego](https://github.com/ghywel/placego): PROOFS.md entries 40 and 41 and `tests/probes/lean/JenRoute.lean`, 2026.
