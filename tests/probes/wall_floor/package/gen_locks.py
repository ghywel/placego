#!/usr/bin/env python3
"""gen_locks.py (Local, L1548): the kit module Rule30RightWallLocks: the three locks as numbers, from lock45.txt, the record's 136-cell module and lock175.json."""
import json,re,sys
def nat(s): return sum(1<<i for i,c in enumerate(s) if c=='#')
w45=[l.strip() for l in open('../lock45.txt') if l.strip()]
A=[w for w in w45 if w.endswith('..####...##')]; B=[w for w in w45 if w.endswith('.#.###...##')]
ph45=[[nat(w) for w in A],[nat(w) for w in B]]
aab=open(sys.argv[1]+'/TwoPairsWallLockAAB.lean',encoding='utf-8').read()
ph136=[[int(x) for x in re.findall(r'dec 136 (\d+)',re.search(rf'def P{i} : .*',aab).group(0))] for i in range(3)]
d=json.load(open('../lock175.json'))
ph175=[[nat(w) for w in d[str(i)]] for i in range(6)]
def lst(ph): return '[' + ',\n  '.join('['+', '.join(str(n) for n in p)+']' for p in ph) + ']'
head='''module

public import Ruliology.CellularAutomata.Rule30RightWall

/-!
# Rule 30: three locks at the wall of a rain-tailed edge code

A *lock* is a set of windows at the wall, in phases, closed under the backward tick for every pair of lower cells. A code showing one
of its windows shows them at every backward tick for ever, whatever lies below, and its letters follow the phases (`Lock.letters`).

* `LockAB`: four windows of 45 cells, letters `A`, `B` for ever. Each window starts with a reset word.
* `LockAAB`: six windows of 136 cells, letters `A`, `A`, `B`. Each window starts with a reset word.
* `LockThird`: forty windows of 175 cells in six phases, letters `B`, `A`, `A`, `B`, `A`, `A`. Apart from the wall's own word, no reset
  word stands at one depth in all forty windows (`no_floor`).

Each lock has a witness on an anchored row, and no code in a lock is periodic under the edge map. Nothing here concerns the center column.
-/

@[expose] public section

namespace Ruliology.CellularAutomata.Rule30RightWall

open WindowClosed

set_option autoImplicit false
set_option maxRecDepth 100000
'''
def lock(name,W,k,ph,lc_def,lc_stmt,doc,proof_extra=''):
    n0=ph[0][0]
    return f'''
/-! ## {doc} -/

namespace {name}

/-- The phases, as window numbers, low cell first. -/
def Ph : List (List Nat) := {lst(ph)}

/-- All the windows, as numbers. -/
def All : List Nat := Ph.flatten

/-- All the windows. -/
def Win : List (List Bool) := All.map (dec {W})

/-- The letter of each phase. -/
def lc (r : Nat) : List Bool := {lc_def}

/-- **The lock.** -/
theorem lock : Lock {W} {k} Ph All :=
  ⟨by decide, by decide, by decide +kernel, by decide +kernel, by decide +kernel⟩

theorem closed : Closed {W} Win := lock.closed

/-- **For ever.** Every row `n` ticks before a held row is held `3 n` cells higher, whatever lies below the window. -/
theorem held {{x : Row}} {{L : Nat}} (hL : 2 ≤ L) (h : Held {W} Win x L) :
    ∀ n z, iter z n = x → Held {W} Win z (L + 3 * n) := held_forever closed hL h

theorem chk_letters : ∀ r, r < {k} → ∀ n, n ∈ Ph.getD r [] → dec 11 (n >>> {W-11}) = lc r := by decide +kernel

/-- **The letters.** There is a phase `r` such that the wall of every row `n` ticks before the row reads the letter of phase `r + n`. -/
theorem letters {{x : Row}} {{L : Nat}} (hL : 2 ≤ L) (h : Held {W} Win x L) :
    ∃ r, r < {k} ∧ ∀ n z, iter z n = x → seg z (L + 3 * n + {W-11}) 11 = {lc_stmt} := by
  obtain ⟨r, hr, f⟩ := lock.letters lc chk_letters hL h
  exact ⟨r, hr, fun n z hz => by simpa [lc] using f n z hz⟩

theorem chk_wall : ∀ n, n ∈ All → n >>> {W-11} = 1596 ∨ n >>> {W-11} = 1594 := by decide +kernel

/-- **A row in the lock is not periodic.** -/
theorem not_periodic {{x : Row}} {{L P : Nat}} (hL : 2 ≤ L) (h : Held {W} Win x L) (hP : 0 < P) : iter x P ≠ x := by
  refine held_not_periodic closed (by decide) (fun w hw => ?_) hL h hP
  obtain ⟨n, hn, rfl⟩ := List.mem_map.1 hw
  exact wall_of_letter (by decide) (chk_wall n hn)

/-- **An anchored row in the lock.** -/
theorem witness : anchor {W} {n0} 0 = true ∧ Held {W} Win (anchor {W} {n0}) 2 :=
  anchor_held (by decide) (by decide +kernel) (by decide +kernel)
{proof_extra}
end {name}
'''
out=head
floor=lambda W:f'''
/-- **The shield of the lock.** Each window starts with a reset word. -/
theorem floor : ∀ n, n ∈ All → ∃ b u v, (dec {W} n).take 10 = Reset.F b u v := by decide +kernel
'''
out+=lock('LockAB',45,2,ph45,'if r = 1 then wordB else wordA','if (r + n) % 2 = 1 then wordB else wordA','The letters `A`, `B`: four windows of 45 cells',floor(45))
out+=lock('LockAAB',136,3,ph136,'if r = 2 then wordB else wordA','if (r + n) % 3 = 2 then wordB else wordA','The letters `A`, `A`, `B`: six windows of 136 cells',floor(136))
third='''
/-- **No fixed shield.** Below the wall's own word, no depth carries a reset word in all forty windows. -/
theorem no_floor : ∀ d, d < 164 → ¬ ∀ n, n ∈ All → ∃ b u v, ((dec 175 n).drop d).take 10 = Reset.F b u v := by decide +kernel
'''
out+=lock('LockThird',175,6,ph175,'if r % 3 = 0 then wordB else wordA','if (r + n) % 6 % 3 = 0 then wordB else wordA','A third lock, with no fixed shield: forty windows of 175 cells',third)
out+='\nend Ruliology.CellularAutomata.Rule30RightWall\n'
open('Rule30RightWallLocks.lean','w',encoding='utf-8').write(out)
print(len(out))
