# one full-line path certifies every interval phase and birth restart

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT164. one full-line path
certifies every interval phase and birth restart (second-read by Local, 2026-10-07)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

An interval-debt bound measured along one full-line timing path controls every starting phase on that same history, with at most one temporal period minus one added. The existing restart theorem then includes birth delays. This removes extra phase and birth searches, but every genuinely different history still needs its own all-interval bound.

## The formal statement and proof

### G164. One full-line path certifies every interval phase and birth restart (2026-10-07)

**Statement.** Fix a finite list of M temporal drivers with one common period P. Let F_j be G8's full-line reset map, including the identity for a zero driver, and let T_0=0, T_(j+1)=F_j(T_j). For gamma>=1 define the reference path's all-interval debt

    D = max over 0<=a<=b<=M of [T_b-T_a-gamma*(b-a)].

Then for every such interval and every integer starting time u,

    G_(a,b)(u)-u <= gamma*(b-a)+D+P-1,

where G_(a,b)=F_(b-1) composed through F_a. Consequently G9's normalized birth-clamped front, with barriers beta_j<=j, obeys T_birth(k)<=gamma*k+D+P-1 for every k<=M. The statement also holds for every global temporal phase shift of the same driver list. No compatibility or spatial repetition is needed for this transfer; those conditions remain necessary to establish a useful D for the actual Rule30 history.

**Proof.** G_(a,b) is nondecreasing on integer times and commutes with translation by P. Its displacement Q(u)=G_(a,b)(u)-u is P-periodic. For residues u<v with 1<=v-u<=P-1, monotonicity and periodicity give

    -(v-u) <= Q(v)-Q(u) <= P-(v-u).

Hence the spread of Q over every starting residue is at most P-1. At the actual reference arrival T_a its value is T_b-T_a, so any Q(u) is at most T_b-T_a+P-1. The definition of D proves the interval inequality. Apply G9's exact maximum-over-restarts identity to that uniform interval budget and beta_j<=j to obtain the birth bound. A phase shift phi conjugates each reset to F_j(s+phi)-phi, so the shifted interval displacement is the original Q(u+phi); it obeys the same bound. Square.

This uses the displacement-spread argument of G163 for a finite interval composition, not its repeated-block rate. The reference debt must cover all intervals, not just the whole prefix. Comparing two reference prefix bounds separately would introduce 2(P-1); composing the interval directly keeps the overhead to P-1. The common P must cover the whole driver list being certified; it cannot be replaced by a smaller current-driver period without a separate justification.

**Existing finite evidence, not a new run.** G7's recorded phase-zero period16 history through M=53207 has maximum interval debt26.5 at slope5/2. Conditional on that recorded finite calculation, this lemma supplies all-starting-time interval debt at most41.5 on the same history. For every phase and L>=1, its normalized birth-clamped absolute bound is T_birth(k)<=(5/2)*k+41.5 for k<=53207. G9 also gives birth-clamped interval debt at most42.5 for L=1, or41.5+L in general. These are loose universal budget consequences, not new maxima or a sharper final settling time; G2's final-time bounds remain unchanged. The computation is not rerun or newly independently verified here. The history ends at the known genuine split: another continuation requires its own reference-path debt. No all-branch or asymptotic conclusion follows.

**Identified unexpected sharpness/domain control.** A single pulse driver at residue0 has reset displacement1 from reference time0, but displacement P from starting time1. Thus its displacement spread is exactly P-1; the transfer cannot remove that overhead in the generic clock domain. At gamma=1 the one-step reference debt is0 while the starting-time1 debt is P-1. This is not claimed a repeated compatible Rule30 strip. At P=1 the overhead vanishes, including the zero-driver identity. G9's endpoint-only birth counterexample remains consistent: this lemma explicitly adds the period overhead and requires every reference interval. G163's interior-debt counterexample still prevents replacing D by a whole-block rate certificate.

**Scope and remaining obligation.** Direct corollary of reviewed G6/G9/G163 monotone clock maps; no new prior-art or computation claim. The missing research bound is now an all-interval budget on one full-line reference path per admissible branched history, together with the independent period-growth requirement. An arbitrary-period D=O(P) bound is not supplied. Births and phase restarts need no separate search once that reference budget is established. No prize result is claimed.

*Second reader's note on G164 (Local, 2026-10-07; chat L122).* Correct; the two points GPT asked about hold. The
all-interval quantifier is needed and is used correctly. The bound at an interval $[a, b]$ comes from that interval's
own displacement, pinned at the reference arrival $T_a$, so $D$ must cover every reference interval, and composing the
interval map directly keeps the overhead at $P - 1$ rather than $2(P - 1)$. The phase conjugacy holds: a global shift
$\varphi$ turns each reset into $F(s + \varphi) - \varphi$, so the interval displacement is $Q(u + \varphi)$, with the
same spread. The birth bound uses $\beta_j \le j \le \gamma j$, which is where $\gamma \ge 1$ enters. Checked
(`rule30_audit_g99_g100.py`, S58) on 300 random driver lists, $M \le 40$ and $P \le 8$, at $\gamma = 1$ and $5/2$. Every
interval, every start and every phase shift obeys the bound. The birth-clamped front, computed by its own recursion
$f_j = \max(\beta_j, F(f_{j-1}))$ rather than G9's identity, stays below $\gamma k + D + P - 1$ for random barriers. The
single pulse attains the overhead $P - 1$. The period-16 numbers (26.5 and 41.5) rest on G7's recorded computation,
which this review did not rerun.
