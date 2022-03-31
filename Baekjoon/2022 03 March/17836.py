from collections import deque
import sys
input = sys.stdin.readline

N, M, T = map(int, input().rstrip().split())

# available movements
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

answer = 0

# get input
castle = list()
for _ in range(N):
    castle.append(list(map(int, input().rstrip().split())))

# list to check if block is visited
visited = [[[0 for _ in range(2)] for _ in range(M)] for _ in range(N)]

# bfs
queue = deque()
queue.append((0, 0, 0, 1))

# starting position visited
visited[0][0][0] = 1

while queue:
    r, c, gram, cnt = queue.popleft()

    # if gram is on current block
    if castle[r][c] == 2:
        gram = 1
        visited[r][c][gram] += 1

    # if reached destination
    if r == N - 1 and c == M - 1:
        # subtract 1 because starting position was also counted
        answer = cnt - 1
        break

    # checking each up, down, left, right blocks
    for (dr, dc) in directions:
        next_r = r + dr
        next_c = c + dc
        # if gram is found
        if gram == 1:
            # if in castle boundary and not yet visited
            if 0 <= next_r < N and 0 <= next_c < M and visited[next_r][next_c][gram] == 0:
                visited[next_r][next_c][gram] = cnt + 1
                queue.append((next_r, next_c, gram, cnt + 1))
        # if gram is not found
        else:
            # if in castle boundary, not a wall, and not yet visited
            if 0 <= next_r < N and 0 <= next_c < M and visited[next_r][next_c][gram] == 0 and castle[next_r][next_c] != 1:
                visited[next_r][next_c][gram] = cnt + 1
                queue.append((next_r, next_c, gram, cnt + 1))

if 0 < answer <= T:
    print(answer)
else:
    print("Fail")
