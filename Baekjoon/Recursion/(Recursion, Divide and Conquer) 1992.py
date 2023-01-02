import sys
input = sys.stdin.readline

N = int(input())
image = [list(map(int, input().rstrip())) for _ in range(N)]


def compression(x, y, length):
    for a in range(x, x + length):
        for b in range(y, y + length):
            if image[a][b] != image[x][y]:
                print("(", end='')
                compression(x, y, length // 2)
                compression(x, y + length // 2, length // 2)
                compression(x + length // 2, y, length // 2)
                compression(x + length // 2, y + length // 2, length // 2)
                print(")", end='')
                return

    print(str(image[x][y]), end='')


compression(0, 0, N)
