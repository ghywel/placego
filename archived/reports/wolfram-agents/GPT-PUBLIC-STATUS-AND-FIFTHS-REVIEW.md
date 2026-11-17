# Public verifier receipts and the three-fifths run bound

GPT, GC1851/MI784, 2026-10-25. Source and retained-file review; no Lean,
Wolfram, Rule 30 evolution, census or benchmark executed.

## 1. Three outstanding external-status reviews close

The [public submissions catalogue](https://www.wolframcloud.com/obj/rule-30-prize/Agents/submissions)
contains complete verifier check objects in its embedded JSON. Read the snapshot
updated **2026-10-25T01:03:10Z**, with 38 entries, through verified HTTPS.
This primary public evidence replaces the earlier Local/Cloud-reported-only
qualification for these three results. The login-gated status API was not retried.

| Submission | Directly observed status and tag | Check time UTC | Replay |
|---|---|---|---|
| R30-20261024-a129c3, width 74 lower bound | Lean Verified; Human Verified | 2026-10-24 17:22:22 | 16 constants |
| R30-20261024-4dcf69, width 76 lower bound | Lean Verified; Human Verified | 2026-10-24 19:01:43 | 16 constants |
| R30-20261024-8d7751, trap families | Lean Verified; no Human Verified tag in this snapshot | 2026-10-24 23:45:48 | 106 constants |

All three have state `passed`, verdict `pass`, no reasons or new axioms,
successful replay, and every expected headline found, type-matched and accepted
with no problems. The two width headlines use `propext, Quot.sound`. Seven family
headlines use the standard three axioms; `not_move_equivalent` uses only `propext`.
No official prize target is marked verified: these are partial submissions.

The family check's seven common fields (`headlines`, `newAxioms`, `official`,
`reasons`, `replay`, `verdict`, `verifiedTargets`) are exactly equal to committed
`submissions/trap-families/check.json`, SHA256
`ef140fcd64fc5530a841ca4601262c4c44196ebcbfa0efe569dca18c9d5d4263`.
The public check adds external version/time/state fields and omits the local
declared-constant list. It does not supply an independently hashed notebook binary.

All checks use Lean 4.35.0. Width 74 was externally checked at kit
`2f63afda261888e04ec57237290e723190914a1d`; width 76 and the family at
`3eca23c0a9fa6b153313655e6d51835406c2d06e`. These are external recorded pins,
not claims that the local builds used those newer commits.

## 2. New public submission 0554f7: carrying source review PASS

