---
Template: ComputationalEssay
Name: The universal start of the right diagonals of rule 30
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-29
Description: A partial result about the right diagonals of rule 30, proved in core Lean with a kernel-checked 256-case certificate: in every finite nonempty row, the six diagonals after the alternating prefix have least periods 4, 8, 8, 16, 32, 32, whatever the other cells
Abstract: Read rule 30 from a start whose rightmost black cell is at $0$, along its right diagonals $D_j(t)=x_t(t-j)$, and write $s_d=x_0(-d)$. Let $m\ge2$ be the first index with $s_m=s_{m-1}$. Then $D_{m+1},\dots,D_{m+6}$ have least periods $4,8,8,16,32,32$ and $D_{m+7}$ has least period $32$ or $64$, whatever the other start bits (`Rule30Submission.universal_start`). Under these edge hypotheses every finitely supported start has such an $m$, so the conclusion holds for every finite nonempty seed (`Rule30Submission.universal_start_finite`). The proof has a hand part and a finite part. The black edge makes $D_1$ and $D_2$ alternate. From there through $D_m$, the next diagonal's feeders have opposite phases, so their OR is always black; $D_{m-1}$ and $D_m$ then alternate with equal phase. A running XOR of a $P$-periodic forcing repeats after $2P$ (`Rule30Submission.run_double`), so the next seven diagonals repeat within $256$ ticks, and on those ticks they depend only on the common phase and seven start bits. A certificate checked by the kernel with `decide +kernel`, without native code, computes all $256$ cases as bit masks and decides each least period by cyclic rotations (`Rule30Submission.cert`, `Rule30Submission.universal_start_profiles`). The general doubling criterion and the single cell's right periods are the kit's (`Rule30RightPeriods`); what is added is that this opening is the same for every finite seed. If $s_d\ne s_{d-1}$ for every $d\ge2$, no such $m$ exists, and this theorem does not apply. Nothing here concerns the centre column or decides Problem 1.
Keywords: [rule 30, Rule 30 Prize, right diagonals, least period, period doubling, finite seeds, kernel certificate, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[Rule30RightPeriods in the kit](https://github.com/WolframInstitute/Rule30PrizeKit/blob/main/lean/Ruliology/CellularAutomata/Rule30RightPeriods.lean)"]
---

## The question

Read rule 30 along its right diagonals: put the rightmost black cell of the start at $0$ and write
$D_j(t) = x_t(t - j)$, the cell $j$ places in from the right edge, which moves one cell per step. The rule,
$\text{left} \oplus (\text{centre} \lor \text{right})$, becomes

$$D_j(t+1) = D_j(t) \oplus \bigl(D_{j-1}(t) \lor D_{j-2}(t)\bigr),$$

with $D_0$ black and $D_{-1}$ white for ever (`rightDiag_step`, `edge`). Each diagonal is a running XOR of the OR of
the two to its right. A running XOR of a $P$-periodic forcing repeats after $2P$. This gives upper bounds for individual diagonal
periods; common periods of whole diagonal prefixes track the feeders jointly.

For the single black cell, the kit's `Rule30RightPeriods` describes these periods. A finite row has many other
starts, and its far-left cells eventually feed every diagonal. This essay asks how much of the opening of the
period sequence depends on the start. The first six periods after the alternating prefix are universal;
the seventh can depend on the remaining start bits.

## The alternating prefix

Write $s_d = x_0(-d)$ for the start bits, so $s_0 = 1$. Every diagonal $D_d$ with $1 \le d$ starts at $s_d$. While
consecutive start bits differ, the two feeders of the next diagonal alternate with opposite phases, so their OR is
always black and the diagonal flips at every step. Let $m \ge 2$ be the first index with $s_m = s_{m-1}$. Then
$D_1, \dots, D_m$ all alternate, and $D_{m-1}$, $D_m$ alternate *with the same phase*: their OR is itself an
alternating word, the first forcing that is not constant.

For a finitely supported start the index $m$ exists, since two white cells beyond the support are equal
(`universal_start_finite`). If $s_d\ne s_{d-1}$ for every $d\ge2$, there is no such $m$, and all positive right diagonals alternate. An
eventually alternating tail can still have an earlier equal pair; that case is covered when such an $m$ exists.

## Two equal-phase feeders fix the next seven diagonals

From two alternating feeders of common phase $p$, the next diagonals are $E_0, E_1, \dots$ with
$E_k(0) = s_{m+1+k}$ and

$$E_0(t+1) = E_0(t) \oplus \mathrm{alt}_p(t), \quad E_1(t+1) = E_1(t) \oplus \bigl(E_0(t) \lor \mathrm{alt}_p(t)\bigr), \quad
E_{k+2}(t+1) = E_{k+2}(t) \oplus \bigl(E_{k+1}(t) \lor E_k(t)\bigr).$$

A running XOR of a $P$-periodic forcing repeats after $2P$ (`run_double`), so $E_k$ repeats after $2^{k+2}$ ticks
(`E_per`): every one of $E_0, \dots, E_6$ repeats after $256$. Their values on the ticks $0, \dots, 255$ depend only on
$p$ and the seven bits $s_{m+1}, \dots, s_{m+7}$ (`E_congr`). So their least periods are decided by $2 \times 2^7 = 256$
finite cases.

`universal_start_profiles` states the outcome: in every case $E_0, \dots, E_5$ have least periods
$4, 8, 8, 16, 32, 32$, and $E_6$ has least period $32$ or $64$. `universal_start` transfers this to the diagonals
$D_{m+1}, \dots, D_{m+7}$ of the kit's `Rule30Realization.evol`.

## The certificate

The certificate `cert` is one Boolean function evaluated by the kernel on all $256$ cases (`decide +kernel`; no
`native_decide`). For each case one loop runs the seven recurrences for $256$ ticks and stores each diagonal's
ticks as the bits of a natural number (`loop_spec` proves that bit $t$ of the mask is $E_k(t)$). A word of period
dividing $256$ has period $c$ exactly when its mask equals its cyclic rotation by $c$ (`perOK_iff`). The least
period $P$ is then confirmed by checking the rotation by $P$ and rejecting every rotation by $0 < c < P$
(`leastOK_spec`). A smaller period that does not divide $256$ is rejected as well, so "least" means least among all
positive periods.

## A computation

The Wolfram Language reads the same diagonals off a literal evolution, for the single cell and six random seeds of
eleven cells. `CellularAutomaton` trims background cells from the ends of the initial list, so the edge is located
from the width of the output.

```wl
SeedRandom[30];
seeds = Prepend[Table[Join[{1}, RandomInteger[1, 10]], 6], {1}];
T = 512;
row[s_] := Module[{sp = Join[s, {0, 0}], m, ca, e, d, lp},
  m = SelectFirst[Range[2, Length[sp] - 1], sp[[# + 1]] == sp[[#]] &];
  ca = CellularAutomaton[30, {Reverse[s], 0}, T];
  e = Length[First[ca]] - T;
  d[j_, t_] := ca[[t + 1, e + t - j]];
  lp[j_] := SelectFirst[Range[128], Function[p, AllTrue[Range[0, T - p - 1], d[j, #] == d[j, # + p] &]]];
  {StringJoin[ToString /@ s], m, lp /@ Range[1, m], lp /@ Range[m + 1, m + 7]}];
Grid[Prepend[row /@ seeds, {"seed bits s0 s1 ...", "m", "periods of D1..Dm", "periods of D(m+1)..D(m+7)"}], Frame -> All]
```

Each row shows period $2$ through $D_m$, then $4, 8, 8, 16, 32, 32$, then $32$ or $64$. The single cell has $m = 2$
and ends in $64$; most of the random seeds end in $32$. The table illustrates the theorem on seven starts within
$512$ steps; the theorem does not depend on it.

## The formal proof

The module, built against the kit at the verifier's commit:

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["%%LEAN%%", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The headlines, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30Realization"};
heads = {"universal_start", "universal_start_finite", "universal_start_profiles", "cert", "run_double", "rightDiag_step"};
Column[rule30Submission["Rule30Submission." <> #]["TypeForm", "Open" -> opens] & /@ heads]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The kernel accepts every declaration of the module again, the certificate included. This is the replay the
verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.universal_start"]["KernelCheck"]
```

## What is not proved

- Nothing is claimed beyond $D_{m+7}$. Whether $D_{m+7}$ has period $32$ or $64$ depends on the start bits, and the
  later diagonals depend on more of them.
- The existence guard fails when $s_d\ne s_{d-1}$ for every $d\ge2$. An alternating far-left tail alone does
  not prevent an equal pair nearer the root.
- The general doubling criterion (`Rule30RightPeriods.S_rule`, and the T-function lifting) and the single cell's
  right periods are the kit's; they are not restated as headlines. The certificate decides seven least periods; it
  is not a period-growth law for later diagonals.
- Nothing here concerns the centre column or decides Problem 1. We found no such statement in the kit's catalog or
  the submissions list as we read them, which is a statement about our search, not a global novelty determination.
- The Wolfram Language computation above illustrates the theorem on seven starts; the theorems do not depend on it.

## Relation to earlier work

The edge map of a right-finite row is the 2-adic right-edge map of Coven, Pivato and Yassawi (Proc. AMS 135,
2007). The kit's `Rule30RightPeriods` proves the doubling criterion and the single cell's right periods. Its
`Rule30FrozenRuler`, an earlier contribution of ours, compares a finite row's edge code with the single cell's and
bounds its white run behind the edge; it does not compute diagonal periods. The universal start came out of the
same study of the doubling letters as our 101 shift law (submission R30-20261029-7d47a9). Read as letters, its
periods $2, 4, 8, 8, 16, 32, 32$ give the six letters $110110$ at base period $2$. For this opening these
individual periods also determine the common prefix periods; this does not establish later individual-period
monotonicity for arbitrary seeds.

## Provenance

The universal start was found by Claude (Anthropic) on 2026-10-28, with a hand reduction to $256$ cases and a Python
check of them. GPT (OpenAI) read the reduction, found the infinite-alternating-tail exception, and checked all $256$
cases independently against $149{,}760$ literal spatial comparisons; it wrote the delivery scope. Claude formalized
the reduction and the certificate in core Lean on the kit's `evol` on 2026-10-29, and GPT read the frozen source
before the certificate was first evaluated.

## Assembly note — remove before publication

Assembled from `essay-prose.md` and `Rule30Submission.lean` by substituting the module for `%%LEAN%%`. The
certificate's first evaluation is the frozen stage in `RUN-SPEC.md`, after GPT's read. Upload only after that stage
passes, the notebook is built and checked under its own frozen budget, and GPT has read the final essay.
