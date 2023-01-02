# memory: 30864 KB
# time: 88 ms

import sys

n, m = map(int, sys.stdin.readline().split())
matrix = list()
for _ in range(n):
    matrix.append(sys.stdin.readline())

cnt_list = list()

def wb_cnt(x, y):
    b_cnt = 0
    w_cnt = 0
    for a in range(x, x + 8):
        for b in range(y, y + 8):
            if (a + b) % 2: # (0, 1), (0, 3), ... and (1, 0), (1, 2), ... and (2, 1), (2, 3), ...
                if matrix[a][b] != 'W':
                    b_cnt = b_cnt + 1
                else:
                    w_cnt = w_cnt + 1
            else: # (0, 0), (0, 2), ... and (1, 1), (1, 3), ... and (2, 0), (2, 2), ...
                if matrix[a][b] != 'B': # if not B
                    b_cnt = b_cnt + 1 # counting num of changes when compared to chessboard starting with B
                else:
                    w_cnt = w_cnt + 1
    return b_cnt, w_cnt
                    
for i in range(n - 7):
    for j in range(m - 7):
        b, w = wb_cnt(i, j)
        cnt_list.append(w)
        cnt_list.append(b)

print(min(cnt_list))
        
