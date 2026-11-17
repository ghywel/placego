import numpy as np, re
rows=[]
for line in open('sweep.log'):
    m=re.match(r'n=(\d+) m=\d+ f=(\d+)',line)
    if m: rows.append((int(m.group(1)),int(m.group(2))))
n=np.array([r[0] for r in rows],float); f=np.array([r[1] for r in rows],float)
g=f/n; W=(n+f)/n; l=np.log(n); ll=np.log(l)
forms={'sqrt(log n)':np.sqrt(l),'sqrt(log n/loglog n)':np.sqrt(l/ll)}
for name,h in forms.items():
    for tgt,lab in [(g,'f/n'),(W,'(n+f)/n')]:
        A=np.vstack([np.ones_like(h),h]).T
        coef,res,_,_=np.linalg.lstsq(A,tgt,rcond=None)
        pred=A@coef; rms=np.sqrt(np.mean((pred-tgt)**2))
        # pure proportional fit
        c=np.sum(tgt*h)/np.sum(h*h); rms0=np.sqrt(np.mean((c*h-tgt)**2))
        print('%-22s %-8s affine a=%+.4f b=%.4f rms=%.5f | proportional c=%.4f rms=%.5f'%(name,lab,coef[0],coef[1],rms,c,rms0))
print()
print('n, f/n, f/(n sqrt(log n)), f/(n sqrt(log n/loglog n)), (2/sqrt e)sqrt(l/ll), 1.7398 sqrt(l)')
for i in range(len(n)):
    print('%9d %.4f %.4f %.4f   %.3f %.3f'%(n[i],g[i],g[i]/np.sqrt(l[i]),g[i]/np.sqrt(l[i]/ll[i]),2/np.sqrt(np.e)*np.sqrt(l[i]/ll[i]),1.7398*np.sqrt(l[i])))
