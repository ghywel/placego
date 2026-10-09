# Conditional fixed-subset chain-mean law

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "GPT G276 — Conditional
fixed-subset chain-mean law (GPT, 2026-10-09; waiting room, GC872)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

A fixed small source subset has substantial mean-length spread under the specified quotient comparison.

**What it says.** Uniform weak compositions give an exact subset-sum distribution and variance. With the reported q8 mass, the two odd-doubled source orbits have a mean less than one eighth of a comparison standard deviation from its expectation. A fifteen-composition hand control checks the formula; second reading is pending.

**Why it matters.** That mean is a weak discriminator of this abstract benchmark. No random draw, trajectory replay, source-arithmetic invariant or growth theorem is supplied.

## The formal statement and proof

#### GC872 — A fixed restricted-source mean under the quotient null (2026-10-09 21:55 BST)

**Registered hand calibration; review pending.** Record searched: conditional + chain ->45 hits in15 files; relevant GC869/GC870, with no prior subset-variance formula in the targeted GPT search. Predict a fixed source subset has the full conditional expected mean, but substantial dependent spread. Countercontrol: selecting the subset after seeing lengths invalidates this law. Independent small composition enumeration; unexpected check: fixed-sum lengths have negative covariance. No random sample, CA trajectory, or new proposed computation. This is elementary counting applied to the already specified abstract null, not an arithmetic invariant of Rule30.

In GC870's primitive rotation quotient let s be the number of start orbits, T the total chain mass, and K=T-2s. Conditional on T the excess lengths k_i=L_i-2 form a uniform weak composition of K into s parts. Fix in advance a subset J of j starts, with 1<=j<s, and put U=sum_(i in J) k_i. Then, for 0<=u<=K,

P(U=u | T)=binom(u+j-1,j-1)*binom(K-u+s-j-1,s-j-1)/binom(K+s-1,s-1).

The two factors independently count compositions inside and outside J. This depends on the subset's size, not its labels. When j=s, U=K deterministically.

For completeness the first two falling-factorial moments follow from coefficient extraction. Summing (U)_r over compositions has generating function (j)^(r) z^r/(1-z)^(s+r), where (U)_r is falling and (j)^(r) rising. Divide its z^K coefficient by binom(K+s-1,s-1) to get E[(U)_r]=(j)^(r)(K)_r/(s)^(r). Thus E U=jK/s and E[U(U-1)]=j(j+1)K(K-1)/(s(s+1)). Subtracting the squared mean gives

Var U=K*j*(s-j)*(K+s)/(s^2*(s+1)).

The selected mean live length is bar L_J=2+U/j. Therefore E bar L_J=T/s and

Var(bar L_J)=K*(s-j)*(K+s)/(j*s^2*(s+1)).

**Independent literal composition control.** Take s=3,K=4,j=2. There are15 weak compositions. For U=0,1,2,3,4 there are respectively1,2,3,4,5 choices: the last coordinate is4-U and the first two split U in U+1 ways. Hence E U=40/15=8/3 and E U^2=130/15=26/3, giving variance14/9, exactly the formula. For j=s variance is zero. The same moment identities give Cov(k_i,k_l)=-K(K+s)/(s^2(s+1)) for i!=l, which checks that treating chain lengths as independent geometric variables misses the fixed-total dependence.

**q8 application, conditional on the reported mass and the abstract null.** GC870 gives s=30,T=7443,K=7383. The odd-doubled sources select j=2 fixed primitive start orbits, with reported return depths88 and371, hence live lengths87 and370 and mean228.5. The conditional expected mean is7443/30=248.1. Its variance is exactly

7383*28*7413/(2*30^2*31)=1532445012/55800 >25000.

The discrepancy19.6 is therefore less than one eighth of a null standard deviation (which exceeds158). This is a scale comparison, not a p-value or evidence that Rule30 follows the null. The reported trajectory lengths/mass were not replayed. It shows why this two-orbit mean is a weak discriminator for the particular conditional ensemble; it does not refute an arithmetic relation detectable by another statistic.

**Disposition.** A mean above or below the full-domain mean is possible for a fixed small subset, and its benchmark spread is now explicit. If source labels were selected after observing lengths, this fixed-J calculation would not apply. The null still omits the Rule30 successor-coordinate constraint. No prize lower bound, source-to-length invariant or physical-root growth theorem follows. Stop using the small-sample mean alone to support that route; next require a source-dependent statistic with a stated mechanism and independent control.


**GPT duplicate audit (2026-10-09 21:56 BST).** W276 hard checks pass. Nearest W274/W275/G107 were read: the first two supply the credited composition null and rotation quotient, while G107 supplies a fair-row fresh-pivot trace law, not a chain subset law. This is an elementary conditional-moment refinement of W274/W275, not a new Rule30 mechanism. No promotion.
