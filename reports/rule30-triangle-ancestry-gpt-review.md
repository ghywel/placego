# L998 triangle ancestry: targeted independent review

GPT, 26 October 2026, GC1933. Read L998 in full at20bb9de3, all192 lines of reports/rule30-triangle-ancestry-local-read.md and all170 lines of tests/probes/wolfram/triangle_parents_check.py. No script execution, new experiment, schedule restart or portal work. Read the relevant8.18/8.82 record in GC1932 and8.68 including its withdrawn Poisson significance statement in this review.

## Verdict

Adopt Local's independent carrying read of GC1932. The cap classification, backward maps, periodic templates and singleton correction now have both parties' reads. L998's parent trichotomy, deterministic singleton-child rule, H1/H2 counterexample and explicitly conditioned first-generation fair-row law carry by the hand arguments below. Several explanatory sentences need the scope amendments in section4. No novelty, general renewal process or single-seed law is adopted.

## 1. Three parents and their counts

For a maximal output zero run[a,b] of lengthL with output ones at both ends, f(L,C,R)=L XOR(C OR R) forces precisely:

- C: 1 0^(L+2) 1 on[a-2,b+2].
- A: 0 1^(L+1) 0 0 on[a-2,b+2].
- B: 0 1^L 0 1 on[a-2,b+1], with x(b+2) free.

I checked both flanks as well as the zero interior, includingL=1. Right-pair00 gives C. Right-pair10 gives A after its right output-one condition; right-pair11 cannot give that right output one. Right-pair01 gives B. The left output one fixes the leading bit in each case. The alternatives are disjoint and exhaustive.

Under an independently fair input row, C and A each fixL+4 bits and B fixesL+3. Their unconditional probabilities are2^(-(L+4)),2^(-(L+4)),2^(-(L+3)); conditioned on the displayed maximal run the shares are1/4,1/4,1/2. Among non-continuation tops A+B the fractions are1/3 and2/3. This is an exact model count, not an established frequency split in the single-seed picture. It agrees with8.68's total top probability. No invariance theorem is needed for this one-step cylinder count; invariance allows the same fair-row marginal at later deterministic times.

With vertical/horizontal white connectivity, A has no parent white cell above its run, B has the singleton, C has the wider run. This classification carries; 'independent triangle' should mean absence of a white parent under this connectivity convention, not statistical independence of births.

## 2. The child and the explicit counterexample

Let the isolated white tip be atc in rowx. Suppose the maximal black run on its left is[p,c-1] and x(p-1)=0. Then the next row has ones atp,c+1 and zeros exactly on[p+1,c]. Atp the left parent is0 and the centre1; in the interior the left and centre are both1; atc the triple is101; atc+1 its left parent is0 and centre1. These four checks prove the statement, including black-run length1. A finite left endpoint is an assumption: an infinite black half-line would not give a finite child width.

The deciding black run is in the SAME row as the singleton tip, before the child's update. The report's phrase 'one row after the tip forms' is one step late; use 'at the tip time (one update after the displayed white triple)'.

H1/H2, indexedc-5..c+4, carry without replay. They share the white triple[c-1,c+1]. One update later both have an isolated zero atc and a one atc-1. H1 has y(c-2)=0, hence child width1. H2 has y(c-2)=y(c-3)=1 and y(c-4)=0, hence width3. The differing initial bit is c-3. Thus own width, position and immediate flanks do not determine this descendant; this does not refute richer descriptions containing the relevant surrounding cells.

## 3. First-generation width law

Use exactly the conditioning in L998: a fixed-time input row with10001 on[c-2,c+2] and all other cells independently fair. After one step y(c)=0, y(c-1)=y(c+1)=1. Moving left from y(c-2), each output depends by XOR on a previously unexposed fair input, with all remaining parents already fixed/exposed. Conditional on the inspected suffix, the next output is fair. Hence the probability of k-1 further black cells followed by white is2^-k; this gives child widthk for everyk>=1. The infinite black-run event has probability0. Summing evenk gives1/3.

This does NOT yet establish the same conditional law for a tip reached by following a previously selected lineage, nor independent child widths, nor almost-sure termination of that lineage, nor behaviour of the fixed single-seed orbit. That adaptive conditioning is precisely the unresolved dependency. Local already leaves independence open; retain the exact fixed-time conditioning whenever quoting the law.

## 4. Backward maps and wording amendments

I checked the additional block maps by composition of the previously carried T_0,T_1. In pair order00,01,10,11:

    B_101110 = (10,01,01,01)
    B_110010 = (00,00,00,00)
    B_011100 = (00,11,11,11).

Their cycles, phase/pattern alternatives and stated forward templates carry. For the six-periodic preimages, fixed points of each six-cell block map give the declared aligned periodic ancestors. The branch at011100 is the first two-distinct-pattern branch along this displayed chain; the earlier101 level already has phase ambiguity.

- A four-state block orbit enters a cycle after at most3 blocks. This bounds the TRANSIENT, not all boundary uncertainty. Different attracting cycles or different positions in a cycle can leave phase/pattern ambiguity throughout the interior. Local's conditional discussion recognizes this; do not abbreviate it as 'the uncertain margin is always at most3 blocks' without the surviving template choice.
- T_0,T_1 both merge10 and11: when the common upper centre is1, the differing upper right bit is masked. 'Boundary forgotten exactly where black cells appear' is too broad: other pairs containing black need not merge. For example T_0(01)=10 and T_0(11)=11 remain different.
- The shape-A cap's two-phase account follows from T_0 twice sending all pairs into{00,11}, followed by the T_1 cycle. Preserve the possible terminal011 departure; an exact periodic interior is not a claim about every endpoint bit.
- A black band's parent has a periodic interior of white pairs separated by ones. Those pairs end together. At finite boundaries retain the allowed truncated/terminal patterns; do not describe every bit of the entire actual predecessor row as such a lattice.

## 5. Executable and evidence scope

The source implements the advertised six-ring checks, exhaustive finite-window C/A/B classification, singleton rule and conditional child-width enumeration. I inspected indexing and bounds; I did not run it or independently recount reported totals. Runtime2.3s and totals851972/425986 remain producer-reported, not a newly verified receipt. The header retains an earlier K4 assertion failure and its indexing correction; do not recast the history as a clean first run.

K4 uses15 free input bits, omits children extending beyond the determined window, and explicitly asserts its geometric counts only for k=1..10 (range(1,M-9), M=20). Its support is a finite guard, not a verification of all k. The all-k conclusion comes from section3's fresh-bit proof. H1/H2 are checked by hand above; this committed script does not contain explicit H1/H2 fixtures. The program prints failures but does not turn a nonzero fails total into a nonzero process exit; any later reuse in automation would need that failure-contract repair before relying on exit status. No rerun requested.

## 6. Owner's latest sharpening and next question

The owner emphasizes birth followed by forced erosion: a repeating precursor forms a black band, which creates a white patch whose interior then narrows. Preserve the singleton exception and the distinction between a triangle core and its connected white lineage. The confirmed singleton-child rule now makes that distinction concrete.

The useful new question is what surrounding information determines a lineage beyond its first child. The fair-row renewal question is also precise but needs its stopping-time conditioning handled before extrapolating2^-k across generations. No next test or computation is accepted by this review. Remain in owner-led question/response/challenge mode; L997's unrelated funnel comparison stays separately unreviewed.
