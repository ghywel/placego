import Rule30PrizeKit
import Ruliology.CellularAutomata.Rule30ZeroBoundarySmall
import Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes

/-!
# The death time at width 56 is exactly 100: a complete chunk certificate and its witness

**Partial result on the kit's `Q01` (the period-2 question, Problem 1 of the Rule 30 Prize).** The kit proves `Q01`
for every zero-boundary start of width at most 52 (`Rule30ZeroBoundaryWidth52`, 256 chunk checks, bound 96) and
mentions that width 56 was also checked privately (1,024 checks, bound 100) and left out for build cost. This module
carries those 1,024 checks (`check 56 101 18 c = true`, each decided by the kernel, in 64 namespaces of 16 with the
kit's `chunksOK_append` trees), assembles them by the kit's `q01_of_chunks` into `q01_width_le_56` (every start of
width at most 56 has a white depth-1 cell at an even time at most 100), and proves the bound exact: the explicit
start `w56` is black at depth 1 at every even time below 100 and white at 100, by the kit's packed evaluator `prun`
and its bridge `run_toFun` (`death_time_56_exact`).

**Provenance.** The chunk text is the W2 generator's of the Wolfram · Collatz · Mahler record (github.com/ghywel/placego,
tests/probes/wolfram/w2_harness.py), whose width-52 regeneration equals the kit's own modules line for line; the
certificate was built and checked by the kit's `Check.lean` on the M5 on 2026-10-23 (CHAT-LEDGER.md L794), the witness
found and validated in lane D-exact (L812, L816). Nothing is claimed for any other width.
-/

set_option Elab.async false

namespace Rule30Submission

open Ruliology.CellularAutomata
open Ruliology.CellularAutomata.Rule30ZeroBoundary
open Ruliology.CellularAutomata.Rule30ZeroBoundarySmall
open Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes

/-! ## The 1,024 chunk checks, kernel-decided -/
namespace C0

theorem c0 : check 56 101 18 0 = true := by decide +kernel
theorem c1 : check 56 101 18 1 = true := by decide +kernel
theorem c2 : check 56 101 18 2 = true := by decide +kernel
theorem c3 : check 56 101 18 3 = true := by decide +kernel
theorem c4 : check 56 101 18 4 = true := by decide +kernel
theorem c5 : check 56 101 18 5 = true := by decide +kernel
theorem c6 : check 56 101 18 6 = true := by decide +kernel
theorem c7 : check 56 101 18 7 = true := by decide +kernel
theorem c8 : check 56 101 18 8 = true := by decide +kernel
theorem c9 : check 56 101 18 9 = true := by decide +kernel
theorem c10 : check 56 101 18 10 = true := by decide +kernel
theorem c11 : check 56 101 18 11 = true := by decide +kernel
theorem c12 : check 56 101 18 12 = true := by decide +kernel
theorem c13 : check 56 101 18 13 = true := by decide +kernel
theorem c14 : check 56 101 18 14 = true := by decide +kernel
theorem c15 : check 56 101 18 15 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 0 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c0) (chunksOK_one c1)) (chunksOK_append (chunksOK_one c2) (chunksOK_one c3))) (chunksOK_append (chunksOK_append (chunksOK_one c4) (chunksOK_one c5)) (chunksOK_append (chunksOK_one c6) (chunksOK_one c7)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c8) (chunksOK_one c9)) (chunksOK_append (chunksOK_one c10) (chunksOK_one c11))) (chunksOK_append (chunksOK_append (chunksOK_one c12) (chunksOK_one c13)) (chunksOK_append (chunksOK_one c14) (chunksOK_one c15)))))

end C0

namespace C1

theorem c16 : check 56 101 18 16 = true := by decide +kernel
theorem c17 : check 56 101 18 17 = true := by decide +kernel
theorem c18 : check 56 101 18 18 = true := by decide +kernel
theorem c19 : check 56 101 18 19 = true := by decide +kernel
theorem c20 : check 56 101 18 20 = true := by decide +kernel
theorem c21 : check 56 101 18 21 = true := by decide +kernel
theorem c22 : check 56 101 18 22 = true := by decide +kernel
theorem c23 : check 56 101 18 23 = true := by decide +kernel
theorem c24 : check 56 101 18 24 = true := by decide +kernel
theorem c25 : check 56 101 18 25 = true := by decide +kernel
theorem c26 : check 56 101 18 26 = true := by decide +kernel
theorem c27 : check 56 101 18 27 = true := by decide +kernel
theorem c28 : check 56 101 18 28 = true := by decide +kernel
theorem c29 : check 56 101 18 29 = true := by decide +kernel
theorem c30 : check 56 101 18 30 = true := by decide +kernel
theorem c31 : check 56 101 18 31 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 16 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c16) (chunksOK_one c17)) (chunksOK_append (chunksOK_one c18) (chunksOK_one c19))) (chunksOK_append (chunksOK_append (chunksOK_one c20) (chunksOK_one c21)) (chunksOK_append (chunksOK_one c22) (chunksOK_one c23)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c24) (chunksOK_one c25)) (chunksOK_append (chunksOK_one c26) (chunksOK_one c27))) (chunksOK_append (chunksOK_append (chunksOK_one c28) (chunksOK_one c29)) (chunksOK_append (chunksOK_one c30) (chunksOK_one c31)))))

end C1

namespace C2

theorem c32 : check 56 101 18 32 = true := by decide +kernel
theorem c33 : check 56 101 18 33 = true := by decide +kernel
theorem c34 : check 56 101 18 34 = true := by decide +kernel
theorem c35 : check 56 101 18 35 = true := by decide +kernel
theorem c36 : check 56 101 18 36 = true := by decide +kernel
theorem c37 : check 56 101 18 37 = true := by decide +kernel
theorem c38 : check 56 101 18 38 = true := by decide +kernel
theorem c39 : check 56 101 18 39 = true := by decide +kernel
theorem c40 : check 56 101 18 40 = true := by decide +kernel
theorem c41 : check 56 101 18 41 = true := by decide +kernel
theorem c42 : check 56 101 18 42 = true := by decide +kernel
theorem c43 : check 56 101 18 43 = true := by decide +kernel
theorem c44 : check 56 101 18 44 = true := by decide +kernel
theorem c45 : check 56 101 18 45 = true := by decide +kernel
theorem c46 : check 56 101 18 46 = true := by decide +kernel
theorem c47 : check 56 101 18 47 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 32 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c32) (chunksOK_one c33)) (chunksOK_append (chunksOK_one c34) (chunksOK_one c35))) (chunksOK_append (chunksOK_append (chunksOK_one c36) (chunksOK_one c37)) (chunksOK_append (chunksOK_one c38) (chunksOK_one c39)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c40) (chunksOK_one c41)) (chunksOK_append (chunksOK_one c42) (chunksOK_one c43))) (chunksOK_append (chunksOK_append (chunksOK_one c44) (chunksOK_one c45)) (chunksOK_append (chunksOK_one c46) (chunksOK_one c47)))))

end C2

namespace C3

theorem c48 : check 56 101 18 48 = true := by decide +kernel
theorem c49 : check 56 101 18 49 = true := by decide +kernel
theorem c50 : check 56 101 18 50 = true := by decide +kernel
theorem c51 : check 56 101 18 51 = true := by decide +kernel
theorem c52 : check 56 101 18 52 = true := by decide +kernel
theorem c53 : check 56 101 18 53 = true := by decide +kernel
theorem c54 : check 56 101 18 54 = true := by decide +kernel
theorem c55 : check 56 101 18 55 = true := by decide +kernel
theorem c56 : check 56 101 18 56 = true := by decide +kernel
theorem c57 : check 56 101 18 57 = true := by decide +kernel
theorem c58 : check 56 101 18 58 = true := by decide +kernel
theorem c59 : check 56 101 18 59 = true := by decide +kernel
theorem c60 : check 56 101 18 60 = true := by decide +kernel
theorem c61 : check 56 101 18 61 = true := by decide +kernel
theorem c62 : check 56 101 18 62 = true := by decide +kernel
theorem c63 : check 56 101 18 63 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 48 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c48) (chunksOK_one c49)) (chunksOK_append (chunksOK_one c50) (chunksOK_one c51))) (chunksOK_append (chunksOK_append (chunksOK_one c52) (chunksOK_one c53)) (chunksOK_append (chunksOK_one c54) (chunksOK_one c55)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c56) (chunksOK_one c57)) (chunksOK_append (chunksOK_one c58) (chunksOK_one c59))) (chunksOK_append (chunksOK_append (chunksOK_one c60) (chunksOK_one c61)) (chunksOK_append (chunksOK_one c62) (chunksOK_one c63)))))

end C3

namespace C4

theorem c64 : check 56 101 18 64 = true := by decide +kernel
theorem c65 : check 56 101 18 65 = true := by decide +kernel
theorem c66 : check 56 101 18 66 = true := by decide +kernel
theorem c67 : check 56 101 18 67 = true := by decide +kernel
theorem c68 : check 56 101 18 68 = true := by decide +kernel
theorem c69 : check 56 101 18 69 = true := by decide +kernel
theorem c70 : check 56 101 18 70 = true := by decide +kernel
theorem c71 : check 56 101 18 71 = true := by decide +kernel
theorem c72 : check 56 101 18 72 = true := by decide +kernel
theorem c73 : check 56 101 18 73 = true := by decide +kernel
theorem c74 : check 56 101 18 74 = true := by decide +kernel
theorem c75 : check 56 101 18 75 = true := by decide +kernel
theorem c76 : check 56 101 18 76 = true := by decide +kernel
theorem c77 : check 56 101 18 77 = true := by decide +kernel
theorem c78 : check 56 101 18 78 = true := by decide +kernel
theorem c79 : check 56 101 18 79 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 64 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c64) (chunksOK_one c65)) (chunksOK_append (chunksOK_one c66) (chunksOK_one c67))) (chunksOK_append (chunksOK_append (chunksOK_one c68) (chunksOK_one c69)) (chunksOK_append (chunksOK_one c70) (chunksOK_one c71)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c72) (chunksOK_one c73)) (chunksOK_append (chunksOK_one c74) (chunksOK_one c75))) (chunksOK_append (chunksOK_append (chunksOK_one c76) (chunksOK_one c77)) (chunksOK_append (chunksOK_one c78) (chunksOK_one c79)))))

end C4

namespace C5

theorem c80 : check 56 101 18 80 = true := by decide +kernel
theorem c81 : check 56 101 18 81 = true := by decide +kernel
theorem c82 : check 56 101 18 82 = true := by decide +kernel
theorem c83 : check 56 101 18 83 = true := by decide +kernel
theorem c84 : check 56 101 18 84 = true := by decide +kernel
theorem c85 : check 56 101 18 85 = true := by decide +kernel
theorem c86 : check 56 101 18 86 = true := by decide +kernel
theorem c87 : check 56 101 18 87 = true := by decide +kernel
theorem c88 : check 56 101 18 88 = true := by decide +kernel
theorem c89 : check 56 101 18 89 = true := by decide +kernel
theorem c90 : check 56 101 18 90 = true := by decide +kernel
theorem c91 : check 56 101 18 91 = true := by decide +kernel
theorem c92 : check 56 101 18 92 = true := by decide +kernel
theorem c93 : check 56 101 18 93 = true := by decide +kernel
theorem c94 : check 56 101 18 94 = true := by decide +kernel
theorem c95 : check 56 101 18 95 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 80 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c80) (chunksOK_one c81)) (chunksOK_append (chunksOK_one c82) (chunksOK_one c83))) (chunksOK_append (chunksOK_append (chunksOK_one c84) (chunksOK_one c85)) (chunksOK_append (chunksOK_one c86) (chunksOK_one c87)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c88) (chunksOK_one c89)) (chunksOK_append (chunksOK_one c90) (chunksOK_one c91))) (chunksOK_append (chunksOK_append (chunksOK_one c92) (chunksOK_one c93)) (chunksOK_append (chunksOK_one c94) (chunksOK_one c95)))))

end C5

namespace C6

theorem c96 : check 56 101 18 96 = true := by decide +kernel
theorem c97 : check 56 101 18 97 = true := by decide +kernel
theorem c98 : check 56 101 18 98 = true := by decide +kernel
theorem c99 : check 56 101 18 99 = true := by decide +kernel
theorem c100 : check 56 101 18 100 = true := by decide +kernel
theorem c101 : check 56 101 18 101 = true := by decide +kernel
theorem c102 : check 56 101 18 102 = true := by decide +kernel
theorem c103 : check 56 101 18 103 = true := by decide +kernel
theorem c104 : check 56 101 18 104 = true := by decide +kernel
theorem c105 : check 56 101 18 105 = true := by decide +kernel
theorem c106 : check 56 101 18 106 = true := by decide +kernel
theorem c107 : check 56 101 18 107 = true := by decide +kernel
theorem c108 : check 56 101 18 108 = true := by decide +kernel
theorem c109 : check 56 101 18 109 = true := by decide +kernel
theorem c110 : check 56 101 18 110 = true := by decide +kernel
theorem c111 : check 56 101 18 111 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 96 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c96) (chunksOK_one c97)) (chunksOK_append (chunksOK_one c98) (chunksOK_one c99))) (chunksOK_append (chunksOK_append (chunksOK_one c100) (chunksOK_one c101)) (chunksOK_append (chunksOK_one c102) (chunksOK_one c103)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c104) (chunksOK_one c105)) (chunksOK_append (chunksOK_one c106) (chunksOK_one c107))) (chunksOK_append (chunksOK_append (chunksOK_one c108) (chunksOK_one c109)) (chunksOK_append (chunksOK_one c110) (chunksOK_one c111)))))

end C6

namespace C7

