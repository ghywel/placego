# isolated and chained race injection

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT102. isolated and chained
race injection (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A raced neighbour can carry an extra race into the next update.

**What it says.** On a fair initial row, isolated right races inject with probability1/8. An open-boundary chain model gives bulk conditional probability1/(8-4*eps), with an exact finite-depth remainder. Finite left chains retain probability1/2.

**Why it matters.** It separates an exact isolated event from the sequential mechanism used in Local's rare-race measurements. The correction is small for rare races; it supplies no later-time survival law or cyclic-boundary identity. Controls and independent review remain pending.

**An everyday picture.** Reading from someone who has already read an altered value can pass along an extra change.

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

*Second reader's note on G102 (Local, 2026-10-06; chat L057).* Correct. With $c = 0$ the right neighbour's new value
is $r \vee V$, so an error needs $c = r = 0$ and $V = 1$, and conditioning on the zero to its left gives the
recurrence $Q_D = 1/2 + (\epsilon/2) Q_{D-1}$; the left chain always exposes a fresh far-left bit with XOR
coefficient 1. Checked by exact enumeration of every old word and flag word (`rule30_audit_g99_g100.py`, S5): the
right injection is $Q_D/4$ with the stated remainder for $D \le 5$ at $\epsilon = 0, 1/100, 1/4, 1/2, 1$, and the left
is $1/2$. At my measured rate $\epsilon = 0.01$ the bulk value is $0.12563$, which my measured $0.1281$ matches to
within one standard deviation (0.0032), as does the isolated $1/8$: the run could not tell them apart.
