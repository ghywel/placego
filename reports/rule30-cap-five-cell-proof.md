# Why the cap forbids00010 — GC2036 working proof

Owner asks for a hand explanation of GC2035's five-cell exclusion. Follow the same cap01111110 at sites0..7,
output sites8..12 at t8; no new depths or motifs. GPT takes this proof extraction; Local retains degree/kit work.
Record searched: GC2035 exact supports and hand relations, GC2028 recovery, L999/GC1935 run and staircase rules.
These are local consequences of Rule30, not a novelty or prize claim. Prior-art comparison remains separate.

Use moving coordinates r_t(j)=x_t(t+j), so r_(t+1)(j)=r_t(j) XOR(r_t(j+1) OR r_t(j+2)).
A word of length n has exactly four length-(n+2) predecessors: choose its last two bits and solve backwards
for each remaining bit. Hand first step:00010 has predecessors1111000,1110101,1110110,1110111.
The retained t7 constraints rule out1110 on positions0..3 and1110 on0,1,2,5; these suffice, but their origin
needs a hand explanation, not an appeal to the measured table.

## Frozen bounded certificate extraction

Prediction: the target's backward tree can be cut by a short prefix relation at an earlier time, allowing a
small hand proof. Counterfactual: if only long correlated prefixes cut it, retain that obstruction rather than
call a full truth table explanatory. Enumerate only predecessors of this one target back to t0 (at most65536
words of length21), compare first1..8 cells with the ALREADY retained supports at each time. Report minimum
prefix length that excludes all such ancestors, and their projected words. Independent control: every inverse
word updates by the literal decimal30 truth table to its specified child. Check the fixed initial cap excludes
all t0 ancestors. No new forward exterior scan, no scope expansion. One Intel process under run_capped.py:
10CPU/15wall seconds,256MiB sampled group RSS,4MiB/file,8MiB output, launch free+inactive1024MiB, ongoing512MiB,
swap growth128MiB. Source cap_backward_certificate.py; stop on any failed check/cap, no automatic rerun.

## Hand route found; final local checks frozen before execution

After3 updates the cap gives10r1(NOT r), with r=NOT x_0(8). After4 updates the prefix is a1abc,
where a AND b=0 and a OR b OR c=1. These conditions allow only01001,01010,01011,11100,11101.
Two more updates have neither001 nor100 as their first triple, and cannot start010011.
Two-step ancestors of00010 start with one of those excluded alternatives. This gives a short hand proof.

Final validation is local to the hand lemmas, not a larger cap census: all1280 thirteen-cell words whose first
five satisfy the premises; literal30 versus XOR/OR updates; verify the two-step restrictions and four-step
exclusion. Countercontrol: the target must be attainable from some unrestricted thirteen-cell row (use its
four-step inverse tree,256 words). Separately verify the cap-to10r1(NOT r) reduction on all8 relevant three-bit
right completions. Five CPU/10wall seconds,128MiB RSS,2MiB/file,4MiB disk, same pressure thresholds; one run.

## GC2038 — complete hand argument

**PROOF-SKETCH, awaiting Local's carrying read.** The finite exclusion remains independently COMPUTED from
GC2035. The argument below explains it by local identities and small case splits; the inverse search was a
proof-discovery aid, not an assumption in the proof. Claim: if x_0[0..7]=01111110 and every exterior cell is
arbitrary, x_8[8..12] cannot equal00010.

All displayed words use moving coordinates r_t(j)=x_t(t+j); the first displayed position is j=0. Write
G(z)_j=z_j XOR(z_(j+1) OR z_(j+2)). This is the ordinary Rule30 update in these coordinates, not a modified rule.

### A. The cap becomes a relation

Let u=x_0(8), v=x_0(9). Direct updates give

    t0: 0 1 1 1 1 1 1 0 u v ...
    t1: 1 0 0 0 0 0 NOT u (u OR v) ...
    t2: 1 0 0 0 r 1 ...                   r=NOT u
    t3: 1 0 r 1 NOT r ...

