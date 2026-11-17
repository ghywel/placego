# Six initial literals, one black target — GC2609

GPT, 3 November 2026. The physical implication is **PROVED hand/two-party**
by GC2607/L1491: initial 111011 on [x,x+5] forces X(4,x+4)=1, with
arbitrary exterior. This report gives an explicit 18-addition positive-RUP
candidate for that implication. **GC2613: the finite implication now has a
verified cake_lpr certificate**, following the partial GC2611 outcome and
separately frozen GC2612 positive call. The original freeze follows. No shortest antecedent or novel word mechanism is claimed.

## Gate support and the guarded clause

Write v(t,j)=X(t,x+j). The clause is

    NOT v(0,0) OR NOT v(0,1) OR NOT v(0,2) OR v(0,3)
      OR NOT v(0,4) OR NOT v(0,5) OR v(4,4).

Let H denote its first six literals. They are the negated initial-word
conditions, not extra unit clauses borrowed from a particular root.
Number variables in this order:

| Coordinates | Variable IDs |
|---|---|
| (0,0)..(0,6) | 1..7 |
| (1,1)..(1,7) | 8..14 |
| (2,2)..(2,6) | 15..19 |
| (3,3)..(3,5) | 20..22 |
| (4,4) | 23 |

Thus H=(-1,-2,-3,4,-5,-6), and the target is H+(23).
Each gate with key (t,j) has parents v(t,j-1),v(t,j),v(t,j+1) and output
v(t+1,j). Its eight truth-table clauses are ordered by 4a+2b+c; the
output table is (0,1,1,1,1,0,0,0). The following 14 gates supply 112 clauses:

| Gate keys | First clause IDs, in the same order |
|---|---|
| (0,1)..(0,5) | 1,9,17,25,33 |
| (1,2)..(1,6) | 41,49,57,65,73 |
| (2,3)..(2,5) | 81,89,97 |
| (3,4) | 105 |

Some unused intermediate/exterior cells are free: in particular v(1,6)
and v(1,7) have no defining first-row gates in this support. This only
weakens the premises. No root, path, boundary or observer assumption is
part of these 112 clauses.

## Explicit hand RUP sequence

The first six rows are the existing a10 template with
(A,B,C,U,V,P,Q,R,Z)=(10,11,12,13,14,17,18,19,22). Subsequent rows retain
H while deriving the forcing tableau. A row means: assume its clause
false, then unit-propagate the listed positive clause IDs to a conflict.

| ID | Clause | Hints |
|---:|---|---|
|113|17,-18,22|99,100|
|114|17,-19,22|98,100|
|115|-17,-18,-22|103,104|
|116|-17,-19,-22|102,104|
|117|-10,-11,12,22|63,113,114,69,75,76|
|118|10,-11,12,-22|59,115,116,69,75,76|
|119|H,-8|8|
|120|H,-9|15|
|121|H,-10|22|
|122|H,11|28|
|123|H,-12|39,40|
|124|H,-15|119,120,121,41|
|125|H,16|120,121,122,50|
|126|H,17|121,122,123,59|
|127|H,20|124,125,126,84|
|128|H,-21|125,126,95,96|
|129|H,-22|121,122,123,118|
|130|H,23|127,128,129,109|

The two-row mask at 123 proves rule(1,1,unknown)=0; the same mask is
used at 128. Row 129 is the white a10 consequence of time1's 010. The
last gate is rule(1,0,0)=1. This explains the otherwise nonlocal use of
the discarded outside forecast; it does not establish a complete observer.

## Composition with a host CNF

A later exporter must injectively map all 23 variables to the intended
physical cells, byte-match every one of the 112 gate clauses, assign
fresh addition IDs, and rewrite every hint. Root and path units remain
forbidden throughout the prefix. Only a separate final contradiction
may use the host's initial conditions and an opposite target literal.
An augmented-CNF UNSAT receipt alone does not certify the original CNF.

The saved original time3000 root has 111010 at positions11..16, not
111011. This new clause therefore gives no direct exclusion of that
root. The separately completed 25-root-literal/tick19 proof remains its
own package; this work neither replaces nor reruns it.

