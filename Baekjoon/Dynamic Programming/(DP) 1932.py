import sys
input = sys.stdin.readline

row = int(input())
triangle = [list(map(int, input().split())) for _ in range(row)]

for i in range(row - 1, -1, -1):
    for j in range(i):
        left = triangle[i][j]
        right = triangle[i][j + 1]
        if left >= right:
            triangle[i - 1][j] += left
        else:
            triangle[i - 1][j] += right

print(triangle[0][0])
