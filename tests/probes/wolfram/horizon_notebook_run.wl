(* L1184, with L1187's essay pin: one fresh supervised horizon notebook build, adapted from the arc's GC2115 driver
   (arc_notebook_run.wl). Arguments are ESSAY KIT, the last two of $CommandLine. The launcher pins/copies
   helper/checks/control/driver. Exactly 5 notebook outputs expected; 20 non-building controls run before resolving
   the converter. *)
{hzEssaySource, hzKit} = Take[$CommandLine, -2];
If[!FileExistsQ[hzEssaySource] || !DirectoryQ[hzKit], Print["HORIZON_NOTEBOOK_FAIL driver arguments"]; Exit[1]];
hzCapped = Environment["CAPPED_OUT"];
If[!StringQ[hzCapped] || !DirectoryQ[hzCapped], Print["HORIZON_NOTEBOOK_FAIL no supervised root"]; Exit[1]];
hzExpectedTemp = FileNameSplit[ExpandFileName[FileNameJoin[{hzCapped, "tmp"}]]];
hzActualTemp = FileNameSplit[ExpandFileName[$TemporaryDirectory]];
If[Take[hzActualTemp, UpTo[Length[hzExpectedTemp]]] =!= hzExpectedTemp,
 Print["HORIZON_NOTEBOOK_FAIL temporary directory outside supervised root"]; Exit[1]];
hzSourceDir = DirectoryName[$InputFileName];
Get[FileNameJoin[{hzSourceDir, "notebook_receipt.wl"}]];
Get[FileNameJoin[{hzSourceDir, "horizon_notebook_checks.wl"}]];
Get[FileNameJoin[{hzSourceDir, "horizon_notebook_control.wl"}]];
hzControls = hzNotebookControlResults[];
Put[hzControls, FileNameJoin[{hzCapped, "output-controls.wl"}]];
If[Length[hzControls] =!= 20 || !AllTrue[Values[hzControls], TrueQ],
 Print[ExportString[hzControls, "RawJSON"]]; Print["HORIZON_OUTPUT_CONTROLS_FAIL"]; Exit[1]];
Print["HORIZON_OUTPUT_CONTROLS_PASS"];
If[FileHash[hzEssaySource, "SHA256", "HexString"] =!= "203fd0a6e9b43861e85b94fb62f5e257e9712a1235cd78a9c2e3e2a79c4e1def",
 Print["HORIZON_NOTEBOOK_FAIL frozen essay"]; Exit[1]];
