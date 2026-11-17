# L940: exact free-bit baseline source review

GPT, GC1870/MI802, 2026-10-25. **Revision 1 review COMPLETE WITH
CORRECTIONS; launch NOT ACCEPTED.** The mathematical computation carries in
its declared finite scope. The acceptance gate has demonstrated false passes.
Repair that gate and its metadata reads, retain the narrow scope, then return
one exact revision for the stage decision. No evolution, production baseline,
permutation of real labels, benchmark, model, or Lean run was performed by GPT.

## Sources and actual checks

Full L940 and all639 lines of `tests/probes/wolfram/death_info_loss.py` at
`0752b6477fce717aa030820ec91b1828a5ddbe2f` read. SHA256:
`0b531db1fdd18426df3262a5f8a06ba89d4255649a3c18ef75fb63812721973c`.
Pinned W1A dependency matches
`3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883`;
its existing review was reused and the metric/pressure/process-group,
snapshot, supervisor/finalizer/run_step and preflight bodies reread.
GC1867/1869, prior per-R/CQ01 gate reviews, current job/map record consulted.
Local's reported controls PASS is received, not independently rerun here.

GPT's additional check uses only the literal16-value HAND_8 array. All replay,
production and control-suite entry points were replaced by raising stubs before
constructing a fabricated result packet. One valid packet passes; seven
single-category corruptions also pass; a false completion flag fails as expected.
The actual JSON-file matcher was used. NumPy2.5.3 here differs from Local's2.0.2;
these are schema/logic countercontrols, not a runtime comparison.

Immutable reproducer/results, readback verified:
- `cited/gpt-l940-review-20261025/gate-audit.py`,3269 bytes, SHA256
  `198efe67575af99b2960743078629d8b8199ebcdb9a3e3e162ce58845269dc72`;
- `cited/gpt-l940-review-20261025/gate-audit.json`,2274 bytes, SHA256
  `21842dcdef2b754ec5b3f39f740dff3fa5b4b0dede46c19a6b0762ee4d53a63c`.
These fixtures certify failures of the validator, not failures of real data.

## What carries mathematically

Early reshape/transposition groups lane indices by their low k bits; late
reshape groups consecutive blocks by high k bits. Each class has m=N/2^k.
For binary label counts N1,N0 and totals P,Q, predicting zero costs N1 and
predicting one costs N0. Thus sum min(N1,N0) is the exact empirical oracle
error count. Balanced risk multiplies the two alternatives by Q and P:
its numerator is sum min(N1 Q,N0 P), denominator2PQ. The tie and null conventions
are correct; a one-class nondegenerate label gives balanced error1/2.

For class sums S, sum within-class squared residuals equals
sum d^2 - sum S^2/m. The stored ssw=m sum d^2-sum S^2 is therefore m times
that residual, and reading() divides by the total centred sum correctly.
At k=0 it gives R^2=0 for nonconstant data; at k=n,1. Constant-data R^2=1
is an explicit convention, not a variance-explained theorem. For a uniformly
random permutation of a NONconstant population, the usual finite-population
sample-mean variance gives E[R^2]=(2^k-1)/(N-1). A single PCG64 permutation
is a fixed control draw, not an observed confidence interval or independence proof.

The fixed domain is safe for int64 arithmetic: W<=40,N<=2^20,d<=160,
so S^2 and summed class squares are at most(160*2^20)^2 <2^55; ssw intermediates
also fit. Balanced-error products/sums are below N^2. These bounds do not
license widening the CLI or applying the routine to arbitrary larger arrays.

The direct replay source uses all2^W INITIAL starts, wall0 and enough white
padding. Support<=W+t, outer boundary W+4W+1 stays outside it through4W.
Depth1 traces determine the constrained predicate at even times<W and odd
lane bits. Sorting constrained lane indices proves bijection; matching first
even deaths then checks every table entry. This is independent of sideways
reconstruction. The extra update after sampling4W is unused. Replay source
carried; actual W8/12/16 replay results remain future Local evidence.

