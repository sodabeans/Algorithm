import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000)

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
M, N = map(int, input().split())
input_map = [list(map(int, input().split())) for _ in range(M)]
visited = [[0 for _ in range(N)] for _ in range(M)]
answer = 0


def search(x, y):
    global answer

    for idx in range(len(directions)):
        dx, dy = directions[idx]
        new_x = x + dx
        new_y = y + dy
        if 0 <= new_x < M and 0 <= new_y < N and visited[new_x][new_y] == 0:
            if input_map[new_x][new_y] < input_map[x][y]:
                if new_x == M - 1 and new_y == N - 1:
                    answer += 1
                    continue
                visited[new_x][new_y] = 1
                search(new_x, new_y)
                visited[new_x][new_y] = 0


visited[0][0] = 1
search(0, 0)
print(answer)
