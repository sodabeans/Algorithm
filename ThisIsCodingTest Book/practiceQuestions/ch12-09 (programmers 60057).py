def solution(s):
    answer = len(s)
    for i in range(1, len(s) - 1):
        new_s = ''
        cnt = 1
        curr = s[:i]
        for j in range(i, len(s) + i, i):
            if curr == s[j:j + i]:
                cnt += 1
            else:
                if cnt > 1:
                    new_s += str(cnt) + curr
                else:
                    new_s += curr
                cnt = 1
                curr = s[j:j + i]
        answer = min(len(new_s), answer)
    return answer