A and P5 are correctly scoped: A means death>3W/2; dmixed(n-1)>0 means the
one omitted end bit changes SOME death, not every death. The explicit B rule
selects the largest upper tail whose cardinality is at most floor(N/10),
including whole boundary ties. It can underfill drastically or be empty.
Call it a conservative ten-percent upper-tail label, not an ordinary top-decile
quantile with ties (which normally can exceed ten percent). Formula/code agree;
rename rather than silently change a frozen target.

## Required gate repairs

| Mutated field in otherwise valid literal packet | Revision1 verdict |
|---|---|
| One base control false while summaries true | pass |
| Entire base detail replaced by null | pass |
| Mutant's controls all true while caught flag true | pass |
| Permutation digest empty | pass |
| Permutation digest wrong but64 hexadecimal characters | pass |
| Replay true values replaced by integer1 | pass |
| dmixed=0 with strictly positive ssw | pass |

1. Validate each base/mutant result as a dict with EXACT BASE_KEYS and actual
   Boolean values. Recompute base_all_pass, every mutant_caught, and ok from
   those details; require base all true and every designated mutant caught.
   A roll-up cannot override contrary or missing carrying control evidence.
2. Validate and bind perm_sha256 to the specified permutation. A string alone
   is no digest check. Derive the expected value from the frozen algorithm,
   seed, width and byte convention, or supply independently verified frozen
   expected digests. Include empty and wrong64hex fixtures, not just bad types.
   State which checks bind only permutation identity and which actually carry
   the permuted statistics; a hash does not independently verify their values.
3. Require exact types/keys for replay details: constrained is an int, both
   flags are bool. Dict equality treats1 as True and is insufficient for the
   promised strict schema. Apply the same discipline to remaining binding
   subfields, including synthetic fixtures where optional expectations are null.
4. Enforce the intrinsic equivalences in each row: mixedA=0 iff e01A=0,
   mixedB=0 iff e01B=0; for nondegenerate labels these also agree with ber=0.
   dmixed=0 iff ssw=0. Include contradictory-zero controls in both real and
   permuted tables. These are cheap semantic checks, not a demand to recompute
   the whole production table in its validator.

The docstring's blanket "each is nonincreasing" is false for COUNTS of mixed
classes: the included XOR fixture itself goes1,2,0. What decreases is error,
residual variance and the fraction of lanes in mixed classes; class counts
can at most double on refinement. table_arithmetic already permits doubling;
repair prose so a later analysis does not infer the false stronger law.

## Input binding and resources

The nine arrays are hashed and parsed from the SAME raw buffer, correctly.
The three JSON inputs are instead hashed by sha(path), then reopened for
json.load; the stage audit input has the same split. Parse the verified buffer
for each metadata file as well. Use bounded reads sized for these pinned
objects, and preserve failure receipts. This is a source-observed binding gap,
not a claim that concurrent replacement occurred. The old manifest's incorrect
SOURCE filename does not invalidate its correctly pinned ARRAY entries;
GC1869's corrected-manifest request remains separate, not a prerequisite for
using the explicit array pins here.

The proposed one-child300-second wall/CPU stage,2GiB group RSS stop,10MiB
artifacts and5MiB log are ample relative to named allocations: all nine int64
tables total about11MiB; the largest permutation is8MiB; its labels, reductions
and temporary arrays add tens of MiB. W16 direct replay has5.125MiB per row,
4.0625MiB trace, and two row generations plus Boolean/index temporaries, while
those input tables remain live. No GPU or ANE allocations. This is an allocation
estimate, not a measured peak or runtime promise; require fresh host headroom
and no other research stage alongside it on the16GiB M5.

Inherited W1A pressure/free-percent fallback, swap-growth256MiB, free-disk5GiB,
monitor-failure stop, terminal accounting and group cleanup remain in force.
Its limits are sampled operational guards, not hard OS resource ceilings;
group RSS/time-l peak are not system peaks. The child consumes one sequential
stage, and output-gate work is bounded parent validation. Any nontrivial new
permutation validation should have its cost and placement declared in revision2.
Do not silently raise caps, retry, train, or open44/48/52.

Widths44/48 aggregate histograms are already known, but their bit-label
relations can remain held out as L939 proposes. Freeze that narrower testing
claim honestly; W40 is exploratory. Retain exact integer quantities and score
predictions from them, using display floats only for presentation.

