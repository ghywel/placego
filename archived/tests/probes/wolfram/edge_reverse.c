// edge_reverse: block exponents E_n of seed a (optionally with bit FLIP complemented) by the lifting rule, with the
// weight parity of wheel n-2 over the period 2^E_(n-1) printed per n (w2), for the reversal rule of CL650.
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
typedef unsigned __int128 u128;
int main(int argc,char**argv){ u128 a=strtoull(argv[1],0,0); int N=atoi(argv[2]); int flip=(argc>3)?atoi(argv[3]):-1;
  if(flip>=0) a^=((u128)1<<flip);
  uint64_t L=1; printf("seed=%s flip=%d E_n:",argv[1],flip);
  int E[200]; int w2[200];
  for(int n=1;n<=N;n++){ u128 x=a; int par=0,p2=0; for(uint64_t t=0;t<L;t++){ int b1=(n>=1)?(int)((x>>(n-1))&1):0; int b2=(n>=2)?(int)((x>>(n-2))&1):0; par^=(b1|b2); p2^=b2; x = x ^ ((x<<1)|(x<<2)); }
    w2[n]=p2; if(par) L<<=1; int e=0; uint64_t l=L; while(l>1){l>>=1;e++;} E[n]=e; printf(" %d",e); }
  printf("\n w2:"); for(int n=1;n<=N;n++) printf(" %d",w2[n]); printf("\n"); return 0; }
