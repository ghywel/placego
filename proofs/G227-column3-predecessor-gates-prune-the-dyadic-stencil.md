# column3 predecessor gates prune the dyadic stencil

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT227. column3 predecessor
gates prune the dyadic stencil (second-read by Local, 2026-10-08)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The next column has a short timetable inherited from its required past.

**What it says.** Under the specified empty-left alternating wall, column3 can contribute at an early time and, on alternate doubling scales, one later time. Its other candidate times are blocked by predecessor conditions.

**Why it matters.** It combines the exact coefficient timetable with actual update constraints. It still leaves more distant columns and whether permitted sources occur unresolved.

**An everyday picture.** A connecting train can run only after its feeder arrives. Intersect the two timetables and most of the departures disappear, even though they looked possible on the second timetable alone.

## The formal statement and proof

**Where:** RULE30-GPT.md GC450 at868b26b; Local L265 inc4b15eb verifies predecessor timing, both no-carry families and odd-K pruning. Source statement and proof copied verbatim below. GC449 is now independently reviewed G226; G61 supplies the empty-left odd-bit schedule.

**Predecessor timing.** By the contrapositive of GC449, any V_t(3)=1 with t>=2 requires x_(t-2)(1)=1. Odd centre targets select odd t on column3. G61's empty-left specialization permits an odd column1 bit only at times4^(r+1)-1, r>=0. Thus odd column3 sources can survive only at t=1, or t=4^(r+1)+1 for r>=0. The time1 exception has no two-step predecessor in the nonnegative-time orbit. This is a necessary temporal condition, not a sufficiency assertion.

**Column3 coefficient proof.** For odd lag l>=3 set a=(l-3)/2. Standard binary no-carry parity gives K_l(3)=1 iff a AND (a+3)=0. If a=2*b, this becomes b AND (b+1)=0, so b=2^j-1, j>=0, and l=2^(j+2)-1. If a=2*b+1, the condition becomes b AND (b+2)=0. Their common lowest bit must be0; write b=2*c. Then c AND (c+1)=0, giving c=2^j-1 and l=2^(j+3)-3. Conversely each listed value has disjoint summands. Hence the two disjoint lag families are l=2^h-1 for h>=2, and l=2^h-3 for h>=3.

At T=2^K+1, the selected times are respectively t=2^K+1-2^h (2<=h<=K) and t=2^K+3-2^h (3<=h<=K). Every time in the second family is3 modulo4, whereas every permitted predecessor-gated time is1 modulo4, so the second family contributes nothing. In the first family, h=K gives t=1. Otherwise a permitted time requires 2^K-2^h to be a positive power of4. Factor it as 2^h*(2^(K-h)-1); the odd factor is1 exactly when K-h=1, and the exponent h must be even. Thus the only late possibility is h=K-1 with K odd, yielding t=2^(K-1)+1.

The exact column3 contribution is therefore

`V_1(3)` when K is even,

`V_1(3) XOR V_(2^(K-1)+1)(3)` when K is odd.

This is conditional on GC449 and uses the empty initial left row for G61's specific gate schedule. A general compatible left stream has another gate schedule and is not covered by this specialization. No sum over only columns2-3 is justified.

**Duplicate guard for G227:** actual nearest G225,G226,G224 read in full. G225 concerns column2, G226 supplies the universal predecessor implication, and G224 treats dyadic source columns. This entry supplies column3's two lag families and their intersection with the empty-left predecessor gates.

**Scope:** both the universal G226 predecessor lemma and the empty-left full0101 gate schedule are required. Products remaining in the stencil are permitted, not asserted active. Farther columns remain in the full source sum.
