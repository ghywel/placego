/-! ### Rooted profile chains return (Local's section for the joint module, L1089)

PROOFS.md entry 39. `child_source_eq`, `child_source_unique`: the source is recovered on any carrier. `child_unique`,
`child_exists`: a `q`-periodic driver black somewhere has exactly one `q`-periodic child (the reset).
`rooted_chain_returns`: a chain of `q`-periodic profiles starting from a white word, each consecutive triple a
`Child`, reaches a white word again. States are coded by their first `q` cells of each word
(`Rule30Jen.pigeonhole` on lists of length `2q`), so no infinite function space is counted. No physical-root
ancestry and no bound on the return depth. -/

/-- **Source recovery**: `A` is determined by `B` and `C`. -/
theorem child_source_eq {ι : Type} {succ : ι → ι} {A B C : ι → Bool} (h : Child succ A B C) (t : ι) :
    A t = xor (C (succ t)) (B t || C t) := by
  rw [h t]; cases A t <;> cases (B t || C t) <;> rfl

theorem child_source_unique {ι : Type} {succ : ι → ι} {A A' B C : ι → Bool}
    (h : Child succ A B C) (h' : Child succ A' B C) : A = A' := by
  funext t; rw [child_source_eq h t, child_source_eq h' t]

theorem periodic_mul {q : Nat} {f : Nat → Bool} (h : Periodic q f) : ∀ m t, f (q * m + t) = f t := by
  intro m
  induction m with
  | zero => intro t; simp
  | succ m ih => intro t; rw [show q * (m + 1) + t = q + (q * m + t) by rw [Nat.mul_succ]; omega, h, ih]

theorem periodic_mod {q : Nat} {f : Nat → Bool} (h : Periodic q f) (t : Nat) : f t = f (t % q) := by
  have := periodic_mul h (t / q) (t % q)
  rw [Nat.div_add_mod] at this
  exact this

theorem periodic_ext {q : Nat} {f g : Nat → Bool} (hf : Periodic q f) (hg : Periodic q g) (hq : 0 < q)
    (h : ∀ t, t < q → f t = g t) : f = g := by
  funext t; rw [periodic_mod hf t, periodic_mod hg t]; exact h _ (Nat.mod_lt _ hq)

/-- **Reset uniqueness**: a driver black at `t0` has at most one `q`-periodic child. -/
theorem child_unique {q : Nat} (hq : 0 < q) {A B C C' : Nat → Bool} (hC : Periodic q C)
    (hC' : Periodic q C') (h : Child (· + 1) A B C) (h' : Child (· + 1) A B C') {t0 : Nat}
    (hb : B t0 = true) : C = C' := by
  have hagree : ∀ k, C (t0 + 1 + k) = C' (t0 + 1 + k) := by
    intro k
    induction k with
    | zero =>
      have e := h t0
      have e' := h' t0
      simp only [hb, Bool.true_or] at e e'
      simpa using e.trans e'.symm
    | succ k ih =>
      have e := h (t0 + 1 + k)
      have e' := h' (t0 + 1 + k)
      rw [show t0 + 1 + (k + 1) = t0 + 1 + k + 1 by omega, e, e', ih]
  funext t
  have hle : t0 + 1 ≤ q * (t0 + 1) := Nat.le_mul_of_pos_left _ hq
  rw [← periodic_mul hC (t0 + 1) t, ← periodic_mul hC' (t0 + 1) t]
  have := hagree (q * (t0 + 1) + t - (t0 + 1))
  rwa [show t0 + 1 + (q * (t0 + 1) + t - (t0 + 1)) = q * (t0 + 1) + t by omega] at this

/-- The forward run after a reset at `t0`: `run A B t0 k` is the child's value at `t0 + 1 + k`. -/
def run (A B : Nat → Bool) (t0 : Nat) : Nat → Bool
  | 0 => !A t0
  | k + 1 => xor (A (t0 + 1 + k)) (B (t0 + 1 + k) || run A B t0 k)

theorem run_periodic {q : Nat} (hq : 0 < q) {A B : Nat → Bool} (hA : Periodic q A) (hB : Periodic q B)
    {t0 : Nat} (hb : B t0 = true) : ∀ k, run A B t0 (k + q) = run A B t0 k := by
  intro k
  induction k with
  | zero =>
    obtain ⟨p, rfl⟩ : ∃ p, q = p + 1 := ⟨q - 1, by omega⟩
    rw [Nat.zero_add]
    show xor (A (t0 + 1 + p)) (B (t0 + 1 + p) || run A B t0 p) = !A t0
    have e1 : A (t0 + 1 + p) = A t0 := by rw [show t0 + 1 + p = (p + 1) + t0 by omega]; exact hA t0
    have e2 : B (t0 + 1 + p) = B t0 := by rw [show t0 + 1 + p = (p + 1) + t0 by omega]; exact hB t0
    rw [e1, e2, hb]; cases A t0 <;> rfl
  | succ k ih =>
    rw [show k + 1 + q = (k + q) + 1 by omega]
    show xor (A (t0 + 1 + (k + q))) (B (t0 + 1 + (k + q)) || run A B t0 (k + q)) =
      xor (A (t0 + 1 + k)) (B (t0 + 1 + k) || run A B t0 k)
    rw [ih, show t0 + 1 + (k + q) = q + (t0 + 1 + k) by omega, hA, hB]

/-- The child built from the reset at `t0`. -/
def childOf (A B : Nat → Bool) (q t0 : Nat) (t : Nat) : Bool := run A B t0 (q * (t0 + 1) + t - (t0 + 1))

/-- **Reset existence**: a driver black at `t0` has a `q`-periodic child. -/
theorem child_exists {q : Nat} (hq : 0 < q) {A B : Nat → Bool} (hA : Periodic q A) (hB : Periodic q B)
    {t0 : Nat} (hb : B t0 = true) :
    Periodic q (childOf A B q t0) ∧ Child (· + 1) A B (childOf A B q t0) := by
  have hle : t0 + 1 ≤ q * (t0 + 1) := Nat.le_mul_of_pos_left _ hq
  refine ⟨fun t => ?_, fun t => ?_⟩
  · unfold childOf
    rw [show q * (t0 + 1) + (q + t) - (t0 + 1) = (q * (t0 + 1) + t - (t0 + 1)) + q by omega]
    exact run_periodic hq hA hB hb _
  · unfold childOf
    rw [show q * (t0 + 1) + (t + 1) - (t0 + 1) = (q * (t0 + 1) + t - (t0 + 1)) + 1 by omega]
    show xor (A (t0 + 1 + (q * (t0 + 1) + t - (t0 + 1))))
        (B (t0 + 1 + (q * (t0 + 1) + t - (t0 + 1))) || run A B t0 (q * (t0 + 1) + t - (t0 + 1))) =
      xor (A t) (B t || run A B t0 (q * (t0 + 1) + t - (t0 + 1)))
    rw [show t0 + 1 + (q * (t0 + 1) + t - (t0 + 1)) = q * (t0 + 1) + t by omega,
      periodic_mul hA, periodic_mul hB]

/-- Equal codes give equal states. -/
theorem state_eq {q : Nat} (hq : 0 < q) (w : Nat → Nat → Bool) (hper : ∀ k, Periodic q (w k)) {m n : Nat}
    (h : (List.range q).map (w m) ++ (List.range q).map (w (m + 1)) =
      (List.range q).map (w n) ++ (List.range q).map (w (n + 1))) :
    w m = w n ∧ w (m + 1) = w (n + 1) := by
  obtain ⟨h1, h2⟩ := List.append_inj h (by simp)
  refine ⟨periodic_ext (hper m) (hper n) hq fun t ht => ?_, periodic_ext (hper _) (hper _) hq fun t ht => ?_⟩
  · exact (List.map_inj_left.1 h1) t (List.mem_range.2 ht)
  · exact (List.map_inj_left.1 h2) t (List.mem_range.2 ht)

/-- **Rooted chains return**: a chain of `q`-periodic profiles starting from a white word, each triple a
child triple, reaches a white word again. -/
theorem rooted_chain_returns {q : Nat} (hq : 0 < q) (w : Nat → Nat → Bool) (hper : ∀ k, Periodic q (w k))
    (h0 : ∀ t, w 0 t = false) (hchild : ∀ k, Child (· + 1) (w k) (w (k + 1)) (w (k + 2))) :
    ∃ k, 1 ≤ k ∧ ∀ t, w k t = false := by
  have ha : ∀ m, ((List.range q).map (w m) ++ (List.range q).map (w (m + 1))).length = q + q := by
    intro m; simp
  obtain ⟨i, j, hij, -, hijeq⟩ := Ruliology.CellularAutomata.Rule30Jen.pigeonhole (q + q)
    (fun m => (List.range q).map (w m) ++ (List.range q).map (w (m + 1))) ha
  have descend : ∀ d, d ≤ i → w (i - d) = w (j - d) ∧ w (i - d + 1) = w (j - d + 1) := by
    intro d
    induction d with
    | zero => intro _; simpa using state_eq hq w hper hijeq
    | succ d ih =>
      intro hd
      obtain ⟨e1, e2⟩ := ih (by omega)
      have hc1 := hchild (i - (d + 1))
      have hc2 := hchild (j - (d + 1))
      rw [show i - (d + 1) + 1 = i - d by omega, show i - (d + 1) + 2 = i - d + 1 by omega, e1, e2] at hc1
      rw [show j - (d + 1) + 1 = j - d by omega, show j - (d + 1) + 2 = j - d + 1 by omega] at hc2
      refine ⟨child_source_unique hc1 hc2, ?_⟩
      rw [show i - (d + 1) + 1 = i - d by omega, show j - (d + 1) + 1 = j - d by omega]
      exact e1
  obtain ⟨e, -⟩ := descend i (Nat.le_refl i)
  rw [Nat.sub_self] at e
  exact ⟨j - i, by omega, fun t => by rw [← e]; exact h0 t⟩

