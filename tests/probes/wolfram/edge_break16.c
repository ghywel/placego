// edge_break: block exponents of seed a under the edge map Phi(x) = x ^ ((x<<1)|(x<<2)) with breaks (CL652):
//  f<k> reverse wheel k (flip seed bit k); c<k> clamp wheel k to 0 for ever; a<k> / x<k> wheel k flips on AND / XOR of its
//  two suppliers; A / X: AND / XOR at every wheel. Generic lifting: period mod 2^(n+1) is L (bit n returns after L steps of
//  the lower bits' period) or 2L. Prints E_n, and per n the parities over L of bit n-1 (w1), bit n-2 (w2), their AND (ov).
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned __int128 u128;
static u128 clampmask=0, andmask=0, xormask=0; static int allA=0, allX=0, gtt=-1;
static u128 step(u128 x){ u128 s1=x<<1, s2=x<<2; u128 g;
  if(gtt>=0){ g=0; if(gtt&1) g|=~(s1|s2); if(gtt&2) g|=(~s1)&s2; if(gtt&4) g|=s1&(~s2); if(gtt&8) g|=s1&s2; } else if(allA) g = s1&s2; else if(allX) g = s1^s2; else g = s1|s2;
  g = (g & ~(andmask|xormask)) | ((s1&s2)&andmask) | ((s1^s2)&xormask);
  x ^= g; x &= ~clampmask; return x; }
int main(int argc,char**argv){ u128 a=strtoull(argv[1],0,0); int N=atoi(argv[2]);
  for(int i=3;i<argc;i++){ char c=argv[i][0]; int k=atoi(argv[i]+1);
    if(c=='f') a^=((u128)1<<k); else if(c=='c') clampmask|=((u128)1<<k); else if(c=='a') andmask|=((u128)1<<k);
    else if(c=='x') xormask|=((u128)1<<k); else if(c=='A') allA=1; else if(c=='X') allX=1; else if(c=='g') gtt=k; }
  a &= ~clampmask;
  uint64_t L=1; int E[200],w1[200],w2[200],ov[200];
  { u128 x0=a; u128 x1=step(x0); if(((x0^x1)&1)) L=2; } // bit 0: period 1 or 2 (CL662 correction: gates with g(0,0)=1 toggle it)
  printf("seed=%s mods:",argv[1]); for(int i=3;i<argc;i++) printf(" %s",argv[i]); printf(" E_n:");
  for(int n=1;n<=N;n++){ u128 x=a; int p1=0,p2=0,po=0; for(uint64_t t=0;t<L;t++){ int b1=(int)((x>>(n-1))&1); int b2=(n>=2)?(int)((x>>(n-2))&1):0; p1^=b1; p2^=b2; po^=(b1&b2); x=step(x); }
    int ret = (int)(((x^a)>>n)&1)==0; w1[n]=p1; w2[n]=p2; ov[n]=po; if(!ret) L<<=1; int e=0; uint64_t l=L; while(l>1){l>>=1;e++;} E[n]=e; printf(" %d",e); }
  printf("\n w1:"); for(int n=1;n<=N;n++) printf(" %d",w1[n]);
  printf("\n w2:"); for(int n=1;n<=N;n++) printf(" %d",w2[n]);
  printf("\n ov:"); for(int n=1;n<=N;n++) printf(" %d",ov[n]); printf("\n"); return 0; }
