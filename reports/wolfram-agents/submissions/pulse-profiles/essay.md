---
Template: ComputationalEssay
Name: Periodic temporal profiles of rule 30: pulse holes, source weights and rooted returns
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-29
Description: Exact identities and a finite-state return theorem for periodic profiles along rule 30 left diagonals, proved in core Lean
Abstract: We study Boolean temporal profiles related by the rule 30 left-diagonal recurrence C(t+1) = A(t) XOR (B(t) OR C(t)). `Rule30Submission.pulse_source_weight` shows that a one-bit pulse in B makes the cyclic weight of its recovered source A equal to twice the rising-edge count of C, with an explicit correction of minus one, zero or one. `Rule30Submission.pulse_child_holes` shows that a pulse followed by a profile whose first positive black phase is L forces a child white exactly at phases 1 through L. For q-periodic profiles with q at least 4, `Rule30Submission.leftWindow_pulse_bound` identifies the resulting three first-black delays and bounds their doubled maximum contiguous-interval excess over slope 5/2 by 2q-5 + max(0,2L-5), attained at the phase just after the pulse. Separately, `Rule30Submission.rooted_chain_returns_bounded` proves that any infinite chain of q-periodic child triples starting with a white profile contains another white profile at an index from 1 through 2^(2q); the proof counts finite two-profile codes and recovers predecessors from a repeated pair. Reset existence and uniqueness (`Rule30Submission.child_exists`, `Rule30Submission.child_unique`), and explicit connections to actual rule 30 evolution after a common onset, are also proved. These are conditional profile statements. They neither establish finite-seed ancestry for arbitrary profiles nor decide eventual periodicity of the single-seed centre column.
Keywords: [rule 30, temporal profiles, left diagonals, periodic words, reset, pulse, finite-state return, Lean 4, partial result]
Sources: ["[Rule30PrizeKit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[Source record, PROOFS entries 24, 25 and 39](https://github.com/ghywel/placego/blob/main/PROOFS.md)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)"]
---

## The question

A repeating profile can be complicated internally while still obeying short exact rules when it is placed beside
another profile. Which properties can we recover without listing all the profiles of a given period?

We study three neighbouring **left diagonals**, rather than three vertical columns. Write x_t(i) for rule 30
from any initial configuration x_0 on the integer line, with black equal to 1. Put

    L_j(t) = x_t(j-t).

The ordinary update gives

    L_(j+2)(t+1) = L_j(t) XOR (L_(j+1)(t) OR L_(j+2)(t)).

This recurrence is known kit machinery (`Rule30Diagonals.D_step` for the single seed). We use its arbitrary-start
form, `leftDiag_step`, and call the relation between three profiles Child(A,B,C). A profile is q-periodic when
its values repeat every q time steps; q is a common period and need not be the least period.

The first group of results follows a pulse through this recurrence. The second asks whether a chain of such
periodic profiles can start white and avoid white for ever. Both use the same source-recovery identity.

## Source recovery and the weight of a pulse

Given B and C, the source is uniquely determined:

    A(t) = C(t+1) XOR (B(t) OR C(t)).

This is Boolean cancellation, not a new reversibility theorem for a whole rule 30 configuration. It works on any
indexed carrier with a specified successor (`child_parent_recover`, `child_parent_unique`).

Suppose B is black at only one phase s modulo q. Away from that phase, A is the transition profile
E(t) = C(t+1) XOR C(t). At phase s, a black C(s) makes no difference; a white C(s) toggles precisely that bit.
If r is the cyclic number of white-to-black transitions, then E has weight 2r. Consequently:

| C(s) | C(s+1) | Source weight |
|---|---|---|
| black | either | 2r |
| white | white | 2r+1 |
| white | black | 2r-1 |

`pulse_source_weight` proves the identity as a finite sum with a closing seam C(q)=C(0).
Its three corollaries give the displayed cases. Either constant word has r=0: an all-white C has source weight1,
and an all-black C has source weight0. Thus there is no hidden convention assigning a constant black word one
rising edge. In particular, source weight greater than3 requires at least two rising edges
(`heavy_source_two_runs`).

The sum identity needs only the closing seam, not full periodicity. Its actual-diagonal instantiation
`leftWindow_source_weight` assumes a periodic C and a pulse B on the shifted window, and recovers the weight of
A without assuming that A itself is periodic.

## A pulse makes an exact white interval

Normalize the pulse phase to0. Let C first be black after that phase at L, where 1 <= L < q. The value C(0) is
unrestricted. Suppose D is periodic and Child(pulse,C,D) holds. Then, within one period,

    D(t) = 0 exactly for 1 <= t <= L,
    D(t) = 1 at phase0 and at phases L+1 through q-1.

Why? Away from the pulse, the recurrence is D(t+1)=C(t) OR D(t). The black C(L) forces D(L+1)=1, and that value
persists to the closing seam, hence D(0)=1. At the pulse, XOR with1 resets D(1)=0. The zero values of C before L
keep D white through L; C(L) then turns it black. The proof includes the endpoint L=q-1
(`pulse_child_holes`).

For example, read these words in phase order0,...,7:

    pulse  10000000
    C      00000001
    D      10000000

Here q=8 and L=7: the child is white for all seven nonzero phases. This is a cyclic-profile example; we are not
asserting that these words occur as a chosen triple in the single-seed picture.

## First-black delays and the interval that costs most

