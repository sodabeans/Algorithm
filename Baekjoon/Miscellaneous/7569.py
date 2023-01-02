import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())

box = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

ripe = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                ripe.append((i, j, k))

while ripe:
    i, j, k = ripe.popleft()
    for (di, dj, dk) in directions:
        new_i = i - di
        new_j = j - dj
        new_k = k - dk
        if 0 <= new_i < H and 0 <= new_j < N and 0 <= new_k < M and box[new_i][new_j][new_k] == 0:
            box[new_i][new_j][new_k] = box[i][j][k] + 1
            ripe.append((new_i, new_j, new_k))

# get results
day_cnt = 0 # count number of days it takes to ripe
condition = 1 # if unripe, make -1

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 0:
                condition = -1
                break
            day_cnt = max(day_cnt, box[i][j][k] - 1)

if condition == -1:
    print(-1)
else:
    print(day_cnt)
