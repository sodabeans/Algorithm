import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visitor = list(map(int, input().split()))

if max(visitor) == 0:
    print('SAD')
    exit()

cnt = 1
max_visitor = sum(visitor[0:X])
window_sum = max_visitor

for i in range(1, N - X + 1):
    # 시간초과 1 (range는 0부터)
    # window_sum = sum(visitor[i:i + X])

    # 시간초과 2 (range는 0부터)
    # window_sum = 0
    # for idx in range(i, i + X):
    #     window_sum += visitor[idx]

    # 정답 코드
    window_sum = window_sum - visitor[i-1] + visitor[i+X-1]
    if max_visitor < window_sum:
        max_visitor = window_sum
        cnt = 1
    elif max_visitor == window_sum:
        cnt += 1

print(max_visitor)
print(cnt)
