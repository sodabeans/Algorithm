def solution(n, results):
    answer = 0
    visited = [0] * n
    graph = [[0] * n for _ in range(n)]
    for a, b in results:
        graph[a - 1][b - 1] = 1
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if graph[j][i] and graph[i][k]:
                    graph[j][k] = 1
    visited = [0] * n
    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                visited[i] += 1
            if graph[j][i]:
                visited[i] += 1
    return visited.count(n - 1)
