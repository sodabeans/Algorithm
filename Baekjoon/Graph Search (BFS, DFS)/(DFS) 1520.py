import sys
input = sys.stdin.readline

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
M, N = map(int, input().split())
input_map = [list(map(int, input().split())) for _ in range(M)]
visited = [[-1 for _ in range(N)] for _ in range(M)]


def search(x, y):
    if x == M - 1 and y == N - 1:
        return 1

    if visited[x][y] == -1:
        visited[x][y] = 0
        for idx in range(len(directions)):
            dx, dy = directions[idx]
            new_x = x + dx
            new_y = y + dy
            if 0 <= new_x < M and 0 <= new_y < N:
                if input_map[new_x][new_y] < input_map[x][y]:
                    visited[x][y] += search(new_x, new_y)
    return visited[x][y]


print(search(0, 0))
