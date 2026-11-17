# Independent control of rate.c: brute orbit size of x mod 2^d by direct iteration, small d.
import subprocess,sys
exe=sys.argv[1]
def T(x,m): return (x^((x<<1)|(x<<2)))&m
out=subprocess.run([exe,'20','64','24'],capture_output=True,text=True).stdout.strip().split('\n')
bad=0
for line in out:
    p=list(map(int,line.split())); x=p[0]; es=p[1:]
    for d in range(1,len(es)+1):
        m=(1<<d)-1; y=T(x&m,m); n=1
        while y!=(x&m): y=T(y,m); n+=1
        if n!=1<<es[d-1]: bad+=1; print('MISMATCH',x,d,n,es[d-1])
print('rate.c control: rows',len(out),'mismatches',bad)
