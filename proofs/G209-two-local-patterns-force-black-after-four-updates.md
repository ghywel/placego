# two local patterns force black after four updates

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT209. two local patterns
force black after four updates (second-read by Local, 2026-10-08)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Two small initial patterns guarantee a black square four ticks later.

**What it says.** Under Rule30, either the seven-cell pattern0101110 or five specified cells in the pattern1110?1 guarantee that the fifth cell is black after four updates. Every unspecified initial cell may be chosen freely. The proof needs no blinking wall or wheel.

**Why it matters.** A short Boolean argument explains the final step of a correlation first found by exhaustive computation. Reaching either pattern from an earlier prescribed strip remains a separate computed obligation; this does not explain the wheel's eventual departure limit.

**An everyday picture.** A few correctly placed dominoes guarantee one particular fall, even though the rest of the arrangement is unknown. Establishing that those dominoes were placed correctly is a different job.

## The formal statement and proof

**Where:** RULE30-GPT.md GC401 at cc8f8bf, statement and proof copied verbatim below. Independent hand second reading and separate scalar controls: Local L244 at48480a9. The original pending-review sentence is retained as historical source text; L244 resolves it.

Setting: Rule30 update x'_j = x_(j-1) XOR (x_j OR x_(j+1)). Positions1..9 below are a translated local interval, not an assumption of a prescribed wall. All unspecified initial cells are arbitrary. Independent second reading pending.

Claim: after four updates, position5 is1 if initially either (A) positions1..7 are0101110, or (B) positions1,2,3,4,6 are1,1,1,0,1 (position5 and positions7..9 arbitrary). This is a local lemma; no wheel, long preparation or prize statement.

Proof A: let initial positions8,9 be d,e. After one update, positions2..8 are1,0,1,0,0,1-d,d OR e. After two, positions3..7 are0,1,1,1-d,1: the last entry is (1-d) OR d OR e. After three, positions4..6 are1,0,0. Hence the fourth update at5 is1 XOR (0 OR0)=1.

Proof B: write initial position5=b, a=x7 OR x8, q=x7 XOR (x8 OR x9). After one update, positions2..8 are0,0,1-b,1,1-b,1-a,q. After two, positions3..7 are1-b,1,b,b AND a,z, where z=(1-b) XOR ((1-a) OR q). After three, positions4..6 are b,1-b,b XOR ((b AND a) OR z). If b=0, the first two entries are0,1 and the next output is1 regardless of the third. If b=1, z=(1-a) OR q, so (b AND a) OR z = a OR (1-a) OR q =1 and the third entry is0; the first two are1,0, again giving output1. This proves B.

Controls: all20 assignments to the free positions of these two nine-cell patterns scalar-evolved to output1. Radius-one locality uses only positions1..9, so no wall value or exterior enters this four-update proof. The earlier eight wall values are needed to establish the reached cut restrictions from GC397's initial anchor, not for this local lemma.

**Review and application scope.** Local checked both case analyses line by line and all20 free assignments. Its independently encoded time8 bridge also verifies that all1504 antecedent-positive runs among4096 initial assignments under GC397's anchor match A or B. This latter assertion remains a finite census, separate from the unconditional hand lemma. No long wheel preparation or death127 theorem follows.

**Duplicate guard for G209:** actual nearest25,24,G208 read in full. Pulse source weights, arrival-phase debt and width15 wheel forcing do not restate either unconditional four-update pattern. This lemma fixes one output without any wall or periodicity assumption.
