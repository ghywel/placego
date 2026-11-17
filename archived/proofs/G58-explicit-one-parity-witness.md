# Explicit one-parity witness

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT58. Explicit one-parity witness
(second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this
summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

For Rule 30's sibling Rule 210, GPT built an explicit left half that keeps a whole family of walls going.

**What it says.** Take walls that are white at every even tick and anything at odd ticks. For Rule 210, the left
half can start entirely white and stay consistent for ever, and GPT wrote down the exact column-1 signal needed. So
the left-side form of the question fails for Rule 210 on these walls. Rule 30 remains open.

**Why it matters.** Rule 210 is a test bed: a sibling where the left-side question can be answered. It shows the
left side alone cannot decide the question for every rule.

**An everyday picture.** A scale model where the bridge does stand; it does not tell you yet whether the full-size
bridge will.

## The formal statement and proof

### G58. One-parity walls: an explicit empty-left witness (2026-10-06)

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

*Second reader's note on G58 and its addendum (Local, 2026-10-06; chat L033).* Correct. The invariant $u_k(t) = 0$ for
$t + k$ even holds from the empty row and the white even times of the wall, and propagates because both neighbours
then have $t + k$ even; so Rule 210's term $c \cdot r$ vanishes and the half-line is Rule 90's exactly. The wall
equation holds at even times by the definition of $\sigma$ and at odd times because every term is 0. The filter uses
the classical fact that $C_j$ is odd exactly when $j = 2^r - 1$. The addendum is sound: over $\mathbb{F}_2$,
$V = A(1 + S)$, rational series are exactly the eventually periodic ones, and $S = \sum z^{2^r}$ has unbounded gaps,
so a nonzero periodic $A$ forces $\sigma$ to be aperiodic. Checked independently (`rule30_audit_g58.py`): from an
empty row under Rule 210's own truth table, for 200 inputs (periodic with periods 1 to 7 and random, with holes),
the parity invariant, the wall equation, $\sigma(\text{odd}) = 0$ and the dyadic filter hold at every time to 160;
the Rule 30 counterfactual fails. **This settles Local's C066** (formerly in the waiting room): its existence claim
is proved, for every one-parity wall in this phase and with odd-time holes allowed; its family wording is
corrected as G58 says (not every $\sigma$ with $\sigma(\text{odd}) = 0$ gives an empty initial row).
