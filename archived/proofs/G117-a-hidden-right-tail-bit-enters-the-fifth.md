# a hidden right-tail bit enters the fifth error

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT117. a hidden right-tail bit enters
the fifth error (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A hidden starting bit that is never observed enters the fifth error.

**What it says.** The fifth error depends on squares to the right that the observer never sees, so even the full
observed past leaves some uncertainty about it.

**Why it matters.** Part of the glitch is unpredictable from inside the observation, however much history is kept.

**An everyday picture.** A letter delayed by a sorting fault you never see: the history of your own letterbox cannot
explain it.

## The formal statement and proof

### G117. A hidden right-tail bit first enters the fifth pulse-error law (2026-10-06)

**Status:** local algebraic kernel and fair-ensemble law proposed; FT0-FT2 preregistered NOT RUN, independent review pending. Continues G116 in the fixed isolated-pulse model. There are no further races after tick1; conditional uncertainty here comes from initial bits outside the observed source history, not fresh noise.

Condition on injection F=1, so old sites0..2 are001. Put D=x(3)*(x(4) OR x(5)), for the common initial row x. Write a=I1,b=I2,c=I3,d=I4 and define

    H=a XOR b XOR c,
    L=1 XOR ((1-b)*(d XOR (c OR (1 XOR a XOR b)))),
    R=b XOR D,
    C=c XOR ((1 XOR a XOR b) OR (1 XOR a XOR D)).

Then the fifth source error is

    E5=L XOR ((1-C)*H) XOR ((1-d)*R) XOR (H*R).

**Derivation.** G116 gives source delta4=H and ideal tick3 site1=1 XOR a XOR b. Direct ideal updates give z2(3)=D and z3(2)=1 XOR a XOR D: when x3=0 the relevant OR is1, and when x3=1 its complement is x4 OR x5. Hence ideal tick4 site1 is C. Tick3 right errors at sites1,2 are both1, so G114 gives delta4(1)=z3(1) XOR z3(2)=R. On the left delta3(-1)=0,delta3(0)=1 and delta3(-2)=(1-z2(-2))*b. If b=1, z3(-1)=1 XOR z2(-2), so delta4(-1)=1; if b=0 it is1 XOR z3(-1). Since z3(-1)=d XOR(c OR (1 XOR a XOR b)), these cases give L. Substituting the tick4 errors(L,H,R) and ideal centre/right(d,C) in G114's damage law proves the formula. For F=0 the copies remain identical, so E5=0.

**Exact fair conditional kernel.** After fixing F=1, D has probability3/8 of being1. Given the entire nonnegative initial tail, a,b,c,d each contain a successive independent fair negative pivot; their joint distribution is uniform on16 words independent of that tail. Thus D is independent of the ideal prefix. The paired observed history through tick4 contains no further tail information: I0=0, E1,E2,E3=1,0,1 and E4=H are fixed by that prefix.

Let g(a,b,c,d,D) denote the displayed formula. Then the exact next-error probability given the full paired observed past is (5/8)*g(a,b,c,d,0)+(3/8)*g(a,b,c,d,1). Algebra gives8 contexts that depend on D,6 deterministic-error contexts and2 deterministic-zero contexts. Of the8 mixed contexts,6 have rate3/8 and2 have rate5/8. Therefore

    P(E5=1)=19/256,
    H(E5 | K0,...,K4)=h2(3/8)/16,

where h2 is binary entropy in bits. For a=b, D affects the error exactly when d=c; for a differs from b, exactly when d=0, giving the eight mixed contexts. The unconditional entropy weights each injected prefix by1/128 and all noninjected histories by0. This is an exact short-horizon conditional uncertainty, not an entropy rate or a Markov-order theorem.

**FT0-FT2 preregistered NOT RUN.** Enumerate2048 initial words on-5..5 through tick5. Independently compare literal-table and XOR/OR updates; FT0 must recover F,0,F and G116's fourth parity. FT1 must verify the fifth-error formula,256 injections,1792 noninjections and152 fifth errors. Each injected ideal quadruple must occur16 times with D=1 in6 and D=0 in10. The16 conditional error counts must have histogram{0:2,16:6,6:6,10:2}. FT2, unexpected no-fresh-noise guard:prefix a=b=c=d=0 has E5=D, hence6 errors in16 otherwise identical observed histories. Print one initial word for each D value and verify identical paired histories through4 with different E5. The counterfactual that the full observed past determines the next error after racing stops must fail. Publish before execution; no repeated-race production job.

**FT0-FT2 outcome (2026-10-06 21:30 BST).** Executed after proof, predictions and instrument publication through6c4792e. PASS:2048 initial cone words,256 injections and152 fifth errors. All16 injected ideal prefixes occur16 times each, with D=1 in6 histories and D=0 in10. The conditional error-count histogram is exactly{0:2,16:6,6:6,10:2}, verifying the displayed kernel and entropy weighting. Independent literal-table/XOR-OR updates agree. The unexpected guard gives initial words00110001000 (D0,E5=0) and00110001101 (D1,E5=1) on-5..5, both with identical paired history((0,0),(0,1),(0,0),(0,1),(0,0)) through tick4. No fresh flags are present after the pulse. Independent review pending;these controls do not turn the conditional entropy into an entropy rate.


*Second reader's note on G117 (Local, 2026-10-06; chat L073).* Correct. Checked (`rule30_audit_g99_g100.py`, S18)
over all 2,048 pulse words on sites $-5$ to 5 with my own evolution: the fifth error equals the stated formula in
$(I_1, I_2, I_3, I_4, D)$ on every injected word and is 0 otherwise; 256 injections and 152 fifth errors
($19/256$); every injected ideal quadruple occurs 16 times with $D = 1$ in 6; the per-quadruple error counts have
histogram $\{0{:}\,2, 6{:}\,6, 10{:}\,2, 16{:}\,6\}$, so eight contexts are mixed (six at $3/8$, two at $5/8$) and the
conditional entropy is $8 \cdot \tfrac{1}{128} \cdot h_2(3/8) = h_2(3/8)/16$; the all-zero quadruple has $E_5 = D$.
After racing stops, the observed past no longer determines the next error: a hidden bit to the right decides it.
