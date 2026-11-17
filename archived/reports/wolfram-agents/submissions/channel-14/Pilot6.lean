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

/-! ## 7. Explicit certificates: one closure theorem per state -/

/-- A complete binary tree of bitsets, indexed by the bits of the state number. -/
inductive BTree where
  | leaf : Nat → BTree
  | node : BTree → BTree → BTree

/-- Lookup by the bits of `i`, low bit first. -/
def look : BTree → Nat → Nat
  | BTree.leaf w, _ => w
  | BTree.node l r, i => cond (Nat.beq (Nat.land i 1) 0) (look l (Nat.shiftRight i 1)) (look r (Nat.shiftRight i 1))

/-- The bitset of state `i`: the tree's leaf for `i < N`, empty past the end (so a dead edge has no members). -/
def bset (T : BTree) (N i : Nat) : Nat := cond (Nat.blt i N) (look T i) 0

/-- The four two-step images of `s` are in `tgt`. -/
def imgs4In (mask top s tgt : Nat) : Bool :=
  let s0 := nxtT mask s 0 0
  let s1 := nxtT mask s 0 top
  Nat.beq (Nat.land (Nat.shiftRight tgt (nxtT mask s0 1 0)) 1) 1 &&
  Nat.beq (Nat.land (Nat.shiftRight tgt (nxtT mask s0 1 top)) 1) 1 &&
  Nat.beq (Nat.land (Nat.shiftRight tgt (nxtT mask s1 1 0)) 1) 1 &&
  Nat.beq (Nat.land (Nat.shiftRight tgt (nxtT mask s1 1 top)) 1) 1

