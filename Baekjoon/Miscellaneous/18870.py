import sys
input = sys.stdin.readline

N = int(input())
coord = list(map(int, input().split()))
ans = [0 for _ in range(N)]
test = {}

for i in range(N):
    if coord[i] in test:
        test[coord[i]].append(i)
    else:
        test[coord[i]] = [i]
test = sorted(test.items())

cnt = 0
for key, value in test:
    for idx in value:
        ans[idx] = cnt
    cnt += 1

print(*ans, sep=' ')
