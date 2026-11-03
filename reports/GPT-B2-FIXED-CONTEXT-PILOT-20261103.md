# B2 fixed-context pilot freeze — GC2521

GPT, Intel host, 3 November2026. **FROZEN, NOT RUN at this checkpoint.**
The mathematical weighted/history formulas are now PROVED hand/two-party
by Local L1418; its entire carrying argument,121-line check and all output
were read. Its2000 random algebra/1200 history cases are Local computations,
not an Intel replay or the retained-leaf experiment below. No duplicate
random census is proposed. This pilot tests an implementation against an
independent physical-row oracle on the already selected retained context.

## Fixed source, input and predictions

Source: tests/probes/wolfram/b2_history_fixed.py, SHA256
`b9999a86a33af34cc5f42356c862e2fe150f7fd034644b453af20d58bd304e6b`.
No CLI parameters, network, subprocess creation, imports of old probe code,
seed search, adjustable horizon or new random input. The script enforces
internal CPU5s/wall15s stops. Only these two cases execute:

| case | seed | target j | terminal r/P | changed seed bits | last observed tick |
|---|---|---:|---|---|---:|
| Existing hand control |0x889da3|5|3/2|1,2|8|
| Chosen retained test |0x889da3|14|12/64|10,11|256|

Both are actual word100 leaves in the first block of edge_shift_tree64.out.
No other leaf is selected during the stage. The target's OLD forcing
period is2P, and the oracle includes2*(2P) to decide the target's doubling
only when the entire earlier history is preserved. For rejected histories
the target is explicitly NOT interpreted on an obsolete baseline period.

Prediction P1 (must hold): all15636 physical cells match the independently
integrated three-coefficient response; all1024 exhaustive pointwise OR
controls pass; weighted-response/local00/first-failed-history-guard
predictions match. The j5 control reproduces onlyidentity in full H and
the local-only11 intervention losing d4. A mismatch stops the stage and
retains its failure; no repair/rerun is authorized by this freeze.

Discriminating prediction P2: the selected j14 context admits at least one
nonidentity intervention preserving the entire history AND changing its
target doubling flag. This is a proposed finite actual-history freedom,
not a prediction of a fair distribution. Counterfactual: H is trivial, or
all its choices keep the same functional. P2 is then REFUTED; keep the
actual H/coefficient result and change the intervention rather than extend
the seed/horizon sample. P1 passing does not rescue P2.

Independent oracle: evolve complete finite physical rows using the literal
eight-entry Rule30 truth table. Initial cells at positions-i are the seed
bits; two white halo cells surround the entire seed cone through the last
tick. Read R_i(t) at physical x=t-i. The primary implementation instead
uses the integer Phi update and the seven mixed terms of the response
recurrence. Compare all four interventions at every fixed tick/depth.
Prefix return at the old period and nonreturn at its half identify exact
old least periods using the known dyadic prefix property. No individual
diagonal nonloss is assumed.

Negative controls: delete the z_a*z_b mixed product from the pointwise
response; exhaustive controls must detect a mismatch. Delete the mixed
mask-parity term in the j5 control; choice11 must then be wrong. Unexpected
check: record the FIRST changed depth, not just a pooled full-history
boolean; a baseline-period coefficient after the first failure is not
labelled a valid new growth flag.

Record searched: complete GC2519 body, GC2014/2210/2211 and GC2405; actual
current kit c42f6e51 TFunctionCycles.Phi_bit/lift_iff/per and exact source
comparison; portal/open35PR index COMPLETE11:50:45Z. Primary Boolean
coordinate background re-read in GC2519. Local L1418's new exact check was
read in full before this freeze. Those checks do not test j14's selected
retained functional against literal physical evolution.

## Stage limits and host gate

One stage, one research child/thread, nice10. Default pilot ceiling remains
120 aggregate CPU seconds/300wall/768MiB; this stage is narrower:
child RLIMIT_CPU10s; internal computing CPU5s/wall15s; supervisor wall30s;
summed owned RSS256MiB; output16MiB/file and128MiB/stage; max3 owned
processes; --track-tree. Launch free+inactive4096MiB, running3072MiB,
swap-growth64MiB. No concurrent owned research job, GPU or compiler.
Any pressure/monitor/process/thermal failure stops this job, retains evidence
and redirects to hand reasoning. No automatic retry or relaxed limit.

