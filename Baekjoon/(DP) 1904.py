import sys
input = sys.stdin.readline

N = int(input())
first, second = 1, 1
ans = 1

for i in range(2, N + 1):
    ans = (first + second) % 15746
    first = second
    second = ans
print(ans)
