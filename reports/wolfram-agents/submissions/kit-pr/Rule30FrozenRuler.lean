module

public import Ruliology.CellularAutomata.Rule30Prize
public import Ruliology.CellularAutomata.Rule30Realization

/-!
# Rule 30: a finite-depth right edge follows the single-cell ruler with a fixed cap

Read a finite nonzero row of rule 30 from its rightmost black cell `e`: bit `k` of its *edge code*
is the cell at distance `k` from that cell (`code x e k = x (e - k)`). The right edge advances one
cell per step, and the code evolves by the edge map

  `T c 0 = c 0`, `T c 1 = c 1 ⊕ c 0`, `T c (k + 2) = c (k + 2) ⊕ (c (k + 1) ∨ c k)`

(`edge_evol`), the 2-adic right-edge map of Coven, Pivato and Yassawi (Proc. AMS 135, 2007). The
single black cell has code `one` (bit `0` only); `orbit s = iter s one` is its code at time `s`
(`seed_code`). Bit `k` of `T c` reads only bits `k - 2 .. k` of `c` and passes bit `k` through an
exclusive or, so two codes that agree below `k` and differ at `k` keep doing so for ever
(`iter_agree`, `iter_diff`).

* `HasDepth`, `depth_dichotomy`: a code has **depth `k`** with phase `s₀` when it agrees with
  `orbit s₀` below bit `k` while no code of the single cell's orbit agrees with it below `k + 1`.
  Every code with bit `0` black has a depth `k ≥ 2`, or agrees with the orbit at every depth.
* `frozen_ruler`: **the frozen ruler.** For a finite nonzero row whose code has depth `k ≥ 2` with
  phase `s₀`, at every time `t` its code, read from its rightmost black cell `e + t`, agrees with the
  single cell's code at time `s₀ + t` below `k` and differs at `k`; its white run behind the edge
  cell equals the single cell's when that is shorter than `k - 1`, is exactly `k - 1` when the single
  cell's is at least `k - 1`, and is never longer.
* `no_width_at_depth`: the single cell's code never has a white run of exactly `k - 1` when some code
  has depth `k`, so the cut width lies in a gap of the single cell's ruler. No counting of periods
  is used: such a run would put every depth-`k` code into the orbit at depth `k + 1`.
* `edge_run_alternates`: the cell behind the edge cell flips at every step, for every finite row.

Contributed by Gareth Herbert with Claude (Anthropic) and GPT (OpenAI). Nothing here concerns the
center column.
-/

@[expose] public section

namespace Ruliology.CellularAutomata.Rule30FrozenRuler

open Rule30Jen Rule30Realization

/-- One step of rule 30 read from a right edge that advances one cell per step. -/
def T (c : Nat → Bool) : Nat → Bool
  | 0 => c 0
  | 1 => xor (c 1) (c 0)
  | k + 2 => xor (c (k + 2)) (c (k + 1) || c k)

/-- `iter n c`: `n` steps of the edge map. -/
def iter : Nat → (Nat → Bool) → (Nat → Bool)
  | 0, c => c
  | n + 1, c => T (iter n c)

/-- The single black cell's edge code. -/
def one : Nat → Bool := fun k => decide (k = 0)

/-- The single black cell's edge code at time `s`. -/
def orbit (s : Nat) : Nat → Bool := iter s one

/-- Two codes agree on bits `0 .. k - 1`. -/
def AgreeBelow (k : Nat) (c d : Nat → Bool) : Prop := ∀ i, i < k → c i = d i

theorem xor_ne_xor {a b x y : Bool} (h : a ≠ b) (hxy : x = y) : xor a x ≠ xor b y := by
  subst hxy; cases a <;> cases b <;> cases x <;> simp_all

theorem T_agree {k : Nat} {c d : Nat → Bool} (h : AgreeBelow k c d) :
    AgreeBelow k (T c) (T d) := by
  intro i hi
  match i, hi with
  | 0, hi => simp [T, h 0 hi]
  | 1, hi => simp [T, h 1 hi, h 0 (by omega)]
  | j + 2, hi => simp [T, h (j + 2) hi, h (j + 1) (by omega), h j (by omega)]

