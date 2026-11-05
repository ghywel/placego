#!/usr/bin/env python3
"""SW-02 smoke tasks (design section 7). SM-A reader on a small locus (default model), SM-B librarian on Fable through the queue
and the web, SM-C screener on four planted claims with known answers, SM-M1/M2 mock tasks for the resume control."""
from build_common import *

A = """# SW-02 task {{ID}}: smoke reader

**Role.** A reader on a small locus, to prove the tools. Read `{{KIT}}/lean/Ruliology/CellularAutomata/Rule30GateTrap.lean`, the definitions of `Q01Gap` and `u_empty_gaps`
in particular. Run `python3 {{REC}}/tests/probes/record_find.py Q01Gap --offline`. Then write in your folder: `report.md` (150 words on what the module proves and leaves
open) and `doors.jsonl` with exactly one line, a JSON object with fields `door`, `route`, `target`, `claimed_status`, `source`, `closure_kind`, `scope`, `reopen`, `aliases`,
`verdict`, `next_test`, `cost`, `info`, for the door 'Q01Gap gives CQ01Empty'. Then run, through the queue, a script in your folder that imports `ref` and prints
`ref.u(0, 160)[146:160]`. Paste the printed line into `report.md`. Budget: 15 tool calls.
"""

B = """# SW-02 task {{ID}}: smoke librarian

**Role.** A librarian on a small locus, to prove the web tools, the Fable model and the queue. Load `WebSearch` and `WebFetch` with ToolSearch (`select:WebSearch,WebFetch`). Find the arXiv
abstract page of Condrey's preprint arXiv:2609.09431 and read it. Write in your folder `sources.jsonl` with one line: `cite`, `url`, `read`, `theorems`, `applies_if`, `obstacle`, `for`,
`in_record`. Also write `model.txt` saying which model you are, as far as you know. Then run through the queue a script in your folder that prints `sum(ref.center(1000))`, and put that number
in `report.md` with two sentences on the paper. Budget: 15 tool calls.
"""

C = """# SW-02 task {{ID}}: smoke screener (planted controls)

**Role.** A gate and statement screener. Read `{{SW}}/TERMS.md`. Four claims follow, each as an attack agent might report it. For each, compare the title, the quantified statement, the proof and
the intended target, and classify it as KNOWN (cite the matching kit theorem or record name), REFUTED (give the witness), UNJUSTIFIED (name the missing step), INCONCLUSIVE, OUT OF SCOPE or
CANDIDATE (a valid statement that deserves a skeptic). A theorem gate rejection must name the matched hypotheses. Use the queue for any small test. Write `screen.jsonl` in your folder, one line
per claim, with `claim`, `class`, `reason`, `cite_or_witness`.

**Claim 1, 'The Outward Creep Lemma' (new).** In the zero-boundary half-row, the leftmost black cell of any nonzero row moves out by exactly one depth at every tick. Proof: at depth m + 1 above the
top cell the update reads 0 xor (0 or 1) = 1, and above that all is white.

**Claim 2, 'Lowest-difference exclusion'.** Let Y, Y' be distinct naturals whose lowest differing bit is i. Then bit 0 of F^i(Y) and of F^i(Y') differ. Hence for every i at most one of Y, Y' can survive
through tick i, so every two survivors through tick t have their lowest differing bit above t.

**Claim 3, 'Linear death'.** D(W) < 2W at every width where D(W) is known exactly, and at every width up to 76 the lower bounds also stay below 2W. Hence D(W) < 2W for all W, and so S_W(2W) = 0 for
all W, which proves Q01.

**Claim 4, 'Second survival law'.** For every natural Y with Y odd and G(Y) odd, G(G(Y)) is odd if and only if bits 1 and 4 of Y differ. Proof: expand bit 0 of G(G(Y)) in the bits of Y, using that G(Y) odd
means bits 1 and 2 differ. No claim about Q01 is made.

Budget: 25 tool calls.
"""

M1 = """# SW-02 task {{ID}}: mock

Run exactly this shell command once, then return the manifest with outcome complete and files empty:

    echo ran >> {{DATA}}/out/SM-M/counter-{{ID}}.txt

Do nothing else.
"""

M2 = """# SW-02 task {{ID}}: mock

Run exactly this shell command once, then wait for it, then return the manifest with outcome complete and files empty:

    echo started >> {{DATA}}/out/SM-M/counter-{{ID}}.txt; sleep 100; echo finished >> {{DATA}}/out/SM-M/counter-{{ID}}.txt

Do nothing else.
"""

os.makedirs(os.path.join(DATA, "out", "SM-M"), exist_ok=True)
write_task("SM-A", A, REC_PRE)
write_task("SM-B", B, REC_PRE)
write_task("SM-C", C, REC_PRE)
write_task("SM-M1", M1, REC_PRE)
write_task("SM-M2", M2, REC_PRE)
write_batch("smoke", [{"id": "SM-A", "effort": "high"}, {"id": "SM-B", "model": "fable", "effort": "high"}, {"id": "SM-C", "effort": "medium"}], 3)
write_batch("smoke-resume", [{"id": "SM-M1", "model": "haiku", "effort": "low"}, {"id": "SM-M2", "model": "haiku", "effort": "low"}], 1)
print("ok")
