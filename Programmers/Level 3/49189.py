def solution(n, edge):
    graph = [[] for _ in range(n)]
    visited = [0] * n
    distance = [float('inf')] * n
    for a, b in edge:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    queue = [0]
    distance[0] = 0
    while queue:
        curr = queue.pop(0)
        visited[curr] = 1
        for neighbor in graph[curr]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                distance[neighbor] = min(distance[curr] + 1, distance[neighbor])
                queue.append(neighbor)
    
    return distance.count(max(distance))
