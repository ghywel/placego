(* universal_start_notebook.wl (Local, L1116): stage B, the universal-start essay's notebook build.

   Evaluate with Get in a FRESH Wolfram MCP kernel (no earlier LeanLink build), after defining
     usEssay    the essay copy to build (its sha256 is checked),
     usNotebook the notebook path to write (must not exist),
     usOut      an existing empty folder for the receipts,
     usKit      the pipeline kit copy (RULE30PRIZE_KIT).
   The caller runs kernel_watch.py on this kernel with the stage's caps, and stops the kernel afterwards.

   Builds the notebook with the Wolfram Institute's MarkdownToNotebook ("UseCache" -> False) under a 900 s
   TimeConstrained, recording every message through a handler. Then it checks the notebook itself:
     * the count of Output cells (predicted 6), the count of Message cells (predicted 0), and no $Failed in any output;
     * the illustration grid, rebuilt from its boxes, equals the retained corrected table row for row
       (receipts/illustration-mcp.md, evaluation 3);
     * the axiom output names no sorryAx, ofReduceBool or trustCompiler, and names propext;
     * the KernelCheck output contains "Success".
   It writes each Output cell's InputForm with a digest, the message packet, a message-name tally and summary.json to
   usOut, prints RESULT OK or RESULT FAIL <reasons>, and touches usOut/DONE last. *)

usReasons = {};
usNote[why_] := AppendTo[usReasons, why];
If[FileHash[usEssay, "SHA256", "HexString"] =!= "01449e0ca0062b00b84a04a5401ac7c04176796e78ee6c4fb96160d065f148a0",
  usNote["essay digest"]];
If[FileExistsQ[usNotebook], usNote["notebook path exists"]];
If[!DirectoryQ[usOut] || FileNames["*", usOut] =!= {}, usNote["receipt folder missing or not empty"]];

