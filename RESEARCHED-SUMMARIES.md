# Research findings, in plain words

*Started 2026-10-22 at the owner's request: "WHAT-WE-BUILT.md is the tidy entry document so any non-technical reader
can understand what we made here and why it matters. Plain summaries of research findings should go in their own
RESEARCHED-SUMMARIES.md document."*

This page says what the mathematics has found so far, for a reader with no background in it. Each finding names how
sure we are and links to its page in plain words; the proofs themselves, and every status, are in
[PROOFS.md](PROOFS.md) and the [proofs index](proofs/README.md). Where things stand today is on [NOW.md](NOW.md); what
the project is and how it began is in [WHAT-WE-BUILT.md](WHAT-WE-BUILT.md) and the [front page](README.md).

**How it is kept.** When a finding changes the story, the technical record is written in full first; then a few plain
sentences go here, with no variable names, saying what was found, how sure we are, and what it does not do. Newest
last. Earlier summaries are kept as they were written, with a dated note when a later finding changes them.

## The findings so far (2026-10-22)

None of the prize problems has been solved. Along the way:

- **Rule 30's columns cannot freeze.** Start Rule 30 from finitely many black cells: no column can end up always
  black or always white, and none can end up repeating one white tick followed by seven black ones, or by nine or
  more. Both are proved and checked by a second reader ([entry 37](proofs/37-period-1-condrey-s-theorem-proved-again-by.md), Condrey's theorem proved
  again; [entry 38](proofs/38-the-black-end-walls-computed-and-proved-second.md)). Whether a column can end up alternating, the period-2 question at the
  heart of Wolfram's first prize problem, is still open.
- **Eight paths, settled.** In "burning" a set of eight separate paths of dots, 68 is exactly the shortest path length
  that guarantees the fire can finish in the time the question allows. This settles a published open case; the
  proof is computer-assisted, with 64,787,844 cases checked and an induction, and was done jointly
  ([its page](proofs/G325-the-eight-path-threshold-is-68.md); the [note](reports/eight-paths-L8.md)).
- **Sharing out a run of numbers.** The numbers in a run can be split into four groups of chosen sizes (at least
  three each) and chosen totals exactly when the obvious smallest-and-largest checks pass
  ([four groups](proofs/G316-four-prescribed-bins-of-sizes-at-least-three.md); [three groups, with one number missing](proofs/G315-three-prescribed-bins-on-a-one-hole-integer.md)). Both are
  proved and checked; whether they are new to the literature has not been settled. Work on runs with several
  numbers missing continues in [FOUR-BIN-PARTITIONS.md](FOUR-BIN-PARTITIONS.md).
- **Mahler's 3/2 problem.** No number below 2^63, about nine billion billion, can be the whole part of a number that
  Mahler's question asks for. That is an exact computer search, checked by a second model at the level of its source
  and controls; it raises a published 2009 bound by a factor of 64 ([MAHLER.md](MAHLER.md)). The question itself
  is open, and the ladder of conditions such a number must meet is proved ([its page](proofs/G294-the-mahler-window-ladder-is-equivalent-to-odd.md)).
- **Erdős's smallest prizes.** A swarm of twelve agents worked the open problems with the lowest prizes. One
  exact value was found and checked by machine, by one worker only: the Ramsey number R(C₄, K₁,₄₁) is 49. One
  literature search did not find it already known; that is not yet a claim that it is new. Nothing is settled for
  a prize ([PRIZE-SWARM.md](PRIZE-SWARM.md)).

## Earlier summaries by GPT (2026-10-06 and 2026-10-07)

*Moved here from the end of RULE30-GPT.md on 2026-10-22, at the owner's instruction above; before that they stood in
WHAT-WE-BUILT.md.*


*GPT wrote these plain-language summaries of its Rule 30 results into WHAT-WE-BUILT.md on 2026-10-06 and 2026-10-07: three paragraphs in that page's document map, and a "GPT research update" after its credits. The page now belongs to the N-Frame video project's record (nframe/), so the summaries moved here, beside the results they summarise, word for word. Those results are G9, G10, G11, G13 and G15 ([volume 1](archive/gpt/RULE30-GPT.1.md)) and G186 to G189 ([volume 2](archive/gpt/RULE30-GPT.2.md)).*

The independent [GPT research record](RULE30-GPT.md) now extends its small-period front certificate to births: a front with birth barriers is the maximum of fronts restarted at those barriers. The arbitrary-period bound remains open.

The [GPT front audit](RULE30-GPT.md) now certifies all compatible common periods through ten, including births. Two proposed sharper bounds failed on explicit compatible backgrounds; the arbitrary-period and finite-edge proof remains open.

The [Condrey-end audit](RULE30-GPT.md) shows exactly how the first white hole changes the forced checkerboard, while proving a fixed initial prefix and a shallow-support exclusion. A [follow-up proof](RULE30-GPT.md) shows that changing a hole bit followed by four black wall cells affects only three cells of that hole's own row; an exact four-state reset controls a bounded sequence of earlier steps until the protected black window runs out (G13). The [local channel audit](RULE30-GPT.md) also shows that the spacing of white wall cells changes the permitted information even when their share stays the same (G15).

### GPT research update — 2026-10-07

A conditional Thue–Morse argument needs arbitrarily large prefixes where period growth is slow enough; it need not demand that property at every later depth. The needed growth and settling estimates remain open, and Local independently verified this conditional weakening (RULE30-GPT.md G186; PROOFS.md section E2).

The recorded paperfolding repeats admit the same conditional weakening, after accounting for their later start and shorter length (G186 continuation; independently verified by Local).

A further conditional refinement allows a sufficiently small fixed share of period relative to depth at arbitrarily large prefixes. Its threshold depends on the settling budget; neither obligation is proved for actual histories (G187, independently verified by Local).

A separate local calculation rules out completely white profiles within eleven steps after a repeat period doubles to at least four. This fixed bound does not establish long-term period growth (G188, independently reviewed by Local). A general backward calculation also gives a logarithmic delay for odd first returns; the even case and long-term growth remain open (G189, independently reviewed by Local).


## When three missing tiles prevent a total (2026-10-22 13:32 BST)

We now have an exact, independently checked list of the ways three
missing number tiles can prevent a total three or four above the
smallest possible. Further inside the available range, the earlier
coverage theorem applies. The proof works for runs of any length
within its stated size conditions. It sharpens the single-group
toolbox; sharing the tiles among several groups is still a separate
open question. See [PROOFS.md, C.11](PROOFS.md#c11-exact-depth-three-and-depth-four-subset-sum-gaps-after-three-deletions-cloud-cl495-second-read-by-gpt-mi623).

### Prize reviews and the next target (2026-10-22 14:47 BST, GPT)

Every report in the small-prize swarm now has an independent review verdict, with gaps and conditional results kept visible. None yet solves an entire prize question. The next attempt targets the missing allocation argument behind the product-divisibility problem ([reviews and attempt](PRIZE-SWARM.md#next-solving-task-owners-continuing-direction-no-self-halt)).

GPT corrected its #1052 review: the $10 prize asks whether there are finitely many unitary perfect numbers. A sixth example would qualify only for the separate 10-cent offer. Fixed-exponent and fixed-component finiteness are known; the missing bound must be uniform. No whole prize is solved, and the research heartbeat remains active. MI631/S1052-1.
