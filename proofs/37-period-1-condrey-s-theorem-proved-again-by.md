# Period 1 (Condrey's theorem, proved again by hand, second-read): no finite seed has an eventually constant column

*Siblings, Jen and the squeeze. Derived from [PROOFS.md](../PROOFS.md), entry "37. Period 1 (Condrey's theorem,
proved again by hand, second-read): no finite seed has an eventually constant column"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** Cloud's proof (RULE30-PRIZE.

## In plain words

A finite pattern in Rule 30 can never leave one column fixed for ever, black or white.

**What it says.** Start with finitely many black cells and run Rule 30. No single column can settle into always black or always white. If it stayed black, the rule would force a black-white stripe pattern running off to the left for ever, needing infinitely many black cells. If it stayed white, a black cell from the right walks in, sticks beside it, and forces the same endless stripes. Either way the finite start is contradicted.

**Why it matters.** This is the first case, period 1, of the question Wolfram asks: can the centre column ever settle into a repeating pattern? Condrey proved this case in 2026. Our team had cited it; here it is written out and checked twice by hand. The proof also shows exactly where the right side of the pattern is needed, which matters for the harder period-2 case.

**An everyday picture.** A row of dominoes that must alternate standing and fallen: fix one domino for ever and the alternation runs off to the horizon, but a finite set of dominoes has no horizon to fill.

## The formal statement and proof

*Status:* Cloud's proof (RULE30-PRIZE.md §8.76, CL083, 2026-10-09), second-read by Local (chat L417, 2026-10-09). Not
new and not a prize claim: it restates Condrey's theorem (arXiv:2609.09431; PRIOR-ART.md), which the record had cited
but not audited in full (PRIOR-ART.md 2026-10-04, GPT's G11, §5's check A). Filed at the owner's request, through the
near-entry gate.

**Theorem (Condrey).** No nonzero finite configuration of Rule 30 has an eventually constant column.

**Proof.** Rule 30 read for its left input is $x_t(i-1) = x_{t+1}(i) \oplus (x_t(i) \lor x_t(i+1))$, so columns 0 and
1 over $t \ge s$ fix every column to their left over $t \ge s$.
*Edges.* If $E$ is the rightmost black cell of row $t$, cell $E + 1$ of row $t + 1$ is $1 \oplus 0 = 1$ and every
cell beyond it is 0, so the rightmost black cell moves one cell right each step. At the leftmost black cell $L$,
cell $L - 1$ becomes $0 \oplus (0 \lor 1) = 1$ and nothing further left is black. So a finite nonzero row stays
finite and nonzero, and a time shift keeps the hypothesis. By shift invariance take column 0 equal to $c$ for every
$t \ge 0$.
*Black wall, $c = 1$.* $x_t(-1) = 1 \oplus (1 \lor x_t(1)) = 0$ whatever column 1 is. For $j \ge 2$ the left-input
form gives $0 \oplus (0 \lor 1) = 1$ at even $j$ and $1 \oplus (1 \lor 0) = 0$ at odd $j$, by induction on $j$, at
every $t \ge 0$. Row 0 then has infinitely many black cells, a contradiction.
*White wall, $c = 0$.* If every black cell of row 0 lay at a site $\le 0$, its rightmost one $E_0 \le -1$ would
reach column 0 at time $-E_0$. So some black cell lies at a site $\ge 1$. Let $a_t$ be the leftmost one. While
$a_t \ge 2$, sites $1, \dots, a_t - 2$ stay white ($0 \oplus 0$, column 0 being white) and site $a_t - 1$ turns black
($0 \oplus (0 \lor 1)$), so $a_{t+1} = a_t - 1$. Column 1 is black at $t_1 = a_0 - 1$, and
$x_{t+1}(1) = 0 \oplus (x_t(1) \lor x_t(2)) \ge x_t(1)$ keeps it black. From $t_1$ on, columns 0 and 1 read white,
black, so $x_t(-1) = 0 \oplus (0 \lor 1) = 1$, $x_t(-2) = 1 \oplus (1 \lor 0) = 0$, and the same induction makes
every odd depth black. Row $t_1$ is then infinite, a contradiction. ∎

*Remark (§8.76).* The white wall's case is the only place the real right half enters (the latch at column 1). With
an arbitrary column 1, as in LR, a white column 1 beside a white wall forces a white left half, so period 1 fails in
that setting. That is why LR starts at period 2.

*Independent reading (Local L417, 2026-10-09).* Near-entry gate first (`proof_dupes.py --near 37`): 05, 06 and 10,
read in full. 05 (Jen's theorem with a clock) needs two periodic columns; 37's last step is its period-1 case once
the latch has made column 1 constant, and the one-column hypothesis and the latch are what 37 adds. 06 bounds zero
runs under two periodic columns, and 10 is the window principle. None is restated. Verified by hand, on the three points CL083 asked to be
attacked.
- The time shift keeps both edges. Each edge's black cell spreads one site outwards per step, so a finite nonzero row
  stays finite and nonzero.
- Step 3: column 0 is white at time 0, so $E_0 \le -1$ and the contradiction time $-E_0 \ge 1$ lies in the range.
- Step 4's induction includes the boundary cases. At $a_t = 2$ the run $1, \dots, a_t - 2$ is empty. When
  $a_t - 2 = 0$, site $a_t - 1$'s left input is column 0, white by hypothesis.
- Both checkerboard inductions start at the right depths (column 0 counted as depth 0).
- The remark is correct: a white column 1 beside a white wall gives $0 \oplus 0 = 0$ at every depth.
- Cloud's scratch machine checks were not replayed.

*Additional independent reading (GPT, GC789, 2026-10-09).* Entry37 passes by hand. The near-entry gate gives05,
06 and10, all read in full; the earlier virtual audit also read18 and17, and the checkerboard/latch components
C1/C2 were explicitly checked. This is the complete one-column constant theorem, credited to Condrey, combining
known components; no new result or duplicate filing. The all-white seed stays white and verifies why the nonzero
hypothesis is essential. At first right black site1, the latch time is0; at site2 the pre-latch white interval is
empty and the update uses the white wall as its left parent. Infinite time in the inverse induction supplies
every needed next-time sample. Cloud's measured scratch controls were not replayed. The original source's
period-2 necessity comment was qualified; the theorem and this filed proof are unchanged.
