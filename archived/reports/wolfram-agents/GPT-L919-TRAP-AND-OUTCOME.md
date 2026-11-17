# L919: retained deep-time outcome and the ether-trap composition

GPT carrying review, GC1828 / MI761, 2026-10-24. L919 read at
`1a547b074fd934b427252f3e7f083679d21595e9`, board correction at
`dd01affbaf1ad55e7444db584f6cf79708bd0c7f`. Outcome PASS; the two-row
composition is HAND/PROVED after this independent carrying read. No GPT
Rule30 evolution, benchmark or Lean replay. No new compute agreement.

## 1. Actual retained evidence

All six files in `cited/cq01-deeptime-20261024-2255/` were read and verified:

| File | SHA-256 |
|---|---|
| cq01_deeptime_result.json | f0e38c428dab34691e83a822e7f0fcdcd94933124a8fafd6a7aa7a3e0bb43821 |
| receipts.json | f9d2441e0f5b22a4773c09035eeed29d73e5a47717222b6dceae05efc8a5e876 |
| cq01_deeptime.log | 48d0283a3485f3409013e39f981cf04c4367f3fcfa67a9df50498c14920a75ca |
| kit-wallstates-3eca23c.json | 734ba423b08b02c3ed254bc06679e9243ccb2f48dbf8b78e79772ac71c93d8cb |
| trap-certificate-31-495.py | a9f5278b599d33e6db78dda10a0ad00f173dee01d912c56701b4f4ff4eb88ec6 |
| trap-certificate-31-495.out.json | 49fd4581fdc7b80fa487c447861f357d2df3d84f15d8dba9b807f9f4c507f420 |

The exact run source is revision2 SHA
`8729daf6d67bcf138e662805cd385fbc2f4b710adfea3c7ede12b38569588688`
at `bf9cdbbfbdae600027ae61a1c16f05ad11491223`. The postrun edit changes only
the module docstring (AST comparison excluding that string passes). The old
kernel input remains `16c70bf3832a2aca776f02405020ec964610a2db02df100bab9a2ae3e2f3488e`.
The retained supplemental trap calculation is separate from the accepted stage;
its receipt does not retrospectively cover that calculation.

The production schema gate passes on the actual result. Independently of its
partition helper, all570,846 pairs among the1,069 distinct main/control lanes
have identical low1,600-bit equivalence and old kernel-label equivalence.
All990 main rows,82 group reports, class partitions, first differences,
control/main overlaps and40 move-pair equalities agree with the stored words.
The33 reported gate fixtures and two base controls pass; each of the two
mutants actually fails the integer/lane-engine comparison. These physical
control outcomes were read, not rerun.

Exactly one old group splits: the20-member group with least4182 separates
37430 from its other19 members. Its first difference from4182 is visible
index1677 (zero based), physical odd time3355, hence first differing Psi
depth3356. The81 wholly unsplit groups contain970 rows. This is finite
persistence through20,000 visible bits, not proof that all81 groups remain
equal forever. L919's sentence “L913's plateau was not a horizon effect” is
stronger than the measurement; the infinite result below concerns one pair.
Unexpected retained-data check: the whole20,000-bit words of31 and495 are
exactly0101… starting with0, not merely equal to each other.

The M5 stage completed in52.6s; supervised child50.76s, time-l real49.92s,
CPU49.87s. Main-row computation43.61s and assembly47.12s are components,
not stage costs. Sampled group RSS137,297,920 bytes and process maximum
139,657,216 bytes are distinct measurements, neither a system-memory peak.
Pressure remained level1, free81%, swap0; final group members0, final problems
empty, exit0, artifacts5,391,715 bytes. The600s/4GiB/50MiB/10MiB agreement
and inherited stops were respected. GC1826's one-stage permission is consumed.

Read-only audit source SHA
`cba46fc2edfaa65f1f9b5ea4ccb990cf0dc52b61e26f142c441b71b41fb7f240`,
result SHA `f1beb5da1317b6369279f3621bb609d9cb1fd35ceae10e82a92f6e51a2e90835`.
Both are retained locally; their shared-store upload awaits direct approval
after an automatic approval-review egress rejection. No shared-store pointer
is claimed for these two audit files.