## One frozen certificate check

Source: [a4_six_guard_certificate.py](../tests/probes/wolfram/a4_six_guard_certificate.py).
The plan pins the source, a10 helper, existing aggregate monitor and
verified checker. GPT owns this single fixed job; no solver, random
paths, graph, closure build, host-CNF embedding or larger horizon.

Prediction: all 18 additions pass a gate-only RUP replay; cake_lpr
accepts gates plus the negated seven-literal conclusion using that
prefix and one final empty clause. Counterfactual: any invalid hint,
literal, gate table or checker rejection refutes this encoding; preserve
the failure and do not retry/enlarge automatically.

Controls: compare each four-variable gate against the independent scalar
rule; replay all eight exterior completions of the fixed six-cell word;
check a unit-conflict positive control and reject a proof with the final
forcing-gate hint removed. Unexpected check: scan only the fixed nine-cell
cone's 512 initial assignments for a countermodel when the sixth root
guard is removed. This is a finite encoding/guard check, not a census of
fronts or a minimality claim. No symbolic algebra substitute is used.

Record searched: GC2581's a10 proof and GC2589--2591's guarded-prefix
composition; GC2606--2607/L1491; the current record, kit and portal search
for 111011 and discarded forecasts; COMPLETE external refresh20:40:46Z,
kit c42f6e5133f61a47e99289fd4b6e0536fd8a0453. This is a translation of
the just-carried result using known machinery, not a novelty decision.

Stage caps: 30 aggregate CPU seconds,60 wall,768MiB sampled tree RSS,
16MiB/file,128MiB/stage, one serial worker/nice10,max6 processes.
run_capped tracks the tree with launch4096MiB/running3072MiB free+inactive,
swap-growth64MiB and thermal/monitor failure stops. The inner helper
tracks worker self+reaped+live checker CPU at10s; the stage driver tracks
its self+reaped+live worker at20s, reserving10s for outer supervision.
Final accounting counts driver+outer once, not nested subtotals twice.
Worker hard CPU3s and each checker2s are backstops, not aggregate gates;
each checker wall5s, worker wall25s. Freeze/source hashes precede launch.

Next after a successful check: retain a reusable checked clause and its
host-embedding obligations. No automatic original-CNF insertion. The
actual final phase packet has priority once supplied; Local owns its
assembly/builds and Cloud its packaging/owner exchange.


## Partial outcome and the checker-status contract — GC2611

Freeze2cff54b3 ran once at20:54:37Z. All18 gate-only RUP additions,
224 scalar gate rows,8 fixed-word exteriors and512 nine-bit initial rows
passed, including a countermodel to omission of the sixth guard. These
are self-checks of the instance, not yet the intended verified-checker
receipt. The unit-conflict control returned VERIFIED UNSAT. The corrupted
final-hint proof was rejected with "Checking failed at line:17" (zero-based
line18 of the prefix); it emitted no VERIFIED UNSAT marker but exited0.
Our added assertion wrongly demanded a nonzero rejection exit status,
and stopped the stage before the good certificate call. The existing
a10 and guarded-root helpers correctly use the marker for rejection and
require rc0 only for acceptance. This is a harness-contract failure,
not an accepted corrupted proof or a counterexample to the implication.

[Partial receipt](receipts/gc2611-six-guard-partial.json) pins every output.
Evidence `cited/gpt/gc2611-six-guard-partial.tar.gz`,3610bytes,SHA256
 d09365e3269bc8c5b314d00e09b434d1840ec2ee14d4cc237e0dac82a579276b;
raw-body transfer and manifest readback verified. Driver aggregate0.26103
plus outer0.076 gives0.33703CPU seconds; wall0.54s,maxRSS20,488,192bytes.
Launch free+inactive5771MiB,swap1160.75MiB,thermal100/100. No tree sample
before completion; sampled zero is not zero usage. Original source and
failed receipt are preserved, with no automatic rerun.

## Separately frozen remaining positive call — GC2612

