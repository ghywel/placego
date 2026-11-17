/* wall_closure.c (Local, L1532): closure of a set of windows under the backward tick with all four lower states, for windows up to 190 cells. Reads words (# and ., low to high, ending at the wall pair) from stdin, one group per line with the same length, or one word per line.
   Usage: ./wall_closure CAP [TRIM] : TRIM cells are removed from the low end first. For each input word prints the closure size, letters, and whether the next letter is forced at every window. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned char u8; typedef unsigned long long u64;
typedef struct { u64 a[3]; } win;
static u8 TOUT[4][256], TST[4][256];
static void mk(void){ for(int s=0;s<4;s++) for(int b=0;b<256;b++){ int p1=s>>1,p2=s&1,o=0; for(int i=0;i<8;i++){ int c=(b>>i)&1; int q=c^(p1|p2); o|=q<<i; p2=p1; p1=q; } TOUT[s][b]=o; TST[s][b]=(p1<<1)|p2; } }
static inline int getb(const win*x,int i){ return (x->a[i>>6]>>(i&63))&1; }
static inline void setb(win*x,int i){ x->a[i>>6]|=1ULL<<(i&63); }
static win nxt(win x,int w,int s){ setb(&x,w+1); int n=w+3; win o={{0,0,0}}; u8*xb=(u8*)&x; u8*ob=(u8*)&o; int pos=0; while(n-pos>=8){ int b=xb[pos>>3]; ob[pos>>3]=TOUT[s][b]; s=TST[s][b]; pos+=8; } int p1=s>>1,p2=s&1; while(pos<n){ int c=getb(&x,pos); int q=c^(p1|p2); if(q) setb(&o,pos); p2=p1; p1=q; pos++; }
  win r; r.a[0]=(o.a[0]>>3)|(o.a[1]<<61); r.a[1]=(o.a[1]>>3)|(o.a[2]<<61); r.a[2]=o.a[2]>>3; /* mask w cells */ for(int i=w;i<192;i++){ if(i%64==0){ for(int k=i/64;k<3;k++) r.a[k]=0; break; } r.a[i>>6]&=~(1ULL<<(i&63)); } return r; }
static win *H; static u8*used; static long HM; static long cnt;
static u64 hs(const win*v){ u64 h=v->a[0]*0x9E3779B97F4A7C15ULL^v->a[1]*0xC2B2AE3D27D4EB4FULL^v->a[2]*0x165667B19E3779F9ULL; h^=h>>29; h*=0xBF58476D1CE4E5B9ULL; h^=h>>32; return h; }
static int ins(win v){ u64 h=hs(&v)&(HM-1); while(used[h]){ if(!memcmp(&H[h],&v,sizeof(win))) return 0; h=(h+1)&(HM-1); } used[h]=1; H[h]=v; cnt++; return 1; }
static int letter(const win*v,int w){ int t=0; for(int i=0;i<11;i++) if(getb(v,w-11+i)) t|=1<<i; return t==0x63C?1:t==0x63A?2:0; }
int main(int c,char**a){ mk(); long cap=atol(a[1]); int trim=c>2?atoi(a[2]):0; HM=1; while(HM<3*cap) HM<<=1; H=malloc(sizeof(win)*HM); used=malloc(HM); win*st=malloc(sizeof(win)*(cap+8)); char line[400]; long ln=0;
  while(fgets(line,400,stdin)){ int n=strcspn(line,"\n"); line[n]=0; if(!n) continue; int w=n-trim; win v={{0,0,0}}; for(int i=trim;i<n;i++) if(line[i]=='#') setb(&v,i-trim); memset(used,0,HM); cnt=0; long sp=0; ins(v); st[sp++]=v; int letters=0; long split=0; int over=0;
    while(sp){ win u=st[--sp]; letters|=1<<letter(&u,w); int nl=-1; for(int s=0;s<4;s++){ win y=nxt(u,w,s); int L=letter(&y,w); if(nl<0) nl=L; else if(nl!=L) split++; if(ins(y)){ st[sp++]=y; if(cnt>=cap){ over=1; break; } } } if(over) break; }
    printf("%ld w %d closure %s%ld letters %s%s%s split windows %ld\n",ln++,w,over?">":"",cnt,letters&2?"A":"",letters&4?"B":"",letters&1?"?":"",split); fflush(stdout); }
  return 0; }
