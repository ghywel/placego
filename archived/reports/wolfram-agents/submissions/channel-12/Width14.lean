import Rule30PrizeKit
set_option linter.unusedSimpArgs false

/-!
# The channel bound, certified: how much a clocked center column lets its right neighbour say

**Partial result for Problem 1** (period 2, the kit's `Rule30ZeroBoundary.Q01` family). Suppose a
configuration `x : Int → Bool` has the clock on its center column, `evol x t 0 = decide (t % 2 = 1)`
for every `t` (`Clock`). Then the visible bits, column `1` at the even times, are constrained: for
every `n` the words `visFrom x 0 n = [evol x 0 1, evol x 2 1, …, evol x (2 (n - 1)) 1]` of all
clocked configurations lie in one set of at most `C (R / D) ^ n` words (`Cert.bound`,
`channel_bound_12`: `D = 10 ^ 9`, `R = 1195924139`, `C = 218` at width `12`), so they carry at most
`log₂ (R / D) = 0.2581` bits of information per visible bit, instead of `1`.

**The method.** The `M` cells right of the center form a window; under the clock, two time steps map
the window row `s` to `step2 s u v` with the two unknown cells beyond the window as inputs `u, v`.
The set of rows consistent with the visible bits read so far is an automaton state; the certificate
is the finite graph of these states (`succ12`) with a Collatz–Wielandt weight vector (`weights12`).
The kernel rebuilds every state as a bitset of `2 ^ M` bits from the graph alone, with the bit
operations GMP evaluates, checks that every edge is closed (`check`) and that the weights satisfy
`D (w j0 + w j1) ≤ R w i` (`wcheck`); `check_sound` and `weight_bound` turn the two Boolean facts
into the bound, and `win_succ`, `win_step2` tie the window to the kit's `evol`.

What the catalog has: `Q01` reduced to the zero-boundary left half, kernel-checked up to width 52;
nothing about the right neighbour of a clocked column. Nothing here decides `Q01`: the bound says
how constrained the right neighbour is, not that no configuration keeps the clock.
-/
namespace Rule30Submission
open Ruliology.CellularAutomata Rule30Realization Rule30Jen

/-! ## 1. The kernel computation -/

/-- Force `n` to a literal before continuing (the kernel reduces the major premise of `casesOn`). -/
noncomputable def force {α : Sort u} (n : Nat) (k : Nat → α) : α :=
  Nat.casesOn (motive := fun _ => α) n (k 0) (fun m => k (Nat.succ m))

theorem force_eq {α : Sort u} (n : Nat) (k : Nat → α) : force n k = k n := by
  cases n <;> rfl

/-- One rule 30 step on an `M`-cell window `s` (cell `p + 1` is bit `p`), clock bit `tv` on the left,
input `u` on the right; `mask = 2 ^ M - 1`. -/
def nxt (M mask s tv u : Nat) : Nat :=
  Nat.land (Nat.xor (Nat.lor (Nat.shiftLeft s 1) tv)
    (Nat.lor s (Nat.lor (Nat.shiftRight s 1) (Nat.shiftLeft u (Nat.sub M 1))))) mask

/-- The same step with the right input already shifted into place (`ut = u <<< (M - 1)`). -/
def nxtT (mask s tv ut : Nat) : Nat :=
  Nat.land (Nat.xor (Nat.lor (Nat.shiftLeft s 1) tv) (Nat.lor s (Nat.lor (Nat.shiftRight s 1) ut))) mask

theorem nxtT_eq (M mask s tv u : Nat) : nxtT mask s tv (Nat.shiftLeft u (Nat.sub M 1)) = nxt M mask s tv u := rfl

/-- Two steps: the clock white, then black. -/
def step2 (M mask s u v : Nat) : Nat := nxt M mask (nxt M mask s 0 u) 1 v

/-- The bitset of the four two-step images of `s`, sharing the first step (`top = 1 <<< (M - 1)`). -/
def img4 (mask top s : Nat) : Nat :=
  let s0 := nxtT mask s 0 0
  let s1 := nxtT mask s 0 top
  Nat.lor (Nat.lor (Nat.shiftLeft 1 (nxtT mask s0 1 0)) (Nat.shiftLeft 1 (nxtT mask s0 1 top)))
    (Nat.lor (Nat.shiftLeft 1 (nxtT mask s1 1 0)) (Nat.shiftLeft 1 (nxtT mask s1 1 top)))

/-- `⌊log₂ w⌋` for `0 < w < 2 ^ 64`, by six comparisons. -/
def pos64 (w : Nat) : Nat :=
  let a := cond (Nat.ble 4294967296 w) 32 0
  let w := Nat.shiftRight w a
  let b := cond (Nat.ble 65536 w) 16 0
  let w := Nat.shiftRight w b
  let c := cond (Nat.ble 256 w) 8 0
  let w := Nat.shiftRight w c
  let d := cond (Nat.ble 16 w) 4 0
  let w := Nat.shiftRight w d
  let e := cond (Nat.ble 4 w) 2 0
  let w := Nat.shiftRight w e
  let f := cond (Nat.ble 2 w) 1 0
  Nat.add (Nat.add (Nat.add a b) (Nat.add c d)) (Nat.add e f)

/-- The members of the word `w` at base `base`, highest first: the images of each go into the
half of `acc` selected by its low bit (`H = 2 ^ M`). -/
noncomputable def wordLoop (M mask H top : Nat) (fuel : Nat) : Nat → Nat → Nat → Nat :=
  Nat.rec (motive := fun _ => Nat → Nat → Nat → Nat) (fun _ _ acc => acc)
    (fun _ ih w base acc =>
      cond (Nat.beq w 0) acc
        (force (pos64 w) fun p => force (Nat.add base p) fun s =>
          force (Nat.xor w (Nat.shiftLeft 1 p)) fun w' =>
            force (Nat.lor acc (Nat.shiftLeft (img4 mask top s) (Nat.mul (Nat.land s 1) H))) fun acc' =>
              ih w' base acc'))
    fuel

/-- Sweep the words `nwords - 1, …, 0` of the bitset `B`. -/
noncomputable def sweep (M mask H top : Nat) (nwords : Nat) : Nat → Nat → Nat :=
  Nat.rec (motive := fun _ => Nat → Nat → Nat) (fun _ acc => acc)
    (fun k ih B acc =>
      force (Nat.land (Nat.shiftRight B (Nat.mul 64 k)) 18446744073709551615) fun w =>
        cond (Nat.beq w 0) (ih B acc)
          (force (wordLoop M mask H top 64 w (Nat.mul 64 k) acc) fun acc' => ih B acc'))
    nwords

/-- The two image bitsets of `B`, packed: label `0` in the low `2 ^ M` bits, label `1` above. -/
noncomputable def imageSets (M mask H : Nat) (B : Nat) : Nat :=
  sweep M mask H (Nat.shiftRight H 1) (Nat.shiftRight H 6) B 0

def DEAD : Nat := 1000000

/-- The bitset of state `j` among `cnt` discovered ones, newest first. -/
def at_ (bits : List Nat) (cnt j : Nat) : Nat := List.getD bits (Nat.sub (Nat.sub cnt 1) j) 0

/-- One edge to `j` with image `T`: a dead edge needs `T = 0`; a new state is recorded; an old one
must contain `T`. -/
noncomputable def edge (j T : Nat) (bits : List Nat) (cnt : Nat) : Option (List Nat × Nat) :=
  force T fun T =>
  cond (Nat.beq j DEAD) (cond (Nat.beq T 0) (some (bits, cnt)) none)
    (cond (Nat.beq j cnt) (some (T :: bits, Nat.succ cnt))
      (cond (Nat.blt j cnt)
        (cond (Nat.beq (Nat.land T (at_ bits cnt j)) T) (some (bits, cnt)) none)
        none))

/-- Run over the successor list in state order; at the end every discovered state was processed. -/
noncomputable def run (M mask H ALL : Nat) : List (Nat × Nat) → Nat → List Nat → Nat → Bool :=
  List.rec (motive := fun _ => Nat → List Nat → Nat → Bool) (fun i _ cnt => Nat.beq i cnt)
    (fun p _ ih i bits cnt =>
      cond (Nat.blt i cnt)
        (force (at_ bits cnt i) fun B =>
         force (imageSets M mask H B) fun T =>
         match edge p.1 (Nat.land T ALL) bits cnt with
         | none => false
         | some (bits1, cnt1) =>
           match edge p.2 (Nat.shiftRight T H) bits1 cnt1 with
           | none => false
           | some (bits2, cnt2) => force cnt2 fun cnt2 => ih (Nat.succ i) bits2 cnt2)
        false)

/-- The closure check for width `M`. -/
noncomputable def check (M : Nat) (succ : List (Nat × Nat)) : Bool :=
  force (Nat.shiftLeft 1 M) fun H => force (Nat.sub H 1) fun mask => force (Nat.sub (Nat.shiftLeft 1 H) 1) fun ALL =>
    run M mask H ALL succ 0 [ALL] 1

/-- The weight check: `D (w j0 + w j1) ≤ R w i` with `w DEAD = 0`, every `w i > 0`. -/
def wcheck (D R : Nat) (succ : List (Nat × Nat)) (w : List Nat) : Bool :=
  (List.range succ.length).all fun i =>
    let p := succ.getD i (DEAD, DEAD)
    let wi := w.getD i 0
    Nat.blt 0 wi && Nat.ble (Nat.mul D (Nat.add (w.getD p.1 0) (w.getD p.2 0))) (Nat.mul R wi)


/-! ## 2. What the computation establishes -/

/-- `s` is a member of the bitset `B`. -/
def Mem (B s : Nat) : Prop := Nat.testBit B s = true

theorem lor_eq' (a b : Nat) : Nat.lor a b = a ||| b := rfl
theorem land_eq' (a b : Nat) : Nat.land a b = a &&& b := rfl
theorem xor_eq' (a b : Nat) : Nat.xor a b = a ^^^ b := rfl
theorem shiftLeft_eq' (a b : Nat) : Nat.shiftLeft a b = a <<< b := rfl
theorem shiftRight_eq' (a b : Nat) : Nat.shiftRight a b = a >>> b := rfl
theorem add_eq' (a b : Nat) : Nat.add a b = a + b := rfl
theorem sub_eq' (a b : Nat) : Nat.sub a b = a - b := rfl
theorem mul_eq' (a b : Nat) : Nat.mul a b = a * b := rfl

theorem beq_zero_false {w : Nat} (hw0 : w ≠ 0) : Nat.beq w 0 = false := by
  cases h : Nat.beq w 0
  · rfl
  · exact absurd (Nat.eq_of_beq_eq_true h) hw0

theorem cond_ble (c w k : Nat) : cond (Nat.ble c w) k 0 = if c ≤ w then k else 0 := by
  by_cases h : c ≤ w
  · simp [Nat.ble_eq_true_of_le h, h]
  · have : Nat.ble c w = false := by
      cases hb : Nat.ble c w
      · rfl
      · exact absurd (Nat.le_of_ble_eq_true hb) h
    simp [this, h]

/-- One halving step of `pos64`. -/
theorem pos_step (k c w : Nat) (hc : c = 2 ^ k) (hw : w < 2 ^ (2 * k)) :
    let a := if c ≤ w then k else 0
    let w' := w >>> a
    w' < 2 ^ k ∧ 2 ^ a * w' ≤ w ∧ w < 2 ^ a * (w' + 1) ∧ (0 < w → 0 < w') := by
  intro a w'
  subst hc
  simp only [a, w', Nat.shiftRight_eq_div_pow]
  by_cases h : 2 ^ k ≤ w
  · simp only [h, ite_true]
    have hpos : 0 < 2 ^ k := Nat.two_pow_pos k
    refine ⟨?_, ?_, ?_, ?_⟩
    · rw [Nat.div_lt_iff_lt_mul hpos, ← Nat.pow_add]
      rw [show k + k = 2 * k by omega]; exact hw
    · exact Nat.mul_div_le w (2 ^ k)
    · exact Nat.lt_mul_div_succ w hpos
    · intro _; exact Nat.div_pos h hpos
  · simp only [h, ite_false, Nat.pow_zero, Nat.div_one, Nat.one_mul]
    exact ⟨Nat.lt_of_not_le h, Nat.le_refl _, Nat.lt_succ_self _, fun h0 => h0⟩

theorem pos64_spec (w : Nat) (h0 : 0 < w) (h : w < 2 ^ 64) :
    2 ^ pos64 w ≤ w ∧ w < 2 ^ (pos64 w + 1) := by
  unfold pos64
  simp only [cond_ble, add_eq', shiftRight_eq']
  have s1 := pos_step 32 4294967296 w (by norm_num) (by simpa using h)
  obtain ⟨l1, le1, lt1, p1⟩ := s1
  set a := (if 4294967296 ≤ w then 32 else 0) with ha
  set w1 := w >>> a with hw1
  have s2 := pos_step 16 65536 w1 (by norm_num) (by simpa using l1)
  obtain ⟨l2, le2, lt2, p2⟩ := s2
  set b := (if 65536 ≤ w1 then 16 else 0) with hb
  set w2 := w1 >>> b with hw2
  have s3 := pos_step 8 256 w2 (by norm_num) (by simpa using l2)
  obtain ⟨l3, le3, lt3, p3⟩ := s3
  set c := (if 256 ≤ w2 then 8 else 0) with hc
  set w3 := w2 >>> c with hw3
  have s4 := pos_step 4 16 w3 (by norm_num) (by simpa using l3)
  obtain ⟨l4, le4, lt4, p4⟩ := s4
  set d := (if 16 ≤ w3 then 4 else 0) with hd
  set w4 := w3 >>> d with hw4
  have s5 := pos_step 2 4 w4 (by norm_num) (by simpa using l4)
  obtain ⟨l5, le5, lt5, p5⟩ := s5
  set e := (if 4 ≤ w4 then 2 else 0) with he
  set w5 := w4 >>> e with hw5
  have w5pos : 0 < w5 := p5 (p4 (p3 (p2 (p1 h0))))
  set f := (if 2 ≤ w5 then 1 else 0) with hf
  have hf1 : 2 ^ f ≤ w5 ∧ w5 < 2 ^ (f + 1) := by
    simp only [hf]; split_ifs with h2 <;> simp <;> omega
  -- combine: 2^(a+b+c+d+e+f) ≤ w < 2^(a+b+c+d+e+f+1)
  have key : ∀ (x y : Nat) (p q : Nat), 2 ^ p * y ≤ x → x < 2 ^ p * (y + 1) →
      2 ^ q ≤ y → y < 2 ^ (q + 1) → 2 ^ (p + q) ≤ x ∧ x < 2 ^ (p + q + 1) := by
    intro x y p q h1 h2 h3 h4
    constructor
    · calc 2 ^ (p + q) = 2 ^ p * 2 ^ q := Nat.pow_add 2 p q
        _ ≤ 2 ^ p * y := Nat.mul_le_mul_left _ h3
        _ ≤ x := h1
    · calc x < 2 ^ p * (y + 1) := h2
        _ ≤ 2 ^ p * 2 ^ (q + 1) := Nat.mul_le_mul_left _ h4
        _ = 2 ^ (p + q + 1) := by rw [← Nat.pow_add, Nat.add_assoc]
  have k5 := key w4 w5 e f le5 lt5 hf1.1 hf1.2
  have k4 := key w3 w4 d (e + f) le4 lt4 k5.1 k5.2
  have k3 := key w2 w3 c (d + (e + f)) le3 lt3 k4.1 k4.2
  have k2 := key w1 w2 b (c + (d + (e + f))) le2 lt2 k3.1 k3.2
  have k1 := key w w1 a (b + (c + (d + (e + f)))) le1 lt1 k2.1 k2.2
  have hex : a + b + (c + d) + (e + f) = a + (b + (c + (d + (e + f)))) := by omega
  rw [hex]; exact k1

theorem pos64_testBit (w : Nat) (h0 : 0 < w) (h : w < 2 ^ 64) : w.testBit (pos64 w) = true :=
  Nat.testBit_of_two_pow_le_and_two_pow_add_one_gt (pos64_spec w h0 h).1 (pos64_spec w h0 h).2

/-- Clearing the top bit leaves a number below `2 ^ pos64 w`. -/
theorem pos64_clear (w : Nat) (h0 : 0 < w) (h : w < 2 ^ 64) :
    w ^^^ (1 <<< pos64 w) < 2 ^ pos64 w := by
  rw [Nat.shiftLeft_eq, Nat.one_mul]
  apply Nat.lt_pow_two_of_testBit
  intro i hi
  rw [Nat.testBit_xor]
  rcases Nat.eq_or_lt_of_le hi with rfl | hlt
  · rw [pos64_testBit w h0 h, Nat.testBit_two_pow_self]; rfl
  · rw [Nat.testBit_two_pow_of_ne (Nat.ne_of_lt hlt)]
    have : w < 2 ^ i := lt_of_lt_of_le (pos64_spec w h0 h).2 (Nat.pow_le_pow_right (by norm_num) hlt)
    rw [Nat.testBit_lt_two_pow this]; rfl

theorem testBit_clear_of_ne (w p j : Nat) (hj : j ≠ p) :
    (w ^^^ (1 <<< p)).testBit j = w.testBit j := by
  rw [Nat.shiftLeft_eq, Nat.one_mul, Nat.testBit_xor, Nat.testBit_two_pow_of_ne (Ne.symm hj), Bool.xor_false]

/-- The four images of `s` are in `img4`. -/
theorem img4_mem (M mask top s u v : Nat) (htop : top = Nat.shiftLeft 1 (Nat.sub M 1)) (hu : u ≤ 1) (hv : v ≤ 1) :
    (img4 mask top s).testBit (step2 M mask s u v) = true := by
  unfold img4 step2
  rw [← nxtT_eq M mask s 0 u, ← nxtT_eq M mask _ 1 v]
  have h0 : Nat.shiftLeft 0 (Nat.sub M 1) = 0 := by simp [shiftLeft_eq']
  simp only [lor_eq', shiftLeft_eq', Nat.testBit_or, Nat.shiftLeft_eq, Nat.one_mul]
  rcases Nat.le_one_iff_eq_zero_or_eq_one.mp hu with rfl | rfl <;>
  rcases Nat.le_one_iff_eq_zero_or_eq_one.mp hv with rfl | rfl <;>
  simp [Nat.testBit_two_pow_self, htop, h0, shiftLeft_eq', Nat.shiftLeft_eq, Nat.one_mul]

theorem wordLoop_succ (M mask H top fuel w base acc : Nat) :
    wordLoop M mask H top (fuel + 1) w base acc =
      cond (Nat.beq w 0) acc
        (force (pos64 w) fun p => force (Nat.add base p) fun s =>
          force (Nat.xor w (Nat.shiftLeft 1 p)) fun w' =>
            force (Nat.lor acc (Nat.shiftLeft (img4 mask top s) (Nat.mul (Nat.land s 1) H))) fun acc' =>
              wordLoop M mask H top fuel w' base acc') := rfl

theorem wordLoop_zero (M mask H top w base acc : Nat) : wordLoop M mask H top 0 w base acc = acc := rfl

/-- Every member of the word gets its images into the right half; nothing is lost. -/
theorem wordLoop_spec (M mask H top : Nat) (htop : top = Nat.shiftLeft 1 (Nat.sub M 1)) :
    ∀ (fuel w base acc : Nat), w < 2 ^ fuel → w < 2 ^ 64 →
    (∀ t, acc.testBit t = true → (wordLoop M mask H top fuel w base acc).testBit t = true) ∧
    (∀ j, w.testBit j = true → ∀ u v, u ≤ 1 → v ≤ 1 →
      (wordLoop M mask H top fuel w base acc).testBit
        (step2 M mask (base + j) u v + (base + j) % 2 * H) = true) := by
  intro fuel
  induction fuel with
  | zero =>
    intro w base acc hw _
    have : w = 0 := by simpa using hw
    subst this
    refine ⟨fun t ht => by simpa [wordLoop_zero] using ht, fun j hj => ?_⟩
    simp at hj
  | succ n ih =>
    intro w base acc hw h64
    rw [wordLoop_succ]
    by_cases hw0 : w = 0
    · subst hw0
      rw [show Nat.beq 0 0 = true from rfl, cond_true]
      exact ⟨fun t ht => ht, fun j hj => by simp at hj⟩
    · have hbeq : Nat.beq w 0 = false := beq_zero_false hw0
      rw [hbeq]; simp only [cond_false, force_eq, lor_eq', land_eq', xor_eq', shiftLeft_eq', add_eq', mul_eq']
      have hpos : 0 < w := Nat.pos_of_ne_zero hw0
      have hp := pos64_spec w hpos h64
      have hpl : pos64 w ≤ n := by
        have : 2 ^ pos64 w < 2 ^ (n + 1) := lt_of_le_of_lt hp.1 hw
        exact Nat.lt_succ_iff.mp (Nat.pow_lt_pow_iff_right (by norm_num) |>.mp this)
      have hw' : w ^^^ (1 <<< pos64 w) < 2 ^ n :=
        lt_of_lt_of_le (pos64_clear w hpos h64) (Nat.pow_le_pow_right (by norm_num) hpl)
      have hp64 : pos64 w < 64 := by
        have := lt_of_le_of_lt hp.1 h64
        exact (Nat.pow_lt_pow_iff_right (by norm_num)).mp this
      have hw'64 : w ^^^ (1 <<< pos64 w) < 2 ^ 64 := Nat.xor_lt_two_pow h64 (by
        rw [Nat.shiftLeft_eq, Nat.one_mul]; exact Nat.pow_lt_pow_right (by norm_num) hp64)
      obtain ⟨mono, mem⟩ := ih (w ^^^ (1 <<< pos64 w)) base
        (acc ||| (img4 mask top (base + pos64 w) <<< (((base + pos64 w) &&& 1) * H))) hw' hw'64
      refine ⟨fun t ht => mono t (by rw [Nat.testBit_or, ht]; rfl), fun j hj u v hu hv => ?_⟩
      by_cases hjp : j = pos64 w
      · subst hjp
        apply mono
        rw [Nat.testBit_or, Nat.testBit_shiftLeft]
        have hland : (base + pos64 w) &&& 1 = (base + pos64 w) % 2 := Nat.and_one_is_mod _
        rw [hland]
        simp only [ge_iff_le, Nat.le_add_left, decide_true, Bool.true_and, Nat.add_sub_cancel]
        rw [img4_mem M mask top _ u v htop hu hv]; simp
      · exact mem j (by rw [testBit_clear_of_ne w (pos64 w) j hjp]; exact hj) u v hu hv

theorem sweep_succ (M mask H top k B acc : Nat) :
    sweep M mask H top (k + 1) B acc =
      force (Nat.land (Nat.shiftRight B (Nat.mul 64 k)) 18446744073709551615) fun w =>
        cond (Nat.beq w 0) (sweep M mask H top k B acc)
          (force (wordLoop M mask H top 64 w (Nat.mul 64 k) acc) fun acc' => sweep M mask H top k B acc') := rfl

theorem sweep_zero (M mask H top B acc : Nat) : sweep M mask H top 0 B acc = acc := rfl

theorem word_testBit (B k j : Nat) :
    ((B >>> (64 * k)) &&& 18446744073709551615).testBit j = (decide (j < 64) && B.testBit (64 * k + j)) := by
  rw [Nat.testBit_and, Nat.testBit_shiftRight]
  rw [show (18446744073709551615 : Nat) = 2 ^ 64 - 1 by norm_num, Nat.testBit_two_pow_sub_one]
  rw [Bool.and_comm]

theorem word_lt (B k : Nat) : (B >>> (64 * k)) &&& 18446744073709551615 < 2 ^ 64 :=
  Nat.and_lt_two_pow _ (by norm_num)

/-- Every member `s < 64 n` of `B` gets its images into the right half; nothing is lost. -/
theorem sweep_spec (M mask H top : Nat) (htop : top = Nat.shiftLeft 1 (Nat.sub M 1)) : ∀ (n B acc : Nat),
    (∀ t, acc.testBit t = true → (sweep M mask H top n B acc).testBit t = true) ∧
    (∀ s, s < 64 * n → B.testBit s = true → ∀ u v, u ≤ 1 → v ≤ 1 →
      (sweep M mask H top n B acc).testBit (step2 M mask s u v + s % 2 * H) = true) := by
  intro n
  induction n with
  | zero => intro B acc; exact ⟨fun t ht => by simpa [sweep_zero] using ht, fun s hs => by omega⟩
  | succ k ih =>
    intro B acc
    rw [sweep_succ, force_eq]
    simp only [land_eq', shiftRight_eq', mul_eq']
    set w := (B >>> (64 * k)) &&& 18446744073709551615 with hw
    by_cases hw0 : w = 0
    · rw [hw0, show Nat.beq 0 0 = true from rfl, cond_true]
      obtain ⟨mono, mem⟩ := ih B acc
      refine ⟨mono, fun s hs hB u v hu hv => ?_⟩
      by_cases hsk : s < 64 * k
      · exact mem s hsk hB u v hu hv
      · exfalso
        have hj : w.testBit (s - 64 * k) = true := by
          rw [hw, word_testBit]
          have : 64 * k + (s - 64 * k) = s := by omega
          rw [this, hB]; simp; omega
        rw [hw0] at hj; simp at hj
    · have hbeq : Nat.beq w 0 = false := beq_zero_false hw0
      rw [hbeq]; simp only [cond_false, force_eq]
      obtain ⟨wmono, wmem⟩ := wordLoop_spec M mask H top htop 64 w (64 * k) acc (hw ▸ word_lt B k) (hw ▸ word_lt B k)
      obtain ⟨mono, mem⟩ := ih B (wordLoop M mask H top 64 w (64 * k) acc)
      refine ⟨fun t ht => mono t (wmono t ht), fun s hs hB u v hu hv => ?_⟩
      by_cases hsk : s < 64 * k
      · exact mem s hsk hB u v hu hv
      · apply mono
        have hj : w.testBit (s - 64 * k) = true := by
          rw [hw, word_testBit]
          have : 64 * k + (s - 64 * k) = s := by omega
          rw [this, hB]; simp; omega
        have := wmem (s - 64 * k) hj u v hu hv
        have e : 64 * k + (s - 64 * k) = s := by omega
        rw [e] at this; exact this

/-- The packed image bitsets: label `b` members of `B` below `2 ^ M` send their images to half `b`. -/
theorem imageSets_spec (M mask H : Nat) (hM : 6 ≤ M) (hH : H = 2 ^ M) (B s u v : Nat)
    (hs : s < 2 ^ M) (hB : B.testBit s = true) (hu : u ≤ 1) (hv : v ≤ 1) :
    (imageSets M mask H B).testBit (step2 M mask s u v + s % 2 * H) = true := by
  unfold imageSets
  have htop : Nat.shiftRight H 1 = Nat.shiftLeft 1 (Nat.sub M 1) := by
    rw [hH, shiftRight_eq', shiftLeft_eq', sub_eq', Nat.shiftRight_eq_div_pow, Nat.shiftLeft_eq, Nat.one_mul]
    rw [Nat.pow_div (by omega) (by norm_num)]
  apply (sweep_spec M mask H _ htop (H >>> 6) B 0).2 s _ hB u v hu hv
  rw [hH, Nat.shiftRight_eq_div_pow]
  have : 2 ^ M = 64 * (2 ^ M / 2 ^ 6) := by
    rw [show (64 : Nat) = 2 ^ 6 by norm_num]
    rw [Nat.mul_div_cancel' (Nat.pow_dvd_pow 2 hM)]
  omega


/-! ### The run: every edge of the graph is closed -/

theorem nxt_lt (M mask s tv u : Nat) (hmask : mask = 2 ^ M - 1) : nxt M mask s tv u < 2 ^ M := by
  unfold nxt; simp only [land_eq']; rw [hmask]
  exact Nat.and_lt_two_pow _ (Nat.sub_lt (Nat.two_pow_pos M) Nat.one_pos)

theorem step2_lt (M mask s u v : Nat) (hmask : mask = 2 ^ M - 1) : step2 M mask s u v < 2 ^ M :=
  nxt_lt M mask _ 1 v hmask

/-- The successor of state `i` on letter `b` in the list `succ` (`DEAD` past the end). -/
def succAt (succ : List (Nat × Nat)) (i b : Nat) : Nat :=
  if b = 0 then (succ.getD i (DEAD, DEAD)).1 else (succ.getD i (DEAD, DEAD)).2

/-- Edge `(i, b) → j` is closed: every member of `Bset i` below `2 ^ M` with low bit `b` has its four
two-step images in `Bset j`, and `j` is a live state below `N`. -/
def EdgeOK (M mask : Nat) (Bset : Nat → Nat) (N i j b : Nat) : Prop :=
  ∀ s, s < 2 ^ M → (Bset i).testBit s = true → s % 2 = b →
    j < N ∧ ∀ u v, u ≤ 1 → v ≤ 1 → (Bset j).testBit (step2 M mask s u v) = true

theorem at_cons_lt (T : Nat) (bits : List Nat) (cnt k : Nat) (hk : k < cnt) :
    at_ (T :: bits) (cnt + 1) k = at_ bits cnt k := by
  unfold at_
  simp only [sub_eq']
  have : cnt + 1 - 1 - k = (cnt - 1 - k) + 1 := by omega
  rw [this, List.getD_cons_succ]

theorem at_cons_self (T : Nat) (bits : List Nat) (cnt : Nat) : at_ (T :: bits) (cnt + 1) cnt = T := by
  unfold at_; simp only [sub_eq']
  rw [show cnt + 1 - 1 - cnt = 0 by omega, List.getD_cons_zero]

theorem edge_sound (j T : Nat) (bits : List Nat) (cnt : Nat) (bits' : List Nat) (cnt' : Nat)
    (h : edge j T bits cnt = some (bits', cnt')) (hlen : cnt = bits.length) :
    cnt' = bits'.length ∧ cnt ≤ cnt' ∧ (∀ k, k < cnt → at_ bits' cnt' k = at_ bits cnt k) ∧
    (j = DEAD → T = 0) ∧
    (j ≠ DEAD → j < cnt' ∧ ∀ t, T.testBit t = true → (at_ bits' cnt' j).testBit t = true) := by
  unfold edge at h
  rw [force_eq] at h
  cases hjd : Nat.beq j DEAD with
  | true =>
    rw [hjd, cond_true] at h
    have hj : j = DEAD := Nat.eq_of_beq_eq_true hjd
    cases hT : Nat.beq T 0 with
    | true =>
      rw [hT, cond_true] at h
      have hT0 : T = 0 := Nat.eq_of_beq_eq_true hT
      simp only [Option.some.injEq, Prod.mk.injEq] at h
      obtain ⟨rfl, rfl⟩ := h
      exact ⟨hlen, Nat.le_refl _, fun _ _ => rfl, fun _ => hT0, fun hne => absurd hj hne⟩
    | false => rw [hT, cond_false] at h; cases h
  | false =>
    rw [hjd, cond_false] at h
    have hj : j ≠ DEAD := Nat.ne_of_beq_eq_false hjd
    cases hjc : Nat.beq j cnt with
    | true =>
      rw [hjc, cond_true] at h
      have hjc' : j = cnt := Nat.eq_of_beq_eq_true hjc
      simp only [Option.some.injEq, Prod.mk.injEq] at h
      obtain ⟨rfl, rfl⟩ := h
      refine ⟨by simp [hlen], Nat.le_succ _, fun k hk => at_cons_lt T bits cnt k hk, fun hd => absurd hd hj,
        fun _ => ⟨by omega, fun t ht => ?_⟩⟩
      rw [hjc', at_cons_self]; exact ht
    | false =>
      rw [hjc, cond_false] at h
      cases hlt : Nat.blt j cnt with
      | true =>
        rw [hlt, cond_true] at h
        have hjlt : j < cnt := Nat.le_of_ble_eq_true hlt
        cases hsub : Nat.beq (Nat.land T (at_ bits cnt j)) T with
        | true =>
          rw [hsub, cond_true] at h
          have hsub' : T &&& at_ bits cnt j = T := Nat.eq_of_beq_eq_true hsub
          simp only [Option.some.injEq, Prod.mk.injEq] at h
          obtain ⟨rfl, rfl⟩ := h
          refine ⟨hlen, Nat.le_refl _, fun _ _ => rfl, fun hd => absurd hd hj, fun _ => ⟨hjlt, fun t ht => ?_⟩⟩
          have := congrArg (fun x => x.testBit t) hsub'
          simp only [Nat.testBit_and, ht, Bool.true_and] at this
          exact this
        | false => rw [hsub, cond_false] at h; cases h
      | false => rw [hlt, cond_false] at h; cases h

theorem run_nil (M mask H ALL i : Nat) (bits : List Nat) (cnt : Nat) :
    run M mask H ALL [] i bits cnt = Nat.beq i cnt := rfl

theorem run_cons (M mask H ALL : Nat) (p : Nat × Nat) (l : List (Nat × Nat)) (i : Nat) (bits : List Nat) (cnt : Nat) :
    run M mask H ALL (p :: l) i bits cnt =
      cond (Nat.blt i cnt)
        (force (at_ bits cnt i) fun B =>
         force (imageSets M mask H B) fun T =>
         match edge p.1 (Nat.land T ALL) bits cnt with
         | none => false
         | some (bits1, cnt1) =>
           match edge p.2 (Nat.shiftRight T H) bits1 cnt1 with
           | none => false
           | some (bits2, cnt2) => force cnt2 fun cnt2 => run M mask H ALL l (Nat.succ i) bits2 cnt2)
        false := rfl

theorem succAt_cons_succ (p : Nat × Nat) (l : List (Nat × Nat)) (k b : Nat) :
    succAt (p :: l) (k + 1) b = succAt l k b := by
  unfold succAt; rw [List.getD_cons_succ]

theorem succAt_cons_zero (p : Nat × Nat) (l : List (Nat × Nat)) (b : Nat) :
    succAt (p :: l) 0 b = if b = 0 then p.1 else p.2 := by
  unfold succAt; rw [List.getD_cons_zero]

theorem run_sound (M mask H ALL : Nat) (hM : 6 ≤ M) (hmask : mask = 2 ^ M - 1) (hH : H = 2 ^ M)
    (hALL : ALL = 2 ^ H - 1) :
    ∀ (l : List (Nat × Nat)) (i : Nat) (bits : List Nat) (cnt : Nat),
      run M mask H ALL l i bits cnt = true → cnt = bits.length → i ≤ cnt →
      ∃ (bitsF : List Nat) (cntF : Nat), cntF = bitsF.length ∧ cnt ≤ cntF ∧
        (∀ k, k < cnt → at_ bitsF cntF k = at_ bits cnt k) ∧ cntF = i + l.length ∧
        ∀ k, k < l.length → ∀ b, b ≤ 1 →
          EdgeOK M mask (at_ bitsF cntF) cntF (i + k) (succAt l k b) b := by
  intro l
  induction l with
  | nil =>
    intro i bits cnt hrun hlen hi
    rw [run_nil] at hrun
    have := Nat.eq_of_beq_eq_true hrun
    exact ⟨bits, cnt, hlen, Nat.le_refl _, fun _ _ => rfl, by simp [this], fun k hk => by simp at hk⟩
  | cons p l ih =>
    intro i bits cnt hrun hlen hi
    rw [run_cons] at hrun
    cases hblt : Nat.blt i cnt with
    | false => rw [hblt, cond_false] at hrun; cases hrun
    | true =>
    rw [hblt, cond_true, force_eq, force_eq] at hrun
    have hilt : i < cnt := Nat.le_of_ble_eq_true hblt
    set B := at_ bits cnt i with hB
    set T := imageSets M mask H B with hT
    rcases h1 : edge p.1 (Nat.land T ALL) bits cnt with _ | ⟨bits1, cnt1⟩
    · rw [h1] at hrun; cases hrun
    rw [h1] at hrun; dsimp only at hrun
    rcases h2 : edge p.2 (Nat.shiftRight T H) bits1 cnt1 with _ | ⟨bits2, cnt2⟩
    · rw [h2] at hrun; cases hrun
    rw [h2] at hrun; dsimp only at hrun; rw [force_eq] at hrun
    obtain ⟨len1, le1, st1, dead1, live1⟩ := edge_sound _ _ _ _ _ _ h1 hlen
    obtain ⟨len2, le2, st2, dead2, live2⟩ := edge_sound _ _ _ _ _ _ h2 len1
    obtain ⟨bitsF, cntF, lenF, leF, stF, cntF_eq, edges⟩ := ih (Nat.succ i) bits2 cnt2 hrun len2 (by omega)
    refine ⟨bitsF, cntF, lenF, by omega, ?_, by simp [cntF_eq]; omega, ?_⟩
    · intro k hk
      rw [stF k (by omega), st2 k (by omega), st1 k hk]
    · intro k hk b hb
      cases k with
      | succ k' =>
        rw [succAt_cons_succ]
        have := edges k' (by simpa using hk) b hb
        rw [show i + (k' + 1) = Nat.succ i + k' by omega]
        exact this
      | zero =>
        rw [succAt_cons_zero]
        intro s hs hmem hsb
        rw [Nat.add_zero, stF i (by omega), st2 i (by omega), st1 i hilt] at hmem
        have himg := fun u v hu hv => imageSets_spec M mask H hM hH B s u v hs hmem hu hv
        have hst2 : ∀ u v, step2 M mask s u v < H := fun u v => hH ▸ step2_lt M mask s u v hmask
        rcases Nat.le_one_iff_eq_zero_or_eq_one.mp hb with rfl | rfl
        · simp only [ite_true]
          have hT0 : ∀ u v, u ≤ 1 → v ≤ 1 → (Nat.land T ALL).testBit (step2 M mask s u v) = true := by
            intro u v hu hv
            rw [land_eq', Nat.testBit_and, hALL, Nat.testBit_two_pow_sub_one]
            have := himg u v hu hv
            rw [hsb, Nat.zero_mul, Nat.add_zero] at this
            rw [this]; simp [hst2 u v]
          by_cases hd : p.1 = DEAD
          · exfalso
            have := hT0 0 0 (Nat.le_refl _ |>.trans (Nat.zero_le 1)) (Nat.zero_le 1)
            rw [dead1 hd] at this; simp at this
          · obtain ⟨hj, hmemj⟩ := live1 hd
            refine ⟨by omega, fun u v hu hv => ?_⟩
            rw [stF _ (by omega), st2 _ (by omega)]
            exact hmemj _ (hT0 u v hu hv)
        · simp only [one_ne_zero, ite_false]
          have hT1 : ∀ u v, u ≤ 1 → v ≤ 1 → (Nat.shiftRight T H).testBit (step2 M mask s u v) = true := by
            intro u v hu hv
            rw [shiftRight_eq', Nat.testBit_shiftRight]
            have := himg u v hu hv
            rw [hsb, Nat.one_mul, Nat.add_comm] at this
            exact this
          by_cases hd : p.2 = DEAD
          · exfalso
            have := hT1 0 0 (Nat.zero_le 1) (Nat.zero_le 1)
            rw [dead2 hd] at this; simp at this
          · obtain ⟨hj, hmemj⟩ := live2 hd
            refine ⟨by omega, fun u v hu hv => ?_⟩
            rw [stF _ (by omega)]
            exact hmemj _ (hT1 u v hu hv)

/-- `check M succ = true` gives bitsets for the states, the root full, every edge closed. -/
theorem check_sound (M : Nat) (hM : 6 ≤ M) (succ : List (Nat × Nat)) (h : check M succ = true) :
    ∃ Bset : Nat → Nat, Bset 0 = 2 ^ (2 ^ M) - 1 ∧
      ∀ i, i < succ.length → ∀ b, b ≤ 1 →
        EdgeOK M (2 ^ M - 1) Bset succ.length i (succAt succ i b) b := by
  unfold check at h
  simp only [force_eq, shiftLeft_eq', sub_eq', Nat.shiftLeft_eq, Nat.one_mul] at h
  obtain ⟨bitsF, cntF, lenF, leF, stF, cntF_eq, edges⟩ :=
    run_sound M (2 ^ M - 1) (2 ^ M) (2 ^ 2 ^ M - 1) hM rfl rfl rfl succ 0 [2 ^ 2 ^ M - 1] 1 h rfl (Nat.zero_le 1)
  have hc : cntF = succ.length := by simpa using cntF_eq
  subst hc
  refine ⟨at_ bitsF succ.length, ?_, ?_⟩
  · rw [stF 0 Nat.one_pos]; rfl
  · intro i hi b hb
    have := edges i hi b hb
    rw [Nat.zero_add] at this
    exact this


/-! ## 3. The physical window -/

/-- The `M` cells right of the center at time `t`, cell `p + 1` as bit `p`. -/
def win (x : Int → Bool) (t : Nat) : Nat → Nat
  | 0 => 0
  | M + 1 => 2 ^ M * (evol x t ((M + 1 : Nat) : Int)).toNat + win x t M

theorem win_lt (x : Int → Bool) (t : Nat) : ∀ M, win x t M < 2 ^ M
  | 0 => by simp [win]
  | M + 1 => by
    unfold win
    have h1 := win_lt x t M
    have h2 : (evol x t ((M + 1 : Nat) : Int)).toNat ≤ 1 := Bool.toNat_le _
    calc 2 ^ M * (evol x t ((M + 1 : Nat) : Int)).toNat + win x t M
        ≤ 2 ^ M * 1 + win x t M := by gcongr
      _ < 2 ^ M * 1 + 2 ^ M := by omega
      _ = 2 ^ (M + 1) := by rw [Nat.pow_succ]; ring

theorem win_testBit (x : Int → Bool) (t : Nat) : ∀ M p,
    (win x t M).testBit p = (decide (p < M) && evol x t ((p + 1 : Nat) : Int))
  | 0, p => by simp [win]
  | M + 1, p => by
    unfold win
    rw [Nat.testBit_two_pow_mul_add _ (win_lt x t M)]
    by_cases hp : p < M
    · rw [if_pos hp, win_testBit x t M p]
      simp [hp, Nat.lt_succ_of_lt hp]
    · rw [if_neg hp, Nat.testBit_bool_toNat]
      by_cases hpm : p = M
      · subst hpm; simp
      · have : ¬ p < M + 1 := by omega
        have : p - M ≠ 0 := by omega
        simp [*]

theorem win_mod_two (x : Int → Bool) (t M : Nat) (hM : 0 < M) :
    win x t M % 2 = (evol x t 1).toNat := by
  have h := win_testBit x t M 0
  rw [Nat.testBit_eq_decide_div_mod_eq] at h
  simp only [Nat.pow_zero, Nat.div_one, hM, decide_true, Bool.true_and] at h
  have : (0 + 1 : Nat) = 1 := rfl
  rw [this] at h
  cases hc : evol x t ((1 : Nat) : Int)
  · rw [hc] at h; simp at h; simp [h]
  · rw [hc] at h; simp at h; simp [h]

/-- One step of the window is `nxt`. -/
theorem win_succ (x : Int → Bool) (t M : Nat) (hM : 1 ≤ M) :
    win x (t + 1) M = nxt M (2 ^ M - 1) (win x t M) (evol x t 0).toNat (evol x t ((M + 1 : Nat) : Int)).toNat := by
  apply Nat.eq_of_testBit_eq
  intro p
  unfold nxt
  simp only [land_eq', xor_eq', lor_eq', shiftLeft_eq', shiftRight_eq', sub_eq']
  rw [Nat.testBit_and, Nat.testBit_xor, Nat.testBit_or, Nat.testBit_or, Nat.testBit_or,
    Nat.testBit_shiftLeft, Nat.testBit_shiftRight, Nat.testBit_shiftLeft, Nat.testBit_two_pow_sub_one,
    Nat.testBit_bool_toNat, Nat.testBit_bool_toNat, win_testBit, win_testBit, win_testBit, win_testBit]
  by_cases hp : p < M
  · simp only [hp, decide_true, Bool.true_and, Bool.and_true]
    rw [show evol x (t + 1) ((p + 1 : Nat) : Int) =
        rule (evol x t (((p + 1 : Nat) : Int) - 1)) (evol x t ((p + 1 : Nat) : Int)) (evol x t (((p + 1 : Nat) : Int) + 1)) from rfl]
    unfold rule
    have e1 : (((p + 1 : Nat) : Int) - 1) = ((p : Nat) : Int) := by push_cast; ring
    have e2 : (((p + 1 : Nat) : Int) + 1) = ((p + 2 : Nat) : Int) := by push_cast; ring
    rw [e1, e2]
    by_cases h0 : p = 0
    · subst h0
      simp only [ge_iff_le, Nat.zero_le, Nat.lt_irrefl, decide_false, Bool.false_and, Bool.false_or, Nat.sub_zero,
        Nat.zero_add, decide_true, Bool.true_and]
      have hM1 : ¬ (0 ≥ M - 1) ∨ (0 ≥ M - 1) := by tauto
      by_cases hm : M = 1
      · subst hm; simp
      · have : ¬ (0 ≥ M - 1) := by omega
        have : 0 + 1 < M := by omega
        simp [*]
    · have h1 : p ≥ 1 := Nat.pos_of_ne_zero h0
      simp only [h1, ge_iff_le, decide_true, Bool.true_and, h0, decide_false, Bool.false_and, Bool.or_false]
      have hpm : p - 1 < M := by omega
      simp only [hpm, decide_true, Bool.true_and]
      rw [show p - 1 + 1 = p by omega, show 1 + p = p + 1 by omega]
      by_cases hlast : p + 1 < M
      · have : ¬ (p ≥ M - 1) := by omega
        simp [hlast, this, show ((p : Int) + 1 + 1) = (p : Int) + 2 by ring]
      · have hpM : M = p + 1 := by omega
        subst hpM
        simp [show ((p : Int) + 1 + 1) = (p : Int) + 2 by ring]
  · simp [hp]

/-- The clock: column `0` reads `0, 1, 0, 1, …` from time `0`. -/
def Clock (x : Int → Bool) : Prop := ∀ t, evol x t 0 = decide (t % 2 = 1)

/-- Two steps under the clock are `step2`. -/
theorem win_step2 (x : Int → Bool) (hx : Clock x) (k M : Nat) (hM : 1 ≤ M) :
    win x (2 * k + 2) M = step2 M (2 ^ M - 1) (win x (2 * k) M)
      (evol x (2 * k) ((M + 1 : Nat) : Int)).toNat (evol x (2 * k + 1) ((M + 1 : Nat) : Int)).toNat := by
  unfold step2
  have h0 : (evol x (2 * k) 0).toNat = 0 := by rw [hx]; simp
  have h1 : (evol x (2 * k + 1) 0).toNat = 1 := by rw [hx]; simp
  rw [show 2 * k + 2 = (2 * k + 1) + 1 by omega, win_succ x (2 * k + 1) M hM, win_succ x (2 * k) M hM, h0, h1]

/-! ## 4. The walk and the count -/

/-- The automaton state after reading `k` visible bits. -/
def st (succ : List (Nat × Nat)) (x : Int → Bool) : Nat → Nat
  | 0 => 0
  | k + 1 => succAt succ (st succ x k) (evol x (2 * k) 1).toNat

theorem st_inv (M : Nat) (hM : 6 ≤ M) (succ : List (Nat × Nat)) (hN : 0 < succ.length)
    (Bset : Nat → Nat) (hB0 : Bset 0 = 2 ^ (2 ^ M) - 1)
    (hE : ∀ i, i < succ.length → ∀ b, b ≤ 1 → EdgeOK M (2 ^ M - 1) Bset succ.length i (succAt succ i b) b)
    (x : Int → Bool) (hx : Clock x) :
    ∀ k, st succ x k < succ.length ∧ (Bset (st succ x k)).testBit (win x (2 * k) M) = true := by
  intro k
  induction k with
  | zero =>
    refine ⟨hN, ?_⟩
    simp only [st, hB0, Nat.testBit_two_pow_sub_one]
    simp [win_lt x 0 M]
  | succ k ih =>
    obtain ⟨hlt, hmem⟩ := ih
    have hb : (evol x (2 * k) 1).toNat ≤ 1 := Bool.toNat_le _
    have := hE (st succ x k) hlt _ hb (win x (2 * k) M) (win_lt x _ M) hmem
      (win_mod_two x (2 * k) M (by omega))
    obtain ⟨hj, himg⟩ := this
    refine ⟨hj, ?_⟩
    show (Bset (succAt succ (st succ x k) (evol x (2 * k) 1).toNat)).testBit (win x (2 * (k + 1)) M) = true
    rw [show 2 * (k + 1) = 2 * k + 2 by ring, win_step2 x hx k M (by omega)]
    exact himg _ _ (Bool.toNat_le _) (Bool.toNat_le _)

/-- The accepted words of length `n` from state `i`. -/
def AccF (succ : List (Nat × Nat)) : Nat → Nat → Finset (List Bool)
  | 0, i => if i < succ.length then {[]} else ∅
  | n + 1, i => if i < succ.length then
      (AccF succ n (succAt succ i 0)).image (List.cons false) ∪ (AccF succ n (succAt succ i 1)).image (List.cons true)
    else ∅

/-- Their number, by the recursion of the automaton. -/
def cntA (succ : List (Nat × Nat)) : Nat → Nat → Nat
  | 0, i => if i < succ.length then 1 else 0
  | n + 1, i => if i < succ.length then cntA succ n (succAt succ i 0) + cntA succ n (succAt succ i 1) else 0

theorem card_AccF_le (succ : List (Nat × Nat)) : ∀ n i, (AccF succ n i).card ≤ cntA succ n i
  | 0, i => by unfold AccF cntA; split_ifs <;> simp
  | n + 1, i => by
    unfold AccF cntA
    split_ifs with h
    · calc _ ≤ ((AccF succ n (succAt succ i 0)).image (List.cons false)).card +
            ((AccF succ n (succAt succ i 1)).image (List.cons true)).card := Finset.card_union_le _ _
        _ ≤ (AccF succ n (succAt succ i 0)).card + (AccF succ n (succAt succ i 1)).card :=
            Nat.add_le_add Finset.card_image_le Finset.card_image_le
        _ ≤ _ := by have := card_AccF_le succ n (succAt succ i 0); have := card_AccF_le succ n (succAt succ i 1); omega
    · simp

/-- The visible bits from the `k`-th even time on, `n` of them. -/
def visFrom (x : Int → Bool) : Nat → Nat → List Bool
  | _, 0 => []
  | k, n + 1 => evol x (2 * k) 1 :: visFrom x (k + 1) n

theorem visFrom_mem (M : Nat) (hM : 6 ≤ M) (succ : List (Nat × Nat)) (hN : 0 < succ.length)
    (Bset : Nat → Nat) (hB0 : Bset 0 = 2 ^ (2 ^ M) - 1)
    (hE : ∀ i, i < succ.length → ∀ b, b ≤ 1 → EdgeOK M (2 ^ M - 1) Bset succ.length i (succAt succ i b) b)
    (x : Int → Bool) (hx : Clock x) : ∀ n k, visFrom x k n ∈ AccF succ n (st succ x k) := by
  intro n
  induction n with
  | zero => intro k; simp [visFrom, AccF, (st_inv M hM succ hN Bset hB0 hE x hx k).1]
  | succ n ih =>
    intro k
    have hlt := (st_inv M hM succ hN Bset hB0 hE x hx k).1
    simp only [visFrom, AccF, hlt, ite_true, Finset.mem_union, Finset.mem_image]
    have := ih (k + 1)
    simp only [st] at this
    cases hb : evol x (2 * k) 1
    · left; refine ⟨visFrom x (k + 1) n, ?_, rfl⟩; rw [hb] at this; simpa using this
    · right; refine ⟨visFrom x (k + 1) n, ?_, rfl⟩; rw [hb] at this; simpa using this

theorem wcheck_sound (D R : Nat) (succ : List (Nat × Nat)) (w : List Nat) (h : wcheck D R succ w = true) :
    ∀ i, i < succ.length → 0 < w.getD i 0 ∧
      D * (w.getD (succAt succ i 0) 0 + w.getD (succAt succ i 1) 0) ≤ R * w.getD i 0 := by
  intro i hi
  unfold wcheck at h
  rw [List.all_eq_true] at h
  have := h i (List.mem_range.mpr hi)
  simp only [Bool.and_eq_true] at this
  obtain ⟨h1, h2⟩ := this
  refine ⟨Nat.le_of_ble_eq_true h1, ?_⟩
  have := Nat.le_of_ble_eq_true h2
  simpa [succAt, mul_eq', add_eq'] using this

/-- The weight bound: `D ^ n · wmin · cntA n i ≤ R ^ n · w i`. -/
theorem weight_bound (D R : Nat) (succ : List (Nat × Nat)) (w : List Nat) (hw : wcheck D R succ w = true)
    (wmin : Nat) (hmin : ∀ i, i < succ.length → wmin ≤ w.getD i 0) :
    ∀ n i, D ^ n * wmin * cntA succ n i ≤ R ^ n * w.getD i 0 := by
  intro n
  induction n with
  | zero =>
    intro i; unfold cntA
    split_ifs with h
    · simpa using hmin i h
    · simp
  | succ n ih =>
    intro i; unfold cntA
    split_ifs with h
    · obtain ⟨_, hineq⟩ := wcheck_sound D R succ w hw i h
      have h0 := ih (succAt succ i 0)
      have h1 := ih (succAt succ i 1)
      calc D ^ (n + 1) * wmin * (cntA succ n (succAt succ i 0) + cntA succ n (succAt succ i 1))
          = D * (D ^ n * wmin * cntA succ n (succAt succ i 0)) + D * (D ^ n * wmin * cntA succ n (succAt succ i 1)) := by ring
        _ ≤ D * (R ^ n * w.getD (succAt succ i 0) 0) + D * (R ^ n * w.getD (succAt succ i 1) 0) := by gcongr
        _ = R ^ n * (D * (w.getD (succAt succ i 0) 0 + w.getD (succAt succ i 1) 0)) := by ring
        _ ≤ R ^ n * (R * w.getD i 0) := by gcongr
        _ = R ^ (n + 1) * w.getD i 0 := by ring
    · simp

/-! ## 5. The certificate and the bound -/

/-- A certificate: the width, the graph, the weights and the ratio `R / D`. -/
structure Cert where
  M : Nat
  succ : List (Nat × Nat)
  w : List Nat
  D : Nat
  R : Nat
  C : Nat
  wmin : Nat

/-- What the kernel checks of a certificate. -/
structure Cert.Valid (c : Cert) : Prop where
  hM : 6 ≤ c.M
  hcheck : check c.M c.succ = true
  hw : wcheck c.D c.R c.succ c.w = true
  hN : 0 < c.succ.length
  hlen : c.succ.length ≤ c.w.length
  hmin : c.w.all (fun v => Nat.ble c.wmin v) = true
  hmin0 : 0 < c.wmin
  hC : c.w.getD 0 0 ≤ c.C * c.wmin

/-- **The channel bound.** For a valid certificate and every `n`, a set of at most
`C (R / D) ^ n` words of length `n` contains the first `n` visible bits of every configuration
whose center column reads the clock from time `0`. -/
theorem Cert.bound (c : Cert) (hv : c.Valid) (n : Nat) :
    ∃ S : Finset (List Bool), (∀ x : Int → Bool, Clock x → visFrom x 0 n ∈ S) ∧
      S.card * c.D ^ n ≤ c.C * c.R ^ n := by
  obtain ⟨Bset, hB0, hE⟩ := check_sound c.M hv.hM c.succ hv.hcheck
  refine ⟨AccF c.succ n 0, fun x hx => visFrom_mem c.M hv.hM c.succ hv.hN Bset hB0 hE x hx n 0, ?_⟩
  have hmin : ∀ i, i < c.succ.length → c.wmin ≤ c.w.getD i 0 := by
    intro i hi
    have hl : i < c.w.length := lt_of_lt_of_le hi hv.hlen
    have hmem : c.w.getD i 0 ∈ c.w := by
      rw [List.getD_eq_getElem _ _ hl]; exact List.getElem_mem hl
    exact Nat.le_of_ble_eq_true (List.all_eq_true.mp hv.hmin _ hmem)
  have hwb := weight_bound c.D c.R c.succ c.w hv.hw c.wmin hmin n 0
  have hcard := card_AccF_le c.succ n 0
  have h1 : c.D ^ n * c.wmin * (AccF c.succ n 0).card ≤ c.R ^ n * (c.C * c.wmin) :=
    le_trans (Nat.mul_le_mul_left _ hcard) (le_trans hwb (Nat.mul_le_mul_left _ hv.hC))
  have h2 : c.wmin * ((AccF c.succ n 0).card * c.D ^ n) ≤ c.wmin * (c.C * c.R ^ n) := by
    calc c.wmin * ((AccF c.succ n 0).card * c.D ^ n) = c.D ^ n * c.wmin * (AccF c.succ n 0).card := by ring
      _ ≤ c.R ^ n * (c.C * c.wmin) := h1
      _ = c.wmin * (c.C * c.R ^ n) := by ring
  exact Nat.le_of_mul_le_mul_left h2 hv.hmin0


/-- The number of distinct words a set of visible prefixes can take, as a cardinality. -/
theorem Cert.ncard_bound (c : Cert) (hv : c.Valid) (n : Nat) :
    Set.ncard {w : List Bool | ∃ x : Int → Bool, Clock x ∧ visFrom x 0 n = w} * c.D ^ n ≤ c.C * c.R ^ n := by
  obtain ⟨S, hS, hcard⟩ := c.bound hv n
  have hsub : {w : List Bool | ∃ x : Int → Bool, Clock x ∧ visFrom x 0 n = w} ⊆ (S : Set (List Bool)) := by
    rintro w ⟨x, hx, rfl⟩; exact hS x hx
  have := Set.ncard_le_ncard hsub S.finite_toSet
  rw [Set.ncard_coe_finset] at this
  calc _ ≤ S.card * c.D ^ n := Nat.mul_le_mul_right _ this
    _ ≤ _ := hcard

/-- Shifting time: the evolution from time `T` on is the evolution of the row at time `T`. -/
theorem evol_add (x : Int → Bool) (T : Nat) : ∀ t p, evol x (T + t) p = evol (fun q => evol x T q) t p
  | 0, p => by simp [evol]
  | t + 1, p => by
    rw [show T + (t + 1) = (T + t) + 1 by omega]
    show rule (evol x (T + t) (p - 1)) (evol x (T + t) p) (evol x (T + t) (p + 1)) = _
    rw [evol_add x T t, evol_add x T t, evol_add x T t]; rfl

/-- **The eventual form.** If the center column reads the clock from an even time `T` on, the
visible bits from `T` on are bounded in the same way. -/
theorem Cert.bound_eventually (c : Cert) (hv : c.Valid) (n : Nat) :
    ∃ S : Finset (List Bool),
      (∀ (x : Int → Bool) (T : Nat), T % 2 = 0 → (∀ t, T ≤ t → evol x t 0 = decide (t % 2 = 1)) →
        visFrom (fun q => evol x T q) 0 n ∈ S) ∧
      S.card * c.D ^ n ≤ c.C * c.R ^ n := by
  obtain ⟨S, hS, hcard⟩ := c.bound hv n
  refine ⟨S, fun x T hT hx => hS _ ?_, hcard⟩
  intro t
  rw [← evol_add x T t 0, hx (T + t) (Nat.le_add_right T t)]
  have h2 : (T + t) % 2 = t % 2 := by omega
  rw [h2]

theorem visFrom_getD (x : Int → Bool) : ∀ n k m, m < n → (visFrom x k n).getD m false = evol x (2 * (k + m)) 1
  | 0, _, _, h => by omega
  | n + 1, k, 0, _ => by simp [visFrom]
  | n + 1, k, m + 1, h => by
    simp only [visFrom, List.getD_cons_succ]
    rw [visFrom_getD x n (k + 1) m (by omega)]
    congr 2; omega

/-! ## 6. Width 14 -/

def succ14 : List (Nat × Nat) := [(1,2),(3,4),(5,1000000),(6,7),(8,1000000),(9,10),(11,12),(13,1000000),(14,15),(16,17),(18,1000000),(1000000,19),(20,1000000),(21,22),(23,24),(25,1000000),(26,27),(28,1000000),(29,30),(31,1000000),(32,33),(34,24),(35,1000000),(36,37),(38,1000000),(39,40),(1000000,41),(42,1000000),(43,44),(45,1000000),(46,1000000),(47,48),(49,50),(35,1000000),(51,52),(39,53),(1000000,54),(55,1000000),(56,1000000),(57,1000000),(58,1000000),(59,1000000),(60,33),(61,62),(63,1000000),(64,65),(66,40),(67,68),(69,1000000),(70,71),(72,1000000),(1000000,73),(74,1000000),(75,1000000),(76,1000000),(77,78),(79,80),(81,82),(83,84),(85,48),(86,68),(87,88),(89,1000000),(90,91),(1000000,92),(93,1000000),(94,1000000),(95,96),(72,1000000),(39,53),(1000000,97),(98,1000000),(56,1000000),(99,1000000),(100,78),(83,101),(102,103),(104,105),(106,1000000),(107,1000000),(108,1000000),(1000000,109),(110,1000000),(111,1000000),(112,1000000),(113,114),(115,71),(1000000,116),(117,1000000),(118,1000000),(119,1000000),(120,1000000),(121,1000000),(122,78),(123,124),(1000000,125),(126,1000000),(127,1000000),(100,78),(128,103),(129,105),(130,1000000),(131,132),(133,1000000),(134,135),(136,1000000),(137,53),(1000000,138),(139,1000000),(140,1000000),(141,1000000),(1000000,142),(83,143),(144,96),(145,1000000),(1000000,146),(147,1000000),(148,149),(150,80),(151,82),(83,152),(153,154),(104,155),(1000000,156),(157,1000000),(158,1000000),(159,160),(161,162),(163,132),(164,165),(83,166),(167,168),(169,1000000),(170,53),(1000000,171),(172,1000000),(173,1000000),(174,1000000),(175,1000000),(176,177),(178,179),(180,1000000),(181,1000000),(182,1000000),(1000000,183),(184,1000000),(185,1000000),(186,187),(188,1000000),(189,1000000),(107,1000000),(1000000,190),(191,1000000),(192,193),(194,1000000),(195,1000000),(196,1000000),(197,1000000),(198,162),(199,200),(201,1000000),(202,203),(204,1000000),(167,205),(1000000,206),(207,1000000),(208,1000000),(1000000,209),(210,1000000),(211,1000000),(212,1000000),(213,1000000),(214,215),(176,216),(81,217),(218,1000000),(219,1000000),(220,1000000),(221,222),(223,1000000),(224,1000000),(225,1000000),(83,143),(226,1000000),(227,80),(161,228),(229,230),(231,1000000),(1000000,232),(233,234),(235,1000000),(236,166),(237,168),(238,1000000),(239,53),(240,1000000),(241,179),(242,1000000),(243,203),(164,244),(245,1000000),(246,247),(248,1000000),(249,1000000),(250,53),(251,1000000),(252,1000000),(214,253),(254,255),(256,1000000),(257,258),(259,80),(260,261),(262,228),(263,105),(264,1000000),(265,1000000),(266,1000000),(229,267),(1000000,268),(269,1000000),(270,271),(272,1000000),(273,274),(1000000,275),(276,1000000),(277,278),(279,1000000),(280,1000000),(167,1000000),(281,1000000),(282,283),(284,1000000),(285,1000000),(286,1000000),(287,288),(289,1000000),(1000000,290),(211,1000000),(291,1000000),(176,292),(293,294),(295,1000000),(296,1000000),(297,1000000),(298,1000000),(299,1000000),(300,1000000),(1000000,301),(302,1000000),(303,1000000),(257,304),(305,1000000),(306,1000000),(307,1000000),(308,1000000),(277,278),(309,1000000),(310,1000000),(311,1000000),(1000000,312),(313,1000000),(314,203),(164,315),(316,53),(317,1000000),(318,1000000),(319,1000000),(320,1000000),(176,321),(1000000,322),(323,1000000),(324,1000000),(325,1000000),(326,1000000),(327,1000000),(328,1000000),(329,330),(331,1000000),(1000000,332),(333,334),(335,1000000),(336,1000000),(337,1000000),(338,339),(81,340),(83,341),(221,222),(342,1000000),(1000000,343),(344,1000000),(260,261),(345,1000000),(1000000,271),(346,1000000),(1000000,347),(1000000,348),(349,339),(176,350),(81,351),(83,352),(256,1000000),(353,80),(260,354),(355,1000000),(356,1000000),(357,358),(1000000,359),(83,166),(1000000,244),(246,360),(1000000,361),(362,1000000),(363,1000000),(364,1000000),(365,1000000),(366,1000000),(176,367),(368,1000000),(369,1000000),(370,1000000),(371,1000000),(372,1000000),(373,374),(259,375),(376,377),(83,378),(379,228),(1000000,380),(381,1000000),(382,1000000),(250,274),(383,1000000),(384,1000000),(385,1000000),(386,387),(388,389),(83,390),(391,392),(393,1000000),(394,1000000),(395,1000000),(396,274),(397,1000000),(277,398),(399,1000000),(400,1000000),(401,1000000),(402,1000000),(391,105),(403,1000000),(404,1000000),(405,1000000),(406,1000000),(407,1000000),(246,408),(409,1000000),(410,1000000),(411,1000000),(394,1000000),(412,1000000),(413,1000000),(414,179),(415,1000000),(1000000,416),(417,253),(418,419),(420,1000000),(421,1000000),(386,422),(423,424),(425,1000000),(426,1000000),(427,1000000),(428,1000000),(429,1000000),(1000000,430),(431,1000000),(432,1000000),(433,330),(434,1000000),(1000000,435),(302,1000000),(436,1000000),(260,1000000),(83,437),(438,1000000),(439,1000000),(1000000,440),(441,1000000),(442,1000000),(164,443),(444,1000000),(445,446),(447,1000000),(448,449),(450,1000000),(451,1000000),(452,1000000),(453,367),(454,455),(456,228),(457,278),(458,1000000),(459,1000000),(448,460),(1000000,461),(462,1000000),(463,1000000),(1000000,464),(465,419),(1000000,101),(448,466),(467,1000000),(468,222),(469,1000000),(470,1000000),(263,471),(1000000,472),(473,1000000),(474,1000000),(1000000,475),(476,1000000),(477,1000000),(478,1000000),(176,479),(423,480),(1000000,481),(482,360),(483,1000000),(484,1000000),(485,1000000),(83,486),(487,1000000),(488,228),(489,1000000),(229,490),(491,1000000),(1000000,492),(493,1000000),(494,1000000),(495,1000000),(236,496),(497,1000000),(173,1000000),(498,1000000),(499,1000000),(500,1000000),(111,1000000),(501,1000000),(376,502),(503,1000000),(504,274),(505,1000000),(506,1000000),(507,1000000),(356,330),(329,508),(509,510),(511,1000000),(512,1000000),(513,1000000),(514,1000000),(1000000,466),(515,1000000),(1000000,516),(517,1000000),(518,490),(270,1000000),(1000000,519),(520,398),(521,1000000),(522,1000000),(523,1000000),(386,524),(525,1000000),(526,1000000),(1000000,527),(528,1000000),(529,1000000),(530,1000000),(531,1000000),(532,1000000),(176,533),(534,535),(536,1000000),(537,1000000),(1000000,538),(539,540),(457,541),(542,1000000),(448,166),(372,1000000),(176,533),(543,535),(544,1000000),(545,1000000),(546,547),(548,419),(1000000,549),(550,1000000),(254,551),(473,1000000),(552,1000000),(553,1000000),(1000000,554),(1000000,555),(556,1000000),(557,1000000),(558,1000000),(559,1000000),(560,1000000),(254,460),(561,1000000),(562,1000000),(563,1000000),(564,1000000),(1000000,449),(565,1000000),(566,1000000),(329,567),(568,1000000),(569,570),(571,1000000),(572,1000000),(573,228),(574,575),(576,1000000),(386,510),(577,1000000),(578,1000000),(579,339),(580,1000000),(220,1000000),(1000000,581),(582,1000000),(583,1000000),(1000000,255),(584,1000000),(585,1000000),(586,1000000),(587,1000000),(588,1000000),(539,589),(590,1000000),(1000000,591),(592,593),(594,1000000),(1000000,595),(596,1000000),(1000000,597),(598,1000000),(1000000,599),(600,354),(601,1000000),(602,1000000),(176,603),(604,1000000),(1000000,605),(606,1000000),(1000000,607),(608,480),(1000000,609),(610,480),(611,570),(1000000,612),(613,228),(614,1000000),(386,615),(616,222),(617,1000000),(618,1000000),(619,1000000),(433,540),(620,1000000),(621,1000000),(622,1000000),(386,479),(623,510),(391,624),(1000000,625),(626,1000000),(627,1000000),(1000000,628),(563,398),(1000000,629),(630,1000000),(333,631),(632,422),(633,1000000),(1000000,634),(635,1000000),(636,481),(637,1000000),(638,639),(564,1000000),(236,640),(641,1000000),(1000000,460),(642,1000000),(1000000,643),(370,1000000),(644,1000000),(645,1000000),(386,646),(647,1000000),(574,510),(648,1000000),(649,1000000),(650,1000000),(651,1000000),(652,222),(653,1000000),(433,654),(655,1000000),(656,1000000),(657,271),(658,274),(1000000,659),(660,510),(1000000,661),(662,1000000),(663,508),(664,1000000),(665,1000000),(362,1000000),(666,1000000),(667,1000000),(668,1000000),(669,1000000),(353,670),(671,1000000),(585,1000000),(672,1000000),(673,1000000),(674,166),(1000000,675),(676,1000000),(677,1000000),(678,1000000),(679,1000000),(680,228),(681,228),(682,1000000),(683,490),(684,1000000),(685,1000000),(686,1000000),(687,228),(1000000,688),(689,228),(1000000,690),(657,691),(277,692),(693,1000000),(623,646),(694,1000000),(1000000,695),(696,1000000),(697,1000000),(698,1000000),(699,1000000),(453,700),(701,1000000),(1000000,702),(703,1000000),(1000000,704),(376,1000000),(705,228),(706,1000000),(707,1000000),(83,708),(259,709),(710,711),(712,1000000),(713,1000000),(386,350),(714,1000000),(1000000,352),(1000000,715),(1000000,716),(539,424),(534,535),(717,1000000),(176,718),(719,1000000),(423,1000000),(720,716),(721,1000000),(720,1000000),(722,1000000),(723,1000000),(724,1000000),(725,1000000),(176,510),(726,1000000),(376,354),(681,727),(1000000,728),(729,1000000),(730,1000000),(1000000,731),(732,1000000),(1000000,733),(734,1000000),(433,424),(356,480),(735,1000000),(736,1000000),(737,1000000),(539,654),(738,1000000),(1000000,739),(740,1000000),(1000000,741),(742,1000000),(743,1000000),(1000000,744),(745,1000000),(574,746),(747,1000000),(748,692),(749,1000000),(1000000,750),(751,274),(386,752),(753,1000000),(754,1000000),(647,1000000),(755,1000000),(756,1000000),(757,1000000),(758,1000000),(759,1000000),(760,1000000),(176,761),(448,486),(762,1000000),(763,764),(765,1000000),(356,1000000),(766,1000000),(674,767),(768,1000000),(769,1000000),(425,1000000),(770,1000000),(1000000,771),(663,330),(610,424),(772,1000000),(773,1000000),(774,1000000),(423,775),(776,764),(777,1000000),(778,700),(779,1000000),(356,775),(780,1000000),(453,781),(645,1000000),(453,603),(782,1000000),(783,1000000),(784,1000000),(785,786),(787,1000000),(788,789),(790,692),(791,1000000),(792,1000000),(793,360),(794,354),(795,1000000),(796,1000000),(797,1000000),(1000000,798),(799,1000000),(800,424),(176,1000000),(801,1000000),(802,1000000),(803,352),(804,1000000),(805,806),(807,1000000),(254,808),(809,1000000),(810,1000000),(800,716),(453,811),(812,398),(813,1000000),(1000000,814),(176,815),(816,1000000),(388,1000000),(817,1000000),(1000000,818),(819,1000000),(820,1000000),(1000000,821),(822,1000000),(823,1000000),(824,1000000),(825,1000000),(826,827),(828,1000000),(1000000,829),(735,1000000),(830,1000000),(610,1000000),(831,1000000),(832,1000000),(833,1000000),(623,1000000),(834,1000000),(835,1000000),(1000000,836),(632,837),(838,1000000),(1000000,839),(1000000,840),(1000000,841),(842,1000000),(843,1000000),(844,1000000),(674,486),(845,1000000),(846,1000000),(1000000,847),(848,849),(850,1000000),(851,508),(753,1000000),(852,1000000),(853,1000000),(854,570),(855,1000000),(856,1000000),(857,1000000),(386,858),(859,1000000),(254,390),(860,1000000),(386,700),(861,1000000),(539,862),(863,1000000),(386,811),(864,1000000),(622,541),(865,1000000),(468,866),(867,1000000),(681,1000000),(868,1000000),(869,1000000),(1000000,870),(871,1000000),(872,179),(873,1000000),(396,874),(1000000,875),(876,1000000),(877,1000000),(878,1000000),(879,1000000),(880,1000000),(881,1000000),(882,1000000),(539,294),(883,1000000),(884,1000000),(885,1000000),(886,1000000),(887,1000000),(888,1000000),(889,1000000),(176,890),(891,535),(1000000,892),(259,893),(1000000,390),(894,1000000),(1000000,895),(259,896),(1000000,897),(1000000,898),(899,1000000),(1000000,900),(901,1000000),(902,1000000),(800,480),(903,1000000),(904,1000000),(905,1000000),(906,1000000),(907,1000000),(908,1000000),(680,692),(556,1000000),(909,1000000),(910,1000000),(680,911),(912,1000000),(176,913),(666,1000000),(356,424),(453,533),(914,1000000),(851,508),(915,1000000),(916,764),(917,1000000),(918,1000000),(176,700),(794,1000000)]
def weights14 : List Nat := [195955063994,132426329597,99712014807,100912371032,55966216395,118123346978,69059544755,50485812525,66299582693,90273556719,49660902894,36434793386,45375891773,59807184136,57775348581,20765728321,67806153551,39135858368,58829949227,43161546624,53753680984,50377475929,20472335874,60786554144,7656229545,24599079753,35807010187,44518836363,46361382017,50381957998,19310165701,51130441601,43206151327,20472335874,52022612864,24251510352,31561624862,40448404436,9068820877,18446193573,10694092595,42417838891,52738364332,35054481674,19866667152,59684152150,22874737376,40098512546,20472335874,43527053310,7656229545,30893106165,30734659154,10282342089,37388513650,47916298836,10742257013,21851226780,12667646473,50249403062,42003349395,33870121177,7656229545,23534000686,30255656672,40448404436,16403439391,39845567415,7656229545,24251510352,20828782471,30734659154,9068820877,36596548327,36408842947,12179863375,44291377952,36290855965,20472335874,8333870898,4390833861,18508842914,7376180118,4311538196,10694092595,39054784112,42102145637,16680027067,23443262765,9068820877,17896225822,9982307024,35841389351,47916298836,19431263840,20237174679,26964969076,24673777290,36408842947,43353170726,22658468335,10116236960,35979688095,16489216027,38999090946,3991939163,24251510352,9871593431,5200447169,21925444747,8737058390,5106509033,12667646473,38743889808,7521447002,19140755687,19758925341,27771039537,10742257013,21199703656,11824424748,42458566391,36290855965,16927211001,6090986114,23972925004,31943053380,29228777125,34868234382,22849388160,11983085781,35302801723,7319601224,19532879727,17046908549,29152450970,4727893793,18446193573,11693267115,6159561197,25972945850,10349232294,6048276760,10694092595,18932064640,8909149800,22674044623,23406363577,14397173674,18500796693,8333870898,17737011513,9695164118,33808435134,16489216027,3991939163,20051753514,7214544377,28398507591,17869315661,19971059883,18772480882,15852408455,33986110355,967284918,26100216918,9883123016,18932064640,22888460172,8670031794,12856234992,20193554048,34534469018,5599747556,21851226780,13851325506,2989067300,4306714990,20431000547,10336845611,12259105313,7163948443,12667646473,22426817320,10553101561,26859779917,17044725655,10682600973,17054527193,21915912754,21011089309,11484258910,32730611804,7319601224,19532879727,4727893793,23753264515,8545575481,17788896303,17871037769,3296786532,23657670266,15982052250,6255713049,18778481213,21328632589,1144716130,30918618726,11706925727,22426817320,27113788788,10269828751,15229043479,23921249506,22462809069,18447505029,3643527872,7376180118,16407884376,3539834679,5100795163,16882940905,7319601224,12244431339,14521649658,8485636656,26566900370,8109786576,13045959441,15982052250,4208915804,12654032822,20202579503,16939728389,9021925344,24889748320,3720599474,15884901965,8670031794,12856234992,5599747556,17801439635,10122390728,14816841938,20202579503,3904376401,18036089237,9988949642,18932064640,7409689268,11962531554,25265928199,1354911247,14163962842,3751269327,10116236960,26566900370,14397173674,17722180025,7774205470,11258288169,6781719372,15291330394,22617599050,21852780410,4315145936,8737058390,3454477357,4192305080,6041507754,3081883140,16917425481,8670031794,5579057537,8925208492,17201988538,10051383783,16586094371,14885384156,9606130378,15453801877,4984936677,7248481136,7741022124,23931941545,20066582328,10686701916,20431000547,9053628122,4406449366,18816974869,15229043479,3643527872,14281442509,6805972021,11990375868,17551690141,23931941545,4624161959,21365393828,11832293974,22426817320,8776755213,14170311493,15533099132,1603920353,16778252377,4442782626,11983085781,17054527193,20993519107,9208581886,13336024661,8032826332,11858083116,25825626338,15604521466,5110782940,10349232294,4091185929,4965258672,4166862158,3649789605,20040161029,10269828751,6608084616,10572125624,20377270618,11906256996,13391934265,6255713049,17632889154,11378784464,8023927064,10282342089,5904255194,8585778878,9169271006,16565961877,11783994322,5261988664,8347352857,10724258814,5218946207,22290475411,4315145936,8061557386,14203297444,20791547070,16565961877,2487793618,6800634737,9704486454,6005425520,5527485172,18400209211,1898910718,12665129148,7210159495,5261988664,6832844451,10907825876,15797429633,9514958888,14046575927,30593323087,18484820157,3064272542,12259105313,4845467160,5880943513,4935117533,4322563942,13151508334,10588023063,4390833861,1280279130,6546849565,8211619255,11092931158,14103645438,15863663357,7409689268,13478771444,9504416304,12179863375,2602498397,4390833861,4992400670,5177617270,6549717774,15631858019,3991939163,13958806117,6232466790,9887564931,3778174581,6181476236,9819287595,5110782940,9548995311,16824850366,24629666097,2945997327,8055234557,11495302683,7113184419,6546989077,3760661857,2248373102,15002648610,8540380912,8093392019,12920847077,8376504523,11270777519,16639189144,22077445330,17877517387,4019468631,3628927085,14521649658,3136533261,3927132258,3038583662,5845236598,5119570733,15578841094,12541990459,5200447169,1515506892,7754586183,9726767175,6884420263,16706796923,18791814403,15966535615,10116236960,3081883140,5200447169,5913097470,6132515622,7757984026,17549919650,4727893793,12665129148,3870082874,7382150448,4311538196,7400649676,4474656096,7321744124,11631302640,2989067300,6920265121,4390833861,6884531808,14291136319,3488811532,9541504953,9305267381,8425498695,7754751464,4453909556,2662366140,13752338654,5275170263,15305586630,2602498397,13350820262,19710546408,3535415330,21177540576,4760506783,4297849011,17201988538,3714531249,4651119854,3598494575,3934348167,2136618104,18454397716,8023927064,6159561197,1794171093,9185339762,7210159495,8154491641,6744678977,22260668889,2931630476,11983085781,3649789605,6159561197,7003807328,7263742591,5468765566,20789449617,15002648610,4583535914,8744131184,8766046430,4019468631,8672570401,4852710365,3539834679,8196955513,5200447169,3536975035,1686775886,2445084265,11302225508,11022365035,9980140922,9185535571,3152805867,16290618910,6248082468,15199054437,15814957350,13529763539,4187069662,25086935980,5638382778,2487793618,20377270618,4399260579,5508796789,4261796925,4659668217,2529974807,21860945848,9504416304,4306714990,1471103119,653189453,10880291932,8540380912,9659090522,1733233088,6255713049,12078935143,3471791735,7642734883,8603858480,6477426482,16427379164,8199802136,13752338654,5428733015,10357611129,6632303860,10272836137,5747612395,4192305080,9709395657,6159561197,4188917377,1997066113,2895401394,13388075351,11821858638,10880523908,3733808694,19297610254,18004480833,18734114474,2635009478,4959056491,19898940816,9819287595,6678364674,2945997327,11092931158,1615768941,3594660994,6524849729,5518923650,2995967554,14112542440,11258288169,1741567862,772620755,12888228798,11441524040,2052101945,7409689268,14308209818,4111697519,7319601224,10191436080,7672343648,16395351671,3064272542,9712767934,16290618910,6430001634,12269031359,7855820220,12168602059,1280279130,4965258672,11501118383,4306714990,4961245399,2364653585,3428872708,15859091862,11867044221,12888503622,2285479621,13040575850,21327948710,9146354803,3120397609,3271097652,16252632650,11631302640,7910386453,3488811532,1912947241,4257255448,7728523902,1102924833,1085478787,13336024661,2061975798,914105875,15266945160,2429852150,8776755213,8925208492,1733233088,8670031794,12072170914,9087910572,967284918,3628927085,4588346332,6916767048,3895561989,14533408619,14414434331,1515506892,13623695160,5100795163,3273690757,2800118639,18786398744,14057191760,15267270745,2706324641,8127822918,25265118026,3949687833,3695416028,3873943891,2335184088,4852710365,9369909612,1686775886,2265001579,5042202569,5617489836,1305402893,1284735324,2441549284,1081717205,18084908026,2877356551,4390833861,10572125624,10269828751,14300196501,881748751,1144716130,4297849011,5434431700,8192811511,4613719923,4169959434,4029015694,1794171093,13206590011,6041507754,3877015829,3315995340,9208293743,16651765262,5039334309,3204881615,7292313156,13343218647,4677840458,4588109873,2765207387,5747612395,11098943862,1997066113,2682065196,2983028326,6653613713,1545269932,1520785964,2891213649,8377267875,3407495746,5200447169,8211619255,4390833861,4798102622,12141539871,1043385117,1354911247,6436752609,5464490710,4938786758,15644093996,4166862158,4591749066,5968697752,19725444790,3795500597,8637704810,15805952056,5540451523,3274637475,9118240602,2364653585,3176142508,3532680558,7881065063,1829430084,1800424995,3423911661,6159561197,9726767175,5200447169,14382374948,1234868761,1603920353,7624159037,6472362235,5849583388,18531700031,4935117533,3822693817,7069674614,10023481954,4495181474,10231532384,9798237812,3959851313,3878137367,10800802443,3761454628,4183829890,9335173833,2166062379,2131701315,4054976060,4306714990,6159561197,7802109459,9234886337,1461711188,9030828310,6784595489,6928564943,21952522587,4527396116,8373954503,12119671296,11606365859,4689880696,665945447,3559174685,4454848698,1972190142,11057793891,2524150110,1813503580,9241638536,10938987638,1730441645,4812664344,5884584490,8036233546,3815954078,4390833861,12661805152,5362226588,9919078736,7523623729,8220892140,5554715075,787732231,4215216352,5276282799,2335184088,10059924049,2147194939,10946986661,3253276636,2048795046,1615768941,4084402637,6970029249,5767725942,4519411865,5200447169,3362147003,1930233301,8911728477,9737752331,3590179826,932007790,6249400413,2765207387,11916374284,2542504723,12967239167,3852832120,2425934612,1912947241,4837431289,914105875,7341803050,6831591967,5352768022,3981806132,10556156411,11534711292,4251946800,7402210954,3274637475,14115630955,1277578114,15360545336,4563099693,2872715618,2265001579,5729511910,1081717205,8696333358,6340009187,4715889621,12504239389,7642734883,6020756325,5035913640,5230920933,16720995652,1512307121,8376504523,5404523109,3401997838,2682065196,4183823016,1280279130,7509551294,14812049424,7319601224,7131346154,6195662174,1790380469,7319601224,6401321206,3176142508,4955210333,1515506892,8895057480,7209167004,8670031794,4668839530,7338549588,2119801991,8670031794,7582185001,3761454628,5869039674,1794171093,10536407012,10269828751,5529788542,8692479104,2510053484,10269828751,8981103501,4454848698,3962546649,1471103119,12480843141,4390833861,10296421111,2972367625,4390833861,10638342024,5276282799,4693073746,1741567862,14784332914,5200447169,3520051281,5200447169,12601601156,6249400413,5558497745,2061975798,4168868526,6159561197,10757430294,7402210954,3594660994,12742679908,4257255448,5859633323,5042202569,6940470669]
def R14 : Nat := 1184655442
def C14 : Nat := 300

theorem check14 : check 14 succ14 = true := by decide +kernel
theorem wcheck14 : wcheck 1000000000 R14 succ14 weights14 = true := by decide +kernel
theorem wmin14 : weights14.all (fun v => Nat.ble 653189453 v) = true := by decide +kernel
theorem len14 : succ14.length = 919 ∧ weights14.length = 919 := by decide +kernel
theorem w0_14 : weights14.getD 0 0 ≤ C14 * 653189453 := by decide +kernel

/-- The width-14 certificate. -/
def cert14 : Cert := ⟨14, succ14, weights14, 1000000000, R14, C14, 653189453⟩

theorem cert14_valid : cert14.Valid where
  hM := by decide
  hcheck := check14
  hw := wcheck14
  hN := by rw [show cert14.succ.length = 919 from len14.1]; decide
  hlen := by show succ14.length ≤ weights14.length; rw [len14.1, len14.2]
  hmin := wmin14
  hmin0 := by decide
  hC := w0_14

/-- **The channel bound at width 14.** -/
theorem channel_bound_14 (n : Nat) :
    ∃ S : Finset (List Bool), (∀ x : Int → Bool, Clock x → visFrom x 0 n ∈ S) ∧
      S.card * 1000000000 ^ n ≤ 300 * 1184655442 ^ n :=
  cert14.bound cert14_valid n

theorem channel_bound_14_eventually (n : Nat) :
    ∃ S : Finset (List Bool),
      (∀ (x : Int → Bool) (T : Nat), T % 2 = 0 → (∀ t, T ≤ t → evol x t 0 = decide (t % 2 = 1)) →
        visFrom (fun q => evol x T q) 0 n ∈ S) ∧
      S.card * 1000000000 ^ n ≤ 300 * 1184655442 ^ n :=
  cert14.bound_eventually cert14_valid n

theorem channel_ncard_14 (n : Nat) :
    Set.ncard {w : List Bool | ∃ x : Int → Bool, Clock x ∧ visFrom x 0 n = w} * 1000000000 ^ n
      ≤ 300 * 1184655442 ^ n :=
  cert14.ncard_bound cert14_valid n

end Rule30Submission
