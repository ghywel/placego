
/-- The predecessor, by triangular recovery of the whole row. -/
def previous (x : Row) : Row
  | 0 => x 0
  | 1 => xor (x 1) (x 0)
  | j + 2 => xor (x (j + 2)) (previous x (j + 1) || previous x j)

theorem xor_twice (a b : Bool) : xor (xor a b) b = a := by
  cases a <;> cases b <;> rfl

theorem step_previous (x : Row) : step (previous x) = x := by
  funext j
  cases j with
  | zero => rfl
  | succ k =>
    cases k with
    | zero => exact xor_twice _ _
    | succ i =>
      rw [step_add, previous]
      exact xor_twice _ _

theorem previous_step (x : Row) : previous (step x) = x := by
  have pair : ∀ i, previous (step x) i = x i ∧ previous (step x) (i + 1) = x (i + 1) := by
    intro i
    induction i with
    | zero => exact ⟨rfl, xor_twice _ _⟩
    | succ i ih =>
      refine ⟨ih.2, ?_⟩
      rw [previous, ih.1, ih.2, step_add]
      exact xor_twice _ _
  funext i
  exact (pair i).1

/-- **Every row has exactly one predecessor,** so a backward tick is well defined and the theorems on predecessors are not empty. -/
theorem predecessor_unique (x : Row) : ∃ z, step z = x ∧ ∀ y, step y = x → y = z :=
  ⟨previous x, step_previous x, fun y h => by rw [← h, previous_step]⟩

/-- `n` backward ticks. -/
def previousN : Nat → Row → Row
  | 0, x => x
  | n + 1, x => previous (previousN n x)

theorem iter_previousN (x : Row) (n : Nat) : iter (previousN n x) n = x := by
  induction n with
  | zero => rfl
  | succ n ih =>
    have e := iter_add (previousN (n + 1) x) 1 n
    rw [Nat.add_comm 1 n] at e
    rw [e]
    show iter (step (previous (previousN n x))) n = x
    rw [step_previous]; exact ih

namespace WindowClosed

/-- **A held row is not periodic**, when each window of the set ends in the wall's equal pair. -/
theorem held_not_periodic {W : Nat} {S : List (List Bool)} (C : Closed W S) (hW : 2 ≤ W)
    (wall : ∀ w, w ∈ S → w.getD (W - 2) false = w.getD (W - 1) false)
    {x : Row} {L P : Nat} (hL : 2 ≤ L) (h : Held W S x L) (hP : 0 < P) : iter x P ≠ x := by
  intro hper
  have hf := held_forever C hL h P x hper
  have hwall := wall _ hf.1
  rw [seg_getD x W _ (W - 2) (by omega), seg_getD x W _ (W - 1) (by omega)] at hwall
  have hr := h.2 (L + 3 * P + (W - 2)) (by omega)
  rw [show L + 3 * P + (W - 2) + 1 = L + 3 * P + (W - 1) by omega, ← hwall] at hr
  cases hb : x (L + 3 * P + (W - 2)) <;> simp [hb] at hr

/-- The two letters. -/
def letterSet : List (List Bool) := [wordA, wordB]

/-- **The letters are closed.** A row showing a letter with rain above it shows a letter at every backward tick. -/
theorem letters_closed : Closed 11 letterSet :=
  ⟨by decide, by decide, by decide, by decide, by decide, by decide⟩

/-- **After `B` comes `A`,** for every pair of lower cells. -/
theorem letter_after_B {z x : Row} {L : Nat} (hL : 2 ≤ L) (hs : step z = x) (h : Held 11 letterSet x L)
    (hb : seg x L 11 = wordB) : seg z (L + 3) 11 = wordA := by
  rw [next_seg letters_closed hL hs h, hb]
  generalize z (L - 1) = p1
  generalize z (L - 2) = p2
  revert p1 p2
  decide

/-- **After `A` comes `A` exactly when the two cells of the predecessor below the window are white.** -/
theorem letter_after_A {z x : Row} {L : Nat} (hL : 2 ≤ L) (hs : step z = x) (h : Held 11 letterSet x L)
    (ha : seg x L 11 = wordA) : seg z (L + 3) 11 = if (z (L - 1) || z (L - 2)) then wordB else wordA := by
  rw [next_seg letters_closed hL hs h, ha]
  generalize z (L - 1) = p1
  generalize z (L - 2) = p2
  revert p1 p2
  decide

/-! ## Windows as numbers

