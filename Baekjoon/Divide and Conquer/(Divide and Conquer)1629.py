import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())


def funct(num1, num2):
    if num2 == 1:
        return num1 % C
    else:
        tmp = funct(num1, num2 // 2)
        if num2 % 2:
            return num1 * tmp * tmp % C
        else:
            return tmp * tmp % C


print(funct(A, B))
