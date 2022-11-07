import math

def solution(n, words):
    answer = [0, 0]
    
    curr = words[0][-1]
    for idx in range(1, len(words)):
        if words[idx] in words[0:idx] or curr != words[idx][0]:
            if (idx + 1) % n == 0:
                answer[0] = n
            else:
                answer[0] = (idx + 1) % n
            answer[1] = int(math.ceil((idx + 1) / n))
            break
        else:
            curr = words[idx][-1]
        
    return answer
  