theorem c112 : check 56 101 18 112 = true := by decide +kernel
theorem c113 : check 56 101 18 113 = true := by decide +kernel
theorem c114 : check 56 101 18 114 = true := by decide +kernel
theorem c115 : check 56 101 18 115 = true := by decide +kernel
theorem c116 : check 56 101 18 116 = true := by decide +kernel
theorem c117 : check 56 101 18 117 = true := by decide +kernel
theorem c118 : check 56 101 18 118 = true := by decide +kernel
theorem c119 : check 56 101 18 119 = true := by decide +kernel
theorem c120 : check 56 101 18 120 = true := by decide +kernel
theorem c121 : check 56 101 18 121 = true := by decide +kernel
theorem c122 : check 56 101 18 122 = true := by decide +kernel
theorem c123 : check 56 101 18 123 = true := by decide +kernel
theorem c124 : check 56 101 18 124 = true := by decide +kernel
theorem c125 : check 56 101 18 125 = true := by decide +kernel
theorem c126 : check 56 101 18 126 = true := by decide +kernel
theorem c127 : check 56 101 18 127 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 112 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c112) (chunksOK_one c113)) (chunksOK_append (chunksOK_one c114) (chunksOK_one c115))) (chunksOK_append (chunksOK_append (chunksOK_one c116) (chunksOK_one c117)) (chunksOK_append (chunksOK_one c118) (chunksOK_one c119)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c120) (chunksOK_one c121)) (chunksOK_append (chunksOK_one c122) (chunksOK_one c123))) (chunksOK_append (chunksOK_append (chunksOK_one c124) (chunksOK_one c125)) (chunksOK_append (chunksOK_one c126) (chunksOK_one c127)))))

end C7

namespace C8

theorem c128 : check 56 101 18 128 = true := by decide +kernel
theorem c129 : check 56 101 18 129 = true := by decide +kernel
theorem c130 : check 56 101 18 130 = true := by decide +kernel
theorem c131 : check 56 101 18 131 = true := by decide +kernel
theorem c132 : check 56 101 18 132 = true := by decide +kernel
theorem c133 : check 56 101 18 133 = true := by decide +kernel
theorem c134 : check 56 101 18 134 = true := by decide +kernel
theorem c135 : check 56 101 18 135 = true := by decide +kernel
theorem c136 : check 56 101 18 136 = true := by decide +kernel
theorem c137 : check 56 101 18 137 = true := by decide +kernel
theorem c138 : check 56 101 18 138 = true := by decide +kernel
theorem c139 : check 56 101 18 139 = true := by decide +kernel
theorem c140 : check 56 101 18 140 = true := by decide +kernel
theorem c141 : check 56 101 18 141 = true := by decide +kernel
theorem c142 : check 56 101 18 142 = true := by decide +kernel
theorem c143 : check 56 101 18 143 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 128 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c128) (chunksOK_one c129)) (chunksOK_append (chunksOK_one c130) (chunksOK_one c131))) (chunksOK_append (chunksOK_append (chunksOK_one c132) (chunksOK_one c133)) (chunksOK_append (chunksOK_one c134) (chunksOK_one c135)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c136) (chunksOK_one c137)) (chunksOK_append (chunksOK_one c138) (chunksOK_one c139))) (chunksOK_append (chunksOK_append (chunksOK_one c140) (chunksOK_one c141)) (chunksOK_append (chunksOK_one c142) (chunksOK_one c143)))))

end C8

namespace C9

theorem c144 : check 56 101 18 144 = true := by decide +kernel
theorem c145 : check 56 101 18 145 = true := by decide +kernel
theorem c146 : check 56 101 18 146 = true := by decide +kernel
theorem c147 : check 56 101 18 147 = true := by decide +kernel
theorem c148 : check 56 101 18 148 = true := by decide +kernel
theorem c149 : check 56 101 18 149 = true := by decide +kernel
theorem c150 : check 56 101 18 150 = true := by decide +kernel
theorem c151 : check 56 101 18 151 = true := by decide +kernel
theorem c152 : check 56 101 18 152 = true := by decide +kernel
theorem c153 : check 56 101 18 153 = true := by decide +kernel
theorem c154 : check 56 101 18 154 = true := by decide +kernel
theorem c155 : check 56 101 18 155 = true := by decide +kernel
theorem c156 : check 56 101 18 156 = true := by decide +kernel
theorem c157 : check 56 101 18 157 = true := by decide +kernel
theorem c158 : check 56 101 18 158 = true := by decide +kernel
theorem c159 : check 56 101 18 159 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 144 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c144) (chunksOK_one c145)) (chunksOK_append (chunksOK_one c146) (chunksOK_one c147))) (chunksOK_append (chunksOK_append (chunksOK_one c148) (chunksOK_one c149)) (chunksOK_append (chunksOK_one c150) (chunksOK_one c151)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c152) (chunksOK_one c153)) (chunksOK_append (chunksOK_one c154) (chunksOK_one c155))) (chunksOK_append (chunksOK_append (chunksOK_one c156) (chunksOK_one c157)) (chunksOK_append (chunksOK_one c158) (chunksOK_one c159)))))

end C9

namespace C10

theorem c160 : check 56 101 18 160 = true := by decide +kernel
theorem c161 : check 56 101 18 161 = true := by decide +kernel
theorem c162 : check 56 101 18 162 = true := by decide +kernel
theorem c163 : check 56 101 18 163 = true := by decide +kernel
theorem c164 : check 56 101 18 164 = true := by decide +kernel
theorem c165 : check 56 101 18 165 = true := by decide +kernel
theorem c166 : check 56 101 18 166 = true := by decide +kernel
theorem c167 : check 56 101 18 167 = true := by decide +kernel
theorem c168 : check 56 101 18 168 = true := by decide +kernel
theorem c169 : check 56 101 18 169 = true := by decide +kernel
theorem c170 : check 56 101 18 170 = true := by decide +kernel
theorem c171 : check 56 101 18 171 = true := by decide +kernel
theorem c172 : check 56 101 18 172 = true := by decide +kernel
theorem c173 : check 56 101 18 173 = true := by decide +kernel
theorem c174 : check 56 101 18 174 = true := by decide +kernel
theorem c175 : check 56 101 18 175 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 160 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c160) (chunksOK_one c161)) (chunksOK_append (chunksOK_one c162) (chunksOK_one c163))) (chunksOK_append (chunksOK_append (chunksOK_one c164) (chunksOK_one c165)) (chunksOK_append (chunksOK_one c166) (chunksOK_one c167)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c168) (chunksOK_one c169)) (chunksOK_append (chunksOK_one c170) (chunksOK_one c171))) (chunksOK_append (chunksOK_append (chunksOK_one c172) (chunksOK_one c173)) (chunksOK_append (chunksOK_one c174) (chunksOK_one c175)))))

end C10

namespace C11

theorem c176 : check 56 101 18 176 = true := by decide +kernel
theorem c177 : check 56 101 18 177 = true := by decide +kernel
theorem c178 : check 56 101 18 178 = true := by decide +kernel
theorem c179 : check 56 101 18 179 = true := by decide +kernel
theorem c180 : check 56 101 18 180 = true := by decide +kernel
theorem c181 : check 56 101 18 181 = true := by decide +kernel
theorem c182 : check 56 101 18 182 = true := by decide +kernel
theorem c183 : check 56 101 18 183 = true := by decide +kernel
theorem c184 : check 56 101 18 184 = true := by decide +kernel
theorem c185 : check 56 101 18 185 = true := by decide +kernel
theorem c186 : check 56 101 18 186 = true := by decide +kernel
theorem c187 : check 56 101 18 187 = true := by decide +kernel
theorem c188 : check 56 101 18 188 = true := by decide +kernel
theorem c189 : check 56 101 18 189 = true := by decide +kernel
theorem c190 : check 56 101 18 190 = true := by decide +kernel
theorem c191 : check 56 101 18 191 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 176 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c176) (chunksOK_one c177)) (chunksOK_append (chunksOK_one c178) (chunksOK_one c179))) (chunksOK_append (chunksOK_append (chunksOK_one c180) (chunksOK_one c181)) (chunksOK_append (chunksOK_one c182) (chunksOK_one c183)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c184) (chunksOK_one c185)) (chunksOK_append (chunksOK_one c186) (chunksOK_one c187))) (chunksOK_append (chunksOK_append (chunksOK_one c188) (chunksOK_one c189)) (chunksOK_append (chunksOK_one c190) (chunksOK_one c191)))))

end C11

namespace C12

theorem c192 : check 56 101 18 192 = true := by decide +kernel
theorem c193 : check 56 101 18 193 = true := by decide +kernel
theorem c194 : check 56 101 18 194 = true := by decide +kernel
theorem c195 : check 56 101 18 195 = true := by decide +kernel
theorem c196 : check 56 101 18 196 = true := by decide +kernel
theorem c197 : check 56 101 18 197 = true := by decide +kernel
theorem c198 : check 56 101 18 198 = true := by decide +kernel
theorem c199 : check 56 101 18 199 = true := by decide +kernel
theorem c200 : check 56 101 18 200 = true := by decide +kernel
theorem c201 : check 56 101 18 201 = true := by decide +kernel
theorem c202 : check 56 101 18 202 = true := by decide +kernel
theorem c203 : check 56 101 18 203 = true := by decide +kernel
theorem c204 : check 56 101 18 204 = true := by decide +kernel
theorem c205 : check 56 101 18 205 = true := by decide +kernel
theorem c206 : check 56 101 18 206 = true := by decide +kernel
theorem c207 : check 56 101 18 207 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 192 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c192) (chunksOK_one c193)) (chunksOK_append (chunksOK_one c194) (chunksOK_one c195))) (chunksOK_append (chunksOK_append (chunksOK_one c196) (chunksOK_one c197)) (chunksOK_append (chunksOK_one c198) (chunksOK_one c199)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c200) (chunksOK_one c201)) (chunksOK_append (chunksOK_one c202) (chunksOK_one c203))) (chunksOK_append (chunksOK_append (chunksOK_one c204) (chunksOK_one c205)) (chunksOK_append (chunksOK_one c206) (chunksOK_one c207)))))

end C12

namespace C13

theorem c208 : check 56 101 18 208 = true := by decide +kernel
theorem c209 : check 56 101 18 209 = true := by decide +kernel
theorem c210 : check 56 101 18 210 = true := by decide +kernel
theorem c211 : check 56 101 18 211 = true := by decide +kernel
theorem c212 : check 56 101 18 212 = true := by decide +kernel
theorem c213 : check 56 101 18 213 = true := by decide +kernel
theorem c214 : check 56 101 18 214 = true := by decide +kernel
theorem c215 : check 56 101 18 215 = true := by decide +kernel
theorem c216 : check 56 101 18 216 = true := by decide +kernel
theorem c217 : check 56 101 18 217 = true := by decide +kernel
theorem c218 : check 56 101 18 218 = true := by decide +kernel
theorem c219 : check 56 101 18 219 = true := by decide +kernel
theorem c220 : check 56 101 18 220 = true := by decide +kernel
theorem c221 : check 56 101 18 221 = true := by decide +kernel
theorem c222 : check 56 101 18 222 = true := by decide +kernel
theorem c223 : check 56 101 18 223 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 208 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c208) (chunksOK_one c209)) (chunksOK_append (chunksOK_one c210) (chunksOK_one c211))) (chunksOK_append (chunksOK_append (chunksOK_one c212) (chunksOK_one c213)) (chunksOK_append (chunksOK_one c214) (chunksOK_one c215)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c216) (chunksOK_one c217)) (chunksOK_append (chunksOK_one c218) (chunksOK_one c219))) (chunksOK_append (chunksOK_append (chunksOK_one c220) (chunksOK_one c221)) (chunksOK_append (chunksOK_one c222) (chunksOK_one c223)))))

end C13

namespace C14

theorem c224 : check 56 101 18 224 = true := by decide +kernel
theorem c225 : check 56 101 18 225 = true := by decide +kernel
theorem c226 : check 56 101 18 226 = true := by decide +kernel
theorem c227 : check 56 101 18 227 = true := by decide +kernel
theorem c228 : check 56 101 18 228 = true := by decide +kernel
theorem c229 : check 56 101 18 229 = true := by decide +kernel
theorem c230 : check 56 101 18 230 = true := by decide +kernel
theorem c231 : check 56 101 18 231 = true := by decide +kernel
theorem c232 : check 56 101 18 232 = true := by decide +kernel
theorem c233 : check 56 101 18 233 = true := by decide +kernel
theorem c234 : check 56 101 18 234 = true := by decide +kernel
theorem c235 : check 56 101 18 235 = true := by decide +kernel
theorem c236 : check 56 101 18 236 = true := by decide +kernel
theorem c237 : check 56 101 18 237 = true := by decide +kernel
theorem c238 : check 56 101 18 238 = true := by decide +kernel
theorem c239 : check 56 101 18 239 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 224 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c224) (chunksOK_one c225)) (chunksOK_append (chunksOK_one c226) (chunksOK_one c227))) (chunksOK_append (chunksOK_append (chunksOK_one c228) (chunksOK_one c229)) (chunksOK_append (chunksOK_one c230) (chunksOK_one c231)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c232) (chunksOK_one c233)) (chunksOK_append (chunksOK_one c234) (chunksOK_one c235))) (chunksOK_append (chunksOK_append (chunksOK_one c236) (chunksOK_one c237)) (chunksOK_append (chunksOK_one c238) (chunksOK_one c239)))))

end C14

namespace C15

theorem c240 : check 56 101 18 240 = true := by decide +kernel
theorem c241 : check 56 101 18 241 = true := by decide +kernel
theorem c242 : check 56 101 18 242 = true := by decide +kernel
theorem c243 : check 56 101 18 243 = true := by decide +kernel
theorem c244 : check 56 101 18 244 = true := by decide +kernel
theorem c245 : check 56 101 18 245 = true := by decide +kernel
theorem c246 : check 56 101 18 246 = true := by decide +kernel
theorem c247 : check 56 101 18 247 = true := by decide +kernel
theorem c248 : check 56 101 18 248 = true := by decide +kernel
theorem c249 : check 56 101 18 249 = true := by decide +kernel
theorem c250 : check 56 101 18 250 = true := by decide +kernel
theorem c251 : check 56 101 18 251 = true := by decide +kernel
theorem c252 : check 56 101 18 252 = true := by decide +kernel
theorem c253 : check 56 101 18 253 = true := by decide +kernel
theorem c254 : check 56 101 18 254 = true := by decide +kernel
theorem c255 : check 56 101 18 255 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 240 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c240) (chunksOK_one c241)) (chunksOK_append (chunksOK_one c242) (chunksOK_one c243))) (chunksOK_append (chunksOK_append (chunksOK_one c244) (chunksOK_one c245)) (chunksOK_append (chunksOK_one c246) (chunksOK_one c247)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c248) (chunksOK_one c249)) (chunksOK_append (chunksOK_one c250) (chunksOK_one c251))) (chunksOK_append (chunksOK_append (chunksOK_one c252) (chunksOK_one c253)) (chunksOK_append (chunksOK_one c254) (chunksOK_one c255)))))

