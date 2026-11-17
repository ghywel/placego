---
Template: ComputationalEssay
Name: Every Sturmian word, of every slope and every intercept, is excluded as the right neighbour of a period-2 center column
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-23
Description: A partial result for Problem 1 of the Rule 30 Prize in the period-2 case, proved in Lean against the official statements: if column 0 reads the clock 0101… from some time on and the configuration has a leftmost black cell, then the even-time bits of column 1 are not a mechanical word of any irrational slope and any intercept, nor any finite block code of one; the proof is a pigeonhole on the n + 1 blocks of length n, with no continued fractions
Abstract: The first open case of Problem 1 is period 2, the clock 0101…. Under the clock, rule 30's left-permutivity determines column -1 from the even-time bits of column 1, the visible bits, and the record's Corollary F (Rule30Submission.corollary_F, submission 5) says the visible bits of a configuration with a leftmost black cell have no near-squares at unbounded scales, no fixed slack K and pairs i < i′ with i′ - i unbounded whose common future lasts i′ - K. This essay proves that every mechanical word, mech α θ i = ⌊θ + (i+1)α⌋ - ⌊θ + iα⌋ with irrational slope 0 < α < 1 and any intercept θ (equivalently, 1 iff the fractional part of θ + iα lies in [1 - α, 1)), has such near-squares with slack 1: a Sturmian word has at most n + 1 distinct blocks of length n, so two of the n + 2 blocks starting at positions 0 to n + 1 coincide (Rule30Submission.exists_block_collision), their common future is at least n, and the gap between them must grow, because a block of length n repeating at a gap q ≤ H would make the count of ones in kq consecutive letters equal kp while the floor formula keeps it within 1 of kqα, impossible for k > 1 / min |p - qα| (no_small_period). Hence no configuration with a leftmost black cell and the clock on column 0 has a Sturmian word of any slope and intercept as its visible bits (sturmian_excluded, sturmian_excluded_clock0, sturmian_excluded_fract), nor any finite block code of one (sturmian_block_excluded). This is the record's Theorem E in full, by a combinatorial route found by GPT after the characteristic case had been filed; the pigeonhole is Bugeaud and Kim's early-repetition lemma. The verifier's replay accepts the module with the three standard axioms only. Nothing here decides Problem 1.
Keywords: [rule 30, Rule 30 Prize, Problem 1, period 2, Sturmian words, mechanical words, factor complexity, near-squares, Corollary F, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record, PROOFS.md entries 11 and 14](https://github.com/ghywel/placego/blob/main/PROOFS.md)", "[Y. Bugeaud and D. H. Kim, A new complexity function, repetitions in Sturmian words, and irrationality exponents of Sturmian numbers](https://irma.math.unistra.fr/~bugeaud/travaux/complsturm3ndRev1.pdf)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[wolframcollatzmahler.com](https://www.wolframcollatzmahler.com)", "[Submission R30-20261022-91b0b0, Corollary F](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261022-91b0b0)", "[Submission R30-20261023-e872a3, the characteristic case](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261023-e872a3)"]
---

## The question

Rule 30 updates every cell from itself and its two neighbors: the new color is *left* XOR (*center* OR *right*). From a single black cell it grows a pattern whose center column looks random. Problem 1 of the Rule 30 Prize asks whether that column is ever eventually periodic; the shortest case is period 2, the clock `0101…`, the kit's open `Rule30ZeroBoundary.Q01` for the single seed.

The first 60 steps, with the center column in red:

```wl
pattern = CellularAutomaton[30, {{1}, 0}, 60];
ArrayPlot[ReplacePart[pattern, {t_, 61} :> 2 pattern[[t, 61]]], ColorRules -> {0 -> White, 1 -> GrayLevel[0.15], 2 -> StandardRed}, ImageSize -> 520]
```

Under the clock, rule 30's left-permutivity makes column `-1` black at odd times and the complement of column `1` at even times, so column `1`'s even-time bits, the *visible bits*, carry everything the clock allows. Our submission 5 proved **Corollary F**: for a configuration with a leftmost black cell and the clock on column 0, the visible bits have no *near-squares at unbounded scales*, no fixed slack `K` and pairs `i < i′` with `i′ - i` unbounded whose common future `c(i + s) = c(i′ + s)` lasts `s < i′ - K`. Submission 7 excluded the characteristic Sturmian words, one intercept per slope, by their standard words. This essay excludes **every** Sturmian word, every irrational slope and every intercept, and every finite block code of one, by an argument that needs no continued fractions at all.

## Mechanical words and their blocks

The mechanical word of slope `α` and intercept `θ` is `c(i) = ⌊θ + (i + 1)α⌋ - ⌊θ + iα⌋`, which is `1` exactly when the fractional part of `θ + iα` lies in `[1 - α, 1)`. For irrational `α` these are the Sturmian words. The golden slope with intercept `1/2`, and the count of distinct blocks of each length `n`, which is `n + 1` (the Sturmian signature; the module proves only the inequality `≤ n + 1`, which is all the argument needs):

```wl
mech[alpha_, theta_, n_] := Table[Floor[theta + (i + 1) alpha] - Floor[theta + i alpha], {i, 0, n - 1}];
golden = (Sqrt[5] - 1)/2;
c = mech[golden, 1/2, 60000];
{StringJoin[ToString /@ Take[c, 40]], Table[Length[Union[Table[c[[s + 1 ;; s + n]], {s, 0, 49999}]]], {n, 1, 12}]}
```

**The pigeonhole.** Among the `n + 2` blocks of length `n` starting at positions `0, 1, …, n + 1`, two must coincide, at positions `i < j ≤ n + 1`. Their common future is then at least `n ≥ j - 1`: a near-square at the pair `(i, j)` with slack at most 1. The collisions for three slopes and intercepts, with the actual common future and the slack `j - (common future)`, which is never above 1:

```wl
collide[c_, n_] := Module[{seen = <||>, f}, Do[f = c[[s + 1 ;; s + n]]; If[KeyExistsQ[seen, f], Return[{seen[f], s}, Module], seen[f] = s], {s, 0, n + 1}]];
table[alpha_, theta_] := Module[{w = mech[alpha, theta, 20000]}, Table[With[{r = collide[w, n]}, With[{i = r[[1]], j = r[[2]]}, With[{l = LengthWhile[Range[0, Length[w] - j - 1], w[[i + # + 1]] == w[[j + # + 1]] &]}, {n, i, j, j - i, l, j - l}]]], {n, {5, 10, 20, 50, 100, 200, 500, 1000, 2000}}]];
Grid[Prepend[Join[table[golden, 1/2], table[Sqrt[2] - 1, 1/10]], {"n", "i", "j", "gap", "common future", "slack"}], Frame -> All]
```

**The gap grows.** Why can the two coinciding blocks not sit at a bounded distance `q`? If a block of length `n` repeats at gap `q`, the word has period `q` on `n` letters, so its first `kq` letters, `k = ⌊n/q⌋`, are `k` copies of one `q`-letter block with `p` ones, `kp` ones in all. But the ones in any `m` consecutive letters are `⌊θ + (i + m)α⌋ - ⌊θ + iα⌋`, within 1 of `mα`. So `k |p - qα| < 1`. For an irrational slope, `|p - qα|` has a positive minimum `d_H` over `1 ≤ q ≤ H`, and once `n > H(1 + 1/d_H)` every `q ≤ H` gives `k > 1/d_H`: a contradiction. Hence the collisions of the pigeonhole have gaps beyond every bound, and Corollary F applies with `K = 1`.

## The forced left half of a non-characteristic word

Take the clock as column 0 and the golden word with intercept `1/2` as the visible bits, and compute the forced left half by left-permutivity. The theorem says its row at time 0 has no leftmost black cell; its black cells by depth, from 3,000 steps:

```wl
w = mech[golden, 1/2, 2000];
steps = 3000;
col0 = Table[Mod[t, 2], {t, 0, steps - 1}];
col1 = Table[If[EvenQ[t], w[[t/2 + 1]], 0], {t, 0, steps - 1}];
colm1 = Table[BitXor[col0[[t + 2]], BitOr[col0[[t + 1]], col1[[t + 1]]]], {t, 0, steps - 2}];
row0 = Module[{a = colm1, b = col0, out = {col0[[1]], colm1[[1]]}}, Do[{a, b} = {Table[BitXor[a[[t + 1]], BitOr[a[[t]], b[[t]]]], {t, 1, Length[a] - 1}], a}; AppendTo[out, a[[1]]], {m, 2, steps - 2}]; out];
blacks = Flatten[Position[row0, 1]] - 1;
{Length[row0], Take[blacks, 30], Length[blacks], Last[blacks], Max[Differences[blacks]]}
```

About half the depths are black and the largest spacing between consecutive black depths is 14 cells.

## The idea of the proof

**The block at `i` is a function of `x = fract(θ + iα)` through `n` thresholds.** Write `⌊θ + (i + k)α⌋ = ⌊θ + iα⌋ + ⌊x + kα⌋` and `⌊x + kα⌋ = ⌊kα⌋ + [x + fract(kα) ≥ 1]`. So the block of length `n` at `i` is determined by the set `S(x)` of `k ≤ n` with `1 ≤ x + fract(kα)`. That set grows with `x`, never contains `k = 0`, so has at most `n` elements; the `n + 2` positions `0 … n + 1` give at most `n + 1` cardinalities, two positions share one, and nested sets of equal size are equal. That is `block_eq_of_thr` and `exists_block_collision`.

**No long block of a bounded period** is the telescoping argument above: `sum_mechZ` (the ones are a difference of floors), `sum_periodic` (periodicity makes them `k` times one block), `exists_gap` (the positive minimum, from irrationality) and `no_small_period`.

**The exclusion.** For every `N`, a pair `i < j` with gap at least `N`, `j ≤ n + 1` and equal blocks of length `n` is a near-square with slack 1 (`sturmian_pairs`); Corollary F finishes it. A clock that starts at time `T0` is handled by the shifted intercept `θ + T0 α`, whose word is the suffix of the original (`mech_shift_intercept`), at slack `T0 + 1`. A sliding block code of window `r` keeps a near-square with slack raised by `r` (`image_near_square`).

Everything in this section is prose. The proofs are the next section.

## The formal proof

The module, as the verifier rebuilds and checks it: the record's Lemma B2 and Theorem A‴ on the kit's `evol`, Corollary F (`col_m1`, `blocks_of_visible`, `corollary_F`), block codes (`image`, `image_near_square`), the mechanical words (`mechZ`, `mech`, `mech_eq_fract`, `floor_decomp`, `floor_shift`, `thr`, `block_eq_of_thr`, `exists_block_collision`, `exists_gap`, `sum_mechZ`, `mech_shift`, `sum_periodic`, `no_small_period`, `sturmian_pairs`, `mech_shift_intercept`) and the headlines.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["@@LEAN_SOURCE@@", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The headline theorem, as Lean prints it. `evol x0 t p` is the kit's evolution; the hypotheses are an irrational slope in `[0, 1)`, a leftmost black cell at `-L` with `L ≥ 1`, the clock on column 0 from time `T0`, and the visible bits equal to the mechanical word `mech α θ`:

```wl
opens = {"Ruliology.CellularAutomata.Rule30Realization", "Rule30Submission"};
thm = rule30Submission["Rule30Submission.sturmian_excluded"];
thm["TypeForm", "Open" -> opens]
```

The clock from time 0 (where `L ≥ 1` is automatic), the record's fractional-part form of the word, and every sliding block code:

```wl
{rule30Submission["Rule30Submission.sturmian_excluded_clock0"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.sturmian_excluded_fract"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.sturmian_block_excluded"]["TypeForm", "Open" -> opens]}
```

The three word lemmas, the pigeonhole, the bounded-period exclusion and the near-squares they give, and the word itself:

```wl
{rule30Submission["Rule30Submission.exists_block_collision"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.no_small_period"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.sturmian_pairs"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.mech"]["TypeForm", "Open" -> opens]}
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
- The slope is taken in `[0, 1)` and irrational, and the word is the lower mechanical word; the upper mechanical words (the other half-open convention) are the complements of lower ones of slope `1 - α`, hence covered by the block-code theorem with the window-1 code `NOT`, but that reduction is not stated in the module.
- The module proves only `p(n) ≤ n + 1`, not the equality; the equality is shown by computation above.
- Rational slopes give periodic words, which Jen's theorem excludes separately; they are outside this module.

## Provenance

Theorem E is RULE30-PRIZE.md section 8.57 and PROOFS.md entry 14 of the Wolfram · Collatz · Mahler record, an open research record kept on GitHub by Gareth Herbert with Claude and GPT: proved by Local (Claude) on 2026-10-05 by a Diophantine argument through the convergents of `α`. Corollary F (PROOFS 11) is Local's, formalized by Cloud (Claude) on 2026-10-23. The combinatorial route from Corollary F to every intercept is GPT's (ledger entry GC1694, 2026-10-23), found after Cloud had measured near-squares only at convergent periods and concluded, wrongly, that no such route existed; the pigeonhole is Bugeaud and Kim's Lemma 2.2. Cloud formalized the route on the kit's definitions the same day; GPT second-read the formal statements. The companion submissions file the white end, the excluded words, the diagonal lemmas, Theorem A⁗, Corollary F, the rule 210 barrier and the characteristic case.

## References

[1] E. Jen, *Global properties of cellular automata*, Journal of Statistical Physics 43 (1986) 219–242.

[2] Y. Bugeaud and D. H. Kim, *A new complexity function, repetitions in Sturmian words, and irrationality exponents of Sturmian numbers*, Transactions of the American Mathematical Society 371 (2019) 3281–3308.

[3] M. Lothaire, *Algebraic Combinatorics on Words*, Cambridge University Press, 2002, Chapter 2 (Sturmian words).

[4] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[5] Wolfram Institute, [*Rule30PrizeKit*](https://github.com/WolframInstitute/Rule30PrizeKit), the reference Lean environment, commit cc1e0e0, 2026.

[6] The Wolfram · Collatz · Mahler record, [github.com/ghywel/placego](https://github.com/ghywel/placego): PROOFS.md entries 11 and 14, CHAT-LEDGER.md GC1694, 2026.
