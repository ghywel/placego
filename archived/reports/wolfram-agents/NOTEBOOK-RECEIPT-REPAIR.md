# Receipt-only repair for the next notebook (GC2107)

Prepared, UNEXECUTED. No change to the historical universal-start notebook/build/receipt is made or needed.
The public module is Lean Verified; its retained0-byte original JSON and manually accepted notebook remain
historical facts. This repair is for future use before the ring/arc notebooks, not an excuse to rebuild it.

The actual B2 builder directly exported an Association containing non-JSON Wolfram values, including None in
KernelCheck data, and its driver accepted FileExistsQ[summary.json]. The export failed and left0bytes.
Resource provenance also queried an unsupported ReleaseDate property outside the intended per-query Check.

notebook_receipt.wl addresses both causes. It retains the complete raw Wolfram Association, serializes only
JSON-compatible leaves directly, and tags other values by explicit wolfram_inputform rather than silently
calling None Null. It requires a nonempty parsed Association and exact file/serialized-JSON round trip. It
refuses overwrite. nrResourceMetadata queries only Name/Version/UUID, each inside the actual Check, without
ReleaseDate. This operates on trusted build metadata; it is not an evaluator of untrusted notebook boxes.
No resource or LeanLink call occurs when loading the helper or running the controls.

## Frozen small control stage for Local's review, after other allocations are idle

Question: can the actual problematic nested None and optional metadata be retained faithfully while empty,
malformed or structurally invalid JSON is rejected before a notebook driver can report success?
Prediction: all14 named fixture checks pass, retaining exact raw data and a parsed positive JSON receipt.
Counterfactual: any false result, message/resource failure, cap/pressure stop or leftover process ends this
ONE stage and is retained. No notebook/converter/Lean/compiler/dependency build, network fetch or auto retry.
Record searched: actual B2 builder/driver/output checks, GC2098 final artifact review, original failed JSON
and the existing17 non-building output fixtures. This is an implementation correction, not a research claim.

Pins:
- notebook_receipt.wl:4c6301c0d16cba03c03ba141da3afd827d1c5f777f4ea1cefbb8166e862b11e7
- notebook_receipt_control.wl:b24543a2cb722272cbc5da100da477f3fc7b44783c32106cafee852cbda470ae
- launcher notebook_receipt_control_launch.py SHA25691a3836e761873198b1d3f1a5f73e6915c50cdf764fab75a845abafcfd68ee71 verifies/copies both into fresh CAPPED_OUT/src, sets the kernel's
  temp root inside CAPPED_OUT/tmp and execs the already installed bare kernel. The fixture checks the actual
  temporary directory. No Wolfram MCP attach or existing owner kernel is used.

One Local run_capped.py stage: --track-tree --max-procs4, CPU30s PER PROCESS,60s stage wall,2048MiB sampled
owned RSS,8MiB/file,16MiB total outputs,3072MiB launch/1024MiB ongoing free+inactive,128MiB swap-growth stop.
No other Lean/kernel/compute allocation. Command after the usual fresh supervisor destination/options:
python3 tests/probes/wolfram/notebook_receipt_control_launch.py EXISTING_KERNEL. No private kernel path is
committed. Expected2 workload lifetimes (launcher execs kernel, plus optional time wrapper), nominal60 CPU
seconds across inherited limits, not an aggregate30s cap. Report actual process/lifetime/time/pressure facts.
No owner session is closed to pass a gate. Retain raw stdout,14 results, summary.raw.wl, parsed summary.json,
negative fixture files and supervisor/time receipts. Core ring/arc proof checks take priority; serialize jobs.

After success, the actual FUTURE notebook builder must call nrWriteReceipt and treat a Failure as a failure;
its driver must require nrReceiptFileOK with required output/axiom/kernel/reasons keys, and confirm reasons
are empty and checks true. The actual builder must also use the checked provenance function and retain raw
summary/message data, including any unavailable metadata. Merely adding this helper or passing its fixtures
does not establish that a future builder has adopted it: that exact integration/source needs review/freeze
with the new notebook's output-specific guards. No new notebook stage is authorized by this fixture plan.

## GC2111 / L1133: the14 pure controls passed

Complete compact producer receipt independently read. Pinned helper/control/launcher matched; COMPLETED4.26s,
295696KiB sampled owned RSS,2 processes,min headroom6437MiB, no swap growth/residual process reported. All14
positive/adversarial results are true, including exact raw data and explicit None/Missing/fraction tags.
Receipt: receipts/local-gc2107-receipt-controls.json. This validates the helper's pure fixture behavior, not
its integration into either future notebook. The exact arc driver now integrates it under GC2110; actual
notebook execution and manual artifact/source read remain pending.
