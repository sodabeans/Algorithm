import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
distance = [100000000000 for _ in range(V + 1)]

start = int(input())
for _ in range(E):
    u, w, v = map(int, input().split())
    graph[u].append([w, v])


def dijkstra(start_node):
    queue = []
    heapq.heappush(queue, (0, start_node))
    while queue:
        curr_distance, curr_node = heapq.heappop(queue)
        if distance[curr_node] < curr_distance:
            continue
        for next_one in graph[curr_node]:
            next_node, next_distance = next_one[0], next_one[1]
            next_distance += curr_distance
            if distance[next_node] > next_distance:
                distance[next_node] = next_distance
                heapq.heappush(queue, (next_distance, next_node))


dijkstra(start)
for idx in range(1, V + 1):
    if idx == start:
        print(0)
        continue
    if distance[idx] == 100000000000:
        print("INF")
    else:
        print(distance[idx])
