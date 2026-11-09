# The gap words of the gate trap (the trap lemma; queue row S-15)

**DRAFT, not posted (L1608, 9 November 2026).** Started at the owner's word from Cloud's CL759 recommendation: GPT's
trap lemma (GC2775: inside the kit's gate trap the gap word `3353` has no path, so no `33535555` begins after entry),
carried by Cloud's replay (CL758). Local's third replay found that the trap forbids more, and the packet states the
whole list. Posting needs GPT's release review and the owner's word. One scope question is open (below).

## What the module proves

`Rule30GateTrapWords` (core Lean, imports only `Rule30GateTrap`). For every right half `R` whose window enters the
kit's 829-window trap at an odd time `t0`, and every step `s` with `t0 ≤ 2 s + 1`:
- `gap_words_of_entry`: `u R` reads none of the gap words `333`, `3353`, `3533`, `3553`, `5533` from `s`;
  `no_3353_of_entry` is GPT's word alone; `no_33535555_of_entry` follows.
- `no_late_33`: after any two gaps the next two are not both `3` (with `gaps_of_entry`: from the third black cell
  after entry, no `33`; no `3553` anywhere after entry).
- `minimal_paths`: each word is minimal for the trap graph (its six maximal proper factors have explicit paths).
- `Q01GapWords` (open), `Q01GapWords_of_Q01Gap`, `not_finSupp_Psi_of_Q01GapWords`, `CQ01Empty_of_Q01GapWords`:
  the kit's `Q01Gap` weakens to a statement about fewer free-bit sequences (0.132 against 0.256 bit per sample) with
  the same consequences for trapped right halves.

Method: the kit's own (trap codes, `step2`, `allSucc`, `win_next`, `win_mem_trap`). Path-set layers for the five words
are data in a trie, 40 layers, one start check and 44 step checks, each its own `decide +kernel` so that the kernel's
caches stay small; a bitmap from the codes (`maskN`) and `decode (encList w) = w` carry membership.

| Form | File | sha256 | Check |
|---|---|---|---|
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean) (896 lines) | `82d0eb9ec399eb03…` | pass at the verifier's kit `5fb59158`: 152 declared, 239 constants replayed, 9 headlines, standard axioms, no new axioms ([receipt](check-5fb59158.json)) |
| Kit | [`Rule30GateTrapWords.lean`](Rule30GateTrapWords.lean) (899 lines) | `63f0387527521292…` | builds at `5fb59158` (28 s, 1.04 GB); not yet built or checked at kit main `8d8e157c`, where `Rule30ZeroBoundary` has changed |

Build cost (portal form, M5, under `run_capped` with an 8 GiB cap): 27 s, 1.22 GB peak. The first single-check design
took 32 s and 3.6 GB; a `List.contains` design took 125 s and 7.7 GB (kernel `decEq` on `Nat`); both were dropped.

**Mutants** ([output](../../../../tests/probes/swarm/sw02/block3/mutate_trap_words.out), script
[`mutate_trap_words.py`](../../../../tests/probes/swarm/sw02/block3/mutate_trap_words.py)): eight must-fail mutants
rejected (a dropped window in a middle layer and in the shared first layer, a claimed allowed word, a white start, a
shifted layer, a missing final layer, a start window with the wrong column 1, a start window outside the trap). M4,
one flipped column-17 value early in a witness path, was ACCEPTED: column 17 reaches column 1 only after about eight
double steps, so that path still reads its word. Kept as found; not a must-fail mutant.

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
- **R30-20261030-60990f (J. Lee):** Lean, for the one-cell seed R1 only: no `33`, `3553`, `3535353` at every index, via
  an 18-cell pool of 2,040 states; `33` and `3553` credited to the authors' earlier work (not on the portal).
- **Our record:** SW02-RESULTS CP-2.2 (COMPUTED, 6 November): inside the kit's trap, for every R, `33` at most once,
  no `3553`, no `3535353` (18 columns), tail entropy at most 0.12707; it names the weaker `Q01Core`, which
  `Q01GapWords` formalizes. GC1087 (11 October, GPT, hand): a closed core with no two short renewals after entry, in
  another frame (the identification with `33` is to be confirmed in GPT's review).
- rule30-open: a larger gap trap (3,562 entry windows) containing the kit's; no adjacent `3`s for the empty half
  (computed). Kit `Rule30PeriodTwoWidth13` (R30-20261109-62afca): nine pairs, all four pairs over 3 and 5 allowed.

New relative to these: the list in Lean for every right half that enters the kit's trap (Lee's is one seed), the start
words `3353`, `333`, `3533`, `5533`, minimality and completeness for the 16-column trap, and `Q01GapWords` in Lean.

## Open scope question for the owner

`3535353` is excluded for every trapped right half by the 18-column lift (computed). Adding it in Lean would make the
module the all-right-half version of Lee's R1 theorem and the formal form of CP-2.2. Cost estimate: one more block (an
18-column window with its double-step lemma copied into the module, about 27 more layers).

## Texts

[`essay-prose.md`](essay-prose.md) and [`essay.md`](essay.md) (assembled by
[`assemble_gate_trap_words_essay.py`](../../../../tests/probes/wolfram/assemble_gate_trap_words_essay.py)),
[`title.txt`](title.txt), [`abstract.txt`](abstract.txt) (197 words), [`headlines.txt`](headlines.txt) (9). The
generator [`gen_trap_words.py`](../../../../tests/probes/swarm/sw02/block3/gen_trap_words.py) writes both Lean forms
from the kit's trap codes. Notebook driver
[`gate_trap_words_notebook.wl`](../../../../tests/probes/wolfram/gate_trap_words_notebook.wl) is written (S-14's with
this packet's axioms, 239 declarations and the replay list); the notebook is not yet built.

**Not done:** the notebook, pins and post script; the kit-main build and `Check`; the kit integration patch; GPT's
release review.
