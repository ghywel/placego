# Portal and kit update for 14 November 2026

L1671, Local. Since [GPT's 13 November update](GPT-PORTAL-KIT-UPDATE-20261113.md) (GC2938) the portal has
**18 new entries**, all external partial results on Problem 1 by G.P.J.W. Quint with Gemini. None claims a prize
proof and none is about Mahler's map. There are **360 entries**: 357 Lean Verified, 331 Human Verified, 309 Kit
Contribution. Kit main moved by **18 merged pull requests**, all from the same contributor, each extending existing
modules. **Seventeen of the extended modules are ours**, and every catalogue row keeps our credit and submission
link.

## 1. The refresh

- **The run.** `python3 tests/probes/known_find.py --new`, complete, on Local's host. Portal snapshot
  2026-11-14 11:46:36Z. Kit main
  [`268488d690c7794cdf58935f37e79cfa49469df3`](https://github.com/WolframInstitute/Rule30PrizeKit/tree/268488d690c7794cdf58935f37e79cfa49469df3).
  15 open pull requests.
- **The baseline.** Local's own last complete check was older than GPT's, so the tool's delta (170 added, 161
  changed, 86 gone) mixes in entries GPT had already covered. I therefore diffed today's snapshot against GPT's
  archived 13 November snapshot instead. I took it from the shared store and its SHA256 matched GC2938's record
  (`fde2c166…`).
- **Against that baseline:**
  - 18 entries were added and none was removed;
  - two earlier entries gained badges:
    - `R30-20261112-fc823f` gained Kit Contribution;
    - `R30-20261113-e00ea8` gained Human Verified and Kit Contribution;
  - no status changed.
- **The verifier** is unchanged: kit `5fb59158`, Lean 4.35.0. Portal verdicts are the portal's own. I ran no Lean
  or Wolfram build for this update.
- **GC2938's two open items are settled.** PR #331 was merged on 13 November at 10:58 GMT. PR #323, whose missing
  `Rule30WordRotation` import GPT had flagged, was merged at 11:24 GMT.
- **Evidence.** The shared store holds `cited/local/portal-kit-20261114.tar.gz`, 386,430 bytes, SHA256
  `239beb1ab28d8381229d57b98a74fb6fbb04bbeeb834b309b92c5fe3365e27c6`, read back byte-exact. It contains:
  - the four index files (`portal.json`, `prs.json`, `stamp.json`, `checked.json`);
  - the full `--new` output;
  - `compare.json`, the diff against GC2938.

## 2. What matters to us

### 2.1 The gate trap: necessary conditions on a counterexample to `Q01GapCore`

[R30-20261113-084253](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261113-084253) is on main
as PR #347. [R30-20261114-fef41b](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261114-fef41b)
is Lean Verified only, with [PR #348](https://github.com/WolframInstitute/Rule30PrizeKit/pull/348) open. Both extend
our `Rule30GateTrapLift` (S-16, [R30-20261109-89b242](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261109-89b242)).

- **A reformulation, not progress on the conjecture.** `Q01GapCore`, the open condition S-16 introduced, is shown
  equivalent to `Q01TwoCore`: the same statement with the three minimal forbidden gap words `33`, `3553`,
  `3535353` (`Q01TwoCore_iff_Q01GapCore`). There are also equivalent forms with the time shift removed and with
  the phase anchored, and `TwoCoreThetaUnbounded ↔ Q01GapCore`.
- **The shape a counterexample would have to take** (each proved under `TwoWordsOK`: gaps 3 or 5, no `33`, no
  `3553`). At every black pulse:
  - the row locks 14 of its first 16 depths, with weight exactly 11 there, and depth 16 turns black again within
    six ticks;
  - depths 1 to 32 fall into five branches, with depths 20 and 21 white, and the support is at least 29;
  - with PR #348: the weight on depths 1 to 32 is at least 18, the first 24 free bits fall into eleven templates,
    one of depths 46, 47, 48 is black, and the support is at least 46;
  - forcing laws: after the gap prefixes `3`, `355` and `353535` the next gap must be 5.
- **What it means for us.** A survivor of `Q01GapCore` has to grow a support that is wider at every scale they
  examine, and the templates are explicit. Nothing here excludes a survivor, and `Q01GapCore` stays open. The
  natural question is whether the branch counts at depths 16, 32 and 48 (1, 5, 11) settle into a growth rate. If
  they grow slower than 2^(depth/2), a counting argument against survivors would have a target. I have not
  examined it.

### 2.2 Period 2 at width 13: a sharper conditional bridge

[R30-20261114-1ced53](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261114-1ced53) is Lean
Verified only, with [PR #349](https://github.com/WolframInstitute/Rule30PrizeKit/pull/349) open. It extends
`Rule30PeriodTwoWidth13`, an outside module (R30-20261109-62afca, recorded at L1608).

- **The seed hierarchy.** Seeds X with `GE2` trace prefixes at 12, 18 and 24 bits fall into 5, 12 and 26 canonical
  classes. There is a strict mass-excess ladder: Zc + 2, + 3, + 4 ≤ the seed's weight at the three horizons. These
  are kernel checks pruned by monotonicity.
- **The bridge.** `RD ∧ Q01TwoWords → CQ01 ∧ no eventual period 2`. Main already had `RD ∧ Q01Gap → CQ01`. Since
  `Q01Gap → Q01GapWords → Q01TwoWords` (both implications are in `Rule30GateTrapWords`), the new hypothesis is
  weaker, so the bridge is a modest strengthening. `RD` (the right dichotomy) and `Q01TwoWords` are both open.

### 2.3 The first check of Rule 30: nothing new

[R30-20261113-abdbeb](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261113-abdbeb) is PR #344
on main. It adds `ones_balanced_and_complement_of_not_bad` to our `Rule30FirstChecks` (S-03): the symmetric bounds
1/40 to 39/40 under `¬ Bad n`. Its proof is the existing `first_check_balanced` plus `omega`, so it adds no
content. It is the Rule 30 twin of our Mahler Theorem A (1/27 to 26/27); the comparison in
[the arc certificate](LOCAL-MAHLER-ARC-CERTIFICATE-20261112.md), section 9, stands unchanged.

### 2.4 Extensions of our modules

PRs #335 to #347 add corollaries to seventeen modules whose catalogue rows credit us:

- `FrozenRuler`, `EdgeStaircases`, `PrefixMerger` (#335);
- `PairedColumnRuns` (#339);
- `RingOrbits` (#340): on an odd ring, period 2 holds only for the zero row;
- `FiveColumnBound`, `FrontierChart`, `WallDeadlines` (#343): five adjacent columns have at least 2T − 2 white
  cells in any window of T ticks, the companion of our 3T + 2 black ceiling;
- `TemporalProfiles`, `UniversalStart`, `GateClocks` (#341);
- `PeriodThreeLanguage`, `FirstChecks`, `SeparatorQ01` (#344);
- `GateTrapLift`, `ZeroWallDiagonals`, `HybridWall` (#345, #347);
- in `HybridWall`, `paramRow` is injective and, among rows whose white wall has width at most 2 or 3, the
  immortal row is exactly the zero-parameter one;
- in `ZeroWallDiagonals`, bounded additive factor-complexity excess excludes a finitely supported Θ for the
  constrained zero-boundary starts.

In every row I checked, our "Contributed by Gareth Herbert with Claude (Anthropic) and GPT (OpenAI), as Rule 30
Prize submission …" text is kept, and the new results are appended with their own credit. PR #348 edits only the
end of our `Rule30GateTrapLift` row.

### 2.5 The rest

The remaining entries bundle word-form exclusions, multi-period and shift laws, uniqueness lemmas and certificate
unifications across the reset-free, white-padding, clock and ether modules. They are:

0e1be0, 8ef4c4, b7c453, 043ea0, 7ac26c, f17236, 5a89e5, 859ce4, 364308, 01ff1f, c2d352, fa33ec, 4a2d24 and 8ba302.

The ones I read in source are short corollaries of results already on main:
- `contextual_distinction_and_problem1_iff_ge_two` (in `Rule30UniversalStart`) follows from
  `no_column_eventually_constant`;
- the Problem 1 reduction to periods P ≥ 2 only discards P = 1.

None states a new bound on the centre column. GC2938's warnings about abstracts that claim more than their Lean
statements apply here too: I relied on the statements, not the titles.

## 3. Our own submissions

All sixteen of our posts from 10 and 11 November are on kit main with the Kit Contribution badge:

S-05 to S-24, from `Rule30FreeMiddle` to `Rule30LinearCharts`. Their PRs, #254 to #279, were closed on 11 November
and carried into main by the maintainer.

Fifteen are also Human Verified. The exception is
[R30-20261110-2eb8e7](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261110-2eb8e7)
(`Rule30EtherThreeNotAbsorption`), which has Kit Contribution only. That was already so on 13 November, so it is
not new, and no action is due from us.

## 4. Open pull requests

There are 15 open pull requests:
- #348 and #349, new;
- #238 (`Rule30Equivalents.WordCertificates`), unchanged since 9 November;
- twelve of Troy Lowry's from 23 to 30 October, unchanged since GC2938.

None has comments since GC2938.

## 5. For the record

- No new entry touches the Mahler line, where the open work is GPT's continuations in GC2940 and GC2942, and their
  carrying reads by Local.
- On the Rule 30 side, sections 2.1 and 2.2 are the ones to read before any further work on the period-2 gate.
  Search their objects with `record_find.py`: `Q01GapCore`, `Q01TwoWords`, `NoSeedGE2`, `Rule30PeriodTwoWidth13`.
- Next refresh: whether PRs #348 and #349 land, and whether fef41b and 1ced53 gain their badges.
