---
Template: ComputationalEssay
Name: The white end: no column of rule 30 settles into 1 0^q, for any q ≥ 10
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-22
Description: A partial result for Problem 1 of the Rule 30 Prize, proved in Lean against the official statements: the center column is never eventually the repeating word 1 0^q for any q ≥ 10, and the same holds for every column of every configuration with a leftmost black cell
Abstract: Problem 1 asks whether the center column of rule 30 is ever eventually periodic. The kit's catalog excludes the words 1 0^10, 1 0^11 and 1 0^12 by three separate certificates. This essay excludes the whole family 1 0^q, uniformly in q ≥ 10, as the headline theorem Rule30Submission.not_eventuallyWord_white_end, together with the same statement for every column of every configuration with a leftmost black cell (Rule30Submission.white_end). The argument is Jen's: the eight cells right of the column form a finite relaxation on which, after three periods, the next column is forced to read 1 0 0 1^(q-2); two adjacent periodic columns contradict the moving left edge. What is new is the uniformity: a periodicity of the relaxation's white step (W^26 = W^22 on the sets that occur) makes sixteen kernel checks cover every q. The verifier's replay accepts the module with the three standard axioms only. Nothing is claimed for q ≤ 9, and this is not a solution of Problem 1.
Keywords: [rule 30, Rule 30 Prize, Problem 1, eventually periodic, Jen's theorem, strip relaxation, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record, PROOFS.md entry 40](https://github.com/ghywel/placego/blob/main/PROOFS.md)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[wolframcollatzmahler.com](https://www.wolframcollatzmahler.com)"]
---

## The question

Rule 30 updates every cell from itself and its two neighbors: the new color is *left* XOR (*center* OR *right*). From a single black cell it grows a pattern whose center column looks random. Problem 1 of the Rule 30 Prize asks whether that column is ever eventually periodic: whether, from some time on, it repeats a word forever.

The first 60 steps, with the center column in red:

```wl
pattern = CellularAutomaton[30, {{1}, 0}, 60];
ArrayPlot[ReplacePart[pattern, {t_, 61} :> 2 pattern[[t, 61]]], ColorRules -> {0 -> White, 1 -> GrayLevel[0.15], 2 -> StandardRed}, ImageSize -> 520]
```

A proof of Problem 1 has to rule out every word, from every starting time. This essay rules out one infinite family of words: `1 0^q`, one black cell followed by `q` white cells, repeated, for every `q ≥ 10`. It proves it for the center column of the single seed, in the kit's own vocabulary, and for every column of every configuration that has a leftmost black cell.

## The center column, and the words it does and does not settle into

The first 10,000 cells of the center column, and the first 20 of them:

```wl
center = CellularAutomaton[30, {{1}, 0}, {10^4 - 1, {{0}}}];
Take[center, 20]
```

The block `1 0^q` does occur in the column as a finite block; what the theorem excludes is the column *settling into* it. How often each block occurs in the first 10,000 cells, and the longest run of white cells there:

```wl
{Table[{q, SequenceCount[center, Prepend[ConstantArray[0, q], 1]]}, {q, {8, 9, 10, 11, 12, 15, 20}}], Max[Length /@ Select[Split[center], First[#] == 0 &]]}
```

So `1 0^10` occurs six times, `1 0^12` twice, and no white run is longer than 12. None of this proves anything about the infinite column; it shows that the excluded words are not exotic. The kit's catalog already excludes `1 0^10`, `1 0^11` and `1 0^12`, each by its own strip certificate (`Rule30StripCertificateTable`), and the mirror-image family `1^r 0` for large `r` (`Rule30BlackRunBlocks`). The family `1 0^q` as a whole, for every `q`, is what is added here.

## The idea: the eight cells to the right are a finite machine

Suppose column `c` reads `1 0^q` from some time on. Watch the eight cells immediately to its right, `c + 1, …, c + 8`. Their next values depend on column `c` (known: the word), on themselves, and on one unknown cell `c + 9`. Allow that unknown cell both values at every step. The eight cells then move through a finite nondeterministic system with 256 states, and every actual history of rule 30 is one path of it.

The system, with a state as a number below 256 (bit `j` is cell `c + 1 + j`), the column's bit `w` and the outside bit `u`:

```wl
stp[w_, s_, u_] := BitAnd[BitXor[BitAnd[BitOr[BitShiftLeft[s, 1], w], 255], BitOr[s, BitShiftRight[s, 1], BitShiftLeft[u, 7]]], 255];
img[w_, S_] := Union[Flatten[Table[{stp[w, s, 0], stp[w, s, 1]}, {s, S}]]];
mac[q_, S_] := Nest[img[0, #] &, img[1, S], q];
reach[q_, n_] := Nest[mac[q, #] &, Range[0, 255], n];
```

`img` is the image of a set of states under one step, over both values of the outside bit; `mac[q, S]` applies one period of `1 0^q` (a black step, then `q` white steps); `reach[q, n]` is the set of states reachable after `n` periods from every start.

The sets shrink and stop. After three periods they are fixed, and on the fixed set the first cell of the strip, column `c + 1`, takes a single value at every tick of the period. The number of states after 1, 2, 3, 4 periods, whether one more period maps the third set into itself, and column `c + 1` over one period read off the fixed set (`?` marks a tick where both values occur):

```wl
tick[S_, i_] := If[i == 0, S, Nest[img[0, #] &, img[1, S], i - 1]];
word[q_] := StringJoin[Table[Union[BitAnd[#, 1] & /@ tick[reach[q, 3], i]] /. {{0} -> "0", {1} -> "1", {0, 1} -> "?"}, {i, 0, q}]];
Grid[Prepend[Table[{q, Length /@ Table[reach[q, n], {n, 1, 4}], mac[q, reach[q, 3]] === reach[q, 3], word[q]}, {q, {9, 10, 11, 12, 15, 20, 25}}], {"q", "states after 1, 2, 3, 4 periods", "fixed after 3", "column c+1 over one period"}], Frame -> All, Alignment -> Left]
```

For every `q ≥ 10` shown, column `c + 1` is forced: it reads `1 0 0 1^(q-2)`, so it is periodic with the same period `q + 1`. At `q = 9` the third set is not yet fixed and one tick is undetermined; the method says nothing there, and the proof below does not claim it.

**Every `q`, from finitely many checks.** The white step `W = img[0, ·]` repeats on the sets that occur: `W^26 = W^22` on each set `img[1, reach[q, n]]`, `n = 0, …, 3`, for `q = 22, …, 25`. So the behaviour of `q ≥ 26` is that of `22 + (q − 22) mod 4`, and sixteen checks, `q = 10, …, 25`, cover every `q ≥ 10`:

```wl
Table[{q, And @@ Table[Nest[img[0, #] &, img[1, reach[q, n]], 26] === Nest[img[0, #] &, img[1, reach[q, n]], 22], {n, 0, 3}]}, {q, 22, 25}]
```

**The contradiction: Jen's theorem with a clock.** Columns `c` and `c + 1` are now both periodic, with period `q + 1`, from some time `a` on. Rule 30 is left-permutive: the cell at `c − 1` at time `t` is determined by the cells at `c` at times `t` and `t + 1` and at `c + 1` at time `t`. So periodicity of two adjacent columns on a time window propagates to the column on their left, on a window one step shorter, and by induction `L` columns to the left on a window `L` shorter. Meanwhile the leftmost black cell of the configuration moves one cell left per step: at time `t` it is at `e − t`, with everything left of it white. Take the column `c − j` with `j = a + P + L`, where `L` is the distance from column `c` to the leftmost black cell at time 0. At time `a` that column is left of the edge, so white; at time `a + P` the edge is exactly there, so black; yet the two times differ by one period, so periodicity (which reaches that column on a window long enough to contain both times, once the window `[a, b]` is taken long enough) makes them equal. That is Theorem A below: `b ≤ 2a + L + 2P − 1`, which fails for `b` large. If the leftmost black cell starts to the right of column `c`, the clock is re-based after it has passed.

Everything in this section is a computation or a sketch. The proof is the next section.

## The formal proof

The module, as the verifier rebuilds and checks it. Its definitions and lemmas follow the sketch: `stp`, `img`, `Wp`, `mac`, `reach` are the finite machine; `checkQ` and `repOK` are the kernel-decided facts; `win` encodes the actual eight cells and `win_step` proves that the encoding follows rule 30 exactly; `edge`, `left`, `theorem_A` and `no_two_periodic` are Jen's theorem with a clock on the kit's `evol`; `core` and `white_end` assemble the contradiction; the bridge lemmas turn the kit's `EventuallyWord` into the module's `Reads` through the kit's `evol_seed`.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["import Rule30PrizeKit
import Mathlib

/-!
# The white end: no column of rule 30 ever settles into the word `1 0^q`, for any `q ≥ 10`

**Partial result for Problem 1.** For every `q ≥ 10`, the center column of the single-seed pattern
is not eventually the repeating word `1 0^q` (one black cell, then `q` white cells): the kit's
`EventuallyWord (true :: List.replicate q false)` is false. The same holds for every column of
every configuration with a leftmost black cell, every finite nonzero configuration included.

**What is new.** The kit's `Rule30StripCertificateTable` excludes `1 0^q` for `q = 10, 11, 12`
by three separate certificates, and `Rule30BlackRunBlocks` treats the mirror-image family
`1^r 0`. This module excludes the whole family `1 0^q`, uniformly in `q`: finitely many kernel
checks (for `q = 10 … 25`) and a periodicity of the one-sided strip relaxation (its white-step
relation satisfies `W^26 = W^22` on the sets that occur) cover every `q ≥ 26`.

**The argument** (the route of Jen's theorem, as the kit's strip certificates use it).
1. *A finite relaxation.* Watch the eight cells right of the column, with an arbitrary cell
   beyond them at every step. Every actual history is a path of this nondeterministic system.
   One period of `1 0^q` is one black step followed by `q` white steps; from any start, three
   periods reach a set of states that one more period maps into itself (`checkQ`, `reach`).
2. *Column `c + 1` is determined.* On that set, the first cell of the strip takes a single value at
   every tick of the period: column `c + 1` reads `1 0 0 1^(q-2)`. So columns `c` and `c + 1` are
   both periodic with period `q + 1` from some time on.
3. *Every `q ≥ 26`.* The white-step relation `W` on 256-bit sets has `W^26 = W^22` on the sets
   that occur, so `q` behaves as `22 + (q - 22) % 4` (`repOK`, `Wp_period`).
4. *The contradiction.* Two adjacent columns periodic for ever, in a configuration with a leftmost
   black cell, contradict Jen's theorem in its clocked form (`theorem_A` below: the edge moves one
   cell left per step and the periodicity propagates left by left-permutivity). If the leftmost
   black cell starts right of column `c`, time is re-based.

