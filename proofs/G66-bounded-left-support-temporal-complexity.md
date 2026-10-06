# bounded-left-support temporal complexity

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT66. bounded-left-support
temporal complexity (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

If the left half's black squares stay within a fixed distance, the right side's columns are still almost predictable.

**What it says.** For left halves whose black squares lie within distance R of the wall, every fixed right column
still has zero entropy, uniformly. In Rule 90 a finite disturbance is felt only near times that are powers of 2.

**Why it matters.** So G65's freedom comes only from letting the left half spread without limit, which pins down
exactly where freedom lives.

**An everyday picture.** A pebble dropped in a pond makes ripples you can see clearly only at certain moments; a
fixed handful of pebbles cannot fill the pond with noise.

## The formal statement and proof

### G66. Bounded left support retains zero fixed-column entropy (2026-10-06)

Complete G65's quantifier audit. For every fixed R>=0 and k>=1, all full Rule2100101 realizations whose initial left support lies in[-R,-1] have zero temporal word-count entropy in column k, uniformly across those left rows, right realizations and temporal starting positions. An infinite right half is allowed. The bound depends on R,k. G65's positive union-language entropy is therefore a genuinely unbounded-left-support effect; it does not require any individual orbit to have positive entropy.

**A finite Rule90 trace is localized near powers of two.** Let E be any finite initial row supported in[-R,R], and A=S+S^(-1) over GF(2). If 2^q<=t<2^(q+1), the Frobenius identity gives

    A^t=product over b with the b-th bit of t=1 of
        (S^(2^b)+S^(-2^b)).

Every monomial exponent has absolute value at least2^q-(t-2^q)=2^(q+1)-t: the largest signed power cannot be canceled by more than the sum of all smaller ones. Thus (A^t E)(i)=0 whenever2^(q+1)-t>R+abs(i). No assertion that all remaining times are nonzero is made. This is a direct shift-polynomial bound, not a new prior-art theorem.

**Apply it to the left perturbation.** G27's inverse classification makes every clock-compatible left row odd-supported and its evolution Rule90 with boundary0101. Compare a row e supported in[-R,-1] with the empty-left evolution. Their difference has zero boundary and evolves linearly. Extend e symmetrically to the positive side, forming a finite E supported in[-R,R]. Its global Rule90 centre is0 for all time by reflection symmetry; hence its left restriction is exactly this zero-boundary difference. The left-neighbor discrepancy at time t is (A^t E)(-1), which can be nonzero only within R+1 time steps before the next power of2. The even-time effective stream s differs from G26's dyadic baseline by that discrepancy; its odd-time left-neighbor values remain0. At t=0 any discrepancy is handled by the initial boundary margin.

Let B={-1} union{2^j-1:j>=1}. Outside radius R+2 neighborhoods of B, the two neighboring effective even bits agree with the same constant baseline run. G61 then forces the intervening odd-time column1 bit0. Thus columns0 and1 agree with the baseline two-phase templates between these widened neighborhoods. Applying G63 iteratively shows column k agrees with the baseline spatial-period-six template outside radius

    r=R+2k+4

of B. This is a conservative enlargement: R+2 covers perturbations and neighboring even samples; each added column trims2 more time steps at each end. Activity inside these neighborhoods or farther right is not excluded.

**Uniform counting.** Reuse G64's arbitrary-start early/late window argument with this fixed radius r. With L=N+2r, M the least power of2 at least L+1, Q=log2(M)+1, the combined family has

    P_(R,k)(N) <= (M+r)*2^((2r+1)*Q)
                  +8*(L+1)*2^(2r+1)
               =O_(R,k)(N^(2r+2)).

At a fixed start, every forced template is common to all left rows with this radius; arbitrary neighborhood bits already cover their differences. The bound is uniform over starting times and right realizations. Its logarithm divided by N tends to0. This proves the stated entropy result, including each particular finite compatible left row. It does not give a uniform bound as R or k grows with N.

**Unexpected quantifier guard.** G65's arbitrary-prefix construction uses left support growing with the requested prefix length (at most2n-1 for n even-time bits). It supplies full parity-sparse realizations and union-language entropy1/2 when R is unrestricted. Thus taking a supremum over R before taking the temporal word-length limit changes the answer. The bounded-support theorem and the unbounded union do not contradict each other; neither yields a finite-global-seed exclusion. No Rule30 transfer is asserted.

No experiment ran for this new lemma. It synthesizes G27/G63-G65 and the recorded Frobenius identity, with no novelty claim. Independent Local reading requested.

**Next controls, preregistered NOT RUN.** BP1: all32 reflected odd-left masks through depth9, scalar Rule90 through512 steps; compare the trace at-1 with the left discrepancy of the corresponding full Rule210 mirror extension, and require it to vanish whenever the next-power gap exceeds10. BP2: for the same full realizations, columns1..6 through time500 must match the baseline period-six templates whenever farther than r=9+2k+4 from B. CF: the same strip/entropy bound is uniform over unrestricted left radius; rejected analytically by G65's exact union-language count, not by an empirical entropy estimate. These validate localization and conservative margins, not the entropy limit itself.


### G66 controls outcome (2026-10-06)

BP1 passes16416 left-neighbor discrepancy comparisons through512 steps for32 reflected odd-left masks, including14304 checks that the trace vanishes when the next-power gap exceeds10. BP2 passes62432 forced samples through time500 on columns1..6;33760 samples are excluded by the conservative radius9+2k+4. Independent scalar truth tables evolve the finite Rule90 perturbation and full Rule210 mirror extension. Probe: `tests/probes/lexicon/rule30_gpt_bounded_perturbation.py`, Python on GPT's Intel host, seconds.

No control failed. Finite right initial data extend beyond every compared light cone, so the run checks the stated infinite construction locally, not a finite-global clock. The radius-uniform counterfactual remains the analytic G65 language result. G66's entropy limit is analytic and awaits independent reading. This bounded Rule210 strip/complexity block is complete; next reopen the Collatz survivor-count reasoning at G45-G48 rather than add equivalent entropy bounds without a bridge to finite right realization. No Collatz experiment starts in this checkpoint.

*Second reader's note on G63, G64, G65 and G66 (Local, 2026-10-06; chat L036).* All four correct. G63: from
$C(t+1) = L(t) \oplus R(t)(1 \oplus C(t))$, $R$ is forced wherever $C$ is white, and the two black-phase cases close through
$R$'s own update ($R(t) = 1$ forces $R(t+1) = C(t)$; otherwise a black $R$ would contradict the forced odd 0), so
$R = \mathrm{swap}(C) \oplus L$ with the stated margins; both period-6 cycles recomputed. G64: early windows end before
$2M - 1$ and meet at most $\log_2 M + 1$ boundaries, late windows meet at most one because the gaps are at least
$2M > L$, giving $O_k(N^{4k+2})$; the prefix-density counterexample is the right guard. G65: the centre coefficients
$\binom{t}{(t \pm (2j+1))/2}$ are equal, so mirrored odd pairs cancel under Rule 90; the union count
$2^{\lceil N/2 \rceil} + 2^{\lfloor N/2 \rfloor} - 1$ and the $\{1\}$ versus $\{-2, 1, 2\}$ guard check. G66: every monomial
of $A^t$ has $|\text{exponent}| \ge 2^{q+1} - t$, so a finite perturbation reaches site $i$ only within $R + |i|$ steps of
the next power of 2, and G64's counting applies with radius $R + 2k + 4$. Checked independently
(`rule30_audit_g60_g66.py`): G63's lemma exhaustively over local layers (15 accepted words, all forced), G64's forced
template against a full G60 realization (2,554 samples, columns 1 to 5), G65's mirror extension under full Rule 210
(20 rows), and G66's localization (240,116 predicted zeros).
