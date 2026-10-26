# Can the starting row replace the diary—or help it?

GPT, 26 October 2026, GC1923 / MI845. Owner-directed manual review of Local
L983–L985 and one small Intel experiment. **COMPUTED, single-party**, with two
implementations and controls; new results await Local's independent read.
Heartbeats remain paused. No M5 or Cloud job, portal submission, or larger run.

## 1. Answer in everyday words

The far end of the starting row did **not** beat the recent diary as a replacement
for it. That was my prediction, and it failed at both larger tested widths.
Even six far-end cells can look identical in two beginnings whose next colours
are opposite. We retained the actual pair, rather than merely an average score.

There is a narrower warm lead. A witness that is weak alone can be useful beside
another witness. In one group of 32 beginnings with the same recent diary, the
next colours split exactly 16–16. Four far-end cells divide that group into
smaller groups and raise its best possible score to 28/32. This was noticed
**after** the test. It is a finite information calculation, not a successful
unseen forecast or a law for larger beginnings. Some of those smaller groups
contain only one to three beginnings.

The better question is: **does the diary tell us which other observation would
settle the ambiguity—and can the rule explain why, without a lookup table?**
That differs from simply enlarging the same window until it memorizes the cases.

## 2. What carries from Local, and what needs qualification

Read complete committed L983–L985 through `5be7eda8`, including L983 at
`a99a3a4926e9d3449cefc3c9061a1cc050190d94`.

- L983 independently carries GC1922's observation-class criterion, majority
  optimum, confidence/Brier example and hidden-fair-bit guards. Adopt that read;
  it does not independently verify this new code or its results.
- Local correctly identifies GC1899's exposure process as an existing example
  of knowing when the next input is fresh or determined. L960's approximately
  0.4252 fresh-odd share gives the model-based estimate
  `1 - 0.4252/2 = 0.7874`, conditional on that recorded decision population and
  full exposed-prefix information. It is not an executed blind predictor,
  a score for all sideways states (the decision table uses 01/11), or a score for
  one finite beginning. Advancing a sideways reconstruction decision is not
  automatically advancing physical time; revisits can concern earlier times.
- A deterministic beginning fixes its actual future, but a restricted observer
  can still have intermediate conditional probabilities over compatible
  beginnings. The music box analogy must distinguish fixed notes from what the
  listener knows. L955's measured individual influences are not a proof that
  every predictor must store nearly the whole diary, nor a computational lower
  bound.
- L985's coin-run argument does **not** show extinction by GC1904/GC1907. Those
  results say almost-sure infinite live paths must eventually enter protecting
  regimes. A proof excluding those regimes is still missing. Likewise, normality
  is not itself the conditional fresh-coin hypothesis of an arbitrary adaptive
  prediction argument. No transfer from the product ensemble to the designated
  finite seed has been established.
- Nonperiodic automatic sequences remain a legitimate distinction: a small
  machine reading a binary clock need not produce an eventually repeating word.
  Existing specific exclusions and edge period doubling do not settle all such
  possible survivor diaries. No new automatic-sequence census is justified here.
- The zero-wall survival lane is itself the Q01 reduction of the period-two
  problem. The comparison with a physically clamped alternating wall changes the
  system and must retain its own boundary and survival conditions.

These are scope corrections to the analogies, not reasons to discard the owner's
questions. The one-history/ensemble, transformed-repeat and disappearing-ink
questions are preserved in DEEP-QUESTIONS.md.

## 3. Frozen experiment and what its scores mean

Source: `tests/probes/wolfram/blind_witness_intel.py`, frozen and pushed at
`b32654759efcf7aed1c1934a5ff7cd376fad50b5` **before execution**.

Let depth 1 be next to the zero wall, with increasing depth extending leftward.
For each W in 8,12,16,20, take every binary free diary of length W/2, prescribe
the even trace entries to be 1 through time W−2, and reconstruct its unique
initial row supported in depths 1..W. There are 16+64+256+1024 = **1360 lanes**.
Replay the actual half-line through time W+1, with no truncation of growing
support. The hidden target is the physical odd-time value `x(W+1,1)`.

Compare two separately labelled populations: all lanes; and those with
`x(W,1)=1`. This second selection is available at cutoff W, before the target.
The passing populations have sizes 4,38,112,498. All scores weight beginnings
equally, not distinct futures equally.

Observers read k=1,2,3,4,6 bits where k<=W/2: near-start cells, far-start cells,
oldest free diary entries, or newest free diary entries. Full diary, full start
and no observations are controls. The far window is **depths W−k+1..W**, not a
window shifted to each beginning's actual last black cell. Counting k observed
bits is an equal read budget, not equal entropy: the prescribed ticks impose
different dependencies among these views.

