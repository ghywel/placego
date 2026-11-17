# Neutral gap blocks do not force zero entropy

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT239. Neutral gap blocks do not force
zero entropy (second-read by Cloud, 2026-10-08)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

Perfectly balanced blocks can still carry choices.

**What it says.** Six equal-length gap blocks have the same number of ones and zero net charge, yet their arbitrary concatenations have positive entropy and bounded charge discrepancy.

**Why it matters.** Exact wheel balance and the listed forbidden words alone cannot establish zero boundary entropy. These abstract words have no proved Rule 30 realization.

**An everyday picture.** Six boxes can weigh the same while holding different messages.

## The formal statement and proof

**Promoted from the waiting room, 2026-10-08 (GC620; Local L334).** Second reader: Cloud, chat CL047. Waiting-room heading: "G239. Neutral gap blocks do not force zero entropy (GPT, 2026-10-08; waiting room)". The text below is unchanged, so its *Status:* line is historical.

*Scope.* An abstract binary gap language only. This is a standard equal-length block construction applied to CL045's charge, not a Rule 30 realization or a lower bound for portfolio question 4.

Let S=100 and L=10000. Take the six length-28 words formed by placing one S among five L blocks. Every word has six ones and charge 14*6-3*28=0. Their positions of successive ones distinguish all six words. Arbitrary concatenation therefore supplies at least 6^k distinct length-28k factors in the shift closure X of these concatenations. Thus its topological entropy is at least log2(6)/28 bits per symbol, strictly positive. Equal lengths suffice for this count; no claim about ambiguous variable-length parsing is needed.

For charge Q(n)=14*ones(prefix n)-3*n, each complete S contributes +5 and each complete L contributes -1. Before the short block, complete-block charge runs from 0 down to at worst -5; afterwards it runs from at most +5 back to 0. Within any block its initial one raises charge by 11 and each following zero lowers it by 3. Consequently -5<=Q(n)<=16 for every concatenation prefix, since each 28-symbol group resets charge to zero. Every factor, including factors in the shift closure, has absolute charge at most 21, by subtraction of two prefix charges. Every member of X therefore has density 3/14 with uniformly bounded discrepancy, a stronger requirement than a limiting balance.

All successive ones are separated by exactly two or four zeros. Hence X avoids 11 and 00000, as well as CL041's 101001,0100101,010010001,0101000101,0101010000: each of these last five contains an internal one-zero or three-zero gap. G238's 01000010001001 contains an internal three-zero gap and is also avoided. Thus these finite necessary restrictions together with bounded charge still permit positive entropy abstractly.

*Unexpected check and counterfactual.* The stronger bounded-prefix requirement holds, not merely density at group endpoints. There are uncountably many distinct one-sided concatenations but only countably many eventually periodic binary words; some concatenations are not eventually periodic. Exact charge balance therefore does not force periodicity either. No experiment was run. Additional Rule 30 predecessor constraints may exclude this entire construction; their absence here is precisely the missing realization obligation. No statement about the actual wheel's entropy, kick drift or singleton trace follows.

*Duplicate audit.* W239 nearest older entries G168,G48,G126 read in full. G126 uses the same standard equal-length block entropy argument for a different ternary image; G168 concerns potential reserves and G48 affine lifts. This application adds exact neutral binary gap blocks and bounded discrepancy, without a novelty claim or a restatement of their conclusions. Initial audit missed the nonstandard heading; corrected the heading and reran successfully.



**G239 extension: its entire abstract family survives controlled width 2 (GPT, 2026-10-08; awaiting reading).** This is a finite-width realization, not an autonomous infinite right half. Let the current two-site state be (a,b), with wall 0, and let free exterior column 3 take values u,v on the two updates. The odd pair is (a OR b, a XOR(b OR u)); the next wall is 1. The next even pair is therefore

    (1 XOR ((a OR b) OR (a XOR (b OR u))),
     (a OR b) XOR ((a XOR (b OR u)) OR v)).

Varying u,v yields the complete relation

    00 -> {10,11,01}; 01 -> {00};
    10 -> {00,01};    11 -> {00,01}.

Consequently state 10 has loops 10,01,00,10 and 10,01,00,01,00,10. Their visible bits between visits to 10 are 100 and 10000. Every succession of two- and four-zero gaps can concatenate these loops, choosing the free exterior inputs separately for each edge. In particular G239's six neutral length-28 blocks and every infinite concatenation have a controlled width-2 realization. Shift invariance supplies the shift closure too. Thus h(X_2) is at least log2(6)/28, but this gives no uniform lower bound as width increases.

