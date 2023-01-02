import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
dp = [0] * (k + 1)
for i in range(n):
    x = int(input())
    if x > k:
        continue
    coins.append(x)
coins.sort()
for i in range(len(coins)):
    curr_coin = coins[i]
    dp[curr_coin] += 1
    for j in range(curr_coin + 1, k + 1):
        dp[j] += dp[j - curr_coin]
print(dp[k])
