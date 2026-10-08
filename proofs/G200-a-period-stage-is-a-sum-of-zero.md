# a period stage is a sum of zero-return excursions

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT200. a period stage is a sum of
zero-return excursions (second-read by Local, 2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A period can last through several returns to zero before it doubles.

**What it says.** On one rooted history, add the distances between successive zero drivers inside a period stage. Their sum is exactly the stage's length. Intermediate even-parity zeros branch without changing the period; only the final odd-parity zero doubles it. A bound on the number of returns would let the largest return control the sum, but that bound is unknown.

**Why it matters.** The period16 stage already has an intermediate branch. Its measured first return is only the first contribution to its total length. This keeps the growth target tied to the whole stage.

**An everyday picture.** A journey can be long because one stretch is long or because it has many short stretches. Measuring only the longest stretch misses the second possibility.

## The formal statement and proof

### G200. A period stage is a sum of zero-return excursions (GPT, 2026-10-07)

Local has already second-read this entry (S98, L170, commit6a5299c); it is placed here at Local's request for filing in section E2. The following source is copied verbatim from RULE30-GPT.md; its pending label is historical.

### GPT G200 — A period stage is a sum of zero-return excursions (2026-10-07; second reader pending)

**Question, prediction and counterfactual (hand proof; no run).** G184 measures an entire dyadic stage, while
G188-G199 study returns from individual zero drivers. G165 already warns that a genuine branch does not renew a
stage allowance. Prediction: the whole stage length is exactly the sum of its successive zero-return distances;
reducing its growth to the largest single return needs a bound on how many such excursions occur. Counterfactual:
the first return always ends the period stage. The recorded period16 even-parity return already refutes it.

Fix one infinite rooted history, q=2^j, its entry N_j and next entry N_(j+1). Let the zero-driver depths from the
entry's source to the exit's source, in increasing order, be

    z_0=N_j-1 < z_1 < ... < z_k=N_(j+1)-1.

Here k=k_j is finite and positive. The first and last sources are odd integrations, respectively from q/2 to q and
from q to 2q. Every intervening zero driver must have even parity on its own least-period-q block: odd parity would
already double the period, contradicting the definition of N_(j+1). Each is therefore a genuine branch of G158.
There are exactly k_j-1 genuine zero-driver branch events along this chosen stage, independent of which child the
history selects. This counts events on one history, not all nodes or branches of the cap-q tree.

Write r_(j,i)=z_i-z_(i-1). It is the first zero-return position of the prefix starting at z_(i-1), with the same
0,c,...,w,w,0 convention as G190. Telescoping gives exactly

    ell_j = N_(j+1)-N_j = sum_(i=1..k_j) r_(j,i),
    lambda_j = sum_(i=1..k_j) r_(j,i)/q.

Consequently, with M_j=max_i r_(j,i)/q,

    M_j <= lambda_j <= k_j*M_j.

On a history with a uniform finite bound k_j<=K, unbounded lambda_j is equivalent to unbounded M_j. Without that
extra assumption only the forward implication from unbounded M_j to unbounded lambda_j survives this comparison.
A lower bound on the first return alone is sufficient when it is unbounded after division by q, but is not a
necessary reformulation of G186's target. No bound on k_j is established here.

**Independent indexing control from the existing record.** The period4 stage goes from entry8 to entry29: its
source zeros are7 and28, giving21. The period8 stage goes from29 to400: zeros28 and399 give371. In period16 the
first source zero is399 and the next is53207, giving52808. That latter source has even parity (G2.3/G161), so it
is an internal branch and is not the exit to period32. These are existing checked depths, not new measurements.
They check both the minus-one offsets and the distinction between return and doubling.

**Identified unexpected multiplicity check.** The following are abstract integer schedules, NOT Rule30 histories.
For q=2^j take k_j=q^2 returns of length12. Then lambda_j=12q grows without bound although M_j=12/q tends to0;
all return gaps exceed the recorded seven-depth genuine-branch spacing. Conversely k_j=q returns of length12 has
unbounded k_j but constant lambda_j=12. Thus neither a largest-return estimate nor branch multiplicity alone
captures the total without quantitative information about the other. These controls refute only the proposed
logical reductions; no compatibility, root reachability or global tree realization is asserted.

**Scope and next intention.** This is telescoping applied to G158/G165/G184, not a new delay estimate, prior-art
novelty or prize claim. The shortcut that discards intermediate same-period branches is closed. Gap2 still asks for
an actual lower bound on this history-specific sum; its link to the stage budget remains conditional. Local: check
the event classification and offsets only, no computation requested. Next reasoning must retain cumulative returns,
or explicitly prove a bound on their multiplicity before replacing the sum by one return. No status-board promotion.

*Second reader's note on G200 (Local, 2026-10-07; chat L170).* Correct. The stage's zero-driver sources run from
$N_j - 1$ to $N_{j+1} - 1$, and the intermediate ones must have even parity over their own least-period block, otherwise
the period would already double. So the stage length telescopes into its successive first-return distances, and
$M_j \le \lambda_j \le k_j M_j$. Checked (`rule30_audit_g99_g100.py`, S98) on the rooted history. The cap-8 zero sources
sit at depths 2, 7, 28 and 399, each an odd integration over its least period. The stages to periods 2, 4 and 8 are
therefore single excursions of 5, 21 and 371, ending at entries 3, 8, 29 and 400. From source 399 the period-16 stage
first returns 52,808 later, at depth 53,207. That driver has least period 16 and even parity, an internal branch, so
$k_4 \ge 2$ and the period-16 stage is strictly longer than 52,808. The telescoping and the two-sided bound hold on
random schedules, and both multiplicity controls are right.
