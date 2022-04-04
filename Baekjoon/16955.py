from collections import deque
import sys
input = sys.stdin.readline

chessboard = list()
directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]

for i in range(10):
    row = list(input())
    chessboard.append(row)

queue = deque()
answer = 0

for i in range(10):
    for j in range(10):
        if chessboard[i][j] == 'X':
            queue.append([i, j])

while queue:
    row, col = queue.popleft()
    for i in range(8):
        x_cnt = 0
        dot_cnt = 0
        dr, dc = directions[i]
        for j in range(5):
            new_r = row + (dr * j)
            new_c = col + (dc * j)
            if 0 <= new_r < 10 and 0 <= new_c < 10:
                if chessboard[new_r][new_c] == '.':
                    dot_cnt += 1
                elif chessboard[new_r][new_c] == 'X':
                    x_cnt += 1
            if dot_cnt >= 2:
                break
            if x_cnt == 4 and dot_cnt == 1:
                print("1")
                sys.exit()

print(answer)

