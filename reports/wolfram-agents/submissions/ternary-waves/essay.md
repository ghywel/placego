---
Template: ComputationalEssay
Name: Free Ternary Codes of Rule 30 Travelling Waves: Three Freely Joining Tiles at Moving Period 12, and Three at Moving Period 15
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-10
Description: Core Lean. Three freely joining 34-cell tiles at moving period 12 and three 31-cell tiles at moving period 15 give free ternary codes of rule 30 travelling waves, by one generic kernel-checked development. Nothing is claimed about other periods.
Abstract: In core Lean 4.35.0 we extend the kit's travelling-wave codes of rule 30 from two tiles to three, and from moving period 12 to moving period 15. In the frame that moves one cell right per step, a row is a travelling return of period P when P updates of rule 30 bring it back moved P cells to the right. The kit shows that two 34-cell tiles at period 12 join freely, so that every bi-infinite binary code gives such a row. We give three 34-cell tiles at period 12, the kit's two and one more, and three 31-cell tiles at period 15. In each family every pair of tiles joins at every offset and phase: 3672 and 4185 local rule 30 identities, checked by the Lean kernel. So every bi-infinite ternary code gives a row of exact minimal moving return 12, or 15, and two cells of each block read the code back. Hence there are 3 to the power k distinct marked rings of size 34k, or 31k, and at least 3 to the power floor(n/34), or floor(n/31), distinct words of length n in such rows: at least log2(3)/34 and log2(3)/31 bits per cell. The development is generic in the tile length, the period and the profile data, and is proved once. Nothing is claimed about other periods, about whether 15 is the next period with positive spatial entropy, or about the exact spatial entropy at either period.
Keywords: [rule 30, Rule 30 Prize, travelling waves, moving frame, spatial entropy, tiles, ternary code, kernel certificate, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)"]
---

## 1. The statement

