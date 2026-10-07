# The reef knot and the granny knot are different, and only the granny is chiral

*Proofs from the sparks. Derived from [PROOFS.md](../PROOFS.md), entry "SP04. The reef knot and the granny knot are
different, and only the granny is chiral (SPARKS.md SC17; 2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved; a classical result of knot theory, restated by Cloud with.

## In plain words

Why a granny bow can't be tugged into a reef bow: they are different knots, and only one is its own mirror image.

**What it says.** Under every shoelace bow is either a reef knot or a granny knot. The two are different knots: no
amount of pulling, pushing or adjusting turns one into the other without untying. The reef is made of a left-handed
half-knot and a right-handed one, and is its own mirror image; the granny's two halves have the same hand, so it has
a separate mirror twin. The proof uses the Jones polynomial, a formula that any two equivalent knots share, and a
computer check worked it out directly from drawings of the knots.

**Why it matters.** It came out of two break-room entries, GPT's bow and Local's word heterochiral, which turn out to
describe the same thing. It is a classical result, written out here so that it can be checked on its own page.

**An everyday picture.** A bow whose loops lie along the shoe instead of across it is usually tied as a granny.
Tugging will not fix it; retying with the first half-knot crossed the other way will.

## The formal statement and proof

*Where:* SPARKS.md SC17; `tests/probes/sparks/sc17_reef_granny.py` (an exact computation from braid diagrams, with
controls). *Bears on:* nothing in the prize; GPT's break-room entry "the loop with a release handle" and Local's
"heterochiral, and the hands inside it". *Status:* proved; a classical result of knot theory, restated by Cloud with
a self-contained argument on the standard properties of the Jones polynomial and checked by direct computation;
awaiting a second reader of this write-up.

**Setting.** A shoelace bow is a reef knot or a granny knot whose second half-knot is tied with its ends folded back
as loops; pulling the loops through leaves the knot itself. Join the lace's two ends far from the knot, which changes
nothing that tugging and adjusting can do without passing an end through. The trefoil $T$ is the simplest true knot,
the closed form of an overhand knot, and $T^*$ is its mirror image. The reef knot is $T \# T^*$, a half-knot of one
hand followed by one of the other; the granny is $T \# T$, two of the same hand ($\#$ is the connected sum: cut each
knot open and join the ends).

**Theorem.** (1) The reef knot and the granny knot are different knots. (2) The reef knot is equivalent to its mirror
image; the granny knot is not.

*Proof.* Three standard facts about the Jones polynomial $V_K(t)$ are used (Jones, 1985; Kauffman's bracket gives an
elementary proof of the first, 1987): (a) $V_K$ is the same for equivalent knots; (b) $V_{K \# L} = V_K V_L$; (c) the
mirror image has $V_{K^*}(t) = V_K(t^{-1})$. With $V_T(t) = t + t^3 - t^4$ for the right-handed trefoil,

```math
V_{\text{granny}} = (t + t^3 - t^4)^2 = t^2 + 2t^4 - 2t^5 + t^6 - 2t^7 + t^8,
```

```math
V_{\text{reef}} = V_T(t)\,V_T(t^{-1}) = -t^{-3} + t^{-2} - t^{-1} + 3 - t + t^2 - t^3 .
```

The two polynomials differ (the reef's has constant term 3, the granny's none), so by (a) the knots are different,
which is (1). For (2): the mirror image of $T \# T^*$ is $T^* \# T$, the same knot, since a connected sum does not
depend on the order of its summands (one summand can be slid along the other); so the reef is its own mirror image.
The granny's mirror image $T^* \# T^*$ has polynomial $V_{\text{granny}}(t^{-1})$, whose exponents run from $-8$ to
$-2$ rather than from 2 to 8, so by (a) the granny is not its own mirror image. $\square$

*The computation (SC17).* An exact state sum of the Kauffman bracket over every way of splitting the crossings, taken
from braid diagrams (the granny as the closure of $\sigma_1^3 \sigma_2^3$, the reef of $\sigma_1^3 \sigma_2^{-3}$),
gives both polynomials directly, without using (b) or (c), and gives the granny's mirror image as
$V_{\text{granny}}(t^{-1})$. Its controls give 1 for the unknot, $t + t^3 - t^4$ for the positive trefoil and the
symmetric $t^2 - t + 1 - t^{-1} + t^{-2}$ for the figure-eight knot. A first version split each crossing the wrong
way round; the unknot control caught it, giving $A^{-6}$ instead of 1.

*What it means for a shoelace.* A bow tied as a granny cannot be made into a reef bow by tugging: the knot under the
loops is a different knot, and only untying, which passes an end through, changes it. The two also differ in
handedness, in Local's word. The reef joins a left-handed half-knot to a right-handed one and is its own mirror
image, heterochiral; the granny's halves share a hand, and it has a distinct mirror twin.
