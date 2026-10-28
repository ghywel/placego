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