The checks on a closed set are finite, and the kernel runs them on numbers. A window of `W` cells is a number. `load` puts the two lower
cells under it and rain over it, `run` is the backward sweep cell by cell, and `nxt` reads the image window off the result. The theorems say
this is `next` on words. -/

/-- A word of `W` cells from a number, low to high. -/
def dec (W n : Nat) : List Bool := seg n.testBit 0 W

/-- One cell of the sweep: bit `i + 2` takes the inverse rule from the two bits below it. -/
def sw (i y : Nat) : Nat := y ^^^ ((((y >>> (i + 1)) ||| (y >>> i)) &&& 1) <<< (i + 2))

/-- The sweep. The test on `sw i y` never changes the value, since `0` stays `0`; it forces each cell as the kernel reaches it. -/
def run : Nat → Nat → Nat → Nat
  | 0, _, y => y
  | f + 1, i, y => cond (Nat.beq (sw i y) 0) 0 (run f (i + 1) (sw i y))

/-- The two lower cells, the window and six cells of rain over a black top. -/
def load (W n : Nat) (p1 p2 : Bool) : Nat := ((n ||| (42 <<< W)) <<< 2) ||| (p1.toNat <<< 1) ||| p2.toNat

/-- The whole sweep on a window. -/
def image (W n : Nat) (p1 p2 : Bool) : Nat := run (W + 6) 0 (load W n p1 p2)

/-- The image window. -/
def nxt (W n : Nat) (p1 p2 : Bool) : Nat := (image W n p1 p2 >>> 5) &&& (2 ^ W - 1)

/-- The finite check on one window number: a black top cell, and under each pair of lower cells rain resumes and the image window is in `T`. -/
def Fast (W : Nat) (T : List Nat) (n : Nat) : Prop :=
  n >>> (W - 1) = 1 ∧ ∀ p1 p2 : Bool, image W n p1 p2 >>> (W + 4) = 5 ∧ nxt W n p1 p2 ∈ T

instance (W : Nat) (T : List Nat) (n : Nat) : Decidable (Fast W T n) := by unfold Fast; infer_instance

theorem sw_bit (i y j : Nat) :
    (sw i y).testBit j = if j = i + 2 then xor (y.testBit (i + 2)) (y.testBit (i + 1) || y.testBit i) else y.testBit j := by
  have hone : ∀ a : Nat, (a &&& 1).testBit 0 = a.testBit 0 := by
    intro a; simp
  have hhi : ∀ (a k : Nat), (a &&& 1).testBit (k + 1) = false := by
    intro a k; simp [Nat.testBit_succ]
  unfold sw
  rw [Nat.testBit_xor, Nat.testBit_shiftLeft]
  by_cases c : j = i + 2
  · subst c
    simp only [ge_iff_le, Nat.le_refl, decide_true, Bool.true_and, Nat.sub_self, if_true]
    rw [hone, Nat.testBit_or, Nat.testBit_shiftRight, Nat.testBit_shiftRight]
    simp
  · rw [if_neg c]
    by_cases d : i + 2 ≤ j
    · obtain ⟨k, rfl⟩ : ∃ k, j = i + 2 + (k + 1) := ⟨j - (i + 2) - 1, by omega⟩
      rw [show i + 2 + (k + 1) - (i + 2) = k + 1 by omega, hhi]
      simp
    · simp [d]

theorem run_zero (f i : Nat) : run f i 0 = 0 := by
  induction f generalizing i with
  | zero => rfl
  | succ f ih =>
    have : sw i 0 = 0 := by simp [sw]
    simp [run, this]

theorem run_succ (f i y : Nat) : run (f + 1) i y = run f (i + 1) (sw i y) := by
  show cond (Nat.beq (sw i y) 0) 0 (run f (i + 1) (sw i y)) = _
  cases h : Nat.beq (sw i y) 0 with
  | false => rfl
  | true =>
    have : sw i y = 0 := Nat.eq_of_beq_eq_true h
    rw [this, run_zero]; rfl

/-- The sweep leaves every bit below its start alone. -/
theorem run_low (f i y j : Nat) (hj : j < i + 2) : (run f i y).testBit j = y.testBit j := by
  induction f generalizing i y with
  | zero => rfl
  | succ f ih =>
    rw [run_succ, ih (i + 1) (sw i y) (by omega), sw_bit, if_neg (by omega)]

/-- And every bit above its end. -/
theorem run_high (f i y j : Nat) (hj : i + 2 + f ≤ j) : (run f i y).testBit j = y.testBit j := by
  induction f generalizing i y with
  | zero => rfl
  | succ f ih =>
    rw [run_succ, ih (i + 1) (sw i y) (by omega), sw_bit, if_neg (by omega)]

