module

public import Ruliology.CellularAutomata.Rule30GateTrap

/-!
# Locks of period five and seven beside the alternating column

Drive a right half `R` with the alternating column, black at the even ticks
(`Rule30PeriodTwoCoupled.altCol`). Column `1` at the white ticks is `Rule30PeriodTwoSideways.u R`, and
the sideways row `Psi R` is infinite whenever `u R` is eventually periodic
(`Rule30PeriodTwoSideways.not_finSupp_Psi_of_eventuallyPeriodic`). So `CQ01` holds for every right half
whose column `1` locks into a period.

A **lock** of width `W` and period `p` is a list of `p` classes of windows (the columns `1..W` at an odd
tick) such that every window of class `k` reads the `k`-th letter of a word in column `1`, and two ticks
later, for every value of the cells of columns `W + 1` and `W + 2` at the odd tick, the window is in
class `k + 1` (modulo `p`). The two outer cells are all a window cannot see: two ticks later columns
`1..W` depend on nothing else (`winW_dstep`). This module proves, for any width and period:

* `lock_forever`: a window that is in class `k` at an odd tick `t0` is in class `k + n` at `t0 + 2 n`;
* `u_of_lock`, `u_eventuallyPeriodic_of_lock`: so `u R` repeats the word from `t0` on;
* `not_finSupp_Psi_of_lock`: so `Psi R` has infinitely many black cells, for every `R`, finite or not.

Three locks are checked by the kernel (`lock5_ok`, `lock7_ok`, `lock7b_ok`):

* `lock5`: width `34`, `25` windows in `5` classes, column `1` reads `10000`;
* `lock7`: width `30`, `66` windows in `7` classes, column `1` reads `0101000`;
* `lock7b`: width `45`, `33` windows in `7` classes, column `1` reads `0010100`.

Each is entered: the right half `28998` enters `lock5` at tick `15`, `1891` enters `lock7` at tick `27`,
and `3793493` enters `lock7b` at tick `29` (`lock5_entry`, `lock7_entry`, `lock7b_entry`, by `evolve`).
The window at an odd tick `t0` depends only on the cells `1..W + t0` of the start, so every right half
with the same first `W + t0` cells enters too (`winW_prefix`): `CQ01_lock5_family`,
`CQ01_lock7_family`, `CQ01_lock7b_family` give `CQ01` for each such `R`, whatever its later cells.

`lock5` lies inside the gate trap of `Rule30GateTrap`: the first `16` columns of each of its windows
are a window of the trap (`lock5_win_trap`). In the trap the gaps between black cells of `u R` are `3`
or `5`, and `CQ01` there is conditional on `Q01Gap`; inside `lock5` every gap is `5`, and `CQ01` holds
without that hypothesis.

Nothing here decides `CQ01`, `CQ01Empty` or Problem 1.
-/

@[expose] public section

-- Sequential elaboration: the kernel checks would otherwise run in parallel and stack their memory.
set_option Elab.async false

namespace Ruliology.CellularAutomata
namespace Rule30SidewaysLocks

open Rule30StripCertificates Rule30Ether Rule30PeriodTwoCoupled Rule30PeriodTwoSideways Rule30Jen

/-! ## Windows and the double step -/

/-- The window of width `W`: the columns `1..W` of the right half `R` driven by the alternating
column, at time `t`. -/
def winW (W : Nat) (R : Nat → Bool) (t : Nat) : List Bool := rowOf (drv altCol R) t 0 W

/-- The double step from an odd tick: column `0` is white, then black, and `x1`, `x2` are the cells of
columns `W + 1` and `W + 2` at the odd tick. -/
def dstep (s : List Bool) (x1 x2 : Bool) : List Bool := lin3 (true :: lin3 (false :: (s ++ [x1, x2])))

