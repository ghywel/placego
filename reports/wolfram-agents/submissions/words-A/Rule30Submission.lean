import Rule30PrizeKit
import Mathlib

/-!
# Excluded column words of length 11 to 16, beyond the kit's table

**Partial result for Problem 1.** 48 words of length 11 to 16 (41 at strip width 8, 7 at width 10), none in the kit's certificate table. For each word `w` listed below, the center column of the
single-seed pattern is not eventually `w` repeated (the kit's `EventuallyWord w` is false), and no column of any
configuration with a leftmost black cell reads `w` periodically from any time on.

**What is new.** The kit's `Rule30StripCertificateTable` excludes 30 words of length 8 to 13; none of the words
below is among them. (Eleven other words of our list are, and are left out here.)

**The argument** is the one of the white-end submission, word by word: the `K` cells right of the column (`K = 8`,
or `10` for a few words) with an arbitrary cell beyond them form a finite relaxation; after `n0` periods of the word
one more period maps its reachable set into itself while the first cell of the strip takes a single value at
every tick (`check K ws n0`, decided by the kernel); so columns `c` and `c + 1` are both periodic, which Jen's theorem with a clock forbids in a
configuration with a leftmost black cell. The words are least rotations; any rotation is the same column word.

**Provenance.** Entry 41 of the Wolfram · Collatz · Mahler record (github.com/ghywel/placego, PROOFS.md), computed
twice with separate code (Local, Cloud) and machine-checked by Local on 2026-10-10 (`tests/probes/lean/JenRoute.lean`),
restated here on the kit's `evol` and `cell` with the bridge to `EventuallyWord`. Mechanism: E. Jen, J. Stat. Phys.
43 (1986). Not a solution of Problem 1; nothing is claimed for any word not listed.
-/

set_option Elab.async false

namespace Rule30Submission

open Ruliology.CellularAutomata
open Ruliology.CellularAutomata.Rule30Jen
open Ruliology.CellularAutomata.Rule30Prize
open Ruliology.CellularAutomata.Rule30Realization
open Ruliology.CellularAutomata.Rule30StripCertificates

/-! ## Jen's theorem with a clock (Theorem A), on the kit's `evol` -/

lemma edge (x0 : ℤ → Bool) (e : ℤ) (he : x0 e = true) (hl : ∀ j < e, x0 j = false) (t : ℕ) :
    evol x0 t (e - t) = true ∧ ∀ j < e - t, evol x0 t j = false := by
  induction t with
  | zero => simpa using ⟨he, hl⟩
  | succ t ih =>
    obtain ⟨h1, h2⟩ := ih
    constructor
    · show xor (evol x0 t (e - ↑(t + 1) - 1)) (evol x0 t (e - ↑(t + 1)) || evol x0 t (e - ↑(t + 1) + 1)) = true
      have a1 : evol x0 t (e - ↑(t + 1) - 1) = false := h2 _ (by push_cast; omega)
      have a2 : evol x0 t (e - ↑(t + 1)) = false := h2 _ (by push_cast; omega)
      have a3 : e - ↑(t + 1) + 1 = e - ↑t := by push_cast; ring
      rw [a1, a2, a3, h1]; rfl
    · intro j hj
      show xor (evol x0 t (j - 1)) (evol x0 t j || evol x0 t (j + 1)) = false
      have b1 : evol x0 t (j - 1) = false := h2 _ (by push_cast at hj; omega)
      have b2 : evol x0 t j = false := h2 _ (by push_cast at hj; omega)
      have b3 : evol x0 t (j + 1) = false := h2 _ (by push_cast at hj; omega)
      rw [b1, b2, b3]; rfl

def Per (x0 : ℤ → Bool) (k : ℤ) (P a b : ℕ) : Prop :=
  ∀ t : ℕ, a ≤ t → t + P ≤ b → evol x0 t k = evol x0 (t + P) k

lemma left (x0 : ℤ → Bool) (k : ℤ) (P a b : ℕ) (hP : 1 ≤ P) (h0 : Per x0 k P a b) (h1 : Per x0 (k + 1) P a b) :
    Per x0 (k - 1) P a (b - 1) := by
  intro t ht htb
  have inv : ∀ s : ℕ, evol x0 s (k - 1) = xor (evol x0 (s + 1) k) (evol x0 s k || evol x0 s (k + 1)) := by
    intro s
    show evol x0 s (k - 1) = xor (xor (evol x0 s (k - 1)) (evol x0 s k || evol x0 s (k + 1))) (evol x0 s k || evol x0 s (k + 1))
    cases evol x0 s (k - 1) <;> cases (evol x0 s k || evol x0 s (k + 1)) <;> rfl
  rw [inv t, inv (t + P)]
  have e1 : evol x0 (t + 1) k = evol x0 (t + 1 + P) k := h0 (t + 1) (by omega) (by omega)
  have e2 : evol x0 t k = evol x0 (t + P) k := h0 t ht (by omega)
  have e3 : evol x0 t (k + 1) = evol x0 (t + P) (k + 1) := h1 t ht (by omega)
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
  have black : evol x0 (a + P) (c - j) = true := by
    have := (E (a + P)).1
    have e : c - ↑L - ↑(a + P) = c - ↑j := by rw [hj]; push_cast; ring
    rwa [e] at this
  have white : evol x0 a (c - j) = false := by
    have := (E a).2 (c - j) (by rw [hj]; push_cast; omega)
    exact this
  have := hper a le_rfl (by omega)
  rw [white, black] at this
  exact absurd this (by decide)

theorem no_two_periodic (x0 : ℤ → Bool) (c : ℤ) (L : ℕ) (hc : x0 (c - L) = true) (hl : ∀ j < c - L, x0 j = false)
    (P a : ℕ) (hP : 1 ≤ P)
    (h0 : ∀ t : ℕ, a ≤ t → evol x0 t c = evol x0 (t + P) c)
    (h1 : ∀ t : ℕ, a ≤ t → evol x0 t (c + 1) = evol x0 (t + P) (c + 1)) : False := by
  have := theorem_A x0 c L hc hl P a (2 * a + L + 2 * P) hP (fun t ht _ => h0 t ht) (fun t ht _ => h1 t ht)
  omega

/-- Evolution is a semigroup: evolving `evol x0 k` for `t` steps is evolving `x0` for `k + t`. -/
lemma evol_add (x0 : ℤ → Bool) (k t : ℕ) : evol (evol x0 k) t = evol x0 (k + t) := by
  induction t with
  | zero => rfl
  | succ t ih =>
    funext p
    show rule (evol (evol x0 k) t (p - 1)) (evol (evol x0 k) t p) (evol (evol x0 k) t (p + 1)) =
      rule (evol x0 (k + t) (p - 1)) (evol x0 (k + t) p) (evol x0 (k + t) (p + 1))
    rw [ih]

/-! ## The finite relaxation on `K` cells, and the actual window -/

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

/-- `A ⊆ B` as bitmasks: one `&&&`. -/
def sub (A B : ℕ) : Bool := (A &&& B == A)

lemma sub_spec (A B : ℕ) (h : sub A B = true) : ∀ s, A.testBit s = true → B.testBit s = true := by
  intro s hs
  simp only [sub, beq_iff_eq] at h
  have := congrArg (fun x => x.testBit s) h
  simp only [Nat.testBit_and, hs, Bool.true_and] at this
  exact this

/-- One period of the word from `X`: `none` if cell c + 1 is not constant at some tick, else the final set. -/
def walk (K : ℕ) : List ℕ → ℕ → Option ℕ
  | [], X => some X
  | w :: ws, X => if const0 K X then walk K ws (img K w X) else none

lemma walk_some (K : ℕ) : ∀ (ws : List ℕ) X Y, walk K ws X = some Y → Y = run K ws X ∧ ticks K ws X = true := by
  intro ws
  induction ws with
  | nil => intro X Y h; simp only [walk, Option.some.injEq] at h; subst h; simp [run, ticks]
  | cons w ws ih =>
    intro X Y h
    simp only [walk] at h
    by_cases hc : const0 K X = true
    · rw [if_pos hc] at h
      obtain ⟨h1, h2⟩ := ih _ _ h
      exact ⟨by simpa [run] using h1, by simp [ticks, hc, h2]⟩
    · rw [if_neg hc] at h
      exact absurd h (by simp)

/-- The certificate for a word: after `n0` warm-up periods, one more period keeps cell c + 1 constant at every
tick and maps the set into itself. -/
def check (K : ℕ) (ws : List ℕ) (n0 : ℕ) : Bool :=
  match walk K ws (reach K ws n0) with
  | none => false
  | some X => sub X (reach K ws n0)
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

/-! ## Sets: everything in an image comes from a state of the set; images are monotone -/

lemma imgAux_elim (K w S : ℕ) : ∀ n acc y, (imgAux K w S n acc).testBit y = true →
    acc.testBit y = true ∨ ∃ s, s < n ∧ S.testBit s = true ∧ ∃ u, u ≤ 1 ∧ y = stp K w s u := by
  intro n
  induction n with
  | zero => intro acc y h; exact Or.inl h
  | succ n ih =>
    intro acc y h
    rw [imgAux_succ] at h
    rcases ih _ y h with h' | ⟨s, hs, hS, u, hu, rfl⟩
    · split_ifs at h' with hn
      · simp only [Nat.testBit_or, Bool.or_eq_true] at h'
        rcases h' with (h' | h') | h'
        · exact Or.inl h'
        · right; refine ⟨n, by omega, hn, 0, by omega, ?_⟩
          rw [Nat.one_shiftLeft, Nat.testBit_two_pow] at h'
          exact (decide_eq_true_iff.mp h').symm
        · right; refine ⟨n, by omega, hn, 1, by omega, ?_⟩
          rw [Nat.one_shiftLeft, Nat.testBit_two_pow] at h'
          exact (decide_eq_true_iff.mp h').symm
      · exact Or.inl h'
    · exact Or.inr ⟨s, by omega, hS, u, hu, rfl⟩

lemma img_mono (K w A B : ℕ) (hAB : ∀ s, A.testBit s = true → B.testBit s = true) :
    ∀ y, (img K w A).testBit y = true → (img K w B).testBit y = true := by
  intro y hy
  rcases imgAux_elim K w A (2 ^ K) 0 y hy with h | ⟨s, hs, hA, u, hu, rfl⟩
  · simp at h
  · exact img_mem K w B s u hs hu (hAB s hA)

lemma run_mono (K : ℕ) : ∀ (ws : List ℕ) (A B : ℕ), (∀ s, A.testBit s = true → B.testBit s = true) →
    ∀ y, (run K ws A).testBit y = true → (run K ws B).testBit y = true := by
  intro ws
  induction ws with
  | nil => intro A B h y hy; exact h y hy
  | cons w ws ih => intro A B h y hy; exact ih _ _ (img_mono K w A B h) y hy

/-- From a set that one period maps into itself, every later set stays inside it. -/
lemma reach_sub (K : ℕ) (ws : List ℕ) (n0 : ℕ)
    (hS : ∀ s, (run K ws (reach K ws n0)).testBit s = true → (reach K ws n0).testBit s = true) :
    ∀ n, n0 ≤ n → ∀ y, (reach K ws n).testBit y = true → (reach K ws n0).testBit y = true := by
  intro n hn
  induction n, hn using Nat.le_induction with
  | base => intro y hy; exact hy
  | succ n _ ih =>
    intro y hy
    have hy' : (run K ws (reach K ws n)).testBit y = true := hy
    exact hS y (run_mono K ws _ _ ih y hy')


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

def win (K : ℕ) (x0 : ℤ → Bool) (c : ℤ) (t : ℕ) : ℕ := enc (fun j => evol x0 t (c + 1 + j)) K

lemma win_lt (K : ℕ) (x0 : ℤ → Bool) (c : ℤ) (t : ℕ) : win K x0 c t < 2 ^ K := enc_lt _ K

lemma win_bit (K : ℕ) (x0 : ℤ → Bool) (c : ℤ) (t j : ℕ) (hj : j < K) :
    (win K x0 c t).testBit j = evol x0 t (c + 1 + j) := by
  simp [win, enc_testBit, hj]

lemma win_step (K : ℕ) (hK : StpOK K) (hK2 : 2 ≤ K) (x0 : ℤ → Bool) (c : ℤ) (t : ℕ) :
    win K x0 c (t + 1) = stp K (evol x0 t c).toNat (win K x0 c t) (evol x0 t (c + K + 1)).toNat := by
  apply Nat.eq_of_testBit_eq
  intro j
  by_cases hj : j < K
  · rw [win_bit K x0 c (t + 1) j hj, hK _ (win_lt K x0 c t) _ _ j hj]
    show xor (evol x0 t (c + 1 + j - 1)) (evol x0 t (c + 1 + j) || evol x0 t (c + 1 + j + 1)) = _
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
    (img K (evol x0 t c).toNat S).testBit (win K x0 c (t + 1)) = true := by
  rw [win_step K hK hK2]
  exact img_mem _ _ _ _ _ (win_lt K x0 c t) (Bool.toNat_le _) hS

lemma run_mem (K : ℕ) (hK : StpOK K) (hK2 : 2 ≤ K) (x0 : ℤ → Bool) (c : ℤ) :
    ∀ (ws : List ℕ) t X, X.testBit (win K x0 c t) = true →
      (∀ i < ws.length, (evol x0 (t + i) c).toNat = ws.getD i 0) →
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
  ∀ n i, i < ws.length → (evol x0 (a + n * ws.length + i) c).toNat = ws.getD i 0

/-- The determination package for a word at width K: a set reached after `n0` periods that one period maps into
itself, with cell c + 1 constant at every tick of the period. -/
def Det (K : ℕ) (ws : List ℕ) : Prop :=
  ∃ S n0, reach K ws n0 = S ∧ (∀ s, (run K ws S).testBit s = true → S.testBit s = true) ∧
    ∀ i < ws.length, const0 K (run K (ws.take i) S) = true

lemma det_of_check (K : ℕ) (ws : List ℕ) (n0 : ℕ) (h : check K ws n0 = true) : Det K ws := by
  unfold check at h
  split at h
  · exact absurd h (by simp)
  · rename_i X hX
    obtain ⟨h1, h2⟩ := walk_some K ws _ _ hX
    refine ⟨reach K ws n0, n0, rfl, ?_, ticks_spec K ws _ h2⟩
    rw [← h1]; exact sub_spec _ _ h

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
      evol x0 (a + n * ws.length + i) (c + 1) = evol x0 (a + (n + 1) * ws.length + i) (c + 1) := by
  obtain ⟨S, n0, hS, hsub, ht⟩ := hd
  refine ⟨n0, fun n i hn hi => ?_⟩
  have mem : ∀ m, n0 ≤ m → (run K (ws.take i) S).testBit (win K x0 c (a + m * ws.length + i)) = true := by
    intro m hm
    have hm' := orbit_mem K hK hK2 x0 c ws a hr m
    replace hm' := reach_sub K ws n0 (by rw [hS]; exact hsub) m hm _ hm'
    rw [hS] at hm'
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
    apply core K hK hK2 ws hd hp (evol x0 k) c 0 (by simpa using E.1) (by simpa using E.2) (a + k * ws.length - k)
    intro n i hi
    have : k ≤ k * ws.length := Nat.le_mul_of_pos_right k hp
    rw [evol_add, show k + (a + k * ws.length - k + n * ws.length + i) = a + (n + k) * ws.length + i by
      rw [add_mul]; omega]
    exact hr (n + k) i hi

/-! ## The words -/

def words8 : List (ℕ × List ℕ) := [
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1]),
  (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1]),
  (4, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1]),
  (4, [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
  (2, [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1]),
  (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1]),
  (3, [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1]),
  (3, [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1]),
  (3, [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1]),
  (3, [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1]),
  (2, [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])]

def words10 : List (ℕ × List ℕ) := [
  (4, [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]),
  (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1]),
  (4, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1]),
  (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1]),
  (3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]),
  (2, [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1])]

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_0 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_1 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_2 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_3 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_4 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_5 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_6 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_7 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_8 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_9 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_10 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_11 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_12 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_13 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1] 4 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_14 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_15 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_16 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_17 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_18 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_19 : check 8 [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 4 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_20 : check 8 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_21 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_22 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_23 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_24 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_25 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_26 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_27 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_28 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_29 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_30 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_31 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_32 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_33 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_34 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_35 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_36 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_37 : check 8 [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_38 : check 8 [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_39 : check 8 [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w8_40 : check 8 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w10_0 : check 10 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1] 4 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w10_1 : check 10 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w10_2 : check 10 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1] 4 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w10_3 : check 10 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w10_4 : check 10 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1] 2 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w10_5 : check 10 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1] 3 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma w10_6 : check 10 [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1] 2 = true := by decide +kernel

