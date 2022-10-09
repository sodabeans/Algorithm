import sys
input = sys.stdin.readline

N, M = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]

ans = 0

# horizontal 4
for i in range(N):
    for j in range(M - 3):
        curr = field[i][j] + field[i][j + 1] + field[i][j + 2] + field[i][j + 3]
        ans = max(ans, curr)

# vertical 4
for i in range(N - 3):
    for j in range(M):
        curr = field[i][j] + field[i + 1][j] + field[i + 2][j] + field[i + 3][j]
        ans = max(ans, curr)

# horizontal 2 + vertical 2 = square
for i in range(N - 1):
    for j in range(M - 1):
        curr = field[i][j] + field[i][j + 1] + field[i + 1][j] + field[i + 1][j + 1]
        ans = max(ans, curr)

# horizontal 3, vertical 1 up
for i in range(1, N):
    for j in range(M - 2):
        curr_one = field[i][j] + field[i][j + 1] + field[i][j + 2] + field[i - 1][j]
        curr_two = field[i][j] + field[i][j + 1] + field[i][j + 2] + field[i - 1][j + 1]
        curr_thr = field[i][j] + field[i][j + 1] + field[i][j + 2] + field[i - 1][j + 2]
        curr_fou = field[i][j] + field[i][j + 1] + field[i - 1][j + 1] + field[i - 1][j + 2]
        ans = max(ans, curr_one, curr_two, curr_thr, curr_fou)

# horizontal 3, vertical 1 down
for i in range(N - 1):
    for j in range(M - 2):
        curr_one = field[i][j] + field[i][j + 1] + field[i][j + 2] + field[i + 1][j]
        curr_two = field[i][j] + field[i][j + 1] + field[i][j + 2] + field[i + 1][j + 1]
        curr_thr = field[i][j] + field[i][j + 1] + field[i][j + 2] + field[i + 1][j + 2]
        curr_fou = field[i][j] + field[i][j + 1] + field[i + 1][j + 1] + field[i + 1][j + 2]
        ans = max(ans, curr_one, curr_two, curr_thr, curr_fou)

# horizontal 1 right, vertical 3
for i in range(N - 2):
    for j in range(M - 1):
        curr_one = field[i][j] + field[i + 1][j] + field[i + 2][j] + field[i][j + 1]
        curr_two = field[i][j] + field[i + 1][j] + field[i + 2][j] + field[i + 1][j + 1]
        curr_thr = field[i][j] + field[i + 1][j] + field[i + 2][j] + field[i + 2][j + 1]
        curr_fou = field[i][j] + field[i + 1][j] + field[i + 1][j + 1] + field[i + 2][j + 1]
        ans = max(ans, curr_one, curr_two, curr_thr, curr_fou)

# horizontal 1 left, vertical 3
for i in range(N - 2):
    for j in range(1, M):
        curr_one = field[i][j] + field[i + 1][j] + field[i + 2][j] + field[i][j - 1]
        curr_two = field[i][j] + field[i + 1][j] + field[i + 2][j] + field[i + 1][j - 1]
        curr_thr = field[i][j] + field[i + 1][j] + field[i + 2][j] + field[i + 2][j - 1]
        curr_fou = field[i][j] + field[i + 1][j] + field[i + 1][j - 1] + field[i + 2][j - 1]
        ans = max(ans, curr_one, curr_two, curr_thr, curr_fou)

print(ans)
