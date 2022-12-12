import sys
input = sys.stdin.readline

INF = int(1e9)
N = int(input())
M = int(input())

graph = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    graph[i][i] = 0

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a][b] = cost

for x in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][x] + graph[x][j])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j] == INF:
            print("INFINITY", end=' ')
        else:
            print(graph[i][j], end=' ')
    print()