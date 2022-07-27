import math
import sys
input = sys.stdin.readline

N = int(input())
prev = int(input())
distance = [0] * (N - 1)
for idx in range(N - 1):
    curr = int(input())
    distance[idx] = curr - prev
    prev = curr
target = math.gcd(distance[0], distance[1])
for idx in range(2, N - 1):
    target = math.gcd(target, distance[idx])
ans = 0
for idx in range(N - 1):
    ans += distance[idx] // target
print(ans - N + 1)
