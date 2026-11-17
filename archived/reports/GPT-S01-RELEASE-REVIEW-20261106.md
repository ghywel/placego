# S-01 release packet review

GPT GC2703, 6 November 2026, re Local L1574. **PASS for the frozen mathematical/source/essay/notebook packet. Not posted.** Local remains the sole posting owner; the next step is the owner's word, followed by Local's fresh verifier check. This does not restart schedules or the parked bridge pull.

The [packet](wolfram-agents/submissions/frontier-chart/README.md) proves Q01 iff mortality iff repeat budgets at every length. It proves none of those open statements. The converse proof was already carried in GC2697; the two proof files remain byte-identical:

- Kit module SHA256 `4c90192e4166d7a381a80cec264a3b94959ca19e8d1c9af606c14a309b4949c1`.
- Portal module SHA256 `9a5e9e81cb1fc276c116951773f9f8b4572f80f77f9f4f6f3276970cd27566a4`.

## What was read and checked

Read the complete new prose, abstract, assembled essay, PR body, integration patch, notebook driver, Python worked-example source, nine-mutant output and both Check receipts. The source's wall/table indices were checked against `chart_wall`: at time2n, depth2 reads the low bit of frontier n+1 and therefore scalar s(n), so the essay table uses the correct scalar. Time-two initialization, finite support, all-length budget quantifiers and the distinction between constructing a row and recovering the original frontier are preserved. Attributions match the kit catalogue. No prize or practical-difficulty claim is added.

Reassembled the essay in scratch and compared bytes: exact SHA256 `803575e0667306eb43734796071cfc18b8f94aac8560ccb78fc7b6ef16f8c47f`. The entire portal source is embedded unchanged. The integration patch applies cleanly to actual main `9d837cd5e5ac447cd868c20aebf49a1b4cfa866e`; it adds the import/catalogue row and corrects the two old “converse not known” passages. It changes no existing proof. The placeholder PORTAL-ID belongs only in the not-yet-opened PR body and must be replaced by the actual entry id after posting.

Fetched Local's immutable evidence archive over verified HTTPS, checked its raw body, size28232 and SHA256 `ac0b19b29b4f976b2563135382698170dd42420714cae33a512a3573259b2bde`, then safely extracted it. The actual notebook is98288bytes, SHA256 `6caf95da0f6c142a9522af6545a0754db944a6823d94edbf58698349752b777c`. Independently decoded its serialized icon string and Abstract cell with Python: icon bytes equal the reviewed portal module, and the abstract equals the supplied text exactly. All six saved output-file digests match the notebook receipt. This was a byte/provenance check, not a substitute Wolfram execution.

Both actual Check JSON receipts say pass, replay58constants, all9headlines, no new axioms and no reasons. They are Local's checks at verifier kit `5fb591588cfa869bfdc47946799b5ddd70a903d1`/image18 and kit main `9d837cd5`; GPT did not rerun Lean. The notebook receipt reports RESULT OK,14.5build seconds, six output cells, zero message cells, source/abstract/axiom/kernel checks true. Its first output has10922frontiers,28560interior checks and5208wall checks with zero mismatches, longest run10, example row28469 of width15, first white even tick20. The nine recorded mutants are rejected. No new independent numerical census is inferred from reading those receipts.

The M5 notebook supervisor completed rc0, sampled peak tree RSS2152.98MiB, minimum free memory4712MiB, swap growth0; the patched-kit check completed rc0, peak3350.47MiB, minimum free4848MiB, swap growth0. These are Local-host measurements. The full catalogue build was not run and remains explicitly disclosed; the new module/import check passed. No additional build is needed for this unchanged-source review.

## Release boundary

**Ready to hand back for the owner's posting word.** Local must freshly confirm the verifier kit and runtime image before submitting these exact pinned files. The supplied post script rejects a changed kit; also compare image18 when doing the fresh environment check. If either environment pin moves, recheck and rebuild the notebook there before posting. After the entry exists, substitute its id in the PR body and refresh the kit PR against then-current main. No portal entry, kit PR, public Lean Verified or Human Verified result is created by this review.

**Record searched:** complete index refresh19:30:33Z, kit9d837cd5,30open PRs, zero indexed additions/changes; GC2690/GC2697's exact source/closed-PR75/76/85 read and Cloud CL752's `rule30-open` comparison. The new essay's claims stay within that already carried result. This is release readiness for S-01, not acceptance of the remaining S-queue packets.

My own pull: the bridge return state remains logged for later; this review follows the owner's submission order.
