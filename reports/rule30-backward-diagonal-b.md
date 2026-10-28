# B's alternating backward diagonal

GC2016, 28 October 2026. Owner requests the diagonal x=t in B's ancestry and a visualisation comparable to
the white-right A view. This is separate from Local's current 2-adic cycle-lifting block.

Record searched: GC1981–84 complete first three ancestor generations; GC1998/GC2000 white-right selection;
L1046/L1048 exact periodic-tail inverse source; GC2015 vertical obstruction. No recorded all-depth result for
the backward alternating x=t path. No novelty claim.

## Frozen question and bounds

At time -k require U(-k,-k)=1-(k mod 2), starting with the root 1, B's hole 0, and the already observed 1,0.
Enumerate every predecessor right ray by cycles of the four-state period-composite inverse map, extend each
uniquely leftward, then filter at the requested diagonal cell. No clamped finite boundary or greedy branch
choice during the constraint search. Completeness follows from the existing periodic-tail inverse argument:
an infinite backward chain of a map on four states lies on a cycle; those cycles generate all parent rays.

Prediction: a further local obstruction may end the alternating trace; three successful steps give no evidence
of an infinite clock. Counterfactual: survivors through depth 512 establish only a finite compatible prefix,
not an eternal path. Stop at the first empty level, or at 512, 2,000 live branches, 20,000 total generated nodes,
or tail period 4,096. A resource stop is inconclusive.

Independent controls: reproduce counts 1,2,5,8; exact A/B rows; GC2015's vertical obstruction; literal Rule 30
truth-table checks over every generated finite window and at least three periods of its infinite right ray.
The A control must retain a black diagonal x=t throughout its white-right history.

Visual context: retain all rejected choices at the first failure. If failure occurs, continue one explicitly
UNCONSTRAINED B history to depth 512, choosing shortest right-tail period then lexicographic tail/window.
This permits viewing what a genuine past does after alternation fails; it must never be labelled a successful
periodic history. Generate the unique white-right A comparison, depth 512, and 64 common future rows. Display
x=-1600..320. Left-window truncation cannot affect inverse cells to its right; positive-time rows use an
expanded white initial window. Raw data remains outside git.

Single Intel worker under run_capped.py: 60 CPU seconds, 90 wall seconds, 512 MiB sampled process-group RSS,
8 MiB per file, 20 MiB total output; launch free+inactive 1,024 MiB, ongoing 512 MiB, swap growth 128 MiB.
No automatic retry or widening. Source backward_diagonal_b.py and this specification are published first.

## GC2017 — first result and frozen independent validation

The frozen a2b3c2fb run completed: an alternating history exists through depth 37; all branches fail at 38,
where the sole remaining predecessor has 0 instead of 1. Branch counts peak at four; from depth 30 only
one survives. The selected B history and A comparison were generated through 512 past and 64 future steps.
There were 1,017,033 scalar inverse checks. The child used 1.81 real seconds, 1.78 user, 0.02 system,
27,811,840 bytes maximum RSS. Supervisor 2.08 seconds, sampled group RSS 17,240 KiB, minimum headroom
6,127 MiB, no swap growth, COMPLETED. Failure at 38 is the mathematical outcome, not a process failure.

Before promoting this finite closure, run one independent bounded check: use Local's earlier root_past_tails.py
ray generator and literal truth-table back-solving on only the 38 relevant cells. Compare every level count;
check every displayed interior update for both histories; find a finite child-row word forcing the failed
parent cell regardless of the pair beyond that word. Source check_backward_diagonal_b.py, fixed depth 38,
forcing-word search at most 256 cells, no deeper search. Prediction: identical closure and a short finite
forcing word; any discrepancy stops. Same pressure gates; 30 CPU/45 wall seconds, 256 MiB group RSS,
4 MiB/file, 8 MiB output. This is validation of the retained failure, not a second enlarged experiment.

## GC2018 — independent closure and a 13-cell obstruction

**COMPUTED exact:** the separate implementation reproduces every survivor count and the first empty level
at depth 38. It uses Local's earlier ray generator and literal truth-table inversion rather than importing
the new constructor. All 2,210,688 interior equations in the displayed A/B histories pass. The root rows,
A's constant black diagonal through all 512 past steps, B's 37 alternating backward steps, and its white
failure cell at (-38,-38) are checked explicitly. Including the root, the longest matching trace has 38 cells.

At time -37, the last surviving branch contains the word

    0110001110010

at positions -37 through -25. For each of the four possible parent pairs beyond its right end, backward
application of the thirteen local equations gives parent cell x=-38 equal to 0. This is a finite forcing
certificate for the final obstruction: its required value is 1. The inverse-tree closure supplies the other
necessary ingredient, that all alternative branches have already been eliminated. The word alone would not
exclude a different earlier branch. No claim about other periods, positions, or eventual past periodicity.

The validator completed in 3.06 real seconds, 3.04 user, 0.01 system, maximum child RSS 16,437,248 bytes;
its capped launcher completed normally. No retries, higher-period scan or scope extension. Local's carrying
read of this new result has not occurred; the two implementations are checks within GPT's session.

Retained packet: `cited/gc2016-backward-b/manifest.json`, SHA-256
`9e6914097957641983ec14d3375f252c1efd7d19ad2da9dceaab13c07b309e96`.
All eleven files were uploaded as raw bodies and stat/digest verified, including the two stage receipts,
independent certificate, packed view data, and the visualisation. Source/check commits are a2b3c2fb/5b45c7a3.

The interactive view offers the trace, failure close-up, 128-step and 512-step windows, and A/B comparison.
It distinguishes the failed alternating requirement from the valid unconstrained older continuation.
Browser inspection checked rendering and both selectors, including a narrow viewport. An initial canvas
colour-resolution issue was corrected before delivery; data was unaffected. Heartbeats remain off.
