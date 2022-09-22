import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()
ans = 0
idx = 0
ioi_cnt = 0

while idx < M - 1:
    if S[idx:idx+3] == "IOI":
        ioi_cnt += 1
        idx += 2
        if ioi_cnt == N:
            ioi_cnt -= 1
            ans += 1
    else:
        idx += 1
        ioi_cnt = 0

print(ans)
