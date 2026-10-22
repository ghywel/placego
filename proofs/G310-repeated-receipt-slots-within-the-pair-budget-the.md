# Repeated receipt slots within the pair budget; the E31 lone-93 slice

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT310. Repeated receipt slots within
the pair budget; the E31 lone-93 slice (2026-10-16; Cloud CL424)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Repeated receipt slots allow up to h positive units per bin when hn equal-sum
pairs have a consecutive chosen-token run. This constructs all105 E31 targets
with lone odd target93. PROVED after Cloud CL424; no general E31 statement.

## The formal statement and proof

**Current status: PROVED in the stated scope.** Original source MI052 is reproduced
verbatim below; its original candidate labels are publication history. Independent carrying
read CL424, commit57dbf2ad; no novelty claim or full L8 conclusion.

**Direct hand extension, PROOF-SKETCH, not a separately queued proof.** Let h,n>=1 be integers. Suppose hn disjoint pairs of
odd integers all have common sum S, and one chosen member from each pair forms a consecutive run of hn
odd tokens. Then the pairs' elements can be partitioned into n bins of2h elements for any targets
hS+2e_i, where the e_i are integers with e_i<=h and sum e_i=0. This changes G304's positive-capacity
restriction; its verification is not automatically inherited from CL417. No source priority asserted.

For each positive bin i create e_i labeled receipt slots, rather than one slot. Let u be the total
number of slots, p the number of positive bins, and d the number of negative bins. A donor e=-k gets
k slots, split arbitrarily among the donors according to their required amounts. The chain for that
donor uses k+1 consecutive tokens, one root plus its k receipt slots. All chains together use

    u+d <= hp+d <= h(p+d) <= hn

tokens, so they pack into the chosen run as disjoint segments. Assign the root's entire pair to its
donor and each receipt token's pair to its positive bin. A donor gets one pair, a positive bin gets
e_i<=h pairs, and a neutral bin gets none. Fill every bin to h pairs with the remaining pairs. Then
perform the donor-chain swaps exactly as in G304. Each positive bin gains2 for each of its slots,
and each donor loses2k; all element counts and coverage are preserved.

**Unexpected check, resolved:** a positive bin may occur twice consecutively in one chain. If it
initially holds v_1,v_2 and the donor holds v_0, with successive differences2, the first swap leaves
the positive bin holding v_0,v_2 and the donor v_1. The second leaves it holding v_0,v_1 and the
donor v_2. Its gain is4, as required. More generally a token assigned to a future slot is never
removed by an earlier swap, even if its bin has already received another slot. Different slots use
different whole pairs, so no bin's pair capacity or later-token ownership is assumed away.

For the first2hn odds one may take S=4hn, giving mean4h^2 n and even targets up to mean+2h.
In particular h=2 permits mean+4, not just G304's mean+2. This is the same construction with receipt
slots counted correctly, not a new search or a claim that arbitrary large deviations are covered.

**Concrete E31 consequence.** Reserve {1,31,61}, of sum93, as the lone odd-target bin. The remaining
28 odds form fourteen62-complement pairs with chosen upper tokens33,35,...,59, a consecutive run.
Apply the extension with n=7,h=2,S=62. Every seven even targets<=128 summing868 can be filled from
them, with four elements per bin. Thus E31's slice with lone odd target93 is covered by this hand
candidate. Other odd targets, or three/five/seven odd targets, are not included.

A hand boundary case is(93,100,128,128,128,128,128,128). Its normal residuals from124 are-24,+4^6:
one donor supplies twelve unit receipts, two to each of six bins. The13-token chain59,57,...,35 fits
in the14-token pool. Explicit final bins, written here as a check of the repeated-receipt mechanism:

    {1,31,61} ->93
    {3,35,29,33} ->100
    {5,59,7,57}, {9,55,11,53}, {13,51,15,49},
    {17,47,19,45}, {21,43,23,41}, {25,39,27,37} ->128 each.

These cover all31 odds exactly once by inspection; no machine check or experiment ran. The donor's
unused filler pair is{29,33}; the six receiving bins each own two initial pairs, as the capacity bound
requires. This is a finite check, not evidence for the remaining E31 tuples.


**Independent carrying read, Cloud CL424 (verbatim).**

**MI052 (h-fold receipt capacity; the E31 lone-odd-93 slice): VERIFIED.** The extension of G304 is sound as written.
Checked by hand: a donor with k slots uses k+1 consecutive run tokens; the chains total u + d ≤ hp + d ≤ h(p+d) ≤ hn,
so they pack as disjoint segments whatever the e_i ≤ h are; every active bin receives whole pairs (one for a
donor, e_i ≤ h for a recipient), the fillers are exactly the unreserved pairs, and the swap chain lowers the donor by
2 per step and raises the slot's owner by 2, including the repeated-recipient case (a bin holding v_1, v_2 ends with
v_0, v_1, gain 4). Machine: my re-implementation of the construction passes every deviation vector with e_i ≤ h and
sum 0 for h ≤ 3 and n ≤ 5 (5,769 vectors), and the E31 slice exactly: with {1,31,61} reserved, the remaining 28 odds
pair to 62 with the upper run 33..59, and all 105 sorted even 7-tuples ≤ 128 summing 868 are constructed and
checked for coverage and sums. The hand example (93,100,128⁶) is covered as written. Scope as you state it: one
odd target, equal to 93; nothing about other odd targets or the fragmented pools.




**Filing check.** proof_dupes hard checks pass. Nearest entries G304,G305,G306 read: this increases positive receipt capacity and treats a distinct E31 pool; not a restatement.
