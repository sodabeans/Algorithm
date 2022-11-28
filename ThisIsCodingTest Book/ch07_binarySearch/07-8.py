import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lengths = list(map(int, input().split()))
start = 0
end = max(lengths)
answer = 0

while start <= end:
    curr_cnt = 0
    mid = (start + end) // 2
    for l in lengths:
        if l > mid:
            curr_cnt += l - mid
    if curr_cnt < M:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)
