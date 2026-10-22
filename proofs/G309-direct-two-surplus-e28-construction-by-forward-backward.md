# Direct two-surplus E28 construction by forward/backward subdivision

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT309. Direct two-surplus E28
construction by forward/backward subdivision (2026-10-16)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A four-move parent with simultaneous forward/backward subdivision constructs all2,919 even
E28 targets with two positive high surpluses and t4<112. PROVED after Cloud CL422, with the
span portion independently checked over the full finite parameter family.

**Why it matters.** Choosing which end of a negative edge receives positive moves controls
position collisions and span. General endpoint allocation and the wider E28 region remain open.

## The formal statement and proof

**Status: PROVED after Cloud's carrying read and independent re-implementation, CL422/fde83bd8.**
Source: GPT-MATH-INSTINCT.md MI090, first committed a221b287; formula certificates MI091.
Statement: every sorted even E28 tuple (t1,t2,t3,t4,112,112,112+2a,112+2b) with
t4<112 and 1<=a<=b<=5 partitions the first28 positive odd numbers. E28 means each
target lies in68..122 and their sum is784. The subfamily has2,919 members.
The argument below is verbatim; its historical sketch label is superseded by this review.

Put q=a+b, R=W-q. Since u+v>=12>q, W>q and R>0. Then R+Z=u+v. We have W<=21
(as MI088), v<=17 (u+3v+q<=56), and always a,b<=5. Bin indices carry
(u,v,-W,-Z,0,0,a,b). Select exactly one token in each nonzero bin.

**Split cases, all with distinct positions.**
1. If W=v then Z=u+q<=v. Use (+u,+a,+b,-Z) at 0,u,u+a,Z and (+v,-W) at
1,v+1. All six positions are distinct; v<=14, so span<=15.
2. If {R,Z}={u,v}, use a 4-cycle and a 2-cycle. If R=v,Z=u, use (+u,-Z)
at 0,u and (+v,+a,+b,-W) at 1,v+1,v+a+1,W+1. Here W<=19 and span<=20.
Otherwise R=u,Z=v: use (+u,+a,+b,-W) at 0,u,u+a,W and (+v,-Z) at r,r+v.
Choose the first r in {1,2,3} with r+v distinct from u+a,W. At most two r are forbidden,
r<u, and the six positions are distinct. W<=19, v<=14, so span<=19.
3. If W=v+d,Z=u+c with (c,d)=(a,b) or (b,a), use (+u,+c,-Z) at 0,u,u+c
and (+v,+d,-W) at r,r+v,r+v+d. Again choose r in {1,2,3} avoiding the two possible
equalities r+v=u+c and r+v+d=u+c. W=v+d<=16 (2v+d<=28, d<=5), span<=19.

**Nonmatching ordinary parent.** If R>=Z, take the cycle (+v,-Z,+u,-R) at
0,v,A,R, where A=R-u=v-Z>0. Its positions are distinct; R=v would have been paired.
Subdivide -R using +c,+d,-W at R,R+c,W, with {c,d}={a,b}. The new endpoint W can
collide only with v, already handled in case1. An intermediate collision requires R+c=v;
choose the other order. If both orders collide, a=b and v=R+a, hence W=v+a,Z=u+a,
which is case3. All six are distinct with span max(v,W)<=21.

If R<Z, start the cycle (+v,-R,+u,-Z) at 0,v,A,Z with A=v-R=Z-u>0.
Subdivide backward: replace -R at v by -W at v, +d at A-q and +c at A-c, where
c+d=q. The path goes v -> A-q -> A-c -> A, the old endpoint. Thus the two new positions
are A-c and A-q; normalize after adding them. This is the reverse-reflected version of
forward subdivision, written directly to keep its coordinates unambiguous. Each new point
is below A and can meet an old point only at 0. A=q would imply W=v, case1.
Choose c from a,b with c!=A; if neither is possible, a=b=A and W=v+a,Z=u+a, case3.
Thus this gives six distinct positions. Span D=M+max(0,q-A). If A>=q, D=M<=20:
W=21 would force v<=7, R>=11, Z<=3, contrary to R<Z. If A<q and v>=Z then
D=R+q=W<=20 for the same reason. If A<q and Z>v then D=u+q<=21: combine
2R+q>=u+v>=2u with R+q+v<=28 to get 2u+q/2<=28, so u+q<=21.5.
Equality D=21 forces q=10,u=v=11,R=6 or7. R=6 is case3; R=7 gives only
(u,v,W,Z,a,b)=(11,11,17,15,5,5), with shape {0,5,6,10,17,21}; root1 works.

**The other span-21 cases.** In R>=Z, span21 means W=21 and v<=7. Positivity
Z=u+v+q-21 and 6<=u<=v enumerate exactly seven tuples. For the displayed forward
shape use c=b. Literal direct folded labels for these prescribed roots will be checked:

| u | v | W | Z | a | b | root |
|---|---|---|---|---|---|---|
|6|6|21|1|5|5|1|
|6|7|21|2|5|5|1|
|6|7|21|1|4|5|1|
|7|7|21|3|5|5|4|
|7|7|21|2|4|5|0|
|7|7|21|1|3|5|2|
|7|7|21|1|4|4|1|

All remaining shapes span<=20, so MI087 gives a reflection-free translation. Filling the
remaining complementary-pair slots and simultaneously permuting the selected tokens produces
the desired sums with all first28 odds used exactly once. This is a PROOF-SKETCH, independent
of any assertion that the abstract four-point parent was itself reflection-free; only its
displacement identity is used. This avoids importing B34's root exceptions or B35's repairs.


**Review provenance and proof mode.** Cloud checked the split constructions, forward collisions
and backward endpoints by hand. For the backward subcase span bound and its exceptions, Cloud
instead independently re-implemented the text over the whole constraint-derived family:2,919
inputs, identical branch counts, no distinctness failure or span above21, exactly the eight
listed span21 cases and a complement-free root for every input. Thus that part of the independent
verification is a complete finite check, not a claimed all-hand second proof. The elementary
inequality 2u+q/2<=28 in the original argument remains available in full above. CL422 also
independently recounted the broader4,523-target region; that recount does not independently
adopt B34/B35's other hand arguments.


**Filing check.** proof_dupes hard checks pass. Nearest older entries G308, G307 and G306: read; this uses the geometry bound for a two-surplus family, distinct from either boundary predecessor.
