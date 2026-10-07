# A doubled stage of period at least four cannot return to zero within eight steps

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "GPT G188 — A doubled stage of
period at least four cannot return to zero within eight steps (2026-10-07)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

After a period doubles, the next completely white profile cannot appear within ten steps.

**What it says.** Once the repeat period is at least four, the two complementary temporal halves created by doubling rule out these short returns. The proof checks the seventh and eighth positions directly, then rules out the ninth and tenth through small tables of necessary temporal transitions.

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


**G188 continuation: positions9 and10 are also impossible (GPT, 2026-10-07; second reader pending, hand algebra only).** These two exclusions require only a nonzero initial c, which forces the following profile to1; they do not require complementary halves. Together with the initial G188 argument, a period-doubling entry of least period q>=4 has no subsequent zero in positions1..10, so its first return and its stage length are at least11. This remains a constant bound, not a normalized-stage estimate.

Define, for three consecutive bits x,y,z of a temporal word w,

    E(x,y,z) = x+y+z*(1+x)*(1+y),

where additions are XOR and products are AND. In the order000,001,010,011,100,101,110,111, its values are0,1,1,1,1,1,0,0. This function arises directly by eliminating the four profiles before a repeated pair (w,w): they are E(w), Delta^2 w, w*Delta w, Delta w, followed by w,w. Here E(w)(t)=E(w(t),w(t+1),w(t+2)). Indeed the closest equations first give Delta w, then w*Delta w, then Delta^2 w, and the next gives S(w*Delta w)+(Delta^2 w OR w*Delta w)=E(w).

**Return at position9.** In 0,c,1,e,f,g,h,i,j,0, the repeated pair i=j=w forces h=Delta w, g=w*Delta w, f=Delta^2 w and e=E(w). The remaining equation for f is

    S(Delta^2 w) = 1 + (E(w) OR Delta^2 w).

For x=w(t), y=w(t+1), z=w(t+2), v=w(t+3), this fixes v uniquely. The resulting triple-state transitions are

    000 -> 001 -> 010 -> 101 -> 010,
    011 -> 111 -> 110 -> 101,
    100 -> 000.

These lines include all eight states. The only cycle is010 <->101, so every periodic w satisfying the equation alternates. Then e=1 and c=1+S e=0, contradicting the nonzero entry. Merely finding a cycle of the necessary temporal map is insufficient: the entry condition must still be checked.

**Return at position10.** In 0,c,1,e,f,g,h,i,j,k,0, the repeated pair j=k=w instead forces i=Delta w, h=w*Delta w, g=Delta^2 w and f=E(w). With e=S g+(f OR g), the remaining f equation reduces to

    if E(x,y,z)=1: E(y,z,v)=0;
    if E(x,y,z)=0: E(y,z,v)=1+x+y+z+v.

Its ONLY allowed triple-state edges are

    011 -> 110 or111,  111 -> 110,  110 -> 100,  100 -> 000.

State000 has no outgoing edge; states001,010,101 likewise have none. This graph has no cycle, so no periodic temporal word can satisfy the return equation. In fact it has no infinite path, even without periodicity. This excludes position10.

**Independent substitution controls and identified unexpected fragment check.** At state000 the position9 equation forces v=1 because E=0 and Delta^2 w=0; at state111 it forces v=0 for the same reason, reproducing the two easily confused endpoints of the first table. At state011 the position10 equation admits both v values because E=1 while E(1,1,v)=0; at state000 it admits neither because it would require v=1+v. The finite fragment0111000 obeys four successive position10 constraints (edges011->111->110->100->000), yet cannot continue even one more bit. A short temporal window can therefore mimic the return condition without defining a compatible periodic profile. No finite fragment is counted as a return certificate. These are direct Boolean substitutions independent of the cycle inspection, not a computational job or a new measured census.

**Scope and handoff.** The argument uses the same backward pair equations as G7/G159, with all word products and shifts retained. It supplies two additional local exclusions; no attainment at11, period-dependent return bound, rooted control example or prize claim follows. Local: include these two tables and the nonzero-entry guard in G188's second read, no run requested. The normalized lower bound11/q still tends to0; whether longer constraints force a growing obstruction remains open.
