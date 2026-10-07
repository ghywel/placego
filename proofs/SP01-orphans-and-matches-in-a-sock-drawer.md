# Orphans and matches in a sock drawer

*Proofs from the sparks. Derived from [PROOFS.md](../PROOFS.md), entry "SP01. Orphans and matches in a sock drawer
(SPARKS.md SC2; 2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary
in [summaries.md](summaries.md), never this file.*

**Status:** proved by Cloud and second-read by GPT, who counted independently and enumerated.

## In plain words

How many odd socks a laundry loss leaves, and how long a wait for a matching pair takes.

**What it says.** A drawer holds n matched pairs. If k socks go missing at random, the number left without their
partner (orphans) is k(2n − k)/(2n − 1) on average. Two socks pulled out at random match with chance 1/(2n − 1), so
someone who pulls two at random from a full drawer each morning waits 2n − 1 mornings on average for a matching
pair. A drawer of identical black socks never strands one while two remain. Cloud proved it by counting; GPT
counted again a different way and checked every small case exactly.

**Why it matters.** It came from the owner's break-room story about socks, and shows the room's chatter becoming a
checked result. GPT's reading also marks where it stops: the waiting time assumes the drawer is refilled every
morning, and with two pairs and no refill a match before the drawer empties has only a one-in-three chance.

**An everyday picture.** Ten pairs of patterned socks in a drawer, two grabbed in the dark each morning: about once
in nineteen mornings they match.

## The formal statement and proof

*Where:* SPARKS.md SC2 and GPT's second-reading note there; `tests/probes/sparks/sc2_socks.py` (simulation) and
`tests/probes/sparks/sc2_gpt_audit.py` (exact enumeration). *Bears on:* nothing in the prize; the break-room entry
on socks (Gareth). *Status:* proved by Cloud and second-read by GPT, who counted independently and enumerated
exactly.

**Proposition.** A drawer holds $n \ge 1$ matched pairs of socks.

1. If $k$ of the $2n$ socks are lost, all $k$-subsets equally likely, the expected number of surviving socks whose
   partner was lost (orphans) is $\dfrac{k(2n-k)}{2n-1}$.
2. Two socks drawn at random from the full drawer match with probability $\dfrac{1}{2n-1}$. So if every morning two
   socks are drawn independently from the full, replenished drawer, the first matched pair comes after a geometric
   number of mornings with mean $2n-1$.
3. If all the socks are interchangeable, no sock is without a possible partner while at least two remain.

*Proof.* (1) A given sock survives with probability $(2n-k)/(2n)$. Given that it survives, the lost socks form a
uniform $k$-subset of the other $2n-1$, which contains its partner with probability $k/(2n-1)$. By linearity of
expectation over the $2n$ socks, the mean number of orphans is
$2n \cdot \frac{2n-k}{2n} \cdot \frac{k}{2n-1} = \frac{k(2n-k)}{2n-1}$. (2) Whatever the first sock, the second is
uniform among the other $2n-1$, exactly one of which is its partner. Mornings are independent with success
probability $p = 1/(2n-1)$, so the first match comes on morning $m$ with probability $(1-p)^{m-1}p$, and the mean is
$1/p = 2n-1$. (3) Any two remaining socks make a pair. $\square$

*GPT's independent count (second reading).* Each orphan is the surviving half of exactly one split pair, so the
orphans are counted by the split pairs. A given pair is split with probability
$\binom{2n-2}{k-1} \cdot 2/\binom{2n}{k} = \frac{k(2n-k)}{n(2n-1)}$, and the $n$ pairs give the same mean. GPT noted
that losing $k$ socks and losing $2n-k$ leave the same orphan mean (a pair is split by a set exactly when it is split
by the set's complement), that $k = 0$ and $k = 2n$ leave none, and that $k = 1$ leaves exactly one, with no spread.
GPT's exact enumeration checked every loss count for $n \le 6$ (48 cases, 5,460 subsets) and every two-sock draw in
those drawers (161 draws).

*Scope (GPT's note).* The mean wait in (2) needs independent draws from the full drawer. Without replenishment it
fails: with two matched pairs, a mismatched first draw leaves a mismatched second, so a match before the drawer
empties has probability only $1/3$. In (3), having a possible partner is not being paired: three interchangeable
socks each have a possible partner, yet one is left over in any pairing.

*Measured as well (SC2).* In 200,000 simulated trials for each $n \in \{5, 10, 20\}$ and $k \in \{1, 3, 5, 10\}$, every
orphan mean lay within 2.5 standard errors of (1), and the mean waits were 8.97, 19.02 and 38.61 mornings against 9,
19 and 39.
