def solution(s):
    answer = []
    s = s.split('{')
    s = [(x.rstrip('},')).split(',') for x in s if x]
    s = sorted(s, key=len)
    answer.append(int(s[0][0]))
    for i in range(1, len(s)):
        for j in range(len(s[i])):
            if int(s[i][j]) not in answer:
                answer.append(int(s[i][j]))
                break
    return answer
