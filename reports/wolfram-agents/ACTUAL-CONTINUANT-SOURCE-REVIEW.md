# Actual continuant data and finite-carry instantiation (GC2144)

**Execution update:** the10:28 gate deferral was followed by the single L1159 stage once headroom recovered.
It failed in MechanicalCarry, while both core components pass4.35; GC2145 retains the full failure and
freezes a targeted instance/deprecation source repair. These two adapters remain UNCOMPILED and are not
added to that repair stage.

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

## GC2148: finite threshold/coefficient selection uses actual kit inputs

Two further UNCOMPILED sources, with no added validation run:

- FiniteHorizonSelection.lean SHA256c416f5cefb2e72774d1d7916eb7f62577d9f652a89b2b99ee55cde2a1ef770bf:
  coefficient_one, crossing_before, crossing_scale, successive_ge. A>=2 and next=A*q+previous together
  with next<=2q+2C+6 force previous<=2C+6; hence above that threshold the coefficient is1. Threshold selection
  uses induction on a supplied finite witness, not Nat.find, and needs no monotonicity for the crossing itself.
- ContinuantSequence.lean: denominator_zero, denominator_recurrence, denominator_unbounded,
  denominator_successive, threshold_crossing, using the ACTUAL ArcRotation denominator. Source digest is
  recorded in GC2148. Lagrange.contQ_ge gives the explicit unboundedness witness B+1; the positive recurrence
  gives successive nondecrease, including the possible initial equality q0=q1=1.

The core adapter is instantiated in the second file: q0=1 and qr<=T<q(r+1) are not merely assumed for an
arbitrary substitute model. The offset recurrence q(n+2)=a(n+2)q(n+1)+q(n) avoids Nat-subtraction index cases.
Core lemma signatures were checked from the installed Lean source; current4.35 elaboration still awaits a
future separately frozen integration. No result is upgraded from source preparation alone.

Local: please include this coefficient/selection carrying read with the actual index/sign adapter read,
not an extra compiler run. First finish/review the seven-head repair's actual outcome. Then locate exact
previous arc module objects and agree one dependent-source integration plan. Do not rebuild Mathlib or
widen an active stage silently. Opposite-arc separation and the complete251 theorem remain unfinished.
