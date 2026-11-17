# Morning catch-up: Local and the public portal

GPT GC1999, 28 October 2026. Owner requested catch-up and a fresh submission check. No simulation, Lean replay, schedule restart or submission.

## Local L1054–L1057

Fetched and fast-forwarded through `01a2c406e48ad849364fcab89f3cc6fb9cbe1eda`; read all four complete entries and the report corrections. Local independently carries GC1998's exact first-mismatch proof. That hand result is now two-party: the dyadic past readout agrees with the centre until the first unsupported diagonal period, then gives the opposite bit. The Rule 60 countercontrol remains essential; this alone does not exclude a periodic centre.

L1054's period-parity equation carries directly from the XOR recurrence. With both feeders P-periodic, the obstruction is the parity of A OR B over a full P-block, equivalently parity(A) XOR parity(B) XOR parity(AB). The overlap is the new **nonlinear** term. Strictly, compared with Rule 60 there is also the additional linear feeder parity(B); “exactly one term” should refer to the nonlinear addition to the two-feeder XOR rule. For even P, feeders whose periods divide P/2 have even repeated block counts, so their OR cannot force doubling. This does not yet relate different centre bits.

L1055's statement about **periodic background tails** carries. The output-zero pair graph has only the two constant cycles; the output-one graph has only the 001 cycle. A periodic parent tail of least period q produces a tail with least period dividing q. Follow its finite forward ancestry to the white tail of the seed: the first nonconstant periodic tail must feed black and therefore have period 3; every earlier nonconstant period is divisible by 3. The argument neither says all possible tails are periodic nor restricts finite interior stretches to these periods. Transient graph paths must not be called periodic backgrounds.

L1057's no-solid-row lemma also carries: from time 1 the two leftmost cells are black, so from time 2 the third cell is white (both 110 and 111 output zero). The row still has a black edge. This excludes a solid black row across the whole occupied cone after time 1, not long interior caps. Numerical run-length claims were not rerun.

L1056's local identities carry, and the proposed direct inference from spatial background periods to temporal centre periods is unsupported. However, its stronger closure wording is not established. Known fixed-depth forcing establishes particular blocks, not a theorem that *only* a bounded block can ever be forced. Nonperiodicity of column 1 does not by itself exclude every spatial structure farther away. The absence of a demonstrated connection between the readout band and background is not proof that no dynamical connection can be established. Record the direct argument as insufficient; keep the broader reconstruction question open, with the missing cross-diagonal relation named in GC1998. This is a qualification of an inference, not a claim that the proposed bridge exists.

## Fresh public catalogue

Snapshot updated **2026-10-28T08:54:15Z**, compared with the retained GC1976 snapshot **2026-10-27T17:26:39Z**. Both have 56 entries. Two added IDs, two absent older IDs; current totals are **55 Lean Verified, one Lean Unverified**. No entry has a verified official prize target or a Prize Claimed tag. Catalogue and separate environment retain verifier image 10 / kit `7d665044b904117af9e82328aeb90a30692b2b85` / Lean 4.35.0.

### Newly listed e34744: existing proof, new listing

[Left-Diagonal Defect Spectra, Sublinear Monochromatic Run Bounds, and Semigroup Saturation](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261028-e34744) is Lean Verified, with 735 replayed constants and 20 selected accepted headlines, no Human Verified tag. Its 2,973-line Lean source is **byte-for-byte identical** to the now-absent `01554c` source, retrieved again for comparison: SHA-256 `d19dfbce3625a2ab7ab72c5e92cb151af8c0a32427ee5e62a96c6507eae0a181`.

Thus the prior [carrying review](GPT-D1BCBA-DIAGONAL-REVIEW.md) and [comment-correction review](GPT-PORTAL-UPDATE-20261025-EVENING.md) apply. There is no new proof body here. The advertised fixed-index bound L ≤ a − 2 remains linear despite “sublinear” in the title; white-run results retain their spatial-row hypotheses. Its `supersedes` field is null: source equality establishes reuse, not the administrative reason for the old listing's disappearance.

### Newly listed 6827d2: periodic pulses and aperiodic left columns

[Universal Center OR-Mask Blocking, Invariant Pulse Injection, and Left-Cone Aperiodicity](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261028-6827d2) is Lean Verified: 31 replayed constants, seven selected headlines, standard axioms, no Human Verified tag or official target. The earlier unverified `b035ac` is absent, but no explicit replacement relation is supplied.

Read the complete 213-line submission and the carrying definitions, effective-boundary identities, finite-strip/adjacent-column proof and real-pattern bridge in the pinned `Rule30MaskedJen` and `Rule30DrivenLeft` imports. Source review passes in its stated conditional scope; no independent Lean run or blanket audit of unrelated imported lemmas.

If the centre were eventually periodic, every recurring fall 1→0 would force a black cell immediately to its left. Meanwhile **every fixed column strictly to the left would have to remain nonperiodic**. The latter is an application of the kit's driven-left theorem: two periodic boundary columns enclose a finite deterministic strip, hence yield eventually periodic adjacent columns, contradicting the moving finite left edge. The effective driver c(t) AND c(t+1) inherits periodicity and is coupled to the actual finite left row.

The “grand incompatibility” theorem concludes a conjunction of these properties; it does **not** conclude False or nonperiodicity of the centre. Periodic prescribed pulses are compatible with an otherwise nonperiodic sequence. This usefully restates constraints a hypothetical exception must satisfy, but leaves the compatibility obstruction open. It does not establish a constraint on our past-readout frontier. Much of the carrying mechanism is explicitly imported from the existing kit; broader novelty is unassessed.

## Other changes and team status

- External `1910d0` (six-/seven-cell stripe tails), `1b82d8` (half-rate diagonal bound), and `0ef9c8` (period-32 shielding) gained Human Verified tags. The half-rate diagonal result had already received our complete source review in GC1960–GC1962.
- All 23 current team submissions remain listed: 22 Lean Verified; the old width-60 entry remains Lean Unverified. Nineteen have Human Verified tags. S1/S2/S3 remain Lean Verified, with human tags still empty. No fresh GitHub PR-status claim.
- No new computation is warranted merely by these catalogue changes. Local's overlap-parity identity is the relevant hand lead; deriving an actual relation between different centre bits remains the work required.

## Evidence

[Public catalogue](https://www.wolframcloud.com/obj/rule-30-prize/Agents/submissions), [JSON](https://www.wolframcloud.com/obj/rule-30-prize/Agents/submissions.json), [environment](https://www.wolframcloud.com/obj/rule-30-prize/Agents/api/environment). Verified-TLS downloads, baseline, exact sources, imports, delta and SHA-256 manifest retained outside git in `cited/gc1999-portal-morning/`. No authenticated portal action, local kernel replay, experiment or schedule change.
