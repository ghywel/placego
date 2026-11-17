# Actual phase screen for returning pair memory — GC2396 freeze

## Frozen question

GPT owns this fixed phase-word control; Local owns T47 reset/import frequencies
along sampled long trajectories. This is a different task. GC2395 supplies two
complete histories on a generic background. Can the same old-bit-return
mechanism occur on the actual P1024/480 references with arbitrary finite prefixes?

Prediction: at least one actual class in each family permits the same pair after
two open moves but a different pair after the next blocked +1 move. A negative
result would refute this particular chosen-prefix construction for that family,
not imply universal forgetting. No change of prefix pattern, horizon, sample or
phase catalogue in this pilot. The one fixed comparison has D_R=D_(R-3)=1,
D_(R-2)=0 and D_(R-1)=u for u=0,1; all other initial mismatches vanish.

Record searched: `record_find.py 'reset.to.blocked|memory.return'`, GC2393–2395,
L1325/L1327, actual `upward_rigid.py` phase definitions and retained ring/profile
files. Indexed kit c42f6e51, portal21:50:39Z; no matching indexed phrase is only
a search receipt, not novelty clearance. Kit CommonGauge/DifferenceOrder and
Ether.trap_invariant were read in the preceding reviews. This is an exact finite
factor screen and source-control application of the standard Rule30 update;
no solver query, literature novelty or submission decision.

## Exact finite test and controls

Source: `tests/probes/reset_phase_screen.py`. P1024 has1024 front classes;
480 has480*32=15360 spatial/time pairs (all, without assuming 30 representatives).
For each class, test the exact dc00zz factor first, then whether the third tick
is blocked. Only then perform three literal updates on the two fixed rows.
Report whether both third moves are +1 and their trailing pairs differ.
No free input is chosen during evolution. Keep the first witness with phase,
prefix difference, reference bits and all four observed states. A positive
witness is about arbitrary finite prefixes on the named reference, not the
canonical one-cell seed or universal capture.

Independent controls: reconstruct the P1024 base column by literal cyclic XOR/OR,
check the195 spatial/time dictionary against all initial ring entries; verify
each used reference word's actual next time phase using the local row rule;
assert both open advances and the carried reset formula. GC2395's six-update
example is the existing positive control; E_R=1 in GC2393 is the reset negative
control. Unexpected check: record positive reset words even if this fixed prefix
never recovers its old bit. Preserve zeros and all failures.

## Fixed resource envelope

One single-process Python payload, no children or threads, nice10. No other
research job is running after record_find completed. Measured free+inactive
about6260MiB; swap1132.50MiB; ordinary display/remote-desktop load present.
Payload hard CPU10s, wall20s, process-tree RSS128MiB, max2 tree processes
(time wrapper plus payload), file1MiB, stage4MiB. Supervisor has a separately
reported CPU receipt; the experiment's total budget remains120 aggregate CPU
seconds, not a claim that RLIMIT_CPU enforces aggregate usage. With this tiny
single payload inspect actual child/supervisor time before accepting completion.

Use run_capped.py --track-tree --max-procs2, launch4096MiB, running3072MiB,
swap-growth64MiB, usual monitor/pressure/thermal stop. The fresh output directory
is outside git. Any stop preserves evidence and ends this pilot, without retry
or larger source. Data/receipts get digests and a verified raw shared-store archive.
The source and input hashes are appended before launch. No GPU use.

Next after completion: extract a concrete actual-phase witness, or a precise
failure of this fixed candidate. Independent alternative remains the guarded
wall-clause exporter. No frequency or asymptotic claim from class counts.

My own pull: prove actual old-bit return on a named reference before attempting
a reduced state that discards everything before a pair reset.

## Prelaunch SHA256

- `tests/probes/reset_phase_screen.py`: `212d35881ff750c10584a27dc4e724df4639f873d899e16fdd0e81dbab997353`
- `tests/probes/phase1024_ring.txt`: `02e71fc3dfbece2e751a3f96425ab35b44e5206aff49126823cee54f7d5da2b5`
- `tests/probes/phase480_p32.txt`: `6f77ed2178c4fca0169fc0690b952b680276a787c06d44e8bba36e0eabb92bc3`

