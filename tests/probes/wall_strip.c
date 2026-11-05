/* wall_strip.c (Local, L1529): is the profile below the wall one strip up to a time shift? For rows quiet (period-3 letters) over the last Q ticks, collect the profile at every B tick of the last Q ticks.
   For each K: the number of distinct K-prefixes across all rows, and within one row (its time orbit). Usage: ./wall_strip ROWS TICKS LOW SEED Q */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef unsigned long long u64;
#define MAXB 24000
#define PK 320
static u64 s[2];
static inline u64 rotl(u64 x,int k){return (x<<k)|(x>>(64-k));}
static u64 rnd(void){u64 a=s[0],b=s[1],r=a+b;b^=a;s[0]=rotl(a,24)^b^(b<<16);s[1]=rotl(b,37);return r;}
static const unsigned char WA[11]={0,0,1,1,1,1,0,0,0,1,1}, WB[11]={0,1,0,1,1,1,0,0,0,1,1};
static unsigned char (*P)[PK]; static int *owner; static long np=0;
static int cmp(const void*a,const void*b){return memcmp(a,b,PK);}
int main(int c,char**v){ long rows=atol(v[1]); int ticks=atoi(v[2]), low=atoi(v[3]); s[0]=0x9E3779B97F4A7C15ULL^atol(v[4]); s[1]=0xBF58476D1CE4E5B9ULL; int Q=atoi(v[5]); for(int i=0;i<20;i++)rnd();
  P=malloc((size_t)rows*(Q/3+2)*PK); owner=malloc(sizeof(int)*rows*(Q/3+2));
  static unsigned char x[MAXB],z[MAXB]; static char seq[8192]; int n=low+3*ticks+40; long used=0;
  for(long r=0;r<rows;r++){ x[0]=1; for(int j=1;j<low;j++) x[j]=rnd()&1; { int b=x[low-1]; for(int j=low;j<n;j++){b^=1;x[j]=b;} }
    int top=-1; long start=np;
    for(int t=0;t<ticks;t++){ if(top<0){ int k=n-3; while(k>=1 && x[k]!=x[k+1]) k--; if(k>=10&&(!memcmp(x+k-9,WA,11)||!memcmp(x+k-9,WB,11))) top=k; } else top+=3;
      char ch='?'; if(top>=0){ if(!memcmp(x+top-9,WA,11)) ch='A'; else if(!memcmp(x+top-9,WB,11)) ch='B'; }
      seq[t]=ch;
      if(t>=ticks-Q && ch=='B' && top>PK+2){ for(int k=0;k<PK;k++) P[np][k]=x[top+1-k]; owner[np]=(int)r; np++; }
      int p1=1,p2=0; z[0]=1; for(int j=1;j<n;j++){ int o=x[j]^(p1|p2); z[j]=o; p2=p1; p1=o; } memcpy(x,z,n); }
    int ok=1; for(int t=ticks-Q;t<ticks;t++) if(seq[t]!=seq[t-3]) ok=0; if(!ok){ np=start; continue; } used++; }
  printf("rows quiet over the last %d ticks: %ld of %ld, profiles %ld\n",Q,used,rows,np);
  int Ks[]={12,20,24,26,28,32,36,40,44,48,56,64,80,96,128,160,200,256,320};
  /* the first row's orbit */
  int r0=owner[0]; long c0=0; while(c0<np&&owner[c0]==r0) c0++;
  static unsigned char tmp[PK];
  for(int i=0;i<(int)(sizeof Ks/sizeof Ks[0]);i++){ int K=Ks[i]; /* distinct K-prefixes overall */
    unsigned char (*Q2)[PK]=malloc(np*PK); memcpy(Q2,P,np*PK); for(long a=0;a<np;a++) memset(Q2[a]+K,0,PK-K); qsort(Q2,np,PK,cmp); long d=0; for(long a=0;a<np;a++) if(a==0||memcmp(Q2[a],Q2[a-1],PK)) d++;
    unsigned char (*R)[PK]=malloc(c0*PK); memcpy(R,P,c0*PK); for(long a=0;a<c0;a++) memset(R[a]+K,0,PK-K); qsort(R,c0,PK,cmp); long d0=0; for(long a=0;a<c0;a++) if(a==0||memcmp(R[a],R[a-1],PK)) d0++;
    /* share of all profiles whose K-prefix lies in the first row's orbit */
    long in=0; for(long a=0;a<np;a++){ memcpy(tmp,P[a],PK); memset(tmp+K,0,PK-K); if(bsearch(tmp,R,c0,PK,cmp)) in++; }
    printf("K=%3d distinct overall %6ld, in the first row's orbit %5ld, share of all profiles inside that orbit %.4f\n",K,d,d0,(double)in/np); free(Q2); free(R); }
  return 0; }
