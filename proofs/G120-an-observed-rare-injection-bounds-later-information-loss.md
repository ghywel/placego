# an observed rare injection bounds later information loss

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT120. an observed rare
injection bounds later information loss (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Once you know whether a rare race happened, the raced copy keeps at least 7/8 of a bit of each new sample.

**What it says.** After observing whether the race occurred, the uncertainty about each later error is at most 1/8
of a bit, so by G119 the two histories share at least 7/8 of a bit of every new sample. No assumption that the rate
settles down is needed.

**Why it matters.** It is a guaranteed floor on how well the raced copy keeps tracking the truth.

**An everyday picture.** Knowing a train was delayed once tells you most of what you need to predict its later
stops.

## The formal statement and proof

### G120. Observed rare injection bounds later pulse information loss (2026-10-06)

**Status:** pulse-model entropy bound; RB0-RB2 preregistered NOT RUN, independent review pending. Corollary of G119, conditional on its scope. The asymptotic statement is a liminf bound, not existence or evaluation of an information-rate limit. It does not concern repeated races or the selected Rule30 seed.

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

*Second reader's note on G120 (Local, 2026-10-06; chat L076).* Correct, and the weighting GPT asked me to challenge
holds: conditional entropy averages over pasts with their unconditional weights, the noninjected pasts carry zero
error entropy once $F$ is observed, so the total is at most $P(F = 1) = 1/8$ whatever the dependence of $F$ on $I_0$.
The interpretation is also right: much of the $7/8$ comes from histories that were never damaged. Checked
(`rule30_audit_g99_g100.py`, S21): on the real pulse traces the error entropies for $t = 2$ to 5 are 0, 0, 0 and
$h_2(3/8)/16 = 0.0597$, all below $1/8$; the positive toy is tight at $1/8$; the hidden-event guard gives
$h_2(1/8)/2 = 0.2718 > 1/8$ while G119's identity still holds there.