/-- From an odd tick, the window two ticks later is the double step of the window, with the two cells
beyond it. -/
theorem winW_dstep (W : Nat) (R : Nat → Bool) (t : Nat) (ht : t % 2 = 1) :
    winW W R (t + 2) = dstep (winW W R t) (drv altCol R t (W + 1)) (drv altCol R t (W + 2)) := by
  have hF := drv_isR30 altCol R
  have h2 := rowOf_succ hF (t + 1) 0 W
  have h1 := rowOf_succ hF t 0 (W + 1)
  rw [drv_col0] at h1 h2
  have a1 : altCol t = false := by unfold altCol; simp [ht]
  have a2 : altCol (t + 1) = true := by unfold altCol; simp; omega
  rw [a1] at h1
  rw [a2] at h2
  have e2 : rowOf (drv altCol R) (t + 1) 0 W ++ [drv altCol R (t + 1) (0 + W + 1)] =
      rowOf (drv altCol R) (t + 1) 0 (W + 1) := by
    unfold rowOf; rw [seg_succ]
  have e1 : rowOf (drv altCol R) t 0 (W + 1) =
      rowOf (drv altCol R) t 0 W ++ [drv altCol R t (0 + W + 1)] := by
    unfold rowOf; rw [seg_succ]
  unfold winW dstep
  rw [show t + 2 = t + 1 + 1 by omega, h2, e2, h1, e1, show 0 + W + 1 = W + 1 by omega,
    show 0 + (W + 1) + 1 = W + 2 by omega, List.append_assoc, List.singleton_append]

/-- The window coded by `n`: bit `i` of `n` is column `i + 1`. -/
def decodeW (W n : Nat) : List Bool := seg (fun i => n.testBit i) W

/-! ## Locks -/

/-- Class `k` of a lock of width `W`, decoded. -/
def cls (W : Nat) (codes : List (List Nat)) (k : Nat) : List (List Bool) :=
  (codes.getD k []).map (decodeW W)

/-- Every double step from `w` is in `L`. -/
def succIn (L : List (List Bool)) (w : List Bool) : Bool :=
  L.contains (dstep w false false) && L.contains (dstep w false true) &&
    L.contains (dstep w true false) && L.contains (dstep w true true)

/-- **The lock check.** Every window of class `k` reads `word.getD k false` in column `1`, and every
double step from it lands in class `k + 1` modulo `p`. -/
def lockCheck (W p : Nat) (word : List Bool) (codes : List (List Nat)) : Bool :=
  (List.range p).all fun k => (cls W codes k).all fun w =>
    (w.headD false == word.getD k false) && succIn (cls W codes ((k + 1) % p)) w

theorem succIn_spec {L : List (List Bool)} {w : List Bool} (h : succIn L w = true) (x1 x2 : Bool) :
    dstep w x1 x2 ∈ L := by
  unfold succIn at h
  simp only [Bool.and_eq_true] at h
  obtain ⟨⟨⟨h1, h2⟩, h3⟩, h4⟩ := h
  cases x1 <;> cases x2
  · exact List.contains_iff_mem.1 h1
  · exact List.contains_iff_mem.1 h2
  · exact List.contains_iff_mem.1 h3
  · exact List.contains_iff_mem.1 h4

theorem lockCheck_spec {W p : Nat} {word : List Bool} {codes : List (List Nat)}
    (hc : lockCheck W p word codes = true) {k : Nat} (hk : k < p) {w : List Bool}
    (hw : w ∈ cls W codes k) :
    w.headD false = word.getD k false ∧ succIn (cls W codes ((k + 1) % p)) w = true := by
  unfold lockCheck at hc
  have h1 := List.all_eq_true.1 hc k (List.mem_range.2 hk)
  have h2 := List.all_eq_true.1 h1 w hw
  simp only [Bool.and_eq_true, beq_iff_eq] at h2
  exact h2

/-- **A window in a lock stays in it**, moving one class per double step. -/
theorem lock_forever {W p : Nat} {word : List Bool} {codes : List (List Nat)}
    (hc : lockCheck W p word codes = true) (hp : 0 < p) (R : Nat → Bool) {t0 k : Nat}
    (h0 : t0 % 2 = 1) (hk : k < p) (hw : winW W R t0 ∈ cls W codes k) :
    ∀ n, winW W R (t0 + 2 * n) ∈ cls W codes ((k + n) % p) := by
  intro n
  induction n with
  | zero => rw [Nat.mul_zero, Nat.add_zero, Nat.add_zero, Nat.mod_eq_of_lt hk]; exact hw
  | succ n ih =>
    have hs := (lockCheck_spec hc (Nat.mod_lt _ hp) ih).2
    rw [show t0 + 2 * (n + 1) = t0 + 2 * n + 2 by omega, winW_dstep W R _ (by omega)]
    have e : ((k + n) % p + 1) % p = (k + (n + 1)) % p := by
      rw [Nat.add_mod, Nat.mod_mod, ← Nat.add_mod, Nat.add_assoc]
    rw [← e]
    exact succIn_spec hs _ _

