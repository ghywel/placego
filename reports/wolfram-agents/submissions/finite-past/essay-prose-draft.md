---
Template: ComputationalEssay
Name: Finite ancestors of Rule 30 rows: roots, boundary tests and exact counts
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-30
Description: A formal interface for known finite-ancestry structure, with exact physical boundaries and all-width counting
Keywords: [rule 30, finite configurations, predecessors, roots, counting, Lean, partial result]
Sources: ["[Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[Karttunen, OEIS A269160](https://oeis.org/A269160)", "[Karttunen, OEIS A269162](https://oeis.org/A269162)", "[Karttunen, OEIS A269165](https://oeis.org/A269165)", "[Karttunen, OEIS A269166](https://oeis.org/A269166)", "[Research record, G121](https://github.com/ghywel/placego/blob/main/proofs/G121-finite-predecessor-descent-reduces-to-roots.md)"]
---

**Preparation draft.** The mathematical finite-core argument has an earlier independent hand read; its current Lean transcription and these notebook cells are unvalidated. This file is not a submission artifact. The abstract is in `abstract-draft.txt`. A later assembly must insert that exact text into the metadata and replace the source marker with the full validated UTF-8 module. No output below is presented as an executed result.

## The question: how much finite past does a finite row have?

Rule 30 updates a row by F(x)(i) = x(i-1) XOR (x(i) OR x(i+1)). A row is finite when only finitely many cells are black. We exclude the all-white row, which is fixed. If the first and last black cells are L and R, its width is R-L+1, including all white gaps between them.

The next row has extreme black cells L-1 and R+1. Thus a finite predecessor, if it exists, is exactly two cells narrower. Finite predecessors are also unique: a rightmost difference between two finite inputs survives one cell farther right in their outputs. Consequently every nonzero finite row descends to a unique finite root with no finite predecessor, and has a unique nonnegative age. The age is at most floor((R-L)/2).

The following small illustration uses the literal three-input rule. Its rows are aligned at the original seed's centre; each displayed row also has its own normalized word. The centre column is included for orientation, not as evidence about its eventual behaviour.

```wl
Clear[physicalStep, normalizedWords];
physicalStep[word_List] := Map[BitXor[#[[1]], BitOr[#[[2]], #[[3]]]] &,
  Partition[Join[{0, 0}, word, {0, 0}], 3, 1]];
smallRows = NestList[physicalStep, {1}, 4];
smallPicture = Table[PadRight[Join[ConstantArray[0, 4-t], smallRows[[t+1]]], 9], {t, 0, 4}];
Column[{ArrayPlot[smallPicture, ColorRules -> {0 -> White, 1 -> Black}, Frame -> True],
  Grid[Prepend[Table[{t, StringJoin[ToString /@ smallRows[[t+1]]], smallRows[[t+1, t+1]]}, {t, 0, 4}],
    {"time", "normalized row", "centre bit"}], Frame -> All]}]
```

## The exact boundary test

Fix a target y with black endpoints L,R and an actual predecessor p with F(p)=y. Require p(i)=0 for every i>=R, including R itself. This is the white-right branch of inverse reconstruction. The theorem `finite_parent_test` says that this p is finite if and only if y(L+1)=1 and p(L+1)=1. Its premise includes the entire physical predecessor equation; it does not assert that arbitrary choices at these two cells construct a predecessor.

For sufficiency, those two black bits force p(L)=p(L-1)=0 by the equations at L+1 and L. A white target half-line then propagates this adjacent white pair indefinitely leftward. The prescribed right tail gives the other finite boundary. Necessity follows from the exact endpoint growth. In particular the right-tail hypothesis starts at R, not at R+1; changing it changes the parent problem. Width-one and width-two targets have no nonzero finite parent.

The canonical inverse constructor is already available in the kit's `Preimages.leftPair` and `extendLeft`, with its correctness and uniqueness theorems. This package supplies the explicit physical stopping test, not a replacement constructor or a classification of all infinite inverse branches.

## Normalization makes the counting bijection exact

A normalized width-w word has black cells at 0 and w-1 and white cells outside that interval. Write C(0)=0, C(1)=1, and C(w)=2^(w-2) for w>=2. The width-one case has a single endpoint, not two independent endpoint choices.

For n steps, translate F^n(x) right by n, returning its left endpoint to 0. This map sends normalized width-w words to width-(w+2n) words. It is injective. Conversely, every normalized target with an n-step finite past has a parent with endpoints n,w+n-1; translating that parent left by n gives the unique normalized preimage. Both directions, including n=0 and the empty width-zero domain, occur in `normalized_ancestor_bijection`.

The proof counts actual rows by constructing an exhaustive list with no duplicates. `finite_word_enumeration` gives all normalized words and their exact length C(w). `finite_parent_enumeration` gives precisely those having a finite predecessor. For target width W>=4 there are 2^(W-4) such words among 2^(W-2) total words: one quarter have a finite parent. At W=3, only 111 among 101 and 111 does, giving one half. At widths one and two the count is zero.

This fixed, tiny table illustrates those universal statements. The independent integer formula is Karttunen's A269160, n XOR (2n OR 4n). Agreement with it checks the word orientation; neither formula replaces the Lean proof.

