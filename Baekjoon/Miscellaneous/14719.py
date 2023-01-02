import sys
input = sys.stdin.readline

H, W = map(int, input().split())
blocks = list(map(int, input().split()))
max_H = max(blocks)
max_H_idx = blocks.index(max_H)
ans = 0

for i in range(0, max_H_idx):
    if blocks[i] > blocks[i + 1]:
        ans += blocks[i] - blocks[i + 1]
        blocks[i + 1] = blocks[i]

for i in range(W - 1, max_H_idx, -1):
    if blocks[i] > blocks[i - 1]:
        ans += blocks[i] - blocks[i - 1]
        blocks[i - 1] = blocks[i]

print(ans)
