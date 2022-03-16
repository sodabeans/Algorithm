import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

# first element
dp[0][0] = graph[0][0]

# first row and first column
for i in range(1, N):
    dp[0][i] = graph[0][i] + dp[0][i-1]
    dp[i][0] = graph[i][0] + dp[i-1][0]

# other rows and columns
for i in range(1, N):
    for j in range(1, N):
            dp[i][j] = graph[i][j] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

def check_idx(x, y):
    if x < 0 or y < 0:
        return 0
    else:
        return dp[x][y]

for _ in range(M):
    # get inputs
    x1, y1, x2, y2 = map(int, input().split())

    answer = check_idx(x2 - 1, y2 - 1) - check_idx(x1 - 2, y2 - 1) - check_idx(x2 - 1, y1 - 2) + check_idx(x1 - 2, y1 - 2)

    # print result
    print(answer)

