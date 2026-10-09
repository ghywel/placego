import Mathlib

/-!
# Entry 41 and the black end: the one-sided Jen route, word by word (Local, 2026-10-09)

The route of entry 40 (WhiteEnd.lean) for any periodic column word, at width K = 8 or 10. If, from every start, the
K cells right of a column reading the word w periodically settle (within n0 periods) into a set on which cell +1 takes
one value at each tick, then column +1 is eventually periodic too, and Theorem A (entry 5) forbids it when there is a
leftmost black cell. `check K w n0` is that finite condition, decided in the kernel.

Machine-checked here:
- `entry41`: each of PROOFS.md entry 41's 139 words (129 at width 8, 10 at width 10; the lists are WC's, L499,
  replayed by Cloud's WR2, CL111);
- `black_end`: the black-end words 0 1^m for every m >= 14 (L497; entry 38 has q = 7 and q >= 9 by another route),
  with q >= 24 reduced to 20 + (m - 20) % 4 by B^24 = B^20 on the sets that occur.

How to check: as for TheoremA.lean; the `#print axioms` lines must list no `sorryAx` (here: propext,
Classical.choice, Quot.sound; `decide +kernel` adds no axiom). About 150 s on the M5. Memory: `Elab.async false` and
one kernel check per word keep the peak near one check's, about 1.7 GB above Mathlib's mapped files (7.4 GB resident).
Statement scope: `ReadsW x0 c ws a` says column c reads the word ws periodically from time a; any phase of an
eventually periodic column with that word has such an a. Only a leftmost black cell is assumed (finite seeds have one;
see WhiteEnd.lean's `white_end_finite` for that step).
-/

set_option Elab.async false

namespace JenRoute

/-! ## Rule 30 and Theorem A (verbatim from TheoremA.lean, as in WhiteEnd.lean) -/

def step (x : ℤ → Bool) : ℤ → Bool := fun i => xor (x (i - 1)) (x i || x (i + 1))

def ev (x0 : ℤ → Bool) : ℕ → ℤ → Bool
  | 0 => x0
  | t + 1 => step (ev x0 t)

lemma edge (x0 : ℤ → Bool) (e : ℤ) (he : x0 e = true) (hl : ∀ j < e, x0 j = false) (t : ℕ) :
    ev x0 t (e - t) = true ∧ ∀ j < e - t, ev x0 t j = false := by
  induction t with
  | zero => simpa using ⟨he, hl⟩
  | succ t ih =>
    obtain ⟨h1, h2⟩ := ih
    constructor
    · show xor (ev x0 t (e - ↑(t + 1) - 1)) (ev x0 t (e - ↑(t + 1)) || ev x0 t (e - ↑(t + 1) + 1)) = true
      have a1 : ev x0 t (e - ↑(t + 1) - 1) = false := h2 _ (by push_cast; omega)
      have a2 : ev x0 t (e - ↑(t + 1)) = false := h2 _ (by push_cast; omega)
      have a3 : e - ↑(t + 1) + 1 = e - ↑t := by push_cast; ring
      rw [a1, a2, a3, h1]; rfl
    · intro j hj
      show xor (ev x0 t (j - 1)) (ev x0 t j || ev x0 t (j + 1)) = false
      have b1 : ev x0 t (j - 1) = false := h2 _ (by push_cast at hj; omega)
      have b2 : ev x0 t j = false := h2 _ (by push_cast at hj; omega)
      have b3 : ev x0 t (j + 1) = false := h2 _ (by push_cast at hj; omega)
      rw [b1, b2, b3]; rfl

def Per (x0 : ℤ → Bool) (k : ℤ) (P a b : ℕ) : Prop :=
  ∀ t : ℕ, a ≤ t → t + P ≤ b → ev x0 t k = ev x0 (t + P) k

lemma left (x0 : ℤ → Bool) (k : ℤ) (P a b : ℕ) (hP : 1 ≤ P) (h0 : Per x0 k P a b) (h1 : Per x0 (k + 1) P a b) :
    Per x0 (k - 1) P a (b - 1) := by
  intro t ht htb
  have inv : ∀ s : ℕ, ev x0 s (k - 1) = xor (ev x0 (s + 1) k) (ev x0 s k || ev x0 s (k + 1)) := by
    intro s
    show ev x0 s (k - 1) = xor (xor (ev x0 s (k - 1)) (ev x0 s k || ev x0 s (k + 1))) (ev x0 s k || ev x0 s (k + 1))
    cases ev x0 s (k - 1) <;> cases (ev x0 s k || ev x0 s (k + 1)) <;> rfl
  rw [inv t, inv (t + P)]
  have e1 : ev x0 (t + 1) k = ev x0 (t + 1 + P) k := h0 (t + 1) (by omega) (by omega)
  have e2 : ev x0 t k = ev x0 (t + P) k := h0 t ht (by omega)
  have e3 : ev x0 t (k + 1) = ev x0 (t + P) (k + 1) := h1 t ht (by omega)
  rw [e1, e2, e3, show t + 1 + P = t + P + 1 by ring]

lemma left_iter (x0 : ℤ → Bool) (k : ℤ) (P a b : ℕ) (hP : 1 ≤ P) (h0 : Per x0 k P a b) (h1 : Per x0 (k + 1) P a b) :
    ∀ j : ℕ, Per x0 (k - j) P a (b - j) ∧ Per x0 (k - j + 1) P a (b - j) := by
  intro j
  induction j with
  | zero => simpa using ⟨h0, h1⟩
  | succ j ih =>
    obtain ⟨g0, g1⟩ := ih
    have g := left x0 (k - j) P a (b - j) hP g0 (by simpa using g1)
    refine ⟨?_, ?_⟩
    · have : (k - ↑(j + 1)) = k - ↑j - 1 := by push_cast; ring
      rw [this, show b - (j + 1) = b - j - 1 by omega]; exact g
    · have e : (k - ↑(j + 1) + 1) = k - ↑j := by push_cast; ring
      rw [e, show b - (j + 1) = b - j - 1 by omega]
      intro t ht htb
      exact g0 t ht (by omega)

theorem theorem_A (x0 : ℤ → Bool) (c : ℤ) (L : ℕ) (hc : x0 (c - L) = true) (hl : ∀ j < c - L, x0 j = false)
    (P a b : ℕ) (hP : 1 ≤ P) (h0 : Per x0 c P a b) (h1 : Per x0 (c + 1) P a b) :
    b ≤ 2 * a + L + 2 * P - 1 := by
  by_contra hb
  push Not at hb
  set j : ℕ := a + P + L with hj
  have hper := (left_iter x0 c P a b hP h0 h1 j).1
  have E := edge x0 (c - L) hc hl
  have black : ev x0 (a + P) (c - j) = true := by
    have := (E (a + P)).1
    have e : c - ↑L - ↑(a + P) = c - ↑j := by rw [hj]; push_cast; ring
    rwa [e] at this
  have white : ev x0 a (c - j) = false := by
    have := (E a).2 (c - j) (by rw [hj]; push_cast; omega)
    exact this
  have := hper a le_rfl (by omega)
  rw [white, black] at this
  exact absurd this (by decide)

theorem no_two_periodic (x0 : ℤ → Bool) (c : ℤ) (L : ℕ) (hc : x0 (c - L) = true) (hl : ∀ j < c - L, x0 j = false)
    (P a : ℕ) (hP : 1 ≤ P)
    (h0 : ∀ t : ℕ, a ≤ t → ev x0 t c = ev x0 (t + P) c)
    (h1 : ∀ t : ℕ, a ≤ t → ev x0 t (c + 1) = ev x0 (t + P) (c + 1)) : False := by
  have := theorem_A x0 c L hc hl P a (2 * a + L + 2 * P) hP (fun t ht _ => h0 t ht) (fun t ht _ => h1 t ht)
  omega

/-- Evolution is a semigroup: evolving `ev x0 k` for `t` steps is evolving `x0` for `k + t`. -/
lemma ev_add (x0 : ℤ → Bool) (k t : ℕ) : ev (ev x0 k) t = ev x0 (k + t) := by
  induction t with
  | zero => rfl
  | succ t ih => show step (ev (ev x0 k) t) = step (ev x0 (k + t)); rw [ih]

/-! ## The relaxation of width K -/

/-- One step of the K cells: bit j is cell c + 1 + j, `w` the column's bit, `u` the cell beyond. -/
def stp (K w s u : ℕ) : ℕ :=
  ((((s <<< 1) ||| w) &&& (2 ^ K - 1)) ^^^ (s ||| ((s >>> 1) ||| (u <<< (K - 1))))) &&& (2 ^ K - 1)

def imgAux (K w S n : ℕ) : ℕ → ℕ :=
  Nat.rec (motive := fun _ => ℕ → ℕ) (fun acc => acc)
    (fun k ih acc => ih (if S.testBit k then acc ||| (1 <<< stp K w k 0) ||| (1 <<< stp K w k 1) else acc)) n

lemma imgAux_succ (K w S n acc : ℕ) : imgAux K w S (n + 1) acc =
    imgAux K w S n (if S.testBit n then acc ||| (1 <<< stp K w n 0) ||| (1 <<< stp K w n 1) else acc) := rfl

def img (K w S : ℕ) : ℕ := imgAux K w S (2 ^ K) 0

/-- The steps of a word, in order. -/
def run (K : ℕ) : List ℕ → ℕ → ℕ
  | [], S => S
  | w :: ws, S => run K ws (img K w S)

def reach (K : ℕ) (ws : List ℕ) : ℕ → ℕ
  | 0 => 2 ^ (2 ^ K) - 1
  | n + 1 => run K ws (reach K ws n)

/-- Cell c + 1 takes one value on the set `S`. -/
def const0 (K S : ℕ) : Bool :=
  (List.range (2 ^ K)).all (fun s => !(S.testBit s) || !(s.testBit 0)) ||
  (List.range (2 ^ K)).all (fun s => !(S.testBit s) || s.testBit 0)

def ticks (K : ℕ) : List ℕ → ℕ → Bool
  | [], _ => true
  | w :: ws, X => const0 K X && ticks K ws (img K w X)

def check (K : ℕ) (ws : List ℕ) (n0 : ℕ) : Bool :=
  run K ws (reach K ws n0) == reach K ws n0 && ticks K ws (reach K ws n0)

def StpOK (K : ℕ) : Prop := ∀ s < 2 ^ K, ∀ w u : Bool, ∀ j < K,
    (stp K w.toNat s u.toNat).testBit j =
      xor (if j = 0 then w else s.testBit (j - 1)) (s.testBit j || if j = K - 1 then u else s.testBit (j + 1))

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma stpOK8 : StpOK 8 := by unfold StpOK; decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma stpOK10 : StpOK 10 := by unfold StpOK; decide +kernel

lemma stp_lt (K w s u : ℕ) : stp K w s u < 2 ^ K := by
  unfold stp
  exact lt_of_le_of_lt Nat.and_le_right (Nat.sub_lt (Nat.two_pow_pos K) one_pos)

/-! ## Sets: membership -/

lemma imgAux_acc (K w S : ℕ) : ∀ n acc y, acc.testBit y = true → (imgAux K w S n acc).testBit y = true := by
  intro n
  induction n with
  | zero => intro acc y h; exact h
  | succ n ih =>
    intro acc y h
    rw [imgAux_succ]
    apply ih
    split_ifs
    · simp [Nat.testBit_or, h]
    · exact h

lemma imgAux_mem (K w S u : ℕ) (hu : u ≤ 1) :
    ∀ n acc s, s < n → S.testBit s = true → (imgAux K w S n acc).testBit (stp K w s u) = true := by
  intro n
  induction n with
  | zero => intro acc s hs; omega
  | succ n ih =>
    intro acc s hs hS
    rw [imgAux_succ]
    rcases Nat.lt_succ_iff_lt_or_eq.mp hs with h | h
    · exact ih _ s h hS
    · subst h
      apply imgAux_acc
      rw [if_pos hS]
      interval_cases u <;> simp [Nat.testBit_or]

lemma img_mem (K w S s u : ℕ) (hs : s < 2 ^ K) (hu : u ≤ 1) (hS : S.testBit s = true) :
    (img K w S).testBit (stp K w s u) = true :=
  imgAux_mem K w S u hu (2 ^ K) 0 s hs hS

lemma const0_spec (K S : ℕ) (h : const0 K S = true) :
    ∃ b, ∀ s < 2 ^ K, S.testBit s = true → s.testBit 0 = b := by
  simp only [const0, Bool.or_eq_true, List.all_eq_true, List.mem_range] at h
  rcases h with h | h
  · refine ⟨false, fun s hs hS => ?_⟩
    have := h s hs; rw [hS] at this; simpa using this
  · refine ⟨true, fun s hs hS => ?_⟩
    have := h s hs; rw [hS] at this; simpa using this

/-! ## The actual window -/

def enc (f : ℕ → Bool) : ℕ → ℕ
  | 0 => 0
  | k + 1 => Nat.bit (f 0) (enc (fun j => f (j + 1)) k)

lemma enc_lt (f : ℕ → Bool) (k : ℕ) : enc f k < 2 ^ k := by
  induction k generalizing f with
  | zero => simp [enc]
  | succ k ih =>
    have := ih (fun j => f (j + 1))
    simp only [enc]
    cases f 0 <;> simp [Nat.bit, pow_succ] <;> omega

lemma enc_testBit (f : ℕ → Bool) (k j : ℕ) : (enc f k).testBit j = (decide (j < k) && f j) := by
  induction k generalizing f j with
  | zero => simp [enc]
  | succ k ih =>
    rcases j with _ | j
    · simp [enc]
    · simp only [enc, Nat.testBit_bit_succ, ih]
      simp

def win (K : ℕ) (x0 : ℤ → Bool) (c : ℤ) (t : ℕ) : ℕ := enc (fun j => ev x0 t (c + 1 + j)) K

lemma win_lt (K : ℕ) (x0 : ℤ → Bool) (c : ℤ) (t : ℕ) : win K x0 c t < 2 ^ K := enc_lt _ K

lemma win_bit (K : ℕ) (x0 : ℤ → Bool) (c : ℤ) (t j : ℕ) (hj : j < K) :
    (win K x0 c t).testBit j = ev x0 t (c + 1 + j) := by
  simp [win, enc_testBit, hj]

lemma win_step (K : ℕ) (hK : StpOK K) (hK2 : 2 ≤ K) (x0 : ℤ → Bool) (c : ℤ) (t : ℕ) :
    win K x0 c (t + 1) = stp K (ev x0 t c).toNat (win K x0 c t) (ev x0 t (c + K + 1)).toNat := by
  apply Nat.eq_of_testBit_eq
  intro j
  by_cases hj : j < K
  · rw [win_bit K x0 c (t + 1) j hj, hK _ (win_lt K x0 c t) _ _ j hj]
    show xor (ev x0 t (c + 1 + j - 1)) (ev x0 t (c + 1 + j) || ev x0 t (c + 1 + j + 1)) = _
    rw [win_bit K x0 c t j hj]
    congr 1
    · split_ifs with h0
      · subst h0; congr 1; ring
      · rw [win_bit K x0 c t (j - 1) (by omega)]; congr 1; push_cast [show 1 ≤ j by omega]; ring
    · congr 1
      split_ifs with h7
      · congr 1; rw [h7]; push_cast [show 1 ≤ K by omega]; ring
      · rw [win_bit K x0 c t (j + 1) (by omega)]; congr 1; push_cast; ring
  · have hK' : 2 ^ K ≤ 2 ^ j := Nat.pow_le_pow_right (by norm_num) (by omega)
    rw [Nat.testBit_eq_false_of_lt (lt_of_lt_of_le (win_lt K x0 c (t + 1)) hK'),
      Nat.testBit_eq_false_of_lt (lt_of_lt_of_le (stp_lt _ _ _ _) hK')]

lemma step_mem (K : ℕ) (hK : StpOK K) (hK2 : 2 ≤ K) (x0 : ℤ → Bool) (c : ℤ) (t S : ℕ)
    (hS : S.testBit (win K x0 c t) = true) :
    (img K (ev x0 t c).toNat S).testBit (win K x0 c (t + 1)) = true := by
  rw [win_step K hK hK2]
  exact img_mem _ _ _ _ _ (win_lt K x0 c t) (Bool.toNat_le _) hS

lemma run_mem (K : ℕ) (hK : StpOK K) (hK2 : 2 ≤ K) (x0 : ℤ → Bool) (c : ℤ) :
    ∀ (ws : List ℕ) t X, X.testBit (win K x0 c t) = true →
      (∀ i < ws.length, (ev x0 (t + i) c).toNat = ws.getD i 0) →
      (run K ws X).testBit (win K x0 c (t + ws.length)) = true := by
  intro ws
  induction ws with
  | nil => intro t X h _; simpa [run] using h
  | cons w ws ih =>
    intro t X h hw
    have h0 := hw 0 (by simp)
    simp only [add_zero, List.getD_cons_zero] at h0
    have h1 := step_mem K hK hK2 x0 c t X h
    rw [h0] at h1
    have := ih (t + 1) _ h1 (fun i hi => by
      have := hw (i + 1) (by simp; omega)
      simpa [show t + (i + 1) = t + 1 + i by ring] using this)
    simpa [run, show t + 1 + ws.length = t + (ws.length + 1) by ring] using this

lemma getD_take (ws : List ℕ) : ∀ i k, k < i → (ws.take i).getD k 0 = ws.getD k 0 := by
  induction ws with
  | nil => intro i k _; simp
  | cons w ws ih =>
    intro i k hk
    rcases i with _ | i
    · omega
    · rcases k with _ | k
      · simp
      · simp only [List.take_succ_cons, List.getD_cons_succ]; exact ih i k (by omega)

lemma ticks_spec (K : ℕ) : ∀ (ws : List ℕ) X, ticks K ws X = true →
    ∀ i < ws.length, const0 K (run K (ws.take i) X) = true := by
  intro ws
  induction ws with
  | nil => intro X _ i hi; simp at hi
  | cons w ws ih =>
    intro X h i hi
    simp only [ticks, Bool.and_eq_true] at h
    rcases i with _ | i
    · simpa [run] using h.1
    · simp only [List.take_succ_cons, run]
      exact ih _ h.2 i (by simp at hi; omega)

/-! ## Assembly -/

lemma toNat_inj' {a b : Bool} (h : a.toNat = b.toNat) : a = b := by
  cases a <;> cases b <;> simp_all

/-- Column c reads the word `ws` periodically from time `a`. -/
def ReadsW (x0 : ℤ → Bool) (c : ℤ) (ws : List ℕ) (a : ℕ) : Prop :=
  ∀ n i, i < ws.length → (ev x0 (a + n * ws.length + i) c).toNat = ws.getD i 0

/-- The determination package for a word at width K. -/
def Det (K : ℕ) (ws : List ℕ) : Prop :=
  ∃ S n0, (∀ n, n0 ≤ n → reach K ws n = S) ∧ ∀ i < ws.length, const0 K (run K (ws.take i) S) = true

lemma det_of_check (K : ℕ) (ws : List ℕ) (n0 : ℕ) (h : check K ws n0 = true) : Det K ws := by
  simp only [check, Bool.and_eq_true, beq_iff_eq] at h
  refine ⟨reach K ws n0, n0, ?_, ticks_spec K ws _ h.2⟩
  intro n hn
  induction n, hn using Nat.le_induction with
  | base => rfl
  | succ n _ ih => show run K ws (reach K ws n) = reach K ws n0; rw [ih, h.1]

lemma orbit_mem (K : ℕ) (hK : StpOK K) (hK2 : 2 ≤ K) (x0 : ℤ → Bool) (c : ℤ) (ws : List ℕ) (a : ℕ)
    (hr : ReadsW x0 c ws a) : ∀ n, (reach K ws n).testBit (win K x0 c (a + n * ws.length)) = true := by
  intro n
  induction n with
  | zero =>
    show (2 ^ (2 ^ K) - 1).testBit _ = true
    rw [Nat.testBit_two_pow_sub_one]; simpa using win_lt K x0 c (a + 0 * ws.length)
  | succ n ih =>
    have := run_mem K hK hK2 x0 c ws _ _ ih (fun i hi => hr n i hi)
    show (run K ws (reach K ws n)).testBit _ = true
    rwa [show a + n * ws.length + ws.length = a + (n + 1) * ws.length by ring] at this

/-- Column c + 1 at time a + n p + i takes, for n ≥ n0, a value depending on i alone. -/
lemma col1_eq (K : ℕ) (hK : StpOK K) (hK2 : 2 ≤ K) (x0 : ℤ → Bool) (c : ℤ) (ws : List ℕ) (a : ℕ)
    (hr : ReadsW x0 c ws a) (hd : Det K ws) : ∃ n0, ∀ n i, n0 ≤ n → i < ws.length →
      ev x0 (a + n * ws.length + i) (c + 1) = ev x0 (a + (n + 1) * ws.length + i) (c + 1) := by
  obtain ⟨S, n0, hS, ht⟩ := hd
  refine ⟨n0, fun n i hn hi => ?_⟩
  have mem : ∀ m, n0 ≤ m → (run K (ws.take i) S).testBit (win K x0 c (a + m * ws.length + i)) = true := by
    intro m hm
    have hm' := orbit_mem K hK hK2 x0 c ws a hr m
    rw [hS m hm] at hm'
    have := run_mem K hK hK2 x0 c (ws.take i) _ _ hm' (fun k hk => by
      rw [getD_take ws i k (by simp at hk; omega)]
      exact hr m k (by simp at hk; omega))
    simpa [List.length_take, Nat.min_eq_left hi.le] using this
  obtain ⟨b, hb⟩ := const0_spec K _ (ht i hi)
  have e1 := hb _ (win_lt K x0 c _) (mem n hn)
  have e2 := hb _ (win_lt K x0 c _) (mem (n + 1) (by omega))
  rw [win_bit K x0 c _ 0 (by omega)] at e1 e2
  simp only [Nat.cast_zero, add_zero] at e1 e2
  rw [e1, e2]

/-- The core: a leftmost black cell at or left of column c. -/
theorem core (K : ℕ) (hK : StpOK K) (hK2 : 2 ≤ K) (ws : List ℕ) (hd : Det K ws) (hp : 1 ≤ ws.length)
    (x0 : ℤ → Bool) (c : ℤ) (L : ℕ) (hc : x0 (c - L) = true) (hl : ∀ j < c - L, x0 j = false) (a : ℕ)
    (hr : ReadsW x0 c ws a) : False := by
  set p := ws.length with hpdef
  obtain ⟨n0, h1⟩ := col1_eq K hK hK2 x0 c ws a hr hd
  have split : ∀ t, a ≤ t → t = a + ((t - a) / p) * p + (t - a) % p := by
    intro t ht
    have := Nat.div_add_mod (t - a) p
    rw [mul_comm] at this; omega
  have hmod : ∀ t, (t - a) % p < p := fun t => Nat.mod_lt _ (by omega)
  apply no_two_periodic x0 c L hc hl p (a + n0 * p) hp
  · intro t ht
    have e1 := split t (by nlinarith)
    have h0 := hr ((t - a) / p) ((t - a) % p) (hmod t)
    have h0' := hr ((t - a) / p + 1) ((t - a) % p) (hmod t)
    rw [← h0] at h0'
    have := toNat_inj' h0'
    rw [e1, show a + (t - a) / p * p + (t - a) % p + p = a + ((t - a) / p + 1) * p + (t - a) % p by ring]
    exact this.symm
  · intro t ht
    have e1 := split t (by nlinarith)
    have hn : n0 ≤ (t - a) / p := by
      rw [Nat.le_div_iff_mul_le (by omega)]; omega
    rw [e1, show a + (t - a) / p * p + (t - a) % p + p = a + ((t - a) / p + 1) * p + (t - a) % p by ring]
    exact h1 _ _ hn (hmod t)

/-- Any leftmost black cell: re-base time when it lies right of column c. -/
theorem no_word (K : ℕ) (hK : StpOK K) (hK2 : 2 ≤ K) (ws : List ℕ) (hd : Det K ws) (hp : 1 ≤ ws.length)
    (x0 : ℤ → Bool) (e : ℤ) (he : x0 e = true) (hl : ∀ j < e, x0 j = false) (c : ℤ) (a : ℕ)
    (hr : ReadsW x0 c ws a) : False := by
  by_cases hec : e ≤ c
  · exact core K hK hK2 ws hd hp x0 c (c - e).toNat (by rwa [show c - ((c - e).toNat : ℤ) = e by omega])
      (by rw [show c - ((c - e).toNat : ℤ) = e by omega]; exact hl) a hr
  · set k : ℕ := (e - c).toNat with hk
    have E := edge x0 e he hl k
    have hkc : e - (k : ℤ) = c := by rw [hk]; omega
    rw [hkc] at E
    apply core K hK hK2 ws hd hp (ev x0 k) c 0 (by simpa using E.1) (by simpa using E.2) (a + k * ws.length - k)
    intro n i hi
    have : k ≤ k * ws.length := Nat.le_mul_of_pos_right k hp
    rw [ev_add, show k + (a + k * ws.length - k + n * ws.length + i) = a + (n + k) * ws.length + i by
      rw [add_mul]; omega]
    exact hr (n + k) i hi

/-! ## Entry 41's words -/

def words8 : List (ℕ × List ℕ) :=
  [(5, [0, 0, 1, 1, 1, 1, 1, 1, 1, 1]), (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]), (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]), (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]), (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]), (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]),
   (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1]), (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1]), (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1]),
   (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]), (4, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]),
   (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1]), (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1]), (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1]),
   (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1]), (4, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1]),
   (4, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1]), (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1]), (4, [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1]), (5, [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
   (2, [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]), (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1]), (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1]), (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1]), (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1]), (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1]),
   (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1]), (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1]),
   (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1]), (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1]), (4, [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1]), (4, [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1]),
   (2, [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]),
   (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1]),
   (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1]),
   (4, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1]),
   (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1]),
   (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1]),
   (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1]),
   (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1]),
   (4, [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1]),
   (4, [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1]),
   (5, [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1]),
   (3, [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
   (2, [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]),
   (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1]),
   (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1]),
   (4, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1]),
   (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1]),
   (6, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1]),
   (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1]),
   (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1]),
   (4, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1]),
   (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1]),
   (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1]),
   (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1]),
   (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1]),
   (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1]),
   (4, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1]),
   (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1]),
   (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1]),
   (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1]),
   (4, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1]),
   (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]),
   (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1]),
   (2, [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1]),
   (3, [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1]),
   (6, [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]),
   (3, [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
   (4, [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
   (3, [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]),
   (2, [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
   (5, [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]),
   (5, [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
   (2, [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])]

def words10 : List (ℕ × List ℕ) :=
  [(5, [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]), (5, [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]),
   (4, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1]), (4, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1]),
   (5, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1]), (4, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]),
   (4, [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1]), (6, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1]),
   (4, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]), (3, [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1])]

-- One kernel check per word (with Elab.async off, memory stays near one check's).
set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_0 : check 8 [0, 0, 1, 1, 1, 1, 1, 1, 1, 1] 5 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_1 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_2 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_3 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_4 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_5 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_6 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_7 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_8 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_9 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_10 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_11 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_12 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_13 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_14 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_15 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1] 4 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_16 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_17 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_18 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_19 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_20 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_21 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1] 4 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_22 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1] 4 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_23 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_24 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_25 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1] 4 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_26 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_27 : check 8 [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 5 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_28 : check 8 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_29 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_30 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_31 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_32 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_33 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_34 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_35 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_36 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_37 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_38 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_39 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_40 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_41 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_42 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_43 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_44 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_45 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1] 4 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_46 : check 8 [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_47 : check 8 [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1] 4 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_48 : check 8 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_49 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_50 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_51 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_52 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_53 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_54 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_55 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_56 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_57 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1] 4 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_58 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_59 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_60 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_61 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_62 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_63 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_64 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_65 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_66 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_67 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_68 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_69 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_70 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_71 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1] 4 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_72 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1] 4 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_73 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_74 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_75 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_76 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_77 : check 8 [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1] 5 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_78 : check 8 [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_79 : check 8 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_80 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_81 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_82 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_83 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_84 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_85 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_86 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_87 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_88 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1] 4 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_89 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_90 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1] 6 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_91 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_92 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_93 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_94 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_95 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1] 4 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_96 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_97 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_98 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_99 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_100 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_101 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_102 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_103 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_104 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_105 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_106 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_107 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1] 4 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_108 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_109 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_110 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_111 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_112 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_113 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_114 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1] 4 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_115 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_116 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_117 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_118 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_119 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_120 : check 8 [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_121 : check 8 [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1] 6 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_122 : check 8 [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_123 : check 8 [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 4 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_124 : check 8 [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_125 : check 8 [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_126 : check 8 [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1] 5 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_127 : check 8 [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 5 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_128 : check 8 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w10_0 : check 10 [0, 0, 0, 0, 0, 0, 0, 0, 1, 1] 5 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w10_1 : check 10 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1] 5 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w10_2 : check 10 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1] 4 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w10_3 : check 10 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1] 4 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w10_4 : check 10 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1] 5 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w10_5 : check 10 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1] 4 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w10_6 : check 10 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1] 4 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w10_7 : check 10 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1] 6 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w10_8 : check 10 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1] 4 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w10_9 : check 10 [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1] 3 = true := by decide +kernel

