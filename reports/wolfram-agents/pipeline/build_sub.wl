(* usage: wolframscript -file build_sub.wl NAME [OUTPUT-NOTEBOOK]      (revision 4, 2026-10-24, GC1800: the printed digests are FileHash of the
   file bytes; revision 3 printed Hash[File[...]], the hash of the File expression, which matches no byte digest; revision 3 for GC1762 gate 4
   and GC1764 item 2)
   OUTPUT-NOTEBOOK, when given, is the absolute path the notebook is written to (the supervised stage passes a path inside
   its monitored output folder); otherwise NAME/essay.nb.
   Builds NAME/essay.nb from NAME/essay.md with the Wolfram Institute's MarkdownToNotebook, LeanLink building and
   kernel-replaying the essay's Lean module against the kit copy in this folder. Prints the resolved resource's
   provenance, the wall time, the result head, and a final `RESULT OK` or `RESULT FAIL <why>` line; exits 1 on any failure
   (missing essay, failed conversion, no fresh notebook file). *)
name = $ScriptCommandLine[[2]];
fail[why_] := (Print["RESULT FAIL ", why]; Exit[1]);
essay = FileNameJoin[{Directory[], name, "essay.md"}];
nbout = If[Length[$ScriptCommandLine] >= 3, $ScriptCommandLine[[3]], FileNameJoin[{Directory[], name, "essay.nb"}]];
If[!FileExistsQ[essay], fail["no essay: " <> essay]];
If[FileExistsQ[nbout], fail["the output notebook already exists; move it aside so the output is fresh"]];
Print["notebook path: ", nbout];
If[$CloudBase === Automatic, $CloudBase = "https://www.wolframcloud.com/"];
SetEnvironment["RULE30PRIZE_KIT" -> FileNameJoin[{Directory[], "Rule30PrizeKit"}]];
Print["essay sha256: ", FileHash[essay, "SHA256", "HexString"]];
url = "https://www.wolframcloud.com/obj/wolframinstitute/DeployedResources/Function/MarkdownToNotebook";
ro = Quiet[ResourceObject[url]];
Print["resource: ", url];
Print["resource provenance: name ", Quiet[Check[ro["Name"], "unknown"]], "  version ", Quiet[Check[ro["Version"], "unknown"]],
  "  uuid ", Quiet[Check[ro["UUID"], "unknown"]], "  updated ", Quiet[Check[ro["ReleaseDate"], "unknown"]]];
md2nb = ResourceFunction[url];
If[Head[md2nb] =!= ResourceFunction, fail["resource function did not resolve"]];
t = AbsoluteTiming[r = md2nb[essay, nbout, "UseCache" -> False]];
Print["build seconds: ", Round[First[t], 0.1], "  result: ", Shallow[r, 2]];
If[r === $Failed || Head[r] === ResourceFunction || !FreeQ[r, $Failed], fail["conversion failed"]];
If[!FileExistsQ[nbout], fail["no notebook written"]];
Print["notebook bytes: ", FileByteCount[nbout], "  sha256: ", FileHash[nbout, "SHA256", "HexString"]];
Print["RESULT OK"];
