(* period_three_language_notebook.wl (Local, S-14): the release build of the period-three language essay, adapted from sideways_locks_notebook.wl. Run as `WolframKernel -script` through
   universal_start_notebook_launch.py, under run_capped.py --track-tree, from a built kit at the verifier's commit:  KERNEL period_three_language_notebook.wl ESSAY KIT.
   The essay digest is read from essay.sha256 next to it. Gates: 6 Output cells, no Message cells, no $Failed; the first cell equal to the plain Python replay
   (period_three_language_replay.py); the Abstract cell equal to abstract.txt; the icon payload equal to the raw bytes of Rule30Submission.lean; the kit cell True; a LeanEnvironment;
   the headlines' axiom sets as Check printed them at the verifier's kit; KernelChecked at the count Check printed. *)

{rnEssaySource, rnKit} = Take[$CommandLine, -2];
rnReasons = {};
rnNote[why_] := AppendTo[rnReasons, why];
rnCapped = Environment["CAPPED_OUT"];
If[!StringQ[rnCapped] || !DirectoryQ[rnCapped], Print["RESULT FAIL no CAPPED_OUT"]; Exit[1]];
If[Take[FileNameSplit[ExpandFileName[$TemporaryDirectory]], UpTo[Length[FileNameSplit[ExpandFileName[FileNameJoin[{rnCapped, "tmp"}]]]]]] =!=
    FileNameSplit[ExpandFileName[FileNameJoin[{rnCapped, "tmp"}]]], Print["RESULT FAIL temporary directory outside supervised root"]; Exit[1]];
rnHere = DirectoryName[$InputFileName];
If[Quiet[Check[Get[FileNameJoin[{rnHere, "notebook_receipt.wl"}]], $Failed]] === $Failed, rnNote["receipt helper did not load"]];
rnEssay = FileNameJoin[{rnCapped, "essay.md"}];
CopyFile[rnEssaySource, rnEssay];
rnPin = StringTrim[Import[FileNameJoin[{DirectoryName[rnEssaySource], "essay.sha256"}], "Text"]];
If[FileHash[rnEssay, "SHA256", "HexString"] =!= rnPin, rnNote["essay digest"]];
rnNotebook = FileNameJoin[{rnCapped, "essay.nb"}];
rnOut = FileNameJoin[{rnCapped, "nb-receipts"}];
CreateDirectory[rnOut];

rnAxioms = <|"no_pattern3" -> {"Classical.choice", "Quot.sound", "propext"}, "col1_011" -> {"Classical.choice", "Quot.sound", "propext"}, "free_bits_011" -> {"Classical.choice", "Quot.sound", "propext"}, "col1_001" -> {"Classical.choice", "Quot.sound", "propext"}, "free_bits_001" -> {"Classical.choice", "Quot.sound", "propext"}, "C3r011_of_C3w" -> {"propext"}, "not_eventually_011_of_C3r" -> {"Classical.choice", "Quot.sound", "propext"}, "C3g001_of_C3s" -> {"propext"}, "not_eventually_001_of_C3g" -> {"Classical.choice", "Quot.sound", "propext"}, "no_eventual_period_three_of_C3g" -> {"Classical.choice", "Quot.sound", "propext"}|>;
rnHeads = Keys[rnAxioms];
rnDeclarations = 142;
rnExpected = {{{3, 136}, 136, {False, False, False, False, False, False, False, False, True, True}}, {{3, 3, 6, 553}, 553, {False, False, False, False, False, False, False, False, False, False, True, True, True}}};
rnHeld[BoxData[b_]] := Quiet[Check[ToExpression[b, StandardForm, HoldComplete], $Failed]];
rnHeld[_] := $Failed;

If[rnReasons === {},
  SetEnvironment["RULE30PRIZE_KIT" -> rnKit];
  If[$CloudBase === Automatic, $CloudBase = "https://www.wolframcloud.com/"];
  rnConnected = TrueQ[$CloudConnected];
  If[!rnConnected, rnNote["kernel not connected to the cloud"]];
  rnMD2NB = ResourceFunction["https://www.wolframcloud.com/obj/wolframinstitute/DeployedResources/Function/MarkdownToNotebook"];
  rnMessages = {};
  rnHandler = Function[m, AppendTo[rnMessages, m]];
  Internal`AddHandler["Message", rnHandler];
  rnTiming = AbsoluteTiming[rnResult = TimeConstrained[rnMD2NB[rnEssay, rnNotebook, "UseCache" -> False], 900, $TimedOut]];
  Internal`RemoveHandler["Message", rnHandler];
  If[rnResult === $TimedOut, rnNote["build timed out"]];
  If[rnResult === $Failed || !FreeQ[rnResult, $Failed], rnNote["build returned $Failed"]];
  If[!FileExistsQ[rnNotebook], rnNote["no notebook written"]];
];

