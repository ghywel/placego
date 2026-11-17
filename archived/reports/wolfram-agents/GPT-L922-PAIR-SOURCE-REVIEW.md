# L922 pair source review (GC1831, 2026-10-24)

**Source review PASS; proposed Check plan not yet accepted.** Read all 183 lines
and the folder README at commit `540b68405914448b7634f4c12acb391b213db690`.
Rule30Submission.lean is 9141 bytes, SHA256
`27f799f47eecf22f138967ac27ccbc14ab0dffb20f55f5dc29be800aa6b44fd6`.
No Lean execution or new dynamics on GPT's host. Four draft compiles and their
axiom lists are Local-reported; no terminal Check receipt has been supplied.

## Carrying source and scope

The functions encode exactly the intended finite right halves. For p beyond
the cell-list length, getD returns false, so their finite support is immediate;
explicit FinSupp R31/R495 lemmas would make that fact visible but are not needed
for the five proposed headline statements. Column zero is deliberately unused
by the driven right-half initial state.

Both trap entries match GC1828's independently carried hand table: R31 at9 and
R495 at5 have row {6,8,14}. The ether prefix, wall indices7..19, phase0 and
(3+6)%7=2 all match trap_invariant. The boundary lemma supplies the full future
wall, not just one cycle. Subtracting the entry time is safe under the explicit
t>=entry premise. The q<4 / q<2 branches cover precisely the remaining odd
physical times. The parity lemma supplies every later odd sample. No unbounded
quantifier is discharged by the finite examples alone.

The equality u_eq and definition of Psi carry Psi_eq. Period2 from time0 gives
the two non-FinSupp conclusions by the existing absorption theorem. These are
two CQ01 instances; the global CQ01 proposition and CQ01Empty remain open.
The four-step restart is explanatory prose, not an unproved formal dependency:
the module independently certifies both entries. GC1830's explicit phase-3 Psi
corollary is optional and is not silently included among the five headlines.

The reversed-list relation is the claimed right-end move, including the special
one-cell black-wall extension. Validity requires the farthest cell to be black,
so it represents a canonical nonempty finite right half. For each valid shape,
P(S a)=some a and length(S a)=length(a)+1. These identities alone imply
root(S a)=root(a): the extra fuel is spent on that first inverse step. There is
no hidden reliance on a global termination or completeness theorem. Equality
of roots therefore propagates through all four constructors of EqvGen, including
arbitrary reverse moves and detours. P returns none on both reversed starting
lists; their roots are themselves, of different lengths5 and9. The final decided
inequality genuinely proves non-move-equivalence, not merely R31≠R495.

Unexpected boundary check: S [true]=[true,false] is the reversed representation
of a black cell at position2 with position1 white. It correctly accounts for
the wall-assisted width1 move that the kit's native width>=2 relation omits.
The result concerns this finite-word Move and fixed alternating-driver Psi;
it does not refute all-driver response completeness. L922's catalogue-first-use
assertion remains its bounded source-search claim, not independently established
novelty. No new mathematical source correction is required.

## Pipeline source comparison

Resolved the public pipeline kit to
`cc1e0e0e7c1ae8c971aec5c14aaabb47c7b8c554` and compared its complete Ether and
Sideways files with the already-read `3eca23c0a9fa6b153313655e6d51835406c2d06e`
snapshot. Pipeline file hashes:

- Rule30Ether.lean: `741114f2f05b514f1b8af8ce23d492b73418b90e28feb9c25bdcb4b97937d0f4`.
- Rule30PeriodTwoSideways.lean: `5184536e22d5f83b187aecf2dcd6afc118fa81257fa7fa303cef2ce9b793aaf3`.

The trap data, trap_invariant, driven recurrence, u/Psi definitions and absorption
proof are unchanged. The full differences are module/public syntax and tactic
renamings if_pos/if_neg to ite_eq_left/ite_eq_right in other proofs. This supports
the carrying semantic comparison; it does not establish the bytes of Local's
actual checkout or replay the entire import closure. The Check receipt should
bind that actual kit revision/toolchain and relevant source hashes.

## Checking-plan verdict

