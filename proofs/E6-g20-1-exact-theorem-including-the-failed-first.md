# G20.1. Exact theorem, including the failed first prediction

*Theorems proved by GPT. Derived from [PROOFS.md](../PROOFS.md), entry "E.6. G20.1. Exact theorem, including the
failed first prediction"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved by GPT (statement in PROOFS.md; the proof is copied below from RULE30-GPT.md).

## In plain words

For walls with one white beat per odd period of 5 or more, even four columns of the right side allow every pattern.

**What it says.** Ask the first four columns on the right to obey Rule 30 (the width-four relaxation). For walls
with one white beat per odd period p of 5 or more, every sequence of column-1 bits at the white beats is still
possible. GPT predicted the opposite at width four, and the failed prediction is kept.

**Why it matters.** If Rule 30's own consistency rules out these walls at all, the evidence first appears at width
five or more. It tells future searches where not to look.

**An everyday picture.** A lock that gives way to none of the first four picks: if it can be opened, it needs a
fifth.

## The formal statement and proof

*Where:* RULE30-GPT.md, "G20.1. Exact theorem, including the failed first prediction". *Status:* proved by GPT (proof there).

**Theorem.** For every odd p>=5, the width-four relaxation of wall0 1^(p-1)
allows every finite and infinite one-sided sequence of visible hole bits. It has
exactly2^n words of length n and rate1/p bit per time step. Combining G15-G17,
a layer that first restricts these walls, if one exists, has width at least five.
This is not an existence proof for an entire infinite right half or a finite seed.

## The proof, copied from RULE30-GPT.md

*Verbatim from [RULE30-GPT.md](../RULE30-GPT.md), the section named above; the master PROOFS.md holds the statement only.*

**Theorem.** For every odd p>=5, the width-four relaxation of wall0 1^(p-1)
allows every finite and infinite one-sided sequence of visible hole bits. It has
exactly2^n words of length n and rate1/p bit per time step. Combining G15-G17,
a layer that first restricts these walls, if one exists, has width at least five.
This is not an existence proof for an entire infinite right half or a finite seed.

**Blind FC2 was refuted.** The prediction that p5 would first lose freedom at
width four was wrong. Its complete accepting subset graph has no empty edge;
that supplies the theorem at p5, not merely a failure to find a short forbidden word.

### G20.2. Exact all-period certificate

For four state bits x1..x4 encoded by s=sum(xj*2^(j-1)), a step has
xj'=leftj XOR(xj OR rightj), with left1=tau and right4=u.
Allow both u choices. Let W and B be the resulting white and black relations.
Set composition gives B^8=B^16; here are all sixteen image masks for either
power (mask m encodes the states j with bit j of m equal to1):

| Initial s | B^8 and B^16 image mask |
|---|---|
| 0 | 17476 |
| 1 | 17472 |
| 2 | 1028 |
| 3 | 26182 |
| 4 | 17492 |
| 5 | 26182 |
| 6 | 17472 |
| 7 | 50372 |
| 8 | 17733 |
| 9 | 1028 |
| 10 | 1024 |
| 11 | 50372 |
| 12 | 17492 |
| 13 | 26182 |
| 14 | 17472 |
| 15 | 17476 |

The verifier starts from singleton images and applies the displayed Rule30
formula for both u choices, checking these exact integers. Equality of all images
is an equality of relations, so associativity proves B^(k+8)=B^k for every k>=8.
The period macro is first W, then B^(p-1). Thus odd p5 and7 are short exceptions;
p9,11,13,15 represent every odd residue thereafter. No extrapolation from the
largest tested period is needed.

For a visible symbol e, keep starting states with s modulo2=e and union their
macro images. Start with I={0,..,15}, mask65535. For each of the six representative
odd periods, the reachable subsets are exactly I, E and H, with masks
E=59351 and H=59078. In full:
E={0,1,2,4,6,7,8,9,10,13,14,15};
H={1,2,6,7,9,10,13,14,15}.
The same accepting graph holds for all of them:

| Subset | visible0 | visible1 |
|---|---|---|
| I | E | H |
| E | E | H |
| H | H | H |

Each nonempty edge is precisely the union of valid state/input paths through
one period. Induction on the visible word proves exact language equivalence
between these subsets and the original layer; the table never reaches empty.
Consequently every finite word has a hidden layer path. For a specified infinite
visible word, the arbitrarily long finite paths form a finitely branching tree;
an infinite branch gives a consistent infinite state/input history. This proves
the infinite-language statement. It leaves the outside input unconstrained, as
the theorem's relaxation requires.

The p3 graph was separately checked: an initial all-zero-visible loop enters
states with transitions exactly as in G17's forbidden100 graph. Its visible
language remains words avoiding100. No new even-period classification is claimed
in this block; CF at width two,p4 is an instrument control only.
