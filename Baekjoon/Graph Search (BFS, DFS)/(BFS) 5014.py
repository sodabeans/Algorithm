from collections import deque
import sys
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
visited = [0 for _ in range(F + 1)]
queue = deque([S])
visited[S] = 1

while queue:
    curr = queue.popleft()
    if curr == G:
        break
    new_up = curr + U
    new_down = curr - D
    if 0 < new_up < F + 1 and visited[new_up] == 0:
        visited[new_up] = visited[curr] + 1
        queue.append(new_up)
    if 0 < new_down < F + 1 and visited[new_down] == 0:
        visited[new_down] = visited[curr] + 1
        queue.append(new_down)

if visited[G]:
    print(visited[G] - 1)
else:
    print("use the stairs")
