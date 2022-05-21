import sys
input = sys.stdin.readline

while True:
    brackets = []
    ans = True

    input_str = input().rstrip()
    if input_str == ".":
        exit()

    for character in input_str:
        if character == "(":
            brackets.append(0)
        if character == ")":
            if len(brackets) == 0:
                ans = False
                break
            tmp = brackets.pop()
            if tmp != 0:
                ans = False
                break
        if character == "[":
            brackets.append(1)
        if character == "]":
            if len(brackets) == 0:
                ans = False
                break
            tmp = brackets.pop()
            if tmp != 1:
                ans = False
                break

    if ans and len(brackets) == 0:
        print("yes")
    else:
        print("no")