import sys
input = sys.stdin.readline

N = int(input())
edges = list(map(int, input().split()))
liters = list(map(int, input().split()))
min_liter = liters[0]
ans = 0

for idx in range(N-1):
    min_liter = min(min_liter, liters[idx])
    ans += min_liter * edges[idx]

print(ans)
