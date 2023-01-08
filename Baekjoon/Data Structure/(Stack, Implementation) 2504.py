import sys
input = sys.stdin.readline
input_string = input().rstrip()
answer = 0
curr_num = 1
bracket_list = []

for idx in range(len(input_string)):
    curr = input_string[idx]
    if curr == '(':
        curr_num *= 2
        bracket_list.append(curr)
    elif curr == '[':
        curr_num *= 3
        bracket_list.append(curr)
    elif curr == ')':
        if not bracket_list or bracket_list[-1] != '(':
            answer = 0
            break
        if input_string[idx - 1] == '(':
            answer += curr_num
        curr_num //= 2
        bracket_list.pop()
    elif curr == ']':
        if not bracket_list or bracket_list[-1] != '[':
            answer = 0
            break
        if input_string[idx - 1] == '[':
            answer += curr_num
        curr_num //= 3
        bracket_list.pop()

if bracket_list:
    print(0)
else:
    print(answer)
