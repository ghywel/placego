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


## G3. Forced-zero reasoning and diagnostics (2026-10-06; in progress)

The owner authorized continued work and use of spare compute. Taking the agreed reasoning lane of §8.2,
not duplicating Local's record searches or million-diagonal run. Both startup probes passed again.
Read §8.2, §8.37–§8.38 and §8.41 before choosing the diagnostic. The existing record already measures
approximately geometric forced-walk survival; this run will distinguish an exact algebraic identity from
a possible small-state explanation, and check deeper random prefixes rather than increase exact records.

For the anti-diagonal pair P = A(k-1), Q = A(k-2), let pi mean bit parity and
z = pi(P AND (Q shifted left once)). Expanding OR as XOR plus AND in the running-XOR update gives
L(k) = (k mod 2) XOR pi(P) XOR pi(Q) XOR z XOR ((k mod 2) AND c), where c is the newest input bit.
At even depth the input bit is hidden: the three parity bits determine the forced output exactly.
This does not say those three bits update autonomously; the counterfactual asks that question.

The pre-registered probe is tests/probes/lexicon/rule30_gpt_forced.py. Its header specifies controls,
sample sizes and seeds, a blind conditional-survival band and counterexamples sought against three-bit
closure and against deleting the overlap term. No run has started. A targeted prior-art search returned
Kopra's left-permutivity paper already in our record and Brunnbauer's diagonal-polynomial work; neither
was used to assert a new theorem or novelty. The parity expansion is elementary Boolean algebra applied
to records.c's existing recurrence.
