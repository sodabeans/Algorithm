import sys
input = sys.stdin.readline

E, S, M = map(int, input().split())
E_cnt, S_cnt, M_cnt = 1, 1, 1
ans = 1

while True:
    if E == E_cnt and S == S_cnt and M == M_cnt:
        break
    E_cnt += 1
    S_cnt += 1
    M_cnt += 1
    ans += 1
    if E_cnt > 15:
        E_cnt = 1
    if S_cnt > 28:
        S_cnt = 1
    if M_cnt > 19:
        M_cnt = 1

print(ans)