import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N = int(input())
grid = [list(map(str, input().rstrip())) for _ in range(N)]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = [[False for _ in range(N)] for _ in range(N)]
ans_first = 0
ans_second = 0


def dfs(x, y):
    visited[x][y] = True
    curr_color = grid[x][y]
    for idx in range(4):
        dx, dy = directions[idx]
        new_x = dx + x
        new_y = dy + y
        if 0 <= new_x < N and 0 <= new_y < N and visited[new_x][new_y] == 0:
            if curr_color == grid[new_x][new_y]:
                dfs(new_x, new_y)


for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i, j)
            ans_first += 1

visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if grid[i][j] == 'R':
            grid[i][j] = 'G'

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i, j)
            ans_second += 1

print(f'{ans_first} {ans_second}')
