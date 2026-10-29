(* GC2110: one fresh supervised arc notebook build, using the checked B2 bare-kernel argument convention.
   Arguments are ESSAY KIT, last2 of $CommandLine. The launcher pins/copies helper/checks/control/driver.
   Exactly6 notebook outputs expected;18 non-building controls run before resolving the converter. *)
{arcEssaySource, arcKit} = Take[$CommandLine, -2];
If[!FileExistsQ[arcEssaySource] || !DirectoryQ[arcKit], Print["ARC_NOTEBOOK_FAIL driver arguments"]; Exit[1]];
arcCapped = Environment["CAPPED_OUT"];
If[!StringQ[arcCapped] || !DirectoryQ[arcCapped], Print["ARC_NOTEBOOK_FAIL no supervised root"]; Exit[1]];
arcExpectedTemp = FileNameSplit[ExpandFileName[FileNameJoin[{arcCapped, "tmp"}]]];
arcActualTemp = FileNameSplit[ExpandFileName[$TemporaryDirectory]];
If[Take[arcActualTemp, UpTo[Length[arcExpectedTemp]]] =!= arcExpectedTemp,
 Print["ARC_NOTEBOOK_FAIL temporary directory outside supervised root"]; Exit[1]];
arcSourceDir = DirectoryName[$InputFileName];
Get[FileNameJoin[{arcSourceDir, "notebook_receipt.wl"}]];
Get[FileNameJoin[{arcSourceDir, "arc_notebook_checks.wl"}]];
Get[FileNameJoin[{arcSourceDir, "arc_notebook_control.wl"}]];
arcControls = arcNotebookControlResults[];
Put[arcControls, FileNameJoin[{arcCapped, "output-controls.wl"}]];
If[Length[arcControls] =!= 18 || !AllTrue[Values[arcControls], TrueQ],
 Print[ExportString[arcControls, "RawJSON"]]; Print["ARC_OUTPUT_CONTROLS_FAIL"]; Exit[1]];
Print["ARC_OUTPUT_CONTROLS_PASS"];
If[FileHash[arcEssaySource, "SHA256", "HexString"] =!= "37bcdad893f1e432cfffc67223665f1ade25b0a6f66ff5859cbea6dc2e641a59",
 Print["ARC_NOTEBOOK_FAIL frozen essay"]; Exit[1]];
