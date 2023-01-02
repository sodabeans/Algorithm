import sys
input = sys.stdin.readline

prime = [True for _ in range(10001)]

p = 2
while p ** 2 <= 10000:
    if prime[p]:
        for i in range(p ** 2, 10001, p):
            prime[i] = False
    p += 1

N = int(input())
for _ in range(N):
    input_num = int(input())
    check = input_num // 2
    for i in range(check, 1, -1):
        if prime[i] and prime[input_num - i]:
            print(f'{i} {input_num - i}')
            break