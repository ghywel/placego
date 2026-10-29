// Right diagonals R_j(t) = bit j of Phi^t(1), Phi(x)=x^((x<<1)|(x<<2)), stored for t < 2^N (low 64 bits per row).
// For each j<=JMAX: least period p_j=2^e_j of R_j (checked by halving from 2^N), d_j=e_j-e_(j-1),
// omega_j = weight parity of R_j over one least period, g_j = R_(j-1)|R_(j-2): weight parity over P=p_(j-1),
// even-time black count parity of g_j over P, and parity of weight of R_(j-1)&R_(j-2) over P.
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
int main(int argc,char**argv){ int N=atoi(argv[1]); int JMAX=atoi(argv[2]); uint64_t T=(uint64_t)1<<N;
  uint64_t *row=malloc(T*8); __uint128_t a=1; for(uint64_t t=0;t<T;t++){ row[t]=(uint64_t)a; a=a^((a<<1)|(a<<2)); }
  int e[64]; uint64_t p[64];
  for(int j=0;j<=JMAX;j++){ // least period of bit j: largest halving that still works
    uint64_t P=T; while(P>1){ uint64_t h=P/2; int ok=1; for(uint64_t t=0;t<T-h;t++){ if(((row[t]>>j)&1)!=((row[t+h]>>j)&1)){ok=0;break;} } if(ok) P=h; else break; }
    p[j]=P; int ee=0; uint64_t q=P; while(q>1){q>>=1;ee++;} e[j]=ee; }
  printf("j e_j d_j omega_j wg_par evenpar andpar caseA_pred caseB_pred\n");
  for(int j=0;j<=JMAX;j++){
    int d = j? e[j]-e[j-1] : 0;
    uint64_t w=0; for(uint64_t t=0;t<p[j];t++) w+=(row[t]>>j)&1; int omega=w&1;
    int wg=-1,ev=-1,an=-1,cA=-1,cB=-1;
    if(j>=3){ uint64_t P=p[j-1]; uint64_t wgs=0,evs=0,ans=0;
      for(uint64_t t=0;t<P;t++){ int a1=(row[t]>>(j-1))&1, a2=(row[t]>>(j-2))&1; int g=a1|a2; wgs+=g; if(!(t&1)) evs+=g; ans+=a1&a2; }
      wg=wgs&1; ev=evs&1; an=ans&1;
      int dprev=e[j-1]-e[j-2];
      if(dprev==1){ // case A: d_j = parity of w(R_(j-2)) over its least period
        uint64_t w2=0; for(uint64_t t=0;t<p[j-2];t++) w2+=(row[t]>>(j-2))&1; cA=w2&1; }
      else { // case B: d_j = omega_(j-1)+omega_(j-2)+andpar
        uint64_t w1=0,w2=0; for(uint64_t t=0;t<p[j-1];t++) w1+=(row[t]>>(j-1))&1; for(uint64_t t=0;t<p[j-2];t++) w2+=(row[t]>>(j-2))&1;
        cB=((w1&1)+(w2&1)+an)&1; }
    }
    printf("%d %d %d %d %d %d %d %d %d\n",j,e[j],d,omega,wg,ev,an,cA,cB); }
  return 0; }