L922 gives 600 seconds CPU for each process, sequential commands and retained
logs. That is not a complete stage cap: a waiting child can outlive a CPU cap,
a Lake build can spawn dependency workers, and no memory/output/disk or pressure
stop is specified. The source is ready; revise/freeze only the execution wrapper
and agreement, not the mathematics merely to satisfy this review.

A concrete small-stage proposal to freeze is: one build then one Check, each
wall/aggregate-child CPU <=600 seconds; whole stage wall and cumulative child
CPU <=1200 seconds; one active Lean worker; aggregate process-group RSS <=4 GiB;
logs <=10 MiB; new artifacts <=128 MiB; free disk >=5 GiB; existing W1A pressure
and <=256 MiB swap-growth stops. The 4 GiB allowance covers the Lean/compiler
process group and supervisor, leaving substantial room in 16 GiB unified memory;
preflight must check actual headroom and avoid competing jobs. This is a proposed
cap set, not a newly measured cost or permission to run without its wrapper.
Reuse the reviewed W1A supervision primitives (3f908914...), with explicit stage
and per-step limits, failure retention and final group/accounting receipts.
Bind the exact module, full kit commit, toolchain, Check source and the five
headline arguments. Build only this target with dependencies already present;
refuse an unplanned dependency rebuild/network download or parallel expansion.

Back up the original root source and its digest before mutation. A finally path
must restore it on success, checker failure, resource stop or interruption;
verify restoration and retain failed artifacts/logs separately before cleanup.
Keep child/process-group cleanup explicit. Stop after one failed build or Check;
no automatic retry, notebook build or submission is authorized by this stage.

**Next concrete dependency:** exact wrapper/commands and Local's adoption of a
complete cap/receipt/restoration plan. Then accept or decline that bounded stage;
after it runs, read actual Check JSON, exit/axiom/headline and resource receipts.
The essay/notebook/gate are a later review. No extra source audit is needed unless
the module changes.


## L923 essay/abstract source read (GC1832)

Read the full 109-line essay template, seven-line abstract, assembly script and
33-line expected-number source at be7bcdca (full committed pointer retained in
the ledger). A pure-file comparison verifies that all 292 lines of assembled
essay.md are exactly the template with the reviewed Lean source inserted once,
byte-for-byte. Essay SHA256:
`45a0599cb24270ccf8d3a9169698d1dcb857fdeddae037ad2cc4f8147d98ea30`.
There are nine Wolfram cells. No assembly rewrite, evolution, Wolfram execution
or Lean build was run by GPT.

**Source verdict PASS, with scope qualifications for final prose/output review.**
The three illustration cells use the correct old-time alternating boundary,
physical row index t+1, odd-visible index2s+2, cell-list direction and ether
index offsets. The padding exceeds the 30-step cone for the displayed cells.
The reversed move/inverse formulas match the formal S/P; root stops before
applying the partial inverse at a root. Outputs asserted in the prose match
the carried hand trace and formulas. The expected-number script is a separate
implementation read here, not an independently rerun or retained-output check.
Local reports one Wolfram run; its actual output is not included in this commit.

The five formal type displays match L922's headlines; KernelCheck is last.
The Axioms and CallGraph cells address CQ01_R31 only. That is accurately described
as one headline, but the final acceptance gate must still check all required
headlines/axiom policies and the whole-module replay result from actual outputs.
DirectoryQ, import success, no failed/unevaluated cells, exact source binding,
checker success and resource receipts remain for the later notebook/gate review.
Do not treat prospective prose “the kernel accepts” as an already-read receipt.

Keep the prior-art wording bounded: replace the unqualified “no explicit right
half is shown in the kit” with what the cited catalogue search actually checked.
Likewise “new here” means the contribution presented by this submission, not
world-first priority. Existing trap/absorption machinery is correctly credited;
general CQ01, CQ01Empty and Problem1 are explicitly left open. The abstract's
LaTeX commands have single backslashes in the actual bytes (six commands);
JSON/tool display escaping is not a file defect. This unexpected byte check
avoids an unnecessary escaping correction. Public submission authorship is
pre-existing Local text and was not rewritten by this review.

No change to the frozen Lean source is requested. Exact Check wrapper/caps are
still pending; essay rendering, actual notebook outputs and gate will be reviewed
when supplied. This closes L923's available source review without granting a
build, submission or external-verification status.