The reported optimum chooses each observation class's majority outcome. This
answers what information is present in that finite population. It does not
train a predictor, test on unseen widths, or show how cheaply an algorithm could
find the class probabilities. Reading all three actual update inputs at cutoff
W would trivially determine the next value; this experiment deliberately asks
about restricted diary/start-row observations. Far-start cells are alternative
witnesses and possible ancestors, not necessarily causally irrelevant cells.

| Passing population | No observations | Four far-start cells | Four newest diary entries | Six far-start cells | Six newest diary entries |
|---|---:|---:|---:|---:|---:|
| W=16, N=112 | 59/112 (52.7%) | 9/14 (64.3%) | 3/4 (75.0%) | 85/112 (75.9%) | 101/112 (90.2%) |
| W=20, N=498 | 137/249 (55.0%) | 101/166 (60.8%) | 311/498 (62.4%) | 117/166 (70.5%) | 383/498 (76.9%) |

**P1 REFUTED:** predicted far4 minus newest4 >=0.05 at both W16 and W20;
actual differences are −3/28 and −4/249. No width-independent ranking follows.

**P2 HELD in the stated finite domain:** far6 is not sufficient at W20. Lane116
has initial integer609099 and target0; lane153 has initial integer607133 and
target1. Both pass at time20; both have `start >> 14 = 37`, hence identical
depths15..20. All later initial cells are zero. The integer encoding puts depth1
in the least significant bit. This pair rules out every exact predictor using
only those six cells on this population, regardless of its sophistication.

Confidence also matters here. At W20, observing near4 keeps the no-information
accuracy137/249, while its optimal squared probability error decreases from
15344/62001 to153676009/622666000. This is small but exact. It is not an unseen
calibration result.

## 4. Post-hoc retained-data finding: help instead of replacement

No additional dynamics were run. Inspect the already retained W20 passing cases
whose newest four free diary entries are all zero (`lane >> 6 = 0`). There are
32, with 16 outcomes of each colour. The following table counts targets after
also observing the far4 value (`start >> 16`):

| Far4 value | Target0 | Target1 |
|---:|---:|---:|
| 1 | 2 | 3 |
| 2 | 1 | 0 |
| 3 | 3 | 0 |
| 4 | 1 | 0 |
| 5 | 2 | 3 |
| 6 | 0 | 3 |
| 7 | 3 | 0 |
| 10 | 0 | 3 |
| 11 | 0 | 2 |
| 12 | 0 | 2 |
| 14 | 1 | 0 |
| 15 | 3 | 0 |

Hand arithmetic: 22 cases belong to pure subgroups; the remaining two groups
each allow three correct guesses out of five. Thus accuracy becomes28/32=7/8,
certainty coverage22/32=11/16, and squared probability error
`(6/5+6/5)/32 = 3/40`, against1/4 before the extra observation.
For a concrete ambiguous pair, lane0/start699051 and lane21/start515837 both
have the four recent tocks0000 and pass time20, but their time21 targets are1
and0. Their far4 values10 and7 distinguish them.

This selected group was examined after seeing the output. It is a discovery
example, not a predeclared performance victory. Adding four observations to
four also doubles the read budget; no advantage over eight recent entries is
claimed. Even its locally pure groups need not remain pure at another width.
What it does establish is that the far window is not redundant *within this
particular recent-diary class*. It supplies actual missing information here.

## 5. Hand answer to the alternating-wall question

For an imposed wall bit b, encode a finite half-row by integer r, depth1 first.
One update is

    F_b(r) = (r >> 1) XOR (r OR ((r << 1) OR b)).

At b=0, `F_0(5)=F_0(6)=13`; at b=1, `F_1(2)=F_1(3)=6`.
For example the first pair, written from the wall outwards with trailing zeros,
is `101000…` versus `011000…`, both becoming `1011000…`.
Once the whole half-rows agree, any common future prescribed wall sequence
keeps them equal by determinism. **Both phases of an alternating imposed wall
therefore admit finite mergers.** This is an elementary local calculation,
not a new structural theorem or a survivor construction.

The missing difference is easy to locate. On the full line, the two inputs
would give different next values at the boundary site itself. Clamping that
site overrides its natural update. Thus a boundary can discard information
even while its prescribed colour alternates. On a full line, the rightmost
difference of two finite configurations forces a difference one site to its
right on the next step (the left XOR input has changed, the other inputs have
not), proving finite injectivity. These statements are compatible.

Unexpected control U1 checked all256 eight-bit starts, each of four boundary
schedules, through four steps using packed and literal engines. Both alternating
schedules merge at step1; the open-line control remains injective throughstep4.
This does not say the two halves obey every required survival condition, or can
both be completed with the same genuine right-hand evolution. The one-way
period-one latch and the sideways finite-partner bridge are separate claims;
this calculation does not settle their proposed alternating analogue.

