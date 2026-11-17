/* wall_member.c (Local, L1532): real rows against the finite picture. N rows (40 random low cells, rain above), T backward ticks. Each tick: top wall; if the top 11 cells are a letter, the row is settled; look up its top-w window in E<w>.txt.
   Reports when rows enter the two closed classes, whether any leaves, which windows of E are seen, and the letters.
   Usage: ./wall_member W_ N T SEED CLOUD_PART LOCK_PART (part numbers from the file; pass -1 to detect by size). */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef unsigned __int128 u128; typedef unsigned char u8; typedef unsigned long long u64;
static u8 TOUT[4][256], TST[4][256];
static void mk(void){ for(int s=0;s<4;s++) for(int b=0;b<256;b++){ int p1=s>>1,p2=s&1,o=0; for(int i=0;i<8;i++){ int c=(b>>i)&1; int q=c^(p1|p2); o|=q<<i; p2=p1; p1=q; } TOUT[s][b]=o; TST[s][b]=(p1<<1)|p2; } }
static u64 rs; static u64 rnd(void){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
typedef struct { u128 v; int cls; int part; long seen; } ent; static ent *H; static long HM;
static u64 hsh(u128 v){ u64 a=(u64)v,b=(u64)(v>>64); a^=b*0x9E3779B97F4A7C15ULL; a^=a>>29; a*=0xBF58476D1CE4E5B9ULL; a^=a>>32; return a; }
static ent* look(u128 v){ u64 h=hsh(v)&(HM-1); while(H[h].cls){ if(H[h].v==v) return &H[h]; h=(h+1)&(HM-1); } return 0; }
static void put(u128 v,int cls,int part){ u64 h=hsh(v)&(HM-1); while(H[h].cls) h=(h+1)&(HM-1); H[h].v=v; H[h].cls=cls; H[h].part=part; H[h].seen=0; }
int main(int c,char**a){ mk(); int w=atoi(a[1]); long N=atol(a[2]); int T=atoi(a[3]); rs=strtoull(a[4],0,10)*2654435761ULL+88172645463325252ULL; char nm[64]; sprintf(nm,"E%d.txt",w); FILE*f=fopen(nm,"r"); if(!f){puts("no file");return 1;}
  long n=0; static long cap=1<<24; u128*V=malloc(sizeof(u128)*cap); int*P=malloc(sizeof(int)*cap); u8*TM=malloc(cap); char hx[40]; int part,term,cyc,e0,e1,e2,e3; static long psize[1<<22];
  while(fscanf(f,"%32s %d %d %d %d %d %d %d",hx,&part,&term,&cyc,&e0,&e1,&e2,&e3)==8){ u128 v=0; for(int i=0;i<32;i++){ int d=hx[i]<='9'?hx[i]-'0':hx[i]-'a'+10; v=(v<<4)|d; } V[n]=v; P[n]=part; TM[n]=term; psize[part]++; n++; } fclose(f);
  HM=1; while(HM<4*n) HM<<=1; H=calloc(HM,sizeof(ent)); long big=0; int cloud=-1,lock=-1; for(long i=0;i<n;i++) if(TM[i]&&psize[P[i]]>big){ big=psize[P[i]]; cloud=P[i]; } for(long i=0;i<n;i++) if(TM[i]&&P[i]!=cloud) lock=P[i];
  for(long i=0;i<n;i++) put(V[i],P[i]==cloud?1:P[i]==lock?2:3,P[i]);
  printf("w %d: E %ld cloud %ld lock %ld\n",w,n,psize[cloud],lock>=0?psize[lock]:0);
  int WB=(3*T+200)/8+16; u8*r=malloc(WB),*q=malloc(WB);
  long inCloud=0,inLock=0,neither=0,settledNone=0,leaves=0; long entry[64]={0}; long nonE=0,settledTicks=0,transTicks=0; long ticksCloud=0,ticksLock=0; long hist[32]={0};
  for(long row=0;row<N;row++){ memset(r,0,WB); u64 x=rnd(); x&=(1ULL<<40)-1; x|=1; for(int i=0;i<5;i++) r[i]=(x>>(8*i))&255; int b=(x>>39)&1; for(int j=40;j<WB*8;j++){ b^=1; if(b) r[j>>3]|=1<<(j&7); }
    int state=0,tin=-1; int cellmax=WB*8-16;
    for(int t=0;t<T;t++){ /* inverse */ int s=2; /* p1=1,p2=0 */ { int y0=r[0]&1; /* bit 0 stays */ int p1=1,p2=0; u8 o=y0; for(int j=1;j<8;j++){ int cc=(r[0]>>j)&1; int qq=cc^(p1|p2); o|=qq<<j; p2=p1; p1=qq; } q[0]=o; s=(p1<<1)|p2; } for(int i=1;i<WB;i++){ q[i]=TOUT[s][r[i]]; s=TST[s][r[i]]; } u8*tmp=r; r=q; q=tmp;
      /* top: scan down from the top of the used region */ int lim=40+3*(t+1)+80; if(lim>cellmax) lim=cellmax; int d=-1; for(int j=lim;j>=1;j--){ int a1=(r[j>>3]>>(j&7))&1,a0=(r[(j+1)>>3]>>((j+1)&7))&1; if(a1==a0){ d=j; break; } } if(d<w) continue;
      u128 v=0; for(int i=0;i<w;i++){ int j=d+2-w+i; if((r[j>>3]>>(j&7))&1) v|=((u128)1)<<i; }
      u64 t11=(u64)(v>>(w-11))&2047; int settled=(t11==0x63C||t11==0x63A); if(!settled){ if(state) leaves++; continue; } settledTicks++;
      ent*e=look(v); int cl=e?e->cls:0; if(e) e->seen++; else nonE++; if(cl==3) transTicks++; if(cl==1) ticksCloud++; if(cl==2) ticksLock++;
      if(state==0&&(cl==1||cl==2)){ state=cl; tin=t; if(t/32<64) entry[t/32]++; } else if(state&&cl!=state){ leaves++; } }
    if(state==1) inCloud++; else if(state==2) inLock++; else neither++; }
  long seenC=0,seenL=0,seenT=0; for(long i=0;i<HM;i++) if(H[i].cls&&H[i].seen){ if(H[i].cls==1) seenC++; else if(H[i].cls==2) seenL++; else seenT++; }
  printf("rows %ld: ended in cloud %ld lock %ld neither %ld; settled ticks %ld, in cloud %ld lock %ld transient %ld outside E %ld; departures from a class %ld\n",N,inCloud,inLock,neither,settledTicks,ticksCloud,ticksLock,transTicks,nonE,leaves);
  { static long ps[1<<22]; for(long i=0;i<HM;i++) if(H[i].cls==3) ps[H[i].part]+=H[i].seen; printf("transient cyclic or not, ticks spent by part (size:ticks):"); int shown=0; for(int p=0;p<(1<<22)&&shown<40;p++) if(ps[p]&&psize[p]>1){ printf(" %ld:%ld",psize[p],ps[p]); shown++; } puts(""); }
  printf("windows seen: cloud %ld lock %ld transient %ld\nentry tick histogram (bins of 32):",seenC,seenL,seenT); for(int i=0;i<24;i++) printf(" %ld",entry[i]); puts(""); return 0; }
