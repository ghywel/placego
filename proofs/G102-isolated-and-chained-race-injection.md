# isolated and chained race injection

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT102. isolated and chained
race injection (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A single race corrupts a square one time in eight; a chain of races changes that slightly.

**What it says.** These pages come from the owner's questions about clocks and about GPU "races" (CONSTELLATION rows
18 and 19): what happens when a computer updates Rule 30 in place and some squares read a neighbour that has already
been updated. They are about Rule 30 for its own sake, not directly about the prize. Model a race as a square
reading its right neighbour's new value instead of its old one. On a random row, a lone race gives a wrong value one
time in eight. If the neighbour raced too, races chain and the rate becomes 1/(8 − 4ε), where ε is how often races
happen. A race that reads the left neighbour is wrong half the time.

**Why it matters.** It is the exact starting rate behind Local's race measurements. The left-right difference is
Rule 30's own: the left input passes straight through (the perfect wire of CL004), so racing it scrambles the result
completely.

**An everyday picture.** Copying from a neighbour who has already changed their answer: from one side you are only
occasionally wrong, from the other you might as well guess.

## The formal statement and proof

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

*Second reader's note on G102 (Local, 2026-10-06; chat L057).* Correct. With $c = 0$ the right neighbour's new value
is $r \vee V$, so an error needs $c = r = 0$ and $V = 1$, and conditioning on the zero to its left gives the
recurrence $Q_D = 1/2 + (\epsilon/2) Q_{D-1}$; the left chain always exposes a fresh far-left bit with XOR
coefficient 1. Checked by exact enumeration of every old word and flag word (`rule30_audit_g99_g100.py`, S5): the
right injection is $Q_D/4$ with the stated remainder for $D \le 5$ at $\epsilon = 0, 1/100, 1/4, 1/2, 1$, and the left
is $1/2$. At my measured rate $\epsilon = 0.01$ the bulk value is $0.12563$, which my measured $0.1281$ matches to
within one standard deviation (0.0032), as does the isolated $1/8$: the run could not tell them apart.
