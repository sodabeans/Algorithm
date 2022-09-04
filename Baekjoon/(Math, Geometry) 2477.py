import sys
input = sys.stdin.readline

N = int(input())
lengths = []
max_w = 0
max_w_idx = 0
max_h = 0
max_h_idx = 0

for idx in range(6):
    direction, length = map(int, input().split())
    lengths.append(length)
    if direction == 1 or direction == 2:
        if max_w < length:
            max_w = length
            max_w_idx = idx
    else:
        if max_h < length:
            max_h = length
            max_h_idx = idx

small_w = abs(lengths[(max_w_idx - 1) % 6] - lengths[(max_w_idx + 1) % 6])
small_h = abs(lengths[(max_h_idx - 1) % 6] - lengths[(max_h_idx + 1) % 6])

print((max_w * max_h - small_w * small_h) * N)
