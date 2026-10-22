"""CL514: the edge cases n = 8..10, h = 9..11 of spectrum_h.py.  OUTCOME: n 8 h 9: 2 pools with a gap; h 10: 10; n 9 h 9, 10: 0;
n 9 h 11: 2 (witness {0} u [12,19], u = 38); n 10 h 10, 11: 0."""
import sys
sys.argv=['x']
exec(open('tests/probes/cloud_reads/spectrum_h.py').read().rsplit("\nif __name__ == '__main__':",1)[0])
for n,h in ((9,11),):
    pools,gaps=run(n,h); print('n',n,'h',h,'pools',pools,'with a gap',len(gaps),gaps[:1],flush=True)
