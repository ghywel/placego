import Mathlib

/-!
# Theorem A⁗ (PROOFS.md entry 13): a repeat's white run cannot lie in the settled band (Local, 2026-10-10)

In the setting of Theorem A‴ (equal blocks of n on columns i and i + 1 at times a and a′, leftmost black cell L
cells left of column i), if the rows at times a′ - P and a′ agree on the diagonals up to M (Lemma B3's hypothesis;
P ≥ 1, P ≤ a′) and M < a′ - a, then n ≤ L + a′ - M + 2P.

The proof is entry 13's: Theorem A‴'s white run reaches the settled band; the nearest black diagonal to its left
exists (diagonal 0, the edge, is black), and Lemma B3 bounds the run. The definitions and lemmas of
TheoremAprime.lean and LemmaB3.lean are repeated here verbatim, in one namespace.

How to check: as for TheoremA.lean; the `#print axioms` line must list no `sorryAx`.
-/

namespace TheoremA4

/-- One Rule 30 step (as in TheoremA.lean). -/
def step (x : ℤ → Bool) : ℤ → Bool := fun i => xor (x (i - 1)) (x i || x (i + 1))

/-- The evolution from `x0` (as in TheoremA.lean). -/
def ev (x0 : ℤ → Bool) : ℕ → ℤ → Bool
  | 0 => x0
  | t + 1 => step (ev x0 t)

lemma ev_succ (x0 : ℤ → Bool) (t : ℕ) (i : ℤ) :
    ev x0 (t + 1) i = xor (ev x0 t (i - 1)) (ev x0 t i || ev x0 t (i + 1)) := rfl

/-- Fact 2 (as in TheoremA.lean): the leftmost black cell moves left one cell a step. -/
lemma edge (x0 : ℤ → Bool) (e : ℤ) (he : x0 e = true) (hl : ∀ j < e, x0 j = false) (t : ℕ) :
    ev x0 t (e - t) = true ∧ ∀ j < e - t, ev x0 t j = false := by
  induction t with
  | zero => simpa using ⟨he, hl⟩
  | succ t ih =>
    obtain ⟨h1, h2⟩ := ih
    constructor
    · rw [ev_succ]
      have a1 : ev x0 t (e - ↑(t + 1) - 1) = false := h2 _ (by push_cast; omega)
      have a2 : ev x0 t (e - ↑(t + 1)) = false := h2 _ (by push_cast; omega)
      have a3 : e - ↑(t + 1) + 1 = e - ↑t := by push_cast; ring
      rw [a1, a2, a3, h1]; rfl
    · intro j hj
      rw [ev_succ]
      have b1 : ev x0 t (j - 1) = false := h2 _ (by push_cast at hj; omega)
      have b2 : ev x0 t j = false := h2 _ (by push_cast at hj; omega)
      have b3 : ev x0 t (j + 1) = false := h2 _ (by push_cast at hj; omega)
      rw [b1, b2, b3]; rfl

/-- Read right to left: x_t(j - 1) from x_(t+1)(j), x_t(j) and x_t(j + 1). -/
lemma inv (x0 : ℤ → Bool) (t : ℕ) (j : ℤ) :
    ev x0 t (j - 1) = xor (ev x0 (t + 1) j) (ev x0 t j || ev x0 t (j + 1)) := by
  rw [ev_succ]
  cases ev x0 t (j - 1) <;> cases (ev x0 t j || ev x0 t (j + 1)) <;> rfl

