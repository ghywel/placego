# Rule 30: GPT's independent record

Results here use sections G1, G2, and so on. The shared research record and lead status remain in
`RULE30-PRIZE.md` and `PERIOD-TWO.md`. The collaboration protocol is `WORKING-TOGETHER.md`.

## G1. Joining the collaboration (2026-10-06)

**Asked.** Set up a checkout with push access, read the handover and import the standing workflow.

**Identity and reading.** Codex, based on GPT-6; an exact deployment build identifier is not available in this
session. Read `WORKING-TOGETHER.md`, `WORKFLOW-SAVED-MEMORY.md`, `PERIOD-TWO.md`, the shared ledger and messages,
and the honest summaries in `RULE30-PRIZE.md` and `PRIZE-PROBLEMS.md`. Read the Rule 30 notation in `LEXICON.md`
and the headers of the two required startup probes. This is onboarding, not a review of every proof or cited paper.

**Workflow import.** `AGENTS.md` points future Codex sessions at the standing documents, the GPT lanes, the
status board, the evidence standard and the git/privacy checks. It keeps those documents as the source of truth.

**Environment.** Intel macOS, 16 logical cores; Python 3.14.7 with numpy 2.5.3. HTTPS clone succeeded. A dry-run
push of the setup branch succeeded. Existing Git authentication was sufficient; GitHub CLI was not installed.

**Startup checks.** Both standard commands initially stopped at the C compile: Apple clang rejected
`-fopenmp`, because neither library location checked by `ompflags.py` contained libomp. The initial Python
controls passed, but those attempts were not full passes. OpenMP installation and serial verification were
started. Homebrew installed libomp 23.1.2 and upgraded its build dependency, CMake, to 4.4.4.

**Final outcome, 2026-10-06.** Both standard commands completed with exit status 0 and `ALL CHECKS PASS`:

- `python3 tests/probes/lexicon/rule30_wall.py`: WA0 passed on 300 columns; WA1 held through m = 10; WA2 held at
  all 25 depths 3 to 27; WA3 held. The header's warning that WA3 is a weak counterfactual still applies.
- `python3 tests/probes/lexicon/rule30_merge.py`: MG0a, MG0b and MG0c passed; unshielded flips changed the run
  in 0.68 of trials, and all 13 records and histograms at odd depths 21 to 45 agreed. MG1, MG3, MG5 and CF held.
  MG2, MG4, MG6 and MG7 were refuted, as expected from the existing outcome. MG5's largest number of distinct
  sampled record walks was 2, median 1. MG6 failed at depth 43 (latest differing time 32). At depth 65 the
  latest differing time was 18, rather than the saved run's 24. These are summaries of the at-most-64 witnesses
  printed by the engine; the selected subset can differ with execution order. They are not exhaustive counts
  of all record walks.

The wall check also passed using serial compilation while installation ran. The temporary serial merge run
reproduced its controls and witnesses through depth 59, then was interrupted at depth 61 once OpenMP was ready.
Its serial executable was removed before the standard rerun, which compiled the engine with OpenMP. Results
computed during this setup at depths 21 to 59 were reused from the temporary cache; depths 61 and 65 were computed
with OpenMP. Depths 69, 73, 77 and 81 used the committed Local witness file, as the probe normally does. No probe
source or prior outcome was changed.

**Unexpected check.** Inspected the startup probes' temporary-cache paths before trusting them. No pre-existing
records cache or merge executable was present. The merge probe reuses committed Local witnesses at depths 69,
73, 77 and 81; its earlier witness results need a fresh computation in this checkout.

**First research task proposed by the handover.** Independently try to break Theorems A, B, E, E-double-prime and
A-prime, with attention to the hypotheses and boundary cases. No new research experiment was started during
setup. The repository reports that period 2 remains open and that there is nothing to submit; no prize-status
claim or theorem has been independently verified by this onboarding entry.

**Owner's hardware and coordination clarification, 2026-10-06.** This machine is an Intel MacBook Pro with an AMD
RX 6600 GPU; Claude Local's machine is an M5-series MacBook Pro. This is owner-reported hardware, not a GPU
capability measurement. The startup checks above used this Intel machine's CPU. The owner asks for frequent
milestone pushes and messages about status, work and intention. GPT accepts Local's proposed reasoning lanes:
the forced zeros inside long runs, structural balance at the core, and independent proof audits including section
8.59. The first intended research step remains the proof audit; no new research run has started.

## G2. Independent proof audit (2026-10-06; completed first pass)

**Scope and verdict.** Read the proofs of A, B, A′, E, E″ and §8.59 as an adversary. I found no
counterexample to their main statements under the stated Rule 30 hypotheses. Two applications need explicit
qualifications: a substitution must grow on its starting letter, and an unbounded Thue–Morse extension must
control periods and settling times on every admissible branched left side. A short argument missing from E's
Step 4 is supplied below. These are a first independent audit, not formal verification or a prize solution.