```wl
normalizedWords[0] := {};
normalizedWords[1] := {{1}};
normalizedWords[w_Integer] /; w >= 2 := Join[{1}, #, {1}] & /@ Tuples[{0, 1}, w-2];
countRows = Table[Module[{words = normalizedWords[w], parents, images},
  parents = If[w >= 3, normalizedWords[w-2], {}];
  images = physicalStep /@ parents;
  {w, Length[words], Length[DeleteDuplicates[images]], Length[words]-Length[DeleteDuplicates[images]]}],
  {w, 1, 8}];
illustrationWords = Join @@ Table[normalizedWords[w], {w, 1, 6}];
orientationOK = AllTrue[illustrationWords, Function[word,
  With[{n = FromDigits[word, 2]}, FromDigits[physicalStep[word], 2] === BitXor[n, BitOr[2n, 4n]]]]];
Column[{Grid[Prepend[countRows, {"width", "all words", "finite-parent words", "roots"}], Frame -> All],
  {"independent integer orientation check", orientationOK}}]
```

## What is already known, and what this interface supplies

Finite injectivity is standard cellular-automaton background. The kit's `Rule30Equivalents.Preimages.eq_of_evol_one_eq_of_right` is stronger: equal images and equal sufficiently far-right tails imply equal rows. Its white-right inverse reconstruction supplies the other main ingredient. `Rule30FiniteConfigs` and `Rule30FrozenRuler` already contain the needed edge facts. The present proof bodies repeat short specialized arguments using the core Realization interface; those repetitions are credited, not discoveries. The assembled source directly imports the official Prize module and Realization; both use the kit's core Jen module. Actual resource use remains to be measured during validation.

Karttunen's 2016 OEIS entries A269160 and A269162 record the finite map and inverse; A269165 and A269166 record the earliest finite ancestor and its age, including reconstruction. Positive odd integers encode our normalized words, with binary digits written left to right from most significant to least significant. The external decomposition and its objects are known. Our October6 G121 argument, carried by Local L077, already gave the exact width count and root descent.

The proposed contribution is a reusable physical-row formal interface joining the exact boundary test, simultaneous root/age uniqueness, translated n-step image characterization and exhaustive duplicate-free all-width enumeration. The current source comparison has not identified those combined exported interfaces in the kit; that is not a mathematical priority claim or automatic submission clearance. A final current-kit, portal and PR comparison must precede delivery.

## Formal source and its statements

The seven public wrappers are `Rule30Submission.finite_root_age`, `finite_parent_test`, `normalized_ancestor_bijection`, `finite_word_enumeration`, `finite_parent_enumeration`, `finite_parent_count`, and `finite_parent_small_widths`. Their complete definitions, including `Span`, `Root`, `Normal`, `Past` and the two enumerations, must be included in the embedded module. A submission may not import these preparation files from a private checkout.

The next cells are the planned formal checks. `%%LEAN_SOURCE_JSON_STRING%%` is a non-executable assembly marker, to be replaced only with a JSON-quoted, validated single module importing the official `Ruliology.CellularAutomata.Rule30Prize` module. This draft intentionally has no claimed `LeanEnvironment` or replay result. The final notebook uses `RULE30PRIZE_KIT` and contains its source rather than reading a local proof file.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)%%LEAN_SOURCE_JSON_STRING%%,
  "ProjectDir" -> $Rule30PrizeKit, "IncludeInternal" -> True]
```

```wl
fullheads = {"Rule30Submission.finite_root_age", "Rule30Submission.finite_parent_test",
  "Rule30Submission.normalized_ancestor_bijection", "Rule30Submission.finite_word_enumeration",
  "Rule30Submission.finite_parent_enumeration", "Rule30Submission.finite_parent_count",
  "Rule30Submission.finite_parent_small_widths"};
AssociationMap[rule30Submission[#]["TypeForm"] &, fullheads]
```

```wl
AssociationMap[rule30Submission[#]["Axioms"] &, fullheads]
```

Kernel replay comes last because it resets LeanLink's elaboration state. An axiom list alone is insufficient.

```wl
rule30Submission[First[fullheads]]["KernelCheck"]
```

## Limits and references

The result does not exclude any new eventual centre-column period. A minimal-counterexample argument still has to handle the roots; most fixed-width words are roots already. No infinite-past family, spatial-density limit, orbit-frequency statement or low-population age classification is part of this package. A uniform distribution over finite words is not the distribution of an actual orbit.

The final notebook must report the actual checker outcome for its exact source, with compilation, kernel replay, portal receipt, Lean Verified and Human Verified kept separate. The present draft has none of those outcomes.

References: the Rule 30 Prize kit's actual `Preimages`, `FiniteConfigs`, `FrozenRuler` and `Jen` sources; Karttunen's OEIS A269160, A269162, A269165 and A269166; the project G121/G122/L077 carrying record; Jarkko Kari's [Cellular Automata tutorial](https://users.utu.fi/jkari/wp-content/uploads/sites/1251/2023/12/CAintro.pdf) on finite configurations and global surjectivity.
