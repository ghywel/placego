# The critical selector is odd when the first odd-tail profile has least period 5

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT260. The critical selector is odd
when the first odd-tail profile has least period 5 (second-read, 2026-10-09)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

In one family of hypothetical repeating patterns, a hidden parity is always odd, which pins down one choice that had looked free.

**What it says.** Suppose a Rule 30 pattern repeats every 310 steps, and a certain column next to its turning point repeats every 5. Then that column must be the beat 01011, and a parity that decides the next column's orientation comes out odd. So the next column's direction is forced, with no choice left.

**Why it matters.** It closes one branch of a search for possible period-2 patterns by pure reasoning, without a computer search. The harder branches, columns repeating every 31 or 155 steps, remain open.

**An everyday picture.** A combination lock with a hidden wheel: once you know one dial turns every 5 clicks, the hidden wheel can only sit in one position.

## The formal statement and proof

*Where:* RULE30-GPT.md GC821. *Credit:* GPT's proof. Independently read by Local (chat L442), with a literal check:
U built from the stated constraints and filtered by GC798's exact projection, the odd driver and B's period 310. All
10,018 admissible U give odd E and XOR a_b = 1. (A purely random U sampler found none admissible; it is not counted as
validation.) *Status:* hand proof verified by a second reader; conditional on the critical premises below. Not a prize
claim. *Filed by:* Local, at GPT's request (GC823); the G number is assigned at filing.

**Setting.** This is the actual period-310 all-L interface of GC785 and GC796.
- A complements after 155, and D is its first 155-periodic right profile, with an odd black count over 155 (GC785).
- U is the next profile, with $\Delta D = U \lor W$ and $\Delta U = W \lor X$.
- B is a period-310 primitive just left of A, and $E(t) = B(t+155) \oplus B(t)$.

**Statement.** If D has least period 5, then D is a temporal translate of 01011 repeated 31 times, and E has an odd
black count. So GC793's next-orientation selector is unique in this subcase.

**Proof.**
1. A proper-period D with no singleton run has every transition marked (GC798), so U = Delta D, and the pair's joint
   period divides D's, against GC760.
2. Counts 1 and 4 contain 00100 or 11011, which G.GPT258 forbids. Counts 2 with adjacent blacks and 3 with adjacent
   whites have no singleton. 00101 has an even count over 155, against GC785.
3. Take D = 01011, so T = Delta D = 11101. Phase 2 enters a black run of length 2, so it is marked: U(5b + 2) = 1.
   Phase 3 has T = 0, so U(5b + 3) = 0.
4. Put $a_b = U(5b)$. D OR U has an odd count (A complements), and D has 93, also odd. So the U-black ticks at D-white
   positions are even in number: $31 + \sum a_b$ is even, and $\bigoplus a_b = 1$.
5. In GC796's formula only the ticks j = 5b can have $r_j = 1$ (value $1 - a_b$), and each has $1 + 2(30 - b)$ later
   white ticks, an odd number. So $\mathrm{parity}(E) = 1 \oplus (1 \oplus \bigoplus a_b) = \bigoplus a_b = 1$. ∎

*Scope (GC821).* Nothing is claimed about iterated uniqueness, the least-period 31 and 155 cases, or excluding this
interface. GC817's genuine q5 source (D = 01011, next profile 11100) is a local control with odd E. With U = 0 instead,
E is even, but the U equation then fails, which shows that the extra right equation supplies the marked phase.

*Near-entry gate (Local, at filing).* `--near G260` gives G259 (the coprime-period lemma), G252 (an odd adjacent
correlation at p = 310) and G158, read. They are different statements; G259 and G252 are the same interface's other
constraints. None is restated.
