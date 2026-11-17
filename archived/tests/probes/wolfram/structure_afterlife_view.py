#!/usr/bin/env python3
"""Analyse retained GC2034 supports and render a static explanatory figure; no CA evolution."""
import itertools,json,sys
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
src=Path(sys.argv[1]);dest=Path(sys.argv[2]);dest.mkdir(parents=True,exist_ok=True)
r=json.loads(src.read_text());summary=[]
for c in r['cases']:
    q=c['levels'][8];support=q['support']
    for k in range(1,9):
        missing=[]
        for sites in itertools.combinations(range(8),k):
            seen={''.join(w[j] for j in sites) for w in support}
            for p in itertools.product('01',repeat=k):
                p=''.join(p)
                if p not in seen:missing.append({'sites':sites,'pattern':p})
        if missing:break
    first=next(q['t'] for q in c['levels'] if not q['known'])
    summary.append({'name':c['name'],'first_no_known':first,'t8_support':len(support),
                    'minimum_forbidden_arity':k,'example':missing[0]})
a,b=r['cases'][:2]
intersection={str(t):sorted(set(a['levels'][t]['support']) & set(b['levels'][t]['support'])) for t in (5,6,7,8)}
jsonout={'status':'retained-data analysis only','summary':summary,'triangle_intersections':intersection}
(dest/'support_analysis.json').write_text(json.dumps(jsonout,indent=2)+'\n')
W,H=1540,1220;im=Image.new('RGB',(W,H),'#f7f7f4');d=ImageDraw.Draw(im)
def font(size,bold=False):
    return ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial'+(' Bold' if bold else '')+'.ttf',size)
f=font(19);small=font(16);head=font(24,True)
d.text((35,24),'VISIBLE COLOURS END. JOINT CONSTRAINTS CAN CONTINUE.',font=font(31,True),fill='#142536')
d.text((35,72),'Exact Rule 30 continuations of six eight-cell fragments; every exterior is allowed.',font=f,fill='#283d50')
for x,col,txt in [(35,'#18202a','fixed 1'),(230,'#ffffff','fixed 0'),(425,'#a9dbe6','either colour')]:
    d.rectangle((x,110,x+22,132),fill=col,outline='#536678');d.text((x+32,109),txt,font=f,fill='#283d50')
d.text((665,109),'Blue means variable, not independent or equally likely.',font=f,fill='#283d50')
names=['Even white triangle','Odd white triangle','Rain / staircase','Period-three precursor','Black cap','Irregular control']
for idx,(c,summ) in enumerate(zip(r['cases'],summary)):
    ox=35+(idx%3)*505;oy=165+(idx//3)*400
    d.text((ox,oy),names[idx],font=head,fill='#142536')
    d.text((ox,oy+33),'Initial: '+c['word'],font=f,fill='#42556a')
    d.text((ox,oy+65),'t',font=small,fill='#536678');d.text((ox+350,oy+65),'allowed / box',font=small,fill='#536678')
    for q in c['levels']:
        t=q['t'];yy=oy+92+t*25
        d.text((ox,yy),str(t),font=small,fill='#536678')
        for j in range(8):
            xx=ox+28+(t+j)*19;v=q['known'].get(str(j))
            col='#a9dbe6' if v is None else '#18202a' if v else '#ffffff'
            d.rectangle((xx,yy,xx+17,yy+19),fill=col,outline='#8093a4')
        d.text((ox+350,yy),str(q['support_count'])+' / '+str(q['independent_box']),font=small,fill='#283d50')
        if idx in (0,1) and t==6:
            xx=ox+28+t*19;d.rectangle((xx-2,yy-2,xx+36,yy+21),outline='#b54045',width=3)
    d.text((ox,oy+330),'At t=8: smallest forbidden group = '+str(summ['minimum_forbidden_arity']),font=small,fill='#283d50')
    if idx==0:d.text((ox,oy+355),'Red pair: always opposite, neither fixed.',font=small,fill='#b54045')
    if idx==1:d.text((ox,oy+355),'Red pair: always equal, neither fixed.',font=small,fill='#b54045')
    if idx==4:d.text((ox,oy+355),'All four-cell projections allow all 16 patterns.',font=small,fill='#72549c')
d.line((35,980,1500,980),fill='#bac4cc',width=2)
d.text((35,1000),'A FIVE-CELL EXCLUSION HIDING AFTER THE BLACK CAP',font=head,fill='#72549c')
d.text((35,1040),'At t=8, cells x=8..12 cannot be 00010. Drop any one cell, and the remaining assignment is possible.',font=f,fill='#283d50')
d.text((35,1080),'Each row displays x=t..t+7. Outside this moving window is not drawn. Time runs downward.',font=f,fill='#283d50')
d.text((35,1115),'Allowed = exact joint possibilities. Box = possibilities suggested by fixed colours alone.',font=f,fill='#283d50')
d.text((35,1150),'These are conditioned finite patches, not frequencies or a universal claim about the single-seed picture.',font=f,fill='#283d50')
im.save(dest/'structure-afterlife.png')
print(json.dumps(summary))
