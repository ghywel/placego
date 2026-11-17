import Rule30PrizeKit
import Ruliology.CellularAutomata.Rule30ZeroBoundarySmall
import Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes

/-!
# The death time at width 60 is exactly 114: a complete chunk certificate and its witness

**Partial result on the kit's `Q01` (the period-2 question, Problem 1 of the Rule 30 Prize).** The kit proves `Q01`
for every zero-boundary start of width at most 52 (`Rule30ZeroBoundaryWidth52`, 256 chunk checks, bound 96) and
has no width-60 statement; W3 of our record certified bound 128 (4,096 checks at K = 129) and the census found the true maximum 114. This module
carries 1024 checks (`check 60 115 18 c = true`, each decided by the kernel, in 64 namespaces of 16 with the
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

/-! ## The 1024 chunk checks, kernel-decided -/
namespace C0

theorem c0 : check 60 115 20 0 = true := by decide +kernel
theorem c1 : check 60 115 20 1 = true := by decide +kernel
theorem c2 : check 60 115 20 2 = true := by decide +kernel
theorem c3 : check 60 115 20 3 = true := by decide +kernel
theorem c4 : check 60 115 20 4 = true := by decide +kernel
theorem c5 : check 60 115 20 5 = true := by decide +kernel
theorem c6 : check 60 115 20 6 = true := by decide +kernel
theorem c7 : check 60 115 20 7 = true := by decide +kernel
theorem c8 : check 60 115 20 8 = true := by decide +kernel
theorem c9 : check 60 115 20 9 = true := by decide +kernel
theorem c10 : check 60 115 20 10 = true := by decide +kernel
theorem c11 : check 60 115 20 11 = true := by decide +kernel
theorem c12 : check 60 115 20 12 = true := by decide +kernel
theorem c13 : check 60 115 20 13 = true := by decide +kernel
theorem c14 : check 60 115 20 14 = true := by decide +kernel
theorem c15 : check 60 115 20 15 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 0 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c0) (chunksOK_one c1)) (chunksOK_append (chunksOK_one c2) (chunksOK_one c3))) (chunksOK_append (chunksOK_append (chunksOK_one c4) (chunksOK_one c5)) (chunksOK_append (chunksOK_one c6) (chunksOK_one c7)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c8) (chunksOK_one c9)) (chunksOK_append (chunksOK_one c10) (chunksOK_one c11))) (chunksOK_append (chunksOK_append (chunksOK_one c12) (chunksOK_one c13)) (chunksOK_append (chunksOK_one c14) (chunksOK_one c15)))))

end C0

namespace C1

theorem c16 : check 60 115 20 16 = true := by decide +kernel
theorem c17 : check 60 115 20 17 = true := by decide +kernel
theorem c18 : check 60 115 20 18 = true := by decide +kernel
theorem c19 : check 60 115 20 19 = true := by decide +kernel
theorem c20 : check 60 115 20 20 = true := by decide +kernel
theorem c21 : check 60 115 20 21 = true := by decide +kernel
theorem c22 : check 60 115 20 22 = true := by decide +kernel
theorem c23 : check 60 115 20 23 = true := by decide +kernel
theorem c24 : check 60 115 20 24 = true := by decide +kernel
theorem c25 : check 60 115 20 25 = true := by decide +kernel
theorem c26 : check 60 115 20 26 = true := by decide +kernel
theorem c27 : check 60 115 20 27 = true := by decide +kernel
theorem c28 : check 60 115 20 28 = true := by decide +kernel
theorem c29 : check 60 115 20 29 = true := by decide +kernel
theorem c30 : check 60 115 20 30 = true := by decide +kernel
theorem c31 : check 60 115 20 31 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 16 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c16) (chunksOK_one c17)) (chunksOK_append (chunksOK_one c18) (chunksOK_one c19))) (chunksOK_append (chunksOK_append (chunksOK_one c20) (chunksOK_one c21)) (chunksOK_append (chunksOK_one c22) (chunksOK_one c23)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c24) (chunksOK_one c25)) (chunksOK_append (chunksOK_one c26) (chunksOK_one c27))) (chunksOK_append (chunksOK_append (chunksOK_one c28) (chunksOK_one c29)) (chunksOK_append (chunksOK_one c30) (chunksOK_one c31)))))

end C1

namespace C2

theorem c32 : check 60 115 20 32 = true := by decide +kernel
theorem c33 : check 60 115 20 33 = true := by decide +kernel
theorem c34 : check 60 115 20 34 = true := by decide +kernel
theorem c35 : check 60 115 20 35 = true := by decide +kernel
theorem c36 : check 60 115 20 36 = true := by decide +kernel
theorem c37 : check 60 115 20 37 = true := by decide +kernel
theorem c38 : check 60 115 20 38 = true := by decide +kernel
theorem c39 : check 60 115 20 39 = true := by decide +kernel
theorem c40 : check 60 115 20 40 = true := by decide +kernel
theorem c41 : check 60 115 20 41 = true := by decide +kernel
theorem c42 : check 60 115 20 42 = true := by decide +kernel
theorem c43 : check 60 115 20 43 = true := by decide +kernel
theorem c44 : check 60 115 20 44 = true := by decide +kernel
theorem c45 : check 60 115 20 45 = true := by decide +kernel
theorem c46 : check 60 115 20 46 = true := by decide +kernel
theorem c47 : check 60 115 20 47 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 32 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c32) (chunksOK_one c33)) (chunksOK_append (chunksOK_one c34) (chunksOK_one c35))) (chunksOK_append (chunksOK_append (chunksOK_one c36) (chunksOK_one c37)) (chunksOK_append (chunksOK_one c38) (chunksOK_one c39)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c40) (chunksOK_one c41)) (chunksOK_append (chunksOK_one c42) (chunksOK_one c43))) (chunksOK_append (chunksOK_append (chunksOK_one c44) (chunksOK_one c45)) (chunksOK_append (chunksOK_one c46) (chunksOK_one c47)))))

end C2

namespace C3

theorem c48 : check 60 115 20 48 = true := by decide +kernel
theorem c49 : check 60 115 20 49 = true := by decide +kernel
theorem c50 : check 60 115 20 50 = true := by decide +kernel
theorem c51 : check 60 115 20 51 = true := by decide +kernel
theorem c52 : check 60 115 20 52 = true := by decide +kernel
theorem c53 : check 60 115 20 53 = true := by decide +kernel
theorem c54 : check 60 115 20 54 = true := by decide +kernel
theorem c55 : check 60 115 20 55 = true := by decide +kernel
theorem c56 : check 60 115 20 56 = true := by decide +kernel
theorem c57 : check 60 115 20 57 = true := by decide +kernel
theorem c58 : check 60 115 20 58 = true := by decide +kernel
theorem c59 : check 60 115 20 59 = true := by decide +kernel
theorem c60 : check 60 115 20 60 = true := by decide +kernel
theorem c61 : check 60 115 20 61 = true := by decide +kernel
theorem c62 : check 60 115 20 62 = true := by decide +kernel
theorem c63 : check 60 115 20 63 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 48 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c48) (chunksOK_one c49)) (chunksOK_append (chunksOK_one c50) (chunksOK_one c51))) (chunksOK_append (chunksOK_append (chunksOK_one c52) (chunksOK_one c53)) (chunksOK_append (chunksOK_one c54) (chunksOK_one c55)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c56) (chunksOK_one c57)) (chunksOK_append (chunksOK_one c58) (chunksOK_one c59))) (chunksOK_append (chunksOK_append (chunksOK_one c60) (chunksOK_one c61)) (chunksOK_append (chunksOK_one c62) (chunksOK_one c63)))))

end C3

namespace C4

theorem c64 : check 60 115 20 64 = true := by decide +kernel
theorem c65 : check 60 115 20 65 = true := by decide +kernel
theorem c66 : check 60 115 20 66 = true := by decide +kernel
theorem c67 : check 60 115 20 67 = true := by decide +kernel
theorem c68 : check 60 115 20 68 = true := by decide +kernel
theorem c69 : check 60 115 20 69 = true := by decide +kernel
theorem c70 : check 60 115 20 70 = true := by decide +kernel
theorem c71 : check 60 115 20 71 = true := by decide +kernel
theorem c72 : check 60 115 20 72 = true := by decide +kernel
theorem c73 : check 60 115 20 73 = true := by decide +kernel
theorem c74 : check 60 115 20 74 = true := by decide +kernel
theorem c75 : check 60 115 20 75 = true := by decide +kernel
theorem c76 : check 60 115 20 76 = true := by decide +kernel
theorem c77 : check 60 115 20 77 = true := by decide +kernel
theorem c78 : check 60 115 20 78 = true := by decide +kernel
theorem c79 : check 60 115 20 79 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 64 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c64) (chunksOK_one c65)) (chunksOK_append (chunksOK_one c66) (chunksOK_one c67))) (chunksOK_append (chunksOK_append (chunksOK_one c68) (chunksOK_one c69)) (chunksOK_append (chunksOK_one c70) (chunksOK_one c71)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c72) (chunksOK_one c73)) (chunksOK_append (chunksOK_one c74) (chunksOK_one c75))) (chunksOK_append (chunksOK_append (chunksOK_one c76) (chunksOK_one c77)) (chunksOK_append (chunksOK_one c78) (chunksOK_one c79)))))

end C4

namespace C5

theorem c80 : check 60 115 20 80 = true := by decide +kernel
theorem c81 : check 60 115 20 81 = true := by decide +kernel
theorem c82 : check 60 115 20 82 = true := by decide +kernel
theorem c83 : check 60 115 20 83 = true := by decide +kernel
theorem c84 : check 60 115 20 84 = true := by decide +kernel
theorem c85 : check 60 115 20 85 = true := by decide +kernel
theorem c86 : check 60 115 20 86 = true := by decide +kernel
theorem c87 : check 60 115 20 87 = true := by decide +kernel
theorem c88 : check 60 115 20 88 = true := by decide +kernel
theorem c89 : check 60 115 20 89 = true := by decide +kernel
theorem c90 : check 60 115 20 90 = true := by decide +kernel
theorem c91 : check 60 115 20 91 = true := by decide +kernel
theorem c92 : check 60 115 20 92 = true := by decide +kernel
theorem c93 : check 60 115 20 93 = true := by decide +kernel
theorem c94 : check 60 115 20 94 = true := by decide +kernel
theorem c95 : check 60 115 20 95 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 80 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c80) (chunksOK_one c81)) (chunksOK_append (chunksOK_one c82) (chunksOK_one c83))) (chunksOK_append (chunksOK_append (chunksOK_one c84) (chunksOK_one c85)) (chunksOK_append (chunksOK_one c86) (chunksOK_one c87)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c88) (chunksOK_one c89)) (chunksOK_append (chunksOK_one c90) (chunksOK_one c91))) (chunksOK_append (chunksOK_append (chunksOK_one c92) (chunksOK_one c93)) (chunksOK_append (chunksOK_one c94) (chunksOK_one c95)))))

end C5

namespace C6

theorem c96 : check 60 115 20 96 = true := by decide +kernel
theorem c97 : check 60 115 20 97 = true := by decide +kernel
theorem c98 : check 60 115 20 98 = true := by decide +kernel
theorem c99 : check 60 115 20 99 = true := by decide +kernel
theorem c100 : check 60 115 20 100 = true := by decide +kernel
theorem c101 : check 60 115 20 101 = true := by decide +kernel
theorem c102 : check 60 115 20 102 = true := by decide +kernel
theorem c103 : check 60 115 20 103 = true := by decide +kernel
theorem c104 : check 60 115 20 104 = true := by decide +kernel
theorem c105 : check 60 115 20 105 = true := by decide +kernel
theorem c106 : check 60 115 20 106 = true := by decide +kernel
theorem c107 : check 60 115 20 107 = true := by decide +kernel
theorem c108 : check 60 115 20 108 = true := by decide +kernel
theorem c109 : check 60 115 20 109 = true := by decide +kernel
theorem c110 : check 60 115 20 110 = true := by decide +kernel
theorem c111 : check 60 115 20 111 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 96 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c96) (chunksOK_one c97)) (chunksOK_append (chunksOK_one c98) (chunksOK_one c99))) (chunksOK_append (chunksOK_append (chunksOK_one c100) (chunksOK_one c101)) (chunksOK_append (chunksOK_one c102) (chunksOK_one c103)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c104) (chunksOK_one c105)) (chunksOK_append (chunksOK_one c106) (chunksOK_one c107))) (chunksOK_append (chunksOK_append (chunksOK_one c108) (chunksOK_one c109)) (chunksOK_append (chunksOK_one c110) (chunksOK_one c111)))))

end C6

namespace C7

theorem c112 : check 60 115 20 112 = true := by decide +kernel
theorem c113 : check 60 115 20 113 = true := by decide +kernel
theorem c114 : check 60 115 20 114 = true := by decide +kernel
theorem c115 : check 60 115 20 115 = true := by decide +kernel
theorem c116 : check 60 115 20 116 = true := by decide +kernel
theorem c117 : check 60 115 20 117 = true := by decide +kernel
theorem c118 : check 60 115 20 118 = true := by decide +kernel
theorem c119 : check 60 115 20 119 = true := by decide +kernel
theorem c120 : check 60 115 20 120 = true := by decide +kernel
theorem c121 : check 60 115 20 121 = true := by decide +kernel
theorem c122 : check 60 115 20 122 = true := by decide +kernel
theorem c123 : check 60 115 20 123 = true := by decide +kernel
theorem c124 : check 60 115 20 124 = true := by decide +kernel
theorem c125 : check 60 115 20 125 = true := by decide +kernel
theorem c126 : check 60 115 20 126 = true := by decide +kernel
theorem c127 : check 60 115 20 127 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 112 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c112) (chunksOK_one c113)) (chunksOK_append (chunksOK_one c114) (chunksOK_one c115))) (chunksOK_append (chunksOK_append (chunksOK_one c116) (chunksOK_one c117)) (chunksOK_append (chunksOK_one c118) (chunksOK_one c119)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c120) (chunksOK_one c121)) (chunksOK_append (chunksOK_one c122) (chunksOK_one c123))) (chunksOK_append (chunksOK_append (chunksOK_one c124) (chunksOK_one c125)) (chunksOK_append (chunksOK_one c126) (chunksOK_one c127)))))

