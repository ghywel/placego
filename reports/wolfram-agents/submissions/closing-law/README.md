# The closing law of prefix doublings (NIGHT-TASKS A3) — delivery record

Local, 3 November 2026 (L1406, L1408, L1410, L1411). **Status: PREPARED, not posted.** Posting waits for the owner's word.

## Statement

The kit's gate clocks (`Rule30GateClocks`), any gate family with a quadratic term (Rule 30's OR included), any seed.
Headlines of `Rule30Submission.lean`:

| Headline | Says |
|---|---|
| `order_countdown_exact` | s with period M = 2^v ≥ 2, b antiperiodic at M, h(t+1) = h t xor g(b t)(s t), g quadratic, h with period 2M and order s M + 1 < M: order h (2M) + 1 = order s M |
| `closing_law` | after a doubling at exponent E, m ≥ 0 pairs 10 and a doubling: m + 1 ≤ 2^E, and the next column doubles iff m + 1 = 2^E |
| `closing_law_or` | the same for Rule 30's OR |
| `no_1101011` | the doubling word 1(10)²11 never occurs |
| `five_letter` | prefixExp n ≥ 2 implies prefixExp (n + 5) ≤ prefixExp n + 3 |

## Checks

- Source `Rule30Submission.lean`: 331 lines, SHA256 `10812b8961b062c98656c12a1be52a87c44269ae60e22096311a405dd5c69a94`. It is built by
  `tests/probes/wolfram/make_closing_law_submission.py` from `tests/probes/lean/ClosingLaw.lean` (cdf38552…), which
  GPT reviewed for source fidelity (GC2510, PASS).
- The kit's unchanged `Check.lean` on the verifier kit 93d98bbe, whose GateClocks, DifferenceOrder and RecordCharge
  are identical to main c42f6e51, gives **verdict pass**:
  - replay OK over 97 constants;
  - no new axioms;
  - five headlines found and ok, each with propext, Classical.choice and Quot.sound only;
  - 18 declarations, all on standard axioms;
  - the statement module is imported.
- `lake build Rule30Submission` took 0.6 s. The raw Check output is kept outside git, SHA256 `fdf966cf9cc280b2a7af14943593172dab91c5f8c07058a5d670ee147e9bda17`.
- Scalar replay: `tests/probes/closing_law_replay.py` (0 violations over 2,158 occurrences; 0 of 4,743 five-letter
  windows exceed three doublings).

## Prior art and credit

- **Hand mechanisms.** GC2008's Newton countdown (read in L1195). The closing composition: GPT's GC2197 and GC2201,
  Cloud's CL645, and GC2205.
- **PR #55** (head 918284e3) already formalizes OR's no-11011 for E ≥ 2. PR #55 uses the "≤" countdown.
- **The kit's** `order_countdown` and `order_countdown_gate` give the "≤" direction.
- **Rowland 2006 §5** is related literature.
- **Not found in the kit main or the portal:** the exact countdown and the all-m closing law. This is a scoped index
  and source comparison, not a priority clearance.

## Essay and notebook (L1413)

- `essay-prose.md` SHA256 `cfa9c4df…` and `abstract.txt` (252 words). `essay.md` is assembled by
  `tests/probes/wolfram/assemble_closing_law_essay.py`, with both inputs pinned; its SHA256 is `f1a7dad6…`.
- The essay's Wolfram cell computes the single cell's letters, `0101101101000001100000`, and five runs. It agrees
  with `closing_law_replay.py`.
- **Release notebook: RESULT OK** (`tests/probes/wolfram/closing_law_notebook.wl`, driver SHA256 `a9b5b4bc…`,
  built from the verifier kit 93d98bbe in 24 s).
  - Seven outputs, no message cells. The Lean source is in an icon, the kit cell is True and a LeanEnvironment is
    present.
  - All five headlines carry propext, Classical.choice and Quot.sound only.
  - KernelChecked over 97 declarations, the same count the official check replayed.
  - No local paths. Notebook SHA256 `2509ad98a922349a3474bcd032db08d2599fa4628096854ce98dd445a5b825ab`, 103,202
    bytes, kept outside git with its receipts.

## Left to do

GPT's read of the packet, then the owner's word before posting.
