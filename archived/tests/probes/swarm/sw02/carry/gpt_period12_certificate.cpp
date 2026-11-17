// Independent scalar checker of a small generated period12 profile graph.
#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stdexcept>
#include <vector>
#define REQUIRE(x) if(!(x))throw std::runtime_error(#x)
int shift(int w,int t){t%=12;return ((w>>t)|(w<<(12-t)))&4095;}
int main(int argc,char**argv){try{
 REQUIRE(argc==2);std::ifstream f(argv[1]);REQUIRE(f.good());
 int n,m,root;f>>n>>m>>root;REQUIRE(n==552&&m==576);
 std::vector<int>c(n),d(n),label(n);std::map<int,int>ids;
 std::vector<std::vector<int>>adj(n);
 for(int i=0;i<n;i++){f>>c[i]>>d[i]>>label[i];REQUIRE(c[i]>=0&&c[i]<4096&&d[i]>=0&&d[i]<4096);REQUIRE(ids.emplace((c[i]<<12)|d[i],i).second);}
 for(int k=0;k<m;k++){int a,b;f>>a>>b;REQUIRE(a>=0&&a<n&&b>=0&&b<n);adj[a].push_back(b);}
 REQUIRE(f.good());
 // Enumerate all4096 integrals independently, rather than prefix-XOR.
 for(int i=0;i<n;i++){
  std::set<int>actual(adj[i].begin(),adj[i].end()),expected;
  REQUIRE(actual.size()==adj[i].size());
  for(int w=0;w<4096;w++)if((shift(w,1)^w)==(c[i]|d[i])){
   auto q=ids.find((w<<12)|c[i]);REQUIRE(q!=ids.end());expected.insert(q->second);
  }
  REQUIRE(actual==expected);
 }
 auto reach=[&](std::vector<int>starts,int lab){
  std::vector<bool>seen(n,false);std::queue<int>q;
  for(int x:starts){seen[x]=true;q.push(x);}
  while(!q.empty()){int x=q.front();q.pop();for(int y:adj[x])if(!seen[y]&&(lab<0||label[y]==lab)){seen[y]=true;q.push(y);}}
  return seen;
 };
 std::vector<int>roots;
 for(int t=0;t<12;t++)roots.push_back(ids.at((shift(c[root],t)<<12)|shift(d[root],t)));
 auto visited=reach(roots,-1);REQUIRE(std::count(visited.begin(),visited.end(),true)==n);
 for(int l=0;l<6;l++){
  int count=0,edges=0,branches=0;
  for(int i=0;i<n;i++)if(label[i]==l){
   count++;int degree=0;for(int j:adj[i])degree+=label[j]==l;
   edges+=degree;branches+=degree==2;
   auto r=reach({i},l);REQUIRE(std::count(r.begin(),r.end(),true)==30);
   int j=ids.at((shift(c[i],1)<<12)|shift(d[i],1));REQUIRE(label[j]==(l+1)%6);
   for(int p=1;p<12;p++)REQUIRE(c[i]!=shift(c[i],p)||d[i]!=shift(d[i],p));
  }
  REQUIRE(count==30&&edges==32&&branches==2);
 }
 std::vector<bool>a(n,true),b(n);int rounds=0;bool changed=true;
 while(changed){changed=false;rounds++;for(int i=0;i<n;i++){
  bool any=false;for(int j:adj[i])any|=a[j];b[i]=a[i]&&any;changed|=a[i]!=b[i];
 }a.swap(b);}
 for(int i=0;i<n;i++)REQUIRE(a[i]==(label[i]>=0));
 for(int i=0;i<n;i++)if(a[i])for(int j:adj[i])if(a[j])REQUIRE(label[i]==label[j]);
 std::cout<<"PERIOD12_CERTIFICATE_PASS nodes="<<n<<" edges="<<m<<" live=180 peel_rounds="<<rounds<<std::endl;
 return 0;
 }catch(const std::exception&e){std::cerr<<"CERTIFICATE_REJECT "<<e.what()<<std::endl;return 2;}}
