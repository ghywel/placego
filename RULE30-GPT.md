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

## G8. A bounded local front potential, certified through common period 8 (2026-10-06)

**Scope.** G7 proposed charging adaptive waits with a local potential. This block tests that precise
domain: compatible pairs of periodic temporal words and the current clock phase. It is about the
conservative reset front, not the forced zero-run walk of Q3. Fetched the shared history and messages;
no new Claude reply. Both startup commands printed ALL CHECKS PASS, with witness scope as G1.
Pre-registered LF0–LF5 and pushed `c3ba8e5` before the first diagnostic. Its outcomes and the LP0–LP2
potential addendum were pushed in `29c1d70` before the second run. No Local long run was repeated.

### G8.1. Graph and certificate inequality

For a chosen common period P, a vertex is $v=(a,b,r)$, two P-bit temporal words and arrival phase
$r\in\{0,\ldots,P-1\}$. Allow an edge to $v'=(b,c,r')$ precisely when
$S c=a\oplus(b\lor c)$, the actual Rule 30 diagonal equation. Define

```math
 \delta(b,r)=\begin{cases}
 0,&b\equiv0,\\
 1+\min\{d\ge0:b(r+d)=1\},&b\not\equiv0,
 \end{cases}
 \qquad r'=(r+\delta(b,r))\bmod P.
```

Here the full-line periodic-parent front advances by $\delta$. There are $P4^P$ vertices and
exactly $P4^P$ edges counted across the whole graph: each child pair has a unique predecessor
by G7, and each predecessor arrival phase specifies its target phase. A vertex can have zero,
one or two forward child choices; phases may merge. This counts all pairs, including ones that
are not edge-generated, and all allowed choices, not sampled seeds.

Seek a nonnegative integer potential h satisfying every edge inequality

```math
 h(v)\ge 2\delta(b,r)-5+h(v').
```

**Certificate implication, proof.** Sum these inequalities along any compatible path of m edges.
The potentials telescope, giving

```math
 T(m)-T(0)\le\tfrac52 m+\tfrac12\bigl(h(v_0)-h(v_m)\bigr)
 \le\tfrac52 m+\tfrac12\max_v h(v).
```

The same holds on every interval, starting at any vertex and any phase. Once such an h is
verified on the finite graph, this is a bound for **all path lengths**, not just the paths used
while constructing h. The word sequence need not be spatially periodic. It must have common
temporal period P and satisfy the compatibility equation at every extension.

The constructor starts h=0 and propagates increases backward until no inequality can improve.
A bounded solution exists if no cycle has positive weight for weights $2\delta-5$: removing
nonpositive cycles bounds every walk reward by a finite simple-path maximum. The first diagnostic
checked all pair cycles and their finite phase maps, finding maximum mean below 5/2 at the
periods tested. The second run verifies the final inequality on **every edge** regardless of
how h was obtained. For P≤4 it additionally constructs forward edges from the two initial bits
and checks them independently. Potential arrays are reconstructed by the script and are not
stored in git. This is an exact finite computer certificate, not a formal proof-assistant result.

**Computed finite theorem.** For P=1,2,3,4,8, the verified values of max h are respectively
0,0,2,6,45. Therefore every compatible full-line periodic-parent front at those common periods
has interval debt above slope 5/2 at most 0,0,1,3,22.5, respectively. In particular,
for common period 8, $T(b)-T(a)\le(5/2)(b-a)+22.5$ for every interval and every path.

This certificate does **not** cover arbitrary P. Its graph size is exponential, and neither a
uniform formula nor a bound max h=O(P) has been proved. Birth clamps are absent from this graph;
the separate finite edge-tree check below includes them. An arbitrary-period argument would
also have to retain G2/G6's all-branch, birth and sublinear-period qualifications.

### G8.2. A genuine compatible cycle obstructs slope-2 local charging

The following list gives the integer encodings of twelve successive P=4 temporal words,
least significant bit first in time:

`[9, 8, 14, 12, 4, 7, 6, 2, 11, 3, 1, 13]`.

Repeat it spatially. Every triple satisfies the diagonal equation cyclically. Starting the
front in phase 3, its twelve increments are

`[1, 4, 2, 1, 4, 2, 1, 4, 2, 1, 4, 2]`.

They sum to 28 and return to phase 3. Thus the front's exact long-run slope is $28/12=7/3$.
Starting instead at phase 0 gives a transient first circuit of 27 steps and then enters phase 3;
the slope concerns the recurrent circuit, not that first transient. These lists are expansions
of the first run's reported witness pair 217, spatial period 12, using the same exact certificate.

Any bounded potential that charges these same allowed edges at slope $\gamma<7/3$ is impossible:
summing its proposed inequality around this recurrent cycle would give
$28\le12\gamma$, a contradiction. In particular, slope 2 cannot be obtained on the entire
locally compatible domain merely by selecting a different bounded local potential.

This is stronger than G6's inadmissible half-density toy: the cycle really satisfies Rule 30's
local equations. It is a spatially periodic infinite background, not an edge-generated side,
and not a finite-seed prize counterexample. G7 proves such a pair cycle is unreachable from the
black edge root. An edge-sensitive slope-2 argument is not refuted by it.

**Why the clock phase is essential.** Suppose instead that the potential is a bounded function
$g(a,b)$ of just the two temporal words, required to charge every allowed phase at slope $\gamma$.
On the twelve-word cycle above, the maximum next-black delays over phases are
`[3,4,2,3,4,2,3,4,2,3,4,2]`: a word with one black bit has maximum gap 4; the other listed words
have maximum gaps 3 or 2 as shown by their four bits. Their sum is 36. Applying the proposed
word-only inequality separately at each edge's worst phase and summing around the spatial cycle
would give $36\le12\gamma$. Thus $\gamma\ge3$ is necessary. In particular, **no word-only
potential on the full compatible domain can supply the below-3 bound**, even though carrying
clock phase makes slope 5/2 feasible at these small periods. Choosing each worst phase separately
is not a claim about a coherent physical front; it is valid because a phase-free certificate
would be required to satisfy all of those individual inequalities. An edge-restricted domain
or a potential carrying history is outside this obstruction. This is an exact algebraic
consequence of the displayed compatible witness, not a further blind statistical experiment.

### G8.3. Both pre-registered runs, every outcome

Commands: `PYTHONDONTWRITEBYTECODE=1 python3 tests/probes/lexicon/rule30_gpt_local_front.py`, and
the same with `potential` appended. GPT Intel CPU, one process. Both exited 0 and printed
ALL CONTROLS PASS. Every blind prediction held; both counterfactuals were rejected.

| Common P | Complete edge-tree nodes | Maximum slope-5/2 debt, full / births | All pair cycles | Maximum cyclic front mean |
|---|---:|---|---:|---|
| 1 | 3 | 0 / 0 | 1 | 0 |
| 2 | 13 | 0 / 1/2 | 2 | 1 |
| 3 | not part of edge-tree run | not run | 2 | 7/6 |
| 4 | 97 | 1/2 / 1/2 | 4 | 7/3 |
| 8 | 3065 | 7 / 7 | 24 | 7/3 |

LF0 reproduces G7's complete node counts. LF1's debt-at-most-4P prediction holds on every
edge-tree path in both variants; the P8 maximizing witness has last diagonal 281, arrival 549,
parent word 144 and child word 250. LF2 checks every cycle's local equations and exact phase
means. LF3/LF4 predict means at most 5/2, all held. LF4 is the explicitly **unexpected odd-period
check**. LF5's independent bit predecessors and scalar front scans agree for P≤4.
The first counterfactual detects slope 4 for the repeated single-bit P4 word 1 and rejects its
constant-spatial-pattern compatibility equation.

| Common P | All augmented states / verified edges | max h | Certified interval debt bound | Maximizing state (a,b,r) |
|---|---:|---:|---|---|
| 1 | 4 / 4 | 0 | 0 | (0,0,0) |
| 2 | 32 / 32 | 0 | 0 | (0,0,0) |
| 3 | 192 / 192 | 2 | 1 | (3,2,2) |
| 4 | 1024 / 1024 | 6 | 3 | (3,2,2) |
| 8 | 524288 / 524288 | 45 | 45/2 | (27,12,4) |

LP0's full edge inequalities and independent small forward-edge checks all pass. LP1's
max h/2≤4P prediction holds at every tested P. LP2 rejects the zero potential on a **valid**
P4 edge: (1,1,1) to (1,0,1) has delay 4 and positive weight 3. Thus the certificate needs
nonzero potential values; simply assigning a unit cost would miss a real local slow step.

**What moved.** There is now a named, fully checked local potential for the small-period front,
covering all compatible paths rather than one measured side. Its mathematical extension is
open: bound the potentials uniformly as P grows, or find an obstruction in that broader
compatible class and use edge reachability instead. Q7 remains PART. No ranking of the LR
forced walk, no prize solution and no unbounded-period settling theorem are claimed.

## G9. Birth clamps inherit an all-interval front budget (2026-10-06)

**Question and scope.** G8 left birth correction outside its full-line certificate. This block proves
an elementary transfer lemma, extending that certificate without a second graph. Read the current
history, standing workflow, PERIOD-TWO.md and both shared ledgers; fetched main with no new Claude
reply. Both startup checks printed ALL CHECKS PASS, with the capped witness scope of G1.
BR0–BR3 and the endpoint-only counterfactual were pushed in `54592f2` before running the diagnostic.
This is a theorem about the conservative front, not actual settling times or a prize solution.

### G9.1. Maximum over restarts: exact identity

Fix the temporal words and phase. Write $F_j(s)=s+\delta(w_j,s\bmod P)$ for the next-black map,
with $F_j(s)=s$ for an identically white word. These maps are nondecreasing on integer times:
starting later cannot find an earlier next black. The same holds after a fixed phase shift.
Put $G_{a,b}=F_{b-1}\circ\cdots\circ F_a$ and $G_{a,a}(s)=s$. Let birth barriers be $b_j$,
and define $T_0=0$ and $T_{j+1}=F_j(\max(T_j,b_j))$. Then, for $k\ge1$,

```math
 T_k=\max\left\{G_{0,k}(0),\ \max_{0\le j<k}G_{j,k}(b_j)\right\}.
```

**Proof.** On a totally ordered domain, a nondecreasing map preserves a finite maximum:
$F(\max(u,v))=\max(F(u),F(v))$. At each step distribute $F_j$ over the old maximum and the
new barrier. Induction gives the displayed formula, including the original start and each
restart at its own barrier. The barrier need not increase with j. This is the usual maximum
expansion of a reflected recurrence, applied here to next-black maps; no novelty is claimed
for that order argument (PRIOR-ART.md records the limited reading).

### G9.2. Transfer theorem and the precise quantifiers

Suppose $C\ge0$, $\gamma\ge1$, and the unclamped front has the **same** budget for every
interval and every starting time:

```math
 G_{a,b}(u)-u\le\gamma(b-a)+C
 \qquad(0\le a\le b,\ u\in\mathbb Z).
```

For periodic words it suffices to check u in every residue class, because the maps commute
with translation by P. Suppose also $b_j\le j$. Every restart term obeys

```math
 G_{j,k}(b_j)\le b_j+\gamma(k-j)+C
 \le\gamma k+C-(\gamma-1)j\le\gamma k+C.
```

The original-start term has that same bound. Taking their maximum proves
$T_k\le\gamma k+C$ **including all birth clamps**. No per-birth penalty is added. Rule 30
compatibility is needed to obtain the budget from G8, but not for this transfer lemma.

For the normalized half-line recursion of G2/G6, $b_j=\max(0,j+1-L)$ with $L\ge1$,
so $b_j\le j$. Thus the theorem applies. Any already required initial-time offset remains
part of the normalization; this does not assert that all physical cells settle at time zero.

On an interval of the birth-clamped front, the same expansion starting at a gives

```math
 T_b-T_a\le\gamma(b-a)+C+\max(0,a-T_a).
```

For L=1, $T_a\ge a-1$ for $a\ge1$, since the preceding update starts at its birth barrier
and never decreases time. Hence the extra term is at most 1; at a=0 it is zero.
For general L, $T_a\ge\max(0,a-L)$ gives an extra term at most L. These interval statements
are weaker than the absolute bound at the normalized origin; the distinction matters.

**New consequence of the existing finite certificate.** G8 supplies the all-interval,
all-phase budget with $\gamma=5/2$ and C=0,0,1,3,22.5 for common P=1,2,3,4,8 respectively.
Consequently **every compatible path at those common periods**, of arbitrary length, has
birth-clamped $T_k\le(5/2)k+C$ under the normalized schedule above. At P=8 the absolute debt
is at most 22.5; every birth-clamped interval has debt at most 23.5 for L=1, or 22.5+L generally.
These are rigorous consequences conditional on G8's exactly checked finite edge inequalities,
not an extrapolation of the random diagnostic or the finite edge trees. Compatible pairs
need not be reachable from the black edge root; the broader G8 domain already covers them.

An unbounded-period certificate with C(P)=O(P), slope below 3 and P=o(M) would therefore carry
its birth correction automatically. Neither the uniform certificate nor sublinear periods
has been proved. A bound only from one original start, even at every prefix, is insufficient.

### G9.3. Diagnostic, failed shortcut and unexpected check

Ran `PYTHONDONTWRITEBYTECODE=1 python3 tests/probes/lexicon/rule30_gpt_birth_restart.py`,
one GPT Intel CPU process, standard library, exit 0, ALL CONTROLS PASS. BR0–BR3 are theorem
controls, not blind evidence. Seed 2026100609 generates 24 word lists of length24 at each
P=1,2,3,4,7,8. Each list uses L=1,2,5 barriers and a fourth barrier that is j at multiples
of 3 and zero otherwise. All phases and prefixes are checked. Words may be incompatible;
this deliberately tests the generic transfer theorem independently of Rule 30 assumptions.

The budget C is computed by independent scalar scans of every unclamped interval at every
starting residue. Birth updates use waiting tables. A third calculation scans every restart
suffix and checks exact equality to their maximum. All 57600 scalar/restart/bound comparisons
passed; counts by P are 2304,4608,6912,9216,16128,18432. Largest doubled interval debt was 21.
No control failed. **Unexpected check:** odd P=7 and the barrier that repeatedly falls to zero
both pass; monotonicity is required of the clock maps, not of the barriers.

**Counterfactual rejected, with exact witness.** At P=16, take four white words followed by
word1. From time 0 the unclamped front stays 0 then ends 1, obeying every original-prefix
slope-5/2 bound with debt0. With $b_j=j$, the last word is entered at time 4, its next black
is at time 16, and the result is 17, exceeding $(5/2)\times5=12.5$. This is a generic-map
counterexample to replacing the all-phase, all-interval hypothesis by an endpoint-only
hypothesis. The word list is not claimed to be a compatible Rule 30 side.

**What moved.** Birth transfer is now DONE as a lemma. The local-potential lead remains PART:
its missing ingredients are a uniform arbitrary-period budget and sublinear period growth,
or an edge-sensitive substitute if broader compatibility obstructs that budget. Next
reasoning intention: use simultaneous temporal rotation to express the phase-aware potential
on clock-aligned word pairs; this retains phase information while removing the redundant
factor P in the finite graph. No Local long run was duplicated or requested.

### G9.4. Next lead advanced: clock alignment removes a redundant factor P

There is a second exact reduction, without a new computation. Let S rotate a temporal word
by one time step, so $(S a)(t)=a(t+1)$. Replace $(a,b,r)$ by the clock-aligned pair
$Q(a,b,r)=(S^r a,S^r b)$. If these words are A,B, let $d=\delta(B,0)$. Its allowed quotient
edges are precisely

```math
 (A,B)\longrightarrow(S^d B,S^d C),
 \qquad S C=A\oplus(B\lor C),\qquad \text{weight }2d-5.
```

**Proof of equivalence.** Simultaneously rotating the three words preserves the compatibility
equation. The change $R_t(a,b,r)=(S^t a,S^t b,r-t\bmod P)$ preserves delay, edges and Q.
Its action is free because the phase coordinate changes, even if the words have smaller
fundamental period. Each orbit has P vertices. Every quotient edge lifts at r=0, and every
original edge projects to the displayed edge. Thus the quotient has $4^P$ vertices and
$4^P$ edges, counted with allowed choices, instead of $P4^P$ each.

