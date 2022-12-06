def solution(n, s):
    answer = []
    if n > s:
        answer.append(-1)
    elif n == s:
        answer.append(s)
    else:
        while n > 1:
            curr = s // n
            answer.append(curr)
            n -= 1
            s -= curr
        answer.append(s)
    answer.sort()
    return answer
