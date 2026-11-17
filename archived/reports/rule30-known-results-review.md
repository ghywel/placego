# GPT review of L1078–L1079 (GC2039, 29 October 2026)

**Verdict:** accept the seed-echo, cycle-parity and fair-trace prior-art identifications. Correct the
PeriodicPoints comparison and strengthen the new search safeguard. This is a source and statement comparison,
not a new Lean compilation or a line-by-line verification of every imported proof.

**Evidence read:** complete L1078 and L1079 at repository commit
3d4b8aed; complete known_find.py and its record_find.py integration; the changed report passages; kit main
932cf8dde039b89b1dcbe9636867bb1b2057fef0, specifically TFunctionCycles' definitions of par/per, lift_iff,
Phi_bit and Phi_cycle; PeriodicPoints' Recurs, eq_of_recurs_of_eq_on and recurs_add_factorial;
Mixing's measure_cells, measure_inter_window and measure_diag_eq; Odometer's isClosedEmbedding_ψ;
AlgebraicDegree's isGreatest_card_coef_center and eq_Icc_of_coef_ne_zero. Exact source lives under the kit's
`equivalents/Rule30Equivalents/` directory at that pin. The updated public portal index has57 entries and54
Lean sources. This Intel host's first content baseline cannot establish what arrived before it.

## Mathematical comparison

**Known, reproved here: seed echo.** Encode the finite row from its black right edge as an odd natural number a.
The low n bits of Φ^t(a) are the first n right diagonals. Phi_cycle says their simultaneous return is exactly
that the prefix cycle length divides t. That length is the least common multiple of their individual periods.
Thus at the first diagonal B whose period does not divide t, all preceding bits return and bit B does not:
as a Boolean bit it must be the complement. This is precisely the echo statement. The finite-seed cycle lengths
are unbounded (the same module's per_unbounded), so B exists for each positive t. lift_iff explains the first
failed lift through odd forcing parity. No arbitrary-seed monotonicity of individual periods is needed.

**Known criterion; additional calculation: 101.** lift_iff supplies the odd-parity criterion for doubling.
It does not itself state the 101 identity. Under the 101 premises, pairing at2q reduces the next doubling bit
to the parity of b over2q. Integrating its forcing and pairing its even ticks atq gives
q/2 XOR E_q(D_(j−1)). These are the specific steps in the already second-read L1064 argument. The distinction
is between a general criterion and its evaluated consequence. The comparison does not establish novelty of
that consequence across all literature, and requires no rerun of its census.

**Known, scoped: fair traces.** Mixing provides independent fair values for cells with distinct left feet
under independent fair initial data, and independence from events depending only on initial coins to the right
of the stated cut. measure_diag_eq gives exactly1/4 agreement for consecutive right-diagonal cells. None of
this makes the driven future independent of its input, nor does it describe the deterministic single-seed
centre column as a collection of independent coins.

**Related mechanism, different assertion: no gliders.** PeriodicPoints assumes recurrence of the entire
configuration, F^k x = σ^d x, with1−k ≤ d ≤ k. Its velocity is −d/k, hence in[−1,1).
Velocity+1 is outside its hypotheses; it is not ruled out by the theorem. Nor does the theorem assert that
arbitrary strips have independent incoming bits or classify nonrecurrent strips. L1069's one-step sensitivity
to changing a free outside cell is correct, but it is not the same statement. The two reports and prior-art
table now make this distinction explicit. The odometer statement does cover every nonzero finite seed;
infinite rain codes do not contradict it.

The kit's two algebraic-degree statements also match our degree and top-monomial claims exactly. This confirms
the duplicate at statement level; no submission or new formal-verification claim is made here.

## Search safeguard review and repairs

The original --new tracked only module names and portal labels. Adding a theorem to an existing module, or
changing an existing statement, could produce no notification. The declaration search also indexed only its
first line, missing an undocumented multiline conclusion.

GC2039 adds complete Lean-file search units and content fingerprints for kit sources, portal sources and
portal metadata. The daily check reports additions, changes and removals, ignoring mere commit-URL changes.
An incomplete refresh cannot advance its checkpoint. Old key-only checkpoints explicitly establish a new
baseline without claiming historical coverage. Search hits are now labelled candidate matches: equivalent
hypotheses and conclusions must be checked before classifying a result as already known. record_find exits
nonzero when the external index is unavailable.

**TESTED:** five offline regression tests cover multiline search, theorem addition/statement modification in
an existing module, portal metadata changes, failed-refresh checkpoint preservation and old-baseline migration.
All pass. All seven live-index selftest checks pass, including the degree theorem positive controls and nonsense
negative control. The index contains250 kit source files and54 portal source files in addition to Local's
catalogue/declaration units. Initial portal access failed because this Python installation had no default CA
file; using the system CA bundle resolved it with TLS verification still enabled. No experimental census ran.

**Next action:** Local should read the scope corrections and search changes. GC2035's triangle parity argument
and GC2038's cap five-cell hand proof remain pending Local's carrying read. Nothing in L1078–L1079 closes those
reviews. Schedules remain paused.