/-- **The sweep is `back`.** -/
theorem run_back (n i y : Nat) :
    seg (run n i y).testBit (i + 2) n = back (y.testBit (i + 1)) (y.testBit i) (seg y.testBit (i + 2) n) := by
  induction n generalizing i y with
  | zero => rfl
  | succ n ih =>
    have hseg : seg (sw i y).testBit (i + 3) n = seg y.testBit (i + 3) n := by
      have : ∀ (m L : Nat), i + 3 ≤ L → seg (sw i y).testBit L m = seg y.testBit L m := by
        intro m
        induction m with
        | zero => intro L _; rfl
        | succ m ihm =>
          intro L hL
          show (sw i y).testBit L :: seg (sw i y).testBit (L + 1) m = y.testBit L :: seg y.testBit (L + 1) m
          rw [ihm (L + 1) (by omega), sw_bit, if_neg (by omega)]
      exact this n (i + 3) (Nat.le_refl _)
    have h2 : (sw i y).testBit (i + 2) = xor (y.testBit (i + 2)) (y.testBit (i + 1) || y.testBit i) := by
      rw [sw_bit, if_pos rfl]
    have h1 : (sw i y).testBit (i + 1) = y.testBit (i + 1) := by
      rw [sw_bit, if_neg (by omega)]
    show (run (n + 1) i y).testBit (i + 2) :: seg (run (n + 1) i y).testBit (i + 3) n =
      xor (y.testBit (i + 2)) (y.testBit (i + 1) || y.testBit i) ::
        back (xor (y.testBit (i + 2)) (y.testBit (i + 1) || y.testBit i)) (y.testBit (i + 1)) (seg y.testBit (i + 3) n)
    rw [run_succ, run_low n (i + 1) (sw i y) (i + 2) (by omega), h2]
    have := ih (i + 1) (sw i y)
    rw [show i + 1 + 2 = i + 3 by omega, show i + 1 + 1 = i + 2 by omega, h2, h1, hseg] at this
    rw [this]

theorem load_low1 (W n : Nat) (p1 p2 : Bool) : (load W n p1 p2).testBit 1 = p1 := by
  have a : ((n ||| (42 <<< W)) <<< 2).testBit 1 = false := by simp [Nat.testBit_shiftLeft]
  cases p1 <;> cases p2 <;> (simp only [load, Nat.testBit_or, a]; decide)

theorem load_low0 (W n : Nat) (p1 p2 : Bool) : (load W n p1 p2).testBit 0 = p2 := by
  have a : ((n ||| (42 <<< W)) <<< 2).testBit 0 = false := by simp
  cases p1 <;> cases p2 <;> (simp only [load, Nat.testBit_or, a]; decide)

theorem load_bit (W n : Nat) (p1 p2 : Bool) (j : Nat) :
    (load W n p1 p2).testBit (j + 2) = (n.testBit j || (42 <<< W).testBit j) := by
  have e : ∀ b : Bool, (b.toNat <<< 1).testBit (j + 2) = false := by
    intro b; rw [Nat.testBit_shiftLeft]; cases b <;> simp [Nat.testBit_succ]
  have f : ∀ b : Bool, b.toNat.testBit (j + 2) = false := by
    intro b; cases b <;> simp [Nat.testBit_succ]
  simp only [load, Nat.testBit_or, e, f, Bool.or_false]
  rw [Nat.testBit_shiftLeft]
  simp [Nat.testBit_or]

theorem seg_ext {f g : Nat → Bool} (m : Nat) : ∀ L M, (∀ i, i < m → f (L + i) = g (M + i)) → seg f L m = seg g M m := by
  induction m with
  | zero => intro _ _ _; rfl
  | succ m ih =>
    intro L M h
    show f L :: seg f (L + 1) m = g M :: seg g (M + 1) m
    rw [show f L = g M from h 0 (by omega), ih (L + 1) (M + 1) (fun i hi => by
      rw [show L + 1 + i = L + (i + 1) by omega, show M + 1 + i = M + (i + 1) by omega]; exact h (i + 1) (by omega))]

