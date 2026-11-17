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

/-! ## 6. Width 16 -/

def succ16 : List (Nat × Nat) := [(1,2),(3,4),(5,1000000),(6,7),(8,1000000),(9,10),(11,12),(13,1000000),(14,15),(16,17),(18,1000000),(1000000,19),(20,1000000),(21,22),(23,24),(25,1000000),(26,27),(28,1000000),(29,30),(31,1000000),(32,33),(34,35),(36,1000000),(37,38),(39,1000000),(40,41),(1000000,42),(43,1000000),(44,45),(46,1000000),(47,1000000),(48,49),(50,51),(52,1000000),(53,54),(55,1000000),(56,57),(1000000,58),(59,1000000),(60,1000000),(61,1000000),(62,1000000),(63,1000000),(64,33),(65,66),(67,1000000),(68,69),(70,71),(72,73),(74,1000000),(75,76),(77,1000000),(56,78),(1000000,79),(80,1000000),(81,1000000),(82,1000000),(83,1000000),(84,1000000),(85,86),(87,88),(89,90),(91,92),(93,94),(95,96),(97,98),(99,1000000),(100,101),(1000000,102),(103,1000000),(104,1000000),(105,1000000),(106,107),(108,1000000),(109,78),(1000000,110),(111,1000000),(112,1000000),(113,1000000),(114,1000000),(115,116),(117,88),(118,119),(120,121),(122,123),(124,125),(126,1000000),(127,1000000),(128,1000000),(1000000,129),(130,1000000),(131,1000000),(132,1000000),(133,134),(135,1000000),(136,76),(137,1000000),(1000000,138),(139,1000000),(140,1000000),(141,1000000),(142,1000000),(143,1000000),(144,145),(146,147),(148,92),(1000000,149),(150,1000000),(151,1000000),(152,1000000),(153,1000000),(154,155),(156,157),(120,158),(159,123),(160,125),(161,1000000),(162,1000000),(1000000,163),(164,1000000),(165,1000000),(166,1000000),(167,168),(169,1000000),(170,171),(172,1000000),(173,174),(1000000,175),(176,1000000),(177,1000000),(178,1000000),(1000000,179),(148,180),(181,182),(183,1000000),(184,78),(1000000,185),(186,1000000),(187,1000000),(188,189),(190,191),(192,119),(193,194),(195,196),(197,198),(199,1000000),(1000000,200),(201,1000000),(202,1000000),(203,1000000),(204,205),(206,207),(208,209),(210,211),(212,125),(213,1000000),(214,1000000),(215,1000000),(216,1000000),(217,168),(218,219),(220,174),(1000000,221),(222,1000000),(223,1000000),(1000000,224),(148,225),(226,227),(228,1000000),(229,78),(1000000,230),(231,1000000),(232,1000000),(233,1000000),(234,1000000),(235,1000000),(236,237),(238,239),(240,1000000),(241,1000000),(242,1000000),(1000000,243),(244,1000000),(245,1000000),(246,1000000),(247,1000000),(156,248),(249,250),(251,1000000),(252,1000000),(253,1000000),(254,1000000),(1000000,255),(256,1000000),(257,1000000),(258,259),(260,1000000),(261,171),(262,1000000),(263,264),(265,1000000),(266,1000000),(1000000,267),(268,211),(269,270),(271,1000000),(272,1000000),(273,1000000),(1000000,274),(275,1000000),(276,277),(278,1000000),(218,279),(280,174),(1000000,281),(282,1000000),(148,283),(226,284),(1000000,285),(286,1000000),(287,1000000),(288,1000000),(289,239),(290,1000000),(291,1000000),(292,1000000),(1000000,293),(294,1000000),(295,1000000),(296,1000000),(297,1000000),(298,299),(300,301),(118,302),(120,303),(304,1000000),(305,1000000),(306,1000000),(307,308),(309,1000000),(310,1000000),(311,1000000),(312,313),(314,1000000),(315,316),(317,207),(318,209),(210,319),(320,1000000),(321,322),(323,1000000),(1000000,324),(325,326),(1000000,327),(328,1000000),(329,1000000),(1000000,330),(331,225),(332,333),(334,1000000),(335,78),(1000000,336),(337,1000000),(338,1000000),(339,1000000),(340,239),(341,1000000),(342,1000000),(343,344),(345,346),(347,1000000),(348,349),(1000000,350),(351,1000000),(352,1000000),(353,1000000),(354,1000000),(355,1000000),(356,357),(358,1000000),(359,1000000),(360,1000000),(236,361),(292,1000000),(362,1000000),(363,1000000),(298,364),(118,302),(365,1000000),(307,366),(367,1000000),(368,1000000),(369,370),(371,1000000),(372,373),(374,375),(376,377),(378,379),(380,125),(381,1000000),(382,1000000),(383,1000000),(384,1000000),(385,1000000),(386,387),(1000000,388),(389,1000000),(390,391),(392,1000000),(393,394),(1000000,395),(396,1000000),(397,1000000),(398,1000000),(399,400),(401,270),(402,1000000),(403,1000000),(1000000,404),(405,1000000),(406,1000000),(226,1000000),(407,1000000),(408,409),(410,1000000),(411,1000000),(412,1000000),(413,1000000),(236,414),(415,416),(417,1000000),(418,1000000),(1000000,419),(420,1000000),(421,1000000),(422,1000000),(423,1000000),(300,424),(425,302),(120,426),(427,428),(429,1000000),(430,1000000),(431,1000000),(432,1000000),(1000000,433),(434,1000000),(435,1000000),(436,1000000),(437,1000000),(438,1000000),(439,361),(440,239),(441,1000000),(1000000,442),(443,1000000),(444,1000000),(445,1000000),(446,364),(447,448),(449,1000000),(450,1000000),(372,451),(452,1000000),(453,1000000),(454,387),(455,1000000),(1000000,456),(457,1000000),(458,1000000),(459,1000000),(460,400),(461,1000000),(462,1000000),(463,1000000),(464,1000000),(1000000,465),(466,1000000),(467,277),(468,1000000),(469,470),(471,472),(1000000,473),(474,1000000),(475,1000000),(476,283),(477,1000000),(478,1000000),(479,1000000),(236,480),(1000000,481),(482,1000000),(483,1000000),(484,1000000),(485,1000000),(486,1000000),(487,1000000),(1000000,488),(489,490),(491,492),(493,1000000),(345,494),(348,495),(1000000,496),(497,1000000),(498,499),(439,500),(501,1000000),(502,1000000),(503,1000000),(504,505),(506,507),(508,509),(510,1000000),(511,1000000),(512,513),(514,1000000),(515,1000000),(1000000,516),(517,1000000),(372,518),(374,519),(520,377),(521,379),(522,1000000),(1000000,523),(524,1000000),(1000000,391),(525,1000000),(1000000,526),(527,1000000),(1000000,528),(529,1000000),(530,1000000),(531,505),(532,533),(534,535),(120,536),(537,1000000),(538,1000000),(539,366),(540,1000000),(541,1000000),(542,375),(543,544),(120,545),(546,547),(1000000,548),(549,1000000),(550,387),(551,1000000),(552,1000000),(553,1000000),(554,555),(556,1000000),(557,1000000),(558,1000000),(559,1000000),(1000000,560),(489,490),(491,561),(1000000,494),(562,563),(1000000,564),(565,1000000),(566,1000000),(567,1000000),(568,1000000),(498,569),(1000000,570),(571,1000000),(572,1000000),(573,1000000),(574,1000000),(439,575),(576,1000000),(577,1000000),(1000000,578),(579,1000000),(580,1000000),(581,1000000),(582,1000000),(583,584),(374,585),(586,377),(508,587),(588,379),(1000000,589),(590,1000000),(591,1000000),(592,1000000),(593,1000000),(594,1000000),(595,596),(597,1000000),(598,1000000),(599,1000000),(600,239),(601,1000000),(602,1000000),(450,1000000),(603,604),(605,606),(607,608),(609,610),(611,1000000),(1000000,612),(613,1000000),(614,1000000),(615,1000000),(616,387),(617,1000000),(618,391),(619,1000000),(620,621),(622,1000000),(623,1000000),(624,625),(626,1000000),(464,1000000),(1000000,627),(467,628),(629,1000000),(630,1000000),(631,632),(633,1000000),(634,1000000),(635,1000000),(636,1000000),(542,637),(638,1000000),(639,640),(641,1000000),(642,1000000),(1000000,643),(644,1000000),(645,1000000),(646,387),(1000000,647),(648,391),(1000000,649),(650,651),(652,1000000),(1000000,653),(654,1000000),(655,1000000),(656,470),(657,1000000),(658,1000000),(659,1000000),(660,1000000),(661,480),(562,662),(663,1000000),(664,1000000),(665,1000000),(1000000,666),(374,667),(668,379),(1000000,669),(670,1000000),(671,1000000),(672,1000000),(673,1000000),(674,1000000),(439,675),(676,677),(678,1000000),(1000000,679),(680,1000000),(681,1000000),(682,364),(683,684),(508,685),(686,1000000),(687,1000000),(688,1000000),(1000000,689),(690,1000000),(603,691),(692,693),(694,1000000),(695,1000000),(696,1000000),(697,1000000),(698,1000000),(1000000,699),(700,1000000),(701,702),(703,1000000),(704,1000000),(1000000,705),(706,707),(1000000,708),(709,1000000),(710,1000000),(711,1000000),(712,505),(120,713),(714,1000000),(512,366),(715,1000000),(607,716),(717,1000000),(718,1000000),(1000000,719),(720,1000000),(721,1000000),(722,1000000),(469,723),(724,1000000),(725,555),(726,1000000),(727,1000000),(1000000,488),(728,729),(730,1000000),(236,731),(1000000,732),(733,1000000),(734,1000000),(735,1000000),(736,1000000),(737,1000000),(491,738),(739,1000000),(740,563),(741,1000000),(742,1000000),(743,575),(744,239),(745,1000000),(292,1000000),(746,747),(748,379),(1000000,589),(749,750),(751,1000000),(752,1000000),(656,753),(754,1000000),(1000000,755),(756,1000000),(757,1000000),(758,1000000),(759,760),(761,1000000),(762,1000000),(1000000,763),(764,1000000),(491,765),(766,1000000),(1000000,767),(768,1000000),(769,1000000),(770,283),(1000000,570),(771,1000000),(772,239),(773,1000000),(1000000,774),(775,1000000),(776,1000000),(1000000,777),(778,684),(1000000,779),(780,1000000),(781,1000000),(701,782),(783,1000000),(784,1000000),(785,1000000),(534,786),(787,788),(789,1000000),(450,1000000),(790,791),(792,1000000),(793,1000000),(794,1000000),(795,796),(797,1000000),(546,798),(1000000,799),(800,1000000),(801,1000000),(802,693),(803,1000000),(1000000,804),(805,1000000),(806,400),(807,1000000),(808,1000000),(809,1000000),(236,810),(811,812),(1000000,813),(814,563),(815,1000000),(816,1000000),(631,817),(818,1000000),(819,1000000),(820,379),(821,1000000),(822,1000000),(823,1000000),(824,1000000),(825,1000000),(542,826),(827,544),(120,828),(639,829),(830,1000000),(831,832),(1000000,833),(834,1000000),(1000000,835),(836,1000000),(837,1000000),(838,1000000),(1000000,839),(840,817),(841,1000000),(842,1000000),(843,1000000),(289,844),(845,1000000),(846,1000000),(847,1000000),(1000000,848),(849,1000000),(850,1000000),(374,851),(852,606),(853,587),(1000000,854),(855,1000000),(856,1000000),(857,858),(859,1000000),(860,677),(861,1000000),(862,1000000),(307,863),(1000000,516),(864,1000000),(865,1000000),(866,782),(491,867),(868,1000000),(869,1000000),(870,1000000),(871,1000000),(872,1000000),(873,1000000),(874,875),(876,877),(878,1000000),(879,1000000),(880,1000000),(1000000,881),(686,1000000),(882,1000000),(883,379),(884,1000000),(595,885),(886,1000000),(676,887),(888,1000000),(889,1000000),(300,890),(307,863),(891,1000000),(892,1000000),(1000000,893),(1000000,788),(894,1000000),(1000000,895),(896,1000000),(806,897),(815,1000000),(898,1000000),(820,899),(900,1000000),(542,901),(902,1000000),(903,1000000),(904,1000000),(905,832),(618,1000000),(619,1000000),(393,906),(1000000,907),(908,909),(910,1000000),(834,1000000),(911,1000000),(912,1000000),(913,1000000),(914,1000000),(631,915),(916,1000000),(917,918),(919,1000000),(920,1000000),(491,921),(922,1000000),(1000000,923),(924,1000000),(925,1000000),(926,1000000),(927,1000000),(928,1000000),(929,1000000),(439,930),(931,932),(933,1000000),(1000000,934),(935,1000000),(936,937),(938,1000000),(939,1000000),(1000000,940),(706,707),(749,941),(751,1000000),(1000000,942),(943,1000000),(944,1000000),(728,760),(761,1000000),(945,1000000),(946,1000000),(947,760),(948,1000000),(439,949),(950,932),(951,1000000),(952,1000000),(745,1000000),(953,954),(955,956),(957,684),(958,1000000),(959,1000000),(1000000,960),(369,961),(962,1000000),(963,1000000),(964,1000000),(965,1000000),(1000000,966),(967,1000000),(968,1000000),(969,1000000),(970,1000000),(971,1000000),(972,1000000),(973,786),(790,974),(542,975),(1000000,976),(977,1000000),(1000000,978),(979,1000000),(980,1000000),(981,1000000),(595,982),(439,675),(1000000,983),(984,954),(300,985),(986,1000000),(987,1000000),(988,1000000),(989,990),(991,1000000),(992,1000000),(1000000,993),(369,707),(994,1000000),(995,1000000),(701,937),(996,1000000),(997,1000000),(998,1000000),(999,1000000),(1000,1000000),(1000000,267),(1001,1000000),(1000000,804),(1002,897),(1003,1000000),(1004,1000000),(1005,1000000),(840,1006),(1007,1000000),(1008,1000000),(1009,1000000),(1010,1000000),(1011,1000000),(1012,1000000),(1000000,1013),(1000000,729),(1014,1000000),(1015,1000000),(1016,1000000),(491,1017),(1018,1000000),(1000000,1019),(1020,1000000),(1021,1000000),(1022,1023),(1024,1000000),(1025,1000000),(1000000,1026),(1027,1000000),(1028,1000000),(1029,379),(1030,1000000),(671,1000000),(1031,1032),(1033,1000000),(603,875),(1034,1000000),(1000000,1035),(1036,1000000),(1037,505),(1038,1000000),(1039,1000000),(1000000,1040),(1041,1000000),(1000000,1042),(1043,1000000),(542,1044),(1045,1000000),(1046,1000000),(1000000,669),(1047,1000000),(1048,1000000),(1049,1000000),(1050,1000000),(770,1051),(1052,1000000),(1053,1000000),(1054,887),(1055,1000000),(1056,1000000),(1057,1000000),(1058,1059),(1060,1000000),(1061,1000000),(1062,1063),(1064,1000000),(1065,1000000),(1066,1000000),(1000000,1067),(620,1068),(1000000,1069),(1070,1000000),(1071,1000000),(1072,1073),(236,1074),(1075,1076),(1077,1000000),(1078,1000000),(1000000,1079),(820,1080),(1000000,1081),(1082,901),(1083,544),(193,1084),(1000000,1085),(1086,1000000),(1087,1000000),(1088,1000000),(1089,1000000),(1090,1000000),(1091,1092),(1000000,1093),(1094,1000000),(1095,1000000),(1096,1000000),(1097,1063),(1098,1000000),(1099,693),(1000000,1100),(1101,1000000),(1102,391),(1103,1000000),(1104,1105),(1000000,1106),(1107,1000000),(1108,1109),(1075,812),(542,1110),(193,1111),(1112,1113),(1114,1115),(1000000,1116),(1117,1000000),(1118,921),(1119,1000000),(1120,1076),(1121,1023),(1122,1000000),(1123,596),(542,1124),(1125,569),(1000000,1126),(1127,1000000),(1128,1000000),(1129,1000000),(1000000,1130),(1131,1132),(1133,1134),(1135,1000000),(857,1136),(1137,1000000),(1000000,777),(1138,1139),(1140,1141),(1142,1000000),(1143,1000000),(1000000,370),(1144,1000000),(1000000,1145),(1146,1000000),(866,937),(1147,1000000),(1148,1000000),(1149,1000000),(1150,1000000),(661,1074),(1151,1000000),(1152,1000000),(1153,1154),(1000000,1155),(1156,1000000),(1157,1000000),(1158,1000000),(1159,1000000),(1160,909),(1161,1000000),(1000000,1162),(1163,1000000),(1164,1000000),(1165,1000000),(1125,1166),(676,1167),(1025,1000000),(1168,1169),(1170,691),(790,1171),(1000000,1172),(1173,1113),(1174,1000000),(1175,1000000),(1176,1000000),(1000000,1177),(1178,1000000),(1179,1180),(1181,1000000),(1182,1000000),(1000000,1183),(1184,1000000),(1185,1000000),(1186,1000000),(1187,1000000),(1188,1000000),(1000000,1189),(491,1190),(1191,1000000),(1192,1000000),(1193,1000000),(927,1000000),(1194,930),(1195,932),(1196,1000000),(1197,1000000),(1198,1000000),(1199,1000000),(1000000,699),(1200,1000000),(1201,1000000),(1202,1000000),(869,1000000),(1203,1000000),(374,1204),(1205,1000000),(1206,1000000),(1207,1000000),(1208,1000000),(603,1209),(193,1210),(1211,1000000),(1179,1212),(1213,1000000),(1214,1000000),(1215,1000000),(1031,875),(1000000,1216),(1089,1000000),(1217,1000000),(1218,1000000),(1219,1000000),(1220,1000000),(1118,1190),(1221,1000000),(1222,1000000),(943,1000000),(1223,1000000),(1224,1000000),(1225,1000000),(1226,1000000),(1227,1000000),(1228,575),(1229,1000000),(692,1113),(1230,1000000),(1231,1232),(1000000,1233),(1234,1000000),(1235,1000000),(1236,1000000),(1237,1000000),(1194,675),(1238,1000000),(1239,1000000),(1240,1000000),(1241,1000000),(1242,1000000),(701,1243),(1244,1000000),(1245,1000000),(1246,1000000),(1247,1000000),(1248,1000000),(1249,1000000),(1250,391),(1251,1000000),(1252,394),(1000000,1253),(1150,1000000),(1254,1000000),(1255,875),(1000000,1256),(1000000,1257),(1258,1000000),(1259,1260),(1261,1000000),(1262,1000000),(1263,753),(1264,1000000),(1265,1000000),(917,1266),(1267,1000000),(1268,1000000),(1269,1270),(1271,1076),(1272,1000000),(1273,1000000),(542,1274),(1000000,854),(1275,1000000),(1276,1000000),(1277,1000000),(1278,1000000),(1279,1000000),(1280,1000000),(1281,1000000),(1282,1000000),(916,1000000),(1283,1284),(1000000,1285),(1286,1000000),(1287,1000000),(1288,1000000),(1000000,1289),(1290,1000000),(1291,1000000),(1292,1000000),(1293,1000000),(439,1294),(1121,1295),(853,608),(1296,1297),(1298,1000000),(1299,1000000),(884,1000000),(1300,1301),(1302,1000000),(1000000,1303),(862,1000000),(1000000,1304),(1305,1000000),(1300,569),(1306,1297),(1000000,1307),(476,1308),(1309,877),(1310,851),(1311,693),(1312,1000000),(1313,1314),(1000000,1315),(1316,1000000),(1160,1000000),(1317,1000000),(1318,1000000),(1120,1319),(1320,1000000),(1321,575),(1000000,1322),(1323,1000000),(1324,1000000),(586,1000000),(508,608),(1325,1297),(1326,1000000),(1300,1327),(1328,1000000),(1000000,1329),(1330,1000000),(586,606),(1131,1331),(1332,1333),(538,1000000),(1000000,1334),(1000000,1335),(1250,1336),(1337,1000000),(1338,1000000),(1339,544),(1272,1000000),(1340,1000000),(1296,1341),(1000000,1342),(1343,1000000),(1344,1345),(1000000,1346),(1347,1348),(809,1000000),(1349,569),(1152,1209),(193,1350),(1351,1000000),(1000000,1352),(1353,1000000),(1000000,1354),(1355,1000000),(1356,1000000),(1357,1000000),(1358,1000000),(1359,1000000),(1360,1000000),(1361,1000000),(1031,1362),(1363,1000000),(981,1000000),(1259,867),(1000000,1364),(1000000,1365),(1366,1000000),(1367,877),(1368,1000000),(1000000,1369),(1370,1000000),(1371,1000000),(1372,1000000),(1373,1000000),(439,1374),(1375,1000000),(1376,1000000),(1377,1000000),(1000000,1378),(1379,1380),(1000000,1381),(1382,1000000),(1000000,1383),(1384,1000000),(1385,1000000),(1386,1000000),(1387,1000000),(1273,1000000),(374,1388),(1306,1341),(1000000,1389),(1390,1000000),(1037,1391),(1138,1392),(1393,1000000),(1394,1000000),(1395,1000000),(1396,1000000),(1000000,1397),(1398,1000000),(1399,1000000),(706,1400),(1401,1000000),(1402,1000000),(661,1362),(1403,1000000),(1404,1000000),(1405,1000000),(936,1243),(1406,1000000),(1407,1000000),(1408,1409),(1410,1000000),(1411,1000000),(1412,1000000),(1413,1000000),(945,1000000),(1414,1000000),(1415,1416),(1417,1000000),(770,1308),(1418,1000000),(1419,505),(1420,1000000),(1421,1000000),(1311,1000000),(995,1000000),(1422,1397),(1423,1000000),(1424,1000000),(1194,930),(1425,1000000),(1426,875),(1427,1000000),(1428,1000000),(1429,1000000),(1430,1000000),(1431,1000000),(1432,1000000),(1433,1000000),(1269,1434),(1000000,1435),(1000000,1436),(1437,1000000),(1438,1000000),(1439,1000000),(1118,1260),(1440,1000000),(1441,1000000),(1442,1000000),(1443,1000000),(1444,1000000),(1445,1000000),(1446,1000000),(1447,1000000),(1448,875),(1449,1000000),(1450,1451),(852,544),(1306,1452),(1453,1454),(1000000,1455),(820,1297),(1456,1000000),(1457,1000000),(1000000,1458),(1459,1000000),(1460,1000000),(1000000,1461),(1058,1462),(1463,1000000),(1464,1000000),(1000000,1465),(1000000,1466),(706,1467),(1000000,1335),(1468,1000000),(1469,1076),(1470,1000000),(1000000,1471),(1472,1000000),(1473,1000000),(1474,1000000),(1475,1000000),(1321,875),(1476,1000000),(374,1477),(1478,1000000),(1000000,1479),(1480,1000000),(1481,1000000),(1482,1000000),(1483,1000000),(1484,1000000),(1485,1000000),(1000000,1486),(1173,693),(1487,1000000),(1252,1488),(1489,1000000),(1490,569),(1000000,1491),(1492,1000000),(1493,1000000),(795,1494),(1495,1000000),(1496,1000000),(1497,1000000),(1498,1000000),(1000000,1499),(1102,1000000),(1500,1000000),(1000000,1501),(1000000,1026),(439,1374),(1000000,1502),(1503,1000000),(1504,1000000),(1505,1000000),(1031,1506),(1507,1000000),(639,1154),(1000000,1508),(1509,1000000),(1510,1000000),(1000000,1511),(193,1512),(1150,1345),(1513,1000000),(1514,1515),(1516,1000000),(1349,1517),(749,1000000),(1518,1000000),(1000000,1519),(1450,1520),(1521,1000000),(1522,1000000),(1523,1000000),(1158,1524),(1325,1525),(1000000,1526),(1300,1000000),(1527,1000000),(1000000,1528),(1000000,1529),(1530,1000000),(1531,1308),(1000000,1532),(1533,1000000),(1534,1000000),(1535,1000000),(1536,1000000),(1537,1000000),(1538,1000000),(1539,1000000),(1540,1000000),(1541,1000000),(1542,1000000),(1543,1000000),(1544,1000000),(1545,1000000),(1546,1000000),(1547,1000000),(1548,1000000),(236,1362),(1549,1000000),(1550,1000000),(1551,1000000),(1552,1000000),(1553,1000000),(1554,1000000),(1194,1374),(1555,1000000),(1556,1000000),(1370,606),(1000000,1331),(1557,1000000),(1558,1000000),(1559,1000000),(1560,1000000),(1561,1000000),(661,1562),(1563,1000000),(1564,1565),(1566,1000000),(1567,1568),(1569,1000000),(1570,1000000),(1571,1572),(1573,1000000),(1574,1000000),(1575,1000000),(1576,1000000),(1000000,707),(1000000,1577),(1578,1000000),(1579,867),(1000000,1580),(1000000,1581),(1582,1583),(1584,1000000),(1585,1000000),(1586,1000000),(1587,1000000),(1588,693),(1000000,1589),(1590,1000000),(1591,1000000),(1592,1000000),(1293,1000000),(1259,1593),(1000000,1594),(1595,1000000),(1596,1000000),(1000000,1597),(1598,1000000),(1599,1000000),(1000000,1600),(1601,1000000),(1120,812),(1602,1000000),(1603,1000000),(706,1604),(1605,1167),(1054,1167),(1606,1000000),(1607,1000000),(1608,1000000),(1609,1000000),(1610,1000000),(1611,1000000),(1000000,1612),(577,1000000),(1613,1000000),(1614,1113),(1000000,1615),(1616,1617),(1000000,1618),(1619,1000000),(1620,1524),(1000000,923),(1621,1000000),(1622,1000000),(1623,1000000),(1624,1362),(1625,1000000),(1626,1583),(1627,1000000),(1628,1000000),(1629,1000000),(1091,1630),(1631,932),(1632,1000000),(1633,707),(917,1634),(1000000,1635),(1296,1080),(1636,1000000),(1588,1637),(1626,1113),(1077,1000000),(1000000,1638),(1639,1000000),(1640,1000000),(1194,1374),(1058,937),(1641,1000000),(1642,1000000),(1643,1000000),(1644,1000000),(1645,875),(1646,1647),(1648,1000000),(1649,1000000),(508,1650),(1651,1652),(1653,1000000),(1306,1654),(1655,1000000),(1000000,1656),(1363,1000000),(1657,1000000),(1658,1000000),(1659,1000000),(1660,1000000),(489,1661),(374,1662),(1663,1000000),(1664,1345),(1665,1000000),(1666,1000000),(1667,1362),(1668,1000000),(1669,1000000),(1670,1000000),(1671,1000000),(820,1654),(1556,1672),(1673,1000000),(1000000,1528),(1000000,1674),(1675,1000000),(795,1676),(1677,1678),(1619,1000000),(1679,1000000),(1058,1680),(1681,1682),(1683,569),(820,1684),(1685,1000000),(1686,1000000),(1269,1687),(1688,1000000),(1296,1565),(1689,1000000),(1690,1000000),(1691,1000000),(1418,1000000),(1692,1000000),(439,1693),(1694,1000000),(1592,1695),(1696,1000000),(1000000,1697),(1698,1000000),(1699,812),(1700,1000000),(1701,1000000),(1702,1000000),(746,1703),(1704,1000000),(1000000,1705),(1706,1000000),(1707,1000000),(1708,1000000),(1709,1000000),(1000000,1710),(1711,1000000),(1712,1000000),(692,1454),(1713,1000000),(1300,1524),(1000000,983),(1714,1466),(1000000,1715),(1716,1000000),(1717,1718),(1719,1000000),(1000000,1720),(1721,1000000),(1722,1000000),(1723,1000000),(1724,1000000),(1000000,1725),(1726,1000000),(1727,1167),(1728,1000000),(1549,1000000),(1296,899),(1000000,1729),(1730,1000000),(1731,1000000),(1732,1000000),(1733,832),(1734,1000000),(1000000,1322),(1735,1000000),(1736,1000000),(1737,1738),(1000000,1739),(1740,1000000),(1741,1000000),(1742,1000000),(1743,1000000),(1744,1000000),(1741,909),(1745,1000000),(1746,1000000),(1747,1000000),(1000000,1748),(1749,1000000),(1750,1000000),(1751,1000000),(1752,1000000),(1753,1000000),(1000000,1754),(1755,1000000),(1756,1000000),(1757,1167),(1000000,1758),(986,1000000),(1000000,1303),(1759,1000000),(1760,1000000),(1761,1000000),(1762,1000000),(1763,1000000),(1764,1000000),(1000000,1765),(1766,1000000),(1000000,1767),(1000000,1768),(1769,1000000),(1770,1000000),(1771,1000000),(1772,1000000),(1773,1000000),(1000000,1774),(1775,1000000),(1776,1000000),(1777,1000000),(1778,1000000),(820,1779),(1624,1074),(1000000,1780),(1781,1000000),(1000000,1782),(1783,1000000),(1784,1000000),(1785,1786),(1787,1000000),(1788,1000000),(1347,1789),(1000000,1790),(1791,1000000),(1792,1000000),(1793,1794),(1058,1795),(1000000,1796),(1797,1000000),(1426,1000000),(706,1798),(1412,1000000),(1799,1000000),(926,1000000),(1800,1454),(1000000,1801),(1802,1000000),(1803,1000000),(1804,1000000),(1426,1209),(1805,1000000),(1000000,1806),(1807,1583),(1808,1809),(1556,1656),(1810,1000000),(787,1811),(1812,1000000),(1813,1000000),(1000000,1814),(947,1815),(1816,1000000),(1300,1817),(1818,1000000),(1819,1000000),(706,1820),(1821,1822),(1823,1000000),(905,1824),(1825,1000000),(1000000,719),(1826,1000000),(1000000,1026),(1827,1000000),(1828,1000000),(1000000,1829),(1830,1000000),(1831,1000000),(1000000,1832),(979,1000000),(1571,1833),(1834,1000000),(1000000,1835),(1836,1000000),(1837,1362),(1271,1617),(1838,1000000),(603,1839),(1840,1000000),(1841,1000000),(1514,1000000),(1842,1000000),(1000000,1843),(1844,1000000),(1845,1000000),(1846,1000000),(1847,1000000),(1848,1000000),(1849,1000000),(1850,1000000),(1851,1092),(1852,887),(1853,1000000),(1854,1000000),(1855,1000000),(1856,1000000),(1857,1345),(824,1000000),(1000000,1858),(1859,1000000),(1860,1000000),(1000000,1861),(1862,1000000),(1863,1000000),(1864,1000000),(1865,1000000),(1866,1000000),(1867,1000000),(1868,1000000),(1000000,1869),(1870,1000000),(1000000,1871),(374,1872),(1873,1000000),(880,1000000),(1000000,1874),(1875,1000000),(1876,1684),(1000000,1877),(1878,1000000),(1879,1000000),(1880,1000000),(1881,1000000),(1882,1000000),(917,1883),(1000000,875),(1884,1260),(1885,1000000),(1886,1000000),(1857,1000000),(1887,1000000),(1888,1000000),(1889,1000000),(1000000,1890),(1891,1000000),(1892,1000000),(1893,1000000),(1894,1000000),(1895,1000000),(1300,1794),(1896,932),(1897,1000000),(1898,1000000),(1899,1900),(1901,1000000),(853,1902),(1903,1454),(1000000,1904),(1000000,1905),(1906,1000000),(1907,1000000),(790,1908),(1909,1000000),(795,1682),(1910,1000000),(1000000,1911),(1271,1000000),(1912,1000000),(1000000,923),(1913,1000000),(1914,1000000),(1915,1362),(1807,1617),(1000000,1335),(706,1916),(1000000,1917),(1000000,1918),(706,1919),(1920,1000000),(1000000,1921),(1922,1000000),(1923,1000000),(1924,1000000),(1925,1000000),(1926,1927),(936,1928),(1929,1000000),(1000000,1930),(1000000,1931),(1932,1000000),(1884,1593),(1933,1000000),(1934,1000000),(1935,1000000),(692,1617),(1261,941),(1936,1076),(1937,1000000),(1938,1000000),(1939,1000000),(1306,1000000),(1940,1000000),(1000000,1941),(1942,1000000),(1943,1000000),(1944,1945),(1588,1000000),(1946,1000000),(1947,1000000),(1948,1000000),(1000000,1949),(1950,1000000),(1951,1000000),(1952,1000000),(1953,1000000),(1954,1000000),(1000000,1955),(1956,1000000),(1000000,1957),(374,1388),(1958,1000000),(1959,1345),(1960,693),(1961,1000000),(1962,1000000),(824,1000000),(1963,1000000),(1964,1000000),(1965,1000000),(1966,1967),(1968,1000000),(1633,1969),(1563,1000000),(1970,1000000),(1971,1167),(1972,1000000),(1973,1000000),(1974,1000000),(1306,1975),(1976,1000000),(1977,1000000),(374,1978),(1426,691),(1979,1000000),(1000000,1980),(1981,1000000),(1982,693),(1983,1000000),(1984,1000000),(1985,1000000),(1986,1000000),(1000000,1987),(1031,1988),(1250,1000000),(1989,1000000),(1990,1000000),(1000000,1991),(1992,1000000),(1993,1000000),(840,1994),(1000000,777),(1995,1000000),(1269,1996),(1997,1000000),(1998,1000000),(1999,1000000),(2000,1000000),(706,2001),(811,1000000),(1020,1000000),(2002,1000000),(1000000,2003),(2004,1000000),(2005,1000000),(1000000,1189),(1058,2006),(2007,1000000),(1000000,2008),(2009,1000000),(2010,1000000),(1000000,2011),(1000000,2012),(1000000,2013),(2014,1000000),(2015,1000000),(706,1467),(2016,1000000),(2017,1000000),(2018,1362),(2019,1000000),(1000000,1635),(2020,1000000),(2021,1000000),(1851,2022),(1000000,2023),(580,1000000),(1608,1000000),(2024,1000000),(2025,1000000),(2026,1000000),(2027,1000000),(2028,2029),(2030,932),(933,1000000),(2031,1000000),(2032,1000000),(1000000,2033),(2034,1000000),(746,2035),(2036,1167),(2037,1000000),(2038,1000000),(2039,1000000),(1271,1000000),(2040,1000000),(2041,1000000),(1104,2042),(2043,1000000),(2044,707),(1000000,1532),(2045,1000000),(2046,1000000),(2047,1000000),(603,2048),(2049,569),(1469,1076),(1470,1000000),(2050,1000000),(2051,1000000),(1000000,2052),(1000000,2053),(2054,1000000),(2055,1000000),(2056,1000000),(603,2057),(1000000,2058),(2059,1000000),(2060,1000000),(2061,1000000),(1000000,2062),(2063,1000000),(1000000,1820),(2064,1000000),(2065,693),(2066,1000000),(1058,2067),(1633,1798),(1000000,923),(2068,1000000),(2069,1000000),(2070,1000000),(2071,1000000),(1000000,2072),(2073,1000000),(2074,1000000),(2075,1000000),(1000000,2076),(2077,1000000),(2078,1000000),(1000000,2079),(1699,1076),(2080,1000000),(2081,1000000),(2082,1000000),(1000000,1525),(1031,1000000),(2083,1000000),(2084,1000000),(1173,1583),(1000000,2085),(2086,1000000),(2087,1000000),(1000000,2088),(1000000,1345),(2089,1000000),(2090,1000000),(2091,1000000),(802,1113),(1000000,2092),(746,1703),(1131,2093),(2094,1000000),(1000000,2095),(746,2096),(2097,1000000),(2098,1000000),(2099,1000000),(2100,1000000),(2101,1000000),(2102,1000000),(2103,1000000),(2104,1000000),(2105,1000000),(2106,1000000),(2107,1000000),(1415,2108),(2109,1000000),(2110,1000000),(1000000,2111),(1194,2112),(2113,1000000),(2114,1000000),(2115,1000000),(1000000,2116),(2117,1000000),(2118,1000000),(2119,1000000),(1000000,2120),(1194,575),(1000000,2121),(2122,1000000),(1579,2123),(2031,693),(2124,1000000),(439,2125),(2126,2127),(686,1000000),(2128,1000000),(1000000,2129),(1741,1000000),(2130,1000000),(2131,1000000),(746,2132),(2133,1000000),(840,2134),(2135,1000000),(2136,1000000),(2137,1000000),(1000000,2138),(2139,1000000),(2140,1000000),(2141,693),(2142,1000000),(1000000,2143),(2144,1000000),(2145,1000000),(2146,1000000),(2147,1000000),(2148,1000000),(2149,1000000),(2150,1000000),(2151,1000000),(2152,1000000),(2153,1000000),(1000000,2154),(2155,1000000),(1851,2156),(2157,1000000),(1000000,2158),(1852,1167),(2159,1000000),(2160,1000000),(2161,1000000),(2162,1000000),(1000000,1980),(1094,1000000),(2163,1362),(1549,1000000),(1579,2164),(1415,2165),(2166,1000000),(2167,1000000),(1000000,2168),(2169,1000000),(2170,1000000),(2171,1000000),(1296,1452),(2172,1000000),(1000000,2173),(1000000,2174),(2175,1000000),(1737,2108),(2176,1000000),(2177,1000000),(2178,1000000),(1091,2156),(1000000,2179),(2180,1000000),(706,2181),(1000000,2182),(2183,1000000),(1000000,2184),(2185,1000000),(2186,1000000),(2187,1000000),(1000000,2188),(2189,1000000),(2190,1000000),(2191,1000000),(1269,2192),(2193,1000000),(2194,1000000),(1415,2195),(2196,1000000),(2197,1000000),(2198,1000000),(2199,1000000),(2200,1000000),(1592,2174),(2201,1362),(2202,1000000),(1756,1000000),(706,2203),(2204,2205),(2206,1000000),(1000000,2207),(1259,1017),(2208,2209),(1000000,777),(2210,1000000),(2211,1000000),(1469,1000000),(2212,1000000),(1000000,2213),(2214,1000000),(2215,1000000),(2216,1000000),(2217,1000000),(2218,1000000),(2141,1617),(1000000,2219),(706,1798),(2220,1000000),(2221,1000000),(2222,875),(1000000,2223),(1000000,2224),(2225,1000000),(2226,1000000),(2227,1000000),(2228,1000000),(2229,1000000),(2230,1000000),(2231,1000000),(2104,2232),(2122,1000000),(1000000,2233),(2234,1000000),(1000000,2235),(706,2236),(2237,1000000),(2238,1000000),(2239,1000000),(1000000,2240),(2241,1000000),(1965,1000000),(2242,1000000),(2243,1000000),(2244,1000000),(2245,1000000),(2246,1000000),(2247,1000000),(2248,1362),(1851,1294),(1727,2249),(2187,693),(1000000,2250),(2251,1000000),(2252,1000000),(2253,1000000),(1000000,2254),(2255,1380),(1827,1000000),(2256,1000000),(2257,1000000),(2258,1000000),(2259,606),(1099,1113),(1000000,1465)]
def weights16 : List Nat := [92830470123,61435134354,46165339455,45916486581,25293013644,53509970007,30790082615,22431436740,29316431800,39928066932,22095213800,15868061254,19820135098,25999519681,25011770937,8968286697,29729389810,16550830233,25609796932,18391777471,22972706723,21356497283,8778859912,25874082425,3116355042,10394108304,15066398055,19392327621,19183188821,21409942627,8273679120,21317068268,17848056700,8778859912,21662954512,3090580774,10174539861,12602469766,17387490541,3611015020,7399020916,4647786215,17462553299,22476826351,13804448117,8429961072,24815485022,9588974516,15928972407,8778859912,17821541172,2865289147,10174539861,12402603206,12706152937,3581139541,7399020916,4393279964,14606563819,20152978823,4184385444,8575140307,5386128226,20239985571,17273271648,13332878194,2666923036,9770124100,11417532264,17345386214,6465773949,4647786215,15853474486,2608906106,10174539861,7949942742,12706152937,3319999428,4393279964,14374894425,14726745032,4149756166,8575140307,5091124851,16929549988,14989934195,8368578331,3152899980,1696090761,6953624245,2984779960,1687503590,4554451883,14680503882,8778859912,17155296099,2865289147,6409236173,9043958828,3090069213,7051377255,4272157071,13233078609,20104174841,7493394749,5386128226,7804419243,10570450233,3022820609,7399020916,9213724982,14726745032,3847063344,5091124851,16661017283,8700276076,8368578331,3112760478,6953624245,2984779960,1634045798,4265965260,12817571322,6804599163,15849400691,1524521595,9698974107,3653375060,1964757744,8058871901,3458503780,1954804317,5277942505,14504316034,2510939225,10174539861,7177684495,3319999428,7427860578,10481821312,3580546533,8172179448,4950728839,15337515290,14989934195,8312008643,6419892887,2264638023,1687503590,9045045734,12251208506,3502597308,8575140307,10678600667,8700276076,8368578331,2860474181,1597519646,4265965260,12506309605,8558929867,9698974107,3606848545,8058871901,3458503780,1892840302,4943551791,12866439089,1989453134,7886133993,6430816652,11939330815,1765888446,6863025591,4378037319,4233485896,2276175086,9339986921,4007606693,2264638023,4429051616,6353067993,10457964405,2909265204,7399020916,8318584707,3847063344,8608568821,4818793579,7329683370,2483746905,1665321839,6486544096,1593906296,4143368886,11070178346,6706632283,15849400691,1524521595,9633403030,7440213053,2623772572,1954804317,10483081120,6567965773,7631443808,2461196565,1597519646,6953624245,2984779960,6224916734,6151651113,8558929867,9698974107,3314418362,1850501959,4943551791,12505649306,14570353,9905043924,6863025591,4179556063,9339986921,4007606693,2192814273,4041452538,6353067993,8559467942,2304800039,4746483046,7452874989,13837905886,2045661650,7953857189,5073456790,4905904151,1035117617,1602027616,6587799531,4237153842,4644083046,2623772572,5132588508,7362754897,12120823895,3370972926,8575140307,9641025331,1597519646,5974352714,4002799020,5584346159,8494769795,2877746084,1929092861,7517469776,1846313786,4801447840,10841000289,1989453134,7772578588,6430816652,1765888446,6863025591,4302032550,8622886900,3040052727,2264638023,5998286052,6428042227,1183804922,8844546464,2851607529,1850501959,8058871901,3458503780,5432864296,1781347790,7129288603,9905043924,6863025591,3840594287,2143738880,4041452538,8141269173,15673323,11479922478,7953857189,4843392983,6587799531,4644083046,2540520201,4683314534,7362754897,9920238059,2670325027,5500529623,8637563579,8545498971,7493083876,1035117617,1334834820,2264638023,4245485850,5685317811,1198610378,1855727239,5722394759,1912442139,4910155837,5381835728,3040052727,1634045798,4314026638,8533103504,6473404009,7574874119,2308628067,6953624245,4948976398,1850501959,5481987669,1441790562,4638510332,6471713700,6334158762,3511086406,3334438534,2234835195,8712436681,2138884440,1522788010,5194946333,7369862232,2304800039,4614858665,7452874989,2045661650,7953857189,4985358116,5756594351,3522571516,2623772572,5170172065,1781347790,14570353,7435088628,1370956839,5976777390,4273901036,3304140805,2143738880,9339986921,4007606693,6296128090,2063580902,3869208136,4393279964,11479922478,7953857189,4450495490,1448518116,9435495369,16951794,4759897243,5612859840,1912442139,5381835728,2943553210,1113283199,4314026638,8533103504,5441263327,6056271039,1496492800,1597519646,3699870731,2674689603,5146933299,4863826900,8379524575,8684170646,1198610378,1546018654,2623772572,4919813690,5481987669,1106764344,1388118149,2149795609,594787629,6036941087,2215535029,2303396229,3386849908,6236979858,3522571516,1892840302,4999260724,4281588671,5608089679,6318433766,8778975387,2674762278,8058871901,5735243839,2143738880,1669993211,2018401804,3356974429,7500279433,7340836886,4068556324,3863800025,1554109709,6587799531,3509747568,2478009032,1763879138,6020352511,8541341834,2670325027,5347961124,8637563579,1334834820,6953624245,4143368886,5209257624,1462112493,4081868848,3040052727,5991636187,2063580902,15673323,8616946960,1587888414,6926588847,4952750307,3828681314,1035117617,6587799531,4644083046,7296754697,2390723020,4483662404,5091124851,8545498971,6953624245,2264638023,5157444363,1677791255,5494395939,18433692,5516078317,5398000159,2215535029,6236979858,3410716962,1289213785,4999260724,4281588671,6305863550,7018731603,1733399733,1850501959,4287379928,3099071740,4183351758,5636545332,14570353,9697091601,6221774003,3843009544,1388118149,1790806112,3040052727,1659988272,6353067993,1281657528,1607780444,1455538593,688214943,6996325815,2566856139,2668697977,3924551264,7228194800,4081868848,2192814273,1593906296,4199623201,3180313115,1781347790,6499235481,7308039235,4197896267,3099155878,9339986921,2382238220,4264384198,1448518116,1934507520,2338355060,3889921986,4086747385,4605763471,6486544096,2021153869,1634045798,3080685251,4477393675,1800184619,5722394759,1912442139,4067004401,2871095240,2043332767,6977097582,4457964326,1597519646,3523025480,5146933299,1546018654,8058871901,4801447840,1693548775,4730161749,3522571516,6943811944,2390723020,16951794,5381099485,920861832,918476365,6002201285,2025333328,4105572513,4436686866,1198610378,5722394759,5381835728,8456601328,1172400429,3198055491,1997833340,4265965260,8379524575,1524521595,8058871901,2623772572,4870118815,1943546391,6367450762,20151385,4695096332,1697486840,6255716358,2566856139,7228194800,3952215960,1493138506,1781347790,5871158141,2263181071,2008003363,2143738880,4968373767,3590981707,4847792682,4149980761,15673323,11238880712,7210569411,4453295201,1607780444,1039426594,3522571516,1922910751,7362754897,1484379757,1862395460,1685928833,796508433,4983573800,3124794355,1477586756,417437054,2913766048,3513305283,4730161749,2540520201,1846313786,4866653385,3685150097,2063580902,3597923745,3934256958,8469681428,4864651633,3591079115,6587799531,2760085286,4941719146,796049955,1445061455,1193901962,1515317405,1593906296,2913766048,3582755066,1153061294,5337418714,7517469776,2341545158,1892840302,3569669594,4081858186,2085415030,594787629,2215535029,1440485655,3272446471,3326729452,2367253151,3850034894,4236045334,5166101727,4082395000,1781347790,1790806112,9339986921,1522788010,4041452538,1961811255,5481611220,4081868848,8047498211,1597519646,18433692,4711604673,1524521595,1066174172,1063409135,6956058160,2346389641,4757637297,4034674098,1388118149,594787629,6236979858,4215149499,5585853622,1357737678,3705715644,2314513883,4943551791,14570353,1765888446,9339986921,3040052727,5643838355,796049955,1508268223,22142393,5440966212,1966376129,7249912634,1477586756,3513305283,4579878451,1729511799,2063580902,6804163429,2622083822,2326301997,1448518116,2094556841,3663170711,4161164554,5617959659,4809111807,16951794,8266102559,6671328212,1685374054,3526643926,1862395460,1203604985,4081868848,2227669541,8533103504,923309241,1053863837,1103661044,1952978824,922033608,5775346338,3620797268,1711485310,482644277,3376190139,2366791299,1704336795,5481611220,2943553210,2138884440,1440198447,4199623201,4270316887,2390723020,4169211155,4559061936,5210401018,4003455549,4161277325,3198055491,4132925570,921502189,1673784571,1382660490,1755219791,1846313786,3376190139,4137058330,1335321257,4488008338,8712436681,2712917219,1419955558,2716505738,4730149377,1380913756,688214943,2566856139,1668480735,3791943925,3854864326,2742715852,1281125038,4908870960,3723737111,4730771568,2063580902,1035117617,6587799531,1763879138,999336358,1273423368,1488804665,3740949765,5585853622,1850501959,20151385,5445530938,1765888446,1234608648,1231403644,8061693044,2718532541,1557155820,3956303039,4675457346,1607780444,688214943,7228194800,1704336795,6473461213,1572565840,4294154830,2681584745,1687503590,2045661650,6587799531,3522571516,6540672398,921502189,1747049010,24450204,4620145090,2278051174,8402305738,1711485310,1704336795,5307414793,2003496891,2390723020,1883427538,1014270616,2023824685,2695248395,514185711,1912442139,4244840273,4822075087,6510675850,1440198447,4132925570,18433692,1200667535,7731656822,1952335906,4086589383,1053863837,1393907482,4730161749,2580921651,4281588671,1069011004,1220339505,1278060440,1227404256,1053863837,13668541,6693105977,1932543255,1982601858,558227287,2389407303,2742180520,1974315892,1488804665,3410716962,2478009032,1668147908,4866653385,4948595587,1597519646,2833568659,3649240300,1326661536,4639271448,4034674098,787531545,3705715644,4789342784,1066916414,1938902163,1601454317,2033295524,2138884440,1522788010,4794132881,1546582468,5200926291,3509747568,3143382126,1644683947,3147541721,5481596863,1599429669,796508433,1477586756,417437054,1480337949,4467036187,3177922300,1483762549,1799617996,3889138834,4315043975,1819147300,2390723020,1198610378,1912442139,1157135600,1474835368,20151385,1154682251,6473461213,2143738880,22142393,6310810172,2045661650,1429844460,507653118,918476365,6587799531,2755457369,3149890943,1803715560,4584616027,5418202224,796508433,3513305283,1974315892,3904381479,1821577515,2881669788,3107064051,1954804317,1334834820,4081868848,7580210958,1066916414,27125227,5354088682,2639320060,5456479323,1974315892,4661912281,2321078582,1597519646,2181903757,1174446236,2344641007,2335370097,2615669058,5588149922,3309395988,4236045334,1668147908,20151385,1390502622,8960705264,2261776813,3212845548,1220339505,696014594,918476365,5481611220,2990383351,1781347790,1237896867,1413304825,1480210311,1421493685,1220339505,14628018,7756899822,2238834717,1261740921,459116384,186720694,2768395256,3177301797,2287254133,20151385,1704336795,3952215960,2871095240,1932368767,1993852422,3283231554,4228693334,1536544835,911628301,4294154830,1593906296,1235468986,1211087713,1668341972,2355618756,2478009032,4084624381,1471136942,1035117617,756341995,4341909919,4067004401,3642342753,1905171194,2533881104,6352614905,1852715886,922033608,1711485310,482644277,1714674424,5176617027,3682378940,1718643789,2084758380,4506764597,3117012234,1593209340,1597519646,1388118149,2215535029,1340043898,1708296093,22142393,1337200148,3904381479,24450204,5842635960,1334834820,1656146242,587215589,1063409135,5722394759,1912442139,3192691276,3649887233,2089507967,6279132895,922033608,2287254133,4524432658,2110211993,3338986616,3600245770,1546018654,3328681899,1235468986,30225892,6204817607,1535286165,6323500830,2287254133,5402501993,2689193978,1850501959,2527873613,1360109050,2705759462,3030659803,6476122835,654459500,4908870960,1932368767,22142393,1610544314,6523124201,3862196085,2620456055,3722859307,1413304825,805549174,1063409135,1488804665,3464998730,507653118,926002770,1636974836,1646466668,1413304825,15740163,4384201410,2593863368,1461294015,530955649,215216284,3207687906,3681659714,1477586756,22142393,1974315892,3326729452,2238632540,2309899416,3804444940,3212845548,1779824817,1055471359,2094556841,1846313786,1430841683,1402580850,20151385,1912442139,2729230164,2871095240,3750169486,983186085,1704009305,1198610378,875475863,5031580616,3272446471,4220698159,2207107257,2935857800,4215149499,3147080104,1111187450,1053863837,13668541,1982601858,558227287,1986298600,4510301925,4267104880,393379744,417437054,3628760890,3611776784,1845505802,1850501959,1607780444,2566856139,1552056612,920861832,1058043309,24450204,1548760337,4524432658,27125227,5787916554,1546018654,814796174,679438062,1231403644,594787629,2215535029,312648079,3386849908,4229443095,2420775757,3262242727,4014812391,1477586756,3649240300,1841335771,603438293,1440485655,2428586187,4171902733,1790806112,2075779507,1430841683,20151385,3328718696,1778366025,3394226133,1477586756,2110953829,3115884016,2143738880,2928894306,1575314586,3135085289,938135983,2573548031,2995088362,4510301925,757381795,3889138834,2238632540,681794169,1183804922,5722394759,1837475649,4475534673,3036208451,1636974836,932512922,1231403644,4015135059,587215589,1072133120,1896235278,1636974836,17029269,4711604673,368996826,3005384285,1692600045,614225993,248246097,3716880959,30225892,1711485310,24450204,2287254133,3854864326,2593629108,565282075,2314037111,804645025,1257170545,298893513,1912442139,2138884440,1053863837,1624544419,22142393,2215535029,3162290737,3326729452,14570353,4331111806,1138415462,1973936392,1388118149,1013566336,5830991928,3791943925,4891081666,2557087485,3401797174,1704336795,3646629163,1286784426,1220339505,1035117617,459116384,2301143709,5226767342,4944872597,454758984,4204955233,4185268417,2137947741,1862395460,1477586756,1797804844,1066174172,1225183966,27125227,997934078,3649240300,30225892,6693105977,1790806112,943231316,786335000,688214943,361181262,3924551264,4901218071,2804754985,4652435303,1711485310,2133114226,698242087,1668480735,2813808237,4834521945,1035117617,2404862743,22142393,2019694296,1837475649,2060124837,3933101105,1711485310,2445634037,3610469112,3393725544,1824763689,3632725562,1086197035,2981836499,1103661044,5226767342,876681106,4506764597,2593629108,789065984,1370956839,594787629,2128639847,1799617996,3518115497,1079679172,507653118,4652809255,679438062,1241515765,1042067055,1154682251,1896235278,18523495,14570353,426496264,3482386530,1264696950,710746332,286531621,262583837,4044513151,20151385,1982601858,27125227,1477586756,3005112849,654014501,2681032056,931464913,1455996425,345238056,2215535029,2478009032,696014594,1185812287,24450204,2566856139,3664260043,3854864326,15673323,5019064232,1318344974,2286814362,1607780444,138512177,3428887115,908237632,4759899181,2962756682,3941876988,1907256217,2318410418,1490322432,1413304825,530955649,2666087078,970587744,525904903,3212845548,2094556841,999336358,1053863837,1711485310,1295125053,787531545,1234608648,1418920080,1155510168,4228693334,13668541,7756899822,1035117617,1092103091,910241408,796508433,919986913,3249833111,3484260765,1982601858,2471320550,808131081,2322190965,2037298475,3565278873,2786309800,24450204,1745065602,2128639847,2386717209,2559888695,2833568659,3275515117,3932520880,2113905206,2788042993,1421507502,1257817605,1469330218,1985761752,1907256217,3628760890,3005112849,913406914,1587888414,688214943,2466134167,2084758380,4076703740,1250262550,587215589,5391950369,786335000,930197497,1206665632,20255477,15673323,493145028,1279832144,1464720410,822625009,330909143,303150795,4686862179,22142393,1261740921,30225892,1711485310,3482072020,756866059,1376083673,1730339682,1078464412,1686459530,398956949,2566856139,2871095240,805549174,1373283590,1477586756,4467036187,16951794,1432282438,845110743,2649477571,1862395460,159336783,3973277407,1051541204,5516080598,3432976091,3127696050,2209523987,2686101329,1636974836,614225993,3089100359,608371577,3722859307,514185711,1912442139,1157135600,1220339505,1982601858,1499990310,1429844460,696014594,947468933,1338159804,14628018,4384201410,1198610378,1264663378,13618793,3765732210,4037462168,2863342357,17029269,2690483406,2360258706,4131371854,3228452821,27125227,2021525582,2466134167,2502693234,2966003537,3283231554,3795500835,4557049504,2449055004,1646482792,1456746491,1701915123,2300521468,2209523987,4204955233,3482072020,1057533002,920861832,796508433,1409993636,1447337035,3753586971,1053863837,394125358,679438062,910241408,1076995299,1397455179,22263048,16951794,570398961,1462112493,1696571650,952305844,382348025,350172776,3991223569,1461294015,20151385,1982601858,4034925092,876083388,1593831094,2004456538,1248854507,461223601,1477586756,3326729452,932512922,1590585369,1711485310,5176617027,18433692,1658972181,978369549,3069847861,183474997,2804673268,1217647275,2242605094,3978016962,3624160800,2559888695,1672100905,1896235278,710746332,3579423655,703960368,4314026638,2215535029,1340043898,1737453787,1656146242,805549174,1097014960,1042219577,15740163,1388118149,1464681501,14570353,4363721337,3084782871,18523495,1469330218,1648048451,2734608480,2880285518,30225892,2341975959,1447337035,2899707290,3436739490,3804444940,4149980761,4360966410,2837533933,1687328999,1971509016,2665365861,2559888695,1659988272,4034925092,1224592464,1066174172,922033608,1633136796,1676422241,4349643614,1220339505,455623221,786335000,1053863837,1247151600,1618603212,24590057,18433692,659945561,1693548775,1102621521,441971871,404676905,4625093146,1692600045,22142393,4675748324,1014270616,1446357115,533398132,1711485310,3854864326,1079679172,1046414303,1982601858,1488804665,4510301925,20151385,1104361713,817371143,1132832529,3557107599,201980269,9473815,3249738451,1410184186,2598233688,4609784909,2966003537,1936950825,1042067055,822625009,4147767355,801090727,13668541,4999260724,2566856139,1552056612,2012702520,814796174,932512922,1270356781,1206842379,17029269,654459500,15673323,5056862680,3574419216,20255477,1701915123,1909071106,3168524916,3337382170,2713416501,1676422241,1919695918,1668341972,4809111807,5053669526,3287827738,1954601862,2284000779,3088264423,2966003537,4675748324,814796174,1234608648,1053863837,13668541,1891786557,1941959541,890564228,526906636,910241408,1220339505,514185711,1874940380,13618793,20151385,763740839,1961811255,355993628,324362380,467853742,1160201076,1264696950,24450204,1174446236,860490212,4467036187,1250262550,1211704558,5226767342,22142393,1278872558,946216096,393397333,1451592382,2670307870,232903938,9765838,2131576758,381966627,1251390990,3010450010,4371492224,3436739490,2243943763,952305844,4806546091,927345075,14628018,4199623201,1477586756,1797804844,910241408,943231316,1079679172,541083292,1397660001,18523495,757381795,16951794,3127696050,22263048,2211627781,3671486281,2427013754,1668758062,1475202713,2223943239,1912442139,1440198447,4132925570,1706615038,2320967753,2264403260,2646216335,3315870915,3436739490,943231316,1429844460,1220339505,2191592738,1214631583,1031055586,592503412,1053863837,1413304825,594787629,2158397445,14570353,22142393,884052049,1273423368,411423943,374759557,541083292,1343597281,1464720410,27125227,1360109050,996196197,5176617027,1403295836,1130978830,1095562903,454779383,507653118,1173701572,3093992768,268748183,10104328,2469538590,441529845,1449297189,3488258314,5065870192,1668341972,2599785533,1073689048,15740163,4866653385,1711485310,1295125053,1053863837,1250262550,625965142,507653118,1111187450,20255477,876681106,18433692,3624160800,24590057,2562327381,2811985636,1933075911,1708722052,2576602506,2215535029,1668147908,4789342784,1976956741,2689065477,2623500343,3066067747,3842278117,1668341972,1092103091,2539104159,1406688623,1193901962,685567279,1220339505,1636974836,688214943,2500626858,15673323,24450204,1023507210,1474835368,475674337,433175943,625965142,1556175558,1696571650,30225892,1575314586,1153495751,4510301925,1309725010,1268673826,525928561,587215589,1359245820,312648079,3272446471,310295966,10496677,1391946807,510570782,1678694268,4042095615,1720757056,4149980761,1912442139,3012248977,1243319315,4199623201,1499990310,1053863837,724353410,587215589,1286784426,22263048,20151385,4199623201,13618793,9004527,2959825900,2239452090,965128452,2985377044,2566856139,1932368767,3956303039,2290315298,1208478809,3039737053,3552726052,3012248977,20151385,1912442139,1264663378,606541592,1629305822,793439494,1896235278,796508433,2897311912,16951794,27125227,1185152512,348167994,500887559,724353410,1802579367,1035117617,1824763689,539774893,5226767342,1516913321,608399015,679438062,1574313910,361181262,3791943925,358454834,10951455,1612218467,590597535,886549753,1802389878,1993349015,4809111807,2215535029,3490343756,18433692,1737453787,1220339505,838397239,679438062,1490322432,24590057,22142393,4866653385,14570353,9221879,3429579079,2594578933,1117484640,3459195935,1477586756,2238632540,2653535565,1399556955,1201237711,4116821582,3490343756,22142393,2215535029,1464681501,701839175,1191331328,1042067055,922033608,3357117602,30225892,1372518854,402353128,579373461,838397239,2088191041,1198610378,2113905206,624448582,1570348788,703992189,786335000,514185711,1309417975,417437054,2913766048,20151385,11478596,1867539834,683358171,1026402341,1573785471,2309315886,2566856139,4044513151,2012702520,970587744,786335000,796049955,4199623201,15673323,9473815,2533881104,3006213657,1294083804,4008409058,1711485310,2593629108,3074551550,1239854892,381184630,1371012095,4770676170,4044513151,24450204,2566856139,812300527,1379680824,1206665632,20151385,1589698976,465160213,670348057,2419249347,1388118149,2449055004,722595569,514185711,1304821925,910241408,594787629,1516557455,482644277,3376190139,22142393,12089615,2163488027,790878909,1188508308,1822991199,2675559497,4686862179,910241408,20151385,910241408,921502189,16951794,9765838,2935857800,1279832144,2203515669,1498783494,3484812092,3005112849,1248522612,1435925605,440623444,1587952461,4557984562,4686862179,27125227,1477586756,1598000535,1397455179,22142393,737775808,537961176,775798551,2802985768,1607780444,2837533933,328706614,1511230086,1053863837,688214943,1756657018,558227287,2389407303,12797857,2243943763,915508382,1376408615,2111850606,3100079897,3991223569,1053863837,1066916414,18433692,10104328,1462112493,2552924384,1736055077,4038101245,3482072020,1445972424,1663195156,509520185,1839412432,5282037258,30225892,1711485310,920861832,1618603212,853955457,622346244,11478596,3247782465,379795065,1750481962,1220339505,796508433,1035117617,999843662,459116384,13618793,2599785533,1059968935,1594207664,1447337035,1278112991,4625093146,1220339505,1235468986,10496677,1693548775,2645283044,2011081404,479806762,1674840498,1926627914,589379804,1334834820,1971320703,1066174172,1874940380,988621642,720158683,12089615,3763355368,439012726,1231753699,1413304825,922033608,1198610378,1157723578,530955649,14570353,1227416097,743001905,1676422241,1460119793,1430841683,10951455,1961811255,3064985978,2329870022,554938320,1940126117,2231978180,681946717,1546018654,2283782438,1234608648,1144715945,833535060,12797857,1426535226,1636974836,1388118149,1340725380,614225993,15673323,860013116,1941959541,1691239003,11478596,2613336200,2699384404,642024834,1248287690,2585915881,789242913,1790806112,2645963178,1429844460,1325648013,964951909,13618793,1652310435,1896235278,1607780444,856831875,710746332,16951794,995643178,1214631583,1959133959,12089615,3027955776,3127696050,742968580,1445700102,2996172265,913612122,3065774224,1656146242,493302983,14570353,878893433,1042067055,1154682251,991955713,822625009,1152854728,1406688623,1270320068,12797857,1985761752,3624160800,859974524,1674524822,3471708776,1057771008,3552385725,814796174,570582029,15673323,1017527727,1206665632,1337200148,1148580485,952305844,1335081815,1629305822,1471238281,13618793,2300521468,4199623201,995598488,1053210433,4022912809,1224868511,943231316,660157734,16951794,1178221542,399929925,504237864,1191331328,1704126647,14570353,2665365861,4866653385,1152802975,1219582097,1418554632,1092103091,763986745,18433692,462351423,583256837,1379680824,15673323,3088264423,4199623201,1335021884,1412426858,1643060161,1264663378,884337051,20151385,534705442,674849320,1598000535,16951794,3315870915,4866653385,1546235517,939942527,1903289095,1464681501,1023837523,22142393,618572448,920861832,18433692,4199623201,369550019,1421507502,1088290974,2204925752,507653118,677882222,715784390,1066174172,4866653385,427137454,1646482792,1260244660,2554558946,587215589,784531536,1234608648,493888214,1907256217,541083292,2959825900,679438062,908150909,1429844460,571260369,2209523987,625965142,3429579079,786335000,1037821828,660943995,2559888695,724353410,2533881104,910241408,1201744840,764898098,2966003537,838397239,1053863837,1391751317,885393396,3436739490,970587744,1220339505,681794169,2314037111,1413304825,789065984,2681032056,1636974836,913406914,1376083673,1057533002,1593831094,1224592464,330909143]
def R16 : Nat := 1159107281
def C16 : Nat := 10310

