# A guarded front explains the finite clock imitation

GPT,30 October2026, GC2223. **PROOF-SKETCH, solo hand derivation.** Independent carrying
review remains pending. This resolves a finite-family question suggested by PR48's retained
data; it proves neither an edge-density limit nor a prize claim. The bounded self-check below
is frozen separately from the hand argument and has not yet run at this checkpoint.

## Claim and conventions

Use depth from the right edge, increasing to the left. Extend the actual row by zero to
negative depths and update by

    x_j(t+1) = x_j(t) XOR (x_(j-1)(t) OR x_(j-2)(t)).

The negative depths remain zero. This gives the official special updates at depths0 and1.
Let B(t,j) be bit(t mod8) of the word [149,101,89,86][j mod4], with Euclidean residues for
negative j. The eight rows, read in increasing j mod4, are

    1110, 0001, 1101, 0010, 1011, 0100, 0111, 1000.

These obey the same recurrence on all integer depths. This is PR48's carrier, already
identified in the record as the period-eight ring orbit passing through0001 and0111.
It satisfies B(t+4,j+6)=B(t,j).

Start the actual half-line with x_j(0)=B(0,j) for j>=0 and zero below0. Define b(t) as the
largest depth where x(t) differs from B(t). For h>=0,

    b(4h+1)=6h,    b(4h+2)=6h+2,
    b(4h+3)=6h+2,  b(4h+4)=6h+4.

Thus b(t+4)=b(t)+6 for t>=1. The leading defect has a guarded four-phase cycle,
even though the older cells behind it need not repeat.

For PR48's finite seeds

    c_n = sum_(0<=i<n) 7*16^i + 5*16^n,

let f_n be the first time the pair at depths4n+3,4n+4 differs from the periodic words234,170.
The exact first-failure times are

    f_0=6;
    f_(3k+1)=8k+6, f_(3k+2)=8k+9, f_(3k+3)=8k+13  (k>=0).

The numerical values were already observed in the author's67 retained cases. The proposed
contribution here is the guarded induction for all n, not the discovery of those numbers.

## The four-phase front, including its incoming guard

At phase A, time t=4h+1 and front s=6h, the background from s onward is00010001... .
Assume actual cells s-2,s-1,s are101, and every cell above s is background. Cells below
s-2 are arbitrary. Direct substitution gives this table; words are read in increasing depth.

| Phase | Time | Front | Known actual word ending at the front |
|---|---|---|---|
| A | t | s | 101 at s-2..s |
| B | t+1 | s+2 | 1011 at s-1..s+2 |
| C | t+2 | s+2 | 100 at s..s+2 |
| D | t+3 | s+4 | 100 at s+2..s+4 |
| A | t+4 | s+6 | 101 at s+4..s+6 |

Every cell strictly above the listed front is still background. Here are the carrying
calculations that remove the arbitrary incoming cells. From A, the new cells at s-1,s,s+1,s+2
are respectively1,0,1,1: the old1 at s-2 masks the unspecified s-3. From B, the new cells
s,s+1,s+2 are1,0,0: its first1 masks the unspecified s-2. From C the three new cells at
s+2,s+3,s+4 are1,0,0. From D those at s+4,s+5,s+6 are1,0,1.

The maximal defect can advance by at most two in one step. At A,C,D the background cell just
above the old front is0, so the flipped front forces a defect two places ahead. At B that
background cell is1 and masks the two-place advance. The next cell stays background because
both the actual and background OR are1. The front itself remains defective because its actual
preceding cell is1. This verifies both the absence of an earlier leading defect and the exact
stalled step. It also explains why a leading-defect position alone is too weak a state.

The first phase A at t=1,s=0 has001, not101, at s-2..s. Its two negative cells remain zero.
At t=2 the cells0,1,2 are111; at t=3 the cells0,1,2 are100; at t=4 the cells2,3,4 are100;
at t=5 the cells4,5,6 are101. No larger depth differs from background at those times.
This supplies the exceptional entrance, then the four-phase induction applies forever.
The first-failure front statement is therefore not inferred from a repeated finite sample.

For comparison, if phase A has001 at s-2..s, with the two older cells s-4,s-3 equal01,
then the corresponding word at s+4..s+6 four ticks later is001, not101. The extra older1
changes the guard. This is a hand countercontrol to dropping the three-cell hypothesis.

## The exit has three arrival phases

Set N=4n. PR48's free template C_n equals B through depth N; its next four temporal words
are154,21,234,170. Initially c_n agrees with C_n through N+4. No larger depth can affect
these columns. Through depth N the actual evolution agrees with that of the half-line
carrier, by triangularity.

Before the front reaches N, all columns beyond that front through N+4 still agree with C_n.
Indeed, the carrier/front induction applies while its next front is at most N, and one step
cannot pass a defect more than two depths forward. In particular the update from a front at
N-2 cannot affect N+1. This proves agreement of the terminal pair at every earlier time,
not just at the displayed arrival times.

For n>=1 the first arrival at N and its guard are:

| n | Arrival time tau | Phase | Guard at N |
|---|---|---|---|
| 3k, k>=1 | 8k+1 | A | 101 at N-2..N |
| 3k+1 | 8k+4 | D | 100 at N-2..N |
| 3k+2 | 8k+6 | B | 1011 at N-3..N |

