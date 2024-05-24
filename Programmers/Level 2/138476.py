def solution(k, tangerine):
    answer = 0
    tan_dict = [0] * (max(tangerine) + 1)
    for t in tangerine:
        tan_dict[t] += 1
    tan_dict.sort(reverse=True)
    i = 0
    while k > 0:
        k -= tan_dict[i]
        answer += 1
        i += 1
    return answer
