import sys
input = sys.stdin.readline

N = int(input())

S = [0 for _ in range(20)]

for _ in range(N):
    input_string = input().rstrip()

    # those with only one word
    if input_string == 'all':
        S = [1 for _ in range(20)]
        continue
    elif input_string == 'empty':
        S = [0 for _ in range(20)]
        continue

    # those inputs with one word and one number
    word, num = input_string.split()
    num = int(num) - 1
    if word == 'add':
        S[num] = 1
    elif word == 'remove':
        S[num] = 0
    elif word == 'check':
        if S[num]:
            print(1)
        else:
            print(0)
    elif word == 'toggle':
        if S[num]:
            S[num] = 0
        else:
            S[num] = 1