*Checks and limits.* Prediction of a shared black state holds. All 16 source/input assignments agree between literal decimal Rule 30 and the paired formula, and their four successor sets match the hand split. The unexpected hidden-neighbour check retains state 01 rather than collapsing all white samples: it is needed for the four-gap loop. As a further scope control, fixing both exterior inputs to zero removes edge 00 to 01 and this four-gap loop. The preregistered wider-extension counterfactual is unsupported: at width 3 those exterior bits become interior and must obey a new Rule 30 equation, which the width-2 graph never checked. No assertion that every extension fails, or succeeds, is made. Next identify a compatible exterior coding or an actual obstruction, retaining that equation; do not extrapolate this graph to all widths. This is an extension of the same G239 guard, not a new numbered lead.

**G239 extension: controlled width 3, with a changed hidden state (GPT, 2026-10-08; awaiting reading).** Write the current state as (a,b,c), free exterior inputs at column 4 as u,v, and the odd triple as p=a OR b, q=a XOR(b OR c), r=b XOR(c OR u). Its next even triple is (1 XOR(p OR q), p XOR(q OR r), q XOR(r OR v)). Direct splitting gives the needed relation

    111 -> {010,011}; 011 -> {000,001};
    001 -> {010}; 010 -> {000,001};
    000 -> {100,101,111}.

The common state 111 has loops 111,010,000,111 and 111,011,001,010,000,111, spelling 100 and 10000. Each edge has independently selectable column-4 inputs, so arbitrary concatenations realize G239's entire neutral family at controlled width 3. Shift closure follows by advancing the clamped wall two ticks. This improves the finite-layer lower bound to h(X_3)>=log2(6)/28, with no all-width claim.

*Predictions and controls.* The common-state prediction holds; 32 assignments of a,b,c,u,v agree with literal decimal Rule 30 and produce the five displayed successor sets. The old explicit lift fails: for current state 10c every successor has second bit zero, so the width-2 edge 10 to 01 cannot lift. This is the unexpected retained dependence r=b XOR(c OR u), and the preregistered unchanged-lift counterfactual is refuted. The alternative state 111 repairs the finite construction, rather than pretending its old hidden state survives. No width sweep, language census, wheel computation or autonomous exterior construction was attempted. Stop small-width enumeration here; a uniform construction needs a new mechanism.

*Scope reading of G239 and its width-2 extension (Cloud, 2026-10-08 16:32 BST; chat CL047; GC551, GC551.1).* G239 is
correct as stated. The six blocks have length 28, six ones and charge 0, and they are distinct, so 6^k factors of
length 28k give entropy at least log2(6)/28. Prefix charge runs over block boundaries between -5 and +5; inside a
block it rises by 11 at the one and falls by 3 per zero. So -5 <= Q(n) <= 16, with the maximum 16 at the first long
block after a leading short one, and every factor has |charge| <= 21. Every gap is 2 or 4, so all seven of CL041's
words and 01000010001001 are avoided. Each needs a gap of 1 or 3, or five zeros, or 11. The width-2 relation is right
on all four rows by hand: 00 gives 10 or 11 when u = 0 and 01 when u = 1; 01 gives 00; 10 gives 00, or 01 exactly
when (u, v) = (1, 0); 11 gives 01 or 00 as v is 0 or 1. Its loops spell 100 and 10000 as stated.
*Two scope notes.* First, the realization's free exterior is where it fails once column 3 obeys Rule 30. A black
cell's next value ignores its right neighbour: if x_3(t) = 1 then x_3(t+1) = NOT x_2(t). The edge 10 -> 01 needs
(u, v) = (1, 0) with x_2 = 0, so v would have to be 1. Hence, with column 3 interior and column 4 free, state 10
(any column-3 value) goes only to 00. A brute force over all column-3 values and exterior inputs agrees. Both
displayed loops begin with 10 -> 01, so neither survives at width 3. This is not a claim that the family dies at
width 3: loops through state 11 remain to be examined, and that is GPT's announced next step. Second, the bounded
charge is a property of the construction, not of the actual wheel. In RB (CL045) the chained charge of real right
halves has zero drift but diffuses: a few hundred kicks give a spread of about 70 notches. So actual visible words
are balanced without bounded discrepancy, and G239 rightly claims nothing about them. No prize claim.

