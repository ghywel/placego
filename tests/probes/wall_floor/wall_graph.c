/* wall_graph.c (Local, L1556): the chain, recording its sequence of top-K words on ticks of depth at least DMIN, for K = 96, 128, 160, 192. Writes node tables and id streams. Arguments 6 and 7: DMIN and the output stem. From wall_capture.c (Local, L1534): does the window chain ever enter a lock? W-cell chain with fair lower states; each tick, depth of agreement with the consensus cells of a closed set (one word per phase, ? for cells that vary), and exact membership of the top K cells in the set. Chains restart on capture.
   Usage: ./wall_capture W SECONDS SEED SETFILE CONSENSUSFILE. Prints a line at every capture and the agreement histogram at the end. */
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
static u64 A[NWD],B[NWD];
static u64 refv[16][NWD],refm[16][NWD]; static int nref; static u64 setv[256][NWD]; static int nset,K; static long hist[MAXW+1];
#define NK 4
#define HB 22
static const int KS[NK]={96,128,160,192};
static u64 *hk[NK]; static unsigned *hid[NK]; static unsigned nn[NK]; static FILE *fo[NK],*fn[NK]; static int wasin=0;
static inline u64 mix(u64 x){ x^=x>>33; x*=0xff51afd7ed558ccdULL; x^=x>>33; x*=0xc4ceb9fe1a85ec53ULL; x^=x>>33; return x; }
 static int L3[4]; static long lastbreak; static long quietflags; static int maxbest;
