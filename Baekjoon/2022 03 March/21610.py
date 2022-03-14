# memory: 32452 KB
# time: 580 ms

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# starting positions of cloud
cloud = deque([[N - 2, 0], [N - 2, 1], [N - 1, 0], [N - 1, 1]])

# possible directions for d_i (diagonals are idx = 1, 3, 5, 7)
directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

for i in range(M):
    d_i, s_i = map(int, sys.stdin.readline().split())
    d_ir, d_ic = directions[d_i - 1]
    length = len(cloud)
    visited = [[False] * N for _ in range(N)]
    
    while length:
        # for each cloud block...
        curr_r, curr_c = cloud.popleft()
        # move cloud s_i times in d_i direction
        curr_r = (N + curr_r + (d_ir * s_i)) % N
        curr_c = (N + curr_c + (d_ic * s_i)) % N
        cloud.append([curr_r, curr_c])
        length -= 1
    
    for [r, c] in cloud:
        # add 1, and add this block to visited clouds
        visited[r][c] = True
        A[r][c] += 1
    
    # for each cloud, if there is a block in diagonal direction with water, add 1 to current block
    for [r, c] in cloud:
        for x in range(1, 8, 2):
            d_r, d_c = directions[x]
            if 0 <= r + d_r < N and 0 <= c + d_c < N and A[r + d_r][c + d_c]:
                A[r][c] += 1
    
    # cloud disappears
    cloud = deque()

    # excluding visited blocks, blocks with more than 2 have clouds and -2
    for k in range(N):
        for j in range(N):
            if A[k][j] >= 2 and not visited[k][j]:
                A[k][j] -= 2
                cloud.append([k, j])

print(sum(sum(row) for row in A))