end C15

namespace C16

theorem c256 : check 56 101 18 256 = true := by decide +kernel
theorem c257 : check 56 101 18 257 = true := by decide +kernel
theorem c258 : check 56 101 18 258 = true := by decide +kernel
theorem c259 : check 56 101 18 259 = true := by decide +kernel
theorem c260 : check 56 101 18 260 = true := by decide +kernel
theorem c261 : check 56 101 18 261 = true := by decide +kernel
theorem c262 : check 56 101 18 262 = true := by decide +kernel
theorem c263 : check 56 101 18 263 = true := by decide +kernel
theorem c264 : check 56 101 18 264 = true := by decide +kernel
theorem c265 : check 56 101 18 265 = true := by decide +kernel
theorem c266 : check 56 101 18 266 = true := by decide +kernel
theorem c267 : check 56 101 18 267 = true := by decide +kernel
theorem c268 : check 56 101 18 268 = true := by decide +kernel
theorem c269 : check 56 101 18 269 = true := by decide +kernel
theorem c270 : check 56 101 18 270 = true := by decide +kernel
theorem c271 : check 56 101 18 271 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 256 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c256) (chunksOK_one c257)) (chunksOK_append (chunksOK_one c258) (chunksOK_one c259))) (chunksOK_append (chunksOK_append (chunksOK_one c260) (chunksOK_one c261)) (chunksOK_append (chunksOK_one c262) (chunksOK_one c263)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c264) (chunksOK_one c265)) (chunksOK_append (chunksOK_one c266) (chunksOK_one c267))) (chunksOK_append (chunksOK_append (chunksOK_one c268) (chunksOK_one c269)) (chunksOK_append (chunksOK_one c270) (chunksOK_one c271)))))

end C16

namespace C17

theorem c272 : check 56 101 18 272 = true := by decide +kernel
theorem c273 : check 56 101 18 273 = true := by decide +kernel
theorem c274 : check 56 101 18 274 = true := by decide +kernel
theorem c275 : check 56 101 18 275 = true := by decide +kernel
theorem c276 : check 56 101 18 276 = true := by decide +kernel
theorem c277 : check 56 101 18 277 = true := by decide +kernel
theorem c278 : check 56 101 18 278 = true := by decide +kernel
theorem c279 : check 56 101 18 279 = true := by decide +kernel
theorem c280 : check 56 101 18 280 = true := by decide +kernel
theorem c281 : check 56 101 18 281 = true := by decide +kernel
theorem c282 : check 56 101 18 282 = true := by decide +kernel
theorem c283 : check 56 101 18 283 = true := by decide +kernel
theorem c284 : check 56 101 18 284 = true := by decide +kernel
theorem c285 : check 56 101 18 285 = true := by decide +kernel
theorem c286 : check 56 101 18 286 = true := by decide +kernel
theorem c287 : check 56 101 18 287 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 272 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c272) (chunksOK_one c273)) (chunksOK_append (chunksOK_one c274) (chunksOK_one c275))) (chunksOK_append (chunksOK_append (chunksOK_one c276) (chunksOK_one c277)) (chunksOK_append (chunksOK_one c278) (chunksOK_one c279)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c280) (chunksOK_one c281)) (chunksOK_append (chunksOK_one c282) (chunksOK_one c283))) (chunksOK_append (chunksOK_append (chunksOK_one c284) (chunksOK_one c285)) (chunksOK_append (chunksOK_one c286) (chunksOK_one c287)))))

end C17

namespace C18

theorem c288 : check 56 101 18 288 = true := by decide +kernel
theorem c289 : check 56 101 18 289 = true := by decide +kernel
theorem c290 : check 56 101 18 290 = true := by decide +kernel
theorem c291 : check 56 101 18 291 = true := by decide +kernel
theorem c292 : check 56 101 18 292 = true := by decide +kernel
theorem c293 : check 56 101 18 293 = true := by decide +kernel
theorem c294 : check 56 101 18 294 = true := by decide +kernel
theorem c295 : check 56 101 18 295 = true := by decide +kernel
theorem c296 : check 56 101 18 296 = true := by decide +kernel
theorem c297 : check 56 101 18 297 = true := by decide +kernel
theorem c298 : check 56 101 18 298 = true := by decide +kernel
theorem c299 : check 56 101 18 299 = true := by decide +kernel
theorem c300 : check 56 101 18 300 = true := by decide +kernel
theorem c301 : check 56 101 18 301 = true := by decide +kernel
theorem c302 : check 56 101 18 302 = true := by decide +kernel
theorem c303 : check 56 101 18 303 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 288 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c288) (chunksOK_one c289)) (chunksOK_append (chunksOK_one c290) (chunksOK_one c291))) (chunksOK_append (chunksOK_append (chunksOK_one c292) (chunksOK_one c293)) (chunksOK_append (chunksOK_one c294) (chunksOK_one c295)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c296) (chunksOK_one c297)) (chunksOK_append (chunksOK_one c298) (chunksOK_one c299))) (chunksOK_append (chunksOK_append (chunksOK_one c300) (chunksOK_one c301)) (chunksOK_append (chunksOK_one c302) (chunksOK_one c303)))))

end C18

namespace C19

theorem c304 : check 56 101 18 304 = true := by decide +kernel
theorem c305 : check 56 101 18 305 = true := by decide +kernel
theorem c306 : check 56 101 18 306 = true := by decide +kernel
theorem c307 : check 56 101 18 307 = true := by decide +kernel
theorem c308 : check 56 101 18 308 = true := by decide +kernel
theorem c309 : check 56 101 18 309 = true := by decide +kernel
theorem c310 : check 56 101 18 310 = true := by decide +kernel
theorem c311 : check 56 101 18 311 = true := by decide +kernel
theorem c312 : check 56 101 18 312 = true := by decide +kernel
theorem c313 : check 56 101 18 313 = true := by decide +kernel
theorem c314 : check 56 101 18 314 = true := by decide +kernel
theorem c315 : check 56 101 18 315 = true := by decide +kernel
theorem c316 : check 56 101 18 316 = true := by decide +kernel
theorem c317 : check 56 101 18 317 = true := by decide +kernel
theorem c318 : check 56 101 18 318 = true := by decide +kernel
theorem c319 : check 56 101 18 319 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 304 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c304) (chunksOK_one c305)) (chunksOK_append (chunksOK_one c306) (chunksOK_one c307))) (chunksOK_append (chunksOK_append (chunksOK_one c308) (chunksOK_one c309)) (chunksOK_append (chunksOK_one c310) (chunksOK_one c311)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c312) (chunksOK_one c313)) (chunksOK_append (chunksOK_one c314) (chunksOK_one c315))) (chunksOK_append (chunksOK_append (chunksOK_one c316) (chunksOK_one c317)) (chunksOK_append (chunksOK_one c318) (chunksOK_one c319)))))

end C19

namespace C20

theorem c320 : check 56 101 18 320 = true := by decide +kernel
theorem c321 : check 56 101 18 321 = true := by decide +kernel
theorem c322 : check 56 101 18 322 = true := by decide +kernel
theorem c323 : check 56 101 18 323 = true := by decide +kernel
theorem c324 : check 56 101 18 324 = true := by decide +kernel
theorem c325 : check 56 101 18 325 = true := by decide +kernel
theorem c326 : check 56 101 18 326 = true := by decide +kernel
theorem c327 : check 56 101 18 327 = true := by decide +kernel
theorem c328 : check 56 101 18 328 = true := by decide +kernel
theorem c329 : check 56 101 18 329 = true := by decide +kernel
theorem c330 : check 56 101 18 330 = true := by decide +kernel
theorem c331 : check 56 101 18 331 = true := by decide +kernel
theorem c332 : check 56 101 18 332 = true := by decide +kernel
theorem c333 : check 56 101 18 333 = true := by decide +kernel
theorem c334 : check 56 101 18 334 = true := by decide +kernel
theorem c335 : check 56 101 18 335 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 320 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c320) (chunksOK_one c321)) (chunksOK_append (chunksOK_one c322) (chunksOK_one c323))) (chunksOK_append (chunksOK_append (chunksOK_one c324) (chunksOK_one c325)) (chunksOK_append (chunksOK_one c326) (chunksOK_one c327)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c328) (chunksOK_one c329)) (chunksOK_append (chunksOK_one c330) (chunksOK_one c331))) (chunksOK_append (chunksOK_append (chunksOK_one c332) (chunksOK_one c333)) (chunksOK_append (chunksOK_one c334) (chunksOK_one c335)))))

end C20

namespace C21

theorem c336 : check 56 101 18 336 = true := by decide +kernel
theorem c337 : check 56 101 18 337 = true := by decide +kernel
theorem c338 : check 56 101 18 338 = true := by decide +kernel
theorem c339 : check 56 101 18 339 = true := by decide +kernel
theorem c340 : check 56 101 18 340 = true := by decide +kernel
theorem c341 : check 56 101 18 341 = true := by decide +kernel
theorem c342 : check 56 101 18 342 = true := by decide +kernel
theorem c343 : check 56 101 18 343 = true := by decide +kernel
theorem c344 : check 56 101 18 344 = true := by decide +kernel
theorem c345 : check 56 101 18 345 = true := by decide +kernel
theorem c346 : check 56 101 18 346 = true := by decide +kernel
theorem c347 : check 56 101 18 347 = true := by decide +kernel
theorem c348 : check 56 101 18 348 = true := by decide +kernel
theorem c349 : check 56 101 18 349 = true := by decide +kernel
theorem c350 : check 56 101 18 350 = true := by decide +kernel
theorem c351 : check 56 101 18 351 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 336 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c336) (chunksOK_one c337)) (chunksOK_append (chunksOK_one c338) (chunksOK_one c339))) (chunksOK_append (chunksOK_append (chunksOK_one c340) (chunksOK_one c341)) (chunksOK_append (chunksOK_one c342) (chunksOK_one c343)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c344) (chunksOK_one c345)) (chunksOK_append (chunksOK_one c346) (chunksOK_one c347))) (chunksOK_append (chunksOK_append (chunksOK_one c348) (chunksOK_one c349)) (chunksOK_append (chunksOK_one c350) (chunksOK_one c351)))))

end C21

namespace C22

theorem c352 : check 56 101 18 352 = true := by decide +kernel
theorem c353 : check 56 101 18 353 = true := by decide +kernel
theorem c354 : check 56 101 18 354 = true := by decide +kernel
theorem c355 : check 56 101 18 355 = true := by decide +kernel
theorem c356 : check 56 101 18 356 = true := by decide +kernel
theorem c357 : check 56 101 18 357 = true := by decide +kernel
theorem c358 : check 56 101 18 358 = true := by decide +kernel
theorem c359 : check 56 101 18 359 = true := by decide +kernel
theorem c360 : check 56 101 18 360 = true := by decide +kernel
theorem c361 : check 56 101 18 361 = true := by decide +kernel
theorem c362 : check 56 101 18 362 = true := by decide +kernel
theorem c363 : check 56 101 18 363 = true := by decide +kernel
theorem c364 : check 56 101 18 364 = true := by decide +kernel
theorem c365 : check 56 101 18 365 = true := by decide +kernel
theorem c366 : check 56 101 18 366 = true := by decide +kernel
theorem c367 : check 56 101 18 367 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 352 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c352) (chunksOK_one c353)) (chunksOK_append (chunksOK_one c354) (chunksOK_one c355))) (chunksOK_append (chunksOK_append (chunksOK_one c356) (chunksOK_one c357)) (chunksOK_append (chunksOK_one c358) (chunksOK_one c359)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c360) (chunksOK_one c361)) (chunksOK_append (chunksOK_one c362) (chunksOK_one c363))) (chunksOK_append (chunksOK_append (chunksOK_one c364) (chunksOK_one c365)) (chunksOK_append (chunksOK_one c366) (chunksOK_one c367)))))

end C22

namespace C23

theorem c368 : check 56 101 18 368 = true := by decide +kernel
theorem c369 : check 56 101 18 369 = true := by decide +kernel
theorem c370 : check 56 101 18 370 = true := by decide +kernel
theorem c371 : check 56 101 18 371 = true := by decide +kernel
theorem c372 : check 56 101 18 372 = true := by decide +kernel
theorem c373 : check 56 101 18 373 = true := by decide +kernel
theorem c374 : check 56 101 18 374 = true := by decide +kernel
theorem c375 : check 56 101 18 375 = true := by decide +kernel
theorem c376 : check 56 101 18 376 = true := by decide +kernel
theorem c377 : check 56 101 18 377 = true := by decide +kernel
theorem c378 : check 56 101 18 378 = true := by decide +kernel
theorem c379 : check 56 101 18 379 = true := by decide +kernel
theorem c380 : check 56 101 18 380 = true := by decide +kernel
theorem c381 : check 56 101 18 381 = true := by decide +kernel
theorem c382 : check 56 101 18 382 = true := by decide +kernel
theorem c383 : check 56 101 18 383 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 368 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c368) (chunksOK_one c369)) (chunksOK_append (chunksOK_one c370) (chunksOK_one c371))) (chunksOK_append (chunksOK_append (chunksOK_one c372) (chunksOK_one c373)) (chunksOK_append (chunksOK_one c374) (chunksOK_one c375)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c376) (chunksOK_one c377)) (chunksOK_append (chunksOK_one c378) (chunksOK_one c379))) (chunksOK_append (chunksOK_append (chunksOK_one c380) (chunksOK_one c381)) (chunksOK_append (chunksOK_one c382) (chunksOK_one c383)))))

end C23

namespace C24