**Method and prior reading.** Followed the inverse rule, edge positions and closed-strip recurrence directly.
Read [Rowland, Local nested structure in rule 30, §5](https://ericrowland.github.io/papers/Local_nested_structure_in_rule_30.pdf)
(pages 15–17), including the reset lemma, period doubling and possible branching. The continued-fraction
best-approximation fact was checked against Theorem 27 of
[the UNCG ergodic-theory notes](https://uncg.edu/~cdsmyth/UNCG_Ergodic_Theory_Summer_School_2020_Final_Lecture_Notes.pdf).
No new claim of priority follows from this audit; Jen 1986 remains owed a full reading.

### G2.1. The elementary and band arguments

| Statement | Audit finding |
|---|---|
| A, adjacent periodic columns | The inverse rule loses one time value per step left. At distance $L+a+P$, the later row's left edge is black and the earlier row is white. The threshold is $b\ge2a+L+2P$, giving the stated $b\le2a+L+2P-1$. |
| A′, repeated adjacent blocks | A length-$n$ repeat determines $n-1$ cells left of the pair. The later edge at distance $L+a'$ forces $n\le L+a'$. A is this statement with $n=b-a-P+1$. |
| B, white-run bound | For $P\ge2$, a run of length $2P-1$ supplies a full period of zeros in an interior column. That column is identically zero; its right neighbour is monotone, periodic and initially zero, hence zero too. The adjacent zero pair propagates back to the nonzero boundary. The $P=1$ case is separate. |
| B1, white then black | Once $D_j=0$, $D_{j+2}$ is nondecreasing. Its zero limit would force an adjacent zero pair, impossible by backward propagation to $D_0=1$. |
| B2, unbounded diagonal periods | If the power-of-two periods were bounded, they would divide one common $P$. Two pairs of periodic time-words must coincide. Unique backward reconstruction takes that equality into the zero negative diagonals, contradicting $V_0=1$. This concerns eventual periods; it does not bound their settling times. |
| A‴, black inside the repeat | The forced white interval is exactly $[L+a'-n+1,a'-a-1]$ in diagonal coordinates. A black $b<a'-a$ yields $n\le L+a'-b$. |
| Corollary F | B2 supplies an eventually black $b\ge L+2K$. Apply A‴ to the pair $(-1,0)$, whose left-edge distance is $L-1$ and block length is $2\ell$. The contradiction retains the necessary one-cell margin. |
| B3, settled white runs | Backward expansion can remain in its older-run case for fewer than $P$ steps; otherwise periodicity would put the black boundary inside an expanded white run. At birth the black preimage and the forward white cone overlap if the run is longer than $2P$. Short runs are already within the claimed bound. |
| A⁗, repeats versus the band | The intersection with the settled prefix has length $M-(L+a'-n)$, bounded by $2P$ by B3. If that intersection is empty, the resulting inequality is automatic. |

**Substitution qualification.** If a fixed point starts with $aa$, applying the substitution gives prefix
$\sigma^k(a)\sigma^k(a)$. Corollary F applies when $|\sigma^k(a)|\to\infty$; that growth should be stated.
The identity substitution fixes arbitrary words but supplies no unbounded sequence of square lengths.
This is a qualification of the application, not a counterexample to Corollary F. The named period-doubling
and Chacon substitutions do grow and retain their exclusions.

### G2.2. Rotation proofs and the suppressed finite-offset step

E uses an irrational slope $0<\alpha<1$ and the Sturmian half-open interval convention. Its passage from visible
bits to the two-column trace gives the stated constant $C=\lfloor(L-3)/2\rfloor$. The first two visits to the
small mismatch arc give

```math
q_{n+1}-q_n-C-4\le h(n)\le q_n+C+2.
```

An empty initial equality stretch (first visit at 0 or 1) still satisfies the upper bound for large $n$.
Return gaps use a strict inequality because two points in the same half-open arc of length $|\delta_n|$
are strictly less than that length apart. Adjacent opposite-side mismatch arcs are disjoint with the given
endpoint convention. Infinitely many partial quotients at least 2 give the stated contradiction.

For the eventually-all-1 case, Step 4 asserts that only $m=-q_n$ can occur. Here is the finite-offset argument
that makes that assertion precise. Put $D=2C+6\ge4$. Best approximation and the bound
$-q_n-D\le m\le D$ force $m=-q_n-r$, with integer $0\le r\le D$, for large $n$.
If $r>0$, irrationality gives the fixed positive number

```math
\eta=\min_{1\le r\le D}\|r\alpha\|>0.
```

Consequently

```math
\|(q_n+r)\alpha\|\ge\eta-|\delta_n|>|\delta_{n-1}|
```

for sufficiently large $n$. This contradicts the required distance across the two mismatch arcs.
Thus $r=0$ and $h(n+1)=h(n)+q_n$; the final incompatible bounds in E follow. The missing sentence is repairable
within the existing proof, without any extra hypothesis on the phase.

For E″, use genuine finite interval codings with consistent half-open endpoints. The break-time recurrence
$d_{j+1}\le2d_j+q_n+C+3$ and its pigeonhole argument check out. Under a finite-left-half assumption there must
be infinitely many breaks at each fixed period: a final infinite equality stretch would violate Step 0
(or give the already excluded periodic trace). This also covers constant/degenerate codings separately.
The theorem does not exclude every finite-arc coding of every irrational rotation: bounded partial quotients
with unrelated endpoints remain open. The informal phrase “a pure rotation by any angle fails” must be read
in the Sturmian coding scope of E.

### G2.3. Exact finite certificate, all seeds, and the first branch

The new probe is [rule30_gpt_cycles.py](tests/probes/lexicon/rule30_gpt_cycles.py), standard-library Python,
one CPU core. Predictions were committed and pushed in `cf64715` before its first run. It applies Rowland's
reset/parity mechanism and the existing §8.31 construction; it claims no new period-doubling theorem.

**Why the classification covers all seeds.** Suppose a prefix has one eventual cycle of common period $P$,
up to phase. For the next diagonal write its periodic parents as $a,b$, and its state as $z$:

```math
z(t+1)=a(t)\oplus(b(t)\lor z(t)).
```

If $b$ has a black cell, that time resets $z$ independently of its incoming state. The next diagonal has a
unique $P$-periodic continuation for each parent phase. If $b=0$, this is cumulative XOR with $a$.
Odd parity over a period gives two complementary $2P$-periodic continuations; shifting by $P$ exchanges them
while leaving the old prefix unchanged, so there is still one cycle up to phase. Even parity gives two
$P$-periodic continuations; this is the first opportunity for distinct cycles. Induct from $D_0=1$.
This proves eventual attraction for every edge-normalised seed at each finite width before a branch;
right-hand cells cannot affect the closed prefix. It does not assume random seeds represent all seeds.

The program follows all these cases until diagonal 53208. It also checks every phase against the independent
spatial update $V'=((V\ll2)\oplus((V\ll1)\lor V))\bmod2^K$. At the first branch the two certified orbits are
disjoint. Each is realised by a finite seed: choose one of its strip rows and append zeros to the right.

| Pre-registered item | First-run outcome |
|---|---|
| GC0, exhaustive small control | All 512 edge-normalised width-10 seeds agree with the classified cycle after 64 steps and for the next 16 directly simulated rows. |
| GC1 | First branch 53208; earlier common-period doublings at 3, 8, 29, 400. |
| GC2 | Unique cycle up to phase on diagonals 0–53207; period 16; white diagonals exactly 2, 7, 28, 399, 53207; all spatial transitions certified. |
| GC3, known settling control | Worst-phase full-line reset upper bound $\tau(53199)\le107294$, agreeing with §8.59. |
| CF, one-cycle continuation | Rejected: two disjoint certified 16-cycles on diagonals 0–53208. |
| GC4, blind extension of the bound | Held: $\tau(53207)\le107312$, inside the predicted interval 107294–107326. |

The first run printed `ALL CHECKS PASS`, exit 0. These settling numbers are conservative reset bounds, not
measured maxima attained by seeds. The all-seed classification validates the universal-prefix premise at
§8.59's finite width. It cannot make one cycle universal beyond its first branch; the existing §8.31 already
realises four left sides farther out.

**Unexpected boundary check, including a failed prediction.** A full-line diagonal exists at time 0. In the
forced half-line it need only enter at time $k-L$. Before using the same reset recursion there, take
$\max(\tau_{k-2},\tau_{k-1},k-L,0)$ as its start. Pre-registered and pushed this extra check in `5f5e8a9`
before running `python3 tests/probes/lexicon/rule30_gpt_cycles.py birth`. The worst valid $L=1$ gives conservative
bounds 107295 and 107313, each one greater than the full-line bound. GB0 and the late-birth counterfactual GB2
passed; blind GB1 (unchanged bounds) was **refuted**. The command printed `FAILURES`, exit 1, as it should.
This does not refute the full-line bound or exhibit a late-settling wall configuration. It identifies the
birth correction needed for the reset proof to apply directly to the half-line. No published finite exclusion
threshold is changed by this check alone.

### G2.4. What an unbounded Thue–Morse extension would actually need

The existing repetitions have $i=0$, $i'=3\cdot2^k$, $\ell=2^{k+1}$. For a fixed left-edge distance $L$, the
following sufficient criterion makes the one-cell contradiction explicit. At arbitrarily large scales choose
an endpoint $M_k$ and a common eventual period $P_k$ for its prefix. Write $\tau(M_k)$ for an upper bound
on the settling time of the entire prefix, with

```math
M_k<6\cdot2^k,\qquad
\tau(M_k)+P_k\le6\cdot2^k,\qquad
M_k\ge L+2^{k+1}+2P_k.
```

Apply A⁗ to $(-1,0)$, with distance $L-1$, time $a'=6\cdot2^k$ and length $n=2\ell$:

```math
2\ell\le L-1+6\cdot2^k-M_k+2P_k\le2\ell-1,
```

impossible. In particular, sufficient asymptotic bounds are
$\tau(M)\le\gamma M+O(1)$ with $\gamma<3$ and $P(M)=o(M)$: choose
$M_k=\lceil(2+\varepsilon)2^k\rceil$ with $\gamma(2+\varepsilon)<6$.
For an exclusion covering every admissible left half, these bounds must hold on every left-side cycle that
can arise (constants may depend on that left half; seed-independent constants would be stronger).
A bounded settling slope without period control is insufficient. A bound for just one selected branch is
insufficient. This sharpens the last reduction of §8.59 without closing it.

**Validation and handoff.** The certificate and its controls passed; the unexpected birth check retained its
failed blind prediction. Math rendering passed on RULE30-GPT.md, PERIOD-TWO.md, PRIOR-ART.md and CLOUD-LOCAL.md (zero TeX errors
and zero loose dollar signs in each). Local owns the computational
runs; the requested feedback is to make growth, coding scope, birth times and branch coverage explicit in future
applications. Next reasoning lane: the forced zeros inside long runs, then structural balance at the core.


## G3. Forced zeros: a parity criterion, and why three bits do not close the walk (2026-10-06)

**Scope and result.** Took the agreed reasoning lane of §8.2, with a four-process CPU diagnostic supporting it.
Read §8.2, §8.37–§8.38 and §8.41 first; both startup probes passed again. The forced output has an exact
three-parity description, but explicit realised prefixes show that this summary does not determine the next
forced output. Sampling 80,000 prefixes at four deeper starting depths supports roughly half-survival per
forced test. This is neither an independence theorem nor a uniform survival bound; the prize remains open.

### G3.1. Exact criterion

Use the existing anti-diagonals $A_k[j]=x(-j,k-j)$, with $0\le j\le k$ and $A_k[0]=\tau(k)$.
Write $P=A_{k-1}$, $Q=A_{k-2}$ as bit words; at $k=1$, $Q$ is empty. Let $\pi$ denote bit parity, and
$c=\sigma(k-1)$ the newest column-1 bit. Then, for any centre word $\tau$,

```math
L(k)=\tau(k)\oplus\pi(P)\oplus\pi(Q)
\oplus\pi\big(P\mathbin{\&}(Q\ll1)\big)
\oplus\big((1-\tau(k-1))c\big).
```

**Proof.** The anti-diagonal recurrence is a running XOR of
$P[j-1]\lor Q[j-2]$ for $j=2,\ldots,k$, with first term $P[0]\lor c$ and initial bit $\tau(k)$.
For bits, $u\lor v=u\oplus v\oplus uv$. Summing modulo two gives the three parities above;
the first term supplies the additional $c\oplus P[0]c=(1-\tau(k-1))c$.
All the bits of $P$ and $Q$ are included; there is no omitted endpoint term. This is elementary Boolean algebra
applied to the recurrence already in `records.c`, not a new claim about the rule's invertibility.

For $\tau=0101\ldots$, odd $k$ admits exactly one choice of $c$ making $L(k)=0$. At even $k$, $c$ is hidden and

```math
L(k)=\pi(P)\oplus\pi(Q)\oplus\pi\big(P\mathbin{\&}(Q\ll1)\big).
```

Thus a forced cell stays zero precisely when the parity of overlapping black entries matches the XOR of the
two individual parities. The overlap is the nonlinear term. This gives a concrete test of the internal
configuration; it does not explain why that equality must eventually fail for every prefix.

### G3.2. A falsified small-state shortcut, with replayable witnesses

The three bits determine the current forced cell, but are not an autonomous state for the zero-forcing walk.
For an even starting depth, take two prefixes giving the same three bits and current output zero; advance that
forced step and then force the next free step to zero. Their following forced outputs can differ:

| Depth | Three bits before the current forced step | Prefixes | Following forced outputs |
|---|---|---|---|
| 22 | $(1,1,0)$ | 26 and 48 | 1 and 0 |
| 66 | $(0,1,1)$ | 2767783534 and 1338062742 | 1 and 0 |

Prefix bit $i$ is $\sigma(2i)$; take hidden odd-time bits as zero. The probe's `state`, `summary` and `zero_step`
functions replay these witnesses. Therefore no deterministic update using only these three bits and the depth
can reproduce the zero-forcing dynamics: the initial summary, current depth and forced choices agree, while
the later predicted output differs. This closes this particular compression shortcut. It does not rule out
other summaries, larger finite-state descriptions, or a theorem using the full diagonal pair.

### G3.3. Pre-registration and outcomes

Probe: [rule30_gpt_forced.py](tests/probes/lexicon/rule30_gpt_forced.py). Predictions, fixed sampling seeds,
controls and counterfactuals were committed in `9c621e7` and pushed to main before the first run.
One process per starting depth sampled 20,000 uniform visible prefixes; these are prefix-weighted statistics,
not uniformly sampled distinct walks. Free steps choose their unique zero continuation; a forced 1 ends a walk.
At each test the denominator contains only prefixes surviving all earlier tests.

- **FZ0 passed.** Scalar left-parent reconstruction on 100 random column-1 words, every depth through 64,
  agrees with the formula and bit-word update. All 1,024 prefixes at depth 21 reproduce freshly compiled
  `records.c`'s complete histogram: run lengths/counts 1/512, 3/244, 5/81, 7/72, 9/48, 11/36, 13/16, 17/15.
  The control raises an error if a walk reaches its cap; none was censored.
- **FZ1 held.** All 32 conditional survival fractions at starting depths 65, 129, 257 and 513 fall inside the
  pre-registered interval [0.35, 0.65], each based on at least 100 reached prefixes. The first test's fractions
  are 0.49605, 0.4959, 0.50235 and 0.49535. The full range is 0.41875–0.56. Counts are retained in the header.
- **FZ2's three-bit closure counterfactual was rejected** at both stipulated depths, by the witnesses above.
- **CF was rejected.** Omitting the overlap parity changes directly reconstructed cells.

The run printed `ALL CONTROLS PASS`, exit 0. The roughly half-survival was already suggested at smaller depths
by §8.36–§8.38; this is an extension of that diagnostic, not a newly discovered law. Neither the finite samples
nor their marginal conditional rates exclude an exceptional infinite survivor.

**Unexpected check: change the centre's phase.** Pre-registered the `phase` addendum in `3164fc4` and pushed
before running it. For $1010\ldots$ the free depths are even, so reusing the $0101\ldots$ coefficient is wrong.
The general formula above agrees with scalar reconstruction at all 6,400 new cells (100 words, 64 depths,
seed 302). The old phase-specific formula disagrees at 3,194 cells. The command printed `ALL CONTROLS PASS`,
exit 0. This tests the boundary coefficient independently of the original phase's passing results.

### G3.4. Feedback on Local's right-edge damage question (CHAT C003)

A closed right-edge prefix is not by itself a barrier to damage travelling into the interior. Let $r+t$ be
the common right edge and $R_k(t)=x(r+t-k,t)$. The forward rule is

```math
R_k(t+1)=R_k(t)\oplus\big(R_{k-1}(t)\lor R_{k-2}(t)\big).
```

So the values of a fixed prefix depend only on that prefix, but values farther inward depend on it as well.
For a direct counterexample to a *fixed-width* confinement criterion, put a black cell at $r=0$ in both rows,
and flip only the cell at $-K$ in one row, with $K\ge2$ and every other cell white. The initial damage is confined
to the last $K+1$ cells. At the next step the cell at $-K-1$ differs, because its middle parent is white and
its right parent is the flipped bit. The common edge is now 1, so that difference has offset $K+2$, outside
the former fixed-width strip. Both rows are finite valid seeds with the same right edge.

This does not refute Local's observed long-lived identical wall traces or any stronger certificate of
confinement within a particular growing band. It does show why finite-time localisation alone is insufficient.
A proof of permanent non-escape needs an invariant boundary condition or a quantitative bound on the inward
front relative to a precisely defined growing band. No such invariant was established in this block.

### G3.5. Incoming exact-halving claim: the raw counts refute it

Local's newly pushed §8.60 and CHAT C006 call the survival curve an exact halving, attributed to
left-permutivity. The committed `rule30_records_word.txt` contradicts that wording. For 00001 at depth 45,
the population is 68,719,476,736; its first death count is 34,359,738,788, whereas half is 34,359,738,368.
The difference is 420. Its next death count is 17,175,829,450, whereas a quarter of the initial population
is 17,179,869,184. This is approximate geometric decay, not exact halving.

Our independently reproduced 0101 depth-21 control is a smaller counterexample. All 1,024 prefixes pass
the first free step; 512 survive the first forced test. Of these, 244 die at the next forced test
(the histogram's length-3 bin), leaving 268, not 256. Exact balance after conditioning on earlier
success does not follow from left-permutivity. No new long-word computation was run for this correction.

Similarly, agreement over 4,096 steps (and 16,384 for the checked subset) is a finite observation. It does
not justify “for ever” without a permanent-confinement proof. The shared status board now states those
windows explicitly; Local was asked to correct their own §8.60 prose.

**Lead status and next intention.** The forced-zero lead is PART: the exact criterion and failed summary shortcut
are recorded; a global cost or termination argument is still missing. Next reasoning lane is structural balance
at the core. Local's exact record and million-diagonal jobs remain separate. Document math checks and publication
checks accompany this milestone; raw large datasets were not added to git.


## G4. Structural balance: ordered cancellation, correlations and exact obstructions (2026-10-06)

**Result and scope.** The ordered band's cancellation is stronger than in 991 of 1,000 permutations of its
same finite list of diagonal densities. Two candidate shortcuts failed: my proposed absolute discrepancy
bound, and balance of every nonzero power-of-two-period ring cycle. A precise temporal fair-coin theorem
holds for a random initial-row ensemble; it cannot be transferred to the fixed single-cell seed or to
conditioned forced walks. Exact correlation identities below state what remains to control. No proof of
Prize Problem 2, or of a limiting ordered-band density, is claimed.

Read §8.34/8.35 and `rule30_core.py`'s raw outcomes before choosing the diagnostic. The cycle machinery is from
G2 and Rowland's already credited mechanism. Targeted searches about periodic cycles found Wolfram's prize
page and cycle literature; no new claim of priority is made for these elementary identities or witnesses.

### G4.1. What balance means algebraically

For physical cells put $s_i(t)=1-2x_i(t)$, so black has spin $-1$. Rule 30 gives exactly

```math
2s_i(t+1)=s_{i-1}(t)\big(s_i(t)+s_{i+1}(t)+s_i(t)s_{i+1}(t)-1\big).
```

The probe checks all eight neighbourhoods. This is the spin form of the OR truth table, not a conservation
law. Write $\mu_i(T)$ for the temporal spin mean, and $C_{1,i},C_{2,i},C_{3,i}$ for the temporal means of
$s_{i-1}s_i$, $s_{i-1}s_{i+1}$ and $s_{i-1}s_i s_{i+1}$. Summing the identity gives

```math
2\mu_i(T)+\mu_{i-1}(T)=C_{1,i}(T)+C_{2,i}(T)+C_{3,i}(T)
-\frac{2(s_i(T)-s_i(0))}{T}.
```

The endpoint error has absolute value at most $4/T$. Thus even a temporal limit of zero neighbour bias
would leave a correlation sum to control for the centre column. Balanced local outputs alone do not set
those correlations to zero.

Average also over a spatial window of $M$ cells. The shift of $\mu_{i-1}$ costs one cell at either end, giving

```math
3\overline\mu=\overline C_1+\overline C_2+\overline C_3+E,
\qquad |E|\le \frac4T+\frac2M.
```

This concerns a space-time average, not the temporal average of one selected column. On a ring over a full
cycle, $E=0$. A density of one-half is then equivalent to cancellation of that correlation sum; it does
not follow just from surjectivity.

**Diagonal-coordinate qualification.** The ordered band uses $D_k$, with parents $k-2,k-1,k$, rather than
physical adjacent cells. For a temporally periodic prefix the same spin expansion applies with those
indices. Its spatial boundary term involves two diagonals, so the corresponding mean identity has
$|E|\le4/M$ and no temporal error. Keeping the coordinate system explicit avoids transferring the
physical-cell boundary constant to the diagonal strip.

### G4.2. Two exact biased cycles

The first biased power-of-two cycle found by the exhaustive ring check is

```math
1\longrightarrow67\longrightarrow100\longrightarrow63\longrightarrow1
```

on seven cells, with bit $i$ meaning cell $i$. Direct cyclic Rule 30 updates verify all four arrows.
Its black counts are 1, 3, 3 and 6, total $13/28$, not one-half. The per-column black counts across the
four phases are $(3,2,2,1,1,2,2)$: column 0 has density $3/4$, while columns 3 and 4 have density $1/4$.
A power-of-two temporal period therefore does not enforce collective or individual-column balance.
Of the 31 nonzero power-of-two cycles on rings of sizes 1–14, only 17 are balanced.

There is also the simple five-cell travelling cycle

```math
7\longrightarrow25\longrightarrow14\longrightarrow19\longrightarrow28\longrightarrow7,
```

each row with three black cells, so density $3/5$. It is the spatial repetition of `11100`, shifted two
cells at each step. Both cycles represent infinite spatially periodic configurations. Neither is a finite
configuration counterexample to a prize statement. They do block a blanket argument that a balanced,
surjective rule, periodicity, or a power-of-two clock forces every orbit to have density one-half.

In particular, an argument for the *edge-generated* ordered strip must retain that accessibility condition;
it cannot replace the strip by arbitrary power-of-two-period configurations.

### G4.3. Finite ordered-prefix discrepancy, and the permutation null

For the unique period-16 cycle on diagonals 0–53207, let $w_k$ be the number of black cells in the 16-phase
word at diagonal $k$. Define

```math
U(M)=\sum_{k=0}^{M-1}w_k-8M.
```

The previously recorded value at $M=40000$ is $U=-7$, reproduced exactly. My pre-registered claim
$|U(M)|\le128$ for every $1000\le M\le53208$ was **refuted**: the maximum absolute discrepancy is 216,
attained with sign $-216$ at $M=50086$. At $M=53208$, black count 425490 gives $U=-174$ and density about
0.499796. A close average at one endpoint is not a bound on all partial sums.

Shuffling the diagonal weights keeps each diagonal's temporal black count, the weight distribution and
final total unchanged, but destroys spatial order. The first shuffle (seed 304) gave maximum 473;
it passed the prediction of exceeding both 100 and twice the natural maximum. This one draw alone was
not treated as a significance test.

A second pre-registered run used 1,000 shuffles, seeds 40000–40999 and eight CPU workers. Only 9 gave a
maximum no greater than 216; the plus-one randomisation value is $10/1001\approx0.009990$.
The null maxima ranged from 189 to 966, median 401. The prediction of at most 5% below the natural
statistic held; all total-preservation controls passed.

This is evidence of unusually strong cancellation in the spatial ordering of this **fixed finite list**.
It is not a probability that a density theorem is true, a test of independent Rule 30 cells, or a result
about the core. The randomisation statistic and width range were fixed before that run.

A useful new reasoning target is to bound the normalized discrepancy $U(M)/P$ in terms of the common
period $P$ for prefixes reachable from a finite left edge, across every branch. If such a bound is
small compared with $M$, it would explain collective band balance. Arbitrary periodic rings are excluded
from that proposed target by the seven-cell witness. No such bound is proved here.

### G4.4. The exact coin statement that is actually true

Under independent fair initial bits, every finite temporal trace of a fixed physical column is uniform.
Here is the standard triangular argument, spelled out to separate it from the false conditional-halving
claim caught in G3.

For the centre at time $t$, iterated left-permutivity gives

```math
x_0(t)=x_{-t}(0)\oplus G_t\big(x_{-t+1}(0),\ldots,x_t(0)\big).
```

The leftmost initial bit propagates through the unique all-rightward path and enters as XOR. Equivalently,
induct on the rule: its left-parent term carries that bit, whereas its middle and right terms have later
left endpoints. Fix the $T$ positive-index bits 1 through $T$. Given any desired trace at times 0 through
$T$, solve successively for the initial bits $0,-1,\ldots,-T$. Exactly one assignment works.
Thus each $(T+1)$-bit trace has exactly $2^T$ preimages among the $2^{2T+1}$ light-cone words, and probability
$2^{-(T+1)}$. This establishes finite-dimensional independence and fairness for that ensemble.

The fixed single-cell row supplies no fresh random leftmost bits. Conditioning on earlier forced-walk
success also supplies no guarantee that a later forced test has a new unconstrained fair bit. These are
different probability spaces; the exact ensemble theorem proves neither claim.

**Unexpected scope check: a finite seed with a biased long prefix.** Restrict the seven-periodic initial row
of the four-cycle to $[-T,T]$, with zeros outside. Finite propagation makes its centre agree with the
periodic row through time $T$. Taking $T=4q-1$ gives a finite seed with $3q$ black cells in its first $4q$
centre values, density $3/4$. This works for arbitrarily large $q$, with a different seed each time;
it says nothing about any one seed's limiting density. No seed-width-independent convergence assertion
can be inferred from ensemble balance.

The pre-registered `ensemble` check exhaustively enumerated every light-cone word for $T=0,\ldots,8$;
all trace counts were exactly $2^T$. The finite patch with $T=31$ gave `1101` repeated eight times,
24 black cells out of 32, as predicted. Both controls passed. This directly rejects the inference
that Bernoulli preservation forces every finite prefix to be half black.

### G4.5. Reproduction, failures, coordination and next lead

Probe: [rule30_gpt_balance.py](tests/probes/lexicon/rule30_gpt_balance.py), commands main, `shuffle`, `ensemble`.
Pre-registration commit `503f6dc` preceded the first run; GitHub rejected the main push and a branch push
was pending. Later remote inspection confirmed the branch publication. Its server completion before the
first run was not verified. The shuffle and ensemble pre-registrations (`88e8d22`, `c302117`) were pushed
and confirmed before their runs. The main push later succeeded. CB1 and CB3 remain recorded failures;
CB0, CB4, SH0 and EN0/EN1 passed; CB2 and SH1 held. All three commands exited 0 with `ALL CONTROLS PASS`.

Local acknowledged and corrected the G3 exact-halving error in CHAT C010 and §8.60. Local's C009 now supplies
four distinct left sides at a million diagonals, each period 32 and settling slope near 2. Those finite
measurements retain their scope. I will take the suggested open reasoning question about reset-front bounds:
what would make their sub-3 slope follow on every admissible branch? Global black density alone does not
control an adaptively sampled front. The ordered-bias target remains an open sublead of core balance.

The owner requested ongoing work without human continuation prompts. Automatic follow-ups in this chat are
active every 30 minutes, with meaningful findings and blocking failures reported. This does not alter the
shared evidence or publication standards. The shared board, ledger and chat carry this block's status and
feedback; document math checks accompany publication.


## G5. Logical audit of the new certificate-route assessment (2026-10-06)

Read Local's §8.61 after fetching it. Its practical decision to defer encoding until there is a concrete
Rule 30 candidate is reasonable. Its two general impossibility/equivalence claims do not follow. This
review supplies counterexamples to those claims; it supplies no Rule 30 termination certificate.

**Fixed dimension can carry an unbounded linear potential.** Interpret a unary symbol by

```math
A=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
A^n=\begin{pmatrix}1&n\\0&1\end{pmatrix}.
```

The upper-right entry represents word length in fixed dimension two. Deleting a unary symbol decreases
it by one. Other labels can have identity interpretations. Thus linear growth of a value with an
unbounded string does not imply an unbounded matrix dimension or prohibit a matrix interpretation.
This does not show that these particular weights rank the expanding Rule 30 walk; they do not encode it.

**Individual ranking does not imply uniform fractional population contraction.** For each seed width
$d$, take $2^d$ labelled deterministic paths, each with $2d$ countdown steps before termination. A
nonnegative ranking is the remaining count, initially $2d$, falling by one at each step. All paths
survive together until the final step. In particular, at $T=d$ and $k=d-1$, the survivor counts satisfy

```math
N_d(T+k)=N_d(T)=2^d.
```

For any fixed $c$ and $\alpha>0$, choose $d$ so that $\alpha(d-1)>c$. The proposed uniform law

```math
N_d(T+k)\le2^{c-\alpha k}N_d(T)
```

is then false, despite a linear initial ranking and certified termination of every path. A unary
countdown tail with identity-weighted binary seed labels realises this example using the fixed matrix
above. Inserting harmless free steps between countdown steps does not alter the distinction.

A ranking controls the maximum remaining length of each admissible path. A uniform contraction law
controls how an entire population is distributed across remaining lengths. The latter is an additional
quantitative assertion. It cannot be obtained merely by renaming the former log N. Nor must a ranking
predict a future forced cell's value: it must decrease on every transition that is actually admissible.

**Scope and disposition.** This is an analytic counterexample audit, not a new numerical experiment.
The observed record lengths through finite depth do not establish a length asymptotic at every depth.
No actual Rule 30 ranking, finite candidate search family suited to its transitions, or encoding has
been supplied here. Leave Q3's practical deferral intact pending such a candidate, but remove the claim
that fixed-dimension methods are generally impossible or equivalent to Q1's uniform contraction law.
Asked Local to revise their own prose; a dated note is appended under §8.61. Next substantive reasoning
intention remains the reset-front question named in G4 and CHAT C009.

## G6. Reset-front phase comparison and the remaining path cost (2026-10-06)

**Scope.** A bounded reasoning block on C009/C011's reset-front question. Fetched current shared history
before starting; no new Claude reply was present. Both fresh startup commands printed ALL CHECKS PASS;
the standard merge probe's witness summaries retain the capped-input scope recorded in G1.
The diagnostic's SF0–SF5 predictions and operational intention were pushed on `gpt/reset-front` in
`01affe1` before its first run. No Local million-diagonal job was repeated. Prior-art reading/search is
in PRIOR-ART.md's dated reset-front entry; this extends the existing Rowland/Local reset mechanism.

### G6.1. Theorem: one phase controls the conservative front within P−1

Fix a finite compatible prefix of periodic diagonal words $w_0,\ldots,w_{M-1}$ with common period $P$.
They need not have minimal period $P$. This compares the conservative reset bounds of §8.59, not actual
last transient times or different branches. Set $T_\phi(0)=0$ for integer phases $\phi$.
Let $b_k$ be a phase-independent earliest birth time for diagonal $k+1$, or zero on the full line.
For the half-line one may use $b_k=\max(0,k+1-L)$; G2's worst valid $L=1$ gives $b_k=k$.
Define

```math
 F_k(s)=\begin{cases}
 s,&w_k\equiv0,\\
 1+\min\{t\ge s:w_k(t)=1\},&w_k\not\equiv0.
 \end{cases}
```

The front is nondecreasing in $k$, so the older-parent maximum in §8.59 is redundant. Writing
$U_\phi(k)=T_\phi(k)+\phi$ gives exactly

```math
 U_\phi(0)=\phi,\qquad
 U_\phi(k+1)=F_k\bigl(\max(U_\phi(k),b_k+\phi)\bigr).
```

**Proof.** Each $F_k$ is nondecreasing and satisfies $F_k(s+P)=F_k(s)+P$. Induction therefore gives
both $U_\phi(k)\le U_\psi(k)$ for $\phi\le\psi$ and
$U_{\phi+P}(k)=U_\phi(k)+P$. For $0\le\phi<\psi<P$, put $d=\psi-\phi$.
The lifted difference is between 0 and $P$, hence

```math
 -d\le T_\psi(k)-T_\phi(k)\le P-d.
```

Since $1\le d\le P-1$, every pair of phase bounds differs by at most $P-1$.
In particular, for any chosen phase $\phi_0$,

```math
 \max_{0\le\phi<P}T_\phi(M)\le T_{\phi_0}(M)+P-1.
```

For $P=1$ there is only one phase. Birth clamps preserve the proof because $b_k+\phi$ is
nondecreasing in phase and translates by $P$.

**Consequence for the open bound.** On each admissible branched side, a bound
$T_{\phi_0}(M)\le\gamma M+O(1)$ with $\gamma<3$, together with $P(M)=o(M)$,
suffices for the worst phase to have slope below 3 eventually. The representative phase may be chosen
for each prefix, provided the proposed one-phase bound applies to that choice. This removes the
need for separate phase-speed estimates. It does not remove the all-branch quantifier, prove period
growth, or prove a speed bound. Branches have different word lists and must each satisfy the hypotheses.

### G6.2. Exact accounting: waiting zeros, not area density

For a chosen phase, let $c_k=\max(0,b_k-T_\phi(k))$ be the birth-clamp increment. Let $z_k$ be the
number of zero cells scanned before the first black cell, starting at the clamped time; set $z_k=0$
when $w_k\equiv0$. Let $W(M)$ count those identically white parent words for $0\le k<M$.
Summing the reset recurrence gives the exact identity

```math
 T_\phi(M)=M-W(M)+\sum_{k<M}z_k+\sum_{k<M}c_k.
```

Thus a sub-3 front theorem requires control of the zero-wait budget along this selected path.
An area-average or time-average black density alone does not provide it.

**Compatibility along a wait.** In an actual side, write the two parent words as $a=w_{k-2}$ and
$b=w_{k-1}$, the child as $c=w_k$. If $c(s)=0$ and the first following black is $c(s+z)=1$,
then the recurrence $c(t+1)=a(t)\oplus(b(t)\lor c(t))$ implies $a(t)=b(t)$ for
$s\le t\le s+z-2$, and $a(s+z-1)\ne b(s+z-1)$. The first range is empty when $z=1$.
Thus a nonzero waiting cost is exactly an adjacent-parent agreement run followed by a disagreement,
plus the starting zero. This is an exact necessary local condition, not yet a bound on the sum of
such costs at adaptively selected times. The toy below fails these compatibility equations.


**Counterexample to that shortcut, not to Rule 30.** Let $P=2h$ and prescribe word $w_k$ to be black
on the $h$ consecutive residues starting at $k(h+1)+h$ modulo $2h$, white elsewhere. Each word is
exactly half black. The phase-zero front begins at $T_0(0)=0$ and at step $k$ waits through exactly
$h$ zeros, so induction gives $T_0(M)=(h+1)M$. With $h=8$ the period is 16, yet the slope is 9.
For larger power-of-two $h$, the slope is arbitrarily large. These prescribed words do not satisfy
Rule 30's diagonal recurrence: the finite check below rejects them. Any argument for the actual
band must use compatibility between neighbouring words, not just their marginal densities.

### G6.3. Pre-registered finite checks

Ran `PYTHONDONTWRITEBYTECODE=1 python3 tests/probes/lexicon/rule30_gpt_front.py` on the GPT Intel CPU,
one process. First run exit 0, ALL CONTROLS PASS. All numerical values below are that run's output.

| Item | Outcome |
|---|---|
| SF0, known independent strip certificate and front endpoints | Period 16, 53,208 words certified; original worst bound 107312, birth-aware 107313, matching G2. |
| SF1, phase theorem | Passed at every prefix; maximum spread 15 in both variants. Phase-zero final bound 107308 in both variants. Thus the theorem's generic one-phase bound is 107323; exact worst bounds above are tighter. |
| SF2, blind phase coalescence | Held. First persistent singleton residue of the lifted phases is at diagonal 429; all remain singleton through diagonal 53207. |
| SF3, independent scalar bit scan | Passed for 16 phases, 1024 transitions and both boundary variants. |
| SF4, density shortcut counterfactual | Rejected: all 129 toy words half black; phase-zero bound 1152 at diagonal 128, slope 9. There are 1651 failed Rule 30 local equations, confirming the toy is inadmissible. |
| SF5, explicitly unexpected check | Passed for 256 seeded word lists, period 7, width 64, both boundary variants, including an all-white list. No power-of-two or Rule 30 premise is needed for the phase theorem. |

The observed coalescence has a precise limited meaning. In the original front, once the lifted phases
have one residue modulo $P$, their pairwise differences are 0 or $P$. With inactive birth clamps,
translation equivariance preserves those differences under every later map. Thus phase offsets can
remain fixed while the front advances. The measurement certifies this over the existing finite prefix;
it does not prove coalescence on every branch or after every period doubling.

**What moved.** Q7 remains PART. The phase quantifier in its settling requirement has an elementary
bound; the missing item is now a one-phase adaptive waiting budget, across all admissible sides, plus
sublinear period growth. Next intention: inspect the compatibility equations along successive waits
for a telescoping charge or an explicit obstruction. Local's long-run lane stays separate. No prize
solution or limiting-density theorem is claimed.

**Record check.** The first document render reported 0 TeX errors but 20 unconsumed dollar signs: this project's renderer accepts fenced display math, not double-dollar display blocks. Converted the five new blocks to the established math fences before publication. This was a document-format failure, not a scientific probe failure.

## G7. Adaptive waiting debt and a finite all-branch period tree (2026-10-06)

**Question.** Can G6's zero-wait cost be charged over intervals rather than bounded at every single
step? What does Lemma B2's backward-reading argument say about branches quantitatively?
Fetched current history and both ledgers; no new Claude replies. Both startup probes printed
ALL CHECKS PASS (standard witness-input scope as G1). Pre-registered WT0–WT5 and pushed `714d36f`
on `gpt/waiting-budget` before the diagnostic. No Local million-side computation was repeated.
Prior-art search and source scope are recorded in PRIOR-ART.md's dated G7 entry.

### G7.1. Theorem: period-P edge histories form a finite tree

Represent every temporal word by its $P$ bits indexed by absolute time modulo $P$. This includes
words whose minimal period divides $P$. Write $S w(t)=w(t+1)$ for the cyclic time shift.
A node is the adjacent pair $(a,b)=(w_{k-1},w_k)$; the root is $(0,1^P)$ at diagonal 0.
A child $(b,c)$ is allowed exactly when

```math
 S c=a\oplus(b\lor c).
```

**Unique predecessor.** The predecessor of any pair $(a,b)$ is determined by

```math
 H(a,b)=\bigl(S b\oplus(a\lor b),a\bigr).
```

There are at most two children: for a specified initial bit $c(0)$ the scalar recurrence fixes the
whole word, and a child is allowed only if it closes after $P$ steps. The root's predecessor is
$(0,0)$, whose predecessor is itself. The pair $(0,0)$ is not reachable from the root: repeatedly
reading its predecessor backward would contradict the root's black word.

No pair can occur at two different depths in the rooted graph. If one did, apply the unique
predecessor until the shallower copy reaches the root. The deeper copy then equals the root at
positive depth, so its preceding node would have to be $(0,0)$, already excluded. No two genuinely
different paths can reach the same pair at the same depth either: backward reading makes their
entire histories identical. Thus the root-reachable graph is a tree, with no reconvergence across
branches and no repeated pair along a path.

There are $4^P$ possible pairs and the zero pair is excluded. Consequently the entire rooted tree,
counting all its branches and temporal phase choices together, has at most $4^P-1$ nodes. A
compatible prefix of $K$ diagonals therefore obeys

```math
 K\le4^P-1,\qquad P\ge\tfrac12\log_2(K+1).
```

This is a quantitative consequence of Local's Lemma B2, not a separate mechanism or a priority
claim. Every finite path is realisable: construct its $P$ strip rows, which obey the closed
one-sided spatial update; take one row as a finite seed and put white cells to its right.
The right boundary cannot affect the strip. The theorem does not bound settling times.
Its inequality is a **lower** bound on period; it supplies no upper bound such as $P=o(K)$.

A fixed-P tree can be exhaustively certified rather than sampling branches. Its leaves have no
period-dividing-P extension. In the edge-generated power-of-two setting, the reset/parity
classification then forces the next period doubling. This remains a finite certificate whose
worst-case size is exponential in P, not a tractable all-period proof of the open front conjecture.

### G7.2. Pre-registered interval charging diagnostic

For the phase-zero conservative front $T(k)$, define the maximum interval debt at a specified slope:

```math
 D_\gamma(M)=\max_{0\le a\le b\le M}
 \bigl(T(b)-T(a)-\gamma(b-a)\bigr).
```

It can be computed exactly by scanning $T(k)-\gamma k$ and subtracting its minimum at earlier
indices. The diagnostic uses integer arithmetic for slopes 3, 5/2 and 2. These slopes and the
blind thresholds were chosen before the run. A bound at an endpoint alone can miss a large
interval debt; the slope-2 measurement below shows that distinction.

**Candidate sufficient condition, not proved.** On every admissible side, if
$D_{5/2}(M)\le C P(M)+O(1)$ with a finite constant C (allowed to depend on the side), and
$P(M)=o(M)$, then $T(M)\le(5/2)M+o(M)$. G6 transfers this to every phase. This would supply
the below-3 settling hypothesis used in G2's sufficient Thue–Morse exclusion criterion. The
single finite prefix below does not establish either hypothesis or cover other branches.

The local equations checked are G6.2's parent-agreement criterion. Every nonempty zero wait at
word $w_k$ has $w_{k-2}=w_{k-1}$ at the scanned times except the final transition, where they
are different. All such selected comparisons were checked. This identity does not, by itself,
charge one interval against another.

### G7.3. What ran and every outcome

Ran `PYTHONDONTWRITEBYTECODE=1 python3 tests/probes/lexicon/rule30_gpt_waiting.py`, GPT Intel CPU,
one process. First-run exit 0, ALL CONTROLS PASS. Numbers below are its recorded output.

| Pre-registered item | Outcome |
|---|---|
| WT0, certified prefix and waiting identity | Passed: phase-zero final bound 107308 at diagonal 53207; 53207 extension steps, four identically white parent words, 54105 waiting zeros. Exactly 53207−4+54105=107308. The final white word 53207 is not used as a parent in this calculation. |
| WT1, slope-3 debt at most 32 | Held: maximum 18, interval [43832,43839], elapsed 39 over seven diagonals. |
| WT2, slope-5/2 debt at most 64 | Held: maximum 26.5, interval [28738,28779], elapsed 129 over 41 diagonals. |
| WT3, parent-agreement equations | Passed: 27292 nonempty waits; all 54105 selected parent comparisons agree with the exact criterion. |
| CF, slope at most 2 on every interval | Rejected: maximum debt 1136 on [3097,51295], larger than endpoint debt 894. |
| WT4, explicitly unexpected all-branch tree check | Passed for periods 1,2,3,4,8; node totals and leaves below, no pair collision, every predecessor verified. |
| WT5, independent extension control | Passed: at every reachable node with P≤4, brute force over all possible next words agrees exactly with the two-initial-bit construction. |

| Common period P | All reachable pair nodes | Maximum last diagonal | Leaves |
|---|---:|---:|---:|
| 1 | 3 | 2 | 1 |
| 2 | 13 | 7 | 2 |
| 3 | 3 | 2 | 1 |
| 4 | 97 | 28 | 4 |
| 8 | 3065 | 399 | 8 |

The period-3 case is deliberately unexpected: a non-power-of-two common period allows the
period-1 prefix but cannot cross its first doubling. These node counts include phase-related
paths; they are not counts of different left sides up to temporal shift. In particular, the
small trees precede the first genuine side split at diagonal 53208.

No blind prediction failed in this block. The tree ceiling and no-reconvergence property are
proved for every P; the debt figures are finite measurements on the existing one-side prefix.
No all-branch sub-3 settling theorem or prize solution follows. Q7 stays PART. The next useful
reasoning target is a potential that charges these selected agreement runs, with its precise
class of compatible side prefixes stated; a bound for arbitrary half-black words is already
excluded by G6's toy.
