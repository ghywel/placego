# Proper-period tail profiles need both singleton colours; the selection parity reduces to phase sums

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT261. Proper-period tail profiles
need both singleton colours; the selection parity reduces to phase sums (second-read, 2026-10-09)"; rebuild with
`python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this
file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

In the same hypothetical repeating pattern, every column that repeats on a short cycle must contain both a lone black beat and a lone white beat.

**What it says.** A column repeating every 5 or 31 steps cannot be made only of long runs: it needs at least one isolated black tick and one isolated white tick. The parity that fixes the next column's direction then reduces to a short sum over the column's white phases, one term per phase.

**Why it matters.** It turns the remaining question for the 31-step case into a small, exact bookkeeping problem, instead of a search over every possible column.

**An everyday picture.** A drum pattern that loops quickly must have at least one single hit and one single rest; and to know how the next drummer must play, you only need to tally a few beats of the loop.

## The formal statement and proof

*Where:* RULE30-GPT.md GC822. *Credit:* GPT's proof. Independently read by Local (chat L442), with a literal check:
random D of period m and odd count, and U built under GC798's projection. The compressed formula equals E from full
310-tick integration in every admissible case (1,985 at m = 5, 2,976 at m = 31), and XOR u_j = 0 throughout. The
generator did not impose G258 or the singleton conditions, so this checks the identity, which needs neither.
*Status:* hand proofs verified by a second reader. Not a prize claim. *Filed by:* Local, at GPT's request (GC823).

**Statement.** In GC821's actual critical setting, let D have proper least period m in {5, 31}, with 155 = m s and s
odd.
- (a) D has at least one black singleton run and at least one white singleton run. This holds for every
  proper-period profile in this tail.
- (b) Let J be D's white phases in an m-block, w = |J| (even), c_j the number of white phases after j (mod 2), and
  $u_j = \bigoplus_b U(bm + j)$. Then $\bigoplus_{j \in J} u_j = 0$ and
  $\mathrm{parity}(E) = 1 \oplus (w/2 \bmod 2) \oplus \bigoplus_{j \in J} u_j c_j$.

**Proof.**
- (a) GC821 gives some singleton. If every white run had length >= 2, a black singleton would sit in 00100,
  forbidden by G.GPT258, so there would be no singleton at all. The symmetric argument with 11011 gives the other
  colour.
- (b) w is even because D's m-block black count is odd (s odd, total odd). U <= Delta D makes u_j = 0 at white
  phases that are not run ends.
  - A white end before a black run of length >= 2 is marked in every copy (GC798), so u_j = 1.
  - D OR U odd gives $\bigoplus u_j = 0$.
  - In GC796's ordered-pair count, a white tick at phase j has c_j later whites mod 2 in every copy, since each later
    full block adds an even w.
  - Summing over the s (odd) copies gives $\bigoplus_j c_j (1 \oplus u_j)$, and
    $\bigoplus_{j \in J} c_j = \binom{w}{2} \equiv w/2$. ∎

*Control (GC822).* At m = 5, D = 01011 gives J = {0, 2}, (c_0, c_2) = (1, 0), u_2 = 1, then u_0 = 1, so the parity
is 1, which recovers G.GPT260. At m = 31 the formula is the remaining obligation, not a value. The 155 case is
uncompressed.

*Near-entry gate (Local, at filing).* `--near G261` gives G260 (its companion: (b) at m = 5 recovers G260's value,
but G260's forcing of the word 01011 and of the marked phase is its own), 03 and G259, read. None is restated. The hard
checks pass.
