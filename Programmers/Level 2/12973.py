def solution(s):
    stack = []
    i = 0
    
    while i < len(s):
        curr = s[i]
        if len(stack) and stack[-1] == curr:
            stack.pop()
            i += 1
        else:
            stack.append(curr)
            i += 1
        
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0

    return answer
