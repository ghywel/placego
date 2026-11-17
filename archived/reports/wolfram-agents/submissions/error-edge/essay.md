---
Template: ComputationalEssay
Name: The error edge of two rule 30 configurations never retreats, heals exactly at a black parent, and obeys six laws after a heal
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-05
Description: Core Lean. For any two arrays with the left-diagonal recurrence, agreement below the lowest differing wheel is kept, at an edge of index at least 1 a black parent is exactly the condition for healing, and six guarded laws constrain the new parent after a heal at an edge of index at least 2.
Abstract: Align the leftmost black cells of two rule 30 configurations and read their left diagonals as wheels. The error edge is the lowest wheel where they differ. For any two arrays satisfying the kit's left-diagonal recurrence, agreement below an edge persists, so any later edge is no lower (agree_step, agree_after, edge_le). At an edge of index at least 1, the arrays agree there one tick later exactly when its parent is black (heal_iff). A white parent preserves the edge; a black parent removes that difference, possibly leaving the arrays identical. For an old edge of index at least 2, six laws constrain the new parent after a heal and a finite jump. A jump of 2 leaves that parent white, and a jump of 3 leaves it black (jump_two, jump_three). After 4 it is black one tick later, regardless of its earlier value (jump_four). After 5 with a white new parent it becomes black one tick later (jump_five). After 6 or 7 with a white new parent it remains white one tick later (jump_six, jump_seven). Thus the last two stall conclusions need the white-parent condition. The proofs unfold the recurrence and decide Boolean identities in at most thirteen variables; the module builds in seconds. These exact local statements concern the left damage front. They make no assertion about its limiting speed, the center column or the Prize problems.
Keywords: [rule 30, Rule 30 Prize, left diagonals, damage front, difference pattern, error edge, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)", "S. Wolfram, Random sequence generation by cellular automata, Adv. Appl. Math. 7 (1986)", "S. Wolfram, A New Kind of Science (2002), p. 949"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[R30-20261103-e660e4: the universal healing bound](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-e660e4)"]
---

## 1. The object

Take two configurations of rule 30, each with a leftmost black cell, translate their leftmost cells into alignment, and read from that common left edge: wheel `j` at tick `t` is the cell at position `lo − t + j`, with `lo` the initial leftmost black cell (`Rule30FiniteDiagonals.Ld`). The wheels of a configuration satisfy the kit's left-diagonal recurrence (`Rule30AgedLeftDiagonals.Recurrence`): wheel 0 is constant, wheel 1 at tick `t + 1` is the or of wheels 0 and 1 at tick `t`, and wheel `i + 2` at tick `t + 1` is `xor (wheel i) (wheel (i + 1) || wheel (i + 2))` read at tick `t`. Everything below is proved for any two arrays `a`, `b` with this recurrence. `Rule30AgedLeftDiagonals.Ld_recurrence` gives the recurrence for a configuration that is white left of `lo`, so it holds for any two configurations with leftmost black cells, whatever lies to their right, and in particular for a configuration against a periodic strip.

