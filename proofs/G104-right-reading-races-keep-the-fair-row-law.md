# right-reading races keep the fair row law; left-reading races change pairs

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT104. right-reading races
keep the fair row law; left-reading races change pairs (second-read by Local, 2026-10-06)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

One race direction preserves fair spatial rows; the other can hide changed pairs behind fair density.

**What it says.** The infinite right-reading model preserves the fair product law via a conditional block inverse. On a fair input row, the left-reading model retains density1/2 but gives adjacent disagreement1/2+eps/4.

**Why it matters.** It earns a right-bulk extension of the injection calculation to later noisy rows, while leaving ideal-history disagreement separate. The left result is first-step only. No exact finite-ring or selected-seed law is claimed. Controls pass on2720 right cases,10880 left cases and48 exact weighted moments; independent review remains pending.

**An everyday picture.** Two patterns can contain the same number of black cells but arrange neighbouring cells differently.

## The formal statement and proof

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



**OM1-OM2 outcome (2026-10-06 20:07 BST).** Executed after predictions and instrument publication through8753ab0. OM1 PASS: 2720 right input cases, every fixed-tail/flag block map bijective and independently inverted. OM2 PASS: 10880 left input cases and48 exact rational weighted moments. Both densities are1/2, but left adjacent disagreement is1/2+eps/4 as predicted. The eps1 checks are finite anchored endpoint controls; the infinite terminating-chain theorem excludes eps1. These controls support the spatial-law proof, not ideal/noisy history survival or exact cyclic invariance. Local independently reviewed it in L059.


*Second reader's note on G104 (Local, 2026-10-06; chat L059).* Correct. With the tail at sites $\ge b$ fixed, the
right-reading recursion inverts uniquely from right to left, so fair rows stay fair under independent flags; the
left-reading chain exposes a fresh far-left bit (density $1/2$), while a raced right cell makes the pair XOR
$x_{i+1} \vee x_{i+2}$. Checked (`rule30_audit_g99_g100.py`, S7): a bijection for every flag pattern and tail at block
widths up to 5; on a fair first row, left races give density $1/2$ and adjacent disagreement $1/2, 9/16, 5/8, 3/4$
at $\epsilon = 0, 1/4, 1/2, 1$, which is $1/2 + \epsilon/4$. This fits my race run (right-race rows stayed at 1/2 in
density and pairs; the left-race pair bias $\epsilon/4 \le 0.00025$ was below its resolution) and sharpens its
summary: one direction of fuzz leaves the row law exactly intact, the other leaves a fingerprint in the pairs.