theorem c384 : check 56 101 18 384 = true := by decide +kernel
theorem c385 : check 56 101 18 385 = true := by decide +kernel
theorem c386 : check 56 101 18 386 = true := by decide +kernel
theorem c387 : check 56 101 18 387 = true := by decide +kernel
theorem c388 : check 56 101 18 388 = true := by decide +kernel
theorem c389 : check 56 101 18 389 = true := by decide +kernel
theorem c390 : check 56 101 18 390 = true := by decide +kernel
theorem c391 : check 56 101 18 391 = true := by decide +kernel
theorem c392 : check 56 101 18 392 = true := by decide +kernel
theorem c393 : check 56 101 18 393 = true := by decide +kernel
theorem c394 : check 56 101 18 394 = true := by decide +kernel
theorem c395 : check 56 101 18 395 = true := by decide +kernel
theorem c396 : check 56 101 18 396 = true := by decide +kernel
theorem c397 : check 56 101 18 397 = true := by decide +kernel
theorem c398 : check 56 101 18 398 = true := by decide +kernel
theorem c399 : check 56 101 18 399 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 384 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c384) (chunksOK_one c385)) (chunksOK_append (chunksOK_one c386) (chunksOK_one c387))) (chunksOK_append (chunksOK_append (chunksOK_one c388) (chunksOK_one c389)) (chunksOK_append (chunksOK_one c390) (chunksOK_one c391)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c392) (chunksOK_one c393)) (chunksOK_append (chunksOK_one c394) (chunksOK_one c395))) (chunksOK_append (chunksOK_append (chunksOK_one c396) (chunksOK_one c397)) (chunksOK_append (chunksOK_one c398) (chunksOK_one c399)))))

end C24

namespace C25

theorem c400 : check 56 101 18 400 = true := by decide +kernel
theorem c401 : check 56 101 18 401 = true := by decide +kernel
theorem c402 : check 56 101 18 402 = true := by decide +kernel
theorem c403 : check 56 101 18 403 = true := by decide +kernel
theorem c404 : check 56 101 18 404 = true := by decide +kernel
theorem c405 : check 56 101 18 405 = true := by decide +kernel
theorem c406 : check 56 101 18 406 = true := by decide +kernel
theorem c407 : check 56 101 18 407 = true := by decide +kernel
theorem c408 : check 56 101 18 408 = true := by decide +kernel
theorem c409 : check 56 101 18 409 = true := by decide +kernel
theorem c410 : check 56 101 18 410 = true := by decide +kernel
theorem c411 : check 56 101 18 411 = true := by decide +kernel
theorem c412 : check 56 101 18 412 = true := by decide +kernel
theorem c413 : check 56 101 18 413 = true := by decide +kernel
theorem c414 : check 56 101 18 414 = true := by decide +kernel
theorem c415 : check 56 101 18 415 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 400 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c400) (chunksOK_one c401)) (chunksOK_append (chunksOK_one c402) (chunksOK_one c403))) (chunksOK_append (chunksOK_append (chunksOK_one c404) (chunksOK_one c405)) (chunksOK_append (chunksOK_one c406) (chunksOK_one c407)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c408) (chunksOK_one c409)) (chunksOK_append (chunksOK_one c410) (chunksOK_one c411))) (chunksOK_append (chunksOK_append (chunksOK_one c412) (chunksOK_one c413)) (chunksOK_append (chunksOK_one c414) (chunksOK_one c415)))))

end C25

namespace C26

theorem c416 : check 56 101 18 416 = true := by decide +kernel
theorem c417 : check 56 101 18 417 = true := by decide +kernel
theorem c418 : check 56 101 18 418 = true := by decide +kernel
theorem c419 : check 56 101 18 419 = true := by decide +kernel
theorem c420 : check 56 101 18 420 = true := by decide +kernel
theorem c421 : check 56 101 18 421 = true := by decide +kernel
theorem c422 : check 56 101 18 422 = true := by decide +kernel
theorem c423 : check 56 101 18 423 = true := by decide +kernel
theorem c424 : check 56 101 18 424 = true := by decide +kernel
theorem c425 : check 56 101 18 425 = true := by decide +kernel
theorem c426 : check 56 101 18 426 = true := by decide +kernel
theorem c427 : check 56 101 18 427 = true := by decide +kernel
theorem c428 : check 56 101 18 428 = true := by decide +kernel
theorem c429 : check 56 101 18 429 = true := by decide +kernel
theorem c430 : check 56 101 18 430 = true := by decide +kernel
theorem c431 : check 56 101 18 431 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 416 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c416) (chunksOK_one c417)) (chunksOK_append (chunksOK_one c418) (chunksOK_one c419))) (chunksOK_append (chunksOK_append (chunksOK_one c420) (chunksOK_one c421)) (chunksOK_append (chunksOK_one c422) (chunksOK_one c423)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c424) (chunksOK_one c425)) (chunksOK_append (chunksOK_one c426) (chunksOK_one c427))) (chunksOK_append (chunksOK_append (chunksOK_one c428) (chunksOK_one c429)) (chunksOK_append (chunksOK_one c430) (chunksOK_one c431)))))

end C26

namespace C27

theorem c432 : check 56 101 18 432 = true := by decide +kernel
theorem c433 : check 56 101 18 433 = true := by decide +kernel
theorem c434 : check 56 101 18 434 = true := by decide +kernel
theorem c435 : check 56 101 18 435 = true := by decide +kernel
theorem c436 : check 56 101 18 436 = true := by decide +kernel
theorem c437 : check 56 101 18 437 = true := by decide +kernel
theorem c438 : check 56 101 18 438 = true := by decide +kernel
theorem c439 : check 56 101 18 439 = true := by decide +kernel
theorem c440 : check 56 101 18 440 = true := by decide +kernel
theorem c441 : check 56 101 18 441 = true := by decide +kernel
theorem c442 : check 56 101 18 442 = true := by decide +kernel
theorem c443 : check 56 101 18 443 = true := by decide +kernel
theorem c444 : check 56 101 18 444 = true := by decide +kernel
theorem c445 : check 56 101 18 445 = true := by decide +kernel
theorem c446 : check 56 101 18 446 = true := by decide +kernel
theorem c447 : check 56 101 18 447 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 432 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c432) (chunksOK_one c433)) (chunksOK_append (chunksOK_one c434) (chunksOK_one c435))) (chunksOK_append (chunksOK_append (chunksOK_one c436) (chunksOK_one c437)) (chunksOK_append (chunksOK_one c438) (chunksOK_one c439)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c440) (chunksOK_one c441)) (chunksOK_append (chunksOK_one c442) (chunksOK_one c443))) (chunksOK_append (chunksOK_append (chunksOK_one c444) (chunksOK_one c445)) (chunksOK_append (chunksOK_one c446) (chunksOK_one c447)))))

end C27

namespace C28

theorem c448 : check 56 101 18 448 = true := by decide +kernel
theorem c449 : check 56 101 18 449 = true := by decide +kernel
theorem c450 : check 56 101 18 450 = true := by decide +kernel
theorem c451 : check 56 101 18 451 = true := by decide +kernel
theorem c452 : check 56 101 18 452 = true := by decide +kernel
theorem c453 : check 56 101 18 453 = true := by decide +kernel
theorem c454 : check 56 101 18 454 = true := by decide +kernel
theorem c455 : check 56 101 18 455 = true := by decide +kernel
theorem c456 : check 56 101 18 456 = true := by decide +kernel
theorem c457 : check 56 101 18 457 = true := by decide +kernel
theorem c458 : check 56 101 18 458 = true := by decide +kernel
theorem c459 : check 56 101 18 459 = true := by decide +kernel
theorem c460 : check 56 101 18 460 = true := by decide +kernel
theorem c461 : check 56 101 18 461 = true := by decide +kernel
theorem c462 : check 56 101 18 462 = true := by decide +kernel
theorem c463 : check 56 101 18 463 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 448 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c448) (chunksOK_one c449)) (chunksOK_append (chunksOK_one c450) (chunksOK_one c451))) (chunksOK_append (chunksOK_append (chunksOK_one c452) (chunksOK_one c453)) (chunksOK_append (chunksOK_one c454) (chunksOK_one c455)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c456) (chunksOK_one c457)) (chunksOK_append (chunksOK_one c458) (chunksOK_one c459))) (chunksOK_append (chunksOK_append (chunksOK_one c460) (chunksOK_one c461)) (chunksOK_append (chunksOK_one c462) (chunksOK_one c463)))))

end C28

namespace C29

theorem c464 : check 56 101 18 464 = true := by decide +kernel
theorem c465 : check 56 101 18 465 = true := by decide +kernel
theorem c466 : check 56 101 18 466 = true := by decide +kernel
theorem c467 : check 56 101 18 467 = true := by decide +kernel
theorem c468 : check 56 101 18 468 = true := by decide +kernel
theorem c469 : check 56 101 18 469 = true := by decide +kernel
theorem c470 : check 56 101 18 470 = true := by decide +kernel
theorem c471 : check 56 101 18 471 = true := by decide +kernel
theorem c472 : check 56 101 18 472 = true := by decide +kernel
theorem c473 : check 56 101 18 473 = true := by decide +kernel
theorem c474 : check 56 101 18 474 = true := by decide +kernel
theorem c475 : check 56 101 18 475 = true := by decide +kernel
theorem c476 : check 56 101 18 476 = true := by decide +kernel
theorem c477 : check 56 101 18 477 = true := by decide +kernel
theorem c478 : check 56 101 18 478 = true := by decide +kernel
theorem c479 : check 56 101 18 479 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 464 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c464) (chunksOK_one c465)) (chunksOK_append (chunksOK_one c466) (chunksOK_one c467))) (chunksOK_append (chunksOK_append (chunksOK_one c468) (chunksOK_one c469)) (chunksOK_append (chunksOK_one c470) (chunksOK_one c471)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c472) (chunksOK_one c473)) (chunksOK_append (chunksOK_one c474) (chunksOK_one c475))) (chunksOK_append (chunksOK_append (chunksOK_one c476) (chunksOK_one c477)) (chunksOK_append (chunksOK_one c478) (chunksOK_one c479)))))

end C29

namespace C30

theorem c480 : check 56 101 18 480 = true := by decide +kernel
theorem c481 : check 56 101 18 481 = true := by decide +kernel
theorem c482 : check 56 101 18 482 = true := by decide +kernel
theorem c483 : check 56 101 18 483 = true := by decide +kernel
theorem c484 : check 56 101 18 484 = true := by decide +kernel
theorem c485 : check 56 101 18 485 = true := by decide +kernel
theorem c486 : check 56 101 18 486 = true := by decide +kernel
theorem c487 : check 56 101 18 487 = true := by decide +kernel
theorem c488 : check 56 101 18 488 = true := by decide +kernel
theorem c489 : check 56 101 18 489 = true := by decide +kernel
theorem c490 : check 56 101 18 490 = true := by decide +kernel
theorem c491 : check 56 101 18 491 = true := by decide +kernel
theorem c492 : check 56 101 18 492 = true := by decide +kernel
theorem c493 : check 56 101 18 493 = true := by decide +kernel
theorem c494 : check 56 101 18 494 = true := by decide +kernel
theorem c495 : check 56 101 18 495 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 480 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c480) (chunksOK_one c481)) (chunksOK_append (chunksOK_one c482) (chunksOK_one c483))) (chunksOK_append (chunksOK_append (chunksOK_one c484) (chunksOK_one c485)) (chunksOK_append (chunksOK_one c486) (chunksOK_one c487)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c488) (chunksOK_one c489)) (chunksOK_append (chunksOK_one c490) (chunksOK_one c491))) (chunksOK_append (chunksOK_append (chunksOK_one c492) (chunksOK_one c493)) (chunksOK_append (chunksOK_one c494) (chunksOK_one c495)))))

end C30

namespace C31

theorem c496 : check 56 101 18 496 = true := by decide +kernel
theorem c497 : check 56 101 18 497 = true := by decide +kernel
theorem c498 : check 56 101 18 498 = true := by decide +kernel
theorem c499 : check 56 101 18 499 = true := by decide +kernel
theorem c500 : check 56 101 18 500 = true := by decide +kernel
theorem c501 : check 56 101 18 501 = true := by decide +kernel
theorem c502 : check 56 101 18 502 = true := by decide +kernel
theorem c503 : check 56 101 18 503 = true := by decide +kernel
theorem c504 : check 56 101 18 504 = true := by decide +kernel
theorem c505 : check 56 101 18 505 = true := by decide +kernel
theorem c506 : check 56 101 18 506 = true := by decide +kernel
theorem c507 : check 56 101 18 507 = true := by decide +kernel
theorem c508 : check 56 101 18 508 = true := by decide +kernel
theorem c509 : check 56 101 18 509 = true := by decide +kernel
theorem c510 : check 56 101 18 510 = true := by decide +kernel
theorem c511 : check 56 101 18 511 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 496 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c496) (chunksOK_one c497)) (chunksOK_append (chunksOK_one c498) (chunksOK_one c499))) (chunksOK_append (chunksOK_append (chunksOK_one c500) (chunksOK_one c501)) (chunksOK_append (chunksOK_one c502) (chunksOK_one c503)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c504) (chunksOK_one c505)) (chunksOK_append (chunksOK_one c506) (chunksOK_one c507))) (chunksOK_append (chunksOK_append (chunksOK_one c508) (chunksOK_one c509)) (chunksOK_append (chunksOK_one c510) (chunksOK_one c511)))))

end C31

namespace C32

theorem c512 : check 56 101 18 512 = true := by decide +kernel
theorem c513 : check 56 101 18 513 = true := by decide +kernel
theorem c514 : check 56 101 18 514 = true := by decide +kernel
theorem c515 : check 56 101 18 515 = true := by decide +kernel
theorem c516 : check 56 101 18 516 = true := by decide +kernel
theorem c517 : check 56 101 18 517 = true := by decide +kernel
theorem c518 : check 56 101 18 518 = true := by decide +kernel
theorem c519 : check 56 101 18 519 = true := by decide +kernel
theorem c520 : check 56 101 18 520 = true := by decide +kernel
theorem c521 : check 56 101 18 521 = true := by decide +kernel
theorem c522 : check 56 101 18 522 = true := by decide +kernel
theorem c523 : check 56 101 18 523 = true := by decide +kernel
theorem c524 : check 56 101 18 524 = true := by decide +kernel
theorem c525 : check 56 101 18 525 = true := by decide +kernel
theorem c526 : check 56 101 18 526 = true := by decide +kernel
theorem c527 : check 56 101 18 527 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 512 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c512) (chunksOK_one c513)) (chunksOK_append (chunksOK_one c514) (chunksOK_one c515))) (chunksOK_append (chunksOK_append (chunksOK_one c516) (chunksOK_one c517)) (chunksOK_append (chunksOK_one c518) (chunksOK_one c519)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c520) (chunksOK_one c521)) (chunksOK_append (chunksOK_one c522) (chunksOK_one c523))) (chunksOK_append (chunksOK_append (chunksOK_one c524) (chunksOK_one c525)) (chunksOK_append (chunksOK_one c526) (chunksOK_one c527)))))

