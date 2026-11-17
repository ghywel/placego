#!/usr/bin/env python3
"""gen_portal.py (Local, L1548): the portal form of the wall entry: the three kit modules in one module, in namespace Rule30Submission, with only their headers and namespaces changed."""
import re,sys
def inner(f):
    s=open(f,encoding='utf-8').read()
    a=s.index('namespace Ruliology.CellularAutomata.Rule30RightWall\n')
    a=s.index('\n',a)+1
    b=s.rindex('end Ruliology.CellularAutomata.Rule30RightWall')
    t=s[a:b]
    t=re.sub(r'^open Rule30FrozenRuler\n','',t,flags=re.M)
    t=re.sub(r'^open WindowClosed\n\nset_option autoImplicit false\nset_option maxRecDepth 100000\n','',t,flags=re.M)
    t=re.sub(r'^set_option autoImplicit false\nset_option maxRecDepth 8192\n','',t,flags=re.M)
    return t.strip()+'\n'
head=open(sys.argv[1],encoding='utf-8').read()
body=head+'\nnamespace Rule30Submission\n\nopen Ruliology.CellularAutomata Rule30FrozenRuler\n\nset_option autoImplicit false\nset_option maxRecDepth 100000\n\n'
body+=inner('Rule30RightWall.lean')+'\nopen WindowClosed\n\n'+inner('Rule30RightWallLocks.lean')+'\n'+inner('Rule30RightWallCloud.lean')+'\nend Rule30Submission\n'
assert '"' not in body and '\\' not in body,'the portal form takes neither a double quote nor a backslash'
open('Rule30Submission.lean','w',encoding='utf-8').write(body)
print(len(body))
