from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
trials = list(permutations([i for i in range(N)], N))
ans = 0
for t in trials:
    total = 0
    for idx in range(1, N):
        total += abs(A[t[idx - 1]] - A[t[idx]])
    ans = max(ans, total)
print(ans)
