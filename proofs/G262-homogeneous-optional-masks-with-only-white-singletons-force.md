# Homogeneous optional masks with only white singletons force odd selection

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT262. Homogeneous optional masks with
only white singletons force odd selection (second-read, 2026-10-09)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

In the hypothetical repeating pattern, if a short-cycle column has only lone white beats and its optional beats all lean the same way, the hidden parity is forced odd.

**What it says.** The column's white beats each stand alone. Rule 30 forbids two long black stretches separated by one white beat, so the long and short black stretches must take turns. Taking turns fixes the count of compulsory beats, and the parity that decides the next column's direction comes out odd.

**Why it matters.** It closes one more branch in the search for a period-2 pattern, again by reasoning alone. Anything that escapes must have a longer white stretch somewhere, or optional beats that lean both ways.

**An everyday picture.** Fence posts between single gaps: if no two tall posts may stand side by side, tall and short must alternate, and you can count them without looking.

## The formal statement and proof

*Where:* RULE30-GPT.md GC825. *Credit:* GPT's proof. Independently read by Local (chat L446), with an exhaustive check
of the relaxation. It covered every cyclic word of odd length 5 .. 21 with odd black count, all white runs singletons
and no cyclic 11011: 2,272 words. The 839 with homogeneous O give parity 1 for every optional vector u with
XOR u = C; the 1,433 mixed-O words are outside the statement. *Status:* hand proof verified by a second reader. Not a
prize claim. *Filed by:* Local, at GPT's request (GC826).

**Setting.** GC822's critical premises: D is the first odd-tail profile, of proper least period m in {5, 31}. Use
GC824's classification of D's white-run ends.
- M: the ends followed by a black run of length >= 2. They are compulsory marks.
- O: the ends followed by a singleton black run. They are optional.
- c_j is the parity of the white phases after j, and C = |M| mod 2.

**Statement.** If every white run of D is a singleton and all ends in O have the same coefficient k, then E has odd
parity.

**Proof.**
1. The white runs are the white ticks, so h = w, which is even and nonzero. Successive ends are one white tick
   apart, so their coefficients alternate around the cycle.
2. The intervening white singleton between two adjacent black runs of length >= 2 would form 11011, which G.GPT258
   forbids. So no two cyclically adjacent black runs are both M, and O is nonempty.
3. If O is homogeneous with coefficient k, every (1 xor k)-end is M. The run after each k-end neighbours an M run,
   so it is O. Hence M and O alternate, |M| = h/2 = C, and every M coefficient is 1 xor k.
4. GC824 gives $K = 1 \oplus C \oplus (1 \oplus k)C$ and $\mathrm{parity}(E) = K \oplus kC = 1$. ∎

*Scope (GC825).* A least-period-31 even-E counterexample therefore needs a white run of length >= 2, or optional ends
in both coefficient classes. This is necessary, not an existence claim.
- With h = 2 the two black runs neighbour each other on both sides, and the argument holds.
- No colour-swapped version is claimed.
- Controls: D = 01011 gives odd E, matching G.GPT260. The all-white-singleton word (011)^2 is rejected by 11011
  first.

*Near-entry gate (Local, at filing).* `--near G262` gives G261 (the phase formula it applies), G260 (its least-period-5
case) and 06 (zero runs), read. G262 is a new case of G261's formula, not a restatement. Hard checks pass.
