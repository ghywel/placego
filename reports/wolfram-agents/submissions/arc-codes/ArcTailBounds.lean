import ArcBreakSequence

/-!
# Finite changes and tail shifts of a repeat-window obstruction

Core-Lean integration of the existing G131/G132 eventual-code argument, not a new novelty claim.
If c and d agree from N onwards, RepeatBound c q C implies RepeatBound d q (C+2*N).
This transfers the obstruction directly, without restarting the physical Rule30 configuration.
The endpoint interpretation still needs an irrational orbit's single-visit property; no such geometry
is inferred merely from these abstract predicates. No efficient last-exception search is asserted.
-/

namespace ArcTailBounds

open ArcBreakSequence

/-- Shifting the time origin by N costs only N in the repeat constant. -/
theorem shift_repeat_bound (c : Nat → Bool) (q C N : Nat) (hr : RepeatBound c q C) :
    RepeatBound (fun n => c (n+N)) q (C+N) := by
  intro a b hab hm
  have h := hr (a+N) (b+N) (by omega) (by
    intro s hs ht
    have hNs : N ≤ s := by omega
    obtain ⟨k,rfl⟩ := Nat.exists_eq_add_of_le hNs
    have he := hm k (by omega) (by omega)
    simpa [Nat.add_assoc,Nat.add_comm,Nat.add_left_comm] using he)
  omega

/-- Finite prefix changes cost at most 2*N; the conclusion concerns the unshifted new trace. -/
theorem eventual_transfer (c d : Nat → Bool) (q C N : Nat) (hr : RepeatBound c q C)
    (he : ∀ s, N ≤ s → c s = d s) : RepeatBound d q (C+2*N) := by
  intro a b hab hm
  by_cases hb : b < N
  · omega
  have hmax : max a N ≤ b := Nat.max_le_of_le_of_le hab (by omega)
  have h := hr (max a N) b hmax (by
    intro s hs ht
    have hNs : N ≤ s := Nat.le_trans (Nat.le_max_right a N) hs
    rw [he (s+q) (by omega), he s hNs]
    exact hm s (Nat.le_trans (Nat.le_max_left a N) hs) ht)
  have hmarg : max a N ≤ a+N := Nat.max_le_of_le_of_le (by omega) (by omega)
  omega

/-- A single new constant works for every positive lag after finite changes. -/
theorem uniform_eventual_transfer (c d : Nat → Bool) (C N : Nat)
    (hr : ∀ q, 0 < q → RepeatBound c q C) (he : ∀ s, N ≤ s → c s = d s) :
    ∀ q, 0 < q → RepeatBound d q (C+2*N) := by
  intro q hq
  exact eventual_transfer c d q C N (hr q hq) he

/-- Finitely many labels, each used at most once in time, have a last-use cutoff.
    This is classical finite existence, not a bound in terms of the label count. -/
theorem finite_single_hits_cutoff (r : Nat) (P : Nat → Nat → Prop)
    (hone : ∀ i, i < r → ∀ s t, P i s → P i t → s = t) :
    ∃ N, ∀ i, i < r → ∀ n, N ≤ n → ¬ P i n := by
  classical
  induction r with
  | zero =>
    refine ⟨0,?_⟩
    intro i hi
    omega
  | succ r ih =>
    obtain ⟨N,hN⟩ := ih (fun i hi s t hs ht => hone i (by omega) s t hs ht)
    by_cases hp : ∃ k, P r k
    · obtain ⟨k,hk⟩ := hp
      refine ⟨max N (k+1),?_⟩
      intro i hi n hn hpin
      by_cases hir : i < r
      · exact hN i hir n (by omega) hpin
      · have hir : i = r := by omega
        subst i
        have he := hone r (by omega) n k hpin hk
        omega
    · refine ⟨N,?_⟩
      intro i hi n hn hpin
      by_cases hir : i < r
      · exact hN i hir n hn hpin
      · have hir : i = r := by omega
        subst i
        exact hp ⟨n,hpin⟩

/-- Changes supported on finitely many single-visit labels eventually disappear. -/
theorem finite_single_hits_eventual (c d : Nat → Bool) (r : Nat) (P : Nat → Nat → Prop)
    (hone : ∀ i, i < r → ∀ s t, P i s → P i t → s = t)
    (hbad : ∀ n, c n ≠ d n → ∃ i, i < r ∧ P i n) :
    ∃ N, ∀ n, N ≤ n → c n = d n := by
  obtain ⟨N,hN⟩ := finite_single_hits_cutoff r P hone
  refine ⟨N,?_⟩
  intro n hn
  by_cases he : c n = d n
  · exact he
  · obtain ⟨i,hi,hpin⟩ := hbad n he
    exact False.elim (hN i hi n hn hpin)

#print axioms ArcTailBounds.shift_repeat_bound
#print axioms ArcTailBounds.eventual_transfer
#print axioms ArcTailBounds.uniform_eventual_transfer
#print axioms ArcTailBounds.finite_single_hits_cutoff
#print axioms ArcTailBounds.finite_single_hits_eventual

end ArcTailBounds
