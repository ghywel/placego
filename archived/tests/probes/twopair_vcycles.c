// vcycles.c (Local, L1519): at width n, walk every cycle of Phi on odd registers once. For each cycle take the word
// V(t) = bit n-1 OR bit n-2. A collision of V on the registers is (a) a cycle whose V word has a period smaller than the cycle,
// or (b) two cycles whose V words are rotations of each other. Least rotation by Booth's algorithm, then a 128-bit hash.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
typedef uint64_t u64;
static inline u64 mix(u64 h,u64 v){h^=v;h*=0x9E3779B97F4A7C15ULL;h^=h>>29;return h;}
typedef struct{u64 a,b;u64 rep;uint32_t p;uint32_t used;}Ent;
static Ent*tab;static u64 cap,cnt;
static void grow(void);
static int insert(u64 a,u64 b,uint32_t p,u64 rep,u64*other){
  if(cnt*2>=cap)grow();
  u64 i=(a^(b*31))&(cap-1);
  for(;;){if(!tab[i].used){tab[i]=(Ent){a,b,rep,p,1};cnt++;return 0;}
    if(tab[i].a==a&&tab[i].b==b&&tab[i].p==p){*other=tab[i].rep;return 1;}
    i=(i+1)&(cap-1);}
}
static void grow(void){Ent*o=tab;u64 oc=cap;cap*=2;tab=calloc(cap,sizeof(Ent));if(!tab){puts("OOM");exit(2);}cnt=0;
  for(u64 k=0;k<oc;k++)if(o[k].used){u64 x;insert(o[k].a,o[k].b,o[k].p,o[k].rep,&x);}free(o);}
static uint32_t booth(const uint8_t*s,uint32_t n){ // least rotation start, O(n)
  uint32_t i=0,j=1,k=0;
  while(i<n&&j<n&&k<n){uint8_t a=s[(i+k)%n],b=s[(j+k)%n];
    if(a==b){k++;continue;}
    if(a>b)i+=k+1;else j+=k+1;
    if(i==j)j++;k=0;}
  return i<j?i:j;
}
int main(int c,char**v){int n0=atoi(v[1]),n1=atoi(v[2]);
 for(int n=n0;n<=n1;n++){
  u64 M=(n==64)?~0ULL:((1ULL<<n)-1);u64 N=1ULL<<(n-1);
  uint8_t*vis=calloc((N+7)/8,1);if(!vis){puts("OOM");return 2;}
  cap=1<<20;cnt=0;tab=calloc(cap,sizeof(Ent));
  size_t bc=1<<20;uint8_t*w=malloc(bc);
  u64 cycles=0,within=0,cross=0,maxP=0;u64 small[8]={0};u64 hist[64]={0};
  for(u64 idx=0;idx<N;idx++){
    if(vis[idx>>3]&(1<<(idx&7)))continue;
    u64 x=idx*2+1,y=x;uint32_t P=0;
    do{u64 k=y>>1;vis[k>>3]|=1<<(k&7);
      if(P>=bc){bc*=2;w=realloc(w,bc);}
      w[P++]=((y>>(n-1))|(y>>(n-2)))&1;
      y=(y^((y<<1)|(y<<2)))&M;}while(y!=x);
    cycles++;if(P>maxP)maxP=P;int lg=0;while((1u<<lg)<P)lg++;hist[lg]++;
    uint32_t p=P;
    for(;;){if(p&1)break;uint32_t h=p/2;int ok=1;for(uint32_t i=0;i<h;i++)if(w[i]!=w[i+h]){ok=0;break;}if(!ok)break;p=h;}
    if(p<P){within++;if(within<=3)printf("  n=%d within-cycle: x=%llx P=%u Vperiod=%u\n",n,(unsigned long long)x,P,p);}
    uint32_t r=booth(w,p);u64 a=0x1234567,b=0x89abcdef;
    u64 acc=0;int nb=0;for(uint32_t i=0;i<p;i++){uint32_t q=r+i;if(q>=p)q-=p;acc=acc*2+w[q];if(++nb==60){a=mix(a,acc);b=mix(b^0x55,acc+1);acc=0;nb=0;}}
    a=mix(a,acc+((u64)nb<<60));b=mix(b^0x77,acc+((u64)nb<<58));
    u64 other;if(insert(a,b,p,x,&other)){cross++;if(cross<=5)printf("  n=%d cross-cycle: x=%llx y=%llx Vperiod=%u\n",n,(unsigned long long)x,(unsigned long long)other,p);}
  }
  printf("n=%d registers=%llu cycles=%llu maxP=%llu within=%llu cross=%llu lgP:",n,(unsigned long long)N,(unsigned long long)cycles,(unsigned long long)maxP,(unsigned long long)within,(unsigned long long)cross);
  for(int i=0;i<40;i++)if(hist[i])printf(" %d:%llu",i,(unsigned long long)hist[i]);puts("");fflush(stdout);
  free(vis);free(tab);free(w);
 }
}
