# the period-growth gap is an exponentially weighted stage-length condition

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT184. the period-growth gap
is an exponentially weighted stage-length condition (second-read by Local, 2026-10-07)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

How fast periods must grow along an edge history: stages that are long only in proportion to their period are not
enough.

**What it says.** Along a history the period stays fixed for a stretch, a stage, and then doubles. Divide each
stage's length by its period. Depth divided by the current period is then a running total that halves at each
doubling before the new stage's share is added. For the period to become small compared with the depth, that total
must grow without bound; stages whose length is a fixed multiple of their period leave it stuck.

**Why it matters.** It states gap 2 exactly, as a condition on stage lengths that can be checked, and shows which
easy hopes are not enough.

**An everyday picture.** Savings that are halved at every birthday: only deposits that keep outgrowing the halving
make the balance climb for ever.

## The formal statement and proof

### GPT G184 — Period-growth gap is an exponentially weighted stage-length condition (2026-10-07)

**Symbolic checkpoint, second reader pending; no run.** Fix one infinite admissible rooted history, with N_j the first node of least pair period2^j as in G165. Let ell_j=N_(j+1)-N_j be its spatial stage length, lambda_j=ell_j/2^j and R_j=N_j/2^j. G165's required sublinear period growth is exactly R_j->infinity. The entry recurrence becomes

    R_(j+1)=(R_j+lambda_j)/2,
    R_j=2^(-(j-J))*R_J + sum from i=J to j-1 of 2^(-(j-i))*lambda_i.

Thus the missing growth estimate is divergence of this exponentially weighted moving sum of normalized stage lengths. It is not merely divergence of absolute stage lengths, a large observed entry depth, or a geometric delay lower bound.

**Proof and useful sufficient condition.** N_(j+1)=N_j+ell_j gives the first identity after division by2^(j+1); induction gives the second. G165 already proves p_k=o(k) iff2^j/N_j->0, which is R_j->infinity. If lambda_j->infinity, then R_(j+1)>=lambda_j/2->infinity. More generally, for any fixed positive m and j>=J+m,

    R_j >= 2^(-m) * sum from i=j-m to j-1 of lambda_i.

Hence divergence of an unweighted sum over any fixed recent window of normalized stage lengths is sufficient. These are conditions to prove from compatibility, not estimates supplied here. Their constants and eventual thresholds may depend on the history, as G165 allows.

**Counterfactual: geometric delay alone is insufficient.** For a synthetic stage schedule with lambda_j=C>0 after J (choose integer C so ell_j=C*2^j are positive integers), the recurrence gives R_j=C+2^(-(j-J))*(R_J-C). Thus R_j tends to C rather than infinity, despite exponentially increasing absolute stage lengths and arbitrarily large initial R_J. Its period/depth ratio tends to1/C rather than0. This is a logical stage-schedule control, not a compatible Rule30 counterexample. It shows that a proof of ell_j>=c*2^j with fixed c would not by itself settle the growth target.

**Identified unexpected check: individual normalized stage lengths need not diverge.** In a synthetic integer schedule let lambda_j=1 at even j and lambda_j=j at odd j (after any finite prefix). Then R_j->infinity: if j-1 is odd, R_j>=(j-1)/2; if j-1 is even, the preceding odd term gives R_j>=(j-2)/4. Yet lambda_j remains1 at every even index. Therefore lambda_j->infinity is sufficient, not necessary; refuting that stronger condition would not refute period growth. The two-step recent-window sufficient condition covers this example. Conversely any finite prefix's contribution decays as2^(-(j-J)), so no finite delay record alone can force the limit.

**What the recorded depths say.** The certified unbranched small-cap prefixes give N_1=3,N_2=8,N_3=29,N_4=400, hence R_1=1.5,R_2=2,R_3=29/8,R_4=25. Their normalized completed stage lengths are lambda_1=5/2,lambda_2=21/4,lambda_3=371/8. These are existing G161/G165 and Local L115 records, not new measurements. The known period16 genuine branch at depth53208 preserves period16; it is NOT N_5. Later period16 branch examples likewise supply no certified period32 entry. No N_5 value or asymptotic stage-length estimate is inferred.

