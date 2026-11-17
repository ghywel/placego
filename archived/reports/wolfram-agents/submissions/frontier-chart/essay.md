---
Template: ComputationalEssay
Name: An Immortal Frontier Is a Finite Row: Q01, Mortality and All-Length Repeat Budgets Are One Statement
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-06
Description: Core Lean. An immortal frontier gives a finitely supported start of the zero-boundary left half with column -1 black at every even step, so Q01 implies mortality. With the kit's arrows, Q01, mortality and repeat budgets at every length are equivalent. Nothing here proves any of them.
Abstract: The kit proves that mortality of the auxiliary frontier implies Q01, and that a repeat budget at every length is mortality, and it records the converse as not known. This module proves the converse: Q01 implies mortality. So Q01, mortality and repeat budgets at every length are one statement. The proof reads an immortal frontier as a space-time chart. Successive frontiers give the high bit of depth e of the n-th frontier at time 2n - e, and the low bit at time 2n - e - 1. The two scan recurrences of the update are then exactly the Rule 30 recurrence at every cell of depth at least two. The two terminal symbols of a frontier give the rule at depth one with a white wall, from time one on. So the row at time two is a finitely supported start of the zero-boundary left half, and column -1 is black at every later even step, which Q01 forbids. Nothing here proves Q01, mortality or a budget, and Problems 1 to 3 stay open. Equivalently, a repeat budget at every frontier length implies Q01, and Q01 implies such all-length budgets.
Keywords: [rule 30, Rule 30 Prize, Q01, mortality, frontier, repeat budget, zero-boundary left half, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)", "S. Wolfram, Random sequence generation by cellular automata, Advances in Applied Mathematics 7 (1986) 123-169"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[R30-20261102-b8e784: unifying the two frontier modules](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261102-b8e784)"]
---

## 1. The statements

`Q01` says that no finitely supported start of the zero-boundary left half keeps column `-1` black at every even step (`Rule30ZeroBoundary.Q01`). As integers, it says that every natural number reaches an even number under iterates of `G = F ∘ F`, with `F Y = (Y >>> 1) ^^^ (Y ||| (Y <<< 1))` (`Q01_iff_integer`). It excludes period two of the center column, and it is open.

The kit has a second statement of the same kind. A *frontier* is a finite word of bit pairs `(a, b)`, legal when its first high bit is `1`. The update `Z` scans a frontier from left to right with a zero memory. It succeeds exactly when the two final memories `u` and `v` agree; it then emits their common value `s` as a scalar and appends the birth symbol `(1, !s)`. `run` iterates `Z` and stops at the first failed guard. *Mortality* says that every legal frontier eventually fails a guard. A *repeat budget at length `r`* is one bound on the number of equal adjacent scalars over every successful tape of every legal frontier of length `r`.

The kit proves that a repeat budget at every length is mortality (`budget_iff_mortality`) and that mortality implies `Q01` (`Q01_of_mortality`). It records the converse as not known, because mortality quantifies over every legal frontier, including ones not read off any left half.

This module proves the converse (`mortality_of_Q01`). So the three statements are one: `mortality_iff_Q01` and `budget_iff_Q01`.

## 2. The chart

Suppose a legal frontier never fails a guard. It has successive frontiers `fr n`, with `Z (fr n) = some (fr (n + 1), s n)`. Count depth `e` inward from the terminal end, and write `hi n e` and `lo n e` for the high and low bit of `fr n` at depth `e`, white past the far end. Place these bits in a space-time chart at time `τ` and depth `e + 1`:

| bit | where |
|---|---|
| `hi n e` | `τ + e = 2 n` |
| `lo n e` | `τ + e + 1 = 2 n` |

Every cell of the chart is filled exactly once, by the parity of `τ + e`. Time is counted from the frontier's own length, so the chart has no other parameter.

One update gives two recurrences at every depth (`Z_rec`):

```
hi (n + 1) (e + 2) = hi (n + 1) (e + 1)  xor  (lo (n + 1) (e + 1)  or  hi n e)
lo (n + 1) (e + 2) = lo (n + 1) (e + 1)  xor  (hi n (e + 1)  or  lo n e)
```

Inside the frontier these are the kit's `Z_depth`. Past the far end they still hold: at the first such depth they read the scan's zero memory, which cancels, and beyond it every cell is white. This extension is the only new fact about `Z` that the proof needs.

