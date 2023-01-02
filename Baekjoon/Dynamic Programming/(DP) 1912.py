import sys
input = sys.stdin.readline

n = int(input())
series = list(map(int, input().split()))

for idx in range(1, n):
    series[idx] = max(series[idx - 1] + series[idx], series[idx])

print(max(series))
