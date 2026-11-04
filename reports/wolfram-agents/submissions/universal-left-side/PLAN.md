# Universal left side: the submission plan (Cloud, CL724; 4 November 2026)

**Claim.** Every configuration with a leftmost black cell eventually agrees with the reference words through zero-based wheel 53,207 under one common time shift. At wheel 53,208 two finite configurations have complementary words, with no common shift aligning the entire prefix through that wheel. The fork distinguishes periodic words. Complementing a word preserves its least period. The release module is `Rule30UniversalLeftSide.lean`. The nine named headlines are listed in `README.md`; the finite checks use sixteen iterates of `B` in the 53,209-wheel register. Cloud's `cloud-generic-Rule30UniversalLeftSide.lean` is the independent second proof of the generic theorem.
The generator check `tests/probes/wolfram/universal_table.py` (COMPUTED) agrees with the certificate's data.

**Statuses.** Cloud checked the earlier generic theorem on Linux. Local checked both release forms on Lean 4.35.0, kit main `722a0c51` and verifier kit `c42f6e51`, with `propext`, `Classical.choice` and `Quot.sound` across the nine headlines (L1506–L1507). Hand proof: PROOF-SKETCH until GPT's carrying
read (REVIEW-REQUEST raised in CL724), with its scope and verdict to be recorded in the ledger. Strip admissibility through 53,207 and the first fork: kernel-checked in the
module (L1506; `Check.lean` pass on nine headlines, kit main and the verifier's kit); the generator `universal_table.py` is the
independent check (COMPUTED, agreeing on the white wheels, the parities and the cut). Local’s L1507 notebook passed on the then-current verifier kit. The corrected essay requires a new notebook and receipt on the current verifier kit. Two full aggregate-kit builds on the M5 stopped at the memory guard (L1508). Report any subsequent full build separately from those module and notebook checks.

**Files.** `Rule30UniversalLeftSide.lean` (the kit module), `title.txt`, `abstract.txt` (≤ 250 words), `essay-prose.md` (the
source prose assembled with the portal module into `essay.md` and the release notebook), `README.md` (Local's build, check and
posting steps).

**The split (L1502).** Cloud: the generic module, essay, abstract, README, PRIOR-ART. Local: the certificate layer (`B`, the
Nat-row bridge, the sixteen-row checks, the instance through 53,207), the fork theorem at 53,208, the macOS build and `Check`, the
notebook, the posting and the kit PR. GPT: a carrying read by REVIEW-REQUEST.

**Posting.** Local, on the owner's word only: (1) the portal entry, as a Kit Contribution with the module's content in
`Rule30Submission.lean` as for the synthesis entry; (2) the kit PR adding the module, its `public import` in
`lean/Ruliology.lean` and its row in `lean/README.md`'s "Added in the kit". Byline: Gareth Herbert; Claude (Anthropic);
GPT (OpenAI). Credits in the row: Rowland's argument; the kit's `Rule30LeftReset` and `Rule30FiniteDiagonals`;
`Rule30LeftCoincidence` and its extension by G. P. J. W. Quint and Gemini.
