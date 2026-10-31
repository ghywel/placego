# Run specification for the M(k) portal entry (L1267)

**Sources.**
- **Catalog module.** `lean/Rule30EtherEpisode.lean` v2, sha256
  `2ea831a9de66fefc63e621a218f49e53ed4230f41a15577bfa8e4b01c3c95c22`. GPT passed its source and statement fidelity
  (GC2336). It builds on the verifier's kit 842b756f (L1266).
- **Portal form.** `Rule30Submission.lean`, sha256 `e257396cbbd35cc3a8479f73207f366ce0bb24324bee59a25502249f7063d082`,
  993 lines. `tests/probes/wolfram/make_ether_episode_submission.py` (sha256 `1b2e0090b347ab80ca6012b6a628c9d428078aab948facc95429663e6458f632`) generates it mechanically:
  - plain imports of `Rule30Prize` (the official statements) and `Rule30FrozenRuler`;
  - `namespace Rule30Submission` with `open Ruliology.CellularAutomata`;
  - no `@[expose] public section` and no `#print axioms` lines;
  - public wording in the docstrings that cited record IDs.

  The script refuses any change to the 713 code lines and any internal reference left in the text.
- **Check.** `tests/probes/wolfram/check_ether_episode.sh` (sha256 `c7a9725aadf54bb7f28127929d99d0b53d4c13786ee96cb15a58d9a815bde9fb`), adapted from `check_ring_orbits.sh`. It
  pins both sources and the kit's unchanged `Check.lean` (`b882f2527a1d6e72…`).
  - **Part c.** The catalog module is compiled under the root `EtherEpisodeCert` and checked with five headlines.
    Its compiler output must be byte-identical to the reviewed axiom printout (46d74cbb…).
  - **Part s.** The portal form is compiled alone, with empty output required, and checked as `Rule30Submission`.
  - **Headlines.** `episode_max`, `episode_bound`, `wit_episode`, `episode_witness_finite` and `witness_unique`.
  - **Guards for each part.**
    - one checker JSON line, with a pass and replay ok;
    - the official import and no new axioms;
    - exactly the five headlines, all ok;
    - every declared constant standard.
- **Kit.** The verifier's commit, 842b756fc7d043995e14019fee2a82ab4ec83cf7. The portal's `api/environment`, read at
  about 21:30Z, names it with Lean 4.35.0. The check runs in a fresh detached worktree, with the closure of
  `Rule30FrozenRuler` built.

**Command.** From `<kit worktree>/lean`:
`run_capped.py --track-tree --max-procs 10 --out FRESH --cpu 300 --wall 600 --rss-mib 4096 --file-mib 64
--disk-mib 512 -- lake env sh check_ether_episode.sh CATALOG SUBMISSION CHECKER`.

**Prediction.** `ETHER_EPISODE_CHECK_PASS`, both parts, in under 60 s and under 1.5 GB per process. Each part has five
ok headlines, replay ok and no new axioms.

**Counterfactual.** Any stop, diagnostic, name clash in the new namespace, or guard failure ends the stage, and its
output is kept. One attempt, with no other job running.

**Record searched.** The packaging precedents are ring-orbits' RUN-SPEC (L1131), gate-clocks-nested (L1248) and
`HANDOVER-LOCAL.md`. The portal's instructions are `skill.md` 1.17.3, read at about 21:28Z (sha256 1e702976…). The
verifier's environment is `api/environment` (kit 842b756f, LeanLink 1.2.1, Wolfram 15.0).

## Results (written after the run)

**The portal form check: COMPLETED.** `ETHER_EPISODE_CHECK_PASS` at about 21:57Z on Local's M5, in a fresh worktree at
842b756f. Both parts passed:
- verdict `pass`, replay ok over 491 constants;
- the official statements imported, and no new axioms;
- the five headlines ok, and all 108 declared constants standard;
- the catalog's compiler output equals the reviewed printout, and the portal form's is empty.

Receipts (outside git): `out.txt` 0f7a47b1256ac2a1, `time_receipt.txt` e42ac9bce27ac03d, `launcher.json`
26b46a5ac6b755ad. The prediction held.

## The kit pull request form (L1268)

PR #69's `Rule30EtherGrounding` landed on kit main e5e1728 at about 21:21Z, byte-identical to the head we compared, so
the catalog form can import it.
- **The generator.** `tests/probes/wolfram/make_ether_episode_catalog.py` (sha256 `8144a6090a8328efd5c4f8d5eea140376d8b6d717a707d5d3307a3b815462933`) writes
  `kit-pr/Rule30EtherEpisode.lean` (sha256 `77a8e1048617d865ea4745041ef99fb1f30863f753e5f770fcab48c5a330c114`, 977
  lines).
  - It adds `public import Rule30EtherGrounding` and `open Rule30EtherGrounding (ether ether_step)`, and removes the
    module's copies of `ether` and `ether_step`: 12 code lines, the same names and statements.
  - It removes the `#print axioms` lines, and the docstrings carry no credits.
  - The other 701 code lines are unchanged, which the script checks.
