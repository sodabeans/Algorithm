import heapq


def solution(n, works):
    answer = 0
    queue = []
    for i in range(len(works)):
        heapq.heappush(queue, -works[i])

    while n and queue:
        curr = heapq.heappop(queue)
        curr += 1
        if curr < 0:
            heapq.heappush(queue, curr)
        n -= 1

    for q in queue:
        answer += q ** 2

    return answer
