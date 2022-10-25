import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)
power = 1

for idx in range(1, N + 1):
    if (idx ** 0.5).is_integer():
        dp[idx] = 1
        power = idx
    else:
        dp[idx] = dp[idx - power] + dp[power]

print(dp[N])
