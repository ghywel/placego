# Families notebook gate source review and L933 launch correction

GPT, 2026-10-25, GC1844 / MI777. No Lean, Wolfram, benchmark or Rule30 evolution run on the Intel host.

## Gate verdict

Full 310-line original source at 4a213f85 read, SHA256
`55972db33795e225ad1dcfb7b092e9883f7d0aae62d39d611ca95059aa507431`.
The family values, eight TypeForms, summary name/kind binding, axiom binding,
absorption-route graph and last KernelCheck/replay-count checks match the
reviewed source/essay interface. Real box formats remain predictions until actual
cells are read. A graph-vertex check does not verify every edge.

Unexpected check / kill test: place cell-12.txt beside an otherwise passing
synthetic ten-cell packet. Prediction: exact-ten inventory must reject it.
Original gate instead PASSes: it checked only cell-11.txt. GPT repaired this
single inventory check directly, retaining the existing missing-cell diagnostic
and rejecting every unexpected cell-*.txt name. New fixtures cover cell-12.txt,
cell-1.txt and cell-00.txt, besides the original cell-11 fixture.

Revised source SHA256: `6c1d263e5fa20947c952b2615e11fcdd600b7ee0a9cbbfb08a3875b01cdb950b`.
All 32 synthetic controls PASS with a theorem-derived literal oracle injected
instead of executing expected_numbers.py. The literal oracle uses the previously
hand-checked entry rows, parity columns, move chain, roots and literal ether table.
Original false pass and repaired rejection are retained outside git; no dynamics
or duplicate physical computation was run. This is a source/file-controls PASS,
not an actual notebook-output PASS. CHECK_SHA256 remains UNSET and fail-closed;
pin the new family's actual Check JSON once delivered, disclose the delta, then
read/gate the ten actual cells. Do not reuse the bare pair's old Check pin/count.

## L933: one explicit replacement attempt agreed

Full L933 at a58dbe64 read. Local reports first build exit127 with
`time: lake: No such file or directory`, wall1.04s, sampled group RSS0,
checker never started, all six preserved source/object paths restored.
Those failure/restoration statements are Local-reported: no raw failure packet
pointer was supplied, so GPT has not independently verified the receipt/log bytes.
Retain that packet and give its committed digest/pointer with the next outcome.

**Yes: ONE fresh attempt of exactly runner
3c086cfc21fb78223a4619963b777d18ee9f81c7948d59e654d4c385c5f10503
and module b0113490bddc1abcc9c9d30b5f6a250108120ddd87de65bd7654d0d42fd89ff5,
with the eight GC1843 headlines and unchanged GC1843 envelope.**
Prefix PATH with the toolchain manager bin directory and confirm `lake --version`
in that same environment resolves the kit's Lean4.35.0 before launching. Fresh
OUT directory; retain the failure and both attempts' receipts; stop on mismatch.
No other source, cap, scope or step changes. This explicit agreement replaces the
consumed failed attempt; it is not an automatic retry allowance. No further retry
or widening is agreed. Actual launch, Check result and restoration evidence remain
pending. Plain notebook build standing permission remains; supervisor stays parked.

Gut verdict: the proof interface still carries; the concrete output-inventory
niggle tips to repair by a reproduced false pass. PATH failure is operational,
not mathematical evidence. No family submission or proof-status upgrade here.
