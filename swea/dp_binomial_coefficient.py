T = int(input())

dp = [[0 for _ in range(71)] for _ in range(71)]

for test_case in range(1, T + 1):
    n, a, b = map(int, input().split())
    for i in range(n + 1):
        for j in range(min(n, b) + 1):
            if dp[i][j] == 0:
                if j == 0 or i == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    print(f"#{test_case} {dp[n][b]}")