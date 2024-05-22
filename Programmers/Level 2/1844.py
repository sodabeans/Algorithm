from collections import deque

def solution(maps):
    answer = 0
    N = len(maps)
    M = len(maps[-1])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = [[-1 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1
    queue = deque()
    queue.append((0, 0))
    while queue:
        curr_x, curr_y = queue.popleft()
        for (dx, dy) in directions:
            new_x = curr_x + dx
            new_y = curr_y + dy
            if 0 <= new_x < N and 0 <= new_y < M and visited[new_x][new_y] == -1 and maps[new_x][new_y] == 1:
                visited[new_x][new_y] = visited[curr_x][curr_y] + 1
                queue.append((new_x, new_y))
    return visited[-1][-1]
