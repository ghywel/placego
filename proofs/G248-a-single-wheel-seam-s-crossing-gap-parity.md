# A single wheel seam's crossing-gap parity fixes the half-turn discrepancy

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT248. A single wheel seam's
crossing-gap parity fixes the half-turn discrepancy (second-read by Cloud, 2026-10-08)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

The gap crossing a single wheel splice determines whether its two kick readings disagree by half a turn.

**What it says.** If the old and new visible words are pure wheel phases meeting at one cut, an even number of zeros between their adjoining black cells makes the phase and charge readings agree modulo 28. An odd number makes them differ by 14.

**Why it matters.** Crossing gaps of two or four zeros eliminate this discrepancy within the single-splice domain. A general transient can alter several gaps, and an empirical instant event still needs to be shown to fit the domain. No integer direction or prize theorem follows.

**An everyday picture.** Two rulers can agree on a circular scale while their full readings differ by a complete turn. Here an odd gap additionally moves one reading halfway around the circle.

**GC582 extension of W248 (awaiting reading).** The same parity test applies to RB's adjacent finite locks, including an odd physical cut. For a general pair of locks, count complete zero gaps between black samples inside the locks: phase and charge differ by 14 exactly when an odd number of these gaps have odd length. Two odd gaps cancel. Endpoint choices within a pure lock do not change this parity; no integer direction, actual gap restriction or replay follows.

## The formal statement and proof

**Promoted from the waiting room, 2026-10-08 (GC620; Local L334).** Second reader: Cloud, chat CL056. Waiting-room heading: "G248. A single wheel seam's crossing-gap parity fixes the half-turn discrepancy (GPT, 2026-10-08; waiting room, GC581)". The text below is unchanged, so its *Status:* line is historical.

*Where:* RULE30-GPT.md, GC581. *Bears on:* kicked-wheel lifted-charge interpretation, not a prize conclusion. *Status:* hand proof awaiting independent reading. Uses Cloud CL053's congruence, GC576's endpoint convention and IS1's reviewed literal wheel; no new prior-art or event-realizability claim.

**Statement and conventions.** Let V be the 28 even samples of U = 00010011010001001101000100110100010011010001001101001101. Its six black samples have cyclic zero gaps 2 or 4. Extend the prefix count M to all integers by M(0)=0 and M(a+1)-M(a)=V(a); then M(a+28)=M(a)+6. Set Phi(a)=14 M(a)-3a, a 28-periodic function. For integer phases i,j, splice V(i+n) at n<0 to V(j+n) at n>=0. With continuous running charge Q at the cut, the new minus old wheel level is L=Phi(i)-Phi(j). The physical phases d=-2i and d'=-2j give phase kick K=-17(i-j) modulo 28. Let the last old black be at n=-l, l>=1, and the first new black at n=r, r>=0; write R=l+r-1 for the crossing zero gap. Then

    L-K = 14 R modulo 28.

Thus an even crossing gap gives agreement modulo 28; an odd crossing gap gives precisely a half-turn discrepancy. In particular IS1's crossing-gap domain {2,4} has agreement. This is conditional on a single pure-wheel splice; it neither proves that every empirical instant event has this form nor controls a transient with several altered gaps.

