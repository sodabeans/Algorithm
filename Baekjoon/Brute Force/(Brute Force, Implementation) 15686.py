from itertools import combinations
import sys
input = sys.stdin.readline


def distance(h, c):
    return abs(h[0] - c[0]) + abs(h[1] - c[1])


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
house = []
chicken = []
answer = 100000001

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])

for option in combinations(chicken, M):
    curr_total = 0
    for idx in range(len(house)):
        tmp = 100000001
        for opt in option:
            tmp = min(tmp, distance(house[idx], opt))
        curr_total += tmp
    answer = min(answer, curr_total)
print(answer)
