from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
A, B = map(int, input().split())
m = int(input())

relation = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    relation[x].append(y)
    relation[y].append(x)

visited = [0] * (n + 1)
queue = deque()
queue.append(A)
while queue:
    curr = queue.popleft()
    if curr == B:
        break
    for element in relation[curr]:
        if visited[element] == 0:
            visited[element] = visited[curr] + 1
            queue.append(element)

if visited[B] == 0:
    print("-1")
else:
    print(visited[B])
