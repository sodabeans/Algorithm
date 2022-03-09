# memory: 36688 KB
# time: 136 ms

from fractions import Fraction

import sys

N = int(sys.stdin.readline())
rings = list(int(x) for x in sys.stdin.readline().split())

for i in range(1, N):
    result = Fraction(rings[0], rings[i])
    if int(result) == result:
        print("{}/1".format(result))
        continue
    print(result)
