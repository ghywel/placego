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

[KIMI-ONBOARDING.md](kimi/KIMI-ONBOARDING.md) and [KIMI-QUESTIONS.md](kimi/KIMI-QUESTIONS.md) to
[KIMI-QUESTIONS-5.md](kimi/KIMI-QUESTIONS-5.md): the onboarding written for Kimi, a model that took part early on, and
the five sets of questions it raised. Several became leads of the record, and the probes and the site still cite them
by name (for example the carry of Rule 30, from KIMI-QUESTIONS-5).

## Retired handovers

- [CLAUDE-INTEL-HANDOVER.md](CLAUDE-INTEL-HANDOVER.md): the handover for the Claude that worked on the Intel MacBook
  ("Intel"), a party suspended since 13 October 2026. The rules written for suspended parties stay in force for the
  day they return (AGENTS.md item 16).
