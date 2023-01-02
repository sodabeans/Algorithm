import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [[1, 1] for _ in range(N)]

for i in range(1, N):
    for j in range(0, i):
        if A[j] < A[i]:
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)

for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if A[j] < A[i]:
            dp[i][1] = max(dp[i][1], dp[j][1] + 1)
dp_sum = [sum(_) for _ in dp]

print(max(dp_sum) - 1)
