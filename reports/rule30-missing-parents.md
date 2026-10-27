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
