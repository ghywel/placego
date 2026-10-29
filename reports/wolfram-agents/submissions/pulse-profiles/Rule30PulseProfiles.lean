/-!
Pulse-profile contribution under development (GC2044).
Core Lean; no imports. This file proves local algebra and the exact interval budget.
Cyclic weight/run count and periodic hole/delay bridge are implemented below; current build status is in README.
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

/-- Periodicity is assumed for the whole temporal profile, not inferred from one seam. -/
def Periodic (q : Nat) (f : Nat → Bool) : Prop := ∀ t, f (q+t) = f t

def pulse (q t : Nat) : Bool := decide (t % q = 0)

def FirstBlack (f : Nat → Bool) (arrival wait : Nat) : Prop :=
  f (arrival+wait) = true ∧ ∀ i, i < wait → f (arrival+i) = false

/-- The exact pulse-child holes within a full cycle, including the closing endpoint q. -/
theorem pulse_child_holes (q l : Nat) (C D : Nat → Bool)
    (hl : 1 ≤ l) (hlq : l < q) (hc : C l = true)
    (hz : ∀ t, 1 ≤ t → t < l → C t = false)
    (hd : D q = D 0)
    (hstep : ∀ t, t < q → D (t+1) = xor (decide (t=0)) (C t || D t)) :
    ∀ t, t ≤ q → D t = decide (t=0 ∨ l<t) := by
  have hln : l ≠ 0 := by omega
  have hinit : D (l+1) = true := by
    simpa [hln, hc] using hstep l hlq
  have black : ∀ n, l+1+n ≤ q → D (l+1+n) = true := by
    intro n
    induction n with
    | zero => intro _; simpa using hinit
    | succ n ih =>
      intro hbound
      have hp := ih (by omega)
      have ht : l+1+n < q := by omega
      have hn : l+1+n ≠ 0 := by omega
      rw [show l+1+(n+1) = (l+1+n)+1 by omega, hstep _ ht]
      simp [hn, hp]
  have hq : D q = true := by
    have h := black (q-(l+1)) (by omega)
    simpa [show l+1+(q-(l+1)) = q by omega] using h
  have h0 : D 0 = true := by rw [← hd]; exact hq
  have h1 : D 1 = false := by simpa [h0] using hstep 0 (by omega)
  have white : ∀ n, n+1 ≤ l → D (n+1) = false := by
    intro n
    induction n with
    | zero => intro _; exact h1
    | succ n ih =>
      intro hbound
      have hp := ih (by omega)
      have ht : n+1 < q := by omega
      have hn : n+1 ≠ 0 := by omega
      have hC := hz (n+1) (by omega) (by omega)
      rw [hstep _ ht]
      simp [hn, hC, hp]
  intro t ht
  by_cases hzero : t=0
  · subst t; simp [h0]
  · by_cases hlow : t ≤ l
    · have h := white (t-1) (by omega)
      have heq : t-1+1 = t := by omega
      rw [heq] at h
      simp [h, hzero, show ¬ l<t by omega]
    · have h := black (t-(l+1)) (by omega)
      have heq : l+1+(t-(l+1)) = t := by omega
      rw [heq] at h
      simp [h, show l<t by omega]

/-- A nonzero phase representative in1..q reaches the pulse at time q. -/
theorem first_pulse (q arrival : Nat) (ha : 1 ≤ arrival) (haq : arrival ≤ q) :
    FirstBlack (pulse q) arrival (q-arrival) := by
  constructor
  · rw [show arrival+(q-arrival) = q by omega]
    simp [pulse]
  · intro i hi
    have ht : arrival+i < q := by omega
    have hn : arrival+i ≠ 0 := by omega
    simp [pulse, Nat.mod_eq_of_lt ht, hn]

/-- The pulse's reset arrival is q+1 for every phase representative. -/
theorem pulse_reset_arrival (q arrival : Nat) (haq : arrival ≤ q) :
    arrival + ((q-arrival)+1) = q+1 := by omega

/-- The next first-black wait is l-1, hence its delay is l. -/
theorem first_child_after_reset (q l : Nat) (C : Nat → Bool)
    (hl : 1 ≤ l) (hc : C l = true)
    (hz : ∀ t, 1 ≤ t → t < l → C t = false) (hp : Periodic q C) :
    FirstBlack C (q+1) (l-1) := by
  constructor
  · have heq : q+1+(l-1) = q+l := by omega
    rw [heq, hp l, hc]
  · intro i hi
    have heq : q+1+i = q+(1+i) := by omega
    rw [heq, hp (1+i)]
    exact hz (1+i) (by omega) (by omega)

