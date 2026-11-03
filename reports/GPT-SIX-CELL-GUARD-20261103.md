# Six initial literals, one black target — GC2609

GPT, 3 November 2026. The physical implication is **PROVED hand/two-party**
by GC2607/L1491: initial 111011 on [x,x+5] forces X(4,x+4)=1, with
arbitrary exterior. This report gives an explicit 18-addition positive-RUP
candidate for that implication. Its numeric encoding is **NOT YET CHECKED**
at this freeze. No shortest antecedent or novel word mechanism is claimed.

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
