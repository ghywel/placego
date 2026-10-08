# Prime-ring quotient cycle lifting

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT55. Prime-ring quotient cycle
lifting"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

On a prime ring, every Rule 30 cycle is a lifted copy of a simpler cycle, which explains when cycle lengths are
distinct.

**What it says.** Treat patterns that differ only by turning the ring as one. Each cycle of these classes either
lifts to p separate cycles of the same length or to one cycle p times as long, depending on whether the pattern
drifts round the ring. So all cycle lengths are distinct exactly when every class cycle drifts and no two class
cycles have the same length.

**Why it matters.** It turns the census's observation (C6) into an exact criterion, and shows that the claim cannot
hold for all primes (it already fails at 7 and 11).

**An everyday picture.** A dance on a round floor: either the dancers come back to the same spots each time round,
or they shift along and need p rounds to return.

## The formal statement and proof

**Where:** RULE30-GPT.md G55; copied proof. **Status:** second-read by Local, 2026-10-06 (note below); GPT's RQ1-RQ3 finite controls pass.

### G55 lemma and proof: prime-ring cycle lifting

Let R be rotation of a binary ring of prime size p, and let F commute with R. Nonconstant states have free rotation orbits of size p: a stabilizing nonidentity rotation generates the prime cyclic group and would make every cell equal. Quotient these states by rotation. Consider a q-cycle of the induced quotient map that stays nonconstant. Choose a representative x. After q time steps,

    F^q(x)=R^b(x), with a unique b modulo p.

This rotation displacement is independent of the representative, since F commutes with R. Along this quotient cycle, the corresponding pq states form an invariant set. On return to the chosen quotient vertex, the rotation label advances by b. If b=0, there are p temporal cycles of length q, one for each label. If b!=0, addition by b visits all p labels and there is one temporal cycle of length pq. No shorter period is possible: a temporal return must first return to the quotient vertex, hence be a multiple of q, and its rotation label must return too. In the nonzero case rotation preserves the single temporal cycle; in the zero case it permutes the p separate cycles.

For Rule30 the constant states satisfy F(0)=0,F(1)=0. Therefore its only constant temporal cycle is the white fixed point. For this rule on a prime ring, all temporal cycle lengths are pairwise distinct if and only if every nonconstant quotient cycle has nonzero displacement and the quotient cycle lengths are pairwise distinct. This is an exact reduction, not a proof that either condition holds for unexamined primes.

Existing controls from Local's census: p7 has seven4-cycles and a63-cycle; the lift description predicts a zero-displacement quotient4-cycle and a nonzero-displacement quotient9-cycle. At p11 the eleven17-cycles and154-cycle similarly predict quotient periods17 and14, with zero and nonzero displacement respectively. These are reconstruction targets from known data, not blind new predictions. In particular a claim for all prime sizes is already false.

Unexpected structural check: take F=R itself on a three-cell binary ring. Its two nonconstant temporal cycles, represented by001 and011, both travel and both have length3. Thus every cycle travelling does not imply pairwise distinct lengths. This is a different CA used to test what rotation symmetry alone proves; it is not a Rule30 counterexample at13 or later.

This specializes elementary cyclic-group cycle lifting and the already recorded rotation-orbit pigeonhole in RULE30-PRIZE.md section8.67. It identifies the remaining Rule30 mechanism as excluding zero displacement and repeated quotient periods in the observed prime-size regime, without a novelty or asymptotic claim.

### G55 addendum: spatial symmetry does not imply black/white balance

For a rotation-invariant temporal cycle C of length L on a p-ring, every spatial site has the same number of black occurrences during one temporal cycle. Rotation is a bijection of C and sends the bit at one site to the bit at its neighbour, proving equality of these finite counts. If L is odd, that common integer count cannot equal L/2. Thus the verified Rule30 p13 cycles of lengths91 and247 are travelling yet each column has biased black frequency, at least1/(2L) away from one half.

This proves a limit of the symmetry argument, not a fixed-single-seed Rule30 frequency result. It does not supply the actual black counts of those cycles, which were not measured in this block. Equal frequencies at all sites and equal frequencies of the two colours are distinct requirements.

**G55 finite control status:** RQ1-RQ3 pass10408 states at prime sizes<=13; proof and addendum await independent reading.

*The addendum was written by GPT after Local's first reading below; Local second-read it the same day (chat L028):
correct (rotation maps the cycle onto itself and site $i$ to site $i + 1$, so the black counts per site agree, and an
odd length cannot split in half). The counts it did not measure, measured (`rule30_audit_g55.py`): on the four
travelling cycles at $p = 13$ every site has the same black count, 425 of 832 (0.5108), 133 of 260 (0.5115), 123 of
247 (0.4980) and 46 of 91 (0.5055); the even-length cycles are biased as well, which parity alone does not force.*

*Second reader's note on G55 (Local, 2026-10-06; chat L027).* Correct. A rotation fixing a state on a prime ring
generates all rotations, so nonconstant states have free orbits; $F^q(x) = R^b(x)$ fixes $b$ independently of the
representative because $F$ commutes with $R$; $b = 0$ gives $p$ cycles of length $q$ and $b \ne 0$ one cycle of length
$pq$, with no shorter return in either case; Rule 30 sends the all-black ring to white, so the white fixed point is
the only constant cycle. Checked directly (`rule30_audit_g55.py`): on the prime rings 5, 7, 11, 13, 17 and 19 every
temporal cycle obeys the lifting law; the zero-displacement families are exactly the seven 4-cycles at 7 and the
eleven 17-cycles at 11; and G55's criterion (nonzero displacement and distinct quotient periods) agrees with
"all cycle lengths distinct" at every one of them. The quotient periods at 13 are 64, 20, 19, 7; at 17, 638, 96, 51,
18, 8, 1; at 19, 195, 13, 7, 2. This upgrades PROOFS.md C.6 from a pigeonhole to an exact reduction.
