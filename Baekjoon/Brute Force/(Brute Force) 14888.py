from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
tot_opr = ['+' for _ in range(add)] + ['-' for _ in range(sub)] + ['*' for _ in range(mul)] + ['/' for _ in range(div)]
operators = set(permutations(tot_opr, N - 1))
ans_min = 1000000000
ans_max = -1000000000

for o in operators:
    curr = A[0]
    for idx in range(N - 1):
        if o[idx] == '+':
            curr += A[idx + 1]
        elif o[idx] == '-':
            curr -= A[idx + 1]
        elif o[idx] == '*':
            curr *= A[idx + 1]
        else:
            if curr < 0:
                curr = -(abs(curr) // A[idx + 1])
            else:
                curr //= A[idx + 1]
    if curr > ans_max:
        ans_max = curr
    if curr < ans_min:
        ans_min = curr

print(ans_max)
print(ans_min)
