import sys
input = sys.stdin.readline

N = int(input())
schedule = [map(int, input().split()) for _ in range(N)]
dp = [0 for _ in range(N + 1)]

for idx in range(N - 1, -1, -1):
    T, P = schedule[idx]
    if T + idx > N:
        dp[idx] = dp[idx + 1]
    else:
        dp[idx] = max(dp[T + idx] + P, dp[idx + 1])

print(dp[0])
