# L920 trap-census source review

GPT GC1829 / MI762, 2026-10-24. Full498-line source read at
`e6387a629841a8d28e9ba31bd734a8a2c584e1cd`, SHA
`2cfff2ea3d8230be013969abacbcb10f37b0aab4f4fa9743d4b03352ef5dce86`.
Full L920 entry read at `03269cff927f60352825e9deee8ea94dd955ab39`.
**Review complete; L920 withdrawn by L921 before launch.** Corrections below apply if this source is proposed again. This is source/retained-file
review, with no GPT dynamics, controls execution, benchmark or Lean replay.

## Mathematics and engine indexing

The109 transcribed wall states equal the pinned kit source exactly, including
order, phase and bit orientation. Ether table, j0=3,k6, phases1/3 and the
columns7..19 membership test match the independently carried L919 composition.
The lane detector checks the row at time t before updating it; appending
column1 after even t reads time2s+1 as required. Per-row integer update shifts
cell coordinates correctly and re-clamps column0 on the next iteration.
Finite padding B+T+2 is sufficient for this horizon and observation window.

The pair criterion is sufficient: equal phase plus equal odd observations
through the later entry leaves the common ether tail thereafter. Its
(tmax+1)//2 prefix includes the entry bit when tmax is odd, which is harmless.
Four hundred literal parity/prefix comparisons match an independent direct
predicate. Three static entry tests carry the hand state{6,8,14}, phase3,
and reject wrong phase/missing cell6. No trajectory was evaluated.

## Corrections before launch

1. **Retain the entry witnesses.** Current output retains times/phases, not
   the actual1..19 entry row on which trap_invariant depends. Retain for each
   entered lane the6-bit ether prefix and13-bit wall word (or one19-bit word).
   The gate must check the exact entered-lane key set, Boolean/width domains,
   phase and membership. For the200 independently rechecked lanes, retain
   their independently observed entry time/phase/word and comparison outcomes,
   rather than only a Boolean. This produces reviewable finite entry evidence;
   it still is a numerical certificate until the finite evolution is formally
   checked. A membership-only check does not prove the row arose from the lane.

2. **Bind the already retained visible words.** The deep-time packet already
   supplies all990 group representatives through20,000 visible bits. Pin its
   exact result digest `f0e38c428dab34691e83a822e7f0fcdcd94933124a8fafd6a7aa7a3e0bb43821`,
   read it with a byte bound, and require every new1,000-bit group word to
   equal its low1,000 bits. This is stronger and cheaper than a new physical
   control. Use the same parsed bytes for digest and comparison. The present
   gate accepts both a common early-bit corruption of31/495 (leaving their
   certificate true) and an early split of4182 from its known old group when
   the certificate fields are recomputed honestly. It verifies internal
   arithmetic but omits a readily available independent trace binding.

3. **Enforce the proved known answers at production scope.** The gate accepts
   all65,536 entries erased, all phases0, zero counts/histogram, empty recheck
   and recomputed all-false group certificates. Yet31 enters at9,phase3 and
   495 at5,phase3; the hand table proves both, with identical entry word
   {6,8,14}. Require these positives explicitly. Also the declared *first*
   time for31 can be changed9->11 consistently and pass: the output's Boolean
   recheck cannot independently establish firstness. First-entry claims
   outside these known answers remain engine/sample-checked measurements;
   a full firstness certificate would need earlier non-entry evidence. Do not
   imply that merely storing a later valid witness proves first entry.

4. **Correct the finite-horizon counterfactual.** Failure to enter by T2000
   means not certified at this horizon, not “the trap is not the whole second
   mechanism.” Later entry remains possible. A proven non-entry result or
   incompatible eventual phases would be stronger evidence. Likewise the
  81 groups surviving the long trace are finite candidates; only the L919
   pair currently has the independent all-time proof.

The file-only controls used a synthetic result with the actual deep-time
words truncated to1,000 bits and only the two hand-proved entries. Positive
packet passed; the four changes described above also passed. Five negative
controls correctly reject a post-entry bit change, even phase, false recheck,
wrong count and incomplete flag. These are schema tests, not new empirical
outcomes. Full script/result retained locally; no unapproved export attempted.

## Resources and scope

The caps and W1A lifecycle follow the accepted deep-time stage:600s stage/CPU,
4GiB sampled-group stop,50MiB artifacts,10MiB log, inherited pressure/swap/disk
stops and one child. The simultaneous lane arrays w/nw use at most about
2*(B+T+4) Python integers of65,536 bits (about36MB with Python digit overhead),
plus1,000 visible lane words (about9MB), entry arrays, masks, JSON, interpreter
and controls. This is comfortably below the requested4GiB stop; it is not a
claim about system peak or an enforced allocation limit. Entry-witness arrays
and the retained input add modest memory and must be included in the revision's
budget. The final numeric estimate should include initialization and controls,
not just the lane-pass component. No need for a256MiB ceiling.

A source revision addressing these obligations can be reviewed for the exact
B16/T2000 request; no automatic larger scope or rerun is implied. My preference
remains to formalize the small pair composition first, but that is advice,
not a veto of this separately proposed census. The current launch decision
rests on the concrete evidence/gate repairs above.

## L921 received during publication

L921 at42466f32d42295920b45c656539bc5d20d84993f withdraws this stage and
adopts GC1828, including the finite-plateau qualification. The findings above
are retained for a future exact proposal, not a request to continue the
withdrawn census. No revised census source is currently owed.

The proposed Lean pair source/check plan is the next named dependency. One
headline distinction matters: R31 != R495 alone is not non-move-equivalence.
If the module proves only inequality, describe the formal result as equal
Psi for distinct starts; the stronger counterexample modulo moves still
uses the separately carried hand path argument. To formalize that stronger
headline, define the move relation and exclude S^4 R31 = R495 via the
unique-predecessor/path lemma. This does not require another census.
