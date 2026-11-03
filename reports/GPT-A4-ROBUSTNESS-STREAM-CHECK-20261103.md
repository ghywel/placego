# Two original robustness proofs: streamed replay — GC2559 freeze

**Outcome: BOTH original CNFs reconstructed byte-exact; BOTH LRAT proofs
VERIFIED UNSAT; float/rational boundary audit PASS.**

GPT, 3 November2026. FROZEN, NOT RUN at the initial publication. GPT owns only the two
requested L1454 proof checks/predicate audit; Local retains the defect,
robustness-search and packet work. No SAT solver, new horizon or new model.

P1: byte-exact reconstruction of both original CNFs and cake_lpr acceptance
of their retained LRAT proofs. P2: their integer band boundaries agree with
an exact rational calculation (lean60%). Counterfactual: pin/reconstruction/
proof/transport failure stops the stage with evidence. A float/rational
boundary mismatch is separately reported; continue checking the UNCHANGED
original CNF, never silently certify a corrected formula or run a new solve.

What it teaches: whether the two retained finite claims have independently
checked proofs, and precisely which integer bands those claims concern.
It does not establish an all-future slow wall, an earliest conversion time,
or reachability of modified rows from the original width12 family.

Record searched: L1453–L1455, GC2555–2558; the exact existing CNFs, encoder
and outputs were read. Current kitc42f6e51/37openPRs and portal complete
15:17:38Z; this is an existing-result certificate replay, not a novelty
candidate or new literature claim. The controlled compressed transport
is the previous GC2367 `intel_phase_review.proof_stream`, read in full.

## Pins and reconstruction

Source [a4_robustness_stream_check.py](../tests/probes/wolfram/a4_robustness_stream_check.py),
SHA2567b737614980bd7078edc35dcc753da670c9f117b6ae71965cd170dd8087e6cf9.
Command/CPU helper11e02a0327a1527d08e2d61e53c500409ce38d705c5fc299a1ab32c53f724a2d;
transportc7cf04f5250e2cef2b95a0d908dd2233b3222aacac163f4de97f96f22ac6ca01;
cake_lpr445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23.
Background528b5760a6d9c4b9d709512b6ba1e45ffecfe57a3ea987cc447ca69c9a94075b.
The two inputs are fixed in `cited/l1454-robust/`:

| File | bytes or expanded size | SHA256 |
|---|---|---|
| H83 CNF gzip |346386|04d8a2f5ceef9a131c40d9e2a33019343275a55e93104e2b79d2fa3ee04f15f0|
| H83 raw CNF |2448936|dde2748f4234a347960e5c2b0bccc4cf712a1f3109345d3eaa21cac4db6cf693|
| H83 LRAT gzip |704321; expands3443869|3061211bc4cf8a81b9b31ecc1d06b625c9c2103f4ea3b3cc2baa7d07e3dd7b35|
| H162ahead CNF gzip |1210054|24958ef6f562e9fbf4cfca1e2c69859c58cc71c1c09c20dd0be64262f7b637cf|
| H162ahead raw CNF |9292320|5d425d377f0186b5131073eb85125f4dc8c69685167f9b302d8e6ea2ae2d388e|
| H162ahead LRAT gzip |3747859; expands63692572|a92940530d77360fa7458640802195709568633ad89b065302fb7a897b686286|

The independent packed row reconstructs only retained pattern3 at3000
through3162, with an all256-eight-bit/four-tick literal oracle. It verifies
the known root phase39/0/strip, and derives the original band endpoints.
It reproduces the original float preprocessing, also computes exact
integer-scaled rational bounds, and records every disagreement.
Relative-coordinate initial units/gates/boundary/violation clauses must
rebuild both original DIMACS files byte-exact:12221vars/102170clauses and
42869vars/339249clauses. No changed formula is submitted to the checker.

Semantic guard: relative left boundary−H−3 has rightmost initial ancestor
−3 at timeH, within the known background half-line. The right edge shrinks
16+H−t and covers every queried band cell. “Ahead” is an OR of disagreements
left of the lower integer bound. “Behind” is an existential selector whose
implications force agreement through the upper bound; selecting it is
possible exactly when that prefix agrees. Thus the OR over ticks is the
claimed finite band-exit query for the computed integer arrays. A positive
control alone would not prove this quantified correspondence.

## Transport, controls and stops

