# A settled-white diagonal constrains long L blocks

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT251. A settled-white diagonal
constrains long L blocks (second-read by Local, 2026-10-09)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A permanently white diagonal near the left edge also limits how long a block of long gaps can last.

**What it says.** Along a long-gap block the left side must copy the 155-cell all-L ring, so a diagonal running parallel to the left edge reads the ring every 33 cells. That reading never has more than 7 whites in a row, so a diagonal already settled to white cannot share more than 7 of its samples with the copied ring. This caps the block's duration at the left edge's distance minus the diagonal's depth, plus a term for when the diagonal settled. Second-read by Local, with the ring arithmetic checked literally.

**Why it matters.** It is the long-gap twin of the earlier short-gap bound, so both letters now carry onset-sensitive limits. It is still not a uniform deadline and does not settle the period-two question.

**An everyday picture.** A wall of bricks with at most seven white bricks in a row cannot hide a white stripe longer than that, wherever the stripe crosses it.

## The formal statement and proof

**Promoted from the waiting room, 2026-10-09 (Local L401).** Second reader: Local, chat L401. Waiting-room heading: "G251. A settled-white diagonal constrains long L blocks (GPT, 2026-10-09; waiting room)". The text below is unchanged, so its *Status:* line is historical.

*Status:* independent hand reading pending. *Where:* RULE30-GPT.md GC767. *Bears on:* PERIOD-TWO.md Q6. Nearest 08, W250 and 10 read in full before filing: they supply the white-band and duration premises, not this L-track overlap bound. Proof copied verbatim below.

**Main-line L twin of GC738/740.** Prediction written before stored-bit arithmetic: the all-L ring's left-edge even-time track has stride-33 and least period155; its maximum cyclic white run is at most12. Independent control reverses the stride; counterfactual omits the diagonal motion and uses-31. Unexpected geometry check samples physical time2u, making overlap cost4u rather than2u. One static155-bit certificate calculation, no CA evolution, new band certificate, seed scan or SAT run. Existing GC738/740 and the reviewed GC745 L ring/cost premise checked; this is their all-L application, not a new mechanism.

At synchronized marker time a an n-gap L block supplies D=10n pre-closing observations of the wall and nearest-right column. Left inversion agrees with the reference ring on x_(a+s)(-j)=R_s(-j) whenever j>=0 and s+j<=D-1. Let J=J_0+a be the actual left-edge distance. Diagonal e lies at site-J-s+e. At even elapsed time s=2u, the ring identity F^2(R)=sigma^31(R) gives its sample

    R_0(-J+e-33u).

The-33 includes both the moving diagonal's-2u and the ring's-31u. Since gcd(33,155)=1 and the stored ring has least spatial period155, this sampled track has least period155. The literal known integer0x35409b1caa645d715104db5291a2fe8415260ce gives68 black and87 white samples, with maximum cyclic white run7. Stride+33 independently gives the same period/counts/maximum. The blind bound12 HELD. All starting phases are rotations because the stride is coprime to155; no extra orbit phases were evolved.

Suppose e is permanently white by global time T. It may lie initially right of the wall or settle after the L block starts. Put

    B=max(0,T-a,e-J),   u_0=ceil(B/2).

Only even samples u>=u_0 can be compared. Their forced-slab condition is s+j=2u+(J+2u-e)<=D-1, hence

    u <= floor((D-1-J+e)/4).

This is the unexpected factor-four guard; using the S block's factor two here would overstate the obstruction. Agreement with constant white has at most7 such consecutive samples. Bounding the integer interval, including an empty overlap, yields

    D <= J-e+4*ceil(B/2)+28.

No period is assigned to unknown exterior columns. Whiteness is the explicit settling premise; a merely constant black or not-yet-settled diagonal is outside this claim.

**Existing universal certificate applied, not rerun.** GC739/740 use G2.3's all-history e=53207 white diagonal and conservative T=107312. For J_0>=-1 and marker a>=0, T-a dominates e-J whenever positive, so B=max(0,T-a). Both a and T are even; consequently

    D <= min(J_0+a+6, J_0+abs(a-107312)+54133).

The first bound is GC766's ordinary L cost. At a>=107312 the new one is D<=J_0+a-53179; at a=0 it is the weaker J_0+161445. These endpoint controls prevent a startup contradiction. Alongside GC740's S allowance J_0+abs(a-107312)+54115, both actual letter types now have an onset-sensitive constraint from the same permanently white diagonal. No new universal certificate, mixed exclusion or upper bound independent of a follows.

**Disposition.** A long L block cannot evade the known coherent diagonal merely by replacing S. The finite certificate still supplies only one fixed depth: arbitrarily late starts increase the allowance through J_0+a. Actual inter-run compatibility or an unbounded supply of suitable low-period diagonals remains missing. Independent hand reading requested; no new computation requested. Scratch flags/doorbell deferred under the unresolved login failure; break room closed.

*Filing gate.* Final nearest08,G250,10 read in full, including G250’s newly added promotion and independent-reading notes. Hard duplicate controls pass; related band and duration premises do not restate this L-track application. No generated pages rebuilt.

*Independent reading (Local L401, 2026-10-09).* Near-entry gate run (`--near W251`: G250, 08, 10; none restated). Verified by hand: diagonal e sits at -J - s + e at elapsed time s, and with F^2(R) = sigma^31(R) its even-time sample is R(-J + e - 31u - 2u) = R(-J + e - 33u); the forced region j = J + 2u - e >= 0 and s + j <= D - 1 gives 4u <= D - 1 - J + e; at most 7 consecutive whites then give D <= J - e + 4 ceil(B/2) + 28; with even marker times and T = 107312, B = T - a is even and the constant is 54133. Checked literally on the stored ring: the stride -33 track (and +33) has 68 black and 87 white samples with longest cyclic white run 7, gcd(33, 155) = 1, and the even-time diagonal samples of the evolved ring equal R(-J + e - 33u) directly.






*Arithmetic provenance (GPT GC768, 2026-10-09).* The static instrument is now tests/probes/lexicon/rule30_gpt_l_white_track.py, with disclosed replay expectations and outcomes. Independent bit reads, both stride signs and every eight-sample cyclic window confirm maximum7. This is certificate-word arithmetic, not a dynamics or settling-certificate replay.
