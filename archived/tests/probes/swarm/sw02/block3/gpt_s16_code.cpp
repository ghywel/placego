// GC2795: exact restricted-code determinization, not the full {3,5} language.
// Reuses GC2792's independently truth-table-checked graph; full bitmap equality
// resolves hashes. A=5, B=3555. Frozen ceilings are deliberately below GC2792.
#define main gc2792_unused_main
#include "gpt_s16_core.cpp"
#undef main
#include <sstream>
using Bits=std::vector<U>;
static U bhash(const Bits& a,bool collide){U h=1469598103934665603ULL;
  if(collide)return 0;for(U x:a){h^=x;h*=1099511628211ULL;}return h;}
static std::vector<U> readwords(const std::string& path){std::ifstream f(path);need(bool(f),"READ_CORE");std::vector<U>a;U x;while(f>>x)a.push_back(x);return a;}
static std::vector<std::array<int,2>> readtable(const std::string& path){std::ifstream f(path);need(bool(f),"READ_DFA");std::vector<std::array<int,2>>a;int x,y;while(f>>x>>y)a.push_back({x,y});return a;}
static int advance(int q,int k,const std::vector<std::array<int,2>>& t){
  for(char x:std::string(k?"3555":"5"))if(q>=0)q=t[q][x=='5'];return q;}
int main(int argc,char**argv){try{
  need(argc==5,"ARGS");std::string old=argv[1],out=argv[2];int maxw=std::stoi(argv[3]);bool collide=std::stoi(argv[4]);
  need(maxw>=16&&maxw<=32&&maxw%2==0,"WIDTH");if(collide)need(maxw<=20,"COLLISION_CONTROL_WIDTH");
  std::vector<U> prev;size_t prior_bitmap_bytes=0;
  for(int w=16;w<=maxw;w+=2){Graph g(w);std::vector<U> seeds;
    if(w<=28)seeds=readwords(old+"/core-"+std::to_string(w)+".txt");
    else for(U x:prev)for(U h=0;h<4;h++)seeds.push_back(x|(h<<(w-2)));
    std::sort(seeds.begin(),seeds.end());V c=g.build(seeds);int it=0;
    if(w>28)c=g.core(c,it);
    c=g.tighten(c);prev.clear();for(auto i:c)prev.push_back(g.words[i]);std::sort(prev.begin(),prev.end());
    need(!c.empty(),"EMPTY_CORE");
    std::ofstream co(out+"/code-core-"+std::to_string(w)+".txt");for(U x:prev)co<<x<<'\n';co.close();
    V positions(g.words.size(),UINT32_MAX);for(uint32_t i=0;i<c.size();i++)positions[c[i]]=i;
    size_t nb=(c.size()+63)/64;Bits root(nb);for(size_t i=0;i<c.size();i++)root[i/64]|=U(1)<<(i%64);
    auto pack=[&](const V&a){Bits b(nb);for(auto x:a){need(positions[x]!=UINT32_MAX,"LEAVES_CORE");auto j=positions[x];b[j/64]|=U(1)<<(j%64);}return b;};
    auto unpack=[&](const Bits&a){V b;for(size_t j=0;j<a.size();j++){U x=a[j];while(x){int k=__builtin_ctzll(x);need(64*j+k<c.size(),"BITMAP_PADDING");b.push_back(c[64*j+k]);x&=x-1;}}return b;};
    std::vector<Bits>sets={root};std::vector<std::array<int,2>>tr;std::vector<std::pair<int,int>>parent={{-1,-1}};
    std::unordered_map<U,V>buckets;buckets[bhash(root,collide)].push_back(0);
    std::vector<std::array<int,2>>reference;if(w<=28)reference=readtable(old+"/dfa-"+std::to_string(w)+".txt");
    // Each bitmap state maps to the unique original full-gap subset state.
    std::vector<int>ref={0};bool rejected=false;std::string bad;
    for(size_t i=0;i<sets.size();i++){
      std::array<int,2>row;
      for(int k=0;k<2;k++){V a=unpack(sets[i]);
        for(char x:std::string(k?"3555":"5"))a=g.gap(std::move(a),x-'0');
        int id=-1;if(!a.empty()){Bits b=pack(a);auto &bucket=buckets[bhash(b,collide)];
          for(auto j:bucket)if(sets[j]==b){id=j;break;}
          if(id<0){need(sets.size()<8192,"CODE_STATE_CAP");need(prior_bitmap_bytes+(sets.size()+1)*nb*8<=64*1024*1024,"CODE_BITMAP_CAP");
            id=sets.size();sets.push_back(std::move(b));parent.push_back({i,k});bucket.push_back(id);
            if(w<=28)ref.push_back(advance(ref[i],k,reference));}
        }else if(!rejected){rejected=true;std::string p(1,k?'B':'A');int q=i;while(parent[q].first>=0){p+=parent[q].second?'B':'A';q=parent[q].first;}std::reverse(p.begin(),p.end());bad=p;}
        if(w<=28){int r=advance(ref[i],k,reference);need((id<0)==(r<0),"REFERENCE_ACCEPTANCE");if(id>=0)need(ref[id]==r,"REFERENCE_SUBSET_IDENTITY");}
        row[k]=id;
      }tr.push_back(row);
    }
    // Adversarial guard controls: the two excluded non-code words must die.
    for(auto s:{"33","3553"}){V a=c;for(char x:std::string(s))a=g.gap(std::move(a),x-'0');need(a.empty(),"NEGATIVE_WORD_CONTROL");}
    std::ofstream f(out+"/code-dfa-"+std::to_string(w)+".txt");for(auto r:tr)f<<r[0]<<' '<<r[1]<<'\n';f.close();
    // Small independently replayable bitmap chunks. Core enumeration order is
    // explicit: sorted raw words, also equal to the construction's seed order.
    std::vector<U>ordered;for(auto i:c)ordered.push_back(g.words[i]);need(ordered==prev,"CORE_ORDER");
    size_t per=std::max(size_t(1),size_t(8*1024*1024)/(nb*8)),chunks=0;
    for(size_t a=0;a<sets.size();a+=per){std::ofstream b(out+"/code-bits-"+std::to_string(w)+"-"+std::to_string(chunks++)+".bin",std::ios::binary);
      for(size_t j=a;j<std::min(a+per,sets.size());j++)b.write(reinterpret_cast<const char*>(sets[j].data()),nb*8);}
    std::ofstream meta(out+"/code-meta-"+std::to_string(w)+".txt");meta<<c.size()<<' '<<nb<<' '<<sets.size()<<' '<<chunks<<'\n';meta.close();
    prior_bitmap_bytes+=sets.size()*nb*8;
    std::cout<<"W "<<w<<" core "<<c.size()<<" reachable "<<g.words.size()<<" code_states "<<tr.size()<<" bitmap_bytes "<<sets.size()*nb*8<<" iterations "<<it<<" rejected "<<rejected<<" bad "<<bad<<std::endl;
    if(rejected){std::ofstream f(out+"/counterexample.txt");f<<w<<' '<<bad<<'\n';std::cout<<"S16_CODE_COUNTEREXAMPLE\nS16_CODE_FINISHED"<<std::endl;return 0;}
  }
  std::cout<<"S16_CODE_ALL_PASS\nS16_CODE_FINISHED"<<std::endl;
}catch(const std::exception&e){std::cerr<<e.what()<<std::endl;return 2;}}