arcEssay = FileNameJoin[{arcCapped, "essay.md"}]; CopyFile[arcEssaySource, arcEssay];
arcNotebook = FileNameJoin[{arcCapped, "essay.nb"}];
arcOut = FileNameJoin[{arcCapped, "nb-receipts"}]; CreateDirectory[arcOut];
arcReasons = {}; arcNote[s_] := AppendTo[arcReasons, s];
arcGridOK = False; arcAxiomsOK = False; arcKernelOK = False; arcMessages = {};
SetEnvironment["RULE30PRIZE_KIT" -> arcKit];
If[$CloudBase === Automatic, $CloudBase = "https://www.wolframcloud.com/"];
arcURL = "https://www.wolframcloud.com/obj/wolframinstitute/DeployedResources/Function/MarkdownToNotebook";
arcRO = Quiet[ResourceObject[arcURL]];
arcProvenance = nrResourceMetadata[arcRO];
arcMD2NB = ResourceFunction[arcURL];
arcHandler = Function[m, AppendTo[arcMessages, m]];
Internal`AddHandler["Message", arcHandler];
arcTiming = AbsoluteTiming[arcResult = TimeConstrained[arcMD2NB[arcEssay, arcNotebook, "UseCache" -> False], 900, $TimedOut]];
Internal`RemoveHandler["Message", arcHandler];
If[arcResult === $TimedOut, arcNote["build timed out"]];
If[arcResult === $Failed || !FreeQ[arcResult, $Failed], arcNote["build returned $Failed"]];
If[!FileExistsQ[arcNotebook], arcNote["no notebook written"]];
If[FileExistsQ[arcNotebook],
 arcNB = Quiet[Get[arcNotebook]];
 arcOuts = Cases[arcNB, Cell[c_, "Output", ___] :> c, Infinity];
 arcMsgCells = Cases[arcNB, Cell[_, "Message" | "MSG", ___], Infinity];
 If[Length[arcOuts] =!= 6, arcNote["output count " <> ToString[Length[arcOuts]]]];
 If[arcMsgCells =!= {}, arcNote["message cells " <> ToString[Length[arcMsgCells]]]];
 If[!FreeQ[arcOuts, $Failed], arcNote["$Failed in output"]];
 arcDigests = Table[
  arcCellPath = FileNameJoin[{arcOut, "cell-" <> IntegerString[i,10,2] <> ".txt"}];
  Export[arcCellPath, ToString[arcOuts[[i]], InputForm], "Text"];
  FileHash[arcCellPath,"SHA256","HexString"], {i,Length[arcOuts]}];
 arcChecks = arcNotebookOutputChecks[arcOuts];
 arcGridOK = TrueQ[arcChecks["grid_ok"]]; arcAxiomsOK = TrueQ[arcChecks["axioms_ok"]];
 arcKernelOK = TrueQ[arcChecks["kernelcheck_ok"]];
 If[!arcGridOK, arcNote["threshold grid differs"]];
 If[!arcAxiomsOK, arcNote["axiom output missing or not exact standard sets"]];
 If[!arcKernelOK, arcNote["KernelCheck tag/module/count mismatch"]];
];
Put[arcMessages, FileNameJoin[{arcOut,"messages.m"}]];
arcNames = Tally[Cases[arcMessages, Hold[Message[n_, ___], _] :> ToString[Unevaluated[n],InputForm], {1}]];
arcSummary = <|
 "essay_sha256" -> FileHash[arcEssay,"SHA256","HexString"],
 "source_sha256" -> "56d226a644ffc0c061239fc6daccdd88ba4a69efc9507939994b685411fe9594",
 "resource_url" -> arcURL, "resource" -> arcProvenance,
 "build_seconds" -> Round[First[arcTiming],0.1],
 "notebook_sha256" -> If[FileExistsQ[arcNotebook],FileHash[arcNotebook,"SHA256","HexString"],Null],
 "notebook_bytes" -> If[FileExistsQ[arcNotebook],FileByteCount[arcNotebook],Null],
 "output_cells" -> If[ValueQ[arcOuts],Length[arcOuts],Null],
 "output_digests" -> If[ValueQ[arcDigests],arcDigests,{}],
 "message_cells" -> If[ValueQ[arcMsgCells],Length[arcMsgCells],Null],
 "handler_events" -> Length[arcMessages], "handler_events_printed" -> Count[arcMessages,Hold[_,True]],
 "handler_tally" -> (<|"name"->First[#],"count"->Last[#]|> & /@ SortBy[arcNames,-Last[#]&]),
 "output_controls" -> arcControls,
 "grid_ok" -> arcGridOK, "axioms_ok" -> arcAxiomsOK, "kernelcheck_ok" -> arcKernelOK,
 "kernelcheck_data" -> If[ValueQ[arcChecks],arcChecks["kernelcheck_data"],Null], "reasons" -> arcReasons|>;
arcSummaryPath = FileNameJoin[{arcOut,"summary.json"}];
arcWritten = nrWriteReceipt[arcSummaryPath,arcSummary];
arcRequired = {"essay_sha256","source_sha256","output_cells","output_digests","grid_ok","axioms_ok","kernelcheck_ok","kernelcheck_data","resource","reasons"};
arcSummaryOK = MatchQ[arcWritten,Success["NotebookReceiptWritten",_Association]] && nrReceiptFileOK[arcSummaryPath,arcRequired];
If[arcSummaryOK,
 arcParsed = nrReadReceipt[arcSummaryPath];
 arcSummaryOK = arcParsed["reasons"] === {} && arcParsed["output_cells"] === 6 &&
   AllTrue[{"grid_ok","axioms_ok","kernelcheck_ok"},TrueQ[arcParsed[#]]&];
];
If[arcSummaryOK, Export[FileNameJoin[{arcOut,"DONE"}],"done","Text"]];
arcPass = arcReasons === {} && arcGridOK && arcAxiomsOK && arcKernelOK && arcSummaryOK &&
 FileExistsQ[arcNotebook] && FileExistsQ[FileNameJoin[{arcOut,"messages.m"}]] && FileExistsQ[FileNameJoin[{arcOut,"DONE"}]];
Print[If[TrueQ[arcPass],"ARC_NOTEBOOK_PASS","ARC_NOTEBOOK_FAIL " <> StringRiffle[arcReasons,"; "]]];
Exit[If[TrueQ[arcPass],0,1]];
