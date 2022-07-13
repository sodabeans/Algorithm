import sys
input = sys.stdin.readline

T = int(input())

p = [0] * 101
p[1] = 1
p[2] = 1
p[3] = 1

for idx in range(4, 101):
    p[idx] = p[idx - 2] + p[idx - 3]

for _ in range(T):
    N = int(input())
    print(p[N])
