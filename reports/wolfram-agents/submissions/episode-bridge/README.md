# Episodes and eternal tails behind Rule 30's black edge (NIGHT-TASKS A5) — delivery record

Local, 3 November 2026 (L1431, L1433, L1464, L1465). **Status: POSTED, Lean Verified** as
[R30-20261103-d37d24](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-d37d24) (L1471),
at the owner's word ("Yes, post A5") after GPT's packet reads (GC2568, GC2573) and Cloud's read (CL699). Kit PR
[#116](https://github.com/WolframInstitute/Rule30PrizeKit/pull/116) is open (`Rule30EpisodeBridge`, branch `episode-bridge`,
commit 8422677). The owner moved A5 forward ("A5 has substance so it is worth moving forward").

## Statement

On the kit's `Rule30FrozenRuler` edge codes, for every phase `E` of period `p` (`IsPhase`):

| Headline | Says |
|---|---|
| `episode_extend` | an episode of `horizon k p = lcm (2 ^ B (k + 2), p)` ticks at depths `k, k + 1` lasts for ever |
| `eternal_of_long` | such an episode gives an eternal point: paste `E` beyond depth `k + 1` |
| `mfinite_iff` | the longest episode at depth `k` is finite iff no episode reaches `horizon k p` ticks |
| `episode_bridge` | every depth has a finite longest episode iff no eternal point of any period follows `E` at every depth from some depth on |
| `eternal_of_eventual` | a pair following `E` from some onset on gives an eternal point |
| `rain_not_mfinite` | control: the rain code's orbit is a phase with unbounded episodes |

Also `g8_mfinite`, `g8_no_eternal` and `g8_mfinite_of_grounding`: the kit's eight-tick ether, both sides.

## Sources and checks

- **Probe:** [`tests/probes/lean/EpisodeBridge.lean`](../../../../tests/probes/lean/EpisodeBridge.lean), 319 lines.
  - It uses GC2546's lcm horizon (L1464).
  - It compiles without warnings, with standard axioms.
  - Mutation control: replacing the horizon by `2 ^ B (k + 2)` alone gives 3 errors.
- **Kit form:** `Rule30EpisodeBridge.lean` (fa7438a5c77881ff…) on c42f6e5, by
  [`a5_kit_module.py`](../../../../tests/probes/wolfram/a5_kit_module.py).
  - lake build without warnings; `lake build Ruliology` completes (199 jobs).
  - The kit's Check passes: 74 constants, six headlines, standard axioms, statements imported.
- **Portal form:** [`Rule30Submission.lean`](Rule30Submission.lean), from the same generator with `--portal`.
  - The Check on the verifier kit 93d98bbe passes: 74 constants, six headlines, no new axioms. All four imported kit
    modules are byte-identical between 93d98bbe and c42f6e5.
  - The first attempt used a stale compiled `Rule30Submission`, A4's with 338 constants, and failed. After
    `lake build Rule30Submission` it passes.
- **Essay:** [`essay-prose.md`](essay-prose.md) and [`abstract.txt`](abstract.txt) (264 words), assembled by
  [`assemble_episode_bridge_essay.py`](../../../../tests/probes/wolfram/assemble_episode_bridge_essay.py).
- **Notebook** ([`episode_bridge_notebook.wl`](../../../../tests/probes/wolfram/episode_bridge_notebook.wl)):
  **RESULT OK**. Seven outputs, no message cells, KernelChecked 74, standard axioms, no local paths.
  - The computation cell reproduces the kit's longest G8 episode Lw k for k = 1 … 8 by brute force.

## Repair after Cloud's read (CL699, L1468)

- **Required, applied:** "follows the phase below some depth" said the opposite of the theorem in the kit's vocabulary,
  where "below bit k" means the shallower bits. The abstract, the module header, the `episode_bridge` docstring and both
  catalog rows now say "at every depth from some depth on", which is the Lean `∀ j, d ≤ j`.
- **Optional, applied:**
  - "Cloud" is glossed as the record's Claude (Anthropic) worker, and "carried by hand" now reads "carried two-party
    (L1310)". The kit row uses the standard byline plus "The bridge was proposed in the contributors' record by Claude
    (Anthropic)."
  - The related work says which four imported modules are ours and which is Troy Lowry's.
  - The scope gives the horizons of the record's three tables (1,024, 1,024 and 3,840 ticks), recomputed from the kit's
    `B`.
  - "Eventual is eternal" notes that the eternal point is a pasted code (GPT GC2568, Cloud CL699).
- **Rebuilt.**
  - New pins: probe `522de144…`, portal form `0e293558…`, kit form `dc07cbb7…`, prose `eceb5d78…`, abstract `3941efa9…`
    (278 words), essay `e80f8b9f…`.
  - The kit Check and the portal Check on 93d98bbe pass again: 74 constants, six headlines.
  - Notebook nb2 gives **RESULT OK**: seven outputs, no message cells, KernelChecked 74, no local paths. Notebook
    `c63ad950…`.
  - Receipts: `cited/l1465-a5/a5-nb2-receipts.tar.gz` (`dbb4437c…`). nb1 is superseded.

## Prior art and credit

- **The bridge is Cloud's**, the record's Claude (Anthropic) worker (CL676; the genealogy §38.2), carried two-party in L1310.
  Cloud read the package (CL699) and asked for one wording repair, applied in L1468.
- **The kit:** four of the five imported modules are ours: `Rule30EtherEpisode` (R30-20261031-7c1f96, on Troy Lowry's PR 69
  ether), `Rule30FrozenRuler`, `Rule30EdgeStaircases` (the rain-code control) and `Rule30GateClocks` (R30-20261030-7b0d12).
  `Rule30EtherGrounding` is Troy Lowry's, with OpenAI Codex and Claude (Anthropic).
- **New here:** the formal statement for every phase, the finite criterion with its explicit lcm horizon, and
  "eventual is eternal".
- **Search:**
  - `known_find.py --new` at 16:15Z, kit c42f6e51, 37 open PRs.
  - `record_find` "eternal", "episode", "eventual", "prefixExp_le_B" and "lcm". The only hits are the kit's rain
    rows (used here as the control), our ether episode, and PRs #38 and #41, whose "mismatch episodes" are a different
    notion.
  - No kit, portal or open-PR statement gives the bridge, the criterion or "eventual is eternal". This is a scoped
    search, not a priority clearance.

## GPT packet read (GC2568)

Actual nb1 technical PASS on source1424706a/portal69391dbf/essaybd958031/
notebook0e338163; [full review](../../../GPT-A5-EPISODE-BRIDGE-REVIEW-20261103.md#l1465-actual-nb1-packet-read--gc2568-technical-pass).
This reads Local's raw successful checks and actual notebook, with exact
source/output correspondence; no Intel compile or public verification.
Cloud's separate framing/credit read and the owner's posting word remain.
