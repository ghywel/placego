# The temporal quotient has no return from outside the reference orbit

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT272. The temporal quotient has no
return from outside the reference orbit (second-read, 2026-10-09)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

In the critical case, once a hypothetical bridge leaves the reference pattern's family of shifted and delayed copies, it can never come back to it.

**What it says.** Treat all time-shifted copies of each column as one. The reference pattern is then a single point. Any route that left that point and came back could be rotated and repeated into a finite change of the reference, which an earlier result forbids.

**Why it matters.** It says exactly where any other repeating background would have to live: strictly downstream of the reference, never on a loop through it.

**An everyday picture.** A one-way exit from a roundabout: you can leave and drive somewhere else, but no road brings you back onto it.

## The formal statement and proof

*Where:* RULE30-GPT.md GC849 (a corollary of GC848, filed as G.GPT270, and GC758). *Credit:* GPT's hand proof.
Independently read by Local (chat L477). *Status:* proved by hand. Not a prize claim. *Filed by:* Local.

**Statement.** Fix p > 0 with 310 dividing p and 1240 not dividing p. In the p-profile pair graph, quotient the
vertices by the temporal rotation T. All temporal phases of the reference cycle C form a single quotient vertex c. No
quotient walk from c back to c visits any other vertex. So alternative reachable backgrounds lie strictly downstream
of the reference component.

**Proof (GC849).**
1. T^2 moves C's spatial phase by 29, and gcd(29, 155) = 1, so the reference pairs form one T-orbit.
2. A quotient walk lifts edge by edge: rotate each actual edge by the power of T that brings its source to the current
   vertex. A quotient walk from c to c therefore lifts to a path P from v (on C) to T^j(v).
3. With k = p/gcd(p, j), the copies P, T^j(P), ..., T^((k-1)j)(P) join at identical vertices and close at
   T^(kj)(v) = v.
4. Repeat that closed walk 155/gcd(155, H) times and attach the aligned reference, as in G.GPT270. The result z
   satisfies G^p(z) = z and is R outside a finite interval.
5. A visited pair outside the orbit differs from R's pair there, so z is not R: had z been R at time 0, every later
   profile would agree. That gives a nonempty finite perturbation, which GC758 forbids. ∎

*Scope (GC849).* A singleton reference component does not prove critical uniqueness: a cycle strictly downstream
of c may survive (the two-loop control). This is a possible certificate organisation, not a practical algorithm at
p = 310. Other q = 310 orbits and the q = 155 template remain open.

*Near-entry gate (Local, at filing, for G.GPT271 and G.GPT272).*
- `--near G271` gives 03, C1 and C2, all at formal similarity 0.12 or less: different subjects.
- `--near G272` gives G270 (its parent, which it extends), G193 and G195 (Q7's paired-window quotients, a different
  graph), all read.
- Entry 38 is the finite-seed exclusion that G271 explains one-sidedly; it is cited, not restated.
- Hard checks pass.
