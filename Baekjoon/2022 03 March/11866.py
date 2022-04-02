import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
series = deque()
answer = list()

for i in range(1, N+1):
    series.append(i)

while series:
    for _ in range(K):
        series.append(series.popleft())
    answer.append(series.pop())

print("<", end="")
print(str(answer).lstrip("[").rstrip("]"), end="")
print(">", end="")
