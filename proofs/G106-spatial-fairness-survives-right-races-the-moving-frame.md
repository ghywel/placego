# spatial fairness survives right races; the moving-frame change does not

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT106. spatial fairness
survives right races; the moving-frame change does not (second-read by Local, 2026-10-06)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The snapshots can stay statistically unchanged while motion through them changes.

**What it says.** In the infinite fair right-reading race model, an observer stepping left or staying has flip mean1/2. Stepping right has mean(3-eps)/(4-2eps), increasing from3/4 despite unchanged fair spatial rows.

**Why it matters.** Spatial invariance does not preserve the transition law. The moving-path count mean follows, but temporal independence, variance and ideal-history survival remain open. TF1 passes43648 cases and60 exact weighted means; colleague review is pending.

**An everyday picture.** Two films can have the same distribution of individual frames but different motion between them.

## The formal statement and proof

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

*Second reader's note on G106 (Local, 2026-10-06; chat L061).* Correct. The rightward flip is $A_{i+1}$, and a raced
site gives $A_j = x_j \vee A_{j+1}$ with $x_j$ fresh, so $U = (3 - \epsilon)/(4 - 2\epsilon)$; stays and left steps
keep a fresh far-left bit. Checked (`rule30_audit_g99_g100.py`, S9) by exact enumeration of old words and flags for
$D \le 4$ at $\epsilon = 0, 1/4, 1/2, 1$: means $1/2$, $1/2$ and $U_D$ with the stated remainder; the limit at
$\epsilon = 1/2$ is $5/6$. This is the cleanest answer yet to the owner's fuzz question: every snapshot stays fair,
and the fuzz shows only in the temporal field seen by an observer moving right.
