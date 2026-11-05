---
Template: ComputationalEssay
Name: Locks at the wall of rule 30's rain-tailed rows: letters forced for ever, whatever lies below
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-05
Description: Core Lean. On rows of rule 30 with an alternating left tail, closed sets of windows at the wall force the letter sequences AB and AAB for ever, whatever lies below, and a closed set of 798 windows excludes the first of those locks.
Abstract: Read a row of rule 30 from its rightmost black cell, so that one tick is the kit's edge map T, and take rows whose cells alternate from some index on. Their wall is the last equal pair below that tail. Each row has exactly one predecessor. Going backward, a wall that rises three cells on three ticks running shows one of two eleven-cell letters, A or B (deep_words), and BB and AAA never occur (no_BB, no_AAA). A set of windows closed under the backward tick for every pair of lower cells holds a row for ever, whatever lies below it (held_forever). We give three such sets. Four windows of 45 cells force the letters AB repeated, six of 136 force AAB repeated, and forty of 175 force them with no reset word at a fixed depth below the wall (LockAB.letters, LockAAB.letters, LockThird.letters, LockThird.no_floor). A closed set of 798 windows of 45 cells never reaches the first lock and bounds alternation at 17 ticks (Cloud.avoids_lock, Cloud.no_long_alternation), and one explicit row passes from that set into the third lock (Entry.entry). No row in these sets is periodic under T. The kernel checks everything in about 13 seconds on an M5. Whether every row with such a tail reaches a letter, or a lock, stays open. Nothing here concerns the center column or the Prize problems.
Keywords: [rule 30, Rule 30 Prize, right edge, edge map, backward tick, closed windows, reset word, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)", "E. M. Coven, M. Pivato and R. Yassawi, Prevalence of odometers in cellular automata, Proc. AMS 135 (2007)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[R30-20261027-196370: staircases near the right edge, and the rain rows](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261027-196370)"]
---

## 1. The setting and the claim

Read a row of rule 30 from its rightmost black cell. Bit `k` of its edge code is the cell `k` places behind that cell, and one tick of rule 30 is the kit's edge map `T`:

`T c 0 = c 0`, `T c 1 = c 1 ⊕ c 0`, `T c (k + 2) = c (k + 2) ⊕ (c (k + 1) ∨ c k)`.

This is `Rule30FrozenRuler.edge_evol`, which needs only white to the right of the edge cell, so the row need not be finite. Below, a *row* is such a code. Every row has exactly one predecessor (`predecessor_unique`), so time can be run backward, and `previousN` does so. A statement about all `z` with `iter z n = x` is a statement about one row, the `n`-th predecessor of `x`. It holds whatever the lower cells of `x` are.

A row has a *rain tail* if its cells alternate from some index on. `T` keeps a rain tail and so does the predecessor (`step_rain_tail`, `back_rain_tail`). The rain pair `1010…`, `11010…` of `Rule30EdgeStaircases` is all tail. Any other row with a rain tail has a *wall*, the last equal pair below the tail (`Top`). This entry is about what stands at the wall. Words are written from low cell to high cell, with `#` black and `.` white.

**Letters.** Suppose the wall rises three cells on each of three backward ticks, at depth at least 5. Then the eleven cells ending at the wall read `A = ..####...##` or `B = .#.###...##` (`deep_words`). `BB` never occurs on successive ticks (`no_BB`), nor does `AAA` (`no_AAA`), and `ABA` occurs on an anchored row (`witness_ABA`).

**Locks.** Three sets of windows, each closed under the backward tick for every pair of lower cells:

| Lock | Cells | Windows | Phases | Letters, in backward time | Reset word |
|---|---|---|---|---|---|
| `LockAB` | 45 | 4 | 2 | `A`, `B` | at the foot of every window (`floor`) |
| `LockAAB` | 136 | 6 | 3 | `A`, `A`, `B` | at the foot of every window (`floor`) |
| `LockThird` | 175 | 40 | 6 | `B`, `A`, `A`, `B`, `A`, `A` | at no depth below the wall's own (`no_floor`) |

If a row shows a window of a lock at its wall, with rain above, then every predecessor does too, three cells higher each tick, and the letters follow the phases for ever, whatever lies below the window (`LockAB.letters`, `LockAAB.letters`, `LockThird.letters`). Each lock has a witness on an anchored row (`witness`).

**The cloud.** A set of 798 windows of 45 cells is closed too (`Cloud.closed`). None of them is a window of `LockAB` (`cloud_not_lock`), so a row in the cloud never reaches that lock (`avoids_lock`). Along any backward history in the cloud the letters cannot change on 17 ticks running (`no_long_alternation`).

**Entry.** One explicit anchored row passes from the cloud into the third lock (`Entry.entry`).

**Not periodic.** A row in any of these four sets is not periodic under `T` (`not_periodic`, from the general `held_not_periodic`).

Nothing here concerns the center column or the Prize problems.

## 2. The wall and its letters

The wall moves by an exact local rule under `T`. Say the wall is at `D`. If cell `D` is white it moves up two cells (`top_up`). If `D` is black and a cell of `D − 1`, `D − 2` is black, it stays (`top_stay`). If `D` is black and both are white, it falls by one, two or three cells, according to cells `D − 3` and `D − 4` (`top_minus_one`, `top_minus_two`, `top_minus_three`). So a backward advance of three is the last case read in reverse, and it fixes the six cells at the wall to `#...##` (`marker`).

Three such advances put that marker on three successive rows, and a finite check of the ten cells below the first marker leaves the two letters (`deep_words`). Eighteen windows of eleven cells are closed under the backward tick (`front_back`), and a row showing one is not periodic (`front_not_periodic`). So the open part of the question "is the rain pair the only periodic row with a rain tail?" is whether every other such row reaches those windows. We do not settle that here.

Once a row shows a letter, the two letters are themselves closed (`letters_closed`). The next letter has a simple rule. After `B` comes `A` for every pair of lower cells (`letter_after_B`). After `A` comes `A` exactly when the two cells of the predecessor just below the old window are white (`letter_after_A`). After `AA` comes `B`, by `no_AAA`. So every settled word is a string of blocks `BA` and `BAA`, and the only choice is the letter after `BA`.

## 3. The word that stops what comes from below

A backward tick is a sweep upward. Each new cell reads the old cell at its place and the two new cells below it. So the image of a window depends on what lies below only through two cells.

Take ten cells `F(b, u, v) = 0, b, ¬b, 1, u, 1, 0, v, 0, 1`.

- `Reset.reset`: under any two lower cells, the new cells on places 3 to 9 of the word are `0, b′, ¬b′, 1, ¬v, 1, 0`. Only the bit `b′` feels the lower cells, and only through whether both are white.
- `Reset.above`: the output above the word is one fixed function of the input above it, whatever `b`, `u`, `v` and the cells below.
- `Reset.again`: if the row reads `s, ¬s, s` just above the word, the predecessor has the same shape of word three cells higher, with `v` replaced by `¬s` and `u` by `¬v`.
- `Reset.letters`: `A` and `B` are `F(0, 1, 0)` and `F(1, 1, 0)` with one black cell above.

Rain supplies `s, ¬s, s` on every tick, which is why the wall rises by exactly three.

`Reset.above` is not new in kind. Each word `F(b, u, v)` contains a word `0 1^(3m + 1) 0` of Lowry's `Rule30ResetFreeCore` with a further cell above it, and such words reset the inverse sweep (`Rule30InverseCascade`, kit PR 60). What the theorems here add is the shape that comes back three cells higher.

## 4. Closed sets

Let `S` be a list of words of `W` cells. `S` is *closed* (`Closed`) if for every window in it and each of the four pairs of lower cells, the image window is in `S` and rain resumes above it. `Held W S x L` says that cells `L` to `L + W − 1` of `x` are a window of `S` and that the cells above alternate. Then:

- `held_back`: every predecessor is held three cells higher, whatever lies below the window.
- `held_forever`: every row `n` ticks back is held `3 n` cells higher.
- `held_not_periodic`: if every window ends in the wall's equal pair, a held row is not periodic. A period would put the same wall `3 P` cells higher on the same row, inside its rain.

The check on `S` is finite, and the theorem is general. A closed set of windows that ignores the cells on one side is the method of the kit's `Rule30GateTrap`, here on the wall of an edge code and in backward time.

## 5. Three locks

These are the four windows of `LockAB`. The last eleven cells are the letter.

```
..##.#...#.#..#..#........##....##..####...##    A
.#.#.#...#.#..#..#........##....##..####...##    A
..####.#.##.##.########......#.##..#.###...##    B
.#.###.#.##.##.########......#.##..#.###...##    B
```

The two windows of a phase differ only in cells 1 and 2, the bit `b` of the reset word at the foot of the window. That bit is all the lower cells can move. So a window of `LockAB` holds a second reset word, 34 cells below the wall's own, and the strip between the two cannot feel anything from below. The same holds for `LockAAB`, with the two words 125 cells apart.

`LockThird` shows that a lock needs no such word. No reset word stands at one depth in all forty windows, apart from the wall's own (`no_floor`), and the number of windows in a phase runs 5, 6, 7, 8, 7, 7. Lower states still merge before they reach the letters, but at places that move with the phase. So `AAB` repeated has two different locks.

A separate computation finds that these widths are the smallest. At 135 and 174 cells, a path of free lower cells leaves the letters (COMPUTED).

## 6. The cloud, and a row that enters a lock

Most rows do not lock at once. Of 100,000 rows with 40 random cells, 99,176 entered the 798 windows and 824 entered `LockAB`, all by tick 128 (MEASURED). The cloud explains why late rows never reached `LockAB`: `Cloud.closed` holds them, and `cloud_not_lock` keeps them apart. Its rank function, the longest alternating run from each window, gives `no_long_alternation`.

The cloud is coarse, though. The theorem `Entry.entry` is about one explicit row whose rain starts at cell 569. Its images under `T`, at ticks `k`, read letters for every `k ≤ 110` (`Entry.letters`). The image at tick 97 is held in the cloud, so the images at every tick below 97 are too. The image at tick 7 is outside the third lock, and the image at tick 6 is inside it, so the images at ticks 0 to 6 are as well. Read backward from tick 110, the letters run in a mix of `BA` and `BAA` down to tick 57, then `BAA` repeated, and the row is caught at tick 6.

So a row in the cloud can step into a lock: a window of 45 cells cannot see the third lock.

## 7. A computation

The first cell below checks `LockAB` outside Lean, with plain lists and the inverse rule cell by cell, then reads the letters of the entry row, tick 0 first, by forward ticks on one integer. The second cell draws the top 120 cells of that row in the frame of its wall, with tick 110 at the top, tick 0 at the bottom and the wall on the left.

```wl
back[{p1_, p2_}, l_] := Module[{a = p1, b = p2, z}, Table[z = BitXor[c, BitOr[a, b]]; b = a; a = z; z, {c, l}]];
next[w_, p_] := back[p, Join[Most[w], {1, 0, 1, 0, 1, 0, 1}]][[4 ;; 3 + Length[w]]];
bits[s_] := Characters[s] /. {"." -> 0, "#" -> 1};
lockAB = bits /@ {"..##.#...#.#..#..#........##....##..####...##", ".#.#.#...#.#..#..#........##....##..####...##", "..####.#.##.##.########......#.##..#.###...##", ".#.###.#.##.##.########......#.##..#.###...##"};
closed = AllTrue[Tuples[{lockAB, Tuples[{0, 1}, 2]}], MemberQ[lockAB, next @@ #] &];
row0 = 16^^2aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab1e614b8e559ce1eb5af79ec4b49c942ff71686d7b1f8feea41c22e007f1b8a2a00548ae0e88092689b1f5e23635d5c78434763f914c2c3d26e1dde151efbc42a5bb3f34c886201;
fw[v_] := BitAnd[BitXor[v, BitOr[BitShiftLeft[v, 1], BitShiftLeft[v, 2]]], 2^850 - 1];
rows = NestList[fw, row0, 110];
cells[v_, lo_, n_] := Reverse[IntegerDigits[BitAnd[BitShiftRight[v, lo], 2^n - 1], 2, n]];
letter[w_] := Which[w === bits["..####...##"], "A", w === bits[".#.###...##"], "B", True, "?"];
{closed, StringJoin[Table[letter[cells[rows[[k + 1]], 229 + 3 (110 - k), 11]], {k, 0, 110}]]}
```

```wl
ArrayPlot[Table[Reverse[cells[rows[[k + 1]], 450 - 3 k, 120]], {k, 110, 0, -1}], ImageSize -> 480]
```

## 8. How the kernel checks it

A window of `W` cells is a number. `load` puts the two lower cells under it and six cells of rain over it, `sw` is one cell of the sweep, and `run` is the whole sweep, on one number with one index. `run_back` proves this is `back` on words, `next_fast` that the image window is `nxt`, and `closed_fast` that a list of numbers passing `Fast` is `Closed`. The test inside `run` never changes the value, since `0` stays `0` (`run_succ`), but it forces each cell as the kernel reaches it. For the forward direction `fw` is one exclusive or and two shifts, and `iter_fw` proves it is `T` on all bits.

The record's first versions of these proofs used lists and took 57 s for the cloud alone. With numbers the three kit modules build in about 2, 2 and 10 s, at 2.7 GB at most, and the one-module portal form builds in 13 s at 3.0 GB. All the times here were measured on an M5 MacBook Pro.

We also ran two controls outside the Lean proof. Ten small mutations (a window of each lock, a rank, the rank bound, a window of the cloud, a bit of the row, a letter, the rule, the rain) were all rejected. A separate Python replay from the literals in the source, on plain lists, confirms all 3,392 image checks, the letters, the ranks, the reset depths and the entry row.

## 9. What is computed or open

These are not theorems of this entry.

- **COMPUTED.** Let `E(w)` be the windows of `w` cells that can follow arbitrarily many settled ticks with free lower cells. At every width from 45 to 92 the graph on `E(w)` has exactly two closed classes, the class of `LockAB` and a cloud, of 798 windows at width 45 and 920,783 at width 92.
- **COMPUTED.** A reset word below the wall leaves one free binary word in time. Among primitive words of period up to 13, exactly two reach rain going up, `10` and `110`, the words of `LockAB` and `LockAAB`. Through period 24 this holds within 20,000 columns.
- **MEASURED, on a surrogate.** In a chain on the top 256 cells with independent fair lower cells, no state entered the third lock in about 1.26 · 10^11 ticks. Fair lower cells are an assumption, not a fact about real rows.
- **Open.** Whether every row with a rain tail reaches the letters, whether every settled row ends in a lock, and whether there are other locks. A search by period found these three and no others, with caps, so this is a list of what was found.

## 10. Credits and prior art

The edge map is `Rule30FrozenRuler` (Coven, Pivato and Yassawi, Proc. AMS 135, 2007), and the rain pair is `Rule30EdgeStaircases` (R30-20261027-196370). Reset words `0 1^(3m + 1) 0` and their role in the inverse sweep are Troy Lowry's (`Rule30ResetFreeCore`, `Rule30ResetFreeThree`, kit PR 60). The closed-window method is in `Rule30GateTrap`. `Rule30UniversalStart` (R30-20261029-3ca86f) reads the first equal pair behind the edge on the right diagonals. The wall here is the last one. The word "lock" here is not the `Lock` of the kit's period-4 table, and "wall" is not the kit's zero wall.

