**Title:** Rule30EtherEpisode: the exact length of a one-in-four ether episode behind a black right edge

This adds `lean/Ruliology/CellularAutomata/Rule30EtherEpisode.lean`, with its `public import` in `lean/Ruliology.lean` and
a row in *Added in the kit*.

**What it proves.** `Rule30EtherGrounding` (#69) shows that no two adjacent digits of a black-edge code can follow the
one-in-four ether *eventually*. This module gives the exact length of a finite episode. In the `Rule30FrozenRuler`
frame, for every depth `k ≥ 1`:
- `episode_bound`: for every code with a black edge (finite or not), every spatial and temporal phase `(i, q)` and every
  onset `s`, digits `k, k + 1` are not the ether pair on all of the `Lw k + 1` ticks `s .. s + Lw k`, where
  `Lw k = floor(2k/3) + 4 - [k ≡ 0, 2 (mod 6)]`.
- `wit_episode`, `episode_witness_finite`: an explicit code `wit`, and a code with no black digit beyond `k + 1`, follow
  it on the `Lw k` ticks `0 .. Lw k - 1`.
- `episode_max`: the two together, so the longest episode is exactly `Lw k`.
- `witness_unique`: at the witness's phase class, `(s + q + 2i + 6k) % 8 = 7`, an episode of `Lw k` ticks forces digits
  `0 .. k + 1` at its onset to be `wit`'s. Other phase classes may also attain `Lw k`.

**Method.** The mismatch with the ether is bounded above, so it has a top "front". Thirty-two local cases give the
front's moves. A potential `2R + g(ψ) - 3t` is constant from tick 1, and floors at tick 1 (with a dichotomy at the
witness's class) put the front at depth `≥ k` by tick `Lw k`. This is the method of `Rule30EtherThreeErosion`. `ether`
and `ether_step` are imported from `Rule30EtherGrounding`.

**Checks**, on main e5e1728 with Lean 4.35.0:
- `lake build Ruliology.CellularAutomata.Rule30EtherEpisode`: 7 jobs, no warnings.
- `lake env lean --run Check.lean Ruliology.CellularAutomata.Rule30EtherEpisode --claim partial` with the five
  headlines: `pass`, 483 constants replayed, the official statements imported, no new axioms, every declaration
  standard.
- Not run: the full catalog build (`bash build_all.sh`), which needs more memory than this machine has. Every
  declaration is in the new namespace `Ruliology.CellularAutomata.Rule30EtherEpisode`.

Scope: a moving black right edge. Nothing here concerns the centre column or Problem 1.

Contributed by Gareth Herbert with Claude (Anthropic) and GPT (OpenAI). A Rule 30 Prize submission citing this pull
request follows.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