/-- On an actual periodic pulse-child trajectory, the last delay is1. -/
theorem first_grandchild_after_child (q l : Nat) (D : Nat → Bool)
    (hl : 1 ≤ l) (hlq : l < q) (hp : Periodic q D)
    (holes : ∀ t, t ≤ q → D t = decide (t=0 ∨ l<t)) :
    FirstBlack D (q+l+1) 0 := by
  constructor
  · have heq : q+l+1+0 = q+(l+1) := by omega
    rw [heq, hp (l+1), holes (l+1) (by omega)]
    simp
  · intro i hi; omega

/-- The cyclic child recurrence is exactly the local recurrence used by the hole theorem. -/
theorem local_step_of_pulse (q : Nat) (C D : Nat → Bool)
    (h : ∀ t, D (t+1) = xor (pulse q t) (C t || D t)) :
    ∀ t, t < q → D (t+1) = xor (decide (t=0)) (C t || D t) := by
  intro t ht
  simpa [pulse, Nat.mod_eq_of_lt ht] using h t

/-- Complete phase-to-delay bridge for one full set of arrival representatives. -/
theorem actual_pulse_delays (q l arrival : Nat) (C D : Nat → Bool)
    (hl : 1 ≤ l) (hlq : l < q) (ha : 1 ≤ arrival) (haq : arrival ≤ q)
    (hc : C l = true) (hz : ∀ t, 1 ≤ t → t < l → C t = false)
    (hpC : Periodic q C) (hpD : Periodic q D)
    (hstep : ∀ t, D (t+1) = xor (pulse q t) (C t || D t)) :
    FirstBlack (pulse q) arrival (q-arrival) ∧
    arrival+((q-arrival)+1) = q+1 ∧
    FirstBlack C (q+1) (l-1) ∧ FirstBlack D (q+l+1) 0 := by
  have hd : D q = D 0 := by simpa using hpD 0
  have holes := pulse_child_holes q l C D hl hlq hc hz hd (local_step_of_pulse q C D hstep)
  exact ⟨first_pulse q arrival ha haq, pulse_reset_arrival q arrival haq,
    first_child_after_reset q l C hl hc hz hpC,
    first_grandchild_after_child q l D hl hlq hpD holes⟩

/-- The budget is now tied to the actual profile first-black events. -/
theorem actual_pulse_window_bound (q l arrival : Nat) (C D : Nat → Bool)
    (hq : 4 ≤ q) (hl : 1 ≤ l) (hlq : l < q) (ha : 1 ≤ arrival) (haq : arrival ≤ q)
    (hc : C l = true) (hz : ∀ t, 1 ≤ t → t < l → C t = false)
    (hpC : Periodic q C) (hpD : Periodic q D)
    (hstep : ∀ t, D (t+1) = xor (pulse q t) (C t || D t)) :
    (FirstBlack (pulse q) arrival (q-arrival) ∧
      arrival+((q-arrival)+1) = q+1 ∧
      FirstBlack C (q+1) (l-1) ∧ FirstBlack D (q+l+1) 0) ∧
    intervalDebt2 ((q-arrival+1 : Nat) : Int) (l : Int) ≤
      2*(q : Int)-5 + max 0 (2*(l : Int)-5) := by
  constructor
  · exact actual_pulse_delays q l arrival C D hl hlq ha haq hc hz hpC hpD hstep
  · apply pulse_window_bound <;> omega

/-- Phase1 is an actual representative and attains the arithmetic upper bound. -/
theorem pulse_window_attained (q l : Nat) (hq : 4 ≤ q) (hlq : l < q) :
    intervalDebt2 ((q-1+1 : Nat) : Int) (l : Int) =
      2*(q : Int)-5 + max 0 (2*(l : Int)-5) := by
  have heq : q-1+1 = q := by omega
  rw [heq]
  apply intervalDebt2_at_pulse <;> omega

end Rule30PulseProfiles

#print axioms Rule30PulseProfiles.source_bit_correction
#print axioms Rule30PulseProfiles.pulse_window_bound
#print axioms Rule30PulseProfiles.leftDiag_step

#print axioms Rule30PulseProfiles.pulse_source_weight
#print axioms Rule30PulseProfiles.heavy_source_two_runs

#print axioms Rule30PulseProfiles.pulse_child_holes
#print axioms Rule30PulseProfiles.actual_pulse_delays

#print axioms Rule30PulseProfiles.actual_pulse_window_bound