Read rule 30 in the frame that moves one cell right per step, `Phi x i = x i xor (x (i+1) or x (i+2))` (the kit's `Rule30RingOrbits`). A row `x : Int → Bool` is a *travelling return* of period `P` when `orbit x P = x`. By the kit's `orbit_eq_iff`, this means that `P` ordinary updates of rule 30 bring the row back, moved `P` cells to the right.

The kit's `Rule30MovingWaves` shows that two 34-cell tiles at period 12 can be joined freely. Every bi-infinite binary code gives a travelling return of exact minimal period 12, so the spatial language at that period grows exponentially, and 12 is the least such period. This module gives a larger alphabet at period 12 and the same construction at period 15:
- **Period 12:** three 34-cell tiles (`tiles12`). Tiles 0 and 2 are the kit's two; tile 1 is new.
- **Period 15:** three 31-cell tiles (`tiles15`).

For each family:
- `free_ternary_period_twelve`, `free_ternary_period_fifteen`: an injective map from all bi-infinite ternary codes `Int → Fin 3` to rows of exact minimal moving return `P`.
- `ternary_marked_rings_twelve`, `ternary_marked_rings_fifteen`: for every `k > 0`, an injective family of `3^k` marked rings of size `L k`, each of exact minimal moving return `P`.
- `ternary_words_twelve`, `ternary_words_fifteen`: an injective map from ternary words of length `n / L` to binary words of length `n` that occur in rows with `orbit x P = x`.
- `ternary_wave_twelve`, `ternary_wave_fifteen`: the physical form, `evol (field code 0) P (i + P) = field code 0 i`.

So at least `3^⌊n/34⌋` words of length `n` occur in rows of moving period 12, and at least `3^⌊n/31⌋` in rows of moving period 15. That is at least `log₂3 / 34 ≈ 0.047` and `log₂3 / 31 ≈ 0.051` bits per cell, against the kit's `1/34 ≈ 0.029` at period 12.

## 2. Tiles and seams

A family `Tiles` has a length `L`, a period `P` and three tiles. Each tile lists, for each offset `r < L`, a time profile: bit `t` of it is the cell at offset `r` and phase `t`, read modulo `P`. The field of a code puts at site `i` the cell at offset `i mod L` of tile `code (i div L)`.

The moving frame updates a cell from itself and its two right neighbours. So the field obeys the rule everywhere as soon as every pair of tiles `a b` obeys it at every offset and phase across their seam (`Certificate`). The kernel checks this by `decide +kernel`:
- `tile_certificate12`: 9 seams × 34 offsets × 12 phases = 3672 identities;
- `tile_certificate15`: 9 seams × 31 offsets × 15 phases = 4185 identities.

Then `phi_field` and `orbit_field` identify the field at phase `t` with the `t`-th iterate of its phase-0 row, and `period` closes the loop at `P`. These are proved once, for every `L`, `P` and profile data, and instantiated twice.

## 3. Exact return and decoding

- `exact_period`: if a row returned at some `0 < d < P`, then the tile `code 0` would repeat its phase-0 row at phase `d`. The kernel checks that no tile of either family does that (`Exact`), so the least moving return is exactly `P` for every code.
- `decode12`, `decode15`: two phase-0 cells of each block read the code back. At period 12 the cells at offsets 20 and 23 are `(0,1)`, `(0,0)`, `(1,0)` for tiles 0, 1, 2. At period 15 the cells at offsets 6 and 23 are `(1,1)`, `(0,0)`, `(1,0)`. So the map from codes to rows is injective, and periodic codes give distinct marked rings.

## 4. Scope

These are explicit lower bounds on the travelling-wave language at two periods. They say nothing about other periods. In particular they say nothing about 13 and 14, or about whether 15 is the next period with positive spatial entropy. They do not determine the exact spatial entropy at period 12 or 15, and no statement about stationary periods. The rings counted are marked rings, not rotation classes. The single seed is not addressed.

## 5. Worked numbers

The cell below checks, independently of the Lean module:
- the seam identities of both families, in the moving frame;
- every ring made of one to three tiles, 39 per family, evolved by Wolfram Language's own `CellularAutomaton[30, …]` on a cycle. Each must come back moved `P` cells right after `P` ticks, and at no earlier tick `d` moved `d` cells;
- the decoder cells.

```wl
p12 = {{2868, 3242, 2734, 2769, 1321, 1721, 2469, 1381, 1367, 2772, 3372, 2738, 2986, 1131, 2644, 3674, 2406, 2389, 1493, 1323, 2868, 3242, 2734, 2769, 1321, 1721, 2469, 1381, 1367, 3028, 3116, 2610, 2602, 1323}, {2868, 3242, 2734, 2769, 1321, 1721, 2469, 1381, 1367, 2772, 3372, 2738, 2986, 1131, 2644, 3674, 2406, 2389, 1493, 1327, 2864, 3240, 2728, 2772, 3372, 2738, 2986, 1131, 2644, 3674, 2406, 2389, 1493, 1323}, {2868, 3242, 2734, 2769, 1321, 1721, 2469, 1381, 1367, 3028, 3116, 2610, 2602, 1323, 2868, 3242, 2734, 2769, 1321, 1721, 2469, 1381, 1367, 2772, 3372, 2738, 2986, 1131, 2644, 3674, 2406, 2389, 1493, 1323}};
p15 = {{5461, 23930, 21125, 13126, 10949, 10917, 21927, 10836, 13684, 11082, 11470, 12969, 10921, 27605, 5165, 6707, 22058, 21802, 11581, 21154, 11171, 23122, 26226, 5451, 21834, 24238, 8553, 20889, 12629, 10581, 27050}, {5461, 23930, 21125, 13126, 10949, 10917, 21926, 10837, 30069, 2890, 3277, 2731, 19114, 20310, 10409, 26837, 5293, 7347, 21194, 21162, 11183, 23120, 26216, 21848, 21844, 31412, 17738, 18094, 9577, 26009, 5717}, {5461, 23930, 21125, 13126, 10949, 10917, 21927, 10836, 13684, 11082, 11470, 12969, 10921, 27605, 5165, 6707, 22058, 21802, 11573, 21162, 11183, 23120, 26216, 21848, 21844, 31412, 17738, 18094, 9577, 26009, 5717}};
bit[prof_, a_, r_, t_, per_] := BitGet[prof[[a + 1, r + 1]], Mod[t, per]];
seamsOK[prof_, len_, per_] := Count[Flatten[Table[
     With[{row = Function[{r, t}, If[r < len, bit[prof, a, r, t, per], bit[prof, b, r - len, t, per]]]},
      bit[prof, a, r, t + 1, per] == BitXor[row[r, t], BitOr[row[r + 1, t], row[r + 2, t]]]],
     {a, 0, 2}, {b, 0, 2}, {r, 0, len - 1}, {t, 0, per - 1}]], True];
ringsOK[prof_, len_, per_] := Count[Flatten[Table[
     Module[{x = Flatten[Table[bit[prof, w[[q]], r, 0, per], {q, Length[w]}, {r, 0, len - 1}]], ev},
      ev = CellularAutomaton[30, x, per];
      AllTrue[Range[per - 1], RotateRight[x, #] =!= ev[[# + 1]] &] && RotateRight[x, per] === ev[[per + 1]]],
     {k, 1, 3}, {w, Tuples[{0, 1, 2}, k]}], 1], True];
decoders[prof_, o1_, o2_, per_] := Table[{bit[prof, a, o1, 0, per], bit[prof, a, o2, 0, per]}, {a, 0, 2}];
{seamsOK[p12, 34, 12], seamsOK[p15, 31, 15], ringsOK[p12, 34, 12], ringsOK[p15, 31, 15], decoders[p12, 20, 23, 12], decoders[p15, 6, 23, 15]}
```

## 6. Prior art and scope

- **The method and two of the tiles** are those of the kit's `Rule30MovingWaves` (Emerson Villafuerte, portal entry R30-20261108-9933fc). Tiles 0 and 2 at period 12 are its `zeroProfiles` and `oneProfiles`, restated here because the verifier's kit does not yet contain that module.
- **The frame** is the kit's `Rule30RingOrbits`.
- **What is new:** the third freely joining 34-cell tile at period 12; the three 31-cell tiles at period 15; and the generic development, which certifies any such family by one finite check.
- **History.** GPT found the third period-12 tile in its analysis of the period-12 return state. Cloud found the period-15 tiles by a search of the profile graph. GPT checked both literal families independently, and a Local sub-agent formalized them under Local's direction. The profile-graph framework is the swarm's LN-12; Cloud carried the period-12 return construction in its [period-12 read](https://github.com/ghywel/placego/blob/main/reports/CLOUD-PERIOD12-CARRY-20261110.md), and the period-15 lists are in its [tile report](https://github.com/ghywel/placego/blob/main/reports/CLOUD-PERIOD15-TILES-20261110.md).

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30RingOrbits`.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30RingOrbits
/-!
# Rule 30: free ternary codes of travelling waves at moving periods 12 and 15

Read Rule 30 in the frame that moves one cell right per step (`Rule30RingOrbits.Phi`). A row
`x : Int → Bool` is a travelling return of period `P` when `orbit x P = x`. By
`Rule30RingOrbits.orbit_eq_iff` this says `evol x P (i + P) = x i`: after `P` updates of Rule 30
the row is back, moved `P` cells to the right.

A family of three tiles of length `L` for the period `P` (`Tiles`) lists, for each tile and each
offset `r < L`, a time profile: bit `t` of it is the cell at phase `t`, read modulo `P`. The field
of a code `code : Int → Fin 3` puts at site `i` the cell at offset `(i % L).toNat` of tile
`code (i / L)`, offsets in increasing spatial order. If every seam `a b` obeys the local rule at
every offset and phase (`Certificate`), the field of every bi-infinite ternary code is a
travelling wave of period `P`. If no tile repeats its phase-0 row at a phase `0 < d < P`
(`Exact`), the return is exactly `P`. Two cells at fixed offsets read the tile back (`Decoder`).

The development is generic in `L`, `P` and the profile data, and is proved once:
`phi_field`, `orbit_field`, `period`, `wave`, `exact_period`, `decode`, `code_injective`,
`ring_family`, `words` and `free_ternary`. It is instantiated twice, each instance checked by the
Lean kernel with `decide +kernel`:

* **Period 12, tiles of length 34** (`tiles12`). `tile_certificate12`: all 9 seams, 34 offsets
  and 12 phases, 3672 local identities. `decode12`: the phase-0 cells at offsets 20 and 23 are
  (0,1), (0,0), (1,0) for tiles 0, 1, 2.
* **Period 15, tiles of length 31** (`tiles15`). `tile_certificate15`: all 9 seams, 31 offsets
  and 15 phases, 4185 local identities. `decode15`: the phase-0 cells at offsets 6 and 23 are
  (1,1), (0,0), (1,0) for tiles 0, 1, 2.

For each period `P` with tile length `L`:

* `free_ternary_period_twelve`, `free_ternary_period_fifteen`: an injective map from all
  bi-infinite ternary codes to rows of exact minimal moving return `P`.
* `ternary_marked_rings_twelve`, `ternary_marked_rings_fifteen`: for every `k > 0`, an injective
  family of `3^k` marked rings of size `L k`, each of exact minimal moving return `P`.
* `ternary_words_twelve`, `ternary_words_fifteen`: an injective map from ternary words of length
  `n / L` to binary words of length `n` that occur in rows with `orbit x P = x`.
* `ternary_wave_twelve`, `ternary_wave_fifteen`: the physical statement
  `evol (field code 0) P (i + P) = field code 0 i`.

The word theorems are explicit language lower bounds: at least `3^(n / 34)` distinct words of
length `n` occur in rows of moving period 12, and at least `3^(n / 31)` in rows of moving period
15, that is at least `log2(3)/34` and `log2(3)/31` bits per cell. Nothing is claimed here about
other periods.

Tiles 0 and 2 at period 12 are the two tiles of `Rule30MovingWaves` (Emerson Villafuerte, portal
entry R30-20261108-9933fc): tile 0 is its `TravellingCode.zeroProfiles` and tile 2 its
`TravellingCode.oneProfiles`. The method, profile lists with kernel-checked seams and a block
decoder, is that module's. This module restates the lists rather than importing it.
-/

namespace Rule30Submission

open Ruliology.CellularAutomata

open Rule30RingOrbits (Phi orbit Per orbit_eq_iff)

/-! ### Three tiles and their field -/

/-- Three tiles of length `L` for the moving period `P`. Entry `r` of tile `a` in `profiles` is
the time profile of the cell at offset `r`: bit `t` of it is that cell at phase `t`. -/
structure Tiles where
  /-- The tile length. -/
  L : Nat
  /-- The moving period. -/
  P : Nat
  /-- The three tiles, in order, each a list of `L` time profiles. -/
  profiles : List (List Nat)

/-- The cell of tile `a` at offset `r` and phase `t`. -/
def profile (T : Tiles) (a : Fin 3) (r t : Nat) : Bool :=
  ((T.profiles.getD a.val []).getD r 0).testBit (t % T.P)

/-- Tile `a` followed by tile `b`: offsets `r < L` read `a`, the next ones read `b`. -/
def joined (T : Tiles) (a b : Fin 3) (r t : Nat) : Bool :=
  if r < T.L then profile T a r t else profile T b (r - T.L) t

/-- Every seam `a b`, offset and phase obeys the local rule of the moving frame. -/
def Certificate (T : Tiles) : Prop :=
  ∀ a b : Fin 3, ∀ r : Fin T.L, ∀ t : Fin T.P,
    profile T a r.val (t.val + 1) =
      xor (joined T a b r.val t.val)
        (joined T a b (r.val + 1) t.val || joined T a b (r.val + 2) t.val)

/-- No tile repeats its phase-0 row at a phase `0 < d < P`. -/
def Exact (T : Tiles) : Prop :=
  ∀ a : Fin 3, ∀ d : Fin T.P, d.val ≠ 0 →
    ∃ r : Fin T.L, profile T a r.val d.val ≠ profile T a r.val 0

/-- What the kernel checks for a concrete family. -/
structure Valid (T : Tiles) : Prop where
  two_le : 2 ≤ T.L
  pos : 0 < T.P
  cert : Certificate T
  least : Exact T

/-- Two offsets whose phase-0 cells name the tile. -/
structure Decoder (T : Tiles) where
  o1 : Nat
  o2 : Nat
  read : Bool → Bool → Fin 3
  o1_lt : o1 < T.L
  o2_lt : o2 < T.L
  reads : ∀ a : Fin 3, read (profile T a o1 0) (profile T a o2 0) = a

/-- Site `i` at phase `t` is offset `(i % L).toNat` of tile `code (i / L)`. Sites are labelled by
`Int`, so the code is arbitrary in both directions. -/
def field (T : Tiles) (code : Int → Fin 3) (t : Nat) (i : Int) : Bool :=
  profile T (code (i / T.L)) (i % T.L).toNat t

/-! ### Phases -/

theorem profile_mod (T : Tiles) (a : Fin 3) (r t : Nat) :
    profile T a r (t % T.P) = profile T a r t := by
  simp only [profile, Nat.mod_mod]

theorem joined_mod (T : Tiles) (a b : Fin 3) (r t : Nat) :
    joined T a b r (t % T.P) = joined T a b r t := by
  simp only [joined, profile_mod]

theorem profile_succ_mod (T : Tiles) (a : Fin 3) (r t : Nat) :
    profile T a r (t % T.P + 1) = profile T a r (t + 1) := by
  simp only [profile, Nat.mod_add_mod]

theorem profile_add_period (T : Tiles) (a : Fin 3) (r t : Nat) :
    profile T a r (t + T.P) = profile T a r t := by
  simp only [profile, Nat.add_mod_right]

/-! ### Sites -/

/-- Division by a positive tile length, read off an explicit decomposition. -/
theorem site_split {L : Nat} (hL : 0 < L) {i q : Int} {r : Nat} (hr : r < L)
    (h : i = (L : Int) * q + (r : Int)) :
    i / (L : Int) = q ∧ (i % (L : Int)).toNat = r := by
  have hu := (Int.ediv_emod_unique (a := i) (b := (L : Int)) (r := (r : Int)) (q := q)
    (by omega)).mpr ⟨by omega, by omega, by omega⟩
  refine ⟨hu.1, ?_⟩
  rw [hu.2, Int.toNat_natCast]

theorem site_decomp {L : Nat} (hL : 0 < L) (i : Int) :
    i = (L : Int) * (i / (L : Int)) + (((i % (L : Int)).toNat : Nat) : Int) ∧
      (i % (L : Int)).toNat < L := by
  have h0 : 0 ≤ i % (L : Int) := Int.emod_nonneg i (by omega)
  have h1 : i % (L : Int) < L := Int.emod_lt_of_pos i (by omega)
  have h2 := Int.emod_add_mul_ediv i (L : Int)
  omega

theorem field_local (T : Tiles) (hL : 2 ≤ T.L) (code : Int → Fin 3) (t : Nat) (i : Int)
    (d : Nat) (hd : d ≤ 2) :
    field T code t (i + (d : Int)) =
      joined T (code (i / T.L)) (code (i / T.L + 1)) ((i % T.L).toNat + d) t := by
  obtain ⟨hi, hm⟩ := site_decomp (L := T.L) (by omega) i
  by_cases h : (i % T.L).toNat + d < T.L
  · obtain ⟨hq, hr⟩ := site_split (L := T.L) (i := i + (d : Int)) (q := i / T.L)
      (r := (i % T.L).toNat + d) (by omega) h (by omega)
    simp only [field, hq, hr, joined, ite_eq_left h]
  · have hmul : (T.L : Int) * (i / T.L + 1) = (T.L : Int) * (i / T.L) + (T.L : Int) := by
      rw [Int.mul_add, Int.mul_one]
    obtain ⟨hq, hr⟩ := site_split (L := T.L) (i := i + (d : Int)) (q := i / T.L + 1)
      (r := (i % T.L).toNat + d - T.L) (by omega) (by omega) (by omega)
    simp only [field, hq, hr, joined, ite_eq_right h]

theorem field_block (T : Tiles) (code : Int → Fin 3) (t : Nat) (q : Int) {o : Nat}
    (ho : o < T.L) :
    field T code t ((T.L : Int) * q + (o : Int)) = profile T (code q) o t := by
  obtain ⟨hq, hr⟩ := site_split (L := T.L) (i := (T.L : Int) * q + (o : Int)) (q := q) (r := o)
    (by omega) ho rfl
  simp only [field, hq, hr]

/-! ### The field is a travelling wave -/

theorem phi_field (T : Tiles) (hT : Valid T) (code : Int → Fin 3) (t : Nat) :
    Phi (field T code t) = field T code (t + 1) := by
  funext i
  have hL := hT.two_le
  obtain ⟨_, hm⟩ := site_decomp (L := T.L) (by omega) i
  have hc := hT.cert (code (i / T.L)) (code (i / T.L + 1)) ⟨(i % T.L).toNat, hm⟩
    ⟨t % T.P, Nat.mod_lt t hT.pos⟩
  dsimp only at hc
  simp only [profile_succ_mod, joined_mod] at hc
  have h0 : field T code t i =
      joined T (code (i / T.L)) (code (i / T.L + 1)) (i % T.L).toNat t := by
    simpa using field_local T hL code t i 0 (by decide)
  have h1 : field T code t (i + 1) =
      joined T (code (i / T.L)) (code (i / T.L + 1)) ((i % T.L).toNat + 1) t := by
    simpa using field_local T hL code t i 1 (by decide)
  have h2 : field T code t (i + 2) =
      joined T (code (i / T.L)) (code (i / T.L + 1)) ((i % T.L).toNat + 2) t := by
    simpa using field_local T hL code t i 2 (by decide)
  change xor (field T code t i) (field T code t (i + 1) || field T code t (i + 2)) = _
  rw [h0, h1, h2]
  exact hc.symm

theorem orbit_field (T : Tiles) (hT : Valid T) (code : Int → Fin 3) :
    ∀ t : Nat, orbit (field T code 0) t = field T code t
  | 0 => rfl
  | t + 1 => by rw [orbit, orbit_field T hT code t, phi_field T hT code t]

theorem field_period (T : Tiles) (code : Int → Fin 3) (t : Nat) :
    field T code (t + T.P) = field T code t := by
  funext i
  exact profile_add_period T _ _ t

/-- Every bi-infinite ternary code returns after `P` co-moving steps. -/
theorem period (T : Tiles) (hT : Valid T) (code : Int → Fin 3) :
    orbit (field T code 0) T.P = field T code 0 := by
  have h := field_period T code 0
  rw [Nat.zero_add] at h
  rw [orbit_field T hT code, h]

/-- The physical statement: after `P` updates of Rule 30 the row is back, moved `P` cells right. -/
theorem wave (T : Tiles) (hT : Valid T) (code : Int → Fin 3) (i : Int) :
    Rule30Realization.evol (field T code 0) T.P (i + T.P) = field T code 0 i :=
  (orbit_eq_iff (field T code 0) T.P).mp (period T hT code) i

/-- The return is exactly `P`: no `0 < d < P` returns, since tile `code 0` already moves. -/
theorem exact_period (T : Tiles) (hT : Valid T) (code : Int → Fin 3) :
    orbit (field T code 0) T.P = field T code 0 ∧
      ∀ d : Nat, 0 < d → d < T.P → orbit (field T code 0) d ≠ field T code 0 := by
  refine ⟨period T hT code, ?_⟩
  intro d hd hdP he
  obtain ⟨r, hr⟩ := hT.least (code 0) ⟨d, hdP⟩ (by
    change d ≠ 0
    omega)
  have hh := congrFun he (r.val : Int)
  rw [orbit_field T hT code] at hh
  have hL := hT.two_le
  obtain ⟨hq, hm⟩ := site_split (L := T.L) (i := (r.val : Int)) (q := 0) (r := r.val)
    (by omega) r.isLt (by omega)
  simp only [field, hq, hm] at hh
  exact hr hh

/-! ### Decoding and codes -/

/-- The two decoder cells of block `q` recover `code q`. -/
theorem decode (T : Tiles) (D : Decoder T) (code : Int → Fin 3) (q : Int) :
    D.read (field T code 0 ((T.L : Int) * q + (D.o1 : Int)))
      (field T code 0 ((T.L : Int) * q + (D.o2 : Int))) = code q := by
  rw [field_block T code 0 q D.o1_lt, field_block T code 0 q D.o2_lt]
  exact D.reads (code q)

theorem code_injective (T : Tiles) (D : Decoder T) (a b : Int → Fin 3)
    (h : field T a 0 = field T b 0) : a = b := by
  funext q
  have h1 := congrFun h ((T.L : Int) * q + (D.o1 : Int))
  have h2 := congrFun h ((T.L : Int) * q + (D.o2 : Int))
  calc a q = D.read (field T a 0 ((T.L : Int) * q + (D.o1 : Int)))
        (field T a 0 ((T.L : Int) * q + (D.o2 : Int))) := (decode T D a q).symm
    _ = D.read (field T b 0 ((T.L : Int) * q + (D.o1 : Int)))
        (field T b 0 ((T.L : Int) * q + (D.o2 : Int))) := by rw [h1, h2]
    _ = b q := decode T D b q

/-- A free bi-infinite ternary code, every image of exact minimal moving return `P`. -/
theorem free_ternary (T : Tiles) (hT : Valid T) (D : Decoder T) :
    ∃ E : (Int → Fin 3) → (Int → Bool),
      (∀ a b, E a = E b → a = b) ∧
      ∀ code, orbit (E code) T.P = E code ∧
        (∀ d : Nat, 0 < d → d < T.P → orbit (E code) d ≠ E code) :=
  ⟨fun code => field T code 0, code_injective T D, exact_period T hT⟩

/-! ### Rings -/

/-- The `k`-periodic code with period word `w`. -/
def periodicCode (k : Nat) (hk : 0 < k) (w : Fin k → Fin 3) (q : Int) : Fin 3 :=
  w ⟨(q % (k : Int)).toNat, by
    have h0 : 0 ≤ q % (k : Int) := Int.emod_nonneg _ (by omega)
    have h1 : q % (k : Int) < k := Int.emod_lt_of_pos _ (by omega)
    omega⟩

theorem periodicCode_period (k : Nat) (hk : 0 < k) (w : Fin k → Fin 3) (q : Int) :
    periodicCode k hk w (q + k) = periodicCode k hk w q := by
  simp [periodicCode]

theorem periodicCode_read (k : Nat) (hk : 0 < k) (w : Fin k → Fin 3) (j : Fin k) :
    periodicCode k hk w j.val = w j := by
  have hh : (j.val : Int) % (k : Int) = j.val :=
    Int.emod_eq_of_lt (by omega) (by omega)
  simp only [periodicCode, hh, Int.toNat_natCast]

theorem ring_period (T : Tiles) (hT : Valid T) (k : Nat) (hk : 0 < k) (w : Fin k → Fin 3) :
    Per (T.L * k) (field T (periodicCode k hk w) 0) := by
  intro i
  have hL := hT.two_le
  obtain ⟨hi, hm⟩ := site_decomp (L := T.L) (by omega) i
  have hmul : (T.L : Int) * (i / T.L + (k : Int)) =
      (T.L : Int) * (i / T.L) + ((T.L * k : Nat) : Int) := by
    rw [Int.mul_add, Int.natCast_mul]
  obtain ⟨hq, hr⟩ := site_split (L := T.L) (i := i + ((T.L * k : Nat) : Int))
    (q := i / T.L + (k : Int)) (r := (i % T.L).toNat) (by omega) hm (by omega)
  simp only [field, hq, hr, periodicCode_period]

/-- An injective family indexed by every ternary word of length `k`, on marked rings of size
`L k`, each of exact minimal moving return `P`. -/
theorem ring_family (T : Tiles) (hT : Valid T) (D : Decoder T) (k : Nat) (hk : 0 < k) :
    ∃ E : (Fin k → Fin 3) → (Int → Bool),
      (∀ u v, E u = E v → u = v) ∧
      ∀ w, Per (T.L * k) (E w) ∧ orbit (E w) T.P = E w ∧
        (∀ d : Nat, 0 < d → d < T.P → orbit (E w) d ≠ E w) := by
  refine ⟨fun w => field T (periodicCode k hk w) 0, ?_,
    fun w => ⟨ring_period T hT k hk w, exact_period T hT _⟩⟩
  intro u v h
  have hc := code_injective T D (periodicCode k hk u) (periodicCode k hk v) h
  funext j
  have hh := congrFun hc j.val
  simpa only [periodicCode_read] using hh

/-! ### Words -/

/-- Extend a finite word `u : Fin k → Fin 3` by tile 0 outside `0 ≤ q < k`. -/
def codeOfFin (k : Nat) (u : Fin k → Fin 3) (q : Int) : Fin 3 :=
  if h : 0 ≤ q ∧ q.toNat < k then u ⟨q.toNat, h.2⟩ else 0

theorem codeOfFin_read (k : Nat) (u : Fin k → Fin 3) (j : Fin k) :
    codeOfFin k u (j.val : Int) = u j := by
  have h1 : 0 ≤ (j.val : Int) := Int.natCast_nonneg j.val
  simp [codeOfFin, h1, j.isLt]

/-- The prefix of length `n` of the row that encodes `u : Fin (n / L) → Fin 3`. -/
def wordOfFin (T : Tiles) (n : Nat) (u : Fin (n / T.L) → Fin 3) : Fin n → Bool :=
  fun i : Fin n => field T (codeOfFin (n / T.L) u) 0 (i.val : Int)

theorem wordOfFin_injective (T : Tiles) (D : Decoder T) (n : Nat) :
    Function.Injective (wordOfFin T n) := by
  intro u v h
  funext j
  have hL : 0 < T.L := by have := D.o1_lt; omega
  have hb : (j.val + 1) * T.L ≤ n := (Nat.le_div_iff_mul_le hL).mp j.isLt
  rw [Nat.add_mul, Nat.one_mul, Nat.mul_comm] at hb
  have hj1 : T.L * j.val + D.o1 < n := by have := D.o1_lt; omega
  have hj2 : T.L * j.val + D.o2 < n := by have := D.o2_lt; omega
  have hv1 := congrFun h ⟨T.L * j.val + D.o1, hj1⟩
  have hv2 := congrFun h ⟨T.L * j.val + D.o2, hj2⟩
  dsimp only [wordOfFin] at hv1 hv2
  rw [Int.natCast_add, Int.natCast_mul] at hv1 hv2
  calc u j = codeOfFin (n / T.L) u (j.val : Int) := (codeOfFin_read _ u j).symm
    _ = D.read (field T (codeOfFin (n / T.L) u) 0 ((T.L : Int) * (j.val : Int) + (D.o1 : Int)))
        (field T (codeOfFin (n / T.L) u) 0 ((T.L : Int) * (j.val : Int) + (D.o2 : Int))) :=
          (decode T D _ _).symm
    _ = D.read (field T (codeOfFin (n / T.L) v) 0 ((T.L : Int) * (j.val : Int) + (D.o1 : Int)))
        (field T (codeOfFin (n / T.L) v) 0 ((T.L : Int) * (j.val : Int) + (D.o2 : Int))) := by
          rw [hv1, hv2]
    _ = codeOfFin (n / T.L) v (j.val : Int) := decode T D _ _
    _ = v j := codeOfFin_read _ v j

/-- For every `n`, an injective map from ternary words of length `n / L` to binary words of
length `n` that occur in rows of moving period `P`. -/
theorem words (T : Tiles) (hT : Valid T) (D : Decoder T) (n : Nat) :
    ∃ word : (Fin (n / T.L) → Fin 3) → (Fin n → Bool),
      Function.Injective word ∧
      ∀ u, ∃ x : Int → Bool, orbit x T.P = x ∧ ∀ j : Fin n, word u j = x (j.val : Int) :=
  ⟨wordOfFin T n, wordOfFin_injective T D n,
    fun u => ⟨field T (codeOfFin (n / T.L) u) 0, period T hT _, fun _ => rfl⟩⟩

/-! ### Period 12: three tiles of length 34 -/

/-- The three period-12 tiles of length 34, in order. Tile 0 is
`Rule30MovingWaves.TravellingCode.zeroProfiles` and tile 2 is
`Rule30MovingWaves.TravellingCode.oneProfiles`; tile 1 does not occur there. -/
def profiles12 : List (List Nat) :=
  [ [2868,3242,2734,2769,1321,1721,2469,1381,1367,2772,3372,2738,
     2986,1131,2644,3674,2406,2389,1493,1323,2868,3242,2734,2769,
     1321,1721,2469,1381,1367,3028,3116,2610,2602,1323],
    [2868,3242,2734,2769,1321,1721,2469,1381,1367,2772,3372,2738,
     2986,1131,2644,3674,2406,2389,1493,1327,2864,3240,2728,2772,
     3372,2738,2986,1131,2644,3674,2406,2389,1493,1323],
    [2868,3242,2734,2769,1321,1721,2469,1381,1367,3028,3116,2610,
     2602,1323,2868,3242,2734,2769,1321,1721,2469,1381,1367,2772,
     3372,2738,2986,1131,2644,3674,2406,2389,1493,1323] ]

def tiles12 : Tiles := { L := 34, P := 12, profiles := profiles12 }

/-- All nine seams, all 34 offsets and all 12 phases: 3672 local Rule 30 identities, checked by
the Lean kernel. -/
theorem tile_certificate12 : ∀ a b : Fin 3, ∀ r : Fin 34, ∀ t : Fin 12,
    profile tiles12 a r.val (t.val + 1) =
      xor (joined tiles12 a b r.val t.val)
        (joined tiles12 a b (r.val + 1) t.val || joined tiles12 a b (r.val + 2) t.val) := by
  decide +kernel

theorem tile_exact12 : ∀ a : Fin 3, ∀ d : Fin 12, d.val ≠ 0 →
    ∃ r : Fin 34, profile tiles12 a r.val d.val ≠ profile tiles12 a r.val 0 := by
  decide +kernel

theorem valid12 : Valid tiles12 :=
  ⟨by decide, by decide, tile_certificate12, tile_exact12⟩

/-- Reads a period-12 tile from its phase-0 cells at offsets 20 and 23. -/
def read12 (u v : Bool) : Fin 3 := if u then 2 else if v then 0 else 1

theorem reads12 : ∀ a : Fin 3, read12 (profile tiles12 a 20 0) (profile tiles12 a 23 0) = a := by
  decide +kernel

def decoder12 : Decoder tiles12 :=
  { o1 := 20, o2 := 23, read := read12, o1_lt := by decide, o2_lt := by decide, reads := reads12 }

/-- The cells at offsets 20 and 23 of block `q` recover `code q`. -/
theorem decode12 (code : Int → Fin 3) (q : Int) :
    read12 (field tiles12 code 0 (34 * q + 20)) (field tiles12 code 0 (34 * q + 23)) = code q :=
  decode tiles12 decoder12 code q

/-- A free bi-infinite ternary code, every image of exact minimal moving return 12. -/
theorem free_ternary_period_twelve :
    ∃ E : (Int → Fin 3) → (Int → Bool),
      (∀ a b, E a = E b → a = b) ∧
      ∀ code, orbit (E code) 12 = E code ∧
        (∀ d : Nat, 0 < d → d < 12 → orbit (E code) d ≠ E code) :=
  free_ternary tiles12 valid12 decoder12

/-- An injective family indexed by every ternary word of length `k`, on marked rings of size
`34 k`, each of exact minimal moving return 12. -/
theorem ternary_marked_rings_twelve (k : Nat) (hk : 0 < k) :
    ∃ E : (Fin k → Fin 3) → (Int → Bool),
      (∀ u v, E u = E v → u = v) ∧
      ∀ w, Per (34 * k) (E w) ∧ orbit (E w) 12 = E w ∧
        (∀ d : Nat, 0 < d → d < 12 → orbit (E w) d ≠ E w) :=
  ring_family tiles12 valid12 decoder12 k hk

/-- An injective map from ternary words of length `n / 34` to binary words of length `n` that
occur in rows of moving period 12. -/
theorem ternary_words_twelve (n : Nat) :
    ∃ word : (Fin (n / 34) → Fin 3) → (Fin n → Bool),
      Function.Injective word ∧
      ∀ u, ∃ x, orbit x 12 = x ∧ ∀ j : Fin n, word u j = x (j.val : Int) :=
  words tiles12 valid12 decoder12 n

/-- After 12 updates of Rule 30 the field of every ternary code is back, moved 12 cells right. -/
theorem ternary_wave_twelve (code : Int → Fin 3) (i : Int) :
    Rule30Realization.evol (field tiles12 code 0) 12 (i + 12) = field tiles12 code 0 i :=
  wave tiles12 valid12 code i

/-! ### Period 15: three tiles of length 31 -/

/-- The three period-15 tiles of length 31, in order. -/
def profiles15 : List (List Nat) :=
  [ [5461,23930,21125,13126,10949,10917,21927,10836,13684,11082,11470,12969,
     10921,27605,5165,6707,22058,21802,11581,21154,11171,23122,26226,5451,
     21834,24238,8553,20889,12629,10581,27050],
    [5461,23930,21125,13126,10949,10917,21926,10837,30069,2890,3277,2731,
     19114,20310,10409,26837,5293,7347,21194,21162,11183,23120,26216,21848,
     21844,31412,17738,18094,9577,26009,5717],
    [5461,23930,21125,13126,10949,10917,21927,10836,13684,11082,11470,12969,
     10921,27605,5165,6707,22058,21802,11573,21162,11183,23120,26216,21848,
     21844,31412,17738,18094,9577,26009,5717] ]

def tiles15 : Tiles := { L := 31, P := 15, profiles := profiles15 }

/-- All nine seams, all 31 offsets and all 15 phases: 4185 local Rule 30 identities, checked by
the Lean kernel. -/
theorem tile_certificate15 : ∀ a b : Fin 3, ∀ r : Fin 31, ∀ t : Fin 15,
    profile tiles15 a r.val (t.val + 1) =
      xor (joined tiles15 a b r.val t.val)
        (joined tiles15 a b (r.val + 1) t.val || joined tiles15 a b (r.val + 2) t.val) := by
  decide +kernel

theorem tile_exact15 : ∀ a : Fin 3, ∀ d : Fin 15, d.val ≠ 0 →
    ∃ r : Fin 31, profile tiles15 a r.val d.val ≠ profile tiles15 a r.val 0 := by
  decide +kernel

theorem valid15 : Valid tiles15 :=
  ⟨by decide, by decide, tile_certificate15, tile_exact15⟩

/-- Reads a period-15 tile from its phase-0 cells at offsets 6 and 23. -/
def read15 (u v : Bool) : Fin 3 := if u then (if v then 0 else 2) else 1

theorem reads15 : ∀ a : Fin 3, read15 (profile tiles15 a 6 0) (profile tiles15 a 23 0) = a := by
  decide +kernel

def decoder15 : Decoder tiles15 :=
  { o1 := 6, o2 := 23, read := read15, o1_lt := by decide, o2_lt := by decide, reads := reads15 }

/-- The cells at offsets 6 and 23 of block `q` recover `code q`. -/
theorem decode15 (code : Int → Fin 3) (q : Int) :
    read15 (field tiles15 code 0 (31 * q + 6)) (field tiles15 code 0 (31 * q + 23)) = code q :=
  decode tiles15 decoder15 code q

/-- A free bi-infinite ternary code, every image of exact minimal moving return 15. -/
theorem free_ternary_period_fifteen :
    ∃ E : (Int → Fin 3) → (Int → Bool),
      (∀ a b, E a = E b → a = b) ∧
      ∀ code, orbit (E code) 15 = E code ∧
        (∀ d : Nat, 0 < d → d < 15 → orbit (E code) d ≠ E code) :=
  free_ternary tiles15 valid15 decoder15

/-- An injective family indexed by every ternary word of length `k`, on marked rings of size
`31 k`, each of exact minimal moving return 15. -/
theorem ternary_marked_rings_fifteen (k : Nat) (hk : 0 < k) :
    ∃ E : (Fin k → Fin 3) → (Int → Bool),
      (∀ u v, E u = E v → u = v) ∧
      ∀ w, Per (31 * k) (E w) ∧ orbit (E w) 15 = E w ∧
        (∀ d : Nat, 0 < d → d < 15 → orbit (E w) d ≠ E w) :=
  ring_family tiles15 valid15 decoder15 k hk

/-- An injective map from ternary words of length `n / 31` to binary words of length `n` that
occur in rows of moving period 15: an explicit ternary language lower bound, `log2(3)/31` bits
per cell. -/
theorem ternary_words_fifteen (n : Nat) :
    ∃ word : (Fin (n / 31) → Fin 3) → (Fin n → Bool),
      Function.Injective word ∧
      ∀ u, ∃ x, orbit x 15 = x ∧ ∀ j : Fin n, word u j = x (j.val : Int) :=
  words tiles15 valid15 decoder15 n

/-- After 15 updates of Rule 30 the field of every ternary code is back, moved 15 cells right. -/
theorem ternary_wave_fifteen (code : Int → Fin 3) (i : Int) :
    Rule30Realization.evol (field tiles15 code 0) 15 (i + 15) = field tiles15 code 0 i :=
  wave tiles15 valid15 code i

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The theorems, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata", "Ruliology.CellularAutomata.Rule30RingOrbits"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
heads = {"tile_certificate12", "decode12", "free_ternary_period_twelve", "ternary_marked_rings_twelve", "ternary_words_twelve", "ternary_wave_twelve", "tile_certificate15", "decode15", "free_ternary_period_fifteen", "ternary_marked_rings_fifteen", "ternary_words_fifteen", "ternary_wave_fifteen"};
show[heads, "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.ternary_wave_fifteen"]["KernelCheck"]
```
