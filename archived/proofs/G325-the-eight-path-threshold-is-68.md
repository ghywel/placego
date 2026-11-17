# The eight-path threshold is 68

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT325. The eight-path threshold is 68
(joint computer-assisted result; moved here 2026-10-22)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved, a joint computer-assisted result under the project's two-tier standard.

## In plain words

For eight disjoint paths,68 is the exact minimum path order that guarantees
burning within the ceiling of the square root of their total order.

**Why it matters.** A complete finite set of64,787,844 checked odd-integer
partitions, followed by strong induction, proves the upper bound for all
sizes. A known explicit forest with shortest path67 proves sharpness. The
result is computer-assisted and jointly verified in the project; literature
priority and external review remain separate.

## The formal statement and proof

### GPT G325 — The eight-path threshold is 68 (joint computer-assisted result, 2026-10-19)

**Status: PROVED, computer-assisted under the project's two-tier standard.**
Cloud designed the certificate job and proposed the exceptional-set compression;
Local ran the full job, checked its output and re-derived the induction;
GPT audited the reduction and supplied the independent completeness/tiling
verifier. Local inspected and executed that verifier on the finished stream.
This entry consolidates MI044/276, CL454 and Local L743/addendum at69cc079e;
GPT's full carrying read is MI484. It is a joint result, not a new proof
attributed solely to the person filing this entry.

**Statement.** Let L_8 be the least positive integer L such that every
forest consisting of exactly eight nonempty paths, each of order at least
L, has burning number at most the ceiling of the square root of its total
order. Then L_8=68. Its upper-bound part says that for every positive integer m and every eight
integer targets l_i>=68 with sum m^2, the set

    O_m={1,3,5,...,2m-1}

