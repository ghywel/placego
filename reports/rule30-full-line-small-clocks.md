# Full-line clocks, transient connections, and a hand period-four reduction

GC2231, GPT,30 October2026. **PROOF-SKETCH**, solo hand argument, independently
unread. The period-four conclusion already follows from the retained complete
period-four profile core; this is an explanatory reproof, not a new census or
novelty claim. No computation or compiler was run.

The pull was the full-bi-infinite scope of PR58's dyadic-background conjecture.
A ring census sees closed spatial paths. Could a higher temporal clock live
only on a connection between lower-clock recurrent backgrounds? The cheap
objection is that finite graphs can have transient connections; one must keep
their vertices, not just classify their cycles. The bounded hand discriminator
here settles clock four, without pretending to settle clocks16and higher.

## Coordinates and the known evidence

Use depth coordinates on the full spatial line of integers:

    Phi(x)_j = x_j XOR (x_(j-1) OR x_(j-2)).
    D_j(t) = Phi^t(x)_j; Delta D_j = D_(j-1) OR D_(j-2).

This is the reflection of G in [G258](../proofs/G258-four-forbidden-words-in-every-forward-right-moving.md).
It is the moving-right Rule30 frame, not the fixed physical centre column.
All profiles below are actual profiles of this same row, not independently
chosen temporal controls. Phi^q(x)=x makes every profile q-periodic from time0.

