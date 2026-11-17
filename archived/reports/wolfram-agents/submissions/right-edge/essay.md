---
Template: ComputationalEssay
Name: A finite-depth right edge follows the single-cell ruler with a fixed cap
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-27
Description: A partial structural result on Rule 30, proved in Lean against the kit. Every right-edge code either agrees with the single-cell orbit at every finite depth, with a phase that may depend on that depth, or has finite orbit depth k. In the latter case its emitted white-run lengths follow one fixed phase of the single-cell ruler, capped at k - 1, and the cap lies in a gap of the ruler.
Abstract: For every finite nonzero row $x$ of rule 30, read from its rightmost black cell $e$ (bit $k$ of the edge code is $x(e-k)$), the edge advances one cell per step and the code evolves by the 2-adic edge map $T$ of Coven, Pivato and Yassawi (`edge_evol`). For rows of finite orbit depth, we prove the following capped-ruler theorem. Suppose the code agrees with the single cell's code at time $s_0$ on bits $0,\dots,k-1$, for some $k \ge 2$, while no code of the single cell's orbit agrees with it on bits $0,\dots,k$. Then at every time $t$ the code agrees with the single cell's code at time $s_0+t$ below bit $k$ and differs at bit $k$. Its white run behind the edge cell equals the single cell's when that run is shorter than $k-1$, is exactly $k-1$ when the single cell's is at least $k-1$, and is never longer (`frozen_ruler`). The single cell's code never has a white run of exactly $k-1$ (`no_width_at_depth`), so the cut width lies in a gap of the ruler. Every row has a depth, or agrees with the orbit at every depth (`depth_dichotomy`). The kit's `Rule30RightPeriods` describes the single cell's right diagonals; this gives a conditional capped-ruler theorem and a depth dichotomy for arbitrary right-edge codes. The proof uses only the triangularity of $T$, with no counting of periods. Not claimed: anything about the center column or the Prize problems, or that rows of infinite depth are the single cell's own rows (open).
Keywords: [rule 30, Rule 30 Prize, right edge, edge code, 2-adic, ruler, finite configurations, universality, Lean 4, LeanLink]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[Rule30RightPeriods in the kit](https://github.com/WolframInstitute/Rule30PrizeKit/blob/main/lean/Ruliology/CellularAutomata/Rule30RightPeriods.lean)"]
---

## The question

Started from one black cell, rule 30 has a famously regular right edge. Read the row from its rightmost black cell leftward: just behind that cell there is a run of white cells, and its length, step by step, is a *ruler*: 0, 2, 0, 3, 0, 2, 0, 5, 0, 2, 0, 3, 0, 2, 0, 6, … The kit's `Rule30RightPeriods` describes the single cell's right diagonals, whose periods produce this ruler. What does the right edge of an *arbitrary* finite starting row look like? Every right-edge code either agrees with the single-cell orbit at every finite depth, with a phase that may depend on that depth, or has finite orbit depth `k`. This essay proves that in the latter case its emitted white-run lengths follow one fixed phase of the single-cell ruler, capped at `k - 1`.

## The ruler, and two rows that copy it

One step of rule 30, on a finite row (white beyond both ends), and the length of the white run just behind the rightmost black cell:

```wl
step[w_] := With[{p = Join[{0, 0}, w, {0, 0}]}, Table[BitXor[p[[i - 1]], BitOr[p[[i]], p[[i + 1]]]], {i, 2, Length[p] - 1}]];
width[w_] := With[{r = Reverse[w]}, LengthWhile[Drop[r, First[FirstPosition[r, 1]]], # == 0 &]];
widths[init_, n_] := width /@ Rest[NestList[step, init, n]];
single = widths[{1}, 40];
Take[single, 32]
```

The single cell gives `0, 2, 0, 3, 0, 2, 0, 5, 0, 2, 0, 3, 0, 2, 0, 6, …, 0, 8`: a zero at every other step (the black run at the edge alternates between one cell and more), and between them the widths of the white triangles the edge emits.

The row of four black cells copies the ruler from time `3` on, except that every width of `4` or more becomes exactly `4`:

```wl
four = widths[{1, 1, 1, 1}, 32];
{Take[four, 16], Take[four, 29] === Table[Min[single[[t + 3]], 4], {t, 1, 29}]}
```

The row `1 0 1 1 1` does the same with phase `5`, and the row `1 1`, a *rain edge*, emits only lone white cells, the ruler cut at width `1`:

```wl
{widths[{1, 0, 1, 1, 1}, 29] === Table[Min[single[[t + 5]], 4], {t, 1, 29}], Take[widths[{1, 1}, 12], 12]}
```

The cut widths `1` and `4` never occur in the single cell's own ruler. The theorem says why; it describes every row of finite orbit depth, and the infinite-depth alternative is left explicit below.

## The theorem

Read a finite nonzero row `x` from its rightmost black cell `e`: bit `k` of its **edge code** is the cell at distance `k` from `e` (`code x e k = x (e - k)`). The single cell's code is `one` (bit `0` only), and `orbit s` is its code at time `s`.

- **The edge map** (`edge_evol`). The rightmost black cell of `evol x t` is `e + t`, and its code is `T^[t] (code x e)`, where `T c 0 = c 0`, `T c 1 = c 1 xor c 0` and `T c (k + 2) = c (k + 2) xor (c (k + 1) || c k)`. This is the 2-adic right-edge map of Coven, Pivato and Yassawi.
- **Depth** (`HasDepth`, `depth_dichotomy`). A code has depth `k` with phase `s₀` if it agrees with `orbit s₀` on bits `0 .. k - 1`, while no code of the single cell's orbit agrees with it on bits `0 .. k`. Every finite nonzero row has a depth `k ≥ 2`, or agrees with the single cell's orbit at every depth.
- **The frozen ruler** (`frozen_ruler`). If the code of `x` has depth `k ≥ 2` with phase `s₀`, then for every time `t`, the code of `evol x t` agrees with the single cell's code at time `s₀ + t` below bit `k` and differs from it at bit `k`. Its white run behind the edge cell is the single cell's whenever that run is shorter than `k - 1`, exactly `k - 1` whenever the single cell's run is at least `k - 1`, and never longer.
- **The cut is in a gap** (`no_width_at_depth`). The single cell's code never has a white run of exactly `k - 1` behind its edge, when some code has depth `k`.
- **The first level for every row** (`edge_run_alternates`). The cell behind the edge cell flips at every step.

## The idea of the proof

1. **The edge map.** The rightmost black cell `e` always gains a black right neighbour (`rule 1 0 0 = 1`) and nothing beyond it, so the edge moves one cell per step. Read from the edge, the new bit `k` is the rule applied to the old bits `k`, `k - 1` and `k - 2`, with white beyond the edge: that is `T`.
2. **Triangularity.** Bit `k` of `T c` reads only bits `k - 2 .. k` of `c`, and passes bit `k` through an exclusive or. So two codes that agree below `k` and differ at bit `k` keep doing so for ever (`iter_agree`, `iter_diff`). A row of depth `k` and the single cell, shifted by `s₀`, are such a pair.
3. **Widths.** A white run shorter than `k - 1` is read below bit `k`, where the two agree. If the single cell's bits `1 .. k - 1` are white, its bit `k` must be white too, by step 4, so the row's bit `k` is black: its run is exactly `k - 1`. A longer run for the row would force the single cell's bits `1 .. k - 1` white and bit `k` black, which step 4 excludes.
4. **The gap.** Suppose the single cell's code at some time `u` has bits `1 .. k - 1` white and bit `k` black. It then agrees with `one` below `k` and differs at `k`, so by step 2 the codes at times `u + s₀` and `s₀` differ exactly at bit `k`. The row's code differs from the code at `s₀` exactly at bit `k` too, so it agrees with the code at `u + s₀` on bits `0 .. k`, contradicting its depth. No counting of periods is needed.
5. **Every row has a depth.** Bit `0` is always black, and the single cell's codes at times `0` and `1` cover both values of bit `1`. So every code agrees with the orbit below `2`, and the least depth where agreement fails, if there is one, is at least `3`.

## The formal proof

The module, built against the kit at the verifier's commit:

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["import Rule30PrizeKit

/-!
# A finite-depth right edge follows the single-cell ruler with a fixed cap

Read a finite nonzero row of rule 30 from its rightmost black cell `e`: bit `k` of its *edge code*
is the cell at distance `k` from that cell (`code x e k = x (e - k)`). The right edge advances one
cell per step, and the code evolves by the edge map

  `T c 0 = c 0`, `T c 1 = c 1 ⊕ c 0`, `T c (k + 2) = c (k + 2) ⊕ (c (k + 1) ∨ c k)`

(`edge_evol`). The single black cell has code `one` (bit `0` only), and `orbit s = T^[s] one` is its
code at time `s` (`seed_code`). Bit `k` of `T c` reads only bits `k - 2 .. k` of `c`, and passes
bit `k` through an exclusive or, so two codes that agree below `k` and differ at `k` keep doing so
for ever (`iter_agree`, `iter_diff`).

**Depth.** Say a code `R₀` has depth `k` with phase `s₀` when it agrees with the single cell's code
`orbit s₀` below bit `k`, but no code of the single cell's orbit agrees with it below bit `k + 1`
(`HasDepth`). Every finite nonzero row has a depth `k ≥ 2`, or agrees with the single cell's orbit
at every depth (`depth_dichotomy`).

**The headline (`frozen_ruler`).** Let `x` be a finite nonzero row with rightmost black cell `e`
whose code has depth `k ≥ 2` with phase `s₀`. Then for every time `t`, the code of `evol x t`, read
from its rightmost black cell `e + t`,
* agrees with the single cell's code at time `s₀ + t` below bit `k`, and differs from it at bit `k`;
* has a white run behind its edge cell of length exactly `w` (bits `1 .. w` white, bit `w + 1`
  black) for some `w ≤ k - 1`; for `w < k - 1` this happens exactly when the single cell's code at
  time `s₀ + t` has a white run of exactly `w`, and for `w = k - 1` exactly when the single cell's
  code has at least `k - 1` white cells behind its edge.

So every finite row of finite depth `k` emits the single cell's white triangles at its right edge, shifted in time by `s₀`,
except that each one of width `k - 1` or more is cut to exactly `k - 1`. The cut is never visible in
the single cell's own picture: its code never has a white run of exactly `k - 1` behind the edge
(`no_width_at_depth`), because that would put every code of depth `k` into the orbit at depth
`k + 1`. The width `k - 1` therefore lies in a gap of the single cell's ruler.

Credit: the edge map is the 2-adic right-edge map of Coven, Pivato and Yassawi (2007). The
capped-ruler statement for rows of finite depth is not in the kit's catalog as we read it. Nothing here concerns the
center column.
-/

namespace Rule30Submission

open Ruliology.CellularAutomata
open Ruliology.CellularAutomata.Rule30Jen (rule cell)
open Ruliology.CellularAutomata.Rule30Realization (evol seed evol_seed)

/-! ### The edge map -/

/-- One step of rule 30 read from a right edge that advances one cell per step. -/
def T (c : Nat → Bool) : Nat → Bool
  | 0 => c 0
  | 1 => xor (c 1) (c 0)
  | k + 2 => xor (c (k + 2)) (c (k + 1) || c k)

/-- The single black cell's edge code. -/
def one : Nat → Bool := fun k => decide (k = 0)

/-- The single black cell's edge code at time `s`. -/
def orbit (s : Nat) : Nat → Bool := T^[s] one

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
    ∀ t, AgreeBelow k (T^[t] c) (T^[t] d)
  | 0 => h
  | t + 1 => by
    rw [Function.iterate_succ_apply', Function.iterate_succ_apply']
    exact T_agree (iter_agree h t)

theorem iter_diff {k : Nat} {c d : Nat → Bool} (h : AgreeBelow k c d) (hk : c k ≠ d k) :
    ∀ t, T^[t] c k ≠ T^[t] d k
  | 0 => hk
  | t + 1 => by
    rw [Function.iterate_succ_apply', Function.iterate_succ_apply']
    exact T_diff (iter_agree h t) (iter_diff h hk t)

theorem T_zero (c : Nat → Bool) : T c 0 = c 0 := rfl

theorem iter_zero (c : Nat → Bool) : ∀ t, T^[t] c 0 = c 0
  | 0 => rfl
  | t + 1 => by rw [Function.iterate_succ_apply', T_zero, iter_zero c t]

theorem orbit_zero (s : Nat) : orbit s 0 = true := by
  simp [orbit, iter_zero, one]

theorem orbit_add (s t : Nat) : orbit (s + t) = T^[t] (orbit s) := by
  simp only [orbit]
  rw [Nat.add_comm, Function.iterate_add_apply]

/-! ### Rule 30 on finite rows, read from the right edge -/

/-- The edge code of a row whose rightmost black cell is `e`. -/
def code (x : Int → Bool) (e : Int) : Nat → Bool := fun k => x (e - k)

theorem edge_evol (x : Int → Bool) (e : Int) (he : x e = true)
    (hr : ∀ p, e < p → x p = false) :
    ∀ t : Nat, evol x t (e + t) = true ∧ (∀ p, e + t < p → evol x t p = false) ∧
      code (evol x t) (e + t) = T^[t] (code x e)
  | 0 => by
    refine ⟨by simpa [evol] using he, fun p hp => by simpa [evol] using hr p (by omega), ?_⟩
    funext k; simp [code, evol]
  | t + 1 => by
    obtain ⟨h1, h2, h3⟩ := edge_evol x e he hr t
    have hz : ∀ p, e + (t : Int) < p → evol x t p = false := h2
    refine ⟨?_, ?_, ?_⟩
    · show rule (evol x t (e + (t + 1 : Nat) - 1)) (evol x t (e + (t + 1 : Nat)))
        (evol x t (e + (t + 1 : Nat) + 1)) = true
      have a : e + ((t + 1 : Nat) : Int) - 1 = e + t := by push_cast; ring
      rw [a, h1, hz _ (by push_cast; omega), hz _ (by push_cast; omega)]
      rfl
    · intro p hp
      show rule (evol x t (p - 1)) (evol x t p) (evol x t (p + 1)) = false
      push_cast at hp
      rw [hz _ (by omega), hz _ (by omega), hz _ (by omega)]
      rfl
    · rw [Function.iterate_succ_apply', ← h3]
      funext k
      have hm : e + ((t + 1 : Nat) : Int) = (e + t) + 1 := by push_cast; ring
      show rule (evol x t (e + ((t + 1 : Nat) : Int) - k - 1)) (evol x t (e + ((t + 1 : Nat) : Int) - k))
        (evol x t (e + ((t + 1 : Nat) : Int) - k + 1)) = T (code (evol x t) (e + t)) k
      rw [hm]
      match k with
      | 0 =>
        have a1 : e + (t : Int) + 1 - ((0 : Nat) : Int) - 1 = e + t := by push_cast; ring
        have a2 : e + (t : Int) + 1 - ((0 : Nat) : Int) + 1 = e + t + 2 := by push_cast; ring
        have a3 : e + (t : Int) + 1 - ((0 : Nat) : Int) = e + t + 1 := by push_cast; ring
        rw [a1, a2, a3, hz (e + t + 1) (by omega), hz (e + t + 2) (by omega)]
        simp [T, code, rule]
      | 1 =>
        have a1 : e + (t : Int) + 1 - ((1 : Nat) : Int) - 1 = e + t - ((1 : Nat) : Int) := by
          push_cast; ring
        have a2 : e + (t : Int) + 1 - ((1 : Nat) : Int) + 1 = e + t + 1 := by push_cast; ring
        have a3 : e + (t : Int) + 1 - ((1 : Nat) : Int) = e + t - ((0 : Nat) : Int) := by
          push_cast; ring
        rw [a1, a2, a3, hz (e + t + 1) (by omega)]
        simp [T, code, rule]
      | j + 2 =>
        have a1 : e + (t : Int) + 1 - ((j + 2 : Nat) : Int) - 1 = e + t - ((j + 2 : Nat) : Int) := by
          push_cast; ring
        have a2 : e + (t : Int) + 1 - ((j + 2 : Nat) : Int) + 1 = e + t - ((j : Nat) : Int) := by
          push_cast; ring
        have a3 : e + (t : Int) + 1 - ((j + 2 : Nat) : Int) = e + t - ((j + 1 : Nat) : Int) := by
          push_cast; ring
        rw [a1, a2, a3]
        simp [T, code, rule]

/-- The single black cell's code at time `s` is `orbit s`. -/
theorem seed_code (s : Nat) : code (cell s) s = orbit s := by
  have h := (edge_evol seed 0 (by simp [seed]) (fun p hp => by simp [seed]; omega) s).2.2
  have hc : code seed 0 = one := by funext k; simp [code, seed, one]
  rw [hc] at h
  have : (fun p => evol seed s p) = cell s := funext (evol_seed s)
  simpa [orbit, this] using h

/-- **The edge black run alternates** (the first level of the ruler, for every finite row): the
cell behind the edge cell flips at every step, so the run of black cells ending at the right edge
has length `1` at every other step and at least `2` at the steps between. -/
theorem edge_run_alternates (x : Int → Bool) (e : Int) (he : x e = true)
    (hr : ∀ p, e < p → x p = false) (t : Nat) :
    code (evol x (t + 1)) (e + ((t + 1 : Nat) : Int)) 1 = ! code (evol x t) (e + t) 1 := by
  rw [(edge_evol x e he hr (t + 1)).2.2, (edge_evol x e he hr t).2.2,
    Function.iterate_succ_apply']
  have h0 : T^[t] (code x e) 0 = true := by rw [iter_zero]; simpa [code] using he
  show xor (T^[t] (code x e) 1) (T^[t] (code x e) 0) = !T^[t] (code x e) 1
  rw [h0]; simp

/-! ### Depth, and the frozen ruler -/

/-- The code `R₀` has depth `k` with phase `s₀`. -/
def HasDepth (R₀ : Nat → Bool) (k s₀ : Nat) : Prop :=
  AgreeBelow k (orbit s₀) R₀ ∧ ∀ s, ¬ AgreeBelow (k + 1) (orbit s) R₀

/-- Bits `1 .. w` are white: a white run of at least `w` cells behind the edge cell. -/
def WhiteAtLeast (c : Nat → Bool) (w : Nat) : Prop := ∀ i, 1 ≤ i → i ≤ w → c i = false

/-- A white run of exactly `w` cells behind the edge cell. -/
def Width (c : Nat → Bool) (w : Nat) : Prop := WhiteAtLeast c w ∧ c (w + 1) = true

theorem depth_shift {R₀ : Nat → Bool} {k s₀ : Nat} (hd : HasDepth R₀ k s₀) (t : Nat) :
    AgreeBelow k (orbit (s₀ + t)) (T^[t] R₀) ∧ orbit (s₀ + t) k ≠ T^[t] R₀ k := by
  have hk : orbit s₀ k ≠ R₀ k := by
    intro heq
    apply hd.2 s₀
    intro i hi
    rcases Nat.lt_succ_iff_lt_or_eq.mp hi with hi | rfl
    · exact hd.1 i hi
    · exact heq
  rw [orbit_add]
  exact ⟨iter_agree hd.1 t, iter_diff hd.1 hk t⟩

/-- The single cell's code never has a white run of exactly `k - 1` behind its edge, when some code
has depth `k`. -/
theorem no_width_at_depth {R₀ : Nat → Bool} {k s₀ : Nat} (hd : HasDepth R₀ k s₀) (hk : 1 ≤ k)
    (u : Nat) : ¬ (AgreeBelow k (orbit u) one ∧ orbit u k = true) := by
  rintro ⟨ha, hb⟩
  have hne : orbit u k ≠ one k := by simp [one, hb]; omega
  have hA := iter_agree ha s₀
  have hD := iter_diff ha hne s₀
  rw [← orbit_add] at hA hD
  have hsame : T^[s₀] one = orbit s₀ := rfl
  rw [hsame] at hA hD
  have hk0 : orbit s₀ k ≠ R₀ k := by
    intro heq
    apply hd.2 s₀
    intro i hi
    rcases Nat.lt_succ_iff_lt_or_eq.mp hi with hi | rfl
    · exact hd.1 i hi
    · exact heq
  apply hd.2 (u + s₀)
  intro i hi
  rcases Nat.lt_succ_iff_lt_or_eq.mp hi with hi | rfl
  · rw [hA i hi, hd.1 i hi]
  · revert hD hk0
    cases orbit (u + s₀) i <;> cases orbit s₀ i <;> cases R₀ i <;> simp

theorem frozen_code {R₀ : Nat → Bool} {k s₀ : Nat} (hd : HasDepth R₀ k s₀) (hk : 2 ≤ k)
    (t : Nat) :
    (∀ w, w + 1 < k → (Width (T^[t] R₀) w ↔ Width (orbit (s₀ + t)) w)) ∧
    (Width (T^[t] R₀) (k - 1) ↔ WhiteAtLeast (orbit (s₀ + t)) (k - 1)) ∧
    (∀ w, k ≤ w → ¬ Width (T^[t] R₀) w) := by
  obtain ⟨hA, hD⟩ := depth_shift hd t
  set c := T^[t] R₀
  set o := orbit (s₀ + t)
  -- the single cell's code cannot have bits 1 .. k-1 white and bit k black
  have gap : WhiteAtLeast o (k - 1) → o k = false := by
    intro hw
    by_contra hb
    apply no_width_at_depth hd (by omega) (s₀ + t)
    refine ⟨fun i hi => ?_, by simpa using hb⟩
    rcases Nat.eq_zero_or_pos i with rfl | hpos
    · simp [one, orbit_zero]
    · have h1 : one i = false := by simp [one]; omega
      rw [h1]; exact hw i hpos (by omega)
  refine ⟨fun w hw => ?_, ?_, fun w hw hW => ?_⟩
  · unfold Width WhiteAtLeast
    constructor
    · rintro ⟨h1, h2⟩
      exact ⟨fun i hi hiw => by rw [hA i (by omega)]; exact h1 i hi hiw,
        by rw [hA (w + 1) hw]; exact h2⟩
    · rintro ⟨h1, h2⟩
      exact ⟨fun i hi hiw => by rw [← hA i (by omega)]; exact h1 i hi hiw,
        by rw [← hA (w + 1) hw]; exact h2⟩
  · unfold Width
    have hk1 : k - 1 + 1 = k := by omega
    rw [hk1]
    constructor
    · rintro ⟨h1, _⟩ i hi hiw
      rw [hA i (by omega)]; exact h1 i hi hiw
    · intro h1
      have hc : ∀ i, 1 ≤ i → i ≤ k - 1 → c i = false := fun i hi hiw => by
        rw [← hA i (by omega)]; exact h1 i hi hiw
      refine ⟨hc, ?_⟩
      have := gap h1
      revert hD this
      cases o k <;> cases c k <;> simp
  · -- bits 1 .. k of c white force o's bits 1 .. k-1 white and bit k black: impossible
    have h1 : WhiteAtLeast o (k - 1) := fun i hi hiw => by
      rw [hA i (by omega)]; exact hW.1 i hi (by omega)
    have hck : c k = false := hW.1 k (by omega) hw
    have := gap h1
    revert hD this hck
    cases o k <;> cases c k <;> simp

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
    | 0, _ => simp [orbit, one, h0]
    | 1, _ => simp [orbit, one, h1]
  · right; intro i hi
    match i, hi with
    | 0, _ => simp [orbit, T, one, h0]
    | 1, _ => simp [orbit, T, one, h1]

/-- Every code with bit `0` black either agrees with the single cell's orbit at every depth, or
has a depth `k ≥ 2`. -/
theorem depth_dichotomy (c : Nat → Bool) (h0 : c 0 = true) :
    (∀ k, ∃ s, AgreeBelow k (orbit s) c) ∨ ∃ k s₀, 2 ≤ k ∧ HasDepth c k s₀ := by
  classical
  by_cases hall : ∀ k, ∃ s, AgreeBelow k (orbit s) c
  · exact Or.inl hall
  · right
    push Not at hall
    have hex : ∃ k, ∀ s, ¬ AgreeBelow k (orbit s) c := hall
    let k := Nat.find hex
    have hk : ∀ s, ¬ AgreeBelow k (orbit s) c := Nat.find_spec hex
    have h2 : 2 < k := by
      by_contra hle
      push Not at hle
      rcases orbit_one_bit c h0 with h | h
      · exact hk 0 (fun i hi => h i (by omega))
      · exact hk 1 (fun i hi => h i (by omega))
    have hprev : ∃ s, AgreeBelow (k - 1) (orbit s) c := by
      have := Nat.find_min hex (show k - 1 < k by omega)
      push Not at this
      exact this
    obtain ⟨s₀, hs⟩ := hprev
    refine ⟨k - 1, s₀, by omega, hs, fun s => ?_⟩
    have : k - 1 + 1 = k := by omega
    rw [this]
    exact hk s

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The headlines, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30Realization", "Ruliology.CellularAutomata.Rule30Jen"};
thm = rule30Submission["Rule30Submission.frozen_ruler"];
Table[rule30Submission["Rule30Submission." <> n]["TypeForm", "Open" -> opens], {n, {"frozen_ruler", "no_width_at_depth", "depth_dichotomy", "edge_evol", "edge_run_alternates"}}]
```

The axioms of the headline `frozen_ruler` are the three standard ones and nothing else (the checker verifies all five headlines and replays the whole module):

```wl
thm["Axioms"]
```

The proof's structure, one level down from the headline:

```wl
thm["CallGraph", "Depth" -> 1]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
thm["KernelCheck"]
```

## What is not proved

- Nothing about the center column, or any of the Prize problems. The center sits ever deeper behind the edge, and this result says nothing there.
- The infinite-depth case is stated only as agreement with the single cell's orbit at every finite depth, with a phase that may depend on the depth. Whether every finite row of infinite depth is one of the single cell's own rows, shifted in time, is open.
- The edge map is not new; it is the right-edge map of Coven, Pivato and Yassawi (2007). The capped-ruler theorem for rows of finite orbit depth is new to the kit's catalog and the submissions list as we read them, which is a statement about our search, not a global novelty determination.
- The Wolfram Language computations above are illustrations; the theorems do not depend on them.

## Provenance

The owner of the project noticed the ruler on the single cell's right edge. Claude (Anthropic), on the Apple M5, found that every finite row keeps it up to one depth (the record's L1000 and L1001), and proved the theorem by hand. GPT (OpenAI) read the proof, replaced its period-counting step with a direct argument (GC1935), and qualified the infinite-depth case. Claude wrote this module, using an argument that needs no period counting at all. The record is at github.com/ghywel/placego, reports/rule30-universal-ruler.md and reports/wolfram-agents/submissions/right-edge.

## References

[1] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[2] E. M. Coven, M. Pivato and R. Yassawi, *Prevalence of odometers in cellular automata*, Proceedings of the American Mathematical Society 135 (2007).

[3] Wolfram Institute, [*The Rule 30 Prize kit*](https://github.com/WolframInstitute/Rule30PrizeKit), 2026: `Rule30RightPeriods`, `Rule30Realization.evol`, `Rule30Realization.evol_seed`.