For an arrival T, define the delay as **one plus** the least wait to a black cell. The extra1 accounts for the
next step after that black event. For arrival representatives 1 <= T <= q, the successive delays through the
pulse, C and D are

    (k,L,1), where k=q-T+1.

The pulse is first black at q; the next arrival is q+1. Then C is first black after L-1 waits, and D is already
black at the following arrival q+L+1. `actual_pulse_delays` proves both first-black minimality and these arrival
indices. Thus the delay tuple is tied to profile events, rather than postulated as arithmetic data.

Define the doubled excess of an interval of r consecutive delays to be twice their sum minus5r. Include the
empty interval, of excess0. There are six nonempty contiguous intervals in a three-term tuple. For (k,L,1), their
maximum reduces to

    max(0, 2k-5, 2k+2L-10, 2L-5).

It is nondecreasing in k. For q>=4, its maximum over arrival phases occurs at T=1, where k=q, and equals

    2q-5 + max(0,2L-5).

`actual_pulse_window_bound` connects this bound to the actual first-black events; `pulse_window_attained`
proves equality at that arrival phase. All halves have been cleared: the undoubled excess is half the display.
For q=8,L=7 the maximum is20, or10 before doubling. At k=1 the doubled maximum is9, while the whole-three-term
excess is only3. A cheap last delay therefore cannot cancel an expensive earlier interval.

This is a local three-profile budget. It does not count how often such windows occur or bound an entire settling
history. A pulse at another phase is handled in the exposition by shifting the time origin; the retained Lean
window statements explicitly normalize the pulse to phase0.

## A white start cannot be avoided indefinitely at fixed period

Now let w_0,w_1,... be an infinite chain of q-periodic profiles, with q>0, w_0 entirely white, and
Child(w_k,w_(k+1),w_(k+2)) for every k. Then

    some w_k is entirely white, with 1 <= k <= 2^(2q).

This is `rooted_chain_returns_bounded`. The word “rooted” here means the specified white starting profile,
not the physical single black seed. The conclusion is another white profile; it need not be a return to the
initial pair of profiles.

The proof codes each pair (w_k,w_(k+1)) by its first q bits from each word, giving a Boolean list of length2q.
There are 2^(2q) possible codes. The kit's finite pigeonhole theorem produces equal codes at i<j<=2^(2q).
Periodicity makes the full profile pairs equal. Source recovery then takes that equality one step backwards;
repeating it i times gives w_0=w_(j-i). Since w_0 is white and 1<=j-i<=2^(2q), the result follows.

Only finite codes are counted. The infinite type of all functions from natural numbers to Booleans is never
called finite. The displayed bound is deliberately coarse finite-state counting, not an asymptotic improvement.
The qualitative `rooted_chain_returns` is an immediate corollary.

Why can a nonwhite driver be continued? If B(t0)=1, the recurrence resets C(t0+1) to NOT A(t0), independent of
C(t0). Forward propagation fixes every later value; periodicity determines every earlier phase. An explicit
run from that reset closes after q steps when A and B are q-periodic. These are `child_unique`, `run_periodic`
and `child_exists`. The return theorem itself has an infinite-chain hypothesis; it does not construct an
infinite chain or promise a unique continuation through a white driver. Thus the unique-child walk, continued whenever its driver is nonwhite,
cannot avoid white for ever. The bound above is stated for the formal theorem's infinite-chain hypothesis.

## Actual evolution and the scope of the result

The module uses the kit's `Rule30Realization.evol`. Its `leftWindow x j T0 t` is L_j(T0+t), so a common onset T0
is explicit. `periodic_after_onset` converts an eventual-tail hypothesis into periodicity of this shifted
profile. `leftWindow_child` proves the recurrence after that shift, and `leftWindow_source_weight` and
`leftWindow_pulse_bound` instantiate the pulse identities on actual diagonals.

The existence of an arbitrary periodic Child triple does not certify its ancestry from a finite seed. Nor is a
single onset for an infinite collection of diagonals supplied merely by saying that each one eventually settles.
The rooted-chain theorem assumes a common period for the whole chain. None of these results proves that the
single-seed centre column is eventually periodic or nonperiodic, or gives a global bound on transient growth.

The useful contribution is exact reusable information: which one-bit change controls source weight, which
white interval a pulse forces, how its local first-black costs depend on phase, and why backward source recovery
forces a white return in a fixed-period chain.

## Relation to earlier work

The Rule30PrizeKit's diagonal recurrence and finite pigeonhole theorem are used directly. The general idea of a
reset synchronizing an automaton is established background; see Ananichev, Gusev and Volkov, *Slowly synchronizing
automata and digraphs* (2010), [section1](https://arxiv.org/html/1005.0129v1). That reference is background for the
reset concept, not a claimed source of the exact rule 30 weight, hole or budget formulas.

The source record is PROOFS24/25/39, with earlier independent carrying reads and the current mutual reads of the
assembled module. The delivery specification records the current-kit and portal comparisons. A negative search
is not a claim of exhaustive literature novelty.

## Assembly and validation note — remove before publication

This is GPT's statement/exposition draft for Local's independent read. Local is the sole notebook, PR and portal
posting owner. At assembly, insert the complete retained module into the LeanLink proof cell using the current
kit workflow; print the nine agreed headline statements, run the official checker, retain outputs and distinguish
compilation, checker replay, receipt, Lean Verified and Human Verified. The example and formulas above are
explanatory; no census or new substantial computation is requested. Do not upload this prose draft as though it
already contained executed LeanLink cells.
