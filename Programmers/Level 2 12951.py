def solution(s):
    s = s.lower()
    answer = s[0].upper()
    for idx in range(1, len(s)):
        if s[idx - 1] == ' ':
            answer += s[idx].upper()
        else:
            answer += s[idx]
    return answer
  