For a fixed q, the unrestricted pair graph has vertices(a,b) of q-bit temporal
profiles and edges(a,b)->(b,c) when Delta c=a OR b. A full-line q-return is
exactly a bi-infinite path, by the local recurrence and forward uniqueness.
Ring returns correspond to closed paths, as the already carried Lemma R in
[periodic edges section3](rule30-periodic-edges.md#3-cycles-are-ring-orbits-proved-by-hand-the-ring-census-computed)
proves. Rooted profile graphs impose an additional eventually-white past and
are a third boundary problem.

The complete retained PR58 `profile_core_probe.py` and
`profile-core-result.json` were read: the unrestricted bi-infinite cores have
6,6,46 vertices at q2,4,8. Their algorithm repeatedly removes vertices with
zero incoming or outgoing degree. The period-eight carrier-to-rain path is
also explicitly proved in [PR48's carried source](rule30-edge-clock-drop-review.md).
Its clock eight comes from the carrier itself; it does not exhibit a
higher-clock transient between lower-clock tails. The distinct left-only
core has8,12,132 vertices: it does not require an infinite continuation on the
newer side. These are retained author computations, not a GPT rerun.

The archive's ring tests at widths17–24 with clocks8,16,32 and its two timed-out
SAT targets do not settle the full-line conjecture. The complete archive and
source identities are retained in the [GC2229 packet](rule30-group-cocycle-review.md#gc2229-complete-archive-and-replay-review).
No UNKNOWN result is treated as UNSAT.

## A hand proof that Fix(Phi^4) equals Fix(Phi^2)

Suppose Phi^4(x)=x. G258 already forbids00100and11011 in every forward profile,
without a root or periodicity assumption. Consequently a four-periodic profile
cannot have one or three black bits per period: its cyclic repetition would
contain one of those two words. If its least period is four, it must therefore
be a rotation of0011. The only other possibilities are constants or alternating
profiles, all of period dividing two.

Assume for a contradiction that C=D_j has least period four. Shift the time
origin forward to write C=0011 repeated, so F=Delta C=0101 repeated. Put
A=D_(j-2), B=D_(j-1). Then A OR B=F. Both A and B are supported on the two
black positions of F. A one-position support was just excluded by G258, so
each is either0orF.

If B=0, the identity Delta B=A OR D_(j-3) forces A=0, contradicting
A OR B=F. If A=0, Delta A=D_(j-3) OR D_(j-4) forces D_(j-3)=0; then
Delta B=A OR D_(j-3)=0. Thus B is constant, whereas B=F would be required.
The only remaining case is A=B=F.

Now use the next newer profile E=D_(j+1). It satisfies

    Delta E = B OR C = 0101 OR 0011 = 0111.

The XOR of the four bits on the right is1. The XOR of four consecutive
differences of a four-periodic E telescopes to0. This contradiction eliminates
every primitive four-profile. Therefore each D_j has period dividing two,
and Phi^2(x)=x. The converse follows immediately by iteration.

This is a full-line statement with no finite-support or spatial-periodicity
hypothesis. In particular a transient bridge cannot create clock four from
clock-one/two backgrounds. It is **not** a period-four centre-column exclusion.

### Why the newer neighbour is essential

G258 itself retains the legitimate older-side profile chain

    ...,1010,0101,1010,0101,0101,0011

in increasing depth order, with the displayed0011 as its endpoint and the
earlier alternating part continuing indefinitely. Every recurrence up to the
endpoint holds. The next forcing has odd parity and its integral is
anti-periodic after four ticks, hence has least period eight. Thus a finite
prefix can reach clock four; an everywhere four-periodic extension cannot.
This is the precise distinction between the left-only and full-line cores.

The known period-eight0001 ring carrier is a separate guard against extending
the conclusion to Fix(Phi^8)=Fix(Phi^2). No such extension is claimed.

## The already-known two-step classification

The elementary identity in GC732, in these reflected coordinates, is

    Phi^2(x)_j XOR x_j
      = [x_(j-1)=x_(j-2)] AND (x_(j-3) OR x_(j-4)).

Thus an equal adjacent pair forces the two preceding older cells white.
A00pair propagates white forever in the older direction. A11pair first
forces an older00pair and hence the same white half-line. If a nonwhite row
has no first black cell, neither equal pair can occur, so the row alternates
everywhere. If its first black cell is k, all cells below k are white, x_k=1,
x_(k+1) is either0or1, and the row alternates from k+1 onward. A later00pair
would erase the earlier black cell; a later11pair would force such a00pair.
Conversely each of these rows satisfies the displayed identity.

Therefore the full-line two-return rows are all white, the two alternating
rows, and these white-to-alternating interfaces. This recovers GC732's known
interface, not spatial periodicity of every full-line return. Together with
the preceding argument it classifies the full-line four-return rows too.

## What a larger-clock result would still need

Standard finite-graph pumping applies on both sides of any chosen vertex of
a bi-infinite path: repeat a cycle somewhere in its infinite past, retain the
finite segment through the vertex, and repeat a cycle somewhere in its future.
This yields a path with spatially periodic tails. For q=2^k, an actual point
of least temporal period q has at least one profile of least period q;
otherwise all profiles have period dividing q/2. Keeping such a profile in
the finite segment preserves the full point's least period q after pumping.

This is the two-sided version of the standard argument already used in GC759.
It does not join the two tail cycles to each other. Consequently a ring-only
classification at a proposed q would still need to exclude primitive-q
profiles on transient connections. The current hand result does that at q4.
No primitive16or32 bridge was constructed or excluded in this block.

Record searched: GC732/GC759/G258 and their carrying source; L1066's complete
q8 ring components; GC2014's rooted q32 graph; PR48; PR55's actual WordStep
and realization interfaces; PR58's exact head70ca1830/archive87ba7661;
kit932cf8dd actual PeriodicPoints Recurs and velocity hypotheses, plus current
03:06:23Z portal/open-PR index and exact finite-return source headings. The
PeriodicPoints spatial-periodicity theorem excludes the light-speed boundary
used here and supplies no shortcut. The initial candidate ban was exactly
G258, found before any new computation. Urías–Salazar-Anaya–Ugalde–Enciso1996,
[Traveling patterns in cellular automata](https://pubmed.ncbi.nlm.nih.gov/12780279/),
abstract, already treats finite automata and travelling patterns; the full
paper was not read and no theorem is imported from it. No literature priority
or additional-submission disposition follows from these searches.

**Next step:** read PR33's exact finite eight-return theorem and its certificate
induction. Its finite newest-first state, with three cells dropped before the
two-return test, is different from the full-line problem above. Determine the
carrying invariant and boundary role before attempting any transfer. The old
GC1996 hand-D alternative is withdrawn: L1038/GC1994 already recorded repeated
failed hand attempts, followed by a completed computer-assisted proof. Reopen
that hand route only with a new compression identity, not another identical
two-tick expansion. No larger graph, seed census or compiler job is queued.