- **The listing.** The branch also adds the `public import` in `lean/Ruliology.lean` and a row (`kit-pr/catalog-row.md`)
  at the top of *Added in the kit*.
- **The checks on e5e1728**, in a fresh worktree under run_capped, both COMPLETED:
  - `lake build Ruliology.CellularAutomata.Rule30EtherEpisode`: 7 jobs, no warnings, 7.2 s, 656 MB. `out.txt`
    f8a63c58d8b2f3e9.
  - `Check.lean --claim partial` with the five headlines: `pass`, 483 constants replayed, the official statements
    imported, no new axioms, all 104 declared constants standard. `out.txt` 5a8d131aa16bf1af.
  - The first checker attempt failed on my zsh call: the headline flags reached the checker as one argument, so there
    was no checker verdict. It is kept as a stopped run.
- **Not run:** the full catalog build.
- **Status.** The local branch `ether-episode` holds commit 8642073 on e5e1728, not pushed. Opening the PR needs the
  owner's word. `kit-pr/PR-DESCRIPTION.md` is the draft text.

## Docstring fixes and the pull request (L1269)

- **Docstring fixes.** After the essay review, three docstring fixes went into both generators: "beyond the edge"
  instead of "above", the frame credited to `Rule30FrozenRuler`, and no sentence about how the work was done. The
  portal form now also says PR #69 is absent only from the verifier's build. No code line changed.
- **The portal form is re-pinned.** Its new sha256 is `37733e44c5febb72abb0fd214a9839ca564f4f7ce55a4cbe566d42ee18cb584e`
  (992 lines). The pinned check passed again on 842b756f: `ETHER_EPISODE_CHECK_PASS`, `out.txt` cce9100fe35f7e3e.
- **The catalog form is regenerated and re-checked.** Its new sha256 is
  `615998d207a495dc2b15f69ff0ed73474303bd500868860dbcfe6d8a43b6883a`. It builds with no warnings and passes
  `Check.lean` on e5e1728 (483 constants, the same checker output 5a8d131aa16bf1af). The local commit was amended
  before any push; it is now dd1f09a.
- **The pull request is open.** At the owner's word, branch `ether-episode` (dd1f09a) was pushed to the owner's fork,
  and the pull request was opened as
  [WolframInstitute/Rule30PrizeKit#71](https://github.com/WolframInstitute/Rule30PrizeKit/pull/71) with the text of
  `kit-pr/PR-DESCRIPTION.md`. The kit runs no CI checks on pull requests.

## The release notebook (prediction before the run, L1270)

- **The essay is frozen.**
  - `essay-prose.md` is pinned in `assemble_ether_episode_essay.py`.
  - `essay.md` (sha256 `069b92f5ba454777c63af011d9d940d8fb09dcb2d977a1e119dea5bf9a24f281`) embeds the checked portal
    form (37733e44…) verbatim, as a multi-line string after `(*Iconize["Lean source"]*)`.
  - A test (L1269) showed that MarkdownToNotebook iconizes only a multi-line literal, not one line with escaped
    newlines. The first draft builds failed the icon check for that reason.
  - `abstract.txt`: 247 words, 1,720 characters.
- **The driver.** `tests/probes/wolfram/ether_episode_notebook.wl` (sha256 `1782147b21ffaf71865e4f96872abcf437e0a3adadf0fd72f3d3d8095f70d8aa`) runs through
  `universal_start_notebook_launch.py`, from the kit at the verifier's commit (842b756f, with the prebuilt packages
  linked). The run uses run_capped with CPU 1,500 s, wall 1,500 s, RSS 8,192 MiB and 24 processes.
- **Prediction.** `RESULT OK`, with these gates, in under 120 s and 2 GB:
  - 19 output cells, no message cells, no `$Failed`;
  - the source iconized;
  - the exhaustive table for k = 0..10, as in the draft;
  - the five axiom sets standard;
  - `KernelChecked` with 491 declarations, the count the official check replayed.
- **Counterfactual.** Any failed gate ends the stage, and the notebook and receipts are kept.

**Result (written after the run).** `RESULT OK`, COMPLETED in 44 s wall, peak RSS 1.34 GB, so the prediction held.
- **The build:** 34.4 s; 19 output cells, 0 message cells; the source in an icon.
- **The gates:** the table, the axiom sets, `KernelChecked` (491 declarations) and the LeanEnvironment are all as
  predicted.
- **The notebook** is `essay.nb`, sha256 `e9096c0bfa950fa6d535a8c4666b968a6a78454bbd5a6fedf34d482183ce6b03`, 328,951
  bytes. It is kept outside git, with `summary.json` (35548c2c0f57d63f…) and the 19 output digests.
- **Afterwards:** no kernel or lean process was left running. Three figures were exported as PNGs for the owner's
  reading.