/-- The members of the word `w` at `base`, highest first: each must have its images in the target of its label. -/
noncomputable def wordOK (mask top T0 T1 : Nat) (fuel : Nat) : Nat → Nat → Bool :=
  Nat.rec (motive := fun _ => Nat → Nat → Bool) (fun _ _ => true)
    (fun _ ih w base =>
      cond (Nat.beq w 0) true
        (force (pos64 w) fun p => force (Nat.add base p) fun s =>
          force (Nat.xor w (Nat.shiftLeft 1 p)) fun w' =>
            cond (imgs4In mask top s (cond (Nat.beq (Nat.land s 1) 0) T0 T1)) (ih w' base) false))
    fuel

/-- Sweep the words `nwords - 1, …, 0` of the source bitset. -/
noncomputable def stateCheck (mask top T0 T1 : Nat) (nwords : Nat) : Nat → Bool :=
  Nat.rec (motive := fun _ => Nat → Bool) (fun _ => true)
    (fun k ih B =>
      force (Nat.land (Nat.shiftRight B (Nat.mul 64 k)) 18446744073709551615) fun w =>
        cond (Nat.beq w 0) (ih B) (cond (wordOK mask top T0 T1 64 w (Nat.mul 64 k)) (ih B) false))
    nwords

theorem imgs4In_spec (M mask top s tgt : Nat) (htop : top = Nat.shiftLeft 1 (Nat.sub M 1))
    (h : imgs4In mask top s tgt = true) (u v : Nat) (hu : u ≤ 1) (hv : v ≤ 1) :
    tgt.testBit (step2 M mask s u v) = true := by
  unfold imgs4In at h
  simp only [Bool.and_eq_true] at h
  obtain ⟨⟨⟨h00, h01⟩, h10⟩, h11⟩ := h
  have key : ∀ t, Nat.beq (Nat.land (Nat.shiftRight tgt t) 1) 1 = true → tgt.testBit t = true := by
    intro t ht
    have h1 := Nat.eq_of_beq_eq_true ht
    rw [land_eq', shiftRight_eq', Nat.and_one_is_mod, Nat.shiftRight_eq_div_pow] at h1
    rw [Nat.testBit_eq_decide_div_mod_eq, h1]; rfl
  unfold step2
  rw [← nxtT_eq M mask s 0 u, ← nxtT_eq M mask _ 1 v]
  have h0 : Nat.shiftLeft 0 (Nat.sub M 1) = 0 := by simp [shiftLeft_eq']
  rcases Nat.le_one_iff_eq_zero_or_eq_one.mp hu with rfl | rfl <;>
  rcases Nat.le_one_iff_eq_zero_or_eq_one.mp hv with rfl | rfl <;>
  simp only [h0, ← htop] <;> first | exact key _ h00 | exact key _ h01 | exact key _ h10 | exact key _ h11

theorem wordOK_succ (mask top T0 T1 fuel w base : Nat) :
    wordOK mask top T0 T1 (fuel + 1) w base =
      cond (Nat.beq w 0) true
        (force (pos64 w) fun p => force (Nat.add base p) fun s =>
          force (Nat.xor w (Nat.shiftLeft 1 p)) fun w' =>
            cond (imgs4In mask top s (cond (Nat.beq (Nat.land s 1) 0) T0 T1)) (wordOK mask top T0 T1 fuel w' base) false) := rfl

/-- Every member of the word has its four images in the target of its label. -/
theorem wordOK_spec (M mask top T0 T1 : Nat) (htop : top = Nat.shiftLeft 1 (Nat.sub M 1)) :
    ∀ (fuel w base : Nat), w < 2 ^ fuel → w < 2 ^ 64 → wordOK mask top T0 T1 fuel w base = true →
    ∀ j, w.testBit j = true → ∀ u v, u ≤ 1 → v ≤ 1 →
      (if (base + j) % 2 = 0 then T0 else T1).testBit (step2 M mask (base + j) u v) = true := by
  intro fuel
  induction fuel with
  | zero =>
    intro w base hw _ _ j hj
    have : w = 0 := by simpa using hw
    subst this; simp at hj
  | succ n ih =>
    intro w base hw h64 hok j hj u v hu hv
    rw [wordOK_succ] at hok
    by_cases hw0 : w = 0
    · subst hw0; simp at hj
    have hbeq : Nat.beq w 0 = false := beq_zero_false hw0
    rw [hbeq] at hok; simp only [cond_false, force_eq, xor_eq', shiftLeft_eq', add_eq', land_eq'] at hok
    have hpos : 0 < w := Nat.pos_of_ne_zero hw0
    have hp := pos64_spec w hpos h64
    have hpl : pos64 w ≤ n := by
      have : 2 ^ pos64 w < 2 ^ (n + 1) := lt_of_le_of_lt hp.1 hw
      exact Nat.lt_succ_iff.mp ((Nat.pow_lt_pow_iff_right (by norm_num)).mp this)
    have hp64 : pos64 w < 64 := by
      have := lt_of_le_of_lt hp.1 h64
      exact (Nat.pow_lt_pow_iff_right (by norm_num)).mp this
    have hw' : w ^^^ (1 <<< pos64 w) < 2 ^ n :=
      lt_of_lt_of_le (pos64_clear w hpos h64) (Nat.pow_le_pow_right (by norm_num) hpl)
    have hw'64 : w ^^^ (1 <<< pos64 w) < 2 ^ 64 := Nat.xor_lt_two_pow h64 (by
      rw [Nat.shiftLeft_eq, Nat.one_mul]; exact Nat.pow_lt_pow_right (by norm_num) hp64)
    cases hm : imgs4In mask top (base + pos64 w) (cond (Nat.beq ((base + pos64 w) &&& 1) 0) T0 T1) with
    | false => rw [hm] at hok; simp at hok
    | true =>
    rw [hm, cond_true] at hok
    by_cases hjp : j = pos64 w
    · subst hjp
      have hsel : (cond (Nat.beq ((base + pos64 w) &&& 1) 0) T0 T1) = (if (base + pos64 w) % 2 = 0 then T0 else T1) := by
        rw [Nat.and_one_is_mod]
        by_cases he : (base + pos64 w) % 2 = 0
        · rw [he]; simp
        · have : Nat.beq ((base + pos64 w) % 2) 0 = false := beq_zero_false he
          rw [this]; simp [he]
      rw [hsel] at hm
      exact imgs4In_spec M mask top _ _ htop hm u v hu hv
    · exact ih _ base hw' hw'64 hok j (by rw [testBit_clear_of_ne w (pos64 w) j hjp]; exact hj) u v hu hv

theorem stateCheck_succ (mask top T0 T1 k B : Nat) :
    stateCheck mask top T0 T1 (k + 1) B =
      force (Nat.land (Nat.shiftRight B (Nat.mul 64 k)) 18446744073709551615) fun w =>
        cond (Nat.beq w 0) (stateCheck mask top T0 T1 k B)
          (cond (wordOK mask top T0 T1 64 w (Nat.mul 64 k)) (stateCheck mask top T0 T1 k B) false) := rfl

/-- Every member `s < 64 n` of the source has its four images in the target of its label. -/
theorem stateCheck_spec (M mask top T0 T1 : Nat) (htop : top = Nat.shiftLeft 1 (Nat.sub M 1)) :
    ∀ (n B : Nat), stateCheck mask top T0 T1 n B = true →
    ∀ s, s < 64 * n → B.testBit s = true → ∀ u v, u ≤ 1 → v ≤ 1 →
      (if s % 2 = 0 then T0 else T1).testBit (step2 M mask s u v) = true := by
  intro n
  induction n with
  | zero => intro B _ s hs; omega
  | succ k ih =>
    intro B hok s hs hB u v hu hv
    rw [stateCheck_succ, force_eq] at hok
    simp only [land_eq', shiftRight_eq', mul_eq'] at hok
    set w := (B >>> (64 * k)) &&& 18446744073709551615 with hw
    by_cases hsk : s < 64 * k
    · -- handled by the lower words, whichever branch was taken
      by_cases hw0 : w = 0
      · rw [hw0, show Nat.beq 0 0 = true from rfl, cond_true] at hok
        exact ih B hok s hsk hB u v hu hv
      · rw [beq_zero_false hw0, cond_false] at hok
        cases hwo : wordOK mask top T0 T1 64 w (64 * k) with
        | false => rw [hwo] at hok; simp at hok
        | true => rw [hwo, cond_true] at hok; exact ih B hok s hsk hB u v hu hv
    · have hj : w.testBit (s - 64 * k) = true := by
        rw [hw, word_testBit]
        have : 64 * k + (s - 64 * k) = s := by omega
        rw [this, hB]; simp; omega
      have hw0 : w ≠ 0 := by intro h0; rw [h0] at hj; simp at hj
      rw [beq_zero_false hw0, cond_false] at hok
      cases hwo : wordOK mask top T0 T1 64 w (64 * k) with
      | false => rw [hwo] at hok; simp at hok
      | true =>
        have := wordOK_spec M mask top T0 T1 htop 64 w (64 * k) (hw ▸ word_lt B k) (hw ▸ word_lt B k) hwo
          (s - 64 * k) hj u v hu hv
        have e : 64 * k + (s - 64 * k) = s := by omega
        rw [e] at this; exact this

/-- The per-state obligation, with the successors looked up in the graph. -/
abbrev StateOK (M mask top : Nat) (T : BTree) (N : Nat) (succ : List (Nat × Nat)) (i : Nat) : Prop :=
  stateCheck mask top (bset T N (succAt succ i 0)) (bset T N (succAt succ i 1)) (Nat.shiftRight (Nat.shiftLeft 1 M) 6)
    (bset T N i) = true

theorem bset_zero_of_ge (T : BTree) (N i : Nat) (h : N ≤ i) : bset T N i = 0 := by
  unfold bset
  have : Nat.blt i N = false := by
    cases hb : Nat.blt i N
    · rfl
    · exact absurd (Nat.le_of_ble_eq_true hb) (by omega)
  rw [this]; rfl

/-- All per-state checks give the closure of every edge, with `bset T N` as the family of bitsets. -/
theorem explicit_sound (M : Nat) (hM : 6 ≤ M) (T : BTree) (succ : List (Nat × Nat))
    (hall : ∀ i, i < succ.length → StateOK M (2 ^ M - 1) (Nat.shiftLeft 1 (Nat.sub M 1)) T succ.length succ i) :
    ∀ i, i < succ.length → ∀ b, b ≤ 1 →
      EdgeOK M (2 ^ M - 1) (bset T succ.length) succ.length i (succAt succ i b) b := by
  intro i hi b hb s hs hmem hsb
  have hok := hall i hi
  unfold StateOK at hok
  have hcov : s < 64 * (Nat.shiftRight (Nat.shiftLeft 1 M) 6) := by
    rw [shiftRight_eq', shiftLeft_eq', Nat.shiftRight_eq_div_pow, Nat.shiftLeft_eq, Nat.one_mul]
    have : 2 ^ M = 64 * (2 ^ M / 2 ^ 6) := by
      rw [show (64 : Nat) = 2 ^ 6 by norm_num, Nat.mul_div_cancel' (Nat.pow_dvd_pow 2 hM)]
    omega
  have hspec := stateCheck_spec M (2 ^ M - 1) _ _ _ rfl _ _ hok s hcov hmem
  -- the target of label b
  have htgt : ∀ u v, u ≤ 1 → v ≤ 1 →
      (bset T succ.length (succAt succ i b)).testBit (step2 M (2 ^ M - 1) s u v) = true := by
    intro u v hu hv
    have := hspec u v hu hv
    rcases Nat.le_one_iff_eq_zero_or_eq_one.mp hb with rfl | rfl
    · rw [hsb] at this; simpa using this
    · rw [hsb] at this; simpa using this
  refine ⟨?_, htgt⟩
  by_contra hge
  have := htgt 0 0 (Nat.zero_le _) (Nat.zero_le _)
  rw [bset_zero_of_ge T _ _ (Nat.le_of_not_lt hge)] at this
  simp at this

/-- The bound from any family of bitsets with the root full and every edge closed. -/
theorem bound_of (M : Nat) (hM : 6 ≤ M) (succ : List (Nat × Nat)) (hN : 0 < succ.length)
    (Bset : Nat → Nat) (hB0 : Bset 0 = 2 ^ (2 ^ M) - 1)
    (hE : ∀ i, i < succ.length → ∀ b, b ≤ 1 → EdgeOK M (2 ^ M - 1) Bset succ.length i (succAt succ i b) b)
    (w : List Nat) (D R C wmin : Nat) (hw : wcheck D R succ w = true) (hlen : succ.length ≤ w.length)
    (hmin : w.all (fun v => Nat.ble wmin v) = true) (hmin0 : 0 < wmin) (hC : w.getD 0 0 ≤ C * wmin) (n : Nat) :
    ∃ S : Finset (List Bool), (∀ x : Int → Bool, Clock x → visFrom x 0 n ∈ S) ∧ S.card * D ^ n ≤ C * R ^ n := by
  refine ⟨AccF succ n 0, fun x hx => visFrom_mem M hM succ hN Bset hB0 hE x hx n 0, ?_⟩
  have hmin' : ∀ i, i < succ.length → wmin ≤ w.getD i 0 := by
    intro i hi
    have hl : i < w.length := lt_of_lt_of_le hi hlen
    have hmem : w.getD i 0 ∈ w := by rw [List.getD_eq_getElem _ _ hl]; exact List.getElem_mem hl
    exact Nat.le_of_ble_eq_true (List.all_eq_true.mp hmin _ hmem)
  have hwb := weight_bound D R succ w hw wmin hmin' n 0
  have hcard := card_AccF_le succ n 0
  have h1 : D ^ n * wmin * (AccF succ n 0).card ≤ R ^ n * (C * wmin) :=
    le_trans (Nat.mul_le_mul_left _ hcard) (le_trans hwb (Nat.mul_le_mul_left _ hC))
  have h2 : wmin * ((AccF succ n 0).card * D ^ n) ≤ wmin * (C * R ^ n) := by
    calc wmin * ((AccF succ n 0).card * D ^ n) = D ^ n * wmin * (AccF succ n 0).card := by ring
      _ ≤ R ^ n * (C * wmin) := h1
      _ = wmin * (C * R ^ n) := by ring
  exact Nat.le_of_mul_le_mul_left h2 hmin0

/-- Combining per-state facts over a range. -/
theorem range_split {P : Nat → Prop} (lo mid hi : Nat) (h1 : ∀ i, lo ≤ i → i < mid → P i)
    (h2 : ∀ i, mid ≤ i → i < hi → P i) : ∀ i, lo ≤ i → i < hi → P i := by
  intro i hlo hhi
  by_cases h : i < mid
  · exact h1 i hlo h
  · exact h2 i (Nat.le_of_not_lt h) hhi

theorem range_one {P : Nat → Prop} (i : Nat) (h : P i) : ∀ k, i ≤ k → k < i + 1 → P k := by
  intro k h1 h2
  have : k = i := by omega
  subst this; exact h

/-! ## 8. Width 6: the data -/

def T6 : BTree := (BTree.node (BTree.node (BTree.node (BTree.node (BTree.node (BTree.leaf 18446744073709551615) (BTree.leaf 1224980198441615360)) (BTree.node (BTree.leaf 5769464140251873552) (BTree.leaf 1103806595329))) (BTree.node (BTree.node (BTree.leaf 6057694516470694160) (BTree.leaf 72622206194090371)) (BTree.node (BTree.leaf 1446821598668792980) (BTree.leaf 1229483866788462608)))) (BTree.node (BTree.node (BTree.node (BTree.leaf 6058838025743454485) (BTree.leaf 1157706583507009536)) (BTree.node (BTree.leaf 397448735929730309) (BTree.leaf 563508332724354))) (BTree.node (BTree.node (BTree.leaf 108686187593539971) (BTree.leaf 72058693566333184)) (BTree.node (BTree.leaf 1158590655581398032) (BTree.leaf 72058697861366017))))) (BTree.node (BTree.node (BTree.node (BTree.node (BTree.leaf 1555472052100867479) (BTree.leaf 289361795091793157)) (BTree.node (BTree.leaf 36627489732173954) (BTree.leaf 36029346783166592))) (BTree.node (BTree.node (BTree.leaf 1519443255073514903) (BTree.leaf 1165482359268352)) (BTree.node (BTree.leaf 288230376218836992) (BTree.leaf 325390038068364292)))) (BTree.node (BTree.node (BTree.node (BTree.leaf 398046878878737799) (BTree.leaf 324264120981390336)) (BTree.node (BTree.leaf 5769462971752333312) (BTree.leaf 4899986764464144384))) (BTree.node (BTree.node (BTree.leaf 1518880292235125908) (BTree.leaf 4616542635643978000)) (BTree.node (BTree.leaf 361419389146563845) (BTree.leaf 0))))))
def succ6 : List (Nat × Nat) := [(1,2),(3,4),(5,1000000),(6,4),(7,1000000),(3,8),(9,4),(10,11),(12,1000000),(1000000,4),(6,13),(14,1000000),(15,11),(16,1000000),(17,18),(6,1000000),(19,1000000),(20,1000000),(21,1000000),(22,13),(9,23),(24,18),(25,1000000),(12,1000000),(26,1000000),(1000000,27),(1000000,23),(28,1000000),(29,1000000),(30,13),(9,1000000)]
def weights6 : List Nat := [14963792517,11773773185,8550123853,10018922660,5971984710,11612238347,7635316700,8110362925,5752572666,4397674932,6027055633,4987857234,7812336534,549848752,6773626837,5622247729,745498803,5503323064,3695906970,1011249412,7473781862,5018776312,822368548,5752572666,3119717104,1115661320,4236140094,1514039632,2055155179,2790150095,3238641768]
def N6 : Nat := 31
/-- The per-state check for width 6. -/
abbrev SOK6 (i : Nat) : Prop := StateOK 6 63 32 T6 31 succ6 i
theorem s6_0 : SOK6 0 := by decide +kernel
theorem s6_1 : SOK6 1 := by decide +kernel
theorem s6_2 : SOK6 2 := by decide +kernel
theorem s6_3 : SOK6 3 := by decide +kernel
theorem s6_4 : SOK6 4 := by decide +kernel
theorem s6_5 : SOK6 5 := by decide +kernel
theorem s6_6 : SOK6 6 := by decide +kernel
theorem s6_7 : SOK6 7 := by decide +kernel
theorem s6_8 : SOK6 8 := by decide +kernel
theorem s6_9 : SOK6 9 := by decide +kernel
theorem s6_10 : SOK6 10 := by decide +kernel
theorem s6_11 : SOK6 11 := by decide +kernel
theorem s6_12 : SOK6 12 := by decide +kernel
theorem s6_13 : SOK6 13 := by decide +kernel
theorem s6_14 : SOK6 14 := by decide +kernel
theorem s6_15 : SOK6 15 := by decide +kernel
theorem s6_16 : SOK6 16 := by decide +kernel
theorem s6_17 : SOK6 17 := by decide +kernel
theorem s6_18 : SOK6 18 := by decide +kernel
theorem s6_19 : SOK6 19 := by decide +kernel
theorem s6_20 : SOK6 20 := by decide +kernel
theorem s6_21 : SOK6 21 := by decide +kernel
theorem s6_22 : SOK6 22 := by decide +kernel
theorem s6_23 : SOK6 23 := by decide +kernel
theorem s6_24 : SOK6 24 := by decide +kernel
theorem s6_25 : SOK6 25 := by decide +kernel
theorem s6_26 : SOK6 26 := by decide +kernel
theorem s6_27 : SOK6 27 := by decide +kernel
theorem s6_28 : SOK6 28 := by decide +kernel
theorem s6_29 : SOK6 29 := by decide +kernel
theorem s6_30 : SOK6 30 := by decide +kernel
theorem r6_0_1 : ∀ k, 0 ≤ k → k < 1 → SOK6 k := range_one 0 s6_0
theorem r6_1_2 : ∀ k, 1 ≤ k → k < 2 → SOK6 k := range_one 1 s6_1
theorem r6_2_3 : ∀ k, 2 ≤ k → k < 3 → SOK6 k := range_one 2 s6_2
theorem r6_1_3 : ∀ k, 1 ≤ k → k < 3 → SOK6 k := range_split 1 2 3 r6_1_2 r6_2_3
theorem r6_0_3 : ∀ k, 0 ≤ k → k < 3 → SOK6 k := range_split 0 1 3 r6_0_1 r6_1_3
theorem r6_3_4 : ∀ k, 3 ≤ k → k < 4 → SOK6 k := range_one 3 s6_3
theorem r6_4_5 : ∀ k, 4 ≤ k → k < 5 → SOK6 k := range_one 4 s6_4
theorem r6_3_5 : ∀ k, 3 ≤ k → k < 5 → SOK6 k := range_split 3 4 5 r6_3_4 r6_4_5
theorem r6_5_6 : ∀ k, 5 ≤ k → k < 6 → SOK6 k := range_one 5 s6_5
theorem r6_6_7 : ∀ k, 6 ≤ k → k < 7 → SOK6 k := range_one 6 s6_6
theorem r6_5_7 : ∀ k, 5 ≤ k → k < 7 → SOK6 k := range_split 5 6 7 r6_5_6 r6_6_7
theorem r6_3_7 : ∀ k, 3 ≤ k → k < 7 → SOK6 k := range_split 3 5 7 r6_3_5 r6_5_7
theorem r6_0_7 : ∀ k, 0 ≤ k → k < 7 → SOK6 k := range_split 0 3 7 r6_0_3 r6_3_7
theorem r6_7_8 : ∀ k, 7 ≤ k → k < 8 → SOK6 k := range_one 7 s6_7
theorem r6_8_9 : ∀ k, 8 ≤ k → k < 9 → SOK6 k := range_one 8 s6_8
theorem r6_7_9 : ∀ k, 7 ≤ k → k < 9 → SOK6 k := range_split 7 8 9 r6_7_8 r6_8_9
theorem r6_9_10 : ∀ k, 9 ≤ k → k < 10 → SOK6 k := range_one 9 s6_9
theorem r6_10_11 : ∀ k, 10 ≤ k → k < 11 → SOK6 k := range_one 10 s6_10
theorem r6_9_11 : ∀ k, 9 ≤ k → k < 11 → SOK6 k := range_split 9 10 11 r6_9_10 r6_10_11
theorem r6_7_11 : ∀ k, 7 ≤ k → k < 11 → SOK6 k := range_split 7 9 11 r6_7_9 r6_9_11
theorem r6_11_12 : ∀ k, 11 ≤ k → k < 12 → SOK6 k := range_one 11 s6_11
theorem r6_12_13 : ∀ k, 12 ≤ k → k < 13 → SOK6 k := range_one 12 s6_12
theorem r6_11_13 : ∀ k, 11 ≤ k → k < 13 → SOK6 k := range_split 11 12 13 r6_11_12 r6_12_13
theorem r6_13_14 : ∀ k, 13 ≤ k → k < 14 → SOK6 k := range_one 13 s6_13
theorem r6_14_15 : ∀ k, 14 ≤ k → k < 15 → SOK6 k := range_one 14 s6_14
theorem r6_13_15 : ∀ k, 13 ≤ k → k < 15 → SOK6 k := range_split 13 14 15 r6_13_14 r6_14_15
theorem r6_11_15 : ∀ k, 11 ≤ k → k < 15 → SOK6 k := range_split 11 13 15 r6_11_13 r6_13_15
theorem r6_7_15 : ∀ k, 7 ≤ k → k < 15 → SOK6 k := range_split 7 11 15 r6_7_11 r6_11_15
theorem r6_0_15 : ∀ k, 0 ≤ k → k < 15 → SOK6 k := range_split 0 7 15 r6_0_7 r6_7_15
theorem r6_15_16 : ∀ k, 15 ≤ k → k < 16 → SOK6 k := range_one 15 s6_15
theorem r6_16_17 : ∀ k, 16 ≤ k → k < 17 → SOK6 k := range_one 16 s6_16
theorem r6_15_17 : ∀ k, 15 ≤ k → k < 17 → SOK6 k := range_split 15 16 17 r6_15_16 r6_16_17
theorem r6_17_18 : ∀ k, 17 ≤ k → k < 18 → SOK6 k := range_one 17 s6_17
theorem r6_18_19 : ∀ k, 18 ≤ k → k < 19 → SOK6 k := range_one 18 s6_18
theorem r6_17_19 : ∀ k, 17 ≤ k → k < 19 → SOK6 k := range_split 17 18 19 r6_17_18 r6_18_19
theorem r6_15_19 : ∀ k, 15 ≤ k → k < 19 → SOK6 k := range_split 15 17 19 r6_15_17 r6_17_19
theorem r6_19_20 : ∀ k, 19 ≤ k → k < 20 → SOK6 k := range_one 19 s6_19
theorem r6_20_21 : ∀ k, 20 ≤ k → k < 21 → SOK6 k := range_one 20 s6_20
theorem r6_19_21 : ∀ k, 19 ≤ k → k < 21 → SOK6 k := range_split 19 20 21 r6_19_20 r6_20_21
theorem r6_21_22 : ∀ k, 21 ≤ k → k < 22 → SOK6 k := range_one 21 s6_21
theorem r6_22_23 : ∀ k, 22 ≤ k → k < 23 → SOK6 k := range_one 22 s6_22
theorem r6_21_23 : ∀ k, 21 ≤ k → k < 23 → SOK6 k := range_split 21 22 23 r6_21_22 r6_22_23
theorem r6_19_23 : ∀ k, 19 ≤ k → k < 23 → SOK6 k := range_split 19 21 23 r6_19_21 r6_21_23
theorem r6_15_23 : ∀ k, 15 ≤ k → k < 23 → SOK6 k := range_split 15 19 23 r6_15_19 r6_19_23
theorem r6_23_24 : ∀ k, 23 ≤ k → k < 24 → SOK6 k := range_one 23 s6_23
theorem r6_24_25 : ∀ k, 24 ≤ k → k < 25 → SOK6 k := range_one 24 s6_24
theorem r6_23_25 : ∀ k, 23 ≤ k → k < 25 → SOK6 k := range_split 23 24 25 r6_23_24 r6_24_25
theorem r6_25_26 : ∀ k, 25 ≤ k → k < 26 → SOK6 k := range_one 25 s6_25
theorem r6_26_27 : ∀ k, 26 ≤ k → k < 27 → SOK6 k := range_one 26 s6_26
theorem r6_25_27 : ∀ k, 25 ≤ k → k < 27 → SOK6 k := range_split 25 26 27 r6_25_26 r6_26_27
theorem r6_23_27 : ∀ k, 23 ≤ k → k < 27 → SOK6 k := range_split 23 25 27 r6_23_25 r6_25_27
theorem r6_27_28 : ∀ k, 27 ≤ k → k < 28 → SOK6 k := range_one 27 s6_27
theorem r6_28_29 : ∀ k, 28 ≤ k → k < 29 → SOK6 k := range_one 28 s6_28
theorem r6_27_29 : ∀ k, 27 ≤ k → k < 29 → SOK6 k := range_split 27 28 29 r6_27_28 r6_28_29
theorem r6_29_30 : ∀ k, 29 ≤ k → k < 30 → SOK6 k := range_one 29 s6_29
theorem r6_30_31 : ∀ k, 30 ≤ k → k < 31 → SOK6 k := range_one 30 s6_30
theorem r6_29_31 : ∀ k, 29 ≤ k → k < 31 → SOK6 k := range_split 29 30 31 r6_29_30 r6_30_31
theorem r6_27_31 : ∀ k, 27 ≤ k → k < 31 → SOK6 k := range_split 27 29 31 r6_27_29 r6_29_31
theorem r6_23_31 : ∀ k, 23 ≤ k → k < 31 → SOK6 k := range_split 23 27 31 r6_23_27 r6_27_31
theorem r6_15_31 : ∀ k, 15 ≤ k → k < 31 → SOK6 k := range_split 15 23 31 r6_15_23 r6_23_31
theorem r6_0_31 : ∀ k, 0 ≤ k → k < 31 → SOK6 k := range_split 0 15 31 r6_0_15 r6_15_31

theorem all6 : ∀ i, i < succ6.length → StateOK 6 (2 ^ 6 - 1) (Nat.shiftLeft 1 (Nat.sub 6 1)) T6 succ6.length succ6 i := by
  intro i hi
  have hl : succ6.length = 31 := by decide +kernel
  rw [hl] at hi ⊢
  exact r6_0_31 i (Nat.zero_le i) hi

theorem root6 : bset T6 31 0 = 2 ^ (2 ^ 6) - 1 := by decide +kernel
theorem wcheck6 : wcheck 1000000000 1358273028 succ6 weights6 = true := by decide +kernel
theorem wmin6 : weights6.all (fun v => Nat.ble 549848752 v) = true := by decide +kernel
theorem len6 : succ6.length = 31 ∧ weights6.length = 31 := by decide +kernel
theorem w0_6 : weights6.getD 0 0 ≤ 28 * 549848752 := by decide +kernel

/-- **The channel bound at width 6.** -/
theorem channel_bound_6 (n : Nat) :
    ∃ S : Finset (List Bool), (∀ x : Int → Bool, Clock x → visFrom x 0 n ∈ S) ∧
      S.card * 1000000000 ^ n ≤ 28 * 1358273028 ^ n := by
  have hN : 0 < succ6.length := by rw [len6.1]; decide
  have hE := explicit_sound 6 (by decide) T6 succ6 all6
  have hB0 : bset T6 succ6.length 0 = 2 ^ (2 ^ 6) - 1 := by rw [len6.1]; exact root6
  exact bound_of 6 (by decide) succ6 hN (bset T6 succ6.length) hB0 hE weights6 1000000000 1358273028 28 549848752
    wcheck6 (by rw [len6.1, len6.2]) wmin6 (by decide) w0_6 n


/-! controls at width 6: three wrong certificates are rejected, and the root passes against its own successors -/
theorem neg_dead : stateCheck 63 32 (bset T6 31 3) 0 1 (bset T6 31 1) = false := by decide +kernel
theorem neg_swap : stateCheck 63 32 (bset T6 31 4) (bset T6 31 3) 1 (bset T6 31 1) = false := by decide +kernel
theorem neg_drop : stateCheck 63 32 398046878878737797 (bset T6 31 4) 1 (bset T6 31 1) = false := by decide +kernel
theorem pos_root : stateCheck 63 32 (bset T6 31 1) (bset T6 31 2) 1 (bset T6 31 0) = true := by decide +kernel
end Rule30Submission
