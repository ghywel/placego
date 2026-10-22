"""CL514/CL516: the edge cases of spectrum_h.py.  CORRECTION (CL518): counts are (pool, r) pairs, not pools.  OUTCOME: n 8 h 9: 2 pools with a gap; h 10: 10; n 9 h 9, 10: 0; n 10 h 12: 0, h 13: 2 (u = 44);
n 9 h 11: 2 (witness {0} u [12,19], u = 38); n 10 h 10, 11: 0."""
import sys
sys.argv=['x']
exec(open('tests/probes/cloud_reads/spectrum_h.py').read().rsplit("\nif __name__ == '__main__':",1)[0])
for n,h in ((9,11),):
    pools,gaps=run(n,h); print('n',n,'h',h,'pools',pools,'with a gap',len(gaps),gaps[:1],flush=True)