The extra1 at t2 uses (NOT u) OR(u OR v)=1. Thus the obvious black cap has produced two variable cells with
an exact opposite-colour relationship. At t3 name the next two cells s,h. One more update starts

    t4: a 1 a b c ...
    a=NOT r,  b=r AND NOT s,  c=(NOT r) XOR(s OR h).

Two restrictions follow immediately:

    a AND b=0,                   a OR b OR c=1.                 (P)

For the second, if a=b=0 then r=s=1, hence c=1. So the possible first five cells at t4 are among
01001,01010,01011,11100,11101. We now forget every other fact about the cap and allow the entire remaining
right tail to be arbitrary. This relaxation makes the argument stronger and keeps it short.

### B. Two local lemmas transport (P)

Take any row z beginning a1abc with (P), and set y=G(z), w=G²(z).

**Lemma B1: w cannot start001 or100.** Its middle cell dominates both neighbours:

    w_0 <= w_1,                    w_2 <= w_1.

To check this, write d=z_5 and split the three possibilities for (a,b):

| (a,b) | Extra premise | First four cells of y | First three cells of w |
|---|---|---|---|
| (0,0) | c=1 | 1111 | 000 |
| (0,1) | none | 101 NOT(c OR d) | 01* |
| (1,0) | none | 00 NOT c (c OR d) | (NOT c)1* |

The starred cells need not be fixed. The forbidden fourth possibility (a,b)=(1,1) is excluded by(P).

**Lemma B2: w cannot start010011.** Suppose it does. The inverse rule is

    y_j = w_j XOR(y_(j+1) OR y_(j+2)).

Choose y_6=u and y_7=v; the six preceding cells are forced, giving

    y[0..7] = 1, u, NOT u, NOT u, (NOT u AND v), NOT(u OR v), u, v.

There are two cases, both impossible:

- u=1 makes y begin110. Since y_0=NOT a, y_1=NOT(a OR b), and y_2=a XOR(b OR c), this forces a=b=c=0,
  contradicting(P).
- u=0 makes y[0..6]=1011v(NOT v)0. The first two values force a=0,b=1. Write the subsequent cells of z as
  z[3..8]=b,c,d,e,f,g. The value y_3=1 gives c=d=0. Then y_4=v gives e=v, and
  y_5=NOT v gives v OR f=NOT v. Hence v=0 and f=1. But now y_6=e XOR(f OR g)=1, contradicting y_6=0.

Thus(P) has turned into restrictions on changing cells at t6. No fixed colour is needed in either lemma.

### C. The forbidden five-cell output would require a forbidden predecessor

The inverse rule gives exactly four predecessors of00010. Applying it once more gives the following possible
six-cell prefixes two times earlier (only the prefix matters):

| At t7: a predecessor of00010 | Possible prefixes at t6 |
|---|---|
| 1111000 | 010011 or100100 |
| 1110101 | 100101 or100110 |
| 1110110 | 001000 or100101 |
| 1110111 | 001000 or100101 or100110 |

These entries are four applications of the displayed inverse formula per row; no empirical support table is
used. Every prefix beginning001 or100 contradicts B1. The sole remaining prefix010011 contradicts B2.
All possible predecessors are excluded. Therefore00010 is impossible at t8, proving the claimed local implication.

A slightly more general statement has been proved along the way: **any row starting a1abc with(P) cannot
produce00010 four G-updates later**, regardless of its tail. The cap supplies(P) at time4.

### D. What survives, and why smaller groups miss it

This is not an unchanged conserved quantity. It is an implication chain:

    fixed cap -> opposite-colour pair -> a1abc with(P)
              -> two exclusions on variable cells -> five-cell exclusion.

By t5 every individual cell can vary under some exterior, but restrictions on their joint choices remain.
At t8 all assignments to any four of the eight tracked cells are possible (GC2035 exact certificate), while
00010 on the first five is impossible. Each partial assignment may require a different exterior; compatibility
of all four-cell views separately does not imply compatibility of the five jointly.

Here are the five one-bit changes of00010, each present in the retained exact support. The full eight-cell
witnesses were independently replayed in GC2034:

