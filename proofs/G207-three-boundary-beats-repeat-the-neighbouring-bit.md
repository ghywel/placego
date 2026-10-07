# three boundary beats repeat the neighbouring bit

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT207. three boundary beats
repeat the neighbouring bit (second-read by Local, 2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Three specified beats on one column make a neighbouring bit repeat two steps later.

**What it says.** If one column reads white, black, black on three consecutive rows, and its right neighbour begins white, that neighbour has the same bit on the following row and two rows later. The cells farther right cannot change this equality.

**Why it matters.** It explains why two apparently free choices next to the wheel move together. It provides a local reason for a correlation that was first found by checking a finite graph. It does not decide whether their shared value is black or white.

**An everyday picture.** Two switches that appear independent but move together because of a connecting rod. Seeing the connection explains their agreement without telling you which position they will occupy.

## The formal statement and proof

**Where:** RULE30-GPT.md GC385; source `tests/probes/lexicon/rule30_locked_small_pair.py` at b7ac136. Independent hand and eight-case second reading: Local L237 at8181a7f, verified in594f714.

**Scope:** a local Rule30 identity, not a prize theorem. The following proof and premise control are copied verbatim from GC385.

**Local lemma.** Suppose column4 at times t,t+1,t+2 is0,1,1, and column5(t)=0.
Then column5(t+1)=column5(t+3), regardless of the right exterior.
Write r=column6(t), s=column7(t), z=column7(t+1). Rule30 gives

    a=column5(t+1)=r,
    b=column6(t+1)=r OR s,
    c=column5(t+2)=1 XOR(a OR b),
    e=column6(t+2)=a XOR(b OR z),
    d=column5(t+3)=1 XOR(c OR e).

If r=1, b=1,c=0,e=0,d=1. If r=0 and s=1, then b=1,c=0,e=1,d=0.
If r=s=0, then b=0,c=1 and d=0 regardless of e=z. Hence d=r=a.
**No assumption that the middle column5 bit is zero is needed.** The earlier
GC384 two-row analysis missed the preceding row, not a distant column13 input.
Independent literal scalar evaluation of all8(r,s,z) choices PASS. Unexpected
premise control: relaxing column5(t)=0 to1 permits unequal endpoints, for
example(h,r,s,z)=(1,1,0,0) gives1 then0. That is a control for the local equations
with externally prescribed column4, not a claimed wall-compatible trajectory.


**Finite wheel corollary (conservative).** In the width12 phase core, column4 at phases11..13 is011 and column5 at11 is0. G205's71-round finite-path lemma therefore supplies these premises in a145-observation wheel window centred at phase12: its phase11 and13 vertices are71 edges from the nearer endpoint. The local identity then equates column5 at phases12 and14. This uses the recorded wheel U at even phase with the period-two wall; either common value remains possible at width13. The bound is sufficient, not minimal. Local L237 independently checked these margins and reported a shorter25-row premise certificate; RV2 reported a19-row paired-path certificate. Those sharper numerical thresholds are not needed for this corollary.

**Duplicate guard:** nearest G142,14,C1 from the G205 neighbourhood were read in full. Compact support, Sturmian exclusion and the black-wall checkerboard do not restate this011-boundary temporal identity. G205 is cited for the transfer lemma, not refiled. The existing C2/entry03 white-boundary latch is an ingredient of the first update, not the three-step equality.

**Final nearest-entry check for G207:** the actual G207 query returns G205,17,E3, each read in full. G205 supplies a cited finite-window induction; Jen's periodic-left obstruction and E3's equality of relaxed hole languages do not state the local011-boundary identity. No proof is refiled.
