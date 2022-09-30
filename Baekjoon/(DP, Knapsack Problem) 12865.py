import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
weights = []
values = []

for _ in range(N):
    W, V = map(int, input().split())
    weights.append(W)
    values.append(V)

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if weights[i - 1] <= j:
            dp[i][j] = max(values[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])
