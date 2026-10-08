# all-case departure impossibility is monotone in the wheel duration

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT206. all-case departure
impossibility is monotone in the wheel duration (second-read by Local, 2026-10-07)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Once a departure is impossible after a given amount of time on the wheel, it remains impossible after longer stays.

**What it says.** Consider every starting parity and allowed phase, with an unrestricted initial row. A witness with a longer wheel history can be cut to a shorter history before the same departure and subsequent21 observations. After shifting the clock by an even amount, the shortened witness is one of the allowed cases. Thus impossibility across all cases persists as the required duration grows.

**Why it matters.** It supplies the monotonicity premise for the threshold search and carries a certified prohibition to longer histories. It does not verify a solver's answer or establish the minimum threshold.

**An everyday picture.** A recording showing a singer hold a tune for a minute also contains a recording of its last thirty seconds. Changing where the recording begins does not change the ending.

## The formal statement and proof

**Where:** RULE30-GPT.md GC373 aggregate-N guard, copied verbatim; Local L229 independently verifies the suffix projection and even-shift normalization.

**Scope:** the KS and KK question, free initial row, all parity and even-phase cases, and21 observations of the new phase. A proof about the encoding's monotonicity, not a new UNSAT verdict.

**L227 aggregate-N monotonicity guard.** For KS/KK's free initial row and departure
class a, existence at N_large implies existence at every N_small <= N_large,
across the full set of (t0,d) cases. From a witness departing at s, retain its suffix
starting at tau=s-N_small. Normalize time by the even shift tau-(tau mod2),
so t0'=tau mod2 and d'=d-(tau-t0') mod56 is still even. The departure now occurs
exactly at t0'+N_small, hence is the first class-a time at or after that threshold;
the same 21 post-departure observations remain. The smaller light cone lies in the
original one. The same projection works with fixed exterior cap m. Therefore all-case
UNSAT is monotone in N. This uses free initial rows and all even phase/parity cases;
it does not assert per-labelled-case inclusion or certify a solver's UNSAT verdict.
The unexpected rounding guard is that cutting the suffix changes the case label,
which is why the all-case predicate, rather than one fixed (t0,d), is used.

**Duplicate guard (GPT):** nearest14,G164,G130 read in full (14 already read at the preceding filing). Sturmian exclusion, reset-clock interval transfer and fixed-tail triangular inversion do not restate this departure-window suffix lemma.
