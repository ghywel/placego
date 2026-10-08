# even column3 detects effective switches

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT233. even column3 detects effective
switches (second-read by Local, 2026-10-08)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md
and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The third column marks the switches of the prescribed effective stream.

**What it says.** In the empty-left alternating-clock family, even column3 is white exactly at effective switches. Combining this with the two-step readout gives an exact formula for even column5 from three consecutive effective inputs, including the initial boundary.

**Why it matters.** These tracks are determined without enumerating entire right seeds. They provide explicit inputs for farther predecessor arguments while leaving whole-right uniqueness open.

**An everyday picture.** A lamp marks whether two consecutive timetable entries agree. A second lamp reads a combination of three entries; neither lamp tells us the whole timetable beyond them.

## The formal statement and proof

**Where:** RULE30-GPT.md GC461 at4f50bea; Local L271 at4ff97a2 verifies both track formulae including n=0, reaffirmed L272 at572eb5e. Source proof copied verbatim below. G232 now supplies the source's pending GC459 dependency, making both formulae unconditional within the stated empty-left full0101 family. Write q_n=x_(2n)(3), z_n=x_(2n)(5) and s_n=x_(2n)(1).

**Proof of the column3 formula.** In G61 notation put b_n=x_(2n)(2), d_n=x_(2n+1)(1), c_n=x_(2n+1)(2). G231 proves b_n=0 at every n>=0 in this family, including time0 through G229. Hence d_n=(1-s_n)*b_n=0 and c_n=s_n XOR q_n. G61's next-white-time equation is s_(n+1)=1 XOR ((1-d_n)*c_n)=1 XOR s_n XOR q_n. Solving over the two-element field gives q_n=1 XOR s_n XOR s_(n+1). Therefore q_n=0 exactly when s_n differs from s_(n+1), and otherwise q_n=1. No condition on farther right bits was imposed. This determines the track uniquely from the known effective stream, but says nothing about existence or uniqueness of an entire right realization.

**Conditional column5 formula.** GC459's proposed readout is q_(n+1)=s_n XOR z_n. Combining it with the just-proved formula at n+1 gives z_n=1 XOR s_n XOR s_(n+1) XOR s_(n+2). This use of GC459 remains pending its independent reading. It cannot be obtained merely by declaring the nonlinear correction zero without G231's product conclusion.


**Duplicate guard for G233:** actual nearest G232,G231,G225 read in full. G232 supplies the two-step readout; G231 removes the even column2 bit track; G225 only restricts source products to switches. Solving G61 now fixes the entire even column3 track and then column5, without assuming whole-right parity.

**Scope:** these necessary tracks hold for every member of the empty-left full0101 family, not merely G60's explicit parity-sparse member. They do not determine a whole right realization or exclude mixed-parity members. Initial s_0=x_0(1)=1 and x_0(5)=1 are separate prefix facts.
