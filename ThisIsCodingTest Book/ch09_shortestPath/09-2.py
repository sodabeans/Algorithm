import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
N, M = map(int, input().split())
start = int(input())
graph = [[] for _ in range(N + 1)]
distance = [INF for _ in range(N + 1)]

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        curr_distance, curr = heapq.heappop(queue)
        if distance[curr] >= curr_distance:
            for i in graph[curr]:
                curr_cost = curr_distance + i[1]
                if curr_cost < distance[i[0]]:
                    distance[i[0]] = curr_cost
                    heapq.heappush(queue, (curr_cost, i[0]))


dijkstra(start)

for i in range(1, N + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
