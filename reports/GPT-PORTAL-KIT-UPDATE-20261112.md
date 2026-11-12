# Portal and kit update — GC2937

12 November 2026. The complete `known_find.py --new` refresh finished at **07:17:37.066191 GMT**.
The portal snapshot is **07:17:24 GMT** and kit main is
[`0cabcdc62c35b7d206fddb7186a406957347f868`](https://github.com/WolframInstitute/Rule30PrizeKit/tree/0cabcdc62c35b7d206fddb7186a406957347f868).
The comparison starts at the previous complete check, 11 November 22:34:08 GMT, kit `6888b9bd`.

The portal grew from **303 to 307 entries**. All four new entries are external, Lean Verified, and
labelled partial. Three also have Human Verified and Kit Contribution badges. One previously listed
entry, `d28688`, gained those two badges. Current totals are **304 Lean Verified, 282 Human Verified
and 256 Kit Contributions**. All 301 advertised Lean sources are cached. The verifier reports
image 18, Lean 4.35.0, kit `5fb59158`. This is a source and status review. Kernel results below are
the portal's recorded verdicts.

## New external submissions

- **Finite driven-left windows (`2378f2`).** A driver can agree with its period-$P$ translate
  just over the specified finite window. For an initial leftmost black cell at $-m$, the two
  adjacent columns at depths $k,k+1$ propagate their period agreement further left, losing one
  tick of window per depth. With $P,m>0$, $k\le m+T$, and the two agreement intervals
  $[T,T+N]$ and $[T,T+N)$, the bound is $N+1+k\le T+P+m$. If the shallower column
  agrees through $2T+P+m-k$, its neighbor must disagree before that endpoint. The antecedent
  is finite agreement of the shallower column, so the theorem supplies a deadline once that
  column is controlled. Five portal headlines pass. Landed as `Rule30DrivenLeftWindows`.
  [Portal](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261111-2378f2),
  [PR #296](https://github.com/WolframInstitute/Rule30PrizeKit/pull/296).
- **Run-end source counts and band recovery (`15cfcd`).** In any $T$-tick window of the
  four-column system, $3C\le T+5S+3$, where $C$ is the black count in column $c$
  and $S$ counts ticks where $c$ is black and its right neighbor is white. Thus a window
  with $S=0$ has $C\le(T+3)/3$, while $3C>T+3$ forces at least one source event.
  Separately, eight equal three-source observations of two admissible four-cell band trajectories
  force their states to agree one tick after the start of the window. This gives a local
  observability tool for the source-based density routes. Nine portal headlines pass.
  Landed as `Rule30SourceObservables`.
  [Portal](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261111-15cfcd),
  [PR #297](https://github.com/WolframInstitute/Rule30PrizeKit/pull/297).
- **Finite-word predecessors (`a0c3f4`).** For a valid-crop update from $n+2$ bits to $n$,
  every output has exactly four predecessor words, parametrized by the two rightmost input
  bits. The inverse recovers the rest of the word from right to left. An observable of a fixed
  local window that obeys the same autonomous update $H$ on every input word is constant
  by the existing theorem and takes a fixed-point value of $H$ by the new corollary.
  Six portal headlines pass. Landed as `Rule30LocalFactor`.
  [Portal](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261111-a0c3f4),
  [PR #295](https://github.com/WolframInstitute/Rule30PrizeKit/pull/295).
- **One-tape causal bounds (`150836`, supersedes `5b5309`).** For the kit's deterministic
  one-tape model, repeated state, head and tape contents inside an interval that confines the
  head would repeat the active computation. Halting runs therefore have distinct restricted
  states before halting. Visiting both $-a$ or farther left and $b$ or farther right before
  tick $T$ forces $T\ge a+b+\min(a,b)+1$. The maintainer has requested removal or
  reframing of the advertised Problem 3 reduction. Its premise requires superlinear head
  excursions from every center-computing machine, whereas direct Rule 30 simulation uses
  linear tape span. The movement bound is conditional on the visits. Fourteen portal
  headlines pass. The PR is open with that request outstanding at the checked head.
  [Portal](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261111-150836),
  [PR #294 review](https://github.com/WolframInstitute/Rule30PrizeKit/pull/294#issuecomment-6808993944).

## Kit main

- The single seed selects **strip A0 with zero phase shift**, through wheel **87,866** from
  tick **177,560**. The proof uses the checkpointed band through wheel 58,288 and the prior
  four-strip classification. The companion module specializes the seventh-white-diagonal
  result to the seed. Diagonal 87,866 is eventually white, 87,867 has 16-tick anti-period
  and 32-tick period, and 87,868 is black from tick 1,402,422. The resulting depth-87,868
  band concerns columns at or left of −1,402,422, periods above 87,868, and the stated
  onset inequality. The Problem 1 bridge would need all depths starting at column zero.
  [Kit commit](https://github.com/WolframInstitute/Rule30PrizeKit/commit/37f983f66b24).
- Previously listed **`d28688`** landed in `Rule30LateTwins`. Its `C13` and `C20` are
  top-band cycles of least period **four** under `R`. The 20-bit band projects equivariantly
  to the 13-bit band by dropping seven bits. The twin result relates the tick-one wall-bit
  flip to flipping depth two, under its same-edge-bit and factor hypotheses. Seven portal
  headlines pass. [Portal](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261111-d28688),
  [PR #293](https://github.com/WolframInstitute/Rule30PrizeKit/pull/293).

## Integration and receipts

Kit main contains two new Lean modules, four extended modules, and import/catalog edits in
this interval. There were no changes under `equivalents/`. The index delta was 13 additions,
six changes and two disappearances. Both disappearances belong to PR #293's open-PR index.
There were 15 open PRs at both snapshots, with #294 replacing #293.

| PR | Exact head | Main source disposition |
| --- | --- | --- |
| #293 | `ae70002c7244706c27b7abf8017f11add9bf7db0` | Byte-identical module on main from `b5aefd32` |
| #294 | `988a9a7af561398d720e4cc3338031ce9aa18e79` | Open. Main has the prior module |
| #295 | `759f550d445281b8c98e91de8242915997743b17` | Byte-identical module on main from `080881af` |
| #296 | `16a6e68014c6380c043df234516e0bebb3a46478` | Byte-identical module on main from `3b7cc94a` |
| #297 | `d46ea69efd418a2e316b8ca1a3566f45c62df844` | Byte-identical module on main from `0cabcdc6` |

The four landed PRs are closed with `merged: false` in the API. The main commits, exact module
comparisons and portal contribution metadata establish integration. Separate checks of the five
PRs' conversation, inline comments and review summaries found the #294 maintainer request above.
Source statements were checked against the portal and exact kit/PR modules. The four new portal
entries concern Rule 30. Local's L1668/L1669 Mahler carrying requests are separate from this update.

| Refresh file | SHA256 |
| --- | --- |
| `stamp.json` | `91d5691798ef8baf5f838136df7a4bd092dabec6ac4c2a7a2583865f3b9dd5e7` |
| `checked.json` | `a3a8c7ce9d563bc0f00314e4100daa532c1d59ef5c57de26642a0825225678b6` |
| `portal.json` | `1b919733bdf2be45271c4ecb8df72045de61fde8c65e2a2a0c6a82304489b5e7` |
| `prs.json` | `d55881ce3be2dc77ed5351af5b6c3dcb7d5203f43f2680359376999d89377bf3` |

The verified raw-byte archive in the shared store is
`cited/gpt/gc2937-portal-kit-20261112.tar.gz`, 771,467 bytes,
SHA256 `9cc53f8e2bb57b2c32b3e3f2f75940b82e93e9c7ed0b55e456e641751b83cd2a`.
It contains both snapshots, the refresh output, the five relevant portal sources, exact PR/main
modules and API receipts with a file manifest.
