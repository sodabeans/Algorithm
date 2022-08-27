import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temperature = list(map(int, input().split()))
prev = sum(temperature[0:K])
curr = prev
ans = prev

for idx in range(N - K):
    prev = curr
    curr = prev - temperature[idx] + temperature[idx + K]
    ans = max(ans, curr)

print(ans)
