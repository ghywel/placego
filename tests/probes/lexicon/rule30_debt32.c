/* RD32: finite same-prefix reference debt at slope5/2, GPT preregistration.
 * Source: construction/rotation pattern from Local rule30_tm6.c; that audited
 * constructor is shared in method, not an independent ancestry implementation.
 * New: inherited absolute clock, prefix minimum, doubled debt and witnesses.
 * BUILD: cc -O2 -o /tmp/rule30_debt32 tests/probes/lexicon/rule30_debt32.c
 * RUN: /tmp/rule30_debt32 (transcript outside Git); --smoke is preflight only.
 * Fixed frontier2^20, CPU cap60s, walk cap32, transition cap20million.
 * P1 blind uncertain: maximum doubled debt<=256 (ordinary debt128).
 * P2 blind uncertain: some whole-prefix debt exceeds RD16's maximum60.
 * C0 scalar clock scans and literal child tests on deterministic formal pairs.
 * C1 exact16 N5 entries, debts and GC321 endpoint h reproduce;15 branches and20 doublings.
 * C2 literal equation AND independent scalar reset delay on EVERY transition.
 * CF resetting phase is invalid: pulse bit31 delay1 atT31, delay32 atT0.
 * U terminal zero edges keep D, map h to max(h-5,0), including inherited minima.
 * Known no period32 zero below frontier (TM6); encountering one fails C1.
 * Only full frontier, all16 walks, all controls, no cap certifies the result.
 * No period64 search, change to TM6b, asymptotic inference or prize claim.
 * PRE-FLIGHT 2026-10-07: cc -O2 -Wall -Wextra succeeds without diagnostics;
 * --smoke C0/CF PASS. Full frontier run NOT RUN at preregistration.
 * OUTCOME 2026-10-07: one Intel CPU0.544s run after ce52a59 publication.
 * Frontier1048576;16walks,15branches,20doublings,11600256transitions; no cap.
 * C0/C1/C2/CF/U PASS. P1 HELD (maximum debt60); P2 REFUTED (no debt>60).
 * Largest endpoint h10; finite all-phase/birth bound91 via G164.
 * New witness debts: natural87867 rises to32.5,196189 to40.5,667052 to45.
 * Other thirteen match RD16; maximum60 remains inherited from period16.
 * Single-party finite statistic, independent review pending; no later bound.
 */
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <assert.h>
#define END (1LL<<20)
#define MAXW 32
static uint32_t rot(uint32_t x,int k){k&=31;return k?(x>>k)|(x<<(32-k)):x;}
static uint32_t child(uint32_t a,uint32_t b){
 int t0=__builtin_ctz(b),t=(t0+1)&31;uint32_t c=0,bit=((a>>t0)&1)^1;
 for(int i=0;i<32;i++){c|=bit<<t;bit=((a>>t)&1)^(((b>>t)|bit)&1);t=(t+1)&31;}return c;
}
static int isrot(uint32_t a,uint32_t b){for(int k=1;k<32;k++)if(rot(a,k)==b)return 1;return 0;}
static int period(uint32_t a){for(int p=1;p<32;p*=2)if(rot(a,p)==a)return p;return 32;}
static int delay(uint32_t y,int64_t T){return y?__builtin_ctz(rot(y,T&31))+1:0;}
static int scalar(uint32_t y,int64_t T){if(!y)return 0;for(int i=0;i<32;i++)if((y>>((T+i)&31))&1)return i+1;return -1;}
typedef struct{uint32_t x,y;int64_t d,T,m,D,md,mT,wa,wb,wt,entry;} Walk;
static Walk walks[MAXW];
static const int64_t ns[16]={87867,183184,196189,229338,253537,271596,291257,527724,551910,555813,575211,634886,645655,667052,770532,894235};
static const int64_t ds[16]={57,80,79,87,79,79,73,79,79,79,85,80,79,85,120,120};
static const int64_t hs[16]={0,0,0,0,0,0,1,0,0,0,0,10,0,0,0,0};
static int check_entry(int64_t n,int64_t D){for(int i=0;i<16;i++)if(ns[i]==n)return ds[i]==D?i:-1;return -1;}
int main(int argc,char**argv){
 uint32_t seed=7;
 for(int j=0;j<1000;j++){
  seed=1664525u*seed+1013904223u;uint32_t a=seed;
  seed=1664525u*seed+1013904223u;uint32_t b=seed?seed:1u,c=child(a,b);
  assert(rot(c,1)==(a^(b|c)));
  for(int t=0;t<64;t++)assert(delay(b,t)==scalar(b,t));
 }
 assert(delay(1u<<31,31)==1&&delay(1u<<31,0)==32);
 assert((7-5)>0); /* zero edge after adjusted+7 leaves the old minimum unchanged */
 puts("C0 CF preflight PASS");
 if(argc>1){assert(!strcmp(argv[1],"--smoke"));return 0;}
 clock_t start=clock();int nw=1,branches=0,doublings=0;uint32_t seen=0;
 int64_t steps=0,maxD=0;walks[0]=(Walk){.y=0xffffffffu};
 for(int i=0;i<nw;i++){
  Walk w=walks[i];
  while(w.d<END){
   if(++steps>20000000||((steps&4095)==0&&(double)(clock()-start)/CLOCKS_PER_SEC>60)){
    puts("CAP partial: no frontier certificate");return 2;
   }
   int dt=delay(w.y,w.T);assert(dt==scalar(w.y,w.T));
   int64_t oldD=w.D,oldh=2*w.T-5*w.d-w.m;
   uint32_t c=0;int fork=0,doubled=0;
   if(w.y)c=child(w.x,w.y);
   else{
    assert(!w.entry); /* no period32 zero allowed in this known finite domain */
    assert(!(__builtin_popcount(w.x)&1));
    uint32_t bit=0;for(int t=0;t<32;t++){c|=bit<<t;bit^=(w.x>>t)&1;}
    if(isrot(c,~c)){doublings++;doubled=1;}else{branches++;fork=1;}
    assert(rot(~c,1)==(w.x^(~c)));
   }
   assert(rot(c,1)==(w.x^(w.y|c)));
   w.T+=dt;w.d++;int64_t z=2*w.T-5*w.d;
   if(z-w.m>w.D){w.D=z-w.m;w.wa=w.md;w.wb=w.d;w.wt=w.T-w.mT;}
   if(z<w.m){w.m=z;w.md=w.d;w.mT=w.T;}
   if(!w.y){assert(dt==0&&w.D==oldD);assert(z-w.m==(oldh>5?oldh-5:0));}
   if(doubled&&period(c)==32){
    assert(period(w.x)==16);int k=check_entry(w.d,w.D);assert(k>=0&&!(seen&(1u<<k)));
    assert(z-w.m==hs[k]);seen|=1u<<k;w.entry=w.d;
   }
   if(fork){assert(nw<MAXW);Walk other=w;other.x=0;other.y=~c;walks[nw++]=other;}
   w.x=w.y;w.y=c;
  }
  assert(w.entry&&w.d==END);assert(w.D==2*w.wt-5*(w.wb-w.wa));
  walks[i]=w;if(w.D>maxD)maxD=w.D;
  printf("PREFIX N5=%lld debt2=%lld h2=%lld witness=%lld,%lld elapsed=%lld clock=%lld\n",
   (long long)w.entry,(long long)w.D,(long long)(2*w.T-5*w.d-w.m),(long long)w.wa,(long long)w.wb,(long long)w.wt,(long long)w.T);
 }
 assert(nw==16&&seen==65535u&&branches==15&&doublings==20);
 printf("CERTIFIED frontier=%lld walks=%d branches=%d doublings=%d steps=%lld maxDebt2=%lld P1=%d P2=%d cpu=%.3f C1 C2 U PASS\n",
  END,nw,branches,doublings,(long long)steps,(long long)maxD,maxD<=256,maxD>120,(double)(clock()-start)/CLOCKS_PER_SEC);
 return 0;
}
