# exact dyadic source-column sampling times

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT224. exact dyadic source-column
sampling times (second-read by Local, 2026-10-08)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

At certain observation times, each column at a power-of-two distance has only a short list of chances to affect the centre.

**What it says.** The binary walk-counting coefficients select exact source times on these columns. The list grows only with the number of doublings of the observation time. Other columns still contribute.

**Why it matters.** It replaces a whole time interval with a precise list to check. It does not say that an allowed source actually turns on.

**An everyday picture.** A timetable lists the departures that can reach a station before a particular appointment. An entry in the timetable does not mean someone boarded that train.

## The formal statement and proof

**Where:** RULE30-GPT.md GC446 at bee30ac; Local L262 in e98c45b verifies the binary proof, endpoint examples and nondyadic guard. The source statement and proof are copied verbatim below. Standard binary binomial parity is specialized to G215's kernel; G26/G58 already use related Catalan parity.

**Prediction, written before controls.** For i=2^r, r>=0, K_l(i)=1 exactly when l=2^h-2^r for an integer h>=r+1. At odd dyadic target T=2^K+1 and 1<=r<K, the selected times on source column i=2^r are exactly t=2^K+2^r-2^h, r+1<=h<=K. Counterfactual: column2 contributes only at the last down transition t=2^K-2. Unexpected check: use column4 as well as column2; retain a nondyadic-column guard. No actual orbit or matching source-product claim is predicted.

**Proof.** A coefficient with l<i or wrong parity is zero. Otherwise write a=(l-i)/2, so K_l(i) is the parity of binom(2*a+i,a+i). Over binary coefficients, (1+z)^n is the product of (1+z^(2^j)) over set bits j of n. Its coefficient is odd precisely when the selected exponent is a bit subset of n; equivalently the two summands a and a+i add without carries. Thus K_l(i)=1 iff a AND (a+i)=0. When i=2^r, the lower r bits of a and a+i agree, so disjointness forces them all zero. Write a=2^r*c. The remaining condition is c AND (c+1)=0, which holds exactly for c=2^j-1, j>=0: incrementing clears the trailing ones, while any higher set bit survives in both numbers. Hence l=2*a+i=2^(r+j+1)-2^r. Conversely each such value gives disjoint summands and the coefficient1. Substituting l=T-1-t proves the claimed times; t>=0 restricts h<=K when r<K. Each time also has t>=i and fits the causal cone.

For a full0101 orbit the contribution of this one column to the time-T Duhamel parity is therefore exactly

`XOR_(h=r+1,...,K) V_(2^K+2^r-2^h)(2^r)`.

This is a contribution, not the complete certificate. If initial support[-R,R] satisfies 2^K>R+1, G28's homogeneous centre term is zero at T: A^(2^K+1) samples only positions +/- (2^K-1) and +/- (2^K+1). G215's whole source sum is then1, but nondyadic columns remain in that sum. G216 removes i<=1 termwise. No positivity or independence of the remaining products is assumed.

**Duplicate guard for G224:** actual nearest G215,G216,G62 read in full. G215 supplies the general kernel; G216 removes two columns by temporal parity; G62 restricts source column1. This entry gives exact coefficient times on every dyadic column, rather than any of those source-product statements.

**Scope:** this is a coefficient stencil per dyadic column. Nondyadic columns remain in the full parity certificate, and source products need not fire. No finite-clock exclusion.
