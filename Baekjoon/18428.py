from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

hall = list(list(input().rstrip().split()) for _ in range(N))
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

queue = deque()
for i in range(N):
    for j in range(N):
        if hall[i][j] == 'T':
            queue.append([i, j])

while queue:
    row, col = queue.popleft()
    for i in range(4):
        dr, dc = directions[i]
        new_r = row + dr
        new_c = col + dc
        if 0 <= new_r < N and 0 <= new_c < N:
            if new_r == row or new_c == col:
                if hall[new_r][new_c] == 'X':
                    hall[new_r][new_c] = 'O'
                    queue.append([new_r, new_c])
                elif hall[new_r][new_c] == 'S':
                    queue.append([new_r, new_c])

obstacle_cnt = 0

for i in range(N):
    for j in range(N):
        if hall[i][j] == 'O':
            obstacle_cnt += 1
            if obstacle_cnt > 3:
                print("NO")
                exit()

print("YES")