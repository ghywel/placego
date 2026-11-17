// Independent C++ replay of the fixed b=13..22 B3 wall/funnel statements.
// Greatest all-input closed set; then any-input avoiding-path pruning.
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
int T[7][4]={{0,0,1,1},{0,1,1,0},{1,1,0,1},{0,1,0,1},{0,0,1,1},{0,0,0,1},{0,0,0,1}};
int main(int argc,char**argv){
 assert(argc==2);std::ifstream f(argv[1]);assert(f.good());
 bool wall[4][8192]={};int p,r,n=0;while(f>>p>>r){assert(p<4&&r<8192);assert(!wall[p][r]);wall[p][r]=true;n++;}assert(n==109);
 const int expected[]={1915,4898,11333,25160,54874,117528,247576,521940,1080509,2219547};
 for(int b=13;b<=22;b++){
  uint32_t N=4u<<b,mask=(1u<<b)-1;std::vector<uint8_t>a(N),z(N),fam(N);
  auto next=[&](uint32_t i,int bit){uint32_t ph=i>>b,x=i&mask;
   uint32_t left=((x<<1)|T[2][ph])&mask;
   uint32_t gate=x|(x>>1)|(uint32_t(bit)<<(b-1));
   return (((ph+1)%4)<<b)|(left^gate);};
  for(uint32_t i=0;i<N;i++)a[i]=T[2][i>>b]||((i&1)==unsigned(T[3][i>>b]));
  bool changed=true;while(changed){changed=false;for(uint32_t i=0;i<N;i++){
    z[i]=a[i]&&a[next(i,0)]&&a[next(i,1)];changed|=z[i]!=a[i];}a.swap(z);}
  int count=std::count(a.begin(),a.end(),1);assert(count==expected[b-13]);
  for(uint32_t i=0;i<N;i++){
   uint32_t ph=i>>b,x=i&mask;
   for(int off=0;off+13<=b;off+=7){
    uint32_t pre=0;for(int j=0;j<off;j++)pre|=T[(3+j)%7][ph]<<j;
    if((x&((1u<<off)-1))==pre && wall[ph][(x>>off)&8191])fam[i]=1;
   }
   assert(!fam[i]||a[i]);z[i]=a[i]&&!fam[i];
  }
  // Removing *only* the unshifted wall is a necessary countercontrol at 20.
  if(b==20){std::vector<uint8_t>q(N),qq(N);for(uint32_t i=0;i<N;i++)q[i]=a[i]&&!wall[i>>b][i&8191];
   bool ch=true;while(ch){ch=false;for(uint32_t i=0;i<N;i++){qq[i]=q[i]&&(q[next(i,0)]||q[next(i,1)]);ch|=qq[i]!=q[i];}q.swap(qq);}
   assert(std::count(q.begin(),q.end(),1)==4863);std::cout<<"unshifted20_avoiding=4863\n";
  }
  a=z;int rounds=0;changed=true;while(changed){changed=false;rounds++;
   for(uint32_t i=0;i<N;i++){z[i]=a[i]&&(a[next(i,0)]||a[next(i,1)]);changed|=z[i]!=a[i];}a.swap(z);}
  assert(std::count(a.begin(),a.end(),1)==0);
  std::cout<<"b="<<b<<" G="<<count<<" family="<<std::count(fam.begin(),fam.end(),1)<<" avoiding=0 rounds="<<rounds<<std::endl;
 }
 std::cout<<"BATCH4_WALL_PASS"<<std::endl;
}
