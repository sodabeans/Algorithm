import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)
options = []
for i in range(N):
    if i ** 2 <= N:
        options.append(i ** 2)

for i in range(len(options)):
    curr = options[i]
    dp[curr] = 1
    for j in range(curr + 1, N + 1):
        dp[j] = dp[j - curr] + 1

print(dp[-1])
