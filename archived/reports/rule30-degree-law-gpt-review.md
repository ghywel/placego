# Independent review of L1072's degree law

GC2031, 28 October 2026. Owner requests verification, review and validation of Local's new proof.
Read the complete L1071/L1072 entries, the159-line proof, both numerical sources and the206-line grounding
report at650564e9. This review concerns the all-time degree theorem, not acceptance of every survey claim.

## Validation specification, frozen before execution

Record searched: degree law, multiplicative complexity, Schnorr and algebraic degree. Recovered GC486's
existing exact two-step polynomial, degrees at1/2/4 and fixed-seed scope warning. Read its original probe.
The new independent checker represents Boolean polynomials directly as sets of square-free monomials;
it does not use Local's NumPy truth-table/Mobius implementation or assignment-by-assignment pivot search.

Prediction: exact degree2t-1 and stated top monomials for t2..6; full rightmost-derivative identity for t1..6;
exact symbolic z-frame recursions and top coefficients for m1..6. Independent literal decimal-rule replay
checks all inputs for t1..4. Countercontrols: Rules90/150 stay degree1 through6; an incorrect t2 monomial
label must be rejected. Unexpected check: distinguish Boolean idempotent products from ordinary polynomial
products; the checker cancels duplicate mask unions. These are bounded controls of the proof, not its
all-time justification. Any failed assertion stops acceptance until explained; no automatic larger run.

One Intel process under run_capped.py:30 CPU/45 wall seconds;256MiB sampled group RSS;2MiB/file and8MiB
stage output; launch free+inactive1024MiB, ongoing512MiB, swap growth128MiB. No NumPy dependency, no Local
job duplicated, no t12 replay. Source: tests/probes/wolfram/degree_law_gpt_audit.py. Hand carrying review
continues independently of the numerical result. No novelty certification or formal compilation yet.

## Verdict — GC2032, 28 October 2026

**PROVED, second-read:** L1072's degree theorem and unique top monomial are accepted after reading the carrying
argument, with the clarifications below. This is a hand proof for all t, supported by finite checks; it is not
Lean/formally verified. The theorem concerns a varying-input local function, not the fixed singleton sequence.
Novelty remains unresolved. L1071's broader quantum and information claims are reviewed separately below.

### The carrying read

1. **Derivative.** A flip of y_t has only one light-speed route to cell0 at time t. Each step transmits it iff
   the cell immediately ahead is0. Once blocked, it cannot catch up. Those ahead cells cannot depend on y_t,
   so their white indicators multiply to the exact Boolean derivative. This establishes an identity of
   functions, not a typical-damage claim.
2. **Coefficient elimination.** Left permutivity excludes y_-t from every nonlinear monomial. For coefficients
   containing y_t, the white anti-diagonal has pivots p_k=t-1-2k. All available pivots solve uniquely in order.
   Removing a free cell leaves 2^(t-2) solutions. Removing a nonlast pivot leaves at least one free cell further
   left: earlier constraints cannot see it, and later pivots still solve uniquely. Hence the relevant counts
   are even for t>=3. For the candidate omitting y_t, h ignores y_(t-1), u has exact XOR dependence on
   y_(-t+1), and v ignores that cell and has exact XOR dependence on y_(-t+2). Thus wt(uv)=2^(2t-3), even for
   t>=2; the other three summands also have even weight. This exhausts the high-degree candidates.
3. **The remaining coefficient.** In S_m the earlier even pivots depend only on nearer free cells. The last
   pivot P=z_0(2m-2) equals Phi_(m-1): inserting P toggles the last required equality by exact XOR. The farthest
   free cell q=2m-1 affects no pivot. Along j+2k=q its flip is certain; immediately behind, damage satisfies
   beta_(k+1)=beta_k XOR 1 XOR z_k(q-1-2k). The ahead cell is P XOR W_k^(m-1), because P is its extreme
   permutive input and q is outside its cone. The other inputs coincide with the smaller system. This proves
   both displayed derivative recursions, including their constants, at arbitrary m. Taking the coefficient of
   all remaining free variables kills the constants for m>=2. Joint induction from Phi_1=z_0(1) gives
   tau(W_k)=k XOR (k-1)=1 and tau(Phi_m)=(m-1) XOR (m-2)=1. The number of zeros of Phi has the same parity as
   its number of ones, since its domain has even size. Therefore the surviving top coefficient is1.

The induction supplies the all-time conclusion. Computing further widths is unnecessary for this acceptance.

### Small corrections and wording

- Step2's free-cell case at t2 deletes y_0, giving **y_-1*y_1*y_2**. The surviving last-pivot case gives
  y_0*y_1*y_2. The theorem statement already lists both correctly.
- The comparison of S_m with S_(m-1) means removing the last free cell/pivot and dropping the last constraint.
  Setting the last pivot to0 does not generally preserve that last constraint of S_m; its residual is Phi_(m-1).
- In every balance argument, “linear in a variable” means **that variable XOR a function independent of it**.
  Merely being degree1 in one variable, as xy is in x, would not imply balance.
- Degree increases by2 per step starting at t2; the increase from t1 to t2 is1. “Except the two leftmost” describes
  the unique top monomial, not all dependence: y_-t always enters by exact XOR. Algebraic degree is not the
  cryptographic nonlinearity (distance to the closest affine function), nor the exact number of AND gates.

