---
Template: ComputationalEssay
Name: Telling left edges apart from the center column: exact deadlines for three edge pairs
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-24
Description: A partial result on the trace-edge conjecture of the Rule 30 Prize kit, proved in Lean against the official definitions: two configurations of rule 30 whose leftmost black cells sit at -2 and -1 have center columns that differ by time 8; at -4 and -3 by time 13; at -3 and -2 by time 14; each bound is attained. The right side is unrestricted.
Abstract: For any two configurations x, y of rule 30 whose leftmost black cells sit at -2 and -1, the center columns differ at some time t <= 8 (sep_8); for leftmost black cells at -4 and -3 by time 13 (sep_13), at -3 and -2 by time 14 (sep_14); each bound is attained (attained_8, attained_13, attained_14). The right side is unrestricted, finite or infinite. The kit's later module Rule30TraceEdge names the conjecture that two finite configurations with the same complete center trace have the same left edge and proves that it implies Problem 1; these are three exact negative-edge cases of the conjecture, for every configuration with those edges. The center through time m depends on the initial cells at positions at most m only, so a configuration is cut to the window [a, m]; the 2^(m - a) fillings with a black cell at a run as lanes of one number, the signatures of each edge class are collected into a bitset, and the bitsets are disjoint, checked by the kernel in blocks of 256 values. Nothing is claimed about the general conjecture or Problem 1.
Keywords: [rule 30, Rule 30 Prize, Problem 1, left edge, center trace, light cone, lanes, kernel certificate, Lean 4, LeanLink]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[wolframcollatzmahler.com](https://www.wolframcollatzmahler.com)", "[Rule30TraceEdge in the kit](https://github.com/WolframInstitute/Rule30PrizeKit/blob/main/lean/Ruliology/CellularAutomata/Rule30TraceEdge.lean)"]
---

## The question

Run rule 30 from any configuration with a leftmost black cell. The edge moves left one cell per step, and the center column records what it sees. Does the center column know where the edge was? The kit's module `Rule30TraceEdge` (added after the verifier's pinned commit) states the conjecture `EdgeObservable`: two finite configurations with the same complete center trace have the same left edge; and it proves that the conjecture implies Problem 1 in full. Nobody has proved the conjecture. Here are three exact negative-edge cases of it: for leftmost black cells at `-2` and `-1` the center columns differ by time `8`; at `-4` and `-3` by time `13`; at `-3` and `-2` by time `14`; and each deadline is attained. The theorems hold for every configuration with those edges, finite or not, which is more than the conjecture asks on these instances.

## Three pairs that agree as long as possible

The attaining pairs. Each line is a configuration written from its leftmost black cell; the center columns agree for exactly the stated number of steps and then differ:

```wl
run[cells_, lo_, T_] := Module[{w = cells, l = lo, out = {}}, Do[AppendTo[out, If[1 <= 1 - l <= Length[w], w[[1 - l]], 0]]; w = With[{z = Join[{0, 0}, w, {0, 0}]}, Table[BitXor[z[[i - 1]], BitOr[z[[i]], z[[i + 1]]]], {i, 2, Length[z] - 1}]]; l = l - 1, {T}]; out];
pairs = {{-2, {1, 0, 0, 1, 1, 0, 1, 0, 0}, -1, {1, 0, 0, 1, 0, 0, 0, 1}, 8}, {-4, {1, 1, 1, 0, 1, 1, 0, 1}, -3, {1, 1, 0, 1, 0, 0, 1, 0, 0, 1}, 13}, {-3, {1, 0, 0, 0, 1}, -2, {1, 1, 0, 0, 0, 0, 1}, 14}};
Table[With[{ta = run[p[[2]], p[[1]], p[[5]] + 1], tb = run[p[[4]], p[[3]], p[[5]] + 1]}, {p[[1]], p[[3]], ta, tb, First[Position[MapThread[UnsameQ, {ta, tb}], True]][[1]] - 1}], {p, pairs}]
```

So the pair with edges `-2` and `-1` agrees at times `0` to `7` and differs at `8`, and likewise `13` and `14` for the other two pairs.

## Why a finite search settles an infinite question

The center cell at time `t` depends only on the initial cells at positions `-t` to `t`. So if two configurations with edges `a` and `b` agree on the center through time `m`, cutting both at any position `R >= m` preserves that agreement. Conversely, if an exhaustive search over the window `[a, R]` finds that no pair of edges `a`, `b` agrees through time `m`, and `R >= m`, then no pair at all does: a longer-agreeing pair would cut down to one in the window. The search is run as lanes, every filling of the window as one bit of a big integer:

