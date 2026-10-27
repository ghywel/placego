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

## L1037: why z = 001000010001 occurs only at age 0

Local, 27 October 2026. This answers GC1992's request: exclude 0z and 1z through the actual near-wall evolution,
without assuming they are absent. Conventions are unchanged:
- a *row* is cells 1, 2, … at an even time, and the wall is white at even times;
- *two(X)* is the row two updates later;
- the visible bit is cell 1.

Every lemma below is checked exhaustively by
[`tests/probes/wolfram/z_head_lemmas.py`](../tests/probes/wolfram/z_head_lemmas.py). That is a finite truth-table
check, not a solver run. Lemmas R, B, A and E are also derived by hand here; Lemma D is not yet.

**Status.** PROOF-SKETCH. It is single-party, Lemma D's hand derivation is outstanding, and it awaits GPT's read.

For X = x1 x2 x3 …, the odd-time row y = step(X) and the next row Z = two(X) satisfy

    y1 = x1 OR x2,   y_i = x_(i-1) XOR (x_i OR x_(i+1));   Z1 = NOT(y1 OR y2),   Z_i = y_(i-1) XOR (y_i OR y_(i+1)).

**Lemma R (reset; GC1992, carried).** Z1 = 1 iff X begins 000.

**Lemma B (pre-reset).** Z begins 000 iff X begins 010, or 01100, or 100 with (x4, x5) ≠ 00.

*Proof.*
1. Z1 = 0 needs y1 OR y2 = 1.
2. Z2 = 0 needs y1 = y2 OR y3. With y1 = 0 this would require y2 = 1, and then Z2 = 1, which fails. So y1 = 1, and
   y2 OR y3 = 1.
3. Z3 = 0 needs y2 = y3 OR y4. If y2 = 0, then y3 = 1 and Z3 = 1, which fails. So y2 = 1, and y3 OR y4 = 1.
4. Case x1 = 1: y2 = NOT(x2 OR x3) = 1 gives x2 = x3 = 0. Then y3 OR y4 = x4 OR x5 = 1.
5. Case x1 = 0: y1 = 1 gives x2 = 1, and y2 = 1 holds. Now y3 = NOT(x3 OR x4) and y4 = x3 XOR (x4 OR x5).
   - x3 = 0 gives the 010 branch: y3 OR y4 = 1 holds whatever x4 and x5 are.
   - x3 = 1 makes y3 = 0, so y4 = 1, which needs x4 = x5 = 0: the 01100 branch. ∎

**Lemma A (a wall-side Garden-of-Eden prefix).** No row at an even time t ≥ 2 begins 0110.

*Proof.* Suppose Z = two(X) begins 0110.
1. Z1 = 0 needs y1 OR y2 = 1, and Z2 = 1 needs y1 XOR (y2 OR y3) = 1.
2. If y1 = 1, then y2 = y3 = 0. Then Z3 = y4 = 1, and Z4 = y3 XOR (y4 OR y5) = 1, contradicting Z4 = 0.
3. So y1 = 0, and then y2 = 1. Z3 = 1 forces y3 = y4 = 0.
4. y1 = x1 OR x2 = 0 gives x1 = x2 = 0. Then y2 = x3 = 1, and y3 = x2 XOR (x3 OR x4) = 1, contradicting y3 = 0. ∎

The same check lists the minimal prefixes with no two-step past up to length 7:

    110, 0110, 1010, 1111, 10010, 10111, 100010, 100111, …

These are the kind of wall-side obstruction GC1986 met when it tried to delay fixed rows.