/-- A number whose top bit is bit `W - 1`. -/
theorem top_facts {W n : Nat} (hW : 1 ≤ W) (hn : n >>> (W - 1) = 1) :
    n.testBit (W - 1) = true ∧ ∀ j, W ≤ j → n.testBit j = false := by
  constructor
  · have : (n >>> (W - 1)).testBit 0 = n.testBit (W - 1) := by simp
    rw [← this, hn]; rfl
  · intro j hj
    obtain ⟨k, rfl⟩ : ∃ k, j = (W - 1) + (k + 1) := ⟨j - (W - 1) - 1, by omega⟩
    have : (n >>> (W - 1)).testBit (k + 1) = n.testBit (W - 1 + (k + 1)) := by simp [Nat.testBit_shiftRight]
    rw [← this, hn]
    simp [Nat.testBit_succ]

theorem load_seg {W n : Nat} (hW : 1 ≤ W) (hn : n >>> (W - 1) = 1) (p1 p2 : Bool) :
    seg (load W n p1 p2).testBit 2 (W + 6) = inp W (dec W n) := by
  obtain ⟨htop, hhi⟩ := top_facts hW hn
  have split : seg (load W n p1 p2).testBit 2 (W + 6) =
      seg (load W n p1 p2).testBit 2 (W - 1) ++ seg (load W n p1 p2).testBit (2 + (W - 1)) 7 := by
    rw [← seg_append]; congr 1; omega
  have hlow : ∀ j, j < W → (42 <<< W).testBit j = false := by
    intro j hj; simp [Nat.testBit_shiftLeft]; omega
  have htake : (dec W n).take (W - 1) = seg n.testBit 0 (W - 1) := by
    have e1 : dec W n = seg n.testBit 0 (W - 1) ++ seg n.testBit (0 + (W - 1)) 1 := by
      rw [← seg_append]; show seg n.testBit 0 W = _; congr 1; omega
    rw [e1]; exact List.take_left' (seg_length _ _ _)
  have hget : (dec W n).getD (W - 1) false = true := by
    have := seg_getD n.testBit W 0 (W - 1) (by omega)
    rw [Nat.zero_add] at this
    show (seg n.testBit 0 W).getD (W - 1) false = true
    rw [this, htop]
  have a1 : seg (load W n p1 p2).testBit 2 (W - 1) = seg n.testBit 0 (W - 1) := by
    have g : ∀ (m L : Nat), L + m ≤ W → seg (load W n p1 p2).testBit (L + 2) m = seg n.testBit L m := by
      intro m
      induction m with
      | zero => intro _ _; rfl
      | succ m ih =>
        intro L hLm
        show (load W n p1 p2).testBit (L + 2) :: seg (load W n p1 p2).testBit (L + 2 + 1) m = n.testBit L :: seg n.testBit (L + 1) m
        rw [load_bit, hlow L (by omega), Bool.or_false, show L + 2 + 1 = L + 1 + 2 by omega, ih (L + 1) (by omega)]
    exact g (W - 1) 0 (by omega)
  have a2 : seg (load W n p1 p2).testBit (2 + (W - 1)) 7 = alt true 7 := by
    have bit : ∀ k, k < 7 → (load W n p1 p2).testBit (2 + (W - 1) + k) = (alt true 7).getD k false := by
      intro k hk
      rw [show 2 + (W - 1) + k = (W - 1 + k) + 2 by omega, load_bit]
      have hs : ∀ m : Nat, (42 <<< W).testBit (W + m) = (42 : Nat).testBit m := by
        intro m; simp [Nat.testBit_shiftLeft]
      match k, hk with
      | 0, _ => rw [show W - 1 + 0 = W - 1 by omega, htop]; rfl
      | 1, _ => rw [show W - 1 + 1 = W + 0 by omega, hhi _ (by omega), hs]; rfl
      | 2, _ => rw [show W - 1 + 2 = W + 1 by omega, hhi _ (by omega), hs]; rfl
      | 3, _ => rw [show W - 1 + 3 = W + 2 by omega, hhi _ (by omega), hs]; rfl
      | 4, _ => rw [show W - 1 + 4 = W + 3 by omega, hhi _ (by omega), hs]; rfl
      | 5, _ => rw [show W - 1 + 5 = W + 4 by omega, hhi _ (by omega), hs]; rfl
      | 6, _ => rw [show W - 1 + 6 = W + 5 by omega, hhi _ (by omega), hs]; rfl
    have eq : ∀ (m : Nat) (l : List Bool) (L : Nat), l.length = m →
        (∀ k, k < m → (load W n p1 p2).testBit (L + k) = l.getD k false) → seg (load W n p1 p2).testBit L m = l := by
      intro m
      induction m with
      | zero => intro l _ hl _; cases l with
        | nil => rfl
        | cons _ _ => simp at hl
      | succ m ih =>
        intro l L hl h
        cases l with
        | nil => simp at hl
        | cons b r =>
          show (load W n p1 p2).testBit L :: seg (load W n p1 p2).testBit (L + 1) m = b :: r
          have h0 := h 0 (by omega)
          simp only [Nat.add_zero, List.getD_cons_zero] at h0
          rw [h0, ih r (L + 1) (by simpa using hl) (fun k hk => by
            have := h (k + 1) (by omega)
            rw [show L + (k + 1) = L + 1 + k by omega] at this
            simpa using this)]
    exact eq 7 _ _ rfl bit
  rw [split, a1, a2]
  show _ = (dec W n).take (W - 1) ++ alt ((dec W n).getD (W - 1) false) 7
  rw [htake, hget]

