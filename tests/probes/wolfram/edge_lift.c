// Block period exponents E_n of the right-edge code of a finite seed a under Phi(x)=x^((x<<1)|(x<<2)),
// by the Klimov-Shamir lifting rule (kit TFunctionCycles.lift_iff): the period of x mod 2^(n+1) is
// L_n or 2 L_n according to the parity of psi_n = x_{n-1} | x_{n-2} along one period of x mod 2^n.
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
typedef unsigned __int128 u128;
int main(int argc,char**argv){ u128 a=strtoull(argv[1],0,0); int N=atoi(argv[2]);
  uint64_t L=1; printf("seed=%s E_n:",argv[1]);
  for(int n=1;n<=N;n++){ // period mod 2^n is L; compute parity of psi_n over one period
    u128 x=a; int par=0; for(uint64_t t=0;t<L;t++){ int b1=(n>=1)?(int)((x>>(n-1))&1):0; int b2=(n>=2)?(int)((x>>(n-2))&1):0; par^=(b1|b2); x = x ^ ((x<<1)|(x<<2)); }
    if(par) L<<=1; int E=0; uint64_t l=L; while(l>1){l>>=1;E++;} printf(" %d",E); fflush(stdout); }
  printf("\n"); return 0; }
