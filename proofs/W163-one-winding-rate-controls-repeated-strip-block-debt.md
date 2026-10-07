# One winding rate controls repeated-strip block debt

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G163. One winding rate controls
repeated-strip block debt (2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and
this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

For one fixed spatial pattern repeated forever, all timing phases have the same long-run rate. At whole-pattern boundaries their timing differs from that rate by at most one temporal period minus one. If the rate is at most 5/2 per driver, that gives a small whole-pattern charging potential. Costs inside the pattern and along branching histories remain open.

## The formal statement and proof

**Statement and domain.** Fix a spatially repeated list of m temporal drivers, each periodic with common period P. It may be a compatible Rule30 pair cycle, but the timing statement only uses G8's full-line next-black reset rule. Let F(t) be the integer arrival time after one whole spatial block, starting at integer time t. There is one phase-independent rational rate rho per block such that, for every integer t and n>=0,

    abs(F^n(t)-t-n*rho) <= P-1.

A single orbit of the phase map F modulo P determines rho: if its eventual phase cycle has length d<=P and lift displacement k*P, then rho=k*P/d. All phase cycles have this same rate, even if they do not merge. The per-driver asymptotic slope is rho/m.

At block boundaries, a nonnegative P-periodic integer potential H with

    H(t) >= 2*(F(t)-t)-5*m+H(F(t))

exists if and only if rho<=5*m/2. Whenever it exists, one can choose max H<=2*(P-1), independent of m. This is a whole-block certificate for this fixed repeated strip, not G8's one-edge potential on the entire compatible graph.

**Proof.** A nonzero driver's reset map sends t to one plus its first black time at or after t; a zero driver's map is the identity. Both are nondecreasing and commute with translation by P. Their composition F has both properties. Its phase map is a function on P residues, so every phase orbit eventually cycles. A recurrent lift cycle of length d has displacement k*P; repeating it gives limiting displacement rate k*P/d. If t<=u<=t+P, monotonicity and translation give F^n(t)<=F^n(u)<=F^n(t)+P. Hence any two initial times have the same limiting rate rho, by translating one into that interval and dividing by n. This proves existence, independence and the orbit formula without requiring an invertible phase map.

Fix n>=1 and let D_n(t)=F^n(t)-t. This is P-periodic. For residues t,u with 1<=u-t<=P-1, the previous inequality gives -(u-t)<=D_n(u)-D_n(t)<=P-(u-t). Thus its largest and smallest residue values differ by at most P-1. Write these values M_n and a_n. Iterating F^n in blocks shows j*a_n<=F^(j*n)(t)-t<=j*M_n. Divide by j and let j grow to obtain a_n<=n*rho<=M_n. Every D_n(t) lies in that same interval, giving the claimed P-1 error. The n=0 case is exact.

When rho<=5*m/2, define H(t) as the supremum, over n>=0, of 2*D_n(t)-5*m*n. The n=0 term is0; the error bound makes every term at most2*(P-1). Since these are integers in a bounded interval, the supremum is a finite nonnegative integer, periodic in t. Splitting off the first block gives the potential inequality. Conversely, sum such an inequality over n blocks. A finite periodic H bounds the total reward; dividing by n yields 2*rho-5*m<=0. Equality is allowed: zero-weight recurrent loops do not make the potential infinite. Square.

**Independent existing control.** G8's compatible period4, spatial-length12 witness has F(0)=27 and F(3)=31. Therefore F^n(0)=28*n-1 for n>=1, while F^n(3)=3+28*n; both rates are28 per block, hence slope7/3. The phase-zero first-block slope27/12 is not its asymptotic rate. Its whole-block error from phase0 is1, within P-1=3. No new cycle search was run.

**Identified unexpected check: coalescence is not required.** The all-zero compatible strip gives F(t)=t. Its P phase residues remain separate fixed points, but all have rate0 and H=0. The proof needs weak monotonicity, not invertibility or convergence to one phase. A single pulse at time0 gives a sharp clock-only error control: F(0)=1, F(t)=P+1 for 1<=t<P, and its recurrent rate is P. The error at t=0 is P-1. That single-driver repeated strip is not claimed Rule30-compatible for P>1; it tests the timing lemma's general domain, not a compatible slope obstruction.

**Prior record and limits.** This is the standard monotone degree-one translation-number mechanism, here proved directly on integer times with the discrete P-1 bound. The primary Mathlib translation-number module states phase-independent limits and bounded iterate displacement; no novelty is claimed for rotation theory, and no Lean validation of this application is claimed. G6 already gives phase comparison for a fixed history; G8/G10 already compute exact recurrent phase means. This entry supplies the explicit whole-block potential consequence. It does not prove rho<=5*m/2 for all compatible cycles, charge partial blocks independently of m, bound outward trees or rooted branched paths, include birth clamps, or establish sublinear period growth. Those remain separate obligations before any prize conclusion.
