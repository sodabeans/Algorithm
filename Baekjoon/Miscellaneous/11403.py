# memory: 30864 KB
# time: 300 ms

import sys

N = int(sys.stdin.readline())
graph = [] # initiate graph

for i in range(N):
    graph.append([int(x) for x in sys.stdin.readline().split()])

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]: # if path exists
                graph[i][j] = 1 # make "True" (which is 1 in this case)

for i in range(N):
    for j in range(N):
        if j == N - 1:
            print(graph[i][j]) # if it is last element of a row
        else: 
            print(graph[i][j], end=" ")
