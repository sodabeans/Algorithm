def solution(s):
    answer = True
    p = []
    
    for idx in range(len(s)):
        if s[idx] == '(':
            p.append(1)
        else:
            if p:
                p.pop()
            else:
                answer = False
    if p:
        answer = False

    return answer
    
