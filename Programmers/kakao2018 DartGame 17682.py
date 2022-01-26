# https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    answer = 0
    
    numbers = []
    
    for i in range(len(dartResult)):
        if dartResult[i].isnumeric():
            curr = int(dartResult[i])
            # need to consider 10
            if dartResult[i-1] == '1':
                curr = curr + 10
        elif dartResult[i].isalpha():
            if dartResult[i] == 'D':
                curr = curr ** 2
            elif dartResult[i] == 'T':
                curr = curr ** 3
            numbers.append(curr)
        elif dartResult[i] == '*':
            if len(numbers) > 1:
                # not first score, so need to double both prev and curr
                numbers[-2] = numbers[-2] * 2
            numbers[-1] = numbers[-1] * 2
        elif dartResult[i] == '#':
            numbers[-1] = numbers[-1] * (-1)
    
    answer = sum(numbers)
    
    return answer