Say that `a` and `b` **agree below `m`** at tick `t` when they are equal on every wheel `j < m` (`Agree a b m t`), and that their **error edge is at `m`** when they agree below `m` and differ at `m` (`Edge a b m t`). The edge is the left end of the difference pattern of the translated configurations. For difference patterns on random backgrounds, Wolfram reports an empirical average leftward speed of about 0.2428 cells per step (Grassberger's measurement), equivalent to about 0.7572 wheels per tick in this moving frame. This is not a speed assertion for every pair. The theorems here concern exact local laws, not a limiting speed.

## 2. The barrier and the heal

**The edge never retreats (`agree_step`, `agree_after`, `edge_le`).** A wheel reads only itself and the two wheels below it, so two arrays that agree below `m` at a tick agree below `m` at every later tick. Hence if the edge is at `m` at tick `t` and at `m′` at tick `t + n`, then `m ≤ m′`.

**The heal criterion (`heal_iff`).** Let the edge be at `m + 1` at tick `t`. Then `a` and `b` agree on wheel `m + 1` at tick `t + 1` if and only if wheel `m` of `a` (equally of `b`, since they agree there) is black at tick `t`. For `m = 0` this is the or of wheel 0 with the differing wheel 1; for `m ≥ 1` the differing wheel enters an or with the black parent, which absorbs it, or with a white parent, which exposes it. So with a white parent the edge is still at `m + 1` one tick later (`edge_stall`), and with a black parent the two arrays agree on every wheel through `m + 1` one tick later (`edge_heal`): if a later error edge exists, it lies strictly higher; the two arrays may instead become identical. For arbitrary recurrence arrays, a difference at wheel 0 is constant and is outside this heal criterion. For the physical anchored rows, wheel 0 is black in both, and wheel 1 is black in both from tick 1.

## 3. Six laws after a heal

Let the edge be at `m + 2` at tick `t` with its parent, wheel `m + 1`, black. The wheels above the old edge at tick `t + 1` are then constrained, whatever the two arrays carried there at tick `t`.

**`white_above`.** If wheel `m + 3` agrees at tick `t + 1`, it is white there. **`black_two_above`.** If wheels `m + 3` and `m + 4` agree at tick `t + 1`, wheel `m + 4` is black there.

Write `d` for the jump, the new edge being at `m + 2 + d`, and the **new parent** for wheel `m + 1 + d`.

| jump | law | theorem |
|---|---|---|
| 2 | the new parent is white at `t + 1` | `jump_two` |
| 3 | the new parent is black at `t + 1` | `jump_three` |
| 4 | the new parent is black at `t + 2`, whatever it was at `t + 1` | `jump_four` |
| 5 | if the new parent is white at `t + 1`, it is black at `t + 2` | `jump_five` |
| 6 | if the new parent is white at `t + 1`, it is white at `t + 2` | `jump_six` |
| 7 | if the new parent is white at `t + 1`, it is white at `t + 2` | `jump_seven` |

For these jumps, whose old edge is at least 2, the new edge stalls at least once after a jump of 2 and heals immediately after 3. After 4 or 5 it heals by the second opportunity: immediately if its new parent is black, otherwise one tick later. After 6 or 7, a white new parent forces at least two stalled updates; a black new parent instead gives an immediate heal. Here a heal may eliminate the difference entirely. Jumps of 1 and of 8 carry no such constraint at these ticks: the enumeration behind the module shows both values occur for them. It does not reach jumps above 8.

## 4. The proofs

Each law is a Boolean identity in the values of the two arrays on a window of wheels at tick `t`. Unfolding the recurrence once or twice expresses every wheel at ticks `t + 1` and `t + 2` in those values; the edge hypothesis replaces the values of `b` below the edge by those of `a` and the value at the edge by its complement; and the identity is decided by Lean's `decide` over the remaining free Boolean variables, at most thirteen of them for `jump_seven`. The module has no literals and no computation beyond these decisions, and it builds in about a second; the kit's `Check` replays its constants with the standard axioms `propext` and `Quot.sound`.

## 5. What these laws are for

The error edge is the damage front of rule 30 seen from a single configuration: the lowest wheel on which a configuration differs from a reference, for instance from the periodic strip that every configuration with a leftmost black cell eventually carries on its first wheels (R30-20261104-309041, 458f3b, 9aa447). The heal criterion underlies exact accounting of heals. The six laws constrain the first stall: after a jump of 2 a stall is forced; after 3 it is excluded; after 4 or 5 the new edge heals by its second opportunity; after 6 or 7 it stalls at least twice if its new parent is white. The jump alone does not determine every stall. In measurements on the seed's strip and on random rows (our record) these laws hold on every one of about 300,000 heals, and the stall hazard after the first tick is close to one half.

The cell below runs the laws on two actual configurations: the single black cell, and the same row with a second black cell 500 places to its right. In the tested offset-3 example, the edge becomes pinned at wheel 8 above a permanently white wheel; `edge_stall` then keeps it there. Offset 500 supplies varied jumps for this demonstration. Over 3,000 ticks the cell prints the final edge, the number of heals, the heals by jump, whether `heal_iff` held on the tested transitions `t = 0,…,2998`, and the number of heals that break a jump law.

```wl
n = 3000; d = 500; w = 2 n + d + 61; c = n + 11;
row[cells_] := ReplacePart[ConstantArray[0, w], Thread[cells -> 1]];
{a, b} = CellularAutomaton[30, row[#], n] & /@ {{c}, {c, c + d}};
wheel[x_, j_, t_] := x[[t + 1, c - t + j]];
e = 0; edge = Table[While[wheel[a, e, t] == wheel[b, e, t], e++]; e, {t, 0, n}];
heals = Select[Range[0, n - 2], edge[[# + 2]] > edge[[# + 1]] &];
jump[t_] := edge[[t + 2]] - edge[[t + 1]];
p1[t_] := wheel[a, edge[[t + 2]] - 1, t + 1];
p2[t_] := wheel[a, edge[[t + 2]] - 1, t + 2];
bad[t_] := Switch[jump[t], 2, p1[t] != 0, 3, p1[t] != 1, 4, p2[t] != 1, 5, p1[t] == 0 && p2[t] != 1, 6 | 7, p1[t] == 0 && p2[t] != 0, _, False];
healOK = AllTrue[Range[0, n - 2], (edge[[# + 2]] > edge[[# + 1]]) == (wheel[a, edge[[# + 1]] - 1, #] == 1) &];
{edge[[n + 1]], Length[heals], KeySort[Counts[jump /@ heals]], healOK, Count[heals, _?bad]}
```

## 6. Prior art and scope

The barrier and the heal criterion use the aligned-parent mechanism of `Rule30UniversalLeftSide` (`child_same`, `child_white`). Those theorems already allow abstract arrays and prove persistent transport under persistent parent alignment; their use against a strip is an application. Here agreement below the current error edge supplies the alignment, and `heal_iff` records the instantaneous equivalence. The black half of `heal_iff` is also the recruiting step of our `Rule30HealingBound` (R30-20261103-e660e4), in whole-line coordinates: a black newest known cell masks its unknown neighbour. The masking itself is classical (`Rule30MaskedJen.left_of_black`). The complementary white-parent memory rule is already used inside `child_white`. More directly, `Rule30LightCone.rule_flip_right_iff` (kit PR 98) proves that flipping the right input changes the output exactly when the center input is white; at an error edge of index at least 2 this is precisely the Boolean criterion used by `heal_iff`, in diagonal coordinates. The edge statement packages this known criterion and also handles wheel 1’s boundary rule. The left damage front of rule 30 and its speed are in Wolfram's *Random sequence generation by cellular automata* (1986) and *A New Kind of Science* (p. 949), and the heal identity in diagonal coordinates is in our record (§8.66, 6 October 2026). The six laws after a heal were found by exhaustive enumeration of the window (`jump_facts.py` in our record). We searched the kit at main `5fb59158`, the portal and the open kit PRs on 5 November 2026 for error edges, difference patterns, damage, two-array statements, heals, stalls and jumps, and found no matching statements of these six post-heal laws. This is the scope of the prior-art check, not an exhaustive novelty claim. Nothing here concerns the center column or the Prize problems.

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30AgedLeftDiagonals`, which holds the recurrence.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30AgedLeftDiagonals

/-!
# The error edge of two configurations of rule 30

Two left-diagonal arrays `a` and `b` (`Rule30AgedLeftDiagonals.Recurrence`: wheel `0` is constant, wheel `1` is the
or of wheels `0` and `1`, wheel `i + 2` is `xor (wheel i) (wheel (i + 1) || wheel (i + 2))`, each read one tick earlier)
that agree on every wheel below `m` at tick `t` and differ at `m` have their *error edge* at `m` (`Edge`). Its one-step
law:

* `agree_step`, `agree_after`: agreement below `m` is kept for ever (a wheel reads only itself and the two below it).
  So the edge never retreats (`edge_le`).
* `heal_iff`: at an edge of index at least 1, the arrays agree there one tick later exactly when its parent is black. With a white
  wheel below, the edge stays (`edge_stall`); with a black one agreement extends through the old edge (`edge_heal`), possibly eliminating all differences. The black half is the
  recruiting step of `Rule30HealingBound`; the white-parent memory mechanism also appears inside `Rule30UniversalLeftSide.child_white`. The exact interior Boolean criterion is `Rule30LightCone.rule_flip_right_iff` (kit PR 98).
* After a heal at an old edge of index at least 2, the wheels above it are constrained. If the first wheel above the old edge agrees at the next
  tick, it is white there (`white_above`); if the first two agree, the second is black (`black_two_above`). Hence after
  a jump of exactly 2 the new parent is white (`jump_two`), after a jump of exactly 3 it is black (`jump_three`), after
  a jump of exactly 4 it is black one tick later whatever it was (`jump_four`), after a jump of exactly 5 whose new
  parent is white it is black one tick later (`jump_five`), and after a jump of exactly 6 or 7 whose new parent is
  white it is white one tick later (`jump_six`, `jump_seven`).

Every statement is about two abstract arrays with the recurrence and holds for any two configurations with leftmost
black cells translated into alignment and read from their common left edge (`Rule30FiniteDiagonals.Ld`, `Rule30AgedLeftDiagonals.Ld_recurrence`), the second
array being, for instance, a periodic strip. The proofs unfold the recurrence on a window of wheels and decide the resulting Boolean identities. Nothing
here concerns the center column or the Prize problems.
-/

namespace Rule30Submission

open Ruliology.CellularAutomata
open Rule30AgedLeftDiagonals

set_option autoImplicit false

/-- `a` and `b` agree on every wheel below `m` at tick `t`. -/
def Agree (a b : Nat → Nat → Bool) (m t : Nat) : Prop := ∀ j, j < m → a j t = b j t

/-- The error edge of `a` against `b` is at `m` at tick `t`. -/
def Edge (a b : Nat → Nat → Bool) (m t : Nat) : Prop := Agree a b m t ∧ a m t ≠ b m t

/-! ### The barrier: agreement below the edge is kept -/

theorem agree_step {a b : Nat → Nat → Bool} {m t : Nat} (ha : Recurrence a) (hb : Recurrence b)
    (h : Agree a b m t) : Agree a b m (t + 1) := by
  intro j hj
  match j, hj with
  | 0, hj => rw [ha.1, hb.1, h 0 hj]
  | 1, hj => rw [ha.2.1, hb.2.1, h 0 (by omega), h 1 hj]
  | k + 2, hj => rw [ha.2.2, hb.2.2, h k (by omega), h (k + 1) (by omega), h (k + 2) hj]

theorem agree_after {a b : Nat → Nat → Bool} {m t : Nat} (ha : Recurrence a) (hb : Recurrence b)
    (h : Agree a b m t) (n : Nat) : Agree a b m (t + n) := by
  induction n with
  | zero => exact h
  | succ n ih => exact agree_step ha hb ih

/-- The edge never retreats. -/
theorem edge_le {a b : Nat → Nat → Bool} {m m' t n : Nat} (ha : Recurrence a) (hb : Recurrence b)
    (h : Edge a b m t) (h' : Edge a b m' (t + n)) : m ≤ m' :=
  Nat.le_of_not_lt (fun hlt => h'.2 (agree_after ha hb h.1 n m' hlt))

/-! ### The heal criterion -/

private theorem heal_bool : ∀ (p x y s : Bool), x ≠ y →
    ((xor p (s || x) = xor p (s || y)) ↔ s = true) := by decide

private theorem heal0_bool : ∀ (s x y : Bool), x ≠ y → (((s || x) = (s || y)) ↔ s = true) := by decide

private theorem ne_bool : ∀ (x y : Bool), x ≠ y → y = !x := by decide

theorem heal_iff {a b : Nat → Nat → Bool} {m t : Nat} (ha : Recurrence a) (hb : Recurrence b)
    (h : Edge a b (m + 1) t) : (a (m + 1) (t + 1) = b (m + 1) (t + 1)) ↔ a m t = true := by
  match m, h with
  | 0, h =>
    rw [ha.2.1, hb.2.1, ← h.1 0 (by omega)]
    exact heal0_bool _ _ _ h.2
  | k + 1, h =>
    rw [ha.2.2, hb.2.2, ← h.1 k (by omega), ← h.1 (k + 1) (by omega)]
    exact heal_bool _ _ _ _ h.2

theorem edge_stall {a b : Nat → Nat → Bool} {m t : Nat} (ha : Recurrence a) (hb : Recurrence b)
    (h : Edge a b (m + 1) t) (hw : a m t = false) : Edge a b (m + 1) (t + 1) :=
  ⟨agree_step ha hb h.1, fun e => by have := (heal_iff ha hb h).1 e; rw [hw] at this; exact Bool.false_ne_true this⟩

theorem edge_heal {a b : Nat → Nat → Bool} {m t : Nat} (ha : Recurrence a) (hb : Recurrence b)
    (h : Edge a b (m + 1) t) (hk : a m t = true) : Agree a b (m + 2) (t + 1) := by
  intro j hj
  by_cases hj' : j < m + 1
  · exact agree_step ha hb h.1 j hj'
  · have : j = m + 1 := by omega
    subst this
    exact (heal_iff ha hb h).2 hk

/-! ### After a heal: the wheels above the old edge -/

private theorem white_above_bool : ∀ (x2 x3 y3 : Bool),
    xor true (x2 || x3) = xor true (!x2 || y3) → xor true (x2 || x3) = false := by decide

private theorem black_two_above_bool : ∀ (x2 x3 y3 x4 y4 : Bool),
    xor true (x2 || x3) = xor true (!x2 || y3) →
    xor x2 (x3 || x4) = xor (!x2) (y3 || y4) → xor x2 (x3 || x4) = true := by decide

/-- The two arrays' values at the window above an edge at `m + 2`, with the parent `m + 1` black. -/
private theorem window {a b : Nat → Nat → Bool} {m t : Nat} (h : Edge a b (m + 2) t) (hk : a (m + 1) t = true) :
    b m t = a m t ∧ b (m + 1) t = true ∧ b (m + 2) t = !a (m + 2) t := by
  exact ⟨(h.1 m (by omega)).symm, by rw [← h.1 (m + 1) (by omega)]; exact hk, ne_bool _ _ h.2⟩

theorem white_above {a b : Nat → Nat → Bool} {m t : Nat} (ha : Recurrence a) (hb : Recurrence b)
    (h : Edge a b (m + 2) t) (hk : a (m + 1) t = true) (h3 : a (m + 3) (t + 1) = b (m + 3) (t + 1)) :
    a (m + 3) (t + 1) = false := by
  obtain ⟨-, hb1, hb2⟩ := window h hk
  rw [ha.2.2] at h3 ⊢; rw [hb.2.2, hb1, hb2] at h3; rw [hk] at h3 ⊢
  exact white_above_bool _ _ _ h3

theorem black_two_above {a b : Nat → Nat → Bool} {m t : Nat} (ha : Recurrence a) (hb : Recurrence b)
    (h : Edge a b (m + 2) t) (hk : a (m + 1) t = true) (h3 : a (m + 3) (t + 1) = b (m + 3) (t + 1))
    (h4 : a (m + 4) (t + 1) = b (m + 4) (t + 1)) : a (m + 4) (t + 1) = true := by
  obtain ⟨-, hb1, hb2⟩ := window h hk
  rw [ha.2.2] at h3 h4 ⊢; rw [hb.2.2, hb1, hb2] at h3; rw [hb.2.2, hb2] at h4; rw [hk] at h3
  exact black_two_above_bool _ _ _ _ _ h3 h4

/-! ### The jumps -/

/-- After a jump of exactly 2 the new parent is white. -/
theorem jump_two {a b : Nat → Nat → Bool} {m t : Nat} (ha : Recurrence a) (hb : Recurrence b)
    (h : Edge a b (m + 2) t) (hk : a (m + 1) t = true) (h' : Edge a b (m + 4) (t + 1)) :
    a (m + 3) (t + 1) = false :=
  white_above ha hb h hk (h'.1 (m + 3) (by omega))

/-- After a jump of exactly 3 the new parent is black. -/
theorem jump_three {a b : Nat → Nat → Bool} {m t : Nat} (ha : Recurrence a) (hb : Recurrence b)
    (h : Edge a b (m + 2) t) (hk : a (m + 1) t = true) (h' : Edge a b (m + 5) (t + 1)) :
    a (m + 4) (t + 1) = true :=
  black_two_above ha hb h hk (h'.1 (m + 3) (by omega)) (h'.1 (m + 4) (by omega))

/-- After a jump of exactly 4 the new parent is black one tick later, whatever it was. -/
theorem jump_four {a b : Nat → Nat → Bool} {m t : Nat} (ha : Recurrence a) (hb : Recurrence b)
    (h : Edge a b (m + 2) t) (hk : a (m + 1) t = true) (h' : Edge a b (m + 6) (t + 1)) :
    a (m + 5) (t + 2) = true := by
  have w := white_above ha hb h hk (h'.1 (m + 3) (by omega))
  have k := black_two_above ha hb h hk (h'.1 (m + 3) (by omega)) (h'.1 (m + 4) (by omega))
  rw [show t + 2 = (t + 1) + 1 from rfl, ha.2.2, w, k]
  rfl

private theorem jump_five_bool : ∀ (x2 x3 y3 x4 y4 x5 y5 x6 y6 : Bool),
    xor true (x2 || x3) = xor true (!x2 || y3) →
    xor x2 (x3 || x4) = xor (!x2) (y3 || y4) →
    xor x3 (x4 || x5) = xor y3 (y4 || y5) →
    xor x4 (x5 || x6) = xor y4 (y5 || y6) →
    xor x4 (x5 || x6) = false →
    xor (xor x2 (x3 || x4)) (xor x3 (x4 || x5) || xor x4 (x5 || x6)) = true := by decide

/-- After a jump of exactly 5 whose new parent is white, the new parent is black one tick later. -/
theorem jump_five {a b : Nat → Nat → Bool} {m t : Nat} (ha : Recurrence a) (hb : Recurrence b)
    (h : Edge a b (m + 2) t) (hk : a (m + 1) t = true) (h' : Edge a b (m + 7) (t + 1))
    (hw : a (m + 6) (t + 1) = false) : a (m + 6) (t + 2) = true := by
  obtain ⟨-, hb1, hb2⟩ := window h hk
  have h3 := h'.1 (m + 3) (by omega); have h4 := h'.1 (m + 4) (by omega)
  have h5 := h'.1 (m + 5) (by omega); have h6 := h'.1 (m + 6) (by omega)
  rw [show t + 2 = (t + 1) + 1 from rfl, ha.2.2, ha.2.2, ha.2.2, ha.2.2]
  rw [ha.2.2, hb.2.2, hb1, hb2, hk] at h3; rw [ha.2.2, hb.2.2, hb2] at h4
  rw [ha.2.2, hb.2.2] at h5; rw [ha.2.2, hb.2.2] at h6; rw [ha.2.2] at hw
  exact jump_five_bool _ _ _ _ _ _ _ _ _ h3 h4 h5 h6 hw

private theorem jump_six_bool : ∀ (x2 x3 y3 x4 y4 x5 y5 x6 y6 x7 y7 : Bool),
    xor true (x2 || x3) = xor true (!x2 || y3) →
    xor x2 (x3 || x4) = xor (!x2) (y3 || y4) →
    xor x3 (x4 || x5) = xor y3 (y4 || y5) →
    xor x4 (x5 || x6) = xor y4 (y5 || y6) →
    xor x5 (x6 || x7) = xor y5 (y6 || y7) →
    xor x5 (x6 || x7) = false →
    xor (xor x3 (x4 || x5)) (xor x4 (x5 || x6) || xor x5 (x6 || x7)) = false := by decide

/-- After a jump of exactly 6 whose new parent is white, the new parent is white one tick later. -/
theorem jump_six {a b : Nat → Nat → Bool} {m t : Nat} (ha : Recurrence a) (hb : Recurrence b)
    (h : Edge a b (m + 2) t) (hk : a (m + 1) t = true) (h' : Edge a b (m + 8) (t + 1))
    (hw : a (m + 7) (t + 1) = false) : a (m + 7) (t + 2) = false := by
  obtain ⟨-, hb1, hb2⟩ := window h hk
  have h3 := h'.1 (m + 3) (by omega); have h4 := h'.1 (m + 4) (by omega)
  have h5 := h'.1 (m + 5) (by omega); have h6 := h'.1 (m + 6) (by omega); have h7 := h'.1 (m + 7) (by omega)
  rw [show t + 2 = (t + 1) + 1 from rfl, ha.2.2, ha.2.2, ha.2.2, ha.2.2]
  rw [ha.2.2, hb.2.2, hb1, hb2, hk] at h3; rw [ha.2.2, hb.2.2, hb2] at h4
  rw [ha.2.2, hb.2.2] at h5; rw [ha.2.2, hb.2.2] at h6; rw [ha.2.2, hb.2.2] at h7; rw [ha.2.2] at hw
  exact jump_six_bool _ _ _ _ _ _ _ _ _ _ _ h3 h4 h5 h6 h7 hw

private theorem jump_seven_bool : ∀ (x2 x3 y3 x4 y4 x5 y5 x6 y6 x7 y7 x8 y8 : Bool),
    xor true (x2 || x3) = xor true (!x2 || y3) →
    xor x2 (x3 || x4) = xor (!x2) (y3 || y4) →
    xor x3 (x4 || x5) = xor y3 (y4 || y5) →
    xor x4 (x5 || x6) = xor y4 (y5 || y6) →
    xor x5 (x6 || x7) = xor y5 (y6 || y7) →
    xor x6 (x7 || x8) = xor y6 (y7 || y8) →
    xor x6 (x7 || x8) = false →
    xor (xor x4 (x5 || x6)) (xor x5 (x6 || x7) || xor x6 (x7 || x8)) = false := by decide

/-- After a jump of exactly 7 whose new parent is white, the new parent is white one tick later. -/
theorem jump_seven {a b : Nat → Nat → Bool} {m t : Nat} (ha : Recurrence a) (hb : Recurrence b)
    (h : Edge a b (m + 2) t) (hk : a (m + 1) t = true) (h' : Edge a b (m + 9) (t + 1))
    (hw : a (m + 8) (t + 1) = false) : a (m + 8) (t + 2) = false := by
  obtain ⟨-, hb1, hb2⟩ := window h hk
  have h3 := h'.1 (m + 3) (by omega); have h4 := h'.1 (m + 4) (by omega)
  have h5 := h'.1 (m + 5) (by omega); have h6 := h'.1 (m + 6) (by omega)
  have h7 := h'.1 (m + 7) (by omega); have h8 := h'.1 (m + 8) (by omega)
  rw [show t + 2 = (t + 1) + 1 from rfl, ha.2.2, ha.2.2, ha.2.2, ha.2.2]
  rw [ha.2.2, hb.2.2, hb1, hb2, hk] at h3; rw [ha.2.2, hb.2.2, hb2] at h4
  rw [ha.2.2, hb.2.2] at h5; rw [ha.2.2, hb.2.2] at h6; rw [ha.2.2, hb.2.2] at h7; rw [ha.2.2, hb.2.2] at h8
  rw [ha.2.2] at hw
  exact jump_seven_bool _ _ _ _ _ _ _ _ _ _ _ _ _ h3 h4 h5 h6 h7 h8 hw

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The theorems, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30AgedLeftDiagonals"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
heads = {"agree_step", "agree_after", "edge_le", "heal_iff", "edge_stall", "edge_heal", "white_above", "black_two_above", "jump_two", "jump_three", "jump_four", "jump_five", "jump_six", "jump_seven"};
show[heads, "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.heal_iff"]["KernelCheck"]
```