theorem winW_head (V : Nat) (R : Nat → Bool) (t : Nat) :
    (winW (V + 1) R t).headD false = drv altCol R t 1 := rowOf_head _ t 0 V

/-- **Column `1` repeats the word of the lock.** -/
theorem u_of_lock {V p : Nat} {word : List Bool} {codes : List (List Nat)}
    (hc : lockCheck (V + 1) p word codes = true) (hp : 0 < p) (R : Nat → Bool) {s0 k : Nat}
    (hk : k < p) (hw : winW (V + 1) R (2 * s0 + 1) ∈ cls (V + 1) codes k) (n : Nat) :
    u R (s0 + n) = word.getD ((k + n) % p) false := by
  have h := lock_forever hc hp R (by omega) hk hw n
  have hh := (lockCheck_spec hc (Nat.mod_lt _ hp) h).1
  rw [winW_head] at hh
  rw [← hh]
  show drv altCol R (2 * (s0 + n) + 1) 1 = drv altCol R (2 * s0 + 1 + 2 * n) 1
  rw [show 2 * (s0 + n) + 1 = 2 * s0 + 1 + 2 * n by omega]

theorem u_eventuallyPeriodic_of_lock {V p : Nat} {word : List Bool} {codes : List (List Nat)}
    (hc : lockCheck (V + 1) p word codes = true) (hp : 0 < p) (R : Nat → Bool) {s0 k : Nat}
    (hk : k < p) (hw : winW (V + 1) R (2 * s0 + 1) ∈ cls (V + 1) codes k) :
    EventuallyPeriodic (u R) := by
  refine ⟨s0, p, hp, fun t ht => ?_⟩
  obtain ⟨n, rfl⟩ : ∃ n, t = s0 + n := ⟨t - s0, by omega⟩
  rw [show s0 + n + p = s0 + (n + p) by omega, u_of_lock hc hp R hk hw, u_of_lock hc hp R hk hw,
    show k + (n + p) = k + n + p by omega, Nat.add_mod_right]

/-- **A lock gives `CQ01` for every right half that enters it.** -/
theorem not_finSupp_Psi_of_lock {V p : Nat} {word : List Bool} {codes : List (List Nat)}
    (hc : lockCheck (V + 1) p word codes = true) (hp : 0 < p) (R : Nat → Bool) {s0 k : Nat}
    (hk : k < p) (hw : winW (V + 1) R (2 * s0 + 1) ∈ cls (V + 1) codes k) :
    ¬ Rule30ZeroBoundary.FinSupp (Psi R) :=
  not_finSupp_Psi_of_eventuallyPeriodic R (u_eventuallyPeriodic_of_lock hc hp R hk hw)

/-! ## Entry, and prefix families -/

theorem seg_congr : ∀ (m : Nat) {f g : Nat → Bool}, (∀ i, i < m → f i = g i) → seg f m = seg g m
  | 0, _, _, _ => rfl
  | m + 1, f, g, h => by
    show f 0 :: seg (fun i => f (i + 1)) m = g 0 :: seg (fun i => g (i + 1)) m
    rw [h 0 (by omega), seg_congr m (fun i hi => h (i + 1) (by omega))]

/-- The cells `1..m` of the start of a right half that reads `c` there. -/
theorem rowOf_zero_prefix {R : Nat → Bool} {c m : Nat} (h : ∀ i, i < m → R (i + 1) = c.testBit i) :
    rowOf (drv altCol R) 0 0 m = decodeW m c := by
  unfold rowOf decodeW
  apply seg_congr m
  intro i hi
  rw [drv_init _ _ _ (by omega), Nat.zero_add]
  exact h i hi

/-- **The window at tick `t0` is `evolve` of the first `W + t0` cells**, so every right half with the
same first `W + t0` cells has the same window. -/
theorem winW_prefix {R : Nat → Bool} {W c t0 : Nat}
    (h : ∀ i, i < W + t0 → R (i + 1) = c.testBit i) :
    winW W R t0 = Rule30GateTrap.evolve 0 t0 (decodeW (W + t0) c) := by
  have e := Rule30GateTrap.rowOf_evolve R t0 0 W
  rw [Nat.zero_add, rowOf_zero_prefix h] at e
  exact e

