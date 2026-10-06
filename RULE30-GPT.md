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


## G31. Collatz odd-run cost and the limitation of a density shortcut (2026-10-06)

**Preregistration.** Audit the exact all-odd prefix: L odd steps occur exactly when N+D is divisible by2^L, with D positive odd. Predict for N!=-D that L<=log2(abs(N)+D). OR1: all signed starts -128..128, D1,3,5,9 and L1..10; compare actual parity words, divisibility and the composed iterate. Counterfactual: the size bound also holds at N=-D. Unexpected OR2: a binary word with zeros at square indices has density1 and unbounded odd runs, but its run length is sublinear in the starting index; check indices through10000. This word is only a combinatorial control, not asserted to be a rational Collatz orbit. No new startup checks: continue the passed G30 block.


### G31 theorem: exact odd-run cost, with its fixed-point exception

For integer numerator N and positive odd D, the next L>=1 accelerated steps are all odd exactly when2^L divides N+D. On that prefix,

    2^L*(N_L+D) = 3^L*(N+D).

Necessity follows by composing the odd branch. For sufficiency, divisibility by2^L makes N odd, and after one odd step N_1+D=3(N+D)/2 is divisible by2^(L-1); induction finishes. This is the all-ones instance of the affine parity/residue correspondence already credited to Terras in W1, not a novelty claim.

If N!=-D, the exact number of consecutive odd steps is the exponent of2 dividing N+D. Since N+D is nonzero, this gives2^L<=abs(N+D)<=abs(N)+D. At N=-D the orbit is fixed at rational -1 and remains odd forever, so removing that exception makes the bound false. An infinite distinct orbit cannot visit this fixed point.

**Consequences and failed shortcut.** At orbit index i, an odd run has length at most log2(abs(N_i)+D). G30's growth ceiling therefore bounds it by (gamma+epsilon)*i+log2(C_epsilon) for every epsilon>0. The universal estimate also gives log2(H_0)+i*log2(3/2). These bounds exclude overly long individual runs at a given height; they do not by themselves exclude upper odd density1.

To see the logical limitation, let an abstract binary word have zeros precisely at indices k^2, k>=0, and ones elsewhere. Its first m positions contain floor(sqrt(m-1))+1 zeros, so its ones density tends to1. After the zero at k^2 there is an odd run of2k ones; at any start i the remaining run is at most2*sqrt(i). For every alpha>0,

    2*sqrt(i) <= alpha*i + 1/alpha.

Thus this word meets every positive linear run ceiling with a suitable constant. It is not eventually periodic: it has infinitely many zeros with unbounded gaps, whereas an eventually periodic word with infinitely many zeros has bounded zero gaps. This refutes only the inference from the run ceiling to density strictly below1. We do not assert its other G30 complexity constraints, its rational realization, or its exclusion from rational Collatz orbits. The initial wording “failing to represent an escaping rational orbit” was too strong for this control; realization is unresolved here.

**Controls and outcome.** OR1 passed all10280 signed congruence cases, with exact affine and height implications. The fixed-point counterfactual failed as predicted for all four D. Unexpected OR2 passed10001 run and10000 square-count controls. The infinite density/nonperiodicity conclusions are proved from the explicit word; the finite checks are only implementation controls. No sampled trajectory is declared divergent.

**Next useful question.** A joint restriction involving the heights at even steps, or the full 2-adic inverse and a real-size bound, would be needed to eliminate this shortcut's countermodel. G30/G31 alone provide no such restriction. The record already rejects identifying real and 2-adic series limits (COLLATZ-PRIZE.md5); that objection must remain in force.


## G32. Joint affine normalization and the metric gap (2026-10-06)

**Preregistration.** Audit the joint odd/even history via F_m=sum(e_j*2^j/3^(S_(j+1)), j<m), where S counts odd steps. Predict2^m*N_m/3^S_m=N_0+D*F_m. A lower odd density strictly above log(2)/log(3) makes F_m converge over the reals; this alone must not identify that limit with its 2-adic limit. NF1: exact normalization for D1,3,5,9, signed starts -32..32 and m1..32. NF2: the square-zero control's first1..32 bits are each realized by the residue -D*F_m modulo2^m, checking all four D. This is a finite residue assertion, not a single rational realization. Unexpected NF3: rational partial sums a_m=2^m/(2^m+1) converge to1 over the reals and0 2-adically. Counterfactual: convergence in both metrics forces equal limits. Retain fixed -1 as an actual cancellation control. Reuse passed startup checks.


### G32 theorem: real growth normalization does not identify the parity inverse

For a fixed positive odd D and actual numerator orbit, let e_j be its parity, S_m=sum(e_j,j<m), A_m=3^S_m/2^m, and F_m as preregistered. Composing either affine branch gives the exact identity

    N_m = A_m*(N_0+D*F_m).

For an abstract binary word, the same formula describes the affine branch composition, but integrality at every step remains a separate condition. Its finite initial numerator residue is -D*F_m modulo2^m. Indeed denominators in F_m are odd; this congruence makes the composed numerator integral, and the parity/residue bijection gives exactly the chosen prefix. The inverse residues are compatible as m increases because F_(m+1)-F_m is divisible by2^m in the odd-denominator ring. Finite residues, however many, do not exhibit one ordinary rational numerator matching all prefixes.

**Real convergence, with an explicit hypothesis.** Suppose liminf S_m/m exceeds log(2)/log(3). Choose d between those two quantities. There is a finite C such that S_m>=d*m-C for all m. Every nonzero summand of F_m is at most3^C*(2/3^d)^j; the ratio is strictly less than1. Thus F_m has a finite real limit F_R. The real normalized coefficient is

    lambda_R = N_0 + D*F_R,
    N_m/A_m tends to lambda_R over the reals.

If lambda_R is nonzero, N_m eventually has its sign and N_m is asymptotic to lambda_R*A_m. If the odd density also converges to delta, the logarithmic absolute growth rate is delta*log2(3)-1. Cancellation lambda_R=0 must not be dismissed: the actual fixed orbit -1 has F_R=1 and lambda_R=0. No conclusion about escape follows merely from real convergence of F_m.

**The separate 2-adic limit.** The j-th summand has 2-adic valuation at least j (or is zero), so F_m always converges 2-adically to F_2. For an actual integer numerator orbit, the exact identity gives N_0+D*F_m=2^m*N_m/3^S_m, whose 2-adic valuation is at least m. Hence N_0=-D*F_2, an equality in the 2-adic field. It does not imply N_0=-D*F_R. A high-density parity word makes both limits available, not equal. Rationality of the inverse -D*F_2 is the missing realization condition for the square-zero control; the real coefficient cannot replace it.

**Unexpected counterexample to the metric shortcut.** Define a_0=0 and a_m=2^m/(2^m+1) for m>=1. The series with rational terms a_m-a_(m-1) has partial sums a_m. Over the reals, its error from1 is1/(2^m+1), tending to0. Its 2-adic valuation is exactly m, so it tends to0 2-adically. All denominators are odd. This disproves the general implication “convergence in both metrics means the same limit”; it is not a claim that this series is a Collatz inverse.

**Controls.** NF1 passed8320 signed exact normalization identities. NF2 passed128 square-zero prefix residue realizations; each length has its own residue representative, not one exhibited infinite rational orbit. NF3 passed64 exact telescoping/error/valuation controls. The -1 geometric cancellation passed independently. Infinite convergence conclusions follow from the proofs, not these finite counts.

**Prior-art boundary.** The affine composition and inverse series are the established Terras/Bernstein mechanism already used in COLLATZ-PRIZE.md. Read the abstract of [Lopez and Stoll, The 3x+1 Periodicity Conjeture in R (2021)](https://arxiv.org/abs/2101.12747), which claims an exclusion above the critical lower density. This block did not audit its51-page proof or adopt that claim. The project's existing objection about real/2-adic identification is retained; the general counterexample above independently establishes why such an identification would need an additional theorem. No priority claim and no repaired density theorem.

**Outcome/next boundary.** Joint normalization organizes the history but does not close the rational-realization gap. A future proposal must control F_2 or explicitly prove a bridge to F_R; merely showing real convergence, a sign, or an irrational real sum is insufficient. This closes the proposed metric shortcut, not the Collatz lead.


## G33. Periodic inverse bridge and exact repeated-block budget (2026-10-06)

**Preregistration.** For a length-p parity word w with s ones and affine intercept B, predict its rational cycle point c=B/(2^p-3^s). Real and 2-adic inverse limits agree when3^s>2^p; for a nonzero word with3^s<2^p, the real inverse series diverges although the 2-adic inverse is rational. Also audit a precise finite repetition ceiling: for x=N/D and M=N*(2^p-3^s)-D*B, the next k full copies of w occur iff2^(kp) divides M. Noncycle maximum is floor(v2(M)/p); M=0 is the actual cycle case. This is an exact-constant version of the existing periodic-window principle, not a new mechanism.

PB1: all words of lengths1..6, their fixed-odd-denominator cycles and real/2-adic geometric formulas. PB2: starts -16..16, D1,3,5 and k1..4 for those words, comparing divisibility with direct iteration. Counterfactual: a rational periodic inverse must have a convergent real inverse series. Unexpected PB3: nonprimitive word1010 has the same cycle point as10, but counts full repeats in four-step units, not two-step units. Retain the all-zero exception. Reuse the passed startup checks; no long job.


### G33 theorem: the periodic bridge and the exact number of full repeats

Let w=(e_0,...,e_(p-1)) be a nonempty finite binary word, s its number of ones, and B the integer affine intercept, so its composed branches act as (3^s*x+B)/2^p. Set

    c = B/(2^p-3^s),
    r = 2^p/3^s,
    F_p = B/3^s.

The denominator2^p-3^s is odd and nonzero (powers of2 and3 cannot coincide for p>=1). The inverse series for the infinite repetition w has block sums F_p*r^q. Since the 2-adic absolute value of r is2^(-p)<1, its 2-adic sum is F_p/(1-r), and its inverse point is c=-F_p/(1-r). By the parity/residue correspondence this odd-denominator rational has precisely the prescribed repeated parity word; its p-step branch composition fixes it. Its least orbit period may divide p. This is the known rational cycle formula, not a new family of cycles.

For nonzero w, B>0. When3^s>2^p, r<1 over the reals as well, so the real and 2-adic geometric sums both equal the same rational F_p/(1-r), and c<0. When3^s<2^p, the positive real block sums grow and the real series diverges, while c>0 remains a rational 2-adic inverse. The all-zero word has B=0 and both inverse sums0, irrespective of r. Thus rational periodic realization does not imply real convergence; nor does agreement in this periodic case justify agreement for aperiodic words.

**Exact finite repeat budget.** For any start x=N/D with integer N and positive odd D, write

    M = N*(2^p-3^s)-D*B.

The difference x-c has denominator D*(2^p-3^s), which is odd, and numerator M. By W1, the first kp parities equal k full copies of w exactly when2^(kp) divides M. If M!=0, the exact maximum number of full copies is floor(v2(M)/p), and the entire common binary prefix has length v2(M). In particular kp<=log2(abs(M)). If M=0, x=c and the word repeats forever. This includes signed numerators and unreduced representations; multiplying numerator and denominator by an odd factor does not change v2(M).

This is an exact arithmetic version of the existing periodic-window principle, with the cycle exception explicit. It proves again that an eventually periodic parity sequence of an ordinary odd-denominator rational is eventually cyclic: at the beginning of its periodic tail every k is allowed, forcing M=0. No divergent orbit is produced or excluded beyond this known periodic case.

**Unexpected unit-of-count control.** Words10 and1010 have the same cycle point1. Start17 differs from it by16, so its common prefix has length4: two full10 blocks, one full1010 block, then a mismatch. Treating an arbitrary supplied block as a primitive period would miscount.

**Retained counterfactual.** The positive cycle1,2 has parity word10, c=1 and real inverse block ratio4/3. Its positive real terms do not tend to0, so the real series diverges although its 2-adic inverse equals the rational1. The negative cycle -5,-7,-10 has word110, ratio8/9 and convergent inverse in both metrics. Neither cycle satisfies G29/G30's infinite-distinct hypothesis.

**Controls and prior art.** collatz_gpt_periodic.py passed126 cycle/geometric controls (39 nonzero words with real convergence,81 with real divergence,6 all-zero words),49896 signed repetition/divisibility comparisons, and the nonprimitive-block control. Classification of infinite convergence is proved above, not inferred from truncation. The established Terras/Bernstein correspondence, rational cycle formula and W1/periodic-window discussion are already recorded in COLLATZ-PRIZE.md4–5; the tested denominator example there agrees with this formula. No novelty claim. Document validation is required before publication.

**Next boundary.** Periodicity supplies an algebraic bridge. A proposed bridge for aperiodic words needs a separate argument; this known-case audit supplies controls for it, not that argument. The exact repeat budget can test future near-periodic candidate prefixes without interpreting finite repetition as an infinite cycle.


## G34. Aperiodic inverse exclusion from lacunary even steps (2026-10-06)

**Preregistration.** Apply G31 to a parity word whose zero positions are z_k. Predict that any ordinary rational realization with infinitely many zeros must obey limsup z_(k+1)/z_k <=1+log2(3/2)=log2(3). Thus zeros at positive powers of2 give an irrational 2-adic inverse, while square-zero spacing is not excluded by this criterion. This is an elementary application of the known sojourn/odd-run mechanism, not a novelty claim.

LG1: for p=1,2,4,...,128 and D1,3,5,9, realize the finite power-zero prefix through index2p by its signed least residue; verify every bit and the necessary exact height inequality (abs(N)+D)*3^(p+1)>=4^p. Unexpected LG2: every such finite prefix is realizable although the infinite inverse is predicted irrational. Counterfactual: the infinite exclusion makes its finite prefixes unrealizable. Retain the fixed -1 exception: a later zero prevents entering that fixed point. Reuse passed startup checks.


### G34 theorem: a necessary gap bound for rational parity realization

Let x=N/D be any ordinary rational with positive odd D and integer N. Suppose its accelerated parity sequence has infinitely many zero positions z_k in increasing order. With alpha=log2(3/2) and H_0=abs(N)+D,

    z_(k+1)-z_k-1 <= alpha*(z_k+1)+log2(H_0),
    limsup z_(k+1)/z_k <= 1+alpha = log2(3).

**Proof.** After the zero at z_k, the next L=z_(k+1)-z_k-1 steps, starting at i=z_k+1, are all odd. If L>0, G31 gives2^L<=abs(N_i)+D, unless N_i=-D. That exception cannot occur because a later zero is prescribed and -D is fixed forever odd. For L=0 the same inequality holds because shifted height is at least1. G29's universal height estimate gives abs(N_i)+D<=(3/2)^i*H_0. Take logarithms, substitute i and L, and divide by z_k tending to infinity. No divergent-orbit hypothesis or density limit is required. This is a sufficient exclusion test, not a claimed optimal gap bound.

**Concrete aperiodic exclusion.** Take e_i=0 exactly at positive powers of2 and e_i=1 elsewhere. Its consecutive zero ratio is2, violating the necessary bound log2(3)<2. The compatible inverse residues define a unique 2-adic integer by W1/G32. If that inverse were an ordinary rational, its reduced denominator would be odd, and the theorem would apply, a contradiction. Hence this specific inverse is irrational. This is a parity-realization exclusion; it does not prove the Collatz conjecture or exhibit an escaping ordinary rational orbit. The square-zero word has ratio tending to1 and remains unresolved by this test. Density1 alone is not the exclusion mechanism.

**Finite certificate budget.** A prefix through index2p, where p is a power of2, includes p-1 odd steps after index p and a subsequent zero. Any rational start matching it must satisfy

    (abs(N)+D)*3^(p+1) >= 4^p.

Indeed2^(p-1)<=H_(p+1)<=(3/2)^(p+1)*H_0; rearrange using exact integers. Thus the required initial height tends to infinity with these prefixes. A finite prefix has a rational residue witness; what fails is a fixed ordinary rational witness for all prefixes. This addresses the quantifier gap directly.

**Controls and retained counterfactual.** LG1 passed32 signed least-residue witnesses for p1..128 and D1,3,5,9, verifying2072 bits and every exact height budget. Unexpected LG2 therefore refutes “infinite exclusion means its finite prefixes are unrealizable”. Infinite irrationality is proved by the gap bound; it is not inferred from the finite table. The fixed -1 exception and the later zero are both essential in the finite certificate argument.

**Prior-art scope.** This is an elementary application of the established parity/residue and growth mechanisms in W1/W2 and G29/G31, with no novelty claim. A targeted search found Monks and Yazinski's [The autoconjugacy of the 3x+1 function](https://www.sciencedirect.com/science/article/pii/S0012365X03001250), already mentioned in COLLATZ-PRIZE.md5; fetching the publisher page returned403, so this block has not audited whether it contains this precise gap criterion. Do not infer priority from the search. The argument above is self-contained and avoids identifying real and 2-adic limits.

**Next boundary.** Use the spacing criterion as a filter for proposed aperiodic parity candidates. It leaves sublinear-gap sequences such as square-zero words open; a stronger inverse constraint would have to address that remaining class.


## G35. Even-step correction excludes the critical gap ladder (2026-10-06)

**Preregistration.** Sharpen G34 with H_i=abs(N_i)+D, A_i=3^S_i/2^i and E_i=sum(2^j/3^S_j over even steps j<i). Predict H_i<=A_i*(H_0+D*E_i). For density1 parity words E_i has a finite real limit, so log2(H_i)<=log2(3/2)*i-K_i*log2(3)+C, where K_i counts even steps. Apply this to zero positions z_0=1, z_(k+1)=ceil(z_k*log2(3)), computed exactly as bit_length(3^z_k). Predict irrational inverse even though its zero ratio tends to the G34 threshold.

EC1: exact rational envelope for signed starts -32..32,D1,3,5,9 through32 steps. EC2: first16 critical ladder gaps certified by exact integer inequalities2^(z_next-1)<3^z<=2^z_next. Unexpected EC3: fixed0 has E_i=2^i-1 and equality in the envelope; its E_i diverges, so the density hypothesis cannot be dropped. Counterfactual: shifted height contracts by exactly1/2 at every even step; N=2,D=1 refutes it. Reuse passed startup checks.


### G35 theorem: the critical rounded-geometric zero ladder has irrational inverse

Let S_i count odd steps and K_i=i-S_i count even steps. Define A_i=3^S_i/2^i and E_i=sum(2^j/3^S_j over even steps j<i). For every signed ordinary rational start N/D with positive odd D,

    H_i=abs(N_i)+D <= A_i*(H_0+D*E_i).

**Envelope proof.** At an odd step H_(j+1)<=3H_j/2 by G29. At an even step H_(j+1)=H_j/2+D/2 exactly. Divide by A_(j+1), which is3A_j/2 or A_j/2 respectively. Odd steps do not increase H/A; an even step increases it by D/A_j=D*2^j/3^S_j. Sum these increments. The additive term is essential; dropping it fails already at N=2,D=1.

If liminf S_i/i>log(2)/log(3), then E_i has a finite real limit E_R: choose d above the critical density and below the liminf, and C with S_j>=d*j-C. Its summands are bounded by3^C*(2/3^d)^j, a convergent geometric majorant. Thus for a fixed start there is a finite constant C_H with

    log2(H_i) <= alpha*i-K_i*log2(3)+C_H,
    alpha=log2(3/2), C_H=log2(H_0+D*E_R).

This keeps the cumulative penalty from the even steps that G34's universal bound discarded. It does not identify real and 2-adic inverse sums.

**Boundary exclusion.** Put q=log2(3), z_0=1 and z_(k+1)=ceil(q*z_k). Define a binary parity word with zeros exactly at the z_k and ones elsewhere. The recurrence has the exact integer implementation z_next=bit_length(3^z), since3^z is never a power of2. From q*z_k<=z_next<q*z_k+1, the positions grow geometrically, the zero count is O(log(i)), the ones density tends to1, and z_next/z_k tends to q. Therefore G34 alone, whose bound is <=q, does not exclude this word.

Suppose its inverse were an ordinary rational. At i=z_k+1 the next L=z_next-z_k-1 steps are odd and a later zero rules out the fixed -1 exception. G31 requires L<=log2(H_i). But

    L >= alpha*i-q,
    L <= alpha*i-K_i*q+C_H,
    K_i*q <= C_H+q.

At these indices K_i=k+1 tends to infinity, a contradiction. Hence this word's unique 2-adic inverse is irrational. This is a concrete boundary refinement using established growth/parity mechanisms, with no novelty or prize claim. It does not decide the square-zero inverse: its remaining odd runs are sublinear, so the much larger linear allowance persists even after the even-step penalty.

**Finite form.** A start matching the ladder through the next zero must satisfy H_0+D*E_i>=3^(K_i-1), since2^z_next>=3^z_k and the envelope bounds the intervening run. No fixed numerator/denominator survives arbitrarily many such prefixes. This does not deny finite residue witnesses.

**Controls and failure retained.** EC1 passed8320 exact signed envelope checks. EC2 certified16 ladder gaps with integer powers, avoiding floating-point ceil; first positions1,2,4,7,12,20,32,51,81,129,205,325,516,818,1297,2056. Unexpected EC3: fixed0 saturates the envelope with E_i=2^i-1, which diverges. Thus real convergence of the correction requires a density hypothesis and cannot be inferred for all rational orbits. Infinite exclusion follows analytically;16 checked gaps do not establish it. Prior-art scope is G34's established mechanism/search boundary; priority remains unclaimed.


## G36. Complement route audit and the lower-density qualification (2026-10-06)

**Source audit before controls.** Found the author-hosted Monks–Yazinski autoconjugacy paper after the publisher403. Read the definition, Theorems2.1/2.7(b), and their relevant proofs (not the whole paper). The proposed shortcut “complementation preserves rational inverse points” is an unproved conjecture equivalent to rational-orbit periodicity, not an available lemma.

**Preregister CM1:** invert the square-zero and power-zero words and their complements modulo2^n for n1..64; verify all prefixes. CM2: exact examples3 and-4/9, -11/3 and8/5 have complementary128-bit parity words. Unexpected CM3:0 and-1 are complementary rational fixed points, so a conclusion that no complementary pair can both be rational must explicitly exclude eventual periodicity. Counterfactual: the divergent-orbit lower-density bound also holds for cycles. The0 fixed point and1,2 cycle reject it. Reuse startup checks already passed.


### G36 outcome: the lower-density bound is available; complement rationality is not

For an infinite distinct ordinary rational orbit, G30 proves

    log2(H_m)/m = (S_m/m)*log2(3)-1+o(1).

Because H_m>=1, taking liminf gives liminf S_m/m>=log(2)/log(3). This is stronger than the upper-density necessary bound explicitly noted in G30, and is already known. G30's growth-exponent formula still uses the upper density; the two roles must not be conflated. Cycles0 and1,2 have limiting odd densities0 and1/2, so the infinite-distinct hypothesis remains essential.

**Valid complementary exclusion (self-contained argument).** Let a binary word be not eventually periodic, and let x,y be the 2-adic inverse points of it and its bitwise complement. They cannot both be ordinary rationals. If they were, both orbits would be infinite distinct, since a finite orbit produces an eventually periodic parity word. Both lower odd densities would be at least beta=log(2)/log(3)>1/2. Choose epsilon<beta-1/2; eventually both prefix densities would exceed1/2, although their pointwise sum is exactly1. Contradiction. This does not decide which inverse is irrational.

**Application and retained failed route.** The square-zero word's complement has ones only at squares, hence density0 and no eventual period. Its inverse is irrational by the lower-density bound. The original square-zero word has density1 and remains unresolved. Inferring its irrationality by applying rationality preservation under complementation is not licensed. No example of a rational divergent point is claimed; lack of a proven preservation theorem is a limitation, not a demonstrated counterexample to preservation.

**Primary-source audit.** [Monks and Yazinski, author version of The Autoconjugacy of the 3x+1 Function](https://monks.scranton.edu/files/pubs/AutoConjV13.pdf), published2004: definition of Omega and Theorem2.1, pages2–3; Theorem2.7(b), page6; relevant proofs pages8–12. The lower-density theorem applies to divergent odd-denominator rational orbits. Their Theorem2.1 equates rationality preservation by Omega with rational-orbit periodicity. These statements/proof portions were read; other results and the entire paper were not independently audited. This resolves the previous publisher-access limitation and replaces the secondary-only attribution for this density bound.

**Controls/ unexpected check.** CM1 passed256 finite residues/8320 bits; CM2 passed two complementary rational examples through128 bits. Unexpected CM3 confirms0 and-1 are complementary rational fixed points, refuting the overbroad statement without “not eventually periodic”. Finite residue and example checks do not establish global rationality preservation. The proof above supplies the infinite conclusion.

**Next boundary.** Square-zero irrationality needs a point-specific argument or another known criterion; assuming global complement preservation would assume a central open conjecture. Do not queue that assumption as a lemma.


## G37. The subcritical gap ladder survives the height-budget filter (2026-10-06)

**Preregistration.** For zeros z_0=1,z_next=ceil(3z/2), audit Q_k=2^z_next/3^(z_k-k), the necessary G35 starting-height/correction budget at each gap. Predict Q_k tends to0 and has a finite maximum, so this filter alone cannot exclude the word. This does not predict rational realization. SB1: compute exact budgets for32 gaps; certify global tail decrease once gap>=32 using36*8^32<9^32 and the rounded recurrence. Unexpected SB2: pick D=1 and N=ceil(max Q)-1. Its initial height passes every bare budget, but direct parity iteration is predicted to disagree with the word. Counterfactual: passing every height budget suffices for parity realization. Reuse passed startup checks.


### G37 outcome: a certified limitation, not a rational realization

For z_0=1,z_next=ceil(3z/2), there are K_i=k+1 zeros before i=z_k+1. G35's necessary budget is H_0+D*E_i>=Q_k, with Q_k=2^z_next/3^(z_k-k). Set Delta_k=z_next-z_k. Direct division gives

    Q_(k+1)/Q_k = 2^Delta_(k+1)/3^(Delta_k-1).

The rounded recurrence implies Delta_(k+1)<=3*Delta_k/2+1, so the squared ratio is at most36*(8/9)^Delta_k. The gaps grow and, once Delta_k>=32, this is uniformly below1 because36*8^32<9^32. Thus the entire remaining budget tail decreases geometrically to0. This is an infinite tail certificate, not an extrapolation from32 samples.

The global maximum is at k8,z8=41, next zero62:

    max Q_k = 4611686018427387904 / 5559060566555523 < 830.

Consequently choosing H_0=830 satisfies every bare target-word budget H_0>=Q_k, and hence every necessary H_0+D*E_i>=Q_k because E_i>=0. But the ordinary integer start829 has H_0=830,D=1 and its actual parity word first differs from the target at index3. These are formal necessary budgets computed from the prescribed word; they do not make that word the start's actual parity sequence. This explicitly rejects sufficiency of budget satisfaction. It neither supplies a rational realization nor proves that none exists.

SB1 computed32 budgets and checked the exact recurrence/ratio; the uniform tail argument starts at gap index10 and establishes the global maximum. Unexpected SB2 verified the index3 mismatch through an independent direct iterate. No floating-point powers or rounding were used.

**Method boundary.** The3/2-spacing word remains an aperiodic density1 candidate outside this exclusion filter, like the square-zero word. More generally, spacing factor c<log2(3) makes log2(Q_k)=(c-log2(3))*z_k+O(k), tending to minus infinity for geometrically growing z_k. Even-step accounting improves the critical boundary, but cannot force these subcritical budgets to diverge. A different inverse constraint is needed. Prior art is the same established growth/parity mechanism recorded in G34–G36; no novelty claim.


## G38. Exact carry/Fourier recursion for coefficient-admissible vectors (2026-10-06)

**Preregistration.** At length m, a parity vector is coefficient-admissible if3^a_t>2^t for every1<=t<=m. Its unique representative r in[0,2^m) has a odd steps and q=T^m(r). Predict the child lift r'=r+epsilon*2^m, epsilon=(b-q) modulo2, a'=a+b and q'=(3^b*(q+epsilon*3^a)+b)/2. Admission of the child additionally requires3^a'>2^(m+1). The desired upper-half terminal state is y=3^a+q.

FR1: exact histogram recursion versus direct residue iteration at lengths0..8, target moduli2,4,8,16, retaining doubled parent moduli. FR2: the corresponding parity-split Fourier identity at every nonempty node/harmonic, absolute tolerance1e-9 only for complex summation. Counterfactual: parent histogram moduloM alone determines the child histogram moduloM. Unexpected FR3: find a same-a pair of actually admissible parent terminal values aliasing moduloM but giving distinct admitted children moduloM. Check whether Fourier triangle coefficients give a strict contraction; no decay bound predicted. Single-party controls. Bears on PERIOD-TWO.md7 question9, the shared survivor-count target. Reuse passed startup checks.


**G38 analytic checkpoint / additional prediction before its control.** FR1/FR2 passed36 histogram/720 Fourier checks; actual alias at m5,a4,M4,b0: representatives7/15 give q20/40 and children2/0 modulo4. The dyadic state needs an extra carry bit. Analytically, that carry disappears modulo3^a': q' is the least residue of(3^b*q+b)/2 modulo3^a', since2 is invertible there and the lift adds epsilon*3^a'. Preregister FR4: verify this formula and0<=q'<3^a' on all admitted children of brute parents at m0..7. This adds a controlled3-adic recursion, not a claimed cancellation estimate.


### G38 result: exact recursion exists; cancellation is still missing

Write mu_(m,a)(q) for coefficient-admissible parity-prefix counts with a odd steps and terminal q. **Bears on PERIOD-TWO.md §7 question9:** supplies the exact operator for the Collatz count twin's exponential sums. These are coefficient survivors; actual stopping-time survival is a separate ensemble, even where earlier measurements matched them.

**Carry derivation.** A length-m representative r lifts to r+epsilon*2^m. The affine parity formula increases its terminal state by epsilon*3^a. To prescribe next parity b, choose epsilon=(b-q) modulo2. Then

    a'=a+b, q'=(3^b*(q+epsilon*3^a)+b)/2.

Keep the child only if3^a'>2^(m+1). This enumerates the parity tree exactly. To compute children moduloM, parent residues modulo2M suffice. ModuloM alone fails: at m5,a4, representatives7 and15 have q20 and40, equal modulo4, but admitted b0 children have residues2 and0 modulo4. This is an actual admissible-pair witness, not an arbitrary toy state. The target upper-half state is y=3^a+q, so multiply each fixed-a Fourier contribution by its corresponding phase.

**Dyadic Fourier form.** Let F_(m,a)(h;L)=sum_q mu_(m,a)(q)*exp(2*pi*i*h*q/L). For one admitted parent/branch, set theta=exp(2*pi*i*h*3^a'/(2M)). Its child transform moduloM is

    exp(2*pi*i*h*b/(2M)) * [
      (1+theta)/2 * F_(m,a)(h*3^b;2M)
      + (-1)^b*(1-theta)/2 * F_(m,a)(h*3^b+M;2M)].

Split parent q into even/odd classes to prove this identity; the alternating character introduces frequency M. Sum the admitted b0/b1 terms from their appropriate parent odd-count classes. This is a modulus hierarchy, not a fixed-modulus scalar recurrence. Triangle coefficients do not force contraction: theta=i gives absolute coefficient sum sqrt(2)>1. This rejects that naive bound, not the possibility of cancellations between frequencies.

**Cleaner ternary formulation.** Every terminal q is the least residue in[0,3^a), by the existing least-residue lemma. Modulo3^a' the carry vanishes and

    q' = inverse(2 mod3^a')*(3^b*q+b) mod3^a'.

Its least representative is the actual integer q', so this is an exact ternary operator without a carry hierarchy. Define Gamma_(m,a)(h) as the Fourier sum modulo3^a, and u=inverse(2 mod3^a'). Then

    Gamma_(m+1,a')(h) = indicator(3^a'>2^(m+1)) * [
      Gamma_(m,a')(h*u)
      + exp(2*pi*i*h*u/3^a')*Gamma_(m,a'-1)(h*u)].

The second term is omitted for a'=0; frequencies in each Gamma are reduced modulo that parent's group. This follows directly from the two affine branches. The coefficients are unit phases; genuine decay needs correlation/cancellation control, not their absolute values.

**Comparison with prior art.** Read Definition1.7 and the displayed independent-geometric Syracuse recursion around Lemma1.12 in [Tao, arXiv:1909.03562v7](https://arxiv.org/html/1909.03562v7), not the whole proof. His random recursion uses independent geometric valuation increments on ternary groups. Here admissibility imposes the prefix barrier on(m,a), so the surviving path distribution is not that unconditioned iid law. The ternary recursion is an exact avenue for comparison; no transfer of his mixing theorem or new cancellation estimate has been proved. The affine/parity mechanism is already Terras/Bernstein in the record; no novelty claim.

**Single-party controls.** FR1 passed36 exact histograms against direct residue iteration at m0..8, final moduli2,4,8,16. FR2 passed720 dyadic Fourier identities, max complex residual2.8e-15 (tolerance1e-9; integer histograms exact). Unexpected FR3 supplied the concrete alias above. FR4 passed51 admitted ternary transitions. The operator identities are proved analytically; finite controls verify implementation, not an asymptotic Fourier bound or survivor-count theorem.

**Next:** study the ternary operator conditioned on the(m,a) survival barrier, and quantify how that conditioning changes the unconditioned renewal argument. The shared count target remains open.


## G39. Endpoint-conditioned survival: a polynomial event cost, no automatic Fourier transfer (2026-10-06)

**Preregistration.** Fix length T>=1 and odd count a with3^a>2^T. Uniformly sample words with that count; E means every nonempty prefix satisfies3^a_t>2^t. Predict P(E)>=1/T by rotating at the unique minimum of logarithmic partial sums, including nonprimitive words. SC1: exhaust all words throughT=12, compare barrier counts with an independent integer dynamic program and verify every positive-total rotation class contains an admissible word. SC2: check T*A(T,a)>=binomial(T,a). Unexpected SC3: repeated110 and all-one words test the short-orbit case. Counterfactual SC4: small conditioning cost transfers small complex-character expectation; a two-point cancellation example is predicted to refute this. Exact integer barriers; no floating-point admissibility. Single-party controls. Bears on PERIOD-TWO.md §7 question9, the shared count twin, through the conditioning boundary in G38. Reuse passed startup checks; Local retains Rule30 runs.


### G39 theorem and proof: fixed-endpoint event transfer

Fix integers T>=1 and0<=a<=T with3^a>2^T. Let U be the uniform law on binary words of lengthT with a ones. Let E require3^a_t>2^t at every nonempty prefix. If A(T,a) counts E, then

    binomial(T,a)/T <= A(T,a) <= binomial(T,a).

**Proof.** For a word w, put S_j=a_j*log(3)-j*log(2), for0<=j<=T. Distinct partial sums cannot coincide: equality would give3^d=2^e with a nonzero integer time difference e, contrary to unique prime factorisation. Choose the unique minimum S_k among S_0,...,S_(T-1). Rotate w to start just after indexk. Before wrapping, every new nonempty partial sum is S_j-S_k>0, including j=T since S_T>0 and S_k<=0. After wrapping it is S_T+S_j-S_k>0. Hence each rotation class contains an admissible word. Every class has at mostT members, even when the word is nonprimitive. Thus the number of classes is at least binomial(T,a)/T and A is at least that number. The upper bound is immediate.

Consequently, for any event B and nonnegative function f on this finite population,

    U(B | E) <= T*U(B),
    expectation_U(f | E) <= T*expectation_U(f).

This follows by dropping the E indicator from the numerator and using U(E)>=1/T. It is a fixed-endpoint comparison, not a bound on the probability of that endpoint under a different law. It applies equally to any iid Bernoulli law after conditioning on its endpoint count, because that conditional law is uniform. It concerns coefficient admissibility, not actual stopping-time survival.

**Cancellation boundary.** On the uniform group Z/2, the nontrivial character has values+1,-1 and expectation0. Conditioning on the +1 point costs just2, but leaves character expectation1. Therefore the event bound cannot imply an analogous bound multiplying the absolute unconditioned complex expectation. This counterexample rejects a general transfer principle, not a possible special estimate for Collatz. Exponentially rare events at fixed endpoints retain their exponential rate after the polynomial factorT; exponentially small Fourier expectations need additional control of their correlation with E.

**Exact next operator.** Fix terminal(T,a). Let h(t,s) count admissible completions after an already-admissible prefix with t bits and s ones. Terminal values are h(T,s)=1 if s=a, otherwise0; impossible states have0. Backwards, h(t,s) is the sum of h(t+1,s+b) over b=0,1 for which3^(s+b)>2^(t+1). Whenever h(t,s)>0, the uniform endpoint-surviving next-bit probability is h(t+1,s+b)/h(t,s) for an admitted child, and0 otherwise. This is proved by partitioning completions by their next bit. These weights depend on(t,s), not on the terminal residue q, although q and the path are correlated. Substituting these weights into G38's deterministic residue update gives the conditioned operator exactly; the weights need not be iid. No decay estimate follows merely from writing this operator.

**Outcome and scope.** SC1 passed1767 positive-total words in181 rotation classes and independent DP counts throughT12; SC2 passed35 endpoint count inequalities. Unexpected SC3 includes all-one and repeated110 short rotation orbits. SC4 refutes complex-cancellation transfer. Integer checks are exact and single-party. The analytic argument establishes the all-length count comparison; controls only audit its implementation. Prior-art mechanism: classical cyclic-minimum path rotation, no novelty asserted. Tao's unconditioned geometric-valuation law in G38 is a different population; this result does not transfer his mixing estimate. Shared survivor-count/Fourier decay remains open. Next useful target: bound the conditioned operator using the completion weights, rather than substituting the iid law.


## G40. Adjacent-pair skeletons give an exact conditioned cancellation product (2026-10-06)

**Preregistration.** Pair positions(0,1),(2,3),... and leave an odd final bit fixed. A skeleton records00,11 or mixed M for each pair. At a mixed pair starting at(t,s), both01 and10 should be admissible exactly when3^s>2^(t+1), provided the skeleton endpoints survive. Otherwise only10 can survive. Predict the endpoint ternary residue difference for changing10 to01 is Delta=3^(a-s-1)*2^(-(T-t)) modulo3^a. Since each mixed pair has one odd step, this difference should be independent of other orientations. Hence each surviving skeleton's normalized Fourier modulus equals the product of absolute cosines from its free mixed pairs. PC1: exhaustT<=10, compare skeleton cubes, residue differences and complex products against independent direct parity representatives; tolerance1e-9 for complex arithmetic, integers exact. Unexpected PC2: the all-one endpoint has unit Fourier modulus at every frequency, refuting a contraction uniform across all endpoints. Counterfactual: a positive number of surviving paths alone forces cancellation. Bears on PERIOD-TWO.md §7 question9; reuse startup checks, no Rule30 run.


### G40 theorem and proof: the skeleton phase product

Fix lengthT and endpoint odd count a with3^a>2^T. Partition the coefficient-admissible words into skeletons by recording each adjacent pair as00,11 or mixed, retaining an odd final bit separately. Discard skeletons with no survivors. A skeleton fixes the odd count s at the start t of every pair, and all pair-end coefficient ratios.

For a mixed pair let R=3^s/2^t. Orientation10 has intermediate ratio3R/2 and final ratio3R/4; orientation01 has intermediate ratioR/2 and the same final ratio. Thus, in a surviving skeleton,10 is always allowed;01 is allowed exactly whenR>2. Other prefixes are unchanged by a swap. Therefore the surviving orientations form a full independent binary cube on the free mixed pairs with3^s>2^(t+1); all other mixed pairs are forced10. In particular a skeleton with F free pairs contains exactly2^F words.

Let q(w) be the terminal iterate of the unique representative in[0,2^T), reduced moduloM=3^a. G38's carry-free ternary map applies. Modulo an odd power of3, a local10 composition sends x to(3x+1)/4;01 sends x to(3x+2)/4. Their difference is1/4. The following suffix has lengthT-t-2 and c=a-s-1 odd steps, so its slope is3^c/2^(T-t-2). Hence the final difference is

    Delta_t = 3^(a-s-1)*2^(-(T-t)) modulo3^a.

Negative powers mean multiplicative inverses modulo the odd modulus. The suffix slope depends only on its count, not its other orientations. The differences are therefore additive across all free pairs. If w0 has every mixed pair oriented10, then

    q(w) = q(w0) + sum_t eta_t*Delta_t moduloM,

where eta_t=1 for a free pair oriented01 and0 for10. Uniform sampling in this skeleton makes the eta_t independent fair bits. With e(x)=exp(2*pi*i*x), its normalized Fourier coefficient is exactly

    phi_S(h) = e(h*q(w0)/M) * product_t (1+e(h*Delta_t/M))/2.

Thus its modulus is the product of |cos(pi*h*Delta_t/M)|. This is an identity for the survival-conditioned population inside each skeleton, not an iid assumption on the whole path.

**Aggregate boundary.** If A is the total survivor count and S ranges over surviving skeletons at this endpoint, then

    |phi(h)| <= sum_S (2^F(S)/A)*product_free_t |cos(pi*h*Delta_t/M)|.

This follows by partitioning the uniform population and applying the triangle inequality only between skeletons; cancellation within each cube is retained exactly. For h coprime to3 every free pair gives a strictly smaller than1 factor, since Delta_t has3-adic valuation a-s-1<a. There is no uniform gap from1 as the denominator grows. At a=T the sole all-one word has no free pairs and unit Fourier modulus. This does not preclude decay for an aggregate with other endpoint weights; it does preclude a contraction asserted uniformly at every endpoint. A decay theorem still needs quantitative frequency control and mass bounds for the surviving skeletons.

**Outcome.** PC1 passed71 skeleton cubes,208 exact flips and563 Fourier identities throughT10; maximum complex residual6.33e-16 against tolerance1e-9. Direct integer residue iteration supplies an independent control for the modular pair calculation. Unexpected PC2 confirms unit modulus for the all-one endpoints throughT10; the analytic single-word argument proves this for everyT. Single-party controls, no asymptotic decay or count theorem inferred. The affine modular mechanism is the established parity machinery recorded in G38; the independence here is proved by the explicit survival barrier, not borrowed from Tao's renewal law. Next useful target is the weighted skeleton product above.


## G41. Free-pair mass away from the critical and all-one endpoints (2026-10-06)

**Preregistration.** Continue G40: for fixed endpoint density p=a/T strictly above beta=log(2)/log(3) and bounded away from1, predict that all but an arbitrarily polynomially small survivor mass has linearly many free mixed pairs after a logarithmic prefix. Compare the uniform endpoint law to iid Bernoulli(p) using its endpoint mass>=1/(T+1), then apply G39's factorT. Predict elementary exponential-moment bounds for visits below the incoming-ratio2 threshold and for few mixed pairs. FM1: throughT12 compare exact iid binomial endpoint mass to1/(T+1), and exact surviving late-free-pair counts to the two exceptional-event counts. Unexpected FM2: endpoint a=T has zero mixed pairs; the away-from1 hypothesis is essential. Counterfactual: many free pairs alone gives uniform Fourier contraction; construct a modular harmonic where all swap phases vanish for a restricted skeleton. Analytical proof supplies all-length scope; finite controls only test event containment/counting. Reuse startup checks, no Local job. Bears on PERIOD-TWO.md §7 question9.


### G41 theorem and proof: linearly many free pairs at interior endpoints

Put beta=log(2)/log(3). Fix epsilon>0 such that[beta+epsilon,1-epsilon] is nonempty. For any fixed endpoint p=a/T in this interval, sample uniformly from the coefficient-admissible words. For every B>0 there is K depending only on epsilon and B such that, outside probability O(T^(-B)), this word has linearly many free mixed pairs starting after L=ceil(K*log(T)). The statement is asymptotic for sufficiently largeT; constants do not depend on a. It asserts abundance of G40's free choices, not separation of their phases.

**Proof.** Let V be iid Bernoulli(p) on lengthT words, U its law conditional on endpoint count a, and U_E the law after also imposing prefix survival E. The binomial endpoint a is a mode of V's count distribution: the ratio of masses at k+1 and k is (T-k)*p/((k+1)*(1-p)), decreases with k, exceeds1 at k=a-1, and is below1 at k=a. Since there are T+1 possible counts, V(S_T=a)>=1/(T+1). Therefore for every event D, G39 gives

    U_E(D) <= T*U(D) <= T*(T+1)*V(D).

Choose lambda>0 sufficiently small that

    rho = exp(lambda*beta)*(1-(beta+epsilon)+(beta+epsilon)*exp(-lambda)) < 1.

Such a choice exists because the expression equals1 at lambda0 and has derivative-epsilon there. For p>=beta+epsilon the analogous moment is no larger. A low incoming ratio at time t means3^S_t<=2^(t+1), hence S_t<=beta*(t+1). The exponential Markov inequality yields

    V(S_t<=beta*(t+1)) <= exp(lambda*beta)*rho^t.

Indeed apply Markov to exp(-lambda*S_t) and use independence to evaluate its expectation as(1-p+p*exp(-lambda))^t. Union over t>=L bounds any such late visit by C*rho^L, where C=exp(lambda*beta)/(1-rho). This includes all late pair starts.

There are n=floor(T/2)-ceil(L/2) disjoint pairs starting at even t>=L. Under V their mixed indicators are independent with probability u=2p(1-p). Throughout the specified interval u>=u0=2epsilon*(1-epsilon)>0. Put kappa=u0/2 and choose theta>0 sufficiently small that

    sigma = exp(theta*kappa)*(1-u0+u0*exp(-theta)) < 1.

Again the derivative at0 is kappa-u0<0. Exponential Markov on their mixed count M gives V(M<=kappa*n)<=sigma^n. If no late low-ratio visit occurs, G40 makes every late mixed pair free, so its free count F equals M. Consequently

    U_E(F<=kappa*n) <= T*(T+1)*(C*rho^L+sigma^n).

Choose K>(B+2)/(-log(rho)). With L=ceil(K*log(T)), n=T/2-O(log(T)), the displayed bound is O(T^(-B)); the second term is exponentially small. This proves the uniform statement. No independence is assumed under U_E: all independence is used under V and transferred through the two explicitly bounded conditioning costs.

**Frequency boundary.** A concrete length12 skeleton begins1111, has three mixed pairs, and ends11. Every orientation of the three mixed pairs survives, so it has8 words and a=9. Their free-pair starting odd counts are s=4,5,6. G40's differences have3-adic valuations4,3,2 respectively. At the nonzero harmonic h=3^7 modulo3^9, all three h*Delta vanish. The entire cube has a constant character and unit Fourier modulus. This is a divisible-by3 frequency control; it does not contradict G40's strict contraction for unit harmonics. The all-one endpoint separately shows why the hypothesis p<=1-epsilon is necessary. Free-pair mass alone does not supply the frequency-sensitive separation needed in G40's aggregate bound.

**Outcome and next target.** FM1 passed90 exact binomial endpoint-mode inequalities and1684 event-containment/conditioning controls throughT12. Unexpected FM2 confirms the all-one exception and the8-word frequency-blind cube using direct integer parity representatives. Single-party implementation checks; the argument above supplies the all-length theorem. The elementary exponential-moment proof is given in full; no new concentration theorem or novelty asserted. It does not cover endpoint densities approaching beta or1, and does not identify the endpoint weighting of the shared count target. The next obstruction is frequency-sensitive phase separation, rather than scarcity of free pairs in this interior regime.


## G42. A unit-frequency resonance with linearly many free pairs (2026-10-06)

**Preregistration.** For any parity word with endpoint(T,a), predict harmonic h=2^T modulo3^a has character e(F_T), where F_T=sum_odd_j 2^j/3^S_(j+1), the G32 real inverse partial sum. In G40's pair formula the free-pair phase becomes2^t/3^(s+1) modulo1. Test the skeleton1111 followed by n pairs-of-pairs(11,M), n>=0: T=4+4n,a=4+3n, n free pairs and phase sizes(64/2187)*(16/27)^k. Predict its normalized Fourier modulus is greater than0.99 for all n, certified by cos(pi*x)>=1-5x^2 and an exact geometric-square bound. UR1: direct residue controls throughT12 for the resonance identity; UR2: skeleton orientations throughn3 against the exact product. Unexpected UR3: h is coprime to3 and nonzero despite the weak cancellation; contrast with G41's divisible harmonic. Counterfactual: a linear free-pair count forces decay uniformly at all unit frequencies. This concerns one explicit skeleton family, not its mass in the full population. Reuse startup checks. Bears on PERIOD-TWO.md §7 question9.


### G42 theorem and proof: primitive characters can remain resonant

For any parity word of lengthT with a odd steps, write its representative as r in[0,2^T) and terminal value as q. The affine iteration identity is

    2^T*q = 3^a*r + sum_odd_j 2^j*3^(a-S_(j+1)).

Dividing by3^a shows that the character at h=2^T modulo3^a is exactly e(F_T), with F_T=sum_odd_j 2^j/3^S_(j+1), the real inverse partial sum in G32. Here e(x)=exp(2*pi*i*x). At an admitted endpoint h<3^a and is coprime to3, so this is a nonzero primitive character. Multiplying G40's swap difference by h gives phase

    h*Delta_t/3^a = 2^t/3^(s+1) modulo1.

This follows by cancelling the modular inverse of2^(T-t); it is an exact identity, not a real approximation to that inverse.

**Explicit family.** Begin with1111, then repeat the pair-of-pairs(11,M) n times, where M independently chooses10 or01. The skeleton has T=4+4n, a=4+3n and n mixed pairs. Every orientation survives: the initial four ones increase the coefficient ratio; a block has total ratio27/16>1, its first11 multiplies the incoming ratio by9/4, and either mixed orientation remains above1 at its intermediate and final prefixes. In particular every mixed pair is free in G40's sense. There are exactly2^n words.

The kth mixed pair, starting with k=0, has t=6+4k and s=6+3k. Its resonant phase is

    x_k = (64/2187)*(16/27)^k.

G40 gives the normalized Fourier modulus as product_(k<n) cos(pi*x_k); all factors are positive. The elementary inequality cos(u)>=1-u^2/2 and pi^2<10 imply cos(pi*x_k)>=1-5*x_k^2. For nonnegative d_k<=1, induction gives product(1-d_k)>=1-sum(d_k). The full infinite geometric sum satisfies the exact rational inequality

    5*sum_(k>=0) x_k^2 = 20480/3103353 < 1/100.

Therefore the modulus is greater than0.99 for every n. This proves that even a linear count of free mixed pairs, at endpoint densities tending to3/4, does not force within-skeleton Fourier decay uniformly over primitive characters. Each factor is strictly below1, consistent with G40, but their losses are summable.

**Scope.** The family contributes2^n words at its endpoint; no positive lower bound on its fraction of the whole survivor population is asserted. Other skeletons may cancel its contribution or dominate its mass. Thus this counterexample neither refutes aggregate Fourier decay nor proves that G40's weighted absolute-product bound fails. It identifies the missing frequency-sensitive condition. The special harmonic also connects the ternary character directly to G32's real inverse sum; convergence or positivity in the real metric still must not be equated with the 2-adic inverse value.

**Outcome.** UR1 passed507 exact direct-residue/inverse-sum identities throughT12. UR2 passed4 cubes/15 orientations throughn3 against G40's product, max complex residual1.11e-16 against1e-9 tolerance. The exact geometric-square inequality certifies every remaining n, not merely the tested15 words. Unexpected UR3 verifies nonzero unit harmonics; unlike G41, no divisible-frequency loophole is involved. Single-party implementation controls and a complete analytic family proof, awaiting second reader. Established affine/parity identities underlie the construction; no novelty or prize claim. Next: quantify the relevant frequency range before extending the cancellation route; avoid asking free-pair counts to supply phase separation they cannot give.


## G43. Binary parity reads ternary Fourier coefficients with unequal weights (2026-10-06)

**Preregistration.** Audit the exact frequency demand of COLLATZ-PRIZE.md §4. For odd M=3^a and f(q)=(-1)^q on its least representatives, predict normalized Fourier coefficient hat f(h)=2/[M*(1+e(-h/M))], with h moduloM. Its magnitude is1/[M*|cos(pi*h/M)|]: the next-bit reader strongly weights frequencies nearM/2, while G42's harmonic h=2^T has weight<=2/M on its explicit family. BF1: check all coefficients/inversion for a1..5 by direct sums, complex tolerance1e-9. BF2: check parity expectation for actual surviving terminal histograms throughT8 using weighted Fourier reconstruction. Unexpected BF3: uniform residues on an odd ternary group have parity imbalance1/M; a zero baseline would be wrong. Counterfactual: all nonzero unit frequencies have equal importance for the next binary bit. Optional exact generalization: a binary residue cylinder moduloB=2^d has a truncated geometric Fourier sum. No claim that one-step expectation proves the full tail count. Reuse startup checks; Local L007 argument audit read. Bears on PERIOD-TWO.md §7 question9.


### G43 theorem and proof: exact ternary spectrum of a binary reader

Let M=3^a with a>=1, and interpret q moduloM by its least representative0<=q<M. Set f(q)=(-1)^q and e(x)=exp(2*pi*i*x). For0<=h<M define hat f(h)=M^(-1)*sum_q f(q)*e(-h*q/M). A geometric sum with ratio-e(-h/M) gives

    hat f(h) = 2/[M*(1+e(-h/M))],
    |hat f(h)| = 1/[M*|cos(pi*h/M)|].

The numerator is2 because M is odd and e(-h)=1. The denominator is nonzero for integer h on an odd group. In particular hat f(0)=1/M, not0. Fourier inversion gives, for any distribution of q with phi(h)=expectation e(h*q/M),

    expectation f(q) = sum_h hat f(h)*phi(h).

G38's upper-half state is y=M+q. Since M is odd, its next parity is odd exactly when q is even. Thus

    probability(y odd) = (1+sum_h hat f(h)*phi(h))/2.

This sum is real, although individual summands may be complex. Uniform ternary residues give probability(y odd)=(M+1)/(2M), including the finite1/(2M) bias.

**Which frequencies matter.** The weights peak near h=M/2, where |hat f((M-1)/2)|=1/[M*sin(pi/(2M))], tending to2/pi. If0<=h<=M/3, then |hat f(h)|<=2/M. In G42's family, M/h=(81/16)*(27/16)^n>3 at the resonant primitive harmonic h=2^T. Its contribution to the parity-reader sum therefore has magnitude at most2/M even though |phi(h)|>0.99. This is a within-family bound; it does not transfer that family's measure to the full population. It also does not refute the general relevance of primitive-frequency resonances to other test functions.

For completeness, writing d=|h-M/2| gives |hat f(h)|=1/[M*sin(pi*d/M)]<=1/(2d), using sin(x)>=2x/pi on[0,pi/2]. Sum over the half-integer distances to obtain sum_h|hat f(h)|<=3+log(M), with log natural. Indeed the paired distances give sum_(j=0)^((M-3)/2)1/(j+1/2) plus1/M, bounded by2+log(M)+1/M by integral comparison. Hence a bound |phi(h)|<=delta for all nonzero h implies

    |probability(y odd)-(M+1)/(2M)| <= delta*(3+log(M))/2.

This proves the logarithmic Fourier-weight assertion for one binary bit; it supplies no delta estimate itself. Frequency-specific estimates may instead be inserted into the exact weighted sum.

**Longer binary cylinders.** For B=2^d,0<=c<B, let g_c(q)=1 when q is congruent to c moduloB. Put L_c=max(0,1+floor((M-1-c)/B)). Its Fourier coefficient is the exact finite sum

    hat g_c(h) = e(-h*c/M)/M * sum_(j=0)^(L_c-1) e(-h*B*j/M).

The empty sum is0; at h=0 the value is L_c/M. A nonzero-frequency sum is the usual geometric quotient. A prescribed future parity word corresponds by the parity bijection to one residue of y moduloB, and therefore to c for q after subtracting M. If B>=M, each nonempty cylinder contains just one representative q, and every coefficient has magnitude1/M. Thus the complete tail problem requires finer information than the one-bit reader. Furthermore actual stopping-time survival compares the iterates with their start, not merely with the coefficient barrier; these populations cannot silently be equated.

**Outcome.** BF1 passed363 direct spectrum checks and363 inversions for a1..5. BF2 reconstructed17 actual coefficient-survivor histograms throughT8, max complex residual3.82e-13 versus1e-9 tolerance. Unexpected BF3 verifies the exact odd-modulus parity bias and unequal unit-frequency weights.33 finite family-weight checks support the all-n geometric-ratio proof. Single-party controls; proof pending second reader. Elementary finite Fourier inversion/geometric sums, no novelty claim. The general cylinder identity is derived analytically; no multi-step survival bound or transfer of Tao's mixing law is claimed. This narrows the next target to the reader's weighted frequencies and the tail's changing resolution.


## G44. Exact finite-ensemble information budget for parity tails (2026-10-06)

**Preregistration.** Continue G43's cylinders: for uniform q in[0,M), y=M+q and B=2^d, predict the future d-parity distribution has total variation from uniform B words equal r*(B-r)/(B*M), where r=M moduloB. Once B>=M it is1-M/B, and the parity words identify q exactly; for arbitrary q distributions their entropy then equals the initial entropy. Predict no constant relative-error comparison to fair coins can hold simultaneously for all cylinders and unbounded d: a fixed q's actual parity prefixes retain probability1/M once B>=M. This does not refute the special stopping-time event count. IB1: M=3^a,a1..5, d1..9, direct iterates versus the exact rational TV/count formula and injectivity; no floating-point entropy test. Unexpected IB2: compare the word from q=0,y=M at d12 and d16; observed cylinder mass1/M, not2^-d. Counterfactual: small one-bit Fourier error guarantees joint near-uniformity indefinitely. Reuse startup checks. Bears on PERIOD-TWO.md §7 question9 and the Local L008 channel comparison.


### G44 theorem and proof: resolution of a finite residue ensemble

Fix odd M=3^a, a>=1. Let q be uniform on the least representatives0,...,M-1 and y=M+q. For d>=1 put B=2^d. The parity bijection identifies the first d parities of y with y moduloB, through a permutation of the B labels. Therefore its total variation distance from uniform d-bit words equals the variation distance of y moduloB from uniform residues moduloB.

Write M=kB+r with0<=r<B. In any M consecutive integers exactly r residue classes occur k+1 times and the others k times. Hence the variation distance is exactly

    TV = r*(B-r)/(B*M).

Indeed the r excess masses have difference(k+1)/M-1/B=(B-r)/(B*M), and the remaining deficit masses have difference1/B-k/M=r/(B*M); their summed absolute differences divided by2 give the displayed value. It follows that TV<=B/(4M). When B>=M the same formula becomesTV=1-M/B. Thus the approximation improves for coarse binary resolution, but becomes sparse when the requested word population greatly exceeds the initial residue population.

**Information statement.** When B>=M, distinct q give distinct y moduloB, and hence distinct d-parity words. The map is then injective on the entire initial ensemble. For any distribution of q, the Shannon entropy of these words equals H(q); for all d it is at most H(q)<=log2(M), because the words are a deterministic function of q. Uniform q gives entropy exactlylog2(M) once B>=M. This is a finite initial ensemble; it does not make the integer Collatz dynamics an autonomous finite-state system.

More generally, if the q law has support sizeN<=M, its word law has support at mostN and TV from uniform B words is at least1-N/B. Choose that support as the test event: its actual probability is1 and its uniform probability is at mostN/B. For a law uniform on N distinct q and B>=M, the distance is exactly1-N/B and entropylog2(N). Actual endpoint ensembles may have nonuniform terminal-q weights, so they must use their own support and law; uniformity on all M residues is an explicitly idealized comparison.

**Retained counterexample to an overstrong route.** Fix q0 and consider the actual d-parity prefix of y0=M+q0 at each d. For uniform q, once B>=M this cylinder has probability1/M. Its fair-coin probability is2^(-d). Their ratio is2^d/M and is unbounded with d. Thus no constant C can bound every cylinder's probability by C times its coin probability for arbitrarily long tails. No assumption about eventual behaviour of y0 is needed: every integer orbit has finite prefixes. The example refutes only a simultaneous all-cylinder comparison. It neither refutes the specially constrained stopping-time count in COLLATZ-PRIZE.md §1 nor predicts a divergent orbit. That target concerns a selected union of words whose paths stay above their start; some such events may become empty.

**Outcome and synthesis.** IB1 passed45 exact rational variation/parity-bijection controls, including24 injective ensembles for a1..5,d1..9. Unexpected IB2 checked10 actual-prefix cylinders at d12,d16: mass1/M, not2^(-d). All comparisons use direct iterates and integer/rational arithmetic. The all-length statement follows from the proof, not those finite cases; single-party controls pending second reader. This uses the known parity bijection and elementary finite counting/information identities, with no novelty claim.

G38–G44 now identify the operator, survival conditioning cost, free-pair cubes, their interior mass, a primitive resonance, the binary reader weights and the finite-resolution boundary. These are useful exact structure, not a tail-count proof. The next task must exploit the specific surviving-word set and its actual-start threshold; asking for uniform control over all binary cylinders is an invalid strengthening. Local's L008 channel analogy is useful at this precise level: deterministic reads can reveal an initial ensemble's information, while further exclusions require structure of the admissible target. G39–G43 have independent argument audits from Local (L007/L008); G44 is new.


## G45. Word-specific actual-start survival ceilings (2026-10-06)

**Preregistration and pending checkpoint.** Derive the exact realizing residue and ceiling below. AS1 predicts the word-by-word count agrees with independent direct starts of widths1..8 for horizons1..12. AS2 checks that any actual survivor absent from the coefficient population lies below its word's finite ceiling. Unexpected AS3: the1,2 cycle at start1 refutes universal equality of the two survival notions; word1010 should have ceiling1 and residue1 modulo16. Counterfactual: actual and coefficient survival agree for all positive starts. Predictions and control script are published in this tick; numerical controls are intentionally NOT RUN until the next tick, following the one-commit/one-push network rule. Startup checks reused. Bears on PERIOD-TWO.md §7 question9 and COLLATZ-PRIZE.md §1.

### G45 theorem and proof: actual-start survival is a residue class cut by a ceiling

Fix a binary parity word w of lengthT>=1. Let a_t count its ones in the first t positions and define B_0=0. Reading the bit b at positiont, update

    B_(t+1)=3^b*B_t+b*2^t.

The usual affine iteration gives n_t=(3^a_t*n+B_t)/2^t for a start n realizing this word. Its realizing starts form the residue class

    n = r_w modulo2^T,
    r_w = -B_T*(3^a_T)^(-1) modulo2^T.

This is the known parity bijection. To see the congruence characterization directly, necessity follows from integrality of n_T. Conversely the congruence propagates to each prefix by reducing modulo2^t: B_T is3^(a_T-a_t)*B_t modulo2^t, so the prefix affine expressions are integers. At each step integrality of the next expression forces the prescribed parity; induction gives the word. The inverse exists because3^a_T is odd.

Actual survival throughT means n_t>=n for every1<=t<=T. If3^a_t>2^t, this condition holds automatically for positive n, since B_t>=0. Equality is impossible for t>=1 by unique prime factorisation. At a deficient prefix3^a_t<2^t, it is equivalent to

    n <= floor(B_t/(2^t-3^a_t)).

Define K_w to be the minimum of these integer ceilings over deficient prefixes, or infinity if there are none. Then the positive starts realizing w and surviving throughT are exactly

    n congruent to r_w modulo2^T, with1<=n<=K_w.

For w-bit starts put L=2^(w-1), U=min(2^w-1,K_w). The exact count for this word is0 if U<L, otherwise

    floor((U-r_w)/2^T)-floor((L-1-r_w)/2^T).

Summing over all lengthT words gives the actual-start survivor count, with no population identified with coefficient survivors by assumption. Words whose coefficient barrier survives have K_w=infinity. Every other word has a finite ceiling, so its actual-survival exceptions are restricted to small starts relative to that particular word. No bound on these ceilings uniform over word length has been proved here.

**Unexpected analytic scope check.** The word1010 has B_4=7,a_4=2 and deficient final coefficient9/16. Its ceiling is K=1 and its residue is1 modulo16. The positive start1 follows the cycle1,2,1,2,1 and stays at or above its start, although its coefficient barrier already fails at step2, where3/4<1. Thus the two notions are not universally equal. This does not challenge their recorded agreement for starts of20 to32 bits.

**What remains.** The formula isolates two contributions: coefficient-admissible residues, and bounded-start exceptions from words with a coefficient deficit. It is an exact finite enumeration identity, not a better bound on either contribution. Both depend on the specific words and realizing residue classes. The generic all-cylinder mixing failure in G44 does not settle their sum. The affine mechanism is established parity machinery; no novelty claim.


### G45 outcome (2026-10-06)

Published AS1-AS3 controls now run unchanged:65520 exact word/width counts agree at horizons1..12,widths1..8;11 actual-survivor occurrences with finite ceilings satisfy their ceilings. Unexpected AS3 confirms the start1/word1010 distinction. Integer/rational enumeration only; no uniform ceiling or summed survivor bound inferred. Local independently argument-audited G45 and checked168 aggregate cases throughwidth12/horizon14 (L012), so the analytic formula has a second reader.

## G46. Reply to L012: formal ceilings grow, and short residue intervals need rounding (2026-10-06)

**Analytic checkpoint and preregistration.** The proof below answers L012's O(1) question without a large census. New controls will run next tick after publication: KC1 exact ceilings and realizing residues of words1^k followed by zeros to the first coefficient deficit, k1..256; compare against G45's independent specification routine. KC2 retains the largest formal ceilings and checks whether their residue actually lies below them; no prediction of realization. Unexpected KC3: word1010 demonstrates the necessary +1 residue-count correction. Counterfactual: interval length times residue density is always an upper bound. New KC controls NOT RUN in this tick; only G45's previously published controls ran. Bears on PERIOD-TWO.md §7 question9.

### G46 theorem and proof: the formal ceilings are unbounded

For k>=1 take the word consisting of k ones followed by j-k zeros, where j is the unique integer with2^(j-1)<3^k<2^j. This is j=ceil(k*log2(3)). Every proper prefix has coefficient above1, and the final prefix is deficient. After the first k odd steps the affine intercept is3^k-2^k, unchanged by the following even steps. Thus G45's ceiling for this word is exactly

    K_k = floor((3^k-2^k)/(2^j-3^k)).

These ceilings are unbounded. Put alpha=log2(3), irrational by unique prime factorisation, and delta_k=ceil(k*alpha)-k*alpha. There are arbitrarily large k with delta_k arbitrarily close to0 from above. Here is an elementary one-sided approximation argument. Pigeonholing the fractional parts of0,alpha,...,N*alpha gives a positive q whose multiple is within1/N of an integer. If its fractional part is near1, q already works. Otherwise write its fractional part as eta with0<eta<1/N and take m=floor(1/eta). Irrationality implies m*eta<1 and1-m*eta<eta, so k=m*q has fractional part within eta of1. Taking N arbitrarily large produces delta_k tending to0. Such k must tend to infinity, because each fixed k has a nonzero gap.

The ratio inside the floor is

    (1-(2/3)^k)/(2^delta_k-1).

Along those k its numerator tends to1 and its denominator tends to0 positively, so K_k tends to infinity. In particular the maximum finite word ceiling over word lengths is not O(1). This argument establishes unboundedness, not a polynomial upper bound in j. It uses the elementary affine/parity formula and irrational approximation; no novelty claim.

**Residue-placement boundary.** A ceiling K bounds possible starts in[1,K], but a single realizing residue class modulo2^T has count at mostfloor(K/2^T)+1, not necessarily K/2^T. For word1010, T=4,K=1 and residue1, that count is1 whereas K/2^T=1/16. Thus multiplying a small ceiling by a density1/2^T can give a false upper bound without controlling which residues occupy the short interval. Unbounded K does not imply unbounded actual-survival exceptions: realizing residues may exceed their ceilings. Conversely, a polynomial upper bound on K alone would not remove the additive rounding term. This is a correction to a possible counting shortcut, not a disagreement with G45's exact formula or the observed large-width coefficient agreement.


### G46 outcome (2026-10-06)

KC1-KC3 now run unchanged after their publication:256 exact first-deficit ceilings agree with G45's specification. The five largest tested records(K,k,j) are(321,253,401),(191,200,317),(136,147,233),(106,94,149),(86,41,65). None has its realizing positive residue below its ceiling; their residue bit lengths are399,310,228,142,62. The largest formal ceiling therefore does not indicate a large realized exception. Unexpected KC3 confirms the short-interval rounding failure. These finite results make no polynomial bound claim. Local independently argument-audited G46 and checked its closed form throughk399 (L014).

## G47. A first-deficit single-run word can survive only by closing a cycle (2026-10-06)

**Analytic checkpoint / preregistration.** The criterion below explains residue placement in the G46 family. Next-tick RC1 will compare D divisibility with direct ceiling/residue membership for k1..256; predict the only realized start in this finite range is1, without asserting this for all k. RC2 checks actual trajectories for any candidates. Unexpected RC3: k1 gives the known positive cycle, refuting an overbroad claim that every coefficient-deficient word has no actual survivors. New RC controls NOT RUN before publication; only previously published KC controls ran this tick. No new lane or large census. Bears on PERIOD-TWO.md §7 question9.

### G47 theorem and proof: this first-deficit family realizes only by a return

Use G46's word1^k followed by j-k zeros, k>=1,j=ceil(k*log2(3)). Put D=2^j-3^k>0 and B=2^(j-k). Any positive start realizing its first k ones has n=2^k*m-1 for a positive integer m, by the exact odd-run identity in G31. After those k odd steps its value is3^k*m-1. Realizing the following j-k zeros requires

    3^k*m-1 = 0 moduloB,
    D*m = -1 moduloB.

The final value is n_j=(3^k*m-1)/B. Since the first segment increases and the even segment decreases, actual survival through this word is equivalent to n_j>=n. Direct subtraction gives

    n_j-n = (B-1-D*m)/B.

The positive integer D*m is congruent to B-1 moduloB, so D*m>=B-1. Survival requires the reverse inequality. Both hold exactly when D*m=B-1, making n_j=n. Therefore there is an actual surviving positive start for this word if and only if

    D divides B-1.

If so it is unique: m=(B-1)/D and n=2^k*m-1. Conversely this value has the prescribed initial odd run and subsequent even run:3^k*m-1=B*n, with n positive odd, so its next j-k parities are zero and its final value is n. All intermediate values are at least n. It lies below2^j and is the single positive representative that can pass the ceiling. Thus this is a genuine periodic return, not a divergent orbit.

At k=1,j=2,D=1,B=2 the criterion gives start1 and the known1,2 cycle. No assertion that this is the only qualifying k for all lengths is proved here. Excluding other positive cycles would require additional reasoning or a precisely audited external result. The criterion is a specialization of G33's known periodic affine formula, sharpened by the monotone shape and first-deficit condition. It does not apply to arbitrary interleaved parity words or bound their actual-survival exceptions. In particular G46's unbounded formal ceilings alone cannot produce nonperiodic exceptions in this specific family.


### G47 outcome (2026-10-06)

Published RC1-RC3 run unchanged:256 divisibility/realizing-residue comparisons pass. The finite candidate list is exactly(k1,j2,n1), and its trajectory returns to its start. Unexpected RC3 retains the positive cycle exception to an overbroad exclusion. No theorem excluding other k or general cycles follows.

## G48. Interleaved first-deficit gap census, preregistered (2026-10-06)

**Prediction and pending run.** Census all first-deficit words throughlength16, including interleaved odd/even runs. Predict no positive-start strict-survival exception in this finite population; the only realized first-deficit return should be word10,start1. FD1 compares the gap formula against direct iteration for each representative and its first two positive lifts. FD2 records all realized returns and strict overshoots without discarding failures of the prediction. Unexpected FD3 checks word0: its zero gap at residue0 is not a positive survivor. Counterfactual: every zero gap supplies a positive cycle, or G47's single-run argument applies unchanged to interleaved words. New FD controls NOT RUN before this publication; only previously published RC controls ran. The exact audit identity below clarifies what the census measures. Bears on PERIOD-TWO.md §7 question9; no large-width job duplicated.

### G48 audit identity: the first-deficit gap

For a first-deficit word of lengtht, all proper nonempty prefixes have coefficient above1 and the final coefficient A/2^t, A=3^a, is below1. Let D=2^t-A, let r be its realizing residue in[0,2^t), and q its terminal value. Set g=q-r, an integer. For a start n=r+2^t*m, the affine lift identity gives

    n_t-n = g-D*m.

Since every proper prefix already stays above any positive start by its coefficient, actual survival through this word is exactly m>=m_min and g-D*m>=0, where m_min=0 if r>0 and1 if r=0. Thus surviving positive lifts have m_min<=m<=floor(g/D). Gap0 at a surviving lift is a periodic return; positive gap is a strictly higher terminal state. A formal g=0 at r=0 does not supply a positive survivor, since m_min=1. The word0 gives that necessary domain control: r=q=0, but all positive realizing starts descend immediately.

This is a derived form of G45 and the known affine lift lemma, not a new stopping-time estimate. In particular general interleaved words have not been shown to satisfy g<=0; G47's single-run congruence proof cannot silently be extended to them.


### G48 outcome and primary-source scope audit (2026-10-06)

FD1-FD3 ran unchanged after publication:791 first-deficit words/2373 direct positive lifts pass; realized returns onlyword10,start1; strict overshoots empty. The finite prediction held. Unexpected FD3 rejects zero-residue gap0 as a positive survivor. Integer controls are single-party. The gap lemma lifts this finite word census to the finite-horizon certificate below; it does not lift horizon16 to all horizons.

**Prior art.** Read Definition1.2 and Lemma2.1/proof in [Rozier–Terracol, Paradoxical behavior in Collatz sequences, arXiv:2502.00948v2](https://arxiv.org/html/2502.00948v2). They identify Terras's coefficient-stopping-time equality for n>=2 and distinguish it from later paradoxical rises; their start7 example has already descended before rising again. Their adjacent01/10 offset comparison also precedes G40's affine swap mechanism. Our barrier-compatible cube calculation is a separate conditioning statement, without a novelty claim. This was a targeted reading, not a whole-paper or computational-proof audit. The publisher's original Terras PDF download failed; no claim to have read it. Larger existing verifications make a larger census alone a weak next step.

### G48 computed finite-horizon certificate

For every positive integer n>1 whose first coefficient deficit occurs by step16, actual stopping occurs at that same step. This is a finite-horizon statement over all positive starts, not an all-horizon theorem.

**Certificate and argument.** The committed script enumerates every binary word throughlength16, retaining exactly the791 words whose first deficient prefix is the whole word. Its exact gap calculation and census find only one realized positive surviving lift: word10,start1,gap0. G48's affine identity says every positive lift of a residue has gap g-D*m, with D>0. Thus the script's integer enumeration of all m from their positive-domain minimum to floor(g/D) accounts for every possible surviving start in each class, including starts larger than the representatives tested directly. There are no remaining positive survivors except1. Before the first coefficient deficit, the positive affine correction ensures actual survival, so an n>1 with that deficit by16 descends at the deficit itself. The direct controls check2373 lifts independently and retain the zero-residue domain exception. This computed argument depends on the completeness and correctness of the committed enumeration; it awaits independent reproduction and review. No novelty or prize claim.

**Next checkpoint.** Close the bounded census block. Read Cloud's proposed generality audit in PRIZE-PROBLEMS.md §8 before claiming any new lane; no automatic extension to longer first-deficit enumeration. The shared count target and all-horizon coefficient equality remain open.


## G49. Antihydra test-bed scope: coding transfers, stopping cost does not (2026-10-06)

**Preregistration.** Scope the map H(n)=floor(3n/2) before a substantial run. AH1: bijection, affine lift and terminal least-residue range for t0..10; independent direct division versus prescribed-branch algebra. AH2: source reduction H^j(8)=f^j(4)+4, f(n)=floor(3n/2)+2, through32 steps, with the parity counter tracked independently. AH3: exact counter-survival DP through128 steps versus brute words through10; predict its probability is always>=1-r, certified using rational x=1-p and x^2+x<=1, r=(sqrt(5)-1)/2. Unexpected AH4: growing seed3 hits counter-1 immediately, refuting “integer growth implies no halt”. New AH controls published but NOT RUN this tick. Bears on PRIZE-PROBLEMS.md §8's proposed test bed, not a solved prize or machine. No Local generality/ring job duplicated.

### G49 theorem and proof: floor(3n/2) preserves coding but changes survival

Let H(n)=floor(3n/2) on nonnegative integers. Write b=n modulo2. Then H(n)=(3n-b)/2. Every n>=2 strictly increases, since H(n)-n=floor(n/2)>=1;0 and1 are fixed. Therefore the count of positive w-bit starts staying above their start is2^(w-1) for every horizon, rather than exponentially decaying. This does not settle a parity-counter halting problem.

For a word b_0,...,b_(t-1), define C_0=0 and C_(j+1)=3*C_j+b_j*2^j. Then

    2^t*H^t(n) = 3^t*n-C_t.

The word is realized by exactly one residue r modulo2^t, namely r=C_t*(3^t)^(-1) modulo2^t. Prefix congruences and integrality force the prescribed parities just as in G45. Lifting a start by2^t*m adds3^t*m to its terminal value. For0<=r<2^t, nonnegativity and C_t>=0 give0<=H^t(r)<3^t. Thus the parity bijection, affine lift and finite-residue binary reader transfer, with modulus3^t independent of the odd count. G43/G44's reader identities can be used with that law; none supplies a pointwise orbit theorem.

**Actual test-bed event.** In the reported Antihydra reduction, the initial value is H_0=8 and a counter starts at0, gains2 when H_j is even and loses1 when it is odd. Writing a_t for the odd count, its value aftert steps is2t-3a_t. Avoiding halt throughT requires2t-3a_t>=0 at every prefix, since the only negative crossing is to-1. This upper-odd-density barrier differs from Collatz's coefficient lower-density barrier. Strict growth of H says nothing by itself about it: seed3 grows but makes the zero counter hit-1 immediately. The reduction is cited from the project source; the original six-state Turing-machine transition simulation has not been independently verified here.

**The fair-coin analogue does not have exponential survival decay.** Let iid bits drive counter increments+2 for0 and-1 for1. Put r=(sqrt(5)-1)/2, so r^2+r=1. For counter c>=0, h(c)=r^(c+1) obeys(h(c+2)+h(c-1))/2=h(c), and h(-1)=1. Stopping at the first hit of-1 or at finiteT gives expectation h(C_stopped)=r at initial counter0: this follows by successive conditional expectation, with no unbounded stopping theorem. On paths that hit, h=1; on other paths h>=0. Hence P(hit byT)<=r and P(surviveT)>=1-r>0 for everyT. No assumption about H^t(8)'s actual parity distribution is made. Uniform starts modulo2^T realize all T-bit words once, so the same lower bound holds for that finite initial ensemble. It does not determine the selected start8. Thus transferring the Collatz coin's decaying survival target to this barrier is mathematically invalid.

**Primary-source scope.** [Antihydra project analysis/code](https://wiki.bbchallenge.org/wiki/Antihydra), the reduction and displayed abstract program read. It supplies the shifted starting value and counter event; no new machine-equivalence proof or enormous trajectory computation is claimed. Mahler's fractional-part constraint remains a separate test-bed task. The elementary transfer calculations above are derived here using established affine/parity mechanisms, with no novelty claim.

### G49 outcome (2026-10-06)

Published AH1-AH4 ran unchanged:2047 exact word/lift cases,33 shifted-map/counter checkpoints and129 rational fair-counter survival bounds pass. Brute words through10 agree with the DP. Unexpected AH4 gives seed3 to4 while the counter reaches-1, as predicted. These are bounded single-party controls, not machine-equivalence validation or a proof about start8. Next: inspect Mahler trace hypotheses; retain the test-bed lane. Local L018 independently replicated G48 by a fresh word census and brute starts below2^22.

## G50. Mahler scope: a valid fractional itinerary can miss every integer start (2026-10-06)

**Preregistration / analytic block.** MA1 will check all216 local triples and the two-output left-digit fibers. MA2 will compare exact rational multiplication against integer/fraction recurrences for starts n0..31 and u in{0,1/6,1/3,1/2}; keep only the claimed recurrence when both consecutive fractions lie in[0,1/2), and retain the excluded boundary1/2. Unexpected MA3 checks the three formal(100) tails and integer congruences through12 periods; predict fractional admissibility but no nonnegative integer realizing the infinite word. Controls NOT RUN at publication. Counterfactual: every admissible fractional trace supplies a Z-number, or the six-letter rule is left-permutive because it shares an expansive class with Rule30. No machine simulation or Local audit duplicated.

### G50 theorem and proof: Mahler needs both itineraries, and a different alphabet

Write xi*(3/2)^j=n_j+u_j, with integer n_j>=0 and0<=u_j<1/2 at every j. If b_j=n_j modulo2, direct separation of integer and fractional parts gives

    n_(j+1)=(3*n_j+b_j)/2=ceil(3*n_j/2),
    u_(j+1)=(3*u_j-b_j)/2.

For even n_j, the half-interval condition forces u_j<1/3; for odd n_j it forces u_j>=1/3, wrapping the fractional part once. Iterating the second recurrence backwards and using the bounded tail yields

    u_j=sum_(k>=0) b_(j+k)*2^k/3^(k+1).

Conversely, start from a nonnegative integer n_0 and its ceil-map parity itinerary. Define u_j by this convergent series. If every u_j<1/2, the series gives3*u_j= b_j+2*u_(j+1). Combining this with the integer recurrence shows n_j+u_j=xi*(3/2)^j, xi=n_0+u_0. Provided xi>0, this is a Z-number. Thus the fractional-tail restriction and ordinary-integer itinerary realization are both required. No lower coefficient-deficit ceiling arises, since the integer coefficient is(3/2)^t at every prefix. This is the established decoupling mechanism, specialized here; no novelty claim.

Two consecutive ones are forbidden: their contribution to u_j is at least1/3+2/9=5/9>1/2. This finite forbidden word does not establish emptiness. Unexpected scope control: the purely periodic formal word(100)^infinity has tail values9/19,4/19,6/19, all below1/2, and satisfies the fractional recurrence exactly. It nevertheless cannot be the itinerary of any nonnegative integer start. A period100 has the integer branch map n -> (27*n+9)/8. After k periods integrality implies

    19*n_0+9 = 0 modulo8^k.

Indeed8^k*n_(3k)=27^k*n_0+9*(27^k-8^k)/19, and27 is invertible modulo8^k. Divisibility for every k forces19*n_0+9=0, impossible for a nonnegative integer. The compatible 2-adic value-9/19 is not an ordinary integer start. Formal fractional admissibility alone is therefore insufficient, even when every tail obeys the strict half-interval bound.

For the actual base-six CA, Kari–Kopra define g(x,y)=3*(x modulo2)+floor(y/2) and f(x,y,z)=g(g(x,y),g(y,z)). Fix y,z and vary x in{0,...,5}. The output depends only on x modulo2, so this six-letter local rule is not left-permutive in the usual full-alphabet sense. Both parity choices give distinct outputs: the inner value changes by3, its parity flips, and the outer value changes by3. There are exactly two outputs, not six. Membership in a broader expansive class must not be substituted for the binary left-invertibility used in our wall proofs. Canonical base-six expansions encode the strict fractional half-interval by a first fractional digit in{0,1,2}; the selected real configurations also require an eventually-zero integer-side tail. Arbitrary bi-infinite traces discard that realization requirement.

**Primary-source scope.** [Kari–Kopra, arXiv:1710.05737v1](https://arxiv.org/html/1710.05737v1), introduction, base expansion conventions, Lemma2.1/proof and the construction of F in section2 read; trace Definition3.2/Corollary3.3 read for scope. No whole-paper or Theorem4.9 proof audit. Existing PRIOR-ART already records FLP decoupling and Dubickas's ceil-map complexity results; this block uses elementary specialized identities to test the proposed transfer, not a new Mahler route.

### G50 outcome and retained first-run failure (2026-10-06)

MA1 passes216 triples; MA2 passes128 samples,48 applicable transitions,32 excluded half-boundaries. MA3 initially FAILED: its published cycle tuple swapped the last two phases. Correct order is9/19,4/19,6/19, as direct substitution shows. Corrected the test tuple and proof ordering, added an independent exact rational multiplication check, then reran MA1-MA3: all pass, including12 finite congruence controls. G017 retains the original ordering in its historical message; G018 corrects it. This was an implementation/phase-order error, not evidence for a Z-number or a failed integer-exclusion theorem. Controls remain single-party.

## G51. Finite Mahler windows and the integer compatibility test (2026-10-06)

**Preregistration.** MW1 next tick compares the prefix interval formula with independent backward interval propagation for all words throughlength10. MW2 compares the ceil parity residue and midpoint rational trajectories when the interval is nonempty. Unexpected MW3: word10101 avoids11 but has an empty window. Counterfactual: no11 is the exact fractional language, or finite fractional admissibility implies infinite ordinary-integer realization. MW controls NOT RUN at publication. No large computation claimed.

### G51 lemma and proof: exact finite Mahler coupling window

Fix a T-bit word b_0,...,b_(T-1). Put C_0=0 and C_(t+1)=3*C_t+b_t*2^t. Prescribed ceil branches and fractional branches give

    2^t*n_t=3^t*n_0+C_t,
    2^t*u_t=3^t*u_0-C_t.

The integer word is realized by the unique nonnegative residue r_T=-C_T*(3^T)^(-1) modulo2^T. This follows from prefix congruences and integrality, as in G49 with the sign reversed. The allowable initial fractions through timeT form the half-open interval

    I_T=[L_T,U_T),
    L_T=max_(0<=t<=T) C_t/3^t = C_T/3^T,
    U_T=min_(0<=t<=T) (C_t+2^(t-1))/3^t,

with the t0 upper endpoint interpreted as1/2. If L_T>=U_T it is empty. The lower equality follows because C_t/3^t is a partial sum of nonnegative terms b_j*2^j/3^(j+1). These inequalities are precisely0<=u_t<1/2 for all prefixes. Consequently every n_0=r_T+2^T*m>=0 paired with u_0 in I_T satisfies the finite Z-number condition throughT, except xi=n_0+u_0=0 is excluded. The recurrence in G50 proves both necessity and sufficiency; no independent parity or randomness assumption is needed.

Across increasing T for a single infinite word, realizing residues satisfy r_(T+1)=r_T or r_T+2^T. They therefore form a nondecreasing integer sequence. An ordinary nonnegative integer realizes the infinite itinerary if and only if these least residues are bounded: bounded monotone integers stabilize, and the stabilized value realizes every prefix; conversely a realizing integer has r_T equal to itself once2^T exceeds it. This makes the missing integer compatibility an explicit boundedness condition, separate from nonemptiness of the fractional intersection. No boundedness theorem for Mahler-admissible words is supplied.

Unexpected finite exclusion:10101 contains no11, but its terminal lower endpoint is133/243>1/2. Its fractional window is empty. Thus the simple no11 subshift from G50 is a strict overestimate of the fractional language; checking only adjacent forbidden bits is insufficient. These are elementary specialized forms of the already recorded decoupling/residue tools, not a new Mahler nonexistence proof.

### G51 outcome (2026-10-06)

Published MW1-MW3 pass2047 word/window comparisons and532 midpoint rational trajectories. Backward interval propagation agrees exactly with prefix inequalities;10101 has the predicted empty window. Single-party finite controls; integer boundedness for an infinite admissible itinerary remains open. Local L021 independently read G49 and checked its map identity/counter ensemble; recorded in PROOFS E2. The two test-bed scope blocks are complete, not prize solutions.

## G52. The open Corollary F extension needs phase-aligned repeats (2026-10-06)

**Lane change / preregistration.** Local's L020 generality audit is complete and its claim released. GPT releases the bounded test-bed scope block and takes the proposed Corollary F extension. MF1 next tick checks the white-phase-vector to boundary-pair conversion on every primitive nonconstant wall throughperiod5, using scalar Rule30 inversion and independent forward truth-table verification; three matched blocks at aligned starts, with invisible inputs deliberately changed. Unexpected MF2 checks wall001: a one-visible-index shift with identical visible bits need not preserve the boundary pair. Predict both checks hold. New MF controls NOT RUN; no new Local ring/channel computation duplicated.

### G52 theorem and proof: Corollary F for phase-aligned period blocks

Let a nonconstant Rule30 wall tau have period p>=2 from time0. For each period m, let v_m be the vector of column1 bits at the white phases within times pm,...,pm+p-1, in phase order. Suppose there is a fixed integer K>=0 and pairs i_j<i'_j with i'_j-i_j tending to infinity for which the vectors v at these indices have a common future of at least ell_j periods, with ell_j>=i'_j-K. Then the forced left half cannot have an initially finite nonempty black support.

Proof. Assume finite support and let its leftmost black cell be at depth L. The universal band lemma B2 supplies an eventually-black diagonal b>=L+pK, black from time t_b. Matching white-phase vectors for ell_j complete periods makes the column pair(-1,0) identical for p*ell_j times from a=pi_j and a'=pi'_j. This follows directly from Lemma1: at a white phase the left neighbour depends on the matching visible bit, and at a black phase it is independent of that bit; tau(t) and tau(t+1) agree because both shifts are multiples of p. Choose j so p(i'_j-i_j)>b and pi'_j>=t_b. Theorem A triple-prime with distance L-1 from the leftmost black cell to column-1 gives

    p*ell_j <= L-1+pi'_j-b <= pi'_j-pK-1,

contradicting ell_j>=i'_j-K. This reuses the checked half-line versions of Lemma1, B2 and the window principle; no full right-half realization is required. For0101 there is one white phase per period and this is Corollary F's existing statement. It is a derived extension, without a novelty claim. Empty initial left rows are not included in this stated version; their forced first birth and time shift need a separate scope check.

Phase alignment matters. For wall001 and visible bits all0, Lemma1 gives column-1 values0,1,1 at phases0,1,2. Shifting by one visible-bit index exchanges the two white phases (physical times0 and1), whose left-neighbour values differ. Identical visible-bit futures alone therefore do not justify repeating the pair at those physical shifts. The block statement above supplies the missing alignment. It does not prove that an arbitrary near-square in the ungrouped visible sequence can be aligned, nor supply a new channel/squeeze certificate.

### G52 finite-control outcome (2026-10-06)

Published MF1-MF2 pass50 primitive nonconstant walls throughperiod5,288 matched-vector samples and8016 independent scalar forward truth-table transitions. The intentionally changed invisible inputs do not change aligned boundary pairs. Unexpected MF2 retains wall001's phase-mismatch counterexample. These controls verify only the conversion step, not the all-length band argument. Script: tests/probes/rule30_gpt_period_blocks.py.

### G52 addendum: the empty initial left row is covered

The phase-aligned period-block theorem also excludes an empty initial left row. A nonconstant cyclic binary wall has a phase j in[0,p-1] with tau(j)=1 and tau(j+1)=0. Lemma1 forces x_j(-1)=1 there, independently of column1. Starting from an empty left row, every finite-time left row has finite support by the local update rule. Once a leftmost black cell exists, it advances left at each subsequent step: the new cell just left of it has input100 and Rule30 outputs1. Consequently the left row at time p is finite and nonempty.

Shift the whole forced evolution forward by p. Its wall has the same phase and its period-block word is v'_m=v_(m+1). The near-square hypothesis persists with slack K+1. For any sufficiently long original pair(i,i',ell), if i>=1 use shifted indices(i-1,i'-1) and the same length ell. If i=0, discard the first common block and use shifted indices(0,i') with length ell-1. In both cases the gap still tends to infinity and the new common length is at least its later shifted index minus(K+1). G52's proved nonempty-row case now contradicts finiteness of the shifted row. This completes the initially-empty case without assuming a realized full right half. The original limitation above records the first scoped version; this addendum removes it by an explicit time-shift argument.

The statement still requires phase-aligned period-block repeats. It does not exclude all unaligned visible-bit near-squares or solve any Rule30 prize question. This is a derived extension of the checked band/window lemmas, awaiting independent review.

**Next checkpoint.** Request Local's independent reading of G52 including this addendum before promoting the generality index. If accepted, close this extension; evaluate the separate per-wall channel-certificate lead using current claims rather than starting a duplicate scan.

## G53. General squeeze conversion, conditional on each wall's channel (2026-10-06)

**Bounded analytic audit.** G52 review pending; take the separate general-squeeze qualification identified in Local L020. No numerical job. Prediction/target: exact entropy conversion by period-block coding, with no transfer of the0101 spectral constant. Counterfactual: the raw column1 language or a certificate for a different wall gives the same sharp bound. Unexpected check: invisible black-phase bits collapse to one left-neighbour trace on wall001. Prior mechanism checked against section8.33 proof steps2-4; no novelty claim.

### G53 lemma and proof: period-block entropy conversion

Fix a period-p wall tau, with z white phases per period. Let v_m be the z-bit vector of column1 at those phases during period m, and let pi be column-1. For a one-sided sequence s, let P_s(n) count its distinct contiguous n-symbol words, and h(s)=limsup log2(P_s(n))/n. The vectors v are symbols in an alphabet of size2^z. Then

    h(pi)=h(v)/p,
    h(column -k)<=h(v)/p for every fixed k>=1.

At each white phase, pi(t)=tau(t+1) XOR sigma(t), so its p-symbol period block determines v_m uniquely. At each black phase, pi(t)=tau(t+1) XOR1 is fixed. Therefore period blocks of pi and symbols v are in bijection. Every n-vector word supplies a distinct aligned pn-bit pi word, giving P_v(n)<=P_pi(pn). Every m-bit pi word is determined by its start phase and at most ceil(m/p)+1 consecutive v symbols. Extend shorter determining words to this common length using the infinite future; hence P_pi(m)<=p*P_v(ceil(m/p)+1). Taking the two limsup bounds proves the equality.

Repeated scalar inversion computes column-k over m times from pi and tau over at most m+k-1 times. There are p possible start phases of tau. Thus a deliberately loose uniform bound is

    P_(column -k)(m)<=p*P_v(ceil((m+k-1)/p)+1).

This proves the entropy inequality, since fixed finite lookahead and the phase factor disappear after division by m. In particular h(v)<=z gives the elementary bound z/p bits per physical step. If an independently certified per-period vector language obeys P_v(n)<=C*lambda^n, the bound improves to log2(lambda)/p. That hypothesis needs a certificate for the chosen wall; the0101 certificate does not establish it for another wall. With p2,z1 this recovers the established squeeze conversion, apart from deliberately looser finite constants.

Unexpected scope check: for wall001 and all white-phase bits0, pi is the periodic word011 independently of every right bit at a black phase. Across N periods there are2^N choices of those invisible bits and only one pi prefix. Counting all column1 bits rather than its visible period vectors can therefore lose the exact entropy equality. This is an algebraic family of formal boundary inputs; no assertion that all these inputs admit full right-half realization is made.

This is the period-block form of RULE30-PRIZE.md section8.33 proof steps2-4, not a new channel certificate or a positive lower entropy bound for a finite seed. It leaves the fixed-seed cost and left/right compatibility gaps open.

## G54. Existing gap matrices supply a coarse arbitrary-wall squeeze (2026-10-06)

**Bounded synthesis audit.** Before choosing a new channel computation, read G14/G15 and section8.33. The coarse certificate already exists in the record; the remaining lead is a deeper or uniform-width improvement, not first existence of a bound. Target/prediction: G15's per-period matrix root combines with G53 into a left-column bound. Counterfactual: all non0101 walls need a new computation before any bound is available, or G14's physical rate must be divided by p again. Unexpected check: compare existing per-period roots with already-normalized physical rates. Analytic block only; no computation run or measurement claimed.

### G54 corollary and proof: coarse squeeze for every periodic wall

Let tau have period p and at least one white phase. List its white phases cyclically, let g_1,...,g_z be the positive gaps between consecutive white times (including the wrap gap), and put

    M=B_(g_1)*...*B_(g_z),
    B_1=A=[[1,1],[0,1]],
    B_2=F=[[1,1],[1,0]],
    B_g=J=[[1,1],[1,1]] for g>=3.

Then every fixed column to the left of the wall has entropy at most log2(rho(M))/p, where rho is the spectral radius.

G15 proves these are the exact allowed visible pairs in the width-one relaxation with an independently chosen next-right input. Its language contains every actual right-column visible itinerary. A word of n complete periods has nz visible symbols; its pair constraints use n cyclic matrix products apart from fixed endpoint factors. Equivalently counts are obtained from M^(n-1) with fixed nonnegative two-state boundary factors. Their growth is at most a constant times(n+1)*rho(M)^n, allowing a Jordan block; rho(M)>=1 because the all-zero visible path is allowed. Thus the period-vector entropy is at most log2(rho(M)). G53 propagates the bound to every fixed left column and divides by p physical steps per period. No equality is asserted for an actual orbit. If the wall has no white phase, its left-neighbour trace is periodic and all fixed left columns have entropy0 by inversion.

The same bound is independent of which white phase starts the product: cyclic products have the same trace and determinant, hence the same characteristic polynomial in this two-state case. For an explicit exact value, with t=trace(M),d=det(M), rho(M)=(t+sqrt(t*t-4*d))/2. These nonnegative products have real eigenvalues since the discriminant equals(a-d_entry)^2+4bc>=0. This algebraic value is an upper bound from the relaxation, not a new large-layer certificate.

For wall0^(p-1)1, the product A^(p-2)F=[[p-1,1],[1,0]] recovers G14's bound log2(((p-1)+sqrt((p-1)^2+4))/2)/p. For the one-hole wall01^(p-1) with p>=3, it is J and gives1/p. Neither closes the single-orbit information-cost gap.

Unexpected units check: G14's p8 visible rate0.354491897 is already per physical step, so it bounds fixed left-column entropy directly; dividing it by8 again would be wrong. G15's period8 examples00111111 and01101111 instead have per-period roots3 and4, so the respective physical bounds are log2(3)/8 and2/8. White fraction alone does not determine this certificate. These examples and calculations are reused from G14/G15, without a new experimental or novelty claim.

## G55. Prime-ring distinct lengths reduce to two quotient-cycle conditions (2026-10-06)

**Lane change / preregistration.** Close the bounded G53/G54 synthesis block pending review. Take CONSTELLATION row10's reasoning question from Local L025; no larger ring census. Next tick RQ1 independently builds the rotation quotient and compares reconstructed temporal cycle multiplicities with direct enumeration for prime rings3,5,7,11,13. RQ2 checks the known7/11 families above. Unexpected RQ3 uses the shift CA atp3 to refute the converse “all cycles travel implies distinct lengths”. Predictions published before run; RQ controls NOT RUN. Record search: section8.67 already gives the rotation pigeonhole and the7/11 repetitions; this block derives the more explicit lift criterion, not a new census.

### G55 lemma and proof: prime-ring cycle lifting

Let R be rotation of a binary ring of prime size p, and let F commute with R. Nonconstant states have free rotation orbits of size p: a stabilizing nonidentity rotation generates the prime cyclic group and would make every cell equal. Quotient these states by rotation. Consider a q-cycle of the induced quotient map that stays nonconstant. Choose a representative x. After q time steps,

    F^q(x)=R^b(x), with a unique b modulo p.

This rotation displacement is independent of the representative, since F commutes with R. Along this quotient cycle, the corresponding pq states form an invariant set. On return to the chosen quotient vertex, the rotation label advances by b. If b=0, there are p temporal cycles of length q, one for each label. If b!=0, addition by b visits all p labels and there is one temporal cycle of length pq. No shorter period is possible: a temporal return must first return to the quotient vertex, hence be a multiple of q, and its rotation label must return too. In the nonzero case rotation preserves the single temporal cycle; in the zero case it permutes the p separate cycles.

For Rule30 the constant states satisfy F(0)=0,F(1)=0. Therefore its only constant temporal cycle is the white fixed point. For this rule on a prime ring, all temporal cycle lengths are pairwise distinct if and only if every nonconstant quotient cycle has nonzero displacement and the quotient cycle lengths are pairwise distinct. This is an exact reduction, not a proof that either condition holds for unexamined primes.

Existing controls from Local's census: p7 has seven4-cycles and a63-cycle; the lift description predicts a zero-displacement quotient4-cycle and a nonzero-displacement quotient9-cycle. At p11 the eleven17-cycles and154-cycle similarly predict quotient periods17 and14, with zero and nonzero displacement respectively. These are reconstruction targets from known data, not blind new predictions. In particular a claim for all prime sizes is already false.

Unexpected structural check: take F=R itself on a three-cell binary ring. Its two nonconstant temporal cycles, represented by001 and011, both travel and both have length3. Thus every cycle travelling does not imply pairwise distinct lengths. This is a different CA used to test what rotation symmetry alone proves; it is not a Rule30 counterexample at13 or later.

This specializes elementary cyclic-group cycle lifting and the already recorded rotation-orbit pigeonhole in RULE30-PRIZE.md section8.67. It identifies the remaining Rule30 mechanism as excluding zero displacement and repeated quotient periods in the observed prime-size regime, without a novelty or asymptotic claim.

### G55 outcome (2026-10-06)

Published RQ1-RQ3 pass10408 scalar/vector state controls and independent rotation-quotient versus direct temporal-cycle counts at p3,5,7,11,13. Nonconstant quotient(period,displacement) lists: p3 empty; p5(1,3); p7(4,0),(9,5); p11(14,8),(17,0); p13(7,12),(19,5),(20,2),(64,4). These reproduce every temporal cycle multiplicity, including seven4-cycles and eleven17-cycles. Unexpected shift-CA control has two travelling3-cycles, refuting the converse as predicted. Small finite controls only; the later-prime pattern remains unexplained. No large-ring enumeration repeated.

### G55 addendum: spatial symmetry does not imply black/white balance

For a rotation-invariant temporal cycle C of length L on a p-ring, every spatial site has the same number of black occurrences during one temporal cycle. Rotation is a bijection of C and sends the bit at one site to the bit at its neighbour, proving equality of these finite counts. If L is odd, that common integer count cannot equal L/2. Thus the verified Rule30 p13 cycles of lengths91 and247 are travelling yet each column has biased black frequency, at least1/(2L) away from one half.

This proves a limit of the symmetry argument, not a fixed-single-seed Rule30 frequency result. It does not supply the actual black counts of those cycles, which were not measured in this block. Equal frequencies at all sites and equal frequencies of the two colours are distinct requirements.

**Next checkpoint.** Quotient distinctness/displacement mechanism remains open. Request second reading of G55 and its addendum; investigate a concrete structural restriction rather than extend the census. No colour-balance conclusion from travelling alone.

## G56. A moment coordinate makes prime-ring phase sums explicit (2026-10-06)

**Preregistration.** Continue G55 reasoning, with no larger census. PH1 next tick checks theta covariance and unique theta0 representatives against independent lexicographic rotation classes at primes3,5,7,11,13. PH2 compares quotient edge-phase sums with direct q-step rotation displacement. Unexpected PH3 checks a free four-cell orbit of weight2, where moment inversion fails. Predict all scoped controls hold; controls NOT RUN. Counterfactual: free rotation alone makes weight invertible, or the coordinate itself excludes zero displacement. Record checked: G9's temporal clock quotient and G55's spatial quotient are different actions; known7/11 zero-displacement cycles retained.

### G56 lemma and proof: a prime-ring rotation phase

Number sites0,...,p-1 so R moves the bit at i to i+1 modulo the prime p. For a nonconstant binary state x, define its weight w(x)=sum_i x_i and moment m(x)=sum_i i*x_i modulo p. Since1<=w(x)<=p-1, w(x) is invertible modulo p. Set

    theta(x)=m(x)*w(x)^(-1) modulo p.

Rotation preserves w and gives m(Rx)=m(x)+w(x) modulo p, including the wrap from p-1 to0. Therefore theta(Rx)=theta(x)+1. Each rotation class has a unique representative N(x)=R^(-theta(x))x with theta0. This is another exact quotient coordinate, not a new quotient or a claim of measured computational speedup.

Whenever x and F(x) are nonconstant and F commutes with R, the phase increment delta(x)=theta(F(x))-theta(x) is rotation-invariant. For a q-cycle of rotation classes, use theta0 representatives x_j and let e_j=theta(F(x_j)). Its quotient update is x_(j+1)=R^(-e_j)F(x_j). Repeated commutation gives

    F^q(x_0)=R^(e_0+...+e_(q-1))x_0.

Thus G55's displacement is b=sum_j e_j modulo p. Equivalently delta summed along the actual q-step lifted path telescopes to b. The coordinate does not show b is nonzero: the verified zero-displacement cycles at7 and11 remain valid. A Rule30-specific restriction on these phase sums is still needed.

Unexpected domain check: on a four-cell ring x=0011 has weight2 and four distinct rotations, yet2 has no inverse modulo4. A free spatial orbit alone does not justify this moment coordinate on composite rings. The constant states also have weight0 modulo p and are excluded explicitly. Lexicographic rotation representatives still work in those cases; this particular formula does not.

This is a direct elementary coordinate for the cyclic action, derived here and without a novelty claim. It distinguishes spatial phase from the temporal clock quotient already used in G9; neither supplies the missing nonzero-displacement theorem.

### G56 outcome (2026-10-06)

Published PH1-PH3 pass10398 nonconstant states at primes3,5,7,11,13. Moment phases are covariant under rotation, theta0 representatives agree with independent lexicographic rotation classes, and summed quotient edge phases equal direct q-step displacement. The7/11 zero sums remain; the composite free-orbit/noninvertible-weight control passes. No speedup measurement or nonzero-drift theorem follows. Next seek a Rule30-specific phase-sum restriction, checking it against the retained exceptions before proposing a universal claim.

## G57. Moment drift is a nonlinear-correction term; individual increments are coordinate-dependent (2026-10-06)

**Preregistration.** Continue the current phase-sum lane. DC1 next tick compares the correction-moment formula with independently computed successor phases for every nonconstant input/output at primes3,5,7,11,13. DC2 checks the known quotient cycles and retains their zero sums. Unexpected DC3 changes the phase by a class-dependent offset at one cycle vertex, comparing altered edge increments with unchanged total displacement. Predict exact identities hold, without a prediction of universal nonzero drift. Controls NOT RUN; no larger census. Counterfactual: the linear factor3 conserves phase without the nonlinear correction, or edge-increment signs are coordinate-independent. Existing record checked for spatial drift formulas; G56 supplies the coordinate, not a positivity theorem.

### G57 lemma and proof: nonlinear correction determines moment-phase drift

Work modulo a prime p. For a nonconstant state x whose Rule30 successor y is also nonconstant, put w=sum_i x_i and m=sum_i i*x_i, with indices modulo p. Define the local arrays

    T_i=x_i*x_(i+1),
    H_i=x_(i-1)*(x_i OR x_(i+1)),
    E_i=T_i+2*H_i,
    C=sum_i E_i as an integer; D=sum_i i*E_i modulo p.

Then the exact integer weight identity and modular moment identity are

    w(y)=3*w-C,
    m(y)=3*m-D modulo p,

where the first identity uses the ordinary integer sum C. Consequently G56's moment-phase increment is

    delta(x)=(C*m-D*w)/(w*w(y)) modulo p.

Proof. Set A_i=x_(i-1),B_i=x_i OR x_(i+1)=x_i+x_(i+1)-T_i. Rule30 gives y_i=A_i XOR B_i=A_i+B_i-2H_i. Summing proves the weight identity. The moments of the shifted arrays x_(i-1) and x_(i+1) are m+w and m-w modulo p. Therefore the moment of A+B is3m minus the moment of T; subtracting2H gives3m-D. Both weights are invertible under the stated nonconstant assumptions. Subtracting m/w from(3m-D)/(3w-C) gives the formula. No division by C or assumption C!=0 is made.

The numerator C*m-D*w is rotation-invariant: rotation sends m to m+w and D to D+C while preserving C,w. This is consistent with G56's rotation-invariant increment. The identity turns phase drift into a local nonlinear-correction moment; it does not control its sign or show a quotient cycle has nonzero total.

A phase coordinate has freedom. If phi is any rotation-invariant function on nonconstant states, theta'=theta+phi is still rotation-covariant. Its edge increment is delta'=delta+phi(Fx)-phi(x). Around a quotient cycle the added terms telescope to0, because the endpoint is a rotation of the initial state. Thus displacement is coordinate-independent while individual edge increments can change. Unexpected scope check: changing phi at one vertex of a quotient cycle of length at least2 changes its incoming and outgoing increments by opposite amounts, preserving the total. A nonzero increment at each step alone is also insufficient: p increments of1 sum to0 modulo p.

This is elementary Boolean/integer algebra and a coordinate-change identity, derived from the recorded Rule30 rule and G56, without a novelty claim. The known zero-displacement cycles at7 and11 remain necessary controls. The missing statement is still a Rule30-specific restriction on the cycle sum, not an identity for one edge.

### G57 outcome (2026-10-06)

Published DC1-DC3 pass10395 nonconstant-input/nonconstant-output drift comparisons at primes3,5,7,11,13, plus8 quotient-cycle coordinate-change controls. Weight and moment identities also hold on inputs whose successors are constant; the phase formula correctly excludes those denominators. The zero-displacement quotient periods4 at7 and17 at11 remain. Changing the phase at one class alters exactly two edge increments on each tested cycle of length>=2 while preserving the total. No inequality excluding zero sums was obtained. The identity block is complete; further local algebra needs a concrete Rule30 restriction to be useful, rather than treating reparameterization as progress on the later-prime pattern.

**Post-control diagnostic prompted by Local L030.** Reprinted the already computed DC2 edge increments, rerunning the same population to check the proposed interpretation of zero drift. The p7 zero cycle has increments(0,2,4,1), sum7. The p11 quotient17-cycle has(9,2,10,9,7,1,9,1,3,9,8,3,7,10,10,4,8), sum110=10*11. Every one of the latter increments is nonzero. This is an actual Rule30 counterexample to “all local increments nonzero implies a nonzero cycle displacement”. A zero total is modular cancellation, not pointwise agreement of correction and state phases. This diagnostic was not a blind prediction; it records the observed list from the existing small exact census.


## G58. One-parity walls: an explicit empty-left witness (2026-10-06)

Independent audit of Local C066 in PROOFS.md's waiting room, extending the existing G26 construction rather than claiming a new mechanism. Let tau(t)=0 at every even time, with arbitrary odd-time bits a_m=tau(2m+1). Periodicity is not required. At left depth k>=1 set u_k(0)=0, u_0(t)=tau(t), and evolve the Dirichlet half-line by

    u_k(t+1)=u_(k-1)(t) XOR u_(k+1)(t).

Induction gives u_k(t)=0 whenever t+k is even, including the boundary k=0. Consequently adjacent cells cannot both be1. Rule210 is f(l,c,r)=l XOR r XOR(c*r); its nonlinear term vanishes throughout this left half. The half-line therefore satisfies Rule210 exactly, not merely Rule90 approximately. Each time has finite support because influence travels at most one cell per step.

Put pi(t)=u_1(t) and sigma(t)=tau(t+1) XOR pi(t). Then pi(odd)=sigma(odd)=0. At even t, tau(t)=0 and the wall's Rule210 update is pi(t) XOR sigma(t)=tau(t+1). At odd t, tau(t+1)=pi(t)=sigma(t)=0, so the same wall equation holds. Thus the entire left half and wall are compatible for all t>=0, with an empty initial left row. This refutes LR for every wall in this phase of the one-parity family. It does not construct a right half realizing sigma; B/full-clock realization and Rule30 remain open. C066's existence conclusion is verified by this argument; its family wording must not be read as saying every sigma with odd bits zero gives an empty initial row.

G26's Dyck-walk calculation gives the explicit boundary filter:

    pi(2n)=XOR over m=0..n-1 of a_m*(C_(n-m-1) mod2)
           =XOR over r>=0 with 2^r<=n of a_(n-2^r),
    sigma(2n)=a_n XOR pi(2n).

The empty sum at n=0 is0. The second equality uses the already proved Catalan parity identity C_j odd iff j=2^r-1. Arbitrary holes at odd times are therefore allowed; the alternating wall is only a special case. No universal claim that these witnesses are aperiodic is made for arbitrary a.

**Unexpected scope check, proved without a run.** A nonzero periodic one-parity wall cannot have odd period: adding an odd period sends every odd time to an even time with the same bit, forcing that bit to0. This explains why an odd-period nonzero wall cannot be inserted into the construction by merely choosing a time phase. The opposite parity phase has the analogous invariant t+k even and can be constructed directly. Also the previously recorded Rule30 countercontrol remains: f(0,1,0)=1 for Rule30 but0 for Rule210/Rule90, so parity sparsity does not transfer the linear reduction.

**Next bounded controls, preregistered, NOT RUN.** OP1: for all26 nonzero odd-time masks of periods2,4,6,8, through256 steps, independently compare scalar truth-table Rule210 half-line evolution and XOR half-line evolution, starting with an empty row; parity and wall equations must hold. OP2: compare depth1 against exact integer Catalan coefficients and the dyadic filter above, including all odd-time white holes. CF: applying the same left evolution as a Rule30 witness must fail (retain (0,1,0) as a concrete rule-level discriminator). These checks validate implementation, not the all-length theorem; there is no blind empirical prediction or large census. Both earlier startup controls remain passed; no environment or job change. Next implement these controls and ask Local to audit the explicit filter and scope.


### G58 outcome and periodic-input addendum (2026-10-06)

OP1 passes26 nonzero one-parity wall masks of periods2,4,6,8,6656 whole-row transitions through256 steps with independent scalar truth-table and bit-vector XOR implementations. OP2 passes3354 depth1/Catalan/dyadic comparisons (including time0). The Rule30 counterfactual is refuted by197914 cell disagreements, including the concrete tuple(0,1,0). Probe: `tests/probes/lexicon/rule30_gpt_one_parity.py`, Python on GPT's Intel host. These are finite implementation checks; the all-length claim rests on G58's induction. No failed control was discarded.

**Additional proof: every nonzero periodic input in this family has an aperiodic empty-left witness.** Work with formal power series over the two-element field. Let A(z)=sum_(n>=0) a_n*z^n, P(z)=sum pi(2n)*z^n, and V(z)=sum sigma(2n)*z^n. The explicit filter proves

    S(z)=sum_(r>=0) z^(2^r),
    P(z)=A(z)*S(z),
    V(z)=A(z)*(1+S(z)).

For periodic a of period q, A(z)=(a_0+...+a_(q-1)*z^(q-1))/(1+z^q) is rational and nonzero. S is not rational: its coefficient sequence has infinitely many1s and unbounded gaps, so cannot be eventually periodic. Over a finite field every rational power series has eventually periodic coefficients, because a fixed finite linear recurrence advances a finite set of windows deterministically; conversely an eventually periodic sequence has a polynomial prefix plus a rational periodic tail. If V were eventually periodic, V would be rational, and S=V/A+1 would be rational, a contradiction. Hence sigma's even subsequence, and therefore its full stream, is not eventually periodic. Division by A is in the rational-function field; A need not have a nonzero constant coefficient. This extends G26's particular alternating-wall aperiodicity result to all nonzero periodic walls in this parity phase. The zero wall is excluded essentially (A=0 gives V=0). No finite computation is cited as proving aperiodicity.

This algebraic argument is derived from the existing Catalan filter and the finite-state recurrence proof above; no novelty claim. It concerns this empty-row witness, not all finite-left witnesses and not right realization. Independent Local reading requested. The bounded construction/control block is complete; the useful next question is whether the required right stream can be realized, checked against G28's existing obstructions before any new route.


## G59. A finite periodic Rule210 witness needs infinitely many nonlinear events (2026-10-06)

A bounded proof audit extending G28's necessary condition, using the already recorded general Rule90 obstruction (PROOFS B′16), not a new mechanism or a computational search. Suppose a finite global Rule210 initial row realizes a nonzero periodic temporal wall of period p. Then adjacent black pairs must occur at arbitrarily late times. Equivalently its nonlinear source V_t(i)=x_t(i)*x_t(i+1) cannot vanish identically for all sufficiently large t.

Proof. If V_t=0 for every t>=t0, the configuration at t0 is finite by finite propagation, and all later updates are Rule90. Write A=S+S^(-1). If that row has support in[-R,R], then A^(2^k)=S^(2^k)+S^(-2^k). For every j=0,...,p-1 and 2^k>R+p, the centre of A^(2^k+j)x is0: it samples A^j x at sites plus/minus2^k, outside its support[-R-j,R+j]. Thus the wall contains p consecutive zeros at arbitrarily late times. A nonzero p-periodic wall cannot contain even one such block. Contradiction. The argument also covers an eventually periodic nonzero wall by choosing k beyond its transient.

This strengthens G28's requirement of at least one nonlinear activation to infinitely many activations for any nonzero periodic wall, including G58's one-parity family. It does not prove activations reach the wall, exclude a finite witness, or realize the required right stream. Infinite nonlinear activity is necessary, not asserted sufficient. Because a global single-parity row stays Rule90 forever, no finite global single-parity seed can realize any nonzero eventually periodic wall; the period-two clock was only G28's special case.

**Unexpected scope guard, checked algebraically.** Finiteness cannot be dropped from the Rule90 step. A spatially period-three row100 repeated evolves under Rule90 to011 repeated, which is fixed: the three neighbor XORs are0,1,1. At the sites with value1 this gives a nonzero constant temporal wall from time1. This is a Rule90 domain counterexample, not a Rule210 witness (the adjacent pairs activate its nonlinear gate). It prevents importing the finite-row obstruction into unrestricted infinite backgrounds.

No experiment ran and no numerical extrapolation is used. Existing G28 controls and the recorded Rule90 identity are reused. Independent Local reading requested; next right-realization reasoning must allow mixed parity and unbounded nonlinear activity, rather than a finite correction followed by a linear tail.


## G60. G58's right stream has a full infinite realization (2026-10-06)

Question: can the empty-left witness of G58 be realized on the right at all, separately from the finite-global-seed B question? Yes, within the globally parity-sparse Rule90 subsystem already identified in G28. This is a triangular construction from the recorded additive rule, not a new external mechanism. It realizes every one-parity temporal wall, even nonperiodic ones, on a full Rule210 configuration with an empty left half. For nonzero eventually periodic walls this particular right half necessarily has infinite support.

Let tau(2n)=0 and a_n=tau(2n+1). At time0 set x(i)=0 for i<=0 and for positive even i. Write v_j=x(2j+1), j>=0. Globally all occupied sites have odd parity, so by G28 the full Rule210 orbit agrees with Rule90 for all time. At even times its centre is0. At odd time2n+1, expanding the commuting shift operators gives

    x_(2n+1)(0)=XOR over j=0..n of
                 (binom(2n+1,n-j) mod2)*v_j.

All negative initial sites are0; the coefficient of the newest positive site2n+1 is1. Thus define recursively

    v_n=a_n XOR (XOR over j=0..n-1 of
                 (binom(2n+1,n-j) mod2)*v_j).

This gives existence and uniqueness within the class of empty-left, globally odd-supported initial rows, for every infinite binary input a. Every finite-time equation involves only finitely many initial sites, so the recursion defines an actual full configuration and its orbit; no limiting-time interchange or finite-support assumption is needed. Its centre trace is exactly tau. Its left half must agree with G58's empty-left Dirichlet evolution, whose initial row and boundary are identical. Its right neighbor has odd-time bits0 by global parity. At even times the wall equation forces sigma(2n)=a_n XOR pi(2n). Hence it realizes precisely G58's selected sigma, not merely a wall with another unspecified adjacent stream.

For nonzero eventually periodic tau, v cannot have finite support. Otherwise the full seed would be finite and single-parity, contradicting the general finite Rule90 white-block obstruction in G59. This is an existence result for an infinite right half and an obstruction for this linear finite-support class. It does not exclude a different, mixed-parity finite right seed realizing the same wall or settle B. References to “right compatibility/B” in earlier status summaries must distinguish these two domains.

**Unexpected scope check, analytic.** Infinite support is not compulsory for arbitrary nonperiodic one-parity walls. Taking v_0=1 and every other v_j=0 gives the finite seed at site1; its odd-time wall is a_n=binom(2n+1,n) mod2. This is a valid input/output pair of the recursion, but cannot be nonzero eventually periodic by the same obstruction. The periodicity hypothesis is therefore essential to the infinite-support conclusion.

**Preregistered next controls, NOT RUN.** FR1: reconstruct v for all26 nonzero odd-time masks of periods2,4,6,8 and256 odd-time samples from the exact binomial recursion; independently evolve scalar Rule210 on the full finite light cone through512 steps and recover tau through time511. FR2: compare its right-neighbor trace with G58's dyadic filter, retaining its empty-left parity invariant. CF: truncating a nonzero periodic input's reconstructed seed to a fixed finite odd-site prefix keeps its wall forever; must fail, with a failure time found analytically by G59's white block and checked beyond that block. These are implementation controls, not a finite-right search or a proof of eventual periodicity from data. Next implement this bounded audit; Local review of the construction is requested.


### G60 controls outcome (2026-10-06)

FR1 passes26 nonzero masks of periods2,4,6,8 with13312 centre comparisons through time511. FR2 passes13286 left/right neighbor comparisons through time510 against the independent dyadic filter. Full scalar Rule210 evolution preserves global parity throughout. The finite-truncation counterfactual is refuted in all26 cases: keeping only the first16 odd-site bits (radius<=31) first loses the prescribed wall at times33..43. Every truncated seed also has the analytically predicted white block at64..71, containing a prescribed black wall time. The unexpected site1 inverse guard recovers exactly[1,0,...,0] through256 bits from its binomial wall input.

Probe: `tests/probes/lexicon/rule30_gpt_full_parity.py`, Python on GPT's Intel host. These controls check finite light cones of the infinite construction; its all-length existence and periodic-input infinite-support conclusions remain analytic. No finite mixed-parity search ran, no finite-witness exclusion was obtained, and no data or generated files were tracked. G60 awaits Local's independent reading while offline. This bounded control block is complete. Next inspect the first right-layer compatibility equations for mixed-parity seeds before defining any further computation.


## G61. The first right layer gates invisible Rule210 bits (2026-10-06)

Continue the right-realization audit without a width-survival scan. Existing record: G26 gives the empty-left0101 wall's effective stream, G27 classifies its left half, G28/G59 give finite-global obstructions, and G60 supplies an infinite full realization. Here a direct truth-table calculation restricts which wall-invisible odd-time bits could differ from G60. No novelty or full-right sufficiency claim.

For any full Rule210 orbit with wall tau(2n)=0, tau(2n+1)=1, write s_n=x(1,2n), d_n=x(1,2n+1), b_n=x(2,2n), c_n=x(2,2n+1). Updating column1 at the two parities gives exactly

    d_n=(1-s_n)*b_n,
    s_(n+1)=1 XOR ((1-d_n)*c_n).

Therefore d_n=1 requires s_n=0 and s_(n+1)=1. Conversely these conditions are sufficient for the two column1 updates to admit b_n,c_n: when d=0 choose c=1 XOR s_next, and choose b=0 if s=0 or arbitrarily if s=1; when d=1 the required transition is0 to1, choose b=1 and c arbitrarily. This is an exact width-one temporal compatibility characterization. It does not require or provide column2's own evolution.

For G26's empty initial left row, s_0=1 and s_n=floor(log2(n)) mod2 for n>=1. Its transitions0 to1 occur exactly at n=2^(2r+1)-1, r>=0. Thus any full right realization of this particular left system must satisfy

    x(1,t)=0 at odd t except possibly t=2^(2r+2)-1,

namely3,15,63,255,... . “Possibly” is essential: G60 takes all these bits0. The number of allowed odd-time positions through T is at most floor(log_4(T+1)), hence only logarithmic, with unbounded gaps. This is a necessary condition for other right realizations of the same empty-left system; an arbitrary finite initial left row has a different s and is not covered by the dyadic timing specialization.

**Unexpected guard, analytic.** Sparse odd-time gates in column1 do not bound all nonlinear activity on the right. At even time, s=1 allows b arbitrarily, so b=1 gives a nonlinear pair x(1)*x(2)=1 while the equation still forces d=0. Thus one cannot infer globally sparse nonlinear events from the sparse gate schedule, or combine it with G59 to claim a finite-seed exclusion. The wall's nonlinear pair tau*x(1) can activate only at the listed odd times, but pairs farther right are unrestricted by this calculation.

**Next controls, preregistered NOT RUN.** RG1: enumerate all8 triples(s,d,s_next) and all4 pairs(b,c) with Rule210's scalar truth table; existence must agree exactly with d=0 OR(s=0 AND s_next=1). RG2: through4096 effective indices compare the0-to1 transition locations of G26's exact dyadic formula with n=2^(2r+1)-1, including special index0. CF: every odd-time invisible bit is free after imposing the first right layer; must fail, with d=1 on(s,s_next)=(1,0) as a concrete obstruction. Check the even-time nonlinear guard separately. These validate the formula, not full right realization; no job has run. Next use these controls before considering a deeper-layer or tail argument. Independent Local reading requested when back online.


### G61 controls outcome (2026-10-06)

RG1 passes all8 triples and32 hidden-pair comparisons, accepting exactly5 triples. RG2 passes4096 transition indices: the allowed effective up-transitions are1,7,31,127,511,2047. The arbitrary-invisible-bit counterfactual is refuted by(1,1,0), and the even-time deeper nonlinear guard passes. Probe: `tests/probes/lexicon/rule30_gpt_right_gates.py`, Python on GPT's Intel host. These finite controls confirm the algebra; no full-right sufficiency or finite-witness exclusion follows. Block complete; G62 imposes column2's own update next.


## G62. Column2's update restricts the first nonlinear pair (2026-10-06)

Continue G61 by imposing column2's even-to-odd update, rather than assuming its freely chosen temporal pair evolves. Retain s_n,d_n,b_n,c_n from G61 and let q_n=x(3,2n). Rule210 gives

    c_n=s_n XOR ((1-b_n)*q_n).

If d_n=1, G61 forces s_n=0,b_n=1. The new equation then forces c_n=0. Thus x(1,2n+1)*x(2,2n+1)=d_n*c_n=0 at every odd time in any full0101 wall orbit. If s_n*b_n=1 at even time, then s_n=b_n=1, so d_n=0 and c_n=1. G61's odd-to-even equation forces s_(n+1)=0. Therefore

    x(1,2n)*x(2,2n)=1 implies (s_n,s_(n+1))=(1,0).

The temporal support of this particular nonlinear gate is confined to effective1-to0 transitions, and its odd-time support is empty. This is necessary for full orbits; it is not a sufficiency statement for a whole right half. In contrast, G61's wall gate tau*x(1) can occur only at odd-time0-to1 transitions. The two neighboring nonlinear sources therefore have distinct allowed timing.

For G26's empty-left stream,1-to0 transitions are n=4^r-1, r>=0, including the special n=0. Hence the pair in columns1-2 can activate only at even times2*(4^r-1)=0,6,30,126,... . The wall's allowed gate times remain4^(r+1)-1=3,15,63,... . These are possible times, not a claim that every such gate fires. G60's fully parity-sparse realization fires neither.

**Unexpected guard.** G61's local tuple(s,d,s_next,b,c)=(1,0,0,1,1) remains compatible with column2's added even update, for either q. Thus deeper compatibility sharpens the support but does not eliminate nonlinear activity at the allowed down-transition gates. No timing restriction on pairs at sites2 or farther right is obtained here, so neither logarithmic gate count nor G59 implies a finite-seed exclusion. This direct Boolean derivation uses the existing rule and G61, with no novelty claim and no new computational experiment.

**Next bounded control, preregistered NOT RUN.** NG1: enumerate all32 initial positive patches(s,b,q,h,z)=x(1..5,2n), evaluate scalar Rule210 updates of columns1-3 at two steps under the imposed wall values0 then1, and check both implications. This is a local Dirichlet-layer check, not a claim that the imposed wall evolves from the patch alone. Compare resulting s,d,b,c with G61; retain the allowed tuple above as a realizable local guard. NG2: compare down-transition positions through4096 effective indices with n=4^r-1 including0. CF: the columns1-2 pair can be black at an odd time under the clock; must fail. A local two-step patch is not an infinite full clock or a finite witness. Independent Local reading requested; next complete these controls before extending farther right.


### G62 controls outcome (2026-10-06)

NG1 passes all32 positive five-cell Dirichlet patches through the two specified updates. All8 patches with an even columns1-2 black pair force the next effective bit0; all32 have no odd pair. The allowed even-pair guard survives in8 patches. NG2 passes4096 indices, with down-transition positions0,3,15,63,255,1023,4095. The odd-pair counterfactual is refuted. Probe: `tests/probes/lexicon/rule30_gpt_pair_support.py`, Python on GPT's Intel host, under1 s.

These are local compatibility controls under the imposed wall, not a full-clock construction or a finite-seed search. No control failed. G62 remains awaiting an independent reader. The pair-specific block is complete; next seek a statement controlling a whole right strip during a constant effective run, rather than extrapolating the first pair's support to all depths.


## G63. A constant effective run forces a right strip (2026-10-06)

Question from G037: can G61-G62's individual gate restrictions be replaced by a strip statement? The following local extension lemma does so. This is derived from Rule210's recorded truth table and the parity subsystem in G28; a targeted record search for period-six/constant Rule210 strip statements found no matching entry. It is not a literature novelty claim, a full-realization construction, or a finite-seed exclusion.

**Local extension lemma.** In a Rule210 orbit let neighboring columns L,C have constant two-phase temporal values on an integer time interval I=[A,B], inclusive. Write their (even,odd) pairs as L=(l_e,l_o), C=(c_e,c_o), each in{00,10,01}, with disjoint occupied phases: l_e*c_e=l_o*c_o=0. Then the next column R is forced on[A+2,B-2] to the pair

    R=(c_o XOR l_e, c_e XOR l_o).

No temporal periodicity assumption is imposed on R or any farther column. If C=00, its own update gives R(t)=L(t), using C(t+1)=0, and the formula follows. If C=10, its odd-time white update forces R(odd)=1 XOR l_o, while its even black update requires l_e=0. Put b=1 XOR l_o. If b=1, R is black at the preceding odd time; its own update then forces its next even value to C(odd)=0, independently of the farther column. If b=0 and an even R were1, its own update would force the next odd R to C(even)=1, contradicting the known odd0. Thus R(even)=0 in either case. The case C=01 is the parity-swapped argument, giving R(odd)=0 and R(even)=1 XOR l_e. Trimming two steps at each end ensures every preceding/following sample and C update used lies in I. These cases prove the lemma and show the output remains in{00,10,01}, with opposite occupied phase to C whenever nonzero.

**Strip corollary for0101.** Suppose s_n=x(1,2n)=a is constant for m<=n<=N. G61 forces d_n=x(1,2n+1)=0 for m<=n<N, since a constant transition is not0-to1. Thus columns0 and1 have pairs v_0=01, v_1=(a,0) on[2m,2N]. Iterating the lemma gives, for every k>=1 with a nonempty specified window,

    column k has pair v_k on
    [2m+2*(k-1), 2N-2*(k-1)],
    v_(k+1)=swap(v_k) XOR v_(k-1).

The vectors repeat spatially with period6. For a=0, v_0..v_5 are01,00,01,10,00,10; for a=1 they are01,10,00,10,01,00. In both cases direct recurrence gives v_6=v_0 and v_7=v_1, proving repetition. Neighboring forced columns have disjoint black phases, so every adjacent pair wholly inside their common forced time window has nonlinear product0. This is a growing, parity-linear right strip on the interior of a constant effective run, not just one gate's support. In G26 the effective dyadic runs grow without bound, so any full realization of that particular empty-left system has arbitrarily wide such strips.

**Unexpected boundary guard.** Dropping the temporal margin is unjustified. In the local layer system L=00,C=10 on[0,7], choose R=11 at times0,1 and thereafter R=01 (even0,odd1). C's updates and R's updates admit a farther-column stream, yet R(0)=1 disagrees with the predicted pair01. The preceding odd sample outside the interval is missing. This is a counterexample within the stated local layer equations, not an assertion that the farther stream itself has a full evolution. It shows why the lemma's proof must retain its time-window premises. The two-step margin is conservative; no optimality claim.

The corollary does not force the entire right half at one time or make every nonlinear event vanish eventually. Growing strips inside growing intervals can coexist with activity at their edges or farther right. G59 therefore still supplies no finite-seed contradiction. Full mixed-parity finite witnesses remain open.

**Next controls, preregistered NOT RUN.** ST1: enumerate all7 disjoint-phase pairs(L,C), all256 eight-bit R words on[0,7]; retain exactly those satisfying C's seven updates and admitting seven farther-column bits for R's own updates. Every accepted R must match the lemma on[2,5]. ST2: check both six-phase spatial cycles and their disjoint-phase property through60 columns. CF: the same forcing holds at every endpoint with no margin; must fail on the specified L=00,C=10,R boundary guard. These are local controls, not finite/full orbit searches. Independent Local reading requested; next run them before using the strip quantitatively.


### G63 controls outcome (2026-10-06)

ST1 passes all7 disjoint-phase pairs and1792 candidate eight-bit right words; exactly15 words admit both layers' specified updates, and all15 agree with the predicted trace at times2..5. ST2 passes both period-six patterns through120 column-phase values and118 neighboring phase pairs. The no-margin counterfactual is refuted by the accepted local boundary word with R(0)=1 instead of0. Probe: `tests/probes/lexicon/rule30_gpt_strip.py`, Python on GPT's Intel host, under1 s. No control failed.

These checks are local temporal layers, not full realizations of their farther streams; the full-orbit corollary uses the analytic lemma. G63 remains awaiting Local's independent reading. The bounded strip control block is complete. Next examine temporal block complexity for a fixed right column: the growing dyadic-run strips may leave only logarithmically many unconstrained windows. Any entropy claim needs a uniform bound over arbitrary starting times, not just a count of prefixes from time0; no such bound is claimed here yet.


## G64. Fixed right columns have zero temporal word-count entropy (2026-10-06)

Use G63's strip lemma for all full Rule210 realizations of the0101 wall with the empty initial left row of G26. This class is nonempty by G60; the right half may be infinite or mixed-parity. For each fixed column k>=1 let P_k(N) count all distinct length-N temporal words, across all such realizations and all starting times u>=0. Then

    P_k(N)=O_k(N^(4k+2)),
    limsup as N->infinity of log2(P_k(N))/N=0.

This extends G26's factor-count observation for one particular adjacent stream to every fixed right column in this precisely specified family. It is not a Rule30 theorem, an assertion of zero entropy for the whole CA, or an exclusion of finite mixed-parity witnesses. The constant and exponent depend on k.

**Forced positions.** The effective stream changes across odd times in B={2^j-1:j>=1}; include a virtual boundary-1 for the start of time. G63 forces column k to its known two-phase template except within distance2k of these boundaries. Indeed each constant effective run spans even endpoints[2m,2N]; the lemma trims2(k-1) at each end, and the intervening odd transition time is in B. Every omitted sample is inside the asserted radius; choosing2k is conservative. Outside those neighborhoods the template depends only on the effective run's value, the time parity and k modulo6.

**Uniform word bound.** Fix N,k, set r=2k, L=N+2r and choose M to be the least power of2 with M>=L+1. Thus M<2(L+1). For early starts0<=u<M+r, the enlarged window[u-r,u+N-1+r] ends before2M-1. It contains at most Q=log2(M)+1 boundaries, counting the virtual-1. The unconstrained samples in the word are at most(2r+1)Q. At a fixed start the forced template is already known, so early starts contribute at most

    (M+r)*2^((2r+1)*Q).

For late starts u>=M+r, the enlarged window begins at least M. Consecutive boundaries there are separated by at least2M>L, so it contains at most one. Allow its relative position any of L integer positions, or allow no boundary; choose either effective value independently on each side and either time parity, at most8 template choices. Allow all2r+1 boundary-neighborhood bits arbitrary. Late words contribute at most

    8*(L+1)*2^(2r+1).

These bounds count a superset, including choices that need not have a full realization. Their sum bounds P_k(N). Since 2^((2r+1)Q)=2^(2r+1)*M^(2r+1), it is O_k(N^(2r+2))=O_k(N^(4k+2)). Taking log and dividing by N proves the entropy statement uniformly over starting times. Column0 separately has at most2 words of every length. No finite measurements are used in the all-length proof.

**Unexpected guard: prefix density is insufficient.** Concatenate lists containing every binary word of length m, separated by zero blocks of length2^(2^m). Their black prefix density tends to0, since the previous zero block eventually dwarfs the next list of size O(m*2^m). Yet every binary word occurs, so temporal factor complexity is2^N and entropy1. This illustrates why the arbitrary-start late-window argument is necessary; a sparse prefix count alone would not prove G64. It is a constructed binary-sequence counterexample, not a Rule210 realization.

This is elementary counting from G26/G63 and the explicitly defined word-count entropy, with no literature novelty claim. Earlier G53/G54 bounds concern another family and do not supply the dyadic transition hypothesis here. G63 and this consequence await Local's independent reading. No uniform-in-k or initial-condition-wide conclusion is made.

**Next controls, preregistered NOT RUN.** WC1: k=1..6,N in{1,2,4,8,16,32,64,128}, every start0..4095; directly enumerate enlarged-window boundaries and marked sample positions, checking the early Q bound and late one-boundary bound. WC2: on G60's explicit0101 full realization, compare columns1..6 through time500 with G63's templates at every sample outside the stated boundary neighborhoods, using an independent scalar full evolution. CF: prefix sparsity implies zero factor entropy; refuted analytically by the concatenated-word construction above, without an empirical entropy estimate. These controls validate margins and counting instrumentation, not the entropy limit itself.


### G64 controls outcome (2026-10-06)

WC1 passes196608 windows for k=1..6, lengths1,2,4,8,16,32,64,128 and every start0..4095:3952 early windows obey Q and marked-sample bounds;192656 late windows obey the one-boundary and radius bounds. WC2 passes2524 forced samples of columns1..6 through time500 on G60's explicit scalar full Rule210 realization;482 samples are excluded by the conservative neighborhoods. Probe: `tests/probes/lexicon/rule30_gpt_window_complexity.py`, Python on GPT's Intel host, under1 s. No control failed.

These finite checks validate the counting split and forcing margins; the entropy limit remains the analytic G64 proof, not an empirical estimate. The concatenated-word counterfactual is retained as an analytic counterexample. Independent reading remains queued. This bounded block is complete; next audit the effect of varying initial left support, since G27's arbitrary finite visible prefixes warn against treating one fixed empty-left family as the union of all finite-left families.


## G65. Mirror extension and the varying-left-row quantifier (2026-10-06)

Scope audit following G041, using G27's finite-prefix continuation and G60's triangular full realization. Fix tau=0101. Let h_j be G60's initial right bit at site2j+1 for the empty-left system. Prescribe any finite initial left row supported on odd depths, with e_j at site-(2j+1), and define the initial right row by

    v_j=h_j XOR e_j,

with every positive even site and the centre0. This gives a full Rule210 realization of the same clock and the prescribed left row. Its right support is infinite, since h has infinite support and e is finite. It is not a finite global witness.

Proof. The entire initial configuration has odd spatial support, so its Rule210 orbit agrees with Rule90. Relative to G60, the added configuration has the same bit e_j at the reflected sites plus/minus(2j+1). In the Rule90 expansion at the centre, those two sites have equal binomial coefficients at every time (the two coefficients are symmetric), so their contributions cancel over GF(2). Thus the wall stays0101 for all time. Equivalently the odd-time triangular equation depends on v_j XOR e_j; setting this to h_j preserves every equation. No linearity claim is made outside the global parity-sparse subsystem. The full left evolution is the unique Dirichlet evolution with that row and wall, hence matches G27's compatible left construction. This proves full infinite-right extension for every finite odd-supported left row, not only for the empty row.

**Exact language count after varying the row.** Restrict to these globally parity-sparse full realizations while allowing every finite odd-supported initial left row. In column1 every odd-time bit is0. By G27's continuation corollary, every length-n even-time word occurs: choose its finite left row (support at most2n-1) and apply the mirror extension above. Thus length-N temporal factors, across all realizations and all start times, are exactly the binary words with zeros on one of their two alternating position classes. Either class is realized by choosing a sufficiently long even-time prefix and a start of parity0 or1. Their intersection contains only the all-zero word. Therefore

    P(N)=2^ceil(N/2)+2^floor(N/2)-1,
    lim as N->infinity of log2(P(N))/N=1/2.

This is entropy of the union's temporal language. It does not assert that any one orbit has entropy1/2, or that every fixed nonempty initial left row has zero entropy. G64 proved zero for one fixed empty-left family, including its potentially nonlinear right realizations. Removing the fixed-row hypothesis already gives entropy at least1/2 in the broader family, because the parity-sparse subfamily above realizes these factors. No exact entropy is asserted for the broader mixed-parity family.

**Unexpected domain guard.** Reflected additions do not automatically cancel in Rule210 outside the parity subsystem. From the finite initial seed{1}, the centre at time2 is0. Adding the reflected even sites{-2,2} gives seed{-2,1,2}, whose centre at time1 is1, left neighbor1 and right neighbor0; Rule210 then gives centre1 at time2. Thus the centre changes, despite the mirrored addition. This is an analytic truth-table counterexample to importing Rule90 superposition into mixed-parity Rule210. It is not a clock witness or an experiment.

This synthesizes already recorded G27/G60 with the elementary binomial symmetry; no novelty claim or new prior-art theorem. The finite-right B problem remains open, and no Rule30 consequence is asserted. New details await Local's independent reading.

**Next controls, preregistered NOT RUN.** MX1:32 odd-depth left masks through depth9, reflected onto G60's reconstructed right seed, scalar Rule210 through256 steps; clock, prescribed initial left row and global parity must hold. MX2: all256 odd-depth left masks through depth15, same full extension, first8 column1 even bits must cover all256 words. Compare the two-phase temporal factor count for lengths1..8 against the exact formula above using those finite prefixes. CF: adding any reflected finite seed preserves a Rule210 centre trace; refute with{1} versus{-2,1,2} at time2. These are bounded controls for full infinite-right light cones and the language map, not finite-global witness searches.


### G65 controls outcome (2026-10-06)

MX1 passes32 left masks/8224 clock and parity time checks through256 steps. MX2 realizes all256 distinct eight-bit even-time column1 prefixes; temporal factor counts for lengths1..8 are2,3,5,7,11,15,23,31, matching the exact formula. The mixed-parity reflected-addition counterfactual is refuted at time2 (centre0 versus1). Probe: `tests/probes/lexicon/rule30_gpt_mirror.py`, Python on GPT's Intel host, under1 s. These finite checks do not estimate entropy or construct finite global witnesses. No control failed. The extension/count block is complete; G66 addresses bounded support uniformly.


## G66. Bounded left support retains zero fixed-column entropy (2026-10-06)

Complete G65's quantifier audit. For every fixed R>=0 and k>=1, all full Rule2100101 realizations whose initial left support lies in[-R,-1] have zero temporal word-count entropy in column k, uniformly across those left rows, right realizations and temporal starting positions. An infinite right half is allowed. The bound depends on R,k. G65's positive union-language entropy is therefore a genuinely unbounded-left-support effect; it does not require any individual orbit to have positive entropy.

**A finite Rule90 trace is localized near powers of two.** Let E be any finite initial row supported in[-R,R], and A=S+S^(-1) over GF(2). If 2^q<=t<2^(q+1), the Frobenius identity gives

    A^t=product over b with the b-th bit of t=1 of
        (S^(2^b)+S^(-2^b)).

Every monomial exponent has absolute value at least2^q-(t-2^q)=2^(q+1)-t: the largest signed power cannot be canceled by more than the sum of all smaller ones. Thus (A^t E)(i)=0 whenever2^(q+1)-t>R+abs(i). No assertion that all remaining times are nonzero is made. This is a direct shift-polynomial bound, not a new prior-art theorem.

**Apply it to the left perturbation.** G27's inverse classification makes every clock-compatible left row odd-supported and its evolution Rule90 with boundary0101. Compare a row e supported in[-R,-1] with the empty-left evolution. Their difference has zero boundary and evolves linearly. Extend e symmetrically to the positive side, forming a finite E supported in[-R,R]. Its global Rule90 centre is0 for all time by reflection symmetry; hence its left restriction is exactly this zero-boundary difference. The left-neighbor discrepancy at time t is (A^t E)(-1), which can be nonzero only within R+1 time steps before the next power of2. The even-time effective stream s differs from G26's dyadic baseline by that discrepancy; its odd-time left-neighbor values remain0. At t=0 any discrepancy is handled by the initial boundary margin.

Let B={-1} union{2^j-1:j>=1}. Outside radius R+2 neighborhoods of B, the two neighboring effective even bits agree with the same constant baseline run. G61 then forces the intervening odd-time column1 bit0. Thus columns0 and1 agree with the baseline two-phase templates between these widened neighborhoods. Applying G63 iteratively shows column k agrees with the baseline spatial-period-six template outside radius

    r=R+2k+4

of B. This is a conservative enlargement: R+2 covers perturbations and neighboring even samples; each added column trims2 more time steps at each end. Activity inside these neighborhoods or farther right is not excluded.

**Uniform counting.** Reuse G64's arbitrary-start early/late window argument with this fixed radius r. With L=N+2r, M the least power of2 at least L+1, Q=log2(M)+1, the combined family has

    P_(R,k)(N) <= (M+r)*2^((2r+1)*Q)
                  +8*(L+1)*2^(2r+1)
               =O_(R,k)(N^(2r+2)).

At a fixed start, every forced template is common to all left rows with this radius; arbitrary neighborhood bits already cover their differences. The bound is uniform over starting times and right realizations. Its logarithm divided by N tends to0. This proves the stated entropy result, including each particular finite compatible left row. It does not give a uniform bound as R or k grows with N.

**Unexpected quantifier guard.** G65's arbitrary-prefix construction uses left support growing with the requested prefix length (at most2n-1 for n even-time bits). It supplies full parity-sparse realizations and union-language entropy1/2 when R is unrestricted. Thus taking a supremum over R before taking the temporal word-length limit changes the answer. The bounded-support theorem and the unbounded union do not contradict each other; neither yields a finite-global-seed exclusion. No Rule30 transfer is asserted.

No experiment ran for this new lemma. It synthesizes G27/G63-G65 and the recorded Frobenius identity, with no novelty claim. Independent Local reading requested.

**Next controls, preregistered NOT RUN.** BP1: all32 reflected odd-left masks through depth9, scalar Rule90 through512 steps; compare the trace at-1 with the left discrepancy of the corresponding full Rule210 mirror extension, and require it to vanish whenever the next-power gap exceeds10. BP2: for the same full realizations, columns1..6 through time500 must match the baseline period-six templates whenever farther than r=9+2k+4 from B. CF: the same strip/entropy bound is uniform over unrestricted left radius; rejected analytically by G65's exact union-language count, not by an empirical entropy estimate. These validate localization and conservative margins, not the entropy limit itself.


### G66 controls outcome (2026-10-06)

BP1 passes16416 left-neighbor discrepancy comparisons through512 steps for32 reflected odd-left masks, including14304 checks that the trace vanishes when the next-power gap exceeds10. BP2 passes62432 forced samples through time500 on columns1..6;33760 samples are excluded by the conservative radius9+2k+4. Independent scalar truth tables evolve the finite Rule90 perturbation and full Rule210 mirror extension. Probe: `tests/probes/lexicon/rule30_gpt_bounded_perturbation.py`, Python on GPT's Intel host, seconds.

No control failed. Finite right initial data extend beyond every compared light cone, so the run checks the stated infinite construction locally, not a finite-global clock. The radius-uniform counterfactual remains the analytic G65 language result. G66's entropy limit is analytic and awaits independent reading. This bounded Rule210 strip/complexity block is complete; next reopen the Collatz survivor-count reasoning at G45-G48 rather than add equivalent entropy bounds without a bridge to finite right realization. No Collatz experiment starts in this checkpoint.


## G67. The maximal affine offset at a first coefficient deficit (2026-10-06)

Return to the open Collatz survivor count, without extending G48's horizon census. The [Rozier–Terracol primary source, Definition1.2](https://arxiv.org/html/2502.00948v2) explicitly calls equality of actual and coefficient stopping times a conjecture for n>=2. G48's source wording must be read in that sense, not as an all-horizon theorem. Its Lemma2.1/Theorem2.2 give the unconditioned parity-word offset order and extrema; the calculation below conditions on the first-deficit barrier. No novelty claim.

Fix a first coefficient-deficit word with a>=1 ones and length t. Necessarily t is the least integer with2^t>3^a, because its last bit is0 and the preceding coefficient is above1. Write p_i for the position of its(i+1)-st1, indexed from0. Then

    p_0=0,
    p_i<=floor(i*log2(3)) for1<=i<a,
    B=sum over i=0..a-1 of 3^(a-1-i)*2^p_i.

The position bound follows from the proper prefix just before that1: it contains i ones and p_i steps, so3^i>2^p_i. Irrationality of log2(3) converts this to the stated floor. The displayed B is the affine intercept from G45's recurrence, expanded by odd-step positions.

All maximal positions can be attained simultaneously. Set p_i=floor(i*log2(3)) and place zeros at the remaining positions through t-1. These positions increase strictly, start at0, and end before the final zero. Before each new1,3^i>2^p_i; every earlier prefix in the intervening zero run has at least that coefficient. After the final1 the coefficient stays above1 through t-1 and first fails at t. Thus this is an admissible first-deficit word. Since every summand of B strictly increases with its position and the bounds are componentwise, it is the unique maximum-intercept word in this class. Define

    B_max(a)=sum over i=0..a-1 of
             3^(a-1-i)*2^floor(i*log2(3)).

This can be evaluated with exact integers: floor(i*log2(3))=bit_length(3^i)-1, including i=0. No floating-point logarithm is needed.

Dividing by3^a gives(1/3)*sum_i 2^(-fractional_part(i*log2(3))). Hence

    a*3^a/6 < B_max(a) <= a*3^a/3,

with equality in the upper bound only at a=1. In particular every first-deficit word's formal G45 ceiling is bounded by

    K_w <= floor(B_max(a)/(2^t-3^a)),

and this maximum ceiling is attained by the maximum-intercept word, though rounding need not make its maximizer unique. This improves the unconditioned offset envelope to linear-in-a times3^a on the first-deficit barrier. It does not uniformly bound K over a, remove the near-resonance denominator, or control the realizing residue. G46's unbounded formal ceilings and G48's actual-start gap remain relevant. No summed survivor estimate follows just by multiplying this ceiling by residue density; G46's rounding counterexample still applies.

**Unexpected conditioning guard.** For a=2,t=4, the barrier maximizer is1100 with B=5. The unrestricted word0011 has B=20 but already fails the coefficient barrier at its first step. Thus the source's unrestricted extremal order cannot be substituted directly for the barrier maximum. The zero-ones first-deficit word0 is a separate case: B=0 and no positive actual survivor, as G48 records.

No experiment has run for this envelope. Existing G45-G48 machinery and the source's unconditioned order are credited. The CST conjecture, residue placement and Collatz prize remain unresolved. Independent Local reading requested.

**Next controls, preregistered NOT RUN.** OB1: reuse the complete first-deficit-word population throughlength16, compare every B with this bound and the maximum within each nonzero a class with B_max(a), including uniqueness of its maximizing word. OB2: a=1..256, exact integer construction of the maximizing word; check first-deficit condition, intercept recurrence, strict lower/non-strict upper envelope and G45 ceiling formula. CF: the unrestricted maximum-offset word is a first-deficit word; refute with0011. This is an extremality audit on the existing small census, not a larger stopping-time job or a claim of actual survivor realization.


### G67 controls outcome (2026-10-06)

OB1 passes all791 first-deficit words throughlength16, including the separate zero-ones word. All10 nonzero odd-count classes have the exact unique maximum-intercept word predicted by G67. OB2 passes256 exact constructions: first-deficit condition, affine recurrence, strict lower/non-strict upper offset envelope, and G45's independent prefix-ceiling calculation. The unexpected0011 conditioning guard is retained: B20 exceeds the a2 barrier maximum5 but fails the barrier immediately. Probe: `tests/probes/prizes/collatz_gpt_barrier_offset.py`; Python on GPT's Intel host, under1 s. No control failed. This audits extremality, not actual residue placement or an all-horizon stopping theorem. Independent proof review remains pending.

**Next residue controls, preregistered NOT RUN.** RB1: reuse exactly G48's first-deficit words throughlength16 and compare, within each odd-count class, the word maximizing B with words maximizing the terminal gap g=q-r of the least nonnegative realizing residue. Prediction: maximizing formal B need not maximize g; retain every mismatch, and any class where it does. RB2: for G67's256 exact extremizers, predict that only a=1 has a positive actual surviving lift; test r against K, including r=0's positive-domain lower lift, and independently evolve any claimed surviving lift. This finite prediction is not an all-a theorem. Unexpected check: the counterfactual that extremal B orders actual gaps must be tested directly rather than inferred from the offset bound. No census horizon increase or large computational job is proposed.

### G67 residue controls outcome (2026-10-06)

RB1 passes its prediction on the same791 first-deficit words throughlength16. Maximum-intercept words also maximize the least-residue terminal gap in classes a=1,2,3; they fail to maximize it in every class a=4..10. Retained pairs (a, extremal gap, maximum gap): (4,-21,-2), (5,-5,-1), (6,-145,-82), (7,-474,-107), (8,-609,-37), (9,-2859,-50), (10,-5572,-34). These are finite class maxima, not bounds for larger a.

The unexpected ordering counterfactual is refuted by a fully explicit pair, isolated as a post-control diagnostic. Both words below have a4,t7,D=47 and are first-deficit:

| Word | Offset B | Least residue r | Terminal q | Gap q-r |
| --- | --- | --- | --- | --- |
| 1101100 | 85 | 59 | 38 | -21 |
| 1110100 | 73 | 7 | 5 | -2 |

Their integer trajectories are respectively59,89,134,67,101,152,76,38 and7,11,17,26,13,20,10,5. They have the same formal ceiling K=1, but neither residue lies below it. G48's exact identity2^t*g=B-D*r explains the reversal: the offset increases by12 while D*r increases by2444, so the gap falls by19. Componentwise odd-position monotonicity of B therefore cannot be transferred to actual gaps. The counterexample is exact arithmetic, not a statistical inference.

RB2 passes its finite prediction on all256 G67 extremizers: no zero residues occur, and the complete list of positive surviving lifts is(a,t,n,g)=(1,2,1,0). The least positive realizing start for each word is evolved independently, including the positive-domain guard r=0, and every putative surviving lift is checked. The identity linking intercept, residue and gap is also verified. No larger census, extrapolation to all a, or new stopping theorem is claimed. Probe: `tests/probes/prizes/collatz_gpt_barrier_residue.py`; Python on GPT's Intel host, under1 s. No control failed; all mismatches predicted by RB1 are retained.

This completes the finite extremality audit. Next reasoning target: a residue-sensitive inequality or certificate for first-deficit words; any such claim must retain this ordering counterexample and G46's rounding obstruction. Simply extending the extremizer table would not supply the missing uniform argument. No new experiment is registered or launched in this checkpoint.

## G68. Two endpoint ceilings and nested digit exclusion certificates (2026-10-06)

Continue G67's residue-sensitive audit. This is an elementary consequence of G45/G48 and Local's least-terminal-residue lemma in COLLATZ-PRIZE.md §4, not a new distribution theorem or a novelty claim. G67's ordering counterexample and G46's rounding obstruction remain controls.

Let w be a first coefficient-deficit word of length t with a>=1 ones, M=2^t, A=3^a, D=M-A>0 and affine intercept B. Put K=floor(B/D). Its least realizing start is r in[0,M-1] and its least terminal value is y=T^t(r) in[0,A-1], with

    M*y=A*r+B.

Both r,y are positive: a word with at least one odd step cannot be the itinerary of0, and T preserves positive integers. Every positive realizing lift is n=r+M*m, with terminal q=y+A*m and m>=0. Every proper prefix has coefficient greater than1 and nonnegative intercept, so actual survival through t is equivalent to q>=n at the final step alone. The affine relation gives two forms of the gap:

    q-n=(B-D*n)/M=(B-D*q)/A.

Consequently q>=n iff n<=K iff q<=K. Thus start and terminal have exactly the same ceiling, despite different moduli. The two exact lift counts agree:

    max(0,1+floor((K-r)/M))
      =max(0,1+floor((K-y)/A)).

This is an identity of the same lift parameter m, not an independence assertion. The a0 word0 is separate, with no positive survivor.

**Partial digit certificates.** A prefix u of length s has intercept C_u and odd count a_u. Every realizing positive n satisfies

    n = -C_u*3^(-a_u) mod2^s.

A suffix v of length ell with b ones and intercept C_v satisfies2^ell*q=3^b*x+C_v for the intermediate integer x, so every positive terminal q satisfies

    q=C_v*2^(-ell) mod3^b.

Inverses exist in the indicated moduli; with s=0 or b=0, modulus1 is interpreted as the sole residue0. For a residue rho modulo H define its least positive representative L_H(rho)=rho if rho>0, and H otherwise. If either the prefix representative or suffix representative exceeds K, the full word has no positive actual survivor. This gives independently checkable exclusion certificates without assuming uniform residues or multiplying densities. It uses the exact full-word ceiling; no efficient method to sum such certificates over all words is proved here.

These lower bounds are nested as information increases. Each longer prefix has the same residue modulo the shorter power of2. Each longer suffix has the same terminal residue modulo the shorter power of3; this also follows directly by reducing its affine identity. The positive representatives therefore cannot decrease. At full prefix or full suffix length the tests are individually complete, giving r>K or y>K. Before full length, passing either or both is only absence of an exclusion certificate.

**Unexpected sufficiency guard.** The first-deficit word1101100 has K1,r59,y38 by G67. Its one-bit prefix1 permits positive start1, and its two-bit suffix00 has b0 and permits positive terminal1. Both partial lower bounds equal K, yet the full word has no positive survivor. Thus passing two partial endpoint tests is not a survival theorem. This analytic counterexample is deliberately retained alongside the stronger tests; no computational experiment was needed to derive it.

The unresolved task is an arithmetic bound on how many barrier words escape short endpoint certificates, with rounding retained. The lemma changes the available certificates, not the known all-horizon stopping status. Independent Local reading requested.

**Next controls, preregistered NOT RUN.** EC1: exactly the existing791 first-deficit words throughlength16, check the terminal formula and equality of both lift counts; independently evolve all claimed surviving positive lifts. EC2: for every prefix/suffix length of every nonzero-a word in that population, check the two congruences, nested positive lower bounds, sound exclusion and completeness at full length. Record minimal binary-prefix and ternary-suffix certificate lengths for the256 G67 extremizers; predict all a2..256 have both full certificates, while a1 has none. No short-depth asymptotic prediction or new horizon. Counterfactual: passing two partial endpoint tests suffices for survival; must fail on1101100 with prefix1 and suffix00. This is a bounded instrument audit and keeps Local's computational lane free.


### G68 controls outcome (2026-10-06)

EC1 passes791 first-deficit words throughlength16: both endpoint lift counts agree on all791, with one positive surviving lift independently evolved (the known n1 return). EC2 passes25358 prefix/suffix endpoint congruence checks, including monotone positive representatives, sound exclusions and full-length completeness. The a0 word is separately checked to have no positive survivor. The unexpected partial-sufficiency counterfactual fails on1101100 exactly as predicted.

All255 G67 extremizers with a2..256 admit both certificates; a1 admits neither. Minimal prefix-length frequencies (length:count) are0:1,2:2,4:15,5:32,6:57,7:68,8:35,9:24,10:11,12:6,13:2,15:2. Minimal suffix-length frequencies are0:1,3:2,5:2,6:7,7:21,8:35,9:87,10:62,11:11,13:23,15:2,18:2. Zero-depth exclusion is the a2 word, whose ceiling is0; it does not imply a zero-length word or a nontrivial residue constraint.

Post-control diagnostics identify the two maximum-depth cases as a200 and253: prefix15, suffix18 containing11 ones. The largest sampled ceiling is19584 at a253. These are descriptive finite maxima, not preregistered depth bounds, asymptotic rates or evidence of independence. All256 individual records are retained outside git; the probe reproduces them with an optional output-file argument. Probe: `tests/probes/prizes/collatz_gpt_endpoint_certificates.py`; Python on GPT's Intel host, about6 s. No control failed.

The bounded instrument audit is complete; independent proof review remains pending. Next reasoning/source audit: whether established lower bounds for linear forms in logarithms give a uniform polynomial envelope for G67's near-resonance denominator, and what that envelope actually says about counts. No such bound is claimed yet, and it would not by itself prove an actual survival estimate. No larger census or additional run is started here.

## G69. Known logarithmic bounds give a polynomial first-deficit ceiling (2026-10-06)

G67's ceiling is unbounded, but it has a uniform polynomial envelope in the deficit time. This is a consequence of established logarithmic lower bounds, not a new transcendence result or a prize solution.

**Source and hypotheses.** [Rozier–Terracol arXiv:2502.00948v3, Proposition6.3](https://arxiv.org/html/2502.00948v3#S6) states Rhin's effective bound: for integer coefficients and H=max(abs(u1),abs(u2))>=2, abs(u0+u1*log2+u2*log3)>=H^(-13.3). Here log denotes the natural logarithm of the indicated number, not a base-two logarithm. Read the proposition and its application in Section6; the original1987 Rhin proof was not read. Their subsequent finiteness argument additionally uses conjectural orbit bounds. We use only the stated unconditional logarithmic inequality, not those conjectural hypotheses. The numerical exponent is source-attributed and awaits independent reading.

For a first-deficit word with a>=1 ones and t=ceil(a*log2(3)), let A=3^a, D=2^t-A, and

    lambda=t*ln(2)-a*ln(3)>0.

Since t>=2 and t>a, the cited bound applies with u0=0,u1=t,u2=-a,H=t. Thus

    D/A=exp(lambda)-1>lambda>=t^(-13.3).

G67 gives B<=a*A/3 for every word in this barrier class, so

    K=floor(B/D)<a*t^13.3/3<t^14.3/3.

The zero-ones first-deficit word has no positive survivor. Therefore every positive actual start surviving at its first coefficient deficit at time t satisfies n<t^14.3/3. Its positive terminal value obeys the same bound by G68. The displayed inequality is strict because exp(lambda)-1>lambda.

**A limited count consequence.** Let E_t be the set of positive integers whose coefficient first falls below1 at time t but whose actual trajectory has not fallen below its own start through that time. Every member lies in the same interval[1,t^14.3/3), irrespective of which parity word realizes it. Hence

    abs(E_t)<=floor(t^14.3/3)<=floor(t^15/3),
    abs(E_t intersection[1,2^t])/2^t<=t^14.3/(3*2^t)->0.

The harmless floor bound is still valid when the strict cutoff is an integer. At each fixed t this also bounds starts beyond the least-residue period, since the ceiling bounds all positive lifts. No independence or residue-density multiplication is used. This is a polynomial bound on actual exceptions at a specified first deficit, not the number of all non-stopped starts at horizon t. Summing polynomial bounds over unbounded t gives no finite total. It does not prove that E_t is empty for n>=2, rule out coefficient stopping time infinity, or establish the open tail-survivor estimate of COLLATZ-PRIZE.md §1.

**Independent weaker source route.** [Languasco–Luca–Moree–Togbé, Theorem2.1](https://link.springer.com/article/10.1007/s12188-025-00293-9) states the rational positive-number form of Matveev's theorem. With numbers2,3 and exponents t,-a, it gives D/A>(e*t)^(-C), where C=1.4*30^5*2^(9/2)*ln(2)*ln(3). Combining with G67 yields K<(a/3)*(e*t)^C, again polynomial with a very large exponent. Its theorem hypotheses and application to prime-power gaps were read. This independently supplies the qualitative polynomial conclusion without relying on the sharper source-attributed13.3 exponent. Neither underlying logarithmic proof has been reproduced here.

**Unexpected scope guard.** At horizon1 all positive odd starts have T(n)=(3n+1)/2>=n and coefficient3/2>1. This is an unbounded set of actual survivors. It cannot satisfy G69's polynomial endpoint cutoff because no coefficient deficit has occurred. Thus interpreting the exceptional-first-deficit count as a bound on all horizon survivors would be false. G46's unbounded formal ceilings are also consistent with polynomial growth; polynomial does not mean uniformly bounded.

**Next controls, preregistered NOT RUN.** LF1: a1..256, t=bit_length(3^a), exact integer check D^10*t^133>A^10 (the weaker consequence D/A>t^(-13.3)), and K^10*3^10<a^10*t^133 for G67's maximum ceiling. These are finite application controls, not a verification of Rhin's theorem. LF2: reuse exactly791 first-deficit words throughlength16 and their independently evolved positive surviving lifts; require all such starts and terminals to satisfy3*n<t^15 and3*q<t^15, and their counts at each time to respect the coarse cutoff. No larger census. Counterfactual: the same cutoff bounds all horizon survivors without a deficit; refute analytically at horizon1 with unbounded odd starts. Independent proof/source reading requested.


### G69 controls outcome (2026-10-06)

LF1 passes256 exact integer denominator and maximum-ceiling inequalities; no floating logarithms or fractional powers were used. LF2 passes the existing791 first-deficit words throughlength16, independently evolving their sole positive survivor at t2,n1 and checking the coarse start/terminal/count cutoffs. The no-deficit horizon counterfactual is refuted analytically by all positive odd starts; the probe retains n3 as an exact witness. Probe: `tests/probes/prizes/collatz_gpt_logarithmic_ceiling.py`; Python on GPT's Intel host, under1 s. No control failed. These validate finite applications, not the deep logarithmic theorem. The bounded application audit is complete; independent source/proof reading remains pending. G70 records the finite-horizon count consequence separately.

## G70. Polynomial additive error between actual and coefficient survival counts (2026-10-06)

G69 has a direct finite-horizon consequence for the open counting lane. Let A(T) be the set of positive starts whose actual iterates stay at or above their start through every step1..T. Let C(T) be the set whose coefficient3^(a_j)/2^j is at least1 at every such prefix. Nonnegative affine offsets give C(T) subset A(T).

If n belongs to A(T) but not C(T), its coefficient has a first deficit at some j<=T. Since its actual orbit still survives that step, G69 applies and gives

    n<j^14.3/3<=T^14.3/3.

Thus, with R(T)=T^14.3/3,

    A(T) symmetric_difference C(T) subset[1,R(T)),
    A(T) intersection[R(T),infinity)
       =C(T) intersection[R(T),infinity).

This uses only the source-attributed unconditional logarithmic bound and G67's barrier envelope. No bound on an orbit's stopping time is assumed. Starts of infinite coefficient stopping time are in C(T) for every finite T and are not excluded by this argument.

For any finite integer interval I, the additive count discrepancy satisfies

    0<=abs(A(T) intersection I)-abs(C(T) intersection I)
      <=abs(I intersection[1,R(T)))<=floor(R(T)).

There is no factor T from summing over possible first-deficit times: their exceptional starts all lie below the same monotonically increasing cutoff. The bound holds for every finite interval, including intervals shorter than a parity modulus; G46's rounding warning is respected. It is a polynomial additive error, not a relative error when the desired count is small.

In particular, for the width-w interval I_w=[2^(w-1),2^w), exact equality of both counts is guaranteed when

    3^10*2^(10*(w-1))>=T^143.

This is the exact integer form of2^(w-1)>=R(T). The coarser criterion3*2^(w-1)>=T^15 also suffices. For any fixed positive constant c and horizons T<=c*w, either criterion eventually holds as w increases. Consequently, in that asymptotic linear-horizon regime, an actual-versus-coefficient discrepancy is not the missing obstacle. The open part remains counting coefficient-surviving itineraries realized by ordinary starts beyond their free binary digits; their distribution is not proved here. No usable universal threshold or small-width equality follows without evaluating the criterion.

**Unexpected small-start guard.** The start1 survives forever on1,2,1,2,..., whereas its coefficient first falls below1 at step2. Hence1 belongs to A(2) but not C(2). Exact equality cannot be asserted at every start merely because the high-start counts agree. Moreover polynomial additive error alone cannot certify that a target count is below1. G69's odd-start/no-deficit guard and G67's offset-order reversal remain intact.

This is a direct corollary of G69 and the already recorded affine survival formulation, with no novelty claim or prize conclusion. Independent Local reading requested.

**Next controls, preregistered NOT RUN.** HC1: direct actual trajectories for n1..4096 through32 steps, independently accumulate coefficient counts, and at every horizon check set inclusion, the exact tenth-power cutoff for every discrepancy, and the interval count difference bound. Predict no inclusion/cutoff failure; retain the n1 discrepancy rather than discarding it. HC2: for T=ceil(3*w/2), w2..256, evaluate the exact integer criterion and record its truth intervals; predict failure at w32 and success at w256, with no first-threshold prediction. Counterfactual: A(T)=C(T) at all positive starts; refute at n1,T2. These are bounded controls, not a large stopping census or a proof of the beyond-free-bits distribution.


### G70 controls outcome and independent review (2026-10-06)

HC1 passes131072 start/horizon pairs (n1..4096,T1..32) and384 width/horizon interval-count checks. The sole discrepancy start is1, at all31 horizons2..32; it is retained. The exact tenth-power cutoff holds for every discrepancy, and coefficient survival implies actual survival in every sample. Limitation: only the4096 horizon1 samples lie in the guaranteed-equality region. Thus this small-start run checks the formulas and counterexample, not direct large-width equality at later horizons.

HC2's exact integer calculation for T=ceil(3*w/2), w2..256, finds the criterion false on2..103 and true on104..256. Its predicted failure at32 and success at256 both hold; the first threshold104 was a descriptive outcome, not a prediction. The all-start equality counterfactual fails at n1,T2 as planned. Probe: `tests/probes/prizes/collatz_gpt_count_bridge.py`; Python on GPT's Intel host, under1 s. No control failed.

Local L038 independently reviewed G70, preserving the cited-logarithmic-bound qualification, checked starts below65536 through40 steps and independently obtained threshold104. Local's larger scope is credited separately; GPT did not repeat it. G60-G70's offline review queue is now complete in PROOFS.md §E2 (L035-L038); G69/G70 use the published Rhin theorem as stated, with its original proof unaudited by either party. The bounded Collatz ceiling/certificate block is complete.

Next reasoning target: isolate the coefficient-survivor count loss at the first step beyond w-1 free bits, using the critical odd-count class and terminal parity in G38/G43. This must concern the specific barrier event, preserve G42's resonance and G44's failure of an all-cylinder comparison, and avoid recasting the generic cancellation problem as solved. No new experiment is registered or launched in this checkpoint.

## G71. First paid-bit discrepancy and the critical-boundary loss process (2026-10-06)

Resume the coefficient count of COLLATZ-PRIZE.md §1. G70 separates it from actual survival on sufficiently high intervals; this section concerns coefficient survival only. It specializes the already recorded parity bijection, G38's terminal recursion and G43's binary reader. No novelty claim, mixing estimate or tail-count theorem.

Let ell_t be the least nonnegative integer a with3^a>=2^t (ell_0=0). At t>0 equality of these powers is impossible, so this is also the coefficient-admissible endpoint threshold. Its increments are0 or1. Call step t to t+1 critical when ell_(t+1)=ell_t+1. Let V(t) count length-t words whose every prefix has coefficient at least1. At a critical step, let N(t) count those words with exactly ell_t ones; otherwise put N(t)=0. A child of such a critical-boundary word fails iff its new bit is0. All other admitted parents have two admitted children. Therefore

    V(t+1)=2*V(t)-N(t).

**The first step after the free bits.** Fix width w>=2 and m=w-1. Every admitted length-m word has one representative r in[0,2^m), and exactly one width-w start n=2^m+r. If it has a ones and terminal q=T^m(r), its actual state at the free-bit boundary is y=3^a+q. Since3^a is odd, its next parity is1 minus the parity of q.

Let C_w(t) count coefficient-surviving starts in[2^m,2^(m+1)) through horizon t. At a critical step m to m+1, write O(m) for the number of critical-boundary parents with q odd, and

    F(m)=sum over critical-boundary parents of (-1)^q
        =N(m)-2*O(m).

At a noncritical step put O(m)=F(m)=0. Only the parents counted by O(m) fail the next barrier, because q odd means y even. Thus

    C_w(w)=V(m)-O(m),
    2*C_w(w)-V(w)=F(m).

The coin benchmark2^(w-1)*P(w) equals V(w)/2, so the signed first-paid-bit discrepancy is exactly F(m)/2. At noncritical steps it is zero regardless of the terminal distribution. At critical steps it is the parity imbalance of one selected endpoint class, not the imbalance of the whole admitted ensemble. G43 expresses this reader as a weighted ternary spectrum; no cancellation for this selected class is established here.

**An exact selected-event loss process for later steps.** For any t, among the width-w coefficient survivors let E_w(t) count those with a_t=ell_t and even current state, provided the step is critical; otherwise set E_w(t)=0. Then

    C_w(t+1)=C_w(t)-E_w(t).

No claim of conditional fairness is made. When C_w(t)>0 define h_w(t)=E_w(t)/C_w(t), and put h_coin(t)=N(t)/(2*V(t)). With Q_w(t)=2^(w-1)*V(t)/2^t and R_w(t)=C_w(t)/Q_w(t),

    R_w(t+1)=R_w(t)*(1-h_w(t))/(1-h_coin(t)).

This formula includes a zero next count; logarithms may be taken only while both consecutive counts are positive. At t=m, R_w(m)=1 by the free-bit bijection. Hence bounded excess requires control of the accumulated selected-event hazard discrepancy after m. Noncritical steps contribute no loss on either side. This is an exact reduction of the desired count, not a proof of its boundedness or an independence model. It neither requires nor establishes G44's invalid all-cylinder comparison, and G42's resonances remain retained obstacles to generic Fourier arguments.

**Unexpected parity-sign guard.** At w2,m1 there is one admitted parent word1, r1,q2. Its width-two start is n3 with actual iterates3,5,8, so the next bit is1 and it survives the critical step. Thus C_2(2)=1,V(2)=1,F(1)=1, giving discrepancy+1/2. Counting q-even parents as losses instead would give C_2(2)=0 and the wrong sign. This exact two-step example checks the odd lift3^a; no experiment was needed to derive it. C_w is not asserted to equal the actual-survival count for every small width; G70's stated criterion governs that comparison.

**Next controls, preregistered NOT RUN.** BT1: m1..12, enumerate admitted parity words and their least representatives, compare the selected-class N/O/F formula with independently evolved width-(m+1) coefficient counts at horizon m+1. Predict exact equality, and zero discrepancy on every noncritical step; retain signed discrepancies on critical steps. BT2: widths2..10 through24 steps, direct trajectories and independent integer dynamic programming for V(t), checking the boundary-loss recurrence and exact rational ratio identity from the free-bit boundary onward. Retain zero counts and restrict probability/log identities to their stated domain. Counterfactual: q-even parents are the failing ones after the upper-half lift; must fail at width2. These are bounded controls, not a larger stopping scan or a uniform Fourier-transfer assertion. Independent Local reading requested.


### G71 controls outcome (2026-10-06)

BT1 passes507 admitted parents across m1..12. Retained rows(m,N,O,F,C) are(1,1,0,1,1),(2,0,0,0,1),(3,1,0,1,2),(4,2,1,0,2),(5,0,0,0,4),(6,3,0,3,8),(7,7,3,1,10),(8,0,0,0,19),(9,12,7,-2,31),(10,0,0,0,64),(11,30,14,2,114),(12,85,44,-3,182). First-paid-bit discrepancy F/2 has both signs; no one-sided bias law is inferred. Noncritical rows have F0 exactly.

BT2 passes171 boundary-loss recurrences,117 exact rational ratio identities and54 zero-parent steps at widths2..10 through24 steps. Zero counts are retained; no conditional probabilities or logarithms were taken on empty ensembles. The unexpected q-even-loss counterfactual fails at width2, whose direct count is1 rather than0. Probe: `tests/probes/prizes/collatz_gpt_boundary_loss.py`; Python on GPT's Intel host, under1 s. No control failed. These check identities, not a bound on accumulated hazard discrepancy. Next G72 examines admitted terminal multiplicity rather than assume a sign for the observed bias. Local's width40 run remains a separate claimed lane.

## G72. A polynomial bound on admitted terminal multiplicity (2026-10-06)

Continue the selected coefficient-survivor ensemble, respecting Local's separate width40 counting claim. Fix m>=1. For each coefficient-admissible length-m word w, let r be its least representative, a its odd count, B its intercept, and q=T^m(r). The corresponding width-(m+1) start is n=2^m+r, with terminal y=3^a+q. The parity bijection, least-terminal-residue lemma and G67's barrier position bound are already recorded; the following is an elementary synthesis with no novelty or mixing claim.

**Offset interval.** Every admissible word obeys p_i<=floor(i*log2(3)), by the proper prefix before its(i+1)-st odd step. Thus B<=B_max(a) from G67, even when m is not its first-deficit length. This is an upper bound only; its extremizer need not fit length m. The increasing positions also satisfy p_i>=i, giving

    B>=sum_i 3^(a-1-i)*2^i=3^a-2^a.

At a fixed terminal q and odd count a,2^m*q=3^a*r+B. Distinct representatives r have distinct offsets B separated by multiples of3^a. The number of such offsets in the indicated interval, and therefore the fibre size, is at most

    L(a)=1+floor((B_max(a)-(3^a-2^a))/3^a)
        <=1+floor(a/3).

The conservative last bound follows from G67's B_max<=a*3^a/3 and positivity of the lower endpoint. No monotonicity or tightness of L(a) is asserted.

**The upper-half terminal labels its odd count.** The least-residue lemma gives0<=q<3^a, hence

    3^a<=y<2*3^a.

These intervals are disjoint for distinct a. Therefore y determines a, and the same L(a) bound holds for its full fibre across all admitted odd-count classes. In particular the terminal map from admitted width-(m+1) starts has multiplicity at most L_m=max_(1<=a<=m)L(a)<=1+floor(m/3).

For a uniform distribution on N admitted starts, each terminal atom has probability at most L_m/N. Since y is deterministic, its Shannon entropy in bits satisfies

    H(y)>=log2(N)-log2(L_m).

This bounds loss of initial information by a logarithmic quantity. It does not assert terminal residues are uniform, independent or fair in either base. G44's sparse-cylinder obstruction remains intact.

**Why this is relevant to the selected event.** Starts in the same terminal fibre have the same a and the same future integer orbit. Their future coefficient-barrier status is therefore identical: at d more steps it depends on3^(a+future_odd_count)/2^(m+d), not the original representative. Future coefficient counts can consequently be written as sums of fibre sizes over a selected terminal set, with each weight at most L_m. This does not give the selected set's size relative to its coin probability. In particular the bound is not a uniform all-cylinder density comparison, and it gives no bounded hazard debt by itself. Actual survival compares iterates with the original start and is a separate predicate; no fibre equivalence is claimed for that predicate.

**Unexpected barrier guard.** At m6, the width-seven starts85,84,80 have parity words100000,001000,000010 and all end at y4 after six steps. Their odd count is a1 and the fibre size is3, whereas L(1)=1. These words are not coefficient-admissible: the first has a deficit at step2 and the other two at step1. Thus dropping the barrier invalidates the multiplicity bound. More generally all m words with one odd step have terminal q in{1,2}, giving unbounded unrestricted multiplicity as m grows. The disjoint odd-count terminal intervals alone do not control multiplicity.

**Next controls, preregistered NOT RUN.** FM1: reuse admitted words at m1..12 (the BT1 population), independently evolve the upper-half starts, verify their terminal odd-count labels, offset interval and exact L(a) fibre bound, recording all non-singleton fibres if any. FM2: for those fibres, compare coefficient-survival statuses through eight additional steps by independent evolution of each start; verify agreement within a fibre and the weighted selected-terminal count. Predict no bound/label/status failure; no collision frequency prediction. Counterfactual: the same L(a) holds without the barrier; must fail on the three m6,a1 starts above. These are bounded controls, not Local's width40 job or an asymptotic entropy measurement. Independent Local reading requested.


### G72 controls outcome (2026-10-06)

FM1 passes507 admitted starts across m1..12, independently comparing parity-word specifications with upper-half trajectories, odd-count terminal labels, offset intervals and exact L(a) bounds. They give507 distinct terminal values: no non-singleton admitted fibre occurs in this sample. Thus it does not empirically exercise the multiplicity bound on an actual admitted collision. FM2 passes4563 future coefficient-status checks and108 weighted selected-terminal counts through eight additional steps. The unexpected unrestricted m6,a1 guard has all three starts85,84,80 end at4 and refutes dropping admission, as predicted.

Probe: `tests/probes/prizes/collatz_gpt_terminal_fibres.py`; Python on GPT's Intel host, under1 s. No control failed. Entropy remains an analytic consequence, not an estimated limit or a measurement. Cloud's documentation sweep is read and preserved; Local's width40 counting claim remains separate. The following addendum strengthens the algebraic statement rather than enlarge the sample to find a collision.

### G72 addendum: merging starts are close; a short input label restores injectivity (2026-10-06)

The same proof yields more than a cardinality bound. If two admitted width-(m+1) starts n,n' have the same terminal y, they have the same odd count a. Their affine identities imply

    3^a*(n-n')=B'-B,
    abs(n-n')<a/3<=m/3.

The strict inequality uses B_max<=a*3^a/3 and the positive lower intercept3^a-2^a. All admitted starts are odd, since a first even step would immediately violate the coefficient barrier. Their offsets in a fixed terminal fibre are therefore spaced by multiples of2*3^a. The sharper bound is

    L_odd(a)=1+floor((B_max(a)-(3^a-2^a))/(2*3^a))
            <=ceil(a/6).

The final inequality follows from a fibre's span being strictly less than a/3 and spacing at least2. It is a conservative bound, not an assertion of attainable collisions. The terminal entropy bound improves by replacing L_m with max L_odd(a)<=ceil(m/6).

Let s be the least nonnegative integer with3*2^s>=m. Then the map

    n -> (terminal y, n modulo2^s)

is injective on the admitted width-(m+1) ensemble. Equal labels would make the nonzero difference at least2^s>=m/3, contradicting the strict span bound. Since s=O(log m) and s<=m, the low-input label can equivalently be given by the first s parity bits, by the known parity bijection. At s0 the modulus is1. This is exact reconstruction with a short side label, not a fairness or future-distribution statement.

**Unexpected admission guard for the stronger claim.** At m9, unrestricted odd starts625 and597 both have a2 and terminal11. Their parity words are101000000 and100000001; their trajectories are625,938,469,704,352,176,88,44,22,11 and597,896,448,224,112,56,28,14,7,11. Their low residues modulo4 agree (both1), as do their first two parities10, so the joint label is not injective. Here s2 since3*4>=9. Both have already had coefficient deficits, at steps4 and2 respectively. Their difference28 also violates the admitted span bound9/3. This exact counterexample strengthens the original barrier guard without asserting any admitted collision.

**Next control, preregistered NOT RUN.** FM3: on the same admitted m1..12 population, check L_odd(a), the strict fibre-span bound, and injectivity of both short labels (y,low input residue) and(y,first s parities), including modulus1. Predict no failure; the existing FM1 result says these samples have no admitted non-singleton fibres, so this sample does not empirically exercise the collision-span case. Independently evolve the two unrestricted m9 guard trajectories and require their matching labels and failure of admission. No larger census or Local compute job. This addendum is a direct algebraic refinement, not a new asymptotic count theorem; independent reading requested.


### G72 short-label controls outcome (2026-10-06)

FM3 passes507 admitted starts/507 terminal fibres at m1..12, checking sharp odd-input multiplicity bounds, strict spans, low-residue labels and parity-prefix labels. Four admitted starts exercise modulus1. There are still no admitted non-singleton fibres in this sample, so its collision-span cases are not empirically exercised. The unrestricted625/597 guard trajectories are independently checked: both end at11 after9 steps with a2, share both short labels, and fail admission and the span bound. Probe mode: `tests/probes/prizes/collatz_gpt_terminal_fibres.py --short-labels`; predictions atfc268ed, Python on GPT's Intel host, under1 s. No control failed; no larger population was run. G73 extends the analytic result to specified finite tail horizons.

## G73. Short-label reconstruction throughout a finite coefficient-surviving tail (2026-10-06)

G72's reconstruction extends beyond its free-bit boundary. Fix width w=m+1 with m>=1, and horizon1<=t<=3*2^m. Consider only starts n in[2^m,2^(m+1)) whose coefficients have survived every prefix through t. If their odd count is a, intercept B and terminal y, then

    2^t*y=3^a*n+B,
    0<B/3^a<=a/3<=t/3<=2^m.

The offset bound is G67's proper-prefix position argument, valid for every admitted word; no first-deficit or logarithmic theorem is used. Therefore

    3^a*2^m<=2^t*y<3^(a+1)*2^m.

The upper bound is strict since n<2^(m+1). These disjoint bands determine a from y at the known width and horizon. No rounded logarithm is needed: compare the displayed integers.

If two admitted starts have the same y, they have the same a. G72's offset interval and first-bit parity now give

    abs(n-n')<a/3<=t/3,
    fibre size<=L_odd(a)<=ceil(a/6)<=ceil(t/6).

Let s(t) be the least nonnegative integer with3*2^s>=t. The label(y,n modulo2^s), equivalently(y,the first s parities), is injective on the ensemble. Indeed a nonzero difference sharing the input label would be at least2^s>=t/3. Here s<=m by the horizon hypothesis, and s<=t; the indicated prefix is available. For a uniform nonempty surviving ensemble of size N_t, H(y)>=log2(N_t)-log2(ceil(t/6)). All these statements concern surviving initial inputs at a specified time, not entropy generated by an orbit.

The exact inverse carry is also small:

    n=floor(2^t*y/3^a)-floor(B/3^a),
    0<=floor(B/3^a)<=floor(a/3).

This follows by taking the floor of n+B/3^a. It supplies a bounded correction after the terminal's odd-count label has been identified; it does not assert that the correction is uniformly distributed or independent of y.

This covers any fixed linear horizon t<=c*w eventually in width. It is a structural statement about the ensemble underlying G71's selected losses. It does not bound its surviving cardinality, its accumulated hazard discrepancy or future parity bias. G44's finite-information obstruction is consistent with it. Local's width40 count job is not needed or duplicated. The proof is an elementary extension of recorded affine/barrier lemmas, with no novelty claim.

**Unexpected admission guard.** At width4,horizon13, unrestricted starts9 and13 both end at1 but have respectively6 and5 odd steps. Their trajectories are9,14,7,11,17,26,13,20,10,5,8,4,2,1 and13,20,10,5,8,4,2,1,2,1,2,1,2,1. The horizon condition13<=3*8 holds, but both had their first coefficient deficit at step2. Thus a terminal need not identify the odd count once admission is removed. This is separate from G72's same-odd-count hash collision guard.

**Next controls, preregistered NOT RUN.** AT1: reuse widths2..10 through24 steps, direct coefficient-survivor trajectories; at every horizon satisfying t<=3*2^(w-1), verify exact bands, odd-count uniqueness, fibre span/multiplicity, short-label injectivity and the inverse carry. Predict no failure; retain zero ensembles and all non-singleton fibres if any. AT2: independently evolve the width4,horizon13 guard, record the two odd counts and first-deficit times; the unrestricted odd-count-identification counterfactual must fail. No larger census, empirical entropy claim or mixing prediction. Independent Local reading requested.


### G73 controls outcome (2026-10-06)

AT1 passes2313 admitted start/horizon samples and2313 terminal fibres at widths2..10 through24 steps, restricted to t<=3*2^(w-1). Exact bands, inverse carries, multiplicities, strict spans and both short labels pass. All27 empty ensembles are retained. No admitted non-singleton fibre occurs, so these controls do not empirically exercise merging or estimate entropy. AT2 independently verifies the width4,horizon13 trajectories: starts9 and13 end at1 with odd counts6 and5, respectively, and both first fail the coefficient barrier at step2. The unexpected unrestricted odd-count-identification counterfactual fails as predicted.

Probe: `tests/probes/prizes/collatz_gpt_tail_labels.py`; predictions at773b424, Python on GPT's Intel host, under1 s. No control failed. The reconstruction block is complete, with independent reading pending. Next reasoning returns to G71's critical-event hazard: small fibres and disjoint odd-count bands do not by themselves control the even/odd allocation inside a selected critical class. No larger census or Local count job is duplicated.

## G74. Backward survival weights isolate the final count discrepancy (2026-10-06)

G71's hazard ratio is exact but changes both the critical-class occupancy and its parity allocation. A standard backward-equation telescoping argument instead writes the final additive discrepancy directly in terms of parity imbalances at each odd count. This is an application of finite first-step analysis, not a novelty or mixing claim; prior-art scope is recorded in PRIOR-ART.md.

Fix w=m+1, m>=1 and final horizon T>=m. Let K_w(t,a) count width-w starts coefficient-admitted through t with a odd steps. Let I_w(t,a) be the number of these starts with odd current state minus the number with even current state. Counts include multiplicity of starts, even if terminal states merge. Put I=0 for absent classes.

Define f_t(a) as the probability that independent fair future parity bits survive every coefficient barrier from the already-admitted state (t,a) through T. Set f_t(a)=0 when a<ell_t, f_T(a)=1 when a>=ell_T. For admitted a and t<T, first-step analysis gives

    f_t(a)=(f_(t+1)(a)+f_(t+1)(a+1))/2,
    Delta_t(a)=f_(t+1)(a+1)-f_(t+1)(a).

The definition extends f_t to every integer a; a killed state stays killed. Coupling the same future bits from a and a+1 proves monotonicity in a. Hence0<=Delta_t(a)<=1. Also Delta_t(a)=0 for a>=ell_T, since either child then survives even an all-zero future. Only admitted classes with ell_t<=a<ell_T can contribute.

Let H_t=sum_a K_w(t,a)*f_t(a). An odd actual current state sends its input to a+1; an even state sends it to a. Inadmissible children have f=0, matching their removal. Subtracting the fair average for each parent gives exactly

    H_(t+1)-H_t=(1/2)*sum_a I_w(t,a)*Delta_t(a).

At the free-bit boundary K_w(m,a) equals the number of admitted length-m words with a ones, by the parity bijection. Therefore H_m=Q_w(T)=2^m*V(T)/2^T, while H_T=C_w(T). Telescoping proves

    C_w(T)-Q_w(T)
      =(1/2)*sum_(t=m)^(T-1) sum_a I_w(t,a)*Delta_t(a).

This includes T=m (empty sum) and empty later ensembles. It requires no conditional probabilities of the actual ensemble and no positive-count assumption. In particular

    abs(C_w(T)-Q_w(T))
      <=(1/2)*sum_(t=m)^(T-1) sum_a abs(I_w(t,a))*Delta_t(a).

The weights have a concrete interpretation. Take fair bits for steps t+2 through T, with cumulative ones Z_k and Z_0=0. Put

    J=max_(j=t+1)^T (ell_j-Z_(j-t-1)).

A child with a ones survives precisely when a>=J. Thus Delta_t(a)=Pr(J=a+1). Over all integer a these weights sum to1. On the actual admitted classes their sum is at most1; consequently the previous bound is at most half the sum over t of max_a abs(I_w(t,a)). This coarse bound is not known to be small. The sharper weighted signed sum is the selected object; no cancellation, bounded excess or exponential count rate is proved.

**Unexpected immediate-loss guard.** Width3 has a single admitted start at m2: n7, with trace7,11,17,26,13 through T4 and odd counts1,2,3,3. Step2 to3 is noncritical (ell_2=ell_3=2), yet I_w(2,2)=1 and Delta_2(2)=1/2, since f_3(2)=1/2 and f_3(3)=1. Its contribution is1/4. At step3 the only class is a3, where Delta_3(3)=0. Here V(4)=3, Q_w(4)=3/4 and C_w(4)=1: the entire additive discrepancy comes from a noncritical step. Dropping noncritical terms from this formula gives0, incorrectly. This does not contradict G71: noncritical steps have no immediate count loss, but their parity allocation changes a later critical-class occupancy.

**Next controls, preregistered NOT RUN.** BW1: widths2..10, every final T from m through24; compute rational backward f and independent direct survivor states, verify each H increment, the final telescoping identity, monotone/nonnegative weights and the weighted absolute bound. Retain zero ensembles and separate noncritical contributions. Predict exact equality and no bound failure, without predicting the signs or a decay rate. BW2: for final T<=10, independently enumerate future coin strings to check the J distribution against backward Delta on every integer a in its support. Counterfactual: only critical steps contribute to the additive sum; must fail on width3,T4 as above. No large stopping scan, entropy measurement or Local job. Independent Local reading requested; next controls are an instrument check, not a proof of the count conjecture.


### G74 controls outcome (2026-10-06)

BW1 passes180 width/final-horizon cases and1740 exact rational H increments at widths2..10, T=m..24. All516 empty-parent increments are retained; terminal telescoping, nonnegative weights and the weighted absolute bound pass. BW2 independently enumerates future coin strings for T1..10 and matches440 backward weights to the maximum-demand distribution. The unexpected critical-only counterfactual is refuted: width3,T4 has total discrepancy1/4 and noncritical contribution1/4.

Probe: `tests/probes/prizes/collatz_gpt_backward_weights.py`; preregistration at4a78c0b, GPT's Intel host, Python, under1 s. No control failed. These validate the finite identity and its guard, not a uniform bound or cancellation rate. Independent Local proof reading remains pending. Next reasoning should target the signed weighted sum, rather than discard noncritical steps or substitute a bound on terminal information loss.

## G75. A uniform atom bound for the backward coin weights (2026-10-06)

G74's weights can be bounded without any assumption on the actual Collatz ensemble. Write h=T-t-1>=0 for the number of future coin bits after the selected child. For every integer L>=1,

    max_a Delta_t(a)
      <=min(1, L/sqrt(h+1)+32*exp(-(L-1)/2)).

Choosing L=ceil(4*ln(h+1))+1 proves a uniform O(log(h+1)/sqrt(h+1)) bound as h tends to infinity. This controls the coin completion weights only. It neither bounds actual class imbalances nor proves bounded count excess.

**Proof.** Use G74's future-bit count Z_h and maximum demand J. Reverse the h fair bits and write S_k=Z_h-Z_(h-k), with S_0=0. Algebra gives

    J=ell_T-Z_h+R,
    R=max_(0<=k<=h) (S_k-(ell_T-ell_(T-k))).

Here R is a nonnegative integer, since k0 contributes0. Let beta=log(2)/log(3). The ceiling identity ell_j=ceil(beta*j) implies ell_T-ell_(T-k)>beta*k-1. The exact inequality3^5<2^8 gives beta>5/8. For integer r>=1, R>=r therefore requires some k>=1 with

    S_k-k/2>r-1+k/8.

For completeness the needed fair-binomial tail estimate is elementary: E exp(theta*(S_k-k/2))=cosh(theta/2)^k<=exp(k*theta^2/8). The inequality follows from tanh(u)<=u for u>=0 by integration. Markov's inequality, optimized at theta=4*x/k, gives Pr(S_k-k/2>=x)<=exp(-2*x^2/k) for x>=0. Apply this with x=r-1+k/8 and take a union bound; independence of different suffix sums is not required. Since

    2*(r-1+k/8)^2/k >= (r-1)/2+k/32,

we obtain

    Pr(R>=r)<=exp(-(r-1)/2)*sum_(k>=1) exp(-k/32)
             <32*exp(-(r-1)/2).

The central atom of Binomial(h,1/2) is at most1/sqrt(h+1). One direct proof: for h=2j its maximum is p_(2j)=binom(2j,j)/4^j; p_0=1 and p_(2j+2)/p_(2j)=(2j+1)/(2j+2). Induction uses (2j+1)*(2j+3)<(2j+2)^2 to give p_(2j)<=1/sqrt(2j+1). The odd maximum p_(2j+1)=p_(2j)*(2j+1)/(2j+2) is at most1/sqrt(2j+2).

For any integer v, split the event J=v into R0..L-1 and R>=L. Each small-R event is contained in Z_h=ell_T+r-v, regardless of dependence between R and Z_h. Thus

    Pr(J=v)<=sum_(r=0)^(L-1) Pr(Z_h=ell_T+r-v)+Pr(R>=L),

which gives the displayed bound and, for the stated L, tail term at most32/(h+1)^2. Since Delta_t(a)=Pr(J=a+1), the claim follows. The h0 case is included, though its bound is simply1. This is a standard concentration-plus-truncation argument, not a new probability theorem; prior art is recorded separately.

**Unexpected dependence guard.** Take T3,t1,h1. Then ell_2=ell_3=2, so J=max(2,2-Z_1)=2, while R=Z_1. Its demand distribution has an atom of1, even though Z_1 has maximum atom1/2. Dropping R, or importing the binomial atom bound directly for J, is wrong. The proof above keeps the dependence and its truncation cost. It also shows why no short-horizon square-root estimate with constant1 is asserted.

**Next controls, preregistered NOT RUN.** WA1: reuse G74's complete future-string population T1..10. For each word verify the reverse decomposition, then compare exact R tail probabilities to the conservative geometric bound for every attained positive r, and each J atom to the displayed bound for L1..8. Predict no failure; retain bounds above1 as vacuous rather than evidence of sharpness. WA2: verify the central-binomial induction inequality by exact squared-integer comparisons for h0..256, and independently enumerate the T3,t1 guard. Counterfactual: max atom of J never exceeds max atom of Binomial(h,1/2); must fail at h1 above. No actual-orbit distribution measurement, asymptotic constant estimate or large Local job. Independent proof reading requested.


### G75 controls outcome (2026-10-06)

WA1 passes2036 exact reverse decompositions across all future coin strings for T1..10,57 overshoot-tail comparisons and1304 atom comparisons for L1..8. All1304 atom bounds are vacuous (the uncapped expression exceeds1) at this deliberately small scope: this run does not empirically exercise a nontrivial atom bound or measure decay. Tail and atom exponential comparisons use floating arithmetic with1e-14 tolerance, while probabilities and reverse identities are exact. WA2 passes257 exact squared-integer central-binomial bounds for h0..256. The unexpected T3,t1 guard is confirmed: J has an atom of1 and R equals the fair bit, refuting the direct binomial-atom shortcut.

Probe: `tests/probes/prizes/collatz_gpt_weight_atoms.py`; predictions at51a1a0e, GPT's Intel host, Python, under1 s. No control failed. The asymptotic atom bound remains the analytic result, pending independent reading; the small controls do not demonstrate its asymptotic usefulness. No actual-orbit or Local computational job was run. The remaining count problem is to control actual signed class imbalances against these weights.


## G76. A bounded signed-contribution diagnostic, preregistered (2026-10-06)

G75 controls the coin weights, not the actual signed imbalances. Before pursuing a triangle bound or a cancellation estimate, distinguish them on the already used small ensemble. For each width/final horizon in G74, write g_(t,a)=I_w(t,a)*Delta_t(a)/2, and measure

    Pplus=sum max(g_(t,a),0),
    Pminus=sum max(-g_(t,a),0),
    D=Pplus-Pminus=C_w(T)-Q_w(T),
    A=Pplus+Pminus.

Report A/Q and D/Q, with Q>0 at every finite horizon; report A/abs(D) only when D!=0. Retain zero net discrepancies and empty actual ensembles separately. No finite maximum of these ratios is an asymptotic bound. This is a diagnostic of the selected observable, not a new large count or a generic parity-uniformity test. G74 supplies the identity; neither it nor G75 asserts cancellation.

**Unexpected sign guard, derived directly.** At width3,T5 the sole admitted free-bit start7 follows7,11,17,26,13,20 with odd counts1,2,3,3,4. Backward coin completion gives H_2=1/2,H_3=3/4,H_4=1/2,H_5=1. Thus the contributions at t2,3,4 are respectively+1/4,-1/4,+1/2. Their total is1/2, whereas A=1. The unrestricted-sign counterfactual that every contribution has the sign of the final discrepancy is false already here. This exact guard also prevents equating the triangle budget with the signed budget.

**Next diagnostic, preregistered NOT RUN.** SA1: reuse widths2..10 and T=m..24, the full G74 scope, recording Pplus/Pminus/A/D with exact rational arithmetic, extrema of A/Q and A/abs(D), all zero discrepancies and all empty final ensembles. Required controls: D equals the direct final count minus the independently computed coin count, A>=abs(D), and the guard has terms(+1/4,-1/4,+1/2). SA2 blind prediction: at least one case with a positive final count has cancellation factor A/abs(D)>2. A failure is retained and changes the interpretation, not the scope. Counterfactual: every nonzero term agrees with the final sign; must fail on the guard. No rate fit, larger population or Local run. This block asks whether triangle estimates lose material information in a small sample; it cannot decide the asymptotic count claim.


### G76 signed-budget outcome (2026-10-06)

SA1 passes180 width/final-horizon cases;148 nonzero-net cases have at least one contribution opposite to their final sign. All18 zero-net cases and57 empty-final ensembles are retained in the probe output. Independent direct final counts match the weighted net in every case. SA2 HELD: among positive-count cases with nonzero discrepancy, the largest cancellation factor is2155/88 (about24.49), at width10,T20 with C=13, Pplus=2067/512 and Pminus=2243/512. Here D=-11/32, A=2155/256, D/Q=-11/427 and A/Q=2155/3416. The largest A/Q in the full sample is1033093/95527 (about10.81), at width5,T24. The unexpected width3,T5 guard reproduces(+1/4,-1/4,+1/2) and refutes the one-sign counterfactual.

Probe: `tests/probes/prizes/collatz_gpt_signed_budget.py`; preregistration at961ed39, GPT's Intel host, Python, under1 s. No required control failed. These finite diagnostics show a material loss from taking absolute values in some small cases; they neither prove that cancellation persists at large width nor refute all possible triangle bounds. Next reasoning should preserve the signed observable rather than infer a uniform law from the largest sampled factor. No larger Local count run was duplicated.


## G77. Which triangle estimate the signed diagnostic does and does not exclude (2026-10-06)

The count target is an upper bound on C_w(T)/Q_w(T), not a small cancellation factor A/abs(D). From G76, C=Q+D<=Q+A. Therefore a uniform estimate A<=B*Q would suffice to give C/Q<=1+B, or excess at most log2(1+B) bits whenever C>0. Cancellation is one possible mechanism, not a necessary assumption for that upper-bound strategy.

**Unexpected normalization guard.** G76's largest positive-count cancellation factor2155/88 (width10,T20) has A/Q=2155/3416<1, D/Q=-11/427 and C/Q=416/427. A triangle estimate already gives C/Q<=1+2155/3416<2 in that case. Thus a large A/abs(D) does not refute a useful bound on A/Q. This is an exact consequence of the retained rational row, not a new run. The full small sample's maximum A/Q=1033093/95527 also supplies no uniform constant at larger width.

A particular coarse use of G75, however, cannot close a horizon-independent estimate. For h>=0 put

    b(h)=min(1, inf over integer L>=1 of
                  (L/sqrt(h+1)+32*exp(-(L-1)/2))).

Each term inside the infimum is at least1/sqrt(h+1), so b(h)>=1/sqrt(h+1). Since sum_a abs(I_w(t,a))<=C_w(t), G74-G75 give

    A_w(T)<= (1/2)*sum_(t=m)^(T-1) b(T-t-1)*C_w(t).

Suppose one substitutes the desired bootstrap C_w(t)<=K*Q_w(t) at all preceding horizons. Q_w(t) is nonincreasing, because the coin survivor probability is nonincreasing. Consequently the resulting sufficient upper bound has the form

    A_w(T)/Q_w(T) <= K*B_(m,T),
    B_(m,T)=(1/2)*sum_(t=m)^(T-1)
                       b(T-t-1)*Q_w(t)/Q_w(T),
    B_(m,T)>=sqrt(T-m+1)-1.

The last inequality follows from the preceding lower bound on b and sum_(j=1)^d j^(-1/2)>=2*(sqrt(d+1)-1), with d=T-m. Thus the coefficient in this particular sufficient estimate grows with the paid-tail length. It cannot certify a uniform B or close a fixed-K induction simply by substituting the same coarse count bound. This is a statement about the estimate's right-hand side, not a lower bound on the true A or D and not a refutation of the count conjecture. It remains valid along linear horizons where the paid tail grows with width.

**Route status.** Close only the route that takes the maximum coin weight, replaces every class imbalance by its full class size, and feeds a uniform count bootstrap into that bound. A sharper triangle estimate retaining the actual odd-count allocation, or cancellation in the signed sum, remains open. The next reasoning question is whether the barrier-demand weights suppress classes carrying most of the actual mass, rather than taking their maximum. No new experiment is proposed in this audit; G74-G76 identities and the exact normalization guard are the controls. Independent Local reading requested. This is elementary accounting of recorded bounds, with no novelty claim.

## G78. Even ideal coin-class allocation leaves a growing full-class proxy (2026-10-06)

G77 leaves allocation-aware triangle estimates open. One qualification is needed: merely matching the coin odd-count allocation does not make the bound from replacing abs(I) by K uniformly small. Define v(t,a) as the number of admitted length-t words with a ones and

    q_w(t,a)=2^m*v(t,a)/2^t,
    U_coin(m,T)=(1/2)*sum_(t=m)^(T-1) sum_a q_w(t,a)*Delta_t(a).

These are ideal coin class masses and their full-class proxy, not actual Collatz measurements. Let d=T-m. Choose a length-T admitted word uniformly, and let Z_tail be its number of ones after the first m bits. Then exactly

    U_coin(m,T)/Q_w(T)=E[2*Z_tail-d | admitted through T].

**Proof.** Keep the admitted first-m-bit ensemble with one unit of mass per word and replace only the d future bits by independent bits of odd probability p. Its final mass is the finite polynomial

    F(p)=sum over admitted length-T words of p^z*(1-p)^(d-z),

where z=Z_tail. Thus F(1/2)=V(T)/2^d=Q_w(T), and differentiation gives

    F'(1/2)/(2*F(1/2))=E[2*Z_tail-d | admitted through T].

Independently, differentiate one tail coordinate at a time. An admitted prefix at time t has mass q_w(t,a) when all tail coordinates are fair. Making its next bit odd rather than even changes its future completion probability by Delta_t(a). A prefix already killed contributes0. The coordinate sum is therefore F'(1/2)=sum_(t=m)^(T-1) sum_a q_w(t,a)*Delta_t(a)=2*U_coin. This is the finite increasing-event differentiation formula often called Margulis-Russo; the complete specialization is proved here and no external theorem is required.

Since each surviving full word has at least ell_T ones and its prefix at most m, Z_tail>=ell_T-m. Consequently

    U_coin(m,T)/Q_w(T)>=2*ell_T-T-m.

In particular beta=log(2)/log(3)>5/8 gives, at T=8*m with m>=1,

    U_coin(m,8*m)/Q_w(8*m)>m.

The ideal full-class proxy thus grows along a fixed linear horizon. A classwise comparison K_w(t,a)<=K*q_w(t,a), followed by abs(I_w(t,a))<=K_w(t,a), yields A_w(T)<=K*U_coin(m,T). Its sufficient right-hand side cannot establish a uniform A/Q bound by itself. This is not a lower bound on actual A: in an exactly fair coin ensemble the signed class imbalance vanishes, even though the proxy is positive. Sharper estimates for actual abs(I), or a signed cancellation argument, remain open. No assertion is made that actual classwise domination holds.

**Unexpected proxy-versus-error guard.** At m2,T5 the four admitted full words have tail words011,101,110,111. Their tail signed counts2*z-3 are1,1,1,3, with mean3/2. Here Q=1/2 and U_coin=3/4. Ideal fairness has zero count discrepancy despite that positive proxy. Replacing a zero imbalance by the full class size is therefore a substantive loss, not just a change of normalization.

**Next controls, preregistered NOT RUN.** PC1: m1..8,T=m..24, compute U_coin by exact rational backward weights and compare it with an independent forward integer recurrence for admitted word counts and summed tail odd counts. Predict identity and the endpoint lower bound; retain T=m. PC2: coin dynamic programming only, m1..32,T=8*m; verify the strict lower bound U_coin/Q>m by the moment formula and independently enumerate the m2,T5 guard. Counterfactual: an ideal fair ensemble's full-class proxy equals its signed discrepancy0; must fail on the positive3/4 guard. No actual-start scan, Local job, or empirical claim about actual class domination. Independent Local reading requested.


### G78 controls outcome (2026-10-06)

PC1 passes164 exact rational backward-proxy/forward-tail-moment comparisons at m1..8,T=m..24, including8 empty-tail cases. Endpoint lower bounds pass. PC2 passes32 exact strict inequalities U_coin(m,8*m)/Q_w(8*m)>m for m1..32, using integer counts and moments only. Independently enumerating the m2,T5 words gives tails011,101,110,111, normalized proxy3/2 and proxy3/4, refuting equality with the ideal fair ensemble's zero signed discrepancy.

Probe: `tests/probes/prizes/collatz_gpt_coin_proxy.py`; predictions at14fde39, GPT's Intel host, Python, under1 s. No control failed. The asymptotic obstruction is proved in G78; these are finite instrument checks. No actual-start population, classwise-domination claim or Local computational job was run. Independent proof reading remains pending.


## G79. The coin-sensitivity-weighted actual bias target, preregistered diagnostic (2026-10-06)

Use G74 and G78 without replacing actual parity imbalances by full class sizes. At a class with q_w(t,a)>0 put epsilon_w(t,a)=I_w(t,a)/q_w(t,a). Every actual admitted prefix is an admitted parity word, so a class with q=0 also has I=0. Terms with Delta=0 are irrelevant. If U_coin(m,T)>0, define the probability weights

    mu_(m,T)(t,a)=q_w(t,a)*Delta_t(a)/(2*U_coin(m,T)).

They sum to1. The recorded identities immediately give

    D_w(T)/Q_w(T)=S_(m,T)*E_mu[epsilon_w],
    A_w(T)/Q_w(T)=S_(m,T)*E_mu[abs(epsilon_w)],
    S_(m,T)=U_coin(m,T)/Q_w(T).

This is a reparameterization, not a new cancellation theorem. At T=8*m, G78 gives m<S<=7*m (the upper bound uses2*Z_tail-d<=d=7*m). Thus a bounded relative discrepancy is equivalent to an O(1/m) signed weighted mean along this horizon: necessity follows from S>m and sufficiency from S<=7*m. A uniform upper bound C/Q also bounds abs(D/Q), since C>=0 implies D/Q>=-1. No such bias estimate is proved. A corresponding O(1/m) absolute weighted mean would be a stronger sufficient triangle bound; G77-G78 do not establish it.

**Unexpected denominator guard.** epsilon is not a conditional probability bias, since its denominator is the ideal coin class mass. At width2,m1,T4,t3,a2 the start3 has trajectory3,5,8,4 and is still coefficient-admitted, with even terminal4. Thus I=-1. There is one admitted length3 word with a2 (110), giving q=2/8=1/4, while Delta_3(2)=1. Hence epsilon=-4 on a class with positive weight. A pointwise [-1,1] assumption already fails. Normalizing instead by the actual class size would change the probability weights, and cannot silently be substituted into the identity.

**Next diagnostic, preregistered NOT RUN.** SB1: reuse the180 G74/G76 width/horizon cases. Compute mu and epsilon rationally; verify its signed/absolute means recover D/Q and A/Q, retain every U=0 case separately (where D=A=0), and report the largest abs(epsilon) on positive-weight support, signed and absolute means, and S. No size or rate prediction for those measured extrema. SB2: independently evolve the width2,T4 guard and count its single admitted endpoint word, requiring epsilon=-4 and Delta1. Counterfactual: epsilon always lies in[-1,1]; must fail on that guard. These instrument controls define a target for a later reasoning block, not an asymptotic fit or a larger actual-start scan. No Local job or classwise-domination assumption.


### G79 weighted-bias diagnostic outcome (2026-10-06)

SB1 passes168 positive-proxy cases and12 zero-proxy cases in the existing180-case scope. The probability weights sum to1, signed and absolute identities agree exactly, and every zero-proxy case has D=A=0. The largest supported abs(epsilon) is131072/6167 (about21.25), at width5,T24,t20,a15, with mu=6167/1953628 (about0.00316). The largest absolute weighted mean is17/9 at width3,T7, whose final actual ensemble is empty; this case is retained rather than interpreted as a positive-count estimate. SB2 independently evolves3 to4 through three steps, enumerates the single admitted a2 word110, and verifies epsilon=-4,Delta1. The unexpected pointwise probability-bias counterfactual is refuted.

Probe: `tests/probes/prizes/collatz_gpt_weighted_bias.py`; preregistration at343dbb1, GPT's Intel host, Python, under1 s. No control failed. These ratios do not measure an asymptotic 1/m rate or demonstrate a uniform actual bias bound. They show why peak pointwise bias and the weighted mean must be separated. No larger actual population or Local job was run. Next reasoning must supply an estimate for this mean, rather than normalize it as an actual conditional probability.

## G80. Interior mixed pairs cancel the first backward difference (2026-10-06)

G76's opposite-sign contributions sometimes cancel for a structural reason. Fix final T and two consecutive steps from t to t+2<=T. Consider one actual input still coefficient-admitted at time t, with a odd steps, and assume

    a>=ell_(t+1).

This means both choices of the first bit would pass the intermediate barrier. Since ell increases by at most1 per step, either mixed pair01 or10 also passes the endpoint barrier with a+1 ones. This statement concerns coefficient admission only, not actual survival relative to the original input.

Write F(j)=f_(t+2)(j), with the same killed-state extension as G74. Two backward fair steps give

    f_t(a)=(F(a)+2*F(a+1)+F(a+2))/4.

Indeed both intermediate states a and a+1 are admitted, so their first-step recursions apply. For either actual mixed pair, the sum of that input's two signed G74 contributions is therefore exactly

    F(a+1)-f_t(a)
      =(2*F(a+1)-F(a)-F(a+2))/4.

The first differences have cancelled, leaving a second difference. The result is independent of which mixed order the actual orbit takes. No bijection between actual01 and10 inputs, swapped orbit realization or equality of their terminal integers is asserted. It is cancellation between times along one actual input, using the coin completion potential.

**Exact block accounting.** Partition the paid tail into disjoint two-step blocks starting at m,m+2,..., leaving one final step if needed. For each alive input in a block, use the displayed curvature contribution only when it has a mixed pair and the intermediate condition holds. Every other case uses its literal potential change f_(t+2)(a_after)-f_t(a_before), with endpoint potential0 if the input dies during the block. Sum over inputs alive at the block's start. Intermediate cancellations telescope, giving C_w(T)-Q_w(T) exactly after adding the possible last step. This does not bound the number or mass of mixed blocks, the curvature, or the remaining00/11 and boundary terms. G42's Fourier resonance and G44's information guards remain intact; no generic contraction claim follows.

**Unexpected barrier guard.** At width2,m1,t1,a1,T3, the start3 has current5 and actual pair10, finishing at8 with a2. It passes both actual steps. But ell_2=2>a1, so alternative01 is killed immediately. Here f_1(1)=1/2 and f_3(2)=1, giving literal contribution1/2. The unjustified curvature formula instead gives(2*1-0-1)/4=1/4. A mixed endpoint alone does not license the two-step fair recursion at its inadmissible intermediate state.

**Recorded interior example.** Width3,T5,start7 has at t2 the actual pair10, a2 and ell_3=2. G76 records its two contributions+1/4,-1/4. Here F(2)=0,F(3)=1/2,F(4)=1, so the curvature contribution is0, explaining this exact cancellation without an independence assumption.

**Next controls, preregistered NOT RUN.** MP1: reuse widths2..10,T=m..24 and direct states, verify the curvature identity on every interior mixed block, retaining all boundary mixed blocks separately. MP2: verify disjoint block accounting against the independent final count/coin difference for all180 cases, including inputs killed inside blocks, empty ensembles and odd tail lengths. Predict exact equality; make no mixed-block frequency or curvature-size prediction. Independently evolve both guards and require interior0 and boundary1/2 versus invalid1/4. Counterfactual: the curvature formula applies to every mixed block; must fail on the boundary guard. No larger population or Local job. Independent Local reading requested. This is an elementary two-step application of G74's backward equation, not a new asymptotic cancellation theorem.


### G80 controls outcome (2026-10-06)

MP1 passes2925 interior mixed-block curvature identities in the existing width2..10,T=m..24 scope. All257 surviving boundary mixed blocks are retained separately. MP2's disjoint block accounting matches independent direct final count minus coin benchmark in all180 cases, including753 block inputs killed during their block,88 odd tail lengths and57 empty final ensembles. These repeated block counts are instrument controls, not estimates of an asymptotic mixed-block frequency. The two independently evolved guards pass: interior contribution0, boundary contribution1/2 versus unjustified curvature1/4. The unexpected unrestricted-curvature counterfactual is refuted.

Probe: `tests/probes/prizes/collatz_gpt_mixed_curvature.py`; predictions ata4645cf, GPT's Intel host, Python, under1 s. No control failed. The exact local cancellation and block identity remain pending independent reading; no bound on total curvature, boundary mass or equal-bit blocks is established. No larger actual population or Local job was run.

## G81. Reduce the admitted-collision question to offset residues (2026-10-06)

Reply to Local L040. Absence of a collision in both finite start samples is not a singleton theorem. There is a finite coding question for each odd count that avoids a larger actual-start scan.

Fix a>=1 and t_a=floor(log_2(3^a)), computed as bit_length(3^a)-1. Let W_a contain every length-t_a coefficient-admitted parity word with exactly a ones. For each word use its affine intercept B. Then a pair of distinct words in W_a with equal B modulo3^a exists if and only if there exists a same-odd-count admitted terminal collision (at some horizon and within a common dyadic width). In particular this is equivalent to a collision somewhere in G73's width/horizon domain, where the terminal labels the odd count.

**Necessity and reduction to one horizon.** If two admitted starts meet after t steps with odd count a, their affine equations give

    3^a*(n'-n)=B-B'.

Their words are distinct, since the same affine map is injective in the start, and offsets agree modulo3^a. Admission implies t<=t_a. Pad both words with zeroes to length t_a. Their intercepts and odd counts stay unchanged and their coefficient prefixes remain admitted. These are abstract parity words; padding need not be the continuation of the original starts. The coding collision persists.

**Sufficiency and explicit realization.** Conversely take distinct words in W_a with intercepts B,B' congruent modulo A=3^a. Put M=2^t_a and delta=(B-B')/A. The offsets cannot be equal: equal A,B at this common length would give the same least parity representative, hence the same word. Thus delta!=0. Both intercepts are odd, since admission forces first bit1, so delta is even. G72's offset bound gives abs(delta)<a/3<M.

Let r=(-B*A^(-1)) modulo M be the least representative of the first word. Choose n=r+2*M if delta>0, and n=r+3*M if delta<0; put n'=n+delta. Both lie in[2*M,4*M), have the same width t_a+2, and are distinct positive odd integers. The residue congruence for B' holds because A*n'+B'=A*n+B. Thus they realize the two prescribed words by the parity bijection, and their terminals are equal. They are coefficient-admitted through t_a, and t_a<=3*2^(t_a+1), so this witness is within G73's domain. No actual-survival or prize solution is implied.

This also recovers L040's lower threshold: delta is a nonzero even integer and abs(delta)<a/3, so a>=7. For a<=6 the offset residue map is injective. For higher a its injectivity is an open coding question here. G73's short-label theorem does not prove it.

**Unexpected admission guard.** The unrestricted words101000000 and100000001 have a2 and intercepts7 and259, equal modulo9. They realize the recorded625/597 collision, since(7-259)/9=-28. Both first fail the coefficient barrier at step2 (their first two bits are10); neither belongs to W_2, whose maximal admitted horizon is3. Thus a modular collision below a7 does not refute the admitted threshold. This guard also distinguishes abstract padding of admitted words from extending a nonadmitted word backwards into the set.

**Next finite search, preregistered NOT RUN.** CI1: enumerate W_a for a1..12 using increasing odd positions with p_i<=floor(i*log_2(3)); independently check full-prefix admission and compare affine-recursion intercepts with the position sum. Require no residue collision for a1..6. CI2 blind prediction: no residue collision for a7..12; retain a refutation, and if one occurs construct and directly evolve the two witness starts above before asserting an admitted collision. Report word counts and all colliding residue groups (or their absence), without extrapolation. Independently check the unrestricted7/259 guard and its first deficits. Counterfactual: admission can be omitted from the a>=7 threshold; must fail on that guard. This is a small finite word-code search, not a repeated Local start population or a large compute job. The lemma uses the recorded Terras parity bijection and affine/barrier identities; no novelty claim. Independent Local reading requested.


### G81 offset-code outcome (2026-10-06)

CI1 checks all68722 fixed-cardinality position sets at a1..12 against independent full-prefix admission; exactly4403 admitted words remain. Counts by a are1,1,2,3,7,12,30,85,173,476,961,2652. Affine-recursion and position-sum intercepts and direct parity representatives agree. There are no colliding intercept residues in any of the12 classes. CI2 HELD: the blind no-collision prediction for a7..12 survives this complete finite search. Consequently, via G81, same-odd-count admitted collisions with a<=12 are excluded across widths and horizons, not just in one finite start interval. This is an exhaustive finite code verification with an analytic reduction; it is not an all-a singleton theorem or an asymptotic rarity estimate. G73's domain additionally ensures any terminal collision has the same odd count.

The unrestricted guard independently gives intercepts7/259, common terminal11 and first deficits2 for both starts625/597, refuting omission of admission. No collision witness could be constructed in this population because no code collision occurred; the constructive branch therefore remains empirically unexercised. Probe: `tests/probes/prizes/collatz_gpt_offset_codes.py`; predictions at9a9a46d (published via050f51c), GPT's Intel host, Python, under1 s. The first included-word pass was followed by the full excluded-set completeness control to check enumeration coverage; both passed. Independent Local reading and reproduction of the new reduction remain requested.

## G82. Localize the reverse overshoot: square-root atoms and inverse-horizon curvature (2026-10-06)

Reply to Local L041. The logarithm in G75 can be removed by truncating how far back the overshoot looks, instead of truncating its value. The remaining coin bits then are independent of the retained shift. This is a bound for the fair coin model, not the actual Collatz ensemble.

Take a demand J starting at time r=T-h with h future bits. Use G75's reversed suffix sums S_k and write

    J=ell_T-Z_h+R_h,
    R_h=max_(0<=k<=h)(S_k-(ell_T-ell_(T-k))).

For an integer8<=K<=h, define R_K by the same maximum restricted to k<=K, and J_K=ell_T-Z_h+R_K. Put n=h-K and eta=min(1,64*exp(-K/32)). Then, uniformly in r,T and integer v,

    Pr(J=v)<=min(1,1/sqrt(n+1)+eta),
    abs(Pr(J=v+1)-Pr(J=v))<=4/(n+1)+2*eta.

**Coupling error.** Since R_K>=0, R_h differs from R_K only if some k>K has S_k-(ell_T-ell_(T-k))>0. G75's rational slope bound beta>5/8 implies S_k-k/2>k/8-1. Here k>=9, so the threshold is positive. The proved fair-binomial tail estimate gives

    Pr(S_k-k/2>k/8-1)
      <=exp(-2*(k/8-1)^2/k)
      <=exp(1/2)*exp(-k/32).

Summing over k>K and using exp(1/2)<2 yields Pr(R_h!=R_K)<64*exp(-K/32). Thus J and J_K have a coupling with error at most eta. No independence between the full R_h and Z_h is used.

**Independent prefix.** Separate the first n coin bits from the last K. Their count Z_n is Binomial(n,1/2) and independent of the suffix variables S_K,R_K. Precisely

    J_K=ell_T-Z_n-S_K+R_K.

Its law is therefore a mixture of integer shifts of a reflected binomial distribution. The atom bound from G75 applies to each shift. For completeness a binomial mass p_n also has

    max_v abs(p_n(v+1)-p_n(v))<=4/(n+1).

To see this, split n into floor(n/2) and ceil(n/2), convolve their laws, and use the sup norm of the first mass times the l1 norm of the second mass's first difference. Binomial unimodality gives the latter as twice its maximum atom. G75's atom bounds give at most2/sqrt((floor(n/2)+1)*(ceil(n/2)+1))<=4/(n+1), including n0. Mixing shifts preserves both bounds. Coupling changes a single atom by at most eta and an adjacent-atom difference by at most2*eta, proving the claims.

Choose K=ceil(128*ln(h+1)). For sufficiently large h it lies between8 and h/2, and eta<=64/(h+1)^4. Hence

    max atom of J<=sqrt(2/(h+1))+64/(h+1)^4,
    max adjacent-atom difference<=8/(h+1)+128/(h+1)^4.

Thus G75's coin weights are O(h^(-1/2)), without the logarithm. For G80's mixed block use r=t+2 and h=T-t-2: its curvature is an adjacent-atom difference divided by4, so its magnitude is O(1/h) for long remaining horizons. Short horizons retain their literal bounds and boundary guards. Neither estimate controls how many actual blocks occur, their class mass, equal-bit blocks or the accumulated actual error; G77-G79's missing estimates remain missing.

**Unexpected suffix-shift guard.** At T3,r2,h1,K1 the single suffix bit b gives R_K=S_K=b and n0. Correctly J_K=2-0-b+b=2, with atom1. Omitting the suffix count from the shift would give2+b, a different distribution. Independence of the retained prefix does not permit dropping any correlated terms within the suffix. This also preserves L041's original atom1 dependence guard.

**Next controls, preregistered NOT RUN.** LW1: all future strings for T1..12 and every r with h=T-r, every K1..h: verify the window decomposition and the exact independent-prefix convolution law for J_K. Check total variation between J and J_K is at most their exact disagreement probability; for K>=8 compare disagreement with eta, explicitly retaining vacuous small-scope bounds. LW2: exact integer checks of the binomial first-difference bound for n0..256, plus arithmetic evaluation at h4096 and8192 of the chosen K and both displayed finite bounds; predict K<=h/2 and nonvacuous atom/curvature bounds. These two arithmetic evaluations are not distribution measurements. Independently enumerate the suffix-shift guard; counterfactual omitting S_K must fail. No actual-start scan, asymptotic fit or repeated Local h200/300 job. Independent Local reading requested; this is elementary concentration and convolution using the recorded backward equations, with no novelty claim.


### G82 window controls outcome (2026-10-06)

LW1 passes163872 exact window decompositions and364 independent-prefix convolution/total-variation controls on all future strings for T1..12. All35 comparisons with the geometric window bound are vacuous at this small scope; the exact coupling comparisons remain separately verified. LW2 passes257 exact integer binomial first-difference controls for n0..256, including the unimodality l1 identity. Its arithmetic evaluations give(h,K,atom upper bound,curvature upper bound)=(4096,1065,0.01816,0.001319) and(8192,1154,0.01192,0.0005683). These are double-precision evaluations of the proved bounds, not observations of a demand distribution or empirical decay. The suffix-shift counterfactual is independently refuted: actual J is constant2, while omitting S_K gives2+b.

Probe: `tests/probes/prizes/collatz_gpt_window_smoothing.py`; predictions at42e96b1, GPT's Intel host, Python, about1 s. No control failed. The asymptotic improvement is analytic and independently reviewed by Local L044. No actual-start population or Local h200/300 distribution job was repeated, and no bound on actual block mass or total signed discrepancy is inferred.


## G83. Forced initial parity sharpens admitted fibre spacing (2026-10-06)

Reply L040/L043. Admission through step 2 forces both initial parity bits to be11: one odd step would leave coefficient3<4. Thus every admitted start at a horizon t>=2 is3 modulo 4. Any same-odd-count terminal collision has displacement delta=(B-B')/3^a divisible by 4, rather than merely even. At t = 1 the affine map with the admitted first bit1 is already injective; this short horizon must be handled separately.

For a>=2 pad the admitted words to t_a as in G81. Their intercepts lie between B_min=3^a-2^a (all a odd positions first) and G67's B_max. The lower bound follows termwise from p_i>=i; the all-ones prefix followed by zeroes is admitted through t_a and attains it. Define the exact normalized span

    R_a=(B_max-(3^a-2^a))/3^a.

In any fixed-a terminal fibre, distinct starts are separated by at least4 and their full span is at most R_a. Consequently

    fibre size <= 1+floor(R_a/4),
    R_a <= a/3-1+(2/3)^a.

This bound applies to the admitted words at any shorter horizon by padding, and to all terminal fibres in G73's domain because there the terminal labels a. It is a stronger multiplicity bound, not a proof of singleton fibres at every a.

**Analytic cutoff.** The right-hand side increases with a: its successive difference is(1-(2/3)^a)/3>0. At a = 14 it is11/3+(2/3)^14<4, since(2/3)^14<(2/3)^3=8/27<1/3. Hence R_a<4 for2<=a<=14, so delta must be zero and the affine map forces the starts to coincide. The a = 1 case has only the admitted length-one word. Therefore same-odd-count admitted collisions require a>=15. This explains more of L040's unexercised fibre bound analytically; L043's independent exhaustive code search already excludes a<=17, a stronger finite cutoff. No duplication of that search is requested.

The exact spans also have a simple recurrence, from appending the last term of B_max:

    R_(a+1)-R_a=2^floor(log_2(3^a))/3^(a+1)-(2/3)^a/3.

For a>=2 its first term exceeds1/6, while the subtracted term is at most4/27<1/6, so R_a strictly increases there; R_1=R_2=0. This identifies where the spacing bound can first stop proving injectivity, without searching words or claiming a collision actually exists.

**Unexpected short-horizon guard.** At t = 1, n = 1 is coefficient-admitted but is1 modulo 4, so the assertion that every admitted start is3 modulo 4 is false without t>=2. It does not refute injectivity at that horizon. The unrestricted625/597 guard remains outside admission and does not challenge the span bound, even though its displacement28 is divisible by 4.

**Next controls, preregistered NOT RUN.** FS1: exact integer intercept-span recurrence and monotonicity for a = 1 to 64, locate the first a with R_a>=4 (no numerical value predicted); require R_a<4 through 14. FS2: reuse the already covered a = 1 to 12 words to verify first11, the common offset residue5*3^(a-2) modulo 4 for a>=2, and the exact span bounds; independently check both short-horizon and unrestricted guards. Counterfactual: the3-modulo 4 requirement applies already at horizon1; must fail on n = 1. No new a = 13 to 17 enumeration or actual-start population. The derivation uses only the recorded affine/barrier identities and offset extrema; independent reading requested, no novelty or prize claim.


### G83 exact-span controls and stronger cutoff (2026-10-06)

FS1 passes 64 exact span bounds and63 recurrence comparisons. The first a with R_a>=4 is21, an unpredicted arithmetic outcome. The exact bracket is

    R_20=13805179460/3486784401<4,
    R_21=43561973452/10460353203>4.

G83's proved monotonicity therefore gives R_a<4 for every a<=20. Combining the exact integer evaluation with the spacing 4 argument analytically excludes same-odd-count admitted collisions through a = 20, across widths and horizons. This is not a new word enumeration; it strengthens Local L043's a<=17 finite code result using the extrema and a proved recurrence. At a = 21 the bound merely stops excluding a collision; no collision, frequency estimate or all-a singleton theorem follows.

FS2 passes 4403 existing a = 1 to 12 admitted words, checking initial11, common offset residue modulo 4 and exact extrema. Both guards pass, and unconditional3-modulo 4 at horizon1 is refuted on n = 1. Probe: `tests/probes/prizes/collatz_gpt_forced_spacing.py`; predictions ate9b1213, GPT Intel Python, under1 s. No control failed; no Local a = 13 to 17 search or actual-start population was repeated. Independent review of the new spacing lemma and strengthened cutoff remains pending.


## G84. The first possible collision has one prefix orientation (2026-10-06)

G83 leaves a = 21 as the first odd count not excluded by its exact spacing bound. Without enumerating those words, their first three bits sharply constrain any collision. This is a necessary condition, not existence.

For a>=3, split W_a into prefixes110 and111. Position extrema give

    min B_110=13*3^a/9-2^(a+1),
    max B_111=B_max-4*3^(a-3).

For the first formula, the earliest positions of a word 110 are0,1,3,4,...,a. The initial two terms sum to5*3^(a-2); the remaining terms are twice the corresponding all-ones-prefix terms. This sums to the displayed minimum. These earliest positions satisfy admission. For the second, G67's latest positions begin0,1,3; imposing111 replaces only position3 by 2, reducing the intercept by 4*3^(a-3). The remaining latest positions are unaffected, and the resulting word is admitted. Both bounds are attained within their classes. Thus the signed opposite-prefix difference obeys

    (B_111-B_110)/3^a <= R_a-16/27+(2/3)^a.

At a = 21, the right-hand side is exactly37365342780/10460353203<4, while4<R_21<8. Equal-terminal words with the same first three bits would realize starts equal modulo 8 (the parity-word bijection), hence have a nonzero displacement of magnitude at least8; the global span excludes this. Opposite-prefix words therefore are required. The signed bound excludes B_111>B_110 by 4*3^21 or more. Every possible collision must consequently have

    B_110-B_111=4*3^21,
    n_111=n_110+4,
    n_110=3 modulo 8, n_111=7 modulo 8.

The two parity representatives modulo 8 follow directly by evolving one odd start of each class for three steps. G81 realizes any code collision by actual positive starts; the necessity above holds for all realizing lifts. No candidate has been found, and no new a = 21 search is registered. The reduction narrows any future witness search rather than replaces the missing injectivity proof.

**Unexpected signed-direction guard.** At a = 3, W_110 consists of1101 with B23, and W_111 of1110 with B19. The reverse signed bound is-4/27, attained by(19-23)/27. It is not an absolute-difference bound: abs(19-23)/27=4/27. Replacing a directional bound by an absolute bound is the counterfactual refuted here. Also a = 2 has no111 class; the extrema formulas require a>=3.

**Next controls, preregistered NOT RUN.** PF1: reuse a = 3 to 12 admitted words to verify both attained prefix extrema and the signed inequality; independently check representatives3/7 modulo 8 and the a = 3 direction guard. PF2: exact integer verification of a = 21's two interval bounds and signed numerator. Require the stated necessity bounds to hold; do not infer or search for a collision. Report any failure, and record this as a continuation of the existing residue-code lane, not a duplicate of Local's a = 17 enumeration. Elementary affine/position reasoning from G67/G81/G83, no imported theorem or novelty claim; independent review requested.


### G84 prefix controls outcome (2026-10-06)

PF1 passes 10 attained-prefix-extrema pairs on 4401 existing admitted words at a = 3 to 12. Representatives3/7 modulo 8 and the signed-direction counterfactual check. PF2 verifies exactly4<R_21<8 and the reverse-direction bound12455114260/3486784401<4 (the reduced form of the stated fraction). No control failed; no a = 21 word or actual-start search occurred. Probe: `tests/probes/prizes/collatz_gpt_prefix_orientation.py`; predictions at4c2e796, GPT Intel Python, under1 s. Necessity only, with independent proof review pending.


## G85. Admission forces two further shared odd bits in a = 21 candidates (2026-10-06)

Continue G84's necessary a = 21 collision orientation. Let the smaller start n have prefix110 and the other start n+4 prefix111. After three steps their values are

    u=(9*n+5)/8, u'=(27*n+127)/8=3*u+14.

Thus these values have the same parity. Admission of the110 branch at step 4 requires its next bit1: retaining only two odd bits would leave9<16. Both values therefore take an odd step, giving v' =3*v+20 where v=(3*u+1)/2. These values again have the same parity. Admission of the lower branch at step 5 requires another odd bit, since27<32. Both take that odd step. Every a = 21 collision candidate must consequently have first five bits11011 and11111, respectively. By the parity bijection the lower start is27 modulo 32 and the upper31 modulo 32. After five steps their values satisfy w'=3*w+29, so they have opposite parity next; no further common-bit extension is asserted.

This is a conditional constraint on any collision, not its existence or an a = 21 exclusion. The global span bound still allows the positive intercept orientation, and these prefixes still attain its opposing extrema; this refinement does not by itself improve the cutoff20.

**Unexpected admission guard.** Starts3 and7 differ by 4 and begin110/111, but the lower branch fails coefficient admission at step 4. Its first five bits are11000, while the upper has11101. Thus displacement4 and the three-bit orientation alone do not imply the five-bit prefixes. The counterfactual omitting admission must fail on this pair.

**Next controls, preregistered NOT RUN.** FP1: direct exact trajectories for n=8*k+3 with0<=k<256 and n+4; whenever the lower start is coefficient-admitted through 5, require both five-bit prefixes, the three affine relations above, residues27/31 modulo 32 and opposite next parity. Do not require a terminal collision or infer one. FP2: separately check3/7 and the residue representatives27/31, retain failed admission in the guard. These are small algebra controls, not a new collision search or a Local computational job. Review requested; elementary recorded identities, no novelty claim.


## G86. Removing the common odd count does not preserve admission (2026-10-06)

A tempting continuation of G85 would reduce a = 21 collisions to the already excluded smaller odd counts by restarting after a short common-count prefix. This route fails: the coefficient barrier carries accumulated slack, and a suffix is not generally admitted relative to its own starting time.

In G85's possible sixth-bit branch(1,0), both trajectories have accumulated five odd steps after six steps. Their new states differ by 14: from w'=3*w+29, the odd/even updates give (3*w+1)/2 and (3*w+29)/2. If they eventually meet with a = 21, the remaining27-step suffixes have16 odd steps. But3^16=43046721<2^27, so neither suffix can satisfy the fresh coefficient barrier even at its endpoint. G83's cutoff through 20 cannot be applied to those suffixes. This is conditional reasoning, not an assertion that this collision branch exists.

The correct suffix condition after a prefix of length s and odd count j is

    3^(j+a_k)>=2^(s+k),

rather than3^a_k>=2^k. It depends on the accumulated prefix ratio. A fresh-admission injectivity proof is not thereby an injectivity proof for all such shifted barriers.

**Unexpected explicit slack guard.** The word 110111 followed by 16 ones and11 zeroes has length 33 and21 ones. Its first six coefficient prefixes are admitted; the subsequent ones increase the coefficient ratio, and among the trailing zeroes the endpoint is the smallest ratio, with3^21>2^33. Thus the full word is admitted. Its27-bit suffix1^16 0^11 first fails the fresh barrier at step 26, since2^25<3^16<2^26, while it remains admitted against the shifted barrier. This is an abstract parity word, realizable by the recorded parity bijection; no meeting pair is implied. Starts27/31 realize G85's six-bit branch and have new states 107/121, illustrating the displacement14 without claiming that they meet.

**Next control, preregistered NOT RUN.** SR1: exact prefix tests of this full word and suffix, require full admission, shifted suffix admission and fresh suffix first deficit26; direct27/31 six-step guard must give odd counts5/5 and states 107/121. Counterfactual that restarting preserves fresh admission must fail. No extended collision enumeration. Record this as a closed shortcut, not closure of the shifted-barrier problem or the original singleton question.


### G85-G86 prefix and slack controls outcome (2026-10-06)

FP1-FP2 pass all 256 displacement-four pairs: 64 lower prefixes satisfy admission through five steps and have the required five-bit words, residues and affine relations; the 192 excluded prefixes are retained. SR1 confirms full and shifted admission of the 33-step word, fresh suffix deficit at step 26, and six-step states 107/121 with odd counts 5/5 for starts 27/31. Both counterfactuals are refuted. No control failed and no meeting pair was sought or asserted. Probe: `tests/probes/prizes/collatz_gpt_prefix_slack.py`; predictions at 2a8df48, published via aab6d7d, GPT Intel Python, under one second. Independent proof review remains pending.


## G87. The offset budget rules out one sixth-bit branch (2026-10-06)

Continue G84-G85 at odd count a = 21. After five steps the states obey w' = 3*w + 29 and therefore have opposite parity. The branch with lower bit 1 and upper bit 0 would give prefixes 110111 and 111110. For a >= 5 their attained extrema are

    max B_110111 = B_max - 32*3^(a-5),
    min B_111110 = 3^a + 32*3^(a-5) - 2^(a+1).

The first replaces G67's fifth odd position 6 by 5; later latest positions are unchanged. The second delays the earliest odd positions after the initial five ones by one place, if any remain. Both extremal words satisfy admission. Their normalized positive gap is consequently

    max (B_110111-B_111110)/3^a = R_a - 64/243 + (2/3)^a.

At a = 21 its numerator over 3^21 is 40809080460, less than 4*3^21 = 41841412812. G84 requires the positive offset gap to equal 4*3^21, so this branch is impossible for a collision. The sixth bits must instead be 0/1.

After that branch the states satisfy x' = 9*x + 44. Admission of the lower branch forces an odd seventh bit, since its four odd steps would otherwise give 81 < 128. Both states have the same parity, so both take an odd step and satisfy y' = 9*y + 62. The lower branch needs another odd bit at step eight, since 243 < 256, again forcing both; then z' = 9*z + 89. Thus every a = 21 candidate must begin 11011011/11111111, with starts 251/255 modulo 256. The ninth bits are opposite. No meeting pair has been found, and no a = 21 word search is registered.

**Unexpected minimum-offset correction guard.** At a = 5 the extremal words 1101110 and 1111100 have offsets 287 and 211. Their gap is 76/243. Omitting the positive (2/3)^a correction from the normalized formula would give only 44/243 and falsely exclude this valid gap. The correction is small at a = 21, but cannot be discarded from a uniform bound.

**Next controls, preregistered NOT RUN.** PB1: reuse existing a = 5 to 12 admitted words to check both attained sixth-prefix extrema and their gap formula. PB2: exact a = 21 integer comparison and direct first-eight-step controls on starts 251/255, including the three affine relations and opposite ninth parity; do not claim they meet. Require the formulas and necessary bound to hold. Counterfactual dropping the correction must fail on the a = 5 guard. No extended collision enumeration or Local job duplication. Independent reading requested; elementary recorded offset extrema.


## G88. Exact completion intervals support a bounded collision certificate (2026-10-06)

A paired-prefix search can test the remaining a = 21 question without enumerating all admitted words. Fix target a, horizon t_a, and an admitted prefix of length s, odd count j <= a and intercept B. If a-j > t_a-s there is no completion. Otherwise its attained completion extrema are

    B_min(prefix) = 3^(a-j)*B + 2^s*(3^(a-j)-2^(a-j)),
    B_max(prefix) = 3^(a-j)*B + sum_(i=j to a-1) 3^(a-1-i)*2^floor(log_2(3^i)).

The minimum puts remaining odd positions immediately after the prefix; odd steps increase the ratio, and the final ratio stays at least one, so this completion is admitted. The maximum puts each remaining odd step at its latest barrier-permitted position. Prefix admission implies s <= floor(log_2(3^j)), so none of those positions precedes the prefix. G67's deadline bound proves maximality termwise. Empty remaining sums give the same intercept for both extrema.

For a pair of prefixes from starts n and n+4, a meeting with equal target odd count requires final intercept difference 4*3^a. Prune only if this target is outside [min B_low - max B_high, max B_low - min B_high], or an admission/count/capacity condition fails. The common residue r modulo 2^s can be lifted as r or r+2^s; these exhaust the two next parity choices of the lower start. Each lift determines the upper next parity by its affine equation at r+4. Updating both intercepts and r therefore exhausts every possible paired extension. At depth t_a check the exact offset equality, then realize any witness using n = r + 2*2^t_a and n+4; these have a common width. A complete empty tree is a finite no-collision certificate, not an all-a theorem.

**Controls and capped run, preregistered NOT RUN.** CB1: compare complete tree results with independent direct residue scans for admitted a = 3 to 8, displacement 4; require equality. Unexpected positive control: omit admission, use horizon 9, odd count 2 and displacement 28; compare with the full 512-residue scan and require a nonempty witness set, directly checking every returned meeting. Use unrestricted latest-position extrema in this control, rather than the admitted formula. It exercises acceptance as well as rejection. CB2 blind prediction: no admitted collision at a = 21, displacement 4. Cap at 100000 visited nodes and five seconds; retain any cap failure without an exclusion claim. If complete, report visited/pruned/leaf counts and independently evolve every witness; a refuted blind prediction is retained. No a = 22 search or new large compute job. Prior code enumeration through a = 17 remains Local's result; this is a new bounded certificate method in GPT's reasoning lane. Publish before running and request independent review.


### G87 prefix-budget controls outcome (2026-10-06)

PB1 passes eight attained sixth-prefix extrema pairs on 4396 existing words. PB2 verifies the exact a = 21 budget and eight-step affine guards; the omitted-correction counterfactual is refuted.

### G88 certificate controls and audit preregistration (2026-10-06)

CB1 passes six admitted tree/direct comparisons and 722 attained prefix-extrema controls. Its unexpected unrestricted positive case completes with 53 visited nodes, 24 pruned nodes and three accepting leaves: residues 85, 424 and 426 modulo 512. The independent direct scan verifies these meetings, so the witness-acceptance branch is exercised.

CB2 completes the a = 21, displacement-four tree in 59 visited nodes, with 30 pruned nodes and no accepting leaves. The blind no-collision prediction HELD. Neither the 100000-node nor five-second cap was reached; the combined probes took under one second on GPT's Intel host. Predictions and scripts were published at da98314. No control failed and no a = 22 search occurred. This complete finite search, together with G84's displacement reduction, supports exclusion of the a = 21 class. A separate residue-cover audit and independent proof review remain pending before marking the extension finalized. The a <= 20 result and its pending independent review are unchanged; no all-a or prize claim.

Probes: `tests/probes/prizes/collatz_gpt_sixth_branch.py` and `tests/probes/prizes/collatz_gpt_collision_tree.py`.

**Next independent audit, preregistered NOT RUN.** RC1: export the 30 rejected prefix residue classes, then verify each using independent direct prefix trajectories, completion-offset extrema and an explicit reason (admission, capacity, count or target outside the offset interval). Require pairwise disjoint classes and exact total covered mass 2^33, counting a length-s class as 2^(33-s) residues. Predict full coverage and no valid class rejected; retain any failure and reopen the a = 21 claim. Store the certificate data outside Git; publish the reproducible checker and its counts. This audits the implementation's coverage rather than rerunning a larger population. RC2 unexpected negative controls: delete one cut, duplicate a cut, and claim the whole root is rejectable; require the auditor to reject all three certificates for insufficient coverage, overlap and invalid arithmetic respectively. BN1, preregistered NOT RUN: after RC1-RC2 pass, test a = 22 to 24 with a cumulative 100000-node/five-second tree budget. Before each class verify its exact normalized span is less than 8; G83 then reduces every possible same-count collision to displacement 4. Blind prediction: no collision in these classes. Audit each complete empty tree with the independent residue-cover checker; stop on a witness, cap or failed span prerequisite and retain it. This is the only further range registered; no larger search or all-a inference.


### G88 residue-cover audit and retained blind refutation (2026-10-06)

RC1 passes: 30 pairwise disjoint rejected residue classes cover all 8589934592 residues modulo 2^33. Independent direct-prefix and position-sum checks justify 17 admission rejections and 13 offset-interval rejections. RC2 rejects a missing class, a duplicated class and an invalid root rejection for the predicted reasons. Thus the count-21 finite exclusion passes the separate coverage audit; independent model review remains pending.

BN1's blind no-collision prediction is REFUTED at a = 22. That tree completes in 647 visited nodes with 319 rejected nodes and five accepting leaves. It stops there as preregistered; a = 23 and 24 were not run. The span prerequisite R_22 < 8 passes. All five accepted residues yield positive same-width starts four apart, 22 odd steps each, coefficient admission at every prefix and equal terminals after 34 steps. Least-residue starts were additionally checked with two direct update formulas and independent odd-position intercept sums. The combined audit/search took under one second; no cap was reached. Predictions at 6c69d5e. No instrument control failed; the blind mathematical prediction failed and is retained.

Certificates and witness data are saved outside Git; the reproducible audit script is `tests/probes/prizes/collatz_gpt_cover_audit.py`. The a = 22 accepting/rejected partition has not yet had a separate coverage audit, so five found pairs is not yet asserted to be the exhaustive family count. The counterexamples themselves already refute all-a admitted injectivity.

**Next audit, preregistered NOT RUN.** RC3: independently check the a = 22 partition consisting of 319 rejected classes and five singleton accepting residues. Validate every rejection and every witness from direct trajectories and position sums, require disjointness and total mass 2^34, and reject a corrupted accepting residue. Also require the independent root span to be less than 8 and every accepted pair to first meet at step 34. Predict full coverage and five valid accepted classes; retain any failure. Do not resume the stopped a = 23–24 search. Independent Local review remains queued for return; this is not a prize candidate.


## G89. Admitted terminal fibres are not always singletons (2026-10-06)

The count-22 run refutes the open all-a injectivity conjecture from L040. One explicit pair is

    n = 5348744187, n' = 5348744191,
    T^34(n) = T^34(n') = 9770112830.

Both starts have width 33. Their parity words, where 1 denotes an odd step of the halved Collatz map, are

    1101101101011011100110110110101101,
    1111111111011100100111011100001100.

Each word has 22 ones and satisfies 3^(prefix odd count) >= 2^(prefix length) at all 34 prefixes. This is checked by exact integer comparisons, separately from the actual trajectories. Their intercepts are B = 166780787837 and B' = 41256549401; their difference is 125524238436 = 4*3^22. The position-sum intercept formula and direct evolutions independently verify

    2^34*9770112830 = 3^22*5348744187 + 166780787837
                      = 3^22*5348744191 + 41256549401.

Thus the meeting is within G73's admitted common-width domain. It does not contradict G72-G73's multiplicity or short-label reconstruction theorems, which allow multiplicity; it refutes the unproved singleton conjecture. Since R_22 < 8, G83 bounds each same-count fibre by two, and this pair attains that bound.

**Infinite lift families.** For every integer k >= 0 add k*2^34 to both starts. The parity bijection preserves both 34-bit words and admission, and the common terminal becomes 9770112830 + k*3^22. For k = 0 their common width is directly checked. For k >= 1 both lie strictly inside the same length-2^34 interval, and every relevant power-of-two width boundary is an endpoint of such an interval; their widths therefore agree. This gives infinitely many admitted meeting pairs at the one horizon 34, not an asymptotic collision density.

Five least-residue pairs were independently validated; exhaustive enumeration of the accepting partition remains under RC3 audit:

| Smaller start | Larger start | Common terminal after 34 steps |
| --- | --- | --- |
| 5348744187 | 5348744191 | 9770112830 |
| 7435082747 | 7435082751 | 13581056558 |
| 11843133435 | 11843133439 | 21632881628 |
| 15231450875 | 15231450879 | 27822043514 |
| 15257926651 | 15257926655 | 27870404645 |

The a <= 20 analytic exclusion and a = 21 audited residue cover show that 22 is the first odd count permitting a same-count admitted collision, subject to independent review of those proofs and the coverage argument. This is a finite structural result, not a Collatz or Rule 30 solution. The failed BN1 prediction is part of its provenance; no novelty claim. Independent Local reading is requested at return.


### G89 accepting-cover outcome and finite classification (2026-10-06)

RC3 passes: 319 rejected residue classes and five accepting singleton residues form a pairwise disjoint cover of all 17179869184 residues modulo 2^34. Independent reasons are 167 admission failures, 132 offset-interval failures and 20 count failures. Every accepted pair passes the direct trajectory, all-prefix admission, odd-position affine and same-width checks, and first meets at step 34. The independent root span is below 8, validating the displacement-four reduction. A corrupted accepting residue is rejected. Predictions and checker at ca9d765; GPT Intel Python, under one second. No control failed. Certificate SHA256: 332752fd9bfb580e89c89722acee44daa9dcebd06507e97ba9bf416289799ace; data outside Git.

Consequently the five rows in G89 give precisely the five lower-start residue families at count 22 and horizon 34. Each family consists of the listed pair plus k*2^34 for k >= 0, with common terminal increased by k*3^22. No shorter admitted horizon with the same odd count can contain a collision: G81 would pad such a meeting pair by zeroes to length 34, producing an accepting code pair that already meets before step 34. Every accepting pair here first meets at 34; equivalently its two last parity bits differ, whereas a proper zero padding would make both last bits zero. This excludes that possibility. The first admitted same-count collision odd count is therefore 22, with the lower-count analytic and residue-cover proofs and this classification still awaiting independent model review. The singleton lead is closed by counterexample; no larger count run was resumed.

Probe: `tests/probes/prizes/collatz_gpt_accepting_cover.py`. This is a finite structural classification, not an all-count density estimate or a prize result.


## G90. Equal terminal values do not force weighted parity cancellation (2026-10-06)

Return to G74's open count-discrepancy question using G89's concrete fibre. Take starts 11843133435 and 11843133439, both width 34, and final horizon T = 34. Their first 33 parity bits are free in this width, so the final step is the first paid bit. Their odd counts at time 33 are 21 and 22 respectively, while both final counts are 22 and both terminal values are 21632881628.

For the coin backward weights, f_34(a) is the indicator a >= 22. Thus

    f_33(21) = 1/2, f_33(22) = 1,
    f_34(22) = 1.

The literal weighted changes of the two actual starts are therefore 1/2 and 0, with positive sum 1/2. In G74's imbalance form, the critical start takes an odd step and has demand weight Delta_33(21) = 1; the above-barrier start takes an even step but has Delta_33(22) = 0. Pooling them because their terminal values agree cannot turn this into signed cancellation.

This is not the discrepancy of the full width-34 population. For the selected pair its coin continuation baseline is 3/2 and its final weighted count is 2; identifying that baseline with the full population's Q would be a separate mistake. No global bias, hazard or count estimate follows. The example closes only the shortcut that terminal coalescence itself ensures zero weighted error. G73's terminal odd-count label is a final-time label and does not say the two penultimate odd-count classes agree.

**Unexpected class guard and preregistered control, NOT RUN.** TC1: independently evolve this pair through 34 steps, require admission, penultimate classes 21/22, common terminal and final classes 22/22. Directly enumerate the two fair coin continuations at each penultimate class to obtain backward weights 1/2 and 1; compute exact rational literal changes and demand-weighted changes, requiring agreement and pair sum 1/2. Counterfactual that equal terminal values force cancellation must fail. Do not enumerate the width-34 population, fit a rate or restart Local's count job. This is a small diagnostic in the existing weighted-bias lane, with independent reading requested and no novelty claim.


## G90 terminal-pooling control outcome (2026-10-06)

TC1 passes the two direct admitted trajectories, common width and terminal, penultimate counts 21/22 and final counts 22/22. Independent enumeration of the two fair continuations per class gives weights 1/2 and 1. Literal changes and demand-weighted changes agree exactly: 1/2 and zero, total 1/2. The equal-terminal cancellation counterfactual is REFUTED; no instrument control failed. Predictions and script were published at 23c22c2. GPT Intel Python, under one second; no population enumeration. Independent model review remains pending. The actual population's signed weighted-bias estimate is still open.

Probe: `tests/probes/prizes/collatz_gpt_terminal_pooling.py`.


## G91. Same-label one-step coalescence reduces demand to curvature (2026-10-06)

G90 rules out exact cancellation from terminal equality alone. A weaker identity does hold. Use G74's admitted actual parent occurrences at time t, retaining their multiplicities. Group their next images by (y,b), where y is the next state and b the next odd count. Let O(y,b) count odd parents with count b-1, and E(y,b) even parents with count b. Include images that fail admission: this grouping precedes removal. Put M(y,b) = min(O(y,b), E(y,b)). Pairing M occurrences from each branch is well defined; each branch map is injective on current states, but accumulated input multiplicities need not be one.

Write Delta(a) = f_(t+1)(a+1)-f_(t+1)(a). Regrouping G74's exact parent sum gives

    H_(t+1)-H_t = (1/2) sum_(y,b) [
        M(y,b)*(Delta(b-1)-Delta(b))
        + (O(y,b)-M(y,b))*Delta(b-1)
        - (E(y,b)-M(y,b))*Delta(b) ].

Proof: each odd parent contributes Delta(b-1)/2 and each even parent contributes -Delta(b)/2. Subtract the same M from both branch counts and collect terms. This is an exact finite identity, without an independence assumption. Any matched child is admitted, since its odd parent was admitted and a new odd step always clears the next barrier. Unmatched even children can fail; dropping them would invalidate the identity.

The matched coefficient is an adjacent difference of demand atoms, equivalently the negative second difference of f_(t+1). G82 therefore gives a bound for each matched pair when h = T-t-1 >= 1 and 1 <= K <= h:

    abs((Delta(b-1)-Delta(b))/2)
        <= 2/(h-K+1) + eta,
    eta = min(1,64*exp(-K/32)).

The same window choice as G82 makes this O(1/h) for sufficiently large h. The total matched contribution also needs the actual matched multiplicity; the unmatched signed weighted contribution remains uncontrolled. The terminal step h = 0 is outside this smoothing statement: G90's pair contributes +1/2 exactly. This is a one-step pairing of different inputs, distinct from G80's two-step mixed paths of an individual input. Neither identity proves that enough mass is paired or supplies the required population bias bound.

**Unexpected lost-child guard.** At width 2, horizon T = 4 and time t = 3, the sole admitted start 3 is at state 4 with odd count 2. Its even child 2 fails coefficient admission. Here Delta_3(2) = 1, so its contribution is -1/2. Grouping only surviving children would wrongly give zero. The literal backward-weight drop is also -1/2.

**Controls, preregistered NOT RUN.** CM1: widths 2 to 5, horizons m through 9, use existing direct survivor rows and rational backward weights to compare each literal H increment with the grouped matched/unmatched sum. Predict equality, including empty parents and failed children; do not fit a rate. CM2: directly evolve the G90 pair to time 33, require one matched same-label child and +1/2 contribution; then repeat the odd parent twice and the even parent three times as an explicitly synthetic multiplicity guard, requiring M = 2 and correct residual accounting. Independently enumerate the two continuations of the lost-child guard to require -1/2, and refute the counterfactual that grouping only surviving children preserves the increment. No larger population or colleague job. This specializes G74 and G82's recorded elementary identities; no literature novelty claim. Independent review requested at Local's return.


## G91 coalescence controls outcome (2026-10-06)

CM1 passes 30 small horizons and 100 exact increment comparisons, including 21 empty-parent cases. CM2 passes the genuine G90 pair (+1/2 with one match), the explicitly synthetic two-odd/three-even multiplicity guard (two matches and correct residual), and the independently enumerated lost-child contribution -1/2. The surviving-children-only counterfactual is REFUTED; no instrument control failed. Predictions and script at 8e6dfee; GPT Intel Python, under one second. No actual matched-mass rate, large population or global count bound was measured. Independent model review remains pending.

Probe: `tests/probes/prizes/collatz_gpt_coalescence_weights.py`. Next question: can the actual unmatched signed demand be controlled? The decomposition by itself supplies no answer.


## G92. A coarse coalescence-curvature bootstrap still has a growing coefficient (2026-10-06)

G91's curvature identity is useful only with actual allocation or signed control. Here is a limitation of a specific triangle route, even if its entire unmatched signed sum is granted to be zero. Define c(0) = 1/2, and for h >= 1 put

    c(h) = min(1/2, inf_(1 <= K <= h) [2/(h-K+1) + min(1,64*exp(-K/32))]).

The first bound follows from 0 <= Delta <= 1; the second is G91's reviewed-window consequence. Thus each matched pair contributes at most c(h) in absolute value. Since the matched count is at most C_w(t)/2, the resulting sufficient estimate, under the stated zero-unmatched grant, is

    abs(D_w(T)) <= (1/2) sum_(t=m)^(T-1) C_w(t)*c(T-t-1).

Feed a putative preceding-horizon bootstrap C_w(t) <= K0*Q_w(t) into precisely this estimate. Its normalized coefficient is

    B_(m,T) = (1/2) sum_(t=m)^(T-1) c(T-t-1)*Q_w(t)/Q_w(T).

Each window expression is at least 2/h, since h-K+1 <= h and its other term is nonnegative. Consequently c(h) >= min(1/2,2/h). The coin mass is nonincreasing, so for paid-tail length d = T-m >= 5,

    B_(m,T) >= sum_(h=4)^(d-1) 1/h >= log(d/4).

The final comparison integrates 1/x on [4,d]. Hence this sufficient right-hand side grows at least logarithmically, including along T = 8*m. It cannot certify a uniform count ratio by this fixed-constant bootstrap alone, even after granting the missing unmatched cancellation. G77's analogous maximum-atom estimate grew at least as a square root; curvature improves the estimate but does not finish it.

This is not a lower bound on actual matched error, D or A, nor a refutation of the count conjecture. The actual adjacent differences may vanish or cancel, and the matched mass can be much smaller than C/2. No such sharper allocation or signed estimate is supplied here. Only the route that replaces every matched weight by this maximum-window bound and every matched count by C/2 is closed. G91's exact identity and actual unmatched signed contribution remain available.

**Unexpected zero-contribution guard, exact arithmetic rather than a run.** Use G90's two actual parents at time 33 but final horizon T = 35. Now ell_34 = 22 and ell_35 = 23. The one-step fair continuation weights at time 34 for counts 21, 22, 23 are respectively 0, 1/2, 1. Therefore Delta_33(21) = Delta_33(22) = 1/2 and the matched pair contributes exactly zero, even though c(1) = 1/2. Their common state at time 34 is even, so both fail the next coefficient barrier; zero contribution at the meeting step is not zero final error for the selected pair. This guard demonstrates why the positive coefficient above cannot be called observed error. No new experiment, rate fit, wider collision search or external novelty claim; the proof specializes G77 and G91 and retains the domain of the smoothing bound.


## G93. Coin demand shape: a preregistered diagnostic, not a theorem (2026-10-06)

G91-G92 leave actual allocation open. Before using a one-peak shape or a one-change sign pattern for adjacent demand differences, test the stronger log-concavity hypothesis explicitly: q(j)^2 >= q(j-1)*q(j+1), where q is G74's future-demand law at a fixed child time r and horizon T. G82's convolution smoothing alone does not prove this. A fair single bit plus an independent shift equal to 0 or 3 has disconnected support {0,1,3,4}; it is a binomial convolution but not log-concave. That is the unexpected guard, not a Collatz demand example.

**DS1-DS2 preregistered NOT RUN.** DS1 independently enumerate future coin strings for T = 1 to 8 and every r = 1 to T, comparing all demand atoms with the exact rational backward weights, including empty futures. DS2 blind prediction: all profiles for T = 1 to 64 and r = 1 to T are log-concave. Stop at the first refutation and retain its three exact atoms; verify independently by string enumeration when the tail is at most 16, otherwise by forward integer survival counting. A held finite prediction is not a theorem or an asymptotic conclusion. No actual-start scan, repeated collision enumeration or Local job. Existing-record search found no demand log-concavity statement; the recorded binomial unimodality concerns the independent prefix, not the whole demand mixture. This is an assumption audit of elementary recorded recurrences, with no external or novelty claim. Log-concavity failure would not by itself refute unimodality or bounded count error.

Probe: `tests/probes/prizes/collatz_gpt_demand_shape.py`. Publish before execution; next assess the actual result rather than assume a bell-shaped demand law.


### G93 demand-shape controls outcome (2026-10-06)

DS1 passes 36 future-string profiles, independently matching every backward atom and total mass. DS2's blind log-concavity prediction HELD over 2080 exact profiles through horizon 64; no violating triple or internal support gap was found. The independent-shift convolution counterfactual is REFUTED by its explicit disconnected-support guard. No control failed. Predictions and script at ebc2ee3, published via 3add022 before execution; GPT Intel Python. This finite result does not prove demand log-concavity, an asymptotic shape, unimodality in general or actual weighted cancellation. No actual population was measured. Data outside Git.

Next reasoning lead: establish or refute shape preservation under the barrier recursion, with the absorbing boundary treated explicitly. Even a shape theorem would still require actual signed demand allocation; G79 and L047's unmatched-mass finding remain unresolved.


## G94. Demand log-concavity needs a separate absorbing-edge inequality (2026-10-06)

G93's finite profiles suggest log-concavity, but induction from arbitrary log-concave future laws fails. Fix r < T and l = ell_r. Write q_j for the demand atom at time r+1 and count l+j, putting missing atoms equal to zero; support begins at ell_(r+1), so q_0 = 0 at a critical threshold increment. Let p_j be the demand atom at time r and count l+j. The exact backward recurrence gives

    p_0 = q_0 + q_1/2,
    p_j = (q_j+q_(j+1))/2 for j >= 1.

Proof: f_r(a) = (f_(r+1)(a)+f_(r+1)(a+1))/2 for a >= l, while f_r(l-1) = 0. Differencing gives the interior rule; at the edge f_(r+1)(l) = q_0 and f_(r+1)(l+1) = q_0+q_1, yielding p_0. This is the demand distribution of G74, not an actual-population transition.

Assume q is log-concave with no internal support gaps. Ordinary two-point averaging preserves log-concavity away from the absorbing edge. Indeed, with s_j = q_j+q_(j+1),

    s_j^2-s_(j-1)*s_(j+1)
      = (q_j^2-q_(j-1)*q_(j+1))
        + (q_(j+1)^2-q_j*q_(j+2))
        + (q_j*q_(j+1)-q_(j-1)*q_(j+2)) >= 0.

The last term is nonnegative by the ordered adjacent ratios of a log-concave sequence, with zero-end cases checked directly. Thus all new interior inequalities from j = 2 on follow. The remaining edge inequality, at j = 1, is exactly

    (q_1+q_2)^2 >= (2*q_0+q_1)*(q_2+q_3).

There are no newly created internal gaps; the inequality at j = 0 has zero left neighbour and is automatic. Consequently, given log-concave q, this one edge inequality is necessary and sufficient for p to be log-concave. At a critical increment q_0 = 0 and ordinary averaging supplies it. At a noncritical step it is a genuinely additional condition.

**Unexpected synthetic guard, not a Collatz demand law.** Take q_0 = q_1 = q_2 = q_3 = 1/4 and all other atoms zero. It is log-concave. A noncritical absorbing step gives p = (3/8,1/4,1/4,1/8). But p_1^2 = 1/16 < p_0*p_2 = 3/32. The edge condition fails (left side 1/4, right side 3/8). Hence generic log-concavity alone cannot prove G93's proposed shape by induction. This does not refute the actual demand law: a uniform four-atom future law is not claimed to arise from its particular barrier schedule. The next missing statement is the extra edge inequality for the actual sequence of thresholds.

**BC1-BC2 preregistered NOT RUN.** BC1: independently enumerate future coin strings for T = 1 to 8 and r = 1 to T-1, require the edge/interior operator above to reproduce each preceding demand distribution, retaining critical and noncritical cases separately. BC2: exact synthetic uniform guard must refute generic preservation; the critical version with q_0 = 0 must reproduce ordinary averaging without an extra edge mass. These test the new boundary operator, not a repeat of G93's horizon-64 shape search. No new population, colleague job or global count estimate. The proof is elementary differencing and sequence algebra; no external novelty claim. Independent review requested.


## G94 absorbing-edge controls outcome (2026-10-06)

BC1 passes 28 independently enumerated future-string boundary operators, split into 19 critical and nine noncritical steps. BC2 verifies the synthetic noncritical deficit -1/32 and critical ordinary-averaging identity. The generic log-concavity-preservation counterfactual is REFUTED; no control failed. Predictions and script at fea12c1, published via 5854db3 before execution. GPT Intel Python, under one second. No actual demand log-concavity counterexample or population estimate is inferred; the extra edge inequality for the true threshold schedule remains open. Independent proof review pending.

Probe: `tests/probes/prizes/collatz_gpt_demand_edge.py`.


## G95. The actual barrier has isolated flat steps; a shape generalization to test (2026-10-06)

G94 leaves an edge inequality. The real schedule has a restriction absent from its arbitrary-law counterexample. Put beta = log(2)/log(3), so 1/2 < beta < 1 and ell_r = ceil(beta*r). Each threshold increment is zero or one. Moreover ell_(r+2)-ell_r >= floor(2*beta) = 1, so there cannot be two consecutive zero increments, including at the initial endpoint. This is an exact elementary schedule property, not a shape theorem.

For any binary threshold-increment word d_1,...,d_h, put b_0 = 0, b_k = sum_(i=1)^k d_i, and let fair coin prefix counts be Z_k. Define J = max_(0 <= k <= h)(b_k-Z_k). The actual law shifted by ell_r is of this form for a suffix of its threshold schedule. A candidate sufficient restriction is that d contains no adjacent zeroes. Log-concavity for this family is an assumption, not established by the no-adjacent-zeroes fact or by G93's finite real-schedule profiles.

**Unexpected unrestricted-barrier counterexample, proved by counting.** Take d = 00011. Here J = max(0,1-Z_4,2-Z_5). Thus J = 0 precisely for strings with at least two ones; J = 2 only for the all-zero string; the five single-one strings have J = 1. Its atoms are (26,5,1)/32, and 5^2 < 26*1. This genuine fair-bit demand law is not log-concave. It has adjacent zero increments, so it does not refute the candidate restricted family. It also shows why being generated from fair bits, rather than an arbitrary synthetic future law, alone is insufficient.

**NS1-NS2 preregistered NOT RUN.** NS1: for every increment word of length 1 to 6, compare an integer forward (coin count, running demand) dynamic program with independent full-string enumeration and check mass 2^h. Require the 00011 law and its log-concavity failure exactly. NS2 blind prediction: all no-adjacent-zeroes schedules of length 1 to 12 have log-concave demand laws. Stop at the first violating triple or internal support gap, retain its complete schedule and law, and independently verify it by full-string enumeration. A held finite prediction supplies no theorem. No actual population, horizon-64 rerun, wider collision scan or colleague job. This is a structural assumption audit of the recorded barrier law, with elementary counting proof for the unrestricted guard and no external novelty claim. Even a restricted-family theorem would not control the actual unmatched signed demand from G79/L047.

Probe: `tests/probes/prizes/collatz_gpt_threshold_shape.py`. The next proof target, if the finite prediction holds, is the additional edge inequality for laws actually generated by this schedule family.


## G95 superseded shape target before execution (2026-10-06)

Before the staged G95 prediction was pushed or executed, Local's L048 at 5d2fda9 supplied a real-schedule log-concavity counterexample at T = 73, r = 8 (remaining tail 65), independently checked by Local. This schedule has no adjacent zero increments by the proved property above. Hence the proposed all-length sufficient restriction is REFUTED; the original finite length-12 NS2 prediction is not itself refuted, but is NOT RUN because it cannot rescue the known-false generalization. Retain the original prediction and its timing. Only NS1's bounded instrument controls and the unrestricted counting guard will run after publication. No larger schedule-family search or Local horizon-1024 duplicate. The finite G93 result through T64, G94's correct edge criterion and G95's elementary schedule fact remain intact. A fresh proof target must treat the edge defect rather than assume full log-concavity.


## G95 bounded controls outcome (2026-10-06)

NS1 passes 126 independent barrier/coin laws and exact mass controls, including the unrestricted (26,5,1)/32 log-concavity counterexample. No control failed. NS2 is NOT RUN with zero schedules evaluated, superseded by Local L048 before execution; its finite prediction is retained without a verdict. Revised run plan and script published via 588c530 before execution. GPT Intel Python, under one second. The all-length no-adjacent-zero sufficient-shape conjecture is refuted by Local's actual-schedule counterexample; no shape or actual allocation theorem is claimed. The next active reasoning item follows the owner's temporal-instrument origin: fixed-cell versus moving-frame differences, with no shader changes or duplicate Local complexity job.


## G96. Fixed-cell change and moving-frame change are different observables (2026-10-06)

Follow the owner's temporal-instrument origin and Local's §8.70. For a binary history x_t(i), define Qx_t(i) = x_t(i+1), time shift Sx_t(i) = x_(t+1)(i), and, for fixed integer v,

    D_v = 1 + S*Q^v over GF(2),
    (D_v x)_t(i) = x_(t+1)(i+v) xor x_t(i).

D_0 is the fixed-cell XOR change. For x_t(i) = w(i-v*t), D_v x is zero everywhere, regardless of w; D_0 need not be zero. This is a generic exact-translation history, not a claimed Rule 30 solution. The dyadic identity is

    D_v^(2^k) = 1 + S^(2^k)*Q^(v*2^k),

by repeated squaring of the single linear operator S*Q^v in characteristic two. It compares cells along the same constant-speed worldline. No real-valued acceleration, physical unit, feature identity or noise model is asserted.

For an actual Rule 30 orbit with global map F, pull back to z_t(j) = x_t(j+v*t). Translation covariance gives

    z_(t+1) = Q^v*F(z_t),
    z_(t+1) xor z_t = Q^v*F(z_t) xor z_t.

Proof: at site j, x_(t+1)(j+v*(t+1)) equals F(x_t) at that site; replacing x_t(i) by z_t(i-v*t) gives F(z_t)(j+v). This is a change of coordinates, without treating the update rule as linear. At v = 0, §8.70 supplies F(x) xor x = R210(x).

**Unexpected derivative-dynamics guard.** Write u_t = F(x_t) xor x_t = R210(x_t). Its next value is R210(F(x_t)), not in general R210(u_t). For a single black cell at site 0, x_1 has black sites {-1,0,1}, so u_0 has {-1,1}. The next Rule 30 row has {-2,-1,2}, giving u_1 = {-2,0,1,2}. But applying Rule 210 to u_0 gives {-2,2}. The shortcut that the velocity field itself evolves by Rule 210 fails at sites 0 and 1. This clarifies the scope of the correct identity in §8.70; that section is not being accused of claiming the shortcut.

**Transport-versus-acceleration guard.** In the generic translating pulse x_t(i) = 1 exactly when i = t, the tracked position p_t = t has numerical velocity 1 and acceleration and jerk zero. At fixed site 0 the first three samples are 1,0,0: its second real finite difference is 1, and its second GF(2) difference is also 1. Along i = t every sample is 1, with zero differences. Thus fixed-cell second differences can reflect passage of a constant-speed pattern, not acceleration of that pattern. The example is a scope guard, not Rule 30 data or a PIV validation.

**MC1-MC2 preregistered NOT RUN.** MC1: every binary ring of widths 3 to 8, integer frames v = -1,0,1, compare literal Rule30 truth-table updates with both the transported update and moving-difference identities; separately require the v = 0 Rule210 identity. MC2: independently evolve the finite single-black-cell guard using padded direct truth tables, and verify the fixed/tracked pulse differences and dyadic worldline identity through lag 8. Counterfactual that u evolves by Rule210 must fail at the stated sites. No centre-column rerun, shader edit or Local complexity job. Existing-record search found §8.70's fixed-cell identity but no moving-frame audit or claimed autonomous derivative law. Elementary shift algebra and the recorded truth tables; no novelty or prize claim. The next question is which coherent structures and phase coordinates justify a tracked observable in actual Rule30 dynamics.

Probe: `tests/probes/rule30_gpt_moving_frame.py`. Independent Local reading requested.


**MC1-MC2 outcome (2026-10-06 19:16 BST).** Executed only after preregistration was published at e2c6a02. MC1 PASS: 504 ring rows and 1512 moving-frame cases. MC2 PASS: the padded derivative-dynamics guard and 168 dyadic worldline checks. The autonomous Rule210-change-field counterfactual fails at sites 0 and 1, as predicted; the tracked pulse has zero acceleration while its fixed-cell second difference is one. Finite controls support the implementation and examples, not an orbit-distribution or prize claim. Independent review remains pending.

### G97. The moving-frame flip prediction under a fair spatial ensemble (2026-10-06)

**Status:** proved below for iid fair initial rows; independent review and finite controls pending. Not a theorem about the single-black-cell orbit. Reply to Local L050 and G086. Existing record: C.5 and RULE30-PRIZE.md §8.68 already use invariance of the uniform spatial measure; Local supplies the right-step OR identity in §8.70. No novelty claim.

**Proposition.** Start Rule30 on an iid fair bi-infinite row. For any deterministic observer positions p_t with increments in {-1,0,1}, the expected number of XOR flips in N steps is N/2 + N_right/4, where N_right counts increments +1. No temporal independence is assumed.

**Spatial-law proof.** For any output block of k cells, its k+2 input cells are fair. Fix the two rightmost input bits. Given the output block, solve the other k input bits uniquely from right to left using y_i = x_(i-1) xor (x_i OR x_(i+1)). Every output block has exactly four preimages and hence probability 2^(-k). Every finite output block is therefore iid fair. Induction gives that spatial law at each time. This is a direct counting proof of the previously used invariance.

**Flip proof.** At observer site i, abbreviate a=x_(i-2), b=x_(i-1), c=x_i, d=x_(i+1), e=x_(i+2). The next sampled value XOR the current c is:

    right step: d OR e;
    stay: b xor (c OR d) xor c;
    left step: a xor (b AND NOT c).

The right expression has probability 3/4 under the fair spatial law. Each other expression includes a fair bit independent of the remaining expression, giving probability 1/2. Linearity of expectation then proves the claim, without any assertion that successive flips are independent. For p_t=floor(v*t), 0<=v<=1, N_right=floor(v*N), so the expected flip fraction is 1/2 + floor(v*N)/(4*N). For -1<=v<=0 it is exactly 1/2.

**Unexpected scope guard.** From the deterministic all-zero row every observed flip is zero, including every right step; from the all-one row the first right flip is one. Thus the exact right-step identity alone does not force a three-quarter probability. Nor does the ensemble expectation establish a variance, concentration, almost-sure time frequency or the distribution of the selected single-seed orbit. Those require separate arguments. In particular it does not validate an iid standard-error estimate for Local's temporal samples. The observer here is predetermined, not adaptively tracking features from the random row.

**SC1-SC2 preregistered NOT RUN.** SC1: enumerate all 2^(k+2) input words for k=1..8 using the literal Rule30 truth table; require exactly four preimages of each k-bit output word. SC2: enumerate all 32 five-bit neighbourhoods with literal updates at observer increments -1,0,+1; require 16,16,24 flips respectively, and independently require the three Boolean identities above. Retain the all-zero/all-one guards. These are tiny local controls, not a rerun of Local's 41 rays. Predictions must be published before execution.


**SC1-SC2 outcome (2026-10-06 19:20 BST).** Executed after predictions and instrument were published at a233f59. SC1 PASS: 2040 input words over widths 1..8, exactly four preimages per output word. SC2 PASS: all 32 five-bit neighbourhoods; left/stay/right flip counts 16,16,24. The constant-row scope guards pass. These local controls do not establish any single-seed frequency or temporal variance. Independent review remains pending.

**Corollary: temporal independence in the non-rightward fair-ensemble case.** If the observer is deterministic and p_(t+1)<=p_t for every t, its sampled values s_t=x_t(p_t) are iid fair, and its successive XOR flips are iid fair as well. In particular this applies to floor(v*t) for -1<=v<=0. It remains a statement about the random initial-row ensemble.

**Proof.** The t-step output x_t(p_t) is left-permutive in the leftmost initial input at L_t=p_t-t: it has form x_0(L_t) xor g_t of the other initial inputs. Induct on t in the Rule30 update: only the left child contains that leftmost input, and its coefficient remains one. Every earlier sampled value has a cone whose left endpoint L_s is strictly greater than L_t, because p_t<=p_s and t>s. Thus no earlier sample uses x_0(L_t). Conditional on all initial bits other than this fresh fair bit, the current sample is fair and the earlier samples are fixed. This proves independence from the entire earlier sample vector. Induction proves iid sampled values. Any N prescribed consecutive flip values have exactly two preimages among the 2^(N+1) equally likely sample vectors (choose s_0 and reconstruct); hence flip vectors are uniform and independent, with count variance N/4. No analogous independence is asserted for rightward frames.

**SC3 preregistered NOT RUN.** For all observer increment words over {-1,0} of lengths 1..4, enumerate every initial word on the union of their finite cones and evolve by a padded literal Rule30 truth table, using only cells with their complete cone present. Require each sampled word to have equal multiplicity and each flip word twice that multiplicity. Compare the exact flip-count first and second moments to N/2 and variance N/4. Unexpected guard: with increments +1 for one step, flip probability must instead be 3/4, refuting unrestricted fair-flip independence. No Local profile rerun. Publish this added prediction before execution.


**SC3 outcome (2026-10-06 19:27 BST).** Ran only after the added prediction and instrument were published at 5bb1aac. PASS: 30 left/stay observer paths, 9360 initial words, uniform sampled and flip vectors, and exact mean N/2 and variance N/4 on every path. The unexpected right-step guard gives 3/4 rather than 1/2, as predicted. These finite controls support G97's corollary; the proof uses the fresh initial left bit and does not transfer to the single-seed history. G98's DC1-DC2 remain NOT RUN.

### G98. Clock reparametrization, lattice diamonds and background-dependent fronts (2026-10-06)

**Status:** elementary scope proofs and counterexamples; independent review pending. Reply to Local L051 and CONSTELLATION rows 18/19. No physical time-dilation, Lorentz-invariance or prize claim. Prior-art check recorded in PRIOR-ART.md; no external theorem imported.

**Global-clock proposition.** For a synchronous deterministic map F with states x_n=F^n(x_0), choose any strictly increasing, unbounded tick-completion times T_n. Between completions hold the state at x_n. Every observable depending only on the ordered states is unchanged by the choice of T_n. Proof: neither the recurrence nor its ordered state sequence contains T_n. Durations can affect an observer given an additional physical clock or time-dependent inputs; they are invisible only to the stated state-sequence observables. This makes a precise version of the unequal-tick idea, without identifying elapsed time with computational complexity. A scalar cone simulation uses order n cells per row, but that implementation cost does not prove a lower bound for all ways of computing the nth centre bit.

**Continuum-diamond proposition.** Let a,b>0 be assumed constant left/right cone speeds. Between events (0,0) and (T,X), with -a*T<=X<=b*T, the continuum diamond has area

    A = (b*T-X)*(X+a*T)/(a+b).

Proof: put u=b*s-y and w=y+a*s. The diamond is the rectangle 0<=u<=b*T-X, 0<=w<=X+a*T. The absolute Jacobian of (s,y) to (u,w) is a+b. For a=b=1 this gives (T²-X²)/2. At fixed T the largest area occurs at X/T=(b-a)/2. Setting a=0.246, b=1 therefore gives 0.377, but only inside this assumed geometric model; it is not an established preferred frame of Rule30. A square root of normalized area is a constructed proxy, not a derived physical clock.

**Unexpected discrete-count guard.** On the ordinary integer event grid with speed-one edges, the inclusive diamond count is exactly

    sum over s=0..T of max(0, min(s,X+T-s)-max(-s,X-T+s)+1).

At T=2,X=0 the row counts are 1,3,1, total 5; continuum area is 2. Thus CONSTELLATION row18's exact number-of-events wording needs correction. Boundary conventions and event density must be specified before comparing counts with continuum volumes. For a fixed positive-speed cone, lattice counts have a boundary-order correction, not exact equality with area.

**Background guard.** Compare Rule30 started with a single black cell at zero against the all-zero orbit. The black support's leftmost site is -t at every t: the cell just left of the previous leftmost black has input100, hence becomes black; no cell farther left can turn black because input000 remains zero. Thus a disturbance propagates left at speed1 on this background. The measured approximately0.246 front speed on another background is not a universal causal bound. The symmetric radius-one dependency graph and a measured state-dependent damage front are different objects. Substituting the latter into a causal diamond requires a separate effective-cone model and validation.

**Unequal local-clock guard.** Individual in-place Rule30 updates need not commute. Start with one black cell at site1 and all others zero. Update site0 then site1: the final black set is {0}. Reverse those two updates: the final black set is {0,1}. Both orders update each selected site exactly once; the difference is not a change in global tick duration. This counterexample concerns raw in-place updates, not impossibility of asynchronous simulations with extra state or buffering.

**DC1-DC2 preregistered NOT RUN.** DC1: for integer T=0..12 and |X|<=T, count diamond grid points independently by path reachability and by the row-interval formula; retain T2,X0's five-versus-two guard. DC2: direct truth-table single-seed evolution through12 ticks must have leftmost support -t; two explicit local-update orders must give the sets above. These are bounded guards, not a new damage-speed measurement or asynchronous statistical job. Publish predictions before execution.


**DC1-DC2 outcome (2026-10-06 19:31 BST).** Ran after the predictions at5bb1aac and instrument publication through806cfec. DC1 PASS: 169 integer diamonds, with independent path reachability matching the row-interval formula. The five-versus-two count/area guard passes. DC2 PASS: seed left edge -t through12 and the two update orders giving {0} versus {0,1}. Local's L052 review independently checks larger finite ranges. These controls validate the recorded guards, not an effective physical metric.

### G99. Versioned dependency evaluation preserves logical time (2026-10-06)

**Status:** elementary finite-dependency proof; independent review and controls pending. Follow-up to G98, Local L052 and CONSTELLATION row19. The asynchronous-simulation prior art in PRIOR-ART.md uses additional state; this is a direct scheduling statement, not a new simulator or universality result.

**Proposition.** To compute x_N(0), keep immutable values indexed by (i,k) for 0<=k<=N and |i|<=N-k. Initially store x_0(i) for -N<=i<=N. A noninitial node (i,k) becomes ready only when its three parents (i-1,k-1), (i,k-1), (i+1,k-1) are stored. Evaluate it using the original local rule. Every schedule that eventually evaluates all these nodes and only evaluates ready nodes produces exactly the synchronous values, whatever the physical delays or order of independent ready nodes.

**Proof.** All parents of a node lie in the stated triangle. Generation0 is identical to the original data. By induction on k, every parent of a generation-k node has its synchronous value, so evaluating the deterministic rule produces x_k(i). This holds whenever that node is evaluated, independently of intervening work elsewhere. The finite graph is acyclic because each dependency lowers k; every complete topological order is therefore valid. Unbounded physical delays or lack of eventual completion are excluded explicitly.

There are (N+1)² stored nodes in this full cone, including initial nodes, and a longest chain of N update nodes. Those are costs/depths of this explicit one-step dependency graph, not lower bounds against every algorithm for the centre bit. Generation labels are logical time. The theorem supplies no physical time dilation, uniform physical signal speed, memory-optimal implementation or sublinear prize algorithm.

**Unexpected mixed-generation guard.** Start with a black cell at1. After computing only node(0,1), project the latest stored value at each site while retaining generation0 elsewhere. This projection has black set {0,1}, whereas the complete synchronous generation1 has {0,1,2}. Thus correct individual versioned nodes do not make an arbitrary mixed-generation projection a synchronous frame. An observable must specify its logical generation; buffering and labels are part of the assumptions, not optional bookkeeping. G98's raw in-place order guard separately shows what can go wrong if the parents are overwritten or read from the wrong generation.

**VP1 preregistered NOT RUN.** For N1..4 and every initial word on [-N,N], compare two complete ready-node schedules (increasing generation/site order and a ready-node schedule prioritizing the largest site) with a separately computed synchronous truth-table triangle. Require all stored node values and the centre output to agree. Retain the mixed-generation guard above; the unrestricted claim that every intermediate projection is a synchronous frame must fail. No asynchronous random-cell profile, Local job or speed benchmark. Publish the instrument and predictions before execution.


**VP1 outcome (2026-10-06 19:38 BST).** Executed after predictions and instrument publication through827e006. PASS: 680 initial words at N1..4, both ready-node schedules agree with every synchronous node. Mixed-generation guard passes: {0,1} differs from the complete frame {0,1,2}. These are bounded controls for the stated finite graph, not a new bounded-state simulator or speedup.

### G100. Fair spatial rows do not make rightward flips independent in time (2026-10-06)

**Status:** exact short-horizon ensemble calculation below; independent review and RF1 control pending. Follow-up to G97's open rightward temporal-law scope, not a new orbit-profile run. Existing-record search found no rightward flip triple or lag-two covariance calculation. No novelty, concentration, long-run variance or single-seed claim.

Start from an iid fair row and observe p_t=t. In moving coordinates z_t(j)=x_t(j+t), Rule30 becomes H(z)_j = z_j xor (z_(j+1) OR z_(j+2)). The flip B_t=z_t(1) OR z_t(2) depends on six initial fair bits for t0..2. Spatial fairness persists by G97, so each B_t has mean3/4.

**Exact dependence guard.** Write (d,e,f,g,h,j) for initial sites1..6. Conditional on B_0=0, d=e=0 and B_1=f OR g. For the four pairs (f,g), direct substitution in H twice gives the following B_2:

    (0,0): h OR j; (0,1): 1; (1,0): 0; (1,1): h OR j.

Hence P(B_0=0,B_1=1,B_2=1) = (1/4)*(1/4)*(1+0+3/4) = 7/64, whereas independent Bernoulli(3/4) flips would give9/64. Also P(B_0=0,B_1=0,B_2=1)=3/64. Therefore P(B_0=0,B_2=1)=5/32 and Cov(B_0,B_2)=1/32. Adjacent flips nevertheless have covariance zero: conditional on B_0=0, B_1=f OR g has probability3/4; the unconditional B_1 also has probability3/4. Stationarity under H supplies the same adjacent calculation for B_1,B_2. The variance of B_0+B_1+B_2 is consequently3*(3/16)+2*(1/32)=5/8, not the iid value9/16. This is an explicit example where an adjacent pair test misses temporal dependence.

The ray p_t=t is the right-edge speed, outside Local's measured interior speeds. This calculation does not establish the covariance at an interior speed, asymptotic count variance or a numerical correction to Local's single-seed standard errors. It does refute the general inference that spatial fairness plus the three-quarter mean implies independent rightward flips.

**RF1 preregistered NOT RUN.** Enumerate all64 six-bit words, compare H's three OR flips with independently computed literal Rule30 spacetime samples at p_t=t, and repeat with both choices of the initial origin bit (which cancels from the flips). Predict counts for000..111 of [1,3,5,7,3,9,7,29], marginals3/4, adjacent covariance0, lag-two covariance1/32 and count variance5/8. Counterfactual iid variance9/16 must fail. Publish predictions and instrument before execution; no long column, speed scan or colleague job.


**RF1 outcome (2026-10-06 19:38 BST).** Executed after predictions and instrument publication through827e006. PASS: all64 six-bit words with both origin bits, literal Rule30 spacetime and transported H formulations agree. Counts000..111 are [1,3,5,7,3,9,7,29]. Exact adjacent covariance0, lag-two covariance1/32 and count variance5/8 agree with the derived prediction; iid variance9/16 is refuted in this short-horizon speed-one ensemble. Independent colleague review remains pending. No interior-ray or selected-seed inference.

### G101. An interior speed-three-quarter observer retains temporal memory (2026-10-06)

**Status:** exact four-step fair-ensemble deduction from G97/G100; IF1 and independent review pending. Not a repeated long-ray measurement or selected-seed law.

Let p_t=floor(3*t/4). Its observer increments repeat (0,1,1,1). For any aligned block starting at t=4k, the spatial row at that time is iid fair by G97. Translate the starting site to0. The first flip B_0 (a stay step) equals a fair initial bit at site-1 XOR a function of sites0,1. The next three flips depend only on initial sites0..7: their update cones after cancelling the sampled value exclude site-1. Thus B_0 is independent of the entire subsequent triple. Those three steps are all right steps and, starting from the fair spatial row one tick later, have exactly the G100 triple law.

Consequently this four-step flip block has means (1/2,3/4,3/4,3/4), covariance1/32 between its second and fourth flips, and zero covariance for every other pair in the block. Its count mean is11/4 and variance1/4+5/8=7/8. Independent flips with those means would instead have variance1/4+3*(3/16)=13/16. Independence of the stay flip from the entire triple follows by conditioning on all initial bits except the unused fair site-1 bit. This is stronger than just zero pair covariance.

This law recurs at every aligned four-tick block under the random initial-row ensemble, by spatial-law invariance and translation. It supplies an interior-ray counterexample to temporal flip independence. It does not say distinct blocks are independent, compute a long-run variance coefficient, or prove the measured single-seed ray has this law. The speed3/4 occurs in Local's ray set, but the result is for the ensemble, not that measured orbit. Existing record: G97 supplies the invariant spatial measure and G100 the triple law; no novelty claim.

**IF1 preregistered NOT RUN.** Enumerate all512 initial words at sites-1..7, using literal Rule30 truth tables and observer sites0,0,1,2,3. Predict the four-bit flip histogram is4*[1,3,5,7,3,9,7,29] for each of the two first-flip values. Require all six covariances, count mean11/4 and variance7/8. Independent control: factor the predicted law into a fair first flip and G100's algebraic triple law. Unexpected counterfactual that the interior observer has independent flips with variance13/16 must fail. Publish predictions and instrument before execution. No Local computational run duplicated.


**IF1 outcome (2026-10-06 19:44 BST).** Ran after prediction and instrument publication through7773c41. PASS: all512 initial words at sites-1..7. Four-flip histogram0000..1111 is [4,12,20,28,12,36,28,116,4,12,20,28,12,36,28,116], matching the independently factored prediction. Mean11/4, variance7/8, second/fourth covariance1/32 and all other pair covariances zero agree. Independent review remains pending. No selected-seed, cross-block independence or asymptotic variance claim.

### G102. Isolated and chained race injection differ on a fair initial row (2026-10-06)

**Status:** first-row open-boundary recurrence proof; CI1 and independent review pending. Reply Local L054 and G092. Existing-record search found the isolated injection argument but no chain correction. The asynchronous prior-art pointers remain background, not a source of this probability. No novelty, later-row fairness, noisy-history survival or effective-cone theorem claim.

Model a forced race at site0 on an iid fair initial row. Neighbour flags are independent Bernoulli(eps). In right-to-left processing a flagged site reads its right neighbour's already-computed value, which may itself have raced. Truncate after D neighbour flags at sites1..D and compute site D+1 synchronously; all old inputs remain independent fair. The target's isolated case is D0. This is the local first-row mechanism of races.c, with an open terminal rather than its cyclic boundary.

**Right recurrence.** If the target's old bit is c and its right neighbour's old bit r, its error is (NOT c) AND (new_right XOR r). When c=0, new_right=r OR V, where V is either the next old bit or its updated value depending on that neighbour's race flag. Thus error requires c=r=0 and V=1. Conditional on a zero old bit to the left, let Q_D be the probability this effective right input is1. A nonrace gives a fair old bit. A race gives old_bit OR next_effective_input; conditional on old_bit0, the same zero-left condition recurs. Therefore

    Q_0=1/2; Q_D=(1-eps)/2 + eps*(1/2 + Q_(D-1)/2)
       =1/2 + (eps/2)*Q_(D-1); q_right,D=Q_D/4.

The limit for 0<=eps<=1 is q_right=1/[4*(2-eps)] =1/(8-4*eps). The exact remainder is q_right-q_right,D=(eps/2)^(D+1)/[4*(2-eps)]. The value at eps0 denotes the forced-target isolated limit, not conditioning on a zero-probability natural target event. For eps>0 it is the injection probability conditional on the target race in the stated model. It differs from1/8 for nonzero eps; relative correction is eps/(2-eps), small in the rare-race regime. This is a bulk limit, not an exact formula for every site of the finite cyclic implementation.

**Left contrast.** For a forced left race, target error is new_left XOR old_left. For any fixed finite flag pattern, expanding the consecutive left-race chain exposes a fresh far-left old bit with XOR coefficient1; all OR terms involve sites to its right. That bit is independent fair, so the conditional error probability is exactly1/2 at every finite depth, and in the limit for eps<1 where the chain terminates almost surely. No infinite unanchored left-to-right schedule at eps1 is asserted.

**Unexpected chaining guard.** Set old sites0..3 to0,0,0,1. With site1 synchronous, its new value is0 and a right race at0 injects no error. If site1 also races, site2's synchronous new value1 makes new_site1=1, so the race at0 injects an error. The isolated three-bit velocity formula does not cover this chain. This qualifies the exact isolated probability in L054; it does not refute the measured rare-race scaling or establish a survival law. Noisy later rows need their own joint-law analysis.

**CI1 preregistered NOT RUN.** For D0..5, enumerate every old word and every D-bit neighbour flag word in both directions; use literal Rule30 tables, a forced target race and a synchronous terminal. Apply exact flag weights at eps0,1/4,1/2,1. Predict the right recurrence and remainder, and left injection1/2; retain the explicit chain guard. Independent control is the conditioned algebra above versus full old-word/flag enumeration. No stochastic simulation, eps-scaling fit or colleague job. Publish predictions and instrument before execution.


**CI1 outcome (2026-10-06 19:50 BST).** Executed after predictions and instrument publication through84d09c9. PASS: 43680 old-word/flag combinations and48 exact rational weighted checks. Right finite-depth recurrence and remainder agree at all declared depths and eps; left conditional injection1/2 agrees. The explicit adjacent-race guard gives isolated injection0 and chained injection1. Independent colleague review remains pending. These controls cover the first-row open-terminal model, not the exact cyclic mean, later noisy rows or survival law.

### G103. A clean dependency cone gives a law-free disagreement bound (2026-10-06)

**Status:** coupling/union-bound proof; CP1 and independent review pending. Follow-up to Local L054 and G102. Existing-record search found the effective-cone fit but no clean-dependency-cone bound. This uses elementary deterministic dependencies and Bernoulli/union bounds, not a new concentration theorem.

Couple an ideal radius-one synchronous history and a raced history from the same arbitrary initial row. Assume every unflagged update reads its three parents from the raced history's previous logical row and applies the original rule; flagged updates may read already-computed neighbours as in races.c. For target(i,t), take all ancestor update nodes (j,s), 1<=s<=t, |j-i|<=t-s. There are t² distinct nodes on the line. On a W-cell ring, deduplication gives M=sum over s1..t of min(W,2*(t-s)+1)<=t².

**Clean-cone lemma.** If no ancestor node is flagged, target(i,t) equals the ideal value, regardless of flags outside the cone. Proof: induction from the common initial row through the cone's generations. Each cone update is unflagged and its three parents lie in the preceding cone layer. All those parents therefore agree, and applying the same deterministic rule preserves equality. New-value propagation outside the cone cannot enter via an unflagged node. Snapshot reads at unflagged nodes are an explicit assumption, not a claim about arbitrary in-place updating.

With independent Bernoulli(eps) flags, the clean event has probability(1-eps)^M. Consequently

    P(target differs)<=1-(1-eps)^M<=1-(1-eps)^(t²).

Without independence, if every flag has marginal probability at most eps, the union bound still gives P(target differs)<=min(1,eps*t²). Neither bound assumes fair states, injected-error independence, a measured speed0.246, damage irreversibility or a half-differing interior. Averaging cell indicators gives the same bound for the expected disagreement fraction D_t on a finite ring; spatial independence is unnecessary. Markov's bound also gives P(D_t>=delta)<=min(1,[1-(1-eps)^(t²)]/delta).

For 0<eps,delta<1, mean disagreement at least delta requires

    t>=sqrt(log(1-delta)/log(1-eps))

under independent flags, and t>=sqrt(delta/eps) under the marginal-only bound. Thus the necessary timescale is at least order eps^(-1/2) as eps tends to0, for any fixed mean threshold. This is a lower constraint on the onset of mean decoherence, not a matching upper estimate, exact survival law, realised hitting-time bound or exponent fit. It does not turn Local's measured coefficient0.623 into a theorem. Local's fractions concern finite realised runs.

**Unexpected final-tick guard.** On a five-cell ring started from a black cell at2, allow a right race only at site0 on step1, then no races on step2. Site1 on step2 differs from the ideal history despite its own final update being unflagged. Its ancestor at(step1,site0) was flagged. Checking just the final target is insufficient.

**CP1 preregistered NOT RUN.** For W3..5,T1..2, enumerate all initial rows and flag histories in both sequential race directions with races.c's boundary convention. Require agreement at every site with a clean cone. Use exact weights at eps0,1/4,1/2,1 and require every site disagreement probability to obey both bounds. Independently construct ancestor sets, and retain the final-tick guard. This is77440 short row/flag cases, no stochastic simulation or eps-scaling rerun. Publish predictions and instrument before execution.


**CP1 outcome (2026-10-06 19:56 BST).** Ran after prediction and instrument publication through43095bf. PASS: 77440 initial-row/flag histories and192 exact weighted site bounds. Every clean-cone site agrees, both independent-flag and marginal-only bounds hold, and the final-unflagged/earlier-ancestor guard differs as predicted. These finite controls support the coupling proof; they provide no matching rate, effective cone or realised hitting-time claim. Independent colleague review remains pending.

### G104. Right-reading races preserve fair spatial law; left-reading races change pairs (2026-10-06)

**Status:** bulk spatial-law proof; OM1-OM2 pass, independently reviewed by Local L059. Follow-up G102/G103 and Local L054. Prior-art abstract checks are recorded in PRIOR-ART.md; no imported theorem or novelty claim. This is the sequential snapshot/raced-neighbour model, not a general asynchronous cellular automaton.

On the infinite line, take old row x iid fair and a fixed flag pattern r independent of x. For right-reading updates, assume every rightward consecutive flag run terminates, so the recursion

    y_i=x_(i-1) xor (x_i OR [y_(i+1) if r_i=1 else x_(i+1)])

is well-defined by a finite recursion at every site. This condition holds almost surely for independent Bernoulli(eps) flags with eps<1.

**Right-law proposition.** Conditional on any such fixed flag pattern, y is iid fair. Proof: for output block[a,b], fix all old bits at sites>=b. This fixes y_(b+1), whose recursion uses only those tail bits. Given any prescribed y_a..y_b, solve right-to-left:

    x_(i-1)=y_i xor (x_i OR [y_(i+1) if r_i=1 else x_(i+1)]).

There is exactly one preimage among the b-a+1 old bits at[a-1,b-1]. They were independent fair even conditional on the tail, so every output block has probability2^(-(b-a+1)). This proves the product law for every finite block. Adaptive flags depending on x are excluded. Independent new flag fields at each logical step therefore preserve the fair spatial law at every step, although the temporal history need not match the ideal orbit.

**Earned extension of G102.** In this infinite right-reading model, the current noisy row remains iid fair and is independent of the next fresh flags. Thus G102's bulk conditional injection rate1/(8-4eps) applies at each step relative to F(current noisy row), for eps>0. It is not the disagreement rate relative to the original ideal history, and does not supply a survival law. This is no exact finite-ring invariant-measure claim.

**Left contrast and unexpected density guard.** For left-reading updates, assume each leftward flag chain terminates, and use

    y_i=[y_(i-1) if r_i=1 else x_(i-1)] xor (x_i OR x_(i+1)).

Expanding the chain ending at i exposes a fresh far-left old bit with XOR coefficient1, independent of all old bits at sites>=i. Therefore y_i is fair and independent of those higher old bits, conditional on the fixed flags. If r_(i+1)=0, y_(i+1) depends on x_i,x_(i+1),x_(i+2), so P(y_i differs from y_(i+1))=1/2. If r_(i+1)=1, their XOR is x_(i+1) OR x_(i+2), so that probability is3/4. Independent Bernoulli flags with0<=eps<1 give first-row adjacent disagreement1/2+eps/4 despite both densities remaining1/2. Thus the left map does not preserve the iid fair row law for eps>0.

This separates unchanged density from unchanged pair law. The left formula is for a fair input row and is not asserted at later noisy steps. Local's finite-ring later-time descriptive statistics are not being relabelled refuted; the theorem is about explicit infinite-bulk law and first-step scope. No selected-seed conclusion follows.

**OM1-OM2 preregistered NOT RUN.** OM1: widths1..4, every right flag pattern, every fixed three-bit synchronous terminal tail and every old block; require a bijection to output blocks and recovery by the independent XOR inverse. OM2: anchored left depths0..3, all old rows and flag patterns; require density1/2, pair disagreement1/2 or3/4 according to the right cell's flag. Exact weights at eps0,1/4,1/2,1 must give pair law1/2+eps/4. Counterfactual that unchanged density forces fair pairs must fail. No noisy long-run measurement or Local job. Publish predictions and instruments before execution.


**OM1-OM2 outcome (2026-10-06 20:07 BST).** Executed after predictions and instrument publication through8753ab0. OM1 PASS: 2720 right input cases, every fixed-tail/flag block map bijective and independently inverted. OM2 PASS: 10880 left input cases and48 exact rational weighted moments. Both densities are1/2, but left adjacent disagreement is1/2+eps/4 as predicted. The eps1 checks are finite anchored endpoint controls; the infinite terminating-chain theorem excludes eps1. These controls support the spatial-law proof, not ideal/noisy history survival or exact cyclic invariance. Independent colleague review remains pending.


### G105. Cyclic closure changes zero-row mass in the actual race model (2026-10-06)

**Status:** finite-ring preimage proof; ZR1 passes, independently reviewed by Local L060. Follow-up G104 and Local L054. This is a scope audit of the finite cyclic snapshot/sequential model in races.c, not a new damage-speed or prize theorem. Existing-record checks found fair infinite-row invariance and healing in structured backgrounds; these do not establish finite cyclic uniform invariance.

Take W>=3 cells with indices modulo W, old row x uniformly distributed over all 2^W words, and a fixed state-independent flag word. Sequential right-reading updates process W-1 down to0; an effective race at i<W-1 uses already-computed y_(i+1), otherwise old x_(i+1). Left-reading updates process0 up toW-1; an effective race at i>0 uses y_(i-1), otherwise old x_(i-1). The first processed cell always uses the old cyclic neighbour, so its flag is ineffective.

**Right zero-row preimages.** If the entire new row is zero, every update requires

    x_(i-1)=x_i OR [0 if the right race is effective else x_(i+1)].

If any x_i=1, this equation forces x_(i-1)=1, then repeats around the ring to force all old cells1. Conversely both the all-zero and all-one old rows produce the all-zero new row for every right flag pattern: induction in the scan order, using centre1 to keep the OR1 in the all-one case. These are the only two preimages. Thus conditional on any flags,

    P(new row is all zero)=2^(1-W).

The uniform ring law assigns that row probability2^(-W), so it is not invariant under any fixed right flag pattern or any state-independent mixture of them. G104's infinite-line fair product theorem is intact; closing the inverse around a cycle removes its independent tail. This mass discrepancy is exponentially small as W grows and does not refute Local's large-ring approximate statistics.

**Left zero-row preimages.** Any old1 at an effectively raced site would give new1 because its new left input is0. Therefore an old1 must sit at a nonraced site, where a zero output forces its old left neighbour1. Repeating this implication around the ring either encounters an effective race (a contradiction) or forces the whole old row1 with no effective flags. The all-zero old row always maps to zero. The all-one row does so exactly when no effective left flags are present. Consequently the zero row has one preimage when any effective left flag is present, and two otherwise. With independent Bernoulli(eps) flags,

    P(new row is all zero)=[1+(1-eps)^(W-1)]*2^(-W).

For0<=eps<1 this too differs from the uniform ring law. At eps1 the zero-row mass alone does not decide invariance; no claim is made from this one cylinder.

**No universal decoherence upper bound.** From the common all-zero initial row, ideal and raced histories remain identically zero for all logical times, every flag sequence and either scan direction. Thus no positive mean threshold can have a finite state-uniform onset bound, even with independent positive-rate flags. A matching upper side to G103 needs initial-state or activity assumptions. Fair marginal rows by themselves also cannot specify a coupling: equal copies have disagreement0, while independent fair copies have disagreement1/2, and synchronous Rule30 preserves both constructions' marginals. Those example couplings are not the common-initial-state race process; they only refute inference from marginals alone.

**Unexpected boundary/healing guard.** On a ring, distinct all-zero and all-one rows merge to the same all-zero row in one synchronous tick. Left permutivity therefore supplies no blanket finite-ring noncoalescence theorem. Infinite-line rightmost-damage propagation requires a rightmost discrepancy; these two infinite constant rows would have none. Local's background-dependent healing is preserved, not contradicted.

**ZR1 preregistered NOT RUN.** For W3..7, enumerate every old row and every flag word in both scan directions using the literal Rule30 truth table. Count zero-output preimages for every flag word: right always2; left1 or2 according to whether any effective flag is present. Independently apply exact Bernoulli weights at eps0,1/4,1/2,1 and compare the two formulas. Predict43648 row/flag/direction cases and40 weighted probability checks. Retain zero-row closure and the synchronous two-preimage healing guard. Counterfactual that G104 gives exact finite-ring uniform invariance must fail. This is a short exact enumeration, no long-run or Local scaling job. Publish before execution.


**ZR1 outcome (2026-10-06 20:13 BST).** Ran after proof, predictions and instrument publication throughf0f3a1b. PASS:43648 row/flag/direction cases and40 exact rational weighted probabilities. Right zero-row preimages are exactly zero and one for every flag pattern; left has only zero whenever any effective flag is present. Absorbing-zero and synchronous cyclic-coalescence guards pass. This confirms the finite preimage formulas; it supplies no long-run invariant measure, matching decoherence rate or selected-seed result. Independent review remains pending.


### G106. Spatial fairness survives right races, but moving-frame temporal activity changes (2026-10-06)

**Status:** infinite-bulk one-step flip-law proof; TF1 passes, independently reviewed by Local L061. Follow-up G97/G102/G104. Existing record separates spatial invariance from temporal independence; this derives a changed temporal mean in the specific right-reading race model. No general probabilistic-CA theorem, novelty or selected-seed claim is imported.

Use G104's infinite right-reading recursion with fair iid old row x and fresh independent Bernoulli(eps) flags,0<=eps<1. Let y be the next noisy row. For an observer moving by delta in{-1,0,1}, its flip is x_i XOR y_(i+delta). All flag chains terminate almost surely. The fresh flag field is independent of the current old row at each step.

**Nonrightward mean.** For delta0, y_i has form x_(i-1) XOR A, where A involves only old bits at sites>=i, even through raced-neighbour recursion. The bit x_(i-1) is fresh fair and independent of x_i and A, so the flip is fair. For delta-1, y_(i-1) similarly exposes fresh old x_(i-2). Thus both flip probabilities are1/2, conditional on any terminating fixed flag pattern. This is a marginal statement, not temporal independence of successive flips.

**Rightward mean.** Write

    A_j=x_j OR [y_(j+1) if r_j=1 else x_(j+1)].

The rightward observer's flip is x_i XOR y_(i+1)=A_(i+1). If r_j=0, A_j is the OR of two fair bits, hence has mean3/4. If r_j=1, y_(j+1)=x_j XOR A_(j+1), so

    A_j=x_j OR (x_j XOR A_(j+1))=x_j OR A_(j+1).

Here x_j is independent fair relative to A_(j+1), which depends only on higher old sites and flags. Let U be the translation-invariant mean of A_j. Conditioning on r_j gives

    U=(1-eps)*3/4+eps*(1/2+U/2)=(3-eps)/(4-2eps).

Hence U=3/4+eps/(8-4eps). The additive change is the total right-race injection rate from G102; this equality concerns a one-step temporal observable, not ideal/noisy disagreement accumulated over time. G104 preserves the fair spatial row law and independence from each next fresh flag field, so these flip means hold at every logical step in this ensemble.

**Predetermined moving path.** For N observer increments in{-1,0,1}, with N_right rightward increments, linearity of expectation gives mean flip count

    N/2+N_right/(4-2eps).

This extends G97's synchronous mean. It supplies no independence, covariance, variance, concentration or claim about an adaptively chosen observer. The infinite model excludes eps1; the finite anchored limit as eps tends to1 is a separate endpoint control.

**Finite anchored prediction.** With D potentially raced sites before a synchronous right terminal, define U_0=3/4 and U_D=3/4-eps/4+(eps/2)*U_(D-1). Then

    U-U_D=[eps/(8-4eps)]*(eps/2)^D.

For finite D these are polynomial probabilities also defined at eps1. At eps1, U_D=1-2^(-D-2); this does not define a nonterminating infinite update.

**Unexpected temporal guard.** With eps1/2, the infinite rightward flip mean is5/6, not3/4, although every noisy spatial row remains iid fair. Equal spatial measures need not give equal transition measures. This directly addresses the owner's temporal-field motivation without claiming physical acceleration or a prize result.

**TF1 preregistered NOT RUN.** D0..4, enumerate all old words on sites-2..D+2 and every flag pattern on sites-1..D, with siteD+1 a synchronous terminal. Use the literal Rule30 truth table to compute the next block, then count observer flips for delta-1,0,1. Exact flag weights at eps0,1/4,1/2,1 must give1/2,1/2,U_D. Independent control is the conditioned OR recurrence, including its exact remainder, against full word/flag enumeration. Predict43648 cases and60 weighted flip checks; this count happens to match ZR1 but the objects differ. Counterfactual that unchanged spatial law forces unchanged rightward flip mean must fail. Publish predictions and instrument before execution; no long-ray or colleague race-statistics rerun.


**TF1 outcome (2026-10-06 20:18 BST).** Executed after proof, predictions and instrument publication throughd05bb6b. PASS:43648 old-word/flag cases and60 exact rational weighted flip means. Left/stay means1/2 hold for every finite flag pattern; right U_D and its bulk remainder agree at every declared depth and eps. Finite eps1 checks remain anchored endpoint controls. The infinite eps1/2 rightward mean5/6 follows the proved recurrence, not a long-run empirical fit. No temporal independence, variance or ideal/noisy survival result follows. Independent review remains pending.


### G107. Nonrightward traces stay iid fair conditional on a state-independent right-race schedule (2026-10-06)

**Status:** conditional trace-law proof; NT1 passes, independently reviewed by Local L062. Extends G97's synchronous fresh-bit proof to G104's right-reading recursion, following G106 and Local L061. This is a model-specific extension of known left permutivity, not a prize solution or novelty claim. Existing record G97 supplies the synchronous argument; G104 supplies the terminating recursion.

Start on the infinite line from an iid fair row. Allow any fixed right-reading flag field whose rightward runs terminate at every site and logical step. It need not be spatially or temporally independent. For random flags, require the entire flag field to be independent of the initial row, and termination almost surely. Fresh Bernoulli flags with eps<1 satisfy this. Adaptive flags selected from states are excluded.

**Triangular composition lemma.** Conditional on the whole flag field, each time-t value at site i has form

    x_t(i)=x_0(i-t) XOR g_(t,i)(initial bits strictly to the right of i-t).

Its dependency uses only finitely many initial bits at each finite t. Proof by induction: one right-reading update is x_(t-1)(i-1) XOR A, and the OR/recursive term A uses only previous-row sites>=i. Each recursion terminates, so it has finitely many such inputs. Their initial left endpoints are at least i-(t-1)=i-t+1; only the left input exposes initial bit i-t, with XOR coefficient1. Finite composition of finite recursion trees remains finite. Thus the fresh leftmost initial bit never enters the other term, even though the right dependency may be arbitrarily long.

**Conditional trace law.** Fix a predetermined path p_0,p_1,... with p_t nonincreasing. Define L_t=p_t-t, which strictly decreases. Earlier samples depend only on initial sites>=L_s>L_t. Given all other initial bits and the flag field, the current sample contains the untouched fair bit at L_t, whereas all earlier samples are fixed. It is therefore fair independent of the earlier sample vector. Induction gives iid fair sampled bits conditional on the full flag field. Their distribution does not depend on that field, so the trace is also independent of the flag field as a random object (equality of every finite cylinder law).

Each N-vector of consecutive XOR flips has exactly two sample-vector preimages, so flips are iid fair, mean count N/2 and variance N/4. This now earns the nonrightward temporal-independence result deliberately left open by G106. No state-law induction or independence between successive flag rows is needed: conditioning first handles all their correlations.

**Scope and unexpected coupling guard.** Under these assumptions a single predetermined nonrightward trace has exactly the same statistical law as the synchronous fair-ensemble trace. This does not say the noisy and ideal traces coincide, nor that their two copies are independent: at eps0 they are the same random trace. Their joint history remains a separate question. No selected-seed, finite-ring, adaptive-observer or multisite-transition claim follows. Rightward observers are excluded; G106's rightward mean differs from1/2 even at eps0. Thus this theorem cannot justify calling every temporal observable insensitive to races.

**NT1 preregistered NOT RUN.** T1..3; every path with increments-1 or0; every T-bit schedule switching entire update rows between synchronous and right-reading races, except a fixed synchronous right terminal. Enumerate every initial word on sites-2T..T+1 and evaluate by literal Rule30 tables with shrinking finite boundaries. For each path/schedule, group inputs by all bits except the fresh pivots L_0..L_T: every conditional group must map bijectively onto sampled words. Independently check uniform flip words and mean/variance T/2,T/4. Predict135296 word/path/schedule cases and8736 conditional bijection classes. The schedule family includes fully correlated successive flags, not just fresh Bernoulli rows. Retain the eps0 identical-copy guard using the same inputs. This finite control supports the conditional proof; no simulation fit or colleague job. Publish before execution.


**NT1 outcome (2026-10-06 20:23 BST).** Executed after conditional proof, predictions and instrument publication throughe779bd0. PASS:135296 word/path/schedule cases and8736 conditional pivot-bijection classes. Sample and flip vectors are uniform in every declared path/schedule, with flip-count mean T/2 and variance T/4. The zero-flag history agrees with an independent synchronous XOR/OR formulation, confirming the identical-copy guard. These finite anchored controls support the infinite conditional fresh-bit proof; they establish no selected-seed, finite-ring or joint ideal/noisy independence claim. Independent review remains pending.


### G108. Shared initial bits give a causal invertible coupling of ideal and noisy traces (2026-10-06)

**Status:** conditional finite-horizon coupling proof; CT1 passes, independently reviewed by Local L063. Follow-up G97/G102/G107. Existing-record search found the fresh-bit marginal trace law but no paired causal-mask representation. This uses elementary triangular bijections and entropy counting, not a new general coding theorem or prize solution.

Fix a horizon N, a predetermined nonrightward path, and a terminating right-reading race field independent of the fair initial row as in G107. Couple the ideal synchronous and noisy histories from that same row. Write I_t and J_t for their sampled bits, t0..N. Their distinct fresh initial pivots are L_t=p_t-t. Let R contain all initial bits outside these N+1 pivots, and fix R and the entire flag field. The remaining pivot bits xi_t=x_0(L_t) are independent fair.

**Triangular pair representation.** G97 and G107 give

    I_t=xi_t XOR a_t(xi_0,...,xi_(t-1);R),
    J_t=xi_t XOR b_t(xi_0,...,xi_(t-1);R,flags).

Neither expression uses later pivots, which lie strictly to the left of its dependency boundary. Both expose the same current pivot with coefficient1. Inverting the first expression recursively recovers xi_<t from I_<t and R. Cancelling xi_t therefore yields

    J_t=I_t XOR e_t(I_0,...,I_(t-1);R,flags),   e_0=0.

This is causal: the time-t mask needs no current or future ideal sample. The map from I_0..I_N to J_0..J_N is itself a triangular bijection, recoverable successively from either trace when R and flags are known. Each trace separately is uniform conditional on this environment, yet their conditional joint law has only2^(N+1) equally likely pairs, rather than2^(2N+2).

In bits, conditional entropy of each trace and of their pair isN+1; conditional mutual information between the traces isN+1. These are statements conditional on R and flags. They do not make the unconditional coupling invertible, give its unconditional mutual information, or let an observer recover a hidden schedule from one trace. G107's independence of the single trace from the flag field is compatible with this conditional relation.

**Predictable-mask qualification.** Conditional on R and flags, e_t is determined by the past ideal samples. The current ideal sample is fresh fair independent of that past, so it is independent of the current mask under that conditioning. The masks need not be independent over time or independent of past samples. Their law remains the missing joint-history object, not something spatial invariance determines.

**First-tick state dependence.** For a stationary target i, let E_1=I_1 XOR J_1. On the common fair initial row, a right race can change its OR term only if x_0(i)=0. If x_0(i)=1, both OR values are1 and E_1=0. With fresh iid Bernoulli flags of rate0<=eps<1, G102's total injection probability gives

    P(E_1=1 | I_0=1)=0,
    P(E_1=1 | I_0=0)=eps/(4-2eps),
    Cov(E_1,I_0)=-eps/(16-8eps).

The latter follows because I_0 is fair, E_1*I_0 is always0, and E[E_1]=eps/(8-4eps). Thus even the first error is not state-blind or independent of the past observed bit for eps>0. This does not contradict iid marginal samples; it concerns the pairing of the two copies.

**Unexpected causal-mask guard.** Fix old sites1,2 to0,1, let only target0 read its updated right neighbour, and update site1 synchronously. Vary the two fresh pivots old0 and old-1 fairly. Then I_1=old-1 XOR I_0 while J_1=old-1 XOR1, so E_1=1-I_0. Each two-sample trace is uniform, but its partner is a deterministic bijective scramble given this environment. A state-independent fair error bit would be the wrong coupling. No selected-seed, finite cyclic survival or matching upper decoherence rate follows.

**CT1 preregistered NOT RUN.** Reuse NT1's literal right-reading history evaluator and an independent synchronous XOR/OR evaluator. For T1..3, all left/stay paths, all global-row switch schedules and all initial words on-2T..T+1, group by nonpivot initial bits. Require both trace projections bijective within each group, paired support size2^(T+1), and each time-t XOR mask constant for a fixed ideal prefix of length t. Predict135296 paired cases and8736 conditional classes. Independently check the four-pivot-input causal-mask guard above. This is a paired-law audit, not a repeat of NT1's marginal statistic; the existing first-tick weighted G102 control supplies the rate formula. Publish before execution.


**CT1 outcome (2026-10-06 20:29 BST).** Ran after paired proof, predictions and instrument publication through85f0972. PASS:135296 paired cases and8736 conditional triangular-coupling classes. Both projections are bijective, every time-t mask is determined by the ideal prefix of length t, and the four-input guard gives E_1=1-I_0. These controls support the conditional causal representation and its support/entropy count, not an unconditional independence, information value or survival rate. Independent review remains pending.


### G109. An isolated right-race source error heals once and returns one tick later (2026-10-06)

**Status:** local damage-echo proof; EH1-EH2 pass, independently reviewed by Local L064. Follows G102/G108 and Local L063. Existing record discusses background-dependent healing and state-dependent injection but not this source-site echo. This is a local Boolean mechanism, not a new global damage law, Markov closure or prize solution.

**Single-flip kernel.** Take any line background z and a second row differing only by a flipped bit at site0. Let delta_s(i) be their XOR disagreement after s synchronous Rule30 steps. At s0 the error is only at0. At s1,

    delta_1(-1)=1-z(-1), delta_1(0)=1-z(1), delta_1(1)=1.

These follow respectively from sensitivity of the OR's right input, sensitivity of its centre input, and the permutive left input. Let b=F(z). For the second synchronous step, delta_2(0)=z(1) OR z(2).

To prove this last identity, split on z(1). If z(1)=1, delta_1(0)=0 and b(0)=1-z(-1). Hence delta_2(0)=(1-z(-1)) XOR (1-b(0))=1. If z(1)=0, both centre and right inputs are flipped at s1. Toggling both OR inputs changes its value by1 XOR b(0) XOR b(1). Here b(0)=z(-1) XOR z(0) and b(1)=z(0) XOR z(2). Adding the left disagreement1-z(-1) cancels the z(-1) terms and leaves z(2). Both cases give the OR formula. This is an arbitrary-background identity, requiring no state probabilities.

**Isolated right-race injection.** Start ideal and raced copies from the same arbitrary old row x. On logical tick1, only site0 has an effective right-reading race; site1 is synchronous and already computed. All other sites read the old snapshot. Then the only possible first-row discrepancy is at0, and

    E_1=(1-x(0))*(1-x(1))*x(2).

Indeed an old black target masks the changed right value; with x(0)=0 the updated right neighbour is x(1) OR x(2), so disagreement requires old pattern001 at sites0..2. If no injection occurs, the two rows agree and continue to agree while subsequent ticks are synchronous.

If an injection occurs, the ideal first row z=F(x) has z(1)=1. Apply the single-flip kernel to these first rows. At the original source, disagreement over ticks1,2,3 is exactly

    1, 0, 1.

The second tick heals the source because the ideal right neighbour is black, while the error propagates to site1. The third-tick return follows from delta_2(0)=z(1) OR z(2)=1. There is no new injection in this experiment. Local source healing therefore does not imply the histories have coalesced or that the source will remain healed.

**Fair-input finite law.** On an iid fair initial row the injection probability is1/8 (G102's isolated event). Conditional on injection, second-tick disagreement is always present at site1, absent at0, and present at-1 precisely when x(-2)=x(-1). Thus the second-tick damage set is{1} or{-1,1}, each with probability1/2, and its mean size is3/2. These are conditioned short-time laws; they do not describe dense repeated races, chained injections, finite-ring wraparound or a global survival rate.

**Unexpected echo guard.** The event E_1=1,E_2=0,E_3=1 is forced for every injected isolated right race. It refutes the counterfactual that “healed at a source” means “permanently healed,” and explains why state-blind permanent-defect accumulation is not an exact coupling. It does not refute Local's finite empirical survival fit.

**EH1-EH2 preregistered NOT RUN.** EH1: enumerate all32 backgrounds on-2..2, flip site0 and run two synchronous ticks with shrinking boundaries; require source signature1,1-z(1),z(1) OR z(2). EH2: enumerate all128 old words on-3..3, apply one isolated target right race on tick1, then two synchronous ticks. Predict16 injections, all source signatures101; the other112 give000. Second-tick damage sets{1} and{-1,1} must occur8 times each. Independently verify synchronous propagation with the XOR difference-of-OR equation, rather than the truth-table implementation. These160 exact cases replace no Local long-run job. Publish predictions and instrument before execution.


**EH1-EH2 outcome (2026-10-06 20:34 BST).** Ran after proof, predictions and instrument publication throughf9aa008. EH1 PASS:32 arbitrary backgrounds and the source kernel1,1-z(1),z(1) OR z(2). EH2 PASS:128 initial words; exactly16 injections, all source signatures101, while112 noninjections give000. Second-tick masks{1} and{-1,1} occur8 times each. The independent XOR difference-of-OR propagation agrees throughout. This verifies the local echo, not repeated-race memory closure or a survival rate. Independent review remains pending.


### G110. The isolated-pulse paired trace is not first-order Markov despite iid marginals (2026-10-06)

**Status:** exact projected-memory counterexample; PM1 passes, independently reviewed by Local L065. Follow-up G108/G109 and Local L063's transition-table offer. Existing record provides causal masks and the source echo; this audits a concrete compressed state. It is not a general non-Markov theorem for repeated iid races or a new theory of hidden-state processes.

Use an infinite iid fair initial row. On tick1 only target0 reads its updated right neighbour; all other updates and all later ticks are synchronous. Let I_t,J_t be the ideal/noisy source samples and E_t=I_t XOR J_t. Consider the candidate observable state K_t=(I_t,E_t), equivalently the pair(I_t,J_t). The external pulse schedule is fixed and known.

G109 proves E_2=0 and E_3=E_1 for every initial row, with E_1 the indicator that old sites0..2 are001. Thus E_1 has probability1/8. By synchronous left permutivity, I_2 has form old(-2) XOR a function of old sites-1..2. That fresh old bit is fair independent of the injection event. Hence for b0 or1,

    P(E_1=1 | K_2=(b,0))=1/8,
    P(E_3=1 | K_2=(b,0))=1/8.

But conditioning further on the observed past error gives

    P(E_3=1 | K_2=(b,0),E_1=1)=1,
    P(E_3=1 | K_2=(b,0),E_1=0)=0.

Both earlier-error strata have positive probability in each current-state bin. E_1 is a function of past state K_1, so the next state's error component retains past information absent from K_2. This violates the first-order Markov property at tick2, even allowing a time-dependent transition kernel and the known pulse phase. Merely adding the current ideal sample to the current error does not close this projection.

**Unexpected marginal guard.** Both I_0..I_3 and J_0..J_3 separately are iid fair by G97/G107; the fixed isolated flag field is terminating and independent of the initial row. Each separate trace is therefore Markov, while their paired observable is not. This is an explicit distinction between marginal randomness and coupling memory, not a failure of the previous trace theorem.

A lagged error distinguishes the two groups in this three-tick example, but this proves no general finite-order closure. Repeated fresh Bernoulli races, finite rings and the selected seed are different models and remain to be checked. The full paired configuration remains a sufficient state for synchronous future evolution; this result is about a compressed single-site projection.

**Diagnostic for Local.** A useful measurement state is K_t=(I_t,E_t). Compare the empirical next-error fraction conditional on K_t with the same bins further split by E_(t-1); report counts for every bin. The pulse control must reproduce the exact split above. For repeated iid races, declare scope, flag rule, boundary, sample/replicate counts and predictions before running; a retained split is evidence against the proposed state, while a held finite table is not a Markov proof. GPT remains in the proof/counterexample lane and will not duplicate Local's measurements. No production-law split magnitude is predicted here.

**PM1 preregistered NOT RUN.** Enumerate all128 old words on-3..3; apply the isolated pulse and evolve to tick3 with literal Rule30 tables. Independently compute E_1 from the001 indicator and I_2's fresh-bit complement pairing. Predict current-bin counts8 for previous-error1 and56 for previous-error0, for each ideal bit b; next error equals previous error. Each marginal four-sample histogram must contain16 words8 times each. Counterfactual first-order Markov equality must fail in both bins despite uniform marginal traces. No long-run or colleague job. Publish before execution.


**PM1 outcome (2026-10-06 20:41 BST).** Executed after proof, predictions and instrument publication throughf922142. PASS:128 initial words. In each current ideal-bit bin, previous-error1/next-error1 count is8 and previous-error0/next-error0 count56; both opposite transitions have count0. Both marginal four-sample histograms contain16 words8 times each. The independent001 indicator and fresh-bit complement pairing agree. First-order Markov equality for the paired state is refuted in both bins of this isolated-pulse ensemble, not asserted refuted for repeated iid races. Independent review remains pending.


### G111. A nonzero finite-rate memory split extends to generic rates, but a zero at one rate does not (2026-10-06)

**Status:** finite Bernoulli-polynomial certificate proof; PC1-PC3 pass; independently reviewed by Local L067. Complements Local's requested W5,T3 memory table without enumerating that job. Existing record has exact rational weighting and pulse memory; this derives a parameter-scope certificate. It uses elementary polynomial counting, not a general closure theorem or prize solution.

Let A be a positive-count current-state bin at tick2, B a refined past/current bin contained in A, and S the next-error event E3=1. With a fixed finite initial distribution independent of the flags, use m independent Bernoulli(eps) flags before the current tick and n independent flags for its next step. All probabilities below are finite sums of eps^k*(1-eps)^(M-k) terms with nonnegative fixed weights. Past-only probabilities P(A),P(B) have degree at most m; success probabilities P(S and A),P(S and B) have degree at most m+n.

Define the conditional-split determinant

    D(eps)=P(S and B)*P(A)-P(S and A)*P(B).

When both bins are positive, D differs from0 exactly when P(S|B) differs from P(S|A). Its degree is at most2m+n. Any bin with positive count at an interior rate has positive probability at every eps in(0,1), because each compatible finite flag history has positive weight there. Hence a nonzero D at one interior rate proves D is not the zero polynomial and the split holds at every interior rate except finitely many roots.

**Application conditional on Local finding a split.** W5,T3 has m8 effective flags before tick2 and n4 on tick3, so degree is at most20. At eps0 both copies are identical, making the success event impossible and D(0)=0. If an exact eps1/2 table finds a nonzero witness, that same witness can fail at no more than19 interior rates. In particular it holds for all sufficiently small positive eps, since a nonzero polynomial has only finitely many roots. This gives no numerical rare-rate threshold or magnitude without coefficients, no infinite-ring conclusion and no long-time survival law. This generic implication was prepared before receiving Local's table; the support application below uses its subsequently published certificate.

At eps1/2 every one of the131072 paired histories has equal weight, so the integer witness is

    n_(S,B)*n_A-n_(S,A)*n_B,

and its nonzero status is exactly D(1/2)'s nonzero status. To reconstruct D, retain each event count by total number of active flags k: h_k. The scaled probability polynomial is sum h_k*eps^k*(1-eps)^(12-k); divide by32 for the uniform initial-row probabilities. Polynomial expansion and multiplication use integer coefficients; the determinant's common positive scale does not affect its roots. Past degrees reduce to8 when the future flags are summed out.

**Unexpected held-rate guard.** For two independent flag bits X,Y, take A always, B={X=1}, S={X XOR Y=1}. Then

    D(eps)=eps*(1-eps)*(1-2eps).

Conditional-rate equality holds at eps1/2 while failing at eps1/4, where D=3/32. Thus a held table at one noise rate cannot certify even a single witness polynomial identically zero. Nor does an identically zero determinant for one refinement prove full Markov closure.

**PC1-PC3 preregistered NOT RUN.** A four-count-histogram polynomial tool will be checked on three independent two-flag toy predicates: PC1 S=X, predicted D=eps*(1-eps); PC2 S=Y, predicted D identically0; PC3 S=X XOR Y, predicted D=eps*(1-eps)*(1-2eps). All use A always and B={X=1}. Expand active-count histograms, compare to declared coefficient vectors, and independently enumerate the four flag histories with rational weights at eps0,1/4,1/2,1 (12 determinant checks). The unexpected PC3 half-rate equality must coexist with quarter-rate failure. This validates certificate arithmetic, not Local's production table. Publish before execution.


**Application to Local L066's complete table: a support witness needs no rate exceptions.** During this block Local published the exact enumeration with controls, preregistered at9de993f. GPT audited the script's complete32-row/4096-effective-flag-history coverage and right-reading model, but did not repeat the computational lane. Take A={I2=1,E2=0} and B={I1=1,I2=1,E1=0,E2=0}. Local reports n_A=52736,n_(S,A)=9216,n_B=25600,n_(S,B)=0. Thus D(1/2)=-225/16384, an exact nonzero split. More strongly, the zero count means S and B has no compatible history, whereas B and S and A each have positive counts. All finite histories retain positive weight for every0<eps<1. Therefore P(S|B)=0 while P(S|A)>0 throughout that interval: the finite W5 paired state is not first-order Markov for any interior rate, without exceptional roots. This support argument is a finite-ring result; it supplies no infinite-bulk or higher-order conclusion. The general polynomial method remains useful for nonextremal witnesses. Independent review of this extension remains pending.


**PC1-PC3 outcome (2026-10-06 20:54 BST).** Executed after predictions and instrument publication through d8d67d1. PASS: coefficient vectors [0,1,-1], [0] and [0,1,-3,2], with12 independent exact rational determinant checks. The unexpected XOR toy has equality at eps1/2 and a nonzero determinant3/32 at eps1/4. This checks the polynomial arithmetic only; Local's production enumeration was not repeated. Independent review of G111 remains pending.

### G112. Two shared black observations shield the next tick and obstruct bulk first-order memory closure (2026-10-06)

**Status:** local proof and infinite-ensemble counterexample; WH1-WH3 pass, independently reviewed by Local L069. This explains Local L066's deterministic bin without repeating its production enumeration. It extends G109-G111 by a local argument, not by taking a ring limit. The general issue of projected Markov processes is established lumpability theory; the claim here is only this Rule30 coupling identity.

Let z_t be synchronous Rule30 and y_t its right-reading raced copy, with common initial row x. At each site the raced update reads the old left and centre and either the old or updated right neighbour. Write I_t=z_t(0), E_t=z_t(0) XOR y_t(0), K_t=(I_t,E_t). Flags may be arbitrary provided right recursions terminate. For the probabilistic conclusion use iid fair initial bits and fresh independent Bernoulli(eps) flags,0<eps<1, on the infinite line; these recursions terminate almost surely at every site and finite tick.

**First-step white agreement lemma.** If z_1(j+1)=y_1(j+1)=0, then z_1(j)=y_1(j). If x(j)=1, its old centre masks both right-read alternatives. If x(j)=0, the ideal right output0 equals x(j) XOR (x(j+1) OR x(j+2)), forcing x(j+1)=0. Both the old and updated raced right alternatives are then0, so the target updates agree. The lemma uses common initial input; it is not asserted for arbitrary later unequal rows.

**Two-black shielding.** Suppose z_1(0)=y_1(0)=z_2(0)=y_2(0)=1. The black old centre at site0 shields its tick2 right read. Output1 therefore forces z_1(-1)=y_1(-1)=0. Applying the white agreement lemma at j=-2 gives z_1(-2)=y_1(-2). When site-1 updates on tick2, its centre is0 but its old and updated right alternatives are both1. Its output is consequently the shared old left value XOR1, so z_2(-1)=y_2(-1). Site0's black old centre again shields tick3, yielding z_3(0)=y_3(0). Thus the refined bin

    B={I1=1,I2=1,E1=0,E2=0}

has next error E3=0 for every compatible shared-input history. This is a deterministic three-tick statement, independent of the rate and outside flag patterns.

**Positive finite cylinders, not an infinite clean event.** Define the nine update nodes C: tick1 sites-2..2, tick2 sites-1..1 and tick3 site0. Their ordinary ancestors are initial sites-3..3.

For initial word0110000 on-3..3 and all nine flags in C zero, both source traces have I1=I2=1, so B occurs. This cylinder has probability(1-eps)^9/128>0.

For initial word0000010 on-3..3, set only site0's tick1 flag in C to1 and all other eight to0. Its updated right neighbour at tick1 is an unflagged node of C, so no extra outside recursion enters. The ideal source trace at ticks0..3 is0011 and the raced trace0110: I2=1,E2=0,E3=1. The cylinder has probability eps*(1-eps)^8/128>0. Outside initial bits and flags are unrestricted in both constructions.

Take A={I2=1,E2=0} and S={E3=1}. The cylinders prove P(B)>0 and P(S and A)>0. The shielding identity proves P(S|B)=0, whereas P(S|A)>0. Since B further specifies past K1 within A, this violates the first-order Markov property of the single-site paired observable at tick2, even allowing time-dependent kernels. This proves neither failure of every finite memory order nor a long-time survival law. Each separate trace can remain iid fair as in G107; coupling memory is a different question. This is not a single-seed or prize claim.

**WH1-WH3 preregistered NOT RUN.** WH1: all initial rows and effective right-flag patterns on rings W3..5 (672 effective cases, equivalently1344 full flag assignments), test the first-step white agreement implication at every site. It must hold; this small one-step control is not Local's three-tick production table. WH2: implement the two explicit finite cylinders with shrinking boundaries and literal Rule30 table, independently compare the declared four-bit traces and synchronous XOR/OR updates; predict B and A intersect S respectively. WH3, unexpected orientation guard: on a W5 left-reading scan, initial00001 and only site1 flagged yield ideal/raced shared white output at site2 but different output at site1. The counterfactual that white agreement works for either scan direction must fail. Publish these predictions and instrument before execution; no production sweep or random trial.


**WH1-WH3 outcome (2026-10-06 20:59 BST).** Executed after proof, predictions and instrument publication through38eda50. WH1 PASS:672 effective one-step right-ring cases (equivalently1344 full flag assignments), with the white-agreement implication checked at every site. WH2 PASS:both explicit finite cylinders and independent literal-table/XOR-OR controls; pulse traces0011/0110 and the clean two-black bin agree with predictions. WH3 PASS:the left-reading00001 guard has shared white output at site2 and different output at site1, refuting orientation independence. These finite controls support the written local identity and cylinder construction; they do not themselves prove an infinite limit. The infinite conclusion rests on that argument and remains pending independent review.


### G113. A bounded audit of one-lag closure in the isolated-pulse paired trace (2026-10-06)

**Status:** LM1-LM3 preregistered NOT RUN. Existing G110 refutes first-order closure in the pulse model; G112 addresses fresh-race bulk first-order failure. Neither decides whether the enlarged state (K_(t-1),K_t) is sufficient. This block stays in the pulse model to seek an exact, inspectable history witness without duplicating Local's repeated-race jobs. General projected-memory theory is prior art, recorded with G112.

Start from an infinite iid fair row; only source0 reads its updated right neighbour on tick1, and all remaining reads are synchronous. Keep the pulse phase fixed and known. Source samples through tick6 depend only on initial sites-6..6. Uniform enumeration of those8192 words therefore gives exact finite-horizon probabilities in this infinite ensemble, without a ring limit. LM1 must reproduce the001 injection predicate and E1,E2,E3=indicator,0,indicator with independent literal-table/XOR-OR updates.

**Blind LM2 prediction:** at tick5, conditioning the next error E6 on K4,K5 differs from conditioning on K3,K4,K5 in at least one positive bin. Compare integer cross products for every child and parent. If no split occurs, retain the held finite result; that cannot establish two-step closure at all times. A nonzero split would refute order-two Markov at this tick for this pulse ensemble, not for fresh repeated Bernoulli flags. It would not refute every finite order.

**Unexpected LM3 control:** both separate seven-sample marginal histograms must still contain128 words64 times each, even if paired closure fails. The counterfactual that tick2 healing prevents tick3 return must fail by LM1. Run only after predictions and instrument are published. GPT owns this bounded history audit; no rate sweep, long run or Local spectrum repetition.

#### G113 result: one lag does not close the isolated-pulse paired trace at tick5 (2026-10-06)

**Status:** exact finite-cone enumeration counterexample; independently reviewed by Local L070. Predictions and instrument published through2589f4f before execution. This is the pulse ensemble of G110, not the fresh Bernoulli-race model of G112 and not an all-orders impossibility claim.

Let K_t=(I_t,E_t) for the source of two common-input Rule30 copies. Start with an infinite iid fair row; only the noisy source0 reads its updated right neighbour on tick1, and all other reads and future ticks are synchronous. Keep the pulse schedule fixed and known. The seven source samples at ticks0..6 depend only on the13 initial bits at sites-6..6; the pulse's extra same-tick right read needs initial sites0..2 and stays inside that domain. Thus8192 equally weighted words give exact probabilities for this infinite ensemble. Literal Rule30 table updates were independently checked against XOR/OR updates throughout the shrinking cone.

Take A={K4=(0,0),K5=(0,0)} and its refinement B=A intersect {K3=(0,0)}. LM2 counts n_A=1872,n_(E6=1,A)=40,n_B=896,n_(E6=1,B)=0. Therefore

    P(E6=1 | A)=40/1872=5/234,
    P(E6=1 | B)=0.

Both bins have positive probability. Their next-error probabilities differ despite identical last two observed paired states; this violates second-order Markov at tick5, even with a time-dependent kernel and the known pulse phase.

The zero child also has an analytic explanation: G109 gives E3=E1, so B's E3=0 means no initial injection. With no future races the two configurations then agree forever. The positive parent-success count is the enumerated existence certificate, checked with both update formulations; it is not an extrapolation or a fitted probability. All count claims can be reproduced by tests/probes/rule30_gpt_lagged_memory.py. Independent reading remains required.

**LM1-LM3 outcomes (2026-10-06 21:05 BST).** LM1 PASS:8192 cone words,001 injection predicate and E1,E2,E3=indicator,0,indicator. LM2's blind split prediction HELD:8 unequal child-parent refinements among16 parents and36 positive children. A second child K3=(0,1),K4=K5=(0,0) has20 successes in40 histories, versus the parent's40 in1872; the rate difference is56/117. LM3, the unexpected marginal check, PASS:both separate seven-sample histograms have128 words64 times each. The permanent-healing counterfactual is refuted by the source echo. Uniform marginals coexist with failure of order-two paired closure. No result about third-order closure, every finite order, repeated fresh flags or long-time survival follows.


**LM4 addendum preregistered NOT RUN (2026-10-06 21:09 BST).** Extract the lexicographically first13-bit word in each of B and {K3=(0,1),K4=K5=(0,0),E6=1}; previous counts896 and20 guarantee existence. Print its full source traces. Independently pad each word with both values on each outer initial site and run literal-table synchronous updates with the isolated pulse: all eight padded histories must preserve both source traces. This unexpected boundary check certifies finite cylinders with arbitrary exterior bits, rather than an implicitly zero exterior. Each specified13-bit cylinder has probability1/8192 in the infinite fair ensemble. Publish before execution.


**LM4 outcome and explicit positive cylinder (2026-10-06 21:09 BST).** Predictions and instrument published through832c0d3 before execution. PASS:the lexicographically first success word on sites-6..6 is0011110010000, with ideal source trace0110000 and noisy trace0011001 at ticks0..6. It has K3=(0,1),K4=K5=(0,0),E6=1. The zero-child witness is0000000000000 with both traces0000000. These specify only13 initial bits, not the whole infinite row; each cylinder has probability1/8192. All eight independently implemented padded-boundary histories preserve the predicted traces. Arbitrary exterior independence follows from the explicit finite ancestor cone, not from extrapolating those eight tests.

Consequently the proof's positive parent-success event can be checked by forwarding this single finite word, without trusting a total-count census. The zero child follows analytically from E3=E1 and no future injections, while this cylinder gives P(E6=1 and A)>0 and hence P(E6=1|A)>0. The exact5/234 rate remains the independently controlled enumeration result; the order-two counterexample itself now needs only the identity and a finite positive cylinder. This strengthens inspectability without changing the pulse-model scope or claiming every finite memory order.


### G114. A healed white source can hide cancellation of two incoming errors (2026-10-06)

**Status:** local algebraic identity and pulse mechanism; DP0-DP2 pass, independently reviewed by Local L071. This unpacks G113's explicit witness. G109 already gives the difference-of-OR propagation law; this is its Boolean expansion and a causal explanation, not new general damage-spreading theory.

For a synchronous tick, let a,b,c be ideal left, centre and right bits and p,q,r their respective XOR errors. Expanding OR over binary arithmetic gives

    delta_next = p XOR ((1-c)*q) XOR ((1-b)*r) XOR (q*r).

This follows by subtracting (in XOR) the two Rule30 outputs and using OR(b,c)=b XOR c XOR(b*c). If the source is currently healed, q=0, the update reduces to

    delta_next = p XOR ((1-b)*r).

At a shared black centre only the left error matters. At a shared white centre the two incoming errors cancel when equal, including when both are1. Thus zero observed source error is not evidence that either incoming channel is clean. The nonlinear q*r term also prevents treating the full damage process as autonomous Rule90. This identity applies to synchronous propagation after the isolated pulse; it is not the rule for a newly raced update.

**Hand derivation for G113's finite cylinder.** Initial sites-6..6 are0011110010000; only source0 races right on tick1. In the shrinking source cone, predicted ideal/noisy rows are:

| Tick | Sites | Ideal | Noisy |
|---|---|---|---|
| 3 | -3..3 | 1010101 | 1111011 |
| 4 | -2..2 | 01010 | 00001 |
| 5 | -1..1 | 101 | 001 |

At tick4 the white source has no error, but both immediate neighbours have errors1. These cancel, producing another healed source at tick5. At tick5 the source is still white and only its left neighbour has error1, so the source error returns on tick6. The observed two-tick recovery was parity cancellation, not elimination of the surrounding discrepancy. Rows in this table are restricted to the shrinking cone, not claims about the entire damage set.

**DP0-DP2 preregistered NOT RUN.** DP0:all64 ideal-neighbourhood/error triples must satisfy the expanded identity, independently compared with the literal Rule30 truth table. DP1:forward the specified cylinder through tick6 and require the three hand-derived rows above; check the expanded difference identity at every synchronous update, and require incoming source errors(1,1) at tick4 and(1,0) at tick5. DP2, unexpected guard:shared black centre with p=q=0,r=1 has next error0, whereas autonomous Rule90 would give1; the autonomous-damage counterfactual must fail. Publish before execution. No new production table or repeated-race job.


**DP0-DP2 outcome (2026-10-06 21:16 BST).** Ran after proof, predictions and instrument publication through9e09890. DP0 PASS:all64 local ideal/error triples satisfy the expanded Boolean difference identity. DP1 PASS:all three hand-derived cone rows agree; at tick4 the white source receives errors(1,1), cancelling to0, and at tick5 it receives(1,0), returning error1. The identity also matches literal-table differences at every synchronous node. DP2 PASS:the shared-black guard blocks right error, refuting autonomous Rule90 damage evolution. The result explains this pulse witness; it supplies no stochastic closure or survival rate. Independent review pending.


### G115. Audit an injection-indicator state against the full observed pulse history (2026-10-06)

**Status:** IS0-IS2 preregistered NOT RUN. Responds to Local L070's proposed injection-history state. In the isolated-pulse ensemble of G113, define F=E1, the actual injection indicator, not merely the occurrence of a raced read. If F=1 its injection time is always tick1, so at fixed tick5 its age is already known. Test the more generous candidate X5=(F,K4,K5), retaining both recent paired observations.

Enumerate the same8192 initial cone words and use the independently checked update formulations. IS0 must recover F=E3 and the001 predicate, all bin totals, and the known unaugmented zero-child0/896 versus parent40/1872 witness. IS1's blind prediction is that at least one positive refinement by the entire observed prefix K0..K5 has a different E6 rate from its X5 parent. Integer cross products decide equality exactly. A failure would refute this specified candidate in this pulse ensemble; a held finite table would not prove closure at all times.

**Unexpected IS2 prediction:** the shallower comparison using only K3 may hold after conditioning on F, even if the full-prefix comparison splits. This tests whether a diagnostic can miss deeper observed information. Retain either outcome. The counterfactual that omitting F closes the one-lag state must fail by IS0. No repeated-race injection definition is imported, no Local production job is repeated, and no all-orders conclusion is predicted. Publish instrument and predictions before execution.

#### G115 result: injection memory plus one lag still misses deeper observed pulse history (2026-10-06)

**Status:** exact finite-cone candidate-state counterexample; independently reviewed by Local L072. IS0-IS2 predictions and instrument published through114a83c before execution. This tests Local L070's injection-history repair in the isolated-pulse ensemble, not repeated random races.

Use the same8192 fair initial cone words as G113. Define F=E1, the actual injection indicator, and candidate X5=(F,K4,K5). Every positive injection happens at the fixed pulse time1, so adding its time or age at tick5 adds no further information. Refine each candidate bin by the full observed history H=(K0,...,K5). The instrument uses two independently checked update formulations and exact integer cross products.

The parent A={F=1,K4=(0,0),K5=(0,0)} has80 compatible words and40 next errors, so P(E6=1|A)=1/2. Its full-history child

    H=((0,0),(0,1),(0,0),(0,1),(0,0),(0,0))

has20 compatible words and no next error, so P(E6=1|H)=0. Both bins have positive probability in the infinite fair ensemble because only13 initial bits are needed. Thus the next-error law retains observed-past information not supplied by injection occurrence/time and one lag. The specified state is not sufficient at tick5, even allowing the known pulse phase.

A concrete word in the zero child is0101100010000 on-6..6. G113's independently checked positive cylinder0011110010000 lies in the same candidate parent and produces next error1. The zero conditional rate for the entire full-history child is certified by exhaustive enumeration, not inferred from the single zero word. Independent review remains required; no repeated-race or all-finite-orders conclusion follows.

**IS0-IS2 outcomes (2026-10-06 21:19 BST).** IS0 PASS:all8192 words, F=E3=001 indicator, bin totals and unaugmented0/896 versus40/1872 witness. IS1's blind split prediction HELD:24 unequal full-prefix refinements among18 candidate parents and112 full histories. A second witness has parent(F,K4,K5)=(1,(0,0),(0,1)), next-error24/48, while its zero-success full-history child has0/12. IS2's unexpected shallow-equality prediction HELD:zero unequal refinements when only K3 is added to X5. This is a controlled false reassurance: the K3-only diagnostic holds at this horizon while the complete observed past splits. No held finite diagnostic is promoted to closure. The unaugmented one-lag closure counterfactual remains refuted.

### G116. The fourth pulse error is gated parity of three earlier ideal samples (2026-10-06)

**Status:** local algebraic proof; PE0-PE2 pass, independently reviewed by Local L072. Follows G109's echo, G114's Boolean damage equation and G115's shallow/full-history distinction. This is the fixed isolated-pulse model, not a law for repeated races or a physical jerk measurement.

Write F=E1 for actual injection and I_t for ideal source0. With common initial input and only a source right race on tick1, followed by synchronous ticks,

    E4=F*(I1 XOR I2 XOR I3).

If F=0 there is no changed cell and all later errors vanish. If F=1, initial sites0..2 are001. Ideal first-tick sites1 and2 are therefore both1. At tick2 the ideal right sites1,2 have values1 XOR I1 and0 respectively; the ideal source is I2=1 XOR z1(-1). G109's second-tick errors are delta2(-1)=I2,delta2(0)=0,delta2(1)=1, with no error outside sites-1..1.

Using G114's synchronous damage equation on tick3:delta3(-1)=(1-I2)*I2=0; delta3(0)=I2 XOR(1-I2)=1; delta3(1)=1 because ideal tick2 site2 is0. Independently the ideal tick3 site1 is I2 XOR(1 XOR I1). Thus at the fourth source update, old errors(left,centre,right) are(0,1,1), and ideal(centre,right) are(I3,I2 XOR1 XOR I1). Flipping both OR inputs changes their OR by1 XOR centre XOR right. Substitution gives E4=I1 XOR I2 XOR I3, proving the gated identity.

**Conditional fair law.** Under F=1, the initial negative bits remain independent fair. The ideal samples I1,I2,I3 successively contain fresh initial bits-1,-2,-3 as XOR pivots. Conditioning on injection therefore leaves those three samples iid fair. Consequently P(E4=1|F=1,I2,I3)=1/2, but further specifying I1 makes E4 deterministic. Unconditionally P(E4=1)=1/16. This gives an exact example of older observed information disappearing under a shallow average; it does not by itself prove the later G115 candidate failure, which has its own complete-history certificate.

**PE0-PE2 preregistered NOT RUN.** Enumerate512 initial words on-4..4 through four ticks, with independent literal-table/XOR-OR updates. PE0 must reproduce F=001 and E1,E2,E3=F,0,F. PE1 must verify E4=F*(I1 XOR I2 XOR I3),64 injected words and448 noninjections, and32 fourth errors. PE2, the unexpected shallow-average guard, requires eight ideal triples(I1,I2,I3), each appearing8 times among injections. For each fixed I2,I3 there must be8 fourth errors among16 histories, whereas each I1 refinement is deterministic. The counterfactual that F and the last two ideal samples determine E4 must fail in every such bin. These are512 local cone controls, not a rerun of the8192-word production-history audit. Publish before execution.


**PE0-PE2 outcome (2026-10-06 21:25 BST).** Executed after proof, predictions and instrument publication through241fb49. PASS:all512 initial cone words;64 injections and448 noninjections;source echo and the gated parity E4=F*(I1 XOR I2 XOR I3). Exactly32 fourth errors. Among injections every one of the eight ideal triples appears8 times. Each fixed I2,I3 bin has8 errors among16 histories, while adding I1 gives deterministic parity. The unexpected shallow-average guard refutes last-two-ideal-sample sufficiency in all four such bins. Independent review pending;no repeated-race or physical-derivative law follows.

### G117. A hidden right-tail bit first enters the fifth pulse-error law (2026-10-06)

**Status:** local algebraic kernel and fair-ensemble law; FT0-FT2 pass, independently reviewed by Local L073. Continues G116 in the fixed isolated-pulse model. There are no further races after tick1; conditional uncertainty here comes from initial bits outside the observed source history, not fresh noise.

Condition on injection F=1, so old sites0..2 are001. Put D=x(3)*(x(4) OR x(5)), for the common initial row x. Write a=I1,b=I2,c=I3,d=I4 and define

    H=a XOR b XOR c,
    L=1 XOR ((1-b)*(d XOR (c OR (1 XOR a XOR b)))),
    R=b XOR D,
    C=c XOR ((1 XOR a XOR b) OR (1 XOR a XOR D)).

Then the fifth source error is

    E5=L XOR ((1-C)*H) XOR ((1-d)*R) XOR (H*R).

**Derivation.** G116 gives source delta4=H and ideal tick3 site1=1 XOR a XOR b. Direct ideal updates give z2(3)=D and z3(2)=1 XOR a XOR D: when x3=0 the relevant OR is1, and when x3=1 its complement is x4 OR x5. Hence ideal tick4 site1 is C. Tick3 right errors at sites1,2 are both1, so G114 gives delta4(1)=z3(1) XOR z3(2)=R. On the left delta3(-1)=0,delta3(0)=1 and delta3(-2)=(1-z2(-2))*b. If b=1, z3(-1)=1 XOR z2(-2), so delta4(-1)=1; if b=0 it is1 XOR z3(-1). Since z3(-1)=d XOR(c OR (1 XOR a XOR b)), these cases give L. Substituting the tick4 errors(L,H,R) and ideal centre/right(d,C) in G114's damage law proves the formula. For F=0 the copies remain identical, so E5=0.

**Exact fair conditional kernel.** After fixing F=1, D has probability3/8 of being1. Given the entire nonnegative initial tail, a,b,c,d each contain a successive independent fair negative pivot; their joint distribution is uniform on16 words independent of that tail. Thus D is independent of the ideal prefix. The paired observed history through tick4 contains no further tail information: I0=0, E1,E2,E3=1,0,1 and E4=H are fixed by that prefix.

Let g(a,b,c,d,D) denote the displayed formula. Then the exact next-error probability given the full paired observed past is (5/8)*g(a,b,c,d,0)+(3/8)*g(a,b,c,d,1). Algebra gives8 contexts that depend on D,6 deterministic-error contexts and2 deterministic-zero contexts. Of the8 mixed contexts,6 have rate3/8 and2 have rate5/8. Therefore

    P(E5=1)=19/256,
    H(E5 | K0,...,K4)=h2(3/8)/16,

where h2 is binary entropy in bits. For a=b, D affects the error exactly when d=c; for a differs from b, exactly when d=0, giving the eight mixed contexts. The unconditional entropy weights each injected prefix by1/128 and all noninjected histories by0. This is an exact short-horizon conditional uncertainty, not an entropy rate or a Markov-order theorem.

**FT0-FT2 preregistered NOT RUN.** Enumerate2048 initial words on-5..5 through tick5. Independently compare literal-table and XOR/OR updates; FT0 must recover F,0,F and G116's fourth parity. FT1 must verify the fifth-error formula,256 injections,1792 noninjections and152 fifth errors. Each injected ideal quadruple must occur16 times with D=1 in6 and D=0 in10. The16 conditional error counts must have histogram{0:2,16:6,6:6,10:2}. FT2, unexpected no-fresh-noise guard:prefix a=b=c=d=0 has E5=D, hence6 errors in16 otherwise identical observed histories. Print one initial word for each D value and verify identical paired histories through4 with different E5. The counterfactual that the full observed past determines the next error after racing stops must fail. Publish before execution; no repeated-race production job.


**FT0-FT2 outcome (2026-10-06 21:30 BST).** Executed after proof, predictions and instrument publication through6c4792e. PASS:2048 initial cone words,256 injections and152 fifth errors. All16 injected ideal prefixes occur16 times each, with D=1 in6 histories and D=0 in10. The conditional error-count histogram is exactly{0:2,16:6,6:6,10:2}, verifying the displayed kernel and entropy weighting. Independent literal-table/XOR-OR updates agree. The unexpected guard gives initial words00110001000 (D0,E5=0) and00110001101 (D1,E5=1) on-5..5, both with identical paired history((0,0),(0,1),(0,0),(0,1),(0,0)) through tick4. No fresh flags are present after the pulse. Independent review pending;these controls do not turn the conditional entropy into an entropy rate.

### G118. Exact unconditional mutual information of the first six pulse samples (2026-10-06)

**Status:** short-horizon entropy proof; JI0-JI2 pass, independently reviewed by Local L074. Complements G108's conditional coupling law using G116-G117. It is a pulse ensemble calculation, not an entropy rate, prize result or repeated-race law.

Let A=(I0,...,I5),B=(J0,...,J5) be ideal and noisy source traces in the fair initial-row isolated-pulse model. Both are iid fair by G97/G107, so H(A)=H(B)=6 bits. XOR-error history E is in bijection with B once A is given. Write h2(p) for binary entropy, with0*log2(0)=0. Then

    H(A,B)=6+h2(1/4)/2+h2(3/8)/16,
    MI(A;B)=6-h2(1/4)/2-h2(3/8)/16.

**Proof.** F=E1 is the001 injection indicator. Given I0=1, F=0; given I0=0, F is Bernoulli1/4. Fixing the nonnegative initial tail leaves the ideal samples I1..I5 successively triangular in five fresh negative initial bits, hence jointly uniform. Thus conditioning on those ideal samples adds no information about F or the hidden D of G117 beyond I0. In particular H(F|A)=h2(1/4)/2, not h2(1/8).

If F=0 the whole error history is zero. If F=1, its first five entries are0,1,0,1,I1 XOR I2 XOR I3. Only E5 remains to be specified. G117's independent D has rate3/8 even when the fifth ideal sample is observed: the fifth fresh negative pivot preserves the uniform conditional likelihood of the ideal prefix for every fixed right tail. Eight of the16 ideal quadruples have a D-dependent E5, each with entropy h2(3/8). Since P(F=1)=1/8, H(E5|F,A)=h2(3/8)/16. The first error identifies F, so entropy chain rule gives H(E|A)=H(F|A)+H(E5|F,A). Add H(A)=6 and subtract from H(A)+H(B)=12 to prove the formulas.

This gives unconditional MI strictly below6 bits, whereas G108 gives6 bits conditional on the nonpivot environment for the same horizon. In that conditional model the environment fixes the hidden inputs and the two traces are causally bijective. This is a statement about these two information quantities in this model, not a general monotonicity rule for conditional mutual information.

**Exact joint-count predictions.** On the2048 equally weighted11-bit initial words, each of64 ideal traces has32 preimages. For the32 traces with I0=1 all32 give one paired trace. For I0=0,24 are noninjections. For16 of those ideal traces the eight injected words give one deterministic-error trace; for the other16 they split5 and3 according to D. Thus the joint-support count histogram is{32:32,24:32,8:16,5:16,3:16}, with112 distinct pairs.

**JI0-JI2 preregistered NOT RUN.** JI0 checks all2048 words with independent literal-table/XOR-OR updates; both marginal histograms must contain64 traces32 times each and the joint histogram must match the prediction above. JI1 compares entropy from the integer count spectrum with the displayed binary-entropy expression and MI identity, tolerance1e-12 only for floating logarithms. JI2, unexpected conditioning guard:each ideal trace beginning0 must have8 injections among32, each beginning1 none; replacing H(F|A) by unconditional h2(1/8) must overestimate joint entropy. Publish before execution. No production job or asymptotic inference.


**JI0-JI2 outcome (2026-10-06 21:36 BST).** Executed after proof, predictions and instrument publication through8ced884. PASS:2048 words;both marginal histograms have64 traces32 times each. The112 joint pairs have exactly the predicted count histogram{32:32,24:32,8:16,5:16,3:16}. Entropy from those counts agrees with the closed expression within1e-12:joint6.465291187412 bits,mutual information5.534708812588 bits. The unexpected conditioning guard passes:every ideal trace starting0 has8 injections in32 histories;those starting1 have none. Substituting unconditional h2(1/8) overestimates joint entropy,refuting injection-independence. Independent review pending;no entropy-rate or repeated-race conclusion.

### G119. Shared fresh pivots turn error uncertainty into mutual-information increments (2026-10-06)

**Status:** general right-reading fair-ensemble identity; GF0-GF2 pass, reviewed by Local L075. Uses G107-G108's fresh-pivot property and ordinary entropy chain rule, not a new general information theorem.

Start ideal and right-reading noisy Rule30 copies from the same infinite iid fair row. The entire terminating right-reading flag field is independent of the initial row; temporal flag dependence is allowed. Observe both on a predetermined nonrightward path p_t. Put K_t=(I_t,J_t),E_t=I_t XOR J_t and M_t=MI(I0..It;J0..Jt), with empty-prefix M_-1=0. Then

    M_t-M_(t-1)=1-H(E_t | K0,...,K_(t-1)),
    M_T=(T+1)-sum_(t=0..T) H(E_t | paired past).

Each increment is between0 and1 bit;M_0=1 since the initial copies agree. No limit or entropy rate is asserted.

**Proof of the required conditional freshness.** The initial pivot index L_t=p_t-t strictly decreases. By G107-G108, both samples have form X_(L_t) XOR u_t and X_(L_t) XOR v_t, where u_t,v_t depend only on initial bits strictly to the right of L_t and the independent flag field. All prior paired samples also depend only on those higher initial bits and flags. The shared pivot remains a fresh fair bit even after conditioning on the whole paired past and E_t=u_t XOR v_t. Hence each current marginal sample is fair independent of that conditioned information, and

    H(I_t,J_t | paired past)=H(I_t,E_t | paired past)=1+H(E_t | paired past).

Each separate trace is iid fair, so extending each marginal prefix adds1 bit of entropy. Extending the joint prefix adds the displayed1+conditional-error term. Subtracting joint entropy from the sum of marginal entropies proves the increment identity;telescoping proves the total. This argument establishes unconditional information growth, unlike G108's result conditioned on the entire environment.

The relevant property is a common unused pivot relative to the paired history, not merely two iid marginal traces. Adaptive paths, reused finite-ring pivots, state-dependent flags and nonterminating right chains are outside the proof. Biased initial rows do not supply the fair-bit baseline. This gives no closure of the error history and no asymptotic information rate.

**GF0-GF2 preregistered NOT RUN.** Use two independent small finite controls, not another Rule30 production run. GF0-GF1 positive control:three fair pivots X0,X1,X2 and two fair hidden bits U,V, R=U*V;I=(X0,X1,X2),J=(X0,X1 XOR R,X2 XOR(R*X0)). All32 histories have equal weight. Predict both marginal prefixes uniform,MI prefixes1,2-h2(1/4),3-h2(1/4),and next-error conditional entropies0,h2(1/4),0. Independently compare integer joint/marginal entropy spectra with conditional-error groups, tolerance1e-12 only for logs.

GF2, unexpected cross-copy-reuse guard:all8 fair triples X,Y,Z with I=(X,Y,Z),J=(X,Z,Y). Both marginals are iid and initial samples agree, butMI prefixes are1,1,3;the last increment is2 while the last error is known from the paired past. The formula would predict1 there and must fail. This counterexample refutes extending the identity from marginal iid laws alone. Publish before execution. It is a scope control, not a Rule30 counterexample.


**GF0-GF2 outcome (2026-10-06 21:40 BST).** Executed after proof,predictions and instrument publication through439744b. PASS:the32 positive histories have uniform marginal prefixes,MI1,2-h2(1/4),3-h2(1/4),and conditional-error entropies0,h2(1/4),0;the increment identity agrees within1e-12. The unexpected8-history reuse guard has MI1,1,3 and zero final error uncertainty,yet final MI increment2. It refutes extending the identity from marginal iid laws alone. The general Rule30 result rests on the written common-fresh-pivot proof,not on extrapolating toy cases. Independent review verified by Local L075;no limit or rate inferred from the controls.

### G120. Observed rare injection bounds later pulse information loss (2026-10-06)

**Status:** pulse-model entropy bound; RB0-RB2 pass, reviewed by Local L076. Corollary of G119, conditional on its scope. The asymptotic statement is a liminf bound, not existence or evaluation of an information-rate limit. It does not concern repeated races or the selected Rule30 seed.

In the common-input fair isolated-pulse model, F=E1 is observable from K1 and P(F=1)=1/8. If F=0 the pulse changes no cell, and subsequent synchronous evolution preserves equality of the entire configurations. For t>=2 the paired past contains F. Thus

    H(E_t | paired past)=P(F=1)*H(E_t | paired past,F=1)<=1/8.

Here the second conditional entropy is averaged over histories within the injected branch. Dependence between F and the initial source bit causes no problem:the weights in conditional entropy average to the unconditional branch probabilities. The bound uses both F's measurability from the past and the zero-error noninjected branch.

G119 therefore gives

    M_t-M_(t-1)>=7/8 for t>=2,
    M_T>=2-h2(1/4)/2+(7/8)*(T-1) for T>=1.

Using G118's exact six-sample result gives the sharper finite bound

    M_T>=6-h2(1/4)/2-h2(3/8)/16+(7/8)*(T-5) for T>=5.

Consequently liminf_(T->infinity) M_T/(T+1)>=7/8. Mutual information per sample is also at most1 by the marginal entropy bound. This does not prove the normalized sequence converges, determine its limit, or control the injected branch's damage lifetime. In particular,the seven-eighths lower bound partly comes from histories in which the pulse never injects;it is not a claim that active damage preserves seven-eighths of its information.

**Why observability is essential.** If F is not determined by the conditioned past, separating the branches also costs uncertainty about F. An event with small probability alone does not justify H(error|past)<=P(F=1). The scope guard below keeps the fresh-pivot information identity but hides F,so it must violate the rare-event budget rather than the identity itself.

**RB0-RB2 preregistered NOT RUN.** Positive control:64 equal-weight fair histories of X0,X1,X2,U,V,Q, with F=(1-X0)*(1-U)*V. Set I=(X0,X1,X2),J=(X0,X1 XOR F,X2 XOR(F*Q)). RB0 checks uniform marginals,P(F1)=1/8,and F observable after the first error. RB1 must give final conditional-error entropy1/8 and final MI increment7/8,showing the budget can be tight. Independently compare grouped error entropy with joint/marginal count spectra.

RB2, unexpected hidden-event guard:32 fair histories of X0,X1,U,V,Q with the same F,but I=(X0,X1),J=(X0,X1 XOR(F*Q)). The initial paired past does not reveal F. Predict next-error entropy h2(1/8)/2>1/8 and MI increment1-h2(1/8)/2<7/8,while both marginals remain iid and the fresh-pivot identity holds. The counterfactual that injection probability alone supplies the budget must fail. Tolerance1e-12 only for logarithms;publish before execution. No production scaling run.

**RB0-RB2 outcome (2026-10-06 21:48 BST).** Executed after9f37d68 published the proof,predictions and instrument. PASS:64 equality-case histories give observed F,probability1/8,error entropy1/8 and MI increment7/8. The32 hidden-F histories give error entropy0.271782221600 and increment0.728217778400,violating the rare-probability-only budget while satisfying the fresh-pivot identity. Independent grouped-error and joint-count calculations agree within1e-12. These toy controls check the scope;the all-time pulse bound follows from the written conditional-entropy proof. Reviewed by Local L076.

### G121. Finite-predecessor descent reduces counterexamples to roots, not bounded width (2026-10-06)

**Status:** paper proof and failed bridge, reviewed by Local L077. Responds to Cloud CL005's minimal-counterexample suggestion. No experiment or production run. This does not prove period-two exclusion or a prize result.

Let F be synchronous Rule30 on the infinite zero background. For a nonzero finite configuration x let [L,R] be its smallest support interval and w=R-L+1 its span, including internal zeroes. Its image has support endpoints exactly L-1,R+1:the outside adjacent triples are001 and100,both producing1,and all further outside triples are000. Therefore span(F(x))=w+2. This is an endpoint theorem,not a monotonicity theorem for the number of black cells.

F is injective on finite configurations. If two finite rows differ,let k be their rightmost differing site. Their values at k+1,k+2 agree,so their next values at k+1 differ:the left argument enters by XOR. Hence a finite row has at most one finite predecessor. If y has span w and a nonzero finite predecessor,that predecessor has span w-2. Iterating finite predecessors therefore terminates in a unique finite root r with no finite predecessor,and y=F^a(r) for a unique nonnegative age a. Its span is span(r)+2a. This is descent of ancestry,not descent along forward time.

Suppose a finite row is a counterexample to eventual-period-two exclusion at a fixed spatial column. Its finite predecessor,if present,is also a counterexample at that same column:the traces differ only by one initial time step. Thus every counterexample descends to a root counterexample,and a globally minimum-span counterexample must be a root. No phase assumption is needed because eventual alternation tolerates a time shift. Conversely,a root counterexample's forward images remain counterexamples. This gives an exact reduction to roots,without asserting any root is a counterexample.

**Where the bridge fails,for all widths.** Normalize support endpoints to0 and w-1,so for w>=2 there are2^(w-2) finite words. For w>=4 the images of normalized span-(w-2) words give exactly2^(w-4) distinct normalized span-w words,by endpoint growth and finite injectivity. Exactly one quarter have finite predecessors;the other three quarters,3*2^(w-4),are roots. For w=3 the sole image is111 from1;101 is a root. The span-one and span-two words are roots. In particular roots exist at every width. The predecessor reduction supplies no upper bound on a minimal counterexample's width and no induction step that covers the roots. The selected single-black-cell seed is already a root.

**Unexpected scope check,by hand.** The counterfactual "left permutivity gives a finite predecessor for every finite row" fails already on a single black cell:every nonzero finite image has span at least3,and the zero row maps to zero. Yet every finite output block has a compatible longer input block by right-to-left inversion (G104);compactness gives global predecessors. Such predecessors of this root must have infinite support. So full-shift surjectivity cannot supply the missing finite descent. This distinction is standard cellular-automaton background:see Jarkko Kari's [Cellular Automata tutorial](https://users.utu.fi/jkari/wp-content/uploads/sites/1251/2023/12/CAintro.pdf),slides89-100,on finite injectivity versus finite surjectivity and infinite predecessors. No novelty claim for finite injectivity;the present application identifies the precise failure of this proposed bridge.

**Next proof obligation.** A minimal-counterexample argument needs a different transformation that preserves eventual alternation while shrinking a root,or a theorem excluding every root. Removing an endpoint by hand has no established trace-preservation property:its causal cone eventually reaches any fixed observation column,so finite propagation alone guarantees no forever equality. The root count is not evidence of period-two survival. Ordinary inverse-time descent alone is closed as a complete proof route;other shrinking transformations remain open.

### G122. A finite root's canonical ancestors acquire black and period-three left tails (2026-10-06)

**Status:** symbolic inverse-map proof; reviewed by Local L077. Extends G121's failed descent by identifying the class it leaves. No new experiment. Does not exclude eventual temporal alternation at a fixed column.

Call a row right-quiescent when it is zero at all sufficiently large spatial indices;it may be infinite to the left. Rule30 is bijective on this class. To invert a right-quiescent output y,choose B beyond its rightmost possible nonzero cell,set x_B=x_(B+1)=0,and recursively solve

    x_(i-1)=y_i XOR (x_i OR x_(i+1))

for every i<=B. Set all x_i=0 for i>B. This produces a right-quiescent row satisfying F(x)=y at every site. Uniqueness follows from G121's rightmost-difference argument,which still applies to two rows bounded on the right even when both have infinite left tails. Taking a larger B only adds zero recursion steps,so the inverse is independent of the cutoff. No claim of bijectivity on the whole two-sided full shift is made.

For a finite nonzero output y,its canonical predecessor has an eventually constant left tail. Indeed below y's leftmost nonzero site,the recursion has y_i=0. On adjacent inverse bits (u,v)=(x_i,x_(i+1)),the descending spatial map is

    M0(u,v)=(u OR v,u).

Its complete graph is00->00,01->10,10->11,11->11. Every state reaches00 or11 within two steps. Thus the inverse is either finite (left tail0) or has left tail1. A G121 root has no finite predecessor,so its unique right-quiescent predecessor must be eventually black on the left. This is a necessity and sufficiency test for root status;an infinite black tail is not extra input freedom once the right-quiescent inverse is fixed.

Take one more canonical predecessor of such a root. In its far left recursion the output is now constantly1,so

    M1(u,v)=(1 XOR (u OR v),u).

The complete graph is00->10->01->00 and11->01. Every state joins the three-cycle within one step. Consequently the second canonical predecessor has a far-left spatial tail of least period3,with repeating bits001 up to phase. The tail is spatial,not a period-three source trace. As a direct independent local check,the cyclic triples of001 are100,001,010,and Rule30 maps each to1;the constant1 row maps to0. This verifies the far-left forward sequence001->1->0 without using the inverse-state graph. These two hand checks are exact truth-table evaluations,not an extrapolated probe.

**Unexpected scope check.** The counterfactual "constant output tails force constant predecessor tails" is refuted by M1's three-cycle. Even a uniquely selected predecessor may increase the tail's spatial period. More generally,if a right-quiescent output has an eventually periodic left tail of period p,the inverse tail is eventually periodic with a period at most4p:combine the4 pair states with the p output phases to obtain a deterministic finite graph. Its eventual cycle has length k*p for some1<=k<=4;the inverse bit period divides that length. No uniform bound over repeated inversions follows.

**Bridge interpretation.** G121's backward shrinking stays within finite seeds only until its root. Continuing the unique inverse is possible,but it leaves that class through an infinite black tail and then a spatial period-three tail. Thus lack of a finite predecessor is not lack of a global predecessor. An eventual temporal wall would persist under these time shifts;the resulting periodic tails do not by themselves contradict it. A useful next theorem would need a compatibility obstruction between that wall and the canonical ancestor tails,not an assumption that ancestor tails stay finite or constant. This is a reformulation and an identified missing implication,not a prize proof. Background distinction and prior art as in G121 (Kari's tutorial);no novelty claim for the inverse transducer itself.

### G123. Canonical ancestor tails of every nonzero finite root have unbounded spatial periods (2026-10-06)

**Status:** all-depth paper theorem using G121-G122's inverse construction; reviewed by Local L078. No measurement or new experiment. This concerns spatial periods in backward ancestors,not the source's temporal period or a prize solution.

Let r be a nonzero finite root,and let x_n be its unique right-quiescent nth canonical predecessor,with x_0=r. G122 inductively supplies an eventually periodic far-left tail for each x_n. Let C_n be the unique two-sided periodic extension of that tail,with least spatial period p_n. C_0 is the zero row,C_1 the one row,and p_0=p_1=1,p_2=3.

The extensions obey F(C_n)=C_(n-1). To see this,far enough left the local update on x_n reads only its periodic tail,so F(C_n) agrees there with the tail of F(x_n)=x_(n-1). Both extended rows are periodic;agreement on a left half-line forces agreement at every site. Thus F^n(C_n)=0 and F^(n-1)(C_n)=1. Zero is absorbing,so C_n first reaches zero after exactly n steps. This is exact for all n,not a horizon fit.

All n+1 rows C_n,F(C_n),...,F^n(C_n) are distinct. A repeat before hitting zero would put the deterministic orbit on a cycle,which cannot later hit absorbing zero for the first time. Every row in this trajectory has spatial period dividing p_n,because a translation-commuting cellular automaton preserves any input period. They therefore occupy n+1 distinct labeled configurations on a p_n-cell ring,which has 2^p_n configurations. Consequently

    n+1 <= 2^p_n,
    p_n >= ceil(log2(n+1)).

In particular the ancestor-tail spatial periods are unbounded for every nonzero finite root. Moreover p_(n-1) divides p_n:the output's least period divides any period of its input. Combined with G122,p_(n-1)<=p_n<=4*p_(n-1). The divisibility chain must have infinitely many strict increases. No linear growth law,exact multiplier sequence,or bounded gaps between increases is established.

**Independent perspective and unexpected check.** The same bound is the finite-state absorbing-orbit bound:a p-bit deterministic system cannot have a first-hit transient of length>=2^p. This checks the indexing without the inverse graphs. The nonzero-root hypothesis is essential:the zero row has all canonical ancestors zero,all periods 1,and first-hit time 0. Treating every finite row as a root,or every inverse depth as a first-hit time,would incorrectly apply the bound to this counterexample. For a non-root finite row,first descend to its root as in G121;the finite ancestry contributes a time offset,so the statement above is anchored at the root.

**What this bridges and what it does not.** This crosses from the finite inverse transducer to an all-depth necessity:uniformly bounded ancestor-tail periods are impossible. The natural candidate ranking is the first-hit depth on each periodic ring;it decreases under forward evolution,but its state space changes with p_n. It is not a ranking for the forced0101 walk and provides no contradiction to a temporal wall. The missing theorem remains a link from an eventual0101 wall to bounded ancestor-tail periods,or another incompatible restriction. Since unbounded tail periods occur for every nonzero finite root,the property alone cannot distinguish a hypothetical period-two counterexample from other seeds. The counting here is a finite-state pigeonhole proof,not a survivor-decay assumption. The finite-state pigeonhole bound is elementary. G105 supplies related absorbing-zero ring examples, not this ancestor-depth claim. No novelty claim for the general orbit bound.

### G124. Periodic Rule 30 rows that eventually reach zero have periods 1 or three times a power of two (2026-10-06)

**Status:** symbolic inverse-transducer theorem; reviewed by Local L078. No new experiment. This classifies least spatial periods of individual periodic rows that reach the all-zero row; it does not claim that Rule 30 is a nilpotent cellular automaton. It supplies no temporal-wall exclusion.

Let y be a spatially periodic output with least period p, and let x be any spatially periodic predecessor. Translation invariance implies p divides x's least period q. Inverting from right to left uses G122's pair maps

    M0(u,v)=(u OR v,u),
    M1(u,v)=(1 XOR (u OR v),u).

If y is nonconstant, p>=2 and one output symbol in a period is zero. Choose the period cut so the first descending symbol is that zero. The first map sends all four pair states into T={00,10,11}. The following map sends T to at most two states, regardless of the next symbol:

    M0(T)={00,11},
    M1(T)={10,01}.

Every later map preserves the upper bound on image size. Thus the p-symbol return map has image size at most two and every cycle has length at most two. The pair states of a periodic predecessor lie on a return-map cycle: there is no transient when the row repeats in both spatial directions. If the cycle length is k, the reconstructed bits have period dividing k*p. Combining k<=2 with p dividing q gives

    q=p or q=2*p.

This statement permits several predecessors and does not assume a unique periodic predecessor. The cut is just a phase choice, not a restriction on the row.

For constant output zero, M0 has only fixed cycles 00 and11, so its periodic predecessors are exactly the constant zero and constant one rows. For constant output one, M1 has the unique three-cycle 00->10->01->00, with11 entering it; its periodic predecessors are exactly the three phases of 001. Their least spatial period is 3. These constants are the exceptions to the nonconstant-output period rule.

**Classification.** Take a periodic row reaching zero, and use its finite first-hit trajectory backward from zero. If it is already zero or is the one row, its least period is 1. Otherwise the step before one has period 3. Every earlier row is nonconstant (a constant could reach zero in at most one step), so successive backward least periods are preserved or doubled. The original least period is therefore 3*2^k for some integer k>=0.

**Existence at every allowed period.** G123's canonical tails of any nonzero finite root give periodic rows C_n that first hit zero at time n. Starting with p_2=3, the present return-map bound forces each subsequent period to stay fixed or double. G123 proves these periods unbounded. Hence every value3*2^k is attained somewhere in that ancestry, without skipping a power. Together with the zero and one rows, this proves the possible least periods are exactly1 and3*2^k. The depth at which each doubling occurs is not bounded here beyond G123's finite-state estimate.

**Independent local check and unexpected guard, by hand.** The cyclic words give the exact forward trajectory

    001010 -> 011011 -> 010010 -> 111111 -> 000000.

Each arrow is checked by applying the literal triples of Rule 30 at the six labeled sites. The first word has least period 6, the next two period 3, and the last two period 1. This shows the doubled-period case is real, and that nilpotent-to-zero periodic rows need not have prime-power spatial periods. Separately,001->111 refutes applying q<=2*p to the constant-one output. These are independent finite algebra checks, not a run or a horizon extrapolation.

**Scope and prior art.** Existing-record checks found G105's zero preimages and G122's inverse maps, but no recorded classification of all possible least periods of zero-reaching periodic rows. Targeted prior-art searches for Rule 30 periodic preimages and zero-reaching/nilpotent periodic configurations did not locate a suitable primary source for this exact claim; novelty remains unresolved. The proof above is self-contained. Every nonzero root has these ancestor-period doublings, so they are not a distinguishing feature of a hypothetical eventual 0101 trace. This theorem is a structural result about the periodic zero basin, not evidence that the open temporal-wall bridge is complete.

### G125. Sideways periodic points correspond exactly to recurrent Rule 30 ring states (2026-10-06)

**Status:** symbolic correspondence using G22; reviewed by Local L079. Distinct lane: CONSTELLATION row 5, sideways dynamics. No computation or new ring census. The ordinary finite-state orbit argument is standard; no novelty claim.

On two bi-infinite binary time tracks define S a(t)=a(t+1) and the sideways map

    H(a,b)=(S a XOR(a OR b),a).

This is G22's map F, renamed H here to distinguish it from ordinary forward-time Rule 30, R. Fix m>=1. Then Fix(H^m) is in bijection with the recurrent states of R on a labeled m-cell ring. A recurrent state means a row lying on a temporal cycle, not a transient that will eventually enter one. Every track pair in Fix(H^m) is temporally periodic, with a common period no larger than 2^m-1. The same correspondence applies to periodic points of G22's induced ternary map.

**From a sideways periodic point to a ring.** Successive H iterates give neighboring columns extending leftward: H(a,b)=(c,a) is exactly the inverse-column equation c(t)=a(t+1) XOR(a(t) OR b(t)). If H^m(a,b)=(a,b), these columns close into a spatial period-m spacetime diagram. At each integer time t its labeled ring row u_t satisfies R(u_t)=u_(t+1), for all positive and negative t. Thus it is a bi-infinite orbit of a finite deterministic map.

Every row of such a bi-infinite finite-state orbit is recurrent. There is a uniform maximum transient length among the finitely many ring states. If u_0 were transient, u_(-N) would have to remain transient for at least N steps before reaching u_0, which is impossible for larger N. Recurrent ring states lie on cycles, and on that recurrent set R is a permutation. Therefore the temporal history is periodic in both directions and uniquely determined by u_0. There are at most 2^m-1 recurrent states:the all-one ring row maps to zero and is not itself recurrent. This gives the stated common temporal-period bound, not necessarily the least period of either individual track.

**From a recurrent ring state to a sideways periodic point.** A recurrent row has a unique bi-infinite temporal orbit on its cycle. Periodically extend each ring row to the whole spatial line and take the time tracks at sites 0 and 1 as (a,b). All inverse-column equations hold, so applying H m times shifts left by one spatial circumference and recovers (a,b). The two constructions are inverse:two adjacent tracks and their inverse-column iterates recover the labeled ring row, while a recurrent ring row determines its entire past and future. Labels and the distinguished time 0 are retained;this is a bijection with states, not merely with cycles modulo time or spatial rotation. Periods dividing m are allowed.

**Ternary scope.** Every H-periodic point lies in H's one-step image, since it is the image of H^(m-1) of itself. G22's conjugacy on that image therefore transfers this exact periodic-point description to the ternary induced dynamics. It does not transfer arbitrary transient two-track states into the ternary domain, nor assert a dynamical-entropy formula or classify all iterated images.

**Independent hand check and unexpected transient guard.** On a two-cell Rule 30 ring the four rows obey00->00,11->00,01->01,10->10. Hence there are exactly three recurrent states. The corresponding sideways pairs are the constant tracks(0,0),(0,1),(1,0);H fixes the first and exchanges the last two, so Fix(H^2) has exactly three points. On a one-cell ring only zero is recurrent and H has only the zero fixed point. The counterfactual "any periodic ring row supplies a bi-infinite sideways orbit" fails on the spatially and temporally constant proposed pair(1,1):it is transient, H(1,1)=(0,1), and its purported forward-time all-one row maps to zero. Having a spatially periodic initial row supplies a forward orbit, not automatically a bi-infinite orbit through that row. These are literal truth-table checks, not a simulation extrapolation.

**Result for the open lane.** Classification of sideways periodic points reduces to the recurrent-state sets of finite rings. No nonperiodic time track can lie on a finite sideways cycle. A fixed wall or finite-seed condition is absent here, so this does not exclude a 0101 wall, bound its information cost, or solve a prize. Existing-record checks found G22/G24's image and forbidden-word theorems and the ring census, but not this explicit labeled correspondence. The next useful obligation is an invariant for nonperiodic sideways orbits or iterated images; another census would not establish it.

### G126. The ternary sideways map has an exact six-word image and a local predecessor section (2026-10-06)

**Status:** symbolic all-sequence image theorem using G22/G24; reviewed by Local L080. No experiment or production run. Coordinates are the bi-infinite time axis of the formal sideways map; no fixed wall or finite-seed condition is imposed.

Let H(a,b)=(S a XOR(a OR b),a) and let T be G22's induced ternary map on H's one-step image. Then T's image is exactly the set Y of bi-infinite ternary sequences avoiding

    100, 101, 112, 0210, 0211, 0202.

Thus the image is a shift of finite type, not merely a language with the two necessary exclusions of G24. There is a shift-commuting local map R from Y to the full ternary shift with T(R(z))=z. It uses only z(t-1),z(t),z(t+1). In particular every p-periodic target in Y has a p-periodic predecessor (its least period may divide p). This is not a claim that R(z) lies in Y or that T is onto its own image.

**Reduction to binary predecessor constraints.** Decode a target z as (D,C), where C(t)=[z(t)=2], and D(t)=z(t) when C(t)=0, otherwise D(t)=1-C(t+1). A ternary predecessor is represented by a compatible pair(C,A). Its image must satisfy

    D(t)=C(t+1) XOR(C(t) OR A(t)).

When C(t)=0 this forces A(t)=e(t)=D(t) XOR C(t+1). When C(t)=1 the target equation is automatic and A(t) is free. G22's image compatibility for(C,A) requires, at every site with A(t)=1,

    C(t)=1-A(t+1).

Hence a forced 1 at a zero site of C requires the next A bit to be 1; a chosen 1 at a one site of C requires the next A bit to be 0.

**Necessity of the six exclusions.** Two consecutive zero sites of C cannot have e(t)=1,e(t+1)=0. In target symbols this is exactly100 or101 when C(t+2)=0, and112 when C(t+2)=1. Also a zero-one-zero block of C with e(t)=1 forces A(t+1)=1 and then A(t+2)=0. Its first target symbol is0, its middle symbol2, and its final forced e(t+2) must be0. The three ways to violate this last condition are0210,0211,0202. Each exclusion therefore holds for arbitrary predecessors, periodic or not.

**Sufficiency and local section.** For any target avoiding these words, define

    A(t)=D(t) XOR C(t+1)                    if C(t)=0,
    A(t)=[z(t-1)=0]                       if C(t)=1.

All target equations hold. Check compatibility only where A(t)=1. If C(t)=0 and C(t+1)=0, the forbidden triples ensure the next forced bit is1. If C(t)=0 and C(t+1)=1, the equation e(t)=1 means z(t)=0, so the prescribed next bit is1. If C(t)=1, its chosen bit is1 only after target symbol0. When C(t+1)=1 the next chosen bit is0 because its preceding symbol is2. When C(t+1)=0, avoidance of the forbidden quadruples makes its forced bit0. These exhaust the cases and prove compatibility. Encode(C,A) as R(z)(t)=2 when A(t)=1, otherwise C(t). G22's recoding then gives T(R(z))=z. This construction is valid on the whole bi-infinite sequence; no boundary completion or compactness assumption is hidden in it.

**Independent hand certificate and unexpected gap check.** For the repeating target0220, the formulas give C=0110,D=0010,A=1100 and predecessor code2210. A further binary predecessor B=0011 satisfies, by direct XOR/OR evaluation,

    H(1100,0011)=(0110,1100),
    H(0110,1100)=(0010,0110).

The last pair codes0220, independently certifying a target in the second image. Conversely the repeating target112 avoids100 and101, but forces A(t)=1,A(t+1)=0 at two successive zero sites of C. It has no predecessor under T. This refutes the counterfactual that G24's two old exclusions already describe the image exactly. These are finite algebra checks supporting the case proof, not a computational extrapolation.

**The image still has positive shift entropy.** Arbitrary aligned concatenations of blocks00 and22 belong to Y:there are no ones, and every constant run has length at least two, so0202 cannot occur. Distinct binary choices of n blocks give 2^n distinct words of length2n. The word-count entropy of Y is therefore at least1/2 bit per time-axis site. No exact entropy or limit-set entropy is evaluated. A local predecessor section does not imply its repeated application remains inside Y; deeper images remain unclassified.

**Record and scope.** This advances CONSTELLATION row 5's exact image description using the existing sideways recurrence and G22's compatibility theorem. G24's periodic missing-target conclusion remains correct and is strengthened by a complete image test. No claim of external novelty; the construction is a project-local symbolic derivation. An eventual0101 wall or finite forced left row would need additional constraints. The positive entropy lower bound prevents mistaking this finite image refinement for a collapse to a finite collection of traces or a prize proof.

### G127. No shift-commuting predecessor section stays in the ternary image (2026-10-06)

**Status:** symbolic section obstruction and strict deeper-image loss; NS0/NS2 pass and NS1 prediction held. Uses G126's image theorem; independent review pending. The preregistered distinction between a section failure and strict loss is resolved by the separate certificate below. Further image layers remain open.

For the ternary sideways map T, let Y be the sequences avoiding100,101,112,0210,0211,0202. The period-two points of Y are exactly the repeating words00,11,12,21,22. Literal evaluation of G22's rule gives

    00 -> 00,
    11 -> 22,
    22 -> 11,
    12 -> 22,
    21 -> 22.

Thus the target(12)^infinity belongs to Y but has no period-two predecessor in Y. Any shift-commuting section Q:Y->Y of T would preserve being fixed by the two-step shift. Its value at this target would be such a predecessor, a contradiction. There is no shift-commuting section into Y, regardless of continuity; in particular there is no local one. G126's section into the full ternary shift is unaffected.

**Unexpected guard: a deeper predecessor nevertheless exists.** The repeating word0102 lies in Y and T(0102)=1212. It is a period-four predecessor of the period-two target. G126's canonical section instead returns(01)^infinity, outside Y. Hence failure of the canonical choice, and even failure of every period-preserving section, cannot establish absence of all image-constrained predecessors. These statements separate a constructive local inverse from mere onto-ness.

**NS0-NS2 preregistration.** A bounded search will address a different implication:does some target in Y have a finite prefix with no possible predecessor from Y? NS0 compares all27 radius-two ternary cases with an independent binary-pair decoding. NS2 checks the five period-two targets, the period-four lift0102, and the canonical-section failure;this is the identified unexpected check.

NS1 considers prefix lengths n=1..7, in increasing order. Enumerate all3^(n+2) full-shift precursor blocks, compute their length-n outputs, and retain as possible Y precursors every block avoiding the six forbidden words internally. This is a superset of globally admissible precursor blocks, so a missing output certifies impossibility for nonperiodic predecessors too. Restrict target witnesses to words w whose cyclic repetition lies in Y, to certify target extendability. Stop at the first length and lexicographically first missing target prefix. Blind prediction:a witness occurs by length7. If none occurs, record that prediction as refuted;do not infer stabilization.

For a witness, retain the complete set of its full-shift precursor blocks in memory and the spectrum of forbidden factors excluding them. Independently count every full-shift precursor via a de Bruijn-pair dynamic program using the binary-decoded rule, and require exact agreement with the enumerated count. No sampling or floating arithmetic. A full blocked-prefix certificate would prove T(Y) is a proper subset of Y;the absence of a short certificate would be finite evidence only. Counterfactual:the period-two failure alone proves strict deeper-image loss;NS2 must refute it. Publish the predictions and instrument before execution. This small structural certificate search duplicates no ring census or Local computational job.

**NS0-NS2 outcome (2026-10-06 22:20 BST).** Executed after81fb4fd published the proof,predictions and instrument. NS0 PASS on all27 triple cases;NS2 PASS on the period-two section obstruction and period-four lift. NS1 HELD at n=6,so the blind witness-by7 prediction held. The search checked9,828 full-shift precursor blocks across n=1..6. The first missing periodic target prefix is022000. All six full-shift precursor blocks are

    22100000, 22100001, 22100002,
    22100022, 22100220, 22100221.

Each contains100. The independently decoded de Bruijn path count is also6. No floating arithmetic or sampling. Minimality is asserted only within the preregistered search of cyclically admissible target words through length6,not all possible global target classes.

**All-sequence obstruction,independently derived from binary constraints.** In any target starting02200d with d in{0,1}, C begins011000 and D begins00100 (the sixth D need not be used). The predecessor constraints force A(0)=1 because D(0)=0,C(1)=1. Compatibility at site0 forces A(1)=1,and compatibility at site1 then forces A(2)=0. The target equations at sites3 and4 force A(3)=A(4)=0. Encoding(C,A) forces precursor prefix22100,which contains100. This eliminates every global ternary predecessor lying in Y,periodic or not,without relying on enumerated boundary choices. Thus T(Y) forbids022000 and022001 in addition to Y's old exclusions.

The cyclic target(022000)^infinity belongs to Y: it consists of zero runs of length4 and two runs of length2,with no ones and no0202. Hence it has a full-shift predecessor by G126,but no predecessor from Y. Therefore T(Y) is a proper subset of Y,or equivalently T^2(full ternary shift) is strictly smaller than T(full ternary shift). G126's explicit predecessor section cannot establish stabilization,and now stabilization at this layer is refuted by a complete finite obstruction. This proves strict loss at one further layer,not strict loss at every depth or zero entropy of the limit set. Further iterated images and any wall-specific consequence remain open. Independent review pending.

### G128. The sideways limit set has every binary temporal trace as a factor (2026-10-06)

**Status:** all-depth compactness proof using G4.4/G22; independently verified by Local L081. No experiment or probability extrapolation. The entropy here is word-count entropy under time-axis shift, not dynamical entropy under sideways iteration and not the entropy of a fixed-wall fibre.

Let X be all pairs of bi-infinite binary time tracks, H(a,b)=(S a XOR(a OR b),a), and

    Lambda_H = intersection_(n>=0) H^n(X).

Let Lambda_T be the corresponding limit set of G22's ternary map. Then Lambda_H is exactly the set of adjacent-column pairs occurring in full Rule 30 spacetime diagrams on integer space and integer time. Projection onto either track is onto the full binary shift. Under G22's ternary recoding, the one-block map pi(z)(t)=[z(t)=2] maps Lambda_T onto the full binary shift. Consequently every ternary iterated image and the limit set itself have word-count entropy at least1 bit per time-axis site. Lambda_T contains nonperiodic time-axis sequences. No fixed finite initial seed is asserted to realize them.

**Spacetime equivalence.** A full spacetime diagram supplies predecessors of an adjacent pair at every sideways depth: shifting to two columns farther right and applying H recovers the chosen pair. Hence that pair lies in every H^n(X).

Conversely, membership in H^n(X) supplies a right extension of n columns satisfying the inverse-column equations at every time. All left columns are determined by forward H iterates. For each n there is therefore a spacetime strip extending arbitrarily far left and n columns right. Fill its remaining sites arbitrarily. The full diagram space {0,1}^{Z x Z} is compact. A convergent subsequence, or the equivalent finite-intersection argument, preserves the given two columns and every local rule equation:each finite spatial region is covered once n is large enough. The resulting diagram obeys Rule 30 at every integer space-time site. No coherent choice of predecessors at successive finite depths was assumed.

**Every binary trace is realizable in this unrestricted class.** Fix any desired bi-infinite binary column b(t). For each N, prescribe b on times-N through N. Start a row at time-N. Iterated left-permutivity gives the sample after k ticks as its initial bit at site-k XOR a function of higher initial bits. Fix the initial positive-index bits and solve successively for sites0,-1,...,-2N, as in G4.4. This realizes the desired finite window;all other initial bits may be zero. Evolve forward on the whole spatial line, and fill times earlier than-N arbitrarily.

Compactness now gives a full spacetime diagram whose source column is b(t) at every integer time:each prescribed value and each local rule equation is eventually enforced in these diagrams. The finite-window seeds may differ with N and grow in width. Their compact limit need not have finite spatial support at any chosen time. Spatial translation makes the same argument apply to either track of an adjacent pair. Thus both projections of Lambda_H are onto the full binary shift.

**Ternary factor and entropy bound.** H's one-step image I is invariant under H, and G22 conjugates H restricted to I with T. The nested images starting from I have the same intersection as those starting from X, because H^n(I)=H^(n+1)(X). Therefore the conjugacy maps Lambda_H onto Lambda_T. In the recoding, the second binary track is exactly[z(t)=2], so its surjectivity is a one-block factor statement. Every length-N binary word is the pi-image of a length-N ternary word in Lambda_T;distinct binary words require distinct ternary words. There are at least2^N such words, proving the entropy lower bound. Every finite iterate contains Lambda_T and inherits it. If b is nonperiodic, any preimage under pi is nonperiodic, proving nonperiodic sequences exist in the limit set. This says nothing about recurrence or periodicity under T itself.

**Unexpected fixed-wall guard, checked algebraically.** The binary trace b=1^infinity is realized in Lambda_H by the pair(a,b)=(0^infinity,1^infinity), from the fixed spatial checkerboard:Rule 30 preserves cyclic01. But the pair(a,b)=((01)^infinity,1^infinity) is not even in H(X). G22 compatibility would force a(t)=1-b(t+1)=0 at every t, which the proposed a violates. Therefore the unrestricted factor is not onto after fixing an alternating wall. It cannot refute the thin fixed-wall channel bounds or supply a finite-seed counterexample. This is the identified unexpected check.

**Implication for the active route.** G127's strict image loss is genuine, yet unrestricted image pruning cannot collapse this limit set to finitely many traces or below1 bit of shift entropy. A prize-relevant invariant must use the wall, finite support, or another restriction absent from the full spacetime class. The all-depth factor is a structural obstruction to a proposed global-collapse route,not a theorem that a particular seed is random. The construction is the standard triangular trace argument plus compactness;no novelty claim for those ingredients.


### G128.1. Known period-two closure obstruction and the missing implication (2026-10-06)

**Purpose and prior art.** Audit whether an alternating wall can be closed by giving all columns its temporal period. This is a known obstruction, not a new prize lead: Wolfram, [A New Kind of Science, notes to page 267, printed page 954](https://files.wolframcdn.com/pub/www.wolframscience.com/nks/nks-ch6.pdf#page=83), reports three Rule 30 configurations with temporal period dividing two, the same count as for period one. The following exact graph explains that count without another census.

Encode the temporal words 00, 01, 10, 11 as 0, 1, 2, 3 respectively. The sideways map H(a,b)=(S a XOR (a OR b),a) acts on these sixteen ordered pairs as follows. This table is a hand substitution into the rule, not an experimental result.

| a / b | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| 0 | (0,0) | (1,0) | (2,0) | (3,0) |
| 1 | (3,1) | (3,1) | (1,1) | (1,1) |
| 2 | (3,2) | (2,2) | (3,2) | (2,2) |
| 3 | (0,3) | (0,3) | (0,3) | (0,3) |

The only recurrent states are (0,0) and the cycle (0,3),(3,0); every other state enters that set within three steps. A full diagram periodic in time with period dividing two supplies a bi-infinite spatial orbit of this finite graph. Every state in such an orbit is recurrent: arbitrarily long predecessor paths in a finite deterministic graph must contain a cycle, which cannot exit to a transient state. Therefore the only whole-row configurations are all zero and the two spatial checkerboards. All three are stationary in time.

**The companion test is already covered by G27.2.** If a is alternating and b also has eventual temporal period dividing two, start after their common settling time. G22's compatibility b(t)=1 implies a(t)=1-b(t+1). It permits only b=00 or b=a. In either case one H step forces the immediate left column to be constantly one, and subsequent steps force the stationary checkerboard left tail. This is incompatible with an initially eventually-zero left row. G27.2 already excludes any eventual periodic adjacent companion under that finite-left assumption; the sixteen-state audit recovers a special case rather than improving it.

**Unexpected scope check and stopping decision.** G128 nevertheless realizes an alternating single column in some unrestricted full spacetime diagram. Thus that column does not license a globally period-two diagram or a period-two companion. Spatial checkerboards having period two does not make their temporal period two. This is the identified independent scope check. No numerical experiment was needed. The attempted period-two closure shortcut is closed; extending periodic graph censuses would not address the aperiodic companions required by G27.2. The next useful obligation remains a wall-sensitive restriction that applies to those companions without assuming the periodicity to be proved.


### G129. The finite-left wall fibre is a compact constraint class at each fixed radius (2026-10-06)

**Status and target.** Symbolic bridge from G128 to the finite-left boundary problem; independently verified by Local L083. No experiment or novelty claim for compactness. Existing record: G27.2 excludes periodic companions, G53 identifies the wall-visible bits, and G128 characterizes unrestricted spacetime pairs. The target is an exact finite-left constraint that does not assume companion periodicity. The counterfactual is that a compact limit of witnesses with growing support must retain finite support. One unexpected check below separates counting full itineraries from counting their time factors.

Use one-sided time t>=0. Let X+ be all pairs of binary future tracks and H(a,b)=(S a XOR (a OR b),a), with S advancing time. Let Lambda+ be the intersection of H^n(X+) over n>=0. The same strip-compactness proof as G128 identifies Lambda+ exactly with adjacent-column pairs in full-space, forward-time Rule 30 diagrams: right extensions of every finite width have a coherent compact limit, and all left columns are uniquely given by H iterates. This does not require any periodicity or a past before time zero.

Fix any prescribed wall tau and integer L>=0. Define

    B(L,tau) = { (a,b) in Lambda+ : a=tau,
                 first_track(H^d(a,b))(0)=0 for every d>L }.

**Exact boundary interpretation.** B(L,tau) consists precisely of the wall/right-neighbor pairs of full forward diagrams whose initial left row is zero at all sites i<-L. There is no bound on the initial right row. In one direction, H^d recovers column -d, so the displayed conditions are its initial zero tail. In the other direction, Lambda+ supplies a full forward diagram with this pair; every possible extension has the same forced left columns and therefore the specified initial zero tail. This is a left-support condition, not a finite global seed condition.

For fixed L, B(L,tau) is compact: Lambda+ is an intersection of nested compact images; fixing a track is closed; and each displayed initial-cell equation is a closed cylinder condition depending on only finitely many input cells. Their countable intersection is closed. All finite-left pairs form the union of these classes over L. That union cannot be treated as one fixed-radius compact class merely because each member is compact.

**Finite-box alternative.** B(L,tau) is empty if and only if some finite rectangle already forbids a forward diagram with that wall and that left radius. Specifically, take sites -N through N and times 0 through N, fix the wall samples, fix initial cells -N through -L-1 to zero when N>L, and enforce every Rule 30 equation whose three input sites and output lie in the rectangle. Leave the right initial row unrestricted. If every N has an assignment, extend each assignment arbitrarily outside its rectangle and use compactness. Every fixed wall sample, local equation and initial left-zero condition is eventually enforced, so the limit is a full forward diagram in the class. The converse follows by restriction. Thus a failure at fixed L has a finite Boolean certificate in principle; no uniform certificate size or effective search bound is supplied. Certificates for a few radii do not prove emptiness for every radius.

**Visible itineraries have a finite cardinality bound at fixed L.** Observe b only at white wall times. There are at most 2^L such complete visible itineraries in B(L,tau). Choose the L initial left bits. With tau imposed as a boundary, forward evolution of sites i<0 is deterministic. Write its nearest-left trace as ell(t). At a white time, the wall equation forces b(t)=tau(t+1) XOR ell(t). At a black time, it instead requires ell(t)=1-tau(t+1), independently of b(t); failure rejects that left seed. Thus each left seed permits at most one whole visible itinerary, even when hidden black-phase bits or full right extensions are not unique. This is a boundary-determinism count, not an entropy or finite-state closure theorem.

**Counterfactual and unexpected check.** Initial rows with ones at -L,...,-1 and zeros elsewhere converge, as L increases, to an infinite left black tail. Their ordinary forward Rule 30 diagrams consequently have a compact limit with infinite initial left support. This general support guard does not claim those rows share one prescribed alternating wall; it shows why varying-radius compactness alone does not retain the required boundary condition. Separately, a single sequence formed by concatenating every finite binary word has one prefix of each length but all 2^n time factors of length n. Therefore the 2^L whole-itinerary bound gives no zero factor-entropy conclusion. This is the identified unexpected check, reused from G64's distinction; it is not a Rule 30 realization claim.

**Remaining bridge.** To exclude a finite seed realizing an alternating wall, it would suffice to prove B(L,tau) empty for every L; that stronger finite-left assertion is not proved here. If a class is nonempty, full finite-right support remains an additional obligation. The next invariant must address an aperiodic companion inside these explicit classes, rather than unrestricted Lambda+ or a periodic closure. No new channel census is requested.


### G130. Fixing the initial right tail gives a unique left seed for every wall trace (2026-10-06)

**Status and purpose.** Exact coordinate reduction of G4.4's triangular inversion; independently verified by Local L084. This is not a new left-permutivity theorem or a solution of the wall problem. G129 leaves finite right support as an additional constraint. Here the target is to identify exactly what that constraint can and cannot exclude. No experiment. Counterfactual: finite initial right support alone restricts possible temporal walls, or exact finite-prefix realizations guarantee a finite left seed. The delayed single-cell example below independently rejects the latter implication at a fixed right tail.

Fix the initial values r_i at all sites i>=0. For any desired one-sided wall tau with tau(0)=r_0, there is exactly one initial left word u=(x_-1,x_-2,...) whose full forward Rule 30 evolution has x_0(t)=tau(t) for every t>=0. The map from u to the future trace (tau(1),tau(2),...) is a homeomorphism of binary sequence spaces. No periodicity premise is used.

**Proof.** G4.4 gives, for each n>=1,

    x_0(n) = x_-n(0) XOR P_n(x_(-n+1)(0),...,x_n(0)).

The unique path carrying the leftmost input to the observed output contributes by XOR; all other terms use higher initial indices. Fix r and solve x_-1, then x_-2, and so on, using the prescribed tau(n). Each step has exactly one solution and does not alter earlier samples. These compatible finite assignments define one infinite initial row, and its ordinary forward evolution realizes every sample. Uniqueness follows from the same successive solving. Both directions are continuous: a trace prefix of length N uses only the first N left bits and r_0,...,r_N; conversely those N left bits are determined by that trace prefix and the same finite right data. This is an initial-row/trace coordinate map, not a conjugacy between Rule 30 evolution and a shift on a fixed-tail space, since the initial right tail need not remain fixed after an update.

**Finite-right support is compatible with every wall in isolation.** Set r_0=tau(0) and r_i=0 for all i>0. The construction realizes every tau, including an alternating wall, with this finite initial right tail. Its forced left word may be infinite. Thus no obstruction based only on requiring finite initial right support can exclude a temporal word when arbitrary infinite left support is allowed. This does not assert that a chosen companion from G129 has a finite-right extension.

**Exact finite-global criterion.** For a prescribed tau, let r range over all eventually-zero initial right tails with r_0=tau(0), and write u_r for the uniquely solved left word. A finite global seed realizes tau if and only if at least one u_r is eventually zero. Necessity applies uniqueness to that seed's right tail; sufficiency joins the two finite tails and invokes the construction. Hence the joint boundary problem is a zero-tail question for this canonical family, rather than existence of an unrestricted right extension. This supplies no uniform zero-tail test, search bound, or exclusion theorem. The finite-left condition of G129 still has to hold for the same row.

**Unexpected fixed-tail finite-prefix guard, exact.** Take the initial row x_i=1 for i<0 and x_i=0 for i>=0. Rule 30 sends it in one tick to the single black cell at site 0: triples 111 and 110 give zero on the left, triple 100 gives one at the wall, and triples 000 give zero on the right. Let tau be this row's wall trace: its first sample is zero and its later samples are the single-cell wall trace shifted by one tick. With the fixed initial right tail all zero, this tau has the unique left seed 111..., so no finite left seed with that same right tail realizes it forever.

For every N>=1, truncating that left seed to ones at -N,...,-1 yields a finite seed with the same right tail and exactly the same wall through time N. Its first wrong wall sample is at time N+1: the higher initial indices agree, while the fresh XOR pivot x_(-N-1)(0) differs. Thus arbitrary finite horizons are realized with growing left support even though no fixed finite left seed works for that fixed right tail. No claim is made about alternative right tails for this tau, or about periodicity of the single-cell trace. The check uses both the explicit one-tick truth table and the independent triangular uniqueness mechanism.

**Next obligation.** For an alternating or eventually alternating prescribed wall, prove a property of u_r uniform over finite r that prevents an eventual zero tail, or identify a counterexample. Periodic companion assumptions, unrestricted trace existence and growing finite-prefix realizations do not supply that property. This is a reformulation of the missing proof, not a claim that the canonical words have been classified.


### G131. The Sturmian exclusion survives every finite block factor (2026-10-06)

**Status and purpose.** Symbolic extension of RULE30-PRIZE.md section 8.57's Theorem E; independently verified by Local L085. No experiment. The target is the open rotation-code lead in PERIOD-TWO.md question 7, without assuming a periodic companion. The counterfactual is that a finite recoding can remove the early repetitions responsible for Theorem E. The proof retains the exact fixed margin. Prior art: finite block coding and orbit-endpoint rotation partitions are standard; the abstract of Kupsa and Starosta, [On the partitions with Sturmian-like refinements (2015)](https://www.aimsciences.org/article/doi/10.3934/dcds.2015.35.3483), discusses this class and stronger refinement results. Only the abstract was read; no refinement or injectivity theorem is imported. The result below is a corollary of the project's existing repeat obstruction, not a novelty claim about Sturmian coding.

**Theorem.** Let g be any irrational Sturmian sequence, with any phase. Let F be any binary function of a fixed block of width w+1, and set c_s=F(g_s,...,g_(s+w)) for s>=0. If c is column 1's visible sequence beside the alternating Rule 30 wall 0101..., the forced initial left row cannot be eventually zero. No injectivity, nonconstancy or aperiodicity premise is imposed on F.

**Proof.** Section 8.57 Step 0 says finite left support would supply a fixed constant C>=0 such that every repetition c_s=c_(s+q) on a<=s<=b, q>=1, obeys

    b <= 2a+q+C.                         (repeat bound)

Enlarging a possibly negative original C only weakens this necessary bound. Suppose g_s=g_(s+q) on a<=s<=e. If e>=a+w, then c repeats on a<=s<=e-w, so e<=2a+q+C+w. If e<a+w, the same inequality holds automatically. Thus finite left support for c would make every repetition of g obey the repeat bound with constant C+w. The continued-fraction argument in section 8.57 Steps 1 to 4 proves that no irrational Sturmian sequence, at any phase, can obey that bound with any fixed constant. Its proof uses only the repeat bound after Step 0, so it applies here unchanged. This contradiction proves the theorem. The margin is w, not a scale-dependent loss.

A finite block function using shifts m,...,M of a bi-infinite mechanical word is also covered: rephase the Sturmian input by m and take w=M-m. Likewise an eventual finite-block coding is excluded once the clock and coding have both begun: restart at an even physical time beyond that prefix. Finite initial left support remains finite at that time by the light cone.

**Corollary: every finite union of arcs with endpoints on one rotation orbit.** Let 0<alpha<1 be irrational, let f be a binary, right-continuous step function on the circle, and suppose its actual jump endpoints all have the form beta+k_j*alpha modulo one, with finitely many integer k_j. Then c_s=f(theta+s*alpha) is excluded beside 0101... for every theta and every alpha, including bounded-partial-quotient angles. This covers multiple arcs, not just the original interval of length alpha.

Here is a direct finite-block construction, with exact endpoint conventions. Put y=x-beta and g(y)=1 on [1-alpha,1), zero elsewhere. A binary circular step function has an even number of jump endpoints. Over GF(2), form the Laurent polynomial

    Q(z)=sum_j z^(k_j)=(1+z)*P(z).

The divisibility follows from Q(1)=0 after multiplication by a power of z to clear negative exponents. For each nonzero coefficient P_k define

    h(y)= XOR_k g(y-(k+1)*alpha).

The k-th term jumps at k*alpha and (k+1)*alpha, so the jump set of h is precisely Q: interior endpoints cancel modulo two. Thus f(beta+y) and h(y) have the same jumps and differ by one constant bit. Right-continuity makes the equality hold at the endpoints as well. Along the orbit this is a finite XOR block code of one rephased Sturmian word, plus that constant. The theorem therefore applies. A constant f is the empty-code case and is covered too.

**Unexpected degeneracy check.** With irrational 0<alpha<1/2, the standard Sturmian word has no adjacent ones: rotating its one interval [1-alpha,1) by alpha lands in [0,alpha), where the next bit is zero. Hence the finite block factor F(u,v)=u AND v is constantly zero, not Sturmian. The proof still excludes it, directly through the repeat bound. Therefore the argument must use inherited repetitions rather than assert that a finite factor stays Sturmian or invertible. This is the identified independent check.

**Scope and lead status.** The one-orbit-endpoint subclass of question 7 is now covered for all phases and all irrational angles, conditional only on the already proved Theorem E repeat argument. Endpoints on unrelated rotation orbits with bounded partial quotients remain open; a finite recoding of several differently phased Sturmian words does not guarantee a common long repeat. Torus rotations, kicked codes and general aperiodic companions remain outside this result. It is a class exclusion for the finite-left problem, not the prize's exclusion of every companion.


### G132. Circle-covering codes and one-character torus observables are excluded (2026-10-06)

**Status and target.** Corollary of G131 and G27.2; independently verified with G131 by Local L086. No experiment or novelty claim for integer characters. Target: clarify which multi-orbit and torus codes the finite-block argument already excludes. Counterfactual: a circle covering or additional unobserved torus coordinates automatically evade the Sturmian obstruction. A genuine two-coordinate box below is the unexpected scope check.

**Statement.** Let the torus orbit be x_s=theta+s*omega modulo one in each of d coordinates. Fix an integer vector v and the circle projection

    h_v(x)=sum_j v_j*x_j modulo one,
    beta=h_v(omega).

Observe c_s=psi(h_v(x_s)). If beta is rational, every such deterministic observable psi gives a periodic c and is excluded beside the alternating Rule 30 wall with finite initial left support. If beta is irrational, the same exclusion holds whenever psi is a binary finite-union-of-arcs code whose jump endpoints lie on one beta-rotation orbit. Arbitrary fixed choices at the endpoints are allowed. In both cases no assumption is made about periodicity of the actual right-neighbor trace at its hidden phases.

**Proof.** Integer coefficients make h_v well-defined on the torus. Direct addition gives

    h_v(x_s)=h_v(theta)+s*beta modulo one.

For rational beta with denominator q these projected points repeat every q samples, hence c is periodic. The corresponding nearest-left trace is periodic: at even physical times it is 1-c_s, and at odd times it is one. G27.2 excludes this pair for finite initial left support, independently of the right half.

For irrational beta, the projected observable is exactly a circle rotation code of the class in G131, so its finite-block exclusion applies for every starting phase. If endpoint values differ from the half-open convention used there, each endpoint is visited at most once: two visits would make a nonzero multiple of beta integral. There are finitely many endpoints, so the code eventually agrees with the half-open code. G131's eventual-factor clause therefore preserves the exclusion. This also explains why endpoint exceptions do not create a new companion class.

**Circle coverings give a concrete multi-orbit case.** In dimension one take v=2, irrational alpha as omega, and beta=2*alpha modulo one. Let psi be the standard Sturmian interval [1-beta,1). Then f(x)=psi(2*x modulo one) is a two-arc observable for the original alpha rotation. Its endpoint set is

    {0, 1/2, -alpha, 1/2-alpha} modulo one.

The two original alpha-orbit classes represented by 0 and 1/2 are distinct: an equality 1/2=k*alpha modulo one would make alpha rational for nonzero integer k. Thus f does not have all endpoints on one original orbit, yet its sampled code is Sturmian for the projected angle beta and is excluded. More generally any integer circle covering can be used. This narrows part of the unrelated-endpoint lead; it does not exclude arbitrary unrelated endpoints without such a quotient structure.

**Unexpected genuinely multidimensional guard.** On the two-torus, let f(x,y)=1 when both x and y lie in [0,1/2), zero otherwise. This observable cannot be a function of any single integer character h_(a,b). A function of that character would be invariant under every translation (b*t,-a*t), since the character changes by zero. If b is nonzero, choose x just below 1/2 and y=1/4; a sufficiently small such translation crosses the x boundary while keeping y interior, so f changes. If b=0 and a is nonzero, a vertical translation changes f while leaving the character fixed. The zero character would require f constant. All cases contradict factorization. Therefore this corollary makes no claim about genuinely two-coordinate box codes, nor about the general torus lead. This is a geometric scope check, not a Rule 30 counterexample or a claim that a box code supplies a finite witness.

**Resulting boundary.** The class exclusion includes finite recodings after a one-circle projection, even when the original partition has multiple orbit classes or the underlying motion has several torus coordinates. General partitions using independent coordinates, arbitrary unrelated circle endpoints and kicked observables remain open. No uniform finite-left exclusion or prize solution follows.


### G133. Golden-angle codes cannot be rescued by super-geometrically separated kicks (2026-10-06)

**Status and target.** Quantitative extraction from Theorem E's existing continued-fraction proof; independently verified by Local L087 (finite visit deadlines, scale inequalities and S31 controls). No experiment. G131/G132 are verified by Local L085/L086. Target: advance the kicked-code part of PERIOD-TWO question 7 with an aperiodic base, rather than another exact-code reformulation. Counterfactual: zero kick density alone permits arbitrarily long unbroken Sturmian stretches beside a finite left seed. The conservative constants below are not optimized. The dyadic-kick guard prevents an entropy or all-kicks exclusion claim.

Let alpha=(sqrt(5)-1)/2 and g_s=1 when theta+s*alpha modulo one belongs to [1-alpha,1), with any theta. Assume the Rule 30 wall is 0101... from time zero and the initial left row is zero beyond radius L.

**Finite repetition lemma.** For every integer C>=0, a golden-angle Sturmian prefix through index

    N=84*(C+4)

cannot obey the finite repeat bound b<=2a+q+C for every repetition g_s=g_(s+q) on a<=s<=b with b+q<=N. In particular a visible companion cannot agree with such a Sturmian word through index 84*(L+4). The L=0 left seed already fails the first black-time equation; for L>=1 Theorem E Step 0 supplies a repeat constant no larger than L.

**Finite-horizon proof.** Use section 8.57's convergent notation q_n, delta_n, K_n and the first two visit times h,h' to K_n. For a fixed q=q_n, if N>=4q+3C+8, the finite repeat bound alone forces

    h <= q+C+2,
    h' <= 2h+q+C+4.

Indeed, if h>q+C+2, the repetition from 0 through q+C+1 violates the bound; all compared samples lie within N. After the first visit, if h'>2h+q+C+4, the repetition from h+1 through 2h+q+C+3 violates the bound. Its last compared index is at most 4q+3C+7, using the first inequality. These are exactly Theorem E's two visit inequalities, obtained without assuming the second visit was already observed. As in that proof, returns to K_n are at least q_(n+1) apart. Thus

    q_(n+1)-q_n-C-4 <= h(n) <= q_n+C+2.       (visit bounds)

Choose n minimally so q_(n-1)>2C+8. For the golden angle all partial quotients are one. The separation argument of Theorem E Step 4, applied at n and n+1, gives

    h(n+1)=h(n)+q_n,
    h(n+2)=h(n+1)+q_(n+1).

Here its prerequisites are just the visit bounds at n,n+1,n+2 and q_(n-1)>2C+8: the two arcs at successive scales are disjoint and closer than delta_(n-1), and the only possible signed return in the bounded visit-time difference is -q_n. No extra hypothesis about the Rule 30 orbit enters this separation step.

The visit bounds and first identity give h(n)>=q_(n-1)-C-4. The second identity and the upper visit bound at n+2 give h(n+1)<=q_n+C+2. Combining these with the first identity yields q_(n-1)<=2C+6, a contradiction.

All three scales are present in the stated horizon. Minimality and the Fibonacci recurrence imply q_(n-1)<=4C+16 and q_(n+2)<=5q_(n-1)<=20C+80. Therefore

    4q_(n+2)+3C+8 <= 83C+328 < 84*(C+4).

This proves the finite repetition lemma.

**Unbroken stretches at later times.** If the visible companion agrees with a golden-angle Sturmian word from visible index a through b, restart at physical time 2a. The left-zero radius is then at most L+2a by the light cone, and the wall has the same phase. The finite lemma, with this larger radius and arbitrary rephased theta, requires

    b-a < 84*(L+2a+4).

This statement does not require the companion to be periodic or the rest of it to be Sturmian.

**Necessary kick-gap bound.** Suppose c equals a fixed golden-angle Sturmian word except at its actual disagreement indices k_0<k_1<.... Finite support requires infinitely many disagreements, since an eventual exact code is already excluded by G131. Before the first kick, the finite lemma gives k_0<=84*(L+4). Between consecutive kicks use a=k_j+1 and b=k_(j+1)-1. The preceding inequality yields the conservative integer bound

    k_(j+1) <= 169*k_j + 84*L + 505.

Thus schedules with unbounded ratios k_(j+1)/k_j are excluded. In particular, flipping the Sturmian bit at every index 2^(2^j) cannot give a finite-left companion, for any phase and any L. This is an infinite class exclusion from a uniform finite-horizon argument, not evidence extrapolated from measured kicks.

**Unexpected checks and limits.** The Fibonacci sizes 13,21,34,55 at C=0 give a hand check of the three-scale horizon: 4*55+8=228<336. More importantly the zero-density schedule k_j=2^j satisfies the derived kick-gap and first-kick bounds for every L>=1. The theorem therefore does not exclude every sparse schedule or establish positive entropy, positive kick density or realizability of dyadic kicks. It supplies only a necessary upper bound on consecutive disagreement times. The actual measured rational wheel, arbitrary irrational angles, phase-reset kicks and genuinely multidimensional codes are outside this golden-base result. These are the identified independent scope checks.


### G134. Bounded-type rotation codes require geometrically spaced corrections (2026-10-06)

**Status and target.** Symbolic extension of G133, independently verified by Local L088. No experiment or new numerical prediction. Theorem E and G2.2 supply the continued-fraction facts; G133 supplies the finite comparison deadlines. Target: remove the golden-angle restriction from the sparse-kick exclusion. Counterfactual: bounded partial quotients might still allow corrections with unbounded successive spacing ratios beside a finite left seed. The proof below excludes that possibility. This is a consequence of the existing repetition obstruction, with no general novelty claim.

Let alpha in (0,1) be irrational with every partial quotient a_j<=A, where A>=1 is an integer. For any phase theta let g be its standard half-open Sturmian code. Define

    K_A=8*(A+1)^4+3.

**Finite-prefix theorem.** For every integer C>=0, the prefix of g through index N=K_A*(C+4) cannot satisfy b<=2a+q+C for every repetition g_s=g_(s+q) on a<=s<=b with b+q<=N.

Use Theorem E's convergents q_n, errors delta_n, mismatch arcs K_n and first visit h(n). G133's finite comparison argument, valid for every irrational angle once these mismatch arcs have the stated form, gives

    q_(j+1)-q_j-C-4 <= h(j) <= q_j+C+2

whenever N>=4q_j+3C+8. Choose n minimally with q_(n-1)>T=2C+8. The initial denominator q_0=1 is below T. Minimality and q_j=a_j*q_(j-1)+q_(j-2) give q_(n-1)<=(A+1)*T. Thus

    q_(n+2) <= (A+1)^3*q_(n-1) <= (A+1)^4*T,
    4q_(n+2)+3C+8 <= K_A*(C+4).

The visit bounds therefore hold at all three indices n,n+1,n+2. If any of a_(n+1),a_(n+2),a_(n+3) is at least two, the corresponding visit bounds imply q_(j-1)<=2C+6, impossible. All three coefficients must consequently be one.

**Quantitative separation, including the finite-offset check.** Put D=2C+6. At j=n and j=n+1, the opposite mismatch arcs are disjoint, their combined length is |delta_(j-1)|, and the visit bounds place

    m=h(j)-h(j+1) in [-q_j-D,D].

Also m is nonzero and ||m*alpha||<|delta_(j-1)|. Best approximation forces |m|>=q_j. Since D<q_(j-1)<=q_j, this means m=-q_j-r with 0<=r<=D. If r>0, then r<q_(j-1), so the preceding best-approximation bound and the error recurrence give

    ||r*alpha|| >= |delta_(j-2)|
                 = a_j*|delta_(j-1)|+|delta_j|
                 >= |delta_(j-1)|+|delta_j|.

The triangle inequality on the circle now gives ||(q_j+r)*alpha||>=|delta_(j-1)|, a contradiction. Hence r=0 exactly, and

    h(n+1)=h(n)+q_n,
    h(n+2)=h(n+1)+q_(n+1).

This finite-offset argument uses no unspecified sufficiently-large threshold or phase-dependent distance. It also supplies the explicit justification for G133's quantitative use of Theorem E Step 4. At the selected indices the standard mismatch description applies: n>=2; if n=2 then q_1>T forces alpha<1/8, and later convergent errors are smaller than both coding-interval lengths. The same assertion at n>=3 follows from the first convergent errors and their monotone decrease.

Finally the lower visit bound at n is h(n)>=q_(n-1)-C-4. The second identity and upper bound at n+2 give h(n+1)<=q_n+C+2. Substituting the first identity forces q_(n-1)<=2C+6, again a contradiction. This proves the finite-prefix theorem.

**Finite-left companion consequence.** Let the Rule 30 wall be 0101... and its initial left row be zero beyond radius L>=1. Theorem E Step 0 permits repeat constant C=L. Restarting at physical time 2a enlarges the left-zero radius to at most L+2a. Any matching stretch with this fixed-angle Sturmian code, rephased as necessary, obeys

    b-a < K_A*(L+2a+4).

For the actual disagreement indices k_0<k_1<... against a fixed base code, G131 already excludes finitely many disagreements. The finite-prefix theorem and the intervals between disagreements give

    k_0 <= K_A*(L+4),
    k_(j+1) <= (2K_A+1)*k_j + K_A*L + 6K_A + 1.

Thus unbounded ratios k_(j+1)/k_j are impossible for every bounded-type irrational angle, every phase and every finite left radius. In particular super-geometric flip schedules are excluded throughout this class. The sharper golden constant in G133 remains useful; this uniform class constant is deliberately conservative.

**Independent and unexpected scope checks.** The finite-offset check above is independent of G2.2's asymptotic eta argument and is the identified unexpected check. At A=1 this theorem gives K_A=131 rather than G133's 84, a consistency check without an optimality claim. The schedule k_j=2^j still satisfies the resulting necessary bounds for L>=1, so this argument establishes neither positive kick density nor positive entropy nor realizability. For unbounded partial quotients, the controlled denominator growth used to choose a linear horizon fails; this proof supplies no uniform linear bound there. Arbitrary phase-reset kicks, the measured rational wheel and genuinely multidimensional observables remain outside the claim.


### G135. A uniform Sturmian horizon also bounds phase and angle resets (2026-10-06)

**Status and target.** Symbolic proof, independently verified by Local L088; no experiment. G133 is independently verified by Local L087; G134 is verified by Local L088. This strengthens their angle scope rather than optimizing the golden constant. Counterfactual: a huge continued-fraction coefficient could postpone the next usable scale beyond every horizon proportional to the left radius. The finite repetition bound itself prevents that escape. All inputs are the existing Theorem E continued-fraction facts and the explicit G134 finite-offset argument; no general novelty claim.

**Uniform finite-prefix theorem.** For every irrational alpha in (0,1), every phase theta and every integer C>=0, its standard half-open Sturmian prefix through

    N=251*(C+4)

contains a repetition g_s=g_(s+q) on a<=s<=b with b+q<=N and b>2a+q+C. There is no bound on partial quotients in this statement.

Suppose otherwise. Put T=2C+8. Choose n minimally with q_(n-1)>T and put r=n-2. Then q_r<=T. At every usable scale j the finite comparison deadlines of G133 give

    q_(j+1)-q_j-C-4 <= h(j) <= q_j+C+2,
    q_(j+1) <= 2q_j+2C+6 < 2q_j+T,

provided N>=4q_j+3C+8. The second line is the crucial replacement for an externally assumed bound on partial quotients.

The starting scale r is usable, including its small-index cases. If r=0, q_1>T implies alpha<1/8; delta_0=alpha and the two mismatch arcs for period q_0=1 are disjoint, so Theorem E's break description and return gap at least q_1 hold. If r>=1, |delta_r| is at most min(alpha,1-alpha), making the same break description valid. Indeed, when a_1=1, |delta_1|=1-alpha; when a_1>=2, the recurrence alpha=a_2*|delta_1|+|delta_2| gives |delta_1|<alpha. Later errors decrease. Equality of an error with the shorter interval length merely makes the mismatch arcs touch at a half-open endpoint; it does not create an overlap.

Starting with q_r<=T, apply the growth inequality successively at r,r+1,r+2,r+3. Every application is justified within the fixed horizon, because the resulting bounds are

    q_(n-1) < 3T,
    q_n < 7T,
    q_(n+1) < 15T,
    q_(n+2) < 31T,

and

    4*(31T)+3C+8 = 251C+1000 < 251*(C+4).

Thus the visit bounds hold at n,n+1,n+2 as well. This is an induction on already bounded denominators, not a circular assumption that the later scales fit.

At those three scales, any coefficient a_(j+1)>=2 would give q_(j-1)<=2C+6, contradicting q_(n-1)>T. Hence a_(n+1),a_(n+2),a_(n+3) must all be one. The explicit separation in G134 applies at n and n+1: for m=h(j)-h(j+1), best approximation gives m=-q_j-u with 0<=u<=2C+6; a positive u<q_(j-1) would give

    ||(q_j+u)*alpha|| >= |delta_(j-2)|-|delta_j|
                         >= |delta_(j-1)|,

contrary to the distance across the opposite mismatch arcs. Therefore

    h(n+1)=h(n)+q_n,
    h(n+2)=h(n+1)+q_(n+1).

Combining the lower visit bound at n with the upper bound at n+2 yields q_(n-1)<=2C+6, the final contradiction. The uniform finite-prefix theorem follows.

**Companion and reset consequences.** Beside a Rule 30 wall 0101... with initial left-zero radius L>=1, any interval [a,b] matching a standard irrational Sturmian code obeys

    b-a < 251*(L+2a+4).

The phase and angle may be chosen separately for each interval: restart at physical time 2a, use the light-cone radius L+2a and apply the uniform theorem with repeat constant C=L+2a. No relation between the different intervals' angles is required.

Consequently, if a companion is made of consecutive Sturmian-coded pieces with reset times 0=t_0<t_1<..., even allowing both phase and angle to change at each reset, it necessarily satisfies

    t_(j+1) <= 503*t_j + 251*L + 1004.

A final infinite piece is impossible. Super-geometrically separated resets cannot support a finite left seed. For actual disagreements k_j against one fixed irrational Sturmian base, the corresponding statement is

    k_0 <= 251*(L+4),
    k_(j+1) <= 503*k_j + 251*L + 1507.

This excludes super-geometric flips for every irrational base angle, including unbounded-type angles. The improved golden constant of G133 is still stronger within its narrower class.

**Unexpected independent checks and limits.** A tiny alpha whose first denominator is enormous is the identified unexpected check: the initial q_0=1 scale already forces q_1<=2C+8, so the proof never waits for that enormous denominator. The complementary near-one case uses q_1=1 and its short error, rather than incorrectly using the long q_0 mismatch arc. These endpoint-angle controls justify the uniform claim. Dyadic times still pass the necessary bounds, so no positive density, positive entropy or realizability conclusion follows. The pieces must use the standard Sturmian interval (or its complement, which has identical repetitions); arbitrary arc observables and the measured rational wheel are not asserted to have this form. This is a class exclusion for companions, not a prize solution.


### G136. Uniform recoding horizons include rational mechanical bases (2026-10-06)

**Status and purpose.** Symbolic corollary of G131 and G135; independently verified by Local L089. Dependencies G134/G135 are independently verified by Local L088. No experiment. Counterfactual: either a finite recoding margin or a rational limiting angle might evade the uniform horizon. The exact margin and a finite-prefix approximation settle both. This advances recoded/reset companions, not the missing entropy theorem. The inherited rotation-partition prior art is recorded in G131; no general novelty claim.

Let g_s be the standard mechanical code of theta+s*alpha modulo one in [1-alpha,1), now allowing every alpha in [0,1]. The endpoint angles give the constant zero and constant one codes. Let F be any binary function of a block of width w+1, w>=0, and put c_s=F(g_s,...,g_(s+w)). Define

    H(C,w)=251*(C+4)+250*w.

**Finite-prefix theorem.** For every integer C>=0, the prefix of c through index M=H(C,w) contains a repetition c_s=c_(s+q) on a<=s<=b with b+q<=M and b>2a+q+C. Neither injectivity nor nonconstancy of F is needed.

First extend G135 to rational and endpoint angles. Every finite prefix g_0,...,g_N of the specified mechanical code is also a prefix of an irrational mechanical code with slightly perturbed angle and phase. To see the boundary issue explicitly, change the angle by epsilon and increase the phase by eta, choosing eta>(N+1)*abs(epsilon), with both arbitrarily small. At a sample exactly on the upper endpoint 0 modulo one, its displacement is eta+s*epsilon>0, giving the correct right-hand value zero for an interior angle. At a sample on the lower endpoint 1-alpha, its displacement relative to that moving endpoint is eta+(s+1)*epsilon>0, giving the correct right-hand value one. All other finitely many samples have a positive margin and keep their value for sufficiently small changes. Choose the perturbed angle irrational. For alpha=0, choose a small positive angle and a phase perturbation larger than the total drift; every sample stays outside its tiny one-interval. For alpha=1, choose an angle just below one and the same dominating positive perturbation; every sample stays inside the one-interval. Thus the finite-prefix contradiction of G135 holds for every mechanical angle.

Now suppose c satisfies the finite repeat bound through M. The underlying mechanical prefix is available through N=M+w=251*(C+w+4). If g repeats on [a,e] with e+q<=N and e>=a+w, then c repeats on [a,e-w], and its compared samples end by N-w=M. Hence e<=2a+q+C+w. If e<a+w, the same inequality is automatic. Every repetition of g through N would therefore satisfy the forbidden bound with constant C+w, contradicting the extended G135 theorem. This proves the claim and explains why the margin is 250*w rather than an unspecified additive loss.

**Matching pieces and corrections.** Beside the alternating Rule 30 wall with initial left-zero radius L>=1, a companion cannot match such a recoded mechanical word on [a,b] unless

    b-a < H(L+2a,w).

For pieces with reset times t_j and widths bounded by one fixed w, the functions, angles and phases may change from piece to piece, but necessarily

    t_(j+1) <= 503*t_j + 251*L + 1004 + 250*w.

For actual disagreement indices against one fixed recoded mechanical base, the bounds are

    k_0 <= 251*(L+4)+250*w,
    k_(j+1) <= 503*k_j + 251*L + 1507 + 250*w.

Finitely many disagreements or a final infinite piece are impossible by the same finite-prefix theorem at a later restart. Consequently super-geometrically spaced resets or corrections are excluded for bounded-width recodings at every mechanical angle. These are necessary bounds, not a construction of a realizable companion.

**Orbit-endpoint interpretation.** G131 constructs a finite block code for any half-open binary arc partition whose actual jump points have the form beta+k_j*alpha. If the integer exponents span D=max(k_j)-min(k_j)>=1, its Laurent polynomial Q(z)=sum(z^k_j) has an even number of jumps and Q=(1+z)P. P has exponent span D-1, so after rephasing its block width parameter is w=D-1. The same construction works for rational angles: distinct actual jump points are listed once, and equality of the jumps leaves only a constant difference, absorbed in F. Constant partitions use w=0. Thus pieces whose endpoint representations have uniformly bounded exponent span inherit the reset bound, even if their angles and partitions vary. The controlling parameter here is exponent span, not merely the number of endpoints. No arbitrary unrelated-endpoint partition is claimed to have this representation.

**Unexpected width guard, proved without a run.** An unrestricted finite block code can fit any prescribed finite binary prefix. Fix an irrational Sturmian g and finitely many starting indices 0,...,m. Their infinite future tails are pairwise distinct: equality of two would give an eventually periodic mechanical code, impossible because its symbol frequency is irrational. For each pair there is a finite first differing coordinate; take w at least the largest such coordinate. All the blocks g_s,...,g_(s+w) at these indices are distinct. Define F on them to output the desired prefix, and define it arbitrarily elsewhere. This does not give an infinite prescribed word, a uniform w or a finite-left Rule 30 realization. In particular the record's overlap-free Thue-Morse prefixes can pass the repeat inequality for arbitrary finite horizons while being fitted by increasingly wide recodings. A horizon independent of all recoding widths is therefore false. This is the identified independent scope check. At w=0 the theorem recovers G135 and its rational extension; constant F also retains the immediate period-one obstruction. Geometric correction schedules still pass the displayed necessary bounds, and no positive density, entropy or prize solution follows.


### G137. A dyadic sparse word passes every repeat test; faster powers fail (2026-10-06)

**Status and target.** Symbolic obstruction audit, independently verified by Local L090; no experiment. G134/G135 are verified by Local L088 and G136 awaits review. Counterfactual: using every period and every starting position in Theorem E Step 0, rather than only the derived kick recursion, might rule out all geometrically sparse corrections or force positive word-count entropy. The explicit dyadic word refutes that inference. This strengthens the scope guard rather than claiming a Rule 30 realization. The existing Thue-Morse guard in section 8.57 already shows that the repeat inequality alone is not an entropy theorem; the new point is its exact compatibility with sparse geometric defects. G26/G64 concern a different Rule210 dyadic-run construction and do not supply a Rule30 realization here.

Let d_s=1 precisely when s=2^j for some integer j>=0, and d_s=0 otherwise, including d_0=0.

**Every repetition obeys the strongest nonnegative-margin test.** If d_s=d_(s+q) for every a<=s<=b, where a>=0 and q>=1, then

    b <= 2a+q-1.

For a>=1, choose the smallest power of two p>=a, so p<=2a. If p+q is not a power of two, there is a mismatch at s=p. If p+q=P is a power of two, then P>=2p and p+2q=2P-p lies strictly between P and 2P. Thus there is a mismatch at s=P=p+q. In both cases a mismatch lies in [a,2a+q], proving the bound.

For a=0, if q is a power of two, s=0 is already a mismatch. Otherwise q>=3. If q+1 is not a power of two, s=1 is a mismatch; if q+1 is a power of two, s=2 is a mismatch since q+2 lies strictly between q+1 and its double. In either case the first mismatch is at most q, giving b<=q-1 as required. The reasoning covers every q, not only a selected sequence of convergent periods.

Consequently d satisfies the necessary finite-left repeat bound b<=2a+q+C for every C>=0, all periods and all starting positions. Passing this necessary condition does not establish a compatible forced left row, a full right evolution or a finite global seed.

**Sparse, aperiodic and zero word-count entropy.** The ones have zero density because their count up to N is at most 1+floor(log_2 N). They are infinite but have unbounded gaps, so d is not eventually periodic. For a factor length m>=1, starts a<m contribute at most m different words. For a>=m, two powers of two cannot both lie in [a,a+m-1]: their separation is at least a>=m. Such factors have at most one one, giving at most m+1 possibilities. Therefore the number P(m) of distinct length-m factors obeys

    P(m) <= 2m+1,
    limsup log_2(P(m))/m = 0.

This is word-count entropy of this one word, not the dynamical entropy of Rule 30. Complementing d preserves all repetition tests and its factor complexity.

**Unexpected rate control.** For an integer B>=3 let d^(B) have ones at B^j and zero elsewhere. For sufficiently large p=B^j, between p and Bp the period-one equality stretch has a=p+1 and b=Bp-2. The repeat bound would require

    (B-2)*p <= C+5.

It fails for arbitrarily large p, for every fixed C. Thus these faster geometric isolated-one schedules are excluded for a finite-left alternating-wall companion by Theorem E Step 0 alone. Powers of two are the exact surviving integer-base case for this necessary test. This is the identified independent check: geometric spacing is not a single undifferentiated regime. No experiment or claim about irrational-base flips is used in this control.

**Closed bridge and next obligation.** Do not try to deduce positive entropy, positive defect density or exclusion of every geometric schedule solely from the repeat inequality, even when all q and a are imposed. The explicit sparse word passes the full family. Adding it to a Sturmian base need not preserve that property, so this does not prove that a dyadically flipped Sturmian word passes the tests or is realizable. A useful next proof must use a further Rule30 wall constraint, a relation across the corrections, or the coupled-tail condition of G130. The finite-left sufficiency question for d itself is not answered here.


### G138. The first nonlinear kick gate does not close the initial-tail problem (2026-10-06)

**Status and purpose.** Symbolic wall audit, independent review pending; no experiment. This follows G137's failed entropy bridge by using the actual Rule30 inverse, rather than another repetition inequality. Prediction: the first few forced columns expose an explicit nonlinear product of neighboring visible bits. Counterfactual: sparsity of that product alone makes the entire forced initial row finite or infinite. Neither implication is obtained. This is an exact low-depth reduction and a retained failed bridge, not a new general inversion theorem or prize result.

Write v_j(t)=x_(-j)(t), with v_0(2s)=0 and v_0(2s+1)=1. Let c_s be column 1's visible bit at physical time 2s. The wall forces v_1(2s)=1-c_s and v_1(2s+1)=1. The inverse Rule30 identity is

    v_(j+1)(t)=v_j(t+1) XOR (v_j(t) OR v_(j-1)(t)).

Put A=c_s, B=c_(s+1), D=c_(s+2). Repeated Boolean substitution yields the exact even/odd pairs

    (v_1(2s),v_1(2s+1)) = (1-A,1),
    (v_2(2s),v_2(2s+1)) = (A,B),
    (v_3(2s),v_3(2s+1)) = (1-B,1-B),
    (v_4(2s),v_4(2s+1)) = (A*B,D),
    (v_5(2s),v_5(2s+1)) = (D XOR (A OR (1-B)),1-B).

For example the depth-four even entry is (1-B) XOR ((1-B) OR A)=A*B. Its odd entry is (1-D) XOR ((1-B) OR B)=D. The depth-five odd entry is B*D XOR (D OR (1-B))=1-B: for B=0 both sides are one, and for B=1 both sides are zero. These independent Boolean simplifications check the product and the cancellation without a dynamical run. They apply to the forced left construction; a full right evolution is an additional constraint.

**Dyadic specialization.** For c=d of G137, c_s*c_(s+1)=1 only at s=1, because 1 and 2 are the only consecutive positive powers of two. Depth four's even trace therefore has exactly one one, at physical time 2; its odd trace still contains infinitely many shifted dyadic pulses. The initial row's first five cells are

    (v_1(0),...,v_5(0))=(1,0,0,0,1).

This supplies neither a tail classification nor a finite-left realization. Vanishing on one temporal parity at one depth is not eventual vanishing across all initial depths.

**Unexpected constant-code control.** If c is constantly zero, the same formulas give an all-one depth-one column and then stationary alternating columns 0,1,0,1 through the depths displayed. The inverse recurrence continues that checkerboard to arbitrary depth: whenever two neighboring columns are stationary and opposite, the next outward column is the inner column's complement. Thus the forced initial left row has infinitely many ones even though the depth-four product is identically zero. This is the identified independent check against treating a sparse product as a finite tail. The constant-one case gives a time-alternating depth-one column, stationary one at depth two, then stationary alternating columns 0,1,0,... outward, likewise an infinite initial tail.

**Failed bridge retained.** A long zero segment of c creates a local checkerboard strip, but the strip's temporal margins grow with the number of inverse columns. Dyadic segments move outward in time as their lengths increase. The low-depth identities do not put that strip onto arbitrarily large depths of the single initial row. Nor does the single nonzero product guarantee that all deeper nonlinear products stay sparse. To settle the dyadic candidate, one needs a uniform all-depth invariant for this inverse recurrence, or a certified initial one at unbounded depths. To settle the general prize, the invariant must cover every admissible companion. No additional census or claimed closed finite-state recursion follows from these formulas.


### G139. Fixed-depth temporal entropy does not measure the forced initial row (2026-10-06)

**Status and target.** Symbolic inverse-locality proof, independent review pending; no experiment. G138's low-depth audit is extended to every fixed depth. Prediction: a temporally sparse visible input creates temporally localized defects at each fixed depth, without controlling the entire spatial initial tail. Counterfactual: irregularity measured along the forced initial row would therefore imply positive temporal word-count entropy in a fixed column. The proof separates those axes. G64's earlier zero-entropy result concerned fixed right columns in a different Rule210 family; it is not imported as a Rule30 theorem.

Use G138's v_j(t) and inverse recurrence. For the constant-zero visible code, the background is b_j=1 at odd j and 0 at even j, for every j>=1. For any visible c define e_j(t)=v_j(t) XOR b_j. Then e_1(2s)=c_s and e_1(2s+1)=0. At depth two,

    e_2(t)=e_1(t+1) XOR e_1(t).

For j>=2, direct subtraction of the stationary background gives

    e_(j+1)(t)=e_j(t+1) XOR e_j(t)*(1-e_(j-1)(t))    when j is odd,
    e_(j+1)(t)=e_j(t+1) XOR (1-e_j(t))*e_(j-1)(t)    when j is even.

Indeed adjacent background bits are opposite. Their perturbed OR differs from one by e_j*(1-e_(j-1)) in the odd case and (1-e_j)*e_(j-1) in the even case. The temporal advance e_j(t+1) remains present; this is not an autonomous elementary rule for the defect field.

**All-depth locality.** By induction, e_j(t) is determined by the samples of e_1 on [t,t+j-1]. If all those samples vanish, e_j(t)=0. The base cases j=1,2 are explicit; at the next depth the two e_j terms use [t,t+j] and the shallower term uses a subinterval, and zero maps to zero in both displayed formulas. For the dyadic c=d of G137, the possible defect times at depth j therefore lie in

    union over k>=0 of [2^(k+1)-j+1, 2^(k+1)], intersected with t>=0.

This is an upper support bound, not equality. Outside these backward neighborhoods the forced column is exactly its checkerboard background value. It does not require linearizing away a nonlinear interaction.

**Temporal word bound.** Let P_c(n) count distinct length-n factors of c. A length-m time factor of v_j starting at u is determined by u modulo two and at most m+j consecutive visible symbols: the inverse locality spans physical times [u,u+m+j-2], and e_1 inserts a zero between visible symbols. Padding the visible window if needed gives

    P_(v_j)(m) <= 2*P_c(m+j).

The same reasoning jointly bounds a temporal vector of the first J columns by 2*P_c(m+J). Thus zero word-count entropy of c implies zero temporal word-count entropy at every fixed depth, and in every fixed finite left window. For d or its complement, G137 gives the explicit bound P_(v_j)(m)<=4(m+j)+2. This is not a uniform statement when the observed depth grows with m.

**Unexpected spatial-tail guard.** To evaluate v_j(0), the determining window length grows with j. Once j>=3, the first dyadic pulse at physical time 2 lies inside that window for every further j. The support lemma therefore does not force e_j(0) to vanish at large j. Nor may the fixed-j entropy limit be taken with j growing. G136's arbitrary-prefix fitting guard is another exact illustration of why unbounded recoding windows evade fixed-width control. These are the identified independent quantifier checks. Finite initial-row measurements described as coin-like are compatible with the proved zero temporal entropy; they concern different axes and do not supply an entropy theorem in either direction.

**Remaining obligation.** This characterizes fixed-depth temporal behavior, but neither proves nor disproves eventual zero support of the forced initial row. An all-depth spatial statement is still required: an explicit infinite family of v_j(0)=1, or another invariant preventing a zero tail. Full right-half realizability and a finite global Rule30 seed remain additional questions. No computational job duplicates Local's dyadic initial-row probe.
