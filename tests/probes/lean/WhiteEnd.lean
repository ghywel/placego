import Mathlib

/-!
# Entry 40: no finite nonzero seed has a column that eventually reads 1 0^q, for any q ≥ 10 (Local, 2026-10-09)

PROOFS.md entry 40 (the Condrey white end), machine-checked. The route (L498, second-read by Cloud in CL110 and GPT in
GC880): the eight cells right of the column, with any bit beyond them, are a finite relaxation. From any start, after
three periods of the word 1 0^q their state lies in a stable set S, on which cell +1 is determined at every tick. So
column c + 1 is eventually periodic with period q + 1, and Theorem A (entry 5, TheoremA.lean) forbids two adjacent
eventually periodic columns when there is a leftmost black cell.

The finite part is checked by `decide`. States are numbers below 256 (bit j is cell c + 1 + j), sets of states are
256-bit numbers. Words q = 10 .. 25 are checked one by one. For q ≥ 26 the white relation repeats with period 4:
W^26 = W^22 on the sets that occur, so q behaves as 22 + (q - 22) % 4.

How to check: as for TheoremA.lean; the `#print axioms` lines must list no `sorryAx` (here: propext,
Classical.choice, Quot.sound). About 32 s on the M5, most of it the kernel `decide`s (`decide +kernel` adds no axiom).
Memory: `Elab.async false` and one kernel check per declaration keep the peak near one check's (about 0.8 GB above
Mathlib's mapped files, about 6.5 GB resident in all); the first version, one big check run in parallel, peaked at 10.6 GB.
Control: `control_q9` shows the finite check fails at q = 9, so it is not vacuous.
Statement scope: `white_end` needs only a leftmost black cell; `white_end_finite` assumes a left bound and one black
cell. `Reads x0 c q a` says column c reads 1 0^q periodically from time a, the 1 first (any phase of an eventually
periodic column with that word has such an a). The time re-basing of entry 40's step 4 is `white_end`'s second case.
-/

-- Sequential elaboration: the kernel checks below would otherwise run in parallel and stack their memory.
set_option Elab.async false

namespace WhiteEnd

/-! ## Rule 30 and Theorem A (verbatim from TheoremA.lean) -/

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

/-! ## The finite relaxation on eight cells -/

/-- One step of the eight cells: state bit j is cell c + 1 + j, `w` the column's bit, `u` the cell beyond. -/
def stp (w s u : ℕ) : ℕ := ((((s <<< 1) ||| w) &&& 255) ^^^ (s ||| ((s >>> 1) ||| (u <<< 7)))) &&& 255

def imgAux (w S n : ℕ) : ℕ → ℕ :=
  Nat.rec (motive := fun _ => ℕ → ℕ) (fun acc => acc)
    (fun k ih acc => ih (if S.testBit k then acc ||| (1 <<< stp w k 0) ||| (1 <<< stp w k 1) else acc)) n

lemma imgAux_succ (w S n acc : ℕ) : imgAux w S (n + 1) acc =
    imgAux w S n (if S.testBit n then acc ||| (1 <<< stp w n 0) ||| (1 <<< stp w n 1) else acc) := rfl

/-- The image of the set `S` (a 256-bit number) under one step with column bit `w` and every outside bit. -/
def img (w S : ℕ) : ℕ := imgAux w S 256 0

/-- `Wp j S`: `j` white steps. -/
def Wp : ℕ → ℕ → ℕ
  | 0, S => S
  | j + 1, S => img 0 (Wp j S)

/-- One period of the word 1 0^q: a black step, then `q` white steps. -/
def mac (q S : ℕ) : ℕ := Wp q (img 1 S)

def reach (q : ℕ) : ℕ → ℕ
  | 0 => 2 ^ 256 - 1
  | n + 1 => mac q (reach q n)

/-- Every state in `S` has cell c + 1 equal to `b`. -/
def bit0Const (S : ℕ) (b : Bool) : Bool := (List.range 256).all fun s => !(S.testBit s) || (s.testBit 0 == b)

