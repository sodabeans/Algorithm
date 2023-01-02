import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    numerator = 1
    denominator = 1
    for i in range(1, min(N, M - N) + 1):
        numerator *= M
        denominator *= i
        M -= 1
    print(numerator // denominator)
