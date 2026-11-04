# Universal left side: the submission plan (Cloud, CL724; 4 November 2026)

**Claim (two-sided, L1503).** Rowland's one-left-side conjecture (2006, §5) holds through wheel 53,207 for every configuration
with a leftmost black cell, with one common time shift (`universal_left_side`), and the first fork at 53,208 is realized by two
finite rows with no shift relating them (`first_fork`). File of record `certificate-draft.lean` (Local): `universal_of_strip`,
`universal_left_side`, `one_left_side`, `seed_left_side`, `fork_dichotomy`, `first_fork`, the parity theorems, kernel-checked on
sixteen rows of `B`. Cloud's `cloud-generic-Rule30UniversalLeftSide.lean` is the independent second proof of the generic theorem.
The generator check `tests/probes/wolfram/universal_table.py` (COMPUTED) agrees with the certificate's data.

**Statuses.** Generic theorem: PROVED in Lean 4.35.0 against kit main (722a0c5), axioms propext, Classical.choice, Quot.sound, `Check.lean` verdict pass
on a Linux host (substitute check; Local's macOS build is the one of record). Hand proof: PROOF-SKETCH until GPT's carrying
read (REVIEW-REQUEST raised in CL724), then PROVED hand/two-party. Strip admissibility to 53,208: COMPUTED (1.5 s,
deterministic generator, the seed's row at 65,536 matching the strip on all 49,021 settled wheels as control).

**Files.** `Rule30UniversalLeftSide.lean` (the kit module), `title.txt`, `abstract.txt` (≤ 250 words), `essay-prose.md` (the
essay's prose, for Local to assemble into the notebook with the Lean cell as before), `README.md` (Local's build, check and
posting steps).

**The split (L1502).** Cloud: the generic module, essay, abstract, README, PRIOR-ART. Local: the certificate layer (`B`, the
Nat-row bridge, the sixteen-row checks, the instance through 53,207), the fork theorem at 53,208, the macOS build and `Check`, the
notebook, the posting and the kit PR. GPT: a carrying read by REVIEW-REQUEST.

**Posting.** Local, on the owner's word only: (1) the portal entry, as a Kit Contribution with the module's content in
`Rule30Submission.lean` as for the synthesis entry; (2) the kit PR adding the module, its `public import` in
`lean/Ruliology.lean` and its row in `lean/README.md`'s "Added in the kit". Byline: Gareth Herbert; Claude (Anthropic);
GPT (OpenAI). Credits in the row: Rowland's argument; the kit's `Rule30LeftReset` and `Rule30FiniteDiagonals`;
`Rule30LeftCoincidence` and its extension by G. P. J. W. Quint and Gemini.
