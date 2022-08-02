from collections import deque
import sys
input = sys.stdin.readline

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N = int(input())
houses = [[int(x) for x in input().rstrip()] for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
ans = []

for i in range(N):
    for j in range(N):
        if houses[i][j] == 1 and visited[i][j] == 0:
            cnt = 1
            queue = deque()
            queue.append((i, j))
            while queue:
                curr_x, curr_y = queue.popleft()
                visited[curr_x][curr_y] = 1
                for idx in range(4):
                    dx, dy = directions[idx]
                    new_x = curr_x + dx
                    new_y = curr_y + dy
                    if 0 <= new_x < N and 0 <= new_y < N and visited[new_x][new_y] == 0 and houses[new_x][new_y] == 1:
                        visited[new_x][new_y] = 1
                        queue.append((new_x, new_y))
                        cnt += 1
            ans.append(cnt)

print(len(ans))
ans.sort()
for a in ans:
    print(a)