lemma checks8 : (words8.all fun e => check 8 e.2 e.1) = true := by
  simp only [words8, List.all_cons, List.all_nil, Bool.and_true,
    w8_0, w8_1, w8_2, w8_3, w8_4, w8_5, w8_6, w8_7, w8_8, w8_9, w8_10, w8_11, w8_12, w8_13, w8_14, w8_15, w8_16,
    w8_17, w8_18, w8_19, w8_20, w8_21, w8_22, w8_23, w8_24, w8_25, w8_26, w8_27, w8_28, w8_29, w8_30, w8_31,
    w8_32, w8_33, w8_34, w8_35, w8_36, w8_37, w8_38, w8_39, w8_40, w8_41, w8_42, w8_43, w8_44, w8_45, w8_46,
    w8_47, w8_48, w8_49, w8_50, w8_51, w8_52, w8_53, w8_54, w8_55, w8_56, w8_57, w8_58, w8_59, w8_60, w8_61,
    w8_62, w8_63, w8_64, w8_65, w8_66, w8_67, w8_68, w8_69, w8_70, w8_71, w8_72, w8_73, w8_74, w8_75, w8_76,
    w8_77, w8_78, w8_79, w8_80, w8_81, w8_82, w8_83, w8_84, w8_85, w8_86, w8_87, w8_88, w8_89, w8_90, w8_91,
    w8_92, w8_93, w8_94, w8_95, w8_96, w8_97, w8_98, w8_99, w8_100, w8_101, w8_102, w8_103, w8_104, w8_105,
    w8_106, w8_107, w8_108, w8_109, w8_110, w8_111, w8_112, w8_113, w8_114, w8_115, w8_116, w8_117, w8_118,
    w8_119, w8_120, w8_121, w8_122, w8_123, w8_124, w8_125, w8_126, w8_127, w8_128]

