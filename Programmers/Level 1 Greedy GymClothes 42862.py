def solution(n, lost, reserve):
    answer = n - len(lost)
    
    lost.sort()
    reserve.sort()
    
    # if in both lost and reserve
    common_set = set(lost) & set(reserve)
    for c in common_set:
        lost.remove(c)
        reserve.remove(c)
        answer = answer + 1
        
    for l in lost:
        if l - 1 in reserve:
            reserve.remove(l - 1)
            answer = answer + 1
        elif l + 1 in reserve:
            reserve.remove(l + 1)
            answer = answer + 1
    
    return answer
