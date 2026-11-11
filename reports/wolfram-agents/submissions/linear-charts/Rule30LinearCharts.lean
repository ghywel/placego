module

public import Ruliology.CellularAutomata.Rule30Prize
public import Ruliology.CellularAutomata.Rule30ZeroBoundary

/-!
# Rule 30: every linear chart of the constrained starts is the free-bit chart

The constrained starts of the zero-boundary left half (`Rule30ZeroBoundary`) form the class
`KK L := L 0 = false ∧ InX L`, and two steps of the zero-boundary rule, `zrow · 2`, act on it.
`Theta` and the free-bit read-off `fb L s := zrow L (2 * s + 1) 1` are inverse bijections between
all sequences `Nat → Bool` and `KK` (`kk_Theta`, `fb_Theta`, `Theta_fb`), both uniformly finitely
dependent (`uld_Theta`, `uld_fb`), and they turn two steps into the one-sided shift
(`kk_two_step`, `fb_shift`, and `two_step_shift`).

**The theorem.** Let `A` be a set of sequences closed under `a + b + c`, where `+` is pointwise
xor (`xr`): an affine subspace of the sequences over the two-element field. Let `Lm` be affine on
`A`, and let `Φ`, `Φ'` be mutually inverse maps between `KK` and `A`, both uniformly finitely
dependent, with `Φ (zrow L 2) = Lm (Φ L)` on `KK`. Then `Ψ := Φ ∘ Theta` is affine:
`Ψ (f + g + h) = Ψ f + Ψ g + Ψ h` (`linear_chart_is_free_bit_chart`, and `free_bit_chart_affine`
for `Ψ (f + g) = Ψ f + Ψ g + Ψ 0`). By `free_bit_chart_iso`, `Ψ` is a bijection from all sequences
onto `A`, uniformly finitely dependent in both directions; `free_bit_chart_is_chart` checks that
the hypotheses are met by the free-bit chart itself. In words: every linear chart of the
constrained class, that is every way of reading it as an affine space on which the two-step
dynamics acts affinely, is the free-bit chart followed by an affine bijection.

**Continuity.** Continuity is represented as uniform finite dependence (`ULD`): each output bit is
determined by a fixed finite window of the input, the same window for every input in the domain.
On a compact domain of the product space this is equivalent to continuity, since a continuous map
on a compact space is uniformly continuous; that equivalence is not formalized here. Closedness of
`A` and continuity of `Lm` are not needed.

**The route.** Pull the affine structure of `A` back to the free bits:
`x ⊕ y := Ψ' (Ψ x + Ψ y + Ψ 0)` with `Ψ' := fb ∘ Φ'` (`chartLaw`). This operation is commutative,
has the white sequence as neutral element, satisfies `(x ⊕ y) ⊕ y = x`, commutes with the shift,
and has bit `0` determined by a finite window (`IsChart.law`, `IsChart.window`). The group-law
lemma `groupLaw_eq_xor` says that every such operation on one-sided sequences is pointwise xor:
* `fibre_form`: bit `n` of `x ⊕ y` is `x n + y n + Q (tails)`, where the correction term `Q`
  (`qOf`) is bit `0` of the law on two sequences that start white. One-sidedness enters here:
  changing bit `0` of `x` keeps the shifted law, so it changes bit `0` of `x ⊕ y` and nothing else.
* `involution_Q`: `Q u w = Q (u ⊕ w) w`, read off bit `0` of `(x ⊕ y) ⊕ y = x`.
* `descent_step`: if `Q` reads only coordinates below `r + 1`, it reads only coordinates below
  `r`. If `Q` were sensitive to coordinate `r` of `u` in a context `(p, q)`, take `w` agreeing with
  `q` below `r + 1` with `r + 1`-fold shift `q`, and `u` with `r + 1`-fold shift `p` and
  `u ⊕ w` agreeing with `p` below `r + 1` (`u := v ⊕ w` for a suitable `v`); flipping bit `2 r + 1`
  of `u` keeps `Q u w` but flips coordinate `r` of `u ⊕ w` and nothing below it, so it changes
  `Q (u ⊕ w) w`, against `involution_Q`. `window_zero`: descending to window `0`, `Q` is constant,
  equal to `Q u 0 = 0` (`q_white`). Only this last step uses the neutral element.

**Prior work.** The automorphism theorem for the one-sided full 2-shift (its only automorphisms
are the identity and the bit flip) is due to Hedlund (1969). The group-law lemma is probably known
in the theory of one-sided group shifts; it is not claimed as new.

Nothing here decides `Q01` or the period-2 question.
-/

@[expose] public section

namespace Ruliology.CellularAutomata
namespace Rule30LinearCharts

open Rule30ZeroBoundary

/-! ### Sequences -/

/-- Pointwise xor of two sequences: addition over the two-element field. -/
def xr (a b : Nat → Bool) : Nat → Bool := fun k => xor (a k) (b k)

