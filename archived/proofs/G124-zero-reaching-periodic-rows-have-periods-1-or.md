# zero-reaching periodic rows have periods 1 or 3 times a power of two

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT124. zero-reaching periodic rows
have periods 1 or 3 times a power of two (second-read by Local, 2026-10-06)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A repeating row that eventually fades to all white can only repeat every 1, 3, 6, 12, 24, ... squares.

**What it says.** If a row repeats across space and Rule 30 eventually turns it entirely white, its shortest
repeating block is 1 square long, or three times a power of two. Every such length occurs.

**Why it matters.** It is a clean classification of the patterns that die out completely: their loop lengths start
at three and double. It does not touch the blinking middle column.

**An everyday picture.** Organ pipes for one note in different octaves, each twice the length of the last: 3, 6, 12,
24 and so on, with a single tiny pipe of length 1 standing apart.

## The formal statement and proof

### G124. Periodic Rule 30 rows that eventually reach zero have periods 1 or three times a power of two (2026-10-06)

**Status:** symbolic inverse-transducer theorem; independent review pending. No new experiment. This classifies least spatial periods of individual periodic rows that reach the all-zero row; it does not claim that Rule 30 is a nilpotent cellular automaton. It supplies no temporal-wall exclusion.

Let y be a spatially periodic output with least period p, and let x be any spatially periodic predecessor. Translation invariance implies p divides x's least period q. Inverting from right to left uses G122's pair maps

    M0(u,v)=(u OR v,u),
    M1(u,v)=(1 XOR (u OR v),u).

If y is nonconstant, p>=2 and one output symbol in a period is zero. Choose the period cut so the first descending symbol is that zero. The first map sends all four pair states into T={00,10,11}. The following map sends T to at most two states, regardless of the next symbol:

    M0(T)={00,11},
    M1(T)={10,01}.

Every later map preserves the upper bound on image size. Thus the p-symbol return map has image size at most two and every cycle has length at most two. The pair states of a periodic predecessor lie on a return-map cycle: there is no transient when the row repeats in both spatial directions. If the cycle length is k, the reconstructed bits have period dividing k*p. Combining k<=2 with p dividing q gives

    q=p or q=2*p.

This statement permits several predecessors and does not assume a unique periodic predecessor. The cut is just a phase choice, not a restriction on the row.

For constant output zero, M0 has only fixed cycles 00 and11, so its periodic predecessors are exactly the constant zero and constant one rows. For constant output one, M1 has the unique three-cycle 00->10->01->00, with11 entering it; its periodic predecessors are exactly the three phases of 001. Their least spatial period is 3. These constants are the exceptions to the nonconstant-output period rule.

**Classification.** Take a periodic row reaching zero, and use its finite first-hit trajectory backward from zero. If it is already zero or is the one row, its least period is 1. Otherwise the step before one has period 3. Every earlier row is nonconstant (a constant could reach zero in at most one step), so successive backward least periods are preserved or doubled. The original least period is therefore 3*2^k for some integer k>=0.

**Existence at every allowed period.** G123's canonical tails of any nonzero finite root give periodic rows C_n that first hit zero at time n. Starting with p_2=3, the present return-map bound forces each subsequent period to stay fixed or double. G123 proves these periods unbounded. Hence every value3*2^k is attained somewhere in that ancestry, without skipping a power. Together with the zero and one rows, this proves the possible least periods are exactly1 and3*2^k. The depth at which each doubling occurs is not bounded here beyond G123's finite-state estimate.

**Independent local check and unexpected guard, by hand.** The cyclic words give the exact forward trajectory

    001010 -> 011011 -> 010010 -> 111111 -> 000000.

Each arrow is checked by applying the literal triples of Rule 30 at the six labeled sites. The first word has least period 6, the next two period 3, and the last two period 1. This shows the doubled-period case is real, and that nilpotent-to-zero periodic rows need not have prime-power spatial periods. Separately,001->111 refutes applying q<=2*p to the constant-one output. These are independent finite algebra checks, not a run or a horizon extrapolation.

**Scope and prior art.** Existing-record checks found G105's zero preimages and G122's inverse maps, but no recorded classification of all possible least periods of zero-reaching periodic rows. Targeted prior-art searches for Rule 30 periodic preimages and zero-reaching/nilpotent periodic configurations did not locate a suitable primary source for this exact claim; novelty remains unresolved. The proof above is self-contained. Every nonzero root has these ancestor-period doublings, so they are not a distinguishing feature of a hypothetical eventual 0101 trace. This theorem is a structural result about the periodic zero basin, not evidence that the open temporal-wall bridge is complete.

*Second reader's note on G123 and G124 (Local, 2026-10-06; chat L078).* Both correct, including the steps GPT asked
me to challenge. Periodic rows agreeing on a half-line agree everywhere, so $F(C_n) = C_{n-1}$ and the first hit of
zero is exactly at $n$; the return map's first zero sends the four pair states into $\{00, 10, 11\}$, and both $M_0$ and
$M_1$ then reduce that set to two states, so cycles have length at most 2 and the period keeps or doubles; doubling
one step at a time cannot skip a power. Checked (`rule30_audit_g99_g100.py`, S23): every zero-reaching state on
rings of 1 to 16 cells has least period 1 or $3 \cdot 2^k$, with 3, 6 and 12 all present at 12 cells; the single
cell's canonical tails have periods $1, 3, 3, 6, 6, 6, 6, 6, 6, 12, 12, 12$ for $n = 1$ to 12, with the divisibility
chain, the pigeonhole bound and $F(C_n) = C_{n-1}$; the period-6 trajectory checks cell by cell. (Descriptive: the
doublings come at depths 2, 4 and 10, far earlier than the pigeonhole bound forces.)
