def solution(queue1, queue2):
    queue = queue1 + queue2
    target = sum(queue) // 2
    
    head1 = 0
    head2 = len(queue1) - 1
    curr = sum(queue1)
    answer = 0
    
    while True:
        if curr == target:
            return answer
        if head1 >= len(queue) or head2 >= len(queue):
            break
        if curr < target and head2 < len(queue) - 1:  # resolves time-out error
            head2 += 1
            curr += queue[head2]
        else:
            curr -= queue[head1]
            head1 += 1
        answer += 1     
    
    return -1
  
