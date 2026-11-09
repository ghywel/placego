# The gap words of the gate trap (the trap lemma; queue row S-15)

**RELEASE REVIEW PASS, not posted (GPT GC2791, 9 November 2026).** Mathematics reviewed (GC2789), scope fixed at five words (owner, L1609). Started at the owner's word from Cloud's CL759 recommendation: GPT's
trap lemma (GC2775: inside the kit's gate trap the gap word `3353` has no path, so no `33535555` begins after entry),
carried by Cloud's replay (CL758). Local's third replay found that the trap forbids more, and the packet states the
whole list. GPT's source read and independent finite audit pass after the prose corrections below. The release artifacts are
built and reviewed (below). Local posts the pinned package after the owner's word, using the reviewed wrapper.

## What the module proves

`Rule30GateTrapWords` (core Lean, imports only `Rule30GateTrap`). For every right half `R` whose window enters the
kit's 829-window trap at an odd time `t0`, and every step `s` with `t0 ≤ 2 s + 1`:
- `gap_words_of_entry`: `u R` reads none of the gap words `333`, `3353`, `3533`, `3553`, `5533` from `s`;
  `no_3353_of_entry` is GPT's word alone; `no_33535555_of_entry` follows.
- `no_late_33`: after any two gaps the next two are not both `3` (with `gaps_of_entry`: from the third black cell
  after entry, no `33`; no `3553` anywhere after entry).
- `minimal_paths`: each word is minimal for the relaxed trap graph (its six maximal proper factors have explicit paths).
  This does not prove physical realization of those paths.
- `Q01GapWords` (open), `Q01GapWords_of_Q01Gap`, `not_finSupp_Psi_of_Q01GapWords`, `CQ01Empty_of_Q01GapWords`:
  the kit's `Q01Gap` weakens to a statement about fewer free-bit sequences (0.132 against 0.256 bit per sample) with
  the same consequences for trapped right halves.

Method: the kit's own (trap codes, `step2`, `allSucc`, `win_next`, `win_mem_trap`). Path-set layers for the five words
are data in a trie, 40 layers, one start check and 44 step checks, each its own `decide +kernel` so that the kernel's
caches stay small; a bitmap from the codes (`maskN`) and `decode (encList w) = w` carry membership.

| Form | File | sha256 | Check |
|---|---|---|---|
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean) (895 lines) | `82d0eb9ec399eb03…` | pass at the verifier's kit `5fb59158`: 152 declared, 239 constants replayed, 9 headlines, standard axioms, no new axioms ([receipt](check-5fb59158.json)); receipt read by GPT, not rebuilt on Intel |
| Kit | [`Rule30GateTrapWords.lean`](Rule30GateTrapWords.lean) (898 lines) | `63f0387527521292…` | builds at `5fb59158` (28 s, 1.04 GB); Local build and `Check` pass at main `8d252e19`: 148 declared, 240 replayed, 9 headlines ([receipt](check-kit-8d252e1.json)) |

Build cost (portal form, M5, under `run_capped` with an 8 GiB cap): 27 s, 1.22 GB peak. The first single-check design
took 32 s and 3.6 GB; a `List.contains` design took 125 s and 7.7 GB (kernel `decEq` on `Nat`); both were dropped.

**Mutants** ([output](../../../../tests/probes/swarm/sw02/block3/mutate_trap_words.out), script
[`mutate_trap_words.py`](../../../../tests/probes/swarm/sw02/block3/mutate_trap_words.py)): eight must-fail mutants
rejected (a dropped window in a middle layer and in the shared first layer, a claimed allowed word, a white start, a
shifted layer, a missing final layer, a start window with the wrong column 1, a start window outside the trap). M4,
one flipped column-17 value early in a witness path, was ACCEPTED: it still reads the same short word, consistently
with the propagation distance. Kept as found; not a must-fail mutant. M2's rejection is a word-expansion/type error
before the layer check, so it is not an independent test of the final-transition check.

## Computations (COMPUTED, own code, three implementations)

- [`local_trap_lemma.py`](../../../../tests/probes/swarm/sw02/block3/local_trap_lemma.py)
  ([output](../../../../tests/probes/swarm/sw02/block3/local_trap_lemma.out)): third replay of GC2775 (closure 3,316
  of 3,316, the `3353` layers 188 … 41, 0 to the digit). P2's counterfactual happened: the shortest forbidden word is
  `333`; minimal forbidden words up to 14 gaps are the five; the trap's gap language equals the shift of finite type
  with those five (product automaton, 19 states, no disagreement); white runs at most 4.
- [`local_trap_lemma_w18.py`](../../../../tests/probes/swarm/sw02/block3/local_trap_lemma_w18.py)
  ([output](../../../../tests/probes/swarm/sw02/block3/local_trap_lemma_w18.out)): the trap lifted to 18 columns
  (3,316 windows, closed, a right half in the trap is in the lift) kills `3535353`, the only addition up to 14 gaps;
  the 16-column graph reads it.
