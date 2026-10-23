#!/usr/bin/env python3
"""Submission generator (revision 2: parametrised by width; for W = 56 the generated module equals the submitted one (cc34baac…) in every declaration, differing only in comment wording (the header, the section title '1024' versus '1,024', and the witness docstring), which --test reports with both hashes): the exact death time at width W as ONE module, `Rule30Submission.lean`, carrying W2's 1,024 chunk
checks (`check 56 101 18 c = true` by `decide +kernel`, c = 0 .. 1023, in 64 sub-namespaces of 16 with `range` as the
balanced append tree, exactly the W2 generator's text per namespace), the wrapper (`all_chunks : ChunksOK 56 101 18 0
1024`, `q01_width_le_56` with t <= 100), the witness 0x93d4b223f5b9b5 through the kit's `prun` and `run_toFun`, and
`death_time_56_exact`. The verifier replays every declaration through the kernel, so this submission is also the test
of its time budget (the kit's own 256 checks at width 52 are the only precedent; W2 built the same 1,024 checks here
in 294 s across 16 modules). Usage: python3 d3_submission.py OUT.lean [W]   (W = 56 or 60; --test checks the width-56 text against revision 1)
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import w2_harness as G

CASES = {56: {'K': 101, 'U': 100, 'r': 0x93d4b223f5b9b5, 'prior': 'mentions that width 56 was also checked privately (1,024 checks, bound 100) and left out for build cost'},
         60: {'K': 115, 'U': 114, 'r': 0xe77a4e77b8f99b5, 'prior': 'has no width-60 statement; W3 of our record certified bound 128 (4,096 checks at K = 129) and the census found the true maximum 114'}}
W = int(sys.argv[2]) if len(sys.argv) > 2 else 56
K, U, R = CASES[W]['K'], CASES[W]['U'], CASES[W]['r']; N = 18
CHUNKS = 1 << (W // 2 - N)
NS = CHUNKS // G.PER_NS

head = f"""import Rule30PrizeKit
import Ruliology.CellularAutomata.Rule30ZeroBoundarySmall
import Ruliology.CellularAutomata.Rule30ZeroBoundaryLanes

/-!
# The death time at width {W} is exactly {U}: a complete chunk certificate and its witness

**Partial result on the kit's `Q01` (the period-2 question, Problem 1 of the Rule 30 Prize).** The kit proves `Q01`
for every zero-boundary start of width at most 52 (`Rule30ZeroBoundaryWidth52`, 256 chunk checks, bound 96) and
{CASES[W]['prior']}. This module
carries {CHUNKS} checks (`check {W} {K} 18 c = true`, each decided by the kernel, in {NS} namespaces of 16 with the
kit's `chunksOK_append` trees), assembles them by the kit's `q01_of_chunks` into `q01_width_le_{W}` (every start of
width at most {W} has a white depth-1 cell at an even time at most {U}), and proves the bound exact: the explicit
start `w{W}` is black at depth 1 at every even time below {U} and white at {U}, by the kit's packed evaluator `prun`
and its bridge `run_toFun` (`death_time_{W}_exact`).

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

/-! ## The {CHUNKS} chunk checks, kernel-decided -/
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

/-- Every start supported at depths at most {W} has a white depth-1 cell at an even time at most {U}. -/
theorem q01_width_le_{W} (x : Nat → Bool) (hx : ∀ k, {W} < k → x k = false) :
    ∃ t, t ≤ {U} ∧ t % 2 = 0 ∧ zrow x t 1 = false := by
  obtain ⟨t, ht, he, hz⟩ := q01_of_chunks {W} {K} {N} (by decide) all_chunks x hx
  exact ⟨t, by omega, he, hz⟩

/-! ## The witness -/

/-- The width-{W} witness ({R.bit_length()} bits; bits are depths 1 .. {W}). -/
def w{W} : Nat := {hex(R)}

theorem w{W}_lt : w{W} < 2 ^ {W} := by decide

theorem toFun_width {{r W : Nat}} (h : r < 2 ^ W) (k : Nat) (hk : W < k) : toFun r k = false := by
  unfold toFun
  have h1 : k ≠ 0 := by omega
  simp only [h1, ite_false]
  exact testBit_ge_of_lt h (by omega)

theorem zrow_packed (r t : Nat) : zrow (toFun r) t 1 = (prun r t).testBit 0 := by
  rw [run_toFun]; rfl

/-- Black at depth 1 at every even time below {U}: {U // 2} packed orbits, kernel-evaluated. -/
theorem w{W}_black : ∀ s, s < {U // 2} → (prun w{W} (2 * s)).testBit 0 = true := by decide +kernel

theorem w{W}_white : (prun w{W} {U}).testBit 0 = false := by decide +kernel

theorem w{W}_survives : ∀ t, t < {U} → t % 2 = 0 → zrow (toFun w{W}) t 1 = true := by
  intro t ht he
  rw [zrow_packed]
  obtain ⟨s, rfl⟩ : ∃ s, t = 2 * s := ⟨t / 2, by omega⟩
  exact w{W}_black s (by omega)

theorem w{W}_dies : zrow (toFun w{W}) {U} 1 = false := by
  rw [zrow_packed]; exact w{W}_white

/-! ## The headline -/

/-- **The death time at width {W} is exactly {U}.** -/
theorem death_time_{W}_exact :
    (∀ x : Nat → Bool, (∀ k, {W} < k → x k = false) → ∃ t, t ≤ {U} ∧ t % 2 = 0 ∧ zrow x t 1 = false) ∧
    (∃ x : Nat → Bool, (∀ k, {W} < k → x k = false) ∧ (∀ t, t < {U} → t % 2 = 0 → zrow x t 1 = true)) :=
  ⟨q01_width_le_{W}, ⟨toFun w{W}, toFun_width w{W}_lt, w{W}_survives⟩⟩

end Rule30Submission
"""
text = head + "\n".join(body) + tail
if sys.argv[1] == '--test':
    import hashlib, re; h = hashlib.sha256(text.encode()).hexdigest(); body = re.sub(r'/-!.*?-/', '', text, count=1, flags=re.S)
    bh = hashlib.sha256(body.encode()).hexdigest()
    strip = lambda t: re.sub(r'\s+', ' ', re.sub(r'/-.*?-/|--[^\n]*', '', t, flags=re.S)).strip()   # every comment removed, whitespace normalised
    sub = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../reports/wolfram-agents/submissions/d-exact-56/Rule30Submission.lean')
    if W != 56:
        print('--test compares only the width-56 regeneration; for W = %d it prints the hashes:' % W, h, bh); sys.exit(2)
    same = os.path.exists(sub) and strip(open(sub).read()) == strip(text)
    print('width-56 text sha256', h, '| the complete comment-free, whitespace-normalised source equals the submitted module (cc34baac…):', same)
    sys.exit(0 if same else 1)
open(sys.argv[1], 'w').write(text)
print('lines', text.count('\n'), 'checks', text.count('decide +kernel') - 2, 'bytes', len(text))
