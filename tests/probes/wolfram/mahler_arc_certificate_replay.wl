(* mahler_arc_certificate_replay.wl -- Local, 12 November 2026 (L1668).
   Wolfram replay of tests/probes/mahler/local_arc_certificate.py, by different routes:
   validity by direct rational tail sums (no slack rule), starts by walking every n < 2^k
   (no incremental lift), arc counts over every rotation by cumulative sums (no sorting).
   Exact integers and rationals only.  Nothing above 2^14 is walked. *)

tStep[n_] := Quotient[3 n + 1, 2];
wordOf[n_, k_] := Mod[NestList[tStep, n, k - 1], 2];
validQ[w_List] := Module[{u = 0},
   Catch[Do[u = (b + 2 u)/3; If[u >= 1/2, Throw[False]], {b, Reverse[w]}]; True]];
digitsOfOne = Module[{c = 1, ds = {}, dd},
   Do[dd = Floor[3 c/2]; AppendTo[ds, dd]; c = 3 c/2 - dd, {420}]; ds];
nState = 40;

(* boundary continuations of length k after the prefix state i: starts n < 2^k *)
boundaryFam[i_, k_] := Select[Range[0, 2^k - 1], Function[n,
    With[{s = Join[digitsOfOne[[;; i]], wordOf[n, k]]}, validQ[s] && ! validQ[Append[s, 1]]]]];
validFam[i_, k_] := Select[Range[0, 2^k - 1], Function[n,
    validQ[Join[digitsOfOne[[;; i]], wordOf[n, k]]]]];
deathPoint[n_, k_] := If[OddQ[Nest[tStep, n, k]], n, n + 2^k];

(* min and max over every rotation a of the number of points in [a, a + 2^k) of Z/2^K *)
arcMinMax[{}, K_, k_] := {0, 0};
arcMinMax[pts_List, K_, k_] := Module[{m = 2^K, h = 2^k, ind, cs, cnt},
   ind = ConstantArray[0, 2 m];
   ind[[Join[pts + 1, pts + 1 + m]]] = 1;
   cs = Prepend[Accumulate[ind], 0];
   cnt = cs[[h + 1 ;; h + m]] - cs[[1 ;; m]];
   {Min[cnt], Max[cnt]}];
multipliers[K_] := Table[PowerMod[3, -l, 2^K], {l, 0, 2^(K - 2) - 1}];

(* (a): residues modulo 3 on the boundary continuations of a full word *)
aRow[k_] := Module[{s = boundaryFam[0, k], m = 2^k, worstGaps = Infinity, worstGood = Infinity, p, g, best},
   Do[
    p = Sort[Mod[th s, m]];
    g = If[Length[p] > 1, Mod[RotateLeft[p] - p, m] /. 0 -> m, {m}];
    worstGaps = Min[worstGaps, Count[g, x_ /; Mod[x, 3] != 0]];
    best = Max[Table[Max[Values[Counts[Mod[Mod[p - a, m], 3]]]], {a, 0, m - 1}]];
    worstGood = Min[worstGood, Length[p] - best],
    {th, multipliers[k]}];
   {Length[s], worstGaps, worstGood}];

(* (b): first check, every prefix state *)
bRow[k_] := Module[{ths = multipliers[k + 1], m = 2^(k + 1), fams, pts, tab, num, l0, h0},
   fams = Table[boundaryFam[i, k], {i, 0, nState - 1}];
   pts = Map[Function[f, deathPoint[#, k] & /@ f], fams];
   tab = Table[arcMinMax[Mod[th pts[[i]], m], k + 1, k], {i, nState}, {th, ths}];
   num = Min[Table[Sum[(2/3)^(i - 1) tab[[i, q, 1]], {i, nState}], {q, Length[ths]}]];
   l0 = Min[tab[[1, All, 1]]]; h0 = Max[tab[[1, All, 2]]];
   {Length[fams[[1]]], l0, h0, num/(3/2)^(k + 1)}];

(* (c): j forced bits *)
cRow[j_, k_] := Module[{kk = k + j, ths, m, vs, xs, tab, killed, kept},
   ths = multipliers[kk]; m = 2^kk;
   vs = Table[Length[validFam[i, k]], {i, 0, nState - 1}];
   xs = Table[validFam[i, kk], {i, 0, nState - 1}];
   tab = Table[arcMinMax[Mod[th xs[[i]], m], kk, k], {i, nState}, {th, ths}];
   killed = Min[Table[Sum[(2/3)^(i - 1) (vs[[i]] - tab[[i, q, 2]]), {i, nState}], {q, Length[ths]}]];
   kept = Min[Table[Sum[(2/3)^(i - 1) tab[[i, q, 1]], {i, nState}], {q, Length[ths]}]];
   {kept/(3 (3/2)^k), 1 - killed/(3 (3/2)^k)}];

(* the census by walking every start *)
censusRow[mm_] := Module[{b = 0, d = 0, w},
   Do[w = wordOf[n, mm];
    If[validQ[w] && ! validQ[Append[w, 1]], b++; If[OddQ[Nest[tStep, n, mm]], d++]],
    {n, 0, 2^mm - 1}];
   {b, d}];

(* (E): the renewal counts and the explicit constant *)
renewal[nn_] := Module[{f = {1}, bb},
   Do[AppendTo[f, Sum[If[digitsOfOne[[j + 1]] == 1, f[[m - j]], 0], {j, 0, m - 1}]], {m, 1, nn}];
   bb = Table[Sum[If[digitsOfOne[[j + 1]] == 0, f[[m - j + 1]], 0], {j, 1, m}], {m, 0, nn}];
   {f, bb}];

replay[] := Module[{f, bb, fails},
   {f, bb} = renewal[400];
   fails = Select[Range[7, 400], 27 f[[# - 7 + 1]] < bb[[# + 1]] &];
   <|"a" -> Association[Table[k -> aRow[k], {k, 2, 8}]],
     "b" -> Association[Table[k -> bRow[k], {k, 4, 10}]],
     "c" -> <|{2, 6} -> cRow[2, 6], {3, 5} -> cRow[3, 5]|>,
     "census" -> Association[Table[mm -> censusRow[mm], {mm, {10, 14}}]],
     "E" -> fails, "F" -> f[[;; 23]], "B" -> bb[[;; 23]]|>];
