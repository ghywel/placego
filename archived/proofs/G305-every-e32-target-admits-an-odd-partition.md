# Every E32 target admits an odd partition

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT305. Every E32 target admits an odd
partition (2026-10-15)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Every eight integer targets totaling1024 and individually at most130 can be filled with the first32
odds. Complementary pairs, parity transfers and one three-swap relay handle all five parity counts.
PROVED after Cloud CL417/CL418; no machine enumeration or novelty claim.

**Why it matters.** This discharges all186 exceptional E32 types analytically. Earlier exceptional
levels remain open, so it does not establish the full eight-path minimum-length threshold.

## The formal statement and proof

**Status: PROVED after Cloud's independent hand carrying read, CL418/e44aaa7b (23:10 BST).**
Where: GPT-MATH-INSTINCT.md MI050, first committed e87f9adb; copied verbatim below, retaining its
historical unreviewed status. G304 supplies the independently verified q=0,8 cases; Cloud read the
new q=2,4,6 allocation and relay in full. No novelty claim, no all-level32 or L8 upper bound.

**PROOF-SKETCH; independent carrying read pending, no novelty claim.** Every eight integer targets
t_i<=130 with sum1024 admit a partition of the first32 positive odds with these sums. The hypotheses
already force t_i>=114, so this is exactly the E32 corner; it is not all of level32 without the earlier
induction levels, and it does not establish L8<=68. No machine experiment or solver was run here.

Write t_i=128+delta_i. Even deviations are at most2, odd deviations at most1, and sum delta_i=0.
Let q be the number of odd deviations; q is0,2,4,6 or8. Write P_x={x,64-x}, x=1,3,...,31, for the
16 complementary pairs. Initially every bin gets two such pairs, hence size4 and sum128. We shall
reserve some pairs first, then fill every bin to two pairs using unreserved pairs. A chosen free token
may be the lower or upper member of its pair; selecting one whole free pair for a bin never assigns
the same pair elsewhere.

**Chain bookkeeping used below.** After the specified parity transfers, let s_i be each bin's change
from128, and e_i=(delta_i-s_i)/2. In every case below e_i are integers, e_i<=1 and sum e_i=0. A bin
with e_i=-k needs to donate k units of2; a bin with e_i=1 needs one such unit. Assign the positive
bins among the negative bins in groups of the required sizes. A donor and its k recipients use a
chain of k+1 consecutive odd tokens v_0>...>v_k. Successive swaps of the donor's current token with
the next recipient's token donate2 to each. Each participating bin uses just one token for this chain.
For any remaining groups, the total number of needed token positions is r+d, at most the number of
remaining active bins, hence at most8. Disjoint consecutive segments of a free token interval suffice.

All pair assignments described below are made BEFORE filler pairs are assigned. Every bin with a
specified parity pair has at most one such pair except the explicitly named constrained bins C, which
already have two pairs. Every other active bin is assigned at most one extra free chain pair. Thus no
bin exceeds its two initial pairs. All leftover pairs can fill the remaining slots, since the total
number of slots is16. Perform the parity transfers after filling; they touch only the specified fixed
lower tokens. Then the selected free chain tokens are still present, while the constrained tokens have
arrived exactly where stated. This order is part of the construction, not a separate compatibility assumption.

**q=0.** MI048's even-target construction applies with n=8. No parity transfer is needed.

**q=2.** Name the two odd bins S,T. Reserve P_1 for S, and later move1 from S to T. Their shifts are
s_S=-1 and s_T=+1; all other shifts are0. Thus e_S<=1, e_T<=0, and each other e_i<=1. Every bin has
at least one free initial pair slot. The lower free tokens3,5,...,31 form a15-token interval. Allocate
all donor chains there: r+d<=8 positions suffice. Reserve their pairs, fill remaining slots, move1,
then run the chains. S ends with size3, T with size5, and the six other bins with size4.

**q=4.** Some odd deviation is at least-1. Otherwise the four odd deviations are at most-3 each, and
the other four at most2 each, contradicting their zero total. Choose such an odd bin C; reserve P_3
and P_5 for it. Choose another odd bin R and reserve P_7 for R. Name the remaining two odd bins S,T
and reserve P_1 for S. The parity moves are C gives3,5 to R in exchange for7, and S gives1 to T.
They give shifts-1 at C,S and+1 at R,T. In particular e_C is0 or1; every negative-e bin has a free
pair slot. The free lower tokens9,11,...,31 form a12-token interval.

If e_C=0, allocate every chain in that free interval. If e_C=1, choose any donor of magnitude k>=1
and assign C as its last recipient. After the parity move C holds7. The tokens

    7+2k, 7+2(k-1), ..., 9, 7

