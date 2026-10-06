# selected critical-boundary losses

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT71. selected
critical-boundary losses (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The surviving count loses numbers only at the critical boundary, and the loss is set by whether the leftover number
is odd or even.

**What it says.** Each tick, every surviving pattern has two continuations, except those sitting exactly on the
survival boundary, which lose their even continuation. For real Collatz numbers, at the first step after the free
bits, which boundary numbers are lost is decided by whether F1's base-3 remainder is odd or even.

**Why it matters.** It locates exactly where real Collatz numbers can depart from fair coins in the count: an
odd-even imbalance on the boundary.

**An everyday picture.** A queue where only people standing on the line can be sent home, and a coin they carry
decides who.

## The formal statement and proof

### G71. First paid-bit discrepancy and the critical-boundary loss process (2026-10-06)

Resume the coefficient count of COLLATZ-PRIZE.md §1. G70 separates it from actual survival on sufficiently high intervals; this section concerns coefficient survival only. It specializes the already recorded parity bijection, G38's terminal recursion and G43's binary reader. No novelty claim, mixing estimate or tail-count theorem.

Let ell_t be the least nonnegative integer a with3^a>=2^t (ell_0=0). At t>0 equality of these powers is impossible, so this is also the coefficient-admissible endpoint threshold. Its increments are0 or1. Call step t to t+1 critical when ell_(t+1)=ell_t+1. Let V(t) count length-t words whose every prefix has coefficient at least1. At a critical step, let N(t) count those words with exactly ell_t ones; otherwise put N(t)=0. A child of such a critical-boundary word fails iff its new bit is0. All other admitted parents have two admitted children. Therefore

    V(t+1)=2*V(t)-N(t).

**The first step after the free bits.** Fix width w>=2 and m=w-1. Every admitted length-m word has one representative r in[0,2^m), and exactly one width-w start n=2^m+r. If it has a ones and terminal q=T^m(r), its actual state at the free-bit boundary is y=3^a+q. Since3^a is odd, its next parity is1 minus the parity of q.

Let C_w(t) count coefficient-surviving starts in[2^m,2^(m+1)) through horizon t. At a critical step m to m+1, write O(m) for the number of critical-boundary parents with q odd, and

    F(m)=sum over critical-boundary parents of (-1)^q
        =N(m)-2*O(m).

At a noncritical step put O(m)=F(m)=0. Only the parents counted by O(m) fail the next barrier, because q odd means y even. Thus

    C_w(w)=V(m)-O(m),
    2*C_w(w)-V(w)=F(m).

The coin benchmark2^(w-1)*P(w) equals V(w)/2, so the signed first-paid-bit discrepancy is exactly F(m)/2. At noncritical steps it is zero regardless of the terminal distribution. At critical steps it is the parity imbalance of one selected endpoint class, not the imbalance of the whole admitted ensemble. G43 expresses this reader as a weighted ternary spectrum; no cancellation for this selected class is established here.

**An exact selected-event loss process for later steps.** For any t, among the width-w coefficient survivors let E_w(t) count those with a_t=ell_t and even current state, provided the step is critical; otherwise set E_w(t)=0. Then

    C_w(t+1)=C_w(t)-E_w(t).

No claim of conditional fairness is made. When C_w(t)>0 define h_w(t)=E_w(t)/C_w(t), and put h_coin(t)=N(t)/(2*V(t)). With Q_w(t)=2^(w-1)*V(t)/2^t and R_w(t)=C_w(t)/Q_w(t),

    R_w(t+1)=R_w(t)*(1-h_w(t))/(1-h_coin(t)).

This formula includes a zero next count; logarithms may be taken only while both consecutive counts are positive. At t=m, R_w(m)=1 by the free-bit bijection. Hence bounded excess requires control of the accumulated selected-event hazard discrepancy after m. Noncritical steps contribute no loss on either side. This is an exact reduction of the desired count, not a proof of its boundedness or an independence model. It neither requires nor establishes G44's invalid all-cylinder comparison, and G42's resonances remain retained obstacles to generic Fourier arguments.

**Unexpected parity-sign guard.** At w2,m1 there is one admitted parent word1, r1,q2. Its width-two start is n3 with actual iterates3,5,8, so the next bit is1 and it survives the critical step. Thus C_2(2)=1,V(2)=1,F(1)=1, giving discrepancy+1/2. Counting q-even parents as losses instead would give C_2(2)=0 and the wrong sign. This exact two-step example checks the odd lift3^a; no experiment was needed to derive it. C_w is not asserted to equal the actual-survival count for every small width; G70's stated criterion governs that comparison.

**Next controls, preregistered NOT RUN.** BT1: m1..12, enumerate admitted parity words and their least representatives, compare the selected-class N/O/F formula with independently evolved width-(m+1) coefficient counts at horizon m+1. Predict exact equality, and zero discrepancy on every noncritical step; retain signed discrepancies on critical steps. BT2: widths2..10 through24 steps, direct trajectories and independent integer dynamic programming for V(t), checking the boundary-loss recurrence and exact rational ratio identity from the free-bit boundary onward. Retain zero counts and restrict probability/log identities to their stated domain. Counterfactual: q-even parents are the failing ones after the upper-half lift; must fail at width2. These are bounded controls, not a larger stopping scan or a uniform Fourier-transfer assertion. Independent Local reading requested.

### G71 controls outcome (2026-10-06)

BT1 passes507 admitted parents across m1..12. Retained rows(m,N,O,F,C) are(1,1,0,1,1),(2,0,0,0,1),(3,1,0,1,2),(4,2,1,0,2),(5,0,0,0,4),(6,3,0,3,8),(7,7,3,1,10),(8,0,0,0,19),(9,12,7,-2,31),(10,0,0,0,64),(11,30,14,2,114),(12,85,44,-3,182). First-paid-bit discrepancy F/2 has both signs; no one-sided bias law is inferred. Noncritical rows have F0 exactly.

BT2 passes171 boundary-loss recurrences,117 exact rational ratio identities and54 zero-parent steps at widths2..10 through24 steps. Zero counts are retained; no conditional probabilities or logarithms were taken on empty ensembles. The unexpected q-even-loss counterfactual fails at width2, whose direct count is1 rather than0. Probe: `tests/probes/prizes/collatz_gpt_boundary_loss.py`; Python on GPT's Intel host, under1 s. No control failed. These check identities, not a bound on accumulated hazard discrepancy. Next G72 examines admitted terminal multiplicity rather than assume a sign for the observed bias. Local's width40 run remains a separate claimed lane.

*Second reader's note on G71 (Local, 2026-10-06; chat L039).* Correct. An admitted parent with $a > \ell_t$, or any parent
at a noncritical step, has two admitted children, and a parent with $a = \ell_t$ at a critical step loses exactly its
0-child, so $V(t+1) = 2V(t) - N(t)$. At the free-bit boundary the width-$w$ start's state is $y = 3^a + q$, so its next
parity is $1 - (q \bmod 2)$; hence $C_w(w) = V(m) - O(m)$ and $2C_w(w) - V(w) = F(m)$. Later, $C_w(t+1) = C_w(t) - E_w(t)$,
and $V(t+1)/(2V(t)) = 1 - h_{\mathrm{coin}}(t)$ gives the ratio identity with $R_w(m) = 1$. The width-2 guard reproduces
($3 \to 5 \to 8$, discrepancy $+1/2$). Checked by direct trajectories (`collatz_audit_g67_g69.py`, G71 part): the
recurrence for $V$ to $T = 30$, and for every width 2 to 15 the free-bit equality, the first-paid-bit identity and the
loss process at every step to horizon 30.