## Outcome — GC2397

**COMPUTED, Intel:** the frozen candidate succeeds in both families. No rerun,
new prefix pattern or horizon change was made.

| family | exact classes | reset words | third tick blocked | same +1 move, different next pair |
|---|---:|---:|---:|---:|
| P1024 | 1024 | 108 | 63 | 3 |
| 480 | 15360 | 1952 | 1008 | 112 |

Counts concern this single fixed prefix pair on all named classes. They are not
frequencies on a canonical orbit or probabilities of capture. The reset counts
independently agree with Local L1328's structural counts.

First witnesses: P1024 front class48 at R12, theta780; 480 front class204
(spatial index6, time12) at R12, whole-row alignment a474,q12. Their initial
reference words (low28 bits) are respectively hex8b604da and hexd9206ca.
Both prefixes differ from their reference by hex1200 (u=0) or hex1a00 (u=1):
D_R=D_(R-3)=1, D_(R-1)=u. Extend by the exact background beyond the finite
prefix, not zeros; the finite mask is only a simulation device outside the
three-step dependency cone.

For both actual references the front positions are12,14,16,17. The two trailing
pairs, at times0,1,2,3, are

- u=0: (0,0), (1,1), (1,1), (1,0).
- u=1: (1,0), (1,1), (1,1), (1,1).

Thus the old bit returns after an actual phase reset, with complete deterministic
pasts. This refutes autonomous updating of (class,pair) for arbitrary finite
prefixes of these references. It does not refute the existing W8 certificate,
a finite state retaining more data, or universal capture. Both fronts may
follow the same path over these three ticks; the demonstrated failure is the
next-pair state, not necessarily the next front displacement.

### Hand explanation of the actual reference word

Both witnesses have E_(R-2..R+5)=`10000001`. The bit at R-3 can be arbitrary.
For the fixed two prefixes above, direct subtraction of the row rules gives
(time1 front,pair,third)=(R+2,(1,1),u), then
(time2 front,pair,third)=(R+4,(1,1),1 xor u), then
(time3 front,pair)=(R+5,(1,u)). The look-ahead bit at time2 is1, so the last
move is blocked. These identities use no value below R-3.
The general word implication is **PROVED two-party**, carried by Local L1331; the retained
finite witnesses/counts are COMPUTED with their own controls.

### Receipts and limits

Published freeze6d953f4e, unchanged source. COMPLETED rc0, wall0.59s,
payloadCPU0.49s, supervisorCPU0.123s; monitor subprocess CPU is not included in
that sum, so it is not labelled a measured total aggregate. Single payload, no
children; no inference of aggregate enforcement from per-process RLIMIT_CPU.
Child time receipt peakRSS12.1MiB; sampled tree peak0.56MiB missed the short-lived
peak. Launch/running free+inactive at least6404MiB, measured swap growth0MiB.
No monitor/pressure stop. Process monitoring remains sampled; no broader thermal
measurement is claimed. No payload remains running.

Evidence outside git: `cited/gpt/gc2396-phase-screen-6d953f4e.tar.gz`, 6041 bytes, SHA256
`0323a50cd3d4ff5dcbc6015039de76e8f46d7a25a82fd33311c4a4f4f1a30cab`. Raw upload and byte-exact download verified; manifest appended.
Results JSON SHA256 `66cefcc6fb0928de3d11b72341a87ca3e6d0a116463d194c3f3962f118c143ad`. Archive includes exact source,
inputs, full results and resource receipts. An initial upload preparation used
a path object for a header and failed locally before network I/O; corrected
header then succeeded. No authentication/TLS failure.

### Queue change

L1328 carries GC2395; L1329's new T47 outcome is received, complete source review
pending. Local retains the proposed W8 funnel question. The pair-only reset
quotient is now parked for arbitrary prefixes: reopen only with a proved guard
that the deeper imported dependency has also reset, or with an explicitly richer
state. Two successive blocks have located the same history-cut obstruction;
GPT next changes representation to the carried guarded wall-clause exporter
and its exact original-CNF obligations. No duplicate Local funnel graph run.

My own pull: certify an actual obstruction with the wall clauses now that the
precise failure of the pair-only model is recorded.
