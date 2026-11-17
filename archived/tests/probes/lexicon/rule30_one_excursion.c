/* EX1: one complete zero-return excursion before known rooted pair (320,64).
 * RUN-ON: CPU, C standard library, one process. BUILD outside Git:
 * cc -O2 tests/probes/lexicon/rule30_one_excursion.c -o /tmp/placego-ex1
 * COMMAND: /tmp/placego-ex1
 * Fixed common period16, fixed target only. Stop after the first two zero rows
 * seen backwards, or 800000 inverse edges, or 2 CPU seconds. No cap extension.
 * EX-P1 blind: selected excursion's rise count exceeds ten lifted baselines(80).
 * EX-C1: every inverse step agrees with scalar per-bit inversion and literal
 * equation. Known absorption depth725146 would be a control only if reached;
 * this instrument normally stops earlier and does NOT reverify full rootedness.
 * EX-C2: overlap=returning-source-weight+2*rises, rises>=max(8,2*heavy).
 * EX-U: exclude the initial zero-to-c rise term, while retaining the terminal
 * nonzero-to-zero edge (zero contribution); report the excluded term separately.
 * Prior rootedness supplied by independently reviewed S117, not inferred here.
 * NOT RUN at preregistration. Output outside Git; caps => UNDECIDED.
 */
#include <stdio.h>
#include <stdint.h>
#include <time.h>
#include <assert.h>
static unsigned weight(uint16_t x){return __builtin_popcount((unsigned)x);}
static uint16_t shift(uint16_t x){return (x>>1)|(x<<15);}
static uint16_t scalar(uint16_t a,uint16_t b){
 uint16_t x=0;
 for(int i=0;i<16;i++){
  unsigned z=((b>>((i+1)&15))&1)^(((a>>i)&1)|((b>>i)&1));
  x|=(uint16_t)(z<<i);
 }
 return x;
}
int main(void){
 clock_t t0=clock();uint16_t a=320,b=64;int active=0;
 unsigned first=0,return_weight=0,heavy=0;
 uint64_t rises=0,overlap=0,excluded=0;
 for(unsigned k=0;k<=800000;k++){
  if((double)(clock()-t0)/CLOCKS_PER_SEC>2 || k==800000){
   printf("UNDECIDED cap steps=%u\n",k);return 0;
  }
  if(b==0){
   if(active){
    assert(overlap==return_weight+2*rises);
    assert(rises>=8 && rises>=2*heavy);
    printf("COMPLETE backward_start=%u backward_end=%u length=%u return_weight=%u rises=%llu overlap=%llu heavy=%u excluded_start_rises=%llu prediction=%s cpu=%.6f\n",
     first,k,k-first,return_weight,(unsigned long long)rises,(unsigned long long)overlap,heavy,
     (unsigned long long)excluded,rises>80?"HELD":"REFUTED",(double)(clock()-t0)/CLOCKS_PER_SEC);
    return 0;
   }
   active=1;first=k;return_weight=weight(a);
   assert(a!=0 && a!=65535);
  }
  if(active){
   unsigned rr=weight(shift(b)&(uint16_t)~(a|b));
   if(a){rises+=rr;overlap+=weight(a&b);if(weight(b)==1 && weight(a)>3)heavy++;}
   else excluded+=rr;
  }
  uint16_t x=shift(b)^(a|b);
  assert(x==scalar(a,b));
  for(int i=0;i<16;i++)assert(((b>>((i+1)&15))&1)==(((x>>i)&1)^(((a>>i)&1)|((b>>i)&1))));
  b=a;a=x;
 }
 return 1;
}
