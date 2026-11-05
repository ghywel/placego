# Cloud's third read of SW-02 — CL751, 5 November 2026

*Third review of [the design](SW02-SWARM-DESIGN.md), after Local's draft 1 (L1559) and GPT's draft 2 (GC2686, [review](GPT-SW02-DESIGN-REVIEW-20261105.md)).
The owner's brief to Cloud: make sure the questions are well scoped, that the swarm is worth running, add what is
missing, and above all make sure that what the record already knows supports the brief instead of being
rediscovered. Draft 3's edits are in the design document under the editing protocol (earlier text kept, overruled text
struck with its reason, §18 line). This file holds the reasoning behind them: the verdict (§1), the known inputs by
squad with their statuses and citations (§2), the three hand derivations the inputs rest on (§3), the additions (§4),
the cuts (§5), the answers to Local's six questions (§6), the bet (§7) and what was checked (§8). Nothing here is
posted or run.*

## 1. Verdict: worth running, on the survey's merits, with the attack waves conditional

**Run it.** The objectives that pay regardless of prize yield are O1 (the door ledger over a frozen manifest), O3 (the
barrier atlas with exact scopes), O6 (record repair) and O7 (unforced structure). SW-01's one real yield was the
status sweep (134 flags, 96 real, 85 corrections), and today supplied the case for O1 and O6 again from Cloud's own
work: CL740 derived "speed = heal rate × mean jump" as new, and it was §8.66's identity from 6 October under other
names (PRIOR-ART CL740–CL741). A record this size needs its own index of doors under all their names, and no single
worker's search produces it. The survey wave, the verifiers and the compilers are worth their tokens on that alone.

**The attack waves are worth running only if each squad starts from what the record holds.** Draft 2's own briefs show
the risk: AM-3 asks for an immortal splice whose impossibility by any finite operation is one line from
left-permutivity (§3.2); CP-5 asks for a "meeting point" of the ordered left side and the wall that the record says
does not exist, in five statements of which three are proved (§3.1); HX-2 asks for a seed invariant that the record
shows cannot be a left-side property (§3.3); LN-09 would re-derive the damage front that CL740–CL742 measured and
PRIOR-ART names. None of this is a fault of the drafters: Local and GPT read what they could in a day, and the
left-side work is a week old. It is the vocabulary problem of §4a, and the fix is mechanical: a `Known inputs` list
in every squad brief, with the agent restating it before it attacks (design §8.0). With that rule, Local's P1 of
0.97 (no prize-level statement survives) is still my number, but the attack waves become a test of whether anything
in the record's open items can be moved by a fresh, well-fed mind, and that is a question worth 56 briefs or the
48 I leave after the cuts.

**Recommendation to the owner.** The core, not the full roster, with §5's eight cuts applied first; Wave 0, the smoke
tasks, Wave 1 and the five-task pilot in full; the main attack wave decided after reading Wave 1's door cards and the
pilot's returns, which the design's stop rule already allows. Opus by default, Fable for at most twelve slots (§6,
question 4).

## 2. Known inputs by squad

What the record holds on each question, with the status the record gives it and the citation. Local copies these into
the briefs (design §8.0) and extends them from Wave 1. Squads not listed have briefs that already carry their inputs
(AM-1, AM-2, AM-4, AM-5, CT-1 to CT-5, CP-1 to CP-4, CP-6, the periods, Problem 2, Problem 3, BR-1 to BR-5): GPT's
draft-2 corrections were the inputs for those, and I found nothing in the left-side or edge work that bears on them
beyond the CT-2 row below.

