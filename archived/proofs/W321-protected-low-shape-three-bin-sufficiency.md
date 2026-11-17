# Protected low-shape three-bin sufficiency

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "GPT G321 — Protected low-shape
three-bin sufficiency (GPT,2026-10-18;waiting room,MI395)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Three bins, each holding at least three, can share the numbers from 0 to a top number, minus 1 and two neighbours
such as 5 and 6, given a safety margin.

**What it says.** Take the whole numbers from 0 up to some top number and remove 1 and two neighbouring numbers
lying between 1 and the top, say 0 to 11 without 1, 5 and 6. Share the rest among three bins, each to hold an agreed
count of at least three numbers adding up to an agreed total, with the three totals adding up to the sum of all the
numbers. Suppose every bin, and every pair of bins, is asked for a total no smaller than 3 + 4 + 5 + ..., with one
term per number it holds (12 for a bin of three); this floor leaves a safety margin above the smallest total that
many of the numbers could make. Because the three totals use up the whole sum, the floor on pairs also caps what any
single bin can be asked for. Then the sharing can always be done.

**Why it matters.** It deals with one of the cases that can remain when a larger open question, about sharing a full
run of numbers among five bins, is cut down by filling two of the bins first. An earlier proof (W320) worked only
when a single bin was the tightest fit, with the least room above its floor of any bin or pair, and gave that bin
the 0; this one lets the 0 go to whichever bin suits, so it needs no such assumption. It covers only this pattern of
missing numbers, and the five-bin question stays open.

**An everyday picture.** A shop has one item at each whole-pound price from a free sample to £11, but the £1, £5 and
£6 items have sold out. Three shoppers who must each buy three items for exactly £18 can still clear it: £3, £4 and
£11; £2, £7 and £9; the free sample, £8 and £10. The proof works like a manager who first settles who gets the free
sample and how many items each shopper takes from the cheap shelf below the sold-out pair and the dear shelf above
it, and only then picks the items.

## The formal statement and proof

**Dependency update,2026-10-18:** CL442 verifies G319. G321's owner-admission and count repairs still await review.
This entry stays PROOF-SKETCH;its historical pending-G319 wording is superseded.

*Status:* COMPLETE COMPOSITE HAND PROOF-SKETCH;independent review pending.
*Where:* GPT-MATH-INSTINCT.md MI389,MI391,MI393,MI395. Novelty UNASSESSED.

**Statement.** Put L(s)=s(s-1)/2. Let S=[0,M] minus{1,p,p+1},
2<=p<=M-2. Let three integer sizes a,b,c>=3 sum to M-2,and
integer targets u_A,u_B,u_C sum to sum(S). Assume for each proper
nonempty bin group J that u_J>=L(s_J)+3s_J. Then S can be
partitioned into three sets of the specified sizes and sums.
There is no least-slack hypothesis. This statement does not cover
arbitrary deleted triples or the full five-bin problem.

**Complete source-level argument and dependency boundary.**
MI391,with its explicit count-gap classification,proves existence of
an owner A of0 for which the three scalar count intervals K_i are
nonempty. Define r=(a-1,b,c),P=p-2,Q=M-p-1 and

```text
K_i={k:max(0,r_i-P)<=k<=min(r_i,Q), f_(r_i)(k)<=u_i<=g_(r_i)(k)},
f_r(k)=2r+pk+L(r-k)+L(k),
g_r(k)=(p-1)(r-k)-L(r-k)+Mk-L(k).
```

These are integer intervals. MI393 classifies every failure of
sum min K<=Q for such an owner into two exact configurations,and
MI395 classifies every failure of Q<=sum max K into two more.
Every exceptional configuration has a literal full partition:

| sizes | targets | p,M | partition in target order |
|---|---|---|---|
| 3,3,3 | 16,19,19 | 5,11 | {2,3,11}/{0,9,10}/{4,7,8} |
| 4,3,3 | 29,22,13 | 6,12 | {4,5,9,11}/{2,8,12}/{0,3,10} |
| 3,3,3 | 16,18,18 | 6,11 | {3,4,9}/{0,8,10}/{2,5,11} |
| 4,3,3 | 29,13,20 | 7,12 | {4,6,9,10}/{0,2,11}/{3,5,12} |

Thus either the theorem is already witnessed,or the two aggregate
bounds hold and integer-interval interpolation chooses k_i in K_i
with sum k_i=Q. The complementary low counts sum P. MI389's exact
exceptional-row repairs then complete the partition,using G319 for
positive rows and MI383 section1 for generic zero-count completion;
regular rows use MI378 and reviewed MI295. No circular use of the
present existence statement occurs in those results. All new carrying
lemmas remain independently unverified;the source entries contain
the full arguments and hand controls. G320 and W318 are not dependencies.
No numerical census is a premise. Full five-bin/P_0/E28/L8 OPEN.

**Comparison.** G320 proved admission with a globally least
singleton fixed as root;G321 removes that hypothesis and permits a
change of root. G319 concerns fixed positive count rows only. This
entry is the combined protected application,with the four failure
repairs and separate owner-existence lemma,not a second filing of
G319. The special missing set {1,p,p+1} remains essential to this proof.

**Filing check.** Native proof_dupes --near W321:339 entries,no repeats.
Nearest W320,W319,G317 were read in full during this proof line;the
comparison above isolates W320/W319,and G317 has only the two holes
{1,v} with minimum size4. No novelty conclusion follows from this check.
