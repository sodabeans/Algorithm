import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ans = 0

# code from book
while True:
    tmp = (N // K) * K
    ans = ans + N - tmp
    N = tmp
    if N < K:
        break
    N = N // K
    ans += 1
ans += (N - 1)
###

# my code
# ans = (N % K)
# N = N - ans
# while N > 1:
#     N = N // K
#     ans += 1

print(ans)