theorem T_diff {k : Nat} {c d : Nat → Bool} (h : AgreeBelow k c d) (hk : c k ≠ d k) :
    T c k ≠ T d k := by
  match k, h, hk with
  | 0, _, hk => simpa [T] using hk
  | 1, h, hk => exact xor_ne_xor hk (h 0 (by omega))
  | j + 2, h, hk =>
    exact xor_ne_xor hk (by rw [h (j + 1) (by omega), h j (by omega)])

theorem iter_agree {k : Nat} {c d : Nat → Bool} (h : AgreeBelow k c d) :
    ∀ t, AgreeBelow k (iter t c) (iter t d)
  | 0 => h
  | t + 1 => T_agree (iter_agree h t)

theorem iter_diff {k : Nat} {c d : Nat → Bool} (h : AgreeBelow k c d) (hk : c k ≠ d k) :
    ∀ t, iter t c k ≠ iter t d k
  | 0 => hk
  | t + 1 => T_diff (iter_agree h t) (iter_diff h hk t)

theorem iter_zero (c : Nat → Bool) : ∀ t, iter t c 0 = c 0
  | 0 => rfl
  | t + 1 => iter_zero c t

theorem orbit_zero (s : Nat) : orbit s 0 = true := by
  simp [orbit, iter_zero, one]

theorem iter_add (c : Nat → Bool) (s : Nat) : ∀ t, iter (s + t) c = iter t (iter s c)
  | 0 => rfl
  | t + 1 => by
    show T (iter (s + t) c) = T (iter t (iter s c))
    rw [iter_add c s t]

theorem orbit_add (s t : Nat) : orbit (s + t) = iter t (orbit s) := iter_add one s t

/-! ### Rule 30 on finite rows, read from the right edge -/

/-- The edge code of a row whose rightmost black cell is `e`. -/
def code (x : Int → Bool) (e : Int) : Nat → Bool := fun k => x (e - k)

theorem edge_evol (x : Int → Bool) (e : Int) (he : x e = true)
    (hr : ∀ p, e < p → x p = false) :
    ∀ t : Nat, evol x t (e + t) = true ∧ (∀ p, e + t < p → evol x t p = false) ∧
      code (evol x t) (e + t) = iter t (code x e)
  | 0 => by
    refine ⟨by simpa [evol] using he, fun p hp => by simpa [evol] using hr p (by omega), ?_⟩
    funext k; simp [code, evol, iter]
  | t + 1 => by
    obtain ⟨h1, h2, h3⟩ := edge_evol x e he hr t
    have hz : ∀ p, e + (t : Int) < p → evol x t p = false := h2
    refine ⟨?_, ?_, ?_⟩
    · show rule (evol x t (e + (t + 1 : Nat) - 1)) (evol x t (e + (t + 1 : Nat)))
        (evol x t (e + (t + 1 : Nat) + 1)) = true
      have a : e + ((t + 1 : Nat) : Int) - 1 = e + t := by omega
      have b : e + ((t + 1 : Nat) : Int) + 1 = e + t + 2 := by omega
      have c : e + ((t + 1 : Nat) : Int) = e + t + 1 := by omega
      rw [a, b, c, h1, hz (e + t + 1) (by omega), hz (e + t + 2) (by omega)]
      rfl
    · intro p hp
      show rule (evol x t (p - 1)) (evol x t p) (evol x t (p + 1)) = false
      rw [hz (p - 1) (by omega), hz p (by omega), hz (p + 1) (by omega)]
      rfl
    · show code (evol x (t + 1)) (e + ((t + 1 : Nat) : Int)) = T (iter t (code x e))
      rw [← h3]
      funext k
      show rule (evol x t (e + ((t + 1 : Nat) : Int) - k - 1)) (evol x t (e + ((t + 1 : Nat) : Int) - k))
        (evol x t (e + ((t + 1 : Nat) : Int) - k + 1)) = T (code (evol x t) (e + t)) k
      match k with
      | 0 =>
        have a1 : e + ((t + 1 : Nat) : Int) - ((0 : Nat) : Int) - 1 = e + t := by omega
        have a2 : e + ((t + 1 : Nat) : Int) - ((0 : Nat) : Int) + 1 = e + t + 2 := by omega
        have a3 : e + ((t + 1 : Nat) : Int) - ((0 : Nat) : Int) = e + t + 1 := by omega
        rw [a1, a2, a3, hz (e + t + 1) (by omega), hz (e + t + 2) (by omega)]
        simp [T, code, rule]
      | 1 =>
        have a1 : e + ((t + 1 : Nat) : Int) - ((1 : Nat) : Int) - 1 = e + t - ((1 : Nat) : Int) := by
          omega
        have a2 : e + ((t + 1 : Nat) : Int) - ((1 : Nat) : Int) + 1 = e + t + 1 := by omega
        have a3 : e + ((t + 1 : Nat) : Int) - ((1 : Nat) : Int) = e + t - ((0 : Nat) : Int) := by
          omega
        rw [a1, a2, a3, hz (e + t + 1) (by omega)]
        simp [T, code, rule]
      | j + 2 =>
        have a1 : e + ((t + 1 : Nat) : Int) - ((j + 2 : Nat) : Int) - 1 =
            e + t - ((j + 2 : Nat) : Int) := by omega
        have a2 : e + ((t + 1 : Nat) : Int) - ((j + 2 : Nat) : Int) + 1 =
            e + t - ((j : Nat) : Int) := by omega
        have a3 : e + ((t + 1 : Nat) : Int) - ((j + 2 : Nat) : Int) =
            e + t - ((j + 1 : Nat) : Int) := by omega
        rw [a1, a2, a3]
        simp [T, code, rule]

