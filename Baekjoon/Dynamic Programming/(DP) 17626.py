import sys
input = sys.stdin.readline

n = int(input())

dp = [50001 for _ in range(n + 1)]
dp[0] = 0
dp[1] = 1

for i in range(2, n + 1):
    j = 1
    while i >= j ** 2:
        dp[i] = min(dp[i], dp[i - j ** 2])
        j += 1
    dp[i] += 1

print(dp[n])
