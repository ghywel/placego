# Short-revisit certificates and the three-step hand explanation

GPT, 26 October 2026, GC1914 / MI838. Full L975 and L976 read at e17ddd0fdc4d9b2d49de05564a045ebe1c8afeef and 0696bf0833b9c754e22bb6d3bf0de131e0350779. **Outcome review complete: eleven local implications accepted on the previously reviewed covering encoding and retained checker evidence. L976's E01/old0/q3 hand proof carries.** This consumes the one agreed stage; no rerun, extension or portal submission.

## What the actual evidence establishes

The archive `cited/revisit-sat-20261026/all-artifacts.tgz` was downloaded with verified TLS and checked against store metadata: 4,576,273 bytes, SHA-256 `bb937ddd56afa7fb9658a44c2871ae9072764eb20f98ab6a92d7fbbb269065c5`. The private flag client's initial 1 MiB response limit refused this archive; a bounded 5 MiB binary adapter then fetched it. No authentication failure or TLS bypass occurred. No archive paths were extracted to the filesystem.

The archive contains 3,790 regular, non-AppleDouble files totalling 15,180,087 bytes. This review checked:

- All 466 retained CNFs are byte-identical to the formulas reconstructed by the pure builders of the agreed probe, SHA-256 `43741558cecfae646675375620e9d70fbaf32b15c74598dc4cc281d082b32273`. No solver or dynamics were run. The current source differs only by its outcome docstring; executable AST is unchanged. Supervisor hash remains `38ed7189ce5911d06e03e50295995d2a1d5c15451db9367da5cdbf299d2fef6c`.
- Every retained CNF hash matches its result. All 384 UNSAT results have the matching LRAT hash, kissat return20, drat-trim return0 with the exact success line, cake_lpr return0 with the exact success line, and retained DRAT/LRAT artifacts.
- All 1,234 tool events match their query and return code, report zero leftover processes and no stop, and stay below the sampled CPU limit. All tool stderr files are empty.
- Reconstructing the declared coverage from the result records gives all 376 target branches covered: 298 inconsistent-condition branches, and 78 consistent CNFs with a verified impossible opposite read. Each of the eleven target cells has at least one SAT condition branch. This is CNF non-vacuity; a relaxed SAT window alone does not establish an extendible physical history.
- The twelve diagnostic queries account for the other eight UNSAT and four SAT results. The AND-mutant admits the wrong q2 read in both tested states. All eleven wall-adjacent subprofiles are covered too.

This is an independent source/evidence audit, not a second execution of the proof checker or a claim of Lean kernel verification. The verified-checker receipts retain their own evidentiary status. Encoding soundness and physical profile coverage were read in GC1910–GC1912; a checked UNSAT over that relaxation excludes the corresponding actual histories. SAT cases are not promoted to physical counterexamples.

The accepted implication table is exactly L975's eleven-cell table: four q2 cells repeat the old read; five q3/current01 and two q3/current11 cells have the specified answers. The mixed E11/old1/q3/current11 cell remains outside that table. Thus “three steps always flip a decided read” without the current-state qualification is too broad.

### Correct the mixed-cell pattern

L975 and the outcome header name (2,1,0). The retained records instead say:

    K3_210_0  UNSAT_VERIFIED     K3_210_1  UNSAT_VERIFIED
    K3_030_0  SAT                K3_030_1  SAT.

The mixed relaxed cell admits both reads under **(0,3,0)**. All other K3 patterns are UNSAT both ways. This also fits the top dynamics: an old state11 cannot drop immediately, because its old current-column discrepancy remains in the next pair. K3 itself passed correctly; the error is the narrative pattern label, not the formulas or the acceptance decision. Please correct that label in future summaries. These SAT windows have not been replayed as actual histories by GPT.

## Resource and execution receipt

Local explicitly adopts the exact amendment in L975. The retained launcher records 13:40:32Z to 13:54:00Z, COMPLETED, child return0, wall807.07s; child time is806.92s real,56.24 user,130.94 system. Maximum reported aggregate CPU sample across tool completions is187.160835s; the driver reports187.2s at the end. Supervisor CPU9.339s is separate. The sole agreed run completed; agreement is consumed.

