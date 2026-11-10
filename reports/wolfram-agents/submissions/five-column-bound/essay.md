---
Template: ComputationalEssay
Name: A Sharp Black-Count Bound on Five Adjacent Columns of Every Rule 30 Trajectory
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-10
Description: Core Lean. Every five adjacent Rule 30 columns contain at most 3T + 2 black cells during any interval of T ticks. A bounded potential gives the exact endpoint telescope and both constants are sharp.
Abstract: In core Lean 4.35.0 we prove that any five adjacent physical columns of any Rule 30 trajectory contain at most 3T + 2 black cells during any interval of T ticks. There is no assumption on the initial configuration or the starting time. For a five-cell word u, let H(u) be the maximum of zero and two minus the black population of its four rightmost cells. A finite Boolean check proves pop(u) - 3 <= H(v) - H(u) whenever v is the next window, with both exterior input cells arbitrary. Summing gives the stronger endpoint bound C5 <= 3T + H(final) - H(initial), and H lies between zero and two. Consequently the same window contains at least 2T - 2 white cells. Both constants are sharp: an all-black window requires the additive two at T = 1, and the fixed alternating row has three black cells in a suitable five-column window at every tick. We specialize the bound to the kit's arbitrary-row evolution and official singleton diagram. The result controls a sum over five columns; it gives no upper-density bound for an individual column, no positive black-density lower bound, and no solution of a prize problem.
Keywords: [rule 30, Rule 30 Prize, adjacent columns, black count, potential, telescope, sharp bound, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)"]
---

## 1. The statement

Take any initial configuration on the integer line, evolve it by the official rule `new(i) = old(i-1) xor (old(i) or old(i+1))`, and fix any five adjacent physical columns. In any interval of `T` ticks they contain at most `3T + 2` black cells (`evol_five_column_bound`). The interval includes its first row and excludes its final endpoint. `T = 0` is allowed. The starting time is arbitrary.

The source also proves the bound for any array satisfying the Rule 30 recurrence (`five_column_bound`), and specializes it to the kit's official singleton diagram (`cell_five_column_bound`). No random-row, finite-support, periodicity or capture assumption occurs.

## 2. A short potential

For a five-cell word `u = (a,b,c,d,e)`, let `pop(u)` count black cells and put

`H(u) = max(0, 2 - (b+c+d+e))`.

The first cell is deliberately omitted from this potential. Its range is `0..2` (`potential_bounds`). On every seven-bit input word, let `u` be its middle five cells and `v` the five updated cells. Both exterior input bits are free. The local inequality is

`pop(u) - 3 <= H(v) - H(u)` (`local_potential`).

The proof checks all seven Boolean inputs in the Lean kernel. There is also a short case explanation. If the right four input cells contain zero or one black cell, the required lower bound on `H(v)` is nonpositive. With two or more, `H(u)=0`, and input population at most three is immediate. If the input has four black cells, at most one of the right four output cells is black; if all five inputs are black, those four outputs are all white. These give the required lower bounds one and two.

## 3. Telescope and sharpness

Along an actual trajectory the local inequalities telescope. Writing `C5` for the black count in the window gives

`C5 <= 3T + H(final) - H(initial)` (`telescope`).

The range of `H` then gives `C5 <= 3T + 2`. The module counts bits as integers, with black equal to one. Its separately defined white count plus black count is exactly `5T`, so the window contains at least `2T - 2` white cells (`white_column_bound`).

The additive constant two is necessary already at `T=1`: a real initial row can be all black in the five-cell window, giving count five (`sharp_constant`). The coefficient three is necessary too. The alternating row is fixed by Rule 30, and a window `10101` contains exactly three black cells at every time (`sharp_rate`, at every horizon). These are actual configurations, not just cycles of a relaxed window graph.

## 4. What the bound controls

The result is an upper bound on a sum over five columns. It proves no density limit, no positive lower density of black cells and no stronger conclusion for the singleton. In particular, the sharp alternating example has individual columns permanently black or permanently white, so the five-column statement supplies no individual-column ceiling. Neither of its sharpness examples is the finite singleton seed.

## 5. Worked numbers

The numerical cell checks all 128 seven-bit windows and counts the 70 tight inequalities. It also checks three deliberately wrong controls: the mirrored potential fails on 8 edges, replacing the potential at the all-white word by zero fails on 3 edges, and using rule 150 with the same certificate fails on 16 edges. These are illustrative checks of the finite certificate. The formal proof covers all trajectories and horizons without relying on the numerical cell.