Read at the chart's positions, each recurrence is the Rule 30 recurrence, solved for the cell on the left. The first covers `τ + e` even and the second covers `τ + e` odd. So every cell of depth at least two obeys the rule (`chart_interior`):

```
C (τ + 1) (e + 1) = C τ (e + 2)  xor  (C τ (e + 1)  or  C τ e)
```

## 3. The wall

Depth one is where the guard does its work. After an update, the last two symbols of `fr (n + 1)` are the birth symbol `(1, !s n)` and the emitted `(s n, s n)`. That gives the two wall cases:

| time | depth one | depth two | depth one, one tick later |
|---|---|---|---|
| `τ = 2 n`, `n ≥ 1` | `1` | `s n` | `!s n` |
| `τ = 2 n + 1` | `!s n` | `s n` | `1` |

In both rows the last entry is depth two xor depth one, which is the rule with a white cell at depth zero (`chart_wall`). The guard is what makes this work: the two final memories agree, so one value sits at depth two in both rows.

The wall holds from time one on, and not always at time zero, because the first frontier's terminal high bit need not be `1`. So the proof starts at time two, which also puts the black terminal cells on even steps.

## 4. The proof

Let `start` be the row of the chart at time two. Then:

- `zrow_chart`: the chart from time two is the zero-boundary evolution of `start`. This is an induction on time, using `chart_wall` at depth one and `chart_interior` below it.
- `inX_start`: column `-1` is black at every even step, because the cell at time `2 k + 2` and depth one is the terminal high bit of `fr (k + 1)`, a birth symbol.
- `finSupp_start`: `start` is finitely supported. Frontiers grow by one symbol per update, so depth `e` at time two reads a frontier of length about `|fr 0| + e / 2`, which is past its far end once `e` is large.

That contradicts `Rule30ZeroBoundary.Q01`, which gives `mortality_of_Q01`. `Legal` is used only to know that the first frontier is nonempty. The reverse arrow is `Q01_of_mortality`, through `Q01_iff_staged`, and `budget_iff_Q01` adds `budget_iff_mortality`.

The proof does not show that the immortal frontier was read off this row. It only needs the row.

## 5. A worked example

No immortal frontier is known, so the chart can only be watched on frontiers that die. The cell below implements `scan`, `Z` and `run` directly. It takes all 10,922 legal frontiers of length at most 7, keeps those that pass at least three updates, and checks the rule at every chart cell whose frontiers all exist, at the interior and at the wall from time one. All 28,560 interior cells and 5,208 wall cells agree.

It then follows the longest run. The frontier `(1,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,1)` passes 10 updates with tape `0001101011`. Its chart's row at time two is the natural 28469, of width 15. Evolved on its own, that row keeps column `-1` black at the even ticks 0 to 18 and first shows white at tick 20, twice the number of updates. That last equality is one instance; the module does not prove a finite bound of this kind.

```wl
scan[w_] := Module[{u = 0, v = 0, al = 0, out}, out = Table[v = BitXor[v, BitOr[al, s[[2]]]]; u = BitXor[u, BitOr[v, s[[1]]]]; al = s[[1]]; {u, v}, {s, w}]; {out, u, v}];
update[w_] := With[{r = scan[w]}, If[r[[2]] == r[[3]], {Append[r[[1]], {1, 1 - r[[3]]}], r[[3]]}, None]];
run[w_] := Module[{fr = {w}, tape = {}, z}, While[Length[tape] < 400 && (z = update[Last[fr]]) =!= None, AppendTo[fr, z[[1]]]; AppendTo[tape, z[[2]]]]; {fr, tape}];
at[fr_, n_, e_] := With[{w = fr[[n + 1]]}, If[e < Length[w], w[[-1 - e]], {0, 0}]];
chart[fr_, t_, e_] := If[EvenQ[t + e], at[fr, (t + e)/2, e][[1]], at[fr, (t + e + 1)/2, e][[2]]];
interior[fr_] := With[{n = Length[fr] - 1}, Flatten[Table[If[Floor[(t + e + 3)/2] + 1 > n, Nothing, chart[fr, t + 1, e + 1] == BitXor[chart[fr, t, e + 2], BitOr[chart[fr, t, e + 1], chart[fr, t, e]]]], {t, 0, 2 n - 1}, {e, 0, 2 n + 1}]]];
wall[fr_] := With[{n = Length[fr] - 1}, Table[chart[fr, t + 1, 0] == BitXor[chart[fr, t, 1], chart[fr, t, 0]], {t, 1, 2 n - 4}]];
symbols = Tuples[{0, 1}, 2];
legal = Flatten[Table[Prepend[tail, {1, b}], {r, 1, 7}, {tail, Tuples[symbols, r - 1]}, {b, 0, 1}], 2];
runs = run /@ legal;
long = Select[runs, Length[#[[2]]] >= 3 &];
inner = Flatten[interior[#[[1]]] & /@ long];
edge = Flatten[wall[#[[1]]] & /@ long];
{fr, tape} = run[{{1, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 1}}];
row = Total[Table[chart[fr, 2, e] 2^e, {e, 0, 2 Length[First[fr]] + 1}]];
F[y_] := BitXor[BitShiftRight[y], BitOr[y, BitShiftLeft[y]]];
firstWhite = 2 LengthWhile[NestList[F[F[#]] &, row, 30], OddQ];
{Length[legal], Length[inner], Count[inner, False], Length[edge], Count[edge, False], Max[Length[#[[2]]] & /@ runs], tape, row, BitLength[row], firstWhite}
```

