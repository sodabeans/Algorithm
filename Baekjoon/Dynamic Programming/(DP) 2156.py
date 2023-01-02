import sys
input = sys.stdin.readline

n = int(input())
wine = [int(input()) for _ in range(n)]
dp = [0 for _ in range(n)]
if n == 1:
    print(wine[0])
    exit()
dp[0] = wine[0]
dp[1] = dp[0] + wine[1]
if n == 2:
    print(dp[1])
    exit()
dp[2] = max(dp[1], dp[0] + wine[2], wine[1] + wine[2])
for i in range(3, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i])

print(dp[-1])
