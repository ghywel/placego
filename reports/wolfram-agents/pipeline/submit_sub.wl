(* usage: wolframscript -file submit_sub.wl NAME HEADLINES(space-separated) [SUPERSEDES-ID]
   Every text parameter is wrapped in utf8: with a file in the request, URLExecute sends one byte per character
   (HANDOVER-LOCAL.md step 4, 2026-10-23; the abstracts of submissions 7-9 reached the public page garbled). *)
name = $ScriptCommandLine[[2]]; headlines = $ScriptCommandLine[[3]];
supersedes = If[Length[$ScriptCommandLine] >= 4, $ScriptCommandLine[[4]], None];
If[$CloudBase === Automatic, $CloudBase = "https://www.wolframcloud.com/"];
If[!TrueQ[$CloudConnected], Print["NOT CONNECTED"]; Exit[1]];
utf8 = FromCharacterCode[ToCharacterCode[#, "UTF-8"]] &;
md = Import[FileNameJoin[{Directory[], name, "essay.md"}], "Text", CharacterEncoding -> "UTF-8"];
field[k_] := StringTrim[First[StringCases[md, StartOfLine ~~ k ~~ ": " ~~ v : Except["\n"] .. :> v], ""]];
title = field["Name"]; abstract = field["Abstract"];
params = {"notebook" -> File[FileNameJoin[{Directory[], name, "essay.nb"}]], "problem" -> "1", "claim" -> "partial",
  "title" -> utf8[title], "authors" -> utf8["Gareth Herbert; Claude (Anthropic); GPT (OpenAI)"],
  "agent" -> utf8["Claude Code with Claude Fable 5.1"], "headlines" -> utf8[headlines], "abstract" -> utf8[abstract],
  "repository" -> "https://github.com/ghywel/placego", "consent" -> "true"};
If[supersedes =!= None, AppendTo[params, "supersedes" -> supersedes]];
Print["title: ", title]; Print["abstract chars: ", StringLength[abstract], "  utf8 bytes: ", StringLength[utf8[abstract]], "  headlines: ", headlines, If[supersedes =!= None, "  supersedes: " <> supersedes, ""]];
r = URLExecute[CloudObject["https://www.wolframcloud.com/obj/rule-30-prize/Agents/api/submit"], params, "RawJSON"];
Export[FileNameJoin[{Directory[], name, "submit-response.private.json"}], r, "RawJSON"];
If[AssociationQ[r], Print["ok: ", r["ok"], "  id: ", r["id"], "  status: ", r["status"]]; Print["check: ", r["check"]]; Print["page: ", r["page"]];
  If[KeyExistsQ[r, "error"], Print["error: ", r["error"], " / ", r["message"]]], Print["unexpected: ", Head[r]]];
