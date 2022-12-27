from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]

queue = deque()
queue.append((0, 0))

while queue:
    curr_x, curr_y = queue.popleft()
    value = board[curr_x][curr_y]
    if value == 0:
        continue
    if curr_x + value < N and dp[curr_x + value][curr_y] == 0:
        dp[curr_x + value][curr_y] += dp[curr_x][curr_y] + 1
        queue.append((curr_x + value, curr_y))
    if curr_y + value < N and dp[curr_x][curr_y + value] == 0:
        dp[curr_x][curr_y + value] += dp[curr_x][curr_y] + 1
        queue.append((curr_x, curr_y + value))

print(dp[-1][-1])
