# The gate trap at eighteen columns (queue row S-16)

**BUILT, not posted (L1617, 9 November 2026).** Built at the owner's word ("Yes, build S-16") as the width-18 rung of the S-16 line (L1608–L1614). Posting needs GPT's release review and the owner's word. The kit PR follows posting.

## What the module proves

`Rule30GateTrapLift` (core Lean). The kit form imports only `Rule30GateTrapWords` (kit main `0444830`). The portal form carries S-15's reviewed source verbatim, because the verifier's kit `5fb59158` predates it.
- `win18_eq`, `win18_step2`: the 18-column window is the trap's window plus the columns 17 and 18, and moves by the kit's `step2` with column 19 free. So the lift is closed and every trapped right half stays in it.
- `no_3535353_of_entry`: after entry, `u R` never reads `3535353`, for every right half that enters the trap.
- `trap_reads_3535353`: an explicit path of the 16-column trap graph reads it, so the trap alone cannot exclude it.
- `lift_minimal_paths`: it is minimal for the lift (`353535`, `535353` read along explicit lift paths).
- `Q01GapCore` (open) = `Q01GapWords` plus `3535353`. It is the formal version of CP-2.2's `Q01Core`, with `Q01GapCore_of_Q01GapWords`, `not_finSupp_Psi_of_Q01GapCore` and `CQ01Empty_of_Q01GapCore`.

Method: S-15's. The path sets of `3535353` in the lift from all 752 black lift windows are data: layers of 752, 589, 563, 176, …, 58 and 0 windows, 4,644 in all. One kernel check per sample and per chunk of at most 192 windows. Without chunking, peak memory was 3.54 GB; with it, 1.49 GB.

| Form | File | sha256 | Check |
|---|---|---|---|
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean) | `13c3896fe5a24da7…` | pass at the verifier's kit `5fb59158`: 288 declared, 422 constants replayed, 7 headlines, standard axioms, no new axioms; 58.5 s, 1.78 GB ([receipt](check-5fb59158.json)) |
| Kit | [`Rule30GateTrapLift.lean`](Rule30GateTrapLift.lean) | `49ff0df86a850a6a…` | pass at kit main `03a19bf`: 136 declared, 202 constants, 7 headlines; builds in 38 s, 1.22 GB ([receipt](check-kit-03a19bf.json)); local kit branch `gate-trap-lift` at `eef9432`, not pushed; [`kit-integration.patch`](kit-integration.patch) |

**Mutants.** All seven must-fail mutants rejected: dropped windows in a first-layer chunk and in a middle layer, a white start, a missing final layer, a shifted layer, a wrong-colour start for the 16-column path, a start window outside the trap ([output](../../../../tests/probes/swarm/sw02/block3/mutate_trap_lift.out), [script](../../../../tests/probes/swarm/sw02/block3/mutate_trap_lift.py)).

**Notebook nb1** (`~/placego-data/s16/nb1`, outside git): SHA256 `3e04dd81e581b9cd73f9f4287945e367807b3fc93963a338fb92081e3eee5166`, 356,383 bytes, RESULT OK in 148.8 s, 2.1 GB. Every gate passes: 6 output cells, no message cells; the first cell equals the Python replay; the Abstract cell equals `abstract.txt`; the icon payload equals the portal source; the axioms match `Check`; KernelChecked at 422. Evidence: `cited/local/gate-trap-lift-nb1-20261109.tar.gz`, 102,265 bytes, SHA256 `2cb327f39fa8ea3f17fcd8fb541bcb4e72b8ccb50ba4299d1d332bfb41d1388f` (read back byte-exact)

**Post script.** [`post.sh`](post.sh) is S-15's GPT-reviewed wrapper (GC2791), with only the pins and the headline count changed. Dry run passes: seven pins, verifier `5fb59158`, image 18.

## Texts and tools

[`essay-prose.md`](essay-prose.md) and [`essay.md`](essay.md), assembled by [`assemble_gate_trap_lift_essay.py`](../../../../tests/probes/wolfram/assemble_gate_trap_lift_essay.py); [`title.txt`](title.txt); [`abstract.txt`](abstract.txt) (194 words, one line); [`headlines.txt`](headlines.txt) (7); [`PR-BODY.md`](PR-BODY.md). The generator [`gen_trap_lift.py`](../../../../tests/probes/swarm/sw02/block3/gen_trap_lift.py) writes both Lean forms from the kit's trap codes and S-15's portal source. The notebook driver [`gate_trap_lift_notebook.wl`](../../../../tests/probes/wolfram/gate_trap_lift_notebook.wl) is checked against [`gate_trap_lift_replay.py`](../../../../tests/probes/wolfram/gate_trap_lift_replay.py); the Wolfram cell and the replay agree byte for byte.

## Prior art and scope

- Kit `Rule30GateTrap` (Bosdure) and `Rule30GateTrapWords` (ours, S-15).
- Lee's R30-20261030-60990f: `33`, `3553`, `3535353` at every index for the trajectories of an 18-cell invariant pool, including the one-cell seed. The premise differs: entry into the kit's whole trap.
- Our CP-2.2 found `3535353`'s absence in the trap by computation and named `Q01Core`.

The essay's §4 carries the S-16 research as context, each item with its status: exact long-run languages to width 30; not of finite type at the checked widths24/26/28; G1′ ⇔ code inclusion; the conditional floor log₂λ≈0.099056147. The uncarried control conclusion and finite-SAT sidebar are omitted from the release essay. None of it is in the Lean.

**Risk to watch:** the portal `Check` takes about a minute on the M5, and the verifier allows four minutes on its cloud host.
