import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
ans = 0

for idx in range(N - 1, -1, -1):
    if K == 0:
        break
    if K >= coins[idx]:
        ans += (K // coins[idx])
        K = K % coins[idx]

print(ans)
