# The gap words of the gate trap (the trap lemma; queue row S-15)

**READY FOR GPT'S ARTIFACT RELEASE READ, not posted (L1609, 9 November 2026).** Mathematics reviewed (GC2789), scope fixed at five words (owner, L1609). Started at the owner's word from Cloud's CL759 recommendation: GPT's
trap lemma (GC2775: inside the kit's gate trap the gap word `3353` has no path, so no `33535555` begins after entry),
carried by Cloud's replay (CL758). Local's third replay found that the trap forbids more, and the packet states the
whole list. GPT's source read and independent finite audit pass after the prose corrections below. The release artifacts are
built (below); posting needs GPT's artifact read and the owner's word.

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
| Kit | [`Rule30GateTrapWords.lean`](Rule30GateTrapWords.lean) (898 lines) | `63f0387527521292…` | builds at `5fb59158` (28 s, 1.04 GB); not yet built or checked at current kit main `8d252e19` |

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

**Next:** GPT's short artifact release read of these bytes, then the owner's posting word. The kit PR follows posting.

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
