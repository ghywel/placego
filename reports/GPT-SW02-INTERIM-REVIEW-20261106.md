# SW-02 interim review — GPT GC2688, 6 November 2026

**6 November addendum, GC2690:** Local supplied L1563's immutable carrying packet. The [completed review](GPT-SW02-CARRY-REVIEW-20261106.md) supersedes the pending source/read statuses below: Q01 ⇒ Mortality, repaired AM-3 bounded amplification, CT-2's first-check bounds and the phase-repaired separator converse are carried. The historical interim argument and unresolved questions are preserved here; auxiliary claims remain scoped separately.

**Verdict: useful mathematical leads, correctly kept provisional; no prize conclusion or blanket theorem clearance.**
This reviews Local L1562 at shared commit `9ce60835`. The strongest prospective addition is the reverse
`Q01 → Mortality` bridge: a complete reviewer reconstruction is given below. The finite amplification and checksum
claims need their actual proofs before a carrying verdict. The external `BWH → Q01` claim is confirmed as prior art,
with further exact relationships that sharpen the dependency diagram. Four implementation/brief issues should be
corrected by Local at a safe boundary before their outputs are used in the synthesis.

Local remains the execution owner. No swarm command, build, census, frozen-input edit or schedule restart was made.
Three GPT subagents helped with source inspection; their checks are same-worker self-checks. The owner’s lifted usage
ceiling governs; this review does not restore the old ceiling or request a halt.

## 1. Read scope and status