**Scope and next proof obligation.** The recurrence is elementary weighted summation applied to G165's reviewed dyadic stage structure; no novelty claim or new experiment. All controls here are algebraic synthetic schedules and explicitly lack Rule30 compatibility. A sufficient next lemma would bound actual normalized stage lengths from below by a quantity tending to infinity, or establish divergence of their recent-window sum on each admissible history. Genuine branch spacing from G159 does not imply this bound: same-period branches do not end the stage. GPT next examines constraints at consecutive odd zero-driver doubling events, reasoning first; no new gap-1 family or larger-period run is queued.

*Second reader's note on G184 (Local, 2026-10-07; chat L146).* Correct. Dividing $N_{j+1} = N_j + \ell_j$ by $2^{j+1}$
gives the recurrence, and unrolling it gives the closed form. Each weight $2^{-(j-i)}$ with $i \ge j - m$ is at least
$2^{-m}$ and the other terms are nonnegative, which gives the window bound. G165's criterion is $R_j \to \infty$ because
on stage $j$ the ratio $p_k/k$ peaks at entry, where it equals $1/R_j$. Checked (`rule30_audit_g99_g100.py`, S74). The
entries 3, 8, 29, 400 were recomputed from RQ3's reached graphs rather than copied: they are the first node of least
period $q$ at $q = 2, 4, 8$, and the node after the single $q = 8$ cap exit at depth 399. At every depth the reached
states are temporal rotations of one another, so these prefixes are unbranched, as stated. The reached graphs at
$q \le 8$ are acyclic, each with one sink (its cap exit), so no history stays at a period of 8 or less. $R_j$,
$\lambda_j$, the recurrence and the closed form hold exactly on these entries. The closed form and the window bound also
hold on 200 random nonnegative schedules. The constant schedule $\lambda = 3$ from $R = 100$ gives exactly $3 + 97/2^j$,
and the alternating schedule meets both of G184's bounds. Depth 53208 follows G2.3's convention (zero driver at 53207,
split at 53208). One point of scope: if a history's period stopped doubling, $N_j$ would be undefined from some $j$ on
and $p_k = o(k)$ would hold trivially. G184's "exactly $R_j \to \infty$" therefore presumes unbounded period; at
$q \le 8$ that presumption is now checked. One consequence the record already gives: the shared prefix keeps period 16
through the split, so $N_5 \ge 53{,}208$ on every history. Hence $\lambda_4 \ge 3{,}300$ and $R_5 \ge 1{,}662$, lower
bounds rather than a value of $N_5$.

**GPT scope clarification after L146 (2026-10-07; existing theorem, no run).** The unbounded-period premise on an infinite ROOTED history is already proved in G165's equivalent period-growth checkpoint, using G7/G156. For completeness, a pair at depth k has first backward zero-hit time k+1 under B; therefore two distinct depths cannot have the same pair. If all periods were bounded by a fixed dyadic Q, all pairs would lie in the finite set of4^Q Q-periodic binary pairs, contradicting this injectivity along an infinite history. Rotation classes strengthen the same argument but are not needed. Ambient B-cycles such as G156's period-two example do exist; they are excluded by rooted first-hit times, not by a global acyclicity assertion. Thus every infinite admissible rooted history has all dyadic entries N_j, and no additional bounded-period cyclic rooted case remains to classify. This settles the scope question, not the growth rate. From the shared period16 prefix, the conservative reviewed bound N_5>=53208 implies lambda_4>=(53208-400)/16=6601/2 and R_5>=53208/32=6651/4; neither is the unknown exact entry. These are finite lower bounds, not asymptotic estimates.

*Local's correction (2026-10-07, L149).* Accepted. The scope point in my note above was already settled in the record: G165 proves unbounded period on every infinite rooted history, because by G156 the pair at depth $k$ first hits zero backwards at time $k + 1$, so no pair repeats. S74's acyclicity at $q \le 8$ is a special case. I should have searched the record before calling it open.
