# The missing parents at the pyramid's boundary

GPT, GC1981, 27 October 2026. Owner's question: a black path can be traced to the
root, but the edge seems to lack two parents and the root lacks all three. Are
those parents lost, or can the rule force them?

Status: elementary hand derivation, no simulation or independent second read;
no novelty or prize claim. Existing DQ-001 and the GC1883 amplification review
already warn that backward extension need not stay finite. This note answers
the particular full-line single-seed question, with Rule30's standard orientation.

## The parents outside the drawing are white

Write a black cell as1 and white as0. Rule30 is

    y_i = x_(i-1) XOR (x_i OR x_(i+1)).

The standard single seed is1 at position0 and0 everywhere else. At time t,
everything outside [-t,t] is still0. The extreme black cells at -t and t, for
t>=1, therefore have parent triples001 and100 respectively. Both give1.
There are three parent inputs at each edge, even though only one is black.
White cells participate in the computation; drawing only the expanding pyramid
does not remove them.

This statement uses the full known initial row. If one only possesses an
unlabelled cropped photograph, unshown cells are not automatically known white.

## Can the root have an earlier row?

The experiment specifies time0 and does not claim a past. Requiring an earlier
row is a new boundary-value question: find x with output y_0=1 and y_i=0 for
every i!=0. Locally, a black output allows four triples:001,010,011,100.
The requirement that every other output be white greatly narrows the choice.

There is **no finite black predecessor**. If a nonempty finite row's extreme
black positions are L and R, its next extremes are L-1 and R+1, from001 and100.
Its support span grows by2, so it cannot produce a support span of1. The empty
row remains empty.

There are, however, **exactly two bi-infinite predecessor rows**. In the following
display, the divider is between positions-1 and0, and every indicated tail
continues forever:

```text
earlier A:  ...1111 | 0000...
earlier B:  ...1110 | 1111...
next row:   ...0000 | 1000...
```

A has black cells precisely at i<=-1. B is black everywhere except i=-1.
Both produce the isolated root. They do not supply a finite predecessor or an
alternative finite-seed beginning.

To prove completeness, the white outputs at i>=1 require

    x_(i-1) = x_i OR x_(i+1).

Hence x_0,x_1,... is nonincreasing. It cannot drop from1 to0: a drop followed
by the necessarily zero tail would contradict the same equation at that drop.
Consequently this entire right ray equals a single bit a. At i=0 the black
output forces x_-1=1-a. The white output at i=-1 then forces x_-2=1, and all
further cells to the left are forced1. The alternatives a=0 and a=1 give exactly
A and B. Substituting their only nonconstant triples verifies both directly.

## What is forced, and what is forgotten?

For one update, knowing the child y and the centre/right parent bits c,r forces
the left parent l:

    l = y XOR (c OR r).

That is useful for reconstructing a row sideways from boundary information. It
does not say the child alone determines its three parents. Here even the entire
single-seed output has two distinct possible predecessor rows, so one bit of
past choice is irrecoverable from that row alone.

Question -> response -> challenge -> better question:

- The apparent missing edge parents are known white inputs.
- Extending before the root is possible if infinite black backgrounds are allowed.
- It is impossible while keeping the earlier row finite, and the infinite past
  is not unique even one step back.
- When does a backward reconstruction require an infinite background, and can
  that boundary obstruction constrain a proposed finite clock? This connects
  to the existing finite-predecessor issue, without resolving it generally.

The drawing's root is the beginning of the chosen experiment, not a theorem that
no preceding mathematical configuration exists.

## One more step backwards: A has two parents, B has three (GC1982)

The owner asks to continue the inverse tree, noticing that B is a shifted colour
complement of the real root, while A hides two different infinite backgrounds.
This section is another elementary hand derivation, without an enumeration run
or independent second read. Positions and Rule30 orientation are unchanged.

**Answer:** exactly two rows map to A, and exactly three map to B. Consequently
exactly five distinct rows map to the isolated root in two updates. This is a
count of entire bi-infinite rows, not merely cropped triples. It does not imply
a doubling law, a Fibonacci law or any other all-depth counting formula.

The divider below is still between positions -1 and 0. Nine cells are shown on
each side. Extend the indicated far-left repeating pattern and far-right
constant/repeating pattern forever; preserve the displayed junction cells.

```text
parent of A, choice 1: ...010010010 | 000000000...
parent of A, choice 2: ...001001001 | 111111111...

parent of B, choice 1: ...010010011 | 001001001...
parent of B, choice 2: ...100100100 | 010010010...
parent of B, choice 3: ...010010010 | 100100100...
```

For B's first choice the final `11` before the divider is intentional. The
far-left tail repeats010; the defect at the junction is not repeated.

### Why these lists are complete

Given a desired output y and two adjacent parent bits c=x_i, r=x_(i+1), the
remaining parent to their left is uniquely forced:

    x_(i-1) = y_i XOR (x_i OR x_(i+1)).

For A, the outputs at i>=0 are all0. The previous right-ray argument forces
the entire parent ray x_-1,x_0,... to be constant: either all0 or all1. Each
choice extends uniquely leftward through the required black outputs of A.
They give the two rows above.

For B, the outputs at i>=0 are all1. A parent triple producing1 is001,010,011
or100. But011 cannot occur in this right ray: its last pair11 would force the
next output to be0. The remaining triples001,010,100 force a repeating001
ray, with exactly three possible alignments. Each ray again extends uniquely
leftward across B's white cell at -1 and then its black left half. The three
extensions are the displayed rows.

One can inspect the junctions without simulation. In the two A predecessors,
the triples at output positions -1 and 0 are respectively100/000 and011/111,
so the junction outputs are1/0. In the three B predecessors those triples are
110/100,000/001 and101/010, so the junction outputs are0/1. The displayed
periodic tails produce their required uniform outputs. B's first predecessor
also has011 at output position -2, which correctly produces1 before the white
output at -1. This guards the easily missed junction defect.

More generally, the same argument shows that any full target row with an
eventually all-white right tail has exactly two full-line predecessors, and
one with an eventually all-black right tail has exactly three. Choose the
appropriate constant/period-three parent ray sufficiently far right, then
apply the unique reconstruction to the left. This statement concerns uniform
right tails; it makes no claim about predecessor counts for arbitrary tails.

### B is a complemented picture, but its dynamics do not stay complemented

Let S be the isolated black cell at0. B is the colour complement of an isolated
black cell at-1. The owner's description of this single row is correct.
However, Rule30 does not commute with colour complement: both000 and111 map
to0. Thus its white and black uniform backgrounds both become white in one
update. In particular,

    F(A)=F(B)=S,  hence F^t(A)=F^t(B)=F^(t-1)(S) for t>=1.

Both histories join the ordinary single-seed pyramid after one update. If B is
shifted right one cell first, its resulting seed and subsequent ordinary
pyramid are shifted right by the same amount. A colour-inverted future picture
would require a correspondingly transformed update rule.

A is a boundary between two uniform backgrounds. Their interiors both erase
to white immediately; the interface leaves the single black cell. B achieves
the same output through a one-cell hole in a black background. Their common
future forgets which of these very different whole-row pasts occurred.

The period-three precursor is the same local mechanism as in the earlier
triangle work: consecutive black outputs admit the001 cycle. Here we impose
that condition on an infinite tail, which removes terminal exceptions and
forces an exact periodic ray. No new general survival theorem follows.
