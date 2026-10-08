# isolated effective ones exclude even column2 bits

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT231. isolated effective
ones exclude even column2 bits (second-read by Local, 2026-10-08)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The incoming and outgoing gates demand a one-beat visit that the clock never makes.

**What it says.** A positive-time even column2 bit can be black only if three consecutive effective inputs are010. The empty-left clock has no such isolated positive one. Its longer initial prefix also removes the time-zero bit, so this even track is entirely white.

**Why it matters.** The predecessor theorem then removes every even column4 source, extending the earlier removal at particular observation times. Farther columns remain uncontrolled.

**An everyday picture.** A visit needs arrival immediately followed by departure. A timetable in which every visit lasts at least two beats cannot supply that one-beat slot.

## The formal statement and proof

**Where:** RULE30-GPT.md GC458 at68211fa; Local L269 in78576a7 independently verifies the incoming/outgoing gate composition, G26 run lengths and G229 initial exceptions. Source statement and proof copied verbatim below. Write b_n=x_(2n)(2) and s_n=x_(2n)(1).

**Proof.** Let n>=1 and b_n=1. G228 applied at even time2n-2 gives s_(n-1)=0 and s_n=1. Hence s_n*b_n=1, and G62 applied at time2n gives s_(n+1)=0. This is the claimed isolated effective one. Both lemmas are general-left statements; G26 enters only next.

For the empty-left clock, G26 has s_0=1 and s_n=floor(log2(n)) mod2 for n>=1. Its positive-index one-runs are exactly the intervals [2^(2r+1),2^(2r+2)-1], r>=0, whose lengths are2^(2r+1)>=2. Thus no one at n>=1 is isolated between two zeroes. The initial isolated one at n=0 has no preceding index and is outside the positive-time implication. Therefore x_(2n)(2)=0 for every n>=1.

G229's eight-bit prefix certificate separately fixes the initial positive bits1..7 to seed{1,5,7}, so x_0(2)=0 as well in every empty-left full0101 orbit. Combining the two statements gives x_(2n)(2)=0 for every n>=0. By G226 at j=2, every even-time column4 product V_(2n)(4) with n>=1 is also0: it would require the now-absent even bit x_(2n-2)(2)=1. This strengthens G228's dyadic-target pruning to all positive even source times. The initial V_0(4)=0 follows separately from G229, since its initial bit4 is0. Hence column4 contributes nothing to any odd centre target in this family. No assertion about farther even columns follows.


**Duplicate guard for G231:** actual nearest G228,G230,G226 read in full; G225 from the initial duplicate pass also read. G226 supplies the universal product predecessor, while this entry first removes its entire even column2 bit track. G228 supplies the incoming up-gate and coefficient-specific column4 removal; G230 removes later odd column1 gates; G225 constrains column2 products at effective switches. This composition adds the outgoing G62 down-gate, removes all positive even column2 bits in G26, and extends the column4 source removal to every even time with the stated initial certificate.

**Scope:** general-left orbits require the isolated010 triple for positive-time even column2 bits. Identical whiteness and all even column4 product removal use the empty-left full0101 family. Farther source columns remain open; no finite-witness exclusion follows.
