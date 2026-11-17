/* wall_births.c (Local, L1534): E(w) for every width, with each part's parent: the part of E(w-1) that holds the top w-1 cells of its windows. Prints every cyclic part outside the classes that has just split off the terminal cloud,
   its size, letter family and edges in, and how much of the extended cloud is lost at each width. Usage: ./wall_births WMAX. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef unsigned __int128 u128; typedef unsigned char u8;
static u8 TOUT[4][256], TST[4][256];
static void mk(void){ for(int s=0;s<4;s++) for(int b=0;b<256;b++){ int p1=s>>1,p2=s&1,o=0; for(int i=0;i<8;i++){ int c=(b>>i)&1; int q=c^(p1|p2); o|=q<<i; p2=p1; p1=q; } TOUT[s][b]=o; TST[s][b]=(p1<<1)|p2; } }
static inline u128 nxt(u128 x,int w,int s){ x|=((u128)1)<<(w+1); int n=w+3; u128 out=0; int pos=0; while(n-pos>=8){ int b=(int)(x>>pos)&255; out|=((u128)TOUT[s][b])<<pos; s=TST[s][b]; pos+=8; } int p1=s>>1,p2=s&1; while(pos<n){ int c=(int)(x>>pos)&1; int q=c^(p1|p2); out|=((u128)q)<<pos; p2=p1; p1=q; pos++; } return (out>>3)&((((u128)1)<<w)-1); }
static int cmp(const void*a,const void*b){ u128 x=*(const u128*)a,y=*(const u128*)b; return x<y?-1:x>y; }
static long uniq(u128*a,long n){ qsort(a,n,sizeof(u128),cmp); long m=0; for(long i=0;i<n;i++) if(!m||a[m-1]!=a[i]) a[m++]=a[i]; return m; }
static long find(const u128*a,long n,u128 v){ long lo=0,hi=n-1; while(lo<=hi){ long m=(lo+hi)/2; if(a[m]==v) return m; if(a[m]<v) lo=m+1; else hi=m-1; } return -1; }
int main(int c,char**v){ mk(); int WM=atoi(v[1]); u128 A=0,B=0; int a[11]={0,0,1,1,1,1,0,0,0,1,1},b[11]={0,1,0,1,1,1,0,0,0,1,1}; for(int i=0;i<11;i++){ if(a[i]) A|=((u128)1)<<i; if(b[i]) B|=((u128)1)<<i; }
  long nE=2; u128*E=malloc(sizeof(u128)*2); E[0]=A; E[1]=B; nE=uniq(E,2); u128*PE=0; long nP=0; int*Pcomp=0; int Pcloud=-1; int*Pcs=0;
  for(int w=12;w<=WM;w++){ long nS=2*nE; u128*S=malloc(sizeof(u128)*nS); for(long i=0;i<nE;i++){ S[2*i]=E[i]<<1; S[2*i+1]=(E[i]<<1)|1; } nS=uniq(S,nS); u128*old=E; long nOld=nE; 
    long ext=nS; for(;;){ u128*N=malloc(sizeof(u128)*nS*4); long k=0; for(long i=0;i<nS;i++) for(int s=0;s<4;s++) N[k++]=nxt(S[i],w,s); k=uniq(N,k); if(k>=nS){ free(N); break; } free(S); S=N; nS=k; S=realloc(S,sizeof(u128)*nS); }
    E=S; nE=nS; int *adj=malloc(sizeof(int)*nE*4); for(long i=0;i<nE;i++) for(int s=0;s<4;s++) adj[4*i+s]=(int)find(E,nE,nxt(E[i],w,s));
    int *idx=malloc(sizeof(int)*nE),*low=malloc(sizeof(int)*nE),*comp=malloc(sizeof(int)*nE),*stk=malloc(sizeof(int)*nE),*cs=malloc(sizeof(int)*nE); u8*ei=malloc(nE); u8*on=calloc(nE,1); int *call=malloc(sizeof(int)*nE); memset(idx,-1,sizeof(int)*nE); int ctr=0,sp=0,nc=0;
    for(long r=0;r<nE;r++) if(idx[r]<0){ int cp=0; call[cp]=r; ei[r]=0; idx[r]=low[r]=ctr++; stk[sp++]=r; on[r]=1; while(cp>=0){ int u=call[cp]; if(ei[u]<4){ int t=adj[4*u+ei[u]++]; if(idx[t]<0){ idx[t]=low[t]=ctr++; stk[sp++]=t; on[t]=1; ei[t]=0; call[++cp]=t; } else if(on[t]&&idx[t]<low[u]) low[u]=idx[t]; } else { if(low[u]==idx[u]){ int sz=0; for(;;){ int t=stk[--sp]; on[t]=0; comp[t]=nc; sz++; if(t==u) break; } cs[nc++]=sz; } cp--; if(cp>=0){ int p=call[cp]; if(low[u]<low[p]) low[p]=low[u]; } } } }
    u8*term=malloc(nc); memset(term,1,nc); u8*cyc=calloc(nc,1); int*into=calloc(nc,sizeof(int)); for(long i=0;i<nE;i++) for(int s=0;s<4;s++){ int j=adj[4*i+s]; if(comp[j]!=comp[i]){ term[comp[i]]=0; into[comp[j]]++; } else if(cs[comp[i]]>1||j==i) cyc[comp[i]]=1; }
    int cloud=-1,best=-1; for(int i=0;i<nc;i++) if(term[i]&&cs[i]>best){ best=cs[i]; cloud=i; }
    /* parents and letters of each cyclic part */
    int *parent=malloc(sizeof(int)*nc); memset(parent,-1,sizeof(int)*nc); u8*mixed=calloc(nc,1); u8*AA=calloc(nc,1),*AB=calloc(nc,1); long fromCloud=0,keptCloud=0; 
    for(long i=0;i<nE;i++){ int cm=comp[i]; if(PE){ long q=find(PE,nP,E[i]>>1); int pc=q>=0?Pcomp[q]:-2; if(parent[cm]==-1) parent[cm]=pc; else if(parent[cm]!=pc) mixed[cm]=1; if(pc==Pcloud){ fromCloud++; if(cm==cloud) keptCloud++; } }
      unsigned t=(unsigned)((E[i]>>(w-11))&2047); for(int s=0;s<4;s++){ int j=adj[4*i+s]; if(comp[j]!=cm) continue; unsigned t2=(unsigned)((E[j]>>(w-11))&2047); if(t==t2) AA[cm]=1; } }
    int births=0; for(int i=0;i<nc;i++) if(cyc[i]&&i!=cloud&&parent[i]==Pcloud&&!mixed[i]) births++;
    printf("w %d: E %ld cloud %d; of the windows over the old cloud %ld, in the cloud %ld; cyclic parts over the old cloud:",w,nE,best,fromCloud,keptCloud);
    for(int i=0;i<nc;i++) if(cyc[i]&&i!=cloud&&parent[i]==Pcloud){ printf(" [size %d %s in %d%s%s]",cs[i],AA[i]?"AAB-like":"AB-like",into[i],term[i]?" TERMINAL":"",mixed[i]?" mixed-parent":""); } printf("\n"); fflush(stdout);
    if(PE){ free(PE); free(Pcomp); free(Pcs); } PE=malloc(sizeof(u128)*nE); memcpy(PE,E,sizeof(u128)*nE); nP=nE; Pcomp=malloc(sizeof(int)*nE); memcpy(Pcomp,comp,sizeof(int)*nE); Pcloud=cloud; Pcs=malloc(sizeof(int)*nc); memcpy(Pcs,cs,sizeof(int)*nc);
    free(old); free(adj);free(idx);free(low);free(comp);free(stk);free(cs);free(ei);free(on);free(call);free(term);free(cyc);free(into);free(parent);free(mixed);free(AA);free(AB);
  } return 0; }
