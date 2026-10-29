(* GC2110: structural checks for the six arc notebook outputs; no build on loading.
   Loading this file performs no build or LeanLink call. Only the illustration and axiom boxes are parsed,
   with HoldComplete applied BEFORE evaluation. The KernelCheck object is read from InterpretationBox;
   output cells containing LeanEnvironment/TypeForm are retained for the separate manual read, never evaluated.
   This is an artifact gate, not a replacement for the unchanged Lean checker. *)

arcNotebookHeads = "Rule30Submission.ArcRule30Exclusion." <> # & /@
 {"no_visible_rotation", "no_eventual_visible_rotation", "no_visible_endpoint_variant", "no_visible_interval_union"};
arcNotebookStandardAxioms = {"Classical.choice", "Quot.sound", "propext"};
arcNotebookExpectedGrid = {{"supplied endpoint labels r", "digit threshold K"},
 {0,2},{1,4},{2,8},{3,16},{4,32},{5,64},{6,128}};

arcNotebookHeld[BoxData[b_]] := Quiet[Check[ToExpression[b, StandardForm, HoldComplete], $Failed]];
arcNotebookHeld[_] := $Failed;

arcNotebookAxiomsOK[h_] := Module[{pairs, a},
  If[!MatchQ[h, HoldComplete[Association[Repeated[Rule[_String, {___String}]]]]], Return[False]];
  (* Unwrap only after the literal string/list grammar matched; do not rely on Association's value-only
     traversal conventions to enumerate its rules. Duplicate keys remain visible in this raw rule list. *)
  pairs = h /. HoldComplete[Association[r___]] :> (List @@@ {r});
  If[Length[pairs] =!= Length[arcNotebookHeads] || Sort[First /@ pairs] =!= Sort[arcNotebookHeads], Return[False]];
  If[!AllTrue[pairs, Complement[Last[#], arcNotebookStandardAxioms] === {} &], Return[False]];
  a = Association[Rule @@@ pairs];
  AllTrue[arcNotebookHeads, Sort[a[#]] === Sort[arcNotebookStandardAxioms] &]
];

arcNotebookKernelData[out_] := Module[{objects, a, m},
  objects = Cases[out,
    HoldPattern[InterpretationBox[_, s : Success["KernelChecked", _Association], ___]] :> HoldComplete[s], Infinity];
  If[Length[objects] =!= 1, Return[$Failed]];
  a = First[objects] /. HoldComplete[Success["KernelChecked", v_Association]] :> v;
  m = Lookup[a, "Module", None];
  (* The exact single-file unchanged-checker receipt replays169 declarations. A difference in the notebook
     is a retained discrepancy for review, never an automatic rebuild or permission to weaken this gate. *)
  If[!StringQ[m] || !StringStartsQ[m, "LeanLinkTmp"] || StringLength[m] <= StringLength["LeanLinkTmp"] ||
      Lookup[a, "Declarations", None] =!= 169 || Lookup[a, "MessageParameters", None] =!= {169, m} ||
      Lookup[a, "MessageTemplate", None] =!= "The kernel accepts all `1` declarations of `2`.", Return[$Failed]];
  a
];

arcNotebookOutputChecks[outs_List] := Module[{gridOK = False, axiomsOK = False, kernel = $Failed},
  If[Length[outs] === 6,
    gridOK = MatchQ[arcNotebookHeld[outs[[1]]], With[{e = arcNotebookExpectedGrid}, HoldComplete[Grid[e, ___]]]];
    axiomsOK = TrueQ[arcNotebookAxiomsOK[arcNotebookHeld[outs[[5]]]]];
    kernel = arcNotebookKernelData[outs[[6]]];
  ];
  <|"grid_ok" -> TrueQ[gridOK], "axioms_ok" -> TrueQ[axiomsOK], "kernelcheck_ok" -> AssociationQ[kernel],
    "kernelcheck_data" -> If[AssociationQ[kernel], kernel, Null]|>
];
