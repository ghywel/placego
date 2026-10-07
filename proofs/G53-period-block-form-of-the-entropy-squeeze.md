# Period-block form of the entropy squeeze

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT53. Period-block form of
the entropy squeeze"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The information limit on the left half can be computed one period of the wall at a time.

**What it says.** For a wall that repeats with period p, group column 1's visible bits by period. The rate at which
new information reaches any fixed column on the left is at most the rate of these groups divided by p.

**Why it matters.** It puts the squeeze (proof 19) into a form that works for every repeating wall.

**An everyday picture.** Counting deliveries by the van-load: a depot that sends one van a week can deliver to a
street no faster than one van-load a week, however the parcels are packed.

## The formal statement and proof

**Where:** RULE30-GPT.md G53; copied proof. **Status:** second-read by Local, 2026-10-06 (note below G54). No new numerical certificate claimed.

### G53 lemma and proof: period-block entropy conversion

Fix a period-p wall tau, with z white phases per period. Let v_m be the z-bit vector of column1 at those phases during period m, and let pi be column-1. For a one-sided sequence s, let P_s(n) count its distinct contiguous n-symbol words, and h(s)=limsup log2(P_s(n))/n. The vectors v are symbols in an alphabet of size2^z. Then

    h(pi)=h(v)/p,
    h(column -k)<=h(v)/p for every fixed k>=1.

At each white phase, pi(t)=tau(t+1) XOR sigma(t), so its p-symbol period block determines v_m uniquely. At each black phase, pi(t)=tau(t+1) XOR1 is fixed. Therefore period blocks of pi and symbols v are in bijection. Every n-vector word supplies a distinct aligned pn-bit pi word, giving P_v(n)<=P_pi(pn). Every m-bit pi word is determined by its start phase and at most ceil(m/p)+1 consecutive v symbols. Extend shorter determining words to this common length using the infinite future; hence P_pi(m)<=p*P_v(ceil(m/p)+1). Taking the two limsup bounds proves the equality.

Repeated scalar inversion computes column-k over m times from pi and tau over at most m+k-1 times. There are p possible start phases of tau. Thus a deliberately loose uniform bound is

    P_(column -k)(m)<=p*P_v(ceil((m+k-1)/p)+1).

This proves the entropy inequality, since fixed finite lookahead and the phase factor disappear after division by m. In particular h(v)<=z gives the elementary bound z/p bits per physical step. If an independently certified per-period vector language obeys P_v(n)<=C*lambda^n, the bound improves to log2(lambda)/p. That hypothesis needs a certificate for the chosen wall; the0101 certificate does not establish it for another wall. With p2,z1 this recovers the established squeeze conversion, apart from deliberately looser finite constants.

Unexpected scope check: for wall001 and all white-phase bits0, pi is the periodic word011 independently of every right bit at a black phase. Across N periods there are2^N choices of those invisible bits and only one pi prefix. Counting all column1 bits rather than its visible period vectors can therefore lose the exact entropy equality. This is an algebraic family of formal boundary inputs; no assertion that all these inputs admit full right-half realization is made.

This is the period-block form of RULE30-PRIZE.md section8.33 proof steps2-4, not a new channel certificate or a positive lower entropy bound for a finite seed. It leaves the fixed-seed cost and left/right compatibility gaps open.
