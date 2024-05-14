import copy
from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
lab_map = [list(map(int, input().split())) for _ in range(N)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
answer = 0


def bfs():
    queue = deque()
    bfs_map = copy.deepcopy(lab_map)

    for i in range(N):
        for j in range(M):
            if bfs_map[i][j] == 2:
                queue.append((i, j))

    while queue:
        curr_x, curr_y = queue.popleft()

        for dx, dy in directions:
            new_x = curr_x + dx
            new_y = curr_y + dy

            if 0 <= new_x < N and 0 <= new_y < M:
                if bfs_map[new_x][new_y] == 0:
                    bfs_map[new_x][new_y] = 2
                    queue.append((new_x, new_y))

    global answer
    curr_answer = 0
    for i in range(N):
        for j in range(M):
            if bfs_map[i][j] == 0:
                curr_answer += 1
    answer = max(answer, curr_answer)


def buildWall(wall_cnt):
    # build 3 walls
    if wall_cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if lab_map[i][j] == 0:
                lab_map[i][j] = 1
                buildWall(wall_cnt + 1)
                lab_map[i][j] = 0


buildWall(0)
print(answer)
