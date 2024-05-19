def solution(name):
    answer = 0
    n = len(name)
    left_right = n - 1
    
    for i in range(n):
        answer += min(ord(name[i]) - 65, 26 - ord(name[i]) + 65)
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        left_right = min(left_right, 2 * i + (n - next_idx), 2 * (n - next_idx) + i)
        
    return answer + left_right
