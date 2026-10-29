(* GC2091: structural checks for the six universal-start notebook outputs.
   Loading this file performs no build or LeanLink call. Only the illustration and axiom boxes are parsed,
   with HoldComplete applied BEFORE evaluation. The KernelCheck object is read from InterpretationBox;
   output cells containing LeanEnvironment/TypeForm are retained for the separate manual read, never evaluated.
   This is an artifact gate, not a replacement for the unchanged Lean checker. *)

usNotebookHeads = {"universal_start", "universal_start_finite", "universal_start_profiles", "cert", "run_double", "rightDiag_step"};
usNotebookStandardAxioms = {"Classical.choice", "Quot.sound", "propext"};
usNotebookExpectedGrid = {
  {"seed bits s0 s1 ...", "m", "periods of D1..Dm", "periods of D(m+1)..D(m+7)"},
  {"1", 2, {2, 2}, {4, 8, 8, 16, 32, 32, 64}},
  {"10010010001", 2, {2, 2}, {4, 8, 8, 16, 32, 32, 64}},
  {"10101000011", 6, {2, 2, 2, 2, 2, 2}, {4, 8, 8, 16, 32, 32, 32}},
  {"10011101011", 2, {2, 2}, {4, 8, 8, 16, 32, 32, 32}},
  {"10010111100", 2, {2, 2}, {4, 8, 8, 16, 32, 32, 32}},
  {"11010011100", 5, {2, 2, 2, 2, 2}, {4, 8, 8, 16, 32, 32, 32}},
  {"11011001101", 4, {2, 2, 2, 2}, {4, 8, 8, 16, 32, 32, 32}}};

usNotebookHeld[BoxData[b_]] := Quiet[Check[ToExpression[b, StandardForm, HoldComplete], $Failed]];
usNotebookHeld[_] := $Failed;

usNotebookAxiomsOK[h_] := Module[{pairs, a},
  If[!MatchQ[h, HoldComplete[Association[Repeated[Rule[_String, {___String}]]]]], Return[False]];
  (* Unwrap only after the literal string/list grammar matched; do not rely on Association's value-only
     traversal conventions to enumerate its rules. Duplicate keys remain visible in this raw rule list. *)
  pairs = h /. HoldComplete[Association[r___]] :> (List @@@ {r});
  If[Length[pairs] =!= Length[usNotebookHeads] || Sort[First /@ pairs] =!= Sort[usNotebookHeads], Return[False]];
  If[!AllTrue[pairs, Complement[Last[#], usNotebookStandardAxioms] === {} &], Return[False]];
  a = Association[Rule @@@ pairs];
  Sort[a["cert"]] === {"propext"} &&
    AllTrue[Take[usNotebookHeads, 3], Sort[a[#]] === Sort[usNotebookStandardAxioms] &]
];

usNotebookKernelData[out_] := Module[{objects, a, m},
  objects = Cases[out,
    HoldPattern[InterpretationBox[_, s : Success["KernelChecked", _Association], ___]] :> HoldComplete[s], Infinity];
  If[Length[objects] =!= 1, Return[$Failed]];
  a = First[objects] /. HoldComplete[Success["KernelChecked", v_Association]] :> v;
  m = Lookup[a, "Module", None];
  (* Both exact final-file unchanged-checker receipts replay 258 declarations. A difference in the notebook
     is a retained discrepancy for review, never an automatic rebuild or permission to weaken this gate. *)
  If[!StringQ[m] || !StringStartsQ[m, "LeanLinkTmp"] || StringLength[m] <= StringLength["LeanLinkTmp"] ||
      Lookup[a, "Declarations", None] =!= 258 || Lookup[a, "MessageParameters", None] =!= {258, m} ||
      Lookup[a, "MessageTemplate", None] =!= "The kernel accepts all `1` declarations of `2`.", Return[$Failed]];
  a
];

usNotebookOutputChecks[outs_List] := Module[{gridOK = False, axiomsOK = False, kernel = $Failed},
  If[Length[outs] === 6,
    gridOK = MatchQ[usNotebookHeld[outs[[1]]], With[{e = usNotebookExpectedGrid}, HoldComplete[Grid[e, ___]]]];
    axiomsOK = TrueQ[usNotebookAxiomsOK[usNotebookHeld[outs[[5]]]]];
    kernel = usNotebookKernelData[outs[[6]]];
  ];
  <|"grid_ok" -> TrueQ[gridOK], "axioms_ok" -> TrueQ[axiomsOK], "kernelcheck_ok" -> AssociationQ[kernel],
    "kernelcheck_data" -> If[AssociationQ[kernel], kernel, Null]|>
];
