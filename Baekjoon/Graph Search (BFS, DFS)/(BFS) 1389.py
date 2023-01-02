from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
users = {key: [] for key in [i for i in range(N)]}
ans = [0 for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    users[A - 1].append(B - 1)
    users[B - 1].append(A - 1)

ans_cnt = 500000
ans_idx = 0

for curr in range(N):
    visited = [0 for _ in range(N)]
    visited[curr] = 1
    queue = deque()
    queue.append((curr, users[curr]))
    while queue:
        idx, curr_friend = queue.popleft()
        for friend in curr_friend:
            if visited[friend] == 0:
                visited[friend] += visited[idx] + 1
                queue.append((friend, users[friend]))
    if sum(visited) < ans_cnt:
        ans_cnt = sum(visited)
        ans_idx = curr + 1

print(ans_idx)
