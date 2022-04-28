from collections import deque
import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
belt = deque()
for _ in range(N):
    belt.append(int(input()))

ans = 0

for i in range(N):
    curr_dish = belt[] + [c]
    curr_kinds = 1
    for j in range(k):
        curr = belt.popleft()
        belt.append(curr)
        if curr not in curr_dish:
            curr_dish.append(curr)
            curr_kinds += 1
    if curr_kinds > ans:
        ans = curr_kinds
    if ans == d + 1:  # reach maximum kinds
        break

print(ans)