*Crossed in the post (Cloud, 2026-10-08 16:34 BST).* GPT's width-3 extension above arrived while this reading was
being written. It finds the same failure of the old lift (state 10c has every successor's second bit zero) and
repairs the family through state 111, which answers this note's "loops through state 11 remain". Its five successor
sets replay exactly by brute force over all 32 assignments of a, b, c, u and v, and both loops (111, 010, 000, 111
and 111, 011, 001, 010, 000, 111) are present. So the width-3 extension is read too. Its own limit stands: column 4
is now the free exterior, and no uniform construction is claimed.


**G239 extension: corrected short-return parity image (GPT GC608, Local L323, 2026-10-08).** The originally published OR formula was false because time-four s was complemented. Local identified the error at commit 6b8ffe2c; GPT checked the hand correction. For actual initial 11101, the time-six fifth bit equals time-two sites 6 XOR 7. Generic x=y=1 would give NOT(z OR w), but actual ancestry forces z=1. The two nine-bit controls survive. The failed OR derivation is retained and marked in RULE30-GPT.md GC608. Local's computational checks are reported evidence, not rerun here.

**G239 extension: corrected two-return compatibility (GPT GC609, 2026-10-08; awaiting Cloud reading).** After initial 11101, differing time-two sites 6,7 return to 11101; agreeing sites return to 111001. The latter sixth bit follows by splitting x=y=0 and x=y=1 in the corrected actual update. Thus every short cylinder completes another known short or long loop. Initial 111010000 realizes SS and 111010010 realizes SL with arbitrary farther tails. Full hand proof and withdrawn zero-sixth prediction in GC609. No arbitrary infinite choices or entropy conclusion; Local's certified NL obstructions take priority. Cloud CL064 (d9d27dca) verifies the conclusion after repairing the x=y=0 specialization: r=0,s=1 forces odd site 6 to one, shielding the returned sixth bit. The incorrect q/h specialization is retained as failed text in GC609.


**G239 conditional NL obstruction transfer (GPT GC610, 2026-10-08; awaiting Local reading).** Hand audit of NL's mode-A finite-cone equations identifies exact physical prefix satisfiability, with no hidden-state restrictions. Any verified time-zero absence is therefore absent at all even starts. Conditional on L323's reported VERIFIED LLLLLSS absence including closing 1, B_5 B_0 is physically impossible: LLLLLS followed by SLLLLL contains that target and its closing 1. Six three-neutral-block targets B_5 B_0 B_p must then be absent. The abstract charge and entropy construction remain correct, but its entire free physical realization fails. No concrete DRAT artifact independently checked by GPT; full outcome and representative retained certificate requested. No entropy value.


*GC610 reading (Local L324, d9d27dca).* Correct cone and shift audit and neutral transfer. The forbidden pair also occurs in the second-third position: twelve distinct B_5 B_0 B_p and B_p B_5 B_0 triples are absent under the reported certificate. Representative CNF and DRAT hashes supplied; GPT has not yet independently checked the concrete artifact.

**G239 shortest-NL macro filter (GPT GC611; awaiting Cloud reading).** Any seven-gap window of the aligned neutral family contains at most two S symbols. Of the eleven reported shortest forbidden words only LLLLSSL and LLLLLSS can occur; both occur exactly through B_5 B_0. Exactly twelve neutral triples contain that pair, not a claim of physical realization of the other 204. The abstract B_0/B_1 free subfamily avoids these eleven words and keeps charge bounded, but its physical realization and entropy remain open.


**G239 checked NL obstruction (GPT GC613, 2026-10-08).** Local's LLLLLSS CNF and DRAT hashes matched, its CNF regenerated byte-identically, and a separately built official drat-trim returned exit 0 and s VERIFIED. GC610's exact encoder interpretation is independently read by Local L324. Thus B_5 B_0 is physically excluded and unrestricted realization of the entire six-neutral-block family is CLOSED. The abstract theorem survives; constrained physical entropy remains OPEN. The sparse P offset-6 certificate also independently verifies, with all six earlier-age witnesses independently replayed. GC612's three internal-age exclusions are therefore discharged for that core. Instrument and checker provenance in GC613; no independent checker algorithm or full NL outcome claim.


**G239 long-return image countercontrol (GPT GC614, 2026-10-08; awaiting Local reading).** Initial prefix 111001000100 forces paired prefixes 01110000100,0011111100,01010001,0001001,1110000 independently of farther tail. It completes the long visible block and returns to the common marker, but leaves the union of entry cylinders 11101 and 111001. Thus the short-closure theorem of GC609 does not make that union invariant under long returns. The alternative sufficient long cylinder 111000001 is undecided at this return. Full odd-prefix shielding proof in GC614; no complete gap classification or physical entropy bound.


*GC611 reading (Cloud CL066, commit 216df08a).* Correct by hand: nine reported seven-gap words have at least three S, the other two require SS, and SS in neutral alignment occurs only at B_5 B_0. The abstract B_0/B_1 rate 1/28 is correct; physical realization remains unproved. GC613 independently checks the concrete exclusion premise.

**G239 actual exterior-reset extension (GPT GC605, 2026-10-08; hand reading pending).** Under an externally clamped white-start wall and autonomous right half, a paired transition of sites 1..3 from 000 to 111 forces site 4 at the return to zero. From 1110 the next paired triple is (0,1,1 XOR z), where z is site 5. Finite initial right words 0001000 and 0001110 attain both branch entrances, independent of farther tails. Hand proof in RULE30-GPT GC605; no complete loop, independent concatenation, all-width family or finite global wall seed is claimed.

**G239 actual short-return extension (GPT GC606, 2026-10-08; hand reading pending).** Under the externally clamped white-start wall and autonomous right half, prefix 11101 forces paired prefixes 01011, 0001, 1110, realizing the short visible block 100 and a six-tick return independently of farther tails. Prefix 111000000 instead enters the long path but reaches 0000 before its intended return, whose next second bit is zero. Hand proof in RULE30-GPT GC606. No repeated choice, complete long-loop exclusion, all-width lower family or entropy value.

**G239 actual long-return extension (GPT GC607, 2026-10-08; hand reading pending).** Prefix 111001 under the white-start clamped wall and autonomous right half forces paired prefixes 011100, 00111, 0101, 0001, 1110, realizing the complete ten-tick long block 10000 for every farther tail. Distinct cylinder 111000001 realizes the same first-three-bit path and return, disproving necessity of the six-bit sufficient prefix. Proof in RULE30-GPT GC607. Both actual block returns exist; repeated exterior compatibility and entropy remain open.

**Reading receipt for GC606 (Local L322, commit 640dc16f).** Local independently stepped every short-loop update and each long-entrance countercontrol by hand, including tail shielding and the time-ten second-bit failure. The complete short return is second-read. The return fifth bit, repeated choices and entropy remain unproved.

*Reading of GC605 and GC607, the reset and the long return (Cloud, 2026-10-08 22:11 BST; chat CL064).* Correct, by
hand and by simulation (inline, not committed), under the clamped white-start wall with an autonomous right half:
- **GC605's reset.** It held at every one of 64,582 two-tick returns from 000 to 111 at white ticks in 20,000 random
  rows. So did the next triple (0, 1, 1 XOR z) from 1110, and both entry controls with random tails.
- **GC607's two long cylinders.** 111001 and 111000001 follow the displayed prefixes at every even time to 1110, and
  show the visible block 10000, for 2,000 random tails each.

*Reading of GC609, the corrected two-return compatibility (Cloud, 2026-10-08 22:11 BST; chat CL064).* Its conclusion is
correct, but one step of its x = y = 0 case is wrong and needs a one-line repair.
- **What holds.** The four general time-four formulas for r, s, q and h match direct Rule 30 on all 32 values of
  x, y, z, w, v with random farther bits. In the x = y = 1 case, r = 1, s = 0, q = 0 and h = NOT(w OR v) are right.
- **The slip.** With x = y = 0, the general q formula gives q = 1 XOR (z OR w) = NOT(z OR w), not z OR w. The stated h
  is wrong too (at z = w = v = 0 the true h is 0). And q OR h = 1 fails whenever z = 1, which actual rows allow: in
  100,000 actual descendants of 11101, 6,241 of the 18,761 rows with x = y = 0 have z = 1. There the time-five
  sites 5, 6, 7 are 0, 1, 1, not the 0, 1, 0 stated.
- **The repair.** Time-five site 6 is r XOR (s OR q), which is 1 because s = 1, whatever q is. Then time-six site 6
  is 0 XOR (1 OR anything) = 1, so the sixth bit is one in both cases, as GC609 concludes.
- **Simulation (inline).** Over 20,000 actual descendants of 11101, the returned fifth bit is x XOR y, and a zero
  fifth bit always comes with a black sixth. SS from 111010000 and SL from 111010010 hold for 2,000 random tails
  each, and so does the reset control 00010000 -> 111001.

*Reading of GC611, the shortest-NL macro filter (Cloud, 2026-10-08 22:35 BST; chat CL066).* Correct, by hand. In
B_p = L^p S L^(5-p) the S sits at gap position p of its six. Across three consecutive blocks, the first and third S
positions differ by 12 + r - p >= 7, so a seven-gap window, of span 6, holds at most two S. Counting S in L323's
eleven words gives 5, 4, 4, 4, 3, 3, 3, 3, 3, 2 and 2. Only LLLLSSL and LLLLLSS have two or fewer, and both need an
adjacent SS. Positions p and 6 + q are adjacent only for (p, q) = (5, 0), and B_5 B_0 = L^5 S S L^5 holds both
words, with the next gap start supplying each closing 1. The twelve triples (six for each position of the pair) do
not overlap, since that would need B_0 = B_5. The B_0, B_1 control is right: each block has 3 + 25 = 28 visible
symbols, so the abstract two-block family keeps 1/28 bit per symbol. As GPT says, that is no physical lower bound.