| Squad | Known input | Status | Source |
|---|---|---|---|
| CP-5 | Wheel j at tick t + 1 reads wheels j − 2, j − 1, j at tick t; the wall of the zero-boundary frame is wheel W + t at tick t; wheels below W never see it, and the wall's influence at tick t is depths ≤ t | PROVED | `Rule30AgedLeftDiagonals.Recurrence`; `Rule30ErrorEdge.agree_step`; §3.1 (i) |
| CP-5 | The zero boundary is, in the wall frame, one white reset per tick at the moving wall, breaking the recurrence exactly when depth 1 is black; each wheel J ≥ W is born white at tick J − W and follows the recurrence after | PROVED (one line) | §3.1 (ii) |
| CP-5 | The forced front climbs at most one wheel a tick; the wall passes every wheel J ≥ W before the front reaches it, so the kit's settling bound applies from each wheel's birth | PROOF-SKETCH (one hypothesis check, design §16 Q1) | `Rule30FourFronts.walk_one`, `forced_front_four`; §3.1 (iii) |
| CP-5 | The band edge is at about 0.757 t wheels on the seed, on the fifteen fork rows and on random rows; the band recedes from the wall at about 0.243 cells a tick; the chaotic region between is about W + 0.243 t wide | MEASURED | atlas §21.6 (CL739, 894,235 ticks, sixteen rows); CL742 (nine ring runs, 0.7564 ± 0.0003); §8.66, §8.74 |
| CP-5 | The field the band sends up is fair in every statistic measured: structure above the edge in its first two wheels only; a damaged row's edge has the random background's statistics to 0.003; the strip is fair in five-bit, run and XOR statistics, with one excess of 0.002 in the stall hazard, mechanism open | MEASURED | CL740 addendum; CL741 addendum 3; CL743 addenda 1–2; CL744 addenda 1–2; CL745 addendum 2 |
| CP-5, HX-1 | The wall's only channel down to the band is the branch and phase at forks: the branch law d = ¬a_(j−1)(τ*) ⊕ c(τ* + 1); 48 of 48 random completions of the seed's prefix on A0; the worst-case prefix guard P* = 19,656 with its caveat | PROOF-SKETCH (law, 24 of 24); COMPUTED (48 of 48); PROOF-SKETCH + COMPUTED (guard) | atlas §21.10, §21.11; CL749, CL750 and addenda; `prefix_race.py`, `chink_tree.py` |
| AM-3 | The nearest difference of two rows to the wall moves one depth a tick whatever the rest; rows whose lowest differing bit is i differ in bit₀ at tick i; for even i at most one survives tick i | PROVED (one line) | §3.2; the left-permutivity behind `zrow_edge`, `testBit_F_succ_of_top` |
| AM-3 | A splice at lowest bit i enters every check from tick i on; a forever guard is Q01 at the spliced row; the record holds no check-preserving operation but the forward orbit | PROVED (first clause); record search (second) | §3.2; AM-1's baseline; CL637/GC1883/CL638 |
| AM-3, CT-2 | `Rule30ErrorEdge` and `Rule30HealingBound` are statements at the far edge's ordered band, in wheels from the leftmost black cell; a differencing argument at the wall is the speed-1 law above, not the edge theorem; every chink in the ordered band spills | PROVED (frames, spill: one line; 64 of 64) | design §4a; atlas §21.10; CL748 addendum 1 |
| HX-2 | A seed invariant P cannot be a left-side property: every left-finite configuration carries the strip after a shift; the sixteen left sides are reached from the seed by one cell per fork; random completions end on A0 | PROVED (through 87,866); COMPUTED | `Rule30FourLeftSides`, `Rule30UniversalLeftSide`; atlas §21.10, §21.11; §3.3 |
| HX-2 | The record's pointwise seed-specific structure is on the right wall and in the route graph, not on the left | Local's results; statuses as L1554–L1557 and R-05's modules give them | `Rule30FrozenRuler`, `Rule30RightWall*`; L1554–L1557 |
| R-04, LN-09 | The error edge is the damage front; the identity p = q/(q + S) and the finite form; the chains M(L, R, W) and their extrapolation; λ_L = 0.2436 ± 0.0003 against Grassberger's 0.2428; the post-jump facts; the one walk per strip, locked stretches and excursions | PROVED (identity, two-party; jump facts, kit); CONJECTURE (chain limit); MEASURED (λ_L, walks) | atlas §21.7–§21.9; PRIOR-ART (CL740–CL741); PROOFS (CL743); CL741–CL746; `edge_model.py`, `edge_random.py`, `edge_windows.py`, `jump_facts.py`, `edge_slip.py` and outputs |
| R-13 | Cloud's open items from the edge work: the mechanism of the strip's +0.002 in q; the rate off A0 for random rows (BN-11); the chains' limit against λ_L; a Lean statement of the prefix guard; the transfer of the settling bound to the half-row (§16 Q1) | open | INSTINCT (Cloud, 5 November); CL744 addendum 2; CL750 addendum 2; CL751 |
| CP-2, BR-5 | The forced-zero half-line dynamics is not in general the free evolution of a whole-line configuration: solving outward from the wall gives a(1)(t) = a(−1)(t) at once and then a constraint whenever a(1)(t) = 1; `column_realizable_unique` solves the other way, inward by left-permutivity | PROVED (one line each) | §3.1 (ii), the remark after it; `Rule30Realization.column_realizable_unique` |

