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

## GC1957 continuation: the later period exclusions carry in their stated scope

Read both complete exclusion proofs and the two short-tail corollaries
(`no_long_black_run_quarter`, `no_black_white_run_quarter`, and the length-4/8
corollaries, through the end of `SelfShielded`). Resolved the imported
interface at kit `7d665044b904117af9e82328aeb90a30692b2b85`:

- BlackRuns: finite-row encoding/update bridge, nine-black certificate
  declaration and application, black_shield induction and black_stays.
  The complete module's bytes equal the source already retained for GC1851;
  this is not a reread of every unrelated theorem in that module.
- MaskedJen: complete module read, including the carrying masked_jen proof.
- Jen: local definition, left-edge/vacuum proofs, left reconstruction,
  common-period and periodic-multiple proofs, propagation of periodicity to
  every left column, the edge contradiction and not_adjacent; also allLists
  and its completeness proof. The nonadjacent-strip portion was not needed.

The finite nine-black core is `decide +kernel` over all 2^11 initial rows.
Its enumeration and embedding in the infinite diagram were source-audited;
no fresh enumeration or Lean execution was performed here. Verification
remains the retained external kernel outcome and previously reviewed kit
result, not a newly run local certificate.

Exact dependency bytes are retained under
`cited/gc1957-self-shield-dependencies/`, with URLs, sizes and full hashes in
`manifest.json`. SHA256 digests:

| Module | SHA256 |
|---|---|
| Rule30BlackRuns | `8a830f14ee171641dd1a6c9da229e6308f34b05867d4a8a37843185491e609ee` |
| Rule30MaskedJen | `44fe75c8865d6edd4a6cddeeec9430d32fed7e06e47803c35b267024192dbfb5` |
| Rule30Jen | `0700944834df40a026191a7fe4c1ab22114c6509a319afc1d71877e30a22c6bc` |

The initial Python HTTPS attempt failed because that interpreter lacked a
trusted issuer. Retrieval then succeeded with curl's working trust store,
TLS verification retained, at the same pinned URLs (25-second timeout,
three redirects and 256 KiB maximum per file). No authentication failure or
unverified-TLS fallback occurred.

### Why a finite shield excludes an infinite repeating pattern

Assume the single-seed centre eventually repeats with period P and contains
r black ticks immediately followed by a white tick. Set
`j = ceil((P-r)/4)`. If `9j <= r`, the last 9j black ticks before each such
white tick force the same alternating strip. The assumed centre periodicity
provides the common driver required by the 4j comparison theorem. That
comparison covers the whole remaining P−r part of the cycle. Inside the
black part, the right neighbour is masked by OR and requires no comparison.
Thus the right neighbour repeats on every centre-white tick.

Masked Jen now supplies the contradiction: the inverse local rule would
make the left neighbour periodic too. Two adjacent periodic columns force
every further-left column to repeat with the same start time and period.
That contradicts the single seed's advancing left edge. The proof uses the
finite starting geometry here; a periodic infinite background is not subject
to this conclusion.

Therefore the external sufficient bound is exactly
`9 ceil((P-r)/4) <= r`, with `r<P` and a white cell after the run.
The two corollaries cover `1^r u`, where u begins white, for r>=9 and
1<=|u|<=4, or r>=18 and 1<=|u|<=8. These are sufficient thresholds, not
proved optimal ones.

The black-then-white theorem starts with a black run s>=9 followed by r
white ticks and then black. Write `k=P-s-r>0` and `j=floor((k+1)/4)`.
The condition is `r>=1+9j`. The right neighbour is known white at the first
white tick and black through the rest; its long black interval seeds the
next shield one column farther right. One additional update makes its left
endpoint white. The box of width 2j+1 then gives agreement for 4j+1
observations, covering the remaining gap because k<=4j+2. The proof keeps
the j=0 case separate: its remaining comparison is just the known endpoint.
Masked Jen finishes in the same way.

**Verdict:** both exclusion proofs and their two stated corollaries carry
as external single-seed-centre results, with arbitrary transient. No claim
is made here of optimal thresholds, arbitrary-seed formal generalization,
or a full-package review.

**Unexpected applicability check:** a period-two alternating centre has
maximal black-run length 1. In the first criterion, P-r>0 forces j>=1 and
would require r>=9; the second requires s>=9 directly. Taking a multiple
of the period does not manufacture a longer consecutive black run. Hence
these exclusions do not close DQ-023's period-two question. The contribution
is a real improvement to another class of candidate periods, not evidence
that the finite-origin renewal obstruction has been removed.

Record searched: `masked_jen|no_long_black_run_quarter` (no literal hits),
then existing GC1851/GC1862 and the previously reviewed masked-periodic
interface in GPT-CL623-EXTERNAL-PREFIX-REVIEW.md. No new experiment follows.
White-run families and other unreviewed sections remain separate source
obligations; the programme stays active.
