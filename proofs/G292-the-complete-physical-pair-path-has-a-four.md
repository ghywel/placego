# The complete physical pair path has a four-state carry update

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT292. The complete physical pair path
has a four-state carry update (second-read by Local, 2026-10-13)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Inside a white band on Rule 30's left side, each slanted path of cell pairs turns into the next in one pass that
remembers only four states.

**What it says.** Start Rule 30 with a band of white cells on the left. The band begins at least two cells from the
middle, with a black cell on its side nearer the middle. Inside the white triangle this band opens, follow a slanted
path of neighbouring cell pairs from the triangle's edge to the middle column, and write it as a word whose
"letters" are those pairs. One left-to-right pass gives the next path's word. It starts with the same fixed first
letter. Each new letter comes from the old letter below it and the letter just written: each of its two cells is one
ordinary Rule 30 update. One extra letter is added at the middle column. The only memory carried along is that last
letter, so there are four possible states, and every old letter shuffles them without merging any two. The rule
holds only while the starting white band reaches at least three cells further from the middle than the number of
steps the current path has taken, and the first word must come from the actual starting row.

**Why it matters.** It replaces the single counts and parities of earlier attempts with an exact rule for the whole
path, and those earlier counts can be read back from the words. It does not bound how long the band lasts. The word
grows by one letter every step, so this is not a finite machine for the whole row. The four-state memory never
resets, and its cycling alone gives no bound.

**An everyday picture.** Knitting a scarf from the row below: each new stitch depends on the stitch beneath it and
the one just made, and every row ends with one extra stitch, so the scarf keeps widening. The knitter's only memory
is a four-position dial that each stitch turns or flips, but never jams two positions into one.

## The formal statement and proof

**PROVED, Local L693 at851dd270.** Source: RULE30-GPT.md GC1208. For d>=2, a black-ended initial zero band and the displayed phase-selected paths, the physical word P_a has head(1,1-e) and actual terminal(1,g_a). Under k+3<=E, the next word starts with the same head. Scanning old letters(C,B) after the head with preceding new output(A,H) emits(A XOR(B OR C),H XOR(A OR B)); after the scan append(1,C_last XOR B_last). The new word has one more letter. The old anchor and preceding new anchor have the same physical time and depths separated by2, so this is exactly the two forward local updates; the final white wall supplies the terminal XOR.

The initial word is built from the actual finite left origin, with early guards and visible-prefix conditions retained. The word grows; no finite total-state or all-depth record bound follows. The entire hole/source profile is recovered by one input lookahead. Carry encoding z=A+2H gives input actions -z,z+1,3-z modulo4, all permutations: no carry reset exists, although saturated input01/11 has identical actions. GC1208 includes horizon and failed-guard counters, independent physical controls and the carrying proof.

L693 hand-reads the same-time alignment, actual wall terminal, appended XOR, k+3 head horizon, actual initialization, all carry actions and hole recovery.
