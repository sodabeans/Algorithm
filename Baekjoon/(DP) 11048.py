import sys
input = sys.stdin.readline

N, M = map(int, input().split())
candy = [list(map(int, input().split())) for _ in range(N)]

for r in range(N):
    for c in range(M):
        if r == 0 and c == 0:
            continue
        if r == 0:
            candy[r][c] += candy[r][c - 1]
        elif c == 0:
            candy[r][c] += candy[r - 1][c]
        else:
            candy[r][c] += max(candy[r - 1][c], candy[r][c - 1], candy[r - 1][c - 1])

print(candy[N - 1][M - 1])
