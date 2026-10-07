# Proposition 9 (computed): the first entry to period 64 in the rooted tree is at depth 65,821,413

*Siblings, Jen and the squeeze. Derived from [PROOFS.md](../PROOFS.md), entry "22. Proposition 9 (computed): the
first entry to period 64 in the rooted tree is at depth 65,821,413"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** certified by computation (Local, 2026-10-07); independently replayed and second-read by GPT, R2 (2026-10-07).

## In plain words

No history reaches a repeat length of sixty-four before about 65.8 million steps.

**What it says.** Following all sixteen histories further, side by side, the first one to double its repeat length again, from thirty-two to sixty-four, does so after 65,821,413 steps. Every other history is still at thirty-two at more than 67 million steps.

**Why it matters.** The number of steps each doubling takes, measured against the repeat length, has jumped from about 2,746 to over a million. That is finite evidence that the doublings keep slowing down, though not a proof that they always will.

**An everyday picture.** Runners on many paths at once: the first to cross the line sets a time that every other runner is known to be slower than, because everyone else was still running when the first one finished.

## The formal statement and proof

*Where:* CLOUD-LOCAL.md, TM6 (2026-10-07 14:54), chat L180; `tests/probes/lexicon/rule30_tm6.c`, with its header's correction after GPT's GC288. *Bears on:* PERIOD-TWO.md Q7, gap 2 (the record of $R_6$); G204, which uses it. *Status:* certified by computation (Local, 2026-10-07); independently replayed and second-read by GPT, R2 (2026-10-07).

**Proposition 9 (computed).** Every rooted history has $N_6 \ge 65{,}821{,}413$. Equality holds on exactly one
history up to rotation: the one entering period 32 at $N_5 = 667{,}052$. Its period-32 stage is a single excursion of
65,154,361 steps, ending at an odd zero. No other history has a zero driver at period 32 below depth 67,108,864. Hence

```math
R_6 = N_6 / 64 \ \ge\ 65\,821\,413/64 \quad \text{on every rooted history.}
```

*Proof (certificate).* `rule30_tm6.c` runs the walk of Proposition 8 at common period 32, at which every earlier
stage is periodic too, and advances all live histories in lockstep by rounds of $2^{24}$ depths. A branch inside a
round spawns a walk that is advanced to the round's end in the same round. The first odd zero anywhere is at depth
65,821,412, inside round 4. At that round's end, $F = 67{,}108{,}864$, every other walk has been advanced through
every depth below $F$ without a zero. A zero left unprocessed at exactly $F$ would give an entry of $F + 1$, still
above the minimum (G204's boundary check). The literal equation held on all of about $10^9$ transitions, no cap
fired, and the run reproduced Proposition 8's fifteen branches and sixteen entries, so the result meets the
certification rule of GC288. A later run of the same kernel past the minimum (TM6b) met the same first exit
again. $\square$

*Second reader's note (GPT, 2026-10-07, R2/GC294).* Compiled and replayed the committed TM6 code on the Intel CPU, about40.4s: the exact branch and doubling sets match Proposition8; the only exit is depth65821412, walk9, driver3864731681; the completed frontier is67108864, with fifteen live walks and zero literal failures. A one-step-shifted minimum is rejected. The loop processes depths strictly below the frontier, so the boundary guard in the proof is necessary and was retained. The original lower inequality1028459.58 was false at equality1028459.578125; the exact fraction above repairs it. This independently reproduces the certificate using the same C source; Local's separately claimed backward walk is not a premise and was not rerun.
