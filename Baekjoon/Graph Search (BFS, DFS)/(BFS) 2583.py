from collections import deque
import sys
input = sys.stdin.readline

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

M, N, K = map(int, input().split())
paper = [[0 for _ in range(N)] for _ in range(M)]
visited = [[0 for _ in range(N)] for _ in range(M)]
ans = []
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            paper[y][x] = 1

for x in range(N):
    for y in range(M):
        queue = deque()
        if paper[y][x] == 0 and visited[y][x] == 0:
            cnt = 1
            queue.append((y, x))
            while queue:
                curr_y, curr_x = queue.popleft()
                visited[curr_y][curr_x] = 1
                for idx in range(4):
                    dx, dy = directions[idx]
                    new_x = curr_x + dx
                    new_y = curr_y + dy
                    if 0 <= new_x < N and 0 <= new_y < M:
                        if paper[new_y][new_x] == 0 and visited[new_y][new_x] == 0:
                            visited[new_y][new_x] = 1
                            cnt += 1
                            queue.append((new_y, new_x))
            ans.append(cnt)

ans.sort()
print(len(ans))
print(" ".join(map(str, ans)))