lemma checks10 : (words10.all fun e => check 10 e.2 e.1) = true := by
  simp only [words10, List.all_cons, List.all_nil, Bool.and_true,
    w10_0, w10_1, w10_2, w10_3, w10_4, w10_5, w10_6, w10_7, w10_8, w10_9]

set_option maxRecDepth 100000 in
lemma counts : words8.length = 129 ∧ words10.length = 10 := by decide

set_option maxRecDepth 100000 in
lemma nonempty : ∀ e ∈ words8 ++ words10, 1 ≤ e.2.length := by decide

/-- Entry 41: no configuration with a leftmost black cell has a column reading any of the 139 words periodically. -/
theorem entry41 (ws : List ℕ) (hw : ws ∈ (words8 ++ words10).map Prod.snd) (x0 : ℤ → Bool) (e : ℤ)
    (he : x0 e = true) (hl : ∀ j < e, x0 j = false) (c : ℤ) (a : ℕ) (hr : ReadsW x0 c ws a) : False := by
  simp only [List.map_append, List.mem_append, List.mem_map] at hw
  rcases hw with ⟨⟨n0, ws'⟩, hm, rfl⟩ | ⟨⟨n0, ws'⟩, hm, rfl⟩
  · have hc := List.all_eq_true.mp checks8 _ hm
    have hp : 1 ≤ ws'.length := nonempty _ (List.mem_append_left _ hm)
    exact no_word 8 stpOK8 (by norm_num) ws' (det_of_check 8 ws' n0 hc) hp x0 e he hl c a hr
  · have hc := List.all_eq_true.mp checks10 _ hm
    have hp : 1 ≤ ws'.length := nonempty _ (List.mem_append_right _ hm)
    exact no_word 10 stpOK10 (by norm_num) ws' (det_of_check 10 ws' n0 hc) hp x0 e he hl c a hr

