// GC2799: fixed-word review of L1613 using the archived core emitted BEFORE
// the capped DFA job stopped. No new core pruning or subset determinization.
#define main gc2792_unused_main
#include "gpt_s16_core.cpp"
#undef main
static std::vector<U> input(const std::string& path){std::ifstream f(path);need(bool(f),"INPUT");std::vector<U>a;U x;while(f>>x)a.push_back(x);need(!a.empty(),"EMPTY_INPUT");return a;}
int main(int argc,char**argv){try{
  need(argc==2,"ARGS");std::string path=argv[1],word="355535355535353";
  std::map<int,std::array<int,2>>expected={{26,{19415,93027}},{28,{49376,237197}},{30,{123710,591685}}};
  for(int w:{26,28,30}){
    auto raw=input(path+"/code-core-"+std::to_string(w)+".txt");
    need(std::is_sorted(raw.begin(),raw.end())&&std::adjacent_find(raw.begin(),raw.end())==raw.end(),"CORE_ORDER");
    Graph g(w);V c=g.build(raw);need(c.size()==size_t(expected[w][0])&&g.words.size()==size_t(expected[w][1]),"CORE_REACHABLE_COUNTS");
    V fixed=g.gap(c,3),other=g.gap(c,5);fixed.insert(fixed.end(),other.begin(),other.end());std::sort(fixed.begin(),fixed.end());fixed.erase(std::unique(fixed.begin(),fixed.end()),fixed.end());need(c==fixed,"CORE_FIXED_POINT");
    if(w==30){auto old=input(path+"/code-core-28.txt");for(U a:raw)need(std::binary_search(old.begin(),old.end(),a&((U(1)<<28)-1)),"PROJECTION");}
    auto read=[&](const std::string&s){V a=c;for(char x:s)a=g.gap(std::move(a),x-'0');return a.size();};
    size_t full=read(word),prefix=read(word.substr(0,word.size()-1)),suffix=read(word.substr(1));
    need(w==30?(full==0&&prefix>0&&suffix>0):(full>0),"LOCAL_WITNESS_MISMATCH");
    need(read("33")==0&&read("3553")==0,"NEGATIVE_CONTROL");
    std::string reverse=word;std::reverse(reverse.begin(),reverse.end());
    std::cout<<"W "<<w<<" word "<<word<<" endpoints "<<full<<" proper_prefix "<<prefix<<" proper_suffix "<<suffix<<" reverse "<<read(reverse)<<std::endl;
  }
  std::cout<<"S16_LOCAL_FIXED_WORD_PASS"<<std::endl;
}catch(const std::exception&e){std::cerr<<e.what()<<std::endl;return 2;}}
