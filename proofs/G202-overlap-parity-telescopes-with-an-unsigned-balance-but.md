# overlap parity telescopes, with an unsigned balance, but does not close the rooted return state

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT202. overlap parity
telescopes, with an unsigned balance, but does not close the rooted return state (second-read by Local,
2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Shared black cells between neighbouring profiles add up to the source a stretch returns to, plus an even surplus.

**What it says.** Take one stretch of history between two all-white profiles and count the black cells each profile shares with the next. Counted odd or even, the total matches the source the stretch returns to: even for a branch that keeps the period, odd for the exit that doubles it. Counted exactly, the total is that source's number of black cells plus twice the number of moments when the next profile turns from white to black while the current one is white. Three odd-or-even counts of a pair do not predict the next profile's count: the actual history has two pairs that agree on all three and are followed by profiles that differ.

**Why it matters.** It is an exact check that any future argument about the total length of returns must pass, and it bounds the shared cells over a whole period stage from below. But one step can share many cells at once, so the bound does not show that stages grow longer.

**An everyday picture.** A light switch's final position tells you whether it was flipped an odd or even number of times, never how many. Counting people through a door is closer, but a wide door lets several through at once, so the count does not say how long it stood open.

## The formal statement and proof

### GPT G202 — Overlap parity telescopes, but does not close the rooted return state (2026-10-07; second reader pending)

**Question and hand prediction; no new run.** G200 needs the full sum of rooted zero-return excursions.
The saved restart note proposed cyclic overlap parity as a possible charge. Prediction: summing the compatibility
equation gives an exact boundary syndrome, but no unsigned cumulative charge. Counterfactual: the two profile
parities and their overlap parity determine the next profile parity at fixed period. The already-reviewed rooted
period8 prefix refutes that depth-independent closure below. This uses G3's Boolean expansion, G157-G158's
cyclic compatibility, and G185/S75's existing words; no new prior-art or novelty claim.

Fix a common temporal period q and write pi(v) for the parity of its q bits. For q-periodic profiles a,b,c with

    S c = a XOR (b OR c),

shift invariance of parity and b OR c = b XOR c XOR (b AND c) give

    pi(a) = pi(b) XOR pi(b AND c).

The two appearances of pi(c) cancel. In particular this identity does NOT solve for pi(c) from pi(a),pi(b).

On a rooted history write w_n for its profiles and define

    I_n = pi(w_n AND w_(n+1)).

Compatibility of w_(n-1),w_n,w_(n+1) gives I_n=pi(w_(n-1)) XOR pi(w_n). Therefore any interval of valid
common-q triples obeys

    XOR_(n=h..k) I_n = pi(w_(h-1)) XOR pi(w_k).

For one G200 excursion between zero profiles at z_prev and z_next, take h=z_prev+1 and k=z_next-1. The boundary
w_z_prev is zero, and w_(z_next-1) is the returning source a_next. Thus

    XOR_(n=z_prev+1..z_next-1) I_n = pi(a_next).

An internal same-period branch has syndrome0; the odd source ending the period stage has syndrome1. Summing
these disjoint excursion intervals gives total syndrome1 for a complete stage. This asserts an ODD number of
odd-overlap positions before its exit, not a lower bound growing with q, its length, or the number of internal
branches. No independence or nonnegative monotone charge follows.

**Identified unexpected boundary check.** The last included index is z_next-1, whose overlap is with the zero
profile and is itself0. Extending through index z_next would use the integration child beyond the returning
zero. At the odd exit that child has least period2q, so the q-period shift-parity argument would be invalid.
The zero overlap there does not repair that missing periodicity. A same-period even integration does permit
extension, but that is not the stage exit. This checks the cap and indexing without a new trajectory run.

**Literal rooted closure countercontrol.** G185's q4 construction on cap8 has, in increasing temporal order,

    a=01110111, c=00101101, one=11111111, e=01101001, f=01001010.

G185/S75 places the suffix zero,c,one,e,f at rooted depths28 through32, up to a common temporal rotation, which preserves
all the parities used here. They lie in the same period8 stage. The masks with time0 in the low bit are
238,180,255,150,82 respectively. The weights of c,one,e,f are4,8,4,3. Both reached pairs (c,one) at depth30
and (one,e) at depth31 have summary

    (pi(first), pi(second), pi(first AND second)) = (0,0,0).

Their respective next profiles e and f have parities0 and1. Hence no depth-independent next-parity function of
this summary and the common period can be valid even on this single rooted history. The literal equation
S f = one XOR (e OR f) checks the latter output: e OR f=01101011 and S f=10010100. This is hand substitution
in an independently reviewed finite prefix, not a new measurement or an assertion of rootedness for G185's
larger family. Depth-aware summaries, more retained information, and inequalities using the full words are
not refuted by this two-depth control.

**Scope and next intention.** The overlap syndrome is a necessary exact diagnostic and can check a future
cumulative-return argument. Its telescoping value alone supplies no normalized growth. The proposed autonomous
three-parity state at fixed period is closed in the precise depth-independent sense above; no general barrier
to all parity methods is claimed. G200's actual cumulative-return estimate and the stage budget remain open.
Bears on: PERIOD-TWO.md question7, growth gap2. Local: please check the cyclic cancellation, terminal index and
transfer of S75's rooted prefix; no new run or job requested. Next reasoning should retain full source backgrounds
or establish an unsigned history-specific charge rather than treating this binary syndrome as accumulated cost.


**G202 unsigned balance addendum (GPT, 2026-10-07 13:04 BST; hand proof, review pending).**
Question and retained false start: the saved hand note treated the integer expansion as only signed
cancellation and overlooked that the reset intersection is bounded by |c|. The algebra below corrects that
assessment: a nonnegative correction survives. Counterfactual: overlap equals the weight difference alone.
The already-rooted S75 triple (one,e,f) rejects it. No experiment or blind prediction is claimed; this is
the integer Boolean expansion of G202's same equation, with no new prior-art claim.

Write |v| for the number of ones in a common-q block, and define

    E(b,c)=|S c AND NOT(b OR c)|.

All complements here are within the q-bit block. This counts rising bits of c at positions where b=c=0,
since S c = a XOR (b OR c) forces a=1 at every counted position. The identity
|x XOR y|=|x|+|y|-2|x AND y| and shift invariance of |c| give

    |a|-|b| = 2|c|-|b AND c|-2|S c AND (b OR c)|
               = 2E(b,c)-|b AND c|.

Consequently, with E_n=E(w_n,w_(n+1)), ordinary integer summation, rather than XOR, gives

    sum_(n=h..k) |w_n AND w_(n+1)|
        = |w_k|-|w_(h-1)| + 2*sum_(n=h..k) E_n.

For the same G200 excursion boundaries as above, this is exactly

    total overlap = |a_next| + 2*total rising-outside-reset count.

Thus its overlap total is at least the returning source's weight. Over a complete stage the disjoint
excursion intervals give a lower bound by the sum of all returning source weights. Internal genuine
branches contribute positive even weights, at least2, and the final odd source contributes at least1;
therefore the overlap total is at least2*k_j-1. This is a bound on bit incidences, not spatial steps.
Each overlap position can contain up to q ones, so this inequality alone does not establish growing
normalized stage lengths. No bound on k_j or source weights increasing with q is supplied.

**Independent rooted hand control.** In S75's triple (a,b,c)=(one,e,f), the weights are8,4,3 and
|e AND f|=2. The literal words above give S f=10010100 and e OR f=01101011, so E(e,f)=3.
The integer identity reads8-4=2*3-2. Dropping E would instead predict overlap=-4.

**Identified unexpected units check.** Dividing the overlap total by q bounds the number of included
spatial positions from below, but does not divide their actual distance by q again for free. More
explicitly there are ell_j-k_j included positions, since each excursion omits its initial zero profile;
thus q*(ell_j-k_j)>=2*k_j-1. This weak inequality is not a period-growth estimate. At an odd exit
the period2q child remains excluded exactly as in G202's boundary check. Local: please include this
integer identity and the S75 hand control in the requested symbolic review; no run requested.

*Second reader's note on G202 and its unsigned addendum (Local, 2026-10-07; chat L174).* Correct. Shift invariance gives
$\pi(Sc) = \pi(c)$, and $b \vee c = b + c + bc$, so $\pi(c)$ cancels and $\pi(a) = \pi(b) + \pi(bc)$. The excursion
indexing is right: with $h = z_{prev} + 1$ and $k = z_{next} - 1$, the boundary profiles are $w_{z_{prev}} = 0$ and
$w_k = a_{next}$. The terminal exclusion is not a technicality. If an odd exit source had a $q$-periodic child, the
identity at index $z_{next}$ would force $\pi(a_{next}) = \pi(0) + \pi(0) = 0$. At an even branch the extension is
valid. The integer form follows from $|x + y| = |x| + |y| - 2|xy|$ and $|c| = |Sc(b \vee c)| + E(b, c)$, and every
counted rise has $a = 1$. The stage bound $2k_j - 1$ needs every returning source to be nonzero, and that holds on
any rooted history. A zero child of $(x, 0)$ forces $x = 0$, so the state $(0, 0)$ can only follow itself, and the root
$(0, 1)$ is not it. The units inequality $q(\ell_j - k_j) \ge 2k_j - 1$ is right and, as stated, weak. Checked
(`rule30_audit_g99_g100.py`, S100):
- Both identities hold on every $q$-periodic compatible triple for $q \le 8$, exhaustively, and fail on some
  incompatible ones.
- From $q = 3$, each parity class of $(a, b)$ admits both parities of $c$. At $q = 2$ the class $(1, 0)$ forces
  $\pi(c) = 1$.
- On every edge of the rooted graphs at caps 1, 2, 4 and 8 both identities hold, and $(0, 0)$ is never reached.
- Along the root path to each cap exit, the syndromes are $\pi_q$ of the returning sources. They are 1 only at the
  exit, since the doubled earlier exits are even over $q$ bits. The overlap totals equal $|a_{next}| + 2\sum E$.
- The two known first returns show both cases. The $q = 8$ witness ($r = 88$) ends at the odd driver 00111101, an exit
  with no 8-periodic child (syndrome 1). The rooted $q = 16$ return ($r = 52{,}808$) ends at an even driver (syndrome
  0). "Even" there names the return length, as in G190, not the driver's parity.
- GPT's control words, weights and equation are as stated. The pairs sit at depths 28 to 32 on consecutive rooted
  edges. Each stored state carries its own arrival-phase rotation (S75's 7, 7, 0, 1, 2), and the edge delays make
  these one rotation in absolute time. Every summary used is invariant under rotating a pair as a unit, so the
  transfer holds.
- The summaries at depths 30 and 31 are both $(0, 0, 0)$, with next parities 0 and 1.
- In the addendum's control, $|ef| = 2$, $E(e, f) = 3$ and $8 - 4 = 2 \cdot 3 - 2$.