/-- The sweep is `back` on the loaded window. -/
theorem image_back {W n : Nat} (hW : 1 ≤ W) (hn : n >>> (W - 1) = 1) (p1 p2 : Bool) :
    seg (image W n p1 p2).testBit 2 (W + 6) = back p1 p2 (inp W (dec W n)) := by
  have := run_back (W + 6) 0 (load W n p1 p2)
  rw [show (0 : Nat) + 2 = 2 from rfl, show (0 : Nat) + 1 = 1 from rfl, load_low1, load_low0, load_seg hW hn] at this
  exact this

theorem next_fast {W n : Nat} (hW : 1 ≤ W) (hn : n >>> (W - 1) = 1) (p1 p2 : Bool) :
    next W (dec W n) p1 p2 = dec W (nxt W n p1 p2) := by
  show ((back p1 p2 (inp W (dec W n))).drop 3).take W = _
  rw [← image_back hW hn]
  have e1 : seg (image W n p1 p2).testBit 2 (W + 6) =
      seg (image W n p1 p2).testBit 2 3 ++ seg (image W n p1 p2).testBit (2 + 3) (W + 3) := by
    rw [← seg_append]; congr 1; omega
  have e2 : seg (image W n p1 p2).testBit (2 + 3) (W + 3) =
      seg (image W n p1 p2).testBit (2 + 3) W ++ seg (image W n p1 p2).testBit (2 + 3 + W) 3 := seg_append _ _ _ _
  rw [e1, List.drop_left' (seg_length _ _ _), e2, List.take_left' (seg_length _ _ _)]
  refine seg_ext W _ _ (fun i hi => ?_)
  show (image W n p1 p2).testBit (2 + 3 + i) = ((image W n p1 p2 >>> 5) &&& (2 ^ W - 1)).testBit (0 + i)
  rw [Nat.testBit_and, Nat.testBit_shiftRight, Nat.testBit_two_pow_sub_one]
  simp only [Nat.zero_add]
  rw [show 5 + i = 2 + 3 + i by omega]
  simp [hi]

