T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    objects = [list(map(int, input().split())) for _ in range(M)]
    dp = [[0 for _ in range(N + 1)] for _ in range(M + 1)]

    for i in range(0, M):
        size, price = objects[i]
        for idx in range(1, N + 1):
            if size > idx:
                dp[i + 1][idx] = dp[i][idx]
            else:
                dp[i + 1][idx] = max(dp[i][idx - size] + price, dp[i][idx])
    print(f"#{test_case} {dp[-1][-1]}")
