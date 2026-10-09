# G traces never contain 000001101

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT267. G traces never contain
000001101 (second-read, 2026-10-09)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this
summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A column of Rule 30, read in its light-speed frame, can never show the nine-beat pattern five whites, two blacks, a white, a black.

**What it says.** A computer search had found that this short pattern never occurs. Here is the reason. Working backwards from the first black beat pins down where the nearest black cell must have started, and in both possible places a forced white beat lands exactly where the pattern needs a black one.

**Why it matters.** Two earlier arguments about a hypothetical repeating pattern relied on this pattern being forbidden. Now that rests on proof instead of a search.

**An everyday picture.** A ripple arriving at the shore at a fixed speed: once you know when its front arrived, you know exactly which later moments must be calm.

## The formal statement and proof

*Where:* RULE30-GPT.md GC841 (front normalization from GC840). *Credit:* GPT's proof of a word that Local's census
measured as a minimal forbidden G-trace word of length 9 (L426, exhaustive over every 17-bit cone). Independently
read by Local (chat L463). *Status:* hand proof verified by a second reader; it agrees with the census. Not a prize
claim. *Filed by:* Local, at GPT's request (GC841).

**Statement.** No temporal profile of any forward G orbit, with $G(x)_i = x_i \oplus (x_{i+1} \lor x_{i+2})$, contains
the nine-tick word 000001101.

**Proof.**
1. Zero the irrelevant negative half-row; G reads only right neighbours. Let J be the first black at the start.
   The front moves left two places a tick (GC838). In the normalized digits $z_k(n)$ at distance k from the front,
   GC840 proves:
   - $z_2(n) = 0$ for n >= 2;
   - $z_4(n) = 1$ for n >= 4;
   - $z_5$ alternates from tick 5.
2. Put $A_n = z_5(n)$, $B_n = z_6(n)$, $C_n = z_7(n)$, so that $A_{n+1} = 1 - A_n$,
   $B_{n+1} = \lnot(A_n \lor B_n)$ and $C_{n+1} = A_n \oplus (B_n \lor C_n)$.
   - If $A_5 = 1$: then $B_6 = 0$, $B_7 = 1$, $A_7 = 1$, and $C_8 = 0$.
   - If $A_5 = 0$: then $C_7 = 1 \oplus ((1-b) \lor b \lor c) = 0$, $B_7 = A_7 = 0$, and $C_8 = 0$.
   So $z_7(8) = 0$ in every case.
3. The word's first black at tick 5 gives J in {9, 10} (GC838).
   - J = 10 makes tick 6 equal to $z_2(6) = 0$.
   - J = 9 makes tick 8 equal to $z_7(8) = 0$.
   Both contradict the word. ∎

*Scope (GC841).* G does not commute with complementation, so the complementary word is not covered. The longer
measured word 0001101011 (GC827's h >= 4 branch) is not proved here. This proof makes GC830's U10 <= U6 and GC827's
h = 2 case exact consequences.

*Near-entry gate (Local, at filing).* `--near G267` gives G261, E3 and G141 (all <= 0.08 on the formal text), read;
none is restated. Its companion is G.GPT258 (four shorter forbidden G-trace words). Hard checks pass.
