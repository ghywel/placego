# Rule 30, Prize Problem 1, period 2: where it stands

*A handover, written 2026-10-05 so that the work survives a move of compute, a new machine, or an outage. For a
person, or for an assistant given this file: read it, then the documents it names in the order given, run the
checks at the end, and stop. Do not start an experiment you were not asked for. Run `git log --since=2026-10-05` to
see what moved after this was written.*

*The proved statements, each with its proof and provenance, are collected in PROOFS.md (started 2026-10-06 at the owner's instruction). What is open, running, done or closed: the status board in §6. It is kept current; the rest of this file is the
record.*

## 1. The question

Wolfram's Rule 30 Prize Problem 1 asks whether the centre column of Rule 30, started from one black cell, ever
becomes periodic. The work here attacks it **period by period, for every finite starting configuration**, which is
stronger than the prize needs.
- **Period 1 is closed.** Condrey proved that no nonzero finite configuration has an eventually constant centre
  column (arXiv:2609.09431, 2026-09-08).
- **Period 2 is open.** That is the case worked on here: can a finite configuration's centre column be 0101...
  from some time on? Condrey's own conclusion names it as the next unresolved case.

In coin terms (RULE30-PRIZE.md, "The three questions, as a coin"; added 2026-10-08): read the centre column as a coin,
black heads and white tails. Period 1 asks whether the coin can land on the same face forever, and Condrey proved it
cannot. Period 2 asks whether it can settle into heads, tails, heads, tails, forever. That is this file's question.

Rule 30 is $x_{t+1}(i) = x_t(i-1) \oplus (x_t(i) \lor x_t(i+1))$. It is permutive in its left neighbour, so it can be
run sideways: given columns 0 and 1 for all times, every column to the left is determined (the *forced left half*,
RULE30-PRIZE.md §5).

## 2. The chain of statements

Each line implies the one above it. Section numbers are in RULE30-PRIZE.md.

| Statement | Where |
|---|---|
| **Prize Problem 1, period 2**: no finite configuration has its centre column eventually 0101... | §1, §8 |
| **B**: no finite right half makes the forced left half for 0101... eventually zero | §8, §8.11 |
| **LR_m** for some layer width $m$: no input to a width-$m$ layer next to column 0 makes it eventually zero | §8.11 |
| **LR (= LR_0)**: no column 1 at all makes the forced left half eventually zero | §7 |
| **R(d) is finite for every d** (equivalent to LR, by König's lemma) | §8.36, PRIOR-ART |
| **The doubling conjecture**: R(d) <= d + 4 | §8.36 |

R(d) is the longest zero run of the forced left half that starts at depth d, over every column 1.

The same question has several exact forms, each checked against the others by a probe:
- **The forced walk** (§8.37). A zero run from depth d is one deterministic walk per prefix of column 1: at every
  other cell, column 1's newest bit is forced.
- **The wall form** (§8.39). Run Rule 30 on the half-line $x \le -1$ against a wall at $x = 0$ that alternates
  white and black. The forced left halves are exactly the evolutions in which the cell beside the wall is black at
  every odd time.
- **Black, white and both** (§8.40). At the wall's black times the condition involves the left half alone. At its
  white times it couples the left and right halves. A finite configuration must keep both.

Known theorems used:
- **Jen (1990), via Kopra**: two adjacent columns of a configuration with an eventually zero left half are never
  both eventually periodic. So no eventually periodic column 1 can work (Proposition 7, §8.13).
- **The channel bound**. Next to 0101..., column 1 carries at most about 0.12 bits per visible bit (certified 0.1236
  at $m = 28$, 0.0618 per step, since 2026-10-06),
  whatever the right half. The figure is 0.128 by power iteration (§8.20), certified as 0.1292 in integer
  arithmetic (§8.33).

Proved here (2026-10-05, Local; each is elementary and has a pre-registered check):
- **Theorem A, Jen with a clock** (§8.54). Two adjacent columns cannot both be $P$-periodic on a window $[a, b]$
  unless $b \le 2a + L + 2P - 1$, with $L$ the distance to the left edge. Jen's theorem is $b = \infty$.
- **Theorem B** (§8.54). With $P$-periodic columns 0 and 1 ($P \ge 2$), no zero run of the forced left half is
  longer than $2P - 2$.
- **Theorem E** (§8.57). If column 1's visible bits are a Sturmian sequence, the forced left half is never
  finite. So LR holds for every pure rotation, rational (Jen) or irrational.
- **Theorem A′, the window principle** (§8.58). A block of two adjacent columns recurs at time $a'$ only if its
  length is at most $L + a'$. It contains Theorem A and has a two-line proof. Its Collatz twin is Terras's
  bijection (COLLATZ-PRIZE.md §5).
- **Lemmas B1 to B3, Theorems A‴ and A⁗, Corollary F** (§8.59). The left diagonals' periods are unbounded, so
  infinitely many diagonals are black for ever; a repeat of the trace, being a white run in the later row, stays
  a growing distance below Theorem A′; a column 1 that begins with near-squares at unbounded periods is excluded
  with any left half; the settled band has no white run longer than twice its period, so a repeat's white run
  cannot lie in it.

## 3. What has been measured

All numbers come from probes whose predictions were committed before they ran. Each probe's header records its
OUTCOME.

- **R(d), exact** at depths 1 to 61, 65, 69, 73, 77, 81, 85 and 89 (§8.36, §8.37). R(89) = 75, R(d) <= d + 4 at every
  depth, and R(d) - d is about -0.16 d.
- **Distinct forced walks** at depth d (§8.38): about $2^{0.41 d}$. Each free bit multiplies them by 1.764, not 2,
  because about 6% merge at every step.
- **The record is the best of those walks** under coin flips (§8.38): $R(d) \approx 0.826\,d + 0.8$. This
  predicts depths 49 to 81 within 4.1 cells.
- **Column 1 next to 0101..., from a real right half** (§8.4 to §8.11): the wheel $U$, an exact coding of the
  rotation by 17/56, kicked by domain walls in notches of 1/28 turn.
- **The best finite seed for 0101** (§8.24): its total width plus at most 9 steps, for right halves up to 32 cells.
- **The same for every word up to period 4**, and for a random word (§8.42): total width plus +6 to +10, growing
  like a logarithm of the depth.

## 4. Routes closed (do not reopen without new evidence)

- **Bounded runs from a thin layer**: at every layer width up to 16 the zero runs still grow with depth (§8.14).
  So no local rule of column 1 bounds them (§8.41).
- **Periodic column 1**: settled by Jen's theorem (§8.13). The 550,201 periodic words searched were a check of the
  instrument, not evidence.
- **"Structured families" beating chance**: luck (§8.16).
- **The entropy squeeze as a reduction** (§8.33). It restates the problem. It needs a lower bound on a column's
  entropy that nobody has.
- **The SAT crib** (§8.37): correct, but slower than enumeration.
- **A merging lemma as the easy half** (§8.38, corrected). A merge needs black cells, so it is the original
  problem's flavour again.
- **A Chebyshev-type exact identity in the survivor counts** (§8.41): none is visible.
- **"Periodic words hold deep zero runs down"** (§8.42): refuted.
- **The wheel's rigidity as a bound** (§8.44). The kick game's runs grow like the coin's. The timing cuts them, but
  does not stop them.
- **Self-similarity between depths d and 2d** (§8.36, RC5): none beyond chance.
- **Q6's closed methods** (second triage, 2026-10-08, CL065; each closed as a method only, GC614.1). Shallow
  fixed-source interception (SO with GC591). The one-ray streak census (GC592). Persistent parallel compensation
  (GC597). Finite-age compensation (GC598). Bounded restart counts (GC599). The age-cutoff and phase-mask
  refinements (GC601). Still open: joint compatibility of late, restarting interior sources with the actual clock.
- **Q7's affine waiting envelopes** (GC596; second triage, 2026-10-08): they give a slope below 3 only at dyadic
  periods up to 4.

## 5. The one missing statement

Every form of the problem ends at the same sentence: **keeping the wall's conditions costs real information.** The
delivery side is a theorem (the channel bound). The cost side holds exactly only next to a constant wall. There
column 1 can only turn black once, and that is Condrey's proof. Next to 0101 it holds only as a coin model: each
condition costs about one bit, and luck adds a logarithm, as in Cramér's model of prime gaps (PRIOR-ART, the owner's
zeta note).

**Why it is hard.** The measured law holds for a random centre word as well as for periodic ones (§8.42), so a proof
cannot come from properties every word shares. It must use what is special about periodic words, as Jen's theorem
and Condrey's proof do. The one structure found that exists only next to the 0101 wall is **the wheel**: no other
trace tried turns a wheel of its own (§8.8). The likely shape of a proof is a size argument, like Chebyshev's
proof of Bertrand's postulate, and not a proof that Rule 30 is random.

**Where it sits** (§8.45). The problem has the structure of Mahler's 3/2 problem: the left half is a free full
shift, column 1 is a thin constrained language, and the two must agree at the wall for ever. Mahler's method
proves emptiness only when the constrained side is finite, which is our Jen and Condrey cases. It stops where the
constrained side has positive entropy, as next to 0101. That is where Mahler's own conjecture has been open since
1968.

**What the other fields offer** (§8.47). A survey across biology, physics, chemistry, molecular machinery,
mathematics, computing, the long shots and the Game of Life found no field that holds the missing statement.
It found the same gap everywhere: theorems that holding a chaotic system costs information are about sets of
cases, and the prize is about every single case. The gap has been crossed only by finiteness and by extremal
arguments for single trajectories. §7 turns that into questions.

**Width-one template audited (GPT GC807, 2026-10-09; CL085 item 2).** Kopra's 2021
Proposition2.8 is already included in the later Theorem3.5: fractional multiplication has
$(h,d,w)=(1,1,1)$ and spreading speed $s=\log_{pq}(p/q)<1$ for coprime $p>q>1$.
The useful mechanism is periodicity propagating left faster than the nonzero edge, leaving a full
zero period behind and hence a permanent zero column. Rule30's established parameters are
$(0,1,2)$, so this gives the adjacent-column theorem. A width-one transfer still requires a new
hypothesis or reconstruction argument. Equality of the speeds is insufficient: the shift of a
single seed has an eventually zero fixed column. Detailed source receipt: PRIOR-ART.md GC807.

## 6. Leads and their status

**The status board** (updated 2026-10-09 19:27 BST; the time is from the shell). Every lead in this file, in RULE30-PRIZE.md and
in the mathematics table of CLOUD-LOCAL.md has one row here. When a lead moves, its row here and the tag at its
item change in the same commit. Nothing is deleted: a finished item keeps its text, and its title is struck
through.

The tags. **OPEN**: nothing settles it, and work can start. **PART**: part is settled, and the rest is named.
**RUNNING**: a job is on a machine. **DONE**: acted on, and the result is recorded. **CLOSED**: a dead route, or
settled by a theorem; do not reopen without new evidence. **BLOCKED**: cannot be done with what is here. **PARKED**:
a side question kept for its own sake in CONSTELLATION.md, not active work on the prize. **MERGED**: its open part
now belongs to the named row. The board grows to a
manageable size, then a triage returns it to its main line before it grows again; a new row names the main-line row
it serves, and a closed route is marked in the commit that closes it (the `expand-then-contract` rule in
WORKFLOW-SAVED-MEMORY.md, the owner's, 2026-10-06).

*The prize, and the routes to it.*

Active after the first triage of 2026-10-06, CL009 and GC155: Q1, 6.1, Q2, Q6, Q7, the Rule210 empty-left cancellation, Q9 and the Collatz
critical-boundary count loss, six on Rule 30 and two on Collatz. The clock-compatible finite-left support question
(G129, G140, G141) is part of Q7, not a row of its own (GC155).

Active after the second triage of 2026-10-08 (Cloud's draft CL065, GPT's agreement GC614.1, applied by Local in L326): Q1, 6.1, Q6, Q7 and Q9. Q2 is parked, the Rule210 empty-left cancellation is done (Proposition 19), and the Collatz critical-boundary count loss is merged into Q9. Portfolio question 4 (G239's neutral blocks and Local's NL) stays off the board by design, in CONSTELLATION.md section E: a zero or positive entropy of the clamped right-half language alone supplies neither Q1's signed cost estimate nor Q6's finite-left incompatibility (GC614.1). Nothing was deleted: each row below keeps its text and
its former status.

| Lead | Status | What has been done | What is left |
|---|---|---|---|
| Q1, the counting form (§5's missing statement; M1 in CLOUD-LOCAL.md) | **OPEN** (kept at the second triage, 2026-10-08) | Measured to width 26, and by right parts beyond width 100 (§8.51 to §8.53). Restated as a count of window contents (§8.58). Local, 2026-10-07 (L224, L225): the first right-paid step at position j has an exact width-free ratio rho_j (3/4, 3/8, 13/16, 3/32, ..., computed to j = 22; to j = 35 by ZR3, 2026-10-08, L316: its distance from 1/2 does not decay, 0.087 at j = 33, and the mean of log2 rho_j over j = 23 .. 35 is -1.024), and for T > j the count at position j is the zero-run distribution of the forced left half after a black cell at depth j, the average-case twin of §8.36's records. ZR, ZR2 (L236, `rule30_zero_runs.py`): those runs are cut off by exact local implications, not coins (after a black cell at depth j, at most 4, 2, 0, 3, 3, 2 white cells for j = 2 .. 7; depth 5 is black whenever depth 4 is), and the exact longest white run over every configuration, R_real(d), is computed to d = 19 (4 against the free-column-1 record 17 at d = 13; §8.12's gap, now exact). 2026-10-09 (Local DL and DL2, `rule30_edge_deadline.py` and `rule30_edge_deadline2.py`, L346 and L349; GPT GC637, GC639, GC660): GC637 shows that a uniform linear edge deadline T <= cj + b would give Q1 with alpha = 1/c. The measured per-slice horizons H(w, j) to w = 32 settle with H(j) - j <= 17 for j <= 22, but a five-width plateau at j = 16 broke at w = 27, so a plateau certifies nothing; only section 8.69's left-only ceiling, H - 1 <= H_L, does. GC660 proves the slice j = 1 exactly. 2026-10-09 afternoon: G249 (promoted, second-read by Local) bounds the right-prefix period growth for every finite seed, Q_j <= 2^ceil((2j - 1)/3), so the ordered right band grows at least about 1.5 diagonals per doubling of time; Local's UB (L383) measured the left band's staircase, identical on 21 rows, with P_e <= 32 to about 98,300 diagonals. | The proof. No known method reaches it. |
| 6.1, the wheel's kicks | **PART** (kept at the second triage, 2026-10-08) | Narrowed to a kicked rotation (§8.43). The wheel's rigidity alone is refuted as a bound (§8.44). The kick alphabet is local (Local's KL, 2026-10-07, PROOFS.md entry 26, second-read by GPT in GC359). GPT OLD1 (GC588, single-party boundary audit) qualifies the one-turn table: its 56 old transitions mean 57 observations; the shortest RD lock has 56 observations and its m=16 necessary projection additionally admits class 19, kicks -8..-4, with only 21 new observations fitted. This supplies no actual event and changes no settled alphabet. After 140 steps the alphabet is exact: class 12 certified impossible (Cloud's KS, Local's KK and DT), and every size of classes 32, 42, 52 realized (KX); PROOFS.md entry 27: for every right side, after 133 steps on the wheel, kicks occur only at classes 12, 32, 42, 52, with sizes +4..+8, +2..+6, +1..+5 and -6..-1; the two observed classes' alphabets are exactly the measured ones. Cloud's KB and KS (2026-10-07, after the owner's "bite" steer): class 42 does occur, 67 of 20,282 settled kicks from 80,000 right halves (KB); class 12 cannot occur for any right half, finite or infinite, with any history, once column 1 has run the wheel for 140 steps (exact: satisfiability over column 1's light cone, with positive and negative controls, every model replayed; KS). It is still possible at 56, 84 and 112 steps (56, 43 and 15 of 56 phase cases). Entry 26's automaton allows it because the obstruction needs the rule followed exactly out to column 37 (alive at width 36, dead at 37). The kick game (§8.44) had already left class 12 out from the data, so its coin law stands. GPT's second-read G205 (GC373/GC374) phase-graph certificates force column2 at the centre of any13-observation wheel window and columns2..4 at the centre of any143-observation window (even wheel phases, arbitrary right exterior). Fixed-depth forcing, not a locking-speed theorem. Width 15 forces columns 2..6 next to the wheel (LK, L236; GPT's G208). Entry 28 (Proposition 15, hand proof, GC389): a kick lands at an angle of the take-off's parity and the opposite colour, just after a white, so forward kicks from even white take-offs land on the wheel's even black arc, 44..54 (CL031's window), with at most six sizes. 2026-10-09 (Local KT2N, `rule30_kick_strain_32.py`, L375): class 32 is SAT at N = 392 and 448 in both cases under 12-hour caps, every model replayed, so after 448 steps on the wheel classes 32 and 52 are still possible and class 42 is dead by 560. | The interior's choice among the sizes (at most log2 6 bits a kick), what out at column 37 forbids class 12, whether the wheel's options keep narrowing as it runs longer (KS strain: class 42 is dead at N = 560 in all 56 cases, drat-trim verified, KT2C 2026-10-08, so Cloud's KT-P3 holds; classes 32 and 52 are SAT at 336 and UNKNOWN at 560 under 4-hour caps, KT2L; KT2M 2026-10-08: class 52 is SAT at 448, model replayed, and class 32 is UNKNOWN at 448 in both cases under 4-hour caps); RV3 2026-10-08, rule30_three_gap_death.py: next to the clamped wall the 3-gap is still possible at T = 352 (SAT, replayed) and UNKNOWN from 354 to 1024 under one-hour caps, so no death time is certified. Its white branch dies exactly: window 10000 is last possible at T = 52 (UNSAT at 54, drat-trim verified), so seven white cells beside the wall at an even time are last possible at T = 50 (L289). 14 of the 32 five-site wall windows die (12 by T = 2), and 18 survive to T = 256, 10 of them not seen on the wheel's lock, and the cost side: a statement that the kicks must pay for the left half's conditions. Second triage (CL065): OLD1's class 19 needs at most 55 transitions and is unused by RB's 139,972 kicks (CL060); the main-line remainder is the cost side, which is Q1's statement. |

**GPT application guard, 2026-10-08 (GC412; Q1 remains OPEN):** toolkit119 controls one noisy Boolean readout. Two actual successive Rule30 observations already have positive conditional dependence, so summing their marginal information does not reconstruct or upper-bound their joint information. No deterministic count-loss certificate follows; see RULE30-GPT GC412.

**Cloud update, 2026-10-08 (CL033, RV `rule30_cloud_visible_gaps.py`; 6.1 remains PART):** read at the wall's white times, the wheel's column 1 has zero gaps 4, 4, 4, 4, 2, 4. The six even classes left after one turn are the third zeros of its five 4-gaps and the 1 ending its 2-gap; GC502 and GC503 (second-read in CL033) bar the other even classes, given column 2 black at gap starts. Every even-class departure seen (51,045) is a swap of the two gap-start states (columns 2 .. 6: 11100 at a 4-gap, 10110 at the 2-gap): one cell, column 3 at a visible gap start, decides the kick, which shows 4 ticks later. Forward kicks are the 2-gap arriving early, backward kicks late. RV-P2 refuted, RV-P3 held; the swap reading is post-hoc. No bound on the kicks follows. RV2 (CL037): every one of 19,177 kick transients stays in the wheel's two gap lengths, 2 and 4, so a kick moves the 2-gap and nothing else; and over 189,968 gaps of real right halves next to the wall a 3-gap occurs once (time 214), though GC503's trigger for it is common in random rows. Its exact death time is the next question.

**Local update, 2026-10-09 (KT2N, `rule30_kick_strain_32.py`, chat L375; 6.1 remains PART):** class 32 is SAT at N = 448 in both cases, with 12-hour caps and every model replayed (it was UNKNOWN there under KT2M's 4-hour caps). So after 448 steps on the wheel, classes 32 and 52 are still possible and class 42 is dead by 560 (KT2C). Nothing above 448 is decided for class 32.

**GPT update, 2026-10-08 (GC407; 6.1 remains PART):** independently reviewed G209/G210 prove the short anchored implication by hand. At the last class12 front, anchor2..6=11100 at s-14 and5(s-2)=0 force6(s-6)=0, explaining one necessary exterior defect. The reference does not renew this anchor after12 steps; no long preparation bound or explanation of death127 follows.

**GPT note, 2026-10-07 (GC382–GC384; 6.1 remains PART):** the exact width13 relaxed core still permits both column5 choices, but every phase12-to14 two-edge path pairs them00 or11. A conservative175-observation transfer of that correlation is proposed for independent review; no column5 uniqueness or growing locked region follows.

| ~~Minimal-counterexample finite-predecessor descent (GPT G121; Cloud CL005)~~ | **CLOSED**, G121 to G124; stopped by agreement (L077, G128); G141 exposes a boundary gap, not a descent (first triage of 2026-10-06, CL009 and GC155; was: **PART**, G121-G122 verified by Local L077; G123-G124 verified by Local L078) | Span grows by2; finite injectivity gives a unique root/age. Eventual-alternation counterexamples reduce to roots, but3/4 of normalized words at every width>=4 are roots. The single-cell seed is already a root. G122 locates the exit:unique right-quiescent inverse has a black left tail,then spatial period3;G123 proves all-depth unbounded ancestor-tail periods (p_n>=ceil(log2(n+1))) and infinitely many divisibility increases;G124 classifies least spatial periods of periodic zero-reaching rows as 1 or 3*2^k, all realized; temporal-wall incompatibility is not established. | A different shrinking transformation preserving eventual alternation,or exclusion of all roots. Inverse-time descent alone cannot complete width induction. |
| Q2, the move to a finite window | **PARKED** at the second triage, 2026-10-08 (CL065, GC614.1): no first step named since 2026-10-05; reopen on a concrete condition that is not local in column 1 (was: **OPEN**, not started) | Nothing direct. Theorems E and E″ (§8.57) exclude classes of column 1. They do not force periodicity. **Drawn 2026-10-09 (Local):** the natural condition on column 1 that is not local is the one-hole language at p = 2, the channel of §8.20 (a sofic constraint on column 1's visible bits). It bounds the entropy (0.1236 bits, §8.33) but does not force a finite window, so it is not the reopening condition. OHC reproduces §8.20's channel at every width to 22 (XC, an independent check). | A condition that is not local in column 1. |
| Q3, a machine-found certificate | **CLOSED** (§8.61) | Assessed before any encoding: a certificate is a potential falling at every forced cell; walks of length 0.83 d from every depth force it to be linear in the seed, and a potential of that kind is the bounded-debt statement of Q1 written as log N. Not a separate route. **Reopened and closed again, 2026-10-09 (Local, a drawn row):** the named finite family is entry 38's strip-graph certificates of radius R, the one family that did find exclusions (black-end walls 0 1^q, q = 7 and q >= 9). For the period-2 word 01 it holds no certificate up to radius 9: the cyclic component forcing neither neighbour grows 84, 150, 264, 456 (RG, rule30_rung3_strip.py, L488). The same holds for every word of period 3 .. 6. | Reopen only with another named finite family; the strip graphs of radius <= 9 are searched and empty for period 2. Radius 10 needs a C or memory-lean version, and the component's steady growth suggests it would not help. |
| Q6, LR refuted by construction | **PART** (kept and compressed at the third triage, 2026-10-09) | **On 2026-10-09:** the realizable records R_real(d) to d = 97 are DRAT-certified (Local's RRC) and re-checked by the verified checker cake_lpr (VC); Cloud's RR3 decided d = 98 .. 106 (98 = 14, 99 = 13, 100 = 15, 101 = 15, 102 = 14, 103 = 14, 104 = 13, 105 = 13, 106 = 12; nothing above 15) and runs on from 107 on the M5 since 2026-10-10 01:13 (L515), which has decided 107 = 14 and 108 = 16 and confirmed 101 = 15 and 105 = 13 by the solver; RK93 (the exact free-column-1 record R(93)) runs on the NAS, about 40% (6,462 checkpoint lines at 19:21). Critical all-L uniqueness is bounded and certified (CX and CXE, 100 UNSATs, cake_lpr-verified). The selector-parity and front lemmas G.GPT259 .. G.GPT268 (PROOFS.md E2), with G264's exit refinement; GC828's retained template passes a K = 6 periodic coupling gate (TC, L452) but no ring of up to 30 cells carries it (L463, Cloud's RD). GC848 excludes same-reference-orbit phase backgrounds at p = 310 by exact phase pumping (second-read by Local L474; G.GPT270). GC849 gives the corresponding temporal-quotient no-return condition; downstream backgrounds remain open. GC853/854 restrict first exits to 121 then 56 free ticks (exact two-/three-edge projections only; no surviving-bit coupling). **GPT, 2026-10-10:** GC1017 derives the two-gap train's six-column slab and its column-7 white-phase constraint by correlated local deductions (proof sketch, controls pass); mixed entry/exit compatibility is still open. GC1020 proves the specified finite right seed1001 keeps that train forever by causal P8 feedback at site14 (PROVED, second readings CL189/L595); the clock remains externally clamped, and the all-depth record bound is open. GC1023 derives all-length train exits4,5 from existing short absences and corrects CL190 entrance4/5 with an actual startup gap3 witness; GC1024 gives an actual ten-cycle follower separation (56-bit future), while prefix-conditioned forgetting remains open. **History:** this row as it stood before the third triage is in RULE30-PRIZE.md §8.78, verbatim. | An actual inter-run compatibility input with unbounded reach; the retained template's infinite right extension and its connection to the aligned left reference (GPT's route map GC845; the finite 2^310 entry-graph bound gives no practical closure horizon); deeper records (RK93; RR3 from d = 107). **Cloud, 2026-10-10 (TR):** the decided records climb about 0.085 a depth over d = 30 .. 116 (no shuffle of 2,000 reaches the slope); the exact L = 18 test at d = 140, 148, 156, 164 ended UNKNOWN at 13,321 s each (14:30 stop, no cap increases, CL188); the uniform-ceiling target (R_real <= 17) is replaced by finiteness at every depth, for which a linear bound suffices; the depth frontier is CUT's (Local, L585 .. L591) and RR3's. **2026-10-10 15:20 BST (L596, CL191):** R_real(152) >= 18 by an explicit configuration found by CUT, simulated three ways; the ceiling 17 is refuted outright and TR-P4 held; the target is finiteness at every depth. |
| Q7, the regime between | **PART** (kept and compressed at the third triage, 2026-10-09) | Kicks cannot thin out faster than geometrically (Theorem A); Sturmian, near-square and other structured column 1s are excluded (Theorem E, Corollary F, A⁗, G131, G132). Settling on a rooted history reduces to two gaps (G164, G165, G184): gap 1, a stage budget O(q) at each dyadic period q, and gap 2, period growth R_j to infinity, which is open; the named q = 8 and q = 16 components are closed (finite evidence), and GC652 .. GC702 give the exact debt identity at mismatch endpoints. **History:** this row as it stood before the third triage is in RULE30-PRIZE.md §8.78, verbatim. **2026-10-09 evening (Local, RC88 and RC16, a drawn row):** the rooted returns are now censused over all odd sources and child choices. At q = 8 every walk returns, only at r = 88 and 371, each one rotation class, so there is no other r88 component. At q = 16 there are nine return depths to 60,000, each one class, and r = 52,808 is unique; QX (D1 exits and D2 successors on all six even returns, after PR196's control 5 passes at each) and QX2 (every exit path followed until it dies, at most four steps) close all six: every rooted even return at q = 8 and at q = 16 is exactly its cycle. Every rooted q = 16 walk returns, the last at 214,006 (RC16X), with one first return per source orbit, so the q = 16 even classification is complete; GPT's GC861 confirms D1 and D2 apply. Every rooted walk returns at every fixed q (L487: the injective step plus a unique child of a nonzero driver; GPT auditing). At q = 32, 12 of the first 16 orbits return between 4.5e7 and 4.6e9 and 4 lie beyond 5e9 (RW, RWC). **Fourth triage (2026-10-10):** GPT's W280 .. W281 (GC896 .. GC917) give exact local facts, the one-bit driver response, same-child fibres, the sharp antiperiodic entry and its dense next profile, with no rooted bound (second-read: L510 .. L516, CL122 .. CL136); ZF's q = 16 tree repeats Proposition 8 (CL128). The single cell's own period-32 entry is sharp, so the universal one-parity exclusion is REFUTED (CL134, GC915); the sharp profiles run q/4, 3q/4, 3q/4, q/2 (CL138, second-read L520). | Gap 2 (normalized period growth); Thue–Morse and paperfolding for every left edge; Rudin–Shapiro; q = 32 and beyond; the odd returns (371 at q = 8; 6343, 29167, 44841 at q = 16); a rigidity argument for why every rooted even return closes. Affine waiting envelopes are closed as a method (GC596).  **GPT, 2026-10-10 (GC912/GC913):** single-profile and four-step pair-mask inverse shortcuts CLOSED; physical one-parity source exclusion **REFUTED** by CL134/GC915: the single cell's least-period 16 source is one-parity and its period 32 entry has weight 8. Q7 stays PART.  **GC914 (hand, review pending):** ambient mixed-parity odd sources attain entry weight q/4+1 for every dyadic q>=8; physical ancestry and stage bounds remain open. |
| Q9, the Collatz twin | **PART** (kept at the second triage, 2026-10-08) | (Later Collatz work, G49 onward, is tracked in the critical-boundary count-loss row below.) The least-residue lemma (COLLATZ-PRIZE.md §4). The window principle on both sides, W1 to W3 (COLLATZ-PRIZE.md §5). Exponential sums cannot reach a single case. The counting form keeps the coin's rate to w = 43 (L509). | The literature check (below). G29 independently validates signed odd-denominator scope/exact rounding, with infinite-distinct-orbit and shifted-height qualifications. G30 proves conditional slope at least1/gamma, gamma=(upper odd density)*log2(3)-1; zero gamma forces superlinear complexity. G31 exact odd-run cost; run-only shortcut to upper density<1 refuted by an abstract square-zero word (rational realization unresolved). G32 retains separate real/2-adic limits; G33 proves the known periodic geometric bridge and exact v2 full-repeat budget, with cycle exception. G34 excludes power-of-two zero positions by a necessary gap ratio<=log2(3); G35 additionally excludes the critical rounded-geometric ladder via accumulated even-step cost; square-zero inverse remains open. G36 verifies known lower-density bound from primary Monks–Yazinski; complement preservation is conjectural. G37 certifies that3/2-spacing budgets stay bounded; their sufficiency fails at start829. No general aperiodic rational-realization bridge. G38 gives an exact coefficient-survivor ternary Fourier recursion; conditioning/cancellation and the shared count bound remain open (single-party controls). G39 proves fixed-endpoint survival probability>=1/T and event transfer, but a character counterexample blocks automatic cancellation transfer; exact completion weights recorded (second-read by Local, PROOFS.md E2). G40 proves an exact cosine product inside survival-compatible adjacent-pair cubes; bounding their weighted aggregate remains open (second-read by Local, PROOFS.md E2). G41 controls free-pair mass for densities bounded above critical and below1; phase separation and boundary regimes remain open. G42 gives a primitive-harmonic family with n free pairs and modulus>0.99 for all n; this blocks uniform within-skeleton decay from pair counts, without deciding aggregate decay. Local independently audited G39-G42 (L007; PROOFS.md §E2). G43 derives exact binary-reader weights: the displayed resonance has weight<=2/3^a for one bit; multi-step weighted control remains open. G43 independently audited by Local L008. G44 proves the finite-ensemble tail-resolution boundary; a uniform all-cylinder coin comparison fails, while the special survival-count target remains open. G44 independently audited by Local L009. G45 derives word-specific actual-start ceilings and a residue-class count;65520 controls pass and Local independently audited it (L012). G46 proves formal ceilings unbounded and rejects dropping the short-interval +1 term; no summed bound. G46 KC controls pass256 cases and Local independently audited it (L014). G47 proves actual survival in the single-run first-deficit family requires a periodic return; 256 RC controls pass, finite return only start1. G48 FD controls pass791 words/2373 lifts, giving a single-party computed certificate when the first coefficient deficit is<=16 (onlystart1 survives); no general stopping-time estimate. Primary-source audit identifies the known CST target and adjacent-swap prior art; census block closed. No divergent orbit exhibited. A Collatz statement beyond these conditional bounds. Second triage (CL065, GC614.1): the Collatz critical-boundary count-loss row is merged here, with its open bias estimate. The carry-over audit of 2026-10-08 (CL066, GC616, second-read by Local in L326): the Pascal unrolling transfers to the real carry field; an age obstruction would also need an old-source spatial bound and a non-dyadic residual. |
| Rung 3, periods 3 to 6 (RULE30-PRIZE.md §6) | **PARKED**, other periods, behind period 2 (first triage of 2026-10-06, CL009 and GC155; was: **PART**) | Horizons measured for every word up to period 4 (§8.42). Theorems A, A′, B and E hold for every period. §8.62: the right ladder is freedom, not period; period 3 is two walls on opposite sides of it. **2026-10-09 evening (Local, RG, a drawn row):** entry 38's strip-graph certificate was run on every primitive column word of period 2 .. 6, at radius 6, 7, 8 and 9. No word passes. Each keeps a non-forcing cyclic component that grows about 1.75 times per unit of radius, as the period-2 word does. Rings do not explain it: no ring to n = 18 has such a column with longer-period neighbours. | A method other than strip graphs. A radius-10 C run (about 5 GB in Python) is the only cheap extension, and the growth suggests it would not help. |
| The two Condrey ends (§8.62; the owner's question of 2026-10-06) | **CLOSED** for the white end q >= 10 (entry 40) and the black end q = 7 and every q >= 9 (entry 38); **PARKED** for the white end q = 2 .. 9 and the black end q = 2 .. 6 and 8, behind period 2 (q = 1 is the 0101 wall itself; compressed at the fourth triage, 2026-10-10) | Black end 0 1^q: entry 38 (the strip graph SG at radius 6 plus Theorem A; GC806's lock and the wrap table WT for every q >= 17), reproved one-sidedly for q >= 14 (L497). White end 1 0^q: entry 40 (the one-sided width-8 relaxation plus Theorem A); entry 41 takes the same route to 139 more column words. Machine-checked in Lean: entries 5, 40 and 41 and the black end q >= 14 (TheoremA.lean, WhiteEnd.lean, JenRoute.lean). On the open cases: SGC fails to radius 11 (one non-forcing component, persisting from radius 6); the one-sided route fails to width 16; the one-hole channel keeps positive certified ceilings at p = 2 .. 7 and 9 (next row). GPT's G11 .. G19 (the latch lemma, shielding, the exact width-one to width-three languages, slow walls) stand as recorded. **History:** this row as it stood before the fourth triage is in RULE30-PRIZE.md §8.79, verbatim. | A cost for the second defect after the protected prefix (GPT's next target); whether anything at either end escapes the positive-entropy gap. |
| The one-hole channel layers (GPT G15-G17/G20; CONSTELLATION row16) | **PARKED**, other walls, behind period 2 (first triage of 2026-10-06; compressed at the fourth triage, 2026-10-10) | Widths 1 .. 4 are exact (G15 .. G17, G20): every odd p >= 5 is still free at width 4. Width 5 closes every odd p >= 11, and p = 8 (OH, TB; GC850's nine-step lock for p >= 10; Lean BlackLock.lean, P8Lock.lean), so the one-sided channel is closed exactly at p = 8 and p >= 10, entry 38's exclusion set. Exact plateau forms at p = 7 and 9 (GC857). Certified ceilings per hole (LP, integer certificates verified independently): the width-22 radii p = 3, 4, 5, 6, 7, 9 <= 1.220382, 1.231763, 1.471227, 1.383947, 1.599414, 1.714447; times Cloud's true forbidden words (TC), p = 5, 7, 9 <= 1.461900, 1.590415, 1.697625 (ODD3; rounded up from the integer certificates). Under random right halves the rates are positive (HE). Short free pairs break on long words (FP2: p = 9's (000, 001) at 30 holes). **History:** this row as it stood before the fourth triage is in RULE30-PRIZE.md §8.79, verbatim. | Does the one-sided entropy of p = 5, 7, 9 reach zero? The ceilings are upper bounds; a lower bound needs a construction realizing exponentially many hole words, with an extension guarantee (GC899's note to CL123). p = 3 and the even periods are separate. |


| ~~The reframing: next steps after Condrey without period 2 (§8.63; the owner's question of 2026-10-06)~~ | **DONE**, decided: CL005 and this triage (first triage of 2026-10-06, CL009 and GC155; was: **OPEN**, ours to choose (the owner's reset of 2026-10-06 09:20)) | Walls have two coordinates, freedom and switch density; 0101 switches every step, the farthest wall from Condrey's, which is why only it turns a wheel. The slow walls $0^a 1^b$ are the natural next family. Measured at fixed freedom: no fall of LR's law of the predicted size with switch density (0.81, 0.81, 0.67, 0.79 against 0.83; an effect stays unresolved). From the left (§8.69, `rule30_leftside_horizon.py`): a left seed narrower than about the period $a + b$ dies before two consecutive black stretches next to $0^a 1^b$ (passing widths 13, 17, 23 for $a = 4, 8, 16$ at $b = 8$); the 0101 left-only horizon is $W + 17$. GPT's §G15, §G18, §G19 (G18 and G19's scripts replicated by Local, 2026-10-06, at edce038: every verdict as recorded): the exact injection rate $\log_2(a+1)/(a+b)$, a reset theorem for $b \ge 3a+1$, a latch obstruction on balanced walls; G25 transfers latch coding exactly to spatial prefixes, with first difference at depth q+1; eventual-zero tails remain the missing state. | Our call now on §8.63's three workflow changes: stop extending finite exclusions as a goal; put the slow walls' B question beside period 2; keep period 2 as the measured reference. |
| ~~Rule210 empty-left cancellation (Local8.65; GPT G26)~~ | **DONE**, answered by Proposition 19 (PROOFS.md entry 32, second-read): no finite Rule 210 seed keeps the full 0101 clock; it does not carry over to Rule 30 verbatim (GC479) (second triage, 2026-10-08, CL065; was: **PART**) | Parity invariant reduces the empty-left walled system to Rule90; exact dyadic visible witness proves LR fails. Sixteen-bit-plus-zero continuation refuted at depth65. Replicated by Local on 2026-10-06 from GPT's committed `rule30_gpt_finite_state_scope.py` (0.1 s, at 894fc71: FS1 65,536, FS2 9,216, FS3 32 seeds and 256 words, the even-depth control rejected, as recorded). | G27 classifies the compatible left half as parity-sparse/Rule90; every finite effective prefix extends to a finite-left witness, whose infinite effective trace is aperiodic. G28 requires mixed initial parity, a positive even-site black cell and nonlinear causal activity for any finite full clock witness. G58 independently verifies Local C066: every one-parity wall has an explicit empty-left Rule210 witness, with a Catalan/dyadic boundary filter; OP1-OP2 pass26 walls/6656 transitions/3354 filter comparisons; G58 addendum proves this empty-row witness aperiodic for every nonzero periodic wall in the family (second-read by Local, L033). G59 extends G28: any finite global witness of any nonzero eventually periodic wall requires nonlinear activations at arbitrarily late times (second-read by Local, L034). G60 constructs a full infinite right realization of G58 by a triangular odd-site Rule90 recursion (reviewed by Local L035-L036; FR1-FR2 pass26 walls/13312 centre/13286 neighbor comparisons; all26 finite truncations fail at33..43). That linear seed is necessarily infinite for nonzero eventually periodic walls. G61 gives exact first-right-layer condition d=1 only on an effective0-to1 transition; for the empty-left0101 witness odd-time gates are3,15,63,... (reviewed by Local L035-L036; RG1-RG2 pass8 triples/32 pairs/4096 indices). G62 restricts the columns1-2 nonlinear pair to even down-transition times0,6,30,126,... for this stream; odd pairs there are impossible (reviewed by Local L035-L036, NG1-NG2 pass32 patches/4096 indices; all8 allowed even-pair patches retained). G63 proves a constant effective run forces a parity-linear right strip, with two time steps of margin per added column and a spatial period-six phase pattern (reviewed by Local L035-L036; ST1-ST2 pass7 pairs/1792 words/15 accepted,120 phase values; no-margin CF refuted). G64 uses those strips to bound arbitrary-start temporal complexity of every fixed right column by O_k(N^(4k+2)), hence entropy0 for the same empty-left family (reviewed by Local L035-L036; WC1-WC2 pass196608 windows/2524 forced samples,482 samples excluded). G65 extends the full parity-sparse right realization to every finite odd-supported left row by reflection; varying the row gives exact column1 union-language entropy1/2 in that subfamily (reviewed by Local L035-L036; MX1-MX2 pass32 masks/8224 clock checks/256 prefixes and exact factor counts1..8), not an entropy claim for any one orbit. G66 extends zero fixed-column entropy uniformly to each bounded initial-left-support family, using finite Rule90 trace localization near dyadic times (reviewed by Local L035-L036; BP1-BP2 pass16416 trace/14304 localization/62432 forced samples,33760 excluded). No uniform-in-radius, uniform-in-width or Rule30 consequence. G214 (GC419, second-read by Local L251) proves a quantitative G59 activation-gap bound: finite support[-R,R] and a nonzero eventually p-periodic wall require some global nonlinear activation in every[s,3*s+2*R+3*p] after onset (hand proof;672 bounded linear subset controls PASS). G215-G216 (GC420/GC422, second-read by Local L252-L253) localize required events to a Pascal-selected cone and remove source sites i<=1 for odd0101 wall samples; cone width still grows. GC423 retains the failure of covering the entire source interval with one G63 run. GC425 additionally identifies Pascal-selected transition cells outside every stated G63 run window; both transition types admit the product locally (hand audit, review pending), closing only the coverage-only shortcut. G224-G225 (GC446-GC447, reviewed by Local L262-L263) give an exact sparse Pascal stencil on dyadic source columns and an actual column2 gate implication, pruning that column to two endpoint samples under G26 (512 binomial and32 scalar controls PASS). G226 (GC449, reviewed Local L264) gives a two-step white-ancestor product obstruction (64 scalar/algebra controls PASS), eliminating later even column2 sources and requiring i>=3 at dyadic-plus-one targets. GC425 forward patches lack actual white predecessors. G227 (GC450, reviewed Local L265) reduces column3 to an early sample and one late sample only at odd K under the empty-left clock (256 lag controls PASS). G228 (GC452, reviewed Local L266) gives an even column2 up-gate schedule, removing column4 at these targets (32 scalar/K3..10 controls PASS). G229 (GC454, reviewed Local L267) eliminates the initial column3 source by the exact128-input eight-bit-prefix certificate. Combined reviewed tools place all required sources at i>=5 for even K>=4; odd K retains one late column3 term. G230 (GC456, reviewed Local L268) composes the next white beat, killing odd column1 bits from time3 and all selected column3 sources in the empty-left family (32 scalar controls PASS). It extends i>=5 necessity to all K>=3. G231 (GC458, reviewed by Local L269 in78576a7) proves that G228 incoming up-gates and G62 outgoing down-gates force an isolated effective one for any positive-time even column2 bit; G26 has none, so that track vanishes (128 scalar controls PASS). G229 handles the initial bit separately; G226 then removes every even column4 product. G233 (GC461) proves the exact even column3 switch detector q_n=1 XOR s_n XOR s_(n+1) from G61/G231 (16 scalar controls PASS; reviewed by Local L271); G232 (GC459, reviewed by Local L270) gives even column5 as the three-effective-bit discrepancy. Neither determines a full right realization. GC462 conditionally combines the explicit q,z tracks with an incoming column4 identity: h_(n+1)=(1-q_n)*(1-z_n)*w_n. Permitted arrivals have z_n=1, contradicting h_n*z_n=0, so even column4 vanishes and the selected source boundary moves to i>=7 (12 scalar controls PASS; dependencies and review pending). No even-column induction. GC465 closes the simplest universal incoming/occupancy shortcut: the explicit G60 member has three consecutive white odd-grid cells at n6,j2, permitting the column6/time14 gate. Hand binomial witness and4224 independent cell controls PASS; blind no-triple prediction REFUTED. A permitted gate is not a mixed-parity member. Local (TS/SW, L270-L272, 2026-10-08): G60's 0101 seed is exactly the sites coprime to 6 (closed form; its odd-time centre sum is the Jacobsthal number (2^(2m+1)+1)/3, always odd), and every empty-left full 0101 prefix of any parity agrees with it through site 239, so a mixed-parity member would first differ beyond site 239. Local UQ (L274, 2026-10-08, verified by GPT GC466-GC467): diagonal-window induction plus an independently rebuilt9-state acyclic deviation graph and exhaustive depth121 base certificate prove the empty-left full0101 family is exactly G60's seed. No finite seed with an empty left half realizes0101. This is a computer-assisted proof, filed as PROOFS.md entry 29 (Proposition 16). Entry 31 (Proposition 18, Local L278, second-read GPT GC470): no finite seed with left support in -6..-1 realizes 0101 (even-site rows die by depth 6; each odd-supported row has the unique infinite realization L plus R XOR mirror(L)). B for larger left radius stays open. Finite global right compatibility/B and a tail-sensitive Rule30 invariant remain open.  L278 independently verified by GPT GC470: no finite seed with initial left support inside[-6,-1] realizes0101. Seven depth121 base leaves,56 depth6 exclusions and1792 scalar controls pass; inherited entry29 graph excludes later deviations. Arbitrary finite left radius remains open.  GC471 uniform reduction (verified by Local L280): for odd left radius R, agreement with its G65 parity background throughR+98 forces global agreement, using entry29 graph beyond three cleared windows. A finite candidate must first differ byR+98. GC472 pulse lemma (verified by Local L281) eliminates odd first differences; an even first difference passes its own clock after a finite diagonal pulse. GC473 and independent Local L281 give the exact following-odd gate: its error freezes at the background cell at pulse end, independently of its initial bit (64 vector/gate and32 binomial controls PASS). Some pulses pass that gate; GC474 (verified by Local L282) derives the coupled next-even transient and proves its clock automatic after a passing odd gate. Local E3, independently verified and simplified by GPT GC475, makes passage through e+3 equivalent to white initial background cells e+1 and e+3 for every new-bit choice (64 binomial gates and320 choice controls PASS). Local PL/SB3/FV support a longer-white-run life law, still conjectural. GC476 proves the background gates through the first black equal their initial cells, with a first-black wave at tau+j+1 and finite bound w<=m+1 (verified by Local L284). GC477 supports a stronger paired odd-freeze/even-settling invariant on10880 abstract-history cases, with32 actual causal controls and an instrument error retained; this is bounded evidence. GC478 proposes a hand clearing-front proof of the full2w life law, uniqueness of G65 for every finite left row and no finite full0101 Rule210 seed;16 pair identities and40064 clearing witnesses PASS. Local L285 independently verifies every hand step and G27 scope (60865af); filed as PROOFS entry32, Proposition19. Rule210 B for the full0101 clock is closed at every finite radius. GC479 also excludes eventual nonconstant period2 at any fixed Rule210 column by time shift and translation; unrestricted clearing fails for Rule30, so no Rule30 conclusion follows. |
| Collatz critical-boundary count loss (GPT G71, G74-G80, G82, G90-G92; §7 question9) | **MERGED** into Q9 (second triage, 2026-10-08, CL065; dormant since GC415, with no plan to reopen it, GC614.1; was: **PART**, GPT reasoning) | Exact loss and backward-weighted discrepancy identities; G71, G74, G75, G77, G78, G80, G82, G91-G92 reviewed by Local. Instrument controls pass. Interior mixed pairs reduce to curvature; boundary terms retained. G82 improves coin atoms to O(h^(-1/2)) and mixed curvature to O(1/h); reviewed by Local L044; LW1-LW2 pass163872 exact window identities/364 convolution controls/257 gradients, with35 vacuous geometric checks retained. | Estimate actual signed sensitivity-weighted bias: O(1/m) at T=8*m suffices. G77-G78 close only maximum-weight/full-class-size proxy bounds; actual allocation and cancellation remain open. G90 TC1 passes the noncancellation guard. G91 gives an exact same-label coalescence decomposition: matched mass receives curvature weights; unmatched mass remains open. CM1-CM2 pass 100 increments and guards. G92 closes only the coarse maximum-curvature/count-bootstrap route: its sufficient coefficient grows at least logarithmically, even granting zero unmatched contribution. G93 finds log-concavity in 2080 finite coin-demand profiles through T64; no shape theorem. G94 isolates an absorbing-edge inequality and refutes generic preservation, leaving the actual shape open. GPT GC415 closes generic critical-after-flat log-concavity restoration: a synthetic geometric suffix moves the defect to an interior triple; no actual-law refutation. No generic fairness or contraction. Local L048: the actual demand law is NOT always log-concave: it holds for T <= 64 and fails for 48,727 of 524,800 laws to T = 1024, first at T = 73, r = 8, always at G94's edge triple after a noncritical step, remaining horizon >= 65 (65/41 is a convergent of log2 3); no interior triple fails. G213 gives an exact Abel allocation identity; GC418 retains the failure of its global range-product estimate in seven cases. GC426 weighted centering recovers bounded improvement at four of those seven widths (exact controls PASS; hand refinement reviewed by Local L255 and filed G217), with no uniform count estimate. GC428 proposes optimized<=original under unimodal demand and refutes general domination with a synthetic two-spike guard; actual unimodality remains unproved (conditional theorem reviewed by Local L256 and filed G218). GC430 refutes generic critical-after-flat unimodality restoration even for log-concave input (synthetic hand audit reviewed by Local L257 and filed G219), leaving reachable-law structure necessary for that shape route. GC432 proves a shape-free superlevel-component bound <= both G74 and G217 (196 exact controls PASS; reviewed by Local L258 and filed G220); actual interval imbalance remains open. GC434 gives an exact centering-gap formula and common-endpoint-segment criterion for ties (hand controls PASS; reviewed by Local L259 and filed G221), without a new population run. GC436-GC438 inspect the same seven cases: width7,t34 centering gap comes from an empty-class peak; across-time cancellation exceeds remaining within-increment cancellation in all seven (exact controls PASS). GC439 canonical adjacent pairs capture only14.48% at width7 (majority prediction REFUTED); t28 gains without mixed paths. GC440 gives same-count00/11 curvature regrouping with unmatched/boundary terms retained (reviewed by Local L260 and filed G222); GC442 fixed t28 has one matched pair but essential cross-count residual; GC443 gives count-only G91 matching with triangle<=state matching, while G74 domination fails synthetically (reviewed by Local L261 and filed G223). GC445 extra count matches improve state triangle but lose to G220 at both fixed times (prediction REFUTED); separate absolute-matching chase stopped on this witness. No wider scan or count bound. Local DU (L275, 2026-10-08): every actual demand law with T <= 1024 is unimodal (all 524,800, including L048's 48,727 non-log-concave ones), so G218's comparison applies to every actual law in that range. PROOFS.md entry 30 (Proposition 17, Local L276, second-read by GPT GC469, 2026-10-08): every actual demand law is unimodal at every horizon (critical steps are (1,1)-convolutions; flat steps are isolated, so each acts as B(C(p)), which preserves unimodality), so G218's comparison holds for every actual law. Not a uniform bound. |
| ~~Admitted terminal singleton question (GPT G72-G73, G81, G83-G89; Local L040)~~ | **DONE**, answered by counterexample (G89) (first triage of 2026-10-06, CL009 and GC155; was: **COUNTEREXAMPLE**, reviewed by Local L046) | G88 count-21 cover audited: 30 disjoint classes cover all 2^33 residues. G89 gives five directly verified count-22 meeting pairs; first is 5348744187/5348744191, common terminal 9770112830 after 34 steps. Every coefficient prefix is admitted; infinitely many lifts follow. | Universal singleton route is refuted, while G72-G73 multiplicity and short-label theorems remain valid. BN1 blind prediction failed; counts 23–24 were not run there (Local later ran count 23, below; count 24 is still not run). RC3 passes: 319 rejected classes plus five accepting residues cover all 2^34; exactly five families, all first meeting at 34. G83-G90 independently reviewed by Local L046; exhaustive admitted-word enumeration confirms no collisions through 21 and precisely these five at 22. Local's count-23 extension (`collatz_audit_g83_g89.py --extend`, L046): 20 pairs, all displacement 4, none first meeting at the horizon 36 (15 at step 35, 5 at 34); first meeting and odd count at the meeting are the natural labels (G078). |
| ~~Collatz logarithmic ceiling (GPT G69; §7 question9)~~ | **DONE**, proved; its remainder is Q9's (first triage of 2026-10-06, CL009 and GC155; was: **PART**, GPT reasoning/source audit) | Known Rhin bound plus G67 implies n<t^14.3/3 for actual first-deficit survivors; qualitative polynomial envelope also follows from Matveev. Reviewed by Local L037-L038 using the cited Rhin bound; LF1-LF2 pass256 exact inequalities/791 existing words. G70 gives polynomial additive actual/coefficient count error; HC1-HC2 pass131072 direct pairs/384 interval checks; exact threshold104 for T=ceil(3w/2). | This bounds exceptions at a specified deficit, not all horizon survivors or their total across unbounded times. |
| ~~Collatz endpoint digit certificates (GPT G68; §7 question9)~~ | **DONE**, proved; its remainder is Q9's (first triage of 2026-10-06, CL009 and GC155; was: **PART**, GPT reasoning) | Start and terminal share the exact first-deficit ceiling; nested binary-prefix/ternary-suffix positive representatives give sound exclusions, complete at full length. Reviewed by Local L037; EC1-EC2 pass791 lift counts/25358 endpoint congruences and256 extremizers. Finite maximum depths15/18, not uniform bounds. | Count words escaping short certificates, retaining rounding; no independence or all-horizon estimate. |
| ~~Collatz first-deficit offset envelope (GPT G67; §7 question9)~~ | **DONE**, proved; its remainder is Q9's (first triage of 2026-10-06, CL009 and GC155; was: **PART**, GPT reasoning) | Exact maximum affine intercept attained by latest barrier-compatible odd positions; B_max between a*3^a/6 and a*3^a/3. Reviewed by Local L037; OB1-OB2 pass791 census words/256 exact constructions. RB1-RB2 pass: offset/gap ordering refuted from a4; only known n1 cycle survives among256 extremizers. | Realizing residue placement and summed survivor bound; formal ceiling alone does not pay the count. |
| ~~Sideways dynamics (CONSTELLATION row5; GPT G22)~~ | **CLOSED**, as a prize route (G128); the rest parked in CONSTELLATION row 5 (first triage of 2026-10-06, CL009 and GC155; was: **PART**, GPT reasoning) | Exact two-track CA, one-step image conjugate to full ternary shift, preimage fibres and non-surjective radius-two ternary induced rule proved. G24 adds forbidden ternary output words100/101 and periodic Garden-of-Eden density tending to1. Image word-count rate log2(3); uniform images and pushed uniform inputs give different measures. G22's `rule30_gpt_sideways.py` replicated by Local (2026-10-06, at ee23889, under Python 3.12: it needs 3.10+ for int.bit_count and fails on this Mac's default 3.9 before any check runs). | Iterated images, invariant measures and dynamical entropy; connection to physical boundary-restricted trajectories. |
| The constellation: Rule 30 for its own sake (CONSTELLATION.md; the owner's second question of 2026-10-06) | **PARKED**, it is the parking place itself (first triage of 2026-10-06, CL009 and GC155; was: **OPEN**, ours to choose (the owner's reset of 2026-10-06 09:20)) | A table of interest for both questions: the families after Condrey (Part A) and fourteen objects the rule shows that nobody asked for (Part B), each with what is known, what is not, a first step and why it is beautiful; sorted into cheap runs, thinking items and the prize in other clothes (Part C). | Our choice of rows, said in the chat. Local's picks: the sideways rule (5) for beauty, the channel's limit (6) for both. |
| Time derivatives and linear complexity (the owner's question of 2026-10-06; RULE30-PRIZE.md §8.70; CONSTELLATION row 17) | **PARKED**, the owner's question, answered as far as asked (first triage of 2026-10-06, CL009 and GC155; was: **PART**, Local measuring) | Rule 30 = c xor Rule 210 (its XOR velocity is Rule 210, proved). The centre column's linear complexity is exactly $N/2$ at $N = 2^{22}$; its jump law fits fair coins; velocity, acceleration, jerk and the time-reversed column are equally complex (proved to within the derivative's order, measured equal); no lag difference or derivative up to 1,024 is biased (`rule30_linear_complexity.py`, LC1 to LC4 held). Moving frames (§8.70 second addendum): every interior speed is linearly a coin; a frame of speed $v \ge 0$ sees change with probability $1/2 + v/4$ (the OR term), proved for fair rows by GPT's G97, whose corollary makes non-rightward frames exactly iid for fair rows. The owner's relativity and unequal-tick questions: CONSTELLATION rows 18 and 19, with G98's scope (global tick durations invisible; local update orders do not commute; Nakamura 1974 restores the synchronous history with versioned reads). | GPT G96 adds exact moving-frame differences and a derivative-dynamics scope guard; MC1-MC2 preregistered and run 2026-10-06 19:16 BST, both PASS (RULE30-GPT.md G96 outcome; board corrected by Local 2026-10-09). No tracked Rule30 particle or physical acceleration claim. The profile to $2^{24}$; a non-linear complexity (the quadratic span); any route from a linear-complexity bound to Problem 1 (none known: an eventually periodic column has bounded complexity, but a bound at finite $N$ excludes only short periods). |



*Finished or closed.*

| Lead | Status | What settled it | What is left |
|---|---|---|---|
| Q4, Kari and Kopra's partial result | **CLOSED** | §8.55: true and empty for centre columns. | nothing |
| Q5, a weaker theorem for every seed | **DONE** | Theorems A and B (§8.54), Theorem A′ (§8.58). | nothing |
| Q8, the fourth game | **DONE** | §8.51: independent up to a constant factor. | nothing |
| 6.4, the survey's imports | **DONE** as a list | They became Q2, Q3 and Q5. | see those rows |
| M2, the undecided periodic columns | **CLOSED** | Jen's theorem (§8.13). The run is recorded in `periodic_kill.c`. | nothing |
| The ten routes of §4 | **CLOSED** | Each names its section. | nothing |
| Q3 as a route (added 2026-10-06) | **CLOSED** | §8.61: the certificate is Q1's potential. | nothing |

*Runs.*

| Lead | Status | What is in | What is left |
|---|---|---|---|
| 6.2 and M4, the exact records | **DONE** | Depths 69, 73, 77, 81, 85 and 89: R = 55, 59, 63, 65, 73 and 75. All three predictions held at each; Cloud's MG8 (69 to 79) held at 89. Depth 89 took 14 hours on 10 threads. | Nothing owed. Depth 93 would take about 10 days here. |
| The deep ladder (§8.56) | **DONE** | R(24, S) = 19, 22, 21 and 26 at S = 153, 185, 217 and 249 (LL1 to LL4 held). So no counterexample has its left edge within 248 cells, whatever its right half. | Depth 265 was dropped (the owner's decision). |
| 6.3 and M3b, the search to 34 cells | **DONE** | No candidate. The longest run is still 17 (`rule30_scan.py`). | nothing |
| 6.3 and M3a, the channel bound at widths 27 and 28 | **DONE** | Ran 2026-10-06 with the sets' pool mapped on the internal NVMe (written once; 6 GB resident): 0.1229 and 0.1222 bits per visible bit, EN6 held; certified exactly 0.1243 and 0.1236 (SQ6), so the squeeze lemma's constant is 0.0618 bits per step. | Nothing. |
| ~~Channel subset shape audit (Local C043; GPT G23)~~ | **DONE**, the audit is complete (first triage of 2026-10-06, CL009 and GC155; was: **PART**) | At width10 all155 subsets and225 live edges independently agree; none of154 noninitial states is a cylinder, only one affine. Twelve samples and bit-order controls recorded. Left-record witness rejected at seventh visible bit. | General compressed representation or uniform-width closure; no channel-limit formula. |

*Small items in RULE30-PRIZE.md that were never listed as leads* (found by reading every "open" and "next" in it).

| Item | Status | What has been done | What is left |
|---|---|---|---|
| A renormalisation from depth $d$ to $d/2$ (§7) | **CLOSED** | §8.36, RC5: none beyond chance. | nothing |
| What makes runs of exactly 12 and 14 (§8.1) | **DONE** | The templates (§8.2), then the wheel (§8.5, §8.9). | nothing |
| The three remains of the entropy squeeze (§8.33) | **DONE** | The constant is certified (0.1292), the two worlds are measured, and the uniform bound on patterns stands. | The uniform bound has found no use yet. |
| Are the walls synchronised in time across right halves? (§8.10) | **DONE**, measurements | Duplication: 1,968 distinct columns 1 among 3,936 unlocked halves. Sister pairs agree for 4,096 steps in 37.6% of cases; 200 checked agreeing pairs still agree at 16,384 steps (§8.60, rule30_sync.py). | Permanent confinement needs a proof, not finite agreement (GPT G3.4–G3.5). Why early escape dominates; the 37.6%. |
| ~~Why the forced cells inside a long run stay 0 (§8.2)~~ | **MERGED**, into Q1: its open part is Q1's cost argument (first triage of 2026-10-06, CL009 and GC155; was: **PART**, GPT) | G3: exact overlap-parity criterion; explicit witnesses refute closure of its three-bit summary. 80,000 sampled prefixes at depths 65–513 pass conditional half-survival prediction; scalar, C-histogram and opposite-phase controls passed. | A global cost or termination argument; the identity alone is a restatement of the forced test. |
| LR for long words that are mostly zeros (§7) | **DONE** to 35 free bits | `records_word.c`: exact records for 0001 to depth 44 and 00001 to depth 45 (§8.60). No run reaches the cap; the growth is linear, below the coin's slope. | Nothing; a run deeper is only more of the same. |
| ~~Do branch points go on for ever? (§8.31)~~ | **MERGED**, into Q7: its open part is Q7's slope and period bound (first triage of 2026-10-06, CL009 and GC155; was: **PART**) | Lemma B2 (§8.59): eventually white diagonals never stop, each a doubling or a branch. All four left sides of §8.31 to a million diagonals (§8.60): each doubles to period 32 once, at its own place (87,866; 183,183; 229,337; 291,256); the flipped side branches again at 72,575 and 165,748; settling slopes 2.002 to 2.008 on all four. | Whether the branches go on; every side needs period o(M) and one-phase slope below 3. GPT G6 proves the P−1 overhead covers all phases and isolates the adaptive zero-wait budget. |
| Does a structural reason for balance reach the core? (§8.34) | **PARKED**, Prize Problem 2, not Problem 1 (first triage of 2026-10-06, CL009 and GC155; was: **PART**, GPT) | G4: correlation identities and exact random-row temporal trace theorem; biased period-4 ring counterexample (13/28). Natural-band discrepancy stronger than 991/1000 permutations; proposed bound refuted. | A bound for edge-generated band bias across branches; correlation cancellation for the fixed single seed. |

*Owed checks.*

| Check | Status | What has been done | What is left |
|---|---|---|---|
| GPT independent audit of A, B, A′, E, E″ and §8.59 | **DONE**, first pass | RULE30-GPT.md G2: core arguments checked; E Step 4 expanded; growth and branch/period qualifications stated; all-seed prefix certified through 53207, two first-branch cycles certified. Half-line birth check changed conservative reset bounds by one and refuted GB1. | Formal verification; unbounded branch-wise bounds remain open under Q7. |
| GPT logical audit of the certificate-route closure (§8.61) | **DONE**, assessment | G5: fixed 2-by-2 matrix carries unary length; linear path ranking does not imply uniform population contraction. Counterexamples invalidate those general closure inferences. | No actual Rule 30 ranking or candidate encoding; Q3 practical deferral remains pending one. |
| GPT reset-front phase comparison | **DONE**, lemma; Q7 remains PART | G6: every conservative phase bound lies within P−1 of any chosen phase, including births; exact adaptive waiting identity. Finite prefix coalesces at 429; half-density toy rejects the marginal-density shortcut. | A sub-3 one-phase waiting bound and period o(M), on every admissible side. |
| GPT all-branch fixed-period tree and waiting debt | **DONE**, lemma and finite diagnostic; Q7 remains PART | G7: unique predecessor prevents reconvergence; at most 4^P−1 nodes across all period-P branches. Complete small trees through P=8. One-side debt at slope 5/2 has measured maximum 26.5 through diagonal 53207. RD16 measures all sixteen known period32-entry prefixes: reference debts28.5..60, finite phase/birth bound75 (GC319); independently recomputed by Local L197, sharing the audited child constructor. GC320 isolates endpoint state for extension; GC321 refutes all-terminal-drawup-zero on actual entries291257 and634886 (h0.5 and5); other fourteen h0. RD32 extends all16 clocks through1048576 with maximum debt60 and finite phase/birth91 (GC325, single-party; P2 refuted). No all-period bound. | Prove a period-scaled debt bound on every admissible side; period o(M) remains open. |
| ~~GPT local waiting potential~~ | **MERGED**, into Q7: the same bound (first triage of 2026-10-06, CL009 and GC155; was: **PART**, finite certificate) | G8/G10: nonnegative slope5/2 potential verifies all compatible edges for every common P<=10; G9 transfers budgets through births. Exact full-line debts at P8/P10 are22.5/48.5, with P10 witness146 steps over39 edges. P7 cycle forces broad-domain slope>=5/2; constant4P debt refuted at P10. Phase-free original-pair potentials need slope>=3 (G8). | Uniform potential bound as P grows and sublinear periods; distinguish all-period compatibility from power-of-two edge reachability. Birth transfer proved in G9. |
| GPT birth-restart budget transfer | **DONE**, lemma; Q7 remains PART | G9: a monotone birth front is the maximum of unclamped restarts. An all-interval/all-phase slope at least 1 budget survives barriers b_j<=j without extra absolute debt. 57600 independent diagnostic comparisons pass; endpoint-only counterexample retained. | Arbitrary-period budget and period o(M); no additional birth potential required under this hypothesis. |
| GPT clock-aligned potential quotient | **DONE**, reduction and finite implementation; uniform bound OPEN | G9.4: temporal rotation reduces P4^P states/edges to4^P, preserving optimal maximum potential. G10 implements and certifies every P<=10; P10 checks1048576 edges. | Analytic period-scaled potential; exponential size and edge-domain qualifications remain. |


| Check | Status | What has been done | What is left |
|---|---|---|---|
| The literature for W3 (COLLATZ-PRIZE.md §5) and for Theorems A, A′ and E | **DONE** | Searched 2026-10-05 (PRIOR-ART.md, last entry): W2 is Dubickas 2009, W1 and W3 are in three 2026 notes; the Rule 30 theorems were not found (Kopra and Condrey are the nearest). Dubickas 2009 read in full 2026-10-06: W2 for integers is his Theorem 5 exactly. | Check Lemma B2 (§8.59) against Jen 1986 and Rowland 2006. (2026-10-09: found in print for the single seed, Nersissian arXiv:2609.25077 Theorem 13, same method, with a bound; Rowland §5 has only the doubling criterion; Jen 1986 still owed. RULE30-PRIZE.md §8.59 note, PRIOR-ART.md.) |
| The math check (§9) on every document edited since Local took the lead | **DONE** | Node installed by the owner 2026-10-05; the check passes on RULE30-PRIZE.md, PRIZE-PROBLEMS.md, PERIOD-TWO.md and CLOUD-LOCAL.md. | Run it after every edit. |
| G1, error-free transformations on each GPU (PRIZE-PROBLEMS.md §6) | **PARKED**, outside Rule 30 (first triage of 2026-10-06, CL009 and GC155; was: **OPEN**, not written) | Nothing. It is outside Rule 30. | The job and its prediction. |

**The items**, as first written, with their tags.

1. **[OPEN]** **The wheel's kicks** (§8.43, §8.44). A kick's size comes from the interior, not from the wall's origin, its
   width, or the cells at arrival. Its timing and alphabet are rigid. The kick game, a wheel kicked only at its
   arrival phases, still has the coin's growing runs. So the wheel narrows the cost-side statement to a kicked
   rotation, but does not prove it.
2. **[DONE]** ~~**Local's depths 85 and 89**~~ (CLOUD-LOCAL.md, lead M4). Depth 85 is in: R(85) = 73, and the blind prediction
   (65 to 75, MG8 in `rule30_merge.py`) held. Depth 89 is in: R(89) = 75, inside the predicted 69 to 79.
3. **[DONE]** ~~**Job M3**~~ (CLOUD-LOCAL.md): the channel bound at layer widths 27 and 28, and the counterexample search to 34
   cells. The search is done: no candidate. The channel bound ran on 2026-10-06 once its pool was mapped on the disk.
4. **[DONE]** ~~**The wide survey's imports**~~ (§8.47): Flatto, Lagarias and Pollington's move to a finite window, a
   machine-found certificate, and a weaker single-seed theorem by an extremal argument. They are written
   out as questions in §7.

**Generality audit follow-up (GPT G52-G53, 2026-10-06): G52-G54 REVIEWED.** Corollary F is extended to phase-aligned wall-period vectors, including initially empty left rows; finite boundary conversion passes50 walls. G53 supplies the general entropy conversion h(-1)=h(visible period vectors)/p and bounds for fixed left columns. G54 combines the existing G14/G15 gap matrices with G53 for a coarse bound on every periodic wall; a deeper or uniform-width improvement still needs its own certificate. No fixed-seed lower entropy bound follows. G52 independently checked by Local L023/L024 and moved to PROOFS E2; G53/G54 independently checked by Local L026 and moved to PROOFS E2.

| ~~Paired right-race memory (GPT G110-G115; Local L066-L071)~~ | **DONE**, the races lane, closed by GPT (first triage of 2026-10-06, CL009 and GC155; was: **PART**) | Pulse first-order memory failure reviewed; G113 exact8192-word cone audit also refutes order-two closure at tick5, independently reviewed by Local L070. Finite W5 table support proves first-order failure at every interior rate. G111 arithmetic controls pass12 checks. G112 proves a local shielding identity and positive finite cylinders for the infinite fair-input model, reviewed by Local L069. G115 also refutes pulse injection-indicator plus one-lag sufficiency:24 full-history splits,0 K3-only splits, reviewed by Local L072. | G112 controls and proof reviewed by Local L069;G115 reviewed by Local L072. No all-orders or survival claim. |

| ~~Finite pulse joint information (GPT G108,G117-G118)~~ | **DONE**, the races lane, closed by GPT (first triage of 2026-10-06, CL009 and GC155; was: **PART**) | Conditional coupled traces are bijective;G117 proposes the fifth-step hidden-tail kernel and G118 exact six-sample unconditional MI. G117 controls pass2048 words. | G117 reviewed by Local L073;G118 reviewed by Local L074;JI0-JI2 pass2048 words and exact count spectrum. No entropy-rate or repeated-race law. |

## 7. Questions for fresh eyes (2026-10-05)

Written after the wide survey (RULE30-PRIZE.md §8.47), for a person or a system meeting the problem for the first
time. Each question is precise enough to start on, and none is known to be easy. Each now carries a tag; the
status board in §6 says what the tags mean and what is left of each.

*Replication (adopted 2026-10-06 from Cloud's C089): every row is single-party (one model's run) unless it says "replicated by X, commit Y".*

The survey's one finding frames them. Every theorem found in any field of the form "a low-information drive cannot
hold a chaotic system in a fixed state" is about sets of cases: sets of positive measure, or with interior. The
prize needs a statement about every single finite configuration. The questions are ways across that gap.

1. **[OPEN]** **The counting form of the uniform law.** Let $N_w(T)$ be the number of configurations supported on $w$ cells
   whose centre column reads 0101... (either phase) at times $0$ to $T - 1$. Prove that
   $N_w(T) \le 2^{w - \alpha T} \cdot \mathrm{poly}(w, T)$ for some $\alpha > 0$. Fewer than one configuration is
   none, so this exact count over a finite family would close period 2. Counting crosses the gap here because the
   seeds are finite. The measured horizon, about $w$ plus a logarithm (§8.24, §8.42), is what $\alpha = 1$
   predicts. Measured (§8.51, `rule30_count.py`): to $w = 24$ the count falls by about $2^{1.05}$ per step, so
   $\alpha$ is near 1 and the bound looks true. Proved there: the conditions paid by the seed's left part halve
   the count exactly; only those paid by the right part, after the left part runs out, are open. The right part
   pays in lumps, with at most 3 free steps in a row and any 8 steps costing 8.3 bits or more (§8.52), so the
   form to prove is a bounded debt: $N_{w,j}(T+k) \le 2^{c(w) - \alpha k} N_{w,j}(T)$, with $c(w)$ allowed to grow
   like $\log w$ (measured to $w = 26$: at most 5 for $\alpha = 0.5$). Past the hull widths that enumeration
   reaches, §8.53 counts right parts instead (an exact identity) to total widths beyond 100. There the constant
   is flat in width even at $\alpha = 1$ (about 10), and it comes from one shallow, structured window where the
   wheel forms; deeper it is about 4.5. The bound
   cannot hold for every centre word: a word
   that is some configuration's own centre column has $N_w(T) \ge 1$ for every $T$. So a proof must use the
   periodicity of 0101, as §5 says.
2. **[PARKED, second triage 2026-10-08]** **Flatto, Lagarias and Pollington's move** (§8.45, §8.47). Their partial result on Mahler's problem never beats
   positive entropy. It moves to a nearby window where the constrained side is finite, and then uses pigeonhole.
   Find a condition implied by the 0101 wall under which every admissible column 1 is eventually periodic, then
   apply Jen's theorem. Every local layer language of column 1, up to width 16, has positive entropy (§8.14, §8.20).
   So such a condition, if it exists, is not local in column 1.
3. **[CLOSED, §8.61]** ~~**A machine-found certificate.**~~ Encode the forced walk inside a zero run as a string rewriting system, and
   search with SAT for an arctic (max-plus) matrix interpretation, or for an automaton invariant with a ranking
   function, that proves the runs end. That is how Yolcu, Aaronson and Heule proved weakenings of Collatz. The
   encoding decides whether a proof exists. Condrey's $H(2, w) \ge w$ rules out any fixed-depth induction, so the
   certificate must scale with the seed's width.
4. **[CLOSED, §8.55]** ~~**Kari and Kopra's partial result, for Rule 30.**~~ For the automata that multiply by $p/q$ they prove, without
   constructing it, that some set of windows covering almost everything holds no Z-number orbit. The analogue
   would be a set of centre-column words, of measure near 1, that no nonzero finite configuration's centre column
   keeps to for ever. That would be a new theorem about Rule 30's centre columns, short of the prize. It needs
   Rule 30 to be ergodic and mixing for the uniform measure. Checked (2026-10-05): Shereshevsky,
   Monatsh. Math. 114 (1992) 305-316, proves Bernoulli and K natural extensions for surjective one-sided
   permutive automata under conditions on the neighbourhood's ends. Whether Rule 30's neighbourhood (-1, 0, +1)
   meets them was settled from his thesis (Warwick, 1992, Theorem 1.3.3, read): a left-permutative rule whose
   neighbourhood reaches left of the cell ($l < 0$) is $k$-mixing for every $k$ for the uniform measure. Rule 30
   qualifies. So Kari and Kopra's hypotheses of ergodicity and mixing hold.
   **Closed (§8.55).** Their argument was read in full. It applies to Rule 30 at once, but it is about windows of a
   row; for centre columns it is true and empty. It cannot separate a finite seed from any other configuration.
5. **[DONE, §8.54 and §8.58]** ~~**A weaker theorem about every single seed.**~~ Langton's ant's highway is unproved, but every trajectory is
   proved unbounded, by reversibility and an extremal cell. Rule 30 is not reversible, but left-permutivity solves
   it sideways. Is there a statement weaker than B, about every single finite configuration with a 0101 centre,
   that an extremal argument proves?
   **One found (§8.54, Theorem A).** Two adjacent columns cannot both be $P$-periodic on a time window $[a, b]$
   unless $b \le 2a + L + 2P - 1$, where $L$ is the distance to the left edge. Jen's theorem is $b = \infty$.
6. **[PART]** **LR by construction.** A system strong at construction and search could try to refute Conjecture LR: a column
   1, not necessarily from a finite right half, whose forced left half is eventually zero. The exact records make
   it unlikely ($R(d)$ is finite at every depth computed, about $0.8\,d$). A refutation would still teach
   something: any proof of B would have to use the right half's finiteness.
7. **[PART]** **The regime between.** Columns 1 with zero entropy that are not eventually periodic: kicks that come for ever,
   but ever more rarely. Does the forced walk's law stay bounded, as next to a white wall, or grow like the
   logarithm of the number of histories, as the coin says? This separates "zero entropy" from "finiteness" in this
   problem (the correction to §8.45).
   **Partly answered (§8.54).** Kicks cannot thin out faster than geometrically: with $P$-periodic stretches
   between kicks at times $\tau_n$, a finite left half needs $\tau_{n+1} \le 2\tau_n + L + 2P + 2$. Slower thinning,
   and the steady rate of real right halves, stay open.
   **Answered for one class (§8.57, Theorem E).** Every Sturmian column 1 has zero entropy and is never eventually
   periodic, and for every one of them the left half is never finite. Open next: codings by an arc whose ends are
   not on one orbit, rotations of a torus, and Toeplitz sequences.
8. **[DONE, §8.51]** ~~**The fourth game**~~ (§8.49, from the tetralemma). Count the seeds that survive the black, white, both and
   neither games, and measure $N_\text{both} N_\text{neither} / (N_\text{black} N_\text{white})$. A ratio near 1
   confirms the coin model's independence. One well below 1 would be an obstruction a proof could use.
   Measured (§8.51): between 0.66 and 1.34 at $w = 24$, with no trend. Independent up to a constant factor.

9. **[PART]** **The Collatz twin** (COLLATZ-PRIZE.md §1 to §3). Through Bernstein and Lagarias's conjugacy, Collatz asks
   the same question as period 2: a bijection permutive in its newest input, fed an input of finite support, and
   whether the output past the free part behaves like coins. Measured to 30 bits: the free bits pay exactly
   (Terras), the count past them follows the coin to 0.5%, and the excess stays below 3.7 bits. Collatz has what
   Rule 30 lacks, arithmetic: after the free bits the state is the explicit integer $3^a + T^{w-1}(r)$, and the
   question becomes bounding exponential sums $\sum_v e(h\,y_v / 2^j)$ over the parity vectors that stay up (the
   2-adic counterpart of Tao's 2019 estimate). The measured Fourier structure fades with width. A proof there would
   show what a Rule 30 proof must replace.
   **Sharpened (COLLATZ-PRIZE.md §4).** For $r < 2^k$, $T^k(r)$ is exactly the least residue of the Syracuse
   offset modulo $3^a$ (proved, checked to $k = 18$). So the twin statement is about the binary digits of a
   remainder modulo a power of 3: Tao's object itself, read in the other base.
   **Carried both ways (COLLATZ-PRIZE.md §5, RULE30-PRIZE.md §8.58).** One exact statement holds in both
   problems, the window principle: a block of the trace can repeat only if it is no longer than the state is
   large. For Collatz it gives, in three lines from Terras, that the parity sequence of an infinite orbit has
   complexity at least $1.71\,n$, so no rational has a Sturmian parity sequence. For Rule 30 it gives Theorem A′
   and only $p(n) \ge n - L$, because a configuration grows a cell a step. Exponential sums cannot reach a single
   case on either side: their error is at least the square root of the population. What would close Rule 30
   period 2 is a lower bound, for one orbit, on the number of contents of the $2n$ cells beside the centre:
   more than $2^{0.13\,n}$.

## 8. Reading order

0. `RECORD-MAP.md` (2026-10-09, the owner's request): one line per known result and where it lives. Read it in
   full first, and again after any context compaction; search the rest with `tests/probes/record_find.py`.
1. This file.
2. `WORKFLOW-SAVED-MEMORY.md`: the working rules. Predictions are written before runs, failures are recorded,
   prior art is surveyed before leaps, and every script that produced a recorded number is kept.
3. `CLOUD-LOCAL.md`: how Cloud and Local split work, the messages table, and the ledger (start from main and the
   ledger, never from memory). A model new to this record, of any make, reads `WORKING-TOGETHER.md` first: the
   lanes in the repository, the method, and what to do in the first hour.
4. `RULE30-PRIZE.md`: the honest summary at the top, then §5, §7, §8.4 to §8.14, §8.20, §8.36 to §8.42, and
   §8.45 to §8.47 (where the problem sits among its relatives).
   The Collatz twin has its own record since 2026-10-06, `COLLATZ-PRIZE.md`, with its own board (§6). The map of what
   Rule 30 shows beyond the prize, and of the families after Condrey, is `CONSTELLATION.md` (2026-10-06).
5. `PRIOR-ART.md`: the dated surveys, especially Condrey, Jen and Kopra, Rowland, the prime-gap parallel, the
   siblings in arithmetic, and the owner's wide survey.
6. `tests/probes/PROBES.md`: the index of every probe (row `lexicon/`).

## 9. How to reproduce the core numbers

Everything is in `tests/probes/lexicon/`. Each script's header gives its command, cost and predictions. Pure
Python 3 scripts need nothing else, and the C engines need a C compiler with OpenMP.

| Script | What it computes | Cost |
|---|---|---|
| `records.c`, `rule30_records.py` | exact R(d), the forced walk over every prefix | seconds to depth 61 |
| `records_bits.c`, `records_fast.c` | the same, 64 prefixes per machine word (Local's engines) | 12 times faster |
| `rule30_merge.py` (and mode `recur`) | the distinct walks D(d) and the merge rate | a minute |
| `rule30_wall.py` | the wall form, checked against `records.c` | seconds |
| `rule30_words.py` | black, white and both, for every word up to period 4 | 25 minutes |
| `rule30_race.py` | the information race in the combined game | seconds |
| `rule30_uniform.py` (modes `deep`, `horizon`, `windows`) | total width plus a constant or a logarithm | 15 minutes |
| `rule30_complement.py` | the best finite seed for 0101 (§8.24) | 5 minutes |
| `ladder.c`, `rule30_ladder_deep.py` | the ladder R(m, s) | minutes |
| `entropy.c`, `entropy2.c` | the channel bound | minutes to hours by width |
| `wheel_orbit.c` | Proposition 6's certificate for the pure wheel | minutes per phase |
| `rule30_jenclock.py`, `jenclock.c` | Jen's theorem with a clock (§8.54): Theorems A and B, checked | seconds |
| `rule30_sturmian.py` | Theorem E (§8.57): every Sturmian column 1 is excluded | 2 minutes |
| `rule30_window.py` | Theorem A′ (§8.58): the window principle | 20 seconds |
| `rule30_sync.py`, `rule30_records_word.py` + `records_word.c`, `rule30_leftside_million.py` | the small items (§8.60): the slips' synchrony is duplication; exact records for any wall word; the left side to a million diagonals | a minute; 15 minutes; 5 minutes |
| `rule30_otherrules.py` | the left band of every rule whose edge moves at light speed (§8.64): 30, 110 and 118 alone have one | seconds |
| `rule30_damage_speed.py` | the leftward light speed on structured backgrounds: $v = 1 - P(\text{heal})E[\text{jump}]$; the checkerboard heals ($-0.39$), the band locks above its white diagonals, rings give exact rationals (§8.66) | `python3 tests/probes/lexicon/rule30_damage_speed.py 13` and `... 13 lock` | 2 min |
| `rule30_ring_census.py` | Rule 30 on rings to $n = 24$, complete: cycle counts, periodic states, transients, gliders; OEIS A334496/A334497 reproduced (§8.67) | `python3 tests/probes/lexicon/rule30_ring_census.py 24` | 40 s |
| `rule30_triangle_census.py` | the single cell's triangle tops to $10^5$: the core obeys the uniform measure's $3 \cdot 2^{-(L+4)}$ to 0.1%; the right edge's widest at $m 2^k$; the band's widest 16 (§8.68) | `python3 tests/probes/lexicon/rule30_triangle_census.py 100000` | 4 min |
| `rule30_leftside_horizon.py` | the slow walls from the left: a left seed narrower than about the period $a + b$ dies before two consecutive black stretches next to $0^a 1^b$; wider ones pass; 0101's left-only horizon $W + 17$ (§8.69) | `python3 tests/probes/lexicon/rule30_leftside_horizon.py 20 100` | seconds |
| `rule30_band.py` | Lemmas B1 to B3, Theorems A‴ and A⁗, Corollary F (§8.59): the band of stripes meets the window principle; the universal strip to 53,200 diagonals with a certificate | a minute |
| `ladder_deep.c`, `rule30_ladder_local.py` | the layer ladder to depth 318, in parallel (§8.56) | minutes to hours |
| `rule30_walls.py`, `rule30_slips.py` | the wheel's domain walls and kicks | minutes |

**The math check.** After any edit of a document with TeX in it, run `python3 tests/probes/mathcheck/check.py
RULE30-PRIZE.md` once `npm install` has been run in that folder. It must report 0 TeX errors and no stray dollar
signs.

## 10. Checks before you start

- `git log --oneline -5` on main and on the working branch. Read the ledger's last rows.
- `python3 tests/probes/lexicon/rule30_wall.py` must print ALL CHECKS PASS (4 seconds). It ties the wall form to
  `records.c`.
- `python3 tests/probes/lexicon/rule30_merge.py` must print ALL CHECKS PASS (14 seconds).
- Then stop, and ask what to do.

**Temporal-instrument reasoning checkpoint (GPT G99/G100, 2026-10-06; second-read by Local, PROOFS.md §E2).** Versioned prior-generation reads preserve the synchronous finite dependency graph under complete ready-node schedules; this is known scheduling, with VP1 passing680 initial words. G100 gives an exact fair-row speed-one temporal-dependence guard: adjacent flip covariance0, lag-two covariance1/32, three-flip count variance5/8 versus iid9/16. RF1 checks all64 relevant initial words with two formulations. This does not establish an interior-ray covariance, asymptotic variance, physical clock or selected-seed claim. Local's race-condition measurements remain a separate lane.

**Interior temporal-memory checkpoint (GPT G101, 2026-10-06; second-read by Local, PROOFS.md §E2).** For speed3/4 under the fair spatial ensemble, an aligned stay/right/right/right block has mean11/4 and variance7/8, against independent13/16; second/fourth covariance1/32. IF1 passes all512 relevant inputs against the factored G100 prediction. Distinct-block dependence, asymptotic variance and the selected seed remain open. This is a small exact scope result, not a new long-ray measurement.

**Race-scope checkpoint (GPT G102, 2026-10-06; second-read by Local, PROOFS.md §E2).** Isolated right-race injection1/8 differs from a fair-first-row open-terminal chain model's bulk conditional rate1/(8-4eps), with exact finite-depth remainder. CI1 passes43680 combinations and48 exact weighted checks. The overall correction is second order in eps, consistent with preserving Local's empirical rare-race fit. No finite-cyclic exact mean, later noisy-row law or effective-cone survival theorem follows. A separate no-race dependency-cone bound is the next reasoning lead.

**Clean-cone checkpoint (GPT G103, 2026-10-06; independently reviewed by Local L058).** Snapshot reads at every unflagged dependency node force target agreement. Independent flags give P(diff)<=1-(1-eps)^(t²); marginal flag bounds give P(diff)<=eps*t². A fixed mean disagreement threshold needs at least a square-root inverse-eps timescale. CP1 passes77440 histories and192 rational site checks. No matching upper rate, realised first-crossing guarantee or coefficient0.623 is proved.


**Oriented spatial-law checkpoint (GPT G104, 2026-10-06; independently reviewed by Local L059).** Infinite right-reading races with state-independent terminating flag runs preserve the fair spatial product law by a conditional block inverse. Fresh independent flags therefore earn the G102 right-bulk per-step injection formula, relative to the current noisy row. Left-reading races retain first-row fair density but change adjacent disagreement to1/2+eps/4. OM1-OM2 pass2720 right cases,10880 left cases and48 exact moments. Ideal-history survival, later left-row law and exact finite cyclic invariance remain open.


**Finite cyclic scope checkpoint (GPT G105, 2026-10-06; independently reviewed by Local L060).** For uniform input on a W-cell ring, every right flag pattern gives zero-row probability2^(1-W); independent left flags give [1+(1-eps)^(W-1)]*2^(-W). Thus infinite-bulk fair invariance is not exact finite cyclic invariance. Common all-zero input never decoheres, so a matching upper bound requires state/activity assumptions. ZR1 passes43648 cases and40 exact weights. Large-ring approximate statistics remain separate; no Local job duplicated.


**Raced temporal-field checkpoint (GPT G106, 2026-10-06; independently reviewed by Local L061).** Right-bulk fair spatial rows persist under fresh independent flags, while right-moving one-step flip mean changes to(3-eps)/(4-2eps). Left/stay flip means remain1/2. Predetermined moving-path count mean is N/2+N_right/(4-2eps). TF1 passes43648 anchored cases and60 exact means. Temporal covariance, adaptive observers, selected-seed laws and coupled-history survival remain open. This is a temporal-field distinction with unchanged frame law, not physical acceleration.


**Conditional noisy-trace checkpoint (GPT G107, 2026-10-06; independently reviewed by Local L062).** In the infinite right-reading model, a predetermined nonrightward path has iid fair samples/flips even conditional on any terminating flag field independent of the initial row. Temporally correlated flags are allowed. NT1 passes135296 finite cases and8736 conditional pivot classes. This extends G97 through raced recursions, but noisy and ideal copies need not agree or be independent; their shared fresh initial bit cancels in the discrepancy. Joint-history coupling is the next reasoning lead.


**Paired trace checkpoint (GPT G108, 2026-10-06; independently reviewed by Local L063).** Conditional on nonpivot initial bits and the terminating right-race schedule, ideal/noisy nonrightward traces are related by a causal invertible XOR mask. Their conditional joint entropy and mutual information are N+1 bits, although each marginal trace is iid fair. First-tick error depends on the old observed state: black targets have no right-race error, white targets have probability eps/(4-2eps) under fresh Bernoulli flags. CT1 passes135296 paired cases and8736 conditional classes. Unconditional coupling and mask dynamics remain open.


**Local source-echo checkpoint (GPT G109, 2026-10-06; independently reviewed by Local L064).** An arbitrary single flip has source errors1,1-z(1),z(1) OR z(2) over two synchronous ticks. An isolated right-race injection forces z(1)=1, so source errors across ticks1..3 are101 despite no further races. EH1-EH2 pass160 words with an independent damage equation. Healing at a source is neither global coalescence nor permanent recovery. Repeated-race memory closure remains open.


**Pulse projected-memory checkpoint (GPT G110, 2026-10-06; independently reviewed by Local L065).** K_t=(ideal source bit,error) is not first-order Markov in the fair isolated-pulse model, despite iid marginal traces. Given K2=(b,0), next error has probability1/8; further conditioning on previous error gives1 or0. PM1 passes128 words with exact8/56 counts per current bin. Local owns the distinct repeated-iid finite-ring conditional-memory table requested in ChatG109; no general finite-order or infinite-bulk claim follows.


**Question 7 rotation-code update (GPT G131, 2026-10-06; second-read by Local, L085).** Theorem E's repeat obstruction transfers to every finite block factor of a Sturmian word, with only a fixed block-width margin. A direct XOR construction covers any finite union of half-open arcs whose endpoints lie on one rotation orbit, for every phase and every irrational angle, including bounded partial quotients. This advances the one-orbit subclass; unrelated endpoint orbits, torus rotations and kicked codes remain open. No new experiment. See RULE30-GPT.md G131 and the waiting room of PROOFS.md.


**Question 7 projection addendum (GPT G132, 2026-10-06; second-read by Local, L086).** A circle covering, or a torus observable that factors through one integer circle coordinate and a G131 arc code, inherits the exclusion. This includes some multiple original endpoint-orbit classes; arbitrary endpoint conventions only change finitely many samples for irrational projected angles. Genuinely multidimensional box partitions, general unrelated endpoints and kicked observables remain open. No experiment.


**Question 7 kicked-code update (GPT G133, 2026-10-06; second-read by Local, L087).** For a golden-angle Sturmian base, Theorem E's proof supplies a conservative uniform linear bound on an unbroken matching stretch beside a finite left seed. Actual disagreement times must satisfy k_next<=169*k+84*L+505; super-geometric flip schedules are excluded. Dyadic schedules are not excluded by this necessary bound. No entropy, positive-density, measured-rational-wheel or general kicked-code theorem is asserted. No experiment.


**Question 7 bounded-type kicked-code update (GPT G134, 2026-10-06; second-read by Local, L088).** The G133 finite-horizon argument extends to every irrational base angle with partial quotients bounded by A. With K_A=8*(A+1)^4+3, actual discrepancies obey k_next<=(2K_A+1)*k+K_A*L+6K_A+1. Hence super-geometric correction schedules are excluded for this whole class. G134 supplies the explicit preceding-convergent argument for finite-offset separation, rather than relying on an eventual threshold. Dyadic corrections, unbounded-type bases, phase-reset kicks and the measured rational wheel remain open. No experiment or entropy claim.


**Question 7 uniform-angle reset update (GPT G135, 2026-10-06; second-read by Local, L088).** The repetition inequality itself bounds consecutive convergent denominators, removing G134's bounded-partial-quotient assumption. Every standard irrational Sturmian piece has matching horizon less than 251(L+2a+4) at starting index a. Piecewise codes may reset both phase and angle, but reset times necessarily satisfy t_next<=503*t+251*L+1004. Super-geometric resets and fixed-base flips are excluded for every irrational angle. Geometric resets, arbitrary arc observables and the measured rational wheel remain open. No entropy or prize claim; no new experiment.


**Question 7 recoded-reset update (GPT G136, 2026-10-06; second-read by Local, L089).** The uniform horizon extends to all mechanical angles and block factors of width w+1, with H(C,w)=251(C+4)+250w. Reset pieces may change angle, phase and recoding, but uniformly bounded widths still exclude super-geometric reset spacing. Half-open orbit-endpoint partitions inherit this through their bounded integer exponent spans. Unbounded-width prefix fitting is explicitly not a fixed-code theorem. Geometric corrections and general unrelated-endpoint observables remain open. No experiment.


**Question 7 geometric-scope audit (GPT G137, 2026-10-06; second-read by Local, L090).** The indicator of powers of two satisfies every repeat inequality b<=2a+q-1 and has factor complexity at most 2m+1, hence zero word-count entropy. Indicators of B^j for integer B>=3 violate the finite-left repeat condition on their zero runs. Thus repetition tests alone cannot force positive entropy or exclude every sparse geometric word. This is not a Rule30 realization or a result about Sturmian words with dyadic flips; an additional wall/coupled-tail constraint remains necessary. No experiment.


**Question 7 wall-gate audit (GPT G138, 2026-10-06; second-read by Local, L092).** The first five forced columns are explicit Boolean functions of c_s,c_(s+1),c_(s+2). Depth-four even bits equal c_s*c_(s+1), with one pulse for the dyadic indicator, but this does not classify the initial tail. The constant-zero control has a zero product and an infinite checkerboard tail. Sparse low-depth gates and temporally shifting checkerboard strips do not close the all-depth obstruction. No experiment or realization claim. G136 is independently verified by Local L089.


**Question 7 inverse-locality update (GPT G139, 2026-10-06; second-read by Local, L092).** For the dyadic input, all defects at fixed depth j lie within j-1 steps before dyadic pulse times; temporal factor counts obey P_j(m)<=4(m+j)+2. Every fixed finite left window has zero temporal word-count entropy. This does not control the spatial initial tail because its determining windows grow with depth. Local L091's finite initial-row measurements and this temporal theorem concern different axes; an infinite family of forced initial ones remains unproved. No new computation.


**Question 7 entropy/limit bridge audit (GPT G140, 2026-10-06; second-read by Local, L093).** The existing wall coding conjugates two wall-driven steps to one visible-word shift. Its full compatible family has entropy one; the dyadic orbit closure has entropy zero and contains the infinite checkerboard limit. Growing support bounds make that limit compatible with a hypothetical finite starting row, so neither temporal entropy nor the limit resolves the initial spatial tail. This shortcut is closed; no experiment or prize claim.


**Spatial-support predecessor audit (GPT G141, 2026-10-06; second-read by Local, L094).** Alternating-wall backward evolution has one black-phase ancestor and two white-phase choices. The existing M0/M1 tail graphs give a finite ancestor-support test, conditional on an actually clock-compatible finite output. Finite boundary rows can merge while passing the first black-time condition, so whole-line finite injectivity and unique-root descent do not transfer unchanged. Descent may stop at an infinite-tail obstruction; no root exclusion or clock witness is proved. No experiment.

**Q7 minimal-family scope audit (GPT G154, 2026-10-07; second-read by Local, L112).** The Rudin–Shapiro binary shift closure is infinite and minimal. Its finite-tail subset is empty or countable dense, residual-complement and null for every invariant probability measure. Generic infinite support therefore leaves the specified original word unresolved. No experiment, realization or prize claim.

**Q7 radius-count update (GPT G155, 2026-10-07; second-read by Local, L113).** The number of finite-tail words of radius at most L is bounded by P_X(ceil(L/2)). For the Rudin–Shapiro family it is either zero or of linear order, by a substitution upper bound and the conditional growing-radius orbit lower bound. G154 is second-read by Local L112. No experiment or specified-word exclusion.

**Q7 edge-period bound update (GPT G156, 2026-10-07; second-read by Local, L114).** Temporal rotation quotienting sharpens G7's rooted-profile count to K+1<=N_4(P), asymptotic to4^P/P. The common-period-one/two maximum prefixes are exactly3/8. This is a period lower bound; an upper period-growth estimate and the all-branch adaptive waiting budget remain open. No experiment or prize claim.

**Q7 source-checked radius-count refinement (G155 follow-up, 2026-10-07; transfer checked by Local, L114).** Allouche–Shallit's exact Rudin–Shapiro factor formula gives N_(X_r)(L)<=8*ceil(L/2)-8 for L>=15; source and small-length guard are in PRIOR-ART.md and RULE30-GPT.md. The verified zero-or-linear conclusion and specified-word spatial-tail gap are unchanged. No experiment.

**GPT dated addendum, 2026-10-07, to row6.1 (GC385; PART unchanged):** the phase12/14 column5 correlation now has a four-row Boolean proof from column4 pattern011 and a preceding column5 zero. A145-observation transfer from the existing width12 certificate is proposed for independent review, improving the earlier175 bound. Either common bit remains possible in the width13 relaxed model; Local's L236 width15 forcing is source-audited and filed as G208 with GPT lift replication. This does not complete the prize proof.

**GPT dated addendum, 2026-10-07, row6.1 (G208; PART unchanged):** exact dynamics through width15 force columns2..6 in the eventual core.193 wheel observations certify column5 at the centre; a conservative303 certify all five. The computed certificate has Local direct-core and GPT lift checks, and no growing spatial front or globally realized infinite wheel follows.


**Q6 finite-language contraction (GPT, 2026-10-08).** G238, independently read with its entry gate by Local L293, excludes visible 01000010001001 by hand. This finite target is CLOSED; the broader Q6 records and realizability question remain PART. No new board row or prize conclusion.

**Q6 silent-source coverage target (GPT, 2026-10-08; GC590, hand extension awaiting reading).** A certified depth j, time colour p and onset age A covers finite-edge depths L<=j-A-2 of parity j-p. The certified family intercepts every finite-edge ray precisely when its thresholds are unbounded separately in both parity classes. No infinite Rule 30 family is proved; Local keeps SO onset measurements, and Q6 stays PART. E14's hand identity is filed in GC589 awaiting independent reading.

**Q6 fixed-source deadline (GPT, 2026-10-08; GC591, awaiting reading).** A positive-L frontier reaches depth j by age j-3. Conditional on L310's replayed SO firing witnesses, all six shallow targets miss every possible onset-interception deadline, as does E30 white using its age-64 control. Longer age caps cannot rescue those fixed targets for this route. The all-depth source family and Q6 remain open; no necessity of a nonlocal obstruction is proved.

**Q6 diagonal-source contraction (GPT, 2026-10-08; GC592, awaiting reading).** A streak of r+1 frontier-diagonal events is exactly one initial black followed outward by 2r+1 whites. A separate one-ray streak census is CLOSED as a new mechanism: it repackages existing realizable white-run records. Joint clock and multiple-ray possibilities remain open; Q6 remains PART.

**Q7 near-extreme waiting constraint (GPT, 2026-10-08; GC594, G247 extension second-read by Local L311).** On an uninterrupted common-period path, consecutive delays a+b>q and b<q force the third delay one. Ordinary nonsingleton triples cost at most 2q-1. GC595 transfers this through conservative births and gives common-period-four prefix debt T(M)-(5/2)M<=1+(5/2)P, P the singleton-driver count (second-read by Local L312 and L313, including the GC572/GC573 birth premises). GC596 gives the affine extension but its certified slope (2q-1)/3 is already five at q8 (awaiting reading), so larger periods, selected frequency and the global waiting budget remain open; Q7 stays PART.

**Q6 ray-coverage route, where it stands (Cloud, 2026-10-08 21:04 BST; chat CL054 to CL058; Q6 remains PART).** The
owner's red-object postulate (CL054) became GPT's ray target. A finite left edge with deepest initial black L forces
the event E_(L+t+2)(t) = 1 at every t (GC585), so a source that is silent where that ray passes forbids that L.
- **Read now.** GC585, GC586 and GC590 to GC592 have their second reading (Cloud, CL057), as have the E14 identity
  (GC589, Local L310) and CL055's adjacency rules (GPT, GC595).
- **Fixed silences.** To depth 31 these are E1 black, E2, E4 white, E6 and E14 white (SS, Local L309). They cover
  only L <= 4 and the even L <= 12.
- **No hardening.** The six near-silent candidates fire at every age to 256 (SO, Local L310). By GC591 they can never
  intercept, since every arrival comes by age j - 3.
- **One diagonal streak** is exactly an initial black followed by white cells (GC592), so it is the zero-tail
  question again.
- **Adjacency rules.** Events never touch straight down or down-left, so no red-set edge is more than half full
  (CL055). They do not bound the interior's parity.
- **What is left.** Interception needs unbounded thresholds j - A - 2 in both parity classes (GC590). That means
  deep sources or joint constraints with the clock. The alternative is a clock-dependent reason why the interior
  cannot pay GC586's 110 signature.

**Row 6.1, G248 read (Cloud, 2026-10-08 21:04 BST; chat CL056; 6.1 remains PART).** The phase and charge readings of
a kick differ by 14 times the sum of the complete visible zero gaps between the two locks, mod 28 (G248 with
GC582). It was read by hand and replayed at every consecutive RB lock pair, 139,972 and 71,016 of them
(`rule30_cloud_review_g248.py`). The one odd pair is RB's single 1-gap at t = 71. It says nothing about which gaps
are admissible, or about the integer lift.


**Q6 duration-accounting refinement (GPT GC766, 2026-10-09; hand reading pending).** GC745's closing-inclusive L cost sharpens GC735's mixed change budget: with n=r+1 maximal same-letter blocks, T<=(J_0+5)(2^n-1)+1, replacing the earlier common constant20. The first-S bound is sharper still. The sparse formal S^(2^j)L word passes the improved block costs, so the tag stays PART and actual inter-run compatibility remains missing. No experiment.


**Q6 settled-white L constraint (GPT GC767, 2026-10-09; hand reading pending).** G2.3’s existing e=53207 diagonal settled by T=107312 also constrains L blocks: D<=min(J_0+a+6,J_0+abs(a-107312)+54133). The all-L even-time diagonal samples stride-33, with cyclic white maximum7; inverse overlap costs four per sample. This complements GC740’s S constraint, but fixed depth leaves arbitrarily late starts unbounded. Q6 stays PART, with actual inter-run compatibility missing. L400 independently hand-accepts GC763/G249 and GC766/G250.
