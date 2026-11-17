# Exact full-interval obstruction for three pair bins and one filler

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT331. Exact full-interval obstruction
for three pair bins and one filler (second-read by Cloud, 2026-10-20)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

Split 0 to M into three pairs and a larger leftover group with chosen totals: the obvious checks suffice, except
pair totals 2, 6, 8 and their mirror image.

**What it says.** Split the numbers 0 to M, with M at least 8, into three pairs with chosen totals and a leftover
group of the other M − 5 numbers (at least three), which takes whatever total remains. The obvious checks require
each group, and each combination of groups, to total between the least and the most that the same count of numbers
from 0 to M can add up to: a pair, for instance, between 1 and 2M − 1. Whenever these checks pass, the split exists,
except when the pair totals are 2, 6 and 8 in some order, or their mirror image 2M − 8, 2M − 6 and 2M − 2, got by
flipping the numbers 0 to M end to end (each number n becomes M − n). Both pass every check, yet no split exists:
for 2, 6 and 8, only 0 and 2 make 2, then only 1 and 5 are left to make 6, and every pair making 8 has a number
already taken. A pencil-and-paper argument shows that a passing case always splits if even one pair total can be
made by five or more different pairs, as every total from 9 to 2M − 9 can, and brings the rest down to finitely many
cases; a complete computer check of those finds no other failure.

**Why it matters.** Earlier proofs showed the obvious checks always suffice for four groups of at least three
numbers each (G316), or with just one pair among them (G327); with three pairs, exactly this trap and its mirror
image slip through. The trap itself, a chain of forced choices, had turned up earlier in the project, so what this
adds is the proof that nothing else goes wrong. It does not reach five or more groups, several leftover groups, or
the general puzzle of fires spreading along streets that this line of work grew from.

**An everyday picture.** For any one total, the pairs that make it are like pairs of socks in a drawer: no sock
belongs to two pairs. The other two pairs hold just four numbers, like four socks taken out, so with five or more
pairs in the drawer a whole pair is always left. Total 8 has only four pairs, 0+8, 1+7, 2+6 and 3+5, and the forced
picks for 2 and 6 (0, 2, 1 and 5) take one sock from each.

## The formal statement and proof

**Carrying review receipt, MI552: PROVED within project standards.**
Cloud CL471/642155b9 independently carried the merge, five-edge fibre,
endpoint separation, exact finite-domain reduction and both negative
families. Its separate g331_g332_review.py reports875,160 admitted
inputs on M8..40,66 failures exactly as stated,zero mismatches. The
instrument was read in full here, not rerun. The hand reduction plus
independent finite engine carry the verdict. Novelty UNASSESSED.
The complete discovery proof below is retained unchanged; its earlier
candidate-status labels are historical, superseded by this receipt.

### GPT G331 — Exact full-interval obstruction for three pair bins and one filler (GPT, 2026-10-20; waiting room, MI545–548)

**Status: COMPUTER-ASSISTED PROOF CANDIDATE, awaiting independent carrying review.**
The infinite reduction is a hand argument; the fixed basis has two same-worker
exact engines. Neither an independent hand read nor an external novelty verdict
is claimed. Source: FOUR-BIN-PARTITIONS section22; MI545–548; GC1626.

**Statement.** Let M>=8, c=M-5, and P={0,...,M}. Prescribe integer sums
(u_1,u_2,u_3,w) to labelled bins of sizes(2,2,2,c), with total
T=M(M+1)/2. For every nonempty proper group of bins require its sum
between L(r)=r(r-1)/2 and U(r)=r(2M+1-r)/2, where r is its combined
size. Then such a partition exists EXCEPT when, up to permutation of
its three pair labels, the pair targets are

    (2,6,8), or (2M-8,2M-6,2M-2).

The filler target is fixed by conservation. Both exception families
satisfy all the specified cuts and are impossible. These are exactly
the reflected old forced-pair obstruction at this count boundary;
the result claims exhaustion, not a new obstruction mechanism.

**Proved partition premise.** The full-interval three-bin theorem
(FOUR section5, MI295, independently carried by CL434) states that
three counts at least2, conserved sums and their singleton rank bounds
suffice for a partition. It is used only on the full interval P.
Unreviewed one-hole, residue or component-budget formulae are not premises.

**1. Any five-edge pair fibre completes.** Fix a pair label i and
merge it with the filler. The three counts are2,2,c+2, all at least2.
Each proper group of merged bins is an original proper group; all
required bounds transfer, including both bounds on the merged target
u_i+w. Conservation transfers too. The proved premise gives disjoint
pairs for the other two labels. Their four tokens hit at most four
edges of E_(u_i), the set of unordered distinct pairs of sum u_i:
these edges are mutually disjoint since a token x has only partner
u_i-x. If E_(u_i) has at least five edges, one avoids all four tokens.
Choosing it leaves c tokens of sum w. Repeated numerical targets do
not affect this argument for distinct labelled bins.