/-- The sequence that starts with `b` and continues with `u`. -/
def prep (b : Bool) (u : Nat → Bool) : Nat → Bool
  | 0 => b
  | k + 1 => u k

/-- The shift by `n` places. -/
def shn (n : Nat) (x : Nat → Bool) : Nat → Bool := fun k => x (n + k)

/-- The sequence `p` with bit `r` flipped. -/
def flipAt (p : Nat → Bool) (r : Nat) : Nat → Bool := fun i => if i = r then !p i else p i

theorem flipAt_ne {p : Nat → Bool} {r i : Nat} (h : i ≠ r) : flipAt p r i = p i := ite_eq_right h

theorem flipAt_self (p : Nat → Bool) (r : Nat) : flipAt p r r = !p r := ite_eq_left rfl

theorem prep_white : prep false (fun _ => false) = (fun _ => false) := by
  funext k; cases k <;> rfl

theorem shn_zero (x : Nat → Bool) : shn 0 x = x := by
  funext k; show x (0 + k) = x k; rw [Nat.zero_add]

theorem shn_succ (n : Nat) (x : Nat → Bool) : shn (n + 1) x = fun k => shn n x (k + 1) := by
  funext k; show x (n + 1 + k) = x (n + (k + 1)); exact congrArg x (by omega)

theorem xr_comm (a b : Nat → Bool) : xr a b = xr b a := by
  funext k; exact Bool.xor_comm (a k) (b k)

theorem xr_cancel (a b : Nat → Bool) : xr (xr a b) b = a := by
  funext k; show xor (xor (a k) (b k)) (b k) = a k
  cases a k <;> cases b k <;> rfl

theorem xr_cancel_two (a b z : Nat → Bool) : xr (xr (xr (xr a b) z) b) z = a := by
  funext k; show xor (xor (xor (xor (a k) (b k)) (z k)) (b k)) (z k) = a k
  cases a k <;> cases b k <;> cases z k <;> rfl

theorem xr_three (a b c z : Nat → Bool) : xr (xr (xr (xr a b) z) c) z = xr (xr a b) c := by
  funext k; show xor (xor (xor (xor (a k) (b k)) (z k)) (c k)) (z k) = xor (xor (a k) (b k)) (c k)
  cases a k <;> cases b k <;> cases c k <;> cases z k <;> rfl

/-! ### The group-law lemma -/

/-- The algebraic hypotheses on a binary operation on one-sided sequences: it is commutative, each
element is its own inverse, and the shift is an endomorphism. -/
structure Law (op : (Nat → Bool) → (Nat → Bool) → Nat → Bool) : Prop where
  comm : ∀ x y, op x y = op y x
  inv : ∀ x y, op (op x y) y = x
  shift : ∀ x y, (fun n => op x y (n + 1)) = op (fun n => x (n + 1)) (fun n => y (n + 1))

/-- The correction term of a law: bit `0` of the law on two sequences that start white. -/
def qOf (op : (Nat → Bool) → (Nat → Bool) → Nat → Bool) (u w : Nat → Bool) : Bool :=
  op (prep false u) (prep false w) 0

/-- The correction term reads only coordinates below `r` of each argument. -/
def Win (op : (Nat → Bool) → (Nat → Bool) → Nat → Bool) (r : Nat) : Prop :=
  ∀ u w u' w' : Nat → Bool, (∀ i, i < r → u i = u' i ∧ w i = w' i) → qOf op u w = qOf op u' w'

section GroupLaw

variable {op : (Nat → Bool) → (Nat → Bool) → Nat → Bool}

/-- The `n`-fold shift is an endomorphism. -/
theorem Law.shn_eq (h : Law op) (n : Nat) : ∀ x y, shn n (op x y) = op (shn n x) (shn n y) := by
  induction n with
  | zero => intro x y; rw [shn_zero, shn_zero, shn_zero]
  | succ n ih =>
    intro x y
    rw [shn_succ, shn_succ, shn_succ, ih x y, h.shift (shn n x) (shn n y)]

