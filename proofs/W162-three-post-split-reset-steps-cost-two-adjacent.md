# Three post-split reset steps cost two adjacent run lengths

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G162. Three post-split reset
steps cost two adjacent run lengths (2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

After a genuine split, three reset steps cost either the current run length plus two, or the current and next run lengths plus two. The known first split costs at most eight. The same temporal difference orders can accompany a much larger cost elsewhere, so those orders alone do not bound waiting.

## The formal statement and proof

**Statement.** At a genuine even-parity zero-driver node (a,0) of least period q, the complementary integrated children are c and1 XOR c. Let r be the arrival phase and suppose the gate a(r-1)=1 holds. Then r starts a constant run of c. Let ell and m be the lengths of this run and the next one, respectively. For G8's full-line reset front, the unordered pair of elapsed costs over the next three nonzero drivers is

    {ell+2, ell+m+2}.

In particular the worst sibling cost is at most q+2. This bound is attained on the gated compatible domain at every dyadic q>=4, so these three steps do not have a uniform period-independent cost bound. Root reachability of the attaining family is not asserted.

**Proof.** Since Delta c=a is nonzero, c is nonconstant. The next driver d satisfies S d=c OR d; periodicity and a black reset force d=1. The following driver e satisfies S e=1 XOR c, hence e(t)=1 XOR c(t-1). For the complementary child the same reasoning gives drivers1 and1 XOR e. These are exactly the next three drivers on each continuation.

If c(r)=1, the first reset costs1 and reaches r+1; the constant-one driver costs1 more. The first one of e at or after r+2 is at r+ell+1, including the ell=1 endpoint. Its reset therefore finishes at r+ell+2. The complementary child initially has zeros of length ell, so its first reset finishes at r+ell+1, and its constant-one reset at r+ell+2. Its third driver is c(t-1); the next c-one starts after the following zero run of length m. That reset finishes at r+ell+m+2. When c(r)=0 interchange the two children. Subtract the initial r to obtain the formula. Adjacent runs occupy at most one period, so ell+m<=q.

For sharpness take c to have one black cell at q-1 and zeros elsewhere, with r=0. Then ell=q-1 and m=1. Its difference a has black cells only at q-2 and q-1, least period q for q>=4 and even parity. The parent gate holds because a(q-1)=1. Both integrated children close at period q, and the larger three-step cost is q+2. This is an ambient compatible witness, not a rooted one. Square.

**Known rooted control, not a new search.** Local L118 and GPT's backward audit give a=0000110001010011. Choosing c(0)=0 integrates to c=0000010000110001. G160's gate allows phases0,5,6,10,12,15. The respective (ell,m) pairs are(5,1),(1,4),(4,2),(2,3),(3,1),(1,5); therefore the two unordered costs are{7,8},{3,7},{6,8},{4,7},{5,6},{3,8}. The maximum is8. An independent literal reset scan checks all six table entries and the same-order cost18 counterexample, without a continuation search. This certifies only the first three full-line reset steps after the known split; it gives no later cost or actual transient maximum.

**Difference-order guard.** At dyadic q>=8, put a single pulse g at q-1 and take c=Delta g, a=Delta^2 g, r=0. Then c has its two adjacent ones at q-2,q-1, a has two ones at q-3,q-1, the gate holds, and the least periods remain q. Since nu(g)=q, their orders are nu(a)=q-2 and nu(c)=q-1. The cost maximum is again q+2. At q=16 this has exactly the known rooted witness’s orders14 ->15 but cost18 rather than8. It is not asserted rooted. Thus these scalar difference orders do not alone control local reset cost on the gated compatible domain.

**Identified unexpected check and scope.** At ell=1 the third driver is already black at its arrival, so its cost is1, not0: the fast sibling cost is3. The sharp gated single-black-cell family rejects a uniform local three-step slope below3 once q>=8, despite the structural seven-depth branch spacing. A period-dependent potential could still absorb such a finite cost; no uniform potential-size bound is disproved. Existing G2.3, G8, G159 and G160 are the relevant prior records; this is direct run-length accounting, with no novelty claim or new search. Birth clamps, rooted all-branch control and sublinear period growth remain separate obligations.
