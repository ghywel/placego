# Unbounded formal ceilings and residue-count rounding

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT46. Unbounded formal
ceilings and residue-count rounding"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this
summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Those height limits can be as large as you like, because powers of 3 sometimes come very close to powers of 2.

**What it says.** For patterns of k odd steps followed by just enough even steps to dip below 1, the ceiling can be
arbitrarily large. Powers of 3 now and then fall just short of a power of 2, because log2(3) is irrational. GPT also
corrected a rounding short cut in counting.

**Why it matters.** It rules out a uniform bound on all ceilings, so any control of the exceptions has to come from
finer arithmetic (G69 supplies it).

**An everyday picture.** Two clocks with unrelated periods: now and then their hands almost line up, and the near
misses can be as close as you like.

## The formal statement and proof

**Where:** RULE30-GPT.md G46, 2026-10-06; copied verbatim. **Bears on:** PERIOD-TWO.md §7 question9. **Status:** analytic argument, second-read by Local, 2026-10-06 (note below); GPT's KC controls preregistered and not run at publication. G45's controls passed and its argument was independently audited by Local L012.

### G46 theorem and proof: the formal ceilings are unbounded

For k>=1 take the word consisting of k ones followed by j-k zeros, where j is the unique integer with2^(j-1)<3^k<2^j. This is j=ceil(k*log2(3)). Every proper prefix has coefficient above1, and the final prefix is deficient. After the first k odd steps the affine intercept is3^k-2^k, unchanged by the following even steps. Thus G45's ceiling for this word is exactly

    K_k = floor((3^k-2^k)/(2^j-3^k)).

These ceilings are unbounded. Put alpha=log2(3), irrational by unique prime factorisation, and delta_k=ceil(k*alpha)-k*alpha. There are arbitrarily large k with delta_k arbitrarily close to0 from above. Here is an elementary one-sided approximation argument. Pigeonholing the fractional parts of0,alpha,...,N*alpha gives a positive q whose multiple is within1/N of an integer. If its fractional part is near1, q already works. Otherwise write its fractional part as eta with0<eta<1/N and take m=floor(1/eta). Irrationality implies m*eta<1 and1-m*eta<eta, so k=m*q has fractional part within eta of1. Taking N arbitrarily large produces delta_k tending to0. Such k must tend to infinity, because each fixed k has a nonzero gap.

The ratio inside the floor is

    (1-(2/3)^k)/(2^delta_k-1).

Along those k its numerator tends to1 and its denominator tends to0 positively, so K_k tends to infinity. In particular the maximum finite word ceiling over word lengths is not O(1). This argument establishes unboundedness, not a polynomial upper bound in j. It uses the elementary affine/parity formula and irrational approximation; no novelty claim.

**Residue-placement boundary.** A ceiling K bounds possible starts in[1,K], but a single realizing residue class modulo2^T has count at mostfloor(K/2^T)+1, not necessarily K/2^T. For word1010, T=4,K=1 and residue1, that count is1 whereas K/2^T=1/16. Thus multiplying a small ceiling by a density1/2^T can give a false upper bound without controlling which residues occupy the short interval. Unbounded K does not imply unbounded actual-survival exceptions: realizing residues may exceed their ceilings. Conversely, a polynomial upper bound on K alone would not remove the additive rounding term. This is a correction to a possible counting shortcut, not a disagreement with G45's exact formula or the observed large-width coefficient agreement.

*Second reader's note on G46 (Local, 2026-10-06; chat L014).* Correct. Only the final prefix of $1^k 0^{j-k}$ is
deficient ($2^{k+i} \le 2^{j-1} < 3^k$ for $k + i < j$); the intercept after $k$ odd steps is
$\sum_{t<k} 3^{k-1-t} 2^t = 3^k - 2^k$; the ratio is $(1 - (2/3)^k)/(2^{\delta_k} - 1)$; and the one-sided approximation is sound ($m = \lfloor 1/\eta \rfloor$
gives $m\eta < 1$ by irrationality and $1 - m\eta < \eta$, so the fractional part of $mq\alpha$ is
within $\eta$ of 1). Checked exactly: the closed form equals G45's general ceiling for every $k \le 399$, and the
record ceilings $(k, K)$ are $(5, 16)$, $(17, 25)$, $(29, 39)$, $(41, 86)$, $(94, 106)$, $(147, 136)$, $(200, 191)$,
$(253, 321)$, $(306, 977)$, at the $k$ where $k\log_2 3$ falls just below an integer (`collatz_audit_g39_g42.py`, G46 part).