end C7

namespace C8

theorem c128 : check 60 115 20 128 = true := by decide +kernel
theorem c129 : check 60 115 20 129 = true := by decide +kernel
theorem c130 : check 60 115 20 130 = true := by decide +kernel
theorem c131 : check 60 115 20 131 = true := by decide +kernel
theorem c132 : check 60 115 20 132 = true := by decide +kernel
theorem c133 : check 60 115 20 133 = true := by decide +kernel
theorem c134 : check 60 115 20 134 = true := by decide +kernel
theorem c135 : check 60 115 20 135 = true := by decide +kernel
theorem c136 : check 60 115 20 136 = true := by decide +kernel
theorem c137 : check 60 115 20 137 = true := by decide +kernel
theorem c138 : check 60 115 20 138 = true := by decide +kernel
theorem c139 : check 60 115 20 139 = true := by decide +kernel
theorem c140 : check 60 115 20 140 = true := by decide +kernel
theorem c141 : check 60 115 20 141 = true := by decide +kernel
theorem c142 : check 60 115 20 142 = true := by decide +kernel
theorem c143 : check 60 115 20 143 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 128 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c128) (chunksOK_one c129)) (chunksOK_append (chunksOK_one c130) (chunksOK_one c131))) (chunksOK_append (chunksOK_append (chunksOK_one c132) (chunksOK_one c133)) (chunksOK_append (chunksOK_one c134) (chunksOK_one c135)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c136) (chunksOK_one c137)) (chunksOK_append (chunksOK_one c138) (chunksOK_one c139))) (chunksOK_append (chunksOK_append (chunksOK_one c140) (chunksOK_one c141)) (chunksOK_append (chunksOK_one c142) (chunksOK_one c143)))))

end C8

namespace C9

theorem c144 : check 60 115 20 144 = true := by decide +kernel
theorem c145 : check 60 115 20 145 = true := by decide +kernel
theorem c146 : check 60 115 20 146 = true := by decide +kernel
theorem c147 : check 60 115 20 147 = true := by decide +kernel
theorem c148 : check 60 115 20 148 = true := by decide +kernel
theorem c149 : check 60 115 20 149 = true := by decide +kernel
theorem c150 : check 60 115 20 150 = true := by decide +kernel
theorem c151 : check 60 115 20 151 = true := by decide +kernel
theorem c152 : check 60 115 20 152 = true := by decide +kernel
theorem c153 : check 60 115 20 153 = true := by decide +kernel
theorem c154 : check 60 115 20 154 = true := by decide +kernel
theorem c155 : check 60 115 20 155 = true := by decide +kernel
theorem c156 : check 60 115 20 156 = true := by decide +kernel
theorem c157 : check 60 115 20 157 = true := by decide +kernel
theorem c158 : check 60 115 20 158 = true := by decide +kernel
theorem c159 : check 60 115 20 159 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 144 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c144) (chunksOK_one c145)) (chunksOK_append (chunksOK_one c146) (chunksOK_one c147))) (chunksOK_append (chunksOK_append (chunksOK_one c148) (chunksOK_one c149)) (chunksOK_append (chunksOK_one c150) (chunksOK_one c151)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c152) (chunksOK_one c153)) (chunksOK_append (chunksOK_one c154) (chunksOK_one c155))) (chunksOK_append (chunksOK_append (chunksOK_one c156) (chunksOK_one c157)) (chunksOK_append (chunksOK_one c158) (chunksOK_one c159)))))

end C9

namespace C10

theorem c160 : check 60 115 20 160 = true := by decide +kernel
theorem c161 : check 60 115 20 161 = true := by decide +kernel
theorem c162 : check 60 115 20 162 = true := by decide +kernel
theorem c163 : check 60 115 20 163 = true := by decide +kernel
theorem c164 : check 60 115 20 164 = true := by decide +kernel
theorem c165 : check 60 115 20 165 = true := by decide +kernel
theorem c166 : check 60 115 20 166 = true := by decide +kernel
theorem c167 : check 60 115 20 167 = true := by decide +kernel
theorem c168 : check 60 115 20 168 = true := by decide +kernel
theorem c169 : check 60 115 20 169 = true := by decide +kernel
theorem c170 : check 60 115 20 170 = true := by decide +kernel
theorem c171 : check 60 115 20 171 = true := by decide +kernel
theorem c172 : check 60 115 20 172 = true := by decide +kernel
theorem c173 : check 60 115 20 173 = true := by decide +kernel
theorem c174 : check 60 115 20 174 = true := by decide +kernel
theorem c175 : check 60 115 20 175 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 160 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c160) (chunksOK_one c161)) (chunksOK_append (chunksOK_one c162) (chunksOK_one c163))) (chunksOK_append (chunksOK_append (chunksOK_one c164) (chunksOK_one c165)) (chunksOK_append (chunksOK_one c166) (chunksOK_one c167)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c168) (chunksOK_one c169)) (chunksOK_append (chunksOK_one c170) (chunksOK_one c171))) (chunksOK_append (chunksOK_append (chunksOK_one c172) (chunksOK_one c173)) (chunksOK_append (chunksOK_one c174) (chunksOK_one c175)))))

end C10

namespace C11

theorem c176 : check 60 115 20 176 = true := by decide +kernel
theorem c177 : check 60 115 20 177 = true := by decide +kernel
theorem c178 : check 60 115 20 178 = true := by decide +kernel
theorem c179 : check 60 115 20 179 = true := by decide +kernel
theorem c180 : check 60 115 20 180 = true := by decide +kernel
theorem c181 : check 60 115 20 181 = true := by decide +kernel
theorem c182 : check 60 115 20 182 = true := by decide +kernel
theorem c183 : check 60 115 20 183 = true := by decide +kernel
theorem c184 : check 60 115 20 184 = true := by decide +kernel
theorem c185 : check 60 115 20 185 = true := by decide +kernel
theorem c186 : check 60 115 20 186 = true := by decide +kernel
theorem c187 : check 60 115 20 187 = true := by decide +kernel
theorem c188 : check 60 115 20 188 = true := by decide +kernel
theorem c189 : check 60 115 20 189 = true := by decide +kernel
theorem c190 : check 60 115 20 190 = true := by decide +kernel
theorem c191 : check 60 115 20 191 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 176 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c176) (chunksOK_one c177)) (chunksOK_append (chunksOK_one c178) (chunksOK_one c179))) (chunksOK_append (chunksOK_append (chunksOK_one c180) (chunksOK_one c181)) (chunksOK_append (chunksOK_one c182) (chunksOK_one c183)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c184) (chunksOK_one c185)) (chunksOK_append (chunksOK_one c186) (chunksOK_one c187))) (chunksOK_append (chunksOK_append (chunksOK_one c188) (chunksOK_one c189)) (chunksOK_append (chunksOK_one c190) (chunksOK_one c191)))))

end C11

namespace C12

theorem c192 : check 60 115 20 192 = true := by decide +kernel
theorem c193 : check 60 115 20 193 = true := by decide +kernel
theorem c194 : check 60 115 20 194 = true := by decide +kernel
theorem c195 : check 60 115 20 195 = true := by decide +kernel
theorem c196 : check 60 115 20 196 = true := by decide +kernel
theorem c197 : check 60 115 20 197 = true := by decide +kernel
theorem c198 : check 60 115 20 198 = true := by decide +kernel
theorem c199 : check 60 115 20 199 = true := by decide +kernel
theorem c200 : check 60 115 20 200 = true := by decide +kernel
theorem c201 : check 60 115 20 201 = true := by decide +kernel
theorem c202 : check 60 115 20 202 = true := by decide +kernel
theorem c203 : check 60 115 20 203 = true := by decide +kernel
theorem c204 : check 60 115 20 204 = true := by decide +kernel
theorem c205 : check 60 115 20 205 = true := by decide +kernel
theorem c206 : check 60 115 20 206 = true := by decide +kernel
theorem c207 : check 60 115 20 207 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 192 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c192) (chunksOK_one c193)) (chunksOK_append (chunksOK_one c194) (chunksOK_one c195))) (chunksOK_append (chunksOK_append (chunksOK_one c196) (chunksOK_one c197)) (chunksOK_append (chunksOK_one c198) (chunksOK_one c199)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c200) (chunksOK_one c201)) (chunksOK_append (chunksOK_one c202) (chunksOK_one c203))) (chunksOK_append (chunksOK_append (chunksOK_one c204) (chunksOK_one c205)) (chunksOK_append (chunksOK_one c206) (chunksOK_one c207)))))

end C12

namespace C13

theorem c208 : check 60 115 20 208 = true := by decide +kernel
theorem c209 : check 60 115 20 209 = true := by decide +kernel
theorem c210 : check 60 115 20 210 = true := by decide +kernel
theorem c211 : check 60 115 20 211 = true := by decide +kernel
theorem c212 : check 60 115 20 212 = true := by decide +kernel
theorem c213 : check 60 115 20 213 = true := by decide +kernel
theorem c214 : check 60 115 20 214 = true := by decide +kernel
theorem c215 : check 60 115 20 215 = true := by decide +kernel
theorem c216 : check 60 115 20 216 = true := by decide +kernel
theorem c217 : check 60 115 20 217 = true := by decide +kernel
theorem c218 : check 60 115 20 218 = true := by decide +kernel
theorem c219 : check 60 115 20 219 = true := by decide +kernel
theorem c220 : check 60 115 20 220 = true := by decide +kernel
theorem c221 : check 60 115 20 221 = true := by decide +kernel
theorem c222 : check 60 115 20 222 = true := by decide +kernel
theorem c223 : check 60 115 20 223 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 208 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c208) (chunksOK_one c209)) (chunksOK_append (chunksOK_one c210) (chunksOK_one c211))) (chunksOK_append (chunksOK_append (chunksOK_one c212) (chunksOK_one c213)) (chunksOK_append (chunksOK_one c214) (chunksOK_one c215)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c216) (chunksOK_one c217)) (chunksOK_append (chunksOK_one c218) (chunksOK_one c219))) (chunksOK_append (chunksOK_append (chunksOK_one c220) (chunksOK_one c221)) (chunksOK_append (chunksOK_one c222) (chunksOK_one c223)))))

end C13

namespace C14

theorem c224 : check 60 115 20 224 = true := by decide +kernel
theorem c225 : check 60 115 20 225 = true := by decide +kernel
theorem c226 : check 60 115 20 226 = true := by decide +kernel
theorem c227 : check 60 115 20 227 = true := by decide +kernel
theorem c228 : check 60 115 20 228 = true := by decide +kernel
theorem c229 : check 60 115 20 229 = true := by decide +kernel
theorem c230 : check 60 115 20 230 = true := by decide +kernel
theorem c231 : check 60 115 20 231 = true := by decide +kernel
theorem c232 : check 60 115 20 232 = true := by decide +kernel
theorem c233 : check 60 115 20 233 = true := by decide +kernel
theorem c234 : check 60 115 20 234 = true := by decide +kernel
theorem c235 : check 60 115 20 235 = true := by decide +kernel
theorem c236 : check 60 115 20 236 = true := by decide +kernel
theorem c237 : check 60 115 20 237 = true := by decide +kernel
theorem c238 : check 60 115 20 238 = true := by decide +kernel
theorem c239 : check 60 115 20 239 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 224 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c224) (chunksOK_one c225)) (chunksOK_append (chunksOK_one c226) (chunksOK_one c227))) (chunksOK_append (chunksOK_append (chunksOK_one c228) (chunksOK_one c229)) (chunksOK_append (chunksOK_one c230) (chunksOK_one c231)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c232) (chunksOK_one c233)) (chunksOK_append (chunksOK_one c234) (chunksOK_one c235))) (chunksOK_append (chunksOK_append (chunksOK_one c236) (chunksOK_one c237)) (chunksOK_append (chunksOK_one c238) (chunksOK_one c239)))))

end C14

namespace C15

theorem c240 : check 60 115 20 240 = true := by decide +kernel
theorem c241 : check 60 115 20 241 = true := by decide +kernel
theorem c242 : check 60 115 20 242 = true := by decide +kernel
theorem c243 : check 60 115 20 243 = true := by decide +kernel
theorem c244 : check 60 115 20 244 = true := by decide +kernel
theorem c245 : check 60 115 20 245 = true := by decide +kernel
theorem c246 : check 60 115 20 246 = true := by decide +kernel
theorem c247 : check 60 115 20 247 = true := by decide +kernel
theorem c248 : check 60 115 20 248 = true := by decide +kernel
theorem c249 : check 60 115 20 249 = true := by decide +kernel
theorem c250 : check 60 115 20 250 = true := by decide +kernel
theorem c251 : check 60 115 20 251 = true := by decide +kernel
theorem c252 : check 60 115 20 252 = true := by decide +kernel
theorem c253 : check 60 115 20 253 = true := by decide +kernel
theorem c254 : check 60 115 20 254 = true := by decide +kernel
theorem c255 : check 60 115 20 255 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 240 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c240) (chunksOK_one c241)) (chunksOK_append (chunksOK_one c242) (chunksOK_one c243))) (chunksOK_append (chunksOK_append (chunksOK_one c244) (chunksOK_one c245)) (chunksOK_append (chunksOK_one c246) (chunksOK_one c247)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c248) (chunksOK_one c249)) (chunksOK_append (chunksOK_one c250) (chunksOK_one c251))) (chunksOK_append (chunksOK_append (chunksOK_one c252) (chunksOK_one c253)) (chunksOK_append (chunksOK_one c254) (chunksOK_one c255)))))

end C15