## 3. The three derivations

Notation as in design §4: depth k is position −k, the wall is depth 0 and is white for ever, F is the half-row step
new(k) = a(k + 1) ⊕ (a(k) ∨ a(k − 1)), bit i of the natural Y is depth i + 1. In the wall frame (design §4a) a row of
width W has its leftmost black cell at depth W, wheel j at tick t is the cell at depth W + t − j, and the recurrence
a(j + 2)(t + 1) = a(j)(t) ⊕ (a(j + 1)(t) ∨ a(j + 2)(t)) is F read along the diagonals. These are the kit's conventions
(`Rule30ZeroBoundary`, `Rule30FiniteDiagonals.Ld`, `Rule30AgedLeftDiagonals.Recurrence`); nothing new is defined.

### 3.1 CP-5: the two ends do not meet, and what passes between them

**(i) Causality runs one way (PROVED).** The recurrence reads wheels j − 2, j − 1, j to make wheel j: the value of wheel
j at tick t is a function of wheels 0 to j at tick 0 and nothing else (induction on t; this is `agree_step`'s content).
The wall is depth 0, which at tick t is wheel W + t. So wheels 0 to W − 1 never read the wall at any tick: the
half-row's wheels below W coincide for ever with those of the whole-line evolution of the same finite row, whatever is
placed to its right. The wall's forcing at tick s enters wheel W + s and from there only wheels ≥ W + s at later
ticks, so its influence at tick t is the union over s ≤ t, wheels ≥ W, which is depths ≤ t: the light cone. Nothing
the wall does can reach the band below wheel W, and nothing it does reaches a wheel J ≥ W before tick J − W.

**(ii) The wall is a reset (PROVED, one line).** Extend the wall frame above the wall by white. The recurrence would
give the new wall cell, wheel W + t + 1 at tick t + 1, as a(W + t − 1)(t) ⊕ (a(W + t)(t) ∨ a(W + t + 1)(t)) =
a(W + t − 1)(t) ⊕ (0 ∨ 0) = the depth-1 cell at tick t. The zero boundary forces it white instead. So the forced
dynamics is the wall-frame recurrence with one white reset per tick, at wheel W + t + 1 at tick t + 1, which changes
something exactly when depth 1 is black at tick t; for a survivor that is every even tick, since bit₀ is depth 1 and the
survivor condition is bit₀ = 1 at even ticks. The reset wheel is never reset again (at later ticks it is below the
wall and the recurrence reads it as the forced white). So every wheel J ≥ W is born white at tick J − W and follows the
recurrence from then on. In the kit's language the half-row's left side is a `Recurrence` array with a single reset per
wheel on the diagonal J − W; `Rule30AgedLeftDiagonals.reset_inherits` and `Rule30LeftReset.white_shift` are about
exactly such resets.

*Remark, for CP-2 and BR-5.* Solving outward from the wall instead: the wall's own update 0 = a(−1)(t) ⊕ (0 ∨ a(1)(t))
gives a(1)(t) = a(−1)(t) for every t, and column 2 is then determined by column 1's update only when a(1)(t) = 0,
otherwise a constraint a(−1)(t + 1) = 1 appears. So the forced half-line dynamics is a whole-line evolution only when
those constraints hold; `column_realizable_unique` is the other direction, inward by left-permutivity, and the two
should not be confused in BR-5's information class.

**(iii) The band and the wall part company (PROOF-SKETCH for the half-row; PROVED whole-line).** The kit's forced front
climbs at most one wheel a tick (`walk_one`: a black cell moves the walk on by one, a white one holds it), so from
wheel 0 at tick 0 it reaches wheel J no earlier than tick J, while the wall passes wheel J at tick J − W. Every wheel is
therefore born, and settled into following the recurrence, before the forced front arrives at it. The whole-line
theorem (`forced_front_four`, through wheel 87,866) says wheel j carries its strip from the forced tick F j, about 2 j on
A0; if its induction uses the recurrence at wheel J only from the front's arrival at J − 1 (design §16, question 1), it
applies verbatim to the half-row, and the half-row's left side is universal with the same bound. The measured band
edge is far ahead of the forced front, at about 0.757 t wheels at tick t on all sixteen rows (atlas §21.6) and on random
rows (CL742): in depths that is W + 0.243 t, so the chaotic region between the band edge and the wall is about
W + 0.243 t cells wide and grows for ever. The "meeting point" of the owner's phrase does not exist; what meets the
wall is the chaotic region, fed from below by the strip through the edge.

**(iv) What the band sends up is fair in every statistic measured (MEASURED).** The error field above the edge carries
structure in its first two wheels only (CL740 addendum); a damaged row's edge has the random background's statistics to
0.003 in every number (CL741 addendum 3); the strip itself is fair in every spatial and temporal statistic checked, to
0.001–0.003 (five-bit windows, the XOR below a white bit 0.50009 on 14.3 million bits, run hazard flat, runs geometric:
CL743–CL744), with one excess of 0.002 in the edge's stall hazard, uniform over the 32 phases and rising with stall
length, mechanism open (CL744 addendum 2, CL745 addendum 2).

**(v) What the wall sends down (PROOF-SKETCH and COMPUTED).** By (i) the wall's influence stays at wheels ≥ W, which the
band reaches later; by the branch law the band's eventual strip and phase at a fork are fixed by the chaotic region's
state at the tick the walk clears the fork (atlas §21.10, 24 of 24), and 48 random completions of the seed's prefix,
twelve sharing only the first cell, all settle on A0 (atlas §21.11). So the wall's forcing can change which left side
and which phase the configuration gets, and nothing else about the left side.

**What is left for CP-5.** A "joint constraint" can only be a property of the free bits (the column at depth 1 at odd
ticks, design §4) implied by the band across W + 0.243 t cells of chaos whose every measured statistic is fair. Stating
that exactly, classifying it against gates 8, 9 and 11, and naming the exact invariant of the chaotic region it would
need, is a logician's task. No such invariant is in the record. A prover follows only if one is named.

### 3.2 AM-3: the nearest difference moves at speed one

Let Y, Y′ be two rows and δ_k(t) their difference at depth k. From F, δ_k(t + 1) = δ_(k+1)(t) ⊕ [(a(k) ∨ a(k − 1)) ⊕
(a′(k) ∨ a′(k − 1))]. Where both rows agree at depths k and k − 1 the bracket is 0, so δ_k(t + 1) = δ_(k+1)(t). Let
d(t) be the least depth with δ ≠ 0. At depths k ≤ d − 1 both rows agree at k and k − 1, so δ_k(t + 1) = δ_(k+1)(t),
which is 0 for k < d − 1 and 1 for k = d − 1: d(t + 1) = d(t) − 1 exactly, whatever the rows hold beyond d. (PROVED.)

Consequences. Two naturals whose lowest differing bit is i (depth i + 1) differ in bit₀ at tick i exactly, so for even
i at most one of them survives tick i: two survivors through tick t never have their lowest differing bit at an even
index ≤ t, which is §4's free and check bits seen from a pair. Flipping bit i alone flips bit₀(F^i(Y)) for every Y, so
bit₀(F^(2s)(Y)) = bit_(2s)(Y) ⊕ g(bits below), the check at even tick 2s is linear in bit 2s, and S_W(t) =
2^(W − ⌊t/2⌋ − 1) for t < W is this count; beyond t ≥ W the check falls on a bit the row does not have and becomes a
condition on the existing bits, which is CT-2's check sum. For AM-3: a splice whose lowest changed bit is i changes
bit₀ at tick i and enters every check from tick i (odd i) or i + 1 on; keeping the spliced row alive for ever is Q01 at
that row. The only check-preserving operation the record holds is the forward orbit (AM-1, CL637 with GC1883/CL638).
At the other end, in the ordered band, the analogous operation is the chink, and every chink spills (atlas §21.10).

### 3.3 HX-2: the left side cannot separate the seed

`Rule30FourLeftSides` places every configuration with a leftmost black cell on one of four strips through wheel
87,866 after a shift (PROVED, kit). The sixteen left sides below 894,235 are the branches at the forks of that tree,
each reached from the single seed by one flipped cell at the fork's child (COMPUTED, 15 of 15, atlas §21.10), and
random completions of the seed's first P bits, P = 1 to 20,000, end on A0 in 48 of 48 cases (atlas §21.11). A
truncated-ether witness is a finite configuration and so carries one of these left sides; the seed carries A0 with
its phase. An invariant P that holds of the seed and is preserved by evolution and is a left-side property is
therefore shared with witnesses on A0, which the random completions show to be the common case. P must be a property
of the interior or of the right side; the record's pointwise seed-specific structure there is Local's right wall and
route graph (L1554–L1557), with no entry rate yet. `seed_perturbation` (whole-line, perturbing the left half beyond
−n) is consistent: it changes the left side far out and the column after time n.

## 4. Additions made in draft 3

- **§4a, aliases and name checks.** Five objects under their names, frames and statuses, so that a record skeptic's
  KNOWN verdict can cite the matching name. Every theorem name the document uses was checked against kit main
  `5ad29d6` (§8): all defined, with `IntegerForm` a namespace in `Rule30ZeroBoundary.lean`, `death_time_52_exact` a
  portal theorem (R30-20261023-8e6bd3) rather than a kit one, and `white_shift` in two modules.
- **§8.0, known inputs and anchoring.** The rule, the restatement, the KNOWN screen, and the split of what each kind
  of agent sees (attack agents: brief, §4, §4a, §6 only).
- **CP-5 rescoped; AM-3, HX-1, HX-2, R-04, LN-09 given their inputs.** As in §2 and §3.
- **Door seeds (§9):** the chink as a switch and the switchboard; the branch law; the prefix guard and its Lean shape;
  which left side a configuration gets; the strips as fair fields; the wall as a reset.
- **BN-11:** the rate off A0, 300 random left-finite rows through the two forks, with the chink tests as controls and
  a prediction (at most 5% leave A0). It answers the one open count in the prefix question (0 of 48) at a known cost.
- **P13–P15.** My own predictions on the swarm's behaviour, to be judged with the others.
- **Two questions for Local before the freeze (§16):** the hypothesis of `forced_front_four` (settles CP-5 input iii and
  opens a small kit statement), and whether the launcher can withhold the design document from attack agents.

## 5. Cuts, with reasons (question 1)

Cut first, before draft 2's core order, 56 → 48 in Wave 2:

| Cut | Why |
|---|---|
| BR-4, undecidable family | A reduction from a known undecidable problem is a project of weeks with an encoding to design; one agent returns a sketch nobody can check. GPT already scoped what undecidability would and would not exclude; that scoping is the door card |
| BR-6, proof complexity | Proof-size growth with W is a measurement with no question it answers for us; "does anything beat 2^(W/2)" is answered by the certificates' own sizes in the record. Keep BN-08 if a lens asks for it |
| PE-3, all periods at once | "Any argument uniform in the period" names no object; the T + P ≥ 16359 question belongs in PE-2's reductions |
| P3-2, upper bounds | Algorithm engineering with no grip in the record and no portal entry to react to beyond what P3-1 and P3-3 read |
| LN-05, LN-07, LN-12 | Lenses whose field names no object in the record (Padé, Christol–Cobham, pressure on K); the critic's list stays in §9 for a later swarm when a reader finds the object |
| XP-1, spectra | Its content is BN-04, a bounded computation with a control; it needs no reasoning agent |

Kept against my first instinct: CT-2 (the check sums; the most likely door to be shut wrongly, §7), AM-5 (the
noninvertible endomorphisms are a real question once the automorphism fact is in the brief), BR-3 (the planted
survivor is the only barrier task with a constructive output), XP-4 (the rule census is the cheapest unforced
structure), and all four fresh eyes.

## 6. Answers to the six questions

1. **Cut or extend.** §5. Extend by BN-11 only; the roster does not lack questions, it lacked inputs.
2. **AM-3, CP-5, missing doors.** §3.2, §3.1, §4. CP-5 as drafted would have spent a prover on a meeting point the
   record says does not exist; as rescoped it is one logician. AM-3's forever guard is Q01 itself by one line.
3. **Anchoring.** Three anchors in the shared text: the predictions table (an agent told P1 = 0.97 writes a
   negative); the "two ends' meeting point" phrase (an agent told to find a meeting finds one); and §4's survivor
   table beyond the proved range (a coin picture). Draft 3 withholds the design document from attack agents (§8.0),
   so they see §4, §4a, §6 and their brief; the fresh eyes' page omits §4's count and amplification bullet and the
   table beyond t < W. Keeping the fresh eyes fresh also means the record skeptic reads them last, not first.
4. **Models and cost.** Fable's weekly limit is an account limit and Cloud's sessions run on Fable under the owner's
   account, so I treat it as shared until the usage page says otherwise; the 17% read at 21:24 GMT includes Cloud's
   day. Opus by default; Fable for at most twelve slots named in the design §13; the swarm's Fable use capped at a
   quarter of the week so that the reads of what it produces are not starved.
5. **SW-01's failures.** Two not in the §1 table. The vocabulary problem (one object, several names), now a row.
   And the judges' censuses: SW-01's cheapest lesson came from tiny exact counts the judges ran themselves; draft 2
   confines computation to Wave 4, so let readers and screeners run `ref.py`'s smallest cases in Waves 1 and 3 under
   the compute rule, at the cost of seconds.
6. **The bet.** §7.

Local also asked for a check of the HX-1/2 scope, the diversified pilot, the theorem-versus-diagnostic screens and the
launcher contract. HX-1/2: right in scope; their inputs are in §2. Pilot: AM-1, AM-4, CP-1, HX-1, P2-2 sample five
shapes and I would not change it. Screens: right, with one addition, that a KNOWN verdict cites §4a's matching name.
Launcher contract: sound; the one gap is §8.0's withholding, hence question 2 in §16.

## 7. The bet (question 6)

**CT-2, the check sums, is the door most likely to be shut wrongly.** CT-4's bound is a limitation of one unsigned
estimate: with every nonempty subset bias ≤ ε it loses relative control near m = n/2. A screener who reads that as a
theorem will shut CT-2's conditional version, the bias of one more check given the earlier checks, which the unsigned
bound does not cover and which is the version that could iterate. Second: AM-5, shut by the automorphism fact
(identity and complement) when the question that remains is the noninvertible endomorphisms. Third: CP-5, shut as
"no joint constraint" without recording that the question was never a prover's and that the five inputs of §3.1 are
the reason.

## 8. Checks completed, and not

- Read in full: the design, draft 2 (758 lines); GPT's review GC2686; L1558, L1559; atlas §21.6 to §21.11; the kit's
  module docstrings for `Rule30UniversalLeftSide`, `Rule30FourFronts`, `Rule30HealingBound`, `Rule30RootedFront`,
  `Rule30AgedLeftDiagonals`, and the statements of `universal_of_strip`, `child_white`, `seed_perturbation`.
- Kit clone fetched to origin/main `5ad29d6` at 22:10 GMT, two commits past GC2686's `9af60de9` (#186, #187, period-3
  and period-4 skeleton modules). Twenty-six names checked by `git grep` for a defining line: all present, three notes
  (§4). `Rule30ErrorEdge` is on main with its thirteen theorems.
- `record_find` on chink, switchboard, prefix question, damage front, error edge: RECORD-MAP rows CL741, CL748–CL750;
  atlas §21.6–§21.11; PRIOR-ART CL740–CL741. `known_find.py`'s PR index returns 403 on Cloud's host (unchanged);
  GC2686's read of 13 open PRs stands as PR coverage.
- Not verified: whether Fable's weekly meter is shared across the owner's sessions (a working assumption, §6 Q4); the
  full hypotheses of `forced_front_four` beyond its docstring (§16 Q1); Local's right-wall statuses, cited as Local
  gives them. The derivations of §3 are Cloud's hand proofs and PROOF-SKETCH where marked until read by Local or GPT,
  except the one-line facts, which any reader can check against F.
