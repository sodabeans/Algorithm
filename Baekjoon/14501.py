import sys
input = sys.stdin.readline

N = int(input())
time = []
price = []
dp = [0 for _ in range(N)]

for i in range(N):
    t, p = map(int, input().split())
    time.append(t)
    price.append(p)

for i in range(1, N):
    if time[i] + i < N:
        dp[time[i] + i] = max(dp[time[i] + i - 1], price[i] + dp[i - 1])
    elif time[i] == 1:
        dp[i] = max(dp[i], dp[i - 1] + price[i])

print(dp)
# ans = max(dp)
# if time[-1] == 1:
#     ans += price[-1]
# print(ans)