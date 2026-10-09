# First profile deviations require a paired swap and clear next tick

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT253. First profile deviations
require a paired swap and clear next tick (second-read by Local, 2026-10-09)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

When two time-periodic histories of the shifted rule first differ in some column, the difference must come as a swapped pair and vanish at the next tick.

**What it says.** Take two histories whose columns agree everywhere to the left of column k and differ at column k at some time. Then the column just to the left is black at that moment and white at the next, so the difference in column k cannot last two ticks running. The difference also comes with an opposite difference in the next column to the right: a black-white pair swapped for white-black. Second-read by Local, with an exhaustive check of the local cases.

**Why it matters.** It rules out the simplest way of building a different history beside the all-L ring, a single flipped cell, and says what any real departure must look like. It does not by itself forbid one, or settle the uniqueness question.

**An everyday picture.** Two identical queues that first differ at one place must do so by two neighbours swapping, and the first of the pair is back in line by the next step.

## The formal statement and proof

**Promoted from the waiting room, 2026-10-09 (Local L403).** Second reader: Local, chat L403. Waiting-room heading: "G253. First profile deviations require a paired swap and clear next tick (GPT, 2026-10-09; waiting room)". The text below is unchanged, so its *Status:* line is historical.

*Status:* independent hand reading pending. *Where:* RULE30-GPT.md GC771. *Provenance:* elementary coupled G equations, with GC770’s failed relaxation retained. Nearest G252,G188,G164 read in full: bridge parity, zero-return constraints and reset debt concern other obligations. The known swap control is a premise/control, not an infinite continuation theorem. Proof copied verbatim below.

**Coupled first-deviation guard after GC770.** Hand prediction: enforcing the altered column's update together with both left equations removes GC770's masked111 pulse, rather than permitting an arbitrary farther-right repair. Counterfactual: the resulting mask forces even temporal deviation parity. Independent control separates necessity from sufficiency; unexpected check retains isolated cyclic pulses as a combinatorial possibility. No dynamics, profile scan or new ring arithmetic. This is a local Boolean consequence of the known G equation; GC749's earlier 1010/1100 swap control is related, not an infinite continuation result.

Let V and W be two genuine G-time diagrams, and suppose their entire profiles agree at every site left of k. Write delta_k(t)=V_k(t) xor W_k(t). Both obey Delta V_i=V_(i+1) OR V_(i+2), and likewise for W. The fixed equation at k-2 gives

    delta_k(t)=1 implies V_(k-1)(t)=1.

The fixed equation at k-1 also gives equality of the two ORs at sites k,k+1. Whenever delta_k(t)=1, their common OR is1: if V_k=1 this is immediate; if V_k=0 the candidate W_k=1 forces it. Thus

    V_(k-1)(t+1)=1 xor1=0,
    delta_k(t+1)=0.

A first differing profile has no consecutive temporal differences, including across a periodic wraparound. This does not assign a temporal period or assert that every isolated pulse is possible.

Now enforce the changed column's own equation and its agreement at t+1. There are two cases at time t:

- If V_k=1 and W_k=0, the fixed left OR forces W_(k+1)=1. Hence W_k(t+1)=1, and V_k(t+1)=1 requires V_(k+1)=V_(k+2)=0. The reference four-bit pattern is1100, while the candidate starts101 at these same sites; W_(k+2) remains unconstrained by these equations.
- If V_k=0 and W_k=1, the fixed left OR requires V_(k+1)=1. Hence V_k(t+1)=1, and W_k(t+1)=1 requires W_(k+1)=W_(k+2)=0. The reference starts101, while the candidate four-bit pattern is1100.

In either case the first difference is accompanied by a difference at k+1: the two adjacent bits01/10 are swapped. A down-flip1->0 needs a reference1100; an up-flip0->1 needs reference101 and makes candidate1100. These are necessary local guards, not sufficient conditions for a full right continuation.

**GC770 repair audit and unexpected parity limit.** Its reference111 at sites1,2,3 and down-flip at site2 violate the1100 guard. At that tick the fixed left equation forces candidate site3 black, so the changed column's next bit is black; the reference next bit is white. But the preceding reference site becomes white and forbids a next-time difference. No farther-right choices can repair that contradiction while preserving the two left profiles. GC770 correctly rejected the pulse diagram; this proves the failure cannot be repaired just by adding right profiles.

The no-consecutive-differences guard alone does not force even deviation parity: a310-periodic abstract word with one1 and309 zeros obeys it and has odd weight. This word is not asserted compatible with the ring masks or any Rule30 diagram. Therefore the guard does not ban GC769's odd-correlation bridge or close critical uniqueness. The full temporal/profile coupling and farther continuation remain necessary.

**Disposition.** Use the paired-swap and one-tick clearing guards when auditing a first profile departure from the all-L reference. No census or new candidate follows; Q6 remains open. Independent hand reading requested, no run. L402/cf138a49's explicit hand acceptance and promotion of G252, including its summary, verified and acknowledged. Scratch deferred without retry; break room closed.

*Independent reading (Local L403, 2026-10-09).* Verified by hand: the k-2 equation equates V_(k-1) or V_k with V_(k-1) or W_k, so a difference forces V_(k-1) = 1; the k-1 equation makes the common OR 1, so V_(k-1) is 0 next tick and the difference clears; the two cases give the 1100 / 101 swap at k+1. Checked exhaustively: over every assignment of the cells the three equations touch (sites k-2 .. k+2, two ticks, W free at k, k+1, k+2), the 960 consistent pairs show no violation of the pin, the one-tick clearing, the swap or the two four-bit patterns. Scope as stated: necessary local guards, no continuation and no parity ban.
