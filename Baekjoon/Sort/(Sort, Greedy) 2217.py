import sys
input = sys.stdin.readline

N = int(input())
weights = [int(input()) for _ in range(N)]
weights.sort()
ans = 0
for idx in range(N):
    ans = max(ans, weights[idx] * (N - idx))
print(ans)