We searched the kit at main `72253aea`, all portal entries and open kit PRs on 5 November 2026 for rain tails, walls of edge codes, closed windows under the backward tick and reset words, and found no earlier statement of these theorems.

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30FrozenRuler`, which holds the edge map. The row of section 1 is `Row`, one tick is `step`, the kit's `T`, and `iter x t` is the kit's `iter t x`.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30FrozenRuler

/-!
# Rule 30: the wall of a rain-tailed edge code. Two letters, three locks and a closed cloud

Read a row from its rightmost black cell, as in `Rule30FrozenRuler`: one tick of rule 30 is the edge map `T`. A code with a rain tail
alternates from some index on, and its wall is the last equal pair below the tail. Under backward ticks a settled wall rises three cells
a tick and shows one of two eleven-cell letters. This module gives closed sets of windows at the wall: a code showing a window of such a
set shows one at every backward tick for ever, whatever lies below the window. Three of them force the letter sequences `AB`, `AAB`
and `BAABAA` for ever, and a set of 798 windows of 45 cells excludes the first of those locks. An explicit row in that set enters the
third lock. Rows in these sets are not periodic under `T`. Nothing here concerns the center column or the Prize problems.
-/

namespace Rule30Submission

open Ruliology.CellularAutomata Rule30FrozenRuler

set_option autoImplicit false
set_option maxRecDepth 100000

/-- A row: bit `0` is the rightmost black cell, bit `k` the cell `k` places behind it. -/
abbrev Row := Nat → Bool

/-- One tick of rule 30 on rows: the kit's edge map. -/
abbrev step : Row → Row := T

/-- `t` ticks, with the row first. -/
abbrev iter (x : Row) (t : Nat) : Row := Rule30FrozenRuler.iter t x

theorem step_zero (x : Row) : step x 0 = x 0 := rfl
theorem step_one (x : Row) : step x 1 = xor (x 1) (x 0) := rfl
theorem step_add (x : Row) (j : Nat) : step x (j + 2) = xor (x (j + 2)) (x (j + 1) || x j) := rfl

theorem iter_zero_bit {x : Row} (h : x 0 = true) (t : Nat) : iter x t 0 = true := by
  induction t with
  | zero => exact h
  | succ t ih => exact ih

theorem iter_add (x : Row) (s t : Nat) : iter x (s + t) = iter (iter x s) t := by
  induction t with
  | zero => rfl
  | succ t ih => show step (iter x (s + t)) = step (iter (iter x s) t); rw [ih]

/-! ## Rain tails survive both ways -/

def seg (x : Row) : Nat → Nat → List Bool
  | _, 0 => []
  | L, n + 1 => x L :: seg x (L + 1) n

/-- The inverse recursion read along a list: `p1`, `p2` are the two output bits below it. -/
def back (p1 p2 : Bool) : List Bool → List Bool
  | [] => []
  | b :: r => xor b (p1 || p2) :: back (xor b (p1 || p2)) p1 r

def alt (b : Bool) : Nat → List Bool
  | 0 => []
  | n + 1 => b :: alt (!b) n

theorem seg_length (x : Row) (n : Nat) : ∀ L, (seg x L n).length = n := by
  induction n with
  | zero => intro L; rfl
  | succ n ih => intro L; simp [seg, ih]

theorem seg_append (x : Row) (a b : Nat) : ∀ L, seg x L (a + b) = seg x L a ++ seg x (L + a) b := by
  induction a with
  | zero => intro L; simp [seg]
  | succ a ih =>
    intro L
    have : a + 1 + b = (a + b) + 1 := by omega
    rw [this]
    show x L :: seg x (L + 1) (a + b) = (x L :: seg x (L + 1) a) ++ seg x (L + (a + 1)) b
    rw [ih (L + 1)]
    have : L + 1 + a = L + (a + 1) := by omega
    rw [this]; rfl

theorem seg_getD (x : Row) (n : Nat) : ∀ L i, i < n → (seg x L n).getD i false = x (L + i) := by
  induction n with
  | zero => intro L i h; omega
  | succ n ih =>
    intro L i h
    cases i with
    | zero => rfl
    | succ i =>
      show (seg x (L + 1) n).getD i false = x (L + (i + 1))
      rw [ih (L + 1) i (by omega)]
      have : L + 1 + i = L + (i + 1) := by omega
      rw [this]

theorem seg_alt {x : Row} {J : Nat} (h : ∀ j, J ≤ j → x (j + 1) = !x j) (n : Nat) :
    ∀ L, J ≤ L → seg x L n = alt (x L) n := by
  induction n with
  | zero => intro L _; rfl
  | succ n ih =>
    intro L hL
    show x L :: seg x (L + 1) n = x L :: alt (!x L) n
    rw [ih (L + 1) (by omega), h L hL]

theorem back_seg {z x : Row} (hs : step z = x) (n : Nat) :
    ∀ L, 2 ≤ L → seg z L n = back (z (L - 1)) (z (L - 2)) (seg x L n) := by
  induction n with
  | zero => intro L _; rfl
  | succ n ih =>
    intro L hL
    obtain ⟨i, rfl⟩ : ∃ i, L = i + 2 := ⟨L - 2, by omega⟩
    have hx : x (i + 2) = xor (z (i + 2)) (z (i + 1) || z i) := by rw [← hs]; rfl
    have ho : xor (x (i + 2)) (z (i + 1) || z i) = z (i + 2) := by
      rw [hx]; cases z (i + 2) <;> cases (z (i + 1) || z i) <;> rfl
    show z (i + 2) :: seg z (i + 2 + 1) n =
      xor (x (i + 2)) (z (i + 1) || z i) :: back (xor (x (i + 2)) (z (i + 1) || z i)) (z (i + 1)) (seg x (i + 2 + 1) n)
    rw [ho, ih (i + 2 + 1) (by omega)]
    rfl

/-- Once a predecessor is the complement of a rain tail on two adjacent bits, it is for ever. -/
theorem compl_tail {z x : Row} (hs : step z = x) {J : Nat} (hx : ∀ j, J ≤ j → x (j + 1) = !x j)
    (h0 : z J = !x J) (h1 : z (J + 1) = !x (J + 1)) (d : Nat) :
    z (J + d) = !x (J + d) ∧ z (J + d + 1) = !x (J + d + 1) := by
  induction d with
  | zero => exact ⟨h0, h1⟩
  | succ d ih =>
    obtain ⟨a, b⟩ := ih
    refine ⟨b, ?_⟩
    have hxx : x (J + d + 2) = xor (z (J + d + 2)) (z (J + d + 1) || z (J + d)) := by rw [← hs]; rfl
    have hxs := hx (J + d) (by omega)
    have hor : (z (J + d + 1) || z (J + d)) = true := by
      rw [b, a, hxs]; cases x (J + d) <;> rfl
    rw [hor] at hxx
    show z (J + d + 2) = !x (J + d + 2)
    rw [hxx]; cases z (J + d + 2) <;> rfl

theorem tail_of_compl {z x : Row} (hs : step z = x) {J : Nat} (hx : ∀ j, J ≤ j → x (j + 1) = !x j)
    (h0 : z J = !x J) (h1 : z (J + 1) = !x (J + 1)) : ∀ j, J ≤ j → z (j + 1) = !z j := by
  intro j hj
  obtain ⟨d, rfl⟩ : ∃ d, j = J + d := ⟨j - J, by omega⟩
  obtain ⟨a, b⟩ := compl_tail hs hx h0 h1 d
  rw [a, b, hx (J + d) (by omega)]

/-- A rain tail survives a forward tick. -/
theorem step_rain_tail {x : Row} {D : Nat} (h : ∀ j, D ≤ j → x (j + 1) = !x j) :
    ∀ j, D + 2 ≤ j → step x (j + 1) = !step x j := by
  intro j hj
  obtain ⟨i, rfl⟩ : ∃ i, j = i + 2 := ⟨j - 2, by omega⟩
  have a1 := h i (by omega)
  have a2 := h (i + 1) (by omega)
  have a3 := h (i + 2) (by omega)
  show xor (x (i + 3)) (x (i + 2) || x (i + 1)) = !xor (x (i + 2)) (x (i + 1) || x i)
  rw [a3, a2, a1]
  cases x i <;> rfl

theorem chk_tail : ∀ p1 p2 b : Bool,
    (back p1 p2 (alt b 5)).getD 3 false = !(alt b 5).getD 3 false ∧
    (back p1 p2 (alt b 5)).getD 4 false = !(alt b 5).getD 4 false := by decide

/-- A rain tail survives a backward tick, three bits higher: every predecessor of a rain-tailed row is rain-tailed. -/
theorem back_rain_tail {z x : Row} {D : Nat} (hD : 2 ≤ D) (hs : step z = x)
    (h : ∀ j, D ≤ j → x (j + 1) = !x j) : ∀ j, D + 3 ≤ j → z (j + 1) = !z j := by
  have e := back_seg hs 5 D hD
  rw [seg_alt h 5 D (Nat.le_refl D)] at e
  obtain ⟨c0, c1⟩ := chk_tail (z (D - 1)) (z (D - 2)) (x D)
  rw [← e, seg_getD z 5 D 3 (by omega)] at c0
  rw [← e, seg_getD z 5 D 4 (by omega)] at c1
  have s3 : (alt (x D) 5).getD 3 false = x (D + 3) := by
    rw [← seg_alt h 5 D (Nat.le_refl D)]; exact seg_getD x 5 D 3 (by omega)
  have s4 : (alt (x D) 5).getD 4 false = x (D + 4) := by
    rw [← seg_alt h 5 D (Nat.le_refl D)]; exact seg_getD x 5 D 4 (by omega)
  rw [s3] at c0
  rw [s4] at c1
  exact tail_of_compl hs (fun j hj => h j (by omega)) c0 c1

/-! ## The top-wall rule -/

/-- `D` is the top wall: its two cells agree and rain lies above. -/
def Top (x : Row) (D : Nat) : Prop := x (D + 1) = x D ∧ ∀ j, D + 1 ≤ j → x (j + 1) = !x j

/-- A white top wall rises by two and turns black. -/
theorem top_up {x : Row} {k : Nat} (h : Top x (k + 5)) (hw : x (k + 5) = false) :
    Top (step x) (k + 7) ∧ step x (k + 7) = true := by
  obtain ⟨e, hr⟩ := h
  have a1 : x (k + 7) = !x (k + 6) := hr (k + 6) (by omega)
  have a2 : x (k + 8) = !x (k + 7) := hr (k + 7) (by omega)
  have s7 : step x (k + 7) = xor (x (k + 7)) (x (k + 6) || x (k + 5)) := rfl
  have s8 : step x (k + 8) = xor (x (k + 8)) (x (k + 7) || x (k + 6)) := rfl
  have b6 : x (k + 6) = false := by rw [show k + 6 = k + 5 + 1 from rfl, e, hw]
  have r7 : step x (k + 7) = true := by rw [s7, a1, b6, hw]; rfl
  have r8 : step x (k + 8) = true := by rw [s8, a2, a1, b6]; rfl
  refine ⟨⟨by rw [show k + 7 + 1 = k + 8 from rfl, r7, r8], ?_⟩, r7⟩
  intro j hj
  exact step_rain_tail (D := k + 6) (fun i hi => hr i (by omega)) j (by omega)

/-- A black top wall with a black cell among the next two stays and turns white. -/
theorem top_stay {x : Row} {k : Nat} (h : Top x (k + 5)) (hb : x (k + 5) = true)
    (hc : (x (k + 4) || x (k + 3)) = true) : Top (step x) (k + 5) ∧ step x (k + 5) = false := by
  obtain ⟨e, hr⟩ := h
  have a1 : x (k + 7) = !x (k + 6) := hr (k + 6) (by omega)
  have a2 : x (k + 8) = !x (k + 7) := hr (k + 7) (by omega)
  have b6 : x (k + 6) = true := by rw [show k + 6 = k + 5 + 1 from rfl, e, hb]
  have r5 : step x (k + 5) = false := by
    show xor (x (k + 5)) (x (k + 4) || x (k + 3)) = false
    rw [hb, hc]; rfl
  have r6 : step x (k + 6) = false := by
    show xor (x (k + 6)) (x (k + 5) || x (k + 4)) = false
    rw [b6, hb]; rfl
  have r7 : step x (k + 7) = true := by
    show xor (x (k + 7)) (x (k + 6) || x (k + 5)) = true
    rw [a1, b6, hb]; rfl
  have r8 : step x (k + 8) = false := by
    show xor (x (k + 8)) (x (k + 7) || x (k + 6)) = false
    rw [a2, a1, b6]; rfl
  refine ⟨⟨by rw [show k + 5 + 1 = k + 6 from rfl, r5, r6], ?_⟩, r5⟩
  intro j hj
  by_cases c6 : j = k + 6
  · subst c6; rw [show k + 6 + 1 = k + 7 from rfl, r6, r7]; rfl
  · by_cases c7 : j = k + 7
    · subst c7; rw [show k + 7 + 1 = k + 8 from rfl, r7, r8]; rfl
    · exact step_rain_tail (D := k + 6) (fun i hi => hr i (by omega)) j (by omega)

/-- Above a black top wall with two white cells under it, the row after a tick reads black, white, black from the wall up. -/
theorem top_fall_rain {x : Row} {k : Nat} (h : Top x (k + 5)) (hb : x (k + 5) = true)
    (h4 : x (k + 4) = false) (h3 : x (k + 3) = false) :
    step x (k + 5) = true ∧ step x (k + 6) = false ∧ ∀ j, k + 5 ≤ j → step x (j + 1) = !step x j := by
  obtain ⟨e, hr⟩ := h
  have a1 : x (k + 7) = !x (k + 6) := hr (k + 6) (by omega)
  have a2 : x (k + 8) = !x (k + 7) := hr (k + 7) (by omega)
  have b6 : x (k + 6) = true := by rw [show k + 6 = k + 5 + 1 from rfl, e, hb]
  have r5 : step x (k + 5) = true := by
    show xor (x (k + 5)) (x (k + 4) || x (k + 3)) = true
    rw [hb, h4, h3]; rfl
  have r6 : step x (k + 6) = false := by
    show xor (x (k + 6)) (x (k + 5) || x (k + 4)) = false
    rw [b6, hb]; rfl
  have r7 : step x (k + 7) = true := by
    show xor (x (k + 7)) (x (k + 6) || x (k + 5)) = true
    rw [a1, b6, hb]; rfl
  have r8 : step x (k + 8) = false := by
    show xor (x (k + 8)) (x (k + 7) || x (k + 6)) = false
    rw [a2, a1, b6]; rfl
  refine ⟨r5, r6, ?_⟩
  intro j hj
  by_cases c5 : j = k + 5
  · subst c5; rw [show k + 5 + 1 = k + 6 from rfl, r5, r6]; rfl
  · by_cases c6 : j = k + 6
    · subst c6; rw [show k + 6 + 1 = k + 7 from rfl, r6, r7]; rfl
    · by_cases c7 : j = k + 7
      · subst c7; rw [show k + 7 + 1 = k + 8 from rfl, r7, r8]; rfl
      · exact step_rain_tail (D := k + 6) (fun i hi => hr i (by omega)) j (by omega)

/-- Retreat by one: the wall drops one cell and stays black. -/
theorem top_minus_one {x : Row} {k : Nat} (h : Top x (k + 5)) (hb : x (k + 5) = true)
    (h4 : x (k + 4) = false) (h3 : x (k + 3) = false) (h2 : x (k + 2) = true) :
    Top (step x) (k + 4) ∧ step x (k + 4) = true := by
  obtain ⟨r5, r6, hr⟩ := top_fall_rain h hb h4 h3
  have r4 : step x (k + 4) = true := by
    show xor (x (k + 4)) (x (k + 3) || x (k + 2)) = true
    rw [h4, h3, h2]; rfl
  exact ⟨⟨by rw [show k + 4 + 1 = k + 5 from rfl, r4, r5], hr⟩, r4⟩

/-- Retreat by two: the wall drops two cells and turns white. -/
theorem top_minus_two {x : Row} {k : Nat} (h : Top x (k + 5)) (hb : x (k + 5) = true)
    (h4 : x (k + 4) = false) (h3 : x (k + 3) = false) (h2 : x (k + 2) = false) (h1 : x (k + 1) = false) :
    Top (step x) (k + 3) ∧ step x (k + 3) = false := by
  obtain ⟨r5, r6, hr⟩ := top_fall_rain h hb h4 h3
  have r4 : step x (k + 4) = false := by
    show xor (x (k + 4)) (x (k + 3) || x (k + 2)) = false
    rw [h4, h3, h2]; rfl
  have r3 : step x (k + 3) = false := by
    show xor (x (k + 3)) (x (k + 2) || x (k + 1)) = false
    rw [h3, h2, h1]; rfl
  refine ⟨⟨by rw [show k + 3 + 1 = k + 4 from rfl, r3, r4], ?_⟩, r3⟩
  intro j hj
  by_cases c4 : j = k + 4
  · subst c4; rw [show k + 4 + 1 = k + 5 from rfl, r4, r5]; rfl
  · exact hr j (by omega)

/-- Retreat by three: the wall drops three cells and stays black. -/
theorem top_minus_three {x : Row} {k : Nat} (h : Top x (k + 5)) (hb : x (k + 5) = true)
    (h4 : x (k + 4) = false) (h3 : x (k + 3) = false) (h2 : x (k + 2) = false) (h1 : x (k + 1) = true) :
    Top (step x) (k + 2) ∧ step x (k + 2) = true := by
  obtain ⟨r5, r6, hr⟩ := top_fall_rain h hb h4 h3
  have r4 : step x (k + 4) = false := by
    show xor (x (k + 4)) (x (k + 3) || x (k + 2)) = false
    rw [h4, h3, h2]; rfl
  have r3 : step x (k + 3) = true := by
    show xor (x (k + 3)) (x (k + 2) || x (k + 1)) = true
    rw [h3, h2, h1]; rfl
  have r2 : step x (k + 2) = true := by
    show xor (x (k + 2)) (x (k + 1) || x k) = true
    rw [h2, h1]; rfl
  refine ⟨⟨by rw [show k + 2 + 1 = k + 3 from rfl, r2, r3], ?_⟩, r2⟩
  intro j hj
  by_cases c3 : j = k + 3
  · subst c3; rw [show k + 3 + 1 = k + 4 from rfl, r3, r4]; rfl
  · by_cases c4 : j = k + 4
    · subst c4; rw [show k + 4 + 1 = k + 5 from rfl, r4, r5]; rfl
    · exact hr j (by omega)

/-! ## The robust backward front -/

/-- The eighteen windows, low to high; the top wall is their last two cells. -/
def B11 : List (List Bool) := [
  [false, true, false, false, true, false, false, false, false, true, true],
  [false, false, true, false, true, false, false, false, false, true, true],
  [true, false, true, false, true, false, false, false, false, true, true],
  [false, true, false, true, false, true, false, false, false, true, true],
  [false, false, true, true, false, true, false, false, false, true, true],
  [true, false, true, true, false, true, false, false, false, true, true],
  [false, true, false, true, true, true, false, false, false, true, true],
  [false, false, true, true, true, true, false, false, false, true, true],
  [true, false, true, true, true, true, false, false, false, true, true],
  [false, true, false, false, true, false, false, true, false, true, true],
  [false, false, true, false, true, false, false, true, false, true, true],
  [true, false, true, false, true, false, false, true, false, true, true],
  [false, true, false, true, false, true, false, true, false, true, true],
  [false, false, true, true, false, true, false, true, false, true, true],
  [true, false, true, true, false, true, false, true, false, true, true],
  [false, true, false, true, true, true, false, true, false, true, true],
  [false, false, true, true, true, true, false, true, false, true, true],
  [true, false, true, true, true, true, false, true, false, true, true]]

/-- A row with its window of eleven cells from `L` in `B11` and rain above it. -/
def Front (x : Row) (L : Nat) : Prop :=
  seg x L 11 ∈ B11 ∧ ∀ j, L + 10 ≤ j → x (j + 1) = !x j

/-- A window with seven cells of rain over its last. -/
def inp (w : List Bool) : List Bool := w.take 10 ++ alt (w.getD 10 false) 7

theorem chk_mem : ∀ w, w ∈ B11 → ∀ p1 p2 : Bool, ((back p1 p2 (inp w)).drop 3).take 11 ∈ B11 := by decide +kernel
theorem chk_a : ∀ w, w ∈ B11 → ∀ p1 p2 : Bool,
    (back p1 p2 (inp w)).getD 14 false = !(back p1 p2 (inp w)).getD 13 false := by decide +kernel
theorem chk_b : ∀ w, w ∈ B11 → ∀ p1 p2 : Bool,
    (back p1 p2 (inp w)).getD 15 false = !(inp w).getD 15 false := by decide +kernel
theorem chk_c : ∀ w, w ∈ B11 → ∀ p1 p2 : Bool,
    (back p1 p2 (inp w)).getD 16 false = !(inp w).getD 16 false := by decide +kernel
theorem chk_d : ∀ w, w ∈ B11 → ∀ p1 p2 : Bool,
    (back p1 p2 (inp w)).getD 15 false = !(back p1 p2 (inp w)).getD 14 false := by decide +kernel
theorem chk_wall : ∀ w, w ∈ B11 → w.getD 9 false = w.getD 10 false := by decide +kernel

theorem seg_inp {x : Row} {L : Nat} (h : ∀ j, L + 10 ≤ j → x (j + 1) = !x j) : seg x L 17 = inp (seg x L 11) := by
  have e1 : seg x L 11 = seg x L 10 ++ seg x (L + 10) 1 := seg_append x 10 1 L
  have e2 : (seg x L 11).take 10 = seg x L 10 := by
    rw [e1]; exact List.take_left' (seg_length x 10 L)
  have e3 : (seg x L 11).getD 10 false = x (L + 10) := seg_getD x 11 L 10 (by omega)
  show seg x L 17 = (seg x L 11).take 10 ++ alt ((seg x L 11).getD 10 false) 7
  rw [e2, e3, ← seg_alt h 7 (L + 10) (Nat.le_refl _)]
  exact seg_append x 10 7 L

/-- **The robust backward front.** Every predecessor of a front is a front three cells higher, whatever lies below the window. -/
theorem front_back {z x : Row} {L : Nat} (hL : 2 ≤ L) (hs : step z = x) (hf : Front x L) : Front z (L + 3) := by
  obtain ⟨hw, hr⟩ := hf
  have e : seg z L 17 = back (z (L - 1)) (z (L - 2)) (inp (seg x L 11)) := by
    rw [back_seg hs 17 L hL, seg_inp hr]
  have ha := chk_a _ hw (z (L - 1)) (z (L - 2))
  have hb := chk_b _ hw (z (L - 1)) (z (L - 2))
  have hc := chk_c _ hw (z (L - 1)) (z (L - 2))
  have hd := chk_d _ hw (z (L - 1)) (z (L - 2))
  have hm := chk_mem _ hw (z (L - 1)) (z (L - 2))
  rw [← e] at ha hb hc hd hm
  have g : ∀ i, i < 17 → (seg z L 17).getD i false = z (L + i) := fun i h => seg_getD z 17 L i h
  rw [g 13 (by omega), g 14 (by omega)] at ha
  rw [g 14 (by omega), g 15 (by omega)] at hd
  rw [g 15 (by omega)] at hb
  rw [g 16 (by omega)] at hc
  have q : ∀ i, i < 17 → (inp (seg x L 11)).getD i false = x (L + i) := by
    intro i h; rw [← seg_inp hr]; exact seg_getD x 17 L i h
  rw [q 15 (by omega)] at hb
  rw [q 16 (by omega)] at hc
  have hwin : seg z (L + 3) 11 = ((seg z L 17).drop 3).take 11 := by
    have e1 : seg z L 17 = seg z L 3 ++ seg z (L + 3) 14 := seg_append z 3 14 L
    have e2 : seg z (L + 3) 14 = seg z (L + 3) 11 ++ seg z (L + 3 + 11) 3 := seg_append z 11 3 (L + 3)
    rw [e1, List.drop_left' (seg_length z 3 L), e2]
    exact (List.take_left' (seg_length z 11 (L + 3))).symm
  refine ⟨by rw [hwin]; exact hm, ?_⟩
  have htail := tail_of_compl hs (J := L + 15) (fun j hj => hr j (by omega)) hb hc
  intro j hj
  by_cases c1 : j = L + 13
  · subst c1; exact ha
  · by_cases c2 : j = L + 14
    · subst c2; exact hd
    · exact htail j (by omega)

theorem front_iter {x : Row} {L P : Nat} (hL : 2 ≤ L) (h : Front x L) (hper : iter x P = x) :
    ∀ i, i ≤ P → Front (iter x (P - i)) (L + 3 * i) := by
  intro i
  induction i with
  | zero => intro _; simpa [hper] using h
  | succ i ih =>
    intro hi
    have hs : step (iter x (P - (i + 1))) = iter x (P - i) := by
      have : P - i = (P - (i + 1)) + 1 := by omega
      rw [this]; rfl
    have := front_back (by omega) hs (ih (by omega))
    have e : L + 3 * i + 3 = L + 3 * (i + 1) := by omega
    rw [e] at this
    exact this

/-- **A row with a front is not periodic.** So a periodic row with a rain tail never shows one of the eighteen windows at its top. -/
theorem front_not_periodic {x : Row} {L P : Nat} (hL : 2 ≤ L) (h : Front x L) (hP : 0 < P) : iter x P ≠ x := by
  intro hper
  have hf := front_iter hL h hper P (Nat.le_refl P)
  have e0 : P - P = 0 := by omega
  rw [e0] at hf
  have hf' : Front x (L + 3 * P) := hf
  obtain ⟨hw, _⟩ := hf'
  have hwall := chk_wall _ hw
  rw [seg_getD x 11 _ 9 (by omega), seg_getD x 11 _ 10 (by omega)] at hwall
  have hr := h.2 (L + 3 * P + 9) (by omega)
  have : L + 3 * P + 9 + 1 = L + 3 * P + 10 := rfl
  rw [this, ← hwall] at hr
  cases hb : x (L + 3 * P + 9) <;> simp [hb] at hr

/-! ## Forward transport of finite windows -/

/-- Compute a forward word starting two cells above the input start. -/
def shrink : List Bool → List Bool
  | a :: b :: c :: rest => xor c (b || a) :: shrink (b :: c :: rest)
  | _ => []

def shrinkN (word : List Bool) : Nat → List Bool
  | 0 => word
  | r + 1 => shrinkN (shrink word) r

theorem shrink_seg (z : Row) (A w : Nat) :
    shrink (seg z A (w + 2)) = seg (step z) (A + 2) w := by
  induction w generalizing A with
  | zero => rfl
  | succ w ih =>
    change xor (z (A + 2)) (z (A + 1) || z A) :: shrink (seg z (A + 1) (w + 2)) =
      step z (A + 2) :: seg (step z) (A + 2 + 1) w
    rw [ih] <;> rfl

/-- Exact locality in the original spatial coordinate, for every tick and width. -/
theorem shrinkN_seg (z : Row) (A r w : Nat) :
    shrinkN (seg z A (2 * r + w)) r = seg (iter z r) (A + 2 * r) w := by
  induction r generalizing z A w with
  | zero => simp [shrinkN, iter, Rule30FrozenRuler.iter]
  | succ r ih =>
    have length : 2 * (r + 1) + w = (2 * r + w) + 2 := by omega
    have pos : A + 2 + 2 * r = A + 2 * (r + 1) := by omega
    have time : iter (step z) r = iter z (r + 1) := by
      rw [Nat.add_comm r 1, iter_add z 1 r] <;> rfl
    rw [shrinkN, length, shrink_seg, ih, pos, time]

def contexts : Nat → List (List Bool)
  | 0 => [[]]
  | n+1 => (contexts n).map (false :: ·) ++ (contexts n).map (true :: ·)

theorem mem_contexts (c : List Bool) : c ∈ contexts c.length := by
  induction c with
  | nil => simp [contexts]
  | cons b bs ih =>
    change b :: bs ∈ (contexts bs.length).map (false :: ·) ++ (contexts bs.length).map (true :: ·)
    cases b with
    | false => exact List.mem_append_left _ (List.mem_map.mpr ⟨bs,ih,rfl⟩)
    | true => exact List.mem_append_right _ (List.mem_map.mpr ⟨bs,ih,rfl⟩)

/-! ## Three advances leave two letters -/

/-- An alternating tail above one wall excludes every higher wall. -/
private theorem excludes_higher {x : Row} {d e : Nat} (h : Top x d) (lt : d < e) : ¬Top x e := by
  intro upper
  have alt := h.2 e (by omega)
  rw [upper.1] at alt
  cases b : x e <;> simp [b] at alt

private theorem both_false {u v : Bool} (h : (u || v) = false) : u = false ∧ v = false := by
  cases u <;> cases v <;> simp_all

theorem marker {x : Row} (k : Nat) (a : Top x (k+5)) (b : Top (step x) (k+2)) :
    seg x (k+1) 6 = [true,false,false,false,true,true] := by
  have h5 : x (k+5) = true := by
    cases h : x (k+5) with
    | true => rfl
    | false => exact False.elim (excludes_higher b (by omega) (top_up a h).1)
  have white : (x (k+4) || x (k+3)) = false := by
    cases h : x (k+4) || x (k+3) with
    | false => rfl
    | true => exact False.elim (excludes_higher b (by omega) (top_stay a h5 h).1)
  obtain ⟨h4,h3⟩ := both_false white
  have h2 : x (k+2) = false := by
    cases h : x (k+2) with
    | false => rfl
    | true => exact False.elim (excludes_higher b (by omega) (top_minus_one a h5 h4 h3 h).1)
  have h1 : x (k+1) = true := by
    cases h : x (k+1) with
    | true => rfl
    | false => exact False.elim (excludes_higher b (by omega) (top_minus_two a h5 h4 h3 h2 h).1)
  have h6 : x (k+6) = true := a.1.trans h5
  change [x (k+1), x (k+2), x (k+3), x (k+4), x (k+5), x (k+6)] = _
  rw [h1,h2,h3,h4,h5,h6]

def wordA : List Bool := [false,false,true,true,true,true,false,false,false,true,true]
def wordB : List Bool := [false,true,false,true,true,true,false,false,false,true,true]
private def mark : List Bool := [true,false,false,false,true,true]

private theorem known : wordA ∈ B11 ∧ wordB ∈ B11 := by decide +kernel

/- Three forward retreat markers, displaced three cells at each step.
The ten free lower bits suffice for all three observations by exact locality. -/
set_option maxRecDepth 8192 in
set_option maxHeartbeats 1200000 in
private theorem local_cut : ∀ c, c ∈ contexts 10 →
    (((shrink (c ++ mark)).drop 5).take 6 = mark) →
    ((shrinkN (c ++ mark) 2).take 6 = mark) →
    (c ++ mark).drop 5 = wordA ∨ (c ++ mark).drop 5 = wordB := by decide +kernel

private theorem slice_seg (x : Row) (L a m b : Nat) :
    ((seg x L (a+(m+b))).drop a).take m = seg x (L+a) m := by
  rw [seg_append x a (m+b) L, List.drop_left' (seg_length x a L),
    seg_append x m b (L+a), List.take_left' (seg_length x m (L+a))]

theorem deep_words (z : Row) (D : Nat) (hD : 5≤D)
    (a : Top z (D+9)) (b : Top (iter z 1) (D+6))
    (c : Top (iter z 2) (D+3)) (d : Top (iter z 3) D) :
    seg z D 11 = wordA ∨ seg z D 11 = wordB := by
  obtain ⟨k, rfl⟩ : ∃ k, D=k+5 := ⟨D-5, by omega⟩
  have m0 := marker (k+9) a b
  have m1 := marker (k+6) b c
  have m2 := marker (k+3) c d
  let low := seg z k 10
  have whole : low ++ mark = seg z k 16 := by
    rw [seg_append z 10 6 k, m0]
    rfl
  have context : low ∈ contexts 10 := by
    simpa only [low, seg_length] using mem_contexts (seg z k 10)
  have p1 : ((shrink (low ++ mark)).drop 5).take 6 = mark := by
    rw [whole, shrink_seg z k 14, slice_seg (step z) (k+2) 5 6 3]
    exact m1
  have p2 : (shrinkN (low ++ mark) 2).take 6 = mark := by
    rw [whole, shrinkN_seg z k 2 12, seg_append (iter z 2) 6 6 (k+4),
      List.take_left' (seg_length (iter z 2) 6 (k+4))]
    exact m2
  have choices := local_cut low context p1 p2
  rw [whole, seg_append z 5 11 k, List.drop_left' (seg_length z 5 k)] at choices
  exact choices

theorem deep (z : Row) (D : Nat) (hD : 5≤D)
    (a : Top z (D+9)) (b : Top (iter z 1) (D+6))
    (c : Top (iter z 2) (D+3)) (d : Top (iter z 3) D) : Front z D := by
  have choices := deep_words z D hD a b c d
  refine ⟨?_, a.2⟩
  rcases choices with w | w
  · rw [w]; exact known.1
  · rw [w]; exact known.2

/-! ## The language of the letters -/

private theorem incompatible (a b c : Bool) :
    ¬(xor c (b || a) = false ∧ xor false (c || b) = true ∧ xor true (false || c) = true) := by
  cases a <;> cases b <;> cases c <;> decide

private theorem readB {x : Row} {L : Nat} (w : seg x L 11 = wordB) (i : Nat) (hi : i < 11) :
    x (L+i) = wordB.getD i false := by rw [←w,seg_getD _ _ _ _ hi]

/-- The deeper B is on the predecessor row `z`. If its successor had B
three cells lower, the successor bits at offsets 2,3,4 would be 0,1,1,
while the input bits at offsets 3,4 would be 0,1. No choice of the other
three inputs is consistent with that update. -/
theorem no_BB (z : Row) (L : Nat) (deep : seg z (L+3) 11 = wordB) :
    seg (step z) L 11 ≠ wordB := by
  intro shallow
  have s2 : step z (L+2) = false := readB shallow 2 (by decide)
  have s3 : step z (L+3) = true := readB shallow 3 (by decide)
  have s4 : step z (L+4) = true := readB shallow 4 (by decide)
  have b3 : z (L+3) = false := readB deep 0 (by decide)
  have b4 : z (L+4) = true := readB deep 1 (by decide)
  change xor (z (L+2)) (z (L+1) || z L) = false at s2
  change xor (z (L+3)) (z (L+2) || z (L+1)) = true at s3
  change xor (z (L+4)) (z (L+3) || z (L+2)) = true at s4
  rw [b3] at s3
  rw [b4,b3] at s4
  exact incompatible (z L) (z (L+1)) (z (L+2)) ⟨s2,s3,s4⟩

/-- Extend bit 10 by alternation above the given eleven-bit source word. -/
def source (w low L j : Nat) : Bool :=
  if j < L then low.testBit j else if j < L+10 then w.testBit (j-L)
  else if (j-(L+10)) % 2 = 0 then w.testBit 10 else !(w.testBit 10)

private theorem read {x : Row} {L : Nat} {w : List Bool} (h : seg x L 11 = w) (i : Nat) (hi : i < 11) :
    x (L + i) = w.getD i false := by
  rw [← h, seg_getD _ _ _ _ hi]

private theorem or_false' {a b : Bool} (h : (a || b) = false) : a = false ∧ b = false := by
  cases a <;> cases b <;> simp_all

/-- **`A` cannot occur three times in succession.** The deepest window is on the row `z`, and the two later
windows are on its forward images, three cells lower each. -/
theorem no_AAA (z : Row) (L : Nat) (deep : seg z (L + 6) 11 = wordA)
    (mid : seg (step z) (L + 3) 11 = wordA) (top : seg (step (step z)) L 11 = wordA) : False := by
  -- the window on the top row against the middle row
  have v2 : step (step z) (L + 2) = true := read top 2 (by decide)
  have v4 : step (step z) (L + 4) = true := read top 4 (by decide)
  have u3 : step z (L + 3) = false := read mid 0 (by decide)
  have u4 : step z (L + 4) = false := read mid 1 (by decide)
  have u5 : step z (L + 5) = true := read mid 2 (by decide)
  have u7 : step z (L + 7) = true := read mid 4 (by decide)
  have z6 : z (L + 6) = false := read deep 0 (by decide)
  have z7 : z (L + 7) = false := read deep 1 (by decide)
  change xor (step z (L + 4)) (step z (L + 3) || step z (L + 2)) = true at v4
  rw [u4, u3] at v4
  have u2 : step z (L + 2) = true := by simpa using v4
  change xor (step z (L + 2)) (step z (L + 1) || step z L) = true at v2
  rw [u2] at v2
  have w1 : (step z (L + 1) || step z L) = false := by simpa using v2
  have u1 : step z (L + 1) = false := (or_false' w1).1
  -- the same two steps one row deeper
  change xor (z (L + 7)) (z (L + 6) || z (L + 5)) = true at u7
  rw [z7, z6] at u7
  have z5 : z (L + 5) = true := by simpa using u7
  change xor (z (L + 5)) (z (L + 4) || z (L + 3)) = true at u5
  rw [z5] at u5
  have w2 : (z (L + 4) || z (L + 3)) = false := by simpa using u5
  obtain ⟨z4, z3⟩ := or_false' w2
  change xor (z (L + 4)) (z (L + 3) || z (L + 2)) = false at u4
  rw [z4, z3] at u4
  have z2 : z (L + 2) = false := by simpa using u4
  change xor (z (L + 3)) (z (L + 2) || z (L + 1)) = false at u3
  rw [z3, z2] at u3
  have z1 : z (L + 1) = false := by simpa using u3
  change xor (z (L + 2)) (z (L + 1) || z L) = true at u2
  rw [z2, z1] at u2
  have z0 : z L = true := by simpa using u2
  -- wheel L + 1 of the middle row cannot be white
  cases L with
  | zero =>
    have e : step z 1 = xor (z 1) (z 0) := rfl
    simp only [Nat.zero_add] at u1 z1 z0
    rw [e, z1, z0] at u1
    cases u1
  | succ k =>
    have e : step z (k + 1 + 1) = xor (z (k + 1 + 1)) (z (k + 1) || z k) := rfl
    rw [e, z1, z0] at u1
    cases u1

/-! ## Witnesses on anchored rows -/

/-- The row `x` shows the word `w` from cell `L`, with rain above it. -/
def Shows (x : Row) (L : Nat) (w : List Bool) : Prop :=
  seg x L 11 = w ∧ ∀ j, L + 10 ≤ j → x (j + 1) = !x j

theorem source_tail (w low L j : Nat) (hj : L + 10 ≤ j) :
    source w low L (j + 1) = !source w low L j := by
  by_cases a : (j - (L + 10)) % 2 = 0
  · simp [source, show ¬j < L by omega, show ¬j + 1 < L by omega,
      show ¬j < L + 10 by omega, show ¬j + 1 < L + 10 by omega, a] <;> omega
  · simp [source, show ¬j < L by omega, show ¬j + 1 < L by omega,
      show ¬j < L + 10 by omega, show ¬j + 1 < L + 10 by omega, a] <;> omega

/-- A forward image keeps the rain, given the few cells that the general lemma does not reach. -/
private theorem step_shows {x : Row} {L P : Nat} {w : List Bool} (h : ∀ j, L ≤ j → x (j + 1) = !x j)
    (hw : seg (step x) P 11 = w)
    (near : ∀ j : Fin (L + 2), P + 10 ≤ j.val → step x (j.val + 1) = !step x j.val) :
    Shows (step x) P w := by
  refine ⟨hw, fun j hj => ?_⟩
  by_cases c : j < L + 2
  · exact near ⟨j, c⟩ hj
  · exact step_rain_tail h j (by omega)

/-- `AA`: the row with low bits 33 below `A`. -/
theorem witness_AA :
    source 1596 33 6 0 = true ∧ Shows (source 1596 33 6) 6 wordA ∧ Shows (step (source 1596 33 6)) 3 wordA := by
  have t := source_tail 1596 33 6
  refine ⟨by decide, ⟨by decide +kernel, t⟩, ?_⟩
  exact step_shows (L := 16) t (by decide +kernel) (by decide +kernel)

/-- `AB` in backward order: `B` on the deeper row. The low bits are 7. -/
theorem witness_AB :
    source 1594 7 4 0 = true ∧ Shows (source 1594 7 4) 4 wordB ∧ Shows (step (source 1594 7 4)) 1 wordA := by
  have t := source_tail 1594 7 4
  refine ⟨by decide, ⟨by decide +kernel, t⟩, ?_⟩
  exact step_shows (L := 14) t (by decide +kernel) (by decide +kernel)

/-- `BA` in backward order: `A` on the deeper row. The low bits are 11. -/
theorem witness_BA :
    source 1596 11 4 0 = true ∧ Shows (source 1596 11 4) 4 wordA ∧ Shows (step (source 1596 11 4)) 1 wordB := by
  have t := source_tail 1596 11 4
  refine ⟨by decide, ⟨by decide +kernel, t⟩, ?_⟩
  exact step_shows (L := 14) t (by decide +kernel) (by decide +kernel)

/-- `ABA` on one row: both ends of the pair of pairs share one shallow history. The low bits are 97. -/
theorem witness_ABA :
    source 1596 97 7 0 = true ∧ Shows (source 1596 97 7) 7 wordA ∧ Shows (step (source 1596 97 7)) 4 wordB ∧
      Shows (step (step (source 1596 97 7))) 1 wordA := by
  have t := source_tail 1596 97 7
  have s1 : Shows (step (source 1596 97 7)) 4 wordB := step_shows (L := 17) t (by decide +kernel) (by decide +kernel)
  refine ⟨by decide, ⟨by decide +kernel, t⟩, s1, ?_⟩
  exact step_shows (L := 19) (fun j hj => s1.2 j (by omega)) (by decide +kernel) (by decide +kernel)

/-! ## The shield -/

namespace Reset

/-- The reset word. -/
def F (b u v : Bool) : List Bool := [false, b, !b, true, u, true, false, v, false, true]

/-- The first seven cells of the word. -/
def W (b u : Bool) : List Bool := [false, b, !b, true, u, true, false]

/-- The bit of the new word. -/
def newbit (b u p1 p2 : Bool) : Bool := if b || (!p1 && !p2) then !u else u

/-- **The reset.** Under any two lower cells the output on cells 3 to 9 of the word is the shape `W` with the new bit. -/
theorem reset : ∀ b u v p1 p2 : Bool, ((back p1 p2 (F b u v)).drop 3).take 7 = W (newbit b u p1 p2) (!v) := by decide

/-- **Nothing passes.** Above the word the output is the same function of the input, whatever the bits of the word and the cells below it. -/
theorem above (b u v p1 p2 : Bool) (r : List Bool) : (back p1 p2 (F b u v ++ r)).drop 10 = back false true r := by
  cases b <;> cases u <;> cases v <;> cases p1 <;> cases p2 <;> rfl

/-- **Again.** If the old row reads `s, !s, s` above the word, the new word is a reset word again, three cells higher. -/
theorem again : ∀ b u v s p1 p2 : Bool,
    ((back p1 p2 (F b u v ++ [s, !s, s])).drop 3).take 10 = F (newbit b u p1 p2) (!v) (!s) := by decide

/-- The wall letters are reset words, with `u` black and `v` white, under one black cell. -/
theorem letters : wordA = F false true false ++ [true] ∧ wordB = F true true false ++ [true] := by decide

end Reset

/-! ## Closed sets of windows -/

namespace WindowClosed

/-- A window with seven cells of rain over its last. -/
def inp (W : Nat) (w : List Bool) : List Bool := w.take (W - 1) ++ alt (w.getD (W - 1) false) 7

/-- The image of a window under the backward tick with lower cells `p1`, `p2`. -/
def next (W : Nat) (w : List Bool) (p1 p2 : Bool) : List Bool := ((back p1 p2 (inp W w)).drop 3).take W

/-- The finite checks. -/
structure Closed (W : Nat) (S : List (List Bool)) : Prop where
  pos : 1 ≤ W
  mem : ∀ w, w ∈ S → ∀ p1 p2 : Bool, next W w p1 p2 ∈ S
  a : ∀ w, w ∈ S → ∀ p1 p2 : Bool, (back p1 p2 (inp W w)).getD (W + 3) false = !(back p1 p2 (inp W w)).getD (W + 2) false
  d : ∀ w, w ∈ S → ∀ p1 p2 : Bool, (back p1 p2 (inp W w)).getD (W + 4) false = !(back p1 p2 (inp W w)).getD (W + 3) false
  b : ∀ w, w ∈ S → ∀ p1 p2 : Bool, (back p1 p2 (inp W w)).getD (W + 4) false = !(inp W w).getD (W + 4) false
  c : ∀ w, w ∈ S → ∀ p1 p2 : Bool, (back p1 p2 (inp W w)).getD (W + 5) false = !(inp W w).getD (W + 5) false

/-- A row with its window of `W` cells from `L` in `S` and rain above it. -/
def Held (W : Nat) (S : List (List Bool)) (x : Row) (L : Nat) : Prop :=
  seg x L W ∈ S ∧ ∀ j, L + W - 1 ≤ j → x (j + 1) = !x j

theorem seg_inp {W : Nat} (hW : 1 ≤ W) {x : Row} {L : Nat} (h : ∀ j, L + W - 1 ≤ j → x (j + 1) = !x j) :
    seg x L (W + 6) = inp W (seg x L W) := by
  have e1 : seg x L W = seg x L (W - 1) ++ seg x (L + (W - 1)) 1 := by
    have := seg_append x (W - 1) 1 L
    rwa [show W - 1 + 1 = W by omega] at this
  have e2 : (seg x L W).take (W - 1) = seg x L (W - 1) := by
    rw [e1]; exact List.take_left' (seg_length x (W - 1) L)
  have e3 : (seg x L W).getD (W - 1) false = x (L + (W - 1)) := seg_getD x W L (W - 1) (by omega)
  show seg x L (W + 6) = (seg x L W).take (W - 1) ++ alt ((seg x L W).getD (W - 1) false) 7
  rw [e2, e3, ← seg_alt (J := L + (W - 1)) (fun j hj => h j (by omega)) 7 (L + (W - 1)) (Nat.le_refl _)]
  have := seg_append x (W - 1) 7 L
  rwa [show W - 1 + 7 = W + 6 by omega] at this

private theorem seg_next (W : Nat) {z : Row} {L : Nat} :
    seg z (L + 3) W = ((seg z L (W + 6)).drop 3).take W := by
  have e1 : seg z L (W + 6) = seg z L 3 ++ seg z (L + 3) (W + 3) := by
    have := seg_append z 3 (W + 3) L
    rwa [show 3 + (W + 3) = W + 6 by omega] at this
  have e2 : seg z (L + 3) (W + 3) = seg z (L + 3) W ++ seg z (L + 3 + W) 3 := seg_append z W 3 (L + 3)
  rw [e1, List.drop_left' (seg_length z 3 L), e2]
  exact (List.take_left' (seg_length z W (L + 3))).symm

/-- One tick, on rows. -/
theorem next_seg {W : Nat} {S : List (List Bool)} (C : Closed W S) {z x : Row} {L : Nat} (hL : 2 ≤ L) (hs : step z = x)
    (hf : Held W S x L) : seg z (L + 3) W = next W (seg x L W) (z (L - 1)) (z (L - 2)) := by
  have e : seg z L (W + 6) = back (z (L - 1)) (z (L - 2)) (inp W (seg x L W)) := by
    rw [back_seg hs (W + 6) L hL, seg_inp C.pos hf.2]
  rw [seg_next, e]; rfl

/-- **The tick.** Every predecessor of a held row is held three cells higher, whatever lies below the window. -/
theorem held_back {W : Nat} {S : List (List Bool)} (C : Closed W S) {z x : Row} {L : Nat} (hL : 2 ≤ L) (hs : step z = x)
    (hf : Held W S x L) : Held W S z (L + 3) := by
  have hW := C.pos
  obtain ⟨hw, hr⟩ := id hf
  have e : seg z L (W + 6) = back (z (L - 1)) (z (L - 2)) (inp W (seg x L W)) := by
    rw [back_seg hs (W + 6) L hL, seg_inp hW hr]
  have ha := C.a _ hw (z (L - 1)) (z (L - 2))
  have hb := C.b _ hw (z (L - 1)) (z (L - 2))
  have hc := C.c _ hw (z (L - 1)) (z (L - 2))
  have hd := C.d _ hw (z (L - 1)) (z (L - 2))
  have hm := C.mem _ hw (z (L - 1)) (z (L - 2))
  rw [← e] at ha hb hc hd
  have g : ∀ i, i < W + 6 → (seg z L (W + 6)).getD i false = z (L + i) := fun i h => seg_getD z (W + 6) L i h
  rw [g (W + 2) (by omega), g (W + 3) (by omega)] at ha
  rw [g (W + 3) (by omega), g (W + 4) (by omega)] at hd
  rw [g (W + 4) (by omega)] at hb
  rw [g (W + 5) (by omega)] at hc
  have q : ∀ i, i < W + 6 → (inp W (seg x L W)).getD i false = x (L + i) := by
    intro i h; rw [← seg_inp hW hr]; exact seg_getD x (W + 6) L i h
  rw [q (W + 4) (by omega)] at hb
  rw [q (W + 5) (by omega)] at hc
  refine ⟨by rw [next_seg C hL hs hf]; exact hm, ?_⟩
  have htail := tail_of_compl hs (J := L + (W + 4)) (fun j hj => hr j (by omega)) hb
    (by rw [show L + (W + 4) + 1 = L + (W + 5) by omega]; exact hc)
  intro j hj
  by_cases c1 : j = L + (W + 2)
  · subst c1; exact ha
  · by_cases c2 : j = L + (W + 3)
    · subst c2; exact hd
    · exact htail j (by omega)

/-- **For ever.** Every row `n` ticks before a held row is held `3 n` cells higher. -/
theorem held_forever {W : Nat} {S : List (List Bool)} (C : Closed W S) {x : Row} {L : Nat} (hL : 2 ≤ L) (h : Held W S x L) :
    ∀ n z, iter z n = x → Held W S z (L + 3 * n) := by
  intro n
  induction n with
  | zero => intro z hz; rw [show iter z 0 = z from rfl] at hz; subst hz; exact h
  | succ n ih =>
    intro z hz
    have e : iter z (1 + n) = iter (iter z 1) n := iter_add z 1 n
    rw [Nat.add_comm n 1, e] at hz
    have := held_back C (by omega) (show step z = iter z 1 from rfl) (ih (iter z 1) hz)
    have e2 : L + 3 * n + 3 = L + 3 * (n + 1) := by omega
    rw [e2] at this
    exact this

end WindowClosed

/-- The predecessor, by triangular recovery of the whole row. -/
def previous (x : Row) : Row
  | 0 => x 0
  | 1 => xor (x 1) (x 0)
  | j + 2 => xor (x (j + 2)) (previous x (j + 1) || previous x j)

theorem xor_twice (a b : Bool) : xor (xor a b) b = a := by
  cases a <;> cases b <;> rfl

theorem step_previous (x : Row) : step (previous x) = x := by
  funext j
  cases j with
  | zero => rfl
  | succ k =>
    cases k with
    | zero => exact xor_twice _ _
    | succ i =>
      rw [step_add, previous]
      exact xor_twice _ _

theorem previous_step (x : Row) : previous (step x) = x := by
  have pair : ∀ i, previous (step x) i = x i ∧ previous (step x) (i + 1) = x (i + 1) := by
    intro i
    induction i with
    | zero => exact ⟨rfl, xor_twice _ _⟩
    | succ i ih =>
      refine ⟨ih.2, ?_⟩
      rw [previous, ih.1, ih.2, step_add]
      exact xor_twice _ _
  funext i
  exact (pair i).1

/-- **Every row has exactly one predecessor,** so a backward tick is well defined and the theorems on predecessors are not empty. -/
theorem predecessor_unique (x : Row) : ∃ z, step z = x ∧ ∀ y, step y = x → y = z :=
  ⟨previous x, step_previous x, fun y h => by rw [← h, previous_step]⟩

/-- `n` backward ticks. -/
def previousN : Nat → Row → Row
  | 0, x => x
  | n + 1, x => previous (previousN n x)

theorem iter_previousN (x : Row) (n : Nat) : iter (previousN n x) n = x := by
  induction n with
  | zero => rfl
  | succ n ih =>
    have e := iter_add (previousN (n + 1) x) 1 n
    rw [Nat.add_comm 1 n] at e
    rw [e]
    show iter (step (previous (previousN n x))) n = x
    rw [step_previous]; exact ih

namespace WindowClosed

/-- **A held row is not periodic**, when each window of the set ends in the wall's equal pair. -/
theorem held_not_periodic {W : Nat} {S : List (List Bool)} (C : Closed W S) (hW : 2 ≤ W)
    (wall : ∀ w, w ∈ S → w.getD (W - 2) false = w.getD (W - 1) false)
    {x : Row} {L P : Nat} (hL : 2 ≤ L) (h : Held W S x L) (hP : 0 < P) : iter x P ≠ x := by
  intro hper
  have hf := held_forever C hL h P x hper
  have hwall := wall _ hf.1
  rw [seg_getD x W _ (W - 2) (by omega), seg_getD x W _ (W - 1) (by omega)] at hwall
  have hr := h.2 (L + 3 * P + (W - 2)) (by omega)
  rw [show L + 3 * P + (W - 2) + 1 = L + 3 * P + (W - 1) by omega, ← hwall] at hr
  cases hb : x (L + 3 * P + (W - 2)) <;> simp [hb] at hr

/-- The two letters. -/
def letterSet : List (List Bool) := [wordA, wordB]

/-- **The letters are closed.** A row showing a letter with rain above it shows a letter at every backward tick. -/
theorem letters_closed : Closed 11 letterSet :=
  ⟨by decide, by decide, by decide, by decide, by decide, by decide⟩

/-- **After `B` comes `A`,** for every pair of lower cells. -/
theorem letter_after_B {z x : Row} {L : Nat} (hL : 2 ≤ L) (hs : step z = x) (h : Held 11 letterSet x L)
    (hb : seg x L 11 = wordB) : seg z (L + 3) 11 = wordA := by
  rw [next_seg letters_closed hL hs h, hb]
  generalize z (L - 1) = p1
  generalize z (L - 2) = p2
  revert p1 p2
  decide

/-- **After `A` comes `A` exactly when the two cells of the predecessor below the window are white.** -/
theorem letter_after_A {z x : Row} {L : Nat} (hL : 2 ≤ L) (hs : step z = x) (h : Held 11 letterSet x L)
    (ha : seg x L 11 = wordA) : seg z (L + 3) 11 = if (z (L - 1) || z (L - 2)) then wordB else wordA := by
  rw [next_seg letters_closed hL hs h, ha]
  generalize z (L - 1) = p1
  generalize z (L - 2) = p2
  revert p1 p2
  decide

/-! ## Windows as numbers

The checks on a closed set are finite, and the kernel runs them on numbers. A window of `W` cells is a number. `load` puts the two lower
cells under it and rain over it, `run` is the backward sweep cell by cell, and `nxt` reads the image window off the result. The theorems say
this is `next` on words. -/

/-- A word of `W` cells from a number, low to high. -/
def dec (W n : Nat) : List Bool := seg n.testBit 0 W

/-- One cell of the sweep: bit `i + 2` takes the inverse rule from the two bits below it. -/
def sw (i y : Nat) : Nat := y ^^^ ((((y >>> (i + 1)) ||| (y >>> i)) &&& 1) <<< (i + 2))

/-- The sweep. The test on `sw i y` never changes the value, since `0` stays `0`; it forces each cell as the kernel reaches it. -/
def run : Nat → Nat → Nat → Nat
  | 0, _, y => y
  | f + 1, i, y => cond (Nat.beq (sw i y) 0) 0 (run f (i + 1) (sw i y))

/-- The two lower cells, the window and six cells of rain over a black top. -/
def load (W n : Nat) (p1 p2 : Bool) : Nat := ((n ||| (42 <<< W)) <<< 2) ||| (p1.toNat <<< 1) ||| p2.toNat

/-- The whole sweep on a window. -/
def image (W n : Nat) (p1 p2 : Bool) : Nat := run (W + 6) 0 (load W n p1 p2)

/-- The image window. -/
def nxt (W n : Nat) (p1 p2 : Bool) : Nat := (image W n p1 p2 >>> 5) &&& (2 ^ W - 1)

/-- The finite check on one window number: a black top cell, and under each pair of lower cells rain resumes and the image window is in `T`. -/
def Fast (W : Nat) (T : List Nat) (n : Nat) : Prop :=
  n >>> (W - 1) = 1 ∧ ∀ p1 p2 : Bool, image W n p1 p2 >>> (W + 4) = 5 ∧ nxt W n p1 p2 ∈ T

instance (W : Nat) (T : List Nat) (n : Nat) : Decidable (Fast W T n) := by unfold Fast; infer_instance

theorem sw_bit (i y j : Nat) :
    (sw i y).testBit j = if j = i + 2 then xor (y.testBit (i + 2)) (y.testBit (i + 1) || y.testBit i) else y.testBit j := by
  have hone : ∀ a : Nat, (a &&& 1).testBit 0 = a.testBit 0 := by
    intro a; simp
  have hhi : ∀ (a k : Nat), (a &&& 1).testBit (k + 1) = false := by
    intro a k; simp [Nat.testBit_succ]
  unfold sw
  rw [Nat.testBit_xor, Nat.testBit_shiftLeft]
  by_cases c : j = i + 2
  · subst c
    simp only [ge_iff_le, Nat.le_refl, decide_true, Bool.true_and, Nat.sub_self, ite_true]
    rw [hone, Nat.testBit_or, Nat.testBit_shiftRight, Nat.testBit_shiftRight]
    simp
  · rw [ite_eq_right c]
    by_cases d : i + 2 ≤ j
    · obtain ⟨k, rfl⟩ : ∃ k, j = i + 2 + (k + 1) := ⟨j - (i + 2) - 1, by omega⟩
      rw [show i + 2 + (k + 1) - (i + 2) = k + 1 by omega, hhi]
      simp
    · simp [d]

theorem run_zero (f i : Nat) : run f i 0 = 0 := by
  induction f generalizing i with
  | zero => rfl
  | succ f ih =>
    have : sw i 0 = 0 := by simp [sw]
    simp [run, this]

theorem run_succ (f i y : Nat) : run (f + 1) i y = run f (i + 1) (sw i y) := by
  show cond (Nat.beq (sw i y) 0) 0 (run f (i + 1) (sw i y)) = _
  cases h : Nat.beq (sw i y) 0 with
  | false => rfl
  | true =>
    have : sw i y = 0 := Nat.eq_of_beq_eq_true h
    rw [this, run_zero]; rfl

/-- The sweep leaves every bit below its start alone. -/
theorem run_low (f i y j : Nat) (hj : j < i + 2) : (run f i y).testBit j = y.testBit j := by
  induction f generalizing i y with
  | zero => rfl
  | succ f ih =>
    rw [run_succ, ih (i + 1) (sw i y) (by omega), sw_bit, ite_eq_right (by omega)]

/-- And every bit above its end. -/
theorem run_high (f i y j : Nat) (hj : i + 2 + f ≤ j) : (run f i y).testBit j = y.testBit j := by
  induction f generalizing i y with
  | zero => rfl
  | succ f ih =>
    rw [run_succ, ih (i + 1) (sw i y) (by omega), sw_bit, ite_eq_right (by omega)]

/-- **The sweep is `back`.** -/
theorem run_back (n i y : Nat) :
    seg (run n i y).testBit (i + 2) n = back (y.testBit (i + 1)) (y.testBit i) (seg y.testBit (i + 2) n) := by
  induction n generalizing i y with
  | zero => rfl
  | succ n ih =>
    have hseg : seg (sw i y).testBit (i + 3) n = seg y.testBit (i + 3) n := by
      have : ∀ (m L : Nat), i + 3 ≤ L → seg (sw i y).testBit L m = seg y.testBit L m := by
        intro m
        induction m with
        | zero => intro L _; rfl
        | succ m ihm =>
          intro L hL
          show (sw i y).testBit L :: seg (sw i y).testBit (L + 1) m = y.testBit L :: seg y.testBit (L + 1) m
          rw [ihm (L + 1) (by omega), sw_bit, ite_eq_right (by omega)]
      exact this n (i + 3) (Nat.le_refl _)
    have h2 : (sw i y).testBit (i + 2) = xor (y.testBit (i + 2)) (y.testBit (i + 1) || y.testBit i) := by
      rw [sw_bit, ite_eq_left rfl]
    have h1 : (sw i y).testBit (i + 1) = y.testBit (i + 1) := by
      rw [sw_bit, ite_eq_right (by omega)]
    show (run (n + 1) i y).testBit (i + 2) :: seg (run (n + 1) i y).testBit (i + 3) n =
      xor (y.testBit (i + 2)) (y.testBit (i + 1) || y.testBit i) ::
        back (xor (y.testBit (i + 2)) (y.testBit (i + 1) || y.testBit i)) (y.testBit (i + 1)) (seg y.testBit (i + 3) n)
    rw [run_succ, run_low n (i + 1) (sw i y) (i + 2) (by omega), h2]
    have := ih (i + 1) (sw i y)
    rw [show i + 1 + 2 = i + 3 by omega, show i + 1 + 1 = i + 2 by omega, h2, h1, hseg] at this
    rw [this]

theorem load_low1 (W n : Nat) (p1 p2 : Bool) : (load W n p1 p2).testBit 1 = p1 := by
  have a : ((n ||| (42 <<< W)) <<< 2).testBit 1 = false := by simp [Nat.testBit_shiftLeft]
  cases p1 <;> cases p2 <;> (simp only [load, Nat.testBit_or, a]; decide)

theorem load_low0 (W n : Nat) (p1 p2 : Bool) : (load W n p1 p2).testBit 0 = p2 := by
  have a : ((n ||| (42 <<< W)) <<< 2).testBit 0 = false := by simp
  cases p1 <;> cases p2 <;> (simp only [load, Nat.testBit_or, a]; decide)

theorem load_bit (W n : Nat) (p1 p2 : Bool) (j : Nat) :
    (load W n p1 p2).testBit (j + 2) = (n.testBit j || (42 <<< W).testBit j) := by
  have e : ∀ b : Bool, (b.toNat <<< 1).testBit (j + 2) = false := by
    intro b; rw [Nat.testBit_shiftLeft]; cases b <;> simp [Nat.testBit_succ]
  have f : ∀ b : Bool, b.toNat.testBit (j + 2) = false := by
    intro b; cases b <;> simp [Nat.testBit_succ]
  simp only [load, Nat.testBit_or, e, f, Bool.or_false]
  rw [Nat.testBit_shiftLeft]
  simp [Nat.testBit_or]

theorem seg_ext {f g : Nat → Bool} (m : Nat) : ∀ L M, (∀ i, i < m → f (L + i) = g (M + i)) → seg f L m = seg g M m := by
  induction m with
  | zero => intro _ _ _; rfl
  | succ m ih =>
    intro L M h
    show f L :: seg f (L + 1) m = g M :: seg g (M + 1) m
    rw [show f L = g M from h 0 (by omega), ih (L + 1) (M + 1) (fun i hi => by
      rw [show L + 1 + i = L + (i + 1) by omega, show M + 1 + i = M + (i + 1) by omega]; exact h (i + 1) (by omega))]

/-- A number whose top bit is bit `W - 1`. -/
theorem top_facts {W n : Nat} (hW : 1 ≤ W) (hn : n >>> (W - 1) = 1) :
    n.testBit (W - 1) = true ∧ ∀ j, W ≤ j → n.testBit j = false := by
  constructor
  · have : (n >>> (W - 1)).testBit 0 = n.testBit (W - 1) := by simp
    rw [← this, hn]; rfl
  · intro j hj
    obtain ⟨k, rfl⟩ : ∃ k, j = (W - 1) + (k + 1) := ⟨j - (W - 1) - 1, by omega⟩
    have : (n >>> (W - 1)).testBit (k + 1) = n.testBit (W - 1 + (k + 1)) := by simp [Nat.testBit_shiftRight]
    rw [← this, hn]
    simp [Nat.testBit_succ]

theorem load_seg {W n : Nat} (hW : 1 ≤ W) (hn : n >>> (W - 1) = 1) (p1 p2 : Bool) :
    seg (load W n p1 p2).testBit 2 (W + 6) = inp W (dec W n) := by
  obtain ⟨htop, hhi⟩ := top_facts hW hn
  have split : seg (load W n p1 p2).testBit 2 (W + 6) =
      seg (load W n p1 p2).testBit 2 (W - 1) ++ seg (load W n p1 p2).testBit (2 + (W - 1)) 7 := by
    rw [← seg_append]; congr 1; omega
  have hlow : ∀ j, j < W → (42 <<< W).testBit j = false := by
    intro j hj; simp [Nat.testBit_shiftLeft]; omega
  have htake : (dec W n).take (W - 1) = seg n.testBit 0 (W - 1) := by
    have e1 : dec W n = seg n.testBit 0 (W - 1) ++ seg n.testBit (0 + (W - 1)) 1 := by
      rw [← seg_append]; show seg n.testBit 0 W = _; congr 1; omega
    rw [e1]; exact List.take_left' (seg_length _ _ _)
  have hget : (dec W n).getD (W - 1) false = true := by
    have := seg_getD n.testBit W 0 (W - 1) (by omega)
    rw [Nat.zero_add] at this
    show (seg n.testBit 0 W).getD (W - 1) false = true
    rw [this, htop]
  have a1 : seg (load W n p1 p2).testBit 2 (W - 1) = seg n.testBit 0 (W - 1) := by
    have g : ∀ (m L : Nat), L + m ≤ W → seg (load W n p1 p2).testBit (L + 2) m = seg n.testBit L m := by
      intro m
      induction m with
      | zero => intro _ _; rfl
      | succ m ih =>
        intro L hLm
        show (load W n p1 p2).testBit (L + 2) :: seg (load W n p1 p2).testBit (L + 2 + 1) m = n.testBit L :: seg n.testBit (L + 1) m
        rw [load_bit, hlow L (by omega), Bool.or_false, show L + 2 + 1 = L + 1 + 2 by omega, ih (L + 1) (by omega)]
    exact g (W - 1) 0 (by omega)
  have a2 : seg (load W n p1 p2).testBit (2 + (W - 1)) 7 = alt true 7 := by
    have bit : ∀ k, k < 7 → (load W n p1 p2).testBit (2 + (W - 1) + k) = (alt true 7).getD k false := by
      intro k hk
      rw [show 2 + (W - 1) + k = (W - 1 + k) + 2 by omega, load_bit]
      have hs : ∀ m : Nat, (42 <<< W).testBit (W + m) = (42 : Nat).testBit m := by
        intro m; simp [Nat.testBit_shiftLeft]
      match k, hk with
      | 0, _ => rw [show W - 1 + 0 = W - 1 by omega, htop]; rfl
      | 1, _ => rw [show W - 1 + 1 = W + 0 by omega, hhi _ (by omega), hs]; rfl
      | 2, _ => rw [show W - 1 + 2 = W + 1 by omega, hhi _ (by omega), hs]; rfl
      | 3, _ => rw [show W - 1 + 3 = W + 2 by omega, hhi _ (by omega), hs]; rfl
      | 4, _ => rw [show W - 1 + 4 = W + 3 by omega, hhi _ (by omega), hs]; rfl
      | 5, _ => rw [show W - 1 + 5 = W + 4 by omega, hhi _ (by omega), hs]; rfl
      | 6, _ => rw [show W - 1 + 6 = W + 5 by omega, hhi _ (by omega), hs]; rfl
    have eq : ∀ (m : Nat) (l : List Bool) (L : Nat), l.length = m →
        (∀ k, k < m → (load W n p1 p2).testBit (L + k) = l.getD k false) → seg (load W n p1 p2).testBit L m = l := by
      intro m
      induction m with
      | zero => intro l _ hl _; cases l with
        | nil => rfl
        | cons _ _ => simp at hl
      | succ m ih =>
        intro l L hl h
        cases l with
        | nil => simp at hl
        | cons b r =>
          show (load W n p1 p2).testBit L :: seg (load W n p1 p2).testBit (L + 1) m = b :: r
          have h0 := h 0 (by omega)
          simp only [Nat.add_zero, List.getD_cons_zero] at h0
          rw [h0, ih r (L + 1) (by simpa using hl) (fun k hk => by
            have := h (k + 1) (by omega)
            rw [show L + (k + 1) = L + 1 + k by omega] at this
            simpa using this)]
    exact eq 7 _ _ rfl bit
  rw [split, a1, a2]
  show _ = (dec W n).take (W - 1) ++ alt ((dec W n).getD (W - 1) false) 7
  rw [htake, hget]

/-- The sweep is `back` on the loaded window. -/
theorem image_back {W n : Nat} (hW : 1 ≤ W) (hn : n >>> (W - 1) = 1) (p1 p2 : Bool) :
    seg (image W n p1 p2).testBit 2 (W + 6) = back p1 p2 (inp W (dec W n)) := by
  have := run_back (W + 6) 0 (load W n p1 p2)
  rw [show (0 : Nat) + 2 = 2 from rfl, show (0 : Nat) + 1 = 1 from rfl, load_low1, load_low0, load_seg hW hn] at this
  exact this

theorem next_fast {W n : Nat} (hW : 1 ≤ W) (hn : n >>> (W - 1) = 1) (p1 p2 : Bool) :
    next W (dec W n) p1 p2 = dec W (nxt W n p1 p2) := by
  show ((back p1 p2 (inp W (dec W n))).drop 3).take W = _
  rw [← image_back hW hn]
  have e1 : seg (image W n p1 p2).testBit 2 (W + 6) =
      seg (image W n p1 p2).testBit 2 3 ++ seg (image W n p1 p2).testBit (2 + 3) (W + 3) := by
    rw [← seg_append]; congr 1; omega
  have e2 : seg (image W n p1 p2).testBit (2 + 3) (W + 3) =
      seg (image W n p1 p2).testBit (2 + 3) W ++ seg (image W n p1 p2).testBit (2 + 3 + W) 3 := seg_append _ _ _ _
  rw [e1, List.drop_left' (seg_length _ _ _), e2, List.take_left' (seg_length _ _ _)]
  refine seg_ext W _ _ (fun i hi => ?_)
  show (image W n p1 p2).testBit (2 + 3 + i) = ((image W n p1 p2 >>> 5) &&& (2 ^ W - 1)).testBit (0 + i)
  rw [Nat.testBit_and, Nat.testBit_shiftRight, Nat.testBit_two_pow_sub_one]
  simp only [Nat.zero_add]
  rw [show 5 + i = 2 + 3 + i by omega]
  simp [hi]

/-- **A closed set from numbers.** -/
theorem closed_fast {W : Nat} (hW : 1 ≤ W) (S : List Nat) (h : ∀ n, n ∈ S → Fast W S n) : Closed W (S.map (dec W)) := by
  have bits : ∀ n, n ∈ S → ∀ (p1 p2 : Bool) (k : Nat), k < 4 →
      (back p1 p2 (inp W (dec W n))).getD (W + 2 + k) false = (5 : Nat).testBit k := by
    intro n hn p1 p2 k hk
    have ok := ((h n hn).2 p1 p2).1
    rw [← image_back hW (h n hn).1, seg_getD _ _ _ _ (by omega), ← ok, Nat.testBit_shiftRight]
    rw [show 2 + (W + 2 + k) = W + 4 + k by omega]
  have rain : ∀ n, n ∈ S → ∀ (k : Nat), k < 2 → (inp W (dec W n)).getD (W + 4 + k) false = (42 : Nat).testBit (4 + k) := by
    intro n hn k hk
    rw [← load_seg hW (h n hn).1 false false, seg_getD _ _ _ _ (by omega), show 2 + (W + 4 + k) = (W + (4 + k)) + 2 by omega, load_bit]
    have hi := (top_facts hW (h n hn).1).2 (W + (4 + k)) (by omega)
    rw [hi]
    simp [Nat.testBit_shiftLeft]
  have sub : ∀ w, w ∈ S.map (dec W) → ∃ n, n ∈ S ∧ w = dec W n := by
    intro w hw
    obtain ⟨n, hn, rfl⟩ := List.mem_map.1 hw
    exact ⟨n, hn, rfl⟩
  refine ⟨hW, ?_, ?_, ?_, ?_, ?_⟩
  · intro w hw p1 p2
    obtain ⟨n, hn, rfl⟩ := sub w hw
    rw [next_fast hW (h n hn).1]
    exact List.mem_map.2 ⟨_, ((h n hn).2 p1 p2).2, rfl⟩
  · intro w hw p1 p2
    obtain ⟨n, hn, rfl⟩ := sub w hw
    have b0 := bits n hn p1 p2 0 (by omega)
    have b1 := bits n hn p1 p2 1 (by omega)
    rw [show W + 2 + 0 = W + 2 by omega] at b0
    rw [show W + 2 + 1 = W + 3 by omega] at b1
    rw [b0, b1]; decide
  · intro w hw p1 p2
    obtain ⟨n, hn, rfl⟩ := sub w hw
    have b1 := bits n hn p1 p2 1 (by omega)
    have b2 := bits n hn p1 p2 2 (by omega)
    rw [show W + 2 + 1 = W + 3 by omega] at b1
    rw [show W + 2 + 2 = W + 4 by omega] at b2
    rw [b1, b2]; decide
  · intro w hw p1 p2
    obtain ⟨n, hn, rfl⟩ := sub w hw
    have b2 := bits n hn p1 p2 2 (by omega)
    have r0 := rain n hn 0 (by omega)
    rw [show W + 2 + 2 = W + 4 by omega] at b2
    rw [show W + 4 + 0 = W + 4 by omega] at r0
    rw [b2, r0]; decide
  · intro w hw p1 p2
    obtain ⟨n, hn, rfl⟩ := sub w hw
    have b3 := bits n hn p1 p2 3 (by omega)
    have r1 := rain n hn 1 (by omega)
    rw [show W + 2 + 3 = W + 5 by omega] at b3
    rw [show W + 4 + 1 = W + 5 by omega] at r1
    rw [b3, r1]; decide

/-- The cells of a word above `k`, from the number. -/
theorem dec_drop (W k n : Nat) (hk : k ≤ W) : (dec W n).drop k = dec (W - k) (n >>> k) := by
  have e : dec W n = seg n.testBit 0 k ++ seg n.testBit (0 + k) (W - k) := by
    rw [← seg_append]; show seg n.testBit 0 W = _; congr 1; omega
  rw [e, List.drop_left' (seg_length _ _ _)]
  refine seg_ext (W - k) _ _ (fun i _ => ?_)
  simp [Nat.testBit_shiftRight]

theorem wordA_dec : wordA = dec 11 1596 := by decide
theorem wordB_dec : wordB = dec 11 1594 := by decide

/-- The word above cell `L + k` of a window, read on the row. -/
theorem seg_drop (x : Row) (L W k : Nat) (hk : k ≤ W) : (seg x L W).drop k = seg x (L + k) (W - k) := by
  have e : seg x L W = seg x L k ++ seg x (L + k) (W - k) := by
    rw [← seg_append]; congr 1; omega
  rw [e, List.drop_left' (seg_length x k L)]

theorem Fast.mono {W n : Nat} {T U : List Nat} (h : ∀ m, m ∈ T → m ∈ U) (f : Fast W T n) : Fast W U n :=
  ⟨f.1, fun p1 p2 => ⟨(f.2 p1 p2).1, h _ (f.2 p1 p2).2⟩⟩

/-- A word of `W` cells from a number whose top letter is `A` or `B` ends in the wall's equal pair. -/
theorem wall_of_letter {W n : Nat} (hW : 11 ≤ W) (h : n >>> (W - 11) = 1596 ∨ n >>> (W - 11) = 1594) :
    (dec W n).getD (W - 2) false = (dec W n).getD (W - 1) false := by
  have g1 := seg_getD n.testBit W 0 (W - 2) (by omega)
  have g2 := seg_getD n.testBit W 0 (W - 1) (by omega)
  rw [Nat.zero_add] at g1 g2
  show (seg n.testBit 0 W).getD (W - 2) false = (seg n.testBit 0 W).getD (W - 1) false
  rw [g1, g2]
  have e1 : n.testBit (W - 2) = (n >>> (W - 11)).testBit 9 := by
    rw [Nat.testBit_shiftRight, show W - 11 + 9 = W - 2 by omega]
  have e2 : n.testBit (W - 1) = (n >>> (W - 11)).testBit 10 := by
    rw [Nat.testBit_shiftRight, show W - 11 + 10 = W - 1 by omega]
  rw [e1, e2]
  rcases h with h | h <;> rw [h] <;> decide

/-- A lock: window numbers in `k` phases, each phase going to the next for every pair of lower cells. -/
structure Lock (W k : Nat) (Ph : List (List Nat)) (All : List Nat) : Prop where
  width : 11 ≤ W
  period : 0 < k
  cycle : ∀ r, r < k → ∀ n, n ∈ Ph.getD r [] → Fast W (Ph.getD ((r + 1) % k) []) n
  sub : ∀ r, r < k → ∀ n, n ∈ Ph.getD r [] → n ∈ All
  cover : ∀ n, n ∈ All → ∃ r, r < k ∧ n ∈ Ph.getD r []

namespace Lock
variable {W k : Nat} {Ph : List (List Nat)} {All : List Nat}

theorem closed (H : Lock W k Ph All) : Closed W (All.map (dec W)) :=
  closed_fast (by have := H.width; omega) All (fun n hn => by
    obtain ⟨r, hr, hm⟩ := H.cover n hn
    exact Fast.mono (H.sub _ (Nat.mod_lt _ H.period)) (H.cycle r hr n hm))

theorem phase (H : Lock W k Ph All) {x : Row} {L : Nat} (h : Held W (All.map (dec W)) x L) :
    ∃ r, r < k ∧ seg x L W ∈ (Ph.getD r []).map (dec W) := by
  obtain ⟨n, hn, e⟩ := List.mem_map.1 h.1
  obtain ⟨r, hr, hm⟩ := H.cover n hn
  exact ⟨r, hr, List.mem_map.2 ⟨n, hm, e⟩⟩

/-- **The phases follow each other for ever,** whatever lies below the window. -/
theorem forever (H : Lock W k Ph All) {x : Row} {L r : Nat} (hL : 2 ≤ L) (h : Held W (All.map (dec W)) x L)
    (hp : seg x L W ∈ (Ph.getD (r % k) []).map (dec W)) :
    ∀ n z, iter z n = x → seg z (L + 3 * n) W ∈ (Ph.getD ((r + n) % k) []).map (dec W) := by
  have hW : 1 ≤ W := by have := H.width; omega
  intro n
  induction n with
  | zero =>
    intro z hz
    have e : z = x := hz
    subst e
    exact hp
  | succ n ih =>
    intro z hz
    have e : iter (step z) n = x := by
      have := iter_add z 1 n
      rw [Nat.add_comm 1 n] at this
      rw [← hz, this]; rfl
    obtain ⟨m, hm, em⟩ := List.mem_map.1 (ih (step z) e)
    have hy := held_forever H.closed hL h n (step z) e
    have q := next_seg H.closed (L := L + 3 * n) (by omega) rfl hy
    rw [← em, next_fast hW (H.cycle _ (Nat.mod_lt _ H.period) m hm).1] at q
    rw [show L + 3 * (n + 1) = L + 3 * n + 3 by omega, q]
    refine List.mem_map.2 ⟨_, ?_, rfl⟩
    have := ((H.cycle _ (Nat.mod_lt _ H.period) m hm).2 (z (L + 3 * n - 1)) (z (L + 3 * n - 2))).2
    rw [Nat.mod_add_mod] at this
    exact this

/-- **The letters run through the phases for ever.** -/
theorem letters (H : Lock W k Ph All) (lc : Nat → List Bool)
    (hl : ∀ r, r < k → ∀ n, n ∈ Ph.getD r [] → dec 11 (n >>> (W - 11)) = lc r)
    {x : Row} {L : Nat} (hL : 2 ≤ L) (h : Held W (All.map (dec W)) x L) :
    ∃ r, r < k ∧ ∀ n z, iter z n = x → seg z (L + 3 * n + (W - 11)) 11 = lc ((r + n) % k) := by
  have hW := H.width
  obtain ⟨r, hr, hp⟩ := H.phase h
  refine ⟨r, hr, fun n z hz => ?_⟩
  have hp' : seg x L W ∈ (Ph.getD (r % k) []).map (dec W) := by rwa [Nat.mod_eq_of_lt hr]
  obtain ⟨m, hm, em⟩ := List.mem_map.1 (H.forever hL h hp' n z hz)
  have d1 := seg_drop z (L + 3 * n) W (W - 11) (by omega)
  rw [show W - (W - 11) = 11 by omega, ← em, dec_drop W (W - 11) m (by omega), show W - (W - 11) = 11 by omega] at d1
  rw [← d1]
  exact hl _ (Nat.mod_lt _ H.period) m hm

end Lock

/-- A row with the window `n` on a black edge, one white cell below it, and rain above it. -/
def anchor (W n j : Nat) : Bool :=
  if j = 0 then true else if j = 1 then false else if j < W + 2 then n.testBit (j - 2) else decide ((j - W) % 2 = 1)

/-- **Every window of a set occurs on an anchored row.** -/
theorem anchor_held {W n : Nat} {S : List (List Bool)} (hW : 1 ≤ W) (hn : n >>> (W - 1) = 1) (hm : dec W n ∈ S) :
    anchor W n 0 = true ∧ Held W S (anchor W n) 2 := by
  have htop := (top_facts hW hn).1
  have hs : seg (anchor W n) 2 W = dec W n := by
    refine seg_ext W 2 0 (fun i hi => ?_)
    simp [anchor, show ¬2 + i = 1 by omega, show 2 + i < W + 2 by omega]
  refine ⟨rfl, by rw [hs]; exact hm, fun j hj => ?_⟩
  by_cases c : j = W + 1
  · subst c
    have a1 : anchor W n (W + 1) = true := by
      simp only [anchor, show ¬W + 1 = 0 by omega, show ¬W + 1 = 1 by omega, show W + 1 < W + 2 by omega, ite_false, ite_true]
      rw [show W + 1 - 2 = W - 1 by omega]; exact htop
    have a2 : anchor W n (W + 1 + 1) = false := by
      simp only [anchor, show ¬W + 1 + 1 = 0 by omega, show ¬W + 1 + 1 = 1 by omega, show ¬W + 1 + 1 < W + 2 by omega, ite_false]
      rw [show W + 1 + 1 - W = 2 by omega]; rfl
    rw [a1, a2]; rfl
  · have q : W + 2 ≤ j := by omega
    simp only [anchor, show ¬j = 0 by omega, show ¬j + 1 = 0 by omega, show ¬j = 1 by omega, show ¬j + 1 = 1 by omega,
      show ¬j < W + 2 by omega, show ¬j + 1 < W + 2 by omega, ite_false]
    by_cases a : (j - W) % 2 = 1
    · have b : ¬(j + 1 - W) % 2 = 1 := by omega
      simp [a, b]
    · have b : (j + 1 - W) % 2 = 1 := by omega
      simp [a, b]

/-! ## Forward ticks on numbers -/

/-- One tick on a number: exactly the edge map. -/
def fw (y : Nat) : Nat := y ^^^ ((y <<< 1) ||| (y <<< 2))

def fwN : Nat → Nat → Nat
  | 0, y => y
  | k + 1, y => fw (fwN k y)

theorem fw_bit (y : Nat) : (fw y).testBit = step y.testBit := by
  funext j
  match j with
  | 0 => simp [fw, T]
  | 1 => simp [fw, T, Nat.testBit_xor, Nat.testBit_or, Nat.testBit_shiftLeft]
  | j + 2 => simp [fw, T, Nat.testBit_xor, Nat.testBit_or, Nat.testBit_shiftLeft]

theorem iter_fw (y k : Nat) : iter y.testBit k = (fwN k y).testBit := by
  induction k with
  | zero => rfl
  | succ k ih =>
    show step (iter y.testBit k) = _
    rw [ih]; exact (fw_bit _).symm

/-- Two rows that agree below `N` keep agreeing below `N`. -/
theorem iter_low {x y : Row} {N : Nat} (h : ∀ j, j < N → x j = y j) (k : Nat) : ∀ j, j < N → iter x k j = iter y k j := by
  induction k with
  | zero => exact h
  | succ k ih =>
    intro j hj
    show step (iter x k) j = step (iter y k) j
    match j, hj with
    | 0, hj => exact ih 0 hj
    | 1, hj =>
      show xor _ _ = xor _ _
      rw [ih 1 hj, ih 0 (by omega)]
    | j + 2, hj =>
      show xor _ (_ || _) = xor _ (_ || _)
      rw [ih (j + 2) hj, ih (j + 1) (by omega), ih j (by omega)]

/-- A rain tail above `D` is a rain tail above `D + 2 k` after `k` ticks. -/
theorem iter_tail {x : Row} {D : Nat} (h : ∀ j, D ≤ j → x (j + 1) = !x j) (k : Nat) :
    ∀ j, D + 2 * k ≤ j → iter x k (j + 1) = !iter x k j := by
  induction k with
  | zero => exact h
  | succ k ih =>
    intro j hj
    exact step_rain_tail ih j (by omega)

end WindowClosed

open WindowClosed

/-! ## The letters `A`, `B`: four windows of 45 cells -/

namespace LockAB

/-- The phases, as window numbers, low cell first. -/
def Ph : List (List Nat) := [[27432157596204, 27432157596202],
  [27391699171004, 27391699171002]]

/-- All the windows, as numbers. -/
def All : List Nat := Ph.flatten

/-- All the windows. -/
def Win : List (List Bool) := All.map (dec 45)

/-- The letter of each phase. -/
def lc (r : Nat) : List Bool := if r = 1 then wordB else wordA

/-- **The lock.** -/
theorem lock : Lock 45 2 Ph All :=
  ⟨by decide, by decide, by decide +kernel, by decide +kernel, by decide +kernel⟩

theorem closed : Closed 45 Win := lock.closed

/-- **For ever.** Every row `n` ticks before a held row is held `3 n` cells higher, whatever lies below the window. -/
theorem held {x : Row} {L : Nat} (hL : 2 ≤ L) (h : Held 45 Win x L) :
    ∀ n z, iter z n = x → Held 45 Win z (L + 3 * n) := held_forever closed hL h

theorem chk_letters : ∀ r, r < 2 → ∀ n, n ∈ Ph.getD r [] → dec 11 (n >>> 34) = lc r := by decide +kernel

/-- **The letters.** There is a phase `r` such that the wall of every row `n` ticks before the row reads the letter of phase `r + n`. -/
theorem letters {x : Row} {L : Nat} (hL : 2 ≤ L) (h : Held 45 Win x L) :
    ∃ r, r < 2 ∧ ∀ n z, iter z n = x → seg z (L + 3 * n + 34) 11 = if (r + n) % 2 = 1 then wordB else wordA := by
  obtain ⟨r, hr, f⟩ := lock.letters lc chk_letters hL h
  exact ⟨r, hr, fun n z hz => by simpa [lc] using f n z hz⟩

theorem chk_wall : ∀ n, n ∈ All → n >>> 34 = 1596 ∨ n >>> 34 = 1594 := by decide +kernel

/-- **A row in the lock is not periodic.** -/
theorem not_periodic {x : Row} {L P : Nat} (hL : 2 ≤ L) (h : Held 45 Win x L) (hP : 0 < P) : iter x P ≠ x := by
  refine held_not_periodic closed (by decide) (fun w hw => ?_) hL h hP
  obtain ⟨n, hn, rfl⟩ := List.mem_map.1 hw
  exact wall_of_letter (by decide) (chk_wall n hn)

/-- **An anchored row in the lock.** -/
theorem witness : anchor 45 27432157596204 0 = true ∧ Held 45 Win (anchor 45 27432157596204) 2 :=
  anchor_held (by decide) (by decide +kernel) (by decide +kernel)

/-- **The shield of the lock.** Each window starts with a reset word. -/
theorem floor : ∀ n, n ∈ All → ∃ b u v, (dec 45 n).take 10 = Reset.F b u v := by decide +kernel

end LockAB

/-! ## The letters `A`, `A`, `B`: six windows of 136 cells -/

namespace LockAAB

/-- The phases, as window numbers, low cell first. -/
def Ph : List (List Nat) := [[67918664933144423441542139865466147588794, 67918664933144423441542139865466147588796],
  [67908875212190969569599336687020282132138, 67908875212190969569599336687020282132140],
  [67819754217029842684664044888796937824810, 67819754217029842684664044888796937824812]]

/-- All the windows, as numbers. -/
def All : List Nat := Ph.flatten

/-- All the windows. -/
def Win : List (List Bool) := All.map (dec 136)

/-- The letter of each phase. -/
def lc (r : Nat) : List Bool := if r = 2 then wordB else wordA

/-- **The lock.** -/
theorem lock : Lock 136 3 Ph All :=
  ⟨by decide, by decide, by decide +kernel, by decide +kernel, by decide +kernel⟩

theorem closed : Closed 136 Win := lock.closed

/-- **For ever.** Every row `n` ticks before a held row is held `3 n` cells higher, whatever lies below the window. -/
theorem held {x : Row} {L : Nat} (hL : 2 ≤ L) (h : Held 136 Win x L) :
    ∀ n z, iter z n = x → Held 136 Win z (L + 3 * n) := held_forever closed hL h

theorem chk_letters : ∀ r, r < 3 → ∀ n, n ∈ Ph.getD r [] → dec 11 (n >>> 125) = lc r := by decide +kernel

/-- **The letters.** There is a phase `r` such that the wall of every row `n` ticks before the row reads the letter of phase `r + n`. -/
theorem letters {x : Row} {L : Nat} (hL : 2 ≤ L) (h : Held 136 Win x L) :
    ∃ r, r < 3 ∧ ∀ n z, iter z n = x → seg z (L + 3 * n + 125) 11 = if (r + n) % 3 = 2 then wordB else wordA := by
  obtain ⟨r, hr, f⟩ := lock.letters lc chk_letters hL h
  exact ⟨r, hr, fun n z hz => by simpa [lc] using f n z hz⟩

theorem chk_wall : ∀ n, n ∈ All → n >>> 125 = 1596 ∨ n >>> 125 = 1594 := by decide +kernel

/-- **A row in the lock is not periodic.** -/
theorem not_periodic {x : Row} {L P : Nat} (hL : 2 ≤ L) (h : Held 136 Win x L) (hP : 0 < P) : iter x P ≠ x := by
  refine held_not_periodic closed (by decide) (fun w hw => ?_) hL h hP
  obtain ⟨n, hn, rfl⟩ := List.mem_map.1 hw
  exact wall_of_letter (by decide) (chk_wall n hn)

/-- **An anchored row in the lock.** -/
theorem witness : anchor 136 67918664933144423441542139865466147588794 0 = true ∧ Held 136 Win (anchor 136 67918664933144423441542139865466147588794) 2 :=
  anchor_held (by decide) (by decide +kernel) (by decide +kernel)

/-- **The shield of the lock.** Each window starts with a reset word. -/
theorem floor : ∀ n, n ∈ All → ∃ b u v, (dec 136 n).take 10 = Reset.F b u v := by decide +kernel

end LockAAB

/-! ## A third lock, with no fixed shield: forty windows of 175 cells -/

namespace LockThird

/-- The phases, as window numbers, low cell first. -/
def Ph : List (List Nat) := [[37284303768780549450216512176333106322617512176932327, 37284303768780549450216512176333106322617512176932363, 37284303768780549450216512176333106322617512176932362, 37284303768780549450216512176333106322617512176932305, 37284303768780549450216512176333106322617512176932360],
  [37338680436793518946018258025312893609782730154505572, 37338680436793518946018258025312893609782730154505555, 37338680436793518946018258025312893609782730154505790, 37338680436793518946018258025312893609782730154505573, 37338680436793518946018258025312893609782730154505574, 37338680436793518946018258025312893609782730154505791],
  [37333299180212662931848950068353642697240989240174933, 37333299180212662931848950068353642697240989240174934, 37333299180212662931848950068353642697240989240177210, 37333299180212662931848950068353642697240989240174913, 37333299180212662931848950068353642697240989240174947, 37333299180212662931848950068353642697240989240174932, 37333299180212662931848950068353642697240989240177212],
  [37284303528463190167104685405439550272830198693161685, 37284303528463190167104685405439550272830198693161686, 37284303528463190167104685405439550272830198693161687, 37284303528463190167104685405439550272830198693161688, 37284303528463190167104685405439550272830198693163452, 37284303528463190167104685405439550272830198693161699, 37284303528463190167104685405439550272830198693161684, 37284303528463190167104685405439550272830198693163450],
  [37338680284242987720315585462861809216178240387134149, 37338680284242987720315585462861809216178240387134150, 37338680284242987720315585462861809216178240387134120, 37338680284242987720315585462861809216178240387133964, 37338680284242987720315585462861809216178240387133962, 37338680284242987720315585462861809216178240387134131, 37338680284242987720315585462861809216178240387134148],
  [37333299375615735401535943766818242528686808079618503, 37333299375615735401535943766818242528686808079618472, 37333299375615735401535943766818242528686808079618475, 37333299375615735401535943766818242528686808079618474, 37333299375615735401535943766818242528686808079618494, 37333299375615735401535943766818242528686808079618481, 37333299375615735401535943766818242528686808079618496]]

/-- All the windows, as numbers. -/
def All : List Nat := Ph.flatten

/-- All the windows. -/
def Win : List (List Bool) := All.map (dec 175)

/-- The letter of each phase. -/
def lc (r : Nat) : List Bool := if r % 3 = 0 then wordB else wordA

/-- **The lock.** -/
theorem lock : Lock 175 6 Ph All :=
  ⟨by decide, by decide, by decide +kernel, by decide +kernel, by decide +kernel⟩

theorem closed : Closed 175 Win := lock.closed

/-- **For ever.** Every row `n` ticks before a held row is held `3 n` cells higher, whatever lies below the window. -/
theorem held {x : Row} {L : Nat} (hL : 2 ≤ L) (h : Held 175 Win x L) :
    ∀ n z, iter z n = x → Held 175 Win z (L + 3 * n) := held_forever closed hL h

theorem chk_letters : ∀ r, r < 6 → ∀ n, n ∈ Ph.getD r [] → dec 11 (n >>> 164) = lc r := by decide +kernel

/-- **The letters.** There is a phase `r` such that the wall of every row `n` ticks before the row reads the letter of phase `r + n`. -/
theorem letters {x : Row} {L : Nat} (hL : 2 ≤ L) (h : Held 175 Win x L) :
    ∃ r, r < 6 ∧ ∀ n z, iter z n = x → seg z (L + 3 * n + 164) 11 = if (r + n) % 6 % 3 = 0 then wordB else wordA := by
  obtain ⟨r, hr, f⟩ := lock.letters lc chk_letters hL h
  exact ⟨r, hr, fun n z hz => by simpa [lc] using f n z hz⟩

theorem chk_wall : ∀ n, n ∈ All → n >>> 164 = 1596 ∨ n >>> 164 = 1594 := by decide +kernel

/-- **A row in the lock is not periodic.** -/
theorem not_periodic {x : Row} {L P : Nat} (hL : 2 ≤ L) (h : Held 175 Win x L) (hP : 0 < P) : iter x P ≠ x := by
  refine held_not_periodic closed (by decide) (fun w hw => ?_) hL h hP
  obtain ⟨n, hn, rfl⟩ := List.mem_map.1 hw
  exact wall_of_letter (by decide) (chk_wall n hn)

/-- **An anchored row in the lock.** -/
theorem witness : anchor 175 37284303768780549450216512176333106322617512176932327 0 = true ∧ Held 175 Win (anchor 175 37284303768780549450216512176333106322617512176932327) 2 :=
  anchor_held (by decide) (by decide +kernel) (by decide +kernel)

/-- **No fixed shield.** Below the wall's own word, no depth carries a reset word in all forty windows. -/
theorem no_floor : ∀ d, d < 164 → ¬ ∀ n, n ∈ All → ∃ b u v, ((dec 175 n).drop d).take 10 = Reset.F b u v := by decide +kernel

end LockThird

namespace Cloud

/-- A search tree of numbers with ranks. -/
inductive Tree where
  | e
  | n (l : Tree) (v r : Nat) (t : Tree)

/-- The rank of a number, 0 if it is not there. -/
def Tree.find : Tree → Nat → Nat
  | .e, _ => 0
  | .n l v r t, c => if c < v then l.find c else if v < c then t.find c else r

/-- The numbers. -/
def Tree.toList : Tree → List Nat
  | .e => []
  | .n l v _ t => l.toList ++ v :: t.toList

theorem Tree.mem_of_find : ∀ (t : Tree) (c : Nat), t.find c ≠ 0 → c ∈ t.toList := by
  intro t
  induction t with
  | e => intro c h; exact absurd rfl h
  | n l v r t ihl iht =>
    intro c h
    simp only [Tree.find] at h
    simp only [Tree.toList, List.mem_append, List.mem_cons]
    by_cases c1 : c < v
    · rw [ite_eq_left c1] at h; exact Or.inl (ihl c h)
    · rw [ite_eq_right c1] at h
      by_cases c2 : v < c
      · rw [ite_eq_left c2] at h; exact Or.inr (Or.inr (iht c h))
      · exact Or.inr (Or.inl (by omega))

/-- The windows of the cloud as numbers, each with the longest alternating run that starts at it. -/
def tree : Tree := (.n (.n (.n (.n (.n (.n (.n (.n (.n (.n .e 27392014413220 2 .e) 27392014413221 2 (.n .e 27392014413222 2 .e)) 27392014413331 2 (.n (.n .e 27392014740647 2 .e) 27392014740680 2 .e)) 27392014740682 2 (.n (.n (.n .e 27392014740684 2 .e) 27392014741777 2 .e) 27392019216104 4 (.n (.n .e 27392019216106 4 .e) 27392019216107 4 .e))) 27392019216108 10 (.n (.n (.n (.n .e 27392019216113 4 .e) 27392019216134 12 .e) 27392019216135 12 (.n (.n .e 27392019300570 4 .e) 27392019300571 4 .e)) 27392019300572 4 (.n (.n (.n .e 27392019300573 4 .e) 27392019300574 4 .e) 27392019300576 4 (.n (.n .e 27392019300577 4 .e) 27392019310226 4 .e)))) 27392019310227 4 (.n (.n (.n (.n (.n .e 27392019310372 4 .e) 27392019310373 4 (.n .e 27392019310516 4 .e)) 27392019310517 4 (.n (.n .e 27392019310520 4 .e) 27392019310531 4 .e)) 27392019318857 4 (.n (.n (.n .e 27392019375363 12 .e) 27392019375514 12 .e) 27392019375516 12 (.n (.n .e 27392019375593 12 .e) 27392019375603 12 .e))) 27392019375620 12 (.n (.n (.n (.n .e 27392019375649 12 .e) 27392019375662 12 .e) 27392019375663 12 (.n (.n .e 27392019375664 12 .e) 27392019384564 4 .e)) 27392019384567 4 (.n (.n (.n .e 27392019384568 4 .e) 27392019599726 2 .e) 27392019599727 2 (.n (.n .e 27392019600616 2 .e) 27392019600619 2 .e))))) 27392019600620 2 (.n (.n (.n (.n (.n (.n .e 27392019601670 2 .e) 27392019601671 2 (.n .e 27392019601757 2 .e)) 27392019601758 2 (.n (.n .e 27392019601760 2 .e) 27392179966786 2 .e)) 27392179966787 2 (.n (.n (.n .e 27392179966795 2 .e) 27392179966796 2 .e) 27392179966804 2 (.n (.n .e 27392179966809 2 .e) 27392179966818 2 .e))) 27392179966819 2 (.n (.n (.n (.n .e 27392180106449 2 .e) 27392180106450 2 .e) 27392180106468 2 (.n (.n .e 27392180106471 2 .e) 27392180107528 2 .e)) 27392180107529 2 (.n (.n (.n .e 27392180107530 2 .e) 27392180107531 2 .e) 27392180107532 2 (.n (.n .e 27392180107639 2 .e) 27392180109365 2 .e)))) 27392180109366 2 (.n (.n (.n (.n (.n .e 27392180109368 2 .e) 27392180113587 2 (.n .e 27392180113604 2 .e)) 27392180113938 2 (.n (.n .e 27392180113939 2 .e) 27392180114158 2 .e)) 27392180114159 2 (.n (.n (.n .e 27392180114160 2 .e) 27392180115264 2 .e) 27392180115281 2 (.n (.n .e 27392180115338 2 .e) 27392180115339 2 .e))) 27392180115340 2 (.n (.n (.n (.n .e 27392180115518 2 .e) 27392180259273 2 .e) 27392180260126 2 (.n (.n .e 27392180260127 2 .e) 27392180283429 2 .e)) 27392180283430 2 (.n (.n (.n .e 27392180283917 2 .e) 27392180283918 2 .e) 27392180283919 2 (.n (.n .e 27392180284036 2 .e) 27392180284052 2 .e)))))) 27392180284057 2 (.n (.n (.n (.n (.n (.n (.n .e 27392180284089 2 .e) 27392180284090 2 (.n .e 27392180284091 2 .e)) 27392180284092 2 (.n (.n .e 27392180284097 2 .e) 27392180284098 2 .e)) 27392180284099 2 (.n (.n (.n .e 27392180284122 2 .e) 27392180284124 2 .e) 27392180284129 2 (.n (.n .e 27392180284158 2 .e) 27392180284159 2 .e))) 27392180284160 2 (.n (.n (.n (.n .e 27392180284194 2 .e) 27392180284521 2 .e) 27392180284527 2 (.n (.n .e 27392180284528 2 .e) 27392180284530 2 .e)) 27392180285345 2 (.n (.n (.n .e 27392180285363 2 .e) 27392180285373 2 .e) 27392180285374 2 (.n (.n .e 27392180285375 2 .e) 27392180285376 2 .e)))) 27392180285380 2 (.n (.n (.n (.n (.n .e 27392180285381 2 .e) 27392180285382 2 (.n .e 27392180285466 2 .e)) 27392180285879 2 (.n (.n .e 27392180285880 2 .e) 27392180285904 2 .e)) 27392180285908 2 (.n (.n (.n .e 27392180285909 2 .e) 27392180285910 2 .e) 27392180285911 2 (.n (.n .e 27392180285912 2 .e) 27392180285919 2 .e))) 27392180285920 2 (.n (.n (.n (.n .e 27392180285923 2 .e) 27392180553544 2 .e) 27392180553582 2 (.n (.n .e 27392180553583 2 .e) 27392180553584 2 .e)) 27392180553619 2 (.n (.n (.n .e 27392180566993 2 .e) 27392180567050 2 .e) 27392180567051 2 (.n (.n .e 27392180567052 2 .e) 27392180567875 2 .e))))) 27392180567935 2 (.n (.n (.n (.n (.n (.n .e 27392180567936 2 .e) 27392180584168 2 (.n .e 27392180584170 2 .e)) 27392180584172 2 (.n (.n .e 27392180584173 2 .e) 27392180584174 2 .e)) 27392180584176 2 (.n (.n (.n .e 27392180584177 2 .e) 27392180584179 2 .e) 27392180584190 2 (.n (.n .e 27392180584192 2 .e) 27392180584196 2 .e))) 27392180584197 2 (.n (.n (.n (.n .e 27392180584198 2 .e) 27392180584199 2 .e) 27392180645158 2 (.n (.n .e 27392180645159 2 .e) 27392180645448 2 .e)) 27392180645451 2 (.n (.n (.n .e 27392180645452 2 .e) 27392198621033 6 .e) 27392198621042 16 (.n (.n .e 27392198621060 16 .e) 27392198812724 12 .e)))) 27392198812726 12 (.n (.n (.n (.n (.n .e 27392198812727 12 .e) 27392198812728 12 (.n .e 27392198812729 12 .e)) 27392198813092 12 (.n (.n .e 27392198813093 12 .e) 27392198813128 12 .e)) 27392198813129 12 (.n (.n (.n .e 27392198813130 12 .e) 27392198813140 12 .e) 27392198813145 12 (.n (.n .e 27392198813154 10 .e) 27392198813201 16 .e))) 27392198813202 16 (.n (.n (.n (.n .e 27392198830415 16 .e) 27392198830480 16 .e) 27392198830489 16 (.n (.n .e 27392238148304 14 .e) 27392238148308 14 .e)) 27392238148309 14 (.n (.n (.n .e 27392238148310 14 .e) 27392238148311 14 .e) 27392238148312 14 (.n (.n .e 27392238148313 14 .e) 27392238148319 14 .e))))))) 27392238148320 14 (.n (.n (.n (.n (.n (.n (.n (.n .e 27392238148322 6 .e) 27392238148323 14 (.n .e 27392238148365 12 .e)) 27392238148366 12 (.n (.n .e 27392238148367 12 .e) 27392238148605 6 .e)) 27392238148606 14 (.n (.n (.n .e 27392238150074 6 .e) 27392238150075 6 .e) 27392238150076 6 (.n (.n .e 27392238150081 6 .e) 27392297041258 6 .e))) 27392297041259 6 (.n (.n (.n (.n .e 27392297041260 6 .e) 27392297041262 6 .e) 27392297041264 6 (.n (.n .e 27392297041265 6 .e) 27392297041406 6 .e)) 27392297041407 6 (.n (.n (.n .e 27392297105922 8 .e) 27392297106074 8 .e) 27392297106075 8 (.n (.n .e 27392297106076 8 .e) 27392297106209 6 .e)))) 27392297106219 6 (.n (.n (.n (.n (.n .e 27392297106220 6 .e) 27392297106221 6 (.n .e 27392297106222 6 .e)) 27392297106223 6 (.n (.n .e 27392297106224 8 .e) 27392297107085 6 .e)) 27392297107086 6 (.n (.n (.n .e 27392297107258 8 .e) 27392297107259 8 .e) 27392297107260 8 (.n (.n .e 27392297107521 6 .e) 27392297107536 6 .e))) 27392297107543 6 (.n (.n (.n (.n .e 27392297107544 6 .e) 27392297107550 6 .e) 27392297107551 6 (.n (.n .e 27392297107956 8 .e) 27392297107959 8 .e)) 27392297107960 8 (.n (.n (.n .e 27392297107961 8 .e) 27392297163613 4 .e) 27392297163614 4 (.n (.n .e 27392297163616 4 .e) 27392297163646 4 .e))))) 27392297163647 4 (.n (.n (.n (.n (.n (.n .e 27392297163648 4 .e) 27392325853709 4 (.n .e 27392325853883 4 .e)) 27392325853884 4 (.n (.n .e 27392326323616 14 .e) 27392326323624 14 .e)) 27392326323653 14 (.n (.n (.n .e 27392326323654 14 .e) 27392326323742 14 .e) 27392326323743 14 (.n (.n .e 27392326342273 10 .e) 27392326342306 10 .e))) 27392326342307 10 (.n (.n (.n (.n .e 27392326342350 10 .e) 27392326342351 10 .e) 27392326342416 8 (.n (.n .e 27392326342420 8 .e) 27392326342421 8 .e)) 27392326342422 8 (.n (.n (.n .e 27392326342778 14 .e) 27392326342780 14 .e) 27392326343120 14 (.n (.n .e 27392326343126 14 .e) 27392326343127 14 .e)))) 27392326343128 14 (.n (.n (.n (.n (.n .e 27392326667216 8 .e) 27392326667223 8 (.n .e 27392326667277 10 .e)) 27392326667278 10 (.n (.n .e 27392326667905 10 .e) 27392326667939 10 .e)) 27392326667982 10 (.n (.n (.n .e 27392326667983 10 .e) 27392326668048 10 .e) 27392326668052 10 (.n (.n .e 27392326668053 10 .e) 27392326668054 10 .e))) 27392326668055 10 (.n (.n (.n (.n .e 27392326668056 10 .e) 27392328876218 2 .e) 27392328876219 2 (.n (.n .e 27392328876220 2 .e) 27392328876225 2 .e)) 27392328880169 2 (.n (.n (.n .e 27392328880178 2 .e) 27392328880250 2 .e) 27392328880252 2 (.n (.n .e 27392328881193 2 .e) 27392328881202 2 .e)))))) 27392328881203 2 (.n (.n (.n (.n (.n (.n (.n .e 27392328881225 2 .e) 27392328881274 2 (.n .e 27392328881275 2 .e)) 27392328881276 2 (.n (.n .e 27392328882687 2 .e) 27392328884736 2 .e)) 27392328884882 2 (.n (.n (.n .e 27392328884883 2 .e) 27392328884941 2 .e) 27392328884942 2 (.n (.n .e 27392328885008 2 .e) 27392328885014 2 .e))) 27392328885015 2 (.n (.n (.n (.n .e 27392328885016 2 .e) 27392328885151 2 .e) 27428176267290 3 (.n (.n .e 27428176267292 3 .e) 27428176267408 3 .e)) 27428176267414 3 (.n (.n (.n .e 27428176267415 3 .e) 27428176267416 3 .e) 27428176267444 3 (.n (.n .e 27428176267446 3 .e) 27428176267447 3 .e)))) 27428176267448 3 (.n (.n (.n (.n (.n .e 27428176267449 3 .e) 27428176267458 3 (.n .e 27428176267482 3 .e)) 27428176267483 3 (.n (.n .e 27428176267484 3 .e) 27428176267489 3 .e)) 27428176426052 3 (.n (.n (.n .e 27428176427424 3 .e) 27428176427432 3 .e) 27428176427433 3 (.n (.n .e 27428176427434 3 .e) 27428176427435 3 .e))) 27428176427436 3 (.n (.n (.n (.n .e 27428176427437 3 .e) 27428176427438 3 .e) 27428176427439 3 (.n (.n .e 27428176427440 3 .e) 27428176427441 3 .e)) 27428176427442 3 (.n (.n (.n .e 27428176427454 3 .e) 27428176427455 3 .e) 27428176427456 3 (.n (.n .e 27428176427460 3 .e) 27428176427463 3 .e))))) 27428176427508 3 (.n (.n (.n (.n (.n (.n .e 27428176427509 3 .e) 27428176427510 3 (.n .e 27428176427512 3 .e)) 27428176560643 3 (.n (.n .e 27428176560667 3 .e) 27428176560668 3 .e)) 27428176560669 3 (.n (.n (.n .e 27428176560670 3 .e) 27428176560851 3 .e) 27428176560868 3 (.n (.n .e 27428176560869 3 .e) 27428176560870 3 .e))) 27428176560947 3 (.n (.n (.n (.n .e 27428176570383 3 .e) 27428176570685 3 .e) 27428176570686 3 (.n (.n .e 27428176570916 3 .e) 27428176570943 3 .e)) 27428176570984 3 (.n (.n (.n .e 27428176570995 3 .e) 27428176571524 3 .e) 27428176571525 3 (.n (.n .e 27428176571526 3 .e) 27428176571647 3 .e)))) 27428176572276 3 (.n (.n (.n (.n (.n .e 27428176572278 3 .e) 27428176572279 3 (.n .e 27428176572280 3 .e)) 27428176572281 3 (.n (.n .e 27428176572672 3 .e) 27428176572676 3 .e)) 27428176572736 3 (.n (.n (.n .e 27428176572752 3 .e) 27428176572753 3 .e) 27428176572754 3 (.n (.n .e 27428176572758 3 .e) 27428176572759 3 .e))) 27428176572760 3 (.n (.n (.n (.n .e 27428176572767 3 .e) 27428176572768 3 .e) 27428176572775 3 (.n (.n .e 27428176572809 3 .e) 27428176572810 3 .e)) 27428176572811 3 (.n (.n (.n .e 27428176572812 3 .e) 27428176572813 3 .e) 27428176572814 3 (.n (.n .e 27428176572818 3 .e) 27428176572992 3 .e)))))))) 27428176577675 3 (.n (.n (.n (.n (.n (.n (.n (.n (.n .e 27428176577676 3 .e) 27428176578512 3 (.n .e 27428176578521 3 .e)) 27428176578530 3 (.n (.n .e 27428176872865 3 .e) 27428176872878 3 .e)) 27428176872879 3 (.n (.n (.n .e 27428176872880 3 .e) 27428176872986 3 .e) 27428176872988 3 (.n (.n .e 27428176894693 3 .e) 27428176894694 3 .e))) 27428176894728 3 (.n (.n (.n (.n .e 27428176914575 3 .e) 27428176917480 3 .e) 27428176917491 3 (.n (.n .e 27428176921604 3 .e) 27428176921605 3 .e)) 27428176921606 3 (.n (.n (.n .e 27428176922195 3 .e) 27428176922201 3 .e) 27428176922210 3 (.n (.n .e 27428176922212 3 .e) 27428176922213 3 .e)))) 27428176929199 3 (.n (.n (.n (.n (.n .e 27428176929200 3 .e) 27428177114996 17 (.n .e 27428177115010 17 .e)) 27428177115011 17 (.n (.n .e 27428177301877 13 .e) 27428177301878 13 .e)) 27428177301880 13 (.n (.n (.n .e 27428177302455 17 .e) 27428177302491 13 .e) 27428177302523 13 (.n (.n .e 27428177302524 17 .e) 27428177306989 3 .e))) 27428177306990 3 (.n (.n (.n (.n .e 27428177306992 3 .e) 27428177307213 13 .e) 27428177307214 13 (.n (.n .e 27428177307243 3 .e) 27428177307244 13 .e)) 27428177307245 13 (.n (.n (.n .e 27428177307246 13 .e) 27428177307247 13 .e) 27428177307248 13 (.n (.n .e 27428177307553 3 .e) 27428180870387 17 .e))))) 27428180870399 17 (.n (.n (.n (.n (.n (.n .e 27428181024678 3 .e) 27428181024679 3 (.n .e 27428181024712 3 .e)) 27428181024714 3 (.n (.n .e 27428181024715 3 .e) 27428181024716 3 .e)) 27428181319697 15 (.n (.n (.n .e 27428181321984 15 .e) 27428181321989 15 .e) 27428181322048 15 (.n (.n .e 27428181322057 15 .e) 27428181322064 15 .e))) 27428181322068 15 (.n (.n (.n (.n .e 27428181322073 15 .e) 27428181322078 15 .e) 27428181322079 15 (.n (.n .e 27428181322082 15 .e) 27428181322084 15 .e)) 27428181322109 15 (.n (.n (.n .e 27428181322110 15 .e) 27428181322112 15 .e) 27428181322121 13 (.n (.n .e 27428181322127 15 .e) 27428181322130 13 .e)))) 27428181322131 13 (.n (.n (.n (.n (.n .e 27428181324324 7 .e) 27428181324351 7 (.n .e 27431171214163 9 .e)) 27431171214181 11 (.n (.n .e 27431171214182 11 .e) 27431171214183 11 .e)) 27431171214202 9 (.n (.n (.n .e 27431171214204 11 .e) 27431171214209 11 .e) 27431171214216 11 (.n (.n .e 27431171214219 11 .e) 27431171214397 15 .e))) 27431171214398 15 (.n (.n (.n (.n .e 27431171222050 5 .e) 27431171222051 5 .e) 27431171223887 15 (.n (.n .e 27431171223961 15 .e) 27431171232464 15 .e)) 27431171232470 15 (.n (.n (.n .e 27431171232471 15 .e) 27431171232472 15 .e) 27431171232525 15 (.n (.n .e 27431171232526 15 .e) 27431181051625 3 .e)))))) 27431181051634 3 (.n (.n (.n (.n (.n (.n (.n .e 27431181051652 3 .e) 27431181052744 3 (.n .e 27431181052748 3 .e)) 27431181052817 3 (.n (.n .e 27431181052827 3 .e) 27431181052967 3 .e)) 27431181052973 3 (.n (.n (.n .e 27431181052974 3 .e) 27431181053928 3 .e) 27431181053939 3 (.n (.n .e 27431181053956 3 .e) 27431181053957 3 .e))) 27431181053958 3 (.n (.n (.n (.n .e 27431181059830 3 .e) 27431181059831 3 .e) 27431181060929 11 (.n (.n .e 27431181060944 11 .e) 27431181060946 11 .e)) 27431181060947 11 (.n (.n (.n .e 27431181060959 11 .e) 27431181060960 11 .e) 27431181061001 11 (.n (.n .e 27431181061006 11 .e) 27431181061178 3 .e)))) 27431181061179 11 (.n (.n (.n (.n (.n .e 27431181061180 3 .e) 27431181061183 11 (.n .e 27431181066564 9 .e)) 27431181066655 11 (.n (.n .e 27431181097504 3 .e) 27431181097513 3 .e)) 27431181097522 3 (.n (.n (.n .e 27431181097523 3 .e) 27431542182117 13 .e) 27431542182118 13 (.n (.n .e 27431542182132 13 .e) 27431542183560 13 .e))) 27431542183562 13 (.n (.n (.n (.n .e 27431542183563 13 .e) 27431542183564 13 .e) 27431542183741 13 (.n (.n .e 27431542183742 13 .e) 27431542184000 5 .e)) 27431542184039 13 (.n (.n (.n .e 27431543246082 7 .e) 27431543246088 7 .e) 27431543246150 7 (.n (.n .e 27431543246151 7 .e) 27431543246237 7 .e))))) 27431543246238 7 (.n (.n (.n (.n (.n (.n .e 27431543246376 9 .e) 27431543246379 9 (.n .e 27431543246380 9 .e)) 27431543246383 9 (.n (.n .e 27431543246384 9 .e) 27431543254656 9 .e)) 27431543254685 9 (.n (.n (.n .e 27431543254686 7 .e) 27431543254693 7 .e) 27431543254694 7 (.n (.n .e 27431543254816 9 .e) 27431543254824 9 .e))) 27431543254827 9 (.n (.n (.n (.n .e 27431543254828 9 .e) 27431543254831 9 .e) 27431543254832 9 (.n (.n .e 27431543255110 9 .e) 27431543255111 9 .e)) 27431543255166 9 (.n (.n (.n .e 27431543255167 9 .e) 27431544780048 3 .e) 27431544780052 3 (.n (.n .e 27431544780053 3 .e) 27431544780054 3 .e)))) 27431544780056 3 (.n (.n (.n (.n (.n .e 27431544780057 3 .e) 27431544780962 3 (.n .e 27431544780963 3 .e)) 27431544781007 3 (.n (.n .e 27431544796297 3 .e) 27431544799826 5 .e)) 27431544799828 5 (.n (.n (.n .e 27431544799833 5 .e) 27431544799842 5 .e) 27431544799843 5 (.n (.n .e 27431544799844 5 .e) 27431544803282 5 .e))) 27431544803300 5 (.n (.n (.n (.n .e 27431544803317 5 .e) 27431544803318 5 .e) 27431544803319 5 (.n (.n .e 27431544803320 5 .e) 27431544819721 7 .e)) 27431544820890 7 (.n (.n (.n .e 27431544820892 7 .e) 27431544820897 7 .e) 27431544820909 7 (.n (.n .e 27431544820910 7 .e) 27431544820912 7 .e))))))) 27431544820927 7 (.n (.n (.n (.n (.n (.n (.n (.n .e 27431544822042 5 .e) 27431544822043 5 (.n .e 27431544822044 5 .e)) 27431544822049 5 (.n (.n .e 27431544822062 5 .e) 27431544822063 5 .e)) 27431544822064 5 (.n (.n (.n .e 27431545650090 3 .e) 27431545650092 3 .e) 27431545650097 3 (.n (.n .e 27431545650110 3 .e) 27431545650112 3 .e))) 27431552230408 5 (.n (.n (.n (.n .e 27431552230410 5 .e) 27431552230412 5 .e) 27431552230674 5 (.n (.n .e 27431552230686 5 .e) 27431552230687 5 .e)) 27431552305312 11 (.n (.n (.n .e 27431552305316 5 .e) 27431552305320 5 .e) 27431552305331 5 (.n (.n .e 27431552305348 13 .e) 27431552305349 13 .e)))) 27431552305350 13 (.n (.n (.n (.n (.n .e 27431552305353 13 .e) 27431552455633 3 (.n .e 27431552455655 3 .e)) 27432094462992 1 (.n (.n .e 27432094463005 1 .e) 27432094463006 1 .e)) 27432094463241 1 (.n (.n (.n .e 27432094463348 1 .e) 27432094463350 1 .e) 27432094463351 1 (.n (.n .e 27432094463353 1 .e) 27432094463354 1 .e))) 27432094463355 1 (.n (.n (.n (.n .e 27432094463361 1 .e) 27432094463362 1 .e) 27432094463476 1 (.n (.n .e 27432094463482 1 .e) 27432094463483 1 .e)) 27432094463489 1 (.n (.n (.n .e 27432094463490 1 .e) 27432094463976 1 .e) 27432094463978 1 (.n (.n .e 27432094463980 1 .e) 27432094463985 1 .e))))) 27432094464007 1 (.n (.n (.n (.n (.n (.n .e 27432094464210 1 .e) 27432094464228 1 (.n .e 27432094466976 1 .e)) 27432094466984 1 (.n (.n .e 27432094466989 1 .e) 27432094466990 1 .e)) 27432094467007 1 (.n (.n (.n .e 27432094467008 1 .e) 27432094467014 1 .e) 27432094467015 1 (.n (.n .e 27432094467021 1 .e) 27432094467022 1 .e))) 27432124996978 1 (.n (.n (.n (.n .e 27432124996979 1 .e) 27432124996996 1 .e) 27432124997076 1 (.n (.n .e 27432124997090 1 .e) 27432124997091 1 .e)) 27432124997844 1 (.n (.n (.n .e 27432124997845 1 .e) 27432124997846 1 .e) 27432124997848 1 (.n (.n .e 27432124997855 1 .e) 27432124997856 1 .e)))) 27432124997859 1 (.n (.n (.n (.n (.n .e 27432125387403 1 .e) 27432125387404 1 (.n .e 27432125387581 1 .e)) 27432125387582 1 (.n (.n .e 27432125409757 1 .e) 27432125409758 1 .e)) 27432125411974 1 (.n (.n (.n .e 27432125411975 1 .e) 27432125482088 1 .e) 27432125482091 1 (.n (.n .e 27432125482092 1 .e) 27432129823816 1 .e))) 27432129823818 1 (.n (.n (.n (.n .e 27432129823819 1 .e) 27432129823820 1 .e) 27432129823860 1 (.n (.n .e 27432129823865 1 .e) 27432129836289 1 .e)) 27432129836366 1 (.n (.n (.n .e 27432129836367 1 .e) 27432129836432 1 .e) 27432129836437 1 (.n (.n .e 27432129836438 1 .e) 27432129836439 1 .e)))))) 27432129836440 1 (.n (.n (.n (.n (.n (.n (.n .e 27432129836457 1 .e) 27432129836466 1 (.n .e 27432129836467 1 .e)) 27432129836477 1 (.n (.n .e 27432129836478 1 .e) 27432129836484 1 .e)) 27432129836522 1 (.n (.n (.n .e 27432129836529 1 .e) 27432129836551 1 .e) 27432129837050 1 (.n (.n .e 27432129837052 1 .e) 27432129837057 1 .e))) 27432129837306 1 (.n (.n (.n (.n .e 27432129838297 1 .e) 27432129838302 1 .e) 27432129838303 1 (.n (.n .e 27432129838304 1 .e) 27432129838306 1 .e)) 27432129839475 1 (.n (.n (.n .e 27432129839492 1 .e) 27432129839493 1 .e) 27432129839494 1 (.n (.n .e 27432129854883 1 .e) 27432129854996 1 .e)))) 27432129854997 1 (.n (.n (.n (.n (.n .e 27432129854998 1 .e) 27432129854999 1 (.n .e 27432129855000 1 .e)) 27432129948113 1 (.n (.n .e 27432129948115 1 .e) 27432129948132 1 .e)) 27432129948133 1 (.n (.n (.n .e 27432129948134 1 .e) 27432129949414 1 .e) 27432129949415 1 (.n (.n .e 27432129949789 1 .e) 27432129949790 1 .e))) 27432129949792 1 (.n (.n (.n (.n .e 27432129950208 1 .e) 27432129950216 1 .e) 27432129950218 1 (.n (.n .e 27432129950220 1 .e) 27432129950338 1 .e)) 27432129950339 1 (.n (.n (.n .e 27432129950353 1 .e) 27432129950368 1 .e) 27432129950376 1 (.n (.n .e 27432129950377 1 .e) 27432129950378 1 .e))))) 27432129950380 1 (.n (.n (.n (.n (.n (.n .e 27432129950381 1 .e) 27432129950383 1 (.n .e 27432129950384 1 .e)) 27432129950385 1 (.n (.n .e 27432129950386 1 .e) 27432129950387 1 .e)) 27432129950398 1 (.n (.n (.n .e 27432129950399 1 .e) 27432129950400 1 .e) 27432129950404 1 (.n (.n .e 27432129950406 1 .e) 27432129950407 1 .e))) 27432129950459 1 (.n (.n (.n (.n .e 27432129950460 1 .e) 27432129950491 1 .e) 27432129950495 1 (.n (.n .e 27432129950503 1 .e) 27432130294875 1 .e)) 27432130294876 1 (.n (.n (.n .e 27432130298678 1 .e) 27432130298679 1 .e) 27432130298680 1 (.n (.n .e 27432130303135 1 .e) 27432130304288 1 .e)))) 27432130304297 1 (.n (.n (.n (.n (.n .e 27432130304306 1 .e) 27432130304307 1 .e) 27432130304591 1 (.n (.n .e 27432130304638 1 .e) 27432130304639 1 .e)) 27432130305152 1 (.n (.n (.n .e 27432130305168 1 .e) 27432130305172 1 .e) 27432130305175 1 (.n (.n .e 27432130305176 1 .e) 27432130305177 1 .e))) 27432130305189 1 (.n (.n (.n (.n .e 27432130305190 1 .e) 27432130305869 1 .e) 27432130305870 1 (.n (.n .e 27432130305940 1 .e) 27432130305942 1 .e)) 27432130305943 1 (.n (.n (.n .e 27432130305945 1 .e) 27432130306082 1 .e) 27432130306083 1 (.n (.n .e 27432130306338 1 .e) 27432130306628 1 .e)))))))))

/-- All the numbers. -/
def Qn : List Nat := tree.toList

/-- The cloud. -/
def Q45 : List (List Bool) := Qn.map (dec 45)

/-- The longest alternating run from a window; 0 outside the cloud. -/
def rk (n : Nat) : Nat := tree.find n

/-- What each number must satisfy. -/
def Good (n : Nat) : Prop :=
  1 ≤ rk n ∧ rk n ≤ 17 ∧ (n >>> 34 = 1596 ∨ n >>> 34 = 1594) ∧ dec 45 n ∉ LockAB.Win ∧ n >>> 44 = 1 ∧
  ∀ p1 p2 : Bool, image 45 n p1 p2 >>> 49 = 5 ∧ rk (nxt 45 n p1 p2) ≠ 0 ∧
    (nxt 45 n p1 p2 >>> 34 ≠ n >>> 34 → rk (nxt 45 n p1 p2) + 1 ≤ rk n)

instance : DecidablePred Good := fun n => by unfold Good; infer_instance

theorem good : ∀ n, n ∈ Qn → Good n := by decide +kernel

theorem mem_of_rk {n : Nat} (h : rk n ≠ 0) : n ∈ Qn := Tree.mem_of_find tree n h

/-- **The cloud is closed.** -/
theorem closed : Closed 45 Q45 :=
  closed_fast (by decide) Qn (fun n hn => by
    obtain ⟨_, _, _, _, h5, h6⟩ := good n hn
    exact ⟨h5, fun p1 p2 => ⟨(h6 p1 p2).1, mem_of_rk (h6 p1 p2).2.1⟩⟩)

/-- **For ever.** -/
theorem cloud_forever {x : Row} {L : Nat} (hL : 2 ≤ L) (h : Held 45 Q45 x L) :
    ∀ n z, iter z n = x → Held 45 Q45 z (L + 3 * n) := held_forever closed hL h

/-- **Cloud and lock are apart.** -/
theorem cloud_not_lock : ∀ w, w ∈ Q45 → w ∉ LockAB.Win := by
  intro w hw; obtain ⟨n, hn, rfl⟩ := List.mem_map.1 hw; exact (good n hn).2.2.2.1

/-- **A row in the cloud never reaches the alternating lock.** -/
theorem avoids_lock {x : Row} {L : Nat} (hL : 2 ≤ L) (h : Held 45 Q45 x L) :
    ∀ n z, iter z n = x → seg z (L + 3 * n) 45 ∉ LockAB.Win :=
  fun n z hz => cloud_not_lock _ (cloud_forever hL h n z hz).1

/-- **A row in the cloud is not periodic.** -/
theorem not_periodic {x : Row} {L P : Nat} (hL : 2 ≤ L) (h : Held 45 Q45 x L) (hP : 0 < P) : iter x P ≠ x := by
  refine held_not_periodic closed (by decide) (fun w hw => ?_) hL h hP
  obtain ⟨n, hn, rfl⟩ := List.mem_map.1 hw
  exact wall_of_letter (by decide) (good n hn).2.2.1

/-- **Alternation is bounded.** Along any backward history in the cloud, the 11 cells at the wall cannot change on 17 ticks running. -/
theorem no_long_alternation {L : Nat} (hL : 2 ≤ L) (z : Nat → Row) (hz : ∀ i, step (z (i + 1)) = z i)
    (h : Held 45 Q45 (z 0) L) :
    ¬ ∀ i, i < 17 → seg (z (i + 1)) (L + 3 * (i + 1) + 34) 11 ≠ seg (z i) (L + 3 * i + 34) 11 := by
  intro hc
  have held : ∀ i, Held 45 Q45 (z i) (L + 3 * i) := by
    intro i
    induction i with
    | zero => exact h
    | succ i ih =>
      have := held_back closed (L := L + 3 * i) (by omega) (hz i) ih
      rwa [show L + 3 * i + 3 = L + 3 * (i + 1) by omega] at this
  have top : ∀ (x : Row) (K n : Nat), seg x K 45 = dec 45 n → seg x (K + 34) 11 = dec 11 (n >>> 34) := by
    intro x K n e
    have d := seg_drop x K 45 34 (by decide)
    rw [e, dec_drop 45 34 n (by decide)] at d
    exact d.symm
  have down : ∀ i, i ≤ 17 → ∃ n, n ∈ Qn ∧ seg (z i) (L + 3 * i) 45 = dec 45 n ∧ rk n + i ≤ 17 := by
    intro i
    induction i with
    | zero =>
      intro _
      obtain ⟨n, hn, e⟩ := List.mem_map.1 (held 0).1
      exact ⟨n, hn, e.symm, (good n hn).2.1⟩
    | succ i ih =>
      intro hi
      obtain ⟨n, hn, e, hr⟩ := ih (by omega)
      have g := good n hn
      have hnext := next_seg closed (L := L + 3 * i) (by omega) (hz i) (held i)
      rw [e, next_fast (by decide) g.2.2.2.2.1] at hnext
      have e3 : L + 3 * i + 3 = L + 3 * (i + 1) := by omega
      rw [e3] at hnext
      obtain ⟨_, hne, hdec⟩ := g.2.2.2.2.2 (z (i + 1) (L + 3 * i - 1)) (z (i + 1) (L + 3 * i - 2))
      refine ⟨_, mem_of_rk hne, hnext, ?_⟩
      have ch := hc i (by omega)
      have hlet : nxt 45 n (z (i + 1) (L + 3 * i - 1)) (z (i + 1) (L + 3 * i - 2)) >>> 34 ≠ n >>> 34 := by
        intro q
        apply ch
        rw [top _ _ _ hnext, top _ _ _ e, q]
      have := hdec hlet
      omega
  obtain ⟨n, hn, _, hr⟩ := down 17 (Nat.le_refl _)
  have := (good n hn).1
  omega

end Cloud

/-! ## A row that enters the third lock -/

namespace Entry
open Cloud

/-- The row's cells below 850. -/
def E : Nat := 0x2aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab1e614b8e559ce1eb5af79ec4b49c942ff71686d7b1f8feea41c22e007f1b8a2a00548ae0e88092689b1f5e23635d5c78434763f914c2c3d26e1dde151efbc42a5bb3f34c886201

/-- The letters at ticks 0 to 110, a set bit for `B`. -/
def LB : Nat := 0x4aaa54a92aa54a92492492492492

/-- The row: anchored at bit 0, rain above bit 569. -/
def row (j : Nat) : Bool := if j < 850 then E.testBit j else decide ((j - 850) % 2 = 1)

theorem row_low : ∀ j, j < 850 → row j = E.testBit j := by
  intro j hj; simp [row, hj]

theorem chk_E : ∀ j, j < 280 → E.testBit (569 + j + 1) = !E.testBit (569 + j) := by decide +kernel

theorem chk_top : E.testBit 849 = true := by decide +kernel

theorem row_tail : ∀ j, 569 ≤ j → row (j + 1) = !row j := by
  intro j hj
  by_cases c : j + 1 < 850
  · rw [row_low _ c, row_low j (by omega)]
    have := chk_E (j - 569) (by omega)
    rwa [show 569 + (j - 569) = j by omega] at this
  · by_cases d : j = 849
    · subst d
      rw [row_low 849 (by omega), chk_top]; decide
    · have q : 850 ≤ j := by omega
      simp only [row, show ¬j < 850 by omega, show ¬j + 1 < 850 by omega, ite_false]
      by_cases a : (j - 850) % 2 = 1
      · simp [a]; omega
      · simp [a]; omega

theorem iter_row (k j : Nat) (hj : j < 850) : iter row k j = (fwN k E).testBit j := by
  rw [iter_low row_low k j hj, iter_fw]

theorem seg_row (k L n : Nat) (h : L + n ≤ 850) : seg (iter row k) L n = seg (fwN k E).testBit L n :=
  seg_ext n L L (fun i hi => iter_row k (L + i) (by omega))

theorem chk_t : ∀ j, j < 550 → (fwN 110 E).testBit (239 + j + 1) = !(fwN 110 E).testBit (239 + j) := by decide +kernel

theorem tail110 : ∀ j, 239 ≤ j → iter row 110 (j + 1) = !iter row 110 j := by
  intro j hj
  by_cases c : j < 789
  · rw [iter_row _ _ (by omega), iter_row _ _ (by omega)]
    have := chk_t (j - 239) (by omega)
    rwa [show 239 + (j - 239) = j by omega] at this
  · exact iter_tail row_tail 110 j (by omega)

theorem chk_letters : ∀ k, k < 111 → seg (fwN k E).testBit (229 + 3 * (110 - k)) 11 = if LB.testBit k then wordB else wordA := by
  decide +kernel

/-- **The letters at ticks 0 to 110.** -/
theorem letters : ∀ k, k ≤ 110 → seg (iter row k) (229 + 3 * (110 - k)) 11 = if LB.testBit k then wordB else wordA := by
  intro k hk
  rw [seg_row _ _ _ (by omega)]
  exact chk_letters k (by omega)

theorem held110 : Held 11 letterSet (iter row 110) 229 := by
  refine ⟨?_, tail110⟩
  have := letters 110 (Nat.le_refl _)
  simp only [Nat.sub_self, Nat.mul_zero, Nat.add_zero] at this
  rw [this]
  cases LB.testBit 110 <;> simp [letterSet]

/-- Tick `k` is held by the letters. -/
theorem held_k (k : Nat) (hk : k ≤ 110) : Held 11 letterSet (iter row k) (229 + 3 * (110 - k)) := by
  have e : iter (iter row k) (110 - k) = iter row 110 := by
    rw [← iter_add, show k + (110 - k) = 110 by omega]
  exact held_forever letters_closed (by omega) held110 (110 - k) _ e

theorem chk_97 : rk 27392328885014 ≠ 0 ∧ seg (fwN 97 E).testBit 234 45 = dec 45 27392328885014 := by decide +kernel

theorem chk_6 : 37338680436793518946018258025312893609782730154505790 ∈ LockThird.All ∧ seg (fwN 6 E).testBit 377 175 = dec 175 37338680436793518946018258025312893609782730154505790 := by decide +kernel

theorem chk_7 : seg (fwN 7 E).testBit 374 175 ∉ LockThird.Win := by decide +kernel

/-- **A row in the cloud enters the third lock.** The row is anchored. Its image at tick 97 is in the cloud, its image at tick 7 is outside
the third lock, its image at tick 6 is inside it, and all its images through tick 110 read letters. -/
theorem entry :
    row 0 = true ∧ Held 45 Q45 (iter row 97) 234 ∧ seg (iter row 7) 374 175 ∉ LockThird.Win ∧
      Held 175 LockThird.Win (iter row 6) 377 ∧
      ∀ k, k ≤ 110 → seg (iter row k) (229 + 3 * (110 - k)) 11 = if LB.testBit k then wordB else wordA := by
  refine ⟨by decide +kernel, ⟨?_, ?_⟩, ?_, ⟨?_, ?_⟩, letters⟩
  · rw [seg_row _ _ _ (by omega), chk_97.2]
    exact List.mem_map.2 ⟨_, mem_of_rk chk_97.1, rfl⟩
  · intro j hj
    exact (held_k 97 (by omega)).2 j (by omega)
  · rw [seg_row _ _ _ (by omega)]
    exact chk_7
  · rw [seg_row _ _ _ (by omega), chk_6.2]
    exact List.mem_map.2 ⟨_, chk_6.1, rfl⟩
  · intro j hj
    exact (held_k 6 (by omega)).2 j (by omega)

end Entry

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The theorems of sections 2 to 4, as Lean prints them:

```wl
opens = {"Rule30Submission", "Rule30Submission.WindowClosed", "Rule30Submission.Reset", "Rule30Submission.Cloud", "Rule30Submission.Entry", "Ruliology.CellularAutomata.Rule30FrozenRuler"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
heads1 = {"predecessor_unique", "step_rain_tail", "back_rain_tail", "front_back", "front_not_periodic", "deep_words", "no_BB", "no_AAA", "witness_ABA", "Reset.reset", "Reset.above", "Reset.again", "Reset.letters", "WindowClosed.held_forever", "WindowClosed.held_not_periodic", "WindowClosed.letters_closed", "WindowClosed.letter_after_B", "WindowClosed.letter_after_A"};
heads2 = {"LockAB.letters", "LockAB.not_periodic", "LockAB.witness", "LockAB.floor", "LockAAB.letters", "LockAAB.not_periodic", "LockAAB.witness", "LockAAB.floor", "LockThird.letters", "LockThird.not_periodic", "LockThird.witness", "LockThird.no_floor", "Cloud.closed", "Cloud.cloud_not_lock", "Cloud.avoids_lock", "Cloud.not_periodic", "Cloud.no_long_alternation", "Entry.entry"};
show[heads1, "TypeForm"]
```

The locks, the cloud and the row that enters:

```wl
show[heads2, "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, Join[heads1, heads2]]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.Entry.entry"]["KernelCheck"]
```
