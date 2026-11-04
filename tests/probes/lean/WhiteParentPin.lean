import Std

/-!
White-parent handoff. All indices are wheel indices in the left-wall frame.
The generic certificate works for any deterministic update preserving finite prefix equality.
The numerical CL721 cases and the four candidate continuation files are separate finite inputs.
-/
namespace WhiteParentPin

set_option autoImplicit false
abbrev Row := Nat → Bool

def Agree (w : Nat) (x y : Row) : Prop := ∀ k, k < w → x k = y k
def First (j : Nat) (x y : Row) : Prop := Agree j x y ∧ x j ≠ y j
def Causal (f : Row → Row) : Prop := ∀ {w x y}, Agree w x y → Agree w (f x) (f y)
def Runs (f : Row → Row) (a : Nat → Row) : Prop := ∀ t, a (t+1) = f (a t)

def wall (x : Row) : Row
  | 0 => x 0
  | 1 => x 0 || x 1
  | k+2 => xor (x k) (x (k+1) || x (k+2))

theorem wall_causal : Causal wall := by
  intro w x y h k hk
  match k with
  | 0 => exact h 0 hk
  | 1 => change (x 0 || x 1) = (y 0 || y 1); rw [h 0 (by omega), h 1 hk]
  | k+2 =>
    change xor (x k) (x (k+1) || x (k+2)) = xor (y k) (y (k+1) || y (k+2))
    rw [h k (by omega), h (k+1) (by omega), h (k+2) hk]

theorem propagate {f : Row → Row} (hf : Causal f) {a y : Nat → Row}
    (ha : Runs f a) (hy : Runs f y) {w s t : Nat} (h : Agree w (a s) (y t)) :
    ∀ d, Agree w (a (s+d)) (y (t+d)) := by
  intro d
  induction d with
  | zero => exact h
  | succ d ih =>
    change Agree w (a ((s+d)+1)) (y ((t+d)+1))
    rw [ha, hy]
    exact hf ih

theorem agree_succ {x y : Row} {k : Nat} (h : Agree k x y) (hbit : x k = y k) :
    Agree (k+1) x y := by
  intro i hi
  by_cases he : i = k
  · simpa [he] using hbit
  · exact h i (by omega)

private theorem two_flips {a b c : Bool} (h : a ≠ b) (g : b ≠ c) : a = c := by
  cases a <;> cases b <;> cases c <;> simp_all

private theorem both_flip {a b x y : Bool} (h : a ≠ b) (g : x ≠ y) : (a = x ↔ b = y) := by
  cases a <;> cases b <;> cases x <;> cases y <;> simp_all

/-- Comparing the same lag edge in two histories transports pair equality, bit by bit. -/
theorem four_rows {a b x y : Row} {j k : Nat}
    (h : First j a b) (g : First j x y) (hk : k ≤ j) : a k = x k ↔ b k = y k := by
  by_cases he : k = j
  · subst k; exact both_flip h.2 g.2
  · rw [h.1 k (by omega), g.1 k (by omega)]

/-- An observed self-lag edge cannot move to a lower wheel. -/
theorem edge_mono {f : Row → Row} (hf : Causal f) {a : Nat → Row} (ha : Runs f a)
    {t u p i j : Nat} (htu : t ≤ u) (ht : First i (a t) (a (t+p)))
    (hu : First j (a u) (a (u+p))) : i ≤ j := by
  have h := propagate hf ha ha ht.1 (u-t)
  rw [show t + (u-t) = u by omega, show t+p+(u-t) = u+p by omega] at h
  by_cases he : i ≤ j
  · exact he
  · exact False.elim (hu.2 (h j (by omega)))

private theorem per_iter {a : Nat → Bool} {t p : Nat} (h : ∀ u, t ≤ u → a u = a (u+p)) :
    ∀ n, a t = a (t+n*p) := by
  intro n
  induction n with
  | zero => simp
  | succ n ih =>
    simpa only [Nat.succ_mul,Nat.add_assoc] using ih.trans (h (t+n*p) (by omega))

