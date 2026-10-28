# Independent review of L1072's degree law

GC2031, 28 October 2026. Owner requests verification, review and validation of Local's new proof.
Read the complete L1071/L1072 entries, the159-line proof, both numerical sources and the206-line grounding
report at650564e9. This review concerns the all-time degree theorem, not acceptance of every survey claim.

## Validation specification, frozen before execution

Record searched: degree law, multiplicative complexity, Schnorr and algebraic degree. Recovered GC486's
existing exact two-step polynomial, degrees at1/2/4 and fixed-seed scope warning. Read its original probe.
The new independent checker represents Boolean polynomials directly as sets of square-free monomials;
it does not use Local's NumPy truth-table/Mobius implementation or assignment-by-assignment pivot search.

Prediction: exact degree2t-1 and stated top monomials for t2..6; full rightmost-derivative identity for t1..6;
exact symbolic z-frame recursions and top coefficients for m1..6. Independent literal decimal-rule replay
checks all inputs for t1..4. Countercontrols: Rules90/150 stay degree1 through6; an incorrect t2 monomial
label must be rejected. Unexpected check: distinguish Boolean idempotent products from ordinary polynomial
products; the checker cancels duplicate mask unions. These are bounded controls of the proof, not its
all-time justification. Any failed assertion stops acceptance until explained; no automatic larger run.

One Intel process under run_capped.py:30 CPU/45 wall seconds;256MiB sampled group RSS;2MiB/file and8MiB
stage output; launch free+inactive1024MiB, ongoing512MiB, swap growth128MiB. No NumPy dependency, no Local
job duplicated, no t12 replay. Source: tests/probes/wolfram/degree_law_gpt_audit.py. Hand carrying review
continues independently of the numerical result. No novelty certification or formal compilation yet.
