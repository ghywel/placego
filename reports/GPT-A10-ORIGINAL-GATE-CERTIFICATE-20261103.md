# a10 from the original Rule30 gates — GC2581

GPT, 3 November 2026. **Hand template PROOF-SKETCH; executable check frozen,
NOT RUN at publication.** This implements the known GC2026/L1143 identity;
it is not a new local dynamics theorem. No solver, trajectory, graph
product, closure build or Lean compilation is proposed.

## Local statement and exact encoding

Let A,B,C,U,V be X(t,x-2),...,X(t,x+2), respectively, and P,Q,R be
X(t+1,x-1),X(t+1,x),X(t+1,x+1), with Z=X(t+2,x). The four gates are
P=f(A,B,C), Q=f(B,C,U), R=f(C,U,V), Z=f(P,Q,R), where
f(l,c,r)=l XOR(c OR r). The known identity B=1,C=0 implies Z=A has
two clauses, retaining both guards and both colours:

    C1 = -A -B C  Z       (A=1, B=1, C=0 implies Z=1)
    C0 =  A -B C -Z       (A=0, B=1, C=0 implies Z=0).

A minus sign negates a Boolean variable; each line is a disjunction.
No background, root, phase, active-input, deepest-mismatch or speed
hypothesis occurs in this local lemma. Its use by a monitor still needs
physical antecedents: an ignored printed zero cannot establish C=0.

The encoder writes eight clauses for d=f(a,b,c), in increasing j=0,...,7:
negate input variables whose bits are1 in j, then append d when Rule30(j)=1,
otherwise -d. The truth table is `0,1,1,1,1,0,0,0`. Complete sources read:
[original-CNF reconstruction](../tests/probes/wolfram/a4_counterword_proof_check.py),
SHA25674cc11370602258743ba7af903c0fa4acbdacadc5c109d05ec4d0f72f2721e33;
[unlaunched symmetric-cone driver](../tests/probes/wolfram/a4_counterword_realize.py),
SHA25687c01f973c6228a53ec6c1e07e4d669937db450dfd678297ddbf94b765084fc6.

## Six additions with explicit RUP hints

Number A,B,C,U,V,P,Q,R,Z as1,...,9 and the four gates' clauses as
1..8,9..16,17..24,25..32, in the order above. Append:

| New ID | Clause | Ordered hints |
|---|---|---|
| 33 | P -Q Z | 27, 28 |
| 34 | P -R Z | 26, 28 |
| 35 | -P -Q -Z | 31, 32 |
| 36 | -P -R -Z | 30, 32 |
| 37 | -A -B C Z | 7, 33, 34, 13, 19, 20 |
| 38 | A -B C -Z | 3, 35, 36, 13, 19, 20 |

