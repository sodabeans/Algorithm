import sys
input = sys.stdin.readline

N = int(input())
factors = list(map(int, input().split()))
factors.sort()
print(factors[0] * factors[-1])
