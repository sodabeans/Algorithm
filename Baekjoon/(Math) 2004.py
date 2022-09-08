import sys
input = sys.stdin.readline

n, m = map(int, input().split())
m = min(m, n - m)
numerator = 1
denominator = 1
for idx in range(1, m + 1):
    numerator *= n - idx + 1
    denominator *= idx
target = numerator // denominator

ans = 0
while True:
    if target % 10 == 0:
        target = target // 10
        ans += 1
    else:
        print(ans)
        break
