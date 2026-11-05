/* wall_lang.c (Local, L1528): the letters of the settled wall. Random anchored rows with a rain tail, walked backward by the inverse map; once the top window
   is A or B the letter is recorded at every tick. Counts every factor up to length LMAX. Usage: ./wall_lang ROWS TICKS LOW SEED */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef unsigned long long u64;
#define MAXB 4096
#define LMAX 22
static u64 s[2];
static inline u64 rotl(u64 x,int k){return (x<<k)|(x>>(64-k));}
static u64 rnd(void){u64 a=s[0],b=s[1],r=a+b;b^=a;s[0]=rotl(a,24)^b^(b<<16);s[1]=rotl(b,37);return r;}
static uint32_t *cnt[LMAX+1];
static const unsigned char WA[11]={0,0,1,1,1,1,0,0,0,1,1}, WB[11]={0,1,0,1,1,1,0,0,0,1,1};
int main(int c,char**v){ long rows=atol(v[1]); int ticks=atoi(v[2]), low=atoi(v[3]); s[0]=0x9E3779B97F4A7C15ULL^atol(v[4]); s[1]=0xBF58476D1CE4E5B9ULL; for(int i=0;i<20;i++)rnd();
  for(int L=1;L<=LMAX;L++) cnt[L]=calloc(1u<<L,4);
  static unsigned char x[MAXB],z[MAXB]; long settled=0, letters=0, late=0; long entry_hist[80]={0};
  for(long r=0;r<rows;r++){ int n=low+3*ticks+40; if(n>=MAXB){puts("too long");return 1;}
    x[0]=1; for(int j=1;j<low;j++) x[j]=rnd()&1; { int b=x[low-1]; for(int j=low;j<n;j++){b^=1;x[j]=b;} }
    unsigned w=0; int len=0; int entry=-1; 
    for(int t=0;t<ticks;t++){ /* find the top wall */
      int top=n-3; while(top>=1 && x[top]!=x[top+1]) top--;
      int letter=-1;
      if(top>=10){ if(!memcmp(x+top-9,WA,11)) letter=0; else if(!memcmp(x+top-9,WB,11)) letter=1; }
      if(letter>=0){ if(entry<0){entry=t; settled++; if(t<80)entry_hist[t]++;} w=((w<<1)|letter); if(len<LMAX) len++; letters++;
        for(int L=1;L<=len;L++) cnt[L][w&((1u<<L)-1)]++; }
      else { if(entry>=0) late++; len=0; w=0; }
      /* inverse */
      int p1=1,p2=0; z[0]=1; for(int j=1;j<n;j++){ int o=x[j]^(p1|p2); z[j]=o; p2=p1; p1=o; } memcpy(x,z,n);
    } }
  printf("rows %ld settled %ld letters %ld letters lost after settling %ld\n",rows,settled,letters,late);
  double fib[LMAX+3]; fib[1]=1;fib[2]=1; for(int i=3;i<LMAX+3;i++) fib[i]=fib[i-1]+fib[i-2];
  for(int L=1;L<=LMAX;L++){ long seen=0; double H=0,tot=0; for(unsigned i=0;i<(1u<<L);i++) if(cnt[L][i]){seen++;tot+=cnt[L][i];} 
    long bb=0; for(unsigned i=0;i<(1u<<L);i++) if(cnt[L][i] && (i&(i>>1))) bb++;
    unsigned mn=~0u; for(unsigned i=0;i<(1u<<L);i++) if(cnt[L][i]&&cnt[L][i]<mn) mn=cnt[L][i];
    printf("L=%2d words seen %7ld of %7.0f avoiding BB; with BB %ld; rarest count %u\n",L,seen,fib[L+2],bb,mn); }
  /* the words missing among those avoiding BB and AAA */
  for(int L=3;L<=LMAX;L++){ long ok=0,seen=0; unsigned ex=0; int shown=0; for(unsigned i=0;i<(1u<<L);i++){ if(i&(i>>1)) continue; unsigned nz=(~i)&((1u<<L)-1); if(nz&(nz>>1)&(nz>>2)) continue; ok++; if(cnt[L][i]) seen++; else if(!shown){ex=i;shown=1;} }
    printf("L=%2d no BB, no AAA: %6ld, seen %6ld",L,ok,seen); if(shown){printf("; first missing "); for(int b=L-1;b>=0;b--) putchar((ex>>b)&1?'B':'A');} printf("\n"); }
  /* conditional frequencies; bit 0 is the newest letter */
  double a1=cnt[1][0],b1=cnt[1][1];
  printf("P(B)=%.5f\n",b1/(a1+b1));
  printf("P(B|A)=%.5f P(A|B)=%.5f\n",(double)cnt[2][1]/(cnt[2][0]+cnt[2][1]),(double)cnt[2][2]/(cnt[2][2]+cnt[2][3]));
  /* contexts of length 2 and 3 */
  for(unsigned ctx=0;ctx<8;ctx++){ unsigned n0=cnt[4][ctx<<1],n1=cnt[4][(ctx<<1)|1]; if(n0+n1==0) continue; printf("ctx %c%c%c: P(B)=%.5f (n=%u)\n",ctx&4?'B':'A',ctx&2?'B':'A',ctx&1?'B':'A',(double)n1/(n0+n1),n0+n1); }
  return 0; }
