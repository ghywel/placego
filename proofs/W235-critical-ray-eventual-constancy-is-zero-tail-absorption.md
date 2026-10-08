# Critical-ray eventual constancy is zero-tail absorption

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G235. Critical-ray eventual
constancy is zero-tail absorption (GPT, 2026-10-08; waiting room, GC550)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

The critical-ray bit cannot become constant under a fair initial row, except on a null set.

**What it says.** Its right tail would have to reach the all-zero infinite state. Invariance of the fair measure makes that absorption event null. Both bit values therefore recur infinitely often almost surely.

**Why it matters.** This proves the single-bit baseline without critical-ray ergodicity. Simultaneous longer zero windows and damage escape remain open.

**An everyday picture.** A steady reading at the boundary would require every position farther along the tail to stop contributing, not only its nearest two neighbours.

## The formal statement and proof

*Provenance:* RULE30-GPT.md GC550; uses the exact GC534 cocycle and the previously verified invariant fair measure from G97. Candidate-neighbour check under W235 read G149, G97 and G141. G97 supplies invariance; G149 and G141 concern imposed-wall spatial predecessors, not critical-ray constancy. This is a new boundary characterization using those standard update facts, not their restatement. Independent hand reading pending. No experiment, rate, ergodicity or singleton prize claim.

Use GC534's right-half map H(z,Y)=(z XOR q(Y),G(Y)), where q(Y)=Y_1 OR Y_2 and G(Y)_j=Y_j XOR (Y_(j+1) OR Y_(j+2)). Suppose its boundary bit is constant at all times t>=T. Then q(G^t Y)=0 for every t>=T: both first tail bits are zero at every such time. If the first m tail bits are zero at all these times, with m>=2, updating tail site m-1 gives

    0=0 XOR (0 OR (G^t Y)_(m+1)),

so bit m+1 is also zero at every time t>=T. Induction gives G^T Y equal to the entire all-zero infinite tail. Conversely a tail which reaches zero stays zero and makes the boundary constant thereafter. Thus eventual constancy holds exactly on the union, over finite T, of the preimages G^(-T)({all zero}). This does not require independence over time.

Under the iid fair initial right-tail measure, G preserves the measure by the already retained G97/GC535 projection argument. The all-zero tail has probability zero: its first m zeros have probability 2^(-m), tending to zero. Each fixed-T preimage also has probability zero, and their countable union has probability zero. The critical-ray bit therefore takes both values infinitely often almost surely. The same reasoning applies at every fixed ray offset; a countable intersection gives simultaneous one-bit recurrence at all integer offsets under the full-line fair law. This is recurrent visitation, without a limiting frequency, return-time bound or mixing assertion.

**Independent deterministic controls.** A nonempty finite right tail never reaches all zero: its rightmost occupied site has zero farther neighbours and its bit stays one under G. Its boundary ray consequently cannot become constant. With no right tail, z is constant; the singleton's rightmost ray has precisely this form and remains black. An infinite all-ones right tail reaches all zero in one update, so nonemptiness alone is insufficient; the finite-tail qualification is essential. These are literal update checks and preserve the probability-zero exception in the fair-law statement.
