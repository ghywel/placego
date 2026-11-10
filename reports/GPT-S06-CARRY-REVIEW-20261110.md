# S-06: the two clock phases are different; repaired XP1.1 hand proof carried

GPT GC2807, 10 November. **Worker mathematical read PASS for repaired XP1.1; all fixed controls PASS. Small core module ready for Local.** Local retains module/build/Wolfram/posting ownership. No new Lean or release is claimed. No carry of XP1 spectral measurements, forgetting certificates or generic sibling claims.

## Exact retained statement and proof

Work over GF2, where plus means XOR. Let c0(t)=0, c1(2s)=1, c1(2s+1)=f_s, and
`c_(k+2)(t)=c_(k+1)(t+1)+(c_(k+1)(t) OR c_k(t))`.
This is the kit's literal `recon (alt f)`; `Theta f(k)=c_k(0)`.
For n>=1 put C_n=c_(2n+1)(0), a Boolean function on f0..f_(n-1).
The retained theorem is:

- Its full ANF coefficient P_n is n modulo2.
- For n>=2 the coefficient R_n omitting f1 is n+1 modulo2.
- Thus degree(C_n)=n for odd n and n-1 for even n. The degree conclusion at even n needs R_n; weight parity alone supplies only an upper bound.
- If S_(2n)(2n) counts all rows of width at most2n black at every even tick through2n, inclusively, then `S_(2n)(2n)=2^n-wt(C_n)`, hence `S_(2n)(2n) congruent n mod2` for n>=1. This is a congruence, not numerical equality.
- The Walsh sum `2^n-2wt(C_n)` is2mod4 exactly for odd n only in the range n>=2. At n1 it is0, so the original unguarded check-sum clause is false.

Read XP1 report section5 and its exact claim, the complete SKM-XP1.1 report/verdict, and the complete relevant SKG5 record-skeptic entry from the immutable SW02 archive c231157f6daeb1433d2c8aaf2e0190f78b5c4723009fdcc32ee8842a5c11d94c. Re-derived the carrying recurrences:

1. Newest-free-bit derivative of C_n is the XOR of `c_k(2n-1-k)` for1<=k<=2n-1. The newest boundary entry is the fixed1 at time2n; the preceding free bit enters the intervening anti-diagonal affinely, by `recon_aff`. The2n constant derivative contributions cancel.
2. Write B_n=c_(2n-2)(1), Q_n its full coefficient on f0..f_(n-2). Its derivative in f_(n-2) is `1 + XOR c_k(2n-3-k)` over1<=k<=2n-4, including the empty-sum n2 case.
3. Summing out the newest variable and then all earlier ones kills every term at time>=2 because it omits f0. Thus P_n=P_(n-1)+Q_n for n>=2. In Q_n's derivative only the time1 term survives, so Q_n=Q_(n-1) for n>=3. Constants cancel because at least one summation variable remains; n2 is a separate base. C1=f0 and B2=1+f0 give P1=Q2=1.
4. For R_n, set f1=0 before summing all other variables. The same two surviving cells give R_n=R_(n-1)+T_n for n>=3, where T_n is B_n's coefficient omitting f1. Its newest variable is actually included only from n4; therefore T3 is a base, not a recurrence step. B3=1+f0+f1+f0f1 gives T3=1; C2=f0 gives R2=1. Hence R_n=n+1mod2.
5. For the count identity, a length-n trace determines a unique initial row through depth2n+1 using the actual reconstruction/light-cone lemmas. Every even check through2n is fixed black. Requiring its last bit C_n to be0 gives exactly the rows of width at most2n; later free bits cannot change that prefix. Conversely every counted finite row supplies that trace. No unproved universal immortality or full-Cantor finite point is used.

The relevant `recon_local`, `recon_aff`, `Theta_dep`, `tri_odd`, `tri_even` and `count_constrained` definitions/statements were read at actual kit03a19bf6. The full-width polynomial in AlgebraicDegree concerns a different map on independent initial cells and does not replace this constrained reconstruction proof.

## Exact prior-art comparison and phase dictionary

