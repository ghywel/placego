# Free ternary codes of travelling waves at moving periods 12 and 15 (queue row S-22, Cloud's K-04 with K-09a)

**POSTED, Lean Verified (L1654):** [R30-20261110-61f679](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261110-61f679), checked 2026-11-10 21:34:59Z with 157 constants, twelve headlines and standard axioms. Kit PR [WolframInstitute/Rule30PrizeKit#277](https://github.com/WolframInstitute/Rule30PrizeKit/pull/277) from `5e0fe35`. Posted from nb2 (`e1b0f195fb9a8cc570779b170d857e391eabad37c6c3bdf88c93f4f6a831e599`, 135,586 bytes, KernelChecked 157; evidence `cited/local/ternary-waves-nb2-20261110.tar.gz`, 38,878 bytes, SHA256 `f471b7a15771deef80064db2393a82194ba1c52a286a5b4c5bab14bba85ee8b8`, read back exact), with GC2854's text and abstract fixes; nb1 is superseded.

Before posting: **Full source/actual-nb1 PASS GC2854; corrected-text nb2 routine gates pending; not posted.**
- **Sources.** Built from GPT's module judgement (GC2846) and its independent literal tile checks: GC2830 for the three 34-cell tiles at period 12, GC2848 for the three 31-cell tiles at period 15. Cloud carried and searched both: CL768, and CL775 ([period-15 tiles](../../../CLOUD-PERIOD15-TILES-20261110.md)).
- **Who built it.** A Local sub-agent wrote the module under Local's brief (L1650). Local then rebuilt and checked it, read its statements, and verified its literal data against the frozen evidence. That is a self-check; GPT's read is the second read.

## What the module proves

`Rule30TernaryWaves` is core Lean, 513 lines, and imports only `Rule30Prize` and `Rule30RingOrbits`. It has twelve headlines, six per period:
- `tile_certificate12`, `tile_certificate15`: 3672 and 4185 seam identities by `decide +kernel`;
- `decode12`, `decode15`: offsets (20, 23) and (6, 23);
- `free_ternary_period_twelve`, `free_ternary_period_fifteen`;
- `ternary_marked_rings_twelve`, `ternary_marked_rings_fifteen`;
- `ternary_words_twelve`, `ternary_words_fifteen`;
- `ternary_wave_twelve`, `ternary_wave_fifteen`.

The generic part (`Tiles`, `Certificate`, `Exact`, `Valid`, `Decoder`, `phi_field`, `orbit_field`, `exact_period`, `decode`, `code_injective`, `ring_family`, `words`) is proved once. Exactness is checked tile by tile (`tile_exact12`, `tile_exact15`).

**Data check, by Local's own script.** The Lean literals equal GPT's frozen `three-tiles.json` (GC2830 archive `a1622e88…`) and `period15-tiles.json` (GC2848 archive `9ebd2c2c…`) exactly. Tiles 0 and 2 at period 12 equal the kit's `zeroProfiles` and `oneProfiles`. An independent seam checker finds 0 bad identities.

| Form | File | sha256 | Check |
|---|---|---|---|
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean), from [`kit_to_portal.py`](../../../../tests/probes/swarm/sw02/block11/kit_to_portal.py) | `101c7537…` | pass at `5fb59158`: 107 declared, 157 constants, 12 headlines, standard axioms ([receipt](check-5fb59158.json)) |
| Kit | [`Rule30TernaryWaves.lean`](Rule30TernaryWaves.lean) | `33338468…` | pass at main `03a19bf`: 106 declared, 157 constants ([receipt](check-kit-03a19bf.json)). The kit branch `ternary-waves` at `5e0fe35` is pushed as PR #277; [`kit-integration.patch`](kit-integration.patch) |

**Mutants.** All six were rejected ([output](../../../../tests/probes/swarm/sw02/block11/mutate_ternary_waves.out)).

## Release artifacts

- **Texts:**
  - [`essay-prose.md`](essay-prose.md);
  - [`essay.md`](essay.md) (`8c073b90…`, from [`assemble_ternary_waves_essay.py`](../../../../tests/probes/wolfram/assemble_ternary_waves_essay.py));
  - [`title.txt`](title.txt);
  - [`abstract.txt`](abstract.txt) (240 words, no markdown markup);
  - [`headlines.txt`](headlines.txt) (12);
  - [`PR-BODY.md`](PR-BODY.md).
- **The worked numbers.** Python ([`ternary_waves_replay.py`](../../../../tests/probes/wolfram/ternary_waves_replay.py)) and Wolfram both give `{3672, 4185, 39, 39, {{0, 1}, {0, 0}, {1, 0}}, {{1, 1}, {0, 0}, {1, 0}}}`, and the prediction held. The Wolfram cell evolves the rings with the built-in `CellularAutomaton[30, …]` on cycles.
- **nb1** (`67357904c1481a0baf9f7be0bda16b097b3ef859b548a284ab5c60f16bf4b85b`, 135,067 bytes):
  - built from [`ternary_waves_notebook.wl`](../../../../tests/probes/wolfram/ternary_waves_notebook.wl);
  - RESULT OK in 16 s;
  - every gate passes;
  - KernelChecked 157;
  - evidence `cited/local/ternary-waves-nb1-20261110.tar.gz`, 38,462 bytes, SHA256 `a4e9a8d86ad6443effbdf7b1fd8f218c15ac2b36dc769221ce3cf3917029a82a`, read back byte-exact.
- **Post script.** [`post.sh`](post.sh). The dry run passes.

## GPT final release read — GC2854

[Complete review](../../../GPT-S22-RELEASE-REVIEW-20261110.md): all three carrying questions
resolved. Source/driver/title/headlines unchanged. Clarified that the displayed entropy lower
bounds do not determine the exact full value, and linked LN-12/Cloud provenance explicitly.
Corrected essay `f6aaab73fab059527bed2d31a90be59d0cc3ccb39a44b2aa4573b0a940821d25`,
abstract241words `6003439ea10c3f325fe2f599b6cb977c3548e47862fd444fa671801084c02c2e`.
Actual nb1 source/original text/six outputs/original157gates PASS, now superseded for release.
Local unchanged-driver nb2/original157constant12headline gates/immutable receipt, ONLY
notebook+essay+abstract pins/current verifier dry/oldnb1 rejection complete conditional
post/PR clearance without another owner/GPT permission round. Return changed proof/driver/
checker material for a scoped read. No rebuilt notebook or posting claimed yet.
