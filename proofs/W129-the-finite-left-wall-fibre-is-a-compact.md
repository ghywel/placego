# The finite-left wall fibre is a compact constraint class at each fixed radius

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G129. The finite-left wall
fibre is a compact constraint class at each fixed radius (2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Finite left support becomes an explicit constraint on the sideways limit.

**What it says.** Fix a wall and a maximum initial left radius. The admissible pairs form a compact class: every forced initial cell farther left must be zero. If this class is empty, some finite rectangle already witnesses the failure. Each left seed permits at most one complete visible itinerary.

**Why it matters.** This connects unrestricted spacetime extension to the boundary condition the prize needs. Growing support cannot be passed through compactness as though the radius were fixed. Neither the compactness statement nor the itinerary count proves that the alternating-wall classes are empty or that their time factors have zero entropy.

**An everyday picture.** Matching every finite view can yield a whole picture, but a picture assembled from ever larger canvases need not fit one finite canvas.

## The formal statement and proof

**Status and target.** Symbolic bridge from G128 to the finite-left boundary problem; independent review pending. No experiment or novelty claim for compactness. Existing record: G27.2 excludes periodic companions, G53 identifies the wall-visible bits, and G128 characterizes unrestricted spacetime pairs. The target is an exact finite-left constraint that does not assume companion periodicity. The counterfactual is that a compact limit of witnesses with growing support must retain finite support. One unexpected check below separates counting full itineraries from counting their time factors.

Use one-sided time t>=0. Let X+ be all pairs of binary future tracks and H(a,b)=(S a XOR (a OR b),a), with S advancing time. Let Lambda+ be the intersection of H^n(X+) over n>=0. The same strip-compactness proof as G128 identifies Lambda+ exactly with adjacent-column pairs in full-space, forward-time Rule 30 diagrams: right extensions of every finite width have a coherent compact limit, and all left columns are uniquely given by H iterates. This does not require any periodicity or a past before time zero.

Fix any prescribed wall tau and integer L>=0. Define

    B(L,tau) = { (a,b) in Lambda+ : a=tau,
                 first_track(H^d(a,b))(0)=0 for every d>L }.

**Exact boundary interpretation.** B(L,tau) consists precisely of the wall/right-neighbor pairs of full forward diagrams whose initial left row is zero at all sites i<-L. There is no bound on the initial right row. In one direction, H^d recovers column -d, so the displayed conditions are its initial zero tail. In the other direction, Lambda+ supplies a full forward diagram with this pair; every possible extension has the same forced left columns and therefore the specified initial zero tail. This is a left-support condition, not a finite global seed condition.

For fixed L, B(L,tau) is compact: Lambda+ is an intersection of nested compact images; fixing a track is closed; and each displayed initial-cell equation is a closed cylinder condition depending on only finitely many input cells. Their countable intersection is closed. All finite-left pairs form the union of these classes over L. That union cannot be treated as one fixed-radius compact class merely because each member is compact.

**Finite-box alternative.** B(L,tau) is empty if and only if some finite rectangle already forbids a forward diagram with that wall and that left radius. Specifically, take sites -N through N and times 0 through N, fix the wall samples, fix initial cells -N through -L-1 to zero when N>L, and enforce every Rule 30 equation whose three input sites and output lie in the rectangle. Leave the right initial row unrestricted. If every N has an assignment, extend each assignment arbitrarily outside its rectangle and use compactness. Every fixed wall sample, local equation and initial left-zero condition is eventually enforced, so the limit is a full forward diagram in the class. The converse follows by restriction. Thus a failure at fixed L has a finite Boolean certificate in principle; no uniform certificate size or effective search bound is supplied. Certificates for a few radii do not prove emptiness for every radius.

**Visible itineraries have a finite cardinality bound at fixed L.** Observe b only at white wall times. There are at most 2^L such complete visible itineraries in B(L,tau). Choose the L initial left bits. With tau imposed as a boundary, forward evolution of sites i<0 is deterministic. Write its nearest-left trace as ell(t). At a white time, the wall equation forces b(t)=tau(t+1) XOR ell(t). At a black time, it instead requires ell(t)=1-tau(t+1), independently of b(t); failure rejects that left seed. Thus each left seed permits at most one whole visible itinerary, even when hidden black-phase bits or full right extensions are not unique. This is a boundary-determinism count, not an entropy or finite-state closure theorem.

**Counterfactual and unexpected check.** Initial rows with ones at -L,...,-1 and zeros elsewhere converge, as L increases, to an infinite left black tail. Their ordinary forward Rule 30 diagrams consequently have a compact limit with infinite initial left support. This general support guard does not claim those rows share one prescribed alternating wall; it shows why varying-radius compactness alone does not retain the required boundary condition. Separately, a single sequence formed by concatenating every finite binary word has one prefix of each length but all 2^n time factors of length n. Therefore the 2^L whole-itinerary bound gives no zero factor-entropy conclusion. This is the identified unexpected check, reused from G64's distinction; it is not a Rule 30 realization claim.

**Remaining bridge.** To exclude a finite seed realizing an alternating wall, it would suffice to prove B(L,tau) empty for every L; that stronger finite-left assertion is not proved here. If a class is nonempty, full finite-right support remains an additional obligation. The next invariant must address an aperiodic companion inside these explicit classes, rather than unrestricted Lambda+ or a periodic closure. No new channel census is requested.
