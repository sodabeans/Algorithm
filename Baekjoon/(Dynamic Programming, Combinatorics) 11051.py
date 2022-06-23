import sys
input = sys.stdin.readline

N, K = map(int, input().split())
if K == 0 or K == N:  # first or last coefficient
    print("1")
    exit()

if N - K < K:
    limit = N - K
else:
    limit = K

mid = int(N / 2) + 1

dp = [0] * mid
dp[0] = 1

for i in range(1, limit + 1):
    dp[i] = (dp[i - 1] * (N - i + 1) // i)

print(dp[limit] % 10007)