If[usReasons === {},
  SetEnvironment["RULE30PRIZE_KIT" -> usKit];
  If[$CloudBase === Automatic, $CloudBase = "https://www.wolframcloud.com/"];
  usURL = "https://www.wolframcloud.com/obj/wolframinstitute/DeployedResources/Function/MarkdownToNotebook";
  usRO = Quiet[ResourceObject[usURL]];
  usProvenance = Quiet[Check[#, "unknown"]] & /@ <|"Name" -> usRO["Name"], "Version" -> usRO["Version"],
    "UUID" -> usRO["UUID"], "ReleaseDate" -> ToString[usRO["ReleaseDate"]]|>;
  usMD2NB = ResourceFunction[usURL];
  usMessages = {};
  usHandler = Function[m, AppendTo[usMessages, m]];
  Internal`AddHandler["Message", usHandler];
  usTiming = AbsoluteTiming[usResult = TimeConstrained[usMD2NB[usEssay, usNotebook, "UseCache" -> False], 900, $TimedOut]];
  Internal`RemoveHandler["Message", usHandler];
  If[usResult === $TimedOut, usNote["build timed out"]];
  If[usResult === $Failed || !FreeQ[usResult, $Failed], usNote["build returned $Failed"]];
  If[!FileExistsQ[usNotebook], usNote["no notebook written"]];
];

If[FileExistsQ[usNotebook],
  usNB = Quiet[Get[usNotebook]];
  usOuts = Cases[usNB, Cell[c_, "Output", ___] :> c, Infinity];
  usMsgCells = Cases[usNB, Cell[_, "Message" | "MSG", ___], Infinity];
  If[Length[usOuts] =!= 6, usNote["output cells " <> ToString[Length[usOuts]]]];
  If[usMsgCells =!= {}, usNote["message cells " <> ToString[Length[usMsgCells]]]];
  If[!FreeQ[usOuts, $Failed], usNote["$Failed in an output"]];
  usStrings = ToString[#, InputForm] & /@ usOuts;
  usDigests = Table[
    Export[FileNameJoin[{usOut, "cell-" <> IntegerString[i, 10, 2] <> ".txt"}], usStrings[[i]], "Text"];
    Hash[usStrings[[i]], "SHA256", "HexString"], {i, Length[usStrings]}];
  usExpected = {
    {"seed bits s0 s1 ...", "m", "periods of D1..Dm", "periods of D(m+1)..D(m+7)"},
    {"1", 2, {2, 2}, {4, 8, 8, 16, 32, 32, 64}},
    {"10010010001", 2, {2, 2}, {4, 8, 8, 16, 32, 32, 64}},
    {"10101000011", 6, {2, 2, 2, 2, 2, 2}, {4, 8, 8, 16, 32, 32, 32}},
    {"10011101011", 2, {2, 2}, {4, 8, 8, 16, 32, 32, 32}},
    {"10010111100", 2, {2, 2}, {4, 8, 8, 16, 32, 32, 32}},
    {"11010011100", 5, {2, 2, 2, 2, 2}, {4, 8, 8, 16, 32, 32, 32}},
    {"11011001101", 4, {2, 2, 2, 2}, {4, 8, 8, 16, 32, 32, 32}}};
  usGrid = Quiet[Cases[ToExpression /@ usOuts, Grid[rows_, ___] :> rows, Infinity]];
  usGridOK = usGrid =!= {} && First[usGrid] === usExpected;
  If[!usGridOK, usNote["illustration grid differs from the retained table"]];
  usAxiomCell = SelectFirst[usStrings, StringContainsQ[#, "propext"] &, ""];
  usAxiomsOK = usAxiomCell =!= "" && StringFreeQ[usAxiomCell, "sorryAx" | "ofReduceBool" | "trustCompiler"];
  If[!usAxiomsOK, usNote["axiom output missing or nonstandard"]];
  usKernelOK = StringContainsQ[Last[usStrings, ""], "Success"];
  If[!usKernelOK, usNote["KernelCheck output lacks Success"]];
];

usNames = If[ValueQ[usMessages],
  Tally[Cases[usMessages, Hold[Message[n_, ___], _] :> ToString[Unevaluated[n], InputForm], {1}]], {}];
usPrinted = If[ValueQ[usMessages], Count[usMessages, Hold[_, True]], 0];
If[ValueQ[usMessages], Put[usMessages, FileNameJoin[{usOut, "messages.m"}]]];
Export[FileNameJoin[{usOut, "summary.json"}], <|
  "essay_sha256" -> FileHash[usEssay, "SHA256", "HexString"],
  "resource" -> If[ValueQ[usProvenance], usProvenance, Null],
  "build_seconds" -> If[ValueQ[usTiming], Round[First[usTiming], 0.1], Null],
  "notebook_sha256" -> If[FileExistsQ[usNotebook], FileHash[usNotebook, "SHA256", "HexString"], Null],
  "notebook_bytes" -> If[FileExistsQ[usNotebook], FileByteCount[usNotebook], Null],
  "output_cells" -> If[ValueQ[usOuts], Length[usOuts], Null],
  "output_digests" -> If[ValueQ[usDigests], usDigests, {}],
  "message_cells" -> If[ValueQ[usMsgCells], Length[usMsgCells], Null],
  "handler_events" -> If[ValueQ[usMessages], Length[usMessages], 0],
  "handler_events_printed" -> usPrinted,
  "handler_tally" -> (Rule @@@ SortBy[usNames, -Last[#] &]),
  "grid_ok" -> TrueQ[usGridOK], "axioms_ok" -> TrueQ[usAxiomsOK], "kernelcheck_ok" -> TrueQ[usKernelOK],
  "kernel_pid" -> $ProcessID,
  "reasons" -> usReasons|>, "JSON"];
Print[If[usReasons === {}, "RESULT OK", "RESULT FAIL " <> StringRiffle[usReasons, "; "]]];
Export[FileNameJoin[{usOut, "DONE"}], "done", "Text"];