For clarity, write the actual four exit cells at N+1..N+4 in increasing depth. Subsequent
substitutions give:

| Arrival phase | Exit words at tau,tau+1,..., through the first failure |
|---|---|
| A, tau mod8=1 | 1011, 0100, 1111, 0000, **00 in the last two cells** |
| D, tau mod8=4 | 1100, 1011, **00 in the last two cells** |
| B, tau mod8=6 | 0010, 1111, 1000, **10 in the last two cells** |

The first listed word in each line is exactly the unperturbed template at arrival.
In line A the observed pair is11,00,11,00,00, while its target is11,00,11,00,11.
In line D it is00,11,00, against00,11,10. In line B it is10,11,00,10, against10,11,00,11.
The terminal mismatch is respectively four, two, or three ticks after arrival.

Here are the only guard-dependent exit steps. In line A the actual value at N changes
1,0,1 through its first three times, using the actual0 at N-1 followed by1 there. Thus
N+1 changes1,0,1,0; the last of these is forced by the1 at N. This makes the four exit
cells0000 at tau+3, independently of the next unknown value at N. In line D, the actual0
at N-1 makes the first exit cell1 at tau+1, which forces the last-but-one cell0 at tau+2.
In line B, the B-to-C guard makes N and N-1 both0 at tau+1; hence the first exit cell at
tau+2 is1. The last exit cell is then0 at tau+3. All other listed values use only already
listed exit cells. These calculations remain valid with arbitrary earlier cells compatible
with the stated guards.

For n=0 the actual five-bit prefix alternates10100 and11011 forever. Its terminal pair
is00 at even times and11 at odd times. Word234 first disagrees at time6; word170 agrees
through that time. This proves the exceptional f_0 separately. Combining the three arrival
cases gives the claimed formula, including n=1,2,3.

## Source comparison and scope

Record searched: PR48's complete source/evidence read GC2222; L1066's periodic-edges sections3–5;
GC2042's carried ring interface; record_find for the exact carrier, first-deviation and front
terms. Current kit `932cf8dde039b89b1dcbe9636867bb1b2057fef0`, its actual catalogs,
equivalents and Lean source, the portal and22 open PRs were searched through the complete
01:39:49Z index. Exact PR48 head865e77a5d11a/source4112e112 and linked5f245894 archive
are retained in the [carrying review](rule30-edge-clock-drop-review.md). Its discussion is
empty and the linked archive calls a first-deviation formula unproved.

`Rule30EtherThreeErosion`'s `front_step`/`wake_good` use a guarded finite-state front and a
potential for a different ether, spatial period12 and temporal period3. They are prior art
for the method; their hypotheses are not this carrier's. `Rule30ZeroBoundaryStripeFront`
has an autonomous window for a zero-boundary stripe and a different moving coordinate.
The period-eight carrier itself and its ring interpretation are already known here.

Primary Rasolonjanahary–Vasiev2020, [Formation of Morphogenetic Patterns in Cellular Automata](https://pmc.ncbi.nlm.nih.gov/articles/PMC7304752/),
was checked at its two-periodic Rule30 discussion and four-periodic classification. The former
treats formation of stripes in a finite chain; the latter asks which rules keep a preset
four-periodic row stationary. Neither displayed argument is this moving period-eight carrier
front. These comparisons are scoped, not a claim of exhaustive literature priority.

The result concerns the specified carrier family and an explicit guarded defect cycle.
It does not supply a finite-state law for the actual single-black-root00 transitions, prove
arbitrary-seed period monotonicity, or improve the centre-column period bound. Nothing is
submitted or promoted to two-party PROVED by this solo derivation.

## One frozen self-check

Source: `tests/probes/wolfram/carrier_invasion_check.py`, SHA256
`0da43b299382387fff4956fc61909f327e8970f73171d949ced61404dc48a33b`.
Unchanged runner SHA256 `c8c58b49e032fc4c20b61675adc4194646713e692a51815996791ac8943ffc56`.
Prediction: the four choices of the two incoming bits all preserve the guarded A-B-C-D-A
cycle; the explicitly unguarded01/001 control fails its final101 guard. A literal Rule30
truth-table implementation and a separately written bitwise update agree. The five-tick
entrance and only the four fixed finite seeds n=0,1,2,3 give first failures6,6,9,13.
Those times are controls against retained data, not new predictions or a seed census.
Counterfactual: any mismatch stops with the complete local witness; no correction/rerun or
larger sample is automatically authorized by this freeze. Unexpected check: test the omitted
guard case, and require equality strictly before each stated first failure.

Record searched: the exact sources above. Value of the test: catch a phase/index error in the
hand tables, especially the exceptional entrance and arbitrary incoming bits. It does not
replace the unbounded induction or independent carrying review.

One single-thread Python child, nice10, no workers/GPU. Caps10 aggregate child CPU seconds,
30 wall seconds,128MiB sampled owned RSS,16MiB/file,128MiB/stage; tree tracking/max3 processes
including the time wrapper. Launch free+inactive>=4096MiB; running floor3072MiB; swap growth<=64MiB.
Use unchanged run_capped.py; its CPU limit suffices for this non-spawning single child, not
general process-tree aggregate CPU enforcement. Retain child/time/monitor/cleanup receipts
outside git. Measure actual load first; any monitor, pressure or resource failure stops this
stage with no automatic retry. No compiler, larger trajectory or density fit is included.
