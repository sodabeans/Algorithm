import sys
input = sys.stdin.readline

N = int(input())
dp = [N] * (N + 1)
options = []
for i in range(1, N + 1):
    if i * i <= N + 1:
        options.append(i * i)
    else:
        break

for i in range(len(options)):
    curr = options[i]
    dp[curr] = 1
    for j in range(curr + 1, N + 1):
        dp[j] = min(dp[j - curr] + 1, dp[j])

print(dp[-1])
