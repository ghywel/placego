/-!
# Two pairs: one injectivity law, what it implies, and a robust backward front in the rain

Local, 4 November 2026 (L1519 to L1522). Core Lean only.

A row is a function `Nat → Bool`; bit 0 is the black edge. `step` is the right-edge map
`Φ(x) = x ⊕ (2x ∨ 4x)` read on bits, and `drive k x t` is the word `V_(k+2)`, the OR of bits `k + 1` and `k` at time `t`,
which toggles bit `k + 2`.

`Law k` says: on odd rows the word `drive k` determines the bits below width `k + 2`, except for the two rain rows.
It is open for general `k` (computed through width 33). This file proves, for every `k`:

* the two rain rows `rain true`, `rain false` swap under `step`, have `drive ≡ true`, and differ (`rain_step`, `rain_drive`);
* the shift `S` commutes with `step` and carries `drive k` to `drive (k + 1)` (`S_step`, `drive_S`), so `Law (k + 1) → Law k` (`law_down`);
* `Law k` excludes a single alternating diagonal on a non-rain row (`law_no_alternating`);
* if `Law` holds at every width, the only periodic odd rows are rain (`law_no_periodic`): the light-speed recurrence conjecture.

The last part is unconditional:

* `top_up`, `top_stay`, `top_minus_one`, `top_minus_two`, `top_minus_three`: the top wall of a rain-tailed row moves by an exact local rule;
* `step_rain_tail`, `back_rain_tail`: a rain tail survives a tick forward, and survives on every predecessor;
* `front_back`: a row whose top window is one of eighteen windows of eleven cells, with rain above, has every predecessor of the same
  form three cells higher, whatever lies below the window;
* `front_not_periodic`: such a row is not periodic.
-/

namespace TwoPairs

abbrev Row := Nat → Bool

/-- One tick of the right-edge map. -/
def step (x : Row) : Row := fun j =>
  match j with
  | 0 => x 0
  | 1 => xor (x 1) (x 0)
  | j + 2 => xor (x (j + 2)) (x (j + 1) || x j)

def iter (x : Row) : Nat → Row
  | 0 => x
  | t + 1 => step (iter x t)

/-- The word `V_(k+2)`: the OR of bits `k + 1` and `k` at time `t`. -/
def drive (k : Nat) (x : Row) (t : Nat) : Bool := iter x t (k + 1) || iter x t k

/-- Bits `1 .. m - 1` alternate. -/
def RainTo (m : Nat) (x : Row) : Prop := ∀ j, 1 ≤ j → j + 1 < m → x (j + 1) = !x j

def Agree (m : Nat) (x y : Row) : Prop := ∀ j, j < m → x j = y j

/-- The law at width `k + 2`. -/
def Law (k : Nat) : Prop :=
  ∀ x y : Row, x 0 = true → y 0 = true → (∀ t, drive k x t = drive k y t) →
    Agree (k + 2) x y ∨ (RainTo (k + 2) x ∧ RainTo (k + 2) y)

theorem step_zero (x : Row) : step x 0 = x 0 := rfl
theorem step_one (x : Row) : step x 1 = xor (x 1) (x 0) := rfl
theorem step_add (x : Row) (j : Nat) : step x (j + 2) = xor (x (j + 2)) (x (j + 1) || x j) := rfl

theorem iter_zero_bit {x : Row} (h : x 0 = true) (t : Nat) : iter x t 0 = true := by
  induction t with
  | zero => exact h
  | succ t ih => exact ih

theorem iter_add (x : Row) (s t : Nat) : iter x (s + t) = iter (iter x s) t := by
  induction t with
  | zero => rfl
  | succ t ih => show step (iter x (s + t)) = step (iter (iter x s) t); rw [ih]

/-! ## The rain rows -/

def rain (b : Bool) : Row := fun j =>
  match j with
  | 0 => true
  | j + 1 => if j % 2 = 0 then b else !b

theorem rain_succ_succ (b : Bool) (j : Nat) : rain b (j + 2) = !rain b (j + 1) := by
  show (if (j + 1) % 2 = 0 then b else !b) = !(if j % 2 = 0 then b else !b)
  by_cases h : j % 2 = 0
  · have h1 : ¬ (j + 1) % 2 = 0 := by omega
    simp [h, h1]
  · have h1 : (j + 1) % 2 = 0 := by omega
    simp [h, h1]

theorem rain_or (b : Bool) (j : Nat) : (rain b (j + 1) || rain b j) = true := by
  cases j with
  | zero => show (rain b 1 || true) = true; simp
  | succ j => rw [rain_succ_succ]; cases rain b (j + 1) <;> rfl

theorem rain_step (b : Bool) : step (rain b) = rain (!b) := by
  funext j
  cases j with
  | zero => rfl
  | succ j =>
    cases j with
    | zero => show xor b true = !b; cases b <;> rfl
    | succ j =>
      rw [step_add, rain_or]
      show xor (if (j + 1) % 2 = 0 then b else !b) true = (if (j + 1) % 2 = 0 then !b else !!b)
      by_cases h : (j + 1) % 2 = 0 <;> simp [h]

theorem rain_iter (b : Bool) (t : Nat) : iter (rain b) t = rain (if t % 2 = 0 then b else !b) := by
  induction t with
  | zero => simp [iter]
  | succ t ih =>
    show step (iter (rain b) t) = _
    rw [ih, rain_step]
    by_cases h : t % 2 = 0
    · have h1 : ¬ (t + 1) % 2 = 0 := by omega
      simp [h, h1]
    · have h1 : (t + 1) % 2 = 0 := by omega
      simp [h, h1]

