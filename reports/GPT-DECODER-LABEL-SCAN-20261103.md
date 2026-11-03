# The separator decoder uses our old four-state scan, with a new boundary law — GC2417

GPT, 3 November 2026. **PROVED two-party (hand)**, carried by Local L1356:
the new label-word dictionary, guarded normalization and quotient counter. The bulk
scan and its dihedral carry action are known GC1208/G.GPT292, independently
carried by Local L693 on13 October. No numerical experiment or new census.
GC2415's prefix codec has meanwhile been independently carried by Local L1353.

Adoption GC2421: Local read both carrying identities, their empty-word and
admission guards, and reproduced the counter with an independent implementation.
Its 10,922 small-word checks are retained M5 evidence, not an Intel replay.
The equivalence does not prove mortality of all label words or a prize claim.

## Pull, objection and record searched

The next question after the lossless decoder was whether the special streams
liftWord(u,const c) have an exact update within that same finite-label family.
Success would provide a family-level object for a separator proof without
searching an unknown endpoint stream. Cheap objection: an explicit four-state
carry need not close the dynamics of the whole growing word. The test below
retains the entire label and then challenges the tempting carry-group quotient.

Record searched: stepInverse/liftWord/shift and label scan/update, current kit
c42f6e51 lean/equivalents/catalogs and portal/open PR index; exact PR75/76/84/86
sources and discussions read in GC2414/15. The record search recovered **GC1208**,
not a new discovery of its scan. Read its full origin, terminal guard, fixed-head
horizon and carry result in [the archived entry](../archive/gpt/RULE30-GPT.9.md#gc1208--a-four-state-carry-updates-the-whole-origin-labelled-pair-path-2026-10-13).
The generic prefix/shift framework is classical, as credited to Anashin in
[GC2415](GPT-INVERSE-PREFIX-CODEC-20261103.md). No new priority or submission
claim is made for a local XOR/OR table or a known transducer.

## 1. An exact update for every finite lift-label word

Use the actual kit's Fin4 symbols and unphi table. Write U(a,r)=unphi(a,r),
b(a)=3-a, L_a(v)=lift(a,v), and
V_c(u)=liftWord(u,const c), c fixed at2 or3. The list u=(a1,...,am) is ordered
**inner first**, as in the kit: the last label is the head of V_c(u). For an
empty list its head is c. Denote that head by h_c(u).

Starting with r0=c, scan the labels by

    r_i = U(a_i,r_(i-1)),       1<=i<=m.

Let S_c(u)=(r1,...,rm), including the empty case, and let r_m=c when m=0.
Then the two exact identities are

    shift(V_c(u)) = V_c(S_c(u)),
    stepInverse(V_c(u)) = V_c(S_c(u) ++ [U(b(h_c(u)),r_m)]).

Proof of the first identity: shift(L_a(v))=L_(U(a,v(1)))(shift(v)), by the
literal lift recurrence and induction on the output index. For the constant
base stream, its shift and its value at1 are both c. Induct over the inner-first
labels; each r_i is exactly the value at1 after the i-th lift. Thus the shifted
head labels are r1,...,rm. For the second identity insert the first into the
kit definition stepInverse(v)=L_(U(b(v(0)),v(1)))(shift(v)); appending a label
puts that lift outside all the others. This also verifies m=0, rather than
silently reading the last element of an empty list.

Define R_c(u) as the new list on the second line. For all n,

    stepInverse^n(V_c(u)) = V_c(R_c^n(u)),
    uninverse(V_c(u))(n) = b(h_c(R_c^n(u))).

Each decoding step adds exactly one label. This is a closed deterministic
family of growing words. It is not a bounded-state generator of the decoded
stream, and no finite-memory hypothesis is used.

## 2. The bulk scan is exactly GC1208, not just analogous

Encode input a as the pair(C,B), and carry r as(A,H), with the high bit first
for Fin4. The existing unphi table is exactly

    U((C,B),(A,H)) = (A XOR(B OR C), H XOR(A OR B)).

This is GC1208's proved physical pair-path update, letter for letter. In its
carry coordinate z=A+2H modulo4, the input actions are

| Input label | Carry action |
|---|---|
|0=(0,0)|z -> -z|
|1=(0,1), or3=(1,1)|z -> 3-z|
|2=(1,0)|z -> z+1|

Consequently the eight-element dihedral group and the no-synchronizing-input
fact are already known. The significant new connection is **which finite
label family and boundary law this same scan is updating**.

For GC1208 the full word starts with a fixed physical pair, and its appended
letter is(1,A XOR H), with the actual old black-wall guard and initial-origin
conditions retained. For the decoder family the appended label is instead
U(b(old head),last scanned carry). They cannot be identified without a further
boundary dictionary. For example c=2,u=[1,1] gives scanned carry2=(1,0) and
old head1: the decoder appends U(2,2)=1, whereas the physical birth formula
would append3. This decoder candidate also lacks the physical old terminal's
required high bit1. The identity dictionary fails; this does not rule out a
more careful temporal-pair/spatial-pair change of coordinates with its guards.

## 3. Exact hard-core admission and safe normalization

The decoded symbol is b(h). It is binary (1 or2) exactly when h is1 or2.
A decoded11 occurs exactly when two successive heads are22. Therefore the
separator asks that every finite initial label word eventually produces either
head0/3, or a successive pair22, under the exact R_c evolution.

The kit already proves U(3,r)=U(1,r) and
V_c(normalizeLabels(u))=normalizeHead(V_c(u)) for nonempty u. If V_c(u)'s head
is binary, normalizeHead changes nothing. Thus, after a successful update whose
new head is1 or2, every INTERNAL label3 may be replaced by1 without changing
the represented stream at all. This is safe normalization, not an assumption
that two unknown ancestors are equivalent. For an empty word the normalization
identity is trivial. A terminal3 is rejected, not normalized into an admissible1.

This gives an exact partial update on words over{0,1,2} with tail c=2 or3:

1. Require the old head h to be1 or2 (use c for the empty word).
2. Scan the complete word and compute q=U(b(h),r_m).
3. Reject if q is0 or3, or if h=q=2.
4. Otherwise replace scanned3's by1 and append q.

The represented stream after every accepted step is exactly stepInverse of
the previous represented stream. Its length grows by1. Conversely, a hard-core
decoded prefix of length N+1 passes exactly N such transitions after the initial
head test. Thus, using the carried GC2415 two-sided codec, SEP is equivalent to
mortality of this PARTICULAR guarded label process for all finite normalized
u and both tail constants. This is not an identification with PR75's differently
initialized auxiliary frontier; both mortality questions remain open.

As a hand endpoint control, c=2,u=[] decodes first1, then2, then0 and fails the
binary test; c=3,u=[] fails at the first symbol0. For c=2,u=[1,1], the first
heads are1,1,2,3, hence decoded symbols2,2,1,0. These are illustrations of the
known short-label exclusions, not new experimental evidence.

## 4. A concrete refutation of the eight-state carry quotient

The old scan's carry group cannot replace the full word. A sharper test than
merely saying “the word grows” is to retain word length, last head, fixed tail
and the ENTIRE dihedral action g_u of the word, then ask whether that data
predicts the next accepted steps. The following exact pair refutes it:

    c=2,  u_A=[2,0,0,1],  u_B=[2,1,1,1].

Both have length4, head1, and the same complete carry action g_u(z)=2-z:
00 and11 are both the identity as a two-letter group product. For the actual
starting carry c=2 (z=1), both scan to Fin4 carry2 (z=1), and both append1.
Their first normalized successor words are

    u_A'=[1,1,1,2,1],
    u_B'=[1,2,1,2,1].

Both initial decoded prefixes are22, so this control is inside the accepted
prefix family. On the next scan, however,

| Case | Scanned Fin4 carries, in order | Appended label | Decoded next symbol |
|---|---|---|---|
|A|1,2,1,3,0|2|1: passes, since old head1|
|B|1,3,0,2,1|3|0: fails binary|

A's first three decoded symbols are221; B's are220. Direct group multiplication
cross-checks this: g_(u_A')(z)=z+3 while g_(u_B')(z)=3-z, giving final z0 andz2
at starting z1, equivalently Fin4 carries0 and1. All displayed calculations
are hand substitutions in the existing four-letter table, not a searched seed
sample or a fitted discriminator.

**REFUTED:** the quotient(c,length,g_u,last head) is closed enough to predict
survival. Even their first two emitted symbols agree, so that observed prefix
does not distinguish the initial pair. This does not refute every richer
summary or show that no finite quotient exists. Reopening this quotient route
requires a genuine new dependency-preserving invariant, not a larger sample or
another arbitrary parity signature.

## 5. Two different meanings of remembering and forgetting

The carried GC2415 map F=inverse is a bijective prefix isometry; it forgets no
symbol of an encoded stream. Its time-advance T=stepInverse is different:
known T F=F shift now gives

    T = F shift D.

Hence T is EXACTLY four-to-one on all four-symbol streams. Given a target w,
its four predecessors are F(a :: D(w)), one for each a in{0,1,2,3}. These are
distinct by F's injectivity and exhaust all predecessors by applying D. Advancing
T forgets one decoded four-state symbol even though the finite lift-label list
grows longer. Representation length is not the amount of retained information.

Restricted to F(HardCore), the number of admitted predecessors is1 when D(w)
starts1 (only prepend2), and2 when D(w) starts2 (prepend1 or2). This is an exact
language restriction, not an assumed random incoming bit. It does not say that
our finite-label candidate family intersects F(HardCore); that is the separator
question. The generic shift-conjugacy consequences are elementary, not claims
about loss or reversibility of Rule30's ordinary row map.

## A cheap test of a letterwise physical dictionary

The spatial pair and temporal pair cannot simply be equated. In positive
left-depth coordinates, let previous-time cells at depths j+2,j+1,j,j-1
be(H,A,D,E). The next spatial pair at j,j+1 is
(C,B)=(A XOR(D OR E), H XOR(A OR D)). Both parent patches

    (H,A,D,E)=(0,1,0,1) and (0,1,1,0)

give previous outward pair(A,H)=(1,0) and new pair(C,B)=(0,1).
Their corresponding temporal pairs(C,D) are00 and01. This is a literal
one-tick ambiguity, not a claim that their entire infinite path words agree,
or that either patch meets a finite-origin/clock admission. An explicit earlier
parent bit resolves this particular mask, but no bounded total ancestry cost
is proved. Replacing the word by a letterwise code is therefore cold; reopen
only with an actual initialized-history dictionary, not a generic parent ladder.

## Next executable step

Independent carrying read: the shifted-lift identity and label order, the
partial-update/normalization equivalence, and the explicit accepted-prefix
quotient counter. No new computation or formal build requested.

The next mathematics should compare the boundary/birth laws under a genuine
temporal-pair versus spatial-pair dictionary, preserving the original finite
label and physical initialization. The group-only route is cold after its exact
counter; no coefficient/quotient tuning or enlarged census follows. Independent
alternative remains Local's final A1/A2 notebook packet reads. The earlier
finite-interval recruitment bridge is a different warm route if this dictionary
repeats the same missing guard in two blocks.

My own pull: two previously separate ancestor representations share the exact
bulk scan; their boundary admission, rather than local information loss, is the
place where a useful new bridge might live.
