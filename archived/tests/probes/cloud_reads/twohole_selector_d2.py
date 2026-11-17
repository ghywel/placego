"""CL500: two-hole selector with displacement-1 and -2 pivot repairs. OUTCOME M=13 3333: 954,454 feasible instances; pair 896,298; recipe 57,462; miss 694 (334 with repeated targets; 376 at holes (8,9))."""
import sys
from collections import Counter
sys.argv=['x']
src=open('/home/user/placego/tests/probes/cloud_reads/twohole_selector.py').read().rsplit("\nif __name__ == '__main__':",1)[0]
src=src.replace("                    if len(ex) < 6: ex.append(((q1, q2), t, rep))","                    ex.append(((q1, q2), t, rep))")
exec(src)
REPAIR_SHIFTS=(1,2)
cnt, ex = run(13,(3,3,3,3))
print('with displacement 1 and 2 repairs:', dict(cnt))
print('misses by hole pair:', sorted(Counter(h for h,t,r in ex).items()))
print('examples:', ex[:6])
