/-!
Pulse-profile contribution under development (GC2044).
Core Lean; no imports. This file proves local algebra and the exact interval budget.
Cyclic weight/run count is implemented below; the periodic hole/delay bridge remains pending.
No finite-seed ancestry, settling bound, novelty clearance or portal submission is claimed.
-/
namespace Rule30PulseProfiles

def bit (b : Bool) : Int := if b then 1 else 0

def source (next pulse current : Bool) : Bool := xor next (pulse || current)

theorem source_solves (next pulse current : Bool) :
    xor (source next pulse current) (pulse || current) = next := by
  cases next <;> cases pulse <;> cases current <;> rfl

theorem source_unique (a next pulse current : Bool)
    (h : next = xor a (pulse || current)) : a = source next pulse current := by
  cases a <;> cases next <;> cases pulse <;> cases current <;> simp_all [source]

theorem source_without_pulse (next current : Bool) :
    source next false current = xor next current := rfl

theorem source_black_current (next pulse : Bool) :
    source next pulse true = xor next true := by cases pulse <;> rfl

theorem source_white_pulse (next : Bool) :
    source next true false = !(xor next false) := by cases next <;> rfl

/-- Pointwise signed weight correction; cyclic summation will be a separate theorem. -/
theorem source_bit_correction (next pulse current : Bool) :
    bit (source next pulse current) = bit (xor next current) +
      (if pulse then (if current then 0 else if next then -1 else 1) else 0) := by
  cases next <;> cases pulse <;> cases current <;> decide

/-- The six nonempty intervals and the empty interval of delays (k,l,1), slope5/2, doubled. -/
def intervalDebt2 (k l : Int) : Int :=
  max 0 (max (2*k-5) (max (2*l-5) (max (-3)
    (max (2*k+2*l-10) (max (2*l-8) (2*k+2*l-13))))))

def reducedDebt2 (k l : Int) : Int :=
  max 0 (max (2*k-5) (max (2*k+2*l-10) (2*l-5)))

theorem intervalDebt2_reduce (k l : Int) :
    intervalDebt2 k l = reducedDebt2 k l := by
  unfold intervalDebt2 reducedDebt2
  omega

theorem reducedDebt2_monotone (k k' l : Int) (h : k ≤ k') :
    reducedDebt2 k l ≤ reducedDebt2 k' l := by
  unfold reducedDebt2
  omega

theorem intervalDebt2_monotone (k k' l : Int) (h : k ≤ k') :
    intervalDebt2 k l ≤ intervalDebt2 k' l := by
  rw [intervalDebt2_reduce, intervalDebt2_reduce]
  exact reducedDebt2_monotone k k' l h

theorem intervalDebt2_at_pulse (q l : Int) (hq : 4 ≤ q) (hl : l ≤ q-1) :
    intervalDebt2 q l = 2*q-5 + max 0 (2*l-5) := by
  rw [intervalDebt2_reduce]
  unfold reducedDebt2
  omega

/-- Conditional arithmetic budget: the actual cyclic delay identification is still to be formalized. -/
theorem pulse_window_bound (q k l : Int) (hq : 4 ≤ q) (hk : k ≤ q) (hl : l ≤ q-1) :
    intervalDebt2 k l ≤ 2*q-5 + max 0 (2*l-5) := by
  rw [← intervalDebt2_at_pulse q l hq hl]
  exact intervalDebt2_monotone k q l hk

/-- Literal Rule30 and its left-diagonal coordinates for arbitrary initial rows. -/
def step (x : Int → Bool) (i : Int) : Bool := xor (x (i-1)) (x i || x (i+1))
def evol : Nat → (Int → Bool) → Int → Bool
  | 0, x => x
  | t+1, x => step (evol t x)
def leftDiag (x : Int → Bool) (j : Int) (t : Nat) : Bool := evol t x (j-t)

theorem leftDiag_step (x : Int → Bool) (j : Int) (t : Nat) :
    leftDiag x (j+2) (t+1) =
      xor (leftDiag x j t) (leftDiag x (j+1) t || leftDiag x (j+2) t) := by
  simp only [leftDiag, evol, step]
  congr 1
  · congr 1; omega
  · congr 1 <;> congr 1 <;> omega

/-- Sum over the first n natural indices; integer values keep boundary corrections signed. -/
def total (n : Nat) (f : Nat → Int) : Int :=
  match n with
  | 0 => 0
  | n+1 => total n f + f n

theorem total_congr (n : Nat) (f g : Nat → Int) (h : ∀ i, f i = g i) :
    total n f = total n g := by
  induction n with
  | zero => rfl
  | succ n ih => simp only [total, ih, h]

theorem total_add (n : Nat) (f g : Nat → Int) :
    total n (fun i => f i + g i) = total n f + total n g := by
  induction n with
  | zero => rfl
  | succ n ih => simp only [total, ih]; omega

