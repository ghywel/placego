// T(x) = x xor (2x|4x) on Z_2. Print e_d(x) = log2 of the T-period of x mod 2^d, d = 1..D, for odd x < X.
// Periods only double: Per_(d+1) is Per_d or 2 Per_d, because T is an isometry. Controls: see check_rate.py.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef uint64_t u;
static inline u T(u x){ return x ^ ((x<<1)|(x<<2)); }
int main(int c,char**v){
  int D=atoi(v[1]); u X=strtoull(v[2],0,10); int cap=atoi(v[3]);
  u M=(D>=64)?~0ULL:((1ULL<<D)-1);
  for(u x=1;x<X;x+=2){
    u per=1,y=T(x)&M; int e=0; printf("%llu",(unsigned long long)x);
    int d; for(d=1;d<=D;d++){
      if(((x^y)>>(d-1))&1){
        if(e>=cap){ break; }
        u z=y; for(u i=0;i<per;i++) z=T(z)&M;   // T^(2 per)(x)
        y=z; per<<=1; e++;
      }
      printf(" %d",e);
    }
    printf("\n");
  }
  return 0;
}
