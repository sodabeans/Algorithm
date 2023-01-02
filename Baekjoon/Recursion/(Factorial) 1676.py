import sys
input = sys.stdin.readline


def factorial(num):
    if num == 1 or num == 0:
        return 1
    return factorial(num - 1) * num


ans = 0
result = factorial(int(input()))
while True:
    if result % 10 == 0:
        result = result // 10
        ans += 1
    else:
        print(ans)
        break
