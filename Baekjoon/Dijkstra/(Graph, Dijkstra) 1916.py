import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
ans = [1000000001 for _ in range(N + 1)]

for _ in range(M):
    tmp_start, tmp_end, tmp_distance = map(int, input().split())
    graph[tmp_start].append([tmp_end, tmp_distance])

start, end = map(int, input().split())


def dijkstra(start_node):
    queue = []
    heapq.heappush(queue, (0, start_node))
    ans[start_node] = 0
    while queue:
        curr_distance, curr = heapq.heappop(queue)
        if ans[curr] < curr_distance:
            continue
        for next_info in graph[curr]:
            next_node = next_info[0]
            next_distance = next_info[1]
            next_distance += curr_distance
            if ans[next_node] > next_distance:
                ans[next_node] = next_distance
                heapq.heappush(queue, (next_distance, next_node))


dijkstra(start)
print(ans[end])
