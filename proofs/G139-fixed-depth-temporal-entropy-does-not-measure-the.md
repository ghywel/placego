# fixed-depth temporal entropy does not measure the initial row

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT139. fixed-depth temporal
entropy does not measure the initial row (second-read by Local, 2026-10-06)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A column can look perfectly simple over time while the starting row stays unresolved.

**What it says.** Each fixed column on the left reads only a limited stretch of the future, so for the powers-of-two
candidate every fixed column has almost no variety over time. That says nothing about whether the starting row is
finite, because the depth that matters keeps growing.

**Why it matters.** It separates two measurements that are easy to confuse: variety along time at one place, and the
shape of the starting row across space.

**An everyday picture.** Watching one window for a year tells you about that window, not about how long the street
is.

## The formal statement and proof

### G139. Fixed-depth temporal entropy does not measure the forced initial row (2026-10-06)

**Status and target.** Symbolic inverse-locality proof, independent review pending; no experiment. G138's low-depth audit is extended to every fixed depth. Prediction: a temporally sparse visible input creates temporally localized defects at each fixed depth, without controlling the entire spatial initial tail. Counterfactual: irregularity measured along the forced initial row would therefore imply positive temporal word-count entropy in a fixed column. The proof separates those axes. G64's earlier zero-entropy result concerned fixed right columns in a different Rule210 family; it is not imported as a Rule30 theorem.

Use G138's v_j(t) and inverse recurrence. For the constant-zero visible code, the background is b_j=1 at odd j and 0 at even j, for every j>=1. For any visible c define e_j(t)=v_j(t) XOR b_j. Then e_1(2s)=c_s and e_1(2s+1)=0. At depth two,

    e_2(t)=e_1(t+1) XOR e_1(t).

For j>=2, direct subtraction of the stationary background gives

    e_(j+1)(t)=e_j(t+1) XOR e_j(t)*(1-e_(j-1)(t))    when j is odd,
    e_(j+1)(t)=e_j(t+1) XOR (1-e_j(t))*e_(j-1)(t)    when j is even.

Indeed adjacent background bits are opposite. Their perturbed OR differs from one by e_j*(1-e_(j-1)) in the odd case and (1-e_j)*e_(j-1) in the even case. The temporal advance e_j(t+1) remains present; this is not an autonomous elementary rule for the defect field.

**All-depth locality.** By induction, e_j(t) is determined by the samples of e_1 on [t,t+j-1]. If all those samples vanish, e_j(t)=0. The base cases j=1,2 are explicit; at the next depth the two e_j terms use [t,t+j] and the shallower term uses a subinterval, and zero maps to zero in both displayed formulas. For the dyadic c=d of G137, the possible defect times at depth j therefore lie in

    union over k>=0 of [2^(k+1)-j+1, 2^(k+1)], intersected with t>=0.

This is an upper support bound, not equality. Outside these backward neighborhoods the forced column is exactly its checkerboard background value. It does not require linearizing away a nonlinear interaction.

**Temporal word bound.** Let P_c(n) count distinct length-n factors of c. A length-m time factor of v_j starting at u is determined by u modulo two and at most m+j consecutive visible symbols: the inverse locality spans physical times [u,u+m+j-2], and e_1 inserts a zero between visible symbols. Padding the visible window if needed gives

    P_(v_j)(m) <= 2*P_c(m+j).

The same reasoning jointly bounds a temporal vector of the first J columns by 2*P_c(m+J). Thus zero word-count entropy of c implies zero temporal word-count entropy at every fixed depth, and in every fixed finite left window. For d or its complement, G137 gives the explicit bound P_(v_j)(m)<=4(m+j)+2. This is not a uniform statement when the observed depth grows with m.

**Unexpected spatial-tail guard.** To evaluate v_j(0), the determining window length grows with j. Once j>=3, the first dyadic pulse at physical time 2 lies inside that window for every further j. The support lemma therefore does not force e_j(0) to vanish at large j. Nor may the fixed-j entropy limit be taken with j growing. G136's arbitrary-prefix fitting guard is another exact illustration of why unbounded recoding windows evade fixed-width control. These are the identified independent quantifier checks. Finite initial-row measurements described as coin-like are compatible with the proved zero temporal entropy; they concern different axes and do not supply an entropy theorem in either direction.

**Remaining obligation.** This characterizes fixed-depth temporal behavior, but neither proves nor disproves eventual zero support of the forced initial row. An all-depth spatial statement is still required: an explicit infinite family of v_j(0)=1, or another invariant preventing a zero tail. Full right-half realizability and a finite global Rule30 seed remain additional questions. No computational job duplicates Local's dyadic initial-row probe.

*Second reader's note on G138 and G139 (Local, 2026-10-06; chat L092).* Both correct. G138's five even/odd pairs
follow from the wall's two conditions and the inverse recurrence; G139's background is stationary and alternating in
depth, the defect field obeys the two displayed recurrences, and a defect at depth $j$ needs a visible pulse in
$[t, t + j - 1]$. Checked (`rule30_audit_g99_g100.py`, S35) by direct column computation: the five pairs on 100
random visible words; the dyadic initial cells $1, 0, 0, 0, 1$; both defect recurrences and the locality for depths
to 12; the dyadic defects at depths to 30 inside the stated backward neighbourhoods; temporal factor counts at most
$4(m + j) + 2$ for $j \le 10$, $m \le 30$. G139's quantifier point also qualifies my L091: the dyadic word's spatial
row looks coin-like while every fixed-depth column has zero word entropy, and a zero tail beyond the measured depth
is not excluded by that measurement.
