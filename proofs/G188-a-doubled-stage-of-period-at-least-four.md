# a doubled stage of period at least four cannot return to zero within eleven steps

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT188. a doubled stage of
period at least four cannot return to zero within eleven steps (second-read by Local, 2026-10-07)"; rebuild with
`python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this
file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

After a period doubles, the next completely white profile cannot appear within eleven steps.

**What it says.** Once the repeat period is at least four, the two complementary temporal halves created by doubling rule out these short returns. The proof checks the seventh and eighth positions directly, then rules out the ninth through eleventh through small tables of necessary temporal transitions. An allowed cycle at the eleventh has odd period and cannot follow a doubling.

**Why it matters.** This is an actual local compatibility restriction, but its fixed length does not grow with the period. It supplies no long-term growth estimate.

**An everyday picture.** A machine must pass several checkpoints before it can reset again. Knowing the first few checkpoints does not tell us how long the entire journey takes.

## The formal statement and proof

### GPT G188 — A doubled stage of period at least four cannot return to zero within eight steps (2026-10-07)

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


**G188 continuation: return11 has an odd-period cycle, so cannot follow doubling (GPT, 2026-10-07; second reader pending, hand algebra only).** Retain E(x,y,z)=x+y+z*(1+x)*(1+y), and define H(x,y,z)=(x+y) OR (y+z), equal to0 exactly at000 and111. Four profiles before a repeated pair were eliminated in the previous continuation. One further backward step gives

    F(x,y,z,v)=y+v+H(x,y,z).

For a putative return0,c,1,e,f,g,h,i,j,k,l,0, the last equal pair k=l=w therefore forces j=Delta w, i=w*Delta w, h=Delta^2 w, g=E(w), f=F(w), and e=S E(w)+(F(w) OR E(w)). Its remaining f equation simplifies to

    S F(w) = 1 + (F(w) OR Delta E(w)).

For consecutive w bits x,y,z,v,u, it determines the next bit uniquely:

    u = z + H(y,z,v) + 1
        + [F(x,y,z,v) OR (E(x,y,z)+E(y,z,v))].

The resulting four-bit-state successors, in increasing binary order0000 through1111, are

    0001,0011,0100,0111,1000,1011,1100,1111,
    0000,0010,0100,0111,1001,1011,1100,1110.

Every state feeds the SINGLE cycle

    0000 -> 0001 -> 0011 -> 0111 -> 1111 -> 1110
         -> 1100 -> 1001 -> 0010 -> 0100 -> 1000 -> 0000.

Hence a periodic w satisfying the equation has least period11. The reconstructed preceding profiles are all11-periodic. In particular c cannot have the even least period created by odd integration: its period divides11. For a rooted dyadic stage, there is also the direct check that w cannot be both11-periodic with least period11 and q-periodic for a power of two q. No earlier zero occurs through position10 by the preceding exclusions, so reset uniqueness indeed keeps all these profiles within the entry period until this putative return. Thus position11 is excluded. Combined with G188's earlier parts, the first subsequent zero and the stage length after doubling to q>=4 are at least12. This is still a constant bound.

**Independent cycle-word control and identified unexpected ambient return.** Reading the cycle gives the cyclic temporal word w=00001111001. Its four-bit windows reproduce exactly the eleven cycle states above. It has five black cells and, since11 is prime and the word is nonconstant, least period11. At window0000 the formula has E=F=S E=0, so e=0; at window0111 it has E=F=1 and S E=0, so e=1. Therefore c=1+S e is nonconstant and of least period11. Backward reconstruction consequently DOES produce a compatible ambient return at position11 with a nonzero entry; its pre-integration source Delta c has even block parity. This guards against claiming that the return equation has no compatible solutions. What fails is period-doubling ancestry, not compatibility. Neither this odd-period ambient return nor its gate/root reachability is asserted to belong to the rooted tree. The table and these controls are Boolean proof calculations, not a computed census or a requested Local run.

**Next obligation.** This continuation identifies an actual domain countercontrol while extending only a fixed local exclusion. The lower bound12/q still vanishes. No rule for arbitrary return lengths, period-dependent obstruction, recurrence of large normalized stages, or prize conclusion is established. Local: include the successor list, single cycle and odd-period scope check in G188's second read; no new job.

*Second reader's note on G188 (Local, 2026-10-07; chat L153).* Correct, with its continuation. Checked
(`rule30_audit_g99_g100.py`, S80) exhaustively at $q = 4, 8, 16$. After every odd doubling (every odd $q/2$-source, both
integration children, each with $Tc = 1 + c$), no profile at positions 1 to 11 is zero. Positions 9 and 10 need only a
nonzero $c$, as the continuation says. At every cap from 2 to 12, for every nonzero $c$ and every branch, position 2 is
$1$ and positions 9 and 10 are nonzero. GPT's $E$ table, the position-9 transitions (whose only cycle is
$010 \leftrightarrow 101$), the five position-10 edges (no cycle) and position 8's allowed triples were rebuilt by brute
force over bits. Both literal controls substitute correctly. The return-11 continuation is also correct (S81). The
successor rule reproduces GPT's sixteen entries, and every state feeds the one 11-cycle, whose word is $00001111001$.
Backward reconstruction from it gives a compatible return at position 11 at cap 11, nonzero throughout and with an
even-parity source, and the forward walk reproduces it. Among caps 2 to 13, a first zero at position 11 occurs only at
cap 11. The rooted $q = 16$ stage, followed forwards from the $q = 8$ cap exit $(161, 0)$, first returns to zero 52,808
steps later, at depth 53,207, with an even driver. That is G2.3's genuine split, replayed a third way. The constant is
far from sharp. An exploratory enumeration that was not preregistered (`rule30_g188_returns.py`) gives the earliest
first return after any odd doubling as 21 at $q = 4$, 88 at $q = 8$ and 6,343 at $q = 16$. In units of $q$ that is 5.25,
11 and about 396. Sixteen walks at $q = 16$ show no zero within 200,000 steps. These are descriptive numbers for three
periods, not a bound, and they cover the ambient domain, which contains every rooted history.
