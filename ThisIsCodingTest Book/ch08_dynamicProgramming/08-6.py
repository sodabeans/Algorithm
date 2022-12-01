import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
if N < 3:
    print(max(arr))
    exit()
dp = [0] * N
dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])
for i in range(2, N):
    dp[i] = max(arr[i - 2] + arr[i], arr[i - 1])

print(dp[N - 1])
