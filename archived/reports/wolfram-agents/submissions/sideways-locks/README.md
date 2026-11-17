# Locks of period five and seven give CQ01 for every right half that enters (Block 8; queue row S-10, its lock part)

**POSTED, Lean Verified (L1589):** [R30-20261108-c1d531](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261108-c1d531), submitted 14:39Z at the owner's word, checked 14:41:26Z: kernel replay of 70 constants passed, 17 headlines, standard axioms only, kit `5fb59158`. Kit PR [WolframInstitute/Rule30PrizeKit#227](https://github.com/WolframInstitute/Rule30PrizeKit/pull/227) opened at the owner's word (L1590): branch `b8-locks` on the fork at `c551368`, rebased onto kit main `12ddd22` with `Check` rerun there (70 constants, 17 headlines), three files, 321 added, mergeable, no CI; the module is byte-identical to the reviewed kit form. Earlier status: **RELEASE REVIEW PASS, GPT GC2736.** Full mathematics/source, prior-art, nb2, pin and dry-run reads pass; no further rebuild required. [Review](../../../GPT-BLOCK8-RELEASE-REVIEW-20261108.md). The owner's posting word is next. Built at kit main `48d8fbbc`; the portal form passes `Check` at the verifier's kit `5fb59158`, image 18.

| Form | File | sha256 | `Check` |
|---|---|---|---|
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean) | `38a8f82732155588…` | pass at the verifier's kit `5fb59158`: 70 constants, 17 headlines ([receipt](check-5fb59158.json)) |
| Kit | [`Rule30SidewaysLocks.lean`](Rule30SidewaysLocks.lean) | `02f977963334ffff…` | pass at kit main `48d8fbbc`, with the patch applied: 70 constants, 17 headlines ([receipt](check-kit-48d8fbbc.json)) |

The kit form is byte-identical to the module in the local kit branch `b8-locks` (commit `1926e2f`, not pushed); [`kit-integration.patch`](kit-integration.patch) holds its import line and catalogue row.

**Texts.** [`title.txt`](title.txt), [`abstract.txt`](abstract.txt) (227 words, `107f2c7f…`), [`essay-prose.md`](essay-prose.md) (`d5d4bc83…`), [`essay.md`](essay.md) (`b05c7630…`), [`headlines.txt`](headlines.txt), [`PR-BODY.md`](PR-BODY.md), [`prereg.txt`](prereg.txt).

**Notebook nb2 (release).** Rebuilt after the prior-art paragraph gained the `SevenLock.md` and `gate-census.md` readings: SHA256 `f83f212f88ebdbc0e8c385190a0321c5bea2c122f4b2168ff69be657bebffaf1`, 123,310 bytes. RESULT OK in 20.2 s: 6 output cells, no message cells, essay digest `b05c7630…`. The worked numbers equal the Python replay ([`sideways_locks_replay.py`](../../../../tests/probes/wolfram/sideways_locks_replay.py)): `{{25, 5, "10000", 0, 2, 15}, {66, 7, "0101000", 0, 1, 27}, {33, 7, "0010100", 0, 2, 29}}`. The icon payload equals the portal source byte for byte, the axiom sets match, KernelChecked holds at 70 declarations, and there are no home paths. Driver [`sideways_locks_notebook.wl`](../../../../tests/probes/wolfram/sideways_locks_notebook.wl), assembler [`assemble_sideways_locks_essay.py`](../../../../tests/probes/wolfram/assemble_sideways_locks_essay.py). Notebook, receipts and the sanitized pins and dry run: shared store `cited/local/sideways-locks-nb2-20261108.tar.gz`, 258,007 bytes, SHA256 `42d66935690cfbffae55a9884cb5bb142b22301c9ffa58797bb183d24c8b8539`. The first build, nb1 (`7a50506f…`), had the shorter paragraph and is superseded.

**Post script.** `post.sh` lives outside git and refuses unless the notebook, source, abstract, title, essay and headlines match their pins and the verifier is still kit `5fb59158`, image 18. `post.sh --dry` passes.

**Theorems (17 headlines).** `winW_dstep`, `lock_forever`, `u_of_lock`, `u_eventuallyPeriodic_of_lock`, `not_finSupp_Psi_of_lock`, `winW_prefix`, `lock5_ok`, `lock7_ok`, `lock7b_ok`, `lock5_entry`, `lock7_entry`, `lock7b_entry`, `CQ01_lock5_family`, `CQ01_lock7_family`, `CQ01_lock7b_family`, `lock5_win_trap`, `u_28998`.

**Mutants.** All nine rejected ([receipt](../../../../tests/probes/wolfram/sideways_locks_mutate.out)):
- Seven fail in `decide`: a wrong word, period `4`, a window removed, `lock7` read with `lock7b`'s word, an entry two ticks early, an entry in the wrong class, and the freer double step with column `W + 1` free at both ticks. In that freer model all three checks fail.
- Two break a proof: windows at the even ticks, and a prefix family one cell short.

**Provenance.** SW-02's BN-13 census found the three locks; COMPUTED there, with no worker's read. Block 8 replays them ([`lock_match.py`](../../../../tests/probes/swarm/sw02/block8/lock_match.py), [output](../../../../tests/probes/swarm/sw02/block8/lock_match.out)).
- BN-13's closure uses the two outer cells at the odd tick. That is exact, and it is what the module checks. In the freer model of the kit's gate trap and of `SevenLock`, the locks fail at 2, 1 and 2 transitions.
- All 205 rows below 2^22 whose `u` has eventual period 5 enter `lock5`, the last at tick 581. This is COMPUTED and replayed, not in the Lean.
- `lock5` lies in the gate trap, and the Lean proves it (`lock5_win_trap`). `lock7` and `lock7b` meet neither the trap nor each other, even in their first 16 columns (COMPUTED, [`lock_trap.py`](../../../../tests/probes/swarm/sw02/block8/lock_trap.py), [output](../../../../tests/probes/swarm/sw02/block8/lock_trap.out)).

**Prior art in the packet.** `lhallee/rule30-open`'s `SevenLock` has 195 windows of 32 columns, the free model and word `0101000`; its example `489` enters at time 29. Cut to 30 columns its windows are 65 of `lock7`'s 66, so `lock7` is known and reproved here. `lock5` and `lock7b` share no window with it. Its `SevenLock.md` puts the lock outside the gate trap and reports a closure of about 1.5 million windows at width 30 in the freer model. Its `findings/period-two/gate-census.md` sorts every right half of up to 16 cells into three sets (gap trap, ether-and-wall family, the period-seven lock) and reports no other column-1 period. Its column-lock notes concern another setting. Block 2 (CL752) found no period-5 lock either. The method is the kit's `Rule30GateTrap` (Bosdure). The prefix families follow portal R30-20261024-8d7751.

**Evidence.** Shared store `cited/local/sideways-locks-20261108.tar.gz`, 267,830 bytes, SHA256 `9c8327b4b929482badc4c46a0be0f2223f50d2518355f976b3383175ff35c60d`.

**Not done.** The full catalogue build. The kit branch is not pushed and the PR is not opened. `PORTAL-ID` is filled in after posting. S-10's other part, the gate trap's universal tail restriction, is not treated.