theorem rain_drive (b : Bool) (k t : Nat) : drive k (rain b) t = true := by
  show (iter (rain b) t (k + 1) || iter (rain b) t k) = true
  rw [rain_iter]; exact rain_or _ k

theorem rain_differ : rain true 1 ≠ rain false 1 := by decide

theorem rain_rainTo (b : Bool) (m : Nat) : RainTo m (rain b) := by
  intro j hj _
  obtain ⟨i, rfl⟩ : ∃ i, j = i + 1 := ⟨j - 1, by omega⟩
  exact rain_succ_succ b i

/-! ## The shift -/

def S (x : Row) : Row := fun j =>
  match j with
  | 0 => true
  | 1 => !x 1
  | j + 2 => x (j + 1)

theorem S_zero (x : Row) : S x 0 = true := rfl
theorem S_one (x : Row) : S x 1 = !x 1 := rfl
theorem S_add (x : Row) (j : Nat) : S x (j + 2) = x (j + 1) := rfl

theorem S_step {x : Row} (h : x 0 = true) : S (step x) = step (S x) := by
  funext j
  match j with
  | 0 => rfl
  | 1 =>
    show (!(xor (x 1) (x 0))) = xor (!x 1) true
    rw [h]; cases x 1 <;> rfl
  | 2 =>
    show xor (x 1) (x 0) = xor (x 1) (!x 1 || true)
    rw [h]; cases x 1 <;> rfl
  | 3 =>
    show xor (x 2) (x 1 || x 0) = xor (x 2) (x 1 || !x 1)
    rw [h]; cases x 1 <;> cases x 2 <;> rfl
  | j + 4 =>
    show xor (x (j + 3)) (x (j + 2) || x (j + 1)) = xor (x (j + 3)) (x (j + 2) || x (j + 1))
    rfl

theorem S_iter {x : Row} (h : x 0 = true) (t : Nat) : S (iter x t) = iter (S x) t := by
  induction t with
  | zero => rfl
  | succ t ih =>
    show S (step (iter x t)) = step (iter (S x) t)
    rw [S_step (iter_zero_bit h t), ih]

theorem drive_S {x : Row} (h : x 0 = true) (k t : Nat) (hk : 1 ≤ k) : drive (k + 1) (S x) t = drive k x t := by
  obtain ⟨i, rfl⟩ : ∃ i, k = i + 1 := ⟨k - 1, by omega⟩
  show (iter (S x) t (i + 3) || iter (S x) t (i + 2)) = (iter x t (i + 2) || iter x t (i + 1))
  rw [← S_iter h t]
  rfl

theorem law_down {k : Nat} (hk : 1 ≤ k) (hL : Law (k + 1)) : Law k := by
  intro x y hx hy hd
  have hd' : ∀ t, drive (k + 1) (S x) t = drive (k + 1) (S y) t := by
    intro t; rw [drive_S hx k t hk, drive_S hy k t hk]; exact hd t
  rcases hL (S x) (S y) rfl rfl hd' with ha | ⟨hrx, hry⟩
  · left
    intro j hj
    cases j with
    | zero => rw [hx, hy]
    | succ i => exact ha (i + 2) (by omega)
  · right
    constructor
    · intro j h1 h2
      obtain ⟨i, rfl⟩ : ∃ i, j = i + 1 := ⟨j - 1, by omega⟩
      exact hrx (i + 2) (by omega) (by omega)
    · intro j h1 h2
      obtain ⟨i, rfl⟩ : ∃ i, j = i + 1 := ⟨j - 1, by omega⟩
      exact hry (i + 2) (by omega) (by omega)

/-- `Law k` excludes an alternating diagonal on a non-rain row. -/
theorem law_no_alternating {k : Nat} (hL : Law k) {x : Row} (hx : x 0 = true)
    (hone : ∀ t, drive k x t = true) : RainTo (k + 2) x := by
  rcases hL x (rain (x 1)) hx rfl (fun t => by rw [hone t, rain_drive]) with ha | ⟨h, _⟩
  · intro j h1 h2
    rw [ha (j + 1) (by omega), ha j (by omega)]
    exact rain_rainTo _ _ j h1 h2
  · exact h

/-! ## The law implies that only rain is periodic -/

def Spow : Nat → Row → Row
  | 0, x => x
  | e + 1, x => S (Spow e x)

theorem Spow_zero_bit {x : Row} (h : x 0 = true) (e : Nat) : Spow e x 0 = true := by
  cases e with
  | zero => exact h
  | succ e => rfl

theorem drive_Spow {x : Row} (h : x 0 = true) (e k t : Nat) (hk : 1 ≤ k) :
    drive (k + e) (Spow e x) t = drive k x t := by
  induction e with
  | zero => rfl
  | succ e ih =>
    show drive (k + e + 1) (S (Spow e x)) t = _
    rw [drive_S (Spow_zero_bit h e) (k + e) t (by omega)]; exact ih

theorem S_alt {y : Row} {m : Nat} (h : ∀ j, 1 ≤ j → j < m → y (j + 1) = !y j) :
    ∀ j, 1 ≤ j → j < m + 1 → S y (j + 1) = !S y j := by
  intro j h1 h2
  match j, h1, h2 with
  | 1, _, _ => show y 1 = !!y 1; simp
  | i + 2, _, h2 => exact h (i + 1) (by omega) (by omega)

