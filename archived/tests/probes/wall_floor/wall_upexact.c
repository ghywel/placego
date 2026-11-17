/* wall_upfloors.c (Local, L1538): every periodic floor word. A reset word at offset c with word v has every column above it fixed: C_1 = not v(t-1), C_2 = 1, C_3 = 0, C_4 = v, C_5 = 0, and C_n(t) = C_(n-3)(t+1) ^ (C_(n-4)(t+1) | C_(n-5)(t+1)), where C_n = Y_(c-n).
   For each primitive word v of period P (one per rotation), follow the columns up, for at most LIMIT steps, until they are alternating constants (rain). Reports the words that reach rain, the offset c of the floor, and the letters; also words whose time dependence dies into other constant columns. Usage: ./wall_upfloors PMIN PMAX LIMIT */
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64;
static int P; static u64 MASK;
static inline u64 rot(u64 w){ return ((w>>1)|(w<<(P-1)))&MASK; }
static inline u64 rotinv(u64 w){ return ((w<<1)|(w>>(P-1)))&MASK; }
int main(int c,char**a){ int P0=atoi(a[1]),P1=atoi(a[2]); long LIM=atol(a[3]);
  for(P=P0;P<=P1;P++){ MASK=(P==64)?~0ULL:((1ULL<<P)-1); long tested=0,rain=0,cons=0,big=0,cyc=0; long maxn=0,maxcyc=0,maxrho=0;
    for(u64 v=1;v<MASK;v++){ /* canonical: smallest rotation, primitive */ u64 r=v; int ok=1; for(int i=1;i<P;i++){ r=rot(r); if(r<v){ ok=0; break; } if(r==v){ ok=0; break; } } if(!ok) continue; tested++;
      u64 c1=rotinv(v)^MASK,c2=MASK,c3=0,c4=v,c5=0; long n=5; int alt=0; int construn=0; int done=0; u64 s1=c1,s2=c2,s3=c3,s4=c4,s5=c5; long power=1,lam=0; 
      while(n<LIM){ n++; u64 x=rot(c3^(c2|c1)); /* C_n from C_(n-3), C_(n-4), C_(n-5) with c5=C_(n-1), c4=C_(n-2), c3=C_(n-3), c2=C_(n-4), c1=C_(n-5) */ c1=c2; c2=c3; c3=c4; c4=c5; c5=x; int isconst=(x==0||x==MASK); if(isconst){ construn++; if(c4==(x^MASK)) alt++; else alt=1; } else { construn=0; alt=0; } if(alt>=10){ done=1; break; } if(construn>=40){ done=2; break; } lam++; if(c1==s1&&c2==s2&&c3==s3&&c4==s4&&c5==s5){ done=3; if(lam>maxcyc) maxcyc=lam; if(n>maxrho) maxrho=n; break; } if(lam==power){ s1=c1;s2=c2;s3=c3;s4=c4;s5=c5; power<<=1; lam=0; } }
      if(done==1){ rain++; long cc=n-9; /* C index of the first alternating column */ if(rain<=40){ printf("P=%d v=",P); for(int t=0;t<P;t++) putchar((v>>t)&1?'1':'0'); printf(" reaches rain, alternating from column %ld\n",cc); } if(n>maxn) maxn=n; } else if(done==2) cons++; else if(done==3) cyc++; else big++; }
    printf("P=%d: words %ld, to rain %ld, to other constants %ld, to another cycle %ld (longest cycle %ld, longest run %ld), undecided at %ld steps %ld\n",P,tested,rain,cons,cyc,maxcyc,maxrho,LIM,big); fflush(stdout); }
  return 0; }
