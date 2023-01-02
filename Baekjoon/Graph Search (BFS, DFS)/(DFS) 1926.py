import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
total_cnt = 0
area = 0
largest_area = 0


def search(x, y):
    global area
    if 0 <= x < N and 0 <= y < M and paper[x][y] == 1:
        paper[x][y] = 0
        area += 1
        for idx in range(4):
            dx, dy = directions[idx]
            search(x + dx, y + dy)
        return True
    return False


for i in range(N):
    for j in range(M):
        if search(i, j):
            largest_area = max(largest_area, area)
            total_cnt += 1
            area = 0


print(total_cnt)
print(largest_area)