namespace C16

theorem c256 : check 60 115 20 256 = true := by decide +kernel
theorem c257 : check 60 115 20 257 = true := by decide +kernel
theorem c258 : check 60 115 20 258 = true := by decide +kernel
theorem c259 : check 60 115 20 259 = true := by decide +kernel
theorem c260 : check 60 115 20 260 = true := by decide +kernel
theorem c261 : check 60 115 20 261 = true := by decide +kernel
theorem c262 : check 60 115 20 262 = true := by decide +kernel
theorem c263 : check 60 115 20 263 = true := by decide +kernel
theorem c264 : check 60 115 20 264 = true := by decide +kernel
theorem c265 : check 60 115 20 265 = true := by decide +kernel
theorem c266 : check 60 115 20 266 = true := by decide +kernel
theorem c267 : check 60 115 20 267 = true := by decide +kernel
theorem c268 : check 60 115 20 268 = true := by decide +kernel
theorem c269 : check 60 115 20 269 = true := by decide +kernel
theorem c270 : check 60 115 20 270 = true := by decide +kernel
theorem c271 : check 60 115 20 271 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 256 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c256) (chunksOK_one c257)) (chunksOK_append (chunksOK_one c258) (chunksOK_one c259))) (chunksOK_append (chunksOK_append (chunksOK_one c260) (chunksOK_one c261)) (chunksOK_append (chunksOK_one c262) (chunksOK_one c263)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c264) (chunksOK_one c265)) (chunksOK_append (chunksOK_one c266) (chunksOK_one c267))) (chunksOK_append (chunksOK_append (chunksOK_one c268) (chunksOK_one c269)) (chunksOK_append (chunksOK_one c270) (chunksOK_one c271)))))

end C16

namespace C17

theorem c272 : check 60 115 20 272 = true := by decide +kernel
theorem c273 : check 60 115 20 273 = true := by decide +kernel
theorem c274 : check 60 115 20 274 = true := by decide +kernel
theorem c275 : check 60 115 20 275 = true := by decide +kernel
theorem c276 : check 60 115 20 276 = true := by decide +kernel
theorem c277 : check 60 115 20 277 = true := by decide +kernel
theorem c278 : check 60 115 20 278 = true := by decide +kernel
theorem c279 : check 60 115 20 279 = true := by decide +kernel
theorem c280 : check 60 115 20 280 = true := by decide +kernel
theorem c281 : check 60 115 20 281 = true := by decide +kernel
theorem c282 : check 60 115 20 282 = true := by decide +kernel
theorem c283 : check 60 115 20 283 = true := by decide +kernel
theorem c284 : check 60 115 20 284 = true := by decide +kernel
theorem c285 : check 60 115 20 285 = true := by decide +kernel
theorem c286 : check 60 115 20 286 = true := by decide +kernel
theorem c287 : check 60 115 20 287 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 272 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c272) (chunksOK_one c273)) (chunksOK_append (chunksOK_one c274) (chunksOK_one c275))) (chunksOK_append (chunksOK_append (chunksOK_one c276) (chunksOK_one c277)) (chunksOK_append (chunksOK_one c278) (chunksOK_one c279)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c280) (chunksOK_one c281)) (chunksOK_append (chunksOK_one c282) (chunksOK_one c283))) (chunksOK_append (chunksOK_append (chunksOK_one c284) (chunksOK_one c285)) (chunksOK_append (chunksOK_one c286) (chunksOK_one c287)))))

end C17

namespace C18

theorem c288 : check 60 115 20 288 = true := by decide +kernel
theorem c289 : check 60 115 20 289 = true := by decide +kernel
theorem c290 : check 60 115 20 290 = true := by decide +kernel
theorem c291 : check 60 115 20 291 = true := by decide +kernel
theorem c292 : check 60 115 20 292 = true := by decide +kernel
theorem c293 : check 60 115 20 293 = true := by decide +kernel
theorem c294 : check 60 115 20 294 = true := by decide +kernel
theorem c295 : check 60 115 20 295 = true := by decide +kernel
theorem c296 : check 60 115 20 296 = true := by decide +kernel
theorem c297 : check 60 115 20 297 = true := by decide +kernel
theorem c298 : check 60 115 20 298 = true := by decide +kernel
theorem c299 : check 60 115 20 299 = true := by decide +kernel
theorem c300 : check 60 115 20 300 = true := by decide +kernel
theorem c301 : check 60 115 20 301 = true := by decide +kernel
theorem c302 : check 60 115 20 302 = true := by decide +kernel
theorem c303 : check 60 115 20 303 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 288 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c288) (chunksOK_one c289)) (chunksOK_append (chunksOK_one c290) (chunksOK_one c291))) (chunksOK_append (chunksOK_append (chunksOK_one c292) (chunksOK_one c293)) (chunksOK_append (chunksOK_one c294) (chunksOK_one c295)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c296) (chunksOK_one c297)) (chunksOK_append (chunksOK_one c298) (chunksOK_one c299))) (chunksOK_append (chunksOK_append (chunksOK_one c300) (chunksOK_one c301)) (chunksOK_append (chunksOK_one c302) (chunksOK_one c303)))))

end C18

namespace C19

theorem c304 : check 60 115 20 304 = true := by decide +kernel
theorem c305 : check 60 115 20 305 = true := by decide +kernel
theorem c306 : check 60 115 20 306 = true := by decide +kernel
theorem c307 : check 60 115 20 307 = true := by decide +kernel
theorem c308 : check 60 115 20 308 = true := by decide +kernel
theorem c309 : check 60 115 20 309 = true := by decide +kernel
theorem c310 : check 60 115 20 310 = true := by decide +kernel
theorem c311 : check 60 115 20 311 = true := by decide +kernel
theorem c312 : check 60 115 20 312 = true := by decide +kernel
theorem c313 : check 60 115 20 313 = true := by decide +kernel
theorem c314 : check 60 115 20 314 = true := by decide +kernel
theorem c315 : check 60 115 20 315 = true := by decide +kernel
theorem c316 : check 60 115 20 316 = true := by decide +kernel
theorem c317 : check 60 115 20 317 = true := by decide +kernel
theorem c318 : check 60 115 20 318 = true := by decide +kernel
theorem c319 : check 60 115 20 319 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 304 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c304) (chunksOK_one c305)) (chunksOK_append (chunksOK_one c306) (chunksOK_one c307))) (chunksOK_append (chunksOK_append (chunksOK_one c308) (chunksOK_one c309)) (chunksOK_append (chunksOK_one c310) (chunksOK_one c311)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c312) (chunksOK_one c313)) (chunksOK_append (chunksOK_one c314) (chunksOK_one c315))) (chunksOK_append (chunksOK_append (chunksOK_one c316) (chunksOK_one c317)) (chunksOK_append (chunksOK_one c318) (chunksOK_one c319)))))

end C19

namespace C20

theorem c320 : check 60 115 20 320 = true := by decide +kernel
theorem c321 : check 60 115 20 321 = true := by decide +kernel
theorem c322 : check 60 115 20 322 = true := by decide +kernel
theorem c323 : check 60 115 20 323 = true := by decide +kernel
theorem c324 : check 60 115 20 324 = true := by decide +kernel
theorem c325 : check 60 115 20 325 = true := by decide +kernel
theorem c326 : check 60 115 20 326 = true := by decide +kernel
theorem c327 : check 60 115 20 327 = true := by decide +kernel
theorem c328 : check 60 115 20 328 = true := by decide +kernel
theorem c329 : check 60 115 20 329 = true := by decide +kernel
theorem c330 : check 60 115 20 330 = true := by decide +kernel
theorem c331 : check 60 115 20 331 = true := by decide +kernel
theorem c332 : check 60 115 20 332 = true := by decide +kernel
theorem c333 : check 60 115 20 333 = true := by decide +kernel
theorem c334 : check 60 115 20 334 = true := by decide +kernel
theorem c335 : check 60 115 20 335 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 320 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c320) (chunksOK_one c321)) (chunksOK_append (chunksOK_one c322) (chunksOK_one c323))) (chunksOK_append (chunksOK_append (chunksOK_one c324) (chunksOK_one c325)) (chunksOK_append (chunksOK_one c326) (chunksOK_one c327)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c328) (chunksOK_one c329)) (chunksOK_append (chunksOK_one c330) (chunksOK_one c331))) (chunksOK_append (chunksOK_append (chunksOK_one c332) (chunksOK_one c333)) (chunksOK_append (chunksOK_one c334) (chunksOK_one c335)))))

end C20

namespace C21

theorem c336 : check 60 115 20 336 = true := by decide +kernel
theorem c337 : check 60 115 20 337 = true := by decide +kernel
theorem c338 : check 60 115 20 338 = true := by decide +kernel
theorem c339 : check 60 115 20 339 = true := by decide +kernel
theorem c340 : check 60 115 20 340 = true := by decide +kernel
theorem c341 : check 60 115 20 341 = true := by decide +kernel
theorem c342 : check 60 115 20 342 = true := by decide +kernel
theorem c343 : check 60 115 20 343 = true := by decide +kernel
theorem c344 : check 60 115 20 344 = true := by decide +kernel
theorem c345 : check 60 115 20 345 = true := by decide +kernel
theorem c346 : check 60 115 20 346 = true := by decide +kernel
theorem c347 : check 60 115 20 347 = true := by decide +kernel
theorem c348 : check 60 115 20 348 = true := by decide +kernel
theorem c349 : check 60 115 20 349 = true := by decide +kernel
theorem c350 : check 60 115 20 350 = true := by decide +kernel
theorem c351 : check 60 115 20 351 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 336 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c336) (chunksOK_one c337)) (chunksOK_append (chunksOK_one c338) (chunksOK_one c339))) (chunksOK_append (chunksOK_append (chunksOK_one c340) (chunksOK_one c341)) (chunksOK_append (chunksOK_one c342) (chunksOK_one c343)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c344) (chunksOK_one c345)) (chunksOK_append (chunksOK_one c346) (chunksOK_one c347))) (chunksOK_append (chunksOK_append (chunksOK_one c348) (chunksOK_one c349)) (chunksOK_append (chunksOK_one c350) (chunksOK_one c351)))))

end C21

namespace C22

theorem c352 : check 60 115 20 352 = true := by decide +kernel
theorem c353 : check 60 115 20 353 = true := by decide +kernel
theorem c354 : check 60 115 20 354 = true := by decide +kernel
theorem c355 : check 60 115 20 355 = true := by decide +kernel
theorem c356 : check 60 115 20 356 = true := by decide +kernel
theorem c357 : check 60 115 20 357 = true := by decide +kernel
theorem c358 : check 60 115 20 358 = true := by decide +kernel
theorem c359 : check 60 115 20 359 = true := by decide +kernel
theorem c360 : check 60 115 20 360 = true := by decide +kernel
theorem c361 : check 60 115 20 361 = true := by decide +kernel
theorem c362 : check 60 115 20 362 = true := by decide +kernel
theorem c363 : check 60 115 20 363 = true := by decide +kernel
theorem c364 : check 60 115 20 364 = true := by decide +kernel
theorem c365 : check 60 115 20 365 = true := by decide +kernel
theorem c366 : check 60 115 20 366 = true := by decide +kernel
theorem c367 : check 60 115 20 367 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 352 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c352) (chunksOK_one c353)) (chunksOK_append (chunksOK_one c354) (chunksOK_one c355))) (chunksOK_append (chunksOK_append (chunksOK_one c356) (chunksOK_one c357)) (chunksOK_append (chunksOK_one c358) (chunksOK_one c359)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c360) (chunksOK_one c361)) (chunksOK_append (chunksOK_one c362) (chunksOK_one c363))) (chunksOK_append (chunksOK_append (chunksOK_one c364) (chunksOK_one c365)) (chunksOK_append (chunksOK_one c366) (chunksOK_one c367)))))

end C22

namespace C23

theorem c368 : check 60 115 20 368 = true := by decide +kernel
theorem c369 : check 60 115 20 369 = true := by decide +kernel
theorem c370 : check 60 115 20 370 = true := by decide +kernel
theorem c371 : check 60 115 20 371 = true := by decide +kernel
theorem c372 : check 60 115 20 372 = true := by decide +kernel
theorem c373 : check 60 115 20 373 = true := by decide +kernel
theorem c374 : check 60 115 20 374 = true := by decide +kernel
theorem c375 : check 60 115 20 375 = true := by decide +kernel
theorem c376 : check 60 115 20 376 = true := by decide +kernel
theorem c377 : check 60 115 20 377 = true := by decide +kernel
theorem c378 : check 60 115 20 378 = true := by decide +kernel
theorem c379 : check 60 115 20 379 = true := by decide +kernel
theorem c380 : check 60 115 20 380 = true := by decide +kernel
theorem c381 : check 60 115 20 381 = true := by decide +kernel
theorem c382 : check 60 115 20 382 = true := by decide +kernel
theorem c383 : check 60 115 20 383 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 368 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c368) (chunksOK_one c369)) (chunksOK_append (chunksOK_one c370) (chunksOK_one c371))) (chunksOK_append (chunksOK_append (chunksOK_one c372) (chunksOK_one c373)) (chunksOK_append (chunksOK_one c374) (chunksOK_one c375)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c376) (chunksOK_one c377)) (chunksOK_append (chunksOK_one c378) (chunksOK_one c379))) (chunksOK_append (chunksOK_append (chunksOK_one c380) (chunksOK_one c381)) (chunksOK_append (chunksOK_one c382) (chunksOK_one c383)))))

end C23

namespace C24

