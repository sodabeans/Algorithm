from collections import deque
import sys
input = sys.stdin.readline

directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0 for _ in range(M)] for _ in range(N)]
    queue = deque()
    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1
        queue.append((X, Y))
    cnt = 0
    while queue:
        x, y = queue.popleft()
        field[y][x] = 0
        curr = True
        for i in range(4):
            dx, dy = directions[i]
            if 0 <= x + dx < M and 0 <= y + dy < N:
                if field[y + dy][x + dx] == 1:
                    curr = False
        if curr:
            cnt += 1

    print(cnt)
