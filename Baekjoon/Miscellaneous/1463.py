# memory: 38676 KB
# time: 608 ms

import sys

N = int(sys.stdin.readline())

dp = [0] * (N + 1)

for i in range(2, N + 1):
    dp[i] = dp[i-1] + 1 # case 3
    if (i % 2 == 0):
        # error message: "TypeError: list indices must be integers or slices, not float"
        dp[i] = min(dp[i], dp[i // 2] + 1) # // is integer division
    if (i % 3 == 0):
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])
