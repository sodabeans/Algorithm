import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        curr = board[i][j]
        if curr == 0:
            continue
        if i + curr < N:
            dp[i + curr][j] += dp[i][j]
        if j + curr < N:
            dp[i][j + curr] += dp[i][j]

print(dp[-1][-1])
