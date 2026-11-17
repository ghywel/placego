(* finite_past_notebook_checks_control.wl (Local, L1231): positive and adversarial fixtures for the finite-past output
   gate, adapted from gate_clocks_notebook_checks_control.wl (L1221). No MarkdownToNotebook, LeanLink, resource lookup,
   external process or certificate evaluation. These fixtures test the artifact logic, not the theorem or the notebook.
   Prediction: all 18 true and FINITE_PAST_OUTPUT_CONTROLS_PASS. Counterfactual: any false entry rejects the gate as it stands. *)
Get[FileNameJoin[{DirectoryName[$InputFileName], "finite_past_notebook_checks.wl"}]];
rfSideEffect = 0;
rfComputation = ReleaseHold[rnExpectedComputation];
rfAxioms = rnAxioms;
rfKernel = <|"MessageTemplate" -> "The kernel accepts all `1` declarations of `2`.",
  "MessageParameters" -> {196, "LeanLinkTmp123x456"}, "Module" -> "LeanLinkTmp123x456", "Declarations" -> 196|>;
rfBoxes[a_] := BoxData[ToBoxes[a, StandardForm]];
rfKCell[a_] := BoxData[InterpretationBox["Success", Success["KernelChecked", a]]];
rfBait = BoxData[RowBox[{"rfSideEffect", "=", "1"}]];
rfOutputs = {rfBait, rfBait, rfBoxes[rfComputation], BoxData["True"], rfBait, rfBait, rfBoxes[rfAxioms], rfKCell[rfKernel]};
rfReplace[i_, c_] := ReplacePart[rfOutputs, i -> c];
rfPass[outs_, key_] := TrueQ[rnOutputChecks[outs][key]];

rfResults = <|
  "positive_computation" -> rfPass[rfOutputs, "computation_ok"],
  "positive_axioms" -> rfPass[rfOutputs, "axioms_ok"],
  "positive_kernel" -> rfPass[rfOutputs, "kernelcheck_ok"],
  "missing_output" -> !rfPass[Most[rfOutputs], "kernelcheck_ok"],
  "wrong_width_three_count" -> !rfPass[rfReplace[3, rfBoxes[ReplacePart[rfComputation,
    {"width, all words, finite-parent words, roots", 3, 3} -> 2]]], "computation_ok"],
  "wrong_orientation" -> !rfPass[rfReplace[3, rfBoxes[ReplacePart[rfComputation,
    "orientation agrees with A269160" -> False]]], "computation_ok"],
  "wrong_key" -> !rfPass[rfReplace[3, rfBoxes[KeyMap[StringReplace[#, "centre" -> "center"] &, rfComputation]]],
    "computation_ok"],
  "extra_computation_key" -> !rfPass[rfReplace[3, rfBoxes[Join[rfComputation, <|"extra" -> 1|>]]], "computation_ok"],
  "computation_code_is_held" -> !rfPass[rfReplace[3, rfBait], "computation_ok"],
  "missing_axiom_key" -> !rfPass[rfReplace[7, rfBoxes[KeyDrop[rfAxioms, "Rule30Submission.finite_parent_small_widths"]]], "axioms_ok"],
  "extra_axiom_key" -> !rfPass[rfReplace[7, rfBoxes[Join[rfAxioms, <|"extra" -> {"propext"}|>]]], "axioms_ok"],
  "wrong_axiom_set" -> !rfPass[rfReplace[7, rfBoxes[Join[rfAxioms, <|"Rule30Submission.finite_parent_count" -> {"propext", "Classical.choice", "Quot.sound"}|>]]],
    "axioms_ok"],
  "unknown_axiom" -> !rfPass[rfReplace[7, rfBoxes[Join[rfAxioms, <|"Rule30Submission.finite_root_age" -> {"propext", "sorryAx"}|>]]],
    "axioms_ok"],
  "failure_containing_Success" -> !rfPass[rfReplace[8, BoxData[InterpretationBox["Success", Failure["Success", <||>]]]],
    "kernelcheck_ok"],
  "display_only_Success" -> !rfPass[rfReplace[8, BoxData["Success"]], "kernelcheck_ok"],
  "wrong_success_tag" -> !rfPass[rfReplace[8, BoxData[InterpretationBox["Success", Success["Other", rfKernel]]]],
    "kernelcheck_ok"],
  "wrong_declaration_count" -> !rfPass[rfReplace[8, rfKCell[Join[rfKernel, <|"Declarations" -> 195|>]]], "kernelcheck_ok"],
  "no_output_code_evaluated" -> (rfSideEffect === 0)
|>;
Print[ExportString[rfResults, "JSON"]];
If[Length[rfResults] === 18 && AllTrue[Values[rfResults], TrueQ],
  Print["FINITE_PAST_OUTPUT_CONTROLS_PASS"]; Exit[0],
  Print["FINITE_PAST_OUTPUT_CONTROLS_FAIL"]; Exit[1]];
