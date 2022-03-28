import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

heights = [list(map(int, input().rstrip().split())) for _ in range(N)]
heights = sum(heights, [])

heights.sort()
curr_height = heights[0]
max_height = heights[-1]
changes = list()

while curr_height <= max_height:
    inventory = B
    change_cnt = 0
    time = 0
    for i in range(N * M):
        if heights[i] > curr_height:
            inventory = inventory + heights[i] - curr_height
            time += 2
        elif heights[i] < curr_height:
            inventory = inventory - (heights[i] - curr_height)
            time += 1

    if inventory >= 0:
        changes.append((time, curr_height))
    curr_height += 1

changes.sort()

ans_time, ans_height = changes[0]
print(f'{ans_time} {ans_height}')


