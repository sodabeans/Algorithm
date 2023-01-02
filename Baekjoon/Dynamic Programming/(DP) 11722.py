import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [1] * N

for idx in range(1, N):
    for i in range(idx, -1, -1):
        if A[idx] < A[i]:
            dp[idx] = max(dp[i] + 1, dp[idx])

print(max(dp))