give that chain, with C at its last position. Its other k positions use the first k free pairs.
The remaining free interval has12-k tokens; the other active bins number at most8-(k+1)=7-k, so
their chains fit. Here k<=7 and all selected lower tokens are at most21. Fill, transfer, and swap
as prescribed. No chain pair is assigned to C, which already has its two fixed pairs.

**q=6.** At least four odd deviations are at least-1: if three were at most-3, the other three odd
deviations and the two even ones would total at most3+4, leaving total at most-2. Choose two such
bins C_A,C_B. Reserve P_3,P_11 for C_A and P_7,P_9 for C_B. Choose two other odd bins R_A,R_B;
reserve P_13 for R_A and P_15 for R_B. Name the last two odd bins S,T, and reserve P_1 for S.
Parity moves: C_A gives3,11 for R_A's13; C_B gives7,9 for R_B's15; S gives1 to T. Each C and S
has shift-1, each R and T has shift+1. Thus e_(C_A),e_(C_B) are0 or1, while e_(R_A),e_(R_B),e_T<=0.
All negative bins and all positive bins other than the C bins have a free pair slot. After parity moves,

    C_A holds {13,61,53}; C_B holds {15,57,55}.

The nine free pairs are P_5 and P_17,P_19,...,P_31. The latter give eight consecutive lower tokens.
There are at most five positive-e bins because R_A,R_B,T cannot be positive. We may interchange the
labels C_A,C_B when only one is positive; both were chosen with odd deviations at least-1.

- Neither C positive: allocate all chains in17,19,...,31. At most six active bins need tokens.
- Exactly one C positive: label it C_B. For any donor-k, put C_B last in a chain ending15, with k
  free positions17,...,15+2k preceding it. Here k<=5, so these are available. The remaining8-k free
  positions suffice for all other chains, which use at most7-k active bins.
- Both C positive, some donor has k>=2: assign both to that donor, with C_B then C_A as its last
  two recipients. Use the chain ending ...,17,15,13, starting13+2k. It consumes k-1 free pairs from
  the interval17..31; k<=5. Its remaining9-k free positions suffice for the other chains, which
  use at most7-k active bins.
- Both C positive, every donor has k=1: choose two distinct donors N_1,N_2. Assign free pair P_5 to
  N_1 and P_17 to N_2. After parity moves, perform these three swaps:

      N_1's59 with C_B's57;
      N_2's17 with C_B's15;
      C_B's55 with C_A's53.

  Each N loses2. C_B gains2+2-2=2, and C_A gains2. All six swapped tokens are distinct, and both
  donors have exactly the token claimed from their free pairs. If r is the original positive count,
  the donor count is also r; hence2r<=8. After this relay, at most2r-4<=4 active bins remain. Their
  chains fit in the seven untouched free lower tokens19,21,...,31. No relay token or pair is reused.

This exhausts q=6, including the split-donor case that prevented a direct concatenation of chains.

**q=8.** MI048 supplies the construction: at least four deviations equal1. Choose their bins as the
four raising bins; use the four disjoint triples(3,11,13),(5,17,21),(7,19,25),(9,15,23) for parity
exchanges. Raising bins finish at129. Lowering bins start127 and retain anchor tokens61,59,57,55;
their even residual e_i<=1 sum0. Relabel those four bins in chain order, using at most four anchor
positions. The unused complement pairs fill only the raising bins. This is the same already-written
allocation, not an assumption that arbitrary parity repairs compose.

**Adversarial hand checks / niggle sweep.** All five parity counts exhausted; q=4/q=6 good-bin
existence uses the zero total, not an assumption about signs. Chain cardinalities include roots.
Fixed pairs in q=6 are exactly P_1,P_3,P_7,P_9,P_11,P_13,P_15, leaving precisely the nine pairs
listed; P_5 and P_17 used by the relay are disjoint from the remaining interval. A token's complement
is never selected as a second chain slot. Every constrained bin gets its later token through an
explicit parity exchange, with no extra initial pair. Filling precedes transfers, so no token is
assumed created or duplicated. Swaps preserve coverage; parity moves preserve total and coverage,
with explicit3/5 versus4 cardinalities. No measurement, combined certificate tally, source priority,
runtime or earlier-level conclusion is inferred.


**Independent carrying read (Cloud, CL418).** Verified all new cases by hand: the single reserved
P_1 transfer with fifteen free chain positions; selection of the q=4 constrained bin and its final
7 token; selection of the q=6 constrained bins, every free-slot bound, the two-anchor chain, and the
six distinct relay tokens in their named bins. The relay leaves at most four active bins in seven
untouched free positions. Together with CL417/G304 this verifies all five parity counts and all186
E32 target types. Full review in CHAT-LEDGER.md CL418, commit e44aaa7b.
