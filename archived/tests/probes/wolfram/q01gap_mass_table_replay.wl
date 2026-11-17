(* L1675 (Local, 16 November 2026): Wolfram replay of the Q01Gap mass table by its own code.
   Python builds each prefix with integer anti-diagonals and a prefix-xor trick; here the anti-diagonals are explicit
   lists and the new one is a FoldList along the diagonal.  The acceptor is simulated literally with BitXor/BitOr. *)

fStep[y_] := BitXor[BitShiftRight[y, 1], BitOr[y, BitShiftLeft[y, 1]]];
kids[0] = {{0, 1}}; kids[1] = {{0, 2}}; kids[2] = {{1, 0}, {0, 3}}; kids[3] = {{0, 4}}; kids[4] = {{1, 0}};

(* dn = {z(0,n), ..., z(n-1,1)}, dn1 = {z(0,n-1), ..., z(n-2,1)}, c = depth-1 value at tick n.
   z(t, n+1-t) = z(t+1, n-t) xor (z(t, n-t) or z(t, n-1-t)), from z(n, 1) = c downwards in t. *)
nextDiag[dn_, dn1_, c_] := Reverse[FoldList[BitXor, c, Reverse[BitOr[dn, PadRight[dn1, Length[dn]]]]]];

survLen[y0_, limit_] := Module[{y = y0, age = 0, t = 0, b, g, ok = True},
   While[ok && t < limit,
    b = BitAnd[y, 1];
    Which[
     t == 0, If[b == 1, ok = False],
     OddQ[t], If[b == 0, ok = False],
     True, g = 1 - b;
      Which[age == 2, age = If[g == 1, 0, 3],
       age == 4, If[g == 0, ok = False, age = 0],
       True, If[g == 1, ok = False, age++]]];
    If[ok, y = fStep[y]; t++]];
   t];

massDFS[m_, kmax_] := Module[{stack, cOdd, cEven, mOdd, mEven, arg, s, age, dn, dn1, row, pop, e1, r1, base, g, age2,
    e2, r2, pOdd, e3, chk, pEven, nodes = 0, val},
   cOdd = ConstantArray[0, kmax + 1]; cEven = ConstantArray[0, kmax + 1];
   mOdd = ConstantArray[Infinity, kmax + 1]; mEven = ConstantArray[Infinity, kmax + 1];
   arg = ConstantArray[{}, kmax + 1];
   stack = {{0, 0, nextDiag[{}, {}, 0], {}, {0}, 0}};
   While[stack =!= {},
    {s, age, dn, dn1, row, pop} = Last[stack]; stack = Most[stack];
    e1 = nextDiag[dn, dn1, 1]; r1 = First[e1]; base = pop + r1;
    Do[
     {g, age2} = kid; nodes++;
     e2 = nextDiag[e1, dn, 1 - g]; r2 = First[e2]; pOdd = base + r2;
     If[pOdd <= m,
      cOdd[[s + 1]]++; mOdd[[s + 1]] = Min[mOdd[[s + 1]], pOdd];
      e3 = nextDiag[e2, e1, 1]; chk = First[e3]; pEven = pOdd + chk;
      If[pEven <= m,
       cEven[[s + 1]]++;
       val = FromDigits[Reverse[Join[row, {r1, r2, chk}]], 2];
       Which[pEven < mEven[[s + 1]], mEven[[s + 1]] = pEven; arg[[s + 1]] = {val},
        pEven == mEven[[s + 1]], AppendTo[arg[[s + 1]], val]];
       If[s + 1 < kmax, AppendTo[stack, {s + 1, age2, e2, e1, Join[row, {r1, r2}], pOdd}]]]],
     {kid, kids[age]}]];
   <|"cOdd" -> cOdd, "cEven" -> cEven, "mOdd" -> mOdd, "mEven" -> mEven, "arg" -> arg, "nodes" -> nodes|>];

horizonOf[res_, kmax_] := Module[{h = None},
   Do[If[h === None, If[res["cOdd"][[s]] == 0, h = 2 s + 1, If[res["cEven"][[s]] == 0, h = 2 s + 2]]], {s, 1, kmax}]; h];

c37 = {42813888358306443700074217814, 148978366434744761789452353878, 2654468869608816557330812141910,
   20290708049760378067263390038, 871680261646910262683015020886, 3258683745119620012336052404566,
   793529923180978236193646670102, 343533199256979670105602359638};

r38 = massDFS[38, 70]; r37 = massDFS[37, 70];
Print["M = 37: first horizon ", horizonOf[r37, 70], "; M = 38: first horizon ", horizonOf[r38, 70],
  "; mu(102) = ", r38["mEven"][[50]], "; survivors of popcount <= 38 at H = 102: ", r38["cEven"][[50]],
  "; equal to c37Roots: ", Sort[r38["arg"][[50]]] === Sort[c37]];
Print["survival of the eight as finite seeds: ", survLen[#, 400] & /@ c37];
r50 = massDFS[50, 90];
Print["M = 50: first horizon ", horizonOf[r50, 90], "; nodes ", r50["nodes"], "; mu(H) at H = 20, 40, ..., 140: ",
  Table[r50["mEven"][[h/2 - 1]], {h, 20, 140, 20}]];
r60 = massDFS[60, 110];
Print["M = 60: first horizon ", horizonOf[r60, 110], "; nodes ", r60["nodes"], "; mu(160), mu(180): ",
  {r60["mEven"][[79]], r60["mEven"][[89]]}, "; largest box ", Max[Max[r60["cOdd"]], Max[r60["cEven"]]]];