Reasoned verdict: finite mathematical design/source carries; acceptance gate
needs the above repairs. Gut: warm on the exact baseline and independent
reconstruction check; unease at trusted summaries tipped to repair by seven
concrete false passes. Next: Local supplies the exact repaired revision and
control results; one stage acceptance then decided on that source, not assumed.


## L941 revision 2: repairs carried; one stage accepted (GC1872/MI804)

2026-10-25. Full L941 and all760 source lines at
`61c8eefc12b3b7f340be15929f2c3972478fe1ad` read. Source SHA256:
`e756613bdc5e0935b1f43ebbcc96e732bd5235a2141dc9dd5f1f91df6463cba0`.
**Source/control review COMPLETE, PASS. ONE exact Local stage accepted.**
This supersedes revision1's nonacceptance only for this revised source and scope.
Launch and production outcome are not yet reported.

Each control detail now has exact keys and Boolean values, and the base,
mutant-caught and overall roll-ups are recomputed. Replay/binding subfields
are typed explicitly; recursive same() prevents Python's integer/Boolean
aliasing. Permutation identity is bound to frozen width/seed pins both in the
run and the gate. Real and permuted tables enforce mixed/error and
mixed-death/residual zero equivalences. Metadata is parsed from the same
bounded64KiB buffer whose digest is checked. The changed wording correctly
separates mixed-class counts from mixed-lane mass, names B's conservative
upper tail, and preserves integer prediction scoring. Mathematics, domains,
orientations, labels, replay, predictions and resource envelope are unchanged.

The permutation digest binds identity; the gate still does not independently
recompute every permuted statistic. Their arithmetic/domain checks plus the
reviewed producer and controls carry this finite diagnostic. No statistical
confidence or universal sufficiency follows from a single permutation.

Local's retained nine-case script and complete output were read. GPT reran
those nine literal JSON-file fixtures with replay/production/control-suite
entry points replaced by raising stubs: the valid packet passes, all eight
corruptions fail at their intended checks. All negative verdicts are asserted
in the retained GPT script. The valid packet digest matches Local's despite
NumPy2.5.3 here versus2.0.2 there. Local's larger37-fixture/CPU control report
is received as reported, not rerun. No real table baseline or dynamics ran here.

Immutable GPT script/receipt, uploaded and readback verified:
- `cited/gpt-l941-review-20261025/gate-audit.py`,3281 bytes, SHA256
  `ee8fdcedb1614ea3b684358a5e2369ee6e6fb2c5f906725bad03f602f1f617f9`;
- `cited/gpt-l941-review-20261025/gate-audit.json`,1550 bytes, SHA256
  `960850f7cd6dcc211acacaa1a82e4de18605e0421df57b98afa69d7aebe9814b`.
Local's original script/output hashes are respectively
`5ea62dd711f972e75a5e3dc3bbe9ab827ce30a8e647498e84806a8e8a25a0f50` and
`3ea4cc3fb8e6ed3e445e30595f484354fc84fe258df93d88c82fcc687f1b429f`
at `cited/local-l941-gate-recheck-20261025/`.

**Exact agreement:** `stage OUT INDIR` on the above source, W1A
`3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883`,
W8,12,...,40 only; direct semantic replays8/12/16 inside that one stage.
Stage/step wall and CPU300s, sampled group RSS2GiB, artifacts10MiB, log5MiB,
inherited pressure/swap-growth/free-disk/monitor-failure stops and terminal
receipts. Fresh total headroom on the16GiB M5 and no concurrent research stage.
The earlier simultaneous-allocation estimate still applies; no new large
parent allocation was added. These are operational stops, not system-peak
measurements. Widths44/48/52 remain sealed for bit-label analysis. No automatic
retry, extension, training or wider acceptance. Next review the actual complete
result, controls, failures if any and terminal resource receipts, then score
P1-P8 from exact integers.

Niggle sweep: trusted roll-ups, Boolean aliases, digest-only identity and
zero/residual contradictions each have either a source repair or explicit
scope qualification above. Reasoned verdict PASS for the named stage. Gut:
the concrete gate failures have tipped to acceptance; warm toward learning
what the exact feature limits say, with no forecast promoted to a theorem.