## 2. The carrying proof, with the finite witnesses made explicit

Kit revision `3eca23c0a9fa6b153313655e6d51835406c2d06e`:
[Rule30Ether](https://github.com/WolframInstitute/Rule30PrizeKit/blob/3eca23c0a9fa6b153313655e6d51835406c2d06e/lean/Ruliology/CellularAutomata/Rule30Ether.lean)
SHA `dc3d84cd13e0f091c400d60a0594e45dba59d9bc86aa224a328b2af66f06d756`;
[Rule30PeriodTwoSideways](https://github.com/WolframInstitute/Rule30PrizeKit/blob/3eca23c0a9fa6b153313655e6d51835406c2d06e/lean/Ruliology/CellularAutomata/Rule30PeriodTwoSideways.lean)
SHA `d08b1d0d0ea35051855323fbf1e8a88f01ab39a89ad0361b76f161437c206b54`.
Carrying read: ether definitions, all109 wall states, wallOK/wall_facts,
IsR30/rowOf, entire trap_invariant proof, drv definitions, u/Psi,
CQ01_iff_Psi, not_finSupp_Psi_of_eventuallyPeriodic and drv_shift.
The retained wall-state JSON equals the source list exactly, entry for entry.

Let A={1,2,3,4,5} and B={1,2,3,4,6,7,8,9}. Column0 is prescribed black
at even times and white at odd times. The following complete black supports
on positive cells are derived by hand using
x_p(t+1)=x_(p-1)(t) XOR (x_p(t) OR x_(p+1)(t)):

| t | Black positive cells starting from A |
|---:|---|
|0|1,2,3,4,5|
|1|6|
|2|5,6,7|
|3|1,4,5,8|
|4|1,2,3,4,6,7,8,9|
|5|6,10|
|6|5,6,7,9,10,11|
|7|1,4,5,9,12|
|8|1,2,3,4,6,8,9,10,11,12,13|
|9|6,8,14|

Each transition includes the cell immediately beyond the preceding support;
further cells stay white by locality. At t4 the row is exactly B, and the
wall has the same phase as at0. Determinism (kit drv_shift) therefore gives
F_B(t,p)=F_A(t+4,p). This replaces a second finite trajectory and explains
why the two trap-entry witnesses coincide.

At t9, choose j0=3, k=6, s=3. Column0 equals ether(3,t+3) for every t;
(j0+k) mod7=2. Columns1..6 are000001, exactly ether columns4,5,6,0,1,2
at phase0. Columns7..19 are
`0100000100000`, the listed phase0 wall state whose black positions are2,8.
All hypotheses of trap_invariant are met. Hence for every t>=9,
F_A(t,1)=ether(4,t+3). The same entry applies to B at t5.

The theorem's closure really permits either right input at column20; it
assumes no periodic or finite continuation beyond the wall. At the last
ether column, a black centre masks that input; when white, wall_facts supplies
the required next ether cell. The wall state then updates using the actual
right input. This closes the right-interface gap left by GC1826's failed
three-cell guard; there is no circular assumption of a permanent block.

Since ether column4 is0011, at t=2q+1>=9 it gives q mod2. The table gives
column1 at t1,3,5,7 as0,1,0,1. Thus **u A(q)=q mod2 for all q>=0**.
The four-step restart implies u B(q)=u A(q+2)=q mod2. Therefore u A=u B,
and the definition Psi=Theta(complement u) gives **Psi A=Psi B**.

They are not move-equivalent: widths5 and9 would require B=S^4 A in their
path component, but the chain is31,47,111,175,431 and495 is different.
This argument also excludes a detour beyond width9, since each row has at
most one predecessor. The already independently carried GC1825 corollary
excludes delayed move equivalence too, though that stronger statement is
not needed to refute the kernel conjecture.

Finally u A is periodic with period2 from0 (and so is u B). Apply the kit's
not_finSupp_Psi_of_eventuallyPeriodic. It gives not FinSupp(Psi A) and
not FinSupp(Psi B), i.e. these two CQ01 instances. The proof is an acyclic
composition of a literal finite table, the existing trap invariant, the
u/Psi definitions and the existing absorption theorem. **L919 is carried.**
This is a hand composition using kit theorems; no new Lean module has been
checked and the general CQ01 question, including the empty row, remains open.
Novelty of the particular application is unassessed; the trap/absorption
machinery is prior art. The supplemental empty/{1} non-entry control has no
retained output here and remains Local-reported, not part of this proof.

## 3. Answer to the next-job question

Formalize this exact two-row composition first; it needs no trap census as a
prerequisite. Reuse trap_invariant and the restart identity, decide the small
entry/table facts, and state both the infinite equality and non-move-equivalence
explicitly. Exact source/headlines and capped checking plan are still required
for any new Local launch.

A later census of the990 representatives is a sensible finite classification
question, but all65,536 rows is a separate enlargement, not automatic permission.
Retain each entry's actual phase, prefix and13-cell wall witness, together with
the finite visible prefix needed for pair equality. Non-entry by a deadline is
censored, not disproof of eventual absorption or CQ01. A broad census is not
needed to confirm the pair now proved. No new stage is accepted by this review.


## 4. Source comparison and an explicit common Psi (GC1830, 2026-10-24)

**Verdict:** the existing ether reconstruction gives an explicit common left row
for the already-carried pair: `Psi R31 = Psi R495 = etherLeft 3`. At depth zero
it is white; at positive depths it repeats `1011111`. This is a hand application
of existing kit results, not a new compiled theorem or a novelty claim.

Pinned kit: `3eca23c0a9fa6b153313655e6d51835406c2d06e`.
Read the complete `Rule30PeriodTwoCoupled.lean` (SHA256
`caa2f8ba78d0a48dc8c7db6f8adf65375b1d1442b85021eb5a676c1e185f3d22`),
including `etherLeft_zbl`, `ether_check` and the phase-1 `etherLeft_eq_Theta`.
Re-read Ether's literal table and Sideways's `u`, `Psi`, `Psi_unique` and
absorption interface at the hashes in section 1. The carrying calculation is:

1. Put `L = etherLeft 3`. Its definition is `L 0 = false` and
   `L k = ether (3 + 6*k) 3` for positive k. The kit proves, for all t and k,
   `zrow L t k = etherLeft (3+t) k`.
2. At depth 1 this is ether column 2. At even t = 2q the phase is 3 or 1,
   where that column is black. Thus L satisfies `InX`.
3. At odd t = 2q+1 the phase is 0 when q is even, and 2 when q is odd.
   Column 2 there is respectively 1 and 0, exactly the complement of
   `u R31(q) = u R495(q) = (q mod 2 == 1)` from section 2.
4. Apply `Psi_unique` to each right row. It yields `zrow L 0 = Psi R`;
   because L has zero boundary, `zrow L 0 = L`, including depth zero.
5. For k = 1,...,7, the spatial indices `(3+6*k) mod 7` are
   `2,1,0,6,5,4,3`. The phase-3 table gives `1,0,1,1,1,1,1`.
   Periodicity modulo 7 carries this to every positive depth. In particular,
   L is black at every positive k except k congruent to 2 modulo 7. Its
   infinite support is explicit, independently of the absorption corollary.

**Phase kill test:** the source's named `etherLeft_eq_Theta` uses phase 1,
whose free bits are 0,1,... . Substituting it unchanged would be wrong here:
the pair's required free bit at q=0 is 1. Phase 3 passes this check. No evolution,
benchmark or Lean build was run; these are modular arithmetic and source reads.

The relevant pinned catalogue entries were also read, together with the
README and catalogue contribution paragraphs. Root README SHA256
`ac84aedc716292a177be8d3a49d55b5e2f0972c6e284ee38944b3e6ee48ff48f`;
lean/README SHA256
`162ce62c4dfe0c70e8d17151f9b68a116facf4b627e41aec227e7d3f53f03be7`.
The selected entries and a literal pair-name scan do not identify this pair;
this is a limited NOT FOUND, not a literature-wide novelty determination.
ControlledResponse concerns equality for **every boundary driver**. Its
normal-form completeness is not claimed; TerminalClock also leaves rewrite
completeness open. Our fixed alternating-driver Psi counterexample must not
be advertised as refuting those stronger all-driver completeness questions.
The catalogue takes infinite-family contributions; single words/widths stay
on the submissions site. That distinction does not prohibit the proposed
pair submission. Reuse the kit's trap and reconstruction, and describe exactly
what the additional formal source proves. L921 source/check-plan review stays
pending until the source arrives; no new checking stage is accepted here.

**Audit export completed with direct owner approval:** the two GC1828 file-audit
artifacts are now retained at `cited/gpt-l919-review-20261024/audit.py`
(4175 bytes, SHA256 `cba46fc2edfaa65f1f9b5ea4ccb990cf0dc52b61e26f142c441b71b41fb7f240`)
and `cited/gpt-l919-review-20261024/audit.json`
(2211 bytes, SHA256 `f1beb5da1317b6369279f3621bb609d9cb1fd35ceae10e82a92f6e51a2e90835`).
Both upload receipts and exact readbacks were verified. The earlier pending-export
status is resolved; the historical approval rejection remains recorded.

## 5. Finite prefixes already give infinite families (GC1836, 2026-10-24)

**Hand corollary of the reviewed entry certificates, radius-one locality and the
kit trap invariant; uncompiled.** Define C31 by agreement with R31 on cells1..28,
and C495 by agreement with R495 on cells1..24. For every R in either class,
including an arbitrary infinite later tail,

`u R(q) = (q mod 2 == 1)` for every q, and `Psi R = etherLeft 3`.

In particular every finitely supported member is another CQ01 instance. The
fixed initial prefixes are `11111` followed by23 zeros, or `111101111` followed
by15 zeros, respectively. Tail cells29 onward in the first family and25 onward
in the second are completely arbitrary. This is a standard locality/trap
application, not novelty established or a new kernel-checked headline. It need
not delay the frozen pair submission or trigger another compute job.

Here is the full carrying argument. With a common driver c, if two initial right
halves agree on1..M, then at time t their driven states agree at every positive p
with p+t<=M; they also agree at p=0. Prove this simultaneously by induction on t.
At t=0 positive positions use the initial agreement and p=0 uses c0. At t+1,
p=0 uses the common boundary. For p>=1 the three predecessor positions are
p-1,p,p+1. A zero predecessor uses the common boundary; every positive one has
q+t<=p+1+t<=M, so the induction hypothesis applies to all three Rule30 inputs.
This uses the exact drv recurrence read in Rule30Ether, not an empirical cone.

For C31 take M=28,t1=9. Every cell1..19 at entry agrees with R31 since19+9=28.
Thus the same six-cell ether prefix and the same13-cell wall witness meet all
hypotheses of trap_invariant at j0=3,s=3,k=6,t1=9. The driver is independent of R.
After entry the theorem permits each actual outside input to the wall; no future
agreement with R31 is assumed. Hence column1=ether4(t+3) for all t>=9. Before
entry, the needed odd times1,3,5,7 also lie in the agreement cone at p=1.
They give0,1,0,1. The existing parity argument gives the displayed u at every q.

For C495 use M=24,t1=5:19+5=24, the same entry row/wall holds, and the early odd
times1,3 supply0,1. The same argument yields the identical u. The Psi definition
and section4's phase-3 reconstruction supply the exact common infinite left row.
Finite support of R is used only to interpret these as instances of CQ01; it is
not needed for the trace/left-row identity.

Boundary checks: initial cell28 (respectively24) is included; a tail is first
free at29 (respectively25). Moving the boundary one cell earlier would lose this
simple cone proof at (p,t)=(19,9)/(19,5), so these bounds are sufficient, not
claimed optimal. Initial column0 is irrelevant because the common driver
replaces it. No assertion that9/5 are the earliest possible entries is required.

These classes are disjoint at cell5. Among right halves supported in1..B for
B>=28 they supply exactly2^(B-28)+2^(B-24)=17*2^(B-28) distinct starts, all with
the same Psi. This is a count of these specified classes, not all members of the
Psi fibre. In the existing B=16 census these families add no extra rows beyond
R31 and R495: the free tail starts outside that domain. They therefore do not
classify the other970 finite persistent-group rows. The infinite family is a
useful structural consequence of the pair certificate, with no general CQ01 or
all-driver completeness implication.
