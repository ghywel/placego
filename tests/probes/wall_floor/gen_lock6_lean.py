#!/usr/bin/env python3
"""gen_lock6_lean.py (Local, L1534): writes TwoPairsWallLockSix.lean: the 40 windows of 175 cells by phase, the six-phase cycle, the letters, and a witness row."""
import json
d=json.load(open('lock175.json'))
W=175
def nat(s): return sum(1<<i for i,c in enumerate(s) if c=='#')
ph=[d[str(i)] for i in range(6)]
letters=[]
for p in ph:
    t=p[0][-11:]
    letters.append('A' if t=='..####...##' else 'B')
L=[]
L.append('''import TwoPairsWindowClosed

/-!
# A third lock, with no fixed floor

Forty windows of 175 cells form a closed set under the backward tick for every pair of lower cells, and on them the letters run
`B`, `A`, `A` for ever (`lock_cycle`, `lock_letters`, `lock_forever`). These theorems give six phase classes;
the varying lower scar need not repeat after six ticks. Separate finite computations show that, unlike the 45- and
136-cell locks, no additional reset word occurs at one fixed depth in all forty windows, and the top projections lie
in the wider clouds tested. These computed shape/projection facts are not additional theorems of this file (GC2682).
-/

namespace TwoPairs.WallLockSix
open ThreeMoves (wordA wordB)
open WindowClosed

/-- A word of `W` cells from a number, low to high. -/
def dec (W n : Nat) : List Bool := (List.range W).map n.testBit

''')
for i,p in enumerate(ph):
    L.append(f'/-- Phase {i}, letter `{letters[i]}`. -/\ndef P{i} : List (List Bool) := [' + ', '.join(f'dec 175 {nat(w)}' for w in p) + ']\n')
L.append('''
/-- All forty windows. -/
def L175 : List (List Bool) := P0 ++ P1 ++ P2 ++ P3 ++ P4 ++ P5

theorem chk_mem : ∀ w, w ∈ L175 → ∀ p1 p2 : Bool, next 175 w p1 p2 ∈ L175 := by decide +kernel
theorem chk_a : ∀ w, w ∈ L175 → ∀ p1 p2 : Bool, (back p1 p2 (WindowClosed.inp 175 w)).getD 178 false = !(back p1 p2 (WindowClosed.inp 175 w)).getD 177 false := by decide +kernel
theorem chk_d : ∀ w, w ∈ L175 → ∀ p1 p2 : Bool, (back p1 p2 (WindowClosed.inp 175 w)).getD 179 false = !(back p1 p2 (WindowClosed.inp 175 w)).getD 178 false := by decide +kernel
theorem chk_b : ∀ w, w ∈ L175 → ∀ p1 p2 : Bool, (back p1 p2 (WindowClosed.inp 175 w)).getD 179 false = !(WindowClosed.inp 175 w).getD 179 false := by decide +kernel
theorem chk_c : ∀ w, w ∈ L175 → ∀ p1 p2 : Bool, (back p1 p2 (WindowClosed.inp 175 w)).getD 180 false = !(WindowClosed.inp 175 w).getD 180 false := by decide +kernel

/-- **The lock.** -/
theorem closed : Closed 175 L175 := ⟨by decide, chk_mem, chk_a, chk_d, chk_b, chk_c⟩

''')
for i in range(6):
    L.append(f'theorem chk_{i} : ∀ w, w ∈ P{i} → ∀ p1 p2 : Bool, next 175 w p1 p2 ∈ P{(i+1)%6} := by decide +kernel\n')
for i in range(6):
    L.append(f'theorem let_{i} : ∀ w, w ∈ P{i} → w.drop 164 = word{letters[i]} := by decide +kernel\n')
L.append('''
theorem seg_top (x : Row) (L : Nat) : (seg x L 175).drop 164 = seg x (L + 164) 11 := by
  have e : seg x L 175 = seg x L 164 ++ seg x (L + 164) 11 := seg_append x 164 11 L
  rw [e, List.drop_left' (seg_length x 164 L)]

/-- **The cycle.** Each phase goes to the next, whatever lies below. -/
theorem lock_cycle {z x : Row} {L : Nat} (hL : 2 ≤ L) (hs : step z = x) (hf : Held 175 L175 x L) :
    (seg x L 175 ∈ P0 → seg z (L + 3) 175 ∈ P1) ∧ (seg x L 175 ∈ P1 → seg z (L + 3) 175 ∈ P2) ∧
    (seg x L 175 ∈ P2 → seg z (L + 3) 175 ∈ P3) ∧ (seg x L 175 ∈ P3 → seg z (L + 3) 175 ∈ P4) ∧
    (seg x L 175 ∈ P4 → seg z (L + 3) 175 ∈ P5) ∧ (seg x L 175 ∈ P5 → seg z (L + 3) 175 ∈ P0) := by
  rw [next_seg closed hL hs hf]
  exact ⟨fun h => chk_0 _ h _ _, fun h => chk_1 _ h _ _, fun h => chk_2 _ h _ _, fun h => chk_3 _ h _ _,
    fun h => chk_4 _ h _ _, fun h => chk_5 _ h _ _⟩

''')
L.append('/-- **The letters.** -/\ntheorem lock_letters (x : Row) (L : Nat) :\n    ' + ' ∧\n    '.join(f'(seg x L 175 ∈ P{i} → seg x (L + 164) 11 = word{letters[i]})' for i in range(6)) + ' := by\n  rw [← seg_top]\n  exact ⟨let_0 _, let_1 _, let_2 _, let_3 _, let_4 _, let_5 _⟩\n\n')
n0=nat(ph[0][0])
L.append(f'''/-- **For ever.** -/
theorem lock_forever {{x : Row}} {{L : Nat}} (hL : 2 ≤ L) (h : Held 175 L175 x L) :
    ∀ n z, iter z n = x → Held 175 L175 z (L + 3 * n) := held_forever closed hL h

/-! ## An anchored row -/

/-- A window of phase 0 on the black edge, with one white cell below it, and rain above. -/
def row (j : Nat) : Bool :=
  if j = 0 then true else if j = 1 then false
  else if j < 177 then ({n0} : Nat).testBit (j - 2)
  else if (j - 177) % 2 = 0 then !({n0} : Nat).testBit 174 else ({n0} : Nat).testBit 174

theorem row_tail (j : Nat) (hj : 177 ≤ j) : row (j + 1) = !row j := by
  by_cases a : (j - 177) % 2 = 0
  · simp [row, show ¬j = 0 by omega, show ¬j = 1 by omega, show ¬j < 177 by omega, show ¬j + 1 < 177 by omega, a] <;> omega
  · simp [row, show ¬j = 0 by omega, show ¬j = 1 by omega, show ¬j < 177 by omega, show ¬j + 1 < 177 by omega, a] <;> omega

/-- An anchored row in the lock. -/
theorem witness : row 0 = true ∧ Held 175 L175 row 2 := by
  refine ⟨rfl, by decide +kernel, fun j hj => ?_⟩
  by_cases c : 177 ≤ j
  · exact row_tail j c
  · have : j = 176 := by omega
    subst this; decide +kernel

#print axioms closed
#print axioms lock_cycle
#print axioms lock_letters
#print axioms lock_forever
#print axioms witness
end TwoPairs.WallLockSix
''')
open('lean/TwoPairsWallLockSix.lean','w').write(''.join(L))
print(letters,[len(p) for p in ph])