The finite facts are decided by the kernel (`decide +kernel`), one declaration per `q`; the
control `control_q9` shows the check fails at `q = 9`, so it is not vacuous.

**Provenance.** Entry 40 of the Wolfram · Collatz · Mahler record (github.com/ghywel/placego,
PROOFS.md), found and machine-checked by Local (Claude) on 2026-10-09 (`tests/probes/lean/WhiteEnd.lean`),
second-read by Cloud (Claude, CL110) and GPT (GC880, GC893, GC898). This module is that proof
restated on the kit's `evol` and `cell`, with the bridge to `EventuallyWord` added. Source of the
mechanism: E. Jen, *Global properties of cellular automata*, J. Stat. Phys. 43 (1986) 219–242.

**Not claimed.** Nothing about `q ≤ 9`; `q = 1` is the word `10`, the period-2 case itself.
This is a partial result, not a solution of Problem 1.
-/

-- Sequential elaboration: the kernel checks below would otherwise run in parallel and stack their memory.
set_option Elab.async false

namespace Rule30Submission

open Ruliology.CellularAutomata
open Ruliology.CellularAutomata.Rule30Jen
open Ruliology.CellularAutomata.Rule30Prize
open Ruliology.CellularAutomata.Rule30Realization
open Ruliology.CellularAutomata.Rule30StripCertificates

