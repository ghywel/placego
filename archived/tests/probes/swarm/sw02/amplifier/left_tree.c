// Sideways left-side tree. A branch holds temporal words of two adjacent wheels, period P <= 64.
// Recurrence: D[j+2](t+1) = D[j](t) xor (D[j+1](t) | D[j+2](t)). Black parent: child unique. White parent: x' = a xor x;
// even parity of a over P gives two children (fork); odd parity gives one child of period 2P (doubling).
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef uint64_t u;
typedef struct { int P; u a,b; int id; } B;
static inline int bit(u w,int t){ return (w>>t)&1; }
static inline u mask(int P){ return P==64?~0ULL:((1ULL<<P)-1); }
static u child_black(u a,u b,int P){ int r=0; while(!bit(b,r)) r++; u x=0; int v=bit(a,r)^1; int t=(r+1)%P; x|=(u)v<<t;
  for(int i=1;i<P;i++){ int nv=bit(a,t)^(bit(b,t)|v); t=(t+1)%P; v=nv; x=(x&~(1ULL<<t))|((u)v<<t);} return x; }
static u child_white(u a,int P,int x0){ u x=0; int v=x0; x|=(u)v; for(int t=0;t<P-1;t++){ v^=bit(a,t); x|=(u)v<<(t+1);} return x; }
int main(int c,char**v){ long Kmax=atol(v[1]); int cap=c>2?atoi(v[2]):4096; static B br[1<<16]; int n=1,nid=1; br[0]=(B){1,1,1,0};
  // wheels 0 and 1 are black; b holds wheel j+1. loop computes wheel j+2.
  long lastPi=-1; int stopped=0;
  for(long j=0;j+2<=Kmax;j++){ int m=n; long w=j+1;
    for(int i=0;i<m;i++){ B*x=&br[i]; if(x->P==0) continue; u a=x->a,b=x->b; int P=x->P;
      if(b){ u nx=child_black(a,b,P); x->a=b; x->b=nx; }
      else { int par=__builtin_popcountll(a&mask(P))&1;
        if(!par){ u c0=child_white(a,P,0), c1=c0^mask(P); if(n>=cap){ printf("CAP at wheel %ld\n",w); return 0; }
          printf("wheel %ld white on branch %d P %d: FORK -> %d, %d\n",w,x->id,P,x->id,nid); fflush(stdout);
          br[n]=(B){P,b,c1,nid++}; n++; x->a=b; x->b=c0; }
        else { if(P==64){ printf("wheel %ld white on branch %d P 64: DOUBLE to 128, branch stopped\n",w,x->id); x->P=0; stopped++; continue; }
          int Q=2*P; u a2=a|(a<<P), b2=b|(b<<P); u xx=child_white(a2,Q,0); printf("wheel %ld white on branch %d P %d: DOUBLE -> %d\n",w,x->id,P,Q); fflush(stdout);
          x->P=Q; x->a=b2; x->b=xx; } } }
    long Pi=0; for(int i=0;i<n;i++) Pi+=br[i].P; if(Pi!=lastPi){ printf("Pi(%ld) = %ld, cycles %d\n",j+3,Pi,n-stopped); lastPi=Pi; }
  }
  return 0; }