theorem c384 : check 60 115 20 384 = true := by decide +kernel
theorem c385 : check 60 115 20 385 = true := by decide +kernel
theorem c386 : check 60 115 20 386 = true := by decide +kernel
theorem c387 : check 60 115 20 387 = true := by decide +kernel
theorem c388 : check 60 115 20 388 = true := by decide +kernel
theorem c389 : check 60 115 20 389 = true := by decide +kernel
theorem c390 : check 60 115 20 390 = true := by decide +kernel
theorem c391 : check 60 115 20 391 = true := by decide +kernel
theorem c392 : check 60 115 20 392 = true := by decide +kernel
theorem c393 : check 60 115 20 393 = true := by decide +kernel
theorem c394 : check 60 115 20 394 = true := by decide +kernel
theorem c395 : check 60 115 20 395 = true := by decide +kernel
theorem c396 : check 60 115 20 396 = true := by decide +kernel
theorem c397 : check 60 115 20 397 = true := by decide +kernel
theorem c398 : check 60 115 20 398 = true := by decide +kernel
theorem c399 : check 60 115 20 399 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 384 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c384) (chunksOK_one c385)) (chunksOK_append (chunksOK_one c386) (chunksOK_one c387))) (chunksOK_append (chunksOK_append (chunksOK_one c388) (chunksOK_one c389)) (chunksOK_append (chunksOK_one c390) (chunksOK_one c391)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c392) (chunksOK_one c393)) (chunksOK_append (chunksOK_one c394) (chunksOK_one c395))) (chunksOK_append (chunksOK_append (chunksOK_one c396) (chunksOK_one c397)) (chunksOK_append (chunksOK_one c398) (chunksOK_one c399)))))

end C24

namespace C25

theorem c400 : check 60 115 20 400 = true := by decide +kernel
theorem c401 : check 60 115 20 401 = true := by decide +kernel
theorem c402 : check 60 115 20 402 = true := by decide +kernel
theorem c403 : check 60 115 20 403 = true := by decide +kernel
theorem c404 : check 60 115 20 404 = true := by decide +kernel
theorem c405 : check 60 115 20 405 = true := by decide +kernel
theorem c406 : check 60 115 20 406 = true := by decide +kernel
theorem c407 : check 60 115 20 407 = true := by decide +kernel
theorem c408 : check 60 115 20 408 = true := by decide +kernel
theorem c409 : check 60 115 20 409 = true := by decide +kernel
theorem c410 : check 60 115 20 410 = true := by decide +kernel
theorem c411 : check 60 115 20 411 = true := by decide +kernel
theorem c412 : check 60 115 20 412 = true := by decide +kernel
theorem c413 : check 60 115 20 413 = true := by decide +kernel
theorem c414 : check 60 115 20 414 = true := by decide +kernel
theorem c415 : check 60 115 20 415 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 400 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c400) (chunksOK_one c401)) (chunksOK_append (chunksOK_one c402) (chunksOK_one c403))) (chunksOK_append (chunksOK_append (chunksOK_one c404) (chunksOK_one c405)) (chunksOK_append (chunksOK_one c406) (chunksOK_one c407)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c408) (chunksOK_one c409)) (chunksOK_append (chunksOK_one c410) (chunksOK_one c411))) (chunksOK_append (chunksOK_append (chunksOK_one c412) (chunksOK_one c413)) (chunksOK_append (chunksOK_one c414) (chunksOK_one c415)))))

end C25

namespace C26

theorem c416 : check 60 115 20 416 = true := by decide +kernel
theorem c417 : check 60 115 20 417 = true := by decide +kernel
theorem c418 : check 60 115 20 418 = true := by decide +kernel
theorem c419 : check 60 115 20 419 = true := by decide +kernel
theorem c420 : check 60 115 20 420 = true := by decide +kernel
theorem c421 : check 60 115 20 421 = true := by decide +kernel
theorem c422 : check 60 115 20 422 = true := by decide +kernel
theorem c423 : check 60 115 20 423 = true := by decide +kernel
theorem c424 : check 60 115 20 424 = true := by decide +kernel
theorem c425 : check 60 115 20 425 = true := by decide +kernel
theorem c426 : check 60 115 20 426 = true := by decide +kernel
theorem c427 : check 60 115 20 427 = true := by decide +kernel
theorem c428 : check 60 115 20 428 = true := by decide +kernel
theorem c429 : check 60 115 20 429 = true := by decide +kernel
theorem c430 : check 60 115 20 430 = true := by decide +kernel
theorem c431 : check 60 115 20 431 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 416 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c416) (chunksOK_one c417)) (chunksOK_append (chunksOK_one c418) (chunksOK_one c419))) (chunksOK_append (chunksOK_append (chunksOK_one c420) (chunksOK_one c421)) (chunksOK_append (chunksOK_one c422) (chunksOK_one c423)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c424) (chunksOK_one c425)) (chunksOK_append (chunksOK_one c426) (chunksOK_one c427))) (chunksOK_append (chunksOK_append (chunksOK_one c428) (chunksOK_one c429)) (chunksOK_append (chunksOK_one c430) (chunksOK_one c431)))))

end C26

namespace C27

theorem c432 : check 60 115 20 432 = true := by decide +kernel
theorem c433 : check 60 115 20 433 = true := by decide +kernel
theorem c434 : check 60 115 20 434 = true := by decide +kernel
theorem c435 : check 60 115 20 435 = true := by decide +kernel
theorem c436 : check 60 115 20 436 = true := by decide +kernel
theorem c437 : check 60 115 20 437 = true := by decide +kernel
theorem c438 : check 60 115 20 438 = true := by decide +kernel
theorem c439 : check 60 115 20 439 = true := by decide +kernel
theorem c440 : check 60 115 20 440 = true := by decide +kernel
theorem c441 : check 60 115 20 441 = true := by decide +kernel
theorem c442 : check 60 115 20 442 = true := by decide +kernel
theorem c443 : check 60 115 20 443 = true := by decide +kernel
theorem c444 : check 60 115 20 444 = true := by decide +kernel
theorem c445 : check 60 115 20 445 = true := by decide +kernel
theorem c446 : check 60 115 20 446 = true := by decide +kernel
theorem c447 : check 60 115 20 447 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 432 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c432) (chunksOK_one c433)) (chunksOK_append (chunksOK_one c434) (chunksOK_one c435))) (chunksOK_append (chunksOK_append (chunksOK_one c436) (chunksOK_one c437)) (chunksOK_append (chunksOK_one c438) (chunksOK_one c439)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c440) (chunksOK_one c441)) (chunksOK_append (chunksOK_one c442) (chunksOK_one c443))) (chunksOK_append (chunksOK_append (chunksOK_one c444) (chunksOK_one c445)) (chunksOK_append (chunksOK_one c446) (chunksOK_one c447)))))

end C27

namespace C28

theorem c448 : check 60 115 20 448 = true := by decide +kernel
theorem c449 : check 60 115 20 449 = true := by decide +kernel
theorem c450 : check 60 115 20 450 = true := by decide +kernel
theorem c451 : check 60 115 20 451 = true := by decide +kernel
theorem c452 : check 60 115 20 452 = true := by decide +kernel
theorem c453 : check 60 115 20 453 = true := by decide +kernel
theorem c454 : check 60 115 20 454 = true := by decide +kernel
theorem c455 : check 60 115 20 455 = true := by decide +kernel
theorem c456 : check 60 115 20 456 = true := by decide +kernel
theorem c457 : check 60 115 20 457 = true := by decide +kernel
theorem c458 : check 60 115 20 458 = true := by decide +kernel
theorem c459 : check 60 115 20 459 = true := by decide +kernel
theorem c460 : check 60 115 20 460 = true := by decide +kernel
theorem c461 : check 60 115 20 461 = true := by decide +kernel
theorem c462 : check 60 115 20 462 = true := by decide +kernel
theorem c463 : check 60 115 20 463 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 448 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c448) (chunksOK_one c449)) (chunksOK_append (chunksOK_one c450) (chunksOK_one c451))) (chunksOK_append (chunksOK_append (chunksOK_one c452) (chunksOK_one c453)) (chunksOK_append (chunksOK_one c454) (chunksOK_one c455)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c456) (chunksOK_one c457)) (chunksOK_append (chunksOK_one c458) (chunksOK_one c459))) (chunksOK_append (chunksOK_append (chunksOK_one c460) (chunksOK_one c461)) (chunksOK_append (chunksOK_one c462) (chunksOK_one c463)))))

end C28

namespace C29

theorem c464 : check 60 115 20 464 = true := by decide +kernel
theorem c465 : check 60 115 20 465 = true := by decide +kernel
theorem c466 : check 60 115 20 466 = true := by decide +kernel
theorem c467 : check 60 115 20 467 = true := by decide +kernel
theorem c468 : check 60 115 20 468 = true := by decide +kernel
theorem c469 : check 60 115 20 469 = true := by decide +kernel
theorem c470 : check 60 115 20 470 = true := by decide +kernel
theorem c471 : check 60 115 20 471 = true := by decide +kernel
theorem c472 : check 60 115 20 472 = true := by decide +kernel
theorem c473 : check 60 115 20 473 = true := by decide +kernel
theorem c474 : check 60 115 20 474 = true := by decide +kernel
theorem c475 : check 60 115 20 475 = true := by decide +kernel
theorem c476 : check 60 115 20 476 = true := by decide +kernel
theorem c477 : check 60 115 20 477 = true := by decide +kernel
theorem c478 : check 60 115 20 478 = true := by decide +kernel
theorem c479 : check 60 115 20 479 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 464 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c464) (chunksOK_one c465)) (chunksOK_append (chunksOK_one c466) (chunksOK_one c467))) (chunksOK_append (chunksOK_append (chunksOK_one c468) (chunksOK_one c469)) (chunksOK_append (chunksOK_one c470) (chunksOK_one c471)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c472) (chunksOK_one c473)) (chunksOK_append (chunksOK_one c474) (chunksOK_one c475))) (chunksOK_append (chunksOK_append (chunksOK_one c476) (chunksOK_one c477)) (chunksOK_append (chunksOK_one c478) (chunksOK_one c479)))))

end C29

namespace C30

theorem c480 : check 60 115 20 480 = true := by decide +kernel
theorem c481 : check 60 115 20 481 = true := by decide +kernel
theorem c482 : check 60 115 20 482 = true := by decide +kernel
theorem c483 : check 60 115 20 483 = true := by decide +kernel
theorem c484 : check 60 115 20 484 = true := by decide +kernel
theorem c485 : check 60 115 20 485 = true := by decide +kernel
theorem c486 : check 60 115 20 486 = true := by decide +kernel
theorem c487 : check 60 115 20 487 = true := by decide +kernel
theorem c488 : check 60 115 20 488 = true := by decide +kernel
theorem c489 : check 60 115 20 489 = true := by decide +kernel
theorem c490 : check 60 115 20 490 = true := by decide +kernel
theorem c491 : check 60 115 20 491 = true := by decide +kernel
theorem c492 : check 60 115 20 492 = true := by decide +kernel
theorem c493 : check 60 115 20 493 = true := by decide +kernel
theorem c494 : check 60 115 20 494 = true := by decide +kernel
theorem c495 : check 60 115 20 495 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 480 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c480) (chunksOK_one c481)) (chunksOK_append (chunksOK_one c482) (chunksOK_one c483))) (chunksOK_append (chunksOK_append (chunksOK_one c484) (chunksOK_one c485)) (chunksOK_append (chunksOK_one c486) (chunksOK_one c487)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c488) (chunksOK_one c489)) (chunksOK_append (chunksOK_one c490) (chunksOK_one c491))) (chunksOK_append (chunksOK_append (chunksOK_one c492) (chunksOK_one c493)) (chunksOK_append (chunksOK_one c494) (chunksOK_one c495)))))

end C30

namespace C31

theorem c496 : check 60 115 20 496 = true := by decide +kernel
theorem c497 : check 60 115 20 497 = true := by decide +kernel
theorem c498 : check 60 115 20 498 = true := by decide +kernel
theorem c499 : check 60 115 20 499 = true := by decide +kernel
theorem c500 : check 60 115 20 500 = true := by decide +kernel
theorem c501 : check 60 115 20 501 = true := by decide +kernel
theorem c502 : check 60 115 20 502 = true := by decide +kernel
theorem c503 : check 60 115 20 503 = true := by decide +kernel
theorem c504 : check 60 115 20 504 = true := by decide +kernel
theorem c505 : check 60 115 20 505 = true := by decide +kernel
theorem c506 : check 60 115 20 506 = true := by decide +kernel
theorem c507 : check 60 115 20 507 = true := by decide +kernel
theorem c508 : check 60 115 20 508 = true := by decide +kernel
theorem c509 : check 60 115 20 509 = true := by decide +kernel
theorem c510 : check 60 115 20 510 = true := by decide +kernel
theorem c511 : check 60 115 20 511 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 496 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c496) (chunksOK_one c497)) (chunksOK_append (chunksOK_one c498) (chunksOK_one c499))) (chunksOK_append (chunksOK_append (chunksOK_one c500) (chunksOK_one c501)) (chunksOK_append (chunksOK_one c502) (chunksOK_one c503)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c504) (chunksOK_one c505)) (chunksOK_append (chunksOK_one c506) (chunksOK_one c507))) (chunksOK_append (chunksOK_append (chunksOK_one c508) (chunksOK_one c509)) (chunksOK_append (chunksOK_one c510) (chunksOK_one c511)))))

end C31

namespace C32

