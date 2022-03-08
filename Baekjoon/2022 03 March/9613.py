"""
1) using recursion
memory: 30860 KB
time: 72 ms

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

"""
"""
https://www.geeksforgeeks.org/gcd-in-python/

2) Using math
memory: 32972 KB
time: 72 ms

import math
math.gcd()


3) Euclidean algorithm
memory: 30860 KB
time: 68 ms

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


"""

"""
4) using combinations instead of 2 loops
memory: 30860 KB
time: 72 ms

from itertools import combinations
for (a, b) in list(combinations(case, 2)):
        sum = sum + gcd(a, b)

"""


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

for _ in range(int(input())):
    sum = 0
    case = list(map(int, input().split()))
    length = case.pop(0)
    case.sort()
    for i in range(length):
        for j in range(i):
            sum = sum + gcd(case[i], case[j])

    print(sum)
