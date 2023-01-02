import sys
input = sys.stdin.readline

# https://www.geeksforgeeks.org/analysis-different-methods-find-prime-number-python/
# Sieve of Eratosthenes (에라토스테네스의 체): fast way to get prime numbers

prime = [True for _ in range(1000001)]

# 2의 배수 걸러내고, 3의 배수 걸러내고, 그 다음에 prime number의 배수 걸러내고...
p = 2
while (p ** 2 <= 1000000):
    if prime[p] == True:
        for i in range(p ** 2, 1000001, p):
            prime[i] = False
    p += 1

while True:
    num = int(input())
    if num == 0:
        break
    
    for i in range(3, num, 2): # check for prime numbers (all are odd)
        if prime[i] and prime[num - i]:
            print("{} = {} + {}".format(num, i, num - i))
            break

    # a = 3
    # b = num - 3

    # while b:
    #     if prime[a] and prime[b]:
    #         break
    #     else:
    #         a += 2
    #         b -= 2
    
    # the problem asked to print this message, but will not be printed anyways
    # if not prime[a]:
    #     print("Goldbach's conjecture is wrong.")