lemma checks8 : (words8.all fun e => check 8 e.2 e.1) = true := by
  simp only [words8, List.all_cons, List.all_nil, Bool.and_true, w8_0, w8_1, w8_2, w8_3, w8_4, w8_5, w8_6, w8_7, w8_8, w8_9, w8_10, w8_11, w8_12, w8_13, w8_14, w8_15, w8_16, w8_17, w8_18, w8_19, w8_20, w8_21, w8_22, w8_23, w8_24, w8_25, w8_26, w8_27, w8_28, w8_29, w8_30, w8_31, w8_32, w8_33, w8_34, w8_35, w8_36, w8_37, w8_38, w8_39, w8_40]

lemma checks10 : (words10.all fun e => check 10 e.2 e.1) = true := by
  simp only [words10, List.all_cons, List.all_nil, Bool.and_true, w10_0, w10_1, w10_2, w10_3, w10_4, w10_5, w10_6]

set_option maxRecDepth 100000 in
lemma counts : words8.length = 41 ∧ words10.length = 7 := by decide

set_option maxRecDepth 100000 in
lemma nonempty : ∀ e ∈ words8 ++ words10, 1 ≤ e.2.length := by decide

/-- **The words, for every configuration with a leftmost black cell.** No column reads any listed word
periodically from any time on. -/
theorem words_general (ws : List ℕ) (hw : ws ∈ (words8 ++ words10).map Prod.snd) (x0 : ℤ → Bool) (e : ℤ)
    (he : x0 e = true) (hl : ∀ j < e, x0 j = false) (c : ℤ) (a : ℕ) (hr : ReadsW x0 c ws a) : False := by
  simp only [List.map_append, List.mem_append, List.mem_map] at hw
  rcases hw with ⟨⟨n0, ws'⟩, hm, rfl⟩ | ⟨⟨n0, ws'⟩, hm, rfl⟩
  · have hc := List.all_eq_true.mp checks8 _ hm
    have hp : 1 ≤ ws'.length := nonempty _ (List.mem_append_left _ hm)
    exact no_word 8 stpOK8 (by norm_num) ws' (det_of_check 8 ws' n0 hc) hp x0 e he hl c a hr
  · have hc := List.all_eq_true.mp checks10 _ hm
    have hp : 1 ≤ ws'.length := nonempty _ (List.mem_append_right _ hm)
    exact no_word 10 stpOK10 (by norm_num) ws' (det_of_check 10 ws' n0 hc) hp x0 e he hl c a hr

