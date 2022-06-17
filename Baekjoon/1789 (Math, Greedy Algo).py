import sys
input = sys.stdin.readline

S = int(input())
if S == 1 or S == 2:
    print(1)
    exit()
curr_sum = 1

for i in range(2, S):
    curr_sum += i
    if curr_sum == S:
        print(i)
        exit()
    elif curr_sum > S:
        print(i - 1)
        exit()