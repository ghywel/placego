# Complementary-pair exchange band and all-odd E32

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT304. Complementary-pair exchange
band and all-odd E32 (2026-10-15)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this
summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Complementary pairs and chains of swaps partition the first4n odds into four-element bins for every
even target list of total16n² with each target at most16n+2. Four explicit parity exchanges also cover
the five all-odd E32 types. PROVED after Cloud's hand carrying read CL417; no novelty claim.

**Why it matters.** This analytically covers27 of the186 target types in the top exceptional eight-path
corner. The mixed-parity extension and the full eight-path threshold are separate claims.

## The formal statement and proof

**Status: PROVED after Cloud's independent hand carrying read, CL417/b08ad55a (22:53 BST).**
Where: GPT-MATH-INSTINCT.md MI048, first committed0c6b9b9e; copied verbatim below, including its
historical unreviewed status. Cloud explicitly requested this filing. No priority claim; the bounded
search did not identify the precise lemma, which may be folklore. This serves the graph-burning odd
partition question; it does not solve the full eight-path threshold or any held prize problem.

**PROOF-SKETCH, awaiting an independent carrying read; no novelty claim.** For every n>=1 and even
integer targets t_1,...,t_n satisfying sum t_i=16n^2 and t_i<=16n+2, the first4n positive odd integers
can be partitioned into n bins of exactly four elements, with these target sums.

**Construction.** Write t_i=16n+2e_i. Then e_i are integers, e_i<=1 and sum e_i=0. Let R be the
recipients with e_i=1, r=|R|, and D the donors with e_i=-k_i<0. Thus sum over D of k_i equals r.
Partition R into groups of k_i recipients, one group for each donor. If r=0, every e_i=0 and the
balanced construction below already suffices.

Pair the first4n odds by complementation to8n: each pair is {x,8n-x}, with one lower-half odd and
one upper-half odd. There are2n pairs. Two pairs make a four-element bin of sum16n. For donor i,
reserve a segment v_0>v_1>...>v_(k_i) of consecutive upper-half odds, so v_(j-1)-v_j=2. Choose the
segments disjoint. This is possible because their total length is

    sum over D of (k_i+1) = r+|D| <= n <= 2n,

and the upper half contains2n consecutive odds. Give the whole complement pair of v_0 to the donor,
and the whole pair of v_j to its j-th recipient. Every involved bin has received exactly one pair;
every other bin has received none. Distribute the remaining complement pairs arbitrarily to bring
each bin to exactly two pairs. The number required is exactly the number remaining, so this step
imposes no additional matching condition. Every bin now has four elements and sum16n.

For j=1,...,k_i, swap the donor's current token v_(j-1) with its j-th recipient's v_j. Each swap
reduces the donor by2 and raises that recipient by2. After k_i swaps the donor has lost2k_i;
each recipient has gained2. Different donor groups use disjoint bins and reserved tokens. All
operations are swaps, preserving bin sizes, disjointness and complete coverage of the odds. Hence
the final sums are precisely the t_i. This completes the hand construction.

**Hand checks.** The balanced case r=0 uses only the initial complementary pairs. The extremal
single donor k=n-1 uses n reserved tokens, within the2n available. At n=1 the sole target is16.
There is no hidden negative-target case: the hypotheses force t_i>=16n^2-(n-1)(16n+2)=14n+2.
The carrying allocation issue is explicit: each involved bin receives only one reserved pair, and
the filler pairs are wholly unreserved; later swaps never require a token from the filler pool.
No machine run or census was performed in this block.

**Application.** At n=8, this covers every all-even tuple of E32, since its total is1024
and its cap130. In deficits d_i=130-t_i, these have d_i=2a_i and sum a_i=8. Their count is the known
partition number p(8)=22 (NIST DLMF26.9), not a fresh census. Some overlap B18's certificates; I have
not computed a combined tally. This is neither all of E32 nor an L8 upper bound.

**Unexpected check: composition needs a joint allocation.** A2-for1 exchange using odd
a,b,c with a+b-c=1 lowers one bin by1 and raises another by1, changing their sizes from4/4 to3/5.
Disjoint triples (3,11,13), (5,17,21), (7,19,25), (9,15,23) give four such repairs in the n=8 pool:
put the full pairs of a,b in the lowering bin and the full pair of c in the raising bin, then fill
the latter with an unused pair. All12 reserved pairs are distinct; the four leftover pairs have lower
members1,27,29,31, so they fill the four raising bins. This alone realizes four targets127 and four
targets129. For general mixed-parity targets, those
reservations constrain which upper tokens each bin can hold. The even proof above depended on freely
allocating its chain pairs. Proving the two constructions separately does not supply that joint
allocation. I therefore do not claim a mixed-parity band lemma.

**A pleasant surprise: all eight targets odd do admit the joint allocation.** This further construction
is also a PROOF-SKETCH awaiting an independent read. Write t_i=128+delta_i, with odd delta_i<=1 and
sum delta_i=0. At least four delta_i equal1: otherwise the remaining negative odd deviations have
total magnitude larger than the positive ones. Choose four such bins as the raising bins; each has
desired target129. The remaining four bins are the lowering bins. Perform the four triple exchanges
just described. All raising bins have sum129 and size5, and all lowering bins have sum127 and size3.

The lowering bins retain, respectively, the upper tokens61,59,57,55, the complements of3,5,7,9.
We may assign any lowering-bin label to any triple row before starting. For a lowering bin its remaining
required change is delta_i+1=2e_i. These four integers e_i are at most1 and sum0, because the four
chosen raising deviations sum4 and the lowering deviations sum-4. Apply the same donor-chain argument
to these four bins, reserving only the consecutive tokens61,59,57,55. The sum of the required chain
lengths is at most4. Place disjoint chains in that four-token list, and assign the corresponding bin
labels to the triple rows holding their tokens; neutral bins occupy the unused rows. After the parity
exchanges these tokens remain in those bins, so the swaps are available exactly as prescribed. No filler
pair is needed by a lowering bin, and no raising bin is touched again. This supplies the formerly
missing compatibility for this parity pattern. All odds remain covered exactly once, with sizes3/5.

For the proposed hard hand check(-7,+1,+1,+1,+1,+1,+1,+1), assign the-7 bin to the first triple row.
After its parity exchange, pass61 against59, then59 against57, then57 against55 through the other
three lowering bins. Its sum falls127 to121; their sums rise127 to129. The four raising bins already
have129. The balanced parity case(-1,-1,-1,-1,+1,+1,+1,+1) needs no chains. These are checks of the
construction, not new machine experiments. The five all-odd target types correspond to the five
partitions of4, since writing delta_i=1-2a_i gives nonnegative a_i summing4.


**Independent carrying read (Cloud, CL417).** The reviewed steps are disjoint segment packing
r+|D|<=n<=2n, one reserved pair per involved bin and the exact filler count, followed by the swap
bookkeeping. For the all-odd case Cloud checked existence of four+1 targets, all twelve distinct
reserved pairs and four filler pairs, the four-token lowering residuals, and each of the five target
types by hand. Both constructions were verified; the mixed-parity extension was not part of that read.
Full read: CHAT-LEDGER.md CL417, committed b08ad55a.
