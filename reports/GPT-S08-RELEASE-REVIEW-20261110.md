# S08 plant: complete source and release read

GPT GC2811, 10 November 2026. **Full mathematical/source read PASS. Corrected text accepted; posting clearance is conditional on the routine nb2 gates below.** This packet is BR3.2 only. The hybrid BR3.1 remains separate. No new notebook build, Intel Lean run, submission or public verification is claimed by this review.

## Full carrying read

Read all **698 kit lines and694 portal lines** of the actual L1628 packet (the ledger's671 count was stale), not just headline statements. Source regeneration, the two Check receipts, complete assembler, notebook driver, Python replay, five-mutant source/output, wrapper, essay/abstract/PR body and integration patch were read. GC2804's independent hand carry and147 exact table controls remain the finite baseline; no duplicate495-case census was launched.

### The three L1628 questions

1. **Inclusive convention: correct, including W0.** `survZ`/`survT` take `List.range(t/2+1)`, hence check exactly `0,2,...,2*floor(t/2)`. The current even tick is included; an odd t adds no new check. `ofNat Y k` reads bit `k-1` at positive depths and sets depth0 white. `Y<2^W` is width **at most** W, including zero. At W0 only Y0 is counted; its initial depth1 check is white, so both survival counts are0 at every t. Since L>=1, W0 is always in the unchanged branch.
2. **Two exceptions and injection: correct.** The proof of `survival_table` is carried in detail below. The exception uL and the omitted um may coincide (m=L); the proof never assumes they differ. The dying truncated stripe uses exactly `trunc_survives`, rather than an earlier-pivot substitute.
3. **Domain: correct in the definitions; made explicit in the prose.** `psi`/`psiInv` are automorphisms of all row sequences. On positive-depth finite rows, `psi` maps the finite rows together with the stripe onto the finite rows; its restriction is not a permutation of finite rows. `psiInv_fin` excludes exactly the stripe image. Depth0 is ignored by the zero-boundary flow, and every conjugacy/congruence assertion requiring this is restricted to positive depths. No equality of differently normalized wall cells is assumed.

### Automorphism, flow and finite support

`pf x k` means agreement at depths1 through k-1. It never reads depth0. `site` only flips odd k>=2L+1; the input at k does not enter its own flag. The inverse flag reconstructs previous input cells, so `pf_psiInv`/`ipf_psi` and the two cancellations are valid on all rows, before any finite-support argument.

The finite-inverse lemma proves an upper bound, **not equality of actual widths**. If an inverse of a finite row has a black cell beyond W, it must be a flip site with the entire earlier inverse prefix striped. The induction then forces the full inverse to be the stripe, contradicting the excluded image. `psi_fin` separately bounds forward growth by2; it is not a permutation of the finite-width set.

`Tn_eq` uses the genuine zero-boundary semiflow/congruence lemmas and cancellation on positive depths. For L>=1, depth1 is below every flip site, so its observation is preserved. `T_fixed` follows from the stripe fixed point, and `fixed_survives` uses L>=1. The finite-support proof handles the exceptional stripe inverse separately; all other rows have finite inverse, then support grows by1 under the kit step and by at most2 under psi. No width-growth equality or homogeneous-rule property is transferred to T.

### Finite counts and the exact table

The encoder lemmas give a bijection between `Y<2^W` and positive-depth rows supported at depths<=W. `cnt_update`, `pigeon` and `cnt_perm` were read in full: the latter completes an injective self-map of a finite range and preserves counts, without an unproved surjectivity shortcut.

In the high-width branch put `m=floor((W+1)/2)=ceil(W/2)`. Then m>=L>=1, and both uL and um are below2^W. On all inputs except uL, the finite inverse fits within W and is encoded exactly. It cannot be um: applying psi would force a black cell at depth2m+1, beyond W. The nonexceptional map is injective by the automorphism identities and exact encoding. Define its missing value by `f(uL)=um`. This is an injective self-map of the full range, so `cnt_perm` applies.

All nonexceptional survival predicates correspond. At the exceptional input, T survives forever, whereas the reference predicate at um is `decide(t<2m)`. The one-value count update therefore gives precisely

```text
S_T(W,t) = S_F(W,t) + [2L-1 <= W AND 2*ceil(W/2) <= t].
```

The equality case t=2m is handled correctly: the failing even check is included. The low-width branch proves pointwise identity of the inverse on the counted rows. It uses the forced mismatch at the black stripe depth2L-1 beyond W; this argument includes W0 and avoids invoking m=0 in `trunc_survives`.

## Text repairs: no declaration/proof code changes

Two scope corrections were applied consistently to the Lean comments, abstract/essay, PR body and integration row:

- **Finite portions, not an impossibility assertion about the infinite table.** The original wording said survival counts alone cannot decide Q01. The actual construction matches arbitrarily large finite portions: choose2L-1 above any fixed width cutoff for agreement at all times, or choose2L above any fixed time horizon for agreement at all widths through that horizon. These are immediate consequences of the two guards. The full infinite table can encode the assertion that each finite-width survival count eventually vanishes; the construction proves no general impossibility theorem about that infinite information.
- **Nonincreasing inverse width, not exact width preservation.** `psiInv_fin` proves `Fin_ W` is retained off the exception. For example at L1, inverse of the three-bit row5 is the one-bit row1, by direct reconstruction of its first three cells. Replaced keeps the width/same width by does not increase width. Also made the finite-rows-plus-stripe domain explicit. Neither correction changes any theorem statement or proof.

After removing comments and normalizing whitespace, the complete declaration/proof token stream is unchanged: SHA256 `df02e035f5af44b3373857f404a6871b1d3888742fc6b7fdd0938785d062e283`. This is a source-identity check, not a new Lean compile. The assembler's description now retains both guards; it previously mentioned the width cutoff alone. Title, ten headlines, computation and notebook driver are unchanged.

## Inputs, receipts and artifact

Both old source forms passed official Check,266constants,79kit/91portal declarations, ten headlines, standard axioms/no new axioms. Actual receipt fields were checked for every declared standard-axiom flag and every headline's found/type/ok/problems/axioms. Five mutant proofs fail as reported; compiler rejection alone is not promoted to a mathematical refutation of each altered statement.

The exact current03a19bf6 and verifier5fb59158 imported definitions were compared. ZeroBoundaryBarriers, Jen and Prize are byte-identical; ZeroBoundary differs only by93 appended IntegerForm top-bit/time-injectivity lines, unused here. The used zrow/stripe/truncate/shift/congruence and trunc_survives definitions/proofs agree. Actual Realization input used by Barriers is the same reviewed source. No unused newer theorem is smuggled into the verifier form.

The complete unchanged notebook driver `6deef68944e37e538f1a025b773d7b6ceb803a662341e17a042d9901ca2304b8` checks actual iconized source bytes, exact Abstract, six outputs/no messages/$Failed, exact numerical cell, ten portal axiom sets and KernelChecked266. Its helper/structure are the reviewed inherited workflow. The Python/Wolfram computation shares the intended bit-depth and inclusive conventions; None is the stripe inverse, not a numeric row. Numerical cells are illustrative controls, not the proof of the all-width identity.

Old nb1 was fetched from `cited/local/planted-survivor-nb1-20261110.tar.gz`,50565bytes, SHA256 `f519baa08f79733d2e3ad3327a7af2a77b73ed69c383ad841a1a0ac151d405d3`, verified exact. Actual serialized notebook149053bytes, SHA256 `8670737a04fae33744eafe2d1712aa19187dcf244d9f8743f47c76beeb238db2`, passes source/abstract/title/six evaluated outputs/no Messages, numerical `{True,495,{0,0,0,1,1,1,1,1,1,0,0},True,True}`, ten names/axioms and actual KernelChecked266 **against the OLD text**. Its summary/driver digest/RESULT OK were read too. It is now superseded; no corrected artifact has yet been built or inspected.

The wrapper's old logic/pins were fully read. It refuses the corrected portal source at its digest check, before network or Wolfram. This is the expected stale-artifact control. Do not post oldnb1 with the corrected text. No Intel Wolfram, Lean build, new census or heavy job was run.

## Conditional posting clearance: exact executable next step

Local's existing Wolfram/build/post ownership remains. These routine gates complete clearance without another owner permission or independent mathematical approval round:

1. Rerun official Check on both corrected source forms (comments only changed); expect the same266constants/tenheads/standardaxioms and normal79/91 declaration counts. Regenerate portal from kit and essay from the corrected inputs exactly.
2. Build corrected nb2 using the **unchanged reviewed driver**. Require exact new source/abstract/title, iconized source, six evaluated outputs, no Messages/$Failed, the unchanged numerical cell and ten axiom sets, and KernelChecked266. Preserve immutable evidence with verified raw-body readback.
3. Update exactly four wrapper pins: **notebook, portal source, abstract, essay**. Keep title/headlines/driver/helper/logic unchanged. Pass the fresh public-verifier dry guard and fresh pre-post known_find. If verifier/source/driver/proof logic changes, reopen the affected read rather than assuming clearance.
4. Post once and open the kit PR with the corrected module/filled integration row, under the owner's standing consent. Record actual public files/check/status separately; no duplicate post or Human Verified claim.

Corrected pins:

```text
kit        372ad3943bf4d530752fe6b4bc77b7cbb70a149e19ae9a5d20931e9bbbf02730
portal     51bdd2422745d50ba3bb616d3504e08594477849d99e8830f8f9d6331cf0589a
abstract   50da26094fbbfc9787b5169a15cbdb70cf2a885055d2a8d93813ea2a6382a43b
essay      a80074e19b0939d0847966d31c8cc71d3b0059a3f4b9cec79bdb19923b9770f5
driver     6deef68944e37e538f1a025b773d7b6ceb803a662341e17a042d9901ca2304b8
headlines  1a086963009e6583c0e60b3ef1d3cff0a16420dd1678f9bafdf85fdd1cb927e1
title      d68cf0a256ef380e18d020c59f5376c35acdcf25cce0d1fcf0e679708e24c8a4
```

Prior-art/provenance: GC2804's full BR3.2 and grouped record-skeptic carry, actual kit03a19bf6 lean/equivalents/catalogs and imported proofs; prior generic conjugation/transducer and sibling-rule context remains credited. Fresh complete known_find 2026-11-10T13:04:57.253726+00:00 (portal13:04:53Z,25PRs) reports0additions/changes/removals from the already-read12:58 checkpoint. No new competing plant statement appeared; no priority claim follows from the search. S09/other research is not reopened. Next GPT task is returned source/artifact release reads while Local completes the agreed queue; no extra census is requested.
