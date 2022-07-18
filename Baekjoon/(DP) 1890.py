from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dp = [[0] * N for _ in range(N)]

queue = deque()
queue.append((0, 0))
while queue:
    x, y = queue.popleft()
    curr = board[x][y]
    if curr == 0:
        continue
    x_new = x + curr
    y_new = y + curr
    if x_new < N:
        dp[x_new][y] += 1
        if visited[x_new][y] == 0:
            visited[x_new][y] = 1
            queue.append((x_new, y))
    if y_new < N:
        dp[x][y_new] += 1
        if visited[x][y_new] == 0:
            visited[x][y_new] = 1
            queue.append((x, y_new))

print(dp[-1][-1])
