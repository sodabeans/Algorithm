import sys
input = sys.stdin.readline

n, m = map(int, input().split())
m = min(m, n - m)
cnt_2 = 0
cnt_5 = 0

for idx in range(1, m + 1):
    upper = n - idx + 1
    lower = idx
    while True:
        if upper % 2 == 0:
            upper = upper // 2
            cnt_2 += 1
        elif upper % 5 == 0:
            upper = upper // 5
            cnt_5 += 1
        else:
            break
    while True:
        if lower % 2 == 0:
            lower = lower // 2
            cnt_2 -= 1
        elif lower % 5 == 0:
            lower = lower // 5
            cnt_5 -= 1
        else:
            break

print(min(cnt_2, cnt_5))
