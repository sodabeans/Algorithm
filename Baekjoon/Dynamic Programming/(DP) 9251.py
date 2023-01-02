import sys
input = sys.stdin.readline

str_one = input().rstrip()
str_two = input().rstrip()
dp = [[0 for _ in range(len(str_one) + 1)] for _ in range(len(str_two) + 1)]

for i in range(1, len(str_one) + 1):
    for j in range(1, len(str_two) + 1):
        if str_one[i - 1] == str_two[j - 1]:
            dp[j][i] = dp[j - 1][i - 1] + 1
        else:
            dp[j][i] = max(dp[j][i - 1], dp[j - 1][i])

print(dp[-1][-1])
