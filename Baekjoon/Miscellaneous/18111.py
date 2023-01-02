import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())  # row, column, blocks
ground = list(list(map(int, input().split())) for _ in range(N))  # starting ground heights

ans_time = 1000000000
ans_height = 0

for curr_height in range(257):  # maximum height is 256
    remove_cnt = 0
    add_cnt = 0
    for i in range(N):
        for j in range(M):
            if ground[i][j] > curr_height:  # remove. add to inventory. 2 sec
                remove_cnt += ground[i][j] - curr_height
            else:  # add. remove from inventory. 1 sec
                add_cnt -= ground[i][j] - curr_height  # negative number, so subtract

    if remove_cnt + B >= add_cnt:
        curr_time = remove_cnt * 2 + add_cnt
        if curr_time <= ans_time:  # if time is shorter or same
            ans_height = curr_height   # if same time, answer should update to higher height
            ans_time = curr_time

print(f'{ans_time} {ans_height}')
