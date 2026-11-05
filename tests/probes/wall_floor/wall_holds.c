/* wall_lockscan.c (Local, L1534): every exact solution of period P below letters WORD, tested for closure with no assumption on shape. At each node whose offset is a multiple of STEP, run the closure of its phase-0 window under all four lower states,
   depth first, stopping at the first letter off the word or at CAP windows. A closed node ends its branch (wider words over it are closed too). Prints each closed node: width, closure size, the word. Usage: ./wall_lockscan P WORD KMAX STEP CAP NODECAP */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned char u8; typedef unsigned long long u64;
#define NW 12
typedef struct { u64 a[NW]; } win;
static u8 TOUT[4][256], TST[4][256];
static void mk(void){ for(int s=0;s<4;s++) for(int b=0;b<256;b++){ int p1=s>>1,p2=s&1,o=0; for(int i=0;i<8;i++){ int c=(b>>i)&1; int q=c^(p1|p2); o|=q<<i; p2=p1; p1=q; } TOUT[s][b]=o; TST[s][b]=(p1<<1)|p2; } }
static inline int getb(const win*x,int i){ return (x->a[i>>6]>>(i&63))&1; }
static inline void setb(win*x,int i){ x->a[i>>6]|=1ULL<<(i&63); }
static win nxt(win x,int w,int s){ setb(&x,w+1); int n=w+3; win o; memset(&o,0,sizeof o); u8*xb=(u8*)&x; u8*ob=(u8*)&o; int pos=0; while(n-pos>=8){ int b=xb[pos>>3]; ob[pos>>3]=TOUT[s][b]; s=TST[s][b]; pos+=8; } int p1=s>>1,p2=s&1; while(pos<n){ int c=getb(&x,pos); int q=c^(p1|p2); if(q) setb(&o,pos); p2=p1; p1=q; pos++; }
  win r; memset(&r,0,sizeof r); int top=(n+63)/64; for(int k=0;k<top&&k<NW;k++){ r.a[k]=(o.a[k]>>3)|(k+1<NW?(o.a[k+1]<<61):0); } { int wd=w>>6, bt=w&63; if(bt){ r.a[wd]&=(1ULL<<bt)-1; wd++; } for(int k=wd;k<NW;k++) r.a[k]=0; } return r; }
static win *H; static signed char*ph; static long HM; static long *touched; static long nt;
static u64 hs(const win*v,int nw){ u64 h=0; for(int k=0;k<nw;k++){ h=(h^v->a[k])*0x9E3779B97F4A7C15ULL; h^=h>>29; } h*=0xBF58476D1CE4E5B9ULL; h^=h>>32; return h; }
static int P,KMAX,STEP,NLEN; static long CAP,NODECAP; static u64 MASK; static u64 Y[900]; static long nodes,tests,closed,capped; static const char*WORD; static char LW[64]; static long bytest[900];
static u64 rotl1(u64 w){ return ((w<<1)|(w>>(P-1)))&MASK; }
static int letter(const win*v,int w){ int t=0; for(int i=0;i<11;i++) if(getb(v,w-11+i)) t|=1<<i; return t==0x63C?0:t==0x63A?1:2; }
static win *st; static signed char *sp_ph;
/* returns closure size if closed, 0 if a letter leaves, -1 if capped */
static long closure(win v0,int K){ int nw=(K+63)/64; for(long i=0;i<nt;i++) ph[touched[i]]=-1; nt=0; long sp=0; long cnt=0;
  { u64 h=hs(&v0,nw)&(HM-1); H[h]=v0; ph[h]=0; touched[nt++]=h; cnt=1; } st[0]=v0; sp_ph[0]=0; sp=1;
  while(sp){ sp--; win u=st[sp]; int p=sp_ph[sp]; int e=(p+1)%NLEN; for(int s=3;s>=0;s--){ win y=nxt(u,K,s); int L=letter(&y,K); if(L!=(LW[e]=='B')) return 0; u64 h=hs(&y,nw)&(HM-1); int found=0; while(ph[h]>=0){ if(!memcmp(&H[h],&y,sizeof(u64)*nw)){ found=1; break; } h=(h+1)&(HM-1); } if(found){ if(ph[h]!=e) return 0; continue; } H[h]=y; ph[h]=e; touched[nt++]=h; cnt++; if(cnt>CAP) return -1; st[sp]=y; sp_ph[sp]=e; sp++; } }
  return cnt; }
static u64 seenstrip[4096]; static int nseen=0;
int main(int c,char**v){ mk(); /* usage: wall_holds WORD TRIM CAP LETTERWORD */ const char*Wd=v[1]; int trim=atoi(v[2]); CAP=atol(v[3]); WORD=v[4]; int n=strlen(WORD); NLEN=n; P=n; for(int t=0;t<n;t++) LW[t]=WORD[t]; int len=strlen(Wd); int K=len-trim; win x; memset(&x,0,sizeof x); for(int i=0;i<K;i++) if(Wd[trim+i]=='#') setb(&x,i);
  HM=1; while(HM<4*CAP) HM<<=1; H=malloc(sizeof(win)*HM); ph=malloc(HM); memset(ph,-1,HM); touched=malloc(sizeof(long)*(CAP+8)); st=malloc(sizeof(win)*(4*CAP+16)); sp_ph=malloc(4*CAP+16); long r=closure(x,K); printf("w %d: %s %ld\n",K,r>0?"closed":r==0?"left the letters":"capped",r); return 0; }