/-- **A closed set from numbers.** -/
theorem closed_fast {W : Nat} (hW : 1 ≤ W) (S : List Nat) (h : ∀ n, n ∈ S → Fast W S n) : Closed W (S.map (dec W)) := by
  have bits : ∀ n, n ∈ S → ∀ (p1 p2 : Bool) (k : Nat), k < 4 →
      (back p1 p2 (inp W (dec W n))).getD (W + 2 + k) false = (5 : Nat).testBit k := by
    intro n hn p1 p2 k hk
    have ok := ((h n hn).2 p1 p2).1
    rw [← image_back hW (h n hn).1, seg_getD _ _ _ _ (by omega), ← ok, Nat.testBit_shiftRight]
    rw [show 2 + (W + 2 + k) = W + 4 + k by omega]
  have rain : ∀ n, n ∈ S → ∀ (k : Nat), k < 2 → (inp W (dec W n)).getD (W + 4 + k) false = (42 : Nat).testBit (4 + k) := by
    intro n hn k hk
    rw [← load_seg hW (h n hn).1 false false, seg_getD _ _ _ _ (by omega), show 2 + (W + 4 + k) = (W + (4 + k)) + 2 by omega, load_bit]
    have hi := (top_facts hW (h n hn).1).2 (W + (4 + k)) (by omega)
    rw [hi]
    simp [Nat.testBit_shiftLeft]
  have sub : ∀ w, w ∈ S.map (dec W) → ∃ n, n ∈ S ∧ w = dec W n := by
    intro w hw
    obtain ⟨n, hn, rfl⟩ := List.mem_map.1 hw
    exact ⟨n, hn, rfl⟩
  refine ⟨hW, ?_, ?_, ?_, ?_, ?_⟩
  · intro w hw p1 p2
    obtain ⟨n, hn, rfl⟩ := sub w hw
    rw [next_fast hW (h n hn).1]
    exact List.mem_map.2 ⟨_, ((h n hn).2 p1 p2).2, rfl⟩
  · intro w hw p1 p2
    obtain ⟨n, hn, rfl⟩ := sub w hw
    have b0 := bits n hn p1 p2 0 (by omega)
    have b1 := bits n hn p1 p2 1 (by omega)
    rw [show W + 2 + 0 = W + 2 by omega] at b0
    rw [show W + 2 + 1 = W + 3 by omega] at b1
    rw [b0, b1]; decide
  · intro w hw p1 p2
    obtain ⟨n, hn, rfl⟩ := sub w hw
    have b1 := bits n hn p1 p2 1 (by omega)
    have b2 := bits n hn p1 p2 2 (by omega)
    rw [show W + 2 + 1 = W + 3 by omega] at b1
    rw [show W + 2 + 2 = W + 4 by omega] at b2
    rw [b1, b2]; decide
  · intro w hw p1 p2
    obtain ⟨n, hn, rfl⟩ := sub w hw
    have b2 := bits n hn p1 p2 2 (by omega)
    have r0 := rain n hn 0 (by omega)
    rw [show W + 2 + 2 = W + 4 by omega] at b2
    rw [show W + 4 + 0 = W + 4 by omega] at r0
    rw [b2, r0]; decide
  · intro w hw p1 p2
    obtain ⟨n, hn, rfl⟩ := sub w hw
    have b3 := bits n hn p1 p2 3 (by omega)
    have r1 := rain n hn 1 (by omega)
    rw [show W + 2 + 3 = W + 5 by omega] at b3
    rw [show W + 4 + 1 = W + 5 by omega] at r1
    rw [b3, r1]; decide