/-! ## The black end 0 1^m, every m ≥ 14 -/

def wordB (m : ℕ) : List ℕ := 0 :: List.replicate m 1

def Bp (K : ℕ) : ℕ → ℕ → ℕ
  | 0, X => X
  | j + 1, X => img K 1 (Bp K j X)

lemma Bp_succ' (K m X : ℕ) : Bp K (m + 1) X = Bp K m (img K 1 X) := by
  induction m generalizing X with
  | zero => rfl
  | succ m ih => show img K 1 (Bp K (m + 1) X) = img K 1 (Bp K m (img K 1 X)); rw [ih]

lemma run_rep (K : ℕ) : ∀ m X, run K (List.replicate m 1) X = Bp K m X := by
  intro m
  induction m with
  | zero => intro X; rfl
  | succ m ih => intro X; rw [List.replicate_succ, run, ih, Bp_succ']

lemma Bp_add (K a b X : ℕ) : Bp K (a + b) X = Bp K a (Bp K b X) := by
  induction a with
  | zero => simp [Bp]
  | succ a ih => rw [show a + 1 + b = (a + b) + 1 by ring]; show img K 1 (Bp K (a + b) X) = img K 1 (Bp K a (Bp K b X)); rw [ih]

lemma Bp_period (K X : ℕ) (h : Bp K 24 X = Bp K 20 X) : ∀ j, 20 ≤ j → Bp K j X = Bp K (20 + (j - 20) % 4) X := by
  intro j
  induction j using Nat.strong_induction_on with
  | _ j ih =>
    intro hj
    by_cases h24 : j < 24
    · congr 1; omega
    · have e1 : Bp K j X = Bp K (j - 4) X := by
        rw [show j = (j - 24) + 24 by omega, Bp_add, h, ← Bp_add]; congr 1
      rw [e1, ih (j - 4) (by omega) (by omega)]; congr 1; omega

def checkB (m : ℕ) : Bool := check 8 (wordB m) 2

def repB (m : ℕ) : Bool :=
  (List.range 3).all (fun n => Bp 8 24 (img 8 0 (reach 8 (wordB m) n)) == Bp 8 20 (img 8 0 (reach 8 (wordB m) n))) &&
  ticks 8 (wordB 24) (reach 8 (wordB m) 2)

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma cB14 : checkB 14 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma cB15 : checkB 15 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma cB16 : checkB 16 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma cB17 : checkB 17 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma cB18 : checkB 18 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma cB19 : checkB 19 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma cB20 : checkB 20 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma cB21 : checkB 21 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma cB22 : checkB 22 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma cB23 : checkB 23 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma rB20 : repB 20 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma rB21 : repB 21 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma rB22 : repB 22 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma rB23 : repB 23 = true := by decide +kernel

lemma checksB (m : ℕ) (h1 : 14 ≤ m) (h2 : m ≤ 23) : checkB m = true := by
  interval_cases m
  exacts [cB14, cB15, cB16, cB17, cB18, cB19, cB20, cB21, cB22, cB23]

lemma repsB (m : ℕ) (h1 : 20 ≤ m) (h2 : m ≤ 23) : repB m = true := by
  interval_cases m
  exacts [rB20, rB21, rB22, rB23]

lemma run_wordB (m X : ℕ) : run 8 (wordB m) X = Bp 8 m (img 8 0 X) := by
  simp only [wordB, run, run_rep]

lemma take_wordB (m i : ℕ) (hi : 1 ≤ i) : (wordB m).take i = wordB (min (i - 1) m) := by
  obtain ⟨i, rfl⟩ : ∃ i', i = i' + 1 := ⟨i - 1, by omega⟩
  simp [wordB, List.take_succ_cons, List.take_replicate]

lemma det_black (m : ℕ) (hm : 14 ≤ m) : Det 8 (wordB m) := by
  by_cases hsmall : m ≤ 23
  · exact det_of_check 8 _ 2 (checksB m hm hsmall)
  · set m' := 20 + (m - 20) % 4 with hm'
    have hr := repsB m' (by omega) (by omega)
    have hc := checksB m' (by omega) (by omega)
    simp only [repB, Bool.and_eq_true, List.all_eq_true, List.mem_range, beq_iff_eq] at hr
    obtain ⟨hW, ht⟩ := hr
    simp only [checkB, check, Bool.and_eq_true, beq_iff_eq] at hc
    obtain ⟨hfix, _⟩ := hc
    have hmac : ∀ n < 3, run 8 (wordB m) (reach 8 (wordB m') n) = run 8 (wordB m') (reach 8 (wordB m') n) := by
      intro n hn
      rw [run_wordB, run_wordB, Bp_period _ _ (hW n hn) m (by omega)]
    have heq : ∀ n ≤ 2, reach 8 (wordB m) n = reach 8 (wordB m') n := by
      intro n hn
      induction n with
      | zero => rfl
      | succ n ih => show run 8 _ (reach 8 _ n) = run 8 _ (reach 8 _ n); rw [ih (by omega), hmac n (by omega)]
    refine ⟨reach 8 (wordB m') 2, 2, ?_, ?_⟩
    · intro n hn
      induction n, hn using Nat.le_induction with
      | base => exact heq 2 le_rfl
      | succ n _ ih => show run 8 _ (reach 8 _ n) = _; rw [ih, hmac 2 (by norm_num), hfix]
    · intro i hi
      have hts := ticks_spec 8 (wordB 24) _ ht
      rcases Nat.eq_zero_or_pos i with h0 | h0
      · subst h0; simpa using hts 0 (by simp [wordB])
      · rw [take_wordB m i h0, run_wordB]
        simp only [wordB, List.length_cons, List.length_replicate] at hi
        rw [show min (i - 1) m = i - 1 by omega]
        by_cases h24 : i - 1 < 24
        · have := hts i (by simp [wordB]; omega)
          rwa [take_wordB 24 i h0, run_wordB, show min (i - 1) 24 = i - 1 by omega] at this
        · rw [Bp_period _ _ (hW 2 (by norm_num)) (i - 1) (by omega)]
          have := hts (21 + (i - 1 - 20) % 4) (by simp [wordB]; omega)
          rwa [take_wordB 24 _ (by omega), run_wordB,
            show min (21 + (i - 1 - 20) % 4 - 1) 24 = 20 + (i - 1 - 20) % 4 by omega] at this

/-- The black end: no configuration with a leftmost black cell has a column reading 0 1^m periodically, m ≥ 14. -/
theorem black_end (m : ℕ) (hm : 14 ≤ m) (x0 : ℤ → Bool) (e : ℤ) (he : x0 e = true) (hl : ∀ j < e, x0 j = false)
    (c : ℤ) (a : ℕ) (hr : ReadsW x0 c (wordB m) a) : False :=
  no_word 8 stpOK8 (by norm_num) (wordB m) (det_black m hm) (by simp [wordB]) x0 e he hl c a hr

end JenRoute

#print axioms JenRoute.entry41
#print axioms JenRoute.black_end
