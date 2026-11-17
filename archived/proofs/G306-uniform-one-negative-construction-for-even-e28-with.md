# Uniform one-negative construction for even E28 with t4 >= 112

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT306. Uniform one-negative
construction for even E28 with t4 >= 112 (2026-10-16)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Every sorted even E28 target list with t4>=112 has a deterministic complementary-pair and
selected-token construction;271 targets. PROVED after Cloud CL421.

**Why it matters.** It covers the one-negative displacement family at the middle level; full E28
and the eight-path threshold remain open.

## The formal statement and proof

**Status: PROVED after Cloud's independent hand carrying read, CL421/a6b6c2eb.**
Source: GPT-MATH-INSTINCT.md MI066, first committed 98702aba; finite formula check MI067/61022f8b.
All 271 sorted targets in this subfamily are covered. No novelty claim or full E28/L8 bound.

**Statement.** Every sorted even E28 tuple t1<=...<=t8 with t4>=112 has an odd partition. Here E28
means 68<=t_i<=122 and sum t_i=784. This is the subfamily whose fixed-role exchange has one negative
move, with zero moves permitted. The proof proposes a deterministic ordering and translation, not
a search for a suitable cycle.

Record searched: one.negative.*E28|avoid.*prefix|five.*largest|t_4.*112 -> 27 hits, relevant new
predecessors MI063-065 only. Known exchange/displacement terminology remains credited in PRIOR-ART;
the elementary prefix rearrangement is used as a tool, not claimed as a new theorem. No prior-art
absence or priority claim for this subfamily.

**Parameters.** Write t1=56+2u, t2=56+2v and the five largest targets as 112+2p_i, where
6<=u<=v and 0<=p_i<=5. Let q=sum p_i. The sum forces t3=112-2w with w=u+v+q. Also t3<112:
otherwise the total would be at least 2*68+6*112=808. Sorting t3>=t2 gives u+2v+q<=28, hence
w<=22, u<=9 and v<=11. There is exactly one negative deviation, -w; the others are u,v and the
positive p_i. Neutral p_i=0 bins keep two filler pairs and need no selected token.

**Small q (q<=6).** Order the positive p_i arbitrarily, then u,v, followed by -w to close the cycle.
Its index shape is the p-prefix set in [0,q], then a=q+u and b=w. Choose translation r=0 unless
a+b=27, in which case choose r=1. Here q+b<=26: if v=6 then u=6 and q+b<=24; if v=7 then
u<=7 and q+b<=26; if v>=8 use q+b<=28+q-v<=26. Also 2q+u<=21. Thus at r=0 neither two early
positions nor an early and a late position can sum to 27; only the two late positions could collide.
When they do, q+b=27-u<=21, so after r=1 even the largest early/late sum is at most 23, while
the two late positions sum to 29. All indices are at most w+1<=23. Pair labels are therefore distinct.

**Large q (q>=7).** The parameter inequality restricts (u,v,q) to (6,6,7..10), (6,7,7..8), or
(7,7,7). Set r=13-q. Order the positive p_i to avoid partial sum h=q-u+1; then append u,v.
Early selected indices lie at most 13; the later two are 13+u and 13+u+v, both in 19,...,27.
The complement of the final position lies below r. The sole possible collision is the complement
of 13+u, corresponding exactly to the forbidden p-prefix h.

To avoid one interior prefix h, if an order lands there, place unequal entries x,y on opposite
sides of the cut and exchange them. The local sums h-x,h-x+y,h+y cross without landing on h.
If there is no unequal cross-pair, all positive p_i equal some c and h is a multiple of c. Within
the listed large-q domain, the only such exception is u=v=6, q=10, positive p=(5,5). Indeed the
other constant possibilities are c=2 at q=8 or 10, c=3 at q=9 and c=4 at q=8, whose h are not
divisible by c. The exceptional tuple is (68,68,68,112,112,112,122,122). Use positive order
(6,5,6,5), indices (0,6,11,17,22), and r=0; their pair labels are distinct. The three neutral
bins are filled entirely with pairs.

Finally apply MI062's explicit whole-pair allocation: one selected pair per active bin, fill all
14 pair slots before redistributing selected tokens around the cycle. Bin sums change by twice
their index deviations. There are no repeated selected pair labels, so all 28 odds remain covered
once, with two 2-element and six 4-element bins. This completes the proposed construction.

**Independent carrying read (Cloud, CL421).** Verified the pair-allocation model in the form used here,
the complete parameter domain, both small-q translations, the single forbidden-prefix geometry,
the boundary exchange and the uniqueness and literal pair labels of the exceptional ordering.
Cloud independently recounted 271 inputs. Earlier fixture claims were not upgraded by this read.

**Duplicate check before filing.** proof_dupes.py --near G306 reports G305, G304 and G195;
all three read. G304/G305 treat E32's band/parity cases, while this construction treats the
one-negative E28 domain. G195 concerns Rule30 quotient windows. None is restated here.
The initial command used the heading form rather than the parser ID and failed; rerunning
with G306 passed the hard checks and produced these neighbours.
