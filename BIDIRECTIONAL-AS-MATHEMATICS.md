# bidirectional-interpolation.glsl, written as mathematics

This document restates [shaders/bidirectional-interpolation.glsl](shaders/bidirectional-interpolation.glsl), the
base shader the rest of the family derives from, as equations. It covers all 22 passes, in pass order, and then the
seven passes of the optional reading view. Each equation cites the source lines it comes from, so it can be checked
against the code. The constants are the ones the file ships with.

Transcribed on 2026-10-04 from the file at commit `87f43f3`. It was written by reading the code, not by running it, and
has not been checked numerically against the shader's output. The same day, writing it out exposed four wrong comments
in the shader, which were repaired ([REPAIRS.md](REPAIRS.md)). Later that day Local retired the dead contrast gates and
the edge-snap mechanism (L2 and L3), and this document was brought up to date. The line numbers here refer to the
file at commit `be6fd30`. GitHub renders the equations; a plain-text viewer shows the LaTeX
source.

## Contents

0. [What kind of mathematics this is](#0-what-kind-of-mathematics-this-is)
1. [Notation](#1-notation)
2. [The pipeline at a glance](#2-the-pipeline-at-a-glance)
3. [Luma pyramid](#3-luma-pyramid)
4. [Scene-cut statistic](#4-scene-cut-statistic)
5. [Coarse search at the sixteenth level](#5-coarse-search-at-the-sixteenth-level)
6. [Refinement at the eighth, quarter and half levels](#6-refinement-at-the-eighth-quarter-and-half-levels)
7. [Sub-pixel fit (present, switched off)](#7-sub-pixel-fit-present-switched-off)
8. [Vector median filter](#8-vector-median-filter)
9. [Motion-gated edge masks (retired)](#9-motion-gated-edge-masks-retired)
10. [The output frame](#10-the-output-frame)
11. [The reading view (off by default)](#11-the-reading-view-off-by-default)
12. [What writing it out shows](#12-what-writing-it-out-shows)
13. [How exact this is](#13-how-exact-this-is)

---

## 0. What kind of mathematics this is

A shader does arithmetic on short vectors, and some of that arithmetic is linear algebra. Writing this one out shows
where the linear algebra stops. Once a motion field is known, the output frame is a sparse matrix applied to the two
input frames (§10.2). The luma pyramid, the reading view's pooling and its derivative stencils are linear too. The
motion field itself is not linear. It comes from a search that compares candidate displacements and keeps the
cheapest, a median that picks one vector rather than averaging, and thresholds that switch whole branches on or off.
Those steps are optimisation and decision-making, so their equations are written with $\arg\min$, $\max$, absolute
values $\lvert\cdot\rvert$ and indicator functions $\mathbf 1[\cdot]$, not matrices. §12.1 sorts every stage into one
kind or the other.

---

## 1. Notation

**Inputs.** $A$ and $B$ are the two source frames (`HOOKED` and `NEXT`), RGBA images of $\mathbf N = (N_x, N_y)$
texels. $t \in [0,1]$ is `mix_t`, the output frame's position between them. `pair_changed` only decides whether a
cached result is reused (lines 22-43). The cached value is the same function of $(A, B)$ either way, so it does not
appear in the mathematics.

**Textures and sampling.** A texture $T$ of size $\mathbf N_T$ holds texels $T[\mathbf k]$ for integer
$\mathbf 0 \le \mathbf k < \mathbf N_T$. Shaders address it by a normalised position $\mathbf u \in \mathbb R^2$ and
get the bilinear sample, with indices clamped to the edge:

```math
T(\mathbf u) \;=\; \sum_{\mathbf k \in \mathbb Z^2} T\big[\operatorname{cl}_T(\mathbf k)\big]\;
\Lambda\!\big(N_{T,x}\,u_x - k_x - \tfrac12\big)\,\Lambda\!\big(N_{T,y}\,u_y - k_y - \tfrac12\big),
\qquad \Lambda(s) = \max\big(0,\ 1 - \lvert s \rvert\big)
```

Here $\operatorname{cl}_T$ clamps each index into $[0, N_T - 1]$. A sample is linear in the texel values. The texel
pitch is $\boldsymbol\eta_T = \mathbf 1 \oslash \mathbf N_T$, so an offset of $\boldsymbol\delta$ texels is
$\mathbf u + \boldsymbol\eta_T \odot \boldsymbol\delta$. Here $\odot$ and $\oslash$ multiply and divide component by
component. A pass computes one value at each of its own texel centres,

```math
\mathbf u_{\mathbf k} = \big(\mathbf k + \tfrac12\mathbf 1\big) \oslash \mathbf N_{\text{pass}},
```

and a texture sampled exactly at one of its own texel centres returns that texel: $T(\mathbf u_{\mathbf k}) = T[\mathbf k]$.

**Pyramid levels.** $\ell \in \lbrace S, E, Q, H\rbrace$ are the sixteenth-, eighth-, quarter- and half-resolution
levels. They have scale factors $s_\ell = 16, 8, 4, 2$, sizes $\mathbf N_\ell \approx \mathbf N / s_\ell$ (rounded by
libplacebo) and pitches $\boldsymbol\eta_\ell$. Full resolution has pitch $\boldsymbol\eta$. Each refinement level has
a parent $p(\ell)$: $p(E) = S$, $p(Q) = E$, $p(H) = Q$.

**Offset lists.** The searches visit offsets in a fixed row-major order, $y$ in the outer loop and $x$ in the inner
loop:

```math
\mathcal W_r = \big( (x, y) \;:\; y = -r, \dots, r;\ x = -r, \dots, r \big),
\qquad
\mathcal R_r = \mathcal W_r \setminus \lbrace (0,0) \rbrace .
```

**Other notation.** $\mathbf 1[P]$ is 1 when the statement $P$ holds and 0 otherwise.
$\operatorname{clamp}(x, a, b) = \min(\max(x, a), b)$, and

```math
\operatorname{sstep}_{e_0, e_1}(x) = \tau^2 (3 - 2\tau), \qquad \tau = \operatorname{clamp}\!\Big(\frac{x - e_0}{e_1 - e_0},\, 0,\, 1\Big)
```

is GLSL's `smoothstep`.

**The margin scan.** Every search and median in the file keeps a running best. A candidate replaces it only if the
candidate is cheaper by a relative margin $\varepsilon = 10^{-4}$ (`TIE_MARGIN`, explained at lines 266-311). The scan
starts from an incumbent $(\mathbf d_0, c_0)$, visits candidates $\mathbf d_1, \dots, \mathbf d_n$ in order and scores
each with a cost $J$:

```math
\big(\mathbf d^{(j)}, c^{(j)}\big) =
\begin{cases}
\big(\mathbf d_j,\ J(\mathbf d_j)\big) & \text{if } J(\mathbf d_j) < (1 - \varepsilon)\, c^{(j-1)},\\[4pt]
\big(\mathbf d^{(j-1)},\ c^{(j-1)}\big) & \text{otherwise,}
\end{cases}
\qquad \big(\mathbf d^{(0)}, c^{(0)}\big) = (\mathbf d_0, c_0),
```

```math
\operatorname{scan}^{J}_{\varepsilon}\big[(\mathbf d_0, c_0);\ \mathbf d_1, \dots, \mathbf d_n\big] = \big(\mathbf d^{(n)}, c^{(n)}\big).
```

This is not exactly an $\arg\min$, because the result depends on the visiting order. It is close to one, though. When
$J \ge 0$, the result is never worse than the incumbent ($c^{(n)} \le c_0$), and no candidate beats it by more than the
margin:

```math
(1 - \varepsilon)\, c^{(n)} \;\le\; \min_{1 \le j \le n} J(\mathbf d_j).
```

The proof: the running cost never increases. So a candidate with $J(\mathbf d_j) < (1-\varepsilon)c^{(n)}$ would also
have satisfied $J(\mathbf d_j) < (1-\varepsilon)c^{(j-1)}$ and been accepted, and then $c^{(n)} \le J(\mathbf d_j)$, a
contradiction.

**Constants.**

| Symbol | Value | Name in the source | Line |
|---|---|---|---|
| $\varepsilon$ | $10^{-4}$ | `TIE_MARGIN` | 311 (repeated in every search and median) |
| $\lambda_S$ | $0.06$ | `REG_LAMBDA` | 250 |
| $h_0$ | $0.75$ | `step_px` | 328 |
| $\kappa_S$ | $0.02$ | `MIN_CONTRAST`, coarse level | 232 |
| matching window radius | $1$ | `COARSE_WINDOW_RADIUS`, and the fixed $3 \times 3$ at H | 192, 523, 777, 991 |
| refinement search radius | $2$ | `REFINE_SEARCH_RADIUS` | 594, 820, 1033 |
| $\lambda_R$ | $0.05$ | `REFINE_REG_LAMBDA` | 613, 821, 1034 |
| $D_{\text{cut}}$ | $0.125$ | `SCENE_CUT_DIFF` | 1669 |
| sub-pixel fit | off | `SUBPEL_REFINE = 0` | 1098, 1306 |

---

## 2. The pipeline at a glance

Read the table top to bottom. Each pass reads only symbols defined in rows above it.

| Lines | Pass | Result | Section |
|---|---|---|---|
| 72-92, 450-470, 727-747, 935-955 | luma at $\tfrac1{16}$, $\tfrac18$, $\tfrac14$, $\tfrac12$ resolution | $Y^A_\ell$, $Y^B_\ell$ | §3 |
| 137-155 | scene-cut statistic | $D$ (one number) | §4 |
| 167-351, 358-442 | coarse search, both directions | $F^{AB}_S$, $F^{BA}_S$ | §5 |
| 477-725, 754-933, 962-1377 | refinement at E, Q, H, both directions | $F^{AB}_\ell$, $F^{BA}_\ell$ | §6, §7 |
| 1388-1563 | vector median, twice, both directions | $\bar F^{AB}_H$, $\bar F^{BA}_H$ | §8 |
| 1570-1687 | warp and blend | the output frame $O$ | §10 |
| 1689-2017 | reading view, only when `read_view` $> 0$ | $\mathbf v$, $\mathbf a_n$, $\nabla\mathbf v$, ... | §11 |

All flows $F$ are stored in texels of their own level and mean "where this point of the first frame is found in the
second". They are measured per source-frame interval.

---

## 3. Luma pyramid

*Lines 79-81 and 90-92 ($\tfrac1{16}$); 457-459 and 468-470 ($\tfrac18$); 734-736 and 745-747 ($\tfrac14$); 942-944 and 953-955 ($\tfrac12$).*

Full-resolution luma uses the BT.601 weights $\mathbf w = (0.299,\ 0.587,\ 0.114)^\top$:

```math
Y_A[\mathbf k] = \mathbf w^\top A_{\text{rgb}}[\mathbf k], \qquad Y_B[\mathbf k] = \mathbf w^\top B_{\text{rgb}}[\mathbf k].
```

Each level takes one bilinear sample of the full-resolution frame at its own texel centre. There is no wider prefilter.
Sampling and the dot product are both linear, so their order does not matter:

```math
Y^A_\ell[\mathbf k] = \mathbf w^\top A_{\text{rgb}}\big(\mathbf u^{\ell}_{\mathbf k}\big) = Y_A\big(\mathbf u^{\ell}_{\mathbf k}\big),
\qquad \mathbf u^{\ell}_{\mathbf k} = \big(\mathbf k + \tfrac12\mathbf 1\big) \oslash \mathbf N_\ell,
\qquad \ell \in \lbrace S, E, Q, H \rbrace,
```

and the same for $B$. When $s_\ell$ divides both frame dimensions, the sample falls exactly on a corner between four
full-resolution texels. It is then the mean of that $2 \times 2$ block:

```math
Y^A_\ell[\mathbf k] = \frac14 \sum_{\mathbf j \in \lbrace 0,1 \rbrace^2} Y_A\Big[\, s_\ell\,\mathbf k + \big(\tfrac{s_\ell}{2} - 1\big)\mathbf 1 + \mathbf j \,\Big].
```

Four texels out of $s_\ell^2$ contribute, so any detail finer than about $2 s_\ell$ pixels is aliased at level $\ell$
(the point-sampled pyramid of [NFRAME-LIMITS.md](NFRAME-LIMITS.md)).

---

## 4. Scene-cut statistic

*Lines 145-155.* The statistic is the mean absolute luma difference on a fixed $24 \times 24$ grid of sixteenth-resolution
samples:

```math
D = \frac{1}{576} \sum_{a=0}^{23} \sum_{b=0}^{23} \Big\lvert\, Y^A_S(\mathbf g_{ab}) - Y^B_S(\mathbf g_{ab}) \,\Big\rvert,
\qquad \mathbf g_{ab} = \Big( \frac{a + \frac12}{24},\ \frac{b + \frac12}{24} \Big).
```

It is used once, in §10: the frame pair counts as a cut when $D > D_{\text{cut}} = 0.125$.

---

## 5. Coarse search at the sixteenth level

*$A \to B$: lines 167-351. $B \to A$: lines 358-442.*

**Matching cost.** This is the sum of absolute differences (SAD) over a $3 \times 3$ window at level $\ell$, with the
displacement $\mathbf d$ in that level's texels (lines 194-203; despite the function name `sad5x5`, the window radius
is $1$):

```math
C^{AB}_\ell(\mathbf u, \mathbf d) = \sum_{\boldsymbol\delta \in \mathcal W_1}
\Big\lvert\, Y^A_\ell\big(\mathbf u + \boldsymbol\eta_\ell \odot \boldsymbol\delta\big)
- Y^B_\ell\big(\mathbf u + \boldsymbol\eta_\ell \odot (\mathbf d + \boldsymbol\delta)\big) \,\Big\rvert .
```

$C^{BA}_\ell$ is the same with $A$ and $B$ exchanged.

**Contrast gate.** This is the range of the reference block over a $(2r+1)^2$ window (lines 234-244). The $0$ and $1$ are
the loop's starting values, so for luma in $[0,1]$ this is simply $\max - \min$:

```math
\kappa^A_{\ell, r}(\mathbf u) = \max\!\Big(0,\ \max_{\boldsymbol\delta \in \mathcal W_r} Y^A_\ell(\mathbf u + \boldsymbol\eta_\ell \odot \boldsymbol\delta)\Big)
- \min\!\Big(1,\ \min_{\boldsymbol\delta \in \mathcal W_r} Y^A_\ell(\mathbf u + \boldsymbol\eta_\ell \odot \boldsymbol\delta)\Big).
```

**Regularised cost.** The penalty grows with the length of the whole displacement (line 337):

```math
J_S(\mathbf d) = C^{AB}_S(\mathbf u, \mathbf d) + \lambda_S \lVert \mathbf d \rVert_2 .
```

**Search.** A flat block gets zero motion (lines 259-263). Otherwise there are five rounds of an eight-neighbour step
search, and the step halves each round (lines 312-346):

```math
F^{AB}_S(\mathbf u) =
\begin{cases}
\mathbf 0 & \text{if } \kappa^A_{S,2}(\mathbf u) < \kappa_S,\\[4pt]
\mathbf d_5 & \text{otherwise,}
\end{cases}
```

```math
\begin{aligned}
(\mathbf d_0, c_0) &= \big(\mathbf 0,\ C^{AB}_S(\mathbf u, \mathbf 0)\big),\\
(\mathbf d_{i+1}, c_{i+1}) &= \operatorname{scan}^{J_S}_{\varepsilon}\Big[(\mathbf d_i, c_i);\ \big(\mathbf d_i + h_i\,\boldsymbol\delta\big)_{\boldsymbol\delta \in \mathcal R_1}\Big],
\qquad h_i = 0.75 \cdot 2^{-i}, \quad i = 0, \dots, 4 .
\end{aligned}
```

The penalty is zero at $\mathbf d = \mathbf 0$, so $c_i = J_S(\mathbf d_i)$ at every round. Every component of
$\mathbf d_5$ has the form $\tfrac{3}{64} m$ for an integer $|m| \le 31$, and all 63 values are reachable (§12.4). The
reach is therefore $\pm 1.453$ coarse texels per axis, which is $\pm 23.25$ full-resolution pixels when
$\mathbf N_S = \mathbf N / 16$.

$F^{BA}_S$ is the same with $A \leftrightarrow B$ throughout, including the gate, which tests $\kappa^B_{S,2}$.

---

## 6. Refinement at the eighth, quarter and half levels

*E: lines 477-636 and 643-725. Q: lines 754-844 and 851-933. H: lines 962-1169 and 1176-1377.*

**Seed.** The parent's flow is read at the parent texel that contains $\mathbf u$. `snap_texel` (lines 510-512) turns
the bilinear read into an exact texel read, which is nearest-neighbour upsampling. The read value is doubled into the
finer level's texels (lines 576, 815, 1028):

```math
\hat{\mathbf d}_\ell(\mathbf u) = 2\, F^{AB}_{p(\ell)}\Big[\big\lfloor \mathbf N_{p(\ell)} \odot \mathbf u \big\rfloor\Big].
```

**Search.** One pass over the $5 \times 5$ block of whole-texel offsets around the seed. The penalty is on the
distance from the seed (lines 615-632):

```math
J_\ell(\hat{\mathbf d}_\ell + \boldsymbol\delta) = C^{AB}_\ell\big(\mathbf u,\ \hat{\mathbf d}_\ell + \boldsymbol\delta\big) + \lambda_R \lVert \boldsymbol\delta \rVert_2,
```

```math
\Big( F^{AB}_\ell(\mathbf u),\ \cdot \Big) = \operatorname{scan}^{J_\ell}_{\varepsilon}\Big[ \big(\hat{\mathbf d}_\ell,\ C^{AB}_\ell(\mathbf u, \hat{\mathbf d}_\ell)\big);\ \big(\hat{\mathbf d}_\ell + \boldsymbol\delta\big)_{\boldsymbol\delta \in \mathcal R_2} \Big],
\qquad \ell \in \lbrace E, Q, H \rbrace .
```

The window is $3 \times 3$ at all three levels. Each level can move the seed by up to $\pm 2$ of its own texels:
$\pm 16$, $\pm 8$ and $\pm 4$ full-resolution pixels at E, Q and H.

**The gate retired here.** Until 2026-10-04 each refinement pass also kept a contrast test,
$\kappa^A_{\ell,r}(\mathbf u) < \kappa_\ell$, with $\kappa_\ell = 0$. Since

```math
\max(0, \max) \;\ge\; \max \;\ge\; \min \;\ge\; \min(1, \min) \quad\Longrightarrow\quad \kappa^A_{\ell, r}(\mathbf u) \ge 0,
```

the strict inequality could never be true, and the test was dead code. It was retired across the family, byte-identical
on the Arc ([REPAIRS.md](REPAIRS.md), lead L3). The search above always runs; only the coarse level keeps its gate.

$F^{BA}_\ell$ is the same with $A \leftrightarrow B$, seeded from $F^{BA}_{p(\ell)}$.

---

## 7. Sub-pixel fit (present, switched off)

*Lines 1126-1165 ($A \to B$) and 1334-1373 ($B \to A$).* The whole block sits behind the constant `SUBPEL_REFINE = 0`, so in this
file $F^{AB}_H$ is exactly the result of §6. It is written out here because the generated field shaders switch it on
(lines 1088-1097).

Let $\mathbf d^\ast = F^{AB}_H(\mathbf u)$ from §6, and let $\mathbf e_x = (1, 0)$, $\mathbf e_y = (0, 1)$. Take the
cost at the minimum and its four neighbours:

```math
c_0 = C^{AB}_H(\mathbf u, \mathbf d^\ast), \qquad c_{x\pm} = C^{AB}_H(\mathbf u, \mathbf d^\ast \pm \mathbf e_x), \qquad c_{y\pm} = C^{AB}_H(\mathbf u, \mathbf d^\ast \pm \mathbf e_y).
```

Per axis, the curvature term $\Delta_x$ depends on `SUBPEL_FIT`. The equiangular fit is the file's setting ($1$); the
parabola is the alternative ($0$):

```math
\Delta_x =
\begin{cases}
\max(c_{x-},\, c_{x+}) - c_0 & \text{equiangular,}\\[4pt]
c_{x-} - 2c_0 + c_{x+} & \text{parabola,}
\end{cases}
\qquad
\sigma_x =
\begin{cases}
\operatorname{clamp}\!\Big( \dfrac{c_{x-} - c_{x+}}{2\,\Delta_x},\ -\tfrac12,\ \tfrac12 \Big) & \text{if } \Delta_x > 10^{-6},\\[8pt]
0 & \text{otherwise,}
\end{cases}
```

and the same for $y$. The self-reference correction, also off (`SUBPEL_SELFREF = 0`), fits the reference block against
itself shifted by one texel. Write $C^{AA}_H$ for $C^{AB}_H$ with $B$ replaced by $A$, and
$s_{x\pm} = C^{AA}_H(\mathbf u, \pm \mathbf e_x)$. At zero shift this cost is $0$, which is why $c_0$ drops out:

```math
\Delta'_x =
\begin{cases}
\max(s_{x-},\, s_{x+}) & \text{equiangular,}\\[4pt]
s_{x-} + s_{x+} & \text{parabola,}
\end{cases}
\qquad
\beta_x =
\begin{cases}
\dfrac{s_{x-} - s_{x+}}{2\,\Delta'_x} & \text{if } \Delta'_x > 10^{-6},\\[8pt]
0 & \text{otherwise,}
\end{cases}
```

```math
F^{AB}_H(\mathbf u) \;\leftarrow\; \mathbf d^\ast + \operatorname{clamp}\big(\boldsymbol\sigma - \boldsymbol\beta,\ -\tfrac12,\ \tfrac12\big)
\quad \text{(or } \mathbf d^\ast + \boldsymbol\sigma \text{ without the correction).}
```

---

## 8. Vector median filter

*$A \to B$: lines 1395-1428 (pass 1) and 1446-1477 (pass 2). $B \to A$: lines 1486-1514 and 1532-1563.*

The filter takes the nine flow vectors of the $3 \times 3$ neighbourhood, in the order of $\mathcal W_1$, so
$\mathbf v_4$ is the centre:

```math
\mathbf v_j = F\big(\mathbf u + \boldsymbol\eta_H \odot \boldsymbol\delta_j\big), \qquad (\boldsymbol\delta_0, \dots, \boldsymbol\delta_8) = \mathcal W_1 ,
```

and scores each by its total Euclidean distance to the other eight:

```math
\Phi_i = \sum_{j=0}^{8} \lVert \mathbf v_i - \mathbf v_j \rVert_2 ,
\qquad
\Big( \mathcal V[F](\mathbf u),\ \cdot \Big) = \operatorname{scan}^{\Phi}_{\varepsilon}\big[ (\mathbf v_4,\ 10^{30});\ \mathbf v_0, \dots, \mathbf v_8 \big].
```

The incumbent's cost is $10^{30}$, so $\mathbf v_0$ is always accepted first and $\mathbf v_4$ is only a placeholder. The
result is one of the nine input vectors: the one whose total distance to the others is smallest, within the margin.
That is the vector median filter (Astola, Haavisto and Neuvo, 1990; [PRIOR-ART.md](PRIOR-ART.md)). It runs twice:

```math
\bar F^{AB}_H = \mathcal V\big[\, \mathcal V[F^{AB}_H] \,\big], \qquad \bar F^{BA}_H = \mathcal V\big[\, \mathcal V[F^{BA}_H] \,\big].
```

---

## 9. Motion-gated edge masks (retired)

Until 2026-10-04 the base computed two binary masks at full resolution, for a texel-snapping sampler in the warp. A
pixel was marked if its luma changed between the frames and it sat on a spatial edge in its own frame, with thresholds
$\theta_m = 0.08$ and $\theta_e = 0.1$:

```math
E_A[\mathbf k] = \mathbf 1\Big[\, \big\lvert Y_A[\mathbf k] - Y_B[\mathbf k] \big\rvert > \theta_m \Big]
\cdot \mathbf 1\Big[\, \max_{\boldsymbol\delta \in \mathcal R_1} \big\lvert Y_A[\mathbf k + \boldsymbol\delta] - Y_A[\mathbf k] \big\rvert > \theta_e \Big],
```

```math
E_B[\mathbf k] = \mathbf 1\Big[\, \big\lvert Y_A[\mathbf k] - Y_B[\mathbf k] \big\rvert > \theta_m \Big]
\cdot \mathbf 1\Big[\, \max_{\boldsymbol\delta \in \mathcal R_1} \big\lvert Y_B[\mathbf k + \boldsymbol\delta] - Y_B[\mathbf k] \big\rvert > \theta_e \Big].
```

They entered §10 only multiplied by the snap strength $\sigma = 0$, so they could not change the output. Measured at
$\sigma = 1$, the snap cost $-0.99$ dB on the ladder's mean. The mechanism was retired, both passes went from the
bases, and the generators were fixed to build without them ([REPAIRS.md](REPAIRS.md), lead L2: byte-identical on the
Arc, and the base renders $6.3\%$ faster from a file).

---

## 10. The output frame

*Lines 1570-1687.*

### 10.1 The equation

The displacement is read from the twice-filtered half-resolution flow by a bilinear sample at the output pixel. It is
converted to full-resolution pixels (a factor of $2$) and then to normalised units (line 1681):

```math
\mathbf f(\mathbf u) = 2\, \bar F^{AB}_H(\mathbf u) \quad \text{(full-resolution pixels)},
\qquad
\boldsymbol\Delta(\mathbf u) = \boldsymbol\eta \odot \mathbf f(\mathbf u) .
```

The output at each full-resolution texel centre $\mathbf u_{\mathbf k}$ is then (lines 1675-1686):

```math
O(\mathbf u_{\mathbf k}) =
\begin{cases}
A[\mathbf k] & \text{if } D > D_{\text{cut}} \text{ and } t < \tfrac12,\\[4pt]
B[\mathbf k] & \text{if } D > D_{\text{cut}} \text{ and } t \ge \tfrac12,\\[4pt]
(1 - t)\; A\big(\mathbf u_{\mathbf k} - t\, \boldsymbol\Delta(\mathbf u_{\mathbf k})\big)
\;+\; t\; B\big(\mathbf u_{\mathbf k} + (1 - t)\, \boldsymbol\Delta(\mathbf u_{\mathbf k})\big) & \text{otherwise,}
\end{cases}
```

where $A(\cdot)$ and $B(\cdot)$ are the plain bilinear samplers of §1, so away from a cut the output is:

```math
O(\mathbf u) = (1 - t)\; A\big(\mathbf u - t\, \boldsymbol\Delta(\mathbf u)\big) \;+\; t\; B\big(\mathbf u + (1 - t)\, \boldsymbol\Delta(\mathbf u)\big).
```

Until 2026-10-04 each sample went through an edge-confirmed snapping sampler, weighted by a snap strength
$\sigma = 0$, which reduced it to the plain sampler. It was retired with the masks of §9.

### 10.2 The same thing as matrices

Write each frame as a matrix with one row per pixel and one column per channel: $\mathbf a, \mathbf b \in \mathbb R^{P \times 4}$,
where $P = N_x N_y$. For a fixed displacement field and a fixed $t$, every bilinear read in 10.1 is a row of at most four
weights. Collect them into $\mathbf M_s \in \mathbb R^{P \times P}$, whose row $\mathbf k$ holds the weights of the
sample at $\mathbf u_{\mathbf k} + s\,\boldsymbol\Delta(\mathbf u_{\mathbf k})$:

```math
(\mathbf M_s)_{\mathbf k \mathbf j} = \Lambda\Big( N_x\big(u_{\mathbf k, x} + s\,\Delta_x(\mathbf u_{\mathbf k})\big) - j_x - \tfrac12 \Big)\;
\Lambda\Big( N_y\big(u_{\mathbf k, y} + s\,\Delta_y(\mathbf u_{\mathbf k})\big) - j_y - \tfrac12 \Big),
```

with the weights of out-of-range columns added to the nearest edge texel. Then:

```math
\mathbf o = (1 - t)\, \mathbf M_{-t}\, \mathbf a \;+\; t\, \mathbf M_{1-t}\, \mathbf b .
```

Every row of $\mathbf M_s$ has at most four non-zero entries, all non-negative and summing to $1$. The luma pyramid has
the same form, $\mathbf y^A_\ell = \mathbf P_\ell\, \mathbf a\, (0.299, 0.587, 0.114, 0)^\top$, with $\mathbf P_\ell$ the
sparse sampling matrix of §3. The nonlinear part of the shader is the map from images to displacements,

```math
\boldsymbol\Delta = \mathcal F\big(\mathbf y^A_S, \mathbf y^B_S, \dots, \mathbf y^A_H, \mathbf y^B_H\big),
```

which is §5, §6 and §8. $\mathbf M_s$ depends on $\boldsymbol\Delta$, so the shader as a whole is not linear in its
inputs. It is linear in the pixel values only once the motion has been decided.

---

## 11. The reading view (off by default)

*Lines 1689-2017, generated by `tests/add_human_reading.py`.* These passes run only when `read_view` $> 0$ (the default
is $0$). They work on cells at one eighth of the resolution, with pitch $\boldsymbol\eta_R$, at centres $\mathbf c$.
The two-frame shader has one flow, so every mode reads velocity. Any per-frame memory updates once per **output**
frame, indexed $n$.

**Velocity** (lines 1720-1724), in full-resolution pixels per source interval:

```math
\mathbf v(\mathbf c) = 2\, \bar F^{AB}_H(\mathbf c).
```

**Mode memory** (lines 1754-1780). Each cell keeps $K = 3$ candidates $(\boldsymbol\mu_k, w_k)$ and a miss counter $m$.
With $\mathbf r = \mathbf v(\mathbf c)$, one output frame does:

```math
\begin{aligned}
& w_k \leftarrow 0.97\, w_k, \qquad d_k = \lVert \boldsymbol\mu_k - \mathbf r \rVert_2, \\
& h = \operatorname*{arg\,min}_{k \,:\, w_k > 0,\ d_k < 1.5} d_k \quad \text{(if that set is empty there is no match)}, \\
& m \leftarrow \begin{cases} 0 & \text{match} \\ m + 1 & \text{no match} \end{cases},
\qquad \text{and if } m > 10^9:\ w_k \leftarrow 0.5\, w_k \ \text{for all } k, \\
& \text{match:} \quad \boldsymbol\mu_h \leftarrow 0.7\, \boldsymbol\mu_h + 0.3\, \mathbf r, \qquad w_h \leftarrow w_h + 1, \\
& \text{no match:} \quad (\boldsymbol\mu_q, w_q) \leftarrow (\mathbf r, 1), \qquad q = \operatorname*{arg\,min}_k\, w_k ,
\end{aligned}
```

and the pass outputs $(\boldsymbol\mu_b, w_b)$ with $b = \arg\max_k w_k$. Every $\arg\min$ and $\arg\max$ takes the
lowest index on a tie. The threshold $10^9$ means the faster decay never runs (line 1753).

**Pooled reading** (lines 1818-1839, `READ_MEMORY = 0`). This is a $13 \times 13$ box mean followed by an exponential
moving average:

```math
\bar{\mathbf v}_n(\mathbf c) = \frac{1}{169} \sum_{\boldsymbol\delta \in \mathcal W_6} \mathbf v_n\big(\mathbf c + \boldsymbol\eta_R \odot \boldsymbol\delta\big),
\qquad
\mathbf a_n(\mathbf c) = (1 - \alpha)\, \mathbf a_{n-1}(\mathbf c) + \alpha\, \bar{\mathbf v}_n(\mathbf c),
```

with $\alpha = 0.12$, or $\alpha = 1$ (no memory) when `read_view` $\in \lbrace 3, 6 \rbrace$. The alternative `READ_MEMORY = 1`, which
is off, replaces both with
$\mathbf a(\mathbf c) = \sum_{\mathcal W_1} w_b \boldsymbol\mu_b \big/ \max\big(\sum_{\mathcal W_1} w_b,\ 10^{-6}\big)$.

**Velocity gradient tensor** (lines 1853-1858). These are central differences across neighbouring cells. Cells are $8$ px
apart, so each difference spans $16$ px:

```math
\partial_x \mathbf v \approx \frac{\mathbf v(\mathbf c + \boldsymbol\eta_R \odot \mathbf e_x) - \mathbf v(\mathbf c - \boldsymbol\eta_R \odot \mathbf e_x)}{16},
\qquad
\partial_y \mathbf v \approx \frac{\mathbf v(\mathbf c + \boldsymbol\eta_R \odot \mathbf e_y) - \mathbf v(\mathbf c - \boldsymbol\eta_R \odot \mathbf e_y)}{16}.
```

The pass outputs the four standard invariants of the $2 \times 2$ gradient (units: $1$ per interval):

```math
\nabla \mathbf v = \begin{pmatrix} \partial_x v_x & \partial_y v_x \\ \partial_x v_y & \partial_y v_y \end{pmatrix},
\qquad
\begin{pmatrix} \operatorname{div} \\ \operatorname{curl} \\ \operatorname{shear}_1 \\ \operatorname{shear}_2 \end{pmatrix}
=
\begin{pmatrix}
\partial_x v_x + \partial_y v_y \\
\partial_x v_y - \partial_y v_x \\
\partial_x v_x - \partial_y v_y \\
\partial_y v_x + \partial_x v_y
\end{pmatrix}.
```

Together they rebuild the tensor exactly:

```math
\nabla \mathbf v = \tfrac12 \operatorname{div} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
+ \tfrac12 \operatorname{curl} \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}
+ \tfrac12 \operatorname{shear}_1 \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
+ \tfrac12 \operatorname{shear}_2 \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}.
```

Screen $y$ points down, so a positive curl is clockwise on screen.

**Frame maximum with memory** (lines 1869-1876 and 1903-1916). This is the largest pooled magnitude in the frame,
taken in two stages through $8 \times 8$ blocks of cells, which gives the same result as one global max:

```math
M_n = \max_{\mathbf c} \lVert \mathbf a_n(\mathbf c) \rVert_2 ,
\qquad
s_n = \max\!\left( \phi,\ \begin{cases} s_{n-1} + 0.3\, (M_n - s_{n-1}) & \text{if } M_n > s_{n-1}, \\[4pt] \max(M_n,\ 0.99\, s_{n-1}) & \text{otherwise,} \end{cases} \right)
```

with floor $\phi = 2.0$ when `read_view` $\in \lbrace 1, 4, 7, 8, 9 \rbrace$, $\phi = 0.9$ when it is $3$, and $\phi = 0.22$ when it
is $2$, $5$ or $6$.

**What is drawn** (lines 1961-2017). Let $P = O$ be the interpolated frame from §10.

*Machine modes* write the field as a colour around mid-grey, with full scale $\Gamma$:

| `read_view` | output RGBA |
|---|---|
| $4$, $5$, $6$ | $\big(\tfrac12 + \mathbf v / (2\Gamma),\ \tfrac12,\ 1\big)$, with $\Gamma = 32$ for mode $4$ and $\Gamma = 2$ for modes $5$ and $6$ |
| $7$ | $\big(\tfrac12 + \mathbf a_n / 64,\ \tfrac12,\ 1\big)$ |
| $8$ | $\big(\tfrac12 + \boldsymbol\mu_b / 64,\ \tfrac12,\ 1\big)$ |
| $9$ | $\big(\tfrac12 + \operatorname{div},\ \tfrac12 + \operatorname{curl},\ \tfrac12 + \operatorname{shear}_1,\ 1\big)$ |

*Painted modes* ($1$, $2$, $3$) use gates $(g_{\text{lo}}, g_{\text{hi}}, g_{\text{sat}}) = (1, 2, 3)$, $(0.12, 0.22, 0.30)$ and
$(0.5, 0.9, 1.4)$ respectively. At output position $\mathbf u$, first soften the pooled field with four diagonal taps
$2$ px away and take its magnitude:

```math
\tilde{\mathbf a}(\mathbf u) = \frac14 \sum_{\mathbf s \in \lbrace -2, 2 \rbrace^2} \mathbf a_n\big(\mathbf u + \boldsymbol\eta \odot \mathbf s\big),
\qquad \mu = \lVert \tilde{\mathbf a}(\mathbf u) \rVert_2 .
```

Opacity is a product of four factors: a gate on the pooled magnitude, a scale, a gate on the unpooled field nearby, and
a fade near the frame border:

```math
V = 0.9\; \operatorname{sstep}_{g_{\text{lo}}, g_{\text{hi}}}(\mu)\;\cdot\; \operatorname{clamp}\!\Big(\frac{\mu}{\Sigma},\, 0,\, 1\Big)\;\cdot\;
\operatorname{sstep}_{g_{\text{lo}}/2,\ g_{\text{lo}}}(\rho)\;\cdot\; \operatorname{sstep}_{4, 28}(\beta),
```

where

```math
\rho = \max_{\boldsymbol\delta \in \mathcal W_2} \big\lVert \mathbf v\big(\mathbf u + \boldsymbol\eta_R \odot \boldsymbol\delta\big) \big\rVert_2,
\qquad
\beta = \min\!\Big( \min(u_x, 1 - u_x)\, N_x,\ \min(u_y, 1 - u_y)\, N_y \Big),
```

and the scale is

```math
\Sigma =
\begin{cases}
\mathtt{read\_alpha} & \mathtt{read\_alpha} > 0,\ \text{mode 1},\\[2pt]
\mathtt{read\_alpha} / 10 & \mathtt{read\_alpha} > 0,\ \text{modes 2, 3},\\[2pt]
s_n & \mathtt{read\_alpha} = 0 .
\end{cases}
```

When `read_alpha` $< 0$ the scale factor is left out, which is the same as setting it to $1$. Hue comes from the direction
and saturation from the magnitude. The painting is laid over the picture at brightness $k_p$ = `read_plate`:

```math
\text{hue} = \operatorname{frac}\!\Big( \frac{\operatorname{atan2}(\tilde a_y, \tilde a_x)}{2\pi} + 1 \Big),
\qquad
\text{sat} = 0.95\, \operatorname{sstep}_{g_{\text{lo}}, g_{\text{sat}}}(\mu),
```

```math
\text{rgb} = (1 - V)\, k_p\, P_{\text{rgb}}(\mathbf u) + V\, \operatorname{hsv}(\text{hue}, \text{sat}, 1),
\qquad \text{alpha} = P_{\text{alpha}}(\mathbf u),
```

```math
\operatorname{hsv}(h, s, v)_i = v \Big[ (1 - s) + s\, \operatorname{clamp}\big( \lvert 6 \operatorname{frac}(h + k_i) - 3 \rvert - 1,\ 0,\ 1 \big) \Big],
\qquad (k_1, k_2, k_3) = \big(1, \tfrac23, \tfrac13\big).
```

---

## 12. What writing it out shows

### 12.1 Where the linear algebra is

| Stage | What the operation is | Linear in the pixel values? |
|---|---|---|
| Luma and pyramid (§3) | weighted sums: a sparse matrix | yes |
| Scene-cut statistic (§4) | mean of absolute differences | no |
| Coarse search and refinement (§5, §6) | discrete minimisation over candidate displacements | no |
| Contrast gate (§5) | $\max - \min$, then a threshold | no |
| Vector median (§8) | sums of Euclidean norms, then a selection | no |
| Cut gate (§10) | threshold that picks a branch | no |
| Warp and blend, for a given flow (§10) | a sparse, row-stochastic matrix | yes |
| Reading: pooling and derivatives (§11) | convolution stencils | yes |
| Reading: memories (§11) | conditional recurrences | no |
| Reading: painting (§11) | smoothstep, atan2, HSV | no |

### 12.2 Only the last pass depends on $t$

$t$ appears only in §10. Everything up to $\bar F^{AB}_H$ is a function of $A$ and $B$ alone. That is the condition the
file's flow cache needs: output frames that share a source pair share the flow (lines 22-30).

### 12.3 The source frames come out exactly

At $t = 0$, the equation of §10.1 gives $O(\mathbf u_{\mathbf k}) = A(\mathbf u_{\mathbf k}) = A[\mathbf k]$. At $t = 1$ it
gives $B[\mathbf k]$. This holds whatever the flow, and the cut branch agrees. A wrong flow can only show up strictly
between the two source frames, and its effect grows from zero at either end. The note at lines 1636-1641 makes the same
point in words.

### 12.4 The values the flow can take

From §5 and §6, before the median, the half-resolution flow is

```math
F^{AB}_H = 8\, F^{AB}_S + 4\, \boldsymbol\delta_E + 2\, \boldsymbol\delta_Q + \boldsymbol\delta_H,
\qquad F^{AB}_S = \tfrac{3}{64}\, \mathbf m, \quad \mathbf m \in \lbrace -31, \dots, 31 \rbrace^2, \quad \boldsymbol\delta_\ell \in \lbrace -2, \dots, 2 \rbrace^2,
```

where $\boldsymbol\delta_\ell$ is the offset each refinement level chose. Every value of $\mathbf m$ in that range is
reachable: a step in each round is $-1$, $0$ or $+1$ per axis, and these are signed binary digits of $16, 8, 4, 2, 1$.
In full-resolution pixels this is

```math
\mathbf f = 2\, F^{AB}_H = 0.75\, \mathbf m + 8\, \boldsymbol\delta_E + 4\, \boldsymbol\delta_Q + 2\, \boldsymbol\delta_H .
```

The median picks one of its inputs, so it keeps these values. They are the stored texel values. The warp reads them
bilinearly at full-resolution pixel centres, which sit a quarter of a half-resolution texel from the nearest centre, so
it weights neighbouring texels $\tfrac34$ and $\tfrac14$ per axis. Where neighbouring texels differ, the displacement
the warp uses lies between them. Four consequences follow for the stored values:

- **The flow lies on a quarter-pixel grid**, since $\gcd(0.75, 2) = 0.25$.
- **The coarse level alone sets the fraction.** Refinement only adds even numbers of pixels, so
  $\mathbf f \bmod 2\ \text{px}$ equals $0.75\,\mathbf m \bmod 2\ \text{px}$, which the coarse search fixed.
- **Some motions can be represented exactly only for certain coarse results.** A displacement of a whole even number
  of pixels needs $m \equiv 0 \pmod 8$ in that component, and a whole odd number needs $m \equiv 4 \pmod 8$. For
  example, at $16$ px per interval the coarse level on its own lands on $0.75 \cdot 21 = 15.75$ or
  $0.75 \cdot 22 = 16.5$. The total is exact only if the coarse search returns
  $m \in \lbrace 0, \pm 8, \pm 16, \pm 24 \rbrace$ and the refinements make up the rest.
- **Reach.** $\lvert f_x \rvert, \lvert f_y \rvert \le 23.25 + 16 + 8 + 4 = 51.25$ px, when the level sizes are exact
  divisions of the frame.

Until 2026-10-04 the note above the sub-pixel fit said the finest flow the estimator could express was one
half-resolution texel ($2$ px). That is true of the refinement steps but not of the total, because the coarse steps,
$h_i = 0.75 \cdot 2^{-i}$ coarse texels, are fractional. The note now says so (lines 1055-1065; [REPAIRS.md](REPAIRS.md)).
Whether the quarter-pixel fraction helps or hurts on real footage has not been measured.

### 12.5 What runs without changing the output

With the shipped constants, two parts of the file compute without affecting $O$:

- **The $B \to A$ chain.** $F^{BA}_S \to F^{BA}_E \to F^{BA}_Q \to F^{BA}_H \to \bar F^{BA}_H$ is computed and median-filtered,
  and no later pass in this file reads $\bar F^{BA}_H$. The generators (for example `tests/gen_tridirectional.py`)
  copy these passes into the shaders they build, where they are used. Until 2026-10-04 the file header described a
  forward/backward occlusion check fed by this chain. The note at lines 1607-1646 records that check's removal, and
  the header now does too (lines 13-20; [REPAIRS.md](REPAIRS.md)).
- **The sub-pixel fit** (§7). It sits behind a constant $0$.

Two more did until 2026-10-04: the refinement contrast gates, which could never fire (§6), and the edge masks, which
were read only through $\sigma = 0$ (§9). Both were retired by Local the same day ([REPAIRS.md](REPAIRS.md), L2 and
L3), byte-identical on the Arc. The $B \to A$ chain is lead L7, awaiting the owner's go.

What actually determines the output frame is therefore: §3, §4, the $A \to B$ half of §5 and §6, the $A \to B$ half
of §8, and §10. (In the reading view, `lum` at line 2011 is computed and never used.)

### 12.6 The approximation in the warp

Line 1678 defines the flow by $A(\mathbf x) \approx B(\mathbf x + \mathbf f(\mathbf x))$, a flow attached to positions in
$A$. A point that shows up at output position $\mathbf p$ at time $t$ started at the $\mathbf x_A$ that solves
$\mathbf x_A + t\, \mathbf f(\mathbf x_A) = \mathbf p$. The shader uses $\mathbf f(\mathbf p)$ in place of
$\mathbf f(\mathbf x_A)$. This is the usual backward-warping shortcut. It is exact where the flow is locally uniform.
Elsewhere, the sampling position on the $A$ side is off by

```math
\mathbf x_A - \big(\mathbf p - t\, \mathbf f(\mathbf p)\big) = t^2\, (\nabla \mathbf f)\, \mathbf f + O(t^3),
```

and by the same expression with $1 - t$ in place of $t$ on the $B$ side.

---

## 13. How exact this is

- **Arithmetic.** The equations are exact in real numbers. The GPU works in 32-bit floats, and the margin scan is
  there because the last bits of a float decide near-ties (lines 266-310).
- **Filtering.** Texture units compute bilinear weights at reduced precision (commonly $8$ fractional bits), so
  $\Lambda$ is an idealisation.
- **Assumptions about libplacebo.** Textures are taken to be sampled bilinearly with clamp-to-edge addressing,
  which is what the file's own comments assume (lines 1580-1585, 1590-1597). Intermediate textures are stored at
  whatever precision libplacebo allocates for them.
- **Level sizes.** Where a frame dimension is not a multiple of $16$, $\mathbf N_\ell$ is rounded. The factor $2$ in each
  seed (§6) and in the final flow (§10) is then not an exact change of scale between levels. The equations follow the
  code, which uses $2$.
- **Not modelled.** NaN and infinity are not treated.