Preflight12:21Z: load3.41/3.41/3.27; free+inactive approximately5199MiB,
swap used1799MiB. Browser/display activity is substantial but this pilot
is a small single-thread fixed check. The runner remeasures the gates at
launch. Sandboxed swap measurement failed before launch; the approved
unsandboxed query succeeded. No monitor failure was treated as zero.
No reliable thermal sensor is available, so no thermal-telemetry claim.

Use run_capped.py with tree tracking. Retain an OUTER /usr/bin/time -l
receipt for the runner and descendants, plus its internal child receipt
and launcher JSON. The CPU limit is per process, not an enforced aggregate
tree CPU cap; this program starts no children, and actual whole-stage CPU
must be reported from the outer receipt against the120s ceiling. Supervisor
and monitoring costs are not omitted. Sampling may finish too late for this
short probe; missing ongoing samples are unavailable, not measured zero.
Check cleanup and all file sizes before claiming normal completion.

Invocation from the repository root (fresh output directory only):

```
/usr/bin/time -l python3 tests/probes/wolfram/run_capped.py \
  --out /private/tmp/gc2521-b2-fixed --cpu 10 --wall 30 --rss-mib 256 \
  --file-mib 16 --disk-mib 128 --launch-free-mib 4096 --min-free-mib 3072 \
  --swap-growth-mib 64 --track-tree --max-procs 3 \
  -- nice -n 10 python3 tests/probes/wolfram/b2_history_fixed.py
```

The outer timing receipt is retained separately outside git. Results JSON
contains every oracle prefix at every fixed tick, all history coefficients,
actual admissible choices and source hash. Data are published by digest in
the shared store after checks; no raw output is added to git.

My own pull: whether fixing the real history removes the apparent free
input, or leaves a genuine controlled change of the next decision.

## Outcome — GC2522, run at published freeze c20bbcf4

**COMPUTED: P1 HELD; P2 REFUTED.** Exactly one stage ran12:30:38–39Z.
All15636 physical-row cell comparisons and1024 pointwise algebra controls
passed. Deleting the z_a*z_b mixed product failed64 pointwise controls;
deleting the mixed mask term failed the designated small control. All
weighted values, local00 conditions and FIRST failed history guards agreed
with the independent literal-row oracle. No source repair or rerun.

| fixed case | local00 choices | full-history choices H | target on H | weighted(S,A,B) |
|---|---|---|---|---|
|j5 control|00,11|00|1|(1,1,0)|
|j14 test|00,01,10,11|00,11|1,1|(0,0,0)|

At j14 all history-response triples below depth13 are zero; depth13 and
the baseline-period depth14 triple are(1,1,0). Choices01/10 first fail
at depth13, so the baseline-period depth14 expression is NOT called their
new growth flag. The weighted functional itself is1 for ALL four choices.
Thus the prediction of a nonidentity history-preserving choice that changes
the target is false, even though H has a nonidentity member. This is
history-conditioned rigidity in one selected leaf, not a frequency estimate.

### Resource and retention receipt

Runner COMPLETED rc0; normal completion passed the source's final no-live-
owned-process check, no cleanup signal needed. Launch free+inactive6583MiB,
swap1767MiB. Computing process reports0.095CPU/0.097wall internally; child
time0.20wall/0.16user/0.03sys, reported maxRSS16404480bytes. OUTER whole-stage
time0.74wall/0.31user/0.13sys: **0.44 aggregate measured CPU seconds**,
reported maxRSS18120704bytes. The outer maxRSS is a reported process peak,
not a measured simultaneous sum over the process tree. Supervisor self
CPU0.156s is included in the outer accounting, not added again.

The job finished before the first monitor sample: running RSS/process/
pressure maxima are unavailable, not measured0. Launch pressure gates and
child limits did apply. No ongoing thermal measurement is claimed. No
pressure/monitor failure, enlargement or second job occurred. The runner's
25915-byte final artifact count precedes its own launcher write; including
launcher and outer receipt gives27559bytes before the immutable packet.

Retained raw source/results/every oracle prefix/stdout/launcher/inner and
outer timing in `cited/gpt/gc2522-fixed-history-packet.json`,40777bytes,
SHA256 `182f79494ccbb1cb7bd66e92bf875a3a6d7190424ceca76db462bd5934fa7a0b`.
Raw results JSON SHA256
`9b48d4b92e4ce8999453c9707bdd842897e5ef73d8be4c99dbdc16092103b278`;
stdout `7e73aceb25a8007ec10184abe3a0e05a30e67dd8f01c5c898308cf1edbc1f0a1`.
The packet is outside git; no raw trajectory output is committed.

