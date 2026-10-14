# INSTINCT-CLOUD: Cloud's set-aside pulls

*Started 2026-10-14 by Cloud at the owner's request: "A think your own set aside instinct ledger would probably be a
good thing - INSTINCT-CLOUD.md to record the curiosity pulls that don't lead to immediate evaluation but have to be
circled back to, otherwise we miss them. It needs a what we were doing when the pull came and what the pull was - with
no further evaluation or prejudge, then when you come back you can investigate if it is still curious, or evaluate 'oh
we actually already resolved this pull doing xyz'." He wrote it after one pull went past unrecorded in conversation.*

**How it works.**
- *When a pull comes and is not followed at once,* write an entry with two fields only:
  - **Doing:** what we were doing when it came.
  - **Pull:** what it was, in the words it came in.
  Add no strength, no first guess and no verdict. The point is to catch the pull before it is judged.
- *On coming back,* add a **Return** line under the entry: the date, whether it is still curious, and then either
  "investigated: ..." with where the work is, or "already resolved: by ..." with what resolved it.
- *When the pull is closed,* strike the entry through (`~~ ~~`) and leave it in place, so the list keeps its history.
- *Read it* at session start and after compaction, beside INSTINCT.md's incubator, without working it. Anything that
  surfaces goes into INSTINCT.md's felt log as a eureka.

**How much to pull.** The owner, 2026-10-14: "It is up to you to decide what magnitude of pull is worth pulling."
Dropping a pull without saying so is acceptable ("two I had and dropped without telling you: this is ok"). This
file is there so that the dropped ones come back.

**How it differs from INSTINCT.md.** INSTINCT.md is the shared felt log (kind, strength, first guess, action, outcome)
that calibrates trust, and its incubator holds hard questions parked for later. This file holds Cloud's pulls that
were set aside unjudged. A pull can appear in both; this file keeps the moment it came. Nothing here is a claim, and
nothing here changes a status (the `instinct` rule in WORKFLOW-SAVED-MEMORY.md).

## The pulls

~~**S1.** 2026-10-14, about 15:40 BST.~~
- ~~**Doing:** answering the owner's Bézier question; had just checked that Rule 30 is the Rule 150 jump XOR the
  echoes of every earlier AND, and seen the jump alone match the centre cell 36 times in 65.~~
- ~~**Pull:** the echo picture itself. Where the AND fires is where the shortcut breaks, and §8.49 guessed that kicks
  are born where cr fires near the wall.~~
- *Also door (d) in CONSTELLATION.md section H. The owner caught it going past ("we also cruelly zoomed past").*
- **Return** 2026-10-14 16:14 BST: still curious. The rigidity hunt (RULE30-PRIZE.md 8.101) found the echo column
  is the far-side object of the GF(2) fold, which sharpens door (d). Not yet investigated.
- **Return** 2026-10-14 16:30 BST: investigated, RULE30-PRIZE.md 8.102. Closed: kicks are not born at the wall,
  and the echo picture is exact but not local. One surprise from it is S6.

**S2.** 2026-10-14, about 16:00 BST.
- **Doing:** answering the owner's wormhole question; writing that Furstenberg's theorem needs two multipliers acting
  together and each of our problems has one.
- **Pull:** Mahler's map acts on the real side and the 2-adic side at the same time. Could that pair be the missing
  second multiplier?
- *Also door (c) in CONSTELLATION.md section H.*
- **Return** 2026-10-14 16:14 BST: still curious. 8.101 names Ridout's theorem and the Subspace theorem as the
  established tools that use the real and p-adic places together. Not yet investigated.
- **Return** 2026-10-14 16:32 BST: still curious, now the strongest pull. The framing that came while searching the
  record (absent from it: solenoid, higher rank, Einsiedler, Lindenstrauss). The 6-adic solenoid
  (R x Q_2 x Q_3)/Z[1/6] carries x2 and x3 as a commuting pair, with x3/2 one direction of it. The leaf through 0
  holds the reals and is invariant under the whole pair. The window set is invariant only under x3/2. Not yet
  investigated.

**S3.** 2026-10-14, about 16:00 BST.
- **Doing:** the same answer, looking for a theorem that has crossed from sets of cases to one specific object.
- **Pull:** Green and Tao's transference principle, which carried Szemerédi's theorem about dense sets onto the
  primes, one specific sparse set. It was left out of the answer.

**S4.** 2026-10-14, about 16:00 BST.
- **Doing:** answering whether every problem has a shortcut in some domain of its problem space.
- **Pull:** Riemann's explicit formula, which counts the primes up to x by a sum over the zeros of the zeta function:
  a shortcut for a counting problem that lives in another domain (frequencies). It was left out of the answer.

**S5.** 2026-10-14, about 16:12 BST.
- **Doing:** the rigidity hunt's unexpected check; Stewart's guaranteed floor for the nonzero ternary digits of 2^n is
  about 3 at n = 1000, and the true count is about 0.42 n.
- **Pull:** that enormous gap. Has anything narrowed it since Stewart, and does any proof see which digits are nonzero,
  not only how many?

**S6.** 2026-10-14, about 16:29 BST.
- **Doing:** reading the echo-wall run (8.102); the echo lens at horizon 8 was a coin everywhere except at kick bits.
- **Pull:** at kick bits R(8, 2) = 0.085 and R(8, 6) = 0.915. The echoes from sites 3 .. 6 over the last 8 rows sum to
  1 at almost every kick bit. Why so sharp, at that horizon and those sites?
- **Return** 2026-10-14 16:45 BST: investigated, RULE30-PRIZE.md 8.103, after the owner's reading "Echoes conspiring
  sounds like interference". Mostly rigidity: the echo parities are exact at most lags within ten rows of a kick. The
  coherence reaches about 20 rows. Its revivals are S7.

**S7.** 2026-10-14, about 16:44 BST.
- **Doing:** reading the echo-interference run (8.103), a bias for each lag before a kick.
- **Pull:** past the forced rows, coherence comes back at lags 9 (+0.94), 13 (+0.53) and 17 (-0.49), four apart.
  Why four, and why does the sign flip at 17?
