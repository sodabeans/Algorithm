import sys
input = sys.stdin.readline

position = input()
row = int(ord(position[0])) - 96
col = int(position[1])

directions = [(2, 1), (-2, -1), (1, 2), (-1, -2), (2, -1), (-2, 1), (1, -2), (-1, 2)]
answer = 0

for idx in range(len(directions)):
    dr, dc = directions[idx]
    new_row = row + dr
    new_col = col + dc
    if 0 < new_row <= 8 and 0 < new_col <= 8:
        answer += 1

print(answer)
