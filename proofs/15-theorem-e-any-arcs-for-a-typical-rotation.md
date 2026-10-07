# Theorem E″ (any arcs, for a typical rotation number; added the same night)

*Windows, zero runs and the left band. Derived from [PROOFS.md](../PROOFS.md), entry "15. Theorem E″ (any arcs, for
a typical rotation number; added the same night)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved.

## In plain words

The same holds for almost every wheel speed, whatever pattern of marks it passes.

**What it says.** Theorem 14 used one mark; this allows any finite set of arcs as marks. For almost every rotation
speed, no such coding gives a finite left half.

**Why it matters.** It widens 14 from one simple kind of wheel to nearly all of them. The speeds left out are those
that never come close to repeating for long, such as the golden ratio; for some patterns of marks they are still
open (G132).

**An everyday picture.** Notches are how a wheel grips: like a ratchet's teeth, each one catches as it comes round
(the owner's reading). Here the notches are the ends of the marks, the only places where the wheel's near-repeating
rhythm can be broken. A finite seed needs that rhythm caught again and again, each catch coming within about twice
the time of the last. But a typical wheel sometimes coasts almost exactly round to where it was, for a very long
time, and then any fixed number of notches comes up too rarely: the wheel slips past the catch, and the seed is
exposed.

## The formal statement and proof

*Where:* RULE30-PRIZE.md, "8.57 No pure rotation works: every Sturmian column 1 is excluded (2026-10-05)". *Bears on:* the same for any arcs and a typical rotation number. *Status:* proved.

**Theorem E″ (any arcs, for a typical rotation number; added the same night).** Let $c_s = f(\theta + s\alpha)$,
where $f$ is 1 on a finite union of arcs with $r$ end points in all, and 0 elsewhere. If $\alpha$ has infinitely
many partial quotients larger than $2^{r+1}$, the forced left half is not eventually zero, for every $\theta$.
Almost every $\alpha$ has unbounded partial quotients, so for almost every rotation number **no coding by arcs at
all** can go with a finite left half. These sequences have complexity up to $r\,n$.

*Proof.* $c$ breaks period $q_n$ at time $s$ exactly when $x_s$ lies in one of $r$ arcs of length $|\delta_n|$, one at
each end point. Let $d_1 < d_2 < \dots$ be the break times. Step 0 on the stretch before $d_1$ and on each stretch
between consecutive breaks gives $d_1 \le q_n + C + 1$ and $d_{k+1} \le 2 d_k + q_n + C + 3$, so
$d_k < 2^k (q_n + C + 2)$. Two of the first $r + 1$ breaks belong to the same end point, and returns to an arc of
length $|\delta_n|$ are at least $q_{n+1}$ apart. So $q_{n+1} \le d_{r+1} < 2^{r+1}(q_n + C + 2)$, which fails
when $a_{n+1} > 2^{r+1}$ and $q_n$ is large. $\square$
