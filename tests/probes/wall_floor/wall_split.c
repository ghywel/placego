/* wall_split.c (Local, L1540): multilevel splitting for the rate at which the window chain enters a closed set. Chain: top W cells, independent fair lower states. Importance I(t): the smallest, over the last six ticks, of the deepest agreement with any phase word of the set (consensus cells only).
   Phase 0: a direct run for SECS seconds counts first entries to each level from below BASE, and stores states at the first level. Then for each level: N runs from stored states, with fresh randomness, each until it reaches the next level or falls below BASE.
   Usage: ./wall_split W SECS N SEED SETFILE CONSENSUSFILE LEVELS(comma separated). */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
typedef unsigned char u8; typedef unsigned long long u64;
static u8 TOUT[4][256], TST[4][256];
static void mk(void){ for(int s=0;s<4;s++) for(int b=0;b<256;b++){ int p1=s>>1,p2=s&1,o=0; for(int i=0;i<8;i++){ int c=(b>>i)&1; int q=c^(p1|p2); o|=q<<i; p2=p1; p1=q; } TOUT[s][b]=o; TST[s][b]=(p1<<1)|p2; } }
static u64 rs; static inline u64 rnd(void){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
#define MAXW 512
#define NWD (MAXW/64+2)
#define BASE 36
typedef struct { u64 A[NWD]; int rb[6]; int ph; } st;
static int W,nw,nb,nref,nset,K; static u64 refv[16][NWD],refm[16][NWD],setv[64][NWD],topmask[NWD];
static inline int tick(st*x){ u64 B[NWD]; u8*in=(u8*)x->A; u8*o=(u8*)B; x->A[nw]=(u64)2; int s=rnd()>>62; for(int i=0;i<nb+1;i++){ o[i]=TOUT[s][in[i]]; s=TST[s][in[i]]; } for(int i=0;i<nw;i++) x->A[i]=(B[i]>>3)|(B[i+1]<<61);
  int best=0; for(int r=0;r<nref;r++){ int k=W; for(int wd=nw-1;wd>=0;wd--){ u64 d=(x->A[wd]^refv[r][wd])&refm[r][wd]; if(d){ k=W-1-(wd*64+63-__builtin_clzll(d)); break; } } if(k>best) best=k; }
  x->rb[x->ph]=best; x->ph=(x->ph+1)%6; int mn=best; for(int i=0;i<6;i++) if(x->rb[i]<mn) mn=x->rb[i]; return mn; }
static int captured(const st*x){ for(int r=0;r<nset;r++){ int eq=1; for(int wd=0;wd<nw;wd++) if((x->A[wd]^setv[r][wd])&topmask[wd]){ eq=0; break; } if(eq) return 1; } return 0; }
static void fresh(st*x){ memset(x,0,sizeof *x); for(int i=0;i<nw;i++) x->A[i]=rnd(); u64 top=0x63C; int base=W-11; for(int i=0;i<11;i++){ int j=base+i; u64 m=1ULL<<(j&63); if((top>>i)&1) x->A[j>>6]|=m; else x->A[j>>6]&=~m; } }
int main(int c,char**a){ mk(); W=atoi(a[1]); long secs=atol(a[2]); long N=atol(a[3]); rs=strtoull(a[4],0,10)*2654435761ULL+88172645463325252ULL; for(int i=0;i<20;i++) rnd(); nb=W/8; nw=W/64; char line[700]; FILE*f=fopen(a[6],"r"); while(fgets(line,700,f)){ int n=strcspn(line,"\n"); line[n]=0; if(!n) continue; for(int k=0;k<n;k++){ char ch=line[n-1-k]; int j=W-1-k; if(ch=='?') continue; refm[nref][j>>6]|=1ULL<<(j&63); if(ch=='#') refv[nref][j>>6]|=1ULL<<(j&63); } nref++; } fclose(f); f=fopen(a[5],"r"); while(fgets(line,700,f)){ int n=strcspn(line,"\n"); line[n]=0; if(!n) continue; K=n; for(int k=0;k<n;k++){ int j=W-1-k; if(line[n-1-k]=='#') setv[nset][j>>6]|=1ULL<<(j&63); } nset++; } fclose(f); for(int j=W-K;j<W;j++) topmask[j>>6]|=1ULL<<(j&63);
  int D[64],nl=0; { char*p=strtok(a[7],","); while(p){ D[nl++]=atoi(p); p=strtok(0,","); } }
  long CAP=N*4; st*pool=malloc(sizeof(st)*CAP),*next=malloc(sizeof(st)*CAP); long npool=0; long cnt[64]={0}; long ticks=0; time_t t0=time(0); st x; fresh(&x); int armed=0; int top=-1; long seen1=0; long steps=0;
  for(;;){ int I=tick(&x); ticks++; steps++; if(steps<400) continue; if(I<BASE){ armed=1; top=-1; } else if(armed){ for(int i=top+1;i<nl&&I>=D[i];i++){ cnt[i]++; top=i; if(i==0){ seen1++; if(npool<CAP) pool[npool++]=x; else { long j=rnd()%seen1; if(j<CAP) pool[j]=x; } } } } if((ticks&0xFFFFF)==0&&time(0)-t0>=secs) break; if(steps>3000000&&(ticks&0xFFFFF)==0){ fresh(&x); steps=0; armed=0; top=-1; } }
  printf("direct: ticks %ld; first entries per level:",ticks); for(int i=0;i<nl;i++) printf(" %d:%ld",D[i],cnt[i]); puts(""); fflush(stdout);
  double rate=(double)cnt[0]/ticks; printf("level %d rate %.3e per tick\n",D[0],rate);
  for(int i=0;i<=nl-1;i++){ long succ=0,fail=0,lost=0; long nn=0; long seen=0; long tk=0; int last=(i==nl-1); if(npool==0){ printf("level %d: no states\n",D[i]); break; } for(long j=0;j<N;j++){ st y=pool[rnd()%npool]; long st_=0; for(;;){ int I=tick(&y); st_++; if(!last&&I>=D[i+1]){ succ++; seen++; if(nn<CAP) next[nn++]=y; else { long q=rnd()%seen; if(q<CAP) next[q]=y; } break; } if(last&&I>=K-16&&captured(&y)){ succ++; break; } if(I<BASE){ fail++; break; } if(st_>2000000){ lost++; break; } } tk+=st_; } double p=(double)succ/N; rate*=p; printf("level %d to %s: runs %ld reached %ld fell %ld lost %ld p %.4f mean ticks %.0f rate now %.3e\n",D[i],last?"capture":"next",N,succ,fail,lost,p,(double)tk/N,rate); fflush(stdout); if(!succ) break; st*t=pool; pool=next; next=t; npool=nn; }
  return 0; }
