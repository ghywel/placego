# Proposition 9 (computed): the first entry to period 64 in the rooted tree is at depth 65,821,413

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "22. Proposition 9 (computed):
the first entry to period 64 in the rooted tree is at depth 65,821,413"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

No history reaches a repeat length of sixty-four before about 65.8 million steps.

**What it says.** Following all sixteen histories further, side by side, the first one to double its repeat length again, from thirty-two to sixty-four, does so after 65,821,413 steps. Every other history is still at thirty-two at more than 67 million steps.

**Why it matters.** The number of steps each doubling takes, measured against the repeat length, has jumped from about 2,746 to over a million. That is finite evidence that the doublings keep slowing down, though not a proof that they always will.

**An everyday picture.** Runners on many paths at once: the first to cross the line sets a time that every other runner is known to be slower than, because everyone else was still running when the first one finished.

## The formal statement and proof

*Where:* CLOUD-LOCAL.md, TM6 (2026-10-07 14:54), chat L180; `tests/probes/lexicon/rule30_tm6.c`, with its header's correction after GPT's GC288. *Bears on:* PERIOD-TWO.md Q7, gap 2 (the record of $R_6$); G204, which uses it. *Status:* certified by computation (Local, 2026-10-07); second reader wanted.

**Proposition 9 (computed).** Every rooted history has $N_6 \ge 65{,}821{,}413$. Equality holds on exactly one
history up to rotation: the one entering period 32 at $N_5 = 667{,}052$. Its period-32 stage is a single excursion of
65,154,361 steps, ending at an odd zero. No other history has a zero driver at period 32 below depth 67,108,864. Hence

```math
R_6 = N_6 / 64 \ \ge\ 1\,028\,459.58 \quad \text{on every rooted history.}
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

*Independent backward certificate (Local, 2026-10-07 15:25; `rule30_tm6_backward.py`, TM6-B).* The backward pair map
$B(y, z) = (Sz + (y \lor z), y)$, which uses neither the forward constructor nor the C kernel, takes the minimum's
exit state (driver 3,864,731,681 at depth 65,821,412) to the root $(0, 1)$ in exactly 65,821,412 steps. On the way
it meets zero drivers exactly at 667,051, 537,692, 485,619, 445,474, 350,243, 243,767, 174,449, 165,748, 72,575,
53,207, 399, 28, 7 and 2, so the equality case is certified twice; the bound on every other history rests on the
lockstep alone.
