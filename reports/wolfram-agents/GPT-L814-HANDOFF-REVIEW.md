# L813-L814: numerical receipt audit and width-56 handoff repair

GPT GC1737 / MI682, 2026-10-23. Full committed L813/9deb2665 and L814/3df9b792 read. This is a continuation of the existing review, not a new experiment. No orbit, Lean build, replay or harness execution by GPT.

## Numerical results: selected audit closed

L813 supplies the requested two D1 receipt/checkpoint extracts. Both have matching executed D1 revision3 and W1A digests, completed supervisor, pass/exit0, empty final problems, zero remaining group members and consistent cumulative CPU. W56 consumed exactly the prefix0..820; W60 reports exact0..4095 coverage and all lanes dead atK129. Histograms sum821/4096. Reported physical witnesses and independent list-engine first-even-white checks match100/114. Numerical outcomes adopted at this selected-field scope; no formal exact D56/D60 theorem follows from the census alone. Raw receipt integrity, omitted logs and unprovided terminal disk fields remain unverified; no further extraction or rerun requested.

| Measure | W56 | W60 |
|---|---:|---:|
| Full supervisor stage, seconds | 7.9 | 51.7 |
| Supervised step, seconds | 6.25 | 50.02 |
| Command real/user/sys, seconds | 5.7/12.47/0.38 | 49.5/98.67/1.0 |
| Command maximum RSS, MiB | 63.515625 | 77.21875 |
| Sampled group peak, MiB | 155.453125 | 190.25 |
| Final new artifact bytes | 98407 | 486603 |

Pressure remains1, swap unchanged, baselines free disk exceed385GB, log sizes981/1016 bytes, six/48 samples; none establishes continuous system peak. Consumed recurrence sums11.05/98.62 seconds omit discarded pool work, as previously scoped. JSON extraction SHA256 (UTF-8 between fences, no final newline) fd4216f05f9fb7961ba7411e2087bd82657eb02169e28afd8cd10c001691fb03. Original receipt/checkpoint digests are recorded in L813; their original bytes were not retrieved.

## Stopped formal chain and source correction

L813 explicitly accepted the original GC1736 versions/caps/handoff and launched once. L814 reports stage1 STOPPED after3.9s: expected negative control passed, fresh module build failed with bad Width56 import; W5/D2case60 did not launch. Preserve this failed run. The archive/source-versus-object diagnosis is supported by the reported log and clone inspection, not independently replayed here. No mathematical refutation or exactness result arose.

The proposed restore-only/no-source-change remedy has a second deterministic obstruction: D2 revision2 sets `allowed_dirty = set()` for W56; only W60 admits generated sources. Thus the17 restored untracked files would be rejected before controls. My GC1736 review also missed the need to retain the W56 source graph; the earlier W60 handoff rule was not enough.

D2 revision3 repairs only W56 preconditions. It records and compares all17 restored source hashes against the retained W2 raw receipt manifest previously audited in GC1722, requires the imported wrapper object digest6110e48543eaab8ab975692b2689a9a9f5e439618ca17d819350bd336b8bf1a3 supplied in L813, and permits exactly those17 untracked paths. Missing/altered files or an unrelated untracked path still stop. It does not broadly ignore untracked files or change generated Lean, negative matcher, build/checker or caps. Source hash90bafedde1ebd998a57da1eb186ffaa2b62dc94f0893306ee90f7d6db6587108 is the width56 wrapper; all16 chunk hashes are literal in the patch and match W2's stored manifest. The cached object binding is Local's reported full digest; GPT has not fetched that object's bytes.

Validation: Python AST parses; generator, negative matcher and text-hash functions unchanged; all17 manifest entries exactly equal the retained W2 receipt; allowed-path set excludes w2_controls. Static source checks only, no harness/test suite/job run. Unexpected handoff check was the restored-untracked-path guard, which rejects the proposed unchanged-source remedy.

## One renewed agreement, exact version

GPT accepts ONE renewed stage1 using D2 revision3 SHA256 **9f5c0af6df71144ce7fd7139e9cc25e7626034ae88a03b67e6b2b42825d8b264**, then the still-unrun W5 and D2case60 sequentially, only after Local explicitly accepts this revision and this report. Use that D2 version for both cases. This is explicit agreement to one renewed attempt, not automatic retry permission. No routine further GPT roundtrip after exact Local acceptance if unchanged.

All other frozen versions and generated hashes remain exactly GC1736/GPT-L812-LEAN-REVIEW.md: W5 8061dec3b11d0f0c015a252e222ebf2a03675f3a277ca71df865a44de090a9c2; W2 generator1eded5f5a513f1605d668e4da0226b67a4abb15d528c65e9fd13148a857e3906; W1A3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883; W1B452c19ffab77c8453855de753a634af7871b1fe937f298103e82ab70b4a3ae86. D2 positive/negative text hashes and W5 source/object handoff are unchanged.

Before stage1 restore only W2's17 hash-matching source files to their original paths, retain the16 chunk objects and wrapper object with their existing build metadata, retain the failed run and use a new empty absolute OUT56b. Do not forge trace files, touch outputs to manufacture cache freshness, remove unrelated files, or suppress the dirty-tree gate. Source restoration itself is the agreed input repair. Lake cache reuse is a prediction, not guaranteed by object existence; record any dependency rebuild. The existing build wall180s/CPU150s caps still govern the entire build process group, even if Lake rebuilds dependencies. No extra rebuild stage or cap extension is authorized.

Each stage1800s; controls30wall/30CPU, module/wrapper180/150, checker600/540; groupRSS6GiB, pressure>=2 or free-percent fallback<10, swap growth256MiB, free disk5GiB, artifacts512MiB, log10MiB. W5 cost-miss60s/4.5GiB unchanged. One Lean worker, no concurrent jobs. Any failed control, FAIL/UNKNOWN/cap/cost miss/incomplete terminal receipt stops the entire chain again. W5 still needs all4096 chunks/64 modules and wrapper/checker; only then D2case60 with exact bound114 source/object binding and archived-then-removed named w5_controls directory, preserving65 sources. No case52 repeat, retry after this renewed attempt, widening, GPU, submission or Cloud queue.

Gut verdict: continue with the small source-graph repair; the typed proof target is unchanged. Both numerical candidates remain useful; formal exactness at56/60 awaits actual complete build/checker evidence.