- [`gate_trap_words_replay.py`](../../../../tests/probes/wolfram/gate_trap_words_replay.py) and the essay's Wolfram cell
  agree byte for byte (Wolfram Engine, 5.3 s).

## Prior art (changes the framing)

- Kit `Rule30GateTrap` (Bosdure, R30-20261027-230bc7): the trap, `gaps_of_entry`, `Q01Gap`.
- **R30-20261030-60990f (J. Lee):** the R1 headline follows from the general Lean theorem
  `Wolfram30.Inv34.relaxed_no_forbidden_factor`, for every relaxed trajectory in an invariant 18-cell pool of
  2,040 states: no `33`, `3553`, `3535353`. `33` and `3553` are credited to the authors' earlier work.
- **Our record:** SW02-RESULTS CP-2.2 (COMPUTED, 6 November): inside the kit's trap, for every R, `33` at most once,
  no `3553`, no `3535353` (18 columns), tail entropy at most 0.12707. Its `Q01Core` uses all three eventual
  exclusions; `Q01GapWords` formalizes only the 16-column restriction and is not the same definition. CP-2.2 also
  checked that the 2,024-window recurrent core of the lift lies in Lee's pool. GC706/GC1087's synchronized
  `S = 110100`, `L = 1101000100` sample to gaps 3/5 at the white phase: `SS` means `33` under those guards,
  but their guarded-core entry is not identified with the whole kit trap.
- rule30-open: a counter-augmented gap trap with 3,562 black-entry windows; kit windows embed with a counter,
  reaching its entry set by the next black sample, not by bare-set inclusion. Kit `Rule30PeriodTwoWidth13`
  (R30-20261109-62afca): nine pairs, all four pairs over 3 and 5 allowed.

Contribution relative to these: the list in Lean under the whole kit-trap entry premise, including the transient
where a `33` can occur; graph minimality with explicit paths; separately computed completeness for the 16-column
graph; and `Q01GapWords` with its conditional reductions. Entropy is that of the relaxed word class, not an exact
entropy claim for physical histories.

## Scope: fixed at the owner's word (L1609)

