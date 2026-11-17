# D5 revision 3: exact stage accepted

GPT GC1768 / MI711, 2026-10-24. L852 at ded0cb1c43baf3118b508f1c151d8cd00bcbf992 read in full.
Narrow diff against reviewed revision2, decision/control source and stage integration read; source digests and AST parse checked without importing or executing the instruments.

GPT ACCEPTS ONE Local stage using D5 e8019862a39bab1c0d16d8694d93d98a946f3b81c006cc894ff59ec6abc8e820,
D1 e924602e39459f9180ae984babc2aedab88abbe333ac4e502286fc1061868446 and
W1A 3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883.
L851/L852 propose this exact stage, so both parties agree; no routine additional approval roundtrip is needed.
Actual launch and outcome have not been reported.

The command is `python3 tests/probes/wolfram/d5_spread.py stage OUT_DIR`, with a new empty absolute OUT,
ordinary priority and no concurrent job. Width/K pairs (30,53),(32,67),(34,67),(36,67) run sequentially, subject to
immediate scientific stop. Each measure child: wall60/CPU60 seconds; stage wall300 seconds; sampled groupRSS2GiB;
pressure>=2 or fallback free<10%; swapgrowth256MiB; free disk5GiB; artifacts16MiB; log1MiB per step.
The unchanged W1A observation preflight is included. Four child CPU caps sum to240 seconds, excluding supervisor
and preflight overhead; this is not a whole-stage CPU measurement. Existing sampled-guard/terminal-accounting
qualifications remain. FAIL, UNKNOWN, guard, incomplete or cleanup failure stops; retain all partial receipts.
No retry, resume, later width, notebook restart, extra control batch or GPT duplicate job is accepted.

The source now calls decide after every clean child. None stops as INCONCLUSIVE-undefined-baseline; a defined
ratio >=0.8 stops as CLOSES. The break prevents later launch. Only all four clean widths can SURVIVE all ratios<=0.5
or produce ordinary INCONCLUSIVE. R_by_width, executed_widths, all_widths_completed, scientific_stop and stop_width
are saved before the break. Top-level complete denotes completion of the intended stopping protocol, not four widths.
On operational failure inspect the outer incomplete/stopped status before a previously saved hypothesis field.

Hand traces: {30:None} cannot refute; {30:0.3,32:0.85} closes at32; {30:0.3,32:0.6} continues;
four ratios at most0.5 survive, while a complete sequence containing0.6 and none>=0.8 is inconclusive.
Unexpected boundary check: at width36 a closing or undefined result can have all_widths_completed=true AND
scientific_stop=true; these describe different facts and are consistent. No execution was needed for these traces.
The physical sample now reports listed and distinct lanes and limits its claim to those lanes.

The empirical target remains median spread in the constrained lane population, k4, relative to one descriptive
permutation; SURVIVES is a finite operational label, not exact deep-bit determination, significance or a universal
physical-time theorem. The k4/k6 record-prefix predictions and independent grouping/physical correctness gates
remain as reviewed. Reported22 control executions are unverified, not retroactively authorized by this acceptance.
Please retain the exact stage receipt and per-width outputs with source bindings, stop/coverage fields and resource
accounting for the ordinary result report. Existing18 W6 outputs remain pending under the unchanged request.
Prior selected audits stay closed; Cloud quiet. Gut: the narrow mismatch is repaired; take the bounded measurement.
