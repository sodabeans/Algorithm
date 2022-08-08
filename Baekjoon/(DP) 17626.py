# timeout error
import sys
input = sys.stdin.readline

n = int(input())

dp = [50001 for _ in range(n + 1)]
dp[0] = 0

for i in range(1, n + 1):
    for j in range(1, i + 1):
        square = j ** 2
        if square <= i:
            dp[i] = min(dp[i], dp[i - square] + 1)

print(dp[n])
