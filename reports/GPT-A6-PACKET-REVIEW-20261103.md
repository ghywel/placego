# A6 packet review — GC2615 / GC2617

GPT, 3 November 2026. **Final repaired packet PASS (GC2617 below).**
The original GC2615 verdict was mathematics/proof-receipt PASS with one
notebook abstract-cell repair required. That repair is now cleared. Local remains
the assembler and sole poster under L1494's owner authorization. Cloud's
CL711 confirmation is read and accepted. No new owner permission is needed.

## Exact packet read

| Item | SHA256 |
|---|---|
| Portal Lean, 506 lines | `1e7e7c51a58e684140a4c48c1d962d8bcd259021ed78793b6c91671794b3c977` |
| Essay, 35,279 bytes | `defe0ce18fa9e8f20fd6b6c159acfa0a89f585c8d09fdcc8258f19bd46164c83` |
| Final abstract, 248 words | `a3a6d68a7e794eb76861c19c56a7f327a70d8b68b1777501b351798e92ac499f` |
| Actual notebook, 137,160 bytes | `4b6e1111b7d56dc1c5730dcc7a76b6b757e1ea24eb024b4fffcf7c5c06b59f28` |
| Notebook driver | `2186bb16c58f1f619e61b92ede0c0b1d4645a153a1faed370ada3067f4691137` |

Read the complete portal source, final prose and abstract, both assembly
scripts, notebook driver, and actual archived outputs/launchers/METADATA.
The declarations from `set_option autoImplicit` through the namespace end
match the previously carried probe byte-for-byte. Its source-faithfulness
review is [GC2604](GPT-PHASE-TREES-REVIEW-20261103.md). The essay embeds the
exact portal source. Decoding the actual notebook's iconized interpretation
string, including Wolfram's named/hex character escapes and line wrapping,
also gives the exact portal-source SHA above. This is a text comparison,
not Wolfram execution or an Intel Lean build.

The upper bounds 22/24/24, chosen depths 14/8/10, black-edge hypothesis,
all-alignment reductions and `d <= k` tail restriction are preserved.
Computed maxima and finite growth observations are now separated from
the formal upper bounds. The corrected phase origins agree with L1294,
L1308 and L1304, also confirmed by CL711. The candidate-test counts are
the Python mirror's counts; CL711's optional wording clarification is
reasonable but not a mathematical blocker. No universal capture or
all-depth exclusion is asserted.

## Retained machine evidence

Raw-body archive `cited/l1493-a6/a6-nb1-receipts.tar.gz`: 49,819 bytes,
SHA256 `5a6f0315179658b4687e88c642da65ce28c9be98eb725122bbacfeedbabfe238`.
The archived essay matches the reviewed essay. Local's toolchain is Lean
4.35.0, verifier kit `93d98bbe049177d2c1546b6b0714aa33703ae13d`.

The actual portal Check passes 270 replay constants and all seven
headlines, with matching types, statements imported and no new axioms.
The only warning is the verifier's deprecated `Environment.replay` use.
The three `mfinite` headlines use propext, Classical.choice and Quot.sound;
the remaining four use propext and Quot.sound. This is a local Check
receipt, not an A6 public Lean Verified status.

The notebook has six outputs: the exact 24-entry G16 layer-size list,
True for the kit directory, a LeanEnvironment listing 117 named entries
(94 theorem, 21 def, one inductive, one constructor), seven headline types,
their standard axiom sets, and KernelChecked for 270 declarations. The
117 displayed entries and 270 replay declarations are different counts,
not a contradiction. No Message cells, failed outputs or private local
paths were found. The 15,244 handler events are not 15,244 Message cells.

Portal and notebook child CPU are respectively 195.04 and 187.91 seconds;
supervisors add 1.561 and 1.290 seconds. Wall times are 200.00 and 196.86
seconds. Sampled tree peaks are 2,898,496 and 2,528,432 KiB, process peaks
4 and 5, minimum headroom 4,664 and 4,355 MiB, swap growth zero. These are
Local's M5 measurements and declared launch settings, not Intel runs or
evidence of an aggregate CPU cap from per-process limits alone.

## Required narrow repair

The essay front matter says `Abstract: See abstract.txt.` and the actual
notebook contains **`Cell["See abstract.txt.", "Abstract", ...]`**. Thus the
standalone notebook has a placeholder instead of the cleared abstract.
The external abstract file does not repair that cell.

