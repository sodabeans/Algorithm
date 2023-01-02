import sys
input = sys.stdin.readline

N = int(input())
dp = [[0 for _ in range(10)] for _ in range(N + 1)]
dp[1] = [1 for _ in range(10)]

for i in range(2, N + 1):
    for j in range(10):
        for idx in range(j, 10):
            dp[i][j] = (dp[i][j] + dp[i - 1][idx]) % 10007

print(sum(dp[-1]) % 10007)
