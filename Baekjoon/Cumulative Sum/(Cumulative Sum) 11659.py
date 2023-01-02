import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

for idx in range(1, N):
    numbers[idx] += numbers[idx - 1]

for _ in range(M):
    i, j = map(int, input().split())
    if i == 1:
        ans = numbers[j - 1]
    else:
        ans = numbers[j - 1] - numbers[i - 2]
    print(ans)
