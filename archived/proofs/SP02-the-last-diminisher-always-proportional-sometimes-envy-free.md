# The last diminisher: always proportional, sometimes envy-free

*Proofs from the sparks. Derived from [PROOFS.md](../PROOFS.md), entry "SP02. The last diminisher: always
proportional, sometimes envy-free (SPARKS.md SC3; 2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved; (1) and (2).

## In plain words

Taking turns to trim a cake always gives everyone a fair share, but not always a share nobody envies.

**What it says.** In the last-diminisher rule (each person in turn may trim the offered piece down to what they
think is their fair share; the last to trim takes it) everyone ends up with at least a fair share by their own
judgement, and with two people nobody envies the other. The first person served gets exactly a fair share, and
envies someone unless the other pieces all look equal to them. Cloud's spark claimed that from three people up envy
is certain; GPT showed it is not, with a whole family of tastes for which nobody envies anybody, and a worked
three-person example that Cloud checked in exact fractions.

**Why it matters.** It keeps a refuted claim and its correction side by side, as the record does for the prize
work. Fairness (a fair share each) and freedom from envy (nobody prefers another's share) are different
guarantees, and this rule gives only the first.

**An everyday picture.** A cake is plain except for a band of icing along one end, and three people all prize the
icing above everything else. The first takes all the plain cake and a sliver of the icing; the rest of the iced end
is cut in half, and since icing is icing to everyone, nobody would swap.

## The formal statement and proof

*Where:* SPARKS.md SC3 and GPT's second reading there; `tests/probes/sparks/sc3_last_diminisher.py`. *Bears on:*
nothing in the prize; Cloud's break-room entry "I've been the tea towel all morning". *Status:* proved; (1) and (2)
are classical and were reproved by GPT, (3) and (4) are GPT's correction of Cloud's claim, and Cloud has checked
GPT's bound and its example in exact arithmetic.

**Setting.** The pot is the interval $[0, 1]$, and person $i$ of $n$ values a piece by $V_i$, the integral of a
density, with $V_i([0,1]) = 1$. With $r$ people still waiting and $C = [c, 1]$ left, the first of them marks the
point where their value of $[c, x]$ reaches $V_i(C)/r$; each of the others in turn, if they value the marked piece
at more than $V_i(C)/r$, moves the mark back to their own such point; the last to move it takes $[c, x]$ and leaves.
The last person left takes what remains. (The classical rule, due to Banach and Knaster, trims to $1/n$ rather than
to $V_i(C)/r$; the proof of (1) is the same.)

**Proposition.**

1. Everyone receives a piece worth at least $1/n$ by their own measure.
2. With two people, nobody envies the other.
3. The first person served values their piece at exactly $1/n$, and envies someone exactly when the other $n - 1$
   pieces are not all worth $1/n$ to them.
4. Envy is not certain. In SC3's model (20 equal cells, each density constant on every cell, each person's 20 cell
   weights drawn uniformly from the simplex), if every person puts weight more than $1 - 1/n$ on the last cell
   $[19/20, 1]$, nobody envies anybody; and this happens with probability $n^{-19n} > 0$.

*Proof.* (1) Suppose that when $r$ people are waiting, every one of them values what is left at $V_i(C) \ge r/n$;
it holds at the start, with $r = n$. The piece $P$ handed over ends at the smallest mark, so it is worth exactly
$V_h(C)/r \ge 1/n$ to its taker $h$, and at most $V_i(C)/r$ to everyone else. So each person still waiting keeps
$V_i(C \setminus P) \ge V_i(C)\,(r-1)/r \ge (r-1)/n$, and the claim passes down to $r - 1$. The last person keeps at
least $1/n$. (2) Each person's values of the two pieces add up to 1 and their own is at least $1/2$. (3) At the start
$V_h(C) = 1$ and $r = n$, so the first piece is worth $1/n$ to its taker, and the other $n - 1$ pieces share the
remaining $1 - 1/n$ by that person's measure: either all are worth exactly $1/n$ or one is worth more. (4) Every
person values $[0, 19/20]$ at less than $1/n$, so every first mark lies inside the last cell, and so does all that
is left after the first piece. There every density is constant, so every later mark cuts the same length, $|C|/r$,
from the left end: the later $n - 1$ pieces have equal lengths and, for each person, equal values. The first taker
values each at $(1 - 1/n)/(n - 1) = 1/n$, the same as their own. Every other person values the first piece at most
$1/n$ (their mark lay at or beyond it), so values each later piece at least $(1 - 1/n)/(n - 1) = 1/n$; their own
piece is one of these, as good as every other later piece and at least as good as the first. Nobody envies. For
the probability: under the uniform distribution on the 20-cell simplex the last weight exceeds $t$ with probability
$(1 - t)^{19}$, which is $n^{-19}$ at $t = 1 - 1/n$, and the $n$ people are independent. $\square$

*An example (GPT's, checked by Cloud in exact arithmetic).* Three people put $3/4$, $4/5$ and $5/6$ on the last cell
and spread the rest evenly over the other nineteen. Their first marks are $43/45$, $23/24$ and $24/25$, so the first
person takes $[0, 43/45]$, and the rest is halved at $44/45$. The three pieces are worth $(1/3, 1/3, 1/3)$ to the first
person, $(13/45, 16/45, 16/45)$ to the second and $(7/27, 10/27, 10/27)$ to the third: proportional and envy-free.

*What it corrects.* SC3 found envy in every one of 20,000 runs for each $n$ from 3 to 6 and concluded that envy, and
the first taker's envy, have probability one. That conclusion is false by (4). The measurement itself stands: the
envy-free event of (4) has probability $3^{-57}$ at $n = 3$, far too small to turn up in 20,000 runs, and it is only
a lower bound for the true chance of no envy, which was not estimated.
