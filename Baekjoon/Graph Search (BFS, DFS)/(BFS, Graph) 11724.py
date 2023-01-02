from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
ans = 0

for _ in range(M):
    node_1, node_2 = map(int, input().split())
    edges[node_1].append(node_2)
    edges[node_2].append(node_1)

for node in range(1, N + 1):
    if visited[node] == 0:
        queue = deque()
        queue.append(node)
        while queue:
            curr_node = queue.popleft()
            for next_node in edges[curr_node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)
        ans += 1

print(ans)