/-- A finite self-lag edge seen at T and T+p stays at that same wheel forever.
A lag-p edge which eventually moves spends fewer than p consecutive stall steps there. -/
theorem two_hits {f : Row → Row} (hf : Causal f) {a : Nat → Row} (ha : Runs f a)
    {T p j : Nat} (hp : 0 < p)
    (h0 : First j (a T) (a (T+p))) (h1 : First j (a (T+p)) (a (T+p+p))) :
    ∀ u, T ≤ u → First j (a u) (a (u+p)) := by
  have ret : Agree (j+1) (a T) (a (T+p+p)) :=
    agree_succ (fun k hk => (h0.1 k hk).trans (h1.1 k hk)) (two_flips h0.2 h1.2)
  have per (v : Nat) (hv : T ≤ v) : a v j = a (v+(p+p)) j := by
    have g := propagate hf ha ha ret (v-T) j (by omega)
    simpa only [show T+(v-T)=v by omega, show T+p+p+(v-T)=v+(p+p) by omega] using g
  intro u hu
  have low := propagate hf ha ha h0.1 (u-T)
  rw [show T+(u-T)=u by omega, show T+p+(u-T)=u+p by omega] at low
  refine ⟨low, ?_⟩
  intro he
  have join := agree_succ low he
  have reach : u ≤ T+u*(p+p) := by
    have n : 1 ≤ p+p := by omega
    have m := Nat.mul_le_mul_left u n
    simp only [Nat.mul_one] at m
    omega
  let v := T+u*(p+p)
  have g := propagate hf ha ha join (v-u) j (by omega)
  have gu : u+(v-u)=v := by dsimp [v]; omega
  have gp : u+p+(v-u)=v+p := by dsimp [v]; omega
  rw [gu,gp] at g
  have left := per_iter (a := fun z => a z j) (t:=T) (p:=p+p) per u
  have right := per_iter (a := fun z => a z j) (t:=T+p) (p:=p+p)
    (fun z hz => per z (by omega)) u
  apply h0.2
  change a T j = a (T+p) j
  calc
    a T j = a v j := left
    _ = a (v+p) j := g
    _ = a (T+p) j := by simpa [v,Nat.add_assoc,Nat.add_comm,Nat.add_left_comm] using right.symm

/-- Matching lag edges plus a matching terminal prefix transport actual row agreement
back through the transient. Bounds and chronology are explicit. -/
theorem pullback {f : Row → Row} (hf : Causal f) {a y : Nat → Row}
    (ha : Runs f a) (hy : Runs f y) {N T p K : Nat} (hp : 0 < p) (B : Nat → Nat)
    (bound : ∀ t, N ≤ t → B t ≤ K)
    (edges : ∀ t, N ≤ t → First (B t) (a t) (a (t+p)) ∧ First (B t) (y t) (y (t+p)))
    (join : Agree (K+1) (a T) (y T)) :
    ∀ t, N ≤ t → Agree (B t+1) (a t) (y t) := by
  intro t ht k hk
  have trans (n : Nat) : a t k = y t k ↔ a (t+n*p) k = y (t+n*p) k := by
    induction n with
    | zero => simp
    | succ n ih =>
      have he := edges (t+n*p) (by omega)
      have mono := edge_mono hf ha (show t ≤ t+n*p by omega) (edges t ht).1 he.1
      have flip := four_rows he.1 he.2 (show k ≤ B (t+n*p) by omega)
      simpa only [Nat.succ_mul,Nat.add_assoc] using ih.trans flip
  have tr : T ≤ t+T*p := by
    have m := Nat.mul_le_mul_left T (show 1 ≤ p by omega)
    simp only [Nat.mul_one] at m
    omega
  have g := propagate hf ha hy join (t+T*p-T) k (by have := bound t ht; omega)
  rw [show T+(t+T*p-T)=t+T*p by omega] at g
  exact (trans T).mpr g

/-- Combined endpoint-and-transient certificate. The only comparison loop required is
the finite head of the pair's lag-edge history. The future needs two hits and one join. -/
theorem certify {f : Row → Row} (hf : Causal f) {a y : Nat → Row}
    (ha : Runs f a) (hy : Runs f y) {N T p K : Nat} (hp : 0 < p) (B : Nat → Nat)
    (h0 : First K (a T) (a (T+p))) (h1 : First K (a (T+p)) (a (T+p+p)))
    (join : Agree (K+1) (a T) (y T))
    (head : ∀ t, N ≤ t → t < T → First (B t) (a t) (a (t+p)) ∧ First (B t) (y t) (y (t+p))) :
    ∀ t, N ≤ t → ∃ b, First b (a t) (a (t+p)) ∧ First b (y t) (y (t+p)) ∧
      Agree (b+1) (a t) (y t) := by
  let edge := fun t => if t < T then B t else K
  have tail (t : Nat) (ht : T ≤ t) : Agree (K+1) (a t) (y t) := by
    have e := propagate hf ha hy join (t-T)
    simpa only [show T+(t-T)=t by omega] using e
  have both (t : Nat) (hn : N ≤ t) :
      First (edge t) (a t) (a (t+p)) ∧ First (edge t) (y t) (y (t+p)) := by
    by_cases ht : t < T
    · simpa [edge,ht] using head t hn ht
    · have ht' : T ≤ t := by omega
      have aa := two_hits hf ha hp h0 h1 t ht'
      have u := tail t ht'
      have v := tail (t+p) (by omega)
      have yy : First K (y t) (y (t+p)) := by
        constructor
        · intro i hi
          exact (u i (by omega)).symm.trans ((aa.1 i hi).trans (v i (by omega)))
        · intro he
          exact aa.2 ((u K (by omega)).trans (he.trans (v K (by omega)).symm))
      simpa [edge,ht] using And.intro aa yy
  have bd (t : Nat) (hn : N ≤ t) : edge t ≤ K := by
    by_cases ht : t < T
    · exact edge_mono hf ha (by omega) (both t hn).1 h0
    · simp [edge,ht]
  intro t hn
  exact ⟨edge t,(both t hn).1,(both t hn).2,pullback hf ha hy hp edge bd both join t hn⟩

