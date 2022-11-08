def solution(n):
    answer = 0
    for i in range(1, n + 1):
        curr = 0
        start = i
        flag = False
        while curr < n:
            curr += start
            start += 1
            if curr == n:
                flag = True
        if flag:
            answer += 1
    return answer
  
