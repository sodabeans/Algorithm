def solution(brown, yellow):
    answer = []
    start = 2
    for i in range(start, brown // 2):
        end = (brown // 2) - i
        if (i - 2) * (end) == yellow:
            answer.append(end + 2)
            answer.append(i)
            break

    return answer
