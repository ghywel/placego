# exact mutual information of six pulse samples

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT118. exact mutual
information of six pulse samples (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Exact six-sample mutual information separates conditional and unconditional coupling.

**What it says.** In the isolated-pulse model joint entropy is6+h2(1/4)/2+h2(3/8)/16 bits;mutual information is6 minus the same two uncertainty terms.

**Why it matters.** Each marginal is iid fair, yet hidden initial bits add joint uncertainty. Injection depends on the first observed bit, so unconditional injection entropy cannot replace conditional entropy. JI0-JI2 pass2048 words and exact count spectrum;reviewed by Local L074. No entropy-rate law.

**An everyday picture.** Two random-looking signals share most information, while an unseen input supplies the rest.

## The formal statement and proof

### G118. Exact unconditional mutual information of the first six pulse samples (2026-10-06)

**Status:** short-horizon entropy proof; JI0-JI2 preregistered NOT RUN, independent review pending. Complements G108's conditional coupling law using G116-G117. It is a pulse ensemble calculation, not an entropy rate, prize result or repeated-race law.

Let A=(I0,...,I5),B=(J0,...,J5) be ideal and noisy source traces in the fair initial-row isolated-pulse model. Both are iid fair by G97/G107, so H(A)=H(B)=6 bits. XOR-error history E is in bijection with B once A is given. Write h2(p) for binary entropy, with0*log2(0)=0. Then

    H(A,B)=6+h2(1/4)/2+h2(3/8)/16,
    MI(A;B)=6-h2(1/4)/2-h2(3/8)/16.

**Proof.** F=E1 is the001 injection indicator. Given I0=1, F=0; given I0=0, F is Bernoulli1/4. Fixing the nonnegative initial tail leaves the ideal samples I1..I5 successively triangular in five fresh negative initial bits, hence jointly uniform. Thus conditioning on those ideal samples adds no information about F or the hidden D of G117 beyond I0. In particular H(F|A)=h2(1/4)/2, not h2(1/8).

If F=0 the whole error history is zero. If F=1, its first five entries are0,1,0,1,I1 XOR I2 XOR I3. Only E5 remains to be specified. G117's independent D has rate3/8 even when the fifth ideal sample is observed: the fifth fresh negative pivot preserves the uniform conditional likelihood of the ideal prefix for every fixed right tail. Eight of the16 ideal quadruples have a D-dependent E5, each with entropy h2(3/8). Since P(F=1)=1/8, H(E5|F,A)=h2(3/8)/16. The first error identifies F, so entropy chain rule gives H(E|A)=H(F|A)+H(E5|F,A). Add H(A)=6 and subtract from H(A)+H(B)=12 to prove the formulas.

This gives unconditional MI strictly below6 bits, whereas G108 gives6 bits conditional on the nonpivot environment for the same horizon. In that conditional model the environment fixes the hidden inputs and the two traces are causally bijective. This is a statement about these two information quantities in this model, not a general monotonicity rule for conditional mutual information.

**Exact joint-count predictions.** On the2048 equally weighted11-bit initial words, each of64 ideal traces has32 preimages. For the32 traces with I0=1 all32 give one paired trace. For I0=0,24 are noninjections. For16 of those ideal traces the eight injected words give one deterministic-error trace; for the other16 they split5 and3 according to D. Thus the joint-support count histogram is{32:32,24:32,8:16,5:16,3:16}, with112 distinct pairs.

**JI0-JI2 preregistered NOT RUN.** JI0 checks all2048 words with independent literal-table/XOR-OR updates; both marginal histograms must contain64 traces32 times each and the joint histogram must match the prediction above. JI1 compares entropy from the integer count spectrum with the displayed binary-entropy expression and MI identity, tolerance1e-12 only for floating logarithms. JI2, unexpected conditioning guard:each ideal trace beginning0 must have8 injections among32, each beginning1 none; replacing H(F|A) by unconditional h2(1/8) must overestimate joint entropy. Publish before execution. No production job or asymptotic inference.

**JI0-JI2 outcome (2026-10-06 21:36 BST).** Executed after proof, predictions and instrument publication through8ced884. PASS:2048 words;both marginal histograms have64 traces32 times each. The112 joint pairs have exactly the predicted count histogram{32:32,24:32,8:16,5:16,3:16}. Entropy from those counts agrees with the closed expression within1e-12:joint6.465291187412 bits,mutual information5.534708812588 bits. The unexpected conditioning guard passes:every ideal trace starting0 has8 injections in32 histories;those starting1 have none. Substituting unconditional h2(1/8) overestimates joint entropy,refuting injection-independence. Independent review pending;no entropy-rate or repeated-race conclusion.


*Second reader's note on G118 (Local, 2026-10-06; chat L074).* Correct, including the two points GPT asked me to
challenge. The conditioning is right: injection needs $x(0) = 0$, $x(1) = 0$, $x(2) = 1$, so it is impossible when
$I_0 = 1$ and has probability $1/4$ when $I_0 = 0$; and $I_1$ to $I_5$ each carry a fresh pivot from the left, so for
every fixed right tail they are uniform and say nothing more about $F$ or the hidden $D$. Checked
(`rule30_audit_g99_g100.py`, S19) over all 2,048 words: both marginals 64 traces of 32; joint histogram
$\{32{:}\,32, 24{:}\,32, 8{:}\,16, 5{:}\,16, 3{:}\,16\}$ with 112 pairs; 8 injections in every ideal trace beginning 0
and none in those beginning 1; and the entropies from the counts match both formulas to $10^{-12}$, giving
$\mathrm{MI}(A; B) = 5.5347$ bits.
