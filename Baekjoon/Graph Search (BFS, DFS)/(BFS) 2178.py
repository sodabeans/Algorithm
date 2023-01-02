from collections import deque
import sys
input = sys.stdin.readline

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
N, M = map(int, input().split())
maze = [[int(x) for x in input().rstrip()] for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[0][0] = 1
ans = 1
queue = deque()
queue.append((0, 0))
while queue:
    curr_x, curr_y = queue.popleft()
    for (dx, dy) in directions:
        new_x = curr_x + dx
        new_y = curr_y + dy
        if 0 <= new_x < N and 0 <= new_y < M and visited[new_x][new_y] == 0 and maze[new_x][new_y] == 1:
            visited[new_x][new_y] = visited[curr_x][curr_y] + 1
            queue.append((new_x, new_y))

print(visited[N - 1][M - 1])