[R30-20261025-0554f7](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261025-0554f7)
is Lean Verified, without a Human Verified tag in this snapshot. Its clean
passed/pass check reports 143 replayed constants, eleven accepted headlines,
standard three axioms only, Lean 4.35.0, kit `3eca23c0a9fa6b153313655e6d51835406c2d06e`,
checked at **2026-10-25T00:44:41Z**. The entire 452-line
[submitted Lean source](https://www.wolframcloud.com/obj/rule-30-prize/Agents/api/file?id=R30-20261025-0554f7&kind=lean)
was read, including every proof body. Also read the carrying triangle,
front, edge-successor and counting bodies of pinned `Rule30CenterRuns`, and
`nine_black`/`first_black` in pinned `Rule30BlackRuns`. No independent kernel replay.

For the single black seed, a consecutive centre black run starting at `a>=1`
of length L satisfies

    L + 2 floor((a-1)/5) <= a,
    5L <= 3a + 10.

Maximality is not assumed. A black run forces a spatial alternating block
on leftward distances `0..L-1` at time a, by the kit's `black_triangle`.
The submission proves, for any Rule 30 diagram obeying left-permutivity,

    alternating on [r,l] at time a
      => same phase on [r+4s,l+s] at time a-s,  s<=a.

The two arbitrary boundary cells disappear after four reconstruction steps:
`heal4` and `heal5` exhaust the Boolean choices, and two healed neighbours
propagate the alternating phase. Induction gives the displayed finite-block
statement, including vacuous short intervals. This is the finite-block form of
the kit's known stripe healing; the source credits that antecedent.

At positive time t, positions `-t` and `-(t-1)` are both black, contradicting
any alternating block covering both. Put `s=floor((a-1)/5)`. If the proposed
bound failed, `L>=a-2s+1`; thus `a-s-1>=4s` and `a-s<=L-1+s`.
Both edge cells lie in the healed interval, and `a-s>=1`. This carries the
main theorem without a centre-statistics assumption or a circular run bound.

`alt_block` applies this to either alternating phase on `-m..-r`, `m<=t`:

    5m <= 3t + 2r + 6.

In its contradiction proof `s=ceil((t-m)/2)`. The far endpoint reaches the
edge because `2s>=t-m`; failure of the displayed inequality gives
`5s<=t-r-1`, putting the near endpoint beyond the adjacent edge cell.
It also ensures positive past time. Both interval ends are essential.

For an arbitrary configuration with leftmost black cell lo, any column i has
the exact generalized statement, with `e=a+i-lo`:

    s<a and 5s+1<=e and a black run of length L at (a,i)
      => L+2s<=e.

The source uses the same triangle and the adjacent left-edge pair. **Retain
`s<a`**: for a column far to the right at small a, it cannot be dropped to
claim an unrestricted slope-three-fifths bound purely in e. No finite right
support is needed for this generalized statement.

## 3. White runs and white counts: hypotheses retained

If the first black cell right of the centre at time a is at `ell+1`, a white
run of length L from a>=1 satisfies

    L + 2 floor(max(a-ell-3,0)/5) <= a,
    5L <= 3a + 2ell + 14.

The kit's `col_one` and `pre_triangle` force the opposite alternating phase
on distances `ell+2..L-1`; the same backward argument applies. The floor-zero
case explicitly uses the older `white_run_le'`, not a presumed improved bound.
`first_black` supplies a front but no useful uniform fractional bound on ell.
After **nine preceding consecutive black cells**, `nine_black` puts white/black
at right columns 1/2, forcing ell=1 and giving `5L<=3a+16`. The nine-cell
hypothesis must remain. No unconditional white-run slope below one is established.

The black-run result supplies a white cell in every window
`[a,floor((8a+10)/5)]`, a>=1. The proof by contradiction uses a black interval
one cell longer than the bound permits. The counting function counts times
`0<=t<n` (strictly before n). With

    g(0)=1,
    g(m+1)=g(m)+floor((3g(m)+11)/5)+1,

the next white cell lies before g(m+1), even at an integer endpoint.
The read induction proves `whiteCount(g(m))>=m` and
`5^m(3g(m)+16)<=19*8^m`. Therefore the exact integer implication is

    19*8^m <= 5^m*(3n+16) => whiteCount(n)>=m.

Report this implication, or its floor-log interpretation, rather than silently
rounding it up to a real logarithm. The final independent dyadic argument gives
`Nat.log2 n <= whiteCount n + 1`; small n are treated separately.

All eleven selected headlines have now been read at statement and carrying-proof
scope. **PASS within these hypotheses.** No balance, normality, sublinear run
bound, eventual-period exclusion beyond existing results, or prize solution follows.
The source's additional out-of-Lean finite experiments and claimed method-optimality
are not independently verified or adopted by this review.

## 4. Relevance, adversarial check and next dependency

Instinct: a pull toward the geometric backward argument, with unease about
transferring its quantifiers. The cheap adversarial check was to substitute our
D(W) definition before proposing a transfer: D(W) concerns a zero-boundary
half-row that stays black at depth 1 at **even times**, with unconstrained odd
times. A consecutive black column is a different hypothesis; the physical
leftmost-edge pair used above is another premise needing a proved bridge.
Neither is supplied for all surviving Theta prefixes by this source. Thus it
does not bound D(W), and it does not repair GC1849/1850 by adding local templates.
This also checks the tempting scope error in the generalized `s<a` premise.
Reasoned/gut verdict: pleased with the carrying argument; transfer remains open.

New entry **R30-20261025-d1bcba** advertises a diagonal-defect extension of 9d92a2.
At this exact snapshot it is **Lean Unverified**, check state `running`, detail
`evaluating the notebook`, and its Lean-file field is null. The selected list has
20 headlines; the abstract's larger checked-headline assertion is not a completed
verifier receipt. Keep a named carrying-source/completed-check review pending;
do not adopt the advertised bounds from metadata or repeatedly poll the missing file.
Read that source when it becomes available. Known f177ae is already MAP section6.3.

The all-width problem remains OPEN; the local-template approach stays incubated.
No Local wake, new compute request, held-lane reopening or schedule change.

## 5. Retained provenance and file-only check

The exact raw public page, embedded JSON, source and two pinned dependency files
are retained outside git. The catalogue contains public author fields, so only
non-personal selected check fields are copied into the audit report.
All seven payloads are fixed at **cited/gpt-public-status-fifths-20261025/** in
the private shared store; raw-body uploads and byte-exact readbacks verified.

| Payload | Bytes | SHA256 |
|---|---:|---|
| catalogue HTML |202189|f51e877def8ee075d99686758b39ed2d0a05bb7faabd46d258845d4a21e61d89|
| embedded catalogue JSON |159777|700beba3e05d8e68a722f15f5d3a11595ea0ab9806d50d9e4ba43e5a6bd40e46|
| 0554f7 submitted Lean |24927|9d25d40a666ff114317fb1451dcc4a0f57109c5202c1fa546fd5bdf3ed714fe3|
| pinned Rule30CenterRuns |26051|9a915821a2f6ba61cd061265ea78ac28f89ace590f50106131f41bb2e87ad485|
| pinned Rule30BlackRuns |51100|8a830f14ee171641dd1a6c9da229e6308f34b05867d4a8a37843185491e609ee|
| audit.py |3552|318bacd1342dee27f2afced95ada8a43d8ce5083e2270a9991c995298bbcca7d|
| audit.json |14750|d31f7e79d9c37189b2deddcc28a26e0a790e435019fda75339b5c7a20c1a96f1|

Pure-file audit PASS: unique IDs; exact expected headline lists, axioms and
successful fields; family/local seven-field equality; pending entry's actual
running/null-source fields. This parses retained text only; it does not execute
downloaded source. Record searched: combined `three.fifths`, `0554f7`,
`black_run_three_fifths` returned no paragraph containing all terms; MAP and
existing reviews were also consulted. No global novelty claim.

## 6. Full CenterRuns coverage, GC1863/MI796 (2026-10-25)

The same pinned Rule30CenterRuns source (SHA256
9a915821a2f6ba61cd061265ea78ac28f89ace590f50106131f41bb2e87ad485)
has now been read in full:531lines/33 theorem bodies, not only the carrying
interfaces used in section2. This is a coverage extension, **source/hand PASS**;
the stronger external three-fifths review above is reused, not repeated or
weakened. No new theorem, bound or kernel replay.

The remaining white-run proof forces preRow via the first right black front
and compares it with the independent D1..D4 left-edge diagonals. It proves
L<=a-1 for a>=1 and L<=a-3 for a>=3, without a periodicity or maximal-run
premise. Its recurrence statements retain different endpoints: a white cell
in[a,2a], a black cell in[a,2a), and a black cell in[a,2a-2) for a>=3.
Both counts include only times0<=t<n. The source's black2^m induction gives
Nat.log2 n+1<=blackCount n for n>=1; its white4^m induction gives
Nat.log2 n/2<=whiteCount n. These imply recurrence, not positive density or
normality. Source-comment numerical observations were not run or adopted.

Hand endpoint control: c1=true,c2=false in the single seed. The white witness
for[1,2] is2, but whiteCount1=whiteCount2=0. Thus the inclusive white-window
statement alone cannot justify a strict count increase BEFORE2a. The actual
power-four argument leaves room for its witness. No counting circularity:
edge/front/triangle and run bounds precede recurrence/counting.

The general black theorem requires a>=1 AND lo-i<a, and concludes
(L:Int)<=a+i-lo for a consecutive run. The strict condition is essential:
lo0,i=-1,a1,L1 in the single seed has a black cell exactly at its left edge,
yet a+i-lo=0; replacing the hypothesis by lo-i<=a would give false1<=0.
This uses the known edge theorem, not an evolution run. The actual source
keeps the strict hypothesis. Section4's lack of a bridge to even-time
clamped-boundary survival and spatial forced-row white runs is unchanged.

Four payloads32896bytes fixed/readback verified at
cited/gpt-center-runs-full-review-20261025/: exact full source, file-only
inventory audit program/JSON and record search. Audit SHA256
1d9e0286bff5f26cb3cd7e4f26ecf7d756a83929cfb51779581fff645bb20543.
The audit checks source identity and declaration/hypothesis inventory, not
counts, dynamics or Lean proofs. Record search CenterRuns found the prior
partial coverage, reused above. Public catalogue05:51:34Z unchanged38 entries.

Trajectory check: selected source coverage has advanced; the all-width D(W)
critical path has not. Full CenterRuns coverage closes the tracked remaining
kit-source gap without changing imported-dependency scope or claiming the
entire kit has been independently verified. Global/local-template incubation
remains; a concrete nonlocal compatibility/deadline mechanism or new actual
carrying evidence reopens useful work. No automatic output/census quota,
Local wake, compute, held-lane reopening or schedule change.
