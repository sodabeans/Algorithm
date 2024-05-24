from collections import deque


def solution(n, computers):
    answer = 0
    nodes = [[] for _ in range(n)]
    visited = [False] * n
    
    for i in range(n):
        for j in range(i + 1, n):
            if computers[i][j] == 1:
                nodes[i].append(j)
                nodes[j].append(i)
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            queue = deque()
            queue.append(i)
            while queue:
                curr = queue.popleft()
                visited[curr] = True
                for node in nodes[curr]:
                    if not visited[node]:
                        queue.append(node)
            answer += 1
    
    return answer
