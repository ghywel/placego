# column2 sources require switches and leave two dyadic endpoints

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT225. column2 sources require
switches and leave two dyadic endpoints (second-read by Local, 2026-10-08)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A neighbouring pair can send a selected signal only when the first column changes its effective beat.

**What it says.** On the second source column, an active pair at an even time forces a switch in the first column. For the specified empty-left rhythm, the preceding timetable shrinks to two endpoints. At the smallest exceptional scale there is only one endpoint.

**Why it matters.** Actual update equations remove most of the coefficient-selected possibilities. Farther columns and whether the remaining pairs activate still need checking.

**An everyday picture.** A timetable offers several departures, but a gate opens only at two of them. Those are the departures still possible; an open gate does not guarantee a passenger.

## The formal statement and proof

**Where:** RULE30-GPT.md GC447 at c548593; Local L263 in 6da6597 verifies the actual product implication, G26 specialization and coincident-endpoint guard. The source statement and proof are copied verbatim below. GC446 is now G224, independently read by L262; G61-G62 supply the local equations.

**Prediction before controls.** In any full0101 wall orbit, V_(2*n)(2)=1 implies s_(n+1)=1-s_n, where s_n=x_(2*n)(1). For G26's empty initial left row, at target T=2^K+1 with K>=3, combining this restriction with GC446 leaves only source times2 and2^K-2 on column2. Counterfactual: every effective switch forces the product. Unexpected check: K=2 makes the two proposed endpoints coincide, so it must be handled as one term rather than two XOR copies.

**Boolean proof.** Write b=x_(2*n)(2), q=x_(2*n)(3), d=x_(2*n+1)(1), c=x_(2*n+1)(2). G61-G62 give

`d=(1-s)*b`, `c=s XOR ((1-b)*q)`, `s_next=1 XOR ((1-d)*c)`.

If the actual source product b*q is1, then b=q=1. Hence d=1-s, c=s, and s_next=1 XOR s=1-s. Thus the product vanishes at every even time whose effective s does not switch. This works for every compatible left row under the full0101 wall, not only the empty-left specialization. The implication has no converse: at s=0,b=1,q=0, the equations still give d=1,c=0,s_next=1 but b*q=0. GC425's q=1 patches show both switch directions permit a product locally; that is not full-right sufficiency.

**Exact dyadic specialization.** G26 gives s_0=1 and s_n=floor(log2(n)) modulo2 for n>=1. Its switch indices are n=0 and n=2^j-1 for j>=1. GC446 selects column2 times t=2^K+2-2^h, h=2..K, so n=t/2=2^(K-1)+1-2^(h-1). The endpoints h=K and h=2 give n=1 and n=2^(K-1)-1. For K>=4, all interior h=3..K-1 give

`2^(K-2)+1 <= n <= 2^(K-1)-3`.

This lies strictly inside a single G26 constant run, so no product can occur there. For K=3 there are no interior samples. Consequently the actual column2 contribution to the odd centre Duhamel sum is exactly

`V_2(2) XOR V_(2^K-2)(2)` for K>=3.

At K=2 the only selected time is2, giving V_2(2) once. This says nothing about whether either endpoint is active; all other source columns must still be retained. Combining with the finite-support homogeneous-zero condition of GC446 leaves a whole-source parity certificate, not a two-event certificate.

**Duplicate guard for G225:** actual nearest G224,G215,C2 read in full. G224 supplies candidate times and G215 the entire cone parity. C2 is a Rule30 white-wall latch, a different rule and hypothesis. G62 is also credited: its source is column1, whereas this entry restricts the actual product on column2 and prunes the G224 stencil.

**Scope:** the switch implication holds under every full0101 wall; the two-endpoint specialization requires G26's empty initial left row. Every other source column remains. Local patch compatibility does not imply a full clock or active endpoints.
