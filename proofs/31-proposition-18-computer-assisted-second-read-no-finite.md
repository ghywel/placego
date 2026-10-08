# Proposition 18 (computer-assisted, second-read): no finite Rule 210 seed with left support in -6 .. -1 keeps the 0101 clock

*Siblings, Jen and the squeeze. Derived from [PROOFS.md](../PROOFS.md), entry "31. Proposition 18
(computer-assisted, second-read): no finite Rule 210 seed with left support in -6 .. -1 keeps the 0101 clock";
rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** second-read (GC470).

## In plain words

Even with a few black cells allowed on the left, Rule 210 cannot keep its centre alternating from a finite starting row.

**What it says.** Allow any black cells within six places left of the centre. If one sits at an even distance, the alternating centre fails within six steps. If all sit at odd distances, there is exactly one way to continue on the right, and it is the coprime-to-6 pattern of entry 29 with a few cells mirrored, which never ends. So no finite starting row of this kind works.

**Why it matters.** It answers question B, whether a finite starting row can produce the alternating centre, for every left side of width up to six. Wider left sides remain open, because the check close to the centre does not carry over by symmetry.

**An everyday picture.** A melody that must keep a steady beat: a few extra notes at the start can be answered by adjusting a few notes on the other side, but the tune itself never ends, so no finite score keeps the beat.

## The formal statement and proof

*Where:* chat L277, L278; GC470; `tests/probes/lexicon/rule210_left_rows_census.py` (LB and its `iso` mode); GPT's
`rule210_gpt_left_base_audit.py`.
*Bears on:* PERIOD-TWO.md's Rule210 empty-left row (question B); entry 29; G27 (compatible left halves are
parity-sparse); G60 and G65 (the parity-sparse realizations).
*Credit:* G27, G60 and G65 are GPT's; the census of left rows, the observation that G65's seed agrees with $R$ beyond
the left radius, and the transfer of entry 29's window are Local's; the second reading, independent base certificates
and the smaller witness against a uniform base are GPT's (GC470). *Status:* second-read (GC470).

**Setting.** Rule 210 as in entry 29, now with a nonempty initial left row $L$ supported in $-6, \ldots, -1$ and every
other left site white. $R$ is entry 29's row (the sites coprime to 6).

**Proposition 18.** If $L$ has a black even site, no orbit keeps the clock $x_t(0) = t \bmod 2$. If $L$ is odd-supported,
the only orbit that keeps it starts from $L$ together with the right row $R \oplus \bar L$, where $\bar L$ marks the mirror
sites $-l$, $l \in L$. That right row is infinite, so no finite seed with left support in $-6, \ldots, -1$ keeps the clock.

*Proof.* The 56 rows with a black even site have no surviving right prefix at depth 6 (LB; GC470 independently), as
G27's parity classification predicts. For the 7 odd-supported rows, G65's realization is $L \cup (R \oplus \bar L)$: a
black pair at $-k$ and $+k$ evolves under Rule 90 and cancels at the centre by binomial symmetry. Its orbit is
parity-sparse, so every even diagonal is white everywhere, and it agrees with $R$ at every site beyond 6. For a first
deviation at a right site $e \ge 122$, each window cell ($s \le 48$) has its cone in sites $\ge 26$, where this
background is entry 29's periodic field, so entry 29's steps 3 and 4 kill the deviation unchanged. A first deviation
at $e \le 121$ is excluded by the exhaustive prefix certificate for that row (GC470 to 121; LB to 299). $\square$

*Scope.* Left support within radius 6 only. The census does not commute with the reflection near the wall (for
$L = \{-3\}$ the depth-3 survivors are $\{5\}$ against the reflected $\{3, 5, 7\}$), so no uniform base follows, and
question B for larger left rows stays open: a general statement needs a uniform near-wall argument or a certificate for
each radius.

*Second reader's note (GPT, 2026-10-08; GC470).* Verified as a computer-assisted corollary. Independent bases: each of
the 7 odd-supported rows has a unique compatible prefix through 121, equal to $R \oplus \bar L$; all 56 even-containing
rows die by depth 6; 1,792 scalar controls pass; the window at $e = 122$ starts at site 26, beyond every mirrored
correction.
