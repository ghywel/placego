# Unrestricted tail closing fails on the constrained class (queue row S-23, Cloud's K-08)

**POSTED, Lean Verified (L1656):** [R30-20261110-497a64](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261110-497a64), checked 2026-11-10 22:03:25Z with 82 constants, sixteen headlines and standard axioms. Kit PR [WolframInstitute/Rule30PrizeKit#278](https://github.com/WolframInstitute/Rule30PrizeKit/pull/278) from `05ba1a8`. Posted from nb2 (`7e6029bcd8fc33f8e6c1b8f694dcd2d8302a69f0281f837ac92ebf71ef9728b0`, 94,076 bytes, KernelChecked 82; evidence `cited/local/unrestricted-closing-nb2-20261110.tar.gz`, 29,890 bytes, SHA256 `fe227eb601068c28510cefa9b4b2c2a46d2553f928332ca78abd2a091b18f51a`, read back exact). The GC2860 abstract wrote the free words with three-dot ellipses, which the notebook converter rewrites, so the Abstract gate failed; the posted abstract (`abstract.txt`, 223 words) spells them as 10 repeated, 00 followed by 10 repeated, and 01 repeated, with the essay reassembled from it. nb1 is superseded.

Before posting: **Complete source/actual-nb1 PASS GC2860; routine corrected-text nb2 gates next; not posted.** [Full review](../../../GPT-S23-RELEASE-REVIEW-20261110.md): all three carrying questions resolved. Proof/source/headlines/driver unchanged; title now accurately says eventually periodic, exact free words and guarded context sharpened. Local unchanged-driver nb2/original82constant16headline gates/immutable receipt, ONLY notebook+title+abstract+essay pins/current verifier dry/oldnb1 rejection complete conditional posting/PR clearance under standing consent.
- **Sources.** Built from LN-03.1 as Cloud computed and carried it (CL770 §11.3; [triage](../../../CLOUD-SW02-CARRY-TRIAGE-20261110.md) §9.1), and from GPT's comparison with open PR #52 ([GC2853](../../../GPT-K08-PR52-COMPARISON-20261110.md)), whose parity-translated mismatch Local carried (L1654).
- **Who built it.** A Local sub-agent wrote the module under Local's brief. Local then rebuilt and checked it and read its statements. That is a self-check; GPT's read is the second read.

## What the module proves

`Rule30UnrestrictedClosing` is core Lean, 258 lines, and imports only `Rule30Prize` and `Rule30ZeroBoundary`. It has sixteen headlines:
- `two_A`, `two_B`, `two_C`, `two_cycle`;
- `inX_A`, `inX_B`, `inX_C`;
- `free_A`, `free_B`, `free_C`;
- `theta_A`, `theta_B`, `theta_C`;
- `differ_AB`, `differ_one_tick`;
- `not_unrestricted_closing`.

The exact mismatch set, the nine residues modulo 14 plus depth 2, is COMPUTED, not formalised. The module proves the subsequence `14 q + 3`.

| Form | File | sha256 | Check |
|---|---|---|---|
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean), from [`kit_to_portal.py`](../../../../tests/probes/swarm/sw02/block11/kit_to_portal.py) | `76cc57bd…` | pass at `5fb59158`: 37 declared, 82 constants, 16 headlines, standard axioms ([receipt](check-5fb59158.json)) |
| Kit | [`Rule30UnrestrictedClosing.lean`](Rule30UnrestrictedClosing.lean) | `fc6a8796…` | pass at main `03a19bf`: 37 declared, 82 constants ([receipt](check-kit-03a19bf.json)). The kit branch `unrestricted-closing` at `05ba1a8` is pushed as PR #278; [`kit-integration.patch`](kit-integration.patch) |

**Mutants.** All six were rejected ([output](../../../../tests/probes/swarm/sw02/block11/mutate_unrestricted_closing.out)).

## Release artifacts

- **Texts:**
  - [`essay-prose.md`](essay-prose.md);
  - [`essay.md`](essay.md) (`c0848717…`, corrected GC2860, from [`assemble_unrestricted_closing_essay.py`](../../../../tests/probes/wolfram/assemble_unrestricted_closing_essay.py));
  - [`title.txt`](title.txt);
  - [`abstract.txt`](abstract.txt) (217 words, no markdown markup);
  - [`headlines.txt`](headlines.txt) (16);
  - [`PR-BODY.md`](PR-BODY.md).
- **The worked numbers.** Python ([`unrestricted_closing_replay.py`](../../../../tests/probes/wolfram/unrestricted_closing_replay.py)) and Wolfram both give `{True, True, True, True, {"10101010", "00101010", "01010101"}, {0, 1, 3, 5, 6, 8, 9, 11, 12}, True}`, and the prediction held.
- **nb1** (`beb062cb67bf8309a9ac3fc290b720821a374b6327cc30e41f165a6ced37c788`, 93,400 bytes):
  - built from [`unrestricted_closing_notebook.wl`](../../../../tests/probes/wolfram/unrestricted_closing_notebook.wl);
  - RESULT OK in 15 s;
  - every gate passes;
  - KernelChecked 82;
  - evidence `cited/local/unrestricted-closing-nb1-20261110.tar.gz`, 29,448 bytes, SHA256 `aea6e7d5ae21a170ea1ac516e4713575c1ebb0ab7537c1c18787bdf2b4f14444`, read back byte-exact.
- **Post script.** [`post.sh`](post.sh). The dry run passes.
