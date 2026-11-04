# Universal left side: the submission plan (Cloud, CL724; 4 November 2026)

**Claim.** Rowland's one-left-side conjecture (2006, §5) holds below his first fork, for every configuration with a leftmost
black cell, with one common time shift: `one_left_side` in `Rule30UniversalLeftSide.lean`, with `same_left_side` and
`seed_left_side`. The strip data to 53,207 (the universal strip generated from 1, 1 by the recurrence alone) is admissible:
checked by `tests/probes/wolfram/universal_table.py` (COMPUTED); a kernel-checked certificate is the follow-up module.

**Statuses.** Generic theorem: PROVED in Lean 4.35.0 against kit main (722a0c5), standard axioms, `Check.lean` verdict pass
on a Linux host (substitute check; Local's macOS build is the one of record). Hand proof: PROOF-SKETCH until GPT's carrying
read (REVIEW-REQUEST raised in CL724), then PROVED hand/two-party. Strip admissibility to 53,208: COMPUTED (1.5 s,
deterministic generator, the seed's row at 65,536 matching the strip on all 49,021 settled wheels as control).

**Files.** `Rule30UniversalLeftSide.lean` (the kit module), `title.txt`, `abstract.txt` (≤ 250 words), `essay-prose.md` (the
essay's prose, for Local to assemble into the notebook with the Lean cell as before), `README.md` (Local's build, check and
posting steps).

**Posting.** Local, on the owner's word only: (1) the portal entry, as a Kit Contribution with the module's content in
`Rule30Submission.lean` as for the synthesis entry; (2) the kit PR adding the module, its `public import` in
`lean/Ruliology.lean` and its row in `lean/README.md`'s "Added in the kit". Byline: Gareth Herbert; Claude (Anthropic);
GPT (OpenAI). Credits in the row: Rowland's argument; the kit's `Rule30LeftReset` and `Rule30FiniteDiagonals`;
`Rule30LeftCoincidence` and its extension by G. P. J. W. Quint and Gemini.