## A different representation: two whole seed congruence classes

**New family extension: solo PROOF-SKETCH pending carrying read.** The
generic response/lifting identities used are already carried L1418; the
finite coefficients above are independently checked by the fixed pilot.
This extension requires no new trajectories or extra intervention tests.

In the physical edge convention R_i=bit_i(Phi^t(a)), let a be ANY nonnegative
integer with

`a = 419 or3491 modulo4096`.

Then the proposed whole-prefix periods L0,...,L14 are exactly

`1,2,2,2,4,8,8,16,32,32,64,64,64,128,256`.

In particular d11=d12=0 and d13=d14=1. The known no-three rule additionally
gives d15=0. These are arbitrary finite seeds in two explicit residue
classes, not a statement about the one-black seed or its density.

### Proof, including every higher starting bit

Both classes have low10 bits419=0x1a3; bits10 and11 are equal. The retained
baseline has those two bits both1. Use beta,gamma for their changes, so
the class condition is beta=gamma. Let zeta independently change seed
bit12. Bits13 and higher are arbitrary.

1. The prefix through R9 is fixed. Changing R10's starting bit complements
   its entire stream and cannot change its prefix period. All prefix
   periods through R10 therefore have the retained values.
2. At r12/P64 the retained local coefficients alpha=A=B=0 prove that
   BOTH following0flags survive every beta,gamma. Complementing R12
   by zeta does not change its own prefix period either. Hence L11=L12=64
   for all these choices, independently of bits12 and higher.
3. The retained W=R11 has32 black entries over64 ticks. The response
   h has32 as well. Since W_new=W+gamma+beta*h, every new W has EVEN
   parity over64. The weighted coefficients(S,A_w,B_w)=(0,0,0) give
   F_10(R10_new OR R11_new;64)=1 for every beta,gamma.
4. For a64-periodic integral C=R12 of G=R10 OR R11, exchange the finite
   sums in C(t)=C(0)+SUM_(u<t)G(u). Its parity is F_10(G;64), since
   64*C(0)=0 and the coefficient63-u is odd exactly at even u. Thus
   R12 has ODD parity1 for every beta,gamma,zeta. This step retains
   the ordered integration identity; it is not a random-parity assertion.
5. At zeta=0, the exact depth13 forcing response is beta+gamma, so
   d13_new=1+beta+gamma. Changing zeta complements R12 and changes that
   forcing parity by parity(NOT R11_new)=0. Seed bit13 cannot change
   its own prefix period. Thus d13=1 exactly when beta=gamma, with
   L13=128 in those classes. For unequal bits L13=64; no claim about
   their next flag is made here.
6. In the equal-bit classes, R13 is antiperiodic at64 while R12 has
   period64 and odd parity. Pairing the next forcing over128 ticks
   yields parity_64(NOT R12)=1. Therefore d14=1 and L14=256,
   independently of the starting bits of R13 and R14. Higher seed
   bits never enter these lower profiles. The OR no-three theorem
   at prefix period64 then gives d15=0.

The finite parent words used (least-significant bit=time0) are retained
by the physical oracle, not regenerated for this proof:

| word over64ticks | hexadecimal | black count |
|---|---|---:|
|R9|5d0aab565d0aab56|32|
|R10|95f3355a6a0ccaa5|32|
|R11|6952d59455f4b2a5|32|
|R12|56a2a69455575339|31|

The supplied h has32 black entries. These explicit words make the finite
coefficient checks replayable separately from the infinite-family inference.
No new example a419/3491 was numerically run after the freeze.

Record searched again for889da3/0x1a3/0xda3/3491 across record and current
kit/portal/open-PR sources. Matches are this retained seed/control or
unrelated numerical gate-past certificates, not an adopted theorem of these
classes. This is an application of known recurrence/lifting/response
machinery, not a novelty or submission claim.

### Route disposition

Recent phase changes do not control this target: even permitting ALL higher
starting bits leaves the displayed family law. Park further phase toggling
for this fixed parent cylinder. Reopen it only with a changed older parent
prefix or a genuinely different mask certificate; do not enlarge the seed
or horizon sample. The next independent warm task is NIGHT-TASKS C4's exact
core-parity implication, while this new cylinder proof awaits a carrying
read. The failed P2 prediction led to a family statement rather than a
second search for a favorable leaf.