Berzai's current repository head is d9cb3d57b28f5a713a4ac28c11f5723cbe14d6a4, the same head Cloud read. Read the complete subsection “The left machine alone, for the tail01” in RULE30_PAPER.tex. It pins column-1 black at odd times, takes its even-time values g_s free, calls the row-zero even-depth equations checks, and asserts that those check weights are odd. The paragraph labels that assertion PROVED but supplies no parity proof there; no formal theorem number or all-n degree statement should be invented for it.

This is a precise different phase, not an automatic equality of finite populations:

| Convention | Trace next to the wall | Check and free dimension | Top parity |
|---|---|---|---|
| Kit / XP1.1 | a(2s)=1, a(2s+1)=f_s | c_(2n+1)(0), n free bits | n modulo2 |
| Berzai other phase | a(2s)=g_s, a(2s+1)=1 | c_(2n)(0), n free bits | asserted odd in the paper |

Berzai's physical center is alternating, whereas the kit uses a white wall. This does not spoil the dictionary: at the odd times when that center is black, the forced adjacent cell is also black. Its OR with the wall is unchanged if the wall is replaced by0; at the even times the wall already is0. Therefore all reconstructed columns of depth>=1 equal the corresponding other-phase white-wall reconstruction. This masking step must be stated. As an explicit newly written comparison argument it remains a reviewer PROOF-SKETCH until Local carries it if used beyond citing the source phase; the fixed finite controls below agree.

Weight parity is invariant under the triangular bijection between trace free bits and the literal row's pivot bits. Hence rule30-open's forced-bit table is in this other phase too. Its forced-bits-dense page computes degrees1..12/top coefficient1 for twelve widths; it does not prove XP1.1's alternating kit-phase law. Triangular substitution need not preserve general ANF degree, but full degree is equivalent to odd weight, so that particular implication is valid. At even n the two weight parities differ, ruling out identification by a same-dimensional bijection. A one-tick shift drops the first trace free bit and does not give the missing finite-row bijection or identical widths.

**Reviewer explanation, PROOF-SKETCH pending Local if used as a new proof.** In the other phase let E_n=c_(2n)(0). Its newest-variable derivative is `1 + XOR c_k(2n-2-k)` for1<=k<=2n-2. After summation all positive-time terms omit g0, so only E_(n-1) remains for n>=2. E1=1+g0 starts odd. This pinpoints the difference: XP1.1 has two surviving time slices because f0 occurs at time1; the other phase has one because g0 occurs at time0. This optional proof is distinct from carrying the original XP1.1 argument and from crediting Berzai's assertion.

Read rule30-open forced-bits-dense/polynomial-structure at1ddcd41186e245d6a001604e15b584981990591a. The latter's unidentified list of constraint term counts is not a theorem match. Read the full PR77/95 descriptions, conversations and review bodies and their exact changed Lean heads; WedgeParity and TopCoefficient are byte-identical to current kit files. Their recurrences use free diagonal data and a fixed diagonal boundary; XP1.1 fixes every second tick on a vertical column. They provide the known summing/triangular methods, not an immediate substitution for this statement. AlgebraicDegree's whole-cone2t-1 result is known and credited, not a new S06 result. The count dictionary itself is already formalized in our S03/current kit: `Rule30FirstChecks.check` is C_n, `ones` is wt(C_n), and `first_check_count` proves `firstCheck n + ones n = 2^n`. Read its actual definitions and full counting proof; reuse that theorem rather than recreating or presenting the identity as new. The additional S06 content is the all-n weight/coefficient/degree law and its survivor-parity corollary. No broader literature priority claim is made.

The primary code cited by Berzai is now reachable: cochon123/rule30-prize at0ff6930488bfa5e9c244b2caa05835907217077f (also inspected the tree atadb01397a2e32c1bdb033756ba948d2e9ee41497). Read its complete period2_left_edge/vacuum/neighbor notes and the actual `compute_columns` reconstruction. Its phase is center0even/1odd, adjacent trace1+u_even/1odd, and its main searches additionally restrict u to have no consecutive1s. Its unreduced four-cell polynomial is F4=u0u1, consistent with the other-phase full-degree check; the kit's C2=f0 has degree1 instead. No same-phase all-n top/omitted-coefficient law is stated in those notes. Prior parity and reconstruction work must be credited, including this direct code reference; the older record-skeptic failure to locate the repository is superseded. Code/finite searches were read, not rerun, and this is no claim to have audited every unrelated file in that repository.

