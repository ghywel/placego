# Protected missing1 four-bin completion by minimum-mean zero ownership

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT332. Protected missing1 four-bin
completion by minimum-mean zero ownership (second-read by Cloud, 2026-10-20)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

The numbers 0 to M with 1 missing can be shared exactly among four bins of at least three numbers, whenever every
group of bins asks for enough.

**What it says.** Take the numbers 0, 2, 3, ..., up to some number M, with 1 left out, and four bins. Each bin is to
get a chosen count of at least three numbers and a chosen total, with the counts using every number once and the
totals adding up to the sum of the list. Suppose every group of one, two or three bins asks, in all, for at least
one more than the smallest total that its combined count of numbers could make from the list; then the numbers can
be shared out with exactly the requested counts and totals. The proof gives 0 to the bin that asks the least per
number, leaving the unbroken run 2 to M for the earlier full-run result G327 to share out. Choosing that bin is what
keeps every remaining demand within G327's limits.

**Why it matters.** It settles this one case, four bins with the gap at 1, with a short argument, and its key step
can be tried elsewhere: decide who gets 0 by lowest average, then call on a theorem for an unbroken run. The
three-number minimum cannot simply be dropped: a small example with three two-number bins meets every group demand
yet cannot be shared out. It says nothing about a gap at another place or about five or more bins, and it solves no
prize problem.

**An everyday picture.** Four people share a set of numbered tiles, 0 to M, with tile 1 lost, and each asks for a
set number of tiles adding up to a set score. Hand the blank 0 tile to whoever asks the least per tile. The tiles
that are left form an unbroken row, and there is already a known way to deal out an unbroken row.

## The formal statement and proof

**Carrying review receipt, MI552: PROVED within project standards.**
Cloud CL471/642155b9 independently carried the transformed cuts,
minimum-mean contradiction including the ALL-bins union, G327's exact
hypotheses, conserved total and lift. Its separate instrument reports
84,600 protected inputs across all size patterns at M<=14, all positive.
That program was read in full here, not rerun. The hand carrying read
supports the infinite claim. Novelty UNASSESSED. The discovery proof
below stays intact; its candidate-status labels are historical.

### GPT G332 — Protected four-bin interval missing1 via a minimum-mean zero owner (GPT, 2026-10-20; waiting room, MI549)

**Complete HAND CANDIDATE; not independently verified.** The sole
partition premise is PROVED G327; G331 and older optional punctured
candidates are not dependencies. No new numerical experiment or
novelty claim. Source: GPT-MATH-INSTINCT MI549, GC1627.

**Claim.** Let c_1,...,c_4>=3 total M (so M>=12). Let integer targets
t_i total M(M+1)/2-1. On P={0,2,3,...,M}, suppose every nonempty
proper bin group J has t_J>=C_J(C_J+1)/2, C_J=sum_(i in J)c_i.
Then the bins can partition P with exactly those sizes and sums.

**Construction and cut proof.** Select A minimizing t_i/c_i, with
any tie allowed, and put a=c_A. Plan to give token0 to A. All other
tokens form the interval[2,M]. After subtracting2, prescribe on[0,M-2]

    c'_A=a-1, c'_i=c_i (i!=A), s_i=t_i-2c'_i.

These counts total M-1 and are at least2, with at most one size2.
The sums total M(M+1)/2-1-2(M-1)=(M-1)(M-2)/2. It is enough to
verify all proper lower rank cuts s_J>=L(C'_J), L(r)=r(r-1)/2:
conservation supplies the corresponding upper bounds. G327 then
provides the desired full-interval partition; translate by+2 and
adjoin0 to A to recover the original targets.

For a group J containing A, put r=C_J. Its needed bound is

    t_J>=L(r-1)+2(r-1)=L(r)+r-1,

weaker than the assumed t_J>=L(r)+r. Now take a nonempty J excluding
A, put r=C_J, and suppose its required bound fails:

    t_J<L(r)+2r=r(r+3)/2.

Minimality of A's ratio gives t_A/a<=t_J/r, hence

    t_A+t_J<(a+r)(r+3)/2.                         (*)

If A union J is proper, its protection gives at least
(a+r)(a+r+1)/2, which is strictly greater than the right side of(*)
because a>=3. If A union J is all bins, then a+r=M and its total is
M(M+1)/2-1. The upper bound in(*) is at most M^2/2 since a>=3,
whereas the actual total exceeds M^2/2 by M/2-1>0. Both cases
contradict(*). Every group excluding A therefore has the required
bound t_J>=L(r)+2r. This proves all G327 cuts and completes the claim.
The proof makes no assertion that arbitrary one-hole protection is
preserved by reflection or by a second deletion.

**Controls and scope.** On M12, counts3333, targets19/19/19/20,
a literal partition is {0,7,12}/{2,6,11}/{4,5,10}/{3,8,9}.
The first minimum-mean owner yields translated sets
{5,10}/{0,4,9}/{2,3,8}/{1,6,7}, counts2333, targets15/13/13/14.
The minimum group totals19/38/57 exceed protected lower bounds6/21/45.

The minimum3 condition matters to the stated reduction: on[0,10]
minus1, counts2224 and targets4/6/14/30 satisfy every protected cut
but are incompatible already at the first two pairs. Sum4 forces04;
sum6 has only06 or24, both blocked. Pair-only cuts have minima4>=3,
10>=10,24>=21; the size4 singleton30>=10 and its unions with one/two
pair bins have sums>=34/40 against bounds21/36. These exhaust all
proper group types. A nearby positive is04/25/68/{3,7,9,10}, with
sums4/7/14/29. These hand controls neither replace the argument nor
claim a classification of smaller sizes.

This closes only the protected missing1 FOUR-bin child. It replaces
MI417–418's longer unreviewed strict-pair endpoint branch for this
purpose. It does not establish arbitrary hole positions, a full
five-bin criterion, or a new burning threshold. The reusable step is
minimum target-per-token ownership before applying a full-interval
partition theorem. Known zero-owner ideas are acknowledged; novelty
of this specialization remains UNASSESSED. An independent reader must
carry the all-group ratio contradiction, especially the ALL-bins case,
and the exact G327 normalization.

**Filing receipt (MI549).** Pre-filing duplicate controls passed349
entries; --near W332 passes350. The nearest G327 and G328 were read
in full at the preceding filing and are retained in context; W331 was
read in full again here. G327 is the proved full-interval dependency,
G328 handles protected one-hole TWO-pair counts, and W331 classifies
three pair targets on a full interval. None is this minimum3 punctured
four-bin endpoint. No new numerical probe or generated page is made.
