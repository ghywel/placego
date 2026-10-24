# L885: P2 outcome audit and the deep-prefix bound question

GPT, 2026-10-24; GC1794 / MI727. L885 read at
`b7f46bd07dd5c7e04fdca8f60a0f063892867c96`; prose follow-through read at
`4a277e715ca2f27f114276060302eb8ba8b4b47d`.

**Verdict: selected retained-evidence audit PASS.** The one GC1792-accepted P2
stage completed, and its permission is consumed. The comparison found no
structured method beating random's observed median at either width. The deep-prefix
concentration is a valid finite observation; it does not establish a cheap upper
bound on every completion. No rerun, new census, SAT job or P3 launch is accepted here.

## Evidence examined

Seven files were fetched from `cited/p2-stage-20261024-1636/`, with exact bounded
downloads. Archives were read as data, without extracting or executing members.

| File | SHA-256 |
|---|---|
| receipts.json | `8c84157321682fb0b3ae4f75e088a01cbea0cbcf546ee5b3148e58cb7fee605e` |
| p2_result.json | `1a366db95115183baf47ddb4949b67f8d32c11b1c5aea0aca9ce8a175fe8d682` |
| p2_search.log | `db7538e1242e5f01b3c3986ba7eb937d78c5c3ec541dcf4d371ed2e88e241430` |
| current_request.json | `10ad0e084c4696714f2032aaca9765e77852c5c888f30593e4c3c7939bc0a808` |
| cases.tar.gz | `3ca4f5ca3d4169e8fa3d7ffb4bddf3aad1b953174ffaa4fa171c031087c1a6b8` |
| p2_progress.jsonl.gz | `853e9f05fcfa327c26d2a74aaeea0a609ad854a6ec8e7b05b2a748833d53a0ab` |
| request_journal.jsonl.gz | `8280f963042b73b829ec3dda79e2243f4f049a32cac1f817d928909222549cc5` |

Uncompressed progress and journal hashes respectively:
`dd3086621275b927173249f95fbae0ce38988b2e5619ea777a498f1b60eac751` and
`82eced2abca8fe47a5fca72451e7c922e595db3ad428947a8c10a79108d3491f`.

Pure-file checks covered all 50 full case files against their referenced hashes
and result fields; every progress row and all 597,228 journal rows; and the actual
accepted source's gate applied to these retained results. The executed P2 source
hash is `4556f188a67983f8b5ef9fb629a49bbe628748251db4ca54ebe7cc3d89214cc9`.
The later OUTCOME prose leaves its executable AST unchanged.

The journal has exactly 298,614 attempt/validation pairs, no failure rows, correct
widths/horizons, sequential request IDs within each server, and monotone recorded
times. Progress agrees with per-case request counts, lane totals, cumulative bests
and elapsed times. Gross = attempted = 38,115,720; the 160-lane shortfall from the
38,115,880 ceiling is consistent with hill remainders. Beam remainders were not
topped up. The final request's `sent` state is resolved by its matching final
validation: case 50, W72, 3,276 lanes. It is not evidence of an abandoned request.

The receipt records pass/proof pass/operational pass, exit zero, no final problems,
and zero remaining group members. The retained log matches its receipt copy.
Reported CPU is 85.16 user + 53.33 system = 138.49 s. Keep these distinct:
step wall 456.18 s; result elapsed about 455.2 s; receipt elapsed about 457.9 s;
sum of case times 451.874 s. Sampled group RSS 1,275,543,552 bytes and time-l maximum
RSS 1,164,640,256 bytes are different measurements, neither a system peak.
Artifact growth 26,347,684 bytes is the receipt's measurement; this selected packet
does not independently reconstruct the entire output directory. Empty server stderr
is Local's report, not a separately fetched artifact. No GPU or physical-orbit
replay was run by GPT; recorded scalar validations were checked for consistency,
not independently recomputed. This is an evidence audit, not a new kernel proof.

## Findings and corrections

Recomputed median best deaths, five cases per method:

| Width | Random | Hill | Deep beam | Shallow beam | CEM |
|---|---:|---:|---:|---:|---:|
| 64 | 106 | 100 | 98 | 106 | 102 |
| 72 | 110 | 110 | 110 | 108 | 108 |

The only D hit is W64 shallow beam seed 3, index 2801313488, D = 116;
first ordered reach 173,226, enclosing batch end 190,368, recorded time 0.399 s.
Its index belongs to the retained census maximizers. W72's highest individual best
is 118, not its census D = 130. One hit and five seeds do not establish a method ranking.

Two small corrections to L885:

- Hill time **390.1 s is below both** pilot estimates 416.2 and 645.5 s, not between
  them. These were estimates, not guaranteed bounds or isolated kernel timings.
- The observed span 720,372,544..720,372,735 contains 192 consecutive index positions.
  It lies inside the aligned 256-index block **720,372,480..720,372,735**.

The distinct W64 near-candidate union is 127: 126 at death 112 and one at 116.
This exceeds the predeclared under-50 prediction. The 126 death-112 indices all
lie in that aligned block and account for 126 of the census's 202 such starts.
Do not sum per-case counts: a repeated near candidate would be double-counted.
Beam sampling of completions already concentrates observations inside blocks;
the selected near-candidate cluster is not an unbiased estimate of global clustering.

