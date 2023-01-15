import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(N + 1):
    dp[i][1] = 1
for j in range(K + 1):
    dp[1][j] = j

for i in range(2, N + 1):
    for j in range(2, K + 1):
        dp[i][j] = int((dp[i][j - 1] + dp[i - 1][j]) % 1e9)

print(dp[-1][-1])
