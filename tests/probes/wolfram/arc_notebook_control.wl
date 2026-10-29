(* GC2110:18 non-building output-gate controls; callable before the one build in the SAME fresh kernel.
   Bait code is held and its side effect must stay0. No LeanLink/resource/build on loading this file. *)
arcNotebookControlResults[] := Module[{axes, kernel, bait, outs, axcell, kcell, replace, pass, results},
 arcFixtureSideEffect = 0;
 axes = AssociationMap[arcNotebookStandardAxioms &, arcNotebookHeads];
 kernel = <|"MessageTemplate" -> "The kernel accepts all `1` declarations of `2`.",
  "MessageParameters" -> {169, "LeanLinkTmp123x456"}, "Module" -> "LeanLinkTmp123x456", "Declarations" -> 169|>;
 axcell[a_] := BoxData[ToBoxes[a, StandardForm]];
 kcell[a_] := BoxData[InterpretationBox["Success", Success["KernelChecked", a]]];
 bait = BoxData[RowBox[{"arcFixtureSideEffect", "=", "1"}]];
 outs = {BoxData[ToBoxes[Grid[arcNotebookExpectedGrid], StandardForm]], BoxData["True"], bait, bait, axcell[axes], kcell[kernel]};
 replace[i_, c_] := ReplacePart[outs, i -> c];
 pass[o_, key_] := TrueQ[arcNotebookOutputChecks[o][key]];
 results = <|
  "positive_grid" -> pass[outs, "grid_ok"],
  "positive_axioms" -> pass[outs, "axioms_ok"],
  "positive_kernel" -> pass[outs, "kernelcheck_ok"],
  "missing_output" -> !pass[Most[outs], "kernelcheck_ok"],
  "wrong_grid_value" -> !pass[replace[1, BoxData[ToBoxes[Grid[ReplacePart[arcNotebookExpectedGrid, {8,2}->127]], StandardForm]]], "grid_ok"],
  "wrong_grid_head" -> !pass[replace[1,bait], "grid_ok"],
  "unknown_axiom" -> !pass[replace[5,axcell[Join[axes,<|First[arcNotebookHeads]->{"customAxiom"}|>]]], "axioms_ok"],
  "missing_axiom_key" -> !pass[replace[5,axcell[KeyDrop[axes,First[arcNotebookHeads]]]], "axioms_ok"],
  "extra_axiom_key" -> !pass[replace[5,axcell[Join[axes,<|"extra"->{}|>]]], "axioms_ok"],
  "duplicate_axiom_key" -> !arcNotebookAxiomsOK[With[
    {a=arcNotebookHeads[[1]], b=arcNotebookHeads[[2]], c=arcNotebookHeads[[3]], d=arcNotebookHeads[[4]], z=arcNotebookStandardAxioms},
    HoldComplete[Association[a->z,a->z,b->z,c->z,d->z]]]],
  "missing_standard_axiom" -> !pass[replace[5,axcell[Join[axes,<|First[arcNotebookHeads]->{"propext"}|>]]], "axioms_ok"],
  "axiom_code_is_held" -> !pass[replace[5,bait], "axioms_ok"],
  "failure_containing_Success" -> !pass[replace[6,BoxData[InterpretationBox["Success",Failure["Success",<||>]]]], "kernelcheck_ok"],
  "display_only_Success" -> !pass[replace[6,BoxData["Success"]], "kernelcheck_ok"],
  "wrong_success_tag" -> !pass[replace[6,BoxData[InterpretationBox["Success",Success["Other",kernel]]]], "kernelcheck_ok"],
  "wrong_declaration_count" -> !pass[replace[6,kcell[Join[kernel,<|"Declarations"->168|>]]], "kernelcheck_ok"],
  "inconsistent_module" -> !pass[replace[6,kcell[Join[kernel,<|"Module"->"LeanLinkTmp789x123"|>]]], "kernelcheck_ok"],
  "no_output_code_evaluated" -> (arcFixtureSideEffect === 0)
 |>;
 results
];
