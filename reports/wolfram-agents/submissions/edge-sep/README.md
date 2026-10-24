# Submission edge-sep (in preparation, Cloud, 2026-10-24 16:23 BST): exact edge deadlines for three edge pairs

The first instances of the kit's `EdgeObservable` conjecture (`Rule30TraceEdge`, after cc1e0e0), with exact deadlines:
two configurations with leftmost black cells at -2 and -1 have center columns differing by time 8; at -4 and -3 by time
13; at -3 and -2 by time 14; each attained. Every configuration with those edges, finite or not. Design: GPT's (GC1787,
GPT-CL620-SATURATION-REVIEW.md); the light-cone saturation argument and the finite searches E1, E2, E2b (CL618 to CL620).

Status: the module compiles against the kit at cc1e0e0 (`lake env lean`, 3 min 26 s on Cloud's machine, 1,001 lines,
194 kernel block theorems of 256 signature values each plus three witness checks); the kit's `lake build` and `Check.lean`
receipt are running and will be added here with the module. Files: `essay-template.md` + `assemble.py` -> `essay.md`;
`abstract.md` (246 words); `expected_numbers.py` (independent scalar Python: box maxima at R = m are 8, 13, 14; the
attaining pairs' lanes 44/68, 91/293, 8/33; the saturation 8, 8, 8 at R = 6, 8, 10 for edges -2, -1).
