#!/usr/bin/env python3
"""four_fronts_portal.py BASE FINAL OUT (Local, L1524): the portal form of the forced front on the four strips. The verifier's kit (722a0c51) holds neither
Rule30UniversalLeftSide nor Rule30FourLeftSides, and a submission is one module, so the form repeats the posted module of R30-20261104-458f3b and adds the
kit form's two modules in the same namespace, with only their module headers, opens and qualified names changed."""
import re, sys
FOUR = 'reports/wolfram-agents/submissions/four-left-sides/Rule30Submission.lean'
four = open(FOUR).read()
base = open(sys.argv[1]).read()
fin = open(sys.argv[2]).read()
i = four.index('namespace Rule30Submission\n')
body = four[i:four.rindex('end Rule30Submission')].rstrip() + '\n'
def inner(src, name):
    a = src.index('set_option autoImplicit false\n') + len('set_option autoImplicit false\n')
    b = src.index('end Ruliology.CellularAutomata.' + name)
    return src[a:b].strip() + '\n'
def strip(s):
    return s.replace('Rule30FourLeftSides.', '').replace('Rule30UniversalLeftSide.', '')
head = '''import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30AgedLeftDiagonals

/-!
# The forced front of rule 30 on the four left strips: an explicit tick for every configuration with a leftmost black cell

R30-20261104-458f3b placed every configuration with a leftmost black cell on one of four strips through wheel 87,866, after a time
shift and from some time on. Here the time is explicit. Every such configuration is on its strip through wheel 87,866 from tick
177,560 + s of its own clock, with s at most 15 (`forced_front_four_left_side`), and through wheel 53,207 from tick 107,310 + s
(`forced_front_low_left_side`). `forced_front_four` gives the time wheel by wheel: the settling recursion of the kit's `Rule30FrontLaw`,
run on each strip's sixteen-row cycle. `classification_bounded` is the classification of 458f3b with its shift bounded by 15.

The recursion is evaluated as a walk. From wheel `j` at tick `t`, move to wheel `j + 1` if the strip's cell is black and stay if it is
white, the tick moving on either way (`walk`, `frun_of_walk`). That is one addition, one shift and one mask per tick, so the kernel
runs all four strips in seconds. The first part of this module repeats 458f3b, because the verifier's kit does not hold it. Nothing
here concerns the center column or the Prize problems, and 87,866 is where these rows stop, not a claim about what happens beyond it.
-/

'''
out = head + body + '\n/-! ## The forced front -/\n\n' + strip(inner(base, 'Rule30FourFrontsBase')) + '\n' + strip(inner(fin, 'Rule30FourFronts')) + '\nend Rule30Submission\n'
assert '"' not in out and '\\\\' not in out, 'the portal form takes neither a double quote nor a backslash'
open(sys.argv[3], 'w').write(out)
print('wrote', sys.argv[3], len(out), 'bytes')
