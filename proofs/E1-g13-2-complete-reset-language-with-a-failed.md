# G13.2. Complete reset language, with a failed first characterization retained

*Theorems proved by GPT. Derived from [PROOFS.md](../PROOFS.md), entry "E.1. G13.2. Complete reset language, with a
failed first characterization retained"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and
this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT (statement in PROOFS.md; the proof is copied below from RULE30-GPT.md).

## In plain words

GPT found exactly which stretches of a row erase all memory when you rebuild the row before it.

**What it says.** You can rebuild an earlier row from a later one, square by square, keeping two squares of memory
as you go (four possible states). Some stretches of the later row send all four states to the same one, whatever you
started with: they "reset" the rebuild. GPT proved that a stretch resets exactly when it contains white, then a run
of black squares of length 1, 4, 7, 10, ..., then white, then any square. The shortest are 0100 and 0101. GPT's
first guess was wrong, and the failure is kept on record.

**Why it matters.** A reset means two different pasts become identical from that point on: information from further
away is wiped. This is an exact measure of when the right side's influence is forgotten.

**An everyday picture.** Directions that get you to the town square from anywhere in town, even if you do not know
where you started.

## The formal statement and proof

*Where:* RULE30-GPT.md, "G13.2. Complete reset language, with a failed first characterization retained". *Status:* proved by GPT (proof there).

**Theorem.** A finite driver word resets exactly when it contains a factor

*Correction (Cloud, 2026-10-06): the copy above was cut off mid-sentence. The statement in RULE30-GPT.md G13.2 continues with the factor:*

```math
 0\,1^{3k+1}\,0\,z,\qquad k\ge0,\quad z\in\{0,1\}.
```

## The proof, copied from RULE30-GPT.md

*Verbatim from [RULE30-GPT.md](../RULE30-GPT.md), the section named above; the master PROOFS.md holds the statement only.*

I initially proposed that every reset word contains010 followed by another bit. IR5 checked
that claim and failed at0111100. This is a false characterization, not an instrument failure
and not a refutation of the shortest words or the one-step theorem. The failure remains in
the probe and here. The corrected exact statement is:

**Theorem.** A finite driver word resets exactly when it contains a factor

```math
 0\,1^{3k+1}\,0\,z,\qquad k\ge0,\quad z\in\{0,1\}.
```

**Proof by the reachable non-singleton images.** Begin with the full set F. Label
S0={00,01,11}, S1={00,01,10}, C={00,11}, D={01,10}, B={00,10}, A={00,01}, E={01,11}.
Their transitions, calculated from G13.1, are:

| Image set | Driver0 | Driver1 |
|---|---|---|
| F | S0 | S1 |
| S0 | C | D |
| S1 | S0 | S1 |
| C | C | D |
| D | E | B |
| B | A | A |
| A | C | D |
| E | singleton11 | singleton10 |

A singleton remains a singleton under every later driver. The first collapse must therefore
be from E on one further bit. E is reached only from D on0. Before any collapse, the image
after a0 is S0,C,A orE. If it is E, one more bit already collapses. Otherwise, the next1
always gives D, and successive ones cycle D,B,A,D. Leading ones, with no preceding0, leave
S1. Hence the first visit to E follows a0, a run of ones of length1 modulo3, and another0;
the next bit collapses. Conversely, each such factor collapses the full image, whatever
prefix precedes it, since after its first0 the possible non-singleton image is among those
just listed (or E, which collapses still sooner). This proves the exact language. The
shortest factors have k0 and length4, giving G13.1. No probabilistic premise enters.
