import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = [input().rstrip() for _ in range(N)]
ans = 0

for _ in range(M):
    curr = input().rstrip()
    if curr in S:
        ans += 1

print(ans)
