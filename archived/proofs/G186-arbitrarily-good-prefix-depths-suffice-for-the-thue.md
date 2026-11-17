# arbitrarily good prefix depths suffice for the Thue–Morse and recorded paperfolding reductions

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT186. arbitrarily good prefix depths
suffice for the Thue–Morse and recorded paperfolding reductions (second-read by Local, 2026-10-07)"; rebuild with
`python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this
file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

For the Thue–Morse and paperfolding cases, slow period growth only some of the time is enough.

**What it says.** Assume the timing budget of gap 1. Then to exclude Thue–Morse and the recorded paperfolding codes,
it is enough that the period is very small compared with the depth at infinitely many depths, not at all of them.
Local second-read it (L151).

**Why it matters.** It weakens what gap 2 has to prove. Neither this nor the budget is yet proved on the real
histories.

**An everyday picture.** A detective doesn't need fingerprints on every surface in the room, only that, however long
the search goes on, another clear print keeps turning up.

## The formal statement and proof

### GPT G186 — Arbitrarily good prefix depths suffice for the Thue–Morse reduction (2026-10-07)

**Conditional lemma, second-read by Local L151; reasoning only.** Fix one admissible rooted history and a fixed left-edge distance L. Let p(M) be its nondecreasing least common prefix period. Suppose its entire-prefix settling bound satisfies

    tau(M) <= gamma*M + A*p(M) + B,
    1 <= gamma < 3,  A >= 0,

with finite constants A,B along this history. Then liminf as M tends to infinity of p(M)/M equal to0 suffices for the unbounded Thue–Morse repeat contradiction of G2.4. A full limit p(M)/M ->0 is not required for this application. This supplies no actual growth or settling estimate for Rule30.

**Proof, including endpoint rounding.** Choose a fixed theta with 2<theta<6/gamma; then theta<6. Take integer depths n_s tending to infinity with p(n_s)/n_s ->0. Choose the largest nonnegative integer k_s for which M_s=ceil(theta*2^k_s)<=n_s, and put P_s=p(M_s). Such a k_s exists eventually and tends to infinity. Maximality gives

    n_s < ceil(2*theta*2^k_s) <= 2*theta*2^k_s + 1.

Monotonicity gives P_s<=p(n_s), hence P_s/2^k_s ->0. Also M_s=theta*2^k_s+O(1). The three G2.4 requirements now hold eventually: M_s<6*2^k_s because theta<6; tau(M_s)+P_s<=6*2^k_s because gamma*theta<6 and (A+1)*P_s+B+O(1)=o(2^k_s); and M_s>=L+2*2^k_s+2*P_s because theta-2>0. Substitution in G2.4's A⁗ inequality gives its one-cell contradiction at arbitrarily large scales. Every endpoint uses the settling bound and period from this SAME history. To exclude the code for every admissible left side, the assumptions must hold separately on every such history; constants may depend on the history.

**Stage-entry reformulation.** For the infinite rooted dyadic histories of G165, all entries N_j exist and p(M)=2^j for N_j<=M<N_(j+1). Write R_j=N_j/2^j as in G184. Then

    liminf_M p(M)/M = 0  if and only if  limsup_j R_j = infinity.

For the reverse implication, evaluate p(M)/M at entries N_j along an unbounded R_j subsequence. For the forward implication, a good depth n in stage j obeys N_(j+1)>n, so R_(j+1)>n/(2*p(n)); this is unbounded along the good-depth subsequence. Its stage indices tend to infinity because every fixed stage is finite. Thus, conditional on G165's uniform stage debt bound at slope gamma<3, unbounded R_j suffices for this Thue–Morse application: G165 supplies A=2*(C+1), with any fixed normalization offset absorbed in B. G165's stronger all-depth sublinear-period conclusion and G184's equivalence for a FULL limit remain unchanged.

**Independent margin control and counterfactual.** At gamma=5/2, theta=11/5 gives gamma*theta=11/2<6 and theta-2=1/5. Thus the time margin is half the dyadic scale and the endpoint margin is one fifth; both absorb any fixed B,L and vanishing relative period. If periods were not monotone, moving a good endpoint backwards could destroy its small period. The proof uses the reviewed predecessor-divisibility property, rather than assuming sparse depths align with repeat scales.

**Identified unexpected check: the weakened growth condition is strictly weaker.** This is an algebraic synthetic schedule, NOT a Rule30 history. Start N_1=2 and use the G184 recurrence R_(j+1)=(R_j+lambda_j)/2 with lambda_j=1 except at j_k=2^k, k>=1, where lambda_(j_k)=2^(2^(k-1)). Set each integer stage length to lambda_j*2^j. Immediately after a spike, R_(j_k+1)>=lambda_(j_k)/2, so limsup R_j=infinity. Before the next spike, at j=j_(k+1), the baseline contributes1 and the k earlier spikes contribute in total at most k*2^(-2^(k-1)): each contribution is bounded by 2^(3*j_h/2-j_(k+1))<=2^(-j_k/2). Hence R_(j_(k+1))->1. Consequently p(M)/M has liminf0 but does not tend to0, as evaluating at these latter entries shows. Unlike G184's previous oversized-deposit control, these deposits decay before the next spike.

**Prior record, scope and next intention.** G2.4 supplies the repeat criterion; G165 supplies conditional birth timing and monotone dyadic periods; G184 supplies the exact stage recurrence. This is an elementary subsequence application, with no literature novelty or computation claim. Neither the stage debt hypothesis nor even the weaker growth condition is proved on actual histories. No paperfolding claim or prize conclusion is added. Local: please second-read the endpoint selection, the equivalence and the strictness control; no run requested. GPT next seeks actual odd-zero hitting constraints strong enough to force unbounded R_j on each history.


**G186 continuation: the recorded paperfolding repeats also suffice (GPT, 2026-10-07; second reader pending, no run).** The initial G186 statement concerned only Thue–Morse. RULE30-PRIZE.md section8.59 also records paperfolding repeats with i=s, i'=3*s and ell=2*s-1 at dyadic scales s. Apply A⁗ to the same adjacent pair (-1,0) at distance L-1, with a=2*s, a'=6*s and n=2*ell=4*s-2. Its endpoint and one-cell contradiction requirements become

    M < 4*s,
    tau(M)+P <= 6*s,
    M >= L+2*s+2*P+2.

Indeed these give 4*s-2 <= L-1+6*s-M+2*P <= 4*s-3, impossible. The lost repeat symbol contributes the additional2 in the lower endpoint requirement; the later start contributes the stricter upper endpoint4*s, not6*s.

Under G186's SAME history-specific settling bound and liminf p(M)/M=0, choose theta with 2<theta<min(4,6/gamma). This interval is nonempty for 1<=gamma<3. The already proved endpoint selection gives M=ceil(theta*s), P/s->0 and arbitrarily large dyadic s. The strict positive margins 4-theta, 6-gamma*theta and theta-2 absorb all fixed offsets and the extra2. Thus the conditional sparse-depth criterion excludes the recorded paperfolding code as well as Thue–Morse. No new repeat theorem is proved here: the application uses exactly the recorded section8.59 repeats and A⁗, with the original timing/settled-band assumptions.

**Independent offset control and identified unexpected check.** Put L=1, s=8, P=1 and M=21, and assume tau(21)+1<=48. The upper endpoint is21<32, the lower threshold is1+16+2+2=21, and the A⁗ right side is1-1+48-21+2=29 whereas n=30, the desired one-cell contradiction. Reusing the Thue–Morse lower threshold would allow M=19, giving right side31 and NO contradiction. This literal arithmetic control retains the two-cell correction instead of treating the two repeat families as identical. No actual settling-time measurement is claimed by this assumed-timing control. The unresolved stage budget and actual unbounded stage-entry ratios remain necessary proof obligations for this route; no prize claim. Local: review the additional start-time and length offsets, no new job.

*Second reader's note on G186 (Local, 2026-10-07; chat L151).* Correct. The three requirements are exactly G2.4's
($M_k < 6 \cdot 2^k$, $\tau(M_k) + P_k \le 6 \cdot 2^k$, $M_k \ge L + 2^{k+1} + 2P_k$), and the third is also the upper
half of the A⁗ sandwich. Choosing $k$ maximal with $\lceil \theta 2^k \rceil \le n$ keeps the good depth below $2M + 1$,
since $n < 2\theta 2^k + 1$ and $M \ge \theta 2^k$. Monotone periods, from predecessor divisibility, then carry the
small period down to the endpoint, so $P/2^k \to 0$. The two margins are $6 - \gamma\theta$ for time and $\theta - 2$
for space, and both are fixed fractions of $2^k$ that absorb $A P + B$, $L$ and the ceiling. The equivalence follows
from $p/M = 1/R_j$ at entries and from $R_{j+1} > n/(2p(n))$ inside stage $j$. Checked (`rule30_audit_g99_g100.py`, S76)
at $\gamma = 5/2$, $\theta = 11/5$ on 300 random good depths. In the 134 cases where $P/2^k$ is small against $A$, $B$
and $L$, all three requirements and the sandwich hold with the settling bound taken at its worst. A slope with
$\gamma\theta = 6$ fails the time requirement, as it should. On the spike schedule the recurrence holds exactly, and
$R_{2^k + 1} \ge 2^{2^{k-1}}/2$ and $R_{2^{k+1}} \le 1 + k 2^{-2^{k-1}}$ for $k = 1$ to 4 ($R_{17} > 128$,
$R_{32} - 1 < 1/100$). So the weakened condition is strictly weaker, as stated. Beyond G186, the weakened condition has
an exact restatement: $\limsup R_j = \infty$ if and only if the normalized stage lengths $\lambda_j$ are unbounded,
since $\lambda_j/2 \le R_{j+1} \le \max(R_j, \lambda_j)$ (also checked in S76). The paperfolding continuation is also
correct. With §8.59's recorded repeat ($i = s$, $i' = 3s$, $\ell = 2s - 1$), A⁗ at $(-1, 0)$ has $a = 2s$, $a' = 6s$ and
$n = 4s - 2$. So $M < a' - a = 4s$, and the contradiction needs $M \ge L + 2s + 2P + 2$, the same offsets as BF4's
general form $L + 2i' - 2\ell$. S77 checks both thresholds exactly for $s = 2^3$ to $2^{20}$: one below the threshold
there is no contradiction, and $M = 4s$ breaks the first requirement. It also reproduces GPT's offset control (29
against 30 at $M = 21$, and 31 at the Thue–Morse threshold) and checks that $\theta = 11/5$ serves both families at
$\gamma = 5/2$. The quantifier stays per history, as in GC233. Rule 30's finite record cannot bear on a limsup.
