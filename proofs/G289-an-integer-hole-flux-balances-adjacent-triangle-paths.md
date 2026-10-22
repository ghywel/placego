# An integer hole flux balances adjacent triangle paths

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT289. An integer hole flux balances
adjacent triangle paths (second-read by Local, 2026-10-13)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Holes, two white squares side by side, are gained and lost with exact bookkeeping from one slanting path to the
next, but their number can rise or fall.

**What it says.** Suppose the middle column keeps its black-white beat for long enough, and a wide white stretch in
the left half shrinks into a white triangle. Paths slant from the triangle's black inner edge in to the middle, each
arriving just before a black beat; count each path's holes, leaving out the last pair, which records what the right
side must supply. On the next path, a tick later and a square further out, a new hole appears where there was none
exactly when the two squares just beyond the old pair were both black, and an old hole survives exactly when both
were white. So the count changes by exactly holes made minus holes lost inside the path; the ends add nothing,
thanks to the triangle's edge (proof G287) and the black beat. On one real example, a white stretch starting 125
squares out, the count went 26, 31, 26 on three paths in a row.

**Why it matters.** A proof that the beat cannot last for ever could use a meter that only moves one way. This gives
the hole count exact bookkeeping, then shows that on its own it is no such meter. It does not show that the beat
fails or rule out richer meters, and the return to 26 is gains and losses cancelling in one finite example, not the
whole pattern coming back round.

**An everyday picture.** A bus's passenger count: from stop to stop it changes by exactly those who got on minus
those who got off, yet it can climb from 26 to 31 and fall back to 26. Unlike the mileage counter on the dashboard,
it cannot tell you how far the bus has come.

## The formal statement and proof

**PROVED, Local L690 at92e87905.** Source: RULE30-GPT.md GC1205, under G288's actual triangle and horizon. The integer change of the spatial hole after shifting by one time and one outward depth is Delta=AB-h(A+B), where h=(1-C)(1-D) and A,B are the outward cells. If h0 this is AB; if h1 the new hole is(1-A)(1-B), giving AB-A-B. Summing over adjacent paths and using the old black guard makes the terminal Delta=-q_old. Hence J_(a+1)-J_a is the sum of the strict interior signed changes, where J excludes the terminal visible hole. The first change is0 from G287's entry packet.

GC1205's fixed actual125 fixture has J26->31->26 at consecutive a0/1, and31->29 at a8, with direct counts matching creations minus destructions. Thus a proposed monotone cost using J alone is refuted. This is a finite counter, not a repeatable full-state cycle or an impossibility for richer costs. Registered controls in rule30_zero_triangle_hole_flux.py retain the failed prediction. L690 hand-reads the signed law and terminal cancellation, adopts the fixed counts as tier1 and checks the recoding scope.
