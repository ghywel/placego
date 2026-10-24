(* usage: wolframscript -file build_sub.wl NAME *)
name = $ScriptCommandLine[[2]];
If[$CloudBase === Automatic, $CloudBase = "https://www.wolframcloud.com/"];
SetEnvironment["RULE30PRIZE_KIT" -> FileNameJoin[{Directory[], "Rule30PrizeKit"}]];
md2nb = ResourceFunction["https://www.wolframcloud.com/obj/wolframinstitute/DeployedResources/Function/MarkdownToNotebook"];
t = AbsoluteTiming[r = md2nb[FileNameJoin[{Directory[], name, "essay.md"}], FileNameJoin[{Directory[], name, "essay.nb"}], "UseCache" -> False]];
Print["build seconds: ", Round[First[t], 0.1], "  result: ", Shallow[r, 2]];
