import sys
input = sys.stdin.readline

INF = int(1e9)
N, M = map(int, input().split())
start = int(input())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
distance = [INF for _ in range(N + 1)]

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))


def get_smallest_node():
    min_value = INF
    idx = 0
    for i in range(1, N + 1):
        if distance[i] < min_value and visited[i] == 0:
            min_value = distance[i]
            index = i
    return i


def dijkstra(start):
    distance[start] = 0
    visited[start] = 1
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(N + 1):
        curr = get_smallest_node()
        visited[curr] = 1
        for j in graph[curr]:
            cost = distance[curr] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)

for i in range(1, N + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