theorem Spow_alt {x : Row} {m : Nat} (h : ∀ j, 1 ≤ j → j < m → x (j + 1) = !x j) (e : Nat) :
    ∀ j, 1 ≤ j → j < m + e → Spow e x (j + 1) = !Spow e x j := by
  induction e with
  | zero => exact h
  | succ e ih => exact S_alt ih

/-- The pigeonhole principle for a sequence of bounded naturals. -/
theorem pigeon : ∀ (B : Nat) (g : Nat → Nat), (∀ i, g i < B) → ∃ i j, i < j ∧ g i = g j := by
  intro B
  induction B with
  | zero => intro g h; exact absurd (h 0) (Nat.not_lt_zero _)
  | succ B ih =>
    intro g h
    by_cases hx : ∃ j, 0 < j ∧ g j = g 0
    · obtain ⟨j, h1, h2⟩ := hx
      exact ⟨0, j, h1, h2.symm⟩
    · have hne : ∀ i, g (i + 1) ≠ g 0 := fun i e => hx ⟨i + 1, by omega, e⟩
      let g' : Nat → Nat := fun i => if g (i + 1) > g 0 then g (i + 1) - 1 else g (i + 1)
      have hb : ∀ i, g' i < B := by
        intro i
        have h1 := h (i + 1)
        have h2 := h 0
        have h3 := hne i
        show (if g (i + 1) > g 0 then g (i + 1) - 1 else g (i + 1)) < B
        split <;> omega
      obtain ⟨i, j, hij, he⟩ := ih g' hb
      refine ⟨i + 1, j + 1, by omega, ?_⟩
      have h3 := hne i
      have h4 := hne j
      have he' : (if g (i + 1) > g 0 then g (i + 1) - 1 else g (i + 1)) =
          (if g (j + 1) > g 0 then g (j + 1) - 1 else g (j + 1)) := he
      split at he' <;> split at he' <;> omega

/-- A finite word as a natural number. -/
def code (f : Nat → Bool) : Nat → Nat
  | 0 => 0
  | n + 1 => 2 * code f n + (if f n then 1 else 0)

theorem code_lt (f : Nat → Bool) (n : Nat) : code f n < 2 ^ n := by
  induction n with
  | zero => show 0 < 1; omega
  | succ n ih =>
    show 2 * code f n + (if f n then 1 else 0) < 2 ^ (n + 1)
    rw [Nat.pow_succ]
    split <;> omega

theorem code_inj {f g : Nat → Bool} {n : Nat} (h : code f n = code g n) : ∀ t, t < n → f t = g t := by
  induction n with
  | zero => intro t ht; omega
  | succ n ih =>
    have h' : 2 * code f n + (if f n then 1 else 0) = 2 * code g n + (if g n then 1 else 0) := h
    have hlow : code f n = code g n := by split at h' <;> split at h' <;> omega
    have htop : f n = g n := by
      cases hf : f n <;> cases hg : g n <;> simp [hf, hg] at h' ⊢ <;> omega
    intro t ht
    by_cases e : t = n
    · rw [e]; exact htop
    · exact ih hlow t (by omega)

theorem drive_period {x : Row} {P : Nat} (hP : 0 < P) (hper : iter x P = x) (t : Nat) :
    ∃ r, r < P ∧ ∀ k, drive k x t = drive k x r := by
  induction t using Nat.strongRecOn with
  | _ t ih =>
    by_cases h : t < P
    · exact ⟨t, h, fun _ => rfl⟩
    · obtain ⟨s, rfl⟩ : ∃ s, t = P + s := ⟨t - P, by omega⟩
      obtain ⟨r, hr, e⟩ := ih s (by omega)
      refine ⟨r, hr, fun k => ?_⟩
      rw [← e k]
      show (iter x (P + s) (k + 1) || iter x (P + s) k) = (iter x s (k + 1) || iter x s k)
      rw [iter_add, hper]

