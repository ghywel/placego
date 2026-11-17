# Row119: the actual four-input patch and two ways to carry a black value

GPT GC2748, 8 November 2026. Continuation of the owner's row119 pull while Local's single Intel graph job ran. No new SAT search or enlarged cone. The [preceding transport result](GPT-OLDER-PULSE-CUT-TRANSPORT-20261108.md#outcome--gc2741) and GC2734's phase/support steps are now **PROVED hand/two-party**, carried by Local L1592. Their machine guards retain their original-CNF provenance.

**Result:** the older pulse does not force row119 cells7/8 to have nonzero OR. Saved full-E history14429 has those cells both white, yet carries the required later black value through cells9/10. A four-register/four-actual-input reconstruction explains the local choice. The six saved histories and32 Boolean cases were independently replayed on Intel; this is a same-worker self-check. The new fixed-frame specialization and interpretation remain **PROOF-SKETCH pending Local's carrying read**. Neither the local patch nor the six histories is a solution of the full shared4→7 return.

## A known gate, now read at the shared row

Use the same initial-black driven right half and one-based physical columns as GC2741. Set

```text
a = x119,6     b = x119,7     c = x119,8
d = x119,9     e = x119,10    Q = x121,8.

Q = a XOR ((b == c) AND (d OR e)).
```

This is the already known `Rule30FirstChecks.two_tick`, in reflected spatial indexing, applied to an interior five-cell neighbourhood. It follows directly by substituting the local rule twice; no boundary enters this patch. Current actual kit source at `b85e8a73c560e0222c5ccfe8d37dd8471842310e`, declaration and full proof read. The scalar32-case replay agrees. Known, reproved here; no new two-tick theorem is claimed.

The controlling test is **equality** of b and c. If they differ, Q copies a; if they agree, Q is a XOR(d OR e). Thus their OR alone loses relevant information. Under GC2741's common temporal premise S, the older pulse P implies Q=1. The exact specialization is therefore:

```text
P=1 and b!=c  implies a=1;
P=1 and b==c  implies a XOR(d OR e)=1.
```

The certified white input is x118,8, not c=x119,8. No universal assertion c=0 is inferred from that guard. The values c=0 and a=b below belong to the retained source64 histories, not to every physical history under S.

## Four register cells, four actual incoming values

The inverse rule is x(t,p−1)=x(t+1,p) XOR(x(t,p) OR x(t,p+1)). At the seam before the relevant patch retain

```text
(A,B,C,D) = (x119,10, x119,11, x120,11, x120,12),
(r0,r1,r2,r3) = (x121,11, x121,10, x121,9, x121,8).
```

For each r in that order, recover

```text
upper = r XOR(C OR D)
lower = upper XOR(A OR B)
(A,B,C,D) := (lower,A,upper,C).
```

The four lower outputs are x119,9, x119,8, x119,7, x119,6. Together with the initial A they give the exact five-cell gate above. The first two substitutions recover x120,10 and x119,9; shifting the state makes the same argument apply at the next column, proving the four-step statement by induction.

These eight supplied bits are an interface to the **same full ancestry**. They are not freely chosen exterior cells or an autonomous eight-bit return state. The other reconstructed register pairs, common later-head acceptance checks and earlier E/A^4 ancestry still constrain which state/word pairs are physical. The20-pair/204-bit register from GC2741 has not been replaced by this local patch.

## Reuse of the six whole-E histories

The prior GC2724 full-E witnesses have source row1 low seven bits64 and input labels4482,4498,4520,4521,4522,14429. Source time11 corresponds to physical119 under the even108 shift, and time13 to121. Initial-black drive phase is preserved. The saved histories run through85 ticks and already retain the same source/head ancestry. The new independent scalar replay verifies all85 updates and the local patch; it creates no new solver evidence.

| Label | Row119 cells6..10 | Mechanism for Q=1 |
|---|---|---|
|4482,4498,4520,4521|11010|b!=c, copy a=1|
|4522|11011|b!=c, copy a=1|
|14429|00011|b=c=0, use d OR e=1|

For14429 the exact source-frame root is **77371252455336267063753023**. Initial state(A,B,C,D)=1100, actual incoming word(r0,r1,r2,r3)=0101, older pulse x3,1=1 and Q=x13,8=1. Thus **older pulse ⇒ OR(row119 cells7/8)=1 is REFUTED by an existing full finite history**. This root realizes the source64/full-E conditions; no earlier E/A^4 ancestry at the full target's193 seam is claimed.

All six retained histories satisfy the later common S heads, but they are a selected source64 class. Their two patterns neither exhaust all common-S physical histories nor prove that the original45-tick head premise forces source64. Their low-seven row11 words are100 for the first five and28 for14429, giving a second simple check of the hand trunk calculation. Complete roots, register states and actual incoming words are in the evidence result.

## What this changes, and the next step

The obstruction is more precise: a single nonwhite-pair explanation cannot transport the older pulse. A valid reduced history relation must preserve both the unequal-pair copy branch and the equal-pair conditional-inversion branch, with its actual incoming word. The six source64 histories show both branches are physical through one full E; they do not decide which survives the additional earlier shared-return history.

Next executable step: substitute this five-cell gate into the existing original-cone guard13 derivation and mark which ancestry/head clauses carry each branch. Keep the exact source45/global193 phase dictionary and the earlier E/A^4 obligations explicit. Do not add another free-pair strip filter or launch a larger full-target query. Independent alternative: the explicit20-pair inverse-register relation with all four actual top values, retaining the older-pulse predicate as a joint condition rather than an autonomous transition.

Local carrying question: (1) the row119/121 phase and reflected five-cell gate; (2) the four-state recurrence and its actual-word scope; (3) the14429 counterexample's precise finite-history scope. No new computation assigned. The generic two-tick identity and GC2741's already carried inference need no repeat review.

## Evidence and resources

Record searched: GC2724/GC2734/GC2741 and their original proofs/witnesses, `record_find` output, current kit actual `lean/`/`equivalents/` sources and catalogues, in particular `Rule30FirstChecks.two_tick`, ControlledResponse, Predecessors, LeftCoincidence's two-step retrodiction and BlackRuns. Previous primary permutivity sources remain applicable; no new theorem/novelty or submission claim. Latest successful complete kit/portal index is retained separately from this source read.

[Replay source](../tests/probes/swarm/sw02/block3/lock_job_final_replay.py) was frozen in GC2747 before execution. Independent lineage replay and saved-history replay together complete in0.544260 aggregateCPU/0.55wall seconds, including monitoring; worker rusage and both launcher receipts are retained. A prior sandbox launch was refused before spawning a worker (0.111124CPU) because swap monitoring lacked host permission. The unchanged plan passed with that permission and every monitor/cap active. This subsecond job ended before the first periodic RSS sample; no zero-memory-use claim follows. Combined resources and the evidence digest are in the [job outcome](GPT-LOCK-WIDTH-JOB-REVIEW-20261108.md#outcome--gc2748).

My own pull: which of these two local mechanisms is compatible with the older E/A^4 ancestry on the actual shared row, rather than just with one whole E.

## Local carrying read — L1598

*Local, 8 November 2026, 18:18 UTC. Requested in GC2748. Same independent replay as the [lineage read](GPT-LOCK-WIDTH-JOB-REVIEW-20261108.md#local-carrying-read--l1598): [`local_carry_gc2748.py`](../tests/probes/swarm/sw02/block3/local_carry_gc2748.py), [output](../tests/probes/swarm/sw02/block3/local_carry_gc2748.out). The prediction was written before the run, and an addendum (part C) before that part ran. Every prediction held.*

**Verdict: all three items CARRIED.**

1. **Phase and gate.**
   - The kit's `two_tick` is stated for `zrow` of a zero-boundary half in reflected indexing. Its proof is the 32-case identity f(f(a,b,c), f(b,c,d), f(c,d,e)) = a ⊕ ([b = c] ∧ (d ∨ e)), with f(l,c,r) = l ⊕ (c ∨ r) and l the column nearer the drive. I rechecked all 32 cases in the physical orientation.
   - At row 119 the patch is interior: cells 6..10 at 119 and 7..9 at 120 never read column 0. The even shift 108 keeps the drive phase.
   - The gate is the last two terms of L1592's telescoped Q on diagonal j = 80: Q = x119,6 ⊕ (x119,7 ∨ x119,8) ⊕ (x120,8 ∨ x120,9). So a = x119,6 is itself the six-term partial parity from the white center at 113.
   - From P ⇒ Q (PROVED, L1592): under S, P = 1 and b ≠ c give a = 1.
2. **Register recurrence.**
   - Each round applies the inverse rule twice: at (120, p + 1), giving x120,p, and at (119, p + 1), giving x119,p − 1. The state (x119,p, x119,p+1, x120,p+1, x120,p+2) shifts one column, and induction over four rounds gives cells 6..9.
   - Checked as an identity on 20,000 random rows. On the six histories, the intermediate values equal row-12 cells 10..7.
   - Scope as GPT gives it: the eight bits are read from one history. They are an interface, not a free or autonomous state.
3. **The counterexample's scope.**
   - Root 77371252455336267063753023 is a finite start at source tick 0 (physical 108). My own 85-step replay reproduces all 86 saved rows.
   - The history satisfies S (heads 5..45), P = 1, col8(10) white, Q = 1, and the source-64 row-1 condition. Its row-119 cells 6..10 are `00011`.
   - It therefore REFUTES "S ∧ P ⇒ x119,7 ∨ x119,8" for histories that start at physical 108 under the 45-tick premise.
   - It says nothing about histories with a prescribed earlier E/A^4 past, nor about a seam-193 target witness. The six saved histories are GC2724's source-64 class, not all of S.

**Addendum (part C, COMPUTED on the three GC2741 roots):** the right-OR branch does not need the pulse.
- The P = 0, Q = 1 control 54421244276371 has row-119 window `00011`, the same as 14429, and reaches Q = 1 by right-OR. Its Q-term word 01110101 is also 14429's.
- The P = 0, Q = 0 control has an unequal pair and copies a = 0. The P = 1 fixture copies a = 1.
- So at row 119 the five-cell window does not determine P. In these nine histories the pulse is visible only on the left-copy branch, through cell 6.

The proved half is above: P = 1 ∧ b ≠ c ⇒ a = 1. The converse half is OPEN: under S, do P = 0 and b ≠ c force a = 0? If so, equality P = Q holds exactly on the left-copy branch. The corner (0, 1) would then be purely a right-OR phenomenon.

This is a single specific branch condition on the original 45-tick cone: S, head 3 white, x11,7 ≠ x11,8 and x11,6 black. Its expected outcome and use are in L1598. It is offered to GPT, who holds the original-CNF tooling; Local runs no solver on it.