/-- The single black cell's code at time `s` is `orbit s`. -/
theorem seed_code (s : Nat) : code (cell s) s = orbit s := by
  have h := (edge_evol seed 0 (by simp [seed]) (fun p hp => by simp [seed]; omega) s).2.2
  have hc : code seed 0 = one := by funext k; simp [code, seed, one]
  rw [hc] at h
  have : (fun p => evol seed s p) = cell s := funext (evol_seed s)
  simpa [orbit, this] using h

/-! ### Depth, and the frozen ruler -/

/-- The code `R₀` has depth `k` with phase `s₀`. -/
def HasDepth (R₀ : Nat → Bool) (k s₀ : Nat) : Prop :=
  AgreeBelow k (orbit s₀) R₀ ∧ ∀ s, ¬ AgreeBelow (k + 1) (orbit s) R₀

/-- Bits `1 .. w` are white: a white run of at least `w` cells behind the edge cell. -/
def WhiteAtLeast (c : Nat → Bool) (w : Nat) : Prop := ∀ i, 1 ≤ i → i ≤ w → c i = false

/-- A white run of exactly `w` cells behind the edge cell. -/
def Width (c : Nat → Bool) (w : Nat) : Prop := WhiteAtLeast c w ∧ c (w + 1) = true

/-- **The edge black run alternates** (the first level of the ruler, for every finite row). -/
theorem edge_run_alternates (x : Int → Bool) (e : Int) (he : x e = true)
    (hr : ∀ p, e < p → x p = false) (t : Nat) :
    code (evol x (t + 1)) (e + ((t + 1 : Nat) : Int)) 1 = ! code (evol x t) (e + t) 1 := by
  rw [(edge_evol x e he hr (t + 1)).2.2, (edge_evol x e he hr t).2.2]
  have h0 : iter t (code x e) 0 = true := by rw [iter_zero]; simpa [code] using he
  show xor (iter t (code x e) 1) (iter t (code x e) 0) = !iter t (code x e) 1
  rw [h0]; simp

theorem bit_k {R₀ : Nat → Bool} {k s₀ : Nat} (hd : HasDepth R₀ k s₀) : orbit s₀ k ≠ R₀ k := by
  intro heq
  apply hd.2 s₀
  intro i hi
  rcases Nat.lt_succ_iff_lt_or_eq.mp hi with hi | rfl
  · exact hd.1 i hi
  · exact heq

theorem depth_shift {R₀ : Nat → Bool} {k s₀ : Nat} (hd : HasDepth R₀ k s₀) (t : Nat) :
    AgreeBelow k (orbit (s₀ + t)) (iter t R₀) ∧ orbit (s₀ + t) k ≠ iter t R₀ k := by
  rw [orbit_add]
  exact ⟨iter_agree hd.1 t, iter_diff hd.1 (bit_k hd) t⟩

