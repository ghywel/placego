/* fm.c -- exact f(n,m): least L such that the open interval (m, m+L) contains
 * distinct a_1..a_n with k | a_k.  f(n) = f(n,n) (Erdos problem 710).
 * Bipartite matching k -> multiples of k in (m, m+L); Hopcroft-Karp written here,
 * adjacency generated on the fly; binary search on L with warm starts
 * (a matching for L stays valid for every L' > L).
 * Usage: fm n [m] [dumpfile]   (m defaults to n; dumpfile gets the Hall-deficient
 *        set at L = f-1: the left vertices reachable from free ones by alternating paths)
 * Built-in wall-clock limit: aborts after TLIM seconds.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define TLIM 540.0
static long n, m, L, Lcap;
static int *matchL;   /* left k -> right x (absolute) or 0 */
static int  *matchR;   /* right index x-m-1 -> k or 0 */
static int  *dist, *queue, *stk;
static int *itp, *via;
static time_t t0;
#define INF 0x3fffffff

static void check_time(void){ if (difftime(time(NULL), t0) > TLIM){ fprintf(stderr,"TIME LIMIT\n"); exit(3);} }

static int bfs(void){
  int qh=0, qt=0, found=0;
  for (long k=1;k<=n;k++){ if(!matchL[k]){ dist[k]=0; queue[qt++]=(int)k; } else dist[k]=INF; }
  long hi = m+L-1;
  while(qh<qt){
    int u=queue[qh++];
    long x = ((m)/u+1)*(long)u;
    for(; x<=hi; x+=u){
      int w = matchR[x-m-1];
      if(!w) found=1;
      else if(dist[w]==INF){ dist[w]=dist[u]+1; queue[qt++]=w; }
    }
  }
  return found;
}

static long dfs_all(void){
  long aug=0, hi=m+L-1;
  for(long k=1;k<=n;k++) itp[k] = ((m)/k+1)*k;
  for(long s=1;s<=n;s++){
    if(matchL[s] || dist[s]!=0) continue;
    int sp=0; stk[sp++]=(int)s;
    while(sp){
      int u=stk[sp-1];
      int pushed=0;
      while(itp[u]<=hi){
        long x=itp[u]; itp[u]+=u;
        int w=matchR[x-m-1];
        if(!w){ /* augment */
          long r=x;
          for(int i=sp-1;i>=0;i--){
            int uu=stk[i];
            long rr = (i==sp-1)? r : via[uu];
            matchR[rr-m-1]=uu; matchL[uu]=rr;
          }
          aug++; sp=0; pushed=2; break;
        } else if(dist[w]==dist[u]+1){
          via[u]=x; stk[sp++]=w; pushed=1; break;
        }
      }
      if(pushed==2) break;
      if(!pushed){ dist[u]=INF; sp--; }
    }
  }
  return aug;
}

static long hk(void){ /* returns matching size */
  long size=0; for(long k=1;k<=n;k++) if(matchL[k]) size++;
  while(size<n && bfs()){ long a=dfs_all(); if(!a) break; size+=a; check_time(); }
  return size;
}

static void set_L(long newL, int *saveL){ /* load saved matching (valid for smaller L) */
  L=newL;
  memset(matchR,0,sizeof(int)*(size_t)Lcap);
  for(long k=1;k<=n;k++){ matchL[k]=saveL[k]; if(saveL[k]) matchR[saveL[k]-m-1]=(int)k; }
}

int main(int argc,char**argv){
  t0=time(NULL);
  n=atol(argv[1]); m=(argc>2)?atol(argv[2]):n;
  const char* dump=(argc>3)?argv[3]:NULL;
  Lcap = 4*n+64;
  matchL=calloc(n+1,sizeof(int)); matchR=calloc(Lcap,sizeof(int));
  dist=malloc(sizeof(int)*(n+1)); queue=malloc(sizeof(int)*(n+1)); stk=malloc(sizeof(int)*(n+1));
  itp=malloc(sizeof(int)*(n+1)); via=malloc(sizeof(int)*(n+1));
  int *bestfail=calloc(n+1,sizeof(int)); /* matching at largest failing L */
  long lo=n, hi; /* lo fails: (m,m+n) holds n-1 integers */
  /* exponential search upward from 2n */
  hi=2*n;
  for(;;){
    if(hi>=Lcap){ fprintf(stderr,"Lcap exceeded\n"); return 2; }
    set_L(hi,bestfail);
    long sz=hk();
    if(sz==n) break;
    memcpy(bestfail,matchL,sizeof(int)*(n+1)); lo=hi; hi*=2;
  }
  while(hi-lo>1){
    long mid=(lo+hi)/2;
    set_L(mid,bestfail);
    long sz=hk();
    if(sz==n) hi=mid; else { lo=mid; memcpy(bestfail,matchL,sizeof(int)*(n+1)); }
  }
  /* lo = f-1 fails, hi = f succeeds: rebuild the perfect matching at hi and verify it directly */
  { set_L(hi,bestfail); long s2=hk(); char *used=calloc(Lcap,1); long okc=0;
    for(long k=1;k<=n;k++){ long a=matchL[k]; if(a>m && a<m+hi && a%k==0 && !used[a-m-1]){ used[a-m-1]=1; okc++; } }
    printf("matching at L=f: size %ld, verified pairs (in range, k|a_k, distinct) %ld of %ld\n", s2, okc, n); free(used); }
  set_L(lo,bestfail); long sz=hk();
  long defic = n-sz;
  /* Hall-deficient set: left vertices reachable from free left vertices */
  long Ksz=0, NK=0;
  {
    int qh=0,qt=0; for(long k=1;k<=n;k++){ dist[k]=INF; if(!matchL[k]){dist[k]=0; queue[qt++]=(int)k;} }
    char *seenR=calloc(Lcap,1); long hiX=m+L-1;
    while(qh<qt){ int u=queue[qh++]; for(long x=((m)/u+1)*(long)u;x<=hiX;x+=u){ if(!seenR[x-m-1]){ seenR[x-m-1]=1; NK++; int w=matchR[x-m-1]; if(w && dist[w]==INF){ dist[w]=dist[u]+1; queue[qt++]=w; } } } }
    Ksz=qt;
    if(dump){ FILE*f=fopen(dump,"w"); for(long k=1;k<=n;k++) if(dist[k]!=INF) fprintf(f,"%ld\n",k); fclose(f); }
    free(seenR);
  }
  printf("n=%ld m=%ld f=%ld f/n=%.6f deficiency_at_f-1=%ld |K|=%ld |N(K)|=%ld secs=%.0f\n",
         n,m,hi,(double)hi/n,defic,Ksz,NK,difftime(time(NULL),t0));
  return 0;
}