**Proof.** Consecutive black indices of V differ by 3 or 5. If b and b' are such consecutive indices, M(b')-M(b)=1, so M(b')+b' and M(b)+b have the same parity. The wrap also preserves parity because M increases by 6 and the index by 28. Hence M(b)+b has one constant parity c at every black index on the infinite periodic extension.

Put p=i-l and h=j+r. Both are black indices. There is exactly one black sample in [p,i), namely p, and none in [j,h), so M(i)=M(p)+1 and M(j)=M(h). Therefore M(i)+i equals c+1+l modulo 2, whereas M(j)+j equals c-r modulo 2. Their difference has parity 1+l+r, the same as R. On the other hand direct subtraction gives L-K=14*(M(i)-M(j)+i-j) modulo 28. Combining the two parities proves the claim.

**Independent controls and identified unexpected boundary check.** IS1's retained phases i=0,j=22 have R=2 and L=10; K=-17*(-22)=374=10 modulo 28. The broader-domain phases i=0,j=23 have R=1 and L=13, while K=391=27 modulo 28, giving difference 14 as predicted. Unexpected check: r may be zero, so the new phase can start with black; the proof uses the empty interval [j,h), not an assumed positive new-side wait. The odd control has exactly this boundary. No computation ran in this block; these are hand checks of previously recorded witnesses. The counterfactual that agreement holds for every formal seam fails on the odd witness. Agreement modulo 28 does not choose an integer lift or a nearest signed root; adding 28 is still invisible.

*G248 duplicate audit.* W248's nearest older entries 26, G57 and 20 were read in full, including their second-reader notes and summaries. Entry 26 restricts phase-kick alphabets through hidden-column compatibility; entry 20 excludes the never-kicked wheel's finite left half; G57 identifies moment drift on prime rings. None supplies this visible seam parity identity. CL053's modular argument and GC576's exact correction are explicitly reused. This is an elementary corollary of the reviewed wheel gaps, not a new general phase theory.

*G248 final neighbour refresh.* The final advisory also names G56; its full proof, reading note and summary were read. Its prime-ring moment coordinate is not a crossing-gap parity law. All final three neighbours have now been read.


**G248 finite-lock and gap-chain extension (GPT, 2026-10-08; GC582, awaiting reading).** The infinite pure halves are unnecessary for an adjacent RB lock pair. RD stores half-open locks [a,s) and [a',s'), each of length at least 56 physical steps; an instant pair has a'=s. Let 2m be the first even time at or after s. The visible cut phases are i=m-d/2 and j=m-d'/2. The old lock contains its last old visible black before this cut, and the new lock contains its first new visible black after it: each wheel gap has at most four zeros, and the locks supply at least 28 visible samples. If s is odd, only an odd, uncharged observation lies between s and 2m. Thus transporting each lock level to this cut changes neither level, even though 2m lies just beyond the old physical interval. G248's local proof therefore gives L-K=14 R modulo 28 for any such adjacent pair. No infinite old history, settled wheel or 133-step hypothesis is needed for this parity statement. Even crossing-gap admissibility remains a separate premise.

More generally, take any two RB locks, adjacent or separated, and choose visible black samples at indices A in the old lock and B>A in the new lock. Both phases d,d' are even. Put i=A-d/2 and j=B-d'/2 and let N count actual black samples in [A,B). Let R_1,...,R_N be the successive complete zero gaps from the black at A through the black at B. Moving the level endpoint to a black within its own lock preserves that level. Directly from Q and Phi,

    L-K = 14*(N-M(j)+M(i)+(d'-d)/2) modulo 28.

Since both wheel indices i,j are black, G248's constant parity gives M(j)-M(i)+j-i=0 modulo 2. Also j-i=B-A-(d'-d)/2. The displayed coefficient therefore has parity N+B-A. But B-A=sum_h(R_h+1), so N+B-A has parity sum_h R_h. Consequently the general identity is

    L-K = 14*sum_h R_h modulo 28.

The two readings differ by a half turn exactly when the number of odd complete zero gaps between those black endpoints is odd. Adding further pure-wheel gaps to either endpoint changes the sum by an even number, so the test does not depend on which black samples inside the locks were chosen. This is an elementary gap-count corollary of CL053 and G248, not a new dynamical admissibility result or a claim that all transients use the wheel alphabet.

**Independent controls and unexpected cut check.** RB's recorded exceptional gaps 4,1,4,4 have odd sum 13, predicting a discrepancy 14; its recorded L=4 and K=-10 indeed differ by 14. This is a hand interpretation of received evidence, not a replay. A chain with only gaps 2 and 4 has even sum and therefore agrees modulo 28 regardless of its length or level sign. Conversely two odd gaps cancel in this parity test: the counterfactual that the presence of any odd gap alone forces discrepancy fails algebraically. No actual two-odd-gap transient is asserted. The identified unexpected check is the odd physical cut above: an uncharged observation must not be treated as a new visible bit. Integer lifts differing by 28 and the observed forward-only transient spectrum remain uncontrolled.

*GC582 duplicate check.* The advisory neighbours and their summaries were read, with the prior full extension readings retained. The Rule 210 checkerboard result concerns spatial support; the moment calculation concerns prime-ring drift; the sensitivity estimate concerns random initial inputs. None is this complete-gap test. The direct sources are credited above.





*Reading of G248 and its GC582 extension (Cloud, 2026-10-08 20:57 BST; chat CL056).* Correct, by hand and by replay.
G248: direct subtraction with Phi = 14 M - 3a and K = -17 (i - j) gives L - K = 14 (M(i) - M(j) + i - j) mod 28.
Consecutive black indices of V differ by 3 or 5 while M rises by 1, so M(b) + b has one parity c on all black
indices, across the wrap too (M + 6, index + 28). With p = i - l and h = j + r, M(i) = M(p) + 1 and M(j) = M(h), so
(M(i) + i) - (M(j) + j) has parity 1 + l + r, which is R's. The r = 0 boundary uses only the empty interval [j, h),
as stated. GC582: on visible samples Q(B) - Q(A) = 14 N - 3 (B - A), which gives the displayed
L - K = 14 (N - M(j) + M(i) + (d' - d)/2). The constant parity and j - i = B - A - (d' - d)/2 reduce the coefficient
to N + B - A, and B - A = sum (R_h + 1) makes that sum R_h. Pure wheel gaps are 2 or 4, so the endpoint choice cannot
change the parity. Replay (`rule30_cloud_review_g248.py`): G248 holds on all 784 formal splices. GC582 holds at all
139,972 consecutive RB lock pairs of seed 5601 and 71,016 of seed 4256, with nearest and with random endpoints. The
one odd pair is RB's trial 133 at t = 71. Between its nearest blacks the only complete gap is the 1-gap; GC582's
4, 1, 4, 4 adds wheel gaps either side (12, even). Its cut s = 71 is odd, the boundary GC582 names. Scope as GPT
states it: a parity statement mod 28, with no gap admissibility and no integer lift. Every consecutive lock pair in
these runs is chained, so the separated-lock case is checked by hand only.
