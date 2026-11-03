---
Template: ComputationalEssay
Name: The universal healing bound for rule 30
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-03
Description: A partial result proved in core Lean: for every background orbit of rule 30 and every change confined to the right half-line at time 0, the evolution agrees with the background below an explicit recruitment frontier, so damage moves left no faster than the frontier itself, and on average no faster than one minus the frontier's mean climb rate where that mean exists (it does for periodic backgrounds).
Abstract: See abstract.txt.
Keywords: [rule 30, Rule 30 Prize, damage spreading, light cone, masking, background, ether, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[Tisseur, Cellular automata and Lyapunov exponents, section 3.1](https://arxiv.org/abs/math/0312136)", "[Bagnoli, Rechtman and Ruffo, section 2](https://arxiv.org/abs/cond-mat/9811159)"]
---

## The question

Rule 30 updates each cell from itself and its two neighbours: the new colour is *left* XOR (*centre* OR *right*). Take
any evolution of the whole line, the **background** E (periodic, like an ether, or not), and change it anywhere on the
right half-line $x \ge 0$ at time 0. How fast can the change spread to the left?

The light cone allows one cell per tick. Rule 30 does better, because a black centre hides its right neighbour: OR with
1 is 1, whatever arrives from the right. This essay makes that masking into an exact, universal agreement certificate,
and proves it in Lean for every background at once.

## The recruitment frontier

Index cells by their **diagonal** $k = x + t$. At time 0 the background is known on the diagonals $k \le -1$. Define

$$K(0) = -1, \qquad K(t+1) = \begin{cases} K(t) + 1 & \text{if } E(t, K(t) - t) \text{ is black,} \\ K(t) & \text{otherwise.} \end{cases}$$

**Theorem (`healing_bound`).** If $E$ and $G$ are rule-30 evolutions of the whole line with $G(0, x) = E(0, x)$ for every
$x \le -1$, then $G(t, x) = E(t, x)$ for every cell with $x + t \le K(t)$.

The induction has two cases.
- **Off the new diagonal.** A cell with $x + t + 1 \le K(t)$ at time $t + 1$ reads three cells of time $t$ on known
  diagonals, so it agrees.
- **The recruited diagonal.** When the newest known cell $E(t, K(t) - t)$ is black, the same cell one tick later
  (column $K(t) - t$, time $t + 1$, which lies on the next diagonal) reads that black centre and an unknown right
  neighbour. The OR is 1 either way, so its value is the background's.

Hence the leftmost cell where $G$ differs from $E$ at time $t$ lies at $x \ge K(t) - t + 1$ (`front_ge`). The frontier
never falls and climbs at most one diagonal per tick (`K_succ_bounds`). So damage moves left no faster than the
frontier $K(t) - t + 1$. When the frontier's climb rate has a long-run mean, which it does for a periodic background,
the leftward speed is at most one minus that mean. For a general background no such mean need exist.

## A picture: the classic ether with a random right half

The background is the kit's classic ether (`Rule30Ether`: period 7 in space, 4 in time). The row keeps it on $x < 0$
and is random on $x \ge 0$. One curve is the bound $K(t) - t + 1$, the other the leftmost difference actually present. The finite row wraps around, so the leftmost difference is searched only inside the cone the wrap cannot yet
have reached.

```wl
etherTable = {{0,0,1,1},{0,1,1,0},{1,1,0,1},{0,1,0,1},{0,0,1,1},{0,0,0,1},{0,0,0,1}};
ether[j_, phi_] := etherTable[[Mod[j, 7] + 1, Mod[phi, 4] + 1]];
SeedRandom[30]; lo = -260; hi = 139; tmax = 120;
row0 = Table[If[x < 0, ether[x, 0], RandomInteger[]], {x, lo, hi}];
diff = BitXor[CellularAutomaton[30, row0, tmax], Table[ether[x, t], {t, 0, tmax}, {x, lo, hi}]];
kFront = FoldList[If[ether[#1 - #2, #2] == 1, #1 + 1, #1] &, -1, Range[0, tmax - 1]];
leftmost[t_] := First[Select[Range[lo + t + 1, hi - t - 1], diff[[t + 1, # - lo + 1]] == 1 &, 1], Missing[]];
ListLinePlot[{Table[{t, kFront[[t + 1]] - t + 1}, {t, 0, tmax}], Table[{t, leftmost[t]}, {t, 0, tmax}]},
  AxesLabel -> {"t", "x"}, PlotLegends -> {"bound K(t) - t + 1", "leftmost difference"}, ImageSize -> 480]
```

The theorem guarantees that the leftmost difference never lies below the bound. The bound does not depend on the
perturbation: over each cycle it falls by 7/12 of a cell per tick on average, the classic ether's rate below, and it
reaches $x = -69$ at $t = 120$. The actual
leftmost difference can fall much less. The bound is a guarantee for every perturbation, not the speed of any one.

## The rates for some periodic backgrounds

For a periodic background the frontier is a walk on the background's space-time torus. It enters a cycle, and its
climb rate has an exact cycle mean, computable, as does the leftward bound $1 - \text{rate}$. We replayed the walk at every phase. These rates are
computed, not part of the Lean module.

| background (ring word) | leftward bound on damage speed |
|---|---|
| G8 (`1000`) | 1/2 |
| classic ether (`1000000`) | 7/12 |
| `1010000` | 2/9 |
| `100100000` | 1/2 |
| `100100000000` | 7/17 |

Each value is the same at every phase. These are upper bounds on the speed of any damage, not the speed of a particular
perturbation. For a single black edge inserted into the classic ether the actual speed is 0, a separate result.

## Related work and what is new

- **Literature.** Tisseur (section 3.1) studies exactly such half-line perturbations: the sets of rows agreeing on a
  half-line, and uniform finite-time propagation maps, with asymptotic results of a different, measure-theoretic kind.
  Bagnoli, Rechtman and Ruffo (section 2) use Boolean derivatives for single defects; their local derivative test
  contains the vanishing dependence behind a black centre.
- **The kit.** Related statements have different hypotheses or conclusions: the radius-one cone
  (`Rule30LightCone.evol_window`, `Rule30ZeroBoundaryBarriers.evol_local_le`), rightmost-difference propagation
  (`Rule30CoupledEmptyRight.evol_diff_front`), the local masking step (`Rule30MaskedJen.left_of_black`), and special
  zero-boundary stripes (`Rule30ZeroBoundaryStripe`).
- **The portal.** [R30-20261103-ea30e7](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-ea30e7)
  (kit pull request 98) proves `evol_flip_rightmost_iff`: flipping only the rightmost cell of a light cone changes its
  apex exactly when the cells along the cone's right edge, just inside it, are all white. It is the same masking for one
  flipped cell at the cone's edge, with an exact answer at the apex. Here every right-half change is covered at once,
  over any background, below an explicit frontier.
- **New here.** The explicit recurrence $K$ for an arbitrary background orbit, and agreement below it for all right-tail
  changes at once, proved by induction and kernel-checked. No single-defect linearisation, random model or periodicity
  is assumed. Masking itself is classical.
- **Scope.** Rule 30 on the whole line; nothing here concerns the centre column of the single-cell pattern or the Prize
  problems themselves.

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and `Rule30Jen` (for `rule`) at the
verifier's kit commit 93d98bbe. The proof is one induction on time with two cases, plus `omega`.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30Jen

/-!
# Rule 30: the universal healing bound

For any rule-30 evolution `E` of the whole line (a background orbit, periodic or not) and any rule-30 evolution `G` that
agrees with `E` at time 0 on the columns `x ≤ -1`, define the **recruitment frontier** `K t` on diagonals `x + t`:
`K 0 = -1`, and `K (t + 1) = K t + 1` if the background cell `E t (K t - t)` is black, else `K t`.

* `healing_bound`: `G` agrees with `E` at every cell on a diagonal `x + t ≤ K t`. A black centre masks its right
  neighbour, so a diagonal whose newest known cell is black is recruited at the next tick.
* `front_ge`: the leftmost disagreement at time `t` lies at `x ≥ K t - t + 1`. Where the frontier's climb rate has a
  long-run mean (for a periodic background, the cycle mean of a finite walk on its torus), damage moves left at most at
  one minus that mean.
* `K_succ_bounds`: the frontier never falls and climbs at most one diagonal per tick.

Scope: any background orbit and any perturbation confined to `x ≥ 0` at time 0. Nothing here concerns the centre column of
the single-cell pattern or the Prize problems themselves.
-/

namespace Rule30Submission
open Ruliology.CellularAutomata
open Rule30Jen

/-- A rule-30 evolution of the whole line. -/
def IsR30Z (G : Nat → Int → Bool) : Prop :=
  ∀ t x, G (t + 1) x = rule (G t (x - 1)) (G t x) (G t (x + 1))

/-- The recruitment frontier of the background `E`, a diagonal index (`x + t`). -/
def K (E : Nat → Int → Bool) : Nat → Int
  | 0 => -1
  | t + 1 => if E t (K E t - t) then K E t + 1 else K E t

/-- **The universal healing bound.** -/
theorem healing_bound {E G : Nat → Int → Bool} (hE : IsR30Z E) (hG : IsR30Z G) (h0 : ∀ x, x ≤ -1 → G 0 x = E 0 x) :
    ∀ t x, x + t ≤ K E t → G t x = E t x := by
  intro t
  induction t with
  | zero => intro x hx; exact h0 x (by simpa [K] using hx)
  | succ t ih =>
    intro x hx
    rw [hG, hE]
    by_cases hin : x + (t : Int) + 1 ≤ K E t
    · rw [ih (x - 1) (by omega), ih x (by omega), ih (x + 1) (by omega)]
    · -- the recruited diagonal: x = K t - t and the background centre is black
      have hK : K E (t + 1) = (if E t (K E t - t) then K E t + 1 else K E t) := rfl
      cases hc : E t (K E t - t) with
      | false =>
        rw [hK, hc] at hx
        simp at hx
        omega
      | true =>
        rw [hK, hc] at hx
        simp at hx
        have hx' : x = K E t - t := by omega
        have hcen : G t x = E t x := ih x (by omega)
        have hcb : E t x = true := by rw [hx']; exact hc
        rw [ih (x - 1) (by omega), hcen, hcb]
        simp [rule]

/-- Hence the leftmost cell where `G` differs from `E` at time `t` lies at `x ≥ K t - t + 1`. -/
theorem front_ge {E G : Nat → Int → Bool} (hE : IsR30Z E) (hG : IsR30Z G) (h0 : ∀ x, x ≤ -1 → G 0 x = E 0 x)
    (t : Nat) (x : Int) (hne : G t x ≠ E t x) : K E t - t + 1 ≤ x := by
  by_cases h : x + (t : Int) ≤ K E t
  · exact absurd (healing_bound hE hG h0 t x h) hne
  · omega

/-- The frontier never falls and climbs at most one diagonal per tick. -/
theorem K_succ_bounds (E : Nat → Int → Bool) (t : Nat) : K E t ≤ K E (t + 1) ∧ K E (t + 1) ≤ K E t + 1 := by
  show K E t ≤ (if E t (K E t - t) then K E t + 1 else K E t) ∧ (if E t (K E t - t) then K E t + 1 else K E t) ≤ K E t + 1
  cases E t (K E t - t) <;> simp <;> omega

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The three headlines, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30Jen"};
heads = {"healing_bound", "front_ge", "K_succ_bounds"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
show[heads, "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The frontier and the whole-line rule, as defined in the module:

```wl
show[{"K", "IsR30Z"}, "TermForm"]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it
resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.healing_bound"]["KernelCheck"]
```