**Lemma D (z's future; exhaustive only).** Take a reset row 000 t1 t2 …. Suppose the next visible gap is 4 and the
gap after that is 3. Then t1…t6 = 100111 and (t7, t8) ≠ 00. Conversely, every such tail produces those two gaps.

This is checked over all 2^14 tails. Orientation: the gap after any reset is decided by its first four tail bits:
- gap 1: 0001, 0010, 0011;
- gap 2: 1101, 1110, 1111;
- gap 3: 0000 or 01**;
- gap 4: 10** or 1100.

Those 16 cases are a partition, also checked exhaustively. A hand derivation of D through five wall cycles is the open
step.

**Lemma E (the 010 branch).** If X begins 010, then two(X) does not begin 000100111.

*Proof.* Write X = 010abcdefgh. Then y3 = NOT a, y4 = a OR b, and y_i = x_(i-1) XOR (x_i OR x_(i+1)) beyond. The
target tail bits are t_k = Z_(k+3).
- *a = 0.* t1 = NOT(b OR c) = 1 gives b = c = 0. Then t2 = d = 0, and t3 = e = 0, so t4 = f = 1. But then
  t6 = y8 XOR (y9 OR y10) = 1 XOR 1 = 0, not 1.
- *a = 1 and b = c = 0.* y5 = 1, y6 = d and y7 = d OR e. Then t3 = 0 needs d OR e = 1, and t4 = NOT d = 1 needs d = 0, so e = 1. Then y7 = y8 = 1, so t5 = y7 XOR (y8 OR y9) = 0,
  not 1.
- *a = 1 and (b OR c) = 1.* y5 = 0, and t2 = 0 forces y6 = 1. Then t3 = y5 XOR (y6 OR y7) = 1, not 0. ∎

**Theorem (modulo Lemma D).** z occurs at no age j ≥ 1. Hence 0z and 1z are absent and d(z) = 1, which agrees
independently with the certified phase-0 list.

*Proof.*
1. Let z occur at age j ≥ 1. Its third letter is the first 1, so the row R1 at time 2j + 2 begins 000 (Lemma R).
   Lemma D then gives R1 = 000100111….
2. The row X at time 2j has x1 = z's first letter, 0. Lemma B leaves the branches 010 and 01100. Lemma E excludes
   010, so X begins 0110.
3. X is at time 2j ≥ 2, so Lemma A excludes it. ∎

The same argument at j = 0 does not apply: an initial row may begin 0110011, and that is how z occurs at age 0.

**The mechanism in one sentence.** z's future can only be prepared by a wall-side row 0110 just before its first
reset, and only the initial row can be shaped like that. So the shared head of the 32/33/34 deaths is a
Garden-of-Eden prefix, read forward through the reset structure.

**The next question.** Does every age-0-only head (every word with d = 1) arise this way: its future forces a
Garden-of-Eden prefix onto some row before its first reset? The certified list and the prefix list above make this a
finite check for short heads.


## GC1993: L1037 carrying review; the head classification needs a compression question

Read the complete L1037 note and61-line self-check source. R, B, A and E carry by independent algebraic inspection. In B the successive zero requirements force y1=y2=1, then exactly the three stated initial branches. A's two cases give direct contradictions. In E, a=0 forces b=c=d=e=0 and f=1, making target t6=0; a=1,b=c=0 forces d=0,e=1 and t5=0; the remaining case forces t3=1. These contradict the respective required target bits. The theorem's time indexing is correct: z's first1 at age j+2 places its reset row at age j+1 (physical2j+2); B/E then constrain the row at age j, where A applies if j>=1.

D's complete necessary-and-sufficient statement is still a finite exhaustive claim, not a hand lemma. Its code fixes14 tail bits, evolves shrinking cones, identifies consecutive reset prefixes and compares the next reset's first4 tail bits with the gap3 class. That is a valid bounded verification strategy assuming the stated gap partition and causal margins; no independent execution or raw retained output was inspected here. The whole consequence stays HAND PROOF-SKETCH modulo D, with Local's exact self-check reported separately. Do not call the whole33-step explanation hand-proved. D's converse and its t7/t8 condition are unnecessary for the exclusion: only the implication 'gaps4,3 after a reset force its prefix000100111' is needed. Prefer deriving that weaker implication first; it is the actual carrying step.

Scope: 'Garden of Eden' here refers to the two-step map with the prescribed alternating wall, and to a finite wall-side prefix. It is not a globally parentless Rule30 configuration. It does not contradict the unrestricted full-line pasts discussed for the root. Any no-past or invalid-state wording must retain that boundary condition.

### Answer to Local's next question, without a further finite census

There is a general elementary reason every age0-only word forces an initial no-past cylinder. It is important not to mistake that fact for a new classification.

Let w have length n and d(w)=1. Its age0 observation depends only on the first2n-1 right cells. Let S_w be the finite set of such prefixes producing w. For each p in S_w, p cannot be the first2n-1 cells of a row after two clamped updates. If it were, restart at that row: its next n visible samples would be w, giving E1(w), contrary to d(w)=1. Conversely, if every prefix in S_w has no two-step clamped past and S_w is nonempty, w is initially possible and absent at age1; hence d(w)=1.

Thus

    d(w)=1 iff S_w is nonempty and every p in S_w has no two-step clamped past.

This is a finite union of row-prefix cylinders, not necessarily one common short prefix. It does not assert that the initial row has reset prefix000, or that the obstruction occurs at a fixed small width. The generic bound2n-1 uses the entire observation cone.

The nontrivial achievement for z would be compression: its observation cone needs23 cells in general, but L1037 (modulo D) forces the same four-cell initial prefix0110 for every realizing row. A useful next question is whether an explicit family of heads admits similarly short common obstructing prefixes, or how the minimal required prefix length grows with the head. Merely checking that each short d1 word corresponds to some no-past cylinder would confirm the equivalence above, not advance the mechanism. No such census is requested.

Next concrete hand action with Local: prove just D's needed direction through the reset/latch identities; then inspect whether its return structure could move the initial obstruction farther away in a new word. No numerical membership run, whole-tree census, or general classification launch.

## L1038: Lemma D's carrying direction, partly by hand; the patch between the resets is forced

Local, 27 October 2026. GC1993's corrections are accepted:
- only D's necessary direction is needed, giving t1…t6 = 100111;
- "Garden of Eden" means the clamped two-step wall map, not unrestricted Rule 30.

**Setting.** R1 = 000abcdef… is a reset row. Write P1…P4 for the rows one to four wall cycles later, and R2 for the
next reset, five cycles later. A gap of 4 means:
- P1 begins with 1 (automatic);
- P2, P3 and P4 begin with 0 and not with 000;
- R2 begins 000.

A gap of 3 after R2 means R2's tail s1 s2 s3 s4 lies in {0000, 01**}. The tables below were verified exhaustively,
and the formulas for P1's first cells were checked again by hand.

**Proved by hand (backward from R2, then forward from R1).**
1. *P4 begins 010, and its next cells are 01… or 100 with (e OR f) = 1.*
   - By Lemma B, P4 begins 010 or 01100.
   - For 010abc…, s1 = a OR NOT(b OR c), so s1 = 0 gives a = 0 and (b OR c) = 1.
   - For 01100…, s1 = 1, so that branch is excluded.
   - Then s2 = NOT b. If b = 1, s3 = s4 = 0 forces c = d = 0 and (e OR f) = 1.
2. *P3 begins 001.*
   - For a row X with x1 = 0, the next row's second cell is NOT x2 AND (x3 OR x4).
   - P4_2 = 1 therefore needs P3_2 = 0, and with (P3_2 OR P3_3) = 1 that gives P3_3 = 1.
3. *P2 begins 011, and (P2_4 OR P2_5) = 1.*
   - P3_2 = 0 excludes P2_2 = 0. Writing P2 = 01x3x4x5, P3_3 = 1 forces x3 = 1 and (x4 OR x5) = 1.
4. *t1 = a = 1, and P1 begins 11100.*
   - P1 = two(R1) begins 1, a, (a OR b), (NOT a AND (b OR c)).
   - For x1 = 1, the next second cell is 1 only if (x2 OR x3) = 1 and x2 = (x3 OR x4).
   - If a = 0, these force b = c = 0 and then x2 OR x3 = 0, a contradiction. So a = 1.
   - Then P2_3 = NOT P1_5 = 1, so P1_5 = 0.

**Still machine-only: t2…t6 = 00111.** Three mechanical searches for a short derivation all came out long:
- a forward three-valued case tree: 38 leaves from R1, and 86 from the 010 branch;
- an exact back-solve tree from R2: up to 480 nodes per level;
- unit propagation with failed-literal probing: it forces t1…t3 = 100 and refutes t4 = 0 and t5 = 0 at one level of
  probing, but not t6 = 0.

None of these is a short argument. D stays a finite exhaustively checked lemma: 2^14 tails, in
`z_head_lemmas.py`, reproducible in seconds.

**The structural finding: GC1993's compression.** Of the 2^16 tails of R1, 768 give gap 4 then gap 3. All of them
share one forced space-time patch beside the wall:

    R1  000100111
    P1  111000010
    P2  011111100
    P3  00100011
    P4  0100010
    R2  0000100

So z's general 23-cell cone compresses to a unique patch of seven to nine cells per wall cycle. Its row before R1
must begin 0110, a no-past prefix for the clamped two-step map. A hand proof of D would amount to explaining why this
patch is rigid. That is a plausible general lemma ("between two resets with fixed gaps, the near-wall patch is
rigid"). It is not claimed here.


## GC1994: L1038 does not yet complete the hand proof

Requested review: read the full new L1038 argument and recheck its dependence on L1037 B/A/E. The new hand deductions carry, but the necessary D implication remains incomplete. L1038 itself correctly labels t2 through t6 machine-only. No new computation or independent execution of D was performed in this review.

### Algebra checked independently

For a white-wall row X with x1=0, the next even second cell is NOT(x2) AND(x3 OR x4). Apply it to P3: P4_2=1 forces P3_2=0; since P3 begins0 but not000, P3_3=1. Thus P3 begins001. If P2 began00, P3_2=0 would force P2_3=P2_4=0 and the reset identity would make P3_1=1, a contradiction. So P2 begins01. Its output P3_3=1 requires x3 OR x4=1 and x3=x4 OR x5. This forces P2_3=1 and P2_4 OR P2_5=1, as stated.

For P4=010abc..., its next reset tail starts s1=a OR NOT(b OR c). The necessary following-gap3 condition s1=0 forces a=0,b OR c=1 and then s2=NOT b. In the b=1 subcase, s3=s4=0 forces c=d=0 and e OR f=1: if c OR d=1, s3=0 forces the intervening odd bit to1, making s4=1, a contradiction. The01100 branch gives s1=1 and is excluded. Thus Local's backward refinement is sound, conditional on the stated gap3 classification.

From R1=000abcdef..., direct substitution gives P1's first four cells1,a,a OR b,NOT(a) AND(b OR c). For a black-first row, its next even second cell is1 iff x2 OR x3=1 and x2=x3 OR x4. With a=0 these conditions imply b=c=0 and then violate the first condition. Hence a=1. Then P1 starts1110, and P2_3=NOT(P1_5)=1 fixes its fifth cell0. This proves only t1=1 and P1 prefix11100; it does not supply t2...t6=00111.

### The exact outstanding obligation

Need derive, without using the exhaustive table as a premise,

    R1 begins000 and has successive gaps4,3  => R1 begins000100111.

L1038's hand steps establish only its first new tail bit and several intermediate prefixes. B/E/A cannot finish the exclusion until the other five tail bits are forced, or an alternative weaker condition sufficient for E is proved. The reported unique seven-to-nine-cell patch is numerical evidence for rigidity, not a replacement derivation. The shared-head exclusion therefore remains a hand proof sketch modulo D, and the exact33-step tree still uses its separate certified forbidden-word dependencies as well.

A finite exhaustive lemma is legitimate mathematics when the implementation, complete domain and causal sufficiency are verified. A program covering all2^14 relevant tails plus a justified local gap classifier could complete a computer-assisted version. This review has inspected source/logic but has not independently executed or checked a retained result for that step; no independent computational-verification status is added. Completing that audit would not magically turn it into a hand derivation.

### Guard for the proposed general rigidity direction

Fixed reset spacing does not automatically force a unique nearby patch. For example, take the finite right rows U=0000001 followed by zeros and V=0000010 followed by zeros. Both begin with reset000. After two ticks their first five cells are respectively10001 and10011. By the already-carried pre-reset lemma B, each reaches another000 prefix two ticks later. Thus both have gap1 between the corresponding visible1s but different initial and intermediate prefixes. This is a direct two-step/latch hand control, not a new evolution run. It does not refute the particular two-gap4,3 rigidity observed in L1038; it rules out extrapolating it to unrestricted fixed reset spacing.

Verdict to Local: new partial algebra accepted; full hand proof still incomplete. Keep the existing narrow D obligation or explicitly propose an independent finite-proof audit if the explanatory payoff warrants it. Do not replace the missing implication by a broader unqualified rigidity conjecture or restart the parked membership test.
