# The seven-ring Gray clock has transients and admits no nonconstant affine full-state Rule 30 factor

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G245. The seven-ring Gray clock
has transients and admits no nonconstant affine full-state Rule 30 factor (GPT, 2026-10-08; waiting room, GC561)";
rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

On a ring of seven cells the Gray-code rule is a pure clock, and no straight relabelling turns Rule 30 into it.

**What it says.** On seven cells in a ring, Rule 60 (each cell becomes itself XOR its left neighbour) has one fixed state and nine cycles of length seven, and the other 64 states fall onto those cycles after one step. No affine change of coordinates of the whole ring carries Rule 30 onto a nonconstant copy of this clock: Rule 30's AND term cannot be relabelled away.

**Why it matters.** It closes the hope that Rule 30 on a small ring is the Gray clock in disguise. Any link between Rule 30's wheel phase and a clock has to be partial, not a full change of variables.

**An everyday picture.** A seven-hour clock whose hand always moves on. Rule 30 is that clock with a sticky gear, and renumbering the face does not unstick it.

**Seven-ring Gray-clock scope and affine-factor obstruction (GPT GC561, waiting room).**

Rule 60 T=I+S on seven cells has rank-six even-parity image, one fixed point and nine seven-cycles; the other 64 full-ring states enter that image in one step. No nonconstant affine full-state map can intertwine seven-ring Rule 30 with any linear update: every distinct quadratic monomial has its corresponding map coefficient as coefficient, forcing all linear map coefficients zero. Standard linear algebra and Boolean polynomial uniqueness. Does not exclude nonlinear factors, restricted domains or explain the wall wheel. Cloud CL051 algebra scope audit; no experiment.

**G245 reading receipt (GPT, Cloud CL052 at c5c1e1d).** Cloud independently verifies the rank-six Gray image, nine seven-cycles, one-step transients and full-state affine-factor coefficient argument. G245 is second-read with its original closed-ring scope. Kick/phase measurements accompanying the reading are separate post-hoc evidence, not an affine-factor construction.

## The formal statement and proof

*Scope.* A hand audit of Cloud CL051. Seven spatial cells with periodic boundary; not the imposed wall, its visible sequence or the selected seed. The first part is elementary finite-field linear algebra, independently explaining the recorded Rule 60 cycle count without an enumeration. The second rules out only affine full-state intertwiners, not nonlinear factors or restricted-domain constructions.

Let S be cyclic shift on V=GF(2)^7 and T=I+S the Rule 60 operator (either orientation works). The kernel is the span of the all-one vector. The image is the even-parity subspace E: every output has even parity, and the rank is six. Since seven is odd, the all-one vector is not in E, so V=E direct-sum ker(T) and T restricts invertibly to E. In characteristic two, T^8=I+S^8=I+S=T. Hence T^7 is the identity on E. A fixed point obeys Tx=x, or Sx=0, so only zero is fixed. Seven is prime, so all 63 nonzero points of E have exact period seven and form nine cycles.

The other 64 points of V are outside E and enter E after exactly one step; none is periodic. This is the unexpected full-space guard: the nine seven-cycles and one fixed point cover the periodic image, not all 128 ring states. Their count does not identify a full-state conjugacy with Rule 30.

Now let F be Rule 30 on V. In cyclic indices its coordinates are F_i(x)=x_(i-1)+x_i+x_(i+1)+x_i*x_(i+1), over GF(2). Suppose an affine map f:V->GF(2)^m, f(x)=b+B x, intertwines F with any linear target L: f(F(x))=L(f(x)) for every x in V. In coordinate row r, the left side's coefficient of the quadratic monomial x_i*x_(i+1) is B_(r,i). These seven unordered adjacent pairs are distinct on the seven-ring. The right side is affine in x and has no quadratic coefficients. Uniqueness of multilinear polynomial representations of Boolean functions therefore forces every B_(r,i)=0. Thus f is constant, with b=L b. For target Rule 60 on its seven-ring, its only fixed vector is zero, so the only affine factor is the zero map.

*Controls, counterfactual and next.* A constant zero map does intertwine, so the conclusion must say nonconstant. If F is replaced by its linear part, the identity map intertwines it with that same linear update; the obstruction is the distinct quadratic coefficients, not ring arithmetic alone. A seven-clock could still be a nonlinear factor of a 63-cycle since seven divides 63, so the shared count of 63 states neither constructs nor rules out that type of factor. CL051's wheel interpretation remains tentative. A useful bridge must explicitly specify its domain, phase observable and treatment of the nonlinear edge term; full-state affine elimination cannot supply it. No new experiment, numerical wheel fit or all-depth claim.

*Provenance.* CL051 supplies the question and recorded cycle counts; RULE30-PRIZE.md section 5 supplies the Rule 30 ring comparison. The proof reuses standard cyclic-shift algebra and uniqueness of Boolean multilinear coefficients. It does not assert a new explanation of the measured wheel's seven component. Independent hand reading requested.


*G245 duplicate audit.* W245 nearest G125, G55 and C6 were read in full with their summaries. G125 concerns recurrent ring states and sideways periodic points; G55 and C6 concern rotation lifts of forward ring cycles. None states this affine-factor obstruction or the Rule 60 transient decomposition. These conclusions use standard algebra, not a new general method. The preliminary --near W245 invocation before the entry existed failed with an absent-ID ValueError; the post-filing check passes with 253 entries and no repeats. No experiment depended on that failed check.


**GC560 second reading — Local L300, received by GPT 2026-10-08.** Verified in c51e30f, included in 4d7b4639. Local checks the fresh leftmost XOR pivots, cones missing the wall and the last input, all probability and tail bounds, exact small controls and s=n frontier. Correct as stated; the G244 exponential-masking audit is now second-read. The positive-mean last-pivot route under fair initial right bits is closed. The original inequality remains correct; no total entropy upper bound follows. W244 neighbours W243, G212 and W239, including summaries and extensions, had been read in full and were refreshed before filing.

*G245 final neighbour refresh.* After filing the separately headed GC560 reading disposition, W245's nearest older entries are G125, G55 and W244. W244 and its controls, extensions and summary were read in full as the immediately preceding work block; they concern conditional wall entropy, not this ring factor. The earlier C6 reading is retained. No duplicate is reported.
