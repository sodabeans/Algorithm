def dfs(curr, graph, visited):
    visited[curr] = True
    cnt = 1
    for node in graph[curr]:
        if not visited[node]:
            visited[node] = True
            cnt += dfs(node, graph, visited)
    return cnt

def solution(n, wires):
    answer = n
    
    wire_tree = [[] for _ in range(n + 1)]
    
    for a, b in wires:
        wire_tree[a].append(b)
        wire_tree[b].append(a)
    for a, b, in wires:
        wire_tree[a].remove(b)
        wire_tree[b].remove(a)
        visited = [False] * (n + 1)
        curr_length = dfs(a, wire_tree, visited)
        # other_length = n - curr_length
        # difference = abs(n - curr_length * 2)
        # print(curr_length)
        answer = min(answer, abs(n - curr_length * 2))
        wire_tree[a].append(b)
        wire_tree[b].append(a)
    
    return answer
