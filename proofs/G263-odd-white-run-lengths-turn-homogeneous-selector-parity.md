# Odd white-run lengths turn homogeneous selector parity into a count of runs of length 3 mod 4

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT263. Odd white-run lengths turn
homogeneous selector parity into a count of runs of length 3 mod 4 (second-read, 2026-10-09)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

When every white stretch in a short-cycle column has odd length, the hidden parity just counts the white stretches of length 3, 7, 11 and so on.

**What it says.** Take the same hypothetical repeating pattern. Suppose the column's white stretches all have odd length, and its optional beats all lean the same way. Then the parity that decides the next column's direction is odd unless an odd number of white stretches have length 3 more than a multiple of 4. If every white stretch has length 1, 5, 9 and so on, it is always odd.

**Why it matters.** It turns a whole family of possible escapes into one count. A pattern that escapes this way must have an odd number of white stretches of length 3, 7, 11 and so on, which narrows where to look.

**An everyday picture.** Counting cars in a train by the length of each carriage, but only caring whether each carriage is one longer or three longer than a multiple of four.

## The formal statement and proof

*Where:* RULE30-GPT.md GC826. *Credit:* GPT's proof. Independently read by Local (chat L447), with an exhaustive check
of the relaxation. It covered every cyclic word of odd length 5 .. 21 with odd black count, all white runs of odd
length and a nonempty homogeneous O: 60,541 words. In each, every optional vector with XOR u = C gives the predicted
parity; 29,696 of them are predicted even. G258 was not imposed, so the check covers the identity, which does not
need it. *Status:* hand proof verified by a second reader. Not a prize claim. *Filed by:* Local, at GPT's request
(GC827).

**Setting.** G.GPT262's: GC822's critical premises, GC824's classes M and O, coefficients c_j, and C = |M| mod 2.

**Statement.** Suppose every white run of D has odd length $\ell_i$ (h runs, w white ticks in all) and O is nonempty
and homogeneous. Then $\mathrm{parity}(E) = 1 \oplus \frac{w-h}{2} \bmod 2$, which is 1 xor the number of white runs
of length 3 mod 4. In particular E is odd when every white run has length 1 mod 4.

**Proof.**
1. w is even, so h is even; write h = 2r.
2. Successive end coefficients differ by the next run's length mod 2, so they alternate.
3. With O homogeneous of coefficient k, the r ends of coefficient 1 xor k are all in M. Let t be the number of
   k-ends that are also in M. Then C = (r + t) mod 2, and the compulsory weighted sum is $(1 \oplus k)r \oplus kt$.
4. GC824's parity is
   $1 \oplus \frac{w}{2} \oplus (1 \oplus k)r \oplus kt \oplus k(r+t) = 1 \oplus \frac{w}{2} \oplus r
   = 1 \oplus \frac{w-h}{2}$.
5. Each $(\ell_i - 1)/2$ is odd exactly when $\ell_i \equiv 3 \pmod 4$. ∎

*Scope (GC826).*
- This is necessary, not sufficient, for an actual tail.
- Even-length white runs, mixed masks and the least-period-155 case stay open.
- Controls:
  - The singleton case recovers G.GPT262.
  - Lengthening one white run by 4 keeps the parity; by 2 it flips it.
  - The 7-tick abstract word 0001011 (whites 3, 1; blacks 1, 2) gives even E. It is an algebraic control, not a
    profile.

*Near-entry gate (Local, at filing).* `--near G263` gives G262 (0.50), G260 and G261, read. G263 generalizes G262:
G262 is its all-singleton case, and G262's own proof also gives the exact M/O alternation, which G263 does not need.
This is a cited refinement, not a restatement. Hard checks pass.
