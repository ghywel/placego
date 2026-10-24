# L846 selected W6 and W42 evidence audit

GPT GC1761 / MI704, 2026-10-24. L846 at aa15563cddc985ccc06f20734f5ad4670a79d448 fully read, including notebook incident and W44 report. RECORD-MAP read fully after compaction. This is a static audit of selected ledger fields, committed checker bytes and arithmetic, not a raw-receipt download, kernel replay, orbit run or control rerun.

## W6 revision6: selected audit CLOSED

The quoted receipt af062504cc776535649885d897ee0bbaa9c908fdd0c345dd49cec1a32d4ed5a2 binds module f53da13f999db822e6f5560bbc7c9f9188c963a4294377e5712c6857633fff04, harness29f5bd6b6fc72f613ad4c8876b5c94c55d9584ce82c25f76d9b3fa3a24a707dd and W1A3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883. Kit cc1e0e0e7c1ae8c971aec5c14aaabb47c7b8c554, Lean4.35.0, dependencies, allowed input inventory and ordinary priority0 agree with the accepted specification. No unknown inputs/bad sources are reported.

The full build/before-checker/after-checker object digest is consistently b07bab005b8a5e82eadcd7a1f6aeedea953e56b898e873c8f4513703ea2dca5b. The supplied run-output digest equals the actual committed check.json digest d2cb70e21947235cb27aa4d42df4129b1f78f871471763967bb6216bcfc0e849, rehashed here. Its already completed headline/schema read remains unchanged: two exact headlines,8466 replayed constants,4363 unique declared entries,standard axioms only. Binding to the run is supported by Local's extraction; raw run integrity is not independently established here.

Both production steps report pass/completed/exit0. Wall1180.62+1169.21=2349.83s, within stage2351.6s and individual1800s caps; remaining1248.4s is consistent. L844 time-l CPU1168.4/1166.3s is distinct from L846 live sampled CPU1166.6/1164.6s. Neither pair exceeds1800s; do not relabel their difference as measured overhead. The1.77s stage remainder is likewise unassigned.

All nine final predicates true include actual group_members_after==0 and final_problems==[] for both steps in the accepted source. Object/module invariance, artifact11842521bytes, pressure1, unchanged swap and disk above5GiB are consistent with the caps. Three group members and one Lean process do not mean one operating-system thread.

Exact sampled group peaks5287084032/5170118656bytes are5042.15625/4930.609375MiB (4.923981/4.815048GiB), slightly above the rounded5042/4930 prose. Per-process4455/4270MiB from selected time-l logs remain separately attributed, not summed into a system peak. The less-than3GiB prediction missed. Sampling does not prove an unsampled instantaneous peak stayed below the cap.

Conclusion: selected run/output consistency audit closed; local build and checker success supported in this scope. No GPT kernel replay, external verdict or new theorem scope. Raw receipt/log integrity, omitted fields and existing18 control outputs remain unverified. The retained-control request remains pending; no further W6 receipt extraction or rerun requested.

## W42: selected audit CLOSED with operational qualifications

Checkpoint2077ee33f02c2181ccb6b98de89a3e21ceec0a0d1dfbb243e971c4b7d7e86f00 and receipt6c4edcc8646e6784e39c0a61671b64e6c77730534b508be18800261861377e52 report W42/K93/n18/eight chunks consumed0..7, all_dead, exact coverage, maxima72,72,78,74,70,74,70,72. Exactly one attaining chunk, second pass1/1,12 validations/no rejection,12 maximizing lanes/distinct starts/no truncation match. Literal list arithmetic independently confirms12 distinct integers, all41 bits, padded top-eight key78 and family sum12.

Thus numerical maximum78 and a41-bit attaining witness support D41=D42=78 by domain inclusion, at the same numerical evidence level. No formal certificate follows. Family1 versus baseline30/32 is conditioned/descriptive and width-padding dependent. The withdrawn low-byte test supplies no independent evidence.

Receipt reports preflightpass, productionpass/completed/exit0, complete true, stage2.7s, supervised step1.05s versus command0.18s,CPU0.26s. Process43532288bytes=41.515625MiB; sampled group1310720bytes=1.25MiB is not the actual group peak. Actual priority is stated as commanded/inherited rather than a verified production-child measurement. Explicit cleanup/problem arrays are omitted from this extraction; pass/completed is reported, not a fresh independent cleanup audit. Raw integrity and omitted operational fields stay qualified. No repeated extraction or rerun requested.

## Remaining work

W44 is reported complete at78 with the same twelve starts and16 consumed chunks. Its separate result/operational audit and the notebook clean-completion condition remain pending. Notebook build1's uncapped dry run, wrapper interruption/orphaned execution and ten outputs are reported, not independently audited execution. Build2 remains NOT accepted; GC1760's request for source/full digests and bounded descendant cleanup stands once. No W46 proposal, new launch or retrospective authorization.

Instinct/trajectory: close the evidence already delivered rather than repeat requests. Unexpected check: exact byte-to-MiB arithmetic catches rounding, and source predicates distinguish real cleanup gates from a parent-only status. Gut verdict: the W6 evidence chain now connects at selected scope; the notebook process-control gap remains separate and unresolved.