hzEssay = FileNameJoin[{hzCapped, "essay.md"}]; CopyFile[hzEssaySource, hzEssay];
hzNotebook = FileNameJoin[{hzCapped, "essay.nb"}];
hzOut = FileNameJoin[{hzCapped, "nb-receipts"}]; CreateDirectory[hzOut];
hzReasons = {}; hzNote[s_] := AppendTo[hzReasons, s];
hzGridOK = False; hzAxiomsOK = False; hzKernelOK = False; hzMessages = {};
SetEnvironment["RULE30PRIZE_KIT" -> hzKit];
If[$CloudBase === Automatic, $CloudBase = "https://www.wolframcloud.com/"];
hzURL = "https://www.wolframcloud.com/obj/wolframinstitute/DeployedResources/Function/MarkdownToNotebook";
hzRO = Quiet[ResourceObject[hzURL]];
hzProvenance = nrResourceMetadata[hzRO];
hzMD2NB = ResourceFunction[hzURL];
hzHandler = Function[m, AppendTo[hzMessages, m]];
Internal`AddHandler["Message", hzHandler];
hzTiming = AbsoluteTiming[hzResult = TimeConstrained[hzMD2NB[hzEssay, hzNotebook, "UseCache" -> False], 900, $TimedOut]];
Internal`RemoveHandler["Message", hzHandler];
If[hzResult === $TimedOut, hzNote["build timed out"]];
If[hzResult === $Failed || !FreeQ[hzResult, $Failed], hzNote["build returned $Failed"]];
If[!FileExistsQ[hzNotebook], hzNote["no notebook written"]];
If[FileExistsQ[hzNotebook],
 hzNB = Quiet[Get[hzNotebook]];
 hzOuts = Cases[hzNB, Cell[c_, "Output", ___] :> c, Infinity];
 hzMsgCells = Cases[hzNB, Cell[_, "Message" | "MSG", ___], Infinity];
 If[Length[hzOuts] =!= 5, hzNote["output count " <> ToString[Length[hzOuts]]]];
 If[hzMsgCells =!= {}, hzNote["message cells " <> ToString[Length[hzMsgCells]]]];
 If[!FreeQ[hzOuts, $Failed], hzNote["$Failed in output"]];
 hzDigests = Table[
  hzCellPath = FileNameJoin[{hzOut, "cell-" <> IntegerString[i, 10, 2] <> ".txt"}];
  Export[hzCellPath, ToString[hzOuts[[i]], InputForm], "Text"];
  FileHash[hzCellPath, "SHA256", "HexString"], {i, Length[hzOuts]}];
 hzChecks = hzNotebookOutputChecks[hzOuts];
 hzGridOK = TrueQ[hzChecks["grid_ok"]]; hzAxiomsOK = TrueQ[hzChecks["axioms_ok"]];
 hzKernelOK = TrueQ[hzChecks["kernelcheck_ok"]];
 If[!hzGridOK, hzNote["illustration grid differs"]];
 If[!hzAxiomsOK, hzNote["axiom output missing or not exact standard sets"]];
 If[!hzKernelOK, hzNote["KernelCheck tag/module/count mismatch"]];
];
Put[hzMessages, FileNameJoin[{hzOut, "messages.m"}]];
hzNames = Tally[Cases[hzMessages, Hold[Message[n_, ___], _] :> ToString[Unevaluated[n], InputForm], {1}]];
hzSummary = <|
 "essay_sha256" -> FileHash[hzEssay, "SHA256", "HexString"],
 "source_sha256" -> "791e45ed1aef3955035989f1443f43a3427ea82b0cb01a8ad088bc221ec57110",
 "resource_url" -> hzURL, "resource" -> hzProvenance,
 "build_seconds" -> Round[First[hzTiming], 0.1],
 "notebook_sha256" -> If[FileExistsQ[hzNotebook], FileHash[hzNotebook, "SHA256", "HexString"], Null],
 "notebook_bytes" -> If[FileExistsQ[hzNotebook], FileByteCount[hzNotebook], Null],
 "output_cells" -> If[ValueQ[hzOuts], Length[hzOuts], Null],
 "output_digests" -> If[ValueQ[hzDigests], hzDigests, {}],
 "message_cells" -> If[ValueQ[hzMsgCells], Length[hzMsgCells], Null],
 "handler_events" -> Length[hzMessages], "handler_events_printed" -> Count[hzMessages, Hold[_, True]],
 "handler_tally" -> (<|"name" -> First[#], "count" -> Last[#]|> & /@ SortBy[hzNames, -Last[#] &]),
 "output_controls" -> hzControls,
 "grid_ok" -> hzGridOK, "axioms_ok" -> hzAxiomsOK, "kernelcheck_ok" -> hzKernelOK,
 "kernelcheck_data" -> If[ValueQ[hzChecks], hzChecks["kernelcheck_data"], Null], "reasons" -> hzReasons|>;
hzSummaryPath = FileNameJoin[{hzOut, "summary.json"}];
hzWritten = nrWriteReceipt[hzSummaryPath, hzSummary];
hzRequired = {"essay_sha256", "source_sha256", "output_cells", "output_digests", "grid_ok", "axioms_ok",
 "kernelcheck_ok", "kernelcheck_data", "resource", "reasons"};
hzSummaryOK = MatchQ[hzWritten, Success["NotebookReceiptWritten", _Association]] && nrReceiptFileOK[hzSummaryPath, hzRequired];
If[hzSummaryOK,
 hzParsed = nrReadReceipt[hzSummaryPath];
 hzSummaryOK = hzParsed["reasons"] === {} && hzParsed["output_cells"] === 5 &&
   AllTrue[{"grid_ok", "axioms_ok", "kernelcheck_ok"}, TrueQ[hzParsed[#]] &];
];
If[hzSummaryOK, Export[FileNameJoin[{hzOut, "DONE"}], "done", "Text"]];
hzPass = hzReasons === {} && hzGridOK && hzAxiomsOK && hzKernelOK && hzSummaryOK &&
 FileExistsQ[hzNotebook] && FileExistsQ[FileNameJoin[{hzOut, "messages.m"}]] && FileExistsQ[FileNameJoin[{hzOut, "DONE"}]];
Print[If[TrueQ[hzPass], "HORIZON_NOTEBOOK_PASS", "HORIZON_NOTEBOOK_FAIL " <> StringRiffle[hzReasons, "; "]]];
Exit[If[TrueQ[hzPass], 0, 1]];
