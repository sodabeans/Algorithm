import heapq

def solution(n, costs):
    answer = 0
    nodes = [[] for i in range(n)]
    visited = []
    
    for a, b, c in costs:
        nodes[b].append((c, a))
        nodes[a].append((c, b))
    
    min_heap = [(0, 0)]
    heapq.heapify(min_heap)
    
    while min_heap:
        curr_cost, curr_node = heapq.heappop(min_heap)
        if curr_node not in visited:
            visited.append(curr_node)
            answer += curr_cost
            for cost, neighbor in nodes[curr_node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (cost, neighbor))
    
    return answer
