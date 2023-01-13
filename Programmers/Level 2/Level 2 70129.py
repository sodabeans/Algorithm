def solution(s):
    answer = [0, 0]
    while True:
        # step 1 - remove 0 from string
        prev_len = len(s)
        s = s.replace('0', '')
        curr_len = len(s)
        answer[1] += prev_len - curr_len
        # step 2 - length of string to binary
        s = bin(curr_len)[2:]
        answer[0] += 1
        # check if goal is reached
        if s == '1':
            break
    
    return answer
    
