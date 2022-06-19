from collections import deque
import sys
input = sys.stdin.readline

directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]


def bfs(field, Y, X):
    queue = deque()
    queue.append((X, Y))
    field[Y][X] = 0
    while queue:
        x, y = queue.popleft()
        field[y][x] = 0
        for i in range(4):
            dx, dy = directions[i]
            new_x = x + dx
            new_y = y + dy
            if 0 <= new_x < M and 0 <= new_y < N and field[new_y][new_x] == 1:
                field[new_y][new_x] = 0
                queue.append((new_x, new_y))


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0 for _ in range(M)] for _ in range(N)]
    cabbage = deque()
    cnt = 0

    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1
        cabbage.append((X, Y))

    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                bfs(field, i, j)
                cnt += 1

    print(cnt)