/-- Equal blocks on columns i and i + 1 at times a .. a + n - 1 and a′ .. a′ + n - 1 make the rows agree: the cell
m to the left of column i agrees at times a + s and a′ + s whenever s + m < n. -/
lemma agree (x0 : ℤ → Bool) (i : ℤ) (n a a' : ℕ)
    (hblock : ∀ s : ℕ, s < n → ev x0 (a + s) i = ev x0 (a' + s) i ∧ ev x0 (a + s) (i + 1) = ev x0 (a' + s) (i + 1)) :
    ∀ m s : ℕ, s + m < n → ev x0 (a + s) (i - m) = ev x0 (a' + s) (i - m) := by
  intro m
  induction m using Nat.strong_induction_on with
  | _ m ih =>
    intro s hs
    rcases m with _ | m
    · simpa using (hblock s (by omega)).1
    · -- the cell m + 1 to the left from the cells m and m - 1 to the left (or column i + 1 when m = 0)
      have h1 : ev x0 (a + s + 1) (i - m) = ev x0 (a' + s + 1) (i - m) := by
        have := ih m (by omega) (s + 1) (by omega)
        rwa [show a + (s + 1) = a + s + 1 by ring, show a' + (s + 1) = a' + s + 1 by ring] at this
      have h2 : ev x0 (a + s) (i - m) = ev x0 (a' + s) (i - m) := ih m (by omega) s (by omega)
      have h3 : ev x0 (a + s) (i - m + 1) = ev x0 (a' + s) (i - m + 1) := by
        rcases m with _ | m
        · simpa using (hblock s (by omega)).2
        · have := ih m (by omega) s (by omega)
          rwa [show i - ((m : ℕ) : ℤ) = i - ((m + 1 : ℕ) : ℤ) + 1 by push_cast; ring] at this
      rw [show i - ((m + 1 : ℕ) : ℤ) = (i - m) - 1 by push_cast; ring, inv x0 (a + s), inv x0 (a' + s), h1, h2, h3]

/-- Theorem A′. -/
theorem theorem_A' (x0 : ℤ → Bool) (i : ℤ) (L : ℕ) (hc : x0 (i - L) = true) (hl : ∀ j < i - L, x0 j = false)
    (n a a' : ℕ) (haa : a < a')
    (hblock : ∀ s : ℕ, s < n → ev x0 (a + s) i = ev x0 (a' + s) i ∧ ev x0 (a + s) (i + 1) = ev x0 (a' + s) (i + 1)) :
    n ≤ L + a' := by
  by_contra h
  push Not at h
  have hag := agree x0 i n a a' hblock (L + a') 0 (by omega)
  simp only [add_zero] at hag
  have E := edge x0 (i - L) hc hl
  have black : ev x0 a' (i - ((L + a' : ℕ) : ℤ)) = true := by
    have := (E a').1
    rwa [show i - (L : ℤ) - (a' : ℤ) = i - ((L + a' : ℕ) : ℤ) by push_cast; ring] at this
  have white : ev x0 a (i - ((L + a' : ℕ) : ℤ)) = false :=
    (E a).2 _ (by push_cast; omega)
  rw [white, black] at hag
  exact absurd hag (by decide)

/-- Theorem A‴ (entry 10): row a′ is white at the distances L + a + 1 .. n - 1 left of column i, which are its
diagonals L + a′ - n + 1 .. a′ - a - 1. -/
theorem theorem_A3_white (x0 : ℤ → Bool) (i : ℤ) (L : ℕ) (hc : x0 (i - L) = true) (hl : ∀ j < i - L, x0 j = false)
    (n a a' : ℕ)
    (hblock : ∀ s : ℕ, s < n → ev x0 (a + s) i = ev x0 (a' + s) i ∧ ev x0 (a + s) (i + 1) = ev x0 (a' + s) (i + 1)) :
    ∀ δ : ℕ, L + a + 1 ≤ δ → δ + 1 ≤ n → ev x0 a' (i - δ) = false := by
  intro δ h1 h2
  have hag := agree x0 i n a a' hblock δ 0 (by omega)
  simp only [add_zero] at hag
  rw [← hag]
  exact (edge x0 (i - L) hc hl a).2 _ (by omega)

/-- Theorem A‴'s corollary: if diagonal b (the cell b right of the moving left edge) is black at time a′ and
b < a′ - a, then n ≤ L + a′ - b. -/
theorem theorem_A3 (x0 : ℤ → Bool) (i : ℤ) (L : ℕ) (hc : x0 (i - L) = true) (hl : ∀ j < i - L, x0 j = false)
    (n a a' b : ℕ) (hb : b + a < a') (hblack : ev x0 a' (i - L - a' + b) = true)
    (hblock : ∀ s : ℕ, s < n → ev x0 (a + s) i = ev x0 (a' + s) i ∧ ev x0 (a + s) (i + 1) = ev x0 (a' + s) (i + 1)) :
    n ≤ L + a' - b := by
  by_contra h
  push Not at h
  have hw := theorem_A3_white x0 i L hc hl n a a' hblock (L + a' - b) (by omega) (by omega)
  rw [show i - ((L + a' - b : ℕ) : ℤ) = i - L - a' + b by push_cast [show b ≤ L + a' by omega]; ring] at hw
  rw [hw] at hblack
  exact absurd hblack (by decide)

/-- Diagonal j at time t. -/
def D (x0 : ℤ → Bool) (e : ℤ) (j : ℤ) (t : ℕ) : Bool := ev x0 t (e - t + j)

lemma D_succ (x0 : ℤ → Bool) (e j : ℤ) (t : ℕ) :
    D x0 e j (t + 1) = xor (D x0 e (j - 2) t) (D x0 e (j - 1) t || D x0 e j t) := by
  unfold D
  rw [ev_succ]
  rw [show e - ((t + 1 : ℕ) : ℤ) + j - 1 = e - t + (j - 2) by push_cast; ring,
    show e - ((t + 1 : ℕ) : ℤ) + j = e - t + (j - 1) by push_cast; ring,
    show e - (t : ℤ) + (j - 1) + 1 = e - t + j by ring]

/-- A white cell at time τ + 1 forces D_(k-2) = D_(k-1) or D_k at time τ. -/
lemma constraint (x0 : ℤ → Bool) (e k : ℤ) (τ : ℕ) (h : D x0 e k (τ + 1) = false) :
    D x0 e (k - 2) τ = (D x0 e (k - 1) τ || D x0 e k τ) := by
  rw [D_succ] at h
  revert h
  cases D x0 e (k - 2) τ <;> cases (D x0 e (k - 1) τ || D x0 e k τ) <;> simp

/-- One step back from a white run bounded by a black cell: older (white two wider, black two further left), or
newborn (black on [g - 1, M' - 2]). -/
lemma back (x0 : ℤ → Bool) (e g M' : ℤ) (τ : ℕ) (hgM : g + 1 ≤ M') (hg : D x0 e g (τ + 1) = true)
    (hw : ∀ k, g + 1 ≤ k → k ≤ M' → D x0 e k (τ + 1) = false) :
    ((∀ k, g - 1 ≤ k → k ≤ M' → D x0 e k τ = false) ∧ D x0 e (g - 2) τ = true) ∨
    (∀ k, g - 1 ≤ k → k ≤ M' - 2 → D x0 e k τ = true) := by
  by_cases hall : ∀ k, g - 1 ≤ k → k ≤ M' → D x0 e k τ = false
  · left
    refine ⟨hall, ?_⟩
    have := hg
    rw [D_succ, hall (g - 1) le_rfl (by omega), hall g (by omega) (by omega)] at this
    simpa using this
  · right
    push Not at hall
    obtain ⟨k0, hk0a, hk0b, hk0⟩ := hall
    have hk0' : D x0 e k0 τ = true := by simpa using hk0
    have top : D x0 e (M' - 1) τ = true ∨ D x0 e M' τ = true := by
      by_contra hn
      push Not at hn
      have h1 : D x0 e (M' - 1) τ = false := by simpa using hn.1
      have h2 : D x0 e M' τ = false := by simpa using hn.2
      have down : ∀ n : ℕ, ∀ k, k = M' - n → g - 1 ≤ k → D x0 e k τ = false := by
        intro n
        induction n using Nat.strong_induction_on with
        | _ n ih =>
          intro k hk hkg
          rcases n with _ | _ | n
          · rw [hk]; simpa using h2
          · rw [hk]; simpa using h1
          · have c := constraint x0 e (k + 2) τ (hw (k + 2) (by omega) (by omega))
            rw [show k + 2 - 2 = k by ring, show k + 2 - 1 = k + 1 by ring,
              ih (n + 1) (by omega) (k + 1) (by push_cast at hk ⊢; omega) (by omega),
              ih n (by omega) (k + 2) (by push_cast at hk ⊢; omega) (by omega)] at c
            simpa using c
      have := down (M' - k0).toNat k0 (by omega) hk0a
      rw [hk0'] at this; exact absurd this (by decide)
    have downB : ∀ n : ℕ, ∀ k, k = M' - 2 - n → g - 1 ≤ k → D x0 e k τ = true := by
      intro n
      induction n with
      | zero =>
        intro k hk hkg
        have c := constraint x0 e (k + 2) τ (hw (k + 2) (by omega) (by omega))
        rw [show k + 2 - 2 = k by ring, show k + 2 - 1 = k + 1 by ring] at c
        rw [c]
        rcases top with h | h
        · rw [show k + 1 = M' - 1 by push_cast at hk; omega, h]; rfl
        · rw [show k + 2 = M' by push_cast at hk; omega, h]; simp
      | succ n ih =>
        intro k hk hkg
        have c := constraint x0 e (k + 2) τ (hw (k + 2) (by omega) (by push_cast at hk; omega))
        rw [show k + 2 - 2 = k by ring, show k + 2 - 1 = k + 1 by ring] at c
        rw [c, ih (k + 1) (by push_cast at hk ⊢; omega) (by omega)]; rfl
    intro k hk1 hk2
    exact downB (M' - 2 - k).toNat k (by omega) hk1

/-- Forward: a white run only loses cells from its left side, two a step. -/
lemma fwd (x0 : ℤ → Bool) (e g M' : ℤ) (τ0 : ℕ) (hw : ∀ k, g + 1 ≤ k → k ≤ M' → D x0 e k τ0 = false) :
    ∀ r : ℕ, ∀ k, g + 1 + 2 * r ≤ k → k ≤ M' → D x0 e k (τ0 + r) = false := by
  intro r
  induction r with
  | zero => intro k h1 h2; simpa using hw k (by simpa using h1) h2
  | succ r ih =>
    intro k h1 h2
    rw [show τ0 + (r + 1) = (τ0 + r) + 1 by ring, D_succ, ih (k - 2) (by push_cast at h1; omega) (by omega),
      ih (k - 1) (by push_cast at h1; omega) (by omega), ih k (by push_cast at h1; omega) h2]
    rfl

/-- Lemma B3. -/
theorem lemma_B3 (x0 : ℤ → Bool) (e : ℤ) (t P : ℕ) (g M' M : ℤ) (hP : 1 ≤ P) (htP : P ≤ t) (hgM : g + 1 ≤ M')
    (hM : M' ≤ M) (hper : ∀ k, k ≤ M → D x0 e k (t - P) = D x0 e k t) (hg : D x0 e g t = true)
    (hw : ∀ k, g + 1 ≤ k → k ≤ M' → D x0 e k t = false) : M' - g ≤ 2 * P := by
  -- the older chain: A s, for s <= P, unless a birth (newborn case) happens first
  let A : ℕ → Prop := fun s => (∀ k, g - 2 * s + 1 ≤ k → k ≤ M' → D x0 e k (t - s) = false) ∧
    D x0 e (g - 2 * s) (t - s) = true
  let B : ℕ → Prop := fun s0 => ∀ k, g - 2 * s0 - 1 ≤ k → k ≤ M' - 2 → D x0 e k (t - s0 - 1) = true
  have chain : ∀ s : ℕ, s ≤ P → A s ∨ ∃ s0, s0 < s ∧ B s0 := by
    intro s
    induction s with
    | zero => intro _; left; exact ⟨fun k h1 h2 => by simpa using hw k (by simpa using h1) h2, by simpa using hg⟩
    | succ s ih =>
      intro hs
      rcases ih (by omega) with hA | ⟨s0, hs0, hB⟩
      · obtain ⟨hAw, hAb⟩ := hA
        have ht : t - s = (t - s - 1) + 1 := by omega
        rw [ht] at hAw hAb
        rcases back x0 e (g - 2 * s) M' (t - s - 1) (by omega) hAb hAw with ⟨hw2, hb2⟩ | hB
        · left
          refine ⟨fun k h1 h2 => ?_, ?_⟩
          · rw [show t - (s + 1) = t - s - 1 by omega]; exact hw2 k (by push_cast at h1; omega) h2
          · rw [show t - (s + 1) = t - s - 1 by omega, show g - 2 * ((s + 1 : ℕ) : ℤ) = g - 2 * s - 2 by
              push_cast; ring]; exact hb2
        · right
          exact ⟨s, by omega, fun k h1 h2 => hB k (by omega) h2⟩
      · right; exact ⟨s0, by omega, hB⟩
  -- A P contradicts periodicity at the black cell g
  rcases chain P le_rfl with hA | ⟨s0, hs0, hB⟩
  · exfalso
    have := hA.1 g (by omega) (by omega)
    rw [hper g (by omega), hg] at this
    exact absurd this (by decide)
  · -- forward from t - P the run is white on [g + 1 + 2r, M'] at time t - P + r
    have hw0 : ∀ k, g + 1 ≤ k → k ≤ M' → D x0 e k (t - P) = false := fun k h1 h2 => by
      rw [hper k (by omega)]; exact hw k h1 h2
    have F := fwd x0 e g M' (t - P) hw0 (P - s0 - 1)
    rw [show t - P + (P - s0 - 1) = t - s0 - 1 by omega] at F
    by_contra hlong
    push Not at hlong
    have hwhite := F (g + 1 + 2 * ((P - s0 - 1 : ℕ) : ℤ)) le_rfl (by omega)
    have hblack := hB (g + 1 + 2 * ((P - s0 - 1 : ℕ) : ℤ)) (by omega)
      (by omega)
    rw [hwhite] at hblack
    exact absurd hblack (by decide)

/-- Theorem A⁗. -/
theorem theorem_A4 (x0 : ℤ → Bool) (i : ℤ) (L : ℕ) (hc : x0 (i - L) = true) (hl : ∀ j < i - L, x0 j = false)
    (n a a' P : ℕ) (M : ℤ) (haa : a < a') (hP : 1 ≤ P) (hPa : P ≤ a') (hMa : M < (a' : ℤ) - a)
    (hblock : ∀ s : ℕ, s < n → ev x0 (a + s) i = ev x0 (a' + s) i ∧ ev x0 (a + s) (i + 1) = ev x0 (a' + s) (i + 1))
    (hper : ∀ k, k ≤ M → D x0 (i - L) k (a' - P) = D x0 (i - L) k a') :
    (n : ℤ) ≤ L + a' - M + 2 * P := by
  by_contra hlong
  push Not at hlong
  set e : ℤ := i - L with he
  -- A′: n ≤ L + a′, so the run's left end x = L + a′ - n + 1 is at least 1
  have hA' := theorem_A' x0 i L hc hl n a a' haa hblock
  -- the white run of A‴ in diagonal coordinates at time a′: diagonals x .. M
  set x : ℤ := (L : ℤ) + a' - n + 1 with hx
  have white : ∀ k, x ≤ k → k ≤ M → D x0 e k a' = false := by
    intro k h1 h2
    have hk : 0 ≤ (L : ℤ) + a' - k := by omega
    have := theorem_A3_white x0 i L hc hl n a a' hblock ((L : ℤ) + a' - k).toNat (by omega) (by omega)
    unfold D
    rw [show e - (a' : ℤ) + k = i - (((L : ℤ) + a' - k).toNat : ℤ) by rw [he, Int.toNat_of_nonneg hk]; ring]
    exact this
  -- the edge diagonal 0 is black at a′
  have black0 : D x0 e 0 a' = true := by
    unfold D; simpa using (edge x0 e (by rw [he]; exact hc) (by rw [he]; exact hl) a').1
  -- the nearest black diagonal g < x
  have hx1 : 1 ≤ x := by omega
  obtain ⟨g, hg0, hgx, hgb, hgw⟩ : ∃ g : ℤ, 0 ≤ g ∧ g < x ∧ D x0 e g a' = true ∧
      ∀ k, g + 1 ≤ k → k ≤ x - 1 → D x0 e k a' = false := by
    -- search down from x - 1 to 0
    have key : ∀ m : ℕ, ∀ y : ℤ, y = m → y ≤ x - 1 → (∀ k, y + 1 ≤ k → k ≤ x - 1 → D x0 e k a' = false) →
        ∃ g : ℤ, 0 ≤ g ∧ g < x ∧ D x0 e g a' = true ∧ ∀ k, g + 1 ≤ k → k ≤ x - 1 → D x0 e k a' = false := by
      intro m
      induction m with
      | zero =>
        intro y hy hyx hw
        exact ⟨0, le_rfl, by omega, black0, fun k h1 h2 => hw k (by omega) h2⟩
      | succ m ih =>
        intro y hy hyx hw
        by_cases hb : D x0 e y a' = true
        · exact ⟨y, by omega, by omega, hb, hw⟩
        · apply ih (y - 1) (by push_cast at hy; omega) (by omega)
          intro k h1 h2
          rcases (show k = y ∨ y + 1 ≤ k by omega) with h | h
          · subst h; simpa using hb
          · exact hw k h h2
    exact key (x - 1).toNat (x - 1) (by omega) le_rfl (fun k h1 h2 => by omega)
  -- Lemma B3 on the run [g + 1, M]
  have hB3 := lemma_B3 x0 e a' P g M M hP hPa (by omega) le_rfl hper hgb (fun k h1 h2 => by
    rcases (show k ≤ x - 1 ∨ x ≤ k by omega) with h | h
    · exact hgw k h1 h
    · exact white k h h2)
  omega

end TheoremA4

#print axioms TheoremA4.theorem_A4