/-- A first wall below any wall. -/
theorem first_wall {x : Row} : ∀ k, 1 ≤ k → x (k + 1) = x k →
    ∃ k', 1 ≤ k' ∧ x (k' + 1) = x k' ∧ ∀ j, 1 ≤ j → j < k' → x (j + 1) = !x j := by
  intro k
  induction k using Nat.strongRecOn with
  | _ k ih =>
    intro h1 h2
    by_cases h : ∀ j, 1 ≤ j → j < k → x (j + 1) = !x j
    · exact ⟨k, h1, h2, h⟩
    · have : ∃ j, 1 ≤ j ∧ j < k ∧ x (j + 1) = x j := by
        apply Classical.byContradiction
        intro hn
        apply h
        intro j a b
        cases hj : x j <;> cases hj' : x (j + 1) <;> simp
        · exact hn ⟨j, a, b, by rw [hj, hj']⟩
        · exact hn ⟨j, a, b, by rw [hj, hj']⟩
      obtain ⟨j, a, b, c⟩ := this
      exact ih j b a c

/-- **If the law holds at every width, the only periodic odd rows are rain.** -/
theorem law_no_periodic (hL : ∀ k, Law k) {x : Row} (hx : x 0 = true) {P : Nat} (hP : 0 < P)
    (hper : iter x P = x) : ∀ j, 1 ≤ j → x (j + 1) = !x j := by
  apply Classical.byContradiction
  intro hn
  have : ∃ k, 1 ≤ k ∧ x (k + 1) = x k := by
    apply Classical.byContradiction
    intro hm
    apply hn
    intro j hj
    cases a : x j <;> cases b : x (j + 1) <;> simp
    · exact hm ⟨j, hj, by rw [a, b]⟩
    · exact hm ⟨j, hj, by rw [a, b]⟩
  obtain ⟨k0, h1, h2⟩ := this
  obtain ⟨k, hk1, hk2, hk3⟩ := first_wall k0 h1 h2
  -- two levels share a word
  let g : Nat → Nat := fun m => code (drive (k + m + 1) x) P
  obtain ⟨m, m', hmm, he⟩ := pigeon (2 ^ P) g (fun i => code_lt _ _)
  have heq := code_inj he
  obtain ⟨e, rfl⟩ : ∃ e, m' = m + e + 1 := ⟨m' - m - 1, by omega⟩
  have hidx : k + (m + e + 1) + 1 = k + m + 1 + (e + 1) := by omega
  have hall : ∀ t, drive (k + m + 1 + (e + 1)) (Spow (e + 1) x) t = drive (k + m + 1 + (e + 1)) x t := by
    intro t
    rw [drive_Spow hx (e + 1) (k + m + 1) t (by omega)]
    obtain ⟨r, hr, e1⟩ := drive_period hP hper t
    rw [e1, e1, ← hidx]
    exact heq r hr
  have hnot : x (k + 1) ≠ !x k := by
    rw [hk2]; cases x k <;> simp
  rcases hL (k + m + 1 + (e + 1)) (Spow (e + 1) x) x (Spow_zero_bit hx _) hx hall with ha | ⟨_, hr⟩
  · have e1 := ha (k + 1) (by omega)
    have e2 := ha k (by omega)
    have e3 := Spow_alt hk3 (e + 1) k hk1 (by omega)
    rw [e1, e2] at e3
    exact hnot e3
  · exact hnot (hr k hk1 (by omega))

/-! ## Rain tails survive both ways -/

def seg (x : Row) : Nat → Nat → List Bool
  | _, 0 => []
  | L, n + 1 => x L :: seg x (L + 1) n

/-- The inverse recursion read along a list: `p1`, `p2` are the two output bits below it. -/
def back (p1 p2 : Bool) : List Bool → List Bool
  | [] => []
  | b :: r => xor b (p1 || p2) :: back (xor b (p1 || p2)) p1 r

def alt (b : Bool) : Nat → List Bool
  | 0 => []
  | n + 1 => b :: alt (!b) n

theorem seg_length (x : Row) (n : Nat) : ∀ L, (seg x L n).length = n := by
  induction n with
  | zero => intro L; rfl
  | succ n ih => intro L; simp [seg, ih]

theorem seg_append (x : Row) (a b : Nat) : ∀ L, seg x L (a + b) = seg x L a ++ seg x (L + a) b := by
  induction a with
  | zero => intro L; simp [seg]
  | succ a ih =>
    intro L
    have : a + 1 + b = (a + b) + 1 := by omega
    rw [this]
    show x L :: seg x (L + 1) (a + b) = (x L :: seg x (L + 1) a) ++ seg x (L + (a + 1)) b
    rw [ih (L + 1)]
    have : L + 1 + a = L + (a + 1) := by omega
    rw [this]; rfl

theorem seg_getD (x : Row) (n : Nat) : ∀ L i, i < n → (seg x L n).getD i false = x (L + i) := by
  induction n with
  | zero => intro L i h; omega
  | succ n ih =>
    intro L i h
    cases i with
    | zero => rfl
    | succ i =>
      show (seg x (L + 1) n).getD i false = x (L + (i + 1))
      rw [ih (L + 1) i (by omega)]
      have : L + 1 + i = L + (i + 1) := by omega
      rw [this]

theorem seg_alt {x : Row} {J : Nat} (h : ∀ j, J ≤ j → x (j + 1) = !x j) (n : Nat) :
    ∀ L, J ≤ L → seg x L n = alt (x L) n := by
  induction n with
  | zero => intro L _; rfl
  | succ n ih =>
    intro L hL
    show x L :: seg x (L + 1) n = x L :: alt (!x L) n
    rw [ih (L + 1) (by omega), h L hL]

theorem back_seg {z x : Row} (hs : step z = x) (n : Nat) :
    ∀ L, 2 ≤ L → seg z L n = back (z (L - 1)) (z (L - 2)) (seg x L n) := by
  induction n with
  | zero => intro L _; rfl
  | succ n ih =>
    intro L hL
    obtain ⟨i, rfl⟩ : ∃ i, L = i + 2 := ⟨L - 2, by omega⟩
    have hx : x (i + 2) = xor (z (i + 2)) (z (i + 1) || z i) := by rw [← hs]; rfl
    have ho : xor (x (i + 2)) (z (i + 1) || z i) = z (i + 2) := by
      rw [hx]; cases z (i + 2) <;> cases (z (i + 1) || z i) <;> rfl
    show z (i + 2) :: seg z (i + 2 + 1) n =
      xor (x (i + 2)) (z (i + 1) || z i) :: back (xor (x (i + 2)) (z (i + 1) || z i)) (z (i + 1)) (seg x (i + 2 + 1) n)
    rw [ho, ih (i + 2 + 1) (by omega)]
    rfl

/-- Once a predecessor is the complement of a rain tail on two adjacent bits, it is for ever. -/
theorem compl_tail {z x : Row} (hs : step z = x) {J : Nat} (hx : ∀ j, J ≤ j → x (j + 1) = !x j)
    (h0 : z J = !x J) (h1 : z (J + 1) = !x (J + 1)) (d : Nat) :
    z (J + d) = !x (J + d) ∧ z (J + d + 1) = !x (J + d + 1) := by
  induction d with
  | zero => exact ⟨h0, h1⟩
  | succ d ih =>
    obtain ⟨a, b⟩ := ih
    refine ⟨b, ?_⟩
    have hxx : x (J + d + 2) = xor (z (J + d + 2)) (z (J + d + 1) || z (J + d)) := by rw [← hs]; rfl
    have hxs := hx (J + d) (by omega)
    have hor : (z (J + d + 1) || z (J + d)) = true := by
      rw [b, a, hxs]; cases x (J + d) <;> rfl
    rw [hor] at hxx
    show z (J + d + 2) = !x (J + d + 2)
    rw [hxx]; cases z (J + d + 2) <;> rfl

theorem tail_of_compl {z x : Row} (hs : step z = x) {J : Nat} (hx : ∀ j, J ≤ j → x (j + 1) = !x j)
    (h0 : z J = !x J) (h1 : z (J + 1) = !x (J + 1)) : ∀ j, J ≤ j → z (j + 1) = !z j := by
  intro j hj
  obtain ⟨d, rfl⟩ : ∃ d, j = J + d := ⟨j - J, by omega⟩
  obtain ⟨a, b⟩ := compl_tail hs hx h0 h1 d
  rw [a, b, hx (J + d) (by omega)]

/-- A rain tail survives a forward tick. -/
theorem step_rain_tail {x : Row} {D : Nat} (h : ∀ j, D ≤ j → x (j + 1) = !x j) :
    ∀ j, D + 2 ≤ j → step x (j + 1) = !step x j := by
  intro j hj
  obtain ⟨i, rfl⟩ : ∃ i, j = i + 2 := ⟨j - 2, by omega⟩
  have a1 := h i (by omega)
  have a2 := h (i + 1) (by omega)
  have a3 := h (i + 2) (by omega)
  show xor (x (i + 3)) (x (i + 2) || x (i + 1)) = !xor (x (i + 2)) (x (i + 1) || x i)
  rw [a3, a2, a1]
  cases x i <;> rfl

theorem chk_tail : ∀ p1 p2 b : Bool,
    (back p1 p2 (alt b 5)).getD 3 false = !(alt b 5).getD 3 false ∧
    (back p1 p2 (alt b 5)).getD 4 false = !(alt b 5).getD 4 false := by decide

/-- A rain tail survives a backward tick, three bits higher: every predecessor of a rain-tailed row is rain-tailed. -/
theorem back_rain_tail {z x : Row} {D : Nat} (hD : 2 ≤ D) (hs : step z = x)
    (h : ∀ j, D ≤ j → x (j + 1) = !x j) : ∀ j, D + 3 ≤ j → z (j + 1) = !z j := by
  have e := back_seg hs 5 D hD
  rw [seg_alt h 5 D (Nat.le_refl D)] at e
  obtain ⟨c0, c1⟩ := chk_tail (z (D - 1)) (z (D - 2)) (x D)
  rw [← e, seg_getD z 5 D 3 (by omega)] at c0
  rw [← e, seg_getD z 5 D 4 (by omega)] at c1
  have s3 : (alt (x D) 5).getD 3 false = x (D + 3) := by
    rw [← seg_alt h 5 D (Nat.le_refl D)]; exact seg_getD x 5 D 3 (by omega)
  have s4 : (alt (x D) 5).getD 4 false = x (D + 4) := by
    rw [← seg_alt h 5 D (Nat.le_refl D)]; exact seg_getD x 5 D 4 (by omega)
  rw [s3] at c0
  rw [s4] at c1
  exact tail_of_compl hs (fun j hj => h j (by omega)) c0 c1

/-! ## The top-wall rule -/

/-- `D` is the top wall: its two cells agree and rain lies above. -/
def Top (x : Row) (D : Nat) : Prop := x (D + 1) = x D ∧ ∀ j, D + 1 ≤ j → x (j + 1) = !x j

/-- A white top wall rises by two and turns black. -/
theorem top_up {x : Row} {k : Nat} (h : Top x (k + 5)) (hw : x (k + 5) = false) :
    Top (step x) (k + 7) ∧ step x (k + 7) = true := by
  obtain ⟨e, hr⟩ := h
  have a1 : x (k + 7) = !x (k + 6) := hr (k + 6) (by omega)
  have a2 : x (k + 8) = !x (k + 7) := hr (k + 7) (by omega)
  have s7 : step x (k + 7) = xor (x (k + 7)) (x (k + 6) || x (k + 5)) := rfl
  have s8 : step x (k + 8) = xor (x (k + 8)) (x (k + 7) || x (k + 6)) := rfl
  have b6 : x (k + 6) = false := by rw [show k + 6 = k + 5 + 1 from rfl, e, hw]
  have r7 : step x (k + 7) = true := by rw [s7, a1, b6, hw]; rfl
  have r8 : step x (k + 8) = true := by rw [s8, a2, a1, b6]; rfl
  refine ⟨⟨by rw [show k + 7 + 1 = k + 8 from rfl, r7, r8], ?_⟩, r7⟩
  intro j hj
  exact step_rain_tail (D := k + 6) (fun i hi => hr i (by omega)) j (by omega)

/-- A black top wall with a black cell among the next two stays and turns white. -/
theorem top_stay {x : Row} {k : Nat} (h : Top x (k + 5)) (hb : x (k + 5) = true)
    (hc : (x (k + 4) || x (k + 3)) = true) : Top (step x) (k + 5) ∧ step x (k + 5) = false := by
  obtain ⟨e, hr⟩ := h
  have a1 : x (k + 7) = !x (k + 6) := hr (k + 6) (by omega)
  have a2 : x (k + 8) = !x (k + 7) := hr (k + 7) (by omega)
  have b6 : x (k + 6) = true := by rw [show k + 6 = k + 5 + 1 from rfl, e, hb]
  have r5 : step x (k + 5) = false := by
    show xor (x (k + 5)) (x (k + 4) || x (k + 3)) = false
    rw [hb, hc]; rfl
  have r6 : step x (k + 6) = false := by
    show xor (x (k + 6)) (x (k + 5) || x (k + 4)) = false
    rw [b6, hb]; rfl
  have r7 : step x (k + 7) = true := by
    show xor (x (k + 7)) (x (k + 6) || x (k + 5)) = true
    rw [a1, b6, hb]; rfl
  have r8 : step x (k + 8) = false := by
    show xor (x (k + 8)) (x (k + 7) || x (k + 6)) = false
    rw [a2, a1, b6]; rfl
  refine ⟨⟨by rw [show k + 5 + 1 = k + 6 from rfl, r5, r6], ?_⟩, r5⟩
  intro j hj
  by_cases c6 : j = k + 6
  · subst c6; rw [show k + 6 + 1 = k + 7 from rfl, r6, r7]; rfl
  · by_cases c7 : j = k + 7
    · subst c7; rw [show k + 7 + 1 = k + 8 from rfl, r7, r8]; rfl
    · exact step_rain_tail (D := k + 6) (fun i hi => hr i (by omega)) j (by omega)

/-- Above a black top wall with two white cells under it, the row after a tick reads black, white, black from the wall up. -/
theorem top_fall_rain {x : Row} {k : Nat} (h : Top x (k + 5)) (hb : x (k + 5) = true)
    (h4 : x (k + 4) = false) (h3 : x (k + 3) = false) :
    step x (k + 5) = true ∧ step x (k + 6) = false ∧ ∀ j, k + 5 ≤ j → step x (j + 1) = !step x j := by
  obtain ⟨e, hr⟩ := h
  have a1 : x (k + 7) = !x (k + 6) := hr (k + 6) (by omega)
  have a2 : x (k + 8) = !x (k + 7) := hr (k + 7) (by omega)
  have b6 : x (k + 6) = true := by rw [show k + 6 = k + 5 + 1 from rfl, e, hb]
  have r5 : step x (k + 5) = true := by
    show xor (x (k + 5)) (x (k + 4) || x (k + 3)) = true
    rw [hb, h4, h3]; rfl
  have r6 : step x (k + 6) = false := by
    show xor (x (k + 6)) (x (k + 5) || x (k + 4)) = false
    rw [b6, hb]; rfl
  have r7 : step x (k + 7) = true := by
    show xor (x (k + 7)) (x (k + 6) || x (k + 5)) = true
    rw [a1, b6, hb]; rfl
  have r8 : step x (k + 8) = false := by
    show xor (x (k + 8)) (x (k + 7) || x (k + 6)) = false
    rw [a2, a1, b6]; rfl
  refine ⟨r5, r6, ?_⟩
  intro j hj
  by_cases c5 : j = k + 5
  · subst c5; rw [show k + 5 + 1 = k + 6 from rfl, r5, r6]; rfl
  · by_cases c6 : j = k + 6
    · subst c6; rw [show k + 6 + 1 = k + 7 from rfl, r6, r7]; rfl
    · by_cases c7 : j = k + 7
      · subst c7; rw [show k + 7 + 1 = k + 8 from rfl, r7, r8]; rfl
      · exact step_rain_tail (D := k + 6) (fun i hi => hr i (by omega)) j (by omega)

/-- Retreat by one: the wall drops one cell and stays black. -/
theorem top_minus_one {x : Row} {k : Nat} (h : Top x (k + 5)) (hb : x (k + 5) = true)
    (h4 : x (k + 4) = false) (h3 : x (k + 3) = false) (h2 : x (k + 2) = true) :
    Top (step x) (k + 4) ∧ step x (k + 4) = true := by
  obtain ⟨r5, r6, hr⟩ := top_fall_rain h hb h4 h3
  have r4 : step x (k + 4) = true := by
    show xor (x (k + 4)) (x (k + 3) || x (k + 2)) = true
    rw [h4, h3, h2]; rfl
  exact ⟨⟨by rw [show k + 4 + 1 = k + 5 from rfl, r4, r5], hr⟩, r4⟩

/-- Retreat by two: the wall drops two cells and turns white. -/
theorem top_minus_two {x : Row} {k : Nat} (h : Top x (k + 5)) (hb : x (k + 5) = true)
    (h4 : x (k + 4) = false) (h3 : x (k + 3) = false) (h2 : x (k + 2) = false) (h1 : x (k + 1) = false) :
    Top (step x) (k + 3) ∧ step x (k + 3) = false := by
  obtain ⟨r5, r6, hr⟩ := top_fall_rain h hb h4 h3
  have r4 : step x (k + 4) = false := by
    show xor (x (k + 4)) (x (k + 3) || x (k + 2)) = false
    rw [h4, h3, h2]; rfl
  have r3 : step x (k + 3) = false := by
    show xor (x (k + 3)) (x (k + 2) || x (k + 1)) = false
    rw [h3, h2, h1]; rfl
  refine ⟨⟨by rw [show k + 3 + 1 = k + 4 from rfl, r3, r4], ?_⟩, r3⟩
  intro j hj
  by_cases c4 : j = k + 4
  · subst c4; rw [show k + 4 + 1 = k + 5 from rfl, r4, r5]; rfl
  · exact hr j (by omega)

/-- Retreat by three: the wall drops three cells and stays black. -/
theorem top_minus_three {x : Row} {k : Nat} (h : Top x (k + 5)) (hb : x (k + 5) = true)
    (h4 : x (k + 4) = false) (h3 : x (k + 3) = false) (h2 : x (k + 2) = false) (h1 : x (k + 1) = true) :
    Top (step x) (k + 2) ∧ step x (k + 2) = true := by
  obtain ⟨r5, r6, hr⟩ := top_fall_rain h hb h4 h3
  have r4 : step x (k + 4) = false := by
    show xor (x (k + 4)) (x (k + 3) || x (k + 2)) = false
    rw [h4, h3, h2]; rfl
  have r3 : step x (k + 3) = true := by
    show xor (x (k + 3)) (x (k + 2) || x (k + 1)) = true
    rw [h3, h2, h1]; rfl
  have r2 : step x (k + 2) = true := by
    show xor (x (k + 2)) (x (k + 1) || x k) = true
    rw [h2, h1]; rfl
  refine ⟨⟨by rw [show k + 2 + 1 = k + 3 from rfl, r2, r3], ?_⟩, r2⟩
  intro j hj
  by_cases c3 : j = k + 3
  · subst c3; rw [show k + 3 + 1 = k + 4 from rfl, r3, r4]; rfl
  · by_cases c4 : j = k + 4
    · subst c4; rw [show k + 4 + 1 = k + 5 from rfl, r4, r5]; rfl
    · exact hr j (by omega)

/-! ## The robust backward front -/

/-- The eighteen windows, low to high; the top wall is their last two cells. -/
def B11 : List (List Bool) := [
  [false, true, false, false, true, false, false, false, false, true, true],
  [false, false, true, false, true, false, false, false, false, true, true],
  [true, false, true, false, true, false, false, false, false, true, true],
  [false, true, false, true, false, true, false, false, false, true, true],
  [false, false, true, true, false, true, false, false, false, true, true],
  [true, false, true, true, false, true, false, false, false, true, true],
  [false, true, false, true, true, true, false, false, false, true, true],
  [false, false, true, true, true, true, false, false, false, true, true],
  [true, false, true, true, true, true, false, false, false, true, true],
  [false, true, false, false, true, false, false, true, false, true, true],
  [false, false, true, false, true, false, false, true, false, true, true],
  [true, false, true, false, true, false, false, true, false, true, true],
  [false, true, false, true, false, true, false, true, false, true, true],
  [false, false, true, true, false, true, false, true, false, true, true],
  [true, false, true, true, false, true, false, true, false, true, true],
  [false, true, false, true, true, true, false, true, false, true, true],
  [false, false, true, true, true, true, false, true, false, true, true],
  [true, false, true, true, true, true, false, true, false, true, true]]

/-- A row with its window of eleven cells from `L` in `B11` and rain above it. -/
def Front (x : Row) (L : Nat) : Prop :=
  seg x L 11 ∈ B11 ∧ ∀ j, L + 10 ≤ j → x (j + 1) = !x j

/-- A window with seven cells of rain over its last. -/
def inp (w : List Bool) : List Bool := w.take 10 ++ alt (w.getD 10 false) 7

theorem chk_mem : ∀ w, w ∈ B11 → ∀ p1 p2 : Bool, ((back p1 p2 (inp w)).drop 3).take 11 ∈ B11 := by decide +kernel
theorem chk_a : ∀ w, w ∈ B11 → ∀ p1 p2 : Bool,
    (back p1 p2 (inp w)).getD 14 false = !(back p1 p2 (inp w)).getD 13 false := by decide +kernel
theorem chk_b : ∀ w, w ∈ B11 → ∀ p1 p2 : Bool,
    (back p1 p2 (inp w)).getD 15 false = !(inp w).getD 15 false := by decide +kernel
theorem chk_c : ∀ w, w ∈ B11 → ∀ p1 p2 : Bool,
    (back p1 p2 (inp w)).getD 16 false = !(inp w).getD 16 false := by decide +kernel
theorem chk_d : ∀ w, w ∈ B11 → ∀ p1 p2 : Bool,
    (back p1 p2 (inp w)).getD 15 false = !(back p1 p2 (inp w)).getD 14 false := by decide +kernel
theorem chk_wall : ∀ w, w ∈ B11 → w.getD 9 false = w.getD 10 false := by decide +kernel

theorem seg_inp {x : Row} {L : Nat} (h : ∀ j, L + 10 ≤ j → x (j + 1) = !x j) : seg x L 17 = inp (seg x L 11) := by
  have e1 : seg x L 11 = seg x L 10 ++ seg x (L + 10) 1 := seg_append x 10 1 L
  have e2 : (seg x L 11).take 10 = seg x L 10 := by
    rw [e1]; exact List.take_left' (seg_length x 10 L)
  have e3 : (seg x L 11).getD 10 false = x (L + 10) := seg_getD x 11 L 10 (by omega)
  show seg x L 17 = (seg x L 11).take 10 ++ alt ((seg x L 11).getD 10 false) 7
  rw [e2, e3, ← seg_alt h 7 (L + 10) (Nat.le_refl _)]
  exact seg_append x 10 7 L

/-- **The robust backward front.** Every predecessor of a front is a front three cells higher, whatever lies below the window. -/
theorem front_back {z x : Row} {L : Nat} (hL : 2 ≤ L) (hs : step z = x) (hf : Front x L) : Front z (L + 3) := by
  obtain ⟨hw, hr⟩ := hf
  have e : seg z L 17 = back (z (L - 1)) (z (L - 2)) (inp (seg x L 11)) := by
    rw [back_seg hs 17 L hL, seg_inp hr]
  have ha := chk_a _ hw (z (L - 1)) (z (L - 2))
  have hb := chk_b _ hw (z (L - 1)) (z (L - 2))
  have hc := chk_c _ hw (z (L - 1)) (z (L - 2))
  have hd := chk_d _ hw (z (L - 1)) (z (L - 2))
  have hm := chk_mem _ hw (z (L - 1)) (z (L - 2))
  rw [← e] at ha hb hc hd hm
  have g : ∀ i, i < 17 → (seg z L 17).getD i false = z (L + i) := fun i h => seg_getD z 17 L i h
  rw [g 13 (by omega), g 14 (by omega)] at ha
  rw [g 14 (by omega), g 15 (by omega)] at hd
  rw [g 15 (by omega)] at hb
  rw [g 16 (by omega)] at hc
  have q : ∀ i, i < 17 → (inp (seg x L 11)).getD i false = x (L + i) := by
    intro i h; rw [← seg_inp hr]; exact seg_getD x 17 L i h
  rw [q 15 (by omega)] at hb
  rw [q 16 (by omega)] at hc
  have hwin : seg z (L + 3) 11 = ((seg z L 17).drop 3).take 11 := by
    have e1 : seg z L 17 = seg z L 3 ++ seg z (L + 3) 14 := seg_append z 3 14 L
    have e2 : seg z (L + 3) 14 = seg z (L + 3) 11 ++ seg z (L + 3 + 11) 3 := seg_append z 11 3 (L + 3)
    rw [e1, List.drop_left' (seg_length z 3 L), e2]
    exact (List.take_left' (seg_length z 11 (L + 3))).symm
  refine ⟨by rw [hwin]; exact hm, ?_⟩
  have htail := tail_of_compl hs (J := L + 15) (fun j hj => hr j (by omega)) hb hc
  intro j hj
  by_cases c1 : j = L + 13
  · subst c1; exact ha
  · by_cases c2 : j = L + 14
    · subst c2; exact hd
    · exact htail j (by omega)

theorem front_iter {x : Row} {L P : Nat} (hL : 2 ≤ L) (h : Front x L) (hper : iter x P = x) :
    ∀ i, i ≤ P → Front (iter x (P - i)) (L + 3 * i) := by
  intro i
  induction i with
  | zero => intro _; simpa [hper] using h
  | succ i ih =>
    intro hi
    have hs : step (iter x (P - (i + 1))) = iter x (P - i) := by
      have : P - i = (P - (i + 1)) + 1 := by omega
      rw [this]; rfl
    have := front_back (by omega) hs (ih (by omega))
    have e : L + 3 * i + 3 = L + 3 * (i + 1) := by omega
    rw [e] at this
    exact this

/-- **A row with a front is not periodic.** So a periodic row with a rain tail never shows one of the eighteen windows at its top. -/
theorem front_not_periodic {x : Row} {L P : Nat} (hL : 2 ≤ L) (h : Front x L) (hP : 0 < P) : iter x P ≠ x := by
  intro hper
  have hf := front_iter hL h hper P (Nat.le_refl P)
  have e0 : P - P = 0 := by omega
  rw [e0] at hf
  have hf' : Front x (L + 3 * P) := hf
  obtain ⟨hw, _⟩ := hf'
  have hwall := chk_wall _ hw
  rw [seg_getD x 11 _ 9 (by omega), seg_getD x 11 _ 10 (by omega)] at hwall
  have hr := h.2 (L + 3 * P + 9) (by omega)
  have : L + 3 * P + 9 + 1 = L + 3 * P + 10 := rfl
  rw [this, ← hwall] at hr
  cases hb : x (L + 3 * P + 9) <;> simp [hb] at hr

/-! ## Controls -/

example : B11.length = 18 := by decide

/-- The rain itself has no front: every window of it fails, because it has no wall. -/
example : ∀ w ∈ B11, w.getD 9 false = true := by decide

/-- A window that is not in the set: `###.###..##` loses the climb for one lower state. -/
example : ([true, true, true, false, true, true, true, false, false, true, true] : List Bool) ∉ B11 := by decide

end TwoPairs
