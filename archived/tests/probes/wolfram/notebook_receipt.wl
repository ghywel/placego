(* GC2107: receipt serialization for trusted notebook-build metadata, not an evaluator/parser of notebook boxes.
   Preserve the raw Wolfram expression. Non-JSON values such as None receive an explicit tagged InputForm;
   they are not silently relabelled Null. A receipt is accepted only after nonempty file/JSON round-trip checks.
   Loading this helper performs no build, LeanLink call or resource/network lookup. *)

nrJSONTag[x_] := <|"wolfram_inputform" -> ToString[x, InputForm]|>;
nrJSONSafe[a_Association] := If[AllTrue[Keys[a], StringQ], Map[nrJSONSafe, a], nrJSONTag[a]];
nrJSONSafe[l_List] := nrJSONSafe /@ l;
nrJSONSafe[x_String] := x;
nrJSONSafe[x_Integer] := x;
nrJSONSafe[x_Real] := x;
nrJSONSafe[True] := True;
nrJSONSafe[False] := False;
nrJSONSafe[Null] := Null;
nrJSONSafe[x_] := nrJSONTag[x];

nrReadReceipt[path_String] := Module[{a},
  If[!FileExistsQ[path] || FileByteCount[path] == 0, Return[$Failed]];
  a = Quiet[Check[Import[path, "RawJSON"], $Failed]];
  If[AssociationQ[a] && Length[a] > 0, a, $Failed]
];

nrReceiptFileOK[path_String, required_List : {}] := Module[{a = nrReadReceipt[path]},
  AssociationQ[a] && AllTrue[required, KeyExistsQ[a, #] &]
];

nrWriteReceipt[path_String, data_Association] := Module[{raw, safe, text, parsed, written, disk},
  raw = FileNameJoin[{DirectoryName[path], FileBaseName[path] <> ".raw.wl"}];
  If[FileExistsQ[path] || FileExistsQ[raw], Return[Failure["ReceiptPathExists", <||>]]];
  If[Length[data] == 0, Return[Failure["EmptyReceipt", <||>]]];
  Quiet[Check[Put[data, raw], Return[Failure["RawReceiptWrite", <||>]]]];
  If[!FileExistsQ[raw] || FileByteCount[raw] == 0, Return[Failure["RawReceiptEmpty", <||>]]];
  safe = nrJSONSafe[data];
  text = Quiet[Check[ExportString[safe, "RawJSON"], $Failed]];
  If[!StringQ[text] || StringLength[text] == 0, Return[Failure["JSONSerialization", <||>]]];
  parsed = Quiet[Check[ImportString[text, "RawJSON"], $Failed]];
  If[!AssociationQ[parsed] || Length[parsed] == 0, Return[Failure["JSONParse", <||>]]];
  written = Quiet[Check[Export[path, text, "Text"], $Failed]];
  If[written === $Failed, Return[Failure["JSONReceiptWrite", <||>]]];
  disk = nrReadReceipt[path];
  If[!AssociationQ[disk] || disk =!= parsed, Return[Failure["JSONFileRoundTrip", <||>]]];
  Success["NotebookReceiptWritten", <|"Bytes" -> FileByteCount[path], "Data" -> disk|>]
];

(* Query only the three properties used successfully by the retained B2 build. The unsupported ReleaseDate
   accessor is deliberately absent. Check wraps each actual query, rather than already evaluated values. *)
nrResourceMetadata[resource_] := AssociationMap[
  Function[key, Quiet[Check[resource[key], Missing["Unavailable", key]]]], {"Name", "Version", "UUID"}];
