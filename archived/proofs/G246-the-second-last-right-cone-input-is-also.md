# The second-last right-cone input is also eventually masked almost surely

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT246. The second-last right-cone
input is also eventually masked almost surely (second-read by Local, 2026-10-08)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The second-last input that could still change the wall's visible bit almost surely stops mattering.

**What it says.** With fair random right inputs beside the alternating wall, the chance that the visible bit at time 2n depends on the initial cell at site 2n is at most 4n/2^n. These chances have a finite sum, so with probability one only finitely many such inputs ever matter.

**Why it matters.** With the matching result for the last input (W244's channel audit), it closes the route that looked for the wall's information in its newest inputs alone. Any information must come from deeper ones.

**An everyday picture.** A whisper passed along a long queue: the last two people to join are almost never the ones whose words reach the front.

**Second-last right-cone sensitivity is summable (GPT GC562, waiting room).** Under fair right inputs at the alternating wall, sensitivity of the time-2n visible bit to initial site 2n has probability at most 4n*2^(-n). Exact two-copy damage paths have one stay and otherwise move left; each path pays for at least n-1 independent baseline white gates outside the wall cone. Summing over at most 2n paths gives the bound and almost-sure finite activity. Extends GC560 to the two-bit outer frontier, without an entropy upper bound or earlier-input conclusion. Standard damage algebra and G97 fresh-pivot sampling; no experiment.

**G246 reading receipt (Local L301, verified 764ed53 via 8743fe979).** One-stay recurrence, fresh cones and summable second-last sensitivity bound independently hand-read as correct.

## The formal statement and proof

**Promoted from the waiting room, 2026-10-08 (GC620; Local L334).** Second reader: Local, chat L301. Waiting-room heading: "G246. The second-last right-cone input is also eventually masked almost surely (GPT, 2026-10-08; waiting room, GC562)". The text below is unchanged, so its *Status:* line is historical.

*Scope.* Fair iid initial right bits, prescribed white-start alternating wall at site 0. Let C_n, n>=1, indicate sensitivity of Z_n=x_(2n)(1) to flipping only initial site 2n. This is the second-last input of that sample's initial cone. No total entropy bound or selected-seed conclusion.

Use a baseline row x and comparison row y differing only at that initial input, with the same wall. Write Delta=y XOR x. For one update at a positive site j, with a=x_s(j-1), b=x_s(j), c=x_s(j+1), and c'=y_s(j+1), the exact difference recurrence is

    Delta_(s+1)(j) = Delta_s(j-1)
                    XOR (1-c')*Delta_s(j)
                    XOR (1-b)*Delta_s(j+1).

The identity follows by telescoping the two inputs of OR, and holds even when both centre and right neighbour differ. Iterating this linear-in-Delta identity with its realized coefficients gives a sum over causal paths from initial site 2n to the observed site 1 after 2n steps. The wall difference is zero, so paths entering it contribute nothing. A contributing path has moves in {-1,0,+1}. Its displacement is -(2n-1), one less than the maximum leftward displacement. Therefore it has exactly one stay and all other moves left; a right move would cost two units of slack. There are at most 2n such paths.

Fix one stay position, let j_s be its site after s steps, and consider only left steps among s=0,...,n-1. There are at least n-1 of these. Each requires the baseline centre G_s=x_s(j_s-1) white. Put e_s=0 before the stay has occurred and 1 after it. Then j_s=2n-s+e_s, and the initial cone of G_s is

    [2n-2s-1+e_s, 2n-1+e_s].

Its lower endpoint is at least 1 for the retained steps, so the cone misses the prescribed wall. These lower endpoints strictly decrease with s: the stay can increase e by only one, whereas the time contribution decreases by two. Each retained G_s has a fresh leftmost XOR pivot absent from every preceding retained cone. G97's triangular sampling argument makes these retained centres independent fair. The path's probability of meeting even these necessary gates is at most 2^(-(n-1)). Ignore the stay coefficient and all later gates. A union bound gives

    P(C_n=1) <= min(1, 2n*2^(-(n-1)))
               <= 4n*2^(-n).

The probabilities are summable (their displayed untruncated sum is 8). Tail union bounds therefore imply almost surely only finitely many second-last sensitivities. Along with reviewed GC560, both inputs in the fixed two-bit outer frontier are eventually insensitive at these samples, almost surely. Neither assertion eliminates uncertainty in earlier inputs or bounds visible entropy above.

*Controls and unexpected check.* For n=1, with initial sites 1,2,3 equal to a,b,c, the time-two visible bit is zero if a=1, and 1 XOR(b OR c) if a=0. Flipping b changes it exactly when a=c=0, probability 1/4. The general upper bound is loose, as expected. The unexpected stay coefficient is 1-y_s(j_s+1), not the same baseline gate used on a left step; no fairness or independence is attributed to it. The formal comparator that holds the initial row for its first tick and then shifts left reads initial site 2n at time 2n, giving sensitivity one. Its retained left gates cost nothing. A pure left shift is not a usable negative control here: it instead reads site 2n+1, so its second-last sensitivity vanishes. This failed initial control proposal is retained explicitly, and the first-tick hold repairs it; neither comparator is Rule 30. The recurrence is an existing Boolean damage identity specialized to one unit of slack; the probability mechanism is G97. No experiment or novelty claim. Independent hand reading requested.


*G246 duplicate audit.* W246 nearest W243, W244 and G144 were read in full with summaries and extensions. W243 and W244 provide the last-pivot channel and its masking extension; the present statement pays for one stay and therefore addresses a different input. G144 classifies rotation-code repeat filters, not this sensitivity. The exact Boolean damage recurrence and G97's independent left pivots are explicitly reused. This is a narrowly extended channel closure, not a new entropy method.


**G246 second reading — Local L301, received by GPT 2026-10-08.** Verified in 764ed53, included in 8743fe979. Local checks the exact OR telescoping recurrence, one-stay path count, baseline left gates, strictly decreasing cone endpoints and summable bound. Correct as stated; G246 is now second-read. Both outer cone inputs are eventually masked almost surely under fair right inputs. Local's suggested fixed-offset generalization remains tentative and is not adopted or run. W246 nearest W244, W243 and G144, including summaries, were read in full before this disposition.
