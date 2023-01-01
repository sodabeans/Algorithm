from collections import deque
import sys
input = sys.stdin.readline

dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]
T = int(input())
for _ in range(T):
    N = int(input())
    start_x, start_y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())
    graph = [[0 for _ in range(N)] for _ in range(N)]
    graph[start_x][start_y] = 1
    queue = deque([[start_x, start_y]])
    while queue:
        curr_x, curr_y = queue.popleft()
        for idx in range(8):
            new_x = curr_x + dx[idx]
            new_y = curr_y + dy[idx]
            if 0 <= new_x < N and 0 <= new_y < N and graph[new_x][new_y] == 0:
                graph[new_x][new_y] = graph[curr_x][curr_y] + 1
                queue.append([new_x, new_y])
    print(graph[goal_x][goal_y] - 1)
