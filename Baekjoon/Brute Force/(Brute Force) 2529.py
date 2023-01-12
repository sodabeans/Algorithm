from itertools import permutations
import sys
input = sys.stdin.readline

k = int(input())
sign = list(map(str, input().split()))
numbers = [i for i in range(10)]
ans_max = '0'
ans_min = '9876543210'

for opt in permutations(numbers, k + 1):
    flag = False
    curr = ''
    for sign_idx in range(len(sign)):
        if sign[sign_idx] == '<' and opt[sign_idx] < opt[sign_idx + 1]:
            flag = True
            curr += str(opt[sign_idx])
        elif sign[sign_idx] == '>' and opt[sign_idx] > opt[sign_idx + 1]:
            flag = True
            curr += str(opt[sign_idx])
        else:
            flag = False
            break
    if flag:
        curr += str(opt[-1])
        if int(curr) > int(ans_max):
            ans_max = curr
        if int(curr) < int(ans_min):
            ans_min = curr

print(ans_max)
print(ans_min)
