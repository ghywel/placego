# even column2 up-gates remove column4 dyadic sources

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT228. even column2 up-gates
remove column4 dyadic sources (second-read by Local, 2026-10-08)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The fourth column's candidate source times miss the required predecessor times.

**What it says.** Under the specified empty-left alternating wall, a black even-time bit in column2 needs an upward switch in the first column. A column4 source needs such a bit two ticks earlier. Its selected times never meet that schedule at the stated doubling scales.

**Why it matters.** It removes another entire column from the source certificate at those observation times. It leaves the third column and more distant sources unresolved.

**An everyday picture.** A shop can receive a delivery only after a connecting service arrives. Its delivery slots and that service's arrivals fall on different days, so those slots cannot be filled.

## The formal statement and proof

**Where:** RULE30-GPT.md GC452 at1408e56; Local L266 incec46a1 verifies the bit implication, timing, column4 coefficient intersection and both guards. Source statement and proof copied verbatim below. G226 supplies the universal predecessor obstruction; G224 and G26 give the coefficient and empty-left gate schedules.

**Bit implication.** At even time2n write the positive input(s,b,q,h,z). G61-G62 give d=(1-s)*b, c=s XOR ((1-b)*q), r=b XOR ((1-q)*h). The next even column2 bit is B=d XOR ((1-c)*r). If c=1 then d=0 (d=1 would force s=0,b=1,c=0), so B=0. If c=0 and s=1, then b=0,q=1; hence d=r=0 and B=0. Thus B=1 forces s=0,c=0. The intervening wall bit1 gives s_next=1 XOR ((1-d)*c)=1. This proves the required up-transition. No condition on h,z or the farther tail was imposed.

G26's up-transitions occur at n=2^(2r+1)-1, r>=0. Therefore B can be1 only at physical times2n+2=4^(r+1). This restricts even column2 bits from time2 onward; it says nothing about the initial bit x_0(2). It also does not assert that any allowed bit is1.

**Column4 consequence.** G226 at j=2 says V_t(4)=1 with t>=2 requires x_(t-2)(2)=1. At even source times t>=4, the preceding bit is an even column2 bit with positive time. Under the empty-left clock this restricts t to4^m+2, m>=1, all2 modulo4. At T=2^K+1, K>=3, G224 selects column4 exactly at t=2^K+4-2^h, 3<=h<=K. All these times are at least4 and are0 modulo4. The two lists are disjoint. Therefore column4's entire contribution at these targets is0. Odd source times have the wrong Pascal parity for this column.

This uses actual predecessor constraints, not an enlarged G63 forced window. It supplements G226's removal of column2 and G227's column3 timetable. Sources i>=5 remain, along with G227's possible column3 terms. The total source certificate cannot be replaced by a sum over the first four columns.

**Duplicate guard for G228:** actual nearest G227,G226,G225 read in full. G227 prunes column3 using odd column1 bits; G226 supplies the universal predecessor obstruction; G225 constrains column2 products. This entry instead constrains individual even column2 bits and removes the column4 coefficient timetable.

**Scope:** the bit implication needs full0101; its explicit timing and column4 removal need the empty initial left row. Initial sources are retained at the exceptional scale K=2. Column3 and sources i>=5 remain uncontrolled.
