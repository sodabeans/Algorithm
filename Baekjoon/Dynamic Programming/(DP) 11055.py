import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = A.copy()

for idx in range(1, N):
    for i in range(idx, -1, -1):
        if A[idx] > A[i]:
            dp[idx] = max(dp[i] + A[idx], dp[idx])

print(max(dp))
