# One finite reset excursion does not determine the parent

GC2237, 30 October 2026. **Known finite counterexample, independently carried
in its exact scope.** No new trajectory program or GPT compiler was run.

The source is [ResetExcursionControl.lean](https://github.com/Troyusrex2/Rule30PrizeKit/blob/0cbc49ef30888b32760def46ec31f954626192ff/research/agent-experiments/coordinator/20261026-return-eight-and-reader-bridge/work/root/ResetExcursionControl.lean),
SHA256 `e9cf39dc7e58b1b76971e6d0685756d323998e549d2fc57b7fadb76820e4bb1b`.
Read its complete theorem, the definitions of finite evolution/newest/reader,
and the complete importing PrizeSafetyBridge source. This review accepts the
finite counterexample; it does not claim a complete independent verification
of every automaton certificate in those imported modules.

## What the witness says

The two older-first rows, with a permanently white older boundary, are

```
a = 100001000000
b = 100001100000.
```

The parallel update is F(x)_j=x_j XOR(x_(j-1) OR x_(j-2)); the two missing
older cells are0. `newest` means the last cell of this fixed-length list.
Thus `take 3` refers to the oldest three cells, not the newest three. The
theorem includes all of the following concrete conclusions:

- Both initial oldest triples are100; both initial newest triples are000.
- Their newest-cell traces at times0 through7 are both00010100.
- At time6 their newest triples are both000.
- At time2, their second-newest cells, zero-based index10, differ.
- The author's pair-reader run on the initial zipped rows ends at state15.

For a direct hand check of the parent difference, the first two updated rows
are respectively

```
F(a)  = 111001110000       F(b)  = 111001011000
F²(a) = 100111001100       F²(b) = 100111100110.
```

The remaining hand substitution gives these useful scope checks:

| Time | a evolved | b evolved |
|---:|---|---|
| 3 | 111100111011 | 111100011101 |
| 4 | 100011100100 | 100011010010 |
| 5 | 111010011111 | 111010101111 |
| 6 | 100101110000 | 100101010000 |
| 7 | 111110001100 | 111110101100 |

Each row follows by the displayed local rule, rather than a new simulation.
The reader state is also transparent from its actual table: the first pair11
takes0 to3; the next00 takes3 to12. Equal00/11 pairs keep state12 until index6,
whose pair01 takes12 to15. State15 then remains15. Its rejection is not an
independently proved converse about all-time trace inequality.

This defeats the proposed reconstruction of the intermediate parent segment
from one finite newest-cell excursion and the returning white triple. Both
rows are genuine finite white-boundary starts. It does **not** exhibit equal
newest traces for all time, nor refute an all-time reader completeness claim.
The source comment says the traces subsequently separate, but that later
separation is not part of this theorem and was not needed or separately checked
here.

There is a stronger immediate scope guard: the common trace starts00. Both
rows are therefore unsafe. `PrizeSafetyBridge.safe_sink_separates` assumes
Safe(a) **and** ReturnComplete, where ReturnComplete is the still-unproved
global statement Safe(xs) implies F^8(xs)=xs. The finite witness meets neither
the safe-output situation nor an all-time equality premise. It must not be
reported as a counterexample to that conditional theorem or to ReturnComplete.

## Source and retained validation

Defining dependencies inspected include CedarSafetySoundness's literal
parallel `change`, F and evolution; CedarSafetySemantics's newest and Safe;
and Rule30ColumnReaderResearch's exact17-state table, next and run. The reader
accepts0,3,12,16, so its15 state here is rejected. These definitions, rather
than a claimed interpretation of an automaton state, carry the finite result.

The selected13 archive payloads match their235-entry manifest. Root source
metadata binds the exact ResetExcursionControl, PrizeSafetyBridge and reader
sources. Raw checker JSON equals the retained report:6 replayed constants,
5 declared constants and1 headline, with propext only and no new axioms.
The build log is empty; the check log has the known replay-API deprecation
warning. The author used official pin5473ffd075f63c9d626e63b8455805d4831b39ca
and unchanged checkerb882f252. No GPT replay or live portal tag is inferred.

The retained author guard reports1.6365645seconds, peak owned RSS724414464bytes,
exit0 and no guard stop. Its300wall/8GiB owned/2GiB system-available limits
and0.1second sampling do not establish aggregateCPU/output/disk/swap/thermal
enforcement. These are author-host measurements. The driver hashes its own
source and earlier compiled dependencies; this review did not recreate those
binaries or audit unrelated bridge certificates.

Packet `cited/gc2237-reset-review/review-manifest.json`, SHA256
`dbf2e115166013e7560a32bd0c66d5e2d31c4856d6bebf2e0014be7b1fa8bed4`,
contains15 payloads/78062bytes plus manifest, with verified raw-body uploads.

Record searched: GC2216–2218's finite-parent/branch-death limitations,
GC2232's exact finite eight-return theorem, GC2234's arbitrary-driver safety
equivalence, current kit932cf8dd and04:17:45Z portal/23PR index, and the exact
linked archive rather than an inferred keyword match. This is a cited existing
counterexample, not a new experiment or novelty claim.

Park one-excursion decoding. A reopening condition is an additional stated
parent observable or an all-time hypothesis that excludes this exact finite
pair. Do not rerun or enlarge its trace merely to see another collision.
