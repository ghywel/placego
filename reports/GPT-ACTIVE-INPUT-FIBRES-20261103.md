# Active inputs as successive constraints on initial bits — GC2594

GPT, Intel, 3 November2026. **PROVED hand/two-party after L1479, adopted GC2595.**
Local's complete carrying argument and75-line check source were read. The
reported M5 enumeration is separate, with no Intel replay. Its two-tick
reset loop has16 cases (four free bits), not the printed64; this count-label
error does not affect the hand proof. The original sketch follows.
Hand reasoning only; no solver, simulation, graph, compilation or sampling.
This continues the announced adjacent-ray work after GC2593's essay review.
Local owns the synthesis assembly and final packet; that read takes priority.

## Prior work and the change of representation

The ingredients are already known: the carried [active-input cylinder](GPT-SLOW-WALL-ACTIVE-INPUTS-20261103.md),
the [rightmost-bit derivative/reset rule](GPT-INPUT-HISTORY-GEOMETRY-20261103.md)
(now carried L1477), and the [signed observer's common-witness guard](GPT-A4-COUNTERWORD-PROOF-CHECK-20261103.md#reusing-due-colours-and-the-dropped-cell--gc2577-proof-sketch).
The point here is their exact application to successive active reads, not
a new generic reset theorem or an information-loss rate.

Record searched: two/ray, two/reset, coupled/reset, reset/synchronization,
and inverse cascade, with `record_find.py` and `known_find.py --offline`.
Multiple supplied terms were conjunctive: their zero hits are not a broad
negative search. Current index is the COMPLETE17:58:54.423124Z snapshot,
kitc42f6e5133f61a47e99289fd4b6e0536fd8a0453,119entries/38openPRs.

The positive primary-source match is [PR60, Rule30InverseCascade](https://github.com/WolframInstitute/Rule30PrizeKit/pull/60),
head db6e71128339d1fc45b5a7ab5f2bade997996ae3. Read its complete330-line
module, current discussion and empty review-summary list, and the exact
linked archive's README, REVIEW and UPDATE-REVIEW at3ebd1501497f168c04b3b0fab00595b1266f5a00.
`finite_cascade_closes` and `scheduled_cascade_closes` already provide
qualitative sequential-reset closing under explicit reference-driver
reset hypotheses. Their waits need not be bounded; recurrent resets on
the physical legal rows remain open. The transfer is the predecessor
scan T_b(v,w)=(b XOR(v OR w),v), not the two-driver map below. No transfer
of its hypothesis to our actual inputs is asserted. PR60 remains OPEN;
the discussion reports catalog/import-placement repairs. No local replay
or new verification of that PR is claimed. [Read pins](receipts/gc2594-active-input-fibres.json).

Two blocks have now exposed the same obstacle to erasing old bits by a
reset of the current finite band. Park that compression route: reopen
only with a future-equivalence proof for the permitted moving reads,
or a guard keeping those reads inside the merged band. Instead retain
constraints on initial bits, with their common physical witness.

## Two adjacent rays, retaining both initial bits

Fix the initial configuration strictly left of q. Leave z=X(0,q) and
w=X(0,q+1) free. At each time s put

    c_s = X(s,q-s-2),       u_s = X(s,q-s-1),
    v_s = X(s,q-s),         h_s = X(s,q+1-s).

c and u depend only on the fixed older prefix. The exact physical update is

    v_(s+1) = c_s XOR (u_s OR v_s),
    h_(s+1) = u_s XOR (v_s OR h_s).

Thus v starts at z and h at w. These equations share the SAME v_s; two
independent existential choices for it would not describe a physical row.
For reference, the complete one-step table on(v,h), by hand substitution:

| (c,u) |00|01|10|11|
|---|---|---|---|---|
|00|00|01|11|11|
|01|11|10|10|10|
|10|10|11|01|01|
|11|01|00|00|00|

For each fixed z, the second equation is again the one-bit reset law:

    h_s = B_s(z) XOR (w AND H_s(z)),
    H_0(z)=1,   H_(s+1)(z)=H_s(z) AND NOT v_s(z),

where B is the solution with w=0. Hence a requested pair of read histories
has an exact relation on(z,w): first retain the z choices compatible with
the v reads, then apply the0/1/2 test to h for EACH retained z separately.
The number of pairs is the sum of those conditional counts. This is a
four-assignment relation for a fixed older prefix, not a four-state
description of all older prefixes or a claim of independent observations.

There is a genuine two-tick reset: if(c_s,u_s)=(0,1), all four initial
pair states map at s+2 to(NOT c_(s+1), NOT u_(s+1)). Indeed v_(s+1)=1,
so both next updates are masked. Subsequent equality persists on these
two rays under the same older drivers.

## Even this pair reset does not justify forgetting the initial bits

Set initial cells q-4..q+2 to

    1,0,0,1,z,1,0.

At time1 the cells q-3..q+1 are

    1,1,1,0,NOT z;

at time2 the cells q-2..q are

    0,0,z.

The first two cells are exactly the q and q+1 rays, now independent of z.
The next step gives X(3,q-1)=z. The permitted motion sequence retreat,
stay,stay reads positions q,q-1,q-1,q-1, so its right ancestor labels are
q,q,q+1,q+2. The next stay leaves the merged pair and recovers z.
All displayed cones fit inside the seven initial cells. This is a literal
hand counterexample to future equivalence based only on a pair reset.
It is not asserted to be a particular prepared A4 root or active-input
path; those strip/motion predicates still require their own guards.

## Actual active reads have strictly increasing right endpoints

For the carried A4 strip convention, the physical incoming position is
p_t=A_path(t)+W+1. Its increment is0 on a stay and-1 on a retreat, so
q_t=t+p_t increments1 on a stay and0 on a retreat.

An input is active exactly when the anchor stays AND the last strip cell
is white. Thus an active read is followed immediately by an increase of q.
Since q never decreases, two active reads cannot have the same q. A
constant-q retreat run has at most one active read, at its closing stay.
The multiple-read form in GC2592 is valid for general observations, but
its direct use here is this one-read specialization. Ignored printed
labels remain wildcards, including those on intervening retreats/stays.

## Exact prefix-extension rule, including the masked case

Fix one finite candidate path of the base strip abstraction, with its
prepared root and all phases. List active reads(t_i,p_i,b_i), and write
q_i=t_i+p_i; these q_i strictly increase. Restrict attention to the finite
union of their backward cones. Initial cells already fixed by the root
remain fixed; other initial cells are free variables.

Let Phi_(i-1) describe exactly the initial assignments satisfying the root
and all preceding active reads. Introduce the previously unexposed initial
cells between q_(i-1) and q_i. With all variables strictly left of q_i
held as a single older assignment theta, put z_i=X(0,q_i), and define

    A_i(theta) = X(t_i,p_i) with z_i set to0,
    G_i(theta) = AND over 0<=s<t_i of NOT X(s,q_i-s-1).

These functions do not depend on z_i or any initial cell to its right.
The carried derivative/reset law gives the exact relation

    Phi_i = Phi_(i-1) AND
            [ b_i = A_i(theta) XOR (z_i AND G_i(theta)) ],

with all newly encountered root constraints also intersected. For a FREE
z_i and fixed theta, the number of permitted extensions is

|G_i|condition|choices of z_i|
|---|---|---|
|1|either requested b_i|one, z_i=b_i XOR A_i|
|0|A_i=b_i|two|
|0|A_i!=b_i|zero|

Equivalently, eliminating this free z_i gives

    exists z_i: [b_i=A_i XOR(z_i AND G_i)]
        IFF G_i=1 OR A_i=b_i.

If z_i is root-fixed, use its actual value instead of this elimination.
The empty t_i=0 product is1. For the first read, simply start with the root
and the entire relevant older part of its cone; no artificial q_0 is needed.

The equivalence is exact by the three Boolean cases, and induction on i
keeps precisely the assignments satisfying all active cells. By the carried
masked-cylinder lemma, with the same prepared root these are precisely
the whole-row extensions following that saved finite base path. It says
nothing about compatibility with an earlier seed history before this root.

Elimination is only for this local existence/count test: **do not discard
z_i from the surviving history relation when later reads can see it.**
The next A/G depend on the actual retained older assignment, including
z_i. Distinct witnesses cannot be selected for different clauses. Gaps
q_i-q_(i-1)>1 also retain their intermediate new bits; they are not a
single independent coin. No probabilistic law or uniform entropy loss
follows from the0/1/2 counts.

## What this changes and the exact next step

This isolates failure of a proposed active input: for a free newest bit,
failure occurs only when its extremal channel is masked and the older
assignment already forces the opposite output. A proof excluding a whole
path must eliminate ALL remaining older assignments, as the existing
root-only tick19 certificate does for its specific path. Counting free
labels, or merging a currently reset band, does not discharge that task.

For that already checked fifth active read, (t,p,q)=(19,10,29), the
25-cell root forces output1 for BOTH values of initial29, with every
older exterior assignment allowed. Thus A_5=1 and G_5=0 for every theta
extending the root. The requested b_5=0 makes Phi_5 false irrespective
of Phi_4. This is the existing certificate expressed in the new relation,
not an additional exclusion or a rerun. It also recovers GC2592's
black-mask disjunction, since G_5=0.

Local carrying request, when assembly permits: the coordinate/application
steps, seven-cell counterexample, strict increase of active q_i, and exact
Phi_i equivalence with the carried cylinder lemma. No computation or
formalization requested. Generic reset and cascade mechanisms remain prior art.

Next independent executable step: read the complete b476c1 cylinder-count
proof and compare its quantified trajectory/cylinder variables with this
prefix relation. Check whether any marginalization identity transfers
before drawing a count or density consequence. No new horizon, root or
observer run; reset-only finite-band compression is parked as above.
The final synthesis artifact read has priority when Local supplies it.
