# Universal left side: posting review

**Verdict.** The mathematical carrying read and both official module checks pass. GPT clears the corrected portal source, abstract, essay and kit module at `afad0f15`. For the portal upload, Local should use the replacement notebook generated from the pins below once its Wolfram release receipt passes. The passing L1507 notebook predates the corrections. Local owns the notebook and posting. This review does not require a further editorial pass on an exact regeneration.

## What the proof establishes

Take a configuration with a leftmost black cell and any right tail. At the anchored moving edge, wheel 0 stays black and wheel 1 is black from the next tick. In the induction, first take the maximum of the two parent settling times. A subsequent black of the nearer parent resets both children to the complemented farther bit. If the nearer parent eventually stays white, both children integrate the same sequence and their XOR is constant. For a complementary child the antiperiod L corrects the phase. Adding L to the common shift preserves every previously aligned wheel because L is a period of the entire lower prefix. Finitely many wheel thresholds can be replaced by their maximum. This carries CL724’s hand proof in its own shift convention and the composed module's version with the shift on the configuration.

The finite-register bridge follows the physical diagonal recurrence by induction on time, including its special first two wheels. The mask, four earlier phase lifts and 16-tick return supply the generic hypotheses through wheel 53,207. At the first fork the white parent leaves two complementary choices. A nonzero residue of a proposed common shift modulo 16 changes a phase of wheel 400; that phase can be witnessed arbitrarily late. A zero residue preserves the lower phase but cannot remove the opposite bit at 53,208. If both finite witnesses aligned with the single seed, composing their alignments modulo 16 would contradict this result. This carries the nonconstructive assertion that at least one differs from the singleton, without identifying the witness inside Lean.

The fork distinguishes periodic **words**. The two witnesses' least period lengths at the fork are equal. A separate 16-phase read of the literal gave `0100000100001100` and its complement, of weights 4 and 12. Neither word is a rotation of the other. The formal headline rules out a common shift of the whole prefix.

## Corrections and provenance

The abstract and essay distinguish Rowland's white parent (his column 53,208) from its child (his column 53,209, our wheel 53,208). They state the return on the 53,209-cell register and identify the origin of its literal by external replay. The literal's bit length is 53,207; its stored prefix width is 53,209. Its 16,017-digit decimal representation has SHA256 `3ff6132fbff18e6490e8da585c8facb86eb8eae931f0cd1a13dc56efbf1aa341`, matching the retained replay. The revised text also separates eventual universality from earlier quantitative settling and passage results, and gives the verified range of Bosdure's finite zero-boundary result. The kit row now places weight six at the farther parent, wheel 53,206. [Rowland §5](https://doi.org/10.25088/ComplexSystems.16.3.239) · [Bosdure’s portal entry](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261027-317c64)

| Corrected release input | SHA256 |
|---|---|
| Portal Lean | `fbe8869531ed3ee2edc59faf7c20ea211a2b78a90e690626440d6d48ec28874c` |
| Kit Lean | `991be6f58b57d92fe62bc760ecec8a823728b8b03498b5d5b9eb84442745d437` |
| Abstract, 209 whitespace-delimited words | `f1672edd83205618f99331089fc2ecc5869416ecca74ee75e8942f0c3a58d0c4` |
| Assembled essay | `ef32ec78a8976a0c73f3f8220485b2e2fcf43db7ef980eef2b8a0f1f0040b9c7` |

I checked the embedded Lean byte-for-byte and compared the executable content of each corrected Lean file to L1507 after removing comments. All declarations and proofs are unchanged. The release driver now compares the decoded source in the notebook icon to the portal file. The public index at 18:02:51Z advertised verifier image 17, Lean 4.35.0 and kit `722a0c515486066f97ccc81aed57eca949cf38db`. The reviewed public kit main was `a91c727339e2348b0351b3d1311a60a44ee89561`. The kit, portal, PR sources and Rowland’s original argument were searched for overlap; the attribution is to a kernel-checked universality and realized-fork result. [Release folder](wolfram-agents/submissions/universal-left-side/README.md)

## Which checks ran

Local reported an official pass on all nine headlines and a successful Wolfram notebook for the earlier L1507 packet. Cloud independently reported passing all nine headlines, replaying 193 constants of the earlier module on the Linux host (CL729). On Intel the first two cold compiler treatments reached the original 768 MiB memory guard in the upstream `Rule30BlackRuns` dependency. Neither Intel attempt produced a verdict from the official checker. Host headroom stayed above 5,455 MiB and swap did not grow. The owner raised the allowance to 4 GiB and made this the standing Intel Lean build cap. The same checker then completed on both revisions. Peak sampled tree RSS was 1,598,552 KiB, minimum headroom 5,810 MiB, and swap growth zero.

| Corrected form | Kit revision | Standard compiler and official checker |
|---|---|---|
| Portal `Rule30Submission` | Verifier image 17, `722a0c51` | PASS, 193 constants replayed, 9/9 headlines, zero new axioms |
| Kit `Rule30UniversalLeftSide` | Kit main `a91c7273` | PASS, 193 constants replayed, 9/9 headlines, zero new axioms |

Synchronous elaboration also passed both checks, with 184 constants on each. Recompiling the two modules with the ordinary command-line setting on the same import objects reproduced the 193 expected by the notebook driver on both. The checks use `--claim partial`; they are not portal submissions. The unmodified official checker printed a deprecation warning about its own replay API. The verified shared-store archive `cited/gpt/gc2654-universal-left-checks.tar.gz` is 5,558 bytes, SHA256 `76e9fb1963c50e290a0204d78aa7c82ee1054d3c5aebe7dab0d958e9554635fb`. It contains the four checker outputs, source manifests and the receipts for the stopped and successful builds.

**Release handoff.** Use the corrected source pins in a passing current-verifier module/notebook run. Confirm the notebook’s exact source icon, matching abstract, eight outputs, white-wheel replay, weight table, named axiom sets, 193-declaration kernel check and final notebook digest. Cloud owns the separate whole-kit build and its precise outcome belongs in the PR body. A whole-kit CI result and a public portal verification are separate from this mathematical clearance.
