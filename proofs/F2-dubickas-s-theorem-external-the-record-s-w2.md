# Dubickas's theorem (external; the record's W2)

*Collatz. Derived from [PROOFS.md](../PROOFS.md), entry "F.2. Dubickas's theorem (external; the record's W2)";
rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** a published theorem (A.

## In plain words

A Collatz number that ran off to infinity would have to change its step pattern endlessly: it could not loop or
repeat.

**What it says.** A published theorem (Dubickas, 2009): if an orbit grew for ever, its sequence of odd and even
steps would have at least about 1.7 n different patterns of length n. Repeating or nearly repeating step patterns
are impossible.

**Why it matters.** It is Collatz's counterpart of Jen's theorem (two neighbouring columns cannot both end up
repeating, if the seed is finite) for Rule 30: it rules out the simple counterexamples and says any real one must
look irregular.

**An everyday picture.** A getaway car that can never settle into a fixed route: any repeating loop would get it
caught.

## The formal statement and proof

*Where:* COLLATZ-PRIZE.md §5; PRIOR-ART.md. *Status:* a published theorem (A. Dubickas, 2009, Theorem 5), read in
full and credited; the record's "complexity at least $1.70951129\,n$" statement for divergent integer orbits is
its restatement, and GPT's G29 audits its extension to signed rationals with the hypotheses named.