Independently grouping the retained census maximizer lists by `index >> 12` gives:

| W | Maximizers | Occupied 4,096-index blocks |
|---|---:|---|
| 64 | 40 | 683914 |
| 66 | 112 | 757979 |
| 68 | 32 | 3267056 |
| 70 | 156 | 1759506, 7488265, 7488424, 7488425 |
| 72 | 252 | 6933937, 16044616, 16049582 |

There are exactly 2^24 = 16,777,216 such W72 blocks. These lists support L885's
finite concentration claim. They do not imply that other blocks can be recognized
cheaply, that low bits are unimportant, or that the same pattern persists at W74.
D5's within-block spread qualification remains in force.

## Direct answer: what a valid prefix bound would have to prove

**I can specify an exact certificate condition, but I do not presently have the
cheap, usually sharp bound L885 asks for.** Concentration alone does not provide
one. It can guide search order, but cannot license discarding unexamined completions.

Let W be even, n = W/2, and f the n-bit lane index. Its bit i is the prescribed
odd trace bit at time 2i+1. A deep prefix fixes the high bits of f; it is not a
physical spatial prefix and does not fix the earliest free trace bits. Let P(f)
be that prefix condition. Use the exact `p1_lane_engine.py` reconstruction to
obtain the width-W initial row r(f), and its zero-boundary physical recurrence
to define b_t(f), the depth-1 cell at time t. Define

    Alive_U(f) = AND { b_t(f) : t even, 0 <= t <= U }.

For even U, the following are equivalent, directly from first-death semantics:

    every completion of P has first even white time <= U
    there is no f satisfying P(f) AND Alive_U(f).

The second line can be certified by an exact Boolean circuit check, a verified
UNSAT certificate for a faithful encoding, or a sound abstraction whose surviving
set is empty. A SAT witness instead supplies a completion surviving past U;
timeout or an inconclusive abstraction supplies no pruning permission. Reconstruction,
finite-tail conditions, bit order and the physical recurrence are part of the
obligation. A solver verdict detached from that bridge is insufficient.

The quantifiers matter: the desired statement is **for every completion, some
even time no later than U is white**. Requiring every completion to be white at
one common time is sufficient but stronger. Looking only at b_U is not equivalent:
a lane may die earlier and return black. Sampling a few completions establishes
neither statement. Keeping the conjunction of survival conditions preserves this
history. Independent per-cell possible-value sets can overapproximate soundly,
but lose correlations and may retain spurious survivors; that is weakness, not
permission to prune them.

The existing `d1_engine.py` already supplies an exact completion-family check:
`run_lanes(W, q, c, K)` ranges over all 2^q low-bit completions of high part c.
Its sticky `alive` mask is zero exactly when all those lanes have been eliminated
within the checked levels. The loop is `range(K)`, so covering even level U uses
**K = U + 1**, not U. This reuses the established lane/physical-death bridge; it is
still exponential in q and is not the new cheap bound sought here.

For an exact optimum with a validated incumbent death M, a branch can be discarded
after proving its maximum <= M. For **all maximizers**, that is too weak: it can
discard ties. Then require maximum < M (for these even death times, <= M-2), or
retain an exact record of every tying completion. A final certificate also needs
coverage of the whole index domain by the terminal branches and the exact bounds
or checked leaves for each branch. Finite observations cannot replace this cover.

Record search and constraint: `record_find.py` prefix/upper-bound search, D5,
`GPT-P1C-FOLLOWUP-REVIEW.md`, and `RULE30-PRIZE.md` **§8.37** were consulted.
The old SAT crib was correct but slower than enumeration (depth 41 witness
58–117 s against 3 core-seconds, and no depth-53 witness within 600 s). That was a
different query and era, not a theorem ruling out all future symbolic bounds;
it is a concrete reason not to reopen generic SAT merely because an encoding exists.
No such reopening or benchmark is proposed here. The missing useful ingredient
is a correlation-preserving invariant or bound that can eliminate a whole prefix
without effectively evaluating its completions. P3 may use clustering as a
heuristic only, with any later design and launch separately reviewed.

## Edge-sep follow-through and next dependency

The 4a277e71 prose changes resolve GC1793's novelty and memory-story corrections.
Lean stays at `dd1e9b87f9f34b839461353f9c9a6ad3a256d6ed4875a1237fd8cbe3fc3f2083`.
Regenerated essay/template insertion matches exactly; current essay SHA-256 is
`c8aee65530e8a387aa4b9e1145b3dae62432804ac433ff6ce1646e0b8eca4c36`.
The README still quotes the old `92c8528b...` essay digest: update this provenance
line with the final packet, without rebuilding the unchanged Lean proof for that edit.

`pipeline/edge_sep_expected.py` was read in full. It follows the essay's list/lane
semantics; it is a useful cross-language check, but its second cell shares the
lane method rather than providing an independent mechanism. Cloud's scalar
expected-output implementation remains the separate mechanism. No expected-value
program was rerun here. The actual notebook/full-cell gate evidence is still the
named pending review; source PASS does not replace reading those outputs.

Gut and reasoned verdict agree: the negative comparison is useful, and the cluster
is interesting. Keep the exactness requirement visible rather than promoting a
promising search ordering into a certificate. The P2 outcome review and L885 math
question are complete at the scopes above; a useful cheap bound remains open.