/-- The right half whose cell `p` is bit `p - 1` of `c`. -/
def rh (c : Nat) : Nat → Bool := Rule30ZeroBoundary.IntegerForm.rowOfNat c

theorem rh_prefix (c m : Nat) : ∀ i, i < m → rh c (i + 1) = c.testBit i := fun _ _ => rfl

/-! ## The three locks -/

/-- The windows of `lock5`, as codes in 5 classes (bit `i` is column `i + 1`). -/
def lock5Codes : List (List Nat) := [
  [547958887, 2695442535, 6990409831, 11285377127, 15580344423],
  [2594196878, 6889164174, 11184131470, 15479098766],
  [714676060, 5009643356, 9304610652, 13599577948],
  [706780010, 2854263658, 5001747306, 9296714602, 11444198250, 15739165546],
  [689582056, 2837065704, 4984549352, 7132033000, 11427000296, 15721967592]
]

/-- The windows of `lock7`, as codes in 7 classes (bit `i` is column `i + 1`). -/
def lock7Codes : List (List Nat) := [
  [46898496, 181116224, 315333952, 583769408, 717987136, 852204864, 986422592],
  [59587889, 193805617, 328023345, 462241073, 596458801, 730676529, 999111985],
  [122973256, 223636552, 257190984, 391408712, 492072008, 760507464, 794061896, 1028942920, 1062497352],
  [55753223, 223525383, 357743111, 458406407, 525515271, 592624135, 760396295, 793950727, 861059591,
   894614023, 995277319, 1028831751, 1062386183],
  [54712734, 88267166, 222484894, 356702622, 524474782, 591583646, 625138078, 759355806, 792910238,
   860019102, 893573534, 1027791262, 1061345694],
  [54260276, 87814708, 222032436, 356250164, 591131188, 624685620, 758903348, 859566644, 893121076, 1027338804],
  [75243858, 209461586, 343679314, 612114770, 746332498, 880550226, 1014767954]
]

/-- The windows of `lock7b`, as codes in 7 classes (bit `i` is column `i + 1`). -/
def lock7bCodes : List (List Nat) := [
  [1372794518866, 5770841029970, 14566934052178, 23363027074386, 32159120096594],
  [4817275456832, 13613368479040, 22409461501248, 31205554523456],
  [2878366659889, 11674459682097, 20470552704305, 29266645726513],
  [2427647947848, 11223740970056, 20019833992264, 28815927014472],
  [1462412784135, 10258505806343, 19054598828551, 27850691850759],
  [1455023374750, 5853069885854, 10251116396958, 19047209419166, 23445255930270, 32241348952478],
  [1390110553652, 5788157064756, 10186203575860, 14584250086964, 23380343109172, 32176436131380]
]

/-- Column `1` of the classes of `lock5`. -/
def word5 : List Bool := [true, false, false, false, false]
/-- Column `1` of the classes of `lock7`. -/
def word7 : List Bool := [false, true, false, true, false, false, false]
/-- Column `1` of the classes of `lock7b`. -/
def word7b : List Bool := [false, false, true, false, true, false, false]

theorem lock5_ok : lockCheck 34 5 word5 lock5Codes = true := by decide +kernel
theorem lock7_ok : lockCheck 30 7 word7 lock7Codes = true := by decide +kernel
theorem lock7b_ok : lockCheck 45 7 word7b lock7bCodes = true := by decide +kernel

theorem lock5_entry : winW 34 (rh 28998) 15 ∈ cls 34 lock5Codes 0 := by
  rw [winW_prefix (rh_prefix 28998 _)]; decide +kernel
theorem lock7_entry : winW 30 (rh 1891) 27 ∈ cls 30 lock7Codes 4 := by
  rw [winW_prefix (rh_prefix 1891 _)]; decide +kernel
theorem lock7b_entry : winW 45 (rh 3793493) 29 ∈ cls 45 lock7bCodes 6 := by
  rw [winW_prefix (rh_prefix 3793493 _)]; decide +kernel

/-- **`CQ01` for every right half that starts like `28998`**: if the cells `1..49` of `R` are those of
`28998`, then `u R` has period `5` from step `7` on and `Psi R` is infinite. -/
theorem CQ01_lock5_family {R : Nat → Bool} (h : ∀ i, i < 49 → R (i + 1) = (28998 : Nat).testBit i) :
    ¬ Rule30ZeroBoundary.FinSupp (Psi R) := by
  have hw : winW 34 R (2 * 7 + 1) ∈ cls 34 lock5Codes 0 := by
    rw [winW_prefix h, ← winW_prefix (rh_prefix 28998 _)]; exact lock5_entry
  exact not_finSupp_Psi_of_lock (V := 33) lock5_ok (by decide) R (by decide) hw

