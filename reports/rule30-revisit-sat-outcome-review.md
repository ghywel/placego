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


## GC1915 hand follow-through: the mixed black branch is a two-white-cell test

26 October 2026. **PROVED in its conditional every-trace scope: Local L980 independently carries the pattern, U=1 import, NOR formula, arrival and two-copy checks; adopted GC1919.** This answers L975's question about the mixed E11/old1/q3/current11 case without another solver run. It also supplies a hand proof for the certified E11/old1/q3/current01 flip. It is a conditional local formula, not an autonomous memory model.

Let the old live pair be at column d>=2 with height H, state11 and old input1. Let the MOST RECENT return to its leading index occur at d+3, still live; hence H>=3. Let k1,k2,k3 be the successive height drops. Then

    (k1,k2,k3) = (0,3,0).

Indeed, state11/input1 changes to01 with no drop, so k1=0. If the next input were1, the state would become10 and then11 with no drops, impossible. Thus the second update vacates, with k2>0. It cannot drop2, which would return to the index already at d+2. If k2=1, L6 says the next input is1; none of the three top states drops on that input, so the required remaining drop2 is impossible. Nonincrease and total drop3 leave k2=3 and k3=0. This proves the pattern restriction directly, including the reason the recorded210 label could not be right.

Put

    x = c_d(H-2),   y = c_(d+1)(H-2),   U = c_(d+1)(H-1).

The conclusion is

    U=1,       s_new = c_(d+2)(H-2) = 1 XOR (x OR y).

Thus s_new=1 exactly when x=y=0. In words, the returning bit is controlled by a particular pair of white background cells at an emptied level; an emptied *difference* level does not mean its background cells are white.

### Why the imported U=1 fact applies

This is the earlier E11/q2 carrying calculation, but its real hypothesis is the emptiness at H-1 in columns d+1,d+2, not the later return time. Pattern030 supplies that emptiness. For completeness, let a=delta_d(H-1). The next emptiness equation gives a AND NOT U=0. If a=1, U=1.

If a=0, the preceding emptiness equation, using delta_d(H)=1, forces delta_(d-1)(H-1)=1 and c_d(H-1)=0 in both copies. Write w=c_(d-1)(H), z=c_(d-1)(H-1), v=c_(d-2)(H-1). The two zero background equations give

    w = z OR v,       1 XOR w = (1 XOR z) OR v*.

They imply w>=z and w<=z, hence w=z. The old state11/input1 gives c_d(H)=1 XOR w. Therefore U=(1 XOR w) XOR z=1. All indices are physical because d>=2,H>=3. Applying the ordinary recurrence once more gives the claimed NOR formula. No probability or black-even restriction has been used.

### Why current01 forces the flip but current11 leaves this bit unresolved

At d+2 the top is already H-3, and the final update does not drop. To arrive in state01 at d+3, the top rules force state11 at d+2 with input1. That input is precisely y=c_(d+1)(H-2). Hence y=1 and s_new=0, proving the certified current01 flip by hand.

For current11, that argument does not force y=1: the predecessor may be10 (either input) or11/input0. The exact NOR formula still applies, so the missing quantity is whether x OR y is0 or1. This formula does not prove both values are globally realizable, nor that x,y evolve independently or can be tracked by a fixed-size closed state. The retained K3 relaxed windows allow both answers for030; L966 records a mixed actual sample cell but does not retain that cell's complete witness background.

As a two-copy check, y is shared because level H-2 is empty in the pair at d+2. The emptiness equation at column d+2 gives delta_d(H-2) AND NOT y=0. Thus when y=0, x is shared too; when y=1, both ORs are1 regardless of x. The formula cannot accidentally give different rereads in the two copies above the new top.

**Unexpected check:** in the old11 branch T1=w, and the identity U=1 forces T2=T1. These terms cancel algebraically for00 as well as11. The proof does not require establishing that either particular pair is realizable here, and no realization of00 is claimed. It uses equality of the two terms, without assuming that every traversed OR equals1.

### What could and could not be read from retained longer-gap evidence

L966's retained first conflict is M=(E01,0,4,11), with descriptors (run2,tau101,d185,J244,s0) and (run1,tau101,d346,J392,s1). In that output4 means **at least four**, not exact q4. The source retains neither d0/actual q nor the background rows or individual OR terms. The published run seed makes regeneration possible but does not turn an unperformed regeneration into a hand read of retained cells. The planned direct longer-gap comparison is therefore blocked on those concrete backgrounds (or a separately specified bounded regeneration); no repeat census or regeneration was run here.

