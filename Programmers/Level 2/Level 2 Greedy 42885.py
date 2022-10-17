from collections import deque

def solution(people, limit):
    answer = 0
    
    queue = deque(sorted(people))
    while len(queue) > 1:
        largest = queue.pop()
        smallest = queue.popleft()
        if smallest + largest > limit:
            queue.appendleft(smallest)
        answer += 1
    if queue:
        answer += 1
    
    return answer
