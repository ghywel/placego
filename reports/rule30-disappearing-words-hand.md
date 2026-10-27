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
