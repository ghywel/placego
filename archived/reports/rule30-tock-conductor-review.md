# L954 review: what the conductor remembers

GPT, 2026-10-25, GC1891 / MI819. Owner explicitly permits tests on the Intel machine. This is one bounded follow-up to the words-first dialogue; schedules remain paused. Read Local's complete notebook at `1d2483cde34cf4a7752e038dd0baac2239dac230` and its carrying request, plus both earlier Tick Tock notes and the current record map. No public submission or large run.

## Verdict on Local's hand work

**The requested cells 7–8, Proposition 1 and the width-at-most-five deadlines carry.** I checked the substitutions and triangular reconstruction by hand before the small independent forward checks below. Local's independent read of GC1889 is adopted: its six-cell table, discrepancy identity and periodic-input implication now have a carrying second read. These elementary facts do not prove the prize claim.

For completeness, the sufficiency direction of Proposition 1 can be made explicit. Given an infinite watched trace a with black even entries, set column 0 to zero and column 1 to a. Recursively define column j+1 by

    x(t,j+1) = x(t+1,j) XOR (x(t,j) OR x(t,j-1)).

This defines every cell and satisfies the forward rule identically. Thus imposing F_j = x(0,j) = 0 beyond W is sufficient as well as necessary for a finite starting row. The newest trace bit enters F_j through XOR with coefficient one, giving the claimed k_m and c_m split. No existence assumption about finite survivors is smuggled into this construction.

Proposition 2 carries for passing histories, with the j=1 constant cell treated separately in its displayed dependence bound. Its tail-equality statement concerns the entire future, not merely the short prefix sufficient when a support bound M is supplied. Propositions 3–5 also carry in their stated finite-state / first-arrival / finite-support scopes; no general finite abstraction follows from them.

**A necessary scope qualification in section 3:** write

    e_m = k_(m+2)(b_0,...,b_(m+1)) XOR (1 XOR b_m XOR b_(m+1)).

Then the displayed relation

    d_m = NAND(b_m,b_(m+1)) XOR e_m

holds when **2m+6 > W**, because only then does the white tail force b_(m+2) = k_(m+2). It need not hold during the free chapter. The conductor functions themselves are universal on all prefixes; their equality to the actual future tock is conditional. For example the genuine width-six start 110101 has first tocks 0001, so d_0 = 0, whereas NAND(0,0) XOR e_0 = 1. Here depth 6 is inside the start, precisely outside the guard. Local's surrounding prose recognizes the free chapter; this makes the equation's qualification explicit.

## One selected hypothesis, and its counterexample

Local's closing suggestion was that later corrections might be terms involving an earlier black-to-white fall. A necessary consequence of that specific form is:

> If the preceding tocks never fall from black to white, the correction to the two-tock XNOR rule vanishes.

The registered bounded test rejects it at k_4, on prefix **0001**. This prefix rises once and never falls. Nevertheless k_4(0001) = 1, while XNOR(0,1) = 0. This is not solely an inadmissible arbitrary-prefix artefact: 0001 is the first four tocks of the finite start 110101, which passes the even checks through time 8.

Here is the short hand explanation, recovered after the test. Suppose the first five tocks are (0,0,0,1,r) and the ticks through time 10 are black. Local's formulas and the outward recurrence give:

| Depth j | E_j(0) | O_j(0) |
|---|---:|---:|
| 7 | 0 | 1 |
| 8 | 0 | 0 |
| 9 | 0 | 1 XOR r |
| 10 | 1 XOR r | r |
| 11 | 1 | not needed |

The non-immediate shifted value is E_9(1) = 1: substitute the shifted tocks (0,0,1,r) into E_7 = 1, E_8 = r and O_8 = 0, so E_9 = O_8 XOR (E_8 OR E_7) = 1. Then O_10(0) = E_9(1) XOR (O_9 OR O_8) = r and E_11 = r XOR (1 XOR r) = 1.

Thus making depth 10 white requires r = 1, which gives the nonzero correction. But depth 11 is black regardless of r. A width-six start cannot supply that cell. Its attempt to keep the ticks black therefore fails at time 10, exactly as direct evolution confirms. This is a tiny hand contradiction, not an all-width reduction or a new death-time record.

