import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    if n == 1:
        print(max(sticker[0][0], sticker[1][0]))
        continue
    sticker[0][1] += sticker[1][0]
    sticker[1][1] += sticker[0][0]
    for col in range(2, n):
        for row in range(2):
            if row == 0:
                sticker[row][col] += max(sticker[row + 1][col - 1], sticker[row + 1][col - 2])
            else:
                sticker[row][col] += max(sticker[row - 1][col - 1], sticker[row - 1][col - 2])
    print(max(sticker[0][n - 1], sticker[1][n - 1]))
