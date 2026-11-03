# Episodes and eternal tails behind Rule 30's black edge (NIGHT-TASKS A5) — delivery record

Local, 3 November 2026 (L1431, L1433, L1464, L1465). **Status: PREPARED, not posted.** Posting and the kit PR wait for
GPT's packet read and the owner's word. The owner moved A5 forward ("A5 has substance so it is worth moving forward").

## Statement

On the kit's `Rule30FrozenRuler` edge codes, for every phase `E` of period `p` (`IsPhase`):

| Headline | Says |
|---|---|
| `episode_extend` | an episode of `horizon k p = lcm (2 ^ B (k + 2), p)` ticks at depths `k, k + 1` lasts for ever |
| `eternal_of_long` | such an episode gives an eternal point: paste `E` beyond depth `k + 1` |
| `mfinite_iff` | the longest episode at depth `k` is finite iff no episode reaches `horizon k p` ticks |
| `episode_bridge` | every depth has a finite longest episode iff no eternal point of any period follows `E` |
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

## Prior art and credit

- **The bridge is Cloud's** (CL676; the genealogy §38.2), carried two-party in L1310.
- **The kit:** `Rule30EtherEpisode` (Lowry's PR 69 ether), `Rule30EtherGrounding`, `Rule30FrozenRuler`, and
  `Rule30GateClocks` (our R30-20261030-7b0d12).
- **New here:** the formal statement for every phase, the finite criterion with its explicit lcm horizon, and
  "eventual is eternal".
- **Search:**
  - `known_find.py --new` at 16:15Z, kit c42f6e51, 37 open PRs.
  - `record_find` "eternal", "episode", "eventual", "prefixExp_le_B" and "lcm". The only hits are the kit's rain
    rows (used here as the control), our ether episode, and PRs #38 and #41, whose "mismatch episodes" are a different
    notion.
  - No kit, portal or open-PR statement gives the bridge, the criterion or "eventual is eternal". This is a scoped
    search, not a priority clearance.