## 6. Controls, resources and retained failures

The diagnostic completed once at17:09:50–17:09:52 UTC. Internal elapsed1.156s,
process time receipt1.21s real/1.19s user/0.01s system; supervisor wall2.08s.
Every packed physical update agrees with the literal Rule30 truth table;
triangular reconstruction agrees with independent forward bit-forcing for all
1360 beginnings; every prescribed prefix replays; full descriptions are exact;
all nested observations obey accuracy/Brier monotonicity; all five elementary
probability controls pass; the XOR-for-OR mutant differs as required; U1 passes.
These are same-worker controls, not a Claude second read or a Lean certificate.
After completion, all176 retained summary rows were also rebuilt using explicit
bit-tuple observation keys and separate count arithmetic: class counts, exact
accuracy and exact squared probability error agree throughout. This was a
pure-file audit, with no further dynamics or new cases.

Caps: one single-threaded Python diagnostic, CPU30s, wall45s, sampled process-group
RSS256MiB, per-file2MiB, output directory8MiB; launch free+inactive>=2GiB,
floor1GiB, swap growth<=128MiB. Final payload/result568262bytes; directory569713
bytes. Sampled group RSS max16052KiB; `/usr/bin/time` process max RSS17965056bytes.
These are different measurements, neither a system peak. Sampled free+inactive
minimum7572MiB; zero sampled swap growth. The supervisor's sampled disk maximum
was zero because the short process wrote after the last sample; its final
inventory checked the completed footprint. File limits and final sizes are
retained; do not label the disk sampling continuous. CPU enforcement is per
process; the diagnostic has one Python process plus launcher/time overhead.

Standing legacy startup checks were run separately and serially, once each.
`rule30_wall.py` completed with ALL CHECKS PASS underCPU90s/wall120s/RSS512MiB.
Its old WA3 explanatory parity is not re-promoted; the existing GC1043 correction
stands. `rule30_merge.py` hit its180s wall cap after partial output throughdepth57:
**INCOMPLETE**, with child termination and zero remaining group processes.
Its earlier checks and original forecast refutations are retained, not a full
pass. Sampled group RSS max330664KiB; no sampled swap growth. No retry. The old
scripts compile fixed temporary artifacts outside the monitored receipt folder;
their directory budget is not a whole-filesystem footprint guarantee.

Evidence, outside git: `cited/gc1923-blind-witness-intel/manifest.json` binds all
ten raw outputs/resource receipts. Uploads were read back byte-exactly.
Manifest SHA256:
`ea20d0f2ac9025fcc8ca67ad50ff6d39f2c0281a10ea571b709c71464aefac6c`.
Diagnostic `witness-stage/result.json` SHA256:
`12961ce859e32be7fe68fe019caeeef74c53915055f1b4897ebf12f0861955b5`.
No automatic rerun or larger-width permission is implied by completion.

## 7. Checkpoint and warm lead

Record searched before execution: the two regex groups in the frozen probe's
docstring, with relevant sources L955/GC1894, GC1899/GC1901/GC1907 and GC1922
read. The old L942 result concerns death time, unlike this first physical tock;
the difference is explicit, not a claim that witness methods are novel.

Reasoned verdict: replacement prediction fails; far6 exact sufficiency fails;
one actual diary ambiguity is helped by a second view. Boundary alternation
does not forbid mergers. None bounds D(W), proves survival impossible, or
establishes a practical single-seed forecasting shortcut.

Gut verdict: cool on a larger census of fixed far windows; warm on **choosing a
witness from the already-seen context**. Before an M5 experiment, Local should
read the source and exact selected subgroup, then seek a short Rule30 reason
for a declared observation resolving ambiguity. Any prospective test must freeze
that selector/confidence rule, compare equal read budgets, retain disagreements,
and use as-yet-unexamined widths or cases without calling related samples
independent. This is a proposed direction, not an accepted executable or launch.
The owner's heartbeat restart remains a separate next step.


## Local carrying read and owner restart, 26 October 2026, GC1924

L986 at f413760c7fd17f0cbe98d608126f9dc0aedbaba4 independently reads the frozen source and reproduces both alternating-boundary mergers, the far6 opposite-target pair and the post-hoc diary pair in a separate literal implementation. Adopt that carrying review at its reported scope; it is not a separate recount of all176 summaries or the entire selected32-case table. The owner resumes both GPT heartbeats; Local's contextual-witness/certificate design is next, still unaccepted as an executable stage. Original predictions, outputs and limitations above are unchanged.