can be partitioned into eight subsets of sums l_1,...,l_8. The equivalence
with the square-order path-forest problem and the terminology L_n are
known; see Tan–Teh, *A note on graph burning of path forests*,
[DMTCS26:3(2024), introduction and section2](https://arxiv.org/html/2312.10914v3).
The lower witness below is also from their construction. No general
resolution of their conjecture for arbitrary numbers of paths is claimed.

**1. Finite certificate obligation and its verified result.** For24<=m<=32,
let E_m consist of ALL nondecreasing eight-tuples with sum m^2 and entries
in[68,2m+66]. Every tuple in every E_m has a literal partition of O_m:

| m | verified tuples |
|---:|---:|
|24|3,319|
|25|425,632|
|26|5,523,890|
|27|19,382,158|
|28|24,688,633|
|29|12,385,850|
|30|2,271,658|
|31|106,518|
|32|186|
|Total|64,787,844|

The finite result is a machine-certificate premise, not inferred from
sample success or solver node counts. Each certificate assigns every
position of the descending odd list to one of eight bins; the verifiers
recompute every bin sum. All64,787,844 assignments pass. There are no
unresolved, impossible or invalid records in the accepted stream.

Completeness is independently checked as follows. The285 files are
indexed by(m,a), where a is the exact minimum target and
68<=a<=min(2m+66,floor(m^2/8)). Every record is required to be a sorted
eight-tuple of that domain, and records in a chunk are strictly increasing
lexicographically. After fixing one minimum a and subtracting a from the
remaining seven entries, the chunk cardinality equals the number of
partitions of m^2-8a into at most seven positive parts, each at most
2m+66-a. An independent exact integer DP computes that number. Accepted
row count equals it in every chunk; membership and strict order then prove
exhaustion, including empty chunks. All expected filenames and final DONE
records are required. A stream digest identifies the bytes checked; it is
not a substitute for these checks.

Local's finished-run and verifier receipt is L743/addendum,69cc079e.
Both full verifiers report the same stream SHA256:

    90fea878fc36d18da25e52b2e73fbfcb8e4a447c72e470f9e5c3a5ea30d1063b

The generation took6,385s with eight workers on the M5 host. The separate
GPT verifier was inspected and ran on that host after completion; its
receipt gives285 chunks, the nine counts above,64,787,844 towns and exit0.
GPT did not transfer or replay the6.9GB stream on its own host. Its adoption
uses the explicit tier1 rule for controlled machine certificates.

**2. Strong induction removes the infinite quantifier.** Let P_m assert
the odd-partition conclusion for ALL eight targets>=68 of total m^2,
without imposing an upper bound. For m<=23 it is vacuous, since
m^2<=529<544=8*68. Suppose all earlier P_j hold and consider level m>=24.
If all targets are<=2m+66 and m<=32, the certified E_m result applies,
with bin labels restored after sorting. Otherwise some target satisfies
l_i>=2m+67. Replace it by

    l'_i=l_i-(2m-1)>=68.

The new total is(m-1)^2. Apply P_(m-1) and append the unused largest odd
2m-1 to that same bin. Importantly, P_(m-1) covers its ENTIRE level: the
reduced tuple need not land immediately inside E_(m-1).
For m>=33, the exceptional situation cannot occur, because

    m^2>8(2m+66).

At33 this is1089>1056; the difference increases by2m-15 at each next
step. Thus the induction covers every m. No parity or bin-cardinality
restriction is introduced by peeling. The endpoint m32 is essential to
this argument: target128^8 is not peelable at minimum68, since128-63=65.

**3. Odd partitions give genuine burning sequences.** For a square-order
forest and a partition, cut each path into consecutive intervals of the
assigned odd lengths. For the unique interval of length2r+1, schedule its
middle vertex as the source at time m-r. Its radius by time m is r, so
these scheduled balls cover the forest. Centers of two distinct intervals
in one component have distance at least r+s+1; for ignition times i<j,
this exceeds j-i because r=m-i,s=m-j and j<=m. Hence later designated
centers have not already been reached by earlier fires. The schedule is
legal and burns everything in at most m rounds.

For total order N that is not square, put m=ceil(sqrt(N)) and extend one
path at an end until the total is m^2. Its eight path orders stay>=68.
Use the square-order cover just established. Project any center in the
added segment to the old endpoint. Its distance to any original vertex
of that component does not increase, so the projected radius balls cover
the original forest. Such a ball cover yields a legal m-round burning
process: at a scheduled time, ignite the proposed center if it is still
unburned; if it has already burned, its future ball is already covered
by the existing fire, so any unburned vertex may be ignited instead.
If none remains, the process has already finished. Therefore L_8<=68.
This argument does not assume arbitrary-subgraph monotonicity of burning.

**4. An elementary lower witness gives sharpness.** Consider four paths
of order67 and four of order102, of total676=26^2. In26 rounds a source
can burn at most one odd-sized interval of at most51,49,...,1 vertices,
respectively. The sum of these26 capacities is exactly676. A successful
26-round cover would therefore have to attain every capacity with no
overlap. Consequently the available odds must partition into the eight
path orders. Each67 path needs an odd number of odds and cannot take only
one, since the largest is51; it needs at least three. Each102 path needs
an even number and cannot take only two, since51+49=100; it needs at
least four. This requires4*3+4*4=28 distinct odds, but there are only26.
Contradiction. This forest is not well-burnable, proving L_8>=68.
Together with the upper bound, L_8=68.

**5. Reproducibility, controls and limits.** Generation source
`tests/probes/cloud_reads/l8_certificates.py` at61edb625 has SHA256
`cfcd60a8c28b9bad1a6b711f360282ba3ecbd74c98f9584429f2ca49971b157e`.
The independent verifier `tests/probes/instinct/l8_stream_verify.py` at87a2b0d9
has SHA256
`cef30db19d6401f2eeb31755395fe1a7e346fe64023cc24b42093b4500babd47`.
Local's census source is `tests/probes/instinct/l8_certificate_census.py`.
With a fresh empty output directory outside git, regeneration and checking
use these committed programs:

    python3 tests/probes/cloud_reads/l8_certificates.py run OUTDIR --workers 8
    python3 tests/probes/cloud_reads/l8_certificates.py check OUTDIR
    python3 tests/probes/instinct/l8_stream_verify.py OUTDIR

The retained proof stream stays outside git on Local's host; an archival
release or independent regeneration is needed for readers without access
to it. The known resume-marker defect in the generation source is irrelevant
to this one fresh run and must be fixed before any resume; a fresh regeneration
does not use that gate. The greedy metadata is not mathematical evidence.
Can-fail controls include an intentionally corrupted tiling and a duplicate
replacing an omitted town while preserving valid per-record sums and total
count; the relevant independent checker rejects each. The DP has100 tiny
brute-force controls. All scope qualifications remain with the finite premise.

A bounded current literature search found no later determination of this
value; this is NOT FOUND, not a priority claim. This is a computer-assisted
result with two-party verification within the project, not external peer
review, a hand construction of the119-profile subclass, or a solution of
any prize listed in PRIZE-PROBLEMS section1. H2 and the generic five-bin
partition question remain open; this proof does not need them.

**Consolidation filing check (MI486).** proof_dupes --near W325 passes with
343 entries. G91, G314 and G307, the nearest older entries, were read in
full. Their Collatz identity, primitive-core packing and special E28
boundary do not state or prove the eight-path threshold. No generated
pages were built for this filing.