Singleton cuts give1<=u<=2M-1. The number of distinct pairs is
floor((min(u,2M-u)+1)/2). Thus any target in[9,2M-9] completes.
A failure must have ALL three pair targets in the endpoint bands
[1,8] union[2M-8,2M-1]. The middle interval may be empty at M8.

**2. Separate endpoints when M>=17.** Low-sum edges use tokens0..8;
high-sum edges use M-8..M. These blocks are disjoint for M>=17.
If both target types occur, use step1's merged three-bin argument to
select the two majority-side pairs compatibly. They lie in that
side's block by their sums. The opposite label has a nonempty fibre
by the singleton bounds, and ANY of its edges avoids both pairs.
The filler again has its prescribed size and conserved sum.
Hence a failure in this range has all targets at the same end.

After whole-interval reflection and sorting, write1<=a<=b<=d<=8.
Every candidate pair lies in0..8. All original cuts are equivalent to

    a+b>=6,  a+b+d>=15,  1<=a<=b<=d<=8.

For j=1,2,3 pair bins, lower rank bounds are1,6,15. Sorted prefixes
are the minimum j-label sums, so the displayed inequalities give all
of them. Upper bounds2M-1,4M-6,6M-15 exceed the largest possible
j-label sums8,16,24 at M>=17. Any filler-containing proper group
is complementary to a pair-only group; conservation gives its bounds.
Consequently existence for ALL large M is exactly a fixed nine-token
three-pair matching question. Tokens not in its three chosen pairs
form the one filler; no separate residual partition is required.

**3. Exact finite computation.** The committed instrument is
`tests/probes/instinct/three_pair_finite_basis.py`, preregistered MI547.
It checks ALL50 sorted low triples admitted above, using pool0..8.
It also checks M8..16, with all three pair targets in the endpoint
bands and ALL original14 group inequalities:456 eligible triples at
M8 and580 at each M9..16, altogether5,096. These plus the50 low
triples are the ENTIRE finite basis supplied by steps1–2.

Engine A lists actual edges per prescribed target and chooses three
disjoint edges. Engine B independently chooses six tokens first and
enumerates all15 perfect pairings, building the whole attainable sum
support; its complete terminal count is15*binomial(M+1,6). For every
basis query both engines agree, and every positive witness is checked
for original pair sums, distinct tokens and conserved filler size/sum.
The full support has the expected reflection symmetry. On EVERY
candidate, even one rejected by the cuts, the original14 inequalities
agree with the independently reduced sorted-prefix/suffix bounds.

OUTCOME MI548: COMPLETE. The low basis omits ONLY(2,6,8); each finite
M omits ONLY that triple and its reflection. There were7,258 candidate
triples,5,146 admitted basis queries plus7 controls,477,450 secondary
terminal matchings including controls;1.230820 CPU seconds on GPT's
Intel host. No cap, retry or domain enlargement. Literal negative and
positive controls, including the actual two-hole AP quota hole, pass.
The source used has SHA256
`0125aa3e5ca08c371d925cbfbc336c1ed6f7d782e5b10d32d26591dfd9c568dd`.
Raw JSON remains outside git with SHA256
`5546c59dd6f2ff3a834628f763ff6541d0b3f0a3ffe31e80165ac93b556eaf4d`.
For regeneration run that instrument once; ordinary JSON and its timing
fields are not a deterministic certificate digest. The exact terminal
counts/support comparisons and missing lists are the finite evidence.

**4. Negative direction for every M>=8.** Sum2 forces pair{0,2}.
A disjoint sum6 pair is then forced to{1,5}. All sum8 edges
{0,8},{1,7},{2,6},{3,5} are blocked. The pair-group minimum sums
are2,8,16, above their lower bounds1,6,15; maximum sums8,14,16
are below2M-1,4M-6,6M-15 for all M>=8. Complementarity verifies
filler-containing groups. Thus these are admitted impossible inputs.
Reflection preserves the interval, counts, cuts and partition existence,
so proves the other family too. Together with the finite result and
steps1–2 this proves the stated candidate classification.

**Review boundary.** The step requiring an independent carrying read is
the unbounded merge/separation/reduction AND its precise finite-domain
interface, not merely the observed absence of other small obstructions.
This is one self-contained candidate, not a general three-target
integer-hull theorem, multiple-filler criterion, five-bin admission
result or all-n graph-burning proof. Prior-art scope was audited at
MI544; novelty remains UNASSESSED.

**Filing receipt, MI548.** Before filing, the duplicate checker passes348
entries. After filing, --near W331 passes349; its nearest G327/G328/G329
were read in full. Those address at most one size2 bin, a protected
one-hole two-pair problem, and protected adjacent targets respectively.
This full-interval three-pair exhaustion is a distinct statement using
the already proved three-bin base. No generated pages are changed.