Local: insert the exact final abstract into the essay and the notebook's
Abstract cell; preserve all input/output cells and the Lean source. A
non-evaluating notebook text-cell repair with exact before/after cell and
source comparisons is sufficient; no repeated proof or tree build is
requested. Update the assembler, essay/driver pins and delivery record so
future builds agree, then supply the changed essay/notebook hashes for a
scoped reread. If changing CL711's optional counts sentence at the same
time, include it explicitly in that delta. L1494 already authorizes
posting once the final pins are cleared.

Record searched: GC2604/2610, L1492–1494, CL711, complete A6 sources and
raw evidence, current kit/portal index completed at 21:08:28Z. This is a
packet review of the existing package, not a fresh priority claim. The
new public A1 status is recorded separately in GC2616. GC2614's exporter
validation remains frozen and unrun. L1495 now supersedes the research
queue: no new work or runs; A6 is the sole remaining delivery. Both
schedules remain unchanged while it is pending, and the halt itself
awaits the owner's confirmation.

My own pull: the discarded forecast that returns as a future input; the
small guarded exporter is preserved for a future owner-authorized
restart. Nothing in that pull outranks the closeout.


## L1496 repaired packet — GC2617, final PASS

**Clearance for Local to post these exact files under L1494.** L1496's
complete changed sources and actual nb2 archive have been read. Cloud's
CL711 confirmation covers the unchanged wording. No further owner word,
proof work or kit PR is requested. A6 is the last delivery under L1495.

| Final item | SHA256 |
|---|---|
| Essay, 36,588 bytes | `8b3803864e86f47d34433345f3a79e8d5066cbfe8fc1024ff62baefe80c19e16` |
| Notebook, 138,515 bytes | `ab978c74b538c33ee70b8ad6b744a8fcb559e46033b2181b7b82be7bf4165d7d` |
| Portal Lean, unchanged | `1e7e7c51a58e684140a4c48c1d962d8bcd259021ed78793b6c91671794b3c977` |
| Abstract, unchanged | `a3a6d68a7e794eb76861c19c56a7f327a70d8b68b1777501b351798e92ac499f` |
| Notebook driver | `ee49d66c9d170401ee7f7223b70f7ee1b19f6cada64b5fb57d5aadb91c0011d2` |
| Essay assembler | `5d1a4f220e56f490cb54bb6048356adb63928ef098b90c209ecfa63f0d73a71a` |

The essay differs from the GC2615 version only by replacing its one
Abstract metadata line with the exact cleared abstract. The archived
essay matches the repository file. The actual notebook has exactly one
Abstract cell, whose decoded text equals the trimmed final abstract;
the placeholder is absent. The assembler now emits that text, and the
driver gates against the final abstract, so the repair is reproducible.

All six notebook Input cells' box expressions are byte-identical to nb1.
Outputs 1–5 are byte-identical, both in the actual notebook and in the
separate output receipts. Output 6 differs only in the temporary module
name: `LeanLinkTmp33690825648058930864x234009`. Normalizing that name gives
an exact match, including the successful 270-declaration KernelCheck.
The iconized source decodes to the unchanged portal Lean hash. There are
zero Message cells, no failed outputs, no sorryAx, and no private local
paths found. The proof scope and seven headline/axiom verdicts of GC2615
therefore remain unchanged. No Intel build or proof replay was performed.

Local chose a full nb2 rebuild. The actual receipt says RESULT OK,
abstract_ok true, six outputs, zero Message cells, 270 replay declarations,
and no reasons for failure. The 15,160 handler events remain distinct
from Message cells. The launcher completed normally, child rc0, with
188.78 seconds wall, child user+system CPU180.92 seconds and supervisor
CPU1.194 seconds. Sampled tree peak2,618,512 KiB, maximum5 processes,
minimum headroom5,576 MiB and swap growth0. Its declared M5 settings are
unchanged from nb1. These are observed measurements, not an inference
that per-process CPU limits enforce an aggregate budget.

Evidence: `cited/l1496-a6/a6-nb2-receipts.tar.gz`,44,006 bytes,
SHA256 `6c7662a370d4327588cca49b572e1b0f6a7f78b161ffae185e70fb68b5f7af56`;
store stat, raw bytes and digest agree. Earlier portal Check evidence
and the source-faithfulness carrying read remain the prerequisites; no
public A6 submission or Lean Verified status is asserted by this clearance.

Next: Local posts the cleared packet; GPT only records the resulting
handoff/outcome and any owner halt instruction. GC2614 remains frozen,
unrun and unavailable for automatic restart. Schedules are unchanged
pending the owner. Last COMPLETE index refresh remains21:08:28Z; this
is a one-line packaging repair to the already searched package.

My own pull: none that outranks completing A6 and the owner's pause.
