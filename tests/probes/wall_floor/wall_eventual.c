/* wall_eventual.c (Local, L1532): E(w), the width-w windows at the wall that survive arbitrarily many settled backward ticks, for every w, and the strongly connected parts of its graph.
   A window is a word of w cells, bit 0 the lowest, ending at the wall pair. One tick: read it from each of the four lower states, three rain cells above, keep the top w cells.
   E(11) = {A, B}. E(w) from E(w-1): extend by one lower cell, then take images until the set stops shrinking (the image of a closed set shrinks monotonically).
   Usage: ./wall_eventual WMAX [DUMPW ...]. Writes E<w>.txt for each DUMPW: hex window and part number; terminal parts are marked. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef unsigned __int128 u128; typedef unsigned char u8;
static u8 TOUT[4][256], TST[4][256];
static void mk(void){ for(int s=0;s<4;s++) for(int b=0;b<256;b++){ int p1=s>>1,p2=s&1,o=0; for(int i=0;i<8;i++){ int c=(b>>i)&1; int q=c^(p1|p2); o|=q<<i; p2=p1; p1=q; } TOUT[s][b]=o; TST[s][b]=(p1<<1)|p2; } }
static inline u128 nxt(u128 x,int w,int s){ /* x has w cells; add rain 0,1,0 above */
  x|=((u128)1)<<(w+1); int n=w+3; u128 out=0; int pos=0;
  while(n-pos>=8){ int b=(int)(x>>pos)&255; out|=((u128)TOUT[s][b])<<pos; s=TST[s][b]; pos+=8; }
  int p1=s>>1,p2=s&1; while(pos<n){ int c=(int)(x>>pos)&1; int q=c^(p1|p2); out|=((u128)q)<<pos; p2=p1; p1=q; pos++; }
  return (out>>3)&((((u128)1)<<w)-1); }
static int cmp(const void*a,const void*b){ u128 x=*(const u128*)a,y=*(const u128*)b; return x<y?-1:x>y; }
static long uniq(u128*a,long n){ qsort(a,n,sizeof(u128),cmp); long m=0; for(long i=0;i<n;i++) if(!m||a[m-1]!=a[i]) a[m++]=a[i]; return m; }
static long find(const u128*a,long n,u128 v){ long lo=0,hi=n-1; while(lo<=hi){ long m=(lo+hi)/2; if(a[m]==v) return m; if(a[m]<v) lo=m+1; else hi=m-1; } return -1; }
int main(int c,char**v){ mk(); int WM=atoi(v[1]); int dump[64]={0}; for(int i=2;i<c;i++) dump[atoi(v[i])>63?63:0]=0;
  static char want[129]; for(int i=2;i<c;i++) want[atoi(v[i])]=1;
  u128 A=0,B=0; int a[11]={0,0,1,1,1,1,0,0,0,1,1},b[11]={0,1,0,1,1,1,0,0,0,1,1}; for(int i=0;i<11;i++){ if(a[i]) A|=((u128)1)<<i; if(b[i]) B|=((u128)1)<<i; }
  long nE=2; u128*E=malloc(sizeof(u128)*2); E[0]=A; E[1]=B; nE=uniq(E,2);
  for(int w=12;w<=WM;w++){
    long nS=2*nE; u128*S=malloc(sizeof(u128)*nS); for(long i=0;i<nE;i++){ S[2*i]=E[i]<<1; S[2*i+1]=(E[i]<<1)|1; } free(E); nS=uniq(S,nS);
    int it=0; for(;;){ it++; u128*N=malloc(sizeof(u128)*nS*4); long k=0; for(long i=0;i<nS;i++) for(int s=0;s<4;s++) N[k++]=nxt(S[i],w,s); k=uniq(N,k); if(k>=nS){ free(N); break; } free(S); S=N; nS=k; S=realloc(S,sizeof(u128)*nS); }
    E=S; nE=nS;
    /* graph */
    int *adj=malloc(sizeof(int)*nE*4); for(long i=0;i<nE;i++) for(int s=0;s<4;s++){ long j=find(E,nE,nxt(E[i],w,s)); if(j<0){ puts("not closed"); return 1; } adj[4*i+s]=(int)j; }
    int *idx=malloc(sizeof(int)*nE),*low=malloc(sizeof(int)*nE),*comp=malloc(sizeof(int)*nE),*stk=malloc(sizeof(int)*nE),*cs=malloc(sizeof(int)*nE); u8*ei=malloc(nE); u8*on=calloc(nE,1); int *call=malloc(sizeof(int)*nE); memset(idx,-1,sizeof(int)*nE); int ctr=0,sp=0,nc=0;
    for(long r=0;r<nE;r++) if(idx[r]<0){ int cp=0; call[cp]=r; ei[r]=0; idx[r]=low[r]=ctr++; stk[sp++]=r; on[r]=1;
      while(cp>=0){ int u=call[cp]; if(ei[u]<4){ int t=adj[4*u+ei[u]++]; if(idx[t]<0){ idx[t]=low[t]=ctr++; stk[sp++]=t; on[t]=1; ei[t]=0; call[++cp]=t; } else if(on[t]&&idx[t]<low[u]) low[u]=idx[t]; }
        else { if(low[u]==idx[u]){ int sz=0; for(;;){ int t=stk[--sp]; on[t]=0; comp[t]=nc; sz++; if(t==u) break; } cs[nc++]=sz; } cp--; if(cp>=0){ int p=call[cp]; if(low[u]<low[p]) low[p]=low[u]; } } } }
    u8*term=malloc(nc); memset(term,1,nc); u8*cyc=calloc(nc,1); for(long i=0;i<nE;i++) for(int s=0;s<4;s++){ int j=adj[4*i+s]; if(comp[j]!=comp[i]) term[comp[i]]=0; else if(cs[comp[i]]>1||j==i) cyc[comp[i]]=1; }
    int nt=0,ncy=0; printf("w %d E %ld iters %d parts %d cyclic %d terminal",w,nE,it,nc,0); for(int i=0;i<nc;i++){ if(term[i]){ printf(" %d",cs[i]); nt++; } if(cyc[i]) ncy++; }
    printf(" | cyclic parts %d, sizes:",ncy); { int top[8]={0}; for(int i=0;i<nc;i++) if(cyc[i]&&!term[i]){ int x=cs[i]; for(int j=0;j<8;j++) if(x>top[j]){ int y=top[j]; top[j]=x; x=y; } } for(int j=0;j<8&&top[j];j++) printf(" %d",top[j]); }
    printf("\n"); fflush(stdout);
    if(want[w]){ char nm[64]; sprintf(nm,"E%d.txt",w); FILE*f=fopen(nm,"w"); for(long i=0;i<nE;i++){ unsigned long long hi=(unsigned long long)(E[i]>>64),lo=(unsigned long long)E[i]; fprintf(f,"%016llx%016llx %d %d %d %d %d %d %d\n",hi,lo,comp[i],term[comp[i]],cyc[comp[i]],adj[4*i],adj[4*i+1],adj[4*i+2],adj[4*i+3]); } fclose(f); }
    free(adj);free(idx);free(low);free(comp);free(stk);free(cs);free(ei);free(on);free(call);free(term);free(cyc);
  } return 0; }