theorem c512 : check 60 115 20 512 = true := by decide +kernel
theorem c513 : check 60 115 20 513 = true := by decide +kernel
theorem c514 : check 60 115 20 514 = true := by decide +kernel
theorem c515 : check 60 115 20 515 = true := by decide +kernel
theorem c516 : check 60 115 20 516 = true := by decide +kernel
theorem c517 : check 60 115 20 517 = true := by decide +kernel
theorem c518 : check 60 115 20 518 = true := by decide +kernel
theorem c519 : check 60 115 20 519 = true := by decide +kernel
theorem c520 : check 60 115 20 520 = true := by decide +kernel
theorem c521 : check 60 115 20 521 = true := by decide +kernel
theorem c522 : check 60 115 20 522 = true := by decide +kernel
theorem c523 : check 60 115 20 523 = true := by decide +kernel
theorem c524 : check 60 115 20 524 = true := by decide +kernel
theorem c525 : check 60 115 20 525 = true := by decide +kernel
theorem c526 : check 60 115 20 526 = true := by decide +kernel
theorem c527 : check 60 115 20 527 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 512 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c512) (chunksOK_one c513)) (chunksOK_append (chunksOK_one c514) (chunksOK_one c515))) (chunksOK_append (chunksOK_append (chunksOK_one c516) (chunksOK_one c517)) (chunksOK_append (chunksOK_one c518) (chunksOK_one c519)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c520) (chunksOK_one c521)) (chunksOK_append (chunksOK_one c522) (chunksOK_one c523))) (chunksOK_append (chunksOK_append (chunksOK_one c524) (chunksOK_one c525)) (chunksOK_append (chunksOK_one c526) (chunksOK_one c527)))))

end C32

namespace C33

theorem c528 : check 60 115 20 528 = true := by decide +kernel
theorem c529 : check 60 115 20 529 = true := by decide +kernel
theorem c530 : check 60 115 20 530 = true := by decide +kernel
theorem c531 : check 60 115 20 531 = true := by decide +kernel
theorem c532 : check 60 115 20 532 = true := by decide +kernel
theorem c533 : check 60 115 20 533 = true := by decide +kernel
theorem c534 : check 60 115 20 534 = true := by decide +kernel
theorem c535 : check 60 115 20 535 = true := by decide +kernel
theorem c536 : check 60 115 20 536 = true := by decide +kernel
theorem c537 : check 60 115 20 537 = true := by decide +kernel
theorem c538 : check 60 115 20 538 = true := by decide +kernel
theorem c539 : check 60 115 20 539 = true := by decide +kernel
theorem c540 : check 60 115 20 540 = true := by decide +kernel
theorem c541 : check 60 115 20 541 = true := by decide +kernel
theorem c542 : check 60 115 20 542 = true := by decide +kernel
theorem c543 : check 60 115 20 543 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 528 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c528) (chunksOK_one c529)) (chunksOK_append (chunksOK_one c530) (chunksOK_one c531))) (chunksOK_append (chunksOK_append (chunksOK_one c532) (chunksOK_one c533)) (chunksOK_append (chunksOK_one c534) (chunksOK_one c535)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c536) (chunksOK_one c537)) (chunksOK_append (chunksOK_one c538) (chunksOK_one c539))) (chunksOK_append (chunksOK_append (chunksOK_one c540) (chunksOK_one c541)) (chunksOK_append (chunksOK_one c542) (chunksOK_one c543)))))

end C33

namespace C34

theorem c544 : check 60 115 20 544 = true := by decide +kernel
theorem c545 : check 60 115 20 545 = true := by decide +kernel
theorem c546 : check 60 115 20 546 = true := by decide +kernel
theorem c547 : check 60 115 20 547 = true := by decide +kernel
theorem c548 : check 60 115 20 548 = true := by decide +kernel
theorem c549 : check 60 115 20 549 = true := by decide +kernel
theorem c550 : check 60 115 20 550 = true := by decide +kernel
theorem c551 : check 60 115 20 551 = true := by decide +kernel
theorem c552 : check 60 115 20 552 = true := by decide +kernel
theorem c553 : check 60 115 20 553 = true := by decide +kernel
theorem c554 : check 60 115 20 554 = true := by decide +kernel
theorem c555 : check 60 115 20 555 = true := by decide +kernel
theorem c556 : check 60 115 20 556 = true := by decide +kernel
theorem c557 : check 60 115 20 557 = true := by decide +kernel
theorem c558 : check 60 115 20 558 = true := by decide +kernel
theorem c559 : check 60 115 20 559 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 544 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c544) (chunksOK_one c545)) (chunksOK_append (chunksOK_one c546) (chunksOK_one c547))) (chunksOK_append (chunksOK_append (chunksOK_one c548) (chunksOK_one c549)) (chunksOK_append (chunksOK_one c550) (chunksOK_one c551)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c552) (chunksOK_one c553)) (chunksOK_append (chunksOK_one c554) (chunksOK_one c555))) (chunksOK_append (chunksOK_append (chunksOK_one c556) (chunksOK_one c557)) (chunksOK_append (chunksOK_one c558) (chunksOK_one c559)))))

end C34

namespace C35

theorem c560 : check 60 115 20 560 = true := by decide +kernel
theorem c561 : check 60 115 20 561 = true := by decide +kernel
theorem c562 : check 60 115 20 562 = true := by decide +kernel
theorem c563 : check 60 115 20 563 = true := by decide +kernel
theorem c564 : check 60 115 20 564 = true := by decide +kernel
theorem c565 : check 60 115 20 565 = true := by decide +kernel
theorem c566 : check 60 115 20 566 = true := by decide +kernel
theorem c567 : check 60 115 20 567 = true := by decide +kernel
theorem c568 : check 60 115 20 568 = true := by decide +kernel
theorem c569 : check 60 115 20 569 = true := by decide +kernel
theorem c570 : check 60 115 20 570 = true := by decide +kernel
theorem c571 : check 60 115 20 571 = true := by decide +kernel
theorem c572 : check 60 115 20 572 = true := by decide +kernel
theorem c573 : check 60 115 20 573 = true := by decide +kernel
theorem c574 : check 60 115 20 574 = true := by decide +kernel
theorem c575 : check 60 115 20 575 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 560 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c560) (chunksOK_one c561)) (chunksOK_append (chunksOK_one c562) (chunksOK_one c563))) (chunksOK_append (chunksOK_append (chunksOK_one c564) (chunksOK_one c565)) (chunksOK_append (chunksOK_one c566) (chunksOK_one c567)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c568) (chunksOK_one c569)) (chunksOK_append (chunksOK_one c570) (chunksOK_one c571))) (chunksOK_append (chunksOK_append (chunksOK_one c572) (chunksOK_one c573)) (chunksOK_append (chunksOK_one c574) (chunksOK_one c575)))))

end C35

namespace C36

theorem c576 : check 60 115 20 576 = true := by decide +kernel
theorem c577 : check 60 115 20 577 = true := by decide +kernel
theorem c578 : check 60 115 20 578 = true := by decide +kernel
theorem c579 : check 60 115 20 579 = true := by decide +kernel
theorem c580 : check 60 115 20 580 = true := by decide +kernel
theorem c581 : check 60 115 20 581 = true := by decide +kernel
theorem c582 : check 60 115 20 582 = true := by decide +kernel
theorem c583 : check 60 115 20 583 = true := by decide +kernel
theorem c584 : check 60 115 20 584 = true := by decide +kernel
theorem c585 : check 60 115 20 585 = true := by decide +kernel
theorem c586 : check 60 115 20 586 = true := by decide +kernel
theorem c587 : check 60 115 20 587 = true := by decide +kernel
theorem c588 : check 60 115 20 588 = true := by decide +kernel
theorem c589 : check 60 115 20 589 = true := by decide +kernel
theorem c590 : check 60 115 20 590 = true := by decide +kernel
theorem c591 : check 60 115 20 591 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 576 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c576) (chunksOK_one c577)) (chunksOK_append (chunksOK_one c578) (chunksOK_one c579))) (chunksOK_append (chunksOK_append (chunksOK_one c580) (chunksOK_one c581)) (chunksOK_append (chunksOK_one c582) (chunksOK_one c583)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c584) (chunksOK_one c585)) (chunksOK_append (chunksOK_one c586) (chunksOK_one c587))) (chunksOK_append (chunksOK_append (chunksOK_one c588) (chunksOK_one c589)) (chunksOK_append (chunksOK_one c590) (chunksOK_one c591)))))

end C36

namespace C37

theorem c592 : check 60 115 20 592 = true := by decide +kernel
theorem c593 : check 60 115 20 593 = true := by decide +kernel
theorem c594 : check 60 115 20 594 = true := by decide +kernel
theorem c595 : check 60 115 20 595 = true := by decide +kernel
theorem c596 : check 60 115 20 596 = true := by decide +kernel
theorem c597 : check 60 115 20 597 = true := by decide +kernel
theorem c598 : check 60 115 20 598 = true := by decide +kernel
theorem c599 : check 60 115 20 599 = true := by decide +kernel
theorem c600 : check 60 115 20 600 = true := by decide +kernel
theorem c601 : check 60 115 20 601 = true := by decide +kernel
theorem c602 : check 60 115 20 602 = true := by decide +kernel
theorem c603 : check 60 115 20 603 = true := by decide +kernel
theorem c604 : check 60 115 20 604 = true := by decide +kernel
theorem c605 : check 60 115 20 605 = true := by decide +kernel
theorem c606 : check 60 115 20 606 = true := by decide +kernel
theorem c607 : check 60 115 20 607 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 592 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c592) (chunksOK_one c593)) (chunksOK_append (chunksOK_one c594) (chunksOK_one c595))) (chunksOK_append (chunksOK_append (chunksOK_one c596) (chunksOK_one c597)) (chunksOK_append (chunksOK_one c598) (chunksOK_one c599)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c600) (chunksOK_one c601)) (chunksOK_append (chunksOK_one c602) (chunksOK_one c603))) (chunksOK_append (chunksOK_append (chunksOK_one c604) (chunksOK_one c605)) (chunksOK_append (chunksOK_one c606) (chunksOK_one c607)))))

end C37

namespace C38

theorem c608 : check 60 115 20 608 = true := by decide +kernel
theorem c609 : check 60 115 20 609 = true := by decide +kernel
theorem c610 : check 60 115 20 610 = true := by decide +kernel
theorem c611 : check 60 115 20 611 = true := by decide +kernel
theorem c612 : check 60 115 20 612 = true := by decide +kernel
theorem c613 : check 60 115 20 613 = true := by decide +kernel
theorem c614 : check 60 115 20 614 = true := by decide +kernel
theorem c615 : check 60 115 20 615 = true := by decide +kernel
theorem c616 : check 60 115 20 616 = true := by decide +kernel
theorem c617 : check 60 115 20 617 = true := by decide +kernel
theorem c618 : check 60 115 20 618 = true := by decide +kernel
theorem c619 : check 60 115 20 619 = true := by decide +kernel
theorem c620 : check 60 115 20 620 = true := by decide +kernel
theorem c621 : check 60 115 20 621 = true := by decide +kernel
theorem c622 : check 60 115 20 622 = true := by decide +kernel
theorem c623 : check 60 115 20 623 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 608 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c608) (chunksOK_one c609)) (chunksOK_append (chunksOK_one c610) (chunksOK_one c611))) (chunksOK_append (chunksOK_append (chunksOK_one c612) (chunksOK_one c613)) (chunksOK_append (chunksOK_one c614) (chunksOK_one c615)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c616) (chunksOK_one c617)) (chunksOK_append (chunksOK_one c618) (chunksOK_one c619))) (chunksOK_append (chunksOK_append (chunksOK_one c620) (chunksOK_one c621)) (chunksOK_append (chunksOK_one c622) (chunksOK_one c623)))))

end C38

namespace C39

theorem c624 : check 60 115 20 624 = true := by decide +kernel
theorem c625 : check 60 115 20 625 = true := by decide +kernel
theorem c626 : check 60 115 20 626 = true := by decide +kernel
theorem c627 : check 60 115 20 627 = true := by decide +kernel
theorem c628 : check 60 115 20 628 = true := by decide +kernel
theorem c629 : check 60 115 20 629 = true := by decide +kernel
theorem c630 : check 60 115 20 630 = true := by decide +kernel
theorem c631 : check 60 115 20 631 = true := by decide +kernel
theorem c632 : check 60 115 20 632 = true := by decide +kernel
theorem c633 : check 60 115 20 633 = true := by decide +kernel
theorem c634 : check 60 115 20 634 = true := by decide +kernel
theorem c635 : check 60 115 20 635 = true := by decide +kernel
theorem c636 : check 60 115 20 636 = true := by decide +kernel
theorem c637 : check 60 115 20 637 = true := by decide +kernel
theorem c638 : check 60 115 20 638 = true := by decide +kernel
theorem c639 : check 60 115 20 639 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 624 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c624) (chunksOK_one c625)) (chunksOK_append (chunksOK_one c626) (chunksOK_one c627))) (chunksOK_append (chunksOK_append (chunksOK_one c628) (chunksOK_one c629)) (chunksOK_append (chunksOK_one c630) (chunksOK_one c631)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c632) (chunksOK_one c633)) (chunksOK_append (chunksOK_one c634) (chunksOK_one c635))) (chunksOK_append (chunksOK_append (chunksOK_one c636) (chunksOK_one c637)) (chunksOK_append (chunksOK_one c638) (chunksOK_one c639)))))

end C39

namespace C40

theorem c640 : check 60 115 20 640 = true := by decide +kernel
theorem c641 : check 60 115 20 641 = true := by decide +kernel
theorem c642 : check 60 115 20 642 = true := by decide +kernel
theorem c643 : check 60 115 20 643 = true := by decide +kernel
theorem c644 : check 60 115 20 644 = true := by decide +kernel
theorem c645 : check 60 115 20 645 = true := by decide +kernel
theorem c646 : check 60 115 20 646 = true := by decide +kernel
theorem c647 : check 60 115 20 647 = true := by decide +kernel
theorem c648 : check 60 115 20 648 = true := by decide +kernel
theorem c649 : check 60 115 20 649 = true := by decide +kernel
theorem c650 : check 60 115 20 650 = true := by decide +kernel
theorem c651 : check 60 115 20 651 = true := by decide +kernel
theorem c652 : check 60 115 20 652 = true := by decide +kernel
theorem c653 : check 60 115 20 653 = true := by decide +kernel
theorem c654 : check 60 115 20 654 = true := by decide +kernel
theorem c655 : check 60 115 20 655 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 640 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c640) (chunksOK_one c641)) (chunksOK_append (chunksOK_one c642) (chunksOK_one c643))) (chunksOK_append (chunksOK_append (chunksOK_one c644) (chunksOK_one c645)) (chunksOK_append (chunksOK_one c646) (chunksOK_one c647)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c648) (chunksOK_one c649)) (chunksOK_append (chunksOK_one c650) (chunksOK_one c651))) (chunksOK_append (chunksOK_append (chunksOK_one c652) (chunksOK_one c653)) (chunksOK_append (chunksOK_one c654) (chunksOK_one c655)))))

