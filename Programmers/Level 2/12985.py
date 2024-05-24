def solution(n,a,b):
    answer = 1
    
    while answer < n:
        if a % 2 != 0:
            a = (a + 1) // 2
        else:
            a = a // 2
        if b % 2 != 0:
            b = (b + 1) // 2
        else:
            b = b // 2
        if a == b:
            break
        answer += 1
            
    return answer
