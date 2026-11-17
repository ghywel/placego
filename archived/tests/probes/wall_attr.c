/* wall_attr.c (Local, L1529): the eventual letter words. For each row, the letters on ticks [T/2, T): least period if any, and its canonical rotation. Usage: ./wall_attr ROWS TICKS LOW SEED */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef unsigned long long u64;
#define MAXB 24000
static u64 s[2];
static inline u64 rotl(u64 x,int k){return (x<<k)|(x>>(64-k));}
static u64 rnd(void){u64 a=s[0],b=s[1],r=a+b;b^=a;s[0]=rotl(a,24)^b^(b<<16);s[1]=rotl(b,37);return r;}
static const unsigned char WA[11]={0,0,1,1,1,1,0,0,0,1,1}, WB[11]={0,1,0,1,1,1,0,0,0,1,1};
#define MAXC 4000
static char cls[MAXC][1600]; static long ccnt[MAXC]; static int cper[MAXC]; static int nc=0; static long nonper=0;
static void add(const char*w,int p){ /* canonical rotation */ static char best[1600],tmp[1600]; memcpy(best,w,p); best[p]=0; for(int r=1;r<p;r++){ memcpy(tmp,w+r,p-r); memcpy(tmp+p-r,w,r); tmp[p]=0; if(strcmp(tmp,best)<0) strcpy(best,tmp);} 
  for(int i=0;i<nc;i++) if(cper[i]==p&&!strcmp(cls[i],best)){ccnt[i]++;return;} if(nc<MAXC){strcpy(cls[nc],best);cper[nc]=p;ccnt[nc]=1;nc++;} }
int main(int c,char**v){ long rows=atol(v[1]); int ticks=atoi(v[2]), low=atoi(v[3]); s[0]=0x9E3779B97F4A7C15ULL^atol(v[4]); s[1]=0xBF58476D1CE4E5B9ULL; for(int i=0;i<20;i++)rnd();
  static unsigned char x[MAXB],z[MAXB]; static char seq[8192]; int n=low+3*ticks+40; if(n>=MAXB) return 1;
  for(long r=0;r<rows;r++){ x[0]=1; for(int j=1;j<low;j++) x[j]=rnd()&1; { int b=x[low-1]; for(int j=low;j<n;j++){b^=1;x[j]=b;} }
    int top=-1;
    for(int t=0;t<ticks;t++){ if(top<0){ int k=n-3; while(k>=1 && x[k]!=x[k+1]) k--; if(k>=10&&(!memcmp(x+k-9,WA,11)||!memcmp(x+k-9,WB,11))) top=k; } else top+=3;
      char ch='?'; if(top>=0){ if(!memcmp(x+top-9,WA,11)) ch='A'; else if(!memcmp(x+top-9,WB,11)) ch='B'; }
      seq[t]=ch;
      int p1=1,p2=0; z[0]=1; for(int j=1;j<n;j++){ int o=x[j]^(p1|p2); z[j]=o; p2=p1; p1=o; } memcpy(x,z,n); }
    int a=ticks/2, L=ticks-a, per=0; for(int p=1;p<=L/2&&p<1500;p++){ int ok=1; for(int i=a;i+p<ticks;i++) if(seq[i]!=seq[i+p]){ok=0;break;} if(ok){per=p;break;} }
    if(per) add(seq+a,per); else nonper++; }
  printf("rows %ld ticks %d: no period up to %d in the second half: %ld\n",rows,ticks,ticks/4,nonper);
  for(int i=0;i<nc;i++) printf("period %4d count %5ld  %.120s\n",cper[i],ccnt[i],cls[i]);
  return 0; }
