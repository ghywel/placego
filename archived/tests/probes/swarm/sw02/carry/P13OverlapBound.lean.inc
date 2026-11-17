theorem checked_factor_indices (x : Int → Bool) (hx : orbit x 13 = x) (origin : Int)
    (i : Nat) (hi : i = 6 ∨ i = 49 ∨ i = 53) :
    ¬ Matches x origin (factorWidth i) (factorValue i) := by
  rcases hi with rfl | rfl | rfl
  · change ¬ Matches x origin 7 16
    fail_if_success exact P13JoinedControl.factor_excluded x hx origin
    exact P13Factor0000100.factor_excluded x hx origin
  · change ¬ Matches x origin 12 2010
    exact P13Factor010110111110.factor_excluded x hx origin
  · change ¬ Matches x origin 7 6
    exact P13JoinedControl.factor_excluded x hx origin

theorem conditional_word_bound (m : Nat) :
    ∃ L : List (List Bool), L.length ≤ 170 ∧
      ∀ (x : Int → Bool),
        (∀ i < 141, ∀ o : Int, ¬ Matches x o (factorWidth i) (factorValue i)) →
        ∀ origin : Int, rowWord x origin m ∈ L := by
  refine ⟨allWords 16 retained m, ?_, ?_⟩
  · simpa only [Nat.mul_zero, Nat.add_zero] using allWords_length_le potential m
  · intro x hexclude origin
    exact rowWord_mem_allWords potential (fun o => window_coverage x o hexclude) m origin

end P13OverlapBound

#print axioms P13OverlapBound.checked_factor_indices
#print axioms P13OverlapBound.conditional_word_bound
