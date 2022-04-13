import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

low = 0
high = max(trees)

while low <= high:
    target = 0
    mid = (low + high) // 2
    for t in trees:
        if t > mid:
            target += t - mid
    if target < M:
        high = mid - 1
    elif target >= M:
        low = mid + 1

print(low - 1)
