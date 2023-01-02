from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
get_graph = {key: [] for key in range(1, N + 1)}

for _ in range(M):
    node_1, node_2 = map(int, input().split())
    if node_2 not in get_graph[node_1]:
        get_graph[node_1].append(node_2)
    if node_1 not in get_graph[node_2]:
        get_graph[node_2].append(node_1)


def bfs(graph, root):
    visited = []
    queue = deque()
    queue.append(root)
    while queue:
        curr = queue.popleft()
        if curr not in visited:
            visited.append(curr)
            graph[curr] = sorted(graph[curr])
            queue += graph[curr]
    print(" ".join(map(str, visited)))


def dfs(graph, root):
    visited = []
    queue = [root]
    while queue:
        curr = queue.pop()
        if curr not in visited:
            visited.append(curr)
            queue += sorted(graph[curr], reverse=True)
    print(" ".join(map(str, visited)))


dfs(get_graph, V)
bfs(get_graph, V)
