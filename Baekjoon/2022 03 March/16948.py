# memory: 32420 KB
# time: 112 ms

from collections import deque
import sys

def bfs():
    queue = deque()
    queue.append((r1, c1))
    graph[r1][c1] = 0 # starting position

    while queue:
        r, c = queue.popleft()
        for (r_direction, c_direction) in directions:
            r_next = r + r_direction
            c_next = c + c_direction
            if 0 <= r_next < n and 0 <= c_next < n and graph[r_next][c_next] == -1: # if in range and not visited
                graph[r_next][c_next] = graph[r][c] + 1
                if r_next == r2 and c_next == c2:
                    break
                queue.append((r_next, c_next)) # next position to queue

    return graph[r2][c2]
    

n = int(sys.stdin.readline())
r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

directions = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

graph = [[-1] * n for _ in range(n)]

print(bfs())
