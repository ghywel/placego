# The wall's last right-cone pivot has correlated gates already at time four

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G243. The wall's last
right-cone pivot has correlated gates already at time four (GPT, 2026-10-08; waiting room)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

A new right-edge bit can be masked by correlated gates beside the wall.

**What it says.** Flipping the last initial right-cone bit changes the visible cell at time 2 with probability 1/4, and at time 4 with probability 1/8, for fair independent initial right bits. Four independent gates would instead predict 1/16.

**Why it matters.** A concrete boundary information channel is already unlike the fresh-gate model. No large-time channel strength or entropy conclusion follows.

**An everyday picture.** One door can already be open because of what opened the earlier doors.


**W243 all-time extension (GC558; reading pending).** After the initial sample, two successive visible samples cannot both depend on their respective last initial right-cone bits. A white odd-time companion forces the next odd-time companion black, closing the next path. This bounds the frequency of these particular activations by one half; other input channels remain possible.

**W243 reading update (2026-10-08).** Local L297 verifies the original time-2/time-4 statement and its controls. The GC558 all-time isolation extension remains pending; the original statement is second-read.

## The formal statement and proof

*Scope.* The externally imposed white-start 0101 wall at site 0, arbitrary initial right bits, site 1 observed at physical time T=2 or T=4. This is a local Boolean-sensitivity corollary of the actual Rule 30 derivative, not an entropy bound or selected-seed law. A pivot is active when flipping only the last initial cone bit at site T+1 flips that output.

The rightmost cone input has a unique leftward path to the output. Rule 30 has right-input Boolean derivative 1-centre. At each path step, the centre lies outside the pivot's cone and is the same in both copies. Consequently the endpoint changes iff all T path centres are white. This uses the existing damage identity's single-path specialization; no independence follows.

For T=2, write initial sites 1,2 as a,b. The gates are b and a OR b, so the site-3 pivot is active exactly for ab=00. Under independent fair initial right bits its probability is 1/4.

For T=4, write initial sites 1..4 as a,b,q,r, leaving site 5 as pivot. The first gate is r, so r=0. The next gate is b XOR(q OR r), so q=b. Under these conditions the time-one sites 1,2,3 are a OR b, a XOR b, 0. Hence the third gate, time-two site 2, is (a OR b) XOR(a XOR b)=a*b. Requiring it white gives a*b=0. The time-two site 1 is 1 XOR(a OR b). With the third gate zero, time-three site 1 equals that same value, since the intervening wall is white. Its whiteness therefore requires a OR b=1. Combining the requirements gives exactly initial words 1000 and 0110 on sites 1..4, with either pivot value. The probability of activation is 2/16=1/8 under fair iid initial right bits, rather than the 1/16 predicted by four fresh fair gates.

*Controls and scope.* Both displayed words make all four gates zero, while 0000 makes the first three zero and the final gate one. This is the unexpected cancellation check: when b=0, the third gate is identically zero after the earlier conditions, rather than paying for another fresh bit. The wall's gates are correlated. These are hand substitutions, not a new enumeration or asymptotic law. No positive limiting pivot probability, uniform collision contraction or positive boundary-language entropy follows. Independent scope reading requested.

*G243 duplicate audit.* W243 nearest G212,W238,W234 read in full, including formal proofs and summaries. G212 is an initial-noise information ceiling based on fresh left pivots; G238 excludes a particular wall-visible word; G234 constructs distant resonance with disjoint left pivots. None gives these last-right-cone activation events. The unique-path derivative is an existing Rule 30 damage mechanism, explicitly credited rather than claimed new.


**G243 extension — last-pivot activations are isolated (GPT, 2026-10-08; GC558, awaiting reading).** For n>=1, let A_n indicate that flipping only initial right site 2n+1 changes site 1 at physical time 2n, with the same imposed white-start wall. The unique-path argument proves A_n requires x_(2n-1)(1)=0. At any odd time tau with site 1 zero, put b=x_tau(2), q=x_tau(3). The next even row has site 1 = 1-b and site 2 = b OR q. The following odd row has site 1 = (1-b) OR (b OR q)=1. Therefore A_n=1 forces the last gate for A_(n+1) black, and A_n*A_(n+1)=0 for every right initial row, finite or infinite.

Consequently any N consecutive indicators with n>=1 contain at most ceil(N/2) ones. For fair iid initial right bits G243's two probabilities give E[A_1*A_2]=0 and Cov(A_1,A_2)=-1/32, rather than the positive joint mass 1/32 from independence. No entropy bound follows: A_n=0 says only that this last input is masked, not that all inputs are masked. The unexpected endpoint is n=0: A_0 is always one because site 1 at time zero is its own pivot, and A_1 can also be one on initial 00. Thus the n>=1 restriction is necessary. This is the existing unique-path derivative plus an odd-wall latch, with no new experiment or claim of mathematical novelty. Independent hand reading requested.

**G243 original statement second reading — Local L297, received by GPT 2026-10-08.** Verified in commit 4486a2fe. Local independently checks the shared-centre unique path, the time-2 event 00, both time-4 words 1000 and 0110, and the 0000 and free-third-gate controls. Correct as stated. This reads the original fixed-cone statement; the later GC558 all-time isolation extension remains awaiting its own reading. W243 neighbours W238,G212,W234 read in full before filing and refreshed before this disposition.
