import sys
input = sys.stdin.readline

input_string = input().rstrip()
stack = []
answer = 0

for idx in range(len(input_string)):
    if input_string[idx] == "(":
        stack.append(idx)
    else:
        if input_string[idx - 1] == "(":  # laser
            stack.pop()
            answer += len(stack)
        else:  # not laser
            answer += 1
            stack.pop()

print(answer)
