// Right-edge frame of rule 30: a(t+1) = a ^ ((a<<1) | (a<<2)) on the low 128 bits (a T-function:
// low bits never depend on high bits). At t = 2^k print J_k = number of white cells left of the
// edge cell (bit 0), i.e. the zero run starting at bit 1, and the next 8 cells. Kit: R_n has
// period 2^k iff row 2^k has n white cells left of its right edge (per_iff_gap).
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
typedef unsigned __int128 u128;
int main(int argc,char**argv){ int K = argc>1?atoi(argv[1]):30; u128 a=1; uint64_t t=0;
  for(int k=0;k<=K;k++){ uint64_t target=(uint64_t)1<<k; while(t<target){ a = a ^ ((a<<1)|(a<<2)); t++; }
    int J=0; for(int b=1;b<127;b++){ if((a>>b)&1) break; J++; }
    // tail cells after the gap
    char s[20]; for(int i=0;i<10;i++) s[i]=((a>>(J+1+i))&1)?'1':'0'; s[10]=0;
    printf("k=%2d  J_k=%3d  J/k=%.4f  edge+ : 1 0^%d %s\n",k,J,k?(double)J/k:0.0,J,s); fflush(stdout); }
  return 0; }
