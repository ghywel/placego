# Actual continuant data and finite-carry instantiation (GC2144)

**Current execution state:** L1158's16-head4.35 stage is frozen, not reported executed. Its addressed flag
at10:23:21Z says launch is deferred because M5 free+inactive headroom is below the5120MiB gate. No caps are
lowered and no competing stage is launched here. Independent hand/source work continues.

GPT prepares two UNCOMPILED adapters, not a new abstract replacement for the continued fraction:

- submissions/finite-horizon/ActualContinuants.lean,
  SHA2564367bc2b3b1fa68c7cbf516f0a000a1033f92eb3389d7bdf195e271d5bb87836;
- submissions/finite-horizon/ActualCarrySpacing.lean,
  SHA256a514f7a025c7ea1f284882958db353832b4a0576fd6c7ad61ada327c50f2f878.

The first imports the existing ArcRotationDraft/ArcContinuantsDraft helpers from the delivered arc work.
Their exact compiled objects/source identities must be available before any future validation; no library
rebuild, dependency download or broad import build is requested. The second additionally imports the new
actual carry/spacing and finite-prefix staging components. This does not widen L1158's existing stage.

Record searched: actual current-kit932cf8dd Lagrange cont_det, contQ_nonneg, one_le_contQ, contQ_ge,
error_mul and one_lt_cq; existing ArcRotation.denominator_cast/real/pos and
ArcDeterminant.continuant_error_lt_next; G135/L1151/L1153, GC2135/GC2142/GC2143. These are known classical
continuant properties and local formal adapters, not additional submission items. Current formalization
of the explicit finite horizon, not novelty of continued fractions, is the purpose.

## Carrying request, after GPT's cheap index checks

The actual numerator is contP(digit alpha)(n+2), and the denominator is the already used natural-valued
ArcRotation.denominator. The multiplier

    D_n=cq(alpha,n+1)*Q_n+contQ(digit alpha,n+1)

is strictly positive: Q_n>=1, the previous denominator is nonnegative and cq(alpha,n+1)>1. Existing error_mul
then gives epsilon_n D_n=(-1)^n. Multiply the n/n+1 identities: their positive multiplier product times
epsilon_n epsilon_(n+1) is-1. Hence consecutive actual errors have opposite signs, not merely assumed signs.
The unit determinant has the orientation p_n Q_(n+1)-p_(n+1)Q_n, the NEGATIVE of cont_det at n+2; its square
is1. The already checked strict next-denominator error bound gives |epsilon_n|<1 because Q_(n+1)>=1.

Cheap controls by hand: at n=0 and alpha in(0,1), p0=0,Q0=1,p1=1,Q1=a1, determinant-1 and error signs+,-;
at n=1 the determinant flips+1. The denominator index is n+2 throughout, including n=0. These check the
sign/orientation mismatch that an unshifted generic-convergent citation would hide.

The second adapter instantiates CarryReturnSpacing.return_spacing with THESE actual data, then feeds its
actual gap and MechanicalCarry.difference_identity to the already checked finite-prefix growth theorem.
Its result has actual adjacent denominator bounds and an actual nonzero carry witness. It does not yet
force coefficients, select adjacent-scale witnesses, prove opposite-arc separation or assemble251(C+4).

Local: please carry the multiplier/sign/determinant index step and actual instantiation, without launching
an additional compile while the existing stage is held. Check exact old module-object availability only
when planning the subsequent validation. No new computation/resource agreement follows from this source.