```wl
rule30[a_,b_,c_] := BitXor[a,BitOr[b,c]];
pot[u_] := Max[0,2-Total[Rest[u]]];
damaged[u_] := If[u === ConstantArray[0,5],0,pot[u]];
words = Tuples[{0,1},7];
edges = ({Take[#, {2,6}],rule30 @@@ Partition[#,3,1]} &) /@ words;
slacks = (pot[Last[#]]-pot[First[#]]-Total[First[#]]+3 &) /@ edges;
mirror = (pot[Reverse[Last[#]]]-pot[Reverse[First[#]]]-Total[First[#]]+3 &) /@ edges;
bad = (damaged[Last[#]]-damaged[First[#]]-Total[First[#]]+3 &) /@ edges;
linear = (pot[BitXor @@@ Partition[#,3,1]]-pot[Take[#, {2,6}]]-Total[Take[#, {2,6}]]+3 &) /@ words;
neg[v_] := Count[v,x_ /; x<0];
{And @@ (#>=0 & /@ slacks),Length[slacks],Count[slacks,0],neg[mirror],neg[bad],neg[linear]}
```

## 6. Prior art and provenance

The method of summing local inequalities and telescoping a bounded potential is standard. Related results are the count-transfer bounds in [rule30-open's ColumnTransfer](https://github.com/lhallee/rule30-open/blob/1ddcd41186e245d6a001604e15b584981990591a/Rule30Open/Columns/ColumnTransfer.lean), and the source-dependent one-column bound in [kit PR253](https://github.com/WolframInstitute/Rule30PrizeKit/pull/253). They concern different observables and do not state this five-column ceiling. Earlier spin and finite-row population identities in our public record, and Cappallo's counting formula in [OEIS A070952](https://oeis.org/A070952), are context; no new version of those identities is claimed here.

The certificate came from a sub-agent run of our programme. GPT carried it independently and formalized it against the kit's actual rule and evolution definitions, and Local read the formal source. The two source forms pass the official kernel replay with nine headlines and standard axioms. This is a partial result, with no claim of literature priority or prize solution.

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30Realization`.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30Realization
/-!
# A sharp black-count ceiling on five adjacent Rule 30 columns

For every Rule 30 trajectory, five adjacent physical columns contain at most `3 * T + 2` black
cells in any interval of `T` ticks, counting its first row and not its endpoint.

The proof uses the potential `H(u) = max(0, 2 - pop(right four cells of u))`, with values in
`0..2` (`potential_bounds`). On seven Boolean input cells, `pop(u) - 3 ≤ H(v) - H(u)`, where `u`
is the middle five cells and `v` their update, with both exterior cells free (`local_potential`).
Summing along a trajectory telescopes it (`telescope`, `five_column_bound`), and the window has at
least `2 * T - 2` white cells (`white_column_bound`). `evol_five_column_bound` covers every
initial configuration and starting time, and `cell_five_column_bound` the official singleton
diagram. The constant `2` is needed at `T = 1` (`sharp_constant`), and the fixed alternating
configuration has exactly `3 * T` black cells in a window at every horizon (`sharp_rate`).

Summing local inequalities and telescoping a bounded potential is a standard method. Nothing here
bounds the density of a single column or gives a positive lower density, and Problems 1 to 3 stay
open.
-/

namespace Rule30Submission

open Ruliology.CellularAutomata

open Rule30Jen Rule30Realization

def bit (b : Bool) : Int := if b then 1 else 0

def pop5 (a b c d e : Bool) : Int := bit a + bit b + bit c + bit d + bit e

def potential (_a b c d e : Bool) : Int := max 0 (2 - (bit b + bit c + bit d + bit e))

theorem potential_bounds (a b c d e : Bool) :
    0 ≤ potential a b c d e ∧ potential a b c d e ≤ 2 := by
  cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> decide

/-- Both exterior cells are free; windows read from left to right in physical coordinates. -/
theorem local_potential (l a b c d e r : Bool) :
    pop5 a b c d e - 3 ≤
      potential (rule l a b) (rule a b c) (rule b c d) (rule c d e) (rule d e r) -
      potential a b c d e := by
  cases l <;> cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> cases r <;> decide

def weight (x : Int → Bool) (p : Int) : Int := pop5 (x p) (x (p+1)) (x (p+2)) (x (p+3)) (x (p+4))

def pot (x : Int → Bool) (p : Int) : Int := potential (x p) (x (p+1)) (x (p+2)) (x (p+3)) (x (p+4))

def count (x : Nat → Int → Bool) (p : Int) : Nat → Int
  | 0 => 0
  | t+1 => count x p t + weight (x t) p

def whiteCount (x : Nat → Int → Bool) (p : Int) : Nat → Int
  | 0 => 0
  | t+1 => whiteCount x p t + (5 - weight (x t) p)

theorem pot_bounds (x : Int → Bool) (p : Int) : 0 ≤ pot x p ∧ pot x p ≤ 2 :=
  potential_bounds _ _ _ _ _

theorem step_potential (x : Nat → Int → Bool)
    (hx : ∀ t i, x (t+1) i = rule (x t (i-1)) (x t i) (x t (i+1))) (t : Nat) (p : Int) :
    weight (x t) p - 3 ≤ pot (x (t+1)) p - pot (x t) p := by
  have h0 := hx t p
  have h1 : x (t+1) (p+1) = rule (x t p) (x t (p+1)) (x t (p+2)) := by
    rw [hx t (p+1), show p+1-1=p by omega, show p+1+1=p+2 by omega]
  have h2 : x (t+1) (p+2) = rule (x t (p+1)) (x t (p+2)) (x t (p+3)) := by
    rw [hx t (p+2), show p+2-1=p+1 by omega, show p+2+1=p+3 by omega]
  have h3 : x (t+1) (p+3) = rule (x t (p+2)) (x t (p+3)) (x t (p+4)) := by
    rw [hx t (p+3), show p+3-1=p+2 by omega, show p+3+1=p+4 by omega]
  have h4 : x (t+1) (p+4) = rule (x t (p+3)) (x t (p+4)) (x t (p+5)) := by
    rw [hx t (p+4), show p+4-1=p+3 by omega, show p+4+1=p+5 by omega]
  simpa only [weight, pot, h0, h1, h2, h3, h4] using
    local_potential (x t (p-1)) (x t p) (x t (p+1)) (x t (p+2)) (x t (p+3)) (x t (p+4)) (x t (p+5))

/-- The count includes time `0` and excludes time `T`; the exact endpoint potential is kept. -/
theorem telescope (x : Nat → Int → Bool)
    (hx : ∀ t i, x (t+1) i = rule (x t (i-1)) (x t i) (x t (i+1))) (p : Int) (T : Nat) :
    count x p T ≤ 3 * (T : Int) + pot (x T) p - pot (x 0) p := by
  induction T with
  | zero => simp [count]
  | succ t ih =>
    have h := step_potential x hx t p
    simp only [count]
    omega

theorem five_column_bound (x : Nat → Int → Bool)
    (hx : ∀ t i, x (t+1) i = rule (x t (i-1)) (x t i) (x t (i+1))) (p : Int) (T : Nat) :
    count x p T ≤ 3 * (T : Int) + 2 := by
  have h := telescope x hx p T
  have h0 := pot_bounds (x 0) p
  have hT := pot_bounds (x T) p
  omega

theorem count_partition (x : Nat → Int → Bool) (p : Int) (T : Nat) :
    whiteCount x p T + count x p T = 5 * (T : Int) := by
  induction T with
  | zero => rfl
  | succ t ih => simp only [whiteCount, count]; omega

theorem white_column_bound (x : Nat → Int → Bool)
    (hx : ∀ t i, x (t+1) i = rule (x t (i-1)) (x t i) (x t (i+1))) (p : Int) (T : Nat) :
    2 * (T : Int) - 2 ≤ whiteCount x p T := by
  have h := five_column_bound x hx p T
  have hp := count_partition x p T
  omega

/-- Every initial row, every physical window and every starting time. -/
theorem evol_five_column_bound (y : Int → Bool) (A : Nat) (p : Int) (T : Nat) :
    count (fun t => evol y (A+t)) p T ≤ 3 * (T : Int) + 2 := by
  apply five_column_bound
  intro t i
  rw [show A+(t+1)=(A+t)+1 by omega]
  rfl

/-- The official singleton diagram, without a stronger seed-specific conclusion. -/
theorem cell_five_column_bound (A : Nat) (p : Int) (T : Nat) :
    count (fun t => cell (A+t)) p T ≤ 3 * (T : Int) + 2 := by
  apply five_column_bound
  intro t i
  rw [show A+(t+1)=(A+t)+1 by omega]
  rfl

def alternating (p : Int) : Bool := decide (p % 2 = 0)

theorem rule_alternating (p : Int) :
    rule (alternating (p-1)) (alternating p) (alternating (p+1)) = alternating p := by
  by_cases h : p % 2 = 0
  · have hm : (p-1) % 2 = 1 := by omega
    have hp : (p+1) % 2 = 1 := by omega
    simp [alternating, h, hm, hp, rule]
  · have hm : (p-1) % 2 = 0 := by omega
    have hp : (p+1) % 2 = 0 := by omega
    simp [alternating, h, hm, hp, rule]

theorem evol_alternating : ∀ t p, evol alternating t p = alternating p
  | 0, p => rfl
  | t+1, p => by rw [evol, evol_alternating t (p-1), evol_alternating t p, evol_alternating t (p+1)]; exact rule_alternating p

/-- The rate `3` is attained on an actual fixed row at every horizon. -/
theorem sharp_rate (T : Nat) : count (evol alternating) 0 T = 3 * (T : Int) := by
  have he : evol alternating = fun _ => alternating := funext fun t => funext fun p => evol_alternating t p
  rw [he]
  have hw : weight alternating 0 = 3 := by decide
  induction T with
  | zero => rfl
  | succ t ih => simp only [count, hw]; omega

/-- The additive constant `2` is needed already at horizon `1`, on an actual row. -/
theorem sharp_constant : count (evol (fun _ => true)) 0 1 = 5 := by decide

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The theorems, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata", "Ruliology.CellularAutomata.Rule30Jen", "Ruliology.CellularAutomata.Rule30Realization"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
heads = {"potential_bounds", "local_potential", "telescope", "five_column_bound", "white_column_bound", "evol_five_column_bound", "cell_five_column_bound", "sharp_rate", "sharp_constant"};
show[heads, "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.five_column_bound"]["KernelCheck"]
```
