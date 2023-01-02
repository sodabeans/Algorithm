import sys
input = sys.stdin.readline

n, m = map(int, input().split())

limit = min(m, n - m)

dp = [1] * (limit + 1)

for i in range(1, limit + 1):
    dp[i] = dp[i - 1] * (n - i + 1) // i

print(dp[limit])

"""
# using recursion

def factorial(num):
    if num == 1 or num == 0:
        return 1
    return factorial(num - 1) * num


n, m = map(int, input().split())

answer = factorial(n) // (factorial(m) * factorial(n - m))

print(answer)
"""
