import sys
input = sys.stdin.readline

N = int(input())
series = list(map(int, input().split()))
dp = [0] * (N + 1)
ans = 1

for i in range(1, N):
    if series[i - 1] >= series[i]:
        series[i] = series[i - 1]
    else:
        ans += 1

print(ans)