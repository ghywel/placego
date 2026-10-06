# G18.2. Exact finite-prefix map from a latch position

*Theorems proved by GPT. Derived from [PROOFS.md](../PROOFS.md), entry "E.4. G18.2. Exact finite-prefix map from a
latch position"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved by GPT (statement in PROOFS.md; the proof is copied below from RULE30-GPT.md).

## In plain words

On a slow wall, the left half near the middle carries only "when did the switch go on", so there are just a + 1
possibilities.

**What it says.** Take a wall that is white for a ticks, then black for b ticks, repeating. The first a + b − 1
squares of the left half at the start are fixed by column 1's a bits during the white ticks. Those bits can switch
on only once (C2), so exactly a + 1 different beginnings of the left half are possible.

**Why it matters.** It counts exactly how little a slow wall lets through near the middle: only the moment of one
switch, about log2(a + 1) bits per period.

**An everyday picture.** A light that may be switched on once during a meeting: the only news it carries is when.

## The formal statement and proof

*Where:* RULE30-GPT.md, "G18.2. Exact finite-prefix map from a latch position". *Status:* proved by GPT (proof there); its finite controls replicated by Local from the committed `rule30_gpt_slow_switch.py`, 2026-10-06 at edce038.

**Theorem.** For wall0^a1^b, a,b>=1, the first p-1 left cells on row0 are
determined by the a visible sigma bits at the white times. If these bits are
monotone (the necessary width-one rule), exactly a+1 distinct prefixes occur.
This is a finite-prefix assertion, not an autonomous state for the infinite row.

## The proof, copied from RULE30-GPT.md

*Verbatim from [RULE30-GPT.md](../RULE30-GPT.md), the section named above; the master PROOFS.md holds the statement only.*

**Theorem.** For wall0^a1^b, a,b>=1, the first p-1 left cells on row0 are
determined by the a visible sigma bits at the white times. If these bits are
monotone (the necessary width-one rule), exactly a+1 distinct prefixes occur.
This is a finite-prefix assertion, not an autonomous state for the infinite row.

**Construction and proof.** Begin at time a with the known checkerboard word
of length b-1. To step backwards to time t=a-1,..,0, set x0=0 and
x1=sigma(t) XOR tau(t+1), then successively set
x(k+1)=y(k) XOR(x(k) OR x(k-1)), where y is the known next-time row.
A future prefix of length N determines the preceding prefix of length N+1.
After a steps this constructs exactly b-1+a=p-1 cells. It uses no sigma at a
black time and no later white block. The probe implements this row construction
independently of the column-by-column inverse used by earlier controls.

Monotone visible words have the form0^r1^(a-r), r=0..a. Each is allowed as a
single width-one block (G14/G15; neighbouring blocks are coupled when b=1).
The constructed prefixes are distinct: from any row0 prefix of length at least a,
forward Rule30 on the left half with the fixed wall determines pi(t) for t0..a-1.
The inverse wall identity recovers each visible sigma(t) from pi(t). Thus equal
prefixes would imply equal r. This proves both the a+1 upper count and injectivity,
without assuming an actual whole right half realizes every block.
