// As rate.c, for a listed set of x on stdin. T-period exponents e_d(x), d = 1..D, stopping at the cap.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef uint64_t u;
static inline u T(u x){ return x ^ ((x<<1)|(x<<2)); }
int main(int c,char**v){
  int D=atoi(v[1]); int cap=atoi(v[2]); u M=(D>=64)?~0ULL:((1ULL<<D)-1); unsigned long long x0;
  while(scanf("%llu",&x0)==1){ u x=x0,per=1,y=T(x)&M; int e=0; printf("%llu",x0);
    for(int d=1;d<=D;d++){ if(((x^y)>>(d-1))&1){ if(e>=cap) break; u z=y; for(u i=0;i<per;i++) z=T(z)&M; y=z; per<<=1; e++; } printf(" %d",e); }
    printf("\n"); fflush(stdout); }
  return 0; }
