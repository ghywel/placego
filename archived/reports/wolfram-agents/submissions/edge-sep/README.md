# Submission edge-sep (Cloud's module, 2026-10-24; SUBMITTED by Local 2026-10-24 17:04 BST as R30-20261024-991a71): exact edge deadlines for three edge pairs

Three exact negative-edge cases of the kit's `EdgeObservable` conjecture (`Rule30TraceEdge`, added after cc1e0e0), with exact
deadlines: two configurations with leftmost black cells at -2 and -1 have center columns that differ by time 8; at -4
and -3 by time 13; at -3 and -2 by time 14; each attained by an explicit pair. Every configuration with those edges,
finite or not. Design: GPT's (GC1787, GPT-CL620-SATURATION-REVIEW.md: locality bridge, disjoint signature sets, attaining
witnesses, R = m); the light-cone saturation argument and the finite searches E1, E2, E2b (CL618 to CL620).

- `Rule30Submission.lean`: the module (1,001 lines, 50397 bytes, no double quote or backslash; SHA256 `dd1e9b87f9f34b839461353f9c9a6ad3a256d6ed4875a1237fd8cbe3fc3f2083`).
  Imports `Rule30PrizeKit`, `Rule30ZeroBoundaryBarriers` (`evol_local_le`), `Rule30ZeroBoundaryLanes` (`pat`, `pat_spec`,
  `pack`). Sections: 1 forcing; 2 bitwise rule 30 on lane words (`stepW`, `stepL`, specs); 3 window configurations `cfg`
  and the lane invariant (`laneInv_step`, `iter`); 4 initial lane words (`initWords`, `laneCode`, `laneInv_init`); 5 the
  center words (`centers`, `centers_spec`); 6 signature sets (`memb`, `sigSet` accumulator-passing, `sigSet_testBit`,
  `sigSet_range`); 7 soundness (`HasLeftEdge`, `sig`, `laneOf`, `cfg_laneOf`, `center_eq_lane`, `memb_block`); 8 blocks of
  256 values (`partSet`, `BlocksDisjoint`, `separationB`); 9 the instances: 2 + 64 + 128 = 194 block theorems
  `d8_k`, `d13_k`, `d14_k` by `decide +kernel`, `sep_8`, `sep_13`, `sep_14`; 10 attainment (`witCheck`, `attained`,
  `wit8/13/14`, `attained_8/13/14`).
- `check.json`: the kit's `Check.lean`: verdict `pass`, **583 constants replayed**, eight headlines (`sep_8`, `sep_13`,
  `sep_14`, `attained_8`, `attained_13`, `attained_14`, `separationB`, `centers_spec`) on `propext`, `Classical.choice`,
  `Quot.sound` only, no new axioms. On Cloud's machine: `lake env lean` 206 s, `lake build` 11 min wall (3 min CPU),
  the checker's replay 170 s. At the verifier's half speed the replay alone is near six minutes: the maintainer path
  applies, as for submission 11.
- `essay-template.md` + `assemble.py` -> `essay.md` (SHA256 `c8aee65530e8a387aa4b9e1145b3dae62432804ac433ff6ce1646e0b8eca4c36` after GC1793's two prose repairs;
  it was `92c8528b...` at GPT's source read); `abstract.md` (247 words after the repair, four parts, ASCII outside the math); `expected_numbers.py` (independent scalar Python, below).

## Expected outputs of the essay's cells (`expected_numbers.py`)

- Attaining pairs cell: `{{-2, -1, {0,1,0,0,1,0,0,1,0}, {0,1,0,0,1,0,0,1,1}, 8}, {-4, -3, {1,1,1,0,1,0,0,0,1,0,0,0,0,1}, {1,1,1,0,1,0,0,0,1,0,0,0,0,0}, 13}, {-3, -2, {0,1,1,1,0,1,0,0,0,1,0,0,0,0,1}, {0,1,1,1,0,1,0,0,0,1,0,0,0,0,0}, 14}}`.
- Lanes cell (the saturation): `{{8, 8, 8}, 13, 14}`.
- Lean cells: the three `sep` type forms and `HasLeftEdge`; `attained_8`, `separationB`, `centers_spec`, `d14_0`; `Axioms`
  the three standard ones; `CallGraph` depth 1 of `sep_8`; `KernelCheck` Success.

## The lanes of the witnesses

Edges (-2, -1): codes 89 and 137 on the windows, lanes 44 and 68 (`wit8`). Edges (-4, -3): codes 183 and 587, lanes 91 and
293 (`wit13`). Edges (-3, -2): codes 17 and 67, lanes 8 and 33 (`wit14`). The lane of a window filling with code
`2 l + 1` is `l`; the kernel verified each pair agrees at times below `m` and differs at `m`.

## Kernel design notes

A single loop over all `2^(m+1)` signature values ran out of memory at `m = 13` (12 GB after ten minutes; reported by Cloud in CL622, not a retained artifact): the kernel's
whnf cache keeps every intermediate word for the lifetime of a declaration. Blocks of 256 values are one declaration each
(about one second apiece); the center words are forced to literals (`forceL`) before each loop; `sigSet` is
accumulator-passing so the kernel runs it as a loop, after a first version with a nested fold hit the kernel's recursion
depth at 16,384 iterations.

## Status

**SUBMITTED** 2026-10-24 17:04 BST on the owner's standing permission: **R30-20261024-991a71**, problem 1, claim partial, the eight
headlines above, status at submission Lean Unverified (queued for the verifier). GPT's source review GC1793: PASS, with the two prose
repairs made by Local in commit 4a277e71. The M5 pipeline (L886):
- the kit's checker on the M5 (kit copy cc1e0e0): `lake build Rule30Submission` 65.5 s, maximum resident set 4,061,773,824 bytes;
  `Check.lean` 54.2 s, 3,903,848,448 bytes; verdict pass, 583 constants replayed; the parsed JSON equals Cloud's `check.json` in
  every field (the files differ only in formatting);
- the notebook (`build_sub.wl` revision 3): 111.8 s, 333,142 bytes, nine output cells;
- the full-cell gate (`pipeline/nb_gate_edgesep.py`): PASS; cells 1, 2, 3, 5, 6 and 7 exact, cell 4's counts bound to the checker
  (the summary omits the 18 compiler-generated `match_` auxiliaries the checker lists), cell 8 the call graph of `sep_8`, cell 9
  Success with 583 declarations in every displayed copy; its 16 negative controls pass;
- retained in the shared store at `cited/edge-sep-submission/` (the nine cells, the checker JSON, the gate's outputs, the notebook).
The checker's 3.9 GB resident set lies inside the band where the verifier's sandbox has both passed and failed submissions, so a
maintainer rerun may be needed, as CL622 anticipated.
