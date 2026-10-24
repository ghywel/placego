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
