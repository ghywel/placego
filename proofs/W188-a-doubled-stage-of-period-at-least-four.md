# A doubled stage of period at least four cannot return to zero within eight steps

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "GPT G188 — A doubled stage of
period at least four cannot return to zero within eight steps (2026-10-07)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

After a period doubles, the next completely white profile cannot appear within eight steps.

**What it says.** Once the repeat period is at least four, the two complementary temporal halves created by doubling rule out these short returns. The proof checks the seventh and eighth positions directly.

**Why it matters.** This is an actual local compatibility restriction, but its fixed length does not grow with the period. It supplies no long-term growth estimate.

**An everyday picture.** A machine must pass several checkpoints before it can reset again. Knowing the first few checkpoints does not tell us how long the entire journey takes.

## The formal statement and proof

**Local zero-return lemma, second reader pending; symbolic, no run.** Consider an odd zero-driver integration that doubles period from q/2 to q>=4. Write its following compatible temporal profiles as

    0, c, 1, e, f, g, h, i, ...,

with S w(t)=w(t+1), Delta=I+S over binary XOR, and T=S^(q/2). Integration gives T c=1+c. Then none of profiles at positions1 through8 after the displayed initial zero can be identically zero. Thus the first subsequent zero is at position at least9. On a rooted history, every stage entered by doubling to q>=4 has length at least9. This is a CONSTANT bound; it gives no positive lower bound on normalized stage length as q grows.

**The first six positions.** The reset equations force the next profile to1 and S e=1+c, equivalently e=1+S^(-1)c. G159's direct six-position calculation applies because the pre-integration source Delta c has least period q/2>=2 and is nonconstant. Its only earlier-zero exception would require that source to be constant1. Therefore c,1,e,f,g,h are nonzero. This uses the already reviewed local proof, not its even-branch hypothesis: nonconstancy excludes the same exception here.

**Position7 cannot be zero.** If i=0, compatibility forces g=h. The equations for g and h then give S g=f+g and e=f*g (pointwise product). Since e is contained in f, the f equation reduces to S f=1+f. Thus f alternates, g integrates that alternating word, and g is a rotation of0011 repeated. The word e=f*g has exactly one black cell per four positions. Therefore c=1+S e has least period4 and three black cells per four positions. But an entry word c of least period q with complementary q/2 halves has exactly q/2 black cells. Here q must be4 and the required weight is2, contradicting3.

**Position8 cannot be zero.** Suppose the profile after i is0; then h=i. The equations for h and i give g=Delta h, and comparison with the h equation gives f=g*h. Since f is contained in g, the g equation gives e=Delta g=Delta^2 h. Put x=h(t), y=h(t+1), z=h(t+2). The f equation reads

    y*(1+z) = 1 + [(x+z) OR x*(1+y)].

Its allowed triples are001,010,011,100,101. No periodic or bi-infinite word satisfying these constraints can contain11: both110 and111 are forbidden. Hence011 is also absent, and h has no adjacent ones and no three consecutive zeros. The shifted word T h has the same two properties.

Now beta=h+T h obeys Delta^2 beta=1, because e+T e=1 follows from c+T c=1. Thus beta(t+2)=1+beta(t): beta is a rotation of0011 repeated. Choose a phase with five successive beta bits11001. At the second position, h and T h differ; absence of adjacent ones forces their common bit at the third position to0. At the fifth position they also differ, forcing their common fourth-position bit to0. Absence of000 now forces BOTH second-position bits to1, a contradiction. This excludes position8.

**Independent literal control and identified unexpected exception.** The seven-step compatible zero return

    a=0110, 0, c=1101, 1=1111, e=0001,
    f=0101, g=0011, h=0011, 0

uses increasing temporal order on cap4. Direct substitution gives Delta c=0110, S e=0010=1+c, S f=1010=1+(e OR f), S g=S h=0110, and the last equal pair produces0. It has an EVEN pre-integration source and no complementary halves in c, so it does not refute the lemma. Rootedness of this control is not asserted. The q=2 exception is essential: the compatible prefix0,01,11,01,01,0 returns to zero in five steps after constant-one integration, as already recorded in G159. The new assertion keeps q>=4. These literal checks independently guard against extending the result to all zero-driver events or to the smallest doubling.

**Prior record and scope.** G157-G159 supply reset, integration and the six-position guard; G185 shows difference order can recover rapidly without ending a stage. The present short-return exclusion uses actual compatibility and complementary temporal halves, rather than an autonomous order or half-difference model. Neither rooted reachability of the control nor attainment at position9 is claimed. The bound9/q tends to0: this result does NOT establish the unbounded normalized lengths of G186/L151, or the budget-linked recurrent thresholds of G187. No literature novelty, computation or prize claim. Local: please second-read the two return equations, especially the five-position beta contradiction; no job requested. Next useful task is whether longer return constraints yield a period-dependent obstruction, rather than extrapolating this constant bound.
