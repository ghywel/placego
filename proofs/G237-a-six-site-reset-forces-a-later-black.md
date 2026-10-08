# A six-site reset forces a later black sample with a white neighbour

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT237. A six-site reset forces a later
black sample with a white neighbour (second-read by Local, 2026-10-08)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Six initial sites force a later black reading whose neighbour rules out a two-zero gap.

**What it says.** Starting with 000010 beside the alternating wall forces five successive local transitions. The final black site has a white neighbour, so its next gap contains one or three zeros.

**Why it matters.** This supplies the missing cancellation in the fourth branch of a finite forbidden-word certificate. The earlier classification of branches still uses a checked computation.

**An everyday picture.** Two marks labelled unknown can still refer to the same number; subtracting that number from itself gives zero.

## The formal statement and proof

**Promoted from the waiting room, 2026-10-08 (GC620; Local L334).** Second reader: Local, chat L292. Waiting-room heading: "G237. A six-site reset forces a later black sample with a white neighbour (GPT, with Local's independent fourth-cylinder replay, 2026-10-08; waiting room, GC549.32)". The text below is unchanged, so its *Status:* line is historical.

*Provenance:* GC549 checkpoint 32, following checkpoint 31 and Local L290. GPT derived the shared-variable cancellation and the weaker six-site premise before fetching L290; Local independently closed the fourth cylinder computationally and supplied a seven-site cancellation. No novelty priority claim. This entry proves the six-site local lemma; the application to the fourteen-symbol absence also uses L288's independently checked finite cylinder classification. Candidate-neighbour check W237 read G207, W236 and entry 06 in full: G207 is a three-boundary-beat identity, W236 a forbidden spatial predecessor, and 06 a periodic left-half run bound. None states this six-site reset. Independent reading of this exact six-site chain pending.

At an even time with the wall white, any right row beginning 000010, with arbitrary farther sites, follows these forced prefixes at successive even samples:

    000010 -> 101100 -> 00101 -> 01001 -> 00000 -> 100.

Here each arrow is two Rule 30 ticks under wall 0,1,0. Write the next two arbitrary sites after the initial prefix as A,B. The first odd row begins 00011,(NOT A),(A OR B). Its next row begins 10110 and its sixth site is

    1 XOR ((NOT A) OR A OR B)=0.

This proves the first arrow for all farther tails. The following four arrows can each be read from a shorter odd prefix: 101100 gives odd prefix 10101 and hence output prefix 00101; 00101 gives odd prefix 01101 and hence 01001; 01001 gives odd prefix 11111 and hence 00000; 00000 gives odd prefix 0000 and hence 100. The stated output prefixes use only the displayed odd sites, with a black wall during the odd row. In the first two shorter odd-prefix calculations the final required OR contains a displayed one, so no undisplayed farther bit enters.

After ten ticks the visible site is therefore black and site 2 white. In any black-start row with sites 1..4 equal to 1,b,q,r, direct substitution gives

    b_next=1 XOR ((1 XOR (b OR q)) OR (b XOR (q OR r)))
          =b AND (q OR r).

For b=0, the inner OR is (NOT q) OR q OR r=1. For b=1 it is NOT(q OR r). Thus site 2 stays white at the next even sample in this chain. The reviewed GC503 latch formula allows only a one-gap or a three-gap from that white sample, never a two-gap. This is universal in the farther right tail.

*Controls and limitation.* `rule30_gpt_gap_reset.py` independently checks the five prefix arrows against literal decimal Rule 30 on all fifteen needed tail completions, and confirms that all four L288 source cylinders force 000010 at time 8. Replacing the repeated A in (NOT A) OR A OR B by an unrelated variable destroys its identity at A=1,C=B=0: this is the precise information lost by checkpoint 31's ternary method. L290 independently closes the fourth cylinder with 16,384 completions; its numerical result is Local's, not a GPT run. The full forbidden-word conclusion retains L288's finite classification as a computational premise. No prize or uniform language claim.


*Independent reading of G237 (Local, L292, 2026-10-08).* Local checked all five arrows and the black-row identity by hand, and separately replayed every completion of 000010 to twenty sites and all four source cylinders. No gap found; the six-site statement is verified. This supersedes its historical pending label.
