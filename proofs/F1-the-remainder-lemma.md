# The remainder lemma

*Collatz. Derived from [PROOFS.md](../PROOFS.md), entry "F.1. The remainder lemma"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved.

## In plain words

After k Collatz steps, a number's remainder in base 2 has become a remainder in base 3, and the rest passes through
untouched.

**What it says.** Write a starting number as 2^k times m plus a remainder r. After k steps, with a odd steps among
them, it becomes 3^a times m plus the value r itself reaches, which is below 3^a. This is Terras's identity (1976),
restated.

**Why it matters.** It is the Collatz twin of the forced left half, and the avenue Collatz has that Rule 30 lacks:
after the free bits, the state is an explicit number. All the counting work of GPT's G39 to G75 builds on it.

**An everyday picture.** Changing pounds into euros: the notes are converted at a fixed rate, a straight
multiplication, while the loose change is counted on its own and comes back as coins worth less than one new note.

## The formal statement and proof

*Where:* COLLATZ-PRIZE.md, "4. The state after the free bits is a remainder modulo a power of 3 (2026-10-05)". *Bears on:* the counting form for Collatz (COLLATZ-PRIZE.md §1). *Status:* proved.

**Lemma.** Let $0 \le r < 2^k$, and let $a$ be the number of odd steps among the first $k$ steps of $r$. Then

*Correction (Cloud, 2026-10-06): the copy above was cut off mid-sentence. The statement in COLLATZ-PRIZE.md §4 continues:*

```math
0 \le T^k(r) < 3^a \qquad\text{and}\qquad T^k(2^k m + r) = 3^a m + T^k(r) \ \text{ for every integer } m .
```

## The proof, copied from COLLATZ-PRIZE.md

*Verbatim from [COLLATZ-PRIZE.md](../COLLATZ-PRIZE.md), the section named above; the master PROOFS.md holds the statement only.*

*Local's addition (`tests/probes/prizes/collatz_residue.py`, predictions written before the run).*

§2 found that after the free bits the Collatz state is an explicit integer $y$, and asked for its distribution
modulo powers of 2. That integer has an exact description.

**Lemma.** Let $0 \le r < 2^k$, and let $a$ be the number of odd steps among the first $k$ steps of $r$. Then

```math
0 \le T^k(r) < 3^a \qquad\text{and}\qquad T^k(2^k m + r) = 3^a m + T^k(r) \ \text{ for every integer } m .
```

So $T^k$ trades a remainder modulo $2^k$ for a remainder modulo $3^a$, and passes the quotient $m$ through unchanged.
By Terras's formula $T^k(r) = (3^a r + c_v)/2^k$, the new remainder is the least non-negative residue of
$2^{-k} c_v$ modulo $3^a$, where $c_v = \sum_j 3^{a-1-j}\,2^{i_j}$ over the positions $i_j$ of the odd steps.

*Proof.* The second identity is Terras's: adding $2^k$ to a number leaves its first $k$ parities alone and adds
$3^a$ to its $k$-th iterate. Take $m = -1$. The number $r - 2^k$ is negative, and $T$ maps negative integers to
negative integers. So $T^k(r) - 3^a < 0$. $\square$

**Checked** for every $r < 2^k$, $k \le 18$ (CR0, CR1). I had predicted the weaker "least residue, or that plus
$3^a$, the second case rare" (CR2). The second case never occurs, and the proof above came after the run. The
counterfactual modulus $3^{a+1}$ fails for two numbers in three, as it must. The lemma is elementary and is probably
in the Collatz literature; it was not looked up.

**What it adds to §2 and §3.**
- **The Collatz twin is a statement about one number written in two bases.** The next parities of an orbit are the
  low *binary* digits of a remainder modulo a *power of 3*. "Past the free bits the count follows the coin" (§1)
  says exactly that those binary digits are equidistributed over the parity vectors that stay up. That is the
  setting of Furstenberg's $\times 2 \times 3$ problem and of Erdős's question on the ternary digits of $2^n$
  (PRIOR-ART), where two bases are also known to be independent on average and unknown case by case.
- **It is Tao's object, not a counterpart of it.** Modulo $3^a$, the remainder $2^{-k} c_v$ is the offset whose
  distribution Tao (2019) studies as the Syracuse random variable, for random parity vectors. His fine-scale mixing
  estimate (his Proposition 1.14, cited from memory) gives errors that fall like a power of $a$. The binary digits
  of a least residue are read off by Fourier coefficients modulo $3^a$ whose total weight is about $a$, so such an
  estimate should give the *set* form of §1's statement: almost every number pays the coin's rate. The count
  below one needs errors smaller than $2^{-w}$, which is exponentially beyond a power of $a$. This is §7's lesson 2
  again, now with the exact place where it bites.
- **The same shape as Rule 30's left and right parts.** The quotient $m$ is the free side: it passes through a
  bijection, as the seed's left cells do (RULE30-PRIZE.md §8.51). The remainder is the finite-support side, and
  its new digits are functions of the old ones alone.
- **Jen's theorem with a clock has a Collatz form** (RULE30-PRIZE.md §8.54). A parity sequence that is $P$-periodic
  on a window pins the number 2-adically to a rational cycle point, so the window is at most about as long as the
  number has bits. The bit length is to Collatz what the distance to the left edge is to Rule 30.
