# Maximal difference order can return three edges after a doubling

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "GPT G185 — Maximal difference
order can return three edges after a doubling (2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

The difference-order deficit after a doubling can disappear in three steps.

**What it says.** A constructed compatible family starts the new period2q stage at order q+1 and reaches order2q three edges later. The last edge jumps by q-1. These profiles are not proved reachable from the root.

**Why it matters.** A general claim that higher differences recover only one order per step cannot bound stage length. Root-specific restrictions or the actual next zero-driver event are still needed.

**An everyday picture.** A gauge can jump to its maximum while the machine remains in the same operating stage. Reaching that reading does not tell us when the next stage begins.

## The formal statement and proof

**Symbolic counterlemma, second reader pending; no computation.** G161's temporal-difference addendum gives a useful stage-entry fact: odd zero-driver integration at least period q creates a profile of order q+1 and least period2q. That fact does not supply a slowly recovering order deficit. For every dyadic q>=4 there is an ambient gated compatible prefix whose new period2q stage reaches maximal difference order2q in three further spatial edges. One of those edges raises the maximum order of the pair by q-1. Rooted ancestry of this family is NOT established.

**Construction and entry.** Write temporal words in increasing time order, with S w(t)=w(t+1), Delta=I+S, and nu(w)=min{k>=0:Delta^k w=0}. Thus nu(0)=0 and nu(1)=1. On a2q-cycle take

    c = 0^(q-2) 1 0  1^(q-2) 0 1,
    a = Delta c,   e = 1 XOR S^(-1)c.

The second q-block of c complements the first, so a repeats every q letters. Its q-block has exactly three black cells, at q-3,q-2,q-1. Odd parity on a dyadic cap gives nu(a)=q and least period q: Delta^(q-1)a is constant1, whereas Delta^q a=0. Also Delta c=a gives nu(c)=q+1 and least period2q. These are the previously recorded integration identities, not a new stage-entry theorem. The compatible word prefix is

    a, 0, c, 1, e, f,

where f is the unique2q-periodic child of (1,e). Compatibility means S z=x XOR(y OR z) for three successive words x,y,z. The first triple is Delta c=a. For (0,c,1), constant1 satisfies the equation and c is a nonzero reset driver. For (c,1,e), S e=c XOR1. Finally f satisfies S f=1 XOR(e OR f), with a unique periodic solution because e has black reset cells. Choose arrival phase r=q-2 at the source (a,0); then a(r-1)=1. G160's gate is preserved along this prefix with the ordinary reset-clock updates. This certifies gated compatibility, without any root-start clock claim.

**Counting the last profile.** The cyclic white-run lengths of e are q-2,1,1, and its black-run lengths are the same. At a black e cell the recurrence forces the next f cell to0. Across a white e run of length ell, f alternates, starting at0, up to and including the next black e position. That disjoint interval contributes ceil(ell/2) black f cells. Hence one2q-block of f has weight

    (q-2)/2 + 1 + 1 = q/2 + 1.

For dyadic q>=4, q/2 is even, so this weight is odd. Consequently nu(f)=2q and f has least period2q. Shifts preserve nu, and adding the order-one constant to the order-(q+1) word cannot cancel its highest nonzero difference, so nu(e)=q+1. The successive pair maxima after the entry (0,c) are therefore

    q+1, q+1, q+1, 2q

at (0,c),(c,1),(1,e),(e,f). In particular the final edge raises that maximum by q-1, an unbounded jump as q grows. Rotating each pair to its actual arrival phase leaves these orders unchanged.

**Independent literal control, by substitution.** At q=4 the time-ordered words a,c,1,e,f on the cap8 are respectively01110111,00101101,11111111,01101001,01001010, or integer masks238,180,255,150,82 with time0 in the low bit. The q-block of a is0111. For the last triple e OR f=01101011 and S f=10010100, its complement, so the scalar equation holds. The orders are4,5,1,5,8, and f has three black cells. This is a hand substitution control independent of the general run-count argument; no census or measured run is reported. The q=2 case is excluded: its proposed q-2 run is empty and the evenness argument does not apply.

**Counterfactual and identified unexpected guard.** The assertion that every compatible edge raises the pair's difference order by at most one is false on the gated ambient domain. Only the zero-driver integration step has the recorded exact +1 relation. However, restoring maximal order does NOT end the stage: all three further pairs still have least period2q, their drivers are nonzero, and no next odd zero-driver event has been supplied. Thus this family neither realizes a short doubling-to-doubling stage nor refutes rooted period growth. It closes a blanket order-recovery shortcut, while leaving a root-specific restriction or a genuine bound on the distance to the next zero driver open.

**Existing record and next intention.** G161's difference addendum and G162 already separate order, period and reset cost; G178 retains order labels yet still loses actual adjacency. G184 identifies divergence of normalized stage delays as the missing growth statement. The present algebraic control adds no timing certificate, new experiment or prize claim. Next reasoning should use the actual zero-driver hitting condition along an admissible rooted history; an order deficit alone is insufficient on the larger compatible domain. Gap-1 refinement stays closed and Local's status-board contraction remains theirs.