For RUP, assume the clause's literals false, then visit its hints in order:
each is unit until the last is empty. This is standard ordered unit
propagation, [Cruz-Filipe et al., Efficient Certified RAT Verification,
§§2–3](https://www.cs.utexas.edu/~marijn/publications/lrat.pdf).
No RAT, deletion, auxiliary variable or external lemma is used.

For33, P=0,Q=1,Z=0: final-gate row j=2 (ID27) forces R=1 and j=3
(ID28) contradicts it. For34, P=0,R=1,Z=0: j=1 forces Q=1, then j=3
contradicts it. For35/36, P=1,Z=1 and rows(6,7)/(5,7) give the same
argument. Each masking clause is also one binary-resolution step.

For37, A=1,B=1,C=0,Z=0: ID7 forces P=0;33/34 force Q=R=0. ID13,
the Q gate's j=4 row, forces U=1. ID19, the R gate's j=2 row, forces
V=1; ID20 is empty. For38, A=0,B=1,C=0,Z=1: ID3 forces P=1 and
35/36 force Q=R=0. The final three hints give the same contradiction.

**Neither target is directly RUP in this encoding.** After its negation
fixes P, all remaining unsatisfied clauses on U,V,Q,R have at least two
literals. Unit propagation stops. The four masking clauses expose the
needed consequences; this is an encoding issue, not a failure of a10.

**Guards are necessary.** Removing B=1 is false on roots `(a,0,0,1,0)`;
removing C=0 is false on `(a,1,1,1,0)`. Both give Z=1-a after two
steps, for either a. These preserve the other guard, so the exporter
must not replace the implication by an unguarded equality.

## Original-CNF translation and support guard

L1453's original has12,138 variables and95,174 clauses, SHA256
902aa393975948ff00f775206becc648919693c95170acf134590b12d73ce9c9.
It begins with103 initial units x=-86,...,16. At update time s it has
184-s gates, with output y=-85,...,98-s, then one boundary unit. Thus
the first clause ID of gate(s,y) is

    h(s,y) = 104 + 1473*s - 4*s*(s-1) + 8*(y+85).

Its j-th row has ID h+j. Variables are allocated lazily as in GC2555's
byte-exact reconstruction; clause IDs are not variable IDs. Rebuild the
actual (s,y)->variable map, then compare all32 mapped clauses with the
retained original bytes. Sufficient support guard:

    0 <= t <= 81,   -84 <= x <= 97-t.

This keeps all four gates in the encoded region. The instance t=17,x=10
is the monitor's outside110 implication for X(19,10); the template does
not itself establish that110 from the original root or a monitored path.

The exporter assigns95175..95180 to **one** translated fragment. Several
fragments need fresh noncolliding IDs and renamed hints. These fragments
derive implications, not an empty clause: they are not stand-alone UNSAT
certificates and do not replace the existing cylinder LRAT. For a future
solver run on an augmented CNF, justify the additions first, translate
the solver proof's input/derived IDs into the same database, then check
the combined proof against the original CNF. A checker receipt for the
augmented CNF alone does not accomplish this.

**Avoid vacuity:** the full cylinder is already UNSAT, so it implies any
clause. It cannot alone validate a general forcing primitive. Validate
the template on its satisfiable root-free four-gate circuit, then check
the embedding using only the corresponding32 original gate clauses.
Neither root/path units nor the old cylinder contradiction may enter
this local proof's support.

## Fixed executable check and freeze

Source [a10_gate_certificate.py](../tests/probes/wolfram/a10_gate_certificate.py),
SHA2562ba9251e3bbde12146e1697d5e665e5c78c27e5954b09c550adc6512c2fa3874.
Only syntax parsed before freeze; no execution yet.

Prediction: both six-addition proofs pass exact RUP; cake_lpr verifies
each gate-only circuit with the negated target. All512 nine-variable
assignments match the independent scalar XOR/OR oracle, with32 models.
Direct RUP without masking fails. Counterfactual: any discrepancy or
certificate/resource/monitor failure stops with evidence and no automatic
retry, cap increase or solver fallback; the claim stays unupgraded.

Controls: known good and corrupt unit proofs; both missing-guard scalar
counterexamples for both colours; invalid RUP hint; invalid support
coordinates. Unexpected check: fixed translations(0,-84),(0,97),(81,-84),
(81,16),(17,10), checking every used original clause and only that support.
These are indexing controls, not a dynamics census. Raw artifacts stay
outside git and will be cited by digest.

Record searched: GC2580, GC2026/L1143, GC2406 positive-RUP audit; current
kit c42f6e51 lean/equivalents/catalog and cached portal/open PRs; primary
LRAT §§2–3. COMPLETE external refresh16:34:54Z, next due18:04:54Z.
No novelty/submission claim or reopening of a closed dynamics route.

One Intel CPU worker, nice10, no GPU or concurrent heavy job. Fresh17:45Z
load1.76/2.00/2.17, free+inactive6344MiB, swap1109.75MiB; thermal and
scheduler100,16 logical CPUs. Frozen stage:30 aggregate CPU seconds with
supervisor reserve,60wall,512MiB sampled tree RSS,16MiB/file,128MiB disk,
maximum4 sampled processes. Driver hard6CPU; exactly four sequential
known single-process checker calls, each1CPU/4wall, heap64/stack32.
Pinned helper11e02a03 is reused with its self+reaped+live-child aggregate
stop lowered95->20CPU; reserve10CPU for supervisor/monitor work.
Per-process caps are not aggregate enforcement; final accounting includes
worker and supervisor overhead. Sampling limits remain explicit.

run_capped.py: track-tree/max4, launch4096MiB, floor3072MiB, swapgrowth64MiB,
CPU6 per process (checker caps tightened), wall60,RSS512,file16,disk128.
Pressure, thermal, monitor failure or leftovers stop the job. No repeated
calls after failure. cake_lpr SHA256
445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23.

Success supplies a certified local primitive and guarded original-clause
exporter. It neither changes the existing cylinder result nor shows every
abstract monitored history realizable.
