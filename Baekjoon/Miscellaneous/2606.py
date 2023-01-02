from collections import deque
import sys
input = sys.stdin.readline

N = int(input())  # number of computers
M = int(input())  # number of pairs
graph = [list(map(int, input().split())) for _ in range(M)]
visited = [False for _ in range(N + 1)]
queue = deque()
queue.append(1)
visited[1] = True
cnt = 0

while queue:
    node = queue.popleft()
    for g, h in graph:
        if g == node and not visited[h]:
            queue.append(h)
            visited[h] = True
            cnt += 1
        if h == node and not visited[g]:
            queue.append(g)
            visited[g] = True
            cnt += 1

print(cnt)
