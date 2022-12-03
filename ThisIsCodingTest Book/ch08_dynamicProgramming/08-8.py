import sys
input = sys.stdin.readline

N, M = map(int, input().split())
bills = [int(input()) for _ in range(N)]
dp = [10001] * (M + 1)
dp[0] = 0
for i in range(N):
    for j in range(bills[i], M + 1):
        dp[j] = min(dp[j], dp[j - bills[i]] + 1)

if dp[-1] == 10001:
    print(-1)
else:
    print(dp[-1])
