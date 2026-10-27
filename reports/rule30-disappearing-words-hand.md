# GC1991: disappearing words as finite trees of possible pasts

Owner asks to park the finite test, keep the question open, and start by hand on why known patterns disappear and whether failure can be delayed systematically. This is an elementary hand reduction and scoped partial result, awaiting Local's read. No new CA evolution, enumeration, solver, sampling or certificate check. Existing numerical death anchors remain numerical evidence, not replaced by hand proofs here.

Record searched: record_find.py '0010001|1000101|death criterion',308 paragraphs/128 files. Actual sources read: RULE30-PRIZE8.86, STRATEGY-PLAN's historical D5 account, GC1979 reproduction, GC1983 prefix/shift analysis, phase0 MFW44 list. The older period17 plateau and recurring-family extrapolations were refuted in the record; they are not premises. These deductions reuse the established phase/restart and factor laws. No novelty claim.

## Definitions and the exact cause of disappearance

Let L be the set of finite visible words that can begin at age0 beside wall x(t,0)=t mod2; age j means physical time2j. E_j(w) means some arbitrary initial right row exhibits w beginning at age j. The same wall phase recurs after two updates, so the established restart lemma gives E_(j+1)(w) implies E_j(w). Define d(w) as the first absent age, or infinity if no such age exists. Initially forbidden words have d=0; all other finite deaths are at least1.

A word occurs at age j exactly when some length-j prefix u makes uw a legal initial word. Thus it disappears because all sufficiently long possible opening chapters have been ruled out. For j>=1,

    E_j(w) iff E_(j-1)(0w) OR E_(j-1)(1w).

For w in L this implies the exact recursion, with infinity allowed,

    d(w) = 1 + max(d(0w), d(1w)).

Proof: if the two prefix branches first fail at a and b, both fail at index max(a,b) and at least one is present at every smaller index. The equivalence therefore puts w's first absence one index later. If one branch survives every age, so does w. The qualification w in L matters: an initially forbidden word has d=0, not1. Equivalently, for finite d, the largest legal prefix length is d-1. This explains what a death certificate must eliminate; it does not yet explain the specific long ages32/34/43 from local dynamics.

## A complete cheap failure, and what the long controls still require

Take the initially possible word10010100 (a retained age0 witness was checked in GC1983). Its only immediate past symbols are0 and1. Prefix1 creates11. Prefix0 creates0100101 at its beginning. Both are established forbidden visible factors. Therefore both prefix branches have d=0 and d(10010100)=1. This is a genuine two-branch hand explanation of a disappearance; the same argument applies to10010101.

For0010001, existing reproduced anchors give d=32. Consequently the two words00010001 and10010001 have death at most31, with at least one exactly31. This describes the final split but does not identify each branch's internal obstruction. It would be circular to call this a new hand proof of32.

For1000101, d=34 is a reproduced numerical anchor. Prefix1 immediately creates11, so there is only one viable preceding symbol0. Hence

    d(01000101) = 33,    d(1000101) = 34.

This is an exact hand consequence of the anchor: removing the forced leading0 delays disappearance by one. The remaining challenge is the mechanism ending01000101 at33. Neither the recursion nor a model at33 supplies that mechanism.

## Why the simplest ways of delaying failure do not work

If w is a factor of a longer word v at offset k, then E_j(v) implies E_(j+k)(w). Thus for finite d(w),

    d(v) <= d(w) - k

whenever v is initially possible; a nonpositive right side rules out initial possibility. In particular, appending more symbols cannot increase a finite death time, and prepending k symbols makes the deadline at least k ages earlier. A longer wrapper cannot repair a forbidden piece inside it. This is the existing factor law applied adversarially to the proposed growth mechanism.

The opposite operation can delay a death. If w begins in1, then11's exclusion makes0 its unique possible preceding symbol. Provided w is initially possible,

    d(w) = d(0w) + 1.

But this does not generate an unbounded family from one anchor: stripping one symbol shortens the word. In a fixed word of length n there are at most n-1 nonempty suffix deletions, and after a zero appears at the start the preceding symbol may no longer be unique. Extra predecessor branches may even survive forever. To obtain arbitrarily late finite deaths one needs new words with a controlled deeper obstruction, not repeated shortening of a fixed example.

The length20 control00101010001000010101 has reproduced first absence43 and a witness at42. Direct inspection shows it contains neither0010001 nor1000101. Its gaps between successive1s contain3 and4 zeros in a different context. Thus its later failure is not inherited by simply containing either seven-letter dead core. Similar-looking gaps are not enough to transfer the cause or manufacture a family.

## What could constitute a systematic delay proof

