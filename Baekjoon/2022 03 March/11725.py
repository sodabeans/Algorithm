"""
# 시간 초과

import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)

# connect nodes to each other, unrooted
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# check parent node starting from 1
visited = [1]

while(len(visited) < N):
    for node in visited:
        for t in tree[node]:
            if t not in visited:
                visited.append(t)
                parent[t] = node

for i in range(2, N + 1):
    print(parent[i])
"""