If[FileExistsQ[rnNotebook],
  rnNB = Quiet[Get[rnNotebook]];
  rnOuts = Cases[rnNB, Cell[c_, "Output", ___] :> c, Infinity];
  rnMsgCells = Cases[rnNB, Cell[_, "Message" | "MSG", ___], Infinity];
  If[Length[rnOuts] =!= 6, rnNote["output cells " <> ToString[Length[rnOuts]]]];
  If[rnMsgCells =!= {}, rnNote["message cells " <> ToString[Length[rnMsgCells]]]];
  If[!FreeQ[rnOuts, $Failed], rnNote["$Failed in an output"]];
  (* raw bytes, not Import "Text", which drops the final newline (L1509, nb4) *)
  rnSource = ByteArrayToString[ReadByteArray[FileNameJoin[{DirectoryName[rnEssaySource], "Rule30Submission.lean"}]], "UTF-8"];
  rnIconSources = Cases[rnNB,
    (HoldPattern[InterpretationBox[display_, value_String, ___]] /;
      !FreeQ[display, "IconizedObject"] && StringStartsQ[value, "import Ruliology."]) :> value, Infinity];
  rnIconOK = rnIconSources === {rnSource};
  If[!rnIconOK, rnNote["the icon payload differs from the reviewed portal source"]];
  rnAbstractFile = FileNameJoin[{DirectoryName[rnEssaySource], "abstract.txt"}];
  rnAbstractCells = Cases[rnNB, Cell[c_String, "Abstract", ___] :> c, Infinity];
  rnAbstractOK = rnAbstractCells === {StringTrim[Import[rnAbstractFile, "Text", CharacterEncoding -> "UTF-8"]]};
  If[!rnAbstractOK, rnNote["Abstract cell differs from abstract.txt"]];
  rnStrings = ToString[#, InputForm] & /@ rnOuts;
  rnDigests = Table[Export[FileNameJoin[{rnOut, "cell-" <> IntegerString[i, 10, 2] <> ".txt"}], rnStrings[[i]], "Text"];
    Hash[rnStrings[[i]], "SHA256", "HexString"], {i, Length[rnStrings]}];
  If[Length[rnOuts] === 6,
    rnWhiteOK = With[{got = ReleaseHold[rnHeld[rnOuts[[1]]]]}, got === rnExpected];
    If[!rnWhiteOK, rnNote["first cell differs from the Python replay"]];
    rnGridOK = True;
    rnKitOK = rnHeld[rnOuts[[2]]] === HoldComplete[True];
    If[!rnKitOK, rnNote["kit directory cell is not True"]];
    rnEnvOK = !FreeQ[rnOuts[[3]], "LeanEnvironment"];
    If[!rnEnvOK, rnNote["no LeanEnvironment"]];
    rnAx = rnHeld[rnOuts[[5]]];
    rnAxiomsOK = MatchQ[rnAx, HoldComplete[_Association]] && With[{a = ReleaseHold[rnAx]},
      Sort[Keys[a]] === Sort[rnHeads] && AllTrue[rnHeads, Sort[ToString /@ a[#]] === Sort[rnAxioms[#]] &]];
    If[!rnAxiomsOK, rnNote["axiom sets differ"]];
    rnKC = Cases[rnOuts[[6]], HoldPattern[InterpretationBox[_, s : Success["KernelChecked", _Association], ___]] :> s, Infinity];
    rnKernelOK = Length[rnKC] === 1 && With[{a = First[rnKC][[2]]},
      a["Declarations"] === rnDeclarations && StringQ[a["Module"]] && StringStartsQ[a["Module"], "LeanLinkTmp"] &&
      a["MessageParameters"] === {rnDeclarations, a["Module"]} && a["MessageTemplate"] === "The kernel accepts all `1` declarations of `2`."];
    If[!rnKernelOK, rnNote["KernelCheck object, module or count differs"]];
  ];
];

rnSummary = <|
  "essay_sha256" -> FileHash[rnEssay, "SHA256", "HexString"],
  "driver_sha256" -> FileHash[$InputFileName, "SHA256", "HexString"],
  "build_seconds" -> If[ValueQ[rnTiming], Round[First[rnTiming], 0.1], Missing["NotBuilt"]],
  "notebook_sha256" -> If[FileExistsQ[rnNotebook], FileHash[rnNotebook, "SHA256", "HexString"], Missing["NoNotebook"]],
  "notebook_bytes" -> If[FileExistsQ[rnNotebook], FileByteCount[rnNotebook], Missing["NoNotebook"]],
  "output_cells" -> If[ValueQ[rnOuts], Length[rnOuts], Missing["NoNotebook"]],
  "output_digests" -> If[ValueQ[rnDigests], rnDigests, {}],
  "message_cells" -> If[ValueQ[rnMsgCells], Length[rnMsgCells], Missing["NoNotebook"]],
  "handler_events" -> If[ValueQ[rnMessages], Length[rnMessages], 0],
  "iconized" -> TrueQ[rnIconOK], "embedded_source_matches" -> TrueQ[rnIconOK], "axioms_ok" -> TrueQ[rnAxiomsOK], "abstract_ok" -> TrueQ[rnAbstractOK],
  "white_ok" -> TrueQ[rnWhiteOK], "table_ok" -> TrueQ[rnGridOK],
  "kernelcheck_ok" -> TrueQ[rnKernelOK], "environment_ok" -> TrueQ[rnEnvOK],
  "kernelcheck_declarations" -> If[ValueQ[rnKC] && rnKC =!= {}, First[rnKC][[2]]["Declarations"], Missing["NotChecked"]],
  "reasons" -> rnReasons|>;
rnWrite = nrWriteReceipt[FileNameJoin[{rnOut, "summary.json"}], rnSummary];
If[FailureQ[rnWrite], rnNote["summary receipt failed"]];
Print[If[rnReasons === {}, "RESULT OK", "RESULT FAIL " <> StringRiffle[rnReasons, "; "]]];
Export[FileNameJoin[{rnOut, "DONE"}], "done", "Text"];
Exit[If[rnReasons === {}, 0, 1]];
