import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# starting positions of cloud
cloud = deque([[N - 2, 0], [N - 2, 1], [N - 1, 0], [N - 1, 1]])

# possible directions for d_i
directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]


for i in range(M):
    d_i, s_i = map(int, sys.stdin.readline().split())
    d_ir, d_ic = directions[d_i - 1]
    length = len(cloud)
    next = []
    
    # for each cloud block...
    for i in range(length):
        curr_r, curr_c = cloud[i]
        # move cloud s_i times in d_i direction
        curr_r = (N + curr_r + (d_ir * s_i)) % N
        curr_c = (N + curr_c + (d_ic * s_i)) % N
        # add 1 and cloud disappears
        A[curr_r][curr_c] += 1
        cloud[i] = [curr_r, curr_c]

    # for each block, if there is a block in diagonal direction with water, add 1 to current block
    for [r, c] in cloud:
        # left-up diagonal
        if 0 <= r - 1 < N and 0 <= c - 1 < N and A[r - 1][c - 1]:
            A[r][c] += 1
        # right-up diagonal
        if 0 <= r - 1 < N and 0 <= c + 1 < N and A[r - 1][c + 1]:
            A[r][c] += 1
        # right-down diagonal
        if 0 <= r + 1 < N and 0 <= c + 1 < N and A[r + 1][c + 1]:
            A[r][c] += 1
        # left-down diagonal
        if 0 <= r + 1 < N and 0 <= c - 1 < N and A[r + 1][c - 1]:
            A[r][c] += 1

    # excluding prev_clouds, blocks with more than 2 have clouds and -2
    for k in range(N):
        for j in range(N):
            if A[k][j] >= 2 and ([k, j] not in cloud):
                A[k][j] = A[k][j] - 2
                next.append([k, j])
    
    cloud.clear()
    cloud = next.copy()

print(sum(sum(A, [])))
