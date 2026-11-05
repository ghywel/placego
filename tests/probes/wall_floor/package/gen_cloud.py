#!/usr/bin/env python3
"""gen_cloud.py (Local, L1548): the kit module Rule30RightWallCloud: the 798 windows with their ranks, from the record's module, and the verified row that enters the third lock."""
import json,re,sys
src=open(sys.argv[1]+'/TwoPairsWallCloud.lean',encoding='utf-8').read()
tree=re.search(r'def tree : T := (.*)',src).group(1)
# entry row
d=json.load(open('../witness_break_175_56.json'))
y=d['y0_by_offset']; K=len(y)
row=[1]+[0]*8+y[::-1]
hi0=len(row)-1
N=850
b=row[-1]
while len(row)<N:
    b^=1; row.append(b)
E=sum(1<<i for i,c in enumerate(row) if c)
MASK=(1<<N)-1
def fw(v): return (v^((v<<1)|(v<<2)))&MASK
rows=[E]
for k in range(120): rows.append(fw(rows[-1]))
hi=lambda k: hi0-3*k
letters=[]
for k in range(111):
    c=(rows[k]>>(hi(k)-10))&2047
    assert c in (1596,1594),k
    letters.append(c==1594)
LB=sum(1<<k for k,v in enumerate(letters) if v)
assert hi0==569 and hi(110)==239 and hi(97)==278 and hi(6)==551 and hi(7)==548
m97=(rows[97]>>234)&((1<<45)-1)
m6=(rows[6]>>377)&((1<<175)-1)
top=(E>>(N-1))&1
par=1 if top==1 else 0     # bit N must be the complement of bit N-1
head='''module

public import Ruliology.CellularAutomata.Rule30RightWallLocks

/-!
# Rule 30: the cloud at the wall, and a row that enters a lock

Most rain-tailed codes do not lock at once. This module gives a closed set of 798 windows of 45 cells, the *cloud* (`closed`). A row
showing one shows one at every backward tick for ever (`cloud_forever`). No window of the cloud is a window of `LockAB`, so such a row
never reaches that lock (`cloud_not_lock`, `avoids_lock`), and along any backward history in the cloud the letters cannot change on 17
ticks running (`no_long_alternation`). No row in the cloud is periodic (`not_periodic`).

The cloud is coarse. `Entry.entry` is one explicit anchored row: its forward images are in the cloud through tick 97 and read letters through tick
110, the image at tick 7 is outside `LockThird`, and the image at tick 6 is inside it. So a backward orbit in the cloud can enter the third
lock. Nothing here concerns the center column.
-/

@[expose] public section

namespace Ruliology.CellularAutomata.Rule30RightWall

open WindowClosed

set_option autoImplicit false
set_option maxRecDepth 100000

namespace Cloud

/-- A search tree of numbers with ranks. -/
inductive Tree where
  | e
  | n (l : Tree) (v r : Nat) (t : Tree)

/-- The rank of a number, 0 if it is not there. -/
def Tree.find : Tree → Nat → Nat
  | .e, _ => 0
  | .n l v r t, c => if c < v then l.find c else if v < c then t.find c else r

/-- The numbers. -/
def Tree.toList : Tree → List Nat
  | .e => []
  | .n l v _ t => l.toList ++ v :: t.toList

theorem Tree.mem_of_find : ∀ (t : Tree) (c : Nat), t.find c ≠ 0 → c ∈ t.toList := by
  intro t
  induction t with
  | e => intro c h; exact absurd rfl h
  | n l v r t ihl iht =>
    intro c h
    simp only [Tree.find] at h
    simp only [Tree.toList, List.mem_append, List.mem_cons]
    by_cases c1 : c < v
    · rw [ite_eq_left c1] at h; exact Or.inl (ihl c h)
    · rw [ite_eq_right c1] at h
      by_cases c2 : v < c
      · rw [ite_eq_left c2] at h; exact Or.inr (Or.inr (iht c h))
      · exact Or.inr (Or.inl (by omega))

/-- The windows of the cloud as numbers, each with the longest alternating run that starts at it. -/
def tree : Tree := '''+tree+'''

/-- All the numbers. -/
def Qn : List Nat := tree.toList

/-- The cloud. -/
def Q45 : List (List Bool) := Qn.map (dec 45)

/-- The longest alternating run from a window; 0 outside the cloud. -/
def rk (n : Nat) : Nat := tree.find n

/-- What each number must satisfy. -/
def Good (n : Nat) : Prop :=
  1 ≤ rk n ∧ rk n ≤ 17 ∧ (n >>> 34 = 1596 ∨ n >>> 34 = 1594) ∧ dec 45 n ∉ LockAB.Win ∧ n >>> 44 = 1 ∧
  ∀ p1 p2 : Bool, image 45 n p1 p2 >>> 49 = 5 ∧ rk (nxt 45 n p1 p2) ≠ 0 ∧
    (nxt 45 n p1 p2 >>> 34 ≠ n >>> 34 → rk (nxt 45 n p1 p2) + 1 ≤ rk n)

instance : DecidablePred Good := fun n => by unfold Good; infer_instance

theorem good : ∀ n, n ∈ Qn → Good n := by decide +kernel

theorem mem_of_rk {n : Nat} (h : rk n ≠ 0) : n ∈ Qn := Tree.mem_of_find tree n h

/-- **The cloud is closed.** -/
theorem closed : Closed 45 Q45 :=
  closed_fast (by decide) Qn (fun n hn => by
    obtain ⟨_, _, _, _, h5, h6⟩ := good n hn
    exact ⟨h5, fun p1 p2 => ⟨(h6 p1 p2).1, mem_of_rk (h6 p1 p2).2.1⟩⟩)

/-- **For ever.** -/
theorem cloud_forever {x : Row} {L : Nat} (hL : 2 ≤ L) (h : Held 45 Q45 x L) :
    ∀ n z, iter z n = x → Held 45 Q45 z (L + 3 * n) := held_forever closed hL h

/-- **Cloud and lock are apart.** -/
theorem cloud_not_lock : ∀ w, w ∈ Q45 → w ∉ LockAB.Win := by
  intro w hw; obtain ⟨n, hn, rfl⟩ := List.mem_map.1 hw; exact (good n hn).2.2.2.1

/-- **A row in the cloud never reaches the alternating lock.** -/
theorem avoids_lock {x : Row} {L : Nat} (hL : 2 ≤ L) (h : Held 45 Q45 x L) :
    ∀ n z, iter z n = x → seg z (L + 3 * n) 45 ∉ LockAB.Win :=
  fun n z hz => cloud_not_lock _ (cloud_forever hL h n z hz).1

/-- **A row in the cloud is not periodic.** -/
theorem not_periodic {x : Row} {L P : Nat} (hL : 2 ≤ L) (h : Held 45 Q45 x L) (hP : 0 < P) : iter x P ≠ x := by
  refine held_not_periodic closed (by decide) (fun w hw => ?_) hL h hP
  obtain ⟨n, hn, rfl⟩ := List.mem_map.1 hw
  exact wall_of_letter (by decide) (good n hn).2.2.1

/-- **Alternation is bounded.** Along any backward history in the cloud, the 11 cells at the wall cannot change on 17 ticks running. -/
theorem no_long_alternation {L : Nat} (hL : 2 ≤ L) (z : Nat → Row) (hz : ∀ i, step (z (i + 1)) = z i)
    (h : Held 45 Q45 (z 0) L) :
    ¬ ∀ i, i < 17 → seg (z (i + 1)) (L + 3 * (i + 1) + 34) 11 ≠ seg (z i) (L + 3 * i + 34) 11 := by
  intro hc
  have held : ∀ i, Held 45 Q45 (z i) (L + 3 * i) := by
    intro i
    induction i with
    | zero => exact h
    | succ i ih =>
      have := held_back closed (L := L + 3 * i) (by omega) (hz i) ih
      rwa [show L + 3 * i + 3 = L + 3 * (i + 1) by omega] at this
  have top : ∀ (x : Row) (K n : Nat), seg x K 45 = dec 45 n → seg x (K + 34) 11 = dec 11 (n >>> 34) := by
    intro x K n e
    have d := seg_drop x K 45 34 (by decide)
    rw [e, dec_drop 45 34 n (by decide)] at d
    exact d.symm
  have down : ∀ i, i ≤ 17 → ∃ n, n ∈ Qn ∧ seg (z i) (L + 3 * i) 45 = dec 45 n ∧ rk n + i ≤ 17 := by
    intro i
    induction i with
    | zero =>
      intro _
      obtain ⟨n, hn, e⟩ := List.mem_map.1 (held 0).1
      exact ⟨n, hn, e.symm, (good n hn).2.1⟩
    | succ i ih =>
      intro hi
      obtain ⟨n, hn, e, hr⟩ := ih (by omega)
      have g := good n hn
      have hnext := next_seg closed (L := L + 3 * i) (by omega) (hz i) (held i)
      rw [e, next_fast (by decide) g.2.2.2.2.1] at hnext
      have e3 : L + 3 * i + 3 = L + 3 * (i + 1) := by omega
      rw [e3] at hnext
      obtain ⟨_, hne, hdec⟩ := g.2.2.2.2.2 (z (i + 1) (L + 3 * i - 1)) (z (i + 1) (L + 3 * i - 2))
      refine ⟨_, mem_of_rk hne, hnext, ?_⟩
      have ch := hc i (by omega)
      have hlet : nxt 45 n (z (i + 1) (L + 3 * i - 1)) (z (i + 1) (L + 3 * i - 2)) >>> 34 ≠ n >>> 34 := by
        intro q
        apply ch
        rw [top _ _ _ hnext, top _ _ _ e, q]
      have := hdec hlet
      omega
  obtain ⟨n, hn, _, hr⟩ := down 17 (Nat.le_refl _)
  have := (good n hn).1
  omega

end Cloud

/-! ## A row that enters the third lock -/

namespace Entry
open Cloud

/-- The row's cells below 850. -/
def E : Nat := '''+hex(E)+'''

/-- The letters at ticks 0 to 110, a set bit for `B`. -/
def LB : Nat := '''+hex(LB)+'''

/-- The row: anchored at bit 0, rain above bit 569. -/
def row (j : Nat) : Bool := if j < 850 then E.testBit j else decide ((j - 850) % 2 = '''+str(par)+''')

theorem row_low : ∀ j, j < 850 → row j = E.testBit j := by
  intro j hj; simp [row, hj]

theorem chk_E : ∀ j, j < 280 → E.testBit (569 + j + 1) = !E.testBit (569 + j) := by decide +kernel

theorem chk_top : E.testBit 849 = '''+('true' if top else 'false')+''' := by decide +kernel

theorem row_tail : ∀ j, 569 ≤ j → row (j + 1) = !row j := by
  intro j hj
  by_cases c : j + 1 < 850
  · rw [row_low _ c, row_low j (by omega)]
    have := chk_E (j - 569) (by omega)
    rwa [show 569 + (j - 569) = j by omega] at this
  · by_cases d : j = 849
    · subst d
      rw [row_low 849 (by omega), chk_top]; decide
    · have q : 850 ≤ j := by omega
      simp only [row, show ¬j < 850 by omega, show ¬j + 1 < 850 by omega, ite_false]
      by_cases a : (j - 850) % 2 = '''+str(par)+'''
      · simp [a]; omega
      · simp [a]; omega

theorem iter_row (k j : Nat) (hj : j < 850) : iter row k j = (fwN k E).testBit j := by
  rw [iter_low row_low k j hj, iter_fw]

theorem seg_row (k L n : Nat) (h : L + n ≤ 850) : seg (iter row k) L n = seg (fwN k E).testBit L n :=
  seg_ext n L L (fun i hi => iter_row k (L + i) (by omega))

theorem chk_t : ∀ j, j < 550 → (fwN 110 E).testBit (239 + j + 1) = !(fwN 110 E).testBit (239 + j) := by decide +kernel

theorem tail110 : ∀ j, 239 ≤ j → iter row 110 (j + 1) = !iter row 110 j := by
  intro j hj
  by_cases c : j < 789
  · rw [iter_row _ _ (by omega), iter_row _ _ (by omega)]
    have := chk_t (j - 239) (by omega)
    rwa [show 239 + (j - 239) = j by omega] at this
  · exact iter_tail row_tail 110 j (by omega)

theorem chk_letters : ∀ k, k < 111 → seg (fwN k E).testBit (229 + 3 * (110 - k)) 11 = if LB.testBit k then wordB else wordA := by
  decide +kernel

/-- **The letters at ticks 0 to 110.** -/
theorem letters : ∀ k, k ≤ 110 → seg (iter row k) (229 + 3 * (110 - k)) 11 = if LB.testBit k then wordB else wordA := by
  intro k hk
  rw [seg_row _ _ _ (by omega)]
  exact chk_letters k (by omega)

theorem held110 : Held 11 letterSet (iter row 110) 229 := by
  refine ⟨?_, tail110⟩
  have := letters 110 (Nat.le_refl _)
  simp only [Nat.sub_self, Nat.mul_zero, Nat.add_zero] at this
  rw [this]
  cases LB.testBit 110 <;> simp [letterSet]

/-- Tick `k` is held by the letters. -/
theorem held_k (k : Nat) (hk : k ≤ 110) : Held 11 letterSet (iter row k) (229 + 3 * (110 - k)) := by
  have e : iter (iter row k) (110 - k) = iter row 110 := by
    rw [← iter_add, show k + (110 - k) = 110 by omega]
  exact held_forever letters_closed (by omega) held110 (110 - k) _ e

theorem chk_97 : rk '''+str(m97)+''' ≠ 0 ∧ seg (fwN 97 E).testBit 234 45 = dec 45 '''+str(m97)+''' := by decide +kernel

theorem chk_6 : '''+str(m6)+''' ∈ LockThird.All ∧ seg (fwN 6 E).testBit 377 175 = dec 175 '''+str(m6)+''' := by decide +kernel

theorem chk_7 : seg (fwN 7 E).testBit 374 175 ∉ LockThird.Win := by decide +kernel

/-- **A row in the cloud enters the third lock.** The row is anchored. Its image at tick 97 is in the cloud, its image at tick 7 is outside
the third lock, its image at tick 6 is inside it, and all its images through tick 110 read letters. -/
theorem entry :
    row 0 = true ∧ Held 45 Q45 (iter row 97) 234 ∧ seg (iter row 7) 374 175 ∉ LockThird.Win ∧
      Held 175 LockThird.Win (iter row 6) 377 ∧
      ∀ k, k ≤ 110 → seg (iter row k) (229 + 3 * (110 - k)) 11 = if LB.testBit k then wordB else wordA := by
  refine ⟨by decide +kernel, ⟨?_, ?_⟩, ?_, ⟨?_, ?_⟩, letters⟩
  · rw [seg_row _ _ _ (by omega), chk_97.2]
    exact List.mem_map.2 ⟨_, mem_of_rk chk_97.1, rfl⟩
  · intro j hj
    exact (held_k 97 (by omega)).2 j (by omega)
  · rw [seg_row _ _ _ (by omega)]
    exact chk_7
  · rw [seg_row _ _ _ (by omega), chk_6.2]
    exact List.mem_map.2 ⟨_, chk_6.1, rfl⟩
  · intro j hj
    exact (held_k 6 (by omega)).2 j (by omega)

end Entry

end Ruliology.CellularAutomata.Rule30RightWall
'''
open('Rule30RightWallCloud.lean','w',encoding='utf-8').write(head)
print(len(head),'N',N,'hi0',hi0,'top',top,'par',par,'letters',''.join('B' if v else 'A' for v in letters))
