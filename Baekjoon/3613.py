import sys
input = sys.stdin.readline

input_string = input().rstrip('\n')
answer = ''

# all characters AND first is lower case, = Java style
if input_string.isalpha() and input_string[0].islower():
    for i in range(len(input_string)):
        if input_string[i].isupper():
            answer += '_'
        answer += input_string[i]
    print(answer.lower())
else:
    # split when there is underscore
    input_string = input_string.split('_')
    for s in input_string:
        if not s.islower():
            print("Error!")
            sys.exit()
        answer += s.capitalize()
    answer = answer[0].lower() + answer[1:]
    print(answer)