theorem total_delta (n s : Nat) (v : Int) :
    total n (fun i => if i = s then v else 0) = if s < n then v else 0 := by
  induction n with
  | zero => simp [total]
  | succ n ih =>
    simp only [total, ih]
    by_cases h : s < n
    · have hn : n ≠ s := by omega
      have hs : s < n+1 := by omega
      simp [h, hn, hs]
    · by_cases he : n = s
      · subst s; simp
      · have hs : ¬s < n+1 := by omega
        simp [h, he, hs]

def weight (f : Nat → Bool) (n : Nat) : Int := total n (fun i => bit (f i))
def rises (f : Nat → Bool) (n : Nat) : Int :=
  total n (fun i => if !f i && f (i+1) then 1 else 0)
def changes (f : Nat → Bool) (n : Nat) : Int :=
  total n (fun i => bit (xor (f (i+1)) (f i)))

/-- The boundary term is explicit before the word is closed into a cycle. -/
theorem changes_telescopes (f : Nat → Bool) (n : Nat) :
    changes f n = 2*rises f n + bit (f 0) - bit (f n) := by
  induction n with
  | zero => simp [changes, rises, total]
  | succ n ih =>
    simp only [changes, rises, total] at *
    cases h : f n <;> cases h' : f (n+1) <;> simp [bit, h, h'] at * <;> omega

/-- Cyclic runs are counted by white-to-black edges, zero for either constant word. -/
theorem cyclic_changes (f : Nat → Bool) (q : Nat) (hc : f q = f 0) :
    changes f q = 2*rises f q := by
  have h := changes_telescopes f q
  rw [hc] at h
  omega

def correction (next current : Bool) : Int := if current then 0 else if next then -1 else 1
def profileSource (f : Nat → Bool) (s i : Nat) : Bool :=
  source (f (i+1)) (decide (i=s)) (f i)

theorem profileSource_correction (f : Nat → Bool) (s i : Nat) :
    bit (profileSource f s i) = bit (xor (f (i+1)) (f i)) +
      (if i=s then correction (f (s+1)) (f s) else 0) := by
  by_cases h : i=s
  · subst i
    simpa [profileSource, correction] using source_bit_correction (f (s+1)) true (f s)
  · simp [profileSource, h, source]

/-- Exact cyclic source weight, including both constant-word cases. -/
theorem pulse_source_weight (f : Nat → Bool) (q s : Nat) (hs : s < q) (hc : f q = f 0) :
    weight (profileSource f s) q = 2*rises f q + correction (f (s+1)) (f s) := by
  unfold weight
  calc
    total q (fun i => bit (profileSource f s i)) =
        total q (fun i => bit (xor (f (i+1)) (f i)) +
          if i=s then correction (f (s+1)) (f s) else 0) :=
      total_congr q _ _ (profileSource_correction f s)
    _ = changes f q + correction (f (s+1)) (f s) := by
      rw [total_add, total_delta]
      simp [changes, hs]
    _ = 2*rises f q + correction (f (s+1)) (f s) := by rw [cyclic_changes f q hc]

theorem pulse_source_black (f : Nat → Bool) (q s : Nat) (hs : s < q) (hc : f q = f 0)
    (hb : f s = true) : weight (profileSource f s) q = 2*rises f q := by
  simpa [correction, hb] using pulse_source_weight f q s hs hc

theorem pulse_source_white_white (f : Nat → Bool) (q s : Nat) (hs : s < q) (hc : f q = f 0)
    (hb : f s = false) (hn : f (s+1) = false) :
    weight (profileSource f s) q = 2*rises f q + 1 := by
  simpa [correction, hb, hn] using pulse_source_weight f q s hs hc

theorem pulse_source_white_black (f : Nat → Bool) (q s : Nat) (hs : s < q) (hc : f q = f 0)
    (hb : f s = false) (hn : f (s+1) = true) :
    weight (profileSource f s) q + 1 = 2*rises f q := by
  have h := pulse_source_weight f q s hs hc
  simp [correction, hb, hn] at h
  omega

theorem heavy_source_two_runs (f : Nat → Bool) (q s : Nat) (hs : s < q) (hc : f q = f 0)
    (hh : 3 < weight (profileSource f s) q) : 2 ≤ rises f q := by
  have h := pulse_source_weight f q s hs hc
  have hb : correction (f (s+1)) (f s) ≤ 1 := by
    cases f (s+1) <;> cases f s <;> decide
  omega

end Rule30PulseProfiles

#print axioms Rule30PulseProfiles.source_bit_correction
#print axioms Rule30PulseProfiles.pulse_window_bound
#print axioms Rule30PulseProfiles.leftDiag_step

#print axioms Rule30PulseProfiles.pulse_source_weight
#print axioms Rule30PulseProfiles.heavy_source_two_runs
