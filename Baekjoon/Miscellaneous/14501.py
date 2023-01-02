import sys
input = sys.stdin.readline

N = int(input())
time = []
price = []
dp = [0 for _ in range(N + 1)]

for i in range(N):
    t, p = map(int, input().split())
    time.append(t)
    price.append(p)

for i in range(N - 1, -1, -1):
    if time[i] + i > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[time[i] + i] + price[i], dp[i + 1])

print(dp[0])