/-- Changing bit `0` of `x` changes bit `0` of `op x y` and nothing else. -/
theorem Law.bit0 (h : Law op) (x x' y : Nat → Bool) (hx : ∀ k, x (k + 1) = x' (k + 1)) :
    xor (op x y 0) (op x' y 0) = xor (x 0) (x' 0) := by
  have hs : (fun n => x (n + 1)) = (fun n => x' (n + 1)) := funext hx
  have htail : ∀ k, op x y (k + 1) = op x' y (k + 1) := by
    intro k
    have h1 : op x y (k + 1) = op (fun n => x (n + 1)) (fun n => y (n + 1)) k :=
      congrFun (h.shift x y) k
    have h2 : op x' y (k + 1) = op (fun n => x' (n + 1)) (fun n => y (n + 1)) k :=
      congrFun (h.shift x' y) k
    rw [h1, h2]
    exact congrArg (fun z => op z (fun n => y (n + 1)) k) hs
  by_cases h0 : x 0 = x' 0
  · have hxx : x = x' := funext fun k => by
      cases k with
      | zero => exact h0
      | succ k => exact hx k
    rw [hxx, Bool.xor_self, Bool.xor_self]
  · have hne : op x y 0 ≠ op x' y 0 := by
      intro e
      apply h0
      have hall : op x y = op x' y := funext fun k => by
        cases k with
        | zero => exact e
        | succ k => exact htail k
      rw [← h.inv x y, hall, h.inv]
    revert h0 hne
    cases x 0 <;> cases x' 0 <;> cases op x y 0 <;> cases op x' y 0 <;> decide

/-- Bit `0` of the law: `x 0 + y 0` plus the correction term of the tails. -/
theorem Law.bit0_form (h : Law op) (x y : Nat → Bool) :
    op x y 0 = xor (xor (x 0) (y 0)) (qOf op (fun k => x (k + 1)) (fun k => y (k + 1))) := by
  have e1 : xor (op x y 0) (op (prep false (fun k => x (k + 1))) y 0) = x 0 :=
    (h.bit0 x (prep false (fun k => x (k + 1))) y fun _ => rfl).trans (Bool.xor_false (x 0))
  have e2 : xor (op (prep false (fun k => x (k + 1))) y 0)
      (op (prep false (fun k => x (k + 1))) (prep false (fun k => y (k + 1))) 0) = y 0 := by
    rw [h.comm (prep false (fun k => x (k + 1))) y,
      h.comm (prep false (fun k => x (k + 1))) (prep false (fun k => y (k + 1)))]
    exact (h.bit0 y (prep false (fun k => y (k + 1))) (prep false (fun k => x (k + 1)))
      fun _ => rfl).trans (Bool.xor_false (y 0))
  show op x y 0 = xor (xor (x 0) (y 0))
    (op (prep false (fun k => x (k + 1))) (prep false (fun k => y (k + 1))) 0)
  rw [← e1, ← e2]
  cases op x y 0 <;> cases op (prep false (fun k => x (k + 1))) y 0 <;>
    cases op (prep false (fun k => x (k + 1))) (prep false (fun k => y (k + 1))) 0 <;> rfl

/-- The law on two prefixed sequences. -/
theorem Law.op_prep (h : Law op) (a b : Bool) (u w : Nat → Bool) :
    op (prep a u) (prep b w) = prep (xor (xor a b) (qOf op u w)) (op u w) := by
  funext k
  cases k with
  | zero => exact h.bit0_form (prep a u) (prep b w)
  | succ k => exact congrFun (h.shift (prep a u) (prep b w)) k

/-- **The fibre form.** Bit `n` of the law is `x n + y n` plus the correction term of the tails
after position `n`. -/
theorem fibre_form (h : Law op) (x y : Nat → Bool) (n : Nat) :
    op x y n = xor (xor (x n) (y n)) (qOf op (shn (n + 1) x) (shn (n + 1) y)) := by
  have e : op x y n = op (shn n x) (shn n y) 0 := congrFun (h.shn_eq n x y) 0
  rw [e, h.bit0_form, shn_succ n x, shn_succ n y]
  rfl

/-- The correction term is symmetric. -/
theorem q_symm (h : Law op) (u w : Nat → Bool) : qOf op u w = qOf op w u := by
  unfold qOf; rw [h.comm]

/-- The correction term vanishes against the white sequence. -/
theorem q_white (hid : ∀ x, op x (fun _ => false) = x) (u : Nat → Bool) :
    qOf op u (fun _ => false) = false := by
  have e : op (prep false u) (prep false (fun _ => false)) = prep false u := by
    rw [prep_white, hid]
  exact congrFun e 0

/-- **The involution identity** `Q u w = Q (u ⊕ w) w`. -/
theorem involution_Q (h : Law op) (u w : Nat → Bool) : qOf op u w = qOf op (op u w) w := by
  have e := congrFun (h.inv (prep false u) (prep false w)) 0
  rw [h.op_prep, h.op_prep] at e
  have e' : xor (xor (xor (xor false false) (qOf op u w)) false) (qOf op (op u w) w) = false := e
  revert e'
  cases qOf op u w <;> cases qOf op (op u w) w <;> decide

/-- Two sequences with prescribed first `r + 1` bits and prescribed `r + 1`-fold shift. -/
theorem splice (a b : Nat → Bool) (r : Nat) :
    ∃ c : Nat → Bool, (∀ i, i ≤ r → c i = a i) ∧ shn (r + 1) c = b := by
  refine ⟨fun i => if i ≤ r then a i else b (i - (r + 1)), fun i hi => ite_eq_left hi, ?_⟩
  funext j
  show (if r + 1 + j ≤ r then a (r + 1 + j) else b (r + 1 + j - (r + 1))) = b j
  rw [ite_eq_right (by omega), show r + 1 + j - (r + 1) = j by omega]

/-- **The key step.** If the correction term reads only coordinates below `r + 1`, flipping
coordinate `r` of its first argument does not change it. -/
theorem flip_invariant (h : Law op) (r : Nat) (hr : Win op (r + 1)) (p q : Nat → Bool) :
    qOf op p q = qOf op (flipAt p r) q := by
  by_cases hpq : qOf op p q = qOf op (flipAt p r) q
  · exact hpq
  · exfalso
    obtain ⟨w, hwlo, hw⟩ := splice q q r
    obtain ⟨v, hvlo, hv⟩ := splice p (op p q) r
    have hu : shn (r + 1) (op v w) = p := by rw [h.shn_eq, hv, hw, h.inv]
    have huv : op (op v w) w = v := h.inv v w
    generalize op v w = u at hu huv
    -- `u` has shift `p`, and `op u w = v` agrees with `p` below `r + 1`.
    have hu'sh : shn (r + 1) (flipAt u (2 * r + 1)) = flipAt p r := by
      funext j
      show (if r + 1 + j = 2 * r + 1 then !u (r + 1 + j) else u (r + 1 + j)) =
        (if j = r then !p j else p j)
      rw [show u (r + 1 + j) = p j from congrFun hu j]
      by_cases hj : j = r
      · rw [ite_eq_left (by omega), ite_eq_left hj]
      · rw [ite_eq_right (by omega), ite_eq_right hj]
    -- Flipping bit `2 r + 1` of `u` does not change `Q u w`.
    have e1 : qOf op (flipAt u (2 * r + 1)) w = qOf op u w :=
      hr _ _ _ _ fun i hi => ⟨flipAt_ne (by omega), rfl⟩
    have e2 : qOf op u w = qOf op v w := by rw [involution_Q h u w, huv]
    have e4 : qOf op v w = qOf op p q :=
      hr _ _ _ _ fun i hi => ⟨hvlo i (by omega), hwlo i (by omega)⟩
    -- It does not change the bits of `op u w` below `r` ...
    have hlow : ∀ i, i < r → op (flipAt u (2 * r + 1)) w i = op u w i := by
      intro i hi
      rw [fibre_form h (flipAt u (2 * r + 1)) w i, fibre_form h u w i,
        flipAt_ne (show i ≠ 2 * r + 1 by omega),
        hr (shn (i + 1) (flipAt u (2 * r + 1))) (shn (i + 1) w) (shn (i + 1) u) (shn (i + 1) w)
          fun j hj => ⟨flipAt_ne (by omega), rfl⟩]
    -- ... but it flips bit `r`, since `Q` is sensitive there.
    have hbit : op (flipAt u (2 * r + 1)) w r = !(op u w r) := by
      rw [fibre_form h (flipAt u (2 * r + 1)) w r, fibre_form h u w r,
        flipAt_ne (show r ≠ 2 * r + 1 by omega), hu'sh, hu, hw]
      revert hpq
      cases u r <;> cases w r <;> cases qOf op p q <;> cases qOf op (flipAt p r) q <;> decide
    have e5 : qOf op (op (flipAt u (2 * r + 1)) w) w = qOf op (flipAt p r) q := by
      refine hr _ _ _ _ fun i hi => ⟨?_, hwlo i (by omega)⟩
      by_cases hir : i = r
      · rw [hir, hbit, flipAt_self, huv, hvlo r (Nat.le_refl r)]
      · rw [hlow i (by omega), flipAt_ne hir, huv, hvlo i (by omega)]
    exact hpq (e4.symm.trans (e2.symm.trans (e1.symm.trans ((involution_Q h _ w).trans e5))))

/-- **Descent.** A window of `r + 1` coordinates shrinks to a window of `r` coordinates. -/
theorem descent_step (h : Law op) (r : Nat) (hr : Win op (r + 1)) : Win op r := by
  have hleft : ∀ u u' w, (∀ i, i < r → u i = u' i) → qOf op u w = qOf op u' w := by
    intro u u' w hlt
    by_cases hb : u r = u' r
    · refine hr _ _ _ _ fun i hi => ⟨?_, rfl⟩
      by_cases hir : i = r
      · rw [hir]; exact hb
      · exact hlt i (by omega)
    · rw [flip_invariant h r hr u w]
      refine hr _ _ _ _ fun i hi => ⟨?_, rfl⟩
      by_cases hir : i = r
      · rw [hir, flipAt_self]; revert hb; cases u r <;> cases u' r <;> decide
      · rw [flipAt_ne hir]; exact hlt i (by omega)
  intro u w u' w' hlt
  rw [hleft u u' w fun i hi => (hlt i hi).1, q_symm h, hleft w w' u' fun i hi => (hlt i hi).2,
    q_symm h]

/-- Descending from any window to the empty window. -/
theorem window_zero (h : Law op) : ∀ n, Win op n → Win op 0 := by
  intro n
  induction n with
  | zero => exact id
  | succ n ih => exact fun hn => ih (descent_step h n hn)

/-- A finite window for bit `0` of the law gives a finite window for the correction term. -/
theorem win_of_window
    (hwin : ∃ R, ∀ x y x' y', (∀ i, i < R → x i = x' i ∧ y i = y' i) → op x y 0 = op x' y' 0) :
    ∃ R, Win op R := by
  obtain ⟨R, hR⟩ := hwin
  refine ⟨R, fun u w u' w' hu => hR _ _ _ _ fun i hi => ?_⟩
  cases i with
  | zero => exact ⟨rfl, rfl⟩
  | succ i => exact hu i (by omega)

end GroupLaw

/-- **The group-law lemma.** A commutative operation on one-sided sequences with neutral element
white, in which every element is its own inverse, which commutes with the shift and has bit `0`
determined by a finite window, is pointwise xor. -/
theorem groupLaw_eq_xor (op : (Nat → Bool) → (Nat → Bool) → Nat → Bool)
    (hid : ∀ x, op x (fun _ => false) = x) (hcomm : ∀ x y, op x y = op y x)
    (hinv : ∀ x y, op (op x y) y = x)
    (hsh : ∀ x y, (fun n => op x y (n + 1)) = op (fun n => x (n + 1)) (fun n => y (n + 1)))
    (hwin : ∃ R, ∀ x y x' y', (∀ i, i < R → x i = x' i ∧ y i = y' i) → op x y 0 = op x' y' 0) :
    ∀ x y, op x y = xr x y := by
  have h : Law op := ⟨hcomm, hinv, hsh⟩
  obtain ⟨R, hR⟩ := win_of_window hwin
  have h0 := window_zero h R hR
  have hq : ∀ u w, qOf op u w = false := fun u w =>
    (h0 u w u (fun _ => false) fun i hi => absurd hi (Nat.not_lt_zero i)).trans (q_white hid u)
  intro x y
  funext n
  show op x y n = xor (x n) (y n)
  rw [fibre_form h x y n, hq, Bool.xor_false]

/-! ### The constrained starts -/

/-- The constrained class: white wall, and column `-1` black at every even step. -/
def KK (L : Nat → Bool) : Prop := L 0 = false ∧ InX L

/-- The free bits of a start: column `-1` at the odd steps. -/
def fb (L : Nat → Bool) (s : Nat) : Bool := zrow L (2 * s + 1) 1

theorem kk_Theta (f : Nat → Bool) : KK (Theta f) := ⟨Theta_wall f, Theta_inX f⟩

/-- Reading off the free bits inverts `Theta`. -/
theorem fb_Theta (f : Nat → Bool) : fb (Theta f) = f := funext (Theta_free f)

/-- `Theta` inverts the free-bit read-off on the constrained class. -/
theorem Theta_fb {L : Nat → Bool} (hL : KK L) : Theta (fb L) = L :=
  (Theta_unique (f := fb L) hL.2 fun _ => rfl).symm.trans (zrow_zero_self hL.1)

/-- Two steps preserve the constrained class. -/
theorem kk_two_step {L : Nat → Bool} (hL : KK L) : KK (zrow L 2) := by
  refine ⟨zrow_wall L 2, fun s => ?_⟩
  rw [← zrow_shift, show 2 + 2 * s = 2 * (s + 1) by omega]
  exact hL.2 (s + 1)

/-- Two steps shift the free bits. -/
theorem fb_shift (L : Nat → Bool) : fb (zrow L 2) = fun s => fb L (s + 1) := by
  funext s
  show zrow (zrow L 2) (2 * s + 1) 1 = zrow L (2 * (s + 1) + 1) 1
  rw [← zrow_shift, show 2 + (2 * s + 1) = 2 * (s + 1) + 1 by omega]

/-! ### Uniform finite dependence -/

/-- **Uniform finite dependence** on a domain `D`: each output bit is determined by a fixed finite
window of the input, the same window for every input in `D`. On a compact `D` this is continuity
in the product topology (not formalized here). -/
def ULD (D : (Nat → Bool) → Prop) (f : (Nat → Bool) → Nat → Bool) : Prop :=
  ∀ k, ∃ N, ∀ x y, D x → D y → (∀ i, i < N → x i = y i) → f x k = f y k

theorem uld_Theta : ULD (fun _ => True) Theta := fun k =>
  ⟨k, fun f g _ _ h => Theta_dep f g k fun s hs => h s (by omega)⟩

theorem uld_fb : ULD (fun _ => True) fb := fun s =>
  ⟨2 * s + 3, fun _ _ _ _ h => zrow_light_cone (2 * s + 1) 1 fun i _ hi => h i (by omega)⟩

/-- Finitely many windows have a common bound. -/
theorem bound_below (P : Nat → Nat → Prop) (hmono : ∀ i M M', M ≤ M' → P i M → P i M')
    (h : ∀ i, ∃ M, P i M) : ∀ N, ∃ M, ∀ i, i < N → P i M := by
  intro N
  induction N with
  | zero => exact ⟨0, fun i hi => absurd hi (Nat.not_lt_zero i)⟩
  | succ N ih =>
    obtain ⟨M1, h1⟩ := ih
    obtain ⟨M2, h2⟩ := h N
    refine ⟨M1 + M2, fun i hi => ?_⟩
    by_cases hiN : i < N
    · exact hmono i M1 _ (Nat.le_add_right _ _) (h1 i hiN)
    · rw [show i = N by omega]; exact hmono N M2 _ (Nat.le_add_left _ _) h2

theorem uld_comp {D E : (Nat → Bool) → Prop} {f g : (Nat → Bool) → Nat → Bool}
    (hf : ULD D f) (hg : ULD E g) (hfE : ∀ x, D x → E (f x)) : ULD D (fun x => g (f x)) := by
  intro k
  obtain ⟨N, hN⟩ := hg k
  obtain ⟨M, hM⟩ := bound_below
    (fun i M => ∀ x y : Nat → Bool, D x → D y → (∀ j, j < M → x j = y j) → f x i = f y i)
    (by
      intro _ _ _ hle hP x y hx hy hxy
      exact hP x y hx hy fun j hj => hxy j (by omega)) hf N
  exact ⟨M, fun x y hx hy hxy => hN _ _ (hfE x hx) (hfE y hy) fun i hi => hM i hi x y hx hy hxy⟩

/-! ### Transport of a linear chart to the free bits -/

/-- The hypotheses of a linear chart of the constrained class: `A` is affine, `Lm` is affine on
`A`, `Φ` and `Φ'` are mutually inverse between `KK` and `A`, uniformly finitely dependent, and
`Φ` conjugates two steps to `Lm`. -/
structure IsChart (A : (Nat → Bool) → Prop) (Lm Φ Φ' : (Nat → Bool) → Nat → Bool) : Prop where
  affA : ∀ a b c, A a → A b → A c → A (xr (xr a b) c)
  affL : ∀ a b c, A a → A b → A c → Lm (xr (xr a b) c) = xr (xr (Lm a) (Lm b)) (Lm c)
  mapsTo : ∀ L, KK L → A (Φ L)
  mapsTo' : ∀ a, A a → KK (Φ' a)
  left_inv : ∀ L, KK L → Φ' (Φ L) = L
  right_inv : ∀ a, A a → Φ (Φ' a) = a
  conj : ∀ L, KK L → Φ (zrow L 2) = Lm (Φ L)
  cont : ULD KK Φ
  cont' : ULD A Φ'

/-- The law that a chart induces on the free bits: `x ⊕ y := Ψ' (Ψ x + Ψ y + Ψ 0)`. -/
def chartLaw (Φ Φ' : (Nat → Bool) → Nat → Bool) (x y : Nat → Bool) : Nat → Bool :=
  fb (Φ' (xr (xr (Φ (Theta x)) (Φ (Theta y))) (Φ (Theta (fun _ => false)))))

section Chart

variable {A : (Nat → Bool) → Prop} {Lm Φ Φ' : (Nat → Bool) → Nat → Bool}

theorem IsChart.psi_mem (c : IsChart A Lm Φ Φ') (x : Nat → Bool) : A (Φ (Theta x)) :=
  c.mapsTo _ (kk_Theta x)

theorem IsChart.inv_psi (c : IsChart A Lm Φ Φ') (x : Nat → Bool) : fb (Φ' (Φ (Theta x))) = x := by
  rw [c.left_inv _ (kk_Theta x), fb_Theta]

theorem IsChart.psi_inv (c : IsChart A Lm Φ Φ') {a : Nat → Bool} (ha : A a) :
    Φ (Theta (fb (Φ' a))) = a := by
  rw [Theta_fb (c.mapsTo' a ha), c.right_inv a ha]

theorem IsChart.psi_shift (c : IsChart A Lm Φ Φ') (x : Nat → Bool) :
    Φ (Theta (fun n => x (n + 1))) = Lm (Φ (Theta x)) := by
  rw [← two_step_shift x, c.conj _ (kk_Theta x)]

theorem IsChart.lm_white (c : IsChart A Lm Φ Φ') :
    Lm (Φ (Theta (fun _ => false))) = Φ (Theta (fun _ => false)) :=
  (c.psi_shift (fun _ => false)).symm

theorem IsChart.inv_shift (c : IsChart A Lm Φ Φ') {a : Nat → Bool} (ha : A a) :
    (fun n => fb (Φ' a) (n + 1)) = fb (Φ' (Lm a)) := by
  have hK := c.mapsTo' a ha
  have e : Lm a = Φ (zrow (Φ' a) 2) := by rw [c.conj _ hK, c.right_inv a ha]
  rw [e, c.left_inv _ (kk_two_step hK), fb_shift]

theorem IsChart.sum_mem (c : IsChart A Lm Φ Φ') (x y : Nat → Bool) :
    A (xr (xr (Φ (Theta x)) (Φ (Theta y))) (Φ (Theta (fun _ => false)))) :=
  c.affA _ _ _ (c.psi_mem x) (c.psi_mem y) (c.psi_mem _)

theorem IsChart.ident (c : IsChart A Lm Φ Φ') (x : Nat → Bool) :
    chartLaw Φ Φ' x (fun _ => false) = x := by
  unfold chartLaw
  rw [xr_cancel, c.inv_psi]

/-- The induced law satisfies the algebraic hypotheses of the group-law lemma. -/
theorem IsChart.law (c : IsChart A Lm Φ Φ') : Law (chartLaw Φ Φ') where
  comm x y := by
    unfold chartLaw
    rw [xr_comm (Φ (Theta x))]
  inv x y := by
    unfold chartLaw
    rw [c.psi_inv (c.sum_mem x y), xr_cancel_two, c.inv_psi]
  shift x y := by
    unfold chartLaw
    rw [c.inv_shift (c.sum_mem x y),
      c.affL _ _ _ (c.psi_mem x) (c.psi_mem y) (c.psi_mem (fun _ => false)),
      ← c.psi_shift x, ← c.psi_shift y, c.lm_white]

/-- Bit `0` of the induced law is determined by a finite window. -/
theorem IsChart.window (c : IsChart A Lm Φ Φ') :
    ∃ R, ∀ x y x' y', (∀ i, i < R → x i = x' i ∧ y i = y' i) →
      chartLaw Φ Φ' x y 0 = chartLaw Φ Φ' x' y' 0 := by
  obtain ⟨N, hN⟩ := uld_comp c.cont' uld_fb (fun _ _ => trivial) 0
  have hpsi := uld_comp uld_Theta c.cont (fun x _ => kk_Theta x)
  obtain ⟨M, hM⟩ := bound_below
    (fun i M => ∀ x y : Nat → Bool, True → True → (∀ j, j < M → x j = y j) →
      Φ (Theta x) i = Φ (Theta y) i)
    (by
      intro _ _ _ hle hP x y hx hy hxy
      exact hP x y hx hy fun j hj => hxy j (by omega)) hpsi N
  refine ⟨M, fun x y x' y' hxy => ?_⟩
  unfold chartLaw
  refine hN _ _ (c.sum_mem x y) (c.sum_mem x' y') fun i hi => ?_
  have e1 : Φ (Theta x) i = Φ (Theta x') i := hM i hi x x' trivial trivial fun j hj => (hxy j hj).1
  have e2 : Φ (Theta y) i = Φ (Theta y') i := hM i hi y y' trivial trivial fun j hj => (hxy j hj).2
  simp only [xr]
  rw [e1, e2]

/-- The chart is affine in the two-argument form. -/
theorem IsChart.affine (c : IsChart A Lm Φ Φ') (x y : Nat → Bool) :
    Φ (Theta (xr x y)) = xr (xr (Φ (Theta x)) (Φ (Theta y))) (Φ (Theta (fun _ => false))) := by
  have e := groupLaw_eq_xor (chartLaw Φ Φ') c.ident c.law.comm c.law.inv c.law.shift c.window x y
  rw [← e]
  unfold chartLaw
  exact c.psi_inv (c.sum_mem x y)

end Chart

/-- **Every linear chart of the constrained class is the free-bit chart, up to an affine map.**
Let `A` be closed under `a + b + c`, let `Lm` be affine on `A`, and let `Φ`, `Φ'` be mutually
inverse between the constrained class `KK` and `A`, uniformly finitely dependent, with
`Φ ∘ (two steps) = Lm ∘ Φ` on `KK`. Then `Φ ∘ Theta` is affine. -/
theorem linear_chart_is_free_bit_chart (A : (Nat → Bool) → Prop)
    (hA : ∀ a b c, A a → A b → A c → A (xr (xr a b) c))
    (Lm : (Nat → Bool) → Nat → Bool)
    (hLm : ∀ a b c, A a → A b → A c → Lm (xr (xr a b) c) = xr (xr (Lm a) (Lm b)) (Lm c))
    (Φ Φ' : (Nat → Bool) → Nat → Bool)
    (hΦ : ∀ L, KK L → A (Φ L)) (hΦ' : ∀ a, A a → KK (Φ' a))
    (hΦ'Φ : ∀ L, KK L → Φ' (Φ L) = L) (hΦΦ' : ∀ a, A a → Φ (Φ' a) = a)
    (hconj : ∀ L, KK L → Φ (zrow L 2) = Lm (Φ L))
    (hcont : ULD KK Φ) (hcont' : ULD A Φ') :
    ∀ f g h, Φ (Theta (xr (xr f g) h)) = xr (xr (Φ (Theta f)) (Φ (Theta g))) (Φ (Theta h)) := by
  have c : IsChart A Lm Φ Φ' := ⟨hA, hLm, hΦ, hΦ', hΦ'Φ, hΦΦ', hconj, hcont, hcont'⟩
  intro f g h
  rw [c.affine (xr f g) h, c.affine f g, xr_three]

/-- The two-argument form: `Ψ (f + g) = Ψ f + Ψ g + Ψ 0` for `Ψ = Φ ∘ Theta`. -/
theorem free_bit_chart_affine (A : (Nat → Bool) → Prop)
    (hA : ∀ a b c, A a → A b → A c → A (xr (xr a b) c))
    (Lm : (Nat → Bool) → Nat → Bool)
    (hLm : ∀ a b c, A a → A b → A c → Lm (xr (xr a b) c) = xr (xr (Lm a) (Lm b)) (Lm c))
    (Φ Φ' : (Nat → Bool) → Nat → Bool)
    (hΦ : ∀ L, KK L → A (Φ L)) (hΦ' : ∀ a, A a → KK (Φ' a))
    (hΦ'Φ : ∀ L, KK L → Φ' (Φ L) = L) (hΦΦ' : ∀ a, A a → Φ (Φ' a) = a)
    (hconj : ∀ L, KK L → Φ (zrow L 2) = Lm (Φ L))
    (hcont : ULD KK Φ) (hcont' : ULD A Φ') :
    ∀ f g, Φ (Theta (xr f g)) = xr (xr (Φ (Theta f)) (Φ (Theta g))) (Φ (Theta (fun _ => false))) :=
  (IsChart.mk hA hLm hΦ hΦ' hΦ'Φ hΦΦ' hconj hcont hcont').affine

/-- `Ψ = Φ ∘ Theta` is a bijection from all sequences onto `A`, with inverse `fb ∘ Φ'`, and both
are uniformly finitely dependent. -/
theorem free_bit_chart_iso (A : (Nat → Bool) → Prop) (Φ Φ' : (Nat → Bool) → Nat → Bool)
    (hΦ : ∀ L, KK L → A (Φ L)) (hΦ' : ∀ a, A a → KK (Φ' a))
    (hΦ'Φ : ∀ L, KK L → Φ' (Φ L) = L) (hΦΦ' : ∀ a, A a → Φ (Φ' a) = a)
    (hcont : ULD KK Φ) (hcont' : ULD A Φ') :
    (∀ f, A (Φ (Theta f))) ∧ (∀ f, fb (Φ' (Φ (Theta f))) = f) ∧
      (∀ a, A a → Φ (Theta (fb (Φ' a))) = a) ∧
      ULD (fun _ => True) (fun f => Φ (Theta f)) ∧ ULD A (fun a => fb (Φ' a)) := by
  refine ⟨fun f => hΦ _ (kk_Theta f), fun f => ?_, fun a ha => ?_,
    uld_comp uld_Theta hcont (fun x _ => kk_Theta x), uld_comp hcont' uld_fb (fun _ _ => trivial)⟩
  · rw [hΦ'Φ _ (kk_Theta f), fb_Theta]
  · rw [Theta_fb (hΦ' a ha), hΦΦ' a ha]

/-- Uniform finite dependence on a domain passes to every smaller domain. -/
theorem uld_mono {D E : (Nat → Bool) → Prop} {f : (Nat → Bool) → Nat → Bool} (hDE : ∀ x, D x → E x)
    (hf : ULD E f) : ULD D f := fun k =>
  let ⟨N, hN⟩ := hf k
  ⟨N, fun x y hx hy hxy => hN x y (hDE x hx) (hDE y hy) hxy⟩

/-- **The hypotheses are not vacuous.** The free-bit chart itself, with `A` all sequences and `Lm`
the shift, satisfies them. -/
theorem free_bit_chart_is_chart : IsChart (fun _ => True) (fun a n => a (n + 1)) fb Theta where
  affA _ _ _ _ _ _ := trivial
  affL _ _ _ _ _ _ := rfl
  mapsTo _ _ := trivial
  mapsTo' a _ := kk_Theta a
  left_inv _ hL := Theta_fb hL
  right_inv a _ := fb_Theta a
  conj L _ := fb_shift L
  cont := uld_mono (fun _ _ => trivial) uld_fb
  cont' := uld_Theta

end Rule30LinearCharts
end Ruliology.CellularAutomata