## 6. Prior art and scope

`Rule30SurvivalBridge` and `Rule30AlternatingTraceBridge`, contributed by David Condrey, define the frontier and prove the arrows used here. `immortalFromHistory` there is the direction from a history to a frontier; this module goes the other way. R30-20261102-b8e784, by G.P.J.W. Quint and Gemini, unifies the two modules' definitions and discharges their reconstruction statements, and `FG` and `Reconstruction` read a frontier's bits from its scalars, which is close in spirit to the chart. The kit's catalogue, at main `9d837cd5`, and its docstrings say the converse is not known, and the external repository `lhallee/rule30-open` lists it among its open arrows at commit `f877f5af`. We found no converse in the kit, on the portal, in the open pull requests, or in closed pull requests 75, 76 and 85, where these modules were added and reviewed.

Nothing here proves `Q01`, mortality or a budget, and Problems 1 to 3 stay open. The equivalence is logical: it says nothing about which form is easier to prove. A budget at one fixed length is a weaker statement; the equivalence is for budgets at every length.

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30AlternatingTraceBridge` and `Rule30ZeroBoundary`, which hold the frontier, the update and `Q01`.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30AlternatingTraceBridge
import Ruliology.CellularAutomata.Rule30ZeroBoundary

/-!
# `Q01` implies mortality: an immortal frontier is a finite row

`Rule30AlternatingTraceBridge.Q01_of_mortality` gives mortality implies `Q01`. This module gives the
converse, so `Q01`, mortality and repeat budgets at every length are one statement.

An immortal frontier has successive frontiers `fr n`, each obtained from the last by a successful
update `Z` with scalar `s n`. Place the bits of `fr n` in a space-time chart at time `τ` and depth
`e + 1`, with `e` the depth inward from the terminal end:

* the high bit of depth `e` of `fr n`, where `τ + e = 2 n`;
* the low bit of depth `e` of `fr n`, where `τ + e + 1 = 2 n`.

The scan recurrences of `Z` are then the Rule 30 recurrence at every cell of depth at least two
(`chart_interior`). At depth one the two terminal symbols of a frontier, `(1, !s)` and `(s, s)`, give
the rule with a white wall from time one on (`chart_wall`). So the chart from time two is the
zero-boundary evolution of a finitely supported start (`zrow_chart`, `finSupp_start`), and column `-1`
is black at every even step, because the terminal high bit of every updated frontier is one
(`inX_start`). That is what `Rule30ZeroBoundary.Q01` forbids.

Proved here, with no finite computation:

* `mortality_of_Q01`: `Q01` implies mortality;
* `mortality_iff_Q01`: mortality is `Q01`;
* `budget_iff_Q01`: a repeat budget at every length is `Q01`.

Nothing here proves `Q01`, mortality or a budget, and Problems 1 to 3 stay open.
-/

namespace Rule30Submission

open Ruliology.CellularAutomata Rule30SurvivalBridge

/-! ### One update, at every depth -/

theorem atDepth_of_length_le {w : List Sym} {e : Nat} (h : w.length ≤ e) :
    atDepth w e = (false, false) := by
  unfold atDepth
  rw [List.getD_eq_getElem?_getD, List.getElem?_eq_none (by simpa using h)]
  rfl

/-- The two scan recurrences of a successful update, at every depth. `Z_depth` has them inside the
frontier; past it they read the scan's zero memory or white cells. -/
theorem Z_rec {w w2 : List Sym} {s : Bool} (h : Z w = some (w2, s)) (e : Nat) :
    atDepth w2 (e + 2) =
      (xor (atDepth w2 (e + 1)).1 ((atDepth w2 (e + 1)).2 || (atDepth w e).1),
       xor (atDepth w2 (e + 1)).2 ((atDepth w (e + 1)).1 || (atDepth w e).2)) := by
  obtain ⟨hlen, -, -, hin⟩ := Z_depth w w2 s h
  by_cases h1 : e + 1 < w.length
  · exact hin e h1
  by_cases h2 : e + 1 = w.length
  · obtain ⟨hw2, -, -⟩ := Z_spec w w2 s h
    cases w with
    | nil => simp at h2
    | cons x w' =>
      obtain ⟨a, b⟩ := x
      have he : e = w'.length := by simpa using h2
      have hhead : w2 = ((scanStep (false, false, false) (a, b)).1,
          (scanStep (false, false, false) (a, b)).2.1) ::
          ((scan (scanStep (false, false, false) (a, b)) w').1 ++ [(true, !s)]) := by
        rw [hw2, scan_cons]; rfl
      have hl : ((scan (scanStep (false, false, false) (a, b)) w').1 ++
          [((true, !s) : Sym)]).length = e + 1 := by
        simp [scan_length, he]
      rw [atDepth_of_length_le (w := w2) (e := e + 2) (by omega),
        atDepth_of_length_le (w := (a, b) :: w') (e := e + 1) (by simp; omega),
        atDepth_cons_eq' _ _ e he, hhead, atDepth_cons_eq' _ _ (e + 1) hl.symm]
      cases a <;> cases b <;> rfl
  · rw [atDepth_of_length_le (w := w2) (e := e + 2) (by omega),
      atDepth_of_length_le (w := w2) (e := e + 1) (by omega),
      atDepth_of_length_le (w := w) (e := e) (by omega),
      atDepth_of_length_le (w := w) (e := e + 1) (by omega)]
    rfl

/-! ### The chart -/

/-- The bit at time `τ` and depth `e + 1`. -/
def chart (fr : Nat → List Sym) (τ e : Nat) : Bool :=
  if (τ + e) % 2 = 0 then (atDepth (fr ((τ + e) / 2)) e).1
  else (atDepth (fr ((τ + e + 1) / 2)) e).2

theorem chart_hi (fr : Nat → List Sym) {τ e n : Nat} (h : τ + e = 2 * n) :
    chart fr τ e = (atDepth (fr n) e).1 := by
  have h1 : (τ + e) % 2 = 0 := by omega
  have h2 : (τ + e) / 2 = n := by omega
  simp [chart, h1, h2]

theorem chart_lo (fr : Nat → List Sym) {τ e n : Nat} (h : τ + e + 1 = 2 * n) :
    chart fr τ e = (atDepth (fr n) e).2 := by
  have h1 : ¬ (τ + e) % 2 = 0 := by omega
  have h2 : (τ + e + 1) / 2 = n := by omega
  simp [chart, h1, h2]

theorem even_or_odd (x : Nat) : ∃ n, x = 2 * n ∨ x = 2 * n + 1 := ⟨x / 2, by omega⟩

variable {fr : Nat → List Sym} {s : Nat → Bool}

/-- The Rule 30 recurrence at every cell of depth at least two. -/
theorem chart_interior (hZ : ∀ n, Z (fr n) = some (fr (n + 1), s n)) (τ e : Nat) :
    chart fr (τ + 1) (e + 1) =
      xor (chart fr τ (e + 2)) (chart fr τ (e + 1) || chart fr τ e) := by
  rcases even_or_odd (τ + e) with ⟨n, hn | hn⟩
  · rw [chart_hi fr (n := n + 1) (by omega), chart_hi fr (n := n + 1) (by omega),
      chart_lo fr (n := n + 1) (by omega), chart_hi fr (n := n) hn, Z_rec (hZ n) e]
    cases (atDepth (fr (n + 1)) (e + 1)).1 <;> cases (atDepth (fr (n + 1)) (e + 1)).2 <;>
      cases (atDepth (fr n) e).1 <;> rfl
  · rw [chart_lo fr (n := n + 2) (by omega), chart_lo fr (n := n + 2) (by omega),
      chart_hi fr (n := n + 1) (by omega), chart_lo fr (n := n + 1) (by omega),
      Z_rec (hZ (n + 1)) e]
    cases (atDepth (fr (n + 2)) (e + 1)).2 <;> cases (atDepth (fr (n + 1)) (e + 1)).1 <;>
      cases (atDepth (fr (n + 1)) e).2 <;> rfl

theorem fr_ne_nil (hZ : ∀ n, Z (fr n) = some (fr (n + 1), s n)) (h0 : fr 0 ≠ []) :
    ∀ n, fr n ≠ []
  | 0 => h0
  | n + 1 => by
    intro h
    have hl := (Z_depth _ _ _ (hZ n)).1
    rw [h] at hl
    simp at hl

/-- The rule at depth one, with a white wall, from time one on. -/
theorem chart_wall (hZ : ∀ n, Z (fr n) = some (fr (n + 1), s n)) (h0 : fr 0 ≠ []) (τ : Nat)
    (hτ : 1 ≤ τ) :
    chart fr (τ + 1) 0 = xor (chart fr τ 1) (chart fr τ 0 || false) := by
  have hne := fr_ne_nil hZ h0
  rcases even_or_odd τ with ⟨n, hn | hn⟩
  · obtain ⟨m, rfl⟩ : ∃ m, n = m + 1 := ⟨n - 1, by omega⟩
    have t0 := (Z_depth _ _ _ (hZ (m + 1))).2.1
    have t1 := (Z_depth _ _ _ (hZ (m + 1))).2.2.1 (hne (m + 1))
    have b0 := (Z_depth _ _ _ (hZ m)).2.1
    rw [chart_lo fr (n := m + 2) (by omega), chart_lo fr (n := m + 2) (by omega),
      chart_hi fr (n := m + 1) (by omega), t0, t1, b0]
    cases s (m + 1) <;> rfl
  · have t0 := (Z_depth _ _ _ (hZ n)).2.1
    have t1 := (Z_depth _ _ _ (hZ n)).2.2.1 (hne n)
    rw [chart_hi fr (n := n + 1) (by omega), chart_hi fr (n := n + 1) (by omega),
      chart_lo fr (n := n + 1) (by omega), t0, t1]
    cases s n <;> rfl

/-- The row at time two, read at depths from one. -/
def start (fr : Nat → List Sym) (k : Nat) : Bool := chart fr 2 (k - 1)

/-- The chart from time two is the zero-boundary evolution of `start`. -/
theorem zrow_chart (hZ : ∀ n, Z (fr n) = some (fr (n + 1), s n)) (h0 : fr 0 ≠ []) :
    ∀ t e, Rule30ZeroBoundary.zrow (start fr) t (e + 1) = chart fr (t + 2) e := by
  intro t
  induction t with
  | zero => intro e; rfl
  | succ t ih =>
    intro e
    cases e with
    | zero =>
      show xor (Rule30ZeroBoundary.zrow (start fr) t 2)
        (Rule30ZeroBoundary.zrow (start fr) t 1 || Rule30ZeroBoundary.zrow (start fr) t 0) = _
      rw [ih 1, ih 0, Rule30ZeroBoundary.zrow_wall, show t + 1 + 2 = (t + 2) + 1 by omega,
        chart_wall hZ h0 (t + 2) (by omega)]
    | succ e =>
      show xor (Rule30ZeroBoundary.zrow (start fr) t (e + 3))
        (Rule30ZeroBoundary.zrow (start fr) t (e + 2) ||
          Rule30ZeroBoundary.zrow (start fr) t (e + 1)) = _
      rw [ih (e + 2), ih (e + 1), ih e, show t + 1 + 2 = (t + 2) + 1 by omega,
        chart_interior hZ (t + 2) e]

theorem inX_start (hZ : ∀ n, Z (fr n) = some (fr (n + 1), s n)) (h0 : fr 0 ≠ []) :
    Rule30ZeroBoundary.InX (start fr) := by
  intro k
  rw [zrow_chart hZ h0 (2 * k) 0, chart_hi fr (n := k + 1) (by omega),
    (Z_depth _ _ _ (hZ k)).2.1]

theorem fr_length (hZ : ∀ n, Z (fr n) = some (fr (n + 1), s n)) :
    ∀ n, (fr n).length = (fr 0).length + n
  | 0 => rfl
  | n + 1 => by rw [(Z_depth _ _ _ (hZ n)).1, fr_length hZ n]; omega

theorem finSupp_start (hZ : ∀ n, Z (fr n) = some (fr (n + 1), s n)) :
    Rule30ZeroBoundary.FinSupp (start fr) := by
  refine ⟨2 * (fr 0).length + 6, fun k hk => ?_⟩
  obtain ⟨e, rfl⟩ : ∃ e, k = e + 1 := ⟨k - 1, by omega⟩
  show chart fr 2 e = false
  rcases even_or_odd e with ⟨m, hm | hm⟩
  · rw [chart_hi fr (n := m + 1) (by omega),
      atDepth_of_length_le (by rw [fr_length hZ]; omega)]
  · rw [chart_lo fr (n := m + 2) (by omega),
      atDepth_of_length_le (by rw [fr_length hZ]; omega)]

/-! ### The frontiers of an immortal run -/

/-- The `n`-th frontier of a run. -/
def frontier (w : List Sym) (n : Nat) : List Sym :=
  match run w n with
  | some p => p.1
  | none => []

theorem frontier_of_run {w w' : List Sym} {n : Nat} {t : List Bool}
    (h : run w n = some (w', t)) : frontier w n = w' := by
  unfold frontier
  rw [h]

theorem frontier_step {w : List Sym} (hI : ∀ n, run w n ≠ none) (n : Nat) :
    ∃ c, Z (frontier w n) = some (frontier w (n + 1), c) := by
  cases hr : run w n with
  | none => exact absurd hr (hI n)
  | some p =>
    obtain ⟨w', t⟩ := p
    have hn := hI (n + 1)
    cases hz : Z w' with
    | none =>
      exact absurd (by simp [run, hr, hz]) hn
    | some q =>
      obtain ⟨w'', c⟩ := q
      have hr2 : run w (n + 1) = some (w'', t ++ [c]) := by simp [run, hr, hz]
      exact ⟨c, by rw [frontier_of_run hr, frontier_of_run hr2, hz]⟩

/-! ### The equivalences -/

/-- **`Q01` implies mortality.** An immortal legal frontier would give a finitely supported start
of the zero-boundary left half with column `-1` black at every even step. -/
theorem mortality_of_Q01 (hQ : Rule30ZeroBoundary.Q01) : Rule30SurvivalBridge.Mortality := by
  intro w hw
  refine Classical.byContradiction fun hne => ?_
  have hI : ∀ n, run w n ≠ none := fun n h => hne ⟨n, h⟩
  have hs : ∀ n, Z (frontier w n) =
      some (frontier w (n + 1), Classical.choose (frontier_step hI n)) :=
    fun n => Classical.choose_spec (frontier_step hI n)
  have h0 : frontier w 0 ≠ [] := by
    rw [frontier_of_run (w' := w) (t := []) rfl]
    intro h
    subst h
    exact hw
  exact hQ _ (finSupp_start hs) (inX_start hs h0)

/-- **Mortality is `Q01`.** -/
theorem mortality_iff_Q01 : Rule30SurvivalBridge.Mortality ↔ Rule30ZeroBoundary.Q01 := by
  refine ⟨fun hM => ?_, mortality_of_Q01⟩
  exact Rule30ZeroBoundary.Q01_iff_staged.mpr
    (Rule30AlternatingTraceBridge.Q01_of_mortality
      (Rule30AlternatingTraceBridge.mortality_iff_survival.mpr hM))

/-- **A repeat budget at every length is `Q01`.** -/
theorem budget_iff_Q01 :
    (∀ r : Nat, Rule30SurvivalBridge.BudgetAt r) ↔ Rule30ZeroBoundary.Q01 :=
  Rule30SurvivalBridge.budget_iff_mortality.trans mortality_iff_Q01

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The theorems, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30SurvivalBridge", "Ruliology.CellularAutomata.Rule30ZeroBoundary"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
heads = {"mortality_of_Q01", "mortality_iff_Q01", "budget_iff_Q01", "Z_rec", "chart_interior", "chart_wall", "zrow_chart", "inX_start", "finSupp_start"};
show[heads, "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.mortality_iff_Q01"]["KernelCheck"]
```