```wl
pat[n_, s_] := FromDigits[Table[BitGet[l, s], {l, 2^n - 1, 0, -1}], 2];
laneWords[a_, R_, m_] := With[{n = R - a}, Table[Which[p < a || p > R, 0, p == a, 2^2^n - 1, True, pat[n, p - a - 1]], {p, -m, m}]];
stepLanes[w_] := With[{z = Join[{0}, w, {0}]}, Table[BitXor[z[[i - 1]], BitOr[z[[i]], z[[i + 1]]]], {i, 2, Length[z] - 1}]];
centers[a_, R_, m_] := Module[{w = laneWords[a, R, m], c = {}}, Do[AppendTo[c, w[[m + 1]]]; w = stepLanes[w], {m + 1}]; c];
sigs[c_, n_] := Union[Table[Table[BitGet[c[[t]], l], {t, Length[c]}], {l, 0, 2^n - 1}]];
longest[a_, b_, R_, m_] := Module[{sa = sigs[centers[a, R, m], R - a], sb = sigs[centers[b, R, m], R - b], k = m + 1}, While[k > 0 && Intersection[Take[#, k] & /@ sa, Take[#, k] & /@ sb] === {}, k--]; k];
{Table[longest[-2, -1, R, 10], {R, {6, 8, 10}}], longest[-4, -3, 13, 13], longest[-3, -2, 14, 14]}
```

The longest agreement for edges `-2`, `-1` is `8` whether the window ends at `6`, `8` or `10`: the maximum has saturated, and since `10 >= 8` it is the maximum over every configuration. For edges `-4`, `-3` the window `[a, 13]` gives `13`, and for `-3`, `-2` the window `[a, 14]` gives `14`; both windows reach their own answer, so both are exact.

## The idea of the proof

1. **Locality.** The kit's `evol_local_le`: two configurations that agree on every position `<= b` have the same evolution at `(t, p)` whenever `p + t <= b`. A configuration with its edge at `a` agrees with its own window `[a, m]` filling on every position `<= m` (white left of the edge, equal inside), so its center through time `m` is the window's (`center_eq_lane`).
2. **Lanes.** The window fillings are the numbers `2 l + 1`, `l < 2^(m - a)`: the edge cell black, the free bits the bits of `l`. The lane words `initWords` hold, at each position, the bits of every filling at once; one step of rule 30 on all lanes is `l XOR (c OR r)` on the words (`stepW`, `stepL`), and the invariant `laneInv` says bit `l` of the word at position `p` after `t` steps is the evolution of filling `l` (`laneInv_step`, `centers_spec`).
3. **Signatures.** The signature of a configuration is its center cells at times `0` to `m` as the bits of a number (`sig`). For each value `v`, `memb` ANDs the center words or their complements and is nonzero exactly when some lane has signature `v`; `sigSet` collects the values into a bitset. `memb_block` puts the signature of every configuration with edge `a` into the bitset of its class.
4. **Disjointness, in blocks.** The two classes' bitsets share no bit. The kernel checks this in blocks of `256` values (`partSet`, `BlocksDisjoint`), one theorem per block, because the Lean kernel keeps every intermediate word in a cache that lives for one declaration: a single loop over all the signature values exhausted memory. `separationB` turns the block facts into the theorem.
5. **Attainment.** `witCheck` has the kernel compare two named lanes at every time, and `attained` turns a passing check into two explicit configurations with the given edges that agree before `m` and differ at `m`.

## The formal proof

The module, built against the kit at the verifier's commit:

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["@@LEAN_SOURCE@@", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The three headlines, as Lean prints them, with the edge predicate as defined:

```wl
opens = {"Ruliology.CellularAutomata.Rule30Realization", "Rule30Submission"};
thm = rule30Submission["Rule30Submission.sep_8"];
{thm["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.sep_13"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.sep_14"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.HasLeftEdge"]["TypeForm", "Open" -> opens]}
```

The attained bounds, and the pillars: separation from block-wise disjointness, the lane invariant at the center, and one block's theorem as stated:

```wl
{rule30Submission["Rule30Submission.attained_8"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.separationB"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.centers_spec"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.d14_0"]["TypeForm", "Open" -> opens]}
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

- Nothing about the conjecture `EdgeObservable` in general, about any other pair of edges, or about Problem 1. The three deadlines, `8`, `14`, `13` for edge depths `2`, `3`, `4`, are not monotone, and three values support no law.
- The theorems are about the center column from time `0`; the kit's implication from `EdgeObservable` to Problem 1 applies the conjecture to two times of one orbit, which is Problem 1 itself, and these instances do not touch it.
- The bitsets are computed by the kernel, not supplied as data; the search in the Wolfram Language above is an illustration, and the theorems do not depend on it.

## Provenance

The question came from the kit's `Rule30TraceEdge` (Troy Lowry with OpenAI Codex, 2026-10-24). GPT (OpenAI) proposed the finite search over positioned rows, found the standard common-right-half lemma and corrected the first reading of the data; Claude (Anthropic) ran the searches, found the saturation argument, and wrote the module; GPT read the argument and the retained results before the module was written. The record is at github.com/ghywel/placego, reports/wolfram-agents/submissions/edge-sep.

## References

[1] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[2] Wolfram Institute, [*The Rule 30 Prize kit*](https://github.com/WolframInstitute/Rule30PrizeKit), 2026: `Rule30ZeroBoundaryBarriers.evol_local_le`, `Rule30ZeroBoundaryLanes.pat`, `Rule30TraceEdge.EdgeObservable`.
