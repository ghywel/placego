# finite-tail exceptions in a minimal trace family are empty or countable dense

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT154. finite-tail exceptions
in a minimal trace family are empty or countable dense (second-read by Local, 2026-10-07)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

In a minimal family of traces, finite starting tails are either absent or countable and dense.

**What it says.** The Rudin–Shapiro family has infinitely supported tails for a generic trace. If one finite-tail exception exists, all its time shifts are finite-tail exceptions and are dense in that family.

**Why it matters.** Generic exclusion does not decide the original Rudin–Shapiro word. A direct spatial-tail argument is still needed; this result awaits independent review.

**An everyday picture.** A countable collection can visit every neighbourhood while occupying none of the measure.

## The formal statement and proof

### G154. Finite-tail exceptions in a minimal trace family are empty or countable dense (2026-10-07)

**Status and target.** Symbolic scope audit, independently verified by Local L112; no computation. Uses reviewed G140's wall coding and radius clock, and generalizes G147's phase-counting argument to a minimal trace family. This is an elementary dynamical argument, not a novelty claim about substitution systems. Prediction: generic infinite support cannot exclude the original Rudin–Shapiro trace. Counterfactual: minimal recurrence plus a generic exclusion forces every individual trace to have an infinite tail. The conditional dense-exception argument below shows why that inference fails. G153 and its RSP-S certificate are not assumed in this proof.

Let X be a nonempty compact, forward-shift-invariant family of one-sided visible binary words in which every forward orbit is dense. Assume X is infinite. Under G140's bijection Phi from visible words to compatible white-phase initial rows, set

    E_X = {c in X : Phi(c) has finite left support}.

Then E_X is empty or countable dense in X. Its complement is residual and has full measure for every shift-invariant probability measure on X. For each fixed radius L, at most 2^L words of E_X have radius at most L. None of these statements excludes a specified word of X.

**Proof.** There are at most 2^L binary rows supported in the first L cells. Injectivity of Phi gives the same bound for words, so E_X is countable. The conjugacy F Phi = Phi shift and finite-support preservation show that E_X is forward invariant. If nonempty, it contains a dense forward orbit and hence is dense. On that orbit radii increase by exactly two at each shift.

An infinite minimal compact trace family has no eventually periodic points: such a point would yield a finite periodic orbit in X, whose dense orbit would force X to be finite. It also has no isolated points. If a cylinder isolates c, minimality supplies a positive return of c to that cylinder, forcing shift^n(c)=c. More explicitly, compactness gives a finite cover by inverse images of that cylinder; applying the cover to shift(c) supplies the positive return. The resulting periodic point contradicts infinitude. Thus each singleton is nowhere dense, and countability makes E_X meagre. For an invariant probability measure, an atom at c would give every distinct forward image mass at least that atom's mass, since the preimage of the image contains c. Infinitely many such images contradict total mass one. Hence every such measure is nonatomic and E_X is null. This argument does not require Phi to preserve a preferred measure.

**Rudin–Shapiro supplies such an X.** Write r(n) for adjacent-11 parity. Appending a binary digit gives r(2n)=r(n) and r(2n+1)=r(n) XOR (n modulo 2). The pair (r(n),n modulo 2) is the fixed word starting at a of the substitution

    a -> ab, b -> ad, c -> cd, d -> cb,
    a=(0,0), b=(0,1), c=(1,0), d=(1,1).

Its directed graph reaches a from every letter in at most three steps and reaches every letter from a in at most three; the a self-loop pads each composed path to exactly six. Thus every sixfold substituted letter contains every letter. Any factor of the fixed word occurs inside some substituted prefix of a; consequently every sufficiently large substituted letter contains it. The fixed word is tiled by equal-length such substituted letters, so every sufficiently long factor contains that chosen factor. Projecting to the first coordinate preserves this bounded-gap property. The binary shift closure X_r is therefore minimal: every factor of r occurs in every member with bounded gaps, so every forward orbit meets every cylinder of X_r.

For completeness r is not eventually periodic. For m<2^(k-1), the separated binary blocks give r(2^k+m)=r(m) and r(3*2^k+m)=1 XOR r(m). If r were eventually q-periodic, taking k arbitrarily large in the first identity transfers that periodicity to every initial m, making it purely q-periodic. Now choose k with 2^(k-1)>q. The first identity at m=0 through q-1 says translation by 2^k fixes the entire q-periodic word; translation by 3*2^k must then fix it too. The second identity at m=0 contradicts that, since r(0)=0 and r(3*2^k)=1. Thus X_r is infinite and the stated dichotomy applies.

**Unexpected periodic-family check.** If X is instead a finite periodic orbit, E_X is empty: a finite row corresponding to a p-periodic visible word would return after p applications of F, contradicting radius growth by 2p. The all-zero visible control gives the infinite checkerboard initial tail, not a finite row. This verifies why temporal simplicity is not a spatial-support certificate.

**Scope.** For Rudin–Shapiro, generic members of its binary shift closure have infinite forced initial tails, independently of the pending repeat-filter decision. If even one member has finite support, its dense shift orbit has growing finite radii and remains fully consistent with generic infinite support and infinite-support accumulation points. The original r is a specified member; this argument neither excludes it nor constructs an exception. The missing obligation remains a direct spatial-tail constraint on Phi(r), and full right extension is separate. No prize claim.

*Second reader's note on G154 (Local, 2026-10-07; chat L112).* Correct; every hypothesis is stated and used. The
substitution follows from appending a digit: $r(2n) = r(n)$ and $r(2n+1) = r(n) \oplus (n \bmod 2)$, so a letter
$(r, p)$ becomes $(r, 0)(r \oplus p, 1)$, which is $a \to ab$, $b \to ad$, $c \to cd$, $d \to cb$. Its graph reaches $a$
from every letter and every letter from $a$ within three steps, and the loop at $a$ pads to exactly six, so the sixth
power is positive. Uniform recurrence of the fixed word passes to its first coordinate because a factor of $r$ is the
projection of the factor of the pair word at the same positions. Minimality then gives the two generic statements. An
isolated point would return to its own cylinder and be periodic, so singletons are nowhere dense. An atom would put at
least its mass on every distinct forward image, since each image's preimage contains the point. The block identities
need $m < 2^{k-1}$ so that the digit after the leading 1 or 11 is 0, and both proofs use exactly that. One sharpening,
as in G147: by GC156's free odd depths, at most $2^{\lceil L/2 \rceil}$ words of $E_X$ have radius at most $L$. Checked
(`rule30_audit_g99_g100.py`, S48): both digit recurrences for $n < 2^{14}$; the pair word equals the substitution's
fixed word on $2^{14}$ letters; the sixth power of the letter matrix is positive; and the separated-block identities for
$k \le 12$.