/-! ## Jen's theorem with a clock (Theorem A), on the kit's `evol` -/

/-- The leftmost black cell moves one cell to the left per step, and nothing is black left of it. -/
lemma edge (x0 : ℤ → Bool) (e : ℤ) (he : x0 e = true) (hl : ∀ j < e, x0 j = false) (t : ℕ) :
    evol x0 t (e - t) = true ∧ ∀ j < e - t, evol x0 t j = false := by
  induction t with
  | zero => simpa using ⟨he, hl⟩
  | succ t ih =>
    obtain ⟨h1, h2⟩ := ih
    constructor
    · show xor (evol x0 t (e - ↑(t + 1) - 1)) (evol x0 t (e - ↑(t + 1)) || evol x0 t (e - ↑(t + 1) + 1)) = true
      have a1 : evol x0 t (e - ↑(t + 1) - 1) = false := h2 _ (by push_cast; omega)
      have a2 : evol x0 t (e - ↑(t + 1)) = false := h2 _ (by push_cast; omega)
      have a3 : e - ↑(t + 1) + 1 = e - ↑t := by push_cast; ring
      rw [a1, a2, a3, h1]; rfl
    · intro j hj
      show xor (evol x0 t (j - 1)) (evol x0 t j || evol x0 t (j + 1)) = false
      have b1 : evol x0 t (j - 1) = false := h2 _ (by push_cast at hj; omega)
      have b2 : evol x0 t j = false := h2 _ (by push_cast at hj; omega)
      have b3 : evol x0 t (j + 1) = false := h2 _ (by push_cast at hj; omega)
      rw [b1, b2, b3]; rfl

/-- Column `k` is `P`-periodic on the time window `[a, b]`. -/
def Per (x0 : ℤ → Bool) (k : ℤ) (P a b : ℕ) : Prop :=
  ∀ t : ℕ, a ≤ t → t + P ≤ b → evol x0 t k = evol x0 (t + P) k

/-- Left-permutivity: two periodic adjacent columns make the column to their left periodic, on a window one shorter. -/
lemma left (x0 : ℤ → Bool) (k : ℤ) (P a b : ℕ) (hP : 1 ≤ P) (h0 : Per x0 k P a b) (h1 : Per x0 (k + 1) P a b) :
    Per x0 (k - 1) P a (b - 1) := by
  intro t ht htb
  have inv : ∀ s : ℕ, evol x0 s (k - 1) = xor (evol x0 (s + 1) k) (evol x0 s k || evol x0 s (k + 1)) := by
    intro s
    show evol x0 s (k - 1) = xor (xor (evol x0 s (k - 1)) (evol x0 s k || evol x0 s (k + 1))) (evol x0 s k || evol x0 s (k + 1))
    cases evol x0 s (k - 1) <;> cases (evol x0 s k || evol x0 s (k + 1)) <;> rfl
  rw [inv t, inv (t + P)]
  have e1 : evol x0 (t + 1) k = evol x0 (t + 1 + P) k := h0 (t + 1) (by omega) (by omega)
  have e2 : evol x0 t k = evol x0 (t + P) k := h0 t ht (by omega)
  have e3 : evol x0 t (k + 1) = evol x0 (t + P) (k + 1) := h1 t ht (by omega)
  rw [e1, e2, e3, show t + 1 + P = t + P + 1 by ring]

lemma left_iter (x0 : ℤ → Bool) (k : ℤ) (P a b : ℕ) (hP : 1 ≤ P) (h0 : Per x0 k P a b) (h1 : Per x0 (k + 1) P a b) :
    ∀ j : ℕ, Per x0 (k - j) P a (b - j) ∧ Per x0 (k - j + 1) P a (b - j) := by
  intro j
  induction j with
  | zero => simpa using ⟨h0, h1⟩
  | succ j ih =>
    obtain ⟨g0, g1⟩ := ih
    have g := left x0 (k - j) P a (b - j) hP g0 (by simpa using g1)
    refine ⟨?_, ?_⟩
    · have : (k - ↑(j + 1)) = k - ↑j - 1 := by push_cast; ring
      rw [this, show b - (j + 1) = b - j - 1 by omega]; exact g
    · have e : (k - ↑(j + 1) + 1) = k - ↑j := by push_cast; ring
      rw [e, show b - (j + 1) = b - j - 1 by omega]
      intro t ht htb
      exact g0 t ht (by omega)

