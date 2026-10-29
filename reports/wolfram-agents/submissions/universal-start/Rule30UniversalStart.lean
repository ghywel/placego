module

public import Ruliology.CellularAutomata.Rule30Prize
public import Ruliology.CellularAutomata.Rule30Realization

/-!
# Rule 30: the universal start of the right diagonals

Write `D j t = x_t (t - j)` for the right diagonals of rule 30 from a start whose rightmost black cell is at `0`
(`rightDiag`, on `Rule30Realization.evol`), and `s d = x (-d)` for the start bits. Then `D 0` is black and
`D (-1)` white for ever, and each diagonal is a running XOR of the OR of the two to its right (`rightDiag_step`).

* `universal_start`: let `m ≥ 2` be the first index with `s m = s (m - 1)`. Then the diagonals `D (m+1), …,
  D (m+6)` have least periods `4, 8, 8, 16, 32, 32`, and `D (m+7)` has least period `32` or `64`, whatever the
  other start bits.
* `universal_start_finite`: for a finitely supported start, such an `m` exists, so the conclusion holds for every
  finite seed. For a start with an infinite alternating left tail it can fail to exist.

The proof has three parts.
1. *The prefix.* Up to `m`, every diagonal alternates with its start phase, since its two feeders have opposite
   phases and their OR is always black. `D (m-1)` and `D m` are then alternating with equal phase.
2. *The all-time bound.* A running XOR of a `P`-periodic forcing repeats after `2P` (`run_double`), so the seven
   diagonals after two alternating feeders repeat after `4, 8, …, 256` ticks (`E_per`).
3. *The certificate* (`cert`, assembled from sixteen `decide +kernel` declarations `cert_0000` … `cert_1111`
   of sixteen cases each). For both feeder phases and all seven free start bits (`256` cases), one loop
   computes the first `256` ticks of the seven diagonals as bit masks (`loop_spec`). Cyclic rotation checks then
   decide each period and reject every smaller positive period (`perOK_iff`, `leastOK_spec`).

The seventh diagonal's period is `32` or `64` according to the start bits; nothing is claimed beyond `D (m+7)`.
-/

@[expose] public section

namespace Ruliology.CellularAutomata.Rule30UniversalStart

/-! ### Periods and running XORs -/

/-- `f` repeats with period `P` (from time `0`). -/
def Per (f : Nat → Bool) (P : Nat) : Prop := ∀ t, f (t + P) = f t

/-- `f` has period `P` and no smaller positive period; for `0 < P` this is its least positive period. -/
def LeastPer (f : Nat → Bool) (P : Nat) : Prop := Per f P ∧ ∀ c, 0 < c → c < P → ¬ Per f c

theorem per_mul {f : Nat → Bool} {P : Nat} (h : Per f P) : ∀ n t, f (t + n * P) = f t := by
  intro n
  induction n with
  | zero => intro t; simp
  | succ n ih => intro t; rw [show t + (n + 1) * P = (t + n * P) + P by rw [Nat.succ_mul]; omega, h, ih]

theorem per_of_dvd {f : Nat → Bool} {P Q : Nat} (h : Per f P) (hd : P ∣ Q) : Per f Q := by
  obtain ⟨n, rfl⟩ := hd
  intro t
  rw [Nat.mul_comm]
  exact per_mul h n t

theorem per_mod {f : Nat → Bool} {P : Nat} (h : Per f P) (t : Nat) : f t = f (t % P) := by
  have := per_mul h (t / P) (t % P)
  rw [Nat.mul_comm, Nat.mod_add_div] at this
  exact this

theorem per_or {f g : Nat → Bool} {P : Nat} (hf : Per f P) (hg : Per g P) :
    Per (fun t => f t || g t) P := by
  intro t; simp only; rw [hf, hg]

/-- The running XOR from `b` with forcing `g`. -/
def run (b : Bool) (g : Nat → Bool) : Nat → Bool
  | 0 => b
  | t + 1 => xor (run b g t) (g t)

/-- XOR of `f 0, …, f (n - 1)`. -/
def xr (f : Nat → Bool) : Nat → Bool
  | 0 => false
  | n + 1 => xor (xr f n) (f n)

theorem xr_add (f : Nat → Bool) (n m : Nat) :
    xr f (n + m) = xor (xr f n) (xr (fun i => f (n + i)) m) := by
  induction m with
  | zero => simp [xr]
  | succ m ih =>
    rw [Nat.add_succ]
    simp only [xr]
    rw [ih, Bool.xor_assoc]

theorem run_shift (b : Bool) (g : Nat → Bool) (t n : Nat) :
    run b g (t + n) = xor (run b g t) (xr (fun i => g (t + i)) n) := by
  induction n with
  | zero => simp [xr]
  | succ n ih =>
    rw [show t + (n + 1) = (t + n) + 1 by omega]
    simp only [run, xr]
    rw [ih, Bool.xor_assoc]

theorem xr_window {g : Nat → Bool} {n : Nat} (hg : Per g n) (t : Nat) :
    xr (fun i => g (t + i)) n = xr g n := by
  induction t with
  | zero => simp
  | succ t ih =>
    have e1 : xr (fun i => g (t + i)) (1 + n) = xor (g t) (xr (fun i => g (t + 1 + i)) n) := by
      rw [xr_add]
      simp [xr, Nat.add_assoc]
    have e2 : xr (fun i => g (t + i)) (n + 1) = xor (xr (fun i => g (t + i)) n) (g t) := by
      simp only [xr]
      rw [hg t]
    rw [Nat.add_comm 1 n, e2] at e1
    rw [← ih]
    revert e1
    cases xr (fun i => g (t + i)) n <;> cases g t <;> cases xr (fun i => g (t + 1 + i)) n <;> simp

