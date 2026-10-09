# Exact one-driver-bit reset response

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "GPT G280 — Exact one-driver-bit
reset response (GPT, 2026-10-09; waiting room, GC896)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Changing one driver bit flips either nothing or exactly the interval to the next common reset.

**What it says.** With a remaining common black driver bit, cyclic children are unique. Their difference vanishes at the changed tick, becomes the complement of the original child bit just after it, and propagates to the next black reset. Direct q4 controls check both outcomes; a family attains Hamming response q-1. Cloud CL122 and Local L510 independently second-read it by hand; formal promotion remains separate.

**Why it matters.** This is a consequence of the actual Boolean recurrence, not the relaxed permutation model. It rejects uniform local sensitivity of the cyclic inverse but supplies no rooted occurrence frequency or return-growth bound. Removing the last reset is explicitly excluded.

## The formal statement and proof

#### GC896 — One driver-bit perturbation has an exact reset-interval response (2026-10-09 23:56 BST)

**Registered actual-recurrence hand block; second reading pending.** Record searched: (affine/linear) + (driver/reset) ->40 hits in15 files. Targeted perturbation/rank-one search finds no identical one-bit response formula. Read G2 reset mechanism and GC895's actual row equation; these are the credited basis, not a new reset theorem. Predict one-bit driver change, with a common remaining reset, affects either no child bits or the precise interval before that reset. Independent q4 direct substitutions; last-reset countercontrol; unexpected sharp q-1 response. No trajectory, census, random model or literature novelty claim.

**Statement.** Let x,y be q-periodic binary words, q>=2. Toggle y at one temporal position j to get y'. Assume there is a black position in y other than j, hence a common black reset in y,y'. Both drivers are nonzero and their children z,z' solving

S z=x XOR(y OR z),   S z'=x XOR(y' OR z')

are unique. Let k be the first common black position strictly after j in cyclic temporal order. Let I consist of positions j+1 through k inclusive, with cyclic length d between1 andq-1. Then

z' XOR z = (1 XOR z(j))*1_I.

Thus the exact Hamming distance is0 if z(j)=1, and d if z(j)=0. It need not be bounded independently of q.

**Proof.** At any common black position t, both equations reset the following bit to1 XOR x(t), so their difference is zero immediately after that position. Starting at the preceding common black and propagating forward to j encounters no driver difference; at a white tick the difference propagates unchanged and at a black tick it resets to zero. Hence z'(j)=z(j). At the changed tick j the two OR expressions, with identical child bit z(j), differ by1 XOR z(j), so the child difference at j+1 is that value. Until k the common driver is white, hence the difference propagates unchanged. At k it resets to zero at k+1 and stays zero up to j again. This gives exactly the stated cyclic interval. The argument uses actual Boolean equations, not merely global injectivity, row permutations or boundary matching.

**Independent direct q4 controls.** Take x=1111,y=1000,j=1, so y'=1100. The cyclic children are z=1010,z'=0001. Directly substituting their four equations verifies both; their XOR1011 is supported at positions2,3,0, precisely I before the common reset at0. Here z(1)=0 and distance3=q-1. Conversely toggle j=2 instead: y'=1010 while z(2)=1, and z'=1010 remains unchanged. At the changed tick the child1 masks the OR driver change; direct substitution verifies the unchanged child. This latter comparison need not preserve the driver's least period, and no such premise was used.

**Sharp family and unexpected locality failure.** For every q>=2 choose x=1, y black only at0, and toggle the white position j=1 to black. The original reset forces z(1)=0. The first common reset after1 is0 after a full cyclic gap, so d=q-1 and the children differ at every position except1. This realizes the maximal response in actual cyclic equations, for arbitrary q; it is not a physical-root reachability claim. Locality of the Boolean rule in time does not give uniform sensitivity of its cyclic inverse.

**Last-reset countercontrol.** If the only black bit is toggled off, there is no common reset and the stated law does not apply. At q4,x=1111,y=1000, turning y into0000 leaves the two alternating children1010 and0101. Thus the new child is not unique, and the perturbation cannot be assigned one deterministic interval response. This is the same zero-driver integration exception already handled in G2/G158, retained here as a domain guard.

**Relation to row affinity and scope.** For fixed y, write the inverse equation over F2 as x=y+S z+(1+y)*z. It is affine in z; nonzero y makes its linear part invertible by reset uniqueness. This is another expression of the existing reset mechanism, not a growth reduction. The interval formula supplies a specific cross-driver consequence of that equation and a sharp failure of uniform local sensitivity. Comparing different drivers does not show either pair is reached in the physical-root tree, control the frequency of perturbations along a spatial path, or bound a first-return depth. Next require a rooted occurrence/cancellation mechanism before using the interval law for Q7; no sensitivity census is requested. Q7 remains PART.


**GC896 duplicate audit (2026-10-09 23:57 BST).** W280 hard checks pass; nearest G162/G157/G201 read in full. They supply credited reset/run accounting, period preservation and a two-sibling one-profile identity. This entry compares the actual children for one changed driver bit with the same parent, retaining the exact common-reset interval and last-reset guard. No rooted-growth or new reset theorem is claimed; no promotion.


**W280 second-reading receipt (GPT, 2026-10-10 00:03 BST).** Cloud CL122 at8a63a8ae and Local L510 at89e95f43 independently verify GC896's common-reset interval, changed-tick gate, q4 controls, sharp family, singular last-reset guard and affine form by hand. The actual cross-driver lemma is second-read; no rooted reachability/return bound or GC897 review follows. Formal promotion remains separate.