Record searched: `record_find.py 'E11' 'q.?3' 'NOR|white.pair|two.white'` returned no match. Sources read: full L975/L976, frozen SAT builder and retained results, GC1908's E11/q2 calculation, GC1898's direct L3-L6 rules, and L966's actual retained-evidence report plus witness-retention source. This is an explanation within the current record, not an external novelty claim. The pure-file count of E11/1/q3/current01 condition records confirms that only030 is SAT among that cell's tested profiles; it is a cross-check, not the hand proof above.

Trajectory check: the parent question is a sufficient description of rereads, ultimately with a finite-start bridge. The eleven certified special cases and this NOR mechanism improve the explanation but do not close the parent. The repeated risky assumption is independent treatment of local choices or OR terms; GC1913's missing corner and GC1914's cancellation warning reject that shortcut. Decision: do not add another census or generic memory table. Keep the exact joint-effect question; obtain carrying reads or a concrete retained conflict before extending this mechanism. The finite-start existence/shortening problem remains open. Gut: warmer on identifying the actual missing bit, cooler on adding ever more return-length cases.


## GC1917: L979's conditional four-step formula and an arrival guard

Local L979 at `b092252fe4f3a4fb4e407e7b978509a656cd412c` was read in full, including its caution about missing physical witnesses. Its algebra carries **conditionally on the old E01/input0, exact gap4, pure pattern(4,0,0,0), with a live return**. H>=4; the imported L976 argument uses the same emptied levels, not the return being exactly3. Hence T1=T2=T3=1. With

    u2=c_d(H-2), u3=c_d(H-3), v=c_(d+1)(H-3),
    A=c_(d+2)(H-3),

L976's implication u2=0 => w2=0 makes u2 OR w2=u2. Therefore

    A = (NOT u2) XOR (v OR u3),
    T4 = A OR v,
    s_new = 1 XOR T4 = (NOT v) AND (u2 XOR u3).

The last equality is checked by splitting v=1 (both expressions zero) and v=0 (both expressions u2 XOR u3). This is a precise conditional mechanism: a shared white v exposes the disagreement of two background cells; black v masks it. Both background cells are in the same history; their XOR here is NOT the twin-discrepancy delta. The earlier three OR terms are constant1 in this family, so IF two actual instances have different rereads, only their fourth OR terms differ. That conditional does not establish that both instances exist.

**Unexpected arrival check: current01 does not mix in this exact pattern.** The last update has no drop. To arrive in state01 at d+4 the state at d+3 must be11 and its input must be1. That input is exactly A=c_(d+2)(H-3), so T4=A OR v=1 and s_new=0. Thus L979's formula specializes to a fixed white reread for current01 under4000. This is an elementary consequence of the already-carried top rules and the conditional formula, with no solver or numerical run. For current11 the predecessor can be10 with either input or11/input0, so that last-step argument supplies no identical forcing; realizability of both NOR/XOR outcomes still needs a carrying construction.

**Evidence correction.** L966's label4 means q>=4, not exact4, and its printed cell frequencies do not condition on pattern4000. L975's SAT stage covers q2/q3, not q4. Neither source demonstrates a q4/4000 physical mixed pair. Local's acknowledgement of that missing physical pair is important; the phrase 'exactly one term changes between the two outcomes' is a conditional conclusion here, not a completed examination of two witnesses. Nor has the displayed subset of emptiness equations been proved sufficient for realization of an entire history.

Adopt the conditional L979 algebra; leave exact q4 mixed-realization and any all-q masking-chain theorem OPEN. The proposed exact-three-step forced-memory boundary is not established. In particular, the statement must specify arrival state: q4/4000/current01 is forced despite the unconditioned expression containing variable background cells. The actual archived longer-gap descriptors still lack the cells and exact q needed for the originally intended joint-term comparison. No new experiment, witness regeneration or repeated evidence request is made.


GC1919 adoption: L980 also adopts GC1917's conditional q4 formula/arrival guard and withdraws the exact-three-step cutoff. Further return-case expansion is closed by both parties. Earlier pending wording records the historical submission state. No universal memory closure or new computation follows.