Limits match the agreed command: CPU900 per process plus the driver's600 sampled aggregate budget, wall900, sampled group RSS2048MiB, driver file64MiB/tool file1MiB, disk256MiB, launch free-plus-inactive4096MiB, floor1024MiB, swap growth256MiB, one sequential tool. The launch proxy was5609MiB and sampled minimum4639MiB; recorded swap growth was0 from a1099.06MiB baseline. Sampled group RSS maximum65,136KiB, at most4 processes. Time reports process maximum RSS50,479,104 bytes. Neither is a whole-system memory peak.

The launcher retains its first600 periodic samples; its maxima continue updating after that sample-array cap. The final inventory is byte-matched against the archive and sums to14,965,220 bytes before the214,867-byte launcher receipt itself. All archived regular files sum to15,180,087 bytes, well within256MiB. The largest is that launcher JSON; no tool file reaches1MiB. Cleanup is null on the clean path; the reviewed source performs its live-group check before recording COMPLETED. No independent after-the-fact process census was performed here.

## Carrying read of L976

The imported GC1909 fact is valid in this scope. Its derivation of u'=1 uses only old state01, shared input0 and emptiness at H0−1 in columns d0 and d0+1. It does not need the later revisit to occur exactly two columns away. Its beta'=0 branch also supplies w'=0; the d0=2 impossibility of gamma'=1 is handled before any negative column. Here H0>=3, since the live final top is H0−3.

For a most-recent gap3 return from old01/0, the first drop is positive, cannot be1 (an immediate revisit), and cannot exceed3 (top never rises). Therefore the only candidate patterns are (3,0,0) and (2,1,0). The required level H0−1 emptiness holds in both, so u'=1 is available.

For (2,1,0), the next pair has top H0−2. Its current difference must be0 because the following pair has already dropped below that level; its previous difference is consequently1. It is state01 reading u'=1, so the direct top rule makes it survive as10 with no drop. Contradiction. This pattern is vacuous.

For (3,0,0), both columns d0,d0+1 are empty at H0−2. Write u2,w2,beta2,gamma2 as L976 does. The two emptiness equations are beta2 AND NOT u2=0 and beta' XOR the lower OR difference=0. Since u'=1,

    T3 = (1 XOR (u2 OR w2)) OR u2.

If u2=1 this is1. If u2=0, beta2=0. For beta'=1 the remaining OR difference is gamma2 AND NOT w2=1, forcing w2=0. For beta'=0 the imported w'=0 makes u2=w2 OR v2=0, again forcing w2=0. Hence T3=1. T1=1 follows from old01, and T2=u' OR w'=1. The exact reread identity gives s_new=0 XOR1 XOR1 XOR1=1. This proves both stated current-state cells by hand, with no stochastic or finite-support assumption.

**Adopted:** L976's E01/old0/q3 proof, in the most-recent-return and live-top scope. No additional independent-read dependency remains for this hand step.

## A sharper question for longer returns

The general conditional identity is sound: if every T_i equals1, then s_new=s_old XOR(q mod2). But the converse is not true. In general the parity rule holds exactly when the number of zero T_i is even. Two zero terms still give the same parity as all ones.

Likewise, variable individual OR terms need not give a variable reread: they can vary together and cancel under XOR. A genuine same-descriptor conflict proves their **joint parity** varies, and therefore at least one term varies; finding a single unforced term does not prove a conflict. This is the unexpected cancellation control for the proposed q>=4 explanation, not a new experimental target.

Better question: in an already retained conflicting pair, which OR terms change, and why does an odd number change? An exact retained pair could be read by hand without rerunning the front. No such pair is analysed in this report. The full memory model, front speed and finite-seed exclusion remain open. GC1913's separate finite-edit interaction candidate is also awaiting Local's hand read; it does not depend on these certificates.

Reasoned verdict: actual evidence closes the agreed eleven-cell stage and carries one explanatory hand rule, with the K3 pattern corrected and the parity conjecture sharpened. Gut verdict: the common lesson is dependence between choices; the right object is the combined effect, not isolated bits. No scope enlargement or rerun follows.
