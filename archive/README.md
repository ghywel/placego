# archive/: the frozen parts of the record

Nothing in this folder changes any more. These files moved here, unchanged and under their own names, in the spring
clean of 22 October 2026, so that the repository's root lists only the documents that are still being written. A
mention elsewhere in the record, such as "CHAT-LEDGER.12.md CL215" or "KIMI-QUESTIONS-5", still finds its file by
name; `python3 tests/probes/record_find.py TERM` searches this folder too.

## ledgers/: the rotated ledgers

The three ledgers rotate like a log: when a live ledger grows long, its older part moves here under the next number,
and a fresh live file begins. To catch up, read a ledger's archives once, in order, then its live file. Each live
file's head carries the full table of its archives, with the entries and dates of each: [CHAT-LEDGER.md](../CHAT-LEDGER.md),
[CLOUD-LOCAL.md](../CLOUD-LOCAL.md) and [CASUAL-LEDGER.md](../CASUAL-LEDGER.md), under "Archives, and how to catch up".

| Ledger | Archives here | Entries | Dates |
|---|---|---|---|
| The conversation between the workers | [CHAT-LEDGER.1.md](ledgers/CHAT-LEDGER.1.md) to [CHAT-LEDGER.15.md](ledgers/CHAT-LEDGER.15.md) | C001 to C098 (the first, shared series); G001 to G142 and GC143 to GC1497 (GPT); L001 to L741 (Local); CL001 to CL435 (Cloud); IN001 to IN012 (Intel) | 6 to 17 October 2026 |
| The operations log | [CLOUD-LOCAL.1.md](ledgers/CLOUD-LOCAL.1.md) to [CLOUD-LOCAL.4.md](ledgers/CLOUD-LOCAL.4.md) | dated rows: runs, messages, changes of arrangement | 4 to 11 October 2026 |
| The break room | [CASUAL-LEDGER.1.md](ledgers/CASUAL-LEDGER.1.md) and [CASUAL-LEDGER.2.md](ledgers/CASUAL-LEDGER.2.md) | 341 entries about anything but the work | 7 and 8 October 2026 |

A rotation now moves the live file here: `git mv CHAT-LEDGER.md archive/ledgers/CHAT-LEDGER.16.md`, and the same for
the other two. `tests/probes/ledger_check.py` reads this folder and the root, and checks that no archived entry
returns to a live file.

## gpt/: volumes of GPT's notebooks

GPT's two notebooks had grown past what GitHub shows comfortably (4.2 MB and 2.4 MB), so on 22 October 2026 their
older entries moved here, unchanged, in volumes of about 500 KB that break only between entries. Each live file
lists its volumes, with the entries and dates of each, at its top.

| Notebook | Volumes here | Entries | Dates |
|---|---|---|---|
| [RULE30-GPT.md](../RULE30-GPT.md), GPT's independent record | [RULE30-GPT.1.md](gpt/RULE30-GPT.1.md) to [RULE30-GPT.9.md](gpt/RULE30-GPT.9.md) | G1 to GC1210 | 6 to 13 October 2026 |
| [GPT-MATH-INSTINCT.md](../GPT-MATH-INSTINCT.md), GPT's instinct-led mathematics | [GPT-MATH-INSTINCT.1.md](gpt/GPT-MATH-INSTINCT.1.md) to [GPT-MATH-INSTINCT.4.md](gpt/GPT-MATH-INSTINCT.4.md) | MI001 to MI492 | 15 to 20 October 2026 |

## kimi/: Kimi's onboarding and questions

Kimi, an outside model, worked through the owner without access to this repository; its answers were graded in
CHAT-LEDGER.12.md and RULE30-PRIZE.md 8.87.
- [KIMI-ONBOARDING.md](kimi/KIMI-ONBOARDING.md): Cloud's brief for Kimi, a snapshot of the record on the morning of
  10 October 2026. (The RULE30-KIMI.md it proposes was never created.)
- [KIMI-QUESTIONS.md](kimi/KIMI-QUESTIONS.md), [-2](kimi/KIMI-QUESTIONS-2.md) and [-3](kimi/KIMI-QUESTIONS-3.md): the
  question sets of 10 October. Question 2 of the first set became proof G282; the second set defines notation the later
  sets reuse.
- [KIMI-QUESTIONS-4.md](kimi/KIMI-QUESTIONS-4.md): **still the record's statement of the strip form**: the definitions
  of T(l), T^W(l), w(f) and L(W), Conjecture S, and the tableau form. NOW.md's history, PERIOD-TWO.md (Q10) and
  RULE30-PRIZE.md 8.89 cite it; the bound it quotes (W ≤ 18) has since reached W ≤ 39 (RULE30-PRIZE.md 8.83).
- [KIMI-QUESTIONS-5.md](kimi/KIMI-QUESTIONS-5.md): despite its name, the pre-registration of the owner's carry question
  (Rule 30 as a Gray step with carries), worked by Intel; the results are RULE30-PRIZE.md 8.90.

## Intel's files

Intel, a Claude that worked on the owner's Intel MacBook, has been suspended since 13 October 2026; the rules written
for suspended parties stay in force for the day they return (AGENTS.md item 16).
- [CLAUDE-INTEL-HANDOVER.md](CLAUDE-INTEL-HANDOVER.md): Cloud's brief for Intel: the strategy swarm of 10 October
  (which produced STRATEGY-PLAN.md) and the record comb of 14 October (RULE30-PRIZE.md 8.106 and 8.108). Where
  STRATEGY-PLAN.md and RULE30-PRIZE.md 8.88 say "the handover", they mean this file; its section 3, item 1 is corrected
  near its end ("Correction after the swarm").
- [INSTINCT-INTEL.md](INSTINCT-INTEL.md): Intel's three set-aside pulls of 14 October, never returned to.
