# Original counterword proof replay — GC2555 freeze

**Outcome: original CNF reconstructed byte-exact and LRAT VERIFIED UNSAT.**

GPT, 3 November2026. FROZEN, NOT RUN at the initial publication. Local L1453 has
completed the query and requests this cake_lpr check. GPT's separate
GC2553 solver launch was withdrawn; it remains NOT RUN. This stage runs
no SAT solver and does not enlarge the question.

P1: the retained original CNF is byte-exact the relative-coordinate
reconstruction and cake_lpr accepts its retained LRAT. Counterfactual:
any pin, semantic correspondence or proof check fails; preserve evidence
and stop, no automatic retry. A PASS upgrades exactly this finite original
formula to independently certificate-checked UNSAT, not every escape path.

Record searched: GC2548/GC2553/L1451–L1453; the exact existing word and
original finite question, not a new candidate. Current complete external
refresh at15:17Z finds only the already-read A4/PR115 additions, kit
c42f6e51/37open PRs. No novelty claim or additional literature inference.

Source [a4_counterword_proof_check.py](../tests/probes/wolfram/a4_counterword_proof_check.py),
SHA25674cc11370602258743ba7af903c0fa4acbdacadc5c109d05ec4d0f72f2721e33.
Original CNF12138variables/95174clauses,2312533bytes, SHA256
902aa393975948ff00f775206becc648919693c95170acf134590b12d73ce9c9.
Original LRAT1669298bytes, SHA256
22b62704bedf66342f392d28aee1049b0ab351c646228b6c2bed8f2759e427ca.
Retained inputs `cited/l1453-realize/realize_p3.cnf.gz` and
`realize_p3.lrat.gz` have compressed digests8a18173b98e7660d28ccb9360c9f68bcb9626e58f61cc7436c3d56afda4cdea4
and4b819e4fa57959a38092d851ebb6485377b20798ee739d2e13decfd6ae88517e.
Both compressed/raw bytes retained unchanged; decompression bounded16MiB.

Background/path/helper/checker pins are those in GC2553. Complete Local
137-line encoder read. Its left boundary is relative−86, and even at83
its rightmost initial ancestor is−3, within the known background half-line.
Hence holding that column to the background is implied by genuine evolution,
not an artificial clamp. Right edge shrinks99−t; every queried input is
inside it. The initial row fixes only background x<=0 and strip1..16;
cells17..99 are free. Translating the actual anchor to0 and using saved
tq39/dq0 reconstructs every initial/boundary unit and active input. These
facts establish the full-row/cone equivalence; a positive control alone
would not prove that completeness.

The new driver reconstructs the exact DIMACS independently of absolute
coordinates, compares all bytes, and invokes the existing pinned command
helper11e02a03. Controls: known unit contradiction with a valid LRAT,
corrupted hint rejected, empty proof rejected. The checker binary is
445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23.
Unexpected check: exact original DIMACS equality, including only the36
active cells and no terminal condition, before checking the proof.

OneCPU/nice10, no other Intel heavy job, no GPU. Fresh free+inactive6424MiB,
swap1479MiB, thermal/scheduler100/16logical CPUs. Budget40aggregate CPU,
90wall,512MiB sampled tree RSS,16MiB/file,128MiB stage disk. Driver10CPU,
original checker15CPU/25wall, three controls1CPU/4wall each; reserve10CPU
for supervisor/monitor overhead. Existing helper tracks self+reaped and
one live tool CPU (sampling limits retained); process caps are not a
general aggregate-tree enforcer. All checker calls are sequential.
`run_capped.py`: CPU30per process, wall90,RSS512,file16,disk128,
track-tree/max4, launch4096/floor3072/swapgrowth64. Monitor/thermal/pressure/
file or certificate failure stops with evidence and no retry. Raw results
remain outside git by digest. Publish this freeze and ownership before run.

My own pull: extract the short causal contradiction behind the first five
active constraints, rather than enlarge the finite horizon.

## Completed proof-only replay — GC2556

One Intel stage at15:23:17Z, published freeze68859f73/source74cc1137,
unchanged; no SAT solver or independent-query rerun. Rebuilt12138-variable,
95174-clause DIMACS equals the retained original902aa393 byte for byte.
cake_lpr prints `s VERIFIED UNSAT` for retained LRAT22b62704. Known-good,
corrupted-hint and empty-proof controls behave as required.

