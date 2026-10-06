# Rule 30, Prize Problem 1, period 2: where it stands

*A handover, written 2026-10-05 so that the work survives a move of compute, a new machine, or an outage. For a
person, or for an assistant given this file: read it, then the documents it names in the order given, run the
checks at the end, and stop. Do not start an experiment you were not asked for. Run `git log --since=2026-10-05` to
see what moved after this was written.*

*What is open, running, done or closed: the status board in §6. It is kept current; the rest of this file is the
record.*

## 1. The question

Wolfram's Rule 30 Prize Problem 1 asks whether the centre column of Rule 30, started from one black cell, ever
becomes periodic. The work here attacks it **period by period, for every finite starting configuration**, which is
stronger than the prize needs.
- **Period 1 is closed.** Condrey proved that no nonzero finite configuration has an eventually constant centre
  column (arXiv:2609.09431, 2026-09-08).
- **Period 2 is open.** That is the case worked on here: can a finite configuration's centre column be 0101...
  from some time on? Condrey's own conclusion names it as the next unresolved case.

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

## 6. Leads and their status

**The status board** (updated 2026-10-05 23:06; the time is from the shell). Every lead in this file, in RULE30-PRIZE.md and
in the mathematics table of CLOUD-LOCAL.md has one row here. When a lead moves, its row here and the tag at its
item change in the same commit. Nothing is deleted: a finished item keeps its text, and its title is struck
through.

The tags. **OPEN**: nothing settles it, and work can start. **PART**: part is settled, and the rest is named.
**RUNNING**: a job is on a machine. **DONE**: acted on, and the result is recorded. **CLOSED**: a dead route, or
settled by a theorem; do not reopen without new evidence. **BLOCKED**: cannot be done with what is here.

*The prize, and the routes to it.*

