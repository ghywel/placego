// Rule 30 from one cell to T rows; left wheel j: L_j(t) = cell(t, -t+j). Least period (power of two) on the last half and transient.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#define T 65536
#define W (2*T+3)
static uint8_t row[2][W]; static uint8_t L[1025][T+1];
static double S=0,SJ=0; static int EM=0;
int main(){ memset(row,0,sizeof row); int c=T+1; row[0][c]=1; int cur=0;
  for(int t=0;t<=T;t++){ for(int j=0;j<=1024;j++) L[j][t]=row[cur][c-t+j];
    if(t==T) break; int nx=cur^1; for(int i=1;i<W-1;i++){ int a=row[cur][i-1],b=row[cur][i],d=row[cur][i+1]; row[nx][i]=a^(b|d);} cur=nx; }
  for(int j=0;j<=1024;j++){ int pe=-1; for(int e=0;e<=15;e++){ int p=1<<e, ok=1; for(int t=T/2;t+p<=T;t++) if(L[j][t]!=L[j][t+p]){ok=0;break;} if(ok){pe=e;break;} }
    if(pe<0){ printf("j=%d period not found\n",j); continue; } int p=1<<pe; int t0=0; for(int t=T-p-1;t>=j;t--) if(L[j][t]!=L[j][t+p]){t0=t+1;break;}
    if(j%32==0||j<=40) printf("j=%d e=%d p=%d tau=%d tau/j=%.3f\n",j,pe,p,t0,j?(double)t0/j:0); if(j>=512){S+=t0;SJ+=j;} if(pe>EM)EM=pe; }
  printf("mean tau/j over j=512..1024: %.4f; max period exponent %d\n",S/SJ,EM); return 0; }
