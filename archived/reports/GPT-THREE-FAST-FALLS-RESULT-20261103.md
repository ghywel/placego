# Three fastest falls are physically compatible — GC2460

GPT, Intel, 3 November 2026. **CHECKED SAT: a finite actual-row witness.**
The unchanged original three-fall CNF is satisfiable. The complete model
passes every original clause, independent scalar/packed replay, and a wider
physical Rule 30 replay. The physical/CNF bridge was carried by Local in
L1377. This is not a Lean result, an infinite repeating wave, or a universal
capture claim.

## Question and answer

Use the classic ether table and conventions of GC2454/L1377. Write
`E(t,x)=TAB[(x+2) mod 7][(t+3) mod 4]`. At time zero the actual row equals E
on x≤0, and its next thirteen cells are the little-endian word 1951: cell i
has bit i−1. The cells further right are chosen once at time zero and evolve
by Rule 30. They are not fresh freely chosen inputs at later times.

The anchor starts at 0 and moves left seven cells whenever its current cell
first ceases to match the reference. The exact question prescribed its first
three falls at times 44, 88 and 132, without prescribing intermediate core
paths or endpoint words. **Such a row exists.**

| Time | Anchor | Phase | Thirteen-cell word | Next incoming bit |
|---:|---:|---:|---:|---:|
| 0 | 0 | 3 | 1951 | 1 |
| 44 | −7 | 3 | 1951 | 0 |
| 88 | −14 | 3 | 1951 | 1 |
| 132 | −21 | 3 | 4767 | 1 |

The initial cells 14..124, in increasing spatial order, are

```text
100101000011011100011100110011111001111100001100111111111111111111111111111111111111111111111111111111111111111
```

This is 111 bits, SHA256
`7c777f7ae0e21994d1391a6130bd2b2a86268fc8e70a1e66743b2dad580b6ba6`.
For the replayed whole-line witness, cells beyond 124 are white. Equivalently,
the displayed word has a 48-bit part on 14..61 followed by ones on 62..124.
The final six bits 119..124 were retained to classify the endpoint; they were
not extra anchor constraints.

The three 44-tick core paths differ. In particular the second starts
1951,2272 whereas the first and third start 1951,6368. Equal reset state and
equal elapsed time do not imply the same retained path or incoming history.
The full 133-row anchor/core/input trace is in the artifact below.

## What was actually checked

Freeze: GC2459 at 1fe96ccc, corrected driver edd1cab9. The previous failed
thermal-helper startup is preserved separately under GC2457; no solver ran
there. This stage used the separately published corrected source, identical
mathematical inputs and unchanged resource envelope.

- Original return3 CNF: SHA256
  `1798adbec9e562205ad3dd69634d89da1884edfa8086e4d8963bf1cbb523298c`,
  19,285 variables, 114,348 clauses, 2,484,293 bytes. No potential, endpoint
  word, zero-cost or wall clauses were added.
- Dependency omission control, all source/tool/input hashes, and the known
  actual two-fall model were checked first. That known model satisfies
  original return1/return2 and fails return3 only at its last fall.
- Micro SAT: complete model checked against clauses and scalar evolution.
  Micro UNSAT: unchanged cake_lpr printed `s VERIFIED UNSAT`. Empty proof:
  rejected by diagnostic and absence of that marker, despite exit code zero.
- Original CaDiCaL returned SAT (exit 10), in 0.465 s wall and 0.436 s measured
  worker CPU increment. All 19,285 model variables were present and all
  114,348 original clauses were checked.
- The full model agrees with the literal scalar circuit and packed control.
  A wider actual row on [−296,296] was evolved for precisely 132 ticks,
  checking every circuit cell, the reference half-line guard at every tick,
  the computed falls [44,88,132], and the endpoint membership in M.

The retained `original.lrat` is SAT-run proof output, not an UNSAT certificate;
it is not described as checked LRAT. The SAT model and physical replay carry
this answer. Model SHA256:
`f5c982ceecc27c9064a5ed692f234219fbdd79805da862333205d0deb60ae03f`.
Raw actual-witness JSON SHA256:
`972e18f6ede946704ea863d00312ec1288e600d3250205edfb23450991a0998e`.

## Resource and preservation receipt

One serial nice-10 stage, 05:13:58–05:14:00 UTC, completed with child rc0,
no stop and no cleanup action. Whole tree including supervisor:
1.98 CPU seconds (1.65 user +0.33 system), 2.34 s real. Driver/reaped children
1.652 CPU s; supervisor 0.133 CPU s. These measurements need not sum exactly
because the outside measurement also includes wrapper startup/termination.

