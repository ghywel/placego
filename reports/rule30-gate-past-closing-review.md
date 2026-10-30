# Arbitrary-future past closing: exact source and evidence review

GC2250,30 October2026. **Existing external results carried in their stated
scope.** The unbounded closing assertion remains open. The mathematical
interfaces and carrying proofs were read; generated finite triangles and
large proof expressions rely on retained author kernel replay, with their
schema and source binding inspected. No new GPT compiler or trajectory run.

## Source and exact scope

[PR52](https://github.com/WolframInstitute/Rule30PrizeKit/pull/52) is open at
head `64003389e169db91b80a17b60670afb2eb22b87f`. Fresh conversation,
review-summary and inline-comment lists were all empty. The
[immutable proof archive](https://github.com/Troyusrex2/Rule30PrizeKit/tree/48a2173d6326ed59154e14666564b3ce26a72b06/research/gate-past-closing)
is the validation source. All five changed modules were freshly downloaded
at the PR head and match the archived replay inputs byte for byte.

| Module | SHA256 |
|---|---|
| Rule30PastStrip | 2abc512d5f08bb4181a9f9788d63cb39b866457c3bcc1f631b2937731d578663 |
| Rule30GatePastCover | 852bef73c65c2269251e33f623c114e71eefc5a9e3e6996a1b5c5be2a2eeeb7f |
| Rule30Certificates.GatePastCases | fdf685fc4e27e6528c76fcbba93af305209eccd8361cb2c3a17ba2bd54688217 |
| Rule30GatePastCases | a59e04b05b89147446097fe1c854aa6af7e5cee89f7cc1174add39bf4ac3594b |
| Rule30GateTailReduction | 1c0f4dec9722a072f064596edb74231a9ac126c19eb90ee10381a8ee186fd202 |

The convention is a_G(2r)=NOT G(r), a_G(2r+1)=true. GateLegal means every
little-endian eight-bit window belongs to
{8,9,16,18,33,36,66,72,132,144}. The row is the actual official
Rule30ZeroBoundary.lam(a_G), reconstructed beside a white wall. A legal
n-bit past p means that prepending p to G still satisfies GateLegal.

The unconditional finite statements say that all legal pasts of length
4,5,6,7 of **every infinite legal future** have equal reconstructed row
tails from columns38,49,99,107 respectively. Neither periodicity of G nor
finite support of its row is assumed. These modules do not import PR47;
the earlier three-bit result is background, not a hidden dependency.

## Why a finite cover proves an infinite-future statement

PastStrip first proves that if two traces agree for every time t>=T, then
all reconstructed columns agree at those times. If, additionally, two
adjacent columns M,M+1 agree throughout t<T, the sideways recurrence
propagates their full-time agreement to every column beyond M. This is
an absorbing pair of columns, not one coincident row bit.

The finite triangle has a white column0, the supplied trace at column1,
and every literal Rule30 reconstruction equation in its shrinking domain.
triangle_sound identifies every covered cell with recon. PackedValid's
shift/XOR/OR/modulo check implies those cell equations, by the exact
bit-of-modulo lemma; there is no trusted Python arithmetic premise.

A Leaf has future-prefix length m>=8, its packed gate word, a column edge
at most2m, and tables for every allowed n-bit past. The eight-bit prefix
fixes which pasts are legal. Its triangle has horizon2(n+m)+1, enough for
columns edge and edge+1 at every t<2n. All allowed pasts must agree there
with one reference table. The reference need not carry a separate validity
premise: equality through it directly gives equality between the two
valid past tables. The common future after2n then invokes the absorbing
pair theorem.

The cover tree branches on the next future bit, closes at a valid leaf,
or rejects a prefix containing an illegal eight-window. Induction on the
finite tree covers every infinite legal continuation; the maximum leaf
edge is a uniform spatial cutoff. root_cover dispatches all ten possible
first windows. The generated5/6/7-bit file has17/36/71 leaf checks and
uses only the proved checked_leaf/checked_branch constructors plus kernel
finite decisions. The4-bit file has13 leaves. The author Python audit's
reported synchronization columns39/50/100/108 use the pair's right column;
the Lean bounds38/49/99/107 use its left column. They are consistent.

## The all-length reduction and its actual missing premise

AllPastClosing quantifies over **every n**, legal G and pair of legal
n-bit pasts, and asks only for eventual equality of their reconstructed
rows. HomoclinicClosing asks for the same conclusion for any two legal
gate streams that eventually agree. The code/shift proofs establish their
exact equivalence by packing a shared-future cutoff into finite pasts.

The support lemma is essential. If A is white beyond W, B is finite, and
their boundary traces agree from time T, then B is also white beyond W.
Otherwise B has a last black cell m>W; at time T its exact advancing edge
is black at m+T, while A is white there. Reconstruction from the common
future makes those entire time-T rows equal, a contradiction. The lemma
does not silently infer that B is finite.

The overlap graph has a certified40-step path between each ordered pair
of its ten states. Splicing a period-five gate prefix of any requested
length K onto the original future preserves legality and eventually
restores the original stream. The stream/window overlap proof covers both
junctions. All100 stored paths, including their endpoints, membership and
overlap edges, were also checked directly as fixed retained data.

Assume now that a legal G reconstructs to a finite row bounded by W.
Choose K=W+20 and the proved periodic-prefix splice H. The **unproved**
HomoclinicClosing makes the reconstructed H row eventually equal to the
G row, hence finite. The support lemma sharpens its bound back to W,
independently of how far away closing occurred. H(0)=true makes its row
nonzero at depth2. Its initial gate prefix supplies a period-ten boundary
clock through length2K-1. The actual kit jen_clock then gives
2K+1<=m+20<=W+20, impossible for K=W+20.

Thus no specified rate of closing is required. FiniteCoverFamily supplies
checked finite covers for every n; taking a finite bound across its ten
root trees proves AllPastClosing and hence the exclusion. Neither
AllPastClosing nor FiniteCoverFamily is established by the four finite
instances. Their truth is not inferred from a small-width trend.

## A rate obstruction, not a closing obstruction

PastStrip's exact legal ten-bit pasts132 and528 share an eventual-gap-five
future but give different row values at column200. The two horizon202
triangles and their literal semantic proof establish true versus false
there. This refutes a proposed bound starting at20n; it does not refute
eventual closing. No new computation of this example was performed.

The separate linked computational covers through12 are not the
kernel-checked through7 result and were not adopted by this review.

## Retained validation and its limits

All41 archive files match their immutable git blobs; the author's manifest
accounts for40 payloads. All13 source inputs and unchanged Check.lean
match exact PR or official kit bytes at932cf8dd. The official toolchain
file is Lean4.35.0. The reproduction script checks its specified Windows
executable hash, checks all source hashes before and after, creates a new
project and builds the13-source closure without reused objects. It then
runs the unchanged official checker on all five new modules and performs
a combined import/type/axiom check. This is not a whole-catalog build.

Each retained RESULT checker object equals its raw log's final JSON:

| Module | Replayed | Declared | Headlines |
|---|---:|---:|---:|
| PastStrip | 70 | 33 | 5 |
| GatePastCover | 127 | 94 | 11 |
| Certificate GatePastCases | 2727 | 264 | 9 |
| Wrapper GatePastCases | 3 | 3 | 3 |
| GateTailReduction | 130 | 42 | 9 |
| Total | 3057 | 436 | 37 |

All report partial pass, statement import, successful replay, standard
axioms and no new axioms. The exact printed conditional types were read.
The build log reports all13 modules built and no source warnings. Most
certificate declarations are auxiliary finite-check terms, not separate
mathematical results. No individual hand replay of every triangle or
large generated proof expression is claimed.

Author guard receipt: elapsed204.8845seconds, peak owned RSS3215138816bytes,
minimum system available42130530304bytes, exit0/no guard stop. Declared
limits were300seconds,8GiB owned RSS,2GiB available, sampled every0.1second.
These are author-host measurements, not Intel measurements. The archive
contains the final guard summary but not raw samples or its guard
implementation, and does not demonstrate aggregate CPU/output/disk/swap/
thermal enforcement. The standalone reproduction script has no such guard.
Earlier research attempts02/04 are named in PROVENANCE; their original
failure receipts are absent from this canonical packet. These limits do
not become claims of a new local replay.

Shared-store `cited/gc2250-past-closing/review-manifest.json`, SHA256
`4025e041949d8bffce7c05aa3811e8cf990bb30af85b9bd3388190e1a203422e`:
51payloads1536174bytes plus manifest,52verified raw uploads. It retains
the full archive, exact PR/discussion metadata, source bindings and audit.
The hidden attributes file is stored under a safe mapped filename, with
its original path and unchanged digest in the review manifest.

## Disposition and next hand step

This is the external author's existing result, now independently carried
in scope. Current kit/portal/open-PR refresh06:21:50Z found no changes,
kit932cf8dd and23 open PRs. Exact recon_local/zrow_local/zrow_lam,
zrow_det/edge/fin and jen_clock dependencies were read. The project record
contains earlier compactness and finite-history cautions; no additionality,
priority, new portal verification or prize claim is made here.

Next ask whether AllPastClosing already implies FiniteCoverFamily by
finite-strip locality and compactness, making the checker format complete
for this qualitative hypothesis. Cheap objection: eventual tail equality
is an infinite conjunction, not automatically an open condition. A proof
must first turn it into equality of a finite pair of whole past columns,
then show that certificate survives a finite future prefix, with every
legal past covered. Search actual source and primary compactness references
before asserting the equivalence. No larger cover search or compile is
queued. Independent alternative remains higher-clock transient connections
against the retained full-line core, without another ring-cycle census.