/-- The single cell's code never has a white run of exactly `k - 1` behind its edge, when some code
has depth `k`. -/
theorem no_width_at_depth {R₀ : Nat → Bool} {k s₀ : Nat} (hd : HasDepth R₀ k s₀) (hk : 1 ≤ k)
    (u : Nat) : ¬ (AgreeBelow k (orbit u) one ∧ orbit u k = true) := by
  rintro ⟨ha, hb⟩
  have hne : orbit u k ≠ one k := by simp [one, hb]; omega
  have hA := iter_agree ha s₀
  have hD := iter_diff ha hne s₀
  rw [← orbit_add] at hA hD
  have hk0 := bit_k hd
  apply hd.2 (u + s₀)
  intro i hi
  rcases Nat.lt_succ_iff_lt_or_eq.mp hi with hi | rfl
  · rw [hA i hi]; exact hd.1 i hi
  · have hD' : orbit (u + s₀) i ≠ orbit s₀ i := hD
    revert hD' hk0
    cases orbit (u + s₀) i <;> cases orbit s₀ i <;> cases R₀ i <;> simp

theorem frozen_code {R₀ : Nat → Bool} {k s₀ : Nat} (hd : HasDepth R₀ k s₀) (hk : 2 ≤ k)
    (t : Nat) :
    (∀ w, w + 1 < k → (Width (iter t R₀) w ↔ Width (orbit (s₀ + t)) w)) ∧
    (Width (iter t R₀) (k - 1) ↔ WhiteAtLeast (orbit (s₀ + t)) (k - 1)) ∧
    (∀ w, k ≤ w → ¬ Width (iter t R₀) w) := by
  obtain ⟨hA, hD⟩ := depth_shift hd t
  have gap : WhiteAtLeast (orbit (s₀ + t)) (k - 1) → orbit (s₀ + t) k = false := by
    intro hw
    cases hb : orbit (s₀ + t) k
    · rfl
    · exfalso
      apply no_width_at_depth hd (by omega) (s₀ + t)
      refine ⟨fun i hi => ?_, hb⟩
      rcases Nat.eq_zero_or_pos i with rfl | hpos
      · simp [one, orbit_zero]
      · have h1 : one i = false := by simp [one]; omega
        rw [h1]; exact hw i hpos (by omega)
  refine ⟨fun w hw => ?_, ?_, fun w hw hW => ?_⟩
  · constructor
    · rintro ⟨h1, h2⟩
      exact ⟨fun i hi hiw => by rw [hA i (by omega)]; exact h1 i hi hiw,
        by rw [hA (w + 1) hw]; exact h2⟩
    · rintro ⟨h1, h2⟩
      exact ⟨fun i hi hiw => by rw [← hA i (by omega)]; exact h1 i hi hiw,
        by rw [← hA (w + 1) hw]; exact h2⟩
  · have hk1 : k - 1 + 1 = k := by omega
    unfold Width
    rw [hk1]
    constructor
    · rintro ⟨h1, _⟩ i hi hiw
      rw [hA i (by omega)]; exact h1 i hi hiw
    · intro h1
      refine ⟨fun i hi hiw => by rw [← hA i (by omega)]; exact h1 i hi hiw, ?_⟩
      have := gap h1
      revert hD this
      cases orbit (s₀ + t) k <;> cases iter t R₀ k <;> simp
  · have h1 : WhiteAtLeast (orbit (s₀ + t)) (k - 1) := fun i hi hiw => by
      rw [hA i (by omega)]; exact hW.1 i hi (by omega)
    have hck : iter t R₀ k = false := hW.1 k (by omega) hw
    have := gap h1
    revert hD this hck
    cases orbit (s₀ + t) k <;> cases iter t R₀ k <;> simp

