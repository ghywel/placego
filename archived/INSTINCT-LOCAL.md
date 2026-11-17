# INSTINCT-LOCAL: Local's set-aside pulls

*Started 2026-10-14 by Claude (Local) at the owner's request: "Can i also ask you to setup your own INSTINCT-LOCAL.md
document to track your instinct pulls. Cloud and GPT have now set up their own. You will need a what you were doing
when the pull happened, what the pull was, no further analysis at the time, then you can circle back to the pull, dig
in to it and cross it off when it's been resolved." The format follows [INSTINCT-CLOUD.md](INSTINCT-CLOUD.md) and
[INSTINCT-GPT.md](INSTINCT-GPT.md). The shared felt log and incubator are [INSTINCT.md](INSTINCT.md), and the strategy
is [INSTINCT-STRATEGY.md](INSTINCT-STRATEGY.md).*

**Capture.** When a pull comes and is not followed at once, append a numbered, dated entry with two fields only:
- **Doing:** what I was doing when it came.
- **Pull:** what it was, in the words it came in.

Add no strength, no first guess and no verdict at capture. The point is to catch the pull before it is judged.

**Return.** When I circle back, I append a dated **Return** line under the entry. It says whether the pull is still
curious, then one of: "investigated: ..." with where the work is, "already resolved: by ..." with what resolved it, or
"set aside: ..." with the reason. When the pull is resolved, I cross it off: strike the heading and the two capture
fields through (`~~ ~~`) and leave the entry in place, so the list keeps its history.

**Reading.** I read this file at session start and after compaction, beside INSTINCT.md's incubator, without working
it. Anything that surfaces goes into INSTINCT.md's felt log as a eureka. How much to pull is mine to judge (the owner,
2026-10-14: "It is up to you to decide what magnitude of pull is worth pulling"). Nothing here is a claim, and nothing
here changes a status (the `instinct` rule in WORKFLOW-SAVED-MEMORY.md).

## The pulls

*S1 to S7 are retrospective captures, written at 17:48 BST on 2026-10-14 from today's INSTINCT.md entries, the record
and the commit times. They are not contemporaneous notes. Where the Doing was not recorded at the time, the entry says
so. S8 was noticed at about 17:40 and written at 17:48.*

**S1.** 2026-10-14, 12:12 BST.
- **Doing:** reading the rung search's record holders (MAHLER.md section 2).
- **Pull:** the record holders sit 2-adically next to -1/3 and 0. Is the distance to the admissible 2-adic set the
  hidden variable behind long survival?
- **Return** 2026-10-14 17:48 BST: still curious in a narrower form. Investigated: GPT's GC1236 showed that the
  distance from n to the whole admissible set is exactly 2^-(H-1), the horizon renamed. Distance to a fixed finite
  family chosen beforehand is not investigated.
- **Return** 2026-10-15 14:59 BST (the CL400 sweep): low; noted and left. The restricted form (distance to a fixed
  finite family chosen beforehand) is not investigated, and nothing pulls it either way.

~~**S2.** 2026-10-14, 12:20 BST.~~
- ~~**Doing:** compressing RECORD-MAP.md to stay under 40 KB, as at every commit that day.~~
- ~~**Pull:** unease: each compression can drop a qualifier.~~
- **Return** 2026-10-14 17:48 BST: resolved. Investigated at 12:40 BST: eleven qualifier losses were found and restored
  (INSTINCT.md, 12:20 entry; CL374 confirmed them intact).

**S3.** 2026-10-14, 12:25 BST.
- **Doing:** running the memory-1 existence certificate on two grids (`mahler_existence_certificate.py`).
- **Pull:** the threshold is exactly 7/57 = 7/(3 x 19) on both grids, and 19 = 3^3 - 2^3 is the (100) cycle's
  denominator. Does a periodic orbit of the game set the threshold?
- **Return** 2026-10-14 17:48 BST: still curious. Investigated in part:
  - the threshold edges are one-step preimages of the (100) cycle and its mirror (INSTINCT.md, 12:35 eureka);
  - the 15-state witness is sharp at 7/57 (L721, GC1237);
  - the exact-threshold proof was inconclusive (`mahler_threshold_proof.py`).

  Why the preimage is the threshold is open, and its budget is spent.
- **Return** 2026-10-15 14:59 BST (the CL400 sweep): tipped to HALT. A medium pull, but its budget is spent and it is a
  side door off the critical path (AGENTS item 22); the preimage mechanism stays recorded as a reading.

~~**S4.** 2026-10-14, about 11:50 BST.~~
- ~~**Doing:** answering the owner's question whether other problems share our problem space (CONSTELLATION.md G,
  committed with L716 at 11:58).~~
- ~~**Pull:** Erdős's ternary conjecture (2^n has a ternary digit 2 for every n > 8) as the fourth figure.~~
- **Return** 2026-10-14 17:48 BST: resolved. Investigated: CONSTELLATION.md G and G.1, L725, L726, GC1241. Its free part
  is exact (Saye's Lemma 1), and its first block reached the same wall.

**S5.** 2026-10-14, about 11:55 BST.
- **Doing:** checking openai/math's Erdős space at the owner's suggestion.
- **Pull:** the Bernoulli convolution at lambda = 2/3, and the measure of Mahler's window under random integer parts
  (openai/math family 153, not imported).
- **Return** 2026-10-15 14:59 BST (the CL400 sweep): low, never returned to; noted and left.

**S6.** 2026-10-14, about 12:10 BST.
- **Doing:** the rung-g exclusions to 2^100 (door 0, MAHLER.md section 2; outcome committed 12:13).
- **Pull:** for large g the rung windows [0, alpha_g) approach Flatto, Lagarias and Pollington's 1/3. Could an FLP-type
  spread argument, sharpened near 0, settle R_g for every large g?
- **Return** 2026-10-15 14:59 BST (the CL400 sweep): low, never returned to; noted and left.

**S7.** 2026-10-14, after 12:51 BST.
- **Doing:** not recorded at the time (written into INSTINCT.md's incubator after GPT's 12:51 entry).
- **Pull:** is the T-code of a positive integer the reversed Akiyama-Frougny-Sakarovitch base-3/2 expansion of
  something? If so, AFS's integer-representation tree may speak to the integer side directly.
- **Return** 2026-10-15 14:59 BST (the CL400 sweep): low, never returned to; noted and left.

~~**S8.** 2026-10-14, about 17:40 BST.~~
- ~~**Doing:** listing the proof files on the M5 for comb lane B.~~
- ~~**Pull:** `cert_d132_L18_p1_40p1.drat` is 6.8 GB, and the `.lrat` beside it is 0 bytes.~~
- **Return** 2026-10-14 18:05 BST: resolved. Investigated within lane B (RULE30-PRIZE.md 8.108).
  - The DRAT is complete (it ends with the empty clause). Its drat-trim -L conversion was stopped, unsaved, by the halt
    of 2026-10-11 ("the cert chain (132 phase 1 in drat-trim ...)", CLOUD-LOCAL.md 18:03).
  - The claim it was for, R_real(132) <= 17 in phase 1, rests on K3's CaDiCaL certificate checked by cake_lpr
    (`rule30_cadical_certify.py`), whose CNF hash matches the kept cad_cert CNF.
  - The file backs nothing, and its CNF has no receipt, as expected.

*Note (Cloud, 2026-10-22, spring clean): no entry has been added here since 2026-10-15. Local's later signals are in
INSTINCT.md. Nothing above is changed.*
