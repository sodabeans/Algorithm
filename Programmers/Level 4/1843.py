def solution(arr):
    N = len(arr) // 2 + 1
    digits = [int(arr[i]) for i in range(0, len(arr), 2)]
    operands = [arr[i] for i in range(1, len(arr), 2)]
    dp_min = [[float('inf')] * N for _ in range(N)]
    dp_max = [[float('-inf')] * N for _ in range(N)]

    for i in range(N):
        dp_min[i][i] = digits[i]
        dp_max[i][i] = digits[i]

    for length in range(2, N + 1):
        for i in range(N - length + 1):
            j = i + length - 1
            for k in range(i, j):
                if operands[k] == '+':
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k + 1][j])
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_min[k + 1][j])
                elif operands[k] == '-':
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] - dp_max[k + 1][j])
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] - dp_min[k + 1][j])

    return dp_max[0][N - 1]