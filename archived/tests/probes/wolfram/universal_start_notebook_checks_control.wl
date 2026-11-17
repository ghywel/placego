(* GC2091: small positive/adversarial fixtures for the output gate. NO MarkdownToNotebook, LeanLink,
   resource resolution, dependency setup or certificate evaluation. Run once in a freshly supervised
   Wolfram kernel after source/caps are frozen; retain failure rather than automatically rerun.
   These fixtures test artifact logic, not the real theorem or the actual notebook. *)
Get[FileNameJoin[{DirectoryName[$InputFileName], "universal_start_notebook_checks.wl"}]];
usFixtureSideEffect = 0;
usFixtureAxioms = AssociationMap[If[# === "cert", {"propext"}, usNotebookStandardAxioms] &, usNotebookHeads];
usFixtureKernel = <|"MessageTemplate" -> "The kernel accepts all `1` declarations of `2`.",
  "MessageParameters" -> {258, "LeanLinkTmp123x456"}, "Module" -> "LeanLinkTmp123x456", "Declarations" -> 258|>;
usFixtureAxCell[a_] := BoxData[ToBoxes[a, StandardForm]];
usFixtureKCell[a_] := BoxData[InterpretationBox["Success", Success["KernelChecked", a]]];
usFixtureBait = BoxData[RowBox[{"usFixtureSideEffect", "=", "1"}]];
usFixtureOutputs = {BoxData[ToBoxes[Grid[usNotebookExpectedGrid], StandardForm]], BoxData["True"],
  usFixtureBait, usFixtureBait, usFixtureAxCell[usFixtureAxioms], usFixtureKCell[usFixtureKernel]};
usFixtureReplace[i_, c_] := ReplacePart[usFixtureOutputs, i -> c];
usFixturePass[outs_, key_] := TrueQ[usNotebookOutputChecks[outs][key]];

usFixtureResults = <|
  "positive_grid" -> usFixturePass[usFixtureOutputs, "grid_ok"],
  "positive_axioms" -> usFixturePass[usFixtureOutputs, "axioms_ok"],
  "positive_kernel" -> usFixturePass[usFixtureOutputs, "kernelcheck_ok"],
  "missing_output" -> !usFixturePass[Most[usFixtureOutputs], "kernelcheck_ok"],
  "wrong_grid_value" -> !usFixturePass[usFixtureReplace[1,
    BoxData[ToBoxes[Grid[ReplacePart[usNotebookExpectedGrid, {2, 4, 7} -> 32]], StandardForm]]], "grid_ok"],
  "wrong_grid_head" -> !usFixturePass[usFixtureReplace[1, usFixtureBait], "grid_ok"],
  "unknown_axiom" -> !usFixturePass[usFixtureReplace[5,
    usFixtureAxCell[Join[usFixtureAxioms, <|"run_double" -> {"propext", "customAxiom"}|>]]], "axioms_ok"],
  "missing_axiom_key" -> !usFixturePass[usFixtureReplace[5,
    usFixtureAxCell[KeyDrop[usFixtureAxioms, "rightDiag_step"]]], "axioms_ok"],
  "extra_axiom_key" -> !usFixturePass[usFixtureReplace[5,
    usFixtureAxCell[Join[usFixtureAxioms, <|"extra" -> {"propext"}|>]]], "axioms_ok"],
  "wrong_cert_axioms" -> !usFixturePass[usFixtureReplace[5,
    usFixtureAxCell[Join[usFixtureAxioms, <|"cert" -> usNotebookStandardAxioms|>]]], "axioms_ok"],
  "axiom_code_is_held" -> !usFixturePass[usFixtureReplace[5, usFixtureBait], "axioms_ok"],
  "failure_containing_Success" -> !usFixturePass[usFixtureReplace[6,
    BoxData[InterpretationBox["Success", Failure["Success", <||>]]]], "kernelcheck_ok"],
  "display_only_Success" -> !usFixturePass[usFixtureReplace[6, BoxData["Success"]], "kernelcheck_ok"],
  "wrong_success_tag" -> !usFixturePass[usFixtureReplace[6,
    BoxData[InterpretationBox["Success", Success["Other", usFixtureKernel]]]], "kernelcheck_ok"],
  "wrong_declaration_count" -> !usFixturePass[usFixtureReplace[6,
    usFixtureKCell[Join[usFixtureKernel, <|"Declarations" -> 257|>]]], "kernelcheck_ok"],
  "inconsistent_module" -> !usFixturePass[usFixtureReplace[6,
    usFixtureKCell[Join[usFixtureKernel, <|"Module" -> "LeanLinkTmp789x123"|>]]], "kernelcheck_ok"],
  "no_output_code_evaluated" -> (usFixtureSideEffect === 0)
|>;
Print[ExportString[usFixtureResults, "JSON"]];
If[Length[usFixtureResults] === 17 && AllTrue[Values[usFixtureResults], TrueQ],
  Print["UNIVERSAL_START_OUTPUT_CONTROLS_PASS"]; Exit[0],
  Print["UNIVERSAL_START_OUTPUT_CONTROLS_FAIL"]; Exit[1]];