theorem check16 : check 16 succ16 = true := by decide +kernel
theorem wcheck16 : wcheck 1000000000 R16 succ16 weights16 = true := by decide +kernel
theorem wmin16 : weights16.all (fun v => Nat.ble 9004527 v) = true := by decide +kernel
theorem len16 : succ16.length = 2260 ∧ weights16.length = 2260 := by decide +kernel
theorem w0_16 : weights16.getD 0 0 ≤ C16 * 9004527 := by decide +kernel

/-- The width-16 certificate. -/
def cert16 : Cert := ⟨16, succ16, weights16, 1000000000, R16, C16, 9004527⟩

theorem cert16_valid : cert16.Valid where
  hM := by decide
  hcheck := check16
  hw := wcheck16
  hN := by rw [show cert16.succ.length = 2260 from len16.1]; decide
  hlen := by show succ16.length ≤ weights16.length; rw [len16.1, len16.2]
  hmin := wmin16
  hmin0 := by decide
  hC := w0_16

/-- **The channel bound at width 16.** -/
theorem channel_bound_16 (n : Nat) :
    ∃ S : Finset (List Bool), (∀ x : Int → Bool, Clock x → visFrom x 0 n ∈ S) ∧
      S.card * 1000000000 ^ n ≤ 10310 * 1159107281 ^ n :=
  cert16.bound cert16_valid n

theorem channel_bound_16_eventually (n : Nat) :
    ∃ S : Finset (List Bool),
      (∀ (x : Int → Bool) (T : Nat), T % 2 = 0 → (∀ t, T ≤ t → evol x t 0 = decide (t % 2 = 1)) →
        visFrom (fun q => evol x T q) 0 n ∈ S) ∧
      S.card * 1000000000 ^ n ≤ 10310 * 1159107281 ^ n :=
  cert16.bound_eventually cert16_valid n

theorem channel_ncard_16 (n : Nat) :
    Set.ncard {w : List Bool | ∃ x : Int → Bool, Clock x ∧ visFrom x 0 n = w} * 1000000000 ^ n
      ≤ 10310 * 1159107281 ^ n :=
  cert16.ncard_bound cert16_valid n

end Rule30Submission
