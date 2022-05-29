import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(M)]


def BellmanFord(start):
    distance = [float('inf') for _ in range(N+1)]
    flag = [False for _ in range(N+1)]
    distance[start] = 0

    for i in range(M):
        for [A, B, C] in graph:
            if distance[A] != float("inf") and distance[A] + C < distance[B]:
                distance[B] = distance[A] + C

    for [A, B, C] in graph:
        if distance[A] + C < distance[B]:
            print(-1)
            exit()

    for i in range(2, N+1):
        if distance[i] == float('inf'):
            print(-1)
        else:
            print(distance[i])


BellmanFord(1)
