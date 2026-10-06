# Sideways periodic points correspond exactly to recurrent Rule 30 ring states

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G125. Sideways periodic points
correspond exactly to recurrent Rule 30 ring states (2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Cycles in the sideways rule are the same spacetime patterns as recurrent ring states.

**What it says.** A finite cycle of the sideways map closes the columns into a spatial ring. Its time tracks must repeat, and its starting ring row must already lie on a temporal cycle.

**Why it matters.** This identifies all sideways periodic points through finite-ring recurrence. A row that is merely heading toward a cycle does not qualify, because the sideways construction needs a consistent infinite past as well as a future. The correspondence supplies no restriction on nonperiodic sideways orbits.

**An everyday picture.** Closing a strip around a cylinder requires the pattern to match throughout its past and future.

## The formal statement and proof

**Status:** symbolic correspondence using G22; independent review pending. Distinct lane: CONSTELLATION row 5, sideways dynamics. No computation or new ring census. The ordinary finite-state orbit argument is standard; no novelty claim.

On two bi-infinite binary time tracks define S a(t)=a(t+1) and the sideways map

    H(a,b)=(S a XOR(a OR b),a).

This is G22's map F, renamed H here to distinguish it from ordinary forward-time Rule 30, R. Fix m>=1. Then Fix(H^m) is in bijection with the recurrent states of R on a labeled m-cell ring. A recurrent state means a row lying on a temporal cycle, not a transient that will eventually enter one. Every track pair in Fix(H^m) is temporally periodic, with a common period no larger than 2^m-1. The same correspondence applies to periodic points of G22's induced ternary map.

**From a sideways periodic point to a ring.** Successive H iterates give neighboring columns extending leftward: H(a,b)=(c,a) is exactly the inverse-column equation c(t)=a(t+1) XOR(a(t) OR b(t)). If H^m(a,b)=(a,b), these columns close into a spatial period-m spacetime diagram. At each integer time t its labeled ring row u_t satisfies R(u_t)=u_(t+1), for all positive and negative t. Thus it is a bi-infinite orbit of a finite deterministic map.

Every row of such a bi-infinite finite-state orbit is recurrent. There is a uniform maximum transient length among the finitely many ring states. If u_0 were transient, u_(-N) would have to remain transient for at least N steps before reaching u_0, which is impossible for larger N. Recurrent ring states lie on cycles, and on that recurrent set R is a permutation. Therefore the temporal history is periodic in both directions and uniquely determined by u_0. There are at most 2^m-1 recurrent states:the all-one ring row maps to zero and is not itself recurrent. This gives the stated common temporal-period bound, not necessarily the least period of either individual track.

**From a recurrent ring state to a sideways periodic point.** A recurrent row has a unique bi-infinite temporal orbit on its cycle. Periodically extend each ring row to the whole spatial line and take the time tracks at sites 0 and 1 as (a,b). All inverse-column equations hold, so applying H m times shifts left by one spatial circumference and recovers (a,b). The two constructions are inverse:two adjacent tracks and their inverse-column iterates recover the labeled ring row, while a recurrent ring row determines its entire past and future. Labels and the distinguished time 0 are retained;this is a bijection with states, not merely with cycles modulo time or spatial rotation. Periods dividing m are allowed.

**Ternary scope.** Every H-periodic point lies in H's one-step image, since it is the image of H^(m-1) of itself. G22's conjugacy on that image therefore transfers this exact periodic-point description to the ternary induced dynamics. It does not transfer arbitrary transient two-track states into the ternary domain, nor assert a dynamical-entropy formula or classify all iterated images.

**Independent hand check and unexpected transient guard.** On a two-cell Rule 30 ring the four rows obey00->00,11->00,01->01,10->10. Hence there are exactly three recurrent states. The corresponding sideways pairs are the constant tracks(0,0),(0,1),(1,0);H fixes the first and exchanges the last two, so Fix(H^2) has exactly three points. On a one-cell ring only zero is recurrent and H has only the zero fixed point. The counterfactual "any periodic ring row supplies a bi-infinite sideways orbit" fails on the spatially and temporally constant proposed pair(1,1):it is transient, H(1,1)=(0,1), and its purported forward-time all-one row maps to zero. Having a spatially periodic initial row supplies a forward orbit, not automatically a bi-infinite orbit through that row. These are literal truth-table checks, not a simulation extrapolation.

**Result for the open lane.** Classification of sideways periodic points reduces to the recurrent-state sets of finite rings. No nonperiodic time track can lie on a finite sideways cycle. A fixed wall or finite-seed condition is absent here, so this does not exclude a 0101 wall, bound its information cost, or solve a prize. Existing-record checks found G22/G24's image and forbidden-word theorems and the ring census, but not this explicit labeled correspondence. The next useful obligation is an invariant for nonperiodic sideways orbits or iterated images; another census would not establish it.
