import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
P = [0] + P

for i in range(1, N + 1):
    for j in range(1, i):
        P[i] = max(P[i], P[i - j] + P[j])

print(P[-1])