Any quotient potential g lifts to $h(a,b,r)=g(Q(a,b,r))$ with exactly the same inequalities.
Conversely, from any nonnegative integer certificate h, form
$\bar h(v)=\max_{0\le t<P}h(R_t v)$. Each rotated edge has the same weight; taking maxima
on its inequalities proves $\bar h(v)\ge2d-5+\bar h(v')$. This certificate is invariant on
orbits, descends to g, and has exactly the same global maximum as h. Hence the two graphs
admit certificates with **identical optimal maximum potential**. No computation of a new
potential is claimed. The unaligned unique-predecessor property need not survive projection.

This does not evade G8's phase-free obstruction. The aligned words encode the arrival phase,
and the target words rotate by the actual delay; they are not the original pair at the next
spatial index. At P=8 this proves that a certificate with maximum 45 exists on 65536 aligned
pairs, from the already checked 524288-state certificate. At P=16 the quotient still has
$4^{16}=4294967296$ vertices: this factor-P reduction is not an efficient arbitrary-period
algorithm. Next open target: an analytic potential or smaller sufficient summary on aligned
pairs with a uniform period-scaled bound. No Local computation is requested.

## G10. Exact aligned certificates through period 10, with two failed bounds (2026-10-06)

**Question.** Before guessing an analytic potential, audit two necessary properties of the G8/G9
candidate on the broader compatible domain: its cycle slope and its interval-debt range. This is
GPT's reasoning/certificate lane, not Local's million-diagonal side computation. Read the current
standing rules, PERIOD-TWO.md and shared messages; fetch found no new Claude replies. Both startup
checks printed ALL CHECKS PASS, with G1's existing capped witness scope. The tools reuse G7's
predecessor, G8's cycle reasoning and G9.4's quotient; no new external theorem was imported.

CC0–CC4 were published in `1120bb8` before the first run. Its outcomes and AP0–AP2 were published
in `9144d5c` before the aligned run. Certificate-expansion controls CC5/AP3 were written before
the third command. Commands, from the repository root:

- `PYTHONDONTWRITEBYTECODE=1 python3 tests/probes/lexicon/rule30_gpt_cycle_obstructions.py`
- the same command with `potential` appended;
- the same command with `witness` appended.

All used one GPT Intel CPU process, standard library; no GPU measurement, Local job or stored
potential array. The run scope is common temporal P=1 through10, including periods which cannot
occur as edge-generated powers of two. The latter distinction is kept throughout.

### G10.1. Complete finite domain and every prediction

| P | All pair / quotient states | Pair cycles | Cyclic pair states | Exact maximum clock-cycle mean | Least nonnegative max h | Exact full-line interval debt bound |
|---|---:|---:|---:|---|---:|---|
| 1 | 4 | 1 | 1 | 0 | 0 | 0 |
| 2 | 16 | 2 | 3 | 1 | 0 | 0 |
| 3 | 64 | 2 | 37 | 7/6 | 2 | 1 |
| 4 | 256 | 4 | 43 | 7/3 | 6 | 3 |
| 5 | 1024 | 9 | 416 | 15/8 | 10 | 5 |
| 6 | 4096 | 12 | 1329 | 5/2 | 21 | 10.5 |
| 7 | 16384 | 6 | 5895 | 5/2 | 37 | 18.5 |
| 8 | 65536 | 24 | 16043 | 7/3 | 45 | 22.5 |
| 9 | 262144 | 23 | 44002 | 1006/493 | 59 | 29.5 |
| 10 | 1048576 | 33 | 75698 | 89/41 | 97 | 48.5 |

**CC0 passed.** Every spatial cycle was checked bit by bit against the Rule30 diagonal equation;
every maximizing recurrent clock loop was independently scanned and closed. Known maxima at
P=1,2,3,4,8 matched G8. All clock means at P≤5 were additionally compared with independent
scalar scans, not only their maximizing witnesses. Unique predecessor makes the complete pair
cycle enumeration exhaustive; no sampling or spatial-length cutoff is used.

**CC1 failed at P6 and P7:** the proposed plateau7/3 is false. It held at the other eight periods.
**CC2 held:** every tested mean is at most5/2. **CC3 held:** every tested mean is strictly below3.
Neither implies a theorem at arbitrary P or a small transient-debt budget. **CC4 passed:** bit
repetition lifts the P4 witness to P8 with the same exact mean7/3. The valid-cycle slope2
counterfactual was rejected. **Unexpected check:** non-power-of-two P5,7,9 were included; P7,
unlike P8, attains exactly5/2, revealing a real zero-weight cycle for that slope.

**Harness limitation retained.** The first shell command ran Python into a log and then printed
the log without preserving Python's exit status. Its wrapper returned0. The script's return
expression is1 after CC1 fails, but the original Python process status was not captured; it is
not reported as observed. The potential and witness wrappers explicitly saved and propagated
Python's status; both returned1 because AP1 failed, while both printed ALL CONTROLS PASS.
These failures concern blind bounds, not broken instruments.

**AP0 passed.** For every child pair (b,c), obtain its unique predecessor (a,b), calculate
$d=\delta(b,0)$, and emit the quotient edge $(a,b)\to(S^d b,S^d c)$ with weight2d−5.
This enumerates exactly $4^P$ edges. Reverse relaxation from0 gives nonnegative integer g;
the final inequality $g(v)\ge2d-5+g(v')$ was checked on **every quotient edge**. At P≤8,
an independent forward-child construction checks the lift at every phase on the original
augmented graph. G8's known maxima all match. No cap of50million edge attempts was reached;
P10 used1939298 attempts and1114920 successful increases.

**AP1 failed at P10:** max h/2=48.5 exceeds4P=40. It held at P1 through9. **AP2 passed:**
zero potential is rejected on a valid P4 delay4 edge. **CC5/AP3 passed:** independently expanded
scalar certificates below verify the tight mean5/2 cycle and a path attaining debt48.5.
Every failure is retained in the probe header; there is no revised post-run prediction.

### G10.2. A valid period-7 cycle forces slope at least 5/2 on the broader domain

**Reachability clarification, answering Local C019:** this spatial cycle is unreachable from the finite left-edge root of G7. Every pair has a unique predecessor, and the witness's predecessors stay on its cycle; they cannot reach the root and its zero predecessor. The 5/2 below constrains broader-domain certificates, not the slope of a finite-seed side. No original/flipped/boundary four-branch certification is supplied by this witness.

The fourteen temporal words, least significant bit first in time, are

`[97,101,56,57,14,46,67,75,112,114,28,92,7,23]`.

Every cyclic triple is compatible. At recurrent clock phase2, one circuit advances35 steps
and returns to phase2 modulo7. This is the scalar certificate printed by `witness`; the
spatial period is14. If a bounded potential on the full compatible phase graph charges all
edges at slope gamma, summing around this clock cycle gives $35\le14\gamma$.
Therefore $\gamma\ge5/2$. This strengthens G8's7/3 lower bound for the **all-period, broader**
compatible domain. It does not refute a lower slope on powers-of-two periods or edge-generated
sides: P7 is not such a period, and G7 already excludes spatial pair cycles from the edge root.
The candidate slope5/2 is attained, rather than refuted, by this cycle.

### G10.3. A 39-edge period-10 witness refutes the proposed constant 4P

AP3 follows tight quotient inequalities from the maximizing aligned pair (142,648) to a state
with potential0. It then undoes each clock rotation to recover actual temporal words. In order,
they are

`[142,648,11,782,521,522,14,11,10,2,1011,995,32,642,831,762,394,672,755,190,153,202,238,72,843,527,392,778,271,11,521,13,9,8,14,12,4,1015,999,32,698]`.

The first word is the older parent; the next39 words supply the delays and the final word is
the last child. Starting at clock phase0, the exact delays are

`[4,7,1,2,6,2,2,8,10,3,1,10,2,1,1,2,4,1,1,3,1,1,1,3,3,4,5,2,1,2,7,3,10,8,1,10,2,1,10]`.

Every one of the39 triple equations was checked for all10 time residues. Independent scalar
next-black scans give total146, so

```math
 146-\tfrac52\times39=48.5>4\times10=40,
 \qquad 2\times146-5\times39=97.
```

This is an exact finite counterexample to debt≤4P on arbitrary compatible periodic-word
intervals. It refutes that proposed constant, not the existence of some bound C(P)=O(P).
It is not an edge-generated path or a finite-seed prize counterexample. Period10 also cannot
by itself refute the powers-of-two version. A finite path with a relatively high average is
not an asymptotic slope counterexample; P10's largest recurrent slope is only89/41.

**Why the certificate bound is sharp, rather than an artifact of relaxation.** Starting from0,
every reverse increase stays below every feasible nonnegative integer potential: if the child
value is at most that potential, so is weight plus child value at its parent. At termination
g is feasible, hence the least such potential pointwise. Independently, the displayed path's
reward97 forces any potential range to be at least97 by telescoping. The verified potential
has range97. Thus the exact maximum interval excess at slope5/2 in this common-P10 domain is
48.5; the path attains it and the certificate bounds all other paths.

### G10.4. What moved and what remains

G9.4's quotient has now been implemented and fully certified at **every common P≤10**.
The table's C=max h/2 bounds every full-line interval at slope5/2, for all compatible path
lengths. G9 transfers each budget to the normalized birth front with the same absolute C;
L1 birth intervals cost at most C+1, or C+L for general L. This is a finite computer-certified
theorem with a written transfer proof, not an extrapolation from a measured edge prefix.

The broad analytic target must accept slope at least5/2 and a constant larger than4 in a
putative C(P)≤constant×P. No uniform linear bound is proved, and the edge-generated power-of-two
version remains a separate, potentially stronger target. Q7 and the local waiting-potential
lead remain PART. Next reasoning intention: isolate which restrictions the edge root imposes
on clock-aligned pairs before choosing an analytic potential family. A large unrestricted
period16 computation is not proposed; no new Local run is requested.

## G11. Condrey's two mechanisms and what survives the first hole (2026-10-06)

**Asked by Local in CHAT C018, at the owner's request.** Read Condrey's full seven-page
[Finite Configurations Cannot Generate a Constant Trace in Rule30](https://arxiv.org/pdf/2609.09431),
including the proofs, sharp horizons and the limits of its partial formalization. Read the current
standing workflow, PERIOD-TWO.md and ledgers; both startup checks printed ALL CHECKS PASS, with
G1's capped witness scope. Local keeps the one-hole record runs; none was duplicated.
CH0–CH4 were pushed in `5097375` before the small scalar verification. A concurrent Local
Collatz split was merged, preserving both parties' rows and Local's new references.

### G11.1. The latch belongs to the zero wall, not the one wall

There are two distinct mechanisms in Condrey's proof. Let the prescribed centre be tau,
its right neighbour sigma, and the next right column rho. A genuine right evolution satisfies

```math
 \sigma(t+1)=\tau(t)\oplus\bigl(\sigma(t)\lor\rho(t)\bigr).
```

For a **zero wall**, this is an OR latch: sigma cannot fall from1 to0. In Condrey's
zero-trace classification, the first right-hand1 advances towards the wall until the right
neighbour latches at1; the compatible left row acquires an infinite alternating tail.
His triangular uniqueness lemma identifies that completion with the only possible left row.
For a **one wall**, the update is the complement of that OR: sigma=1 necessarily becomes0.
Here Condrey instead gives a universal fixed checkerboard on the left, independent of the
right half. An eventual-one column forces an eventual-zero left neighbour, giving his short
constant-trace exclusion as well. These mechanisms must not be conflated.

The latch statement is about a right column belonging to an actual Rule30 evolution, with
rho present. In our stronger LR problem, an arbitrary proposed sigma need not satisfy that
right equation. The constant-one left checkerboard works for arbitrary sigma because the
wall masks it; a right-column monotonicity claim cannot silently be imposed on every LR input.
This is the precise qualification to C018's phrase "next to a constant wall".

### G11.2. Exact prefix theorem for one hole per period

Let $p\ge3$, $\tau(t)=0$ precisely at multiples of p, and $h_n=1-\sigma(np)$. At each hole
time np the first p−1 cells of the forced left row are exactly the truncation of

```math
 (h_n,h_n,1-h_n,1,0,1,0,1,\ldots).
```

In particular, once depth4 is reached, every even depth through p−1 is black and every odd
depth through p−1 is white, independently of all hole inputs. This is a finite-prefix
statement for every p and every sigma, not a claim about the whole infinite row.

**Proof.** The inverse recurrence, with $v_0(t)=\tau(t)$ and $v_{-1}(t)=\sigma(t)$, is

```math
 v_j(t)=v_{j-1}(t+1)\oplus\bigl(v_{j-1}(t)\lor v_{j-2}(t)\bigr),\qquad j\ge1.
```

Induction shows that depth j at time t uses only tau on $[t,t+j]$ and sigma on
$[t,t+j-1]$. On a window where tau is all1, the forced columns have the checkerboard values
$v_j(t)=1$ for even j and0 for odd j: verify the recurrence directly, starting with $v_1=0$.
Immediately after the hole, tau is1 for p−1 times. Thus at time np+1 the cells
$y_j=v_j(np+1)$ equal the checkerboard for $1\le j\le p-2$.

Write $x_j=v_j(np)$ and $x_0=0$. The centre equation gives $x_1=h_n$. Running one step
backwards along the left row gives

```math
 x_{j+1}=y_j\oplus(x_j\lor x_{j-1})\qquad(1\le j\le p-2).
```

Since $y_1=0$, $x_2=h_n$. If the relevant depths exist, $y_2=1$ gives
$x_3=1-h_n$, and $y_3=0$ gives $x_4=(1-h_n)\lor h_n=1$. The remaining updates preserve
$x_j=1$ at even j and0 at odd j. This proves exactly the displayed prefix, including the
short truncations p3 and p4.

The same calculation describes the **whole** initial left row for a single transient white
cell followed by an all-one wall. That special trace is eventually constant and is already
excluded by Condrey; its prefix is the comparison object here. The periodic one-hole wall
agrees with it only until the next hole enters the inverse cone.

**Support consequence.** If the initial left row is zero at every depth greater than L,
then for $p\ge5$ a one-hole wall beginning at its white phase requires

```math
 L\ge 2\left\lfloor\frac{p-1}{2}\right\rfloor
 =\begin{cases}p-1,&p\text{ odd},\\p-2,&p\text{ even}.\end{cases}
```

The indicated even cell lies in the forced prefix and is black. This excludes every such
left support smaller than the bound, independently of the right half. It is a range where
the extension gives a theorem: sufficiently long black blocks exclude a specified shallow
left support. It is not LR at a fixed p with unbounded L. If the initial phase is different,
normalize to a hole by a forward time shift and account for the resulting support growth;
do not apply the same L to a shifted row without correction.

### G11.3. Exactly what breaks, with a finite counterexample

The no-hole checkerboard is not preserved by the first white cell. For p4 and sigma(0)=1,
the forced initial left prefix is `[0,0,1]`, rather than `[0,1,0]`. This is not merely an
incompatible right-column toy: the finite row with ones exactly at positions−3 and1 has
centre trace `01110` through time4. It realizes the first one-hole period and the next white
cell, while its initial left row begins with two zeros. No infinite periodic trace is claimed.

The first-column formula pinpoints the change, for arbitrary p≥3:

```math
 v_1(t)=\begin{cases}
 1-\sigma(t),&t\equiv0\pmod p,\\
 1,&t\equiv p-1\pmod p,\\
 0,&1\le t\bmod p\le p-2.
 \end{cases}
```

Even before a hole, the required black pre-hole cell replaces the constant-one neighbour0;
at the hole itself the right input becomes visible. The zero-wall OR latch does not repair
this: throughout the black part of our wall, a black right neighbour is forced to turn white.

What *does* survive is the depth-p−1 comparison prefix of G11.2. The attempted infinite-tail
proof fails at the next hole: at time1, invoking the all-one checkerboard at depth p−1 would
need tau(p)=1, but tau(p)=0. In the original row this opens depth p and beyond to a new
deterministic hole defect; the next visible bit sigma(p) first becomes available at depth p+1.
Sparse freedom counts how many inputs can enter a cone. It does not bound how far the resulting
nonlinear differences persist, or supply a decreasing quantity across successive holes.

**Unexpected exact obstruction to an overly strong ordering claim.** At the white phase of
0101 (p2), the first two cells are $1-\sigma(0),\sigma(0)$, so the maximum zero run starting
at depth1 is1. For the lower-freedom wall0111 (p4), the prefix theorem makes that maximum
exactly2. Thus less freedom does **not** monotonically decrease every fixed-depth record.
This does not contradict Local's late-depth statistical comparison or its proposed scaling.
Phase and depth matter; freedom is a useful parameter rather than a pointwise ordering theorem.

### G11.4. What ran, incoming measurements and the missing statement

`PYTHONDONTWRITEBYTECODE=1 python3 tests/probes/lexicon/rule30_gpt_condrey_holes.py` ran on
one GPT Intel CPU process, exited0 and printed ALL CONTROLS PASS. CH0 checked the two boundary
updates on all Boolean inputs and32 random constant-one fibres. CH1/CH2 checked7936 complete
prefixes: p3 through64, four hole times each,32 sigma lists per period from seed2026100611.
CH3 independently evolved the finite row with ones at−3 and1, giving trace01110. CH4 checked
the unexpected p2/p4 fixed-depth reversal. The counterfactual that the first hole preserves
the old universal checkerboard was rejected. There were no blind asymptotic predictions,
and the theorem is proved above rather than inferred from these tests.

Local's shared output currently contains, among other points, R(011,96)=39,
R(0111,128)=43 and R(01111,160)=30, from the ongoing holes run. These belong to Local;
this block did not recompute them. The prefix theorem imposes no universal R(d)≤1 law,
and is consistent with those longer runs far from the origin. A complete H0–H3 OUTCOME and
§8.62 were not yet present when this block read the shared version, so this is not a report
that Local's whole run passed. No bound of order d/(p−1) is proved here.

**Deliverable.** The constant-wall mechanisms are separated; the unchanged-fibre extension
fails at the first hole with an explicit finite witness; a uniform initial-prefix and shallow
support exclusion survive for every p≥5. The one-hole LR lead remains PART. The exact next
missing step is a cost for repeated hole defects after the comparison cone crosses the next
hole, not another invocation of the zero-wall latch. C020 replies to Local with this distinction
and proof. Further one-hole computations remain Local's lane.

**Incoming measurement update before publication (2026-10-06 07:07 BST).** Fetched and merged `6d7b0fd`:
Local's complete H0–H3 OUTCOME and §8.62 are now present. H0 and CF passed; H1's finite
no-cap prediction and H3's finite upper bound held at all24 points; H2's two-point slope band
was refuted. The deepest (p,d,R) triples are (3,96,39), (4,128,43), (5,160,30), (6,192,32),
(7,224,31), (8,256,31). All are Local M5 measurements with32 free bits. This completes the
measurement side of C018, without promoting the tested LR statement to all depths. The
prefix proof neither contradicts these records nor supplies their unbounded continuation.
Both parties' operational rows were preserved, and the shared Condrey-end board row is PART.

## G12. A hole bit is shielded beyond three cells of its own row (2026-10-06)

**Question and scope.** C021 reported that individual hole effects can spread and cannot generally be
superposed. This block asks exactly where two inputs interact, rather than retrying the ray proposal.
Fetched and merged03bf7bc, read C021 and the shared board; both standard startup probes printed ALL
CHECKS PASS (existing witness scope as G1). Reused §8.2 Lemma4's triangular input formula and G11's
prefix calculation. No Local record search was repeated. Predictions HI0–HI4 were pushed in9ce2aa8;
a subsequent theorem-control addendum was pushed in5127719 before its run.

### G12.1. Exact local shielding theorem

Suppose a prescribed wall has a white cell at time q followed by at least four black cells:

```math
 \tau(q)=0,\qquad \tau(q+1)=\tau(q+2)=\tau(q+3)=\tau(q+4)=1.
```

Take two arbitrary right columns sigma that differ only at q. Their forced left rows **at time q**
differ exactly at depths1,2,3, and agree at every depth4 and beyond. No condition is placed on the
wall or right column after q+4. Thus this holds at every hole of a one-hole wall with p≥5.

**Proof.** Write $x_j=v_j(q)$ and $y_j=v_j(q+1)$, where depth0 is the wall. The future columns y
are identical in the two constructions: inverse causality uses only sigma at times at least q+1.
The four-black window and G11's calculation give

```math
 x_1=h,\quad x_2=h,\quad x_3=1-h,\quad x_4=1,\qquad h=1-\sigma(q).
```

The next cell is determined by

```math
 x_5=y_4\oplus(x_4\lor x_3)=y_4\oplus1.
```

It is therefore identical in both rows. Once the two preceding x cells agree and the y cell
agrees, the recurrence $x_{j+1}=y_j\oplus(x_j\lor x_{j-1})$ gives agreement at the next cell.
Induction proves equality at all depths≥4. The first three displayed cells each flip. This
proves an infinite-depth statement about a **single input at its own time**, not one-hole LR.

For a wall beginning at its white phase, the entire time0 tail beyond depth3 ignores sigma(0),
whatever all later hole inputs are. In particular, sigma(0) has no mixed Boolean interaction
with any later input in that tail. This is stronger than a finite observation of no interaction.
It does not say that a bit injected at time q>0 changes only three cells of the time0 row:
propagating its modified row backwards through q time steps is a different operation. C021's
late-hole spreading and nonlinear effects remain compatible with the theorem.

### G12.2. An exact identity at the second input's leading edge

For the wall beginning at a hole, let a=sigma(0), b=sigma(p), fixing every other input. Let
$I(j)$ be the XOR of the four depth-j cells for (a,b)=00,10,01,11: the coefficient of ab in
that cell's Boolean polynomial. In particular, zero I at all depths is the exact two-input
superposition test for this fixed background.

Lemma4 gives no dependence on b through depth p, and
$x_{p+1}=b\oplus V(a)$. The column at time1 does not depend on a. Put $U(a)=x_p$. Since
$X\lor U=X\oplus U\oplus XU$ over Boolean arithmetic, the inverse recurrence at the next depth gives

```math
 I(p+2)=U(0)\oplus U(1).
```

The term at time1 has no a coefficient; the only ab coefficient comes from bU(a). This is
an exact criterion, not a prediction that the right side is1. For p≥5 it is0 by G12.1, and
indeed every I(j) is0. Thus the first hole is a poor representative of later hole interactions.
The algebra makes the failed blind prediction below understandable without changing it.

### G12.3. Predictions, runs and failures

The probe is `rule30_gpt_hole_interactions.py`, one Intel CPU process. It evaluates four scalar
fibres with only the first two hole inputs variable, all other sigma bits zero. An independent
packed four-case recurrence checks every output cell. This is not an exact record search.

- HI0, packed/scalar agreement, passed at p2..32 through depth3p+2.
- HI1, second-bit arrival at depth p+1 and no earlier dependence, passed.
- HI2, the identity in G12.2, passed at every period tested.
- HI3, blind interaction by depth2p+2 at every p3..32, **refuted at every p5..32**.
  There was no mixed term through the tested horizons3p+2 for those periods. G12.1 explains
  its absence at every depth for that first input, not merely within the horizon.
- HI4, explicitly unexpected p2 comparison, ran: first mixed depth4 at p2,5 at p3,8 at p4.
  Mixed-cell counts through the respective horizons8,11,14 were4,5,5. The generic
  superposition counterfactual was rejected by these witnesses.

The initial shell invocation printed a date after the probe, masking its return code; a separate
invocation of the identical command captured **exit1**, with ALL CONTROLS PASS and HI3 refuted.
The failed blind prediction is retained. A failed prediction is not a failed control.

The `shield` addendum then checked the newly derived theorem on p5..64, eight seeded arbitrary
sigma columns per period, at holes0 andp, through depth96: **960 comparisons**, seed2026100612.
Every flip changed exactly depths1,2,3 of that hole's own row; depth4 was black in both. The
command exited0 and printed ALL SHIELD CONTROLS PASS. Its p3 counterfactual, all other sigma
bits zero, changed depths[1,2,3,4,5,6,8,9,11,12,13] through20, rejecting universal three-cell
shielding at every period. These checks validate the instrument; the proof establishes the
all-depth shielding claim under the stated four-black-window premise.

**What changed.** The one-hole lead remains PART. A local boundary bit really can be erased
from the deep tail, even when later inputs are arbitrary; that distinguishes the first hole
from later inputs observed at time0. We have not bounded their earlier inverse propagation,
proved LR, or justified a coin law. The next missing object is a bound on that backward
propagation or on surviving zero-run histories, with the starting time specified. C023 gives
Local the correction and the exact scope rather than asking for another records run.

### G12.4. Reply to C024: the period-3 first-bit count also terminates exactly

**Proof follow-up, 2026-10-06 07:26 BST; no new experiment.** Local C024 supplied its injection
times and row times. Its first-hole counts at p6 and p8 are3, agreeing with G12.1; its p3
first-hole count is11 through depth160. The existing `shield` OUTCOME independently listed
exactly11 changed depths through20:

`[1,2,3,4,5,6,8,9,11,12,13]`.

That existing check and the following elementary criterion make the p3 example an all-depth
claim with a specified input prefix, rather than an extrapolation from160 cells.

**Terminal agreement criterion.** Compare two right columns differing only at time q. Their
forced columns at q+1 are identical. If their rows at q agree at two consecutive depths j
and j+1, then they agree at every depth≥j. Indeed, in

```math
 x_{k+1}=y_k\oplus(x_k\lor x_{k-1}),
```

the future-time values y are common. Two consecutive common x values force the next common
value; induction finishes. This criterion concerns the input's own row. At an earlier row,
the y values may differ, so a coincidental pair of agreements there is not a terminal test.

**Exact p3 consequence.** For the wall011 beginning at its hole, fix sigma(3),sigma(6),sigma(9)
and sigma(12) to0. Changing only sigma(0) changes exactly the11 depths listed above and no
others, even if the later hole inputs sigma(15),sigma(18),... are arbitrary and common to
the two columns. The previous exact check gives agreement at depths14 and15 when all later
inputs are0. Lemma4's cone bound says these two cells depend only on sigma through time14;
non-hole values are invisible. Thus the same agreement holds for any continuation after14.
Apply the terminal criterion to prove agreement at every subsequent depth. The listed
shallower cells are also unaffected by the continuation. No new run or prediction is needed
to infer this from the existing independently checked finite prefix.

This is a conditional p3 result, not G12.1's universal four-black-window result. It does not
prove that every background at p3 shields the first bit, or that a later input at q>0 has
finite influence on time0. C025 thanks Local for the labelled counts and records the
criterion; the two-end lead remains PART and the earlier-propagation bound remains open.

## G13. An exact four-state reset certificate for one inverse row (2026-10-06)

**Question and scope.** Continue C024/C025's distinction between the injection row and an earlier
row. Fetched shared work, including Local's Collatz measurements and entropy-pool variant; those
jobs were not repeated. Fresh wall and merge startup commands both printed ALL CHECKS PASS,
with the existing witness scope as G1. Used G12's own-row shielding and §8.2 Lemma4, and checked
§8.19's inverse-row record before constructing the automaton. IR0–IR4 were pushed inf082231
before their run. This is a finite certificate for one backward step, not a prize proof.

### G13.1. Four states and the shortest reset words

Fix a future row $y_j=v_j(t+1)$. Reconstruct an earlier row $x_j=v_j(t)$ leftwards, using

```math
 x_{j+1}=y_j\oplus(x_j\lor x_{j-1}).
```

The state before reading y_j is $(x_{j-1},x_j)$, one of00,01,10,11. The transition is

```math
 T_y(a,b)=(b,y\oplus(a\lor b)).
```

| State | Driver0 | Driver1 |
|---|---|---|
| 00 | 00 | 01 |
| 01 | 11 | 10 |
| 10 | 01 | 00 |
| 11 | 11 | 10 |

A word resets if it sends **all four** starting states to one state. These are synchronizing
words in the usual automata sense; only that definition is borrowed from the abstract of
[Maslennikova2014](https://arxiv.org/abs/1405.3576), not a theorem from that paper.

Both0100 and0101 reset: after01 the image is{01,10}, after010 it is{01,11}, and the fourth
bit sends both states to11 if0, or10 if1. No shorter word resets, as is also visible in the
subset table below; these are the only length4 reset words. Reading010 alone leaves two
states and does not reset. This distinction matters in depth bounds.

### G13.2. Complete reset language, with a failed first characterization retained

I initially proposed that every reset word contains010 followed by another bit. IR5 checked
that claim and failed at0111100. This is a false characterization, not an instrument failure
and not a refutation of the shortest words or the one-step theorem. The failure remains in
the probe and here. The corrected exact statement is:

**Theorem.** A finite driver word resets exactly when it contains a factor

```math
 0\,1^{3k+1}\,0\,z,\qquad k\ge0,\quad z\in\{0,1\}.
```

**Proof by the reachable non-singleton images.** Begin with the full set F. Label
S0={00,01,11}, S1={00,01,10}, C={00,11}, D={01,10}, B={00,10}, A={00,01}, E={01,11}.
Their transitions, calculated from G13.1, are:

| Image set | Driver0 | Driver1 |
|---|---|---|
| F | S0 | S1 |
| S0 | C | D |
| S1 | S0 | S1 |
| C | C | D |
| D | E | B |
| B | A | A |
| A | C | D |
| E | singleton11 | singleton10 |

A singleton remains a singleton under every later driver. The first collapse must therefore
be from E on one further bit. E is reached only from D on0. Before any collapse, the image
after a0 is S0,C,A orE. If it is E, one more bit already collapses. Otherwise, the next1
always gives D, and successive ones cycle D,B,A,D. Leading ones, with no preceding0, leave
S1. Hence the first visit to E follows a0, a run of ones of length1 modulo3, and another0;
the next bit collapses. Conversely, each such factor collapses the full image, whatever
prefix precedes it, since after its first0 the possible non-singleton image is among those
just listed (or E, which collapses still sooner). This proves the exact language. The
shortest factors have k0 and length4, giving G13.1. No probabilistic premise enters.

### G13.3. Conditional propagation bound and one step backward from a hole

Suppose two future rows agree at every depth greater than D. If their common future tail has
010 at depths r,r+1,r+2 with r>D, the next driver is also common. The reset word010z sends
both earlier-row states to the same pair at depths r+3,r+4. Every following driver is common,
so the earlier rows agree at every depth≥r+3. Their last possible difference is at most r+2.
If such a start lies at r≤D+G, this gives the conditional bound

```math
 D_{t-1}\le D_t+G+2.
```

The longer factors in G13.2 also reset, with their corresponding length in the bound. No
uniform bound on G for our forced rows is proved. If the two future rows differ infinitely
far left, there is no common tail to which this argument applies.

**One-step theorem.** If a hole at q≥1 is followed by seven black wall cells, flipping only
sigma(q) changes no cell at depth≥8 of the row at q−1. In particular this holds for every
one-hole wall with p≥8, independently of all other right-column inputs.

**Proof.** At q, G12 shows the two rows differ only at depths1,2,3. The seven-black window
also fixes the common cells at depths5,6,7 to010, by G11's prefix formula. The depth8 cells
are common by G12, even if their value is not fixed. Thus the earlier-row driver at depths
5..8 is010z. G13.1 resets both states to a common pair at depths8 and9; all later drivers
are common, so agreement persists. This improves a one-step damage bound without assuming
that later holes are rays or that their time0 effects are linear.

**Why this does not close the problem.** Repeating the argument would require sufficiently
nearby reset factors in each succeeding common future tail. A gap-free assertion is false
for unrestricted drivers: constant0 keeps states00 and11 distinct forever; constant1 cycles
00,01,10 and preserves three possible states. These are the explicitly unexpected controls.
A finite row's far-left zero tail contains no reset factor, so finiteness itself does not
supply the missing reset-gap hypothesis. Failure to reset all four states also does not
prove that a particular pair stays different. This certificate identifies a useful local
mechanism and its exact domain; it supplies no all-depth one-hole LR or universal linear
propagation bound.

### G13.4. Commands and every outcome

`rule30_gpt_inverse_reset.py`, one Intel CPU process, seed2026100613, standard library:

- Default command: exit0, ALL CONTROLS PASS. IR0 checked all Boolean triples; IR1 enumerated
  every word through length4 and found exactly0100,0101; CF rejected010 as a reset.
- IR2 passed512 independently reconstructed scalar prefix/reset/suffix comparisons, all
  four starting states each. IR3 passed200 hole comparisons, p8..32, eight arbitrary sigma
  columns per period, row q−1 at q=p, through depth96. No depth≥8 differed.
- IR4's constant0 two fixed states and constant1 three-cycle obstruction passed. These
  reject a uniform-reset inference from the presence of black cells alone.
- Argument `language`: IR5 exited1 at0111100; the candidate characterization was false.
  It was published before the run and is retained unchanged.
- After the subset-table repair, IR6 was published in0aa21c9 before its check. Argument
  `language-repaired` exited0 and printed ALL RESET-LANGUAGE CONTROLS PASS for all32767
  words through length14. The proof in G13.2 covers arbitrary lengths; the enumeration
  independently checks its implementation rather than supplying that unbounded conclusion.

**Lead status.** The two Condrey ends remain PART. One-step inverse-row propagation now has a
specific finite reset certificate and a p≥8 theorem. A reset-gap bound over the successive
rows is the named missing step; C026 gives Local the mechanism and the failed-language repair.

### G13.5. Several backward steps, with the protected window's exact cost

**Follow-up block, 2026-10-06 07:44 BST.** The one-step theorem has a bounded iteration.
Predictions MS0–MS2 and CF were pushed inc0c27f0 before the `multistep` check. This extends
G13's proved reset mechanism; no new literature theorem or Local computational job was used.

**Theorem.** Suppose a wall has a hole at q and then p−1 black cells, with no premise on its
values outside that window. Compare two right columns differing only at q. For any integer
r with $0\le r\le q$ and $p\ge3r+5$, their rows at q−r agree at **every** depth≥4r+4. In
addition their common cells in the interval

```math
 [4r+4,\ p-1+r]
```

are the checkerboard: black at even depths and white at odd depths. The interval's length
is p−4−3r; each backward step consumes three cells of this protected window. All other
right-column inputs, and the wall before and after the specified window, are arbitrary
and common to the two constructions.

**Proof.** At r0, G12 gives agreement at every depth≥4, and G11 gives the checkerboard
through p−1. Inductively, at row q−s let

```math
 A=4s+4,\qquad B=p-1+s.
```

The rows agree at all depths≥A and are the checkerboard on[A,B]. To step back once, use
these rows as the common driver y beyond A−1. If $p\ge3(s+1)+5$, then B≥A+3. Since A is
even, the three drivers at A+1,A+2,A+3 are010. The next driver, at A+4, is common even if
outside the known checkerboard interval. The reset010z gives a common state at depths
A+4,A+5. Its first component, x(A+4), is1 for either z. All later drivers are common,
so agreement continues forever from depth A+4.

Where the driver remains checkerboard, the reset gives the correctly phased earlier-row
checkerboard: if y(A+4) is known, it is1, giving x(A+5)=0; thereafter each adjacent pair
contains a1, so $x(j+1)=1-y(j)$ preserves black even depths and white odd depths. This
continues through depth B+1. If B=A+3, the new protected interval is just the black
anchor at A+4, already proved. Thus both inductive claims hold for s+1, finishing the proof.

**What was checked.** Argument `multistep` exited0 and printed ALL MULTISTEP CONTROLS PASS:
p5..64, four seeded arbitrary sigma columns each, q=p, every allowed r, through depth96;
**2520** row comparisons checked both all tested tail agreement and every protected
checkerboard cell. Seed2026100614. **Unexpected check MS2:**48 additional comparisons on
nonperiodic walls with arbitrary values before and after the black window, q1..6,
p=3q+5, eight backgrounds each, through depth64 at time0. Every predicted tail agreement
held. This checks that periodicity is not being smuggled into the local theorem.

The counterfactual dropping p≥3r+5 was rejected: for wall01111111, sigma all0 except the
changed bit at q8, row0 has a change at depth36, beyond the proposed unrestricted cutoff
4r+3=35 at r8. This is Local C024's spreading example with an explicit cutoff witness,
not an infinite-influence or LR counterexample.

**Limit and next intention.** The result covers at most floor((p−5)/3) steps back from an
injection. For a later hole q=p, it therefore does not reach row0. Additional reset factors
outside the guaranteed checkerboard window could extend the certificate, but their gaps
are not bounded here. The lead remains PART. C027 passes Local the exact window cost and
records this limit; the next reasoning target is what replaces the protected window after
it expires, rather than extrapolating the local bound to all earlier times.

## G14. Exact two-state counting at the white Condrey end (2026-10-06)

**Question and prior record.** C022/§8.62 bounds the wall $0^{p-1}1$'s column1 by at most
p+1 shapes per period, giving log2(p+1)/p bits per step. That bound is valid, but discards
cross-period reset constraints and counts bits invisible to the left half. This bounded
proof audit sharpens it. The p2 cases are **already known**: §8.2 has the full-column Pell
count and the visible Fibonacci language; `rule30_entropy.py` uses the latter as its m1
control. The contribution here is the elementary general-p formula, not rediscovery of
Fibonacci or a replacement for Local's wider-layer work.

Read shared history and C022–C027, the two-end board and the startup workflow; both fresh
startup checks printed ALL CHECKS PASS, witness scope as G1. WL0–WL4/CF were pushed
in0436ef5 before the small enumeration. No entropy2, mmap, squeeze or Collatz job was run.

### G14.1. The exact width-one relaxation

Let p≥2 and fix tau to0 at times0..p−2 and1 at time p−1, repeating. For a genuine right
column s=sigma with next-right cell rho, the update is

```math
 s(t+1)=\tau(t)\oplus(s(t)\lor\rho(t)).
```

At a white wall cell this requires s(t+1)≥s(t); at a black wall cell it forbids the
transition1→1. Conversely, each allowed transition has some rho(t). We count exactly this
**width-one relaxation**, choosing rho freely at each time. It need not be a valid further
column of a full Rule30 evolution. Therefore these counts bound real right-column
languages from above, and do not establish their actual entropy.

Use the value s(np) as a state,0 or1. If it is0, white updates permit the first1 at one of
positions1..p−1. Each such rise forces the next-period state0, since the black update must
then fall. If no rise occurs, the black update permits either next state. If the starting
state is1, the whole block is1 and the black update forces next state0. Thus the number
of distinct full-column blocks for each state transition is

```math
 T_p=\begin{pmatrix}p&1\\1&0\end{pmatrix}.
```

For n whole periods, including the next-period endpoint s(np), the exact number of full
words is the sum of all four entries of $T_p^n$. The endpoint convention matters: these
are length np+1 words, not the length2n pair-prefix Pell counts printed in §8.2. Both have
the same p2 exponential growth factor1+sqrt2.

### G14.2. Delete the invisible bit without double counting

The left half sees sigma only when tau=0. Omit s at each black time, retaining the next
period's first visible bit as the endpoint. A start0 block whose visible part contains a1
has its first rise at one of positions1..p−2 and forces next state0: p−2 distinct blocks.
If its visible part is all0, either next state is possible. In the all0/next0 case, the
black-time bit can be0 or1, but both extensions give the **same visible word** and must be
counted once. A start1 block has all visible bits1 and forces next0. The visible matrix is
therefore

```math
 V_p=\begin{pmatrix}p-1&1\\1&0\end{pmatrix}.
```

State transitions and their visible block labels identify distinct visible words: each
period's starting state is itself a visible bit, including the final endpoint. Every path
has an allowed full-column extension by the constructions just given. Hence the number
of visible words of length n(p−1)+1 is exactly the sum of entries of $V_p^n$.

Put m=p−1. These counts obey

```math
 C_0=2,\quad C_1=m+2,\quad C_n=mC_{n-1}+C_{n-2}\quad(n\ge2).
```

This follows directly from $V_p^2=mV_p+I$. Its dominant root is

```math
 \lambda_{\rm vis}(p)=\frac{p-1+\sqrt{(p-1)^2+4}}2.
```

Changing the endpoint convention changes prefix counts by at most a factor2, since an
endpoint has two possible values and each prefix extends. The asymptotic visible-language
entropy bound per time step is consequently

```math
 h_{\rm vis}(p)=\frac{\log_2\lambda_{\rm vis}(p)}p.
```

For full sigma the corresponding root replaces p−1 by p, so
$h_{\rm full}(p)=\log_2((p+\sqrt{p^2+4})/2)/p$. Both sharpen the independent-shape bound
log2(p+1)/p, and h_vis is the relevant one for the forced left half. These are elementary
language growth rates, not claims about a particular finite seed's information production.

### G14.3. Numbers, controls and limits

| p | Full sigma bound, bits/step | Visible bound, bits/step | Independent shapes bound |
|---|---:|---:|---:|
| 2 | 0.635776652 | 0.347120957 | 0.792481250 |
| 3 | 0.574559656 | 0.423851101 | 0.666666667 |
| 8 | 0.377753926 | 0.354491897 | 0.396240625 |
| 64 | 0.093755501 | 0.093400676 | 0.094099497 |

The p2 visible count is F(n+3), the existing no-adjacent-ones result with n+1 visible bits.
Its full-column root is the existing Pell root. The p8 visible rate sharpens C022's coarse
0.40 estimate to0.35449; it remains above the black-condition density1/8. For every p≥3,
lambda_vis>2, so h_vis>1/p. At p2 it is below1/p, but an entropy upper bound is still not
the missing lower information cost for every single trajectory. The deeper period2
channel bound is much stronger already; this audit supplies no new prize implication.

`rule30_gpt_white_latch.py`, one Intel CPU process, enumerated **21** (p,n) cases, p2..8,
n≤5 and np≤15. WL0 verified all Boolean existence-of-rho transitions; WL1/WL2 matched
both matrices to full enumeration and deduplicated visible words; WL3 recovered the
Fibonacci count. The counterfactual equating full and visible counts was rejected: at
p2,n1 there are4 full words but3 distinct visible words, with the same endpoint convention.

**Unexpected WL4:** the constant0 wall permits just N+2 full sigma words of length N+1,
not exponential growth; the constant1 wall has no visible bits. The first run implemented
the constant0 part but did not explicitly enumerate the constant1 projection, so it was
not a complete WL4 check. That omission was recorded in the probe, the explicit empty
projection check was added, and the identical main command reran. Both commands exited0;
the verification rerun printed ALL CONTROLS PASS, covering the complete stated controls.
N1..12 were checked for both constant walls. No blind research prediction failed here;
the first control's coverage limitation is retained rather than called a complete pass.

**Lead and coordination.** The two-end lead remains PART. The latch's exact relaxed visible
count is settled by this proof; the actual right half and the cost side remain open. Incoming
be15203 reports Local's completed width27/28 power-iteration measurements0.1229/0.1222
bits per visible bit, with its integer SQ6 certificate pending and MM3's write clause
undecidable as written. Those are Local's measurements, not this run. C028 congratulates
the mmap handoff, sends this counting refinement and preserves all those qualifications.

## G15. The exact width-one visible language depends on white-time gaps (2026-10-06)

**Question.** G14 counted the white end. What does the same local relaxation say at the black
end, and does white fraction alone determine its capacity? Read the current record and ledgers;
no new reply after C028. Both fresh startup checks printed ALL CHECKS PASS, witness scope as G1.
Checked §8.2's known Fibonacci result, G14's matrices and the two-end board before extending
those same local rules. VG0–VG4 and CF were pushed in56dcd32 before the enumeration. No wider
layer, records, squeeze or entropy-pool computation was duplicated.

### G15.1. Exact gap characterization, without a periodicity premise

Let z0<z1<... be the wall's white times and let e_i=sigma(z_i) be the visible bits. Count the
same width-one relaxation as G14: sigma must satisfy its update for some independently
chosen next-right input rho(t) at each time. This does not require rho to be a further
Rule30 column. Consecutive white times have gap g=z(i+1)−z(i), with all g−1 intervening
wall cells black. Their exact allowed visible pairs are:

| Gap | Allowed visible pairs | Matrix, rows=old bit and columns=new bit |
|---|---|---|
| 1 | 00,01,11 | A=[[1,1],[0,1]] |
| 2 | 00,01,10 | F=[[1,1],[1,0]] |
| at least3 | 00,01,10,11 | J=[[1,1],[1,1]] |

**Proof.** At a white wall cell, sigma cannot decrease; at a black wall cell, it cannot
make the transition1→1. Both local conditions are also sufficient for some rho, by G14.
For gap1, the white update directly forbids10. For gap2, visible1 forces the next sigma
value1 after the white update, and the black update then forces visible0:11 is forbidden.
Starting with visible0 allows either next bit, by choosing the intermediate value0.

For gap≥3, use the white update to retain the starting bit. At the first black update,
choose the next sigma value0, possible from either starting value. Keep sigma0 at the
remaining black updates until the final one, which can output either desired next bit.
There are at least two black updates, so this construction realizes all four visible
pairs. Each interval can be constructed independently once its visible endpoints are
specified; adjacent intervals share just those endpoints. Thus the listed nearest-neighbour
conditions are necessary and sufficient for the whole finite or infinite visible language.
Before the first observed white time, choose sigma0 until the last update, then the required
first bit; both outputs are possible from sigma0 under either wall value. Any last observed
visible bit has an allowed continuation. These boundary choices impose no extra constraint.

For n≥1 observed white times, the exact number of visible words is the sum of the entries
of the product of the n−1 gap matrices. With no white times there is just one empty visible
word. The language equality is stronger than equality of the counts: the proof specifies
exactly which visible words extend through the local relaxation.

### G15.2. Two useful consequences and a same-density counterexample

**Black end.** For a one-hole wall $0\,1^{p-1}$ with p≥3, every visible gap uses J. Therefore
**every binary sequence of hole bits** extends in the width-one relaxation. Its capacity
is exactly1 bit per visible bit, or1/p per time step. The p2 wall uses F and recovers the
already-known Fibonacci envelope. This is no claim that a real finite right half can
produce every such sequence; its further columns may exclude many of them. The one-step
right-neighbour rules alone provide no hole-bit entropy loss at the black end for p≥3.

**White end and clustered zeros.** For wall $0^{p-1}1$, the cyclic product is

```math
 A^{p-2}F=\begin{pmatrix}p-1&1\\1&0\end{pmatrix},
```

exactly G14. More generally, if every white block of length l is separated from the next
by at least two black cells, its l visible bits form a non-decreasing word, with l+1
choices, and J makes different blocks independent. For a periodic wall with block lengths
l1,...,lk and period P, the exact per-period growth factor is the product of (li+1).

**Counterexample to freedom determining this relaxed capacity.** Both primitive period8
walls00111111 and01101111 have white fraction2/8. Their cyclic matrices are respectively

```math
 AJ=\begin{pmatrix}2&2\\1&1\end{pmatrix},\qquad
 JJ=\begin{pmatrix}2&2\\2&2\end{pmatrix}.
```

They have rank1 and nonzero eigenvalues3 and4. Equivalently, the first wall has a single
white block with three monotone visible choices; the second has two independently free
hole bits. Their relaxed rates are log2(3)/8 and2/8 bits per time step. Thus white fraction
alone does not determine even the width-one visible entropy. This refutes an exact
capacity-by-fraction statement, not Local's measured coin scaling or a qualitative ladder
of rigidity. It also does not establish distinct actual right-half entropies, since those
languages are narrower and have not been counted here.

For any periodic wall with at least one white time, use its cyclic gap-matrix product M.
The visible prefix count over n periods with a visible endpoint is the sum of entries of
M^n; removing the endpoint changes counts by at most a factor2. Hence its relaxed rate
is log2 of the spectral radius of M divided by the time period. Constant white wall uses
only A and has polynomial counts, rate0; constant black wall has no visible bits, rate0.
These reproduce the existing endpoint controls rather than claiming new constant-wall
prize results.

### G15.3. What ran, scope and next intention

`rule30_gpt_gap_language.py`, one Intel CPU process, exited0 and printed ALL CONTROLS PASS.
VG0 checked all Boolean existence-of-rho transitions. VG1/VG2 enumerated **all256 wall
traces of length8**, and all256 sigma words for each wall, comparing the **entire projected
language** to the gap constraints, as well as its matrix count. No mismatches. VG3 verified
the white-end matrix product for p2..64 and the black-end J case for p≥3. The same-fraction
counterfactual was rejected by the exact matrices above.

**Unexpected VG4:** the finite, non-uniform gap list3,5,3,4 (white times0,3,8,11,15) admitted
all32 five-bit visible words under direct scalar enumeration. The characterization does
not depend on a periodic extension or equal spacing. No blind empirical hypothesis was
introduced, no prediction failed, and these checks establish neither a full right evolution
nor LR.

**Lead.** The two-end row remains PART. Local latch counts and their arrangement dependence
are now completely characterized at width1; a genuine right half still needs wider-layer
constraints. The next question at the black end is specifically which wider layer first
removes this full visible shift, if any, with the source lane named before any run. C029
sends the negative width-one result and the qualification on freedom; it requests no new
Local computation and leaves the existing integer-certificate job with Local.

## G16. Two right-hand cells filter the one-hole language by parity (2026-10-06)

**Question.** G15 allows every hole-bit sequence for wall0 1^(p-1), p>=3,
when only one right-hand cell is constrained. Does a second cell remove that freedom?
This is the existing layer relaxation, not a finite-support hypothesis. Local's long
entropy jobs remain separate. Startup wall and merge checks both ALL CHECKS PASS,
with the capped-witness qualification of G1. Predictions TC0-TC4/CF were published
in de9a03b before the first run; TC5/TC6 in098dd87 before their run.

### G16.1. Exact language theorem for every period

Let state s=a+2b encode the two right cells, and let u be the unconstrained next
cell. One update is (a',b')=(tau XOR(a OR b), a XOR(b OR u)). Sample a at each
white phase of wall0 1^(p-1); allow any initial state and any u at each time.
Then the complete visible language is:

| Period | Allowed finite hole words | Number of length n words | Growth per time step |
|---|---|---|---|
| Even p>=2 | exactly words avoiding11 | F(n+2) | log2(phi)/p |
| p=3 | exactly words avoiding100 | F(n+3)-1 | log2(phi)/3 |
| Odd p>=5 | every binary word | 2^n | 1/p |

Here F(0)=0, F(1)=1, phi=(1+sqrt(5))/2. The table also describes infinite
one-sided sequences: every legal finite prefix extends, and consistent state paths
exist by finite branching. It makes no claim that the unconstrained input u comes
from a further Rule30 column. Any actual right half must obey these restrictions;
full freedom in the relaxation does not establish full freedom in an actual half.

**Proof from four states.** Denote the white and black update relations W and B.
Listing both choices of u gives:

| s | W(s) | B(s) |
|---|---|---|
| 0 | {0,2} | {1,3} |
| 1 | {1,3} | {0,2} |
| 2 | {3} | {2} |
| 3 | {1} | {0} |

The period relation is first W then p-1 applications of B. Direct set composition
shows B^3=B^5, so multiplying by B gives B^(k+2)=B^k for every k>=3.
This is a relation identity, not a fit to the sampled periods. The period images are:

| s | p=2 | p=3 | even p>=4 | odd p>=5 |
|---|---|---|---|---|
| 0 | {1,2,3} | {0,2} | {1,2,3} | {0,2} |
| 1 | {0,2} | {1,2,3} | {0,2} | {1,2,3} |
| 2 | {0} | {1,3} | {0,2} | {1,2,3} |
| 3 | {0,2} | {1,2,3} | {0,2} | {1,2,3} |

For a visible symbol e, keep only starting states s with s modulo2=e, then
union their period images. Start with A={0,1,2,3}. This subset construction
retains exactly the paths of the original relation: induction on the visible prefix
proves both necessity and sufficiency. Its closed nonempty subsets are small:

- Even p: A --0--> A, A --1--> D={0,2}; D --0--> A,
  D --1--> empty. This also holds at p2 despite its different state2 image.
  Thus11 is precisely the forbidden pattern. The usual two-state Fibonacci count
  is F(n+2), crediting the already known p2 language in §8.2.
- p3: A --0--> A, A --1--> H={1,2,3}; H --1--> H,
  H --0--> K={1,3}; K --1--> H, K --0--> empty.
  These transitions forbid exactly100. Before the first1 any zeros are allowed;
  after it, zeros must be isolated. Summing over the first1's position gives
  1+sum(F(j+2), j=0..n-1)=F(n+3)-1. The recurrent H,K graph has growth phi;
  the initial all-zero loop adds no larger exponential rate.
- Odd p>=5: A --0--> A, A --1--> H, and both symbols take H to H.
  Every word is possible; no empty transition can occur.

Each macro edge has at least one hidden state/input path, so every infinite legal
visible word has arbitrarily long hidden paths. Finite branching supplies a single
infinite path. This is the infinite-language certificate, beyond finite counts.

### G16.2. What ran and what failed

`rule30_gpt_two_cell.py`, one Intel CPU process, ran in under one second per run.
TC0 independently checked all24 cell transitions against Rule30's eight-entry
truth table. TC1 compared entire visible languages from independent time-step
state-path enumeration and the subset construction: all60 cases, widths1/2,
p2..6, n1..6. TC2 recovered G15's width-one control, including rejected11 atp2.

**Blind TC3 refuted.** The initial full-shift prediction fails: p3 first misses100;
even p4..16 first miss11. Odd p5..15 have the full-shift certificate. This failure
is retained in the header. **Unexpected TC4:** all133 rotated walls/sample phases
had identical certificates. CF rejected the known-wrong all-word claim at width1,p2.
The first run exited0 because every instrument control passed, despite the blind
prediction failing.

An exploratory table of black-relation powers, labelled without new predictions,
suggested the parity identity. After publishing TC5/TC6, the second run checked
B^3=B^5, every127 macro table for p2..128, all104 exact counts through12 bits for
p2..9, and all72 complete languages through8 bits. All passed, exit0. The all-p
claim rests on relation composition and the subset proof, not those finite tests.

### G16.3. Reply to Local's finite-state question in C030

Two agreeing adjacent depths imply terminal agreement when the entire future row
is common. The inverse-pair machine is finite-state **with the future row supplied
as its input**. An arbitrary input is not thereby generated by a finite autonomous
machine. If all hole inputs except the first are fixed, there are only two complete
spatial rows; each can still have an aperiodic common tail. A singleton infinite
word has a regular prefix language only when it is eventually periodic: along its
unique accepted continuation a finite automaton eventually revisits a state, and
its continuation then repeats. A finite set of infinite words has the same issue
after their last divergence. Terminal agreement alone does not prove regularity
of the resulting spatial-prefix language. This is the missing premise in the proposed
transfer-matrix use; it is not a criticism of the exact finite-state transducer.

There is a simpler temporal statement for column-1. Write its bit as pi(t), the
wall as tau(t), and its right neighbour as sigma(t). Inverting the wall update gives
pi(t)=tau(t+1) XOR(tau(t) OR sigma(t)). At black times pi is fixed by the wall;
at white times it is sigma(t) XOR tau(t+1). Therefore, for a fixed wall, the
visible sigma word and the entire temporal column-1 word determine each other,
apart from the fixed sampling/time convention. Their entropy per time step is
identical. G16's table is consequently an upper bound for column-1 in this
width-two relaxation too. This is temporal entropy, not spatial row complexity,
and not a count restricted to finite initial support. It leaves the prize gap open.

**Status.** The Condrey-end lead stays PART. A second right cell already filters the
black-end holes at even p and atp3; odd p>=5 needs a wider layer. No long Local job
requested. The exact bounds remain positive, and no all-depth LR proof follows.


## G17. A third right cell changes hidden periods but not the hole language (2026-10-06)

**Question.** G16 leaves every odd-period p>=5 hole sequence unrestricted at width
two. Does width three first remove that freedom? The existing eight-state layer is
used, with an arbitrary external input at every time. This is not a finite-support
or whole-right-half assertion. Fresh wall/merge startup checks ALL CHECKS PASS;
the capped-witness scope remains as G1. Local's long entropy jobs were not repeated.
Predictions TH0-TH4/CF were published in47139cf; TH5/TH6 in7cf7a03 before their run.

### G17.1. Exact all-period theorem and certificate

**Theorem.** For every p>=2, width-three and width-two relaxations of wall0 1^(p-1)
have exactly the same finite and infinite one-sided hole languages. Thus even p
avoids11; p3 avoids100; odd p>=5 is unrestricted. G16's counts and entropy rates
remain exact for this relaxation. The third cell neither lowers these rates nor
removes any visible word, even though it constrains the hidden dynamics.

**Proof by finite relation certificate.** Encode three cells as s=a+2b+4c.
For external input u, an update is
(a',b',c')=(tau XOR(a OR b), a XOR(b OR c), b XOR(c OR u)).
Let W and B be the white and black relations, allowing both values of u.
Composing B five times gives these image masks: an integer mask m represents the
set of states j for which bit j of m is1.

| Starting s | B^5 image mask | B^9 image mask |
|---|---|---|
| 0 | 102 | 102 |
| 1 | 68 | 68 |
| 2 | 68 | 68 |
| 3 | 85 | 85 |
| 4 | 196 | 196 |
| 5 | 84 | 84 |
| 6 | 68 | 68 |
| 7 | 69 | 69 |

These eight images follow by applying the displayed update to each current image
for u=0,1; the probe retains the complete set-composition verifier. Equality of
all images proves B^5=B^9. Associativity then proves B^(k+4)=B^k for every k>=5.
Hence the white-to-white macro relation (first W, then B^(p-1)) needs only p2..9:
p2..5 are the short exceptions; p6..9 represent every later residue modulo4.
This finite identity is what extends the result to unbounded periods.

For a visible symbol e, filter the current subset to states with s modulo2=e,
then union their macro images. Name the subsets:
I={0,1,2,3,4,5,6,7}; E={0,1,2,4,5,6,7}; E2={0,1,2,4,5,7};
D={0,2,4,6}; H={1,2,5,6,7}; K={1,5,7}.
Starting from I, direct composition for the eight representative periods gives:

| Period | Subset | symbol0 | symbol1 |
|---|---|---|---|
| even p | I | E | D |
| even p | E | E | D |
| even p | D | E | empty |
| p3 | I | E | H |
| p3 | E | E | H |
| p3 | H | K | H |
| p3 | K | empty | H |
| odd p>=5 | I | E | H |
| odd p>=5 | E | E | H |
| odd p>=5 | H | H | H |

For p2 replace E throughout by E2. These are *all* reachable nonempty subsets;
every output in the table is another listed subset or empty. The table therefore
characterizes every finite word, rather than just tested lengths. Empty transitions
exclude exactly11 for even p and100 for p3; odd p>=5 has none. The same finite-
branching argument as G16 supplies a hidden infinite path for every allowed infinite
word. The graphs have exactly G16's languages, which proves the theorem.

**Hidden period is not visible language.** B^5 differs from B^7. For example,
B^5(0)={1,2,5,6}, whereas B^7(0) is different. Thus the two-step black relation
identity used at width two does not transfer unchanged. The visible language still
agrees because projecting and taking unions produces the same accepting graphs.
The exact value of B^7(0) is reconstructed by the verifier; only inequality is
used. This is a concrete example of hidden dynamics changing without changing
an observed channel language.

### G17.2. Predictions, controls and scope

`rule30_gpt_three_cell.py`, one Intel CPU process, completed both runs in under a
second each. TH0's header said48 transitions: an arithmetic typo, retained and
corrected in its OUTCOME. All32 cases (8 states times2 wall bits times2 inputs)
were actually checked against the independent eight-entry Rule30 truth table.
This is not a claim to have executed48 cases.

TH1 compared complete direct-time-step and subset languages for p3,5,7 through
six visible bits, all18 cases. Blind TH2 held: each odd p5..15 has a closed subset
graph accepting every word. Blind TH3 held: a four-step relation repeat begins
at exponent5. **Unexpected TH4:** all2048 nonperiodic short wall/right-input
traces passed the inverse-wall visible-bijection check from G16.3. CF rejected the
known-wrong width-two,p4 word11. First run exit0, ALL CONTROLS PASS.

After publishing the addendum, TH5 verified the exact masks above, B^5=B^9, and
B^5!=B^7. TH6 checked the explicitly stated subset graphs for every p2..128 and
full width-two/three language equality in all88 cases p2..9,n0..10. Second run
exit0. These are independent finite controls and an exact finite certificate;
the all-p conclusion comes from the relation identity, not extrapolation from128.

**What changed.** The lead remains PART. Width three provides no new hole-channel
restriction. For odd p>=5 the first restrictive width is at least four. A wider
finite relaxation may still have full freedom; this does not prove freedom of a
whole right half, finite initial support, or the forced spatial row. A first small
width-four certificate at p5 is the next bounded question, rather than requesting
another long entropy run from Local.


## G18. Slow-wall switches: a finite prefix, a protected band, and the missing tail state (2026-10-06)

**Asked by Local in C032.** What can the G11-G13 mechanisms certify at the two
switches of wall0^a1^b? This answers the finite question without presuming the
owner's decision about workflow reframing. Fresh wall/merge startup checks both
ALL CHECKS PASS, with the capped-witness scope in G1. SP0-SP3/CF were published
before running in c89589f; SP4 in fe3bca5. No Local record job was repeated.

### G18.1. First fix the phase

Write tau for column0, sigma for column1, and pi for column-1. The inverse wall
identity is pi(t)=tau(t+1) XOR(tau(t) OR sigma(t)). For a period p=a+b starting
at its first white cell:

- at white times0..a-2, pi(t)=sigma(t);
- at the last white time a-1, pi(t)=1-sigma(t);
- at black times a..p-2, pi(t)=0;
- at the last black time p-1, pi(t)=1.

The last white bit is complemented, and the last black time already has a black
left neighbour. A black run of length b beginning at time a guarantees the row
**at time a** is checkerboard on depths1..b-1. At a+r it only gives the direct
future-window guarantee through depth b-r-1. Thus “a checkerboard of depth b-1
just before the black-to-white switch” is not the guarantee of Lemma1. The switch
has to be timed from the future window, rather than treating a whole prefix as
unchanged until the black run ends. CF checks tau111100 at time3: pi(3)=1,
where the unchanged checkerboard would have0.

### G18.2. Exact finite-prefix map from a latch position

**Theorem.** For wall0^a1^b, a,b>=1, the first p-1 left cells on row0 are
determined by the a visible sigma bits at the white times. If these bits are
monotone (the necessary width-one rule), exactly a+1 distinct prefixes occur.
This is a finite-prefix assertion, not an autonomous state for the infinite row.

**Construction and proof.** Begin at time a with the known checkerboard word
of length b-1. To step backwards to time t=a-1,..,0, set x0=0 and
x1=sigma(t) XOR tau(t+1), then successively set
x(k+1)=y(k) XOR(x(k) OR x(k-1)), where y is the known next-time row.
A future prefix of length N determines the preceding prefix of length N+1.
After a steps this constructs exactly b-1+a=p-1 cells. It uses no sigma at a
black time and no later white block. The probe implements this row construction
independently of the column-by-column inverse used by earlier controls.

Monotone visible words have the form0^r1^(a-r), r=0..a. Each is allowed as a
single width-one block (G14/G15; neighbouring blocks are coupled when b=1).
The constructed prefixes are distinct: from any row0 prefix of length at least a,
forward Rule30 on the left half with the fixed wall determines pi(t) for t0..a-1.
The inverse wall identity recovers each visible sigma(t) from pi(t). Thus equal
prefixes would imply equal r. This proves both the a+1 upper count and injectivity,
without assuming an actual whole right half realizes every block.

### G18.3. Uniform protected-band theorem, even without a white prefix

**Theorem.** Suppose a black wall run occupies times a..a+b-1, preceded by any a
wall bits and followed by anything. If a>=1 and b>=3a+1, row0 is checkerboard
on depths4a..a+b-1: even depths are1 and odd depths0. The right column before,
during and after the run is arbitrary. In particular this holds for slow walls,
without needing the monotone latch hypothesis.

**Proof.** At time a the checkerboard is known on depths1..b-1. One backwards
step reads its driver010 at depths1,2,3. For any preceding inverse-pair state,
these three drivers force x4=1; since x4=1 masks x3 in the next OR, every later
known driver determines the next cell independently of x3. Thus the earlier row
has the checkerboard on depths4..b. This needs b>=4.

Inductively after s>=1 steps backwards the known band is
[4s,b-1+s], with the same even-black phase. For one more step use the driver010
at4s+1..4s+3. It forces x(4s+4)=1 independently of all earlier inverse state;
subsequent alternating drivers propagate the phase through depth b+s.
The reset fits when b-1+s>=4s+3, equivalently b>=3(s+1)+1.
For all s<a this follows from b>=3a+1. The final band is [4a,a+b-1].
The inverse update within the row does not depend on the earlier wall bit once
its starting pair is given; the reset handles every pair. That proves the
nonperiodic-prefix version too. The band loses three cells of length per backwards
step, the same protected-window accounting as G13.5.

**Finite-support consequence.** At a slow wall's first white phase, b>=3a+1
forces a black cell at depth2*floor((a+b-1)/2). Hence a finite seed realizing
that trace cannot have a smaller left support radius. This extends G11's a=1
bound. It remains a finite-support exclusion for a specified window; it does not
exclude arbitrary radii or every repeated slow wall.

### G18.4. The prefix does not close the entire per-period state

Take b>=2 and two width-one continuations. Both have their first white block all0.
The first continuation has all later white blocks0. The other has its second white
block all1, then later ones0. Set the first black bit after that all1 block to1,
and the remaining black bits to0. Every sigma update has at least one admissible
further input; G15's independent-block result also supplies these continuations.

The first different visible input is at time p. By the triangular inverse
recurrence, a change in sigma(p) with tau(p)=0 first changes the time0 left row
at depth p+1: at depth1 it first appears at time p, and every further inverse
column moves that first difference one time step earlier through the XOR of the
next-time cell; earlier OR inputs are identical there. No newer input reaches
that leading depth. The rows therefore share the finite prefix above but have
different tails. This proves that a first latch position does not determine the
complete spatial row. A per-period map may have one integer *input*, while still
having an infinite or presently uncontrolled *state*. Its state closure is an
additional theorem, not a consequence of certifying the two finite switches.

### G18.5. What ran, including a finite blind result

`rule30_gpt_slow_switch.py`, one Intel CPU process, both runs under one second.
SP0 passed2112 whole-prefix comparisons at a1..8,b1..24, two arbitrary continuations
per latch position; all192 blocks had exactly a+1 distinct prefixes. SP1 passed
1696 protected-band checks, eight arbitrary white inputs per pair with b>=3a+1
and b<=40. **Unexpected SP3:** all64 nonperiodic preceding-wall cases passed at
b=3a+5, so the band did not rely on a hidden periodicity assumption. CF rejected
the last-black checkerboard. First run exit0, ALL CONTROLS PASS.

**Blind SP2 held finitely:** for balanced a=b4..16, all143 monotone words had a
black cell at depth>=a within their2a-1-cell known prefix. No all-a theorem is
claimed; these balanced walls do not satisfy the protected-band condition above.
After preregistration, SP4 verified88 valid width-one continuation pairs at
a1..8,b2..12: same first latch position, first row difference exactly p+1.
Second run exit0; complete-row counterfactual rejected.

**Status.** Condrey/switch mechanism stays PART, and the reframing remains DECISION
OWED. Local's two questions have an exact finite-prefix answer and a phase correction,
but no complete autonomous finite state or bounded-debt theorem. The next useful
reasoning item is whether the latch restriction improves the three-cells-per-step
loss on balanced slow walls; SP2's finite support observation is a control, not
a proposed global law. The small odd-period width-four audit remains available.


## G19. A concrete latch obstruction on balanced slow walls (2026-10-06)

**Question.** G18's protected band needs b>=3a+1 and misses balanced slow walls.
Does restricting the white input to a monotone latch make any exact difference
in their known finite prefixes? This is a prefix-support audit, not a record run,
a cost asymptotic, or an assumption of an autonomous finite tail state. Startup
wall/merge checks both ALL CHECKS PASS, with G1's capped-witness scope. BL0-BL3/CF
were published in f17e93e before the run; BL4 in63606e8 before its independent check.

### G19.1. Exact certificate for the five-by-five wall

**Finite-window theorem.** Any real Rule30 configuration whose column0 begins
with0000011111 must have a black cell on its initial left half at depth>=7.
In particular a seed with left support radius<=6 is excluded by this window.
The claim uses only this finite trace, not periodicity or an infinite continuation.

**Proof.** At the first five white times, visible sigma must be monotone by the
white-wall update sigma'=sigma OR right2. Its six choices are0^r1^(5-r), r0..5.
G18's exact inverse construction gives these complete nine-cell initial prefixes:

| r | Visible sigma | Left prefix, depths1..9 | Last black depth in prefix |
|---|---|---|---|
| 0 | 11111 | 101000011 | 9 |
| 1 | 01111 | 011000011 | 9 |
| 2 | 00111 | 001000011 | 9 |
| 3 | 00011 | 000100100 | 7 |
| 4 | 00001 | 000000110 | 8 |
| 5 | 00000 | 000011010 | 8 |

Each prefix follows by starting with the depth-four checkerboard at time5 and
performing five inverse-row steps. The displayed finite certificate lists every
allowed latch input, and every prefix contains a black cell at depth at least7.
This proves the exclusion. Both independent inverse constructions and a separate
forward finite-left evolution checked it; no random or asymptotic assertion enters.

**The latch matters in this certificate.** With an arbitrary, unlatched visible
word11001, the same forced-left construction gives100100000, whose last black
cell is at depth4. Exhausting all32 arbitrary visible words shows this is their
minimum, and it is the unique minimizing word. It is forbidden by the latch:
sigma drops from1 to0 between white times1 and2. Thus a left-only freely driven
prefix can pass this support test while every physical right input is excluded
at that support. This is a mechanism-specific distinction between the relaxed
left problem and the extra necessary constraint supplied by the right side.
It does not construct a finite complete left half with an infinite periodic wall.

**Unexpected endpoint failure.** The unique minimizing latch position is r3,
which is interior. Testing only the all-zero and all-one white blocks would give
last black depth8 or9 and miss the true minimum7. The initial endpoint prediction
BL3 is refuted and retained. A proposed worst-case reduction to those two extremes
therefore fails even in this small exact example.

### G19.2. Independent forward check and its practical limit

The first nine pi=column-1 values of a finite left seed are obtained by evolving
that half under the prescribed wall. Negative cells use ordinary Rule30; the
right neighbour of cell-1 is tau(t). Recover the white sigma word as
pi(0),pi(1),pi(2),pi(3),1-pi(4), and require monotonicity. At black times5..8,
pi must be0 because the next wall bit is black. These are necessary conditions
for the ten-bit centre window. Every one of the64 seeds supported on depths1..6
fails them. This independent enumeration is a control of the theorem above.

The finite left seed with black cells at depths4 and7 has
pi(0..8)=000100000, giving visible sigma00011 (r3), and passes these conditions.
It also has exactly the r3 prefix in the table. This is a **left-only positive
control** for the finite necessary conditions. It is not an assertion of a
complete compatible real right half, an infinite slow wall, or any prize candidate.
The positive control verifies that the test is not rejecting every seed by design.

### G19.3. What the broader finite audit says, and does not say

`rule30_gpt_balanced_latch.py`, one Intel CPU process, completed both runs in
seconds. BL0 compared all2044 entire prefixes of arbitrary white words at
balanced a2..10 between row-wise and column-wise inverse constructions. All pass.
BL1 held for all8375 monotone words at balanced a4..128: every known2a-1-cell
prefix contains a black cell at depth>=a. This is **finite evidence only**;
no all-a lower-bound proof was obtained here.

BL2 held: arbitrary/monotone minimum last-black depths were5/6 at a4,4/7 at a5,
7/10 at a7,9/14 at a8,9/15 at a9, and11/17 at a10. At a6 both minima were8;
the latch restriction need not improve this particular support statistic at every
length. These are exact finite minima for the indicated prefixes, not LR records
or a claim about their asymptotic law. Unexpected BL3 failed first at a5,r3;
other failures are retained in the printed audit. CF rejected the same-first-latch
complete-row claim via a valid next-block change, first difference at depth9.
BL4's forward control rejected all64 width-six seeds and accepted the support-seven
left-only control. Both runs exit0 because the instrument controls passed; BL3's
blind prediction nevertheless failed and was not erased.

**Status.** The Condrey-end mechanism remains PART. There is an exact finite latch
obstruction on a balanced wall, but neither the finite support observations nor
channel cardinalities prove a bounded-debt cost. The all-a balanced support bound
is open, and endpoint monotonicity cannot supply it. Next useful reasoning is to
identify which interior latch positions control the last-black depth, or return
to the small width-four channel question; no large Local run is requested.


## G20. Odd one-hole walls remain fully free through four right cells (2026-10-06)

**Question from CONSTELLATION row16.** Is width four the first layer to restrict
the p5 hole language? G15-G17 had shown full freedom through width three for
odd p>=5. This audit uses the existing right-layer update, with the next outside
cell arbitrary at each time. It does not repeat Local's large automata or assume
that the outside cell comes from another valid column. Fresh wall/merge checks
both ALL CHECKS PASS, with G1's capped-witness scope. FC0-FC4/CF were published
in e670d7d; FC5/FC6 in110ae08 before their respective runs.

### G20.1. Exact theorem, including the failed first prediction

**Theorem.** For every odd p>=5, the width-four relaxation of wall0 1^(p-1)
allows every finite and infinite one-sided sequence of visible hole bits. It has
exactly2^n words of length n and rate1/p bit per time step. Combining G15-G17,
a layer that first restricts these walls, if one exists, has width at least five.
This is not an existence proof for an entire infinite right half or a finite seed.

**Blind FC2 was refuted.** The prediction that p5 would first lose freedom at
width four was wrong. Its complete accepting subset graph has no empty edge;
that supplies the theorem at p5, not merely a failure to find a short forbidden word.

### G20.2. Exact all-period certificate

For four state bits x1..x4 encoded by s=sum(xj*2^(j-1)), a step has
xj'=leftj XOR(xj OR rightj), with left1=tau and right4=u.
Allow both u choices. Let W and B be the resulting white and black relations.
Set composition gives B^8=B^16; here are all sixteen image masks for either
power (mask m encodes the states j with bit j of m equal to1):

| Initial s | B^8 and B^16 image mask |
|---|---|
| 0 | 17476 |
| 1 | 17472 |
| 2 | 1028 |
| 3 | 26182 |
| 4 | 17492 |
| 5 | 26182 |
| 6 | 17472 |
| 7 | 50372 |
| 8 | 17733 |
| 9 | 1028 |
| 10 | 1024 |
| 11 | 50372 |
| 12 | 17492 |
| 13 | 26182 |
| 14 | 17472 |
| 15 | 17476 |

The verifier starts from singleton images and applies the displayed Rule30
formula for both u choices, checking these exact integers. Equality of all images
is an equality of relations, so associativity proves B^(k+8)=B^k for every k>=8.
The period macro is first W, then B^(p-1). Thus odd p5 and7 are short exceptions;
p9,11,13,15 represent every odd residue thereafter. No extrapolation from the
largest tested period is needed.

For a visible symbol e, keep starting states with s modulo2=e and union their
macro images. Start with I={0,..,15}, mask65535. For each of the six representative
odd periods, the reachable subsets are exactly I, E and H, with masks
E=59351 and H=59078. In full:
E={0,1,2,4,6,7,8,9,10,13,14,15};
H={1,2,6,7,9,10,13,14,15}.
The same accepting graph holds for all of them:

| Subset | visible0 | visible1 |
|---|---|---|
| I | E | H |
| E | E | H |
| H | H | H |

Each nonempty edge is precisely the union of valid state/input paths through
one period. Induction on the visible word proves exact language equivalence
between these subsets and the original layer; the table never reaches empty.
Consequently every finite word has a hidden layer path. For a specified infinite
visible word, the arbitrarily long finite paths form a finitely branching tree;
an infinite branch gives a consistent infinite state/input history. This proves
the infinite-language statement. It leaves the outside input unconstrained, as
the theorem's relaxation requires.

The p3 graph was separately checked: an initial all-zero-visible loop enters
states with transitions exactly as in G17's forbidden100 graph. Its visible
language remains words avoiding100. No new even-period classification is claimed
in this block; CF at width two,p4 is an instrument control only.

### G20.3. What ran and what remains open

`rule30_gpt_four_cell.py`, one Intel CPU process, first run under one second;
second and final reruns under one second each. FC0 compared all64 local updates
against the independent eight-entry truth table. FC1 compared complete direct
state-path and subset languages for p3,5,7 through six visible bits, all18 cases.
FC2 refuted as above. **Unexpected FC3 held:** p9 also has a closed full-shift
certificate. FC4 held: the first exponent at which the period-eight relation
repeat appeared was8. CF rejected the known-wrong width-two,p4 word11.
First run exit0, ALL CONTROLS PASS despite the blind FC2 failure.

After preregistration, FC5 checked the exact B^8=B^16 masks, all63 odd-period
closed graphs p5..129, the six representative certificates above, and the p3
forbidden100 graph plus an eight-bit comparison to width two. FC6 checked all13
counts2^n at p5,n0..12. Second run exit0; the final rerun also includes the
explicit p3 graph assertion. These finite controls verify the implementation;
the all-p and all-word-length theorem uses the relation identity and closure.

**Status.** The hole-channel lead is PART. The first restrictive layer for odd
p>=5, if any, is beyond four. The hidden periods have changed at widths two,
three and four, while the observed odd-period language stayed the same. This is
an exact projection phenomenon, not a claim of positive actual-channel entropy.
A useful next question is whether the closed subsets have a construction uniform
in width, or precisely where they fail. More sample widths alone would not settle
the complete-right-half question, and no new large job is requested from Local.


## G21. Background control for the incoming other-rule band probe (2026-10-06)

**Proof audit, no experiment.** The incoming `rule30_otherrules.py` selects all
128 rules with f(001)=1, while its shifts supply zero exterior diagonals.
For a single-cell configuration this matches the physical exterior only when
f(000)=0. Rule3 is a counterexample: f(l,c,r)=1 exactly when l=c=0.
At time1, cells-3,-2,-1 are all1; at time2 cell-2 is0, since f(111)=0.
The probe’s lowest diagonal instead stays1: its padded parents stay0 and
f(001)=1. Thus it disagrees already on diagonal0,time2 for this selected rule.
Rule2/30 controls are quiescent and cannot detect that background error.
C040 asks Local to restrict the census to the64 quiescent selected rules or
model the evolving exterior explicitly. Their probe is preserved and not rerun.
This is an exact two-step counterexample, not a claim about their pending outcomes.


## G22. The sideways map has a ternary image and a non-surjective ternary dynamics (2026-10-06)

**Question from CONSTELLATION row5.** Formalize the inverse-column rule as a CA
on the time axis. On two bi-infinite binary tracks, write S a(t)=a(t+1) and
F(a,b)=(c,a), c=S a XOR(a OR b). Here a is the nearest existing column and b
its right neighbour. This is a two-track, four-symbol CA with neighbourhood
{0,1}. It commutes with time shift. It differs from G7’s anti-diagonal predecessor
H(a,b)=(S b XOR(a OR b),a); the coordinates must not be interchanged silently.
No fixed wall or finite-seed restriction is imposed in this formal system.
Startup wall/merge checks ALL CHECKS PASS; G1's scope applies. SI0-SI4/CF1/CF2
were published in f1dcc98 before the run; no Local job was repeated.

**Exact image and fibres.** A pair(c,a) lies in the image iff
c(t) XOR a(t+1)>=a(t) at every t. Where a(t)=0, the predecessor bit is
b(t)=c(t) XOR a(t+1); where a(t)=1, compatibility forces c(t)=1-a(t+1)
and b(t) is free. This proves necessity, sufficiency and the entire preimage
fibre. On P-periodic tracks it has size2^popcount(a). On infinite tracks its
free coordinates are exactly the positions where a is1. In particular F is not
injective, even on constant tracks.

**Ternary recoding theorem.** Encode an image pair by z(t)=2 if a(t)=1,
and otherwise z(t)=c(t). Conversely set A(t)=[z(t)=2] and
C(t)=z(t) if z(t)!=2, otherwise C(t)=1-A(t+1).
Then(c,a)=(C,A). These two rules are inverse, commute with shift and use
finite neighbourhoods. Thus the one-step image, with its time-shift action,
is conjugate to the full three-symbol shift. Every ternary sequence is allowed;
this is an exact representation, not a symbolic fit to a picture.

There are exactly3^P image configurations fixed by the P-step shift. For ordinary
length-n blocks there are4*3^(n-1) choices: choose the first n-1 second-track bits,
with two choices of c at a0 and one at a1; at the final site both a values allow
two c choices because the following a is outside the block. Consequently the
image language’s exponential rate is log2(3) bits per time-axis site, compared
with2 for the full two-binary-track space. This is word-count entropy of the
image under shift, **not** dynamical entropy of iterating F, nor the fixed-wall
channel entropy studied in G20.

**The induced dynamics.** Conjugate F restricted to its image by this recoding.
On arbitrary ternary z, compute A,C as above. Its new symbol is2 if C(t)=1;
otherwise it is C(t+1) XOR A(t). This uses z(t),z(t+1),z(t+2), so it is a
three-symbol CA with neighbourhood{0,1,2}. The probe also implements its explicit
case rule independently and checks the conjugacy.

The induced CA is not onto. For the bi-infinite periodic target(c,a)=(10,00),
the only F predecessor is(a,b)=(00,10). That predecessor is outside the image:
at its first site, c=0 and a=1 while a(next)=0 violate compatibility.
Uniqueness holds without requiring a periodic predecessor. Therefore this target,
whose ternary code is10 repeated, has no predecessor under the induced rule.
The ternary description does not make the iterated image a full invariant
surjective dynamics. Further image layers and dynamical entropy remain open.

**Unexpected measure check.** Uniformly counting P-periodic image configurations
makes the second-track1 density1/3: it is the uniform ternary symbol2 density.
Uniformly counting the4^P binary input pairs and pushing them through F keeps
that density1/2, since the second output track is the first input track. An image
with k second-track ones has2^k predecessors, so its ternary code has probability
2^k/4^P; the pushed measure is a product with probabilities1/4,1/4,1/2 for
symbols0,1,2. Its Shannon entropy is1.5 bits per site. Equal weighting of images
and equal weighting of inputs are different exact ensembles. This makes no
claim about the frequencies of a single physical Rule30 trajectory.

**Checks.** `rule30_gpt_sideways.py`, one Intel CPU process, both runs under one
second: all87380 input pairs at P1..8 passed SI0-SI3’s complete image, exact
fibre, recoding, shift and density checks. All1092 ternary words at P1..6 passed
SI4’s independent induced-rule comparison. Both counterfactuals were rejected:
injectivity and surjectivity onto the image. The final rerun adds all8 explicit
Rule30 inverse truth-table cases; the first SI0 used a scalar versus bit-vector
port, and that narrower initial scope is recorded. Both exit0, ALL CONTROLS PASS.
The all-size theorems use the displayed coordinate formulae, not extrapolation.

**Status.** The sideways formalization moves to PART: exact CA, image recoding,
fibres and induced rule established. Its iterated images, invariant measures and
dynamical entropy are not classified. The ternary shift representation is a
structural result about this formal map; no novelty or prize solution is claimed.


## G23. Channel subset shapes at width10: preregistration (2026-10-06)

Following Local C043, audit the existing entropy2.c subset construction, not a new wide-layer computation. Both startup probes passed, including their stated bounded scopes. Predict SH1: at least one of twelve reproducibly sampled noninitial reachable states is not an exact fixed-bit cylinder. Predict SH2: at least one is not an affine subspace of binary width10. Counterfactual: every sampled set is a cylinder, making fixed bits a sufficient exact representation for this sample. Neither outcome establishes a closed-form growth bound.

Use seed2306, sample twelve distinct states without weighting by size or stationary probability, and examine one state reached by a depth13 record witness from the existing records.c construction. Compare every state and transition to a separately coded scalar Rule30 subset BFS. Controls: whole cube, singleton, fixed-bit cylinder, even parity, and a same-size random set. Measure cardinality, fixed-bit cylinder hull, affine hull, sorted integer runs and largest nonconstant Walsh coefficient. Unexpected check: reverse all bit positions; cylinder/affine properties must be invariant, while integer runs may change. Retain any rejected record prefix honestly. Pictures are membership grids, not evidence of randomness. No novelty claim: this audits the project's existing channel automaton.

### G23 outcome: exact cylinders fail, and low-bit correlations remain

At width10 there are155 reachable subset states including the initial full cube, with225 live labeled edges. The separately coded scalar truth-table BFS agrees with the untouched entropy2.c on every exact subset and transition. All controls pass. SH1 and SH2 hold; the all-cylinders counterfactual fails. Exhaustively, none of154 noninitial states is a cylinder, and just one is affine: q119 is the translate of the span of80,256,512 by58 (XOR throughout), with eight members. This exhausts this finite automaton, not other widths.

The reproducible sample, in draw order, follows. Hull sizes are cardinalities; runs refer to consecutive encoded integers, not physical runs. The final row is only a prefix of a left-record witness, not a complete record-reaching channel path.

| State | Size | Fixed bits | Cylinder hull | Affine hull | Integer runs / reversed | Observation |
|---|---:|---:|---:|---:|---:|---|
| q124 | 12 | 5 | 32 | 32 | 12 / 5 | Nonlinear subset inside a proper fixed-bit hull. |
| q27 | 108 | 2 | 256 | 256 | 108 / 35 | Nonlinear subset inside a proper fixed-bit hull. |
| q18 | 113 | 0 | 1024 | 1024 | 113 / 41 | No fixed bits; sparse correlated subset of the full cube. |
| q75 | 49 | 0 | 1024 | 1024 | 49 / 21 | No fixed bits; sparse correlated subset of the full cube. |
| q67 | 101 | 0 | 1024 | 1024 | 80 / 36 | No fixed bits; sparse correlated subset of the full cube. |
| q17 | 81 | 1 | 512 | 512 | 81 / 28 | Nonlinear subset inside a proper fixed-bit hull. |
| q111 | 52 | 2 | 256 | 256 | 52 / 21 | Nonlinear subset inside a proper fixed-bit hull. |
| q25 | 67 | 1 | 512 | 512 | 67 / 24 | Nonlinear subset inside a proper fixed-bit hull. |
| q118 | 22 | 3 | 128 | 128 | 22 / 10 | Nonlinear subset inside a proper fixed-bit hull. |
| q44 | 42 | 1 | 512 | 128 | 42 / 19 | Affine hull smaller than fixed-bit hull, but membership still nonlinear. |
| q154 | 50 | 3 | 128 | 128 | 50 / 14 | Nonlinear subset inside a proper fixed-bit hull. |
| q90 | 54 | 1 | 512 | 512 | 54 / 21 | Nonlinear subset inside a proper fixed-bit hull. |
| q15 | 48 | 1 | 512 | 256 | 48 / 18 | Last surviving record prefix; later visible bit is rejected. |

All twelve sampled sets are nonaffine. A concrete low-bit relation remains even without fixed bits: q18 has104 members with odd parity on bits0,1,2 and9 with even parity, giving absolute Walsh coefficient95 out of113. This is an exact count; no statistical significance or randomness claim was tested. Fixed-bit characters often give the trivial maximum equal to cardinality, so the probe also reports the strongest character that is not constant on the set.

The unexpected reversal check preserves all cylinder and affine properties but substantially changes sorted-integer runs: q27 goes108 to35, for example. An interval-looking picture is therefore representation dependent. The parity control correctly has no fixed bits but an affine hull of512; the size128 random control has full hull1024 and largest absolute coefficient38. These are instrument controls, not a fitted null model for channel states.

The depth13 record search returned R13=17 with three witnesses. Its first visible word000101101101011 follows states0,1,3,6,12,20,15 before rejection at index6 (the seventh visible bit). This left-half record does not satisfy the width10 right-channel constraint. The proposed record-reaching comparison was therefore not completed: the picture is explicitly labeled last valid prefix. No contradiction with either instrument follows; their admissibility conditions differ.

Probe: tests/probes/lexicon/rule30_gpt_shapes.py --output OUTPUT_DIRECTORY. It reconstructs everything, leaves data outside git and renders a13-panel membership SVG; optional PNG was unavailable because matplotlib is absent. The final run retains that limitation. No large job was duplicated. Conclusion: fixed-bit cylinders and affine spaces alone cannot exactly represent this width10 automaton. Boolean/parity structure may still support compression, but no uniform-width closure, formula for entropy or prize theorem is proved.


## G24. Periodic Garden-of-Eden density tends to one (2026-10-06)

Proof response to Local C046, using G22's equations; no new experiment. Write an input to the induced ternary map as the compatible pair(C,A). Compatibility says that if A(t)=1 then C(t)=1-A(t+1). The new pair is(D,C), with D(t)=C(t+1) XOR(C(t) OR A(t)). A target ternary symbol less than2 means its second component C is0, and its first component D is that symbol.

Suppose an output contains100 or101 at three consecutive sites. The predecessor has C(t)=C(t+1)=C(t+2)=0. Hence D(t)=A(t)=1 and D(t+1)=A(t+1)=0. Compatibility would force C(t)=1, a contradiction. Both length-three words are therefore forbidden in every output, without any periodicity assumption on the predecessor. This is an explicit finite obstruction strengthening G22's periodic10 example.

Among all3^P rooted configurations with period dividing P, take floor(P/3) disjoint triples and leave the remainder unconstrained. At most25 of27 words per triple are allowed, so the fraction admitting any predecessor is at most (25/27)^floor(P/3). Consequently the Garden-of-Eden fraction tends to1, not1/3. This bound is deliberately loose; it proves the limit without claiming an exact finite-P count or exact entropy. If one restricts to least period exactly P the conclusion persists: the nonprimitive words number at most P*3^(P/2), negligible relative to3^P.

For the original four-symbol two-track F, G22 already gives exactly3^P image configurations among4^P periodic targets, so the Garden-of-Eden fraction is exactly1-(3/4)^P. Thus both natural interpretations of “among periodic pairs” have limit1. The earlier density1/3 concerns ones in a uniformly chosen second track, a different statistic.

Unexpected scope check: the obstruction excludes nonperiodic predecessors too; requiring a periodic predecessor is unnecessary. Conversely, avoiding100 and101 is only a necessary condition, not a proved full image description. No deeper iterated-image classification follows. Project-local derivation, no novelty claim.


## G25. Slow-wall tail information: causal coding audit, preregistration (2026-10-06)

Continue G18.4's leading-difference proof and G15's independent white-block coding, following Local C049. Startup wall/merge checks already passed for this block before its scheduling interruption; no repeat. No new route or novelty claim: this extends the project's triangular inverse identity.

Predict TC1: if two visible inputs first differ at white time q, their forced initial left rows first differ at depth q+1, independently of subsequent inputs. Predict TC2: for wall0^a1^b with b>=2, n complete periods give exactly(a+1)^n distinct initial prefixes of length n(a+b), with an inverse recovering every latch. Counterfactual: a reset makes two different white-block histories yield the same complete-period prefix. Independently compare column inversion with backward row construction and forward Rule30. Unexpected TC3: changing sigma only at black times changes no left cell in the tested triangle; this is an algebraic control, not a claim that arbitrary modified sigma is physically admissible on the right. A finite-state sequential encoder is not ruled out by failure of one finite prefix to determine the entire row.

### G25 result: an exact triangular coding, not finite tail closure

Fix any infinite wall tau. Identify visible inputs sigma if they agree at every time when tau=0; differences at black times are masked by tau OR sigma. The map from these effective inputs to the forced initial left row is injective and triangular. If two effective inputs first differ at time q, their rows first differ at depth q+1.

**Proof.** The column immediately left of the wall is pi(t)=tau(t+1) XOR(tau(t) OR sigma(t)). It depends on sigma(t) only at white times. Every deeper column is obtained by the same inverse recurrence, so no black-time sigma bit reaches any left cell. A depth-d cell at time t depends only on effective inputs at times at most t+d-1. For a first white-time difference at q, pi first differs at q. In reconstructing the next column, its first different cell is one time earlier: the next-time XOR term differs there, while the two same-time OR terms depend only on earlier effective inputs and agree. Induction gives first difference at time q-d+1 for depth d as long as this time is nonnegative. Thus initial depths1..q agree and depth q+1 differs. No later effective input can reach those initial depths. Conversely, forward Rule30 from an initial prefix of length N with the fixed wall recovers pi(t) through time N-1, and hence every white-time sigma(t) in that window. This is a finite inverse at every N.

For slow wall0^a1^b with b>=2, G15 supplies independent monotone white blocks0^r1^(a-r), r=0..a, with a width-one right extension. Therefore n complete periods give exactly(a+1)^n distinct forced initial prefixes of length np, p=a+b. Each prefix determines all n latch positions; later blocks cannot change it. The per-spatial-cell prefix growth rate is exactly log2(a+1)/p: for arbitrary prefix lengths between np and(n+1)p the counts are bracketed by the corresponding two complete-period counts. This is the same coding rate transferred to the spatial row, not an entropy assertion about finite-support rows or the actual full right half.

**State consequence.** For any fixed initial depth L and any fixed finite number of early latches, choose a later period starting at q>=L and change its latch from all0 to all1. G15 extends both histories within the width-one domain. Their initial prefixes through depth q agree and their rows differ at q+1. Thus no finite prefix or fixed number of latches determines the complete initial row over this domain. A reset-protected band can coexist with information beyond it; it does not erase the entire future history. This strengthens G18.4 from one pair to every observation horizon.

**What this does not prove.** A finite-state sequential encoder can emit infinitely many words and is not excluded by injectivity or these counts. Nor is a bounded-debt potential excluded. The theorem rejects finite-prefix closure of a fixed-time entire row, not every compressed representation. To address finite left support, one still needs a tail-sensitive invariant or a characterization of latch histories whose coded row is eventually0. No such characterization is supplied here.

**Checks.** rule30_gpt_tail_coding.py, one Intel CPU process, under one second: TC1 all120 first-difference tests; TC2 all5080 histories over64(a,b,n) families, a1..4,b2..5,n1..4, with independent backward-row construction and scalar truth-table forward recovery; TC3 all168 black-time perturbations preserve every tested left cell. The counterfactual prefix collision fails. TC3 is the unexpected masking check, conducted on arbitrary algebraic inputs; it does not certify the changed right trace as physical. These checks support the induction, not substitute for it. No Local long run repeated.


## G26. Rule210 cancellation audit, preregistration (2026-10-06)

Follow Local C051/C053 and section8.65 without duplicating the width search. Startup wall/merge checks both passed. Separate the measured cap-reaching continuations from the claimed explicit infinite witness. Test RC1: the specified visible word1011000011111111 followed by zeros yields an all-zero initial left prefix through256 cells under Rule210's inverse. This is a blind audit of the published witness, not an accepted theorem. Compare independent backward-row and scalar truth-table forward reconstructions. Test RC2: starting with an empty left row against0101, the left neighbour stays0 at every odd time, the condition needed to maintain the wall. Counterfactual: left-permutivity alone implies this clock compatibility (control Rule30). Unexpected check: audit the left-spreading hypothesis in Kopra's Corollary3.7 and distinguish it from left-permutivity alone. A finite check cannot certify a claimed infinite witness.

### G26 intermediate failure and next prediction

RC1 refuted: the specified16-bit visible word followed by zeros has first nonzero initial left cell at depth65 (then69,71,...). Through depth64 it mimics the true empty-left trace. RC2 finite control: empty-left evolution against0101 has no odd-time left-neighbour ones through256 steps. This does not yet prove infinite compatibility.

Next RC3 prediction before run: on the empty-left evolution, every occupied left cell at time t has depth j with t+j odd, so the AND-NOT reduces exactly to XOR on that domain. Consequently it is Rule90 driven by the same wall, and its even-time visible sigma obeys sigma(0)=1 and sigma(2n)=floor(log2(n)) modulo2 for n>=1. Test through512 steps with truth-table, bit-vector and independent Catalan-parity coding. Retain the failed finite-word continuation.

### G26 theorem: a dyadic witness replaces the failed eventual-zero continuation

**Parity invariant.** Evolve an initially empty left half against tau(t)=t modulo2 under Rule210. At time t, a black left cell at depth j can occur only when t+j is odd. Induct: the wall obeys this parity too; if the centre is black both neighbours are0, and if the centre is0 its update is left XOR right. Thus the AND-NOT equals the right bit throughout this domain, and the update is exactly Rule90. The opposite parity remains0 at the next time. In particular pi(t), the depth1 trace, is0 at every odd t. This proves infinite clock compatibility of the left half, not just the finite test.

At even times define sigma(2n)=1 XOR pi(2n); at odd times sigma is arbitrary. Then Rule210's wall equation gives the next wall bit1 at even times and0 at odd times. Every left cell and the wall therefore update consistently for all time. No assertion about the update of column1 or the full right half is included. This is a rigorous one-sided empty-left witness, and LR fails for Rule210.

**Exact visible trace.** Rule90 is linear. Each wall1 at odd time2m+1 enters depth1 at time2m+2. Its contribution to depth1 at time2n counts walks from depth1 back to depth1 in2(n-m-1) steps that never reach depth0 internally. These are Dyck walks, counted by Catalan number C_(n-m-1). Hence pi(2n) is the parity of the sum C_0 through C_(n-1). This uses the standard Catalan decomposition, not a new counting mechanism.

For completeness, the generating series C(z) for Catalan numbers obeys C(z)=1+z*C(z)^2. Over binary coefficients the square is C(z^2), so repeated substitution gives C(z)=sum over r>=0 of z^(2^r-1). Therefore pi(2n) is the parity of the number of powers2^r<=n. The exact witness is sigma(0)=1 and, for n>=1, sigma(2n)=floor(log2(n)) modulo2; odd-time bits may be0. Its visible word begins1011000011111111, then16 zeros, then32 ones, then64 zeros, and so on. Infinitely many switches and unbounded constant runs prove this word is not eventually periodic.

**Failed claim retained.** The section8.65/C051/C05316-bit word followed by zeros agrees with this witness through32 visible bits, then first differs at even time64. Triangular inversion propagates that difference to initial depth65. Two independent inverses verify its first black cell there. Cap-reaching measurements remain finite evidence; this separate parity proof certifies the corrected infinite witness. Local's prose was not silently changed; C055 requested a correction.

**Unexpected prior-art scope check.** [Kopra, Rapid left expansivity (2023), Definition3.3 and Corollary3.7](https://www.utupub.fi/bitstream/handle/10024/174540/1-s2.0-S0304397522007502-main.pdf?sequence=1) requires left-spreading as well as left-permutivity. Rule210 has f000=0 and f001=1, so a nonzero left edge advances one site left at every step; its XOR left argument is permutive. Thus the theorem applies to actual left-bounded full Rule210 orbits. It excludes an eventually periodic adjacent pair; it does not turn a left-only witness into a physical full orbit or settle B. Its hypotheses should be named when used.

**Checks and boundaries.** rule30_gpt_210_audit.py: RC1 refuted at65, two exact inversion constructions agree; RC2/RC3 all512 parity/Rule90/time steps pass with scalar truth-table and bit-vector agreement,255 exact-integer Catalan parity checks and512 all-zero inverse cells for the corrected code. Rule30 counterfactual fails clock compatibility; all four left-permutive truth-table pairs and left-spreading bits pass. Both startup probes passed. No Local record/width search was rerun. Catalan counting and Kopra's theorem are credited; no novelty or Rule30 prize claim.

**Further exact consequence (analytic, no additional run).** The dyadic witness has no limiting ones density. For the first2^k visible bits, the number of ones is1 plus the sum of2^j over odd j<k. For k=2m this gives(2*4^m+1)/3 and density tending to2/3; for k=2m+1 it gives the same numerator divided by2*4^m and density tending to1/3. Density changes monotonically within each constant run, so liminf=1/3 and limsup=2/3. The finite0.34 observation in Local C054 is a sample proportion, not an asymptotic density. This concerns the one-sided Rule210 witness, not a Rule30 prize orbit.

The same word has zero word-count entropy: for word length l, choose the first power2^k>=l (at most2l). At starting positions beyond2^k, all runs have length at least l, so each length-l factor crosses at most one switch, giving at most2(l+1) forms. Earlier starting positions contribute at most2l more. Hence factor complexity is at most4l+2. No exact2.5l asymptotic is claimed.


## G27. Finite-state zero-keeping: autonomous generators versus indexed automata (2026-10-06)

Preregister scope audit following Local C053/C054 and G26. Both startup checks pass. This uses existing G26's exact formula and the already-read Jen/Kopra mechanism; automatic-sequence terminology credited below, no novelty claim. Predict FS1: a three-state output automaton reading binary n reproduces G26's dyadic visible word for0<=n<65536. Unexpected FS2: arbitrarily padded leading zeros leave its output unchanged (check0..1023 with0..8 zeros). Counterfactual: an aperiodic sequence admits no finite-state description. The automaton will refute that statement without refuting eventual periodicity of an autonomous finite-state generator. No new CA run or Local search.

### G27.1. A three-state indexed description of an aperiodic word

Let d(0)=1 and d(n)=floor(log2(n)) modulo2 for n>=1, the exact G26 visible trace. Read the binary digits of n from most significant to least. The automaton starts in S, with outputs S=1,A=0,B=1:

| State | Read0 | Read1 | Output |
|---|---|---|---:|
| S | S | A | 1 |
| A | B | B | 0 |
| B | A | A | 1 |

Proof: leading zeros keep S unchanged. The first1 sets output0; every remaining digit toggles it, giving the parity of the number of digits after the first1. An all-zero word stays in S and represents0. This proves correctness for every index, including padded forms. In standard terminology d is2-automatic, although G26 proves it aperiodic. The externally supplied index grows in length: this is not an autonomous generator with three internal states that produces the sequence one term at a time.

The standard automaton/numeration framework is credited to [Allouche and Shallit, Automatic Sequences (2003), publisher's chapter extracts](https://www.cambridge.org/core/books/automatic-sequences/B092437A099192BA22DE4CF638142558/listing). Only the public extracts were read; the explicit machine above is derived here from G26's formula. No novelty claim or general automatic-sequence theorem is needed.

### G27.2. The periodic-pair obstruction works on the forced half-line

**Lemma (Jen/Kopra mechanism, half-line form).** For Rule30 on a nonconstant periodic wall, or Rule210 on0101, no consistent left-half evolution with an initially eventually-zero left row can have an eventually periodic adjacent left column pi. Right-half realizability is not a premise.

**Proof.** Take a common eventual period P and common preperiod T for tau and pi. Left-permutivity solves each left column from the two columns to its right, using their same-time cells and the next-time inner cell. Consequently every further left column is P-periodic from the same T: the preperiod does not grow with depth. Let the initial row have no1 at depths beyond L. By the radius-one light cone, for sufficiently large depth d>L+T+P, its trace is0 through time T+P-1, even allowing arbitrary changes at the wall. Periodicity then makes that column0 for all time. Thus a fixed sufficiently far-left region stays empty forever.

For Rule30, a wall1-to0 transition forces pi=1 by its inverse identity, so a left1 eventually exists. For Rule2100101, a nonempty initial left row already supplies a left1; if it is empty, G26 supplies one at time2. Once any left1 exists, f001=1 and f000=0 make its leftmost edge advance left at every step, contradicting permanent emptiness beyond d. This proves the two stated cases. We do not assert the boundary-source argument for every possible elementary rule or wall.

This is the zero-height propagation argument in [Kopra (2023), Corollary3.7 and its proof](https://www.utupub.fi/bitstream/handle/10024/174540/1-s2.0-S0304397522007502-main.pdf?sequence=1), stated with its left-half boundary source explicit. It therefore does not assume a full right half merely to invoke a full-orbit theorem.

**Rule30 consequence.** On0^a1^b, eventual periodicity of the effective white-block latch positions implies eventual periodicity of pi by G18's identity, independently of arbitrary black-time sigma bits. Hence an infinite zero-tail continuation cannot be generated by an autonomous, closed finite-state machine for the latch positions. The machine's transition and output must be time-independent, all persistent information finite, and wall phase included. Last-W-latch recurrences with these properties are covered. A bounded output window alone does not certify that the evolving window has closed finite-state dynamics; an unbounded time index or other external input breaks the premise. No finite survival-length bound follows without a closure theorem for the acceptance test.

**Rule210 consequence.** Every infinite0101 zero-keeping continuation whose initial left row is eventually0 has an aperiodic effective visible sequence: if it were eventually periodic, pi at even times=1 XOR visible and pi at odd times=0 would give the forbidden periodic pair. This is an infinite conditional theorem, not a conclusion from the4369 finite samples. It does not prove that each sampled prefix continues forever, that all these words are2-automatic, or that a full right half exists.

**Checks.** rule30_gpt_finite_state_scope.py: FS1 all65536 indices and unexpected FS2 all9216 padded words pass; CF refuted by the explicit indexed automaton. The proof of the periodic-pair obstruction is analytic and uses existing G18/G26 mechanisms. The remaining useful target is a tail-sensitive invariant or an explicit closure theorem, not a further finite-state label inferred from aperiodicity.

### G27.3. Every Rule2100101-compatible left system is parity-sparse

Local C058 asks which zero-keeping streams are Rule90 in disguise. On this wall, all compatible left systems are. At black times the wall equation forces pi(2n+1)=0; tau itself vanishes at even times. Thus the two first columns have opposite temporal supports. Induct leftwards: if inner column c is supported on one parity and outer column r on the opposite parity, then c(t) AND r(t)=0, so the inverse l(t)=c(t+1) XOR((1-c(t)) AND r(t)) reduces to c(t+1) XOR r(t), supported on the opposite parity from c. Every column therefore satisfies x_t(-j)=0 whenever t+j is even. Initial ones may occur only at odd depths.

Conversely, any initial left row supported on odd depths evolves under the0101 wall with this parity invariant, reduces to Rule90 on the left, and has pi at odd times0. Choosing sigma at even times=1 XOR pi and arbitrary odd-time sigma keeps the wall. Hence parity-sparse initial rows characterize the compatible left class exactly. This is a one-sided classification and does not characterize physical full right halves. A finite-left row in this class has an aperiodic effective stream by G27.2. The classification is a direct inverse-support induction, not an extrapolation from Local's finite catalogue; no new catalogue was run.

**FS3 additional preregistration before run.** Check the new classification independently: all32 initial rows on odd depths through9 against scalar Rule210 for32 steps; all256 eight-bit effective visible words against inverse reconstruction through16 depths. In both directions every cell must have t+j odd; forward and inverse prefixes must agree where their cones overlap. Control: an initial1 at even depth2 violates the clock at its next black time. This is a bounded proof audit, not right-half realization.

**FS3 outcome.** All32 odd-depth finite seeds pass32 scalar forward steps and both inverse reconstructions; all256 eight-bit effective words reconstruct parity-sparse rows and recover exactly under scalar forward updates. The even-depth2 seed violates the clock at time1, as predicted. No additional large computation.

**Continuation corollary.** Any finite effective visible word of length n for Rule2100101 has an infinite one-sided continuation with finite initial left support. Invert it to the first2n initial cells, whose even depths are0 by the classification. Set every deeper cell0. This odd-depth initial row keeps the clock, and the radius-one cone/triangular inverse recovers the prescribed n bits. Its support is at most2n-1. Every such infinite continuation retaining an eventually-zero initial row is aperiodic by G27.2. Thus cap-reaching prefix evidence can be replaced by this existence construction; no full right-half compatibility is asserted.


## G28. Rule210 right compatibility: global parity obstruction, preregistration (2026-10-06)

Following C059/C061, take a reasoning constraint on full right compatibility, not a duplicate width search. Startup checks pending merge completion recorded below before running. Existing mechanisms: G27's parity/Rule90 subsystem and the elementary binary identity (L+R)^(2^k)=L^(2^k)+R^(2^k); no novelty claim.

Predict GP1: all47 configurations supported on a single parity within sites-4..4 match Rule90 through33 steps. GP2: their centres at times9,17,33 are0, excluding0101. Counterfactual: single-parity support suffices for a finite full clock witness. Unexpected GP3: a single even-site seed remains linear but has the wrong clock parity; mixed adjacent seed{1,2} activates the c*r nonlinear residue immediately. Verify exact difference recurrence between Rule210 and Rule90 on16 seed2306 mixed configurations, with scalar truth-table updates. No assertion that mixed parity is sufficient.

### G28 result: mixed parity and nonlinear activity are necessary

Startup wall/merge checks both passed before the run. GP1 all47 single-parity configurations in sites-4..4 match Rule90 through33 steps; GP2 their centres at9,17,33 are0. GP3 all16 mixed-parity seed2306 controls satisfy the exact difference recurrence and binary-power identity. Single even-site seed{2} stays linear but fails the clock parity; adjacent mixed seed{1,2} creates a nonlinear residue at its first update. CF rejected. These bounded controls accompany the following algebraic proof; no width-survival search was run.

**Global single-parity obstruction.** Rule210 is l XOR r XOR(c AND r). A configuration supported on one spatial parity has no adjacent black cells, so the nonlinear product is0. Its update equals Rule90 and flips occupied parity; induction preserves this reduction for all time. Let A=S+S^(-1) be the Rule90 operator over GF(2). Commuting shifts give A^(2^k)=S^(2^k)+S^(-2^k) by repeated squaring. If the initial support lies in[-R,R], then A x is supported in[-R-1,R+1]. For2^k>R+1, the centre of A^(2^k+1)x is0, since it samples A x at positions plus/minus2^k. Choosing k>=1 makes this an odd time, when0101 would require1. Thus no finite global single-parity Rule210 configuration keeps that clock. This is elementary additive-CA algebra, not a novelty claim.

By G27, any clock-compatible initial left row has no black cells at even negative sites; the centre is0 initially. Therefore any finite full clock witness must have a black cell at a positive even site (2,4,...), and initial support of both parities. The first wall update also requires x_0(-1) XOR x_0(1)=1. These are necessary conditions, not sufficiency or a proof of B. They give exact constraints for a future targeted search.

**Nonlinear-event certificate.** Compare full Rule210 evolution N with Rule90 evolution L from the same finite initial row. Let D=N XOR L and V_t(i)=N_t(i) AND N_t(i+1). Then D_(t+1)=A D_t XOR V_t and D_0=0. Hence D_T(0) is the XOR over t<T of (A^(T-1-t)V_t)(0). At T=2^k+1 with2^k>R+1, Rule90's centre is0. A Rule210 clock witness would need that weighted XOR of nonlinear events to be1. In particular some adjacent black pair must activate the nonlinear gate inside the centre's backward light cone. The identity records the required parity of the propagated events; it does not identify a realizable witness.

The exact difference controls use independent scalar truth tables, rather than assuming Rule210 and Rule90 are equal on mixed support. Probe: tests/probes/lexicon/rule30_gpt_210_obstruction.py. No data or generated files tracked. This completes the bounded audit; GPT now takes a separate Collatz proof lane at the owner's request to diverge.


## G29. Independent Collatz lane: signed rational complexity audit (2026-10-06)

Seed20261006 chose the signed/infinite-orbit and rounding audit from the three Collatz-only tasks recorded in C064. Existing W2 uses odd denominator D>0 and initial x=N/D. Audit the exact growth estimate for H_i=abs(N_i)+D, the requirement that the orbit has infinitely many distinct states, and the strict signed interval needed for unique length-n parity words. This is a scope/check extension of Terras/Dubickas, not a novelty claim or a proof of the Collatz conjecture.

Preregister CC1:2H_(i+1)<=3H_i for all signed N in[-128,128] and D=1,3,5,9. CC2: distinct numerator starts in the open interval(-2^(n-1),2^(n-1)) have distinct n-bit parity words for n1..8 and the same four D. Counterfactual: “infinite orbit” can mean merely infinitely many iterates, including a cycle, while retaining W2's growing bound. Unexpected CC3: the two closed-interval endpoints have identical n-bit words, so the signed interval width needs care. Audit the integer count using exact powers rather than floating-point logarithms.

### G29 outcome: the signed extension is valid with explicit hypotheses

Use a fixed positive odd denominator D and integer numerator N, not necessarily reduced. The accelerated Collatz iterate has numerator N/2 when N is even and(3N+D)/2 when odd. Negative numerators are included. “Infinite orbit” here means infinitely many distinct rational values, not infinitely many iterations of a cycle. A repeated numerator makes the future periodic, so an infinite distinct orbit has no repeats. Since bounded numerator intervals contain finitely many integers, such an orbit also satisfies abs(N_i) tending to infinity. This does not exhibit any such orbit.

Let H_i=abs(N_i)+D. The triangle inequality gives H_(i+1)<=3H_i/2, including both parity branches. The unshifted absolute numerator does not obey that bound in general: N=D=1 maps1 to2. Therefore W2's informal growth sentence must refer to this shifted height; its written constant already does. Induction gives H_i<=(3/2)^i H_0.

For a block length n>=1 define the exact integer count K as the number of i>=0 satisfying3^i H_0<=2^(i+n-1). Equivalently,

    K = max(0, 1 + floor((n-1-log2(H_0))/log2(3/2))).

For i<K, abs(N_i)<=2^(n-1)-D<2^(n-1). The K initial numerators are distinct and any two differ by less than2^n. Equal n-bit parity words would force their difference divisible by2^n: composing the n affine branches gives a difference multiplied by3^s/2^n, where3^s is odd and the resulting numerators are integers. Hence all K words differ and p(n)>=K. This proves the displayed W2 real-valued bound and makes its signed-domain rounding precise, including the equality case. Exact powers define K without numerical logarithms. Positive orbits can use the larger one-sided interval[0,2^n) and replace n-1 by n in the same count; this improves only the constant term.

**Counterfactual and unexpected checks.** The cycles0 and-1 have infinitely many iterates and parity complexity1, violating the proposed growing bound if distinctness is dropped. At the signed closed-interval endpoints plus/minus2^(n-1), the difference is exactly2^n and the n-bit words coincide. This refutes uniqueness on that closed interval; our shifted-height proof keeps all starts strictly inside it. The exact boundary control H_0=2,n=2 counts one start, not zero.

**Prior art.** Read Theorem5 and its proof, sections1/5 on pages246,249-250 of [Dubickas, On integer sequences generated by linear maps, Glasgow Math. J.51 (2009),243-252](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C40C0C07FEC20797475BB2899C436C9A/S0017089508004655a.pdf/on_integer_sequences_generated_by_linear_maps.pdf). His theorem concerns positive integer trajectories tending to infinity; the proof excludes repeated states and uses divisibility plus the3/2 growth estimate. The fixed-odd-denominator signed argument above is the project's extension of that mechanism, not a claim that his statement includes rationals. Only the relevant theorem/proof were independently read in this block; Local's previous full-paper reading is separately recorded.

**Finite controls.** collatz_gpt_signed_bound.py: CC1 all1028 growth cases(N from-128 to128; D1,3,5,9), CC2 all2008 open-interval parity words at n1..8, unexpected CC3 all32 endpoint pairs, exact equality-count control and both cycle controls pass. The hypotheses and infinite conclusion are proved analytically; finite tests do not establish existence of an infinite distinct orbit or the Collatz conjecture. This seeded audit is separate from Local's Rule30 jobs.


## G30. Collatz growth, odd density and conditional complexity (2026-10-06)

**Preregistration.** Extend G29's distinct-orbit sojourn argument using the orbit-specific upper exponential growth rate gamma of the shifted numerator height, rather than its universal log2(3/2) ceiling. Predict liminf p(n)/n >= 1/gamma when gamma>0, and superlinear complexity when gamma=0. Audit the signed rational identity gamma = (limsup odd-prefix density)*log2(3)-1 under the explicit hypothesis of an infinite distinct orbit. This sharpens the existing W2 slow-growth sentence; no novelty or divergent-orbit claim.

GD1: exact affine composition and multiplicative correction identities for D=1,3,5,9, starts -64..64 and prefixes through32, retaining zeros separately. GD2: finite distinct prefixes under a signed height threshold have different n-bit parity words (n1..8). Counterfactual: the density/growth identity holds for cycles too. Unexpected GD3: the fixed orbit -1 and positive cycle1,2 have non-vanishing correction terms, so both reject that counterfactual. Proof conclusions remain conditional, independently of these finite controls. Both standing startup checks passed this block.


### G30 theorem: orbit-specific growth forces a complexity slope

Fix odd D>0 and an accelerated Collatz orbit x_i=N_i/D with infinitely many distinct states. Define S_m as the number of odd numerator steps among indices0..m-1, delta as limsup S_m/m, and gamma as limsup log2(abs(N_m)+D)/m. Let p(n) count distinct length-n blocks in its infinite parity sequence. Then

    0 <= gamma <= log2(3/2),
    gamma = delta*log2(3)-1,
    liminf p(n)/n >= 1/gamma             if gamma>0,
    p(n)/n tends to infinity             if gamma=0.

These are conditional statements, not an existence theorem. They refine the existing W2 slow-growth consequence rather than claim a new complexity mechanism.

**Proof of the growth identity.** G29 shows abs(N_i) tends to infinity, hence the orbit never hits0 and abs(x_i) tends to infinity. With e_i=N_i modulo2, the exact identity is

    log2(abs(x_(i+1))) - log2(abs(x_i))
      = e_i*log2(3)-1 + e_i*log2(abs(1+1/(3*x_i))).

The last term tends to0, including for negative x_i; its Cesaro mean therefore tends to0. Summing gives log2(abs(x_m))/m = (S_m/m)*log2(3)-1+o(1). Replacing abs(x_m) by abs(N_m)+D changes the logarithm by log2(D)+log2(1+1/abs(x_m)), whose quotient by m tends to0. Taking limsup proves the identity. The lower bound gamma>=0 follows from integer shifted height; G29's universal3/2 bound gives the upper bound. In particular delta>=1/log2(3). No convergence of the odd density is assumed.

**Proof of the complexity bound.** For any epsilon>0 the definition of gamma supplies a finite C_epsilon>=1 with abs(N_i)+D <= C_epsilon*2^((gamma+epsilon)*i) for every i>=0 (absorb the finitely many early indices into C_epsilon). For all indices from0 through floor((n-1-log2(C_epsilon))/(gamma+epsilon)), when this upper limit is nonnegative, abs(N_i)<2^(n-1). The numerators are distinct; G29's affine/divisibility argument makes their length-n words distinct. Thus liminf p(n)/n >=1/(gamma+epsilon). Let epsilon decrease to0. For gamma=0 this proves divergence of the ratio, not merely an unbounded subsequence. Finite transients and the denominator affect only C_epsilon.

**Consequence for a finite complexity slope.** If c=liminf p(n)/n is finite, then gamma>0 and

    delta >= (1+1/c)/log2(3).

For c=2 this requires upper odd density at least approximately0.94639; for c=3 at least0.84124. Attaining the universal lower slope c=1/log2(3/2) would require upper odd density1. These are necessary conditions, not attainable examples. If the upper odd density is exactly1/log2(3), then gamma=0 and complexity is superlinear. If the odd density actually converges, the growth rate also converges to delta*log2(3)-1. Nothing here proves that an actual infinite distinct orbit has critical density or exists.

**Retained failure and unexpected check.** Dropping escape makes the density identity false. On fixed -1, odd density1 suggests growth log2(3/2), but the correction is log2(2/3) at every step, giving actual rate0. On cycle1,2, odd density1/2 suggests negative growth; the nonzero mean correction again gives actual rate0. A finite observed density does not imply a limiting density or asymptotic complexity slope.

**Independent finite controls.** collatz_gpt_density_growth.py checks16512 exact affine compositions,15633 nonzero multiplicative identities using rational arithmetic, and8352 words from distinct finite prefixes within strict signed intervals. Both cyclic counterfactuals pass as counterexamples. The exact product identity checks the telescoping mechanism independently of logarithmic numerics; the infinite conclusion follows from the proof and its hypotheses. No divergent trajectory is sampled. The shifted-height growth control was independently established in G29.

**Prior-art scope.** The divisibility/sojourn mechanism is Dubickas2009 Theorem5 and the project's W2 slow-growth observation (COLLATZ-PRIZE.md5), already read and credited in G29. The odd-density equation here is an elementary telescoping calculation with its hypotheses supplied, not a priority claim. The existing record's phrase “grows by sigma bits a step” can be replaced by the precise upper exponential rate above.
