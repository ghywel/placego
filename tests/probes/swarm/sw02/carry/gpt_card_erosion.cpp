// GC2837. Independent finite preimage count, not an all-depth obstruction.
// Fixed alternating block [-48,0], black at zero. Enumerate exactly s<=9.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using U = unsigned __int128;
static unsigned bit(U x, int j) { return unsigned((x >> j) & 1); }
static unsigned rule(unsigned l, unsigned c, unsigned r) {
  return (30u >> (4*l + 2*c + r)) & 1u;
}
int main() {
  constexpr int W=48;
  for (int phase=0; phase<2; ++phase) {
    U start=0;
    for (int i=0; i<=W; ++i)
      if (((i-W+phase)%2+2)%2==0) start |= U(1)<<i;
    std::vector<U> rows{start}; int lo=-W, n=W+1;
    for (int s=1; s<=9; ++s) {
      std::vector<U> next; next.reserve(4*rows.size());
      std::map<int,uint64_t> histogram;
      for (U y: rows) for (unsigned a=0; a<2; ++a)
        for (unsigned b=0; b<2; ++b) {
          U x=(U(a)<<n)|(U(b)<<(n+1));
          for (int j=n-1; j>=0; --j) {
            unsigned l=bit(y,j) ^ (bit(x,j+1)|bit(x,j+2));
            x |= U(l)<<j;
          }
          // Forward truth-table oracle, separately from the inverse formula.
          for (int j=0; j<n; ++j)
            assert(rule(bit(x,j),bit(x,j+1),bit(x,j+2))==bit(y,j));
          int extent=lo-2;
          for (int j=0; j<n+2; ++j) {
            int p=lo-1+j;
            unsigned want=((p+phase)%2+2)%2==0;
            if (bit(x,j)!=want) break;
            extent=p;
          }
          assert(extent>=lo-1);
          ++histogram[-extent]; next.push_back(x);
        }
      rows.swap(next); --lo; n+=2;
      assert(rows.size()==(uint64_t(1)<<(2*s)));
      int worst=histogram.rbegin()->first;
      assert(worst==4*s-phase);
      if (!phase && s>=4) assert(histogram[4*s]==40*(uint64_t(1)<<(2*(s-4))));
      std::cout << phase << '\t' << s << '\t' << rows.size() << '\t'
                << worst << '\t' << histogram[worst] << '\n';
    }
  }
  std::cout << "CARD_EROSION_FINITE_PASS\n";
}
