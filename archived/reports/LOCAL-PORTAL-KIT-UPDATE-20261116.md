# Portal and kit update for 16 November 2026

L1674, Local. This update covers the period since [the 14 November update](LOCAL-PORTAL-KIT-UPDATE-20261114.md)
(L1671).
- **Portal.** Four new entries, all partial results that the portal verifies in Lean; none claims a prize, and
  none is about Mahler's map. Two earlier entries gained badges. There are **364 entries**: 361 Lean Verified,
  337 Human Verified, 312 Kit Contribution.
- **Kit main.** Three merges, one of them a new module.
- **Two new things matter to us.**
  - The kit now states `Q01Gap` as a statement about popcount, which is the companion of L1673's
    stratification by support.
  - A new contributor working with Claude Code proved the first upper bound in the kit's Problem 3 model: an
    explicit one-tape machine computes the centre column in time 21(n+1)².

## 1. The refresh

- **The run.** `python3 tests/probes/known_find.py --new`, complete, on Local's host. Portal snapshot
  2026-11-16 13:49:53Z; kit main
  [`8b397bde9afc97cfb7ad9ab27e71048736173b1e`](https://github.com/WolframInstitute/Rule30PrizeKit/tree/8b397bde9afc97cfb7ad9ab27e71048736173b1e);
  14 open pull requests.
- **The baseline** is Local's own complete check of 14 November (11:46:36Z), so this time the tool's delta is
  exact. I also diffed against the L1671 archive.
  - Added: 4 entries. Removed: none.
  - Changed: `R30-20261114-fef41b` and `R30-20261114-1ced53` each gained Human Verified and Kit Contribution.
  - No status changed.
- **The verifier** is unchanged: kit `5fb59158`, Lean 4.35.0. Portal verdicts are the portal's own. I ran no Lean
  or Wolfram build.
- **Kit main moved by three commits.**
  - #348 and #349 (G.P.J.W. Quint, 15 November 23:16 GMT) landed: the depth-48 gate-trap skeleton, and the
    width-13 GE2 hierarchy with the bridge `RD ∧ Q01TwoWords → CQ01`. Both pull requests were closed and
    carried into main.
  - #350 (Emerson Villafuerte, 16 November 06:10 GMT) adds the new module `Rule30ZeroCoastBridge`, 2,047 lines.
  - No other module was added or changed.
- **Evidence.** The shared store holds `cited/local/portal-kit-20261116.tar.gz`, 371,615 bytes, SHA256
  `f82af8428661ce688d1f584d3068436aab6b563e8f88a31a2fd18bae29b0da33`, read back byte-exact. It contains:
  - the four index files;
  - the full `--new` output;
  - the kit README patch for the period;
  - `compare.json`, the diff against L1671.

## 2. The new entries

### 2.1 `Q01Gap` as mass divergence: [R30-20261115-fdf6a3](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261115-fdf6a3)

Emerson Villafuerte with Codex and Antigravity. Lean Verified, Human Verified, Kit Contribution; on main as
`Rule30ZeroCoastBridge` (#350).

**The definitions.** A seed y (a finite left row, read as an integer under F) *survives to H* when its depth-1
trace for H ticks is accepted by the gap clock with resets 6 and 10. That is the `Q01Gap` language, gaps 3 or 5
in free steps, read from tick 0. Then:
- `NoMass M H`: no seed of popcount at most M survives to H;
- `MassDiverges`: for every M there is such an H.

**What is proved on main.** These are equivalences between open statements; the module says plainly that all of
them remain open.
- `MassDiverges ↔ FiniteSeedsTerminate`, the statement that every seed eventually fails the clock.
- `massDiverges_iff_Q01Gap`: `MassDiverges ↔ Q01Gap`.
- Consequently `massDiverges_of_Q01` and `CQ01Empty_of_massDiverges`.

**What stays in the submission.** A finite classification: the eight seeds of weight 38 cover the prefix box at
M = 37, K = 102, so `NoMass 37 102` and `NoMass 38 111` hold. There is also a strict-reset block with singleton
fibres, and a two-block extinction.

**Why it matters to us.** L1673 measured the same kind of survival stratified by *support*, for the thinner
`TwoWordsOK` and `TwoCoreOK` languages: the longest-lived row of support W lasts about W/(2 − h) free steps. This
module stratifies by *popcount*.
- The two are different coordinates on one survival table. A finite row of support W has popcount at most W, so
  a support law bounds survival by mass from below, but not from above.
- `NoMass 37 102` is a single exact rung of the mass table for the `Q01Gap` language, which L1673 did not
  enumerate. Running L1673's probe on that language would let the two tables be compared directly. That is a
  natural next measurement, not done here.

### 2.2 Problem 3: an explicit one-tape machine in quadratic time, [R30-20261115-043275](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261115-043275)

KDRonald3 with Claude, "Claude Code with Claude Fable 5.2". Lean Verified and Human Verified; not in the kit.

- **What it proves.** `exists_quadratic_machine`: in the kit's `Rule30Problem3.Machine` model there are M and C
  with `Computes M center (fun n => C*(n+1)^2)`. The witness is explicit: 9 tape symbols, 69 states, C = 21.
  The machine carries a binary counter and the Rule 30 row on two tracks and sweeps once per step.
- **What it is not.** It claims no lower bound, and Problem 3 asks for a linear lower bound. Its value is that
  the model now has a proved upper bound, so the one-tape cost lies between the conjectured n and 21(n+1)².
- **Our record.** Problem 3's formal statements (PRIZE-PROBLEMS.md, D4; RECORD-MAP, GC1282 and CL615) and CL765's
  remark that literal Problem 3 on unary input is Problem 1. We had no machine construction.

### 2.3 Recurrent windows: [R30-20261115-2d4add](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261115-2d4add)

KDRonald3 with Claude. Lean Verified and Human Verified; not in the kit.

- **What it proves.** For every configuration with a leftmost black cell, every column and every time, each of
  seven sets of three-column windows recurs: for example {001, 100} and {000, 011, 100}. So do a black pair, and
  a "low window" (column i white, and columns i+1 and i+2 not both black).
- **The method.** A window that avoided its set forever would trap a wider window (4 or 9 columns) in one
  strongly connected component of a finite graph. Every component either has a constant column or is a simple
  cycle, which contradicts Jen's theorem and `no_column_eventually_constant`.
- **What it does not do, as the authors state.** An alternating centre is compatible with all ten sets, so this
  gives nothing on period 2. It includes a barrier: a configuration with no eventually constant column in which
  columns 0 and 1 are never both white.
- **Our record.** Nothing equivalent. The method, a finite graph of wide windows with the components classified,
  is close to our trap and lock work (`Rule30SidewaysLocks`, `Rule30GateTrap`).

### 2.4 Width-13 retrodiction: [R30-20261116-18db54](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261116-18db54)

G.P.J.W. Quint with Gemini. Lean Verified and Human Verified; [PR #351](https://github.com/WolframInstitute/Rule30PrizeKit/pull/351)
open and uncommented.

It extends `Rule30PeriodTwoWidth13`:
- closed-form formulas for depths 4 to 9 under `GValid`;
- `ge2_shift_at_even_zero`: GE2 re-anchors at every even-time zero;
- the 24-bit seed classes recur at every such zero, with weight at least 9 and the mass excess `Zc + 4 ≤ wtH 24`.

These are necessary conditions on a hypothetical seed, in the same spirit as the gate-trap skeleton. Like that
skeleton (L1673), they are finite-depth statements. Whether their frontier persists is the same question,
untested here.

## 3. Our own work

- **Our sixteen posts** of 10 and 11 November are all on main with Kit Contribution. Fifteen are also Human
  Verified; the exception, `R30-20261110-2eb8e7` (the not-absorption result), is unchanged.
- **Our catalogue credit.** In #348's edit of our `Rule30GateTrapLift` row, "Contributed by Gareth Herbert with
  Claude (Anthropic) and GPT (OpenAI), as Rule 30 Prize submission R30-20261109-89b242" is kept, with Quint's
  additions appended.
- **No other row of ours changed.**

## 4. Open pull requests

There are 14:
- #351, new;
- #238 (AIOvernight), unchanged;
- twelve of Troy Lowry's from October, unchanged.

None has comments since L1671.

## 5. For the record

- **Nothing touches the Mahler line.**
- **On the Rule 30 side:** section 2.1 (popcount against support) and section 2.4 (one more finite-depth
  skeleton) bear on L1673; section 2.2 is the first Problem 3 upper bound in the kit's model.
- **Next refresh:** whether #351 lands, and whether 043275, 2d4add or 18db54 gain Kit Contribution.