**Interpretation in words:** an extra correction is needed even before the tocks have made a downward swing. We cannot explain all corrections as accumulated missed downward beats. In this example, the next tock can satisfy one blank-tail requirement but cannot satisfy the neighbouring requirement too.

## Why repeating corrections are not yet a mechanism

Once the free chapter is over,

    b_(m+2) = XNOR(b_m,b_(m+1)) XOR e_m.

If e eventually repeats with period p, the previous two tocks together with the phase modulo p form a deterministic system with at most 4p states. Hence b eventually repeats. Conversely, if b eventually repeats, e = b_(m+2) XOR XNOR(b_m,b_(m+1)) eventually repeats too. So, along a hypothetical finite survivor, eventual periodicity of e and of b are equivalent.

This does not make the question useless. It identifies the additional work required: prove a restriction on the universal conductor and the odd-depth checks jointly. Merely renaming the irregular signal does not explain why it must settle. The small contradiction above uses their incompatibility directly, without proving anything about long-term repetition.

**Question back to Local and the owner:** can satisfying a blank-tail requirement force an incompatible requirement farther out, in a way that applies to every finite beginning? The example has a two-cell obstruction; there is no claim that every beginning has one, or that the distance to it is bounded. This is the familiar all-width obstruction in a concrete new vocabulary, not a solved new route. A useful next step needs an implication between checks, rather than more unconstrained tables of k_m.

## Test and failure record

Frozen source: `tests/probes/wolfram/tock_conductor_audit.py`, SHA-256 `b417cb25be08231aac928814e1a3d1e74a3af011dcd54d2099ec24c34a3dc4ba`. All predictions and caps were written before its sole execution.

- Independent outward reconstruction versus forward pivot inversion and literal forward replay: **256/256 eight-tock prefixes pass**. E_7/O_7/E_8 agree throughout this domain; k_0 through k_3 checked on all 15 prefixes.
- All **32** padded six-cell starts with black watched cell: support at most four fails by 6; support at most five by 8; only 110101 passes 8, failing at 10. This checks Local's finite hand claims; it is not a new frontier census.
- Known-wrong k_3 with the old-bit term deleted is detected. Unexpected controls: trailing white padding does not alter evolution, and constant-tock reconstructions have nonzero periodic spatial tails, preserving the finite-support distinction.
- No-fall hypothesis: first counterexample at k_4 after nine no-fall cases; hypothesis scan stops there. No k_5–k_8 claim or subsequent enlargement.
- Intel process elapsed time **0.0794 s**, not a benchmark or a system-wide resource measurement. One process; wall 15 s, CPU 10 s, sampled own peak-RSS stop 128 MiB, file cap 256 KiB; all data structures are additionally bounded by the stated tiny domain. No GPU, Lean, network or child process in this test. Terminal result: PASS for controls, REFUTED for the blind hypothesis.
- Retained raw JSON outside git: basename `conductor.json`, SHA-256 `25a71172bdca3ecdb43d901db1911daf94aca4326bb424b821b1d9efd58ec740`; stderr empty. The source reproduces the result except its elapsed-time field. Essential mathematical evidence is printed above so the review does not depend on access to private scratch.

The two legacy startup commands were attempted under a separate bounded supervisor (30 s each, one OpenMP thread, 512 MiB sampled process-group stop, 256 KiB output). Both were stopped immediately because the sandbox denied the supervisor's process-list monitoring. No test output was produced, and **neither startup check passed**. Failure receipts and empty logs are retained outside git; no retry or enlarged run. The dedicated pure-Python audit uses its own resource counters and completed successfully. Its controls do not retroactively turn the startup attempts into passes.

Reasoned verdict: Local's requested algebra and small deadlines carry, with the free-chapter guard explicit. One tempting simplification is refuted by an actual admissible early history and explained by hand. Gut verdict: the joint constraints remain interesting; a supposed correction generated only by falls is now cold. No all-width theorem, general memory bound, novelty claim or schedule restart.
