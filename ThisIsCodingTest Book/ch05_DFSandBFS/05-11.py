from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
space = [list(map(int, input().rstrip())) for _ in range(N)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
queue = deque()
queue.append([0, 0])

while queue:
    x, y = queue.popleft()
    for dx, dy in directions:
        new_x = x + dx
        new_y = y + dy
        if 0 <= new_x < N and 0 <= new_y < M and space[new_x][new_y] == 1:
            space[new_x][new_y] = space[x][y] + 1
            queue.append([new_x, new_y])

print(space[-1][-1])