### Independent validation and receipts

The frozen source at **9b0c93c831962b150179d6bb2362510f8f1c5a0f** passed once, with no retry or enlarged run.
Direct Boolean-polynomial multiplication produced degrees **2,3,5,7,9,11** and term counts
**4,10,30,122,346,1360** for t1..6. The top monomials and rightmost derivative identities agree; all20 symbolic
z-recursion identities,680 literal-rule controls, and Rule90/150 controls passed. This representation is
independent of Local's truth-table/Mobius computation. It is an implementation cross-check, not another worker's
independent carrying read; that read is the hand reasoning above.

Shared-store packet: `cited/gc2032-degree-law-review/manifest.json`, SHA256
`c1f8207c2ee3f3160aaf799a61f4632efad5a679467afed025791f9000bb4b02`.
The manifest covers source, result, stdout, launcher and time receipt; every upload digest was verified.
Source SHA256: `a2b62129edbc117109cf717c25357af36c9f2fc8c1a980011ca24d30295ef297`.
Intel process: exit0,0.08s user/0.01s system/0.10s elapsed; process maximum RSS15,138,816 bytes.
Supervisor elapsed1.05s; launch free+inactive5948MiB, swap184MiB. CPU/file limits were installed and launch
pressure checked. The run ended before the first sampling tick: the empty sample list and recorded zero maxima
are not measurements of zero memory use or evidence of sustained pressure monitoring. Final output2507 bytes
before the launcher receipt. These are process measurements, not system peaks.

### What follows, and what remains open

**Standard corollary, using prior art:** an XOR/AND circuit with binary AND gates for the variable-input f_t
needs at least2t-2 AND gates. Find and Boyar explicitly state the degree-minus-one bound, citing Schnorr, in
[Multiplicative Complexity of Vector Valued Boolean Functions, p13](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=919080).
The original Schnorr full proof was not read here; this is application of a cited standard bound, not a new
circuit lower-bound proof. The naive cone uses t² ANDs. Neither exact multiplicative complexity nor the
single-seed indexing cost follows. This is not a lower bound for arbitrary quantum gate sets.

**Hand consequence for L1071's proposed next test:** if “number of right cells affecting the length-T trace”
means essential variables, with the initial row allowed to vary, the answer is already exactly T. Every
right-hand input y_1,...,y_T occurs in the top monomial of f_T (T>=2; T1 is immediate). A variable occurring in
an ANF has a nonzero Boolean derivative: deleting it from monomials that contain it is injective, so these
terms cannot cancel. Each such cell can therefore change f_T for some assignment; no initial cell beyond T
can influence the trace through time T. Background-averaged influence, reads by an adaptive observer, and
flips that matter in one fixed world are different observables. Do not run an essential-variable census to
estimate a slope near0.19; first recover and match the literature's precise observable.

**Prior-art status:** the record already contains GC486's two-step polynomial and degrees at1/2/4.
[Mariot2024](https://arxiv.org/html/2405.02875v1), in its CA-generator discussion, identifies studying degree and
algebraic immunity as a research direction; it does not certify this exact formula as previously open.
[Deva's abstract](https://ssrn.com/abstract=5908722) claims linear algebraic-degree growth, alongside stronger
claims. This is the already-recorded inaccessible source in PRIOR-ART.md §8.116, not a newly discovered paper.
Full text remains unavailable in this review; neither its claims nor their equivalence to L1072 are accepted.
Internal correctness is settled by the proof; external novelty requires an exact-source comparison.

### Separate qualifications to L1071's grounding report

The degree result is accepted; these broader conclusions are not:

- An unstructured black-box search bound does not close all structured quantum approaches to Rule30.
  “No demonstrated advantage for the selected task” is supported; “quantum cannot help” and blanket statements
  about every classical quantum simulation are not. Dense complex128 amplitudes alone require16GiB at30qubits;
  32–34qubits is not a practical dense-state budget on a16GiB machine. Ancilla costs depend on the encoding and
  reversible storage scheme. A NOT/CNOT/Toffoli circuit can be interpreted classically with one binary AND per
  Toffoli, so the stated bound applies in that basis; it does not cover every quantum circuit.
- Left permutivity with fair independent initial bits gives a fair boundary trace conditional on the initial
  right-side data. It does **not** make that trace independent of the future right region it drives. For example,
  u=y_0 and v=x_1(1)=u XOR (y_1 OR y_2) obey Pr(v=u)=1/4 under fair independent inputs, whereas independence of
  these fair bits would give1/2. Conditional on y_1=y_2=0 they agree identically. Pairwise input/output correlation
  cancellation also does not remove higher-order joint relationships. Keep the time slice explicit.
- For a fixed output x_t(i), the exceptional initial bit in the pairwise argument is y_(i-t); equivalently,
  fixing initial bit0 puts the exceptional future site at i=t. These are different indexing conventions.

No quantum experiment, larger degree census, or portal submission is commissioned by this review. The useful
next steps are the survey corrections and prior-art comparison; formalising the now-reviewed induction is also
well scoped. Local still owes the GC2028 prior-art-chain read, as L1071/L1072 explicitly record.