/-! ## The bridge to the kit's statements: the single-seed pattern and `EventuallyWord` -/

/-- The words as Boolean lists, in the kit's form. -/
def words : List (List Bool) := (words8 ++ words10).map fun e => e.2.map (· == 1)

set_option maxRecDepth 100000 in
lemma words_toNat : ∀ e ∈ words8 ++ words10, (e.2.map (· == 1)).map Bool.toNat = e.2 := by decide

lemma seed_leftmost : seed 0 = true ∧ ∀ p : ℤ, p < 0 → seed p = false := by
  refine ⟨by simp [seed], fun p hp => ?_⟩
  simp only [seed, decide_eq_false_iff_not]; omega

lemma getD_map_toNat : ∀ (w : List Bool) (i : ℕ), (w.map Bool.toNat).getD i 0 = (w.getD i false).toNat
  | [], _ => rfl
  | _ :: _, 0 => rfl
  | _ :: w, i + 1 => by
    rw [List.map_cons, List.getD_cons_succ, List.getD_cons_succ]
    exact getD_map_toNat w i

/-- An eventual word of the center column is a `ReadsW` of the seed's evolution at column `0`. -/
lemma readsW_of_eventuallyWord (w : List Bool) (hw : w ≠ []) (h : EventuallyWord w) :
    ∃ a, ReadsW seed 0 (w.map Bool.toNat) a := by
  obtain ⟨T, hT⟩ := h
  have hlen : 0 < w.length := List.length_pos_iff.2 hw
  refine ⟨T, fun n i hi => ?_⟩
  rw [List.length_map] at hi ⊢
  rw [evol_seed, hT _ (by omega), show T + n * w.length + i - T = i + n * w.length by omega,
    Nat.add_mul_mod_self_right, Nat.mod_eq_of_lt hi, getD_map_toNat]

/-- **Headline.** For every listed word `w`, the center column of the single-seed pattern is not eventually
`w` repeated, whatever the transient. -/
theorem not_eventuallyWord_words (w : List Bool) (hw : w ∈ words) : ¬ EventuallyWord w := by
  intro h
  simp only [words, List.mem_map] at hw
  obtain ⟨e, he, rfl⟩ := hw
  have hne : e.2.map (· == 1) ≠ [] := by
    intro h0
    have h1 : (e.2.map (· == 1)).length = 0 := by rw [h0]; rfl
    rw [List.length_map] at h1
    have := nonempty e he
    omega
  obtain ⟨a, hr⟩ := readsW_of_eventuallyWord _ hne h
  rw [words_toNat e he] at hr
  exact words_general e.2 (List.mem_map.2 ⟨e, he, rfl⟩) seed 0 seed_leftmost.1 seed_leftmost.2 0 a hr

end Rule30Submission