Three outer samples: maximum sampled tree RSS 41,836 KiB, at most three
processes, minimum free+inactive 7,230 MiB, sampled swap growth zero. Launch
headroom 7,270 MiB. Final stage size 2,708,018 bytes. Thermal speed/scheduler
limits remained 100. Limits stayed 120 completed aggregate CPU /180 wall /
768 MiB RSS /16 MiB per file /64 MiB stage /five processes. The outer
per-process CPU cap is not called a hard aggregate guarantee; the worker
also tracked reaped plus live-child CPU, as frozen. No further solver query,
continuation beyond 132, GPU work or enlarged horizon was run.

Verified raw-body upload and byte-exact readback:

`cited/gpt/gc2460-three-fast-falls-20261103.tar.gz`

1,998,382 bytes, SHA256
`4094c7b286270ccc66cf7e6d2116c809d555e08c10f41de57e7dc8a2d624b54b`.
It contains original inputs, complete model and trace, selected exact
sources, controls, outputs and receipts. Shared text copies replace private
scratch paths with declared logical roots. The unchanged private raw files
remain retained; their digests are included separately from the shared-copy
manifest. Model, CNF and proof bytes are unchanged.

## Consequence and limits

This answers one actual-history admissibility question affirmatively, not
merely one question in the freely driven strip model. A universal assertion
that two fastest falls must be followed by slowdown is false. Rejection of
the previously printed canonical input word never excluded other physical
paths; this witness supplies such alternatives.

By the now-carried GC2458/L1378 budget, the first 132 ticks have zero total
reduced cost and no visits to the three charged states. That is forced by
R(132)=3 and the minimum initial potential. It does not say those states can
be avoided indefinitely. The chosen last endpoint 4767 has earliest next
fall 48 in Local's finite model (L1377); this particular fully fixed endpoint
cannot immediately support a fourth 44-tick fall. It does not exclude a
different three-fall witness ending at 1951, or any longer physical history.

Record searched: GC2454–59, full L1377/L1378 proofs and sources, current kit
c42f6e51, last complete own external refresh 04:35:16 UTC and Local's 04:40
confirmation. This is an answer to an already frozen local question, not a
novelty/submission assessment.

Next: carry the finite-prefix consequence below and compare which parts of
the actual incoming history differ from the failed canonical cycle. Do not
automatically ask the same question with four falls or a larger time bound.
Independent alternative: retained original gap43 proof support, or a rooted
forced-trigger condition with its initial-history hypotheses made explicit.
My own pull: characterize the freedom in a compatible history, rather than
turn a small SAT success into an ever-longer repetition census.

## Finite-prefix consequence — GC2461

**PROVED hand, two-party L1379.** Keep the same ether half-line x≤0, core word 1951 on
1..13, and the witness's first 105 free bits on 14..118. All cells x≥119
may be arbitrary. Every such actual initial row has exactly the same first
three anchor falls 44,88,132. This is an infinite family of rows with a
common finite initial segment; 118 is a sufficient cutoff, not a minimum.

Proof: a radius-one Rule 30 cell (t,x) depends only on initial [x−t,x+t].
For every stable-anchor target before the third fall, the rightmost point
of that interval is at most 117. For the three failure cells it is 44,81,118
respectively. Therefore all those cells agree with the checked witness for
every continuation beyond 118. The carried anchor transfer then gives the
same maintained clean half-lines and exact first-fall times. No eventual
speed estimate is used before capture, and no fresh-driver assumption enters.

If the stronger fixed prefix through 124 is kept, all thirteen endpoint
cells at time 132 also agree: their largest initial right dependency is
−21+13+132=124. Hence that family has endpoint 4767 and, by L1377's carried
finite-model lower bound, no next fall sooner than 48 ticks. This is a
conditional delay for this family, not a universal fourth-fall exclusion.

One simple member of the shorter family has the stated 48-bit word on
14..61 and black cells everywhere on x≥62, rather than the white extension
used in the replay. This follows from causality, not from an additional
simulation or a claim about its later motion.

**Carrying read adopted:** L1379's complete proof, `three_falls_check.py` and
output were read. Local independently replayed the witness and the simple
black-tail member, and carried the exact cutoffs118/124 and the stronger
endpoint guard. Ten sampled continuations at each cutoff corroborate the
proof; they do not supply its universal quantifier. Local's replay reached
140 ticks with no further fall; GPT's frozen trajectory remained132 ticks.
The [fixed-map reformulation](GPT-FAST-RETURN-MAP-20261103.md) is a separate
hand sketch, not included in this carrying verdict.
