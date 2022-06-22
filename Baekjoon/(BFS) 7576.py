from collections import deque
import sys
input = sys.stdin.readline

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

M, N = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
all_ones = True
answer = 0

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j))
        elif box[i][j] == 0:
            all_ones = False

if all_ones:
    print("0")
    exit()

while queue:
    x, y = queue.popleft()
    for idx in range(4):
        dx, dy = directions[idx]
        new_x = x + dx
        new_y = y + dy
        if 0 <= new_x < N and 0 <= new_y < M and box[new_x][new_y] == 0:
            box[new_x][new_y] = box[x][y] + 1
            queue.append((new_x, new_y))

for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print("-1")
            exit()
        else:
            if box[i][j] > answer:
                answer = box[i][j]

print(answer - 1)