end C40

namespace C41

theorem c656 : check 60 115 20 656 = true := by decide +kernel
theorem c657 : check 60 115 20 657 = true := by decide +kernel
theorem c658 : check 60 115 20 658 = true := by decide +kernel
theorem c659 : check 60 115 20 659 = true := by decide +kernel
theorem c660 : check 60 115 20 660 = true := by decide +kernel
theorem c661 : check 60 115 20 661 = true := by decide +kernel
theorem c662 : check 60 115 20 662 = true := by decide +kernel
theorem c663 : check 60 115 20 663 = true := by decide +kernel
theorem c664 : check 60 115 20 664 = true := by decide +kernel
theorem c665 : check 60 115 20 665 = true := by decide +kernel
theorem c666 : check 60 115 20 666 = true := by decide +kernel
theorem c667 : check 60 115 20 667 = true := by decide +kernel
theorem c668 : check 60 115 20 668 = true := by decide +kernel
theorem c669 : check 60 115 20 669 = true := by decide +kernel
theorem c670 : check 60 115 20 670 = true := by decide +kernel
theorem c671 : check 60 115 20 671 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 656 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c656) (chunksOK_one c657)) (chunksOK_append (chunksOK_one c658) (chunksOK_one c659))) (chunksOK_append (chunksOK_append (chunksOK_one c660) (chunksOK_one c661)) (chunksOK_append (chunksOK_one c662) (chunksOK_one c663)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c664) (chunksOK_one c665)) (chunksOK_append (chunksOK_one c666) (chunksOK_one c667))) (chunksOK_append (chunksOK_append (chunksOK_one c668) (chunksOK_one c669)) (chunksOK_append (chunksOK_one c670) (chunksOK_one c671)))))

end C41

namespace C42

theorem c672 : check 60 115 20 672 = true := by decide +kernel
theorem c673 : check 60 115 20 673 = true := by decide +kernel
theorem c674 : check 60 115 20 674 = true := by decide +kernel
theorem c675 : check 60 115 20 675 = true := by decide +kernel
theorem c676 : check 60 115 20 676 = true := by decide +kernel
theorem c677 : check 60 115 20 677 = true := by decide +kernel
theorem c678 : check 60 115 20 678 = true := by decide +kernel
theorem c679 : check 60 115 20 679 = true := by decide +kernel
theorem c680 : check 60 115 20 680 = true := by decide +kernel
theorem c681 : check 60 115 20 681 = true := by decide +kernel
theorem c682 : check 60 115 20 682 = true := by decide +kernel
theorem c683 : check 60 115 20 683 = true := by decide +kernel
theorem c684 : check 60 115 20 684 = true := by decide +kernel
theorem c685 : check 60 115 20 685 = true := by decide +kernel
theorem c686 : check 60 115 20 686 = true := by decide +kernel
theorem c687 : check 60 115 20 687 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 672 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c672) (chunksOK_one c673)) (chunksOK_append (chunksOK_one c674) (chunksOK_one c675))) (chunksOK_append (chunksOK_append (chunksOK_one c676) (chunksOK_one c677)) (chunksOK_append (chunksOK_one c678) (chunksOK_one c679)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c680) (chunksOK_one c681)) (chunksOK_append (chunksOK_one c682) (chunksOK_one c683))) (chunksOK_append (chunksOK_append (chunksOK_one c684) (chunksOK_one c685)) (chunksOK_append (chunksOK_one c686) (chunksOK_one c687)))))

end C42

namespace C43

theorem c688 : check 60 115 20 688 = true := by decide +kernel
theorem c689 : check 60 115 20 689 = true := by decide +kernel
theorem c690 : check 60 115 20 690 = true := by decide +kernel
theorem c691 : check 60 115 20 691 = true := by decide +kernel
theorem c692 : check 60 115 20 692 = true := by decide +kernel
theorem c693 : check 60 115 20 693 = true := by decide +kernel
theorem c694 : check 60 115 20 694 = true := by decide +kernel
theorem c695 : check 60 115 20 695 = true := by decide +kernel
theorem c696 : check 60 115 20 696 = true := by decide +kernel
theorem c697 : check 60 115 20 697 = true := by decide +kernel
theorem c698 : check 60 115 20 698 = true := by decide +kernel
theorem c699 : check 60 115 20 699 = true := by decide +kernel
theorem c700 : check 60 115 20 700 = true := by decide +kernel
theorem c701 : check 60 115 20 701 = true := by decide +kernel
theorem c702 : check 60 115 20 702 = true := by decide +kernel
theorem c703 : check 60 115 20 703 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 688 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c688) (chunksOK_one c689)) (chunksOK_append (chunksOK_one c690) (chunksOK_one c691))) (chunksOK_append (chunksOK_append (chunksOK_one c692) (chunksOK_one c693)) (chunksOK_append (chunksOK_one c694) (chunksOK_one c695)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c696) (chunksOK_one c697)) (chunksOK_append (chunksOK_one c698) (chunksOK_one c699))) (chunksOK_append (chunksOK_append (chunksOK_one c700) (chunksOK_one c701)) (chunksOK_append (chunksOK_one c702) (chunksOK_one c703)))))

end C43

namespace C44

theorem c704 : check 60 115 20 704 = true := by decide +kernel
theorem c705 : check 60 115 20 705 = true := by decide +kernel
theorem c706 : check 60 115 20 706 = true := by decide +kernel
theorem c707 : check 60 115 20 707 = true := by decide +kernel
theorem c708 : check 60 115 20 708 = true := by decide +kernel
theorem c709 : check 60 115 20 709 = true := by decide +kernel
theorem c710 : check 60 115 20 710 = true := by decide +kernel
theorem c711 : check 60 115 20 711 = true := by decide +kernel
theorem c712 : check 60 115 20 712 = true := by decide +kernel
theorem c713 : check 60 115 20 713 = true := by decide +kernel
theorem c714 : check 60 115 20 714 = true := by decide +kernel
theorem c715 : check 60 115 20 715 = true := by decide +kernel
theorem c716 : check 60 115 20 716 = true := by decide +kernel
theorem c717 : check 60 115 20 717 = true := by decide +kernel
theorem c718 : check 60 115 20 718 = true := by decide +kernel
theorem c719 : check 60 115 20 719 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 704 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c704) (chunksOK_one c705)) (chunksOK_append (chunksOK_one c706) (chunksOK_one c707))) (chunksOK_append (chunksOK_append (chunksOK_one c708) (chunksOK_one c709)) (chunksOK_append (chunksOK_one c710) (chunksOK_one c711)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c712) (chunksOK_one c713)) (chunksOK_append (chunksOK_one c714) (chunksOK_one c715))) (chunksOK_append (chunksOK_append (chunksOK_one c716) (chunksOK_one c717)) (chunksOK_append (chunksOK_one c718) (chunksOK_one c719)))))

end C44

namespace C45

theorem c720 : check 60 115 20 720 = true := by decide +kernel
theorem c721 : check 60 115 20 721 = true := by decide +kernel
theorem c722 : check 60 115 20 722 = true := by decide +kernel
theorem c723 : check 60 115 20 723 = true := by decide +kernel
theorem c724 : check 60 115 20 724 = true := by decide +kernel
theorem c725 : check 60 115 20 725 = true := by decide +kernel
theorem c726 : check 60 115 20 726 = true := by decide +kernel
theorem c727 : check 60 115 20 727 = true := by decide +kernel
theorem c728 : check 60 115 20 728 = true := by decide +kernel
theorem c729 : check 60 115 20 729 = true := by decide +kernel
theorem c730 : check 60 115 20 730 = true := by decide +kernel
theorem c731 : check 60 115 20 731 = true := by decide +kernel
theorem c732 : check 60 115 20 732 = true := by decide +kernel
theorem c733 : check 60 115 20 733 = true := by decide +kernel
theorem c734 : check 60 115 20 734 = true := by decide +kernel
theorem c735 : check 60 115 20 735 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 720 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c720) (chunksOK_one c721)) (chunksOK_append (chunksOK_one c722) (chunksOK_one c723))) (chunksOK_append (chunksOK_append (chunksOK_one c724) (chunksOK_one c725)) (chunksOK_append (chunksOK_one c726) (chunksOK_one c727)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c728) (chunksOK_one c729)) (chunksOK_append (chunksOK_one c730) (chunksOK_one c731))) (chunksOK_append (chunksOK_append (chunksOK_one c732) (chunksOK_one c733)) (chunksOK_append (chunksOK_one c734) (chunksOK_one c735)))))

end C45

namespace C46

theorem c736 : check 60 115 20 736 = true := by decide +kernel
theorem c737 : check 60 115 20 737 = true := by decide +kernel
theorem c738 : check 60 115 20 738 = true := by decide +kernel
theorem c739 : check 60 115 20 739 = true := by decide +kernel
theorem c740 : check 60 115 20 740 = true := by decide +kernel
theorem c741 : check 60 115 20 741 = true := by decide +kernel
theorem c742 : check 60 115 20 742 = true := by decide +kernel
theorem c743 : check 60 115 20 743 = true := by decide +kernel
theorem c744 : check 60 115 20 744 = true := by decide +kernel
theorem c745 : check 60 115 20 745 = true := by decide +kernel
theorem c746 : check 60 115 20 746 = true := by decide +kernel
theorem c747 : check 60 115 20 747 = true := by decide +kernel
theorem c748 : check 60 115 20 748 = true := by decide +kernel
theorem c749 : check 60 115 20 749 = true := by decide +kernel
theorem c750 : check 60 115 20 750 = true := by decide +kernel
theorem c751 : check 60 115 20 751 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 736 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c736) (chunksOK_one c737)) (chunksOK_append (chunksOK_one c738) (chunksOK_one c739))) (chunksOK_append (chunksOK_append (chunksOK_one c740) (chunksOK_one c741)) (chunksOK_append (chunksOK_one c742) (chunksOK_one c743)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c744) (chunksOK_one c745)) (chunksOK_append (chunksOK_one c746) (chunksOK_one c747))) (chunksOK_append (chunksOK_append (chunksOK_one c748) (chunksOK_one c749)) (chunksOK_append (chunksOK_one c750) (chunksOK_one c751)))))

end C46

namespace C47

theorem c752 : check 60 115 20 752 = true := by decide +kernel
theorem c753 : check 60 115 20 753 = true := by decide +kernel
theorem c754 : check 60 115 20 754 = true := by decide +kernel
theorem c755 : check 60 115 20 755 = true := by decide +kernel
theorem c756 : check 60 115 20 756 = true := by decide +kernel
theorem c757 : check 60 115 20 757 = true := by decide +kernel
theorem c758 : check 60 115 20 758 = true := by decide +kernel
theorem c759 : check 60 115 20 759 = true := by decide +kernel
theorem c760 : check 60 115 20 760 = true := by decide +kernel
theorem c761 : check 60 115 20 761 = true := by decide +kernel
theorem c762 : check 60 115 20 762 = true := by decide +kernel
theorem c763 : check 60 115 20 763 = true := by decide +kernel
theorem c764 : check 60 115 20 764 = true := by decide +kernel
theorem c765 : check 60 115 20 765 = true := by decide +kernel
theorem c766 : check 60 115 20 766 = true := by decide +kernel
theorem c767 : check 60 115 20 767 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 752 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c752) (chunksOK_one c753)) (chunksOK_append (chunksOK_one c754) (chunksOK_one c755))) (chunksOK_append (chunksOK_append (chunksOK_one c756) (chunksOK_one c757)) (chunksOK_append (chunksOK_one c758) (chunksOK_one c759)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c760) (chunksOK_one c761)) (chunksOK_append (chunksOK_one c762) (chunksOK_one c763))) (chunksOK_append (chunksOK_append (chunksOK_one c764) (chunksOK_one c765)) (chunksOK_append (chunksOK_one c766) (chunksOK_one c767)))))

end C47

namespace C48

theorem c768 : check 60 115 20 768 = true := by decide +kernel
theorem c769 : check 60 115 20 769 = true := by decide +kernel
theorem c770 : check 60 115 20 770 = true := by decide +kernel
theorem c771 : check 60 115 20 771 = true := by decide +kernel
theorem c772 : check 60 115 20 772 = true := by decide +kernel
theorem c773 : check 60 115 20 773 = true := by decide +kernel
theorem c774 : check 60 115 20 774 = true := by decide +kernel
theorem c775 : check 60 115 20 775 = true := by decide +kernel
theorem c776 : check 60 115 20 776 = true := by decide +kernel
theorem c777 : check 60 115 20 777 = true := by decide +kernel
theorem c778 : check 60 115 20 778 = true := by decide +kernel
theorem c779 : check 60 115 20 779 = true := by decide +kernel
theorem c780 : check 60 115 20 780 = true := by decide +kernel
theorem c781 : check 60 115 20 781 = true := by decide +kernel
theorem c782 : check 60 115 20 782 = true := by decide +kernel
theorem c783 : check 60 115 20 783 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 768 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c768) (chunksOK_one c769)) (chunksOK_append (chunksOK_one c770) (chunksOK_one c771))) (chunksOK_append (chunksOK_append (chunksOK_one c772) (chunksOK_one c773)) (chunksOK_append (chunksOK_one c774) (chunksOK_one c775)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c776) (chunksOK_one c777)) (chunksOK_append (chunksOK_one c778) (chunksOK_one c779))) (chunksOK_append (chunksOK_append (chunksOK_one c780) (chunksOK_one c781)) (chunksOK_append (chunksOK_one c782) (chunksOK_one c783)))))

