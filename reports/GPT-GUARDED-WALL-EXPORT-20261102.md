# Guarded wall export without changing the original proof target — GC2398

GPT owns this exporter; Local owns the W8 funnel work. GC2390's exact map and
free-boundary proof are carried by L1323. Source reviewed again:
`upward_rigid.py:cnf`, original U_j variable numbers, fixed two deep columns,
and the retained P1024 S_E byte format/hash. The exporter adds no solver path.

## Concrete implementation

[guarded_wall_export.py](../tests/probes/guarded_wall_export.py) writes the
unchanged generator's original CNF and a JSONL list of separate obligations.
It never writes an augmented CNF. It requires the exact independently checked
389-state source hash and verifies the195 phase dictionary against actual columns.
Output must be a fresh directory; files stop at16MiB and preserve failures.
No real export or SAT job has yet been run; a bounded integration pilot needs
its own source freeze and resource receipt. The command interface takes states,
out, D and k; it supports D1..64 and the P1024 phase only.

For candidate2<=j<=D-11, time t and word w it emits
`-ell_j OR ell_2 OR ... OR ell_(j-1) OR window-mismatch-literals`.
Here ell_i is the signed original variable `i*1024+t+1` for mismatch from
background column k-i at t. Window bit h-1 refers to U_(j+h), so a target1
negates ell_(j+h). Candidate depth is r=D+1-j. No depth below12 is exported.
Each certificate state (c,w) fixes exactly one t modulo1024 through
`t=c-195*(k-j)`. Thus the expected obligation count is389*max(0,D-12).

## Finite proof obligation from the carried front law

There is a useful explicit horizon: a forbidden entry at r requires contradiction
within H=3*(D-r) ticks. Each three-tick block raises the deepest mismatch by at
least1, with the carried intermediate floor keeping all updates interior.
After D-r blocks the front reaches at least D, contradicting the fixed reference
tail. Extend past the original two fixed deep columns by the reference; periodic
time indices are read modulo1024. This is a finite consequence of the carried
certificate, not a new universal-capture assertion.

The exporter records H, but a number in JSON is not a formal proof. This explicit
horizon deduction is PROOF-SKETCH pending a carrying read; the underlying
unbounded transfer is already carried. The output gives each clause's negation
as original-variable unit clauses, bound to the SHA256 of original.cnf.
A later LRAT proof of original.cnf plus those units would prove the clause from
the original clauses. Alternatively a kernel theorem can carry the implication.
Until then all files are labelled OBLIGATIONS_ONLY_NOT_CERTIFIED. No added-clause
UNSAT receipt can replace the original-CNF proof obligation.

## Cheap implementation controls, specified before execution

Prediction: for synthetic background polarities and target words, the exported
clause is false exactly at a deepest candidate with that window, accepts an
interior lookalike with a deeper mismatch, and emits no j at D12. Test D13/j2
and D14/j3 for words0,1,128,255 and three background polarity patterns; exhaust
the involved Boolean assignments. Reject the out-of-range boundary j and words.
Counterfactual: a flipped window bit order, missing suffix literal or unchanged
background sign would disagree with the independent mismatch predicate.
These are subsecond mapping controls, not a phase search or solver experiment.

Outcome: all18,432 independent Boolean predicate/sign cases pass, and all three
invalid boundary/word cases are rejected. Source:
[guarded_wall_export_check.py](../tests/probes/guarded_wall_export_check.py).
No solver or original-CNF export has been executed. The integration/proof
pipeline remains pending; the static check does not establish a formal clause
implication.

Record searched: GC2390, L1323, GC2397 queue, `upward_rigid.py`, retained S_E
format and `capture_membership_check.py`; no existing guarded exporter found
in the probe sources. Kit/source comparisons remain those in the carried report;
no novelty or submission claim is made. No TeX edits.

Next executable step: freeze a D13 integration pilot, bind the exact source/input
hashes, generate original CNF and389 obligations under run_capped.py, and verify
the original CNF hash and each candidate's depth/phase. Only then choose one
original-plus-units LRAT obligation; no augmented hard search first.
Independent alternative: full T47 source review and Local's funnel terminal guards.

My own pull: make every new constraint answerable to the original CNF, with a
finite contradiction horizon that can later become an explicit proof artifact.