/-- **A running XOR of a `P`-periodic forcing repeats after `2P`**, whatever the forcing's parity. -/
theorem run_double {b : Bool} {g : Nat → Bool} {P : Nat} (hg : Per g P) : Per (run b g) (2 * P) := by
  intro t
  rw [show t + 2 * P = (t + P) + P by omega, run_shift b g (t + P) P, run_shift b g t P,
    xr_window hg, xr_window hg]
  cases run b g t <;> cases xr g P <;> rfl

theorem run_unique {f g : Nat → Bool} (h : ∀ t, f (t + 1) = xor (f t) (g t)) : f = run (f 0) g := by
  funext t
  induction t with
  | zero => rfl
  | succ t ih => rw [h t, ih]; rfl

/-! ### Two equal-phase alternating feeders and the seven diagonals after them -/

/-- The alternating profile of phase `p`. -/
def alt (p : Bool) (t : Nat) : Bool := xor p (decide (t % 2 = 1))

theorem alt_per (p : Bool) : Per (alt p) 2 := by
  intro t; unfold alt; rw [show (t + 2) % 2 = t % 2 by omega]

theorem alt_succ (p : Bool) (t : Nat) : alt p (t + 1) = !alt p t := by
  unfold alt
  rcases Nat.mod_two_eq_zero_or_one t with h | h
  · have h' : (t + 1) % 2 = 1 := by omega
    simp [h, h']
  · have h' : (t + 1) % 2 = 0 := by omega
    simp [h, h']

theorem alt_not (p : Bool) (t : Nat) : alt (!p) t = !alt p t := by
  unfold alt; cases p <;> simp

/-- `E p bits k` is diagonal `j + k` from the first new diagonal `j`, after two alternating feeders of equal phase
`p`, with start bits `bits 0, bits 1, …`. -/
def E (p : Bool) (bits : Nat → Bool) : Nat → Nat → Bool
  | 0 => run (bits 0) (fun t => alt p t || alt p t)
  | 1 => run (bits 1) (fun t => E p bits 0 t || alt p t)
  | k + 2 => run (bits (k + 2)) (fun t => E p bits (k + 1) t || E p bits k t)

/-- **The all-time upper period**: `E p bits k` repeats after `2^(k+2)`. -/
theorem E_per (p : Bool) (bits : Nat → Bool) :
    ∀ k, Per (E p bits k) (2 ^ (k + 2)) ∧ Per (E p bits (k + 1)) (2 ^ (k + 3)) := by
  intro k
  induction k with
  | zero =>
    have h0 : Per (E p bits 0) 4 := by
      show Per (run (bits 0) (fun t => alt p t || alt p t)) (2 * 2)
      exact run_double (per_or (alt_per p) (alt_per p))
    refine ⟨h0, ?_⟩
    show Per (run (bits 1) (fun t => E p bits 0 t || alt p t)) (2 * 4)
    exact run_double (per_or h0 (per_of_dvd (alt_per p) ⟨2, rfl⟩))
  | succ k ih =>
    refine ⟨ih.2, ?_⟩
    have hdvd : 2 ^ (k + 2) ∣ 2 ^ (k + 3) := ⟨2, by rw [show k + 3 = (k + 2) + 1 by omega]; exact Nat.pow_succ 2 (k + 2)⟩
    have h := run_double (b := bits (k + 2)) (per_or ih.2 (per_of_dvd ih.1 hdvd))
    have e : 2 * 2 ^ (k + 3) = 2 ^ (k + 1 + 3) := by
      rw [show k + 1 + 3 = (k + 3) + 1 by omega]; exact Nat.pow_succ'.symm
    rw [e] at h
    exact h

/-- All seven repeat after `256` ticks. -/
theorem E_per256 (p : Bool) (bits : Nat → Bool) (k : Nat) (hk : k ≤ 6) : Per (E p bits k) 256 :=
  per_of_dvd (E_per p bits k).1 (show 2 ^ (k + 2) ∣ 2 ^ 8 from Nat.pow_dvd_pow 2 (by omega))

theorem E_congr (p : Bool) (bits bits' : Nat → Bool) :
    ∀ k, (∀ i, i ≤ k + 1 → bits i = bits' i) → E p bits k = E p bits' k ∧ E p bits (k + 1) = E p bits' (k + 1) := by
  intro k
  induction k with
  | zero =>
    intro h
    have h0 : E p bits 0 = E p bits' 0 := by
      show run (bits 0) _ = run (bits' 0) _
      rw [h 0 (by omega)]
    refine ⟨h0, ?_⟩
    show run (bits 1) (fun t => E p bits 0 t || alt p t) = run (bits' 1) (fun t => E p bits' 0 t || alt p t)
    rw [h 1 (by omega), h0]
  | succ k ih =>
    intro h
    obtain ⟨h1, h2⟩ := ih (fun i hi => h i (by omega))
    refine ⟨h2, ?_⟩
    show run (bits (k + 2)) (fun t => E p bits (k + 1) t || E p bits k t) =
      run (bits' (k + 2)) (fun t => E p bits' (k + 1) t || E p bits' k t)
    rw [h (k + 2) (by omega), h1, h2]

/-! ### The loop that computes the first 256 ticks of all seven at once -/

structure St where
  v0 : Bool
  v1 : Bool
  v2 : Bool
  v3 : Bool
  v4 : Bool
  v5 : Bool
  v6 : Bool
  m0 : Nat
  m1 : Nat
  m2 : Nat
  m3 : Nat
  m4 : Nat
  m5 : Nat
  m6 : Nat

def bitAt (v : Bool) (t : Nat) : Nat := if v then 2 ^ t else 0

def step (p : Bool) (t : Nat) (s : St) : St where
  v0 := xor s.v0 (alt p t || alt p t)
  v1 := xor s.v1 (s.v0 || alt p t)
  v2 := xor s.v2 (s.v1 || s.v0)
  v3 := xor s.v3 (s.v2 || s.v1)
  v4 := xor s.v4 (s.v3 || s.v2)
  v5 := xor s.v5 (s.v4 || s.v3)
  v6 := xor s.v6 (s.v5 || s.v4)
  m0 := s.m0 ||| bitAt s.v0 t
  m1 := s.m1 ||| bitAt s.v1 t
  m2 := s.m2 ||| bitAt s.v2 t
  m3 := s.m3 ||| bitAt s.v3 t
  m4 := s.m4 ||| bitAt s.v4 t
  m5 := s.m5 ||| bitAt s.v5 t
  m6 := s.m6 ||| bitAt s.v6 t

def loop (p : Bool) (bits : Nat → Bool) : Nat → St
  | 0 => ⟨bits 0, bits 1, bits 2, bits 3, bits 4, bits 5, bits 6, 0, 0, 0, 0, 0, 0, 0⟩
  | t + 1 => step p t (loop p bits t)

def St.v (s : St) : Nat → Bool
  | 0 => s.v0 | 1 => s.v1 | 2 => s.v2 | 3 => s.v3 | 4 => s.v4 | 5 => s.v5 | 6 => s.v6 | _ => false

def St.m (s : St) : Nat → Nat
  | 0 => s.m0 | 1 => s.m1 | 2 => s.m2 | 3 => s.m3 | 4 => s.m4 | 5 => s.m5 | 6 => s.m6 | _ => 0

theorem E_succ0 (p : Bool) (bits : Nat → Bool) (t : Nat) :
    E p bits 0 (t + 1) = xor (E p bits 0 t) (alt p t || alt p t) := rfl
theorem E_succ1 (p : Bool) (bits : Nat → Bool) (t : Nat) :
    E p bits 1 (t + 1) = xor (E p bits 1 t) (E p bits 0 t || alt p t) := rfl
theorem E_succ (p : Bool) (bits : Nat → Bool) (k t : Nat) :
    E p bits (k + 2) (t + 1) = xor (E p bits (k + 2) t) (E p bits (k + 1) t || E p bits k t) := rfl
theorem E_zero (p : Bool) (bits : Nat → Bool) (k : Nat) : E p bits k 0 = bits k := by
  match k with
  | 0 => rfl
  | 1 => rfl
  | _ + 2 => rfl

theorem testBit_bitAt (v : Bool) (t i : Nat) : (bitAt v t).testBit i = (v && decide (t = i)) := by
  unfold bitAt
  cases v
  · simp
  · simp [Nat.testBit_two_pow]

theorem mask_step (m : Nat) (v : Bool) (t : Nat) (f : Nat → Bool) (hv : v = f t)
    (hm : ∀ i, m.testBit i = (decide (i < t) && f i)) :
    ∀ i, (m ||| bitAt v t).testBit i = (decide (i < t + 1) && f i) := by
  intro i
  rw [Nat.testBit_or, hm, testBit_bitAt, hv]
  by_cases h1 : i < t
  · have h2 : i < t + 1 := by omega
    have h3 : t ≠ i := by omega
    simp [h1, h2, h3]
  · by_cases h4 : i = t
    · subst h4; simp
    · have h2 : ¬ i < t + 1 := by omega
      have h3 : t ≠ i := by omega
      simp [h1, h2, h3]

/-- **The loop computes the seven diagonals**: values at tick `t` and the bits of all earlier ticks. -/
theorem loop_spec (p : Bool) (bits : Nat → Bool) :
    ∀ t, (∀ k, k ≤ 6 → (loop p bits t).v k = E p bits k t) ∧
      (∀ k, k ≤ 6 → ∀ i, ((loop p bits t).m k).testBit i = (decide (i < t) && E p bits k i)) := by
  intro t
  induction t with
  | zero =>
    refine ⟨fun k hk => ?_, fun k hk i => ?_⟩
    · rw [E_zero]
      obtain _ | _ | _ | _ | _ | _ | _ | k := k <;> first | rfl | omega
    · obtain _ | _ | _ | _ | _ | _ | _ | k := k <;> first | simp [loop, St.m] | omega
  | succ t ih =>
    obtain ⟨hv, hm⟩ := ih
    have v0 := hv 0 (by omega); have v1 := hv 1 (by omega); have v2 := hv 2 (by omega)
    have v3 := hv 3 (by omega); have v4 := hv 4 (by omega); have v5 := hv 5 (by omega)
    have v6 := hv 6 (by omega)
    simp only [St.v] at v0 v1 v2 v3 v4 v5 v6
    refine ⟨fun k hk => ?_, fun k hk => ?_⟩
    · obtain _ | _ | _ | _ | _ | _ | _ | k := k
      · show xor (loop p bits t).v0 _ = _; rw [v0, E_succ0]
      · show xor (loop p bits t).v1 _ = _; rw [v1, v0, E_succ1]
      · show xor (loop p bits t).v2 _ = _; rw [v2, v1, v0, E_succ]
      · show xor (loop p bits t).v3 _ = _; rw [v3, v2, v1, E_succ]
      · show xor (loop p bits t).v4 _ = _; rw [v4, v3, v2, E_succ]
      · show xor (loop p bits t).v5 _ = _; rw [v5, v4, v3, E_succ]
      · show xor (loop p bits t).v6 _ = _; rw [v6, v5, v4, E_succ]
      · omega
    · obtain _ | _ | _ | _ | _ | _ | _ | k := k
      · exact mask_step _ _ t (E p bits 0) v0 (hm 0 (by omega))
      · exact mask_step _ _ t (E p bits 1) v1 (hm 1 (by omega))
      · exact mask_step _ _ t (E p bits 2) v2 (hm 2 (by omega))
      · exact mask_step _ _ t (E p bits 3) v3 (hm 3 (by omega))
      · exact mask_step _ _ t (E p bits 4) v4 (hm 4 (by omega))
      · exact mask_step _ _ t (E p bits 5) v5 (hm 5 (by omega))
      · exact mask_step _ _ t (E p bits 6) v6 (hm 6 (by omega))
      · omega

/-! ### Cyclic period checks on a 256-bit mask -/

def mask256 : Nat := 2 ^ 256 - 1

/-- Rotate a 256-bit word: bit `i` of the result is bit `(i + c) % 256` of `m`. -/
def rot (m c : Nat) : Nat := ((m >>> c) ||| (m <<< (256 - c))) &&& mask256

theorem testBit_rot (m c i : Nat) (hc : c ≤ 256) (hm : ∀ j, 256 ≤ j → m.testBit j = false) :
    (rot m c).testBit i = (decide (i < 256) && m.testBit ((i + c) % 256)) := by
  unfold rot mask256
  rw [Nat.testBit_and, Nat.testBit_two_pow_sub_one, Nat.testBit_or, Nat.testBit_shiftRight,
    Nat.testBit_shiftLeft]
  by_cases hi : i < 256
  · by_cases hic : i + c < 256
    · have e : (i + c) % 256 = i + c := Nat.mod_eq_of_lt hic
      have hge : ¬ (256 - c ≤ i) := by omega
      simp [hi, e, hge, Nat.add_comm c i]
    · have e : (i + c) % 256 = i - (256 - c) := by omega
      have hge : 256 - c ≤ i := by omega
      have hz : m.testBit (c + i) = false := hm _ (by omega)
      simp [hi, e, hge, hz]
  · simp [hi]

def perOK (m c : Nat) : Bool := rot m c == m

def leastOK (m P : Nat) : Bool := perOK m P && (List.range P).all (fun c => c == 0 || !perOK m c)

/-- The mask of diagonal `k` after the full cycle. -/
def M (p : Bool) (bits : Nat → Bool) (k : Nat) : Nat := (loop p bits 256).m k

theorem M_bit (p : Bool) (bits : Nat → Bool) (k : Nat) (hk : k ≤ 6) (i : Nat) :
    (M p bits k).testBit i = (decide (i < 256) && E p bits k i) :=
  (loop_spec p bits 256).2 k hk i

theorem perOK_iff (p : Bool) (bits : Nat → Bool) (k : Nat) (hk : k ≤ 6) (c : Nat) (hc : c ≤ 256) :
    perOK (M p bits k) c = true ↔ Per (E p bits k) c := by
  have hz : ∀ j, 256 ≤ j → (M p bits k).testBit j = false := by
    intro j hj
    have hj' : ¬ j < 256 := by omega
    rw [M_bit p bits k hk]; simp [hj']
  have h256 := E_per256 p bits k hk
  unfold perOK
  rw [beq_iff_eq]
  constructor
  · intro h t
    have hb := congrArg (fun m => m.testBit (t % 256)) h
    rw [testBit_rot _ _ _ hc hz, M_bit p bits k hk, M_bit p bits k hk] at hb
    have hlt : t % 256 < 256 := Nat.mod_lt _ (by decide)
    have hlt3 : (t + c) % 256 < 256 := Nat.mod_lt _ (by decide)
    simp [hlt, hlt3] at hb
    rw [per_mod h256 (t + c), per_mod h256 t]
    exact hb
  · intro h
    apply Nat.eq_of_testBit_eq
    intro i
    rw [testBit_rot _ _ _ hc hz, M_bit p bits k hk, M_bit p bits k hk]
    by_cases hi : i < 256
    · have hlt : (i + c) % 256 < 256 := Nat.mod_lt _ (by decide)
      simp only [hi, hlt, decide_true, Bool.true_and]
      rw [← per_mod h256 (i + c), h i]
    · simp [hi]

theorem leastOK_spec (p : Bool) (bits : Nat → Bool) (k : Nat) (hk : k ≤ 6) (P : Nat) (hP : P ≤ 256)
    (h : leastOK (M p bits k) P = true) : LeastPer (E p bits k) P := by
  unfold leastOK at h
  rw [Bool.and_eq_true, List.all_eq_true] at h
  refine ⟨(perOK_iff p bits k hk P hP).1 h.1, fun c hc0 hcP hper => ?_⟩
  have hc := h.2 c (List.mem_range.2 hcP)
  have hne : (c == 0) = false := by simp; omega
  rw [hne, Bool.false_or, (perOK_iff p bits k hk c (by omega)).2 hper] at hc
  exact absurd hc (by decide)

/-! ### The certificate: two phases and seven free start bits -/

def bitsOf (b0 b1 b2 b3 b4 b5 b6 : Bool) : Nat → Bool
  | 0 => b0 | 1 => b1 | 2 => b2 | 3 => b3 | 4 => b4 | 5 => b5 | 6 => b6 | _ => false

def certOK (p b0 b1 b2 b3 b4 b5 b6 : Bool) : Bool :=
  let bits := bitsOf b0 b1 b2 b3 b4 b5 b6
  leastOK (M p bits 0) 4 && leastOK (M p bits 1) 8 && leastOK (M p bits 2) 8 &&
    leastOK (M p bits 3) 16 && leastOK (M p bits 4) 32 && leastOK (M p bits 5) 32 &&
    (leastOK (M p bits 6) 32 || leastOK (M p bits 6) 64)

/-! The certificate is split into sixteen declarations of sixteen cases each, one per feeder phase `p` and
start bits `b0 b1 b2`, so that the kernel releases its evaluation caches between them. -/

theorem cert_0000 : ∀ b3 b4 b5 b6 : Bool, certOK false false false false b3 b4 b5 b6 = true := by
  decide +kernel

theorem cert_0001 : ∀ b3 b4 b5 b6 : Bool, certOK false false false true b3 b4 b5 b6 = true := by
  decide +kernel

theorem cert_0010 : ∀ b3 b4 b5 b6 : Bool, certOK false false true false b3 b4 b5 b6 = true := by
  decide +kernel

theorem cert_0011 : ∀ b3 b4 b5 b6 : Bool, certOK false false true true b3 b4 b5 b6 = true := by
  decide +kernel

theorem cert_0100 : ∀ b3 b4 b5 b6 : Bool, certOK false true false false b3 b4 b5 b6 = true := by
  decide +kernel

theorem cert_0101 : ∀ b3 b4 b5 b6 : Bool, certOK false true false true b3 b4 b5 b6 = true := by
  decide +kernel

theorem cert_0110 : ∀ b3 b4 b5 b6 : Bool, certOK false true true false b3 b4 b5 b6 = true := by
  decide +kernel

theorem cert_0111 : ∀ b3 b4 b5 b6 : Bool, certOK false true true true b3 b4 b5 b6 = true := by
  decide +kernel

theorem cert_1000 : ∀ b3 b4 b5 b6 : Bool, certOK true false false false b3 b4 b5 b6 = true := by
  decide +kernel

theorem cert_1001 : ∀ b3 b4 b5 b6 : Bool, certOK true false false true b3 b4 b5 b6 = true := by
  decide +kernel

theorem cert_1010 : ∀ b3 b4 b5 b6 : Bool, certOK true false true false b3 b4 b5 b6 = true := by
  decide +kernel

theorem cert_1011 : ∀ b3 b4 b5 b6 : Bool, certOK true false true true b3 b4 b5 b6 = true := by
  decide +kernel

theorem cert_1100 : ∀ b3 b4 b5 b6 : Bool, certOK true true false false b3 b4 b5 b6 = true := by
  decide +kernel

theorem cert_1101 : ∀ b3 b4 b5 b6 : Bool, certOK true true false true b3 b4 b5 b6 = true := by
  decide +kernel

theorem cert_1110 : ∀ b3 b4 b5 b6 : Bool, certOK true true true false b3 b4 b5 b6 = true := by
  decide +kernel

theorem cert_1111 : ∀ b3 b4 b5 b6 : Bool, certOK true true true true b3 b4 b5 b6 = true := by
  decide +kernel

/-- **The finite certificate**, checked by the kernel: both feeder phases and all seven free start bits. -/
theorem cert : ∀ p b0 b1 b2 b3 b4 b5 b6 : Bool, certOK p b0 b1 b2 b3 b4 b5 b6 = true
  | false, false, false, false, b3, b4, b5, b6 => cert_0000 b3 b4 b5 b6
  | false, false, false, true, b3, b4, b5, b6 => cert_0001 b3 b4 b5 b6
  | false, false, true, false, b3, b4, b5, b6 => cert_0010 b3 b4 b5 b6
  | false, false, true, true, b3, b4, b5, b6 => cert_0011 b3 b4 b5 b6
  | false, true, false, false, b3, b4, b5, b6 => cert_0100 b3 b4 b5 b6
  | false, true, false, true, b3, b4, b5, b6 => cert_0101 b3 b4 b5 b6
  | false, true, true, false, b3, b4, b5, b6 => cert_0110 b3 b4 b5 b6
  | false, true, true, true, b3, b4, b5, b6 => cert_0111 b3 b4 b5 b6
  | true, false, false, false, b3, b4, b5, b6 => cert_1000 b3 b4 b5 b6
  | true, false, false, true, b3, b4, b5, b6 => cert_1001 b3 b4 b5 b6
  | true, false, true, false, b3, b4, b5, b6 => cert_1010 b3 b4 b5 b6
  | true, false, true, true, b3, b4, b5, b6 => cert_1011 b3 b4 b5 b6
  | true, true, false, false, b3, b4, b5, b6 => cert_1100 b3 b4 b5 b6
  | true, true, false, true, b3, b4, b5, b6 => cert_1101 b3 b4 b5 b6
  | true, true, true, false, b3, b4, b5, b6 => cert_1110 b3 b4 b5 b6
  | true, true, true, true, b3, b4, b5, b6 => cert_1111 b3 b4 b5 b6

/-- **The universal start, profile form**: after two equal-phase alternating feeders, whatever the seven start
bits, the next diagonals have least periods `4, 8, 8, 16, 32, 32`, then `32` or `64`. -/
theorem universal_start_profiles (p : Bool) (bits : Nat → Bool) :
    LeastPer (E p bits 0) 4 ∧ LeastPer (E p bits 1) 8 ∧ LeastPer (E p bits 2) 8 ∧
      LeastPer (E p bits 3) 16 ∧ LeastPer (E p bits 4) 32 ∧ LeastPer (E p bits 5) 32 ∧
      (LeastPer (E p bits 6) 32 ∨ LeastPer (E p bits 6) 64) := by
  let b' := bitsOf (bits 0) (bits 1) (bits 2) (bits 3) (bits 4) (bits 5) (bits 6)
  have hb : ∀ i, i ≤ 6 → bits i = b' i := by
    intro i hi
    obtain _ | _ | _ | _ | _ | _ | _ | i := i <;> first | rfl | omega
  have heq : ∀ k, k ≤ 6 → E p bits k = E p b' k := by
    intro k hk
    match k, hk with
    | 0, _ => exact (E_congr p bits b' 0 (fun i hi => hb i (by omega))).1
    | k + 1, hk => exact (E_congr p bits b' k (fun i hi => hb i (by omega))).2
  have hc := cert p (bits 0) (bits 1) (bits 2) (bits 3) (bits 4) (bits 5) (bits 6)
  unfold certOK at hc
  simp only [Bool.and_eq_true, Bool.or_eq_true] at hc
  obtain ⟨⟨⟨⟨⟨⟨h0, h1⟩, h2⟩, h3⟩, h4⟩, h5⟩, h6⟩ := hc
  rw [heq 0 (by omega), heq 1 (by omega), heq 2 (by omega), heq 3 (by omega), heq 4 (by omega),
    heq 5 (by omega), heq 6 (by omega)]
  refine ⟨leastOK_spec p b' 0 (by omega) 4 (by omega) h0, leastOK_spec p b' 1 (by omega) 8 (by omega) h1,
    leastOK_spec p b' 2 (by omega) 8 (by omega) h2, leastOK_spec p b' 3 (by omega) 16 (by omega) h3,
    leastOK_spec p b' 4 (by omega) 32 (by omega) h4, leastOK_spec p b' 5 (by omega) 32 (by omega) h5, ?_⟩
  rcases h6 with h6 | h6
  · exact Or.inl (leastOK_spec p b' 6 (by omega) 32 (by omega) h6)
  · exact Or.inr (leastOK_spec p b' 6 (by omega) 64 (by omega) h6)

/-! ### Actual right diagonals -/

/-- Right diagonal `j` of the kit's evolution: `D j t = x_t (t - j)`. -/
def rightDiag (x : Int → Bool) (j : Int) (t : Nat) : Bool := Rule30Realization.evol x t ((t : Int) - j)

theorem rightDiag_step (x : Int → Bool) (j : Int) (t : Nat) :
    rightDiag x j (t + 1) = xor (rightDiag x j t) (rightDiag x (j - 1) t || rightDiag x (j - 2) t) := by
  unfold rightDiag
  show Rule30Jen.rule (Rule30Realization.evol x t (((t + 1 : Nat) : Int) - j - 1))
      (Rule30Realization.evol x t (((t + 1 : Nat) : Int) - j))
      (Rule30Realization.evol x t (((t + 1 : Nat) : Int) - j + 1)) = _
  unfold Rule30Jen.rule
  congr 1
  · congr 1; omega
  · congr 1 <;> congr 1 <;> omega

/-- With the rightmost black cell at `0`, the right edge moves at light speed. -/
theorem edge (x : Int → Bool) (h0 : x 0 = true) (hr : ∀ i : Int, 0 < i → x i = false) :
    ∀ t : Nat, (∀ i : Int, (t : Int) < i → Rule30Realization.evol x t i = false) ∧
      Rule30Realization.evol x t (t : Int) = true := by
  intro t
  induction t with
  | zero => exact ⟨fun i hi => hr i (by omega), h0⟩
  | succ t ih =>
    obtain ⟨hw, hb⟩ := ih
    refine ⟨fun i hi => ?_, ?_⟩
    · show Rule30Jen.rule (Rule30Realization.evol x t (i - 1)) (Rule30Realization.evol x t i)
        (Rule30Realization.evol x t (i + 1)) = false
      unfold Rule30Jen.rule
      rw [hw (i - 1) (by omega), hw i (by omega), hw (i + 1) (by omega)]; rfl
    · show Rule30Jen.rule (Rule30Realization.evol x t (((t + 1 : Nat) : Int) - 1))
        (Rule30Realization.evol x t ((t + 1 : Nat) : Int)) (Rule30Realization.evol x t (((t + 1 : Nat) : Int) + 1)) = true
      unfold Rule30Jen.rule
      rw [show ((t + 1 : Nat) : Int) - 1 = (t : Int) by omega, hb, hw _ (by omega), hw _ (by omega)]; rfl

/-- **The universal start for actual diagonals.** Let the rightmost black cell be at `0`, write `s d = x (-d)`,
and let `m ≥ 2` be the first index with `s m = s (m-1)`. Then from `j = m + 1` the right diagonals have least
periods `4, 8, 8, 16, 32, 32`, then `32` or `64`. -/
theorem universal_start (x : Int → Bool) (h0 : x 0 = true) (hr : ∀ i : Int, 0 < i → x i = false)
    (m : Nat) (hm : 2 ≤ m) (heq : x (-(m : Int)) = x (-((m : Int) - 1)))
    (hfirst : ∀ d : Nat, 2 ≤ d → d < m → x (-(d : Int)) ≠ x (-((d : Int) - 1))) :
    LeastPer (rightDiag x (m + 1)) 4 ∧ LeastPer (rightDiag x (m + 2)) 8 ∧ LeastPer (rightDiag x (m + 3)) 8 ∧
      LeastPer (rightDiag x (m + 4)) 16 ∧ LeastPer (rightDiag x (m + 5)) 32 ∧
      LeastPer (rightDiag x (m + 6)) 32 ∧
      (LeastPer (rightDiag x (m + 7)) 32 ∨ LeastPer (rightDiag x (m + 7)) 64) := by
  have hE := edge x h0 hr
  have D0 : ∀ t, rightDiag x 0 t = true := fun t => by
    unfold rightDiag; rw [Int.sub_zero]; exact (hE t).2
  have Dm1 : ∀ t, rightDiag x (-1) t = false := fun t => (hE t).1 _ (by omega)
  have Dstart : ∀ d : Int, rightDiag x d 0 = x (-d) := fun d => by
    unfold rightDiag; simp [Rule30Realization.evol]
  -- every diagonal up to `m` alternates with its start phase
  have alt_of : ∀ (d : Int) (q : Bool), (∀ t, (rightDiag x (d - 1) t || rightDiag x (d - 2) t) = true) →
      rightDiag x d 0 = q → ∀ t, rightDiag x d t = alt q t := by
    intro d q hor h0q t
    induction t with
    | zero => rw [h0q]; unfold alt; simp
    | succ t ih => rw [rightDiag_step, hor t, ih, alt_succ]; cases alt q t <;> rfl
  have alt_up : ∀ n : Nat, 1 ≤ n → n ≤ m → (∀ t, rightDiag x n t = alt (x (-(n : Int))) t) ∧
      (n ≥ 2 → ∀ t, rightDiag x (n - 1 : Nat) t = alt (x (-((n - 1 : Nat) : Int))) t) := by
    intro n
    induction n with
    | zero => intro h; omega
    | succ n ih =>
      intro _ hn
      by_cases hn1 : n = 0
      · subst hn1
        refine ⟨alt_of 1 _ (fun t => by rw [show (1 : Int) - 1 = 0 by omega, D0]; rfl) (Dstart 1), fun h => by omega⟩
      · have ih' := ih (by omega) (by omega)
        refine ⟨?_, fun _ => by simpa using ih'.1⟩
        by_cases hn2 : n = 1
        · subst hn2
          exact alt_of 2 _ (fun t => by
            rw [show (2 : Int) - 1 = 1 by omega, show (2 : Int) - 2 = 0 by omega, D0]; simp) (Dstart 2)
        · have hprev := ih'.2 (by omega)
          have hne := hfirst n (by omega) (by omega)
          apply alt_of _ _ _ (Dstart _)
          intro t
          rw [show ((n + 1 : Nat) : Int) - 1 = (n : Int) by omega, ih'.1 t,
            show ((n + 1 : Nat) : Int) - 2 = ((n - 1 : Nat) : Int) by omega, hprev t]
          have hph : x (-((n - 1 : Nat) : Int)) = !x (-(n : Int)) := by
            have : x (-((n : Int) - 1)) = x (-((n - 1 : Nat) : Int)) := by
              rw [show ((n : Int) - 1) = ((n - 1 : Nat) : Int) by omega]
            rw [← this]
            cases h1 : x (-(n : Int)) <;> cases h2 : x (-((n : Int) - 1)) <;> simp_all
          rw [hph, alt_not]; cases alt (x (-(n : Int))) t <;> rfl
  obtain ⟨hDm, hDm1⟩ := alt_up m (by omega) (Nat.le_refl m)
  have hDm1' := hDm1 hm
  -- the two feeders have equal phase p
  have hph : x (-((m - 1 : Nat) : Int)) = x (-(m : Int)) := by
    rw [heq, show ((m - 1 : Nat) : Int) = (m : Int) - 1 by omega]
  let p := x (-(m : Int))
  let bits : Nat → Bool := fun k => x (-((m + 1 + k : Nat) : Int))
  -- identify the diagonals after `m` with `E p bits`
  have ident : ∀ k, rightDiag x ((m + 1 + k : Nat) : Int) = E p bits k ∧
      rightDiag x ((m + 1 + (k + 1) : Nat) : Int) = E p bits (k + 1) := by
    intro k
    induction k with
    | zero =>
      have e0 : rightDiag x ((m + 1 + 0 : Nat) : Int) = E p bits 0 := by
        rw [run_unique (fun t => rightDiag_step x _ t)]
        show run _ _ = run (bits 0) (fun t => alt p t || alt p t)
        congr 1
        funext t
        rw [show ((m + 1 + 0 : Nat) : Int) - 1 = (m : Int) by omega, hDm t,
          show ((m + 1 + 0 : Nat) : Int) - 2 = ((m - 1 : Nat) : Int) by omega, hDm1' t, hph]
      refine ⟨e0, ?_⟩
      rw [run_unique (fun t => rightDiag_step x _ t)]
      show run _ _ = run (bits 1) (fun t => E p bits 0 t || alt p t)
      congr 1
      funext t
      rw [show ((m + 1 + (0 + 1) : Nat) : Int) - 1 = ((m + 1 + 0 : Nat) : Int) by omega, e0,
        show ((m + 1 + (0 + 1) : Nat) : Int) - 2 = (m : Int) by omega, hDm t]
    | succ k ih =>
      refine ⟨ih.2, ?_⟩
      rw [run_unique (fun t => rightDiag_step x _ t)]
      show run _ _ = run (bits (k + 2)) (fun t => E p bits (k + 1) t || E p bits k t)
      congr 1
      funext t
      rw [show ((m + 1 + (k + 1 + 1) : Nat) : Int) - 1 = ((m + 1 + (k + 1) : Nat) : Int) by omega, ih.2,
        show ((m + 1 + (k + 1 + 1) : Nat) : Int) - 2 = ((m + 1 + k : Nat) : Int) by omega, ih.1]
  have hu := universal_start_profiles p bits
  have i0 := (ident 0).1; have i1 := (ident 1).1; have i2 := (ident 2).1; have i3 := (ident 3).1
  have i4 := (ident 4).1; have i5 := (ident 5).1; have i6 := (ident 6).1
  rw [show ((m + 1 : Nat) : Int) = ((m + 1 + 0 : Nat) : Int) by rfl] at *
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · rw [show ((m : Int) + 1) = ((m + 1 + 0 : Nat) : Int) by omega, i0]; exact hu.1
  · rw [show ((m : Int) + 2) = ((m + 1 + 1 : Nat) : Int) by omega, i1]; exact hu.2.1
  · rw [show ((m : Int) + 3) = ((m + 1 + 2 : Nat) : Int) by omega, i2]; exact hu.2.2.1
  · rw [show ((m : Int) + 4) = ((m + 1 + 3 : Nat) : Int) by omega, i3]; exact hu.2.2.2.1
  · rw [show ((m : Int) + 5) = ((m + 1 + 4 : Nat) : Int) by omega, i4]; exact hu.2.2.2.2.1
  · rw [show ((m : Int) + 6) = ((m + 1 + 5 : Nat) : Int) by omega, i5]; exact hu.2.2.2.2.2.1
  · rw [show ((m : Int) + 7) = ((m + 1 + 6 : Nat) : Int) by omega, i6]; exact hu.2.2.2.2.2.2

/-- The least index at which a decidable property first holds, from a bound. -/
theorem least_exists (P : Nat → Prop) [DecidablePred P] :
    ∀ n, (∃ d, 2 ≤ d ∧ d ≤ n ∧ P d) → ∃ m, 2 ≤ m ∧ P m ∧ ∀ d, 2 ≤ d → d < m → ¬ P d := by
  intro n
  induction n with
  | zero => rintro ⟨d, h1, h2, _⟩; omega
  | succ n ih =>
    rintro ⟨d, h1, h2, hd⟩
    by_cases h : ∃ d, 2 ≤ d ∧ d ≤ n ∧ P d
    · exact ih h
    · exact ⟨d, h1, hd, fun e he1 he2 hPe => h ⟨e, he1, by omega, hPe⟩⟩

/-- **Every finite seed**: a finitely supported start with rightmost black cell at `0` has a first equal pair, and
the universal start follows. -/
theorem universal_start_finite (x : Int → Bool) (h0 : x 0 = true) (hr : ∀ i : Int, 0 < i → x i = false)
    (L : Nat) (hl : ∀ i : Int, i < -(L : Int) → x i = false) :
    ∃ m : Nat, 2 ≤ m ∧ LeastPer (rightDiag x (m + 1)) 4 ∧ LeastPer (rightDiag x (m + 2)) 8 ∧
      LeastPer (rightDiag x (m + 3)) 8 ∧ LeastPer (rightDiag x (m + 4)) 16 ∧
      LeastPer (rightDiag x (m + 5)) 32 ∧ LeastPer (rightDiag x (m + 6)) 32 ∧
      (LeastPer (rightDiag x (m + 7)) 32 ∨ LeastPer (rightDiag x (m + 7)) 64) := by
  obtain ⟨m, hm, heq, hfirst⟩ := least_exists (fun d => x (-(d : Int)) = x (-((d : Int) - 1))) (L + 2)
    ⟨L + 2, by omega, Nat.le_refl _, by
      show x (-((L + 2 : Nat) : Int)) = x (-(((L + 2 : Nat) : Int) - 1))
      rw [hl _ (by omega), hl _ (by omega)]⟩
  exact ⟨m, hm, universal_start x h0 hr m hm heq hfirst⟩

end Ruliology.CellularAutomata.Rule30UniversalStart
