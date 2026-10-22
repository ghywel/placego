# A zero triangle fixes the entry packet of its absolute clock guard

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT287. A zero triangle fixes the entry
packet of its absolute clock guard (second-read by Local, 2026-10-13)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Left of the blinking middle, a white triangle turns each black-beat test it covers into bookkeeping: a known
starting pair, then an even-or-odd count of white pairs.

**What it says.** Suppose the middle keeps blinking and, in one row, the squares from d to E places left of it are
white, just outside a black square that is not the middle itself. As this run shrinks into a white triangle, its
black inner edge forces two side-by-side squares a few rows later, whatever else the row holds: both are black if k
− d is even, and only the outer one is white if k − d is odd. Here k is any tick from d to E − 1 (counted from that
first row) at which the middle is black, called a black beat. A diagonal starting at the outer square of the pair
moves one place inward each tick and reaches the square next to the middle exactly at tick k. It changes colour at
every step unless the two squares on its inner side are both white (a white pair). That square must be black at a
black beat for the middle to turn white next, so the number of white pairs met must be even or odd as d and k
decide; the last pair is all white exactly when the square right of the middle must be black one tick earlier.

**Why it matters.** Each black-beat test the run covers now starts from known colours and comes down to one exact
even-or-odd count, worked forward with nothing assumed about earlier rows. It settles no prize question and does not
bound how long a white run can be: later counts run over ever more squares of the actual picture, and white pairs
can cancel out, so no fixed-size summary or growing cost follows.

**An everyday picture.** Carry a coin down a staircase, turning it over at every step except where the two tiles
beside that step are both white. If you know the face at the top, the number of steps and the face needed at the
bottom, you know before looking whether the double-white steps must be even or odd in number. The triangle sets the
top face; the blinking middle names the bottom one.

## The formal statement and proof

**PROVED, Local L688 at6a84b181.** Source: RULE30-GPT.md GC1203. In an actual clock row with x_0(d-1)=1 and x_0(d..E)=0, d>=2, let k=d+2a+e, c=a+1 and n=d+a-1+e, for a>=0,e in{0,1}, k+1<=E. The row at c has (x_c(n),x_c(n+1))=(1,1-e). The persistent black inner boundary of the white triangle and one literal update prove the packets11/10; no backward real parent is assumed.

For the moving adjacent pair F_u=x_(c+u)(n-u), r_u=x_(c+u)(n-u-1), write h_u=(1-F_u)(1-r_u). Summing the literal update of the cell just behind that pair gives x_k(1)=(1-e) XOR(n mod2) XOR XOR h_u. Thus a black-clock guard requires XOR h_u=(d+a-1) mod2. The final h_u, at white time k-1, is the actual right visible bit demanded by the clock. The full derivation, sharp final-cell and d1 controls are in GC1203; independent fixed controls in rule30_zero_triangle_guard_transport.py. This supplies an origin-preserving guard interface, not a finite-state closure or a record bound. Local's L688 hand read verifies both packets, the exact horizon, guard sum, terminal-white bit and fixed offset class; no computation requested.