end C48

namespace C49

theorem c784 : check 60 115 20 784 = true := by decide +kernel
theorem c785 : check 60 115 20 785 = true := by decide +kernel
theorem c786 : check 60 115 20 786 = true := by decide +kernel
theorem c787 : check 60 115 20 787 = true := by decide +kernel
theorem c788 : check 60 115 20 788 = true := by decide +kernel
theorem c789 : check 60 115 20 789 = true := by decide +kernel
theorem c790 : check 60 115 20 790 = true := by decide +kernel
theorem c791 : check 60 115 20 791 = true := by decide +kernel
theorem c792 : check 60 115 20 792 = true := by decide +kernel
theorem c793 : check 60 115 20 793 = true := by decide +kernel
theorem c794 : check 60 115 20 794 = true := by decide +kernel
theorem c795 : check 60 115 20 795 = true := by decide +kernel
theorem c796 : check 60 115 20 796 = true := by decide +kernel
theorem c797 : check 60 115 20 797 = true := by decide +kernel
theorem c798 : check 60 115 20 798 = true := by decide +kernel
theorem c799 : check 60 115 20 799 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 784 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c784) (chunksOK_one c785)) (chunksOK_append (chunksOK_one c786) (chunksOK_one c787))) (chunksOK_append (chunksOK_append (chunksOK_one c788) (chunksOK_one c789)) (chunksOK_append (chunksOK_one c790) (chunksOK_one c791)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c792) (chunksOK_one c793)) (chunksOK_append (chunksOK_one c794) (chunksOK_one c795))) (chunksOK_append (chunksOK_append (chunksOK_one c796) (chunksOK_one c797)) (chunksOK_append (chunksOK_one c798) (chunksOK_one c799)))))

end C49

namespace C50

theorem c800 : check 60 115 20 800 = true := by decide +kernel
theorem c801 : check 60 115 20 801 = true := by decide +kernel
theorem c802 : check 60 115 20 802 = true := by decide +kernel
theorem c803 : check 60 115 20 803 = true := by decide +kernel
theorem c804 : check 60 115 20 804 = true := by decide +kernel
theorem c805 : check 60 115 20 805 = true := by decide +kernel
theorem c806 : check 60 115 20 806 = true := by decide +kernel
theorem c807 : check 60 115 20 807 = true := by decide +kernel
theorem c808 : check 60 115 20 808 = true := by decide +kernel
theorem c809 : check 60 115 20 809 = true := by decide +kernel
theorem c810 : check 60 115 20 810 = true := by decide +kernel
theorem c811 : check 60 115 20 811 = true := by decide +kernel
theorem c812 : check 60 115 20 812 = true := by decide +kernel
theorem c813 : check 60 115 20 813 = true := by decide +kernel
theorem c814 : check 60 115 20 814 = true := by decide +kernel
theorem c815 : check 60 115 20 815 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 800 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c800) (chunksOK_one c801)) (chunksOK_append (chunksOK_one c802) (chunksOK_one c803))) (chunksOK_append (chunksOK_append (chunksOK_one c804) (chunksOK_one c805)) (chunksOK_append (chunksOK_one c806) (chunksOK_one c807)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c808) (chunksOK_one c809)) (chunksOK_append (chunksOK_one c810) (chunksOK_one c811))) (chunksOK_append (chunksOK_append (chunksOK_one c812) (chunksOK_one c813)) (chunksOK_append (chunksOK_one c814) (chunksOK_one c815)))))

end C50

namespace C51

theorem c816 : check 60 115 20 816 = true := by decide +kernel
theorem c817 : check 60 115 20 817 = true := by decide +kernel
theorem c818 : check 60 115 20 818 = true := by decide +kernel
theorem c819 : check 60 115 20 819 = true := by decide +kernel
theorem c820 : check 60 115 20 820 = true := by decide +kernel
theorem c821 : check 60 115 20 821 = true := by decide +kernel
theorem c822 : check 60 115 20 822 = true := by decide +kernel
theorem c823 : check 60 115 20 823 = true := by decide +kernel
theorem c824 : check 60 115 20 824 = true := by decide +kernel
theorem c825 : check 60 115 20 825 = true := by decide +kernel
theorem c826 : check 60 115 20 826 = true := by decide +kernel
theorem c827 : check 60 115 20 827 = true := by decide +kernel
theorem c828 : check 60 115 20 828 = true := by decide +kernel
theorem c829 : check 60 115 20 829 = true := by decide +kernel
theorem c830 : check 60 115 20 830 = true := by decide +kernel
theorem c831 : check 60 115 20 831 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 816 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c816) (chunksOK_one c817)) (chunksOK_append (chunksOK_one c818) (chunksOK_one c819))) (chunksOK_append (chunksOK_append (chunksOK_one c820) (chunksOK_one c821)) (chunksOK_append (chunksOK_one c822) (chunksOK_one c823)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c824) (chunksOK_one c825)) (chunksOK_append (chunksOK_one c826) (chunksOK_one c827))) (chunksOK_append (chunksOK_append (chunksOK_one c828) (chunksOK_one c829)) (chunksOK_append (chunksOK_one c830) (chunksOK_one c831)))))

end C51

namespace C52

theorem c832 : check 60 115 20 832 = true := by decide +kernel
theorem c833 : check 60 115 20 833 = true := by decide +kernel
theorem c834 : check 60 115 20 834 = true := by decide +kernel
theorem c835 : check 60 115 20 835 = true := by decide +kernel
theorem c836 : check 60 115 20 836 = true := by decide +kernel
theorem c837 : check 60 115 20 837 = true := by decide +kernel
theorem c838 : check 60 115 20 838 = true := by decide +kernel
theorem c839 : check 60 115 20 839 = true := by decide +kernel
theorem c840 : check 60 115 20 840 = true := by decide +kernel
theorem c841 : check 60 115 20 841 = true := by decide +kernel
theorem c842 : check 60 115 20 842 = true := by decide +kernel
theorem c843 : check 60 115 20 843 = true := by decide +kernel
theorem c844 : check 60 115 20 844 = true := by decide +kernel
theorem c845 : check 60 115 20 845 = true := by decide +kernel
theorem c846 : check 60 115 20 846 = true := by decide +kernel
theorem c847 : check 60 115 20 847 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 832 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c832) (chunksOK_one c833)) (chunksOK_append (chunksOK_one c834) (chunksOK_one c835))) (chunksOK_append (chunksOK_append (chunksOK_one c836) (chunksOK_one c837)) (chunksOK_append (chunksOK_one c838) (chunksOK_one c839)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c840) (chunksOK_one c841)) (chunksOK_append (chunksOK_one c842) (chunksOK_one c843))) (chunksOK_append (chunksOK_append (chunksOK_one c844) (chunksOK_one c845)) (chunksOK_append (chunksOK_one c846) (chunksOK_one c847)))))

end C52

namespace C53

theorem c848 : check 60 115 20 848 = true := by decide +kernel
theorem c849 : check 60 115 20 849 = true := by decide +kernel
theorem c850 : check 60 115 20 850 = true := by decide +kernel
theorem c851 : check 60 115 20 851 = true := by decide +kernel
theorem c852 : check 60 115 20 852 = true := by decide +kernel
theorem c853 : check 60 115 20 853 = true := by decide +kernel
theorem c854 : check 60 115 20 854 = true := by decide +kernel
theorem c855 : check 60 115 20 855 = true := by decide +kernel
theorem c856 : check 60 115 20 856 = true := by decide +kernel
theorem c857 : check 60 115 20 857 = true := by decide +kernel
theorem c858 : check 60 115 20 858 = true := by decide +kernel
theorem c859 : check 60 115 20 859 = true := by decide +kernel
theorem c860 : check 60 115 20 860 = true := by decide +kernel
theorem c861 : check 60 115 20 861 = true := by decide +kernel
theorem c862 : check 60 115 20 862 = true := by decide +kernel
theorem c863 : check 60 115 20 863 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 848 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c848) (chunksOK_one c849)) (chunksOK_append (chunksOK_one c850) (chunksOK_one c851))) (chunksOK_append (chunksOK_append (chunksOK_one c852) (chunksOK_one c853)) (chunksOK_append (chunksOK_one c854) (chunksOK_one c855)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c856) (chunksOK_one c857)) (chunksOK_append (chunksOK_one c858) (chunksOK_one c859))) (chunksOK_append (chunksOK_append (chunksOK_one c860) (chunksOK_one c861)) (chunksOK_append (chunksOK_one c862) (chunksOK_one c863)))))

end C53

namespace C54

theorem c864 : check 60 115 20 864 = true := by decide +kernel
theorem c865 : check 60 115 20 865 = true := by decide +kernel
theorem c866 : check 60 115 20 866 = true := by decide +kernel
theorem c867 : check 60 115 20 867 = true := by decide +kernel
theorem c868 : check 60 115 20 868 = true := by decide +kernel
theorem c869 : check 60 115 20 869 = true := by decide +kernel
theorem c870 : check 60 115 20 870 = true := by decide +kernel
theorem c871 : check 60 115 20 871 = true := by decide +kernel
theorem c872 : check 60 115 20 872 = true := by decide +kernel
theorem c873 : check 60 115 20 873 = true := by decide +kernel
theorem c874 : check 60 115 20 874 = true := by decide +kernel
theorem c875 : check 60 115 20 875 = true := by decide +kernel
theorem c876 : check 60 115 20 876 = true := by decide +kernel
theorem c877 : check 60 115 20 877 = true := by decide +kernel
theorem c878 : check 60 115 20 878 = true := by decide +kernel
theorem c879 : check 60 115 20 879 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 864 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c864) (chunksOK_one c865)) (chunksOK_append (chunksOK_one c866) (chunksOK_one c867))) (chunksOK_append (chunksOK_append (chunksOK_one c868) (chunksOK_one c869)) (chunksOK_append (chunksOK_one c870) (chunksOK_one c871)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c872) (chunksOK_one c873)) (chunksOK_append (chunksOK_one c874) (chunksOK_one c875))) (chunksOK_append (chunksOK_append (chunksOK_one c876) (chunksOK_one c877)) (chunksOK_append (chunksOK_one c878) (chunksOK_one c879)))))

end C54

namespace C55

theorem c880 : check 60 115 20 880 = true := by decide +kernel
theorem c881 : check 60 115 20 881 = true := by decide +kernel
theorem c882 : check 60 115 20 882 = true := by decide +kernel
theorem c883 : check 60 115 20 883 = true := by decide +kernel
theorem c884 : check 60 115 20 884 = true := by decide +kernel
theorem c885 : check 60 115 20 885 = true := by decide +kernel
theorem c886 : check 60 115 20 886 = true := by decide +kernel
theorem c887 : check 60 115 20 887 = true := by decide +kernel
theorem c888 : check 60 115 20 888 = true := by decide +kernel
theorem c889 : check 60 115 20 889 = true := by decide +kernel
theorem c890 : check 60 115 20 890 = true := by decide +kernel
theorem c891 : check 60 115 20 891 = true := by decide +kernel
theorem c892 : check 60 115 20 892 = true := by decide +kernel
theorem c893 : check 60 115 20 893 = true := by decide +kernel
theorem c894 : check 60 115 20 894 = true := by decide +kernel
theorem c895 : check 60 115 20 895 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 880 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c880) (chunksOK_one c881)) (chunksOK_append (chunksOK_one c882) (chunksOK_one c883))) (chunksOK_append (chunksOK_append (chunksOK_one c884) (chunksOK_one c885)) (chunksOK_append (chunksOK_one c886) (chunksOK_one c887)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c888) (chunksOK_one c889)) (chunksOK_append (chunksOK_one c890) (chunksOK_one c891))) (chunksOK_append (chunksOK_append (chunksOK_one c892) (chunksOK_one c893)) (chunksOK_append (chunksOK_one c894) (chunksOK_one c895)))))

end C55

namespace C56

theorem c896 : check 60 115 20 896 = true := by decide +kernel
theorem c897 : check 60 115 20 897 = true := by decide +kernel
theorem c898 : check 60 115 20 898 = true := by decide +kernel
theorem c899 : check 60 115 20 899 = true := by decide +kernel
theorem c900 : check 60 115 20 900 = true := by decide +kernel
theorem c901 : check 60 115 20 901 = true := by decide +kernel
theorem c902 : check 60 115 20 902 = true := by decide +kernel
theorem c903 : check 60 115 20 903 = true := by decide +kernel
theorem c904 : check 60 115 20 904 = true := by decide +kernel
theorem c905 : check 60 115 20 905 = true := by decide +kernel
theorem c906 : check 60 115 20 906 = true := by decide +kernel
theorem c907 : check 60 115 20 907 = true := by decide +kernel
theorem c908 : check 60 115 20 908 = true := by decide +kernel
theorem c909 : check 60 115 20 909 = true := by decide +kernel
theorem c910 : check 60 115 20 910 = true := by decide +kernel
theorem c911 : check 60 115 20 911 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 896 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c896) (chunksOK_one c897)) (chunksOK_append (chunksOK_one c898) (chunksOK_one c899))) (chunksOK_append (chunksOK_append (chunksOK_one c900) (chunksOK_one c901)) (chunksOK_append (chunksOK_one c902) (chunksOK_one c903)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c904) (chunksOK_one c905)) (chunksOK_append (chunksOK_one c906) (chunksOK_one c907))) (chunksOK_append (chunksOK_append (chunksOK_one c908) (chunksOK_one c909)) (chunksOK_append (chunksOK_one c910) (chunksOK_one c911)))))

end C56

namespace C57

