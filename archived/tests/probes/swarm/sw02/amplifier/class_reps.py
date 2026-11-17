# Least row of each class at exact width W, by agreement at tick T. Prints one class per line: least row, members count.
import sys
def F(y): return (y>>1)^(y|(y<<1))
W=int(sys.argv[1]); T=int(sys.argv[2])
cur={y:y for y in range(1<<(W-1),1<<W)}; cnt={y:1 for y in cur}
for t in range(T):
    nxt={};nc={}
    for y,m in cur.items():
        z=F(y)
        if z in nxt: nxt[z]=min(nxt[z],m); nc[z]+=cnt[y]
        else: nxt[z]=m; nc[z]=cnt[y]
    cur,cnt=nxt,nc
for z,m in sorted(cur.items(),key=lambda p:p[1]): print(m,cnt[z])
