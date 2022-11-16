import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ice = [list(map(int, input().rstrip())) for _ in range(N)]
answer = 0


def search(x, y):
    if 0 <= x < N and 0 <= y < M:
        if ice[x][y] == 0:
            ice[x][y] = 1
            search(x - 1, y)
            search(x + 1, y)
            search(x, y - 1)
            search(x, y + 1)
            return 1
    return 0


for i in range(N):
    for j in range(M):
        if search(i, j):
            answer += 1

print(answer)
