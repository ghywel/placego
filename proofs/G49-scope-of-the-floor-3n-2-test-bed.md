# Scope of the floor(3n/2) test bed

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT49. Scope of the
floor(3n/2) test bed"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A Collatz-like test bed, multiply by 3/2 and round down, keeps the arithmetic but asks a different survival question.

**What it says.** The map n to floor(3n/2) has the same exact arithmetic as Collatz (F1 and its relatives carry
over). But every number from 2 up simply grows, so "staying above the start" is trivial. The real question (the
"Antihydra" Turing-machine problem) is a counter that gains 2 on even steps and loses 1 on odd ones. With fair coins
such a counter survives for ever with probability at least about 0.38, rather than dying out.

**Why it matters.** It shows exactly which of the record's Collatz tools transfer to this famous unsolved test bed,
and which do not.

**An everyday picture.** The same engine in a different race: the arithmetic runs just as before, but the question
becomes a gambler who wins two pounds on heads and loses one on tails. Does the money ever run out? With a fair
coin, more than a third of the time it never does.

## The formal statement and proof

**Where:** RULE30-GPT.md G49, 2026-10-06; copied verbatim. **Bears on:** PRIZE-PROBLEMS.md §8, Antihydra tool transfer. **Status:** analytic map/counter/coin calculation, second-read by Local, 2026-10-06 (note below); AH1-AH4 finite controls pass (G49 outcome). Machine reduction is reported from the project source, not independently machine-verified.

### G49 theorem and proof: floor(3n/2) preserves coding but changes survival

Let H(n)=floor(3n/2) on nonnegative integers. Write b=n modulo2. Then H(n)=(3n-b)/2. Every n>=2 strictly increases, since H(n)-n=floor(n/2)>=1;0 and1 are fixed. Therefore the count of positive w-bit starts staying above their start is2^(w-1) for every horizon, rather than exponentially decaying. This does not settle a parity-counter halting problem.

For a word b_0,...,b_(t-1), define C_0=0 and C_(j+1)=3*C_j+b_j*2^j. Then

    2^t*H^t(n) = 3^t*n-C_t.

The word is realized by exactly one residue r modulo2^t, namely r=C_t*(3^t)^(-1) modulo2^t. Prefix congruences and integrality force the prescribed parities just as in G45. Lifting a start by2^t*m adds3^t*m to its terminal value. For0<=r<2^t, nonnegativity and C_t>=0 give0<=H^t(r)<3^t. Thus the parity bijection, affine lift and finite-residue binary reader transfer, with modulus3^t independent of the odd count. G43/G44's reader identities can be used with that law; none supplies a pointwise orbit theorem.

**Actual test-bed event.** In the reported Antihydra reduction, the initial value is H_0=8 and a counter starts at0, gains2 when H_j is even and loses1 when it is odd. Writing a_t for the odd count, its value aftert steps is2t-3a_t. Avoiding halt throughT requires2t-3a_t>=0 at every prefix, since the only negative crossing is to-1. This upper-odd-density barrier differs from Collatz's coefficient lower-density barrier. Strict growth of H says nothing by itself about it: seed3 grows but makes the zero counter hit-1 immediately. The reduction is cited from the project source; the original six-state Turing-machine transition simulation has not been independently verified here.

**The fair-coin analogue does not have exponential survival decay.** Let iid bits drive counter increments+2 for0 and-1 for1. Put r=(sqrt(5)-1)/2, so r^2+r=1. For counter c>=0, h(c)=r^(c+1) obeys(h(c+2)+h(c-1))/2=h(c), and h(-1)=1. Stopping at the first hit of-1 or at finiteT gives expectation h(C_stopped)=r at initial counter0: this follows by successive conditional expectation, with no unbounded stopping theorem. On paths that hit, h=1; on other paths h>=0. Hence P(hit byT)<=r and P(surviveT)>=1-r>0 for everyT. No assumption about H^t(8)'s actual parity distribution is made. Uniform starts modulo2^T realize all T-bit words once, so the same lower bound holds for that finite initial ensemble. It does not determine the selected start8. Thus transferring the Collatz coin's decaying survival target to this barrier is mathematically invalid.

*Second reader's note on G49 (Local, 2026-10-06; chat L021).* Correct. $H(n) = (3n - b)/2$ and
$H(n) - n = \lfloor n/2 \rfloor$; the identity $2^t H^t(n) = 3^t n - C_t$ follows by induction
($2^{t+1} H^{t+1} = 3 \cdot 2^t H^t - 2^t b_t$); the residue, the lift by $3^t m$ and $0 \le H^t(r) < 3^t$ check;
the counter is $2t - 3a_t$; and $h(c) = r^{c+1}$ is harmonic for the walk that adds 2 or subtracts 1, because
$r^3 - 2r + 1 = (r - 1)(r^2 + r - 1) = 0$, so the stopped expectation gives $P(\text{survive } T) \ge 1 - r$. Checked
exactly: the identity and residue law for every $n < 3000$ and $t \le 20$, and the fair-coin survival probability
by exact dynamic programming, $0.5$, $0.4023$, $0.3822$ at $T = 1$, 10, 60, every value above $1 - r = 0.3820$
(`collatz_audit_g39_g42.py`, G49 part). The Antihydra reduction itself is, as G49 says, taken from the project
source and not machine-verified here.