/-- **The frozen ruler.** A finite nonzero row with rightmost black cell `e` whose edge code has
depth `k ≥ 2` with phase `s₀`: at every time `t`, read from its rightmost black cell `e + t`, its
code agrees with the single cell's code at time `s₀ + t` below bit `k` and differs at bit `k`; the
white run behind its edge cell is the single cell's whenever that run is shorter than `k - 1`,
exactly `k - 1` whenever the single cell's is at least `k - 1`, and never longer. -/
theorem frozen_ruler (x : Int → Bool) (e : Int) (he : x e = true)
    (hr : ∀ p, e < p → x p = false) (k s₀ : Nat) (hk : 2 ≤ k)
    (hd : HasDepth (code x e) k s₀) (t : Nat) :
    evol x t (e + t) = true ∧ (∀ p, e + t < p → evol x t p = false) ∧
    AgreeBelow k (code (cell (s₀ + t)) ((s₀ + t : Nat) : Int)) (code (evol x t) (e + t)) ∧
    code (cell (s₀ + t)) ((s₀ + t : Nat) : Int) k ≠ code (evol x t) (e + t) k ∧
    (∀ w, w + 1 < k →
      (Width (code (evol x t) (e + t)) w ↔ Width (code (cell (s₀ + t)) ((s₀ + t : Nat) : Int)) w)) ∧
    (Width (code (evol x t) (e + t)) (k - 1) ↔
      WhiteAtLeast (code (cell (s₀ + t)) ((s₀ + t : Nat) : Int)) (k - 1)) ∧
    (∀ w, k ≤ w → ¬ Width (code (evol x t) (e + t)) w) := by
  obtain ⟨h1, h2, h3⟩ := edge_evol x e he hr t
  have hs := seed_code (s₀ + t)
  obtain ⟨hA, hD⟩ := depth_shift hd t
  obtain ⟨w1, w2, w3⟩ := frozen_code hd hk t
  rw [h3, hs]
  exact ⟨h1, h2, hA, hD, w1, w2, w3⟩

/-! ### Every finite row has a depth -/

theorem orbit_one_bit (c : Nat → Bool) (h0 : c 0 = true) :
    AgreeBelow 2 (orbit 0) c ∨ AgreeBelow 2 (orbit 1) c := by
  cases h1 : c 1
  · left; intro i hi
    match i, hi with
    | 0, _ => simp [orbit, iter, one, h0]
    | 1, _ => simp [orbit, iter, one, h1]
  · right; intro i hi
    match i, hi with
    | 0, _ => simp [orbit, iter, T, one, h0]
    | 1, _ => simp [orbit, iter, T, one, h1]

/-- From a level where agreement holds to one where it fails, there is a last level that holds. -/
theorem last_level (P : Nat → Prop) (h2 : P 2) :
    ∀ K, 2 ≤ K → ¬ P K → ∃ k, 2 ≤ k ∧ P k ∧ ¬ P (k + 1)
  | 0, hK, _ => absurd hK (by omega)
  | K + 1, hK, h => by
    by_cases hK2 : 2 ≤ K
    · by_cases hP : P K
      · exact ⟨K, hK2, hP, h⟩
      · exact last_level P h2 K hK2 hP
    · have e : K + 1 = 2 := by omega
      rw [e] at h
      exact absurd h2 h

/-- Every code with bit `0` black either agrees with the single cell's orbit at every depth, or
has a depth `k ≥ 2`. -/
theorem depth_dichotomy (c : Nat → Bool) (h0 : c 0 = true) :
    (∀ k, ∃ s, AgreeBelow k (orbit s) c) ∨ ∃ k s₀, 2 ≤ k ∧ HasDepth c k s₀ := by
  by_cases hall : ∀ k, ∃ s, AgreeBelow k (orbit s) c
  · exact Or.inl hall
  · right
    have h2 : ∃ s, AgreeBelow 2 (orbit s) c := by
      rcases orbit_one_bit c h0 with h | h
      · exact ⟨0, h⟩
      · exact ⟨1, h⟩
    have hK : ∃ K, ¬ ∃ s, AgreeBelow K (orbit s) c :=
      Classical.byContradiction fun hc => hall fun k =>
        Classical.byContradiction fun hk => hc ⟨k, hk⟩
    obtain ⟨K, hK⟩ := hK
    have hK2 : 2 ≤ K := by
      apply Classical.byContradiction
      intro hlt
      obtain ⟨s, hs⟩ := h2
      exact hK ⟨s, fun i hi => hs i (by omega)⟩
    obtain ⟨k, hk2, ⟨s₀, hs⟩, hk1⟩ :=
      last_level (fun k => ∃ s, AgreeBelow k (orbit s) c) h2 K hK2 hK
    exact ⟨k, s₀, hk2, hs, fun s hs' => hk1 ⟨s, hs'⟩⟩

end Ruliology.CellularAutomata.Rule30FrozenRuler