/-- The cells of a word above `k`, from the number. -/
theorem dec_drop (W k n : Nat) (hk : k ≤ W) : (dec W n).drop k = dec (W - k) (n >>> k) := by
  have e : dec W n = seg n.testBit 0 k ++ seg n.testBit (0 + k) (W - k) := by
    rw [← seg_append]; show seg n.testBit 0 W = _; congr 1; omega
  rw [e, List.drop_left' (seg_length _ _ _)]
  refine seg_ext (W - k) _ _ (fun i _ => ?_)
  simp [Nat.testBit_shiftRight]

theorem wordA_dec : wordA = dec 11 1596 := by decide
theorem wordB_dec : wordB = dec 11 1594 := by decide

/-- The word above cell `L + k` of a window, read on the row. -/
theorem seg_drop (x : Row) (L W k : Nat) (hk : k ≤ W) : (seg x L W).drop k = seg x (L + k) (W - k) := by
  have e : seg x L W = seg x L k ++ seg x (L + k) (W - k) := by
    rw [← seg_append]; congr 1; omega
  rw [e, List.drop_left' (seg_length x k L)]

theorem Fast.mono {W n : Nat} {T U : List Nat} (h : ∀ m, m ∈ T → m ∈ U) (f : Fast W T n) : Fast W U n :=
  ⟨f.1, fun p1 p2 => ⟨(f.2 p1 p2).1, h _ (f.2 p1 p2).2⟩⟩

/-- A word of `W` cells from a number whose top letter is `A` or `B` ends in the wall's equal pair. -/
theorem wall_of_letter {W n : Nat} (hW : 11 ≤ W) (h : n >>> (W - 11) = 1596 ∨ n >>> (W - 11) = 1594) :
    (dec W n).getD (W - 2) false = (dec W n).getD (W - 1) false := by
  have g1 := seg_getD n.testBit W 0 (W - 2) (by omega)
  have g2 := seg_getD n.testBit W 0 (W - 1) (by omega)
  rw [Nat.zero_add] at g1 g2
  show (seg n.testBit 0 W).getD (W - 2) false = (seg n.testBit 0 W).getD (W - 1) false
  rw [g1, g2]
  have e1 : n.testBit (W - 2) = (n >>> (W - 11)).testBit 9 := by
    rw [Nat.testBit_shiftRight, show W - 11 + 9 = W - 2 by omega]
  have e2 : n.testBit (W - 1) = (n >>> (W - 11)).testBit 10 := by
    rw [Nat.testBit_shiftRight, show W - 11 + 10 = W - 1 by omega]
  rw [e1, e2]
  rcases h with h | h <;> rw [h] <;> decide

/-- A lock: window numbers in `k` phases, each phase going to the next for every pair of lower cells. -/
structure Lock (W k : Nat) (Ph : List (List Nat)) (All : List Nat) : Prop where
  width : 11 ≤ W
  period : 0 < k
  cycle : ∀ r, r < k → ∀ n, n ∈ Ph.getD r [] → Fast W (Ph.getD ((r + 1) % k) []) n
  sub : ∀ r, r < k → ∀ n, n ∈ Ph.getD r [] → n ∈ All
  cover : ∀ n, n ∈ All → ∃ r, r < k ∧ n ∈ Ph.getD r []

namespace Lock
variable {W k : Nat} {Ph : List (List Nat)} {All : List Nat}

theorem closed (H : Lock W k Ph All) : Closed W (All.map (dec W)) :=
  closed_fast (by have := H.width; omega) All (fun n hn => by
    obtain ⟨r, hr, hm⟩ := H.cover n hn
    exact Fast.mono (H.sub _ (Nat.mod_lt _ H.period)) (H.cycle r hr n hm))

theorem phase (H : Lock W k Ph All) {x : Row} {L : Nat} (h : Held W (All.map (dec W)) x L) :
    ∃ r, r < k ∧ seg x L W ∈ (Ph.getD r []).map (dec W) := by
  obtain ⟨n, hn, e⟩ := List.mem_map.1 h.1
  obtain ⟨r, hr, hm⟩ := H.cover n hn
  exact ⟨r, hr, List.mem_map.2 ⟨n, hm, e⟩⟩

/-- **The phases follow each other for ever,** whatever lies below the window. -/
theorem forever (H : Lock W k Ph All) {x : Row} {L r : Nat} (hL : 2 ≤ L) (h : Held W (All.map (dec W)) x L)
    (hp : seg x L W ∈ (Ph.getD (r % k) []).map (dec W)) :
    ∀ n z, iter z n = x → seg z (L + 3 * n) W ∈ (Ph.getD ((r + n) % k) []).map (dec W) := by
  have hW : 1 ≤ W := by have := H.width; omega
  intro n
  induction n with
  | zero =>
    intro z hz
    have e : z = x := hz
    subst e
    exact hp
  | succ n ih =>
    intro z hz
    have e : iter (step z) n = x := by
      have := iter_add z 1 n
      rw [Nat.add_comm 1 n] at this
      rw [← hz, this]; rfl
    obtain ⟨m, hm, em⟩ := List.mem_map.1 (ih (step z) e)
    have hy := held_forever H.closed hL h n (step z) e
    have q := next_seg H.closed (L := L + 3 * n) (by omega) rfl hy
    rw [← em, next_fast hW (H.cycle _ (Nat.mod_lt _ H.period) m hm).1] at q
    rw [show L + 3 * (n + 1) = L + 3 * n + 3 by omega, q]
    refine List.mem_map.2 ⟨_, ?_, rfl⟩
    have := ((H.cycle _ (Nat.mod_lt _ H.period) m hm).2 (z (L + 3 * n - 1)) (z (L + 3 * n - 2))).2
    rw [Nat.mod_add_mod] at this
    exact this

/-- **The letters run through the phases for ever.** -/
theorem letters (H : Lock W k Ph All) (lc : Nat → List Bool)
    (hl : ∀ r, r < k → ∀ n, n ∈ Ph.getD r [] → dec 11 (n >>> (W - 11)) = lc r)
    {x : Row} {L : Nat} (hL : 2 ≤ L) (h : Held W (All.map (dec W)) x L) :
    ∃ r, r < k ∧ ∀ n z, iter z n = x → seg z (L + 3 * n + (W - 11)) 11 = lc ((r + n) % k) := by
  have hW := H.width
  obtain ⟨r, hr, hp⟩ := H.phase h
  refine ⟨r, hr, fun n z hz => ?_⟩
  have hp' : seg x L W ∈ (Ph.getD (r % k) []).map (dec W) := by rwa [Nat.mod_eq_of_lt hr]
  obtain ⟨m, hm, em⟩ := List.mem_map.1 (H.forever hL h hp' n z hz)
  have d1 := seg_drop z (L + 3 * n) W (W - 11) (by omega)
  rw [show W - (W - 11) = 11 by omega, ← em, dec_drop W (W - 11) m (by omega), show W - (W - 11) = 11 by omega] at d1
  rw [← d1]
  exact hl _ (Nat.mod_lt _ H.period) m hm

end Lock

/-- A row with the window `n` on a black edge, one white cell below it, and rain above it. -/
def anchor (W n j : Nat) : Bool :=
  if j = 0 then true else if j = 1 then false else if j < W + 2 then n.testBit (j - 2) else decide ((j - W) % 2 = 1)

/-- **Every window of a set occurs on an anchored row.** -/
theorem anchor_held {W n : Nat} {S : List (List Bool)} (hW : 1 ≤ W) (hn : n >>> (W - 1) = 1) (hm : dec W n ∈ S) :
    anchor W n 0 = true ∧ Held W S (anchor W n) 2 := by
  have htop := (top_facts hW hn).1
  have hs : seg (anchor W n) 2 W = dec W n := by
    refine seg_ext W 2 0 (fun i hi => ?_)
    simp [anchor, show ¬2 + i = 1 by omega, show 2 + i < W + 2 by omega]
  refine ⟨rfl, by rw [hs]; exact hm, fun j hj => ?_⟩
  by_cases c : j = W + 1
  · subst c
    have a1 : anchor W n (W + 1) = true := by
      simp only [anchor, show ¬W + 1 = 0 by omega, show ¬W + 1 = 1 by omega, show W + 1 < W + 2 by omega, ite_false, ite_true]
      rw [show W + 1 - 2 = W - 1 by omega]; exact htop
    have a2 : anchor W n (W + 1 + 1) = false := by
      simp only [anchor, show ¬W + 1 + 1 = 0 by omega, show ¬W + 1 + 1 = 1 by omega, show ¬W + 1 + 1 < W + 2 by omega, ite_false]
      rw [show W + 1 + 1 - W = 2 by omega]; rfl
    rw [a1, a2]; rfl
  · have q : W + 2 ≤ j := by omega
    simp only [anchor, show ¬j = 0 by omega, show ¬j + 1 = 0 by omega, show ¬j = 1 by omega, show ¬j + 1 = 1 by omega,
      show ¬j < W + 2 by omega, show ¬j + 1 < W + 2 by omega, ite_false]
    by_cases a : (j - W) % 2 = 1
    · have b : ¬(j + 1 - W) % 2 = 1 := by omega
      simp [a, b]
    · have b : (j + 1 - W) % 2 = 1 := by omega
      simp [a, b]

/-! ## Forward ticks on numbers -/

/-- One tick on a number: exactly the edge map. -/
def fw (y : Nat) : Nat := y ^^^ ((y <<< 1) ||| (y <<< 2))

def fwN : Nat → Nat → Nat
  | 0, y => y
  | k + 1, y => fw (fwN k y)

theorem fw_bit (y : Nat) : (fw y).testBit = step y.testBit := by
  funext j
  match j with
  | 0 => simp [fw, T]
  | 1 => simp [fw, T, Nat.testBit_xor, Nat.testBit_or, Nat.testBit_shiftLeft]
  | j + 2 => simp [fw, T, Nat.testBit_xor, Nat.testBit_or, Nat.testBit_shiftLeft]

theorem iter_fw (y k : Nat) : iter y.testBit k = (fwN k y).testBit := by
  induction k with
  | zero => rfl
  | succ k ih =>
    show step (iter y.testBit k) = _
    rw [ih]; exact (fw_bit _).symm

/-- Two rows that agree below `N` keep agreeing below `N`. -/
theorem iter_low {x y : Row} {N : Nat} (h : ∀ j, j < N → x j = y j) (k : Nat) : ∀ j, j < N → iter x k j = iter y k j := by
  induction k with
  | zero => exact h
  | succ k ih =>
    intro j hj
    show step (iter x k) j = step (iter y k) j
    match j, hj with
    | 0, hj => exact ih 0 hj
    | 1, hj =>
      show xor _ _ = xor _ _
      rw [ih 1 hj, ih 0 (by omega)]
    | j + 2, hj =>
      show xor _ (_ || _) = xor _ (_ || _)
      rw [ih (j + 2) hj, ih (j + 1) (by omega), ih j (by omega)]

/-- A rain tail above `D` is a rain tail above `D + 2 k` after `k` ticks. -/
theorem iter_tail {x : Row} {D : Nat} (h : ∀ j, D ≤ j → x (j + 1) = !x j) (k : Nat) :
    ∀ j, D + 2 * k ≤ j → iter x k (j + 1) = !iter x k j := by
  induction k with
  | zero => exact h
  | succ k ih =>
    intro j hj
    exact step_rain_tail ih j (by omega)

end WindowClosed
