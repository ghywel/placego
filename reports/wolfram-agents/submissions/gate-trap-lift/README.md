# The gate trap at eighteen columns (queue row S-16)

**PROOF/TEXT REVIEW PASS (GC2801); not posted.** Built at the owner's word ("Yes, build S-16") as the width18 rung. The corrected essay requires nb2; nb1 is stale. Technical clearance is conditional only on the reviewed routine nb2 gates below; no further mathematics review is required. The kit PR follows posting.

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


## GPT release review — GC2801

**CONDITIONAL POSTING CLEARANCE: proof and corrected text PASS; refreshed notebook required.** All new Lean logic and the seven
headlines were read. An independent literal-cell oracle checks all3316lift windows/13264edges, every4644 listed
certificate-window occurrence, all28 layers (752starts, final empty) and all three witness paths. The generator
reproduces BOTH Lean forms byte-for-byte. Their new bodies match, and the portal carries the reviewed S15 body
verbatim. Both Check receipts pass, all declarations use standard axioms, and422/202 constants replay. Proof
bytes remain unchanged: portal13c3896f…/kit49ff0df8…. No new Intel Lean or Wolfram execution is claimed.

Fresh known-find completed9November22:44UTC: kit03a19bf6240b63c6d15894c5f7552f3a6091d937, portal22:44:25Z,13openPRs.
S15 is byte-identical on kit main; closedPR246's comments/reviews are empty. Lee60990f's pool hypothesis and exact
source were checked; the whole black lift is not contained in that pool (441of752 overlap), so it does not
already state this full-trap result. The linked gate-census primary source was read. Kit patch applies to main.

The old nb1's actual serialized icon source, title, old abstract, all six outputs, worked-number table, seven
headlines and KernelChecked422 metadata were independently inspected and agree with its receipts. It is now
STALE because the release text was corrected: non-SFT only at checked24/26/28, conditional entropy log₂λ rather
than λ, and no universal construction-impossibility claim from selected control observations. The corrected
abstract is183words. `post.sh --dry` with nb1 correctly rejects the changed abstract. Do not merely repin nb1.

**Local's only remaining artifact action:** rebuild the corrected essay, update notebook/abstract/essay pins
together, run the existing gates/dry check and share the new nb2 bundle/digest. Expected current essay SHA256
`1a1efa4f5f81f44ee6884709a9ce6fd7fd743fd4c7f009d23718a9954a3345f0`; abstract
`2a86eeba68e88e064270bb5a225ea0c0b2ae0b6e221574db71ca466c4c9d212a`. Local may complete the release under the owner's posting authorization once the following routine gates pass;
no additional GPT approval is required for these exact bytes. This is a Wolfram notebook refresh on Local's host,
as TOOLS§4 requires.

**GPT evidence:** shared store `cited/gc2801-s16-release-review-20261109.tar.gz`,52files/174603bytes, SHA256 `4dbe623ce96b198d49dccdd8c20562b3e48eff92ac14f63c109d28b8dc3d8b86`, verifiedTLS/raw-body exact readback; private paths normalized with raw/stored hashes. Original nb1 remains in Local's cited2cb327f3… bundle.

### Reviewed routine release gates

Build nb2 from the exact essay/abstract hashes above, with unchanged portal source
`13c3896fe5a24da72f25fe2f1c9711e4a9db9499990c46d7f77ed46bfcbade5f`. Use the unchanged reviewed notebook driver
`6908ffb878e649ff27cb18a1e33c3b6c6ccb28671e51cf29f962005c11f8dbbe` under the standing capped-run controls.
Its RESULT OK must confirm all six outputs, exact source/abstract, worked numbers, seven axiom sets and
KernelChecked422. The receipt must name the corrected essay hash and the actual new notebook hash.
Update ONLY the notebook/abstract/essay hashes in the reviewed post wrapper, retaining the other pins and
verifier guard. Its fresh --dry must pass at5fb59158/image18. Those successful gates complete this conditional
technical clearance; if source, driver, headlines, verifier or other wrapper logic changes, return for review.
The new notebook is not yet built or inspected by GPT, and no posting is claimed here. Never merely repin nb1.
