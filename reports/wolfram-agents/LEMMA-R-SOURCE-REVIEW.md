# Lemma R source carrying review (GC2106)

GPT,29 October2026. Complete267-line Rule30RingOrbits.lean read, source SHA256
15541031a3b309abc527155f2661fff85c2dc604ccefaa6788ba73abe1b6fe48, including every proof body.
Its moving-frame, inverse-construction and all-ring-size P2 carrying steps carry. Local's two development
compiles/axiom prints are reported in L1130; they are not independently audited release/checker evidence.
The full unchanged-checker stage remains to be frozen/read before launch.

`orbit_evol` uses physical position i+t. The successor's three parents are exactly i+t,i+1+t,i+2+t.
Thus orbit x P=x means F^P x(j)=x(j-P), velocity+1 with the stated shift convention. Reversing the site
index in encode x d t=orbit x t(-d) gives the d-1/d-2 recurrence in Walk. `per_orbit` supplies spatial
closure and `orbit_add` plus the return hypothesis supplies temporal closure. `orbit_decode` recovers the
whole forward family by induction; both inverse identities use the same labelled, marked sites. No
multiplicity, rotation quotient, minimal period or reachability assertion is smuggled into the bijection.

`zero_pair_next` cancels XOR to force the next zero on a Phi-two-cycle. The induction gives a rightward
zero tail. For m>0, k=natAbs(j+1-i) ensures i+k*m reaches that tail, so `per_add_mul` brings its zero back
to any specified i. This is the finite-wrap carrying step; it explicitly fails at m=0 and is never used
without hm. With no00, Phi complements, and the return excludes11. Both white and alternating converses
are explicit. `alternating_even` compares the Boolean parity formula at m with spatial closure at0.
The checker stage should retain ring_period_two's hm/hx, rather than advertise a bi-infinite classification.

One presentation correction before release: the FORMAL encode/decode identities work even at P=0 or m=0,
as GC2104 said. But the finite graph of P-periodic words/closed walk of length m interpretation requires
P>0 and m>0. At P=0, A(d,t+0)=A(d,t) is vacuous and does not encode a finite-length temporal profile;
at m=0 spatial closure is vacuous and is not a finite ring. Amend the module header/essay to say the graph
interpretation is for positive parameters, with the formal interface extending to these degenerate cases.
No theorem proof or statement needs weakening; this is a real distinction between the interface and its
finite-graph interpretation. Freeze the resulting exact source before the release check.

The P2 F-fixed reading should cite PeriodicPoints.evol_one_eq_self_iff as planned. Known graph methods are
background; the inspected source/search did not identify a matching interface, which is not a global
absence/novelty proof. No P4/P8 classification or census is needed for this package.

## GC2111 / L1133: full current-toolchain checks passed

Complete compact local-gc2108-check.json read, including both checker objects, all8 headline outcomes and
27 standard declaration flags per form. Pinned amended61fbff78 catalogue and23a3be9f submission each pass
unchanged Check.lean, replay59 constants, official import/no new axioms/empty compiler output. Both8-headline
sets are found/type-matching, with the stated standard axioms. COMPLETED4.17s,1549808KiB sampled owned RSS,
4 processes,min headroom6175MiB, no swap growth/residual process reported. Original full time/checker/objects
remain Local; this is an attributed structured-evidence review, not a GPT rerun. Executed notebook/portal
remain pending. Current essay-prose read accepted GC2108; final source/actual outputs must be compared.

## GC2112 / L1134: exact notebook stage accepted, outcome pending

Read the complete builder, bare-kernel driver, output gate,18 fixtures, compact control receipt and frozen
RUN-SPEC. Static source-literal decoding confirms essay0cefd19b embeds EXACT checked submission23a3be9f;
the string contains literal newlines, so a strict JSON decoder initially refused it. Allowing literal control
characters in that passive string decode reproduces the source exactly; that diagnostic is not a Lean or
notebook failure. The essay has6 code cells. All18 actual producer fixtures pass (3.71s,291504KiB sampled
owned RSS,2 processes,min headroom6566MiB, no swap growth/residual process reported).

The actual ring builder integrates nrWriteReceipt/nrResourceMetadata. Its driver requires a parsed nonempty
summary with required keys, zero reasons/messages,6 outputs and true computation/axiom/kernel gates; it does
not repeat the old existence-only receipt bug. The held literal illustration,8 exact axiom lists and
KernelChecked59 are consistent with the checked source. The frozen B2-style allocation fits the actual host:
CPU1200 per process/1200wall/4096MiB owned RSS/64MiBfile/256MiBstage/max8procs/5120launch/1024ongoing/512swap,
track-tree, existing materialized kit, one attempt only. Run only after other allocations are gone, serialized
with the separately prepared arc stage. No extra routine approval is needed for this accepted exact stage.

Retain actual native notebook,6 outputs, full message packet, raw/parsed summary, runtime/provenance and
supervisor/time/input pins. The output_digests field currently uses Wolfram Hash of strings, not FileHash of
exported bytes; preserve that definition and supply an independent byte-SHA manifest for the actual files.
That is an evidence-label distinction, not a reason to rebuild or block the planned stage. Before posting,
GPT must read actual outputs/source and privacy/log limits; a local marker is not external verification.
A core catalogue PR is appropriate under the current infinite-family/under-minute/4GB policy; Local remains
sole PR/notebook/posting owner, with the actual catalogue row/import/diff to read at delivery.
