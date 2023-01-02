from collections import deque
import sys
input = sys.stdin.readline

directions = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
queue = deque()


def bfs():
    while queue:
        r, c = queue.popleft()
        for idx in range(8):
            dr, dc = directions[idx]
            new_r = r + dr
            new_c = c + dc
            if 0 <= new_r < h and 0 <= new_c < w and visited[new_r][new_c] == 0:
                if area_map[new_r][new_c] == 1:
                    visited[new_r][new_c] = 1
                    queue.append((new_r, new_c))


while True:
    answer = 0
    queue = deque()
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        exit()
    visited = [[0 for _ in range(w)] for _ in range(h)]
    area_map = [list(map(int, input().split())) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if area_map[i][j] == 1 and visited[i][j] == 0:
                queue.append((i, j))
                visited[i][j] = 1
                bfs()
                answer += 1
    print(answer)