def ticksAux : ℕ → ℕ → ℕ → Bool
  | 0, _, _ => true
  | r + 1, j, X => bit0Const X (decide (2 ≤ j)) && ticksAux r (j + 1) (img 0 X)

/-- Cell c + 1 at the `q` ticks after the black one: 0, 0, then 1. -/
def ticksOK (q S : ℕ) : Bool := ticksAux q 0 (img 1 S)

def checkQ (q : ℕ) : Bool :=
  mac q (reach q 3) == reach q 3 && bit0Const (reach q 3) true && ticksOK q (reach q 3)

def repOK (q : ℕ) : Bool :=
  (List.range 4).all (fun n => Wp 26 (img 1 (reach q n)) == Wp 22 (img 1 (reach q n))) && ticksOK 26 (reach q 3)

-- The finite facts, one kernel check per word length (with Elab.async off, memory stays near one check's).
set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check10 : checkQ 10 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check11 : checkQ 11 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check12 : checkQ 12 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check13 : checkQ 13 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check14 : checkQ 14 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check15 : checkQ 15 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check16 : checkQ 16 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check17 : checkQ 17 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check18 : checkQ 18 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check19 : checkQ 19 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check20 : checkQ 20 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check21 : checkQ 21 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check22 : checkQ 22 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check23 : checkQ 23 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check24 : checkQ 24 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check25 : checkQ 25 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma rep22 : repOK 22 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma rep23 : repOK 23 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma rep24 : repOK 24 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma rep25 : repOK 25 = true := by decide +kernel

lemma checks (q : ℕ) (h1 : 10 ≤ q) (h2 : q ≤ 25) : checkQ q = true := by
  interval_cases q
  exacts [check10, check11, check12, check13, check14, check15, check16, check17, check18, check19, check20,
    check21, check22, check23, check24, check25]

lemma reps (q : ℕ) (h1 : 22 ≤ q) (h2 : q ≤ 25) : repOK q = true := by
  interval_cases q
  exacts [rep22, rep23, rep24, rep25]

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
/-- Control: the check is not vacuous; it fails at q = 9, where width 8 does not determine cell c + 1 (L498). -/
lemma control_q9 : checkQ 9 = false := by decide +kernel

set_option maxRecDepth 100000 in
lemma stp_bits : ∀ s < 256, ∀ w u : Bool, ∀ j < 8,
    (stp w.toNat s u.toNat).testBit j =
      xor (if j = 0 then w else s.testBit (j - 1)) (s.testBit j || if j = 7 then u else s.testBit (j + 1)) := by
  decide

lemma stp_lt (w s u : ℕ) : stp w s u < 256 := by
  unfold stp; exact lt_of_le_of_lt Nat.and_le_right (by norm_num)

/-! ## Sets: membership -/

lemma testBit_shift_self (k : ℕ) : (1 <<< k).testBit k = true := by
  rw [Nat.one_shiftLeft]; exact Nat.testBit_two_pow_self

lemma imgAux_acc (w S : ℕ) : ∀ n acc y, acc.testBit y = true → (imgAux w S n acc).testBit y = true := by
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

lemma imgAux_mem (w S u : ℕ) (hu : u ≤ 1) :
    ∀ n acc s, s < n → S.testBit s = true → (imgAux w S n acc).testBit (stp w s u) = true := by
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

lemma img_mem (w S s u : ℕ) (hs : s < 256) (hu : u ≤ 1) (hS : S.testBit s = true) :
    (img w S).testBit (stp w s u) = true :=
  imgAux_mem w S u hu 256 0 s hs hS

lemma Wp_succ' (j X : ℕ) : Wp (j + 1) X = Wp j (img 0 X) := by
  induction j generalizing X with
  | zero => rfl
  | succ j ih => show img 0 (Wp (j + 1) X) = img 0 (Wp j (img 0 X)); rw [ih]

lemma Wp_add (a b X : ℕ) : Wp (a + b) X = Wp a (Wp b X) := by
  induction a with
  | zero => simp [Wp]
  | succ a ih => rw [show a + 1 + b = (a + b) + 1 by ring]; show img 0 (Wp (a + b) X) = img 0 (Wp a (Wp b X)); rw [ih]

lemma Wp_period (X : ℕ) (h : Wp 26 X = Wp 22 X) : ∀ j, 22 ≤ j → Wp j X = Wp (22 + (j - 22) % 4) X := by
  intro j
  induction j using Nat.strong_induction_on with
  | _ j ih =>
    intro hj
    by_cases h26 : j < 26
    · congr 1; omega
    · have e1 : Wp j X = Wp (j - 4) X := by
        rw [show j = (j - 26) + 26 by omega, Wp_add, h, ← Wp_add]; congr 1
      rw [e1, ih (j - 4) (by omega) (by omega)]; congr 1; omega

lemma ticksAux_spec : ∀ r j X, ticksAux r j X = true → ∀ i < r, bit0Const (Wp i X) (decide (2 ≤ j + i)) = true := by
  intro r
  induction r with
  | zero => intro j X _ i hi; omega
  | succ r ih =>
    intro j X h i hi
    simp only [ticksAux, Bool.and_eq_true] at h
    rcases i with _ | i
    · simpa [Wp] using h.1
    · have := ih (j + 1) (img 0 X) h.2 i (by omega)
      rw [Wp_succ']; simpa [show j + 1 + i = j + (i + 1) by ring] using this

lemma bit0Const_spec (S : ℕ) (b : Bool) (h : bit0Const S b = true) (s : ℕ) (hs : s < 256) (hS : S.testBit s = true) :
    s.testBit 0 = b := by
  simp only [bit0Const, List.all_eq_true, List.mem_range] at h
  have := h s hs
  rw [hS, Bool.not_true, Bool.false_or, beq_iff_eq] at this
  exact this

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

def win (x0 : ℤ → Bool) (c : ℤ) (t : ℕ) : ℕ := enc (fun j => ev x0 t (c + 1 + j)) 8

lemma win_lt (x0 : ℤ → Bool) (c : ℤ) (t : ℕ) : win x0 c t < 256 := enc_lt _ 8

lemma win_bit (x0 : ℤ → Bool) (c : ℤ) (t j : ℕ) (hj : j < 8) : (win x0 c t).testBit j = ev x0 t (c + 1 + j) := by
  simp [win, enc_testBit, hj]

lemma win_step (x0 : ℤ → Bool) (c : ℤ) (t : ℕ) :
    win x0 c (t + 1) = stp (ev x0 t c).toNat (win x0 c t) (ev x0 t (c + 9)).toNat := by
  apply Nat.eq_of_testBit_eq
  intro j
  by_cases hj : j < 8
  · rw [win_bit x0 c (t + 1) j hj, stp_bits _ (win_lt x0 c t) _ _ j hj]
    show xor (ev x0 t (c + 1 + j - 1)) (ev x0 t (c + 1 + j) || ev x0 t (c + 1 + j + 1)) = _
    rw [win_bit x0 c t j hj]
    congr 1
    · split_ifs with h0
      · subst h0; congr 1; ring
      · rw [win_bit x0 c t (j - 1) (by omega)]; congr 1; push_cast [show 1 ≤ j by omega]; ring
    · congr 1
      split_ifs with h7
      · subst h7; congr 1; ring
      · rw [win_bit x0 c t (j + 1) (by omega)]; congr 1; push_cast; ring
  · have h256 : 256 ≤ 2 ^ j := by
      calc 256 = 2 ^ 8 := by norm_num
        _ ≤ 2 ^ j := Nat.pow_le_pow_right (by norm_num) (by omega)
    rw [Nat.testBit_eq_false_of_lt (lt_of_lt_of_le (win_lt x0 c (t + 1)) h256),
      Nat.testBit_eq_false_of_lt (lt_of_lt_of_le (stp_lt _ _ _) h256)]

lemma step_mem (x0 : ℤ → Bool) (c : ℤ) (t : ℕ) (S : ℕ) (hS : S.testBit (win x0 c t) = true) :
    (img (ev x0 t c).toNat S).testBit (win x0 c (t + 1)) = true := by
  rw [win_step]
  exact img_mem _ _ _ _ (win_lt x0 c t) (Bool.toNat_le _) hS

lemma Wp_mem (x0 : ℤ → Bool) (c : ℤ) : ∀ i t X, X.testBit (win x0 c t) = true →
    (∀ k < i, ev x0 (t + k) c = false) → (Wp i X).testBit (win x0 c (t + i)) = true := by
  intro i
  induction i with
  | zero => intro t X h _; simpa [Wp] using h
  | succ i ih =>
    intro t X h hw
    have := step_mem x0 c (t + i) (Wp i X) (ih t X h (fun k hk => hw k (by omega)))
    rw [hw i (by omega)] at this
    simpa [Wp, show t + (i + 1) = t + i + 1 by ring] using this

/-! ## Assembly -/

/-- The column reads 1 0^q from time `a`, the 1 first. -/
def Reads (x0 : ℤ → Bool) (c : ℤ) (q a : ℕ) : Prop :=
  ∀ n : ℕ, ev x0 (a + n * (q + 1)) c = true ∧ ∀ k, 1 ≤ k → k ≤ q → ev x0 (a + n * (q + 1) + k) c = false

/-- The determination package for a word length `q`. -/
def Det (q : ℕ) : Prop :=
  ∃ S, (∀ n, 3 ≤ n → reach q n = S) ∧ bit0Const S true = true ∧
    ∀ i < q, bit0Const (Wp i (img 1 S)) (decide (2 ≤ i)) = true

lemma det_small (q : ℕ) (h1 : 10 ≤ q) (h2 : q ≤ 25) : Det q := by
  have hc : checkQ q = true := checks q h1 h2
  simp only [checkQ, Bool.and_eq_true, beq_iff_eq] at hc
  obtain ⟨⟨hfix, hb⟩, ht⟩ := hc
  refine ⟨reach q 3, ?_, hb, ?_⟩
  · intro n hn
    induction n, hn using Nat.le_induction with
    | base => rfl
    | succ n _ ih => show mac q (reach q n) = reach q 3; rw [ih, hfix]
  · intro i hi; simpa using ticksAux_spec q 0 _ ht i hi

lemma det_large (q : ℕ) (hq : 26 ≤ q) : Det q := by
  set q' := 22 + (q - 22) % 4 with hq'
  have hr : repOK q' = true := reps q' (by omega) (by omega)
  have hc' : checkQ q' = true := checks q' (by omega) (by omega)
  simp only [repOK, Bool.and_eq_true, List.all_eq_true, List.mem_range, beq_iff_eq] at hr
  obtain ⟨hW, ht⟩ := hr
  simp only [checkQ, Bool.and_eq_true, beq_iff_eq] at hc'
  obtain ⟨⟨hfix, hb⟩, _⟩ := hc'
  have hmac : ∀ n < 4, mac q (reach q' n) = mac q' (reach q' n) := by
    intro n hn
    unfold mac
    rw [Wp_period _ (hW n hn) q (by omega), show 22 + (q - 22) % 4 = q' from rfl]
  have heq : ∀ n ≤ 3, reach q n = reach q' n := by
    intro n hn
    induction n with
    | zero => rfl
    | succ n ih => show mac q (reach q n) = mac q' (reach q' n); rw [ih (by omega), hmac n (by omega)]
  refine ⟨reach q' 3, ?_, hb, ?_⟩
  · intro n hn
    induction n, hn using Nat.le_induction with
    | base => exact heq 3 le_rfl
    | succ n _ ih => show mac q (reach q n) = reach q' 3; rw [ih, hmac 3 (by norm_num), hfix]
  · intro i hi
    have hts := ticksAux_spec 26 0 _ ht
    by_cases h26 : i < 26
    · simpa using hts i h26
    · rw [Wp_period _ (hW 3 (by norm_num)) i (by omega)]
      have := hts (22 + (i - 22) % 4) (by omega)
      simpa [show 2 ≤ i by omega, show 2 ≤ 22 + (i - 22) % 4 by omega] using this

lemma det (q : ℕ) (hq : 10 ≤ q) : Det q := by
  by_cases h : q ≤ 25
  · exact det_small q hq h
  · exact det_large q (by omega)

/-- With the column reading 1 0^q from `a`, the window lies in `reach q n` at each black tick. -/
lemma orbit_mem (x0 : ℤ → Bool) (c : ℤ) (q a : ℕ) (hr : Reads x0 c q a) :
    ∀ n, (reach q n).testBit (win x0 c (a + n * (q + 1))) = true := by
  intro n
  induction n with
  | zero =>
    show (2 ^ 256 - 1).testBit _ = true
    rw [Nat.testBit_two_pow_sub_one]; simpa using win_lt x0 c (a + 0 * (q + 1))
  | succ n ih =>
    have h1 := step_mem x0 c (a + n * (q + 1)) _ ih
    rw [(hr n).1] at h1
    have h2 := Wp_mem x0 c q (a + n * (q + 1) + 1) _ h1 (fun k hk => by
      have := (hr n).2 (k + 1) (by omega) (by omega)
      rwa [show a + n * (q + 1) + (k + 1) = a + n * (q + 1) + 1 + k by ring] at this)
    show (mac q (reach q n)).testBit _ = true
    unfold mac
    rwa [show a + n * (q + 1) + 1 + q = a + (n + 1) * (q + 1) by ring] at h2

/-- Column c + 1 at time a + n (q + 1) + i, for n ≥ 3 and i ≤ q, is 1 0 0 1 1 ... by position. -/
lemma col1 (x0 : ℤ → Bool) (c : ℤ) (q a : ℕ) (hq : 10 ≤ q) (hr : Reads x0 c q a) (n i : ℕ) (hn : 3 ≤ n)
    (hi : i ≤ q) : ev x0 (a + n * (q + 1) + i) (c + 1) = (i == 0 || decide (3 ≤ i)) := by
  obtain ⟨S, hS, hb, ht⟩ := det q hq
  have hm := orbit_mem x0 c q a hr n
  rw [hS n hn] at hm
  rcases i with _ | i
  · have := bit0Const_spec S true hb _ (win_lt x0 c _) hm
    rw [win_bit x0 c _ 0 (by norm_num)] at this
    simpa using this
  · have h1 := step_mem x0 c (a + n * (q + 1)) S hm
    rw [(hr n).1] at h1
    have h2 := Wp_mem x0 c i (a + n * (q + 1) + 1) _ h1 (fun k hk => by
      have := (hr n).2 (k + 1) (by omega) (by omega)
      rwa [show a + n * (q + 1) + (k + 1) = a + n * (q + 1) + 1 + k by ring] at this)
    have := bit0Const_spec _ _ (ht i (by omega)) _ (win_lt x0 c _) h2
    rw [win_bit x0 c _ 0 (by norm_num)] at this
    simp only [Nat.cast_zero, add_zero] at this
    rw [show a + n * (q + 1) + (i + 1) = a + n * (q + 1) + 1 + i by ring, this]
    by_cases h : 2 ≤ i <;> simp [h]

/-- The core: a leftmost black cell at or left of column c. -/
theorem core (x0 : ℤ → Bool) (c : ℤ) (L : ℕ) (hc : x0 (c - L) = true) (hl : ∀ j < c - L, x0 j = false)
    (q a : ℕ) (hq : 10 ≤ q) (hr : Reads x0 c q a) : False := by
  have split : ∀ t, a ≤ t → t = a + ((t - a) / (q + 1)) * (q + 1) + (t - a) % (q + 1) := by
    intro t ht
    have := Nat.div_add_mod (t - a) (q + 1)
    rw [mul_comm] at this; omega
  have hmod : ∀ t, (t - a) % (q + 1) ≤ q := fun t => Nat.lt_succ_iff.mp (Nat.mod_lt _ (by omega))
  apply no_two_periodic x0 c L hc hl (q + 1) (a + 3 * (q + 1)) (by omega)
  · intro t ht
    have e1 := split t (by omega)
    have e2 : t + (q + 1) = a + ((t - a) / (q + 1) + 1) * (q + 1) + (t - a) % (q + 1) := by
      rw [add_mul, one_mul]; omega
    have col0 : ∀ n i, i ≤ q → ev x0 (a + n * (q + 1) + i) c = (i == 0) := by
      intro n i hi
      rcases i with _ | i
      · simpa using (hr n).1
      · simpa using (hr n).2 (i + 1) (by omega) hi
    rw [e1, col0 _ _ (hmod t)]
    rw [show a + (t - a) / (q + 1) * (q + 1) + (t - a) % (q + 1) + (q + 1) =
      a + ((t - a) / (q + 1) + 1) * (q + 1) + (t - a) % (q + 1) by ring, col0 _ _ (hmod t)]
  · intro t ht
    have e1 := split t (by omega)
    have hn : 3 ≤ (t - a) / (q + 1) := by
      rw [Nat.le_div_iff_mul_le (by omega)]; omega
    rw [e1, col1 x0 c q a hq hr _ _ hn (hmod t)]
    rw [show a + (t - a) / (q + 1) * (q + 1) + (t - a) % (q + 1) + (q + 1) =
      a + ((t - a) / (q + 1) + 1) * (q + 1) + (t - a) % (q + 1) by ring, col1 x0 c q a hq hr _ _ (by omega) (hmod t)]

/-- Entry 40: no configuration with a leftmost black cell has a column that reads 1 0^q from some time on (q ≥ 10). -/
theorem white_end (x0 : ℤ → Bool) (e : ℤ) (he : x0 e = true) (hl : ∀ j < e, x0 j = false) (c : ℤ) (q a : ℕ)
    (hq : 10 ≤ q) (hr : Reads x0 c q a) : False := by
  by_cases hec : e ≤ c
  · exact core x0 c (c - e).toNat (by rwa [show c - ((c - e).toNat : ℤ) = e by omega])
      (by rw [show c - ((c - e).toNat : ℤ) = e by omega]; exact hl) q a hq hr
  · -- rebase time: after k = e - c steps the leftmost black cell is at c
    set k : ℕ := (e - c).toNat with hk
    have E := edge x0 e he hl k
    have hkc : e - (k : ℤ) = c := by rw [hk]; omega
    rw [hkc] at E
    apply core (ev x0 k) c 0 (by simpa using E.1) (by simpa using E.2) q (a + k * (q + 1) - k) hq
    intro n
    have ha : k + (a + k * (q + 1) - k + n * (q + 1)) = a + (n + k) * (q + 1) := by
      have : k ≤ k * (q + 1) := Nat.le_mul_of_pos_right k (by omega)
      rw [add_mul]; omega
    refine ⟨?_, fun j h1 h2 => ?_⟩
    · rw [ev_add, ha]; exact (hr (n + k)).1
    · rw [ev_add, show k + (a + k * (q + 1) - k + n * (q + 1) + j) =
        (k + (a + k * (q + 1) - k + n * (q + 1))) + j by ring, ha]
      exact (hr (n + k)).2 j h1 h2

/-- For a finite nonzero seed. -/
theorem white_end_finite (x0 : ℤ → Bool) (hfin : ∃ M : ℤ, ∀ j < M, x0 j = false) (hnz : ∃ j, x0 j = true)
    (c : ℤ) (q : ℕ) (hq : 10 ≤ q) : ¬ ∃ a, Reads x0 c q a := by
  rintro ⟨a, hr⟩
  obtain ⟨M, hM⟩ := hfin
  obtain ⟨e, he, hmin⟩ := Int.exists_least_of_bdd (P := fun j => x0 j = true)
    ⟨M, fun z hz => by by_contra h; push Not at h; rw [hM z h] at hz; exact absurd hz (by decide)⟩ hnz
  exact white_end x0 e he (fun j hj => by
    by_contra h
    have := hmin j (by simpa using h)
    omega) c q a hq hr

end WhiteEnd

#print axioms WhiteEnd.white_end
#print axioms WhiteEnd.white_end_finite
