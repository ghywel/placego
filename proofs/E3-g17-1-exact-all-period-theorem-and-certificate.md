# G17.1. Exact all-period theorem and certificate

*Theorems proved by GPT. Derived from [PROOFS.md](../PROOFS.md), entry "E.3. G17.1. Exact all-period theorem and
certificate"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved by GPT (statement in PROOFS.md; the proof is copied below from RULE30-GPT.md).

## In plain words

For walls with one white beat per period, checking three columns on the right rules out no more than checking two.

**What it says.** Instead of asking for a whole right half obeying Rule 30, ask only that the first k columns obey
it, with the next column free (a "relaxation of width k"). Which patterns of column 1 at the white beats are then
possible? For walls with one white beat per period p, widths two and three give the same answer: for even p, never
two black in a row; for p = 3, never black, white, white; for odd p of 5 or more, anything.

**Why it matters.** It tests whether the right side's own rules squeeze the channel. Here the third column adds
nothing visible, even though it changes what happens out of sight.

**An everyday picture.** Checking an alibi with more witnesses: the third witness tells you nothing the second did
not.

## The formal statement and proof

*Where:* RULE30-GPT.md, "G17.1. Exact all-period theorem and certificate". *Status:* proved by GPT (proof there).

**Theorem.** For every p>=2, width-three and width-two relaxations of wall0 1^(p-1)
have exactly the same finite and infinite one-sided hole languages. Thus even p
avoids11; p3 avoids100; odd p>=5 is unrestricted. G16's counts and entropy rates
remain exact for this relaxation. The third cell neither lowers these rates nor
removes any visible word, even though it constrains the hidden dynamics.

## The proof, copied from RULE30-GPT.md

*Verbatim from [RULE30-GPT.md](../RULE30-GPT.md), the section named above; the master PROOFS.md holds the statement only.*

**Theorem.** For every p>=2, width-three and width-two relaxations of wall0 1^(p-1)
have exactly the same finite and infinite one-sided hole languages. Thus even p
avoids11; p3 avoids100; odd p>=5 is unrestricted. G16's counts and entropy rates
remain exact for this relaxation. The third cell neither lowers these rates nor
removes any visible word, even though it constrains the hidden dynamics.

**Proof by finite relation certificate.** Encode three cells as s=a+2b+4c.
For external input u, an update is
(a',b',c')=(tau XOR(a OR b), a XOR(b OR c), b XOR(c OR u)).
Let W and B be the white and black relations, allowing both values of u.
Composing B five times gives these image masks: an integer mask m represents the
set of states j for which bit j of m is1.

| Starting s | B^5 image mask | B^9 image mask |
|---|---|---|
| 0 | 102 | 102 |
| 1 | 68 | 68 |
| 2 | 68 | 68 |
| 3 | 85 | 85 |
| 4 | 196 | 196 |
| 5 | 84 | 84 |
| 6 | 68 | 68 |
| 7 | 69 | 69 |

These eight images follow by applying the displayed update to each current image
for u=0,1; the probe retains the complete set-composition verifier. Equality of
all images proves B^5=B^9. Associativity then proves B^(k+4)=B^k for every k>=5.
Hence the white-to-white macro relation (first W, then B^(p-1)) needs only p2..9:
p2..5 are the short exceptions; p6..9 represent every later residue modulo4.
This finite identity is what extends the result to unbounded periods.

For a visible symbol e, filter the current subset to states with s modulo2=e,
then union their macro images. Name the subsets:
I={0,1,2,3,4,5,6,7}; E={0,1,2,4,5,6,7}; E2={0,1,2,4,5,7};
D={0,2,4,6}; H={1,2,5,6,7}; K={1,5,7}.
Starting from I, direct composition for the eight representative periods gives:

| Period | Subset | symbol0 | symbol1 |
|---|---|---|---|
| even p | I | E | D |
| even p | E | E | D |
| even p | D | E | empty |
| p3 | I | E | H |
| p3 | E | E | H |
| p3 | H | K | H |
| p3 | K | empty | H |
| odd p>=5 | I | E | H |
| odd p>=5 | E | E | H |
| odd p>=5 | H | H | H |

For p2 replace E throughout by E2. These are *all* reachable nonempty subsets;
every output in the table is another listed subset or empty. The table therefore
characterizes every finite word, rather than just tested lengths. Empty transitions
exclude exactly11 for even p and100 for p3; odd p>=5 has none. The same finite-
branching argument as G16 supplies a hidden infinite path for every allowed infinite
word. The graphs have exactly G16's languages, which proves the theorem.

**Hidden period is not visible language.** B^5 differs from B^7. For example,
B^5(0)={1,2,5,6}, whereas B^7(0) is different. Thus the two-step black relation
identity used at width two does not transfer unchanged. The visible language still
agrees because projecting and taking unions produces the same accepting graphs.
The exact value of B^7(0) is reconstructed by the verifier; only inequality is
used. This is a concrete example of hidden dynamics changing without changing
an observed channel language.
