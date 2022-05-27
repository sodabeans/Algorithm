import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(M)]


def BellmanFord(start):
    distance = [float('inf') for _ in range(N)]
    distance[start] = 0

    for i in range(M):
        for [A, B, C] in graph:
            if distance[A] != float("inf") and distance[A] + C < distance[B]:
                distance[B] = distance[A] + C

    for [A, B, C] in graph:
        if distance[A] != float("inf") and distance[A] + C < distance[B]:
            distance[B] = -1

    for i in range(N):
        print(distance[i])


BellmanFord(1)
