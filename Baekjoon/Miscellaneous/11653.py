import sys
input = sys.stdin.readline

N = int(input())

prime = [True for _ in range(10000001)]

p = 2
while p ** 2 <= 10000000:
    if prime[p]:
        for i in range(p ** 2, 10000001, p):
            prime[i] = False
    p += 1

i = 2
while N > 1 or i < 10000001:
    if prime[i] and N % i == 0:
        print(i)
        N = N / i
        continue
    i += 1
