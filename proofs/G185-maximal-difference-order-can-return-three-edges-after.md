# maximal difference order can return three edges after a doubling

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT185. maximal difference
order can return three edges after a doubling (second-read by Local, 2026-10-07)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The difference-order deficit after a doubling can disappear in three steps.

**What it says.** A constructed compatible family starts the new period2q stage at order q+1 and reaches order2q three edges later. The last edge jumps by q-1. Local verifies the q4 member on the rooted history; rootedness beyond it is unproved.

**Why it matters.** A general claim that higher differences recover only one order per step cannot bound stage length. Root-specific restrictions or the actual next zero-driver event are still needed.

**An everyday picture.** A gauge can jump to its maximum while the machine remains in the same operating stage. Reaching that reading does not tell us when the next stage begins.

## The formal statement and proof

### GPT G185 — Maximal difference order can return three edges after a doubling (2026-10-07)

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

*Second reader's note on G185 (Local, 2026-10-07; chat L147).* Correct, and at $q = 4$ more than claimed. The
construction checks out: $c$'s second $q$-block complements its first, so $a = \Delta c$ has period $q$ with block
$0^{q-3}111$. At a black $e$ cell the equation forces $S f = 1 \oplus 1 = 0$, and across a white run it reads
$S f = 1 \oplus f$, so $f$ alternates; the run count follows. Checked (`rule30_audit_g99_g100.py`, S75) at
$q = 4, 8, 16, 32, 64$ with $f$ taken as the single periodic child of $(1, e)$. The four triples are compatible. The
orders are $q, 0, q + 1, 1, q + 1, 2q$, with least periods $q$ for $a$ and $2q$ for $c, e, f$. $f$ has weight $q/2 + 1$,
and the pair maxima are $q + 1, q + 1, q + 1, 2q$. The three later pairs keep least period $2q$ with nonzero drivers,
and G160's gate holds at all five pairs from arrival phase $q - 2$ under the reset-clock updates. The $q = 4$ masks
match, with $f$ confirmed by brute force. On the excluded $q = 2$: $f$ still has order 4 (its weight is 1), so the order
conclusion survives there. What fails is the run-count formula and the gate at $(a, 0)$ from phase 0. Rooted ancestry at
$q = 4$ is established, not open. RQ3's reached $q = 8$ graph passes through this exact prefix at depths 28 to 32 by
consecutive edges, with arrival phases equal to G185's plus 5 on the 8-cycle. So the actual history enters period 8 at
$N_3 = 29$ and recovers order 8 three edges later, a jump of 3 on the edge from 31 to 32. Seven reached edges at $q = 8$
make that jump, the largest on the graph. The $q = 8$ member is not rooted in this way: the rooted cap exit at depth 399
has $a$-block $10000101$, not $00000111$. Beyond $q = 4$, rooted ancestry stays open, as G185 says.


**GPT incorporation of L147 (2026-10-07).** Local S75 independently verifies the family for q4 through64 and locates the q4 member on the rooted history at depths28 through32, with arrival phases shifted by5 on the cap8 cycle. Thus the rooted period8 stage starts at depth29 with order5 and reaches order8 at depth32; the stage continues through its zero-driver exit at depth399. Rootedness for the larger members remains unproved here; the q8 member is not the rooted cap16 exit word, as Local observes. At q2, direct substitution gives c=1001, a=1010, e=0011, f=0100, with f of weight1/order4. So the order conclusion survives, although the three-run proof degenerates. The stated arrival choice r=q-2=0 fails its gate since a(3)=0. The theorem retains q>=4; the q2 exclusion is not an assertion that maximal order fails to return. Local's verified filing is preserved.
