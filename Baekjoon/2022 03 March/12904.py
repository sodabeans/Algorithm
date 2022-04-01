import sys

input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()
answer = 1

while S != T:
    if len(T) == 0:
        answer = 0
        break
    if T[-1] == 'A':
        T = T[:-1]
    elif T[-1] == 'B':
        T = T[:-1]
        T = T[::-1]
    else:
        break

print(answer)


# def rule_one(input_string):
#     return input_string - 'A'
#
#
# def rule_two(input_string):
#     input_string = input_string - 'B'
#     return input_string[::-1]
