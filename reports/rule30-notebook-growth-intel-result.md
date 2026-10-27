# Notebook growth: the Intel qualification run

GPT, 27 October 2026, GC1979. Owner-directed review and test of L1026/L1027;
schedules remain paused. Source frozen at `e6f77d33` (historical gate) and
`3782cddfd0dedf3bf8f62cb615f0208eacbafdef` (conditional search).

**Result:** the historical gate passed. The subsequent short-word gate is
incomplete because one query reached its 30-second wall limit. The length-20–24
search did not start. P1 and P2 are untested, not refuted; no plateau or soficity
conclusion follows. No automatic rerun or scope increase.

## What the question now means

Question: does a traveller need an ever-growing notebook to describe the legal
continuations? Response: the existing death criterion supplies one testable
consequence for the right-half language beside a forced alternating wall. A word
may be possible early and impossible after some age. Arbitrarily late such
disappearances would exclude a finite language presentation.

Challenge: this concerns the set of possible right-half histories, not an adaptive
observer discovering unread cells, positive information growth per tick, or the
natural single-seed centre column. A larger finite cutoff would still not prove
unboundedness. A finite plateau would not establish a finite presentation.

Better question: can we exhibit a family whose last possible age can be proved,
or first obtain reliable finite examples with retained witnesses? A missing SAT
answer is a search obstruction, not evidence that the word has died.

## Hand improvements made before execution

Let E_j(w) mean that some initial right row produces w at column 1 at physical
times 2j, 2j+2, ..., with column 0 clamped to t mod 2. Two updates restore the
wall phase. Restarting a realizing evolution after those updates proves

    E_(j+1)(w) => E_j(w).

Thus occurrence sets are nested. SAT at d-1 and UNSAT at d establish the exact
death d, including absence at every later start. There is no need to check every
subsequent time separately. For a factor v of w at offset k,

    E_j(w) => E_(j+k)(v),     d(w) <= d(v)-k

when the deaths exist. The offset is essential. Finite cones admit a zero-tail
completion on the right; that does not supply a naturally evolving left half.
These are elementary hand deductions, with a finite phase/restart control, not
a new independently reviewed theorem.

## Historical gate: passed

| Word | Last possible visible start | First impossible visible start |
|---|---:|---:|
| `0010001` | 31 | 32 |
| `1000101` | 33 | 34 |
| `00101010001000010101` | 42 | 43 |

All twelve endpoint queries agreed with these values using both a direct Rule-30
truth-table encoding and a separate OR/XOR encoding. All six positive models
satisfied every clause and independently replayed every physical cell in the
cone. Another 108 tiny membership checks compared both encodings with exhaustive
physical evolution; 512 restart cases checked the two-tick phase convention.

Full CNFs, solver outputs, positive witnesses and binary DRAT outputs were kept.
**No DRAT checker was run.** The negative answers are dual-encoding solver
evidence, not independently checked proof certificates. The same GPT checked
both encodings; this is not a Claude second read.

## Short-word gate: unresolved, then stopped

The committed phase-0 forbidden-word list generated 36 initial length-8 words;
an independent enumeration of all 32,768 initial 15-cell cones agreed exactly.
The planned gate compares all those words at visible ages 34 and 100. Equality,
with no UNKNOWNs, would exclude intermediate deaths by nestedness. Length 7
would follow by right extension and taking prefixes.

Actual completed calls:

| Word | Age | Answer | Solver wall seconds |
|---|---:|---|---:|
| `00001000` | 34 | SAT; physical witness checked | 0.317 |
| `00001000` | 100 | SAT; physical witness checked | 27.523 |
| `00001001` | 34 | SAT; physical witness checked | 0.304 |
| `00001001` | 100 | UNKNOWN; wall timeout | 30.017 |
| `00001010` | 34 | SAT; physical witness checked | 0.303 |

The driver had begun `00001010` at age 100 when the operator stopped the stage
early on the unresolved prerequisite. That interrupted sixth call has no
mathematical answer. Its input and partial log remain retained, along with the
timeout's input/log and an explicit manual-stop receipt. The driver originally
would have finished the remaining gate calls before declining the main search;
the early stop avoided work that could not pass this frozen prerequisite.

The supervisor reports `LEFTOVER_CLEANED`, driver return -15: the driver was
deliberately terminated and its in-flight solver descendant was then stopped.
Cleanup verified **zero remaining group processes**. This is not a completed
search or an unexplained solver crash.

## Resource evidence

| Stage | Supervisor wall | Sampled process-group RSS peak | Minimum free+inactive | Swap growth |
|---|---:|---:|---:|---:|
| Historical gate | 9.38 s | 49,148 KiB | 6,067 MiB | 0 |
| Short-word gate, stopped | 90.06 s | 110,880 KiB | 5,991 MiB | 0 |

Both ran sequentially on the Intel host, with no GPU. These RSS values are sampled
group totals, not system-wide memory peaks. The recorded artifact envelopes were
28,035,474 and 6,198,723 bytes before each final launcher receipt was written.
Per-call limits were 30 seconds CPU and wall; the observed UNKNOWN was the wall
timeout. Stage caps and the cumulative CPU guard are specified in the frozen
design. The interrupted descendant means the driver's time receipt should not
be advertised as a complete process-tree CPU total.

## Evidence and next action

Private write-once evidence manifest:
`cited/gc1979-notebook-test/manifest.json`, SHA256
`8ae4cda06b5772c8aabccb5d89fb79ee9671185cc3e522b3d41653c74c7df3d7`.

- Historical bundle: `gc1977-notebook-death-gate.tar.gz`, 11,110,239 bytes,
  SHA256 `74de143f833cc608548877ab98a8645f5ee64f751c8aa50b1c0e51618938cd28`.
- Conditional-search bundle: `gc1978-notebook-death-search.tar.gz`, 1,223,470 bytes,
  SHA256 `7a782035194af854b00db5266da2c4813421753f2656effb4107455a220f12ba`.

The precise reopening dependency is a cheaper, validated short-word survival
control. First ask whether the earlier D5 witnesses at age 100 can be recovered:
replaying a supplied witness is cheap, whereas the present solver had to find it
from scratch. A revised search should also avoid requiring a difficult age-160
endpoint before inspecting a possible death just after 43. Any follow-up needs a
fresh frozen design; no rerun is authorized by this result alone.

Reasoned verdict: useful qualification and a concrete computational obstruction;
the proposed asymptotic question is unanswered. Gut verdict: retain the question,
but improve the witness route before spending a larger search budget.
