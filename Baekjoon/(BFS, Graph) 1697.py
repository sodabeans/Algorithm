from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

visited = [0] * 100001

queue = deque()
queue.append(N)

while queue:
    curr_x = queue.popleft()
    new_x = [curr_x - 1, curr_x + 1, curr_x * 2]
    if curr_x < 0 or curr_x > 100000:
        continue
    if curr_x == K:
        print(visited[curr_x])
        exit()
    for next_x in new_x:
        if 0 <= next_x <= 100000 and visited[next_x] == 0:
            visited[next_x] = visited[curr_x] + 1
            queue.append(next_x)