Read: L1560–L1562 and the intervening commits; the revised manifest and queue, bench and compilation builders;
the exact frontier, Q01 and wedge definitions in kit `9d837cd5e5ac447cd868c20aebf49a1b4cfa866e`;
[G13.1–G13.3](../archive/gpt/RULE30-GPT.1.md), the full `Rule30InverseCascade` source at
[PR60 head `db6e7112`](https://github.com/WolframInstitute/Rule30PrizeKit/blob/db6e71128339d1fc45b5a7ab5f2bade997996ae3/lean/Ruliology/CellularAutomata/Rule30InverseCascade.lean),
the checksum definitions and earlier population caveats, and the pinned external sources in §3.
The last complete portal/kit refresh is GC2687 at **10:58:01Z**, not a new refresh performed by this review.

**Missing sources:** the committed interim packet contains the summary and builders, not the AM-3/CT-2/CP-4 or
Q01-to-mortality proof reports, their numbered claims, both skeptic verdicts, rescuer repairs or finite certificates.
The M5 run directory is not present on GPT’s host. Fresh shared-store listings found no interim source bundle.
A precise source request was left for Local, without asking for a rerun or interruption. Accordingly:

| Item | Review outcome |
|---|---|
| Q01 ⇒ Mortality | Complete reviewer hand reconstruction; **PROOF-SKETCH**, not a read of Local’s absent proof or a Lean build |
| BWH ⇒ Q01 | Exact matching external theorem and definitions source-read; **KNOWN**, no fresh kernel replay |
| SEP = LR₁ | Full equivalence **not carried**; reverse realization still needs its source |
| AM-3, ticks 46 and depth 7,911 | Mechanism and count comparison audited; numerical/uniform claims **not carried** |
| CT-2, pair law and three-index bound | Definitions of the checks read; epsilon definition and connecting argument **not available** |
| PE-1, ¬AbsorptionT t001 | Exact external theorem located; **KNOWN**; Local’s replay/axiom receipt not independently reviewed |
| CP-2, XP-4, P2-3, CP-3 | Received as L1562 summaries only; **no carrying verdict** |

The 106 screened candidates and repeated subagent derivations are useful triage information, not theorem counts.

## 2. The strongest structural lead: Q01 and frontier mortality

The current kit proves `Q01_of_mortality`, `mortality_iff_survival` and
`budget_iff_mortality_bridge`. Its header still says the reverse is unknown because a legal frontier need not be
known to come from a physical row. The useful repair is **not** to realize the original frontier as a time-zero
horizontal row. Straighten an entire hypothetical immortal frontier history into a later horizontal row instead.

Appendix A gives the complete construction with its two boundary updates. For a starting frontier of length r,
take the horizontal time `T = r + 2`. The row there is finitely supported on the negative half-line, has a leftmost
black cell at either `−2r−2` or `−2r−1`, and keeps column −1 black at every even time measured from T. The successful
frontier guard supplies exactly the two missing updates at column −1. A black center is masked whenever it occurs,
so replacing the center by white gives the exact zero-boundary history forbidden by Q01.

**Status: PROOF-SKETCH, independently reconstructed by GPT while reviewing the claim.** This corroborates L1562’s
proposed implication, but it is not an acknowledgement that the three unavailable Local derivations were read.
The specific carrying step to compare is the birth/guard calculation in Appendix A, followed by finite support and
the parity at T. If carried, the result joins Q01, Mortality and the all-length repeat-budget proposition into one
equivalence. It does not prove any of them, nor give one death-time bound uniform over all frontier lengths.
A 1,231-frontier test cannot establish this universal implication; the chart is what does the work.

**Suggested next step:** compare Local’s full argument with Appendix A and reuse the existing frontier definitions
and budget equivalence. A small reverse-chart theorem is a better formalization target than another frontier census.

## 3. External ladder: stronger prior art than the short summary records

Pinned external repository: `lhallee/rule30-open`, commit
`f877f5afd5609373e2df1639e943d04e3a56e83b`. Read the full
[WedgeLadderQ01 source](https://github.com/lhallee/rule30-open/blob/f877f5afd5609373e2df1639e943d04e3a56e83b/Rule30Open/PeriodTwo/WedgeLadderQ01.lean),
its [proof note](https://github.com/lhallee/rule30-open/blob/f877f5afd5609373e2df1639e943d04e3a56e83b/Rule30Open/PeriodTwo/WedgeLadderQ01.md),
the supporting `WedgeLadder` proof, and the relevant definitions in `WedgeSmall`.
The external copies of the wedge definitions match the current kit: n ≥ 7, binary input prefix of length `2n+2`,
constant wedge of length `n+2`, constant symbol 2 or 3. There is no hard-core premise in BWH.

The exact existing theorems include:

- `Rule30Open.bwh_Q01`: **BWH ⇒ Q01**, with no `SmallRW` assumption.
- `Rule30Open.binaryCTS_iff_Q01`: Q01 is equivalent to the binary constant-tail separator.
- `Rule30Open.q01_iff_horizon`: Q01 is equivalent to a suitable finite horizon at every depth, with the existential
  horizon retained; this is not BWH’s particular linear horizon.
- `Rule30Open.q01_constantTailSeparator`: Q01 implies the kit’s constant-tail separator condition, hence SEP by the
  existing separator equivalence. It does not establish the converse SEP ⇒ Q01.

These statements concern all binary endpoints where specified. Hard-core endpoints are a smaller class; the
right-column condition is needed for the hard-core lemma, not for every part of the cone/peel chart. The current
kit’s broad “no known order” wording is therefore outdated relative to this external source. Our older
[GC2414 comparison](GPT-PR75-76-HYPOTHESIS-COMPARISON-20261103.md) was a statement of the sources then read, not a
barrier to this new source evidence.

GPT also reconstructed a direct moving-front proof of BWH ⇒ Q01 before finishing this external read; it is
**known, reproved here**, not an additional theorem. The source’s reusable helpers already include
`zpair_backward`, `zend_binary`, `zcone_chart`, `zpeel_chart`, `zend_finite_rank`, and the reverse-history lemmas
`hcell_rule`, `hcell_far`, `hstart`, `zl_hstart`. Build on those instead of recreating the whole diagram.

For **SEP = LR₁**, locating the hard-core constraint and proving it necessary is not enough. The reverse direction
must realize each violating hard-core endpoint as a left-finite history with a compatible column 1 and freely
driven column 2, including phase, onset and end conditions. The current review supports the forward exclusion
direction but does not carry that converse. CP-4’s full source is the next required read.

The separate [Traps001 source](https://github.com/lhallee/rule30-open/blob/f877f5afd5609373e2df1639e943d04e3a56e83b/Rule30Open/Columns/Traps001.lean)
contains the exact `Rule30Open.not_absorptionT_t001` at lines 69–74: a closed period-15 trap stays apart from t001.
Its theorem statement and proof call were inspected; its finite certificate was not replayed here. PE-1’s known-result
classification is right. Neither inspecting this source nor Local’s reported compilation supplies a fresh GPT axiom receipt.

## 4. AM-3: keep the finite gain, identify the actual asymptotic gap

L1562 distinguishes finite amplification from the conjectural H(rho), which is essential. G13.3 and PR60 already give
inverse synchronization **when suitable resets occur**. The complete word needs the following cell:
`0 1^(3k+1) 0 z`; treating `010` alone as a complete synchronizer drops a guard. PR60’s
`scheduled_cascade_closes` and `finite_cascade_closes` handle finite stacks under their reset/closing hypotheses.
They do not supply a rate or prove that every relevant generated input has the needed chain of resets.

The proposed new content is the **uniform supply** from the forced strips: the t ≥ 46 twin, and the full depth-7,911
guarded tree after T*. Its proof must specify the strip’s onset in this zero-boundary population, every branch’s
boundary and finite-tail conditions, the following reset bit, and why later reset locations work for all children.
No unproved all-time wall/strip recurrence may replace the from-birth condition. These are requests to read the
actual proof, not evidence that it fails.

The exact counting comparison can already be sharpened. Let `G = F²`, let Y be a nonzero G-immortal row of width W,
and suppose it has a complete guarded binary predecessor tree of d **G-generations**. Then:

1. Every leaf has width **V = W − 2d**, by the nonzero F width law.
2. There are **2^d distinct leaves**. Sibling distinctness is a hypothesis; children of distinct parents cannot
   coincide because G is a function. Different inverse descriptions alone would not suffice.
3. Each leaf is immortal only if all intermediate even-time checks are included in the guards; target immortality
   then supplies the remaining future.

Thus the comparison is **`2^d ≤ I(V) ≤ U(V)`**, for an upper bound U on the same immortal population (or a finite
survivor superset). It is not a comparison at width W. The early-check cap is at leaf width, `2^floor(V/2)`.
Fixing d ≤ 7,911 does not provide an exponential lower bound as V grows. It is a genuine finite family, but the
asymptotic route still needs an unbounded depth/width relation plus matching guards. If H(rho) supplies one,
state its time units and width transformation before comparing exponents. The exact inequality above avoids
confusing F-ticks with G-generations.

**Warm continuation:** extract a reset-chain lemma on the actual generated histories, with a bound on depth versus
leaf width. Do not enlarge the reset census merely because the finite depth is large. If no such bound is available,
preserve the finite theorem and ask which constraint survives conditioning on the earlier inverse choices.

## 5. CT-2: anti-concentration can be useful without yet being a survivor count

The checked definition is

    C_n(f_0,...,f_(n−1)) = X_(2n+1)(0),
    c_n = 2^(−n) sum_f (−1)^C_n(f),

with temporal boundary `(1,f_0,1,f_1,...)` and the sideways Rule 30 inverse recursion. This is uniform measure on
free words, not automatically the uniform measure on fixed-width survivors.

The summary does not define epsilon_n or show how its adjacent-pair law gives the three-index conclusion.
That step must be supplied. For example, **if** epsilon meant `(1−|c|)/2,` the inequality alone would be insufficient:
`c = (24/25, 0, 24/25)` gives `epsilon = (1/50, 1/2, 1/50)`; both adjacent sums exceed 1/4, while two of the three
absolute biases exceed 19/20. This is a control on an incomplete inference, **not a Rule 30 counterexample to CT-2**.
The actual definition or an extra identity may exclude it.

If the stated three-index conclusion is proved, at least two checks per block of three have each output bit with
uniform probability at least 1/40. That is worthwhile uniform anti-concentration. It does not itself give joint
survivor decay: abstract checks all equal to the same fair bit are individually balanced, while the probability of
passing all checks stays 1/2. This example concerns the marginal conclusion, not the unspecified pair law.

A precise continuation is the conditional newest-bit derivative. Write

    D_n(v) = C_n(v,0) XOR C_n(v,1).

For a nonempty event H depending only on older bits v, with the last bit still fair and independent under H,

    P(C_n = 0 | H) ≤ 1 − P(D_n = 1 | H)/2.

For each v with derivative 1, exactly one final-bit choice passes; at most both pass for every other v. A uniform
lower bound on that **conditional** derivative would give an actual contraction factor. Earlier checks respect the
triangular bit dependence, but finite-support requirements may already fix the newest bit. The proof must say which
conditioning event it preserves. This is the useful next examination of CT-2’s pairing, rather than another
unconditioned table at larger n.

## 6. Workflow findings for Local at a safe boundary

These are static source findings, not claims of observed resource overruns or lost results. The existing runtime
evidence was not available. No live-run changes were made.

| Priority | Finding | Correction before relying on the affected output |
|---|---|---|
| P2 | `q.py:75,89`: small and bench use independent locks; neither a small-job cap nor a shared per-task reservation lock is enforced | Restore the documented global one-job lock, or explicitly amend concurrency and enforce small-job limits, atomic budget reservation and unique run IDs. Same-task cross-lane calls can otherwise race for the same run directory. |
| P2 | `build_w5.py:7–37`: the assembled claim index joins claims and skeptic verdicts but never `rescue.json` | Join rescuer statements, status, source and open step by claim ID; preserve original and repaired versions. Include original proof/frame pointers. Correct `build_w3.py`’s `SK-*` pointer to SKR/SKM; keep rescue IDs unique across batches. |
| P2 | `build_w4.py:86–99`: BN15 says a finite search failure refutes Closing(n); BN16 asks for eventual-period conclusions from a finite tail | Distinguish a failed cutoff from a certified nonclosing witness. Report finite-window periods as candidates; eventual periodicity needs a closed-state/strip certificate with a bridge to the entire sequence. |
| P2 | `q.py:99–121`: per-process CPU limits and after-run charging do not enforce a task-wide aggregate CPU stop | Enforce aggregate process-tree CPU or a verified single-worker contract. A missing receipt must block further budgeted launches until reconciled; `min(wall,cpu)` can undercharge multiprocess work. Audit actual receipts before claiming stage totals. |

The manifest also retains an obsolete 50% stop row despite the later owner amendment, and Wave 5’s builder emits
eight tasks where the roster says six. Record the amendment/reallocation; neither discrepancy is a reason to stop
healthy current work. The compilation briefs correctly preserve PROOF-SKETCH status, population matching and open
doors not selected by the judges. Keep those safeguards.

## 7. Compact next queue

1. **Local supplies the immutable interim packet:** AM-3, CT-2, Q01/Mortality and CP-4 full reports and claim locations;
   mathematical/record skeptic verdicts and any rescues; strip certificates; relevant bench receipts. No rerun needed.
2. **GPT’s next carrying read:** the Q01/Mortality boundary chart, then AM-3’s universal finite reset supply, then
   CT-2’s epsilon definition and three-index implication. The packet determines whether the present reconstructions
   match Local’s proofs or repair them.
3. **Local synthesis:** apply the leaf-width and conditional-measure comparisons; incorporate rescued claims;
   cite the exact external ladder. Leave SEP’s reverse realization pending until read.

This ranks the current mathematical review; it does not close the other candidates or dispatch new computations.
The requested interim review is complete within the stated source scope. Carrying clearance of the missing proofs
remains a specific source dependency, not a request for new owner permission.

## Appendix A. Reverse chart from an immortal frontier

**PROOF-SKETCH / GPT reviewer reconstruction.** Assume a legal frontier of length r ≥ 1 survives forever. Let its
successive words be w_n, of lengths r+n, with symbols `(a_i(n), b_i(n))`, high bit first. A successful scan obeys

    b_i(n+1) = b_(i−1)(n+1) XOR (a_(i−1)(n) OR b_i(n)),
    a_i(n+1) = a_(i−1)(n+1) XOR (b_i(n+1) OR a_i(n)),

at old indices `0 ≤ i < r+n`, with the scan-memory entries at index −1 equal to zero. Its last scanned high and low
bits are both s_n. The appended symbol is `(1, NOT s_n)`. At index zero the equations imply
`a_0(n)=1` and `b_0(n)=b_0(0)` for all n.

Place these bits on the skew chart

    a_i(n) = X(n+i+1, i−r−n),
    b_i(n) = X(n+i,   i−r−n).

The two parities are disjoint. For every t ≥ T := r+2 and j < 0:

- If t+j+r is even, take `i=(t+j+r)/2`, `n=(t−j−r)/2` and set X(t,j)=b_i(n) when i ≥ 0.
- If t+j+r is odd, take `i=(t+j+r−1)/2`, `n=(t−j−r−1)/2` and set X(t,j)=a_i(n) when i ≥ 0.
- In either case set X(t,j)=0 if i < 0.

For the nonzero-index cases n ≥ 0 and `i < r+n` follows from j < 0. Thus every negative horizontal cell is defined.
Set X(t,0)=1 precisely when t and r have the same parity.

For old indices the two scan equations become exactly the Rule 30 update `left XOR (center OR right)` on this
chart. Index zero uses the zero scan memory; farther left all cells are zero. The remaining cases are births at −1.
The last symbol of w_n has its high bit at time r+2n. The last scanned low bit s_n sits at column −2 at that same
time, and the last scanned high bit s_n sits there at time r+2n+1. The two updates at −1 are therefore

    s_n XOR (old_last_high OR 1) = NOT s_n,
    s_n XOR (NOT s_n OR 0)       = 1.

These are precisely the appended low and high bits at times r+2n+1 and r+2n+2. Equality of the two scanned bits,
the successful guard, is the carrying condition. Column −1 is consequently black whenever the chosen center is
black. Replacing that center by white leaves the negative-half updates unchanged, because its contribution is then
masked by the already-black cell at −1.

At time T, all positions j < −r−T are zero; at j = 1−r−T the cell is a_0(T−1)=1. The leftmost black cell is either
−r−T or 1−r−T according to b_0. Both are negative. Since T has the parity of r, column −1 is black at all times
T+2k. Starting at T therefore yields a finite nonzero negative-half row contradicting the exact kit Q01 statement.
This proves the desired implication by contraposition, subject to the stated hand-proof status.

## Provenance and validation

**Record searched:** current record and GC2686/GC2414; G13 inverse reset theory; cached current kit lean/equivalents,
catalogues and portal/open-PR index from GC2687; exact PR60 source; pinned external WedgeLadder/WedgeLadderQ01,
WedgeSmall definitions, proof note and the Traps001 theorem. These searches establish the cited matches, not a global
novelty certificate. No mathematical or executable source in the running swarm was changed. Only review records
are edited; ledger, document-link, whitespace and privacy/conflict checks accompany publication. No TeX edit or
fresh Lean/Wolfram validation is claimed.

Evidence packet: shared-store `cited/gpt/gc2688-interim-review-20261106.tar.gz`, SHA256
`c7a18776ba0912a8de136e1b37883bfe42843caffbeb80b94c18f42b00ea4895`, 264,088 bytes. It contains the
reviewer self-check notes, exact fetched external sources and source hashes. It is not the absent Local swarm packet.
