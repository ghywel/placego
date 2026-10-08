# nonlinear event parity in a dyadic causal cone

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT215. nonlinear event parity
in a dyadic causal cone (second-read by Local, 2026-10-08)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A black periodic wall sample requires odd parity of actual nonlinear events in its selected backward cone.

**What it says.** At one black time in G214's dyadic block, the binomial propagation weights select an odd number of active source cells. For full0101, all strictly-left sources disappear and selected cells have time plus site even.

**Why it matters.** It places the required events inside a precise causal cone. Merely counting events in a geometric cone misses zero coefficients and cancellation. The cone still grows, so finite compatibility remains open.

**An everyday picture.** Several contributions can reach an observation, but some paths carry zero weight and two matching contributions cancel. The selected total must match the observation.

## The formal statement and proof

**Where:** RULE30-GPT.md GC420 at1b40b1e, claim and proof copied verbatim below. Local L253 in401eba2 checks Duhamel, the kernel, both guards and G27's full0101 specialization. Hypotheses are G214's finite support[-R,R], nonzero eventually p-periodic centre, onset a and s>=a; N is its least dyadic power at least R+s+p. This refines G28's existing certificate using G214's quantitative block, not a new identity.

Use GC419's hypotheses and dyadic N. Among T=s+N,...,s+N+p-1, choose a time with wall bit1; such a time exists by periodicity. For l>=0 define K_l(i)=binom(l,(l+i)/2) modulo2 when abs(i)<=l and l+i is even, and0 otherwise. Then the actual nonlinear sources obey the exact certificate

`XOR_(t=s,...,T-1) XOR_i K_(T-1-t)(i)*V_t(i) = 1`.

In particular an odd number of active, coefficient-selected spacetime cells lie in this cone. Every selected cell satisfies abs(i)<=T-1-t. Consequently some nonlinear activation lies inside the truncated cone abs(i)<=s+N+p-2-t, rather than merely somewhere in space during GC419's interval.

**Proof.** Iterating x_(t+1)=A*x_t+V_t gives x_T=A^(T-s)*x_s XOR sum_(t=s)^(T-1) A^(T-1-t)*V_t. GC419's dyadic separation makes the homogeneous centre term0 at each of the p candidate times. Expansion of (S+S^-1)^l gives the displayed binomial coefficient at the centre. Finite propagation makes every sum finite. Thus the chosen wall1 is exactly the stated event parity. This proves the claimed localization, with no assumption that the nonlinear sources are independent.

**Full0101 specialization.** If the full wall is0101 from time0, G27's compatible-left classification gives opposite temporal supports for every neighboring pair on the left, including sites-1 and0. Hence V_t(i)=0 for all i<0. The certificate's event sites can therefore be restricted to i>=0. Its chosen T is odd, so the kernel additionally requires t+i even. This is a right-half necessary condition; it does not classify the right half. The claim about left sources uses the exact full0101 hypothesis, not a general eventually periodic wall or an unproved eventual-left parity assertion.

**Scope:** the selected source radius grows; it need not enter a fixed forced strip or exclude a finite witness. The left-source specialization requires full0101 from time0.

**Duplicate guard for G215:** nearest G202,G214,G211 read in full. G214 supplies the dyadic zero block; this entry adds the exact selected causal parity and full0101 left-source specialization. G202 concerns temporal profile overlap and G211 finite white-block precursors. G28 is the credited Duhamel source, not reintroduced as a new identity.
