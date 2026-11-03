# Rule 30, the picture so far (the synthesis entry) — delivery record

Local, 3 November 2026 (L1478). **Status: ASSEMBLED, notebook RESULT OK, not posted.** The prose, the abstract and the
appendix are Cloud's (CL698 to CL704, with GPT's reviews GC2565, GC2585 and GC2593); the Lean anchor, the assembly, the
notebook and the posting are Local's. Posting waits for GPT's packet read and the owner's word in chat.

## What goes out

- **Essay** [`essay.md`](essay.md) (`ac5b6350…`), assembled by
  [`assemble_synthesis_essay.py`](../../../../tests/probes/wolfram/assemble_synthesis_essay.py) from Cloud's
  [`essay-prose.md`](essay-prose.md) (`0ec2c035…`) and [`entries-by-object.md`](entries-by-object.md) (`0933fc20…`), with
  the portal form embedded. Cloud's files are not edited; every repair is an exact replacement the assembler prints.
- **Abstract** [`abstract.txt`](abstract.txt) (`dbfc2f54…`, 247 words), unchanged.
- **Lean content:** the left-coincidence portal form
  [`Rule30Submission.lean`](../left-coincidence/Rule30Submission.lean) (`62b661a9…`), unchanged since GPT's reads (GC2583,
  GC2587). The portal Check on the verifier kit 93d98bbe passes: 37 constants, ten headlines, no new axioms.
- **Notebook** ([`synthesis_notebook.wl`](../../../../tests/probes/wolfram/synthesis_notebook.wl)): **RESULT OK** in 24.7 s
  on the M5. Eight outputs, no message cells, KernelChecked 37, the ten headlines' axiom sets as the Check printed them,
  no local paths. Notebook `8d8d0acd…`. Receipts: `cited/l1478-synth/synth-nb1-receipts.tar.gz` (`be75f65f…`).

## The assembler's repairs

1. Front matter: final date; `Abstract: See abstract.txt.`; Sources and Links in the portal's link format (the kit, the
   record, Rowland 2006, Jen 1986; Rule 30 Prizes, the kit's `Rule30LeftReset` at c42f6e5).
2. The internal draft-status paragraph removed (GC2593).
3. Section 2: "the citation map beside this draft" now points to the appendix (section 8).
4. Section 2F: the 4b2a58 sentence narrowed as GPT gave it (GC2593): the eight-cycle obstruction is on proper subsets
   of the four-cell window in a rational 16-cell potential inequality; the exact-coboundary exclusion is separate.
5. Section 7: built in L1474 and L1476, 180 lines, ten headlines, 37 constants, GPT's source reads GC2583 and GC2587; the
   D bullet lists `D_white_of_coincidence` and `D_evwhite_iff_eventually_eq` and drops "to be added to the module"; a
   Lemma E bullet with its guards (a later black for the white child; blacks arbitrarily late for the equivalence).
6. Section 7 ends with a computation cell: the seed's white diagonals below 48 on the last 1,024 of 4,096 ticks are
   D 2, D 7 and D 28. For each, the parents coincide there, and for w ≥ 3, D(w − 3) is the difference of D(w − 2), which
   has a black. This is an illustration on a finite window.
7. The formal proof and checks: six F1–F3 headlines, then the four Lemma E headlines, axioms for all ten, KernelCheck
   last.
8. The appendix becomes section 8, with its object headings one level down. The author column is the first listed
   author, "ours" as in section 2 (GC2593), and Cloud is glossed as the record's Claude (Anthropic) worker.

## Submit parameters

- Title: the front matter's `Name`.
- Headlines (full names): `Rule30Submission.closed_form`, `.farther_of_child`, `.solutions_agree`, `.coincidence_iff`,
  `.white_of_coincidence`, `.evwhite_iff_eventually_eq`, `.D_closed_form`, `.D_coincidence_iff`,
  `.D_white_of_coincidence`, `.D_evwhite_iff_eventually_eq`.

## Kit PR, staged and not pushed

`Rule30LeftCoincidence` is committed on the local kit branch `left-coincidence` (92aab4b, on c42f6e5): the module, its
import and a catalog row with the standard byline, plus "The lemmas were proposed in the contributors' record by Claude
(Anthropic)". The kit form (`3aa1dbf7…`) differs from the read source (`71f3893d…`) only in that docstring credit
sentence. It passes `lake build` without warnings, `lake build Ruliology` (199 jobs) and the Check (37 constants, ten
headlines). The submission id `R30-PENDING` in the row and in [`PR-BODY.md`](../left-coincidence/PR-BODY.md) is filled in
after posting.
