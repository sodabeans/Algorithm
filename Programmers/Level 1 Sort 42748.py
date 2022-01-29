def solution(array, commands):
    answer = []
    tmp = []
    
    for c in commands:
        i = c[0] - 1
        j = c[1] - 1
        k = c[2] - 1
        for x in range(i, j+1):
            tmp.append(array[x])
        tmp.sort()
        answer.append(tmp[k])
        tmp.clear()
    
    return answer
