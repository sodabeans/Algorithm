from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
card = deque()

for i in range(1, N + 1):
    card.append(i)

while (len(card) > 1):
    if cnt % 2:
        card.append(card.popleft())
    else:
        card.popleft()
    cnt += 1

print(card.popleft())