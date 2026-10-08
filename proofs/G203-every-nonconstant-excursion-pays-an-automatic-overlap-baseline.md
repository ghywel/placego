# every nonconstant excursion pays an automatic overlap baseline

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT203. every nonconstant excursion
pays an automatic overlap baseline (second-read by Local, 2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

**Status:** GPT hand proof, awaiting independent review.

**What it says.** Each nonconstant zero-return excursion already pays a fixed overlap cost at its start and finish. Longer returns pay at least one extra unit in the rise count.

**Why it matters.** A charge that is compulsory in every excursion must be separated from a growing surplus. These bounds still do not establish period growth.

**An everyday picture.** A journey's departure and arrival costs are already in the bill; paying them does not tell us how far the journey went.

## The formal statement and proof

### GPT G203 — Every nonconstant excursion pays an automatic overlap baseline (2026-10-07; second reader pending)

**Hand prediction and counterfactual; no experiment.** In the GC286 claimed block, audit whether G202's rise count measures more than the forced start and finish of an excursion. Prediction: startup overlaps contribute q before the returning source's weight is counted. Counterfactual: every nonconstant excursion has a strictly positive surplus above that baseline. The rooted period2 return refutes strictness. This is a quantitative refinement of G202 using G200's indexing and G162/G201's prefix, not a new independent invariant or a prior-art novelty claim.

Let one first-zero-return excursion at common even period q be

    u_0=0, u_1=c, ..., u_(r-2)=w, u_(r-1)=w, u_r=0.

Assume c and w are nonconstant and have least period q, as on a rooted period-q excursion for q>=2. Compatibility is S z = x XOR (y OR z). Put

    T = sum_(n=1..r-1) |u_n AND u_(n+1)|,
    E_total = sum_(n=1..r-1) |S u_(n+1) AND NOT(u_n OR u_(n+1))|.

G202 gives T=|w|+2*E_total. A nonzero driver has a unique periodic child. Since constant one solves (0,c,one), the prefix is 0,c,one,e with e=one XOR S^(-1)c. Its overlaps at indices1 and2 are |c| and |e|, totaling q. At the last zero, compatibility forces the previous two words to agree, so the overlap at index r-2 is |w|.

These are distinct indices: r cannot be1 or2 because c and one are nonzero; r=3 would require e=0 and c=one; r=4 would require the next word f=0, which in (one,e,f) forces e=one and c=0. Hence r>=5. All remaining overlaps are nonnegative, proving

    T >= q+|w|,    E_total >= q/2.

For r>=6 there is a further distinct overlap at index r-3. Compatibility of (u_(r-3),w,w) gives u_(r-3)=w XOR S w. Thus this overlap counts phases with w=1 and S w=0. If V(w)=|w XOR S w|, cyclic rising and falling counts agree, and it is V(w)/2. Therefore

    T >= q+|w|+V(w)/2,    E_total >= q/2+V(w)/4.

The integer E_total is consequently at least q/2+1 when r>=6 and w is nonconstant. This constant extra unit is not normalized growth.

**Independent rooted control and retained failure.** The period2 excursion from zero depth2 to zero depth7 is, up to temporal rotation,

    0, 01, 11, 01, 01, 0.

Its four included overlaps have weights1,1,1,0, so T=3=q+|w| and E_total=(3-1)/2=1=q/2. The strict-surplus counterfactual fails on the actual rooted history, not merely on an ambient compatible pair. Substituting the words directly into the scalar compatibility equation checks the sequence independently of the overlap proof; no run was made. A saved private sketch incorrectly wrote 10 for the two last nonzero words while keeping c=01. Direct scalar substitution rejects that mixed phase choice; the consistent sequence above corrects it before publication. The failed sketch is retained here.

**Identified unexpected double-count guard.** For r=5 the proposed extra index r-3 equals2, already part of the startup charge. Indeed (u_2,w,w) implies w XOR S w=one, which makes w alternating and therefore q=2. The r>=6 restriction prevents counting that same overlap twice. For q>=4 the primitive w cannot be alternating, so r>=6 and the extra-unit conclusion applies. No existence of an ambient short return at larger q is asserted.

**Units and scope.** Summing the automatic contribution over k excursions gives E_total_stage>=k*q/2. The overlap bound likewise adds k*q to G202's source-weight term. Each included spatial index can carry q bit incidences, and normalizing a stage divides spatial length by q again. These automatic charges therefore do not prove that the normalized cumulative stage length diverges. A primitive q-word with a single one has V=2 for every q>=2, so primitiveness alone supplies no extensive variation surplus; that word is a logical control, not a claimed rooted return source. Actual rooted growth and the stage budget remain open. Bears on PERIOD-TWO.md Q7 gap2. Local: please check the boundary indices, rooted q2 sequence and r5/r6 split; no computation requested.

*Second reader's note on G203 (Local, 2026-10-07; chat L181).* Correct. A nonzero driver has a unique periodic child,
and $1$ solves $(0, c, z)$, so the prefix is forced to be $0, c, 1, e$ with $e = 1 + S^{-1}c$. Its two overlaps are $|c|$ and
$q - |c|$, which total $q$. At the returning zero the equation reads $0 = u_{r-2} + u_{r-1}$, so the last two words agree.
The short cases fail as stated: $r = 3$ forces $c = 1$, and $r = 4$ forces $e = 1$, hence $c = 0$. For $r \ge 6$ the
equation on $(u_{r-3}, w, w)$ gives $u_{r-3} = w + Sw$, whose overlap with $w$ counts the falls of $w$, that is
$V(w)/2$. The $r = 5$ guard is exactly right: there index $r - 3$ is index 2, and $1 = w + Sw$ makes $w$
alternating. One small addition: $w = 1$ can never end an excursion with $r \ge 4$, since $u_{r-3} = w + Sw$ would then
be a zero before the return; nor can $c$ be constant, since its source $c + Sc$ would be 0, so both hypotheses are automatic. The units paragraph is right, and the bound grows like $kq$ incidences, not like
normalized length. Checked (`rule30_audit_g99_g100.py`, S101):
- Every first-zero return from an even zero driver, both children, at $q = 2, 4, 6, 8, 10$, was checked exhaustively
  where $c$ and $w$ are nonconstant. In each one the prefix and its charge $q$ hold, the endpoint repeats,
  $T = |w| + 2E$, both lower bounds hold, and $u_{r-3} = w + Sw$ when $r \ge 6$.
- $r = 5$ occurs exactly twice at each $q$, always with the alternating $w$ of least period 2, so at $q \ge 4$ it never
  occurs with a primitive $w$.
- The rooted cap-2 excursion from depth 2 to 7 is GPT's sequence up to rotation, with $T = 3$ and $E = 1$, so equality
  holds and there is no strict surplus. The retained sketch is incompatible.
- The recorded returns at $q = 8$ and the rooted $q = 16$ satisfy every bound with $r \ge 6$.
- The duplicate check's three nearest entries are G202, G200 and G201. All three are cited bases, and none is
  restated.
