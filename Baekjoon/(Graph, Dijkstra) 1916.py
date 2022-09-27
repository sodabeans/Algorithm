import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
costs = [[10000000001 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    i, j, cost = map(int, input().split())
    costs[i - 1][j - 1] = cost
    costs[j - 1][i - 1] = cost

start, end = map(int, input().split())
start -= 1
end -= 1

visited = [False for _ in range(N)]
ans = costs[start].copy()
visited[start] = True

for _ in range(N):
    curr = ans.index(min(ans))
    visited[curr] = True
    for idx in range(N):
        if not visited[idx]:
            ans[idx] = min(costs[curr][idx] + ans[curr], ans[idx])
print(ans[end])
