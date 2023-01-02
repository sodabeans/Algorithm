import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (N + 1)
ans = [[0]] * (N + 1)
ans[1] = [1]

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        if dp[i] > dp[i // 2] + 1:
            ans[i] = ans[i // 2] + [i]
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        if dp[i] > dp[i // 3] + 1:
            ans[i] = ans[i // 3] + [i]
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if ans[i] == [0]:
        ans[i] = ans[i - 1] + [i]

ans[N].sort(reverse=True)

print(dp[N])
print(*ans[N], sep=' ')
