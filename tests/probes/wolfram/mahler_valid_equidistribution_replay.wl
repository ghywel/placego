(* L1670 (Local, 12 November 2026): Wolfram replay of run 7 by other routes.
   Python decides validity by the automaton of the digits of 1 and gets the starts from the 2-adic formula.
   Here: validity and fullness from the tail sums themselves (exact rationals), starts by walking every n,
   sites from the definition, E_s(r) by counting words, the angles from the starts of the unit words. *)

tStep[n_] := Ceiling[3 n/2];
wordOf[n_, k_] := Mod[NestList[tStep, n, k - 1], 2];
tailsRev[q_] := Rest[FoldList[(#2/3 + 2 #1/3) &, 0, Reverse[q]]];
validQ[q_] := q === {} || Max[tailsRev[q]] < 1/2;
fullQ[q_] := q === {} || With[{tr = tailsRev[q]},
    Max[tr] < 1/2 && Min[MapIndexed[(1/2 - #1) (3/2)^First[#2] &, tr]] >= 1/2];
sitesOf[q_] := Select[Range[0, Length[q] - 3], fullQ[q[[;; #]]] && q[[# + 2]] == 0 && q[[# + 3]] == 0 &];

validStarts[w_] := validStarts[w] = Select[Range[0, 2^w - 1], validQ[wordOf[#, w]] &];

discRow[w_] := Module[{s = validStarts[w], n},
   n = Length[s];
   {w, n, N[Max[Table[k/n - (s[[k]] + 1)/2^w, {k, n}]], 6], N[Max[Table[s[[k]]/2^w - (k - 1)/n, {k, n}]], 6]}];

lifeOf[n_, kmax_] := Module[{q = wordOf[n, kmax], k = 0},
   While[k < kmax && validQ[q[[;; k + 1]]], k++]; k];

passRow[m_] := Module[{s = validStarts[m], lives, a},
   lives = lifeOf[#, m + 40] & /@ s;
   a = Length[s];
   {m, a, Table[N[Count[lives, x_ /; x >= m + j]/a, 4], {j, 1, 8}],
    Max[Rest[lives]], Pick[s, lives, Max[Rest[lives]]]}];

lam = Cos[Pi/5];
fullWords[t_] := fullWords[t] = Select[wordOf[#, t] & /@ validStarts[t], fullQ];
vRow[t_, u_] := Module[{fw = fullWords[t], v},
   v = Total[lam^Length[Intersection[sitesOf[#], u]] & /@ fw];
   {t, u, Length[fw], N[(v/Length[fw])^(1/Length[u]), 6]}];

digitsOfOne[n_] := Module[{c = 1, out = {}, d},
   Do[d = Boole[c > 2/3]; AppendTo[out, d]; c = 3 c/2 - d, {n}]; out];
dd = digitsOfOne[80];
fCount[0] = 1;
fCount[n_] := fCount[n] = Sum[If[dd[[j + 1]] == 1, fCount[n - 1 - j], 0], {j, 0, n - 1}];
eCount[s_, r_] := Count[Tuples[{0, 1}, r], u_ /; fullQ[Join[dd[[;; s]], u]]];
kSeries[r_] := N[Sum[eCount[s, r]/(fCount[s] lam^Ceiling[s/3] fCount[r - 3]), {s, 0, 59}], 7];

gammaRow[w_] := Module[{s = validStarts[w], n, g},
   n = Length[s];
   g = Table[Abs[Total[Exp[2. Pi I Mod[h s, 2^w]/2^w]]]/n, {h, 1, 63}];
   {w, Round[g[[{1, 2, 3, 9, 27}]], 0.00001], Round[Max[g], 0.00001], First[Ordering[g, -1]]}];

toggleRow[w_, c_] := Module[{s = validStarts[w], words, unit, rho, lin, st, viol = 0, least = Infinity, g, b, al},
   words = wordOf[#, w] & /@ s;
   unit = Association[Table[wordOf[n, w] -> n, {n, 0, 2^w - 1}]];
   rho = Table[unit[UnitVector[w, i + 1]], {i, 0, w - 1}];
   lin = And @@ MapThread[Mod[#1 . rho, 2^w] == #2 &, {words, s}];
   st = Select[sitesOf[#], Mod[#, 3] == c &] & /@ words;
   Do[
    al = Mod[h rho, 2^w]/2^w;
    g = Abs[Total[Exp[2. Pi I Mod[h s, 2^w]/2^w]]];
    b = Total[Table[Times @@ Abs[Cos[N[Pi al[[st[[k]] + 1]]]]], {k, Length[words]}]];
    If[g > b + 10^-9, viol++];
    If[g > 10^-9, least = Min[least, b/g]],
    {h, 1, 2^w - 1}];
   {w, c, lin, viol, least}];

Print["A(w), w = 8, 12, 16: ", Length[validStarts[#]] & /@ {8, 12, 16}];
Print["deviation rows {w, A, up, down}: ", discRow /@ {8, 12, 16}];
Print["pass shares {m, A, shares j = 1..8, longest life of n >= 1, where}: ", passRow[12]];
Print["F(12), F(16) by fullness of tail sums: ", Length[fullWords[12]], " ", Length[fullWords[16]],
  "; by the renewal: ", fCount[12], " ", fCount[16]];
Print["per-site factors {t, U, F(t), factor}: ", vRow[12, {2}], " ", vRow[16, {2, 11}]];
Print["K(r), r = 3..6 (s < 60): ", kSeries /@ {3, 4, 5, 6}];
Print["gamma rows {w, at h = 1, 2, 3, 9, 27, largest over h < 64, where}: ", gammaRow /@ {12, 16}];
Print["Lemma T {w, class, linear in the bits, violations, least bound/|G|}: ", toggleRow[10, 0], " ", toggleRow[10, 1], " ", toggleRow[10, 2]];

(* Added after the first replay: Lemmas N and F, with the angles taken from the starts of the unit words. *)
nsRow[w_] := Module[{unit, rho, okRel = True, okGrow = True, okFloor = True, okCount = True, beta, dist, small, ns, a, tab},
   unit = Association[Table[wordOf[n, w] -> n, {n, 0, 2^w - 1}]];
   rho = Table[unit[UnitVector[w, i + 1]], {i, 0, w - 1}];
   tab = Table[
     beta = Table[Mod[h rho[[w - u]], 2^w]/2^w, {u, 0, w - 1}];
     dist = Min[#, 1 - #] & /@ beta;
     small = (# < 1/5) & /@ dist;
     Do[
      If[Mod[2 beta[[u + 1]] - 3 beta[[u]], 1] != 0, okRel = False];
      If[small[[u]] && small[[u + 1]] && dist[[u + 1]] != 3/2 dist[[u]], okGrow = False],
      {u, 1, w - 1}];
     ns = Count[small, False];
     a = IntegerExponent[h, 2];
     If[! (ns > Log[2.71, (w - a)/0.85]), okFloor = False];
     {a, ns},
     {h, 1, 2^w - 1}];
   Do[If[Count[tab, {a0, n_} /; n <= l] > (2 w)^(l - 1), okCount = False], {a0, 0, w - 1}, {l, 1, w}];
   {w, okRel, okGrow, okFloor, okCount, Min[Cases[tab, {0, n_} :> n]]}];
Print["Lemmas N and F {w, relation, growth by 3/2, floor, count, least NS over odd h}: ", nsRow[10], " ", nsRow[12]];

(* Added with the report: Proposition M (the Fejer majorant) at w = m + j = 12 and 16, j = 1 .. 6. *)
majRow[w_] := Module[{s = validStarts[w], n, g, rows},
   n = Length[s];
   g = Table[Abs[Total[Exp[2. Pi I Mod[h s, 2^w]/2^w]]]/n, {h, 1, 63}];
   rows = Table[{Count[s, x_ /; x < 2^(w - j)], N[(Pi^2/4) n 2^-j (1 + 2 Total[g[[;; 2^j - 1]]])]}, {j, 1, 6}];
   {w, And @@ (#[[1]] <= #[[2]] & /@ rows), Round[Min[#[[2]]/#[[1]] & /@ rows], 0.001], rows[[All, 1]]}];
Print["Proposition M {w, holds for j = 1..6, least bound/count, counts}: ", majRow[12], " ", majRow[16]];
