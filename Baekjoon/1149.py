from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
houses = deque()

for _ in range(N):
    r, g, b = map(int, input().split())
    houses.append([r, g, b])

for i in range(1, N):
    houses[i][0] += min(houses[i - 1][1], houses[i - 1][2])
    houses[i][1] += min(houses[i - 1][0], houses[i - 1][2])
    houses[i][2] += min(houses[i - 1][0], houses[i - 1][1])

print(min(houses[-1]))