end C32

namespace C33

theorem c528 : check 56 101 18 528 = true := by decide +kernel
theorem c529 : check 56 101 18 529 = true := by decide +kernel
theorem c530 : check 56 101 18 530 = true := by decide +kernel
theorem c531 : check 56 101 18 531 = true := by decide +kernel
theorem c532 : check 56 101 18 532 = true := by decide +kernel
theorem c533 : check 56 101 18 533 = true := by decide +kernel
theorem c534 : check 56 101 18 534 = true := by decide +kernel
theorem c535 : check 56 101 18 535 = true := by decide +kernel
theorem c536 : check 56 101 18 536 = true := by decide +kernel
theorem c537 : check 56 101 18 537 = true := by decide +kernel
theorem c538 : check 56 101 18 538 = true := by decide +kernel
theorem c539 : check 56 101 18 539 = true := by decide +kernel
theorem c540 : check 56 101 18 540 = true := by decide +kernel
theorem c541 : check 56 101 18 541 = true := by decide +kernel
theorem c542 : check 56 101 18 542 = true := by decide +kernel
theorem c543 : check 56 101 18 543 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 528 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c528) (chunksOK_one c529)) (chunksOK_append (chunksOK_one c530) (chunksOK_one c531))) (chunksOK_append (chunksOK_append (chunksOK_one c532) (chunksOK_one c533)) (chunksOK_append (chunksOK_one c534) (chunksOK_one c535)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c536) (chunksOK_one c537)) (chunksOK_append (chunksOK_one c538) (chunksOK_one c539))) (chunksOK_append (chunksOK_append (chunksOK_one c540) (chunksOK_one c541)) (chunksOK_append (chunksOK_one c542) (chunksOK_one c543)))))

end C33

namespace C34

theorem c544 : check 56 101 18 544 = true := by decide +kernel
theorem c545 : check 56 101 18 545 = true := by decide +kernel
theorem c546 : check 56 101 18 546 = true := by decide +kernel
theorem c547 : check 56 101 18 547 = true := by decide +kernel
theorem c548 : check 56 101 18 548 = true := by decide +kernel
theorem c549 : check 56 101 18 549 = true := by decide +kernel
theorem c550 : check 56 101 18 550 = true := by decide +kernel
theorem c551 : check 56 101 18 551 = true := by decide +kernel
theorem c552 : check 56 101 18 552 = true := by decide +kernel
theorem c553 : check 56 101 18 553 = true := by decide +kernel
theorem c554 : check 56 101 18 554 = true := by decide +kernel
theorem c555 : check 56 101 18 555 = true := by decide +kernel
theorem c556 : check 56 101 18 556 = true := by decide +kernel
theorem c557 : check 56 101 18 557 = true := by decide +kernel
theorem c558 : check 56 101 18 558 = true := by decide +kernel
theorem c559 : check 56 101 18 559 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 544 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c544) (chunksOK_one c545)) (chunksOK_append (chunksOK_one c546) (chunksOK_one c547))) (chunksOK_append (chunksOK_append (chunksOK_one c548) (chunksOK_one c549)) (chunksOK_append (chunksOK_one c550) (chunksOK_one c551)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c552) (chunksOK_one c553)) (chunksOK_append (chunksOK_one c554) (chunksOK_one c555))) (chunksOK_append (chunksOK_append (chunksOK_one c556) (chunksOK_one c557)) (chunksOK_append (chunksOK_one c558) (chunksOK_one c559)))))

end C34

namespace C35

theorem c560 : check 56 101 18 560 = true := by decide +kernel
theorem c561 : check 56 101 18 561 = true := by decide +kernel
theorem c562 : check 56 101 18 562 = true := by decide +kernel
theorem c563 : check 56 101 18 563 = true := by decide +kernel
theorem c564 : check 56 101 18 564 = true := by decide +kernel
theorem c565 : check 56 101 18 565 = true := by decide +kernel
theorem c566 : check 56 101 18 566 = true := by decide +kernel
theorem c567 : check 56 101 18 567 = true := by decide +kernel
theorem c568 : check 56 101 18 568 = true := by decide +kernel
theorem c569 : check 56 101 18 569 = true := by decide +kernel
theorem c570 : check 56 101 18 570 = true := by decide +kernel
theorem c571 : check 56 101 18 571 = true := by decide +kernel
theorem c572 : check 56 101 18 572 = true := by decide +kernel
theorem c573 : check 56 101 18 573 = true := by decide +kernel
theorem c574 : check 56 101 18 574 = true := by decide +kernel
theorem c575 : check 56 101 18 575 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 560 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c560) (chunksOK_one c561)) (chunksOK_append (chunksOK_one c562) (chunksOK_one c563))) (chunksOK_append (chunksOK_append (chunksOK_one c564) (chunksOK_one c565)) (chunksOK_append (chunksOK_one c566) (chunksOK_one c567)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c568) (chunksOK_one c569)) (chunksOK_append (chunksOK_one c570) (chunksOK_one c571))) (chunksOK_append (chunksOK_append (chunksOK_one c572) (chunksOK_one c573)) (chunksOK_append (chunksOK_one c574) (chunksOK_one c575)))))

end C35

namespace C36

theorem c576 : check 56 101 18 576 = true := by decide +kernel
theorem c577 : check 56 101 18 577 = true := by decide +kernel
theorem c578 : check 56 101 18 578 = true := by decide +kernel
theorem c579 : check 56 101 18 579 = true := by decide +kernel
theorem c580 : check 56 101 18 580 = true := by decide +kernel
theorem c581 : check 56 101 18 581 = true := by decide +kernel
theorem c582 : check 56 101 18 582 = true := by decide +kernel
theorem c583 : check 56 101 18 583 = true := by decide +kernel
theorem c584 : check 56 101 18 584 = true := by decide +kernel
theorem c585 : check 56 101 18 585 = true := by decide +kernel
theorem c586 : check 56 101 18 586 = true := by decide +kernel
theorem c587 : check 56 101 18 587 = true := by decide +kernel
theorem c588 : check 56 101 18 588 = true := by decide +kernel
theorem c589 : check 56 101 18 589 = true := by decide +kernel
theorem c590 : check 56 101 18 590 = true := by decide +kernel
theorem c591 : check 56 101 18 591 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 576 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c576) (chunksOK_one c577)) (chunksOK_append (chunksOK_one c578) (chunksOK_one c579))) (chunksOK_append (chunksOK_append (chunksOK_one c580) (chunksOK_one c581)) (chunksOK_append (chunksOK_one c582) (chunksOK_one c583)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c584) (chunksOK_one c585)) (chunksOK_append (chunksOK_one c586) (chunksOK_one c587))) (chunksOK_append (chunksOK_append (chunksOK_one c588) (chunksOK_one c589)) (chunksOK_append (chunksOK_one c590) (chunksOK_one c591)))))

end C36

namespace C37

theorem c592 : check 56 101 18 592 = true := by decide +kernel
theorem c593 : check 56 101 18 593 = true := by decide +kernel
theorem c594 : check 56 101 18 594 = true := by decide +kernel
theorem c595 : check 56 101 18 595 = true := by decide +kernel
theorem c596 : check 56 101 18 596 = true := by decide +kernel
theorem c597 : check 56 101 18 597 = true := by decide +kernel
theorem c598 : check 56 101 18 598 = true := by decide +kernel
theorem c599 : check 56 101 18 599 = true := by decide +kernel
theorem c600 : check 56 101 18 600 = true := by decide +kernel
theorem c601 : check 56 101 18 601 = true := by decide +kernel
theorem c602 : check 56 101 18 602 = true := by decide +kernel
theorem c603 : check 56 101 18 603 = true := by decide +kernel
theorem c604 : check 56 101 18 604 = true := by decide +kernel
theorem c605 : check 56 101 18 605 = true := by decide +kernel
theorem c606 : check 56 101 18 606 = true := by decide +kernel
theorem c607 : check 56 101 18 607 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 592 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c592) (chunksOK_one c593)) (chunksOK_append (chunksOK_one c594) (chunksOK_one c595))) (chunksOK_append (chunksOK_append (chunksOK_one c596) (chunksOK_one c597)) (chunksOK_append (chunksOK_one c598) (chunksOK_one c599)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c600) (chunksOK_one c601)) (chunksOK_append (chunksOK_one c602) (chunksOK_one c603))) (chunksOK_append (chunksOK_append (chunksOK_one c604) (chunksOK_one c605)) (chunksOK_append (chunksOK_one c606) (chunksOK_one c607)))))

end C37

namespace C38

theorem c608 : check 56 101 18 608 = true := by decide +kernel
theorem c609 : check 56 101 18 609 = true := by decide +kernel
theorem c610 : check 56 101 18 610 = true := by decide +kernel
theorem c611 : check 56 101 18 611 = true := by decide +kernel
theorem c612 : check 56 101 18 612 = true := by decide +kernel
theorem c613 : check 56 101 18 613 = true := by decide +kernel
theorem c614 : check 56 101 18 614 = true := by decide +kernel
theorem c615 : check 56 101 18 615 = true := by decide +kernel
theorem c616 : check 56 101 18 616 = true := by decide +kernel
theorem c617 : check 56 101 18 617 = true := by decide +kernel
theorem c618 : check 56 101 18 618 = true := by decide +kernel
theorem c619 : check 56 101 18 619 = true := by decide +kernel
theorem c620 : check 56 101 18 620 = true := by decide +kernel
theorem c621 : check 56 101 18 621 = true := by decide +kernel
theorem c622 : check 56 101 18 622 = true := by decide +kernel
theorem c623 : check 56 101 18 623 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 608 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c608) (chunksOK_one c609)) (chunksOK_append (chunksOK_one c610) (chunksOK_one c611))) (chunksOK_append (chunksOK_append (chunksOK_one c612) (chunksOK_one c613)) (chunksOK_append (chunksOK_one c614) (chunksOK_one c615)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c616) (chunksOK_one c617)) (chunksOK_append (chunksOK_one c618) (chunksOK_one c619))) (chunksOK_append (chunksOK_append (chunksOK_one c620) (chunksOK_one c621)) (chunksOK_append (chunksOK_one c622) (chunksOK_one c623)))))

end C38

namespace C39

theorem c624 : check 56 101 18 624 = true := by decide +kernel
theorem c625 : check 56 101 18 625 = true := by decide +kernel
theorem c626 : check 56 101 18 626 = true := by decide +kernel
theorem c627 : check 56 101 18 627 = true := by decide +kernel
theorem c628 : check 56 101 18 628 = true := by decide +kernel
theorem c629 : check 56 101 18 629 = true := by decide +kernel
theorem c630 : check 56 101 18 630 = true := by decide +kernel
theorem c631 : check 56 101 18 631 = true := by decide +kernel
theorem c632 : check 56 101 18 632 = true := by decide +kernel
theorem c633 : check 56 101 18 633 = true := by decide +kernel
theorem c634 : check 56 101 18 634 = true := by decide +kernel
theorem c635 : check 56 101 18 635 = true := by decide +kernel
theorem c636 : check 56 101 18 636 = true := by decide +kernel
theorem c637 : check 56 101 18 637 = true := by decide +kernel
theorem c638 : check 56 101 18 638 = true := by decide +kernel
theorem c639 : check 56 101 18 639 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 624 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c624) (chunksOK_one c625)) (chunksOK_append (chunksOK_one c626) (chunksOK_one c627))) (chunksOK_append (chunksOK_append (chunksOK_one c628) (chunksOK_one c629)) (chunksOK_append (chunksOK_one c630) (chunksOK_one c631)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c632) (chunksOK_one c633)) (chunksOK_append (chunksOK_one c634) (chunksOK_one c635))) (chunksOK_append (chunksOK_append (chunksOK_one c636) (chunksOK_one c637)) (chunksOK_append (chunksOK_one c638) (chunksOK_one c639)))))

end C39

namespace C40

theorem c640 : check 56 101 18 640 = true := by decide +kernel
theorem c641 : check 56 101 18 641 = true := by decide +kernel
theorem c642 : check 56 101 18 642 = true := by decide +kernel
theorem c643 : check 56 101 18 643 = true := by decide +kernel
theorem c644 : check 56 101 18 644 = true := by decide +kernel
theorem c645 : check 56 101 18 645 = true := by decide +kernel
theorem c646 : check 56 101 18 646 = true := by decide +kernel
theorem c647 : check 56 101 18 647 = true := by decide +kernel
theorem c648 : check 56 101 18 648 = true := by decide +kernel
theorem c649 : check 56 101 18 649 = true := by decide +kernel
theorem c650 : check 56 101 18 650 = true := by decide +kernel
theorem c651 : check 56 101 18 651 = true := by decide +kernel
theorem c652 : check 56 101 18 652 = true := by decide +kernel
theorem c653 : check 56 101 18 653 = true := by decide +kernel
theorem c654 : check 56 101 18 654 = true := by decide +kernel
theorem c655 : check 56 101 18 655 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 640 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c640) (chunksOK_one c641)) (chunksOK_append (chunksOK_one c642) (chunksOK_one c643))) (chunksOK_append (chunksOK_append (chunksOK_one c644) (chunksOK_one c645)) (chunksOK_append (chunksOK_one c646) (chunksOK_one c647)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c648) (chunksOK_one c649)) (chunksOK_append (chunksOK_one c650) (chunksOK_one c651))) (chunksOK_append (chunksOK_append (chunksOK_one c652) (chunksOK_one c653)) (chunksOK_append (chunksOK_one c654) (chunksOK_one c655)))))

end C40

namespace C41