A viable construction must alter the obstruction while proving both sides:

1. A legal history reaching the proposed later age (existence).
2. Elimination of every possible preceding branch one age later (exclusion).

The exact recursion provides a useful target: construct a new terminal word whose preceding branches have known finite depths and one demonstrably deeper branch. Merely extending an old terminal word cannot do this by the factor bound. No such length-growing construction is claimed here.

Question -> response -> challenge -> better question:

- Why do words disappear? All their legal opening chapters eventually run out.
- Can we lengthen the word to postpone that? A wrapper preserves the old obstruction and cannot postpone it.
- Can we remove a forced opening symbol? Yes, a one-age delay is exact, but it spends word length and does not iterate indefinitely.
- Better question: what concrete local constraint exhausts the remaining01000101 branch at33, and can that constraint be moved farther into a genuinely new word without leaving the old dead factor intact?

Next hand task with Local: explain the anchor's carrying obstruction, starting with01000101 or a smaller fully understood branch; distinguish a conditional depth identity from a fresh hand exclusion. No new numerical stage is requested. The finite age100 test stays PARKED and the broader image-language question OPEN.


## GC1992: L1036 review and a precise column-reading lemma

Read complete L1036, its104-line tree report and complete64-line reader. The reader correctly preserves legality by checking only newly prepended forbidden prefixes, since each existing suffix is already legal. A surviving extension beyond44 causes an assertion on the next level; exclusions using listed shorter factors remain sound. The four reported finished trees fit inside the exact range (largest rejected extension length41), so the boundary issue does not affect them. Method accepted relative to the record's certified completeness; no CA/solver or independent rerun of counts here. Existing reproduced endpoints agree. GC1991's hand deductions independently carried by Local; adopted.

The shared head is z=001000010001. Its two prefixes0z=0001000010001 and1z=1001000010001 are literal phase0 forbidden entries. L1036's legal longest paths certify z is initially legal relative to the exact list. Hence d(z)=1. The longest histories of the32/33/34 anchors end on z, but many shorter branches have other terminal obstructions. A longest surviving history is selected by maximality; it is not a uniquely forced history at every intermediate level. A common terminal head does not by itself give a repeatable length-growing construction.

### Hand derivation of Local's column-2 reading

At physical time2m write the first three right cells a,b,c. The white wall gives odd-time first and second cells

    A = a OR b,    B = a XOR(b OR c).

At the following black wall update,

    v_(m+1) = NOT(A OR B).

If a=1 then A=1 and the next visible bit is0. If a=0 then A=b and B=b OR c, so the next bit is NOT(b OR c). Consequently

    v_(m+1)=1 iff a=b=c=0.

Equivalently, current v_m is0 and column2 is white at both physical times2m and2m+1. Under b=0 its odd value B=c, proving the third cell must also be white. These are direct truth-functional identities, not a simulation result. They recover no11 immediately and precisely identify the required reset row. GC503's existing latch classification supplies the complementary cases where that triple is not all white; its full five-cell formula was read. This is known local structure, applied here without a novelty claim.

### Endpoint correction to the gap statement

Count gaps as numbers of zeros between1s (the older handoff instead sometimes counts distances between1s, one larger). Suppose visible1s occur at k,k+5,k+9: gaps4 and3. For k>=3, no11 forces v_(k-1)=0. If v_(k-2)=0, the12-symbol word beginning at k-2 is exactly z, at an age at least1, contradicting d(z)=1. Thus v_(k-2)=1: the preceding gap is1.

The correct formulation is therefore: **a gap pair4,3 whose first1 is at visible age at least3 must be preceded by gap1.** The phrase 'after age0' must refer to the onset of z, not just the first1 of the pair. At k=2, z may start at0 and is allowed; at k=0 or1 there need not be an earlier completed gap in the observed history. This initial exception is exactly why an age0-only head matters.

This derives the eventual gap rule from the two certified forbidden prefixes. It is not yet a hand derivation of those prefixes from local dynamics. Proving no11 and the triple-white reset alone does not exclude all other compatible right columns. The next carrying obligation remains: use the actual evolution of columns2 and3 (and any needed further cells) to rule out0z and1z without importing their absence as a premise. Both prefix branches must be handled; a proof of z's late exclusion alone should state what past compatibility it uses.

Prior record checked: GC503/504's exact latch and no(1,2) gap proof; G238's already-carried different14-letter obstruction01000010001001; GC1796's phase-sensitive nine-word graph comparison. None is silently substituted for this13-letter pair. The tree is useful evidence organization, not yet a hand proof of the whole33-step mechanism or a general gap grammar. Numerical test remains parked.
