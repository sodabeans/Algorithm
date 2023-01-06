import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
dp = [1e9] * (k + 1)
for _ in range(n):
    x = int(input())
    if x > k:
        continue
    coins.append(x)
    dp[x] = 1

for i in range(len(coins)):
    curr_coin = coins[i]
    for j in range(curr_coin + 1, k + 1):
        dp[j] = min(dp[j - curr_coin] + 1, dp[j])
if dp[-1] == 1e9:
    print(-1)
else:
    print(dp[-1])