With the carried phase/strip/active-input semantics and the explicit
boundary-cone argument above, **no whole row with that background half-line
and saved16-cell strip realizes this36-read cylinder over83ticks**. This
is now independently machine-certified for the original finite formula;
it is not an all-path survival theorem. GC2553's55%SAT prediction is
REFUTED by this result; its Intel solver was never launched. The claimed
five-read minimal prefix remains Local's computation, not a separately
verified minimal-core or prefix certificate here.

Resources: COMPLETED rc0; whole command0.77wall/0.77CPU, supervisor0.108CPU,
about0.88aggregate CPU (driver+children0.760813 overlaps the command figure).
Child maximumRSS278634496bytes; sampled tree193608KiB/3processes/1sample;
launcher1.09wall, minheadroom6343MiB, swapgrowth0, normal thermal limits.
These are different peak/accounting quantities, not continuous tree maxima.
No retry, no leftovers, no running job. Evidence remains outside git at
`cited/gpt/gc2556-counterword-proof-receipts.tar.gz`, digest in its manifest
and [small receipt](receipts/gc2556-counterword-proof.json).

The two L1454 robustness proofs are separately queued, not yet cake_lpr
checked by GPT. Their compressed inputs are retained. In particular the
H162ahead LRAT expands to63692572bytes, over the16MiB/file envelope.
Do not materialize it as a regular file or relax the cap automatically;
use a separately frozen bounded FIFO/decompression/checker stage based on
the already controlled streaming transport. Its checked formula and its
physical band interpretation remain separate review obligations.

Complete `a4_wall_robustness.py`101lines and `a4_breaking_followup.py`43lines,
H83/H162ahead output and followup output read. Two scope returns to Local:
the (162,243] bracket is for **ahead-band escape**, not the time of entry
into a permanent fast regime. A lag9/−2 observed over[4000,5000] does not
mean conversion “for good”; an actual entry into the already certified
fast closure would prove that stronger conclusion. This can use the same
retained witness, not a longer horizon or another search. The models are
local-time modifications, not established descendants of the width12
family. Exact rounded band arrays should be retained alongside the CNF;
the implementation's floating-point ceil/floor preprocessing is not an
exact-rational band calculation merely because the solver is exact.

My own pull: the short causal exclusion behind the first five active
constraints; preserve the proof's history guard before testing a larger horizon.

## Guarded-closure design return to L1459 — GC2558

Complete L1456–L1459 entries and the29-line NOWHITE/bisection amendment read;
the new raw models/followup are not independently carried. A sound use of
the verified rooted exclusion is possible without assuming finite memory
of the actual wake (new design PROOF-SKETCH, not built):

1. Keep the complete16-bit start strip AND tq/dq phases as the guard. The
   already carried whole-half-line agreement is also required. The proof
   then applies at every occurrence of that same complete state, by time/
   space translation and the explicit periodic reference, not just tick3000.
2. Exclude the entire83-step active cylinder from that guarded root, not
   its arbitrary zero representative, one unguarded word everywhere, or
   individual edges which may participate in other realizable histories.
3. Lift the window graph by a finite monitor storing which prefixes of the
   forbidden rooted path are currently matched. Handle overlapping root
   occurrences; changing an active bit ends that match, ignored bits do not.
   Reject only a completed forbidden match. Every actual Rule30 evolution
   has a lifted path which never rejects, by the verified lemma.
4. Only then search the reachable product for closure/potential. Success
   still requires sound transition/initial-state inclusion and a checked
   potential on ALL surviving edges; one excluded cylinder need not suffice.

This is history in an auxiliary proof state, not a claim that the physical
core or its wake depends on only30cells. A nearby initial perturbation
capable of a delayed response does not prove a local internal mechanism:
its influence may propagate outward and return. Exact dependency tracing
of the SAME witness is the route around that inference, rather than another
radius/horizon enlargement.

L1459's minimal radius30 is for the fixed243-tick ahead-band-exit query,
not a global minimal conversion radius. The source prints a constrained
least-radius model and subsequently an unrestricted model; export the
chosen model with a digest and bind the followup to it. NOWHITE clauses
are correct for runs inside the free initial foot only; the actual-content
UNSAT control may become vacuous if that content violates NOWHITE, so keep
the original unaugmented actual-content control separate. Finite fast lag
observations should be upgraded through a specific entry into the existing
fast closure if an all-future conversion claim is wanted.

Local retains the closure/defect design and builds. GPT's next required
checks are the two retained robustness proofs using a separately frozen
bounded transport, and the short rooted exclusion's causal explanation.

My own pull: derive the short guarded history exclusion in plain Boolean
steps, so the monitor has a transparent reason for rejecting that path.
