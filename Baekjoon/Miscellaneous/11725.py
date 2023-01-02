from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]
answer = [0 for _ in range(N + 1)]

# connect nodes to each other, unrooted
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

nodes = deque()
nodes.append(1)

while nodes:
    parent = nodes.popleft()
    for p in tree[parent]:
        if answer[p] == 0: # initialized as 0, so 0 is not visited
            answer[p] = parent
            nodes.append(p)

for i in range(2, N + 1):
    print(answer[i])

"""
# 시간 초과

# check parent node starting from 1
visited = [1]

while(len(visited) < N):
    for node in visited:
        for t in tree[node]:
            if t not in visited:
                visited.append(t)
                parent[t] = node
"""
