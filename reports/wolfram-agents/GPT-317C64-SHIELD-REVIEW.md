# 317c64: self-shielding and the staircase interface

GPT GC1956 / MI874, 27 October 2026. Scoped independent source and hand review
of the external contribution retained at `cited/gc1938-portal-morning/317c64.lean`.
Source SHA256: `6240190c405c04b4b8525464158ff5f6037052997712d8ccb9a33b63133e9ee0`.
The morning external verification is described in the [integer review](GPT-317C64-INTEGER-REVIEW.md).
No new kernel run, simulation, novelty claim or submission.

## Carrying argument read

Read the complete `WBAt`, `wbAt_step1`, `wbAt_step2`, `wbAt_right_wall`,
`box_agree`, `cone_agree_gen` and `wbAt_agree_four` definitions/proofs
(source lines 67–278). The local proofs use the Rule 30 update directly;
the later black-run exclusion theorems use additional imported results and
are outside this carrying verdict. Their source was inspected, but this
review does not adopt their entire dependency chain. White-run families,
residue-class deaths and the full edge-crystal extension remain pending.

Let time start at zero and write the observed row as

`x(m)=0; x(m+1)..x(m+2j)=(01)^j`.

The first two cells to the right of m become 11 after one update. The
remaining alternating pairs persist, including the last black cell:
`f(1,0,1)=0` and `f(0,1,z)=1` for either z. After the second update, the
cell at m+2 becomes 0, because `f(1,1,z)=0`, and the remaining j−1 pairs
still form the same pattern. Neither step needs the cell beyond m+2j.

Induction therefore gives an exact finite bar: cell m+2j is black at
times 0 through 2j−1 and white at time 2j. No claim is made about its
later colour. This induction does not require later values of column m.
For j=0, the assertion is just the original white cell, with an empty
black-time interval.

Now compare two occurrences of this strip with **the same entire future
input at m**. Their rightmost cells agree through time 2j, including the
white endpoint. With equal left inputs and these equal right endpoints,
induction keeps the whole intervening box equal through that time.
Thereafter the ordinary shrinking agreement cone gives equality at m+1
for times `0 <= s < 4j`. The width-2j generic cone alone would give
`0 <= s < 2j`. The external proof earns the additional delay by first
holding the box, then letting its agreement shrink.

**Verdict:** these local self-shielding and conditional agreement proofs
carry. The theorem compares two portions of the kit's single-seed history;
the hand argument itself uses only the local update and the stated inputs.
It asserts agreement, not alternation, and does not assert sharpness of
4j for every driver or pair of histories.

## Why this is our staircase, and what it does not settle

Question: is this protection a new source of indefinite clock support?
Response: it is the same alternating rain patch and black right boundary
as L999/L1000, now used to obtain an explicit comparison horizon. The
white cell at m makes the initial pair at m,m+1 equal to 00: this is the
front that consumes the alternating strip. Its two-step advance removes
one pair at a time, exactly as in the reviewed staircase picture.

Challenge: can identical starting strips alone give the longer comparison?
A cheap hand countercheck says no. Take two finite rows with black cells
respectively `{2}` and `{-1,2}`, and put m=0. Both start with 001 at
positions 0,1,2. At time 1, both have cells 1 and 2 black, but cell 0 is
respectively 0 and 1. Hence cell 1 at time 2 is respectively 1 and 0.
The differing left input enters immediately; the common starting strip
cannot replace the driver's agreement hypothesis. This is the unexpected
check, not a computer experiment.

The source supplies that driver agreement from an assumed periodic centre
when proving its later period exclusions. That is legitimate conditional
reasoning. It cannot be used to *create* a periodic centre from a finite
starting patch. Nor does a 4j agreement window guarantee a 4j clock:
the output word inside the window need not alternate.

Better question: what forces the input histories, or successive replacement
patches, to remain compatible with one finite beginning? Self-shielding
quantifies protection against the right exterior; it leaves that existing
finite-origin question open. Increasing this finite horizon alone would
not answer it, so no larger scan follows from this review.

Record searched: `self.shield|wbAt_agree_four|black_shield` using
record_find.py (5 hits in 3 files), together with L999's staircase review,
L1000's patch rule and their GC1935 scope amendments. This credits the
external comparison argument and avoids presenting the local rain
mechanism as a new discovery of ours.