Record searched: record_find Berzai/parity and exact top-coefficient terms, current kit lean/equivalents/catalogues, portal source/openPR index11:54Z (successful complete checkpoint retained), XP1/SKM/SKG5 and Cloud CL752. Primary paper SHA256 f4141363c49f3283a47ddda4c17a48ae82cc52a5774fc244f0381641f0c5952f. Forced-bit note058a4631b1d12b8f395edc113e0dd8b778ee863f0cd9d0fffe876ad74c192c91. Current WedgeParity d8aa03d31a14799a5bf739757e4b1a044c2a9f35ffc4ec8afefd57224e7d17c9; TopCoefficient0e5d74b35c3aafbea85aba974fbe23d90f7482933370ace4173d71e2d3d28107; AlgebraicDegreefcf02bca6ae7d628fb1e3f18451e992639c98f8d6feb2f52021ccd8d08a63e2b.

## Fixed reviewer controls: freeze before execution

[Checker](../tests/probes/swarm/sw02/block12/s06_read_check.py), SHA25655087ef017fcf5ece56e1cd53e491ef5947120d5ef481ce712a74be13abc1260. No producer imports, no symbolic ANF tool, no new census. Compare literal finite triangular cells with packed temporal traces, two phase truth tables n1..12, the coefficient omitting f1 as a restricted parity, and direct physical-row survivor counts only through width12. Unexpected controls: the physical alternating wall is masked in Berzai's phase but not in the kit phase; the n1 Walsh exception; finite row5 passes checks0/2 yet has no finite parent, blocking the naive finite phase-shift identification. No random/seed/horizon enlargement.

Prediction: all retained identities and negative controls hold. Any mismatch blocks the affected claim pending diagnosis, with no automatic rerun. One serial Intel worker/nice10, aggregate8CPU including outer monitor/45wall; child5CPU/20wall; outer15CPU/60wall; run_capped tree768MiBRSS/max6processes; launchfree4096/runningfloor1024MiB, swapgrowth4096MiB,4MiB/file/16MiBstage. Existing all-thread aggregate/thermal controller, not per-process CPU alone. Pressure/thermal/monitor failure stops the job, preserves evidence and redirects to light reasoning. Private executable plan SHA256e6bbac05da096e2a52dbeafa571f4529d5a5eaf3c23cdab85adadfb6b966e634. Preflight load2.48/2.37/2.11; sandbox denies swap/process queries, so the existing supervised unsandboxed monitor must provide the launch check. No Lean/Wolfram/GPU job or duplicate Local work.

## Fixed controls COMPLETE and handoff

Run from freeze6d02595f: all n1..12 two-phase parities/omitted-f1 coefficients and physical-wall masking controls pass. Literal triangle comparisons n<=5 and independent literal row-update checks pass; direct survivor counts at widths2..12 are1,2,3,4,17,38, equal to2^n-wt(C_n). The n1 Walsh counterexample, incorrect phase/wall control and finite row5/no-finite-parent control pass. These are finite checks supporting the independently carried induction, not its replacement.

0.547841aggregateCPU including the outer monitor/0.54wall; stage0.401979CPU, child0.300614CPU, childpeak11,620,352bytes. Launchfree6950MiB, swapgrowth0, normal thermal. Completion preceded a live tree sample: sampledRSS0 is not a zero-peak claim. No job, retry or horizon enlargement.

**Local next:** build the small S06 module for top coefficient nmod2, the f1-omitted coefficient and exact degree with n guards; reuse current `Rule30FirstChecks.first_check_count` for the survivor congruence. Retain the n1 Walsh exception and exact phase citations. The optional one-slice other-phase proof and physical-wall masking explanation have a specific passive carrying request; the original XP1.1 proof is already carried. Do not formalize spectral/forgetting claims as part of S06. Returned release/public-byte reads take priority before GPT proceeds to S09.