/-- **Theorem A** (Jen's theorem with a clock). If columns `c` and `c + 1` are `P`-periodic on `[a, b]`
and the leftmost black cell is `L` cells left of column `c` at time `0`, then `b ≤ 2a + L + 2P - 1`. -/
theorem theorem_A (x0 : ℤ → Bool) (c : ℤ) (L : ℕ) (hc : x0 (c - L) = true) (hl : ∀ j < c - L, x0 j = false)
    (P a b : ℕ) (hP : 1 ≤ P) (h0 : Per x0 c P a b) (h1 : Per x0 (c + 1) P a b) :
    b ≤ 2 * a + L + 2 * P - 1 := by
  by_contra hb
  push Not at hb
  set j : ℕ := a + P + L with hj
  have hper := (left_iter x0 c P a b hP h0 h1 j).1
  have E := edge x0 (c - L) hc hl
  have black : evol x0 (a + P) (c - j) = true := by
    have := (E (a + P)).1
    have e : c - ↑L - ↑(a + P) = c - ↑j := by rw [hj]; push_cast; ring
    rwa [e] at this
  have white : evol x0 a (c - j) = false := by
    have := (E a).2 (c - j) (by rw [hj]; push_cast; omega)
    exact this
  have := hper a le_rfl (by omega)
  rw [white, black] at this
  exact absurd this (by decide)

/-- Two adjacent columns are never both periodic for ever, when there is a leftmost black cell. -/
theorem no_two_periodic (x0 : ℤ → Bool) (c : ℤ) (L : ℕ) (hc : x0 (c - L) = true) (hl : ∀ j < c - L, x0 j = false)
    (P a : ℕ) (hP : 1 ≤ P)
    (h0 : ∀ t : ℕ, a ≤ t → evol x0 t c = evol x0 (t + P) c)
    (h1 : ∀ t : ℕ, a ≤ t → evol x0 t (c + 1) = evol x0 (t + P) (c + 1)) : False := by
  have := theorem_A x0 c L hc hl P a (2 * a + L + 2 * P) hP (fun t ht _ => h0 t ht) (fun t ht _ => h1 t ht)
  omega

/-- Evolution is a semigroup: evolving `evol x0 k` for `t` steps is evolving `x0` for `k + t`. -/
lemma evol_add (x0 : ℤ → Bool) (k t : ℕ) : evol (evol x0 k) t = evol x0 (k + t) := by
  induction t with
  | zero => rfl
  | succ t ih =>
    funext p
    show rule (evol (evol x0 k) t (p - 1)) (evol (evol x0 k) t p) (evol (evol x0 k) t (p + 1)) =
      rule (evol x0 (k + t) (p - 1)) (evol x0 (k + t) p) (evol x0 (k + t) (p + 1))
    rw [ih]

/-! ## The finite relaxation on eight cells -/

/-- One step of the eight cells: state bit `j` is cell `c + 1 + j`, `w` the column's bit, `u` the cell beyond. -/
def stp (w s u : ℕ) : ℕ := ((((s <<< 1) ||| w) &&& 255) ^^^ (s ||| ((s >>> 1) ||| (u <<< 7)))) &&& 255

def imgAux (w S n : ℕ) : ℕ → ℕ :=
  Nat.rec (motive := fun _ => ℕ → ℕ) (fun acc => acc)
    (fun k ih acc => ih (if S.testBit k then acc ||| (1 <<< stp w k 0) ||| (1 <<< stp w k 1) else acc)) n

lemma imgAux_succ (w S n acc : ℕ) : imgAux w S (n + 1) acc =
    imgAux w S n (if S.testBit n then acc ||| (1 <<< stp w n 0) ||| (1 <<< stp w n 1) else acc) := rfl

/-- The image of the set `S` (a 256-bit number) under one step with column bit `w` and every outside bit. -/
def img (w S : ℕ) : ℕ := imgAux w S 256 0

/-- `Wp j S`: `j` white steps. -/
def Wp : ℕ → ℕ → ℕ
  | 0, S => S
  | j + 1, S => img 0 (Wp j S)

/-- One period of the word `1 0^q`: a black step, then `q` white steps. -/
def mac (q S : ℕ) : ℕ := Wp q (img 1 S)

def reach (q : ℕ) : ℕ → ℕ
  | 0 => 2 ^ 256 - 1
  | n + 1 => mac q (reach q n)

/-- Every state in `S` has cell `c + 1` equal to `b`. -/
def bit0Const (S : ℕ) (b : Bool) : Bool := (List.range 256).all fun s => !(S.testBit s) || (s.testBit 0 == b)

def ticksAux : ℕ → ℕ → ℕ → Bool
  | 0, _, _ => true
  | r + 1, j, X => bit0Const X (decide (2 ≤ j)) && ticksAux r (j + 1) (img 0 X)

/-- Cell `c + 1` at the `q` ticks after the black one: `0, 0`, then `1`. -/
def ticksOK (q S : ℕ) : Bool := ticksAux q 0 (img 1 S)

def checkQ (q : ℕ) : Bool :=
  mac q (reach q 3) == reach q 3 && bit0Const (reach q 3) true && ticksOK q (reach q 3)

def repOK (q : ℕ) : Bool :=
  (List.range 4).all (fun n => Wp 26 (img 1 (reach q n)) == Wp 22 (img 1 (reach q n))) && ticksOK 26 (reach q 3)

-- The finite facts, one kernel check per word length (with Elab.async off, memory stays near one check's).
set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check10 : checkQ 10 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check11 : checkQ 11 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check12 : checkQ 12 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check13 : checkQ 13 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check14 : checkQ 14 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check15 : checkQ 15 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check16 : checkQ 16 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check17 : checkQ 17 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check18 : checkQ 18 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check19 : checkQ 19 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check20 : checkQ 20 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check21 : checkQ 21 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check22 : checkQ 22 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check23 : checkQ 23 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check24 : checkQ 24 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma check25 : checkQ 25 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma rep22 : repOK 22 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma rep23 : repOK 23 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma rep24 : repOK 24 = true := by decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
lemma rep25 : repOK 25 = true := by decide +kernel

lemma checks (q : ℕ) (h1 : 10 ≤ q) (h2 : q ≤ 25) : checkQ q = true := by
  interval_cases q
  exacts [check10, check11, check12, check13, check14, check15, check16, check17, check18, check19, check20,
    check21, check22, check23, check24, check25]

lemma reps (q : ℕ) (h1 : 22 ≤ q) (h2 : q ≤ 25) : repOK q = true := by
  interval_cases q
  exacts [rep22, rep23, rep24, rep25]

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
/-- Control: the check is not vacuous; it fails at `q = 9`, where width 8 does not determine cell `c + 1`. -/
lemma control_q9 : checkQ 9 = false := by decide +kernel

set_option maxRecDepth 100000 in
lemma stp_bits : ∀ s < 256, ∀ w u : Bool, ∀ j < 8,
    (stp w.toNat s u.toNat).testBit j =
      xor (if j = 0 then w else s.testBit (j - 1)) (s.testBit j || if j = 7 then u else s.testBit (j + 1)) := by
  decide

lemma stp_lt (w s u : ℕ) : stp w s u < 256 := by
  unfold stp; exact lt_of_le_of_lt Nat.and_le_right (by norm_num)

/-! ## Sets: membership -/

lemma testBit_shift_self (k : ℕ) : (1 <<< k).testBit k = true := by
  rw [Nat.one_shiftLeft]; exact Nat.testBit_two_pow_self

lemma imgAux_acc (w S : ℕ) : ∀ n acc y, acc.testBit y = true → (imgAux w S n acc).testBit y = true := by
  intro n
  induction n with
  | zero => intro acc y h; exact h
  | succ n ih =>
    intro acc y h
    rw [imgAux_succ]
    apply ih
    split_ifs
    · simp [Nat.testBit_or, h]
    · exact h

lemma imgAux_mem (w S u : ℕ) (hu : u ≤ 1) :
    ∀ n acc s, s < n → S.testBit s = true → (imgAux w S n acc).testBit (stp w s u) = true := by
  intro n
  induction n with
  | zero => intro acc s hs; omega
  | succ n ih =>
    intro acc s hs hS
    rw [imgAux_succ]
    rcases Nat.lt_succ_iff_lt_or_eq.mp hs with h | h
    · exact ih _ s h hS
    · subst h
      apply imgAux_acc
      rw [if_pos hS]
      interval_cases u <;> simp [Nat.testBit_or]

lemma img_mem (w S s u : ℕ) (hs : s < 256) (hu : u ≤ 1) (hS : S.testBit s = true) :
    (img w S).testBit (stp w s u) = true :=
  imgAux_mem w S u hu 256 0 s hs hS

lemma Wp_succ' (j X : ℕ) : Wp (j + 1) X = Wp j (img 0 X) := by
  induction j generalizing X with
  | zero => rfl
  | succ j ih => show img 0 (Wp (j + 1) X) = img 0 (Wp j (img 0 X)); rw [ih]

lemma Wp_add (a b X : ℕ) : Wp (a + b) X = Wp a (Wp b X) := by
  induction a with
  | zero => simp [Wp]
  | succ a ih => rw [show a + 1 + b = (a + b) + 1 by ring]; show img 0 (Wp (a + b) X) = img 0 (Wp a (Wp b X)); rw [ih]

lemma Wp_period (X : ℕ) (h : Wp 26 X = Wp 22 X) : ∀ j, 22 ≤ j → Wp j X = Wp (22 + (j - 22) % 4) X := by
  intro j
  induction j using Nat.strong_induction_on with
  | _ j ih =>
    intro hj
    by_cases h26 : j < 26
    · congr 1; omega
    · have e1 : Wp j X = Wp (j - 4) X := by
        rw [show j = (j - 26) + 26 by omega, Wp_add, h, ← Wp_add]; congr 1
      rw [e1, ih (j - 4) (by omega) (by omega)]; congr 1; omega

lemma ticksAux_spec : ∀ r j X, ticksAux r j X = true → ∀ i < r, bit0Const (Wp i X) (decide (2 ≤ j + i)) = true := by
  intro r
  induction r with
  | zero => intro j X _ i hi; omega
  | succ r ih =>
    intro j X h i hi
    simp only [ticksAux, Bool.and_eq_true] at h
    rcases i with _ | i
    · simpa [Wp] using h.1
    · have := ih (j + 1) (img 0 X) h.2 i (by omega)
      rw [Wp_succ']; simpa [show j + 1 + i = j + (i + 1) by ring] using this

lemma bit0Const_spec (S : ℕ) (b : Bool) (h : bit0Const S b = true) (s : ℕ) (hs : s < 256) (hS : S.testBit s = true) :
    s.testBit 0 = b := by
  simp only [bit0Const, List.all_eq_true, List.mem_range] at h
  have := h s hs
  rw [hS, Bool.not_true, Bool.false_or, beq_iff_eq] at this
  exact this

/-! ## The actual window -/

def enc (f : ℕ → Bool) : ℕ → ℕ
  | 0 => 0
  | k + 1 => Nat.bit (f 0) (enc (fun j => f (j + 1)) k)

lemma enc_lt (f : ℕ → Bool) (k : ℕ) : enc f k < 2 ^ k := by
  induction k generalizing f with
  | zero => simp [enc]
  | succ k ih =>
    have := ih (fun j => f (j + 1))
    simp only [enc]
    cases f 0 <;> simp [Nat.bit, pow_succ] <;> omega

lemma enc_testBit (f : ℕ → Bool) (k j : ℕ) : (enc f k).testBit j = (decide (j < k) && f j) := by
  induction k generalizing f j with
  | zero => simp [enc]
  | succ k ih =>
    rcases j with _ | j
    · simp [enc]
    · simp only [enc, Nat.testBit_bit_succ, ih]
      simp

/-- The eight cells right of column `c` at time `t`, as a number below 256. -/
def win (x0 : ℤ → Bool) (c : ℤ) (t : ℕ) : ℕ := enc (fun j => evol x0 t (c + 1 + j)) 8

lemma win_lt (x0 : ℤ → Bool) (c : ℤ) (t : ℕ) : win x0 c t < 256 := enc_lt _ 8

lemma win_bit (x0 : ℤ → Bool) (c : ℤ) (t j : ℕ) (hj : j < 8) : (win x0 c t).testBit j = evol x0 t (c + 1 + j) := by
  simp [win, enc_testBit, hj]

/-- The encoded eight cells follow rule 30 exactly. -/
lemma win_step (x0 : ℤ → Bool) (c : ℤ) (t : ℕ) :
    win x0 c (t + 1) = stp (evol x0 t c).toNat (win x0 c t) (evol x0 t (c + 9)).toNat := by
  apply Nat.eq_of_testBit_eq
  intro j
  by_cases hj : j < 8
  · rw [win_bit x0 c (t + 1) j hj, stp_bits _ (win_lt x0 c t) _ _ j hj]
    show xor (evol x0 t (c + 1 + j - 1)) (evol x0 t (c + 1 + j) || evol x0 t (c + 1 + j + 1)) = _
    rw [win_bit x0 c t j hj]
    congr 1
    · split_ifs with h0
      · subst h0; congr 1; ring
      · rw [win_bit x0 c t (j - 1) (by omega)]; congr 1; push_cast [show 1 ≤ j by omega]; ring
    · congr 1
      split_ifs with h7
      · subst h7; congr 1; ring
      · rw [win_bit x0 c t (j + 1) (by omega)]; congr 1; push_cast; ring
  · have h256 : 256 ≤ 2 ^ j := by
      calc 256 = 2 ^ 8 := by norm_num
        _ ≤ 2 ^ j := Nat.pow_le_pow_right (by norm_num) (by omega)
    rw [Nat.testBit_eq_false_of_lt (lt_of_lt_of_le (win_lt x0 c (t + 1)) h256),
      Nat.testBit_eq_false_of_lt (lt_of_lt_of_le (stp_lt _ _ _) h256)]

lemma step_mem (x0 : ℤ → Bool) (c : ℤ) (t : ℕ) (S : ℕ) (hS : S.testBit (win x0 c t) = true) :
    (img (evol x0 t c).toNat S).testBit (win x0 c (t + 1)) = true := by
  rw [win_step]
  exact img_mem _ _ _ _ (win_lt x0 c t) (Bool.toNat_le _) hS

lemma Wp_mem (x0 : ℤ → Bool) (c : ℤ) : ∀ i t X, X.testBit (win x0 c t) = true →
    (∀ k < i, evol x0 (t + k) c = false) → (Wp i X).testBit (win x0 c (t + i)) = true := by
  intro i
  induction i with
  | zero => intro t X h _; simpa [Wp] using h
  | succ i ih =>
    intro t X h hw
    have := step_mem x0 c (t + i) (Wp i X) (ih t X h (fun k hk => hw k (by omega)))
    rw [hw i (by omega)] at this
    simpa [Wp, show t + (i + 1) = t + i + 1 by ring] using this

/-! ## Assembly -/

/-- Column `c` reads `1 0^q` from time `a`, the `1` first. Any phase of an eventually periodic column with
that word has such an `a`. -/
def Reads (x0 : ℤ → Bool) (c : ℤ) (q a : ℕ) : Prop :=
  ∀ n : ℕ, evol x0 (a + n * (q + 1)) c = true ∧ ∀ k, 1 ≤ k → k ≤ q → evol x0 (a + n * (q + 1) + k) c = false

/-- The determination package for a word length `q`. -/
def Det (q : ℕ) : Prop :=
  ∃ S, (∀ n, 3 ≤ n → reach q n = S) ∧ bit0Const S true = true ∧
    ∀ i < q, bit0Const (Wp i (img 1 S)) (decide (2 ≤ i)) = true

lemma det_small (q : ℕ) (h1 : 10 ≤ q) (h2 : q ≤ 25) : Det q := by
  have hc : checkQ q = true := checks q h1 h2
  simp only [checkQ, Bool.and_eq_true, beq_iff_eq] at hc
  obtain ⟨⟨hfix, hb⟩, ht⟩ := hc
  refine ⟨reach q 3, ?_, hb, ?_⟩
  · intro n hn
    induction n, hn using Nat.le_induction with
    | base => rfl
    | succ n _ ih => show mac q (reach q n) = reach q 3; rw [ih, hfix]
  · intro i hi; simpa using ticksAux_spec q 0 _ ht i hi

lemma det_large (q : ℕ) (hq : 26 ≤ q) : Det q := by
  set q' := 22 + (q - 22) % 4 with hq'
  have hr : repOK q' = true := reps q' (by omega) (by omega)
  have hc' : checkQ q' = true := checks q' (by omega) (by omega)
  simp only [repOK, Bool.and_eq_true, List.all_eq_true, List.mem_range, beq_iff_eq] at hr
  obtain ⟨hW, ht⟩ := hr
  simp only [checkQ, Bool.and_eq_true, beq_iff_eq] at hc'
  obtain ⟨⟨hfix, hb⟩, _⟩ := hc'
  have hmac : ∀ n < 4, mac q (reach q' n) = mac q' (reach q' n) := by
    intro n hn
    unfold mac
    rw [Wp_period _ (hW n hn) q (by omega), show 22 + (q - 22) % 4 = q' from rfl]
  have heq : ∀ n ≤ 3, reach q n = reach q' n := by
    intro n hn
    induction n with
    | zero => rfl
    | succ n ih => show mac q (reach q n) = mac q' (reach q' n); rw [ih (by omega), hmac n (by omega)]
  refine ⟨reach q' 3, ?_, hb, ?_⟩
  · intro n hn
    induction n, hn using Nat.le_induction with
    | base => exact heq 3 le_rfl
    | succ n _ ih => show mac q (reach q n) = reach q' 3; rw [ih, hmac 3 (by norm_num), hfix]
  · intro i hi
    have hts := ticksAux_spec 26 0 _ ht
    by_cases h26 : i < 26
    · simpa using hts i h26
    · rw [Wp_period _ (hW 3 (by norm_num)) i (by omega)]
      have := hts (22 + (i - 22) % 4) (by omega)
      simpa [show 2 ≤ i by omega, show 2 ≤ 22 + (i - 22) % 4 by omega] using this

lemma det (q : ℕ) (hq : 10 ≤ q) : Det q := by
  by_cases h : q ≤ 25
  · exact det_small q hq h
  · exact det_large q (by omega)

/-- With the column reading `1 0^q` from `a`, the window lies in `reach q n` at each black tick. -/
lemma orbit_mem (x0 : ℤ → Bool) (c : ℤ) (q a : ℕ) (hr : Reads x0 c q a) :
    ∀ n, (reach q n).testBit (win x0 c (a + n * (q + 1))) = true := by
  intro n
  induction n with
  | zero =>
    show (2 ^ 256 - 1).testBit _ = true
    rw [Nat.testBit_two_pow_sub_one]; simpa using win_lt x0 c (a + 0 * (q + 1))
  | succ n ih =>
    have h1 := step_mem x0 c (a + n * (q + 1)) _ ih
    rw [(hr n).1] at h1
    have h2 := Wp_mem x0 c q (a + n * (q + 1) + 1) _ h1 (fun k hk => by
      have := (hr n).2 (k + 1) (by omega) (by omega)
      rwa [show a + n * (q + 1) + (k + 1) = a + n * (q + 1) + 1 + k by ring] at this)
    show (mac q (reach q n)).testBit _ = true
    unfold mac
    rwa [show a + n * (q + 1) + 1 + q = a + (n + 1) * (q + 1) by ring] at h2

/-- Column `c + 1` at time `a + n (q + 1) + i`, for `n ≥ 3` and `i ≤ q`, is `1 0 0 1 1 …` by position. -/
lemma col1 (x0 : ℤ → Bool) (c : ℤ) (q a : ℕ) (hq : 10 ≤ q) (hr : Reads x0 c q a) (n i : ℕ) (hn : 3 ≤ n)
    (hi : i ≤ q) : evol x0 (a + n * (q + 1) + i) (c + 1) = (i == 0 || decide (3 ≤ i)) := by
  obtain ⟨S, hS, hb, ht⟩ := det q hq
  have hm := orbit_mem x0 c q a hr n
  rw [hS n hn] at hm
  rcases i with _ | i
  · have := bit0Const_spec S true hb _ (win_lt x0 c _) hm
    rw [win_bit x0 c _ 0 (by norm_num)] at this
    simpa using this
  · have h1 := step_mem x0 c (a + n * (q + 1)) S hm
    rw [(hr n).1] at h1
    have h2 := Wp_mem x0 c i (a + n * (q + 1) + 1) _ h1 (fun k hk => by
      have := (hr n).2 (k + 1) (by omega) (by omega)
      rwa [show a + n * (q + 1) + (k + 1) = a + n * (q + 1) + 1 + k by ring] at this)
    have := bit0Const_spec _ _ (ht i (by omega)) _ (win_lt x0 c _) h2
    rw [win_bit x0 c _ 0 (by norm_num)] at this
    simp only [Nat.cast_zero, add_zero] at this
    rw [show a + n * (q + 1) + (i + 1) = a + n * (q + 1) + 1 + i by ring, this]
    by_cases h : 2 ≤ i <;> simp [h]

/-- The core: a leftmost black cell at or left of column `c`. -/
theorem core (x0 : ℤ → Bool) (c : ℤ) (L : ℕ) (hc : x0 (c - L) = true) (hl : ∀ j < c - L, x0 j = false)
    (q a : ℕ) (hq : 10 ≤ q) (hr : Reads x0 c q a) : False := by
  have split : ∀ t, a ≤ t → t = a + ((t - a) / (q + 1)) * (q + 1) + (t - a) % (q + 1) := by
    intro t ht
    have := Nat.div_add_mod (t - a) (q + 1)
    rw [mul_comm] at this; omega
  have hmod : ∀ t, (t - a) % (q + 1) ≤ q := fun t => Nat.lt_succ_iff.mp (Nat.mod_lt _ (by omega))
  apply no_two_periodic x0 c L hc hl (q + 1) (a + 3 * (q + 1)) (by omega)
  · intro t ht
    have e1 := split t (by omega)
    have e2 : t + (q + 1) = a + ((t - a) / (q + 1) + 1) * (q + 1) + (t - a) % (q + 1) := by
      rw [add_mul, one_mul]; omega
    have col0 : ∀ n i, i ≤ q → evol x0 (a + n * (q + 1) + i) c = (i == 0) := by
      intro n i hi
      rcases i with _ | i
      · simpa using (hr n).1
      · simpa using (hr n).2 (i + 1) (by omega) hi
    rw [e1, col0 _ _ (hmod t)]
    rw [show a + (t - a) / (q + 1) * (q + 1) + (t - a) % (q + 1) + (q + 1) =
      a + ((t - a) / (q + 1) + 1) * (q + 1) + (t - a) % (q + 1) by ring, col0 _ _ (hmod t)]
  · intro t ht
    have e1 := split t (by omega)
    have hn : 3 ≤ (t - a) / (q + 1) := by
      rw [Nat.le_div_iff_mul_le (by omega)]; omega
    rw [e1, col1 x0 c q a hq hr _ _ hn (hmod t)]
    rw [show a + (t - a) / (q + 1) * (q + 1) + (t - a) % (q + 1) + (q + 1) =
      a + ((t - a) / (q + 1) + 1) * (q + 1) + (t - a) % (q + 1) by ring, col1 x0 c q a hq hr _ _ (by omega) (hmod t)]

/-- **The white end, for every configuration with a leftmost black cell.** No column reads `1 0^q`
from some time on, for any `q ≥ 10`. -/
theorem white_end (x0 : ℤ → Bool) (e : ℤ) (he : x0 e = true) (hl : ∀ j < e, x0 j = false) (c : ℤ) (q a : ℕ)
    (hq : 10 ≤ q) (hr : Reads x0 c q a) : False := by
  by_cases hec : e ≤ c
  · exact core x0 c (c - e).toNat (by rwa [show c - ((c - e).toNat : ℤ) = e by omega])
      (by rw [show c - ((c - e).toNat : ℤ) = e by omega]; exact hl) q a hq hr
  · -- rebase time: after k = e - c steps the leftmost black cell is at c
    set k : ℕ := (e - c).toNat with hk
    have E := edge x0 e he hl k
    have hkc : e - (k : ℤ) = c := by rw [hk]; omega
    rw [hkc] at E
    apply core (evol x0 k) c 0 (by simpa using E.1) (by simpa using E.2) q (a + k * (q + 1) - k) hq
    intro n
    have ha : k + (a + k * (q + 1) - k + n * (q + 1)) = a + (n + k) * (q + 1) := by
      have : k ≤ k * (q + 1) := Nat.le_mul_of_pos_right k (by omega)
      rw [add_mul]; omega
    refine ⟨?_, fun j h1 h2 => ?_⟩
    · rw [evol_add, ha]; exact (hr (n + k)).1
    · rw [evol_add, show k + (a + k * (q + 1) - k + n * (q + 1) + j) =
        (k + (a + k * (q + 1) - k + n * (q + 1))) + j by ring, ha]
      exact (hr (n + k)).2 j h1 h2

/-- **For a finite nonzero configuration** (a left bound and one black cell; the right side may be infinite). -/
theorem white_end_finite (x0 : ℤ → Bool) (hfin : ∃ M : ℤ, ∀ j < M, x0 j = false) (hnz : ∃ j, x0 j = true)
    (c : ℤ) (q : ℕ) (hq : 10 ≤ q) : ¬ ∃ a, Reads x0 c q a := by
  rintro ⟨a, hr⟩
  obtain ⟨M, hM⟩ := hfin
  obtain ⟨e, he, hmin⟩ := Int.exists_least_of_bdd (P := fun j => x0 j = true)
    ⟨M, fun z hz => by by_contra h; push Not at h; rw [hM z h] at hz; exact absurd hz (by decide)⟩ hnz
  exact white_end x0 e he (fun j hj => by
    by_contra h
    have := hmin j (by simpa using h)
    omega) c q a hq hr

/-! ## The bridge to the kit's statements: the single-seed pattern and `EventuallyWord` -/

lemma seed_leftmost : seed 0 = true ∧ ∀ p : ℤ, p < 0 → seed p = false := by
  refine ⟨by simp [seed], fun p hp => ?_⟩
  simp only [seed, decide_eq_false_iff_not]; omega

lemma getD_replicate_false : ∀ (q k : ℕ), (List.replicate q false).getD k false = false
  | 0, _ => rfl
  | _ + 1, 0 => rfl
  | q + 1, k + 1 => by
    rw [List.replicate_succ, List.getD_cons_succ]
    exact getD_replicate_false q k

lemma getD_word (q k : ℕ) : (true :: List.replicate q false).getD k false = decide (k = 0) := by
  cases k with
  | zero => rfl
  | succ k => rw [List.getD_cons_succ, getD_replicate_false]; simp

/-- An eventual word `1 0^q` of the center column is a `Reads` of the seed's evolution at column `0`. -/
lemma reads_of_eventuallyWord (q : ℕ) (h : EventuallyWord (true :: List.replicate q false)) :
    ∃ a, Reads seed 0 q a := by
  obtain ⟨T, hT⟩ := h
  have hlen : (true :: List.replicate q false).length = q + 1 := by simp
  refine ⟨T, fun n => ⟨?_, fun k hk1 hk2 => ?_⟩⟩
  · rw [evol_seed, hT _ (by omega), hlen, show T + n * (q + 1) - T = n * (q + 1) by omega,
      Nat.mul_mod_left, getD_word]
    rfl
  · rw [evol_seed, hT _ (by omega), hlen, show T + n * (q + 1) + k - T = k + n * (q + 1) by omega,
      Nat.add_mul_mod_self_right, Nat.mod_eq_of_lt (by omega), getD_word]
    simp only [decide_eq_false_iff_not]; omega

/-- **Headline.** For every `q ≥ 10`, the center column of the single-seed pattern is not eventually the
repeating word `1 0^q`, whatever the transient. -/
theorem not_eventuallyWord_white_end (q : ℕ) (hq : 10 ≤ q) :
    ¬ EventuallyWord (true :: List.replicate q false) := by
  intro h
  obtain ⟨a, hr⟩ := reads_of_eventuallyWord q h
  exact white_end seed 0 seed_leftmost.1 seed_leftmost.2 0 q a hq hr

/-- Every column of the single-seed pattern, in the `Reads` form. -/
theorem white_end_seed (c : ℤ) (q a : ℕ) (hq : 10 ≤ q) : ¬ Reads seed c q a :=
  fun hr => white_end seed 0 seed_leftmost.1 seed_leftmost.2 c q a hq hr

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The headline theorem, as Lean prints it. For every `q ≥ 10`, the center column is not eventually the word `1 0^q`:

```wl
opens = {"Ruliology.CellularAutomata.Rule30StripCertificates", "Ruliology.CellularAutomata.Rule30Realization", "Rule30Submission"};
thm = rule30Submission["Rule30Submission.not_eventuallyWord_white_end"];
thm["TypeForm", "Open" -> opens]
```

Its axioms are the three standard ones and nothing else:

```wl
thm["Axioms"]
```

The general statement, for every column of every configuration with a leftmost black cell. `Reads x0 c q a` says that column `c` of the evolution of `x0` reads `1 0^q` from time `a`, the `1` first:

```wl
rule30Submission["Rule30Submission.white_end"]["TypeForm", "Open" -> opens]
```

The same for finite nonzero configurations (a left bound and one black cell; the right side may be infinite), and for every column of the single seed:

```wl
{rule30Submission["Rule30Submission.white_end_finite"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.white_end_seed"]["TypeForm", "Open" -> opens]}
```

Jen's theorem with a clock, the lemma that finishes the argument:

```wl
rule30Submission["Rule30Submission.theorem_A"]["TypeForm", "Open" -> opens]
```

The control: the finite check fails at `q = 9`, so the checks are not vacuous:

```wl
rule30Submission["Rule30Submission.control_q9"]["TypeForm", "Open" -> opens]
```

The proof's structure, one level down from the headline:

```wl
thm["CallGraph", "Depth" -> 1]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state, after which every fresh display costs a minute:

```wl
thm["KernelCheck"]
```

## What is not proved

- Nothing for `q ≤ 9`. The method does not determine column `c + 1` there (the control above), and `q = 1` is the word `10`, the period-2 case of Problem 1, which stays open.
- Nothing about any other word. The same route excludes further specific words by the same finite checks; that is a separate matter.
- This is a partial result, one infinite family of words removed from Problem 1. It does not touch Problems 2 and 3.

## Provenance

The result is entry 40 of the Wolfram · Collatz · Mahler record, an open research record kept on GitHub by Gareth Herbert with Claude and GPT. Local (Claude) found the route and machine-checked it in Lean on 2026-10-09; Cloud (Claude) and GPT read and replayed it independently with separate implementations; Cloud restated it on the kit's definitions and added the bridge to `EventuallyWord` on 2026-10-22. The finite computations above were reproduced in Python before this essay was written. The mechanism is Jen's, as the kit's strip certificates use it; the kit's `window_jen` is the same clocked form of Jen's theorem, stated with the or-column.

## References

[1] E. Jen, *Global properties of cellular automata*, Journal of Statistical Physics 43 (1986) 219–242.

[2] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[3] Wolfram Institute, [*Rule30PrizeKit*](https://github.com/WolframInstitute/Rule30PrizeKit), the reference Lean environment, commit cc1e0e0, 2026.

[4] The Wolfram · Collatz · Mahler record, [github.com/ghywel/placego](https://github.com/ghywel/placego): PROOFS.md entry 40 and `tests/probes/lean/WhiteEnd.lean`, 2026.