theorem c656 : check 56 101 18 656 = true := by decide +kernel
theorem c657 : check 56 101 18 657 = true := by decide +kernel
theorem c658 : check 56 101 18 658 = true := by decide +kernel
theorem c659 : check 56 101 18 659 = true := by decide +kernel
theorem c660 : check 56 101 18 660 = true := by decide +kernel
theorem c661 : check 56 101 18 661 = true := by decide +kernel
theorem c662 : check 56 101 18 662 = true := by decide +kernel
theorem c663 : check 56 101 18 663 = true := by decide +kernel
theorem c664 : check 56 101 18 664 = true := by decide +kernel
theorem c665 : check 56 101 18 665 = true := by decide +kernel
theorem c666 : check 56 101 18 666 = true := by decide +kernel
theorem c667 : check 56 101 18 667 = true := by decide +kernel
theorem c668 : check 56 101 18 668 = true := by decide +kernel
theorem c669 : check 56 101 18 669 = true := by decide +kernel
theorem c670 : check 56 101 18 670 = true := by decide +kernel
theorem c671 : check 56 101 18 671 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 656 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c656) (chunksOK_one c657)) (chunksOK_append (chunksOK_one c658) (chunksOK_one c659))) (chunksOK_append (chunksOK_append (chunksOK_one c660) (chunksOK_one c661)) (chunksOK_append (chunksOK_one c662) (chunksOK_one c663)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c664) (chunksOK_one c665)) (chunksOK_append (chunksOK_one c666) (chunksOK_one c667))) (chunksOK_append (chunksOK_append (chunksOK_one c668) (chunksOK_one c669)) (chunksOK_append (chunksOK_one c670) (chunksOK_one c671)))))

end C41

namespace C42

theorem c672 : check 56 101 18 672 = true := by decide +kernel
theorem c673 : check 56 101 18 673 = true := by decide +kernel
theorem c674 : check 56 101 18 674 = true := by decide +kernel
theorem c675 : check 56 101 18 675 = true := by decide +kernel
theorem c676 : check 56 101 18 676 = true := by decide +kernel
theorem c677 : check 56 101 18 677 = true := by decide +kernel
theorem c678 : check 56 101 18 678 = true := by decide +kernel
theorem c679 : check 56 101 18 679 = true := by decide +kernel
theorem c680 : check 56 101 18 680 = true := by decide +kernel
theorem c681 : check 56 101 18 681 = true := by decide +kernel
theorem c682 : check 56 101 18 682 = true := by decide +kernel
theorem c683 : check 56 101 18 683 = true := by decide +kernel
theorem c684 : check 56 101 18 684 = true := by decide +kernel
theorem c685 : check 56 101 18 685 = true := by decide +kernel
theorem c686 : check 56 101 18 686 = true := by decide +kernel
theorem c687 : check 56 101 18 687 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 672 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c672) (chunksOK_one c673)) (chunksOK_append (chunksOK_one c674) (chunksOK_one c675))) (chunksOK_append (chunksOK_append (chunksOK_one c676) (chunksOK_one c677)) (chunksOK_append (chunksOK_one c678) (chunksOK_one c679)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c680) (chunksOK_one c681)) (chunksOK_append (chunksOK_one c682) (chunksOK_one c683))) (chunksOK_append (chunksOK_append (chunksOK_one c684) (chunksOK_one c685)) (chunksOK_append (chunksOK_one c686) (chunksOK_one c687)))))

end C42

namespace C43

theorem c688 : check 56 101 18 688 = true := by decide +kernel
theorem c689 : check 56 101 18 689 = true := by decide +kernel
theorem c690 : check 56 101 18 690 = true := by decide +kernel
theorem c691 : check 56 101 18 691 = true := by decide +kernel
theorem c692 : check 56 101 18 692 = true := by decide +kernel
theorem c693 : check 56 101 18 693 = true := by decide +kernel
theorem c694 : check 56 101 18 694 = true := by decide +kernel
theorem c695 : check 56 101 18 695 = true := by decide +kernel
theorem c696 : check 56 101 18 696 = true := by decide +kernel
theorem c697 : check 56 101 18 697 = true := by decide +kernel
theorem c698 : check 56 101 18 698 = true := by decide +kernel
theorem c699 : check 56 101 18 699 = true := by decide +kernel
theorem c700 : check 56 101 18 700 = true := by decide +kernel
theorem c701 : check 56 101 18 701 = true := by decide +kernel
theorem c702 : check 56 101 18 702 = true := by decide +kernel
theorem c703 : check 56 101 18 703 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 688 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c688) (chunksOK_one c689)) (chunksOK_append (chunksOK_one c690) (chunksOK_one c691))) (chunksOK_append (chunksOK_append (chunksOK_one c692) (chunksOK_one c693)) (chunksOK_append (chunksOK_one c694) (chunksOK_one c695)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c696) (chunksOK_one c697)) (chunksOK_append (chunksOK_one c698) (chunksOK_one c699))) (chunksOK_append (chunksOK_append (chunksOK_one c700) (chunksOK_one c701)) (chunksOK_append (chunksOK_one c702) (chunksOK_one c703)))))

end C43

namespace C44

theorem c704 : check 56 101 18 704 = true := by decide +kernel
theorem c705 : check 56 101 18 705 = true := by decide +kernel
theorem c706 : check 56 101 18 706 = true := by decide +kernel
theorem c707 : check 56 101 18 707 = true := by decide +kernel
theorem c708 : check 56 101 18 708 = true := by decide +kernel
theorem c709 : check 56 101 18 709 = true := by decide +kernel
theorem c710 : check 56 101 18 710 = true := by decide +kernel
theorem c711 : check 56 101 18 711 = true := by decide +kernel
theorem c712 : check 56 101 18 712 = true := by decide +kernel
theorem c713 : check 56 101 18 713 = true := by decide +kernel
theorem c714 : check 56 101 18 714 = true := by decide +kernel
theorem c715 : check 56 101 18 715 = true := by decide +kernel
theorem c716 : check 56 101 18 716 = true := by decide +kernel
theorem c717 : check 56 101 18 717 = true := by decide +kernel
theorem c718 : check 56 101 18 718 = true := by decide +kernel
theorem c719 : check 56 101 18 719 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 704 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c704) (chunksOK_one c705)) (chunksOK_append (chunksOK_one c706) (chunksOK_one c707))) (chunksOK_append (chunksOK_append (chunksOK_one c708) (chunksOK_one c709)) (chunksOK_append (chunksOK_one c710) (chunksOK_one c711)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c712) (chunksOK_one c713)) (chunksOK_append (chunksOK_one c714) (chunksOK_one c715))) (chunksOK_append (chunksOK_append (chunksOK_one c716) (chunksOK_one c717)) (chunksOK_append (chunksOK_one c718) (chunksOK_one c719)))))

end C44

namespace C45

theorem c720 : check 56 101 18 720 = true := by decide +kernel
theorem c721 : check 56 101 18 721 = true := by decide +kernel
theorem c722 : check 56 101 18 722 = true := by decide +kernel
theorem c723 : check 56 101 18 723 = true := by decide +kernel
theorem c724 : check 56 101 18 724 = true := by decide +kernel
theorem c725 : check 56 101 18 725 = true := by decide +kernel
theorem c726 : check 56 101 18 726 = true := by decide +kernel
theorem c727 : check 56 101 18 727 = true := by decide +kernel
theorem c728 : check 56 101 18 728 = true := by decide +kernel
theorem c729 : check 56 101 18 729 = true := by decide +kernel
theorem c730 : check 56 101 18 730 = true := by decide +kernel
theorem c731 : check 56 101 18 731 = true := by decide +kernel
theorem c732 : check 56 101 18 732 = true := by decide +kernel
theorem c733 : check 56 101 18 733 = true := by decide +kernel
theorem c734 : check 56 101 18 734 = true := by decide +kernel
theorem c735 : check 56 101 18 735 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 720 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c720) (chunksOK_one c721)) (chunksOK_append (chunksOK_one c722) (chunksOK_one c723))) (chunksOK_append (chunksOK_append (chunksOK_one c724) (chunksOK_one c725)) (chunksOK_append (chunksOK_one c726) (chunksOK_one c727)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c728) (chunksOK_one c729)) (chunksOK_append (chunksOK_one c730) (chunksOK_one c731))) (chunksOK_append (chunksOK_append (chunksOK_one c732) (chunksOK_one c733)) (chunksOK_append (chunksOK_one c734) (chunksOK_one c735)))))

end C45

namespace C46

theorem c736 : check 56 101 18 736 = true := by decide +kernel
theorem c737 : check 56 101 18 737 = true := by decide +kernel
theorem c738 : check 56 101 18 738 = true := by decide +kernel
theorem c739 : check 56 101 18 739 = true := by decide +kernel
theorem c740 : check 56 101 18 740 = true := by decide +kernel
theorem c741 : check 56 101 18 741 = true := by decide +kernel
theorem c742 : check 56 101 18 742 = true := by decide +kernel
theorem c743 : check 56 101 18 743 = true := by decide +kernel
theorem c744 : check 56 101 18 744 = true := by decide +kernel
theorem c745 : check 56 101 18 745 = true := by decide +kernel
theorem c746 : check 56 101 18 746 = true := by decide +kernel
theorem c747 : check 56 101 18 747 = true := by decide +kernel
theorem c748 : check 56 101 18 748 = true := by decide +kernel
theorem c749 : check 56 101 18 749 = true := by decide +kernel
theorem c750 : check 56 101 18 750 = true := by decide +kernel
theorem c751 : check 56 101 18 751 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 736 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c736) (chunksOK_one c737)) (chunksOK_append (chunksOK_one c738) (chunksOK_one c739))) (chunksOK_append (chunksOK_append (chunksOK_one c740) (chunksOK_one c741)) (chunksOK_append (chunksOK_one c742) (chunksOK_one c743)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c744) (chunksOK_one c745)) (chunksOK_append (chunksOK_one c746) (chunksOK_one c747))) (chunksOK_append (chunksOK_append (chunksOK_one c748) (chunksOK_one c749)) (chunksOK_append (chunksOK_one c750) (chunksOK_one c751)))))

end C46

namespace C47

theorem c752 : check 56 101 18 752 = true := by decide +kernel
theorem c753 : check 56 101 18 753 = true := by decide +kernel
theorem c754 : check 56 101 18 754 = true := by decide +kernel
theorem c755 : check 56 101 18 755 = true := by decide +kernel
theorem c756 : check 56 101 18 756 = true := by decide +kernel
theorem c757 : check 56 101 18 757 = true := by decide +kernel
theorem c758 : check 56 101 18 758 = true := by decide +kernel
theorem c759 : check 56 101 18 759 = true := by decide +kernel
theorem c760 : check 56 101 18 760 = true := by decide +kernel
theorem c761 : check 56 101 18 761 = true := by decide +kernel
theorem c762 : check 56 101 18 762 = true := by decide +kernel
theorem c763 : check 56 101 18 763 = true := by decide +kernel
theorem c764 : check 56 101 18 764 = true := by decide +kernel
theorem c765 : check 56 101 18 765 = true := by decide +kernel
theorem c766 : check 56 101 18 766 = true := by decide +kernel
theorem c767 : check 56 101 18 767 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 752 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c752) (chunksOK_one c753)) (chunksOK_append (chunksOK_one c754) (chunksOK_one c755))) (chunksOK_append (chunksOK_append (chunksOK_one c756) (chunksOK_one c757)) (chunksOK_append (chunksOK_one c758) (chunksOK_one c759)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c760) (chunksOK_one c761)) (chunksOK_append (chunksOK_one c762) (chunksOK_one c763))) (chunksOK_append (chunksOK_append (chunksOK_one c764) (chunksOK_one c765)) (chunksOK_append (chunksOK_one c766) (chunksOK_one c767)))))

end C47

namespace C48

theorem c768 : check 56 101 18 768 = true := by decide +kernel
theorem c769 : check 56 101 18 769 = true := by decide +kernel
theorem c770 : check 56 101 18 770 = true := by decide +kernel
theorem c771 : check 56 101 18 771 = true := by decide +kernel
theorem c772 : check 56 101 18 772 = true := by decide +kernel
theorem c773 : check 56 101 18 773 = true := by decide +kernel
theorem c774 : check 56 101 18 774 = true := by decide +kernel
theorem c775 : check 56 101 18 775 = true := by decide +kernel
theorem c776 : check 56 101 18 776 = true := by decide +kernel
theorem c777 : check 56 101 18 777 = true := by decide +kernel
theorem c778 : check 56 101 18 778 = true := by decide +kernel
theorem c779 : check 56 101 18 779 = true := by decide +kernel
theorem c780 : check 56 101 18 780 = true := by decide +kernel
theorem c781 : check 56 101 18 781 = true := by decide +kernel
theorem c782 : check 56 101 18 782 = true := by decide +kernel
theorem c783 : check 56 101 18 783 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 768 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c768) (chunksOK_one c769)) (chunksOK_append (chunksOK_one c770) (chunksOK_one c771))) (chunksOK_append (chunksOK_append (chunksOK_one c772) (chunksOK_one c773)) (chunksOK_append (chunksOK_one c774) (chunksOK_one c775)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c776) (chunksOK_one c777)) (chunksOK_append (chunksOK_one c778) (chunksOK_one c779))) (chunksOK_append (chunksOK_append (chunksOK_one c780) (chunksOK_one c781)) (chunksOK_append (chunksOK_one c782) (chunksOK_one c783)))))

end C48

namespace C49

theorem c784 : check 56 101 18 784 = true := by decide +kernel
theorem c785 : check 56 101 18 785 = true := by decide +kernel
theorem c786 : check 56 101 18 786 = true := by decide +kernel
theorem c787 : check 56 101 18 787 = true := by decide +kernel
theorem c788 : check 56 101 18 788 = true := by decide +kernel
theorem c789 : check 56 101 18 789 = true := by decide +kernel
theorem c790 : check 56 101 18 790 = true := by decide +kernel
theorem c791 : check 56 101 18 791 = true := by decide +kernel
theorem c792 : check 56 101 18 792 = true := by decide +kernel
theorem c793 : check 56 101 18 793 = true := by decide +kernel
theorem c794 : check 56 101 18 794 = true := by decide +kernel
theorem c795 : check 56 101 18 795 = true := by decide +kernel
theorem c796 : check 56 101 18 796 = true := by decide +kernel
theorem c797 : check 56 101 18 797 = true := by decide +kernel
theorem c798 : check 56 101 18 798 = true := by decide +kernel
theorem c799 : check 56 101 18 799 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 784 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c784) (chunksOK_one c785)) (chunksOK_append (chunksOK_one c786) (chunksOK_one c787))) (chunksOK_append (chunksOK_append (chunksOK_one c788) (chunksOK_one c789)) (chunksOK_append (chunksOK_one c790) (chunksOK_one c791)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c792) (chunksOK_one c793)) (chunksOK_append (chunksOK_one c794) (chunksOK_one c795))) (chunksOK_append (chunksOK_append (chunksOK_one c796) (chunksOK_one c797)) (chunksOK_append (chunksOK_one c798) (chunksOK_one c799)))))

