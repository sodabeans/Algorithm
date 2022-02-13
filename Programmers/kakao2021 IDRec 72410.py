import re

def solution(new_id):
    
    # 1
    answer = new_id.lower()
    # 2
    answer = re.sub(r'[^\w.-]', '', answer)
    # 3
    answer = re.sub(r'\.{2,}','.', answer)
    # 4
    if answer[0] == '.':
        answer = answer[1:]
    if answer.endswith('.'):
        answer = answer[:-1]
    # 5
    if not answer:
        answer = 'a'
    # 6
    if len(answer) >= 16:
        answer = answer[:15]
    if answer.endswith('.'):
        answer = answer[:-1]
    # 7
    if len(answer) <= 2:
        tmp = answer[-1]
        while len(answer) < 3:
            answer = answer + tmp
    print(answer)
    
    return answer
