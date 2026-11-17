// Newton (binomial-basis) supports of the right wheels of a seed under Phi (OR) or the AND map: c_m = XOR_{t subset m} R_j(t)
// over one least period 2^e (e <= EMAX); prints |S_j|, the ratio, and whether the all-ones index is in S_j against the weight parity.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
typedef unsigned __int128 u128;
#define EMAX 21
#define NT (1u<<(EMAX+1))
static uint8_t *bits[64];
int main(int argc,char**argv){ u128 a=strtoull(argv[1],0,0); int useand=(argc>2&&argv[2][0]=='A'); int JMAX=(argc>3)?atoi(argv[3]):60;
  for(int j=0;j<64;j++) bits[j]=calloc(NT/8,1);
  u128 x=a; for(uint32_t t=0;t<NT;t++){ for(int j=0;j<64;j++) if((x>>j)&1) bits[j][t>>3]|=1<<(t&7); u128 s1=x<<1,s2=x<<2; x^= useand?(s1&s2):(s1|s2); }
  uint8_t *f=malloc(1u<<EMAX);
  for(int j=0;j<=JMAX;j++){ int e=-1; for(int ee=0;ee<=EMAX;ee++){ uint32_t p=1u<<ee; int ok=1; for(uint32_t t=0;t+p<NT;t++) if(((bits[j][t>>3]>>(t&7))&1)!=((bits[j][(t+p)>>3]>>((t+p)&7))&1)){ok=0;break;} if(ok){e=ee;break;} }
    if(e<0){ printf("j=%d period above 2^%d\n",j,EMAX); continue; }
    uint32_t P=1u<<e; int w=0; for(uint32_t t=0;t<P;t++){ f[t]=(bits[j][t>>3]>>(t&7))&1; w+=f[t]; }
    for(int b=0;b<e;b++) for(uint32_t m=0;m<P;m++) if(m&(1u<<b)) f[m]^=f[m^(1u<<b)];
    uint32_t sz=0; for(uint32_t m=0;m<P;m++) sz+=f[m]; int top=f[P-1];
    printf("j=%d e=%d weight=%d omega=%d |S|=%u ratio=%.3f allones_in_S=%d %s\n",j,e,w,w&1,sz,P>1?(double)sz/P:(double)sz,top,(top==(w&1))?"dict-ok":"DICT-FAIL"); }
  return 0; }
