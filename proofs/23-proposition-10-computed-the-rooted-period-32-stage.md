# Proposition 10 (computed): the rooted period-32 stage runs past 2.6 × 10^10 steps

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "23. Proposition 10 (computed):
the rooted period-32 stage runs past 2.6 × 10^10 steps"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Some histories take more than 26 billion steps to double their repeat length from thirty-two to sixty-four.

**What it says.** All the histories were followed side by side, through every place where one splits into two, for about 26.4 billion steps. Fifty-six of the seventy-three that arose doubled their repeat length to sixty-four along the way. The first did so after about 66 million steps, the last of them after about 26.2 billion. Seventeen had still not doubled when the count stopped.

**Why it matters.** It shows how widely the histories spread out at this stage: the slowest are at least four hundred times slower than the fastest. The doublings keep getting rarer, and much more so for some histories than for others.

**An everyday picture.** A marathon where the leader crosses the line in two hours and the course has to close while some runners are still out after a week: the finishing times say as much about the spread as about the winner.

## The formal statement and proof

*Where:* CLOUD-LOCAL.md, TM6b (2026-10-07 18:03), chat L201; `tests/probes/lexicon/rule30_tm6b.c`. *Bears on:* PERIOD-TWO.md Q7, gap 2 (the spread of $N_6$ across rooted histories); G204, which uses Proposition 9; the joint growth/debt target of GC323. *Status:* certified by computation (Local, 2026-10-07); second reader wanted.

**Proposition 10 (computed).** Follow every rooted history, up to rotation as in Proposition 8, at common period 32
to depth $F = 26{,}424{,}115{,}200$. Exactly 73 histories arise, through 57 genuine branch nodes in the period-32
stage. Of these, 56 enter period 64 at or below $F$, with $N_6$ from $65{,}821{,}413$ (Proposition 9's minimum) to
$26{,}207{,}185{,}419$. The other 17 have no exit by $F$, so

```math
N_6 > 26\,424\,115\,200, \qquad R_6 = N_6/64 > 412\,876\,800 \quad \text{for each of them.}
```

In particular the period-32 stage of the rooted tree is not exhausted at $F$. Each of the sixteen histories entering
period 32 (Proposition 8), followed along its first child at every later branch, enters period 64, the last of them
at $N_6 = 15{,}969{,}952{,}673$.

*Proof (certificate).* `rule30_tm6b.c` continues the walk of Proposition 9 past its minimum, advancing all live
histories in lockstep by rounds of $2^{24}$ depths. It stops only at the end of a completed round, which is GC288's
frontier rule, with its guards in code. The literal equation held on every transition, with no failures over about
$4.4 \times 10^{11}$ period-32 steps. The run reproduced Proposition 9's events, including its first 32-bit zero at
65,821,412. GPT's counter identities (GC304), walks $= 1 +$ branches, live $=$ walks $-$ exits and period-32 zeros
$=$ branches $- 15 +$ exits, hold on every completed-round line and at the stop: $73 = 1 + 72$, $17 = 73 - 56$ and
$113 = 72 - 15 + 56$. The 56 exit depths are listed in the program's header. $\square$
