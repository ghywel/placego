# the ternary sideways image is six forbidden words, with a local section

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT126. the ternary sideways
image is six forbidden words, with a local section (second-read by Local, 2026-10-06)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Six forbidden words completely describe the sideways rule's first ternary image.

**What it says.** A ternary sequence has a predecessor exactly when it avoids six short words. A local construction produces a predecessor for every allowed sequence.

**Why it matters.** The old forbidden words were only a necessary test. This supplies both necessity and sufficiency, including nonperiodic sequences, while showing that the image still contains many freely chosen patterns. It does not describe the deeper images or enforce a prize problem's wall.

**An everyday picture.** A short checklist now determines whether a whole sequence can pass through one stage, but later stages may impose more rules.

## The formal statement and proof

### G126. The ternary sideways map has an exact six-word image and a local predecessor section (2026-10-06)

**Status:** symbolic all-sequence image theorem using G22/G24; reviewed by Local L080. No experiment or production run. Coordinates are the bi-infinite time axis of the formal sideways map; no fixed wall or finite-seed condition is imposed.

Let H(a,b)=(S a XOR(a OR b),a) and let T be G22's induced ternary map on H's one-step image. Then T's image is exactly the set Y of bi-infinite ternary sequences avoiding

    100, 101, 112, 0210, 0211, 0202.

Thus the image is a shift of finite type, not merely a language with the two necessary exclusions of G24. There is a shift-commuting local map R from Y to the full ternary shift with T(R(z))=z. It uses only z(t-1),z(t),z(t+1). In particular every p-periodic target in Y has a p-periodic predecessor (its least period may divide p). This is not a claim that R(z) lies in Y or that T is onto its own image.

**Reduction to binary predecessor constraints.** Decode a target z as (D,C), where C(t)=[z(t)=2], and D(t)=z(t) when C(t)=0, otherwise D(t)=1-C(t+1). A ternary predecessor is represented by a compatible pair(C,A). Its image must satisfy

    D(t)=C(t+1) XOR(C(t) OR A(t)).

When C(t)=0 this forces A(t)=e(t)=D(t) XOR C(t+1). When C(t)=1 the target equation is automatic and A(t) is free. G22's image compatibility for(C,A) requires, at every site with A(t)=1,

    C(t)=1-A(t+1).

Hence a forced 1 at a zero site of C requires the next A bit to be 1; a chosen 1 at a one site of C requires the next A bit to be 0.

**Necessity of the six exclusions.** Two consecutive zero sites of C cannot have e(t)=1,e(t+1)=0. In target symbols this is exactly100 or101 when C(t+2)=0, and112 when C(t+2)=1. Also a zero-one-zero block of C with e(t)=1 forces A(t+1)=1 and then A(t+2)=0. Its first target symbol is0, its middle symbol2, and its final forced e(t+2) must be0. The three ways to violate this last condition are0210,0211,0202. Each exclusion therefore holds for arbitrary predecessors, periodic or not.

**Sufficiency and local section.** For any target avoiding these words, define

    A(t)=D(t) XOR C(t+1)                    if C(t)=0,
    A(t)=[z(t-1)=0]                       if C(t)=1.

All target equations hold. Check compatibility only where A(t)=1. If C(t)=0 and C(t+1)=0, the forbidden triples ensure the next forced bit is1. If C(t)=0 and C(t+1)=1, the equation e(t)=1 means z(t)=0, so the prescribed next bit is1. If C(t)=1, its chosen bit is1 only after target symbol0. When C(t+1)=1 the next chosen bit is0 because its preceding symbol is2. When C(t+1)=0, avoidance of the forbidden quadruples makes its forced bit0. These exhaust the cases and prove compatibility. Encode(C,A) as R(z)(t)=2 when A(t)=1, otherwise C(t). G22's recoding then gives T(R(z))=z. This construction is valid on the whole bi-infinite sequence; no boundary completion or compactness assumption is hidden in it.

**Independent hand certificate and unexpected gap check.** For the repeating target0220, the formulas give C=0110,D=0010,A=1100 and predecessor code2210. A further binary predecessor B=0011 satisfies, by direct XOR/OR evaluation,

    H(1100,0011)=(0110,1100),
    H(0110,1100)=(0010,0110).

The last pair codes0220, independently certifying a target in the second image. Conversely the repeating target112 avoids100 and101, but forces A(t)=1,A(t+1)=0 at two successive zero sites of C. It has no predecessor under T. This refutes the counterfactual that G24's two old exclusions already describe the image exactly. These are finite algebra checks supporting the case proof, not a computational extrapolation.

**The image still has positive shift entropy.** Arbitrary aligned concatenations of blocks00 and22 belong to Y:there are no ones, and every constant run has length at least two, so0202 cannot occur. Distinct binary choices of n blocks give 2^n distinct words of length2n. The word-count entropy of Y is therefore at least1/2 bit per time-axis site. No exact entropy or limit-set entropy is evaluated. A local predecessor section does not imply its repeated application remains inside Y; deeper images remain unclassified.

**Record and scope.** This advances CONSTELLATION row 5's exact image description using the existing sideways recurrence and G22's compatibility theorem. G24's periodic missing-target conclusion remains correct and is strengthened by a complete image test. No claim of external novelty; the construction is a project-local symbolic derivation. An eventual0101 wall or finite forced left row would need additional constraints. The positive entropy lower bound prevents mistaking this finite image refinement for a collapse to a finite collection of traces or a prize proof.

*Second reader's note on G126 (Local, 2026-10-06; chat L080).* Correct, including the sufficiency case GPT asked me to
challenge: a chosen 1 at a $C = 1$ site follows a target 0, and the next bit is 0 either because its own preceding
symbol is 2 (when $C(t+1) = 1$) or because the forbidden quadruples force it (when $C(t+1) = 0$). Checked
(`rule30_audit_g99_g100.py`, S25) with $T$ rebuilt from G22's definitions: no predecessor window of length $k + 2$
maps onto any of the six forbidden words (a local test, no periodicity); for every period $p \le 8$ the periodic
targets with a $p$-periodic predecessor are exactly the periodic words avoiding the six; the local section satisfies
$T(R(z)) = z$ on all of them; $2210 \mapsto 0220$, and 112 has no predecessor. (My first run failed at $p = 2$ through
my own short unrolling, which missed 0202 inside 2020; G126 was right.)
