# A fixed dyadic return closure and a one-tick phase constraint

Owner-authorized manual research block, GC2833. Both schedules remain PAUSED.
Cloud CL768's two carrying reads are adopted, with its full-path component
guard and exact tile-window convention. No other worker's task or build is taken.

## Why this test

The full period16 core and its old glider exits are not a new target:
genealogy29.11/T23 already follows G16's period32 off-cycle choices to closure
(18238 states, only rain exits), and T19 does G8. The period32 wave of480
states is also known, L1304/GC2362. Its old generator follows one surviving
continuation to a cycle; it does not identify that cycle's complete SCC.

The new fixed question is whether **that stored cycle**, at the same temporal
period32, has off-cycle paths returning to it and therefore belongs to a
branching SCC. A negative answer is only about its attached forward closure,
not every period32 component, every dyadic period or actual black-edge capture.
No period64 extension, generic sample or full2^64 census is proposed.

**Record searched:** CL768/report and full probe/output; GC2830; LN12 report
§5–§10; genealogy29.4/29.7/29.11/31.4/32; `phase480.py`, stored cycle,
`general_front.py`, its upward-history control, `glider16_defect.py`,
`glider_defect.py` and their existing outputs; G157/G158. The current actual kit
`lean/`, `equivalents/` and catalogues retain MovingWaves' period12 construction,
minimum12 and low-period bounds, with the prior exact PR232/source read.
Complete fresh known-find refresh2026-11-10T17:58:19.690200Z:
kit03a19bf6240b63c6d15894c5f7552f3a6091d937, portal17:58:15Z,38open PRs,
zero changed/added/removed. Two narrow literature queries returned the portal
and our record, not an additional primary-source match; no novelty priority
claim is made from that search.

## A one-tick identity before computing

Use the leftward pair convention (c,d)->(u,c), with
Delta u=c OR d, Delta u(t)=u(t+1) xor u(t). For even temporal P put L=P/2
and Hc=c xor shift_L(c). Hc is L-periodic. Replacing each profile z by its
independently chosen half-shift is z_e=z xor e*Hz, e in{0,1}.

Let A=Hc AND NOT d, B=Hd AND NOT c, C=Hc AND Hd, all as full P-bit words.
Then Hu has Delta Hu=A xor B xor C. The triple of choices(e_u,e_c,e_d)
is legal exactly when

    (e_u xor e_c)*A xor (e_u xor e_d)*B
        xor (e_u xor (e_c AND e_d))*C = 0.

More directly, applying H to the proposed equation cancels the child's choice:
H Delta(u_e)=H Delta u, whereas H(c_e OR d_e) differs from H(c OR d) by
(e_c xor e_d)*C. Therefore

    Hc AND Hd != 0  ==>  e_c=e_d.

This is a local **overlapping-half-defect guard** for the literal one-tick OR
law. It is a PROOF-SKETCH pending an independent carrying read. It restricts
only configurations assembled from half-shifts of a fixed background; it is
not a criterion for arbitrary profiles or a general no-branching theorem.
The tau^3 positive-entropy/dyadic-order countercontrol remains mandatory:
its six-neighbour local law has additional terms, so this two-neighbour OR
identity cannot silently be applied to that different rule.

## Frozen questions, controls and stops

Predictions, before running:

1. The stored480cycle's SCC at P32 is precisely its480-cycle, with no returning
   off-cycle branch (0.8). Its other cyclic destinations are the rain only (0.7).
   Counterfactual: a larger SCC or another branching destination. Retain actual
   closed walks and treat a dyadic branching certificate as a meaningful result,
   without calling it a prize proof.
2. Every adjacent profile pair of the480wave has nonzero half-defect overlap
   (0.7), so its independently half-shifted configurations have only a global
   binary phase. Counterfactual: a zero overlap or a persistent mixed-phase
   path; inspect its exact mask rather than increasing a graph horizon.
3. Positive control: from U=(1323,2868) at P12 recover the known30-state,
   32-edge branching component. Independently audit complete reachability,
   every temporal integral including wrap, and the entire SCC partition in C++.
   Mutating one stored temporal bit must be rejected.
4. Unexpected/chaos test: allow an independent half-period temporal shift of
   **each** spatial profile, preserving all its individual rotation/weight data.
   The small marked phase-constraint graph, not single-profile statistics,
   decides whether those choices glue. Compare the period12 stay loop too,
   removing duplicate spin encodings on profiles fixed by the half-shift.
5. Scope control: reconstruct one six-to-two wall in the tiny P6 graph and
   check it literally. This tests CL768's suggested phrase "period never falls",
   which is not part of its carried formulas. The general safe statement is
   that the child's least pair period divides twice the parent's; its odd part
   may be lost. Odd factors cannot be created by one integration step.

No additional source cycle is searched. Fixed source
`tests/probes/phase480_p32.txt` SHA256
`6f77ed2178c4fca0169fc0690b952b680276a787c06d44e8bba36e0eabb92bc3`.
Normalize each stored(u,v) to(c,d)=(v,u), so one leftward step is(u,c).
[Extractor and gauge test](../tests/probes/swarm/sw02/carry/gpt_dyadic_return.py),
[independent checker](../tests/probes/swarm/sw02/carry/gpt_dyadic_certificate.cpp),
[hashed serial plan](../tests/probes/swarm/sw02/carry/gpt_dyadic_plan.json).

One Intel stage: a hard200000-node cap,110 aggregate CPU-second stop within
120 ceiling,300wall seconds,768MiB tree RSS,max6processes,16MiB/file and128MiB
stage disk. One compute worker/nice10; no solver, Lean, GPU or Wolfram.
run_capped tree tracking,4096MiB launch/1024MiB running free-memory floors,
4096MiB swap-growth, thermal and monitor-failure stops active. Inputs/plan
published before launch. A cap or pressure failure preserves evidence and
redirects to hand work; no retry or automatic cap enlargement.

## Outcome

Pending the separately frozen stage. No predicted count is an executed result.
