# endpoint digit certificates

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT68. endpoint digit
certificates (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

At a first dip, the start and the end share the same height limit.

**What it says.** For a pattern whose growth factor first dips below 1, a start survives exactly when the start is
at most the ceiling, and equally exactly when the end value is at most the same ceiling. GPT also gave quick tests
that read only the first few or the last few steps of a pattern and can rule out the whole pattern at once.

**Why it matters.** Two descriptions of the same exceptions agree, which makes them easier to count and check.

**An everyday picture.** A door you may enter only if you are under a certain height, and leave only if you are
under the same height.

## The formal statement and proof

### G68. Two endpoint ceilings and nested digit exclusion certificates (2026-10-06)

Continue G67's residue-sensitive audit. This is an elementary consequence of G45/G48 and Local's least-terminal-residue lemma in COLLATZ-PRIZE.md §4, not a new distribution theorem or a novelty claim. G67's ordering counterexample and G46's rounding obstruction remain controls.

Let w be a first coefficient-deficit word of length t with a>=1 ones, M=2^t, A=3^a, D=M-A>0 and affine intercept B. Put K=floor(B/D). Its least realizing start is r in[0,M-1] and its least terminal value is y=T^t(r) in[0,A-1], with

    M*y=A*r+B.

Both r,y are positive: a word with at least one odd step cannot be the itinerary of0, and T preserves positive integers. Every positive realizing lift is n=r+M*m, with terminal q=y+A*m and m>=0. Every proper prefix has coefficient greater than1 and nonnegative intercept, so actual survival through t is equivalent to q>=n at the final step alone. The affine relation gives two forms of the gap:

    q-n=(B-D*n)/M=(B-D*q)/A.

Consequently q>=n iff n<=K iff q<=K. Thus start and terminal have exactly the same ceiling, despite different moduli. The two exact lift counts agree:

    max(0,1+floor((K-r)/M))
      =max(0,1+floor((K-y)/A)).

This is an identity of the same lift parameter m, not an independence assertion. The a0 word0 is separate, with no positive survivor.

**Partial digit certificates.** A prefix u of length s has intercept C_u and odd count a_u. Every realizing positive n satisfies

    n = -C_u*3^(-a_u) mod2^s.

A suffix v of length ell with b ones and intercept C_v satisfies2^ell*q=3^b*x+C_v for the intermediate integer x, so every positive terminal q satisfies

    q=C_v*2^(-ell) mod3^b.

Inverses exist in the indicated moduli; with s=0 or b=0, modulus1 is interpreted as the sole residue0. For a residue rho modulo H define its least positive representative L_H(rho)=rho if rho>0, and H otherwise. If either the prefix representative or suffix representative exceeds K, the full word has no positive actual survivor. This gives independently checkable exclusion certificates without assuming uniform residues or multiplying densities. It uses the exact full-word ceiling; no efficient method to sum such certificates over all words is proved here.

These lower bounds are nested as information increases. Each longer prefix has the same residue modulo the shorter power of2. Each longer suffix has the same terminal residue modulo the shorter power of3; this also follows directly by reducing its affine identity. The positive representatives therefore cannot decrease. At full prefix or full suffix length the tests are individually complete, giving r>K or y>K. Before full length, passing either or both is only absence of an exclusion certificate.

**Unexpected sufficiency guard.** The first-deficit word1101100 has K1,r59,y38 by G67. Its one-bit prefix1 permits positive start1, and its two-bit suffix00 has b0 and permits positive terminal1. Both partial lower bounds equal K, yet the full word has no positive survivor. Thus passing two partial endpoint tests is not a survival theorem. This analytic counterexample is deliberately retained alongside the stronger tests; no computational experiment was needed to derive it.

The unresolved task is an arithmetic bound on how many barrier words escape short endpoint certificates, with rounding retained. The lemma changes the available certificates, not the known all-horizon stopping status. Independent Local reading requested.

**Next controls, preregistered NOT RUN.** EC1: exactly the existing791 first-deficit words throughlength16, check the terminal formula and equality of both lift counts; independently evolve all claimed surviving positive lifts. EC2: for every prefix/suffix length of every nonzero-a word in that population, check the two congruences, nested positive lower bounds, sound exclusion and completeness at full length. Record minimal binary-prefix and ternary-suffix certificate lengths for the256 G67 extremizers; predict all a2..256 have both full certificates, while a1 has none. No short-depth asymptotic prediction or new horizon. Counterfactual: passing two partial endpoint tests suffices for survival; must fail on1101100 with prefix1 and suffix00. This is a bounded instrument audit and keeps Local's computational lane free.


### G68 controls outcome (2026-10-06)

EC1 passes791 first-deficit words throughlength16: both endpoint lift counts agree on all791, with one positive surviving lift independently evolved (the known n1 return). EC2 passes25358 prefix/suffix endpoint congruence checks, including monotone positive representatives, sound exclusions and full-length completeness. The a0 word is separately checked to have no positive survivor. The unexpected partial-sufficiency counterfactual fails on1101100 exactly as predicted.

All255 G67 extremizers with a2..256 admit both certificates; a1 admits neither. Minimal prefix-length frequencies (length:count) are0:1,2:2,4:15,5:32,6:57,7:68,8:35,9:24,10:11,12:6,13:2,15:2. Minimal suffix-length frequencies are0:1,3:2,5:2,6:7,7:21,8:35,9:87,10:62,11:11,13:23,15:2,18:2. Zero-depth exclusion is the a2 word, whose ceiling is0; it does not imply a zero-length word or a nontrivial residue constraint.

Post-control diagnostics identify the two maximum-depth cases as a200 and253: prefix15, suffix18 containing11 ones. The largest sampled ceiling is19584 at a253. These are descriptive finite maxima, not preregistered depth bounds, asymptotic rates or evidence of independence. All256 individual records are retained outside git; the probe reproduces them with an optional output-file argument. Probe: `tests/probes/prizes/collatz_gpt_endpoint_certificates.py`; Python on GPT's Intel host, about6 s. No control failed.

The bounded instrument audit is complete; independent proof review remains pending. Next reasoning/source audit: whether established lower bounds for linear forms in logarithms give a uniform polynomial envelope for G67's near-resonance denominator, and what that envelope actually says about counts. No such bound is claimed yet, and it would not by itself prove an actual survival estimate. No larger census or additional run is started here.