| Cell of00010 changed | Allowed five-cell word | Allowed full eight-cell word |
|---|---|---|
| 0 | 10010 | 10010100 |
| 1 | 01010 | 01010000 |
| 2 | 00110 | 00110000 |
| 3 | 00000 | 00000000 |
| 4 | 00011 | 00011000 |

Deleting any one of the five requirements therefore destroys this particular contradiction. It is genuinely
minimal in that sense. This does not claim equal probabilities, statistical four-wise independence, that these
are the only forbidden words, or that such a relation survives forever. It is a local, finite, all-exterior
statement conditioned on the cap. It does not establish how often the cap occurs in the singleton picture.

### E. Controls, contrary case, and what the search taught us

The one-target inverse extraction passed87380 literal transition checks, with no target ancestor matching the
cap. It located the useful t3/t4 prefix cutoff, allowing the full table to be replaced by A–C above.
The final independent local checker passed1280 thirteen-cell cases of(P),8 cap-prefix cases and340 inverse
checks. XOR/OR and decimal30 updates agree. This is a check of the relaxed lemma, not another horizon scan.

Countercontrol: the row0100010001101 produces00010 after four G-updates. It starts a1abc with a=b=c=0 and
violates the second condition in(P). Thus the forbidden output is not intrinsically illegal for Rule30: it is
incompatible with this cap's surviving constraints. The hand proof deliberately exposes that premise.

Question -> response -> challenge -> better question: Why is00010 absent? Every local predecessor contradicts
a relation inherited from the cap. Is it simply a universally illegal Rule30 word? No; the countercontrol
produces it. Can smaller observers recover the exclusion? A support-only observer limited to groups of four
cannot at t8, although a short temporal proof can. The useful distinction is between the size of a present-day
observation and the length of a causal explanation. No new compute or universal growth claim follows.

## Evidence receipt

Shared-store packet `cited/gc2038-cap-five-cell-proof/manifest.json`, SHA256
`101db160dc6a74c5e05a63c79452e969755f58c8604dd9f36ea5b33c33aefb85`, contains both frozen sources and raw
results/stdout/launcher/time receipts; upload and stat hashes verified. Inverse source frozen3fb9ea2a, final
local checks frozenbf2992ba. Intel inverse child0.93s elapsed,0.90s user/0.02s system, process maxRSS21,221,376
bytes; local child0.09s elapsed,0.07s user/0.01s system, process maxRSS14,188,544 bytes. Both supervisors1.04s,
exit0; launch free+inactive6024/6016MiB and swap184MiB. Both ended before a periodic sample: CPU/file limits
and launch gate were applied, but zero sampled maxima do not establish sustained pressure monitoring. No retry.

The owner's reminder during this work is recorded: L1072's degree theorem was already in the kit and is known,
reproved here. That prior-art failure is not repaired by this exploration. No novelty claim is made for the cap
implication, the inverse-word method, or the Boolean observer viewpoint.

## Local's carrying read — L1083, 29 October 2026

**A–C carry; the local implication is PROVED (two-party).** Read step by step by hand:
- *A.* The four updates from the cap to `a 1 a b c`, and both conditions of (P). If a = b = 0, then r = 1 and s = 1,
  so c = 1.
- *B1.* All three (a, b) cases give w₁ ≥ w₀ and w₁ ≥ w₂.
- *B2.* The backward solve gives y[0..7] = 1, u, ¬u, ¬u, ¬u∧v, ¬(u∨v), u, v. For u = 1, y begins 110 and forces
  a = b = c = 0. For u = 0, b = 1 and c = d = 0, then v = 0 and f = 1, and y₆ = 1 contradicts u = 0.
- *C.* The table in C.

Local's own exhaustive checks, which are self-checks and not GPT's code:
- the four t7 predecessors and the five distinct t6 prefixes (001000, 010011, 100100, 100101, 100110) are exactly
  GPT's table;
- no (P)-row with any 9-cell tail violates B1 or B2;
- none of the 2^13 exteriors of the cap reaches 00010 at t8;
- the countercontrol row produces 00010.

§D's minimality table rests on GC2035's retained supports and is not part of the carrying proof. No novelty claim.
