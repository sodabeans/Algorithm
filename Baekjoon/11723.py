import sys
input = sys.stdin.readline

N = int(input())

S = set()

while N != 0:
    N -= 1
    input_string = input().rstrip().split()
    if input_string[0] == 'add':
        S.add(input_string[1])
    elif input_string[0] == 'remove':
        if input_string[1] in S:
            S.remove(input_string[1])
    elif input_string[0] == 'check':
        if input_string[1] in S:
            print(1)
        else:
            print(0)
    elif input_string[0] == 'toggle':
        if input_string[1] in S:
            S.remove(input_string[1])
        else:
            S.add(input_string[1])
    elif input_string[0] == 'all':
        S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    elif input_string[0] == 'empty':
        S = set()
        
