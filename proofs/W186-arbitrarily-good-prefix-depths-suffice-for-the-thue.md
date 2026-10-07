# Arbitrarily good prefix depths suffice for the Thue–Morse reduction

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "GPT G186 — Arbitrarily good
prefix depths suffice for the Thue–Morse reduction (2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

For this repeat contradiction, occasional sufficiently slow period growth is enough.

**What it says.** Assuming a settling bound with slope below three and an error proportional to period, arbitrarily good prefix depths suffice for the Thue–Morse reduction. Nondecreasing periods let each good endpoint move back to a suitable repeat scale.

**Why it matters.** The required stage-entry ratio need only be unbounded, rather than tend to infinity. Both this weaker growth statement and the settling budget remain unproved on actual histories; the lemma awaits Local review.

**An everyday picture.** A contradiction needs arbitrarily large usable windows. It does not need every later window to be usable.

## The formal statement and proof

**Conditional lemma, second reader pending; reasoning only.** Fix one admissible rooted history and a fixed left-edge distance L. Let p(M) be its nondecreasing least common prefix period. Suppose its entire-prefix settling bound satisfies

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
