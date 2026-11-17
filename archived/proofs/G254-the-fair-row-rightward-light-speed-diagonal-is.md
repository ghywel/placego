# The fair-row rightward light-speed diagonal is not order-two Markov

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT254. The fair-row rightward
light-speed diagonal is not order-two Markov (second-read by Local, 2026-10-09)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Starting from a random row, the colours along Rule 30's rightward diagonal cannot be produced by any rule that only remembers the last two of them.

**What it says.** Start from fair coin tosses and read the cells along the line that moves right one cell per step. Its first three correlations are exactly -1/2, 1/4 and -1/4. A process that remembers only its last two values, and is symmetric under swapping black and white as this one is, would be forced by the first two of those numbers to have -1/8 as the third. So it is not that kind of process. Second-read by Local, with the three correlations recomputed independently.

**Why it matters.** It closes one simple way of describing the diagonal's memory. It says nothing about longer memories or about the single cell's own diagonal.

**An everyday picture.** A forecaster who looks only at the last two days cannot match a climate whose three-day pattern breaks the rule those two days imply.

## The formal statement and proof

**Promoted from the waiting room, 2026-10-09 (Local L406).** Second reader: Local, chat L406. Waiting-room heading: "G254. The fair-row rightward light-speed diagonal is not order-two Markov (GPT, 2026-10-09; waiting room)". The text below is unchanged, so its *Status:* line is historical.

*Status:* independent hand reading pending. *Where:* RULE30-GPT.md GC773. *Provenance:* G97 fair-row invariance, left permutivity and independently replayed CL078 finite correlations. Nearest G110,G97,G113 read in full; G97 supplies the measure premise, while the other two concern pulse-coupled traces rather than this unperturbed diagonal. No general Markov/lumpability novelty claim. Proof copied verbatim below.

**Bounded response to CL078's offered all-lag reasoning lead.** Predict the exact first three correlations already rule out a two-step Markov description of the fair-row light-speed diagonal, using its global spin symmetry. Counterfactual: matching rho2=rho1^2 certifies that short-memory model. Independent control replays only the first three finite counts with decimal list updates; unexpected check keeps that rho2 equality while rho3 fails. No higher-lag scan, random sampling or single-seed measurement.

Let S_t=(-1)^x_t(t), with the initial row iid fair. This is stationary: Rule30 preserves the fair product row law by left permutivity, and the spatial shift preserves it too. Every finite block of these diagonal spins is invariant under simultaneous sign reversal. Indeed x_t(t)=x_0(0) xor g_t(x_0(1),...,x_0(2t)); flipping the fair leading input flips every S_t without changing the drivers. Stationarity extends this symmetry to blocks starting at any time.

Assume it is order-two Markov. Its conditional mean for a preceding spin pair (a,b) must be odd under (a,b)->(-a,-b), and therefore has the form

    E[S_(t+1) | S_(t-1)=a,S_t=b] = A*b+B*a.

All four pair states have positive probability, since rho1=-1/2 gives probabilities1/8 for equal signs and3/8 for unequal signs. Stationarity therefore fixes the same coefficients at every time; allowing time-dependent kernel notation does not evade the argument. Taking correlations gives

    rho1=A+B*rho1,
    rho2=A*rho1+B,
    rho3=A*rho2+B*rho1.

CL078's exact rho1=-1/2 and rho2=1/4 force B=0 and A=-1/2. The model then requires rho3=-1/8, whereas the exact value is-1/4. Hence the fair-row diagonal process is not order-two Markov (nor order one). This is a finite-memory obstruction for this stationary observable, not an assertion about every finite memory order.

**Independent finite-count replay.** tests/probes/lexicon/rule30_gpt_diagonal_memory.py enumerates the128 initial7-bit words and observes the first four leading cells under the literal G update, equivalent to F's rightward light-speed diagonal. The input leading-bit complement control flips all four spins, and each observed spin has zero mean. It reproduces rho1=-1/2,rho2=1/4,rho3=-1/4 exactly by integer sums. DM0/DM1 PASS; DM2's Markov rho3 prediction is REFUTED as required. This is a disclosed expected replay of already published exact counts, not a new blind numerical discovery.

**Unexpected limit and disposition.** The first two correlations really do match the first-order prediction; two-lag agreement cannot certify a kernel. This also does not refute a longer-memory or hidden-state model, prove the alternating sign at every lag, prove decay, or describe the single seed or finite-window density process. The useful all-lag input must retain more information than the last two diagonal bits. Earlier G109-G112 coupling-memory results concern a different pulse/noise observable; general projected-process memory is established theory. Existing higher-order lumpability prior-art entry and Geiger/Temmel's abstract reread; its finite-state criteria are not imported. No novelty claim or exhaustive literature exclusion. Independent hand reading requested; CX and G253 reviews remain priority. Scratch deferred without retry; room closed.

*Independent reading (Local L406, 2026-10-09).* Verified by hand: x_t(t) has cone [0, 2t] with x_0(0) its leftmost input at coefficient one, so flipping the leading fair bit flips every spin and leaves the drivers alone; the process is (G^t x)(0) under the measure-preserving G, so stationary; an odd function on {-1, 1}^2 is A b + B a; the three Yule-Walker relations are right, and rho1 = -1/2, rho2 = 1/4 give B = 0, A = -1/2 and the forced rho3 = -1/8. Checked independently by my own enumeration of all 128 seven-bit words: rho1, rho2, rho3 = -1/2, 1/4, -1/4 exactly, every spin of mean 0.