theorem c912 : check 60 115 20 912 = true := by decide +kernel
theorem c913 : check 60 115 20 913 = true := by decide +kernel
theorem c914 : check 60 115 20 914 = true := by decide +kernel
theorem c915 : check 60 115 20 915 = true := by decide +kernel
theorem c916 : check 60 115 20 916 = true := by decide +kernel
theorem c917 : check 60 115 20 917 = true := by decide +kernel
theorem c918 : check 60 115 20 918 = true := by decide +kernel
theorem c919 : check 60 115 20 919 = true := by decide +kernel
theorem c920 : check 60 115 20 920 = true := by decide +kernel
theorem c921 : check 60 115 20 921 = true := by decide +kernel
theorem c922 : check 60 115 20 922 = true := by decide +kernel
theorem c923 : check 60 115 20 923 = true := by decide +kernel
theorem c924 : check 60 115 20 924 = true := by decide +kernel
theorem c925 : check 60 115 20 925 = true := by decide +kernel
theorem c926 : check 60 115 20 926 = true := by decide +kernel
theorem c927 : check 60 115 20 927 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 912 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c912) (chunksOK_one c913)) (chunksOK_append (chunksOK_one c914) (chunksOK_one c915))) (chunksOK_append (chunksOK_append (chunksOK_one c916) (chunksOK_one c917)) (chunksOK_append (chunksOK_one c918) (chunksOK_one c919)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c920) (chunksOK_one c921)) (chunksOK_append (chunksOK_one c922) (chunksOK_one c923))) (chunksOK_append (chunksOK_append (chunksOK_one c924) (chunksOK_one c925)) (chunksOK_append (chunksOK_one c926) (chunksOK_one c927)))))

end C57

namespace C58

theorem c928 : check 60 115 20 928 = true := by decide +kernel
theorem c929 : check 60 115 20 929 = true := by decide +kernel
theorem c930 : check 60 115 20 930 = true := by decide +kernel
theorem c931 : check 60 115 20 931 = true := by decide +kernel
theorem c932 : check 60 115 20 932 = true := by decide +kernel
theorem c933 : check 60 115 20 933 = true := by decide +kernel
theorem c934 : check 60 115 20 934 = true := by decide +kernel
theorem c935 : check 60 115 20 935 = true := by decide +kernel
theorem c936 : check 60 115 20 936 = true := by decide +kernel
theorem c937 : check 60 115 20 937 = true := by decide +kernel
theorem c938 : check 60 115 20 938 = true := by decide +kernel
theorem c939 : check 60 115 20 939 = true := by decide +kernel
theorem c940 : check 60 115 20 940 = true := by decide +kernel
theorem c941 : check 60 115 20 941 = true := by decide +kernel
theorem c942 : check 60 115 20 942 = true := by decide +kernel
theorem c943 : check 60 115 20 943 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 928 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c928) (chunksOK_one c929)) (chunksOK_append (chunksOK_one c930) (chunksOK_one c931))) (chunksOK_append (chunksOK_append (chunksOK_one c932) (chunksOK_one c933)) (chunksOK_append (chunksOK_one c934) (chunksOK_one c935)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c936) (chunksOK_one c937)) (chunksOK_append (chunksOK_one c938) (chunksOK_one c939))) (chunksOK_append (chunksOK_append (chunksOK_one c940) (chunksOK_one c941)) (chunksOK_append (chunksOK_one c942) (chunksOK_one c943)))))

end C58

namespace C59

theorem c944 : check 60 115 20 944 = true := by decide +kernel
theorem c945 : check 60 115 20 945 = true := by decide +kernel
theorem c946 : check 60 115 20 946 = true := by decide +kernel
theorem c947 : check 60 115 20 947 = true := by decide +kernel
theorem c948 : check 60 115 20 948 = true := by decide +kernel
theorem c949 : check 60 115 20 949 = true := by decide +kernel
theorem c950 : check 60 115 20 950 = true := by decide +kernel
theorem c951 : check 60 115 20 951 = true := by decide +kernel
theorem c952 : check 60 115 20 952 = true := by decide +kernel
theorem c953 : check 60 115 20 953 = true := by decide +kernel
theorem c954 : check 60 115 20 954 = true := by decide +kernel
theorem c955 : check 60 115 20 955 = true := by decide +kernel
theorem c956 : check 60 115 20 956 = true := by decide +kernel
theorem c957 : check 60 115 20 957 = true := by decide +kernel
theorem c958 : check 60 115 20 958 = true := by decide +kernel
theorem c959 : check 60 115 20 959 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 944 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c944) (chunksOK_one c945)) (chunksOK_append (chunksOK_one c946) (chunksOK_one c947))) (chunksOK_append (chunksOK_append (chunksOK_one c948) (chunksOK_one c949)) (chunksOK_append (chunksOK_one c950) (chunksOK_one c951)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c952) (chunksOK_one c953)) (chunksOK_append (chunksOK_one c954) (chunksOK_one c955))) (chunksOK_append (chunksOK_append (chunksOK_one c956) (chunksOK_one c957)) (chunksOK_append (chunksOK_one c958) (chunksOK_one c959)))))

end C59

namespace C60

theorem c960 : check 60 115 20 960 = true := by decide +kernel
theorem c961 : check 60 115 20 961 = true := by decide +kernel
theorem c962 : check 60 115 20 962 = true := by decide +kernel
theorem c963 : check 60 115 20 963 = true := by decide +kernel
theorem c964 : check 60 115 20 964 = true := by decide +kernel
theorem c965 : check 60 115 20 965 = true := by decide +kernel
theorem c966 : check 60 115 20 966 = true := by decide +kernel
theorem c967 : check 60 115 20 967 = true := by decide +kernel
theorem c968 : check 60 115 20 968 = true := by decide +kernel
theorem c969 : check 60 115 20 969 = true := by decide +kernel
theorem c970 : check 60 115 20 970 = true := by decide +kernel
theorem c971 : check 60 115 20 971 = true := by decide +kernel
theorem c972 : check 60 115 20 972 = true := by decide +kernel
theorem c973 : check 60 115 20 973 = true := by decide +kernel
theorem c974 : check 60 115 20 974 = true := by decide +kernel
theorem c975 : check 60 115 20 975 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 960 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c960) (chunksOK_one c961)) (chunksOK_append (chunksOK_one c962) (chunksOK_one c963))) (chunksOK_append (chunksOK_append (chunksOK_one c964) (chunksOK_one c965)) (chunksOK_append (chunksOK_one c966) (chunksOK_one c967)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c968) (chunksOK_one c969)) (chunksOK_append (chunksOK_one c970) (chunksOK_one c971))) (chunksOK_append (chunksOK_append (chunksOK_one c972) (chunksOK_one c973)) (chunksOK_append (chunksOK_one c974) (chunksOK_one c975)))))

end C60

namespace C61

theorem c976 : check 60 115 20 976 = true := by decide +kernel
theorem c977 : check 60 115 20 977 = true := by decide +kernel
theorem c978 : check 60 115 20 978 = true := by decide +kernel
theorem c979 : check 60 115 20 979 = true := by decide +kernel
theorem c980 : check 60 115 20 980 = true := by decide +kernel
theorem c981 : check 60 115 20 981 = true := by decide +kernel
theorem c982 : check 60 115 20 982 = true := by decide +kernel
theorem c983 : check 60 115 20 983 = true := by decide +kernel
theorem c984 : check 60 115 20 984 = true := by decide +kernel
theorem c985 : check 60 115 20 985 = true := by decide +kernel
theorem c986 : check 60 115 20 986 = true := by decide +kernel
theorem c987 : check 60 115 20 987 = true := by decide +kernel
theorem c988 : check 60 115 20 988 = true := by decide +kernel
theorem c989 : check 60 115 20 989 = true := by decide +kernel
theorem c990 : check 60 115 20 990 = true := by decide +kernel
theorem c991 : check 60 115 20 991 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 976 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c976) (chunksOK_one c977)) (chunksOK_append (chunksOK_one c978) (chunksOK_one c979))) (chunksOK_append (chunksOK_append (chunksOK_one c980) (chunksOK_one c981)) (chunksOK_append (chunksOK_one c982) (chunksOK_one c983)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c984) (chunksOK_one c985)) (chunksOK_append (chunksOK_one c986) (chunksOK_one c987))) (chunksOK_append (chunksOK_append (chunksOK_one c988) (chunksOK_one c989)) (chunksOK_append (chunksOK_one c990) (chunksOK_one c991)))))

end C61

namespace C62

theorem c992 : check 60 115 20 992 = true := by decide +kernel
theorem c993 : check 60 115 20 993 = true := by decide +kernel
theorem c994 : check 60 115 20 994 = true := by decide +kernel
theorem c995 : check 60 115 20 995 = true := by decide +kernel
theorem c996 : check 60 115 20 996 = true := by decide +kernel
theorem c997 : check 60 115 20 997 = true := by decide +kernel
theorem c998 : check 60 115 20 998 = true := by decide +kernel
theorem c999 : check 60 115 20 999 = true := by decide +kernel
theorem c1000 : check 60 115 20 1000 = true := by decide +kernel
theorem c1001 : check 60 115 20 1001 = true := by decide +kernel
theorem c1002 : check 60 115 20 1002 = true := by decide +kernel
theorem c1003 : check 60 115 20 1003 = true := by decide +kernel
theorem c1004 : check 60 115 20 1004 = true := by decide +kernel
theorem c1005 : check 60 115 20 1005 = true := by decide +kernel
theorem c1006 : check 60 115 20 1006 = true := by decide +kernel
theorem c1007 : check 60 115 20 1007 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 992 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c992) (chunksOK_one c993)) (chunksOK_append (chunksOK_one c994) (chunksOK_one c995))) (chunksOK_append (chunksOK_append (chunksOK_one c996) (chunksOK_one c997)) (chunksOK_append (chunksOK_one c998) (chunksOK_one c999)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1000) (chunksOK_one c1001)) (chunksOK_append (chunksOK_one c1002) (chunksOK_one c1003))) (chunksOK_append (chunksOK_append (chunksOK_one c1004) (chunksOK_one c1005)) (chunksOK_append (chunksOK_one c1006) (chunksOK_one c1007)))))

end C62

namespace C63

theorem c1008 : check 60 115 20 1008 = true := by decide +kernel
theorem c1009 : check 60 115 20 1009 = true := by decide +kernel
theorem c1010 : check 60 115 20 1010 = true := by decide +kernel
theorem c1011 : check 60 115 20 1011 = true := by decide +kernel
theorem c1012 : check 60 115 20 1012 = true := by decide +kernel
theorem c1013 : check 60 115 20 1013 = true := by decide +kernel
theorem c1014 : check 60 115 20 1014 = true := by decide +kernel
theorem c1015 : check 60 115 20 1015 = true := by decide +kernel
theorem c1016 : check 60 115 20 1016 = true := by decide +kernel
theorem c1017 : check 60 115 20 1017 = true := by decide +kernel
theorem c1018 : check 60 115 20 1018 = true := by decide +kernel
theorem c1019 : check 60 115 20 1019 = true := by decide +kernel
theorem c1020 : check 60 115 20 1020 = true := by decide +kernel
theorem c1021 : check 60 115 20 1021 = true := by decide +kernel
theorem c1022 : check 60 115 20 1022 = true := by decide +kernel
theorem c1023 : check 60 115 20 1023 = true := by decide +kernel

theorem range : ChunksOK 60 115 20 1008 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1008) (chunksOK_one c1009)) (chunksOK_append (chunksOK_one c1010) (chunksOK_one c1011))) (chunksOK_append (chunksOK_append (chunksOK_one c1012) (chunksOK_one c1013)) (chunksOK_append (chunksOK_one c1014) (chunksOK_one c1015)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1016) (chunksOK_one c1017)) (chunksOK_append (chunksOK_one c1018) (chunksOK_one c1019))) (chunksOK_append (chunksOK_append (chunksOK_one c1020) (chunksOK_one c1021)) (chunksOK_append (chunksOK_one c1022) (chunksOK_one c1023)))))

end C63

/-! ## The assembled upper bound -/

theorem all_chunks : ChunksOK 60 115 20 0 1024 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append C0.range C1.range) (chunksOK_append C2.range C3.range)) (chunksOK_append (chunksOK_append C4.range C5.range) (chunksOK_append C6.range C7.range))) (chunksOK_append (chunksOK_append (chunksOK_append C8.range C9.range) (chunksOK_append C10.range C11.range)) (chunksOK_append (chunksOK_append C12.range C13.range) (chunksOK_append C14.range C15.range)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append C16.range C17.range) (chunksOK_append C18.range C19.range)) (chunksOK_append (chunksOK_append C20.range C21.range) (chunksOK_append C22.range C23.range))) (chunksOK_append (chunksOK_append (chunksOK_append C24.range C25.range) (chunksOK_append C26.range C27.range)) (chunksOK_append (chunksOK_append C28.range C29.range) (chunksOK_append C30.range C31.range))))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append C32.range C33.range) (chunksOK_append C34.range C35.range)) (chunksOK_append (chunksOK_append C36.range C37.range) (chunksOK_append C38.range C39.range))) (chunksOK_append (chunksOK_append (chunksOK_append C40.range C41.range) (chunksOK_append C42.range C43.range)) (chunksOK_append (chunksOK_append C44.range C45.range) (chunksOK_append C46.range C47.range)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append C48.range C49.range) (chunksOK_append C50.range C51.range)) (chunksOK_append (chunksOK_append C52.range C53.range) (chunksOK_append C54.range C55.range))) (chunksOK_append (chunksOK_append (chunksOK_append C56.range C57.range) (chunksOK_append C58.range C59.range)) (chunksOK_append (chunksOK_append C60.range C61.range) (chunksOK_append C62.range C63.range))))))

/-- Every start supported at depths at most 60 has a white depth-1 cell at an even time at most 114. -/
theorem q01_width_le_60 (x : Nat → Bool) (hx : ∀ k, 60 < k → x k = false) :
    ∃ t, t ≤ 114 ∧ t % 2 = 0 ∧ zrow x t 1 = false := by
  obtain ⟨t, ht, he, hz⟩ := q01_of_chunks 60 115 20 (by decide) all_chunks x hx
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
