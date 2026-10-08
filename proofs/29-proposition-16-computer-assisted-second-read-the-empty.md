# Proposition 16 (computer-assisted, second-read): the empty-left 0101 orbit of Rule 210 is unique

*Siblings, Jen and the squeeze. Derived from [PROOFS.md](../PROOFS.md), entry "29. Proposition 16
(computer-assisted, second-read): the empty-left 0101 orbit of Rule 210 is unique"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** second-read (GC467).

## In plain words

Rule 210 with an empty left half has exactly one way to keep its centre alternating: start from the sites that share no factor with 6.

**What it says.** Fix every cell left of the centre white and ask the centre to read white, black, white, black for ever. Then the starting row on the right must be black exactly at 1, 5, 7, 11, 13, ..., the numbers coprime to 6. That row works (its centre counts are odd numbers of the form (2^n + 1)/3), and no other row does.

**Why it matters.** It settles a whole family that a long chain of GPT's lemmas had been narrowing column by column: there is only one member, and it is a plain Rule 90 pattern. It also shows that no finite starting row with an empty left half can keep this clock. It says nothing yet about rows with something on the left, or about Rule 30.

**An everyday picture.** Think of a row of dominoes where any wrong piece, placed anywhere, topples into the centre within three more pieces. Checking that once for each of six positions in the repeating pattern, plus the first 121 pieces by hand, leaves room for only one arrangement.

## The formal statement and proof

*Where:* chat L270, L272, L274; GC466, GC467; `tests/probes/lexicon/rule210_two_step_review.py` (TS),
`rule210_census_lag.py` (CL), `rule210_uniqueness_automaton.py` (UQ and its `cross` mode); GPT's
`rule210_gpt_base_certificate.py`.
*Bears on:* PERIOD-TWO.md's Rule210 empty-left row; G60 (existence), G26 (the left half), G226 to G233 and GC462 (all
of which hold in this family because it is one Rule 90 orbit).
*Credit:* existence and uniqueness among odd-supported seeds are GPT's G60; the closed form, its Jacobsthal proof, the
diagonal reduction, the census and the automaton are Local's; the second reading, an independent base certificate
to site 121 and an independent check of the deviation graph are GPT's (GC466, GC467). *Status:* second-read (GC467).

**Setting.** Rule 210 is $x' = \ell \oplus (1 - c)\,r$. Take $x_0(i) = 0$ for every $i \le 0$ and require the centre
clock $x_t(0) = t \bmod 2$ for every $t \ge 0$. Let $R(i) = 1$ exactly when $i \ge 1$ and $\gcd(i, 6) = 1$.

**Proposition 16.** The initial row of every such orbit is $R$. In particular no finite seed with an empty left half
realizes the 0101 clock.

*Existence (closed form).* Every site in $R$ is odd, so at $t = 0$ black cells sit only where $t + i$ is odd. Then
adjacent cells are never both black, $(1 - c)\,r = r$, and the orbit is Rule 90 (G26's parity argument, run over the
whole line); even times leave the centre white. At $t = 2m + 1$ the centre is the sum of $\binom{2m+1}{j}$ over
$m + 1 \le j \le 2m + 1$ with $j \not\equiv m + 2 \pmod 3$. That index condition is invariant under $j \mapsto 2m + 1 - j$,
and the trisection formula gives the excluded class the total $(2^{2m+1} - 2)/3$, so the centre is
$(2^{2m+1} + 1)/3$, an odd (Jacobsthal) number. This is G60's seed for the 0101 wall, in closed form.

*Uniqueness.* (1) Diagonals: with $D_c(s) = x_s(c - s)$, the rule reads
$D_c(s+1) = D_{c-2}(s) \oplus (1 - D_{c-1}(s))\,D_c(s)$, with $D_c(0) = x_0(c)$ and the clock $D_c(c) = c \bmod 2$; a
window $s \le L$ is closed under this recurrence. (2) Background: every even diagonal of $R$'s orbit is white for all
$s$, and for $s \le (c - 1)/2$ the orbit agrees with the periodic field $x_s(i) = [i + s \text{ odd}]\,[3 \nmid i]$, so
inside such a window it depends only on $c \bmod 6$. (3) Let a member first differ from $R$ at site $e$ and write
$\Delta_c$ for the deviation of diagonal $c$. An even diagonal whose deviation is 0 at $s = L$ stays 0 beyond $L$ when
the even diagonal two before it does; an odd diagonal's deviation is constant beyond $L$ when its two predecessors
vanish there, because $R$'s even diagonal before it is white all the way to the wall. So the clock at time $c$ holds
exactly when $\Delta_c(L) = 0$ for odd $c$. (4) With $L = 48$ and $e \ge 2L + 24$, the finite deviation automaton on
states $(c \bmod 6, \Delta_{c-1}[0..L], \Delta_c[0..L])$, explored over every choice of every later site, has no
irregular state (an even diagonal ending the window with $\Delta = 1$), nine deviated surviving states, no cycle and no
return to zero; every deviated path dies within three more diagonals. (5) For $e \le 121$ the exhaustive prefix
census forces $R$ (GPT's base certificate to 121; Local's census to 1200). $\square$

*Scope.* Rule 210 with the empty left half and the 0101 wall only. Question B for a nonempty finite left row remains
open, and nothing here transfers to Rule 30 without its own argument. Checks: UQ reproduces the census's tail sets; a
background shifted by one site is refused (32 irregular states); direct simulation at sites 601 to 612 matches the
automaton's kill time in all 192 cases.

*Second reader's note (GPT, 2026-10-08; GC466, GC467).* An independent exploration of the deviation graph from all
six first-deviation residues finds no irregular endpoint, no return to zero and no cycle, with every surviving
deviated path at most three vertices long. An independent exhaustive certificate through 121 (depth 120 still has two
survivors) supplies the base, and the light-cone argument covers every tail. Verified as a computer-assisted proof.

*Later scope update (GPT, GC482).* Proposition19 in entry32 now covers every finite left row by hand, so this empty-left computer-assisted proof is a special case. The open-status wording above is historical.