The new evidence justifying this narrow continuation is the checker's
actual rejection text and the already-established helper contract.
Only the previously uncalled good certificate is needed. Do not regenerate
anything or rerun the completed controls. Check the immutable retained
CNF b3e6d4b9cd6767d5556856f61eff5e8ac5981b82c33aeb46d3756fe684c9441e
and LRAT ecee5483d6a52affdd2a7cf0c87a97290f23a4f66309d81576d0a34df10d086e.
Prediction: normal exit0 AND literal VERIFIED UNSAT. Counterfactual:
any other outcome is failure of this remaining validation and stops it.

[a4_six_guard_finish.py](../tests/probes/wolfram/a4_six_guard_finish.py),
SHA2569e506d9a3a72106d051c5747d4d99e7fbdafdd3382b3af59a7c29d0b741f435b,
validates both file hashes and the checker, then execs the checker in the
same process. [Plan](../tests/probes/wolfram/a4_six_guard_finish_plan.json)
SHA2565f3a5d7e1d091474fd8e581c7a365f008af68fc631fd2bf3d7f11caa2326ac9c.
This makes the existing serial stage's live/reaped CPU accounting direct.

New total caps10 aggregateCPU/20wall/768MiB,one serial checker/nice10,
max6 processes,16MiB/file/128MiB stage. Stage stop5CPU plus5CPU supervisor
reserve, worker hard2CPU/5wall, outer hard3CPU. Same strict tree/headroom/
swap/thermal gates:4096 launch,3072 running,64swap. Preflight20:56 about
5702MiB free+inactive,swap1160.75MiB,thermal100/100,load1.86/2.08/2.10;
recheck at launch. This is a separately justified call on existing bytes,
not a larger experiment or entitlement to repeat a failed job. GPT owns
it; Local/Cloud phase work is unchanged. No original-host embedding.


## Certified finite implication — GC2613

The separately frozen positive call e2e7b319 completed at20:58:04Z,
normal exit0, stdout exactly `s VERIFIED UNSAT` and empty stderr.
The retained CNF/proof/checker pins matched; no bytes were regenerated
and neither completed control was repeated. Together with GC2611's
restricted replay of all18 additions, the certificate proves the stated
seven-literal implication from the112 gate clauses. The final query has
119 clauses:112 gates and seven negated-conclusion units. The18-step
prefix is followed by one empty-clause addition. Every prefix hint uses
only a gate or an earlier prefix addition, never the query units.

[Successful-call receipt](receipts/gc2613-six-guard-certified.json).
Evidence `cited/gpt/gc2613-six-guard-certified.tar.gz`,1730bytes,SHA256
bc160db88d69e7df0d146db68643333e73e80f3f968bb697895045286a6adb97;
raw-body transfer and manifest verified. Driver aggregate0.139736 plus
outer0.077 gives0.216736CPU seconds,wall0.55s,time maxRSS17,367,040bytes.
Launch free+inactive5674MiB,swap1160.75MiB,thermal100/100. No tree sample
before completion; no pressure stop, repeat or remaining job. Combined
reported driver+outer CPU across the two separately frozen stages is
0.553766s. The first harness failure remains part of the evidence.

The guard test also gives a hand-checkable reason to retain the sixth
initial literal: initial111010011 on[0,8] evolves on the shrinking cone
as 0001111,01100,101,0. It meets the first five antecedent bits but has
a white target. This particular tableau is a hand self-check here; the
frozen512-row test establishes existence independently. No minimality
claim for all six literals is made.

Status: verified finite Boolean implication; physical encoding interpreted
by the carried GC2607/L1491 proof and independent scalar gate checks.
No Lean build, portal Lean Verified/Human Verified label, original-host
CNF embedding, original-root applicability or universal-capture result.
The host composition obligations above remain mandatory.

Next executable step: read Local's actual A6 portal Lean, notebook and
receipts when supplied, checking the corrected upper-bound language and
literal provenance. While that assembly is owned by Local, the independent
light step is to specify how a caller maps this clause's23 physical cells
and112 gate IDs into a candidate host CNF, rejecting any unsupported
placement before emitting additions. No host search or new run is frozen.
