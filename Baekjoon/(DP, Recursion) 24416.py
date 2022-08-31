import sys
input = sys.stdin.readline


def recursion_fibonacci(num):
    if num == 1 or num == 2:
        return 1
    else:
        return recursion_fibonacci(num - 1) + recursion_fibonacci(num - 2)


n = int(input())
dp = [0 for _ in range(n)]
print(f'{recursion_fibonacci(n)} {n - 2}')