| Lead | Status | What has been done | What is left |
|---|---|---|---|
| Q1, the counting form (§5's missing statement; M1 in CLOUD-LOCAL.md) | **OPEN** | Measured to width 26, and by right parts beyond width 100 (§8.51 to §8.53). Restated as a count of window contents (§8.58). | The proof. No known method reaches it. |
| 6.1, the wheel's kicks | **OPEN** | Narrowed to a kicked rotation (§8.43). The wheel's rigidity alone is refuted as a bound (§8.44). | A statement about the kicks' sizes, which come from the interior. |
| Q2, the move to a finite window | **OPEN**, not started | Nothing direct. Theorems E and E″ (§8.57) exclude classes of column 1. They do not force periodicity. | A condition that is not local in column 1. |
| Q3, a machine-found certificate | **CLOSED** (§8.61) | Assessed before any encoding: a certificate is a potential falling at every forced cell; walks of length 0.83 d from every depth force it to be linear in the seed, and a potential of that kind is the bounded-debt statement of Q1 written as log N. Not a separate route. | Reopen only with a named finite family of potentials to search. |
| Q6, LR refuted by construction | **PART** | The exact records cover every column 1: no left half is zero from any depth up to 85 onwards (§8.36, §8.37). | Depths beyond the records. Nothing constructive has been tried. |
| Q7, the regime between | **PART** | Kicks cannot thin out faster than geometrically (Theorem A). Every Sturmian column 1 is excluded (Theorem E). Codings by arcs are excluded for almost every rotation number (Theorem E″). Every column 1 that begins with near-squares at unbounded periods is excluded: period-doubling, Chacon, substitution fixed points starting with a double letter (Corollary F, §8.59). Thue–Morse and paperfolding are excluded for every left edge up to 15,868 cells (Theorem A⁗). | Thue–Morse and paperfolding for every left edge: one-phase adaptive waiting bound below slope 3 and sublinear period growth on every admissible branched left side (§8.59; GPT G2/G6). G6 proves worst phase is at most any chosen phase plus P−1, including births. Rudin–Shapiro. Arcs with unrelated ends when the partial quotients stay small. Rotations of a torus. Kicked wheels. |
| Q9, the Collatz twin | **PART** | The least-residue lemma (COLLATZ-PRIZE.md §4). The window principle on both sides, W1 to W3 (COLLATZ-PRIZE.md §5). Exponential sums cannot reach a single case. | The literature check (below). A Collatz statement beyond complexity $1.71\,n$. |
| Rung 3, periods 3 to 6 (RULE30-PRIZE.md §6) | **PART** | Horizons measured for every word up to period 4 (§8.42). Theorems A, A′, B and E hold for every period. §8.62: the right ladder is freedom, not period; period 3 is two walls on opposite sides of it. | Nothing specific to periods 3 to 6 has been tried since. |
| The two Condrey ends (§8.62; the owner's question of 2026-10-06) | **PART**, GPT reasoning, Local measuring | The ladder by freedom named. Black end $0\,1^{p-1}$: exact records for $p = 3$ to $8$ to 32 free bits, LR holds, $R/d$ about 0.8 of the coin's $1/(p-1)$; GPT's §G11: the checkerboard survives one hole as a known prefix of $p-1$ cells and no further; no rays, chaos past the hole. G12: flipping a hole followed by four black cells changes only its own row's first three cells, with all-depth shielding beyond them; earlier inverse propagation stays open. G12.4 also certifies an eleven-cell first-bit effect for a specified p3 input prefix by terminal adjacent agreement. G13 gives an exact four-state inverse-row reset language and p>=8 one-step-back shielding beyond depth7; successive-row reset gaps remain unbounded. G13.5 iterates through r steps when p>=3r+5, shielding beyond4r+3; the protected window loses three cells per step, so later holes are not controlled all the way to time0. White end $0^{p-1}1$: the latch lemma (column 1 non-decreasing between the wall's black times), too weak alone; the statement there must be B. G14 sharpens the relaxed latch language with exact two-state full/visible matrices, crediting p2 Pell/Fibonacci; p8 visible bound0.35449 bits/step, still no cost theorem. G15 characterizes the width-one visible language by white gaps: one-hole p>=3 allows every hole-bit sequence in that relaxation; equal white density can have different local capacities. G16 proves the exact width-two one-hole language: even p forbids11, p3 forbids100, odd p>=5 is still full; the first two have rate log2(phi)/p. G17 proves width three has exactly the same visible language for every p, despite a period-four hidden black relation; odd-period restrictions require width>=4. G18 answers the slow-switch audit: a+1 exact finite prefixes from a latch position; checkerboard band4a..a+b-1 if b>=3a+1, even for nonperiodic preceding wall; phase corrected and complete one-parameter tail closure refuted. G19 gives a finite-window latch obstruction for0^5 1^5: left support>=7, versus arbitrary-input prefix minimum4; interior r3 defeats the endpoint shortcut. All-a balanced support and bounded debt remain open. | A cost for the second defect after the protected prefix (GPT's next target); whether anything at either end escapes the positive-entropy gap. |
| The one-hole channel layers (GPT G15-G17/G20; CONSTELLATION row16) | **PART**, GPT reasoning | Width one is fully free at p>=3; widths two/three restrict even p and p3 but allow all odd p>=5. G20 proves width four still allows every hole-bit sequence at every odd p>=5, by B^8=B^16 and six exact subset certificates; blind first-restriction prediction refuted. | First restrictive width, if any, is>=5 for odd p>=5. A uniform layer construction or a failure certificate; the full infinite right half remains unproved. |
| The reframing: next steps after Condrey without period 2 (§8.63; the owner's question of 2026-10-06) | **DECISION OWED** | Walls have two coordinates, freedom and switch density; 0101 switches every step, the farthest wall from Condrey's, which is why only it turns a wheel. The slow walls $0^a 1^b$ are the natural next family. Measured at fixed freedom: no fall of LR's law of the predicted size with switch density (0.81, 0.81, 0.67, 0.79 against 0.83; an effect stays unresolved). GPT's §G15, §G18, §G19: the exact injection rate $\log_2(a+1)/(a+b)$, a reset theorem for $b \ge 3a+1$, a latch obstruction on balanced walls; the spatial tail is the missing state. | The owner's call on §8.63's three workflow changes: stop extending finite exclusions as a goal; put the slow walls' B question beside period 2; keep period 2 as the measured reference. |
| Sideways dynamics (CONSTELLATION row5; GPT G22) | **PART**, GPT reasoning | Exact two-track CA, one-step image conjugate to full ternary shift, preimage fibres and non-surjective radius-two ternary induced rule proved. G24 adds forbidden ternary output words100/101 and periodic Garden-of-Eden density tending to1. Image word-count rate log2(3); uniform images and pushed uniform inputs give different measures. | Iterated images, invariant measures and dynamical entropy; connection to physical boundary-restricted trajectories. |
| The constellation: Rule 30 for its own sake (CONSTELLATION.md; the owner's second question of 2026-10-06) | **DECISION OWED** | A table of interest for both questions: the families after Condrey (Part A) and fourteen objects the rule shows that nobody asked for (Part B), each with what is known, what is not, a first step and why it is beautiful; sorted into cheap runs, thinking items and the prize in other clothes (Part C). | The owner's choice of rows. Local's picks: the sideways rule (5) for beauty, the channel's limit (6) for both. |

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
| Channel subset shape audit (Local C043; GPT G23) | **PART** | At width10 all155 subsets and225 live edges independently agree; none of154 noninitial states is a cylinder, only one affine. Twelve samples and bit-order controls recorded. Left-record witness rejected at seventh visible bit. | General compressed representation or uniform-width closure; no channel-limit formula. |

*Small items in RULE30-PRIZE.md that were never listed as leads* (found by reading every "open" and "next" in it).

| Item | Status | What has been done | What is left |
|---|---|---|---|
| A renormalisation from depth $d$ to $d/2$ (§7) | **CLOSED** | §8.36, RC5: none beyond chance. | nothing |
| What makes runs of exactly 12 and 14 (§8.1) | **DONE** | The templates (§8.2), then the wheel (§8.5, §8.9). | nothing |
| The three remains of the entropy squeeze (§8.33) | **DONE** | The constant is certified (0.1292), the two worlds are measured, and the uniform bound on patterns stands. | The uniform bound has found no use yet. |
| Are the walls synchronised in time across right halves? (§8.10) | **DONE**, measurements | Duplication: 1,968 distinct columns 1 among 3,936 unlocked halves. Sister pairs agree for 4,096 steps in 37.6% of cases; 200 checked agreeing pairs still agree at 16,384 steps (§8.60, rule30_sync.py). | Permanent confinement needs a proof, not finite agreement (GPT G3.4–G3.5). Why early escape dominates; the 37.6%. |
| Why the forced cells inside a long run stay 0 (§8.2) | **PART**, GPT | G3: exact overlap-parity criterion; explicit witnesses refute closure of its three-bit summary. 80,000 sampled prefixes at depths 65–513 pass conditional half-survival prediction; scalar, C-histogram and opposite-phase controls passed. | A global cost or termination argument; the identity alone is a restatement of the forced test. |
| LR for long words that are mostly zeros (§7) | **DONE** to 35 free bits | `records_word.c`: exact records for 0001 to depth 44 and 00001 to depth 45 (§8.60). No run reaches the cap; the growth is linear, below the coin's slope. | Nothing; a run deeper is only more of the same. |
| Do branch points go on for ever? (§8.31) | **PART** | Lemma B2 (§8.59): eventually white diagonals never stop, each a doubling or a branch. All four left sides of §8.31 to a million diagonals (§8.60): each doubles to period 32 once, at its own place (87,866; 183,183; 229,337; 291,256); the flipped side branches again at 72,575 and 165,748; settling slopes 2.002 to 2.008 on all four. | Whether the branches go on; every side needs period o(M) and one-phase slope below 3. GPT G6 proves the P−1 overhead covers all phases and isolates the adaptive zero-wait budget. |
| Does a structural reason for balance reach the core? (§8.34) | **PART**, GPT | G4: correlation identities and exact random-row temporal trace theorem; biased period-4 ring counterexample (13/28). Natural-band discrepancy stronger than 991/1000 permutations; proposed bound refuted. | A bound for edge-generated band bias across branches; correlation cancellation for the fixed single seed. |

*Owed checks.*

| Check | Status | What has been done | What is left |
|---|---|---|---|
| GPT independent audit of A, B, A′, E, E″ and §8.59 | **DONE**, first pass | RULE30-GPT.md G2: core arguments checked; E Step 4 expanded; growth and branch/period qualifications stated; all-seed prefix certified through 53207, two first-branch cycles certified. Half-line birth check changed conservative reset bounds by one and refuted GB1. | Formal verification; unbounded branch-wise bounds remain open under Q7. |
| GPT logical audit of the certificate-route closure (§8.61) | **DONE**, assessment | G5: fixed 2-by-2 matrix carries unary length; linear path ranking does not imply uniform population contraction. Counterexamples invalidate those general closure inferences. | No actual Rule 30 ranking or candidate encoding; Q3 practical deferral remains pending one. |
| GPT reset-front phase comparison | **DONE**, lemma; Q7 remains PART | G6: every conservative phase bound lies within P−1 of any chosen phase, including births; exact adaptive waiting identity. Finite prefix coalesces at 429; half-density toy rejects the marginal-density shortcut. | A sub-3 one-phase waiting bound and period o(M), on every admissible side. |
| GPT all-branch fixed-period tree and waiting debt | **DONE**, lemma and finite diagnostic; Q7 remains PART | G7: unique predecessor prevents reconvergence; at most 4^P−1 nodes across all period-P branches. Complete small trees through P=8. One-side debt at slope 5/2 has measured maximum 26.5 through diagonal 53207. | Prove a period-scaled debt bound on every admissible side; period o(M) remains open. |
| GPT local waiting potential | **PART**, finite certificate | G8/G10: nonnegative slope5/2 potential verifies all compatible edges for every common P<=10; G9 transfers budgets through births. Exact full-line debts at P8/P10 are22.5/48.5, with P10 witness146 steps over39 edges. P7 cycle forces broad-domain slope>=5/2; constant4P debt refuted at P10. Phase-free original-pair potentials need slope>=3 (G8). | Uniform potential bound as P grows and sublinear periods; distinguish all-period compatibility from power-of-two edge reachability. Birth transfer proved in G9. |
| GPT birth-restart budget transfer | **DONE**, lemma; Q7 remains PART | G9: a monotone birth front is the maximum of unclamped restarts. An all-interval/all-phase slope at least 1 budget survives barriers b_j<=j without extra absolute debt. 57600 independent diagnostic comparisons pass; endpoint-only counterexample retained. | Arbitrary-period budget and period o(M); no additional birth potential required under this hypothesis. |
| GPT clock-aligned potential quotient | **DONE**, reduction and finite implementation; uniform bound OPEN | G9.4: temporal rotation reduces P4^P states/edges to4^P, preserving optimal maximum potential. G10 implements and certifies every P<=10; P10 checks1048576 edges. | Analytic period-scaled potential; exponential size and edge-domain qualifications remain. |


| Check | Status | What has been done | What is left |
|---|---|---|---|
| The literature for W3 (COLLATZ-PRIZE.md §5) and for Theorems A, A′ and E | **DONE** | Searched 2026-10-05 (PRIOR-ART.md, last entry): W2 is Dubickas 2009, W1 and W3 are in three 2026 notes; the Rule 30 theorems were not found (Kopra and Condrey are the nearest). Dubickas 2009 read in full 2026-10-06: W2 for integers is his Theorem 5 exactly. | Check Lemma B2 (§8.59) against Jen 1986 and Rowland 2006. |
| The math check (§9) on every document edited since Local took the lead | **DONE** | Node installed by the owner 2026-10-05; the check passes on RULE30-PRIZE.md, PRIZE-PROBLEMS.md, PERIOD-TWO.md and CLOUD-LOCAL.md. | Run it after every edit. |
| G1, error-free transformations on each GPU (PRIZE-PROBLEMS.md §6) | **OPEN**, not written | Nothing. It is outside Rule 30. | The job and its prediction. |

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

## 7. Questions for fresh eyes (2026-10-05)

Written after the wide survey (RULE30-PRIZE.md §8.47), for a person or a system meeting the problem for the first
time. Each question is precise enough to start on, and none is known to be easy. Each now carries a tag; the
status board in §6 says what the tags mean and what is left of each.

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
2. **[OPEN, not started]** **Flatto, Lagarias and Pollington's move** (§8.45, §8.47). Their partial result on Mahler's problem never beats
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
