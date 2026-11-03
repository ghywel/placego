(* usage: wolframscript -file submit_package.wl NOTEBOOK TITLEFILE ABSTRACTFILE HEADLINES(space-separated) RESPONSEFILE [SUPERSEDES-ID]
   (Local, L1390.) As submit_sub.wl, but the title and abstract come from files (the packages keep the abstract in
   abstract.txt). Every text parameter is wrapped in utf8 (HANDOVER-LOCAL.md step 4). The response goes to RESPONSEFILE,
   kept outside git. *)
{nb, titleFile, absFile, headlines, respFile} = $ScriptCommandLine[[2 ;; 6]];
supersedes = If[Length[$ScriptCommandLine] >= 7, $ScriptCommandLine[[7]], None];
If[$CloudBase === Automatic, $CloudBase = "https://www.wolframcloud.com/"];
If[!TrueQ[$CloudConnected], Print["NOT CONNECTED"]; Exit[1]];
utf8 = FromCharacterCode[ToCharacterCode[#, "UTF-8"]] &;
title = StringTrim[Import[titleFile, "Text", CharacterEncoding -> "UTF-8"]];
abstract = StringTrim[Import[absFile, "Text", CharacterEncoding -> "UTF-8"]];
params = {"notebook" -> File[nb], "problem" -> "1", "claim" -> "partial",
  "title" -> utf8[title], "authors" -> utf8["Gareth Herbert; Claude (Anthropic); GPT (OpenAI)"],
  "agent" -> utf8["Claude Code with Claude Opus 5.5"], "headlines" -> utf8[headlines], "abstract" -> utf8[abstract],
  "repository" -> "https://github.com/ghywel/placego", "consent" -> "true"};
If[supersedes =!= None, AppendTo[params, "supersedes" -> supersedes]];
Print["title: ", title]; Print["abstract words: ", Length[StringSplit[abstract]], "  headlines: ", headlines];
r = URLExecute[CloudObject["https://www.wolframcloud.com/obj/rule-30-prize/Agents/api/submit"], params, "RawJSON"];
Export[respFile, r, "RawJSON"];
If[AssociationQ[r], Print["ok: ", r["ok"], "  id: ", r["id"], "  status: ", r["status"]]; Print["check: ", r["check"]]; Print["page: ", r["page"]];
  If[KeyExistsQ[r, "error"], Print["error: ", r["error"], " / ", r["message"]]], Print["unexpected: ", Head[r]]];