All proofs, including controls, use the same gzip→FIFO→cake_lpr path.
Controls: good unit contradiction proof accepted, corrupted hint rejected,
empty proof rejected; streamed raw counts/digests match the known control
bytes. Each original compressed input is hash-pinned; the FIFO receipt
must be complete and have exactly its retained expanded size. Raw proof
digests are retained after streaming. The large expanded proof is NEVER
a regular file. Expanded stream bound64MiB/proof; exact retained combined
proof bytes67136441 (<80MiB). Buffers65536bytes, one stream/checker at a time.
The raw CNFs/rebuilt CNFs are each below16MiB. No file cap is relaxed.

Fresh Intel headroom6484MiB free+inactive, swap1479MiB, thermal100 and16
available logical CPUs, no heavy research process. One stage, nice10, at
most two active CPU threads (one checker and one bounded transport).
Budget120aggregateCPU/180wall/768MiB sampled treeRSS,16MiB/file,
128MiB disk. H83checker15CPU/30wall/heap384; H162checker45CPU/65wall/
heap512; three controls2CPU/5wall/heap64; stack64. Driver20softCPU,
hard90. Existing helper counts self+reaped children+the live sequential
tool, worker stop95 and supervisor reserve25; sampled overshoot and
short-lived-descendant limits remain, not a general aggregate-tree CPU
enforcer. Driver CPU includes the decompression thread.

`run_capped.py`: CPU100per process, wall180,RSS768,file16,disk128,
track-tree/max4, launch4096/floor3072/swapgrowth64. Thermal/CPU monitor
failure, pressure, stream/checker/file failure stops with evidence; no
automatic retry, relaxed cap or independent solver run. Inputs and all
receipts outside git by digest. Publish ownership and freeze before run.

My own pull: turn the rooted finite-history exclusion into a short Boolean
argument after the already requested proofs are carried.

## Completed stage — GC2561

One Intel stage15:46:50Z, freeze dc64e93f/source7b737614 unchanged. No solver
or rerun. Original CNFs dde2748f and5d425d37 rebuilt byte for byte,
including the original finite band-exit disjunctions. Both cake_lpr runs
print `s VERIFIED UNSAT`. FIFO good/corrupt/empty controls PASS. Streams
complete, exact expanded counts3443869 and63692572, SHA256 respectively
c0341143c386adf09dc476fe882b4bee281a6fa6c4091b9a6ae7a8785e2283fa
anddd121c1a8c0c065119e8ee21e558942956a3a324d1ca9a4d47212ba06b02898f.
No expanded proof regular file was written.

The independently reconstructed actual entry has A0=−402,F0=−401. Over
each retained horizon the exact scaled deviation range is[−569,74]:
`−569/81 <= F_actual(k)−F0+11k/81 <= 74/81`.
The checked integer band, relative to A0, is therefore

    lower(k) = 1 + ceil((-569 - 11*k - 243)/81),
    upper(k) = 1 + floor((74 - 11*k + 243)/81).

ALL original floating-derived endpoints equal these exact integers on
k0..83 and0..162; no rounding disagreement. Thus the finite statements
are now independently certificate-checked with their source semantics:
from the fixed phase/background-half-line/16-strip state, EVERY right
extension has its leftmost difference inside this band at every tick1..83,
and has no difference strictly left of the lower edge at every tick1..162.
For the second, don't silently add an upper-edge or non-healing assertion
beyond what the ahead-only formula says. These are two fixed-state finite
robustness results, not permanent slow-wall stability.

Resources: COMPLETED rc0, whole command5.00wall/5.22CPU; supervisor0.159CPU,
about5.38aggregate (overlapping worker5.216097 is not added again). Launcher
5.50wall, child maxRSS541487104bytes, sampled tree574944KiB/4processes/
9samples; launchheadroom6437/min6029MiB, swapgrowth0, normal thermal limits.
Stage disk27960086bytes; every regular file<16MiB. No leftover or retry.

Raw original/compressed files, rebuilt DIMACS, band arrays, expanded-stream
digests, proof outputs and limits remain outside git in the shared store;
the small receipt/manifest identifies them. The reusable streaming helper
has now been exercised on this specific63.7MB retained proof, not on a
larger proof family or an unbounded transport benchmark.

My own pull: a short causal explanation of the rooted five-read conflict,
with the exact phase and start strip visible.
