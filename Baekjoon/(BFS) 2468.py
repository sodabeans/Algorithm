from collections import deque
import sys
input = sys.stdin.readline

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(size, limit, graph):
    cnt = 0
    visited = [[0 for _ in range(size)] for _ in range(size)]
    for x in range(size):
        for y in range(size):
            if graph[x][y] > limit and visited[x][y] == 0:
                queue = deque()
                queue.append((x, y))
                while queue:
                    curr_x, curr_y = queue.popleft()
                    visited[curr_x][curr_y] = 1
                    for idx in range(4):
                        dx, dy = directions[idx]
                        new_x = curr_x + dx
                        new_y = curr_y + dy
                        if 0 <= new_x < size and 0 <= new_y < size:
                            if visited[new_x][new_y] == 0 and graph[new_x][new_y] > limit:
                                visited[new_x][new_y] = 1
                                queue.append((new_x, new_y))
                cnt += 1
    return cnt


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
rain = 0
ans = 1
maximum_limit = max([max(_) for _ in area])

while rain < maximum_limit:
    curr_cnt = bfs(N, rain, area)
    rain += 1
    ans = max(ans, curr_cnt)

print(ans)