int main(int c,char**a){ mk(); int W=atoi(a[1]); int DMIN=atoi(a[6]); for(int q=0;q<NK;q++){ hk[q]=calloc(1UL<<HB,8); hid[q]=calloc(1UL<<HB,4); char nm[300]; sprintf(nm,"%s.%d.ids",a[7],KS[q]); fo[q]=fopen(nm,"wb"); sprintf(nm,"%s.%d.nodes",a[7],KS[q]); fn[q]=fopen(nm,"w"); } long secs=atol(a[2]); rs=strtoull(a[3],0,10)*2654435761ULL+88172645463325252ULL; for(int i=0;i<20;i++) rnd(); char line[700]; FILE*f=fopen(a[5],"r"); while(fgets(line,700,f)){ int n=strcspn(line,"\n"); line[n]=0; if(!n) continue; for(int k=0;k<n;k++){ char ch=line[n-1-k]; int j=W-1-k; if(ch=='?') continue; refm[nref][j>>6]|=1ULL<<(j&63); if(ch=='#') refv[nref][j>>6]|=1ULL<<(j&63); } nref++; } fclose(f); f=fopen(a[4],"r"); while(fgets(line,700,f)){ int n=strcspn(line,"\n"); line[n]=0; if(!n) continue; K=n; for(int k=0;k<n;k++){ int j=W-1-k; if(line[n-1-k]=='#') setv[nset][j>>6]|=1ULL<<(j&63); } nset++; } fclose(f);
  int nb=W/8,nw=W/64; int lowj=W-K; u64 topmask[NWD]; memset(topmask,0,sizeof topmask); for(int j=lowj;j<W;j++) topmask[j>>6]|=1ULL<<(j&63); time_t t0=time(0); long ticks=0,caps=0,chains=0,abs=0;
  for(;;){ chains++; for(int i=0;i<nw;i++) A[i]=rnd(); A[nw]=0; { u64 top=0x63C; int base=W-11; for(int i=0;i<11;i++){ int j=base+i; u64 m=1ULL<<(j&63); if((top>>i)&1) A[j>>6]|=m; else A[j>>6]&=~m; } } long t=0; int lastchange=0; int l1=-1,l2=-1; long same2=0; L3[0]=L3[1]=L3[2]=-1; lastbreak=0;
    for(;;){ t++; ticks++; u8*x=(u8*)A; u8*o=(u8*)B; A[nw]=(u64)2; int s=rnd()>>62; for(int i=0;i<nb+1;i++){ o[i]=TOUT[s][x[i]]; s=TST[s][x[i]]; } for(int i=0;i<nw;i++) A[i]=(B[i]>>3)|(B[i+1]<<61);
      /* an AB row never ends: leave after 4,000 ticks of alternation */ { u64 topw=(A[(W-11)>>6]>>((W-11)&63)); if(((W-11)&63)>53) topw|=A[((W-11)>>6)+1]<<(64-((W-11)&63)); topw&=2047; int L=topw==0x63A; if(l2>=0&&L==l2&&L!=l1) same2++; else same2=0; l2=l1; l1=L; if(same2>4000){ abs++; break; } if(L3[2]>=0&&L!=L3[2]) lastbreak=t; L3[2]=L3[1]; L3[1]=L3[0]; L3[0]=L; if(t-lastbreak>20000000){ quietflags++; printf("QUIET chain %ld tick %ld total ticks %ld top: ",chains,t,ticks); for(int j=W-1;j>=0;j--) putchar((A[j>>6]>>(j&63))&1?'#':'.'); puts(""); fflush(stdout); goto next; } }
      if(t<300) continue; int best=0,bestr=0; for(int r=0;r<nref;r++){ int k=0; int done=0; for(int wd=nw-1;wd>=0&&!done;wd--){ u64 d=(A[wd]^refv[r][wd])&refm[r][wd]; if(d){ int hb=63-__builtin_clzll(d); int j=wd*64+hb; k=W-1-j; done=1; } } if(!done) k=W; if(k>best){ best=k; bestr=r; } } if(best>MAXW) best=MAXW; hist[best]++; if(best>=DMIN){ for(int q=0;q<NK;q++){ int K2=KS[q]; u64 h=0; for(int wd=nw-1;wd>=0;wd--){ int lo=wd*64; int top=W-K2; u64 v=A[wd]; if(lo+63<top) break; if(lo<top) v&=~0ULL<<(top-lo); h=mix(h^v); } if(h==0) h=1; u64 i=h>>(64-HB); while(hk[q][i]&&hk[q][i]!=h) i=(i+1)&((1UL<<HB)-1); if(!hk[q][i]){ hk[q][i]=h; hid[q][i]=++nn[q]; fprintf(fn[q],"%u %d %d ",nn[q],best,bestr); for(int j=W-1;j>=W-K2;j--) putc((A[j>>6]>>(j&63))&1?'#':'.',fn[q]); putc(10,fn[q]); } unsigned id=hid[q][i]; fwrite(&id,4,1,fo[q]); } wasin=1; } else if(wasin){ unsigned z=0; for(int q=0;q<NK;q++) fwrite(&z,4,1,fo[q]); wasin=0; } if(best>maxbest){ maxbest=best; if(best>=140){ printf("DEEPEST %d at total ticks %ld\n",best,ticks); fflush(stdout); } }
      if(best>=K-16){ for(int r=0;r<nset;r++){ int eq=1; for(int wd=0;wd<nw;wd++) if((A[wd]^setv[r][wd])&topmask[wd]){ eq=0; break; } if(eq){ caps++; printf("CAPTURE chain %ld tick %ld total ticks %ld top: ",chains,t,ticks); for(int j=W-1;j>=0;j--) putchar((A[j>>6]>>(j&63))&1?'#':'.'); puts(""); fflush(stdout); goto next; } } }
      if((ticks&0xFFFFFFFF)==0){ printf("progress ticks %ld seconds %ld captures %ld quiet %ld AB %ld deepest %d\n",ticks,(long)(time(0)-t0),caps,quietflags,abs,maxbest); fflush(stdout); } if((ticks&0xFFFFFF)==0&&time(0)-t0>=secs) goto done; }
    next: ; }
  done: printf("ticks %ld chains %ld captures %ld quiet %ld AB %ld deepest %d\nagreement depth tail:",ticks,chains,caps,quietflags,abs,maxbest); { long cum=0; for(int k=MAXW;k>=60;k--){ cum+=hist[k]; if(k%5==0&&cum) printf(" >=%d:%ld",k,cum); } } puts(""); return 0; }
