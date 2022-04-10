import sys
input = sys.stdin.readline

N = int(input())
ans = list()

prime = [True for _ in range(1000001)]

p = 2
while (p ** 2 <= 1000000):
    if prime[p] == True:
        for i in range(p ** 2, 1000001, p):
            prime[i] = False
    p += 1

while N > 1:
    for i in range(2, len(prime)):
        if prime[i] and N % i == 0:
            ans.append(i)
            N = N / i
            continue

ans.sort()
for a in ans:
    print(a)