private theorem reset_iff {z u a b : Bool} (hab : a ≠ b) :
    xor z (u || a) = xor z (u || b) ↔ u = true := by
  cases z <;> cases u <;> cases a <;> cases b <;> simp_all

/-- At an actual first difference j=n+1, its old bit heals precisely on a black parent. -/
theorem heals_iff {n : Nat} {x y : Row} (h : First (n+1) x y) :
    wall x (n+1) = wall y (n+1) ↔ x n = true := by
  cases n with
  | zero =>
    change (x 0 || x 1) = (y 0 || y 1) ↔ x 0 = true
    rw [← h.1 0 (by omega)]
    simpa using (reset_iff (z:=false) (u:=x 0) h.2)
  | succ n =>
    change xor (x n) (x (n+1) || x (n+2)) =
      xor (y n) (y (n+1) || y (n+2)) ↔ x (n+1) = true
    rw [← h.1 n (by omega), ← h.1 (n+1) (by omega)]
    exact reset_iff h.2

theorem stays_iff {n : Nat} {x y : Row} (h : First (n+1) x y) :
    First (n+1) (wall x) (wall y) ↔ x n = false := by
  have eqv := heals_iff h
  constructor
  · intro hs
    cases he : x n with
    | false => rfl
    | true => exact False.elim (hs.2 (eqv.mpr he))
  · intro he
    refine ⟨wall_causal h.1, ?_⟩
    intro g
    have bad := eqv.mp g
    simp [he] at bad

/-- With the first difference at n+1 initially, permanent pinning is equivalent
to the single parent staying white on that orbit. The parent histories agree by causality. -/
theorem permanent_pin_iff {a y : Nat → Row} (ha : Runs wall a) (hy : Runs wall y)
    {T n : Nat} (h : First (n+1) (a T) (y T)) :
    (∀ d, First (n+1) (a (T+d)) (y (T+d))) ↔ ∀ d, a (T+d) n = false := by
  constructor
  · intro pins d
    apply (stays_iff (pins d)).mp
    rw [← ha (T+d), ← hy (T+d)]
    exact pins (d+1)
  · intro white d
    induction d with
    | zero => exact h
    | succ d ih =>
      change First (n+1) (a ((T+d)+1)) (y ((T+d)+1))
      rw [ha, hy]
      exact (stays_iff ih).mpr (white d)

/-- First black after m white phases: the rows disagree at the wheel up to and
including T+m, and agree on the entire prefix through that wheel at T+m+1. -/
theorem first_black {a y : Nat → Row} (ha : Runs wall a) (hy : Runs wall y)
    {T n m : Nat} (h : First (n+1) (a T) (y T))
    (white : ∀ d, d < m → a (T+d) n = false) (black : a (T+m) n = true) :
    (∀ d, d ≤ m → First (n+1) (a (T+d)) (y (T+d))) ∧
    Agree (n+2) (a ((T+m)+1)) (y ((T+m)+1)) := by
  have pins (d : Nat) (hd : d ≤ m) : First (n+1) (a (T+d)) (y (T+d)) := by
    induction d with
    | zero => exact h
    | succ d ih =>
      change First (n+1) (a ((T+d)+1)) (y ((T+d)+1))
      rw [ha, hy]
      exact (stays_iff (ih (by omega))).mpr (white d (by omega))
  refine ⟨pins, ?_⟩
  have last := pins m (by omega)
  rw [ha, hy]
  exact agree_succ (wall_causal last.1) ((heals_iff last).mpr black)

#print axioms permanent_pin_iff
#print axioms first_black
#print axioms wall_causal
#print axioms two_hits
#print axioms pullback
#print axioms certify
end WhiteParentPin
