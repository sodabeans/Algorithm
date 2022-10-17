from itertools import permutations

def is_prime(num):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    return prime

def solution(numbers):
    answer = 0
    tot_list = []
    
    for i in range(1, len(numbers) + 1):
        perm_list = [int(''.join(n)) for n in permutations([n for n in numbers], i)]
        for p in perm_list:
            tot_list.append(p)
    
    tot_list = list(set(tot_list))
    for t in tot_list:
        if t > 1 and is_prime(t):
            answer = answer + 1
    
    return answer
