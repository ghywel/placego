// GC2792: independent serial gap-core/subset construction. No Lean/Wolfram execution.
// Inputs: trap codes, output directory, maximum even width. Hard data-size stops below.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>
using U=uint64_t; using V=std::vector<uint32_t>;
static void need(bool p,const char* s){if(!p)throw std::runtime_error(s);}
static U hashvec(const V& v){U h=1469598103934665603ULL;for(auto x:v){h^=x;h*=1099511628211ULL;}return h;}
struct Graph {
  int w; U mask; std::vector<U> words; std::vector<std::array<uint32_t,4>> edge;
  std::unordered_map<U,uint32_t> ids; std::vector<uint32_t> marks; uint32_t stamp=0;
  explicit Graph(int width):w(width),mask((U(1)<<width)-1){}
  U tick(U a,int c,int x)const{U b=a|(U(x)<<w);return (((b<<1)|c)^(b|(b>>1)))&mask;}
  U step(U a,int x,int y)const{return tick(tick(a,0,x),1,y);}
  U scalar(U a,int c,int x)const{
    static const int table[8]={0,1,1,1,1,0,0,0};U r=0;
    for(int i=0;i<w;i++){int l=i?((a>>(i-1))&1):c,m=(a>>i)&1,n=i+1<w?((a>>(i+1))&1):x;
      r|=U(table[4*l+2*m+n])<<i;}return r;
  }
  uint32_t insert(U a){auto p=ids.emplace(a,words.size());if(p.second){need(words.size()<3000000,"REACHABLE_CAP");words.push_back(a);}return p.first->second;}
  V build(const std::vector<U>& seeds){V b;for(auto a:seeds)b.push_back(insert(a));
    for(size_t i=0;i<words.size();i++){U a=words[i];std::array<uint32_t,4> e;int k=0;
      for(int x=0;x<2;x++)for(int y=0;y<2;y++){
        U v=step(a,x,y);if(i<2048)need(v==scalar(scalar(a,0,x),1,y),"SCALAR_ORACLE");e[k++]=insert(v);}
      edge.push_back(e);}
    marks.resize(words.size());std::sort(b.begin(),b.end());return b;
  }
  V gap(V a,int g){for(int k=1;k<=g;k++){
      if(++stamp==0){std::fill(marks.begin(),marks.end(),0);stamp=1;}
      V b;for(auto i:a)for(auto j:edge[i])if(int(words[j]&1)==int(k==g)&&marks[j]!=stamp){marks[j]=stamp;b.push_back(j);}
      std::sort(b.begin(),b.end());a.swap(b);
    }return a;
  }
  V core(V a,int &iterations){iterations=0;for(;;){V b=gap(a,3),c=gap(a,5);b.insert(b.end(),c.begin(),c.end());
      std::sort(b.begin(),b.end());b.erase(std::unique(b.begin(),b.end()),b.end());
      need(std::includes(a.begin(),a.end(),b.begin(),b.end()),"NOT_DECREASING");
      if(a==b)return a;a.swap(b);need(++iterations<1000,"CORE_ITER_CAP");}}
  V tighten(const V& c){std::vector<uint8_t> seen(words.size());V q=c;for(auto i:c)seen[i]=1;
    for(size_t k=0;k<q.size();k++)for(auto j:edge[q[k]])if(!seen[j]){seen[j]=1;q.push_back(j);}
    V pos(words.size(),UINT32_MAX);std::vector<U> nw;std::vector<std::array<uint32_t,4>> ne;
    for(uint32_t i=0;i<words.size();i++)if(seen[i]){pos[i]=nw.size();nw.push_back(words[i]);}
    for(uint32_t i=0;i<words.size();i++)if(seen[i]){std::array<uint32_t,4> e;for(int j=0;j<4;j++)e[j]=pos[edge[i][j]];ne.push_back(e);}
    V nc;for(auto i:c)nc.push_back(pos[i]);words.swap(nw);edge.swap(ne);ids.clear();ids.rehash(0);marks.assign(words.size(),0);stamp=0;return nc;
  }
};
int main(int argc,char**argv){try{
  need(argc==4||argc==5,"ARGS");int maxw=std::stoi(argv[3]),first=argc==5?std::stoi(argv[4]):16;
  need(maxw>=16&&maxw<=32&&maxw%2==0&&first>=16&&first<=maxw&&first%2==0,"WIDTH");
  std::ifstream in(argv[1]);std::vector<U> trap;U a;while(in>>a)trap.push_back(a);need(trap.size()==829,"TRAP_SIZE");std::sort(trap.begin(),trap.end());
  std::vector<U> prev;std::map<int,std::array<int,3>> expected={{16,{173,760,9}},{18,{460,2110,29}},{20,{1180,5484,44}},{22,{2979,13857,68}},{24,{7662,36402,366}},{26,{19415,93027,1326}},{28,{49376,237197,3319}}};
  if(first>16){std::ifstream p(std::string(argv[2])+"/core-"+std::to_string(first-2)+".txt");while(p>>a)prev.push_back(a);need(!prev.empty(),"MISSING_RESUME_CORE");}
  for(int w=first;w<=maxw;w+=2){std::vector<U> seeds;
    if(w==16){for(auto x:trap)if(x&1)seeds.push_back(x);}
    else for(auto x:prev)for(U h=0;h<4;h++)seeds.push_back(x|(h<<(w-2)));
    std::sort(seeds.begin(),seeds.end());Graph g(w);V b=g.build(seeds);size_t initial=g.words.size();int it;V c=g.core(b,it);
    // Independent direct full-lift control through width22; exact set comparison.
    if(w<=22&&w>16){std::vector<U> all;for(U h=0;h<(U(1)<<(w-16));h++)for(auto x:trap)if(x&1)all.push_back(x|(h<<16));
      Graph direct(w);V db=direct.build(all);int dit;V dc=direct.core(db,dit);std::vector<U>x,y;
      for(auto i:c)x.push_back(g.words[i]);for(auto i:dc)y.push_back(direct.words[i]);std::sort(x.begin(),x.end());std::sort(y.begin(),y.end());need(x==y,"DIRECT_CORE_CONTROL");}
    c=g.tighten(c);prev.clear();for(auto i:c)prev.push_back(g.words[i]);std::sort(prev.begin(),prev.end());
    std::ofstream co(std::string(argv[2])+"/core-"+std::to_string(w)+".txt");for(auto x:prev)co<<x<<'\n';co.close();
    std::vector<V> sets={c};std::vector<std::array<int,2>> tr;
    std::unordered_map<U,V> buckets;buckets[hashvec(c)].push_back(0);size_t stored=c.size();
    for(size_t i=0;i<sets.size();i++){
      std::array<int,2> row;for(int k=0;k<2;k++){V t=g.gap(sets[i],k?5:3);int id=-1;
        if(!t.empty()){auto h=hashvec(t);auto &bucket=buckets[h];for(auto j:bucket)if(sets[j]==t){id=j;break;}
          if(id<0){need(sets.size()<100000,"DFA_STATE_CAP");stored+=t.size();need(stored<=60000000,"DFA_STORAGE_CAP");id=sets.size();bucket.push_back(id);sets.push_back(std::move(t));}}
        row[k]=id;}tr.push_back(row);
    }
    if(expected.count(w)){auto e=expected[w];need(c.size()==size_t(e[0])&&g.words.size()==size_t(e[1])&&tr.size()==size_t(e[2]),"LOCAL_BASELINE_MISMATCH");}
    std::ofstream f(std::string(argv[2])+"/dfa-"+std::to_string(w)+".txt");for(auto r:tr)f<<r[0]<<' '<<r[1]<<'\n';f.close();
    std::cout<<"W "<<w<<" core "<<c.size()<<" reachable "<<g.words.size()<<" dfa "<<tr.size()<<" stored_ids "<<stored<<" lifted_reachable "<<initial<<" lifted_iterations "<<it<<std::endl;
  }
  std::cout<<"S16_CORE_REPLAY_PASS"<<std::endl;
}catch(const std::exception&e){std::cerr<<e.what()<<std::endl;return 2;}}
