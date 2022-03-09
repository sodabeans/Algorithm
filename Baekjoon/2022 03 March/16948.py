import sys

n = int(sys.stdin.readline())
r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

r_directions = [-2, -2, 0, 0, 2, 2]
c_directions = [-1, 1, -2, 2, -1, 1]

graph = [[-1 for _ in range(n)] for _ in range(n)]
