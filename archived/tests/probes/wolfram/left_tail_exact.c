/* GC2263: exact reset/integration construction, single CPU thread.
   argv[1]=last column. History buffers are transient + one proved periodic tail.
   Pilot2048; a larger stage requires its own freeze. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <time.h>
#define CAP 524288
static unsigned char mem[3][CAP], oracle[257][65];
struct R { unsigned char *v; int tau,p; };
static unsigned char val(struct R r,int t){return r.v[t<r.tau?t:r.tau+(t-r.tau)%r.p];}
int main(int argc,char **argv){
 assert(argc==2);int J=atoi(argv[1]);assert(J>0&&J<=100000);
 char path[4096];snprintf(path,sizeof path,"%s/left_tails.csv",getenv("CAPPED_OUT"));FILE*f=fopen(path,"w");assert(f);fprintf(f,"j,tau,period\n0,0,1\n");
 /* Direct physical Rule30 oracle, coordinates -256..256, independently read along x=j-t. */
 unsigned char a[1025]={0},b[1025]={0};a[512]=1;
 for(int t=0;t<=256;t++){for(int j=0;j<=64;j++)oracle[t][j]=a[512-t+j];
  for(int x=1;x<1024;x++)b[x]=a[x-1]^(a[x]|a[x+1]);memcpy(a,b,sizeof a);}
 struct R u={mem[0],0,1},v={mem[1],0,1};v.v[0]=1;int maxp=1,maxt=0;double total=0,den=0;clock_t begin=clock();
 for(int j=1;j<=J;j++){
  struct R w={mem[(j+1)%3],0,1}; /* u,v consume the other two buffers. */
  int tau=u.tau>v.tau?u.tau:v.tau,P=u.p>v.p?u.p:v.p,reset=-1,par=0;
  for(int t=tau;t<tau+P;t++){if(val(v,t)&&reset<0)reset=t;par^=val(u,t);}
  int s=reset>=0?reset+1:tau,Q=(reset>=0||!par)?P:2*P;
  int end=s+Q;assert(end+2<CAP);w.v[0]=0;
  for(int t=0;t<end;t++)w.v[t+1]=val(u,t)^(val(v,t)|w.v[t]);
  assert(w.v[end]==w.v[s]);
  while(Q>1){int good=1;for(int t=0;t<Q/2;t++)if(w.v[s+t]!=w.v[s+t+Q/2]){good=0;break;}if(!good)break;Q/=2;}
  while(s>0&&w.v[s-1]==w.v[s-1+Q])s--;
  w.tau=s;w.p=Q;
  /* All recurrence equations beyond the seam follow by a common periodic block. */
  for(int t=tau;t<tau+2*P+2;t++)assert(val(w,t+1)==(val(u,t)^(val(v,t)|val(w,t))));
  if(j<=64)for(int t=0;t<=256;t++)assert(val(w,t)==oracle[t][j]);
  fprintf(f,"%d,%d,%d\n",j,s,Q);if(Q>maxp)maxp=Q;if(s>maxt)maxt=s;
  if(j>J/2){total+=s;den+=j;}
  if(j%10000==0)printf("j=%d tau=%d period=%d CPU=%.3f\n",j,s,Q,(double)(clock()-begin)/CLOCKS_PER_SEC);
  u=v;v=w;
 }
 fclose(f);printf("PASS J=%d max_period=%d max_tau=%d weighted_tail_tau_over_j=%.9f CPU=%.6f\n",J,maxp,maxt,total/den,(double)(clock()-begin)/CLOCKS_PER_SEC);return 0;
}