/-- **`CQ01` for every right half that starts like `1891`** (cells `1..57`): period `7`. -/
theorem CQ01_lock7_family {R : Nat → Bool} (h : ∀ i, i < 57 → R (i + 1) = (1891 : Nat).testBit i) :
    ¬ Rule30ZeroBoundary.FinSupp (Psi R) := by
  have hw : winW 30 R (2 * 13 + 1) ∈ cls 30 lock7Codes 4 := by
    rw [winW_prefix h, ← winW_prefix (rh_prefix 1891 _)]; exact lock7_entry
  exact not_finSupp_Psi_of_lock (V := 29) lock7_ok (by decide) R (by decide) hw

/-- **`CQ01` for every right half that starts like `3793493`** (cells `1..74`): period `7`. -/
theorem CQ01_lock7b_family {R : Nat → Bool}
    (h : ∀ i, i < 74 → R (i + 1) = (3793493 : Nat).testBit i) :
    ¬ Rule30ZeroBoundary.FinSupp (Psi R) := by
  have hw : winW 45 R (2 * 14 + 1) ∈ cls 45 lock7bCodes 6 := by
    rw [winW_prefix h, ← winW_prefix (rh_prefix 3793493 _)]; exact lock7b_entry
  exact not_finSupp_Psi_of_lock (V := 44) lock7b_ok (by decide) R (by decide) hw

theorem seg_take : ∀ (m n : Nat) (f : Nat → Bool), n ≤ m → (seg f m).take n = seg f n
  | _, 0, _, _ => rfl
  | 0, _ + 1, _, h => absurd h (by omega)
  | m + 1, n + 1, f, h => by
    show f 0 :: (seg (fun i => f (i + 1)) m).take n = f 0 :: seg (fun i => f (i + 1)) n
    rw [seg_take m n _ (by omega)]

/-- The first `16` columns of every window of `lock5` are a window of the gate trap. -/
theorem lock5_trap_check : (List.range 5).all (fun k => (cls 34 lock5Codes k).all fun w =>
    Rule30GateTrap.inM (Rule30GateTrap.mask Rule30GateTrap.trap) (w.take 16)) = true := by
  decide +kernel

/-- **`lock5` lies in the gate trap**: a right half whose window is in `lock5` has its gate-trap window in
the trap. -/
theorem lock5_win_trap {R : Nat → Bool} {t k : Nat} (hk : k < 5) (hw : winW 34 R t ∈ cls 34 lock5Codes k) :
    Rule30GateTrap.win R t ∈ Rule30GateTrap.trap := by
  have h := List.all_eq_true.1 (List.all_eq_true.1 lock5_trap_check k (List.mem_range.2 hk)) _ hw
  have e : (winW 34 R t).take 16 = Rule30GateTrap.win R t := by
    unfold winW Rule30GateTrap.win rowOf
    exact seg_take 34 16 _ (by omega)
  rw [e] at h
  exact Rule30GateTrap.mem_of_inM (Rule30GateTrap.win_length R t) h

/-- The witnesses themselves. -/
theorem CQ01_28998 : ¬ Rule30ZeroBoundary.FinSupp (Psi (rh 28998)) :=
  CQ01_lock5_family (rh_prefix 28998 _)
theorem CQ01_1891 : ¬ Rule30ZeroBoundary.FinSupp (Psi (rh 1891)) :=
  CQ01_lock7_family (rh_prefix 1891 _)
theorem CQ01_3793493 : ¬ Rule30ZeroBoundary.FinSupp (Psi (rh 3793493)) :=
  CQ01_lock7b_family (rh_prefix 3793493 _)

/-- `u (rh 28998)` reads `10000` from step `7` on. -/
theorem u_28998 (n : Nat) : u (rh 28998) (7 + n) = word5.getD (n % 5) false := by
  have := u_of_lock (V := 33) lock5_ok (by decide) (rh 28998) (s0 := 7) (k := 0) (by decide)
    lock5_entry n
  rwa [Nat.zero_add] at this

end Rule30SidewaysLocks
end Ruliology.CellularAutomata
