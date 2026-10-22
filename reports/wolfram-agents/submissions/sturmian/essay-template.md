---
Template: ComputationalEssay
Name: Every characteristic Sturmian word is excluded as the right neighbour of a period-2 center column
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-23
Description: A partial result for Problem 1 of the Rule 30 Prize in the period-2 case, proved in Lean against the official statements: if column 0 reads the clock 0101… from time 0 and the configuration has a leftmost black cell, then the even-time bits of column 1 are not the characteristic Sturmian word of any slope, nor any finite block code of one; the Fibonacci word is the first example
Abstract: The first open case of Problem 1 is period 2, the clock 0101…. Under the clock, rule 30's left-permutivity determines column -1 from the even-time bits of column 1, the visible bits, and the record's Corollary F (Rule30Submission.corollary_F, filed in the previous submission) says the visible bits of a configuration with a leftmost black cell have no near-squares at unbounded scales. This essay adds the words. For a directive sequence d with every d n ≥ 1, the standard words std d 0 = [1], std d 1 = [0], std d (n+2) = (std d (n+1))^(d n) ++ std d n are each a prefix of the next, and their limit cw d is the characteristic Sturmian word of slope [0; d 0 + 1, d 1, d 2, …]. Two list inductions give the classical near-commutation, std (n+1) ++ std n and std n ++ std (n+1) agree except in their last two letters (Rule30Submission.std_near_comm), and hence a near-square with slack 2 at the pair (0, |std d (n+1)|) for every n (cw_near_square). Therefore no configuration with a leftmost black cell and the clock on column 0 has a characteristic Sturmian word, or its letter exchange, as its visible bits (characteristic_excluded, characteristic_excluded_compl; fibonacci_excluded for d = 1, 1, 1, …); and since a near-square survives every sliding block code with its slack raised by the window (image_near_square), neither does any finite block code of a characteristic word (characteristic_block_excluded). The record's Theorem E excludes every Sturmian word of every intercept by a Diophantine argument; the characteristic case is what word combinatorics gives alone, and the general intercept is not formalized here. The verifier's replay accepts the module with the three standard axioms only. Nothing here decides Problem 1.
Keywords: [rule 30, Rule 30 Prize, Problem 1, period 2, Sturmian words, standard words, Fibonacci word, near-squares, Corollary F, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record, PROOFS.md entries 11 and 14](https://github.com/ghywel/placego/blob/main/PROOFS.md)", "[M. Lothaire, Algebraic Combinatorics on Words, Chapter 2](https://www.cambridge.org/core/books/algebraic-combinatorics-on-words/)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[wolframcollatzmahler.com](https://www.wolframcollatzmahler.com)", "[Submission R30-20261022-91b0b0, Corollary F](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261022-91b0b0)"]
---

## The question

Rule 30 updates every cell from itself and its two neighbors: the new color is *left* XOR (*center* OR *right*). From a single black cell it grows a pattern whose center column looks random. Problem 1 of the Rule 30 Prize asks whether that column is ever eventually periodic; the shortest case is period 2, the clock `0101…`, the kit's open `Rule30ZeroBoundary.Q01` for the single seed.

The first 60 steps, with the center column in red:

```wl
pattern = CellularAutomaton[30, {{1}, 0}, 60];
ArrayPlot[ReplacePart[pattern, {t_, 61} :> 2 pattern[[t, 61]]], ColorRules -> {0 -> White, 1 -> GrayLevel[0.15], 2 -> StandardRed}, ImageSize -> 520]
```

Under the clock, rule 30's left-permutivity makes column `-1` black at odd times and the complement of column `1` at even times, so column `1`'s even-time bits, the *visible bits*, carry everything the clock allows. The previous submission proved **Corollary F**: for a configuration with a leftmost black cell and the clock on column 0, the visible bits have no *near-squares at unbounded scales*, no fixed slack `K` and pairs `i < i′` with `i′ - i` unbounded whose common future `c(i + s) = c(i′ + s)` lasts `s < i′ - K`. This essay asks which natural aperiodic sequences that excludes, and answers for the whole family of characteristic Sturmian words: all of them.

## Standard words and the characteristic words

A directive sequence `d` with every `d n ≥ 1` builds the standard words `std 0 = [1]`, `std 1 = [0]`, `std (n+2) = (std (n+1))^(d n) ++ std n`. Each is a prefix of the next, and the limit is the characteristic Sturmian word of slope `[0; d 0 + 1, d 1, d 2, …]`; exchanging the letters gives the slopes above `1/2`. With `d = 1, 1, 1, …` the lengths are the Fibonacci numbers and the limit is the Fibonacci word:

```wl
std[d_, 0] := {1}; std[d_, 1] := {0};
std[d_, n_] := std[d, n] = Join[Flatten[ConstantArray[std[d, n - 1], d[[n - 1]]]], std[d, n - 2]];
fib = ConstantArray[1, 20];
{Table[StringJoin[ToString /@ std[fib, n]], {n, 0, 6}], Table[Length[std[fib, n]], {n, 0, 12}], StringJoin[ToString /@ Take[std[fib, 14], 55]]}
```

**Near-commutation.** `std (n+1) ++ std n` and `std n ++ std (n+1)` agree except in their last two letters (Lothaire, Chapter 2). Checked here for `n = 0 … 10` on the Fibonacci sequence and on the directive sequence `2, 1, 3, 1, 2, 1, 3, 1, …`:

```wl
d2 = Flatten[ConstantArray[{2, 1, 3, 1}, 5]];
nearComm[d_] := AllTrue[Range[0, 10], Most[Most[Join[std[d, # + 1], std[d, #]]]] == Most[Most[Join[std[d, #], std[d, # + 1]]]] && Take[Join[std[d, # + 1], std[d, #]], -2] != Take[Join[std[d, #], std[d, # + 1]], -2] &];
{nearComm[fib], nearComm[d2]}
```

**The near-square at the start.** Because `std (n+2) ++ std (n+1)` is a prefix of the word and begins either with two copies of `std (n+1)` or with `std (n+1) ++ std n ++ std (n+1)`, the word agrees with its shift by `|std (n+1)|` on at least `|std (n+1)| - 2` positions: a near-square at the pair `(0, |std (n+1)|)` with slack at most 2, at every scale. The actual common futures, for both sequences (`n`, the length, the common future, the slack; the slack is never above 2 and is usually negative):

```wl
table[d_] := Module[{c = std[d, 14]}, Table[With[{L = Length[std[d, n]]}, With[{l = LengthWhile[Range[0, Length[c] - L - 1], c[[# + 1]] == c[[L + # + 1]] &]}, {n, L, l, L - l}]], {n, 1, 8}]];
{table[fib], table[d2]}
```

## The forced left half of the Fibonacci word

Take the clock as column 0 and the Fibonacci word as the visible bits, and compute the forced left half, column by column, by left-permutivity. Corollary F says the row at time 0 has no leftmost black cell. Its black cells by depth, from 3,000 steps of the clock:

```wl
fibw = std[fib, 20];
steps = 3000;
col0 = Table[Mod[t, 2], {t, 0, steps - 1}];
col1 = Table[If[EvenQ[t], fibw[[t/2 + 1]], 0], {t, 0, steps - 1}];
colm1 = Table[BitXor[col0[[t + 2]], BitOr[col0[[t + 1]], col1[[t + 1]]]], {t, 0, steps - 2}];
row0 = Module[{a = colm1, b = col0, out = {col0[[1]], colm1[[1]]}}, Do[{a, b} = {Table[BitXor[a[[t + 1]], BitOr[a[[t]], b[[t]]]], {t, 1, Length[a] - 1}], a}; AppendTo[out, a[[1]]], {m, 2, steps - 2}]; out];
blacks = Flatten[Position[row0, 1]] - 1;
{Length[row0], Take[blacks, 30], Length[blacks], Last[blacks], Max[Differences[blacks]]}
```

## The idea of the proof

**Near-commutation**, by induction on `n`: `std (n+2) ++ std (n+1) = w ++ (std n ++ std (n+1))` and `std (n+1) ++ std (n+2) = w ++ (std (n+1) ++ std n)` with the same `w = (std (n+1))^(d n)`, because `u ++ u^a = u^a ++ u`; the two tails agree except in their last two letters by the induction hypothesis.

**The near-square.** Write `A = std (n+1)`, `B = std n`. If `d n ≥ 2`, the word begins `A ++ A ++ …`, so the shift by `|A|` agrees on all of `A`. If `d n = 1`, the word begins `A ++ B ++ W` with `A` a prefix of `W`; the shift by `|A|` reads `B ++ W`, which agrees with `B ++ A` on `|B| + |A|` positions, which agrees with `A ++ B` on all but the last two, which agrees with `A` on `|A|`.

**The exclusion.** The pairs `(0, |std (n+1)|)` have slack 2 and lengths at least `n + 1`, so Corollary F applies with `K = 2`. Its hypothesis `L ≥ 1` is automatic: the clock is white at time 0, so column 0 is not the leftmost black cell.

**Block codes.** A sliding block code of window `r` reads `f(c(i), …, c(i + r - 1))`. Where `c` agrees with its shift on `s < i′ - K`, the image agrees on `s < i′ - K - r`: the near-squares survive with slack `K + r`, and Corollary F applies again. The letter exchange is the window-1 code `NOT`.

Everything in this section is prose. The proofs are the next section.

## The formal proof

The module, as the verifier rebuilds and checks it: the record's Lemma B2 and Theorem A‴ on the kit's `evol` (`edge`, `D`, `jen_pow2`, `lemma_B2_quant`, `infinitely_many_black`; `step_inv`, `agree`, `theorem_A3`), Corollary F (`col_m1`, `blocks_of_visible`, `corollary_F`), and the words (`wpow`, `std`, `std_prefix`, `cw`, `cw_eq`, `Agree`, `std_near_comm`, `cw_near_square`) with the headlines `characteristic_excluded`, `characteristic_excluded_compl`, `fibonacci_excluded`, and the block codes (`image`, `image_near_square`, `characteristic_block_excluded`).

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["@@LEAN_SOURCE@@", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The headline theorem, as Lean prints it. `evol x0 t p` is the kit's evolution; the hypotheses are a leftmost black cell at `-L`, the clock on column 0 from time 0, and the visible bits equal to `cw d`, the characteristic word of the directive sequence `d` with every `d n ≥ 1`:

```wl
opens = {"Ruliology.CellularAutomata.Rule30Realization", "Rule30Submission"};
thm = rule30Submission["Rule30Submission.characteristic_excluded"];
thm["TypeForm", "Open" -> opens]
```

Every sliding block code of a characteristic word (`image f r c i = f [c i, …, c (i + r - 1)]`), the letter exchange, and the Fibonacci word:

```wl
{rule30Submission["Rule30Submission.characteristic_block_excluded"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.characteristic_excluded_compl"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.fibonacci_excluded"]["TypeForm", "Open" -> opens]}
```

The two word lemmas, near-commutation and the near-square, and the standard words themselves:

```wl
{rule30Submission["Rule30Submission.std_near_comm"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.cw_near_square"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.std"]["TypeForm", "Open" -> opens]}
```

Corollary F, the theorem the words feed:

```wl
rule30Submission["Rule30Submission.corollary_F"]["TypeForm", "Open" -> opens]
```

The axioms of the headline are the three standard ones and nothing else:

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

- Nothing about the single seed directly: its center column is not known to be eventually a clock.
- The clock is assumed from time 0. A clock from a later time `T0` needs the pairs shifted into it, at the cost of a larger slack, as the Corollary F essay remarks; the module states the time-0 form.
- Only the characteristic words, their letter exchanges and their finite block codes: one intercept per slope. Theorem E of the record covers every intercept by a Diophantine argument that is not formalized here; its block-code extension is the record's G131 (GPT).
- The identification of `cw d` with the rotation coding of slope `[0; d 0 + 1, d 1, …]` is classical and is not part of the module; the module's statement is about the words `std d n` themselves.

## Provenance

Corollary F and Theorem E are RULE30-PRIZE.md sections 8.59 and 8.57, PROOFS.md entries 11 and 14, of the Wolfram · Collatz · Mahler record, an open research record kept on GitHub by Gareth Herbert with Claude and GPT: proved by hand by Local (Claude) on 2026-10-05. The near-commutation of standard words is classical (Lothaire); that Theorem E's exclusion survives finite block codes is the record's G131 (GPT, second-read by Local). Cloud (Claude) formalized Corollary F and this corollary on the kit's definitions on 2026-10-23, from Local's Lean for Lemma B2 and Theorem A‴ (2026-10-10). The companion submissions file the white end, the excluded words, the diagonal lemmas, Theorem A⁗ and Corollary F.

## References

[1] E. Jen, *Global properties of cellular automata*, Journal of Statistical Physics 43 (1986) 219–242.

[2] M. Lothaire, *Algebraic Combinatorics on Words*, Cambridge University Press, 2002, Chapter 2 (Sturmian words).

[3] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[4] Wolfram Institute, [*Rule30PrizeKit*](https://github.com/WolframInstitute/Rule30PrizeKit), the reference Lean environment, commit cc1e0e0, 2026.

[5] The Wolfram · Collatz · Mahler record, [github.com/ghywel/placego](https://github.com/ghywel/placego): PROOFS.md entries 11 and 14, 2026.
