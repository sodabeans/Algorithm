def solution(s):
    l = [int(_) for _ in s.split()]
    return str(min(l)) + ' ' + str(max(l))
  
