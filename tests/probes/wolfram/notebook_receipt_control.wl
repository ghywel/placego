(* GC2107: small, non-building controls. Fresh supervised bare kernel only, with CAPPED_OUT already set.
   No MarkdownToNotebook/LeanLink/resource/dependency lookup. Do not rerun a failed control automatically. *)
Get[FileNameJoin[{DirectoryName[$InputFileName], "notebook_receipt.wl"}]];
nrOut = Environment["CAPPED_OUT"];
If[!StringQ[nrOut] || !DirectoryQ[nrOut], Print["NOTEBOOK_RECEIPT_CONTROLS_FAIL no supervised root"]; Exit[1]];
nrExpectedTemp = FileNameSplit[ExpandFileName[FileNameJoin[{nrOut, "tmp"}]]];
nrActualTemp = FileNameSplit[ExpandFileName[$TemporaryDirectory]];
If[Take[nrActualTemp, UpTo[Length[nrExpectedTemp]]] =!= nrExpectedTemp,
 Print["NOTEBOOK_RECEIPT_CONTROLS_FAIL temporary directory outside supervised root"]; Exit[1]];
nrPath = FileNameJoin[{nrOut, "summary.json"}];
nrData = <|"reasons" -> {}, "kernelcheck_ok" -> True, "kernelcheck_data" -> <|"optional" -> None|>,
  "resource" -> <|"Name" -> "fixture", "Version" -> Missing["Unavailable", "Version"]|>,
  "handler_tally" -> {<|"name" -> "fixture::event", "count" -> 2|>},
  "measured_seconds" -> 0.25, "explicit_null" -> Null, "exact_fraction" -> 1/3|>;
nrResult = nrWriteReceipt[nrPath, nrData];
nrParsed = nrReadReceipt[nrPath];
nrRaw = Quiet[Check[Get[FileNameJoin[{nrOut, "summary.raw.wl"}]], $Failed]];
nrEmpty = FileNameJoin[{nrOut, "empty.json"}]; Export[nrEmpty, "", "Text"];
nrBad = FileNameJoin[{nrOut, "malformed.json"}]; Export[nrBad, "{bad", "Text"];
nrScalar = FileNameJoin[{nrOut, "scalar.json"}]; Export[nrScalar, "12", "Text"];
nrNoFields = FileNameJoin[{nrOut, "no-fields.json"}]; Export[nrNoFields, "{}", "Text"];
nrBytesBefore = FileHash[nrPath, "SHA256"];
nrNoOverwrite = nrWriteReceipt[nrPath, <|"replacement" -> True|>];
nrControls = <|
 "positive_write" -> MatchQ[nrResult, Success["NotebookReceiptWritten", _Association]],
 "positive_nonempty_parsed" -> nrReceiptFileOK[nrPath, {"reasons", "kernelcheck_ok", "kernelcheck_data"}],
 "raw_exact" -> (nrRaw === nrData),
 "none_explicit_tag" -> (nrParsed["kernelcheck_data"]["optional"] === <|"wolfram_inputform" -> "None"|>),
 "missing_explicit_tag" -> StringQ[nrParsed["resource"]["Version"]["wolfram_inputform"]],
 "fraction_preserved_as_expression" -> (nrParsed["exact_fraction"] === <|"wolfram_inputform" -> "1/3"|>),
 "json_values_preserved" -> (TrueQ[nrParsed["kernelcheck_ok"]] && nrParsed["reasons"] === {} && nrParsed["explicit_null"] === Null),
 "empty_file_rejected" -> !nrReceiptFileOK[nrEmpty],
 "malformed_file_rejected" -> !nrReceiptFileOK[nrBad],
 "scalar_json_rejected" -> !nrReceiptFileOK[nrScalar],
 "empty_object_rejected" -> !nrReceiptFileOK[nrNoFields],
 "missing_file_rejected" -> !nrReceiptFileOK[FileNameJoin[{nrOut, "absent.json"}]],
 "required_key_rejected" -> !nrReceiptFileOK[nrPath, {"missing_required"}],
 "no_overwrite" -> (MatchQ[nrNoOverwrite, Failure["ReceiptPathExists", _Association]] && FileHash[nrPath, "SHA256"] === nrBytesBefore)
|>;
Print[ExportString[nrControls, "RawJSON"]];
If[Length[nrControls] === 14 && AllTrue[Values[nrControls], TrueQ],
 Print["NOTEBOOK_RECEIPT_CONTROLS_PASS"]; Exit[0], Print["NOTEBOOK_RECEIPT_CONTROLS_FAIL"]; Exit[1]];
