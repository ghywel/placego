# Exact binary-reader Fourier weights

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT43. Exact binary-reader Fourier
weights"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

An exact translation table between base 3, where the Collatz state lives, and odd or even, which decides the next step.

**What it says.** Suppose you know a number's remainder after dividing by a power of 3, and you want to know whether
the number is odd. GPT wrote down exactly how much each frequency of the remainder's distribution contributes to
that question, with an explicit formula.

**Why it matters.** F1 puts the Collatz state in base 3, but the next step is decided by base 2. This is the exact
bridge between them, and it says which frequencies matter most.

**An everyday picture.** The sliders of a graphic equaliser, read the other way round: for one sound, they show how
much each band of frequencies contributes to it. Here the sound is the answer odd-or-even, and the bands are the
patterns in a base-3 remainder.

## The formal statement and proof

**Where:** RULE30-GPT.md G43, 2026-10-06; copied verbatim. **Bears on:** PERIOD-TWO.md §7 question9 and COLLATZ-PRIZE.md §4. **Status:** analytic derivation and single-party controls; second-read by Local, 2026-10-06 (see the note below the heading of E2). No tail-count bound.

### G43 theorem and proof: exact ternary spectrum of a binary reader

Let M=3^a with a>=1, and interpret q moduloM by its least representative0<=q<M. Set f(q)=(-1)^q and e(x)=exp(2*pi*i*x). For0<=h<M define hat f(h)=M^(-1)*sum_q f(q)*e(-h*q/M). A geometric sum with ratio-e(-h/M) gives

    hat f(h) = 2/[M*(1+e(-h/M))],
    |hat f(h)| = 1/[M*|cos(pi*h/M)|].

The numerator is2 because M is odd and e(-h)=1. The denominator is nonzero for integer h on an odd group. In particular hat f(0)=1/M, not0. Fourier inversion gives, for any distribution of q with phi(h)=expectation e(h*q/M),

    expectation f(q) = sum_h hat f(h)*phi(h).

G38's upper-half state is y=M+q. Since M is odd, its next parity is odd exactly when q is even. Thus

    probability(y odd) = (1+sum_h hat f(h)*phi(h))/2.

This sum is real, although individual summands may be complex. Uniform ternary residues give probability(y odd)=(M+1)/(2M), including the finite1/(2M) bias.

**Which frequencies matter.** The weights peak near h=M/2, where |hat f((M-1)/2)|=1/[M*sin(pi/(2M))], tending to2/pi. If0<=h<=M/3, then |hat f(h)|<=2/M. In G42's family, M/h=(81/16)*(27/16)^n>3 at the resonant primitive harmonic h=2^T. Its contribution to the parity-reader sum therefore has magnitude at most2/M even though |phi(h)|>0.99. This is a within-family bound; it does not transfer that family's measure to the full population. It also does not refute the general relevance of primitive-frequency resonances to other test functions.

For completeness, writing d=|h-M/2| gives |hat f(h)|=1/[M*sin(pi*d/M)]<=1/(2d), using sin(x)>=2x/pi on[0,pi/2]. Sum over the half-integer distances to obtain sum_h|hat f(h)|<=3+log(M), with log natural. Indeed the paired distances give sum_(j=0)^((M-3)/2)1/(j+1/2) plus1/M, bounded by2+log(M)+1/M by integral comparison. Hence a bound |phi(h)|<=delta for all nonzero h implies

    |probability(y odd)-(M+1)/(2M)| <= delta*(3+log(M))/2.

This proves the logarithmic Fourier-weight assertion for one binary bit; it supplies no delta estimate itself. Frequency-specific estimates may instead be inserted into the exact weighted sum.

**Longer binary cylinders.** For B=2^d,0<=c<B, let g_c(q)=1 when q is congruent to c moduloB. Put L_c=max(0,1+floor((M-1-c)/B)). Its Fourier coefficient is the exact finite sum

    hat g_c(h) = e(-h*c/M)/M * sum_(j=0)^(L_c-1) e(-h*B*j/M).

The empty sum is0; at h=0 the value is L_c/M. A nonzero-frequency sum is the usual geometric quotient. A prescribed future parity word corresponds by the parity bijection to one residue of y moduloB, and therefore to c for q after subtracting M. If B>=M, each nonempty cylinder contains just one representative q, and every coefficient has magnitude1/M. Thus the complete tail problem requires finer information than the one-bit reader. Furthermore actual stopping-time survival compares the iterates with their start, not merely with the coefficient barrier; these populations cannot silently be equated.

*Second reader's note on G43 (Local, 2026-10-06; chat L008).* Correct throughout. The geometric sum and its
numerator 2 (odd $M$), the nonvanishing denominator ($e(-h/M) = -1$ is impossible for odd $M$), $\hat f(0) = 1/M$,
the bound $2/M$ for $0 \le h \le M/3$, the peak $2/\pi$, the weight bound via $\sin x \ge 2x/\pi$ and the integral
comparison ($\le 2 + \log M + 1/M$), and the cylinder sums were each checked by hand; the coefficient formula
was checked numerically against the direct sum for every odd $M < 400$ (error $4 \times 10^{-14}$), the weight bound
for those $M$ and for $M = 3^6$ to $3^9$, and the bound $2/M$ at $h = 2^T$ for G42's family for $n = 0$ to $39$
(`collatz_audit_g39_g42.py`, G43 part).
