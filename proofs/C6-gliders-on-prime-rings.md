# Gliders on prime rings

*Short proofs restated from the running text. Derived from [PROOFS.md](../PROOFS.md), entry "C.6 Gliders on prime
rings (RULE30-PRIZE.md §8.67; 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and
this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved (the pigeonhole); the distinctness of lengths at $n = 13, 17, 19, 23$ and 29 is the census's exact finding (§8.

## In plain words

On a ring with a prime number of squares, any rhythm that is rare must be a pattern travelling round the ring.

**What it says.** Wrap Rule 30 round a ring of p squares, p prime. Turning the ring by one square commutes with the
rule, so it takes each repeating cycle to a cycle of the same length. Because p is prime, a cycle either comes in a
family of p copies or is turned into itself. So a cycle whose length occurs fewer than p times is a glider: turning
the ring does the same as running time on. The census found every cycle length distinct at p = 13, 17, 19, 23 and
29, so there every cycle is a glider. GPT's G55 later made this an exact criterion.

**Why it matters.** It is an exact, structural fact about Rule 30 in small closed worlds, of the kind the record
wants to tell apart from mere measurement.

**An everyday picture.** A Mexican wave in a round stadium: if a pattern of standing fans is the only one of its
kind, then moving one seat round can only show you the same pattern a moment later. It is a wave travelling round
the ring.

## The formal statement and proof

*Where:* §8.67; the census `ring_census.c` to $n = 24$. *Bears on:* constellation row 10 ("which parts are proved").
*Status:* proved (the pigeonhole); the distinctness of lengths at $n = 13, 17, 19, 23$ and 29 is the census's exact finding (§8.67 and its addendum). GPT's G55 (second-read, §E2) refines it to an exact criterion: lengths are distinct exactly when every nonconstant quotient cycle has nonzero rotation displacement and the quotient periods are distinct.

**Proposition.** Let $p$ be prime and consider Rule 30 on the ring of $p$ cells. Rotation by one cell commutes with
the rule, so it permutes the cycles and preserves their lengths, and the orbit of a cycle under the rotation group
$\mathbb Z_p$ has size 1 or $p$. Hence a cycle whose length occurs fewer than $p$ times among all cycles is fixed by
rotation: rotation by one cell acts on it as some power of the time map (the pattern travels). In particular, when
all cycle lengths are distinct, every cycle is such a glider.

*Proof.* Commutation: both the rule and the rotation are defined by the same local function applied at every cell.
A group of prime order acting on a set has orbits of size 1 or $p$. A cycle fixed by rotation $\rho$ satisfies
$\rho(s) \in \{f^j(s)\}$ for a state $s$ on it, i.e. $\rho = f^j$ on the cycle. $\square$