end C49

namespace C50

theorem c800 : check 56 101 18 800 = true := by decide +kernel
theorem c801 : check 56 101 18 801 = true := by decide +kernel
theorem c802 : check 56 101 18 802 = true := by decide +kernel
theorem c803 : check 56 101 18 803 = true := by decide +kernel
theorem c804 : check 56 101 18 804 = true := by decide +kernel
theorem c805 : check 56 101 18 805 = true := by decide +kernel
theorem c806 : check 56 101 18 806 = true := by decide +kernel
theorem c807 : check 56 101 18 807 = true := by decide +kernel
theorem c808 : check 56 101 18 808 = true := by decide +kernel
theorem c809 : check 56 101 18 809 = true := by decide +kernel
theorem c810 : check 56 101 18 810 = true := by decide +kernel
theorem c811 : check 56 101 18 811 = true := by decide +kernel
theorem c812 : check 56 101 18 812 = true := by decide +kernel
theorem c813 : check 56 101 18 813 = true := by decide +kernel
theorem c814 : check 56 101 18 814 = true := by decide +kernel
theorem c815 : check 56 101 18 815 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 800 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c800) (chunksOK_one c801)) (chunksOK_append (chunksOK_one c802) (chunksOK_one c803))) (chunksOK_append (chunksOK_append (chunksOK_one c804) (chunksOK_one c805)) (chunksOK_append (chunksOK_one c806) (chunksOK_one c807)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c808) (chunksOK_one c809)) (chunksOK_append (chunksOK_one c810) (chunksOK_one c811))) (chunksOK_append (chunksOK_append (chunksOK_one c812) (chunksOK_one c813)) (chunksOK_append (chunksOK_one c814) (chunksOK_one c815)))))

end C50

namespace C51

theorem c816 : check 56 101 18 816 = true := by decide +kernel
theorem c817 : check 56 101 18 817 = true := by decide +kernel
theorem c818 : check 56 101 18 818 = true := by decide +kernel
theorem c819 : check 56 101 18 819 = true := by decide +kernel
theorem c820 : check 56 101 18 820 = true := by decide +kernel
theorem c821 : check 56 101 18 821 = true := by decide +kernel
theorem c822 : check 56 101 18 822 = true := by decide +kernel
theorem c823 : check 56 101 18 823 = true := by decide +kernel
theorem c824 : check 56 101 18 824 = true := by decide +kernel
theorem c825 : check 56 101 18 825 = true := by decide +kernel
theorem c826 : check 56 101 18 826 = true := by decide +kernel
theorem c827 : check 56 101 18 827 = true := by decide +kernel
theorem c828 : check 56 101 18 828 = true := by decide +kernel
theorem c829 : check 56 101 18 829 = true := by decide +kernel
theorem c830 : check 56 101 18 830 = true := by decide +kernel
theorem c831 : check 56 101 18 831 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 816 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c816) (chunksOK_one c817)) (chunksOK_append (chunksOK_one c818) (chunksOK_one c819))) (chunksOK_append (chunksOK_append (chunksOK_one c820) (chunksOK_one c821)) (chunksOK_append (chunksOK_one c822) (chunksOK_one c823)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c824) (chunksOK_one c825)) (chunksOK_append (chunksOK_one c826) (chunksOK_one c827))) (chunksOK_append (chunksOK_append (chunksOK_one c828) (chunksOK_one c829)) (chunksOK_append (chunksOK_one c830) (chunksOK_one c831)))))

end C51

namespace C52

theorem c832 : check 56 101 18 832 = true := by decide +kernel
theorem c833 : check 56 101 18 833 = true := by decide +kernel
theorem c834 : check 56 101 18 834 = true := by decide +kernel
theorem c835 : check 56 101 18 835 = true := by decide +kernel
theorem c836 : check 56 101 18 836 = true := by decide +kernel
theorem c837 : check 56 101 18 837 = true := by decide +kernel
theorem c838 : check 56 101 18 838 = true := by decide +kernel
theorem c839 : check 56 101 18 839 = true := by decide +kernel
theorem c840 : check 56 101 18 840 = true := by decide +kernel
theorem c841 : check 56 101 18 841 = true := by decide +kernel
theorem c842 : check 56 101 18 842 = true := by decide +kernel
theorem c843 : check 56 101 18 843 = true := by decide +kernel
theorem c844 : check 56 101 18 844 = true := by decide +kernel
theorem c845 : check 56 101 18 845 = true := by decide +kernel
theorem c846 : check 56 101 18 846 = true := by decide +kernel
theorem c847 : check 56 101 18 847 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 832 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c832) (chunksOK_one c833)) (chunksOK_append (chunksOK_one c834) (chunksOK_one c835))) (chunksOK_append (chunksOK_append (chunksOK_one c836) (chunksOK_one c837)) (chunksOK_append (chunksOK_one c838) (chunksOK_one c839)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c840) (chunksOK_one c841)) (chunksOK_append (chunksOK_one c842) (chunksOK_one c843))) (chunksOK_append (chunksOK_append (chunksOK_one c844) (chunksOK_one c845)) (chunksOK_append (chunksOK_one c846) (chunksOK_one c847)))))

end C52

namespace C53

theorem c848 : check 56 101 18 848 = true := by decide +kernel
theorem c849 : check 56 101 18 849 = true := by decide +kernel
theorem c850 : check 56 101 18 850 = true := by decide +kernel
theorem c851 : check 56 101 18 851 = true := by decide +kernel
theorem c852 : check 56 101 18 852 = true := by decide +kernel
theorem c853 : check 56 101 18 853 = true := by decide +kernel
theorem c854 : check 56 101 18 854 = true := by decide +kernel
theorem c855 : check 56 101 18 855 = true := by decide +kernel
theorem c856 : check 56 101 18 856 = true := by decide +kernel
theorem c857 : check 56 101 18 857 = true := by decide +kernel
theorem c858 : check 56 101 18 858 = true := by decide +kernel
theorem c859 : check 56 101 18 859 = true := by decide +kernel
theorem c860 : check 56 101 18 860 = true := by decide +kernel
theorem c861 : check 56 101 18 861 = true := by decide +kernel
theorem c862 : check 56 101 18 862 = true := by decide +kernel
theorem c863 : check 56 101 18 863 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 848 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c848) (chunksOK_one c849)) (chunksOK_append (chunksOK_one c850) (chunksOK_one c851))) (chunksOK_append (chunksOK_append (chunksOK_one c852) (chunksOK_one c853)) (chunksOK_append (chunksOK_one c854) (chunksOK_one c855)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c856) (chunksOK_one c857)) (chunksOK_append (chunksOK_one c858) (chunksOK_one c859))) (chunksOK_append (chunksOK_append (chunksOK_one c860) (chunksOK_one c861)) (chunksOK_append (chunksOK_one c862) (chunksOK_one c863)))))

end C53

namespace C54

theorem c864 : check 56 101 18 864 = true := by decide +kernel
theorem c865 : check 56 101 18 865 = true := by decide +kernel
theorem c866 : check 56 101 18 866 = true := by decide +kernel
theorem c867 : check 56 101 18 867 = true := by decide +kernel
theorem c868 : check 56 101 18 868 = true := by decide +kernel
theorem c869 : check 56 101 18 869 = true := by decide +kernel
theorem c870 : check 56 101 18 870 = true := by decide +kernel
theorem c871 : check 56 101 18 871 = true := by decide +kernel
theorem c872 : check 56 101 18 872 = true := by decide +kernel
theorem c873 : check 56 101 18 873 = true := by decide +kernel
theorem c874 : check 56 101 18 874 = true := by decide +kernel
theorem c875 : check 56 101 18 875 = true := by decide +kernel
theorem c876 : check 56 101 18 876 = true := by decide +kernel
theorem c877 : check 56 101 18 877 = true := by decide +kernel
theorem c878 : check 56 101 18 878 = true := by decide +kernel
theorem c879 : check 56 101 18 879 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 864 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c864) (chunksOK_one c865)) (chunksOK_append (chunksOK_one c866) (chunksOK_one c867))) (chunksOK_append (chunksOK_append (chunksOK_one c868) (chunksOK_one c869)) (chunksOK_append (chunksOK_one c870) (chunksOK_one c871)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c872) (chunksOK_one c873)) (chunksOK_append (chunksOK_one c874) (chunksOK_one c875))) (chunksOK_append (chunksOK_append (chunksOK_one c876) (chunksOK_one c877)) (chunksOK_append (chunksOK_one c878) (chunksOK_one c879)))))

end C54

namespace C55

theorem c880 : check 56 101 18 880 = true := by decide +kernel
theorem c881 : check 56 101 18 881 = true := by decide +kernel
theorem c882 : check 56 101 18 882 = true := by decide +kernel
theorem c883 : check 56 101 18 883 = true := by decide +kernel
theorem c884 : check 56 101 18 884 = true := by decide +kernel
theorem c885 : check 56 101 18 885 = true := by decide +kernel
theorem c886 : check 56 101 18 886 = true := by decide +kernel
theorem c887 : check 56 101 18 887 = true := by decide +kernel
theorem c888 : check 56 101 18 888 = true := by decide +kernel
theorem c889 : check 56 101 18 889 = true := by decide +kernel
theorem c890 : check 56 101 18 890 = true := by decide +kernel
theorem c891 : check 56 101 18 891 = true := by decide +kernel
theorem c892 : check 56 101 18 892 = true := by decide +kernel
theorem c893 : check 56 101 18 893 = true := by decide +kernel
theorem c894 : check 56 101 18 894 = true := by decide +kernel
theorem c895 : check 56 101 18 895 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 880 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c880) (chunksOK_one c881)) (chunksOK_append (chunksOK_one c882) (chunksOK_one c883))) (chunksOK_append (chunksOK_append (chunksOK_one c884) (chunksOK_one c885)) (chunksOK_append (chunksOK_one c886) (chunksOK_one c887)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c888) (chunksOK_one c889)) (chunksOK_append (chunksOK_one c890) (chunksOK_one c891))) (chunksOK_append (chunksOK_append (chunksOK_one c892) (chunksOK_one c893)) (chunksOK_append (chunksOK_one c894) (chunksOK_one c895)))))

end C55

namespace C56

theorem c896 : check 56 101 18 896 = true := by decide +kernel
theorem c897 : check 56 101 18 897 = true := by decide +kernel
theorem c898 : check 56 101 18 898 = true := by decide +kernel
theorem c899 : check 56 101 18 899 = true := by decide +kernel
theorem c900 : check 56 101 18 900 = true := by decide +kernel
theorem c901 : check 56 101 18 901 = true := by decide +kernel
theorem c902 : check 56 101 18 902 = true := by decide +kernel
theorem c903 : check 56 101 18 903 = true := by decide +kernel
theorem c904 : check 56 101 18 904 = true := by decide +kernel
theorem c905 : check 56 101 18 905 = true := by decide +kernel
theorem c906 : check 56 101 18 906 = true := by decide +kernel
theorem c907 : check 56 101 18 907 = true := by decide +kernel
theorem c908 : check 56 101 18 908 = true := by decide +kernel
theorem c909 : check 56 101 18 909 = true := by decide +kernel
theorem c910 : check 56 101 18 910 = true := by decide +kernel
theorem c911 : check 56 101 18 911 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 896 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c896) (chunksOK_one c897)) (chunksOK_append (chunksOK_one c898) (chunksOK_one c899))) (chunksOK_append (chunksOK_append (chunksOK_one c900) (chunksOK_one c901)) (chunksOK_append (chunksOK_one c902) (chunksOK_one c903)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c904) (chunksOK_one c905)) (chunksOK_append (chunksOK_one c906) (chunksOK_one c907))) (chunksOK_append (chunksOK_append (chunksOK_one c908) (chunksOK_one c909)) (chunksOK_append (chunksOK_one c910) (chunksOK_one c911)))))

end C56

namespace C57

theorem c912 : check 56 101 18 912 = true := by decide +kernel
theorem c913 : check 56 101 18 913 = true := by decide +kernel
theorem c914 : check 56 101 18 914 = true := by decide +kernel
theorem c915 : check 56 101 18 915 = true := by decide +kernel
theorem c916 : check 56 101 18 916 = true := by decide +kernel
theorem c917 : check 56 101 18 917 = true := by decide +kernel
theorem c918 : check 56 101 18 918 = true := by decide +kernel
theorem c919 : check 56 101 18 919 = true := by decide +kernel
theorem c920 : check 56 101 18 920 = true := by decide +kernel
theorem c921 : check 56 101 18 921 = true := by decide +kernel
theorem c922 : check 56 101 18 922 = true := by decide +kernel
theorem c923 : check 56 101 18 923 = true := by decide +kernel
theorem c924 : check 56 101 18 924 = true := by decide +kernel
theorem c925 : check 56 101 18 925 = true := by decide +kernel
theorem c926 : check 56 101 18 926 = true := by decide +kernel
theorem c927 : check 56 101 18 927 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 912 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c912) (chunksOK_one c913)) (chunksOK_append (chunksOK_one c914) (chunksOK_one c915))) (chunksOK_append (chunksOK_append (chunksOK_one c916) (chunksOK_one c917)) (chunksOK_append (chunksOK_one c918) (chunksOK_one c919)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c920) (chunksOK_one c921)) (chunksOK_append (chunksOK_one c922) (chunksOK_one c923))) (chunksOK_append (chunksOK_append (chunksOK_one c924) (chunksOK_one c925)) (chunksOK_append (chunksOK_one c926) (chunksOK_one c927)))))

end C57

namespace C58

