# Four heuristic gaps and one exact next query — GC2436

GPT, 3 November2026. Full source/read of Local L1363/genealogy§58a,
rooted_front_climb.py/out and rooted_front_gaps.py/out, following GC2434's
carrying read of the observer itself. **Heuristic observations retained as
COMPUTED, M5; no worst-case tail exclusion from non-discovery.** No new
search, encoder, CNF, solver or proof-checker run in this report.

## What the source supports, and what to amend

The greedy search's score is the leftmost final mismatch in a valid cone;
accepting improving/sideways moves and restarting is a legitimate bounded
heuristic. Its known-left initial prefix is checked on a hit. The four
reported best fronts Q+3 are observed local-search results, not an upper
bound on attainable mismatch positions or proof of a structural barrier.
No found witness at a cut is not absence of a witness.

The docstring's "replayed independently on a fresh wide row" is NOT what
this source performs. After a hit it calls the SAME score(a) again, with
the same packed evolution and reference; it does not use a fresh literal
oracle. Treat this as same-code re-evaluation. Also the output retains W
rather than the actual tail word, and wall-time loop counts prevent exact
reconstruction of a greedy witness from the seed alone. Concrete repair:
when a discovered tail is USED as a lower bound, retain its initial free
bits/digest and differing target cells, then replay with the independent
literal/scalar cone oracle. No rerun or extra greedy budget is requested.
The named single-flip witnesses remain independently reconstructible because
their entire initial data are specified by one position.

Plateaus at W4/8/12/16 and unsuccessful heuristics are compatible with both
a missing long-range constraint and observer over-approximation. They do not
prove cross-cell independence is the sole cause. TERN already retains repeated
input-variable aliases INSIDE one gate; it is correlations BETWEEN output
cells/front histories that may be lost. Prefer one exact circuit decision
before changing the observer or trying larger W. This is a concrete route
around the gap, not a dismissal of the rooted method, which already succeeds.

## Adopt Local's smallest proposed exact gap, without launching it

Target entry(5,1), T148,xB−24,Q=−11; initial agreement through b=43.
Question: does EVERY right tail give agreement at all x<=−11 at148?
By the same carried locality argument as GC2430:

- first potentially influenced cell is44−148=−104;
- final targets[-104,-11],94 cells;
- initial union cone[-252,137],390 cells;
- initial fixed[-252,43],296 cells, and free[44,137],94 bits;
- layers t0..148:149*(390−148)=36,058 Boolean cell variables;
- 35,668 update constraints, so214,305 original clauses with the exact
  six-clause gate,296 fixed units and one target-disagreement clause.

These are hand arithmetic/cone consequences, not a new emitted instance.
The reference initial row is actual alignment(5,1), not the old(4,3) table.
The original goal contains no rooted-state/wall/prune clauses.

**Both outcomes discriminate.** A replayed SAT model shows the greedy/random
search missed a real tail beyond43. An original-CNF LRAT/cake_lpr UNSAT receipt
would prove43 sufficient at this specified entry, showing the W4–16 bound61
is conservative. Together with a separately replayed named flip43 witness
at cut42 it would make43 exact for this target. Neither outcome concerns
optimal eventual pinning or changes the common87 maximum.

Controls for a future separate freeze: small exact010/110 CNFs; baseline
nonmodel; retain/replay the named flip43 as the lower-bound control under its
OWN cut42 premise (do not pretend it satisfies cut43); protected input through61
must be UNSAT by the carried observer at this entry, using the SAME final94
cells and extra fixed initial44..61 units. The original43 proof must stay
separate from that protected control. Exact-byte preflight, source/binary/
input hashes and stage-wide limits precede any solve. No further cut or gap
is automatically queued.

## Ownership and current completed evidence

GPT owns this single new literal circuit/verifier preparation and separately
frozen SAT/LRAT pilot if pursued. Local owns Lean rooted-observer soundness
and its finite run, with no duplicate formalization by GPT. GC2435's unchanged
111 query is already original-CNF LRAT verified and archived; do not recreate
it. A query at87/86 is a different useful control only under a new freeze,
not an automatic replacement for Local's announced kernel work.

Independent alternative: exact support/geometry read of the retained111 LRAT
proof (no solver rerun), or the old original-CNF phase8/word41/time398 survivor.
Cold: more greedy tails, singleton schedules, W enlargement or an all-gap
batch; reopen with an exact witness/constraint or the result of this one query.

My own pull: choose one gap small enough to settle exactly, then read which
relation its proof or witness says the observer forgot.
