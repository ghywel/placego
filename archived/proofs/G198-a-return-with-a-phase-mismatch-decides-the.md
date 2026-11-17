# a return with a phase mismatch decides the known component

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT198. a return with a phase mismatch
decides the known component (second-read by Local, 2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A way back matters only if it arrives out of step with the old loop.

**What it says.** In a region containing the known loop, swaps keep happening exactly when some walk leaves and
comes back at a position different from the one its length predicts. Coming back in step keeps the old period
locked.

**Why it matters.** It names the exact thing a search would have to find. No out-of-step return is known for the
period-16 exits, and finding only in-step ones would not rule one out.

**An everyday picture.** A clock hand taken off and put back: it agrees with the old rhythm only if it lands where
the elapsed ticks say it should.

## The formal statement and proof

### GPT G198 — A return with a phase mismatch decides the known component (2026-10-07; second reader pending)

**Statement, a specialization of reviewed G191.** Let a finite directed graph have the swap automorphism sigma of G190, and a simple directed cycle v_0,...,v_(q-1), with dyadic q>=2 and sigma(v_t)=v_(t+q/2). Let C be its strongly connected component. Then C is persistent in G191's sense if and only if there is a directed excursion from some v_s to some v_u, with no original-cycle vertex in its interior, whose length ell satisfies

    ell+s-u != 0 mod q.

Such an excursion must use an edge outside the original cycle. A return satisfying ell+s-u=0 does not certify persistence. Phases are ORDERED phases modulo q; the unordered quotient phase alone is insufficient.

**Prediction and counterfactual for hand controls.** The original cycle fixes the possible component gcds to divisors of q. A return with a mismatch should force a proper divisor and hence class-preserving swap. The counterfactual that any recurrent branch or any return length not divisible by q suffices will fail on a locked component with a phase-aligned detour. No trajectory search or graph census runs here.

**Component period.** Since v_s and its swap are joined along the original cycle, sigma(C)=C. Let G be C's cycle gcd. The original q-cycle gives G dividing q, hence G is a power of two. Along the original half-cycle, cyclic class advances by q/2, so sigma's cyclic-class displacement is q/2 modulo G. If G=q, that displacement is q/2 and the component is locked. If G is a proper divisor of q, dyadicity implies G divides q/2 and the displacement is zero. By reviewed G191 these are respectively the nonpersistent and persistent cases. Thus C is persistent exactly when G is a proper divisor of q.

**A mismatched return is sufficient.** Close the excursion v_s to v_u by the forward part of the original cycle returning to v_s. Its length L is congruent to ell+s-u modulo q. A nonzero residue means L is not divisible by q. Since G divides both L and q, it is a proper divisor of q; the previous paragraph applies. The closing part may have length zero if u=s. The resulting positive closed walk is enough; it need not be a simple cycle.

**Necessity and first-return reduction.** The gcd of positive closed-walk lengths based at any vertex of a strongly connected finite graph is G. To recall why, every such walk is a concatenation of directed cycles and has length divisible by G. Conversely, paths from the base to a cycle and back give a connector closed walk of length a+b and, after inserting that cycle of length d, one of length a+b+d; their difference recovers d. The gcd of based walks therefore divides every cycle length. A zero-length connector causes no difficulty, since the cycle itself is then a based walk.

If G is proper, some positive closed walk based at v_s has length not divisible by q; otherwise that gcd would be divisible by q. Cut it at every visit to an original-cycle vertex. The segment residues length+startphase-endphase add modulo q to the total walk length, since the phases telescope. At least one segment has nonzero residue. Its interior avoids the original cycle. Ordinary cycle edges have zero residue, so that segment is an excursion departing from the original cycle and returning with a mismatch. This proves the equivalence, without claiming that any such excursion has been found in Rule30.

**Independent locked-detour control.** Start with a directed four-cycle0->1->2->3->0, sigma(t)=t+2. Add vertices a,a' exchanged by sigma and edges0->a->2, 2->a'->0. There is genuine internal branching and a two-edge return to the old circuit, but it is aligned: ell=2, s0, u2. Assign cyclic classes0,1,2,3 to the old vertices and1,3 to a,a'. Every edge advances by1 modulo4, so all closed walks have length divisible by4. The old four-cycle shows G=4 exactly. Swap shift2 keeps the component locked. This is an abstract control, not an actual larger Rule30 component.

**Independent mismatched control.** Instead add chords0->2 and2->0 to the four-cycle, preserving sigma. The first chord rejoins at phase2 after one edge, residue1-2=3 modulo4. Closing through2->3->0 gives a three-cycle, so G divides gcd(4,3)=1 and the component is persistent. Again this is an abstract graph control, not a found Rule30 return.

**Identified unexpected orientation check.** In the unmodified four-cycle, three original edges from phase0 end at ORDERED phase3 and are aligned: 3-3=0. The unordered quotient identifies phases1 and3. Mistaking that endpoint for phase1 gives residue2 and would falsely report persistence. Keep the orientation bit from G193, or retain the full ordered windows, whenever recording a rejoin.

**Actual scope and next obligation.** For D1 the known q16 circuit has only the two unordered exit decisions0 and4, by its completed first-edge census. Any mismatched first-return excursion must start at one of them or their swaps. G197 proves every first rejoin requires at least26396 edges. A hypothetical rejoin from s0 at ell26396 would be aligned at ordered u12, and mismatched at any other u; no such return is asserted. A finite list of aligned returns cannot prove that every return is aligned. This specializes G191's standard gcd/cyclic-class machinery into the exact question a continuation search would have to answer. It establishes neither rooted growth nor persistence of an actual component. Local: second-read the based-walk gcd, first-return reduction and orientation control; no computational job requested.

*Second reader's note on G198 (Local, 2026-10-07; chat L167).* Correct. The swap joins $v_s$ to $\sigma(v_s)$ along the
cycle, so the component is swap-invariant and its period $G$ divides $q$. The class shift is $q/2$ modulo $G$: it is
$G/2$ when $G = q$ (locked) and 0 when $G$ is a proper divisor (persistent, by G191). Closing an excursion along the
cycle gives a walk of length $\ell + s - u$ modulo $q$, so a mismatch forces a proper divisor. Conversely, cutting a
based walk of length not divisible by $q$ at its cycle visits telescopes the residues, so one segment must be a
mismatched excursion, since cycle edges have residue 0. Checked (`rule30_audit_g99_g100.py`, S95) on 600 random graphs
built around a dyadic cycle ($q = 2, 4, 8$) with the half-turn swap and random swap-closed additions: 321 persistent,
279 not. Persistence held exactly when a mismatched excursion existed, found by a search over (vertex, length mod $q$)
avoiding the cycle's interior, and G191's test on the component agreed every time. GPT's locked detour has $G = 4$ and
no mismatched excursion, and the chords give $G = 1$. The ordered-phase trap reads 0 at phase 3 and 2 at phase 1, as
stated, and the D1 arithmetic gives an aligned hypothetical rejoin at phase 12.
