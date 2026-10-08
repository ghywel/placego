# The history-bearing four-gap entry excludes a spatial 011 tail

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G236. The history-bearing
four-gap entry excludes a spatial 011 tail (GPT, 2026-10-08; waiting room, GC549.28)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

The row after a history-bearing four-gap entry retains a restriction three sites beyond its familiar prefix.

**What it says.** From initial prefix 0001, a two-step output beginning 11100 cannot continue with 011. A sixteen-state spatial image map proves this in three subset transitions.

**Why it matters.** A canonical five-site prefix does not erase the incoming history. The missing visible 4,3,2 factor still needs its continuation linked to this spatial restriction.

**An everyday picture.** Two objects can share the same label at the front while their permitted contents farther inside remain different.

## The formal statement and proof

*Provenance:* GC549 checkpoints 27 and 28; single-party instrument controls in `rule30_gpt_entry_image.py`. The direct formula and three subset steps give the hand certificate. Candidate-neighbour check W236 read G126, W234 and G124: G126 uses a different sideways time-axis map, W234 composes finite clock and resonance cones, and G124 classifies periodic zero basins. The finite image method is familiar; this specific conditional spatial restriction is not their restatement. Independent reading pending; no visible fourteen-symbol absence, uniform bound or prize claim.

For the two-step bulk update at site j>=2, write initial sites j-2 through j+2 as a,b,c,d,e. The output is

    F(a,b,c,d,e)=(a XOR (b OR c))
                 XOR ((b XOR (c OR d)) OR (c XOR (d OR e))).

The spatial transducer has four-bit states (a,b,c,d). Appending e emits F and moves to (b,c,d,e). This is a sixteen-state description of one two-step image, not a finite-state description of all future visible traces.

Take an initial right row with sites 1..4 equal to 0001 and arbitrary farther sites z,u,v,... . With a white initial wall clamped black after one step and white after two, its two-step row has first four sites 1110. Requiring its fifth site zero gives z=0 or u=v=0, by checkpoint 27's direct formula. After emitting that fifth zero, the transducer state set is exactly

    A={1000,1001,1010,1011,1100}.

For subsequent emitted bits, direct substitution in F gives

    image(A,0)={0001,0010,0011},
    image({0001,0010,0011},1)={0010,0011},
    image({0010,0011},1)=empty.

Only states 1000 and 1001 in A can emit zero: the former needs appended bit one and gives 0001; the latter gives 0010 or 0011. Of the next set, only 0001 emits one, giving 0010 or 0011. Both remaining states emit zero regardless of the appended bit. Hence the two-step row cannot begin 11100011. This excludes the spatial tail 011 at sites 6..8 after its prefix 11100. It is a concrete farther-site predecessor obstruction; the five-site canonical prefix alone omits it.

*Independent reading of G236 (Cloud, 2026-10-08 15:43 BST; chat CL044).* Checked by hand and replayed by brute
force over all initial rows of 18 sites in `rule30_cloud_review_g236.py`, which shares no code with GPT's. The
formula: F is y_(j-1) XOR (y_j OR y_(j+1)) with y_(j-1) = a XOR (b OR c), y_j = b XOR (c OR d) and
y_(j+1) = c XOR (d OR e), and it agrees with two literal steps on all 32 windows. The entry: with x_0 = 0 and
x_1 .. x_4 = 0001 the time-1 sites 1 .. 4 are 0011 and the clamped wall is 1, so the time-2 sites 1 .. 4 are 1110.
The fifth site is 1 XOR (y_5 OR y_6) with y_5 = NOT (z OR u) and y_6 = z XOR (u OR v). That vanishes exactly when
z = 0 (then y_5 OR y_6 = (NOT u) OR u OR v) or u = v = 0, which gives the state set A as stated. The subset steps,
state by state: 1000 emits 1 XOR e, so zero needs e = 1 and gives 0001; 1001 emits 0 for both e, giving 0010 and
0011; 1010, 1011 and 1100 emit 1 for both e. Then 0001 emits 1 for both e, giving 0010 and 0011, while 0010 and 0011
emit 0 for both e. So the image after 11100 then 0 then 1 is {0010, 0011}, and neither can emit 1. G236 is correct as
stated.

*A sharpening (Cloud, same reading): the premise 0001 is forced.* Keep the wall white at time 0, black at 1 and white
at 2, and let the time-2 row begin 111, with no condition on the initial row. Then w_1 = 1 XOR (y_1 OR y_2) = 1
gives y_1 = y_2 = 0. Since y_1 = x_1 OR x_2, x_1 = x_2 = 0; then y_2 = x_3 = 0; and w_2 = y_3 = x_4 = 1. So every row
whose two-step image begins 111 starts 0001, and G236 applies to it. *Corollary.* In a period-2 wall form (the wall
white at even times, black at odd ones), at every even time t >= 2 sites 1 .. 8 never read 11100011, whatever the
row at time t - 2 was. The same lines show that the prefix 110 never occurs at an even time t >= 2. If w_2 = y_3 = 1,
then w_3 = y_2 XOR (y_3 OR y_4) = 1. So the branch 1101* that checkpoint 27 removes with the preceding visible zero
is excluded by evolution alone. The preceding zero's role is to certify that the row is at least two steps old.
Likewise the visible word never contains 11: a black column 1 at an even time makes y_1 = 1 two steps later, so
w_1 = 0. Hence the shortest absent visible factor 01000010001001 (CL041) is absent if and only if 1000010001001
never begins at an even time t >= 2. The symbol before any later start is 0, because 11 is absent. This restates
the open target without its leading zero; it does not prove it. The brute force also lists 65 minimal missing
prefixes of the walled two-step image up to length 10, beginning 110, 0110, 1010, 1111. 11100011 is one of the nine
of length 8. No prize claim.


**Review-status receipt for G235 and G236 (GPT, 2026-10-08).** The historical waiting-room labels are superseded as regards verification: Local independently verified G235's hand proof and both deterministic controls in L287 (Git d9f2d22f); Cloud independently verified G236 and supplied the stronger two-step-image premise in its reading above, CL044. Local's reading of G235 checks the induction from the first two permanently zero tail bits, the countable null absorption set using the already reviewed invariance, and both finite-tail/all-ones controls. No simultaneous-cylinder recurrence follows. Neighbour checks W235 and W236 again pass; the previously read G149,G141,G97 and G126,W234,G124 remain the respective nearest older entries. G97 is the measure-invariance dependency, and the other entries do not restate these claims. This receipt records verification without copying proofs or claiming a prize.
