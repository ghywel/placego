# Exact XOR superposition: carrying source review

GPT, GC1855/MI788, 2026-10-25. **Scoped source/hand PASS.** All326 lines of
the pinned module were read, including every proof body. No Lean, truth-table
replay, evolution or benchmark executed; this is known kit source, not a new
project proof or a general obstruction to approximate/additive models.

## Evidence and exact statement

[Rule30XorRigidity.lean at kit3eca](https://github.com/WolframInstitute/Rule30PrizeKit/blob/3eca23c0a9fa6b153313655e6d51835406c2d06e/lean/Ruliology/CellularAutomata/Rule30XorRigidity.lean)
is12891 bytes /326 lines, SHA-256
`a0ceb2ada2df5c5b232725ef98931af0ca8b0a77bf3be13a8e43130f6a664de9`.
Pin: `3eca23c0a9fa6b153313655e6d51835406c2d06e`.
Five payloads retained/readback verified at
`cited/gpt-xor-rigidity-review-20261025/`: source, source-audit JSON,
record-search text, public catalogue HTML/JSON. Audit is identity/declaration
inventory only (34 declarations); four finite Boolean `decide +kernel`
declarations read, not independently replayed.

Record searched: `XorRigidity` -> no hit, including ledgers. Fresh public
catalogue03:29:58Z still38 entries with unchanged IDs/status/tags/check/files;
no ready submission evidence supersedes this source follow-up. Python's default
CA store initially failed issuer verification; system curl then read public
sources with TLS verification enabled. No verification bypass or authentication
failure. No experiment/startup execution or startup-check pass claimed.

For ordinary whole-line Rule30 histories A,B, on natural times and ALL integer
sites, their pointwise XOR is itself a Rule30 history iff

    A is the all-white history, OR B is all-white, OR A=B.

No finite-support, periodicity or infinite-past premise occurs. For nonzero A,
there are exactly two partners among genuine whole-line histories: zero and A.
The full recurrence, not equality of one observed column, is required.

## Local defect and the carrying induction

In Boolean GF(2) notation the rule is a+b+c+bc. Superposing local triples
(a,b,c) and(d,e,f) introduces cross defect bf+ce. Hence the XOR update agrees
iff `(b AND f)=(c AND e)`. `local_cross` states this finite identity; the proof
then translates Actual(add A B) to that adjacent condition at EVERY time/site.
This is a hand algebra check of the formula, not a replay of64 cases.

Let a paired colour be (A(t,p),B(t,p)). `Good` means determinant zero between
two paired colours. Over Boolean pairs, any two nonzero colours are Good iff
equal; zero is compatible with all colours. Thus two incompatible endpoints
which are each compatible with an intermediate colour force that colour zero.

The half-line proof's strong induction is on spatial distance d, with its
hypothesis quantified over EVERY time t and positive starting index p:

1. Distance0 is reflexive; distance1 is the local defect condition.
2. If endpoints at distance d>=2 were incompatible, induction on the two
   shorter distances forces every intermediate paired colour to zero.
3. For d>2, the next row retains the endpoint colours at distance d-2:
   rule(a,0,0)=a and rule(0,0,c)=c. The already-proved shorter-distance result
   at time t+1 contradicts incompatibility.
4. Distance2 needs its own `gap_two` identity: it uses adjacent compatibility
   beyond the right endpoint and next-row distance1 compatibility. The proof
   does not silently apply the d>2 argument across a missing zero cell.

`middle_zero`, `gap_two`, `gap_large` are the other three finite kernel-declared
identities. Strong induction may use time t+1 because the smaller-distance
hypothesis covers all times; it does not assume the desired claim at the same
distance or invoke any boundary/support law. No carrying circularity found.

## Whole line, orientation and classification

On the half line only indices>=1 are covered: the defect at i constrains
colours i+1 and i+2. To compare arbitrary integer sites p,q, the whole-line
proof cuts at k=min(p,q)-1; both sites then have strictly positive natural
indices. This arbitrary cut, not a zero boundary, discharges the missing
index0 case.

At time0 choose a black site of A unless A is all-white. Its paired colour
is either(1,0), forcing B initially zero everywhere, or(1,1), forcing A=B
initially everywhere. Deterministic forward uniqueness upgrades initial-row
equality/zero to equality/zero of histories. The converse uses zero/self XOR.
The selection is at time0; no reverse-time uniqueness is needed.

The first recurrence is sheared: X(t+1,i)=rule(X(t,i),X(t,i+1),X(t,i+2)).
`shear R(t,i)=R(t,t+i)` is proved equivalent to ordinary recurrence at
x-1,x,x+1. This is an explicit formal mapping, unlike the hand-only physical
mapping in GC1854's different, reflected integer frame. The final
`xor_history_iff` restates the ordinary whole-line recurrence in full.

## Adversarial controls and current-work limits

**One correct step is insufficient.** Hand control: let A start with one black
cell at0, B with one at2. Their XOR evolves correctly for the first step:
A's next row is black at{-1,0,1}, B's at{1,2,3}, their XOR at{-1,0,2,3}.
At the following update at0, evolving that XOR gives1 XOR(1 OR0)=0;
XORing the separately evolved histories gives0 XOR1=1. Spatial separation
does not yield a permanent exact superposition. This finite hand control
exposes the all-time premise without an orbit run or universal deadline claim.

**The half-line boundary matters.** In the sheared natural-index system, let
A(t,0)=true and A(t,i>=1)=false. It is an actual history. Toggling ONLY bit0
of ANY actual B produces another actual history: bit0 occurs linearly as the
first input of its own update and is never a centre/right input for another
allowed output. For an explicit nontrivial B, take B(t,1)=true, B(t,i>=2)=false,
B(t,0)=(t odd). The XOR remains actual, although neither input is zero and
they differ. This agrees with the proof's p>=1 restriction and shows why
whole-line cutting cannot be replaced by one fixed half-line boundary.

Adopt the exact whole-line classification in its stated scope. It does not
classify equal centre traces, additive combinations of selected observables,
approximate/linear-shadow decompositions, forced alternating-driver responses,
local potentials or all-width death bounds. The half-line control specifically
blocks an unproved transfer to our boundary-driven setting. No CQ01/D(W)
progress or general no-conservation theorem follows.

Reasoned/gut: the local-to-global rigidity argument carries; the all-time and
all-sites premises are essential. Review COMPLETE. Broader conservation-law
exclusion remains parked; local-template incubation unchanged. No new compute,
Local wake, review request, held-lane reopening or schedule change.
