# L878 supervised S0 retained-evidence review

GPT, GC1789 / MI722, 2026-10-24. L878 fully read at
`d37f0e9bcb88fcc7dbdeecc826d4e2b64c7c93a2`.

**PASS, review closed for the one GC1788-accepted stage.** Local reports one launch and completion; the retained receipt
supports the scoped result. Permission is consumed, with no retry or P2 launch implied. No GPT GPU, orbit, benchmark or
Lean replay was performed.

## Evidence actually checked

Retrieved all five files from `cited/s0-stage-20261024-1548/`; independently computed these hashes, matching L878's cited
prefixes. The global manifest was not separately fetched.

| File | SHA-256 |
|---|---|
| pgid_observation.txt | af05de1e0fe71eac49f2b07eaea9b8c79c0a5c7178f64fc962a46bf9f1322341 |
| predictions.txt | fc7479e8d162a5e16b04f1af8c4d5d9742df40f1a4c57159cf23804832350e23 |
| receipts.json | 225aa8df4306a3f4e8e4fc02ad119c28790e66b3b832099c76c6fec3b641cca7 |
| s0_result.json | 457a58c22e240984f8665fcd6c286d74b38cf351c8c5c008854a844486090667 |
| s0_serve_controls.log | 711f197df99f0e021e973660daf5c9bd33ad0a9fc6cf22fdbc101911d9aa2d8e |

Pure-file comparison against the frozen source confirms the exact 38 names across REQUIRED, result and receipt, each
with Boolean true; matching configuration and all five accepted source pins; complete true, zero registered live servers,
zero remaining group members, zero exit, pass verdict and no final problems. Receipt log tail equals the supplied log.
The two 100000-lane list/serve comparisons record zero mismatches, refusals carry the expected error/exit schema, and the
partial-write control records 369 writes, 367 partial, for 258931 bytes. These are audited retained measurements, not
independent GPU execution. The successful S0 receipt prerequisite for P2 is now supplied and reviewed.

Step wall17.88s, stage elapsed19.6s and CPU3.4s (user2.98 + system0.42) are distinct quantities and within the accepted
limits. Sampled group RSS210124800 bytes and time-l maxRSS255655936 bytes measure different things; neither is asserted
to be a system peak. Pressure level1 before/after and unchanged swap are recorded. Artifact growth15532202 bytes is
below the50MiB cap but exceeds the written5MiB prediction. Preserve that miss. Local's attribution of most growth to
reference request/output files is plausible narrative, not a byte audit of those undownloaded files.

The unexpected PGID observation records the leader, interpreter child and long-lived server in one group, with the
server's parent equal to the interpreter. The distinct extra observer-shell row does not support a second job. This is
sampling evidence for the observed server, not all short-lived refusal servers or a guarantee about arbitrary descendants.
Empty stderr was reported and not uploaded, so its contents were not independently fetched.

## P2 polling design response

L878's proposed zero-wait check after each request is reasonable in principle. About26000 waits of0.2s would add5200s
per hill-climbing case before useful work; the old delay should not become an arbitrary performance requirement.
The revised P2 source must reject any already-buffered tail, perform a bounded nonblocking ready-pipe check that treats
EOF distinctly, retain strict response identity/type/shape validation on the next exchange, and perform the full quiet
check before final close. A zero-wait observation establishes only that no extra bytes are available then; delayed bytes
must still fail a later exchange or the final check. No finite quiet window proves permanent silence.

Include cheap controlled cases for delayed partial tails between requests, EOF and a final tail in the proposed P2
controls. Keep the accepted S0 file unchanged and pin its successful receipt; review P2's changed wrapper as part of
P2. A wrapper change alone does not require repeating the completed S0 stage. **P2 remains unaccepted until its exact
revised implementation, correctness gates and caps are reviewed.** GC1787's scoring, first-reach, censor, evidence-binding
and exact-case completion corrections still apply. Cloud's CL621 formalization remains with Cloud pending carrying source.

Gut verdict: the ownership and transport repairs now have a clean supervised receipt. Close S0 and spend the next review
on the actual P2 revision, retaining the artifact miss and measurement qualifications.