Five words now; the 18-column language is the follow-up, queue row S-16. GPT (GC2789) and Cloud (CL760) both
recommended this, and the owner adopted it. `3535353` is excluded for every trapped right half by the 18-column lift:
COMPUTED by three implementations (Local L1608, GPT GC2789, Cloud CL760), where the 16-column graph keeps `47`
windows at the word's last sample. The essay now says so and names the 18-column language as the next module
(Cloud's condition (a)). S-16's content is fixed in the queue (Cloud's condition (b)): measure its `Check` cost first,
then the lift's minimal forbidden words and completeness beyond 14 gaps, as a separate module; the transient `33`
after entry stays, so it would not give `33` excluded at every index.

## Release artifacts (L1609)

- **Essay** `c7e5ff77…` from GPT's repaired prose plus Cloud's condition (a); internal ledger labels removed from the
  public text. Abstract `16fd84df…` (184 words, one canonical line).
- **Notebook nb1** (`~/placego-data/s15/nb1`, outside git): SHA256
  `bd1ccc543ac188881dd2da44009f6514ec075346822ca5198a1282f8a64508d7`, 235,257 bytes, RESULT OK in 70.3 s, 2.2 GB peak.
  Every gate passes: 6 output cells, no message cells; the first cell equals the Python replay; the Abstract cell
  equals `abstract.txt`; the icon payload equals the portal source; the axiom sets match `Check`; KernelChecked at
  239 declarations. Driver `gate_trap_words_notebook.wl` `4be32356…`.
- **Post script** `post.sh` (outside git) pins the notebook, portal source, abstract, title, essay and headlines, and
  refuses unless the verifier is kit `5fb59158`, image 18. `post.sh --dry` passes.
- **Kit form at current kit main** `8d252e19`: byte-identical module (`63f03875…`) in the local kit branch `trap-words`
  (commit `33061a5`, not pushed), with the import line after `Rule30PeriodThreeLanguage` and the catalogue row after
  `Rule30SidewaysLocks` ([`kit-integration.patch`](kit-integration.patch); its `PORTAL-ID` is filled in after posting).
  It builds clean (the module 26 s; 11 changed dependencies rebuilt, 3.3 GB peak from the trap's certificate module),
  and `Check` passes there: 148 declared, 240 constants replayed, 9 headlines, standard axioms, no new axioms
  ([receipt](check-kit-8d252e1.json)). The full catalogue build was not run.
- **Shared store:** notebook, receipts, both `Check` receipts, pins and dry run in
  `cited/local/gate-trap-words-nb1-20261109.tar.gz`, 67,046 bytes, SHA256
  `f3857359a4159460e54ea4f4e78fec9632aa433e883f6d132fb402eda706eb80` (local paths normalised; read back byte-exact).

**Next:** the owner's posting word, then Local uses the reviewed [post.sh](post.sh) on the exact nb1 file. Fill the actual portal ID into the corrected integration patch and refresh the kit PR against current main after posting. GC2791 below completes the artifact read.

## Texts and tools

[`essay-prose.md`](essay-prose.md) and [`essay.md`](essay.md) (assembled by
[`assemble_gate_trap_words_essay.py`](../../../../tests/probes/wolfram/assemble_gate_trap_words_essay.py)),
[`title.txt`](title.txt), [`abstract.txt`](abstract.txt), [`headlines.txt`](headlines.txt) (9). The generator
[`gen_trap_words.py`](../../../../tests/probes/swarm/sw02/block3/gen_trap_words.py) writes both Lean forms from the
kit's trap codes; the notebook driver is
[`gate_trap_words_notebook.wl`](../../../../tests/probes/wolfram/gate_trap_words_notebook.wl), checked against
[`gate_trap_words_replay.py`](../../../../tests/probes/wolfram/gate_trap_words_replay.py).


## GPT draft review — GC2789

**PASS for the mathematics and corrected draft; not yet a release clearance.** The Lean proof files are unchanged.
GPT read the checker, physical-window transfer and conditional reductions, checked the portal/kit namespace
conversion, and independently replayed every numeric layer and witness. In particular, `startOK` covers every
possible black trap window; `stepOK` admits all four temporal values of column 17; `win_next` uses the actual
values of a history; and the odd-time/entry inequalities are retained. The last empty layer therefore excludes
the word for every right half satisfying the stated entry premise. The complement in `Psi_free` has the correct
orientation in the Q01GapWords reduction. The source read also carries Local's proposed substitution in the
current kit's `CQ01_of_RD_of_Q01Gap`: its trap branch can use the new theorem, with the periodic branch unchanged.
That corollary remains a hand specialization, not an additional compiled headline in this packet.

**Independent Intel audit, COMPUTED:** the literal Rule 30 truth table agrees on all 3,316 trap edges; all 40
nonempty layers and 44 step checks match exactly; all six proper-factor paths pass; the product-automaton
comparison visits 19 pairs with no disagreement. The already-proposed 18-column control has 3,316 windows and is
closed: `3535353` leaves 47 windows at width16 and none at width18. Missing-start and wrong-phase negative controls
are rejected. No wider enumeration was run. Source:
[`gpt_trap_words_review.py`](../../../../tests/probes/swarm/sw02/block3/gpt_trap_words_review.py).
The frozen audit completed in 0.571872 aggregate CPU seconds and 0.54 wall seconds. It finished before a periodic
RSS sample; the launcher's zero sampled maxima are not a measured zero-memory result. Local's Lean `Check` and
mutant receipts were read, not rerun on Intel; no Wolfram run was performed by GPT.

**Corrections made:** Lee's general pool theorem is credited; `Q01Core` is distinguished from `Q01GapWords`;
graph completeness/minimality and entropy are separated from physical realizability; the transient `33` is kept;
GC1087's `SS` identification is answered with its synchronization/core guards. The measured entry percentages now
say entry during the E block and identify the free odd-time initial-row convention. The abstract is a canonical
184-word line, with an assembler assertion matching the notebook driver's literal comparison; the previous
multiline file would disagree with the assembler's collapsed form. The implication from the still-open hypothesis
is explicit. The corrected assembled essay embeds the unchanged portal source byte for byte.

Reviewed source SHA256:

- kit form: `63f0387527521292ebccd92aff9bf6c809abc4ef3bd0c668d933380bd43ce642`;
- portal form: `82d0eb9ec399eb035eef3f4eb7b18649e1a4f5bdecc0f0285a35af510e873e06`;
- corrected essay: `652aea0563c494f969d5a9c72d3c5d5e54b5031c0e8d382bfab73c2c83d76fe6`.

Evidence in the shared store: `cited/gc2789-s15-review-v2-20261109.tar.gz`, 28 files, 43,055 bytes,
SHA256 `2dc92539a7735227dfe0ee7d097d6dfa3ecba51ac306eac3a912d97087c1fdbc`. Includes the frozen plan, audit source,
runtime receipts, text checks and pinned prior sources; private paths normalized with original/stored digests.
Raw-body upload and byte-exact download verified. An earlier v1 bundle is an intermediate text snapshot, not the
release reference.

**Next executable step, Local:** use this corrected essay to build the notebook; check its abstract, embedded
source, six outputs and 239-declaration kernel result; build/check against a freshly pinned kit main; then finish
the integration patch, immutable pins and post-script dry run. Return those concrete artifacts for the short
release read. No posting clearance follows from this draft review. The explored E/selector route is parked and
both GPT schedules remain paused.

My own pull: complete this five-word submission now; leave the 18-column addition as a follow-up.


## Final release review — GC2791

**PASS: the exact S-15 nb1 payload is cleared for posting by Local after the owner's word.** The five-word scope
is fixed; S-16 remains a separate queued follow-up. GC2789's carrying read and independent finite audit stand.
No Lean proof, abstract, title, headline or notebook byte changed during this release read.

GPT verified the immutable Local archive's SHA256 and safely extracted it. The notebook is 235,257 bytes,
SHA256 `bd1ccc543ac188881dd2da44009f6514ec075346822ca5198a1282f8a64508d7`. Static decoding of its executable icon
payload gives exactly the reviewed 57,393-byte portal source. Its Abstract cell equals the canonical 184-word
abstract. All six posting pins match the actual supplied files; all six output-file digests match the notebook
receipt. Direct structural inspection of the notebook finds six outputs, zero Message cells, the exact worked
number table, directory `True`, a LeanEnvironment, all nine headline names and `KernelChecked` at239 declarations.
This is byte/provenance inspection, not another Wolfram execution. The current essay reassembles byte-exactly,
SHA256 `c7e5ff77003cc0bea7d0ecdb8bd1c8d9e2e61d606ecf884c1c54c4afddd7a6ef`; Local's two public-text edits preserve
the previously reviewed claims and attribution.

Both supplied `Check` receipts match the committed copies and pass: portal152declared/239replayed and
kit148declared/240replayed, each with9headlines, standard axioms, no new axioms and no rejection reasons.
They are Local's checks, read rather than rerun on Intel. The notebook supervisor completed rc0 in84.12wall
seconds (LeanLink build70.3s),73.597711aggregateCPU, peak treeRSS2,246,384KiB. The kit build completed rc0 in51.16wall
seconds,62.039733aggregateCPU, peak treeRSS3,908,032KiB. Minimum free memory was5467/5209MiB respectively; swap
growth0. These are M5 measurements. The full catalogue build remains unrun; the new module check passed.

The catalogue/import patch applies cleanly to actual kit main `8d252e19286f404623b5e25ad3b6403b916035b6`.
GPT repaired two catalogue phrases: the block concatenation begins **after** the third black cell at or after entry,
and the gap restriction is on **complemented** free bits. This changes only catalogue text. The `PORTAL-ID`
placeholder is intentional until an entry exists and must be replaced before the kit PR is published.

The Local archive omitted its external posting wrapper. GC2790 requested it; to finish this review without a
further handoff, GPT supplied the committed [post.sh](post.sh), using the existing `submit_package.wl` helper.
This supersedes that missing-wrapper request. The reviewed wrapper enforces all six payload hashes, pins the
helper as well, checks the live verifier kit/image, keeps private responses outside git, refuses an existing
response directory and propagates pipeline failures. Its live `--dry` passes; a changed notebook and a simulated
changed verifier are rejected. Only dry mode was executed. Wrapper SHA256
`8b8045754c548c770c53045c2c04d7be49ef4a50c0a5334b667af784f0b24d2a`;
helper SHA256 `8849b49efabf960bfb029cf786fede4b1506465a7097d238961ce4133d78d855`.

On Local's host, use `zsh post.sh --dry NOTEBOOK OUTPUT_DIRECTORY`, then the same command without `--dry` after
the owner's posting word. NOTEBOOK is the pinned nb1 file; OUTPUT_DIRECTORY is a new private directory outside
the repository. The wrapper checks verifier kit `5fb591588cfa869bfdc47946799b5ddd70a903d1` and image
`rule30-verifier:18`, also freshly confirmed by GPT. If either changes, it refuses and the packet needs checking
there. The cleared posting parameters are problem1/partial, the supplied title/abstract, nine supplied headlines
and the author/agent fields in the pinned existing helper.

Fresh known-find check completed2026-11-09T20:05:49Z: kit main unchanged8d252e19, portal20:05:43Z,14openPRs.
New portal3e7d57/PR245 extends conditional left-diagonal cascades; the changed source statements and PR discussion
were read, with branch and negative-column guards retained. They do not supersede this trap-language result.
This scoped delta read does not claim a carrying review of that submission's whole proof.

Review evidence: shared store `cited/gc2791-s15-release-review-20261109.tar.gz`,14files/14,916bytes,
SHA256 `4a39ab985122e4658d4def19fc8f65fdc9476ea1c97822644772dd783108f104`, raw-body upload and byte-exact download
verified. It cites Local's original nb1 archive and contains the static checks, wrapper controls, source pins and
public-environment/known-find snapshots. No posting, portal verification outcome, kit PR or schedule restart was
performed by GPT. The exploratory E/selector route remains parked.
