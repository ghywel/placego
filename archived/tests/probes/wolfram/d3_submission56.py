#!/usr/bin/env python3
"""Submission generator: the width-56 exact death time as ONE module, `Rule30Submission.lean`, carrying W2's 1,024 chunk
checks (`check 56 101 18 c = true` by `decide +kernel`, c = 0 .. 1023, in 64 sub-namespaces of 16 with `range` as the
balanced append tree, exactly the W2 generator's text per namespace), the wrapper (`all_chunks : ChunksOK 56 101 18 0
1024`, `q01_width_le_56` with t <= 100), the witness 0x93d4b223f5b9b5 through the kit's `prun` and `run_toFun`, and
`death_time_56_exact`. The verifier replays every declaration through the kernel, so this submission is also the test
of its time budget (the kit's own 256 checks at width 52 are the only precedent; W2 built the same 1,024 checks here
in 294 s across 16 modules). Usage: python3 d3_submission56.py OUT.lean
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import w2_harness as G

W, K, N = 56, 101, 18
CHUNKS = 1 << (W // 2 - N)          # 1024
NS = CHUNKS // G.PER_NS             # 64 namespaces of 16

head = f"""import Rule30PrizeKit
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
"""
body = []
for j in range(NS):
    lo = j * G.PER_NS
    body.append(f"namespace C{j}\n")
    for c in range(lo, lo + G.PER_NS):
        body.append(f"theorem c{c} : check {W} {K} {N} {c} = true := by decide +kernel")
    body.append(f"\ntheorem range : ChunksOK {W} {K} {N} {lo} {G.PER_NS} :=\n  " + G.append_tree([f"(chunksOK_one c{c})" for c in range(lo, lo + G.PER_NS)], None, None) + f"\n\nend C{j}\n")
tail = f"""
/-! ## The assembled upper bound -/

theorem all_chunks : ChunksOK {W} {K} {N} 0 {CHUNKS} :=
  {G.append_tree([f"C{j}.range" for j in range(NS)], None, None)}

/-- Every start supported at depths at most 56 has a white depth-1 cell at an even time at most 100. -/
theorem q01_width_le_56 (x : Nat → Bool) (hx : ∀ k, 56 < k → x k = false) :
    ∃ t, t ≤ 100 ∧ t % 2 = 0 ∧ zrow x t 1 = false := by
  obtain ⟨t, ht, he, hz⟩ := q01_of_chunks {W} {K} {N} (by decide) all_chunks x hx
  exact ⟨t, by omega, he, hz⟩

/-! ## The witness -/

/-- The width-56 witness: 56 bits (bits are depths 1 .. 56). -/
def w56 : Nat := 0x93d4b223f5b9b5

theorem w56_lt : w56 < 2 ^ 56 := by decide

theorem toFun_width {{r W : Nat}} (h : r < 2 ^ W) (k : Nat) (hk : W < k) : toFun r k = false := by
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
"""
text = head + "\n".join(body) + tail
open(sys.argv[1], 'w').write(text)
print('lines', text.count('\n'), 'checks', text.count('decide +kernel') - 2, 'bytes', len(text))