theorem c928 : check 56 101 18 928 = true := by decide +kernel
theorem c929 : check 56 101 18 929 = true := by decide +kernel
theorem c930 : check 56 101 18 930 = true := by decide +kernel
theorem c931 : check 56 101 18 931 = true := by decide +kernel
theorem c932 : check 56 101 18 932 = true := by decide +kernel
theorem c933 : check 56 101 18 933 = true := by decide +kernel
theorem c934 : check 56 101 18 934 = true := by decide +kernel
theorem c935 : check 56 101 18 935 = true := by decide +kernel
theorem c936 : check 56 101 18 936 = true := by decide +kernel
theorem c937 : check 56 101 18 937 = true := by decide +kernel
theorem c938 : check 56 101 18 938 = true := by decide +kernel
theorem c939 : check 56 101 18 939 = true := by decide +kernel
theorem c940 : check 56 101 18 940 = true := by decide +kernel
theorem c941 : check 56 101 18 941 = true := by decide +kernel
theorem c942 : check 56 101 18 942 = true := by decide +kernel
theorem c943 : check 56 101 18 943 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 928 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c928) (chunksOK_one c929)) (chunksOK_append (chunksOK_one c930) (chunksOK_one c931))) (chunksOK_append (chunksOK_append (chunksOK_one c932) (chunksOK_one c933)) (chunksOK_append (chunksOK_one c934) (chunksOK_one c935)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c936) (chunksOK_one c937)) (chunksOK_append (chunksOK_one c938) (chunksOK_one c939))) (chunksOK_append (chunksOK_append (chunksOK_one c940) (chunksOK_one c941)) (chunksOK_append (chunksOK_one c942) (chunksOK_one c943)))))

end C58

namespace C59

theorem c944 : check 56 101 18 944 = true := by decide +kernel
theorem c945 : check 56 101 18 945 = true := by decide +kernel
theorem c946 : check 56 101 18 946 = true := by decide +kernel
theorem c947 : check 56 101 18 947 = true := by decide +kernel
theorem c948 : check 56 101 18 948 = true := by decide +kernel
theorem c949 : check 56 101 18 949 = true := by decide +kernel
theorem c950 : check 56 101 18 950 = true := by decide +kernel
theorem c951 : check 56 101 18 951 = true := by decide +kernel
theorem c952 : check 56 101 18 952 = true := by decide +kernel
theorem c953 : check 56 101 18 953 = true := by decide +kernel
theorem c954 : check 56 101 18 954 = true := by decide +kernel
theorem c955 : check 56 101 18 955 = true := by decide +kernel
theorem c956 : check 56 101 18 956 = true := by decide +kernel
theorem c957 : check 56 101 18 957 = true := by decide +kernel
theorem c958 : check 56 101 18 958 = true := by decide +kernel
theorem c959 : check 56 101 18 959 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 944 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c944) (chunksOK_one c945)) (chunksOK_append (chunksOK_one c946) (chunksOK_one c947))) (chunksOK_append (chunksOK_append (chunksOK_one c948) (chunksOK_one c949)) (chunksOK_append (chunksOK_one c950) (chunksOK_one c951)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c952) (chunksOK_one c953)) (chunksOK_append (chunksOK_one c954) (chunksOK_one c955))) (chunksOK_append (chunksOK_append (chunksOK_one c956) (chunksOK_one c957)) (chunksOK_append (chunksOK_one c958) (chunksOK_one c959)))))

end C59

namespace C60

theorem c960 : check 56 101 18 960 = true := by decide +kernel
theorem c961 : check 56 101 18 961 = true := by decide +kernel
theorem c962 : check 56 101 18 962 = true := by decide +kernel
theorem c963 : check 56 101 18 963 = true := by decide +kernel
theorem c964 : check 56 101 18 964 = true := by decide +kernel
theorem c965 : check 56 101 18 965 = true := by decide +kernel
theorem c966 : check 56 101 18 966 = true := by decide +kernel
theorem c967 : check 56 101 18 967 = true := by decide +kernel
theorem c968 : check 56 101 18 968 = true := by decide +kernel
theorem c969 : check 56 101 18 969 = true := by decide +kernel
theorem c970 : check 56 101 18 970 = true := by decide +kernel
theorem c971 : check 56 101 18 971 = true := by decide +kernel
theorem c972 : check 56 101 18 972 = true := by decide +kernel
theorem c973 : check 56 101 18 973 = true := by decide +kernel
theorem c974 : check 56 101 18 974 = true := by decide +kernel
theorem c975 : check 56 101 18 975 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 960 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c960) (chunksOK_one c961)) (chunksOK_append (chunksOK_one c962) (chunksOK_one c963))) (chunksOK_append (chunksOK_append (chunksOK_one c964) (chunksOK_one c965)) (chunksOK_append (chunksOK_one c966) (chunksOK_one c967)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c968) (chunksOK_one c969)) (chunksOK_append (chunksOK_one c970) (chunksOK_one c971))) (chunksOK_append (chunksOK_append (chunksOK_one c972) (chunksOK_one c973)) (chunksOK_append (chunksOK_one c974) (chunksOK_one c975)))))

end C60

namespace C61

theorem c976 : check 56 101 18 976 = true := by decide +kernel
theorem c977 : check 56 101 18 977 = true := by decide +kernel
theorem c978 : check 56 101 18 978 = true := by decide +kernel
theorem c979 : check 56 101 18 979 = true := by decide +kernel
theorem c980 : check 56 101 18 980 = true := by decide +kernel
theorem c981 : check 56 101 18 981 = true := by decide +kernel
theorem c982 : check 56 101 18 982 = true := by decide +kernel
theorem c983 : check 56 101 18 983 = true := by decide +kernel
theorem c984 : check 56 101 18 984 = true := by decide +kernel
theorem c985 : check 56 101 18 985 = true := by decide +kernel
theorem c986 : check 56 101 18 986 = true := by decide +kernel
theorem c987 : check 56 101 18 987 = true := by decide +kernel
theorem c988 : check 56 101 18 988 = true := by decide +kernel
theorem c989 : check 56 101 18 989 = true := by decide +kernel
theorem c990 : check 56 101 18 990 = true := by decide +kernel
theorem c991 : check 56 101 18 991 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 976 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c976) (chunksOK_one c977)) (chunksOK_append (chunksOK_one c978) (chunksOK_one c979))) (chunksOK_append (chunksOK_append (chunksOK_one c980) (chunksOK_one c981)) (chunksOK_append (chunksOK_one c982) (chunksOK_one c983)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c984) (chunksOK_one c985)) (chunksOK_append (chunksOK_one c986) (chunksOK_one c987))) (chunksOK_append (chunksOK_append (chunksOK_one c988) (chunksOK_one c989)) (chunksOK_append (chunksOK_one c990) (chunksOK_one c991)))))

end C61

namespace C62

theorem c992 : check 56 101 18 992 = true := by decide +kernel
theorem c993 : check 56 101 18 993 = true := by decide +kernel
theorem c994 : check 56 101 18 994 = true := by decide +kernel
theorem c995 : check 56 101 18 995 = true := by decide +kernel
theorem c996 : check 56 101 18 996 = true := by decide +kernel
theorem c997 : check 56 101 18 997 = true := by decide +kernel
theorem c998 : check 56 101 18 998 = true := by decide +kernel
theorem c999 : check 56 101 18 999 = true := by decide +kernel
theorem c1000 : check 56 101 18 1000 = true := by decide +kernel
theorem c1001 : check 56 101 18 1001 = true := by decide +kernel
theorem c1002 : check 56 101 18 1002 = true := by decide +kernel
theorem c1003 : check 56 101 18 1003 = true := by decide +kernel
theorem c1004 : check 56 101 18 1004 = true := by decide +kernel
theorem c1005 : check 56 101 18 1005 = true := by decide +kernel
theorem c1006 : check 56 101 18 1006 = true := by decide +kernel
theorem c1007 : check 56 101 18 1007 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 992 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c992) (chunksOK_one c993)) (chunksOK_append (chunksOK_one c994) (chunksOK_one c995))) (chunksOK_append (chunksOK_append (chunksOK_one c996) (chunksOK_one c997)) (chunksOK_append (chunksOK_one c998) (chunksOK_one c999)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1000) (chunksOK_one c1001)) (chunksOK_append (chunksOK_one c1002) (chunksOK_one c1003))) (chunksOK_append (chunksOK_append (chunksOK_one c1004) (chunksOK_one c1005)) (chunksOK_append (chunksOK_one c1006) (chunksOK_one c1007)))))

end C62

namespace C63

theorem c1008 : check 56 101 18 1008 = true := by decide +kernel
theorem c1009 : check 56 101 18 1009 = true := by decide +kernel
theorem c1010 : check 56 101 18 1010 = true := by decide +kernel
theorem c1011 : check 56 101 18 1011 = true := by decide +kernel
theorem c1012 : check 56 101 18 1012 = true := by decide +kernel
theorem c1013 : check 56 101 18 1013 = true := by decide +kernel
theorem c1014 : check 56 101 18 1014 = true := by decide +kernel
theorem c1015 : check 56 101 18 1015 = true := by decide +kernel
theorem c1016 : check 56 101 18 1016 = true := by decide +kernel
theorem c1017 : check 56 101 18 1017 = true := by decide +kernel
theorem c1018 : check 56 101 18 1018 = true := by decide +kernel
theorem c1019 : check 56 101 18 1019 = true := by decide +kernel
theorem c1020 : check 56 101 18 1020 = true := by decide +kernel
theorem c1021 : check 56 101 18 1021 = true := by decide +kernel
theorem c1022 : check 56 101 18 1022 = true := by decide +kernel
theorem c1023 : check 56 101 18 1023 = true := by decide +kernel

theorem range : ChunksOK 56 101 18 1008 16 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1008) (chunksOK_one c1009)) (chunksOK_append (chunksOK_one c1010) (chunksOK_one c1011))) (chunksOK_append (chunksOK_append (chunksOK_one c1012) (chunksOK_one c1013)) (chunksOK_append (chunksOK_one c1014) (chunksOK_one c1015)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_one c1016) (chunksOK_one c1017)) (chunksOK_append (chunksOK_one c1018) (chunksOK_one c1019))) (chunksOK_append (chunksOK_append (chunksOK_one c1020) (chunksOK_one c1021)) (chunksOK_append (chunksOK_one c1022) (chunksOK_one c1023)))))

end C63

/-! ## The assembled upper bound -/

theorem all_chunks : ChunksOK 56 101 18 0 1024 :=
  (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append C0.range C1.range) (chunksOK_append C2.range C3.range)) (chunksOK_append (chunksOK_append C4.range C5.range) (chunksOK_append C6.range C7.range))) (chunksOK_append (chunksOK_append (chunksOK_append C8.range C9.range) (chunksOK_append C10.range C11.range)) (chunksOK_append (chunksOK_append C12.range C13.range) (chunksOK_append C14.range C15.range)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append C16.range C17.range) (chunksOK_append C18.range C19.range)) (chunksOK_append (chunksOK_append C20.range C21.range) (chunksOK_append C22.range C23.range))) (chunksOK_append (chunksOK_append (chunksOK_append C24.range C25.range) (chunksOK_append C26.range C27.range)) (chunksOK_append (chunksOK_append C28.range C29.range) (chunksOK_append C30.range C31.range))))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append C32.range C33.range) (chunksOK_append C34.range C35.range)) (chunksOK_append (chunksOK_append C36.range C37.range) (chunksOK_append C38.range C39.range))) (chunksOK_append (chunksOK_append (chunksOK_append C40.range C41.range) (chunksOK_append C42.range C43.range)) (chunksOK_append (chunksOK_append C44.range C45.range) (chunksOK_append C46.range C47.range)))) (chunksOK_append (chunksOK_append (chunksOK_append (chunksOK_append C48.range C49.range) (chunksOK_append C50.range C51.range)) (chunksOK_append (chunksOK_append C52.range C53.range) (chunksOK_append C54.range C55.range))) (chunksOK_append (chunksOK_append (chunksOK_append C56.range C57.range) (chunksOK_append C58.range C59.range)) (chunksOK_append (chunksOK_append C60.range C61.range) (chunksOK_append C62.range C63.range))))))

/-- Every start supported at depths at most 56 has a white depth-1 cell at an even time at most 100. -/
theorem q01_width_le_56 (x : Nat → Bool) (hx : ∀ k, 56 < k → x k = false) :
    ∃ t, t ≤ 100 ∧ t % 2 = 0 ∧ zrow x t 1 = false := by
  obtain ⟨t, ht, he, hz⟩ := q01_of_chunks 56 101 18 (by decide) all_chunks x hx
  exact ⟨t, by omega, he, hz⟩

/-! ## The witness -/

/-- The width-56 witness: 56 bits (bits are depths 1 .. 56). -/
def w56 : Nat := 0x93d4b223f5b9b5

theorem w56_lt : w56 < 2 ^ 56 := by decide

theorem toFun_width {r W : Nat} (h : r < 2 ^ W) (k : Nat) (hk : W < k) : toFun r k = false := by
  unfold toFun
  have h1 : k ≠ 0 := by omega
  simp only [h1, ite_false]
  exact testBit_ge_of_lt h (by omega)

theorem zrow_packed (r t : Nat) : zrow (toFun r) t 1 = (prun r t).testBit 0 := by
  rw [run_toFun]; rfl

/-- Black at depth 1 at every even time below 100: 50 packed orbits, kernel-evaluated. -/
theorem w56_black : ∀ s, s < 50 → (prun w56 (2 * s)).testBit 0 = true := by decide +kernel

theorem w56_white : (prun w56 100).testBit 0 = false := by decide +kernel

theorem w56_survives : ∀ t, t < 100 → t % 2 = 0 → zrow (toFun w56) t 1 = true := by
  intro t ht he
  rw [zrow_packed]
  obtain ⟨s, rfl⟩ : ∃ s, t = 2 * s := ⟨t / 2, by omega⟩
  exact w56_black s (by omega)

theorem w56_dies : zrow (toFun w56) 100 1 = false := by
  rw [zrow_packed]; exact w56_white

/-! ## The headline -/

/-- **The death time at width 56 is exactly 100.** -/
theorem death_time_56_exact :
    (∀ x : Nat → Bool, (∀ k, 56 < k → x k = false) → ∃ t, t ≤ 100 ∧ t % 2 = 0 ∧ zrow x t 1 = false) ∧
    (∃ x : Nat → Bool, (∀ k, 56 < k → x k = false) ∧ (∀ t, t < 100 → t % 2 = 0 → zrow x t 1 = true)) :=
  ⟨q01_width_le_56, ⟨toFun w56, toFun_width w56_lt, w56_survives⟩⟩

end Rule30Submission
