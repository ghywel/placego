---
Template: ComputationalEssay
Name: The death time at width 60 is exactly 114: a complete chunk certificate and its witness
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-24
Description: A partial result on the kit's Q01 (the zero-boundary reduction of the period-2 question, Problem 1 of the Rule 30 Prize), proved in Lean against the kit's own definitions: 4,096 kernel-decided chunk checks give the upper bound 114 at width 60, and an explicit start attains it, so the death time at width 60 is exactly 114.
Abstract: The kit proves Q01 for every zero-boundary start of width at most 52 by 256 kernel-decided chunk checks with the bound 96. This module carries 4,096 checks at width 60 at K = 115, assembled by the kit's q01_of_chunks into q01_width_le_60 (every start of width at most 60 has a white depth-1 cell at an even time at most 114), and proves the bound exact: the explicit start 0xe77a4e77b8f99b5 is black at depth 1 at every even time below 114 and white at 114, by the kit's packed evaluator prun and its bridge run_toFun (the headline theorem Rule30Submission.death_time_60_exact). With submissions R30-20261023-8e6bd3 (D(52) = 96) and R30-20261023-ac3898 (D(56) = 100), the table of exact death times has three kernel-checked entries, 96, 100, 114, not fitted by one common constant c in D(W) = 2W - c.
Keywords: [rule 30, Rule 30 Prize, Problem 1, Q01, zero boundary, death time, exact bound, chunk certificate, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record, CHAT-LEDGER.md L805 to L844](https://github.com/ghywel/placego/blob/main/CHAT-LEDGER.md)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[wolframcollatzmahler.com](https://www.wolframcollatzmahler.com)", "[Submission R30-20261023-ac3898, the width-56 exact value](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261023-ac3898)"]
---

## The question

The kit's `Q01` is the zero-boundary reduction of the period-2 question of Problem 1: every finite start of the left half, evolved by rule 30 with a white wall at depth 0, has a white cell at depth 1 at some even time. The kit proves `Q01` for every start of width at most 52 by 256 kernel-decided chunk checks (`Rule30ZeroBoundaryWidth52`, bound 96); our submissions R30-20261023-8e6bd3 and R30-20261023-ac3898 proved the exact values 96 at width 52 and 100 at width 56. This essay carries a width-60 certificate of 4,096 checks and proves its bound exact.

Write `D(W)` for the largest, over starts supported at depths 1 to `W`, of the first even time at which the depth-1 cell is white. Here: `D(60) = 114`.

## The packed model and the witness

The kit's `Rule30ZeroBoundarySmall` packs a row into a natural number (bit `j` is depth `j + 1`, the wall at depth 0 white) and steps it by `pstep r = (r >>> 1) xor (r ||| (r <<< 1))`; its theorem `run_toFun` says the packed orbit is the physical evolution `zrow`. In the Wolfram Language:

```wl
pstep[r_] := BitXor[BitShiftRight[r, 1], BitOr[r, BitShiftLeft[r, 1]]];
orbit[r_, n_] := NestList[pstep, r, n];
depth1[r_, n_] := BitAnd[#, 1] & /@ orbit[r, n];
firstEvenWhite[r_, n_] := First[Select[Range[0, n, 2], depth1[r, n][[# + 1]] == 0 &]];
w60 = 16^^e77a4e77b8f99b5;
{BitLength[w60], firstEvenWhite[w60, 130]}
```

The orbit of `w60` for 118 steps, depth 1 at the left:

```wl
rows = Reverse[IntegerDigits[#, 2, 190]] & /@ orbit[w60, 118];
ArrayPlot[rows, ImageSize -> 600, Frame -> False]
```

## The certificate

The kit's `Rule30ZeroBoundaryLanes` checks `2^18` starts at once as the bits of one natural number (a chunk), `check 60 115 18 c = true` meaning that every start in chunk `c` has a white depth-1 cell at an even time below 115; `q01_of_chunks` turns all `2^(30 - 18) = 4,096` chunks into `Q01` for width 60. The module below carries the 4,096 checks, each decided by the kernel, in 256 namespaces of 16 with the kit's `chunksOK_append` trees, then the assembled bound and the witness. LeanLink and the kit:

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["import Rule30PrizeKit
import Ruliology.CellularAutomata.Rule30ZeroBoundarySmall
import Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes

/-!
# The death time at width 60 is exactly 114: a complete chunk certificate and its witness

**Partial result on the kit's `Q01` (the period-2 question, Problem 1 of the Rule 30 Prize).** The kit proves `Q01`
for every zero-boundary start of width at most 52 (`Rule30ZeroBoundaryWidth52`, 256 chunk checks, bound 96) and
has no width-60 statement; W3 of our record certified bound 128 (4,096 checks at K = 129) and the census found the true maximum 114. This module
carries 4096 checks (`check 60 115 18 c = true`, each decided by the kernel, in 256 namespaces of 16 with the
kit's `chunksOK_append` trees), assembles them by the kit's `q01_of_chunks` into `q01_width_le_60` (every start of
width at most 60 has a white depth-1 cell at an even time at most 114), and proves the bound exact: the explicit
start `w60` is black at depth 1 at every even time below 114 and white at 114, by the kit's packed evaluator `prun`
and its bridge `run_toFun` (`death_time_60_exact`).

**Provenance.** The chunk text is the W2 generator's of the Wolfram · Collatz · Mahler record (github.com/ghywel/placego,
tests/probes/wolfram/w2_harness.py), whose width-52 regeneration equals the kit's own modules line for line; the
certificate was built and checked by the kit's `Check.lean` on the M5 on 2026-10-23 (CHAT-LEDGER.md L794 for 56, L818
for 60), the witness found and validated in lane D-exact (L812, L816, L818). Nothing is claimed for any other width.
-/

set_option Elab.async false

namespace Rule30Submission

open Ruliology.CellularAutomata
open Ruliology.CellularAutomata.Rule30ZeroBoundary
open Ruliology.CellularAutomata.Rule30ZeroBoundarySmall
open Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes

/-! ## The 4096 chunk checks, kernel-decided -/
namespace C0

theorem c0 : check 60 115 18 0 = true := by decide +kernel
theorem c1 : check 60 115 18 1 = true := by decide +kernel
theorem c2 : check 60 115 18 2 = true := by decide +kernel
theorem c3 : check 60 115 18 3 = true := by decide +kernel
theorem c4 : check 60 115 18 4 = true := by decide +kernel
theorem c5 : check 60 115 18 5 = true := by decide +kernel
theorem c6 : check 60 115 18 6 = true := by decide +kernel
theorem c7 : check 60 115 18 7 = true := by decide +kernel
theorem c8 : check 60 115 18 8 = true := by decide +kernel
theorem c9 : check 60 115 18 9 = true := by decide +kernel
theorem c10 : check 60 115 18 10 = true := by decide +kernel
theorem c11 : check 60 115 18 11 = true := by decide +kernel
theorem c12 : check 60 115 18 12 = true := by decide +kernel
theorem c13 : check 60 115 18 13 = true := by decide +kernel
theorem c14 : check 60 115 18 14 = true := by decide +kernel
theorem c15 : check 60 115 18 15 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 0 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c0) (chunksOK_one c1)) (chunksOK_append (chunksOK_one c2) (chunksOK_one c3))) (chunksOK_append (chunksOK_append (chunksOK_one c4) (chunksOK_one c5)) (chunksOK_append (chunksOK_one c6) (chunksOK_one c7)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c8) (chunksOK_one c9)) (chunksOK_append (chunksOK_one c10) (chunksOK_one c11))) (chunksOK_append (chunksOK_append (chunksOK_one c12) (chunksOK_one c13)) (chunksOK_append (chunksOK_one c14) (chunksOK_one c15)))))

end C0

namespace C1

theorem c16 : check 60 115 18 16 = true := by decide +kernel
theorem c17 : check 60 115 18 17 = true := by decide +kernel
theorem c18 : check 60 115 18 18 = true := by decide +kernel
theorem c19 : check 60 115 18 19 = true := by decide +kernel
theorem c20 : check 60 115 18 20 = true := by decide +kernel
theorem c21 : check 60 115 18 21 = true := by decide +kernel
theorem c22 : check 60 115 18 22 = true := by decide +kernel
theorem c23 : check 60 115 18 23 = true := by decide +kernel
theorem c24 : check 60 115 18 24 = true := by decide +kernel
theorem c25 : check 60 115 18 25 = true := by decide +kernel
theorem c26 : check 60 115 18 26 = true := by decide +kernel
theorem c27 : check 60 115 18 27 = true := by decide +kernel
theorem c28 : check 60 115 18 28 = true := by decide +kernel
theorem c29 : check 60 115 18 29 = true := by decide +kernel
theorem c30 : check 60 115 18 30 = true := by decide +kernel
theorem c31 : check 60 115 18 31 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 16 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c16) (chunksOK_one c17)) (chunksOK_append (chunksOK_one c18) (chunksOK_one c19))) (chunksOK_append (chunksOK_append (chunksOK_one c20) (chunksOK_one c21)) (chunksOK_append (chunksOK_one c22) (chunksOK_one c23)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c24) (chunksOK_one c25)) (chunksOK_append (chunksOK_one c26) (chunksOK_one c27))) (chunksOK_append (chunksOK_append (chunksOK_one c28) (chunksOK_one c29)) (chunksOK_append (chunksOK_one c30) (chunksOK_one c31)))))

end C1

namespace C2

theorem c32 : check 60 115 18 32 = true := by decide +kernel
theorem c33 : check 60 115 18 33 = true := by decide +kernel
theorem c34 : check 60 115 18 34 = true := by decide +kernel
theorem c35 : check 60 115 18 35 = true := by decide +kernel
theorem c36 : check 60 115 18 36 = true := by decide +kernel
theorem c37 : check 60 115 18 37 = true := by decide +kernel
theorem c38 : check 60 115 18 38 = true := by decide +kernel
theorem c39 : check 60 115 18 39 = true := by decide +kernel
theorem c40 : check 60 115 18 40 = true := by decide +kernel
theorem c41 : check 60 115 18 41 = true := by decide +kernel
theorem c42 : check 60 115 18 42 = true := by decide +kernel
theorem c43 : check 60 115 18 43 = true := by decide +kernel
theorem c44 : check 60 115 18 44 = true := by decide +kernel
theorem c45 : check 60 115 18 45 = true := by decide +kernel
theorem c46 : check 60 115 18 46 = true := by decide +kernel
theorem c47 : check 60 115 18 47 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 32 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c32) (chunksOK_one c33)) (chunksOK_append (chunksOK_one c34) (chunksOK_one c35))) (chunksOK_append (chunksOK_append (chunksOK_one c36) (chunksOK_one c37)) (chunksOK_append (chunksOK_one c38) (chunksOK_one c39)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c40) (chunksOK_one c41)) (chunksOK_append (chunksOK_one c42) (chunksOK_one c43))) (chunksOK_append (chunksOK_append (chunksOK_one c44) (chunksOK_one c45)) (chunksOK_append (chunksOK_one c46) (chunksOK_one c47)))))

end C2

namespace C3

theorem c48 : check 60 115 18 48 = true := by decide +kernel
theorem c49 : check 60 115 18 49 = true := by decide +kernel
theorem c50 : check 60 115 18 50 = true := by decide +kernel
theorem c51 : check 60 115 18 51 = true := by decide +kernel
theorem c52 : check 60 115 18 52 = true := by decide +kernel
theorem c53 : check 60 115 18 53 = true := by decide +kernel
theorem c54 : check 60 115 18 54 = true := by decide +kernel
theorem c55 : check 60 115 18 55 = true := by decide +kernel
theorem c56 : check 60 115 18 56 = true := by decide +kernel
theorem c57 : check 60 115 18 57 = true := by decide +kernel
theorem c58 : check 60 115 18 58 = true := by decide +kernel
theorem c59 : check 60 115 18 59 = true := by decide +kernel
theorem c60 : check 60 115 18 60 = true := by decide +kernel
theorem c61 : check 60 115 18 61 = true := by decide +kernel
theorem c62 : check 60 115 18 62 = true := by decide +kernel
theorem c63 : check 60 115 18 63 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 48 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c48) (chunksOK_one c49)) (chunksOK_append (chunksOK_one c50) (chunksOK_one c51))) (chunksOK_append (chunksOK_append (chunksOK_one c52) (chunksOK_one c53)) (chunksOK_append (chunksOK_one c54) (chunksOK_one c55)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c56) (chunksOK_one c57)) (chunksOK_append (chunksOK_one c58) (chunksOK_one c59))) (chunksOK_append (chunksOK_append (chunksOK_one c60) (chunksOK_one c61)) (chunksOK_append (chunksOK_one c62) (chunksOK_one c63)))))

end C3

namespace C4

theorem c64 : check 60 115 18 64 = true := by decide +kernel
theorem c65 : check 60 115 18 65 = true := by decide +kernel
theorem c66 : check 60 115 18 66 = true := by decide +kernel
theorem c67 : check 60 115 18 67 = true := by decide +kernel
theorem c68 : check 60 115 18 68 = true := by decide +kernel
theorem c69 : check 60 115 18 69 = true := by decide +kernel
theorem c70 : check 60 115 18 70 = true := by decide +kernel
theorem c71 : check 60 115 18 71 = true := by decide +kernel
theorem c72 : check 60 115 18 72 = true := by decide +kernel
theorem c73 : check 60 115 18 73 = true := by decide +kernel
theorem c74 : check 60 115 18 74 = true := by decide +kernel
theorem c75 : check 60 115 18 75 = true := by decide +kernel
theorem c76 : check 60 115 18 76 = true := by decide +kernel
theorem c77 : check 60 115 18 77 = true := by decide +kernel
theorem c78 : check 60 115 18 78 = true := by decide +kernel
theorem c79 : check 60 115 18 79 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 64 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c64) (chunksOK_one c65)) (chunksOK_append (chunksOK_one c66) (chunksOK_one c67))) (chunksOK_append (chunksOK_append (chunksOK_one c68) (chunksOK_one c69)) (chunksOK_append (chunksOK_one c70) (chunksOK_one c71)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c72) (chunksOK_one c73)) (chunksOK_append (chunksOK_one c74) (chunksOK_one c75))) (chunksOK_append (chunksOK_append (chunksOK_one c76) (chunksOK_one c77)) (chunksOK_append (chunksOK_one c78) (chunksOK_one c79)))))

end C4

namespace C5

theorem c80 : check 60 115 18 80 = true := by decide +kernel
theorem c81 : check 60 115 18 81 = true := by decide +kernel
theorem c82 : check 60 115 18 82 = true := by decide +kernel
theorem c83 : check 60 115 18 83 = true := by decide +kernel
theorem c84 : check 60 115 18 84 = true := by decide +kernel
theorem c85 : check 60 115 18 85 = true := by decide +kernel
theorem c86 : check 60 115 18 86 = true := by decide +kernel
theorem c87 : check 60 115 18 87 = true := by decide +kernel
theorem c88 : check 60 115 18 88 = true := by decide +kernel
theorem c89 : check 60 115 18 89 = true := by decide +kernel
theorem c90 : check 60 115 18 90 = true := by decide +kernel
theorem c91 : check 60 115 18 91 = true := by decide +kernel
theorem c92 : check 60 115 18 92 = true := by decide +kernel
theorem c93 : check 60 115 18 93 = true := by decide +kernel
theorem c94 : check 60 115 18 94 = true := by decide +kernel
theorem c95 : check 60 115 18 95 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 80 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c80) (chunksOK_one c81)) (chunksOK_append (chunksOK_one c82) (chunksOK_one c83))) (chunksOK_append (chunksOK_append (chunksOK_one c84) (chunksOK_one c85)) (chunksOK_append (chunksOK_one c86) (chunksOK_one c87)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c88) (chunksOK_one c89)) (chunksOK_append (chunksOK_one c90) (chunksOK_one c91))) (chunksOK_append (chunksOK_append (chunksOK_one c92) (chunksOK_one c93)) (chunksOK_append (chunksOK_one c94) (chunksOK_one c95)))))

end C5

namespace C6

theorem c96 : check 60 115 18 96 = true := by decide +kernel
theorem c97 : check 60 115 18 97 = true := by decide +kernel
theorem c98 : check 60 115 18 98 = true := by decide +kernel
theorem c99 : check 60 115 18 99 = true := by decide +kernel
theorem c100 : check 60 115 18 100 = true := by decide +kernel
theorem c101 : check 60 115 18 101 = true := by decide +kernel
theorem c102 : check 60 115 18 102 = true := by decide +kernel
theorem c103 : check 60 115 18 103 = true := by decide +kernel
theorem c104 : check 60 115 18 104 = true := by decide +kernel
theorem c105 : check 60 115 18 105 = true := by decide +kernel
theorem c106 : check 60 115 18 106 = true := by decide +kernel
theorem c107 : check 60 115 18 107 = true := by decide +kernel
theorem c108 : check 60 115 18 108 = true := by decide +kernel
theorem c109 : check 60 115 18 109 = true := by decide +kernel
theorem c110 : check 60 115 18 110 = true := by decide +kernel
theorem c111 : check 60 115 18 111 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 96 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c96) (chunksOK_one c97)) (chunksOK_append (chunksOK_one c98) (chunksOK_one c99))) (chunksOK_append (chunksOK_append (chunksOK_one c100) (chunksOK_one c101)) (chunksOK_append (chunksOK_one c102) (chunksOK_one c103)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c104) (chunksOK_one c105)) (chunksOK_append (chunksOK_one c106) (chunksOK_one c107))) (chunksOK_append (chunksOK_append (chunksOK_one c108) (chunksOK_one c109)) (chunksOK_append (chunksOK_one c110) (chunksOK_one c111)))))

end C6

namespace C7

theorem c112 : check 60 115 18 112 = true := by decide +kernel
theorem c113 : check 60 115 18 113 = true := by decide +kernel
theorem c114 : check 60 115 18 114 = true := by decide +kernel
theorem c115 : check 60 115 18 115 = true := by decide +kernel
theorem c116 : check 60 115 18 116 = true := by decide +kernel
theorem c117 : check 60 115 18 117 = true := by decide +kernel
theorem c118 : check 60 115 18 118 = true := by decide +kernel
theorem c119 : check 60 115 18 119 = true := by decide +kernel
theorem c120 : check 60 115 18 120 = true := by decide +kernel
theorem c121 : check 60 115 18 121 = true := by decide +kernel
theorem c122 : check 60 115 18 122 = true := by decide +kernel
theorem c123 : check 60 115 18 123 = true := by decide +kernel
theorem c124 : check 60 115 18 124 = true := by decide +kernel
theorem c125 : check 60 115 18 125 = true := by decide +kernel
theorem c126 : check 60 115 18 126 = true := by decide +kernel
theorem c127 : check 60 115 18 127 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 112 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c112) (chunksOK_one c113)) (chunksOK_append (chunksOK_one c114) (chunksOK_one c115))) (chunksOK_append (chunksOK_append (chunksOK_one c116) (chunksOK_one c117)) (chunksOK_append (chunksOK_one c118) (chunksOK_one c119)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c120) (chunksOK_one c121)) (chunksOK_append (chunksOK_one c122) (chunksOK_one c123))) (chunksOK_append (chunksOK_append (chunksOK_one c124) (chunksOK_one c125)) (chunksOK_append (chunksOK_one c126) (chunksOK_one c127)))))

end C7

namespace C8

theorem c128 : check 60 115 18 128 = true := by decide +kernel
theorem c129 : check 60 115 18 129 = true := by decide +kernel
theorem c130 : check 60 115 18 130 = true := by decide +kernel
theorem c131 : check 60 115 18 131 = true := by decide +kernel
theorem c132 : check 60 115 18 132 = true := by decide +kernel
theorem c133 : check 60 115 18 133 = true := by decide +kernel
theorem c134 : check 60 115 18 134 = true := by decide +kernel
theorem c135 : check 60 115 18 135 = true := by decide +kernel
theorem c136 : check 60 115 18 136 = true := by decide +kernel
theorem c137 : check 60 115 18 137 = true := by decide +kernel
theorem c138 : check 60 115 18 138 = true := by decide +kernel
theorem c139 : check 60 115 18 139 = true := by decide +kernel
theorem c140 : check 60 115 18 140 = true := by decide +kernel
theorem c141 : check 60 115 18 141 = true := by decide +kernel
theorem c142 : check 60 115 18 142 = true := by decide +kernel
theorem c143 : check 60 115 18 143 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 128 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c128) (chunksOK_one c129)) (chunksOK_append (chunksOK_one c130) (chunksOK_one c131))) (chunksOK_append (chunksOK_append (chunksOK_one c132) (chunksOK_one c133)) (chunksOK_append (chunksOK_one c134) (chunksOK_one c135)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c136) (chunksOK_one c137)) (chunksOK_append (chunksOK_one c138) (chunksOK_one c139))) (chunksOK_append (chunksOK_append (chunksOK_one c140) (chunksOK_one c141)) (chunksOK_append (chunksOK_one c142) (chunksOK_one c143)))))

end C8

namespace C9

theorem c144 : check 60 115 18 144 = true := by decide +kernel
theorem c145 : check 60 115 18 145 = true := by decide +kernel
theorem c146 : check 60 115 18 146 = true := by decide +kernel
theorem c147 : check 60 115 18 147 = true := by decide +kernel
theorem c148 : check 60 115 18 148 = true := by decide +kernel
theorem c149 : check 60 115 18 149 = true := by decide +kernel
theorem c150 : check 60 115 18 150 = true := by decide +kernel
theorem c151 : check 60 115 18 151 = true := by decide +kernel
theorem c152 : check 60 115 18 152 = true := by decide +kernel
theorem c153 : check 60 115 18 153 = true := by decide +kernel
theorem c154 : check 60 115 18 154 = true := by decide +kernel
theorem c155 : check 60 115 18 155 = true := by decide +kernel
theorem c156 : check 60 115 18 156 = true := by decide +kernel
theorem c157 : check 60 115 18 157 = true := by decide +kernel
theorem c158 : check 60 115 18 158 = true := by decide +kernel
theorem c159 : check 60 115 18 159 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 144 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c144) (chunksOK_one c145)) (chunksOK_append (chunksOK_one c146) (chunksOK_one c147))) (chunksOK_append (chunksOK_append (chunksOK_one c148) (chunksOK_one c149)) (chunksOK_append (chunksOK_one c150) (chunksOK_one c151)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c152) (chunksOK_one c153)) (chunksOK_append (chunksOK_one c154) (chunksOK_one c155))) (chunksOK_append (chunksOK_append (chunksOK_one c156) (chunksOK_one c157)) (chunksOK_append (chunksOK_one c158) (chunksOK_one c159)))))

end C9

namespace C10

theorem c160 : check 60 115 18 160 = true := by decide +kernel
theorem c161 : check 60 115 18 161 = true := by decide +kernel
theorem c162 : check 60 115 18 162 = true := by decide +kernel
theorem c163 : check 60 115 18 163 = true := by decide +kernel
theorem c164 : check 60 115 18 164 = true := by decide +kernel
theorem c165 : check 60 115 18 165 = true := by decide +kernel
theorem c166 : check 60 115 18 166 = true := by decide +kernel
theorem c167 : check 60 115 18 167 = true := by decide +kernel
theorem c168 : check 60 115 18 168 = true := by decide +kernel
theorem c169 : check 60 115 18 169 = true := by decide +kernel
theorem c170 : check 60 115 18 170 = true := by decide +kernel
theorem c171 : check 60 115 18 171 = true := by decide +kernel
theorem c172 : check 60 115 18 172 = true := by decide +kernel
theorem c173 : check 60 115 18 173 = true := by decide +kernel
theorem c174 : check 60 115 18 174 = true := by decide +kernel
theorem c175 : check 60 115 18 175 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 160 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c160) (chunksOK_one c161)) (chunksOK_append (chunksOK_one c162) (chunksOK_one c163))) (chunksOK_append (chunksOK_append (chunksOK_one c164) (chunksOK_one c165)) (chunksOK_append (chunksOK_one c166) (chunksOK_one c167)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c168) (chunksOK_one c169)) (chunksOK_append (chunksOK_one c170) (chunksOK_one c171))) (chunksOK_append (chunksOK_append (chunksOK_one c172) (chunksOK_one c173)) (chunksOK_append (chunksOK_one c174) (chunksOK_one c175)))))

end C10

namespace C11

theorem c176 : check 60 115 18 176 = true := by decide +kernel
theorem c177 : check 60 115 18 177 = true := by decide +kernel
theorem c178 : check 60 115 18 178 = true := by decide +kernel
theorem c179 : check 60 115 18 179 = true := by decide +kernel
theorem c180 : check 60 115 18 180 = true := by decide +kernel
theorem c181 : check 60 115 18 181 = true := by decide +kernel
theorem c182 : check 60 115 18 182 = true := by decide +kernel
theorem c183 : check 60 115 18 183 = true := by decide +kernel
theorem c184 : check 60 115 18 184 = true := by decide +kernel
theorem c185 : check 60 115 18 185 = true := by decide +kernel
theorem c186 : check 60 115 18 186 = true := by decide +kernel
theorem c187 : check 60 115 18 187 = true := by decide +kernel
theorem c188 : check 60 115 18 188 = true := by decide +kernel
theorem c189 : check 60 115 18 189 = true := by decide +kernel
theorem c190 : check 60 115 18 190 = true := by decide +kernel
theorem c191 : check 60 115 18 191 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 176 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c176) (chunksOK_one c177)) (chunksOK_append (chunksOK_one c178) (chunksOK_one c179))) (chunksOK_append (chunksOK_append (chunksOK_one c180) (chunksOK_one c181)) (chunksOK_append (chunksOK_one c182) (chunksOK_one c183)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c184) (chunksOK_one c185)) (chunksOK_append (chunksOK_one c186) (chunksOK_one c187))) (chunksOK_append (chunksOK_append (chunksOK_one c188) (chunksOK_one c189)) (chunksOK_append (chunksOK_one c190) (chunksOK_one c191)))))

end C11

namespace C12

theorem c192 : check 60 115 18 192 = true := by decide +kernel
theorem c193 : check 60 115 18 193 = true := by decide +kernel
theorem c194 : check 60 115 18 194 = true := by decide +kernel
theorem c195 : check 60 115 18 195 = true := by decide +kernel
theorem c196 : check 60 115 18 196 = true := by decide +kernel
theorem c197 : check 60 115 18 197 = true := by decide +kernel
theorem c198 : check 60 115 18 198 = true := by decide +kernel
theorem c199 : check 60 115 18 199 = true := by decide +kernel
theorem c200 : check 60 115 18 200 = true := by decide +kernel
theorem c201 : check 60 115 18 201 = true := by decide +kernel
theorem c202 : check 60 115 18 202 = true := by decide +kernel
theorem c203 : check 60 115 18 203 = true := by decide +kernel
theorem c204 : check 60 115 18 204 = true := by decide +kernel
theorem c205 : check 60 115 18 205 = true := by decide +kernel
theorem c206 : check 60 115 18 206 = true := by decide +kernel
theorem c207 : check 60 115 18 207 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 192 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c192) (chunksOK_one c193)) (chunksOK_append (chunksOK_one c194) (chunksOK_one c195))) (chunksOK_append (chunksOK_append (chunksOK_one c196) (chunksOK_one c197)) (chunksOK_append (chunksOK_one c198) (chunksOK_one c199)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c200) (chunksOK_one c201)) (chunksOK_append (chunksOK_one c202) (chunksOK_one c203))) (chunksOK_append (chunksOK_append (chunksOK_one c204) (chunksOK_one c205)) (chunksOK_append (chunksOK_one c206) (chunksOK_one c207)))))

end C12

namespace C13

theorem c208 : check 60 115 18 208 = true := by decide +kernel
theorem c209 : check 60 115 18 209 = true := by decide +kernel
theorem c210 : check 60 115 18 210 = true := by decide +kernel
theorem c211 : check 60 115 18 211 = true := by decide +kernel
theorem c212 : check 60 115 18 212 = true := by decide +kernel
theorem c213 : check 60 115 18 213 = true := by decide +kernel
theorem c214 : check 60 115 18 214 = true := by decide +kernel
theorem c215 : check 60 115 18 215 = true := by decide +kernel
theorem c216 : check 60 115 18 216 = true := by decide +kernel
theorem c217 : check 60 115 18 217 = true := by decide +kernel
theorem c218 : check 60 115 18 218 = true := by decide +kernel
theorem c219 : check 60 115 18 219 = true := by decide +kernel
theorem c220 : check 60 115 18 220 = true := by decide +kernel
theorem c221 : check 60 115 18 221 = true := by decide +kernel
theorem c222 : check 60 115 18 222 = true := by decide +kernel
theorem c223 : check 60 115 18 223 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 208 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c208) (chunksOK_one c209)) (chunksOK_append (chunksOK_one c210) (chunksOK_one c211))) (chunksOK_append (chunksOK_append (chunksOK_one c212) (chunksOK_one c213)) (chunksOK_append (chunksOK_one c214) (chunksOK_one c215)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c216) (chunksOK_one c217)) (chunksOK_append (chunksOK_one c218) (chunksOK_one c219))) (chunksOK_append (chunksOK_append (chunksOK_one c220) (chunksOK_one c221)) (chunksOK_append (chunksOK_one c222) (chunksOK_one c223)))))

end C13

namespace C14

theorem c224 : check 60 115 18 224 = true := by decide +kernel
theorem c225 : check 60 115 18 225 = true := by decide +kernel
theorem c226 : check 60 115 18 226 = true := by decide +kernel
theorem c227 : check 60 115 18 227 = true := by decide +kernel
theorem c228 : check 60 115 18 228 = true := by decide +kernel
theorem c229 : check 60 115 18 229 = true := by decide +kernel
theorem c230 : check 60 115 18 230 = true := by decide +kernel
theorem c231 : check 60 115 18 231 = true := by decide +kernel
theorem c232 : check 60 115 18 232 = true := by decide +kernel
theorem c233 : check 60 115 18 233 = true := by decide +kernel
theorem c234 : check 60 115 18 234 = true := by decide +kernel
theorem c235 : check 60 115 18 235 = true := by decide +kernel
theorem c236 : check 60 115 18 236 = true := by decide +kernel
theorem c237 : check 60 115 18 237 = true := by decide +kernel
theorem c238 : check 60 115 18 238 = true := by decide +kernel
theorem c239 : check 60 115 18 239 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 224 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c224) (chunksOK_one c225)) (chunksOK_append (chunksOK_one c226) (chunksOK_one c227))) (chunksOK_append (chunksOK_append (chunksOK_one c228) (chunksOK_one c229)) (chunksOK_append (chunksOK_one c230) (chunksOK_one c231)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c232) (chunksOK_one c233)) (chunksOK_append (chunksOK_one c234) (chunksOK_one c235))) (chunksOK_append (chunksOK_append (chunksOK_one c236) (chunksOK_one c237)) (chunksOK_append (chunksOK_one c238) (chunksOK_one c239)))))

end C14

namespace C15

theorem c240 : check 60 115 18 240 = true := by decide +kernel
theorem c241 : check 60 115 18 241 = true := by decide +kernel
theorem c242 : check 60 115 18 242 = true := by decide +kernel
theorem c243 : check 60 115 18 243 = true := by decide +kernel
theorem c244 : check 60 115 18 244 = true := by decide +kernel
theorem c245 : check 60 115 18 245 = true := by decide +kernel
theorem c246 : check 60 115 18 246 = true := by decide +kernel
theorem c247 : check 60 115 18 247 = true := by decide +kernel
theorem c248 : check 60 115 18 248 = true := by decide +kernel
theorem c249 : check 60 115 18 249 = true := by decide +kernel
theorem c250 : check 60 115 18 250 = true := by decide +kernel
theorem c251 : check 60 115 18 251 = true := by decide +kernel
theorem c252 : check 60 115 18 252 = true := by decide +kernel
theorem c253 : check 60 115 18 253 = true := by decide +kernel
theorem c254 : check 60 115 18 254 = true := by decide +kernel
theorem c255 : check 60 115 18 255 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 240 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c240) (chunksOK_one c241)) (chunksOK_append (chunksOK_one c242) (chunksOK_one c243))) (chunksOK_append (chunksOK_append (chunksOK_one c244) (chunksOK_one c245)) (chunksOK_append (chunksOK_one c246) (chunksOK_one c247)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c248) (chunksOK_one c249)) (chunksOK_append (chunksOK_one c250) (chunksOK_one c251))) (chunksOK_append (chunksOK_append (chunksOK_one c252) (chunksOK_one c253)) (chunksOK_append (chunksOK_one c254) (chunksOK_one c255)))))

end C15

namespace C16

theorem c256 : check 60 115 18 256 = true := by decide +kernel
theorem c257 : check 60 115 18 257 = true := by decide +kernel
theorem c258 : check 60 115 18 258 = true := by decide +kernel
theorem c259 : check 60 115 18 259 = true := by decide +kernel
theorem c260 : check 60 115 18 260 = true := by decide +kernel
theorem c261 : check 60 115 18 261 = true := by decide +kernel
theorem c262 : check 60 115 18 262 = true := by decide +kernel
theorem c263 : check 60 115 18 263 = true := by decide +kernel
theorem c264 : check 60 115 18 264 = true := by decide +kernel
theorem c265 : check 60 115 18 265 = true := by decide +kernel
theorem c266 : check 60 115 18 266 = true := by decide +kernel
theorem c267 : check 60 115 18 267 = true := by decide +kernel
theorem c268 : check 60 115 18 268 = true := by decide +kernel
theorem c269 : check 60 115 18 269 = true := by decide +kernel
theorem c270 : check 60 115 18 270 = true := by decide +kernel
theorem c271 : check 60 115 18 271 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 256 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c256) (chunksOK_one c257)) (chunksOK_append (chunksOK_one c258) (chunksOK_one c259))) (chunksOK_append (chunksOK_append (chunksOK_one c260) (chunksOK_one c261)) (chunksOK_append (chunksOK_one c262) (chunksOK_one c263)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c264) (chunksOK_one c265)) (chunksOK_append (chunksOK_one c266) (chunksOK_one c267))) (chunksOK_append (chunksOK_append (chunksOK_one c268) (chunksOK_one c269)) (chunksOK_append (chunksOK_one c270) (chunksOK_one c271)))))

end C16

namespace C17

theorem c272 : check 60 115 18 272 = true := by decide +kernel
theorem c273 : check 60 115 18 273 = true := by decide +kernel
theorem c274 : check 60 115 18 274 = true := by decide +kernel
theorem c275 : check 60 115 18 275 = true := by decide +kernel
theorem c276 : check 60 115 18 276 = true := by decide +kernel
theorem c277 : check 60 115 18 277 = true := by decide +kernel
theorem c278 : check 60 115 18 278 = true := by decide +kernel
theorem c279 : check 60 115 18 279 = true := by decide +kernel
theorem c280 : check 60 115 18 280 = true := by decide +kernel
theorem c281 : check 60 115 18 281 = true := by decide +kernel
theorem c282 : check 60 115 18 282 = true := by decide +kernel
theorem c283 : check 60 115 18 283 = true := by decide +kernel
theorem c284 : check 60 115 18 284 = true := by decide +kernel
theorem c285 : check 60 115 18 285 = true := by decide +kernel
theorem c286 : check 60 115 18 286 = true := by decide +kernel
theorem c287 : check 60 115 18 287 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 272 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c272) (chunksOK_one c273)) (chunksOK_append (chunksOK_one c274) (chunksOK_one c275))) (chunksOK_append (chunksOK_append (chunksOK_one c276) (chunksOK_one c277)) (chunksOK_append (chunksOK_one c278) (chunksOK_one c279)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c280) (chunksOK_one c281)) (chunksOK_append (chunksOK_one c282) (chunksOK_one c283))) (chunksOK_append (chunksOK_append (chunksOK_one c284) (chunksOK_one c285)) (chunksOK_append (chunksOK_one c286) (chunksOK_one c287)))))

end C17

namespace C18

theorem c288 : check 60 115 18 288 = true := by decide +kernel
theorem c289 : check 60 115 18 289 = true := by decide +kernel
theorem c290 : check 60 115 18 290 = true := by decide +kernel
theorem c291 : check 60 115 18 291 = true := by decide +kernel
theorem c292 : check 60 115 18 292 = true := by decide +kernel
theorem c293 : check 60 115 18 293 = true := by decide +kernel
theorem c294 : check 60 115 18 294 = true := by decide +kernel
theorem c295 : check 60 115 18 295 = true := by decide +kernel
theorem c296 : check 60 115 18 296 = true := by decide +kernel
theorem c297 : check 60 115 18 297 = true := by decide +kernel
theorem c298 : check 60 115 18 298 = true := by decide +kernel
theorem c299 : check 60 115 18 299 = true := by decide +kernel
theorem c300 : check 60 115 18 300 = true := by decide +kernel
theorem c301 : check 60 115 18 301 = true := by decide +kernel
theorem c302 : check 60 115 18 302 = true := by decide +kernel
theorem c303 : check 60 115 18 303 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 288 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c288) (chunksOK_one c289)) (chunksOK_append (chunksOK_one c290) (chunksOK_one c291))) (chunksOK_append (chunksOK_append (chunksOK_one c292) (chunksOK_one c293)) (chunksOK_append (chunksOK_one c294) (chunksOK_one c295)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c296) (chunksOK_one c297)) (chunksOK_append (chunksOK_one c298) (chunksOK_one c299))) (chunksOK_append (chunksOK_append (chunksOK_one c300) (chunksOK_one c301)) (chunksOK_append (chunksOK_one c302) (chunksOK_one c303)))))

end C18

namespace C19

theorem c304 : check 60 115 18 304 = true := by decide +kernel
theorem c305 : check 60 115 18 305 = true := by decide +kernel
theorem c306 : check 60 115 18 306 = true := by decide +kernel
theorem c307 : check 60 115 18 307 = true := by decide +kernel
theorem c308 : check 60 115 18 308 = true := by decide +kernel
theorem c309 : check 60 115 18 309 = true := by decide +kernel
theorem c310 : check 60 115 18 310 = true := by decide +kernel
theorem c311 : check 60 115 18 311 = true := by decide +kernel
theorem c312 : check 60 115 18 312 = true := by decide +kernel
theorem c313 : check 60 115 18 313 = true := by decide +kernel
theorem c314 : check 60 115 18 314 = true := by decide +kernel
theorem c315 : check 60 115 18 315 = true := by decide +kernel
theorem c316 : check 60 115 18 316 = true := by decide +kernel
theorem c317 : check 60 115 18 317 = true := by decide +kernel
theorem c318 : check 60 115 18 318 = true := by decide +kernel
theorem c319 : check 60 115 18 319 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 304 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c304) (chunksOK_one c305)) (chunksOK_append (chunksOK_one c306) (chunksOK_one c307))) (chunksOK_append (chunksOK_append (chunksOK_one c308) (chunksOK_one c309)) (chunksOK_append (chunksOK_one c310) (chunksOK_one c311)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c312) (chunksOK_one c313)) (chunksOK_append (chunksOK_one c314) (chunksOK_one c315))) (chunksOK_append (chunksOK_append (chunksOK_one c316) (chunksOK_one c317)) (chunksOK_append (chunksOK_one c318) (chunksOK_one c319)))))

end C19

namespace C20

theorem c320 : check 60 115 18 320 = true := by decide +kernel
theorem c321 : check 60 115 18 321 = true := by decide +kernel
theorem c322 : check 60 115 18 322 = true := by decide +kernel
theorem c323 : check 60 115 18 323 = true := by decide +kernel
theorem c324 : check 60 115 18 324 = true := by decide +kernel
theorem c325 : check 60 115 18 325 = true := by decide +kernel
theorem c326 : check 60 115 18 326 = true := by decide +kernel
theorem c327 : check 60 115 18 327 = true := by decide +kernel
theorem c328 : check 60 115 18 328 = true := by decide +kernel
theorem c329 : check 60 115 18 329 = true := by decide +kernel
theorem c330 : check 60 115 18 330 = true := by decide +kernel
theorem c331 : check 60 115 18 331 = true := by decide +kernel
theorem c332 : check 60 115 18 332 = true := by decide +kernel
theorem c333 : check 60 115 18 333 = true := by decide +kernel
theorem c334 : check 60 115 18 334 = true := by decide +kernel
theorem c335 : check 60 115 18 335 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 320 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c320) (chunksOK_one c321)) (chunksOK_append (chunksOK_one c322) (chunksOK_one c323))) (chunksOK_append (chunksOK_append (chunksOK_one c324) (chunksOK_one c325)) (chunksOK_append (chunksOK_one c326) (chunksOK_one c327)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c328) (chunksOK_one c329)) (chunksOK_append (chunksOK_one c330) (chunksOK_one c331))) (chunksOK_append (chunksOK_append (chunksOK_one c332) (chunksOK_one c333)) (chunksOK_append (chunksOK_one c334) (chunksOK_one c335)))))

end C20

namespace C21

theorem c336 : check 60 115 18 336 = true := by decide +kernel
theorem c337 : check 60 115 18 337 = true := by decide +kernel
theorem c338 : check 60 115 18 338 = true := by decide +kernel
theorem c339 : check 60 115 18 339 = true := by decide +kernel
theorem c340 : check 60 115 18 340 = true := by decide +kernel
theorem c341 : check 60 115 18 341 = true := by decide +kernel
theorem c342 : check 60 115 18 342 = true := by decide +kernel
theorem c343 : check 60 115 18 343 = true := by decide +kernel
theorem c344 : check 60 115 18 344 = true := by decide +kernel
theorem c345 : check 60 115 18 345 = true := by decide +kernel
theorem c346 : check 60 115 18 346 = true := by decide +kernel
theorem c347 : check 60 115 18 347 = true := by decide +kernel
theorem c348 : check 60 115 18 348 = true := by decide +kernel
theorem c349 : check 60 115 18 349 = true := by decide +kernel
theorem c350 : check 60 115 18 350 = true := by decide +kernel
theorem c351 : check 60 115 18 351 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 336 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c336) (chunksOK_one c337)) (chunksOK_append (chunksOK_one c338) (chunksOK_one c339))) (chunksOK_append (chunksOK_append (chunksOK_one c340) (chunksOK_one c341)) (chunksOK_append (chunksOK_one c342) (chunksOK_one c343)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c344) (chunksOK_one c345)) (chunksOK_append (chunksOK_one c346) (chunksOK_one c347))) (chunksOK_append (chunksOK_append (chunksOK_one c348) (chunksOK_one c349)) (chunksOK_append (chunksOK_one c350) (chunksOK_one c351)))))

end C21

namespace C22

theorem c352 : check 60 115 18 352 = true := by decide +kernel
theorem c353 : check 60 115 18 353 = true := by decide +kernel
theorem c354 : check 60 115 18 354 = true := by decide +kernel
theorem c355 : check 60 115 18 355 = true := by decide +kernel
theorem c356 : check 60 115 18 356 = true := by decide +kernel
theorem c357 : check 60 115 18 357 = true := by decide +kernel
theorem c358 : check 60 115 18 358 = true := by decide +kernel
theorem c359 : check 60 115 18 359 = true := by decide +kernel
theorem c360 : check 60 115 18 360 = true := by decide +kernel
theorem c361 : check 60 115 18 361 = true := by decide +kernel
theorem c362 : check 60 115 18 362 = true := by decide +kernel
theorem c363 : check 60 115 18 363 = true := by decide +kernel
theorem c364 : check 60 115 18 364 = true := by decide +kernel
theorem c365 : check 60 115 18 365 = true := by decide +kernel
theorem c366 : check 60 115 18 366 = true := by decide +kernel
theorem c367 : check 60 115 18 367 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 352 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c352) (chunksOK_one c353)) (chunksOK_append (chunksOK_one c354) (chunksOK_one c355))) (chunksOK_append (chunksOK_append (chunksOK_one c356) (chunksOK_one c357)) (chunksOK_append (chunksOK_one c358) (chunksOK_one c359)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c360) (chunksOK_one c361)) (chunksOK_append (chunksOK_one c362) (chunksOK_one c363))) (chunksOK_append (chunksOK_append (chunksOK_one c364) (chunksOK_one c365)) (chunksOK_append (chunksOK_one c366) (chunksOK_one c367)))))

end C22

namespace C23

theorem c368 : check 60 115 18 368 = true := by decide +kernel
theorem c369 : check 60 115 18 369 = true := by decide +kernel
theorem c370 : check 60 115 18 370 = true := by decide +kernel
theorem c371 : check 60 115 18 371 = true := by decide +kernel
theorem c372 : check 60 115 18 372 = true := by decide +kernel
theorem c373 : check 60 115 18 373 = true := by decide +kernel
theorem c374 : check 60 115 18 374 = true := by decide +kernel
theorem c375 : check 60 115 18 375 = true := by decide +kernel
theorem c376 : check 60 115 18 376 = true := by decide +kernel
theorem c377 : check 60 115 18 377 = true := by decide +kernel
theorem c378 : check 60 115 18 378 = true := by decide +kernel
theorem c379 : check 60 115 18 379 = true := by decide +kernel
theorem c380 : check 60 115 18 380 = true := by decide +kernel
theorem c381 : check 60 115 18 381 = true := by decide +kernel
theorem c382 : check 60 115 18 382 = true := by decide +kernel
theorem c383 : check 60 115 18 383 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 368 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c368) (chunksOK_one c369)) (chunksOK_append (chunksOK_one c370) (chunksOK_one c371))) (chunksOK_append (chunksOK_append (chunksOK_one c372) (chunksOK_one c373)) (chunksOK_append (chunksOK_one c374) (chunksOK_one c375)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c376) (chunksOK_one c377)) (chunksOK_append (chunksOK_one c378) (chunksOK_one c379))) (chunksOK_append (chunksOK_append (chunksOK_one c380) (chunksOK_one c381)) (chunksOK_append (chunksOK_one c382) (chunksOK_one c383)))))

end C23

namespace C24

theorem c384 : check 60 115 18 384 = true := by decide +kernel
theorem c385 : check 60 115 18 385 = true := by decide +kernel
theorem c386 : check 60 115 18 386 = true := by decide +kernel
theorem c387 : check 60 115 18 387 = true := by decide +kernel
theorem c388 : check 60 115 18 388 = true := by decide +kernel
theorem c389 : check 60 115 18 389 = true := by decide +kernel
theorem c390 : check 60 115 18 390 = true := by decide +kernel
theorem c391 : check 60 115 18 391 = true := by decide +kernel
theorem c392 : check 60 115 18 392 = true := by decide +kernel
theorem c393 : check 60 115 18 393 = true := by decide +kernel
theorem c394 : check 60 115 18 394 = true := by decide +kernel
theorem c395 : check 60 115 18 395 = true := by decide +kernel
theorem c396 : check 60 115 18 396 = true := by decide +kernel
theorem c397 : check 60 115 18 397 = true := by decide +kernel
theorem c398 : check 60 115 18 398 = true := by decide +kernel
theorem c399 : check 60 115 18 399 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 384 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c384) (chunksOK_one c385)) (chunksOK_append (chunksOK_one c386) (chunksOK_one c387))) (chunksOK_append (chunksOK_append (chunksOK_one c388) (chunksOK_one c389)) (chunksOK_append (chunksOK_one c390) (chunksOK_one c391)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c392) (chunksOK_one c393)) (chunksOK_append (chunksOK_one c394) (chunksOK_one c395))) (chunksOK_append (chunksOK_append (chunksOK_one c396) (chunksOK_one c397)) (chunksOK_append (chunksOK_one c398) (chunksOK_one c399)))))

end C24

namespace C25

theorem c400 : check 60 115 18 400 = true := by decide +kernel
theorem c401 : check 60 115 18 401 = true := by decide +kernel
theorem c402 : check 60 115 18 402 = true := by decide +kernel
theorem c403 : check 60 115 18 403 = true := by decide +kernel
theorem c404 : check 60 115 18 404 = true := by decide +kernel
theorem c405 : check 60 115 18 405 = true := by decide +kernel
theorem c406 : check 60 115 18 406 = true := by decide +kernel
theorem c407 : check 60 115 18 407 = true := by decide +kernel
theorem c408 : check 60 115 18 408 = true := by decide +kernel
theorem c409 : check 60 115 18 409 = true := by decide +kernel
theorem c410 : check 60 115 18 410 = true := by decide +kernel
theorem c411 : check 60 115 18 411 = true := by decide +kernel
theorem c412 : check 60 115 18 412 = true := by decide +kernel
theorem c413 : check 60 115 18 413 = true := by decide +kernel
theorem c414 : check 60 115 18 414 = true := by decide +kernel
theorem c415 : check 60 115 18 415 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 400 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c400) (chunksOK_one c401)) (chunksOK_append (chunksOK_one c402) (chunksOK_one c403))) (chunksOK_append (chunksOK_append (chunksOK_one c404) (chunksOK_one c405)) (chunksOK_append (chunksOK_one c406) (chunksOK_one c407)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c408) (chunksOK_one c409)) (chunksOK_append (chunksOK_one c410) (chunksOK_one c411))) (chunksOK_append (chunksOK_append (chunksOK_one c412) (chunksOK_one c413)) (chunksOK_append (chunksOK_one c414) (chunksOK_one c415)))))

end C25

namespace C26

theorem c416 : check 60 115 18 416 = true := by decide +kernel
theorem c417 : check 60 115 18 417 = true := by decide +kernel
theorem c418 : check 60 115 18 418 = true := by decide +kernel
theorem c419 : check 60 115 18 419 = true := by decide +kernel
theorem c420 : check 60 115 18 420 = true := by decide +kernel
theorem c421 : check 60 115 18 421 = true := by decide +kernel
theorem c422 : check 60 115 18 422 = true := by decide +kernel
theorem c423 : check 60 115 18 423 = true := by decide +kernel
theorem c424 : check 60 115 18 424 = true := by decide +kernel
theorem c425 : check 60 115 18 425 = true := by decide +kernel
theorem c426 : check 60 115 18 426 = true := by decide +kernel
theorem c427 : check 60 115 18 427 = true := by decide +kernel
theorem c428 : check 60 115 18 428 = true := by decide +kernel
theorem c429 : check 60 115 18 429 = true := by decide +kernel
theorem c430 : check 60 115 18 430 = true := by decide +kernel
theorem c431 : check 60 115 18 431 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 416 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c416) (chunksOK_one c417)) (chunksOK_append (chunksOK_one c418) (chunksOK_one c419))) (chunksOK_append (chunksOK_append (chunksOK_one c420) (chunksOK_one c421)) (chunksOK_append (chunksOK_one c422) (chunksOK_one c423)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c424) (chunksOK_one c425)) (chunksOK_append (chunksOK_one c426) (chunksOK_one c427))) (chunksOK_append (chunksOK_append (chunksOK_one c428) (chunksOK_one c429)) (chunksOK_append (chunksOK_one c430) (chunksOK_one c431)))))

end C26

namespace C27

theorem c432 : check 60 115 18 432 = true := by decide +kernel
theorem c433 : check 60 115 18 433 = true := by decide +kernel
theorem c434 : check 60 115 18 434 = true := by decide +kernel
theorem c435 : check 60 115 18 435 = true := by decide +kernel
theorem c436 : check 60 115 18 436 = true := by decide +kernel
theorem c437 : check 60 115 18 437 = true := by decide +kernel
theorem c438 : check 60 115 18 438 = true := by decide +kernel
theorem c439 : check 60 115 18 439 = true := by decide +kernel
theorem c440 : check 60 115 18 440 = true := by decide +kernel
theorem c441 : check 60 115 18 441 = true := by decide +kernel
theorem c442 : check 60 115 18 442 = true := by decide +kernel
theorem c443 : check 60 115 18 443 = true := by decide +kernel
theorem c444 : check 60 115 18 444 = true := by decide +kernel
theorem c445 : check 60 115 18 445 = true := by decide +kernel
theorem c446 : check 60 115 18 446 = true := by decide +kernel
theorem c447 : check 60 115 18 447 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 432 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c432) (chunksOK_one c433)) (chunksOK_append (chunksOK_one c434) (chunksOK_one c435))) (chunksOK_append (chunksOK_append (chunksOK_one c436) (chunksOK_one c437)) (chunksOK_append (chunksOK_one c438) (chunksOK_one c439)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c440) (chunksOK_one c441)) (chunksOK_append (chunksOK_one c442) (chunksOK_one c443))) (chunksOK_append (chunksOK_append (chunksOK_one c444) (chunksOK_one c445)) (chunksOK_append (chunksOK_one c446) (chunksOK_one c447)))))

end C27

namespace C28

theorem c448 : check 60 115 18 448 = true := by decide +kernel
theorem c449 : check 60 115 18 449 = true := by decide +kernel
theorem c450 : check 60 115 18 450 = true := by decide +kernel
theorem c451 : check 60 115 18 451 = true := by decide +kernel
theorem c452 : check 60 115 18 452 = true := by decide +kernel
theorem c453 : check 60 115 18 453 = true := by decide +kernel
theorem c454 : check 60 115 18 454 = true := by decide +kernel
theorem c455 : check 60 115 18 455 = true := by decide +kernel
theorem c456 : check 60 115 18 456 = true := by decide +kernel
theorem c457 : check 60 115 18 457 = true := by decide +kernel
theorem c458 : check 60 115 18 458 = true := by decide +kernel
theorem c459 : check 60 115 18 459 = true := by decide +kernel
theorem c460 : check 60 115 18 460 = true := by decide +kernel
theorem c461 : check 60 115 18 461 = true := by decide +kernel
theorem c462 : check 60 115 18 462 = true := by decide +kernel
theorem c463 : check 60 115 18 463 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 448 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c448) (chunksOK_one c449)) (chunksOK_append (chunksOK_one c450) (chunksOK_one c451))) (chunksOK_append (chunksOK_append (chunksOK_one c452) (chunksOK_one c453)) (chunksOK_append (chunksOK_one c454) (chunksOK_one c455)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c456) (chunksOK_one c457)) (chunksOK_append (chunksOK_one c458) (chunksOK_one c459))) (chunksOK_append (chunksOK_append (chunksOK_one c460) (chunksOK_one c461)) (chunksOK_append (chunksOK_one c462) (chunksOK_one c463)))))

end C28

namespace C29

theorem c464 : check 60 115 18 464 = true := by decide +kernel
theorem c465 : check 60 115 18 465 = true := by decide +kernel
theorem c466 : check 60 115 18 466 = true := by decide +kernel
theorem c467 : check 60 115 18 467 = true := by decide +kernel
theorem c468 : check 60 115 18 468 = true := by decide +kernel
theorem c469 : check 60 115 18 469 = true := by decide +kernel
theorem c470 : check 60 115 18 470 = true := by decide +kernel
theorem c471 : check 60 115 18 471 = true := by decide +kernel
theorem c472 : check 60 115 18 472 = true := by decide +kernel
theorem c473 : check 60 115 18 473 = true := by decide +kernel
theorem c474 : check 60 115 18 474 = true := by decide +kernel
theorem c475 : check 60 115 18 475 = true := by decide +kernel
theorem c476 : check 60 115 18 476 = true := by decide +kernel
theorem c477 : check 60 115 18 477 = true := by decide +kernel
theorem c478 : check 60 115 18 478 = true := by decide +kernel
theorem c479 : check 60 115 18 479 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 464 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c464) (chunksOK_one c465)) (chunksOK_append (chunksOK_one c466) (chunksOK_one c467))) (chunksOK_append (chunksOK_append (chunksOK_one c468) (chunksOK_one c469)) (chunksOK_append (chunksOK_one c470) (chunksOK_one c471)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c472) (chunksOK_one c473)) (chunksOK_append (chunksOK_one c474) (chunksOK_one c475))) (chunksOK_append (chunksOK_append (chunksOK_one c476) (chunksOK_one c477)) (chunksOK_append (chunksOK_one c478) (chunksOK_one c479)))))

end C29

namespace C30

theorem c480 : check 60 115 18 480 = true := by decide +kernel
theorem c481 : check 60 115 18 481 = true := by decide +kernel
theorem c482 : check 60 115 18 482 = true := by decide +kernel
theorem c483 : check 60 115 18 483 = true := by decide +kernel
theorem c484 : check 60 115 18 484 = true := by decide +kernel
theorem c485 : check 60 115 18 485 = true := by decide +kernel
theorem c486 : check 60 115 18 486 = true := by decide +kernel
theorem c487 : check 60 115 18 487 = true := by decide +kernel
theorem c488 : check 60 115 18 488 = true := by decide +kernel
theorem c489 : check 60 115 18 489 = true := by decide +kernel
theorem c490 : check 60 115 18 490 = true := by decide +kernel
theorem c491 : check 60 115 18 491 = true := by decide +kernel
theorem c492 : check 60 115 18 492 = true := by decide +kernel
theorem c493 : check 60 115 18 493 = true := by decide +kernel
theorem c494 : check 60 115 18 494 = true := by decide +kernel
theorem c495 : check 60 115 18 495 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 480 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c480) (chunksOK_one c481)) (chunksOK_append (chunksOK_one c482) (chunksOK_one c483))) (chunksOK_append (chunksOK_append (chunksOK_one c484) (chunksOK_one c485)) (chunksOK_append (chunksOK_one c486) (chunksOK_one c487)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c488) (chunksOK_one c489)) (chunksOK_append (chunksOK_one c490) (chunksOK_one c491))) (chunksOK_append (chunksOK_append (chunksOK_one c492) (chunksOK_one c493)) (chunksOK_append (chunksOK_one c494) (chunksOK_one c495)))))

end C30

namespace C31

theorem c496 : check 60 115 18 496 = true := by decide +kernel
theorem c497 : check 60 115 18 497 = true := by decide +kernel
theorem c498 : check 60 115 18 498 = true := by decide +kernel
theorem c499 : check 60 115 18 499 = true := by decide +kernel
theorem c500 : check 60 115 18 500 = true := by decide +kernel
theorem c501 : check 60 115 18 501 = true := by decide +kernel
theorem c502 : check 60 115 18 502 = true := by decide +kernel
theorem c503 : check 60 115 18 503 = true := by decide +kernel
theorem c504 : check 60 115 18 504 = true := by decide +kernel
theorem c505 : check 60 115 18 505 = true := by decide +kernel
theorem c506 : check 60 115 18 506 = true := by decide +kernel
theorem c507 : check 60 115 18 507 = true := by decide +kernel
theorem c508 : check 60 115 18 508 = true := by decide +kernel
theorem c509 : check 60 115 18 509 = true := by decide +kernel
theorem c510 : check 60 115 18 510 = true := by decide +kernel
theorem c511 : check 60 115 18 511 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 496 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c496) (chunksOK_one c497)) (chunksOK_append (chunksOK_one c498) (chunksOK_one c499))) (chunksOK_append (chunksOK_append (chunksOK_one c500) (chunksOK_one c501)) (chunksOK_append (chunksOK_one c502) (chunksOK_one c503)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c504) (chunksOK_one c505)) (chunksOK_append (chunksOK_one c506) (chunksOK_one c507))) (chunksOK_append (chunksOK_append (chunksOK_one c508) (chunksOK_one c509)) (chunksOK_append (chunksOK_one c510) (chunksOK_one c511)))))

end C31

namespace C32

theorem c512 : check 60 115 18 512 = true := by decide +kernel
theorem c513 : check 60 115 18 513 = true := by decide +kernel
theorem c514 : check 60 115 18 514 = true := by decide +kernel
theorem c515 : check 60 115 18 515 = true := by decide +kernel
theorem c516 : check 60 115 18 516 = true := by decide +kernel
theorem c517 : check 60 115 18 517 = true := by decide +kernel
theorem c518 : check 60 115 18 518 = true := by decide +kernel
theorem c519 : check 60 115 18 519 = true := by decide +kernel
theorem c520 : check 60 115 18 520 = true := by decide +kernel
theorem c521 : check 60 115 18 521 = true := by decide +kernel
theorem c522 : check 60 115 18 522 = true := by decide +kernel
theorem c523 : check 60 115 18 523 = true := by decide +kernel
theorem c524 : check 60 115 18 524 = true := by decide +kernel
theorem c525 : check 60 115 18 525 = true := by decide +kernel
theorem c526 : check 60 115 18 526 = true := by decide +kernel
theorem c527 : check 60 115 18 527 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 512 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c512) (chunksOK_one c513)) (chunksOK_append (chunksOK_one c514) (chunksOK_one c515))) (chunksOK_append (chunksOK_append (chunksOK_one c516) (chunksOK_one c517)) (chunksOK_append (chunksOK_one c518) (chunksOK_one c519)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c520) (chunksOK_one c521)) (chunksOK_append (chunksOK_one c522) (chunksOK_one c523))) (chunksOK_append (chunksOK_append (chunksOK_one c524) (chunksOK_one c525)) (chunksOK_append (chunksOK_one c526) (chunksOK_one c527)))))

end C32

namespace C33

theorem c528 : check 60 115 18 528 = true := by decide +kernel
theorem c529 : check 60 115 18 529 = true := by decide +kernel
theorem c530 : check 60 115 18 530 = true := by decide +kernel
theorem c531 : check 60 115 18 531 = true := by decide +kernel
theorem c532 : check 60 115 18 532 = true := by decide +kernel
theorem c533 : check 60 115 18 533 = true := by decide +kernel
theorem c534 : check 60 115 18 534 = true := by decide +kernel
theorem c535 : check 60 115 18 535 = true := by decide +kernel
theorem c536 : check 60 115 18 536 = true := by decide +kernel
theorem c537 : check 60 115 18 537 = true := by decide +kernel
theorem c538 : check 60 115 18 538 = true := by decide +kernel
theorem c539 : check 60 115 18 539 = true := by decide +kernel
theorem c540 : check 60 115 18 540 = true := by decide +kernel
theorem c541 : check 60 115 18 541 = true := by decide +kernel
theorem c542 : check 60 115 18 542 = true := by decide +kernel
theorem c543 : check 60 115 18 543 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 528 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c528) (chunksOK_one c529)) (chunksOK_append (chunksOK_one c530) (chunksOK_one c531))) (chunksOK_append (chunksOK_append (chunksOK_one c532) (chunksOK_one c533)) (chunksOK_append (chunksOK_one c534) (chunksOK_one c535)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c536) (chunksOK_one c537)) (chunksOK_append (chunksOK_one c538) (chunksOK_one c539))) (chunksOK_append (chunksOK_append (chunksOK_one c540) (chunksOK_one c541)) (chunksOK_append (chunksOK_one c542) (chunksOK_one c543)))))

end C33

namespace C34

theorem c544 : check 60 115 18 544 = true := by decide +kernel
theorem c545 : check 60 115 18 545 = true := by decide +kernel
theorem c546 : check 60 115 18 546 = true := by decide +kernel
theorem c547 : check 60 115 18 547 = true := by decide +kernel
theorem c548 : check 60 115 18 548 = true := by decide +kernel
theorem c549 : check 60 115 18 549 = true := by decide +kernel
theorem c550 : check 60 115 18 550 = true := by decide +kernel
theorem c551 : check 60 115 18 551 = true := by decide +kernel
theorem c552 : check 60 115 18 552 = true := by decide +kernel
theorem c553 : check 60 115 18 553 = true := by decide +kernel
theorem c554 : check 60 115 18 554 = true := by decide +kernel
theorem c555 : check 60 115 18 555 = true := by decide +kernel
theorem c556 : check 60 115 18 556 = true := by decide +kernel
theorem c557 : check 60 115 18 557 = true := by decide +kernel
theorem c558 : check 60 115 18 558 = true := by decide +kernel
theorem c559 : check 60 115 18 559 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 544 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c544) (chunksOK_one c545)) (chunksOK_append (chunksOK_one c546) (chunksOK_one c547))) (chunksOK_append (chunksOK_append (chunksOK_one c548) (chunksOK_one c549)) (chunksOK_append (chunksOK_one c550) (chunksOK_one c551)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c552) (chunksOK_one c553)) (chunksOK_append (chunksOK_one c554) (chunksOK_one c555))) (chunksOK_append (chunksOK_append (chunksOK_one c556) (chunksOK_one c557)) (chunksOK_append (chunksOK_one c558) (chunksOK_one c559)))))

end C34

namespace C35

theorem c560 : check 60 115 18 560 = true := by decide +kernel
theorem c561 : check 60 115 18 561 = true := by decide +kernel
theorem c562 : check 60 115 18 562 = true := by decide +kernel
theorem c563 : check 60 115 18 563 = true := by decide +kernel
theorem c564 : check 60 115 18 564 = true := by decide +kernel
theorem c565 : check 60 115 18 565 = true := by decide +kernel
theorem c566 : check 60 115 18 566 = true := by decide +kernel
theorem c567 : check 60 115 18 567 = true := by decide +kernel
theorem c568 : check 60 115 18 568 = true := by decide +kernel
theorem c569 : check 60 115 18 569 = true := by decide +kernel
theorem c570 : check 60 115 18 570 = true := by decide +kernel
theorem c571 : check 60 115 18 571 = true := by decide +kernel
theorem c572 : check 60 115 18 572 = true := by decide +kernel
theorem c573 : check 60 115 18 573 = true := by decide +kernel
theorem c574 : check 60 115 18 574 = true := by decide +kernel
theorem c575 : check 60 115 18 575 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 560 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c560) (chunksOK_one c561)) (chunksOK_append (chunksOK_one c562) (chunksOK_one c563))) (chunksOK_append (chunksOK_append (chunksOK_one c564) (chunksOK_one c565)) (chunksOK_append (chunksOK_one c566) (chunksOK_one c567)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c568) (chunksOK_one c569)) (chunksOK_append (chunksOK_one c570) (chunksOK_one c571))) (chunksOK_append (chunksOK_append (chunksOK_one c572) (chunksOK_one c573)) (chunksOK_append (chunksOK_one c574) (chunksOK_one c575)))))

end C35

namespace C36

theorem c576 : check 60 115 18 576 = true := by decide +kernel
theorem c577 : check 60 115 18 577 = true := by decide +kernel
theorem c578 : check 60 115 18 578 = true := by decide +kernel
theorem c579 : check 60 115 18 579 = true := by decide +kernel
theorem c580 : check 60 115 18 580 = true := by decide +kernel
theorem c581 : check 60 115 18 581 = true := by decide +kernel
theorem c582 : check 60 115 18 582 = true := by decide +kernel
theorem c583 : check 60 115 18 583 = true := by decide +kernel
theorem c584 : check 60 115 18 584 = true := by decide +kernel
theorem c585 : check 60 115 18 585 = true := by decide +kernel
theorem c586 : check 60 115 18 586 = true := by decide +kernel
theorem c587 : check 60 115 18 587 = true := by decide +kernel
theorem c588 : check 60 115 18 588 = true := by decide +kernel
theorem c589 : check 60 115 18 589 = true := by decide +kernel
theorem c590 : check 60 115 18 590 = true := by decide +kernel
theorem c591 : check 60 115 18 591 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 576 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c576) (chunksOK_one c577)) (chunksOK_append (chunksOK_one c578) (chunksOK_one c579))) (chunksOK_append (chunksOK_append (chunksOK_one c580) (chunksOK_one c581)) (chunksOK_append (chunksOK_one c582) (chunksOK_one c583)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c584) (chunksOK_one c585)) (chunksOK_append (chunksOK_one c586) (chunksOK_one c587))) (chunksOK_append (chunksOK_append (chunksOK_one c588) (chunksOK_one c589)) (chunksOK_append (chunksOK_one c590) (chunksOK_one c591)))))

end C36

namespace C37

theorem c592 : check 60 115 18 592 = true := by decide +kernel
theorem c593 : check 60 115 18 593 = true := by decide +kernel
theorem c594 : check 60 115 18 594 = true := by decide +kernel
theorem c595 : check 60 115 18 595 = true := by decide +kernel
theorem c596 : check 60 115 18 596 = true := by decide +kernel
theorem c597 : check 60 115 18 597 = true := by decide +kernel
theorem c598 : check 60 115 18 598 = true := by decide +kernel
theorem c599 : check 60 115 18 599 = true := by decide +kernel
theorem c600 : check 60 115 18 600 = true := by decide +kernel
theorem c601 : check 60 115 18 601 = true := by decide +kernel
theorem c602 : check 60 115 18 602 = true := by decide +kernel
theorem c603 : check 60 115 18 603 = true := by decide +kernel
theorem c604 : check 60 115 18 604 = true := by decide +kernel
theorem c605 : check 60 115 18 605 = true := by decide +kernel
theorem c606 : check 60 115 18 606 = true := by decide +kernel
theorem c607 : check 60 115 18 607 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 592 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c592) (chunksOK_one c593)) (chunksOK_append (chunksOK_one c594) (chunksOK_one c595))) (chunksOK_append (chunksOK_append (chunksOK_one c596) (chunksOK_one c597)) (chunksOK_append (chunksOK_one c598) (chunksOK_one c599)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c600) (chunksOK_one c601)) (chunksOK_append (chunksOK_one c602) (chunksOK_one c603))) (chunksOK_append (chunksOK_append (chunksOK_one c604) (chunksOK_one c605)) (chunksOK_append (chunksOK_one c606) (chunksOK_one c607)))))

end C37

namespace C38

theorem c608 : check 60 115 18 608 = true := by decide +kernel
theorem c609 : check 60 115 18 609 = true := by decide +kernel
theorem c610 : check 60 115 18 610 = true := by decide +kernel
theorem c611 : check 60 115 18 611 = true := by decide +kernel
theorem c612 : check 60 115 18 612 = true := by decide +kernel
theorem c613 : check 60 115 18 613 = true := by decide +kernel
theorem c614 : check 60 115 18 614 = true := by decide +kernel
theorem c615 : check 60 115 18 615 = true := by decide +kernel
theorem c616 : check 60 115 18 616 = true := by decide +kernel
theorem c617 : check 60 115 18 617 = true := by decide +kernel
theorem c618 : check 60 115 18 618 = true := by decide +kernel
theorem c619 : check 60 115 18 619 = true := by decide +kernel
theorem c620 : check 60 115 18 620 = true := by decide +kernel
theorem c621 : check 60 115 18 621 = true := by decide +kernel
theorem c622 : check 60 115 18 622 = true := by decide +kernel
theorem c623 : check 60 115 18 623 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 608 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c608) (chunksOK_one c609)) (chunksOK_append (chunksOK_one c610) (chunksOK_one c611))) (chunksOK_append (chunksOK_append (chunksOK_one c612) (chunksOK_one c613)) (chunksOK_append (chunksOK_one c614) (chunksOK_one c615)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c616) (chunksOK_one c617)) (chunksOK_append (chunksOK_one c618) (chunksOK_one c619))) (chunksOK_append (chunksOK_append (chunksOK_one c620) (chunksOK_one c621)) (chunksOK_append (chunksOK_one c622) (chunksOK_one c623)))))

end C38

namespace C39

theorem c624 : check 60 115 18 624 = true := by decide +kernel
theorem c625 : check 60 115 18 625 = true := by decide +kernel
theorem c626 : check 60 115 18 626 = true := by decide +kernel
theorem c627 : check 60 115 18 627 = true := by decide +kernel
theorem c628 : check 60 115 18 628 = true := by decide +kernel
theorem c629 : check 60 115 18 629 = true := by decide +kernel
theorem c630 : check 60 115 18 630 = true := by decide +kernel
theorem c631 : check 60 115 18 631 = true := by decide +kernel
theorem c632 : check 60 115 18 632 = true := by decide +kernel
theorem c633 : check 60 115 18 633 = true := by decide +kernel
theorem c634 : check 60 115 18 634 = true := by decide +kernel
theorem c635 : check 60 115 18 635 = true := by decide +kernel
theorem c636 : check 60 115 18 636 = true := by decide +kernel
theorem c637 : check 60 115 18 637 = true := by decide +kernel
theorem c638 : check 60 115 18 638 = true := by decide +kernel
theorem c639 : check 60 115 18 639 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 624 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c624) (chunksOK_one c625)) (chunksOK_append (chunksOK_one c626) (chunksOK_one c627))) (chunksOK_append (chunksOK_append (chunksOK_one c628) (chunksOK_one c629)) (chunksOK_append (chunksOK_one c630) (chunksOK_one c631)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c632) (chunksOK_one c633)) (chunksOK_append (chunksOK_one c634) (chunksOK_one c635))) (chunksOK_append (chunksOK_append (chunksOK_one c636) (chunksOK_one c637)) (chunksOK_append (chunksOK_one c638) (chunksOK_one c639)))))

end C39

namespace C40

theorem c640 : check 60 115 18 640 = true := by decide +kernel
theorem c641 : check 60 115 18 641 = true := by decide +kernel
theorem c642 : check 60 115 18 642 = true := by decide +kernel
theorem c643 : check 60 115 18 643 = true := by decide +kernel
theorem c644 : check 60 115 18 644 = true := by decide +kernel
theorem c645 : check 60 115 18 645 = true := by decide +kernel
theorem c646 : check 60 115 18 646 = true := by decide +kernel
theorem c647 : check 60 115 18 647 = true := by decide +kernel
theorem c648 : check 60 115 18 648 = true := by decide +kernel
theorem c649 : check 60 115 18 649 = true := by decide +kernel
theorem c650 : check 60 115 18 650 = true := by decide +kernel
theorem c651 : check 60 115 18 651 = true := by decide +kernel
theorem c652 : check 60 115 18 652 = true := by decide +kernel
theorem c653 : check 60 115 18 653 = true := by decide +kernel
theorem c654 : check 60 115 18 654 = true := by decide +kernel
theorem c655 : check 60 115 18 655 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 640 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c640) (chunksOK_one c641)) (chunksOK_append (chunksOK_one c642) (chunksOK_one c643))) (chunksOK_append (chunksOK_append (chunksOK_one c644) (chunksOK_one c645)) (chunksOK_append (chunksOK_one c646) (chunksOK_one c647)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c648) (chunksOK_one c649)) (chunksOK_append (chunksOK_one c650) (chunksOK_one c651))) (chunksOK_append (chunksOK_append (chunksOK_one c652) (chunksOK_one c653)) (chunksOK_append (chunksOK_one c654) (chunksOK_one c655)))))

end C40

namespace C41

theorem c656 : check 60 115 18 656 = true := by decide +kernel
theorem c657 : check 60 115 18 657 = true := by decide +kernel
theorem c658 : check 60 115 18 658 = true := by decide +kernel
theorem c659 : check 60 115 18 659 = true := by decide +kernel
theorem c660 : check 60 115 18 660 = true := by decide +kernel
theorem c661 : check 60 115 18 661 = true := by decide +kernel
theorem c662 : check 60 115 18 662 = true := by decide +kernel
theorem c663 : check 60 115 18 663 = true := by decide +kernel
theorem c664 : check 60 115 18 664 = true := by decide +kernel
theorem c665 : check 60 115 18 665 = true := by decide +kernel
theorem c666 : check 60 115 18 666 = true := by decide +kernel
theorem c667 : check 60 115 18 667 = true := by decide +kernel
theorem c668 : check 60 115 18 668 = true := by decide +kernel
theorem c669 : check 60 115 18 669 = true := by decide +kernel
theorem c670 : check 60 115 18 670 = true := by decide +kernel
theorem c671 : check 60 115 18 671 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 656 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c656) (chunksOK_one c657)) (chunksOK_append (chunksOK_one c658) (chunksOK_one c659))) (chunksOK_append (chunksOK_append (chunksOK_one c660) (chunksOK_one c661)) (chunksOK_append (chunksOK_one c662) (chunksOK_one c663)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c664) (chunksOK_one c665)) (chunksOK_append (chunksOK_one c666) (chunksOK_one c667))) (chunksOK_append (chunksOK_append (chunksOK_one c668) (chunksOK_one c669)) (chunksOK_append (chunksOK_one c670) (chunksOK_one c671)))))

end C41

namespace C42

theorem c672 : check 60 115 18 672 = true := by decide +kernel
theorem c673 : check 60 115 18 673 = true := by decide +kernel
theorem c674 : check 60 115 18 674 = true := by decide +kernel
theorem c675 : check 60 115 18 675 = true := by decide +kernel
theorem c676 : check 60 115 18 676 = true := by decide +kernel
theorem c677 : check 60 115 18 677 = true := by decide +kernel
theorem c678 : check 60 115 18 678 = true := by decide +kernel
theorem c679 : check 60 115 18 679 = true := by decide +kernel
theorem c680 : check 60 115 18 680 = true := by decide +kernel
theorem c681 : check 60 115 18 681 = true := by decide +kernel
theorem c682 : check 60 115 18 682 = true := by decide +kernel
theorem c683 : check 60 115 18 683 = true := by decide +kernel
theorem c684 : check 60 115 18 684 = true := by decide +kernel
theorem c685 : check 60 115 18 685 = true := by decide +kernel
theorem c686 : check 60 115 18 686 = true := by decide +kernel
theorem c687 : check 60 115 18 687 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 672 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c672) (chunksOK_one c673)) (chunksOK_append (chunksOK_one c674) (chunksOK_one c675))) (chunksOK_append (chunksOK_append (chunksOK_one c676) (chunksOK_one c677)) (chunksOK_append (chunksOK_one c678) (chunksOK_one c679)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c680) (chunksOK_one c681)) (chunksOK_append (chunksOK_one c682) (chunksOK_one c683))) (chunksOK_append (chunksOK_append (chunksOK_one c684) (chunksOK_one c685)) (chunksOK_append (chunksOK_one c686) (chunksOK_one c687)))))

end C42

namespace C43

theorem c688 : check 60 115 18 688 = true := by decide +kernel
theorem c689 : check 60 115 18 689 = true := by decide +kernel
theorem c690 : check 60 115 18 690 = true := by decide +kernel
theorem c691 : check 60 115 18 691 = true := by decide +kernel
theorem c692 : check 60 115 18 692 = true := by decide +kernel
theorem c693 : check 60 115 18 693 = true := by decide +kernel
theorem c694 : check 60 115 18 694 = true := by decide +kernel
theorem c695 : check 60 115 18 695 = true := by decide +kernel
theorem c696 : check 60 115 18 696 = true := by decide +kernel
theorem c697 : check 60 115 18 697 = true := by decide +kernel
theorem c698 : check 60 115 18 698 = true := by decide +kernel
theorem c699 : check 60 115 18 699 = true := by decide +kernel
theorem c700 : check 60 115 18 700 = true := by decide +kernel
theorem c701 : check 60 115 18 701 = true := by decide +kernel
theorem c702 : check 60 115 18 702 = true := by decide +kernel
theorem c703 : check 60 115 18 703 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 688 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c688) (chunksOK_one c689)) (chunksOK_append (chunksOK_one c690) (chunksOK_one c691))) (chunksOK_append (chunksOK_append (chunksOK_one c692) (chunksOK_one c693)) (chunksOK_append (chunksOK_one c694) (chunksOK_one c695)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c696) (chunksOK_one c697)) (chunksOK_append (chunksOK_one c698) (chunksOK_one c699))) (chunksOK_append (chunksOK_append (chunksOK_one c700) (chunksOK_one c701)) (chunksOK_append (chunksOK_one c702) (chunksOK_one c703)))))

end C43

namespace C44

theorem c704 : check 60 115 18 704 = true := by decide +kernel
theorem c705 : check 60 115 18 705 = true := by decide +kernel
theorem c706 : check 60 115 18 706 = true := by decide +kernel
theorem c707 : check 60 115 18 707 = true := by decide +kernel
theorem c708 : check 60 115 18 708 = true := by decide +kernel
theorem c709 : check 60 115 18 709 = true := by decide +kernel
theorem c710 : check 60 115 18 710 = true := by decide +kernel
theorem c711 : check 60 115 18 711 = true := by decide +kernel
theorem c712 : check 60 115 18 712 = true := by decide +kernel
theorem c713 : check 60 115 18 713 = true := by decide +kernel
theorem c714 : check 60 115 18 714 = true := by decide +kernel
theorem c715 : check 60 115 18 715 = true := by decide +kernel
theorem c716 : check 60 115 18 716 = true := by decide +kernel
theorem c717 : check 60 115 18 717 = true := by decide +kernel
theorem c718 : check 60 115 18 718 = true := by decide +kernel
theorem c719 : check 60 115 18 719 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 704 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c704) (chunksOK_one c705)) (chunksOK_append (chunksOK_one c706) (chunksOK_one c707))) (chunksOK_append (chunksOK_append (chunksOK_one c708) (chunksOK_one c709)) (chunksOK_append (chunksOK_one c710) (chunksOK_one c711)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c712) (chunksOK_one c713)) (chunksOK_append (chunksOK_one c714) (chunksOK_one c715))) (chunksOK_append (chunksOK_append (chunksOK_one c716) (chunksOK_one c717)) (chunksOK_append (chunksOK_one c718) (chunksOK_one c719)))))

end C44

namespace C45

theorem c720 : check 60 115 18 720 = true := by decide +kernel
theorem c721 : check 60 115 18 721 = true := by decide +kernel
theorem c722 : check 60 115 18 722 = true := by decide +kernel
theorem c723 : check 60 115 18 723 = true := by decide +kernel
theorem c724 : check 60 115 18 724 = true := by decide +kernel
theorem c725 : check 60 115 18 725 = true := by decide +kernel
theorem c726 : check 60 115 18 726 = true := by decide +kernel
theorem c727 : check 60 115 18 727 = true := by decide +kernel
theorem c728 : check 60 115 18 728 = true := by decide +kernel
theorem c729 : check 60 115 18 729 = true := by decide +kernel
theorem c730 : check 60 115 18 730 = true := by decide +kernel
theorem c731 : check 60 115 18 731 = true := by decide +kernel
theorem c732 : check 60 115 18 732 = true := by decide +kernel
theorem c733 : check 60 115 18 733 = true := by decide +kernel
theorem c734 : check 60 115 18 734 = true := by decide +kernel
theorem c735 : check 60 115 18 735 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 720 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c720) (chunksOK_one c721)) (chunksOK_append (chunksOK_one c722) (chunksOK_one c723))) (chunksOK_append (chunksOK_append (chunksOK_one c724) (chunksOK_one c725)) (chunksOK_append (chunksOK_one c726) (chunksOK_one c727)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c728) (chunksOK_one c729)) (chunksOK_append (chunksOK_one c730) (chunksOK_one c731))) (chunksOK_append (chunksOK_append (chunksOK_one c732) (chunksOK_one c733)) (chunksOK_append (chunksOK_one c734) (chunksOK_one c735)))))

end C45

namespace C46

theorem c736 : check 60 115 18 736 = true := by decide +kernel
theorem c737 : check 60 115 18 737 = true := by decide +kernel
theorem c738 : check 60 115 18 738 = true := by decide +kernel
theorem c739 : check 60 115 18 739 = true := by decide +kernel
theorem c740 : check 60 115 18 740 = true := by decide +kernel
theorem c741 : check 60 115 18 741 = true := by decide +kernel
theorem c742 : check 60 115 18 742 = true := by decide +kernel
theorem c743 : check 60 115 18 743 = true := by decide +kernel
theorem c744 : check 60 115 18 744 = true := by decide +kernel
theorem c745 : check 60 115 18 745 = true := by decide +kernel
theorem c746 : check 60 115 18 746 = true := by decide +kernel
theorem c747 : check 60 115 18 747 = true := by decide +kernel
theorem c748 : check 60 115 18 748 = true := by decide +kernel
theorem c749 : check 60 115 18 749 = true := by decide +kernel
theorem c750 : check 60 115 18 750 = true := by decide +kernel
theorem c751 : check 60 115 18 751 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 736 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c736) (chunksOK_one c737)) (chunksOK_append (chunksOK_one c738) (chunksOK_one c739))) (chunksOK_append (chunksOK_append (chunksOK_one c740) (chunksOK_one c741)) (chunksOK_append (chunksOK_one c742) (chunksOK_one c743)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c744) (chunksOK_one c745)) (chunksOK_append (chunksOK_one c746) (chunksOK_one c747))) (chunksOK_append (chunksOK_append (chunksOK_one c748) (chunksOK_one c749)) (chunksOK_append (chunksOK_one c750) (chunksOK_one c751)))))

end C46

namespace C47

theorem c752 : check 60 115 18 752 = true := by decide +kernel
theorem c753 : check 60 115 18 753 = true := by decide +kernel
theorem c754 : check 60 115 18 754 = true := by decide +kernel
theorem c755 : check 60 115 18 755 = true := by decide +kernel
theorem c756 : check 60 115 18 756 = true := by decide +kernel
theorem c757 : check 60 115 18 757 = true := by decide +kernel
theorem c758 : check 60 115 18 758 = true := by decide +kernel
theorem c759 : check 60 115 18 759 = true := by decide +kernel
theorem c760 : check 60 115 18 760 = true := by decide +kernel
theorem c761 : check 60 115 18 761 = true := by decide +kernel
theorem c762 : check 60 115 18 762 = true := by decide +kernel
theorem c763 : check 60 115 18 763 = true := by decide +kernel
theorem c764 : check 60 115 18 764 = true := by decide +kernel
theorem c765 : check 60 115 18 765 = true := by decide +kernel
theorem c766 : check 60 115 18 766 = true := by decide +kernel
theorem c767 : check 60 115 18 767 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 752 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c752) (chunksOK_one c753)) (chunksOK_append (chunksOK_one c754) (chunksOK_one c755))) (chunksOK_append (chunksOK_append (chunksOK_one c756) (chunksOK_one c757)) (chunksOK_append (chunksOK_one c758) (chunksOK_one c759)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c760) (chunksOK_one c761)) (chunksOK_append (chunksOK_one c762) (chunksOK_one c763))) (chunksOK_append (chunksOK_append (chunksOK_one c764) (chunksOK_one c765)) (chunksOK_append (chunksOK_one c766) (chunksOK_one c767)))))

end C47

namespace C48

theorem c768 : check 60 115 18 768 = true := by decide +kernel
theorem c769 : check 60 115 18 769 = true := by decide +kernel
theorem c770 : check 60 115 18 770 = true := by decide +kernel
theorem c771 : check 60 115 18 771 = true := by decide +kernel
theorem c772 : check 60 115 18 772 = true := by decide +kernel
theorem c773 : check 60 115 18 773 = true := by decide +kernel
theorem c774 : check 60 115 18 774 = true := by decide +kernel
theorem c775 : check 60 115 18 775 = true := by decide +kernel
theorem c776 : check 60 115 18 776 = true := by decide +kernel
theorem c777 : check 60 115 18 777 = true := by decide +kernel
theorem c778 : check 60 115 18 778 = true := by decide +kernel
theorem c779 : check 60 115 18 779 = true := by decide +kernel
theorem c780 : check 60 115 18 780 = true := by decide +kernel
theorem c781 : check 60 115 18 781 = true := by decide +kernel
theorem c782 : check 60 115 18 782 = true := by decide +kernel
theorem c783 : check 60 115 18 783 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 768 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c768) (chunksOK_one c769)) (chunksOK_append (chunksOK_one c770) (chunksOK_one c771))) (chunksOK_append (chunksOK_append (chunksOK_one c772) (chunksOK_one c773)) (chunksOK_append (chunksOK_one c774) (chunksOK_one c775)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c776) (chunksOK_one c777)) (chunksOK_append (chunksOK_one c778) (chunksOK_one c779))) (chunksOK_append (chunksOK_append (chunksOK_one c780) (chunksOK_one c781)) (chunksOK_append (chunksOK_one c782) (chunksOK_one c783)))))

end C48

namespace C49

theorem c784 : check 60 115 18 784 = true := by decide +kernel
theorem c785 : check 60 115 18 785 = true := by decide +kernel
theorem c786 : check 60 115 18 786 = true := by decide +kernel
theorem c787 : check 60 115 18 787 = true := by decide +kernel
theorem c788 : check 60 115 18 788 = true := by decide +kernel
theorem c789 : check 60 115 18 789 = true := by decide +kernel
theorem c790 : check 60 115 18 790 = true := by decide +kernel
theorem c791 : check 60 115 18 791 = true := by decide +kernel
theorem c792 : check 60 115 18 792 = true := by decide +kernel
theorem c793 : check 60 115 18 793 = true := by decide +kernel
theorem c794 : check 60 115 18 794 = true := by decide +kernel
theorem c795 : check 60 115 18 795 = true := by decide +kernel
theorem c796 : check 60 115 18 796 = true := by decide +kernel
theorem c797 : check 60 115 18 797 = true := by decide +kernel
theorem c798 : check 60 115 18 798 = true := by decide +kernel
theorem c799 : check 60 115 18 799 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 784 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c784) (chunksOK_one c785)) (chunksOK_append (chunksOK_one c786) (chunksOK_one c787))) (chunksOK_append (chunksOK_append (chunksOK_one c788) (chunksOK_one c789)) (chunksOK_append (chunksOK_one c790) (chunksOK_one c791)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c792) (chunksOK_one c793)) (chunksOK_append (chunksOK_one c794) (chunksOK_one c795))) (chunksOK_append (chunksOK_append (chunksOK_one c796) (chunksOK_one c797)) (chunksOK_append (chunksOK_one c798) (chunksOK_one c799)))))

end C49

namespace C50

theorem c800 : check 60 115 18 800 = true := by decide +kernel
theorem c801 : check 60 115 18 801 = true := by decide +kernel
theorem c802 : check 60 115 18 802 = true := by decide +kernel
theorem c803 : check 60 115 18 803 = true := by decide +kernel
theorem c804 : check 60 115 18 804 = true := by decide +kernel
theorem c805 : check 60 115 18 805 = true := by decide +kernel
theorem c806 : check 60 115 18 806 = true := by decide +kernel
theorem c807 : check 60 115 18 807 = true := by decide +kernel
theorem c808 : check 60 115 18 808 = true := by decide +kernel
theorem c809 : check 60 115 18 809 = true := by decide +kernel
theorem c810 : check 60 115 18 810 = true := by decide +kernel
theorem c811 : check 60 115 18 811 = true := by decide +kernel
theorem c812 : check 60 115 18 812 = true := by decide +kernel
theorem c813 : check 60 115 18 813 = true := by decide +kernel
theorem c814 : check 60 115 18 814 = true := by decide +kernel
theorem c815 : check 60 115 18 815 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 800 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c800) (chunksOK_one c801)) (chunksOK_append (chunksOK_one c802) (chunksOK_one c803))) (chunksOK_append (chunksOK_append (chunksOK_one c804) (chunksOK_one c805)) (chunksOK_append (chunksOK_one c806) (chunksOK_one c807)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c808) (chunksOK_one c809)) (chunksOK_append (chunksOK_one c810) (chunksOK_one c811))) (chunksOK_append (chunksOK_append (chunksOK_one c812) (chunksOK_one c813)) (chunksOK_append (chunksOK_one c814) (chunksOK_one c815)))))

end C50

namespace C51

theorem c816 : check 60 115 18 816 = true := by decide +kernel
theorem c817 : check 60 115 18 817 = true := by decide +kernel
theorem c818 : check 60 115 18 818 = true := by decide +kernel
theorem c819 : check 60 115 18 819 = true := by decide +kernel
theorem c820 : check 60 115 18 820 = true := by decide +kernel
theorem c821 : check 60 115 18 821 = true := by decide +kernel
theorem c822 : check 60 115 18 822 = true := by decide +kernel
theorem c823 : check 60 115 18 823 = true := by decide +kernel
theorem c824 : check 60 115 18 824 = true := by decide +kernel
theorem c825 : check 60 115 18 825 = true := by decide +kernel
theorem c826 : check 60 115 18 826 = true := by decide +kernel
theorem c827 : check 60 115 18 827 = true := by decide +kernel
theorem c828 : check 60 115 18 828 = true := by decide +kernel
theorem c829 : check 60 115 18 829 = true := by decide +kernel
theorem c830 : check 60 115 18 830 = true := by decide +kernel
theorem c831 : check 60 115 18 831 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 816 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c816) (chunksOK_one c817)) (chunksOK_append (chunksOK_one c818) (chunksOK_one c819))) (chunksOK_append (chunksOK_append (chunksOK_one c820) (chunksOK_one c821)) (chunksOK_append (chunksOK_one c822) (chunksOK_one c823)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c824) (chunksOK_one c825)) (chunksOK_append (chunksOK_one c826) (chunksOK_one c827))) (chunksOK_append (chunksOK_append (chunksOK_one c828) (chunksOK_one c829)) (chunksOK_append (chunksOK_one c830) (chunksOK_one c831)))))

end C51

namespace C52

theorem c832 : check 60 115 18 832 = true := by decide +kernel
theorem c833 : check 60 115 18 833 = true := by decide +kernel
theorem c834 : check 60 115 18 834 = true := by decide +kernel
theorem c835 : check 60 115 18 835 = true := by decide +kernel
theorem c836 : check 60 115 18 836 = true := by decide +kernel
theorem c837 : check 60 115 18 837 = true := by decide +kernel
theorem c838 : check 60 115 18 838 = true := by decide +kernel
theorem c839 : check 60 115 18 839 = true := by decide +kernel
theorem c840 : check 60 115 18 840 = true := by decide +kernel
theorem c841 : check 60 115 18 841 = true := by decide +kernel
theorem c842 : check 60 115 18 842 = true := by decide +kernel
theorem c843 : check 60 115 18 843 = true := by decide +kernel
theorem c844 : check 60 115 18 844 = true := by decide +kernel
theorem c845 : check 60 115 18 845 = true := by decide +kernel
theorem c846 : check 60 115 18 846 = true := by decide +kernel
theorem c847 : check 60 115 18 847 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 832 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c832) (chunksOK_one c833)) (chunksOK_append (chunksOK_one c834) (chunksOK_one c835))) (chunksOK_append (chunksOK_append (chunksOK_one c836) (chunksOK_one c837)) (chunksOK_append (chunksOK_one c838) (chunksOK_one c839)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c840) (chunksOK_one c841)) (chunksOK_append (chunksOK_one c842) (chunksOK_one c843))) (chunksOK_append (chunksOK_append (chunksOK_one c844) (chunksOK_one c845)) (chunksOK_append (chunksOK_one c846) (chunksOK_one c847)))))

end C52

namespace C53

theorem c848 : check 60 115 18 848 = true := by decide +kernel
theorem c849 : check 60 115 18 849 = true := by decide +kernel
theorem c850 : check 60 115 18 850 = true := by decide +kernel
theorem c851 : check 60 115 18 851 = true := by decide +kernel
theorem c852 : check 60 115 18 852 = true := by decide +kernel
theorem c853 : check 60 115 18 853 = true := by decide +kernel
theorem c854 : check 60 115 18 854 = true := by decide +kernel
theorem c855 : check 60 115 18 855 = true := by decide +kernel
theorem c856 : check 60 115 18 856 = true := by decide +kernel
theorem c857 : check 60 115 18 857 = true := by decide +kernel
theorem c858 : check 60 115 18 858 = true := by decide +kernel
theorem c859 : check 60 115 18 859 = true := by decide +kernel
theorem c860 : check 60 115 18 860 = true := by decide +kernel
theorem c861 : check 60 115 18 861 = true := by decide +kernel
theorem c862 : check 60 115 18 862 = true := by decide +kernel
theorem c863 : check 60 115 18 863 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 848 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c848) (chunksOK_one c849)) (chunksOK_append (chunksOK_one c850) (chunksOK_one c851))) (chunksOK_append (chunksOK_append (chunksOK_one c852) (chunksOK_one c853)) (chunksOK_append (chunksOK_one c854) (chunksOK_one c855)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c856) (chunksOK_one c857)) (chunksOK_append (chunksOK_one c858) (chunksOK_one c859))) (chunksOK_append (chunksOK_append (chunksOK_one c860) (chunksOK_one c861)) (chunksOK_append (chunksOK_one c862) (chunksOK_one c863)))))

end C53

namespace C54

theorem c864 : check 60 115 18 864 = true := by decide +kernel
theorem c865 : check 60 115 18 865 = true := by decide +kernel
theorem c866 : check 60 115 18 866 = true := by decide +kernel
theorem c867 : check 60 115 18 867 = true := by decide +kernel
theorem c868 : check 60 115 18 868 = true := by decide +kernel
theorem c869 : check 60 115 18 869 = true := by decide +kernel
theorem c870 : check 60 115 18 870 = true := by decide +kernel
theorem c871 : check 60 115 18 871 = true := by decide +kernel
theorem c872 : check 60 115 18 872 = true := by decide +kernel
theorem c873 : check 60 115 18 873 = true := by decide +kernel
theorem c874 : check 60 115 18 874 = true := by decide +kernel
theorem c875 : check 60 115 18 875 = true := by decide +kernel
theorem c876 : check 60 115 18 876 = true := by decide +kernel
theorem c877 : check 60 115 18 877 = true := by decide +kernel
theorem c878 : check 60 115 18 878 = true := by decide +kernel
theorem c879 : check 60 115 18 879 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 864 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c864) (chunksOK_one c865)) (chunksOK_append (chunksOK_one c866) (chunksOK_one c867))) (chunksOK_append (chunksOK_append (chunksOK_one c868) (chunksOK_one c869)) (chunksOK_append (chunksOK_one c870) (chunksOK_one c871)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c872) (chunksOK_one c873)) (chunksOK_append (chunksOK_one c874) (chunksOK_one c875))) (chunksOK_append (chunksOK_append (chunksOK_one c876) (chunksOK_one c877)) (chunksOK_append (chunksOK_one c878) (chunksOK_one c879)))))

end C54

namespace C55

theorem c880 : check 60 115 18 880 = true := by decide +kernel
theorem c881 : check 60 115 18 881 = true := by decide +kernel
theorem c882 : check 60 115 18 882 = true := by decide +kernel
theorem c883 : check 60 115 18 883 = true := by decide +kernel
theorem c884 : check 60 115 18 884 = true := by decide +kernel
theorem c885 : check 60 115 18 885 = true := by decide +kernel
theorem c886 : check 60 115 18 886 = true := by decide +kernel
theorem c887 : check 60 115 18 887 = true := by decide +kernel
theorem c888 : check 60 115 18 888 = true := by decide +kernel
theorem c889 : check 60 115 18 889 = true := by decide +kernel
theorem c890 : check 60 115 18 890 = true := by decide +kernel
theorem c891 : check 60 115 18 891 = true := by decide +kernel
theorem c892 : check 60 115 18 892 = true := by decide +kernel
theorem c893 : check 60 115 18 893 = true := by decide +kernel
theorem c894 : check 60 115 18 894 = true := by decide +kernel
theorem c895 : check 60 115 18 895 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 880 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c880) (chunksOK_one c881)) (chunksOK_append (chunksOK_one c882) (chunksOK_one c883))) (chunksOK_append (chunksOK_append (chunksOK_one c884) (chunksOK_one c885)) (chunksOK_append (chunksOK_one c886) (chunksOK_one c887)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c888) (chunksOK_one c889)) (chunksOK_append (chunksOK_one c890) (chunksOK_one c891))) (chunksOK_append (chunksOK_append (chunksOK_one c892) (chunksOK_one c893)) (chunksOK_append (chunksOK_one c894) (chunksOK_one c895)))))

end C55

namespace C56

theorem c896 : check 60 115 18 896 = true := by decide +kernel
theorem c897 : check 60 115 18 897 = true := by decide +kernel
theorem c898 : check 60 115 18 898 = true := by decide +kernel
theorem c899 : check 60 115 18 899 = true := by decide +kernel
theorem c900 : check 60 115 18 900 = true := by decide +kernel
theorem c901 : check 60 115 18 901 = true := by decide +kernel
theorem c902 : check 60 115 18 902 = true := by decide +kernel
theorem c903 : check 60 115 18 903 = true := by decide +kernel
theorem c904 : check 60 115 18 904 = true := by decide +kernel
theorem c905 : check 60 115 18 905 = true := by decide +kernel
theorem c906 : check 60 115 18 906 = true := by decide +kernel
theorem c907 : check 60 115 18 907 = true := by decide +kernel
theorem c908 : check 60 115 18 908 = true := by decide +kernel
theorem c909 : check 60 115 18 909 = true := by decide +kernel
theorem c910 : check 60 115 18 910 = true := by decide +kernel
theorem c911 : check 60 115 18 911 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 896 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c896) (chunksOK_one c897)) (chunksOK_append (chunksOK_one c898) (chunksOK_one c899))) (chunksOK_append (chunksOK_append (chunksOK_one c900) (chunksOK_one c901)) (chunksOK_append (chunksOK_one c902) (chunksOK_one c903)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c904) (chunksOK_one c905)) (chunksOK_append (chunksOK_one c906) (chunksOK_one c907))) (chunksOK_append (chunksOK_append (chunksOK_one c908) (chunksOK_one c909)) (chunksOK_append (chunksOK_one c910) (chunksOK_one c911)))))

end C56

namespace C57

theorem c912 : check 60 115 18 912 = true := by decide +kernel
theorem c913 : check 60 115 18 913 = true := by decide +kernel
theorem c914 : check 60 115 18 914 = true := by decide +kernel
theorem c915 : check 60 115 18 915 = true := by decide +kernel
theorem c916 : check 60 115 18 916 = true := by decide +kernel
theorem c917 : check 60 115 18 917 = true := by decide +kernel
theorem c918 : check 60 115 18 918 = true := by decide +kernel
theorem c919 : check 60 115 18 919 = true := by decide +kernel
theorem c920 : check 60 115 18 920 = true := by decide +kernel
theorem c921 : check 60 115 18 921 = true := by decide +kernel
theorem c922 : check 60 115 18 922 = true := by decide +kernel
theorem c923 : check 60 115 18 923 = true := by decide +kernel
theorem c924 : check 60 115 18 924 = true := by decide +kernel
theorem c925 : check 60 115 18 925 = true := by decide +kernel
theorem c926 : check 60 115 18 926 = true := by decide +kernel
theorem c927 : check 60 115 18 927 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 912 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c912) (chunksOK_one c913)) (chunksOK_append (chunksOK_one c914) (chunksOK_one c915))) (chunksOK_append (chunksOK_append (chunksOK_one c916) (chunksOK_one c917)) (chunksOK_append (chunksOK_one c918) (chunksOK_one c919)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c920) (chunksOK_one c921)) (chunksOK_append (chunksOK_one c922) (chunksOK_one c923))) (chunksOK_append (chunksOK_append (chunksOK_one c924) (chunksOK_one c925)) (chunksOK_append (chunksOK_one c926) (chunksOK_one c927)))))

end C57

namespace C58

theorem c928 : check 60 115 18 928 = true := by decide +kernel
theorem c929 : check 60 115 18 929 = true := by decide +kernel
theorem c930 : check 60 115 18 930 = true := by decide +kernel
theorem c931 : check 60 115 18 931 = true := by decide +kernel
theorem c932 : check 60 115 18 932 = true := by decide +kernel
theorem c933 : check 60 115 18 933 = true := by decide +kernel
theorem c934 : check 60 115 18 934 = true := by decide +kernel
theorem c935 : check 60 115 18 935 = true := by decide +kernel
theorem c936 : check 60 115 18 936 = true := by decide +kernel
theorem c937 : check 60 115 18 937 = true := by decide +kernel
theorem c938 : check 60 115 18 938 = true := by decide +kernel
theorem c939 : check 60 115 18 939 = true := by decide +kernel
theorem c940 : check 60 115 18 940 = true := by decide +kernel
theorem c941 : check 60 115 18 941 = true := by decide +kernel
theorem c942 : check 60 115 18 942 = true := by decide +kernel
theorem c943 : check 60 115 18 943 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 928 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c928) (chunksOK_one c929)) (chunksOK_append (chunksOK_one c930) (chunksOK_one c931))) (chunksOK_append (chunksOK_append (chunksOK_one c932) (chunksOK_one c933)) (chunksOK_append (chunksOK_one c934) (chunksOK_one c935)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c936) (chunksOK_one c937)) (chunksOK_append (chunksOK_one c938) (chunksOK_one c939))) (chunksOK_append (chunksOK_append (chunksOK_one c940) (chunksOK_one c941)) (chunksOK_append (chunksOK_one c942) (chunksOK_one c943)))))

end C58

namespace C59

theorem c944 : check 60 115 18 944 = true := by decide +kernel
theorem c945 : check 60 115 18 945 = true := by decide +kernel
theorem c946 : check 60 115 18 946 = true := by decide +kernel
theorem c947 : check 60 115 18 947 = true := by decide +kernel
theorem c948 : check 60 115 18 948 = true := by decide +kernel
theorem c949 : check 60 115 18 949 = true := by decide +kernel
theorem c950 : check 60 115 18 950 = true := by decide +kernel
theorem c951 : check 60 115 18 951 = true := by decide +kernel
theorem c952 : check 60 115 18 952 = true := by decide +kernel
theorem c953 : check 60 115 18 953 = true := by decide +kernel
theorem c954 : check 60 115 18 954 = true := by decide +kernel
theorem c955 : check 60 115 18 955 = true := by decide +kernel
theorem c956 : check 60 115 18 956 = true := by decide +kernel
theorem c957 : check 60 115 18 957 = true := by decide +kernel
theorem c958 : check 60 115 18 958 = true := by decide +kernel
theorem c959 : check 60 115 18 959 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 944 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c944) (chunksOK_one c945)) (chunksOK_append (chunksOK_one c946) (chunksOK_one c947))) (chunksOK_append (chunksOK_append (chunksOK_one c948) (chunksOK_one c949)) (chunksOK_append (chunksOK_one c950) (chunksOK_one c951)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c952) (chunksOK_one c953)) (chunksOK_append (chunksOK_one c954) (chunksOK_one c955))) (chunksOK_append (chunksOK_append (chunksOK_one c956) (chunksOK_one c957)) (chunksOK_append (chunksOK_one c958) (chunksOK_one c959)))))

end C59

namespace C60

theorem c960 : check 60 115 18 960 = true := by decide +kernel
theorem c961 : check 60 115 18 961 = true := by decide +kernel
theorem c962 : check 60 115 18 962 = true := by decide +kernel
theorem c963 : check 60 115 18 963 = true := by decide +kernel
theorem c964 : check 60 115 18 964 = true := by decide +kernel
theorem c965 : check 60 115 18 965 = true := by decide +kernel
theorem c966 : check 60 115 18 966 = true := by decide +kernel
theorem c967 : check 60 115 18 967 = true := by decide +kernel
theorem c968 : check 60 115 18 968 = true := by decide +kernel
theorem c969 : check 60 115 18 969 = true := by decide +kernel
theorem c970 : check 60 115 18 970 = true := by decide +kernel
theorem c971 : check 60 115 18 971 = true := by decide +kernel
theorem c972 : check 60 115 18 972 = true := by decide +kernel
theorem c973 : check 60 115 18 973 = true := by decide +kernel
theorem c974 : check 60 115 18 974 = true := by decide +kernel
theorem c975 : check 60 115 18 975 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 960 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c960) (chunksOK_one c961)) (chunksOK_append (chunksOK_one c962) (chunksOK_one c963))) (chunksOK_append (chunksOK_append (chunksOK_one c964) (chunksOK_one c965)) (chunksOK_append (chunksOK_one c966) (chunksOK_one c967)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c968) (chunksOK_one c969)) (chunksOK_append (chunksOK_one c970) (chunksOK_one c971))) (chunksOK_append (chunksOK_append (chunksOK_one c972) (chunksOK_one c973)) (chunksOK_append (chunksOK_one c974) (chunksOK_one c975)))))

end C60

namespace C61

theorem c976 : check 60 115 18 976 = true := by decide +kernel
theorem c977 : check 60 115 18 977 = true := by decide +kernel
theorem c978 : check 60 115 18 978 = true := by decide +kernel
theorem c979 : check 60 115 18 979 = true := by decide +kernel
theorem c980 : check 60 115 18 980 = true := by decide +kernel
theorem c981 : check 60 115 18 981 = true := by decide +kernel
theorem c982 : check 60 115 18 982 = true := by decide +kernel
theorem c983 : check 60 115 18 983 = true := by decide +kernel
theorem c984 : check 60 115 18 984 = true := by decide +kernel
theorem c985 : check 60 115 18 985 = true := by decide +kernel
theorem c986 : check 60 115 18 986 = true := by decide +kernel
theorem c987 : check 60 115 18 987 = true := by decide +kernel
theorem c988 : check 60 115 18 988 = true := by decide +kernel
theorem c989 : check 60 115 18 989 = true := by decide +kernel
theorem c990 : check 60 115 18 990 = true := by decide +kernel
theorem c991 : check 60 115 18 991 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 976 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c976) (chunksOK_one c977)) (chunksOK_append (chunksOK_one c978) (chunksOK_one c979))) (chunksOK_append (chunksOK_append (chunksOK_one c980) (chunksOK_one c981)) (chunksOK_append (chunksOK_one c982) (chunksOK_one c983)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c984) (chunksOK_one c985)) (chunksOK_append (chunksOK_one c986) (chunksOK_one c987))) (chunksOK_append (chunksOK_append (chunksOK_one c988) (chunksOK_one c989)) (chunksOK_append (chunksOK_one c990) (chunksOK_one c991)))))

end C61

namespace C62

theorem c992 : check 60 115 18 992 = true := by decide +kernel
theorem c993 : check 60 115 18 993 = true := by decide +kernel
theorem c994 : check 60 115 18 994 = true := by decide +kernel
theorem c995 : check 60 115 18 995 = true := by decide +kernel
theorem c996 : check 60 115 18 996 = true := by decide +kernel
theorem c997 : check 60 115 18 997 = true := by decide +kernel
theorem c998 : check 60 115 18 998 = true := by decide +kernel
theorem c999 : check 60 115 18 999 = true := by decide +kernel
theorem c1000 : check 60 115 18 1000 = true := by decide +kernel
theorem c1001 : check 60 115 18 1001 = true := by decide +kernel
theorem c1002 : check 60 115 18 1002 = true := by decide +kernel
theorem c1003 : check 60 115 18 1003 = true := by decide +kernel
theorem c1004 : check 60 115 18 1004 = true := by decide +kernel
theorem c1005 : check 60 115 18 1005 = true := by decide +kernel
theorem c1006 : check 60 115 18 1006 = true := by decide +kernel
theorem c1007 : check 60 115 18 1007 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 992 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c992) (chunksOK_one c993)) (chunksOK_append (chunksOK_one c994) (chunksOK_one c995))) (chunksOK_append (chunksOK_append (chunksOK_one c996) (chunksOK_one c997)) (chunksOK_append (chunksOK_one c998) (chunksOK_one c999)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1000) (chunksOK_one c1001)) (chunksOK_append (chunksOK_one c1002) (chunksOK_one c1003))) (chunksOK_append (chunksOK_append (chunksOK_one c1004) (chunksOK_one c1005)) (chunksOK_append (chunksOK_one c1006) (chunksOK_one c1007)))))

end C62

namespace C63

theorem c1008 : check 60 115 18 1008 = true := by decide +kernel
theorem c1009 : check 60 115 18 1009 = true := by decide +kernel
theorem c1010 : check 60 115 18 1010 = true := by decide +kernel
theorem c1011 : check 60 115 18 1011 = true := by decide +kernel
theorem c1012 : check 60 115 18 1012 = true := by decide +kernel
theorem c1013 : check 60 115 18 1013 = true := by decide +kernel
theorem c1014 : check 60 115 18 1014 = true := by decide +kernel
theorem c1015 : check 60 115 18 1015 = true := by decide +kernel
theorem c1016 : check 60 115 18 1016 = true := by decide +kernel
theorem c1017 : check 60 115 18 1017 = true := by decide +kernel
theorem c1018 : check 60 115 18 1018 = true := by decide +kernel
theorem c1019 : check 60 115 18 1019 = true := by decide +kernel
theorem c1020 : check 60 115 18 1020 = true := by decide +kernel
theorem c1021 : check 60 115 18 1021 = true := by decide +kernel
theorem c1022 : check 60 115 18 1022 = true := by decide +kernel
theorem c1023 : check 60 115 18 1023 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1008 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1008) (chunksOK_one c1009)) (chunksOK_append (chunksOK_one c1010) (chunksOK_one c1011))) (chunksOK_append (chunksOK_append (chunksOK_one c1012) (chunksOK_one c1013)) (chunksOK_append (chunksOK_one c1014) (chunksOK_one c1015)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1016) (chunksOK_one c1017)) (chunksOK_append (chunksOK_one c1018) (chunksOK_one c1019))) (chunksOK_append (chunksOK_append (chunksOK_one c1020) (chunksOK_one c1021)) (chunksOK_append (chunksOK_one c1022) (chunksOK_one c1023)))))

end C63

namespace C64

theorem c1024 : check 60 115 18 1024 = true := by decide +kernel
theorem c1025 : check 60 115 18 1025 = true := by decide +kernel
theorem c1026 : check 60 115 18 1026 = true := by decide +kernel
theorem c1027 : check 60 115 18 1027 = true := by decide +kernel
theorem c1028 : check 60 115 18 1028 = true := by decide +kernel
theorem c1029 : check 60 115 18 1029 = true := by decide +kernel
theorem c1030 : check 60 115 18 1030 = true := by decide +kernel
theorem c1031 : check 60 115 18 1031 = true := by decide +kernel
theorem c1032 : check 60 115 18 1032 = true := by decide +kernel
theorem c1033 : check 60 115 18 1033 = true := by decide +kernel
theorem c1034 : check 60 115 18 1034 = true := by decide +kernel
theorem c1035 : check 60 115 18 1035 = true := by decide +kernel
theorem c1036 : check 60 115 18 1036 = true := by decide +kernel
theorem c1037 : check 60 115 18 1037 = true := by decide +kernel
theorem c1038 : check 60 115 18 1038 = true := by decide +kernel
theorem c1039 : check 60 115 18 1039 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1024 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1024) (chunksOK_one c1025)) (chunksOK_append (chunksOK_one c1026) (chunksOK_one c1027))) (chunksOK_append (chunksOK_append (chunksOK_one c1028) (chunksOK_one c1029)) (chunksOK_append (chunksOK_one c1030) (chunksOK_one c1031)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1032) (chunksOK_one c1033)) (chunksOK_append (chunksOK_one c1034) (chunksOK_one c1035))) (chunksOK_append (chunksOK_append (chunksOK_one c1036) (chunksOK_one c1037)) (chunksOK_append (chunksOK_one c1038) (chunksOK_one c1039)))))

end C64

namespace C65

theorem c1040 : check 60 115 18 1040 = true := by decide +kernel
theorem c1041 : check 60 115 18 1041 = true := by decide +kernel
theorem c1042 : check 60 115 18 1042 = true := by decide +kernel
theorem c1043 : check 60 115 18 1043 = true := by decide +kernel
theorem c1044 : check 60 115 18 1044 = true := by decide +kernel
theorem c1045 : check 60 115 18 1045 = true := by decide +kernel
theorem c1046 : check 60 115 18 1046 = true := by decide +kernel
theorem c1047 : check 60 115 18 1047 = true := by decide +kernel
theorem c1048 : check 60 115 18 1048 = true := by decide +kernel
theorem c1049 : check 60 115 18 1049 = true := by decide +kernel
theorem c1050 : check 60 115 18 1050 = true := by decide +kernel
theorem c1051 : check 60 115 18 1051 = true := by decide +kernel
theorem c1052 : check 60 115 18 1052 = true := by decide +kernel
theorem c1053 : check 60 115 18 1053 = true := by decide +kernel
theorem c1054 : check 60 115 18 1054 = true := by decide +kernel
theorem c1055 : check 60 115 18 1055 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1040 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1040) (chunksOK_one c1041)) (chunksOK_append (chunksOK_one c1042) (chunksOK_one c1043))) (chunksOK_append (chunksOK_append (chunksOK_one c1044) (chunksOK_one c1045)) (chunksOK_append (chunksOK_one c1046) (chunksOK_one c1047)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1048) (chunksOK_one c1049)) (chunksOK_append (chunksOK_one c1050) (chunksOK_one c1051))) (chunksOK_append (chunksOK_append (chunksOK_one c1052) (chunksOK_one c1053)) (chunksOK_append (chunksOK_one c1054) (chunksOK_one c1055)))))

end C65

namespace C66

theorem c1056 : check 60 115 18 1056 = true := by decide +kernel
theorem c1057 : check 60 115 18 1057 = true := by decide +kernel
theorem c1058 : check 60 115 18 1058 = true := by decide +kernel
theorem c1059 : check 60 115 18 1059 = true := by decide +kernel
theorem c1060 : check 60 115 18 1060 = true := by decide +kernel
theorem c1061 : check 60 115 18 1061 = true := by decide +kernel
theorem c1062 : check 60 115 18 1062 = true := by decide +kernel
theorem c1063 : check 60 115 18 1063 = true := by decide +kernel
theorem c1064 : check 60 115 18 1064 = true := by decide +kernel
theorem c1065 : check 60 115 18 1065 = true := by decide +kernel
theorem c1066 : check 60 115 18 1066 = true := by decide +kernel
theorem c1067 : check 60 115 18 1067 = true := by decide +kernel
theorem c1068 : check 60 115 18 1068 = true := by decide +kernel
theorem c1069 : check 60 115 18 1069 = true := by decide +kernel
theorem c1070 : check 60 115 18 1070 = true := by decide +kernel
theorem c1071 : check 60 115 18 1071 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1056 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1056) (chunksOK_one c1057)) (chunksOK_append (chunksOK_one c1058) (chunksOK_one c1059))) (chunksOK_append (chunksOK_append (chunksOK_one c1060) (chunksOK_one c1061)) (chunksOK_append (chunksOK_one c1062) (chunksOK_one c1063)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1064) (chunksOK_one c1065)) (chunksOK_append (chunksOK_one c1066) (chunksOK_one c1067))) (chunksOK_append (chunksOK_append (chunksOK_one c1068) (chunksOK_one c1069)) (chunksOK_append (chunksOK_one c1070) (chunksOK_one c1071)))))

end C66

namespace C67

theorem c1072 : check 60 115 18 1072 = true := by decide +kernel
theorem c1073 : check 60 115 18 1073 = true := by decide +kernel
theorem c1074 : check 60 115 18 1074 = true := by decide +kernel
theorem c1075 : check 60 115 18 1075 = true := by decide +kernel
theorem c1076 : check 60 115 18 1076 = true := by decide +kernel
theorem c1077 : check 60 115 18 1077 = true := by decide +kernel
theorem c1078 : check 60 115 18 1078 = true := by decide +kernel
theorem c1079 : check 60 115 18 1079 = true := by decide +kernel
theorem c1080 : check 60 115 18 1080 = true := by decide +kernel
theorem c1081 : check 60 115 18 1081 = true := by decide +kernel
theorem c1082 : check 60 115 18 1082 = true := by decide +kernel
theorem c1083 : check 60 115 18 1083 = true := by decide +kernel
theorem c1084 : check 60 115 18 1084 = true := by decide +kernel
theorem c1085 : check 60 115 18 1085 = true := by decide +kernel
theorem c1086 : check 60 115 18 1086 = true := by decide +kernel
theorem c1087 : check 60 115 18 1087 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1072 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1072) (chunksOK_one c1073)) (chunksOK_append (chunksOK_one c1074) (chunksOK_one c1075))) (chunksOK_append (chunksOK_append (chunksOK_one c1076) (chunksOK_one c1077)) (chunksOK_append (chunksOK_one c1078) (chunksOK_one c1079)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1080) (chunksOK_one c1081)) (chunksOK_append (chunksOK_one c1082) (chunksOK_one c1083))) (chunksOK_append (chunksOK_append (chunksOK_one c1084) (chunksOK_one c1085)) (chunksOK_append (chunksOK_one c1086) (chunksOK_one c1087)))))

end C67

namespace C68

theorem c1088 : check 60 115 18 1088 = true := by decide +kernel
theorem c1089 : check 60 115 18 1089 = true := by decide +kernel
theorem c1090 : check 60 115 18 1090 = true := by decide +kernel
theorem c1091 : check 60 115 18 1091 = true := by decide +kernel
theorem c1092 : check 60 115 18 1092 = true := by decide +kernel
theorem c1093 : check 60 115 18 1093 = true := by decide +kernel
theorem c1094 : check 60 115 18 1094 = true := by decide +kernel
theorem c1095 : check 60 115 18 1095 = true := by decide +kernel
theorem c1096 : check 60 115 18 1096 = true := by decide +kernel
theorem c1097 : check 60 115 18 1097 = true := by decide +kernel
theorem c1098 : check 60 115 18 1098 = true := by decide +kernel
theorem c1099 : check 60 115 18 1099 = true := by decide +kernel
theorem c1100 : check 60 115 18 1100 = true := by decide +kernel
theorem c1101 : check 60 115 18 1101 = true := by decide +kernel
theorem c1102 : check 60 115 18 1102 = true := by decide +kernel
theorem c1103 : check 60 115 18 1103 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1088 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1088) (chunksOK_one c1089)) (chunksOK_append (chunksOK_one c1090) (chunksOK_one c1091))) (chunksOK_append (chunksOK_append (chunksOK_one c1092) (chunksOK_one c1093)) (chunksOK_append (chunksOK_one c1094) (chunksOK_one c1095)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1096) (chunksOK_one c1097)) (chunksOK_append (chunksOK_one c1098) (chunksOK_one c1099))) (chunksOK_append (chunksOK_append (chunksOK_one c1100) (chunksOK_one c1101)) (chunksOK_append (chunksOK_one c1102) (chunksOK_one c1103)))))

end C68

namespace C69

theorem c1104 : check 60 115 18 1104 = true := by decide +kernel
theorem c1105 : check 60 115 18 1105 = true := by decide +kernel
theorem c1106 : check 60 115 18 1106 = true := by decide +kernel
theorem c1107 : check 60 115 18 1107 = true := by decide +kernel
theorem c1108 : check 60 115 18 1108 = true := by decide +kernel
theorem c1109 : check 60 115 18 1109 = true := by decide +kernel
theorem c1110 : check 60 115 18 1110 = true := by decide +kernel
theorem c1111 : check 60 115 18 1111 = true := by decide +kernel
theorem c1112 : check 60 115 18 1112 = true := by decide +kernel
theorem c1113 : check 60 115 18 1113 = true := by decide +kernel
theorem c1114 : check 60 115 18 1114 = true := by decide +kernel
theorem c1115 : check 60 115 18 1115 = true := by decide +kernel
theorem c1116 : check 60 115 18 1116 = true := by decide +kernel
theorem c1117 : check 60 115 18 1117 = true := by decide +kernel
theorem c1118 : check 60 115 18 1118 = true := by decide +kernel
theorem c1119 : check 60 115 18 1119 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1104 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1104) (chunksOK_one c1105)) (chunksOK_append (chunksOK_one c1106) (chunksOK_one c1107))) (chunksOK_append (chunksOK_append (chunksOK_one c1108) (chunksOK_one c1109)) (chunksOK_append (chunksOK_one c1110) (chunksOK_one c1111)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1112) (chunksOK_one c1113)) (chunksOK_append (chunksOK_one c1114) (chunksOK_one c1115))) (chunksOK_append (chunksOK_append (chunksOK_one c1116) (chunksOK_one c1117)) (chunksOK_append (chunksOK_one c1118) (chunksOK_one c1119)))))

end C69

namespace C70

theorem c1120 : check 60 115 18 1120 = true := by decide +kernel
theorem c1121 : check 60 115 18 1121 = true := by decide +kernel
theorem c1122 : check 60 115 18 1122 = true := by decide +kernel
theorem c1123 : check 60 115 18 1123 = true := by decide +kernel
theorem c1124 : check 60 115 18 1124 = true := by decide +kernel
theorem c1125 : check 60 115 18 1125 = true := by decide +kernel
theorem c1126 : check 60 115 18 1126 = true := by decide +kernel
theorem c1127 : check 60 115 18 1127 = true := by decide +kernel
theorem c1128 : check 60 115 18 1128 = true := by decide +kernel
theorem c1129 : check 60 115 18 1129 = true := by decide +kernel
theorem c1130 : check 60 115 18 1130 = true := by decide +kernel
theorem c1131 : check 60 115 18 1131 = true := by decide +kernel
theorem c1132 : check 60 115 18 1132 = true := by decide +kernel
theorem c1133 : check 60 115 18 1133 = true := by decide +kernel
theorem c1134 : check 60 115 18 1134 = true := by decide +kernel
theorem c1135 : check 60 115 18 1135 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1120 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1120) (chunksOK_one c1121)) (chunksOK_append (chunksOK_one c1122) (chunksOK_one c1123))) (chunksOK_append (chunksOK_append (chunksOK_one c1124) (chunksOK_one c1125)) (chunksOK_append (chunksOK_one c1126) (chunksOK_one c1127)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1128) (chunksOK_one c1129)) (chunksOK_append (chunksOK_one c1130) (chunksOK_one c1131))) (chunksOK_append (chunksOK_append (chunksOK_one c1132) (chunksOK_one c1133)) (chunksOK_append (chunksOK_one c1134) (chunksOK_one c1135)))))

end C70

namespace C71

theorem c1136 : check 60 115 18 1136 = true := by decide +kernel
theorem c1137 : check 60 115 18 1137 = true := by decide +kernel
theorem c1138 : check 60 115 18 1138 = true := by decide +kernel
theorem c1139 : check 60 115 18 1139 = true := by decide +kernel
theorem c1140 : check 60 115 18 1140 = true := by decide +kernel
theorem c1141 : check 60 115 18 1141 = true := by decide +kernel
theorem c1142 : check 60 115 18 1142 = true := by decide +kernel
theorem c1143 : check 60 115 18 1143 = true := by decide +kernel
theorem c1144 : check 60 115 18 1144 = true := by decide +kernel
theorem c1145 : check 60 115 18 1145 = true := by decide +kernel
theorem c1146 : check 60 115 18 1146 = true := by decide +kernel
theorem c1147 : check 60 115 18 1147 = true := by decide +kernel
theorem c1148 : check 60 115 18 1148 = true := by decide +kernel
theorem c1149 : check 60 115 18 1149 = true := by decide +kernel
theorem c1150 : check 60 115 18 1150 = true := by decide +kernel
theorem c1151 : check 60 115 18 1151 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1136 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1136) (chunksOK_one c1137)) (chunksOK_append (chunksOK_one c1138) (chunksOK_one c1139))) (chunksOK_append (chunksOK_append (chunksOK_one c1140) (chunksOK_one c1141)) (chunksOK_append (chunksOK_one c1142) (chunksOK_one c1143)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1144) (chunksOK_one c1145)) (chunksOK_append (chunksOK_one c1146) (chunksOK_one c1147))) (chunksOK_append (chunksOK_append (chunksOK_one c1148) (chunksOK_one c1149)) (chunksOK_append (chunksOK_one c1150) (chunksOK_one c1151)))))

end C71

namespace C72

theorem c1152 : check 60 115 18 1152 = true := by decide +kernel
theorem c1153 : check 60 115 18 1153 = true := by decide +kernel
theorem c1154 : check 60 115 18 1154 = true := by decide +kernel
theorem c1155 : check 60 115 18 1155 = true := by decide +kernel
theorem c1156 : check 60 115 18 1156 = true := by decide +kernel
theorem c1157 : check 60 115 18 1157 = true := by decide +kernel
theorem c1158 : check 60 115 18 1158 = true := by decide +kernel
theorem c1159 : check 60 115 18 1159 = true := by decide +kernel
theorem c1160 : check 60 115 18 1160 = true := by decide +kernel
theorem c1161 : check 60 115 18 1161 = true := by decide +kernel
theorem c1162 : check 60 115 18 1162 = true := by decide +kernel
theorem c1163 : check 60 115 18 1163 = true := by decide +kernel
theorem c1164 : check 60 115 18 1164 = true := by decide +kernel
theorem c1165 : check 60 115 18 1165 = true := by decide +kernel
theorem c1166 : check 60 115 18 1166 = true := by decide +kernel
theorem c1167 : check 60 115 18 1167 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1152 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1152) (chunksOK_one c1153)) (chunksOK_append (chunksOK_one c1154) (chunksOK_one c1155))) (chunksOK_append (chunksOK_append (chunksOK_one c1156) (chunksOK_one c1157)) (chunksOK_append (chunksOK_one c1158) (chunksOK_one c1159)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1160) (chunksOK_one c1161)) (chunksOK_append (chunksOK_one c1162) (chunksOK_one c1163))) (chunksOK_append (chunksOK_append (chunksOK_one c1164) (chunksOK_one c1165)) (chunksOK_append (chunksOK_one c1166) (chunksOK_one c1167)))))

end C72

namespace C73

theorem c1168 : check 60 115 18 1168 = true := by decide +kernel
theorem c1169 : check 60 115 18 1169 = true := by decide +kernel
theorem c1170 : check 60 115 18 1170 = true := by decide +kernel
theorem c1171 : check 60 115 18 1171 = true := by decide +kernel
theorem c1172 : check 60 115 18 1172 = true := by decide +kernel
theorem c1173 : check 60 115 18 1173 = true := by decide +kernel
theorem c1174 : check 60 115 18 1174 = true := by decide +kernel
theorem c1175 : check 60 115 18 1175 = true := by decide +kernel
theorem c1176 : check 60 115 18 1176 = true := by decide +kernel
theorem c1177 : check 60 115 18 1177 = true := by decide +kernel
theorem c1178 : check 60 115 18 1178 = true := by decide +kernel
theorem c1179 : check 60 115 18 1179 = true := by decide +kernel
theorem c1180 : check 60 115 18 1180 = true := by decide +kernel
theorem c1181 : check 60 115 18 1181 = true := by decide +kernel
theorem c1182 : check 60 115 18 1182 = true := by decide +kernel
theorem c1183 : check 60 115 18 1183 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1168 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1168) (chunksOK_one c1169)) (chunksOK_append (chunksOK_one c1170) (chunksOK_one c1171))) (chunksOK_append (chunksOK_append (chunksOK_one c1172) (chunksOK_one c1173)) (chunksOK_append (chunksOK_one c1174) (chunksOK_one c1175)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1176) (chunksOK_one c1177)) (chunksOK_append (chunksOK_one c1178) (chunksOK_one c1179))) (chunksOK_append (chunksOK_append (chunksOK_one c1180) (chunksOK_one c1181)) (chunksOK_append (chunksOK_one c1182) (chunksOK_one c1183)))))

end C73

namespace C74

theorem c1184 : check 60 115 18 1184 = true := by decide +kernel
theorem c1185 : check 60 115 18 1185 = true := by decide +kernel
theorem c1186 : check 60 115 18 1186 = true := by decide +kernel
theorem c1187 : check 60 115 18 1187 = true := by decide +kernel
theorem c1188 : check 60 115 18 1188 = true := by decide +kernel
theorem c1189 : check 60 115 18 1189 = true := by decide +kernel
theorem c1190 : check 60 115 18 1190 = true := by decide +kernel
theorem c1191 : check 60 115 18 1191 = true := by decide +kernel
theorem c1192 : check 60 115 18 1192 = true := by decide +kernel
theorem c1193 : check 60 115 18 1193 = true := by decide +kernel
theorem c1194 : check 60 115 18 1194 = true := by decide +kernel
theorem c1195 : check 60 115 18 1195 = true := by decide +kernel
theorem c1196 : check 60 115 18 1196 = true := by decide +kernel
theorem c1197 : check 60 115 18 1197 = true := by decide +kernel
theorem c1198 : check 60 115 18 1198 = true := by decide +kernel
theorem c1199 : check 60 115 18 1199 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1184 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1184) (chunksOK_one c1185)) (chunksOK_append (chunksOK_one c1186) (chunksOK_one c1187))) (chunksOK_append (chunksOK_append (chunksOK_one c1188) (chunksOK_one c1189)) (chunksOK_append (chunksOK_one c1190) (chunksOK_one c1191)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1192) (chunksOK_one c1193)) (chunksOK_append (chunksOK_one c1194) (chunksOK_one c1195))) (chunksOK_append (chunksOK_append (chunksOK_one c1196) (chunksOK_one c1197)) (chunksOK_append (chunksOK_one c1198) (chunksOK_one c1199)))))

end C74

namespace C75

theorem c1200 : check 60 115 18 1200 = true := by decide +kernel
theorem c1201 : check 60 115 18 1201 = true := by decide +kernel
theorem c1202 : check 60 115 18 1202 = true := by decide +kernel
theorem c1203 : check 60 115 18 1203 = true := by decide +kernel
theorem c1204 : check 60 115 18 1204 = true := by decide +kernel
theorem c1205 : check 60 115 18 1205 = true := by decide +kernel
theorem c1206 : check 60 115 18 1206 = true := by decide +kernel
theorem c1207 : check 60 115 18 1207 = true := by decide +kernel
theorem c1208 : check 60 115 18 1208 = true := by decide +kernel
theorem c1209 : check 60 115 18 1209 = true := by decide +kernel
theorem c1210 : check 60 115 18 1210 = true := by decide +kernel
theorem c1211 : check 60 115 18 1211 = true := by decide +kernel
theorem c1212 : check 60 115 18 1212 = true := by decide +kernel
theorem c1213 : check 60 115 18 1213 = true := by decide +kernel
theorem c1214 : check 60 115 18 1214 = true := by decide +kernel
theorem c1215 : check 60 115 18 1215 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1200 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1200) (chunksOK_one c1201)) (chunksOK_append (chunksOK_one c1202) (chunksOK_one c1203))) (chunksOK_append (chunksOK_append (chunksOK_one c1204) (chunksOK_one c1205)) (chunksOK_append (chunksOK_one c1206) (chunksOK_one c1207)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1208) (chunksOK_one c1209)) (chunksOK_append (chunksOK_one c1210) (chunksOK_one c1211))) (chunksOK_append (chunksOK_append (chunksOK_one c1212) (chunksOK_one c1213)) (chunksOK_append (chunksOK_one c1214) (chunksOK_one c1215)))))

end C75

namespace C76

theorem c1216 : check 60 115 18 1216 = true := by decide +kernel
theorem c1217 : check 60 115 18 1217 = true := by decide +kernel
theorem c1218 : check 60 115 18 1218 = true := by decide +kernel
theorem c1219 : check 60 115 18 1219 = true := by decide +kernel
theorem c1220 : check 60 115 18 1220 = true := by decide +kernel
theorem c1221 : check 60 115 18 1221 = true := by decide +kernel
theorem c1222 : check 60 115 18 1222 = true := by decide +kernel
theorem c1223 : check 60 115 18 1223 = true := by decide +kernel
theorem c1224 : check 60 115 18 1224 = true := by decide +kernel
theorem c1225 : check 60 115 18 1225 = true := by decide +kernel
theorem c1226 : check 60 115 18 1226 = true := by decide +kernel
theorem c1227 : check 60 115 18 1227 = true := by decide +kernel
theorem c1228 : check 60 115 18 1228 = true := by decide +kernel
theorem c1229 : check 60 115 18 1229 = true := by decide +kernel
theorem c1230 : check 60 115 18 1230 = true := by decide +kernel
theorem c1231 : check 60 115 18 1231 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1216 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1216) (chunksOK_one c1217)) (chunksOK_append (chunksOK_one c1218) (chunksOK_one c1219))) (chunksOK_append (chunksOK_append (chunksOK_one c1220) (chunksOK_one c1221)) (chunksOK_append (chunksOK_one c1222) (chunksOK_one c1223)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1224) (chunksOK_one c1225)) (chunksOK_append (chunksOK_one c1226) (chunksOK_one c1227))) (chunksOK_append (chunksOK_append (chunksOK_one c1228) (chunksOK_one c1229)) (chunksOK_append (chunksOK_one c1230) (chunksOK_one c1231)))))

end C76

namespace C77

theorem c1232 : check 60 115 18 1232 = true := by decide +kernel
theorem c1233 : check 60 115 18 1233 = true := by decide +kernel
theorem c1234 : check 60 115 18 1234 = true := by decide +kernel
theorem c1235 : check 60 115 18 1235 = true := by decide +kernel
theorem c1236 : check 60 115 18 1236 = true := by decide +kernel
theorem c1237 : check 60 115 18 1237 = true := by decide +kernel
theorem c1238 : check 60 115 18 1238 = true := by decide +kernel
theorem c1239 : check 60 115 18 1239 = true := by decide +kernel
theorem c1240 : check 60 115 18 1240 = true := by decide +kernel
theorem c1241 : check 60 115 18 1241 = true := by decide +kernel
theorem c1242 : check 60 115 18 1242 = true := by decide +kernel
theorem c1243 : check 60 115 18 1243 = true := by decide +kernel
theorem c1244 : check 60 115 18 1244 = true := by decide +kernel
theorem c1245 : check 60 115 18 1245 = true := by decide +kernel
theorem c1246 : check 60 115 18 1246 = true := by decide +kernel
theorem c1247 : check 60 115 18 1247 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1232 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1232) (chunksOK_one c1233)) (chunksOK_append (chunksOK_one c1234) (chunksOK_one c1235))) (chunksOK_append (chunksOK_append (chunksOK_one c1236) (chunksOK_one c1237)) (chunksOK_append (chunksOK_one c1238) (chunksOK_one c1239)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1240) (chunksOK_one c1241)) (chunksOK_append (chunksOK_one c1242) (chunksOK_one c1243))) (chunksOK_append (chunksOK_append (chunksOK_one c1244) (chunksOK_one c1245)) (chunksOK_append (chunksOK_one c1246) (chunksOK_one c1247)))))

end C77

namespace C78

theorem c1248 : check 60 115 18 1248 = true := by decide +kernel
theorem c1249 : check 60 115 18 1249 = true := by decide +kernel
theorem c1250 : check 60 115 18 1250 = true := by decide +kernel
theorem c1251 : check 60 115 18 1251 = true := by decide +kernel
theorem c1252 : check 60 115 18 1252 = true := by decide +kernel
theorem c1253 : check 60 115 18 1253 = true := by decide +kernel
theorem c1254 : check 60 115 18 1254 = true := by decide +kernel
theorem c1255 : check 60 115 18 1255 = true := by decide +kernel
theorem c1256 : check 60 115 18 1256 = true := by decide +kernel
theorem c1257 : check 60 115 18 1257 = true := by decide +kernel
theorem c1258 : check 60 115 18 1258 = true := by decide +kernel
theorem c1259 : check 60 115 18 1259 = true := by decide +kernel
theorem c1260 : check 60 115 18 1260 = true := by decide +kernel
theorem c1261 : check 60 115 18 1261 = true := by decide +kernel
theorem c1262 : check 60 115 18 1262 = true := by decide +kernel
theorem c1263 : check 60 115 18 1263 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1248 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1248) (chunksOK_one c1249)) (chunksOK_append (chunksOK_one c1250) (chunksOK_one c1251))) (chunksOK_append (chunksOK_append (chunksOK_one c1252) (chunksOK_one c1253)) (chunksOK_append (chunksOK_one c1254) (chunksOK_one c1255)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1256) (chunksOK_one c1257)) (chunksOK_append (chunksOK_one c1258) (chunksOK_one c1259))) (chunksOK_append (chunksOK_append (chunksOK_one c1260) (chunksOK_one c1261)) (chunksOK_append (chunksOK_one c1262) (chunksOK_one c1263)))))

end C78

namespace C79

theorem c1264 : check 60 115 18 1264 = true := by decide +kernel
theorem c1265 : check 60 115 18 1265 = true := by decide +kernel
theorem c1266 : check 60 115 18 1266 = true := by decide +kernel
theorem c1267 : check 60 115 18 1267 = true := by decide +kernel
theorem c1268 : check 60 115 18 1268 = true := by decide +kernel
theorem c1269 : check 60 115 18 1269 = true := by decide +kernel
theorem c1270 : check 60 115 18 1270 = true := by decide +kernel
theorem c1271 : check 60 115 18 1271 = true := by decide +kernel
theorem c1272 : check 60 115 18 1272 = true := by decide +kernel
theorem c1273 : check 60 115 18 1273 = true := by decide +kernel
theorem c1274 : check 60 115 18 1274 = true := by decide +kernel
theorem c1275 : check 60 115 18 1275 = true := by decide +kernel
theorem c1276 : check 60 115 18 1276 = true := by decide +kernel
theorem c1277 : check 60 115 18 1277 = true := by decide +kernel
theorem c1278 : check 60 115 18 1278 = true := by decide +kernel
theorem c1279 : check 60 115 18 1279 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1264 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1264) (chunksOK_one c1265)) (chunksOK_append (chunksOK_one c1266) (chunksOK_one c1267))) (chunksOK_append (chunksOK_append (chunksOK_one c1268) (chunksOK_one c1269)) (chunksOK_append (chunksOK_one c1270) (chunksOK_one c1271)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1272) (chunksOK_one c1273)) (chunksOK_append (chunksOK_one c1274) (chunksOK_one c1275))) (chunksOK_append (chunksOK_append (chunksOK_one c1276) (chunksOK_one c1277)) (chunksOK_append (chunksOK_one c1278) (chunksOK_one c1279)))))

end C79

namespace C80

theorem c1280 : check 60 115 18 1280 = true := by decide +kernel
theorem c1281 : check 60 115 18 1281 = true := by decide +kernel
theorem c1282 : check 60 115 18 1282 = true := by decide +kernel
theorem c1283 : check 60 115 18 1283 = true := by decide +kernel
theorem c1284 : check 60 115 18 1284 = true := by decide +kernel
theorem c1285 : check 60 115 18 1285 = true := by decide +kernel
theorem c1286 : check 60 115 18 1286 = true := by decide +kernel
theorem c1287 : check 60 115 18 1287 = true := by decide +kernel
theorem c1288 : check 60 115 18 1288 = true := by decide +kernel
theorem c1289 : check 60 115 18 1289 = true := by decide +kernel
theorem c1290 : check 60 115 18 1290 = true := by decide +kernel
theorem c1291 : check 60 115 18 1291 = true := by decide +kernel
theorem c1292 : check 60 115 18 1292 = true := by decide +kernel
theorem c1293 : check 60 115 18 1293 = true := by decide +kernel
theorem c1294 : check 60 115 18 1294 = true := by decide +kernel
theorem c1295 : check 60 115 18 1295 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1280 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1280) (chunksOK_one c1281)) (chunksOK_append (chunksOK_one c1282) (chunksOK_one c1283))) (chunksOK_append (chunksOK_append (chunksOK_one c1284) (chunksOK_one c1285)) (chunksOK_append (chunksOK_one c1286) (chunksOK_one c1287)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1288) (chunksOK_one c1289)) (chunksOK_append (chunksOK_one c1290) (chunksOK_one c1291))) (chunksOK_append (chunksOK_append (chunksOK_one c1292) (chunksOK_one c1293)) (chunksOK_append (chunksOK_one c1294) (chunksOK_one c1295)))))

end C80

namespace C81

theorem c1296 : check 60 115 18 1296 = true := by decide +kernel
theorem c1297 : check 60 115 18 1297 = true := by decide +kernel
theorem c1298 : check 60 115 18 1298 = true := by decide +kernel
theorem c1299 : check 60 115 18 1299 = true := by decide +kernel
theorem c1300 : check 60 115 18 1300 = true := by decide +kernel
theorem c1301 : check 60 115 18 1301 = true := by decide +kernel
theorem c1302 : check 60 115 18 1302 = true := by decide +kernel
theorem c1303 : check 60 115 18 1303 = true := by decide +kernel
theorem c1304 : check 60 115 18 1304 = true := by decide +kernel
theorem c1305 : check 60 115 18 1305 = true := by decide +kernel
theorem c1306 : check 60 115 18 1306 = true := by decide +kernel
theorem c1307 : check 60 115 18 1307 = true := by decide +kernel
theorem c1308 : check 60 115 18 1308 = true := by decide +kernel
theorem c1309 : check 60 115 18 1309 = true := by decide +kernel
theorem c1310 : check 60 115 18 1310 = true := by decide +kernel
theorem c1311 : check 60 115 18 1311 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1296 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1296) (chunksOK_one c1297)) (chunksOK_append (chunksOK_one c1298) (chunksOK_one c1299))) (chunksOK_append (chunksOK_append (chunksOK_one c1300) (chunksOK_one c1301)) (chunksOK_append (chunksOK_one c1302) (chunksOK_one c1303)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1304) (chunksOK_one c1305)) (chunksOK_append (chunksOK_one c1306) (chunksOK_one c1307))) (chunksOK_append (chunksOK_append (chunksOK_one c1308) (chunksOK_one c1309)) (chunksOK_append (chunksOK_one c1310) (chunksOK_one c1311)))))

end C81

namespace C82

theorem c1312 : check 60 115 18 1312 = true := by decide +kernel
theorem c1313 : check 60 115 18 1313 = true := by decide +kernel
theorem c1314 : check 60 115 18 1314 = true := by decide +kernel
theorem c1315 : check 60 115 18 1315 = true := by decide +kernel
theorem c1316 : check 60 115 18 1316 = true := by decide +kernel
theorem c1317 : check 60 115 18 1317 = true := by decide +kernel
theorem c1318 : check 60 115 18 1318 = true := by decide +kernel
theorem c1319 : check 60 115 18 1319 = true := by decide +kernel
theorem c1320 : check 60 115 18 1320 = true := by decide +kernel
theorem c1321 : check 60 115 18 1321 = true := by decide +kernel
theorem c1322 : check 60 115 18 1322 = true := by decide +kernel
theorem c1323 : check 60 115 18 1323 = true := by decide +kernel
theorem c1324 : check 60 115 18 1324 = true := by decide +kernel
theorem c1325 : check 60 115 18 1325 = true := by decide +kernel
theorem c1326 : check 60 115 18 1326 = true := by decide +kernel
theorem c1327 : check 60 115 18 1327 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1312 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1312) (chunksOK_one c1313)) (chunksOK_append (chunksOK_one c1314) (chunksOK_one c1315))) (chunksOK_append (chunksOK_append (chunksOK_one c1316) (chunksOK_one c1317)) (chunksOK_append (chunksOK_one c1318) (chunksOK_one c1319)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1320) (chunksOK_one c1321)) (chunksOK_append (chunksOK_one c1322) (chunksOK_one c1323))) (chunksOK_append (chunksOK_append (chunksOK_one c1324) (chunksOK_one c1325)) (chunksOK_append (chunksOK_one c1326) (chunksOK_one c1327)))))

end C82

namespace C83

theorem c1328 : check 60 115 18 1328 = true := by decide +kernel
theorem c1329 : check 60 115 18 1329 = true := by decide +kernel
theorem c1330 : check 60 115 18 1330 = true := by decide +kernel
theorem c1331 : check 60 115 18 1331 = true := by decide +kernel
theorem c1332 : check 60 115 18 1332 = true := by decide +kernel
theorem c1333 : check 60 115 18 1333 = true := by decide +kernel
theorem c1334 : check 60 115 18 1334 = true := by decide +kernel
theorem c1335 : check 60 115 18 1335 = true := by decide +kernel
theorem c1336 : check 60 115 18 1336 = true := by decide +kernel
theorem c1337 : check 60 115 18 1337 = true := by decide +kernel
theorem c1338 : check 60 115 18 1338 = true := by decide +kernel
theorem c1339 : check 60 115 18 1339 = true := by decide +kernel
theorem c1340 : check 60 115 18 1340 = true := by decide +kernel
theorem c1341 : check 60 115 18 1341 = true := by decide +kernel
theorem c1342 : check 60 115 18 1342 = true := by decide +kernel
theorem c1343 : check 60 115 18 1343 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1328 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1328) (chunksOK_one c1329)) (chunksOK_append (chunksOK_one c1330) (chunksOK_one c1331))) (chunksOK_append (chunksOK_append (chunksOK_one c1332) (chunksOK_one c1333)) (chunksOK_append (chunksOK_one c1334) (chunksOK_one c1335)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1336) (chunksOK_one c1337)) (chunksOK_append (chunksOK_one c1338) (chunksOK_one c1339))) (chunksOK_append (chunksOK_append (chunksOK_one c1340) (chunksOK_one c1341)) (chunksOK_append (chunksOK_one c1342) (chunksOK_one c1343)))))

end C83

namespace C84

theorem c1344 : check 60 115 18 1344 = true := by decide +kernel
theorem c1345 : check 60 115 18 1345 = true := by decide +kernel
theorem c1346 : check 60 115 18 1346 = true := by decide +kernel
theorem c1347 : check 60 115 18 1347 = true := by decide +kernel
theorem c1348 : check 60 115 18 1348 = true := by decide +kernel
theorem c1349 : check 60 115 18 1349 = true := by decide +kernel
theorem c1350 : check 60 115 18 1350 = true := by decide +kernel
theorem c1351 : check 60 115 18 1351 = true := by decide +kernel
theorem c1352 : check 60 115 18 1352 = true := by decide +kernel
theorem c1353 : check 60 115 18 1353 = true := by decide +kernel
theorem c1354 : check 60 115 18 1354 = true := by decide +kernel
theorem c1355 : check 60 115 18 1355 = true := by decide +kernel
theorem c1356 : check 60 115 18 1356 = true := by decide +kernel
theorem c1357 : check 60 115 18 1357 = true := by decide +kernel
theorem c1358 : check 60 115 18 1358 = true := by decide +kernel
theorem c1359 : check 60 115 18 1359 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1344 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1344) (chunksOK_one c1345)) (chunksOK_append (chunksOK_one c1346) (chunksOK_one c1347))) (chunksOK_append (chunksOK_append (chunksOK_one c1348) (chunksOK_one c1349)) (chunksOK_append (chunksOK_one c1350) (chunksOK_one c1351)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1352) (chunksOK_one c1353)) (chunksOK_append (chunksOK_one c1354) (chunksOK_one c1355))) (chunksOK_append (chunksOK_append (chunksOK_one c1356) (chunksOK_one c1357)) (chunksOK_append (chunksOK_one c1358) (chunksOK_one c1359)))))

end C84

namespace C85

theorem c1360 : check 60 115 18 1360 = true := by decide +kernel
theorem c1361 : check 60 115 18 1361 = true := by decide +kernel
theorem c1362 : check 60 115 18 1362 = true := by decide +kernel
theorem c1363 : check 60 115 18 1363 = true := by decide +kernel
theorem c1364 : check 60 115 18 1364 = true := by decide +kernel
theorem c1365 : check 60 115 18 1365 = true := by decide +kernel
theorem c1366 : check 60 115 18 1366 = true := by decide +kernel
theorem c1367 : check 60 115 18 1367 = true := by decide +kernel
theorem c1368 : check 60 115 18 1368 = true := by decide +kernel
theorem c1369 : check 60 115 18 1369 = true := by decide +kernel
theorem c1370 : check 60 115 18 1370 = true := by decide +kernel
theorem c1371 : check 60 115 18 1371 = true := by decide +kernel
theorem c1372 : check 60 115 18 1372 = true := by decide +kernel
theorem c1373 : check 60 115 18 1373 = true := by decide +kernel
theorem c1374 : check 60 115 18 1374 = true := by decide +kernel
theorem c1375 : check 60 115 18 1375 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1360 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1360) (chunksOK_one c1361)) (chunksOK_append (chunksOK_one c1362) (chunksOK_one c1363))) (chunksOK_append (chunksOK_append (chunksOK_one c1364) (chunksOK_one c1365)) (chunksOK_append (chunksOK_one c1366) (chunksOK_one c1367)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1368) (chunksOK_one c1369)) (chunksOK_append (chunksOK_one c1370) (chunksOK_one c1371))) (chunksOK_append (chunksOK_append (chunksOK_one c1372) (chunksOK_one c1373)) (chunksOK_append (chunksOK_one c1374) (chunksOK_one c1375)))))

end C85

namespace C86

theorem c1376 : check 60 115 18 1376 = true := by decide +kernel
theorem c1377 : check 60 115 18 1377 = true := by decide +kernel
theorem c1378 : check 60 115 18 1378 = true := by decide +kernel
theorem c1379 : check 60 115 18 1379 = true := by decide +kernel
theorem c1380 : check 60 115 18 1380 = true := by decide +kernel
theorem c1381 : check 60 115 18 1381 = true := by decide +kernel
theorem c1382 : check 60 115 18 1382 = true := by decide +kernel
theorem c1383 : check 60 115 18 1383 = true := by decide +kernel
theorem c1384 : check 60 115 18 1384 = true := by decide +kernel
theorem c1385 : check 60 115 18 1385 = true := by decide +kernel
theorem c1386 : check 60 115 18 1386 = true := by decide +kernel
theorem c1387 : check 60 115 18 1387 = true := by decide +kernel
theorem c1388 : check 60 115 18 1388 = true := by decide +kernel
theorem c1389 : check 60 115 18 1389 = true := by decide +kernel
theorem c1390 : check 60 115 18 1390 = true := by decide +kernel
theorem c1391 : check 60 115 18 1391 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1376 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1376) (chunksOK_one c1377)) (chunksOK_append (chunksOK_one c1378) (chunksOK_one c1379))) (chunksOK_append (chunksOK_append (chunksOK_one c1380) (chunksOK_one c1381)) (chunksOK_append (chunksOK_one c1382) (chunksOK_one c1383)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1384) (chunksOK_one c1385)) (chunksOK_append (chunksOK_one c1386) (chunksOK_one c1387))) (chunksOK_append (chunksOK_append (chunksOK_one c1388) (chunksOK_one c1389)) (chunksOK_append (chunksOK_one c1390) (chunksOK_one c1391)))))

end C86

namespace C87

theorem c1392 : check 60 115 18 1392 = true := by decide +kernel
theorem c1393 : check 60 115 18 1393 = true := by decide +kernel
theorem c1394 : check 60 115 18 1394 = true := by decide +kernel
theorem c1395 : check 60 115 18 1395 = true := by decide +kernel
theorem c1396 : check 60 115 18 1396 = true := by decide +kernel
theorem c1397 : check 60 115 18 1397 = true := by decide +kernel
theorem c1398 : check 60 115 18 1398 = true := by decide +kernel
theorem c1399 : check 60 115 18 1399 = true := by decide +kernel
theorem c1400 : check 60 115 18 1400 = true := by decide +kernel
theorem c1401 : check 60 115 18 1401 = true := by decide +kernel
theorem c1402 : check 60 115 18 1402 = true := by decide +kernel
theorem c1403 : check 60 115 18 1403 = true := by decide +kernel
theorem c1404 : check 60 115 18 1404 = true := by decide +kernel
theorem c1405 : check 60 115 18 1405 = true := by decide +kernel
theorem c1406 : check 60 115 18 1406 = true := by decide +kernel
theorem c1407 : check 60 115 18 1407 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1392 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1392) (chunksOK_one c1393)) (chunksOK_append (chunksOK_one c1394) (chunksOK_one c1395))) (chunksOK_append (chunksOK_append (chunksOK_one c1396) (chunksOK_one c1397)) (chunksOK_append (chunksOK_one c1398) (chunksOK_one c1399)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1400) (chunksOK_one c1401)) (chunksOK_append (chunksOK_one c1402) (chunksOK_one c1403))) (chunksOK_append (chunksOK_append (chunksOK_one c1404) (chunksOK_one c1405)) (chunksOK_append (chunksOK_one c1406) (chunksOK_one c1407)))))

end C87

namespace C88

theorem c1408 : check 60 115 18 1408 = true := by decide +kernel
theorem c1409 : check 60 115 18 1409 = true := by decide +kernel
theorem c1410 : check 60 115 18 1410 = true := by decide +kernel
theorem c1411 : check 60 115 18 1411 = true := by decide +kernel
theorem c1412 : check 60 115 18 1412 = true := by decide +kernel
theorem c1413 : check 60 115 18 1413 = true := by decide +kernel
theorem c1414 : check 60 115 18 1414 = true := by decide +kernel
theorem c1415 : check 60 115 18 1415 = true := by decide +kernel
theorem c1416 : check 60 115 18 1416 = true := by decide +kernel
theorem c1417 : check 60 115 18 1417 = true := by decide +kernel
theorem c1418 : check 60 115 18 1418 = true := by decide +kernel
theorem c1419 : check 60 115 18 1419 = true := by decide +kernel
theorem c1420 : check 60 115 18 1420 = true := by decide +kernel
theorem c1421 : check 60 115 18 1421 = true := by decide +kernel
theorem c1422 : check 60 115 18 1422 = true := by decide +kernel
theorem c1423 : check 60 115 18 1423 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1408 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1408) (chunksOK_one c1409)) (chunksOK_append (chunksOK_one c1410) (chunksOK_one c1411))) (chunksOK_append (chunksOK_append (chunksOK_one c1412) (chunksOK_one c1413)) (chunksOK_append (chunksOK_one c1414) (chunksOK_one c1415)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1416) (chunksOK_one c1417)) (chunksOK_append (chunksOK_one c1418) (chunksOK_one c1419))) (chunksOK_append (chunksOK_append (chunksOK_one c1420) (chunksOK_one c1421)) (chunksOK_append (chunksOK_one c1422) (chunksOK_one c1423)))))

end C88

namespace C89

theorem c1424 : check 60 115 18 1424 = true := by decide +kernel
theorem c1425 : check 60 115 18 1425 = true := by decide +kernel
theorem c1426 : check 60 115 18 1426 = true := by decide +kernel
theorem c1427 : check 60 115 18 1427 = true := by decide +kernel
theorem c1428 : check 60 115 18 1428 = true := by decide +kernel
theorem c1429 : check 60 115 18 1429 = true := by decide +kernel
theorem c1430 : check 60 115 18 1430 = true := by decide +kernel
theorem c1431 : check 60 115 18 1431 = true := by decide +kernel
theorem c1432 : check 60 115 18 1432 = true := by decide +kernel
theorem c1433 : check 60 115 18 1433 = true := by decide +kernel
theorem c1434 : check 60 115 18 1434 = true := by decide +kernel
theorem c1435 : check 60 115 18 1435 = true := by decide +kernel
theorem c1436 : check 60 115 18 1436 = true := by decide +kernel
theorem c1437 : check 60 115 18 1437 = true := by decide +kernel
theorem c1438 : check 60 115 18 1438 = true := by decide +kernel
theorem c1439 : check 60 115 18 1439 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1424 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1424) (chunksOK_one c1425)) (chunksOK_append (chunksOK_one c1426) (chunksOK_one c1427))) (chunksOK_append (chunksOK_append (chunksOK_one c1428) (chunksOK_one c1429)) (chunksOK_append (chunksOK_one c1430) (chunksOK_one c1431)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1432) (chunksOK_one c1433)) (chunksOK_append (chunksOK_one c1434) (chunksOK_one c1435))) (chunksOK_append (chunksOK_append (chunksOK_one c1436) (chunksOK_one c1437)) (chunksOK_append (chunksOK_one c1438) (chunksOK_one c1439)))))

end C89

namespace C90

theorem c1440 : check 60 115 18 1440 = true := by decide +kernel
theorem c1441 : check 60 115 18 1441 = true := by decide +kernel
theorem c1442 : check 60 115 18 1442 = true := by decide +kernel
theorem c1443 : check 60 115 18 1443 = true := by decide +kernel
theorem c1444 : check 60 115 18 1444 = true := by decide +kernel
theorem c1445 : check 60 115 18 1445 = true := by decide +kernel
theorem c1446 : check 60 115 18 1446 = true := by decide +kernel
theorem c1447 : check 60 115 18 1447 = true := by decide +kernel
theorem c1448 : check 60 115 18 1448 = true := by decide +kernel
theorem c1449 : check 60 115 18 1449 = true := by decide +kernel
theorem c1450 : check 60 115 18 1450 = true := by decide +kernel
theorem c1451 : check 60 115 18 1451 = true := by decide +kernel
theorem c1452 : check 60 115 18 1452 = true := by decide +kernel
theorem c1453 : check 60 115 18 1453 = true := by decide +kernel
theorem c1454 : check 60 115 18 1454 = true := by decide +kernel
theorem c1455 : check 60 115 18 1455 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1440 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1440) (chunksOK_one c1441)) (chunksOK_append (chunksOK_one c1442) (chunksOK_one c1443))) (chunksOK_append (chunksOK_append (chunksOK_one c1444) (chunksOK_one c1445)) (chunksOK_append (chunksOK_one c1446) (chunksOK_one c1447)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1448) (chunksOK_one c1449)) (chunksOK_append (chunksOK_one c1450) (chunksOK_one c1451))) (chunksOK_append (chunksOK_append (chunksOK_one c1452) (chunksOK_one c1453)) (chunksOK_append (chunksOK_one c1454) (chunksOK_one c1455)))))

end C90

namespace C91

theorem c1456 : check 60 115 18 1456 = true := by decide +kernel
theorem c1457 : check 60 115 18 1457 = true := by decide +kernel
theorem c1458 : check 60 115 18 1458 = true := by decide +kernel
theorem c1459 : check 60 115 18 1459 = true := by decide +kernel
theorem c1460 : check 60 115 18 1460 = true := by decide +kernel
theorem c1461 : check 60 115 18 1461 = true := by decide +kernel
theorem c1462 : check 60 115 18 1462 = true := by decide +kernel
theorem c1463 : check 60 115 18 1463 = true := by decide +kernel
theorem c1464 : check 60 115 18 1464 = true := by decide +kernel
theorem c1465 : check 60 115 18 1465 = true := by decide +kernel
theorem c1466 : check 60 115 18 1466 = true := by decide +kernel
theorem c1467 : check 60 115 18 1467 = true := by decide +kernel
theorem c1468 : check 60 115 18 1468 = true := by decide +kernel
theorem c1469 : check 60 115 18 1469 = true := by decide +kernel
theorem c1470 : check 60 115 18 1470 = true := by decide +kernel
theorem c1471 : check 60 115 18 1471 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1456 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1456) (chunksOK_one c1457)) (chunksOK_append (chunksOK_one c1458) (chunksOK_one c1459))) (chunksOK_append (chunksOK_append (chunksOK_one c1460) (chunksOK_one c1461)) (chunksOK_append (chunksOK_one c1462) (chunksOK_one c1463)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1464) (chunksOK_one c1465)) (chunksOK_append (chunksOK_one c1466) (chunksOK_one c1467))) (chunksOK_append (chunksOK_append (chunksOK_one c1468) (chunksOK_one c1469)) (chunksOK_append (chunksOK_one c1470) (chunksOK_one c1471)))))

end C91

namespace C92

theorem c1472 : check 60 115 18 1472 = true := by decide +kernel
theorem c1473 : check 60 115 18 1473 = true := by decide +kernel
theorem c1474 : check 60 115 18 1474 = true := by decide +kernel
theorem c1475 : check 60 115 18 1475 = true := by decide +kernel
theorem c1476 : check 60 115 18 1476 = true := by decide +kernel
theorem c1477 : check 60 115 18 1477 = true := by decide +kernel
theorem c1478 : check 60 115 18 1478 = true := by decide +kernel
theorem c1479 : check 60 115 18 1479 = true := by decide +kernel
theorem c1480 : check 60 115 18 1480 = true := by decide +kernel
theorem c1481 : check 60 115 18 1481 = true := by decide +kernel
theorem c1482 : check 60 115 18 1482 = true := by decide +kernel
theorem c1483 : check 60 115 18 1483 = true := by decide +kernel
theorem c1484 : check 60 115 18 1484 = true := by decide +kernel
theorem c1485 : check 60 115 18 1485 = true := by decide +kernel
theorem c1486 : check 60 115 18 1486 = true := by decide +kernel
theorem c1487 : check 60 115 18 1487 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1472 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1472) (chunksOK_one c1473)) (chunksOK_append (chunksOK_one c1474) (chunksOK_one c1475))) (chunksOK_append (chunksOK_append (chunksOK_one c1476) (chunksOK_one c1477)) (chunksOK_append (chunksOK_one c1478) (chunksOK_one c1479)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1480) (chunksOK_one c1481)) (chunksOK_append (chunksOK_one c1482) (chunksOK_one c1483))) (chunksOK_append (chunksOK_append (chunksOK_one c1484) (chunksOK_one c1485)) (chunksOK_append (chunksOK_one c1486) (chunksOK_one c1487)))))

end C92

namespace C93

theorem c1488 : check 60 115 18 1488 = true := by decide +kernel
theorem c1489 : check 60 115 18 1489 = true := by decide +kernel
theorem c1490 : check 60 115 18 1490 = true := by decide +kernel
theorem c1491 : check 60 115 18 1491 = true := by decide +kernel
theorem c1492 : check 60 115 18 1492 = true := by decide +kernel
theorem c1493 : check 60 115 18 1493 = true := by decide +kernel
theorem c1494 : check 60 115 18 1494 = true := by decide +kernel
theorem c1495 : check 60 115 18 1495 = true := by decide +kernel
theorem c1496 : check 60 115 18 1496 = true := by decide +kernel
theorem c1497 : check 60 115 18 1497 = true := by decide +kernel
theorem c1498 : check 60 115 18 1498 = true := by decide +kernel
theorem c1499 : check 60 115 18 1499 = true := by decide +kernel
theorem c1500 : check 60 115 18 1500 = true := by decide +kernel
theorem c1501 : check 60 115 18 1501 = true := by decide +kernel
theorem c1502 : check 60 115 18 1502 = true := by decide +kernel
theorem c1503 : check 60 115 18 1503 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1488 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1488) (chunksOK_one c1489)) (chunksOK_append (chunksOK_one c1490) (chunksOK_one c1491))) (chunksOK_append (chunksOK_append (chunksOK_one c1492) (chunksOK_one c1493)) (chunksOK_append (chunksOK_one c1494) (chunksOK_one c1495)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1496) (chunksOK_one c1497)) (chunksOK_append (chunksOK_one c1498) (chunksOK_one c1499))) (chunksOK_append (chunksOK_append (chunksOK_one c1500) (chunksOK_one c1501)) (chunksOK_append (chunksOK_one c1502) (chunksOK_one c1503)))))

end C93

namespace C94

theorem c1504 : check 60 115 18 1504 = true := by decide +kernel
theorem c1505 : check 60 115 18 1505 = true := by decide +kernel
theorem c1506 : check 60 115 18 1506 = true := by decide +kernel
theorem c1507 : check 60 115 18 1507 = true := by decide +kernel
theorem c1508 : check 60 115 18 1508 = true := by decide +kernel
theorem c1509 : check 60 115 18 1509 = true := by decide +kernel
theorem c1510 : check 60 115 18 1510 = true := by decide +kernel
theorem c1511 : check 60 115 18 1511 = true := by decide +kernel
theorem c1512 : check 60 115 18 1512 = true := by decide +kernel
theorem c1513 : check 60 115 18 1513 = true := by decide +kernel
theorem c1514 : check 60 115 18 1514 = true := by decide +kernel
theorem c1515 : check 60 115 18 1515 = true := by decide +kernel
theorem c1516 : check 60 115 18 1516 = true := by decide +kernel
theorem c1517 : check 60 115 18 1517 = true := by decide +kernel
theorem c1518 : check 60 115 18 1518 = true := by decide +kernel
theorem c1519 : check 60 115 18 1519 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1504 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1504) (chunksOK_one c1505)) (chunksOK_append (chunksOK_one c1506) (chunksOK_one c1507))) (chunksOK_append (chunksOK_append (chunksOK_one c1508) (chunksOK_one c1509)) (chunksOK_append (chunksOK_one c1510) (chunksOK_one c1511)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1512) (chunksOK_one c1513)) (chunksOK_append (chunksOK_one c1514) (chunksOK_one c1515))) (chunksOK_append (chunksOK_append (chunksOK_one c1516) (chunksOK_one c1517)) (chunksOK_append (chunksOK_one c1518) (chunksOK_one c1519)))))

end C94

namespace C95

theorem c1520 : check 60 115 18 1520 = true := by decide +kernel
theorem c1521 : check 60 115 18 1521 = true := by decide +kernel
theorem c1522 : check 60 115 18 1522 = true := by decide +kernel
theorem c1523 : check 60 115 18 1523 = true := by decide +kernel
theorem c1524 : check 60 115 18 1524 = true := by decide +kernel
theorem c1525 : check 60 115 18 1525 = true := by decide +kernel
theorem c1526 : check 60 115 18 1526 = true := by decide +kernel
theorem c1527 : check 60 115 18 1527 = true := by decide +kernel
theorem c1528 : check 60 115 18 1528 = true := by decide +kernel
theorem c1529 : check 60 115 18 1529 = true := by decide +kernel
theorem c1530 : check 60 115 18 1530 = true := by decide +kernel
theorem c1531 : check 60 115 18 1531 = true := by decide +kernel
theorem c1532 : check 60 115 18 1532 = true := by decide +kernel
theorem c1533 : check 60 115 18 1533 = true := by decide +kernel
theorem c1534 : check 60 115 18 1534 = true := by decide +kernel
theorem c1535 : check 60 115 18 1535 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1520 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1520) (chunksOK_one c1521)) (chunksOK_append (chunksOK_one c1522) (chunksOK_one c1523))) (chunksOK_append (chunksOK_append (chunksOK_one c1524) (chunksOK_one c1525)) (chunksOK_append (chunksOK_one c1526) (chunksOK_one c1527)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1528) (chunksOK_one c1529)) (chunksOK_append (chunksOK_one c1530) (chunksOK_one c1531))) (chunksOK_append (chunksOK_append (chunksOK_one c1532) (chunksOK_one c1533)) (chunksOK_append (chunksOK_one c1534) (chunksOK_one c1535)))))

end C95

namespace C96

theorem c1536 : check 60 115 18 1536 = true := by decide +kernel
theorem c1537 : check 60 115 18 1537 = true := by decide +kernel
theorem c1538 : check 60 115 18 1538 = true := by decide +kernel
theorem c1539 : check 60 115 18 1539 = true := by decide +kernel
theorem c1540 : check 60 115 18 1540 = true := by decide +kernel
theorem c1541 : check 60 115 18 1541 = true := by decide +kernel
theorem c1542 : check 60 115 18 1542 = true := by decide +kernel
theorem c1543 : check 60 115 18 1543 = true := by decide +kernel
theorem c1544 : check 60 115 18 1544 = true := by decide +kernel
theorem c1545 : check 60 115 18 1545 = true := by decide +kernel
theorem c1546 : check 60 115 18 1546 = true := by decide +kernel
theorem c1547 : check 60 115 18 1547 = true := by decide +kernel
theorem c1548 : check 60 115 18 1548 = true := by decide +kernel
theorem c1549 : check 60 115 18 1549 = true := by decide +kernel
theorem c1550 : check 60 115 18 1550 = true := by decide +kernel
theorem c1551 : check 60 115 18 1551 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1536 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1536) (chunksOK_one c1537)) (chunksOK_append (chunksOK_one c1538) (chunksOK_one c1539))) (chunksOK_append (chunksOK_append (chunksOK_one c1540) (chunksOK_one c1541)) (chunksOK_append (chunksOK_one c1542) (chunksOK_one c1543)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1544) (chunksOK_one c1545)) (chunksOK_append (chunksOK_one c1546) (chunksOK_one c1547))) (chunksOK_append (chunksOK_append (chunksOK_one c1548) (chunksOK_one c1549)) (chunksOK_append (chunksOK_one c1550) (chunksOK_one c1551)))))

end C96

namespace C97

theorem c1552 : check 60 115 18 1552 = true := by decide +kernel
theorem c1553 : check 60 115 18 1553 = true := by decide +kernel
theorem c1554 : check 60 115 18 1554 = true := by decide +kernel
theorem c1555 : check 60 115 18 1555 = true := by decide +kernel
theorem c1556 : check 60 115 18 1556 = true := by decide +kernel
theorem c1557 : check 60 115 18 1557 = true := by decide +kernel
theorem c1558 : check 60 115 18 1558 = true := by decide +kernel
theorem c1559 : check 60 115 18 1559 = true := by decide +kernel
theorem c1560 : check 60 115 18 1560 = true := by decide +kernel
theorem c1561 : check 60 115 18 1561 = true := by decide +kernel
theorem c1562 : check 60 115 18 1562 = true := by decide +kernel
theorem c1563 : check 60 115 18 1563 = true := by decide +kernel
theorem c1564 : check 60 115 18 1564 = true := by decide +kernel
theorem c1565 : check 60 115 18 1565 = true := by decide +kernel
theorem c1566 : check 60 115 18 1566 = true := by decide +kernel
theorem c1567 : check 60 115 18 1567 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1552 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1552) (chunksOK_one c1553)) (chunksOK_append (chunksOK_one c1554) (chunksOK_one c1555))) (chunksOK_append (chunksOK_append (chunksOK_one c1556) (chunksOK_one c1557)) (chunksOK_append (chunksOK_one c1558) (chunksOK_one c1559)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1560) (chunksOK_one c1561)) (chunksOK_append (chunksOK_one c1562) (chunksOK_one c1563))) (chunksOK_append (chunksOK_append (chunksOK_one c1564) (chunksOK_one c1565)) (chunksOK_append (chunksOK_one c1566) (chunksOK_one c1567)))))

end C97

namespace C98

theorem c1568 : check 60 115 18 1568 = true := by decide +kernel
theorem c1569 : check 60 115 18 1569 = true := by decide +kernel
theorem c1570 : check 60 115 18 1570 = true := by decide +kernel
theorem c1571 : check 60 115 18 1571 = true := by decide +kernel
theorem c1572 : check 60 115 18 1572 = true := by decide +kernel
theorem c1573 : check 60 115 18 1573 = true := by decide +kernel
theorem c1574 : check 60 115 18 1574 = true := by decide +kernel
theorem c1575 : check 60 115 18 1575 = true := by decide +kernel
theorem c1576 : check 60 115 18 1576 = true := by decide +kernel
theorem c1577 : check 60 115 18 1577 = true := by decide +kernel
theorem c1578 : check 60 115 18 1578 = true := by decide +kernel
theorem c1579 : check 60 115 18 1579 = true := by decide +kernel
theorem c1580 : check 60 115 18 1580 = true := by decide +kernel
theorem c1581 : check 60 115 18 1581 = true := by decide +kernel
theorem c1582 : check 60 115 18 1582 = true := by decide +kernel
theorem c1583 : check 60 115 18 1583 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1568 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1568) (chunksOK_one c1569)) (chunksOK_append (chunksOK_one c1570) (chunksOK_one c1571))) (chunksOK_append (chunksOK_append (chunksOK_one c1572) (chunksOK_one c1573)) (chunksOK_append (chunksOK_one c1574) (chunksOK_one c1575)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1576) (chunksOK_one c1577)) (chunksOK_append (chunksOK_one c1578) (chunksOK_one c1579))) (chunksOK_append (chunksOK_append (chunksOK_one c1580) (chunksOK_one c1581)) (chunksOK_append (chunksOK_one c1582) (chunksOK_one c1583)))))

end C98

namespace C99

theorem c1584 : check 60 115 18 1584 = true := by decide +kernel
theorem c1585 : check 60 115 18 1585 = true := by decide +kernel
theorem c1586 : check 60 115 18 1586 = true := by decide +kernel
theorem c1587 : check 60 115 18 1587 = true := by decide +kernel
theorem c1588 : check 60 115 18 1588 = true := by decide +kernel
theorem c1589 : check 60 115 18 1589 = true := by decide +kernel
theorem c1590 : check 60 115 18 1590 = true := by decide +kernel
theorem c1591 : check 60 115 18 1591 = true := by decide +kernel
theorem c1592 : check 60 115 18 1592 = true := by decide +kernel
theorem c1593 : check 60 115 18 1593 = true := by decide +kernel
theorem c1594 : check 60 115 18 1594 = true := by decide +kernel
theorem c1595 : check 60 115 18 1595 = true := by decide +kernel
theorem c1596 : check 60 115 18 1596 = true := by decide +kernel
theorem c1597 : check 60 115 18 1597 = true := by decide +kernel
theorem c1598 : check 60 115 18 1598 = true := by decide +kernel
theorem c1599 : check 60 115 18 1599 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1584 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1584) (chunksOK_one c1585)) (chunksOK_append (chunksOK_one c1586) (chunksOK_one c1587))) (chunksOK_append (chunksOK_append (chunksOK_one c1588) (chunksOK_one c1589)) (chunksOK_append (chunksOK_one c1590) (chunksOK_one c1591)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1592) (chunksOK_one c1593)) (chunksOK_append (chunksOK_one c1594) (chunksOK_one c1595))) (chunksOK_append (chunksOK_append (chunksOK_one c1596) (chunksOK_one c1597)) (chunksOK_append (chunksOK_one c1598) (chunksOK_one c1599)))))

end C99

namespace C100

theorem c1600 : check 60 115 18 1600 = true := by decide +kernel
theorem c1601 : check 60 115 18 1601 = true := by decide +kernel
theorem c1602 : check 60 115 18 1602 = true := by decide +kernel
theorem c1603 : check 60 115 18 1603 = true := by decide +kernel
theorem c1604 : check 60 115 18 1604 = true := by decide +kernel
theorem c1605 : check 60 115 18 1605 = true := by decide +kernel
theorem c1606 : check 60 115 18 1606 = true := by decide +kernel
theorem c1607 : check 60 115 18 1607 = true := by decide +kernel
theorem c1608 : check 60 115 18 1608 = true := by decide +kernel
theorem c1609 : check 60 115 18 1609 = true := by decide +kernel
theorem c1610 : check 60 115 18 1610 = true := by decide +kernel
theorem c1611 : check 60 115 18 1611 = true := by decide +kernel
theorem c1612 : check 60 115 18 1612 = true := by decide +kernel
theorem c1613 : check 60 115 18 1613 = true := by decide +kernel
theorem c1614 : check 60 115 18 1614 = true := by decide +kernel
theorem c1615 : check 60 115 18 1615 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1600 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1600) (chunksOK_one c1601)) (chunksOK_append (chunksOK_one c1602) (chunksOK_one c1603))) (chunksOK_append (chunksOK_append (chunksOK_one c1604) (chunksOK_one c1605)) (chunksOK_append (chunksOK_one c1606) (chunksOK_one c1607)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1608) (chunksOK_one c1609)) (chunksOK_append (chunksOK_one c1610) (chunksOK_one c1611))) (chunksOK_append (chunksOK_append (chunksOK_one c1612) (chunksOK_one c1613)) (chunksOK_append (chunksOK_one c1614) (chunksOK_one c1615)))))

end C100

namespace C101

theorem c1616 : check 60 115 18 1616 = true := by decide +kernel
theorem c1617 : check 60 115 18 1617 = true := by decide +kernel
theorem c1618 : check 60 115 18 1618 = true := by decide +kernel
theorem c1619 : check 60 115 18 1619 = true := by decide +kernel
theorem c1620 : check 60 115 18 1620 = true := by decide +kernel
theorem c1621 : check 60 115 18 1621 = true := by decide +kernel
theorem c1622 : check 60 115 18 1622 = true := by decide +kernel
theorem c1623 : check 60 115 18 1623 = true := by decide +kernel
theorem c1624 : check 60 115 18 1624 = true := by decide +kernel
theorem c1625 : check 60 115 18 1625 = true := by decide +kernel
theorem c1626 : check 60 115 18 1626 = true := by decide +kernel
theorem c1627 : check 60 115 18 1627 = true := by decide +kernel
theorem c1628 : check 60 115 18 1628 = true := by decide +kernel
theorem c1629 : check 60 115 18 1629 = true := by decide +kernel
theorem c1630 : check 60 115 18 1630 = true := by decide +kernel
theorem c1631 : check 60 115 18 1631 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1616 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1616) (chunksOK_one c1617)) (chunksOK_append (chunksOK_one c1618) (chunksOK_one c1619))) (chunksOK_append (chunksOK_append (chunksOK_one c1620) (chunksOK_one c1621)) (chunksOK_append (chunksOK_one c1622) (chunksOK_one c1623)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1624) (chunksOK_one c1625)) (chunksOK_append (chunksOK_one c1626) (chunksOK_one c1627))) (chunksOK_append (chunksOK_append (chunksOK_one c1628) (chunksOK_one c1629)) (chunksOK_append (chunksOK_one c1630) (chunksOK_one c1631)))))

end C101

namespace C102

theorem c1632 : check 60 115 18 1632 = true := by decide +kernel
theorem c1633 : check 60 115 18 1633 = true := by decide +kernel
theorem c1634 : check 60 115 18 1634 = true := by decide +kernel
theorem c1635 : check 60 115 18 1635 = true := by decide +kernel
theorem c1636 : check 60 115 18 1636 = true := by decide +kernel
theorem c1637 : check 60 115 18 1637 = true := by decide +kernel
theorem c1638 : check 60 115 18 1638 = true := by decide +kernel
theorem c1639 : check 60 115 18 1639 = true := by decide +kernel
theorem c1640 : check 60 115 18 1640 = true := by decide +kernel
theorem c1641 : check 60 115 18 1641 = true := by decide +kernel
theorem c1642 : check 60 115 18 1642 = true := by decide +kernel
theorem c1643 : check 60 115 18 1643 = true := by decide +kernel
theorem c1644 : check 60 115 18 1644 = true := by decide +kernel
theorem c1645 : check 60 115 18 1645 = true := by decide +kernel
theorem c1646 : check 60 115 18 1646 = true := by decide +kernel
theorem c1647 : check 60 115 18 1647 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1632 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1632) (chunksOK_one c1633)) (chunksOK_append (chunksOK_one c1634) (chunksOK_one c1635))) (chunksOK_append (chunksOK_append (chunksOK_one c1636) (chunksOK_one c1637)) (chunksOK_append (chunksOK_one c1638) (chunksOK_one c1639)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1640) (chunksOK_one c1641)) (chunksOK_append (chunksOK_one c1642) (chunksOK_one c1643))) (chunksOK_append (chunksOK_append (chunksOK_one c1644) (chunksOK_one c1645)) (chunksOK_append (chunksOK_one c1646) (chunksOK_one c1647)))))

end C102

namespace C103

theorem c1648 : check 60 115 18 1648 = true := by decide +kernel
theorem c1649 : check 60 115 18 1649 = true := by decide +kernel
theorem c1650 : check 60 115 18 1650 = true := by decide +kernel
theorem c1651 : check 60 115 18 1651 = true := by decide +kernel
theorem c1652 : check 60 115 18 1652 = true := by decide +kernel
theorem c1653 : check 60 115 18 1653 = true := by decide +kernel
theorem c1654 : check 60 115 18 1654 = true := by decide +kernel
theorem c1655 : check 60 115 18 1655 = true := by decide +kernel
theorem c1656 : check 60 115 18 1656 = true := by decide +kernel
theorem c1657 : check 60 115 18 1657 = true := by decide +kernel
theorem c1658 : check 60 115 18 1658 = true := by decide +kernel
theorem c1659 : check 60 115 18 1659 = true := by decide +kernel
theorem c1660 : check 60 115 18 1660 = true := by decide +kernel
theorem c1661 : check 60 115 18 1661 = true := by decide +kernel
theorem c1662 : check 60 115 18 1662 = true := by decide +kernel
theorem c1663 : check 60 115 18 1663 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1648 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1648) (chunksOK_one c1649)) (chunksOK_append (chunksOK_one c1650) (chunksOK_one c1651))) (chunksOK_append (chunksOK_append (chunksOK_one c1652) (chunksOK_one c1653)) (chunksOK_append (chunksOK_one c1654) (chunksOK_one c1655)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1656) (chunksOK_one c1657)) (chunksOK_append (chunksOK_one c1658) (chunksOK_one c1659))) (chunksOK_append (chunksOK_append (chunksOK_one c1660) (chunksOK_one c1661)) (chunksOK_append (chunksOK_one c1662) (chunksOK_one c1663)))))

end C103

namespace C104

theorem c1664 : check 60 115 18 1664 = true := by decide +kernel
theorem c1665 : check 60 115 18 1665 = true := by decide +kernel
theorem c1666 : check 60 115 18 1666 = true := by decide +kernel
theorem c1667 : check 60 115 18 1667 = true := by decide +kernel
theorem c1668 : check 60 115 18 1668 = true := by decide +kernel
theorem c1669 : check 60 115 18 1669 = true := by decide +kernel
theorem c1670 : check 60 115 18 1670 = true := by decide +kernel
theorem c1671 : check 60 115 18 1671 = true := by decide +kernel
theorem c1672 : check 60 115 18 1672 = true := by decide +kernel
theorem c1673 : check 60 115 18 1673 = true := by decide +kernel
theorem c1674 : check 60 115 18 1674 = true := by decide +kernel
theorem c1675 : check 60 115 18 1675 = true := by decide +kernel
theorem c1676 : check 60 115 18 1676 = true := by decide +kernel
theorem c1677 : check 60 115 18 1677 = true := by decide +kernel
theorem c1678 : check 60 115 18 1678 = true := by decide +kernel
theorem c1679 : check 60 115 18 1679 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1664 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1664) (chunksOK_one c1665)) (chunksOK_append (chunksOK_one c1666) (chunksOK_one c1667))) (chunksOK_append (chunksOK_append (chunksOK_one c1668) (chunksOK_one c1669)) (chunksOK_append (chunksOK_one c1670) (chunksOK_one c1671)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1672) (chunksOK_one c1673)) (chunksOK_append (chunksOK_one c1674) (chunksOK_one c1675))) (chunksOK_append (chunksOK_append (chunksOK_one c1676) (chunksOK_one c1677)) (chunksOK_append (chunksOK_one c1678) (chunksOK_one c1679)))))

end C104

namespace C105

theorem c1680 : check 60 115 18 1680 = true := by decide +kernel
theorem c1681 : check 60 115 18 1681 = true := by decide +kernel
theorem c1682 : check 60 115 18 1682 = true := by decide +kernel
theorem c1683 : check 60 115 18 1683 = true := by decide +kernel
theorem c1684 : check 60 115 18 1684 = true := by decide +kernel
theorem c1685 : check 60 115 18 1685 = true := by decide +kernel
theorem c1686 : check 60 115 18 1686 = true := by decide +kernel
theorem c1687 : check 60 115 18 1687 = true := by decide +kernel
theorem c1688 : check 60 115 18 1688 = true := by decide +kernel
theorem c1689 : check 60 115 18 1689 = true := by decide +kernel
theorem c1690 : check 60 115 18 1690 = true := by decide +kernel
theorem c1691 : check 60 115 18 1691 = true := by decide +kernel
theorem c1692 : check 60 115 18 1692 = true := by decide +kernel
theorem c1693 : check 60 115 18 1693 = true := by decide +kernel
theorem c1694 : check 60 115 18 1694 = true := by decide +kernel
theorem c1695 : check 60 115 18 1695 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1680 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1680) (chunksOK_one c1681)) (chunksOK_append (chunksOK_one c1682) (chunksOK_one c1683))) (chunksOK_append (chunksOK_append (chunksOK_one c1684) (chunksOK_one c1685)) (chunksOK_append (chunksOK_one c1686) (chunksOK_one c1687)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1688) (chunksOK_one c1689)) (chunksOK_append (chunksOK_one c1690) (chunksOK_one c1691))) (chunksOK_append (chunksOK_append (chunksOK_one c1692) (chunksOK_one c1693)) (chunksOK_append (chunksOK_one c1694) (chunksOK_one c1695)))))

end C105

namespace C106

theorem c1696 : check 60 115 18 1696 = true := by decide +kernel
theorem c1697 : check 60 115 18 1697 = true := by decide +kernel
theorem c1698 : check 60 115 18 1698 = true := by decide +kernel
theorem c1699 : check 60 115 18 1699 = true := by decide +kernel
theorem c1700 : check 60 115 18 1700 = true := by decide +kernel
theorem c1701 : check 60 115 18 1701 = true := by decide +kernel
theorem c1702 : check 60 115 18 1702 = true := by decide +kernel
theorem c1703 : check 60 115 18 1703 = true := by decide +kernel
theorem c1704 : check 60 115 18 1704 = true := by decide +kernel
theorem c1705 : check 60 115 18 1705 = true := by decide +kernel
theorem c1706 : check 60 115 18 1706 = true := by decide +kernel
theorem c1707 : check 60 115 18 1707 = true := by decide +kernel
theorem c1708 : check 60 115 18 1708 = true := by decide +kernel
theorem c1709 : check 60 115 18 1709 = true := by decide +kernel
theorem c1710 : check 60 115 18 1710 = true := by decide +kernel
theorem c1711 : check 60 115 18 1711 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1696 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1696) (chunksOK_one c1697)) (chunksOK_append (chunksOK_one c1698) (chunksOK_one c1699))) (chunksOK_append (chunksOK_append (chunksOK_one c1700) (chunksOK_one c1701)) (chunksOK_append (chunksOK_one c1702) (chunksOK_one c1703)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1704) (chunksOK_one c1705)) (chunksOK_append (chunksOK_one c1706) (chunksOK_one c1707))) (chunksOK_append (chunksOK_append (chunksOK_one c1708) (chunksOK_one c1709)) (chunksOK_append (chunksOK_one c1710) (chunksOK_one c1711)))))

end C106

namespace C107

theorem c1712 : check 60 115 18 1712 = true := by decide +kernel
theorem c1713 : check 60 115 18 1713 = true := by decide +kernel
theorem c1714 : check 60 115 18 1714 = true := by decide +kernel
theorem c1715 : check 60 115 18 1715 = true := by decide +kernel
theorem c1716 : check 60 115 18 1716 = true := by decide +kernel
theorem c1717 : check 60 115 18 1717 = true := by decide +kernel
theorem c1718 : check 60 115 18 1718 = true := by decide +kernel
theorem c1719 : check 60 115 18 1719 = true := by decide +kernel
theorem c1720 : check 60 115 18 1720 = true := by decide +kernel
theorem c1721 : check 60 115 18 1721 = true := by decide +kernel
theorem c1722 : check 60 115 18 1722 = true := by decide +kernel
theorem c1723 : check 60 115 18 1723 = true := by decide +kernel
theorem c1724 : check 60 115 18 1724 = true := by decide +kernel
theorem c1725 : check 60 115 18 1725 = true := by decide +kernel
theorem c1726 : check 60 115 18 1726 = true := by decide +kernel
theorem c1727 : check 60 115 18 1727 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1712 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1712) (chunksOK_one c1713)) (chunksOK_append (chunksOK_one c1714) (chunksOK_one c1715))) (chunksOK_append (chunksOK_append (chunksOK_one c1716) (chunksOK_one c1717)) (chunksOK_append (chunksOK_one c1718) (chunksOK_one c1719)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1720) (chunksOK_one c1721)) (chunksOK_append (chunksOK_one c1722) (chunksOK_one c1723))) (chunksOK_append (chunksOK_append (chunksOK_one c1724) (chunksOK_one c1725)) (chunksOK_append (chunksOK_one c1726) (chunksOK_one c1727)))))

end C107

namespace C108

theorem c1728 : check 60 115 18 1728 = true := by decide +kernel
theorem c1729 : check 60 115 18 1729 = true := by decide +kernel
theorem c1730 : check 60 115 18 1730 = true := by decide +kernel
theorem c1731 : check 60 115 18 1731 = true := by decide +kernel
theorem c1732 : check 60 115 18 1732 = true := by decide +kernel
theorem c1733 : check 60 115 18 1733 = true := by decide +kernel
theorem c1734 : check 60 115 18 1734 = true := by decide +kernel
theorem c1735 : check 60 115 18 1735 = true := by decide +kernel
theorem c1736 : check 60 115 18 1736 = true := by decide +kernel
theorem c1737 : check 60 115 18 1737 = true := by decide +kernel
theorem c1738 : check 60 115 18 1738 = true := by decide +kernel
theorem c1739 : check 60 115 18 1739 = true := by decide +kernel
theorem c1740 : check 60 115 18 1740 = true := by decide +kernel
theorem c1741 : check 60 115 18 1741 = true := by decide +kernel
theorem c1742 : check 60 115 18 1742 = true := by decide +kernel
theorem c1743 : check 60 115 18 1743 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1728 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1728) (chunksOK_one c1729)) (chunksOK_append (chunksOK_one c1730) (chunksOK_one c1731))) (chunksOK_append (chunksOK_append (chunksOK_one c1732) (chunksOK_one c1733)) (chunksOK_append (chunksOK_one c1734) (chunksOK_one c1735)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1736) (chunksOK_one c1737)) (chunksOK_append (chunksOK_one c1738) (chunksOK_one c1739))) (chunksOK_append (chunksOK_append (chunksOK_one c1740) (chunksOK_one c1741)) (chunksOK_append (chunksOK_one c1742) (chunksOK_one c1743)))))

end C108

namespace C109

theorem c1744 : check 60 115 18 1744 = true := by decide +kernel
theorem c1745 : check 60 115 18 1745 = true := by decide +kernel
theorem c1746 : check 60 115 18 1746 = true := by decide +kernel
theorem c1747 : check 60 115 18 1747 = true := by decide +kernel
theorem c1748 : check 60 115 18 1748 = true := by decide +kernel
theorem c1749 : check 60 115 18 1749 = true := by decide +kernel
theorem c1750 : check 60 115 18 1750 = true := by decide +kernel
theorem c1751 : check 60 115 18 1751 = true := by decide +kernel
theorem c1752 : check 60 115 18 1752 = true := by decide +kernel
theorem c1753 : check 60 115 18 1753 = true := by decide +kernel
theorem c1754 : check 60 115 18 1754 = true := by decide +kernel
theorem c1755 : check 60 115 18 1755 = true := by decide +kernel
theorem c1756 : check 60 115 18 1756 = true := by decide +kernel
theorem c1757 : check 60 115 18 1757 = true := by decide +kernel
theorem c1758 : check 60 115 18 1758 = true := by decide +kernel
theorem c1759 : check 60 115 18 1759 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1744 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1744) (chunksOK_one c1745)) (chunksOK_append (chunksOK_one c1746) (chunksOK_one c1747))) (chunksOK_append (chunksOK_append (chunksOK_one c1748) (chunksOK_one c1749)) (chunksOK_append (chunksOK_one c1750) (chunksOK_one c1751)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1752) (chunksOK_one c1753)) (chunksOK_append (chunksOK_one c1754) (chunksOK_one c1755))) (chunksOK_append (chunksOK_append (chunksOK_one c1756) (chunksOK_one c1757)) (chunksOK_append (chunksOK_one c1758) (chunksOK_one c1759)))))

end C109

namespace C110

theorem c1760 : check 60 115 18 1760 = true := by decide +kernel
theorem c1761 : check 60 115 18 1761 = true := by decide +kernel
theorem c1762 : check 60 115 18 1762 = true := by decide +kernel
theorem c1763 : check 60 115 18 1763 = true := by decide +kernel
theorem c1764 : check 60 115 18 1764 = true := by decide +kernel
theorem c1765 : check 60 115 18 1765 = true := by decide +kernel
theorem c1766 : check 60 115 18 1766 = true := by decide +kernel
theorem c1767 : check 60 115 18 1767 = true := by decide +kernel
theorem c1768 : check 60 115 18 1768 = true := by decide +kernel
theorem c1769 : check 60 115 18 1769 = true := by decide +kernel
theorem c1770 : check 60 115 18 1770 = true := by decide +kernel
theorem c1771 : check 60 115 18 1771 = true := by decide +kernel
theorem c1772 : check 60 115 18 1772 = true := by decide +kernel
theorem c1773 : check 60 115 18 1773 = true := by decide +kernel
theorem c1774 : check 60 115 18 1774 = true := by decide +kernel
theorem c1775 : check 60 115 18 1775 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1760 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1760) (chunksOK_one c1761)) (chunksOK_append (chunksOK_one c1762) (chunksOK_one c1763))) (chunksOK_append (chunksOK_append (chunksOK_one c1764) (chunksOK_one c1765)) (chunksOK_append (chunksOK_one c1766) (chunksOK_one c1767)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1768) (chunksOK_one c1769)) (chunksOK_append (chunksOK_one c1770) (chunksOK_one c1771))) (chunksOK_append (chunksOK_append (chunksOK_one c1772) (chunksOK_one c1773)) (chunksOK_append (chunksOK_one c1774) (chunksOK_one c1775)))))

end C110

namespace C111

theorem c1776 : check 60 115 18 1776 = true := by decide +kernel
theorem c1777 : check 60 115 18 1777 = true := by decide +kernel
theorem c1778 : check 60 115 18 1778 = true := by decide +kernel
theorem c1779 : check 60 115 18 1779 = true := by decide +kernel
theorem c1780 : check 60 115 18 1780 = true := by decide +kernel
theorem c1781 : check 60 115 18 1781 = true := by decide +kernel
theorem c1782 : check 60 115 18 1782 = true := by decide +kernel
theorem c1783 : check 60 115 18 1783 = true := by decide +kernel
theorem c1784 : check 60 115 18 1784 = true := by decide +kernel
theorem c1785 : check 60 115 18 1785 = true := by decide +kernel
theorem c1786 : check 60 115 18 1786 = true := by decide +kernel
theorem c1787 : check 60 115 18 1787 = true := by decide +kernel
theorem c1788 : check 60 115 18 1788 = true := by decide +kernel
theorem c1789 : check 60 115 18 1789 = true := by decide +kernel
theorem c1790 : check 60 115 18 1790 = true := by decide +kernel
theorem c1791 : check 60 115 18 1791 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1776 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1776) (chunksOK_one c1777)) (chunksOK_append (chunksOK_one c1778) (chunksOK_one c1779))) (chunksOK_append (chunksOK_append (chunksOK_one c1780) (chunksOK_one c1781)) (chunksOK_append (chunksOK_one c1782) (chunksOK_one c1783)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1784) (chunksOK_one c1785)) (chunksOK_append (chunksOK_one c1786) (chunksOK_one c1787))) (chunksOK_append (chunksOK_append (chunksOK_one c1788) (chunksOK_one c1789)) (chunksOK_append (chunksOK_one c1790) (chunksOK_one c1791)))))

end C111

namespace C112

theorem c1792 : check 60 115 18 1792 = true := by decide +kernel
theorem c1793 : check 60 115 18 1793 = true := by decide +kernel
theorem c1794 : check 60 115 18 1794 = true := by decide +kernel
theorem c1795 : check 60 115 18 1795 = true := by decide +kernel
theorem c1796 : check 60 115 18 1796 = true := by decide +kernel
theorem c1797 : check 60 115 18 1797 = true := by decide +kernel
theorem c1798 : check 60 115 18 1798 = true := by decide +kernel
theorem c1799 : check 60 115 18 1799 = true := by decide +kernel
theorem c1800 : check 60 115 18 1800 = true := by decide +kernel
theorem c1801 : check 60 115 18 1801 = true := by decide +kernel
theorem c1802 : check 60 115 18 1802 = true := by decide +kernel
theorem c1803 : check 60 115 18 1803 = true := by decide +kernel
theorem c1804 : check 60 115 18 1804 = true := by decide +kernel
theorem c1805 : check 60 115 18 1805 = true := by decide +kernel
theorem c1806 : check 60 115 18 1806 = true := by decide +kernel
theorem c1807 : check 60 115 18 1807 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1792 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1792) (chunksOK_one c1793)) (chunksOK_append (chunksOK_one c1794) (chunksOK_one c1795))) (chunksOK_append (chunksOK_append (chunksOK_one c1796) (chunksOK_one c1797)) (chunksOK_append (chunksOK_one c1798) (chunksOK_one c1799)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1800) (chunksOK_one c1801)) (chunksOK_append (chunksOK_one c1802) (chunksOK_one c1803))) (chunksOK_append (chunksOK_append (chunksOK_one c1804) (chunksOK_one c1805)) (chunksOK_append (chunksOK_one c1806) (chunksOK_one c1807)))))

end C112

namespace C113

theorem c1808 : check 60 115 18 1808 = true := by decide +kernel
theorem c1809 : check 60 115 18 1809 = true := by decide +kernel
theorem c1810 : check 60 115 18 1810 = true := by decide +kernel
theorem c1811 : check 60 115 18 1811 = true := by decide +kernel
theorem c1812 : check 60 115 18 1812 = true := by decide +kernel
theorem c1813 : check 60 115 18 1813 = true := by decide +kernel
theorem c1814 : check 60 115 18 1814 = true := by decide +kernel
theorem c1815 : check 60 115 18 1815 = true := by decide +kernel
theorem c1816 : check 60 115 18 1816 = true := by decide +kernel
theorem c1817 : check 60 115 18 1817 = true := by decide +kernel
theorem c1818 : check 60 115 18 1818 = true := by decide +kernel
theorem c1819 : check 60 115 18 1819 = true := by decide +kernel
theorem c1820 : check 60 115 18 1820 = true := by decide +kernel
theorem c1821 : check 60 115 18 1821 = true := by decide +kernel
theorem c1822 : check 60 115 18 1822 = true := by decide +kernel
theorem c1823 : check 60 115 18 1823 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1808 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1808) (chunksOK_one c1809)) (chunksOK_append (chunksOK_one c1810) (chunksOK_one c1811))) (chunksOK_append (chunksOK_append (chunksOK_one c1812) (chunksOK_one c1813)) (chunksOK_append (chunksOK_one c1814) (chunksOK_one c1815)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1816) (chunksOK_one c1817)) (chunksOK_append (chunksOK_one c1818) (chunksOK_one c1819))) (chunksOK_append (chunksOK_append (chunksOK_one c1820) (chunksOK_one c1821)) (chunksOK_append (chunksOK_one c1822) (chunksOK_one c1823)))))

end C113

namespace C114

theorem c1824 : check 60 115 18 1824 = true := by decide +kernel
theorem c1825 : check 60 115 18 1825 = true := by decide +kernel
theorem c1826 : check 60 115 18 1826 = true := by decide +kernel
theorem c1827 : check 60 115 18 1827 = true := by decide +kernel
theorem c1828 : check 60 115 18 1828 = true := by decide +kernel
theorem c1829 : check 60 115 18 1829 = true := by decide +kernel
theorem c1830 : check 60 115 18 1830 = true := by decide +kernel
theorem c1831 : check 60 115 18 1831 = true := by decide +kernel
theorem c1832 : check 60 115 18 1832 = true := by decide +kernel
theorem c1833 : check 60 115 18 1833 = true := by decide +kernel
theorem c1834 : check 60 115 18 1834 = true := by decide +kernel
theorem c1835 : check 60 115 18 1835 = true := by decide +kernel
theorem c1836 : check 60 115 18 1836 = true := by decide +kernel
theorem c1837 : check 60 115 18 1837 = true := by decide +kernel
theorem c1838 : check 60 115 18 1838 = true := by decide +kernel
theorem c1839 : check 60 115 18 1839 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1824 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1824) (chunksOK_one c1825)) (chunksOK_append (chunksOK_one c1826) (chunksOK_one c1827))) (chunksOK_append (chunksOK_append (chunksOK_one c1828) (chunksOK_one c1829)) (chunksOK_append (chunksOK_one c1830) (chunksOK_one c1831)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1832) (chunksOK_one c1833)) (chunksOK_append (chunksOK_one c1834) (chunksOK_one c1835))) (chunksOK_append (chunksOK_append (chunksOK_one c1836) (chunksOK_one c1837)) (chunksOK_append (chunksOK_one c1838) (chunksOK_one c1839)))))

end C114

namespace C115

theorem c1840 : check 60 115 18 1840 = true := by decide +kernel
theorem c1841 : check 60 115 18 1841 = true := by decide +kernel
theorem c1842 : check 60 115 18 1842 = true := by decide +kernel
theorem c1843 : check 60 115 18 1843 = true := by decide +kernel
theorem c1844 : check 60 115 18 1844 = true := by decide +kernel
theorem c1845 : check 60 115 18 1845 = true := by decide +kernel
theorem c1846 : check 60 115 18 1846 = true := by decide +kernel
theorem c1847 : check 60 115 18 1847 = true := by decide +kernel
theorem c1848 : check 60 115 18 1848 = true := by decide +kernel
theorem c1849 : check 60 115 18 1849 = true := by decide +kernel
theorem c1850 : check 60 115 18 1850 = true := by decide +kernel
theorem c1851 : check 60 115 18 1851 = true := by decide +kernel
theorem c1852 : check 60 115 18 1852 = true := by decide +kernel
theorem c1853 : check 60 115 18 1853 = true := by decide +kernel
theorem c1854 : check 60 115 18 1854 = true := by decide +kernel
theorem c1855 : check 60 115 18 1855 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1840 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1840) (chunksOK_one c1841)) (chunksOK_append (chunksOK_one c1842) (chunksOK_one c1843))) (chunksOK_append (chunksOK_append (chunksOK_one c1844) (chunksOK_one c1845)) (chunksOK_append (chunksOK_one c1846) (chunksOK_one c1847)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1848) (chunksOK_one c1849)) (chunksOK_append (chunksOK_one c1850) (chunksOK_one c1851))) (chunksOK_append (chunksOK_append (chunksOK_one c1852) (chunksOK_one c1853)) (chunksOK_append (chunksOK_one c1854) (chunksOK_one c1855)))))

end C115

namespace C116

theorem c1856 : check 60 115 18 1856 = true := by decide +kernel
theorem c1857 : check 60 115 18 1857 = true := by decide +kernel
theorem c1858 : check 60 115 18 1858 = true := by decide +kernel
theorem c1859 : check 60 115 18 1859 = true := by decide +kernel
theorem c1860 : check 60 115 18 1860 = true := by decide +kernel
theorem c1861 : check 60 115 18 1861 = true := by decide +kernel
theorem c1862 : check 60 115 18 1862 = true := by decide +kernel
theorem c1863 : check 60 115 18 1863 = true := by decide +kernel
theorem c1864 : check 60 115 18 1864 = true := by decide +kernel
theorem c1865 : check 60 115 18 1865 = true := by decide +kernel
theorem c1866 : check 60 115 18 1866 = true := by decide +kernel
theorem c1867 : check 60 115 18 1867 = true := by decide +kernel
theorem c1868 : check 60 115 18 1868 = true := by decide +kernel
theorem c1869 : check 60 115 18 1869 = true := by decide +kernel
theorem c1870 : check 60 115 18 1870 = true := by decide +kernel
theorem c1871 : check 60 115 18 1871 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1856 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1856) (chunksOK_one c1857)) (chunksOK_append (chunksOK_one c1858) (chunksOK_one c1859))) (chunksOK_append (chunksOK_append (chunksOK_one c1860) (chunksOK_one c1861)) (chunksOK_append (chunksOK_one c1862) (chunksOK_one c1863)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1864) (chunksOK_one c1865)) (chunksOK_append (chunksOK_one c1866) (chunksOK_one c1867))) (chunksOK_append (chunksOK_append (chunksOK_one c1868) (chunksOK_one c1869)) (chunksOK_append (chunksOK_one c1870) (chunksOK_one c1871)))))

end C116

namespace C117

theorem c1872 : check 60 115 18 1872 = true := by decide +kernel
theorem c1873 : check 60 115 18 1873 = true := by decide +kernel
theorem c1874 : check 60 115 18 1874 = true := by decide +kernel
theorem c1875 : check 60 115 18 1875 = true := by decide +kernel
theorem c1876 : check 60 115 18 1876 = true := by decide +kernel
theorem c1877 : check 60 115 18 1877 = true := by decide +kernel
theorem c1878 : check 60 115 18 1878 = true := by decide +kernel
theorem c1879 : check 60 115 18 1879 = true := by decide +kernel
theorem c1880 : check 60 115 18 1880 = true := by decide +kernel
theorem c1881 : check 60 115 18 1881 = true := by decide +kernel
theorem c1882 : check 60 115 18 1882 = true := by decide +kernel
theorem c1883 : check 60 115 18 1883 = true := by decide +kernel
theorem c1884 : check 60 115 18 1884 = true := by decide +kernel
theorem c1885 : check 60 115 18 1885 = true := by decide +kernel
theorem c1886 : check 60 115 18 1886 = true := by decide +kernel
theorem c1887 : check 60 115 18 1887 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1872 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1872) (chunksOK_one c1873)) (chunksOK_append (chunksOK_one c1874) (chunksOK_one c1875))) (chunksOK_append (chunksOK_append (chunksOK_one c1876) (chunksOK_one c1877)) (chunksOK_append (chunksOK_one c1878) (chunksOK_one c1879)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1880) (chunksOK_one c1881)) (chunksOK_append (chunksOK_one c1882) (chunksOK_one c1883))) (chunksOK_append (chunksOK_append (chunksOK_one c1884) (chunksOK_one c1885)) (chunksOK_append (chunksOK_one c1886) (chunksOK_one c1887)))))

end C117

namespace C118

theorem c1888 : check 60 115 18 1888 = true := by decide +kernel
theorem c1889 : check 60 115 18 1889 = true := by decide +kernel
theorem c1890 : check 60 115 18 1890 = true := by decide +kernel
theorem c1891 : check 60 115 18 1891 = true := by decide +kernel
theorem c1892 : check 60 115 18 1892 = true := by decide +kernel
theorem c1893 : check 60 115 18 1893 = true := by decide +kernel
theorem c1894 : check 60 115 18 1894 = true := by decide +kernel
theorem c1895 : check 60 115 18 1895 = true := by decide +kernel
theorem c1896 : check 60 115 18 1896 = true := by decide +kernel
theorem c1897 : check 60 115 18 1897 = true := by decide +kernel
theorem c1898 : check 60 115 18 1898 = true := by decide +kernel
theorem c1899 : check 60 115 18 1899 = true := by decide +kernel
theorem c1900 : check 60 115 18 1900 = true := by decide +kernel
theorem c1901 : check 60 115 18 1901 = true := by decide +kernel
theorem c1902 : check 60 115 18 1902 = true := by decide +kernel
theorem c1903 : check 60 115 18 1903 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1888 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1888) (chunksOK_one c1889)) (chunksOK_append (chunksOK_one c1890) (chunksOK_one c1891))) (chunksOK_append (chunksOK_append (chunksOK_one c1892) (chunksOK_one c1893)) (chunksOK_append (chunksOK_one c1894) (chunksOK_one c1895)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1896) (chunksOK_one c1897)) (chunksOK_append (chunksOK_one c1898) (chunksOK_one c1899))) (chunksOK_append (chunksOK_append (chunksOK_one c1900) (chunksOK_one c1901)) (chunksOK_append (chunksOK_one c1902) (chunksOK_one c1903)))))

end C118

namespace C119

theorem c1904 : check 60 115 18 1904 = true := by decide +kernel
theorem c1905 : check 60 115 18 1905 = true := by decide +kernel
theorem c1906 : check 60 115 18 1906 = true := by decide +kernel
theorem c1907 : check 60 115 18 1907 = true := by decide +kernel
theorem c1908 : check 60 115 18 1908 = true := by decide +kernel
theorem c1909 : check 60 115 18 1909 = true := by decide +kernel
theorem c1910 : check 60 115 18 1910 = true := by decide +kernel
theorem c1911 : check 60 115 18 1911 = true := by decide +kernel
theorem c1912 : check 60 115 18 1912 = true := by decide +kernel
theorem c1913 : check 60 115 18 1913 = true := by decide +kernel
theorem c1914 : check 60 115 18 1914 = true := by decide +kernel
theorem c1915 : check 60 115 18 1915 = true := by decide +kernel
theorem c1916 : check 60 115 18 1916 = true := by decide +kernel
theorem c1917 : check 60 115 18 1917 = true := by decide +kernel
theorem c1918 : check 60 115 18 1918 = true := by decide +kernel
theorem c1919 : check 60 115 18 1919 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1904 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1904) (chunksOK_one c1905)) (chunksOK_append (chunksOK_one c1906) (chunksOK_one c1907))) (chunksOK_append (chunksOK_append (chunksOK_one c1908) (chunksOK_one c1909)) (chunksOK_append (chunksOK_one c1910) (chunksOK_one c1911)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1912) (chunksOK_one c1913)) (chunksOK_append (chunksOK_one c1914) (chunksOK_one c1915))) (chunksOK_append (chunksOK_append (chunksOK_one c1916) (chunksOK_one c1917)) (chunksOK_append (chunksOK_one c1918) (chunksOK_one c1919)))))

end C119

namespace C120

theorem c1920 : check 60 115 18 1920 = true := by decide +kernel
theorem c1921 : check 60 115 18 1921 = true := by decide +kernel
theorem c1922 : check 60 115 18 1922 = true := by decide +kernel
theorem c1923 : check 60 115 18 1923 = true := by decide +kernel
theorem c1924 : check 60 115 18 1924 = true := by decide +kernel
theorem c1925 : check 60 115 18 1925 = true := by decide +kernel
theorem c1926 : check 60 115 18 1926 = true := by decide +kernel
theorem c1927 : check 60 115 18 1927 = true := by decide +kernel
theorem c1928 : check 60 115 18 1928 = true := by decide +kernel
theorem c1929 : check 60 115 18 1929 = true := by decide +kernel
theorem c1930 : check 60 115 18 1930 = true := by decide +kernel
theorem c1931 : check 60 115 18 1931 = true := by decide +kernel
theorem c1932 : check 60 115 18 1932 = true := by decide +kernel
theorem c1933 : check 60 115 18 1933 = true := by decide +kernel
theorem c1934 : check 60 115 18 1934 = true := by decide +kernel
theorem c1935 : check 60 115 18 1935 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1920 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1920) (chunksOK_one c1921)) (chunksOK_append (chunksOK_one c1922) (chunksOK_one c1923))) (chunksOK_append (chunksOK_append (chunksOK_one c1924) (chunksOK_one c1925)) (chunksOK_append (chunksOK_one c1926) (chunksOK_one c1927)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1928) (chunksOK_one c1929)) (chunksOK_append (chunksOK_one c1930) (chunksOK_one c1931))) (chunksOK_append (chunksOK_append (chunksOK_one c1932) (chunksOK_one c1933)) (chunksOK_append (chunksOK_one c1934) (chunksOK_one c1935)))))

end C120

namespace C121

theorem c1936 : check 60 115 18 1936 = true := by decide +kernel
theorem c1937 : check 60 115 18 1937 = true := by decide +kernel
theorem c1938 : check 60 115 18 1938 = true := by decide +kernel
theorem c1939 : check 60 115 18 1939 = true := by decide +kernel
theorem c1940 : check 60 115 18 1940 = true := by decide +kernel
theorem c1941 : check 60 115 18 1941 = true := by decide +kernel
theorem c1942 : check 60 115 18 1942 = true := by decide +kernel
theorem c1943 : check 60 115 18 1943 = true := by decide +kernel
theorem c1944 : check 60 115 18 1944 = true := by decide +kernel
theorem c1945 : check 60 115 18 1945 = true := by decide +kernel
theorem c1946 : check 60 115 18 1946 = true := by decide +kernel
theorem c1947 : check 60 115 18 1947 = true := by decide +kernel
theorem c1948 : check 60 115 18 1948 = true := by decide +kernel
theorem c1949 : check 60 115 18 1949 = true := by decide +kernel
theorem c1950 : check 60 115 18 1950 = true := by decide +kernel
theorem c1951 : check 60 115 18 1951 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1936 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1936) (chunksOK_one c1937)) (chunksOK_append (chunksOK_one c1938) (chunksOK_one c1939))) (chunksOK_append (chunksOK_append (chunksOK_one c1940) (chunksOK_one c1941)) (chunksOK_append (chunksOK_one c1942) (chunksOK_one c1943)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1944) (chunksOK_one c1945)) (chunksOK_append (chunksOK_one c1946) (chunksOK_one c1947))) (chunksOK_append (chunksOK_append (chunksOK_one c1948) (chunksOK_one c1949)) (chunksOK_append (chunksOK_one c1950) (chunksOK_one c1951)))))

end C121

namespace C122

theorem c1952 : check 60 115 18 1952 = true := by decide +kernel
theorem c1953 : check 60 115 18 1953 = true := by decide +kernel
theorem c1954 : check 60 115 18 1954 = true := by decide +kernel
theorem c1955 : check 60 115 18 1955 = true := by decide +kernel
theorem c1956 : check 60 115 18 1956 = true := by decide +kernel
theorem c1957 : check 60 115 18 1957 = true := by decide +kernel
theorem c1958 : check 60 115 18 1958 = true := by decide +kernel
theorem c1959 : check 60 115 18 1959 = true := by decide +kernel
theorem c1960 : check 60 115 18 1960 = true := by decide +kernel
theorem c1961 : check 60 115 18 1961 = true := by decide +kernel
theorem c1962 : check 60 115 18 1962 = true := by decide +kernel
theorem c1963 : check 60 115 18 1963 = true := by decide +kernel
theorem c1964 : check 60 115 18 1964 = true := by decide +kernel
theorem c1965 : check 60 115 18 1965 = true := by decide +kernel
theorem c1966 : check 60 115 18 1966 = true := by decide +kernel
theorem c1967 : check 60 115 18 1967 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1952 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1952) (chunksOK_one c1953)) (chunksOK_append (chunksOK_one c1954) (chunksOK_one c1955))) (chunksOK_append (chunksOK_append (chunksOK_one c1956) (chunksOK_one c1957)) (chunksOK_append (chunksOK_one c1958) (chunksOK_one c1959)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1960) (chunksOK_one c1961)) (chunksOK_append (chunksOK_one c1962) (chunksOK_one c1963))) (chunksOK_append (chunksOK_append (chunksOK_one c1964) (chunksOK_one c1965)) (chunksOK_append (chunksOK_one c1966) (chunksOK_one c1967)))))

end C122

namespace C123

theorem c1968 : check 60 115 18 1968 = true := by decide +kernel
theorem c1969 : check 60 115 18 1969 = true := by decide +kernel
theorem c1970 : check 60 115 18 1970 = true := by decide +kernel
theorem c1971 : check 60 115 18 1971 = true := by decide +kernel
theorem c1972 : check 60 115 18 1972 = true := by decide +kernel
theorem c1973 : check 60 115 18 1973 = true := by decide +kernel
theorem c1974 : check 60 115 18 1974 = true := by decide +kernel
theorem c1975 : check 60 115 18 1975 = true := by decide +kernel
theorem c1976 : check 60 115 18 1976 = true := by decide +kernel
theorem c1977 : check 60 115 18 1977 = true := by decide +kernel
theorem c1978 : check 60 115 18 1978 = true := by decide +kernel
theorem c1979 : check 60 115 18 1979 = true := by decide +kernel
theorem c1980 : check 60 115 18 1980 = true := by decide +kernel
theorem c1981 : check 60 115 18 1981 = true := by decide +kernel
theorem c1982 : check 60 115 18 1982 = true := by decide +kernel
theorem c1983 : check 60 115 18 1983 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1968 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1968) (chunksOK_one c1969)) (chunksOK_append (chunksOK_one c1970) (chunksOK_one c1971))) (chunksOK_append (chunksOK_append (chunksOK_one c1972) (chunksOK_one c1973)) (chunksOK_append (chunksOK_one c1974) (chunksOK_one c1975)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1976) (chunksOK_one c1977)) (chunksOK_append (chunksOK_one c1978) (chunksOK_one c1979))) (chunksOK_append (chunksOK_append (chunksOK_one c1980) (chunksOK_one c1981)) (chunksOK_append (chunksOK_one c1982) (chunksOK_one c1983)))))

end C123

namespace C124

theorem c1984 : check 60 115 18 1984 = true := by decide +kernel
theorem c1985 : check 60 115 18 1985 = true := by decide +kernel
theorem c1986 : check 60 115 18 1986 = true := by decide +kernel
theorem c1987 : check 60 115 18 1987 = true := by decide +kernel
theorem c1988 : check 60 115 18 1988 = true := by decide +kernel
theorem c1989 : check 60 115 18 1989 = true := by decide +kernel
theorem c1990 : check 60 115 18 1990 = true := by decide +kernel
theorem c1991 : check 60 115 18 1991 = true := by decide +kernel
theorem c1992 : check 60 115 18 1992 = true := by decide +kernel
theorem c1993 : check 60 115 18 1993 = true := by decide +kernel
theorem c1994 : check 60 115 18 1994 = true := by decide +kernel
theorem c1995 : check 60 115 18 1995 = true := by decide +kernel
theorem c1996 : check 60 115 18 1996 = true := by decide +kernel
theorem c1997 : check 60 115 18 1997 = true := by decide +kernel
theorem c1998 : check 60 115 18 1998 = true := by decide +kernel
theorem c1999 : check 60 115 18 1999 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 1984 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1984) (chunksOK_one c1985)) (chunksOK_append (chunksOK_one c1986) (chunksOK_one c1987))) (chunksOK_append (chunksOK_append (chunksOK_one c1988) (chunksOK_one c1989)) (chunksOK_append (chunksOK_one c1990) (chunksOK_one c1991)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1992) (chunksOK_one c1993)) (chunksOK_append (chunksOK_one c1994) (chunksOK_one c1995))) (chunksOK_append (chunksOK_append (chunksOK_one c1996) (chunksOK_one c1997)) (chunksOK_append (chunksOK_one c1998) (chunksOK_one c1999)))))

end C124

namespace C125

theorem c2000 : check 60 115 18 2000 = true := by decide +kernel
theorem c2001 : check 60 115 18 2001 = true := by decide +kernel
theorem c2002 : check 60 115 18 2002 = true := by decide +kernel
theorem c2003 : check 60 115 18 2003 = true := by decide +kernel
theorem c2004 : check 60 115 18 2004 = true := by decide +kernel
theorem c2005 : check 60 115 18 2005 = true := by decide +kernel
theorem c2006 : check 60 115 18 2006 = true := by decide +kernel
theorem c2007 : check 60 115 18 2007 = true := by decide +kernel
theorem c2008 : check 60 115 18 2008 = true := by decide +kernel
theorem c2009 : check 60 115 18 2009 = true := by decide +kernel
theorem c2010 : check 60 115 18 2010 = true := by decide +kernel
theorem c2011 : check 60 115 18 2011 = true := by decide +kernel
theorem c2012 : check 60 115 18 2012 = true := by decide +kernel
theorem c2013 : check 60 115 18 2013 = true := by decide +kernel
theorem c2014 : check 60 115 18 2014 = true := by decide +kernel
theorem c2015 : check 60 115 18 2015 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2000 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2000) (chunksOK_one c2001)) (chunksOK_append (chunksOK_one c2002) (chunksOK_one c2003))) (chunksOK_append (chunksOK_append (chunksOK_one c2004) (chunksOK_one c2005)) (chunksOK_append (chunksOK_one c2006) (chunksOK_one c2007)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2008) (chunksOK_one c2009)) (chunksOK_append (chunksOK_one c2010) (chunksOK_one c2011))) (chunksOK_append (chunksOK_append (chunksOK_one c2012) (chunksOK_one c2013)) (chunksOK_append (chunksOK_one c2014) (chunksOK_one c2015)))))

end C125

namespace C126

theorem c2016 : check 60 115 18 2016 = true := by decide +kernel
theorem c2017 : check 60 115 18 2017 = true := by decide +kernel
theorem c2018 : check 60 115 18 2018 = true := by decide +kernel
theorem c2019 : check 60 115 18 2019 = true := by decide +kernel
theorem c2020 : check 60 115 18 2020 = true := by decide +kernel
theorem c2021 : check 60 115 18 2021 = true := by decide +kernel
theorem c2022 : check 60 115 18 2022 = true := by decide +kernel
theorem c2023 : check 60 115 18 2023 = true := by decide +kernel
theorem c2024 : check 60 115 18 2024 = true := by decide +kernel
theorem c2025 : check 60 115 18 2025 = true := by decide +kernel
theorem c2026 : check 60 115 18 2026 = true := by decide +kernel
theorem c2027 : check 60 115 18 2027 = true := by decide +kernel
theorem c2028 : check 60 115 18 2028 = true := by decide +kernel
theorem c2029 : check 60 115 18 2029 = true := by decide +kernel
theorem c2030 : check 60 115 18 2030 = true := by decide +kernel
theorem c2031 : check 60 115 18 2031 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2016 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2016) (chunksOK_one c2017)) (chunksOK_append (chunksOK_one c2018) (chunksOK_one c2019))) (chunksOK_append (chunksOK_append (chunksOK_one c2020) (chunksOK_one c2021)) (chunksOK_append (chunksOK_one c2022) (chunksOK_one c2023)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2024) (chunksOK_one c2025)) (chunksOK_append (chunksOK_one c2026) (chunksOK_one c2027))) (chunksOK_append (chunksOK_append (chunksOK_one c2028) (chunksOK_one c2029)) (chunksOK_append (chunksOK_one c2030) (chunksOK_one c2031)))))

end C126

namespace C127

theorem c2032 : check 60 115 18 2032 = true := by decide +kernel
theorem c2033 : check 60 115 18 2033 = true := by decide +kernel
theorem c2034 : check 60 115 18 2034 = true := by decide +kernel
theorem c2035 : check 60 115 18 2035 = true := by decide +kernel
theorem c2036 : check 60 115 18 2036 = true := by decide +kernel
theorem c2037 : check 60 115 18 2037 = true := by decide +kernel
theorem c2038 : check 60 115 18 2038 = true := by decide +kernel
theorem c2039 : check 60 115 18 2039 = true := by decide +kernel
theorem c2040 : check 60 115 18 2040 = true := by decide +kernel
theorem c2041 : check 60 115 18 2041 = true := by decide +kernel
theorem c2042 : check 60 115 18 2042 = true := by decide +kernel
theorem c2043 : check 60 115 18 2043 = true := by decide +kernel
theorem c2044 : check 60 115 18 2044 = true := by decide +kernel
theorem c2045 : check 60 115 18 2045 = true := by decide +kernel
theorem c2046 : check 60 115 18 2046 = true := by decide +kernel
theorem c2047 : check 60 115 18 2047 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2032 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2032) (chunksOK_one c2033)) (chunksOK_append (chunksOK_one c2034) (chunksOK_one c2035))) (chunksOK_append (chunksOK_append (chunksOK_one c2036) (chunksOK_one c2037)) (chunksOK_append (chunksOK_one c2038) (chunksOK_one c2039)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2040) (chunksOK_one c2041)) (chunksOK_append (chunksOK_one c2042) (chunksOK_one c2043))) (chunksOK_append (chunksOK_append (chunksOK_one c2044) (chunksOK_one c2045)) (chunksOK_append (chunksOK_one c2046) (chunksOK_one c2047)))))

end C127

namespace C128

theorem c2048 : check 60 115 18 2048 = true := by decide +kernel
theorem c2049 : check 60 115 18 2049 = true := by decide +kernel
theorem c2050 : check 60 115 18 2050 = true := by decide +kernel
theorem c2051 : check 60 115 18 2051 = true := by decide +kernel
theorem c2052 : check 60 115 18 2052 = true := by decide +kernel
theorem c2053 : check 60 115 18 2053 = true := by decide +kernel
theorem c2054 : check 60 115 18 2054 = true := by decide +kernel
theorem c2055 : check 60 115 18 2055 = true := by decide +kernel
theorem c2056 : check 60 115 18 2056 = true := by decide +kernel
theorem c2057 : check 60 115 18 2057 = true := by decide +kernel
theorem c2058 : check 60 115 18 2058 = true := by decide +kernel
theorem c2059 : check 60 115 18 2059 = true := by decide +kernel
theorem c2060 : check 60 115 18 2060 = true := by decide +kernel
theorem c2061 : check 60 115 18 2061 = true := by decide +kernel
theorem c2062 : check 60 115 18 2062 = true := by decide +kernel
theorem c2063 : check 60 115 18 2063 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2048 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2048) (chunksOK_one c2049)) (chunksOK_append (chunksOK_one c2050) (chunksOK_one c2051))) (chunksOK_append (chunksOK_append (chunksOK_one c2052) (chunksOK_one c2053)) (chunksOK_append (chunksOK_one c2054) (chunksOK_one c2055)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2056) (chunksOK_one c2057)) (chunksOK_append (chunksOK_one c2058) (chunksOK_one c2059))) (chunksOK_append (chunksOK_append (chunksOK_one c2060) (chunksOK_one c2061)) (chunksOK_append (chunksOK_one c2062) (chunksOK_one c2063)))))

end C128

namespace C129

theorem c2064 : check 60 115 18 2064 = true := by decide +kernel
theorem c2065 : check 60 115 18 2065 = true := by decide +kernel
theorem c2066 : check 60 115 18 2066 = true := by decide +kernel
theorem c2067 : check 60 115 18 2067 = true := by decide +kernel
theorem c2068 : check 60 115 18 2068 = true := by decide +kernel
theorem c2069 : check 60 115 18 2069 = true := by decide +kernel
theorem c2070 : check 60 115 18 2070 = true := by decide +kernel
theorem c2071 : check 60 115 18 2071 = true := by decide +kernel
theorem c2072 : check 60 115 18 2072 = true := by decide +kernel
theorem c2073 : check 60 115 18 2073 = true := by decide +kernel
theorem c2074 : check 60 115 18 2074 = true := by decide +kernel
theorem c2075 : check 60 115 18 2075 = true := by decide +kernel
theorem c2076 : check 60 115 18 2076 = true := by decide +kernel
theorem c2077 : check 60 115 18 2077 = true := by decide +kernel
theorem c2078 : check 60 115 18 2078 = true := by decide +kernel
theorem c2079 : check 60 115 18 2079 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2064 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2064) (chunksOK_one c2065)) (chunksOK_append (chunksOK_one c2066) (chunksOK_one c2067))) (chunksOK_append (chunksOK_append (chunksOK_one c2068) (chunksOK_one c2069)) (chunksOK_append (chunksOK_one c2070) (chunksOK_one c2071)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2072) (chunksOK_one c2073)) (chunksOK_append (chunksOK_one c2074) (chunksOK_one c2075))) (chunksOK_append (chunksOK_append (chunksOK_one c2076) (chunksOK_one c2077)) (chunksOK_append (chunksOK_one c2078) (chunksOK_one c2079)))))

end C129

namespace C130

theorem c2080 : check 60 115 18 2080 = true := by decide +kernel
theorem c2081 : check 60 115 18 2081 = true := by decide +kernel
theorem c2082 : check 60 115 18 2082 = true := by decide +kernel
theorem c2083 : check 60 115 18 2083 = true := by decide +kernel
theorem c2084 : check 60 115 18 2084 = true := by decide +kernel
theorem c2085 : check 60 115 18 2085 = true := by decide +kernel
theorem c2086 : check 60 115 18 2086 = true := by decide +kernel
theorem c2087 : check 60 115 18 2087 = true := by decide +kernel
theorem c2088 : check 60 115 18 2088 = true := by decide +kernel
theorem c2089 : check 60 115 18 2089 = true := by decide +kernel
theorem c2090 : check 60 115 18 2090 = true := by decide +kernel
theorem c2091 : check 60 115 18 2091 = true := by decide +kernel
theorem c2092 : check 60 115 18 2092 = true := by decide +kernel
theorem c2093 : check 60 115 18 2093 = true := by decide +kernel
theorem c2094 : check 60 115 18 2094 = true := by decide +kernel
theorem c2095 : check 60 115 18 2095 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2080 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2080) (chunksOK_one c2081)) (chunksOK_append (chunksOK_one c2082) (chunksOK_one c2083))) (chunksOK_append (chunksOK_append (chunksOK_one c2084) (chunksOK_one c2085)) (chunksOK_append (chunksOK_one c2086) (chunksOK_one c2087)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2088) (chunksOK_one c2089)) (chunksOK_append (chunksOK_one c2090) (chunksOK_one c2091))) (chunksOK_append (chunksOK_append (chunksOK_one c2092) (chunksOK_one c2093)) (chunksOK_append (chunksOK_one c2094) (chunksOK_one c2095)))))

end C130

namespace C131

theorem c2096 : check 60 115 18 2096 = true := by decide +kernel
theorem c2097 : check 60 115 18 2097 = true := by decide +kernel
theorem c2098 : check 60 115 18 2098 = true := by decide +kernel
theorem c2099 : check 60 115 18 2099 = true := by decide +kernel
theorem c2100 : check 60 115 18 2100 = true := by decide +kernel
theorem c2101 : check 60 115 18 2101 = true := by decide +kernel
theorem c2102 : check 60 115 18 2102 = true := by decide +kernel
theorem c2103 : check 60 115 18 2103 = true := by decide +kernel
theorem c2104 : check 60 115 18 2104 = true := by decide +kernel
theorem c2105 : check 60 115 18 2105 = true := by decide +kernel
theorem c2106 : check 60 115 18 2106 = true := by decide +kernel
theorem c2107 : check 60 115 18 2107 = true := by decide +kernel
theorem c2108 : check 60 115 18 2108 = true := by decide +kernel
theorem c2109 : check 60 115 18 2109 = true := by decide +kernel
theorem c2110 : check 60 115 18 2110 = true := by decide +kernel
theorem c2111 : check 60 115 18 2111 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2096 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2096) (chunksOK_one c2097)) (chunksOK_append (chunksOK_one c2098) (chunksOK_one c2099))) (chunksOK_append (chunksOK_append (chunksOK_one c2100) (chunksOK_one c2101)) (chunksOK_append (chunksOK_one c2102) (chunksOK_one c2103)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2104) (chunksOK_one c2105)) (chunksOK_append (chunksOK_one c2106) (chunksOK_one c2107))) (chunksOK_append (chunksOK_append (chunksOK_one c2108) (chunksOK_one c2109)) (chunksOK_append (chunksOK_one c2110) (chunksOK_one c2111)))))

end C131

namespace C132

theorem c2112 : check 60 115 18 2112 = true := by decide +kernel
theorem c2113 : check 60 115 18 2113 = true := by decide +kernel
theorem c2114 : check 60 115 18 2114 = true := by decide +kernel
theorem c2115 : check 60 115 18 2115 = true := by decide +kernel
theorem c2116 : check 60 115 18 2116 = true := by decide +kernel
theorem c2117 : check 60 115 18 2117 = true := by decide +kernel
theorem c2118 : check 60 115 18 2118 = true := by decide +kernel
theorem c2119 : check 60 115 18 2119 = true := by decide +kernel
theorem c2120 : check 60 115 18 2120 = true := by decide +kernel
theorem c2121 : check 60 115 18 2121 = true := by decide +kernel
theorem c2122 : check 60 115 18 2122 = true := by decide +kernel
theorem c2123 : check 60 115 18 2123 = true := by decide +kernel
theorem c2124 : check 60 115 18 2124 = true := by decide +kernel
theorem c2125 : check 60 115 18 2125 = true := by decide +kernel
theorem c2126 : check 60 115 18 2126 = true := by decide +kernel
theorem c2127 : check 60 115 18 2127 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2112 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2112) (chunksOK_one c2113)) (chunksOK_append (chunksOK_one c2114) (chunksOK_one c2115))) (chunksOK_append (chunksOK_append (chunksOK_one c2116) (chunksOK_one c2117)) (chunksOK_append (chunksOK_one c2118) (chunksOK_one c2119)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2120) (chunksOK_one c2121)) (chunksOK_append (chunksOK_one c2122) (chunksOK_one c2123))) (chunksOK_append (chunksOK_append (chunksOK_one c2124) (chunksOK_one c2125)) (chunksOK_append (chunksOK_one c2126) (chunksOK_one c2127)))))

end C132

namespace C133

theorem c2128 : check 60 115 18 2128 = true := by decide +kernel
theorem c2129 : check 60 115 18 2129 = true := by decide +kernel
theorem c2130 : check 60 115 18 2130 = true := by decide +kernel
theorem c2131 : check 60 115 18 2131 = true := by decide +kernel
theorem c2132 : check 60 115 18 2132 = true := by decide +kernel
theorem c2133 : check 60 115 18 2133 = true := by decide +kernel
theorem c2134 : check 60 115 18 2134 = true := by decide +kernel
theorem c2135 : check 60 115 18 2135 = true := by decide +kernel
theorem c2136 : check 60 115 18 2136 = true := by decide +kernel
theorem c2137 : check 60 115 18 2137 = true := by decide +kernel
theorem c2138 : check 60 115 18 2138 = true := by decide +kernel
theorem c2139 : check 60 115 18 2139 = true := by decide +kernel
theorem c2140 : check 60 115 18 2140 = true := by decide +kernel
theorem c2141 : check 60 115 18 2141 = true := by decide +kernel
theorem c2142 : check 60 115 18 2142 = true := by decide +kernel
theorem c2143 : check 60 115 18 2143 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2128 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2128) (chunksOK_one c2129)) (chunksOK_append (chunksOK_one c2130) (chunksOK_one c2131))) (chunksOK_append (chunksOK_append (chunksOK_one c2132) (chunksOK_one c2133)) (chunksOK_append (chunksOK_one c2134) (chunksOK_one c2135)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2136) (chunksOK_one c2137)) (chunksOK_append (chunksOK_one c2138) (chunksOK_one c2139))) (chunksOK_append (chunksOK_append (chunksOK_one c2140) (chunksOK_one c2141)) (chunksOK_append (chunksOK_one c2142) (chunksOK_one c2143)))))

end C133

namespace C134

theorem c2144 : check 60 115 18 2144 = true := by decide +kernel
theorem c2145 : check 60 115 18 2145 = true := by decide +kernel
theorem c2146 : check 60 115 18 2146 = true := by decide +kernel
theorem c2147 : check 60 115 18 2147 = true := by decide +kernel
theorem c2148 : check 60 115 18 2148 = true := by decide +kernel
theorem c2149 : check 60 115 18 2149 = true := by decide +kernel
theorem c2150 : check 60 115 18 2150 = true := by decide +kernel
theorem c2151 : check 60 115 18 2151 = true := by decide +kernel
theorem c2152 : check 60 115 18 2152 = true := by decide +kernel
theorem c2153 : check 60 115 18 2153 = true := by decide +kernel
theorem c2154 : check 60 115 18 2154 = true := by decide +kernel
theorem c2155 : check 60 115 18 2155 = true := by decide +kernel
theorem c2156 : check 60 115 18 2156 = true := by decide +kernel
theorem c2157 : check 60 115 18 2157 = true := by decide +kernel
theorem c2158 : check 60 115 18 2158 = true := by decide +kernel
theorem c2159 : check 60 115 18 2159 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2144 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2144) (chunksOK_one c2145)) (chunksOK_append (chunksOK_one c2146) (chunksOK_one c2147))) (chunksOK_append (chunksOK_append (chunksOK_one c2148) (chunksOK_one c2149)) (chunksOK_append (chunksOK_one c2150) (chunksOK_one c2151)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2152) (chunksOK_one c2153)) (chunksOK_append (chunksOK_one c2154) (chunksOK_one c2155))) (chunksOK_append (chunksOK_append (chunksOK_one c2156) (chunksOK_one c2157)) (chunksOK_append (chunksOK_one c2158) (chunksOK_one c2159)))))

end C134

namespace C135

theorem c2160 : check 60 115 18 2160 = true := by decide +kernel
theorem c2161 : check 60 115 18 2161 = true := by decide +kernel
theorem c2162 : check 60 115 18 2162 = true := by decide +kernel
theorem c2163 : check 60 115 18 2163 = true := by decide +kernel
theorem c2164 : check 60 115 18 2164 = true := by decide +kernel
theorem c2165 : check 60 115 18 2165 = true := by decide +kernel
theorem c2166 : check 60 115 18 2166 = true := by decide +kernel
theorem c2167 : check 60 115 18 2167 = true := by decide +kernel
theorem c2168 : check 60 115 18 2168 = true := by decide +kernel
theorem c2169 : check 60 115 18 2169 = true := by decide +kernel
theorem c2170 : check 60 115 18 2170 = true := by decide +kernel
theorem c2171 : check 60 115 18 2171 = true := by decide +kernel
theorem c2172 : check 60 115 18 2172 = true := by decide +kernel
theorem c2173 : check 60 115 18 2173 = true := by decide +kernel
theorem c2174 : check 60 115 18 2174 = true := by decide +kernel
theorem c2175 : check 60 115 18 2175 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2160 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2160) (chunksOK_one c2161)) (chunksOK_append (chunksOK_one c2162) (chunksOK_one c2163))) (chunksOK_append (chunksOK_append (chunksOK_one c2164) (chunksOK_one c2165)) (chunksOK_append (chunksOK_one c2166) (chunksOK_one c2167)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2168) (chunksOK_one c2169)) (chunksOK_append (chunksOK_one c2170) (chunksOK_one c2171))) (chunksOK_append (chunksOK_append (chunksOK_one c2172) (chunksOK_one c2173)) (chunksOK_append (chunksOK_one c2174) (chunksOK_one c2175)))))

end C135

namespace C136

theorem c2176 : check 60 115 18 2176 = true := by decide +kernel
theorem c2177 : check 60 115 18 2177 = true := by decide +kernel
theorem c2178 : check 60 115 18 2178 = true := by decide +kernel
theorem c2179 : check 60 115 18 2179 = true := by decide +kernel
theorem c2180 : check 60 115 18 2180 = true := by decide +kernel
theorem c2181 : check 60 115 18 2181 = true := by decide +kernel
theorem c2182 : check 60 115 18 2182 = true := by decide +kernel
theorem c2183 : check 60 115 18 2183 = true := by decide +kernel
theorem c2184 : check 60 115 18 2184 = true := by decide +kernel
theorem c2185 : check 60 115 18 2185 = true := by decide +kernel
theorem c2186 : check 60 115 18 2186 = true := by decide +kernel
theorem c2187 : check 60 115 18 2187 = true := by decide +kernel
theorem c2188 : check 60 115 18 2188 = true := by decide +kernel
theorem c2189 : check 60 115 18 2189 = true := by decide +kernel
theorem c2190 : check 60 115 18 2190 = true := by decide +kernel
theorem c2191 : check 60 115 18 2191 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2176 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2176) (chunksOK_one c2177)) (chunksOK_append (chunksOK_one c2178) (chunksOK_one c2179))) (chunksOK_append (chunksOK_append (chunksOK_one c2180) (chunksOK_one c2181)) (chunksOK_append (chunksOK_one c2182) (chunksOK_one c2183)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2184) (chunksOK_one c2185)) (chunksOK_append (chunksOK_one c2186) (chunksOK_one c2187))) (chunksOK_append (chunksOK_append (chunksOK_one c2188) (chunksOK_one c2189)) (chunksOK_append (chunksOK_one c2190) (chunksOK_one c2191)))))

end C136

namespace C137

theorem c2192 : check 60 115 18 2192 = true := by decide +kernel
theorem c2193 : check 60 115 18 2193 = true := by decide +kernel
theorem c2194 : check 60 115 18 2194 = true := by decide +kernel
theorem c2195 : check 60 115 18 2195 = true := by decide +kernel
theorem c2196 : check 60 115 18 2196 = true := by decide +kernel
theorem c2197 : check 60 115 18 2197 = true := by decide +kernel
theorem c2198 : check 60 115 18 2198 = true := by decide +kernel
theorem c2199 : check 60 115 18 2199 = true := by decide +kernel
theorem c2200 : check 60 115 18 2200 = true := by decide +kernel
theorem c2201 : check 60 115 18 2201 = true := by decide +kernel
theorem c2202 : check 60 115 18 2202 = true := by decide +kernel
theorem c2203 : check 60 115 18 2203 = true := by decide +kernel
theorem c2204 : check 60 115 18 2204 = true := by decide +kernel
theorem c2205 : check 60 115 18 2205 = true := by decide +kernel
theorem c2206 : check 60 115 18 2206 = true := by decide +kernel
theorem c2207 : check 60 115 18 2207 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2192 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2192) (chunksOK_one c2193)) (chunksOK_append (chunksOK_one c2194) (chunksOK_one c2195))) (chunksOK_append (chunksOK_append (chunksOK_one c2196) (chunksOK_one c2197)) (chunksOK_append (chunksOK_one c2198) (chunksOK_one c2199)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2200) (chunksOK_one c2201)) (chunksOK_append (chunksOK_one c2202) (chunksOK_one c2203))) (chunksOK_append (chunksOK_append (chunksOK_one c2204) (chunksOK_one c2205)) (chunksOK_append (chunksOK_one c2206) (chunksOK_one c2207)))))

end C137

namespace C138

theorem c2208 : check 60 115 18 2208 = true := by decide +kernel
theorem c2209 : check 60 115 18 2209 = true := by decide +kernel
theorem c2210 : check 60 115 18 2210 = true := by decide +kernel
theorem c2211 : check 60 115 18 2211 = true := by decide +kernel
theorem c2212 : check 60 115 18 2212 = true := by decide +kernel
theorem c2213 : check 60 115 18 2213 = true := by decide +kernel
theorem c2214 : check 60 115 18 2214 = true := by decide +kernel
theorem c2215 : check 60 115 18 2215 = true := by decide +kernel
theorem c2216 : check 60 115 18 2216 = true := by decide +kernel
theorem c2217 : check 60 115 18 2217 = true := by decide +kernel
theorem c2218 : check 60 115 18 2218 = true := by decide +kernel
theorem c2219 : check 60 115 18 2219 = true := by decide +kernel
theorem c2220 : check 60 115 18 2220 = true := by decide +kernel
theorem c2221 : check 60 115 18 2221 = true := by decide +kernel
theorem c2222 : check 60 115 18 2222 = true := by decide +kernel
theorem c2223 : check 60 115 18 2223 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2208 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2208) (chunksOK_one c2209)) (chunksOK_append (chunksOK_one c2210) (chunksOK_one c2211))) (chunksOK_append (chunksOK_append (chunksOK_one c2212) (chunksOK_one c2213)) (chunksOK_append (chunksOK_one c2214) (chunksOK_one c2215)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2216) (chunksOK_one c2217)) (chunksOK_append (chunksOK_one c2218) (chunksOK_one c2219))) (chunksOK_append (chunksOK_append (chunksOK_one c2220) (chunksOK_one c2221)) (chunksOK_append (chunksOK_one c2222) (chunksOK_one c2223)))))

end C138

namespace C139

theorem c2224 : check 60 115 18 2224 = true := by decide +kernel
theorem c2225 : check 60 115 18 2225 = true := by decide +kernel
theorem c2226 : check 60 115 18 2226 = true := by decide +kernel
theorem c2227 : check 60 115 18 2227 = true := by decide +kernel
theorem c2228 : check 60 115 18 2228 = true := by decide +kernel
theorem c2229 : check 60 115 18 2229 = true := by decide +kernel
theorem c2230 : check 60 115 18 2230 = true := by decide +kernel
theorem c2231 : check 60 115 18 2231 = true := by decide +kernel
theorem c2232 : check 60 115 18 2232 = true := by decide +kernel
theorem c2233 : check 60 115 18 2233 = true := by decide +kernel
theorem c2234 : check 60 115 18 2234 = true := by decide +kernel
theorem c2235 : check 60 115 18 2235 = true := by decide +kernel
theorem c2236 : check 60 115 18 2236 = true := by decide +kernel
theorem c2237 : check 60 115 18 2237 = true := by decide +kernel
theorem c2238 : check 60 115 18 2238 = true := by decide +kernel
theorem c2239 : check 60 115 18 2239 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2224 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2224) (chunksOK_one c2225)) (chunksOK_append (chunksOK_one c2226) (chunksOK_one c2227))) (chunksOK_append (chunksOK_append (chunksOK_one c2228) (chunksOK_one c2229)) (chunksOK_append (chunksOK_one c2230) (chunksOK_one c2231)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2232) (chunksOK_one c2233)) (chunksOK_append (chunksOK_one c2234) (chunksOK_one c2235))) (chunksOK_append (chunksOK_append (chunksOK_one c2236) (chunksOK_one c2237)) (chunksOK_append (chunksOK_one c2238) (chunksOK_one c2239)))))

end C139

namespace C140

theorem c2240 : check 60 115 18 2240 = true := by decide +kernel
theorem c2241 : check 60 115 18 2241 = true := by decide +kernel
theorem c2242 : check 60 115 18 2242 = true := by decide +kernel
theorem c2243 : check 60 115 18 2243 = true := by decide +kernel
theorem c2244 : check 60 115 18 2244 = true := by decide +kernel
theorem c2245 : check 60 115 18 2245 = true := by decide +kernel
theorem c2246 : check 60 115 18 2246 = true := by decide +kernel
theorem c2247 : check 60 115 18 2247 = true := by decide +kernel
theorem c2248 : check 60 115 18 2248 = true := by decide +kernel
theorem c2249 : check 60 115 18 2249 = true := by decide +kernel
theorem c2250 : check 60 115 18 2250 = true := by decide +kernel
theorem c2251 : check 60 115 18 2251 = true := by decide +kernel
theorem c2252 : check 60 115 18 2252 = true := by decide +kernel
theorem c2253 : check 60 115 18 2253 = true := by decide +kernel
theorem c2254 : check 60 115 18 2254 = true := by decide +kernel
theorem c2255 : check 60 115 18 2255 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2240 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2240) (chunksOK_one c2241)) (chunksOK_append (chunksOK_one c2242) (chunksOK_one c2243))) (chunksOK_append (chunksOK_append (chunksOK_one c2244) (chunksOK_one c2245)) (chunksOK_append (chunksOK_one c2246) (chunksOK_one c2247)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2248) (chunksOK_one c2249)) (chunksOK_append (chunksOK_one c2250) (chunksOK_one c2251))) (chunksOK_append (chunksOK_append (chunksOK_one c2252) (chunksOK_one c2253)) (chunksOK_append (chunksOK_one c2254) (chunksOK_one c2255)))))

end C140

namespace C141

theorem c2256 : check 60 115 18 2256 = true := by decide +kernel
theorem c2257 : check 60 115 18 2257 = true := by decide +kernel
theorem c2258 : check 60 115 18 2258 = true := by decide +kernel
theorem c2259 : check 60 115 18 2259 = true := by decide +kernel
theorem c2260 : check 60 115 18 2260 = true := by decide +kernel
theorem c2261 : check 60 115 18 2261 = true := by decide +kernel
theorem c2262 : check 60 115 18 2262 = true := by decide +kernel
theorem c2263 : check 60 115 18 2263 = true := by decide +kernel
theorem c2264 : check 60 115 18 2264 = true := by decide +kernel
theorem c2265 : check 60 115 18 2265 = true := by decide +kernel
theorem c2266 : check 60 115 18 2266 = true := by decide +kernel
theorem c2267 : check 60 115 18 2267 = true := by decide +kernel
theorem c2268 : check 60 115 18 2268 = true := by decide +kernel
theorem c2269 : check 60 115 18 2269 = true := by decide +kernel
theorem c2270 : check 60 115 18 2270 = true := by decide +kernel
theorem c2271 : check 60 115 18 2271 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2256 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2256) (chunksOK_one c2257)) (chunksOK_append (chunksOK_one c2258) (chunksOK_one c2259))) (chunksOK_append (chunksOK_append (chunksOK_one c2260) (chunksOK_one c2261)) (chunksOK_append (chunksOK_one c2262) (chunksOK_one c2263)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2264) (chunksOK_one c2265)) (chunksOK_append (chunksOK_one c2266) (chunksOK_one c2267))) (chunksOK_append (chunksOK_append (chunksOK_one c2268) (chunksOK_one c2269)) (chunksOK_append (chunksOK_one c2270) (chunksOK_one c2271)))))

end C141

namespace C142

theorem c2272 : check 60 115 18 2272 = true := by decide +kernel
theorem c2273 : check 60 115 18 2273 = true := by decide +kernel
theorem c2274 : check 60 115 18 2274 = true := by decide +kernel
theorem c2275 : check 60 115 18 2275 = true := by decide +kernel
theorem c2276 : check 60 115 18 2276 = true := by decide +kernel
theorem c2277 : check 60 115 18 2277 = true := by decide +kernel
theorem c2278 : check 60 115 18 2278 = true := by decide +kernel
theorem c2279 : check 60 115 18 2279 = true := by decide +kernel
theorem c2280 : check 60 115 18 2280 = true := by decide +kernel
theorem c2281 : check 60 115 18 2281 = true := by decide +kernel
theorem c2282 : check 60 115 18 2282 = true := by decide +kernel
theorem c2283 : check 60 115 18 2283 = true := by decide +kernel
theorem c2284 : check 60 115 18 2284 = true := by decide +kernel
theorem c2285 : check 60 115 18 2285 = true := by decide +kernel
theorem c2286 : check 60 115 18 2286 = true := by decide +kernel
theorem c2287 : check 60 115 18 2287 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2272 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2272) (chunksOK_one c2273)) (chunksOK_append (chunksOK_one c2274) (chunksOK_one c2275))) (chunksOK_append (chunksOK_append (chunksOK_one c2276) (chunksOK_one c2277)) (chunksOK_append (chunksOK_one c2278) (chunksOK_one c2279)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2280) (chunksOK_one c2281)) (chunksOK_append (chunksOK_one c2282) (chunksOK_one c2283))) (chunksOK_append (chunksOK_append (chunksOK_one c2284) (chunksOK_one c2285)) (chunksOK_append (chunksOK_one c2286) (chunksOK_one c2287)))))

end C142

namespace C143

theorem c2288 : check 60 115 18 2288 = true := by decide +kernel
theorem c2289 : check 60 115 18 2289 = true := by decide +kernel
theorem c2290 : check 60 115 18 2290 = true := by decide +kernel
theorem c2291 : check 60 115 18 2291 = true := by decide +kernel
theorem c2292 : check 60 115 18 2292 = true := by decide +kernel
theorem c2293 : check 60 115 18 2293 = true := by decide +kernel
theorem c2294 : check 60 115 18 2294 = true := by decide +kernel
theorem c2295 : check 60 115 18 2295 = true := by decide +kernel
theorem c2296 : check 60 115 18 2296 = true := by decide +kernel
theorem c2297 : check 60 115 18 2297 = true := by decide +kernel
theorem c2298 : check 60 115 18 2298 = true := by decide +kernel
theorem c2299 : check 60 115 18 2299 = true := by decide +kernel
theorem c2300 : check 60 115 18 2300 = true := by decide +kernel
theorem c2301 : check 60 115 18 2301 = true := by decide +kernel
theorem c2302 : check 60 115 18 2302 = true := by decide +kernel
theorem c2303 : check 60 115 18 2303 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2288 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2288) (chunksOK_one c2289)) (chunksOK_append (chunksOK_one c2290) (chunksOK_one c2291))) (chunksOK_append (chunksOK_append (chunksOK_one c2292) (chunksOK_one c2293)) (chunksOK_append (chunksOK_one c2294) (chunksOK_one c2295)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2296) (chunksOK_one c2297)) (chunksOK_append (chunksOK_one c2298) (chunksOK_one c2299))) (chunksOK_append (chunksOK_append (chunksOK_one c2300) (chunksOK_one c2301)) (chunksOK_append (chunksOK_one c2302) (chunksOK_one c2303)))))

end C143

namespace C144

theorem c2304 : check 60 115 18 2304 = true := by decide +kernel
theorem c2305 : check 60 115 18 2305 = true := by decide +kernel
theorem c2306 : check 60 115 18 2306 = true := by decide +kernel
theorem c2307 : check 60 115 18 2307 = true := by decide +kernel
theorem c2308 : check 60 115 18 2308 = true := by decide +kernel
theorem c2309 : check 60 115 18 2309 = true := by decide +kernel
theorem c2310 : check 60 115 18 2310 = true := by decide +kernel
theorem c2311 : check 60 115 18 2311 = true := by decide +kernel
theorem c2312 : check 60 115 18 2312 = true := by decide +kernel
theorem c2313 : check 60 115 18 2313 = true := by decide +kernel
theorem c2314 : check 60 115 18 2314 = true := by decide +kernel
theorem c2315 : check 60 115 18 2315 = true := by decide +kernel
theorem c2316 : check 60 115 18 2316 = true := by decide +kernel
theorem c2317 : check 60 115 18 2317 = true := by decide +kernel
theorem c2318 : check 60 115 18 2318 = true := by decide +kernel
theorem c2319 : check 60 115 18 2319 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2304 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2304) (chunksOK_one c2305)) (chunksOK_append (chunksOK_one c2306) (chunksOK_one c2307))) (chunksOK_append (chunksOK_append (chunksOK_one c2308) (chunksOK_one c2309)) (chunksOK_append (chunksOK_one c2310) (chunksOK_one c2311)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2312) (chunksOK_one c2313)) (chunksOK_append (chunksOK_one c2314) (chunksOK_one c2315))) (chunksOK_append (chunksOK_append (chunksOK_one c2316) (chunksOK_one c2317)) (chunksOK_append (chunksOK_one c2318) (chunksOK_one c2319)))))

end C144

namespace C145

theorem c2320 : check 60 115 18 2320 = true := by decide +kernel
theorem c2321 : check 60 115 18 2321 = true := by decide +kernel
theorem c2322 : check 60 115 18 2322 = true := by decide +kernel
theorem c2323 : check 60 115 18 2323 = true := by decide +kernel
theorem c2324 : check 60 115 18 2324 = true := by decide +kernel
theorem c2325 : check 60 115 18 2325 = true := by decide +kernel
theorem c2326 : check 60 115 18 2326 = true := by decide +kernel
theorem c2327 : check 60 115 18 2327 = true := by decide +kernel
theorem c2328 : check 60 115 18 2328 = true := by decide +kernel
theorem c2329 : check 60 115 18 2329 = true := by decide +kernel
theorem c2330 : check 60 115 18 2330 = true := by decide +kernel
theorem c2331 : check 60 115 18 2331 = true := by decide +kernel
theorem c2332 : check 60 115 18 2332 = true := by decide +kernel
theorem c2333 : check 60 115 18 2333 = true := by decide +kernel
theorem c2334 : check 60 115 18 2334 = true := by decide +kernel
theorem c2335 : check 60 115 18 2335 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2320 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2320) (chunksOK_one c2321)) (chunksOK_append (chunksOK_one c2322) (chunksOK_one c2323))) (chunksOK_append (chunksOK_append (chunksOK_one c2324) (chunksOK_one c2325)) (chunksOK_append (chunksOK_one c2326) (chunksOK_one c2327)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2328) (chunksOK_one c2329)) (chunksOK_append (chunksOK_one c2330) (chunksOK_one c2331))) (chunksOK_append (chunksOK_append (chunksOK_one c2332) (chunksOK_one c2333)) (chunksOK_append (chunksOK_one c2334) (chunksOK_one c2335)))))

end C145

namespace C146

theorem c2336 : check 60 115 18 2336 = true := by decide +kernel
theorem c2337 : check 60 115 18 2337 = true := by decide +kernel
theorem c2338 : check 60 115 18 2338 = true := by decide +kernel
theorem c2339 : check 60 115 18 2339 = true := by decide +kernel
theorem c2340 : check 60 115 18 2340 = true := by decide +kernel
theorem c2341 : check 60 115 18 2341 = true := by decide +kernel
theorem c2342 : check 60 115 18 2342 = true := by decide +kernel
theorem c2343 : check 60 115 18 2343 = true := by decide +kernel
theorem c2344 : check 60 115 18 2344 = true := by decide +kernel
theorem c2345 : check 60 115 18 2345 = true := by decide +kernel
theorem c2346 : check 60 115 18 2346 = true := by decide +kernel
theorem c2347 : check 60 115 18 2347 = true := by decide +kernel
theorem c2348 : check 60 115 18 2348 = true := by decide +kernel
theorem c2349 : check 60 115 18 2349 = true := by decide +kernel
theorem c2350 : check 60 115 18 2350 = true := by decide +kernel
theorem c2351 : check 60 115 18 2351 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2336 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2336) (chunksOK_one c2337)) (chunksOK_append (chunksOK_one c2338) (chunksOK_one c2339))) (chunksOK_append (chunksOK_append (chunksOK_one c2340) (chunksOK_one c2341)) (chunksOK_append (chunksOK_one c2342) (chunksOK_one c2343)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2344) (chunksOK_one c2345)) (chunksOK_append (chunksOK_one c2346) (chunksOK_one c2347))) (chunksOK_append (chunksOK_append (chunksOK_one c2348) (chunksOK_one c2349)) (chunksOK_append (chunksOK_one c2350) (chunksOK_one c2351)))))

end C146

namespace C147

theorem c2352 : check 60 115 18 2352 = true := by decide +kernel
theorem c2353 : check 60 115 18 2353 = true := by decide +kernel
theorem c2354 : check 60 115 18 2354 = true := by decide +kernel
theorem c2355 : check 60 115 18 2355 = true := by decide +kernel
theorem c2356 : check 60 115 18 2356 = true := by decide +kernel
theorem c2357 : check 60 115 18 2357 = true := by decide +kernel
theorem c2358 : check 60 115 18 2358 = true := by decide +kernel
theorem c2359 : check 60 115 18 2359 = true := by decide +kernel
theorem c2360 : check 60 115 18 2360 = true := by decide +kernel
theorem c2361 : check 60 115 18 2361 = true := by decide +kernel
theorem c2362 : check 60 115 18 2362 = true := by decide +kernel
theorem c2363 : check 60 115 18 2363 = true := by decide +kernel
theorem c2364 : check 60 115 18 2364 = true := by decide +kernel
theorem c2365 : check 60 115 18 2365 = true := by decide +kernel
theorem c2366 : check 60 115 18 2366 = true := by decide +kernel
theorem c2367 : check 60 115 18 2367 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2352 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2352) (chunksOK_one c2353)) (chunksOK_append (chunksOK_one c2354) (chunksOK_one c2355))) (chunksOK_append (chunksOK_append (chunksOK_one c2356) (chunksOK_one c2357)) (chunksOK_append (chunksOK_one c2358) (chunksOK_one c2359)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2360) (chunksOK_one c2361)) (chunksOK_append (chunksOK_one c2362) (chunksOK_one c2363))) (chunksOK_append (chunksOK_append (chunksOK_one c2364) (chunksOK_one c2365)) (chunksOK_append (chunksOK_one c2366) (chunksOK_one c2367)))))

end C147

namespace C148

theorem c2368 : check 60 115 18 2368 = true := by decide +kernel
theorem c2369 : check 60 115 18 2369 = true := by decide +kernel
theorem c2370 : check 60 115 18 2370 = true := by decide +kernel
theorem c2371 : check 60 115 18 2371 = true := by decide +kernel
theorem c2372 : check 60 115 18 2372 = true := by decide +kernel
theorem c2373 : check 60 115 18 2373 = true := by decide +kernel
theorem c2374 : check 60 115 18 2374 = true := by decide +kernel
theorem c2375 : check 60 115 18 2375 = true := by decide +kernel
theorem c2376 : check 60 115 18 2376 = true := by decide +kernel
theorem c2377 : check 60 115 18 2377 = true := by decide +kernel
theorem c2378 : check 60 115 18 2378 = true := by decide +kernel
theorem c2379 : check 60 115 18 2379 = true := by decide +kernel
theorem c2380 : check 60 115 18 2380 = true := by decide +kernel
theorem c2381 : check 60 115 18 2381 = true := by decide +kernel
theorem c2382 : check 60 115 18 2382 = true := by decide +kernel
theorem c2383 : check 60 115 18 2383 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2368 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2368) (chunksOK_one c2369)) (chunksOK_append (chunksOK_one c2370) (chunksOK_one c2371))) (chunksOK_append (chunksOK_append (chunksOK_one c2372) (chunksOK_one c2373)) (chunksOK_append (chunksOK_one c2374) (chunksOK_one c2375)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2376) (chunksOK_one c2377)) (chunksOK_append (chunksOK_one c2378) (chunksOK_one c2379))) (chunksOK_append (chunksOK_append (chunksOK_one c2380) (chunksOK_one c2381)) (chunksOK_append (chunksOK_one c2382) (chunksOK_one c2383)))))

end C148

namespace C149

theorem c2384 : check 60 115 18 2384 = true := by decide +kernel
theorem c2385 : check 60 115 18 2385 = true := by decide +kernel
theorem c2386 : check 60 115 18 2386 = true := by decide +kernel
theorem c2387 : check 60 115 18 2387 = true := by decide +kernel
theorem c2388 : check 60 115 18 2388 = true := by decide +kernel
theorem c2389 : check 60 115 18 2389 = true := by decide +kernel
theorem c2390 : check 60 115 18 2390 = true := by decide +kernel
theorem c2391 : check 60 115 18 2391 = true := by decide +kernel
theorem c2392 : check 60 115 18 2392 = true := by decide +kernel
theorem c2393 : check 60 115 18 2393 = true := by decide +kernel
theorem c2394 : check 60 115 18 2394 = true := by decide +kernel
theorem c2395 : check 60 115 18 2395 = true := by decide +kernel
theorem c2396 : check 60 115 18 2396 = true := by decide +kernel
theorem c2397 : check 60 115 18 2397 = true := by decide +kernel
theorem c2398 : check 60 115 18 2398 = true := by decide +kernel
theorem c2399 : check 60 115 18 2399 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2384 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2384) (chunksOK_one c2385)) (chunksOK_append (chunksOK_one c2386) (chunksOK_one c2387))) (chunksOK_append (chunksOK_append (chunksOK_one c2388) (chunksOK_one c2389)) (chunksOK_append (chunksOK_one c2390) (chunksOK_one c2391)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2392) (chunksOK_one c2393)) (chunksOK_append (chunksOK_one c2394) (chunksOK_one c2395))) (chunksOK_append (chunksOK_append (chunksOK_one c2396) (chunksOK_one c2397)) (chunksOK_append (chunksOK_one c2398) (chunksOK_one c2399)))))

end C149

namespace C150

theorem c2400 : check 60 115 18 2400 = true := by decide +kernel
theorem c2401 : check 60 115 18 2401 = true := by decide +kernel
theorem c2402 : check 60 115 18 2402 = true := by decide +kernel
theorem c2403 : check 60 115 18 2403 = true := by decide +kernel
theorem c2404 : check 60 115 18 2404 = true := by decide +kernel
theorem c2405 : check 60 115 18 2405 = true := by decide +kernel
theorem c2406 : check 60 115 18 2406 = true := by decide +kernel
theorem c2407 : check 60 115 18 2407 = true := by decide +kernel
theorem c2408 : check 60 115 18 2408 = true := by decide +kernel
theorem c2409 : check 60 115 18 2409 = true := by decide +kernel
theorem c2410 : check 60 115 18 2410 = true := by decide +kernel
theorem c2411 : check 60 115 18 2411 = true := by decide +kernel
theorem c2412 : check 60 115 18 2412 = true := by decide +kernel
theorem c2413 : check 60 115 18 2413 = true := by decide +kernel
theorem c2414 : check 60 115 18 2414 = true := by decide +kernel
theorem c2415 : check 60 115 18 2415 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2400 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2400) (chunksOK_one c2401)) (chunksOK_append (chunksOK_one c2402) (chunksOK_one c2403))) (chunksOK_append (chunksOK_append (chunksOK_one c2404) (chunksOK_one c2405)) (chunksOK_append (chunksOK_one c2406) (chunksOK_one c2407)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2408) (chunksOK_one c2409)) (chunksOK_append (chunksOK_one c2410) (chunksOK_one c2411))) (chunksOK_append (chunksOK_append (chunksOK_one c2412) (chunksOK_one c2413)) (chunksOK_append (chunksOK_one c2414) (chunksOK_one c2415)))))

end C150

namespace C151

theorem c2416 : check 60 115 18 2416 = true := by decide +kernel
theorem c2417 : check 60 115 18 2417 = true := by decide +kernel
theorem c2418 : check 60 115 18 2418 = true := by decide +kernel
theorem c2419 : check 60 115 18 2419 = true := by decide +kernel
theorem c2420 : check 60 115 18 2420 = true := by decide +kernel
theorem c2421 : check 60 115 18 2421 = true := by decide +kernel
theorem c2422 : check 60 115 18 2422 = true := by decide +kernel
theorem c2423 : check 60 115 18 2423 = true := by decide +kernel
theorem c2424 : check 60 115 18 2424 = true := by decide +kernel
theorem c2425 : check 60 115 18 2425 = true := by decide +kernel
theorem c2426 : check 60 115 18 2426 = true := by decide +kernel
theorem c2427 : check 60 115 18 2427 = true := by decide +kernel
theorem c2428 : check 60 115 18 2428 = true := by decide +kernel
theorem c2429 : check 60 115 18 2429 = true := by decide +kernel
theorem c2430 : check 60 115 18 2430 = true := by decide +kernel
theorem c2431 : check 60 115 18 2431 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2416 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2416) (chunksOK_one c2417)) (chunksOK_append (chunksOK_one c2418) (chunksOK_one c2419))) (chunksOK_append (chunksOK_append (chunksOK_one c2420) (chunksOK_one c2421)) (chunksOK_append (chunksOK_one c2422) (chunksOK_one c2423)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2424) (chunksOK_one c2425)) (chunksOK_append (chunksOK_one c2426) (chunksOK_one c2427))) (chunksOK_append (chunksOK_append (chunksOK_one c2428) (chunksOK_one c2429)) (chunksOK_append (chunksOK_one c2430) (chunksOK_one c2431)))))

end C151

namespace C152

theorem c2432 : check 60 115 18 2432 = true := by decide +kernel
theorem c2433 : check 60 115 18 2433 = true := by decide +kernel
theorem c2434 : check 60 115 18 2434 = true := by decide +kernel
theorem c2435 : check 60 115 18 2435 = true := by decide +kernel
theorem c2436 : check 60 115 18 2436 = true := by decide +kernel
theorem c2437 : check 60 115 18 2437 = true := by decide +kernel
theorem c2438 : check 60 115 18 2438 = true := by decide +kernel
theorem c2439 : check 60 115 18 2439 = true := by decide +kernel
theorem c2440 : check 60 115 18 2440 = true := by decide +kernel
theorem c2441 : check 60 115 18 2441 = true := by decide +kernel
theorem c2442 : check 60 115 18 2442 = true := by decide +kernel
theorem c2443 : check 60 115 18 2443 = true := by decide +kernel
theorem c2444 : check 60 115 18 2444 = true := by decide +kernel
theorem c2445 : check 60 115 18 2445 = true := by decide +kernel
theorem c2446 : check 60 115 18 2446 = true := by decide +kernel
theorem c2447 : check 60 115 18 2447 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2432 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2432) (chunksOK_one c2433)) (chunksOK_append (chunksOK_one c2434) (chunksOK_one c2435))) (chunksOK_append (chunksOK_append (chunksOK_one c2436) (chunksOK_one c2437)) (chunksOK_append (chunksOK_one c2438) (chunksOK_one c2439)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2440) (chunksOK_one c2441)) (chunksOK_append (chunksOK_one c2442) (chunksOK_one c2443))) (chunksOK_append (chunksOK_append (chunksOK_one c2444) (chunksOK_one c2445)) (chunksOK_append (chunksOK_one c2446) (chunksOK_one c2447)))))

end C152

namespace C153

theorem c2448 : check 60 115 18 2448 = true := by decide +kernel
theorem c2449 : check 60 115 18 2449 = true := by decide +kernel
theorem c2450 : check 60 115 18 2450 = true := by decide +kernel
theorem c2451 : check 60 115 18 2451 = true := by decide +kernel
theorem c2452 : check 60 115 18 2452 = true := by decide +kernel
theorem c2453 : check 60 115 18 2453 = true := by decide +kernel
theorem c2454 : check 60 115 18 2454 = true := by decide +kernel
theorem c2455 : check 60 115 18 2455 = true := by decide +kernel
theorem c2456 : check 60 115 18 2456 = true := by decide +kernel
theorem c2457 : check 60 115 18 2457 = true := by decide +kernel
theorem c2458 : check 60 115 18 2458 = true := by decide +kernel
theorem c2459 : check 60 115 18 2459 = true := by decide +kernel
theorem c2460 : check 60 115 18 2460 = true := by decide +kernel
theorem c2461 : check 60 115 18 2461 = true := by decide +kernel
theorem c2462 : check 60 115 18 2462 = true := by decide +kernel
theorem c2463 : check 60 115 18 2463 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2448 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2448) (chunksOK_one c2449)) (chunksOK_append (chunksOK_one c2450) (chunksOK_one c2451))) (chunksOK_append (chunksOK_append (chunksOK_one c2452) (chunksOK_one c2453)) (chunksOK_append (chunksOK_one c2454) (chunksOK_one c2455)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2456) (chunksOK_one c2457)) (chunksOK_append (chunksOK_one c2458) (chunksOK_one c2459))) (chunksOK_append (chunksOK_append (chunksOK_one c2460) (chunksOK_one c2461)) (chunksOK_append (chunksOK_one c2462) (chunksOK_one c2463)))))

end C153

namespace C154

theorem c2464 : check 60 115 18 2464 = true := by decide +kernel
theorem c2465 : check 60 115 18 2465 = true := by decide +kernel
theorem c2466 : check 60 115 18 2466 = true := by decide +kernel
theorem c2467 : check 60 115 18 2467 = true := by decide +kernel
theorem c2468 : check 60 115 18 2468 = true := by decide +kernel
theorem c2469 : check 60 115 18 2469 = true := by decide +kernel
theorem c2470 : check 60 115 18 2470 = true := by decide +kernel
theorem c2471 : check 60 115 18 2471 = true := by decide +kernel
theorem c2472 : check 60 115 18 2472 = true := by decide +kernel
theorem c2473 : check 60 115 18 2473 = true := by decide +kernel
theorem c2474 : check 60 115 18 2474 = true := by decide +kernel
theorem c2475 : check 60 115 18 2475 = true := by decide +kernel
theorem c2476 : check 60 115 18 2476 = true := by decide +kernel
theorem c2477 : check 60 115 18 2477 = true := by decide +kernel
theorem c2478 : check 60 115 18 2478 = true := by decide +kernel
theorem c2479 : check 60 115 18 2479 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2464 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2464) (chunksOK_one c2465)) (chunksOK_append (chunksOK_one c2466) (chunksOK_one c2467))) (chunksOK_append (chunksOK_append (chunksOK_one c2468) (chunksOK_one c2469)) (chunksOK_append (chunksOK_one c2470) (chunksOK_one c2471)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2472) (chunksOK_one c2473)) (chunksOK_append (chunksOK_one c2474) (chunksOK_one c2475))) (chunksOK_append (chunksOK_append (chunksOK_one c2476) (chunksOK_one c2477)) (chunksOK_append (chunksOK_one c2478) (chunksOK_one c2479)))))

end C154

namespace C155

theorem c2480 : check 60 115 18 2480 = true := by decide +kernel
theorem c2481 : check 60 115 18 2481 = true := by decide +kernel
theorem c2482 : check 60 115 18 2482 = true := by decide +kernel
theorem c2483 : check 60 115 18 2483 = true := by decide +kernel
theorem c2484 : check 60 115 18 2484 = true := by decide +kernel
theorem c2485 : check 60 115 18 2485 = true := by decide +kernel
theorem c2486 : check 60 115 18 2486 = true := by decide +kernel
theorem c2487 : check 60 115 18 2487 = true := by decide +kernel
theorem c2488 : check 60 115 18 2488 = true := by decide +kernel
theorem c2489 : check 60 115 18 2489 = true := by decide +kernel
theorem c2490 : check 60 115 18 2490 = true := by decide +kernel
theorem c2491 : check 60 115 18 2491 = true := by decide +kernel
theorem c2492 : check 60 115 18 2492 = true := by decide +kernel
theorem c2493 : check 60 115 18 2493 = true := by decide +kernel
theorem c2494 : check 60 115 18 2494 = true := by decide +kernel
theorem c2495 : check 60 115 18 2495 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2480 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2480) (chunksOK_one c2481)) (chunksOK_append (chunksOK_one c2482) (chunksOK_one c2483))) (chunksOK_append (chunksOK_append (chunksOK_one c2484) (chunksOK_one c2485)) (chunksOK_append (chunksOK_one c2486) (chunksOK_one c2487)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2488) (chunksOK_one c2489)) (chunksOK_append (chunksOK_one c2490) (chunksOK_one c2491))) (chunksOK_append (chunksOK_append (chunksOK_one c2492) (chunksOK_one c2493)) (chunksOK_append (chunksOK_one c2494) (chunksOK_one c2495)))))

end C155

namespace C156

theorem c2496 : check 60 115 18 2496 = true := by decide +kernel
theorem c2497 : check 60 115 18 2497 = true := by decide +kernel
theorem c2498 : check 60 115 18 2498 = true := by decide +kernel
theorem c2499 : check 60 115 18 2499 = true := by decide +kernel
theorem c2500 : check 60 115 18 2500 = true := by decide +kernel
theorem c2501 : check 60 115 18 2501 = true := by decide +kernel
theorem c2502 : check 60 115 18 2502 = true := by decide +kernel
theorem c2503 : check 60 115 18 2503 = true := by decide +kernel
theorem c2504 : check 60 115 18 2504 = true := by decide +kernel
theorem c2505 : check 60 115 18 2505 = true := by decide +kernel
theorem c2506 : check 60 115 18 2506 = true := by decide +kernel
theorem c2507 : check 60 115 18 2507 = true := by decide +kernel
theorem c2508 : check 60 115 18 2508 = true := by decide +kernel
theorem c2509 : check 60 115 18 2509 = true := by decide +kernel
theorem c2510 : check 60 115 18 2510 = true := by decide +kernel
theorem c2511 : check 60 115 18 2511 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2496 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2496) (chunksOK_one c2497)) (chunksOK_append (chunksOK_one c2498) (chunksOK_one c2499))) (chunksOK_append (chunksOK_append (chunksOK_one c2500) (chunksOK_one c2501)) (chunksOK_append (chunksOK_one c2502) (chunksOK_one c2503)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2504) (chunksOK_one c2505)) (chunksOK_append (chunksOK_one c2506) (chunksOK_one c2507))) (chunksOK_append (chunksOK_append (chunksOK_one c2508) (chunksOK_one c2509)) (chunksOK_append (chunksOK_one c2510) (chunksOK_one c2511)))))

end C156

namespace C157

theorem c2512 : check 60 115 18 2512 = true := by decide +kernel
theorem c2513 : check 60 115 18 2513 = true := by decide +kernel
theorem c2514 : check 60 115 18 2514 = true := by decide +kernel
theorem c2515 : check 60 115 18 2515 = true := by decide +kernel
theorem c2516 : check 60 115 18 2516 = true := by decide +kernel
theorem c2517 : check 60 115 18 2517 = true := by decide +kernel
theorem c2518 : check 60 115 18 2518 = true := by decide +kernel
theorem c2519 : check 60 115 18 2519 = true := by decide +kernel
theorem c2520 : check 60 115 18 2520 = true := by decide +kernel
theorem c2521 : check 60 115 18 2521 = true := by decide +kernel
theorem c2522 : check 60 115 18 2522 = true := by decide +kernel
theorem c2523 : check 60 115 18 2523 = true := by decide +kernel
theorem c2524 : check 60 115 18 2524 = true := by decide +kernel
theorem c2525 : check 60 115 18 2525 = true := by decide +kernel
theorem c2526 : check 60 115 18 2526 = true := by decide +kernel
theorem c2527 : check 60 115 18 2527 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2512 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2512) (chunksOK_one c2513)) (chunksOK_append (chunksOK_one c2514) (chunksOK_one c2515))) (chunksOK_append (chunksOK_append (chunksOK_one c2516) (chunksOK_one c2517)) (chunksOK_append (chunksOK_one c2518) (chunksOK_one c2519)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2520) (chunksOK_one c2521)) (chunksOK_append (chunksOK_one c2522) (chunksOK_one c2523))) (chunksOK_append (chunksOK_append (chunksOK_one c2524) (chunksOK_one c2525)) (chunksOK_append (chunksOK_one c2526) (chunksOK_one c2527)))))

end C157

namespace C158

theorem c2528 : check 60 115 18 2528 = true := by decide +kernel
theorem c2529 : check 60 115 18 2529 = true := by decide +kernel
theorem c2530 : check 60 115 18 2530 = true := by decide +kernel
theorem c2531 : check 60 115 18 2531 = true := by decide +kernel
theorem c2532 : check 60 115 18 2532 = true := by decide +kernel
theorem c2533 : check 60 115 18 2533 = true := by decide +kernel
theorem c2534 : check 60 115 18 2534 = true := by decide +kernel
theorem c2535 : check 60 115 18 2535 = true := by decide +kernel
theorem c2536 : check 60 115 18 2536 = true := by decide +kernel
theorem c2537 : check 60 115 18 2537 = true := by decide +kernel
theorem c2538 : check 60 115 18 2538 = true := by decide +kernel
theorem c2539 : check 60 115 18 2539 = true := by decide +kernel
theorem c2540 : check 60 115 18 2540 = true := by decide +kernel
theorem c2541 : check 60 115 18 2541 = true := by decide +kernel
theorem c2542 : check 60 115 18 2542 = true := by decide +kernel
theorem c2543 : check 60 115 18 2543 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2528 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2528) (chunksOK_one c2529)) (chunksOK_append (chunksOK_one c2530) (chunksOK_one c2531))) (chunksOK_append (chunksOK_append (chunksOK_one c2532) (chunksOK_one c2533)) (chunksOK_append (chunksOK_one c2534) (chunksOK_one c2535)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2536) (chunksOK_one c2537)) (chunksOK_append (chunksOK_one c2538) (chunksOK_one c2539))) (chunksOK_append (chunksOK_append (chunksOK_one c2540) (chunksOK_one c2541)) (chunksOK_append (chunksOK_one c2542) (chunksOK_one c2543)))))

end C158

namespace C159

theorem c2544 : check 60 115 18 2544 = true := by decide +kernel
theorem c2545 : check 60 115 18 2545 = true := by decide +kernel
theorem c2546 : check 60 115 18 2546 = true := by decide +kernel
theorem c2547 : check 60 115 18 2547 = true := by decide +kernel
theorem c2548 : check 60 115 18 2548 = true := by decide +kernel
theorem c2549 : check 60 115 18 2549 = true := by decide +kernel
theorem c2550 : check 60 115 18 2550 = true := by decide +kernel
theorem c2551 : check 60 115 18 2551 = true := by decide +kernel
theorem c2552 : check 60 115 18 2552 = true := by decide +kernel
theorem c2553 : check 60 115 18 2553 = true := by decide +kernel
theorem c2554 : check 60 115 18 2554 = true := by decide +kernel
theorem c2555 : check 60 115 18 2555 = true := by decide +kernel
theorem c2556 : check 60 115 18 2556 = true := by decide +kernel
theorem c2557 : check 60 115 18 2557 = true := by decide +kernel
theorem c2558 : check 60 115 18 2558 = true := by decide +kernel
theorem c2559 : check 60 115 18 2559 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2544 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2544) (chunksOK_one c2545)) (chunksOK_append (chunksOK_one c2546) (chunksOK_one c2547))) (chunksOK_append (chunksOK_append (chunksOK_one c2548) (chunksOK_one c2549)) (chunksOK_append (chunksOK_one c2550) (chunksOK_one c2551)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2552) (chunksOK_one c2553)) (chunksOK_append (chunksOK_one c2554) (chunksOK_one c2555))) (chunksOK_append (chunksOK_append (chunksOK_one c2556) (chunksOK_one c2557)) (chunksOK_append (chunksOK_one c2558) (chunksOK_one c2559)))))

end C159

namespace C160

theorem c2560 : check 60 115 18 2560 = true := by decide +kernel
theorem c2561 : check 60 115 18 2561 = true := by decide +kernel
theorem c2562 : check 60 115 18 2562 = true := by decide +kernel
theorem c2563 : check 60 115 18 2563 = true := by decide +kernel
theorem c2564 : check 60 115 18 2564 = true := by decide +kernel
theorem c2565 : check 60 115 18 2565 = true := by decide +kernel
theorem c2566 : check 60 115 18 2566 = true := by decide +kernel
theorem c2567 : check 60 115 18 2567 = true := by decide +kernel
theorem c2568 : check 60 115 18 2568 = true := by decide +kernel
theorem c2569 : check 60 115 18 2569 = true := by decide +kernel
theorem c2570 : check 60 115 18 2570 = true := by decide +kernel
theorem c2571 : check 60 115 18 2571 = true := by decide +kernel
theorem c2572 : check 60 115 18 2572 = true := by decide +kernel
theorem c2573 : check 60 115 18 2573 = true := by decide +kernel
theorem c2574 : check 60 115 18 2574 = true := by decide +kernel
theorem c2575 : check 60 115 18 2575 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2560 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2560) (chunksOK_one c2561)) (chunksOK_append (chunksOK_one c2562) (chunksOK_one c2563))) (chunksOK_append (chunksOK_append (chunksOK_one c2564) (chunksOK_one c2565)) (chunksOK_append (chunksOK_one c2566) (chunksOK_one c2567)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2568) (chunksOK_one c2569)) (chunksOK_append (chunksOK_one c2570) (chunksOK_one c2571))) (chunksOK_append (chunksOK_append (chunksOK_one c2572) (chunksOK_one c2573)) (chunksOK_append (chunksOK_one c2574) (chunksOK_one c2575)))))

end C160

namespace C161

theorem c2576 : check 60 115 18 2576 = true := by decide +kernel
theorem c2577 : check 60 115 18 2577 = true := by decide +kernel
theorem c2578 : check 60 115 18 2578 = true := by decide +kernel
theorem c2579 : check 60 115 18 2579 = true := by decide +kernel
theorem c2580 : check 60 115 18 2580 = true := by decide +kernel
theorem c2581 : check 60 115 18 2581 = true := by decide +kernel
theorem c2582 : check 60 115 18 2582 = true := by decide +kernel
theorem c2583 : check 60 115 18 2583 = true := by decide +kernel
theorem c2584 : check 60 115 18 2584 = true := by decide +kernel
theorem c2585 : check 60 115 18 2585 = true := by decide +kernel
theorem c2586 : check 60 115 18 2586 = true := by decide +kernel
theorem c2587 : check 60 115 18 2587 = true := by decide +kernel
theorem c2588 : check 60 115 18 2588 = true := by decide +kernel
theorem c2589 : check 60 115 18 2589 = true := by decide +kernel
theorem c2590 : check 60 115 18 2590 = true := by decide +kernel
theorem c2591 : check 60 115 18 2591 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2576 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2576) (chunksOK_one c2577)) (chunksOK_append (chunksOK_one c2578) (chunksOK_one c2579))) (chunksOK_append (chunksOK_append (chunksOK_one c2580) (chunksOK_one c2581)) (chunksOK_append (chunksOK_one c2582) (chunksOK_one c2583)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2584) (chunksOK_one c2585)) (chunksOK_append (chunksOK_one c2586) (chunksOK_one c2587))) (chunksOK_append (chunksOK_append (chunksOK_one c2588) (chunksOK_one c2589)) (chunksOK_append (chunksOK_one c2590) (chunksOK_one c2591)))))

end C161

namespace C162

theorem c2592 : check 60 115 18 2592 = true := by decide +kernel
theorem c2593 : check 60 115 18 2593 = true := by decide +kernel
theorem c2594 : check 60 115 18 2594 = true := by decide +kernel
theorem c2595 : check 60 115 18 2595 = true := by decide +kernel
theorem c2596 : check 60 115 18 2596 = true := by decide +kernel
theorem c2597 : check 60 115 18 2597 = true := by decide +kernel
theorem c2598 : check 60 115 18 2598 = true := by decide +kernel
theorem c2599 : check 60 115 18 2599 = true := by decide +kernel
theorem c2600 : check 60 115 18 2600 = true := by decide +kernel
theorem c2601 : check 60 115 18 2601 = true := by decide +kernel
theorem c2602 : check 60 115 18 2602 = true := by decide +kernel
theorem c2603 : check 60 115 18 2603 = true := by decide +kernel
theorem c2604 : check 60 115 18 2604 = true := by decide +kernel
theorem c2605 : check 60 115 18 2605 = true := by decide +kernel
theorem c2606 : check 60 115 18 2606 = true := by decide +kernel
theorem c2607 : check 60 115 18 2607 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2592 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2592) (chunksOK_one c2593)) (chunksOK_append (chunksOK_one c2594) (chunksOK_one c2595))) (chunksOK_append (chunksOK_append (chunksOK_one c2596) (chunksOK_one c2597)) (chunksOK_append (chunksOK_one c2598) (chunksOK_one c2599)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2600) (chunksOK_one c2601)) (chunksOK_append (chunksOK_one c2602) (chunksOK_one c2603))) (chunksOK_append (chunksOK_append (chunksOK_one c2604) (chunksOK_one c2605)) (chunksOK_append (chunksOK_one c2606) (chunksOK_one c2607)))))

end C162

namespace C163

theorem c2608 : check 60 115 18 2608 = true := by decide +kernel
theorem c2609 : check 60 115 18 2609 = true := by decide +kernel
theorem c2610 : check 60 115 18 2610 = true := by decide +kernel
theorem c2611 : check 60 115 18 2611 = true := by decide +kernel
theorem c2612 : check 60 115 18 2612 = true := by decide +kernel
theorem c2613 : check 60 115 18 2613 = true := by decide +kernel
theorem c2614 : check 60 115 18 2614 = true := by decide +kernel
theorem c2615 : check 60 115 18 2615 = true := by decide +kernel
theorem c2616 : check 60 115 18 2616 = true := by decide +kernel
theorem c2617 : check 60 115 18 2617 = true := by decide +kernel
theorem c2618 : check 60 115 18 2618 = true := by decide +kernel
theorem c2619 : check 60 115 18 2619 = true := by decide +kernel
theorem c2620 : check 60 115 18 2620 = true := by decide +kernel
theorem c2621 : check 60 115 18 2621 = true := by decide +kernel
theorem c2622 : check 60 115 18 2622 = true := by decide +kernel
theorem c2623 : check 60 115 18 2623 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2608 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2608) (chunksOK_one c2609)) (chunksOK_append (chunksOK_one c2610) (chunksOK_one c2611))) (chunksOK_append (chunksOK_append (chunksOK_one c2612) (chunksOK_one c2613)) (chunksOK_append (chunksOK_one c2614) (chunksOK_one c2615)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2616) (chunksOK_one c2617)) (chunksOK_append (chunksOK_one c2618) (chunksOK_one c2619))) (chunksOK_append (chunksOK_append (chunksOK_one c2620) (chunksOK_one c2621)) (chunksOK_append (chunksOK_one c2622) (chunksOK_one c2623)))))

end C163

namespace C164

theorem c2624 : check 60 115 18 2624 = true := by decide +kernel
theorem c2625 : check 60 115 18 2625 = true := by decide +kernel
theorem c2626 : check 60 115 18 2626 = true := by decide +kernel
theorem c2627 : check 60 115 18 2627 = true := by decide +kernel
theorem c2628 : check 60 115 18 2628 = true := by decide +kernel
theorem c2629 : check 60 115 18 2629 = true := by decide +kernel
theorem c2630 : check 60 115 18 2630 = true := by decide +kernel
theorem c2631 : check 60 115 18 2631 = true := by decide +kernel
theorem c2632 : check 60 115 18 2632 = true := by decide +kernel
theorem c2633 : check 60 115 18 2633 = true := by decide +kernel
theorem c2634 : check 60 115 18 2634 = true := by decide +kernel
theorem c2635 : check 60 115 18 2635 = true := by decide +kernel
theorem c2636 : check 60 115 18 2636 = true := by decide +kernel
theorem c2637 : check 60 115 18 2637 = true := by decide +kernel
theorem c2638 : check 60 115 18 2638 = true := by decide +kernel
theorem c2639 : check 60 115 18 2639 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2624 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2624) (chunksOK_one c2625)) (chunksOK_append (chunksOK_one c2626) (chunksOK_one c2627))) (chunksOK_append (chunksOK_append (chunksOK_one c2628) (chunksOK_one c2629)) (chunksOK_append (chunksOK_one c2630) (chunksOK_one c2631)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2632) (chunksOK_one c2633)) (chunksOK_append (chunksOK_one c2634) (chunksOK_one c2635))) (chunksOK_append (chunksOK_append (chunksOK_one c2636) (chunksOK_one c2637)) (chunksOK_append (chunksOK_one c2638) (chunksOK_one c2639)))))

end C164

namespace C165

theorem c2640 : check 60 115 18 2640 = true := by decide +kernel
theorem c2641 : check 60 115 18 2641 = true := by decide +kernel
theorem c2642 : check 60 115 18 2642 = true := by decide +kernel
theorem c2643 : check 60 115 18 2643 = true := by decide +kernel
theorem c2644 : check 60 115 18 2644 = true := by decide +kernel
theorem c2645 : check 60 115 18 2645 = true := by decide +kernel
theorem c2646 : check 60 115 18 2646 = true := by decide +kernel
theorem c2647 : check 60 115 18 2647 = true := by decide +kernel
theorem c2648 : check 60 115 18 2648 = true := by decide +kernel
theorem c2649 : check 60 115 18 2649 = true := by decide +kernel
theorem c2650 : check 60 115 18 2650 = true := by decide +kernel
theorem c2651 : check 60 115 18 2651 = true := by decide +kernel
theorem c2652 : check 60 115 18 2652 = true := by decide +kernel
theorem c2653 : check 60 115 18 2653 = true := by decide +kernel
theorem c2654 : check 60 115 18 2654 = true := by decide +kernel
theorem c2655 : check 60 115 18 2655 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2640 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2640) (chunksOK_one c2641)) (chunksOK_append (chunksOK_one c2642) (chunksOK_one c2643))) (chunksOK_append (chunksOK_append (chunksOK_one c2644) (chunksOK_one c2645)) (chunksOK_append (chunksOK_one c2646) (chunksOK_one c2647)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2648) (chunksOK_one c2649)) (chunksOK_append (chunksOK_one c2650) (chunksOK_one c2651))) (chunksOK_append (chunksOK_append (chunksOK_one c2652) (chunksOK_one c2653)) (chunksOK_append (chunksOK_one c2654) (chunksOK_one c2655)))))

end C165

namespace C166

theorem c2656 : check 60 115 18 2656 = true := by decide +kernel
theorem c2657 : check 60 115 18 2657 = true := by decide +kernel
theorem c2658 : check 60 115 18 2658 = true := by decide +kernel
theorem c2659 : check 60 115 18 2659 = true := by decide +kernel
theorem c2660 : check 60 115 18 2660 = true := by decide +kernel
theorem c2661 : check 60 115 18 2661 = true := by decide +kernel
theorem c2662 : check 60 115 18 2662 = true := by decide +kernel
theorem c2663 : check 60 115 18 2663 = true := by decide +kernel
theorem c2664 : check 60 115 18 2664 = true := by decide +kernel
theorem c2665 : check 60 115 18 2665 = true := by decide +kernel
theorem c2666 : check 60 115 18 2666 = true := by decide +kernel
theorem c2667 : check 60 115 18 2667 = true := by decide +kernel
theorem c2668 : check 60 115 18 2668 = true := by decide +kernel
theorem c2669 : check 60 115 18 2669 = true := by decide +kernel
theorem c2670 : check 60 115 18 2670 = true := by decide +kernel
theorem c2671 : check 60 115 18 2671 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2656 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2656) (chunksOK_one c2657)) (chunksOK_append (chunksOK_one c2658) (chunksOK_one c2659))) (chunksOK_append (chunksOK_append (chunksOK_one c2660) (chunksOK_one c2661)) (chunksOK_append (chunksOK_one c2662) (chunksOK_one c2663)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2664) (chunksOK_one c2665)) (chunksOK_append (chunksOK_one c2666) (chunksOK_one c2667))) (chunksOK_append (chunksOK_append (chunksOK_one c2668) (chunksOK_one c2669)) (chunksOK_append (chunksOK_one c2670) (chunksOK_one c2671)))))

end C166

namespace C167

theorem c2672 : check 60 115 18 2672 = true := by decide +kernel
theorem c2673 : check 60 115 18 2673 = true := by decide +kernel
theorem c2674 : check 60 115 18 2674 = true := by decide +kernel
theorem c2675 : check 60 115 18 2675 = true := by decide +kernel
theorem c2676 : check 60 115 18 2676 = true := by decide +kernel
theorem c2677 : check 60 115 18 2677 = true := by decide +kernel
theorem c2678 : check 60 115 18 2678 = true := by decide +kernel
theorem c2679 : check 60 115 18 2679 = true := by decide +kernel
theorem c2680 : check 60 115 18 2680 = true := by decide +kernel
theorem c2681 : check 60 115 18 2681 = true := by decide +kernel
theorem c2682 : check 60 115 18 2682 = true := by decide +kernel
theorem c2683 : check 60 115 18 2683 = true := by decide +kernel
theorem c2684 : check 60 115 18 2684 = true := by decide +kernel
theorem c2685 : check 60 115 18 2685 = true := by decide +kernel
theorem c2686 : check 60 115 18 2686 = true := by decide +kernel
theorem c2687 : check 60 115 18 2687 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2672 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2672) (chunksOK_one c2673)) (chunksOK_append (chunksOK_one c2674) (chunksOK_one c2675))) (chunksOK_append (chunksOK_append (chunksOK_one c2676) (chunksOK_one c2677)) (chunksOK_append (chunksOK_one c2678) (chunksOK_one c2679)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2680) (chunksOK_one c2681)) (chunksOK_append (chunksOK_one c2682) (chunksOK_one c2683))) (chunksOK_append (chunksOK_append (chunksOK_one c2684) (chunksOK_one c2685)) (chunksOK_append (chunksOK_one c2686) (chunksOK_one c2687)))))

end C167

namespace C168

theorem c2688 : check 60 115 18 2688 = true := by decide +kernel
theorem c2689 : check 60 115 18 2689 = true := by decide +kernel
theorem c2690 : check 60 115 18 2690 = true := by decide +kernel
theorem c2691 : check 60 115 18 2691 = true := by decide +kernel
theorem c2692 : check 60 115 18 2692 = true := by decide +kernel
theorem c2693 : check 60 115 18 2693 = true := by decide +kernel
theorem c2694 : check 60 115 18 2694 = true := by decide +kernel
theorem c2695 : check 60 115 18 2695 = true := by decide +kernel
theorem c2696 : check 60 115 18 2696 = true := by decide +kernel
theorem c2697 : check 60 115 18 2697 = true := by decide +kernel
theorem c2698 : check 60 115 18 2698 = true := by decide +kernel
theorem c2699 : check 60 115 18 2699 = true := by decide +kernel
theorem c2700 : check 60 115 18 2700 = true := by decide +kernel
theorem c2701 : check 60 115 18 2701 = true := by decide +kernel
theorem c2702 : check 60 115 18 2702 = true := by decide +kernel
theorem c2703 : check 60 115 18 2703 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2688 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2688) (chunksOK_one c2689)) (chunksOK_append (chunksOK_one c2690) (chunksOK_one c2691))) (chunksOK_append (chunksOK_append (chunksOK_one c2692) (chunksOK_one c2693)) (chunksOK_append (chunksOK_one c2694) (chunksOK_one c2695)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2696) (chunksOK_one c2697)) (chunksOK_append (chunksOK_one c2698) (chunksOK_one c2699))) (chunksOK_append (chunksOK_append (chunksOK_one c2700) (chunksOK_one c2701)) (chunksOK_append (chunksOK_one c2702) (chunksOK_one c2703)))))

end C168

namespace C169

theorem c2704 : check 60 115 18 2704 = true := by decide +kernel
theorem c2705 : check 60 115 18 2705 = true := by decide +kernel
theorem c2706 : check 60 115 18 2706 = true := by decide +kernel
theorem c2707 : check 60 115 18 2707 = true := by decide +kernel
theorem c2708 : check 60 115 18 2708 = true := by decide +kernel
theorem c2709 : check 60 115 18 2709 = true := by decide +kernel
theorem c2710 : check 60 115 18 2710 = true := by decide +kernel
theorem c2711 : check 60 115 18 2711 = true := by decide +kernel
theorem c2712 : check 60 115 18 2712 = true := by decide +kernel
theorem c2713 : check 60 115 18 2713 = true := by decide +kernel
theorem c2714 : check 60 115 18 2714 = true := by decide +kernel
theorem c2715 : check 60 115 18 2715 = true := by decide +kernel
theorem c2716 : check 60 115 18 2716 = true := by decide +kernel
theorem c2717 : check 60 115 18 2717 = true := by decide +kernel
theorem c2718 : check 60 115 18 2718 = true := by decide +kernel
theorem c2719 : check 60 115 18 2719 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2704 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2704) (chunksOK_one c2705)) (chunksOK_append (chunksOK_one c2706) (chunksOK_one c2707))) (chunksOK_append (chunksOK_append (chunksOK_one c2708) (chunksOK_one c2709)) (chunksOK_append (chunksOK_one c2710) (chunksOK_one c2711)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2712) (chunksOK_one c2713)) (chunksOK_append (chunksOK_one c2714) (chunksOK_one c2715))) (chunksOK_append (chunksOK_append (chunksOK_one c2716) (chunksOK_one c2717)) (chunksOK_append (chunksOK_one c2718) (chunksOK_one c2719)))))

end C169

namespace C170

theorem c2720 : check 60 115 18 2720 = true := by decide +kernel
theorem c2721 : check 60 115 18 2721 = true := by decide +kernel
theorem c2722 : check 60 115 18 2722 = true := by decide +kernel
theorem c2723 : check 60 115 18 2723 = true := by decide +kernel
theorem c2724 : check 60 115 18 2724 = true := by decide +kernel
theorem c2725 : check 60 115 18 2725 = true := by decide +kernel
theorem c2726 : check 60 115 18 2726 = true := by decide +kernel
theorem c2727 : check 60 115 18 2727 = true := by decide +kernel
theorem c2728 : check 60 115 18 2728 = true := by decide +kernel
theorem c2729 : check 60 115 18 2729 = true := by decide +kernel
theorem c2730 : check 60 115 18 2730 = true := by decide +kernel
theorem c2731 : check 60 115 18 2731 = true := by decide +kernel
theorem c2732 : check 60 115 18 2732 = true := by decide +kernel
theorem c2733 : check 60 115 18 2733 = true := by decide +kernel
theorem c2734 : check 60 115 18 2734 = true := by decide +kernel
theorem c2735 : check 60 115 18 2735 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2720 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2720) (chunksOK_one c2721)) (chunksOK_append (chunksOK_one c2722) (chunksOK_one c2723))) (chunksOK_append (chunksOK_append (chunksOK_one c2724) (chunksOK_one c2725)) (chunksOK_append (chunksOK_one c2726) (chunksOK_one c2727)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2728) (chunksOK_one c2729)) (chunksOK_append (chunksOK_one c2730) (chunksOK_one c2731))) (chunksOK_append (chunksOK_append (chunksOK_one c2732) (chunksOK_one c2733)) (chunksOK_append (chunksOK_one c2734) (chunksOK_one c2735)))))

end C170

namespace C171

theorem c2736 : check 60 115 18 2736 = true := by decide +kernel
theorem c2737 : check 60 115 18 2737 = true := by decide +kernel
theorem c2738 : check 60 115 18 2738 = true := by decide +kernel
theorem c2739 : check 60 115 18 2739 = true := by decide +kernel
theorem c2740 : check 60 115 18 2740 = true := by decide +kernel
theorem c2741 : check 60 115 18 2741 = true := by decide +kernel
theorem c2742 : check 60 115 18 2742 = true := by decide +kernel
theorem c2743 : check 60 115 18 2743 = true := by decide +kernel
theorem c2744 : check 60 115 18 2744 = true := by decide +kernel
theorem c2745 : check 60 115 18 2745 = true := by decide +kernel
theorem c2746 : check 60 115 18 2746 = true := by decide +kernel
theorem c2747 : check 60 115 18 2747 = true := by decide +kernel
theorem c2748 : check 60 115 18 2748 = true := by decide +kernel
theorem c2749 : check 60 115 18 2749 = true := by decide +kernel
theorem c2750 : check 60 115 18 2750 = true := by decide +kernel
theorem c2751 : check 60 115 18 2751 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2736 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2736) (chunksOK_one c2737)) (chunksOK_append (chunksOK_one c2738) (chunksOK_one c2739))) (chunksOK_append (chunksOK_append (chunksOK_one c2740) (chunksOK_one c2741)) (chunksOK_append (chunksOK_one c2742) (chunksOK_one c2743)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2744) (chunksOK_one c2745)) (chunksOK_append (chunksOK_one c2746) (chunksOK_one c2747))) (chunksOK_append (chunksOK_append (chunksOK_one c2748) (chunksOK_one c2749)) (chunksOK_append (chunksOK_one c2750) (chunksOK_one c2751)))))

end C171

namespace C172

theorem c2752 : check 60 115 18 2752 = true := by decide +kernel
theorem c2753 : check 60 115 18 2753 = true := by decide +kernel
theorem c2754 : check 60 115 18 2754 = true := by decide +kernel
theorem c2755 : check 60 115 18 2755 = true := by decide +kernel
theorem c2756 : check 60 115 18 2756 = true := by decide +kernel
theorem c2757 : check 60 115 18 2757 = true := by decide +kernel
theorem c2758 : check 60 115 18 2758 = true := by decide +kernel
theorem c2759 : check 60 115 18 2759 = true := by decide +kernel
theorem c2760 : check 60 115 18 2760 = true := by decide +kernel
theorem c2761 : check 60 115 18 2761 = true := by decide +kernel
theorem c2762 : check 60 115 18 2762 = true := by decide +kernel
theorem c2763 : check 60 115 18 2763 = true := by decide +kernel
theorem c2764 : check 60 115 18 2764 = true := by decide +kernel
theorem c2765 : check 60 115 18 2765 = true := by decide +kernel
theorem c2766 : check 60 115 18 2766 = true := by decide +kernel
theorem c2767 : check 60 115 18 2767 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2752 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2752) (chunksOK_one c2753)) (chunksOK_append (chunksOK_one c2754) (chunksOK_one c2755))) (chunksOK_append (chunksOK_append (chunksOK_one c2756) (chunksOK_one c2757)) (chunksOK_append (chunksOK_one c2758) (chunksOK_one c2759)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2760) (chunksOK_one c2761)) (chunksOK_append (chunksOK_one c2762) (chunksOK_one c2763))) (chunksOK_append (chunksOK_append (chunksOK_one c2764) (chunksOK_one c2765)) (chunksOK_append (chunksOK_one c2766) (chunksOK_one c2767)))))

end C172

namespace C173

theorem c2768 : check 60 115 18 2768 = true := by decide +kernel
theorem c2769 : check 60 115 18 2769 = true := by decide +kernel
theorem c2770 : check 60 115 18 2770 = true := by decide +kernel
theorem c2771 : check 60 115 18 2771 = true := by decide +kernel
theorem c2772 : check 60 115 18 2772 = true := by decide +kernel
theorem c2773 : check 60 115 18 2773 = true := by decide +kernel
theorem c2774 : check 60 115 18 2774 = true := by decide +kernel
theorem c2775 : check 60 115 18 2775 = true := by decide +kernel
theorem c2776 : check 60 115 18 2776 = true := by decide +kernel
theorem c2777 : check 60 115 18 2777 = true := by decide +kernel
theorem c2778 : check 60 115 18 2778 = true := by decide +kernel
theorem c2779 : check 60 115 18 2779 = true := by decide +kernel
theorem c2780 : check 60 115 18 2780 = true := by decide +kernel
theorem c2781 : check 60 115 18 2781 = true := by decide +kernel
theorem c2782 : check 60 115 18 2782 = true := by decide +kernel
theorem c2783 : check 60 115 18 2783 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2768 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2768) (chunksOK_one c2769)) (chunksOK_append (chunksOK_one c2770) (chunksOK_one c2771))) (chunksOK_append (chunksOK_append (chunksOK_one c2772) (chunksOK_one c2773)) (chunksOK_append (chunksOK_one c2774) (chunksOK_one c2775)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2776) (chunksOK_one c2777)) (chunksOK_append (chunksOK_one c2778) (chunksOK_one c2779))) (chunksOK_append (chunksOK_append (chunksOK_one c2780) (chunksOK_one c2781)) (chunksOK_append (chunksOK_one c2782) (chunksOK_one c2783)))))

end C173

namespace C174

theorem c2784 : check 60 115 18 2784 = true := by decide +kernel
theorem c2785 : check 60 115 18 2785 = true := by decide +kernel
theorem c2786 : check 60 115 18 2786 = true := by decide +kernel
theorem c2787 : check 60 115 18 2787 = true := by decide +kernel
theorem c2788 : check 60 115 18 2788 = true := by decide +kernel
theorem c2789 : check 60 115 18 2789 = true := by decide +kernel
theorem c2790 : check 60 115 18 2790 = true := by decide +kernel
theorem c2791 : check 60 115 18 2791 = true := by decide +kernel
theorem c2792 : check 60 115 18 2792 = true := by decide +kernel
theorem c2793 : check 60 115 18 2793 = true := by decide +kernel
theorem c2794 : check 60 115 18 2794 = true := by decide +kernel
theorem c2795 : check 60 115 18 2795 = true := by decide +kernel
theorem c2796 : check 60 115 18 2796 = true := by decide +kernel
theorem c2797 : check 60 115 18 2797 = true := by decide +kernel
theorem c2798 : check 60 115 18 2798 = true := by decide +kernel
theorem c2799 : check 60 115 18 2799 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2784 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2784) (chunksOK_one c2785)) (chunksOK_append (chunksOK_one c2786) (chunksOK_one c2787))) (chunksOK_append (chunksOK_append (chunksOK_one c2788) (chunksOK_one c2789)) (chunksOK_append (chunksOK_one c2790) (chunksOK_one c2791)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2792) (chunksOK_one c2793)) (chunksOK_append (chunksOK_one c2794) (chunksOK_one c2795))) (chunksOK_append (chunksOK_append (chunksOK_one c2796) (chunksOK_one c2797)) (chunksOK_append (chunksOK_one c2798) (chunksOK_one c2799)))))

end C174

namespace C175

theorem c2800 : check 60 115 18 2800 = true := by decide +kernel
theorem c2801 : check 60 115 18 2801 = true := by decide +kernel
theorem c2802 : check 60 115 18 2802 = true := by decide +kernel
theorem c2803 : check 60 115 18 2803 = true := by decide +kernel
theorem c2804 : check 60 115 18 2804 = true := by decide +kernel
theorem c2805 : check 60 115 18 2805 = true := by decide +kernel
theorem c2806 : check 60 115 18 2806 = true := by decide +kernel
theorem c2807 : check 60 115 18 2807 = true := by decide +kernel
theorem c2808 : check 60 115 18 2808 = true := by decide +kernel
theorem c2809 : check 60 115 18 2809 = true := by decide +kernel
theorem c2810 : check 60 115 18 2810 = true := by decide +kernel
theorem c2811 : check 60 115 18 2811 = true := by decide +kernel
theorem c2812 : check 60 115 18 2812 = true := by decide +kernel
theorem c2813 : check 60 115 18 2813 = true := by decide +kernel
theorem c2814 : check 60 115 18 2814 = true := by decide +kernel
theorem c2815 : check 60 115 18 2815 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2800 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2800) (chunksOK_one c2801)) (chunksOK_append (chunksOK_one c2802) (chunksOK_one c2803))) (chunksOK_append (chunksOK_append (chunksOK_one c2804) (chunksOK_one c2805)) (chunksOK_append (chunksOK_one c2806) (chunksOK_one c2807)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2808) (chunksOK_one c2809)) (chunksOK_append (chunksOK_one c2810) (chunksOK_one c2811))) (chunksOK_append (chunksOK_append (chunksOK_one c2812) (chunksOK_one c2813)) (chunksOK_append (chunksOK_one c2814) (chunksOK_one c2815)))))

end C175

namespace C176

theorem c2816 : check 60 115 18 2816 = true := by decide +kernel
theorem c2817 : check 60 115 18 2817 = true := by decide +kernel
theorem c2818 : check 60 115 18 2818 = true := by decide +kernel
theorem c2819 : check 60 115 18 2819 = true := by decide +kernel
theorem c2820 : check 60 115 18 2820 = true := by decide +kernel
theorem c2821 : check 60 115 18 2821 = true := by decide +kernel
theorem c2822 : check 60 115 18 2822 = true := by decide +kernel
theorem c2823 : check 60 115 18 2823 = true := by decide +kernel
theorem c2824 : check 60 115 18 2824 = true := by decide +kernel
theorem c2825 : check 60 115 18 2825 = true := by decide +kernel
theorem c2826 : check 60 115 18 2826 = true := by decide +kernel
theorem c2827 : check 60 115 18 2827 = true := by decide +kernel
theorem c2828 : check 60 115 18 2828 = true := by decide +kernel
theorem c2829 : check 60 115 18 2829 = true := by decide +kernel
theorem c2830 : check 60 115 18 2830 = true := by decide +kernel
theorem c2831 : check 60 115 18 2831 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2816 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2816) (chunksOK_one c2817)) (chunksOK_append (chunksOK_one c2818) (chunksOK_one c2819))) (chunksOK_append (chunksOK_append (chunksOK_one c2820) (chunksOK_one c2821)) (chunksOK_append (chunksOK_one c2822) (chunksOK_one c2823)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2824) (chunksOK_one c2825)) (chunksOK_append (chunksOK_one c2826) (chunksOK_one c2827))) (chunksOK_append (chunksOK_append (chunksOK_one c2828) (chunksOK_one c2829)) (chunksOK_append (chunksOK_one c2830) (chunksOK_one c2831)))))

end C176

namespace C177

theorem c2832 : check 60 115 18 2832 = true := by decide +kernel
theorem c2833 : check 60 115 18 2833 = true := by decide +kernel
theorem c2834 : check 60 115 18 2834 = true := by decide +kernel
theorem c2835 : check 60 115 18 2835 = true := by decide +kernel
theorem c2836 : check 60 115 18 2836 = true := by decide +kernel
theorem c2837 : check 60 115 18 2837 = true := by decide +kernel
theorem c2838 : check 60 115 18 2838 = true := by decide +kernel
theorem c2839 : check 60 115 18 2839 = true := by decide +kernel
theorem c2840 : check 60 115 18 2840 = true := by decide +kernel
theorem c2841 : check 60 115 18 2841 = true := by decide +kernel
theorem c2842 : check 60 115 18 2842 = true := by decide +kernel
theorem c2843 : check 60 115 18 2843 = true := by decide +kernel
theorem c2844 : check 60 115 18 2844 = true := by decide +kernel
theorem c2845 : check 60 115 18 2845 = true := by decide +kernel
theorem c2846 : check 60 115 18 2846 = true := by decide +kernel
theorem c2847 : check 60 115 18 2847 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2832 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2832) (chunksOK_one c2833)) (chunksOK_append (chunksOK_one c2834) (chunksOK_one c2835))) (chunksOK_append (chunksOK_append (chunksOK_one c2836) (chunksOK_one c2837)) (chunksOK_append (chunksOK_one c2838) (chunksOK_one c2839)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2840) (chunksOK_one c2841)) (chunksOK_append (chunksOK_one c2842) (chunksOK_one c2843))) (chunksOK_append (chunksOK_append (chunksOK_one c2844) (chunksOK_one c2845)) (chunksOK_append (chunksOK_one c2846) (chunksOK_one c2847)))))

end C177

namespace C178

theorem c2848 : check 60 115 18 2848 = true := by decide +kernel
theorem c2849 : check 60 115 18 2849 = true := by decide +kernel
theorem c2850 : check 60 115 18 2850 = true := by decide +kernel
theorem c2851 : check 60 115 18 2851 = true := by decide +kernel
theorem c2852 : check 60 115 18 2852 = true := by decide +kernel
theorem c2853 : check 60 115 18 2853 = true := by decide +kernel
theorem c2854 : check 60 115 18 2854 = true := by decide +kernel
theorem c2855 : check 60 115 18 2855 = true := by decide +kernel
theorem c2856 : check 60 115 18 2856 = true := by decide +kernel
theorem c2857 : check 60 115 18 2857 = true := by decide +kernel
theorem c2858 : check 60 115 18 2858 = true := by decide +kernel
theorem c2859 : check 60 115 18 2859 = true := by decide +kernel
theorem c2860 : check 60 115 18 2860 = true := by decide +kernel
theorem c2861 : check 60 115 18 2861 = true := by decide +kernel
theorem c2862 : check 60 115 18 2862 = true := by decide +kernel
theorem c2863 : check 60 115 18 2863 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2848 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2848) (chunksOK_one c2849)) (chunksOK_append (chunksOK_one c2850) (chunksOK_one c2851))) (chunksOK_append (chunksOK_append (chunksOK_one c2852) (chunksOK_one c2853)) (chunksOK_append (chunksOK_one c2854) (chunksOK_one c2855)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2856) (chunksOK_one c2857)) (chunksOK_append (chunksOK_one c2858) (chunksOK_one c2859))) (chunksOK_append (chunksOK_append (chunksOK_one c2860) (chunksOK_one c2861)) (chunksOK_append (chunksOK_one c2862) (chunksOK_one c2863)))))

end C178

namespace C179

theorem c2864 : check 60 115 18 2864 = true := by decide +kernel
theorem c2865 : check 60 115 18 2865 = true := by decide +kernel
theorem c2866 : check 60 115 18 2866 = true := by decide +kernel
theorem c2867 : check 60 115 18 2867 = true := by decide +kernel
theorem c2868 : check 60 115 18 2868 = true := by decide +kernel
theorem c2869 : check 60 115 18 2869 = true := by decide +kernel
theorem c2870 : check 60 115 18 2870 = true := by decide +kernel
theorem c2871 : check 60 115 18 2871 = true := by decide +kernel
theorem c2872 : check 60 115 18 2872 = true := by decide +kernel
theorem c2873 : check 60 115 18 2873 = true := by decide +kernel
theorem c2874 : check 60 115 18 2874 = true := by decide +kernel
theorem c2875 : check 60 115 18 2875 = true := by decide +kernel
theorem c2876 : check 60 115 18 2876 = true := by decide +kernel
theorem c2877 : check 60 115 18 2877 = true := by decide +kernel
theorem c2878 : check 60 115 18 2878 = true := by decide +kernel
theorem c2879 : check 60 115 18 2879 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2864 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2864) (chunksOK_one c2865)) (chunksOK_append (chunksOK_one c2866) (chunksOK_one c2867))) (chunksOK_append (chunksOK_append (chunksOK_one c2868) (chunksOK_one c2869)) (chunksOK_append (chunksOK_one c2870) (chunksOK_one c2871)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2872) (chunksOK_one c2873)) (chunksOK_append (chunksOK_one c2874) (chunksOK_one c2875))) (chunksOK_append (chunksOK_append (chunksOK_one c2876) (chunksOK_one c2877)) (chunksOK_append (chunksOK_one c2878) (chunksOK_one c2879)))))

end C179

namespace C180

theorem c2880 : check 60 115 18 2880 = true := by decide +kernel
theorem c2881 : check 60 115 18 2881 = true := by decide +kernel
theorem c2882 : check 60 115 18 2882 = true := by decide +kernel
theorem c2883 : check 60 115 18 2883 = true := by decide +kernel
theorem c2884 : check 60 115 18 2884 = true := by decide +kernel
theorem c2885 : check 60 115 18 2885 = true := by decide +kernel
theorem c2886 : check 60 115 18 2886 = true := by decide +kernel
theorem c2887 : check 60 115 18 2887 = true := by decide +kernel
theorem c2888 : check 60 115 18 2888 = true := by decide +kernel
theorem c2889 : check 60 115 18 2889 = true := by decide +kernel
theorem c2890 : check 60 115 18 2890 = true := by decide +kernel
theorem c2891 : check 60 115 18 2891 = true := by decide +kernel
theorem c2892 : check 60 115 18 2892 = true := by decide +kernel
theorem c2893 : check 60 115 18 2893 = true := by decide +kernel
theorem c2894 : check 60 115 18 2894 = true := by decide +kernel
theorem c2895 : check 60 115 18 2895 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2880 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2880) (chunksOK_one c2881)) (chunksOK_append (chunksOK_one c2882) (chunksOK_one c2883))) (chunksOK_append (chunksOK_append (chunksOK_one c2884) (chunksOK_one c2885)) (chunksOK_append (chunksOK_one c2886) (chunksOK_one c2887)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2888) (chunksOK_one c2889)) (chunksOK_append (chunksOK_one c2890) (chunksOK_one c2891))) (chunksOK_append (chunksOK_append (chunksOK_one c2892) (chunksOK_one c2893)) (chunksOK_append (chunksOK_one c2894) (chunksOK_one c2895)))))

end C180

namespace C181

theorem c2896 : check 60 115 18 2896 = true := by decide +kernel
theorem c2897 : check 60 115 18 2897 = true := by decide +kernel
theorem c2898 : check 60 115 18 2898 = true := by decide +kernel
theorem c2899 : check 60 115 18 2899 = true := by decide +kernel
theorem c2900 : check 60 115 18 2900 = true := by decide +kernel
theorem c2901 : check 60 115 18 2901 = true := by decide +kernel
theorem c2902 : check 60 115 18 2902 = true := by decide +kernel
theorem c2903 : check 60 115 18 2903 = true := by decide +kernel
theorem c2904 : check 60 115 18 2904 = true := by decide +kernel
theorem c2905 : check 60 115 18 2905 = true := by decide +kernel
theorem c2906 : check 60 115 18 2906 = true := by decide +kernel
theorem c2907 : check 60 115 18 2907 = true := by decide +kernel
theorem c2908 : check 60 115 18 2908 = true := by decide +kernel
theorem c2909 : check 60 115 18 2909 = true := by decide +kernel
theorem c2910 : check 60 115 18 2910 = true := by decide +kernel
theorem c2911 : check 60 115 18 2911 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2896 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2896) (chunksOK_one c2897)) (chunksOK_append (chunksOK_one c2898) (chunksOK_one c2899))) (chunksOK_append (chunksOK_append (chunksOK_one c2900) (chunksOK_one c2901)) (chunksOK_append (chunksOK_one c2902) (chunksOK_one c2903)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2904) (chunksOK_one c2905)) (chunksOK_append (chunksOK_one c2906) (chunksOK_one c2907))) (chunksOK_append (chunksOK_append (chunksOK_one c2908) (chunksOK_one c2909)) (chunksOK_append (chunksOK_one c2910) (chunksOK_one c2911)))))

end C181

namespace C182

theorem c2912 : check 60 115 18 2912 = true := by decide +kernel
theorem c2913 : check 60 115 18 2913 = true := by decide +kernel
theorem c2914 : check 60 115 18 2914 = true := by decide +kernel
theorem c2915 : check 60 115 18 2915 = true := by decide +kernel
theorem c2916 : check 60 115 18 2916 = true := by decide +kernel
theorem c2917 : check 60 115 18 2917 = true := by decide +kernel
theorem c2918 : check 60 115 18 2918 = true := by decide +kernel
theorem c2919 : check 60 115 18 2919 = true := by decide +kernel
theorem c2920 : check 60 115 18 2920 = true := by decide +kernel
theorem c2921 : check 60 115 18 2921 = true := by decide +kernel
theorem c2922 : check 60 115 18 2922 = true := by decide +kernel
theorem c2923 : check 60 115 18 2923 = true := by decide +kernel
theorem c2924 : check 60 115 18 2924 = true := by decide +kernel
theorem c2925 : check 60 115 18 2925 = true := by decide +kernel
theorem c2926 : check 60 115 18 2926 = true := by decide +kernel
theorem c2927 : check 60 115 18 2927 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2912 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2912) (chunksOK_one c2913)) (chunksOK_append (chunksOK_one c2914) (chunksOK_one c2915))) (chunksOK_append (chunksOK_append (chunksOK_one c2916) (chunksOK_one c2917)) (chunksOK_append (chunksOK_one c2918) (chunksOK_one c2919)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2920) (chunksOK_one c2921)) (chunksOK_append (chunksOK_one c2922) (chunksOK_one c2923))) (chunksOK_append (chunksOK_append (chunksOK_one c2924) (chunksOK_one c2925)) (chunksOK_append (chunksOK_one c2926) (chunksOK_one c2927)))))

end C182

namespace C183

theorem c2928 : check 60 115 18 2928 = true := by decide +kernel
theorem c2929 : check 60 115 18 2929 = true := by decide +kernel
theorem c2930 : check 60 115 18 2930 = true := by decide +kernel
theorem c2931 : check 60 115 18 2931 = true := by decide +kernel
theorem c2932 : check 60 115 18 2932 = true := by decide +kernel
theorem c2933 : check 60 115 18 2933 = true := by decide +kernel
theorem c2934 : check 60 115 18 2934 = true := by decide +kernel
theorem c2935 : check 60 115 18 2935 = true := by decide +kernel
theorem c2936 : check 60 115 18 2936 = true := by decide +kernel
theorem c2937 : check 60 115 18 2937 = true := by decide +kernel
theorem c2938 : check 60 115 18 2938 = true := by decide +kernel
theorem c2939 : check 60 115 18 2939 = true := by decide +kernel
theorem c2940 : check 60 115 18 2940 = true := by decide +kernel
theorem c2941 : check 60 115 18 2941 = true := by decide +kernel
theorem c2942 : check 60 115 18 2942 = true := by decide +kernel
theorem c2943 : check 60 115 18 2943 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2928 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2928) (chunksOK_one c2929)) (chunksOK_append (chunksOK_one c2930) (chunksOK_one c2931))) (chunksOK_append (chunksOK_append (chunksOK_one c2932) (chunksOK_one c2933)) (chunksOK_append (chunksOK_one c2934) (chunksOK_one c2935)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2936) (chunksOK_one c2937)) (chunksOK_append (chunksOK_one c2938) (chunksOK_one c2939))) (chunksOK_append (chunksOK_append (chunksOK_one c2940) (chunksOK_one c2941)) (chunksOK_append (chunksOK_one c2942) (chunksOK_one c2943)))))

end C183

namespace C184

theorem c2944 : check 60 115 18 2944 = true := by decide +kernel
theorem c2945 : check 60 115 18 2945 = true := by decide +kernel
theorem c2946 : check 60 115 18 2946 = true := by decide +kernel
theorem c2947 : check 60 115 18 2947 = true := by decide +kernel
theorem c2948 : check 60 115 18 2948 = true := by decide +kernel
theorem c2949 : check 60 115 18 2949 = true := by decide +kernel
theorem c2950 : check 60 115 18 2950 = true := by decide +kernel
theorem c2951 : check 60 115 18 2951 = true := by decide +kernel
theorem c2952 : check 60 115 18 2952 = true := by decide +kernel
theorem c2953 : check 60 115 18 2953 = true := by decide +kernel
theorem c2954 : check 60 115 18 2954 = true := by decide +kernel
theorem c2955 : check 60 115 18 2955 = true := by decide +kernel
theorem c2956 : check 60 115 18 2956 = true := by decide +kernel
theorem c2957 : check 60 115 18 2957 = true := by decide +kernel
theorem c2958 : check 60 115 18 2958 = true := by decide +kernel
theorem c2959 : check 60 115 18 2959 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2944 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2944) (chunksOK_one c2945)) (chunksOK_append (chunksOK_one c2946) (chunksOK_one c2947))) (chunksOK_append (chunksOK_append (chunksOK_one c2948) (chunksOK_one c2949)) (chunksOK_append (chunksOK_one c2950) (chunksOK_one c2951)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2952) (chunksOK_one c2953)) (chunksOK_append (chunksOK_one c2954) (chunksOK_one c2955))) (chunksOK_append (chunksOK_append (chunksOK_one c2956) (chunksOK_one c2957)) (chunksOK_append (chunksOK_one c2958) (chunksOK_one c2959)))))

end C184

namespace C185

theorem c2960 : check 60 115 18 2960 = true := by decide +kernel
theorem c2961 : check 60 115 18 2961 = true := by decide +kernel
theorem c2962 : check 60 115 18 2962 = true := by decide +kernel
theorem c2963 : check 60 115 18 2963 = true := by decide +kernel
theorem c2964 : check 60 115 18 2964 = true := by decide +kernel
theorem c2965 : check 60 115 18 2965 = true := by decide +kernel
theorem c2966 : check 60 115 18 2966 = true := by decide +kernel
theorem c2967 : check 60 115 18 2967 = true := by decide +kernel
theorem c2968 : check 60 115 18 2968 = true := by decide +kernel
theorem c2969 : check 60 115 18 2969 = true := by decide +kernel
theorem c2970 : check 60 115 18 2970 = true := by decide +kernel
theorem c2971 : check 60 115 18 2971 = true := by decide +kernel
theorem c2972 : check 60 115 18 2972 = true := by decide +kernel
theorem c2973 : check 60 115 18 2973 = true := by decide +kernel
theorem c2974 : check 60 115 18 2974 = true := by decide +kernel
theorem c2975 : check 60 115 18 2975 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2960 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2960) (chunksOK_one c2961)) (chunksOK_append (chunksOK_one c2962) (chunksOK_one c2963))) (chunksOK_append (chunksOK_append (chunksOK_one c2964) (chunksOK_one c2965)) (chunksOK_append (chunksOK_one c2966) (chunksOK_one c2967)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2968) (chunksOK_one c2969)) (chunksOK_append (chunksOK_one c2970) (chunksOK_one c2971))) (chunksOK_append (chunksOK_append (chunksOK_one c2972) (chunksOK_one c2973)) (chunksOK_append (chunksOK_one c2974) (chunksOK_one c2975)))))

end C185

namespace C186

theorem c2976 : check 60 115 18 2976 = true := by decide +kernel
theorem c2977 : check 60 115 18 2977 = true := by decide +kernel
theorem c2978 : check 60 115 18 2978 = true := by decide +kernel
theorem c2979 : check 60 115 18 2979 = true := by decide +kernel
theorem c2980 : check 60 115 18 2980 = true := by decide +kernel
theorem c2981 : check 60 115 18 2981 = true := by decide +kernel
theorem c2982 : check 60 115 18 2982 = true := by decide +kernel
theorem c2983 : check 60 115 18 2983 = true := by decide +kernel
theorem c2984 : check 60 115 18 2984 = true := by decide +kernel
theorem c2985 : check 60 115 18 2985 = true := by decide +kernel
theorem c2986 : check 60 115 18 2986 = true := by decide +kernel
theorem c2987 : check 60 115 18 2987 = true := by decide +kernel
theorem c2988 : check 60 115 18 2988 = true := by decide +kernel
theorem c2989 : check 60 115 18 2989 = true := by decide +kernel
theorem c2990 : check 60 115 18 2990 = true := by decide +kernel
theorem c2991 : check 60 115 18 2991 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2976 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2976) (chunksOK_one c2977)) (chunksOK_append (chunksOK_one c2978) (chunksOK_one c2979))) (chunksOK_append (chunksOK_append (chunksOK_one c2980) (chunksOK_one c2981)) (chunksOK_append (chunksOK_one c2982) (chunksOK_one c2983)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2984) (chunksOK_one c2985)) (chunksOK_append (chunksOK_one c2986) (chunksOK_one c2987))) (chunksOK_append (chunksOK_append (chunksOK_one c2988) (chunksOK_one c2989)) (chunksOK_append (chunksOK_one c2990) (chunksOK_one c2991)))))

end C186

namespace C187

theorem c2992 : check 60 115 18 2992 = true := by decide +kernel
theorem c2993 : check 60 115 18 2993 = true := by decide +kernel
theorem c2994 : check 60 115 18 2994 = true := by decide +kernel
theorem c2995 : check 60 115 18 2995 = true := by decide +kernel
theorem c2996 : check 60 115 18 2996 = true := by decide +kernel
theorem c2997 : check 60 115 18 2997 = true := by decide +kernel
theorem c2998 : check 60 115 18 2998 = true := by decide +kernel
theorem c2999 : check 60 115 18 2999 = true := by decide +kernel
theorem c3000 : check 60 115 18 3000 = true := by decide +kernel
theorem c3001 : check 60 115 18 3001 = true := by decide +kernel
theorem c3002 : check 60 115 18 3002 = true := by decide +kernel
theorem c3003 : check 60 115 18 3003 = true := by decide +kernel
theorem c3004 : check 60 115 18 3004 = true := by decide +kernel
theorem c3005 : check 60 115 18 3005 = true := by decide +kernel
theorem c3006 : check 60 115 18 3006 = true := by decide +kernel
theorem c3007 : check 60 115 18 3007 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 2992 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c2992) (chunksOK_one c2993)) (chunksOK_append (chunksOK_one c2994) (chunksOK_one c2995))) (chunksOK_append (chunksOK_append (chunksOK_one c2996) (chunksOK_one c2997)) (chunksOK_append (chunksOK_one c2998) (chunksOK_one c2999)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3000) (chunksOK_one c3001)) (chunksOK_append (chunksOK_one c3002) (chunksOK_one c3003))) (chunksOK_append (chunksOK_append (chunksOK_one c3004) (chunksOK_one c3005)) (chunksOK_append (chunksOK_one c3006) (chunksOK_one c3007)))))

end C187

namespace C188

theorem c3008 : check 60 115 18 3008 = true := by decide +kernel
theorem c3009 : check 60 115 18 3009 = true := by decide +kernel
theorem c3010 : check 60 115 18 3010 = true := by decide +kernel
theorem c3011 : check 60 115 18 3011 = true := by decide +kernel
theorem c3012 : check 60 115 18 3012 = true := by decide +kernel
theorem c3013 : check 60 115 18 3013 = true := by decide +kernel
theorem c3014 : check 60 115 18 3014 = true := by decide +kernel
theorem c3015 : check 60 115 18 3015 = true := by decide +kernel
theorem c3016 : check 60 115 18 3016 = true := by decide +kernel
theorem c3017 : check 60 115 18 3017 = true := by decide +kernel
theorem c3018 : check 60 115 18 3018 = true := by decide +kernel
theorem c3019 : check 60 115 18 3019 = true := by decide +kernel
theorem c3020 : check 60 115 18 3020 = true := by decide +kernel
theorem c3021 : check 60 115 18 3021 = true := by decide +kernel
theorem c3022 : check 60 115 18 3022 = true := by decide +kernel
theorem c3023 : check 60 115 18 3023 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3008 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3008) (chunksOK_one c3009)) (chunksOK_append (chunksOK_one c3010) (chunksOK_one c3011))) (chunksOK_append (chunksOK_append (chunksOK_one c3012) (chunksOK_one c3013)) (chunksOK_append (chunksOK_one c3014) (chunksOK_one c3015)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3016) (chunksOK_one c3017)) (chunksOK_append (chunksOK_one c3018) (chunksOK_one c3019))) (chunksOK_append (chunksOK_append (chunksOK_one c3020) (chunksOK_one c3021)) (chunksOK_append (chunksOK_one c3022) (chunksOK_one c3023)))))

end C188

namespace C189

theorem c3024 : check 60 115 18 3024 = true := by decide +kernel
theorem c3025 : check 60 115 18 3025 = true := by decide +kernel
theorem c3026 : check 60 115 18 3026 = true := by decide +kernel
theorem c3027 : check 60 115 18 3027 = true := by decide +kernel
theorem c3028 : check 60 115 18 3028 = true := by decide +kernel
theorem c3029 : check 60 115 18 3029 = true := by decide +kernel
theorem c3030 : check 60 115 18 3030 = true := by decide +kernel
theorem c3031 : check 60 115 18 3031 = true := by decide +kernel
theorem c3032 : check 60 115 18 3032 = true := by decide +kernel
theorem c3033 : check 60 115 18 3033 = true := by decide +kernel
theorem c3034 : check 60 115 18 3034 = true := by decide +kernel
theorem c3035 : check 60 115 18 3035 = true := by decide +kernel
theorem c3036 : check 60 115 18 3036 = true := by decide +kernel
theorem c3037 : check 60 115 18 3037 = true := by decide +kernel
theorem c3038 : check 60 115 18 3038 = true := by decide +kernel
theorem c3039 : check 60 115 18 3039 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3024 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3024) (chunksOK_one c3025)) (chunksOK_append (chunksOK_one c3026) (chunksOK_one c3027))) (chunksOK_append (chunksOK_append (chunksOK_one c3028) (chunksOK_one c3029)) (chunksOK_append (chunksOK_one c3030) (chunksOK_one c3031)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3032) (chunksOK_one c3033)) (chunksOK_append (chunksOK_one c3034) (chunksOK_one c3035))) (chunksOK_append (chunksOK_append (chunksOK_one c3036) (chunksOK_one c3037)) (chunksOK_append (chunksOK_one c3038) (chunksOK_one c3039)))))

end C189

namespace C190

theorem c3040 : check 60 115 18 3040 = true := by decide +kernel
theorem c3041 : check 60 115 18 3041 = true := by decide +kernel
theorem c3042 : check 60 115 18 3042 = true := by decide +kernel
theorem c3043 : check 60 115 18 3043 = true := by decide +kernel
theorem c3044 : check 60 115 18 3044 = true := by decide +kernel
theorem c3045 : check 60 115 18 3045 = true := by decide +kernel
theorem c3046 : check 60 115 18 3046 = true := by decide +kernel
theorem c3047 : check 60 115 18 3047 = true := by decide +kernel
theorem c3048 : check 60 115 18 3048 = true := by decide +kernel
theorem c3049 : check 60 115 18 3049 = true := by decide +kernel
theorem c3050 : check 60 115 18 3050 = true := by decide +kernel
theorem c3051 : check 60 115 18 3051 = true := by decide +kernel
theorem c3052 : check 60 115 18 3052 = true := by decide +kernel
theorem c3053 : check 60 115 18 3053 = true := by decide +kernel
theorem c3054 : check 60 115 18 3054 = true := by decide +kernel
theorem c3055 : check 60 115 18 3055 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3040 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3040) (chunksOK_one c3041)) (chunksOK_append (chunksOK_one c3042) (chunksOK_one c3043))) (chunksOK_append (chunksOK_append (chunksOK_one c3044) (chunksOK_one c3045)) (chunksOK_append (chunksOK_one c3046) (chunksOK_one c3047)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3048) (chunksOK_one c3049)) (chunksOK_append (chunksOK_one c3050) (chunksOK_one c3051))) (chunksOK_append (chunksOK_append (chunksOK_one c3052) (chunksOK_one c3053)) (chunksOK_append (chunksOK_one c3054) (chunksOK_one c3055)))))

end C190

namespace C191

theorem c3056 : check 60 115 18 3056 = true := by decide +kernel
theorem c3057 : check 60 115 18 3057 = true := by decide +kernel
theorem c3058 : check 60 115 18 3058 = true := by decide +kernel
theorem c3059 : check 60 115 18 3059 = true := by decide +kernel
theorem c3060 : check 60 115 18 3060 = true := by decide +kernel
theorem c3061 : check 60 115 18 3061 = true := by decide +kernel
theorem c3062 : check 60 115 18 3062 = true := by decide +kernel
theorem c3063 : check 60 115 18 3063 = true := by decide +kernel
theorem c3064 : check 60 115 18 3064 = true := by decide +kernel
theorem c3065 : check 60 115 18 3065 = true := by decide +kernel
theorem c3066 : check 60 115 18 3066 = true := by decide +kernel
theorem c3067 : check 60 115 18 3067 = true := by decide +kernel
theorem c3068 : check 60 115 18 3068 = true := by decide +kernel
theorem c3069 : check 60 115 18 3069 = true := by decide +kernel
theorem c3070 : check 60 115 18 3070 = true := by decide +kernel
theorem c3071 : check 60 115 18 3071 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3056 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3056) (chunksOK_one c3057)) (chunksOK_append (chunksOK_one c3058) (chunksOK_one c3059))) (chunksOK_append (chunksOK_append (chunksOK_one c3060) (chunksOK_one c3061)) (chunksOK_append (chunksOK_one c3062) (chunksOK_one c3063)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3064) (chunksOK_one c3065)) (chunksOK_append (chunksOK_one c3066) (chunksOK_one c3067))) (chunksOK_append (chunksOK_append (chunksOK_one c3068) (chunksOK_one c3069)) (chunksOK_append (chunksOK_one c3070) (chunksOK_one c3071)))))

end C191

namespace C192

theorem c3072 : check 60 115 18 3072 = true := by decide +kernel
theorem c3073 : check 60 115 18 3073 = true := by decide +kernel
theorem c3074 : check 60 115 18 3074 = true := by decide +kernel
theorem c3075 : check 60 115 18 3075 = true := by decide +kernel
theorem c3076 : check 60 115 18 3076 = true := by decide +kernel
theorem c3077 : check 60 115 18 3077 = true := by decide +kernel
theorem c3078 : check 60 115 18 3078 = true := by decide +kernel
theorem c3079 : check 60 115 18 3079 = true := by decide +kernel
theorem c3080 : check 60 115 18 3080 = true := by decide +kernel
theorem c3081 : check 60 115 18 3081 = true := by decide +kernel
theorem c3082 : check 60 115 18 3082 = true := by decide +kernel
theorem c3083 : check 60 115 18 3083 = true := by decide +kernel
theorem c3084 : check 60 115 18 3084 = true := by decide +kernel
theorem c3085 : check 60 115 18 3085 = true := by decide +kernel
theorem c3086 : check 60 115 18 3086 = true := by decide +kernel
theorem c3087 : check 60 115 18 3087 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3072 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3072) (chunksOK_one c3073)) (chunksOK_append (chunksOK_one c3074) (chunksOK_one c3075))) (chunksOK_append (chunksOK_append (chunksOK_one c3076) (chunksOK_one c3077)) (chunksOK_append (chunksOK_one c3078) (chunksOK_one c3079)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3080) (chunksOK_one c3081)) (chunksOK_append (chunksOK_one c3082) (chunksOK_one c3083))) (chunksOK_append (chunksOK_append (chunksOK_one c3084) (chunksOK_one c3085)) (chunksOK_append (chunksOK_one c3086) (chunksOK_one c3087)))))

end C192

namespace C193

theorem c3088 : check 60 115 18 3088 = true := by decide +kernel
theorem c3089 : check 60 115 18 3089 = true := by decide +kernel
theorem c3090 : check 60 115 18 3090 = true := by decide +kernel
theorem c3091 : check 60 115 18 3091 = true := by decide +kernel
theorem c3092 : check 60 115 18 3092 = true := by decide +kernel
theorem c3093 : check 60 115 18 3093 = true := by decide +kernel
theorem c3094 : check 60 115 18 3094 = true := by decide +kernel
theorem c3095 : check 60 115 18 3095 = true := by decide +kernel
theorem c3096 : check 60 115 18 3096 = true := by decide +kernel
theorem c3097 : check 60 115 18 3097 = true := by decide +kernel
theorem c3098 : check 60 115 18 3098 = true := by decide +kernel
theorem c3099 : check 60 115 18 3099 = true := by decide +kernel
theorem c3100 : check 60 115 18 3100 = true := by decide +kernel
theorem c3101 : check 60 115 18 3101 = true := by decide +kernel
theorem c3102 : check 60 115 18 3102 = true := by decide +kernel
theorem c3103 : check 60 115 18 3103 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3088 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3088) (chunksOK_one c3089)) (chunksOK_append (chunksOK_one c3090) (chunksOK_one c3091))) (chunksOK_append (chunksOK_append (chunksOK_one c3092) (chunksOK_one c3093)) (chunksOK_append (chunksOK_one c3094) (chunksOK_one c3095)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3096) (chunksOK_one c3097)) (chunksOK_append (chunksOK_one c3098) (chunksOK_one c3099))) (chunksOK_append (chunksOK_append (chunksOK_one c3100) (chunksOK_one c3101)) (chunksOK_append (chunksOK_one c3102) (chunksOK_one c3103)))))

end C193

namespace C194

theorem c3104 : check 60 115 18 3104 = true := by decide +kernel
theorem c3105 : check 60 115 18 3105 = true := by decide +kernel
theorem c3106 : check 60 115 18 3106 = true := by decide +kernel
theorem c3107 : check 60 115 18 3107 = true := by decide +kernel
theorem c3108 : check 60 115 18 3108 = true := by decide +kernel
theorem c3109 : check 60 115 18 3109 = true := by decide +kernel
theorem c3110 : check 60 115 18 3110 = true := by decide +kernel
theorem c3111 : check 60 115 18 3111 = true := by decide +kernel
theorem c3112 : check 60 115 18 3112 = true := by decide +kernel
theorem c3113 : check 60 115 18 3113 = true := by decide +kernel
theorem c3114 : check 60 115 18 3114 = true := by decide +kernel
theorem c3115 : check 60 115 18 3115 = true := by decide +kernel
theorem c3116 : check 60 115 18 3116 = true := by decide +kernel
theorem c3117 : check 60 115 18 3117 = true := by decide +kernel
theorem c3118 : check 60 115 18 3118 = true := by decide +kernel
theorem c3119 : check 60 115 18 3119 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3104 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3104) (chunksOK_one c3105)) (chunksOK_append (chunksOK_one c3106) (chunksOK_one c3107))) (chunksOK_append (chunksOK_append (chunksOK_one c3108) (chunksOK_one c3109)) (chunksOK_append (chunksOK_one c3110) (chunksOK_one c3111)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3112) (chunksOK_one c3113)) (chunksOK_append (chunksOK_one c3114) (chunksOK_one c3115))) (chunksOK_append (chunksOK_append (chunksOK_one c3116) (chunksOK_one c3117)) (chunksOK_append (chunksOK_one c3118) (chunksOK_one c3119)))))

end C194

namespace C195

theorem c3120 : check 60 115 18 3120 = true := by decide +kernel
theorem c3121 : check 60 115 18 3121 = true := by decide +kernel
theorem c3122 : check 60 115 18 3122 = true := by decide +kernel
theorem c3123 : check 60 115 18 3123 = true := by decide +kernel
theorem c3124 : check 60 115 18 3124 = true := by decide +kernel
theorem c3125 : check 60 115 18 3125 = true := by decide +kernel
theorem c3126 : check 60 115 18 3126 = true := by decide +kernel
theorem c3127 : check 60 115 18 3127 = true := by decide +kernel
theorem c3128 : check 60 115 18 3128 = true := by decide +kernel
theorem c3129 : check 60 115 18 3129 = true := by decide +kernel
theorem c3130 : check 60 115 18 3130 = true := by decide +kernel
theorem c3131 : check 60 115 18 3131 = true := by decide +kernel
theorem c3132 : check 60 115 18 3132 = true := by decide +kernel
theorem c3133 : check 60 115 18 3133 = true := by decide +kernel
theorem c3134 : check 60 115 18 3134 = true := by decide +kernel
theorem c3135 : check 60 115 18 3135 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3120 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3120) (chunksOK_one c3121)) (chunksOK_append (chunksOK_one c3122) (chunksOK_one c3123))) (chunksOK_append (chunksOK_append (chunksOK_one c3124) (chunksOK_one c3125)) (chunksOK_append (chunksOK_one c3126) (chunksOK_one c3127)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3128) (chunksOK_one c3129)) (chunksOK_append (chunksOK_one c3130) (chunksOK_one c3131))) (chunksOK_append (chunksOK_append (chunksOK_one c3132) (chunksOK_one c3133)) (chunksOK_append (chunksOK_one c3134) (chunksOK_one c3135)))))

end C195

namespace C196

theorem c3136 : check 60 115 18 3136 = true := by decide +kernel
theorem c3137 : check 60 115 18 3137 = true := by decide +kernel
theorem c3138 : check 60 115 18 3138 = true := by decide +kernel
theorem c3139 : check 60 115 18 3139 = true := by decide +kernel
theorem c3140 : check 60 115 18 3140 = true := by decide +kernel
theorem c3141 : check 60 115 18 3141 = true := by decide +kernel
theorem c3142 : check 60 115 18 3142 = true := by decide +kernel
theorem c3143 : check 60 115 18 3143 = true := by decide +kernel
theorem c3144 : check 60 115 18 3144 = true := by decide +kernel
theorem c3145 : check 60 115 18 3145 = true := by decide +kernel
theorem c3146 : check 60 115 18 3146 = true := by decide +kernel
theorem c3147 : check 60 115 18 3147 = true := by decide +kernel
theorem c3148 : check 60 115 18 3148 = true := by decide +kernel
theorem c3149 : check 60 115 18 3149 = true := by decide +kernel
theorem c3150 : check 60 115 18 3150 = true := by decide +kernel
theorem c3151 : check 60 115 18 3151 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3136 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3136) (chunksOK_one c3137)) (chunksOK_append (chunksOK_one c3138) (chunksOK_one c3139))) (chunksOK_append (chunksOK_append (chunksOK_one c3140) (chunksOK_one c3141)) (chunksOK_append (chunksOK_one c3142) (chunksOK_one c3143)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3144) (chunksOK_one c3145)) (chunksOK_append (chunksOK_one c3146) (chunksOK_one c3147))) (chunksOK_append (chunksOK_append (chunksOK_one c3148) (chunksOK_one c3149)) (chunksOK_append (chunksOK_one c3150) (chunksOK_one c3151)))))

end C196

namespace C197

theorem c3152 : check 60 115 18 3152 = true := by decide +kernel
theorem c3153 : check 60 115 18 3153 = true := by decide +kernel
theorem c3154 : check 60 115 18 3154 = true := by decide +kernel
theorem c3155 : check 60 115 18 3155 = true := by decide +kernel
theorem c3156 : check 60 115 18 3156 = true := by decide +kernel
theorem c3157 : check 60 115 18 3157 = true := by decide +kernel
theorem c3158 : check 60 115 18 3158 = true := by decide +kernel
theorem c3159 : check 60 115 18 3159 = true := by decide +kernel
theorem c3160 : check 60 115 18 3160 = true := by decide +kernel
theorem c3161 : check 60 115 18 3161 = true := by decide +kernel
theorem c3162 : check 60 115 18 3162 = true := by decide +kernel
theorem c3163 : check 60 115 18 3163 = true := by decide +kernel
theorem c3164 : check 60 115 18 3164 = true := by decide +kernel
theorem c3165 : check 60 115 18 3165 = true := by decide +kernel
theorem c3166 : check 60 115 18 3166 = true := by decide +kernel
theorem c3167 : check 60 115 18 3167 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3152 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3152) (chunksOK_one c3153)) (chunksOK_append (chunksOK_one c3154) (chunksOK_one c3155))) (chunksOK_append (chunksOK_append (chunksOK_one c3156) (chunksOK_one c3157)) (chunksOK_append (chunksOK_one c3158) (chunksOK_one c3159)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3160) (chunksOK_one c3161)) (chunksOK_append (chunksOK_one c3162) (chunksOK_one c3163))) (chunksOK_append (chunksOK_append (chunksOK_one c3164) (chunksOK_one c3165)) (chunksOK_append (chunksOK_one c3166) (chunksOK_one c3167)))))

end C197

namespace C198

theorem c3168 : check 60 115 18 3168 = true := by decide +kernel
theorem c3169 : check 60 115 18 3169 = true := by decide +kernel
theorem c3170 : check 60 115 18 3170 = true := by decide +kernel
theorem c3171 : check 60 115 18 3171 = true := by decide +kernel
theorem c3172 : check 60 115 18 3172 = true := by decide +kernel
theorem c3173 : check 60 115 18 3173 = true := by decide +kernel
theorem c3174 : check 60 115 18 3174 = true := by decide +kernel
theorem c3175 : check 60 115 18 3175 = true := by decide +kernel
theorem c3176 : check 60 115 18 3176 = true := by decide +kernel
theorem c3177 : check 60 115 18 3177 = true := by decide +kernel
theorem c3178 : check 60 115 18 3178 = true := by decide +kernel
theorem c3179 : check 60 115 18 3179 = true := by decide +kernel
theorem c3180 : check 60 115 18 3180 = true := by decide +kernel
theorem c3181 : check 60 115 18 3181 = true := by decide +kernel
theorem c3182 : check 60 115 18 3182 = true := by decide +kernel
theorem c3183 : check 60 115 18 3183 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3168 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3168) (chunksOK_one c3169)) (chunksOK_append (chunksOK_one c3170) (chunksOK_one c3171))) (chunksOK_append (chunksOK_append (chunksOK_one c3172) (chunksOK_one c3173)) (chunksOK_append (chunksOK_one c3174) (chunksOK_one c3175)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3176) (chunksOK_one c3177)) (chunksOK_append (chunksOK_one c3178) (chunksOK_one c3179))) (chunksOK_append (chunksOK_append (chunksOK_one c3180) (chunksOK_one c3181)) (chunksOK_append (chunksOK_one c3182) (chunksOK_one c3183)))))

end C198

namespace C199

theorem c3184 : check 60 115 18 3184 = true := by decide +kernel
theorem c3185 : check 60 115 18 3185 = true := by decide +kernel
theorem c3186 : check 60 115 18 3186 = true := by decide +kernel
theorem c3187 : check 60 115 18 3187 = true := by decide +kernel
theorem c3188 : check 60 115 18 3188 = true := by decide +kernel
theorem c3189 : check 60 115 18 3189 = true := by decide +kernel
theorem c3190 : check 60 115 18 3190 = true := by decide +kernel
theorem c3191 : check 60 115 18 3191 = true := by decide +kernel
theorem c3192 : check 60 115 18 3192 = true := by decide +kernel
theorem c3193 : check 60 115 18 3193 = true := by decide +kernel
theorem c3194 : check 60 115 18 3194 = true := by decide +kernel
theorem c3195 : check 60 115 18 3195 = true := by decide +kernel
theorem c3196 : check 60 115 18 3196 = true := by decide +kernel
theorem c3197 : check 60 115 18 3197 = true := by decide +kernel
theorem c3198 : check 60 115 18 3198 = true := by decide +kernel
theorem c3199 : check 60 115 18 3199 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3184 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3184) (chunksOK_one c3185)) (chunksOK_append (chunksOK_one c3186) (chunksOK_one c3187))) (chunksOK_append (chunksOK_append (chunksOK_one c3188) (chunksOK_one c3189)) (chunksOK_append (chunksOK_one c3190) (chunksOK_one c3191)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3192) (chunksOK_one c3193)) (chunksOK_append (chunksOK_one c3194) (chunksOK_one c3195))) (chunksOK_append (chunksOK_append (chunksOK_one c3196) (chunksOK_one c3197)) (chunksOK_append (chunksOK_one c3198) (chunksOK_one c3199)))))

end C199

namespace C200

theorem c3200 : check 60 115 18 3200 = true := by decide +kernel
theorem c3201 : check 60 115 18 3201 = true := by decide +kernel
theorem c3202 : check 60 115 18 3202 = true := by decide +kernel
theorem c3203 : check 60 115 18 3203 = true := by decide +kernel
theorem c3204 : check 60 115 18 3204 = true := by decide +kernel
theorem c3205 : check 60 115 18 3205 = true := by decide +kernel
theorem c3206 : check 60 115 18 3206 = true := by decide +kernel
theorem c3207 : check 60 115 18 3207 = true := by decide +kernel
theorem c3208 : check 60 115 18 3208 = true := by decide +kernel
theorem c3209 : check 60 115 18 3209 = true := by decide +kernel
theorem c3210 : check 60 115 18 3210 = true := by decide +kernel
theorem c3211 : check 60 115 18 3211 = true := by decide +kernel
theorem c3212 : check 60 115 18 3212 = true := by decide +kernel
theorem c3213 : check 60 115 18 3213 = true := by decide +kernel
theorem c3214 : check 60 115 18 3214 = true := by decide +kernel
theorem c3215 : check 60 115 18 3215 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3200 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3200) (chunksOK_one c3201)) (chunksOK_append (chunksOK_one c3202) (chunksOK_one c3203))) (chunksOK_append (chunksOK_append (chunksOK_one c3204) (chunksOK_one c3205)) (chunksOK_append (chunksOK_one c3206) (chunksOK_one c3207)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3208) (chunksOK_one c3209)) (chunksOK_append (chunksOK_one c3210) (chunksOK_one c3211))) (chunksOK_append (chunksOK_append (chunksOK_one c3212) (chunksOK_one c3213)) (chunksOK_append (chunksOK_one c3214) (chunksOK_one c3215)))))

end C200

namespace C201

theorem c3216 : check 60 115 18 3216 = true := by decide +kernel
theorem c3217 : check 60 115 18 3217 = true := by decide +kernel
theorem c3218 : check 60 115 18 3218 = true := by decide +kernel
theorem c3219 : check 60 115 18 3219 = true := by decide +kernel
theorem c3220 : check 60 115 18 3220 = true := by decide +kernel
theorem c3221 : check 60 115 18 3221 = true := by decide +kernel
theorem c3222 : check 60 115 18 3222 = true := by decide +kernel
theorem c3223 : check 60 115 18 3223 = true := by decide +kernel
theorem c3224 : check 60 115 18 3224 = true := by decide +kernel
theorem c3225 : check 60 115 18 3225 = true := by decide +kernel
theorem c3226 : check 60 115 18 3226 = true := by decide +kernel
theorem c3227 : check 60 115 18 3227 = true := by decide +kernel
theorem c3228 : check 60 115 18 3228 = true := by decide +kernel
theorem c3229 : check 60 115 18 3229 = true := by decide +kernel
theorem c3230 : check 60 115 18 3230 = true := by decide +kernel
theorem c3231 : check 60 115 18 3231 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3216 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3216) (chunksOK_one c3217)) (chunksOK_append (chunksOK_one c3218) (chunksOK_one c3219))) (chunksOK_append (chunksOK_append (chunksOK_one c3220) (chunksOK_one c3221)) (chunksOK_append (chunksOK_one c3222) (chunksOK_one c3223)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3224) (chunksOK_one c3225)) (chunksOK_append (chunksOK_one c3226) (chunksOK_one c3227))) (chunksOK_append (chunksOK_append (chunksOK_one c3228) (chunksOK_one c3229)) (chunksOK_append (chunksOK_one c3230) (chunksOK_one c3231)))))

end C201

namespace C202

theorem c3232 : check 60 115 18 3232 = true := by decide +kernel
theorem c3233 : check 60 115 18 3233 = true := by decide +kernel
theorem c3234 : check 60 115 18 3234 = true := by decide +kernel
theorem c3235 : check 60 115 18 3235 = true := by decide +kernel
theorem c3236 : check 60 115 18 3236 = true := by decide +kernel
theorem c3237 : check 60 115 18 3237 = true := by decide +kernel
theorem c3238 : check 60 115 18 3238 = true := by decide +kernel
theorem c3239 : check 60 115 18 3239 = true := by decide +kernel
theorem c3240 : check 60 115 18 3240 = true := by decide +kernel
theorem c3241 : check 60 115 18 3241 = true := by decide +kernel
theorem c3242 : check 60 115 18 3242 = true := by decide +kernel
theorem c3243 : check 60 115 18 3243 = true := by decide +kernel
theorem c3244 : check 60 115 18 3244 = true := by decide +kernel
theorem c3245 : check 60 115 18 3245 = true := by decide +kernel
theorem c3246 : check 60 115 18 3246 = true := by decide +kernel
theorem c3247 : check 60 115 18 3247 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3232 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3232) (chunksOK_one c3233)) (chunksOK_append (chunksOK_one c3234) (chunksOK_one c3235))) (chunksOK_append (chunksOK_append (chunksOK_one c3236) (chunksOK_one c3237)) (chunksOK_append (chunksOK_one c3238) (chunksOK_one c3239)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3240) (chunksOK_one c3241)) (chunksOK_append (chunksOK_one c3242) (chunksOK_one c3243))) (chunksOK_append (chunksOK_append (chunksOK_one c3244) (chunksOK_one c3245)) (chunksOK_append (chunksOK_one c3246) (chunksOK_one c3247)))))

end C202

namespace C203

theorem c3248 : check 60 115 18 3248 = true := by decide +kernel
theorem c3249 : check 60 115 18 3249 = true := by decide +kernel
theorem c3250 : check 60 115 18 3250 = true := by decide +kernel
theorem c3251 : check 60 115 18 3251 = true := by decide +kernel
theorem c3252 : check 60 115 18 3252 = true := by decide +kernel
theorem c3253 : check 60 115 18 3253 = true := by decide +kernel
theorem c3254 : check 60 115 18 3254 = true := by decide +kernel
theorem c3255 : check 60 115 18 3255 = true := by decide +kernel
theorem c3256 : check 60 115 18 3256 = true := by decide +kernel
theorem c3257 : check 60 115 18 3257 = true := by decide +kernel
theorem c3258 : check 60 115 18 3258 = true := by decide +kernel
theorem c3259 : check 60 115 18 3259 = true := by decide +kernel
theorem c3260 : check 60 115 18 3260 = true := by decide +kernel
theorem c3261 : check 60 115 18 3261 = true := by decide +kernel
theorem c3262 : check 60 115 18 3262 = true := by decide +kernel
theorem c3263 : check 60 115 18 3263 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3248 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3248) (chunksOK_one c3249)) (chunksOK_append (chunksOK_one c3250) (chunksOK_one c3251))) (chunksOK_append (chunksOK_append (chunksOK_one c3252) (chunksOK_one c3253)) (chunksOK_append (chunksOK_one c3254) (chunksOK_one c3255)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3256) (chunksOK_one c3257)) (chunksOK_append (chunksOK_one c3258) (chunksOK_one c3259))) (chunksOK_append (chunksOK_append (chunksOK_one c3260) (chunksOK_one c3261)) (chunksOK_append (chunksOK_one c3262) (chunksOK_one c3263)))))

end C203

namespace C204

theorem c3264 : check 60 115 18 3264 = true := by decide +kernel
theorem c3265 : check 60 115 18 3265 = true := by decide +kernel
theorem c3266 : check 60 115 18 3266 = true := by decide +kernel
theorem c3267 : check 60 115 18 3267 = true := by decide +kernel
theorem c3268 : check 60 115 18 3268 = true := by decide +kernel
theorem c3269 : check 60 115 18 3269 = true := by decide +kernel
theorem c3270 : check 60 115 18 3270 = true := by decide +kernel
theorem c3271 : check 60 115 18 3271 = true := by decide +kernel
theorem c3272 : check 60 115 18 3272 = true := by decide +kernel
theorem c3273 : check 60 115 18 3273 = true := by decide +kernel
theorem c3274 : check 60 115 18 3274 = true := by decide +kernel
theorem c3275 : check 60 115 18 3275 = true := by decide +kernel
theorem c3276 : check 60 115 18 3276 = true := by decide +kernel
theorem c3277 : check 60 115 18 3277 = true := by decide +kernel
theorem c3278 : check 60 115 18 3278 = true := by decide +kernel
theorem c3279 : check 60 115 18 3279 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3264 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3264) (chunksOK_one c3265)) (chunksOK_append (chunksOK_one c3266) (chunksOK_one c3267))) (chunksOK_append (chunksOK_append (chunksOK_one c3268) (chunksOK_one c3269)) (chunksOK_append (chunksOK_one c3270) (chunksOK_one c3271)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3272) (chunksOK_one c3273)) (chunksOK_append (chunksOK_one c3274) (chunksOK_one c3275))) (chunksOK_append (chunksOK_append (chunksOK_one c3276) (chunksOK_one c3277)) (chunksOK_append (chunksOK_one c3278) (chunksOK_one c3279)))))

end C204

namespace C205

theorem c3280 : check 60 115 18 3280 = true := by decide +kernel
theorem c3281 : check 60 115 18 3281 = true := by decide +kernel
theorem c3282 : check 60 115 18 3282 = true := by decide +kernel
theorem c3283 : check 60 115 18 3283 = true := by decide +kernel
theorem c3284 : check 60 115 18 3284 = true := by decide +kernel
theorem c3285 : check 60 115 18 3285 = true := by decide +kernel
theorem c3286 : check 60 115 18 3286 = true := by decide +kernel
theorem c3287 : check 60 115 18 3287 = true := by decide +kernel
theorem c3288 : check 60 115 18 3288 = true := by decide +kernel
theorem c3289 : check 60 115 18 3289 = true := by decide +kernel
theorem c3290 : check 60 115 18 3290 = true := by decide +kernel
theorem c3291 : check 60 115 18 3291 = true := by decide +kernel
theorem c3292 : check 60 115 18 3292 = true := by decide +kernel
theorem c3293 : check 60 115 18 3293 = true := by decide +kernel
theorem c3294 : check 60 115 18 3294 = true := by decide +kernel
theorem c3295 : check 60 115 18 3295 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3280 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3280) (chunksOK_one c3281)) (chunksOK_append (chunksOK_one c3282) (chunksOK_one c3283))) (chunksOK_append (chunksOK_append (chunksOK_one c3284) (chunksOK_one c3285)) (chunksOK_append (chunksOK_one c3286) (chunksOK_one c3287)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3288) (chunksOK_one c3289)) (chunksOK_append (chunksOK_one c3290) (chunksOK_one c3291))) (chunksOK_append (chunksOK_append (chunksOK_one c3292) (chunksOK_one c3293)) (chunksOK_append (chunksOK_one c3294) (chunksOK_one c3295)))))

end C205

namespace C206

theorem c3296 : check 60 115 18 3296 = true := by decide +kernel
theorem c3297 : check 60 115 18 3297 = true := by decide +kernel
theorem c3298 : check 60 115 18 3298 = true := by decide +kernel
theorem c3299 : check 60 115 18 3299 = true := by decide +kernel
theorem c3300 : check 60 115 18 3300 = true := by decide +kernel
theorem c3301 : check 60 115 18 3301 = true := by decide +kernel
theorem c3302 : check 60 115 18 3302 = true := by decide +kernel
theorem c3303 : check 60 115 18 3303 = true := by decide +kernel
theorem c3304 : check 60 115 18 3304 = true := by decide +kernel
theorem c3305 : check 60 115 18 3305 = true := by decide +kernel
theorem c3306 : check 60 115 18 3306 = true := by decide +kernel
theorem c3307 : check 60 115 18 3307 = true := by decide +kernel
theorem c3308 : check 60 115 18 3308 = true := by decide +kernel
theorem c3309 : check 60 115 18 3309 = true := by decide +kernel
theorem c3310 : check 60 115 18 3310 = true := by decide +kernel
theorem c3311 : check 60 115 18 3311 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3296 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3296) (chunksOK_one c3297)) (chunksOK_append (chunksOK_one c3298) (chunksOK_one c3299))) (chunksOK_append (chunksOK_append (chunksOK_one c3300) (chunksOK_one c3301)) (chunksOK_append (chunksOK_one c3302) (chunksOK_one c3303)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3304) (chunksOK_one c3305)) (chunksOK_append (chunksOK_one c3306) (chunksOK_one c3307))) (chunksOK_append (chunksOK_append (chunksOK_one c3308) (chunksOK_one c3309)) (chunksOK_append (chunksOK_one c3310) (chunksOK_one c3311)))))

end C206

namespace C207

theorem c3312 : check 60 115 18 3312 = true := by decide +kernel
theorem c3313 : check 60 115 18 3313 = true := by decide +kernel
theorem c3314 : check 60 115 18 3314 = true := by decide +kernel
theorem c3315 : check 60 115 18 3315 = true := by decide +kernel
theorem c3316 : check 60 115 18 3316 = true := by decide +kernel
theorem c3317 : check 60 115 18 3317 = true := by decide +kernel
theorem c3318 : check 60 115 18 3318 = true := by decide +kernel
theorem c3319 : check 60 115 18 3319 = true := by decide +kernel
theorem c3320 : check 60 115 18 3320 = true := by decide +kernel
theorem c3321 : check 60 115 18 3321 = true := by decide +kernel
theorem c3322 : check 60 115 18 3322 = true := by decide +kernel
theorem c3323 : check 60 115 18 3323 = true := by decide +kernel
theorem c3324 : check 60 115 18 3324 = true := by decide +kernel
theorem c3325 : check 60 115 18 3325 = true := by decide +kernel
theorem c3326 : check 60 115 18 3326 = true := by decide +kernel
theorem c3327 : check 60 115 18 3327 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3312 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3312) (chunksOK_one c3313)) (chunksOK_append (chunksOK_one c3314) (chunksOK_one c3315))) (chunksOK_append (chunksOK_append (chunksOK_one c3316) (chunksOK_one c3317)) (chunksOK_append (chunksOK_one c3318) (chunksOK_one c3319)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3320) (chunksOK_one c3321)) (chunksOK_append (chunksOK_one c3322) (chunksOK_one c3323))) (chunksOK_append (chunksOK_append (chunksOK_one c3324) (chunksOK_one c3325)) (chunksOK_append (chunksOK_one c3326) (chunksOK_one c3327)))))

end C207

namespace C208

theorem c3328 : check 60 115 18 3328 = true := by decide +kernel
theorem c3329 : check 60 115 18 3329 = true := by decide +kernel
theorem c3330 : check 60 115 18 3330 = true := by decide +kernel
theorem c3331 : check 60 115 18 3331 = true := by decide +kernel
theorem c3332 : check 60 115 18 3332 = true := by decide +kernel
theorem c3333 : check 60 115 18 3333 = true := by decide +kernel
theorem c3334 : check 60 115 18 3334 = true := by decide +kernel
theorem c3335 : check 60 115 18 3335 = true := by decide +kernel
theorem c3336 : check 60 115 18 3336 = true := by decide +kernel
theorem c3337 : check 60 115 18 3337 = true := by decide +kernel
theorem c3338 : check 60 115 18 3338 = true := by decide +kernel
theorem c3339 : check 60 115 18 3339 = true := by decide +kernel
theorem c3340 : check 60 115 18 3340 = true := by decide +kernel
theorem c3341 : check 60 115 18 3341 = true := by decide +kernel
theorem c3342 : check 60 115 18 3342 = true := by decide +kernel
theorem c3343 : check 60 115 18 3343 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3328 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3328) (chunksOK_one c3329)) (chunksOK_append (chunksOK_one c3330) (chunksOK_one c3331))) (chunksOK_append (chunksOK_append (chunksOK_one c3332) (chunksOK_one c3333)) (chunksOK_append (chunksOK_one c3334) (chunksOK_one c3335)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3336) (chunksOK_one c3337)) (chunksOK_append (chunksOK_one c3338) (chunksOK_one c3339))) (chunksOK_append (chunksOK_append (chunksOK_one c3340) (chunksOK_one c3341)) (chunksOK_append (chunksOK_one c3342) (chunksOK_one c3343)))))

end C208

namespace C209

theorem c3344 : check 60 115 18 3344 = true := by decide +kernel
theorem c3345 : check 60 115 18 3345 = true := by decide +kernel
theorem c3346 : check 60 115 18 3346 = true := by decide +kernel
theorem c3347 : check 60 115 18 3347 = true := by decide +kernel
theorem c3348 : check 60 115 18 3348 = true := by decide +kernel
theorem c3349 : check 60 115 18 3349 = true := by decide +kernel
theorem c3350 : check 60 115 18 3350 = true := by decide +kernel
theorem c3351 : check 60 115 18 3351 = true := by decide +kernel
theorem c3352 : check 60 115 18 3352 = true := by decide +kernel
theorem c3353 : check 60 115 18 3353 = true := by decide +kernel
theorem c3354 : check 60 115 18 3354 = true := by decide +kernel
theorem c3355 : check 60 115 18 3355 = true := by decide +kernel
theorem c3356 : check 60 115 18 3356 = true := by decide +kernel
theorem c3357 : check 60 115 18 3357 = true := by decide +kernel
theorem c3358 : check 60 115 18 3358 = true := by decide +kernel
theorem c3359 : check 60 115 18 3359 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3344 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3344) (chunksOK_one c3345)) (chunksOK_append (chunksOK_one c3346) (chunksOK_one c3347))) (chunksOK_append (chunksOK_append (chunksOK_one c3348) (chunksOK_one c3349)) (chunksOK_append (chunksOK_one c3350) (chunksOK_one c3351)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3352) (chunksOK_one c3353)) (chunksOK_append (chunksOK_one c3354) (chunksOK_one c3355))) (chunksOK_append (chunksOK_append (chunksOK_one c3356) (chunksOK_one c3357)) (chunksOK_append (chunksOK_one c3358) (chunksOK_one c3359)))))

end C209

namespace C210

theorem c3360 : check 60 115 18 3360 = true := by decide +kernel
theorem c3361 : check 60 115 18 3361 = true := by decide +kernel
theorem c3362 : check 60 115 18 3362 = true := by decide +kernel
theorem c3363 : check 60 115 18 3363 = true := by decide +kernel
theorem c3364 : check 60 115 18 3364 = true := by decide +kernel
theorem c3365 : check 60 115 18 3365 = true := by decide +kernel
theorem c3366 : check 60 115 18 3366 = true := by decide +kernel
theorem c3367 : check 60 115 18 3367 = true := by decide +kernel
theorem c3368 : check 60 115 18 3368 = true := by decide +kernel
theorem c3369 : check 60 115 18 3369 = true := by decide +kernel
theorem c3370 : check 60 115 18 3370 = true := by decide +kernel
theorem c3371 : check 60 115 18 3371 = true := by decide +kernel
theorem c3372 : check 60 115 18 3372 = true := by decide +kernel
theorem c3373 : check 60 115 18 3373 = true := by decide +kernel
theorem c3374 : check 60 115 18 3374 = true := by decide +kernel
theorem c3375 : check 60 115 18 3375 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3360 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3360) (chunksOK_one c3361)) (chunksOK_append (chunksOK_one c3362) (chunksOK_one c3363))) (chunksOK_append (chunksOK_append (chunksOK_one c3364) (chunksOK_one c3365)) (chunksOK_append (chunksOK_one c3366) (chunksOK_one c3367)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3368) (chunksOK_one c3369)) (chunksOK_append (chunksOK_one c3370) (chunksOK_one c3371))) (chunksOK_append (chunksOK_append (chunksOK_one c3372) (chunksOK_one c3373)) (chunksOK_append (chunksOK_one c3374) (chunksOK_one c3375)))))

end C210

namespace C211

theorem c3376 : check 60 115 18 3376 = true := by decide +kernel
theorem c3377 : check 60 115 18 3377 = true := by decide +kernel
theorem c3378 : check 60 115 18 3378 = true := by decide +kernel
theorem c3379 : check 60 115 18 3379 = true := by decide +kernel
theorem c3380 : check 60 115 18 3380 = true := by decide +kernel
theorem c3381 : check 60 115 18 3381 = true := by decide +kernel
theorem c3382 : check 60 115 18 3382 = true := by decide +kernel
theorem c3383 : check 60 115 18 3383 = true := by decide +kernel
theorem c3384 : check 60 115 18 3384 = true := by decide +kernel
theorem c3385 : check 60 115 18 3385 = true := by decide +kernel
theorem c3386 : check 60 115 18 3386 = true := by decide +kernel
theorem c3387 : check 60 115 18 3387 = true := by decide +kernel
theorem c3388 : check 60 115 18 3388 = true := by decide +kernel
theorem c3389 : check 60 115 18 3389 = true := by decide +kernel
theorem c3390 : check 60 115 18 3390 = true := by decide +kernel
theorem c3391 : check 60 115 18 3391 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3376 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3376) (chunksOK_one c3377)) (chunksOK_append (chunksOK_one c3378) (chunksOK_one c3379))) (chunksOK_append (chunksOK_append (chunksOK_one c3380) (chunksOK_one c3381)) (chunksOK_append (chunksOK_one c3382) (chunksOK_one c3383)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3384) (chunksOK_one c3385)) (chunksOK_append (chunksOK_one c3386) (chunksOK_one c3387))) (chunksOK_append (chunksOK_append (chunksOK_one c3388) (chunksOK_one c3389)) (chunksOK_append (chunksOK_one c3390) (chunksOK_one c3391)))))

end C211

namespace C212

theorem c3392 : check 60 115 18 3392 = true := by decide +kernel
theorem c3393 : check 60 115 18 3393 = true := by decide +kernel
theorem c3394 : check 60 115 18 3394 = true := by decide +kernel
theorem c3395 : check 60 115 18 3395 = true := by decide +kernel
theorem c3396 : check 60 115 18 3396 = true := by decide +kernel
theorem c3397 : check 60 115 18 3397 = true := by decide +kernel
theorem c3398 : check 60 115 18 3398 = true := by decide +kernel
theorem c3399 : check 60 115 18 3399 = true := by decide +kernel
theorem c3400 : check 60 115 18 3400 = true := by decide +kernel
theorem c3401 : check 60 115 18 3401 = true := by decide +kernel
theorem c3402 : check 60 115 18 3402 = true := by decide +kernel
theorem c3403 : check 60 115 18 3403 = true := by decide +kernel
theorem c3404 : check 60 115 18 3404 = true := by decide +kernel
theorem c3405 : check 60 115 18 3405 = true := by decide +kernel
theorem c3406 : check 60 115 18 3406 = true := by decide +kernel
theorem c3407 : check 60 115 18 3407 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3392 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3392) (chunksOK_one c3393)) (chunksOK_append (chunksOK_one c3394) (chunksOK_one c3395))) (chunksOK_append (chunksOK_append (chunksOK_one c3396) (chunksOK_one c3397)) (chunksOK_append (chunksOK_one c3398) (chunksOK_one c3399)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3400) (chunksOK_one c3401)) (chunksOK_append (chunksOK_one c3402) (chunksOK_one c3403))) (chunksOK_append (chunksOK_append (chunksOK_one c3404) (chunksOK_one c3405)) (chunksOK_append (chunksOK_one c3406) (chunksOK_one c3407)))))

end C212

namespace C213

theorem c3408 : check 60 115 18 3408 = true := by decide +kernel
theorem c3409 : check 60 115 18 3409 = true := by decide +kernel
theorem c3410 : check 60 115 18 3410 = true := by decide +kernel
theorem c3411 : check 60 115 18 3411 = true := by decide +kernel
theorem c3412 : check 60 115 18 3412 = true := by decide +kernel
theorem c3413 : check 60 115 18 3413 = true := by decide +kernel
theorem c3414 : check 60 115 18 3414 = true := by decide +kernel
theorem c3415 : check 60 115 18 3415 = true := by decide +kernel
theorem c3416 : check 60 115 18 3416 = true := by decide +kernel
theorem c3417 : check 60 115 18 3417 = true := by decide +kernel
theorem c3418 : check 60 115 18 3418 = true := by decide +kernel
theorem c3419 : check 60 115 18 3419 = true := by decide +kernel
theorem c3420 : check 60 115 18 3420 = true := by decide +kernel
theorem c3421 : check 60 115 18 3421 = true := by decide +kernel
theorem c3422 : check 60 115 18 3422 = true := by decide +kernel
theorem c3423 : check 60 115 18 3423 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3408 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3408) (chunksOK_one c3409)) (chunksOK_append (chunksOK_one c3410) (chunksOK_one c3411))) (chunksOK_append (chunksOK_append (chunksOK_one c3412) (chunksOK_one c3413)) (chunksOK_append (chunksOK_one c3414) (chunksOK_one c3415)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3416) (chunksOK_one c3417)) (chunksOK_append (chunksOK_one c3418) (chunksOK_one c3419))) (chunksOK_append (chunksOK_append (chunksOK_one c3420) (chunksOK_one c3421)) (chunksOK_append (chunksOK_one c3422) (chunksOK_one c3423)))))

end C213

namespace C214

theorem c3424 : check 60 115 18 3424 = true := by decide +kernel
theorem c3425 : check 60 115 18 3425 = true := by decide +kernel
theorem c3426 : check 60 115 18 3426 = true := by decide +kernel
theorem c3427 : check 60 115 18 3427 = true := by decide +kernel
theorem c3428 : check 60 115 18 3428 = true := by decide +kernel
theorem c3429 : check 60 115 18 3429 = true := by decide +kernel
theorem c3430 : check 60 115 18 3430 = true := by decide +kernel
theorem c3431 : check 60 115 18 3431 = true := by decide +kernel
theorem c3432 : check 60 115 18 3432 = true := by decide +kernel
theorem c3433 : check 60 115 18 3433 = true := by decide +kernel
theorem c3434 : check 60 115 18 3434 = true := by decide +kernel
theorem c3435 : check 60 115 18 3435 = true := by decide +kernel
theorem c3436 : check 60 115 18 3436 = true := by decide +kernel
theorem c3437 : check 60 115 18 3437 = true := by decide +kernel
theorem c3438 : check 60 115 18 3438 = true := by decide +kernel
theorem c3439 : check 60 115 18 3439 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3424 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3424) (chunksOK_one c3425)) (chunksOK_append (chunksOK_one c3426) (chunksOK_one c3427))) (chunksOK_append (chunksOK_append (chunksOK_one c3428) (chunksOK_one c3429)) (chunksOK_append (chunksOK_one c3430) (chunksOK_one c3431)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3432) (chunksOK_one c3433)) (chunksOK_append (chunksOK_one c3434) (chunksOK_one c3435))) (chunksOK_append (chunksOK_append (chunksOK_one c3436) (chunksOK_one c3437)) (chunksOK_append (chunksOK_one c3438) (chunksOK_one c3439)))))

end C214

namespace C215

theorem c3440 : check 60 115 18 3440 = true := by decide +kernel
theorem c3441 : check 60 115 18 3441 = true := by decide +kernel
theorem c3442 : check 60 115 18 3442 = true := by decide +kernel
theorem c3443 : check 60 115 18 3443 = true := by decide +kernel
theorem c3444 : check 60 115 18 3444 = true := by decide +kernel
theorem c3445 : check 60 115 18 3445 = true := by decide +kernel
theorem c3446 : check 60 115 18 3446 = true := by decide +kernel
theorem c3447 : check 60 115 18 3447 = true := by decide +kernel
theorem c3448 : check 60 115 18 3448 = true := by decide +kernel
theorem c3449 : check 60 115 18 3449 = true := by decide +kernel
theorem c3450 : check 60 115 18 3450 = true := by decide +kernel
theorem c3451 : check 60 115 18 3451 = true := by decide +kernel
theorem c3452 : check 60 115 18 3452 = true := by decide +kernel
theorem c3453 : check 60 115 18 3453 = true := by decide +kernel
theorem c3454 : check 60 115 18 3454 = true := by decide +kernel
theorem c3455 : check 60 115 18 3455 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3440 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3440) (chunksOK_one c3441)) (chunksOK_append (chunksOK_one c3442) (chunksOK_one c3443))) (chunksOK_append (chunksOK_append (chunksOK_one c3444) (chunksOK_one c3445)) (chunksOK_append (chunksOK_one c3446) (chunksOK_one c3447)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3448) (chunksOK_one c3449)) (chunksOK_append (chunksOK_one c3450) (chunksOK_one c3451))) (chunksOK_append (chunksOK_append (chunksOK_one c3452) (chunksOK_one c3453)) (chunksOK_append (chunksOK_one c3454) (chunksOK_one c3455)))))

end C215

namespace C216

theorem c3456 : check 60 115 18 3456 = true := by decide +kernel
theorem c3457 : check 60 115 18 3457 = true := by decide +kernel
theorem c3458 : check 60 115 18 3458 = true := by decide +kernel
theorem c3459 : check 60 115 18 3459 = true := by decide +kernel
theorem c3460 : check 60 115 18 3460 = true := by decide +kernel
theorem c3461 : check 60 115 18 3461 = true := by decide +kernel
theorem c3462 : check 60 115 18 3462 = true := by decide +kernel
theorem c3463 : check 60 115 18 3463 = true := by decide +kernel
theorem c3464 : check 60 115 18 3464 = true := by decide +kernel
theorem c3465 : check 60 115 18 3465 = true := by decide +kernel
theorem c3466 : check 60 115 18 3466 = true := by decide +kernel
theorem c3467 : check 60 115 18 3467 = true := by decide +kernel
theorem c3468 : check 60 115 18 3468 = true := by decide +kernel
theorem c3469 : check 60 115 18 3469 = true := by decide +kernel
theorem c3470 : check 60 115 18 3470 = true := by decide +kernel
theorem c3471 : check 60 115 18 3471 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3456 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3456) (chunksOK_one c3457)) (chunksOK_append (chunksOK_one c3458) (chunksOK_one c3459))) (chunksOK_append (chunksOK_append (chunksOK_one c3460) (chunksOK_one c3461)) (chunksOK_append (chunksOK_one c3462) (chunksOK_one c3463)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3464) (chunksOK_one c3465)) (chunksOK_append (chunksOK_one c3466) (chunksOK_one c3467))) (chunksOK_append (chunksOK_append (chunksOK_one c3468) (chunksOK_one c3469)) (chunksOK_append (chunksOK_one c3470) (chunksOK_one c3471)))))

end C216

namespace C217

theorem c3472 : check 60 115 18 3472 = true := by decide +kernel
theorem c3473 : check 60 115 18 3473 = true := by decide +kernel
theorem c3474 : check 60 115 18 3474 = true := by decide +kernel
theorem c3475 : check 60 115 18 3475 = true := by decide +kernel
theorem c3476 : check 60 115 18 3476 = true := by decide +kernel
theorem c3477 : check 60 115 18 3477 = true := by decide +kernel
theorem c3478 : check 60 115 18 3478 = true := by decide +kernel
theorem c3479 : check 60 115 18 3479 = true := by decide +kernel
theorem c3480 : check 60 115 18 3480 = true := by decide +kernel
theorem c3481 : check 60 115 18 3481 = true := by decide +kernel
theorem c3482 : check 60 115 18 3482 = true := by decide +kernel
theorem c3483 : check 60 115 18 3483 = true := by decide +kernel
theorem c3484 : check 60 115 18 3484 = true := by decide +kernel
theorem c3485 : check 60 115 18 3485 = true := by decide +kernel
theorem c3486 : check 60 115 18 3486 = true := by decide +kernel
theorem c3487 : check 60 115 18 3487 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3472 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3472) (chunksOK_one c3473)) (chunksOK_append (chunksOK_one c3474) (chunksOK_one c3475))) (chunksOK_append (chunksOK_append (chunksOK_one c3476) (chunksOK_one c3477)) (chunksOK_append (chunksOK_one c3478) (chunksOK_one c3479)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3480) (chunksOK_one c3481)) (chunksOK_append (chunksOK_one c3482) (chunksOK_one c3483))) (chunksOK_append (chunksOK_append (chunksOK_one c3484) (chunksOK_one c3485)) (chunksOK_append (chunksOK_one c3486) (chunksOK_one c3487)))))

end C217

namespace C218

theorem c3488 : check 60 115 18 3488 = true := by decide +kernel
theorem c3489 : check 60 115 18 3489 = true := by decide +kernel
theorem c3490 : check 60 115 18 3490 = true := by decide +kernel
theorem c3491 : check 60 115 18 3491 = true := by decide +kernel
theorem c3492 : check 60 115 18 3492 = true := by decide +kernel
theorem c3493 : check 60 115 18 3493 = true := by decide +kernel
theorem c3494 : check 60 115 18 3494 = true := by decide +kernel
theorem c3495 : check 60 115 18 3495 = true := by decide +kernel
theorem c3496 : check 60 115 18 3496 = true := by decide +kernel
theorem c3497 : check 60 115 18 3497 = true := by decide +kernel
theorem c3498 : check 60 115 18 3498 = true := by decide +kernel
theorem c3499 : check 60 115 18 3499 = true := by decide +kernel
theorem c3500 : check 60 115 18 3500 = true := by decide +kernel
theorem c3501 : check 60 115 18 3501 = true := by decide +kernel
theorem c3502 : check 60 115 18 3502 = true := by decide +kernel
theorem c3503 : check 60 115 18 3503 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3488 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3488) (chunksOK_one c3489)) (chunksOK_append (chunksOK_one c3490) (chunksOK_one c3491))) (chunksOK_append (chunksOK_append (chunksOK_one c3492) (chunksOK_one c3493)) (chunksOK_append (chunksOK_one c3494) (chunksOK_one c3495)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3496) (chunksOK_one c3497)) (chunksOK_append (chunksOK_one c3498) (chunksOK_one c3499))) (chunksOK_append (chunksOK_append (chunksOK_one c3500) (chunksOK_one c3501)) (chunksOK_append (chunksOK_one c3502) (chunksOK_one c3503)))))

end C218

namespace C219

theorem c3504 : check 60 115 18 3504 = true := by decide +kernel
theorem c3505 : check 60 115 18 3505 = true := by decide +kernel
theorem c3506 : check 60 115 18 3506 = true := by decide +kernel
theorem c3507 : check 60 115 18 3507 = true := by decide +kernel
theorem c3508 : check 60 115 18 3508 = true := by decide +kernel
theorem c3509 : check 60 115 18 3509 = true := by decide +kernel
theorem c3510 : check 60 115 18 3510 = true := by decide +kernel
theorem c3511 : check 60 115 18 3511 = true := by decide +kernel
theorem c3512 : check 60 115 18 3512 = true := by decide +kernel
theorem c3513 : check 60 115 18 3513 = true := by decide +kernel
theorem c3514 : check 60 115 18 3514 = true := by decide +kernel
theorem c3515 : check 60 115 18 3515 = true := by decide +kernel
theorem c3516 : check 60 115 18 3516 = true := by decide +kernel
theorem c3517 : check 60 115 18 3517 = true := by decide +kernel
theorem c3518 : check 60 115 18 3518 = true := by decide +kernel
theorem c3519 : check 60 115 18 3519 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3504 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3504) (chunksOK_one c3505)) (chunksOK_append (chunksOK_one c3506) (chunksOK_one c3507))) (chunksOK_append (chunksOK_append (chunksOK_one c3508) (chunksOK_one c3509)) (chunksOK_append (chunksOK_one c3510) (chunksOK_one c3511)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3512) (chunksOK_one c3513)) (chunksOK_append (chunksOK_one c3514) (chunksOK_one c3515))) (chunksOK_append (chunksOK_append (chunksOK_one c3516) (chunksOK_one c3517)) (chunksOK_append (chunksOK_one c3518) (chunksOK_one c3519)))))

end C219

namespace C220

theorem c3520 : check 60 115 18 3520 = true := by decide +kernel
theorem c3521 : check 60 115 18 3521 = true := by decide +kernel
theorem c3522 : check 60 115 18 3522 = true := by decide +kernel
theorem c3523 : check 60 115 18 3523 = true := by decide +kernel
theorem c3524 : check 60 115 18 3524 = true := by decide +kernel
theorem c3525 : check 60 115 18 3525 = true := by decide +kernel
theorem c3526 : check 60 115 18 3526 = true := by decide +kernel
theorem c3527 : check 60 115 18 3527 = true := by decide +kernel
theorem c3528 : check 60 115 18 3528 = true := by decide +kernel
theorem c3529 : check 60 115 18 3529 = true := by decide +kernel
theorem c3530 : check 60 115 18 3530 = true := by decide +kernel
theorem c3531 : check 60 115 18 3531 = true := by decide +kernel
theorem c3532 : check 60 115 18 3532 = true := by decide +kernel
theorem c3533 : check 60 115 18 3533 = true := by decide +kernel
theorem c3534 : check 60 115 18 3534 = true := by decide +kernel
theorem c3535 : check 60 115 18 3535 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3520 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3520) (chunksOK_one c3521)) (chunksOK_append (chunksOK_one c3522) (chunksOK_one c3523))) (chunksOK_append (chunksOK_append (chunksOK_one c3524) (chunksOK_one c3525)) (chunksOK_append (chunksOK_one c3526) (chunksOK_one c3527)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3528) (chunksOK_one c3529)) (chunksOK_append (chunksOK_one c3530) (chunksOK_one c3531))) (chunksOK_append (chunksOK_append (chunksOK_one c3532) (chunksOK_one c3533)) (chunksOK_append (chunksOK_one c3534) (chunksOK_one c3535)))))

end C220

namespace C221

theorem c3536 : check 60 115 18 3536 = true := by decide +kernel
theorem c3537 : check 60 115 18 3537 = true := by decide +kernel
theorem c3538 : check 60 115 18 3538 = true := by decide +kernel
theorem c3539 : check 60 115 18 3539 = true := by decide +kernel
theorem c3540 : check 60 115 18 3540 = true := by decide +kernel
theorem c3541 : check 60 115 18 3541 = true := by decide +kernel
theorem c3542 : check 60 115 18 3542 = true := by decide +kernel
theorem c3543 : check 60 115 18 3543 = true := by decide +kernel
theorem c3544 : check 60 115 18 3544 = true := by decide +kernel
theorem c3545 : check 60 115 18 3545 = true := by decide +kernel
theorem c3546 : check 60 115 18 3546 = true := by decide +kernel
theorem c3547 : check 60 115 18 3547 = true := by decide +kernel
theorem c3548 : check 60 115 18 3548 = true := by decide +kernel
theorem c3549 : check 60 115 18 3549 = true := by decide +kernel
theorem c3550 : check 60 115 18 3550 = true := by decide +kernel
theorem c3551 : check 60 115 18 3551 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3536 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3536) (chunksOK_one c3537)) (chunksOK_append (chunksOK_one c3538) (chunksOK_one c3539))) (chunksOK_append (chunksOK_append (chunksOK_one c3540) (chunksOK_one c3541)) (chunksOK_append (chunksOK_one c3542) (chunksOK_one c3543)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3544) (chunksOK_one c3545)) (chunksOK_append (chunksOK_one c3546) (chunksOK_one c3547))) (chunksOK_append (chunksOK_append (chunksOK_one c3548) (chunksOK_one c3549)) (chunksOK_append (chunksOK_one c3550) (chunksOK_one c3551)))))

end C221

namespace C222

theorem c3552 : check 60 115 18 3552 = true := by decide +kernel
theorem c3553 : check 60 115 18 3553 = true := by decide +kernel
theorem c3554 : check 60 115 18 3554 = true := by decide +kernel
theorem c3555 : check 60 115 18 3555 = true := by decide +kernel
theorem c3556 : check 60 115 18 3556 = true := by decide +kernel
theorem c3557 : check 60 115 18 3557 = true := by decide +kernel
theorem c3558 : check 60 115 18 3558 = true := by decide +kernel
theorem c3559 : check 60 115 18 3559 = true := by decide +kernel
theorem c3560 : check 60 115 18 3560 = true := by decide +kernel
theorem c3561 : check 60 115 18 3561 = true := by decide +kernel
theorem c3562 : check 60 115 18 3562 = true := by decide +kernel
theorem c3563 : check 60 115 18 3563 = true := by decide +kernel
theorem c3564 : check 60 115 18 3564 = true := by decide +kernel
theorem c3565 : check 60 115 18 3565 = true := by decide +kernel
theorem c3566 : check 60 115 18 3566 = true := by decide +kernel
theorem c3567 : check 60 115 18 3567 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3552 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3552) (chunksOK_one c3553)) (chunksOK_append (chunksOK_one c3554) (chunksOK_one c3555))) (chunksOK_append (chunksOK_append (chunksOK_one c3556) (chunksOK_one c3557)) (chunksOK_append (chunksOK_one c3558) (chunksOK_one c3559)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3560) (chunksOK_one c3561)) (chunksOK_append (chunksOK_one c3562) (chunksOK_one c3563))) (chunksOK_append (chunksOK_append (chunksOK_one c3564) (chunksOK_one c3565)) (chunksOK_append (chunksOK_one c3566) (chunksOK_one c3567)))))

end C222

namespace C223

theorem c3568 : check 60 115 18 3568 = true := by decide +kernel
theorem c3569 : check 60 115 18 3569 = true := by decide +kernel
theorem c3570 : check 60 115 18 3570 = true := by decide +kernel
theorem c3571 : check 60 115 18 3571 = true := by decide +kernel
theorem c3572 : check 60 115 18 3572 = true := by decide +kernel
theorem c3573 : check 60 115 18 3573 = true := by decide +kernel
theorem c3574 : check 60 115 18 3574 = true := by decide +kernel
theorem c3575 : check 60 115 18 3575 = true := by decide +kernel
theorem c3576 : check 60 115 18 3576 = true := by decide +kernel
theorem c3577 : check 60 115 18 3577 = true := by decide +kernel
theorem c3578 : check 60 115 18 3578 = true := by decide +kernel
theorem c3579 : check 60 115 18 3579 = true := by decide +kernel
theorem c3580 : check 60 115 18 3580 = true := by decide +kernel
theorem c3581 : check 60 115 18 3581 = true := by decide +kernel
theorem c3582 : check 60 115 18 3582 = true := by decide +kernel
theorem c3583 : check 60 115 18 3583 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3568 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3568) (chunksOK_one c3569)) (chunksOK_append (chunksOK_one c3570) (chunksOK_one c3571))) (chunksOK_append (chunksOK_append (chunksOK_one c3572) (chunksOK_one c3573)) (chunksOK_append (chunksOK_one c3574) (chunksOK_one c3575)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3576) (chunksOK_one c3577)) (chunksOK_append (chunksOK_one c3578) (chunksOK_one c3579))) (chunksOK_append (chunksOK_append (chunksOK_one c3580) (chunksOK_one c3581)) (chunksOK_append (chunksOK_one c3582) (chunksOK_one c3583)))))

end C223

namespace C224

theorem c3584 : check 60 115 18 3584 = true := by decide +kernel
theorem c3585 : check 60 115 18 3585 = true := by decide +kernel
theorem c3586 : check 60 115 18 3586 = true := by decide +kernel
theorem c3587 : check 60 115 18 3587 = true := by decide +kernel
theorem c3588 : check 60 115 18 3588 = true := by decide +kernel
theorem c3589 : check 60 115 18 3589 = true := by decide +kernel
theorem c3590 : check 60 115 18 3590 = true := by decide +kernel
theorem c3591 : check 60 115 18 3591 = true := by decide +kernel
theorem c3592 : check 60 115 18 3592 = true := by decide +kernel
theorem c3593 : check 60 115 18 3593 = true := by decide +kernel
theorem c3594 : check 60 115 18 3594 = true := by decide +kernel
theorem c3595 : check 60 115 18 3595 = true := by decide +kernel
theorem c3596 : check 60 115 18 3596 = true := by decide +kernel
theorem c3597 : check 60 115 18 3597 = true := by decide +kernel
theorem c3598 : check 60 115 18 3598 = true := by decide +kernel
theorem c3599 : check 60 115 18 3599 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3584 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3584) (chunksOK_one c3585)) (chunksOK_append (chunksOK_one c3586) (chunksOK_one c3587))) (chunksOK_append (chunksOK_append (chunksOK_one c3588) (chunksOK_one c3589)) (chunksOK_append (chunksOK_one c3590) (chunksOK_one c3591)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3592) (chunksOK_one c3593)) (chunksOK_append (chunksOK_one c3594) (chunksOK_one c3595))) (chunksOK_append (chunksOK_append (chunksOK_one c3596) (chunksOK_one c3597)) (chunksOK_append (chunksOK_one c3598) (chunksOK_one c3599)))))

end C224

namespace C225

theorem c3600 : check 60 115 18 3600 = true := by decide +kernel
theorem c3601 : check 60 115 18 3601 = true := by decide +kernel
theorem c3602 : check 60 115 18 3602 = true := by decide +kernel
theorem c3603 : check 60 115 18 3603 = true := by decide +kernel
theorem c3604 : check 60 115 18 3604 = true := by decide +kernel
theorem c3605 : check 60 115 18 3605 = true := by decide +kernel
theorem c3606 : check 60 115 18 3606 = true := by decide +kernel
theorem c3607 : check 60 115 18 3607 = true := by decide +kernel
theorem c3608 : check 60 115 18 3608 = true := by decide +kernel
theorem c3609 : check 60 115 18 3609 = true := by decide +kernel
theorem c3610 : check 60 115 18 3610 = true := by decide +kernel
theorem c3611 : check 60 115 18 3611 = true := by decide +kernel
theorem c3612 : check 60 115 18 3612 = true := by decide +kernel
theorem c3613 : check 60 115 18 3613 = true := by decide +kernel
theorem c3614 : check 60 115 18 3614 = true := by decide +kernel
theorem c3615 : check 60 115 18 3615 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3600 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3600) (chunksOK_one c3601)) (chunksOK_append (chunksOK_one c3602) (chunksOK_one c3603))) (chunksOK_append (chunksOK_append (chunksOK_one c3604) (chunksOK_one c3605)) (chunksOK_append (chunksOK_one c3606) (chunksOK_one c3607)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3608) (chunksOK_one c3609)) (chunksOK_append (chunksOK_one c3610) (chunksOK_one c3611))) (chunksOK_append (chunksOK_append (chunksOK_one c3612) (chunksOK_one c3613)) (chunksOK_append (chunksOK_one c3614) (chunksOK_one c3615)))))

end C225

namespace C226

theorem c3616 : check 60 115 18 3616 = true := by decide +kernel
theorem c3617 : check 60 115 18 3617 = true := by decide +kernel
theorem c3618 : check 60 115 18 3618 = true := by decide +kernel
theorem c3619 : check 60 115 18 3619 = true := by decide +kernel
theorem c3620 : check 60 115 18 3620 = true := by decide +kernel
theorem c3621 : check 60 115 18 3621 = true := by decide +kernel
theorem c3622 : check 60 115 18 3622 = true := by decide +kernel
theorem c3623 : check 60 115 18 3623 = true := by decide +kernel
theorem c3624 : check 60 115 18 3624 = true := by decide +kernel
theorem c3625 : check 60 115 18 3625 = true := by decide +kernel
theorem c3626 : check 60 115 18 3626 = true := by decide +kernel
theorem c3627 : check 60 115 18 3627 = true := by decide +kernel
theorem c3628 : check 60 115 18 3628 = true := by decide +kernel
theorem c3629 : check 60 115 18 3629 = true := by decide +kernel
theorem c3630 : check 60 115 18 3630 = true := by decide +kernel
theorem c3631 : check 60 115 18 3631 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3616 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3616) (chunksOK_one c3617)) (chunksOK_append (chunksOK_one c3618) (chunksOK_one c3619))) (chunksOK_append (chunksOK_append (chunksOK_one c3620) (chunksOK_one c3621)) (chunksOK_append (chunksOK_one c3622) (chunksOK_one c3623)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3624) (chunksOK_one c3625)) (chunksOK_append (chunksOK_one c3626) (chunksOK_one c3627))) (chunksOK_append (chunksOK_append (chunksOK_one c3628) (chunksOK_one c3629)) (chunksOK_append (chunksOK_one c3630) (chunksOK_one c3631)))))

end C226

namespace C227

theorem c3632 : check 60 115 18 3632 = true := by decide +kernel
theorem c3633 : check 60 115 18 3633 = true := by decide +kernel
theorem c3634 : check 60 115 18 3634 = true := by decide +kernel
theorem c3635 : check 60 115 18 3635 = true := by decide +kernel
theorem c3636 : check 60 115 18 3636 = true := by decide +kernel
theorem c3637 : check 60 115 18 3637 = true := by decide +kernel
theorem c3638 : check 60 115 18 3638 = true := by decide +kernel
theorem c3639 : check 60 115 18 3639 = true := by decide +kernel
theorem c3640 : check 60 115 18 3640 = true := by decide +kernel
theorem c3641 : check 60 115 18 3641 = true := by decide +kernel
theorem c3642 : check 60 115 18 3642 = true := by decide +kernel
theorem c3643 : check 60 115 18 3643 = true := by decide +kernel
theorem c3644 : check 60 115 18 3644 = true := by decide +kernel
theorem c3645 : check 60 115 18 3645 = true := by decide +kernel
theorem c3646 : check 60 115 18 3646 = true := by decide +kernel
theorem c3647 : check 60 115 18 3647 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3632 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3632) (chunksOK_one c3633)) (chunksOK_append (chunksOK_one c3634) (chunksOK_one c3635))) (chunksOK_append (chunksOK_append (chunksOK_one c3636) (chunksOK_one c3637)) (chunksOK_append (chunksOK_one c3638) (chunksOK_one c3639)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3640) (chunksOK_one c3641)) (chunksOK_append (chunksOK_one c3642) (chunksOK_one c3643))) (chunksOK_append (chunksOK_append (chunksOK_one c3644) (chunksOK_one c3645)) (chunksOK_append (chunksOK_one c3646) (chunksOK_one c3647)))))

end C227

namespace C228

theorem c3648 : check 60 115 18 3648 = true := by decide +kernel
theorem c3649 : check 60 115 18 3649 = true := by decide +kernel
theorem c3650 : check 60 115 18 3650 = true := by decide +kernel
theorem c3651 : check 60 115 18 3651 = true := by decide +kernel
theorem c3652 : check 60 115 18 3652 = true := by decide +kernel
theorem c3653 : check 60 115 18 3653 = true := by decide +kernel
theorem c3654 : check 60 115 18 3654 = true := by decide +kernel
theorem c3655 : check 60 115 18 3655 = true := by decide +kernel
theorem c3656 : check 60 115 18 3656 = true := by decide +kernel
theorem c3657 : check 60 115 18 3657 = true := by decide +kernel
theorem c3658 : check 60 115 18 3658 = true := by decide +kernel
theorem c3659 : check 60 115 18 3659 = true := by decide +kernel
theorem c3660 : check 60 115 18 3660 = true := by decide +kernel
theorem c3661 : check 60 115 18 3661 = true := by decide +kernel
theorem c3662 : check 60 115 18 3662 = true := by decide +kernel
theorem c3663 : check 60 115 18 3663 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3648 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3648) (chunksOK_one c3649)) (chunksOK_append (chunksOK_one c3650) (chunksOK_one c3651))) (chunksOK_append (chunksOK_append (chunksOK_one c3652) (chunksOK_one c3653)) (chunksOK_append (chunksOK_one c3654) (chunksOK_one c3655)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3656) (chunksOK_one c3657)) (chunksOK_append (chunksOK_one c3658) (chunksOK_one c3659))) (chunksOK_append (chunksOK_append (chunksOK_one c3660) (chunksOK_one c3661)) (chunksOK_append (chunksOK_one c3662) (chunksOK_one c3663)))))

end C228

namespace C229

theorem c3664 : check 60 115 18 3664 = true := by decide +kernel
theorem c3665 : check 60 115 18 3665 = true := by decide +kernel
theorem c3666 : check 60 115 18 3666 = true := by decide +kernel
theorem c3667 : check 60 115 18 3667 = true := by decide +kernel
theorem c3668 : check 60 115 18 3668 = true := by decide +kernel
theorem c3669 : check 60 115 18 3669 = true := by decide +kernel
theorem c3670 : check 60 115 18 3670 = true := by decide +kernel
theorem c3671 : check 60 115 18 3671 = true := by decide +kernel
theorem c3672 : check 60 115 18 3672 = true := by decide +kernel
theorem c3673 : check 60 115 18 3673 = true := by decide +kernel
theorem c3674 : check 60 115 18 3674 = true := by decide +kernel
theorem c3675 : check 60 115 18 3675 = true := by decide +kernel
theorem c3676 : check 60 115 18 3676 = true := by decide +kernel
theorem c3677 : check 60 115 18 3677 = true := by decide +kernel
theorem c3678 : check 60 115 18 3678 = true := by decide +kernel
theorem c3679 : check 60 115 18 3679 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3664 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3664) (chunksOK_one c3665)) (chunksOK_append (chunksOK_one c3666) (chunksOK_one c3667))) (chunksOK_append (chunksOK_append (chunksOK_one c3668) (chunksOK_one c3669)) (chunksOK_append (chunksOK_one c3670) (chunksOK_one c3671)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3672) (chunksOK_one c3673)) (chunksOK_append (chunksOK_one c3674) (chunksOK_one c3675))) (chunksOK_append (chunksOK_append (chunksOK_one c3676) (chunksOK_one c3677)) (chunksOK_append (chunksOK_one c3678) (chunksOK_one c3679)))))

end C229

namespace C230

theorem c3680 : check 60 115 18 3680 = true := by decide +kernel
theorem c3681 : check 60 115 18 3681 = true := by decide +kernel
theorem c3682 : check 60 115 18 3682 = true := by decide +kernel
theorem c3683 : check 60 115 18 3683 = true := by decide +kernel
theorem c3684 : check 60 115 18 3684 = true := by decide +kernel
theorem c3685 : check 60 115 18 3685 = true := by decide +kernel
theorem c3686 : check 60 115 18 3686 = true := by decide +kernel
theorem c3687 : check 60 115 18 3687 = true := by decide +kernel
theorem c3688 : check 60 115 18 3688 = true := by decide +kernel
theorem c3689 : check 60 115 18 3689 = true := by decide +kernel
theorem c3690 : check 60 115 18 3690 = true := by decide +kernel
theorem c3691 : check 60 115 18 3691 = true := by decide +kernel
theorem c3692 : check 60 115 18 3692 = true := by decide +kernel
theorem c3693 : check 60 115 18 3693 = true := by decide +kernel
theorem c3694 : check 60 115 18 3694 = true := by decide +kernel
theorem c3695 : check 60 115 18 3695 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3680 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3680) (chunksOK_one c3681)) (chunksOK_append (chunksOK_one c3682) (chunksOK_one c3683))) (chunksOK_append (chunksOK_append (chunksOK_one c3684) (chunksOK_one c3685)) (chunksOK_append (chunksOK_one c3686) (chunksOK_one c3687)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3688) (chunksOK_one c3689)) (chunksOK_append (chunksOK_one c3690) (chunksOK_one c3691))) (chunksOK_append (chunksOK_append (chunksOK_one c3692) (chunksOK_one c3693)) (chunksOK_append (chunksOK_one c3694) (chunksOK_one c3695)))))

end C230

namespace C231

theorem c3696 : check 60 115 18 3696 = true := by decide +kernel
theorem c3697 : check 60 115 18 3697 = true := by decide +kernel
theorem c3698 : check 60 115 18 3698 = true := by decide +kernel
theorem c3699 : check 60 115 18 3699 = true := by decide +kernel
theorem c3700 : check 60 115 18 3700 = true := by decide +kernel
theorem c3701 : check 60 115 18 3701 = true := by decide +kernel
theorem c3702 : check 60 115 18 3702 = true := by decide +kernel
theorem c3703 : check 60 115 18 3703 = true := by decide +kernel
theorem c3704 : check 60 115 18 3704 = true := by decide +kernel
theorem c3705 : check 60 115 18 3705 = true := by decide +kernel
theorem c3706 : check 60 115 18 3706 = true := by decide +kernel
theorem c3707 : check 60 115 18 3707 = true := by decide +kernel
theorem c3708 : check 60 115 18 3708 = true := by decide +kernel
theorem c3709 : check 60 115 18 3709 = true := by decide +kernel
theorem c3710 : check 60 115 18 3710 = true := by decide +kernel
theorem c3711 : check 60 115 18 3711 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3696 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3696) (chunksOK_one c3697)) (chunksOK_append (chunksOK_one c3698) (chunksOK_one c3699))) (chunksOK_append (chunksOK_append (chunksOK_one c3700) (chunksOK_one c3701)) (chunksOK_append (chunksOK_one c3702) (chunksOK_one c3703)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3704) (chunksOK_one c3705)) (chunksOK_append (chunksOK_one c3706) (chunksOK_one c3707))) (chunksOK_append (chunksOK_append (chunksOK_one c3708) (chunksOK_one c3709)) (chunksOK_append (chunksOK_one c3710) (chunksOK_one c3711)))))

end C231

namespace C232

theorem c3712 : check 60 115 18 3712 = true := by decide +kernel
theorem c3713 : check 60 115 18 3713 = true := by decide +kernel
theorem c3714 : check 60 115 18 3714 = true := by decide +kernel
theorem c3715 : check 60 115 18 3715 = true := by decide +kernel
theorem c3716 : check 60 115 18 3716 = true := by decide +kernel
theorem c3717 : check 60 115 18 3717 = true := by decide +kernel
theorem c3718 : check 60 115 18 3718 = true := by decide +kernel
theorem c3719 : check 60 115 18 3719 = true := by decide +kernel
theorem c3720 : check 60 115 18 3720 = true := by decide +kernel
theorem c3721 : check 60 115 18 3721 = true := by decide +kernel
theorem c3722 : check 60 115 18 3722 = true := by decide +kernel
theorem c3723 : check 60 115 18 3723 = true := by decide +kernel
theorem c3724 : check 60 115 18 3724 = true := by decide +kernel
theorem c3725 : check 60 115 18 3725 = true := by decide +kernel
theorem c3726 : check 60 115 18 3726 = true := by decide +kernel
theorem c3727 : check 60 115 18 3727 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3712 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3712) (chunksOK_one c3713)) (chunksOK_append (chunksOK_one c3714) (chunksOK_one c3715))) (chunksOK_append (chunksOK_append (chunksOK_one c3716) (chunksOK_one c3717)) (chunksOK_append (chunksOK_one c3718) (chunksOK_one c3719)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3720) (chunksOK_one c3721)) (chunksOK_append (chunksOK_one c3722) (chunksOK_one c3723))) (chunksOK_append (chunksOK_append (chunksOK_one c3724) (chunksOK_one c3725)) (chunksOK_append (chunksOK_one c3726) (chunksOK_one c3727)))))

end C232

namespace C233

theorem c3728 : check 60 115 18 3728 = true := by decide +kernel
theorem c3729 : check 60 115 18 3729 = true := by decide +kernel
theorem c3730 : check 60 115 18 3730 = true := by decide +kernel
theorem c3731 : check 60 115 18 3731 = true := by decide +kernel
theorem c3732 : check 60 115 18 3732 = true := by decide +kernel
theorem c3733 : check 60 115 18 3733 = true := by decide +kernel
theorem c3734 : check 60 115 18 3734 = true := by decide +kernel
theorem c3735 : check 60 115 18 3735 = true := by decide +kernel
theorem c3736 : check 60 115 18 3736 = true := by decide +kernel
theorem c3737 : check 60 115 18 3737 = true := by decide +kernel
theorem c3738 : check 60 115 18 3738 = true := by decide +kernel
theorem c3739 : check 60 115 18 3739 = true := by decide +kernel
theorem c3740 : check 60 115 18 3740 = true := by decide +kernel
theorem c3741 : check 60 115 18 3741 = true := by decide +kernel
theorem c3742 : check 60 115 18 3742 = true := by decide +kernel
theorem c3743 : check 60 115 18 3743 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3728 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3728) (chunksOK_one c3729)) (chunksOK_append (chunksOK_one c3730) (chunksOK_one c3731))) (chunksOK_append (chunksOK_append (chunksOK_one c3732) (chunksOK_one c3733)) (chunksOK_append (chunksOK_one c3734) (chunksOK_one c3735)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3736) (chunksOK_one c3737)) (chunksOK_append (chunksOK_one c3738) (chunksOK_one c3739))) (chunksOK_append (chunksOK_append (chunksOK_one c3740) (chunksOK_one c3741)) (chunksOK_append (chunksOK_one c3742) (chunksOK_one c3743)))))

end C233

namespace C234

theorem c3744 : check 60 115 18 3744 = true := by decide +kernel
theorem c3745 : check 60 115 18 3745 = true := by decide +kernel
theorem c3746 : check 60 115 18 3746 = true := by decide +kernel
theorem c3747 : check 60 115 18 3747 = true := by decide +kernel
theorem c3748 : check 60 115 18 3748 = true := by decide +kernel
theorem c3749 : check 60 115 18 3749 = true := by decide +kernel
theorem c3750 : check 60 115 18 3750 = true := by decide +kernel
theorem c3751 : check 60 115 18 3751 = true := by decide +kernel
theorem c3752 : check 60 115 18 3752 = true := by decide +kernel
theorem c3753 : check 60 115 18 3753 = true := by decide +kernel
theorem c3754 : check 60 115 18 3754 = true := by decide +kernel
theorem c3755 : check 60 115 18 3755 = true := by decide +kernel
theorem c3756 : check 60 115 18 3756 = true := by decide +kernel
theorem c3757 : check 60 115 18 3757 = true := by decide +kernel
theorem c3758 : check 60 115 18 3758 = true := by decide +kernel
theorem c3759 : check 60 115 18 3759 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3744 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3744) (chunksOK_one c3745)) (chunksOK_append (chunksOK_one c3746) (chunksOK_one c3747))) (chunksOK_append (chunksOK_append (chunksOK_one c3748) (chunksOK_one c3749)) (chunksOK_append (chunksOK_one c3750) (chunksOK_one c3751)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3752) (chunksOK_one c3753)) (chunksOK_append (chunksOK_one c3754) (chunksOK_one c3755))) (chunksOK_append (chunksOK_append (chunksOK_one c3756) (chunksOK_one c3757)) (chunksOK_append (chunksOK_one c3758) (chunksOK_one c3759)))))

end C234

namespace C235

theorem c3760 : check 60 115 18 3760 = true := by decide +kernel
theorem c3761 : check 60 115 18 3761 = true := by decide +kernel
theorem c3762 : check 60 115 18 3762 = true := by decide +kernel
theorem c3763 : check 60 115 18 3763 = true := by decide +kernel
theorem c3764 : check 60 115 18 3764 = true := by decide +kernel
theorem c3765 : check 60 115 18 3765 = true := by decide +kernel
theorem c3766 : check 60 115 18 3766 = true := by decide +kernel
theorem c3767 : check 60 115 18 3767 = true := by decide +kernel
theorem c3768 : check 60 115 18 3768 = true := by decide +kernel
theorem c3769 : check 60 115 18 3769 = true := by decide +kernel
theorem c3770 : check 60 115 18 3770 = true := by decide +kernel
theorem c3771 : check 60 115 18 3771 = true := by decide +kernel
theorem c3772 : check 60 115 18 3772 = true := by decide +kernel
theorem c3773 : check 60 115 18 3773 = true := by decide +kernel
theorem c3774 : check 60 115 18 3774 = true := by decide +kernel
theorem c3775 : check 60 115 18 3775 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3760 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3760) (chunksOK_one c3761)) (chunksOK_append (chunksOK_one c3762) (chunksOK_one c3763))) (chunksOK_append (chunksOK_append (chunksOK_one c3764) (chunksOK_one c3765)) (chunksOK_append (chunksOK_one c3766) (chunksOK_one c3767)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3768) (chunksOK_one c3769)) (chunksOK_append (chunksOK_one c3770) (chunksOK_one c3771))) (chunksOK_append (chunksOK_append (chunksOK_one c3772) (chunksOK_one c3773)) (chunksOK_append (chunksOK_one c3774) (chunksOK_one c3775)))))

end C235

namespace C236

theorem c3776 : check 60 115 18 3776 = true := by decide +kernel
theorem c3777 : check 60 115 18 3777 = true := by decide +kernel
theorem c3778 : check 60 115 18 3778 = true := by decide +kernel
theorem c3779 : check 60 115 18 3779 = true := by decide +kernel
theorem c3780 : check 60 115 18 3780 = true := by decide +kernel
theorem c3781 : check 60 115 18 3781 = true := by decide +kernel
theorem c3782 : check 60 115 18 3782 = true := by decide +kernel
theorem c3783 : check 60 115 18 3783 = true := by decide +kernel
theorem c3784 : check 60 115 18 3784 = true := by decide +kernel
theorem c3785 : check 60 115 18 3785 = true := by decide +kernel
theorem c3786 : check 60 115 18 3786 = true := by decide +kernel
theorem c3787 : check 60 115 18 3787 = true := by decide +kernel
theorem c3788 : check 60 115 18 3788 = true := by decide +kernel
theorem c3789 : check 60 115 18 3789 = true := by decide +kernel
theorem c3790 : check 60 115 18 3790 = true := by decide +kernel
theorem c3791 : check 60 115 18 3791 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3776 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3776) (chunksOK_one c3777)) (chunksOK_append (chunksOK_one c3778) (chunksOK_one c3779))) (chunksOK_append (chunksOK_append (chunksOK_one c3780) (chunksOK_one c3781)) (chunksOK_append (chunksOK_one c3782) (chunksOK_one c3783)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3784) (chunksOK_one c3785)) (chunksOK_append (chunksOK_one c3786) (chunksOK_one c3787))) (chunksOK_append (chunksOK_append (chunksOK_one c3788) (chunksOK_one c3789)) (chunksOK_append (chunksOK_one c3790) (chunksOK_one c3791)))))

end C236

namespace C237

theorem c3792 : check 60 115 18 3792 = true := by decide +kernel
theorem c3793 : check 60 115 18 3793 = true := by decide +kernel
theorem c3794 : check 60 115 18 3794 = true := by decide +kernel
theorem c3795 : check 60 115 18 3795 = true := by decide +kernel
theorem c3796 : check 60 115 18 3796 = true := by decide +kernel
theorem c3797 : check 60 115 18 3797 = true := by decide +kernel
theorem c3798 : check 60 115 18 3798 = true := by decide +kernel
theorem c3799 : check 60 115 18 3799 = true := by decide +kernel
theorem c3800 : check 60 115 18 3800 = true := by decide +kernel
theorem c3801 : check 60 115 18 3801 = true := by decide +kernel
theorem c3802 : check 60 115 18 3802 = true := by decide +kernel
theorem c3803 : check 60 115 18 3803 = true := by decide +kernel
theorem c3804 : check 60 115 18 3804 = true := by decide +kernel
theorem c3805 : check 60 115 18 3805 = true := by decide +kernel
theorem c3806 : check 60 115 18 3806 = true := by decide +kernel
theorem c3807 : check 60 115 18 3807 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3792 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3792) (chunksOK_one c3793)) (chunksOK_append (chunksOK_one c3794) (chunksOK_one c3795))) (chunksOK_append (chunksOK_append (chunksOK_one c3796) (chunksOK_one c3797)) (chunksOK_append (chunksOK_one c3798) (chunksOK_one c3799)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3800) (chunksOK_one c3801)) (chunksOK_append (chunksOK_one c3802) (chunksOK_one c3803))) (chunksOK_append (chunksOK_append (chunksOK_one c3804) (chunksOK_one c3805)) (chunksOK_append (chunksOK_one c3806) (chunksOK_one c3807)))))

end C237

namespace C238

theorem c3808 : check 60 115 18 3808 = true := by decide +kernel
theorem c3809 : check 60 115 18 3809 = true := by decide +kernel
theorem c3810 : check 60 115 18 3810 = true := by decide +kernel
theorem c3811 : check 60 115 18 3811 = true := by decide +kernel
theorem c3812 : check 60 115 18 3812 = true := by decide +kernel
theorem c3813 : check 60 115 18 3813 = true := by decide +kernel
theorem c3814 : check 60 115 18 3814 = true := by decide +kernel
theorem c3815 : check 60 115 18 3815 = true := by decide +kernel
theorem c3816 : check 60 115 18 3816 = true := by decide +kernel
theorem c3817 : check 60 115 18 3817 = true := by decide +kernel
theorem c3818 : check 60 115 18 3818 = true := by decide +kernel
theorem c3819 : check 60 115 18 3819 = true := by decide +kernel
theorem c3820 : check 60 115 18 3820 = true := by decide +kernel
theorem c3821 : check 60 115 18 3821 = true := by decide +kernel
theorem c3822 : check 60 115 18 3822 = true := by decide +kernel
theorem c3823 : check 60 115 18 3823 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3808 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3808) (chunksOK_one c3809)) (chunksOK_append (chunksOK_one c3810) (chunksOK_one c3811))) (chunksOK_append (chunksOK_append (chunksOK_one c3812) (chunksOK_one c3813)) (chunksOK_append (chunksOK_one c3814) (chunksOK_one c3815)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3816) (chunksOK_one c3817)) (chunksOK_append (chunksOK_one c3818) (chunksOK_one c3819))) (chunksOK_append (chunksOK_append (chunksOK_one c3820) (chunksOK_one c3821)) (chunksOK_append (chunksOK_one c3822) (chunksOK_one c3823)))))

end C238

namespace C239

theorem c3824 : check 60 115 18 3824 = true := by decide +kernel
theorem c3825 : check 60 115 18 3825 = true := by decide +kernel
theorem c3826 : check 60 115 18 3826 = true := by decide +kernel
theorem c3827 : check 60 115 18 3827 = true := by decide +kernel
theorem c3828 : check 60 115 18 3828 = true := by decide +kernel
theorem c3829 : check 60 115 18 3829 = true := by decide +kernel
theorem c3830 : check 60 115 18 3830 = true := by decide +kernel
theorem c3831 : check 60 115 18 3831 = true := by decide +kernel
theorem c3832 : check 60 115 18 3832 = true := by decide +kernel
theorem c3833 : check 60 115 18 3833 = true := by decide +kernel
theorem c3834 : check 60 115 18 3834 = true := by decide +kernel
theorem c3835 : check 60 115 18 3835 = true := by decide +kernel
theorem c3836 : check 60 115 18 3836 = true := by decide +kernel
theorem c3837 : check 60 115 18 3837 = true := by decide +kernel
theorem c3838 : check 60 115 18 3838 = true := by decide +kernel
theorem c3839 : check 60 115 18 3839 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3824 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3824) (chunksOK_one c3825)) (chunksOK_append (chunksOK_one c3826) (chunksOK_one c3827))) (chunksOK_append (chunksOK_append (chunksOK_one c3828) (chunksOK_one c3829)) (chunksOK_append (chunksOK_one c3830) (chunksOK_one c3831)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3832) (chunksOK_one c3833)) (chunksOK_append (chunksOK_one c3834) (chunksOK_one c3835))) (chunksOK_append (chunksOK_append (chunksOK_one c3836) (chunksOK_one c3837)) (chunksOK_append (chunksOK_one c3838) (chunksOK_one c3839)))))

end C239

namespace C240

theorem c3840 : check 60 115 18 3840 = true := by decide +kernel
theorem c3841 : check 60 115 18 3841 = true := by decide +kernel
theorem c3842 : check 60 115 18 3842 = true := by decide +kernel
theorem c3843 : check 60 115 18 3843 = true := by decide +kernel
theorem c3844 : check 60 115 18 3844 = true := by decide +kernel
theorem c3845 : check 60 115 18 3845 = true := by decide +kernel
theorem c3846 : check 60 115 18 3846 = true := by decide +kernel
theorem c3847 : check 60 115 18 3847 = true := by decide +kernel
theorem c3848 : check 60 115 18 3848 = true := by decide +kernel
theorem c3849 : check 60 115 18 3849 = true := by decide +kernel
theorem c3850 : check 60 115 18 3850 = true := by decide +kernel
theorem c3851 : check 60 115 18 3851 = true := by decide +kernel
theorem c3852 : check 60 115 18 3852 = true := by decide +kernel
theorem c3853 : check 60 115 18 3853 = true := by decide +kernel
theorem c3854 : check 60 115 18 3854 = true := by decide +kernel
theorem c3855 : check 60 115 18 3855 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3840 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3840) (chunksOK_one c3841)) (chunksOK_append (chunksOK_one c3842) (chunksOK_one c3843))) (chunksOK_append (chunksOK_append (chunksOK_one c3844) (chunksOK_one c3845)) (chunksOK_append (chunksOK_one c3846) (chunksOK_one c3847)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3848) (chunksOK_one c3849)) (chunksOK_append (chunksOK_one c3850) (chunksOK_one c3851))) (chunksOK_append (chunksOK_append (chunksOK_one c3852) (chunksOK_one c3853)) (chunksOK_append (chunksOK_one c3854) (chunksOK_one c3855)))))

end C240

namespace C241

theorem c3856 : check 60 115 18 3856 = true := by decide +kernel
theorem c3857 : check 60 115 18 3857 = true := by decide +kernel
theorem c3858 : check 60 115 18 3858 = true := by decide +kernel
theorem c3859 : check 60 115 18 3859 = true := by decide +kernel
theorem c3860 : check 60 115 18 3860 = true := by decide +kernel
theorem c3861 : check 60 115 18 3861 = true := by decide +kernel
theorem c3862 : check 60 115 18 3862 = true := by decide +kernel
theorem c3863 : check 60 115 18 3863 = true := by decide +kernel
theorem c3864 : check 60 115 18 3864 = true := by decide +kernel
theorem c3865 : check 60 115 18 3865 = true := by decide +kernel
theorem c3866 : check 60 115 18 3866 = true := by decide +kernel
theorem c3867 : check 60 115 18 3867 = true := by decide +kernel
theorem c3868 : check 60 115 18 3868 = true := by decide +kernel
theorem c3869 : check 60 115 18 3869 = true := by decide +kernel
theorem c3870 : check 60 115 18 3870 = true := by decide +kernel
theorem c3871 : check 60 115 18 3871 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3856 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3856) (chunksOK_one c3857)) (chunksOK_append (chunksOK_one c3858) (chunksOK_one c3859))) (chunksOK_append (chunksOK_append (chunksOK_one c3860) (chunksOK_one c3861)) (chunksOK_append (chunksOK_one c3862) (chunksOK_one c3863)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3864) (chunksOK_one c3865)) (chunksOK_append (chunksOK_one c3866) (chunksOK_one c3867))) (chunksOK_append (chunksOK_append (chunksOK_one c3868) (chunksOK_one c3869)) (chunksOK_append (chunksOK_one c3870) (chunksOK_one c3871)))))

end C241

namespace C242

theorem c3872 : check 60 115 18 3872 = true := by decide +kernel
theorem c3873 : check 60 115 18 3873 = true := by decide +kernel
theorem c3874 : check 60 115 18 3874 = true := by decide +kernel
theorem c3875 : check 60 115 18 3875 = true := by decide +kernel
theorem c3876 : check 60 115 18 3876 = true := by decide +kernel
theorem c3877 : check 60 115 18 3877 = true := by decide +kernel
theorem c3878 : check 60 115 18 3878 = true := by decide +kernel
theorem c3879 : check 60 115 18 3879 = true := by decide +kernel
theorem c3880 : check 60 115 18 3880 = true := by decide +kernel
theorem c3881 : check 60 115 18 3881 = true := by decide +kernel
theorem c3882 : check 60 115 18 3882 = true := by decide +kernel
theorem c3883 : check 60 115 18 3883 = true := by decide +kernel
theorem c3884 : check 60 115 18 3884 = true := by decide +kernel
theorem c3885 : check 60 115 18 3885 = true := by decide +kernel
theorem c3886 : check 60 115 18 3886 = true := by decide +kernel
theorem c3887 : check 60 115 18 3887 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3872 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3872) (chunksOK_one c3873)) (chunksOK_append (chunksOK_one c3874) (chunksOK_one c3875))) (chunksOK_append (chunksOK_append (chunksOK_one c3876) (chunksOK_one c3877)) (chunksOK_append (chunksOK_one c3878) (chunksOK_one c3879)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3880) (chunksOK_one c3881)) (chunksOK_append (chunksOK_one c3882) (chunksOK_one c3883))) (chunksOK_append (chunksOK_append (chunksOK_one c3884) (chunksOK_one c3885)) (chunksOK_append (chunksOK_one c3886) (chunksOK_one c3887)))))

end C242

namespace C243

theorem c3888 : check 60 115 18 3888 = true := by decide +kernel
theorem c3889 : check 60 115 18 3889 = true := by decide +kernel
theorem c3890 : check 60 115 18 3890 = true := by decide +kernel
theorem c3891 : check 60 115 18 3891 = true := by decide +kernel
theorem c3892 : check 60 115 18 3892 = true := by decide +kernel
theorem c3893 : check 60 115 18 3893 = true := by decide +kernel
theorem c3894 : check 60 115 18 3894 = true := by decide +kernel
theorem c3895 : check 60 115 18 3895 = true := by decide +kernel
theorem c3896 : check 60 115 18 3896 = true := by decide +kernel
theorem c3897 : check 60 115 18 3897 = true := by decide +kernel
theorem c3898 : check 60 115 18 3898 = true := by decide +kernel
theorem c3899 : check 60 115 18 3899 = true := by decide +kernel
theorem c3900 : check 60 115 18 3900 = true := by decide +kernel
theorem c3901 : check 60 115 18 3901 = true := by decide +kernel
theorem c3902 : check 60 115 18 3902 = true := by decide +kernel
theorem c3903 : check 60 115 18 3903 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3888 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3888) (chunksOK_one c3889)) (chunksOK_append (chunksOK_one c3890) (chunksOK_one c3891))) (chunksOK_append (chunksOK_append (chunksOK_one c3892) (chunksOK_one c3893)) (chunksOK_append (chunksOK_one c3894) (chunksOK_one c3895)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3896) (chunksOK_one c3897)) (chunksOK_append (chunksOK_one c3898) (chunksOK_one c3899))) (chunksOK_append (chunksOK_append (chunksOK_one c3900) (chunksOK_one c3901)) (chunksOK_append (chunksOK_one c3902) (chunksOK_one c3903)))))

end C243

namespace C244

theorem c3904 : check 60 115 18 3904 = true := by decide +kernel
theorem c3905 : check 60 115 18 3905 = true := by decide +kernel
theorem c3906 : check 60 115 18 3906 = true := by decide +kernel
theorem c3907 : check 60 115 18 3907 = true := by decide +kernel
theorem c3908 : check 60 115 18 3908 = true := by decide +kernel
theorem c3909 : check 60 115 18 3909 = true := by decide +kernel
theorem c3910 : check 60 115 18 3910 = true := by decide +kernel
theorem c3911 : check 60 115 18 3911 = true := by decide +kernel
theorem c3912 : check 60 115 18 3912 = true := by decide +kernel
theorem c3913 : check 60 115 18 3913 = true := by decide +kernel
theorem c3914 : check 60 115 18 3914 = true := by decide +kernel
theorem c3915 : check 60 115 18 3915 = true := by decide +kernel
theorem c3916 : check 60 115 18 3916 = true := by decide +kernel
theorem c3917 : check 60 115 18 3917 = true := by decide +kernel
theorem c3918 : check 60 115 18 3918 = true := by decide +kernel
theorem c3919 : check 60 115 18 3919 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3904 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3904) (chunksOK_one c3905)) (chunksOK_append (chunksOK_one c3906) (chunksOK_one c3907))) (chunksOK_append (chunksOK_append (chunksOK_one c3908) (chunksOK_one c3909)) (chunksOK_append (chunksOK_one c3910) (chunksOK_one c3911)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3912) (chunksOK_one c3913)) (chunksOK_append (chunksOK_one c3914) (chunksOK_one c3915))) (chunksOK_append (chunksOK_append (chunksOK_one c3916) (chunksOK_one c3917)) (chunksOK_append (chunksOK_one c3918) (chunksOK_one c3919)))))

end C244

namespace C245

theorem c3920 : check 60 115 18 3920 = true := by decide +kernel
theorem c3921 : check 60 115 18 3921 = true := by decide +kernel
theorem c3922 : check 60 115 18 3922 = true := by decide +kernel
theorem c3923 : check 60 115 18 3923 = true := by decide +kernel
theorem c3924 : check 60 115 18 3924 = true := by decide +kernel
theorem c3925 : check 60 115 18 3925 = true := by decide +kernel
theorem c3926 : check 60 115 18 3926 = true := by decide +kernel
theorem c3927 : check 60 115 18 3927 = true := by decide +kernel
theorem c3928 : check 60 115 18 3928 = true := by decide +kernel
theorem c3929 : check 60 115 18 3929 = true := by decide +kernel
theorem c3930 : check 60 115 18 3930 = true := by decide +kernel
theorem c3931 : check 60 115 18 3931 = true := by decide +kernel
theorem c3932 : check 60 115 18 3932 = true := by decide +kernel
theorem c3933 : check 60 115 18 3933 = true := by decide +kernel
theorem c3934 : check 60 115 18 3934 = true := by decide +kernel
theorem c3935 : check 60 115 18 3935 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3920 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3920) (chunksOK_one c3921)) (chunksOK_append (chunksOK_one c3922) (chunksOK_one c3923))) (chunksOK_append (chunksOK_append (chunksOK_one c3924) (chunksOK_one c3925)) (chunksOK_append (chunksOK_one c3926) (chunksOK_one c3927)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3928) (chunksOK_one c3929)) (chunksOK_append (chunksOK_one c3930) (chunksOK_one c3931))) (chunksOK_append (chunksOK_append (chunksOK_one c3932) (chunksOK_one c3933)) (chunksOK_append (chunksOK_one c3934) (chunksOK_one c3935)))))

end C245

namespace C246

theorem c3936 : check 60 115 18 3936 = true := by decide +kernel
theorem c3937 : check 60 115 18 3937 = true := by decide +kernel
theorem c3938 : check 60 115 18 3938 = true := by decide +kernel
theorem c3939 : check 60 115 18 3939 = true := by decide +kernel
theorem c3940 : check 60 115 18 3940 = true := by decide +kernel
theorem c3941 : check 60 115 18 3941 = true := by decide +kernel
theorem c3942 : check 60 115 18 3942 = true := by decide +kernel
theorem c3943 : check 60 115 18 3943 = true := by decide +kernel
theorem c3944 : check 60 115 18 3944 = true := by decide +kernel
theorem c3945 : check 60 115 18 3945 = true := by decide +kernel
theorem c3946 : check 60 115 18 3946 = true := by decide +kernel
theorem c3947 : check 60 115 18 3947 = true := by decide +kernel
theorem c3948 : check 60 115 18 3948 = true := by decide +kernel
theorem c3949 : check 60 115 18 3949 = true := by decide +kernel
theorem c3950 : check 60 115 18 3950 = true := by decide +kernel
theorem c3951 : check 60 115 18 3951 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3936 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3936) (chunksOK_one c3937)) (chunksOK_append (chunksOK_one c3938) (chunksOK_one c3939))) (chunksOK_append (chunksOK_append (chunksOK_one c3940) (chunksOK_one c3941)) (chunksOK_append (chunksOK_one c3942) (chunksOK_one c3943)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3944) (chunksOK_one c3945)) (chunksOK_append (chunksOK_one c3946) (chunksOK_one c3947))) (chunksOK_append (chunksOK_append (chunksOK_one c3948) (chunksOK_one c3949)) (chunksOK_append (chunksOK_one c3950) (chunksOK_one c3951)))))

end C246

namespace C247

theorem c3952 : check 60 115 18 3952 = true := by decide +kernel
theorem c3953 : check 60 115 18 3953 = true := by decide +kernel
theorem c3954 : check 60 115 18 3954 = true := by decide +kernel
theorem c3955 : check 60 115 18 3955 = true := by decide +kernel
theorem c3956 : check 60 115 18 3956 = true := by decide +kernel
theorem c3957 : check 60 115 18 3957 = true := by decide +kernel
theorem c3958 : check 60 115 18 3958 = true := by decide +kernel
theorem c3959 : check 60 115 18 3959 = true := by decide +kernel
theorem c3960 : check 60 115 18 3960 = true := by decide +kernel
theorem c3961 : check 60 115 18 3961 = true := by decide +kernel
theorem c3962 : check 60 115 18 3962 = true := by decide +kernel
theorem c3963 : check 60 115 18 3963 = true := by decide +kernel
theorem c3964 : check 60 115 18 3964 = true := by decide +kernel
theorem c3965 : check 60 115 18 3965 = true := by decide +kernel
theorem c3966 : check 60 115 18 3966 = true := by decide +kernel
theorem c3967 : check 60 115 18 3967 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3952 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3952) (chunksOK_one c3953)) (chunksOK_append (chunksOK_one c3954) (chunksOK_one c3955))) (chunksOK_append (chunksOK_append (chunksOK_one c3956) (chunksOK_one c3957)) (chunksOK_append (chunksOK_one c3958) (chunksOK_one c3959)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3960) (chunksOK_one c3961)) (chunksOK_append (chunksOK_one c3962) (chunksOK_one c3963))) (chunksOK_append (chunksOK_append (chunksOK_one c3964) (chunksOK_one c3965)) (chunksOK_append (chunksOK_one c3966) (chunksOK_one c3967)))))

end C247

namespace C248

theorem c3968 : check 60 115 18 3968 = true := by decide +kernel
theorem c3969 : check 60 115 18 3969 = true := by decide +kernel
theorem c3970 : check 60 115 18 3970 = true := by decide +kernel
theorem c3971 : check 60 115 18 3971 = true := by decide +kernel
theorem c3972 : check 60 115 18 3972 = true := by decide +kernel
theorem c3973 : check 60 115 18 3973 = true := by decide +kernel
theorem c3974 : check 60 115 18 3974 = true := by decide +kernel
theorem c3975 : check 60 115 18 3975 = true := by decide +kernel
theorem c3976 : check 60 115 18 3976 = true := by decide +kernel
theorem c3977 : check 60 115 18 3977 = true := by decide +kernel
theorem c3978 : check 60 115 18 3978 = true := by decide +kernel
theorem c3979 : check 60 115 18 3979 = true := by decide +kernel
theorem c3980 : check 60 115 18 3980 = true := by decide +kernel
theorem c3981 : check 60 115 18 3981 = true := by decide +kernel
theorem c3982 : check 60 115 18 3982 = true := by decide +kernel
theorem c3983 : check 60 115 18 3983 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3968 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3968) (chunksOK_one c3969)) (chunksOK_append (chunksOK_one c3970) (chunksOK_one c3971))) (chunksOK_append (chunksOK_append (chunksOK_one c3972) (chunksOK_one c3973)) (chunksOK_append (chunksOK_one c3974) (chunksOK_one c3975)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3976) (chunksOK_one c3977)) (chunksOK_append (chunksOK_one c3978) (chunksOK_one c3979))) (chunksOK_append (chunksOK_append (chunksOK_one c3980) (chunksOK_one c3981)) (chunksOK_append (chunksOK_one c3982) (chunksOK_one c3983)))))

end C248

namespace C249

theorem c3984 : check 60 115 18 3984 = true := by decide +kernel
theorem c3985 : check 60 115 18 3985 = true := by decide +kernel
theorem c3986 : check 60 115 18 3986 = true := by decide +kernel
theorem c3987 : check 60 115 18 3987 = true := by decide +kernel
theorem c3988 : check 60 115 18 3988 = true := by decide +kernel
theorem c3989 : check 60 115 18 3989 = true := by decide +kernel
theorem c3990 : check 60 115 18 3990 = true := by decide +kernel
theorem c3991 : check 60 115 18 3991 = true := by decide +kernel
theorem c3992 : check 60 115 18 3992 = true := by decide +kernel
theorem c3993 : check 60 115 18 3993 = true := by decide +kernel
theorem c3994 : check 60 115 18 3994 = true := by decide +kernel
theorem c3995 : check 60 115 18 3995 = true := by decide +kernel
theorem c3996 : check 60 115 18 3996 = true := by decide +kernel
theorem c3997 : check 60 115 18 3997 = true := by decide +kernel
theorem c3998 : check 60 115 18 3998 = true := by decide +kernel
theorem c3999 : check 60 115 18 3999 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 3984 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3984) (chunksOK_one c3985)) (chunksOK_append (chunksOK_one c3986) (chunksOK_one c3987))) (chunksOK_append (chunksOK_append (chunksOK_one c3988) (chunksOK_one c3989)) (chunksOK_append (chunksOK_one c3990) (chunksOK_one c3991)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c3992) (chunksOK_one c3993)) (chunksOK_append (chunksOK_one c3994) (chunksOK_one c3995))) (chunksOK_append (chunksOK_append (chunksOK_one c3996) (chunksOK_one c3997)) (chunksOK_append (chunksOK_one c3998) (chunksOK_one c3999)))))

end C249

namespace C250

theorem c4000 : check 60 115 18 4000 = true := by decide +kernel
theorem c4001 : check 60 115 18 4001 = true := by decide +kernel
theorem c4002 : check 60 115 18 4002 = true := by decide +kernel
theorem c4003 : check 60 115 18 4003 = true := by decide +kernel
theorem c4004 : check 60 115 18 4004 = true := by decide +kernel
theorem c4005 : check 60 115 18 4005 = true := by decide +kernel
theorem c4006 : check 60 115 18 4006 = true := by decide +kernel
theorem c4007 : check 60 115 18 4007 = true := by decide +kernel
theorem c4008 : check 60 115 18 4008 = true := by decide +kernel
theorem c4009 : check 60 115 18 4009 = true := by decide +kernel
theorem c4010 : check 60 115 18 4010 = true := by decide +kernel
theorem c4011 : check 60 115 18 4011 = true := by decide +kernel
theorem c4012 : check 60 115 18 4012 = true := by decide +kernel
theorem c4013 : check 60 115 18 4013 = true := by decide +kernel
theorem c4014 : check 60 115 18 4014 = true := by decide +kernel
theorem c4015 : check 60 115 18 4015 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 4000 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c4000) (chunksOK_one c4001)) (chunksOK_append (chunksOK_one c4002) (chunksOK_one c4003))) (chunksOK_append (chunksOK_append (chunksOK_one c4004) (chunksOK_one c4005)) (chunksOK_append (chunksOK_one c4006) (chunksOK_one c4007)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c4008) (chunksOK_one c4009)) (chunksOK_append (chunksOK_one c4010) (chunksOK_one c4011))) (chunksOK_append (chunksOK_append (chunksOK_one c4012) (chunksOK_one c4013)) (chunksOK_append (chunksOK_one c4014) (chunksOK_one c4015)))))

end C250

namespace C251

theorem c4016 : check 60 115 18 4016 = true := by decide +kernel
theorem c4017 : check 60 115 18 4017 = true := by decide +kernel
theorem c4018 : check 60 115 18 4018 = true := by decide +kernel
theorem c4019 : check 60 115 18 4019 = true := by decide +kernel
theorem c4020 : check 60 115 18 4020 = true := by decide +kernel
theorem c4021 : check 60 115 18 4021 = true := by decide +kernel
theorem c4022 : check 60 115 18 4022 = true := by decide +kernel
theorem c4023 : check 60 115 18 4023 = true := by decide +kernel
theorem c4024 : check 60 115 18 4024 = true := by decide +kernel
theorem c4025 : check 60 115 18 4025 = true := by decide +kernel
theorem c4026 : check 60 115 18 4026 = true := by decide +kernel
theorem c4027 : check 60 115 18 4027 = true := by decide +kernel
theorem c4028 : check 60 115 18 4028 = true := by decide +kernel
theorem c4029 : check 60 115 18 4029 = true := by decide +kernel
theorem c4030 : check 60 115 18 4030 = true := by decide +kernel
theorem c4031 : check 60 115 18 4031 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 4016 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c4016) (chunksOK_one c4017)) (chunksOK_append (chunksOK_one c4018) (chunksOK_one c4019))) (chunksOK_append (chunksOK_append (chunksOK_one c4020) (chunksOK_one c4021)) (chunksOK_append (chunksOK_one c4022) (chunksOK_one c4023)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c4024) (chunksOK_one c4025)) (chunksOK_append (chunksOK_one c4026) (chunksOK_one c4027))) (chunksOK_append (chunksOK_append (chunksOK_one c4028) (chunksOK_one c4029)) (chunksOK_append (chunksOK_one c4030) (chunksOK_one c4031)))))

end C251

namespace C252

theorem c4032 : check 60 115 18 4032 = true := by decide +kernel
theorem c4033 : check 60 115 18 4033 = true := by decide +kernel
theorem c4034 : check 60 115 18 4034 = true := by decide +kernel
theorem c4035 : check 60 115 18 4035 = true := by decide +kernel
theorem c4036 : check 60 115 18 4036 = true := by decide +kernel
theorem c4037 : check 60 115 18 4037 = true := by decide +kernel
theorem c4038 : check 60 115 18 4038 = true := by decide +kernel
theorem c4039 : check 60 115 18 4039 = true := by decide +kernel
theorem c4040 : check 60 115 18 4040 = true := by decide +kernel
theorem c4041 : check 60 115 18 4041 = true := by decide +kernel
theorem c4042 : check 60 115 18 4042 = true := by decide +kernel
theorem c4043 : check 60 115 18 4043 = true := by decide +kernel
theorem c4044 : check 60 115 18 4044 = true := by decide +kernel
theorem c4045 : check 60 115 18 4045 = true := by decide +kernel
theorem c4046 : check 60 115 18 4046 = true := by decide +kernel
theorem c4047 : check 60 115 18 4047 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 4032 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c4032) (chunksOK_one c4033)) (chunksOK_append (chunksOK_one c4034) (chunksOK_one c4035))) (chunksOK_append (chunksOK_append (chunksOK_one c4036) (chunksOK_one c4037)) (chunksOK_append (chunksOK_one c4038) (chunksOK_one c4039)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c4040) (chunksOK_one c4041)) (chunksOK_append (chunksOK_one c4042) (chunksOK_one c4043))) (chunksOK_append (chunksOK_append (chunksOK_one c4044) (chunksOK_one c4045)) (chunksOK_append (chunksOK_one c4046) (chunksOK_one c4047)))))

end C252

namespace C253

theorem c4048 : check 60 115 18 4048 = true := by decide +kernel
theorem c4049 : check 60 115 18 4049 = true := by decide +kernel
theorem c4050 : check 60 115 18 4050 = true := by decide +kernel
theorem c4051 : check 60 115 18 4051 = true := by decide +kernel
theorem c4052 : check 60 115 18 4052 = true := by decide +kernel
theorem c4053 : check 60 115 18 4053 = true := by decide +kernel
theorem c4054 : check 60 115 18 4054 = true := by decide +kernel
theorem c4055 : check 60 115 18 4055 = true := by decide +kernel
theorem c4056 : check 60 115 18 4056 = true := by decide +kernel
theorem c4057 : check 60 115 18 4057 = true := by decide +kernel
theorem c4058 : check 60 115 18 4058 = true := by decide +kernel
theorem c4059 : check 60 115 18 4059 = true := by decide +kernel
theorem c4060 : check 60 115 18 4060 = true := by decide +kernel
theorem c4061 : check 60 115 18 4061 = true := by decide +kernel
theorem c4062 : check 60 115 18 4062 = true := by decide +kernel
theorem c4063 : check 60 115 18 4063 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 4048 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c4048) (chunksOK_one c4049)) (chunksOK_append (chunksOK_one c4050) (chunksOK_one c4051))) (chunksOK_append (chunksOK_append (chunksOK_one c4052) (chunksOK_one c4053)) (chunksOK_append (chunksOK_one c4054) (chunksOK_one c4055)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c4056) (chunksOK_one c4057)) (chunksOK_append (chunksOK_one c4058) (chunksOK_one c4059))) (chunksOK_append (chunksOK_append (chunksOK_one c4060) (chunksOK_one c4061)) (chunksOK_append (chunksOK_one c4062) (chunksOK_one c4063)))))

end C253

namespace C254

theorem c4064 : check 60 115 18 4064 = true := by decide +kernel
theorem c4065 : check 60 115 18 4065 = true := by decide +kernel
theorem c4066 : check 60 115 18 4066 = true := by decide +kernel
theorem c4067 : check 60 115 18 4067 = true := by decide +kernel
theorem c4068 : check 60 115 18 4068 = true := by decide +kernel
theorem c4069 : check 60 115 18 4069 = true := by decide +kernel
theorem c4070 : check 60 115 18 4070 = true := by decide +kernel
theorem c4071 : check 60 115 18 4071 = true := by decide +kernel
theorem c4072 : check 60 115 18 4072 = true := by decide +kernel
theorem c4073 : check 60 115 18 4073 = true := by decide +kernel
theorem c4074 : check 60 115 18 4074 = true := by decide +kernel
theorem c4075 : check 60 115 18 4075 = true := by decide +kernel
theorem c4076 : check 60 115 18 4076 = true := by decide +kernel
theorem c4077 : check 60 115 18 4077 = true := by decide +kernel
theorem c4078 : check 60 115 18 4078 = true := by decide +kernel
theorem c4079 : check 60 115 18 4079 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 4064 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c4064) (chunksOK_one c4065)) (chunksOK_append (chunksOK_one c4066) (chunksOK_one c4067))) (chunksOK_append (chunksOK_append (chunksOK_one c4068) (chunksOK_one c4069)) (chunksOK_append (chunksOK_one c4070) (chunksOK_one c4071)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c4072) (chunksOK_one c4073)) (chunksOK_append (chunksOK_one c4074) (chunksOK_one c4075))) (chunksOK_append (chunksOK_append (chunksOK_one c4076) (chunksOK_one c4077)) (chunksOK_append (chunksOK_one c4078) (chunksOK_one c4079)))))

end C254

namespace C255

theorem c4080 : check 60 115 18 4080 = true := by decide +kernel
theorem c4081 : check 60 115 18 4081 = true := by decide +kernel
theorem c4082 : check 60 115 18 4082 = true := by decide +kernel
theorem c4083 : check 60 115 18 4083 = true := by decide +kernel
theorem c4084 : check 60 115 18 4084 = true := by decide +kernel
theorem c4085 : check 60 115 18 4085 = true := by decide +kernel
theorem c4086 : check 60 115 18 4086 = true := by decide +kernel
theorem c4087 : check 60 115 18 4087 = true := by decide +kernel
theorem c4088 : check 60 115 18 4088 = true := by decide +kernel
theorem c4089 : check 60 115 18 4089 = true := by decide +kernel
theorem c4090 : check 60 115 18 4090 = true := by decide +kernel
theorem c4091 : check 60 115 18 4091 = true := by decide +kernel
theorem c4092 : check 60 115 18 4092 = true := by decide +kernel
theorem c4093 : check 60 115 18 4093 = true := by decide +kernel
theorem c4094 : check 60 115 18 4094 = true := by decide +kernel
theorem c4095 : check 60 115 18 4095 = true := by decide +kernel

theorem range : ChunksOK 60 115 18 4080 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c4080) (chunksOK_one c4081)) (chunksOK_append (chunksOK_one c4082) (chunksOK_one c4083))) (chunksOK_append (chunksOK_append (chunksOK_one c4084) (chunksOK_one c4085)) (chunksOK_append (chunksOK_one c4086) (chunksOK_one c4087)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c4088) (chunksOK_one c4089)) (chunksOK_append (chunksOK_one c4090) (chunksOK_one c4091))) (chunksOK_append (chunksOK_append (chunksOK_one c4092) (chunksOK_one c4093)) (chunksOK_append (chunksOK_one c4094) (chunksOK_one c4095)))))

end C255

/-! ## The assembled upper bound -/

theorem all_chunks : ChunksOK 60 115 18 0 4096 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append C0.range C1.range) (chunksOK_append C2.range C3.range)) (chunksOK_append (chunksOK_append C4.range C5.range) (chunksOK_append C6.range C7.range))) (chunksOK_append (chunksOK_append (chunksOK_append C8.range C9.range) (chunksOK_append C10.range C11.range)) (chunksOK_append (chunksOK_append C12.range C13.range) (chunksOK_append C14.range C15.range)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append C16.range C17.range) (chunksOK_append C18.range C19.range)) (chunksOK_append (chunksOK_append C20.range C21.range) (chunksOK_append C22.range C23.range))) (chunksOK_append (chunksOK_append (chunksOK_append C24.range C25.range) (chunksOK_append C26.range C27.range)) (chunksOK_append (chunksOK_append C28.range C29.range) (chunksOK_append C30.range C31.range))))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append C32.range C33.range) (chunksOK_append C34.range C35.range)) (chunksOK_append (chunksOK_append C36.range C37.range) (chunksOK_append C38.range C39.range))) (chunksOK_append (chunksOK_append (chunksOK_append C40.range C41.range) (chunksOK_append C42.range C43.range)) (chunksOK_append (chunksOK_append C44.range C45.range) (chunksOK_append C46.range C47.range)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append C48.range C49.range) (chunksOK_append C50.range C51.range)) (chunksOK_append (chunksOK_append C52.range C53.range) (chunksOK_append C54.range C55.range))) (chunksOK_append (chunksOK_append (chunksOK_append C56.range C57.range) (chunksOK_append C58.range C59.range)) (chunksOK_append (chunksOK_append C60.range C61.range) (chunksOK_append C62.range C63.range)))))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append C64.range C65.range) (chunksOK_append C66.range C67.range)) (chunksOK_append (chunksOK_append C68.range C69.range) (chunksOK_append C70.range C71.range))) (chunksOK_append (chunksOK_append (chunksOK_append C72.range C73.range) (chunksOK_append C74.range C75.range)) (chunksOK_append (chunksOK_append C76.range C77.range) (chunksOK_append C78.range C79.range)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append C80.range C81.range) (chunksOK_append C82.range C83.range)) (chunksOK_append (chunksOK_append C84.range C85.range) (chunksOK_append C86.range C87.range))) (chunksOK_append (chunksOK_append (chunksOK_append C88.range C89.range) (chunksOK_append C90.range C91.range)) (chunksOK_append (chunksOK_append C92.range C93.range) (chunksOK_append C94.range C95.range))))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append C96.range C97.range) (chunksOK_append C98.range C99.range)) (chunksOK_append (chunksOK_append C100.range C101.range) (chunksOK_append C102.range C103.range))) (chunksOK_append (chunksOK_append (chunksOK_append C104.range C105.range) (chunksOK_append C106.range C107.range)) (chunksOK_append (chunksOK_append C108.range C109.range) (chunksOK_append C110.range C111.range)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append C112.range C113.range) (chunksOK_append C114.range C115.range)) (chunksOK_append (chunksOK_append C116.range C117.range) (chunksOK_append C118.range C119.range))) (chunksOK_append (chunksOK_append (chunksOK_append C120.range C121.range) (chunksOK_append C122.range C123.range)) (chunksOK_append (chunksOK_append C124.range C125.range) (chunksOK_append C126.range C127.range))))))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append C128.range C129.range) (chunksOK_append C130.range C131.range)) (chunksOK_append (chunksOK_append C132.range C133.range) (chunksOK_append C134.range C135.range))) (chunksOK_append (chunksOK_append (chunksOK_append C136.range C137.range) (chunksOK_append C138.range C139.range)) (chunksOK_append (chunksOK_append C140.range C141.range) (chunksOK_append C142.range C143.range)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append C144.range C145.range) (chunksOK_append C146.range C147.range)) (chunksOK_append (chunksOK_append C148.range C149.range) (chunksOK_append C150.range C151.range))) (chunksOK_append (chunksOK_append (chunksOK_append C152.range C153.range) (chunksOK_append C154.range C155.range)) (chunksOK_append (chunksOK_append C156.range C157.range) (chunksOK_append C158.range C159.range))))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append C160.range C161.range) (chunksOK_append C162.range C163.range)) (chunksOK_append (chunksOK_append C164.range C165.range) (chunksOK_append C166.range C167.range))) (chunksOK_append (chunksOK_append (chunksOK_append C168.range C169.range) (chunksOK_append C170.range C171.range)) (chunksOK_append (chunksOK_append C172.range C173.range) (chunksOK_append C174.range C175.range)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append C176.range C177.range) (chunksOK_append C178.range C179.range)) (chunksOK_append (chunksOK_append C180.range C181.range) (chunksOK_append C182.range C183.range))) (chunksOK_append (chunksOK_append (chunksOK_append C184.range C185.range) (chunksOK_append C186.range C187.range)) (chunksOK_append (chunksOK_append C188.range C189.range) (chunksOK_append C190.range C191.range)))))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append C192.range C193.range) (chunksOK_append C194.range C195.range)) (chunksOK_append (chunksOK_append C196.range C197.range) (chunksOK_append C198.range C199.range))) (chunksOK_append (chunksOK_append (chunksOK_append C200.range C201.range) (chunksOK_append C202.range C203.range)) (chunksOK_append (chunksOK_append C204.range C205.range) (chunksOK_append C206.range C207.range)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append C208.range C209.range) (chunksOK_append C210.range C211.range)) (chunksOK_append (chunksOK_append C212.range C213.range) (chunksOK_append C214.range C215.range))) (chunksOK_append (chunksOK_append (chunksOK_append C216.range C217.range) (chunksOK_append C218.range C219.range)) (chunksOK_append (chunksOK_append C220.range C221.range) (chunksOK_append C222.range C223.range))))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append C224.range C225.range) (chunksOK_append C226.range C227.range)) (chunksOK_append (chunksOK_append C228.range C229.range) (chunksOK_append C230.range C231.range))) (chunksOK_append (chunksOK_append (chunksOK_append C232.range C233.range) (chunksOK_append C234.range C235.range)) (chunksOK_append (chunksOK_append C236.range C237.range) (chunksOK_append C238.range C239.range)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append C240.range C241.range) (chunksOK_append C242.range C243.range)) (chunksOK_append (chunksOK_append C244.range C245.range) (chunksOK_append C246.range C247.range))) (chunksOK_append (chunksOK_append (chunksOK_append C248.range C249.range) (chunksOK_append C250.range C251.range)) (chunksOK_append (chunksOK_append C252.range C253.range) (chunksOK_append C254.range C255.range))))))))

/-- Every start supported at depths at most 60 has a white depth-1 cell at an even time at most 114. -/
theorem q01_width_le_60 (x : Nat → Bool) (hx : ∀ k, 60 < k → x k = false) :
    ∃ t, t ≤ 114 ∧ t % 2 = 0 ∧ zrow x t 1 = false := by
  obtain ⟨t, ht, he, hz⟩ := q01_of_chunks 60 115 18 (by decide) all_chunks x hx
  exact ⟨t, by omega, he, hz⟩

/-! ## The witness -/

/-- The width-60 witness (60 bits; bits are depths 1 .. 60). -/
def w60 : Nat := 0xe77a4e77b8f99b5

theorem w60_lt : w60 < 2 ^ 60 := by decide

theorem toFun_width {r W : Nat} (h : r < 2 ^ W) (k : Nat) (hk : W < k) : toFun r k = false := by
  unfold toFun
  have h1 : k ≠ 0 := by omega
  simp only [h1, ite_false]
  exact testBit_ge_of_lt h (by omega)

theorem zrow_packed (r t : Nat) : zrow (toFun r) t 1 = (prun r t).testBit 0 := by
  rw [run_toFun]; rfl

/-- Black at depth 1 at every even time below 114: 57 packed orbits, kernel-evaluated. -/
theorem w60_black : ∀ s, s < 57 → (prun w60 (2 * s)).testBit 0 = true := by decide +kernel

theorem w60_white : (prun w60 114).testBit 0 = false := by decide +kernel

theorem w60_survives : ∀ t, t < 114 → t % 2 = 0 → zrow (toFun w60) t 1 = true := by
  intro t ht he
  rw [zrow_packed]
  obtain ⟨s, rfl⟩ : ∃ s, t = 2 * s := ⟨t / 2, by omega⟩
  exact w60_black s (by omega)

theorem w60_dies : zrow (toFun w60) 114 1 = false := by
  rw [zrow_packed]; exact w60_white

/-! ## The headline -/

/-- **The death time at width 60 is exactly 114.** -/
theorem death_time_60_exact :
    (∀ x : Nat → Bool, (∀ k, 60 < k → x k = false) → ∃ t, t ≤ 114 ∧ t % 2 = 0 ∧ zrow x t 1 = false) ∧
    (∃ x : Nat → Bool, (∀ k, 60 < k → x k = false) ∧ (∀ t, t < 114 → t % 2 = 0 → zrow x t 1 = true)) :=
  ⟨q01_width_le_60, ⟨toFun w60, toFun_width w60_lt, w60_survives⟩⟩

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

```wl
Head[rule30Submission]
```

## The headline theorem

```wl
opens = {"Ruliology.CellularAutomata.Rule30ZeroBoundary", "Ruliology.CellularAutomata.Rule30ZeroBoundarySmall", "Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes", "Rule30Submission"};
thm = rule30Submission["Rule30Submission.death_time_60_exact"];
thm["TypeForm", "Open" -> opens]
```

The upper bound, assembled from the chunks, and the witness's survival and death:

```wl
{rule30Submission["Rule30Submission.q01_width_le_60"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.w60_survives"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.w60_dies"]["TypeForm", "Open" -> opens]}
```

Two of the chunk checks, the first and the last, and the complete range:

```wl
{rule30Submission["Rule30Submission.C0.c0"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.C255.c4095"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.all_chunks"]["TypeForm", "Open" -> opens]}
```

The axioms behind the headline, which must be the standard three:

```wl
thm["Axioms"]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
thm["KernelCheck"]
```

## The table so far

| width W | D(W) | status |
|---|---|---|
| 52 | 96 | exact, kernel-checked (submission R30-20261023-8e6bd3; the kit's bound, attained) |
| 56 | 100 | exact, kernel-checked (submission R30-20261023-ac3898) |
| 60 | 114 | exact, kernel-checked here (this certificate, attained) |

The values 96, 100, 114 are not fitted by one common constant `c` in `D(W) = 2W - c` (the differences from `2W` are 8, 12, 6); that says nothing about every width. In our record a census over all 16,384 chunks at width 64 gives the numerical candidate 116, not certified.

## What is not proved

- No universal-width result: the upper theorem `q01_width_le_60` covers every width at most 60, and the only exact values established (here and in the two earlier submissions) are at widths 52, 56 and 60; no further exact value follows from this certificate, and `Q01` for every width is untouched.
- No law of `D(W)` is claimed.

## Provenance

The chunk text is the W2 generator's of the Wolfram · Collatz · Mahler record (an open research record kept on GitHub by Gareth Herbert with Claude and GPT), whose width-52 regeneration equals the kit's own modules line for line; the sixty-four-module form of this certificate was built and checked by the kit's `Check.lean` on the M5 on 2026-10-23 (CHAT-LEDGER.md L818), and this single module was built and kernel-replayed there under a supervised resource envelope (L844: build 1,181 s, replay 1,169 s, 8,466 constants; process maximum resident size 4,455 MiB in the build and 4,270 MiB in the replay, sampled process-group peaks 5,042 MiB and 4,930 MiB, as the receipt records them). The witness was found by a complete census over the 4,096 chunks and validated by two independent physical engines before its Lean proof. GPT (OpenAI) reviewed the production designs and sources and the selected receipt fields of the earlier stages; the single-module stage's selected receipt fields were supplied for its audit after this essay was written; raw omitted data and independent GPT replay are outside that audit. Submission R30-20261023-ac3898 showed the prize's verifier replaying a 1,024-check module; this module carries four times that number of chunk checks; its own runtime, memory and verification duration are measured separately, not inferred from that submission.

## References

[1] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[2] Wolfram Institute, [*Rule30PrizeKit*](https://github.com/WolframInstitute/Rule30PrizeKit), the reference Lean environment, commit cc1e0e0, 2026: `Rule30ZeroBoundary`, `Rule30ZeroBoundarySmall`, `Rule30ZeroBoundaryLanes`, `Rule30ZeroBoundaryWidth52`.

[3] The Wolfram · Collatz · Mahler record, [github.com/ghywel/placego](https://github.com/ghywel/placego): `tests/probes/wolfram/w2_harness.py`, `w5_harness.py`, `d1_engine.py`, `d2_witness.py`, `d3_submission.py`, `w6_check60.py` and CHAT-LEDGER.md L805 to L844, 2026.
