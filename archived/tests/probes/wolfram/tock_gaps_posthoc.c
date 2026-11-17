/* tock_gaps_posthoc.c: POST HOC checks added after tock_twins.c's run (Local, 2026-10-26, L955). Not predictions.

RUN-ON:   cpu (cc -O2 -o tock_gaps_posthoc tock_gaps_posthoc.c -lm; ./tock_gaps_posthoc), about a second, 160 MB.
Model and lanes copied verbatim from tock_twins.c (W = 40).
  1. PU in tock_twins.c gave a successive-gap Spearman of -0.198 for GPT's discrepancy along the 64 longest-lived lanes,
     against a within-lane shuffle. Those lanes are near-twins (L947), so the gaps are duplicated. Here every future is
     counted once (class key: the trace at times W .. 3W-1, which fixes the row at time W). OUTCOME: 125,401 futures (the
     funnel's count, an independent cross-check); the 64 lanes are 7 futures; deduplicated Spearman -0.067 (D >= 70, 151
     pairs), +0.0045 (D >= 60, 2,045), +0.0053 (D >= 52, 24,090), +0.0006 (all, 1,103,469). A coin-tock null (iid tocks,
     length 36 and 1000, computed separately in numpy) gives +0.002 and -0.003. PU's correlation was the duplication.
  2. Do distinct futures merge after the free chapter? Union-find over the tick-n classes, alive lanes (passed every
     earlier tick), every tick from W+2. OUTCOME: exactly 2 merge events, both at time 42, both between lanes that fail at
     42; no future that passes tick W+2 ever merges with another. (A first version started at time 2W, when every lane is
     dead, and reported nothing; corrected before any reading was recorded.)
Raw output gaps3.txt sha256 e82d60ad..., cited/tock-twins-20261026/.
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>

#define NW 4                 /* row words: depths 0..255 */
#define TW 3                 /* trace words: times 0..191 */
#define WMIN 8
#define WMAX 40
#define MMAX 24
typedef uint64_t u64;

static int RULE_XOR = 0;
static int fails = 0;
#define CHECK(cond, ...) do { if (!(cond)) { fails++; printf("CONTROL FAIL: " __VA_ARGS__); printf("\n"); } } while (0)

static inline int gb(const u64 *r, int d) { return (int)((r[d >> 6] >> (d & 63)) & 1); }
static inline void sb(u64 *r, int d) { r[d >> 6] |= 1ULL << (d & 63); }
static inline int req(const u64 *a, const u64 *b) { for (int i = 0; i < NW; i++) if (a[i] != b[i]) return 0; return 1; }
static int support(const u64 *r) { for (int i = NW - 1; i >= 0; i--) if (r[i]) return i * 64 + 63 - __builtin_clzll(r[i]); return 0; }

static void step(const u64 *w, u64 *o) {
  u64 r[NW], l[NW];
  for (int i = 0; i < NW; i++) {
    r[i] = (w[i] >> 1) | (i + 1 < NW ? (w[i + 1] << 63) : 0);
    l[i] = (w[i] << 1) | (i > 0 ? (w[i - 1] >> 63) : 0);
  }
  for (int i = 0; i < NW; i++) o[i] = RULE_XOR ? (r[i] ^ w[i] ^ l[i]) : (r[i] ^ (w[i] | l[i]));
  o[0] &= ~1ULL;
}

/* outward reconstruction from trace bits a(0..T-1), T <= 63: row bit d = F_d, d = 1..T */
static void reconstruct(u64 a, int T, u64 *row) {
  u64 cm1 = 0, c = a;
  memset(row, 0, NW * 8);
  if (c & 1) sb(row, 1);
  for (int d = 1; d < T; d++) {
    u64 nx = RULE_XOR ? ((c >> 1) ^ c ^ cm1) : ((c >> 1) ^ (c | cm1));
    cm1 = c; c = nx;
    if (c & 1) sb(row, d + 1);
  }
}
static int recon_last(u64 a, int T) {        /* F_T only */
  u64 cm1 = 0, c = a;
  for (int d = 1; d < T; d++) { u64 nx = (c >> 1) ^ (c | cm1); cm1 = c; c = nx; }
  return (int)(c & 1);
}
static u64 lane_trace(u64 l, int n) { u64 a = 0; for (int i = 0; i < n; i++) { a |= 1ULL << (2 * i); a |= ((l >> i) & 1ULL) << (2 * i + 1); } return a; }

