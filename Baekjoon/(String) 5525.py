import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()

ans = 0
target = 'I'

for _ in range(N):
    target += 'OI'

limit = len(target)

for idx in range(M - limit + 1):
    if S[idx:idx + limit] == target:
        ans += 1

print(ans)
