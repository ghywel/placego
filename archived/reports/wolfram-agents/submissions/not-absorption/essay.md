---
Template: ComputationalEssay
Name: AbsorptionT t001 Is False: a Period-15 Trap for 001, after lhallee/rule30-open
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-10
Description: Core Lean, the kit's own definitions. The kit's open statement AbsorptionT t001 for the period-3 word 001 is false: a checked period-15 trap for 001 is apart from t001, and a right half started in it never enters t001. The theorem and the trap are Logan Hallee's, in lhallee/rule30-open; this restates it in the kit's form so that the kit's status can be corrected.
Abstract: In core Lean 4.35.0, with the kit's own definitions, we prove that the kit's AbsorptionT t001 is false. The kit reduces the word 001 of least period three to AbsorptionT t001: every finitely supported right half driven by 001, from any phase, eventually has its first 47 cells in a state of the 815-state trap t001 at a label of the same phase. The kit lists it as open. A second checked trap for 001 refutes it. It has period 15, 52 cells and 153 states; no state of it, cut to 47 cells, is a state of t001 at the same phase, and the right half given by its state 0 stays in it for ever by the kit's trap invariant, so it never enters t001. The theorem and the trap are Logan Hallee's, in lhallee/rule30-open (Rule30Open.Columns.Traps001), which proves more: entry into one of any three of four pairwise apart traps fails. This module restates the first theorem in the kit's PTrap form so that the kit's status table can be corrected; the half that rule30-open names is the trap's state 25. The kit's implication from AbsorptionT t001 to the exclusion of 001 stays true, but its hypothesis is false. Whether the center column can be eventually 001 remains open.
Keywords: [rule 30, Rule 30 Prize, period three, 001, trap, AbsorptionT, right half, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[lhallee/rule30-open](https://github.com/lhallee/rule30-open)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[rule30-open: Traps001](https://github.com/lhallee/rule30-open/blob/1ddcd41186e245d6a001604e15b584981990591a/Rule30Open/Columns/Traps001.md)"]
---

## 1. The statement

For the word `001` of least period three, the kit's `Rule30EtherThreeTrap` gives a trap: `t001` is a set of `815` states of the first `47` columns beside the center, each with a label modulo `21`, closed under both values of column `48`. If the right half of rule 30 enters it while the center column repeats `001`, column `1` becomes periodic at the white times, which masked Jen forbids. So the kit reduces `001` to an entry statement.

`AbsorptionT t001`: every finitely supported right half driven by `001`, from any phase, eventually has its first `47` cells in a state of `t001` at a label of the same phase. It implies that the center column is not eventually `001` repeated (`not_eventually_001_of_absorption`). The kit's status table, its `Rule30EtherThreeTrap` row and the header of `Rule30EtherThreeErosion` all list it as open.

It is false:

- `trap001fifteen_check`: `trap001fifteen` is a checked `PTrap` for `001`, with `52` cells, labels modulo `15` and `153` states, closed under both values of column `53`.
- `fifteen_apart_t001`: no state of `trap001fifteen`, cut to its first `47` cells, is a state of `t001` whose label has the same phase. The kernel compares all `153 × 815 = 124,695` pairs.
- `stays`: the right half whose cells `1..48` are the state `0` of `trap001fifteen`, white beyond, driven by `001` from phase `0`, keeps its first `52` cells in the trap at every step, with the label counting the time. This is the kit's own `PTrap.invariant`.
- `not_absorptionT_t001`: so that half never enters `t001`, and `¬ AbsorptionT t001`.
- `rule30open_half`: the right half that `lhallee/rule30-open` names as its witness is the state `25` of the same table, at label `3`, which has the same phase.

## 2. Why two traps cannot share an orbit

This explains why the two traps can be apart; the proof is the kernel check `fifteen_apart_t001`, state by state. Both traps are closed, so a half that entered `t001` from `trap001fifteen` would stay in both for ever. On each trap, column `1` at the white phases is a function of the label, with period `21` on `t001` and period `15` on `trap001fifteen`. In both at once, that column would repeat with period `3` at the white times, which the function for `t001` does not do.

## 3. What it changes in the kit

`not_eventually_001_of_absorption` stays true, but its hypothesis is false, so it gives nothing. The kit's route for `001` needs a weaker entry statement. A half that starts in one trap stays in it, so entry into one of a list of traps fails whenever some further trap is apart from every trap of the list; `rule30-open` shows this for any three of its four. What remains is entry into one of a longer list, or into some trap. The empty right half does enter `t001`, at step `1270` (`Rule30EtherThreeReach.absorbed_empty`). Whether the center column can be eventually `001` remains open.

## 4. Worked numbers

The cell below reads the kit's packed table for `t001` and runs three right halves for `3,000` steps, driven by `001` from phase `0`: the module's witness, the half named by `rule30-open`, and the empty half. For each it gives the first step at which cells `1..47` are a state of `t001` at a label of the same phase, or `-1` if there is none. For the two witnesses it also gives the number of distinct `52`-cell windows seen.

```wl
trapSource = Import[FileNameJoin[{Environment["RULE30PRIZE_KIT"], "lean", "Ruliology", "CellularAutomata", "Rule30EtherThreeTrap.lean"}], "Text"];
num[name_] := ToExpression[First[StringCases[trapSource, "def " <> name <> " : Nat := " ~~ digits : DigitCharacter .. :> digits]]];
r001 = num["t001_R"]; l001 = num["t001_L"];
states = GroupBy[Table[{Mod[BitShiftRight[l001, 5 i], 2^5], Mod[BitShiftRight[r001, 47 i], 2^47]}, {i, 0, 814}], (Mod[First[#], 3] &) -> Last, AssociationThread[# -> True] &];
run[x0_] := Module[{x = x0, first = -1, seen = <||>}, Do[If[first < 0 && KeyExistsQ[Lookup[states, Mod[t, 3], <||>], Mod[x, 2^47]], first = t]; seen[Mod[x, 2^52]] = True; x = BitXor[BitOr[BitShiftLeft[x, 1], {0, 0, 1}[[Mod[t, 3] + 1]]], BitOr[x, BitShiftRight[x, 1]]], {t, 0, 3000}]; {first, Length[seen]}];
{a, r, c} = run /@ {266113541000008, 196676618523018, 0};
{a[[1]], r[[1]], c[[1]], a[[2]], r[[2]]}
```

## 5. Prior art and credit

The theorem and the trap are Logan Hallee's: [`lhallee/rule30-open`, `Rule30Open.Columns.Traps001`](https://github.com/lhallee/rule30-open/blob/1ddcd41186e245d6a001604e15b584981990591a/Rule30Open/Columns/Traps001.lean), with its note [Traps001](https://github.com/lhallee/rule30-open/blob/1ddcd41186e245d6a001604e15b584981990591a/Rule30Open/Columns/Traps001.md). That module proves more:
- there are four traps for `001`, pairwise apart;
- entry into one of any three of them fails;
- entry into some trap of `001` would still exclude it.

Our agent PE-1 found the period-15 table independently while searching traps for `001`, and our replay BN-L1 checked the refutation with the kit's `PTrap` machinery before we saw that rule30-open already had it. This module is that replay, cleaned for the kit.

We submit it, with the owner's approval and full credit, because the kit and the portal still list the statement as open. What is ours is only the kit-form restatement and its check. Nothing here decides Problem 1 for period three.

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30EtherThreeTrap`.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30EtherThreeTrap
/-!
# `AbsorptionT t001` is false

`Rule30EtherThreeTrap` reduces the word `001` of least period three to `AbsorptionT t001`: every
finitely supported right half driven by `001`, from any phase, eventually has its first `47` cells
in a state of the trap `t001` whose label reads the drive's phase. Then the center column is not
eventually `001` repeated (`not_eventually_001_of_absorption`). That entry statement is false, by a
second trap.

* `trap001fifteen_check`: `trap001fifteen` is a checked `PTrap` for `001` of period `15`, with `52`
  cells and `153` labelled states.
* `fifteen_apart_t001`: no state of it, cut to its first `47` cells, is a state of `t001` whose
  label has the same phase.
* `stays`: the right half `xw` whose cells `1..48` are the state `0` of `trap001fifteen` (white
  beyond) stays in it for ever, its label counting the time, by the kit's `PTrap.invariant`.
* `not_absorptionT_t001`: hence `¬ AbsorptionT t001`.
* `rule30open_half`: the half that `lhallee/rule30-open` names is the state `25` of the table, at
  label `3`, of the same phase.

The theorem and the trap are from `lhallee/rule30-open` (Logan Hallee), module
`Rule30Open.Columns.Traps001`, which also gives two traps more and shows that entry into one of any
three of the four fails. This module states the first theorem with the kit's own `PTrap` check and
invariant. `not_eventually_001_of_absorption` stays true, but its hypothesis is false, so the kit's
route for `001` needs a weaker entry statement. Nothing here decides whether the center column can
be eventually `001`.
-/

namespace Rule30Submission

open Ruliology.CellularAutomata

open Rule30Jen Rule30StripCertificates Rule30Ether Rule30EtherThree

def trap001fifteen_R : Nat := 9450600693252949843732448339815039139048768350953350715112823805916787025649778104590648527770421809983648099512722874139022579145115806677637912344428374689234887314788089527210240717358375449597586127644712238228714234996544983333176871007283268701049101512963649828230858900996498721026461250339574941707508312856495005440329120072006896968624028748994391835340344473380246625445540833728284361430820090895698379273012100671444072731540401981300891065376466119040615630667001557389897752748981360711534058855618421376529920583254183209058598054415930008438055551077372732137882822904971448251520374054425583339913346388812818114949392559916555143758113853804081869108339843002410147112200792267927010413649171597100984739534518259721664713838774476674636078615601430654708476614949558334796924496140277517977813959761727010944798512939537745583852916689108032915612284587146171446697871866129320614446107021537891654583829796866666217281199656819888586262445505258581444484931853719261715262427937410242480378569595863251721588067121485463787771170574025803759713699949359780494873395305814476940281192961457117073416597279198667795596187593512971127347274947717224400390856107638080235560923832153099579696918149701123786154319731270496898765681484193017732002377079331895810000674083901721982659714478428156869798586158841305104501893233500723886099194340101706894201012913858044538088619559453714225264296467926595849375872638446504981271442372247383095461278480998115234307638229887155163782015837952856870132108332900114070451926983997832229059418112787426149993933410144040780861485897911176240900160112672778973546169300854814946332204827955878992749700071689574892331573646131677543796102686040550894827338515033387442400370323863026403002249220923944580593744350635246654336568995785001231341117566140198618856575900782088963537235752294500697460736063316326752516455380683578659074185370909933706319404077318504007597642231911050453390847946727595476001910910766981810627690039220490174230585036462519146099817524992410457313335345053271521518012635073292181343356827463209949118197222948400195000179565859165076474168737619959121037031852379971514514933170356619496948244113462280128277205046245458738558141773749554560572677036462762303021998051204082779771271572228279879425386066168544241809082025456421996612924175291645808417088722733309143023151426023707351302268982593375048
def trap001fifteen_L : Nat := 15863321385459746804189563166579650987068578116034125387509785810259451246829976933572125761297880128199724223706412980683286120641524351081106604182677311527668269199645910951138426880
def trap001fifteen_S : Nat := 327267183279939480304312763851464835155876934788893097923950833766915821333493686179209014681099261737098392765076880812661165753242587714520718937864109058047268288906605720612714589264730487540138977208137671038880749805235517007938172252077107651983931662681211099700412871911160835317075114791114433138361849688149484980246442435632336027912703177875026036504606332143384153089500618261826951380141039693256840039087964773472216890665732823480090992237167761888572678126413643478222884573461347742945799733145448353713018181652824567090032410674591845969683794970690752858733997480145282444553914114709773494997865068873117754214449817777754674865396103603993117288113377270976225065292410043408133847748741463600871320193384254986

/-- The period-15 trap for `001` of `lhallee/rule30-open`: `52` cells, labels modulo `15`, `153` states. -/
def trap001fifteen : PTrap :=
  { w := w001, b := 52, m := 15, n := 153, lb := 4, ib := 8, u := 18864,
    R := trap001fifteen_R, L := trap001fifteen_L, S := trap001fifteen_S }

theorem trap001fifteen_check : trap001fifteen.check = true := by decide +kernel

/-- The right half of the witness, as a bit mask (bit `i` is column `i + 1`). -/
def x0 : Nat := 266113541000008
def i0 : Nat := 0

theorem i0_lt : i0 < trap001fifteen.n := by decide +kernel
theorem st_i0 : trap001fifteen.st i0 = x0 := by decide +kernel
theorem lab_i0 : trap001fifteen.lab i0 = 0 := by decide +kernel
theorem x0_lt : x0 < 2 ^ 48 := by decide +kernel

/-- No state of `A`, cut to its low `K` bits, equals a state of `B` at equal phase. -/
def disjointB (A B : PTrap) (K : Nat) : Bool :=
  allBelowT (fun j => allBelowT (fun i =>
    !(A.lab j % 3 == B.lab i % 3 && A.st j % 2 ^ K == B.st i)) B.n) A.n

theorem disjointB_spec {A B : PTrap} {K : Nat} (h : disjointB A B K = true) {j i : Nat}
    (hj : j < A.n) (hi : i < B.n) (hl : A.lab j % 3 = B.lab i % 3)
    (hs : A.st j % 2 ^ K = B.st i) : False := by
  unfold disjointB at h
  have h1 := allBelowT_spec (allBelowT_spec h j hj) i hi
  simp [hl, hs] at h1

theorem fifteen_apart_t001 : disjointB trap001fifteen t001 47 = true := by decide +kernel

/-- The witness as a right half. -/
def xw : Nat → Bool := fun p => x0.testBit (p - 1)

/-- The evolution in the statement of `AbsorptionT t001` for `xw` at phase `0`. -/
def Fw : Nat → Nat → Bool := drv (fun t => wordAt3 t001.w (t + 0)) xw

theorem xw_fin : ∀ p, 48 < p → xw p = false := by
  intro p hp
  exact Nat.testBit_lt_two_pow
    (Nat.lt_of_lt_of_le x0_lt (Nat.pow_le_pow_right (by decide) (by omega)))

/-- The orbit of `xw` stays in `trap001fifteen`, the label counting time modulo `15`. -/
theorem stays (t : Nat) : ∃ j, j < trap001fifteen.n ∧ EncF Fw trap001fifteen.b t 0 (trap001fifteen.st j) ∧
    trap001fifteen.lab j % 3 = t % 3 := by
  have hc : ∀ t, 0 ≤ t → Fw t 0 = wordAt3 trap001fifteen.w (t - 0) := by
    intro t _
    unfold Fw
    rw [drv_col0]
    rfl
  have hr0 : EncF Fw trap001fifteen.b 0 0 (trap001fifteen.st i0) := by
    refine ⟨PTrap.st_lt trap001fifteen i0, fun k _ => ?_⟩
    unfold Fw
    rw [drv_init _ _ _ (by omega), st_i0]
    show x0.testBit k = x0.testBit (0 + 1 + k - 1)
    congr 1
    omega
  have hph : (0 - 0) % 3 = trap001fifteen.lab i0 % 3 := by rw [lab_i0]
  obtain ⟨j, hj, hr, hl⟩ :=
    PTrap.invariant trap001fifteen trap001fifteen_check (drv_isR30 _ _) 0 hc 0 i0 (Nat.le_refl 0) i0_lt hph hr0 t
  refine ⟨j, hj, ?_, ?_⟩
  · rw [Nat.zero_add] at hr
    exact hr
  · have hm : trap001fifteen.m = 15 := rfl
    rw [hl, lab_i0, hm]
    omega

/-- **`AbsorptionT t001` is false.** -/
theorem not_absorptionT_t001 : ¬ AbsorptionT t001 := by
  intro hA
  obtain ⟨t1, i, hi, hph, hr⟩ := hA xw 48 xw_fin 0
  have hr' : EncF Fw t001.b t1 0 (t001.st i) := hr
  obtain ⟨j, hj, hrj, hlj⟩ := stays t1
  have hb47 : t001.b = 47 := rfl
  have hb52 : trap001fifteen.b = 52 := rfl
  have hl : trap001fifteen.lab j % 3 = t001.lab i % 3 := by
    rw [hlj, ← hph]
    omega
  have hs : trap001fifteen.st j % 2 ^ 47 = t001.st i := by
    apply Nat.eq_of_testBit_eq
    intro k
    by_cases hk : k < 47
    · rw [Nat.testBit_mod_two_pow, decide_eq_true hk, Bool.true_and]
      exact (hrj.2 k (by rw [hb52]; omega)).trans (hr'.2 k (by rw [hb47]; exact hk)).symm
    · have h1 : (t001.st i).testBit k = false :=
        Nat.testBit_lt_two_pow (Nat.lt_of_lt_of_le (PTrap.st_lt t001 i)
          (Nat.pow_le_pow_right (by decide) (by rw [hb47]; omega)))
      rw [Nat.testBit_mod_two_pow, decide_eq_false hk, Bool.false_and, h1]
  exact disjointB_spec fifteen_apart_t001 hj hi hl hs

/-- **The half that `lhallee/rule30-open` names is a state of this trap**, at a label of phase `0`. -/
theorem rule30open_half : trap001fifteen.st 25 = 196676618523018 ∧ trap001fifteen.lab 25 = 3 := by
  decide +kernel

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The theorems, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata", "Ruliology.CellularAutomata.Rule30EtherThree", "Ruliology.CellularAutomata.Rule30Ether", "Ruliology.CellularAutomata.Rule30StripCertificates"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
heads = {"trap001fifteen_check", "fifteen_apart_t001", "stays", "not_absorptionT_t001", "rule30open_half"};
show[heads, "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.rule30open_half"]["KernelCheck"]
```