/* one backward step: Q with forward(Q) = R, finite, support(R)-1; returns 1 if valid */
static int back1(const u64 *R, int x1, u64 *Q) {
  int r = support(R);
  memset(Q, 0, NW * 8);
  if (r < 1) return 0;
  int qm1 = 0, qc = x1;
  if (x1) sb(Q, 1);
  for (int j = 1; j <= r; j++) { int nx = gb(R, j) ^ (qc | qm1); qm1 = qc; qc = nx; if (nx) { if (j + 1 >= 255) return 0; sb(Q, j + 1); } }
  return gb(Q, r) == 0 && gb(Q, r + 1) == 0;
}

static int cmp_pair2(const void *A, const void *B){const int*a=A,*b=B; if(a[0]!=b[0]) return (a[0]>b[0])-(a[0]<b[0]); return (a[1]>b[1])-(a[1]<b[1]);}

/* POST-HOC (added after tock_twins.c's run, L955): deduplicated discrepancy-gap correlation at W = 40.
   Not a prediction: it checks whether PU's -0.198 survives removing twin duplicates (the top lanes share futures). */
#include <stdlib.h>
static int W=40, n=20;
static double spearman(double *x, double *y, int N){
  double *rx=malloc(N*sizeof(double)),*ry=malloc(N*sizeof(double));
  /* ranks via counting (gaps are small integers) */
  int cx[256]={0},cy[256]={0}; for(int i=0;i<N;i++){cx[(int)x[i]]++;cy[(int)y[i]]++;}
  double bx[256],by[256]; double acc=0; for(int v=0;v<256;v++){bx[v]=acc+(cx[v]+1)/2.0;acc+=cx[v];}
  acc=0; for(int v=0;v<256;v++){by[v]=acc+(cy[v]+1)/2.0;acc+=cy[v];}
  for(int i=0;i<N;i++){rx[i]=bx[(int)x[i]];ry[i]=by[(int)y[i]];}
  double mx=0,my=0; for(int i=0;i<N;i++){mx+=rx[i];my+=ry[i];} mx/=N;my/=N;
  double sxy=0,sxx=0,syy=0; for(int i=0;i<N;i++){sxy+=(rx[i]-mx)*(ry[i]-my);sxx+=(rx[i]-mx)*(rx[i]-mx);syy+=(ry[i]-my)*(ry[i]-my);}
  free(rx);free(ry); return sxy/sqrt(sxx*syy);
}
typedef struct { u64 key[TW]; int D; uint32_t l; } K;
static u64 *g_rows;
static int cmp_rows_ph(const void *A,const void *B){const u64*a=g_rows+(u64)(*(const uint32_t*)A)*NW,*b=g_rows+(u64)(*(const uint32_t*)B)*NW; for(int i=NW-1;i>=0;i--){if(a[i]<b[i])return -1;if(a[i]>b[i])return 1;} return 0;}
static int ck(const void*A,const void*B){const K*a=A,*b=B; for(int i=0;i<TW;i++){if(a->key[i]<b->key[i])return -1;if(a->key[i]>b->key[i])return 1;} return 0;}
int main(void){
  u64 L=1ULL<<n; int tmax=4*W+4;
  u64 *rows=calloc(L*NW,8),*tr=calloc(L*TW,8),*db=calloc(L*TW,8),tmp[NW]; int *D=calloc(L,sizeof(int));
  for(u64 l=0;l<L;l++) reconstruct(lane_trace(l,n),W,rows+l*NW);
  for(int t=0;t<=tmax;t++){
    for(u64 l=0;l<L;l++){ u64*r=rows+l*NW; int a=gb(r,1);
      if(a) tr[l*TW+(t>>6)]|=1ULL<<(t&63);
      if(!(t&1)&&!a&&D[l]==0) D[l]=t;
      if(t&1){ if(gb(r,3)^gb(r,5)) db[l*TW+((t>>1)>>6)]|=1ULL<<((t>>1)&63); }
      if(t<tmax){ step(r,tmp); memcpy(r,tmp,NW*8);} }
  }
  /* class key: trace bits at times W .. 3W-1 */
  K *k=malloc(L*sizeof(K));
  for(u64 l=0;l<L;l++){ memset(k[l].key,0,sizeof(k[l].key)); for(int t=W;t<3*W;t++) if((tr[l*TW+(t>>6)]>>(t&63))&1){int s=t-W; k[l].key[s>>6]|=1ULL<<(s&63);} k[l].D=D[l]; k[l].l=(uint32_t)l; }
  qsort(k,L,sizeof(K),ck);
  /* representatives: first of each class */
  int *rep=malloc(L*sizeof(int)); int nr=0; for(u64 i=0;i<L;i++) if(i==0||ck(&k[i],&k[i-1])) rep[nr++]=(int)k[i].l;
  printf("W=40 lanes %llu, distinct futures (trace W..3W-1) %d\n",(unsigned long long)L,nr);
  static double gx[4000000],gy[4000000];
  int thr[4]={70,60,52,0}; const char *nm[4]={"D>=70","D>=60","D>=52","all"};
  for(int z=0;z<4;z++) for(int win=0;win<2;win++){
    int N=0, lanes=0;
    for(int r=0;r<nr;r++){ int l=rep[r]; if(D[l]<thr[z]) continue; lanes++;
      int g[128],ng=0,last=-1; int i0= win? n : 0;
      for(int i=i0;2*i+1<D[l];i++){ if((db[(u64)l*TW+(i>>6)]>>(i&63))&1){ if(last>=0) g[ng++]=i-last; last=i; } }
      for(int q=0;q+1<ng && N<4000000;q++){gx[N]=g[q];gy[N]=g[q+1];N++;} }
    printf("%-6s window %-9s classes %7d successive-gap pairs %8d Spearman %+.4f\n",nm[z],win?"conducted":"whole",lanes,N,N>2?spearman(gx,gy,N):0.0);
  }
  /* the PU population itself, deduplicated: top-64 lanes by death */
  int top[64]; { int *o=malloc(L*2*sizeof(int)); for(u64 l=0;l<L;l++){o[2*l]=-D[l];o[2*l+1]=(int)l;}
    qsort(o,L,2*sizeof(int),cmp_pair2); for(int s=0;s<64;s++) top[s]=o[2*s+1]; free(o); }
  int distinct=0; for(int s=0;s<64;s++){ int dup=0; for(int q=0;q<s;q++){ int same=1; for(int t=W;t<3*W;t++) if(((tr[(u64)top[s]*TW+(t>>6)]^tr[(u64)top[q]*TW+(t>>6)])>>(t&63))&1){same=0;break;} if(same){dup=1;break;} } if(!dup) distinct++; }
  printf("PU's top-64 lanes form %d distinct futures\n",distinct);

  /* POST-HOC 2: exact check that no two distinct tick-n futures merge later (W = 40) */
  {
    uint32_t *cid=malloc(L*4); { int c=-1; for(u64 i=0;i<L;i++){ if(i==0||ck(&k[i],&k[i-1])) c++; cid[k[i].l]=(uint32_t)c; } }
    u64 *rw=calloc(L*NW,8);
    for(u64 l=0;l<L;l++) reconstruct(lane_trace(l,n),W,rw+l*NW);
    for(int t=1;t<=W+2;t++){ for(u64 l=0;l<L;l++){ step(rw+l*NW,tmp); memcpy(rw+l*NW,tmp,NW*8);} }
    int later_merges=0, ticks=0;
    uint32_t *ix=malloc(L*4); uint32_t *uf=malloc(L*4); for(u64 q=0;q<L;q++) uf[q]=(uint32_t)q;
    for(int t=W+2; t<=tmax; t+=2){
      u64 na=0; for(u64 l=0;l<L;l++) if(D[l]>=t) ix[na++]=(uint32_t)l;
      if(na==0) break;
      g_rows=rw; qsort(ix,na,4,cmp_rows_ph);
      for(u64 i=1;i<na;i++) if(req(rw+(u64)ix[i]*NW, rw+(u64)ix[i-1]*NW)){ uint32_t a=cid[ix[i]],b=cid[ix[i-1]]; while(uf[a]!=a)a=uf[a]; while(uf[b]!=b)b=uf[b];
          if(a!=b){ uf[a]=b; later_merges++; printf("LATER MERGE at time %d: lanes %u and %u (deaths %d)\n",t,ix[i],ix[i-1],D[ix[i]]); } }
      ticks++;
      for(int s2=0;s2<2;s2++) for(u64 l=0;l<L;l++){ step(rw+l*NW,tmp); memcpy(rw+l*NW,tmp,NW*8);} 
    }
    printf("POST-HOC 2: distinct merge events between tick-n classes after the free chapter (alive lanes, %d ticks from time W+2): %d\n",ticks,later_merges);
  }
  return 0;
}
