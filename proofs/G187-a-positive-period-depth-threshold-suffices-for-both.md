# a positive period/depth threshold suffices for both repeat reductions

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT187. a positive
period/depth threshold suffices for both repeat reductions (second-read by Local, 2026-10-07)"; rebuild with
`python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this
file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The conditional repeat argument needs a sufficiently small ratio, not a vanishing one.

**What it says.** A fixed settling budget determines a positive threshold for period divided by depth. Infinitely many prefixes below that threshold suffice for the Thue–Morse and recorded paperfolding contradictions. Aligning the repeat scale with the dyadic period sharpens the sufficient threshold.

**Why it matters.** This complements G186 by weakening the growth target for a specified settling budget. Local L152 verified the conditional reduction; actual histories have not been shown to meet its two asymptotic obligations.

**An everyday picture.** A usable window needs enough room for its repeating pattern. The pattern need not become negligible; it can occupy a sufficiently small fixed share.

## The formal statement and proof

### GPT G187 — A positive period/depth threshold suffices for both repeat reductions (2026-10-07)

**Conditional quantitative lemma, second-read by Local L152; no GPT run.** Fix a left-edge distance L and one admissible rooted history with nondecreasing common prefix period p(M). Suppose its entire-prefix settling bound is

    tau(M) <= gamma*M+A*p(M)+B,
    1 <= gamma < 3, A >= 0,

with finite constants A,B on that history. Define

    delta = (3-gamma)/(2*gamma+2*A+8).

Then liminf p(M)/M < delta suffices for G2.4's unbounded Thue–Morse repeat contradiction. For the recorded paperfolding repeats, the sufficient condition is liminf p(M)/M < min(delta,1/6). In G165's application A=2*(C+1)>=2, so delta<=1/7<1/6 and the SAME delta suffices for both codes. This complements G186: for a specified budget it weakens the sufficient growth condition. G186 remains useful when only existence of a finite budget constant is known. Neither lemma proves an actual budget or period estimate.

**Endpoint construction and proof.** Choose a number r strictly between the liminf and the relevant threshold. Along arbitrarily large integer depths n, let q=p(n)<=r*n. Put D=L for Thue–Morse and D=L+2 for paperfolding, and choose the largest dyadic s for which 2*s<=n-2*q-D. Such a scale exists eventually. Then

    s > (n-2*q-D)/4,
    M = 2*s+2*q+D <= n,
    P = p(M) <= q.

Thus s tends to infinity, and limsup along these chosen depths of q/s is at most 4*r/(1-2*r). Direct rearrangement shows

    r < delta  iff  4*r/(1-2*r) < (6-2*gamma)/(2*gamma+A+1).

Consequently

    tau(M)+P <= 2*gamma*s+(2*gamma+A+1)*q+gamma*D+B < 6*s

eventually, by a strict linear margin in s. For Thue–Morse, r<delta<=1/5<1/4 implies q/s<2 eventually, hence M<6*s. For paperfolding, r<1/6 implies q/s<1 eventually, hence M<4*s. All fixed D and B are absorbed by those strict margins.

For Thue–Morse, the G2.4 A⁗ right side is at most L-1+6*s-M+2*q=4*s-1, below its repeat-run length4*s. For paperfolding the same expression is4*s-3, below repeat-run length4*s-2. Both contradictions use exactly the repeats and timing hypotheses already recorded in G2.4 and G186's section8.59 continuation. To exclude either code for every admissible left side, this quantitative condition and the settling budget must hold separately on every such history, with history-dependent constants allowed.

**Exact dyadic stage interpretation.** In G165's rooted stage structure the last depth m_j=N_(j+1)-1 minimizes p(M)/M within stage j. Its value is

    p(m_j)/m_j = 1/(2*R_(j+1)-2^(-j)).

Every stage is finite and its index tends to infinity with depth. Thus taking the liminf of these stage minima gives the exact extended-real identity

    liminf_M p(M)/M = 1/(2*limsup_j R_j),

with 1/infinity=0 and 1/0=infinity. The vanishing subtraction2^(-j) does not affect the denominator's limsup; inversion exchanges positive limsup and liminf, including these limiting cases. Hence the displayed quantitative condition is equivalent to limsup R_j>1/(2*delta). The factor2 comes from using the END of a stage, just before the next doubling, rather than its entry. For G165 at gamma=5/2 and C=1, A=4 and delta=1/42. Entry ratios above21 by a fixed margin at arbitrarily large indices therefore suffice for BOTH repeat applications, conditional on that stage budget. No such actual asymptotic statement is established.

**Independent integer control.** Hypothetically take L=1, B=0, gamma=5/2, A=4, n=1000 and q=16. For paperfolding D=3; the selected s is256 and M=547. The assumed bound gives tau(M)+P<=1447.5<1536=6*s, and M<1024=4*s. The A⁗ right side is at most1021 against repeat-run length1022. The same endpoint also works for Thue–Morse, whose run length is1024. This verifies the arithmetic under the stated assumptions; it is NOT a settling measurement or a certified C=1 budget on a Rule30 history.

**Identified unexpected strictness/control check.** If q/s equals (6-2*gamma)/(2*gamma+A+1), the scale-dependent time margin vanishes. A positive gamma*D+B then prevents the required timing inequality: this argument cannot replace its strict threshold by a non-strict one. Moreover the synthetic schedule N_j=25*2^j has constant R_j=25 and integer stage lengths25*2^j; it satisfies the gamma=5/2,C=1 entry threshold while p(N_j)/N_j=1/25 never tends to0. Its stage-end ratios tend to1/50. At period16, the entry depth400 has ratio1/25 above1/42, but the last stage depth799 has ratio16/799 below1/42. Thus G186's unbounded-ratio condition is sufficient but not necessary for the conditional application. This schedule has no asserted Rule30 compatibility.

**Prior record and next intention.** This is a quantitative endpoint selection using reviewed G165 timing, G184 stage notation and the pending G186 repeat applications; no novelty or computation claim. A finite large entry such as the conservative N_5 lower bound does not establish arbitrarily many useful scales. The actual target can now be a history-specific positive period/depth threshold tied to its stage-debt constant, rather than unbounded R alone. Both linked obligations remain open. Local: please second-read the threshold algebra and scope, together with G186; no run requested. GPT next examines what actual odd-zero hitting constraints could maintain or recurrently recover such a threshold.


**G187 continuation: align the repeat scale with the dyadic period (GPT, 2026-10-07; second reader pending, no run).** The general sparse-depth threshold is sufficient but can lose room by treating periods as arbitrary integers. In G165's actual stage structure, let q=2^j and choose a FIXED power of two K with

    K > (2*gamma+A+1)/(6-2*gamma).

For the paperfolding application also require K>1. With G165's A=2*(C+1)>=2 and gamma>=1, the displayed fraction is at least5/4, so its smallest admissible dyadic K automatically meets this additional requirement. Then

    limsup_j R_j > K+1

suffices for both repeat contradictions, conditional on that same history's settling budget. At infinitely many stages the next entry obeys N_(j+1)>2*(K+1)*q+D, where D=L for Thue–Morse or L+2 for paperfolding, because the limsup inequality has a fixed positive margin and q tends to infinity. Set s=K*q (a valid dyadic repeat scale) and M=2*(K+1)*q+D. Since M<N_(j+1), its common prefix period P is at most q, whether M falls in the q-stage or an earlier stage. The settling bound gives

    tau(M)+P <= [2*gamma*(K+1)+A+1]*q+gamma*D+B < 6*K*q = 6*s

eventually. The strict coefficient gap is (6-2*gamma)*K-(2*gamma+A+1)>0. Also M<4*s eventually when K>1, hence the paperfolding upper endpoint holds; this also implies the Thue–Morse upper endpoint M<6*s. Both lower endpoints and the one-cell contradictions follow from the same M=2*s+2*q+D construction in G187. This proves the claim without assuming liminf period/depth zero, or measuring any new stage length.

**Independent coefficient control and identified unexpected comparison.** For the hypothetical gamma=5/2,C=1 budget, A=4 and the coefficient fraction is10. Choose K=16; the sufficient entry threshold is now17 rather than G187's general21. At q=16,L=1,B=0 the paperfolding endpoint is again M=547,s=256, and the timing margin is6*q-7.5=88.5, agreeing with the earlier literal control. A synthetic constant schedule N_j=18*2^j has R_j=18 and stage-end period/depth ratios tending to1/36. It passes this new threshold but fails the earlier sufficient condition liminf period/depth<1/42. Thus the improvement is strict as a reduction; no Rule30 compatibility or actual C=1 budget is asserted. Choosing K=8 instead would give a negative coefficient gap8-10=-2, so the next smaller dyadic scale is not licensed by this bound. If the fraction itself is a power of two, equality still leaves no positive margin for offsets: choose the next power. No optimality claim is made for other endpoint strategies or stronger timing information.

**Handoff.** This is a refinement of the same pending G187 proof, not a new growth estimate or a reopened gap-1 family. Local: include the dyadic scale choice and the earlier-stage prefix-period guard in the second read; no job requested. The remaining actual obligation is a recurrent entry-ratio margin linked to the history's uniform stage-debt constant. Finite large entries alone still supply no such recurrence.

*Second reader's note on G187 (Local, 2026-10-07; chat L152).* Correct. With $M = 2s + 2q + D$ the third G2.4
requirement holds with $q$ in place of $P$, and $P \le q$ by monotone periods. The time requirement then reduces to
$(2\gamma + A + 1) q < (6 - 2\gamma) s$, up to the fixed $\gamma D + B$. Taking $s$ maximal and dyadic gives $q/s$ at
most $4r/(1 - 2r)$ in the limit. Cross-multiplying, $4r/(1 - 2r) < (6 - 2\gamma)/(2\gamma + A + 1)$ is
$r(4\gamma + 4A + 16) < 6 - 2\gamma$, which is $r < \delta$. The two codes differ only in $D$, and in paperfolding's cap
$M < 4s$, which $r < 1/6$ secures; $\delta \le 1/7$ once $A \ge 2$. Within a stage $p/M$ falls until the last depth,
where it equals $1/(2R_{j+1} - 2^{-j})$, so the liminf is $1/(2 \limsup R_j)$. Checked (`rule30_audit_g99_g100.py`,
S78). The equivalence holds on a rational grid. On 400 random depths the construction reaches both contradictions
whenever $r < \delta$ (800 of 800), and at $r = 3\delta$ its time margin fails (200 of 200). S78 also covers GPT's
integer control, the strictness case, the stage-end identity on random schedules and the $25 \cdot 2^j$ schedule.
Against the record, at $\gamma = 5/2$ and $C = 1$ ($\delta = 1/42$, so entries above 21): RC2's exact finite budget, a
debt of 7 at $q = 8$ (S72), lies within $Cq$ with $C = 1$ through period 8. The recorded entry $R_4 = 25$ and the bound
$R_5 \ge 1{,}662$ both exceed 21, and the stage ends $8/399$ and at most $16/53{,}207$ lie below $1/42$. That is finite
evidence about two scales and proves nothing about arbitrarily large ones, as G187 says. The dyadic refinement is also
correct. With $K$ the least power of two above $(2\gamma + A + 1)/(6 - 2\gamma)$, the endpoint $s = Kq$,
$M = 2s + 2q + D$ lies before the next entry, so $P \le q$, and the coefficient gap $(6 - 2\gamma)K - (2\gamma + A + 1)$
is positive while at $K/2$ it is not. Since the fraction is at least 5/4 once $A \ge 2$, $K \ge 2$ gives paperfolding's
$M < 4s$ (S79, with GPT's control: fraction 10, $K = 16$, threshold 17, margin 88.5). At $C = 1$ the record's $R_4 = 25$
clears this threshold too.
