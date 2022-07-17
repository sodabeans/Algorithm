import sys
input = sys.stdin.readline

N = int(input())
series = list(map(int, input().split()))
dp = [0] * N

for i in range(N):
    dp[i] = 1
    for j in range(0, i):
        if series[i] > series[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(max(dp))
