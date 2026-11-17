// GC2833: independently check every integral, closure/reachability and SCC partition.
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <unordered_map>
#include <vector>
using namespace std;
void require(bool b, const char* why) { if (!b) throw runtime_error(why); }
int main(int argc, char** argv) {
  try {
    require(argc == 2, "INPUT"); ifstream in(argv[1]);
    size_t p,n,roots; in>>p>>n>>roots;
    require(in.good() && p<=32 && n<=200000 && roots>0 && roots<=n,"HEADER");
    vector<uint32_t> c(n),d(n); vector<size_t> stated(n);
    unordered_map<uint64_t,size_t> index;
    auto key=[](uint32_t a,uint32_t b){return (uint64_t(a)<<32)|b;};
    const uint64_t mask=(uint64_t(1)<<p)-1;
    for(size_t i=0;i<n;i++) {
      uint64_t a,b,k; in>>a>>b>>k;
      require(in.good() && a<=mask && b<=mask,"ROW"); c[i]=a;d[i]=b;stated[i]=k;
      require(index.emplace(key(c[i],d[i]),i).second,"DUPLICATE");
    }
    vector<vector<size_t>> adj(n),rev(n);
    for(size_t i=0;i<n;i++) {
      uint32_t drive=c[i]|d[i]; unsigned parity=0,bit=0; uint32_t w=0;
      for(size_t t=0;t<p;t++) { w|=uint32_t(bit)<<t; bit^=(drive>>t)&1; parity^=(drive>>t)&1; }
      if(parity) continue;
      for(uint32_t u : {w,uint32_t(w^mask)}) {
        auto found=index.find(key(u,c[i]));require(found!=index.end(),"NOT_CLOSED");
        size_t j=found->second;adj[i].push_back(j);rev[j].push_back(i);
      }
    }
    for(size_t i=0;i<n;i++) for(size_t j:adj[i]) for(size_t t=0;t<p;t++)
      require(((c[j]>>((t+1)%p))&1)==(((c[j]>>t)&1)^(((c[i]>>t)&1)|((d[i]>>t)&1))),"RECURRENCE");
    vector<char> seen(n); vector<size_t> order;
    for(size_t start=0;start<n;start++) if(!seen[start]) {
      vector<pair<size_t,size_t>> stack={{start,0}};seen[start]=1;
      while(!stack.empty()) {
        size_t v=stack.back().first, &next=stack.back().second;
        if(next<adj[v].size()) {size_t w=adj[v][next++];if(!seen[w]){seen[w]=1;stack.push_back({w,0});}}
        else {order.push_back(v);stack.pop_back();}
      }
    }
    fill(seen.begin(),seen.end(),0); vector<size_t> comp(n);size_t nc=0;
    for(auto it=order.rbegin();it!=order.rend();++it) if(!seen[*it]) {
      vector<size_t> stack={*it};seen[*it]=1;
      while(!stack.empty()){size_t v=stack.back();stack.pop_back();comp[v]=nc;
        for(size_t w:rev[v])if(!seen[w]){seen[w]=1;stack.push_back(w);}}
      nc++;
    }
    unordered_map<size_t,size_t> correspondence,reverse_map;
    for(size_t i=0;i<n;i++) {
      auto a=correspondence.emplace(stated[i],comp[i]);require(a.first->second==comp[i],"STATED_SPLIT");
      auto b=reverse_map.emplace(comp[i],stated[i]);require(b.first->second==stated[i],"STATED_MERGE");
    }
    fill(seen.begin(),seen.end(),0);vector<size_t> stack={0};seen[0]=1;size_t reachable=0;
    while(!stack.empty()){size_t v=stack.back();stack.pop_back();reachable++;for(size_t w:adj[v])if(!seen[w]){seen[w]=1;stack.push_back(w);}}
    require(reachable==n,"UNREACHABLE");
    if(roots>1) for(size_t i=0;i<roots;i++)
      require(find(adj[i].begin(),adj[i].end(),(i+1)%roots)!=adj[i].end(),"INPUT_CYCLE");
    size_t count=0,edges=0,forks=0;
    for(size_t i=0;i<n;i++) if(comp[i]==comp[0]) {
      count++;size_t deg=0;for(size_t w:adj[i])if(comp[w]==comp[0])deg++;
      edges+=deg;forks+=deg>1;
    }
    cout<<"p "<<p<<" nodes "<<n<<" components "<<nc<<" root_scc "<<count<<" edges "<<edges<<" forks "<<forks<<"\n";
    cout<<"DYADIC_CERTIFICATE_PASS\n";
  } catch(const exception& e) {cerr<<e.what()<<"\n";cout<<"DYADIC_CERTIFICATE_REJECT\n";return 2;}
}
