import TwoPairsSixCertificate

/-! Physical soundness of the finite six-window certificate. All predecessor
boundary inputs at different ticks come from the same earliest row. -/
namespace TwoPairs.Six
open WindowTransport

theorem decode_physical (z : Row) (A R n : Nat) :
    ∀ r, r ≤ R → decode (seg z A (2*R)) r (seg (iter z r) (A+2*R) n) = seg z (A+2*R) n := by
  intro r
  induction r with
  | zero => intro _; rfl
  | succ r ih =>
    intro hr
    let M := 2*R-2*r
    have hm : 2 ≤ M := by dsimp [M]; omega
    have c : shrinkN (seg z A (2*R)) r = seg (iter z r) (A+2*r) M := by
      have hh := shrinkN_seg z A r M
      rwa [show 2*r+M=2*R by dsimp [M]; omega] at hh
    rw [decode,c,seg_length,seg_getD _ _ _ _ (by omega),seg_getD _ _ _ _ (by omega)]
    rw [show A+2*r+(M-1)=A+2*R-1 by dsimp [M]; omega,
      show A+2*r+(M-2)=A+2*R-2 by dsimp [M]; omega]
    rw [← back_seg (z:=iter z r) (x:=iter z (r+1)) rfl n (A+2*R) (by omega)]
    exact ih (by omega)

private theorem target_seg (x : Row) (L r : Nat)
    (h : ∀ j, L+10 ≤ j → x (j+1) = !x j) :
    target (seg x L 11) r = seg x L (14+3*r) := by
  have pre : (seg x L 11).take 10 = seg x L 10 := by
    rw [show 11=10+1 by decide,seg_append x 10 1 L,List.take_left' (seg_length x 10 L)]
  rw [target,pre,seg_getD _ _ _ _ (by omega),←seg_alt h (3*r+4) (L+10) (by omega),
    ←seg_append,show 10+(3*r+4)=14+3*r by omega]

private theorem at_window (z : Row) (L r : Nat) (hL : 2*r ≤ L)
    (h : ∀ j, L+10 ≤ j → iter z r (j+1) = !iter z r j) :
    output (seg (iter z r) L 11) (seg z (L-2*r) (2*r)) r = seg z L (14+3*r) := by
  unfold output
  rw [target_seg _ _ _ h]
  have e := decode_physical z (L-2*r) r (14+3*r) r (by omega)
  rwa [show L-2*r+2*r=L by omega] at e

theorem rain_back_many (z : Row) (D : Nat) (hd : 2≤D) : ∀ r,
    (∀ j, D≤j → iter z r (j+1) = !iter z r j) →
    ∀ j, D+3*r≤j → z (j+1) = !z j := by
  intro r
  induction r generalizing D with
  | zero => intro h; exact h
  | succ r ih =>
    intro h j hj
    have h' := back_rain_tail (z:=iter z r) (x:=iter z (r+1)) hd rfl h
    exact ih (D+3) (by omega) h' j (by omega)

private theorem from_arrival (z : Row) (L r : Nat) (hL : 2*r ≤ L)
    (rain : ∀ j, L+10≤j → iter z r (j+1) = !iter z r j)
    (arr : Arrived (seg (iter z r) L 11) (seg z (L-2*r) (2*r)) r) :
    Front z (L+3*r) := by
  refine ⟨?_, fun j hj => rain_back_many z (L+10) (by omega) r rain j (by omega)⟩
  unfold Arrived at arr
  rw [at_window z L r hL rain, show 14+3*r=3*r+14 by omega,
    seg_append z (3*r) 14 L,List.drop_left' (seg_length z (3*r) L),
    show 14=11+3 by decide,seg_append z 11 3 (L+3*r),List.take_left' (seg_length z 11 _)] at arr
  exact arr

private theorem actual_context (z : Row) (A n : Nat) : seg z A n ∈ contexts n := by
  have e := mem_contexts (seg z A n)
  rwa [seg_length] at e

theorem fast_physical (z : Row) (L : Nat) (hL : 4≤L)
    (screen : seg (iter z 2) L 11 ∈ fast)
    (rain : ∀ j, L+10 ≤ j → iter z 2 (j+1) = !iter z 2 j) : Front z (L+6) :=
  from_arrival z L 2 hL rain (fast_two _ screen _ (actual_context _ _ _))

theorem slow_physical (z : Row) (L : Nat) (hL : 6≤L)
    (screen : seg (iter z 3) L 11 ∈ slow)
    (rain : ∀ j, L+10 ≤ j → iter z 3 (j+1) = !iter z 3 j) : Front z (L+9) :=
  from_arrival z L 3 hL rain (slow_three _ screen _ (actual_context _ _ _))

#print axioms fast_physical
#print axioms slow_physical
end TwoPairs.Six
