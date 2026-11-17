"""Independent integer-only replay of emitted matrix inequalities; never trusts floating eigenvalues."""
import json,sys
from pathlib import Path
out=Path(sys.argv[1]);count=0
for path in sorted(out.glob('analysis-[0-9]*.json')):
    obj=json.loads(path.read_text());tr=json.loads((out/f'min-dfa-{obj["width"]}.json').read_text())
    for side in ['lower','upper']:
        cert=obj['entropy_certificate'][side];U,D=cert['numerator'],cert['denominator']
        nodes=cert['nodes'];values=cert['vector'];assert U>D>0 and len(nodes)==len(values) and all(x>0 for x in values)
        val=dict(zip(nodes,values));assert len(val)==len(nodes)
        if side=='upper':assert set(nodes)==set(range(len(tr)))
        for i in nodes:
            a,b=tr[i];lhs=D**3*U**2*val.get(a,0)+D**5*val.get(b,0);rhs=U**5*val[i]
            assert lhs<=rhs if side=='upper' else lhs>=rhs
    count+=1
print('S16_INTEGER_CERTIFICATES_PASS',count)
